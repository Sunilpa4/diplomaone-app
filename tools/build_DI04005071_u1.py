# -*- coding: utf-8 -*-
"""Build DI04005071 Unit 1: subject.json + unit1.json + 360-wide SVG diagrams
+ standalone bilingual preview HTML. Run: python3 tools/build_DI04005071_u1.py"""
import json, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))
from content_DI04005071_u1 import NOTES, tr
from content_DI04005071_u1_extras import NUMERICALS, SYNTAX, VIVA, EXAM, ANSWERED, SOURCES

SUBJ_DIR = ROOT / "content/chemical/sem4/DI04005071"
DIAG_DIR = SUBJ_DIR / "diagrams"
CODE = "DI04005071"

# ------------------------------------------------------------------ diagrams
P, BL, G, O, R = "#7B2CD9", "#1565C0", "#2E7D32", "#B66A00", "#BD2543"
def _t(x, y, s, size=10.5, fill="#272134", bold=False, anchor="middle"):
    w = ' font-weight="bold"' if bold else ""
    return f'<text x="{x}" y="{y}" font-size="{size}" fill="{fill}" text-anchor="{anchor}"{w}>{s}</text>'
def _r(x, y, w, h, stroke, fill="#ffffff"):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="7" fill="{fill}" stroke="{stroke}" stroke-width="1.4"/>'
def _a(x1, y1, x2, y2, color="#444444"):
    return (f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="1.4"/>'
            f'<polygon points="{x2},{y2} {x2-4},{y2-7} {x2+4},{y2-7}" fill="{color}"/>')
def svg(title, height, body):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="360" height="{height}" '
            f'viewBox="0 0 360 {height}" font-family="DejaVu Sans, Arial, sans-serif">'
            f'<rect width="360" height="{height}" fill="#ffffff"/>'
            + _t(180, 20, title, 13, P, True) + body + "</svg>")

def d_trap():
    b = _r(18, 40, 324, 235, "#B9A6CE", "#FBF8FE")
    b += _t(180, 58, "Ground surface / sea bed", 10, "#666666")
    # anticline trap lens
    b += '<path d="M70 120 Q180 70 290 120 L290 200 L70 200 Z" fill="#FFF3E0" stroke="#B66A00" stroke-width="1.4"/>'
    b += '<path d="M70 120 Q180 70 290 120 L290 140 Q180 95 70 140 Z" fill="#FCE4EC" stroke="#BD2543" stroke-width="1"/>'
    b += '<path d="M70 140 Q180 95 290 140 L290 168 Q180 125 70 168 Z" fill="#FFF8E1" stroke="#B66A00" stroke-width="1"/>'
    b += _t(180, 128, "GAS", 10, R, True) + _t(180, 158, "OIL", 10, O, True) + _t(180, 188, "WATER", 10, BL, True)
    b += _r(18, 215, 324, 32, "#8D6E63", "#EFEBE9") + _t(180, 235, "Source rock (kerogen) — oil forms here", 10, "#4E342E", True)
    b += _t(180, 263, "Cap rock (shale) seals the arch (anticline trap)", 9.5, "#666666")
    b += _t(180, 292, "Reservoir rock stores oil; migration is upward", 9.5, "#666666")
    b += _t(180, 308, "Oil window about 60-150 °C (deeper = hotter)", 9.5, "#666666")
    return svg("Petroleum trap: where oil collects", 318, b)

def d_families():
    rows = [("Paraffins (alkanes)", "CnH2n+2 — chains; fuels, wax", BL, "#E3F2FD"),
            ("Naphthenes (cycloparaffins)", "CnH2n — rings; lubes, solvents", G, "#E8F5E9"),
            ("Aromatics", "benzene rings; octane, heavier", O, "#FFF3E0"),
            ("Resins + asphaltenes", "largest molecules; residue, coke", R, "#FCE4EC")]
    b, y = "", 46
    for name, desc, c, f in rows:
        b += _r(18, y, 324, 52, c, f) + _t(180, y+21, name, 11, c, True) + _t(180, y+40, desc, 9.5, "#444444")
        y += 62
    b += _t(180, y+6, "Plus: S, N, O compounds + salt and water", 9.5, "#666666")
    return svg("Four hydrocarbon families of crude oil", y+16, b)

