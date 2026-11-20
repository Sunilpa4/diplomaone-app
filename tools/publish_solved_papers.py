#!/usr/bin/env python3
"""Publish FREE paper sets and private-paper listing metadata only.

Paid answer bytes are never copied by the public CLI. Existing public copies
need a separate verified private migration and cleanup before sales can open.
All files, pairs, scoped assets and destinations are checked before any write.
A differing HTML reader may be replaced only with an explicitly passed review
manifest pinning BOTH its previous and incoming SHA-256 hashes. Original PDFs
and images cannot be overwritten. Identical reruns remain safe.
"""
from html.parser import HTMLParser
from hashlib import sha256
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


def reviewed_replacements_manifest(path):
    """Narrow, opt-in authorization to replace a reviewed HTML exam reader."""
    if path is None:
        return {}
    path = Path(path)
    if path.is_symlink() or not path.is_file():
        raise ValueError('Replacement manifest must be a regular file')
    records = json.loads(path.read_text(encoding='utf-8'))
    if not isinstance(records, list):
        raise ValueError('Invalid replacement manifest')
    result = {}
    for record in records:
        if not isinstance(record, dict) or set(record) != {'path', 'old_sha256', 'new_sha256', 'reason', 'source_drive_id'}:
            raise ValueError('Invalid replacement record')
        name = record['path']
        parts = name.split('/') if isinstance(name, str) else []
        if (len(parts) != 2 or not CODE.fullmatch(parts[0]) or not parts[1].endswith('.html')
                or not SESSION.fullmatch(parts[1][:-5])):
            raise ValueError('Only exact subject/session HTML readers may be replaced')
        if any(not isinstance(record[k], str) or not re.fullmatch('[0-9a-f]{64}', record[k]) for k in ('old_sha256', 'new_sha256')):
            raise ValueError('Replacement must pin both SHA-256 hashes')
        if record['old_sha256'] == record['new_sha256']:
            raise ValueError('Replacement hashes must differ')
        if any(not isinstance(record[k], str) or not record[k].strip() for k in ('reason', 'source_drive_id')):
            raise ValueError('Replacement requires a reason and reviewed source identity')
        rel = Path(name)
        if rel in result:
            raise ValueError('Duplicate replacement path')
        result[rel] = record
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


def prepare(source, site, missing_originals=None, replacements=None):
    source = Path(source).resolve()
    site = Path(site).resolve()
    if not source.is_dir() or not site.is_dir():
        raise ValueError('Source papers directory and site checkout must exist')
    exceptions = missing_originals_manifest(missing_originals)
    reviewed = reviewed_replacements_manifest(replacements)
    source_paths = set()
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
        source_paths.add(rel)
        if rel in reviewed and sha256(data).hexdigest() != reviewed[rel]['new_sha256']:
            raise ValueError(f'Incoming reader differs from reviewed replacement: {rel}')
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
        if target.exists():
            if not target.is_file():
                raise ValueError(f'Existing public file differs; refusing to overwrite: {target}')
            existing = target.read_bytes()
            if existing != data and (rel not in reviewed or sha256(existing).hexdigest() != reviewed[rel]['old_sha256']):
                raise ValueError(f'Existing public file differs; refusing to overwrite: {target}')
        files.append((path, target))
    if set(reviewed) - source_paths:
        raise ValueError('Replacement manifest refers to an absent staged reader')
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


def stage_reviewed_files(source, site, missing_originals=None, replacements=None):
    """Private/offline compatibility staging, NOT the public CLI publisher."""
    return _copy_files(prepare(source, site, missing_originals, replacements))


def _copy_files(files):
    changed = []
    for src, target in files:
        exists = target.exists()
        if exists and target.read_bytes() == src.read_bytes():
            continue
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(src, target)
        changed.append(target)
        if target.suffix in ('.html', '.pdf'):
            print(f'{"Replaced reviewed reader" if exists else "Added"} {target}')
    return changed


FREE_PUBLIC_CODES = frozenset({'DI01000021', 'DI01000121'})


def publish(source, site, missing_originals=None, replacements=None):
    """Public-safe only: free papers + filename-sized private product metadata.

    No flag can publish branch-specific answer HTML, images or PDFs. Existing
    public copies are NOT silently deleted: verified private import and an owner
    audit/cleanup are separate launch prerequisites; Git history remains public.
    """
    files = prepare(source, site, missing_originals, replacements)
    root = Path(source).resolve()
    free, metadata = [], {}
    for src, target in files:
        rel = src.relative_to(root)
        if rel.parts[0] in FREE_PUBLIC_CODES:
            free.append((src, target))
        elif len(rel.parts) == 2:
            name = rel.parts[1]
            kind = '.solution.pdf' if name.endswith('.solution.pdf') else src.suffix
            session = name[:-len(kind)]
            destination = target.parent / (session + '.json')
            item = {'version': 1, 'private': True, 'id': rel.parts[0] + '--' + session}
            if destination.is_symlink() or (destination.exists() and not destination.is_file()):
                raise ValueError('Unsafe private listing metadata target')
            if destination.exists():
                existing = json.loads(destination.read_text(encoding='utf-8'))
                if (not isinstance(existing, dict) or any(existing.get(k) != v for k, v in item.items())
                        or not set(existing) <= {'version', 'private', 'id', 'title', 'branch', 'amount', 'currency'}):
                    raise ValueError('Unreviewed existing private listing metadata')
            else:
                metadata[destination] = item
    # Everything, including all metadata targets, was validated before writing.
    changed = _copy_files(free)
    for destination, item in sorted(metadata.items()):
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_text(json.dumps(item, separators=(',', ':')) + '\n', encoding='utf-8')
        changed.append(destination)
    return changed


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('source', type=Path)
    parser.add_argument('site', type=Path)
    parser.add_argument('--missing-originals', type=Path, help='Explicit manifest of reviewed solutions without an original PDF')
    parser.add_argument('--replacements', type=Path, help='Reviewed HTML replacements pinning old/new hashes; no general overwrite flag')
    args = parser.parse_args()
    print(f'{len(publish(args.source, args.site, args.missing_originals, args.replacements))} free files/private listing records added; paid answers were not published. Existing public copies still require migration.')
