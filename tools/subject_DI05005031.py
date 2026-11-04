"""GTU Chemical Reaction Engineering (DI05005031) - Chemical Engineering, Semester 5, w.e.f. 2026-27.

Content policy for this subject (user decision): **both languages, English and Gujarati, in parallel**
- every text node carries both an "en" and a "gu" value, so the app language toggle shows the same
lesson in either language. Technical terms stay in English inside the Gujarati sentence, the way the
other Gujarati subjects of this app are written.

Every unit is written as **derivation first, formula second, equipment third**: each main result is
derived line by line from the rate law, and every reactor is drawn part by part (construction) and
then walked through its working (step 1, step 2, ...), which is what the syllabus asks for in Units
IV and V.

Syllabus source: tools/syllabus_DI05005031.txt (transcribed from the uploaded PDF, sha256 kept in
subject.json). Units, hours, weightages, marks split, course outcomes, books, practical list and
activities are copied from it.
"""
import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SUBJ_DIR = ROOT / "content/chemical/sem5/DI05005031"
DIAG_DIR = SUBJ_DIR / "diagrams"
TABS = ["notes", "diagrams", "equations", "viva", "exam"]

CODE = "DI05005031"
TITLE = "Chemical Reaction Engineering"
TITLE_GU = "રાસાયણિક પ્રક્રિયા ઇજનેરી"

SYLLABUS = ROOT / "tools/syllabus_DI05005031.txt"


def tr(en, gu=None):
    """A bilingual text node. Gujarati is required everywhere in this subject."""
    assert gu, f"Gujarati text missing for: {en[:60]!r}"
    return {"en": en, "gu": gu}


# (no, title_en, title_gu, hours, weightage, marks, co, topics[(en, gu)], outcome (en, gu))
UNITS = [
    (1, "Basics of Chemical Reactions", "રાસાયણિક પ્રક્રિયાઓના પાયા", 7, 15, 10, "CO1", [
        ("Scope and importance of chemical reaction engineering",
         "Chemical reaction engineering નું ક્ષેત્ર અને મહત્વ"),
        ("Classification of reactions: homogeneous vs heterogeneous, catalytic vs non-catalytic",
         "પ્રક્રિયાઓનું વર્ગીકરણ: homogeneous vs heterogeneous, catalytic vs non-catalytic"),
        ("Reversible vs irreversible, molecularity, exothermic vs endothermic, order of reaction",
         "Reversible vs irreversible, molecularity, exothermic vs endothermic, પ્રક્રિયાનો order"),
        ("Introduction to biochemical reactions",
         "Biochemical પ્રક્રિયાઓનો પરિચય"),
        ("Reaction rate on various bases and the variables that affect it",
         "જુદા જુદા આધાર પર reaction rate અને તેને અસર કરતા ચલો"),
    ], ("Describe the fundamental aspects of the various chemical reactions.",
        "વિવિધ રાસાયણિક પ્રક્રિયાઓની મૂળભૂત બાબતો સમજાવવી.")),
    (2, "Kinetics of Homogeneous Reactions", "સમરૂપ પ્રક્રિયાઓની ગતિકી", 8, 17, 12, "CO2", [
        ("Rate equation / rate law", "Rate equation / rate law"),
        ("Concentration dependent term, rate constant, elementary and non-elementary reactions",
         "Concentration વાળો ભાગ, rate constant, elementary અને non-elementary પ્રક્રિયાઓ"),
        ("Molecularity and order of reaction", "Molecularity અને પ્રક્રિયાનો order"),
        ("Temperature dependent term, the Arrhenius law", "Temperature વાળો ભાગ, Arrhenius law"),
        ("Activation energy", "Activation energy"),
    ], ("Determine the rate, rate constant, activation energy and order of reaction.",
        "પ્રક્રિયાનો rate, rate constant, activation energy અને order નક્કી કરવા.")),
    (3, "Interpretation of Batch Reactor Data", "બેચ રિએક્ટરના ડેટાનું અર્થઘટન", 9, 20, 14, "CO3", [
        ("Differential method, integral method and half-life method of analysis",
         "Analysis ની differential method, integral method અને half-life method"),
        ("Relations for a constant volume batch system",
         "Constant volume batch system માટેના સંબંધો"),
        ("Total pressure, partial pressure, concentration and conversion",
         "Total pressure, partial pressure, concentration અને conversion"),
        ("Integrated rate equations: zero, first, second, third and nth order",
         "Integrated rate equations: zero, first, second, third અને nth order"),
    ], ("Analyse kinetic data to find the rate equation of a batch reactor.",
        "Kinetic data નું analysis કરીને batch reactor નું rate equation શોધવું.")),
    (4, "Ideal Reactors", "આદર્શ રિએક્ટર", 11, 24, 17, "CO4", [
        ("Features of ideal reactors", "Ideal reactors ની લાક્ષણિકતાઓ"),
        ("Batch, semi-batch, flow, mixed flow (CSTR), plug flow (tubular), fixed bed and fluidized "
         "bed reactors - construction and working",
         "Batch, semi-batch, flow, mixed flow (CSTR), plug flow (tubular), fixed bed અને fluidized "
         "bed reactors - રચના અને કાર્યપદ્ધતિ"),
        ("Multiphase reactors: G-L-S, slurry, bubble column, spray and trickle bed reactors",
         "Multiphase reactors: G-L-S, slurry, bubble column, spray અને trickle bed reactors"),
    ], ("Control the different reactors efficiently using the knowledge of their functioning.",
        "રિએક્ટરોની કાર્યપદ્ધતિના જ્ઞાનથી તેમને કાર્યક્ષમ રીતે નિયંત્રિત કરવા.")),
    (5, "Design of Single Ideal Reactor", "એક આદર્શ રિએક્ટરની ડિઝાઇન", 11, 24, 17, "CO5", [
        ("Performance equation of a single ideal reactor for a single reaction, constant density",
         "એક પ્રક્રિયા, constant density માટે single ideal reactor નું performance equation"),
        ("Ideal batch reactor, steady state mixed flow reactor and steady state plug flow reactor",
         "Ideal batch reactor, steady state mixed flow reactor અને steady state plug flow reactor"),
        ("Flow reactors: space time, space velocity, holding time versus space time",
         "Flow reactors: space time, space velocity, holding time vs space time"),
    ], ("Estimate volume, space time and space velocity for ideal reactors.",
        "Ideal reactors માટે volume, space time અને space velocity ગણવા.")),
]

