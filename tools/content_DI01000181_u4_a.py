"""DI01000181 Unit 4, part A: non-metallic materials in general, and rubber."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from subject_DI01000181 import tr  # noqa: E402
from content_DI01000181_lib import (p, h4, table, math, eq, why, check, pit, card,  # noqa: E402
                                    ul, ol)

NOTES_A = []

NOTES_A.append({
    "title": tr("4.1 Non-metallic materials and how they are classified",
                "4.1 Non-metallic materials અને તેમનું વર્ગીકરણ"),
    "items": [
        card(
            "Four families, chosen by bond and not by strength",
            "ચાર કુટુંબ, તાકાત થી નહીં પણ bond થી નક્કી",
            p("A non-metallic material is any engineering material that has no free electron sea. That "
              "one sentence classifies it: without free electrons there is no metallic bond, so no "
              "ductility, no conduction and no weld. The syllabus divides them into four families - "
              "<b>polymers</b> (long covalent chains held to each other by weak forces), "
              "<b>ceramics</b> (a rigid ionic and covalent network), <b>composites</b> (a stiff fibre "
              "carrying the load inside a tough matrix) and <b>natural materials</b> (wood, cork, "
              "leather, cotton) which are polymers that grew rather than being made.",
              "Non-metallic material એટલે એવી કોઈ પણ ઇજનેરી સામગ્રી જેમાં free electrons નો સમુદ્ર નથી. એક જ "
              "વાક્ય વર્ગીકરણ કરી દે છે: free electrons ન હોય તો metallic bond નહીં, તેથી ductility નહીં, "
              "વાહકતા નહીં અને weld નહીં. Syllabus તેમને ચાર કુટુંબમાં વહેંચે છે - <b>polymers</b> (લાંબી "
              "covalent chains જે એકબીજા સાથે નબળા બળથી જોડાયેલી), <b>ceramics</b> (કઠણ ionic અને covalent "
              "network), <b>composites</b> (લોડ ઉપાડતો કઠણ fibre, લચીલા matrix માં) અને <b>natural "
              "materials</b> (લાકડું, cork, ચામડું, કપાસ) જે બનાવેલા નહીં પણ ઊગેલા polymers છે."),
            table([tr("family", "કુટુંબ"), tr("bond", "bond"), tr("density, g/cm3", "density, g/cm3"),
                   tr("ceiling", "મર્યાદા"), tr("a part it makes", "એનો એક ભાગ")],
                  [[tr("polymer", "polymer"), tr("covalent chains, van der Waals between", "covalent chains, વચ્ચે van der Waals"),
                    tr("0.9 - 1.4", "0.9 - 1.4"), tr("100 - 200 C", "100 - 200 C"),
                    tr("tank, guard, gear, seal", "ટાંકી, guard, ગિયર, seal")],
                   [tr("ceramic", "ceramic"), tr("ionic and covalent network", "ionic અને covalent network"),
                    tr("2.5 - 4.0", "2.5 - 4.0"), tr("1500 - 2000 C", "1500 - 2000 C"),
                    tr("brick, insulator, insert", "ઈંટ, insulator, insert")],
                   [tr("composite", "composite"), tr("fibre plus matrix", "fibre અને matrix"),
                    tr("1.5 - 2.0", "1.5 - 2.0"), tr("120 - 180 C", "120 - 180 C"),
                    tr("tank, blade, panel", "ટાંકી, blade, panel")],
                   [tr("natural", "natural"), tr("cellulose, protein, cork", "cellulose, protein, cork (લાકડું, કૉર્ક)"),
                    tr("0.2 - 0.9", "0.2 - 0.9"), tr("under 120 C", "120 C ની નીચે"),
                    tr("packing, gasket, handle", "packing, gasket, handle (ભરણી)")]]),
            math("specific stiffness E/rho, in GPa per g/cm3",
                 "steel   200/7.85 = 25.5      alumina 300/3.9  = 76.9",
                 "CFRP    150/1.60 = 93.8      oak     11/0.70 = 15.7",
                 "alumina is 3.0 times steel and CFRP is 3.7 times, for the same weight"),
            why("the bond fixes everything downstream. A covalent chain with weak forces between the "
                "chains gives a low modulus and a low melting point; an ionic network with no free "
                "electrons gives hardness, insulation and brittleness; a composite reports the "
                "volume-weighted average of a stiff fibre and a tough matrix, which is why its "
                "stiffness sits between glass and aluminium.",
                "bond જ બાકીનું બધું નક્કી કરે છે. chains વચ્ચે નબળા બળવાળી covalent chain નીચું modulus "
                "અને નીચું ગલનબિંદુ આપે; free electrons વગરનું ionic network સખતાઈ, અવાહકતા અને ભંગુરતા "
                "આપે; composite કઠણ fibre અને લચીલા matrix ની volume-પ્રમાણે સરેરાશ આપે, તેથી તેની "
                "કઠણાઈ glass અને aluminium વચ્ચે બેસે."),
            pit("non-metallic does not mean non-metallic element. Silicon and germanium are elements "
                "but they are used as ceramics, and diamond is carbon; rubber is carbon and hydrogen, "
                "two non-metals, yet it is an engineering solid with a 22 MPa strength.",
                "non-metallic એટલે non-metallic element નહીં. Silicon અને germanium elements છે પણ "
                "ceramics તરીકે વપરાય છે, અને diamond carbon છે; rubber carbon અને hydrogen - બે "
                "non-metals - છે, તોય 22 MPa તાકાતવાળી ઇજનેરી સામગ્રી છે."),
            check("before choosing a family, ask the ceiling and the joint. A polymer above 150 C "
                  "creeps, a ceramic cannot be threaded, and a composite cannot be welded - each "
                  "one changes the design, not just the material line on the drawing.",
                  "કુટુંબ પસંદ કરતાં પહેલાં ceiling અને જોડાણ પૂછો. 150 C ઉપર polymer creep કરે, ceramic ને "
                  "thread કરી શકાય નહીં, અને composite weld થાય નહીં - દરેક material line નહીં, design "
                  "બદલે છે."),
            diagram="u4_tree",
        ),
    ],
})

NOTES_A.append({
    "title": tr("4.2 Rubber and elastomers", "4.2 Rubber અને elastomers"),
    "items": [
        card(
            "Natural rubber, and what vulcanisation did to it",
            "Natural rubber, અને vulcanisation એ શું કર્યું",
            p("Natural rubber is tapped as latex from the <b>Hevea</b> tree and dried into a gum of "
              "cis-1,4 polyisoprene chains. Raw gum is sticky, creeps under its own weight and reaches "
              "only about 2 MPa, so for fifty years it was a curiosity rather than an engineering "
              "material. In 1839 Goodyear heated it with sulphur and got a rubber that stretches "
              "550 % and comes back: <b>vulcanisation</b> ties neighbouring chains together with "
              "sulphur bridges, one every hundred to two hundred chain atoms. The chains can still "
              "uncoil - that is the softness - but they can no longer slide past each other, and that "
              "is the elasticity.",
              "Natural rubber Hevea વૃક્ષના latex માંથી નીકળે અને સુકાઈને cis-1,4 polyisoprene chains નું gum "
              "બને. કાચું gum ચીકણું હોય, પોતાના વજન નીચે વહી જાય અને ફક્ત 2 MPa સુધી પહોંચે, તેથી પચાસ વર્ષ "
              "સુધી તે ઇજનેરી સામગ્રી નહીં પણ કુતૂહલ રહ્યું. 1839 માં Goodyear એ તેને sulphur સાથે ગરમ કરીને "
              "એવું rubber મેળવ્યું જે 550 % ખેંચાય અને પાછું આવે: <b>vulcanisation</b> પડોશી chains ને "
              "sulphur પુલ થી જોડે, દર સો-બસો chain atoms માં એક. Chains હજી ખૂલી શકે - એ જ નરમાઈ - પણ "
              "એકબીજા પર સરકી શકે નહીં, અને એ જ elasticity."),
            math("E = 3G   with G = 1.0 MPa  ->  E = 3.0 MPa  (rubber is nearly incompressible)",
                 "secant modulus at 100 % strain = 1.6/1.0 = 1.6 MPa",
                 "strain energy to break ~ 0.5 x 22 x 5.5 = 60 MJ per m3",
                 "cure: 1 - 3 % sulphur at 140 - 160 C for 10 - 30 min, or a peroxide"),
            table([tr("property", "ગુણધર્મ"), tr("raw gum", "કાચું gum"),
                   tr("soft rubber", "નરમ rubber"), tr("ebonite", "ebonite")],
                  [[tr("sulphur", "sulphur"), tr("0", "0"), tr("1 - 3 %", "1 - 3 %"),
                    tr("30 - 40 %", "30 - 40 %")],
                   [tr("tensile", "tensile"), tr("2 MPa", "2 MPa"), tr("22 MPa", "22 MPa"),
                    tr("45 MPa", "45 MPa")],
                   [tr("elongation", "elongation"), tr("450 %", "450 %"), tr("550 %", "550 %"),
                    tr("3 %", "3 %")],
                   [tr("hardness", "hardness"), tr("Shore A 20", "Shore A 20"),
                    tr("Shore A 60", "Shore A 60"), tr("Shore D 75", "Shore D 75")],
                   [tr("recovery", "પાછું આવવું"), tr("none", "નહીં"), tr("100 %", "100 %"),
                    tr("100 %", "100 %")]]),
            why("a raw chain slides because van der Waals forces between chains are weak. A sulphur "
                "bridge is a covalent bond, so it pins two points of two chains together; the length "
                "of chain between two bridges still uncoils, which is why cured rubber is soft, but "
                "the network cannot flow, which is why the strain returns.",
                "કાચી chain સરકે છે કારણ કે chains વચ્ચેના van der Waals બળ નબળા છે. Sulphur પુલ covalent "
                "bond છે, તેથી બે chains ના બે બિંદુ જકડાઈ જાય; બે પુલ વચ્ચેની chain હજી ખૂલે, તેથી cured "
                "rubber નરમ છે, પણ network વહી શકે નહીં, તેથી strain પાછું આવે."),
            pit("more sulphur is not better. At 30 - 40 % sulphur the same recipe gives ebonite, a "
                "hard brittle plastic used for battery boxes and old telephone handsets, not a seal.",
                "વધુ sulphur સારું નથી. 30 - 40 % sulphur પર એ જ recipe ebonite આપે - સખત, ભંગુર plastic જે "
                "battery box અને જૂના telephone માટે વપરાય, seal માટે નહીં."),
            diagram="u4_rubber",
        ),
        card(
            "Compounding, and choosing an elastomer for the duty",
            "Compounding, અને કામ પ્રમાણે elastomer પસંદ કરવો",
            p("A rubber part is never one material. The recipe is written in <b>phr</b> - parts per "
              "hundred rubber, by weight - and a typical tyre tread is 100 phr natural or SBR, 50 phr "
              "carbon black, 3 phr sulphur, 1 phr accelerator, 2 phr zinc oxide and stearic acid, plus "
              "an antioxidant and a softener. The carbon black is what turns a 2 MPa gum into a 22 MPa "
              "compound: the particles bond to the chains, carry part of the load and stop a crack "
              "from running. The choice of base elastomer, though, is decided by the fluid and the "
              "temperature, not by the strength.",
              "Rubber નો ભાગ કદી એક જ સામગ્રીનો નથી. Recipe <b>phr</b> માં લખાય - સો ભાગ rubber દીઠ ભાગ, "
              "વજન પ્રમાણે - અને સામાન્ય ટાયર tread એટલે 100 phr natural કે SBR, 50 phr carbon black, 3 phr "
              "sulphur, 1 phr accelerator, 2 phr zinc oxide અને stearic acid, સાથે antioxidant અને "
              "softener. Carbon black જ 2 MPa ના gum ને 22 MPa નું compound બનાવે: કણ chains સાથે જોડાય, "
              "લોડનો ભાગ ઉપાડે અને તિરાડ લાંબી દોડતી અટકાવે. પણ base elastomer ની પસંદગી તાકાત નહીં, પ્રવાહી "
              "અને તાપમાન નક્કી કરે છે."),
            math("recipe in phr:  100 gum + 50 black + 3 S + 1 accelerator + 2 ZnO = 156 phr",
                 "carbon black share = 50/156 = 32 % of the compound by weight",
                 "tensile 2 MPa -> 22 MPa; modulus at 100 % strain 1.6 -> 4.5 MPa",
                 "an oil seal swells 50 % in NR, 10 % in SBR and 5 % in NBR"),
            table([tr("elastomer", "elastomer"), tr("service range", "સેવા મર્યાદા"),
                   tr("resists", "શેની સામે ટકે"), tr("fails at", "શેમાં નિષ્ફળ જાય"),
                   tr("used for", "ઉપયોગ")],
                  [[tr("NR natural", "NR natural"), tr("-50 to 90 C", "-50 થી 90 C"),
                    tr("tear, fatigue", "છેકું, fatigue"), tr("oil, ozone, heat", "તેલ, ozone, ગરમી"),
                    tr("tyre, mount, belt", "ટાયર, mount, belt")],
                   [tr("SBR", "SBR"), tr("-40 to 100 C", "-40 થી 100 C"),
                    tr("abrasion", "ઘસારો"), tr("oil, ozone", "તેલ, ozone"),
                    tr("tyre tread, shoe sole", "ટાયર tread, જૂતાના તળિયા")],
                   [tr("NBR nitrile", "NBR nitrile"), tr("-30 to 120 C", "-30 થી 120 C"),
                    tr("mineral oil, fuel", "ખનીજ તેલ, fuel"), tr("ozone, ketones", "ozone, ketone"),
                    tr("oil seal, hose, gasket", "તેલ seal, hose, gasket")],
                   [tr("CR neoprene", "CR neoprene"), tr("-40 to 120 C", "-40 થી 120 C"),
                    tr("weather, flame", "હવામાન, જ્યોત"), tr("ester oils", "ester તેલ"),
                    tr("gasket, cable jacket", "gasket, cable jacket (ભરણી, આવરણ)")],
                   [tr("EPDM", "EPDM"), tr("-50 to 150 C", "-50 થી 150 C"),
                    tr("steam, ozone, UV", "steam, ozone, UV"), tr("mineral oil", "ખનીજ તેલ"),
                    tr("radiator hose, roofing", "radiator hose, છત")],
                   [tr("silicone", "silicone"), tr("-60 to 230 C", "-60 થી 230 C"),
                    tr("heat, cold, ozone", "ગરમી, ઠંડી, ozone"), tr("tear, oil", "છેકું, તેલ"),
                    tr("oven seal, keypad", "ઓવન seal, keypad")],
                   [tr("butyl", "butyl"), tr("-40 to 120 C", "-40 થી 120 C"),
                    tr("air, water", "હવા, પાણી"), tr("heat, oil", "ગરમી, તેલ"),
                    tr("inner tube, liner", "inner tube, liner")]]),
            why("a seal fails on the fluid long before it fails on the load. Rubber is a polymer "
                "network with free volume, so a solvent that wets it diffuses in and swells it; the "
                "swelling is a property of the pair, not of the rubber alone, which is why the "
                "datasheet prints a volume swell against oil, water and fuel.",
                "seal લોડ પર નહીં, પ્રવાહી પર પહેલાં નિષ્ફળ જાય. Rubber એ free volume વાળું polymer network "
                "છે, તેથી જે દ્રાવક તેને ભીંજવે તે અંદર ફેલાઈને ફુલાવે; ફૂલવું એ rubber નું નહીં, જોડીનું "
                "ગુણધર્મ છે, તેથી datasheet તેલ, પાણી અને fuel સામે volume swell આપે છે."),
            pit("a rubber that swells 10 % in service has already failed: a 50 mm O-ring grows to 55 mm, "
                "the groove no longer holds it and the joint leaks at the next pressure cycle.",
                "સેવામાં 10 % ફૂલી ગયેલું rubber નિષ્ફળ જ ગયું છે: 50 mm O-ring 55 mm થાય, groove તેને "
                "પકડી શકે નહીં અને આગલા pressure cycle માં જોડાણ ચૂ થાય."),
            check("write the duty as four numbers - fluid, temperature, movement and life - and only "
                  "then read the table. Hardness is the last choice, not the first: a 70 Shore A "
                  "nitrile and a 70 Shore A silicone behave completely differently in hot oil.",
                  "કામ ચાર આંકડામાં લખો - પ્રવાહી, તાપમાન, હલનચલન અને આયુષ્ય - અને પછી જ કોષ્ટક વાંચો. "
                  "Hardness પહેલી નહીં, છેલ્લી પસંદગી છે: 70 Shore A nitrile અને 70 Shore A silicone "
                  "ગરમ તેલમાં સાવ જુદું વર્તન કરે."),
        ),
    ],
})
