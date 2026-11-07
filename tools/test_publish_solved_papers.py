import tempfile
import unittest
from pathlib import Path
from publish_solved_papers import prepare, publish


def solution():
    return '<main>' + ''.join('<section>' + ''.join('<details><summary><span class="en">Question</span><span class="gu">પ્રશ્ન</span></summary></details>' for _ in range(28 if i == 0 else 0)) + '</section>' for i in range(5)) + '</main>'


class PublisherTest(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        root = Path(self.temp.name)
        self.src, self.site = root / 'src', root / 'site'
        self.src.mkdir(); self.site.mkdir()
        folder = self.src / '4351902'; folder.mkdir()
        (folder / 'summer-2026.html').write_text(solution(), encoding='utf-8')
        (folder / 'summer-2026.pdf').write_bytes(b'%PDF-1.4\n%%EOF\n')

    def tearDown(self):
        self.temp.cleanup()

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

    def test_destination_symlinks_rejected(self):
        (self.site / 'papers').symlink_to(self.src, target_is_directory=True)
        with self.assertRaisesRegex(ValueError, 'Unsafe target'):
            publish(self.src, self.site)


if __name__ == '__main__':
    unittest.main()
