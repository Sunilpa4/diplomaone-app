"""GTU Environmental Sustainability (DI02000051) - Semester 2, common to every branch, w.e.f. 2024-25.

The PDF prints "Branch: ALL", so the subject lives in content/common/sem2/DI02000051 and the
exporter inserts it into semester 2 of every diploma branch in the app.

This subject is bilingual: every text node carries "en" and "gu" (the same user decision as
Applied Physics and the other bilingual subjects). Diagram labels stay in English.

Syllabus source: tools/syllabus_DI02000051.txt (transcribed from the uploaded PDF, sha256 kept in
subject.json). The five units, their hours, weightages, the marks split, the course outcomes, the
reference books, the project list and the activity list are copied from it exactly.
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SUBJ_DIR = ROOT / "content/common/sem2/DI02000051"
DIAG_DIR = SUBJ_DIR / "diagrams"
TABS = ["notes", "diagrams", "equations", "numericals", "viva", "exam"]

CODE = "DI02000051"
TITLE_EN = "Environmental Sustainability"
TITLE_GU = "પર્યાવરણીય ટકાઉપણું"


def tr(en, gu):
    return {"en": en, "gu": gu}


# (no, title_en, title_gu, hours, weightage, theory_marks, co, topics[(en, gu)], outcome_en, outcome_gu)
UNITS = [
    (1, "Introduction to Environmental Sustainability, Ecosystem and Biodiversity",
     "પર્યાવરણીય ટકાઉપણાનો પરિચય, પારિતંત્ર અને જૈવવિવિધતા", 4, 10, 7, "CO1", [
        ("Definition and scope of sustainability",
         "ટકાઉપણાની વ્યાખ્યા અને વ્યાપ્તિ"),
        ("Structure of an ecosystem and its components",
         "પારિતંત્રની રચના અને તેના ઘટકો"),
        ("Function of an ecosystem: energy flow and nutrient cycling",
         "પારિતંત્રનું કાર્ય: ઊર્જા પ્રવાહ અને પોષક તત્વોનું ચક્ર"),
        ("Carbon and nitrogen cycles",
         "કાર્બન અને નાઇટ્રોજન ચક્ર"),
        ("Sulphur and phosphorus cycles",
         "સલ્ફર અને ફોસ્ફરસ ચક્ર"),
        ("Importance of biodiversity",
         "જૈવવિવિધતાનું મહત્વ"),
        ("Threats to biodiversity: habitat loss, pollution, climate change and invasive species",
         "જૈવવિવિધતા પરના ભય: નિવાસસ્થાનનો નાશ, પ્રદૂષણ, જળવાયુ પરિવર્તન અને આક્રમક જાતિઓ"),
        ("Conservation strategies: in-situ, ex-situ and community conservation",
         "સંરક્ષણ વ્યૂહરચનાઓ: સ્થાનિક, સ્થાનાંતરિત અને સમુદાય આધારિત સંરક્ષણ"),
    ],
     "Explain the basic principles of environmental sustainability, the working of ecosystems and "
     "the value and conservation of biodiversity.",
     "પર્યાવરણીય ટકાઉપણાના પાયાના સિદ્ધાંતો, પારિતંત્રનું કાર્ય તથા જૈવવિવિધતાનું મૂલ્ય અને "
     "સંરક્ષણ સમજાવવું."),
    (2, "Waste Management and Pollution Control", "કચરાનું સંચાલન અને પ્રદૂષણ નિયંત્રણ", 7, 25, 17, "CO2", [
        ("Air pollution: classification, sources and its effects",
         "વાયુ પ્રદૂષણ: વર્ગીકરણ, સ્રોત અને તેની અસરો"),
        ("Air pollution control equipment: settling chamber, cyclone separator, bag filter, "
         "electrostatic precipitator, scrubber",
         "વાયુ પ્રદૂષણ નિયંત્રણ સાધનો: સેટલિંગ ચેમ્બર, સાયક્લોન સેપરેટર, બેગ ફિલ્ટર, "
         "ઇલેક્ટ્રોસ્ટેટિક પ્રિસિપિટેટર, સ્ક્રબર"),
        ("Water pollution: sources and the meaning of the parameters",
         "જળ પ્રદૂષણ: સ્રોત અને પરિમાણોનો અર્થ"),
        ("BOD and COD: definition, measurement and meaning",
         "BOD અને COD: વ્યાખ્યા, માપન અને અર્થ"),
        ("pH, total suspended solids, turbidity and total solids",
         "pH, કુલ નિલંબિત ઘન, ક્ષોભ અને કુલ ઘન"),
        ("Waste water treatment: primary, secondary and tertiary",
         "ગંદા પાણીની સફાઈ: પ્રાથમિક, દ્વિતીય અને તૃતીય"),
        ("Solid waste: generation, sources and characteristics",
         "ઘન કચરો: ઉત્પાદન, સ્રોત અને લક્ષણો"),
        ("Collection and disposal of municipal solid waste",
         "નગરપાલિકા ઘન કચરાનો સંગ્રહ અને નિકાલ"),
        ("Hazardous waste: types, handling and disposal",
         "જોખમી કચરો: પ્રકાર, હેન્ડલિંગ અને નિકાલ"),
        ("Noise pollution: measurement, effects and control",
         "ઘોંઘાટ પ્રદૂષણ: માપન, અસરો અને નિયંત્રણ"),
        ("Plastic waste and e-waste: hazards and management",
         "પ્લાસ્ટિક કચરો અને ઈ-કચરો: જોખમ અને સંચાલન"),
    ],
     "Develop strategies for waste management and pollution control in an engineering setting.",
     "ઇજનેરી કાર્યક્ષેત્રમાં કચરાના સંચાલન અને પ્રદૂષણ નિયંત્રણ માટે વ્યૂહરચના વિકસાવવી."),
    (3, "Renewable Energy Technologies", "નવીકરણીય ઊર્જા ટેકનોલોજી", 7, 25, 18, "CO3", [
        ("Importance of renewable energy in reducing the carbon footprint",
         "કાર્બન ફૂટપ્રિન્ટ ઘટાડવામાં નવીકરણીય ઊર્જાનું મહત્વ"),
        ("Comparison of renewable and non-renewable energy sources",
         "નવીકરણીય અને બિનનવીકરણીય ઊર્જા સ્રોતોની તુલના"),
        ("Principles of photovoltaic technology",
         "ફોટોવોલ્ટેઇક ટેકનોલોજીના સિદ્ધાંતો"),
        ("Types of solar cells and their efficiency",
         "સૌર કોષોના પ્રકાર અને તેમની કાર્યક્ષમતા"),
        ("Wind energy: HAWT and VAWT with their parts and operation",
         "પવન ઊર્જા: HAWT અને VAWT તેમના ભાગો અને કાર્ય સાથે"),
        ("Bladeless wind turbines",
         "બ્લેડ વગરના પવન ટર્બાઇન"),
        ("Biofuels: ethanol, biodiesel and biogas",
         "જૈવ ઇંધણ: ઇಥેનોલ, બાયોડીઝલ અને બાયોગેસ"),
        ("Biomass in solid, liquid and gaseous form; algae biofuels; gasification",
         "ઘન, પ્રવાહી અને વાયુરૂપ બાયોમાસ; શેવાળ બાયોફ્યુઅલ; ગેસિફિકેશન"),
        ("Geothermal, ocean and tidal energy",
         "ભૂતાપીય, મહાસાગર અને ભરતી ઊર્જા"),
        ("Hydrogen energy and the hydrogen economy",
         "હાઇડ્રોજન ઊર્જા અને હાઇડ્રોજન અર્થતંત્ર"),
    ],
     "Evaluate renewable energy technologies for a given site or application.",
     "આપેલ સ્થળ કે ઉપયોગ માટે નવીકરણીય ઊર્જા ટેકનોલોજીનું મૂલ્યાંકન કરવું."),
    (4, "Climate Change: Science and Solutions", "જળવાયુ પરિવર્તન: વિજ્ઞાન અને ઉકેલ", 6, 20, 14, "CO4", [
        ("Earth's climate system: atmosphere, hydrosphere, cryosphere, land and biosphere",
         "પૃથ્વીની જળવાયુ પ્રણાલી: વાતાવરણ, જળાવરણ, હિમાવરણ, ભૂમિ અને જૈવાવરણ"),
        ("The greenhouse effect and the greenhouse gases with their sources",
         "હરિતગૃહ અસર અને હરિતગૃહ વાયુઓ તેમના સ્રોત સાથે"),
        ("Evidence of climate change: temperature records and melting ice",
         "જળવાયુ પરિવર્તનના પુરાવા: તાપમાનની નોંધ અને પીગળતો બરફ"),
        ("Rising sea level, shifting rainfall and extreme weather",
         "વધતું દરિયાનું સ્તર, બદલાતો વરસાદ અને આત્યંતિક હવામાન"),
        ("Impacts: biodiversity loss, ocean acidification and desertification",
         "અસરો: જૈવવિવિધતાનો નાશ, મહાસાગરનું આમ્લીકરણ અને રણીકરણ"),
        ("Social and economic impacts",
         "સામાજિક અને આર્થિક અસરો"),
        ("Mitigation: energy efficiency, renewables and carbon capture and storage",
         "શમન: ઊર્જા કાર્યક્ષમતા, નવીકરણીય ઊર્જા અને કાર્બન કેપ્ચર તથા સંગ્રહ"),
        ("Sustainable land use and forestry as a sink",
         "ટકાઉ ભૂમિ ઉપયોગ અને વનીકરણ"),
    ],
     "Analyse the impact of climate change and choose suitable mitigation measures.",
     "જળવાયુ પરિવર્તનની અસરનું વિશ્લેષણ કરી યોગ્ય શમન પગલાં પસંદ કરવાં."),
    (5, "Environmental Policy and Governance", "પર્યાવરણ નીતિ અને શાસન", 6, 20, 14, "CO5", [
        ("Environmental policies in India: Air Act, Water Act and Environment Protection Act",
         "ભારતની પર્યાવરણ નીતિઓ: વાયુ અધિનિયમ, જળ અધિનિયમ અને પર્યાવરણ સંરક્ષણ અધિનિયમ"),
        ("Wild Life Protection Act, Forest Conservation Act and Biological Diversity Act",
         "વન્યજીવ સંરક્ષણ અધિનિયમ, વન સંરક્ષણ અધિનિયમ અને જૈવિક વિવિધતા અધિનિયમ"),
        ("Environmental management system ISO 14000: definition and benefits",
         "પર્યાવરણીય વ્યવસ્થાપન પ્રણાલી ISO 14000: વ્યાખ્યા અને ફાયદા"),
        ("Rain water harvesting",
         "વરસાદી પાણીનો સંગ્રહ"),
        ("Green building and the rating systems used in India",
         "હરિત ઇમારત અને ભારતમાં વપરાતી રેટિંગ પ્રણાલી"),
        ("Cradle to cradle concept and life cycle analysis",
         "ક્રેડલ ટુ ક્રેડલ સંકલ્પના અને જીવન ચક્ર વિશ્લેષણ"),
        ("Green label and the carbon credit system with its advantages and disadvantages",
         "હરિત લેબલ અને કાર્બન ક્રેડિટ પ્રણાલી તેના ફાયદા તથા ગેરફાયદા સાથે"),
        ("The 5R concept: refuse, reduce, reuse, repurpose, recycle",
         "5R સંકલ્પના: નકારો, ઘટાડો, ફરી વાપરો, નવો ઉપયોગ કરો, રિસાઇકલ કરો"),
        ("Eco tourism: advantages and disadvantages",
         "પર્યાવરણ પર્યટન: ફાયદા અને ગેરફાયદા"),
    ],
     "Adopt cleaner technologies in your field in compliance with the environmental policies and "
     "standards of India.",
     "ભારતની પર્યાવરણ નીતિઓ અને ધોરણોનું પાલન કરી તમારા ક્ષેત્રમાં સ્વચ્છ ટેકનોલોજી "
     "અપનાવવી."),
]

SUBJECT = {
    "code": CODE,
    "name": tr(TITLE_EN, TITLE_GU),
    "branch": "common",
    "common_to_all_branches": True,
    "semester": 2,
    "syllabus_year": "2024-25",
    "category": "Engineering Science (ESC)",
    "type": "theory",
    "languages": ["en", "gu"],
    "code_lang": None,
    "teaching": {"lecture": 2, "tutorial": 0, "practical": 0},
    "exam": {"theory_ese": 70, "theory_pa": 30, "practical_pa": 0, "practical_ese": 0,
             "total": 100, "credits": 2},
    "prerequisites": tr("Basic science, Environmental Science and Earth science at school level",
                        "શાળા સ્તરે પાયાનું વિજ્ઞાન, પર્યાવરણ વિજ્ઞાન અને પૃથ્વી વિજ્ઞાન"),
    "units": [
        {"no": no, "title": tr(t_en, t_gu), "hours": hours, "weightage": weightage,
         "theory_marks": marks, "official": True, "course_outcome": co,
         "topics": [tr(t, g) for t, g in topics], "outcomes": [tr(o_en, o_gu)]}
        for (no, t_en, t_gu, hours, weightage, marks, co, topics, o_en, o_gu) in UNITS
    ],
    "course_outcomes": [
        tr("CO1: Understand the basic principles of environmental sustainability, ecosystem and "
           "biodiversity.",
           "CO1: પર્યાવરણીય ટકાઉપણાના પાયાના સિદ્ધાંતો, પારિતંત્ર અને જૈવવિવિધતા સમજવા."),
        tr("CO2: Develop strategies for waste management and pollution control.",
           "CO2: કચરાના સંચાલન અને પ્રદૂષણ નિયંત્રણ માટે વ્યૂહરચના વિકસાવવી."),
        tr("CO3: Evaluate renewable energy technologies.",
           "CO3: નવીકરણીય ઊર્જા ટેકનોલોજીનું મૂલ્યાંકન કરવું."),
        tr("CO4: Analyze the impact of climate change.",
           "CO4: જળવાયુ પરિવર્તનની અસરનું વિશ્લેષણ કરવું."),
        tr("CO5: Adopt cleaner technologies in the relevant field in compliance with various "
           "environmental policies.",
           "CO5: વિવિધ પર્યાવરણ નીતિઓનું પાલન કરી સંબંધિત ક્ષેત્રમાં સ્વચ્છ ટેકનોલોજી અપનાવવી."),
    ],
    "course_outcome_rbt": {"CO1": "R/U", "CO2": "R/U/A", "CO3": "R/U/A", "CO4": "R/U/A",
                           "CO5": "R/U/A"},
    "theory_marks_by_unit": {"1": 7, "2": 17, "3": 18, "4": 14, "5": 14},
    "theory_marks_note": tr(
        "The PDF prints only the weightage column, so the 70 theory marks are split by weightage: "
        "7 / 17.5 / 17.5 / 14 / 14, rounded to whole marks 7 / 17 / 18 / 14 / 14 (70 in total).",
        "PDFમાં ફક્ત વેઇટેજ કોલમ આપેલી છે, તેથી 70 થિયરી માર્ક્સ વેઇટેજ પ્રમાણે વહેંચ્યા છે: "
        "7 / 17.5 / 17.5 / 14 / 14, જે પૂર્ણ માર્ક્સમાં 7 / 17 / 18 / 14 / 14 (કુલ 70) થાય છે."),
    "theory_rbt_percent": {"remember": 30, "understand": 50, "apply": 20,
                           "analyze": 0, "evaluate": 0, "create": 0},
    "theory_rbt_marks": {"remember": 21, "understand": 35, "apply": 14,
                         "analyze": 0, "evaluate": 0, "create": 0},
    "total_hours": 30,
    "source_pdf_sha256": "4d965bae1e7a2bc0e64bfebf2cd74fc5de59204228abcc767a9bd0ffc583c821",
    "source_note": tr(
        "Syllabus text transcribed from the uploaded GTU DI02000051 PDF (Environmental "
        "Sustainability, Branch: ALL, semester 2). Unit hours, weightages, the marks split, the "
        "course outcomes, the reference books, the project list and the activity list are copied "
        "from it; the course has no practical list and no laboratory requirement (NIL).",
        "અપલોડ કરેલ GTU DI02000051 PDF (પર્યાવરણીય ટકાઉપણું, શાખા: બધી, સેમેસ્ટર 2)માંથી સિલેબસનું "
        "ટ્રાન્સક્રિપ્શન. યુનિટના કલાક, વેઇટેજ, માર્ક્સ વિભાજન, કોર્સ આઉટકમ, સંદર્ભ પુસ્તકો, "
        "પ્રોજેક્ટ યાદી અને પ્રવૃત્તિ યાદી તેમાંથી લીધેલી છે; આ કોર્સમાં પ્રેક્ટિકલ યાદી કે "
        "લેબોરેટરી જરૂરિયાત નથી (NIL)."),
    "official_practicals": [],
    "practicals": [],
    "suggested_projects": [
        tr("Micro-project on wind energy: measure the wind speed at your campus for a week and "
           "estimate the energy a small turbine could give.",
           "પવન ઊર્જા પર સૂક્ષ્મ પ્રોજેક્ટ: એક અઠવાડિયું કેમ્પસમાં પવનની ઝડપ માપી નાના ટર્બાઇનથી "
           "મળતી ઊર્જાનો અંદાજ કાઢવો."),
        tr("Micro-project on solar energy: measure the output of a small PV panel at different "
           "tilt angles through the day.",
           "સૌર ઊર્જા પર સૂક્ષ્મ પ્રોજેક્ટ: દિવસ દરમિયાન જુદા ઝૂકાવવાના ખૂણે નાના PV પેનલનું આઉટપુટ "
           "માપવું."),
        tr("Micro-project on natural cycles: draw and explain the carbon and nitrogen cycles with "
           "local examples.",
           "કુદરતી ચક્ર પર સૂક્ષ્મ પ્રોજેક્ટ: સ્થાનિક ઉદાહરણ સાથે કાર્બન અને નાઇટ્રોજન ચક્ર દોરી "
           "સમજાવવા."),
        tr("Micro-project \"best out of waste\": build a usable article from campus waste and "
           "record the material saved.",
           "સૂક્ષ્મ પ્રોજેક્ટ \"કચરામાંથી શ્રેષ્ઠ\": કેમ્પસના કચરામાંથી ઉપયોગી વસ્તુ બનાવી બચેલી "
           "સામગ્રીની નોંધ રાખવી."),
        tr("Field visit: report on an energy park or the garbage disposal system of your city.",
           "ક્ષેત્ર મુલાકાત: ઊર્જા પાર્ક કે તમારા શહેરની કચરા નિકાલ પ્રણાલી પર અહેવાલ."),
    ],
    "books": [
        "Solanki, Chetan Singh - Renewable Energy Technologies: A Practical Guide for Beginners, "
        "PHI Learning, New Delhi, 2010. Print ISBN 9788120334342, eBook ISBN 9789354437151",
        "Izrael, Y. A. - Ecology and Control of the Natural Environment, Kluwer Academic "
        "Publisher, eBook ISBN 978-94-011-3390-6, softcover ISBN 978-94-010-5499-7",
        "Singh, Ritu and Kumar, Sanjeev - Green Technologies and Environmental Sustainability, "
        "Springer International Publishing, 2017, eBook ISBN 978-3-319-50654-8",
        "Chhatwal, G. R.; Satake, M.; Mehra, M. C.; Katyal, Mohan; Katyal, T.; Nagahiro, T. - "
        "Environmental Noise Pollution and Its Control, Anmol Publications, New Delhi, "
        "ISBN 8170411378",
        "Earnest, Joshua and Wizelius, Tore - Wind Power Plants and Project Development, PHI "
        "Learning, New Delhi, 2011, ISBN-10 8120351274, ISBN-13 978-8120351271",
        "Kothari, D. P.; Singal, K. C.; Ranjan, Rakesh - Renewable Energy Sources and Emerging "
        "Technologies, PHI Learning, New Delhi, 2009, ISBN-13 978-8120344709",
        "Basak, Anandita - Environmental Studies, Pearson Publications, "
        "ISBN 8131785688, 9788131785683",
        "Debi, Aloka - Environmental Science and Engineering, University Press, "
        "ISBN 9788173718113, ISBN-10 8173716080, ISBN-13 978-8173716089",
        "Valadia, K. S. - Coping With Natural Hazards: Indian Context, Orient Longman, "
        "ISBN-10 8125027351, ISBN-13 978-8125027355",
        "Rubin, Edward S. - Introduction to Engineering and Environment, McGraw Hill "
        "Publications, ISBN-10 0071181857, ISBN-13 978-0071181853",
        "Wilson, Elizabeth and Gerard, David - Carbon Capture and Sequestration: Integrating "
        "Technology, Monitoring, Regulation, Wiley-Blackwell (15 March 2007), CBS Publishers, "
        "ISBN-13 978-0813802077",
    ],
    "learning_resources": [
        "NPTEL - https://www.nptel.iitm.ac.in",
        "Khan Academy - https://www.khanacademy.org",
        "Gujarat Pollution Control Board - https://gpcb.gujarat.gov.in",
        "Central Pollution Control Board - https://cpcb.nic.in",
        "Wind energy animation (US DOE) - "
        "http://www1.eere.energy.gov/wind/wind_animation.html",
        "NREL solar learning - http://www.nrel.gov/learning/re_solar.html",
        "NREL biomass learning - http://www.nrel.gov/learning/re_biomass.html",
        "MNRE biomass power - "
        "http://www.mnre.gov.in/schemes/grid-connected/biomass-powercogen/",
        "EPA climate students - http://www.epa.gov/climatestudents/",
        "Climate Central - http://www.climatecentral.org",
        "ENVIS - http://www.envis.nic.in/",
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


def spec_for(number):
    for spec in SUBJECT["units"]:
        if spec["no"] == number:
            return spec
    raise AssertionError(f"unit {number} is not registered for {CODE}")


_STATS = {"total": 0, "gujarati": 0}


def _check_bilingual(obj, where="unit"):
    """Every text node must carry both languages.

    Symbols, formulas and numbers read the same in both languages, so an identical pair is allowed
    up to 40 characters. Anything longer must be written in Gujarati, and at least 85 % of all nodes
    in a unit must carry Gujarati script - that catches a card that was simply left in English.
    """
    if isinstance(obj, dict):
        if "en" in obj or "gu" in obj:
            assert "en" in obj and "gu" in obj, f"{where}: a text node has only one language: {obj}"
            assert obj["en"].strip() and obj["gu"].strip(), f"{where}: empty text node"
            _STATS["total"] += 1
            if re.search(r"[\u0a80-\u0aff]", obj["gu"]):
                _STATS["gujarati"] += 1
            else:
                assert obj["en"] == obj["gu"] and len(obj["gu"]) <= 40, \
                    f"{where}: Gujarati node has no Gujarati script: {obj['gu'][:70]!r}"
        for v in obj.values():
            _check_bilingual(v, where)
    elif isinstance(obj, list):
        for v in obj:
            _check_bilingual(v, where)


def unit_stats_total():
    return _STATS["total"]


def write_unit(unit):
    SUBJ_DIR.mkdir(parents=True, exist_ok=True)
    DIAG_DIR.mkdir(exist_ok=True)
    spec = spec_for(unit["unit"])
    assert unit["title"] == spec["title"], "unit title must match subject.json"
    assert (unit["hours"], unit["weightage"]) == (spec["hours"], spec["weightage"]), \
        "unit hours/weightage must match the syllabus"
    _STATS.update(total=0, gujarati=0)
    _check_bilingual(unit, f"unit {unit['unit']}")
    share = _STATS["gujarati"] / max(unit_stats_total(), 1)
    assert share >= 0.85, (f"unit {unit['unit']}: only {share:.0%} of text nodes carry Gujarati; "
                           "the unit is not fully bilingual")
    out = SUBJ_DIR / f"unit{unit['unit']}.json"
    out.write_text(json.dumps(unit, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    write_subject()
    return out


if __name__ == "__main__":
    write_subject()
    print("subject written:", SUBJ_DIR / "subject.json")
