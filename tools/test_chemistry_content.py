"""Regression checks for the imported chemistry courses and app-compatible data."""
import json
import unittest
import xml.etree.ElementTree as ET
from pathlib import Path

from export_app_content import BRANCH_SEMS, SUBJECTS, normalize_for_app

ROOT = Path(__file__).resolve().parent.parent
COURSES = {
    'DI01000161': ('chemical', ['Atomic Structure', 'Electrochemistry', 'Corrosion', 'Water treatment', 'Basic concepts of organic chemistry', 'Lubricants', 'Polymers', 'Additional study topic', 'Additional study topic']),
    'DI01000071': ('electrical', ['Atomic Structure', 'Electrochemistry', 'Corrosion', 'Fuels', 'Lubricants', 'Polymers', 'Electrochemical energy sources', 'Additional study topic', 'Additional study topic']),
}


class ChemistryContentTest(unittest.TestCase):
    def test_branch_registrations(self):
        for branch, semester in [('chemical', 1), ('textile_proc', 1), ('ic', 2), ('textile_mfg', 2), ('robotics', 2), ('printing', 2)]:
            self.assertIn('DI01000161', BRANCH_SEMS[branch][semester])
        for branch, semester in [('electrical', 1), ('it', 1), ('power', 1), ('biomedical', 2), ('computer', 2), ('ec', 2), ('cse', 2), ('ict', 2)]:
            self.assertIn('DI01000071', BRANCH_SEMS[branch][semester])
        self.assertEqual(SUBJECTS['DI01000071'][0], 'Engineering Chemistry')
        self.assertEqual(SUBJECTS['DI01000161'][0], 'Basic Chemistry')

    def test_units_and_diagrams_are_safe_for_existing_readers(self):
        for code, (branch, titles) in COURSES.items():
            folder = ROOT / 'content' / branch / 'sem1' / code
            subject = json.loads((folder / 'subject.json').read_text(encoding='utf-8'))
            self.assertEqual(subject['code'], code)
            self.assertEqual(subject['available_units'], list(range(1, 10)))
            self.assertEqual(sum(u['weightage'] for u in subject['units'][:7]), 100)
            for index, (entry, expected) in enumerate(zip(subject['units'], titles), 1):
                with self.subTest(subject=code, unit=index):
                    self.assertEqual(entry['no'], index)
                    self.assertTrue(entry['title']['en'].startswith(expected))
                    unit = json.loads((folder / entry['file']).read_text(encoding='utf-8'))
                    self.assertEqual((unit['subject'], unit['unit']), (code, index))
                    self.assertEqual(unit['title'], entry['title'])
                    if index > 7:
                        self.assertEqual((entry['hours'], entry['weightage']), (0, 0))
                    self.assertTrue(unit['notes'])
                    self.assertTrue(unit['numericals'])
                    self.assertTrue(unit['viva'][0]['items'])
                    for diagram in unit['diagrams']:
                        self.assertEqual(Path(diagram['file']).stem, diagram['id'])
                        svg = folder / diagram['file']
                        ET.parse(svg)
                    normalize_for_app(unit)
                    self.assertTrue(set(unit['tabs']) <= {'notes', 'diagrams', 'numericals', 'viva', 'exam'})
                    self.assertTrue(all('q' in v and 'a' in v for v in unit['numericals']))
                    self.assertTrue(all('q' in v and 'a' in v for v in unit['viva'][0]['items']))


if __name__ == '__main__':
    unittest.main()
