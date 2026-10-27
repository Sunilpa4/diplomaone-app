"""Builds DI02000101 (Scripting Language - Python) Unit 1 JSON + preview. English only."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from subject_DI02000101 import check_and_write
from content_DI02000101_u1_notes_a import NOTES_A
from content_DI02000101_u1_notes_b import NOTES_B
from content_DI02000101_u1_programs import PROGRAMS
from content_DI02000101_u1_extras import SYNTAX, VIVA, EXAM_QS

DIAGRAM_TITLES = {
    "py1_history": {"en": "History of Python"},
    "py1_features": {"en": "Features of Python"},
    "py1_exec": {"en": "How a Python Program is Executed"},
    "py1_structure": {"en": "Basic Structure of a Python Program"},
    "py1_variables": {"en": "Variables and Objects"},
    "py1_io": {"en": "Input and Output"},
    "py1_typecasting": {"en": "Type Conversion"},
    "py1_datatypes": {"en": "Built-in Data Types"},
    "py1_string_index": {"en": "String Indexing and Slicing"},
    "py1_collections": {"en": "List vs Tuple vs Set vs Dictionary"},
}

UNIT = {
    "subject": "DI02000101", "unit": 1, "format": "notes",
    "title": {"en": "Introduction and Syntax of Python Programming"},
    "weightage": 15, "hours": 7,
    "notes": NOTES_A + NOTES_B,
    "programs": PROGRAMS,
    "diagrams": [{"id": k, "title": v, "file": f"diagrams/{k}.svg"} for k, v in DIAGRAM_TITLES.items()],
    "syntax": SYNTAX, "viva": VIVA, "exam_questions": EXAM_QS,
}

if __name__ == "__main__":
    check_and_write(UNIT, DIAGRAM_TITLES, "DI02000101_unit1_preview.html")
