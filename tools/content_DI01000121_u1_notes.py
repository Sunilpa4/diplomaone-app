"""DI01000121 Applied Physics - Unit 1: Units and Measurements (bilingual en + gu).

GTU 1.1-1.5, 7 h, 17 %, 12 marks, CO1. Every text node carries English and Gujarati, as the user
asked for this subject ("same as before" = the older bilingual subjects in the app).

Builders: every fragment is a {"en": html, "gu": html} dict, so a card body is summed from fragments
and both languages stay in step.
"""
from subject_DI01000121 import tr as _tr  # noqa: F401  (kept for the shared module surface)


def T(en, gu=None):
    """A bilingual node. Symbols and units (L, m, SI, 10⁵) read the same in both languages."""
    return {"en": en, "gu": en if gu is None else gu}


def _join(parts):
    return {"en": "".join(p["en"] for p in parts), "gu": "".join(p["gu"] for p in parts)}


def P(en, gu):
    return T(f"<p>{en}</p>", f"<p>{gu}</p>")


def H4(en, gu):
    return T(f"<h4>{en}</h4>", f"<h4>{gu}</h4>")


def UL(*items):
    return T("<ul>" + "".join(f"<li>{i[0]}</li>" for i in items) + "</ul>",
             "<ul>" + "".join(f"<li>{i[1]}</li>" for i in items) + "</ul>")


def OL(*items):
    return T("<ol>" + "".join(f"<li>{i[0]}</li>" for i in items) + "</ol>",
             "<ol>" + "".join(f"<li>{i[1]}</li>" for i in items) + "</ol>")


def TB(head, rows):
    """head: [(en, gu), ...]; rows: [[(en, gu), ...], ...]"""
    def build(k):
        out = "<table><tr>" + "".join(f"<th>{h[k]}</th>" for h in head) + "</tr>"
        for r in rows:
            out += "<tr>" + "".join(f"<td>{c[k]}</td>" for c in r) + "</tr>"
        return out + "</table>"
    return T(build("en"), build("gu"))


def card(h, parts, diagram=None, syllabus_item=None, examples=None):
    item = {"h": h, "body": _join(parts)}
    if diagram:
        item["diagram"] = diagram
    if syllabus_item:
        item["syllabus_item"] = syllabus_item
    if examples:
        item["examples"] = list(examples)
    return item


def num(id_, h, statement, solution_parts, answer, unit_no=1):
    """A solved numerical: given, step-by-step work and a boxed answer, in both languages."""
    def build(k, given_head, steps_head, answer_head):
        return (f"<h4>{given_head}</h4><p>{statement[k]}</p>"
                f"<h4>{steps_head}</h4>{''.join(p[k] for p in solution_parts)}"
                f"<h4>{answer_head}</h4><p><b>{answer[k]}</b></p>")
    return {"id": id_, "unit": unit_no, "h": h, "q": statement,
            "a": T(build("en", "Given and assumptions", "Step-by-step solution", "Answer"),
                   build("gu", "આપેલી માહિતી", "પગલાવાર ઉકેલ", "જવાબ")),
            "answer": answer}


SOURCES = [
    T("GTU DI01000121 Applied Physics syllabus (uploaded PDF, w.e.f. 2024-25)",
      "GTU DI01000121 એપ્લાઇડ ફિઝિક્સ સિલેબસ (અપલોડ કરેલ PDF, 2024-25થી અમલમાં)"),
    T("NCERT Physics Class XI, Part I - Units and Measurements (chapter 1)",
      "NCERT ભૌતિક વિજ્ઞાન ધોરણ 11, ભાગ 1 - એકમો અને માપન (પ્રકરણ 1)"),
    T("H. C. Verma - Concepts of Physics, Vol. I, chapter 1 and 2",
      "એચ. સી. વર્મા - કોન્સેપ્ટ્સ ઓફ ફિઝિક્સ, ભાગ 1, પ્રકરણ 1 અને 2"),
    T("C. L. Arora - B.Sc. Practical Physics: vernier calipers and screw gauge",
      "સી. એલ. અરોરા - પ્રેક્ટિકલ ફિઝિક્સ: વર્નિયર કેલિપર્સ અને સ્ક્રુ ગેજ"),
    T("NIST - SI base units and prefixes (https://www.nist.gov/pml/owm/metric-si/si-units)",
      "NIST - SI પાયાના એકમો અને ઉપસર્ગ (https://www.nist.gov/pml/owm/metric-si/si-units)"),
]

