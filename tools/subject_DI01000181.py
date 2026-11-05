"""GTU Engineering Materials Science (DI01000181) - Mechanical Engineering, Semester 1, w.e.f. 2024-25.

Content policy for this subject (user decision): **both languages, English and Gujarati, in parallel**
- every text node carries both an "en" and a "gu" value, so the app language toggle shows the same
lesson in either language. Technical terms stay in English inside the Gujarati sentence, the way the
other Gujarati subjects of this app are written.

Every unit is written as **picture first, number second, application third**: each structure or
process is drawn part by part (unit cell, grain, phase diagram, furnace, coating) and then the number
that goes with it is computed (packing fraction, density, stress, plating thickness, corrosion rate),
because this subject is examined on recognition, explanation and simple calculation.

Syllabus source: tools/syllabus_DI01000181.txt (transcribed from the uploaded PDF, sha256 kept in
subject.json). Units, hours, weightages, marks split, course outcomes, books, practical list and
activities are copied from it.
"""
import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SUBJ_DIR = ROOT / "content/mechanical/sem1/DI01000181"
DIAG_DIR = SUBJ_DIR / "diagrams"
TABS = ["notes", "diagrams", "equations", "viva", "exam"]

CODE = "DI01000181"
TITLE = "Engineering Materials Science"
TITLE_GU = "ઇજનેરી સામગ્રી વિજ્ઞાન"

SYLLABUS = ROOT / "tools/syllabus_DI01000181.txt"


def tr(en, gu=None):
    """A bilingual text node. Gujarati is required everywhere in this subject."""
    assert gu, f"Gujarati text missing for: {en[:60]!r}"
    return {"en": en, "gu": gu}


