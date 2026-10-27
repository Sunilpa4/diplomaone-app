"""Builds DI01000131 (Computer Programming Fundamentals) Unit 5 JSON + preview. English only."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from subject_DI01000131 import check_and_write
from content_DI01000131_u5_notes_a import NOTES_A
from content_DI01000131_u5_notes_b import NOTES_B
from content_DI01000131_u5_programs import PROGRAMS
from content_DI01000131_u5_extras import SYNTAX, VIVA, EXAM_QS

DIAGRAM_TITLES = {
    "c5_string_memory": {"en": "String in Memory"},
    "c5_read_methods": {"en": "Reading a String: Methods"},
    "c5_str_funcs": {"en": "Important String Functions"},
    "c5_strcmp": {"en": "How strcmp() Works"},
    "c5_str_array": {"en": "Array of Strings"},
    "c5_cmdline": {"en": "Command Line Arguments"},
    "c5_file_io": {"en": "File Input/Output in C"},
    "c5_file_modes": {"en": "File Opening Modes"},
    "c5_file_funcs": {"en": "File I/O Functions"},
    "c5_fc_copy": {"en": "Flowchart: Copy a File"},
}

UNIT = {
    "subject": "DI01000131", "unit": 5, "format": "notes",
    "title": {"en": "Character Arrays, Strings and Files"},
    "weightage": 14, "hours": 9,
    "notes": NOTES_A + NOTES_B,
    "programs": PROGRAMS,
    "diagrams": [{"id": k, "title": v, "file": f"diagrams/{k}.svg"} for k, v in DIAGRAM_TITLES.items()],
    "syntax": SYNTAX, "viva": VIVA, "exam_questions": EXAM_QS,
}

if __name__ == "__main__":
    check_and_write(UNIT, DIAGRAM_TITLES, "DI01000131_unit5_preview.html")