NOTES = [
    {"title": T("1. Measurement, Units and Physical Quantities",
                "1. માપન, એકમો અને ભૌતિક રાશિઓ"),
     "items": [
         card(T("1.1 Why measurement comes before engineering",
                "1.1 ઇજનેરી પહેલાં માપન કેમ જરૂરી છે"),
              [H4("Definition", "વ્યાખ્યા"),
               P("<b>Measurement</b> is the comparison of an unknown quantity with a fixed, accepted "
                 "standard of the same kind. The result is written as a number with a unit.",
                 "<b>માપન</b> એટલે અજાણી રાશિની સરખામણી તે જ પ્રકારના નિશ્ચિત અને સ્વીકૃત માનક સાથે કરવી. "
                 "પરિણામ સંખ્યા અને એકમ સાથે લખાય છે."),
               P("A number without a unit is not a measurement: \"25\" means nothing until it is "
                 "25 mm or 25 mm².",
                 "એકમ વગરની સંખ્યા માપન નથી: \"25\" ત્યાં સુધી અર્થહીન છે જ્યાં સુધી તે 25 mm કે 25 mm² "
                 "ન લખાય."),
               H4("Where a diploma engineer measures", "ડિપ્લોમા ઇજનેર ક્યાં માપે છે"),
               TB([T("Situation", "પરિસ્થિતિ"), T("What is measured", "શું માપાય"), T("Typical instrument", "સામાન્ય સાધન")],
                  [[T("Shaft diameter on a lathe", "લેથ પર શાફ્ટનો વ્યાસ"), T("outside diameter, 0.01 mm", "બહારનો વ્યાસ, 0.01 mm"), T("micrometer screw gauge", "માઇક્રોમીટર સ્ક્રુ ગેજ")],
                   [T("Plate thickness before welding", "વેલ્ડિંગ પહેલાં પ્લેટની જાડાઈ"), T("thickness, 0.1 mm", "જાડાઈ, 0.1 mm"), T("vernier caliper", "વર્નિયર કેલિપર")],
                   [T("Wire used in a winding", "વાઇન્ડિંગમાં વપરાતો તાર"), T("wire diameter, 0.01 mm", "તારનો વ્યાસ, 0.01 mm"), T("screw gauge", "સ્ક્રુ ગેજ")],
                   [T("Tank level in a process plant", "પ્રોસેસ પ્લાન્ટમાં ટાંકીનું સ્તર"), T("level in metres", "સ્તર મીટરમાં"), T("scale or level gauge", "સ્કેલ કે લેવલ ગેજ")]]),
               H4("Worked example", "ઉકેલાયેલ દાખલો"),
               P("A drawing asks for a bore of 25.00 mm with a tolerance of ±0.02 mm. The allowed range "
                 "is 24.98 mm to 25.02 mm, so the instrument chosen must at least read 0.01 mm.",
                 "ડ્રોઇંગમાં 25.00 mm બોર અને ±0.02 mm ટોલરન્સ માંગ્યું છે. માન્ય મર્યાદા 24.98 mm થી "
                 "25.02 mm છે, તેથી પસંદ કરેલ સાધન ઓછામાં ઓછું 0.01 mm વાંચી શકે તેવું હોવું જોઈએ."),
               H4("Common mistake", "સામાન્ય ભૂલ"),
               P("Writing \"25\" on a job card. The next shift reads 25 cm instead of 25 mm and the part "
                 "is scrap.",
                 "જોબ કાર્ડ પર ફક્ત \"25\" લખવું. આગલી શિફ્ટ તેને 25 mm ને બદલે 25 cm વાંચે છે અને પાર્ટ "
                 "કચરો બને છે.")],
              syllabus_item="1.1"),
         card(T("1.2 Fundamental and derived quantities",
                "1.2 પાયાની અને વ્યુત્પન્ન રાશિઓ"),
              [H4("Rule", "નિયમ"),
               P("<b>Fundamental quantities</b> are independent: they are not defined from any other "
                 "quantity. <b>Derived quantities</b> are built from the fundamental ones.",
                 "<b>પાયાની રાશિઓ</b> સ્વતંત્ર છે: તે બીજી કોઈ રાશિથી બનતી નથી. <b>વ્યુત્પન્ન રાશિઓ</b> "
                 "પાયાની રાશિઓમાંથી બને છે."),
               H4("The seven SI base quantities", "SIની સાત પાયાની રાશિઓ"),
               TB([T("Quantity", "રાશિ"), T("Symbol", "સંજ્ઞા"), T("SI unit", "SI એકમ"), T("Unit symbol", "એકમ સંજ્ઞા")],
                  [[T("length", "લંબાઈ"), T("L"), T("metre", "મીટર"), T("m")],
                   [T("mass", "દ્રવ્યમાન"), T("M"), T("kilogram", "કિલોગ્રામ"), T("kg")],
                   [T("time", "સમય"), T("T"), T("second", "સેકન્ડ"), T("s")],
                   [T("electric current", "વિદ્યુત પ્રવાહ"), T("I"), T("ampere", "એમ્પિયર"), T("A")],
                   [T("temperature", "તાપમાન"), T("K"), T("kelvin", "કેલ્વિન"), T("K")],
                   [T("amount of substance", "પદાર્થનો જથ્થો"), T("N"), T("mole", "મોલ"), T("mol")],
                   [T("luminous intensity", "પ્રકાશીય તીવ્રતા"), T("J"), T("candela", "કેન્ડેલા"), T("cd")]]),
               H4("Examples of derived quantities", "વ્યુત્પન્ન રાશિઓનાં ઉદાહરણ"),
               TB([T("Quantity", "રાશિ"), T("Formula", "સૂત્ર"), T("SI unit", "SI એકમ")],
                  [[T("area", "ક્ષેત્રફળ"), T("length × length", "લંબાઈ × લંબાઈ"), T("m²")],
                   [T("velocity", "વેગ"), T("displacement / time", "સ્થાનાંતર / સમય"), T("m/s")],
                   [T("force", "બળ"), T("mass × acceleration", "દ્રવ્યમાન × પ્રવર્ગ"), T("N = kg·m/s²")],
                   [T("pressure", "દબાણ"), T("force / area", "બળ / ક્ષેત્રફળ"), T("Pa = N/m²")],
                   [T("work", "કાર્ય"), T("force × displacement", "બળ × સ્થાનાંતર"), T("J = N·m")],
                   [T("density", "ઘનતા"), T("mass / volume", "દ્રવ્યમાન / ઘનફળ"), T("kg/m³")]]),
               H4("Common mistake", "સામાન્ય ભૂલ"),
               P("Calling force a fundamental quantity because it feels basic. It is derived: "
                 "1 N = 1 kg·m/s².",
                 "બળને પાયાની રાશિ કહેવી કારણ કે તે મૂળભૂત લાગે છે. તે વ્યુત્પન્ન છે: 1 N = 1 kg·m/s².")],
              syllabus_item="1.2"),
         card(T("1.3 Systems of units: CGS, MKS and SI",
                "1.3 એકમ પદ્ધતિઓ: CGS, MKS અને SI"),
              [H4("Rule", "નિયમ"),
               P("A <b>system of units</b> is a complete, agreed set of base units with their multiples "
                 "and sub-multiples. The three met here are CGS, MKS and SI.",
                 "<b>એકમ પદ્ધતિ</b> એટલે પાયાના એકમોનો સંપૂર્ણ, સ્વીકૃત સમૂહ અને તેના ગુણક-અપવર્તક. "
                 "અહીં ત્રણ મળે છે: CGS, MKS અને SI."),
               TB([T("Quantity", "રાશિ"), T("CGS", "CGS"), T("MKS", "MKS"), T("SI", "SI")],
                  [[T("length", "લંબાઈ"), T("centimetre", "સેન્ટિમીટર"), T("metre", "મીટર"), T("metre", "મીટર")],
                   [T("mass", "દ્રવ્યમાન"), T("gram", "ગ્રામ"), T("kilogram", "કિલોગ્રામ"), T("kilogram", "કિલોગ્રામ")],
                   [T("time", "સમય"), T("second", "સેકન્ડ"), T("second", "સેકન્ડ"), T("second", "સેકન્ડ")],
                   [T("force", "બળ"), T("dyne", "ડાઇન"), T("newton", "ન્યૂટન"), T("newton", "ન્યૂટન")],
                   [T("work", "કાર્ય"), T("erg", "અર્ગ"), T("joule", "જૂલ"), T("joule", "જૂલ")],
                   [T("power", "શક્તિ"), T("erg/s", "અર્ગ/સે"), T("watt", "વોટ"), T("watt", "વોટ")]]),
               H4("Requirements of a standard unit", "માનક એકમની શરતો"),
               OL(("It must be well defined and unambiguous.", "તે સ્પષ્ટ અને એકાર્થી હોવું જોઈએ."),
                  ("It must not change with time, place or temperature.", "તે સમય, સ્થળ કે તાપમાન સાથે બદલાવું ન જોઈએ."),
                  ("It must be easily reproducible in a laboratory.", "તે પ્રયોગશાળામાં સહેલાઈથી પુનઃઉત્પાદિત થઈ શકે."),
                  ("It must be of a convenient size for daily use.", "તે રોજિંદા ઉપયોગ માટે અનુકૂળ માપનું હોવું જોઈએ."),
                  ("It must be internationally accepted.", "તે આંતરરાષ્ટ્રીય રીતે સ્વીકૃત હોવું જોઈએ.")),
               H4("Examples", "ઉદાહરણો"),
               TB([T("Situation", "પરિસ્થિતિ"), T("System normally used", "સામાન્ય રીતે વપરાતી પદ્ધતિ")],
                  [[T("laboratory experiment on a small wire", "નાના તાર પર પ્રયોગશાળાનો પ્રયોગ"), T("CGS (cm, g, dyne)", "CGS (cm, g, ડાઇન)")],
                   [T("machine-shop drawing", "મશીન શોપનું ડ્રોઇંગ"), T("MKS/SI (mm, kg, N)", "MKS/SI (mm, kg, N)")],
                   [T("engineering calculation and data sheet", "ઇજનેરી ગણતરી અને ડેટા શીટ"), T("SI", "SI")]]),
               H4("Common mistake", "સામાન્ય ભૂલ"),
               P("Mixing systems inside one calculation: 20 cm and 3 m added as 23. Convert first, "
                 "then calculate.",
                 "એક જ ગણતરીમાં પદ્ધતિઓ ભેગી કરવી: 20 cm અને 3 m ને 23 તરીકે જોડવા. પહેલાં રૂપાંતરણ કરો, "
                 "પછી ગણતરી.")],
              "u1_units", syllabus_item="1.3"),
         card(T("1.4 Interconversion of units (MKS and CGS)",
                "1.4 એકમોનું રૂપાંતરણ (MKS અને CGS)"),
              [H4("Method", "રીત"),
               OL(("Write the quantity as a number multiplied by its unit.", "રાશિને સંખ્યા × એકમ તરીકે લખો."),
                  ("Replace each unit by its equivalent in the target system.",
                   "દરેક એકમને લક્ષ્ય પદ્ધતિના સમાન મૂલ્યથી બદલો."),
                  ("Multiply the numbers and simplify the powers of ten.",
                   "સંખ્યાઓનો ગુણાકાર કરો અને દશના ઘાતાંક સાદા કરો.")),
               H4("Conversion factors worth memorising", "યાદ રાખવા જેવા રૂપાંતરણ અચળાંક"),
               TB([T("Quantity", "રાશિ"), T("From", "થી"), T("To", "સુધી"), T("Factor", "અચળાંક")],
                  [[T("length", "લંબાઈ"), T("1 m", "1 m"), T("cm", "cm"), T("100")],
                   [T("mass", "દ્રવ્યમાન"), T("1 kg", "1 kg"), T("g", "g"), T("1000")],
                   [T("force", "બળ"), T("1 N", "1 N"), T("dyne", "ડાઇન"), T("10⁵")],
                   [T("work or energy", "કાર્ય કે ઊર્જા"), T("1 J", "1 J"), T("erg", "અર્ગ"), T("10⁷")],
                   [T("power", "શક્તિ"), T("1 W", "1 W"), T("erg/s", "અર્ગ/સે"), T("10⁷")],
                   [T("pressure", "દબાણ"), T("1 Pa", "1 Pa"), T("dyne/cm²", "ડાઇન/cm²"), T("10")],
                   [T("density", "ઘનતા"), T("1 kg/m³", "1 kg/m³"), T("g/cm³", "g/cm³"), T("10⁻³")]]),
               H4("Worked example", "ઉકેલાયેલ દાખલો"),
               P("Convert 1 N into dyne. 1 N = 1 kg × 1 m/s² = 1000 g × 100 cm/s² = 10⁵ g·cm/s² = "
                 "10⁵ dyne.",
                 "1 N ને ડાઇનમાં ફેરવો. 1 N = 1 kg × 1 m/s² = 1000 g × 100 cm/s² = 10⁵ g·cm/s² = 10⁵ ડાઇન."),
               H4("Common mistake", "સામાન્ય ભૂલ"),
               P("Multiplying where you should divide. Going from a big unit to a small unit the number "
                 "grows; from small to big it shrinks.",
                 "ભાગ આપવાના સ્થાને ગુણાકાર કરવો. મોટા એકમથી નાના એકમમાં જતી વખતે સંખ્યા વધે છે; "
                 "નાનાથી મોટામાં જતી વખતે ઘટે છે.")],
              syllabus_item="1.3"),
         card(T("1.5 Dimensions as a check",
                "1.5 પરિમાણનો ઉપયોગ ચકાસણીમાં"),
              [H4("Rule", "નિયમ"),
               P("The <b>dimensional formula</b> of a quantity shows how it is built from L, M, T (and "
                 "A, K, mol, cd). Both sides of any correct equation must have the same dimensions.",
                 "રાશિનું <b>પરિમાણીય સૂત્ર</b> દર્શાવે છે કે તે L, M, T (અને A, K, mol, cd)માંથી કેવી "
                 "રીતે બને છે. કોઈપણ સાચા સમીકરણની બંને બાજુનાં પરિમાણ સમાન હોવાં જોઈએ."),
               TB([T("Quantity", "રાશિ"), T("Dimensional formula", "પરિમાણીય સૂત્ર")],
                  [[T("area", "ક્ષેત્રફળ"), T("[L²]", "[L²]")],
                   [T("volume", "ઘનફળ"), T("[L³]", "[L³]")],
                   [T("velocity", "વેગ"), T("[L T⁻¹]", "[L T⁻¹]")],
                   [T("acceleration", "પ્રવર્ગ"), T("[L T⁻²]", "[L T⁻²]")],
                   [T("force", "બળ"), T("[M L T⁻²]", "[M L T⁻²]")],
                   [T("pressure or stress", "દબાણ કે પ્રતિબળ"), T("[M L⁻¹ T⁻²]", "[M L⁻¹ T⁻²]")],
                   [T("work or energy", "કાર્ય કે ઊર્જા"), T("[M L² T⁻²]", "[M L² T⁻²]")],
                   [T("surface tension", "પૃષ્ઠતાણ"), T("[M T⁻²]", "[M T⁻²]")],
                   [T("coefficient of viscosity", "શ્યાનતા ગુણાંક"), T("[M L⁻¹ T⁻¹]", "[M L⁻¹ T⁻¹]")]]),
               H4("Worked check", "ઉકેલાયેલ ચકાસણી"),
               P("Check v = u + at. LHS: [L T⁻¹]. RHS: [L T⁻¹] + [L T⁻²][T] = [L T⁻¹] + [L T⁻¹]. Equal, "
                 "so the equation is dimensionally correct.",
                 "v = u + at ચકાસો. ડાબી બાજુ: [L T⁻¹]. જમણી બાજુ: [L T⁻¹] + [L T⁻²][T] = [L T⁻¹] + [L T⁻¹]. "
                 "સમાન છે, તેથી સમીકરણ પરિમાણીય રીતે સાચું છે."),
               H4("Common mistake", "સામાન્ય ભૂલ"),
               P("Thinking a dimensional check proves an equation. It only rules out wrong ones; a "
                 "missing numerical factor (2 in s = ½at²) passes the test.",
                 "પરિમાણીય ચકાસણી સમીકરણ સાબિત કરે છે એમ માનવું. તે ફક્ત ખોટાં સમીકરણો કાઢી નાખે છે; "
                 "ખોવાયેલો આંકડાકીય અવયવ (s = ½at²માં 2) ચકાસણી પાસ કરી જાય છે.")],
              syllabus_item="1.2"),
     ]},

    {"title": T("2. Vernier Calipers and Micrometer Screw Gauge",
                "2. વર્નિયર કેલિપર્સ અને માઇક્રોમીટર સ્ક્રુ ગેજ"),
     "items": [
         card(T("2.1 Vernier calipers: principle and construction",
                "2.1 વર્નિયર કેલિપર્સ: સિદ્ધાંત અને રચના"),
              [H4("Principle", "સિદ્ધાંત"),
               P("The vernier scale carries <i>n</i> divisions that cover <i>n − 1</i> divisions of "
                 "the main scale. The difference between one main-scale division and one vernier "
                 "division is the <b>least count</b>.",
                 "વર્નિયર સ્કેલના <i>n</i> વિભાગો મુખ્ય સ્કેલના <i>n − 1</i> વિભાગોને આવરી લે છે. એક "
                 "મુખ્ય વિભાગ અને એક વર્નિયર વિભાગના તફાવતને <b>લીસ્ટ કાઉન્ટ</b> કહે છે."),
               H4("Formula", "સૂત્ર"),
               P("<b>L.C. = 1 M.S.D. − 1 V.S.D. = (1 − (n − 1)/n) M.S.D. = M.S.D./n</b>",
                 "<b>L.C. = 1 M.S.D. − 1 V.S.D. = (1 − (n − 1)/n) M.S.D. = M.S.D./n</b>"),
               H4("Construction", "રચના"),
               UL(("Main scale on a steel rule, graduated in mm.", "સ્ટીલ રૂલ પર મુખ્ય સ્કેલ, mmમાં."),
                  ("Vernier scale on a sliding jaw.", "સરકતા જડબા પર વર્નિયર સ્કેલ."),
                  ("Fixed jaw and movable jaw for outside measurement.", "બહારના માપ માટે સ્થિર અને ચલ જડબું."),
                  ("Two upper jaws for internal measurement.", "આંતરિક માપ માટે ઉપરનાં બે જડબાં."),
                  ("Depth rod attached to the slider.", "સ્લાઇડર સાથે જોડાયેલ ઊંડાઈ સળિયો.")),
               H4("Worked example", "ઉકેલાયેલ દાખલો"),
               P("If 10 V.S.D. equal 9 M.S.D. and 1 M.S.D. = 1 mm, then L.C. = 1/10 mm = 0.1 mm.",
                 "જો 10 V.S.D. = 9 M.S.D. અને 1 M.S.D. = 1 mm, તો L.C. = 1/10 mm = 0.1 mm."),
               H4("Common mistake", "સામાન્ય ભૂલ"),
               P("Measuring a cylinder with the jaws pressed on a chamfer. The reading is short by the "
                 "chamfer width.",
                 "શેમ્ફર પર જડબાં દબાવીને સિલિન્ડર માપવો. વાંચન શેમ્ફરની પહોળાઈ જેટલું ઓછું આવે છે.")],
              "u1_vernier", syllabus_item="1.4"),
         card(T("2.2 Reading a vernier caliper",
                "2.2 વર્નિયર કેલિપરનું વાંચન"),
              [H4("Method", "રીત"),
               OL(("Read the main scale just before the vernier zero (M.S.R.).",
                   "વર્નિયરના શૂન્ય પહેલાંનું મુખ્ય સ્કેલ વાંચો (M.S.R.)."),
                  ("Find the vernier division that coincides with a main-scale line (V.C.).",
                   "મુખ્ય સ્કેલની કોઈ રેખા સાથે મળતો વર્નિયર વિભાગ શોધો (V.C.)."),
                  ("Add L.C. × V.C. to M.S.R.", "M.S.R.માં L.C. × V.C. ઉમેરો."),
                  ("Correct the zero error with its sign.", "શૂન્ય ભૂલને તેના ચિહ્ન સાથે સુધારો.")),
               TB([T("Reading", "વાંચન"), T("M.S.R.", "M.S.R."), T("V.C.", "V.C."), T("L.C.", "L.C."), T("Result", "પરિણામ")],
                  [[T("1", "1"), T("2.3 cm", "2.3 cm"), T("6", "6"), T("0.01 cm", "0.01 cm"), T("2.36 cm", "2.36 cm")],
                   [T("2", "2"), T("15 mm", "15 mm"), T("4", "4"), T("0.1 mm", "0.1 mm"), T("15.4 mm", "15.4 mm")],
                   [T("3", "3"), T("0.0 mm", "0.0 mm"), T("27", "27"), T("0.02 mm", "0.02 mm"), T("0.54 mm", "0.54 mm")]]),
               H4("Zero error", "શૂન્ય ભૂલ"),
               UL(("Positive zero error: the vernier zero lies to the right of the main zero. "
                   "<b>Correction = − Z.E.</b>",
                   "ધન શૂન્ય ભૂલ: વર્નિયરનું શૂન્ય મુખ્ય શૂન્યની જમણી બાજુ હોય. <b>સુધારો = − Z.E.</b>"),
                  ("Negative zero error: the vernier zero lies to the left. <b>Correction = + |Z.E.|</b>",
                   "ઋણ શૂન્ય ભૂલ: વર્નિયરનું શૂન્ય ડાબી બાજુ હોય. <b>સુધારો = + |Z.E.|</b>")),
               H4("Worked example", "ઉકેલાયેલ દાખલો"),
               P("Zero error +0.03 cm and observed reading 2.36 cm give a true value of "
                 "2.36 − 0.03 = 2.33 cm.",
                 "શૂન્ય ભૂલ +0.03 cm અને વાંચન 2.36 cm હોય તો સાચું મૂલ્ય 2.36 − 0.03 = 2.33 cm."),
               H4("Common mistake", "સામાન્ય ભૂલ"),
               P("Adding the zero error instead of subtracting it when it is positive.",
                 "ધન શૂન્ય ભૂલ હોય ત્યારે તેને બાદ કરવાના સ્થાને ઉમેરી દેવી.")],
              syllabus_item="1.4"),
         card(T("2.3 Micrometer screw gauge",
                "2.3 માઇક્રોમીટર સ્ક્રુ ગેજ"),
              [H4("Principle", "સિદ્ધાંત"),
               P("A screw advances by one <b>pitch</b> in one full rotation. The circular scale "
                 "divides that pitch into many parts, so a small rotation gives a very small "
                 "movement.",
                 "સ્ક્રુ એક પૂર્ણ ભ્રમણમાં એક <b>પિચ</b> જેટલો આગળ વધે છે. વર્તુળાકાર સ્કેલ તે પિચને ઘણા "
                 "ભાગમાં વહેંચે છે, તેથી થોડું ભ્રમણ ઘણું નાનું સ્થાનાંતર આપે છે."),
               P("<b>L.C. = pitch / number of circular-scale divisions</b>",
                 "<b>L.C. = પિચ / વર્તુળાકાર સ્કેલના વિભાગોની સંખ્યા</b>"),
               H4("Construction", "રચના"),
               UL(("U-shaped frame and fixed anvil.", "U આકારનો ફ્રેમ અને સ્થિર એન્વિલ."),
                  ("Spindle turned by a ratchet.", "રેચિટથી ફરતો સ્પિન્ડલ."),
                  ("Sleeve (main) scale in mm and half-mm.", "સ્લીવ (મુખ્ય) સ્કેલ mm અને અડધા mmમાં."),
                  ("Thimble with 50 or 100 divisions.", "50 કે 100 વિભાગવાળું થિંબલ."),
                  ("Ratchet to avoid over-tightening.", "વધુ કસવાથી બચવા રેચિટ.")),
               TB([T("Pitch", "પિચ"), T("Circular divisions", "વર્તુળાકાર વિભાગ"), T("Least count", "લીસ્ટ કાઉન્ટ")],
                  [[T("0.5 mm", "0.5 mm"), T("50", "50"), T("0.01 mm", "0.01 mm")],
                   [T("1.0 mm", "1.0 mm"), T("100", "100"), T("0.01 mm", "0.01 mm")],
                   [T("0.5 mm", "0.5 mm"), T("100", "100"), T("0.005 mm", "0.005 mm")]]),
               H4("Common mistake", "સામાન્ય ભૂલ"),
               P("Screwing until the ratchet clicks many times. The anvil digs in and the wire reads "
                 "thin.",
                 "રેચિટ ઘણી વાર ક્લિક થાય ત્યાં સુધી કસવું. એન્વિલ દબાઈ જાય છે અને તારનું માપ ઓછું આવે છે.")],
              "u1_micrometer", syllabus_item="1.4"),
         card(T("2.4 Reading a screw gauge and its errors",
                "2.4 સ્ક્રુ ગેજનું વાંચન અને તેની ભૂલો"),
              [H4("Method", "રીત"),
               OL(("Read the sleeve scale (S.S.R.).", "સ્લીવ સ્કેલ વાંચો (S.S.R.)."),
                  ("Read the thimble division on the reference line (C.S.R.).",
                   "સંદર્ભ રેખા પરનો થિંબલ વિભાગ વાંચો (C.S.R.)."),
                  ("Compute reading = S.S.R. + C.S.R. × L.C.", "વાંચન = S.S.R. + C.S.R. × L.C. ગણો."),
                  ("Apply the zero-error correction with its sign.", "શૂન્ય ભૂલનો સુધારો ચિહ્ન સાથે લાગુ કરો.")),
               H4("Worked example", "ઉકેલાયેલ દાખલો"),
               P("S.S.R. = 4.5 mm, C.S.R. = 32, L.C. = 0.01 mm, so reading = 4.5 + 0.32 = 4.82 mm. "
                 "With a zero error of +0.02 mm the true diameter is 4.80 mm.",
                 "S.S.R. = 4.5 mm, C.S.R. = 32, L.C. = 0.01 mm, તેથી વાંચન = 4.5 + 0.32 = 4.82 mm. "
                 "+0.02 mm શૂન્ય ભૂલ સાથે સાચો વ્યાસ 4.80 mm."),
               H4("Errors of the two instruments", "બંને સાધનોની ભૂલો"),
               TB([T("Error", "ભૂલ"), T("Cause", "કારણ"), T("Cure", "ઉપાય")],
                  [[T("zero error", "શૂન્ય ભૂલ"), T("jaws or anvil not closing at zero", "જડબાં કે એન્વિલ શૂન્ય પર બંધ ન થાય"), T("measure it and correct every reading", "તે માપો અને દરેક વાંચન સુધારો")],
                   [T("parallax error", "પેરાલેક્સ ભૂલ"), T("eye not perpendicular to the scale", "આંખ સ્કેલને લંબ ન હોય"), T("view straight on, use the mirror", "સીધું જુઓ, અરીસાનો ઉપયોગ કરો")],
                   [T("wear of jaws", "જડબાંનો ઘસારો"), T("old instrument", "જૂનું સાધન"), T("calibrate against a slip gauge", "સ્લિપ ગેજ સામે કેલિબ્રેટ કરો")],
                   [T("excess pressure", "વધુ દબાણ"), T("screw tightened hard", "સ્ક્રુ કસીને બંધ કરવો"), T("use the ratchet", "રેચિટ વાપરો")],
                   [T("temperature", "તાપમાન"), T("job and gauge at different temperatures", "જોબ અને ગેજ જુદા તાપમાને"), T("measure at 20 °C", "20 °C પર માપો")]]),
               H4("Common mistake", "સામાન્ય ભૂલ"),
               P("Reading the half-millimetre line as zero when it is visible below the thimble. The "
                 "answer is then short by exactly 0.5 mm.",
                 "થિંબલ નીચે દેખાતી અડધા મિલીમીટરની રેખાને શૂન્ય ગણવી. પછી જવાબ બરાબર 0.5 mm ઓછો આવે છે.")],
              syllabus_item="1.4"),
     ]},

    {"title": T("3. Accuracy, Precision and Errors", "3. ચોકસાઈ, પરિશુદ્ધતા અને ભૂલો"),
     "items": [
         card(T("3.1 Accuracy and precision",
                "3.1 ચોકસાઈ અને પરિશુદ્ધતા"),
              [H4("Definitions", "વ્યાખ્યાઓ"),
               P("<b>Accuracy</b> says how close a measured value is to the true value. "
                 "<b>Precision</b> says how close repeated measurements are to each other.",
                 "<b>ચોકસાઈ</b> દર્શાવે છે કે માપેલું મૂલ્ય સાચા મૂલ્યની કેટલું નજીક છે. "
                 "<b>પરિશુદ્ધતા</b> દર્શાવે છે કે વારંવાર લીધેલાં માપન એકબીજાની કેટલાં નજીક છે."),
               TB([T("Case", "સ્થિતિ"), T("Readings", "વાંચન"), T("True", "સાચું"), T("Verdict", "નિષ્કર્ષ")],
                  [[T("A", "A"), T("9.81, 9.82, 9.80", "9.81, 9.82, 9.80"), T("9.81", "9.81"), T("accurate and precise", "ચોકસાઈપૂર્ણ અને પરિશુદ્ધ")],
                   [T("B", "B"), T("9.79, 9.80, 9.79", "9.79, 9.80, 9.79"), T("9.81", "9.81"), T("precise but not accurate", "પરિશુદ્ધ પણ ચોકસાઈપૂર્ણ નહીં")],
                   [T("C", "C"), T("9.60, 9.85, 9.95", "9.60, 9.85, 9.95"), T("9.81", "9.81"), T("neither", "બંને નહીં")]]),
               H4("Why they differ", "બંને કેમ જુદા પડે"),
               UL(("A wrongly zeroed instrument is precise but inaccurate.",
                   "ખોટી રીતે ઝીરો કરેલું સાધન પરિશુદ્ધ હોય પણ ચોકસાઈપૂર્ણ નહીં."),
                  ("A careless hand gives scattered readings, so the result is neither.",
                   "બેદરકાર હાથ વિખરાયેલાં વાંચન આપે, તેથી પરિણામ બંને રીતે ખોટું."),
                  ("Calibration improves accuracy; careful technique improves precision.",
                   "કેલિબ્રેશન ચોકસાઈ સુધારે છે; કાળજીપૂર્વકની પદ્ધતિ પરિશુદ્ધતા સુધારે છે.")),
               H4("Example", "ઉદાહરણ"),
               P("An electronic balance that reads 50.02 g, 50.02 g, 50.02 g for a 49.90 g standard is "
                 "precise and inaccurate; the zero must be reset.",
                 "ઇલેક્ટ્રોનિક બેલેન્સ 49.90 g માનક માટે 50.02 g, 50.02 g, 50.02 g વાંચે તો તે પરિશુદ્ધ "
                 "છે પણ ચોકસાઈપૂર્ણ નથી; શૂન્ય ફરી સેટ કરવું પડશે."),
               H4("Common mistake", "સામાન્ય ભૂલ"),
               P("Using the two words as synonyms. An exam answer must define both and then compare.",
                 "બંને શબ્દોને સમાનાર્થી ગણવા. પરીક્ષાના જવાબમાં બંનેની વ્યાખ્યા આપી પછી સરખામણી કરવી.")],
              "u1_accuracy", syllabus_item="1.5"),
         card(T("3.2 Types of errors", "3.2 ભૂલોના પ્રકાર"),
              [H4("The three types", "ત્રણ પ્રકાર"),
               TB([T("Type", "પ્રકાર"), T("Cause", "કારણ"), T("Behaviour", "વર્તન"), T("Cure", "ઉપાય")],
                  [[T("systematic", "ક્રમબદ્ધ"), T("zero error, wrong scale, wrong formula", "શૂન્ય ભૂલ, ખોટો સ્કેલ, ખોટું સૂત્ર"), T("same sign every time", "દર વખતે એક જ ચિહ્ન"), T("calibrate, correct the formula", "કેલિબ્રેશન, સૂત્ર સુધારો")],
                   [T("random", "યાદૃચ્છિક"), T("handling, vibration, changing temperature", "હેન્ડલિંગ, કંપન, બદલાતું તાપમાન"), T("scattered both ways", "બંને બાજુ વિખરાયેલી"), T("repeat and take the mean", "વારંવાર માપી સરેરાશ લો")],
                   [T("gross", "ઘોર"), T("misreading, wrong unit, wrong entry", "ખોટું વાંચન, ખોટું એકમ, ખોટી નોંધ"), T("large and obvious", "મોટી અને સ્પષ્ટ"), T("recheck the reading and the unit", "વાંચન અને એકમ ફરી ચકાસો")]]),
               H4("Examples", "ઉદાહરણો"),
               UL(("Systematic: a vernier with +0.03 cm zero error reads every length 0.03 cm long.",
                   "ક્રમબદ્ધ: +0.03 cm શૂન્ય ભૂલવાળું વર્નિયર દરેક લંબાઈ 0.03 cm વધુ વાંચે."),
                  ("Random: five readings of a wire diameter spread from 0.98 mm to 1.02 mm.",
                   "યાદૃચ્છિક: તારના વ્યાસનાં પાંચ વાંચન 0.98 mm થી 1.02 mm સુધી વિખરાયેલાં."),
                  ("Gross: a 25 mm reading entered as 2.5 mm on the job card.",
                   "ઘોર: જોબ કાર્ડ પર 25 mm વાંચન 2.5 mm લખાઈ જવું.")),
               H4("Common mistake", "સામાન્ય ભૂલ"),
               P("Averaging a systematic error away. Repeating a wrongly zeroed instrument gives the "
                 "same wrong answer with great confidence.",
                 "ક્રમબદ્ધ ભૂલને સરેરાશથી દૂર કરવાનો પ્રયત્ન. ખોટી રીતે ઝીરો કરેલું સાધન વારંવાર વાપરવાથી "
                 "એ જ ખોટો જવાબ આત્મવિશ્વાસ સાથે મળે.")],
              syllabus_item="1.5"),
         card(T("3.3 Absolute, relative and percentage error",
                "3.3 નિરપેક્ષ, સાપેક્ષ અને ટકાવારી ભૂલ"),
              [H4("Formulae", "સૂત્રો"),
               TB([T("Name", "નામ"), T("Formula", "સૂત્ર"), T("Unit", "એકમ")],
                  [[T("absolute error", "નિરપેક્ષ ભૂલ"), T("Δa = |a<sub>measured</sub> − a<sub>true</sub>|", "Δa = |a<sub>માપેલ</sub> − a<sub>સાચું</sub>|"), T("same as the quantity", "રાશિ જેવું જ")],
                   [T("mean absolute error", "સરેરાશ નિરપેક્ષ ભૂલ"), T("Δa<sub>mean</sub> = (Δa₁ + Δa₂ + …)/n", "Δa<sub>mean</sub> = (Δa₁ + Δa₂ + …)/n"), T("same as the quantity", "રાશિ જેવું જ")],
                   [T("relative error", "સાપેક્ષ ભૂલ"), T("Δa / a", "Δa / a"), T("no unit", "એકમ નહીં")],
                   [T("percentage error", "ટકાવારી ભૂલ"), T("(Δa / a) × 100 %", "(Δa / a) × 100 %"), T("%")]]),
               H4("Worked example", "ઉકેલાયેલ દાખલો"),
               P("A length measures 24.8 cm against a true value of 25.0 cm. Absolute error = 0.2 cm; "
                 "relative error = 0.2/25.0 = 0.008; percentage error = 0.8 %.",
                 "લંબાઈ 24.8 cm મળે છે જ્યારે સાચું મૂલ્ય 25.0 cm છે. નિરપેક્ષ ભૂલ = 0.2 cm; સાપેક્ષ ભૂલ "
                 "= 0.2/25.0 = 0.008; ટકાવારી ભૂલ = 0.8 %."),
               H4("Errors combine, they do not cancel", "ભૂલો જોડાય છે, રદ થતી નથી"),
               TB([T("Combination", "સંયોજન"), T("Rule for maximum error", "મહત્તમ ભૂલનો નિયમ")],
                  [[T("sum or difference, Z = A ± B", "સરવાળો કે તફાવત, Z = A ± B"), T("ΔZ = ΔA + ΔB", "ΔZ = ΔA + ΔB")],
                   [T("product or quotient, Z = AB or A/B", "ગુણાકાર કે ભાગાકાર, Z = AB કે A/B"), T("ΔZ/Z = ΔA/A + ΔB/B", "ΔZ/Z = ΔA/A + ΔB/B")],
                   [T("power, Z = Aⁿ", "ઘાત, Z = Aⁿ"), T("ΔZ/Z = n (ΔA/A)", "ΔZ/Z = n (ΔA/A)")]]),
               H4("Common mistake", "સામાન્ય ભૂલ"),
               P("Subtracting errors because the quantities are subtracted. A difference of two large "
                 "numbers has a large relative error.",
                 "રાશિઓ બાદ કરાય છે તેથી ભૂલો પણ બાદ કરવી. બે મોટી સંખ્યાઓના તફાવતમાં સાપેક્ષ ભૂલ મોટી "
                 "થાય છે.")],
              syllabus_item="1.5"),
         card(T("3.4 Rounding off and significant figures",
                "3.4 રાઉન્ડિંગ ઓફ અને સાર્થક અંકો"),
              [H4("Rounding rules", "રાઉન્ડિંગના નિયમો"),
               OL(("If the digit dropped is more than 5, add 1 to the last kept digit.",
                   "કાઢવાનો અંક 5થી મોટો હોય તો રાખેલા છેલ્લા અંકમાં 1 ઉમેરો."),
                  ("If it is less than 5, leave the last kept digit unchanged.",
                   "તે 5થી નાનો હોય તો રાખેલો છેલ્લો અંક જેમ છે તેમ રાખો."),
                  ("If it is exactly 5, make the last kept digit even.",
                   "તે બરાબર 5 હોય તો રાખેલા છેલ્લા અંકને યુગ્મ બનાવો.")),
               H4("Significant-figure rules", "સાર્થક અંકોના નિયમો"),
               TB([T("Rule", "નિયમ"), T("Example", "ઉદાહરણ")],
                  [[T("all non-zero digits count", "બધા શૂન્યેતર અંક ગણાય"), T("245 has 3", "245માં 3")],
                   [T("zeros between non-zero digits count", "શૂન્યેતર અંકો વચ્ચેના શૂન્ય ગણાય"), T("2.045 has 4", "2.045માં 4")],
                   [T("leading zeros do not count", "શરૂઆતના શૂન્ય ગણાય નહીં"), T("0.0025 has 2", "0.0025માં 2")],
                   [T("trailing zeros after a decimal count", "દશાંશ પછીના અંતિમ શૂન્ય ગણાય"), T("2.500 has 4", "2.500માં 4")],
                   [T("trailing zeros in a whole number are ambiguous", "પૂર્ણ સંખ્યામાં અંતિમ શૂન્ય અસ્પષ્ટ"), T("write 2.5 × 10³", "2.5 × 10³ લખો")]]),
               H4("In calculations", "ગણતરીમાં"),
               UL(("Multiplication and division: keep the smallest number of significant figures.",
                   "ગુણાકાર અને ભાગાકાર: સૌથી ઓછા સાર્થક અંકો રાખો."),
                  ("Addition and subtraction: keep the smallest number of decimal places.",
                   "સરવાળો અને તફાવત: સૌથી ઓછા દશાંશ સ્થાન રાખો.")),
               H4("Worked example", "ઉકેલાયેલ દાખલો"),
               P("2.5 × 1.25 = 3.125. The inputs have 2 and 3 significant figures, so the answer is "
                 "3.1 (2 s.f.). 12.11 + 18.0 + 1.013 = 31.123 becomes 31.1.",
                 "2.5 × 1.25 = 3.125. ઇનપુટમાં 2 અને 3 સાર્થક અંક છે, તેથી જવાબ 3.1 (2 s.f.). "
                 "12.11 + 18.0 + 1.013 = 31.123 એટલે 31.1."),
               H4("Common mistake", "સામાન્ય ભૂલ"),
               P("Copying all the digits from a calculator. The extra digits claim an accuracy the "
                 "instrument never had.",
                 "કેલ્ક્યુલેટરના બધા અંક ઉતારી લેવા. વધારાના અંક એ ચોકસાઈ દર્શાવે છે જે સાધનમાં કદી હતી જ નહીં.")],
              "u1_sigfig", syllabus_item="1.5"),
     ]},

    {"title": T("4. Measurement in the Workshop", "4. કાર્યશાળામાં માપન"),
     "items": [
         card(T("4.1 Choosing the instrument for the tolerance",
                "4.1 ટોલરન્સ માટે સાધનની પસંદગી"),
              [H4("Rule of thumb", "સામાન્ય નિયમ"),
               P("The least count of the instrument should be about one tenth of the tolerance you "
                 "have to check.",
                 "સાધનનું લીસ્ટ કાઉન્ટ તમારે ચકાસવાના ટોલરન્સના લગભગ દશમા ભાગ જેટલું હોવું જોઈએ."),
               TB([T("Tolerance", "ટોલરન્સ"), T("Instrument", "સાધન"), T("Least count", "લીસ્ટ કાઉન્ટ")],
                  [[T("±0.5 mm", "±0.5 mm"), T("steel rule", "સ્ટીલ રૂલ"), T("0.5 mm", "0.5 mm")],
                   [T("±0.1 mm", "±0.1 mm"), T("vernier caliper", "વર્નિયર કેલિપર"), T("0.02 mm", "0.02 mm")],
                   [T("±0.02 mm", "±0.02 mm"), T("micrometer screw gauge", "માઇક્રોમીટર સ્ક્રુ ગેજ"), T("0.01 mm", "0.01 mm")],
                   [T("±0.005 mm", "±0.005 mm"), T("dial gauge or air gauge", "ડાયલ ગેજ કે એર ગેજ"), T("0.001 mm", "0.001 mm")]]),
               H4("Example", "ઉદાહરણ"),
               P("A bearing seat is drawn 40.00 ±0.02 mm. A caliper with 0.02 mm least count can barely "
                 "decide; a screw gauge with 0.01 mm is the correct choice.",
                 "બેરિંગ સીટ 40.00 ±0.02 mm છે. 0.02 mm લીસ્ટ કાઉન્ટવાળું કેલિપર ભાગ્યે જ નિર્ણય આપી "
                 "શકે; 0.01 mm વાળું સ્ક્રુ ગેજ યોગ્ય પસંદગી છે."),
               H4("Common mistake", "સામાન્ય ભૂલ"),
               P("Rejecting a good part because the instrument was coarse. Decide the instrument before "
                 "you decide the part.",
                 "સાધન જાડું હોવાથી સારો પાર્ટ રિજેક્ટ કરવો. પાર્ટનો નિર્ણય કરતાં પહેલાં સાધન નક્કી કરો.")],
              syllabus_item="1.4"),
         card(T("4.2 Recording a measurement correctly",
                "4.2 માપનની સાચી નોંધ"),
              [H4("Three parts of a measurement", "માપનના ત્રણ ભાગ"),
               TB([T("Part", "ભાગ"), T("Example", "ઉદાહરણ"), T("Why", "કેમ")],
                  [[T("number", "સંખ્યા"), T("25.04", "25.04"), T("carries the value", "મૂલ્ય દર્શાવે")],
                   [T("unit", "એકમ"), T("mm", "mm"), T("gives the scale", "માપક્રમ આપે")],
                   [T("uncertainty", "અનિશ્ચિતતા"), T("±0.01 mm", "±0.01 mm"), T("says how far to trust it", "કેટલો ભરોસો કરવો તે કહે")]]),
               H4("Good and bad entries", "સારી અને ખરાબ નોંધ"),
               TB([T("Bad entry", "ખરાબ નોંધ"), T("Problem", "સમસ્યા"), T("Good entry", "સારી નોંધ")],
                  [[T("25", "25"), T("no unit", "એકમ નહીં"), T("25.00 mm", "25.00 mm")],
                   [T("25.0437", "25.0437"), T("more digits than the tool can read", "સાધન વાંચી શકે તેનાથી વધુ અંક"), T("25.04 mm", "25.04 mm")],
                   [T("about 25", "લગભગ 25"), T("no value at all", "કોઈ મૂલ્ય નહીં"), T("25.04 ± 0.01 mm", "25.04 ± 0.01 mm")]]),
               H4("Example", "ઉદાહરણ"),
               P("A screw gauge reads 4.82 mm with a least count of 0.01 mm. Write 4.82 ± 0.01 mm, not "
                 "4.8 mm and not 4.8200 mm.",
                 "સ્ક્રુ ગેજ 4.82 mm વાંચે છે અને લીસ્ટ કાઉન્ટ 0.01 mm છે. 4.82 ± 0.01 mm લખો, 4.8 mm કે "
                 "4.8200 mm નહીં."),
               H4("Common mistake", "સામાન્ય ભૂલ"),
               P("Writing the uncertainty as ±0.01 when the zero error was never measured.",
                 "શૂન્ય ભૂલ માપી જ ન હોય તોપણ અનિશ્ચિતતા ±0.01 લખવી.")],
              syllabus_item="1.5"),
         card(T("4.3 Four errors that ruin a good instrument",
                "4.3 સારા સાધનને બગાડતી ચાર ભૂલો"),
              [H4("The list", "યાદી"),
               TB([T("Error", "ભૂલ"), T("How it happens", "કેવી રીતે થાય"), T("Cure", "ઉપાય")],
                  [[T("parallax", "પેરાલેક્સ"), T("eye not square to the scale", "આંખ સ્કેલને લંબ ન હોય"), T("view straight on; use the mirror", "સીધું જુઓ; અરીસો વાપરો")],
                   [T("zero error", "શૂન્ય ભૂલ"), T("jaws do not close at 0.00", "જડબાં 0.00 પર બંધ ન થાય"), T("measure and correct it", "તે માપો અને સુધારો")],
                   [T("temperature", "તાપમાન"), T("part measured hot after machining", "મશીનિંગ પછી ગરમ પાર્ટ માપવો"), T("cool to 20 °C", "20 °C સુધી ઠંડું કરો")],
                   [T("pressure", "દબાણ"), T("jaws or spindle forced", "જડબાં કે સ્પિન્ડલ પર જોર"), T("light touch or ratchet", "હળવો સ્પર્શ કે રેચિટ")]]),
               H4("Example", "ઉદાહરણ"),
               P("A 100 mm aluminium part measured at 60 °C reads about 0.13 mm larger than at 20 °C "
                 "(α ≈ 23 × 10⁻⁶ /°C), which is more than a typical tolerance.",
                 "100 mm નો એલ્યુમિનિયમ પાર્ટ 60 °C પર માપતાં 20 °C કરતાં લગભગ 0.13 mm મોટો વંચાય છે "
                 "(α ≈ 23 × 10⁻⁶ /°C), જે સામાન્ય ટોલરન્સ કરતાં વધુ છે."),
               H4("Common mistake", "સામાન્ય ભૂલ"),
               P("Blaming the instrument. Nine times out of ten the error is in the hand that holds it.",
                 "સાધનને દોષ દેવો. દસમાંથી નવ વાર ભૂલ સાધન પકડનારા હાથમાં હોય છે.")],
              syllabus_item="1.5"),
         card(T("4.4 What the exam asks from Unit 1",
                "4.4 યુનિટ 1 પરથી પરીક્ષામાં શું પૂછાય"),
              [H4("Question types", "પ્રશ્નના પ્રકાર"),
               TB([T("Question", "પ્રશ્ન"), T("What to write", "શું લખવું"), T("Marks", "માર્ક્સ")],
                  [[T("Define fundamental and derived quantities with examples", "પાયાની અને વ્યુત્પન્ન રાશિઓ ઉદાહરણ સાથે સમજાવો"), T("definition + table of 4 examples each", "વ્યાખ્યા + દરેકના 4 ઉદાહરણનું કોષ્ટક"), T("3-4", "3-4")],
                   [T("Explain vernier calipers", "વર્નિયર કેલિપર્સ સમજાવો"), T("principle, L.C. formula, construction, one reading", "સિદ્ધાંત, L.C. સૂત્ર, રચના, એક વાંચન"), T("4-7", "4-7")],
                   [T("Difference between accuracy and precision", "ચોકસાઈ અને પરિશુદ્ધતાનો ભેદ"), T("two definitions + example table", "બે વ્યાખ્યા + ઉદાહરણ કોષ્ટક"), T("3-4", "3-4")],
                   [T("Numerical on error", "ભૂલ પર દાખલો"), T("formula, substitution, unit, % sign", "સૂત્ર, આંકડા, એકમ, % ચિહ્ન"), T("3-4", "3-4")],
                   [T("Convert 1 N into dyne", "1 N ને ડાઇનમાં ફેરવો"), T("full substitution, not just the answer", "ફક્ત જવાબ નહીં, પૂરું આંકડા મૂકવું"), T("2-3", "2-3")]]),
               H4("Time plan for a 7-mark answer", "7 માર્કના જવાબનો સમય પ્લાન"),
               OL(("Half a page of principle and formula.", "અડધું પાનું સિદ્ધાંત અને સૂત્ર."),
                  ("A labelled sketch (caliper or gauge).", "લેબલવાળું ચિત્ર (કેલિપર કે ગેજ)."),
                  ("One worked reading with zero-error correction.", "શૂન્ય ભૂલ સુધારા સાથે એક ઉકેલાયેલ વાંચન."),
                  ("One line of application in the workshop.", "કાર્યશાળામાં ઉપયોગની એક લાઇન.")),
               H4("Common mistake", "સામાન્ય ભૂલ"),
               P("Writing the formula and jumping to the answer. Marks are given for the substitution "
                 "and the unit.",
                 "સૂત્ર લખીને સીધું જવાબ પર કૂદી જવું. આંકડા મૂકવા અને એકમ માટે માર્ક્સ મળે છે.")],
              syllabus_item="1.1"),
     ]},

    {"title": T("5. Practice Questions with Model Answers", "5. સરાવ પ્રશ્નો અને આદર્શ જવાબો"),
     "items": []},
]

