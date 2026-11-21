#!/usr/bin/env python3
"""Build ONLY the static publish directory for a Git-connected Netlify deploy.

Server functions and SQL migrations stay outside this directory. This uses the
same reviewed substitutions/content redirects as the manual frontend ZIP; it
never publishes backend/.env, npm dependencies, private imports or paper data.
"""
from pathlib import Path
from tempfile import TemporaryDirectory
from zipfile import ZipFile
import argparse
import shutil
from build_netlify_package import ROOT, build_package

# Explicit review is required to broaden the public surface. In particular,
# silently adding a private file under assets/ must not deploy it as a website.
PUBLIC_FILES = frozenset({
    'index.html', 'app.js', 'auth.js', 'styles.css', 'ads.txt', '_redirects',
    'assets/favicon.svg', 'assets/study-illustration.webp',
    'assets/noto-sans-gujarati.ttf', 'assets/NOTO-SANS-GUJARATI-LICENSE.txt',
    'assets/firebase-auth.js', 'assets/firebase-auth.js.LEGAL.txt',
})


def build_site(destination=None):
    output = Path(destination or ROOT / 'build/netlify-site').resolve()
    build = (ROOT / 'build').resolve()
    if output == build or not output.is_relative_to(build):
        raise ValueError('Publish output must be a child of the ignored repository build/ directory')
    if output.exists():
        shutil.rmtree(output)
    output.mkdir(parents=True)
    with TemporaryDirectory() as tmp:
        with ZipFile(build_package(Path(tmp) / 'frontend.zip')) as archive:
            if set(archive.namelist()) != PUBLIC_FILES:
                raise ValueError('Unexpected or missing public file: review the explicit publish allowlist')
            archive.extractall(output)
    return output


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('output', nargs='?')
    print(build_site(parser.parse_args().output))
