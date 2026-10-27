"""Builds DI03000031 (RDBMS) Unit 5 JSON + preview. English only, PL/SQL and triggers."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from subject_DI03000031 import check_and_write
from content_DI03000031_u5_notes import NOTES
from content_DI03000031_u5_programs import PROGRAMS
from content_DI03000031_u5_extras import SYNTAX, VIVA, EXAM_QS

DIAGRAM_TITLES = {
    "db5_block": {"en": "PL/SQL Block Structure"},
    "db5_engine": {"en": "PL/SQL Engine"},
    "db5_type_rowtype": {"en": "%TYPE and %ROWTYPE"},
    "db5_if": {"en": "IF-THEN-ELSIF-ELSE Flow"},
    "db5_loops": {"en": "Loops in PL/SQL"},
    "db5_cursor": {"en": "Cursor: Context Area and Active Set"},
    "db5_cursor_steps": {"en": "Explicit Cursor: Four Steps"},
    "db5_exceptions": {"en": "Types of Exceptions"},
    "db5_proc_func": {"en": "Procedure vs Function"},
    "db5_trigger_flow": {"en": "How a Trigger Fires"},
    "db5_trigger_types": {"en": "Types of Triggers"},
}

UNIT = {
    "subject": "DI03000031", "unit": 5, "format": "notes",
    "title": {"en": "PL/SQL and Triggers"},
    "weightage": 20, "hours": 9,
    "notes": NOTES,
    "programs": PROGRAMS,
    "diagrams": [{"id": k, "title": v, "file": f"diagrams/{k}.svg"} for k, v in DIAGRAM_TITLES.items()],
    "syntax": SYNTAX, "viva": VIVA, "exam_questions": EXAM_QS,
}

if __name__ == "__main__":
    check_and_write(UNIT, DIAGRAM_TITLES, "DI03000031_unit5_preview.html")
