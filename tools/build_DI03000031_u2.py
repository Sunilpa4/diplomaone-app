"""Builds DI03000031 (RDBMS) Unit 2 JSON + preview. English only, Oracle SQL."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from subject_DI03000031 import check_and_write
from content_DI03000031_u2_notes_a import NOTES_A
from content_DI03000031_u2_notes_b import NOTES_B
from content_DI03000031_u2_programs import PROGRAMS
from content_DI03000031_u2_extras import SYNTAX, VIVA, EXAM_QS

DIAGRAM_TITLES = {
    "db2_operators": {"en": "SQL Operators"},
    "db2_like": {"en": "LIKE Wildcards: % and _"},
    "db2_functions": {"en": "Types of SQL Functions"},
    "db2_substr_instr": {"en": "String Positions: SUBSTR and INSTR"},
    "db2_date_funcs": {"en": "Date Functions"},
    "db2_conversion": {"en": "Conversion Functions"},
    "db2_groupby": {"en": "GROUP BY and HAVING"},
    "db2_query_order": {"en": "Order of Execution of a SELECT"},
    "db2_joins": {"en": "Types of Joins"},
    "db2_cross_join": {"en": "Cross Join (Cartesian Product)"},
    "db2_self_join": {"en": "Self Join: Employee and Manager"},
    "db2_subquery": {"en": "Sub-query and Correlated Sub-query"},
    "db2_set_ops": {"en": "Set Operators"},
}

UNIT = {
    "subject": "DI03000031", "unit": 2, "format": "notes",
    "title": {"en": "SQL Functions and Joins"},
    "weightage": 24, "hours": 11,
    "notes": NOTES_A + NOTES_B,
    "programs": PROGRAMS,
    "diagrams": [{"id": k, "title": v, "file": f"diagrams/{k}.svg"} for k, v in DIAGRAM_TITLES.items()],
    "syntax": SYNTAX, "viva": VIVA, "exam_questions": EXAM_QS,
}

if __name__ == "__main__":
    check_and_write(UNIT, DIAGRAM_TITLES, "DI03000031_unit2_preview.html")
