"""Builds DI01000131 (Computer Programming Fundamentals) Unit 1 JSON + preview."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from subject_DI01000131 import check_and_write
from content_DI01000131_u1_notes_a import NOTES_A
from content_DI01000131_u1_notes_b import NOTES_B
from content_DI01000131_u1_notes_c import NOTES_C
from content_DI01000131_u1_programs import PROGRAMS
from content_DI01000131_u1_extras import SYNTAX, VIVA, EXAM_QS

DIAGRAM_TITLES = {
    "c1_fc_symbols": {"en": "Flowchart Symbols", "gu": "Flowchart Symbols"},
    "c1_fc_sum": {"en": "Flowchart: Sum of Two Numbers", "gu": "Flowchart: બે સંખ્યાઓનો સરવાળો"},
    "c1_fc_largest": {"en": "Flowchart: Largest of Three Numbers", "gu": "Flowchart: ત્રણ સંખ્યાઓમાં સૌથી મોટી"},
    "c1_fc_factorial": {"en": "Flowchart: Factorial of N (Loop)", "gu": "Flowchart: N નો Factorial (Loop)"},
    "c1_structure": {"en": "Basic Structure of a C Program", "gu": "C Program નું મૂળભૂત Structure"},
    "c1_execute": {"en": "Executing a C Program", "gu": "C Program નું Execution"},
    "c1_tokens": {"en": "C Tokens", "gu": "C Tokens"},
    "c1_datatypes": {"en": "Classification of Data Types", "gu": "Data Types નું વર્ગીકરણ"},
    "c1_type_hierarchy": {"en": "Implicit Type Conversion Hierarchy", "gu": "Implicit Type Conversion Hierarchy"},
    "c1_operators": {"en": "Classification of C Operators", "gu": "C Operators નું વર્ગીકરણ"},
}

UNIT = {
    "subject": "DI01000131", "unit": 1, "format": "notes",
    "title": {"en": "Flowchart, Algorithm, Basics of C, Operators", "gu": "Flowchart, Algorithm, C ના મૂળભૂત ખ્યાલો, Operators"},
    "weightage": 20, "hours": 8,
    "notes": NOTES_A + NOTES_B + NOTES_C,
    "programs": PROGRAMS,
    "diagrams": [{"id": k, "title": v, "file": f"diagrams/{k}.svg"} for k, v in DIAGRAM_TITLES.items()],
    "syntax": SYNTAX, "viva": VIVA, "exam_questions": EXAM_QS,
}

if __name__ == "__main__":
    check_and_write(UNIT, DIAGRAM_TITLES, "DI01000131_unit1_preview.html")
