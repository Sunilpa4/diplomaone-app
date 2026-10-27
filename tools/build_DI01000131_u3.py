"""Builds DI01000131 (Computer Programming Fundamentals) Unit 3 JSON + preview. English only."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from subject_DI01000131 import check_and_write
from content_DI01000131_u3_notes_a import NOTES_A
from content_DI01000131_u3_notes_b import NOTES_B
from content_DI01000131_u3_programs import PROGRAMS
from content_DI01000131_u3_extras import SYNTAX, VIVA, EXAM_QS

DIAGRAM_TITLES = {
    "c3_array_types": {"en": "Types of Arrays"},
    "c3_1d_memory": {"en": "One-dimensional Array in Memory"},
    "c3_fc_search": {"en": "Flowchart: Linear Search"},
    "c3_bubble": {"en": "Bubble Sort – Pass by Pass"},
    "c3_2d_memory": {"en": "2-D Array: Row-major Storage"},
    "c3_matmul": {"en": "Matrix Multiplication"},
    "c3_pointer": {"en": "Pointer Concept"},
    "c3_ptr_ptr": {"en": "Pointer to Pointer"},
    "c3_ptr_array": {"en": "Pointers and Arrays"},
    "c3_void_null": {"en": "void Pointer and NULL Pointer"},
}

UNIT = {
    "subject": "DI01000131", "unit": 3, "format": "notes",
    "title": {"en": "Arrays and Pointers"},
    "weightage": 20, "hours": 8,
    "notes": NOTES_A + NOTES_B,
    "programs": PROGRAMS,
    "diagrams": [{"id": k, "title": v, "file": f"diagrams/{k}.svg"} for k, v in DIAGRAM_TITLES.items()],
    "syntax": SYNTAX, "viva": VIVA, "exam_questions": EXAM_QS,
}

if __name__ == "__main__":
    check_and_write(UNIT, DIAGRAM_TITLES, "DI01000131_unit3_preview.html")
