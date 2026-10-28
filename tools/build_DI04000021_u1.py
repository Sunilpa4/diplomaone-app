"""Builds DI04000021 (OOP - Java) Unit 1 JSON + preview. English only."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from subject_DI04000021 import check_and_write
from content_DI04000021_u1_notes import NOTES
from content_DI04000021_u1_programs import PROGRAMS
from content_DI04000021_u1_extras import SYNTAX, VIVA, EXAM_QS

DIAGRAM_TITLES = {
    "jv1_jdk_jre_jvm": {"en": "JDK, JRE and JVM"},
    "jv1_wora": {"en": "Write Once, Run Anywhere"},
    "jv1_structure": {"en": "Structure of a Java Program"},
    "jv1_datatypes": {"en": "Primitive Data Types of Java"},
    "jv1_casting": {"en": "Type Conversion and Casting"},
    "jv1_operators": {"en": "Operators in Java"},
    "jv1_loops": {"en": "Control Flow Overview"},
}

UNIT = {
    "subject": "DI04000021", "unit": 1, "format": "notes",
    "title": {"en": "Introduction to Java Programming"},
    "weightage": 20, "hours": 10,
    "notes": NOTES,
    "programs": PROGRAMS,
    "diagrams": [{"id": k, "title": v, "file": f"diagrams/{k}.svg"} for k, v in DIAGRAM_TITLES.items()],
    "syntax": SYNTAX, "viva": VIVA, "exam_questions": EXAM_QS,
}

if __name__ == "__main__":
    check_and_write(UNIT, DIAGRAM_TITLES, "DI04000021_unit1_preview.html")
