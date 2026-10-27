"""Builds DI03000011 Digital Electronics Fundamentals Unit 1 (Number Systems and Binary Codes). Bilingual EN + GU."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import subprocess
from subject_DI03000011 import check_and_write
from content_DI03000011_u1_notes_a import NOTES_A
from content_DI03000011_u1_notes_b import NOTES_B
from content_DI03000011_u1_extras import NUMERICALS, EQUATIONS, VIVA, EXAM_QS

DIAGRAM_TITLES = {
    "de1_analog_digital": {"en": "Analog and Digital Signals", "gu": "Analog અને Digital Signals"},
    "de1_digital_system": {"en": "Block Diagram of a Digital System", "gu": "Digital System નો Block Diagram"},
    "de1_number_systems": {"en": "Number Systems: Base and Digits", "gu": "Number Systems: Base અને Digits"},
    "de1_positional": {"en": "Positional Weights of a Binary Number", "gu": "Binary સંખ્યાના Positional Weights"},
    "de1_division": {"en": "Decimal to Binary by Repeated Division", "gu": "Repeated Division વડે Decimal થી Binary"},
    "de1_fraction": {"en": "Decimal Fraction to Binary by Multiplication", "gu": "ગુણાકાર વડે Decimal Fraction થી Binary"},
    "de1_grouping": {"en": "Binary to Octal and Hexadecimal by Grouping", "gu": "Grouping વડે Binary થી Octal અને Hexadecimal"},
    "de1_conv_map": {"en": "Summary of Conversion Methods", "gu": "Conversion Methods નો સારાંશ"},
    "de1_binary_add": {"en": "Binary Addition with Carry", "gu": "Carry સાથે Binary Addition"},
    "de1_complement": {"en": "1's and 2's Complement", "gu": "1's અને 2's Complement"},
    "de1_sub_flow": {"en": "Flowchart: Subtraction using 2's Complement", "gu": "Flowchart: 2's Complement વડે Subtraction"},
}

UNIT = {
    "subject": "DI03000011", "unit": 1, "format": "notes",
    "title": {"en": "Number Systems and Binary Codes", "gu": "Number Systems અને Binary Codes"},
    "weightage": 20, "hours": 6,
    "notes": NOTES_A + NOTES_B,
    "numericals": NUMERICALS, "equations": EQUATIONS, "viva": VIVA, "exam_questions": EXAM_QS,
}

if __name__ == "__main__":
    subprocess.run([sys.executable, os.path.join(os.path.dirname(os.path.abspath(__file__)), "diagrams_DI03000011_u1.py")], check=True)
    check_and_write(UNIT, DIAGRAM_TITLES, "DI03000011_unit1_preview.html")
