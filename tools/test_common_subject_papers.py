"""Verify the byte-exact Common Subjects papers added from Google Drive."""
from hashlib import md5, sha256
from pathlib import Path
import json
import unittest

ROOT = Path(__file__).resolve().parent.parent / 'papers-upload'
EXPECTED = {
    'papers/DI01000021/summer-2026.pdf': '36a3028eab80233cbeb176b8686a70ec',
    'papers/DI01000021/summer-2026.solution.pdf': '1e96e927c39b11fad70f645487c96f79',
    'papers/DI01000021/winter-2025.pdf': 'e41beeac45ce20ba5ce7098d22d091f9',
    'papers/DI01000021/winter-2025.solution.pdf': '3909193eba8c6c63f63dcbafd9feb977',
    'papers/DI01000121/summer-2026.pdf': '210b0bd6bf1fb5ccc3aba8f6bcae211e',
    'papers/DI01000121/summer-2026.solution.pdf': '9fea72a2027c2a6ae104308ae37b1f64',
    'papers/DI01000121/winter-2025.pdf': 'c5f8ee86279a5ca4d4901441696b2fd4',
    'papers/DI01000121/winter-2025.solution.pdf': '9ea320b3db7df40df80c1df725698342',
}


class CommonSubjectPaperTest(unittest.TestCase):
    def test_drive_checksums_and_complete_distinct_pairs(self):
        entries = json.loads((ROOT / 'common-subject-pdf-provenance.json').read_text(encoding='utf-8'))
        self.assertEqual(len(entries), len(EXPECTED))
        self.assertEqual({entry['path'] for entry in entries}, set(EXPECTED))

        pairs = {}
        seen = set()
        for entry in entries:
            rel = Path(entry['path'])
            self.assertEqual(len(rel.parts), 3)
            self.assertEqual(rel.parts[0], 'papers')
            self.assertNotIn(rel.as_posix(), seen)
            seen.add(rel.as_posix())

            data = (ROOT / rel).read_bytes()
            self.assertTrue(data.startswith(b'%PDF-'), rel)
            self.assertIn(b'%%EOF', data[-2048:], rel)
            self.assertEqual(entry['drive_md5'], EXPECTED[rel.as_posix()], rel)
            self.assertEqual(md5(data).hexdigest(), EXPECTED[rel.as_posix()], rel)
            self.assertEqual(sha256(data).hexdigest(), entry['sha256'], rel)

            kind = 'solution' if rel.name.endswith('.solution.pdf') else 'original'
            self.assertIn('solved' if kind == 'solution' else 'original', entry['source_name'].lower())
            pairs.setdefault((rel.parts[1], rel.name.removesuffix('.solution.pdf').removesuffix('.pdf')), {})[kind] = data

        self.assertEqual(set(pairs), {
            ('DI01000021', 'summer-2026'), ('DI01000021', 'winter-2025'),
            ('DI01000121', 'summer-2026'), ('DI01000121', 'winter-2025'),
        })
        for key, files in pairs.items():
            with self.subTest(pair=key):
                self.assertEqual(set(files), {'original', 'solution'})
                self.assertNotEqual(files['original'], files['solution'])


if __name__ == '__main__':
    unittest.main()