BRANCH = "chemical"
SEMESTER = 5

SUBJECT = {
    "code": CODE,
    "name": {"en": TITLE, "gu": TITLE_GU},
    "branch": BRANCH,
    "semester": SEMESTER,
    "syllabus_year": "2026-27",
    "category": "Professional Elective (PEC-III)",
    "type": "theory",
    "languages": ["en", "gu"],
    "code_lang": None,
    "teaching": {"lecture": 3, "tutorial": 0, "practical": 2},
    "exam": {"theory_ese": 70, "theory_pa": 30, "practical_pa": 20, "practical_ese": 30,
             "total": 150, "credits": 4},
    "prerequisites": tr(
        "Mathematics - calculus and differential equations, because every reactor equation is an "
        "integral of a rate law; physical chemistry - kinetics, equilibrium and thermodynamics; and "
        "material & energy balance with the elements of fluid flow, because a reactor is a vessel "
        "with a flow through it.",
        "ગણિત - calculus અને differential equations, કારણ કે દરેક reactor equation એ rate law નું "
        "integral છે; physical chemistry - kinetics, equilibrium અને thermodynamics; અને material & "
        "energy balance તથા fluid flow ના પાયા, કારણ કે reactor એ flow ધરાવતું vessel છે."),
    "rationale": tr(
        "A reactor is where the money of a chemical plant is made, and its design pulls together "
        "thermodynamics, kinetics, fluid mechanics, heat transfer, mass transfer and economics. This "
        "subject gives the diploma engineer the tools to select a reactor, size it, and fix its "
        "operating conditions from laboratory kinetic data.",
        "Chemical plant ની આવક reactor માંથી જ થાય છે, અને તેની design માં thermodynamics, kinetics, "
        "fluid mechanics, heat transfer, mass transfer તથા economics એકસાથે આવે છે. આ subject "
        "diploma engineer ને laboratory kinetic data પરથી reactor પસંદ કરવા, તેનું size નક્કી કરવા "
        "અને operating conditions ઠરાવવાના tools આપે છે."),
    "units": [
        {"no": no, "title": {"en": t_en, "gu": t_gu}, "hours": hours, "weightage": weightage,
         "theory_marks": marks, "official": True, "course_outcome": co,
         "topics": [tr(a, b) for a, b in topics],
         "outcomes": [tr(out_en, out_gu)]}
        for (no, t_en, t_gu, hours, weightage, marks, co, topics, (out_en, out_gu)) in UNITS
    ],
    "course_outcomes": [
        tr("CO1: Describe fundamental aspects of various chemical reactions. (R, U)",
           "CO1: વિવિધ રાસાયણિક પ્રક્રિયાઓની મૂળભૂત બાબતો સમજાવવી. (R, U)"),
        tr("CO2: Determine rate, rate constant, activation energy and order of reaction. (R, U, A)",
           "CO2: Rate, rate constant, activation energy અને order of reaction નક્કી કરવા. (R, U, A)"),
        tr("CO3: Analyze kinetic data to find out rate equation for batch reactor. (R, U, A)",
           "CO3: Kinetic data નું analysis કરીને batch reactor માટે rate equation શોધવું. (R, U, A)"),
        tr("CO4: Control different reactors efficiently using fundamental knowledge of their "
           "functioning. (U, A)",
           "CO4: રિએક્ટરોની કાર્યપદ્ધતિના પાયાના જ્ઞાનથી તેમને કાર્યક્ષમ રીતે નિયંત્રિત કરવા. (U, A)"),
        tr("CO5: Estimate volume, space time and space velocity for ideal reactors. (R, U, A)",
           "CO5: Ideal reactors માટે volume, space time અને space velocity ગણવા. (R, U, A)"),
    ],
    "course_outcome_rbt": {"CO1": "Understand", "CO2": "Apply", "CO3": "Analyze", "CO4": "Apply",
                           "CO5": "Apply"},
    "theory_marks_by_unit": {"1": 10, "2": 12, "3": 14, "4": 17, "5": 17},
    "theory_marks_note": tr(
        "The PDF prints only the percentage weightage (15 / 17 / 20 / 24 / 24), so the 70 theory "
        "marks are split by weightage with the largest remainder: 10 / 12 / 14 / 17 / 17 = 70. The "
        "practical half (PA 20 + ESE 30) is assessed on the fifteen listed experiments.",
        "PDF માં ફક્ત ટકાવારી weightage (15 / 17 / 20 / 24 / 24) આપેલી છે, તેથી 70 theory marks "
        "weightage પ્રમાણે largest remainder થી વહેંચ્યા છે: 10 / 12 / 14 / 17 / 17 = 70. Practical "
        "ભાગ (PA 20 + ESE 30) પંદર પ્રયોગો પર લેવાય છે."),
    "theory_rbt_percent": {"remember": 25, "understand": 41, "apply": 34, "analyze": 0,
                           "evaluate": 0, "create": 0},
    "theory_rbt_marks": {"remember": 18, "understand": 29, "apply": 23, "analyze": 0,
                         "evaluate": 0, "create": 0},
    "total_hours": 45,
    "hours_note": tr(
        "The unit hours printed in the PDF (7 + 8 + 9 + 11 + 11) add to 46, while the printed total "
        "is 45. The unit table is kept exactly as printed and the difference is recorded here "
        "instead of being silently corrected.",
        "PDF માં છપાયેલા unit hours (7 + 8 + 9 + 11 + 11) નો સરવાળો 46 થાય છે, જ્યારે છપાયેલો "
        "total 45 છે. Unit table છાપ્યા પ્રમાણે જ રાખેલું છે અને તફાવત ચૂપચાપ સુધારવાને બદલે અહીં "
        "નોંધ્યો છે."),
    "source_pdf_sha256": hashlib.sha256(SYLLABUS.read_bytes()).hexdigest(),
    "source_note": tr(
        "Syllabus text transcribed from the uploaded GTU DI05005031 PDF (Chemical Reaction "
        "Engineering, Chemical Engineering, semester 5, w.e.f. 2026-27). Units, hours, weightages, "
        "marks scheme, course outcomes, reference books, practical list and activities are copied "
        "from it.",
        "Syllabus નું લખાણ અપલોડ કરેલી GTU DI05005031 PDF (Chemical Reaction Engineering, Chemical "
        "Engineering, semester 5, w.e.f. 2026-27) માંથી ઉતારેલું છે. Units, hours, weightages, "
        "marks scheme, course outcomes, reference books, practical list અને activities તેમાંથી જ "
        "લીધેલા છે."),
    "official_practicals": [
        tr("Determine the activation energy of the reaction between sodium thiosulphate and HCl "
           "using the Arrhenius equation.",
           "Arrhenius equation વાપરીને sodium thiosulphate અને HCl વચ્ચેની પ્રક્રિયાની activation "
           "energy નક્કી કરવી."),
        tr("Determine the order of the reaction between sodium thiosulphate and HCl.",
           "Sodium thiosulphate અને HCl વચ્ચેની પ્રક્રિયાનો order નક્કી કરવો."),
        tr("Determine the kinetics of ethyl acetate and sodium hydroxide under conditions of excess "
           "ethyl acetate at room temperature.",
           "Room temperature પર excess ethyl acetate ની સ્થિતિમાં ethyl acetate અને sodium hydroxide "
           "ની kinetics નક્કી કરવી."),
        tr("Determine the kinetics of ethyl acetate and sodium hydroxide by the integral method at "
           "room temperature.",
           "Room temperature પર integral method થી ethyl acetate અને sodium hydroxide ની kinetics "
           "નક્કી કરવી."),
        tr("Determine the activation energy of the reaction between ethyl acetate and sodium "
           "hydroxide.", "Ethyl acetate અને sodium hydroxide વચ્ચેની પ્રક્રિયાની activation energy "
           "નક્કી કરવી."),
        tr("Determine the kinetics of ethyl acetate and sodium hydroxide by the differential method.",
           "Differential method થી ethyl acetate અને sodium hydroxide ની kinetics નક્કી કરવી."),
        tr("Determine the kinetics of n-butyl acetate and sodium hydroxide by the differential "
           "method.", "Differential method થી n-butyl acetate અને sodium hydroxide ની kinetics નક્કી "
           "કરવી."),
        tr("Determine the kinetics of n-butyl acetate and sodium hydroxide by the integral method.",
           "Integral method થી n-butyl acetate અને sodium hydroxide ની kinetics નક્કી કરવી."),
        tr("Determine the activation energy of the reaction between n-butyl acetate and sodium "
           "hydroxide using the Arrhenius equation.",
           "Arrhenius equation વાપરીને n-butyl acetate અને sodium hydroxide વચ્ચેની પ્રક્રિયાની "
           "activation energy નક્કી કરવી."),
        tr("Determine the rate constant and order of reaction for the catalytic decomposition of "
           "hydrogen peroxide.",
           "Hydrogen peroxide ના catalytic decomposition માટે rate constant અને order નક્કી કરવો."),
        tr("Study the pseudo-first-order kinetics of the crystal violet - sodium hydroxide reaction "
           "and determine the activation energy.",
           "Crystal violet - sodium hydroxide પ્રક્રિયાની pseudo-first-order kinetics ભણવી અને "
           "activation energy નક્કી કરવી."),
        tr("Kinetic study of a batch reactor.", "Batch reactor નો kinetic study."),
        tr("Kinetic study of a continuous stirred tank reactor.",
           "Continuous stirred tank reactor નો kinetic study."),
        tr("Kinetic study of a plug flow reactor.", "Plug flow reactor નો kinetic study."),
        tr("Kinetic study of a semi batch reactor.", "Semi batch reactor નો kinetic study."),
    ],
    "practicals": [],
    "suggested_projects": [
        tr("Collect the kinetic data of the saponification experiment of your laboratory, fit zero, "
           "first and second order equations to it and report which order the data supports, with "
           "the residues of each fit.",
           "તમારી laboratory ના saponification પ્રયોગનો kinetic data લઈ, તેના પર zero, first અને "
           "second order ના equations fit કરો અને data કયો order સમર્થન આપે છે તે દરેક fit ના "
           "residues સાથે રિપોર્ટ કરો."),
        tr("Compare the volume of a CSTR and a PFR needed for 80 % conversion of a second order "
           "reaction and show the ratio on a Levenspiel plot.",
           "Second order પ્રક્રિયાના 80 % conversion માટે જરૂરી CSTR અને PFR ના volume ની સરખામણી "
           "કરો અને ગુણોત્તર Levenspiel plot પર દર્શાવો."),
    ],
    "activities": [
        tr("Assignments", "Assignments"),
        tr("Technical quiz / MCQ test", "Technical quiz / MCQ test"),
        tr("Presentation on some course topic", "કોઈ course topic પર presentation"),
        tr("Internet based assignments", "Internet આધારિત assignments"),
        tr("Micro-project in a team or individually", "ટીમમાં અથવા એકલા micro-project"),
    ],
    "books": [
        "Octave Levenspiel - Chemical Reaction Engineering, Third Edition, John Wiley and Sons",
        "H. Scott Fogler - Essentials of Chemical Reaction Engineering, Fourth Edition, Prentice "
        "Hall International",
        "Lanny D. Schmidt - The Engineering of Chemical Reactions, Second Edition, Oxford "
        "University Press",
    ],
    "learning_resources": [
        "NPTEL / SWAYAM courses on Chemical Reaction Engineering - https://nptel.ac.in/",
        "Levenspiel plots and reactor design worked examples - https://www.swayam.gov.in/",
        "Laboratory glassware, conductivity meter, burette, thermostat bath and stop watch for the "
        "kinetics experiments",
    ],
}


