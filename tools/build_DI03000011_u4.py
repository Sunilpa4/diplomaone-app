"""Builds DI03000011 Digital Electronics Fundamentals Unit 4 (Basic Combinational Circuits). Bilingual EN + GU."""
import os, sys, subprocess
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from subject_DI03000011 import check_and_write
from content_DI03000011_u4_notes_a import NOTES_A
from content_DI03000011_u4_notes_b import NOTES_B
from content_DI03000011_u4_extras import NUMERICALS, EQUATIONS, VIVA, EXAM_QS

DIAGRAM_TITLES = {
    "de4_comb": {"en": "Combinational Circuit: Block Diagram and Types", "gu": "Combinational Circuit: Block Diagram અને પ્રકારો"},
    "de4_design": {"en": "Design Procedure", "gu": "Design Procedure"},
    "de4_ha": {"en": "Half Adder: Block Diagram and Truth Table", "gu": "Half Adder: Block Diagram અને Truth Table"},
    "de4_ha_logic": {"en": "Half Adder: Logic Diagram", "gu": "Half Adder: Logic Diagram"},
    "de4_fa": {"en": "Full Adder: Block Diagram and Truth Table", "gu": "Full Adder: Block Diagram અને Truth Table"},
    "de4_fa_kmap": {"en": "Full Adder: K-maps", "gu": "Full Adder: K-maps"},
    "de4_fa_logic": {"en": "Full Adder: Logic Diagram", "gu": "Full Adder: Logic Diagram"},
    "de4_fa_2ha": {"en": "Full Adder using Two Half Adders", "gu": "બે Half Adders વડે Full Adder"},
    "de4_hs": {"en": "Half Subtractor", "gu": "Half Subtractor"},
    "de4_fs": {"en": "Full Subtractor: Block Diagram and Truth Table", "gu": "Full Subtractor: Block Diagram અને Truth Table"},
    "de4_fs_logic": {"en": "Full Subtractor: K-map and Logic Diagram", "gu": "Full Subtractor: K-map અને Logic Diagram"},
    "de4_enc": {"en": "4-to-2 Encoder", "gu": "4-to-2 Encoder"},
    "de4_dec": {"en": "2-to-4 Decoder", "gu": "2-to-4 Decoder"},
    "de4_mux": {"en": "4-to-1 Multiplexer: Block Diagram", "gu": "4-to-1 Multiplexer: Block Diagram"},
    "de4_mux_logic": {"en": "4-to-1 Multiplexer: Logic Diagram", "gu": "4-to-1 Multiplexer: Logic Diagram"},
    "de4_demux": {"en": "1-to-4 Demultiplexer: Block Diagram", "gu": "1-to-4 Demultiplexer: Block Diagram"},
    "de4_demux_logic": {"en": "1-to-4 Demultiplexer: Logic Diagram", "gu": "1-to-4 Demultiplexer: Logic Diagram"},
    "de4_compare": {"en": "Data Transmission Circuits at a Glance", "gu": "Data Transmission Circuits એક નજરે"},
}


UNIT = {
    "subject": "DI03000011", "unit": 4, "format": "notes",
    "title": {"en": "Basic Combinational Circuits", "gu": "Basic Combinational Circuits"},
    "weightage": 23, "hours": 7,
    "notes": NOTES_A + NOTES_B,
    "numericals": NUMERICALS, "equations": EQUATIONS, "viva": VIVA, "exam_questions": EXAM_QS,
}

if __name__ == "__main__":
    subprocess.run([sys.executable, os.path.join(os.path.dirname(os.path.abspath(__file__)), "diagrams_DI03000011_u4.py")], check=True,
                   stdout=subprocess.DEVNULL)
    check_and_write(UNIT, DIAGRAM_TITLES, "DI03000011_unit4_preview.html")
