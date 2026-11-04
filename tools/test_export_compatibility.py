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

    def test_exam_questions_tab_alias_is_visible_without_duplicates(self):
        unit = {'tabs': ['notes', 'exam_questions', 'exam'], 'exam_questions': [{'q': 'Q', 'marks': 2}]}
        normalize_for_app(unit)
        self.assertEqual(unit['tabs'], ['notes', 'exam'])
        self.assertEqual(unit['exam_questions'][0]['marks'], 2)

    def test_single_group_rich_fields_are_compatible_and_preserved(self):
        unit = {
            'tabs': ['notes', 'numericals', 'syntax', 'viva', 'exam'],
            'notes': [],
            'numericals': {'title': {'en': 'Solved'}, 'items': [
                {'id': 'n1', 'title': {'en': 'Example', 'gu': 'દાખલો'},
                 'body': {'en': '<p>Solution</p>', 'gu': '<p>ઉકેલ</p>'}}]},
            'syntax': {'title': {'en': 'Formulae'}, 'items': [
                {'name': {'en': 'Efficiency'}, 'body': {'en': '<p>E = x/y</p>'}, 'diagram': 'fig'}]},
            'viva': {'title': {'en': 'Questions'}, 'items': [
                {'q': {'en': 'Q'}, 'a': {'en': 'A'}}]},
        }
        original = copy.deepcopy(unit)
        normalize_for_app(unit)
        self.assertEqual(unit['numericals'][0]['id'], 'n1')
        self.assertEqual(unit['numericals'][0]['q'], original['numericals']['items'][0]['title'])
        self.assertEqual(unit['numericals'][0]['a'], original['numericals']['items'][0]['body'])
        self.assertEqual(unit['notes'][0]['items'][0]['h'], original['syntax']['items'][0]['name'])
        self.assertEqual(unit['notes'][0]['items'][0]['body'], original['syntax']['items'][0]['body'])
        self.assertEqual(unit['notes'][0]['items'][0]['diagram'], 'fig')
        self.assertEqual(unit['viva'], [original['viva']])
        self.assertEqual(unit['tabs'], ['notes', 'numericals', 'viva', 'exam'])
        self.assertNotIn('syntax', unit)

    def test_unrecognized_rich_group_fails_instead_of_losing_notes(self):
        for name in ('syntax', 'viva', 'numericals'):
            with self.subTest(name=name), self.assertRaises(ValueError):
                normalize_for_app({name: {'items': [{'unexpected': 'content'}]}})

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
