"""Builds DI03000031 (RDBMS) Unit 1 JSON + preview. English only, Oracle SQL."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from subject_DI03000031 import check_and_write
from content_DI03000031_u1_notes_a import NOTES_A
from content_DI03000031_u1_notes_b import NOTES_B
from content_DI03000031_u1_programs import PROGRAMS
from content_DI03000031_u1_extras import SYNTAX, VIVA, EXAM_QS

DIAGRAM_TITLES = {
    "db1_data_info": {"en": "Data, Processing and Information"},
    "db1_hierarchy": {"en": "Data Item, Record, File and Database"},
    "db1_dictionary": {"en": "Metadata in the Data Dictionary"},
    "db1_file_vs_db": {"en": "File System vs Database System"},
    "db1_environment": {"en": "Database System Environment"},
    "db1_three_level": {"en": "Three-Level (ANSI/SPARC) Architecture"},
    "db1_schema_instance": {"en": "Schema, Sub-schema and Instance"},
    "db1_sql_cmds": {"en": "Classification of SQL Commands"},
    "db1_dcl": {"en": "Users, Roles and Privileges (DCL)"},
    "db1_acid": {"en": "ACID Properties of a Transaction"},
    "db1_tx_states": {"en": "States of a Transaction"},
    "db1_savepoint": {"en": "SAVEPOINT and ROLLBACK TO"},
}

UNIT = {
    "subject": "DI03000031", "unit": 1, "format": "notes",
    "title": {"en": "Introduction to Database System and SQL Commands"},
    "weightage": 27, "hours": 12,
    "notes": NOTES_A + NOTES_B,
    "programs": PROGRAMS,
    "diagrams": [{"id": k, "title": v, "file": f"diagrams/{k}.svg"} for k, v in DIAGRAM_TITLES.items()],
    "syntax": SYNTAX, "viva": VIVA, "exam_questions": EXAM_QS,
}

if __name__ == "__main__":
    check_and_write(UNIT, DIAGRAM_TITLES, "DI03000031_unit1_preview.html")
