"""Builds DI03000041 Fundamentals of Operating System Unit 4 (File System). Bilingual EN + GU."""
import os, sys, subprocess
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from subject_DI03000041 import check_and_write
from content_DI03000041_u4_notes import NOTES
from content_DI03000041_u4_extras import NUMERICALS, EQUATIONS, VIVA, EXAM_QS

DIAGRAM_TITLES = {
    "os4_paths": {"en": "Absolute and Relative File Paths", "gu": "Absolute અને Relative File Paths"},
    "os4_perm": {"en": "Unix File Permissions (rwx)", "gu": "Unix File Permissions (rwx)"},
    "os4_single": {"en": "Single-Level Directory", "gu": "Single-Level Directory"},
    "os4_two": {"en": "Two-Level Directory", "gu": "Two-Level Directory"},
    "os4_tree": {"en": "Tree-Structured Directory", "gu": "Tree-Structured Directory"},
    "os4_acyclic": {"en": "Acyclic-Graph Directory", "gu": "Acyclic-Graph Directory"},
    "os4_general": {"en": "General Graph Directory", "gu": "General Graph Directory"},
    "os4_contig": {"en": "Contiguous Allocation", "gu": "Contiguous Allocation"},
    "os4_linked": {"en": "Linked Allocation", "gu": "Linked Allocation"},
    "os4_indexed": {"en": "Indexed Allocation", "gu": "Indexed Allocation"},
    "os4_disk": {"en": "Physical Structure of a Disk", "gu": "Disk નું Physical Structure"},
    "os4_scan": {"en": "SCAN (Practical 5)", "gu": "SCAN (Practical 5)"},
    "os4_cscan": {"en": "C-SCAN (Practical 5)", "gu": "C-SCAN (Practical 5)"},
}

UNIT = {
    "subject": "DI03000041", "unit": 4, "format": "notes",
    "title": {"en": "File System", "gu": "File System"},
    "weightage": 13, "hours": 6,
    "notes": NOTES,
    "numericals": NUMERICALS, "equations": EQUATIONS, "viva": VIVA, "exam_questions": EXAM_QS,
}

if __name__ == "__main__":
    subprocess.run([sys.executable, os.path.join(os.path.dirname(os.path.abspath(__file__)), "diagrams_DI03000041_u4.py")], check=True,
                   stdout=subprocess.DEVNULL)
    check_and_write(UNIT, DIAGRAM_TITLES, "DI03000041_unit4_preview.html")
