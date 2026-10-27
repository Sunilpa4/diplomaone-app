"""Builds DI02000101 (Scripting Language - Python) Unit 5 JSON + preview. English only."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from subject_DI02000101 import check_and_write
from content_DI02000101_u5_notes_a import NOTES_A
from content_DI02000101_u5_notes_b import NOTES_B
from content_DI02000101_u5_programs import PROGRAMS
from content_DI02000101_u5_extras import SYNTAX, VIVA, EXAM_QS

DIAGRAM_TITLES = {
    "py5_module": {"en": "Module: Write Once, Import Anywhere"},
    "py5_import_forms": {"en": "Ways to Import"},
    "py5_math_round": {"en": "ceil(), floor(), trunc()"},
    "py5_package_tree": {"en": "Package Structure"},
    "py5_mpl_anatomy": {"en": "Parts of a Matplotlib Plot"},
    "py5_out_line": {"en": "Output: Line Plot (plot)"},
    "py5_out_bar": {"en": "Output: Bar Chart (bar)"},
    "py5_out_hist": {"en": "Output: Histogram (hist)"},
    "py5_out_pie": {"en": "Output: Pie Chart (pie)"},
    "py5_out_subplot": {"en": "Output: subplot() Grid"},
    "py5_out_waves": {"en": "Output: Sine and Cosine (NumPy + Matplotlib)"},
    "py5_np_array": {"en": "NumPy Arrays and Attributes"},
    "py5_np_slicing": {"en": "Indexing and Slicing a 2-D Array"},
    "py5_np_axis": {"en": "axis in NumPy Functions"},
    "py5_np_ops": {"en": "dot, cross and matmul"},
}

UNIT = {
    "subject": "DI02000101", "unit": 5, "format": "notes",
    "title": {"en": "Python Modules and Packages"},
    "weightage": 22, "hours": 10,
    "notes": NOTES_A + NOTES_B,
    "programs": PROGRAMS,
    "diagrams": [{"id": k, "title": v, "file": f"diagrams/{k}.svg"} for k, v in DIAGRAM_TITLES.items()],
    "syntax": SYNTAX, "viva": VIVA, "exam_questions": EXAM_QS,
}

if __name__ == "__main__":
    check_and_write(UNIT, DIAGRAM_TITLES, "DI02000101_unit5_preview.html")