NUMERICALS = [
    num("u1n01", T("Convert 1 N into dyne.", "1 N ને ડાઇનમાં ફેરવો."),
        T("Convert 1 newton into the CGS unit of force.", "1 ન્યૂટનને બળના CGS એકમમાં ફેરવો."),
        [P("1 N = 1 kg × 1 m/s²", "1 N = 1 kg × 1 m/s²"),
         P("= (1000 g) × (100 cm/s²) = 10⁵ g·cm/s²", "= (1000 g) × (100 cm/s²) = 10⁵ g·cm/s²"),
         P("g·cm/s² is the dyne, so 1 N = 10⁵ dyne.", "g·cm/s² એ ડાઇન છે, તેથી 1 N = 10⁵ ડાઇન.")],
        T("1 N = 10⁵ dyne", "1 N = 10⁵ ડાઇન")),
    num("u1n02", T("Convert 1 J into erg.", "1 J ને અર્ગમાં ફેરવો."),
        T("Convert one joule into the CGS unit of work.", "1 જૂલને કાર્યના CGS એકમમાં ફેરવો."),
        [P("1 J = 1 N × 1 m = 10⁵ dyne × 100 cm", "1 J = 1 N × 1 m = 10⁵ ડાઇન × 100 cm"),
         P("= 10⁷ dyne·cm = 10⁷ erg", "= 10⁷ ડાઇન·cm = 10⁷ અર્ગ")],
        T("1 J = 10⁷ erg", "1 J = 10⁷ અર્ગ")),
    num("u1n03", T("Convert 1 W into erg/s.", "1 W ને અર્ગ/સેમાં ફેરવો."),
        T("Convert one watt into the CGS unit of power.", "1 વોટને શક્તિના CGS એકમમાં ફેરવો."),
        [P("1 W = 1 J/s = 10⁷ erg / 1 s", "1 W = 1 J/s = 10⁷ અર્ગ / 1 s"),
         P("= 10⁷ erg/s", "= 10⁷ અર્ગ/સે")],
        T("1 W = 10⁷ erg/s", "1 W = 10⁷ અર્ગ/સે")),
    num("u1n04", T("Convert 2.7 g/cm³ into kg/m³.", "2.7 g/cm³ ને kg/m³ માં ફેરવો."),
        T("The density of aluminium is 2.7 g/cm³. Express it in SI units.",
          "એલ્યુમિનિયમની ઘનતા 2.7 g/cm³ છે. તેને SI એકમમાં દર્શાવો."),
        [P("1 g/cm³ = 10⁻³ kg / 10⁻⁶ m³ = 10³ kg/m³", "1 g/cm³ = 10⁻³ kg / 10⁻⁶ m³ = 10³ kg/m³"),
         P("So 2.7 g/cm³ = 2.7 × 10³ = 2700 kg/m³.", "તેથી 2.7 g/cm³ = 2.7 × 10³ = 2700 kg/m³.")],
        T("2700 kg/m³", "2700 kg/m³")),
    num("u1n05", T("Convert 72 km/h into m/s.", "72 km/h ને m/s માં ફેરવો."),
        T("A truck runs at 72 km/h. What is its speed in SI units?",
          "એક ટ્રક 72 km/h ઝડપે દોડે છે. SI એકમમાં તેની ઝડપ કેટલી?"),
        [P("72 km/h = 72 × (1000 m / 3600 s)", "72 km/h = 72 × (1000 m / 3600 s)"),
         P("= 72 × (5/18) = 20 m/s", "= 72 × (5/18) = 20 m/s")],
        T("20 m/s", "20 m/s")),
    num("u1n06", T("Least count when 10 V.S.D. = 9 M.S.D. (1 M.S.D. = 1 mm).",
                   "જ્યારે 10 V.S.D. = 9 M.S.D. (1 M.S.D. = 1 mm) ત્યારે લીસ્ટ કાઉન્ટ."),
        T("A vernier has 10 divisions covering 9 main-scale divisions of 1 mm each. Find its least "
          "count.", "વર્નિયરના 10 વિભાગ 1 mmના 9 મુખ્ય વિભાગો આવરે છે. તેનું લીસ્ટ કાઉન્ટ શોધો."),
        [P("L.C. = 1 M.S.D. − 1 V.S.D. = 1 mm − 0.9 mm", "L.C. = 1 M.S.D. − 1 V.S.D. = 1 mm − 0.9 mm"),
         P("= 0.1 mm = 0.01 cm", "= 0.1 mm = 0.01 cm")],
        T("L.C. = 0.1 mm", "L.C. = 0.1 mm")),
    num("u1n07", T("Least count when 20 V.S.D. = 19 M.S.D.", "જ્યારે 20 V.S.D. = 19 M.S.D. ત્યારે લીસ્ટ કાઉન્ટ."),
        T("A vernier with 20 divisions coincides with 19 mm. Find the least count.",
          "20 વિભાગવાળું વર્નિયર 19 mm સાથે મળે છે. લીસ્ટ કાઉન્ટ શોધો."),
        [P("1 V.S.D. = 19/20 mm = 0.95 mm", "1 V.S.D. = 19/20 mm = 0.95 mm"),
         P("L.C. = 1 − 0.95 = 0.05 mm", "L.C. = 1 − 0.95 = 0.05 mm")],
        T("L.C. = 0.05 mm", "L.C. = 0.05 mm")),
    num("u1n08", T("Least count when 50 V.S.D. = 49 M.S.D.", "જ્યારે 50 V.S.D. = 49 M.S.D. ત્યારે લીસ્ટ કાઉન્ટ."),
        T("A precision vernier has 50 divisions over 49 mm. Find its least count.",
          "ચોકસાઈવાળા વર્નિયરના 50 વિભાગ 49 mm પર છે. લીસ્ટ કાઉન્ટ શોધો."),
        [P("L.C. = M.S.D./n = 1/50 mm", "L.C. = M.S.D./n = 1/50 mm"),
         P("= 0.02 mm", "= 0.02 mm")],
        T("L.C. = 0.02 mm", "L.C. = 0.02 mm")),
    num("u1n09", T("Vernier reading: M.S.R. 2.3 cm, V.C. 6, L.C. 0.01 cm.",
                   "વર્નિયર વાંચન: M.S.R. 2.3 cm, V.C. 6, L.C. 0.01 cm."),
        T("A vernier caliper shows a main-scale reading of 2.3 cm and the 6th vernier division "
          "coincides. The least count is 0.01 cm. Find the length.",
          "વર્નિયર કેલિપરમાં મુખ્ય સ્કેલનું વાંચન 2.3 cm છે અને 6ઠ્ઠો વર્નિયર વિભાગ મળે છે. લીસ્ટ કાઉન્ટ "
          "0.01 cm છે. લંબાઈ શોધો."),
        [P("Reading = M.S.R. + V.C. × L.C.", "વાંચન = M.S.R. + V.C. × L.C."),
         P("= 2.3 + 6 × 0.01 = 2.3 + 0.06", "= 2.3 + 6 × 0.01 = 2.3 + 0.06"),
         P("= 2.36 cm", "= 2.36 cm")],
        T("2.36 cm", "2.36 cm")),
    num("u1n10", T("Zero error +0.03 cm, observed 2.36 cm.",
                   "શૂન્ય ભૂલ +0.03 cm, વાંચન 2.36 cm."),
        T("The vernier above has a positive zero error of 0.03 cm. Find the true length.",
          "ઉપરના વર્નિયરમાં 0.03 cm ધન શૂન્ય ભૂલ છે. સાચી લંબાઈ શોધો."),
        [P("True value = observed − zero error", "સાચું મૂલ્ય = વાંચન − શૂન્ય ભૂલ"),
         P("= 2.36 − 0.03 = 2.33 cm", "= 2.36 − 0.03 = 2.33 cm")],
        T("2.33 cm", "2.33 cm")),
    num("u1n11", T("Zero error −0.02 cm, observed 5.48 cm.",
                   "શૂન્ય ભૂલ −0.02 cm, વાંચન 5.48 cm."),
        T("A caliper has a negative zero error of 0.02 cm and reads 5.48 cm. Find the true length.",
          "કેલિપરમાં 0.02 cm ઋણ શૂન્ય ભૂલ છે અને વાંચન 5.48 cm છે. સાચી લંબાઈ શોધો."),
        [P("True value = observed + |zero error|", "સાચું મૂલ્ય = વાંચન + |શૂન્ય ભૂલ|"),
         P("= 5.48 + 0.02 = 5.50 cm", "= 5.48 + 0.02 = 5.50 cm")],
        T("5.50 cm", "5.50 cm")),
    num("u1n12", T("Least count of a screw gauge: pitch 0.5 mm, 50 divisions.",
                   "સ્ક્રુ ગેજનું લીસ્ટ કાઉન્ટ: પિચ 0.5 mm, 50 વિભાગ."),
        T("A screw gauge has a pitch of 0.5 mm and 50 circular divisions. Find its least count.",
          "સ્ક્રુ ગેજની પિચ 0.5 mm અને 50 વર્તુળાકાર વિભાગ છે. તેનું લીસ્ટ કાઉન્ટ શોધો."),
        [P("L.C. = pitch / number of divisions", "L.C. = પિચ / વિભાગોની સંખ્યા"),
         P("= 0.5/50 = 0.01 mm", "= 0.5/50 = 0.01 mm")],
        T("L.C. = 0.01 mm", "L.C. = 0.01 mm")),
    num("u1n13", T("Screw-gauge reading: S.S.R. 4.5 mm, C.S.R. 32, L.C. 0.01 mm.",
                   "સ્ક્રુ ગેજ વાંચન: S.S.R. 4.5 mm, C.S.R. 32, L.C. 0.01 mm."),
        T("The sleeve reads 4.5 mm and the thimble shows 32 divisions. The least count is 0.01 mm. "
          "Find the diameter.", "સ્લીવ 4.5 mm વાંચે છે અને થિંબલ 32 વિભાગ દર્શાવે છે. લીસ્ટ કાઉન્ટ 0.01 mm છે. "
          "વ્યાસ શોધો."),
        [P("Reading = S.S.R. + C.S.R. × L.C.", "વાંચન = S.S.R. + C.S.R. × L.C."),
         P("= 4.5 + 32 × 0.01 = 4.5 + 0.32", "= 4.5 + 32 × 0.01 = 4.5 + 0.32"),
         P("= 4.82 mm", "= 4.82 mm")],
        T("4.82 mm", "4.82 mm")),
    num("u1n14", T("Zero error +0.02 mm, reading 4.82 mm.",
                   "શૂન્ય ભૂલ +0.02 mm, વાંચન 4.82 mm."),
        T("The gauge above has a zero error of +0.02 mm. Find the true diameter.",
          "ઉપરના ગેજમાં +0.02 mm શૂન્ય ભૂલ છે. સાચો વ્યાસ શોધો."),
        [P("True diameter = 4.82 − 0.02", "સાચો વ્યાસ = 4.82 − 0.02"),
         P("= 4.80 mm", "= 4.80 mm")],
        T("4.80 mm", "4.80 mm")),
    num("u1n15", T("Percentage error when 9.80 m/s² is measured against 9.81 m/s².",
                   "9.81 m/s² સામે 9.80 m/s² માપતાં ટકાવારી ભૂલ."),
        T("An experiment gives g = 9.80 m/s². The accepted value is 9.81 m/s². Find the absolute, "
          "relative and percentage error.",
          "પ્રયોગમાં g = 9.80 m/s² મળે છે. સ્વીકૃત મૂલ્ય 9.81 m/s² છે. નિરપેક્ષ, સાપેક્ષ અને ટકાવારી ભૂલ શોધો."),
        [P("Absolute error = |9.80 − 9.81| = 0.01 m/s²", "નિરપેક્ષ ભૂલ = |9.80 − 9.81| = 0.01 m/s²"),
         P("Relative error = 0.01/9.81 = 1.02 × 10⁻³", "સાપેક્ષ ભૂલ = 0.01/9.81 = 1.02 × 10⁻³"),
         P("Percentage error = 0.102 % ≈ 0.10 %", "ટકાવારી ભૂલ = 0.102 % ≈ 0.10 %")],
        T("0.01 m/s²; 1.02 × 10⁻³; 0.10 %", "0.01 m/s²; 1.02 × 10⁻³; 0.10 %")),
    num("u1n16", T("Resistance from V = 100 ± 2 V and I = 5.0 ± 0.1 A.",
                   "V = 100 ± 2 V અને I = 5.0 ± 0.1 A પરથી અવરોધ."),
        T("The voltage across a resistor is 100 ± 2 V and the current is 5.0 ± 0.1 A. Find the "
          "resistance with its percentage error.",
          "એક રેઝિસ્ટર પરનો વોલ્ટેજ 100 ± 2 V અને પ્રવાહ 5.0 ± 0.1 A છે. અવરોધ અને તેની ટકાવારી ભૂલ શોધો."),
        [P("R = V/I = 100/5.0 = 20 Ω", "R = V/I = 100/5.0 = 20 Ω"),
         P("ΔV/V = 2/100 = 2 %, ΔI/I = 0.1/5.0 = 2 %", "ΔV/V = 2/100 = 2 %, ΔI/I = 0.1/5.0 = 2 %"),
         P("ΔR/R = 2 % + 2 % = 4 %, so ΔR = 0.04 × 20 = 0.8 Ω", "ΔR/R = 2 % + 2 % = 4 %, તેથી ΔR = 0.04 × 20 = 0.8 Ω"),
         P("R = 20 ± 0.8 Ω", "R = 20 ± 0.8 Ω")],
        T("20 ± 0.8 Ω (4 %)", "20 ± 0.8 Ω (4 %)")),
    num("u1n17", T("Density of a block: m = 250.0 ± 0.5 g, V = 50.0 ± 0.5 cm³.",
                   "બ્લોકની ઘનતા: m = 250.0 ± 0.5 g, V = 50.0 ± 0.5 cm³."),
        T("A metal block has mass 250.0 ± 0.5 g and volume 50.0 ± 0.5 cm³. Find the density and its "
          "percentage error.", "ધાતુના બ્લોકનું દ્રવ્યમાન 250.0 ± 0.5 g અને ઘનફળ 50.0 ± 0.5 cm³ છે. ઘનતા અને "
          "તેની ટકાવારી ભૂલ શોધો."),
        [P("ρ = m/V = 250.0/50.0 = 5.00 g/cm³", "ρ = m/V = 250.0/50.0 = 5.00 g/cm³"),
         P("Δm/m = 0.5/250 = 0.2 %, ΔV/V = 0.5/50 = 1.0 %", "Δm/m = 0.5/250 = 0.2 %, ΔV/V = 0.5/50 = 1.0 %"),
         P("Δρ/ρ = 1.2 %, so Δρ = 0.012 × 5.00 = 0.06 g/cm³", "Δρ/ρ = 1.2 %, તેથી Δρ = 0.012 × 5.00 = 0.06 g/cm³"),
         P("ρ = 5.00 ± 0.06 g/cm³", "ρ = 5.00 ± 0.06 g/cm³")],
        T("5.00 ± 0.06 g/cm³", "5.00 ± 0.06 g/cm³")),
    num("u1n18", T("Area of a circle with r = 2.0 ± 0.1 cm.",
                   "r = 2.0 ± 0.1 cm હોય તેવા વર્તુળનું ક્ષેત્રફળ."),
        T("The radius of a disc is 2.0 ± 0.1 cm. Find its area with the percentage error.",
          "એક ડિસ્કની ત્રિજ્યા 2.0 ± 0.1 cm છે. તેનું ક્ષેત્રફળ ટકાવારી ભૂલ સાથે શોધો."),
        [P("A = πr² = π(2.0)² = 12.6 cm² (3 s.f.: 12.6)", "A = πr² = π(2.0)² = 12.6 cm²"),
         P("Δr/r = 0.1/2.0 = 5 %, and A depends on r²", "Δr/r = 0.1/2.0 = 5 %, અને A એ r² પર આધારિત છે"),
         P("ΔA/A = 2 × 5 % = 10 %, so ΔA = 1.26 ≈ 1.3 cm²", "ΔA/A = 2 × 5 % = 10 %, તેથી ΔA = 1.26 ≈ 1.3 cm²"),
         P("A = 12.6 ± 1.3 cm²", "A = 12.6 ± 1.3 cm²")],
        T("12.6 ± 1.3 cm² (10 %)", "12.6 ± 1.3 cm² (10 %)")),
    num("u1n19", T("Significant figures: 2.5 × 1.25 and 12.11 + 18.0 + 1.013.",
                   "સાર્થક અંકો: 2.5 × 1.25 અને 12.11 + 18.0 + 1.013."),
        T("Work out 2.5 × 1.25 and 12.11 + 18.0 + 1.013, keeping the correct number of significant "
          "figures.", "2.5 × 1.25 અને 12.11 + 18.0 + 1.013 યોગ્ય સાર્થક અંકો રાખીને ગણો."),
        [P("2.5 × 1.25 = 3.125. The smallest input has 2 s.f., so the answer is 3.1.",
           "2.5 × 1.25 = 3.125. સૌથી ઓછા સાર્થક અંક 2 છે, તેથી જવાબ 3.1."),
         P("12.11 + 18.0 + 1.013 = 31.123. The smallest number of decimal places is 1, so the answer "
           "is 31.1.", "12.11 + 18.0 + 1.013 = 31.123. સૌથી ઓછા દશાંશ સ્થાન 1 છે, તેથી જવાબ 31.1.")],
        T("3.1 and 31.1", "3.1 અને 31.1")),
    num("u1n20", T("Volume of a sphere of radius 1.20 cm.",
                   "1.20 cm ત્રિજ્યાવાળા ગોળાનું ઘનફળ."),
        T("Find the volume of a steel ball of radius 1.20 cm, with the correct significant figures.",
          "1.20 cm ત્રિજ્યાવાળા સ્ટીલના દડાનું ઘનફળ યોગ્ય સાર્થક અંકો સાથે શોધો."),
        [P("V = (4/3)πr³ = (4/3)π(1.20)³", "V = (4/3)πr³ = (4/3)π(1.20)³"),
         P("(1.20)³ = 1.728, so V = 4.1888 × 1.728 = 7.2378 cm³",
           "(1.20)³ = 1.728, તેથી V = 4.1888 × 1.728 = 7.2378 cm³"),
         P("r has 3 s.f., so V = 7.24 cm³.", "rમાં 3 સાર્થક અંક છે, તેથી V = 7.24 cm³.")],
        T("7.24 cm³", "7.24 cm³")),
]

