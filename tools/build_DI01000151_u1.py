"""Builds app data (JSON) + a self-contained HTML preview for Basics of Electronics Unit 1."""
import json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from content_DI01000151_u1_notes_a import SEC_1_1, SEC_1_2
from content_DI01000151_u1_notes_b import SEC_1_3, SEC_1_4, SEC_1_5
from content_DI01000151_u1_extras import SEC_NUMERICALS, EQUATIONS, VIVA, EXAM_QS

ROOT = os.path.join(HERE, "..")
SUBJ_DIR = os.path.join(ROOT, "content", "computer", "sem1", "DI01000151")
DIAG_DIR = os.path.join(SUBJ_DIR, "diagrams")

DIAGRAM_TITLES = {
    "u1_symbols": {"en": "Symbols of R, C and L", "gu": "R, C અને L ની સંજ્ઞાઓ"},
    "u1_resistor_tree": {"en": "Classification of Resistors", "gu": "રેઝિસ્ટરનું વર્ગીકરણ"},
    "u1_colour_code": {"en": "Resistor Colour Code (Example)", "gu": "રેઝિસ્ટર કલર કોડ (ઉદાહરણ)"},
    "u1_parallel_plate": {"en": "Parallel Plate Capacitor", "gu": "સમાંતર પ્લેટ કેપેસિટર"},
    "u1_capacitor_tree": {"en": "Classification of Capacitors", "gu": "કેપેસિટરનું વર્ગીકરણ"},
    "u1_mutual_induction": {"en": "Mutual Induction", "gu": "પરસ્પર પ્રેરણ (મ્યુચ્યુઅલ ઇન્ડક્શન)"},
    "u1_dc_power_supply": {"en": "Block Diagram of Regulated DC Power Supply", "gu": "રેગ્યુલેટેડ DC પાવર સપ્લાયનો બ્લોક ડાયાગ્રામ"},
}

SUBJECT = {
    "code": "DI01000151",
    "name": {"en": "Basics of Electronics", "gu": "બેઝિક્સ ઓફ ઇલેક્ટ્રોનિક્સ"},
    "branch": "computer", "semester": 1, "syllabus_year": "2024-25",
    "exam": {"theory_ese": 70, "theory_pa": 30, "practical_pa": 20, "practical_ese": 30, "total": 150, "credits": 3},
    "units": [
        {"no": 1, "title": {"en": "Electronic Components", "gu": "ઇલેક્ટ્રોનિક ઘટકો"}, "hours": 6, "weightage": 20,
         "topics": ["1.1 Introduction to electronics, history, active & passive components",
                    "1.2 Resistors: specifications, classification, fixed & variable, colour coding",
                    "1.3 Capacitors: classification, specifications, fixed & variable",
                    "1.4 Inductors: Faraday's laws, self & mutual inductance, specifications",
                    "1.5 DC & AC power supply analysis"], "file": "unit1.json"},
        {"no": 2, "title": {"en": "Fundamentals of Semiconductors", "gu": "સેમિકન્ડક્ટરના મૂળભૂત સિદ્ધાંતો"}, "hours": 6, "weightage": 15,
         "topics": ["2.1 Atomic structure: trivalent, tetravalent, pentavalent; valence & free electrons, energy levels",
                    "2.2 Doping, intrinsic and extrinsic semiconductors",
                    "2.3 P-type and N-type, majority & minority carriers, conductivity"], "file": None},
        {"no": 3, "title": {"en": "Diodes and Rectifiers", "gu": "ડાયોડ અને રેક્ટિફાયર"}, "hours": 8, "weightage": 30,
         "topics": ["3.1 P-N junction, depletion layer, knee voltage", "3.2 Forward & reverse bias",
                    "3.3 V-I characteristics", "3.4 Zener diode", "3.5 Varactor, photodiode, LED, multi-colour LED",
                    "3.6 Rectifiers: half wave and full wave"], "file": None},
        {"no": 4, "title": {"en": "Transistors", "gu": "ટ્રાન્ઝિસ્ટર"}, "hours": 6, "weightage": 20,
         "topics": ["4.1 PNP, NPN", "4.2 Working", "4.3 CB, CE, CC configurations & characteristics",
                    "4.4 Voltage gain and current gain", "4.5 Transistor as a switch"], "file": None},
        {"no": 5, "title": {"en": "555 Timer IC and Applications", "gu": "555 ટાઇમર IC અને ઉપયોગો"}, "hours": 4, "weightage": 15,
         "topics": ["5.1 IC 555", "5.2 Description of 8 pins", "5.3 Functional block diagram",
                    "5.4 Applications: pulse generators, oscillators, timers, frequency counters"], "file": None},
    ],
}

UNIT = {
    "subject": "DI01000151", "unit": 1,
    "title": {"en": "Electronic Components", "gu": "ઇલેક્ટ્રોનિક ઘટકો"},
    "weightage": 20, "hours": 6,
    "notes": [SEC_1_1, SEC_1_2, SEC_1_3, SEC_1_4, SEC_1_5, SEC_NUMERICALS],
    "diagrams": [{"id": k, "title": v, "file": f"diagrams/{k}.svg"} for k, v in DIAGRAM_TITLES.items()],
    "equations": EQUATIONS,
    "viva": VIVA,
    "exam_questions": EXAM_QS,
}


def write_subject():
    """subject.json lists every unit; 'file' is filled only for units whose JSON exists."""
    for u in SUBJECT["units"]:
        fn = f'unit{u["no"]}.json'
        u["file"] = fn if os.path.exists(os.path.join(SUBJ_DIR, fn)) else None
    with open(os.path.join(SUBJ_DIR, "subject.json"), "w", encoding="utf-8") as f:
        json.dump(SUBJECT, f, ensure_ascii=False, indent=1)


def write_json():
    with open(os.path.join(SUBJ_DIR, "unit1.json"), "w", encoding="utf-8") as f:
        json.dump(UNIT, f, ensure_ascii=False, indent=1)
    write_subject()


from preview_builder import build_preview



def write_preview():
    return build_preview(UNIT, SUBJECT, DIAG_DIR, os.path.join(ROOT, "preview", "DI01000151_unit1_preview.html"))


if __name__ == "__main__":
    write_json()
    out = write_preview()
    n_notes = sum(len(s["items"]) for s in UNIT["notes"])
    n_eq = sum(len(g["items"]) for g in EQUATIONS)
    n_viva = sum(len(g["items"]) for g in VIVA)
    print(f"notes={n_notes} diagrams={len(DIAGRAM_TITLES)} equations={n_eq} viva={n_viva} exam={len(EXAM_QS)}")
    print("preview:", out)
