"""Regression checks for compatibility with shipped Flutter readers."""
import copy
import unittest

from export_app_content import normalize_for_app


class CompatibilityTest(unittest.TestCase):
    def test_rich_cards_and_flat_entries_are_visible_to_existing_readers(self):
        original = {
            'tabs': ['notes', 'programs', 'diagrams', 'syntax', 'viva', 'exam'],
            'notes': [],
            'programs': [{'format': 'rich_cards', 'title': {'en': 'Practicals'},
                          'items': [{'h': {'en': 'Guide'}, 'body': {'en': 'Content'}, 'diagram': 'ct'}]}],
            'syntax': [{'title': {'en': 'Formula'}, 'body': {'en': 'I = V/R', 'gu': 'સૂત્ર'}}],
            'viva': [{'q': {'en': 'Question'}, 'a': {'en': 'Answer'}}],
        }
        unit = copy.deepcopy(original)
        normalize_for_app(unit)
        self.assertEqual(unit['tabs'], ['notes', 'diagrams', 'viva', 'exam'])
        self.assertEqual(unit['notes'][0]['items'], original['programs'][0]['items'])
        self.assertEqual(unit['notes'][1]['items'][0]['body'], original['syntax'][0]['body'])
        self.assertEqual(unit['viva'][0]['items'], original['viva'])
        self.assertNotIn('programs', unit)
        self.assertNotIn('syntax', unit)

    def test_existing_formats_are_unchanged(self):
        unit = {'tabs': ['notes', 'programs', 'syntax', 'viva'], 'notes': [],
                'programs': [{'id': 'p1', 'code': 'int main() {}'}],
                'syntax': [{'title': {'en': 'Syntax'}, 'items': [{'name': 'if', 'f': 'if'}]}],
                'viva': [{'title': {'en': 'Questions'}, 'items': [{'q': 'Q', 'a': 'A'}]}]}
        expected = copy.deepcopy(unit)
        normalize_for_app(unit)
        self.assertEqual(unit, expected)


if __name__ == '__main__':
    unittest.main()
