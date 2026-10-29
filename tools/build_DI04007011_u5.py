"""Build DI04007011 Unit 5 JSON + self-contained preview. Real MySQLi runtime required."""
import os
import sys
import subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from subject_DI04007011 import check_and_write
from content_DI04007011_u5_notes import NOTES
from content_DI04007011_u5_programs import PROGRAMS
from content_DI04007011_u5_extras import SYNTAX, VIVA, EXAM_QS

DIAGRAM_TITLES = {
    "wd5_stack": {"en": "From Browser Form to Stored Rows"},
    "wd5_phpmyadmin": {"en": "phpMyAdmin: Practical 19 Workflow"},
    "wd5_table_design": {"en": "Table Design: Types, Keys and Rules"},
    "wd5_connection": {"en": "A MySQLi Connection's Working Life"},
    "wd5_crud": {"en": "CRUD: HTTP Action, SQL and Evidence"},
    "wd5_prepared": {"en": "Prepared Statements Keep Values Separate"},
    "wd5_injection": {"en": "SQL Injection: Code vs Literal Data"},
    "wd5_transaction": {"en": "Transaction: All Writes or No Writes"},
    "wd5_mvc": {"en": "MVC Contacts: Each Layer Has One Job"},
    "wd5_deploy": {"en": "Inventory Hosting: A Separate Checklist"},
}

UNIT = {
    "subject": "DI04007011", "unit": 5, "format": "notes",
    "title": {"en": "Database Connectivity using MySQLi"},
    "weightage": 30, "hours": 16,
    "notes": NOTES, "programs": PROGRAMS,
    "diagrams": [{"id": k, "title": v, "file": f"diagrams/{k}.svg"} for k, v in DIAGRAM_TITLES.items()],
    "syntax": SYNTAX, "viva": VIVA, "exam_questions": EXAM_QS,
}

if __name__ == "__main__":
    subprocess.run([sys.executable, os.path.join(HERE, "diagrams_DI04007011_u5.py")], check=True)
    check_and_write(UNIT, DIAGRAM_TITLES, "DI04007011_unit5_preview.html")
