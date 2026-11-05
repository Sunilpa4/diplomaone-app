"""DI01000181 Unit 5, part C: oils and lubricants."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from subject_DI01000181 import tr  # noqa: E402
from content_DI01000181_lib import (p, h4, table, math, eq, why, check, pit, card,  # noqa: E402
                                    ul, ol)

NOTES_C = []

NOTES_C.append({
    "title": tr("5.3 Oils and lubricants", "5.3 Oils અને lubricants"),
    "items": [
        card(
            "What an oil does, and the four numbers that describe it",
            "તેલ શું કરે, અને તેને વર્ણવતા ચાર આંકડા",
            p("An oil does four jobs at once: it separates the surfaces so that metal never touches "
              "metal, it carries heat away, it carries dirt to the filter, and it keeps oxygen and "
              "water off the metal. The property that does the first job is <b>viscosity</b>, and it "
              "is the hardest one to hold, because an oil that is 68 cSt at 40 C is about 10 cSt at "
              "100 C and 300 cSt at 30 C - the same oil, one fluid, a thirty-fold change. The "
              "<b>viscosity index</b> measures how little of that change a particular oil suffers, "
              "and the <b>pour point</b> and <b>flash point</b> mark the two ends of its useful life.",
              "તેલ એકસાથે ચાર કામ કરે: સપાટી અલગ રાખે જેથી ધાતુ ધાતુને ન અડે, ઉષ્મા દૂર લઈ જાય, ગંદકી "
              "filter સુધી પહોંચાડે, અને ધાતુ પરથી oxygen અને પાણી દૂર રાખે. પહેલું કામ કરતો ગુણધર્મ "
              "<b>viscosity</b> છે, અને તે જાળવવો સૌથી કઠિન છે, કારણ કે 40 C પર 68 cSt વાળું તેલ 100 C પર "
              "લગભગ 10 cSt અને 30 C પર 300 cSt હોય - એ જ તેલ, એક જ પ્રવાહી, ત્રીસ ગણો ફરક. "
              "<b>Viscosity index</b> માપે કે કોઈ તેલ આ ફરક કેટલો ઓછો સહે છે, અને <b>pour point</b> તથી "
              "<b>flash point</b> તેના ઉપયોગી આયુષ્યની બંને ધાર બતાવે."),
            math("film parameter  lambda = h_min/sqrt(Ra1^2 + Ra2^2)",
                 "h_min = 1.2 micron, journal Ra 0.4, bearing Ra 0.3",
                 "lambda = 1.2/sqrt(0.16 + 0.09) = 1.2/0.5 = 2.4",
                 "lambda above 3 is a full film, 1 to 3 is mixed, below 1 is boundary contact"),
            table([tr("property", "ગુણધર્મ"), tr("unit", "એકમ"), tr("what it decides", "શું નક્કી કરે"),
                   tr("typical for VG 68", "VG 68 માટે સામાન્ય")],
                  [[tr("viscosity at 40 C", "40 C પર viscosity"), tr("cSt, mm2/s", "cSt, mm2/s"),
                    tr("film thickness, the grade", "ફિલ્મની જાડાઈ, grade"), tr("61.2 - 74.8", "61.2 - 74.8")],
                   [tr("viscosity index", "viscosity index"), tr("number", "આંકડો"),
                    tr("how much it thins when hot", "ગરમ થતાં કેટલું પાતળું થાય"), tr("95 - 105 mineral", "95 - 105 ખનીજ")],
                   [tr("pour point", "pour point"), tr("C", "C"),
                    tr("cold start limit", "ઠંડી શરૂઆતની મર્યાદા"), tr("-9", "-9")],
                   [tr("flash point", "flash point"), tr("C", "C"),
                    tr("fire and loss limit", "આગ અને વ્યયની મર્યાદા"), tr("200 - 240", "200 - 240")],
                   [tr("total base number", "total base number"), tr("mg KOH/g", "mg KOH/g"),
                    tr("acid neutralising reserve", "એસિડ સામે અનામત"), tr("engine oils 8 - 12", "એન્જિન તેલ 8 - 12")]]),
            why("viscosity is a thermal property because it is an activated process: a molecule needs "
                "energy to slide past its neighbours, so raising the temperature by 60 K makes it far "
                "easier. Additives that are long, stiff molecules resist the change, and that is all "
                "a high VI oil is - the same base oil with a polymer that uncoils as it warms.",
                "viscosity ઉષ્મીય ગુણધર્મ છે કારણ કે તે activated પ્રક્રિયા છે: પડોશીઓ પર સરકવા અણુને ઊર્જા "
                "જોઈએ, તેથી 60 K તાપમાન વધારવું ઘણું સરળ કરે. લાંબા, કઠણ અણુવાળા additives એ ફરક સામે ટકે, "
                "અને ઊંચા VI વાળું તેલ એટલું જ છે - એ જ base oil સાથે ગરમ થતાં ખૂલતો polymer."),
            pit("thicker is not safer. An oil that is too thick cannot reach the bearing clearance on a "
                "cold start, so the machine runs dry for the first seconds; an oil that is too thin "
                "lets the asperities touch at running temperature. The grade is chosen at the running "
                "temperature, not at the drum.",
                "જાડું વધુ સલામત નથી. વધુ જાડું તેલ ઠંડી શરૂઆતમાં bearing ના clearance સુધી પહોંચી શકે નહીં, "
                "તેથી મશીન પહેલી સેકન્ડો સૂકું ચાલે; વધુ પાતળું તેલ ચાલુ તાપમાને asperities અડવા દે. Grade "
                "ચાલુ તાપમાને પસંદ થાય, ડ્રમ પર નહીં."),
            check("for a bearing, compute lambda before choosing the grade: a 2.4 means mixed "
                  "lubrication and a shorter life, and either a thinner surface finish or a thicker "
                  "oil will fix it - not an additive.",
                  "bearing માટે grade પહેલાં lambda ગણો: 2.4 એટલે mixed lubrication અને ટૂંકું આયુષ્ય, અને "
                  "તેને પાતળી સપાટી કે જાડું તેલ સુધારશે - additive નહીં."),
            diagram="u5_visc",
        ),
        card(
            "Types, additives, and how an oil is designated",
            "પ્રકારો, additives, અને તેલનું designation કેમ થાય",
            p("Base oils come in three groups: <b>mineral</b> from crude, <b>synthetic</b> (PAO, ester, "
              "PAG, silicone) with a higher VI and a longer life, and <b>semi-synthetic</b> in "
              "between; greases are oil held in a soap thickener, and cutting fluids are neat oils or "
              "oil emulsified in water. What makes an oil an engineering product is the additive "
              "package: anti-wear and extreme pressure agents (ZDDP, sulphur, phosphorus), oxidation "
              "inhibitors, detergents and dispersants, pour point depressants, VI improvers, "
              "antifoam and rust inhibitors.",
              "Base oils ત્રણ જૂથમાં આવે: crude માંથી <b>mineral</b>, ઊંચા VI અને લાંબા આયુષ્યવાળું "
              "<b>synthetic</b> (PAO, ester, PAG, silicone), અને વચ્ચે <b>semi-synthetic</b>; grease એટલે "
              "soap thickener માં પકડાયેલું તેલ, અને cutting fluid એટલે neat oil કે પાણીમાં emulsified તેલ. "
              "તેલને ઇજનેરી ઉત્પાદન બનાવે તે additive package છે: anti-wear અને extreme pressure agents "
              "(ZDDP, sulphur, phosphorus), oxidation inhibitor, detergent અને dispersant, pour point "
              "depressant, VI improver, antifoam અને rust inhibitor."),
            math("ISO VG grade = nominal viscosity at 40 C, allowed spread +/- 10 %",
                 "grades: 10, 15, 22, 32, 46, 68, 100, 150, 220, 320, 460, 680",
                 "VG 68: 61.2 to 74.8 cSt;  VG 220: 198 to 242 cSt",
                 "an Indian drum is ordered by the IS standard, the performance class and the grade"),
            table([tr("type", "પ્રકાર"), tr("VI", "VI"), tr("range", "મર્યાદા"),
                   tr("used for", "ઉપયોગ")],
                  [[tr("hydraulic oil VG 46", "hydraulic oil VG 46"), tr("100", "100"),
                    tr("-10 to 70 C", "-10 થી 70 C"), tr("press, cylinder, servo", "press, cylinder, servo")],
                   [tr("gear oil VG 220 EP", "gear oil VG 220 EP"), tr("95", "95"),
                    tr("-5 to 80 C", "-5 થી 80 C"), tr("industrial gearbox", "ઔદ્યોગિક gearbox")],
                   [tr("turbine oil VG 32", "turbine oil VG 32"), tr("100", "100"),
                    tr("long life, demulsibility", "લાંબું આયુષ્ય, પાણી અલગ કરે"), tr("turbine, governor", "turbine, governor")],
                   [tr("compressor oil VG 68", "compressor oil VG 68"), tr("100", "100"),
                    tr("low carbon residue", "ઓછો carbon residue"), tr("reciprocating air", "reciprocating air")],
                   [tr("engine oil 15W-40", "engine oil 15W-40"), tr("135", "135"),
                    tr("-20 to 150 C", "-20 થી 150 C"), tr("diesel engine", "ડીઝલ એન્જિન")],
                   [tr("cutting oil, emulsifiable", "cutting oil, emulsifiable"), tr("-", "-"),
                    tr("1 : 20 in water", "પાણીમાં 1 : 20"), tr("turning, milling, grinding", "turning, milling, grinding")],
                   [tr("grease NLGI 2", "grease NLGI 2"), tr("-", "-"),
                    tr("-30 to 120 C", "-30 થી 120 C"), tr("bearings, chassis", "bearing, chassis")]]),
            why("an additive is a compromise that pays for itself. ZDDP is both an anti-wear film "
                "former and an antioxidant, but its phosphorus poisons a catalytic converter, which is "
                "why the same oil cannot be sold for an old engine and a new one; every additive "
                "package is a set of such trades.",
                "additive એ સમાધાન છે જે પોતાનો ખર્ચ કાઢે. ZDDP anti-wear ફિલ્મ બનાવે અને antioxidant પણ છે, "
                "પણ તેનો phosphorus catalytic converter ને નુકસાન કરે, તેથી એ જ તેલ જૂના અને નવા એન્જિન "
                "માટે વેચાય નહીં; દરેક additive package આવા સમાધાનોનો સંગ્રહ છે."),
            pit("never top up one oil with another of a different specification. Two additive packages "
                "can react, the detergent can drop out of suspension and the oil turns to sludge in "
                "the sump - the failure looks like an engine problem, not an oil problem.",
                "એક તેલમાં બીજા specification નું તેલ કદી ઉમેરો નહીં. બે additive packages react કરી શકે, "
                "detergent suspension માંથી નીકળી જાય અને તેલ sump માં કાદવ બની જાય - નિષ્ફળતા એન્જિનની "
                "લાગે, તેલની નહીં."),
            check("write the order as three lines: the IS standard, the performance class and the "
                  "viscosity grade, plus the additives you actually need. 'Good quality oil' is not "
                  "a purchase specification and cannot be inspected on receipt.",
                  "ઓર્ડર ત્રણ લીટીમાં લખો: IS standard, performance class અને viscosity grade, સાથે જરૂરી "
                  "additives. 'સારી ગુણવત્તાનું તેલ' એ ખરીદ specification નથી અને આવક પર ચકાસી શકાય નહીં."),
        ),
    ],
})
