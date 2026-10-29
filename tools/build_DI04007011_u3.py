"""Builds DI04007011 (Introduction to Web Development) Unit 3 JSON + preview. English only."""
import os, sys, subprocess
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from subject_DI04007011 import check_and_write
from content_DI04007011_u3_notes import NOTES
from content_DI04007011_u3_programs import PROGRAMS
from content_DI04007011_u3_extras import SYNTAX, VIVA, EXAM_QS

DIAGRAM_TITLES = {
    "wd3_form_controls": {"en": "Form Controls Catalog"},
    "wd3_get_post": {"en": "GET vs POST"},
    "wd3_superglobals": {"en": "The Superglobals Map"},
    "wd3_selfprocess": {"en": "The Self-Processing Page Pattern"},
    "wd3_validation": {"en": "Validation Pipeline"},
    "wd3_files": {"en": "Reading and Writing Text Files"},
    "wd3_upload": {"en": "File Upload Flow"},
    "wd3_email": {"en": "mail(): Anatomy of Sending"},
}

UNIT = {
    "subject": "DI04007011", "unit": 3, "format": "notes",
    "title": {"en": "Working with Data and Forms"},
    "weightage": 15, "hours": 10,
    "notes": NOTES,
    "programs": PROGRAMS,
    "diagrams": [{"id": k, "title": v, "file": f"diagrams/{k}.svg"} for k, v in DIAGRAM_TITLES.items()],
    "syntax": SYNTAX, "viva": VIVA, "exam_questions": EXAM_QS,
}

if __name__ == "__main__":
    subprocess.run([sys.executable, os.path.join(HERE, "diagrams_DI04007011_u1.py")], check=True)
    check_and_write(UNIT, DIAGRAM_TITLES, "DI04007011_unit3_preview.html")
