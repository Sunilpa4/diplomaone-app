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
    def __init__(self):
        super().__init__()
        self.in_main = False
        self.details = 0
        self.sections = 0
        self.en = 0
        self.gu = 0

    def handle_starttag(self, tag, attrs):
        attributes = dict(attrs)
        if tag == 'main':
            self.in_main = True
        elif self.in_main and tag == 'details':
            self.details += 1
        elif self.in_main and tag == 'section':
            self.sections += 1
        if self.in_main:
            classes = (attributes.get('class') or '').split()
            self.en += 'en' in classes
            self.gu += 'gu' in classes

    def handle_endtag(self, tag):
        if tag == 'main':
            self.in_main = False


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
            if parser.sections != 5 or parser.details != 28 or parser.en < 28 or parser.gu < 28:
                raise ValueError(f'Incomplete bilingual solution: {rel}')
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
