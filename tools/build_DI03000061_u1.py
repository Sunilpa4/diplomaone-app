"""Builds DI03000061 (RWPD) Unit 1 JSON + preview. English only, jQuery and Bootstrap introduction."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from subject_DI03000061 import check_and_write
from content_DI03000061_u1_notes import NOTES
from content_DI03000061_u1_programs import PROGRAMS
from content_DI03000061_u1_extras import SYNTAX, VIVA, EXAM_QS

DIAGRAM_TITLES = {
    "web1_jq_syntax": {"en": "jQuery Syntax"},
    "web1_selectors": {"en": "jQuery Selectors"},
    "web1_events": {"en": "jQuery Events"},
    "web1_bs_history": {"en": "History of Bootstrap"},
    "web1_setup": {"en": "Setting up Bootstrap"},
    "web1_responsive": {"en": "Responsive Web Design"},
    "web1_viewport": {"en": "The Viewport Meta Tag"},
    "web1_breakpoints": {"en": "Bootstrap 5 Breakpoints"},
    "web1_features": {"en": "Major Features of Bootstrap"},
}

UNIT = {
    "subject": "DI03000061", "unit": 1, "format": "notes",
    "title": {"en": "Introduction to jQuery and Bootstrap"},
    "weightage": 17, "hours": 10,
    "notes": NOTES,
    "programs": PROGRAMS,
    "diagrams": [{"id": k, "title": v, "file": f"diagrams/{k}.svg"} for k, v in DIAGRAM_TITLES.items()],
    "syntax": SYNTAX, "viva": VIVA, "exam_questions": EXAM_QS,
}

if __name__ == "__main__":
    check_and_write(UNIT, DIAGRAM_TITLES, "DI03000061_unit1_preview.html")
