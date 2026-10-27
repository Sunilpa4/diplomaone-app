"""Builds DI02000101 (Scripting Language - Python) Unit 3 JSON + preview. English only."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from subject_DI02000101 import check_and_write
from content_DI02000101_u3_notes_a import NOTES_A
from content_DI02000101_u3_notes_b import NOTES_B
from content_DI02000101_u3_programs import PROGRAMS
from content_DI02000101_u3_extras import SYNTAX, VIVA, EXAM_QS

DIAGRAM_TITLES = {
    "py3_list_index": {"en": "List Indexing and Slicing"},
    "py3_list_methods": {"en": "List Methods: Before and After"},
    "py3_list_copy": {"en": "Aliasing vs Copying a List"},
    "py3_tuple_pack": {"en": "Tuple Packing and Unpacking"},
    "py3_set_ops": {"en": "Set Operations (Venn Diagrams)"},
    "py3_dict_struct": {"en": "Dictionary Structure"},
    "py3_dict_methods": {"en": "Dictionary Methods"},
    "py3_nested": {"en": "Nested Data Structures"},
    "py3_builtin_matrix": {"en": "Built-in Functions by Data Type"},
    "py3_choose": {"en": "Choosing a Data Structure"},
}

UNIT = {
    "subject": "DI02000101", "unit": 3, "format": "notes",
    "title": {"en": "Data Structures in Python: Lists, Tuples, Sets, Dictionaries"},
    "weightage": 18, "hours": 8,
    "notes": NOTES_A + NOTES_B,
    "programs": PROGRAMS,
    "diagrams": [{"id": k, "title": v, "file": f"diagrams/{k}.svg"} for k, v in DIAGRAM_TITLES.items()],
    "syntax": SYNTAX, "viva": VIVA, "exam_questions": EXAM_QS,
}

if __name__ == "__main__":
    check_and_write(UNIT, DIAGRAM_TITLES, "DI02000101_unit3_preview.html")
