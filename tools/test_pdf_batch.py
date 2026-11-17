"""Check that this reviewed batch keeps Drive solution/original bytes unchanged."""
from pathlib import Path
from hashlib import md5, sha256
import json
import unittest

ROOT = Path(__file__).resolve().parent.parent / 'papers-upload'

class PDFBatchTest(unittest.TestCase):
    def test_checksums_and_distinct_pairs(self):
        entries = json.loads((ROOT / 'pdf-batch-provenance.json').read_text())
        self.assertEqual(len(entries), 66)
        pairs = {}
        seen = set()
        for entry in entries:
            rel = Path(entry['path'])
            self.assertEqual(len(rel.parts), 3)
            self.assertEqual(rel.parts[0], 'papers')
            self.assertNotIn(rel.as_posix(), seen)
            seen.add(rel.as_posix())
            data = (ROOT / rel).read_bytes()
            self.assertTrue(data.startswith(b'%PDF-'))
            self.assertEqual(md5(data).hexdigest(), entry['drive_md5'])
            self.assertEqual(sha256(data).hexdigest(), entry['sha256'])
            kind = 'solution' if rel.name.endswith('.solution.pdf') else 'original'
            session = rel.name.removesuffix('.solution.pdf' if kind == 'solution' else '.pdf')
            self.assertIn(kind if kind == 'original' else 'solved', entry['source_name'].lower())
            pairs.setdefault((rel.parts[1], session), {})[kind] = data
        self.assertEqual(len(pairs), 33)
        for pair, docs in pairs.items():
            self.assertEqual(set(docs), {'original', 'solution'}, pair)
            self.assertNotEqual(docs['original'], docs['solution'], pair)

if __name__ == '__main__':
    unittest.main()
