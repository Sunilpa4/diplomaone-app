"""Builds DI04000021 (OOP - Java) Unit 3 JSON + preview. English only."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from subject_DI04000021 import check_and_write
from content_DI04000021_u3_notes import NOTES
from content_DI04000021_u3_programs import PROGRAMS
from content_DI04000021_u3_extras import SYNTAX, VIVA, EXAM_QS

DIAGRAM_TITLES = {
    "jv3_inherit_types": {"en": "Types of Inheritance"},
    "jv3_super_this": {"en": "this vs super"},
    "jv3_override_vs": {"en": "Overloading vs Overriding"},
    "jv3_dispatch": {"en": "Dynamic Method Dispatch"},
    "jv3_abstract_vs": {"en": "Abstract Class vs Interface"},
    "jv3_interface_multi": {"en": "Multiple Inheritance via Interfaces"},
    "jv3_packages": {"en": "Packages and import"},
}

UNIT = {
    "subject": "DI04000021", "unit": 3, "format": "notes",
    "title": {"en": "Inheritance, Interfaces and Abstraction"},
    "weightage": 25, "hours": 10,
    "notes": NOTES,
    "programs": PROGRAMS,
    "diagrams": [{"id": k, "title": v, "file": f"diagrams/{k}.svg"} for k, v in DIAGRAM_TITLES.items()],
    "syntax": SYNTAX, "viva": VIVA, "exam_questions": EXAM_QS,
}

if __name__ == "__main__":
    check_and_write(UNIT, DIAGRAM_TITLES, "DI04000021_unit3_preview.html")
