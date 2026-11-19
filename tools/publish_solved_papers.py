#!/usr/bin/env python3
"""Copy compatible uploaded paper sets and scoped images, without overwrites.

All source files, referenced assets, pairs and existing destinations are checked
before any write. Running again with identical content is safe; differing public
files still require review. Adding HTML alongside a solution PDF changes only
its default presentation: the byte-exact PDFs remain optional downloads.
"""
from html.parser import HTMLParser
from pathlib import Path
import argparse
import json
import re
import shutil
import struct

CODE = re.compile(r'(?:DI[0-9]{8}|[0-9]{7})\Z')
SESSION = re.compile(r'[a-z][a-z0-9]*-[0-9]{4}\Z')
ASSET = re.compile(r'[0-9]{4}\.(?:webp|png)\Z')
EMBEDDED_IMAGE = re.compile(r'data:image/(?:png|jpeg|gif|webp);base64,[a-z0-9+/=\s]+\Z', re.I)
CARD_LAYOUTS = {'source-pdf-cards-v1', 'source-html-cards-v1'}


class SolutionParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.in_main = False
        self.details = 0
        self.sections = 0
        self.en = 0
        self.gu = 0
        self.english_only = False
        self.document_language = None
        self.layout = None
        self.declared_count = None
        self.images = []
        self.cards = []
        self.current_card = None
        self.unsafe = False

    def handle_starttag(self, tag, attrs):
        attributes = dict(attrs)
        if tag == 'html':
            self.document_language = attributes.get('lang')
        if tag == 'meta':
            name, value = attributes.get('name'), attributes.get('content')
            if name == 'paper-language' and value == 'en-only':
                self.english_only = True
            elif name == 'paper-layout':
                self.layout = value
            elif name == 'paper-question-count':
                self.declared_count = value
        if tag == 'main':
            self.in_main = True
        elif self.in_main and tag == 'details':
            self.details += 1
            if self.current_card is not None:
                self.unsafe = True
            self.current_card = {'summary': 0, 'answer': 0, 'en': 0, 'gu': 0}
            self.cards.append(self.current_card)
        elif self.in_main and tag == 'section':
            self.sections += 1
        if self.in_main:
            classes = (attributes.get('class') or '').split()
            self.en += 'en' in classes
            self.gu += 'gu' in classes
            if tag == 'img':
                self.images.append(attributes.get('src', ''))
            if self.current_card is not None:
                self.current_card['summary'] += tag == 'summary'
                for name in ('en', 'gu', 'answer'):
                    self.current_card[name] += name in classes
            if tag in ('script', 'iframe', 'object', 'embed', 'style', 'form'):
                self.unsafe = True
            if any(name.lower().startswith('on') for name in attributes):
                self.unsafe = True

    def handle_endtag(self, tag):
        if tag == 'main':
            self.in_main = False
        elif tag == 'details':
            self.current_card = None


def missing_originals_manifest(path):
    """Explicit, reviewed exceptions: solutions whose source question PDF is absent."""
    if path is None:
        return set()
    path = Path(path)
    if path.is_symlink() or not path.is_file():
        raise ValueError('Missing-originals manifest must be a regular file')
    items = json.loads(path.read_text(encoding='utf-8'))
    if not isinstance(items, list) or any(not isinstance(x, str) for x in items) or len(items) != len(set(items)):
        raise ValueError('Invalid missing-originals manifest')
    result = set()
    for item in items:
        parts = item.split('/')
        if len(parts) != 2 or not CODE.fullmatch(parts[0]) or not SESSION.fullmatch(parts[1]):
            raise ValueError('Invalid missing-originals entry: ' + item)
        result.add((parts[0], parts[1]))
    return result