def d_block():
    steps = [("Crude oil (desalter feed)", BL, "#E3F2FD"), ("Desalter — remove salt + water", BL, "#E3F2FD"),
             ("Pipe-still heater — preheat crude", O, "#FFF3E0"), ("Atmospheric column (ADU)", P, "#F3E5F5"),
             ("Vacuum column (VDU)", P, "#F3E5F5"), ("Conversion + treating units", G, "#E8F5E9"),
             ("Finished products (Unit 1.6 slate)", G, "#E8F5E9")]
    b, y = "", 42
    for i, (s, c, f) in enumerate(steps):
        b += _r(52, y, 256, 34, c, f) + _t(180, y+21, s, 10, c, True)
        if i < len(steps)-1:
            b += _a(180, y+35, 180, y+47)
        y += 48
    return svg("Refinery block flow (common skeleton)", y+2, b)

def d_slate():
    rows = [("LPG", "below 40 °C", 28, BL), ("Petrol", "30-180 °C", 56, G),
            ("Kerosene / ATF", "150-275 °C", 82, O), ("Diesel", "200-360 °C", 100, O),
            ("Vacuum gas oil", "above 360 °C", 108, R), ("Residue / bitumen", "heaviest", 108, "#4E342E")]
    b = _t(180, 44, "Lighter (top of column)  →  heavier (bottom)", 9.5, "#666666")
    y = 56
    for name, rng, w, c in rows:
        b += _t(18, y+14, name, 9.5, "#272134", True, "start")
        b += f'<rect x="118" y="{y}" width="{w}" height="16" rx="4" fill="{c}" opacity="0.75"/>'
        b += _t(234, y+14, rng, 9, "#444444", False, "start")
        y += 26
    b += _t(180, y+8, "Ranges are approximate; cuts overlap by design", 9.5, "#666666")
    return svg("Product slate by boiling range", y+18, b)

DIAGRAMS = [
    ("ref1_trap", "Petroleum trap: gas over oil over water in an anticline", d_trap()),
    ("ref1_families", "Four hydrocarbon families of crude oil", d_families()),
    ("ref1_refinery_block", "Refinery block flow: desalter to finished products", d_block()),
    ("ref1_product_slate", "Refinery product slate in boiling-range order", d_slate()),
]

