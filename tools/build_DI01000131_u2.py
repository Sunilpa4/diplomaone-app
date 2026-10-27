"""Builds DI01000131 (Computer Programming Fundamentals) Unit 2 JSON + preview. English only."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from subject_DI01000131 import check_and_write
from content_DI01000131_u2_notes_a import NOTES_A
from content_DI01000131_u2_notes_b import NOTES_B
from content_DI01000131_u2_programs import PROGRAMS
from content_DI01000131_u2_extras import SYNTAX, VIVA, EXAM_QS

DIAGRAM_TITLES = {
    "c2_control_tree": {"en": "Classification of Control Statements"},
    "c2_fc_if": {"en": "Flowchart: Simple if"},
    "c2_fc_ifelse": {"en": "Flowchart: if-else"},
    "c2_fc_nested": {"en": "Flowchart: Nested if-else"},
    "c2_fc_ladder": {"en": "Flowchart: else-if Ladder"},
    "c2_fc_switch": {"en": "Flowchart: switch Statement"},
    "c2_loop_types": {"en": "Entry-controlled vs Exit-controlled Loop"},
    "c2_fc_for": {"en": "Flowchart: for Loop"},
    "c2_break_continue": {"en": "break and continue"},
    "c2_fc_reverse": {"en": "Flowchart: Reverse of a Number"},
}

UNIT = {
    "subject": "DI01000131", "unit": 2, "format": "notes",
    "title": {"en": "Decision Making, Branching and Looping"},
    "weightage": 22, "hours": 10,
    "notes": NOTES_A + NOTES_B,
    "programs": PROGRAMS,
    "diagrams": [{"id": k, "title": v, "file": f"diagrams/{k}.svg"} for k, v in DIAGRAM_TITLES.items()],
    "syntax": SYNTAX, "viva": VIVA, "exam_questions": EXAM_QS,
}

if __name__ == "__main__":
    check_and_write(UNIT, DIAGRAM_TITLES, "DI01000131_unit2_preview.html")
