#!/usr/bin/env python3
"""Build a deploy-ready, static Netlify ZIP without bundling stale note data.

The Netlify rewrite serves published note data at /data/. The in-site paper
reader fetches and sanitizes individual question cards and scoped image assets;
PDFs stay optional downloads, never frames. Only the two free subjects' legacy
paper URLs redirect publicly. Paid readers require the separate same-origin API.
"""
from pathlib import Path
from zipfile import ZipFile, ZipInfo, ZIP_DEFLATED
import argparse

ROOT = Path(__file__).resolve().parent.parent
SITE = ROOT / 'website'
CONTENT_BASE = 'https://sunilpa4.github.io/diplomaone-content'
REDIRECTS = (
    f'/data/*  {CONTENT_BASE}/data/:splat  200\n'
    f'/papers/DI01000021/*  {CONTENT_BASE}/papers/DI01000021/:splat  302\n'
    f'/papers/DI01000121/*  {CONTENT_BASE}/papers/DI01000121/:splat  302\n'
    '/papers/*  /index.html  404\n'
)


def replace_once(content, old, new):
    if content.count(old) != 1:
        raise ValueError(f'Expected exactly one occurrence of {old!r}; review Netlify packaging')
    return content.replace(old, new, 1)


def build_package(destination):
    destination = Path(destination).resolve()
    destination.parent.mkdir(parents=True, exist_ok=True)
    index = (SITE / 'index.html').read_text(encoding='utf-8')
    index = replace_once(index, 'href="app/"', f'href="{CONTENT_BASE}/app/"')
    app = (SITE / 'app.js').read_text(encoding='utf-8')
    app = replace_once(app,
        'GitHub Pages hosts this website and its free notes and may receive technical information such as IP addresses to operate and secure its service.',
        'Netlify hosts this website and its same-origin payment API/private delivery. Free notes, Maths-I and Applied Physics are loaded from GitHub Pages. Paid answers never fall back to public files. These service providers may receive technical information such as IP addresses to operate and secure their services.')
    app = replace_once(app,
        'GitHub Pages આ સાઇટ અને મફત નોટ્સ હોસ્ટ કરે છે અને સેવા તથા સુરક્ષા માટે IP એડ્રેસ જેવી ટેકનિકલ માહિતી મેળવી શકે છે.',
        'Netlify આ વેબસાઇટ અને આ જ સાઇટની ચુકવણી API/ખાનગી સામગ્રી હોસ્ટ કરે છે. મફત નોટ્સ, Maths-I અને Applied Physics GitHub Pages પરથી આવે છે. ચૂકવેલા જવાબ માટે જાહેર ફાઇલનો વિકલ્પ વપરાતો નથી. સેવા અને સુરક્ષા માટે આ સેવા પ્રદાતાઓ IP એડ્રેસ જેવી ટેકનિકલ માહિતી મેળવી શકે છે.')
    with ZipFile(destination, 'w', compression=ZIP_DEFLATED, compresslevel=9) as archive:
        def write_text(name, content):
            entry = ZipInfo(name)
            entry.external_attr = 0o100644 << 16
            entry.compress_type = ZIP_DEFLATED
            archive.writestr(entry, content)
        write_text('index.html', index)
        write_text('app.js', app)
        write_text('_redirects', REDIRECTS)
        for name in ('styles.css', 'auth.js', 'ads.txt'):
            archive.write(SITE / name, name)
        for path in sorted((SITE / 'assets').rglob('*')):
            if path.is_file():
                archive.write(path, path.relative_to(SITE).as_posix())
    return destination


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('output', nargs='?', default='release/DiplomaOne-Netlify.zip')
    args = parser.parse_args()
    print(build_package(args.output))