# ------------------------------------------------------------------- subject
SUBJECT = {
 "code": CODE, "name": tr("Petroleum Refining and Petroleum Technology", "પેટ્રોલિયમ રિફાઇનિંગ તથા પેટ્રોલિયમ ટેકનોલોજી"),
 "branch": "chemical", "semester": 4, "syllabus_year": "2025-26",
 "category": "Professional Elective - II", "type": "theory",
 "languages": ["en", "gu"], "code_lang": None,
 "teaching": {"lecture": 3, "tutorial": 0, "practical": 2},
 "exam": {"theory_ese": 70, "theory_pa": 30, "practical_pa": 20, "practical_ese": 30, "total": 150, "credits": 4},
 "prerequisites": [tr("Unit Operations and basics of Chemical Process Technology (official prerequisite, GTU syllabus DI04005071)",
                       "Unit Operations તથા Chemical Process Technology ના basics (સત્તાવાર prerequisite, GTU syllabus DI04005071)")],
 "units": [
  {"no": 1, "title": tr("Basics of Petroleum and Refinery", "Petroleum તથા Refinery ના મૂળભૂત સિદ્ધાંતો"), "hours": 4, "weightage": 11,
   "topics": ["1.1 Occurrence of petroleum", "1.2 Composition of Petroleum", "1.3 Classification of Petroleum", "1.4 Types of Refineries", "1.5 Refinery processes: 1.5.1 Physical Changes, 1.5.2 Chemical Changes", "1.6 Refinery Products"], "file": "unit1.json"},
  {"no": 2, "title": tr("Fractionation of Petroleum", "Petroleum નું Fractionation"), "hours": 9, "weightage": 16,
   "topics": ["2.1 Primary treatment of crude: (a) Dehydration and Desalting, (b) Pipe still heaters", "2.2 Atmospheric distillation of crude", "2.3 Vacuum distillation of crude residue", "2.4 Physical properties of petroleum products and its measurements: (a) Petrol (b) Diesel (c) Kerosene (d) Lubricant oil (e) CNG and LPG (f) Grease"], "file": None},
  {"no": 3, "title": tr("Refinery Processes", "Refinery Processes"), "hours": 10, "weightage": 20,
   "topics": ["3.1 Cracking: purpose; effect of temperature and pressure; Thermal (Visbreaking, Delayed Coking, Fluid Coking), Catalytic, FCC, Hydrocracking; compare thermal and catalytic", "3.2 Reforming: purpose, Platforming", "3.3 Hydrotreating"], "file": None},
  {"no": 4, "title": tr("Treatment Techniques", "Treatment Techniques"), "hours": 11, "weightage": 24,
   "topics": ["4.1 Purposes and methods of sulfur removal", "4.2 Methods: Doctor's sweetening, Catalytic desulfurization, MEROX treatment", "4.3 Treatment of Kerosene by liquid SO2 extraction", "4.4 Solvent extraction: Furfural, Phenol", "4.5 Purpose of dewaxing", "4.6 Dewaxing: without solvent, with solvent (Ketone dewaxing)"], "file": None},
  {"no": 5, "title": tr("Petrochemicals", "Petrochemicals"), "hours": 11, "weightage": 29,
   "topics": ["5.1 Basics: Definition, Classification and feedstocks", "5.2 C1 compounds: Methanol, Formaldehyde", "5.3 C2 compounds: Vinyl chloride, Ethylene oxide", "5.4 C3 compounds: Propylene oxide", "5.5 Chemicals from aromatics: Manufacture of LAB"], "file": None},
 ],
 "course_outcomes": [
  tr("CO1: Identify properties of crude petroleum and petroleum products (RBT: U, A)", "CO1: Crude petroleum તથા petroleum products ના properties ઓળખો (RBT: U, A)"),
  tr("CO2: Explain fractionation of crude petroleum and treatment techniques (RBT: R, U)", "CO2: Crude petroleum નું fractionation તથા treatment techniques સમજાવો (RBT: R, U)"),
  tr("CO3: Apply refinery processes to maximize desired petro products (RBT: R, U, A)", "CO3: ઇચ્છિત petro products મહત્તમ કરવા refinery processes લાગુ કરો (RBT: R, U, A)"),
  tr("CO4: Explain manufacturing processes of petrochemicals (RBT: R, U)", "CO4: Petrochemicals ની manufacturing processes સમજાવો (RBT: R, U)")],
 "theory_rbt_percent": {"R": 27, "U": 24, "A": 19},
 "practicals": [
  {"number": i+1, "title": tr(t, t)} for i, t in enumerate([
   "Prepare a detail chart of modern refinery", "Prepare a detail chart of petrochemical products",
   "Determine flash point of petroleum product by Pensky-Martens method", "Determine fire point of petroleum product by Pensky-Martens method",
   "Measure softening point of petroleum product", "Measure Aniline point of petroleum product",
   "Determine penetration number of Grease", "Determine Carbon residue by Ramsbottom method",
   "Determine Carbon residue by Conradson method", "Measure smoke point of kerosene",
   "Measure cloud point of given petroleum product", "Measure pour point of given petroleum product",
   "Measure initial & final boiling point of petroleum product", "Measure Viscosity of lube oil by Redwood / Saybolt / Engler"])],
 "books": [
  {"title": "Modern Petroleum Refining Processes — Bhaskar Rao, Oxford and IBH, 2007"},
  {"title": "Outlines of Chemical Technology — Gopala Rao & Sittig, 3rd ed., East-West Press, Delhi"},
  {"title": "Shreve's Chemical Process Industries — Austin, 5th ed., McGraw Hill, New Delhi"},
  {"title": "A Text on Petrochemicals — Bhaskar Rao, 2nd ed., Khanna Publishers, Delhi, 1998"},
  {"title": "Petroleum Refinery Engineering — Nelson, McGraw Hill, New York, 1958"}],
 "source_note": "Official GTU syllabus DI04005071 (w.e.f. 2025-26), 5 pages, uploaded by the owner; text copy in tools/syllabus_DI04005071.txt.",
 "source_discrepancies": ["Theory RBT table in the official PDF gives R=27, U=24, A=19 and dashes for N, E, C (27+24+19=70); recorded exactly as printed, no values invented."],
 "available_units": [1],
}

