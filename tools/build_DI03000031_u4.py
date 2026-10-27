"""Builds DI03000031 (RDBMS) Unit 4 JSON + preview. English only, constraints and database objects."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from subject_DI03000031 import check_and_write
from content_DI03000031_u4_notes import NOTES
from content_DI03000031_u4_programs import PROGRAMS
from content_DI03000031_u4_extras import SYNTAX, VIVA, EXAM_QS

DIAGRAM_TITLES = {
    "db4_constraints": {"en": "Types of Integrity Constraints"},
    "db4_pk_unique": {"en": "PRIMARY KEY vs UNIQUE"},
    "db4_fk": {"en": "Foreign Key: Parent and Child"},
    "db4_cascade": {"en": "Delete Rules for a Parent Row"},
    "db4_objects": {"en": "Oracle Database Objects"},
    "db4_view": {"en": "A View is a Window on a Table"},
    "db4_view_types": {"en": "Simple View vs Complex View"},
    "db4_sequence": {"en": "Sequence: Automatic Number Generator"},
    "db4_index": {"en": "Index on EMP(ENAME)"},
}

UNIT = {
    "subject": "DI03000031", "unit": 4, "format": "notes",
    "title": {"en": "Database Integrity Constraints and Objects"},
    "weightage": 16, "hours": 7,
    "notes": NOTES,
    "programs": PROGRAMS,
    "diagrams": [{"id": k, "title": v, "file": f"diagrams/{k}.svg"} for k, v in DIAGRAM_TITLES.items()],
    "syntax": SYNTAX, "viva": VIVA, "exam_questions": EXAM_QS,
}

if __name__ == "__main__":
    check_and_write(UNIT, DIAGRAM_TITLES, "DI03000031_unit4_preview.html")