def validate_asset(path, data, rel):
    if len(data) > 2_000_000:
        raise ValueError(f'Paper image is too large: {rel}')
    if path.suffix == '.png':
        valid = (len(data) >= 45 and data.startswith(b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR')
                 and data.endswith(b'\x00\x00\x00\x00IEND\xaeB`\x82')
                 and all(0 < n <= 10000 for n in struct.unpack('>II', data[16:24])))
    else:
        valid = (len(data) >= 20 and data[:4] == b'RIFF' and data[8:12] == b'WEBP'
                 and data[12:16] in (b'VP8L', b'VP8 ', b'VP8X')
                 and int.from_bytes(data[4:8], 'little') + 8 == len(data))
    if not valid:
        raise ValueError(f'Invalid paper image: {rel}')


def validate_solution(data, rel):
    if len(data) > 3_000_000:
        raise ValueError(f'Solution is too large: {rel}')
    parser = SolutionParser()
    parser.feed(data.decode('utf-8'))
    common = (rel.parts[0] in ('DI01000021', 'DI01000121') and
              parser.layout == 'source-pdf-cards-v1' and parser.declared_count == '38')
    count = 38 if common else 28
    bilingual = parser.en >= count and parser.gu >= count and not parser.english_only
    english_only = (parser.english_only and parser.document_language == 'en'
                    and parser.en == 0 and parser.gu == 0)
    if parser.sections != 5 or parser.details != count or not (bilingual or english_only):
        raise ValueError(f'Incomplete bilingual solution or invalid English-only solution: {rel}')
    if parser.layout in CARD_LAYOUTS:
        if parser.unsafe or any(card['summary'] != 1 or card['answer'] != 1 or
                               (bilingual and (not card['en'] or not card['gu']))
                               for card in parser.cards):
            raise ValueError(f'Incomplete or unsafe question cards: {rel}')
    return parser


def prepare(source, site, missing_originals=None):
    source = Path(source).resolve()
    site = Path(site).resolve()
    if not source.is_dir() or not site.is_dir():
        raise ValueError('Source papers directory and site checkout must exist')
    exceptions = missing_originals_manifest(missing_originals)
    files, pairs, assets, required_assets = [], {}, set(), set()
    for path in sorted(source.rglob('*')):
        if path.is_symlink():
            raise ValueError(f'Symlinks are not allowed: {path}')
        if path.is_dir():
            continue
        rel = path.relative_to(source)
        if not CODE.fullmatch(rel.parts[0]):
            raise ValueError(f'Unexpected paper path: {rel}')
        data = path.read_bytes()
        if (len(rel.parts) == 3 and rel.parts[1].endswith('.assets')
                and SESSION.fullmatch(rel.parts[1][:-7]) and ASSET.fullmatch(rel.name)):
            validate_asset(path, data, rel)
            assets.add(rel)
        else:
            if len(rel.parts) != 2:
                raise ValueError(f'Unexpected paper path: {rel}')
            kind = '.solution.pdf' if path.name.endswith('.solution.pdf') else path.suffix
            session = path.name[:-len(kind)] if kind in ('.html', '.pdf', '.solution.pdf') else ''
            if not SESSION.fullmatch(session):
                raise ValueError(f'Unexpected paper path: {rel}')
            if path.suffix == '.html':
                parser = validate_solution(data, rel)
                for src in parser.images:
                    if len(src) <= 1_200_000 and EMBEDDED_IMAGE.fullmatch(src):
                        continue
                    parts = src.split('/')
                    if len(parts) != 2 or parts[0] != session + '.assets' or not ASSET.fullmatch(parts[1]):
                        raise ValueError(f'Unscoped paper image reference: {rel}: {src[:100]}')
                    required_assets.add(Path(rel.parts[0]) / src)
            elif not data.startswith(b'%PDF-') or b'%%EOF' not in data[-2048:]:
                raise ValueError(f'Invalid PDF: {rel}')
            pairs.setdefault((rel.parts[0], session), set()).add(kind)
        target = site / 'papers' / rel
        # Check every ancestor, including nested asset directories. Do not
        # follow even an existing symlink pointing back inside this checkout.
        ancestors = [parent for parent in target.parents if parent != site and parent.is_relative_to(site)]
        if target.is_symlink() or any(parent.is_symlink() or (parent.exists() and not parent.is_dir()) for parent in ancestors):
            raise ValueError(f'Unsafe target: {target}')
        if not target.resolve().is_relative_to(site):
            raise ValueError(f'Target escapes site: {target}')
        if target.exists() and (not target.is_file() or target.read_bytes() != data):
            raise ValueError(f'Existing public file differs; refusing to overwrite: {target}')
        files.append((path, target))
    if assets != required_assets:
        raise ValueError('Missing or unreferenced paper images: ' + str(sorted(assets ^ required_assets)))
    if not pairs:
        raise ValueError('Every solution needs a matching original PDF')
    missing = {pair for pair, extensions in pairs.items() if extensions == {'.html'}}
    allowed = ({'.html'}, {'.html', '.pdf'}, {'.pdf', '.solution.pdf'}, {'.html', '.pdf', '.solution.pdf'})
    if any(extensions not in allowed for extensions in pairs.values()) or missing != exceptions:
        raise ValueError('Every solution needs a matching original PDF or a matching reviewed exception')
    for (code, session), extensions in pairs.items():
        if '.solution.pdf' in extensions:
            if (source / code / (session + '.solution.pdf')).read_bytes() == (source / code / (session + '.pdf')).read_bytes():
                raise ValueError(f'Solution and original must be different PDFs: {code}/{session}')
            # A PDF-only set must not silently change the presentation of an existing HTML paper.
            if '.html' not in extensions and (site / 'papers' / code / (session + '.html')).exists():
                raise ValueError(f'Existing HTML requires review: {code}/{session}')
    return files


def publish(source, site, missing_originals=None):
    files = prepare(source, site, missing_originals)
    added = []
    for src, target in files:
        if target.exists():
            continue
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(src, target)
        added.append(target)
        if target.suffix in ('.html', '.pdf'):
            print(f'Added {target}')
    return added


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('source', type=Path)
    parser.add_argument('site', type=Path)
    parser.add_argument('--missing-originals', type=Path, help='Explicit manifest of reviewed solutions without an original PDF')
    args = parser.parse_args()
    print(f'{len(publish(args.source, args.site, args.missing_originals))} files added; existing files preserved.')
