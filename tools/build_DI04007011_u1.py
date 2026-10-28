"""Builds DI04007011 (Introduction to Web Development) Unit 1 JSON + preview. English only."""
import os, sys, subprocess
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from subject_DI04007011 import check_and_write
from content_DI04007011_u1_notes import NOTES
from content_DI04007011_u1_programs import PROGRAMS
from content_DI04007011_u1_extras import SYNTAX, VIVA, EXAM_QS

DIAGRAM_TITLES = {
    "wd1_client_server": {"en": "Client-Server: One Request Cycle"},
    "wd1_3tier": {"en": "3-Tier Architecture of a Web App"},
    "wd1_xampp": {"en": "XAMPP: The Whole Lab in One Install"},
    "wd1_embed": {"en": "Embedding PHP Inside HTML"},
    "wd1_datatypes": {"en": "PHP Data Types (Loosely Typed)"},
    "wd1_operators": {"en": "PHP Operator Families"},
    "wd1_ifelif": {"en": "if - elseif - else Flow"},
    "wd1_loops": {"en": "Four Loops, Four Personalities"},
}

UNIT = {
    "subject": "DI04007011", "unit": 1, "format": "notes",
    "title": {"en": "Introduction to PHP"},
    "weightage": 20, "hours": 12,
    "notes": NOTES,
    "programs": PROGRAMS,
    "diagrams": [{"id": k, "title": v, "file": f"diagrams/{k}.svg"} for k, v in DIAGRAM_TITLES.items()],
    "syntax": SYNTAX, "viva": VIVA, "exam_questions": EXAM_QS,
}

if __name__ == "__main__":
    subprocess.run([sys.executable, os.path.join(HERE, "diagrams_DI04007011_u1.py")], check=True)
    check_and_write(UNIT, DIAGRAM_TITLES, "DI04007011_unit1_preview.html")
