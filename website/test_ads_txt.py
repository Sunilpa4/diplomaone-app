"""Checks for the public AdSense declarations and safe ads.txt updates."""
import unittest
from html.parser import HTMLParser
from pathlib import Path
from merge_ads_txt import merge_ads


ROOT = Path(__file__).resolve().parent
PUBLISHER = 'pub-6133298835140242'


class Metadata(HTMLParser):
    def __init__(self):
        super().__init__()
        self.meta = []

    def handle_starttag(self, tag, attrs):
        if tag == 'meta':
            self.meta.append(dict(attrs))


class AdsDeclarationTest(unittest.TestCase):
    def test_publisher_matches_in_ads_txt_and_html(self):
        records = (ROOT / 'ads.txt').read_text(encoding='utf-8').splitlines()
        self.assertIn(f'google.com, {PUBLISHER}, DIRECT, f08c47fec0942fa0', records)
        parser = Metadata()
        parser.feed((ROOT / 'index.html').read_text(encoding='utf-8'))
        matches = [m['content'] for m in parser.meta if m.get('name') == 'google-adsense-account']
        self.assertEqual(matches, [f'ca-{PUBLISHER}'])

    def test_existing_records_are_preserved_and_not_duplicated(self):
        old = '# existing seller\nother.example, pub-123, DIRECT, abc\n'
        new = (ROOT / 'ads.txt').read_text(encoding='utf-8')
        merged = merge_ads(old, new)
        self.assertTrue(merged.startswith(old))
        self.assertIn(new, merged)
        self.assertEqual(merge_ads(merged, new), merged)
        variant = f'GOOGLE.COM, {PUBLISHER}, direct, f08c47fec0942fa0 # comment\n'
        self.assertEqual(merge_ads(variant, new), variant)

    def test_explicit_retirement_preserves_unrelated_sellers_and_comments(self):
        previous = ('# keep this comment\n'
                    'other.example, pub-123, DIRECT, abc\n'
                    ' GOOGLE.COM , pub-9622139822966375, direct, f08c47fec0942fa0 # old\n')
        additions = (ROOT / 'ads.txt').read_text(encoding='utf-8')
        retirements = (ROOT / 'ads-retired.txt').read_text(encoding='utf-8')
        merged = merge_ads(previous, additions, retirements)
        self.assertIn('# keep this comment', merged)
        self.assertIn('other.example, pub-123, DIRECT, abc', merged)
        self.assertNotIn('pub-9622139822966375', merged)
        self.assertIn(f'google.com, {PUBLISHER}, DIRECT, f08c47fec0942fa0', merged)
        self.assertEqual(merge_ads(merged, additions, retirements), merged)

    def test_cannot_retire_and_add_same_seller(self):
        with self.assertRaises(ValueError):
            merge_ads('', 'google.com, pub-123, DIRECT, abc', 'google.com, pub-123, DIRECT, abc')

    def test_empty_destination_gets_valid_final_newline(self):
        new = (ROOT / 'ads.txt').read_text(encoding='utf-8')
        self.assertEqual(merge_ads('', new), new)


if __name__ == '__main__':
    unittest.main()
