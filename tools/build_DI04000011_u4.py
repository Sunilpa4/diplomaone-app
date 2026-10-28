"""Builds DI04000011 (Software Engineering) Unit 4 JSON + preview. English only."""
import os, sys, subprocess
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from subject_DI04000011 import check_and_write
from content_DI04000011_u4_notes import NOTES
from content_DI04000011_u4_extras import SYNTAX, VIVA, EXAM_QS

DIAGRAM_TITLES = {
    "se4_standards": {"en": "Coding Standards: What They Police"},
    "se4_review": {"en": "Walkthrough vs Inspection"},
    "se4_docs": {"en": "Internal vs External Documentation"},
    "se4_levels": {"en": "Levels of Testing"},
    "se4_blackbox": {"en": "Black-Box Testing: Inputs Only"},
    "se4_whitebox": {"en": "White-Box Testing: Cover the Code"},
    "se4_ab": {"en": "Alpha and Beta Testing"},
    "se4_testcase": {"en": "Test Case Template (Practical 15)"},
}

UNIT = {
    "subject": "DI04000011", "unit": 4, "format": "notes",
    "title": {"en": "Coding and Testing"},
    "weightage": 20, "hours": 8,
    "notes": NOTES,
    "syntax": SYNTAX, "viva": VIVA, "exam_questions": EXAM_QS,
}

if __name__ == "__main__":
    subprocess.run([sys.executable, os.path.join(HERE, "diagrams_DI04000011_u4.py")], check=True)
    check_and_write(UNIT, DIAGRAM_TITLES, "DI04000011_unit4_preview.html")
