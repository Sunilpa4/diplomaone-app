"""Builds DI03000061 (RWPD) Unit 4 JSON + preview. English only, Bootstrap plug-ins."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from subject_DI03000061 import check_and_write
from content_DI03000061_u4_notes import NOTES
from content_DI03000061_u4_programs import PROGRAMS
from content_DI03000061_u4_extras import SYNTAX, VIVA, EXAM_QS

DIAGRAM_TITLES = {
    "web4_plugins": {"en": "Bootstrap Plug-ins"},
    "web4_api": {"en": "Two Ways to Use a Plug-in"},
    "web4_modal": {"en": "Modal Dialog Structure"},
    "web4_modal_api": {"en": "Modal: Options, Methods, Events"},
    "web4_scrollspy": {"en": "Scrollspy"},
    "web4_tooltip_popover": {"en": "Tooltip and Popover"},
    "web4_collapse": {"en": "Collapse and Accordion"},
    "web4_carousel": {"en": "Carousel Structure"},
    "web4_affix": {"en": "Affix (BS3) and Sticky (BS5)"},
}

UNIT = {
    "subject": "DI03000061", "unit": 4, "format": "notes",
    "title": {"en": "Bootstrap Plug-ins"},
    "weightage": 23, "hours": 14,
    "notes": NOTES,
    "programs": PROGRAMS,
    "diagrams": [{"id": k, "title": v, "file": f"diagrams/{k}.svg"} for k, v in DIAGRAM_TITLES.items()],
    "syntax": SYNTAX, "viva": VIVA, "exam_questions": EXAM_QS,
}

if __name__ == "__main__":
    check_and_write(UNIT, DIAGRAM_TITLES, "DI03000061_unit4_preview.html")
