"""Builds DI03000021 (Data Structures) Unit 1 JSON + preview. English only."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from subject_DI03000021 import check_and_write
from content_DI03000021_u1_notes_a import NOTES_A
from content_DI03000021_u1_notes_b import NOTES_B
from content_DI03000021_u1_programs import PROGRAMS
from content_DI03000021_u1_extras import ALGORITHMS, NUMERICALS, VIVA, EXAM_QS

DIAGRAM_TITLES = {
    "ds1_data_info": {"en": "Data, Processing and Information"},
    "ds1_classification": {"en": "Classification of Data Structures"},
    "ds1_linear_nonlinear": {"en": "Linear vs Non-Linear Data Structure"},
    "ds1_operations": {"en": "Operations on Data Structures"},
    "ds1_characteristics": {"en": "Characteristics of an Algorithm"},
    "ds1_growth": {"en": "Growth of Common Time Complexities"},
    "ds1_asymptotic": {"en": "Asymptotic Notations: O, Ω, Θ"},
    "ds1_array_memory": {"en": "One-Dimensional Array in Memory"},
    "ds1_row_col_major": {"en": "Row Major vs Column Major"},
    "ds1_insert_delete": {"en": "Insertion and Deletion in an Array"},
}

UNIT = {
    "subject": "DI03000021", "unit": 1, "format": "notes",
    "title": {"en": "Basic Concepts of Data Structures"},
    "weightage": 14, "hours": 6,
    "notes": NOTES_A + NOTES_B,
    "programs": PROGRAMS,
    "diagrams": [{"id": k, "title": v, "file": f"diagrams/{k}.svg"} for k, v in DIAGRAM_TITLES.items()],
    "algorithms": ALGORITHMS, "numericals": NUMERICALS,
    "syntax": [], "viva": VIVA, "exam_questions": EXAM_QS,
}

if __name__ == "__main__":
    check_and_write(UNIT, DIAGRAM_TITLES, "DI03000021_unit1_preview.html")
