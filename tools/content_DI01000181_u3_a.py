"""DI01000181 Unit 3, part A: sections 3.1 and 3.2 - classification, steels and their designation."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from subject_DI01000181 import tr  # noqa: E402
from content_DI01000181_lib import (p, h4, table, math, eq, why, check, pit, card,  # noqa: E402
                                    ul, ol)

NOTES_A = []

NOTES_A.append({
    "title": tr("3.1 Classification of metals, and metals against non-metals",
                "3.1 Metals નું વર્ગીકરણ, અને metals સામે non-metals"),
    "items": [
        card(
            "Two branches, and the carbon content that splits the first one",
            "બે શાખા, અને પહેલીને વહેંચતું carbon content",
            p("Engineering metals are either <b>ferrous</b> - based on iron - or <b>non-ferrous</b>, "
              "based on some other metal. The ferrous branch splits at one number: <b>2.14 % "
              "carbon</b>, the most that austenite can dissolve. Below it the material is "
              "<b>steel</b>, which can be rolled, forged and welded; above it the material is "
              "<b>cast iron</b>, which is poured into a mould and cannot be rolled because the "
              "eutectic at 4.3 % carbon makes it too brittle. Steel itself is described in two "
              "ways - by its carbon content (plain carbon steels) or by the element added to give it "
              "a property it did not have (alloy steels).",
              "ઇજનેરી ધાતુઓ <b>ferrous</b> - લોખંડ પર આધારિત - અથવા <b>non-ferrous</b> હોય છે, જે "
              "બીજી કોઈ ધાતુ પર આધારિત હોય. Ferrous શાખા એક જ આંકડા પર વહેંચાય છે: <b>2.14 % "
              "carbon</b>, જેટલું austenite ઓગાળી શકે તે વધુમાં વધુ. તેની નીચે સામગ્રી <b>steel</b> છે, "
              "જે roll, forge અને weld કરી શકાય; તેની ઉપર <b>cast iron</b> છે, જે mould માં રેડાય છે "
              "અને roll થઈ શકતું નથી કારણ કે 4.3 % carbon પરનું eutectic તેને ખૂબ ભંગુર કરે છે. સ્ટીલને "
              "બે રીતે વર્ણવાય છે - તેના carbon content થી (plain carbon steels) અથવા જે element ઉમેરાય "
              "તે થી (alloy steels)."),
            table([tr("Family", "કુટુંબ"), tr("Carbon", "Carbon"),
                   tr("What it is for", "શેના માટે"), tr("Examples", "ઉદાહરણ")],
                  [[tr("Low carbon steel", "Low carbon steel"), tr("up to 0.30 %", "0.30 % સુધી"),
                    tr("formable and weldable, cheap", "formable, weldable, સસ્તું"),
                    tr("C10, C20, EN32", "C10, C20, EN32")],
                   [tr("Medium carbon steel", "Medium carbon steel"), tr("0.30 - 0.60 %", "0.30 - 0.60 %"),
                    tr("hardenable, good strength", "hardenable, સારી તાકાત"),
                    tr("C40, C45, EN8, EN9", "C40, C45, EN8, EN9")],
                   [tr("High carbon steel", "High carbon steel"), tr("0.60 - 2.14 %", "0.60 - 2.14 %"),
                    tr("springs, tools, wear", "સ્પ્રિંગ, tools, wear"),
                    tr("C80, EN42, EN31", "C80, EN42, EN31")],
                   [tr("Alloy steel", "Alloy steel"), tr("any, plus Cr, Ni, Mo, V", "કોઈ પણ, સાથે Cr, Ni, Mo, V"),
                    tr("corrosion, toughness, hardenability", "કાટ, toughness, hardenability"),
                    tr("SS 304, EN19, HSS M2", "SS 304, EN19, HSS M2 (સ્ટેનલેસ, ટૂલ સ્ટીલ)")],
                   [tr("Cast iron", "Cast iron"), tr("2.14 - 6.67 %", "2.14 - 6.67 %"),
                    tr("castings, damping, compression", "castings, damping, compression (કંપન શોષણ)"),
                    tr("grey, white, ductile CI", "grey, white, ductile CI (ભૂખરું, સફેદ)")],
                   [tr("Copper alloys", "Copper alloys"), tr("nil", "કંઈ નહીં"),
                    tr("conduction, bearing, sea water", "વહન, bearing, દરિયાનું પાણી"),
                    tr("brass, bronze, gunmetal", "પિત્તળ, bronze, gunmetal")],
                   [tr("Aluminium alloys", "Aluminium alloys"), tr("nil", "કંઈ નહીં"),
                    tr("weight saving, corrosion", "વજન બચત, corrosion"),
                    tr("6061-T6, 7075, LM6", "6061-T6, 7075, LM6")]]),
            math("steel vs cast iron:  2.14 % C is the boundary",
                 "plain carbon steel classification:  low <= 0.30,  medium 0.30-0.60,  high 0.60-2.14",
                 "cast iron:  eutectic at 4.3 % C, so most cast irons sit at 3.0 - 3.8 % C",
                 "",
                 "density: steel 7.85, cast iron 7.2, copper 8.96, aluminium 2.70 g/cm3"),
            why("Everything in the ferrous branch follows from the iron-carbon diagram of Unit 2. Up "
                "to 2.14 % the carbon can hide inside austenite, so the metal can be deformed hot and "
                "becomes steel; beyond that the excess carbon has to appear as cementite at the grain "
                "boundaries, which is what makes white cast iron hard and unmachinable.",
                "Ferrous શાખાનું બધું Unit 2 ના iron-carbon diagram પરથી આવે. 2.14 % સુધી carbon "
                "austenite માં સંતાઈ શકે, તેથી ધાતુ ગરમ કરીને deform કરી શકાય અને steel બને; તેનાથી ઉપર "
                "વધારાનો carbon grain boundary પર cementite સ્વરૂપે આવવો પડે, અને તેથી જ white cast iron "
                "સખત અને unmachinable બને."),
            diagram="u3_tree",
        ),
        card(
            "Metals and non-metals: one test settles it",
            "Metals અને non-metals: એક જ કસોટી નક્કી કરે",
            p("A metal has <b>free electrons</b> that belong to the whole crystal instead of to a "
              "particular pair of atoms. Every other difference in the comparison below follows from "
              "that one: free electrons carry current and heat, reflect light (lustre), and allow "
              "layers of atoms to slide without breaking the bond, which is ductility. A non-metal "
              "holds its electrons in fixed bonds, so it insulates, looks dull and cracks instead of "
              "bending. Silicon and germanium sit between the two and are called <b>metalloids</b>.",
              "ધાતુમાં <b>free electrons</b> હોય છે જે કોઈ એક જોડીના atoms ના નહીં પણ આખા crystal ના "
              "હોય. નીચેની સરખામણીનો બાકીનો દરેક ફરક એક જ વાત પરથી આવે: free electrons current અને ગરમી "
              "વહન કરે, પ્રકાશ પાછો ઝીલે (lustre), અને atoms ના સ્તરો bond તોડ્યા વગર સરકી શકે - એ જ "
              "ductility. Non-metal પોતાના electrons નિશ્ચિત bonds માં રાખે, તેથી તે અવાહક, ઝાંખું અને "
              "વળવાને બદલે તૂટે છે. Silicon અને germanium વચ્ચે બેસે છે અને તેમને <b>metalloids</b> કહે છે."),
            table([tr("Property", "ગુણધર્મ"), tr("Metal", "Metal"), tr("Non-metal", "Non-metal")],
                  [[tr("Electrons", "Electrons"), tr("free, shared by the crystal", "મુક્ત, crystal આખાના"),
                    tr("held in fixed bonds", "નિશ્ચિત bonds માં")],
                   [tr("Conduction", "વાહકતા"), tr("heat and current: copper 385 W/m K", "ગરમી અને current: copper 385 W/m K"),
                    tr("insulator; graphite and Si are exceptions", "અવાહક; graphite અને Si અપવાદ")],
                   [tr("Deformation", "Deformation"), tr("malleable and ductile", "malleable અને ductile"),
                    tr("brittle - it cracks", "ભંગુર - તૂટે")],
                   [tr("Lustre", "Lustre"), tr("shiny, reflects light", "ચળકતું, પ્રકાશ પાછો ઝીલે"),
                    tr("dull", "ઝાંખું")],
                   [tr("Melting point", "ગલનબિંદુ"), tr("usually high, 660 C to 3400 C", "સામાન્ય રીતે ઊંચું, 660 C થી 3400 C"),
                    tr("low (sulphur 115 C) or very high (diamond 3550 C)", "નીચું (sulphur 115 C) કે ખૂબ ઊંચું (diamond 3550 C)")],
                   [tr("Density", "Density"), tr("2.7 to 19 g/cm3", "2.7 થી 19 g/cm3"),
                    tr("under 5 g/cm3", "5 g/cm3 ની નીચે")],
                   [tr("Oxides", "Oxides"), tr("basic: Na2O, FeO, they react with acid", "basic: Na2O, FeO, એસિડ સાથે react કરે"),
                    tr("acidic: CO2, SiO2, they react with alkali", "acidic: CO2, SiO2, આલ્કલી સાથે react કરે")]]),
            math("sigma(copper) = 5.8e7 S/m      sigma(glass) = 1e-12 S/m",
                 "5.8e7 / 1e-12 = 5.8e19 -> nineteen orders of magnitude",
                 "one free electron per atom is the whole difference"),
            pit("Do not write 'metals are hard'. Lead is a metal and is softer than your thumb; "
                "diamond is a non-metal and scratches everything. Hardness is not the test - free "
                "electrons are.",
                "'Metals સખત હોય' એવું ન લખો. Lead ધાતુ છે અને અંગૂઠા કરતાં નરમ છે; diamond અધાતુ છે "
                "અને બધું ખૂંચે છે. Hardness કસોટી નથી - free electrons છે."),
            diagram="u3_compare",
        ),
    ],
})

NOTES_A.append({
    "title": tr("3.2 Steels: plain carbon, alloy, and how they are ordered",
                "3.2 Steels: plain carbon, alloy, અને તે કેવી રીતે ઓર્ડર થાય"),
    "items": [
        card(
            "Plain carbon steels: what carbon buys and what it costs",
            "Plain carbon steels: carbon શું આપે અને શું લે",
            p("A plain carbon steel is iron with carbon and nothing else that matters - manganese up "
              "to 0.8 % for deoxidation and sulphur and phosphorus kept low. Everything about it "
              "follows from the volume fraction of pearlite, and that follows from the carbon "
              "content. More carbon means more cementite, so the steel gets stronger and harder and "
              "less ductile and less weldable. The strength roughly doubles between 0.1 % and 1.2 % "
              "carbon while the elongation falls from 30 % to 5 %, which is why the useful "
              "engineering steels sit between 0.2 % and 0.5 %.",
              "Plain carbon steel એ iron સાથે carbon છે અને બીજું કંઈ નહીં - deoxidation માટે 0.8 % "
              "સુધી manganese અને sulphur તથા phosphorus ઓછા રખાય. તેનું બધું pearlite ના volume fraction "
              "પરથી આવે, અને એ carbon content પરથી આવે. વધુ carbon એટલે વધુ cementite, તેથી સ્ટીલ વધુ "
              "મજબૂત અને સખત પણ ઓછું ductile અને ઓછું weldable બને. 0.1 % થી 1.2 % carbon વચ્ચે તાકાત "
              "લગભગ બમણી થાય જ્યારે elongation 30 % થી 5 % થાય, તેથી ઉપયોગી ઇજનેરી સ્ટીલ 0.2 % થી "
              "0.5 % વચ્ચે બેસે છે."),
            table([tr("Steel", "સ્ટીલ"), tr("C %", "C %"), tr("UTS (MPa)", "UTS (MPa)"),
                   tr("Elongation", "Elongation"), tr("Hardness", "Hardness"), tr("Typical use", "સામાન્ય ઉપયોગ")],
                  [[tr("Dead mild", "Dead mild"), tr("0.10", "0.10"), tr("400", "400"), tr("30 %", "30 %"),
                    tr("110 HB", "110 HB"), tr("sheet, wire, nails, car body", "sheet, wire, nails, car body (ચાદર, તાર, ખીલા)")],
                   [tr("Mild", "Mild"), tr("0.20", "0.20"), tr("450", "450"), tr("27 %", "27 %"),
                    tr("130 HB", "130 HB"), tr("structurals, studs, chain", "structurals, studs, chain (બાંધકામ, ચેઇન)")],
                   [tr("Medium", "Medium"), tr("0.40", "0.40"), tr("600", "600"), tr("20 %", "20 %"),
                    tr("170 HB", "170 HB"), tr("shafts, axles, gears, keys", "shafts, axles, gears, keys (ધરી, ગિયર)")],
                   [tr("Eutectoid", "Eutectoid"), tr("0.80", "0.80"), tr("800", "800"), tr("10 %", "10 %"),
                    tr("230 HB", "230 HB"), tr("springs, piano wire, saws", "સ્પ્રિંગ, piano wire, saws")],
                   [tr("Hypereutectoid", "Hypereutectoid"), tr("1.20", "1.20"), tr("900", "900"), tr("5 %", "5 %"),
                    tr("285 HB", "285 HB"), tr("files, razors, dies, balls", "files, razors, dies, balls (પાની, બેરિંગ)")]]),
            math("pearlite % = (C - 0.02)/0.78 x 100       every +0.10 % C adds 12.8 % pearlite",
                 "",
                 "0.2 % C -> 23 % pearlite       0.4 % C -> 49 % pearlite",
                 "0.8 % C -> 100 % pearlite      1.2 % C -> 100 % pearlite + 6.8 % cementite",
                 "",
                 "so 'more carbon' means 'more cementite in the mixture', not a different metal"),
            check("Read the table across, not down: every row trades strength for elongation. A "
                  "question that asks for 'the strongest steel' is incomplete until it says for what - "
                  "a file wants 1.2 % and a car body wants 0.1 %.",
                  "કોષ્ટક આડું વાંચો, ઊભું નહીં: દરેક લાઈન તાકાત સામે elongation નો સોદો કરે. 'સૌથી મજબૂત "
                  "સ્ટીલ' પૂછે તો શેના માટે તે કહ્યા વગર અધૂરું છે - file ને 1.2 % અને car body ને 0.1 % "
                  "જોઈએ."),
            diagram="u3_carbon",
        ),
        card(
            "Alloy steels, stainless steel and how a designation is read",
            "Alloy steels, stainless steel અને designation કેવી રીતે વાંચવું",
            p("Carbon alone cannot give a thick section that hardens all the way through, nor a "
              "surface that resists rust, nor a steel that stays tough at 500 C. An <b>alloy steel</b> "
              "adds one or more elements to buy exactly those properties: <b>chromium</b> above 12 % "
              "forms a passive oxide film (stainless), <b>nickel</b> raises toughness and makes the "
              "austenite stable at room temperature (18/8), <b>molybdenum</b> raises hardenability and "
              "high-temperature strength, <b>vanadium</b> and <b>tungsten</b> keep the hardness at red "
              "heat (tool steels), and small amounts of <b>niobium</b> or <b>titanium</b> give the "
              "fine-grain high-strength low-alloy steels used in pipelines.",
              "ફક્ત carbon થી જાડો ભાગ આખો harden થાય, સપાટી કાટ સામે ટકે, કે 500 C પર toughness "
              "જળવાય તે શક્ય નથી. <b>Alloy steel</b> એ એક કે વધુ element ઉમેરીને બરાબર એ ગુણધર્મ ખરીદે છે: "
              "12 % થી ઉપર <b>chromium</b> passive oxide પડ બનાવે (stainless), <b>nickel</b> toughness "
              "વધારે અને austenite ને room temperature પર ટકાવે (18/8), <b>molybdenum</b> hardenability "
              "અને ઊંચા temperature ની તાકાત વધારે, <b>vanadium</b> અને <b>tungsten</b> લાલ ગરમીમાં પણ "
              "hardness રાખે (tool steels), અને થોડું <b>niobium</b> કે <b>titanium</b> pipeline માં વપરાતું "
              "fine-grain high-strength low-alloy સ્ટીલ આપે."),
            table([tr("Steel", "સ્ટીલ"), tr("Main elements", "મુખ્ય elements"),
                   tr("Property it buys", "જે ગુણધર્મ મળે"), tr("Where it is used", "ક્યાં વપરાય")],
                  [[tr("SS 304", "SS 304"), tr("18 Cr, 8 Ni, 0.08 C", "18 Cr, 8 Ni, 0.08 C"),
                    tr("corrosion resistance, weldable", "કાટ પ્રતિકાર, weldable"),
                    tr("kitchen, dairy, architecture", "રસોડું, dairy, architecture")],
                   [tr("SS 316", "SS 316"), tr("16 Cr, 10 Ni, 2 Mo", "16 Cr, 10 Ni, 2 Mo"),
                    tr("resists chlorides and sea water", "chloride અને દરિયાના પાણી સામે ટકે"),
                    tr("chemical plant, marine, surgical", "chemical plant, દરિયાઈ, surgical")],
                   [tr("SS 410", "SS 410"), tr("12 Cr, 0.15 C, no Ni", "12 Cr, 0.15 C, Ni નહીં"),
                    tr("hardenable, cheaper stainless", "hardenable, સસ્તું stainless"),
                    tr("cutlery blades, pump shafts", "cutlery blades, pump shafts (ચાકુ, પંપ)")],
                   [tr("EN19", "EN19"), tr("0.4 C, 1 Cr, 0.25 Mo", "0.4 C, 1 Cr, 0.25 Mo (રચના)"),
                    tr("through-hardenable and tough", "આખું hardenable અને tough"),
                    tr("gears, crankshafts, axles", "ગિયર, crankshafts, axles")],
                   [tr("EN31", "EN31"), tr("1 C, 1.5 Cr", "1 C, 1.5 Cr"),
                    tr("very hard and wear resistant", "ખૂબ સખત અને wear પ્રતિરોધક"),
                    tr("ball bearings, dies, rolls", "ball bearings, dies, rolls (બેરિંગ, રોલ)")],
                   [tr("HSS M2", "HSS M2"), tr("0.85 C, 4 Cr, 5 Mo, 6 W, 2 V", "0.85 C, 4 Cr, 5 Mo, 6 W, 2 V (રચના)"),
                    tr("keeps hardness up to 600 C", "600 C સુધી hardness રાખે"),
                    tr("drills, taps, milling cutters", "drills, taps, milling cutters (કોરણી)")]]),
            math("stainless needs Cr > 12 % for a continuous passive film",
                 "18/8 (304): Cr 18 %, Ni 8 % - austenitic, non-magnetic, not hardenable by quench",
                 "12 % Cr (410): martensitic - hardenable, magnetic, less corrosion resistant",
                 "",
                 "designation:  C 45 = 0.45 % C plain carbon;  EN19 = old BS name of 709M40",
                 "X 5 CrNi 18-10 = 0.05 % C, 18 % Cr, 10 % Ni"),
            pit("Stainless steel is not 'steel that cannot rust'. It is steel whose chromium makes a "
                "self-healing oxide skin. Scratch it in chloride water, or heat it to 600 C and let "
                "chromium carbide form at the grain boundaries, and it corrodes like any steel.",
                "Stainless steel એ 'કાટ ન લાગે તેવું સ્ટીલ' નથી. તે એવું સ્ટીલ છે જેનું chromium પોતાની "
                "જાતે સંધાતું oxide પડ બનાવે. Chloride વાળા પાણીમાં ખૂંચે, કે 600 C પર ગરમ કરી grain "
                "boundary પર chromium carbide બનવા દો, તો તે પણ સામાન્ય સ્ટીલની જેમ કાટ ખાય."),
            diagram="u3_desig",
        ),
    ],
})
