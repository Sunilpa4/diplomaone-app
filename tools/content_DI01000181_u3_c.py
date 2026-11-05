"""DI01000181 Unit 3, part C: section 3.5 - aluminium and its alloys."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from subject_DI01000181 import tr  # noqa: E402
from content_DI01000181_lib import (p, h4, table, math, eq, why, check, pit, card,  # noqa: E402
                                    ul, ol)

NOTES_C = []

NOTES_C.append({
    "title": tr("3.5 Aluminium: wrought alloys, cast alloys and tempers",
                "3.5 Aluminium: wrought alloys, cast alloys અને tempers"),
    "items": [
        card(
            "The eight series and what the number tells you",
            "આઠ series અને આંકડો શું કહે છે",
            p("Aluminium is light - 2.70 g/cm3, a third of steel - and it protects itself with a thin "
              "oxide film, so it does not rust. Pure aluminium is soft, only 110 MPa, so almost "
              "everything used is an alloy. The wrought alloys are numbered by their main alloying "
              "element, and the first digit says which: <b>series 1 (1050)</b> is 99 % pure, "
              "<b>series 2 (2024)</b> is copper, strong but not weldable, which is why an aircraft "
              "skin is riveted, <b>series 3 (3003)</b> is manganese for kitchen foil and utensils, "
              "<b>series 4 (4043)</b> is silicon for brazing sheet, <b>series 5 (5052)</b> is "
              "magnesium for marine plate because it is the best of them at welding and at sea "
              "water, <b>series 6 (6061)</b> is magnesium plus silicon and is the extrusion alloy of "
              "window frames, ladders and structures, <b>series 7 (7075)</b> is zinc, the strongest "
              "at 570 MPa, used for an aircraft wing, and <b>series 8 (8006)</b> is everything else.",
              "Aluminium હલકું છે - 2.70 g/cm3, સ્ટીલનો ત્રીજો ભાગ - અને પાતળા oxide પડથી પોતાને રક્ષે "
              "છે, તેથી કાટ ખાતું નથી. શુદ્ધ aluminium નરમ, ફક્ત 110 MPa, તેથી વપરાતું લગભગ બધું alloy છે. "
              "Wrought alloys મુખ્ય alloying element પ્રમાણે ગણાય છે અને પહેલો અંક કહે છે કે કયો: "
              "<b>series 1 (1050)</b> 99 % શુદ્ધ, <b>series 2 (2024)</b> copper, મજબૂત પણ weldable નહીં, "
              "તેથી aircraft skin rivet થાય, <b>series 3 (3003)</b> manganese - kitchen foil અને વાસણ, "
              "<b>series 4 (4043)</b> silicon - brazing sheet, <b>series 5 (5052)</b> magnesium - marine "
              "plate, welding અને દરિયાના પાણી માટે સૌથી સારું, <b>series 6 (6061)</b> magnesium અને "
              "silicon - window frame, ladders તથી structures નું extrusion alloy, <b>series 7 (7075)</b> "
              "zinc - સૌથી મજબૂત, 570 MPa, aircraft wing, અને <b>series 8 (8006)</b> બાકીનું."),
            table([tr("Series", "Series"), tr("Main element", "મુખ્ય element"),
                   tr("UTS range", "UTS range"), tr("Weldable", "Weldable"), tr("Typical use", "સામાન્ય ઉપયોગ")],
                  [[tr("1 (1050)", "1 (1050)"), tr("none, 99 % Al", "કંઈ નહીં, 99 % Al"), tr("70 - 185 MPa", "70 - 185 MPa"),
                    tr("yes", "હા"), tr("foil, busbar, cladding", "foil, busbar, cladding (પન્ની)")],
                   [tr("2 (2024)", "2 (2024)"), tr("copper", "copper"), tr("190 - 480 MPa", "190 - 480 MPa"),
                    tr("no, needs rivets", "ના, rivets જોઈએ"), tr("aircraft skin, 2024", "aircraft skin, 2024")],
                   [tr("3 (3003)", "3 (3003)"), tr("manganese", "manganese"), tr("110 - 285 MPa", "110 - 285 MPa"),
                    tr("yes", "હા"), tr("utensils, AC tubing", "utensils, AC tubing")],
                   [tr("4 (4043)", "4 (4043)"), tr("silicon", "silicon"), tr("170 - 380 MPa", "170 - 380 MPa"),
                    tr("brazing", "brazing"), tr("filler sheet, pistons", "filler sheet, pistons (ભરણી)")],
                   [tr("5 (5052)", "5 (5052)"), tr("magnesium", "magnesium"), tr("125 - 350 MPa", "125 - 350 MPa"),
                    tr("yes, best", "હા, સૌથી સારું"), tr("marine plate, fuel tanks", "marine plate, fuel tanks (દરિયાઈ)")],
                   [tr("6 (6061)", "6 (6061)"), tr("Mg + Si", "Mg + Si"), tr("125 - 310 MPa", "125 - 310 MPa"),
                    tr("yes", "હા"), tr("extrusion: frames, ladders", "extrusion: frames, ladders (ચોકઠાં)")],
                   [tr("7 (7075)", "7 (7075)"), tr("zinc", "zinc"), tr("220 - 600 MPa", "220 - 600 MPa"),
                    tr("no", "ના"), tr("aircraft wing, 7075", "aircraft wing, 7075")],
                   [tr("8 (8006)", "8 (8006)"), tr("other (Li, Fe, Ni)", "બીજું (Li, Fe, Ni)"), tr("150 - 400 MPa", "150 - 400 MPa"),
                    tr("varies", "બદલાય"), tr("bearings, foil, specialist", "bearings, foil, વિશિષ્ટ કામ")]]),
            math("temper is written after the alloy:  6061-T6",
                 "O annealed (softest)   H strain hardened   T solution treated and aged   F as made",
                 "6061-O 110 MPa -> 6061-T6 310 MPa: the same alloy, three times the strength",
                 "",
                 "7075-T6 570 MPa against mild steel 450 MPa - and at 2.7 instead of 7.85 g/cm3"),
            why("The T tempers work by precipitation. The alloy is heated to dissolve the alloying "
                "elements, quenched to trap them in a supersaturated solution, then held warm so that "
                "fine particles precipitate and block dislocations. Nothing is added and nothing is "
                "removed - the strength comes entirely from the heat treatment, which is why the "
                "temper letter has to be written with the alloy number.",
                "T temper precipitation થી કામ કરે. Alloy ને ગરમ કરીને alloying elements ઓગળાય, quench "
                "કરીને supersaturated solution માં ફસાવાય, પછી ગરમ રાખીને નાના particles બનાવાય જે "
                "dislocation રોકે. કંઈ ઉમેરાતું નથી કે કાઢાતું નથી - તાકાત આખી heat treatment થી આવે, તેથી "
                "temper નો અક્ષર alloy ના આંકડા સાથે જ લખવો પડે."),
            diagram="u3_al",
        ),
        card(
            "Cast alloys, and choosing aluminium against steel",
            "Cast alloys, અને steel સામે aluminium પસંદ કરવું",
            p("Casting alloys are numbered differently, by a three-digit system and a decimal, because "
              "a casting cannot be rolled to close its porosity. The workhorse is <b>LM6</b>, an "
              "Al-12 % Si alloy: silicon lowers the melting point and makes the metal fluid, so it "
              "fills a mould and casts almost without shrinkage, and the result is light, "
              "corrosion-resistant and dimensionally stable - pistons, manifolds and pump bodies. "
              "<b>A356</b> with a T6 temper reaches 260 MPa and is used for wheels and gearbox "
              "housings. Cast alloys reach about 300 MPa against 600 for the best wrought alloys, so "
              "anything highly stressed is forged rather than cast.",
              "Casting alloys જુદી રીતે ગણાય છે, ત્રણ અંક અને decimal થી, કારણ કે casting ને roll કરીને "
              "તેના છિદ્રો બંધ કરી શકાતા નથી. મુખ્ય ધોરણ <b>LM6</b> છે, Al-12 % Si alloy: silicon ગલનબિંદુ "
              "નીચું કરે અને ધાતુને પ્રવાહી બનાવે, તેથી તે mould ભરે અને લગભગ shrinkage વગર cast થાય, અને "
              "પરિણામ હલકું, કાટ-પ્રતિરોધક અને માપમાં ટકી રહેતું હોય - pistons, manifolds અને pump "
              "bodies. <b>A356</b> T6 temper સાથે 260 MPa સુધી પહોંચે અને wheels તથી gearbox housings માટે "
              "વપરાય. Cast alloys લગભગ 300 MPa સુધી જાય જ્યારે શ્રેષ્ઠ wrought alloys 600, તેથી વધુ ભાર "
              "વાળો ભાગ forge કરાય, cast નહીં."),
            table([tr("Question to ask", "પૂછવાનો પ્રશ્ન"), tr("Choose aluminium when", "Aluminium પસંદ કરો જ્યારે"),
                   tr("Choose steel when", "Steel પસંદ કરો જ્યારે")],
                  [[tr("How heavy may it be?", "કેટલું ભારે ચાલે?"),
                    tr("weight or inertia matters: piston, robot arm, bicycle", "વજન કે inertia મહત્વનું: piston, robot arm, bicycle"),
                    tr("weight is no problem: machine bed, anvil", "વજન સમસ્યા નથી: machine bed, anvil")],
                   [tr("How hot does it run?", "કેટલું ગરમ ચાલે?"),
                    tr("below 150 C; strength falls fast above it", "150 C ની નીચે; ઉપર તાકાત ઝડપથી ઘટે"),
                    tr("up to 500 C or more with alloy steels", "alloy steels સાથે 500 C કે વધુ")],
                   [tr("How is it loaded?", "ભાર કેવો છે?"),
                    tr("stiffness-limited, spread over a large section", "stiffness મુખ્ય, મોટા section પર ફેલાયેલો"),
                    tr("fatigue, impact, point loads", "fatigue, impact, બિંદુ ભાર")],
                   [tr("What does it meet?", "શેના સંપર્કમાં આવે?"),
                    tr("sea water, atmosphere, food: the oxide film wins", "દરિયાનું પાણી, હવા, ખોરાક: oxide પડ જીતે"),
                    tr("abrasion, hot wear, cutting edges", "ઘસરો, ગરમ wear, cutting edges")],
                   [tr("How is it made?", "કેવી રીતે બને?"),
                    tr("extruded, die cast, deep drawn", "extruded, die cast, deep drawn (આકાર આપવો)"),
                    tr("welded, forged, induction hardened", "welded, forged, induction hardened (જોડાય, ઢબાય)")]]),
            math("same volume: steel 7.85 vs aluminium 2.70 g/cm3 -> aluminium 66 % lighter",
                 "same weight: aluminium needs 2.9 times the volume",
                 "",
                 "so replace steel by aluminium only if the section can be made thicker",
                 "or if the part is stiffness-limited and the shape can grow"),
            check("A straight swap of material at the same dimensions is safe only for a "
                  "stiffness-critical part if the deflection is allowed to grow; for a strength-limited "
                  "part you must compare specific strength, not strength.",
                  "સરખા માપ પર સીધી સામગ્રી બદલી ફક્ત ત્યારે સલામત છે જ્યારે deflection વધવા દેવાય; "
                  "તાકાત-મર્યાદિત ભાગ માટે specific strength સરખાવવું પડે, ફક્ત strength નહીં."),
        ),
    ],
})
