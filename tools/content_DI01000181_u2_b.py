"""DI01000181 Unit 2, part B: sections 2.3 and 2.4 - solid solutions and the binary diagrams."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from subject_DI01000181 import tr  # noqa: E402
from content_DI01000181_lib import (p, h4, table, math, eq, why, check, pit, card,  # noqa: E402
                                    ul, ol)

NOTES_B = []

NOTES_B.append({
    "title": tr("2.3 Solid solution, intermediate phase and the Hume-Rothery rules",
                "2.3 Solid solution, intermediate phase અને Hume-Rothery rules"),
    "items": [
        card(
            "Two ways to dissolve one metal in another",
            "એક ધાતુ બીજીમાં ઓગળવાની બે રીત",
            p("A <b>solid solution</b> is a single crystal in which one kind of atom has been replaced "
              "by another without changing the lattice. If the two atoms are of similar size the "
              "substitute atom simply takes the place of the one it replaced: a <b>substitutional</b> "
              "solution, as in copper-nickel, brass or stainless steel. If the second atom is much "
              "smaller it cannot take a lattice site and instead sits in the gap between the atoms: an "
              "<b>interstitial</b> solution, as carbon, nitrogen or hydrogen in iron. Interstitial "
              "atoms are few - carbon reaches only 2.14 % in austenite and 0.02 % in ferrite - but "
              "they distort the lattice and control the hardness of steel.",
              "<b>Solid solution</b> એ એક જ crystal છે જેમાં એક જાતના atom ની જગ્યાએ બીજા જાતના atom "
              "આવે છે, પણ lattice બદલાતું નથી. બે atoms ના માપ સરખા હોય તો નવો atom પોતાની જગ્યા "
              "સંભાળી લે: <b>substitutional</b> solution, જેમ copper-nickel, brass કે stainless steel માં. "
              "બીજો atom ઘણો નાનો હોય તો lattice ની જગ્યા લઈ શકે નહીં અને atoms વચ્ચેની ખાલી જગ્યામાં "
              "બેસે: <b>interstitial</b> solution, જેમ iron માં carbon, nitrogen કે hydrogen. Interstitial "
              "atoms થોડા હોય છે - austenite માં carbon 2.14 % અને ferrite માં 0.02 % સુધી જ - પણ તે "
              "lattice ને વાળે છે અને સ્ટીલની hardness નક્કી કરે છે."),
            table([tr("Point", "મુદ્દો"), tr("Substitutional", "Substitutional"),
                   tr("Interstitial", "Interstitial")],
                  [[tr("The second atom", "બીજો atom"),
                    tr("replaces a host atom on its site", "host atom ની જગ્યાએ બેસે"),
                    tr("sits in a gap between host atoms", "host atoms વચ્ચેની ખાલી જગ્યામાં બેસે")],
                   [tr("Size of the second atom", "બીજા atom નું માપ"),
                    tr("within 15 % of the host", "host કરતાં 15 % અંદર"),
                    tr("much smaller, below 0.6 of the host radius", "ઘણો નાનો, host radius ના 0.6 થી નીચે")],
                   [tr("How much dissolves", "કેટલું ઓગળે"),
                    tr("up to 100 % (Cu-Ni)", "100 % સુધી (Cu-Ni)"),
                    tr("a small fraction (max 2.14 % C)", "થોડો ભાગ (વધુમાં વધુ 2.14 % C)")],
                   [tr("Effect on properties", "ગુણધર્મો પર અસર"),
                    tr("raises strength and hardness steadily", "તાકાત અને hardness સતત વધારે"),
                    tr("distorts the lattice, huge effect on hardness", "lattice વાળે, hardness પર ઘણી અસર")],
                   [tr("Example", "ઉદાહરણ"),
                    tr("brass, bronze, stainless steel", "પિત્તળ, bronze, stainless steel"),
                    tr("carbon and nitrogen in steel", "સ્ટીલમાં carbon અને nitrogen")]]),
            math("Vegard's law:   a(alloy) = x a(A) + (1 - x) a(B)",
                 "",
                 "Cu-Ni solid solution, a(Cu) = 0.3615 nm, a(Ni) = 0.3524 nm",
                 "50 % alloy: a = 0.5 x 0.3615 + 0.5 x 0.3524 = 0.3570 nm",
                 "measured for 50/50 cupro-nickel: 0.3568 nm - within 0.06 %",
                 "",
                 "interstitial carbon distorts instead: 0.02 % C in ferrite already changes a by 0.0002 nm"),
            why("The lattice parameter of a substitutional solution changes almost linearly with "
                "composition - Vegard's law - because the two atoms simply share the sites in "
                "proportion. That linear change is used to measure how much solute a phase holds, and "
                "it is why a copper-nickel alloy has one density you can predict.",
                "Substitutional solution નું lattice parameter composition સાથે લગભગ સીધું બદલાય છે - "
                "Vegard's law - કારણ કે બે atoms પ્રમાણમાં જગ્યા વહેંચે છે. એ સીધા ફેરફારથી phase માં "
                "કેટલું solute છે તે મપાય છે, અને તેથી copper-nickel alloy ની density અગાઉથી ગણી શકાય છે."),
            diagram="u2_solution",
        ),
        card(
            "The Hume-Rothery rules, and when a compound forms instead",
            "Hume-Rothery rules, અને ત્યારે શું compound બને",
            p("Two metals do not dissolve in each other in every proportion. The four rules below say "
              "when a wide substitutional solution is possible; break one of them and the solubility "
              "drops, break several and the pair prefers to form a <b>compound</b> with a fixed "
              "composition. That compound - CuAl2, Fe3C, Mg2Si - is called an <b>intermediate phase</b>: "
              "it has its own lattice, its own melting point, and usually it is hard and brittle.",
              "બે ધાતુઓ દરેક પ્રમાણમાં એકબીજામાં ઓગળતી નથી. નીચેના ચાર નિયમો કહે છે કે પહોળું "
              "substitutional solution ક્યારે શક્ય છે; એક નિયમ તૂટે તો solubility ઘટે, ઘણા તૂટે તો જોડી "
              "નિશ્ચિત composition નું <b>compound</b> બનાવવાનું પસંદ કરે. એ compound - CuAl2, Fe3C, "
              "Mg2Si - ને <b>intermediate phase</b> કહે છે: તેનું પોતાનું lattice, પોતાનું ગલનબિંદુ, અને "
              "સામાન્ય રીતે તે સખત અને ભંગુર હોય છે."),
            ol((tr("<b>Size factor:</b> the atomic radii differ by less than 15 %.", "<b>Size factor:</b> atomic radii માં ફરક 15 % થી ઓછો.")),
               (tr("<b>Crystal structure:</b> both metals have the same lattice type.", "<b>Crystal structure:</b> બંને ધાતુનું lattice એક જ પ્રકારનું.")),
               (tr("<b>Valency:</b> the same valency dissolves best; a metal of low valency dissolves little of a metal of high valency.", "<b>Valency:</b> સરખી valency સૌથી સારી ઓગળે; ઓછી valency વાળી ધાતુ વધુ valency વાળી ધાતુનું થોડું ઓગાળે.")),
               (tr("<b>Electronegativity:</b> close values; a large difference gives an ionic compound instead of a solution.", "<b>Electronegativity:</b> મૂલ્યો નજીક; મોટો ફરક હોય તો solution ને બદલે ionic compound બને.")),
               (tr("<b>Relative valency effect</b> and a large temperature difference between the melting points reduce solubility too.", "<b>Relative valency effect</b> અને ગલનબિંદુમાં મોટો ફરક પણ solubility ઘટાડે."))),
            math("Cu-Ni:  r(Cu) = 128 pm, r(Ni) = 125 pm -> difference 2.3 %  (rule 1 passes)",
                 "        both FCC                                     (rule 2 passes)",
                 "        -> complete solubility, no compound",
                 "",
                 "Cu-Zn:  r(Cu) = 128 pm, r(Zn) = 134 pm -> 4.7 % (passes), but brass stops",
                 "        at about 39 % Zn and then the beta phase appears",
                 "Fe-C:   r(Fe) = 126 pm, r(C) = 77 pm -> carbon is 39% of iron: no substitution",
                 "        carbon is interstitial, and above 6.67 % it is all cementite"),
            pit("Do not say carbon 'dissolves in iron up to 2.14 %' without saying which iron. It is "
                "austenite (FCC) that takes 2.14 %; ferrite (BCC) takes only 0.02 %, which is why "
                "quenching traps carbon in a distorted lattice and makes martensite.",
                "'Carbon iron માં 2.14 % સુધી ઓગળે' એ કઈ iron તે કહ્યા વગર ન કહો. 2.14 % austenite "
                "(FCC) લે છે; ferrite (BCC) ફક્ત 0.02 % લે છે, અને તેથી જ quenching માં carbon વળેલા "
                "lattice માં ફસાય અને martensite બને."),
        ),
    ],
})

NOTES_B.append({
    "title": tr("2.4 Reading a binary phase diagram, and the lever rule",
                "2.4 Binary phase diagram વાંચવું, અને lever rule"),
    "items": [
        card(
            "Copper-nickel: the isomorphous diagram and the lever rule",
            "Copper-nickel: isomorphous diagram અને lever rule",
            p("Copper and nickel pass all the Hume-Rothery tests, so their diagram is the simplest one "
              "possible: a single liquidus above a single solidus, meeting at the melting points of "
              "the two pure metals. Every alloy of the pair begins to freeze at its liquidus, finishes "
              "at its solidus, and inside the lens between them two phases - liquid and solid solution "
              "- sit side by side. The compositions of those two phases are read at the two ends of a "
              "horizontal <b>tie line</b> drawn at the temperature of interest, and how much of each "
              "there is comes from the <b>lever rule</b>.",
              "Copper અને nickel બધા Hume-Rothery કસોટી પાસ કરે છે, તેથી તેમનો diagram સૌથી સરળ છે: એક "
              "liquidus નીચે એક જ solidus, જે બંને શુદ્ધ ધાતુનાં ગલનબિંદુએ મળે છે. જોડીનું દરેક alloy "
              "પોતાના liquidus પર થીજવા લાગે, solidus પર પૂરું થાય, અને વચ્ચેના lens માં liquid અને "
              "solid solution - બે phase સાથે રહે છે. એ બે phase નું composition વિચારેલા temperature પર "
              "દોરેલી સપાટ <b>tie line</b> ના બે છેડે વંચાય છે, અને દરેક કેટલું છે તે <b>lever rule</b> "
              "આપે છે."),
            math("lever rule on a tie line at T, alloy composition C0:",
                 "",
                 "W(liquid) = (C_s - C0) / (C_s - C_l)      W(solid) = (C0 - C_l) / (C_s - C_l)",
                 "W(liquid) + W(solid) = 1",
                 "",
                 "50 % Ni at 1300 C:  C_l = 40 % Ni,  C_s = 60 % Ni",
                 "W(liquid) = (60 - 50)/(60 - 40) = 10/20 = 0.50",
                 "W(solid)  = (50 - 40)/(60 - 40) = 10/20 = 0.50",
                 "in 2 kg of alloy: 1.00 kg liquid and 1.00 kg solid, of 40 % and 60 % Ni"),
            why("The lever rule is a balance, not a formula to memorise: the amount of a phase is "
                "inversely proportional to its distance from the alloy composition, exactly like a "
                "see-saw. The phase whose composition is far from C0 must be present in small amount, "
                "which is why the answer for the 50 % alloy comes out equal - it sits exactly in the "
                "middle.",
                "Lever rule એ સંતુલન છે, યાદ રાખવાનું સૂત્ર નહીં: phase ની માત્રા alloy ના composition થી "
                "તેના અંતરની વ્યસ્ત પ્રમાણમાં હોય છે, જેમ સીસોડિયું. જે phase નું composition C0 થી દૂર "
                "હોય તેની માત્રા ઓછી જ હોય, અને તેથી જ 50 % alloy નો જવાબ સરખો આવે - તે બરાબર વચ્ચે બેસે "
                "છે."),
            check("A quick check that catches most mistakes: at the liquidus, W(liquid) must be 1; at "
                  "the solidus it must be 0. Put C0 = C_l and C0 = C_s in your own formula and see.",
                  "મોટા ભાગની ભૂલ પકડતી ઝડપી ચકાસણી: liquidus પર W(liquid) = 1 થવું જોઈએ; solidus પર 0. "
                  "તમારા સૂત્રમાં C0 = C_l અને C0 = C_s મૂકી જુઓ."),
            diagram="u2_cuni",
        ),
        card(
            "Lead-tin: the eutectic diagram",
            "Lead-tin: eutectic diagram અને તેનાં બિંદુઓ",
            p("Lead and tin fail the size and structure tests, so each dissolves only a little of the "
              "other: at 183 C lead takes 19.2 % tin and tin takes 2.5 % lead. The two liquidus "
              "branches therefore meet at a single point - the <b>eutectic point</b>, 61.9 % tin and "
              "183 C - where the liquid freezes all at once into the two solid solutions, α and β. An "
              "alloy of eutectic composition has no freezing range at all: it is liquid at 184 C and "
              "solid at 182 C, which is exactly what a solder or a type metal wants.",
              "Lead અને tin size તથા structure ની કસોટીમાં ઊતરતા નથી, તેથી દરેક થોડું જ બીજાનું ઓગાળે "
              "છે: 183 C પર lead 19.2 % tin લે અને tin 2.5 % lead લે. તેથી બંને liquidus શાખા એક જ "
              "બિંદુએ મળે - <b>eutectic point</b>, 61.9 % tin અને 183 C - જ્યાં પ્રવાહી એકસાથે બે solid "
              "solution α અને β માં થીજે છે. Eutectic composition ના alloy ને freezing range જ નથી: 184 "
              "C પર પ્રવાહી અને 182 C પર ઘન, જે solder કે type metal ને બરાબર જોઈએ તેવું છે."),
            table([tr("Point or line", "બિંદુ કે રેખા"), tr("Composition", "Composition"),
                   tr("Temperature", "Temperature"), tr("What happens", "શું થાય")],
                  [[tr("Melting point of Pb", "Pb નું ગલનબિંદુ"), tr("0 % Sn", "0 % Sn"),
                    tr("327 C", "327 C"), tr("pure lead melts", "શુદ્ધ lead પીગળે")],
                   [tr("Melting point of Sn", "Sn નું ગલનબિંદુ"), tr("100 % Sn", "100 % Sn"),
                    tr("232 C", "232 C"), tr("pure tin melts", "શુદ્ધ tin પીગળે")],
                   [tr("Eutectic point", "Eutectic point"), tr("61.9 % Sn", "61.9 % Sn"),
                    tr("183 C", "183 C"), tr("L -> α + β at one temperature", "L -> α + β એક જ temperature પર")],
                   [tr("Max Sn in α", "α માં વધુમાં વધુ Sn"), tr("19.2 % Sn", "19.2 % Sn"),
                    tr("183 C", "183 C"), tr("the lead-rich solid solution", "lead-વધુ solid solution")],
                   [tr("Max Pb in β", "β માં વધુમાં વધુ Pb"), tr("97.5 % Sn", "97.5 % Sn"),
                    tr("183 C", "183 C"), tr("the tin-rich solid solution", "tin-વધુ solid solution")]]),
            math("40 % Sn alloy at 200 C:  C_l = 55 % Sn,  C_alpha = 17 % Sn",
                 "W(liquid) = (40 - 17)/(55 - 17) = 23/38 = 0.60",
                 "W(alpha)  = (55 - 40)/(55 - 17) = 15/38 = 0.40",
                 "",
                 "cool it further to 183 C: the last liquid is 61.9 % Sn",
                 "the eutectic reaction: L(61.9) -> alpha(19.2) + beta(97.5)   F = 0"),
            why("Every alloy to the left of the eutectic is <b>hypoeutectic</b> and shows primary α "
                "before the eutectic freezes; every alloy to the right is <b>hypereutectic</b> and "
                "shows primary β. The eutectic alloy shows only the two-phase mixture, which is why its "
                "micrograph looks like a fine striped pattern.",
                "Eutectic ની ડાબી બાજુનું દરેક alloy <b>hypoeutectic</b> છે અને eutectic થીજે તે પહેલાં "
                "primary α દેખાય; જમણી બાજુનું દરેક <b>hypereutectic</b> છે અને primary β દેખાય. Eutectic "
                "alloy માં ફક્ત બે-phase મિશ્રણ દેખાય, તેથી તેનું micrograph નાની પટ્ટીઓ જેવું લાગે."),
            diagram="u2_pbsn",
        ),
    ],
})
