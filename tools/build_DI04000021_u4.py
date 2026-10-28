"""Builds DI04000021 (OOP - Java) Unit 4 JSON + preview. English only."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from subject_DI04000021 import check_and_write
from content_DI04000021_u4_notes import NOTES
from content_DI04000021_u4_programs import PROGRAMS
from content_DI04000021_u4_extras import SYNTAX, VIVA, EXAM_QS

DIAGRAM_TITLES = {
    "jv4_error_types": {"en": "Three Kinds of Errors"},
    "jv4_hierarchy": {"en": "Exception Hierarchy (simplified)"},
    "jv4_try_flow": {"en": "Control Flow: try / catch / finally"},
    "jv4_throw_throws": {"en": "throw vs throws"},
    "jv4_catch_order": {"en": "Multiple catch: First Match Wins"},
    "jv4_collections": {"en": "Collections Framework: Overview"},
    "jv4_list_vs_set": {"en": "ArrayList vs HashSet"},
}

UNIT = {
    "subject": "DI04000021", "unit": 4, "format": "notes",
    "title": {"en": "Exception Handling and Collections Framework"},
    "weightage": 20, "hours": 8,
    "notes": NOTES,
    "programs": PROGRAMS,
    "diagrams": [{"id": k, "title": v, "file": f"diagrams/{k}.svg"} for k, v in DIAGRAM_TITLES.items()],
    "syntax": SYNTAX, "viva": VIVA, "exam_questions": EXAM_QS,
}

if __name__ == "__main__":
    check_and_write(UNIT, DIAGRAM_TITLES, "DI04000021_unit4_preview.html")
