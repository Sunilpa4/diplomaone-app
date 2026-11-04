"""Regression checks for compatibility with shipped Flutter readers."""
import copy
import unittest
import json
from pathlib import Path

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

    def test_recent_subjects_all_export_to_app_readable_groups(self):
        root = Path(__file__).resolve().parent.parent
        directories = [root / 'content/mechanical/sem2/DI02000121',
                       root / 'content/chemical/sem5/DI05005011',
                       root / 'content/chemical/sem5/DI05005021']
        paths = [path for directory in directories for path in sorted(directory.glob('unit*.json'))]
        self.assertEqual(len(paths), 18)
        for path in paths:
            with self.subTest(path=path):
                source = json.loads(path.read_text(encoding='utf-8'))
                unit = copy.deepcopy(source)
                normalize_for_app(unit)
                self.assertIsInstance(unit['viva'], list)
                self.assertEqual(unit['viva'][0], source['viva'])
                self.assertEqual(len(unit['numericals']), len(source['numericals']['items']))
                for result, original in zip(unit['numericals'], source['numericals']['items']):
                    self.assertEqual(result['id'], original['id'])
                    self.assertEqual(result['q'], original['title'])
                    self.assertEqual(result['a'], original['body'])
                original_formulas = source['syntax']['items']
                if original_formulas:
                    self.assertEqual(len(unit['notes'][-1]['items']), len(original_formulas))
                    for result, original in zip(unit['notes'][-1]['items'], original_formulas):
                        self.assertEqual(result['h'], original['name'])
                        self.assertEqual(result['body'], original['body'])
                self.assertNotIn('syntax', unit)
                self.assertNotIn('syntax', unit['tabs'])

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
