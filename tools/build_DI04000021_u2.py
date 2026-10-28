"""Builds DI04000021 (OOP - Java) Unit 2 JSON + preview. English only."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from subject_DI04000021 import check_and_write
from content_DI04000021_u2_notes import NOTES
from content_DI04000021_u2_programs import PROGRAMS
from content_DI04000021_u2_extras import SYNTAX, VIVA, EXAM_QS

DIAGRAM_TITLES = {
    "jv2_pillars": {"en": "Four Principles of OOP"},
    "jv2_class_object": {"en": "Class and Objects"},
    "jv2_ctor": {"en": "Constructors"},
    "jv2_this_static": {"en": "this and static"},
    "jv2_access": {"en": "Access Modifiers"},
    "jv2_strings": {"en": "Common String Methods"},
    "jv2_boxing": {"en": "Wrapper Classes, Autoboxing and Unboxing"},
    "jv2_gc": {"en": "Garbage Collection and finalize()"},
}

UNIT = {
    "subject": "DI04000021", "unit": 2, "format": "notes",
    "title": {"en": "Object-Oriented Programming Concepts"},
    "weightage": 25, "hours": 10,
    "notes": NOTES,
    "programs": PROGRAMS,
    "diagrams": [{"id": k, "title": v, "file": f"diagrams/{k}.svg"} for k, v in DIAGRAM_TITLES.items()],
    "syntax": SYNTAX, "viva": VIVA, "exam_questions": EXAM_QS,
}

if __name__ == "__main__":
    check_and_write(UNIT, DIAGRAM_TITLES, "DI04000021_unit2_preview.html")
