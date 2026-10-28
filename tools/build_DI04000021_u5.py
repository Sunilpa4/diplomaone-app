"""Builds DI04000021 (OOP - Java) Unit 5 JSON + preview. English only."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from subject_DI04000021 import check_and_write
from content_DI04000021_u5_notes import NOTES
from content_DI04000021_u5_programs import PROGRAMS
from content_DI04000021_u5_extras import SYNTAX, VIVA, EXAM_QS

DIAGRAM_TITLES = {
    "jv5_timeline": {"en": "Java Version Highlights (7 onwards)"},
    "jv5_twr": {"en": "try-with-resources vs try-finally (Java 7)"},
    "jv5_lambda": {"en": "Lambda Anatomy"},
    "jv5_func_iface": {"en": "Ready-made Functional Interfaces"},
    "jv5_stream": {"en": "Stream Pipeline: filter, map, collect"},
    "jv5_aiml": {"en": "AI, ML, DL - How They Nest"},
    "jv5_ailibs": {"en": "Java's Role in AI + Its Libraries"},
}

UNIT = {
    "subject": "DI04000021", "unit": 5, "format": "notes",
    "title": {"en": "Modern Java Features"},
    "weightage": 10, "hours": 7,
    "notes": NOTES,
    "programs": PROGRAMS,
    "diagrams": [{"id": k, "title": v, "file": f"diagrams/{k}.svg"} for k, v in DIAGRAM_TITLES.items()],
    "syntax": SYNTAX, "viva": VIVA, "exam_questions": EXAM_QS,
}

if __name__ == "__main__":
    check_and_write(UNIT, DIAGRAM_TITLES, "DI04000021_unit5_preview.html")
