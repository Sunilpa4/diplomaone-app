"""Builds DI03000021 (Data Structures) Unit 3 JSON + preview. English only."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from subject_DI03000021 import check_and_write
from content_DI03000021_u3_notes_a import NOTES_A
from content_DI03000021_u3_notes_b import NOTES_B
from content_DI03000021_u3_programs import PROGRAMS
from content_DI03000021_u3_extras import ALGORITHMS, NUMERICALS, VIVA, EXAM_QS

DIAGRAM_TITLES = {
    "ds3_pointer": {"en": "Pointer: & and * Operators"},
    "ds3_structure": {"en": "Structure and Structure Pointer"},
    "ds3_dma": {"en": "Dynamic Memory Allocation"},
    "ds3_representation": {"en": "Linked List Representation"},
    "ds3_types": {"en": "Types of Linked List"},
    "ds3_insert_begin": {"en": "Insert at Beginning"},
    "ds3_insert_end": {"en": "Insert at End"},
    "ds3_insert_after": {"en": "Insert After / Before a Node"},
    "ds3_insert_sorted": {"en": "Insert into a Sorted List"},
    "ds3_delete": {"en": "Delete First and Last Node"},
    "ds3_traverse": {"en": "Search and Count (Traversal)"},
}

UNIT = {
    "subject": "DI03000021", "unit": 3, "format": "notes",
    "title": {"en": "Linked List"},
    "weightage": 24, "hours": 11,
    "notes": NOTES_A + NOTES_B,
    "programs": PROGRAMS,
    "diagrams": [{"id": k, "title": v, "file": f"diagrams/{k}.svg"} for k, v in DIAGRAM_TITLES.items()],
    "algorithms": ALGORITHMS, "numericals": NUMERICALS,
    "syntax": [], "viva": VIVA, "exam_questions": EXAM_QS,
}

if __name__ == "__main__":
    check_and_write(UNIT, DIAGRAM_TITLES, "DI03000021_unit3_preview.html")
