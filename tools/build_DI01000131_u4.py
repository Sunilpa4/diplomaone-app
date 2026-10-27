"""Builds DI01000131 (Computer Programming Fundamentals) Unit 4 JSON + preview. English only."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from subject_DI01000131 import check_and_write
from content_DI01000131_u4_notes_a import NOTES_A
from content_DI01000131_u4_notes_b import NOTES_B
from content_DI01000131_u4_programs import PROGRAMS
from content_DI01000131_u4_extras import SYNTAX, VIVA, EXAM_QS

DIAGRAM_TITLES = {
    "c4_func_types": {"en": "Types of Functions"},
    "c4_modular": {"en": "Modular (Top-down) Programming"},
    "c4_elements": {"en": "Elements of a User-defined Function"},
    "c4_call_flow": {"en": "Flow of Control in a Function Call"},
    "c4_value_ref": {"en": "Call by Value vs Call by Reference"},
    "c4_categories": {"en": "Categories of Functions"},
    "c4_pass_array": {"en": "Passing an Array to a Function"},
    "c4_recursion_fact": {"en": "Recursion: fact(4)"},
    "c4_fib_tree": {"en": "Recursion Tree: fib(4)"},
    "c4_scope": {"en": "Scope and Lifetime of Variables"},
}

UNIT = {
    "subject": "DI01000131", "unit": 4, "format": "notes",
    "title": {"en": "User-defined Functions"},
    "weightage": 24, "hours": 10,
    "notes": NOTES_A + NOTES_B,
    "programs": PROGRAMS,
    "diagrams": [{"id": k, "title": v, "file": f"diagrams/{k}.svg"} for k, v in DIAGRAM_TITLES.items()],
    "syntax": SYNTAX, "viva": VIVA, "exam_questions": EXAM_QS,
}

if __name__ == "__main__":
    check_and_write(UNIT, DIAGRAM_TITLES, "DI01000131_unit4_preview.html")
