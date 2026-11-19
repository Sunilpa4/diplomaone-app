"""Tests for the manual Netlify deploy artifact."""
import subprocess
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
                self.assertTrue({'index.html', 'app.js', 'auth.js', 'styles.css', 'ads.txt', '_redirects',
                                 'assets/firebase-auth.js', 'assets/firebase-auth.js.LEGAL.txt',
                                 'assets/study-illustration.webp', 'assets/noto-sans-gujarati.ttf'} <= files)
                self.assertFalse(any(name.startswith(('data/', 'auth/', 'scripts/', 'node_modules/')) for name in files))
                self.assertFalse(any(name.startswith('.git/') or name.endswith('.py') for name in files))
                self.assertEqual(z.read('_redirects').decode(), REDIRECTS)
                self.assertEqual(REDIRECTS.splitlines(), [
                    f'/data/*  {CONTENT_BASE}/data/:splat  200',
                    f'/papers/*  {CONTENT_BASE}/papers/:splat  302',
                ])
                packaged_app = Path(tmp) / 'packaged-app.js'
                packaged_app.write_bytes(z.read('app.js'))
                subprocess.run(['node', str(Path(__file__).resolve().parent.parent / 'website' / 'test_paper_links.js'), str(packaged_app)], check=True)
                subprocess.run(['node', str(Path(__file__).resolve().parent.parent / 'website' / 'test_paper_reader.js'), str(packaged_app)], check=True)
                subprocess.run(['node', str(Path(__file__).resolve().parent.parent / 'website' / 'test_card_refresh.js'), str(packaged_app)], check=True)
                subprocess.run(['node', str(Path(__file__).resolve().parent.parent / 'tools' / 'test_mechanical_refresh.js'), str(packaged_app)], check=True)
                subprocess.run(['node', str(Path(__file__).resolve().parent.parent / 'website' / 'test_mechanical_listing.js'), str(packaged_app)], check=True)
                unpacked = Path(tmp) / 'site'
                z.extractall(unpacked)
                subprocess.run(['node', str(Path(__file__).resolve().parent.parent / 'website' / 'test_account.js'), str(unpacked)], check=True)
                subprocess.run(['node', str(Path(__file__).resolve().parent.parent / 'website' / 'test_auth.js'), str(unpacked / 'auth.js')], check=True)
                for name in ('auth.js', 'assets/firebase-auth.js', 'assets/firebase-auth.js.LEGAL.txt'):
                    self.assertEqual(z.read(name), (Path(__file__).resolve().parent.parent / 'website' / name).read_bytes())
                with ZipFile(Path(__file__).resolve().parent.parent / 'DiplomaOne-Netlify.zip') as committed:
                    self.assertEqual(set(committed.namelist()), files, 'Rebuild the committed Netlify ZIP')
                    for name in files:
                        self.assertEqual(committed.read(name), z.read(name), 'Stale Netlify ZIP: ' + name)
                self.assertEqual(z.read('styles.css'), (Path(__file__).resolve().parent.parent / 'website/styles.css').read_bytes())
                packaged_html = z.read('index.html').decode()
                self.assertIn(f'href="{CONTENT_BASE}/app/"', packaged_html)
                self.assertIn('src="auth.js" defer', packaged_html)
                self.assertIn('frame-src https://diplomaone-53b4e.firebaseapp.com/__/auth/;', packaged_html)
                self.assertIn("object-src 'none';", packaged_html)
                self.assertNotIn('<iframe', packaged_html)
                self.assertNotIn('unsafe-eval', packaged_html)
                self.assertIn("img-src 'self' data: https://sunilpa4.github.io/diplomaone-content/papers/;", packaged_html)
                packaged_js = z.read('app.js').decode()
                self.assertIn('Netlify hosts this website', packaged_js)
                self.assertNotIn('paperPdfCard', packaged_js)
                self.assertNotIn('<iframe', packaged_js)
                self.assertIn('paperAssetUrl', packaged_js)
                self.assertIn('bindPaperReader', packaged_js)
                self.assertIn('branchSemesterPaperGroups', packaged_js)
                self.assertIn('paperSets', packaged_js)
                self.assertIn('.paper-image-dialog', z.read('styles.css').decode())
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
