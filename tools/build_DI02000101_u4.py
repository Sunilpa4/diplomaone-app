"""Builds DI02000101 (Scripting Language - Python) Unit 4 JSON + preview. English only."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from subject_DI02000101 import check_and_write
from content_DI02000101_u4_notes_a import NOTES_A
from content_DI02000101_u4_notes_b import NOTES_B
from content_DI02000101_u4_programs import PROGRAMS
from content_DI02000101_u4_extras import SYNTAX, VIVA, EXAM_QS

DIAGRAM_TITLES = {
    "py4_func_types": {"en": "Types of Functions"},
    "py4_conversion": {"en": "Type / Data Conversion Functions"},
    "py4_str_is": {"en": "String Testing Methods"},
    "py4_align": {"en": "Alignment and Strip Methods"},
    "py4_file_modes": {"en": "File Opening Modes"},
    "py4_file_flow": {"en": "Steps of File Handling"},
    "py4_read_methods": {"en": "read() vs readline() vs readlines()"},
    "py4_func_anatomy": {"en": "Defining and Calling a Function"},
    "py4_recursion": {"en": "Recursion: fact(4)"},
    "py4_scope": {"en": "Scope of Variables"},
}

UNIT = {
    "subject": "DI02000101", "unit": 4, "format": "notes",
    "title": {"en": "Python Functions and File Handling"},
    "weightage": 27, "hours": 12,
    "notes": NOTES_A + NOTES_B,
    "programs": PROGRAMS,
    "diagrams": [{"id": k, "title": v, "file": f"diagrams/{k}.svg"} for k, v in DIAGRAM_TITLES.items()],
    "syntax": SYNTAX, "viva": VIVA, "exam_questions": EXAM_QS,
}

if __name__ == "__main__":
    check_and_write(UNIT, DIAGRAM_TITLES, "DI02000101_unit4_preview.html")
