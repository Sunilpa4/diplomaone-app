"""Builds DI03000021 (Data Structures) Unit 5 JSON + preview. English only."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from subject_DI03000021 import check_and_write
from content_DI03000021_u5_notes_a import NOTES_A
from content_DI03000021_u5_notes_b import NOTES_B
from content_DI03000021_u5_programs import PROGRAMS
from content_DI03000021_u5_extras import ALGORITHMS, NUMERICALS, VIVA, EXAM_QS

DIAGRAM_TITLES = {
    "ds5_bubble": {"en": "Bubble Sort"},
    "ds5_selection": {"en": "Selection Sort"},
    "ds5_insertion": {"en": "Insertion Sort"},
    "ds5_quick_partition": {"en": "Quick Sort: Partition"},
    "ds5_quick_tree": {"en": "Quick Sort: Whole Process"},
    "ds5_merge": {"en": "Merge Sort"},
    "ds5_radix": {"en": "Radix Sort"},
    "ds5_linear": {"en": "Linear Search"},
    "ds5_binary": {"en": "Binary Search"},
    "ds5_hash_table": {"en": "Hashing: Hash Table"},
    "ds5_hash_methods": {"en": "Hash Functions"},
}

UNIT = {
    "subject": "DI03000021", "unit": 5, "format": "notes",
    "title": {"en": "Sorting and Searching"},
    "weightage": 24, "hours": 11,
    "notes": NOTES_A + NOTES_B,
    "programs": PROGRAMS,
    "diagrams": [{"id": k, "title": v, "file": f"diagrams/{k}.svg"} for k, v in DIAGRAM_TITLES.items()],
    "algorithms": ALGORITHMS, "numericals": NUMERICALS,
    "syntax": [], "viva": VIVA, "exam_questions": EXAM_QS,
}

if __name__ == "__main__":
    check_and_write(UNIT, DIAGRAM_TITLES, "DI03000021_unit5_preview.html")