def write_subject():
    SUBJ_DIR.mkdir(parents=True, exist_ok=True)
    DIAG_DIR.mkdir(exist_ok=True)
    for spec in SUBJECT["units"]:
        name = f"unit{spec['no']}.json"
        spec["file"] = name if (SUBJ_DIR / name).is_file() else None
    (SUBJ_DIR / "subject.json").write_text(
        json.dumps(SUBJECT, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")


GUJARATI = re.compile(r"[\u0a80-\u0aff]")


def check_bilingual(obj, path="unit"):
    """Both languages, everywhere: every dict of text carries en and gu, and gu really is Gujarati."""
    if isinstance(obj, dict):
        if "en" in obj or "gu" in obj:
            assert "en" in obj and "gu" in obj, f"{path}: text node with one language only: {obj}"
            # Short labels may legitimately stay as the English technical term ("Power law",
            # "Michaelis-Menten", "Order"); anything longer must be written in Gujarati.
            assert GUJARATI.search(obj["gu"]) or len(obj["gu"]) < 20, \
                f"{path}: gu value has no Gujarati script: {obj['gu'][:60]!r}"
            assert not GUJARATI.search(obj["en"]), f"{path}: Gujarati inside en: {obj['en'][:60]!r}"
            return
        for k, v in obj.items():
            check_bilingual(v, f"{path}.{k}")
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            check_bilingual(v, f"{path}[{i}]")


def spec_for(number):
    for spec in SUBJECT["units"]:
        if spec["no"] == number:
            return spec
    raise AssertionError(f"unit {number} is not registered for {CODE}")


def write_unit(unit):
    SUBJ_DIR.mkdir(parents=True, exist_ok=True)
    DIAG_DIR.mkdir(exist_ok=True)
    spec = spec_for(unit["unit"])
    assert unit["title"] == spec["title"], "unit title must match subject.json"
    assert (unit["hours"], unit["weightage"]) == (spec["hours"], spec["weightage"]), \
        "unit hours/weightage must match the syllabus"
    check_bilingual(unit)
    out = SUBJ_DIR / f"unit{unit['unit']}.json"
    out.write_text(json.dumps(unit, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    write_subject()
    return out


if __name__ == "__main__":
    write_subject()
    print("subject written:", SUBJ_DIR / "subject.json")
