"""Builds DI03000041 Fundamentals of Operating System Unit 1 (Introduction of Operating System). Bilingual EN + GU."""
import os, sys, subprocess
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from subject_DI03000041 import check_and_write
from content_DI03000041_u1_notes import NOTES
from content_DI03000041_u1_extras import NUMERICALS, EQUATIONS, VIVA, EXAM_QS

DIAGRAM_TITLES = {
    "os1_role": {"en": "OS: Interface between User and Hardware", "gu": "OS: User અને Hardware વચ્ચે Interface"},
    "os1_functions": {"en": "Functions and Goals of an OS", "gu": "OS ના Functions અને Goals"},
    "os1_services": {"en": "Operating System Services", "gu": "Operating System Services"},
    "os1_multiprog": {"en": "Multiprogramming OS", "gu": "Multiprogramming OS"},
    "os1_timeshare": {"en": "Time-Sharing OS", "gu": "Time-Sharing OS"},
    "os1_realtime": {"en": "Real-Time OS: Hard and Soft", "gu": "Real-Time OS: Hard અને Soft"},
    "os1_multithread": {"en": "Single-Threaded vs Multithreaded Process", "gu": "Single-Threaded vs Multithreaded Process"},
    "os1_distributed": {"en": "Distributed OS", "gu": "Distributed OS"},
    "os1_embedded": {"en": "Embedded OS", "gu": "Embedded OS"},
    "os1_layered": {"en": "Layered Structure", "gu": "Layered Structure"},
    "os1_monolithic": {"en": "Monolithic Kernel", "gu": "Monolithic Kernel"},
    "os1_microkernel": {"en": "Microkernel", "gu": "Microkernel"},
    "os1_linux": {"en": "Linux Layers", "gu": "Linux Layers"},
    "os1_case": {"en": "Linux vs Windows vs macOS", "gu": "Linux vs Windows vs macOS"},
}

UNIT = {
    "subject": "DI03000041", "unit": 1, "format": "notes",
    "title": {"en": "Introduction of Operating System", "gu": "Operating System નો પરિચય"},
    "weightage": 13, "hours": 6,
    "notes": NOTES,
    "numericals": NUMERICALS, "equations": EQUATIONS, "viva": VIVA, "exam_questions": EXAM_QS,
}

if __name__ == "__main__":
    subprocess.run([sys.executable, os.path.join(os.path.dirname(os.path.abspath(__file__)), "diagrams_DI03000041_u1.py")], check=True,
                   stdout=subprocess.DEVNULL)
    check_and_write(UNIT, DIAGRAM_TITLES, "DI03000041_unit1_preview.html")
