"""Builds DI03000031 (RDBMS) Unit 3 JSON + preview. English only, normalization."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from subject_DI03000031 import check_and_write
from content_DI03000031_u3_notes import NOTES
from content_DI03000031_u3_programs import PROGRAMS
from content_DI03000031_u3_numericals import NUMERICALS
from content_DI03000031_u3_extras import VIVA, EXAM_QS

DIAGRAM_TITLES = {
    "db3_anomalies": {"en": "Redundancy and Anomalies"},
    "db3_keys": {"en": "Types of Keys"},
    "db3_fd": {"en": "Functional Dependency"},
    "db3_fd_types": {"en": "Full, Partial and Transitive Dependency"},
    "db3_steps": {"en": "Steps of Normalization"},
    "db3_1nf": {"en": "UNF to 1NF"},
    "db3_2nf": {"en": "1NF to 2NF"},
    "db3_3nf": {"en": "2NF to 3NF"},
}

UNIT = {
    "subject": "DI03000031", "unit": 3, "format": "notes",
    "title": {"en": "Normalization"},
    "weightage": 13, "hours": 6,
    "tabs": ["notes", "numericals", "diagrams", "programs", "viva", "exam"],
    "notes": NOTES,
    "programs": PROGRAMS,
    "numericals": NUMERICALS,
    "diagrams": [{"id": k, "title": v, "file": f"diagrams/{k}.svg"} for k, v in DIAGRAM_TITLES.items()],
    "syntax": [], "viva": VIVA, "exam_questions": EXAM_QS,
}

if __name__ == "__main__":
    check_and_write(UNIT, DIAGRAM_TITLES, "DI03000031_unit3_preview.html")