EQUATIONS = [
    {"title": T("Units and conversion", "એકમો અને રૂપાંતરણ"),
     "items": [
         {"name": T("Metre into centimetre", "મીટરથી સેન્ટિમીટર"),
          "f": "1 m = 100 cm;  1 kg = 1000 g", "terms": T("Multiply when going to a smaller unit.",
                                                         "નાના એકમમાં જતી વખતે ગુણાકાર કરો.")},
         {"name": T("Newton into dyne", "ન્યૂટનથી ડાઇન"),
          "f": "1 N = 10⁵ dyne", "terms": T("kg·m/s² into g·cm/s².", "kg·m/s² થી g·cm/s².")},
         {"name": T("Joule into erg", "જૂલથી અર્ગ"),
          "f": "1 J = 10⁷ erg", "terms": T("N·m into dyne·cm.", "N·m થી ડાઇન·cm.")},
         {"name": T("Watt into erg per second", "વોટથી અર્ગ પ્રતિ સેકન્ડ"),
          "f": "1 W = 10⁷ erg/s", "terms": T("Power keeps the same factor of 10⁷.",
                                            "શક્તિમાં પણ 10⁷ નો જ અવયવ રહે.")},
         {"name": T("Pascal into dyne per cm²", "પાસ્કલથી ડાઇન પ્રતિ cm²"),
          "f": "1 Pa = 10 dyne/cm²", "terms": T("Pressure is force divided by area, so both factors count.",
                                                "દબાણ = બળ/ક્ષેત્રફળ, તેથી બંને અવયવ ગણાય.")},
         {"name": T("Density", "ઘનતા"),
          "f": "1 g/cm³ = 1000 kg/m³", "terms": T("The most common slip in workshop calculations.",
                                                 "કાર્યશાળાની ગણતરીમાં સૌથી સામાન્ય ભૂલ.")},
     ]},
    {"title": T("Instruments and errors", "સાધનો અને ભૂલો"),
     "items": [
         {"name": T("Vernier least count", "વર્નિયર લીસ્ટ કાઉન્ટ"),
          "f": "L.C. = 1 M.S.D. − 1 V.S.D. = M.S.D./n",
          "terms": T("n vernier divisions cover n − 1 main divisions.",
                     "n વર્નિયર વિભાગ n − 1 મુખ્ય વિભાગ આવરે છે.")},
         {"name": T("Vernier reading", "વર્નિયર વાંચન"),
          "f": "reading = M.S.R. + V.C. × L.C. − zero error",
          "terms": T("Subtract a positive zero error, add a negative one.",
                     "ધન શૂન્ય ભૂલ બાદ કરો, ઋણ ઉમેરો.")},
         {"name": T("Screw-gauge least count", "સ્ક્રુ ગેજ લીસ્ટ કાઉન્ટ"),
          "f": "L.C. = pitch / circular divisions",
          "terms": T("0.5 mm pitch over 50 divisions gives 0.01 mm.",
                     "0.5 mm પિચ 50 વિભાગ પર એટલે 0.01 mm.")},
         {"name": T("Screw-gauge reading", "સ્ક્રુ ગેજ વાંચન"),
          "f": "reading = S.S.R. + C.S.R. × L.C. − zero error",
          "terms": T("Sleeve first, thimble second.", "પહેલાં સ્લીવ, પછી થિંબલ.")},
         {"name": T("Percentage error", "ટકાવારી ભૂલ"),
          "f": "(Δa / a) × 100 %",
          "terms": T("Δa is the absolute error, taken positive.",
                     "Δa નિરપેક્ષ ભૂલ છે, હંમેશા ધન.")},
         {"name": T("Errors in a product or quotient", "ગુણાકાર કે ભાગાકારની ભૂલ"),
          "f": "ΔZ/Z = ΔA/A + ΔB/B",
          "terms": T("Relative errors add; they never cancel.",
                     "સાપેક્ષ ભૂલો ઉમેરાય છે; ક્યારેય રદ થતી નથી.")},
         {"name": T("Error in a power", "ઘાતમાં ભૂલ"),
          "f": "Z = Aⁿ → ΔZ/Z = n (ΔA/A)",
          "terms": T("The power multiplies the relative error.",
                     "ઘાત સાપેક્ષ ભૂલને ગુણે છે.")},
     ]},
]

