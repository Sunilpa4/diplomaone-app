"""Builds DI04007011 (Introduction to Web Development) Unit 2 JSON + preview. English only."""
import os, sys, subprocess
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from subject_DI04007011 import check_and_write
from content_DI04007011_u2_notes import NOTES
from content_DI04007011_u2_programs import PROGRAMS
from content_DI04007011_u2_extras import SYNTAX, VIVA, EXAM_QS

DIAGRAM_TITLES = {
    "wd2_anatomy": {"en": "Anatomy of a PHP Function"},
    "wd2_value_ref": {"en": "By Value vs By Reference"},
    "wd2_scope": {"en": "Variable Scope: Rooms of the Script"},
    "wd2_array_types": {"en": "Three Flavours of PHP Arrays"},
    "wd2_foreach_map": {"en": "foreach: Streaming an Array"},
    "wd2_array_funcs": {"en": "Array Function Toolbox"},
    "wd2_quotes": {"en": "Four Ways to Write a String"},
    "wd2_string_funcs": {"en": "String Function Toolbox"},
}

UNIT = {
    "subject": "DI04007011", "unit": 2, "format": "notes",
    "title": {"en": "PHP Functions, Arrays and Strings"},
    "weightage": 20, "hours": 12,
    "notes": NOTES,
    "programs": PROGRAMS,
    "diagrams": [{"id": k, "title": v, "file": f"diagrams/{k}.svg"} for k, v in DIAGRAM_TITLES.items()],
    "syntax": SYNTAX, "viva": VIVA, "exam_questions": EXAM_QS,
}

if __name__ == "__main__":
    subprocess.run([sys.executable, os.path.join(HERE, "diagrams_DI04007011_u2.py")], check=True)
    check_and_write(UNIT, DIAGRAM_TITLES, "DI04007011_unit2_preview.html")
