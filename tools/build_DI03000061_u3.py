"""Builds DI03000061 (RWPD) Unit 3 JSON + preview. English only, Bootstrap components."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from subject_DI03000061 import check_and_write
from content_DI03000061_u3_notes import NOTES
from content_DI03000061_u3_programs import PROGRAMS
from content_DI03000061_u3_extras import SYNTAX, VIVA, EXAM_QS

DIAGRAM_TITLES = {
    "web3_components": {"en": "Types of Bootstrap Components"},
    "web3_bs3_map": {"en": "Bootstrap 3 Components in Bootstrap 5"},
    "web3_dropdown": {"en": "Dropdown Menu Structure"},
    "web3_card": {"en": "Card Component"},
    "web3_btn_groups": {"en": "Button Group and Toolbar"},
    "web3_input_group": {"en": "Input Group"},
    "web3_navs": {"en": "Navs: Tabs and Pills"},
    "web3_navbar": {"en": "Responsive Navbar"},
    "web3_breadcrumb": {"en": "Breadcrumb and Pagination"},
    "web3_alerts_badges": {"en": "Alerts, Badges and Jumbotron"},
    "web3_progress": {"en": "Progress Bars"},
    "web3_media_list": {"en": "Media Object and List Group"},
}

UNIT = {
    "subject": "DI03000061", "unit": 3, "format": "notes",
    "title": {"en": "Bootstrap Components"},
    "weightage": 23, "hours": 14,
    "notes": NOTES,
    "programs": PROGRAMS,
    "diagrams": [{"id": k, "title": v, "file": f"diagrams/{k}.svg"} for k, v in DIAGRAM_TITLES.items()],
    "syntax": SYNTAX, "viva": VIVA, "exam_questions": EXAM_QS,
}

if __name__ == "__main__":
    check_and_write(UNIT, DIAGRAM_TITLES, "DI03000061_unit3_preview.html")
