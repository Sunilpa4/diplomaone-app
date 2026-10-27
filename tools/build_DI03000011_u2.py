"""Builds DI03000011 Digital Electronics Fundamentals Unit 2 (Binary Logic and Boolean Algebra). Bilingual EN + GU."""
import os, sys, subprocess
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from subject_DI03000011 import check_and_write
from content_DI03000011_u2_notes_a import NOTES_A
from content_DI03000011_u2_notes_b import NOTES_B
from content_DI03000011_u2_extras import NUMERICALS, EQUATIONS, VIVA, EXAM_QS

DIAGRAM_TITLES = {
    "de2_pos_neg": {"en": "Positive and Negative Logic", "gu": "Positive અને Negative Logic"},
    "de2_and": {"en": "AND Gate: Symbol, Truth Table and Switch Analogy", "gu": "AND Gate: Symbol, Truth Table અને Switch Analogy"},
    "de2_or": {"en": "OR Gate: Symbol, Truth Table and Switch Analogy", "gu": "OR Gate: Symbol, Truth Table અને Switch Analogy"},
    "de2_not": {"en": "NOT Gate: Symbol, Truth Table and Waveforms", "gu": "NOT Gate: Symbol, Truth Table અને Waveforms"},
    "de2_nand": {"en": "NAND Gate", "gu": "NAND Gate"},
    "de2_nor": {"en": "NOR Gate", "gu": "NOR Gate"},
    "de2_xor": {"en": "EX-OR Gate and its Implementation", "gu": "EX-OR Gate અને તેની રચના"},
    "de2_xnor": {"en": "EX-NOR Gate", "gu": "EX-NOR Gate"},
    "de2_summary": {"en": "Summary of Logic Gates", "gu": "Logic Gates નો સારાંશ"},
    "de2_nand_universal": {"en": "NAND as a Universal Gate", "gu": "Universal Gate તરીકે NAND"},
    "de2_nor_universal": {"en": "NOR as a Universal Gate", "gu": "Universal Gate તરીકે NOR"},
    "de2_ic7400": {"en": "IC 7400 Pin Diagram and Gate ICs", "gu": "IC 7400 Pin Diagram અને Gate ICs"},
    "de2_demorgan": {"en": "De Morgan's Theorems", "gu": "De Morgan's Theorems"},
    "de2_func_impl": {"en": "Implementing a Boolean Function", "gu": "Boolean Function ની રચના"},
    "de2_sop_pos": {"en": "SOP and POS Circuits", "gu": "SOP અને POS Circuits"},
}

UNIT = {
    "subject": "DI03000011", "unit": 2, "format": "notes",
    "title": {"en": "Binary Logic and Boolean Algebra", "gu": "Binary Logic અને Boolean Algebra"},
    "weightage": 23, "hours": 7,
    "notes": NOTES_A + NOTES_B,
    "numericals": NUMERICALS, "equations": EQUATIONS, "viva": VIVA, "exam_questions": EXAM_QS,
}

if __name__ == "__main__":
    subprocess.run([sys.executable, os.path.join(os.path.dirname(os.path.abspath(__file__)), "diagrams_DI03000011_u2.py")], check=True)
    check_and_write(UNIT, DIAGRAM_TITLES, "DI03000011_unit2_preview.html")
