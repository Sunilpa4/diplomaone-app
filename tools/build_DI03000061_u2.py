"""Builds DI03000061 (RWPD) Unit 2 JSON + preview. English only, Bootstrap grid and content classes."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from subject_DI03000061 import check_and_write
from content_DI03000061_u2_notes import NOTES
from content_DI03000061_u2_programs import PROGRAMS
from content_DI03000061_u2_extras import SYNTAX, VIVA, EXAM_QS

DIAGRAM_TITLES = {
    "web2_grid_anatomy": {"en": "Bootstrap Grid Structure"},
    "web2_grid12": {"en": "12-Column Grid"},
    "web2_containers": {"en": "Containers"},
    "web2_offset_order": {"en": "Offset and Reordering"},
    "web2_nesting": {"en": "Nesting Columns"},
    "web2_img_shapes": {"en": "Image Classes"},
    "web2_typography": {"en": "Bootstrap Typography"},
    "web2_tables": {"en": "Table Classes"},
    "web2_form_layouts": {"en": "Form Layouts"},
    "web2_buttons": {"en": "Bootstrap Buttons"},
    "web2_display": {"en": "Show / Hide with Display Classes"},
}

UNIT = {
    "subject": "DI03000061", "unit": 2, "format": "notes",
    "title": {"en": "Bootstrap Grid"},
    "weightage": 20, "hours": 12,
    "notes": NOTES,
    "programs": PROGRAMS,
    "diagrams": [{"id": k, "title": v, "file": f"diagrams/{k}.svg"} for k, v in DIAGRAM_TITLES.items()],
    "syntax": SYNTAX, "viva": VIVA, "exam_questions": EXAM_QS,
}

if __name__ == "__main__":
    check_and_write(UNIT, DIAGRAM_TITLES, "DI03000061_unit2_preview.html")
