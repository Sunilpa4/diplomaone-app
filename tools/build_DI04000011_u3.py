"""Builds DI04000011 (Software Engineering) Unit 3 JSON + preview. English only."""
import os, sys, subprocess
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from subject_DI04000011 import check_and_write
from content_DI04000011_u3_notes import NOTES
from content_DI04000011_u3_extras import SYNTAX, VIVA, EXAM_QS

DIAGRAM_TITLES = {
    "se3_pm_duties": {"en": "Software Project Manager: Duties"},
    "se3_loc_fp": {"en": "LOC vs Function Points"},
    "se3_fp_calc": {"en": "Function Point Calculation"},
    "se3_cocomo": {"en": "Basic COCOMO"},
    "se3_gantt": {"en": "Gantt Chart: 8-Week Project Plan"},
    "se3_flow": {"en": "Flow Chart: Building the Schedule"},
    "se3_burndown": {"en": "Sprint Burndown Chart"},
    "se3_risk_cycle": {"en": "Risk Management Cycle"},
    "se3_risk_matrix": {"en": "Risk Assessment: Probability x Impact Grid"},
}

UNIT = {
    "subject": "DI04000011", "unit": 3, "format": "notes",
    "title": {"en": "Software Project Estimation and Scheduling"},
    "weightage": 26, "hours": 11,
    "notes": NOTES,
    "syntax": SYNTAX, "viva": VIVA, "exam_questions": EXAM_QS,
}

if __name__ == "__main__":
    subprocess.run([sys.executable, os.path.join(HERE, "diagrams_DI04000011_u1.py")], check=True)
    check_and_write(UNIT, DIAGRAM_TITLES, "DI04000011_unit3_preview.html")