VIVA = [
    {"title": T("Definitions", "વ્યાખ્યાઓ"),
     "items": [
         {"q": T("What is a physical quantity?", "ભૌતિક રાશિ એટલે શું?"),
          "a": T("A quantity that can be measured and expressed as a number with a unit, such as "
                 "length, mass or time.",
                 "જેને માપી શકાય અને સંખ્યા તથા એકમ સાથે દર્શાવી શકાય તેવી રાશિ, જેમ કે લંબાઈ, દ્રવ્યમાન કે સમય.")},
         {"q": T("Name the seven SI base quantities.", "SIની સાત પાયાની રાશિઓ જણાવો."),
          "a": T("Length, mass, time, electric current, temperature, amount of substance and "
                 "luminous intensity.",
                 "લંબાઈ, દ્રવ્યમાન, સમય, વિદ્યુત પ્રવાહ, તાપમાન, પદાર્થનો જથ્થો અને પ્રકાશીય તીવ્રતા.")},
         {"q": T("Give two derived quantities with their units.",
                 "બે વ્યુત્પન્ન રાશિઓ તેમના એકમ સાથે જણાવો."),
          "a": T("Force (newton = kg·m/s²) and pressure (pascal = N/m²).",
                 "બળ (ન્યૂટન = kg·m/s²) અને દબાણ (પાસ્કલ = N/m²).")},
         {"q": T("What is the least count of an instrument?",
                 "સાધનનું લીસ્ટ કાઉન્ટ એટલે શું?"),
          "a": T("The smallest measurement the instrument can read reliably.",
                 "સાધન વિશ્વસનીય રીતે વાંચી શકે તેવું સૌથી નાનું માપ.")},
         {"q": T("State the formula for vernier least count.",
                 "વર્નિયર લીસ્ટ કાઉન્ટનું સૂત્ર જણાવો."),
          "a": T("L.C. = 1 M.S.D. − 1 V.S.D., which equals M.S.D./n when n vernier divisions cover "
                 "n − 1 main divisions. A 50-division vernier on a millimetre scale reads 0.02 mm.",
                 "L.C. = 1 M.S.D. − 1 V.S.D., જે n વર્નિયર વિભાગ n − 1 મુખ્ય વિભાગ આવરે ત્યારે M.S.D./n "
                 "થાય. મિલીમીટર સ્કેલ પર 50 વિભાગવાળું વર્નિયર 0.02 mm વાંચે છે.")},
         {"q": T("State the formula for screw-gauge least count.",
                 "સ્ક્રુ ગેજ લીસ્ટ કાઉન્ટનું સૂત્ર જણાવો."),
          "a": T("L.C. = pitch / number of circular-scale divisions.",
                 "L.C. = પિચ / વર્તુળાકાર સ્કેલના વિભાગોની સંખ્યા.")},
     ]},
    {"title": T("Accuracy, errors and significant figures", "ચોકસાઈ, ભૂલો અને સાર્થક અંકો"),
     "items": [
         {"q": T("Difference between accuracy and precision?",
                 "ચોકસાઈ અને પરિશુદ્ધતામાં શું ફરક?"),
          "a": T("Accuracy is closeness to the true value; precision is closeness of repeated "
                 "readings to one another.",
                 "ચોકસાઈ સાચા મૂલ્યની નજીકતા છે; પરિશુદ્ધતા વારંવાર લીધેલાં વાંચનની એકબીજાની નજીકતા છે.")},
         {"q": T("Name three types of error.", "ભૂલના ત્રણ પ્રકાર જણાવો."),
          "a": T("Systematic, random and gross errors. Systematic errors keep one sign (a zero error), "
                 "random errors scatter both ways (unsteady hands), and gross errors are plain "
                 "misreadings or wrong units.",
                 "ક્રમબદ્ધ, યાદૃચ્છિક અને ઘોર ભૂલો. ક્રમબદ્ધ ભૂલનું ચિહ્ન એક જ રહે (શૂન્ય ભૂલ), યાદૃચ્છિક "
                 "ભૂલ બંને બાજુ વિખરાય (ઢીલા હાથ) અને ઘોર ભૂલ એટલે સીધું ખોટું વાંચન કે ખોટું એકમ.")},
         {"q": T("Give one example of a systematic error and its cure.",
                 "ક્રમબદ્ધ ભૂલનું એક ઉદાહરણ અને તેનો ઉપાય જણાવો."),
          "a": T("A zero error of +0.03 cm in a vernier; the cure is to measure it and subtract it "
                 "from every reading.",
                 "વર્નિયરમાં +0.03 cm શૂન્ય ભૂલ; ઉપાય એ છે કે તેને માપી દરેક વાંચનમાંથી બાદ કરવી.")},
         {"q": T("Write the formula for percentage error.",
                 "ટકાવારી ભૂલનું સૂત્ર લખો."),
          "a": T("Percentage error = (|measured − true| / true) × 100 %.",
                 "ટકાવારી ભૂલ = (|માપેલ − સાચું| / સાચું) × 100 %.")},
         {"q": T("How many significant figures are in 0.00250 m?",
                 "0.00250 m માં કેટલા સાર્થક અંક છે?"),
          "a": T("Three: 2, 5 and the trailing 0 after the decimal. The leading zeros of 0.00250 do "
                 "not count, and writing 0.0025 would drop one significant figure.",
                 "ત્રણ: 2, 5 અને દશાંશ પછીનો અંતિમ 0. 0.00250માં શરૂઆતના શૂન્ય ગણાય નહીં, અને 0.0025 લખવાથી "
                 "એક સાર્થક અંક ખોવાઈ જાય.")},
         {"q": T("Why must a measurement carry a unit?",
                 "માપન સાથે એકમ કેમ જરૂરી છે?"),
          "a": T("Without a unit the number has no meaning: 25 could be 25 mm, 25 cm or 25 µm.",
                 "એકમ વગર સંખ્યાનો અર્થ નથી: 25 એ 25 mm, 25 cm કે 25 µm હોઈ શકે.")},
         {"q": T("What is a zero error, and how is it corrected?",
                 "શૂન્ય ભૂલ શું છે અને તે કેવી રીતે સુધારાય?"),
          "a": T("The reading when the jaws or anvil are closed; subtract it if positive, add it if "
                 "negative.",
                 "જડબાં કે એન્વિલ બંધ હોય ત્યારે મળતું વાંચન; ધન હોય તો બાદ કરો, ઋણ હોય તો ઉમેરો.")},
     ]},
]