# (no, title_en, title_gu, hours, weightage, marks, co, topics[(en, gu)], outcome (en, gu))
UNITS = [
    (1, "Introduction of Engineering Materials", "ઇજનેરી સામગ્રીનો પરિચય", 6, 14, 10, "CO1", [
        ("Classification of materials", "સામગ્રીનું વર્ગીકરણ"),
        ("Types of bonds: electrovalent, covalent, coordinate, hydrogen and metallic - construction "
         "and characteristics",
         "બંધનના પ્રકાર: electrovalent, covalent, coordinate, hydrogen અને metallic - રચના અને "
         "લક્ષણો"),
        ("Structure of solids: concept of crystalline structure, structure of metal, unit cell, "
         "BCC, FCC and HCP",
         "ઘન પદાર્થની રચના: crystalline structure નો ખ્યાલ, ધાતુની રચના, unit cell, BCC, FCC અને HCP"),
        ("Physical, mechanical, chemical, electrical, electromagnetic and thermal properties of "
         "materials",
         "સામગ્રીના physical, mechanical, chemical, electrical, electromagnetic અને thermal ગુણધર્મો"),
    ], ("Compare appropriate material for manufacturing various components.",
        "જુદા જુદા components બનાવવા માટે યોગ્ય સામગ્રીની સરખામણી કરવી.")),
    (2, "Phase Diagrams", "ફેઝ ડાયાગ્રામ", 7, 20, 14, "CO2", [
        ("Solidification of metals: crystal, grain and grain boundaries, effect of cooling rate on "
         "material properties, solid solution",
         "ધાતુનું ઘનીકરણ: crystal, grain અને grain boundaries, cooling rate ની material properties પર "
         "અસર, solid solution"),
        ("Iron-carbon equilibrium diagram: concept, need, characteristics and the terms used",
         "Iron-carbon equilibrium diagram: ખ્યાલ, જરૂર, લક્ષણો અને વપરાતા શબ્દો"),
        ("Concept of heat treatment processes",
         "Heat treatment પ્રક્રિયાઓનો ખ્યાલ"),
    ], ("Explain appropriate heat treatment process for various components.",
        "જુદા જુદા components માટે યોગ્ય heat treatment પ્રક્રિયા સમજાવવી.")),
    (3, "Metals and Its Alloys", "ધાતુઓ અને તેમના એલોય", 8, 17, 12, "CO3", [
        ("Ferrous metals: classification of steel and cast iron, properties and applications",
         "Ferrous ધાતુઓ: steel અને cast iron નું વર્ગીકરણ, ગુણધર્મો અને ઉપયોગ"),
        ("Non-ferrous metals: copper, brass, bronze, gun metal, aluminium, wrought and cast alloys of "
         "aluminium - properties and applications",
         "Non-ferrous ધાતુઓ: copper, brass, bronze, gun metal, aluminium, aluminium ના wrought અને "
         "cast alloys - ગુણધર્મો અને ઉપયોગ"),
        ("Comparison between metals and non-metals",
         "ધાતુ અને અધાતુ વચ્ચેની સરખામણી"),
    ], ("Understand classification, properties and applications of various metallic materials.",
        "વિવિધ ધાતુઈ સામગ્રીનું વર્ગીકરણ, ગુણધર્મો અને ઉપયોગ સમજવા.")),
    (4, "Non Metallic Materials", "અધાતુઈ સામગ્રી", 8, 17, 12, "CO4", [
        ("Introduction and classification of non-metallic materials",
         "અધાતુઈ સામગ્રીનો પરિચય અને વર્ગીકરણ"),
        ("Properties and applications of rubber and elastomers",
         "રબર અને elastomers ના ગુણધર્મો તથા ઉપયોગ"),
        ("Properties and applications of ceramics and refractories",
         "ceramics અને refractories ના ગુણધર્મો તથા ઉપયોગ"),
        ("Insulators, abrasives and adhesives: properties and applications",
         "Insulators, abrasives અને adhesives: ગુણધર્મો અને ઉપયોગ"),
    ], ("Understand classification, properties and applications of various non-metallic materials.",
        "વિવિધ અધાતુઈ સામગ્રીનું વર્ગીકરણ, ગુણધર્મો અને ઉપયોગ સમજવા.")),
    (5, "Electrolytes, Oils, Paints/Varnish and Corrosion",
     "ઇલેક્ટ્રોલાઇટ, તેલ, પેન્ટ/વાર્નિશ અને કાટ", 10, 17, 12, "CO5", [
        ("Surface engineering: coatings and surface treatments, cleaning and mechanical finishing, "
         "organic coatings, electroplating and special metallic plating, electropolishing and "
         "photo-etching, conversion coatings (oxide, phosphate, chromate), thin film coatings "
         "(PVD and CVD)",
         "Surface engineering: coatings અને surface treatments, cleaning અને mechanical finishing, "
         "organic coatings, electroplating અને special metallic plating, electropolishing અને "
         "photo-etching, conversion coatings (oxide, phosphate, chromate), thin film coatings "
         "(PVD અને CVD)"),
        ("Oils: types, properties, BIS designation methods and applications in mechanical engineering",
         "તેલ: પ્રકાર, ગુણધર્મ, BIS પ્રમાણે designation અને mechanical engineering માં ઉપયોગ"),
        ("Paints and varnishes: definition, classification, surface preparation and coating methods",
         "પેન્ટ અને વાર્નિશ: વ્યાખ્યા, વર્ગીકરણ, surface preparation અને coating પદ્ધતિઓ"),
        ("Corrosion: types and reasons", "કાટ: પ્રકાર અને કારણો"),
    ], ("Explain electrolysis, paints/varnish and corrosion to improve surface properties.",
        "Surface properties સુધારવા electrolysis, paints/varnish અને corrosion સમજાવવું.")),
    (6, "Green Material", "હરિત સામગ્રી", 6, 15, 10, "CO6", [
        ("Concept of green material", "Green material નો ખ્યાલ"),
        ("Sustainable and renewable material in mechanical and allied industries",
         "Mechanical અને સંલગ્ન ઉદ્યોગોમાં sustainable અને renewable સામગ્રી"),
        ("Need of advanced material in mechanical and automotive sector: electric vehicle, solar "
         "panels, battery",
         "Mechanical અને automotive ક્ષેત્રે advanced material ની જરૂર: electric vehicle, solar "
         "panels, battery"),
    ], ("Identify green material as an alternative of existing materials.",
        "હાલની સામગ્રીના વિકલ્પ તરીકે green material ઓળખવી.")),
]

BRANCH = "mechanical"
SEMESTER = 1

