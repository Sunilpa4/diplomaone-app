"""Builds DI03000011 Digital Electronics Fundamentals Unit 5 (Basic Sequential Circuits). Bilingual EN + GU."""
import os, sys, subprocess
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from subject_DI03000011 import check_and_write
from content_DI03000011_u5_notes import NOTES
from content_DI03000011_u5_extras import NUMERICALS, EQUATIONS, VIVA, EXAM_QS

DIAGRAM_TITLES = {
    "de5_seq": {"en": "Sequential Circuit: Block Diagram", "gu": "Sequential Circuit: Block Diagram"},
    "de5_clock": {"en": "Clock Signal and Triggering", "gu": "Clock Signal અને Triggering"},
    "de5_compare": {"en": "Combinational vs Sequential", "gu": "Combinational vs Sequential"},
    "de5_latch": {"en": "SR Latch using NOR Gates", "gu": "NOR Gates વડે SR Latch"},
    "de5_sr_nand": {"en": "SR Latch using NAND Gates", "gu": "NAND Gates વડે SR Latch"},
    "de5_sr": {"en": "Clocked SR Flip-Flop", "gu": "Clocked SR Flip-Flop"},
    "de5_jk": {"en": "JK Flip-Flop", "gu": "JK Flip-Flop"},
    "de5_d": {"en": "D Flip-Flop", "gu": "D Flip-Flop"},
    "de5_t": {"en": "T Flip-Flop", "gu": "T Flip-Flop"},
    "de5_symbols": {"en": "Flip-Flop Symbols", "gu": "Flip-Flop Symbols"},
    "de5_timing": {"en": "Timing Diagram: D Flip-Flop", "gu": "Timing Diagram: D Flip-Flop"},
    "de5_convert": {"en": "Flip-Flop Conversions", "gu": "Flip-Flop Conversions"},
}


UNIT = {
    "subject": "DI03000011", "unit": 5, "format": "notes",
    "title": {"en": "Basic Sequential Circuits", "gu": "Basic Sequential Circuits"},
    "weightage": 11, "hours": 3,
    "notes": NOTES,
    "numericals": NUMERICALS, "equations": EQUATIONS, "viva": VIVA, "exam_questions": EXAM_QS,
}

if __name__ == "__main__":
    subprocess.run([sys.executable, os.path.join(os.path.dirname(os.path.abspath(__file__)), "diagrams_DI03000011_u5.py")], check=True,
                   stdout=subprocess.DEVNULL)
    check_and_write(UNIT, DIAGRAM_TITLES, "DI03000011_unit5_preview.html")
