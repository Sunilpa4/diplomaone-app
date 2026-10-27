"""Builds DI03000011 Digital Electronics Fundamentals Unit 3 (Simplification using K-map). Bilingual EN + GU."""
import os, sys, subprocess
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from subject_DI03000011 import check_and_write
from content_DI03000011_u3_notes_a import NOTES_A
from content_DI03000011_u3_notes_b import NOTES_B
from content_DI03000011_u3_extras import NUMERICALS, EQUATIONS, VIVA, EXAM_QS

DIAGRAM_TITLES = {
    "de3_need": {"en": "Why Simplify: Before and After", "gu": "Simplification કેમ: પહેલાં અને પછી"},
    "de3_kmap2": {"en": "Two-Variable K-map", "gu": "Two-Variable K-map"},
    "de3_kmap3": {"en": "Three-Variable K-map (Cells and Minterms)", "gu": "Three-Variable K-map (Cells અને Minterms)"},
    "de3_kmap4": {"en": "Four-Variable K-map (Minterm Numbers)", "gu": "Four-Variable K-map (Minterm Numbers)"},
    "de3_groups": {"en": "Pairs, Quads, Octets and Wrap-around Groups", "gu": "Pairs, Quads, Octets અને Wrap-around Groups"},
    "de3_steps": {"en": "Steps of K-map Simplification", "gu": "K-map Simplification ના Steps"},
    "de3_ex3": {"en": "Solved 3-Variable K-map", "gu": "Solved 3-Variable K-map"},
    "de3_ex4": {"en": "Solved 4-Variable K-map", "gu": "Solved 4-Variable K-map"},
    "de3_pos": {"en": "POS Simplification by Grouping 0s", "gu": "0s ના Grouping વડે POS Simplification"},
    "de3_dontcare": {"en": "K-map with Don't-Care Conditions", "gu": "Don't-Care Conditions સાથે K-map"},
    "de3_bcd": {"en": "BCD ≥ 5 Detector using Don't-Cares", "gu": "Don't-Cares વડે BCD ≥ 5 Detector"},
    "de3_impl": {"en": "Implementation with Basic Gates", "gu": "Basic Gates વડે Implementation"},
}

UNIT = {
    "subject": "DI03000011", "unit": 3, "format": "notes",
    "title": {"en": "Simplification using Karnaugh Map", "gu": "Karnaugh Map દ્વારા Simplification"},
    "weightage": 23, "hours": 7,
    "notes": NOTES_A + NOTES_B,
    "numericals": NUMERICALS, "equations": EQUATIONS, "viva": VIVA, "exam_questions": EXAM_QS,
}

if __name__ == "__main__":
    subprocess.run([sys.executable, os.path.join(os.path.dirname(os.path.abspath(__file__)), "diagrams_DI03000011_u3.py")], check=True,
                   stdout=subprocess.DEVNULL)
    check_and_write(UNIT, DIAGRAM_TITLES, "DI03000011_unit3_preview.html")
