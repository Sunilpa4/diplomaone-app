import tempfile
import unittest
from pathlib import Path
from publish_solved_papers import prepare, publish


def parts(n, bilingual=True):
    if bilingual:
        body = '<details><summary><span class="en">Question</span><span class="gu">પ્રશ્ન</span></summary></details>'
    else:
        body = '<details><summary>Question</summary><div>Answer</div></details>'
    return body * n


def solution(pattern=(28,), bilingual=True):
    return '<main>' + ''.join(f'<section>{parts(n, bilingual)}</section>' for n in pattern) + '</main>'


class PublisherTest(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        root = Path(self.temp.name)
        self.src, self.site = root / 'src', root / 'site'
        self.src.mkdir(); self.site.mkdir()
        folder = self.src / '4351902'; folder.mkdir()
        (folder / 'summer-2026.html').write_text(solution((28,)), encoding='utf-8')
        (folder / 'summer-2026.pdf').write_bytes(b'%PDF-1.4\n%%EOF\n')

    def tearDown(self):
        self.temp.cleanup()

    def write(self, text):
        (self.src / '4351902' / 'summer-2026.html').write_text(text, encoding='utf-8')

    def test_additive_and_idempotent(self):
        other = self.site / 'papers' / 'DI03000141' / 'old.html'
        other.parent.mkdir(parents=True); other.write_text('preserve')
        self.assertEqual(len(publish(self.src, self.site)), 2)
        self.assertEqual(len(publish(self.src, self.site)), 0)
        self.assertEqual(other.read_text(), 'preserve')

    def test_conflicts_abort_before_any_write(self):
        target = self.site / 'papers' / '4351902' / 'summer-2026.pdf'
        target.parent.mkdir(parents=True); target.write_bytes(b'existing')
        with self.assertRaisesRegex(ValueError, 'refusing to overwrite'):
            publish(self.src, self.site)
        self.assertEqual(target.read_bytes(), b'existing')
        self.assertFalse((target.parent / 'summer-2026.html').exists())

    def test_malformed_and_missing_files_rejected(self):
        (self.src / '4351902' / 'summer-2026.pdf').unlink()
        with self.assertRaisesRegex(ValueError, 'matching original PDF'):
            prepare(self.src, self.site)
        (self.src / '4351902' / 'summer-2026.pdf').write_bytes(b'not a pdf')
        with self.assertRaisesRegex(ValueError, 'Invalid PDF'):
            prepare(self.src, self.site)

    def test_any_paper_pattern_is_accepted(self):
        # The shape comes from the paper, not from a fixed 4+6+6+6+6 template.
        for pattern in ((28,), (15,), (6, 6, 6, 6, 6), (4, 6, 6, 6, 6), (12,), (10, 10)):
            self.write(solution(pattern))
            self.assertEqual(len(prepare(self.src, self.site)), 2, pattern)

    def test_incomplete_structure_rejected(self):
        cases = {
            '<main><section><details><summary><span class="en">Q</span><span class="gu">પ્ર</span></summary></details></section>': 'no closed <main>',
            '<main></main>': 'no question section',
            '<main><section><h2>Q1</h2></section></main>': 'no answer part',
            '<main><section><details><summary><span class="en">Q</span><span class="gu">પ્ર</span></summary></details></section><section><h2>Q2</h2></section></main>': r'section\(s\) \[2\] have no answer part',
            '<main><section><details><summary><span class="en">Q</span></summary></details></section></main>': 'Incomplete bilingual solution',
            '<main><section><details><summary><span class="en">Q</span><span class="gu">પ્ર</span><span class="gu">પ્ર</span></summary></details></section></main>': 'Incomplete bilingual solution',
        }
        for text, message in cases.items():
            self.write(text)
            with self.assertRaisesRegex(ValueError, message):
                prepare(self.src, self.site)

    def test_explicit_english_only(self):
        english = ('<html lang="en"><head><meta name="paper-language" content="en-only"></head><main>'
                   + f'<section>{parts(28, bilingual=False)}</section>' + '</main></html>')
        self.write(english)
        self.assertEqual(len(prepare(self.src, self.site)), 2)
        for invalid, message in (
            (english.replace('en-only', 'en'), 'Incomplete bilingual solution'),
            (english.replace('lang="en"', 'lang="gu"'), 'must use lang="en"'),
            (english.replace('<details>', '<details class="en">', 1), 'must use lang="en"'),
            # A part replaced by a non-<details> wrapper breaks the part/summary pairing.
            (english.replace('<details>', '<div>', 1), 'needs its own <summary>'),
        ):
            self.write(invalid)
            with self.assertRaisesRegex(ValueError, message):
                prepare(self.src, self.site)

    def test_destination_symlinks_rejected(self):
        (self.site / 'papers').symlink_to(self.src, target_is_directory=True)
        with self.assertRaisesRegex(ValueError, 'Unsafe target'):
            publish(self.src, self.site)


if __name__ == '__main__':
    unittest.main()