# ---------------------------------------------------------------------- unit
unit = {
 "subject": CODE, "unit": 1, "format": "notes",
 "title": tr("Basics of Petroleum and Refinery", "Petroleum તથા Refinery ના મૂળભૂત સિદ્ધાંતો"),
 "hours": 4, "weightage": 11, "languages": ["en", "gu"],
 "tabs": ["notes", "diagrams", "numericals", "syntax", "viva", "exam"],
 "tab_labels": {"numericals": tr("Solved numericals", "ઉકેલેલા દાખલા"), "syntax": tr("Formulae and conversions", "સૂત્રો તથા conversions")},
 "intro_text": tr("Unit 1 of Petroleum Refining and Petroleum Technology (DI04005071, Chemical Semester 4, GTU 2025-26): where petroleum comes from, what crude oil contains, how crudes are classified, what kinds of refinery exist, which refinery processes only separate and which ones convert, and the full product slate of a refinery. Theory is written to the approved Chemical depth (Definition, Detailed theory, Key points, Qualification); every numerical follows the locked style — Given, Find, Formula, Substitution one equation per line, boxed Final answer with units, Validity check.",
                  "Petroleum Refining and Petroleum Technology (DI04005071, Chemical Semester 4, GTU 2025-26) નું Unit 1: petroleum ક્યાંથી આવે છે, crude oil માં શું હોય છે, crudes નું classification કેવી રીતે થાય છે, કયા પ્રકારની refineries હોય છે, કયા refinery processes ફક્ત separate કરે છે અને કયા convert કરે છે, અને refinery નો સંપૂર્ણ product slate. Theory માન્ય Chemical depth મુજબ લખાયું છે (વ્યાખ્યા, વિગતવાર Theory, મુખ્ય મુદ્દા, મર્યાદા); દરેક numerical locked style મુજબ છે — આપેલ, શોધો, સૂત્ર, Substitution એક equation એક line માં, Units સાથે boxed અંતિમ જવાબ, Validity Check."),
 "notes": NOTES + [ANSWERED],
 "diagrams": [{"id": i, "title": tr(t, t), "file": f"diagrams/{i}.svg"} for (i, t, _s) in DIAGRAMS],
 "numericals": NUMERICALS,
 "syntax": SYNTAX,
 "viva": VIVA,
 "exam_questions": EXAM,
 "practicals": [{"number": 1, "title": tr("Prepare a detailed chart of a modern refinery", "Modern refinery નો detailed chart બનાવો"),
                 "body": NOTES[-1]["items"][0]["body"]}],
 "learning_outcomes": [SUBJECT["course_outcomes"][0], SUBJECT["course_outcomes"][1]],
 "practical_numbers": [1],
 "content_kind": "theory_with_guided_practical_support",
 "assessment_note": tr("Official scheme (GTU DI04005071): Theory ESE 70 + PA 30, Practical PA 20 + ESE 30, total 150 marks, 4 credits. Unit 1 carries 4 hours and 11 % weightage in the official syllabus. All exam questions in this unit are original practice questions; their marks are suggested, not from an official paper.",
                       "સત્તાવાર scheme (GTU DI04005071): Theory ESE 70 + PA 30, Practical PA 20 + ESE 30, કુલ 150 marks, 4 credits. Unit 1 ને સત્તાવાર syllabus માં 4 hours તથા 11 % weightage છે. આ unit ના બધા exam questions original practice questions છે; તેમના marks suggested છે, સત્તાવાર paper માંથી નથી."),
 "question_provenance": "Original answered revision questions; not official past papers",
 "question_marks_are_suggested": True,
 "lesson_count": sum(len(s["items"]) for s in NOTES),
 "answered_practice_count": len(ANSWERED["items"]),
 "sources": SOURCES,
}

def main():
    DIAG_DIR.mkdir(parents=True, exist_ok=True)
    try:
        from diagrams_real import REAL
    except Exception:
        REAL = {}
    for (did, _t_, svg_text) in DIAGRAMS:
        (DIAG_DIR / f"{did}.svg").write_text(REAL.get(did, svg_text), encoding="utf-8")
    (SUBJ_DIR / "subject.json").write_text(json.dumps(SUBJECT, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    (SUBJ_DIR / "unit1.json").write_text(json.dumps(unit, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(f"wrote {SUBJ_DIR/'subject.json'}")
    print(f"wrote {SUBJ_DIR/'unit1.json'} ({(SUBJ_DIR/'unit1.json').stat().st_size/1024:.1f} KB)")
    for (did, _t_, _s) in DIAGRAMS:
        print(f"wrote diagrams/{did}.svg")

if __name__ == "__main__":
    main()
