"""GTU Applied Physics (DI01000121) - Semester 1 or 2 by branch, w.e.f. 2024-25.

The PDF prints one subject with two home semesters: semester 1 for Civil, Environmental, Mining,
Textile Manufacturing, Ceramic, Printing and Renewable Energy; semester 2 for Automobile, Chemical,
Mechanical, Mechatronics, Textile Processing, Fabrication, Textile Design and Mechanical (CAD/CAM).
The app carries ten of those fifteen branches, so the subject lists all ten at the semester the PDF
gives, and subject.json says so with "branches" + "semesters" as well as the legacy single fields.

This subject is bilingual: every text node carries "en" and "gu" (user decision, like the older
bilingual subjects in the app). Diagrams stay in English, as in every other bilingual subject here.

Syllabus source: tools/syllabus_DI01000121.txt (transcribed from the uploaded PDF, sha256 kept in
subject.json).
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SUBJ_DIR = ROOT / "content/common/sem1/DI01000121"
DIAG_DIR = SUBJ_DIR / "diagrams"
TABS = ["notes", "diagrams", "equations", "numericals", "viva", "exam"]

CODE = "DI01000121"
TITLE_EN = "Applied Physics"
TITLE_GU = "એપ્લાઇડ ફિઝિક્સ"

# Branches the app carries, at the semester the PDF gives them in.
SEM1_BRANCHES = ["civil", "environmental", "mining", "textile_mfg", "printing"]
SEM2_BRANCHES = ["automobile", "chemical", "mechanical", "mechatronics", "textile_proc"]
ALL_BRANCHES = SEM1_BRANCHES + SEM2_BRANCHES
# Printed in the PDF but not carried by this app yet:
MISSING_BRANCHES = ["ceramic", "renewable_energy", "fabrication", "textile_design", "mech_cad_cam"]


def tr(en, gu):
    return {"en": en, "gu": gu}


# (no, title_en, title_gu, hours, weightage, theory_marks, co, topics[(en, gu)], outcomes[(en, gu)])
UNITS = [
    (1, "Units and Measurements", "એકમો અને માપન", 7, 17, 12, "CO1", [
        ("Measurement and units in engineering and science", "ઇજનેરી અને વિજ્ઞાનમાં માપન તથા એકમો"),
        ("Physical quantities: fundamental and derived quantities",
         "ભૌતિક રાશિઓ: પાયાની અને વ્યુત્પન્ન રાશિઓ"),
        ("Systems of units: CGS, MKS and SI; interconversion of units",
         "એકમ પદ્ધતિઓ: CGS, MKS અને SI; એકમોનું રૂપાંતરણ"),
        ("Vernier calipers and micrometer screw gauge with their errors",
         "વર્નિયર કેલિપર્સ અને માઇક્રોમીટર સ્ક્રુ ગેજ તથા તેમની ભૂલો"),
        ("Accuracy, precision, error, absolute, relative and percentage error",
         "ચોકસાઈ, પરિશુદ્ધતા, ભૂલ, નિરપેક્ષ, સાપેક્ષ અને ટકાવારી ભૂલ"),
        ("Rounding off and significant digits", "રાઉન્ડિંગ ઓફ તથા સાર્થક અંકો"),
    ], [
        ("1.a Explain physical quantities and their units.", "1.a ભૌતિક રાશિઓ અને તેમના એકમો સમજાવવા."),
        ("1.b Convert a unit of a physical quantity from one system to another.",
         "1.b ભૌતિક રાશિના એકમનું એક પદ્ધતિથી બીજી પદ્ધતિમાં રૂપાંતરણ કરવું."),
        ("1.c Measure the dimensions of an object with the relevant instrument.",
         "1.c યોગ્ય સાધનથી પદાર્થનાં પરિમાણ માપવા."),
        ("1.d Estimate errors in a measurement.", "1.d માપનમાં થતી ભૂલોનો અંદાજ કાઢવો."),
        ("1.e Apply least count, errors and significant figures to problems.",
         "1.e લીસ્ટ કાઉન્ટ, ભૂલો અને સાર્થક અંકોના ઉપયોગથી દાખલા ગણવા."),
    ]),
    (2, "Circular Motion", "વર્તુળ ગતિ", 8, 14, 10, "CO2", [
        ("Force, momentum and law of conservation of linear momentum",
         "બળ, વેગમાન અને રેખીય વેગમાનના સંરક્ષણનો નિયમ"),
        ("Recoil of a gun and impulse", "બંદૂકનો રીકોઇલ અને આઘાત (ઇમ્પલ્સ)"),
        ("Circular motion, angular displacement, angular velocity, angular acceleration",
         "વર્તુળ ગતિ, કોણીય સ્થાનાંતરણ, કોણીય વેગ, કોણીય પ્રવર્ગ"),
        ("Centripetal and centrifugal force", "કેન્દ્રગામી અને કેન્દ્રત્યાગી બળ"),
        ("Banking of roads and bending of a cyclist", "રસ્તાનું બેન્કિંગ અને સાયકલ સવારનું નમવું"),
    ], [
        ("2.a Apply conservation of linear momentum to the recoil of a gun.",
         "2.a રેખીય વેગમાન સંરક્ષણનો ઉપયોગ બંદૂકના રીકોઇલમાં કરવો."),
        ("2.b Apply centripetal and centrifugal force to engineering problems.",
         "2.b કેન્દ્રગામી અને કેન્દ્રત્યાગી બળ ઇજનેરી દાખલામાં લાગુ કરવા."),
    ]),
    (3, "General Properties of Matter", "દ્રવ્યના સામાન્ય ગુણધર્મો", 12, 28, 19, "CO3", [
        ("Elasticity, deforming and restoring force", "સ્થિતિસ્થાપકતા, વિકૃતિકારક અને પુનઃસ્થાપક બળ"),
        ("Stress and strain, Hooke's law", "પ્રતિબળ અને વિકૃતિ, હૂકનો નિયમ"),
        ("Moduli of elasticity: Young's, bulk and shear modulus",
         "સ્થિતિસ્થાપકતાના ગુણાંક: યંગ, બલ્ક અને શિયર ગુણાંક"),
        ("Stress-strain curve", "પ્રતિબળ-વિકૃતિ વક્ર"),
        ("Surface tension, cohesion and adhesion", "પૃષ્ઠતાણ, સંસક્તિ અને આસક્તિ"),
        ("Molecular range, sphere of influence, Laplace's molecular theory",
         "આણ્વીય પરાસ, પ્રભાવ ગોળો, લાપ્લાસનો આણ્વીય સિદ્ધાંત"),
        ("Angle of contact and Ascent formula", "સંપર્ક કોણ અને આરોહણ સૂત્ર"),
        ("Relation between surface tension and surface energy", "પૃષ્ઠતાણ અને પૃષ્ઠઊર્જા વચ્ચેનો સંબંધ"),
        ("Viscosity, Newton's law of viscosity, velocity gradient",
         "શ્યાનતા, ન્યૂટનનો શ્યાનતાનો નિયમ, વેગ પ્રવણતા"),
        ("Streamline and turbulent flow, critical velocity, Reynolds number",
         "સ્તરીય અને વમળીય પ્રવાહ, ક્રાંતિક વેગ, રેનોલ્ડ્સ આંક"),
        ("Stokes' law and terminal velocity", "સ્ટોક્સનો નિયમ અને અંતિમ વેગ"),
    ], [
        ("3.a Explain Hooke's law, the stress-strain curve and the moduli of elasticity.",
         "3.a હૂકનો નિયમ, પ્રતિબળ-વિકૃતિ વક્ર અને સ્થિતિસ્થાપકતાના ગુણાંક સમજાવવા."),
        ("3.b Explain surface tension, cohesive and adhesive forces.",
         "3.b પૃષ્ઠતાણ, સંસક્તિ અને આસક્તિ બળો સમજાવવા."),
        ("3.c Apply the Ascent formula to find the surface tension of a liquid.",
         "3.c આરોહણ સૂત્રથી પ્રવાહીનું પૃષ્ઠતાણ શોધવું."),
        ("3.d Explain viscosity, coefficient of viscosity, terminal velocity and Stokes' law.",
         "3.d શ્યાનતા, શ્યાનતા ગુણાંક, અંતિમ વેગ અને સ્ટોક્સનો નિયમ સમજાવવો."),
        ("3.e Explain types of fluid motion and the Reynolds number.",
         "3.e પ્રવાહની ગતિના પ્રકારો અને રેનોલ્ડ્સ આંક સમજાવવો."),
    ]),
    (4, "Heat and Thermometry", "ઉષ્મા અને થર્મોમેટ્રી", 8, 17, 12, "CO4", [
        ("Heat and temperature", "ઉષ્મા અને તાપમાન"),
        ("Modes of heat transfer: conduction, convection, radiation",
         "ઉષ્મા સંક્રમણની રીતો: વહન, સંવહન, વિકિરણ"),
        ("Temperature scales: Kelvin, Celsius, Fahrenheit and conversion",
         "તાપમાન માપક્રમ: કેલ્વિન, સેલ્સિયસ, ફેરનહીટ અને રૂપાંતરણ"),
        ("Heat capacity and specific heat", "ઉષ્મા ધારિતા અને વિશિષ્ટ ઉષ્મા"),
        ("Mercury and bimetallic thermometers", "પારા અને દ્વિધાતુ થર્મોમીટર"),
        ("Coefficient of thermal conductivity", "ઉષ્મીય વાહકતાનો ગુણાંક"),
        ("Expansion of solids and coefficient of linear expansion",
         "ઘન પદાર્થનું પ્રસરણ અને રેખીય પ્રસરણનો ગુણાંક"),
    ], [
        ("4.a Distinguish between heat and temperature.", "4.a ઉષ્મા અને તાપમાન વચ્ચેનો ભેદ સમજાવવો."),
        ("4.b Explain the modes of heat transmission.", "4.b ઉષ્મા સંક્રમણની રીતો સમજાવવી."),
        ("4.c Convert between temperature scales.", "4.c તાપમાન માપક્રમો વચ્ચે રૂપાંતરણ કરવું."),
        ("4.d Explain heat capacity and specific heat.", "4.d ઉષ્મા ધારિતા અને વિશિષ્ટ ઉષ્મા સમજાવવી."),
        ("4.e Explain thermometers and their uses.", "4.e થર્મોમીટર અને તેના ઉપયોગ સમજાવવા."),
        ("4.f Apply the coefficient of thermal conductivity to engineering problems.",
         "4.f ઉષ્મીય વાહકતાનો ગુણાંક ઇજનેરી દાખલામાં લાગુ કરવો."),
        ("4.g Explain expansion in solids and the coefficient of linear expansion.",
         "4.g ઘનનું પ્રસરણ અને રેખીય પ્રસરણ ગુણાંક સમજાવવો."),
    ]),
    (5, "Waves, Ultrasonic and Semiconductor", "તરંગો, અલ્ટ્રાસોનિક અને અર્ધવાહક", 10, 24, 17, "CO5", [
        ("Waves, wave motion, longitudinal and transverse waves",
         "તરંગો, તરંગ ગતિ, સંગત અને અનુપ્રસ્થ તરંગો"),
        ("Frequency, periodic time, amplitude, wavelength and wave velocity",
         "આવૃત્તિ, આવર્તકાળ, કંપવિસ્તાર, તરંગલંબાઈ અને તરંગ વેગ"),
        ("Superposition and interference, stationary interference conditions",
         "અધ્યારોપણ અને વ્યતિકરણ, સ્થિર વ્યતિકરણની શરતો"),
        ("Reverberation, reverberation time, echo, noise, absorption coefficient",
         "પ્રતિધ્વનિ, પ્રતિધ્વનિ સમય, પડઘો, ઘોંઘાટ, શોષણ ગુણાંક"),
        ("Sabine's formula and control of reverberation", "સેબાઇનનું સૂત્ર અને પ્રતિધ્વનિ નિયંત્રણ"),
        ("Ultrasonic waves, properties and applications", "અલ્ટ્રાસોનિક તરંગો, ગુણધર્મો અને ઉપયોગો"),
        ("Conductors, semiconductors and insulators: energy band gap",
         "વાહક, અર્ધવાહક અને અવાહક: ઊર્જા પટ્ટી અંતર"),
        ("Intrinsic and extrinsic semiconductors, P and N type, doping",
         "આંતરિક અને બાહ્ય અર્ધવાહક, P અને N પ્રકાર, ડોપિંગ"),
    ], [
        ("5.a Explain wave and wave motion with an example.", "5.a તરંગ અને તરંગ ગતિ ઉદાહરણ સાથે સમજાવવી."),
        ("5.b Distinguish between longitudinal and transverse waves.",
         "5.b સંગત અને અનુપ્રસ્થ તરંગો વચ્ચેનો ભેદ સમજાવવો."),
        ("5.c Explain frequency, periodic time, amplitude, wavelength and wave velocity.",
         "5.c આવૃત્તિ, આવર્તકાળ, કંપવિસ્તાર, તરંગલંબાઈ અને તરંગ વેગ સમજાવવા."),
        ("5.d Explain superposition and interference.", "5.d અધ્યારોપણ અને વ્યતિકરણ સમજાવવા."),
        ("5.e Explain reverberation, echo, noise and the absorption coefficient.",
         "5.e પ્રતિધ્વનિ, પડઘો, ઘોંઘાટ અને શોષણ ગુણાંક સમજાવવા."),
        ("5.f Apply Sabine's formula for reverberation time.",
         "5.f પ્રતિધ્વનિ સમય માટે સેબાઇનનું સૂત્ર લાગુ કરવું."),
        ("5.g Explain ultrasonic waves and their properties.", "5.g અલ્ટ્રાસોનિક તરંગો અને ગુણધર્મો સમજાવવા."),
        ("5.h List engineering and medical applications of ultrasonics.",
         "5.h અલ્ટ્રાસોનિકના ઇજનેરી અને તબીબી ઉપયોગો જણાવવા."),
        ("5.i Classify conductors, semiconductors and insulators by energy band gap.",
         "5.i ઊર્જા પટ્ટી અંતર દ્વારા વાહક, અર્ધવાહક અને અવાહકનું વર્ગીકરણ કરવું."),
        ("5.j Apply impurity doping to semiconductors.", "5.j અર્ધવાહકમાં અશુદ્ધિ ડોપિંગ લાગુ કરવું."),
    ]),
]

SUBJECT = {
    "code": CODE,
    "name": tr(TITLE_EN, TITLE_GU),
    "branch": "civil",
    "branches": ALL_BRANCHES,
    "semester": 1,
    "semesters": [1, 2],
    "semester_by_branch": {b: 1 for b in SEM1_BRANCHES} | {b: 2 for b in SEM2_BRANCHES},
    "syllabus_year": "2024-25",
    "category": "Basic Science (BSC)",
    "type": "theory",
    "languages": ["en", "gu"],
    "code_lang": None,
    "teaching": {"lecture": 3, "tutorial": 0, "practical": 2},
    "exam": {"theory_ese": 70, "theory_pa": 30, "practical_pa": 20, "practical_ese": 30,
             "total": 150, "credits": 4},
    "prerequisites": tr("10+ (Physics at school level)", "10+ (શાળા સ્તરે ભૌતિક વિજ્ઞાન)"),
    "units": [
        {"no": n, "title": tr(t_en, t_gu), "hours": h, "weightage": w, "theory_marks": marks,
         "official": True, "course_outcome": co,
         "topics": [tr(a, b) for a, b in topics],
         "outcomes": [tr(a, b) for a, b in outcomes], "file": None}
        for n, t_en, t_gu, h, w, marks, co, topics, outcomes in UNITS
    ],
    "course_outcomes": [
        tr("CO1: Use relevant instruments with precision to measure the dimension of given physical "
           "quantities in various engineering situations.",
           "CO1: વિવિધ ઇજનેરી પરિસ્થિતિમાં આપેલ ભૌતિક રાશિઓનાં પરિમાણ ચોકસાઈપૂર્વક માપવા માટે યોગ્ય "
           "સાધનોનો ઉપયોગ કરવો."),
        tr("CO2: Solve various engineering problems by the concept of linear momentum and circular "
           "motion.",
           "CO2: રેખીય વેગમાન અને વર્તુળ ગતિના ખ્યાલથી વિવિધ ઇજનેરી દાખલા ઉકેલવા."),
        tr("CO3: Apply basic concepts of properties of matter in solving engineering problems "
           "efficiently.",
           "CO3: દ્રવ્યના ગુણધર્મોના પાયાના ખ્યાલોનો ઉપયોગ ઇજનેરી દાખલા કાર્યક્ષમ રીતે ઉકેલવામાં કરવો."),
        tr("CO4: Apply the basic concepts of heat transfer and thermometric properties to provide "
           "solutions for various engineering problems.",
           "CO4: ઉષ્મા સંક્રમણ અને થર્મોમેટ્રિક ગુણધર્મોના પાયાના ખ્યાલોથી ઇજનેરી સમસ્યાઓનો ઉકેલ આપવો."),
        tr("CO5: Use the concept of waves, ultrasonic and semiconductor for engineering "
           "applications.",
           "CO5: તરંગો, અલ્ટ્રાસોનિક અને અર્ધવાહકના ખ્યાલનો ઉપયોગ ઇજનેરી ઉપયોગોમાં કરવો."),
    ],
    "course_outcome_rbt": {"CO1": "R/U/A", "CO2": "R/U/A", "CO3": "R/U/A", "CO4": "R/U/A",
                           "CO5": "R/U/A"},
    "theory_marks_by_unit": {"1": 12, "2": 10, "3": 19, "4": 12, "5": 17},
    "theory_marks_note": tr("The PDF prints only the weightage column, so the 70 theory marks are "
                            "split by weightage: 12 / 10 / 19 / 12 / 17.",
                            "PDFમાં ફક્ત વેઇટેજ કોલમ આપેલી છે, તેથી 70 થિયરી માર્ક્સ વેઇટેજ પ્રમાણે "
                            "વહેંચ્યા છે: 12 / 10 / 19 / 12 / 17."),
    "theory_rbt_percent": {"remember": 26, "understand": 37, "apply": 37,
                           "analyze": 0, "evaluate": 0, "create": 0},
    "theory_rbt_marks": {"remember": 18, "understand": 26, "apply": 26,
                         "analyze": 0, "evaluate": 0, "create": 0},
    "total_hours": 45,
    "source_pdf_sha256": "5ff9f534aef4043b01343f9c89811f7f4daa60f3efeb5422cc6d2b14c188602b",
    "source_note": tr("Syllabus text transcribed from the uploaded GTU DI01000121 PDF (Applied "
                      "Physics). Unit hours, weightages, the marks split, the practical list and the "
                      "course outcomes are copied from it.",
                      "અપલોડ કરેલ GTU DI01000121 PDF (એપ્લાઇડ ફિઝિક્સ)માંથી સિલેબસનું ટ્રાન્સક્રિપ્શન. "
                      "યુનિટના કલાક, વેઇટેજ, માર્ક્સ વિભાજન, પ્રેક્ટિકલ યાદી અને કોર્સ આઉટકમ તેમાંથી લીધેલા છે."),
    "official_practicals": [
        {"no": 1, "unit": 1, "hours": 2,
         "outcome": tr("Use vernier caliper to measure the dimensions of a given object.",
                       "આપેલ પદાર્થનાં પરિમાણ માપવા વર્નિયર કેલિપરનો ઉપયોગ કરવો.")},
        {"no": 2, "unit": 1, "hours": 2,
         "outcome": tr("Use micrometer screw gauge to measure the diameter of a given wire and "
                       "determine the volume of a given metallic piece.",
                       "આપેલ તારનો વ્યાસ માપવા અને ધાતુના ટુકડાનું ઘનફળ શોધવા માઇક્રોમીટર સ્ક્રુ ગેજનો "
                       "ઉપયોગ કરવો.")},
        {"no": 3, "unit": 3, "hours": 2,
         "outcome": tr("Use Hooke's law to determine the force constant of a given spring.",
                       "આપેલ સ્પ્રિંગનો બળ અચળાંક શોધવા હૂકનો નિયમ લાગુ કરવો.")},
        {"no": 4, "unit": 3, "hours": 2,
         "outcome": tr("Use Searle's method to determine Young's modulus of the given metallic wire.",
                       "આપેલ ધાતુના તારનો યંગ ગુણાંક શોધવા સર્લની રીત વાપરવી.")},
        {"no": 5, "unit": 3, "hours": 2,
         "outcome": tr("Use the capillary rise method and a travelling microscope to determine the "
                       "surface tension of a given liquid.",
                       "કેશનળી ચઢાણ રીત અને ટ્રાવેલિંગ માઇક્રોસ્કોપથી આપેલ પ્રવાહીનું પૃષ્ઠતાણ શોધવું.")},
        {"no": 6, "unit": 3, "hours": 2,
         "outcome": tr("Use Stokes' law to determine the viscosity of a given liquid (e.g. glycerine).",
                       "આપેલ પ્રવાહી (દા.ત. ગ્લિસરિન)ની શ્યાનતા શોધવા સ્ટોક્સનો નિયમ વાપરવો.")},
        {"no": 7, "unit": 4, "hours": 2,
         "outcome": tr("Use different thermometers to measure the temperature of a hot bath and "
                       "convert it into different scales.",
                       "ગરમ પાણીના સ્નાનનું તાપમાન જુદા જુદા થર્મોમીટરથી માપી જુદા માપક્રમમાં રૂપાંતરિત કરવું.")},
        {"no": 8, "unit": 4, "hours": 2,
         "outcome": tr("Use Searle's method to measure the coefficient of thermal conductivity of a "
                       "given metallic rod.",
                       "આપેલ ધાતુના સળિયાનો ઉષ્મીય વાહકતા ગુણાંક માપવા સર્લની રીત વાપરવી.")},
        {"no": 9, "unit": 4, "hours": 2,
         "outcome": tr("Use Searle's method to determine the coefficient of linear expansion of a "
                       "given metallic rod.",
                       "આપેલ ધાતુના સળિયાનો રેખીય પ્રસરણ ગુણાંક શોધવા સર્લની રીત વાપરવી.")},
        {"no": 10, "unit": 5, "hours": 2,
         "outcome": tr("Determine the acceleration due to gravity with a simple pendulum.",
                       "સાદા લોલકથી ગુરુત્વાકર્ષણનો પ્રવર્ગ શોધવો.")},
        {"no": 11, "unit": 5, "hours": 2,
         "outcome": tr("Use a sonometer to find the frequency of a given tuning fork.",
                       "આપેલ ટ્યુનિંગ ફોર્કની આવૃત્તિ શોધવા સોનોમીટર વાપરવું.")},
        {"no": 12, "unit": 5, "hours": 2,
         "outcome": tr("Use a resonance tube to determine the velocity of sound in air at room "
                       "temperature.",
                       "ઓરડાના તાપમાને હવામાં ધ્વનિનો વેગ શોધવા રેઝોનન્સ ટ્યુબ વાપરવી.")},
        {"no": 13, "unit": 5, "hours": 3,
         "outcome": tr("Use an ultrasonic interferometer to determine the velocity of ultrasonic "
                       "waves in different liquids.",
                       "જુદા જુદા પ્રવાહીમાં અલ્ટ્રાસોનિક તરંગોનો વેગ શોધવા અલ્ટ્રાસોનિક ઇન્ટરફેરોમીટર વાપરવું.")},
        {"no": 14, "unit": 5, "hours": 3,
         "outcome": tr("Use an electrical vibrator to find the frequency of the AC mains.",
                       "AC મેઇન્સની આવૃત્તિ શોધવા ઇલેક્ટ્રિકલ વાઇબ્રેટર વાપરવો.")},
    ],
    "practicals": [],
    "books": [
        "NCERT - Text Book of Physics for Class XI (Part I & II), NCERT Delhi, 2019, "
        "ISBN 81-7450-508-3 / 81-7450-566-0",
        "NCERT - Text Book of Physics for Class XII (Part I & II), NCERT Delhi, 2019, "
        "ISBN 81-7450-631-4 / 81-7450-671-3",
        "TTTI Publications - Applied Physics, Vol. I and II (Tata McGraw Hill, Delhi, 2019)",
        "H. C. Verma - Concepts in Physics Vol. I and II (Bharti Bhawan, 2019), "
        "ISBN 978-8177091878 / 978-8177092325",
        "D. K. Bhattacharya and Poonam Tandon - Engineering Physics (Oxford University Press), "
        "ISBN 9781680158687",
        "C. L. Arora - B.Sc. Practical Physics (S. Chand), ISBN 9788121909099",
        "M. N. Avadhanulu, P. G. Kshirsagar, T. V. S. Arun Murthy - A Textbook of Engineering "
        "Physics (S. Chand, 11th edition, 2018), ISBN 978-9352833993",
        "Hugh D. Young and Roger A. Freedman - Sears and Zemansky's University Physics "
        "(Pearson, 14th edition), ISBN 978-0-321-97361-0",
        "John W. Jewett and Raymond A. Serway - Physics for Scientists and Engineers with Modern "
        "Physics (Cengage, 10th edition), ISBN 1337553298",
        "William Moebs, Samuel J. Ling and Jeff Sanny - University Physics Vol. I-III (OpenStax, "
        "2016), ISBN 1-947172-20-4",
        "Douglas C. Giancoli - Physics for Scientists and Engineers (Pearson, 7th edition, 2015), "
        "ISBN 978-1292057125",
        "Jearl Walker, David Halliday, Robert Resnick - Principles of Physics (Wiley, 10th edition, "
        "2015), ISBN 978-8126552566",
        "L. J. F. Hermans and Wiebke Drenckhan - Physics in Daily Life with Illustrations (EDP "
        "Sciences, 2012), ISBN 978-2-7598-0705-5",
        "Richard Feynman - The Feynman Lectures on Physics Vol. I-III (Pearson, 2012), "
        "ISBN 978-9332580954",
        "Paul G. Hewitt - Conceptual Physics (Pearson, 12th edition), ISBN 978-9352861774",
    ],
    "learning_resources": [
        "MIT OpenCourseWare Physics - https://ocw.mit.edu/courses/physics/",
        "NPTEL - https://www.nptel.iitm.ac.in",
        "PhET simulations - https://phet.colorado.edu/",
        "Virtual Labs - https://www.vlab.co.in/",
        "Amrita Virtual Labs - https://vlab.amrita.edu/",
        "OLabs - https://www.olabs.edu.in/",
        "Khan Academy - https://www.khanacademy.org/",
        "ComPADRE OSP - https://www.compadre.org/osp/",
        "Physics Aviary - https://www.thephysicsaviary.com/",
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

    Symbols, unit codes, numbers and numeric answers (L, m, SI, 10⁵, "1 N = 10⁵ dyne") read the same
    in both languages, so an identical pair is allowed up to 40 characters. Anything longer must be
    written in Gujarati, and at least 85 % of all nodes in a unit must carry Gujarati script - that
    catches a card that was simply left in English.
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
