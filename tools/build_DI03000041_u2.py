"""Builds DI03000041 Fundamentals of Operating System Unit 2 (Process Management). Bilingual EN + GU."""
import os, sys, subprocess
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from subject_DI03000041 import check_and_write
from content_DI03000041_u2_notes import NOTES
from content_DI03000041_u2_extras import NUMERICALS, EQUATIONS, VIVA, EXAM_QS

DIAGRAM_TITLES = {
    "os2_memory": {"en": "Process in Memory", "gu": "Memory માં Process"},
    "os2_states": {"en": "Process State Diagram", "gu": "Process State Diagram"},
    "os2_pcb": {"en": "Process Control Block (PCB)", "gu": "Process Control Block (PCB)"},
    "os2_times": {"en": "AT, BT, CT, TAT and WT", "gu": "AT, BT, CT, TAT અને WT"},
    "os2_fcfs": {"en": "FCFS Gantt Chart (Practical 2a)", "gu": "FCFS Gantt Chart (Practical 2a)"},
    "os2_sjf": {"en": "SJF Gantt Chart (Practical 2a)", "gu": "SJF Gantt Chart (Practical 2a)"},
    "os2_rr": {"en": "Round Robin Gantt Chart (q = 2)", "gu": "Round Robin Gantt Chart (q = 2)"},
    "os2_priority": {"en": "Non-preemptive Priority Gantt Chart", "gu": "Non-preemptive Priority Gantt Chart"},
    "os2_queues": {"en": "Queueing Diagram", "gu": "Queueing Diagram"},
    "os2_schedulers": {"en": "Long, Short and Medium Term Schedulers", "gu": "Long, Short અને Medium Term Schedulers"},
    "os2_context": {"en": "Context Switch", "gu": "Context Switch"},
    "os2_race": {"en": "Race Condition Example", "gu": "Race Condition ઉદાહરણ"},
    "os2_cs": {"en": "Critical Section Structure", "gu": "Critical Section Structure"},
    "os2_mutex": {"en": "Mutual Exclusion", "gu": "Mutual Exclusion"},
    "os2_deadlock": {"en": "Deadlock (Circular Wait)", "gu": "Deadlock (Circular Wait)"},
    "os2_rag": {"en": "Resource Allocation Graph", "gu": "Resource Allocation Graph"},
    "os2_safe": {"en": "Safe, Unsafe and Deadlock States", "gu": "Safe, Unsafe અને Deadlock States"},
    "os2_waitfor": {"en": "Wait-for Graph", "gu": "Wait-for Graph"},
}

UNIT = {
    "subject": "DI03000041", "unit": 2, "format": "notes",
    "title": {"en": "Process Management", "gu": "Process Management"},
    "weightage": 31, "hours": 14,
    "notes": NOTES,
    "numericals": NUMERICALS, "equations": EQUATIONS, "viva": VIVA, "exam_questions": EXAM_QS,
}

if __name__ == "__main__":
    subprocess.run([sys.executable, os.path.join(os.path.dirname(os.path.abspath(__file__)), "diagrams_DI03000041_u2.py")], check=True,
                   stdout=subprocess.DEVNULL)
    check_and_write(UNIT, DIAGRAM_TITLES, "DI03000041_unit2_preview.html")
