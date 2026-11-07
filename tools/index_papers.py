#!/usr/bin/env python3
"""Build the public paper index from existing published solution files.

Input layout: papers/<subject code>/<session>-<year>.html. Optional original
PDFs may use the same basename, or Question_Paper.pdf when unambiguous.
The source files remain untouched. Output is deterministic for quiet reruns.
"""
import argparse
from html.parser import HTMLParser
import json
from pathlib import Path
import re

CODE = re.compile(r'DI[0-9]{8}\Z')
SESSION = re.compile(r'[a-z][a-z0-9]*-[0-9]{4}\Z')


class PaperParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.in_main = 0
        self.has_details = False

    def handle_starttag(self, tag, attrs):
        if tag == 'main':
            self.in_main += 1
        elif tag == 'details' and self.in_main:
            self.has_details = True

    def handle_endtag(self, tag):
        if tag == 'main' and self.in_main:
            self.in_main -= 1


def build_index(papers):
    papers = Path(papers)
    subjects = {}
    if not papers.is_dir():
        raise ValueError(f'Paper directory is missing: {papers}')
    for folder in sorted(papers.iterdir()):
        if folder.is_symlink() or not folder.is_dir() or not CODE.fullmatch(folder.name):
            continue
        valid = {}
        for html in sorted(folder.glob('*.html')):
            if html.is_symlink() or not html.is_file() or not SESSION.fullmatch(html.stem):
                continue
            try:
                if html.stat().st_size > 3_000_000:
                    raise ValueError('larger than 3 MB')
                parser = PaperParser()
                contents = html.read_text(encoding='utf-8')
                parser.feed(contents)
                if not parser.has_details:
                    raise ValueError('missing <main> with <details>')
            except (UnicodeError, ValueError) as error:
                print(f'Skipping incompatible paper {html}: {error}')
                continue
            valid[html.stem] = bool(re.search(r'''href\s*=\s*["'](?:\./)?Question_Paper\.pdf["']''', contents, re.I))
        entries = []
        for session in sorted(valid, key=lambda x: (x[-4:], x), reverse=True):
            named = folder / f'{session}.pdf'
            legacy = folder / 'Question_Paper.pdf'
            pdf = named.name if named.is_file() and not named.is_symlink() else None
            if not pdf and (len(valid) == 1 or valid[session]) and legacy.is_file() and not legacy.is_symlink():
                pdf = legacy.name
            entries.append({'session': session, 'pdf': pdf})
        if entries:
            subjects[folder.name] = entries
    return {'version': 1, 'subjects': subjects}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('papers', type=Path)
    args = parser.parse_args()
    result = build_index(args.papers)
    target = args.papers / 'index.json'
    target.write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(f'Indexed {sum(map(len, result["subjects"].values()))} papers in {len(result["subjects"])} subjects: {target}')


if __name__ == '__main__':
    main()
