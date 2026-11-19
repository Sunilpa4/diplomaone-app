"""Verify Mechanical Summer PDF identity and exact, narrowly reviewed changes."""
from pathlib import Path
from hashlib import sha256
import json
import re
import unittest

from publish_solved_papers import validate_solution, validate_asset, reviewed_replacements_manifest

try:
    import pymupdf
except ImportError:
    pymupdf = None

BASE = Path(__file__).resolve().parent.parent / 'papers-upload'


class MechanicalRefreshTest(unittest.TestCase):
    def test_reader_counts_images_exceptions_and_exact_replacement_scope(self):
        records = json.loads((BASE / 'mechanical-refresh-manifest.json').read_text())['papers']
        sources = json.loads((BASE / 'mechanical-refresh-sources.json').read_text())['sources']
        replacements = reviewed_replacements_manifest(BASE / 'reviewed-paper-replacements.json')
        self.assertEqual(len(records), 8)
        self.assertEqual(set(replacements), {Path(s['code']) / 'summer-2026.html' for s in sources})
        exceptions = json.loads((BASE / 'missing-originals.json').read_text())
        self.assertTrue({s['code']+'/winter-2025' for s in sources} <= set(exceptions))
        for record in records:
            path = BASE / 'papers' / (record['paper'] + '.html')
            data = path.read_bytes()
            self.assertEqual(sha256(data).hexdigest(), record['html_sha256'])
            parser = validate_solution(data, path.relative_to(BASE / 'papers'))
            self.assertEqual(parser.details, 28)
            self.assertTrue(parser.english_only)
            self.assertFalse(parser.unsafe)
            assets = record['assets']
            self.assertEqual({a['path'] for a in assets},
                             {str(p.relative_to(BASE / 'papers')) for p in (BASE / 'papers' / (record['paper']+'.assets')).glob('*')})
            for asset in assets:
                image = BASE / 'papers' / asset['path']; image_data = image.read_bytes()
                self.assertEqual(sha256(image_data).hexdigest(), asset['sha256'])
                validate_asset(image, image_data, image.relative_to(BASE / 'papers'))
        audit = json.loads((BASE / 'mechanical-placement-audit.json').read_text())
        mechanical = next(b for b in audit['catalog_snapshot']['branches'] if b['key'] == 'mechanical')
        self.assertEqual(set(audit['mechanical_semester_3_codes']), set(mechanical['semesters']['3']))
        self.assertEqual(len(audit['drive_search_scope']['missing_winter_source_codes']), 2)

    @unittest.skipIf(pymupdf is None, 'Optional pinned PyMuPDF dependency required for PDF identity audit')
    def test_all_six_summer_originals_are_the_correct_exam(self):
        audit = json.loads((BASE / 'mechanical-placement-audit.json').read_text())
        dates = {'DI03000141':'12-05-2026', 'DI03000151':'14-05-2026', 'DI03000161':'18-05-2026',
                 'DI03000171':'20-05-2026', 'DI03000201':'22-05-2026', 'DI03019011':'26-05-2026'}
        for code in audit['mechanical_semester_3_codes']:
            with self.subTest(code=code), pymupdf.open(BASE / 'papers' / code / 'summer-2026.pdf') as pdf:
                text = pdf[0].get_text()
                self.assertIn('SUMMER 2026', text)
                self.assertIn('Subject Code: '+code, text)
                self.assertIn(dates[code], text)
                self.assertIn('SEMESTER - III', text)
                # These originals print common Q1(a),(b) and only a Q1(c) OR.
                q1 = text.split('Q.1', 1)[1].split('Q.2', 1)[0]
                english_parts = re.findall(r'\(([abc])\)', q1)
                self.assertEqual(english_parts[:4], ['a','b','c','c'])


if __name__ == '__main__':
    unittest.main()
