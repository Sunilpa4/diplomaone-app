#!/usr/bin/env python3
"""Verify source excerpt pixels against the unchanged PDFs, without OCR.

Requires tools/paper-card-requirements.txt. Default: every generated excerpt;
--sample checks first/middle/last per paper for a quicker rendering audit.
The normal CI checksum/structure test is tools/test_paper_card_files.py.
"""
from pathlib import Path
import argparse
import json

import pymupdf as fitz
from PIL import Image, ImageChops

ROOT = Path(__file__).resolve().parent.parent / 'papers-upload'


def verify(sample=False):
    records = json.loads((ROOT / 'pdf-card-manifest.json').read_text())['papers']
    checked = 0
    for record in records:
        assets = record['assets']
        if sample:
            assets = [assets[i] for i in sorted({0, len(assets)//2, len(assets)-1})]
        with fitz.open(ROOT / 'papers' / (record['paper'] + '.solution.pdf')) as doc:
            cached_page, page_image = None, None
            for asset in assets:
                if asset['page'] != cached_page:
                    pix = doc[asset['page']-1].get_pixmap(matrix=fitz.Matrix(2, 2), alpha=False)
                    page_image = Image.frombytes('RGB', (pix.width, pix.height), pix.samples)
                    cached_page = asset['page']
                expected = page_image.crop(asset['raster_box'])
                with Image.open(ROOT / 'papers' / asset['path']) as image:
                    actual = image.convert('RGB')
                if actual.size != expected.size or ImageChops.difference(actual, expected).getbbox():
                    raise ValueError('Source pixels changed: ' + asset['path'])
                checked += 1
        print(record['paper'], len(assets), 'lossless source crops verified', flush=True)
    print(checked, 'excerpts match the original PDF rendering pixel for pixel.')
    return checked


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--sample', action='store_true')
    verify(parser.parse_args().sample)
