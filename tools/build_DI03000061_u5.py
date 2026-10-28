"""Builds DI03000061 (RWPD) Unit 5 JSON + preview. English only, utilities and customization."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from subject_DI03000061 import check_and_write
from content_DI03000061_u5_notes import NOTES
from content_DI03000061_u5_programs import PROGRAMS
from content_DI03000061_u5_extras import SYNTAX, VIVA, EXAM_QS

DIAGRAM_TITLES = {
    "web5_utility_class": {"en": "Anatomy of a Utility Class"},
    "web5_group_map": {"en": "Bootstrap Utility Families"},
    "web5_responsive": {"en": "Mobile-First Responsive Infix"},
    "web5_flex_axes": {"en": "Flexbox Axes and Alignment"},
    "web5_customize_levels": {"en": "Levels of Bootstrap Customization"},
    "web5_sass_flow": {"en": "Sass Customization Workflow"},
    "web5_themes": {"en": "Colour Modes and Themes"},
}

UNIT = {
    "subject": "DI03000061", "unit": 5, "format": "notes",
    "title": {"en": "Utilities and Customization"},
    "weightage": 17, "hours": 10,
    "notes": NOTES,
    "programs": PROGRAMS,
    "diagrams": [{"id": k, "title": v, "file": f"diagrams/{k}.svg"} for k, v in DIAGRAM_TITLES.items()],
    "syntax": SYNTAX, "viva": VIVA, "exam_questions": EXAM_QS,
}

if __name__ == "__main__":
    check_and_write(UNIT, DIAGRAM_TITLES, "DI03000061_unit5_preview.html")