_PRACTICE = [
    (T("Define physical quantity. Distinguish between fundamental and derived quantities with two "
       "examples of each.",
       "ભૌતિક રાશિની વ્યાખ્યા આપો. પાયાની અને વ્યુત્પન્ન રાશિઓ વચ્ચેનો ભેદ દરેકના બે ઉદાહરણ સાથે સમજાવો."),
     4,
     [P("A <b>physical quantity</b> is anything that can be measured and expressed as a number with a "
        "unit, for example 25 mm, 2.5 kg or 10 s.",
        "<b>ભૌતિક રાશિ</b> એટલે જેને માપી શકાય અને સંખ્યા તથા એકમ સાથે દર્શાવી શકાય, જેમ કે 25 mm, 2.5 kg "
        "કે 10 s."),
      P("<b>Fundamental quantities</b> are independent: length, mass, time, electric current, "
        "temperature, amount of substance and luminous intensity.",
        "<b>પાયાની રાશિઓ</b> સ્વતંત્ર છે: લંબાઈ, દ્રવ્યમાન, સમય, વિદ્યુત પ્રવાહ, તાપમાન, પદાર્થનો જથ્થો અને "
        "પ્રકાશીય તીવ્રતા."),
      P("<b>Derived quantities</b> are built from fundamental ones: velocity = length/time (m/s) and "
        "force = mass × acceleration (N = kg·m/s²).",
        "<b>વ્યુત્પન્ન રાશિઓ</b> પાયાની રાશિઓમાંથી બને છે: વેગ = લંબાઈ/સમય (m/s) અને બળ = દ્રવ્યમાન × પ્રવર્ગ "
        "(N = kg·m/s²).")]),
    (T("Explain the construction and working of a vernier caliper with its least-count formula.",
       "વર્નિયર કેલિપરની રચના અને કાર્યપદ્ધતિ તેના લીસ્ટ કાઉન્ટ સૂત્ર સાથે સમજાવો."),
     5,
     [P("A vernier caliper has a steel main scale graduated in mm, a sliding vernier scale, two jaws "
        "for outside measurement, two for inside measurement and a depth rod.",
        "વર્નિયર કેલિપરમાં mmમાં મુખ્ય સ્કેલ, સરકતો વર્નિયર સ્કેલ, બહારના માપ માટે બે જડબાં, આંતરિક માપ માટે "
        "બે જડબાં અને ઊંડાઈનો સળિયો હોય છે."),
      P("Its principle is that <i>n</i> vernier divisions cover <i>n − 1</i> main divisions, so one "
        "vernier division is shorter than one main division by M.S.D./n; that difference is the least "
        "count, L.C. = 1 M.S.D. − 1 V.S.D. = M.S.D./n.",
        "તેનો સિદ્ધાંત એ છે કે <i>n</i> વર્નિયર વિભાગ <i>n − 1</i> મુખ્ય વિભાગ આવરે છે, તેથી એક વર્નિયર "
        "વિભાગ એક મુખ્ય વિભાગ કરતાં M.S.D./n જેટલો નાનો હોય છે; એ તફાવત જ લીસ્ટ કાઉન્ટ છે, "
        "L.C. = 1 M.S.D. − 1 V.S.D. = M.S.D./n."),
      P("Reading = M.S.R. + V.C. × L.C., with the zero error subtracted if it is positive. For example "
        "M.S.R. 2.3 cm, V.C. 6 and L.C. 0.01 cm give 2.36 cm.",
        "વાંચન = M.S.R. + V.C. × L.C., શૂન્ય ભૂલ ધન હોય તો બાદ કરવી. દા.ત. M.S.R. 2.3 cm, V.C. 6 અને "
        "L.C. 0.01 cm માટે 2.36 cm મળે.")]),
    (T("Distinguish between accuracy and precision with an example.",
       "ચોકસાઈ અને પરિશુદ્ધતા વચ્ચેનો ભેદ ઉદાહરણ સાથે સમજાવો."),
     3,
     [P("<b>Accuracy</b> is how close a measurement is to the true value; <b>precision</b> is how "
        "close repeated measurements are to each other.",
        "<b>ચોકસાઈ</b> એ માપન સાચા મૂલ્યની કેટલું નજીક છે તે દર્શાવે; <b>પરિશુદ્ધતા</b> એ વારંવાર લીધેલાં "
        "માપન એકબીજાની કેટલાં નજીક છે તે દર્શાવે."),
      P("Example: a balance reads 50.02 g, 50.02 g and 50.02 g for a 49.90 g standard. The readings "
        "agree with each other (precise) but miss the true value (inaccurate).",
        "ઉદાહરણ: 49.90 g માનક માટે બેલેન્સ 50.02 g, 50.02 g અને 50.02 g વાંચે છે. વાંચન એકબીજા સાથે મળે "
        "છે (પરિશુદ્ધ) પણ સાચા મૂલ્યથી દૂર છે (અચોકસ)."),
      P("Calibration improves accuracy; careful technique improves precision. A good measurement needs "
        "both.",
        "કેલિબ્રેશન ચોકસાઈ સુધારે છે; કાળજીપૂર્વકની પદ્ધતિ પરિશુદ્ધતા સુધારે છે. સારા માપન માટે બંને જરૂરી છે.")]),
    (T("Explain absolute, relative and percentage error with a worked example.",
       "નિરપેક્ષ, સાપેક્ષ અને ટકાવારી ભૂલ ઉકેલાયેલ દાખલા સાથે સમજાવો."),
     4,
     [P("Absolute error Δa = |measured − true| and carries the unit of the quantity. Relative error "
        "= Δa/a has no unit; percentage error = (Δa/a) × 100 %.",
        "નિરપેક્ષ ભૂલ Δa = |માપેલ − સાચું| અને તે રાશિનું એકમ ધરાવે. સાપેક્ષ ભૂલ = Δa/a ને એકમ નથી; "
        "ટકાવારી ભૂલ = (Δa/a) × 100 %."),
      P("Worked example: a length measures 24.8 cm against 25.0 cm. Δa = 0.2 cm, relative error = "
        "0.2/25.0 = 0.008 and percentage error = 0.8 %.",
        "ઉકેલાયેલ દાખલો: લંબાઈ 24.8 cm મળે છે જ્યારે સાચું મૂલ્ય 25.0 cm છે. Δa = 0.2 cm, સાપેક્ષ ભૂલ = "
        "0.2/25.0 = 0.008 અને ટકાવારી ભૂલ = 0.8 %."),
      P("In a product or quotient the relative errors add: for R = V/I, ΔR/R = ΔV/V + ΔI/I.",
        "ગુણાકાર કે ભાગાકારમાં સાપેક્ષ ભૂલો ઉમેરાય છે: R = V/I માટે ΔR/R = ΔV/V + ΔI/I.")]),
    (T("State the rules for rounding off and for counting significant figures.",
       "રાઉન્ડિંગ ઓફ અને સાર્થક અંકો ગણવાના નિયમો જણાવો."),
     4,
     [P("Rounding: if the digit dropped is more than 5, increase the last kept digit by 1; if it is "
        "less than 5, leave it; if it is exactly 5, make the last kept digit even.",
        "રાઉન્ડિંગ: કાઢવાનો અંક 5થી મોટો હોય તો છેલ્લા અંકમાં 1 ઉમેરો; 5થી નાનો હોય તો તેમ રાખો; બરાબર 5 "
        "હોય તો છેલ્લા અંકને યુગ્મ બનાવો."),
      P("Significant figures: all non-zero digits count, zeros between them count, leading zeros do "
        "not, trailing zeros after a decimal do. So 0.00250 has three and 2.500 has four.",
        "સાર્થક અંકો: બધા શૂન્યેતર અંક ગણાય, વચ્ચેના શૂન્ય ગણાય, શરૂઆતના શૂન્ય ગણાય નહીં, દશાંશ પછીના "
        "અંતિમ શૂન્ય ગણાય. તેથી 0.00250માં ત્રણ અને 2.500માં ચાર."),
      P("In calculations, multiplication and division keep the smallest number of significant "
        "figures, while addition and subtraction keep the smallest number of decimal places.",
        "ગણતરીમાં ગુણાકાર અને ભાગાકારમાં સૌથી ઓછા સાર્થક અંક રાખવા, જ્યારે સરવાળા અને તફાવતમાં સૌથી ઓછા "
        "દશાંશ સ્થાન રાખવાં.")]),
    (T("Convert 1 N into dyne and 1 J into erg, showing every step.",
       "1 N ને ડાઇનમાં અને 1 J ને અર્ગમાં દરેક પગલું દર્શાવીને ફેરવો."),
     3,
     [P("1 N = 1 kg × 1 m/s² = 1000 g × 100 cm/s² = 10⁵ g·cm/s² = 10⁵ dyne.",
        "1 N = 1 kg × 1 m/s² = 1000 g × 100 cm/s² = 10⁵ g·cm/s² = 10⁵ ડાઇન."),
      P("1 J = 1 N × 1 m = 10⁵ dyne × 100 cm = 10⁷ dyne·cm = 10⁷ erg.",
        "1 J = 1 N × 1 m = 10⁵ ડાઇન × 100 cm = 10⁷ ડાઇન·cm = 10⁷ અર્ગ."),
      P("The rule is to replace every MKS unit by its CGS equivalent and then multiply the numbers. "
        "Because force carries L and M, both factors of 100 and 1000 enter, which is why the answer is "
        "10⁵ and not 10³.",
        "નિયમ એ છે કે દરેક MKS એકમને CGS સમાન મૂલ્યથી બદલીને પછી સંખ્યાઓનો ગુણાકાર કરવો. બળમાં L અને M "
        "બંને આવે છે, તેથી 100 અને 1000 એમ બંને અવયવ ગણાય, અને તેથી જ જવાબ 10³ નહીં પણ 10⁵ આવે."),
      P("Write the unit at every step: 1 N = 10⁵ dyne and 1 J = 10⁷ erg are worth memorising, but an "
        "exam answer needs the substitution that produces them.",
        "દરેક પગલે એકમ લખો: 1 N = 10⁵ ડાઇન અને 1 J = 10⁷ અર્ગ યાદ રાખવા જેવા છે, પણ પરીક્ષાના જવાબમાં તે "
        "ઉત્પન્ન કરતું આંકડા મૂકવાનું જરૂરી છે.")]),
    (T("A vernier caliper reads M.S.R. 15 mm, V.C. 4 and has L.C. 0.1 mm. Find the length.",
       "વર્નિયર કેલિપર M.S.R. 15 mm, V.C. 4 વાંચે છે અને L.C. 0.1 mm છે. લંબાઈ શોધો."),
     3,
     [P("Reading = M.S.R. + V.C. × L.C. = 15 + 4 × 0.1", "વાંચન = M.S.R. + V.C. × L.C. = 15 + 4 × 0.1"),
      P("= 15 + 0.4 = 15.4 mm", "= 15 + 0.4 = 15.4 mm"),
      P("If the instrument had a zero error of +0.1 mm, the true length would be 15.3 mm.",
        "જો સાધનમાં +0.1 mm શૂન્ય ભૂલ હોય તો સાચી લંબાઈ 15.3 mm થાય."),
      P("The reading is written 15.4 ± 0.1 mm. The uncertainty is the least count, because no "
        "reading taken with this instrument can be trusted beyond one tenth of a millimetre.",
        "વાંચન 15.4 ± 0.1 mm લખાય. અનિશ્ચિતતા લીસ્ટ કાઉન્ટ જેટલી છે, કારણ કે આ સાધનથી લીધેલું કોઈ પણ "
        "વાંચન એક મિલીમીટરના દશમા ભાગથી વધુ ભરોસાપાત્ર નથી.")]),
    (T("A screw gauge has pitch 0.5 mm and 100 divisions. Find its least count and read S.S.R. 3.0 mm "
       "with C.S.R. 45.", "સ્ક્રુ ગેજની પિચ 0.5 mm અને 100 વિભાગ છે. લીસ્ટ કાઉન્ટ શોધો અને S.S.R. 3.0 mm "
       "તથા C.S.R. 45 વાંચન શોધો."),
     4,
     [P("L.C. = pitch/divisions = 0.5/100 = 0.005 mm", "L.C. = પિચ/વિભાગ = 0.5/100 = 0.005 mm"),
      P("Reading = 3.0 + 45 × 0.005 = 3.0 + 0.225 = 3.225 mm", "વાંચન = 3.0 + 45 × 0.005 = 3.0 + 0.225 = 3.225 mm"),
      P("With three decimal places the answer is written 3.225 ± 0.005 mm. Do not round it to "
        "3.23 mm: that would throw away the very resolution the 100-division thimble was bought for.",
        "ત્રણ દશાંશ સ્થાન સાથે જવાબ 3.225 ± 0.005 mm લખાય. તેને 3.23 mm સુધી રાઉન્ડ ન કરો: એમ કરવાથી "
        "100 વિભાગવાળા થિંબલની જે ઝીણવટ માટે ખરીદી કરી હતી તે જ ખોવાઈ જાય."),
      P("A coarser gauge of pitch 0.5 mm and 50 divisions would have given the same reading as "
        "3.21 mm or 3.24 mm, so the choice of instrument decides the answer.",
        "0.5 mm પિચ અને 50 વિભાગવાળું જાડું ગેજ એ જ વાંચન 3.21 mm કે 3.24 mm તરીકે આપત, તેથી સાધનની "
        "પસંદગી જ જવાબ નક્કી કરે છે.")]),
    (T("Explain why the least count of the instrument must suit the tolerance.",
       "સાધનનું લીસ્ટ કાઉન્ટ ટોલરન્સને અનુરૂપ કેમ હોવું જોઈએ તે સમજાવો."),
     3,
     [P("If the least count is coarser than the tolerance, two different readings can fall inside "
        "the same scale division, so a good part may be rejected or a bad one accepted.",
        "જો લીસ્ટ કાઉન્ટ ટોલરન્સ કરતાં જાડું હોય તો બે જુદાં વાંચન એક જ વિભાગમાં આવી શકે, તેથી સારો પાર્ટ "
        "રિજેક્ટ થાય કે ખરાબ પાર્ટ પાસ થાય."),
      P("The rule of thumb is that the least count should be about one tenth of the tolerance: for "
        "±0.02 mm use a gauge reading 0.002 mm or better; a 0.01 mm screw gauge is the practical choice.",
        "સામાન્ય નિયમ એ છે કે લીસ્ટ કાઉન્ટ ટોલરન્સના લગભગ દશમા ભાગનું હોવું જોઈએ: ±0.02 mm માટે 0.002 mm "
        "કે તેથી સારું વાંચતું ગેજ વાપરો; 0.01 mm સ્ક્રુ ગેજ વ્યવહારુ પસંદગી છે."),
      P("Cost is the other side: a 0.001 mm instrument costs several times more, so it is used only "
        "where the drawing demands it.",
        "બીજી બાજુ ખર્ચ છે: 0.001 mm સાધન ઘણા ગણું મોંઘું છે, તેથી તે ફક્ત ત્યાં વપરાય જ્યાં ડ્રોઇંગ માંગે.")]),
    (T("Name four errors that spoil a measurement even when the instrument is good, with one cure "
       "each.", "સાધન સારું હોવા છતાં માપન બગાડતી ચાર ભૂલો તેમના એક-એક ઉપાય સાથે જણાવો."),
     4,
     [P("<b>Parallax:</b> the eye is not square to the scale, so the pointer appears shifted; cure - "
        "view straight on or use the mirror behind the pointer.",
        "<b>પેરાલેક્સ:</b> આંખ સ્કેલને લંબ ન હોવાથી દર્શક સરકેલો દેખાય; ઉપાય - સીધું જુઓ કે દર્શક પાછળનો "
        "અરીસો વાપરો."),
      P("<b>Zero error:</b> jaws do not close at 0.00; cure - measure the zero error and correct every "
        "reading. <b>Temperature:</b> a hot part is larger; cure - allow it to cool to 20 °C.",
        "<b>શૂન્ય ભૂલ:</b> જડબાં 0.00 પર બંધ ન થાય; ઉપાય - શૂન્ય ભૂલ માપી દરેક વાંચન સુધારો. "
        "<b>તાપમાન:</b> ગરમ પાર્ટ મોટો હોય; ઉપાય - 20 °C સુધી ઠંડો કરો."),
      P("<b>Excess pressure:</b> the spindle or jaws are forced and the part reads small; cure - use "
        "the ratchet and a light touch.",
        "<b>વધુ દબાણ:</b> સ્પિન્ડલ કે જડબાં પર જોર પડે તો માપ ઓછું આવે; ઉપાય - રેચિટ અને હળવો સ્પર્શ વાપરો.")]),
    (T("Why is dimensional analysis useful, and what can it not prove?",
       "પરિમાણીય વિશ્લેષણ કેમ ઉપયોગી છે અને તે શું સાબિત કરી શકતું નથી?"),
     3,
     [P("It is a quick check: both sides of a correct equation must have the same dimensions, so a "
        "wrong formula is caught before any numbers are put in.",
        "તે ઝડપી ચકાસણી છે: સાચા સમીકરણની બંને બાજુનાં પરિમાણ સમાન હોવાં જોઈએ, તેથી આંકડા મૂકતાં પહેલાં જ "
        "ખોટું સૂત્ર પકડાઈ જાય."),
      P("It cannot prove an equation, because a missing numerical factor passes the test: s = ut + "
        "½at² and s = ut + at² are both dimensionally correct.",
        "તે સમીકરણ સાબિત કરી શકતું નથી, કારણ કે ખોવાયેલો આંકડાકીય અવયવ ચકાસણી પાસ કરી જાય: s = ut + ½at² "
        "અને s = ut + at² બંને પરિમાણીય રીતે સાચાં છે."),
      P("It also cannot check equations that contain trigonometric, exponential or logarithmic "
        "functions, since those quantities are dimensionless.",
        "તે ત્રિકોણમિતીય, ઘાતાંકીય કે લઘુગણકીય વિધેયોવાળાં સમીકરણો પણ ચકાસી શકતું નથી, કારણ કે તે રાશિઓ "
        "પરિમાણરહિત હોય છે.")]),
    (T("A student records a length as 25.0437 mm from a vernier of least count 0.02 mm. Comment.",
       "વિદ્યાર્થી 0.02 mm લીસ્ટ કાઉન્ટવાળા વર્નિયરથી લંબાઈ 25.0437 mm નોંધે છે. ટીકા કરો."),
     3,
     [P("The recording claims an accuracy of 0.0001 mm, which a 0.02 mm instrument cannot give. The "
        "extra digits are not measurements; they are calculator output.",
        "નોંધ 0.0001 mm ની ચોકસાઈ દર્શાવે છે, જે 0.02 mm સાધન આપી શકતું નથી. વધારાના અંક માપન નથી; તે "
        "કેલ્ક્યુલેટરનું પરિણામ છે."),
      P("The correct record is 25.04 ± 0.02 mm, which states the value, the unit and the uncertainty.",
        "સાચી નોંધ 25.04 ± 0.02 mm છે, જે મૂલ્ય, એકમ અને અનિશ્ચિતતા દર્શાવે છે."),
      P("Marks are lost for extra digits in the practical exam, because they show the instrument was "
        "not understood.",
        "પ્રેક્ટિકલ પરીક્ષામાં વધારાના અંકો માટે માર્ક્સ જાય છે, કારણ કે તે દર્શાવે છે કે સાધન સમજાયું નથી.")]),
    (T("Convert 5 km into cm and 3 hours into seconds, showing the method.",
       "5 km ને cm માં અને 3 કલાકને સેકન્ડમાં ફેરવો, રીત દર્શાવો."),
     3,
     [P("5 km = 5 × 1000 m = 5000 m = 5000 × 100 cm = 5 × 10⁵ cm.",
        "5 km = 5 × 1000 m = 5000 m = 5000 × 100 cm = 5 × 10⁵ cm."),
      P("3 h = 3 × 60 min = 180 min = 180 × 60 s = 10 800 s.", "3 કલાક = 3 × 60 મિનિટ = 180 મિનિટ = "
        "180 × 60 સેકન્ડ = 10 800 સેકન્ડ."),
      P("Keep the units with the numbers at every step; that is what stops a factor of 100 or 60 from "
        "going missing.",
        "દરેક પગલે સંખ્યા સાથે એકમ રાખો; તેથી જ 100 કે 60 નો અવયવ ખોવાતો નથી."),
      P("The same chain works backwards: 5 × 10⁵ cm ÷ 100 gives 5000 m, and ÷ 1000 gives 5 km. A "
        "conversion is only finished when the old unit has disappeared.",
        "એ જ સાંકળ ઊંધી દિશામાં પણ ચાલે: 5 × 10⁵ cm ÷ 100 એટલે 5000 m, અને ÷ 1000 એટલે 5 km. રૂપાંતરણ ત્યારે "
        "જ પૂરું ગણાય જ્યારે જૂનું એકમ રહે જ નહીં.")]),
    (T("Define least count and state the least count of the vernier and the screw gauge used in your "
       "laboratory.", "લીસ્ટ કાઉન્ટની વ્યાખ્યા આપો અને તમારી પ્રયોગશાળાના વર્નિયર તથા સ્ક્રુ ગેજનું લીસ્ટ "
       "કાઉન્ટ જણાવો."),
     3,
     [P("The <b>least count</b> is the smallest measurement an instrument can read. For a vernier it "
        "is M.S.D./n, and for a screw gauge it is pitch/divisions.",
        "<b>લીસ્ટ કાઉન્ટ</b> એ સાધન વાંચી શકે તેવું સૌથી નાનું માપ છે. વર્નિયર માટે તે M.S.D./n અને સ્ક્રુ "
        "ગેજ માટે પિચ/વિભાગ છે."),
      P("The usual laboratory vernier (50 divisions over 49 mm) has L.C. 0.02 mm, and the usual "
        "screw gauge (pitch 0.5 mm, 50 divisions) has L.C. 0.01 mm.",
        "સામાન્ય પ્રયોગશાળાના વર્નિયર (49 mm પર 50 વિભાગ)નું L.C. 0.02 mm અને સામાન્ય સ્ક્રુ ગેજ "
        "(પિચ 0.5 mm, 50 વિભાગ)નું L.C. 0.01 mm હોય છે."),
      P("A smaller least count means a finer reading, which is why the gauge is used for wire "
        "diameters and the caliper for plate thickness.",
        "નાનું લીસ્ટ કાઉન્ટ એટલે ઝીણું વાંચન, તેથી તારના વ્યાસ માટે ગેજ અને પ્લેટની જાડાઈ માટે કેલિપર વપરાય.")]),
]

EXAM = [{"q": q, "marks": m} for q, m, _parts in _PRACTICE]
PRACTICE_ANSWERS = [_join(parts) for _q, _m, parts in _PRACTICE]

LESSON_COUNT = sum(len(s["items"]) for s in NOTES)
