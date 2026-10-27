"""Builds DI02000101 (Scripting Language - Python) Unit 2 JSON + preview. English only."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from subject_DI02000101 import check_and_write
from content_DI02000101_u2_notes_a import NOTES_A
from content_DI02000101_u2_notes_b import NOTES_B
from content_DI02000101_u2_programs import PROGRAMS
from content_DI02000101_u2_extras import SYNTAX, VIVA, EXAM_QS

DIAGRAM_TITLES = {
    "py2_operators": {"en": "Types of Operators"},
    "py2_bitwise": {"en": "Bitwise Operators"},
    "py2_identity": {"en": "Identity vs Equality"},
    "py2_precedence": {"en": "Operator Precedence"},
    "py2_fc_ifelse": {"en": "Flowchart: if and if-else"},
    "py2_fc_elif": {"en": "Flowchart: if-elif-else Ladder"},
    "py2_fc_while": {"en": "Flowchart: while Loop"},
    "py2_fc_for": {"en": "Flowchart: for Loop"},
    "py2_range": {"en": "range() Function"},
    "py2_break_continue": {"en": "break vs continue vs pass"},
}

UNIT = {
    "subject": "DI02000101", "unit": 2, "format": "notes",
    "title": {"en": "Operators and Control Flow Structures"},
    "weightage": 18, "hours": 8,
    "notes": NOTES_A + NOTES_B,
    "programs": PROGRAMS,
    "diagrams": [{"id": k, "title": v, "file": f"diagrams/{k}.svg"} for k, v in DIAGRAM_TITLES.items()],
    "syntax": SYNTAX, "viva": VIVA, "exam_questions": EXAM_QS,
}

if __name__ == "__main__":
    check_and_write(UNIT, DIAGRAM_TITLES, "DI02000101_unit2_preview.html")
