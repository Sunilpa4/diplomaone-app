"""Builds DI03000041 Fundamentals of Operating System Unit 3 (Memory Management). Bilingual EN + GU."""
import os, sys, subprocess
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from subject_DI03000041 import check_and_write
from content_DI03000041_u3_notes import NOTES
from content_DI03000041_u3_extras import NUMERICALS, EQUATIONS, VIVA, EXAM_QS

DIAGRAM_TITLES = {
    "os3_mmu": {"en": "Logical to Physical Address (MMU)", "gu": "Logical થી Physical Address (MMU)"},
    "os3_swap": {"en": "Swapping of Two Processes", "gu": "બે Processes નું Swapping"},
    "os3_fixed": {"en": "Fixed Partitions: Internal Fragmentation", "gu": "Fixed Partitions: Internal Fragmentation"},
    "os3_dynamic": {"en": "Dynamic (Variable) Partitions", "gu": "Dynamic (Variable) Partitions"},
    "os3_frag": {"en": "Internal vs External Fragmentation", "gu": "Internal vs External Fragmentation"},
    "os3_compact": {"en": "Compaction", "gu": "Compaction"},
    "os3_protect": {"en": "Relocation and Protection Hardware", "gu": "Relocation અને Protection Hardware"},
    "os3_fit": {"en": "First, Best and Worst Fit (Practical 3)", "gu": "First, Best અને Worst Fit (Practical 3)"},
    "os3_paging": {"en": "Paging Model", "gu": "Paging Model"},
    "os3_paging_hw": {"en": "Address Translation in Paging", "gu": "Paging માં Address Translation"},
    "os3_segment": {"en": "Segmentation: Segment Table", "gu": "Segmentation: Segment Table"},
    "os3_seg_hw": {"en": "Address Translation in Segmentation", "gu": "Segmentation માં Address Translation"},
    "os3_pagefault": {"en": "Steps in Handling a Page Fault", "gu": "Page Fault handle કરવાના પગલાં"},
    "os3_fifo": {"en": "FIFO Page Replacement (Practical 4)", "gu": "FIFO Page Replacement (Practical 4)"},
    "os3_lru": {"en": "LRU Page Replacement (Practical 4)", "gu": "LRU Page Replacement (Practical 4)"},
}

UNIT = {
    "subject": "DI03000041", "unit": 3, "format": "notes",
    "title": {"en": "Memory Management", "gu": "Memory Management"},
    "weightage": 23, "hours": 10,
    "notes": NOTES,
    "numericals": NUMERICALS, "equations": EQUATIONS, "viva": VIVA, "exam_questions": EXAM_QS,
}

if __name__ == "__main__":
    subprocess.run([sys.executable, os.path.join(os.path.dirname(os.path.abspath(__file__)), "diagrams_DI03000041_u3.py")], check=True,
                   stdout=subprocess.DEVNULL)
    check_and_write(UNIT, DIAGRAM_TITLES, "DI03000041_unit3_preview.html")
