"""Build DI04007011 Unit 4 JSON + self-contained preview. English only."""
import os
import sys
import subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from subject_DI04007011 import check_and_write
from content_DI04007011_u4_notes import NOTES
from content_DI04007011_u4_programs import PROGRAMS
from content_DI04007011_u4_extras import SYNTAX, VIVA, EXAM_QS

DIAGRAM_TITLES = {
    "wd4_cookie_roundtrip": {"en": "A Cookie Takes Two Requests"},
    "wd4_cookie_lifecycle": {"en": "Cookie Lifecycle: Same Name and Path"},
    "wd4_cookie_flags": {"en": "Cookie Options and Safe Defaults"},
    "wd4_session_roundtrip": {"en": "Session ID Travels; Session Data Stays"},
    "wd4_login_flow": {"en": "Login to Logout: The Session Gate"},
    "wd4_cookie_vs_session": {"en": "Cookies vs Sessions"},
    "wd4_exception_flow": {"en": "Exception Flow: Success and Failure"},
    "wd4_exception_tree": {"en": "Modern PHP: The Throwable Family"},
}

UNIT = {
    "subject": "DI04007011", "unit": 4, "format": "notes",
    "title": {"en": "Cookies, Sessions and Exception Handling"},
    "weightage": 15, "hours": 10,
    "notes": NOTES,
    "programs": PROGRAMS,
    "diagrams": [{"id": k, "title": v, "file": f"diagrams/{k}.svg"} for k, v in DIAGRAM_TITLES.items()],
    "syntax": SYNTAX, "viva": VIVA, "exam_questions": EXAM_QS,
}

if __name__ == "__main__":
    subprocess.run([sys.executable, os.path.join(HERE, "diagrams_DI04007011_u4.py")], check=True)
    check_and_write(UNIT, DIAGRAM_TITLES, "DI04007011_unit4_preview.html")
