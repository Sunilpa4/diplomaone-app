"""Builds DI04000011 (Software Engineering) Unit 1 JSON + preview. English only."""
import os, sys, subprocess
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from subject_DI04000011 import check_and_write
from content_DI04000011_u1_notes import NOTES
from content_DI04000011_u1_extras import SYNTAX, VIVA, EXAM_QS

DIAGRAM_TITLES = {
    "se1_domains": {"en": "Software Application Domains"},
    "se1_layers": {"en": "Software Engineering: A Layered Approach"},
    "se1_framework": {"en": "Generic Process Model"},
    "se1_waterfall": {"en": "Waterfall Model"},
    "se1_incremental": {"en": "Incremental Model"},
    "se1_prototype": {"en": "Prototyping Model"},
    "se1_spiral": {"en": "Spiral Model"},
    "se1_vmodel": {"en": "V-Model"},
    "se1_agile": {"en": "Agile Manifesto: The Four Values"},
    "se1_scrum": {"en": "Scrum Framework"},
    "se1_xp": {"en": "Extreme Programming (XP)"},
}

UNIT = {
    "subject": "DI04000011", "unit": 1, "format": "notes",
    "title": {"en": "Software Process Models"},
    "weightage": 26, "hours": 11,
    "notes": NOTES,
    "syntax": SYNTAX, "viva": VIVA, "exam_questions": EXAM_QS,
}

if __name__ == "__main__":
    subprocess.run([sys.executable, os.path.join(HERE, "diagrams_DI04000011_u1.py")], check=True)
    check_and_write(UNIT, DIAGRAM_TITLES, "DI04000011_unit1_preview.html")
