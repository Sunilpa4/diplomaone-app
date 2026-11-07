import tempfile
import unittest
from pathlib import Path
from index_papers import build_index


class PaperIndexTest(unittest.TestCase):
    def test_discovery_additions_optional_pdf_and_validation(self):
        with tempfile.TemporaryDirectory() as temp:
            papers = Path(temp) / 'papers'
            subject = papers / 'DI03000141'
            subject.mkdir(parents=True)
            valid = '<html><main><details><summary>Question</summary>Answer</details></main></html>'
            (subject / 'summer-2026.html').write_text(valid, encoding='utf-8')
            (subject / 'Question_Paper.pdf').write_bytes(b'%PDF')
            (subject / 'index.html').write_text(valid, encoding='utf-8')
            (subject / 'winter-2026.html').write_text('<main>not a solution</main>', encoding='utf-8')
            index = build_index(papers)
            self.assertEqual(index['subjects']['DI03000141'], [{'session': 'summer-2026', 'pdf': 'Question_Paper.pdf'}])
            # Adding a different subject and a second exam requires no code changes.
            new = papers / 'DI05019011'
            new.mkdir()
            (new / 'winter-2027.html').write_text(valid, encoding='utf-8')
            (new / 'winter-2027.pdf').write_bytes(b'%PDF')
            (subject / 'winter-2026.html').write_text(valid, encoding='utf-8')
            index = build_index(papers)
            self.assertEqual(index['subjects']['DI05019011'], [{'session': 'winter-2027', 'pdf': 'winter-2027.pdf'}])
            self.assertEqual(index['subjects']['DI03000141'], [
                {'session':'winter-2026', 'pdf':None}, {'session':'summer-2026', 'pdf':None}])
            # A legacy PDF may be associated explicitly by the paper itself.
            (subject / 'summer-2026.html').write_text(valid + '<a href="Question_Paper.pdf">original</a>', encoding='utf-8')
            self.assertEqual(build_index(papers)['subjects']['DI03000141'][1]['pdf'], 'Question_Paper.pdf')
            bad = papers / 'not-a-subject'
            bad.mkdir()
            (bad / 'summer-2026.html').write_text(valid, encoding='utf-8')
            self.assertNotIn('not-a-subject', build_index(papers)['subjects'])

    def test_missing_source_is_an_error_not_empty_publication(self):
        with tempfile.TemporaryDirectory() as temp:
            with self.assertRaises(ValueError):
                build_index(Path(temp) / 'missing')


if __name__ == '__main__':
    unittest.main()
