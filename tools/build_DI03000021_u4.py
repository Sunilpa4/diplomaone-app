"""Builds DI03000021 (Data Structures) Unit 4 JSON + preview. English only."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from subject_DI03000021 import check_and_write
from content_DI03000021_u4_notes_a import NOTES_A
from content_DI03000021_u4_notes_b import NOTES_B
from content_DI03000021_u4_programs import PROGRAMS
from content_DI03000021_u4_extras import ALGORITHMS, NUMERICALS, VIVA, EXAM_QS

DIAGRAM_TITLES = {
    "ds4_terms": {"en": "Tree: Basic Terminology"},
    "ds4_forest": {"en": "Forest"},
    "ds4_binary_types": {"en": "Binary, Strict and Complete Binary Tree"},
    "ds4_node_repr": {"en": "Binary Tree: Linked Representation"},
    "ds4_gen2bin": {"en": "General Tree to Binary Tree"},
    "ds4_traversal": {"en": "Inorder, Preorder, Postorder"},
    "ds4_bst_build": {"en": "Binary Search Tree Construction"},
    "ds4_bst_search": {"en": "Searching in a BST"},
    "ds4_bst_delete": {"en": "BST Deletion: Three Cases"},
    "ds4_graph_terms": {"en": "Graph: Basic Terms"},
    "ds4_graph_types": {"en": "Types of Graph"},
}

UNIT = {
    "subject": "DI03000021", "unit": 4, "format": "notes",
    "title": {"en": "Trees and Graph"},
    "weightage": 20, "hours": 9,
    "notes": NOTES_A + NOTES_B,
    "programs": PROGRAMS,
    "diagrams": [{"id": k, "title": v, "file": f"diagrams/{k}.svg"} for k, v in DIAGRAM_TITLES.items()],
    "algorithms": ALGORITHMS, "numericals": NUMERICALS,
    "syntax": [], "viva": VIVA, "exam_questions": EXAM_QS,
}

if __name__ == "__main__":
    check_and_write(UNIT, DIAGRAM_TITLES, "DI03000021_unit4_preview.html")
