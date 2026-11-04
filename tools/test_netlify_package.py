"""Tests for the manual Netlify deploy artifact."""
import tempfile
import unittest
from pathlib import Path
from zipfile import ZipFile

from build_netlify_package import CONTENT_BASE, REDIRECTS, build_package


class NetlifyPackageTest(unittest.TestCase):
    def test_package_is_deploy_ready_and_keeps_content_live(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = build_package(Path(tmp) / 'site.zip')
            with ZipFile(path) as z:
                files = set(z.namelist())
                self.assertTrue({'index.html', 'app.js', 'styles.css', 'ads.txt', '_redirects',
                                 'assets/study-illustration.webp', 'assets/noto-sans-gujarati.ttf'} <= files)
                self.assertFalse(any(name.startswith('data/') for name in files))
                self.assertFalse(any(name.startswith('.git/') or name.endswith('.py') for name in files))
                self.assertEqual(z.read('_redirects').decode(), REDIRECTS)
                self.assertIn(f'href="{CONTENT_BASE}/app/"', z.read('index.html').decode())
                self.assertIn('Netlify hosts this website', z.read('app.js').decode())
                self.assertIn('pub-6133298835140242', z.read('ads.txt').decode())
                self.assertIn('ca-pub-6133298835140242', z.read('index.html').decode())
                self.assertNotIn('pagead2.googlesyndication.com/pagead/js/adsbygoogle.js', z.read('index.html').decode())
                self.assertEqual((z.getinfo('index.html').external_attr >> 16) & 0o777, 0o644)
                self.assertIsNone(z.testzip())

    def test_non_expected_markup_fails_fast(self):
        from build_netlify_package import replace_once
        with self.assertRaises(ValueError):
            replace_once('wrong', 'expected', 'new')


if __name__ == '__main__':
    unittest.main()
