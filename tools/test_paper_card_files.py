"""Checksum/coverage checks for the reviewed PDF and Electrical question cards.

No OCR or document regeneration in normal publishing. The optional, pinned
rendering dependencies are needed only by prepare_pdf_paper_cards.py; every
published HTML/image byte is checked against its conversion manifest here.
"""
from hashlib import md5, sha256
from html.parser import HTMLParser
from pathlib import Path
import json
import math
import unittest

from publish_solved_papers import validate_solution, validate_asset

ROOT = Path(__file__).resolve().parent.parent / 'papers-upload'
PAPERS = ROOT / 'papers'


def expected_labels(common=False):
    if common:
        return ([f'Q.1 ({i})' for i in range(1, 15)] +
                [f'Q.{q} ({part}) {i}' for q in range(2, 6) for part in 'AB' for i in range(1, 4)])
    return [f'Q.{q} ({part})' + (' OR' if alternative else '')
            for q in range(1, 6)
            for alternative, part in ([(False, 'a'), (False, 'b'), (False, 'c'), (True, 'c')]
                                       if q == 1 else
                                      [(False, 'a'), (False, 'b'), (False, 'c'),
                                       (True, 'a'), (True, 'b'), (True, 'c')])]


class QuestionLabels(HTMLParser):
    def __init__(self):
        super().__init__()
        self.labels = []

    def handle_starttag(self, tag, attrs):
        if tag == 'details':
            self.labels.append(dict(attrs).get('data-question'))


class PaperCardFilesTest(unittest.TestCase):
    def check_images(self, record):
        seen = set()
        for asset in record['assets']:
            path = PAPERS / asset['path']
            self.assertEqual(path.parent, PAPERS / (record['paper'] + '.assets'))
            self.assertNotIn(path, seen)
            seen.add(path)
            self.assertFalse(path.is_symlink())
            data = path.read_bytes()
            self.assertEqual(sha256(data).hexdigest(), asset['sha256'], str(path))
            validate_asset(path, data, path.relative_to(PAPERS))
        self.assertEqual(seen, set((PAPERS / (record['paper'] + '.assets')).glob('*')))

    def test_all_37_pdf_sets_have_real_question_cards_and_originals(self):
        manifest = json.loads((ROOT / 'pdf-card-manifest.json').read_text())
        self.assertEqual(manifest['format'], 'source-pdf-cards-v1')
        records = manifest['papers']
        sources = json.loads((ROOT / 'pdf-card-sources.json').read_text())['sources']
        self.assertEqual(len(records), 37)
        self.assertEqual({r['paper'] for r in records}, set(sources))
        self.assertEqual(sum(len(r['questions']) for r in records), 1076)
        self.assertEqual(sum(len(r['assets']) for r in records), 3129)
        provenance = {e['path']: e for name in ('pdf-batch-provenance.json', 'common-subject-pdf-provenance.json')
                      for e in json.loads((ROOT / name).read_text())}
        for record in records:
            with self.subTest(paper=record['paper']):
                code, _ = record['paper'].split('/')
                pdf = PAPERS / (record['paper'] + '.solution.pdf')
                self.assertEqual(sha256(pdf.read_bytes()).hexdigest(), record['source_sha256'])
                self.assertEqual(record['source_sha256'], provenance['papers/' + record['paper'] + '.solution.pdf']['sha256'])
                self.assertEqual(md5(pdf.read_bytes()).hexdigest(), record['drive_md5'])
                self.assertEqual(record['drive_id'], sources[record['paper']])
                html = PAPERS / (record['paper'] + '.html')
                data = html.read_bytes()
                self.assertEqual(sha256(data).hexdigest(), record['html_sha256'])
                parsed = validate_solution(data, html.relative_to(PAPERS))
                labels = QuestionLabels(); labels.feed(data.decode())
                expected = expected_labels(code in ('DI01000021', 'DI01000121'))
                self.assertEqual(labels.labels, expected)
                self.assertEqual(record['questions'], expected)
                self.assertEqual(record['uncovered_blocks'], [])
                self.assertGreater(record['native_blocks'], 20)
                self.assertGreater(record['source_blocks_covered'], record['native_blocks'])
                self.assertFalse(parsed.unsafe)
                self.assertTrue((PAPERS / (record['paper'] + '.pdf')).is_file())
                self.check_images(record)
                self.assertEqual(record['languages'], ['en'] if code == 'DI01000021' else ['en', 'gu'])
                for asset in record['assets']:
                    self.assertEqual(asset['clip'][0::2], [51.0, 544.0])
                    self.assertGreaterEqual(asset['clip'][1], 39)
                    self.assertLessEqual(asset['clip'][3], 801)
                    self.assertGreater(asset['clip'][3], asset['clip'][1])
                    x0, y0, x1, y1 = asset['clip']
                    self.assertEqual(asset['raster_box'], [math.floor(2*x0), math.floor(2*y0), math.ceil(2*x1), math.ceil(2*y1)])
                    self.assertEqual(asset['width'], 986)
                    self.assertEqual(asset['height'], asset['raster_box'][3]-asset['raster_box'][1])
                    self.assertGreater(asset['height'], 0)
                    self.assertTrue(asset['blocks'])

    def test_12_electrical_sets_keep_source_bytes_and_diagrams(self):
        records = json.loads((ROOT / 'electrical-card-manifest.json').read_text())['papers']
        provenance = json.loads((ROOT / 'electrical-paper-provenance.json').read_text())
        self.assertEqual(len(records), 12)
        self.assertEqual({r['paper'] for r in records}, {p['paper'] for p in provenance})
        self.assertEqual(sum(len(r['questions']) for r in records), 336)
        self.assertEqual(sum(len(r['assets']) for r in records), 271)
        for source in provenance:
            for entry in source['files']:
                data = (ROOT / entry['path']).read_bytes()
                self.assertEqual(md5(data).hexdigest(), entry['md5'], entry['path'])
                self.assertEqual(sha256(data).hexdigest(), entry['sha256'], entry['path'])
        for record in records:
            with self.subTest(paper=record['paper']):
                path = PAPERS / (record['paper'] + '.html'); data = path.read_bytes()
                self.assertEqual(sha256(data).hexdigest(), record['html_sha256'])
                parsed = validate_solution(data, path.relative_to(PAPERS))
                self.assertEqual(parsed.details, 28)
                self.assertGreaterEqual(parsed.en, 28)
                self.assertGreaterEqual(parsed.gu, 28)
                self.assertEqual(record['questions'], expected_labels())
                self.assertFalse(parsed.unsafe)
                self.check_images(record)

    def test_explicit_electrical_errata_are_mathematically_checked(self):
        # These checks apply only to the two labelled review warnings; they do
        # not certify the rest of the owner's supplied educational answers.
        nor = lambda a, b: int(not (a or b))
        for a in (0, 1):
            for b in (0, 1):
                n1, n2 = nor(a, a), nor(b, b)
                n3 = nor(n1, n2)
                self.assertEqual(nor(n3, n3), int(not (a and b)))
                p = nor(a, b); q = nor(a, p); r = nor(b, p); s = nor(q, r)
                self.assertEqual(nor(s, s), a ^ b)
                for c in (0, 1):
                    sop = ((not a and not b) or (not b and c) or (a and b and not c))
                    self.assertEqual(bool(sop), 4*a + 2*b + c in (0, 1, 5, 6))
        html = (PAPERS / 'DI02000161/summer-2026.html').read_text()
        self.assertEqual(html.count('class="note paper-erratum"'), 4)
        self.assertIn('original answer is retained below', html)


if __name__ == '__main__':
    unittest.main()
