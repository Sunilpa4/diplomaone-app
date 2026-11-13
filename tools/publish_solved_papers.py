#!/usr/bin/env python3
"""Copy compatible uploaded paper sets into a public checkout, without overwrites.

All source files and existing destinations are checked before any write. Running
again with identical content is safe; differing public files require review.
"""
from html.parser import HTMLParser
from pathlib import Path
import argparse
import re
import shutil

CODE = re.compile(r'(?:DI[0-9]{8}|[0-9]{7})\Z')
SESSION = re.compile(r'[a-z][a-z0-9]*-[0-9]{4}\Z')


class SolutionParser(HTMLParser):
    """Structure of one solved-paper document.

    The shape is read from the paper itself: sections are the printed questions,
    every <details> is one answer part (an OR alternative is its own part). The
    publisher therefore does not assume one fixed question pattern; it checks
    that the document is complete and self-consistent.
    """

    def __init__(self):
        super().__init__()
        self.in_main = False
        self.main_closed = False
        self.details = 0
        self.summaries = 0
        self.sections = 0
        self.parts_per_section = []
        self.en = 0
        self.gu = 0
        self.english_only = False
        self.document_language = None

    def handle_starttag(self, tag, attrs):
        attributes = dict(attrs)
        if tag == 'html':
            self.document_language = attributes.get('lang')
        if tag == 'meta' and attributes.get('name') == 'paper-language' and attributes.get('content') == 'en-only':
            self.english_only = True
        if tag == 'main':
            self.in_main = True
        elif self.in_main and tag == 'section':
            self.sections += 1
            self.parts_per_section.append(0)
        elif self.in_main and tag == 'summary':
            self.summaries += 1
        elif self.in_main and tag == 'details':
            self.details += 1
            if self.parts_per_section:
                self.parts_per_section[-1] += 1
        if self.in_main:
            classes = (attributes.get('class') or '').split()
            self.en += 'en' in classes
            self.gu += 'gu' in classes

    def handle_endtag(self, tag):
        if tag == 'main':
            self.in_main = False
            self.main_closed = True

    def check(self, path):
        """Return the paper's structure, or raise ValueError describing the first fault."""
        if not self.main_closed:
            raise ValueError(f'Solution has no closed <main>: {path}')
        if self.sections < 1:
            raise ValueError(f'Solution has no question section: {path}')
        if self.details < 1:
            raise ValueError(f'Solution has no answer part: {path}')
        empty = [i + 1 for i, count in enumerate(self.parts_per_section) if not count]
        if empty:
            raise ValueError(f'Solution section(s) {empty} have no answer part: {path}')
        bilingual = self.en == self.gu and self.en > 0 and not self.english_only
        english_only = (self.english_only and self.document_language == 'en'
                        and self.en == 0 and self.gu == 0)
        if not (bilingual or english_only):
            if self.english_only:
                raise ValueError(f'English-only marker must use lang="en" and no .en/.gu spans: {path}')
            raise ValueError(f'Incomplete bilingual solution: {self.en} English and {self.gu} '
                             f'Gujarati blocks across {self.details} parts: {path}')
        if self.summaries != self.details:
            raise ValueError(f'Every answer part needs its own <summary>: {self.summaries} '
                             f'summaries for {self.details} parts: {path}')
        return {'sections': self.sections, 'parts': self.details,
                'parts_per_section': self.parts_per_section, 'bilingual': bilingual}


def prepare(source, site):
    source = Path(source).resolve()
    site = Path(site).resolve()
    if not source.is_dir() or not site.is_dir():
        raise ValueError('Source papers directory and site checkout must exist')
    files = []
    pairs = {}
    for path in sorted(source.rglob('*')):
        if path.is_symlink():
            raise ValueError(f'Symlinks are not allowed: {path}')
        if path.is_dir():
            continue
        rel = path.relative_to(source)
        if len(rel.parts) != 2 or not CODE.fullmatch(rel.parts[0]) or path.suffix not in ('.html', '.pdf') or not SESSION.fullmatch(path.stem):
            raise ValueError(f'Unexpected paper path: {rel}')
        data = path.read_bytes()
        if path.suffix == '.html':
            if len(data) > 3_000_000:
                raise ValueError(f'Solution is too large: {rel}')
            parser = SolutionParser()
            parser.feed(data.decode('utf-8'))
            parser.check(rel)
        elif not data.startswith(b'%PDF-') or b'%%EOF' not in data[-2048:]:
            raise ValueError(f'Invalid PDF: {rel}')
        pairs.setdefault((rel.parts[0], path.stem), set()).add(path.suffix)
        target = site / 'papers' / rel
        # Do not follow an existing symlink, even if it points back inside the checkout.
        if (site / 'papers').is_symlink() or target.parent.is_symlink() or target.is_symlink():
            raise ValueError(f'Unsafe target: {target}')
        if not target.resolve().is_relative_to(site):
            raise ValueError(f'Target escapes site: {target}')
        if target.exists() and (not target.is_file() or target.read_bytes() != data):
            raise ValueError(f'Existing public file differs; refusing to overwrite: {target}')
        files.append((path, target))
    if not files or any(extensions != {'.html', '.pdf'} for extensions in pairs.values()):
        raise ValueError('Every solution needs a matching original PDF')
    return files


def publish(source, site):
    files = prepare(source, site)
    added = []
    for src, target in files:
        if target.exists():
            print(f'Preserving identical file {target}')
            continue
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(src, target)
        added.append(target)
        print(f'Added {target}')
    return added


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('source', type=Path)
    parser.add_argument('site', type=Path)
    args = parser.parse_args()
    print(f'{len(publish(args.source, args.site))} files added; existing files preserved.')
