"""Builds DI04000011 (Software Engineering) Unit 2 JSON + preview. English only."""
import os, sys, subprocess
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from subject_DI04000011 import check_and_write
from content_DI04000011_u2_notes import NOTES
from content_DI04000011_u2_extras import SYNTAX, VIVA, EXAM_QS

DIAGRAM_TITLES = {
    "se2_req_types": {"en": "Functional vs Non-Functional Requirements"},
    "se2_gather": {"en": "Requirement Gathering Techniques"},
    "se2_srs": {"en": "SRS: Structure and Qualities"},
    "se2_analysis_vs_design": {"en": "Analysis vs Design: WHAT vs HOW"},
    "se2_cohesion": {"en": "Cohesion: Best to Worst"},
    "se2_coupling": {"en": "Coupling: Worst to Best"},
    "se2_dfd_symbols": {"en": "DFD Symbols (Yourdon-DeMarco)"},
    "se2_dfd_levels": {"en": "DFD Levels: Food Ordering System"},
    "se2_usecase": {"en": "Use Case Diagram: Food App"},
    "se2_class": {"en": "Class Diagram: Library Slice"},
    "se2_sequence": {"en": "Sequence Diagram: Place Order"},
    "se2_activity": {"en": "Activity Diagram: Place Order Flow"},
    "se2_component": {"en": "Component Diagram: Food App Backend"},
}

UNIT = {
    "subject": "DI04000011", "unit": 2, "format": "notes",
    "title": {"en": "Software Requirement Analysis and Design"},
    "weightage": 28, "hours": 15,
    "notes": NOTES,
    "syntax": SYNTAX, "viva": VIVA, "exam_questions": EXAM_QS,
}

if __name__ == "__main__":
    subprocess.run([sys.executable, os.path.join(HERE, "diagrams_DI04000011_u1.py")], check=True)
    check_and_write(UNIT, DIAGRAM_TITLES, "DI04000011_unit2_preview.html")