SUBJECT = {
    "code": CODE,
    "name": {"en": TITLE, "gu": TITLE_GU},
    "branch": BRANCH,
    "semester": SEMESTER,
    "syllabus_year": "2024-25",
    "category": "Basic Science Course (BSC-02)",
    "type": "theory",
    "languages": ["en", "gu"],
    "code_lang": None,
    "teaching": {"lecture": 3, "tutorial": 0, "practical": 2},
    "exam": {"theory_ese": 70, "theory_pa": 30, "practical_pa": 20, "practical_ese": 30,
             "total": 150, "credits": 4},
    "prerequisites": tr(
        "School level chemistry and physics - atoms, molecules, the periodic table and the idea of a "
        "chemical bond - together with basic mathematics, because the subject computes densities, "
        "packing fractions, stresses and coating thicknesses from simple formulae.",
        "શાળાનું chemistry અને physics - atoms, molecules, periodic table અને chemical bond નો ખ્યાલ - "
        "તથા પાયાનું ગણિત, કારણ કે આ subject સાદા સૂત્રોમાંથી density, packing fraction, stress અને "
        "coating ની જાડાઈ ગણે છે."),
    "rationale": tr(
        "Every machine part is a material decision before it is a drawing. This subject takes the "
        "diploma engineer from the atom - the bond and the crystal - to the workshop: why steel is "
        "hardened, why brass is chosen for a bearing, why rubber seals an insulator, why a shaft rusts "
        "and how a coating is put on, and finally which material is the green choice for the next "
        "product.",
        "દરેક machine part દોરડું (drawing) બનતા પહેલા સામગ્રીનો નિર્ણય હોય છે. આ subject diploma "
        "engineer ને atom થી - bond અને crystal - workshop સુધી લઈ જાય છે: steel કેમ harden થાય, "
        "bearing માટે brass કેમ પસંદ થાય, ઇન્સ્યુલેટર કેમ રબરથી સીલ થાય, shaft માં કાટ કેમ લાગે અને "
        "coating કેવી રીતે ચઢાવાય, અને અંતે આગલા product માટે કઈ સામગ્રી green પસંદગી છે."),
    "units": [
        {"no": no, "title": {"en": t_en, "gu": t_gu}, "hours": hours, "weightage": weightage,
         "theory_marks": marks, "official": True, "course_outcome": co,
         "topics": [tr(a, b) for a, b in topics],
         "outcomes": [tr(out_en, out_gu)]}
        for (no, t_en, t_gu, hours, weightage, marks, co, topics, (out_en, out_gu)) in UNITS
    ],
    "course_outcomes": [
        tr("CO1: Compare an appropriate material for manufacturing various components. (U, A)",
           "CO1: જુદા જુદા components બનાવવા માટે યોગ્ય સામગ્રીની સરખામણી કરવી. (U, A)"),
        tr("CO2: Explain an appropriate heat treatment process for various components. (U, A)",
           "CO2: જુદા જુદા components માટે યોગ્ય heat treatment પ્રક્રિયા સમજાવવી. (U, A)"),
        tr("CO3: Understand classification, properties and applications of various metallic "
           "materials. (R, U)", "CO3: વિવિધ ધાતુઈ સામગ્રીનું વર્ગીકરણ, ગુણધર્મો અને ઉપયોગ સમજવા. "
           "(R, U)"),
        tr("CO4: Understand classification, properties and applications of various non-metallic "
           "materials. (R, U)", "CO4: વિવિધ અધાતુઈ સામગ્રીનું વર્ગીકરણ, ગુણધર્મો અને ઉપયોગ "
           "સમજવા. (R, U)"),
        tr("CO5: Explain electrolysis, paints/varnish and corrosion to improve surface properties. "
           "(R, U)", "CO5: Surface properties સુધારવા electrolysis, paints/varnish અને corrosion "
           "સમજાવવું. (R, U)"),
        tr("CO6: Identify green material as an alternative of existing materials. (U, A)",
           "CO6: હાલની સામગ્રીના વિકલ્પ તરીકે green material ઓળખવી. (U, A)"),
    ],
    "course_outcome_rbt": {"CO1": "Apply", "CO2": "Apply", "CO3": "Understand", "CO4": "Understand",
                           "CO5": "Understand", "CO6": "Apply"},
    "theory_marks_by_unit": {"1": 10, "2": 14, "3": 12, "4": 12, "5": 12, "6": 10},
    "theory_marks_note": tr(
        "The PDF prints both the percentage weightage (14 / 20 / 17 / 17 / 17 / 15) and the marks "
        "split by Bloom level, so the 70 theory marks are taken straight from its specification "
        "table: 10 / 14 / 12 / 12 / 12 / 10 = 70. The practical half (PA 20 + ESE 30) is assessed on "
        "the seven listed laboratory exercises.",
        "PDF માં ટકાવારી weightage (14 / 20 / 17 / 17 / 17 / 15) અને Bloom level પ્રમાણે marks ની "
        "વહેંચણી બંને છપાયેલાં છે, તેથી 70 theory marks તેની specification table માંથી જ લીધેલા છે: "
        "10 / 14 / 12 / 12 / 12 / 10 = 70. Practical ભાગ (PA 20 + ESE 30) સાત પ્રયોગો પર લેવાય છે."),
    "theory_rbt_percent": {"remember": 20, "understand": 28, "apply": 23, "analyze": 11,
                           "evaluate": 9, "create": 9},
    "theory_rbt_marks": {"remember": 14, "understand": 20, "apply": 16, "analyze": 8,
                         "evaluate": 6, "create": 6},
    "total_hours": 45,
    "hours_note": tr(
        "The unit hours printed in the PDF (6 + 7 + 8 + 8 + 10 + 6) add to exactly 45, and the "
        "printed total is 45, so nothing had to be adjusted.",
        "PDF માં છપાયેલા unit hours (6 + 7 + 8 + 8 + 10 + 6) નો સરવાળો બરાબર 45 થાય છે અને છપાયેલો "
        "total પણ 45 છે, તેથી કંઈ સુધારવું પડ્યું નથી."),
    "source_pdf_sha256": hashlib.sha256(SYLLABUS.read_bytes()).hexdigest(),
    "source_note": tr(
        "Syllabus text transcribed from the uploaded GTU DI01000181 PDF (Engineering Materials "
        "Science, Mechanical Engineering and allied branches, semester 1, w.e.f. 2024-25). Units, "
        "hours, weightages, marks scheme, course outcomes, reference books, practical list and "
        "activities are copied from it.",
        "Syllabus નું લખાણ અપલોડ કરેલી GTU DI01000181 PDF (Engineering Materials Science, Mechanical "
        "Engineering અને સંલગ્ન શાખાઓ, semester 1, w.e.f. 2024-25) માંથી ઉતારેલું છે. Units, hours, "
        "weightages, marks scheme, course outcomes, reference books, practical list અને activities "
        "તેમાંથી જ લીધેલા છે."),
    "official_practicals": [
        tr("Identify any five materials from a selected set (three metallic and two non-metallic) "
           "using the standard identification criteria, list the properties of each and identify the "
           "main alloying elements with the reason for adding them.",
           "પસંદ કરેલા સેટમાંથી પાંચ સામગ્રી (ત્રણ ધાતુઈ અને બે અધાતુઈ) ઓળખો, દરેકના ગુણધર્મો લખો અને "
           "મુખ્ય alloying elements તથા તે ઉમેરવાનું કારણ ઓળખો."),
        tr("Prepare a report on metallurgical examination - its need and the importance of "
           "microstructure - write the steps of specimen preparation and examine the given specimen "
           "under a metallurgical microscope.",
           "Metallurgical examination પર રિપોર્ટ બનાવો - તેની જરૂર અને microstructure નું મહત્વ - "
           "specimen તૈયાર કરવાના પગલાં લખો અને આપેલો specimen metallurgical microscope હેઠળ જુઓ."),
        tr("Perform the hardening process on a ferrous material and measure the hardness before and "
           "after hardening.",
           "Ferrous સામગ્રી પર hardening પ્રક્રિયા કરો અને hardening પહેલાં તથા પછી hardness માપો."),
        tr("Prepare three non-ferrous micro specimens (copper, brass and aluminium), examine them "
           "and prepare a report.",
           "ત્રણ non-ferrous micro specimens (copper, brass અને aluminium) તૈયાર કરો, તેમને જુઓ અને "
           "રિપોર્ટ બનાવો."),
        tr("Study the various heat treatment furnaces, the processes annealing, normalising, "
           "hardening, case hardening, tempering and nitriding with their methods, parameters and "
           "property changes, and the types of quenching media with their properties and "
           "applications.",
           "વિવિધ heat treatment furnaces, annealing, normalising, hardening, case hardening, "
           "tempering અને nitriding પ્રક્રિયાઓ તેમની પદ્ધતિ, parameters અને ગુણધર્મોમાં થતા ફેરફાર "
           "સાથે, અને quenching mediums ના પ્રકાર તેમના ગુણધર્મો તથા ઉપયોગ સાથે ભણો."),
        tr("Prepare a report on at least four non-metallic materials with their classification, "
           "properties and applications.",
           "ઓછામાં ઓછી ચાર અધાતુઈ સામગ્રી પર તેમના વર્ગીકરણ, ગુણધર્મો અને ઉપયોગ સાથે રિપોર્ટ બનાવો."),
        tr("Prepare a report on green materials such as the electric vehicle, solar panels and "
           "batteries.",
           "Electric vehicle, solar panels અને battery જેવી green materials પર રિપોર્ટ બનાવો."),
    ],
    "practicals": [],
    "suggested_projects": [
        tr("Material selection: choose the material for a specific engineering application (a pump "
           "shaft, a bicycle frame or a pressure vessel) and justify the choice against two "
           "alternatives on strength, cost and corrosion.",
           "Material selection: કોઈ ચોક્કસ ઉપયોગ (pump shaft, bicycle frame કે pressure vessel) માટે "
           "સામગ્રી પસંદ કરો અને strength, cost તથા corrosion પર બે વિકલ્પો સામે તેની સમર્થના કરો."),
        tr("Phase diagram analysis: interpret the iron-carbon diagram for three carbon contents and "
           "predict the phases present at room temperature.",
           "Phase diagram analysis: ત્રણ carbon contents માટે iron-carbon diagram સમજાવો અને room "
           "temperature પર હાજર phases અનુમાન કરો."),
        tr("Microstructural analysis: examine the microstructures of mild steel, hardened steel and "
           "cast iron and report the phases seen.",
           "Microstructural analysis: mild steel, hardened steel અને cast iron ના microstructures "
           "જુઓ અને દેખાતા phases નો રિપોર્ટ બનાવો."),
        tr("Heat treatment effects: harden, temper and anneal the same steel and plot hardness "
           "against treatment.",
           "Heat treatment effects: એક જ steel ને harden, temper અને anneal કરો અને treatment સામે "
           "hardness નો ગ્રાફ દોરો."),
        tr("Green material study: survey the materials used in one electric vehicle or solar panel "
           "and report which are recyclable.",
           "Green material study: એક electric vehicle કે solar panel માં વપરાતી સામગ્રીનો સર્વે કરો "
           "અને કઈ recyclable છે તે જણાવો."),
    ],
    "activities": [
        tr("Assignments", "Assignments"),
        tr("Technical quiz / MCQ test", "Technical quiz / MCQ test"),
        tr("Presentation on some course topic", "કોઈ course topic પર presentation"),
        tr("Internet based assignments", "Internet આધારિત assignments"),
        tr("Micro-project in a team or individually", "ટીમમાં અથવા એકલા micro-project"),
    ],
    "books": [
        "G. B. S. Narang - Materials Science, Khanna Publishers, New Delhi, 2021, ISBN 8195028721",
        "R. K. Rajpoot - Materials Science, S. K. Katariya and Sons, New Delhi, 2013, "
        "ISBN 8185749108",
        "R. S. Khurmi and R. S. Sedha - Materials Science, S. Chand, 2004, ISBN 8121901464",
        "U. C. Jindal - Materials Science and Metallurgy, Pearson Education India, 2011, "
        "ISBN 9788131759110",
        "V. Raghavan - Materials Science and Engineering, Prentice Hall India, 2015, "
        "ISBN 9788120350922",
        "R. B. Gupta - Material Science and Engineering, Tech India Publication, New Delhi, 2018, "
        "ISBN 9351921077",
        "O. P. Khanna - Material Science, Dhanpat Rai Publications, New Delhi, 2010, "
        "ISBN 8189928317",
        "Sidney Avner - Physical Metallurgy, Tata McGraw-Hill Education, Noida, 2017, "
        "ISBN 0074630067",
    ],
    "learning_resources": [
        "Metallurgical microscope with a polishing machine and standard specimens - https://nptel.ac.in/",
        "Heat treatment furnaces with oil, water and air quenching media - https://vlab.co.in/",
        "Rockwell hardness tester (scales A, B and C) and a scleroscope - https://vlab.co.in/",
        "Hand grinder for specimen preparation and spark testing",
        "Material science reference wiki - http://en.wikipedia.org/wiki/Materials_science",
        "Iron-carbon phase diagram reference - "
        "http://www.substech.com/dokuwiki/doku.php?id=iron_carbon_phase_diagram",
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
            # Short labels may legitimately stay as the English technical term ("BCC", "HCP",
            # "Brinell"); anything longer must be written in Gujarati.
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
