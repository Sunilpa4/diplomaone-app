"""Builds DI03000021 (Data Structures) Unit 2 JSON + preview. English only."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from subject_DI03000021 import check_and_write
from content_DI03000021_u2_notes_a import NOTES_A
from content_DI03000021_u2_notes_b import NOTES_B
from content_DI03000021_u2_programs import PROGRAMS
from content_DI03000021_u2_extras import ALGORITHMS, NUMERICALS, VIVA, EXAM_QS

DIAGRAM_TITLES = {
    "ds2_stack_array": {"en": "Stack: Array Representation (LIFO)"},
    "ds2_push_pop": {"en": "PUSH and POP Operations"},
    "ds2_stack_apps": {"en": "Applications of Stack"},
    "ds2_notations": {"en": "Infix, Prefix and Postfix Notation"},
    "ds2_postfix_eval": {"en": "Evaluating a Postfix Expression"},
    "ds2_recursion_fact": {"en": "Recursion: Call Stack for fact(4)"},
    "ds2_fib_tree": {"en": "Recursion Tree for fib(4)"},
    "ds2_queue_array": {"en": "Queue: Array Representation (FIFO)"},
    "ds2_queue_limit": {"en": "Limitation of a Simple Queue"},
    "ds2_circular": {"en": "Circular Queue"},
}

UNIT = {
    "subject": "DI03000021", "unit": 2, "format": "notes",
    "title": {"en": "Stack and Queues"},
    "weightage": 18, "hours": 8,
    "notes": NOTES_A + NOTES_B,
    "programs": PROGRAMS,
    "diagrams": [{"id": k, "title": v, "file": f"diagrams/{k}.svg"} for k, v in DIAGRAM_TITLES.items()],
    "algorithms": ALGORITHMS, "numericals": NUMERICALS,
    "syntax": [], "viva": VIVA, "exam_questions": EXAM_QS,
}

if __name__ == "__main__":
    check_and_write(UNIT, DIAGRAM_TITLES, "DI03000021_unit2_preview.html")
