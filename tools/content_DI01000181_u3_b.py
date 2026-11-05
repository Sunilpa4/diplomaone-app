"""DI01000181 Unit 3, part B: sections 3.3 and 3.4 - cast irons, copper and its alloys."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from subject_DI01000181 import tr  # noqa: E402
from content_DI01000181_lib import (p, h4, table, math, eq, why, check, pit, card,  # noqa: E402
                                    ul, ol)

NOTES_B = []

NOTES_B.append({
    "title": tr("3.3 Cast irons: the shape of the graphite decides everything",
                "3.3 Cast irons: graphite નો આકાર બધું નક્કી કરે"),
    "items": [
        card(
            "Four cast irons and what each one is good at",
            "ચાર cast irons અને દરેક શેમાં સારું છે",
            p("A cast iron holds 2.5 to 4 % carbon and 1 to 3 % silicon, and that is far more carbon "
              "than iron can keep in solution - so the carbon comes out of the melt as either "
              "<b>graphite</b> or <b>cementite</b>. Which one it becomes, and what shape the graphite "
              "takes, decides the properties completely. <b>Grey iron</b> cools slowly in a sand mould "
              "and its graphite forms flakes: cheap, easy to cast, an excellent damper, but weak in "
              "tension because every flake is a crack. <b>White iron</b> cools fast or is low in "
              "silicon, keeps its carbon as cementite, and is so hard it can only be ground. "
              "<b>Malleable iron</b> is white iron that has been annealed until the cementite breaks "
              "down into rosettes of temper carbon, and <b>ductile (SG) iron</b> is grey iron whose "
              "graphite was made to grow as nodules by adding a little magnesium.",
              "Cast iron માં 2.5 થી 4 % carbon અને 1 થી 3 % silicon હોય છે, જે iron ઓગાળી શકે તેનાથી ઘણું "
              "વધુ છે - તેથી carbon પ્રવાહીમાંથી <b>graphite</b> કે <b>cementite</b> સ્વરૂપે બહાર નીકળે છે. "
              "કયું બને અને graphite નો આકાર શો હોય તે ગુણધર્મો સંપૂર્ણ નક્કી કરે છે. <b>Grey iron</b> રેતીના "
              "mould માં ધીમે ઠંડું થાય તેથી તેનું graphite flake સ્વરૂપે બને: સસ્તું, સહેલાઈથી cast થાય, "
              "damping ઉત્તમ, પણ tension માં નબળું કારણ કે દરેક flake એક તિરાડ છે. <b>White iron</b> "
              "ઝડપથી ઠંડું થાય કે silicon ઓછું હોય, carbon cementite સ્વરૂપે રાખે, અને એટલું સખત બને કે "
              "ફક્ત ઘસી શકાય. <b>Malleable iron</b> એ white iron છે જેને anneal કરીને cementite ને temper "
              "carbon ના rosettes માં તોડ્યું છે, અને <b>ductile (SG) iron</b> એ grey iron છે જેનું "
              "graphite થોડું magnesium ઉમેરીને nodules સ્વરૂપે વધાવ્યું છે."),
            table([tr("Cast iron", "Cast iron"), tr("C %", "C %"), tr("Graphite", "Graphite"),
                   tr("UTS (MPa)", "UTS (MPa)"), tr("Elongation", "Elongation"), tr("Used for", "ક્યાં વપરાય")],
                  [[tr("Grey", "Grey"), tr("3.2 - 3.6", "3.2 - 3.6"), tr("flakes", "flakes"),
                    tr("150 - 300", "150 - 300"), tr("0.5 %", "0.5 %"),
                    tr("machine beds, housings, covers", "machine beds, housings, covers (મશીન બેડ)")],
                   [tr("White", "White"), tr("2.5 - 3.5", "2.5 - 3.5"), tr("none, all cementite", "કંઈ નહીં, બધું cementite"),
                    tr("300 - 500", "300 - 500"), tr("nil", "nil"),
                    tr("mill liners, plough shares, rolls", "mill liners, plough shares, rolls (ઘસાતા ભાગ)")],
                   [tr("Malleable", "Malleable"), tr("2.2 - 3.0", "2.2 - 3.0"), tr("temper carbon rosettes", "temper carbon ના rosettes"),
                    tr("350 - 450", "350 - 450"), tr("5 - 10 %", "5 - 10 %"),
                    tr("pipe fittings, brackets, hubs", "pipe fittings, brackets, hubs (પાઇપ)")],
                   [tr("Ductile (SG)", "Ductile (SG)"), tr("3.4 - 3.8", "3.4 - 3.8"), tr("nodules", "nodules"),
                    tr("400 - 600", "400 - 600"), tr("10 - 18 %", "10 - 18 %"),
                    tr("crankshafts, gears, pipe, wheels", "crankshafts, ગિયર, પાઇપ, wheels")]]),
            math("carbon equivalent:  CE = %C + (%Si + %P)/3",
                 "",
                 "grey iron C 3.4, Si 2.1, P 0.3:  CE = 3.4 + 2.4/3 = 4.20  (just below eutectic)",
                 "ductile iron C 3.6, Si 2.4:      CE = 3.6 + 2.4/3 = 4.40  (just above)",
                 "CE near 4.3 gives the best fluidity and the easiest casting"),
            why("Silicon does the same job as carbon: it is a graphitiser, pushing the carbon out of "
                "solution. That is why the carbon equivalent adds a third of the silicon - 1 % of "
                "silicon behaves like 0.33 % of carbon. Raise it too far and graphite forms before the "
                "metal freezes (kish graphite), which floats and leaves a rough surface.",
                "Silicon એ carbon જેવું જ કામ કરે: તે graphitiser છે, carbon ને solution માંથી બહાર "
                "ધકેલે. તેથી carbon equivalent માં silicon નો ત્રીજો ભાગ ઉમેરાય - 1 % silicon, 0.33 % "
                "carbon જેવું વર્તે. ઘણું વધારે કરો તો ધાતુ થીજે તે પહેલાં graphite બને (kish graphite), "
                "જે ઉપર તરે અને સપાટી ખરબચડી રાખે."),
            diagram="u3_ci",
        ),
        card(
            "Cast iron against steel, and why a machine bed is cast iron",
            "Cast iron સામે steel, અને machine bed cast iron કેમ હોય",
            p("The difference between the two is not just composition. A cast iron contains graphite "
              "flakes, and a flake is a free surface: it cannot carry tensile stress, it absorbs "
              "vibration as the two faces rub, and it holds oil so the surface stays lubricated. So "
              "cast iron is weak in tension, roughly three to four times stronger in compression, "
              "superb at damping and cheap to make into a complicated shape. Steel has no graphite, "
              "so it is equally strong in tension and compression, can be forged and welded, and "
              "takes shock without cracking.",
              "બંનેમાં ફરક ફક્ત composition નો નથી. Cast iron માં graphite flakes હોય છે, અને flake એટલે "
              "મુક્ત સપાટી: તે tensile stress ખેંચી શકતું નથી, બે સપાટી ઘસાતાં vibration શોષે છે, અને "
              "તેલ પકડી રાખે છે તેથી સપાટી lubricated રહે. તેથી cast iron tension માં નબળું, compression "
              "માં લગભગ ત્રણ-ચાર ગણું મજબૂત, damping માં ઉત્તમ અને ગૂંચવાડાભરી આકૃતિ બનાવવા સસ્તું છે. "
              "Steel માં graphite નથી, તેથી તે tension અને compression બંનેમાં સરખું મજબૂત, forge અને weld "
              "થઈ શકે, અને તણાવ સહન કરે પણ તૂટે નહીં."),
            table([tr("Point", "મુદ્દો"), tr("Cast iron", "Cast iron"), tr("Steel", "Steel")],
                  [[tr("Carbon", "Carbon"), tr("2.14 - 6.67 %", "2.14 - 6.67 %"), tr("0.02 - 2.14 %", "0.02 - 2.14 %")],
                   [tr("Tension against compression", "Tension સામે compression"),
                    tr("compression 3-4 times stronger", "compression 3-4 ગણું મજબૂત"),
                    tr("the same in both", "બંનેમાં સરખું")],
                   [tr("Damping", "Damping"), tr("excellent - graphite rubs", "ઉત્તમ - graphite ઘસાય"),
                    tr("poor, it rings", "નબળું, ઘંટડી જેવું વાગે")],
                   [tr("Forming", "Forming"), tr("casting only", "ફક્ત casting"),
                    tr("rolling, forging, welding, machining", "rolling, forging, welding, machining (આકાર આપવો)")],
                   [tr("Impact", "Impact"), tr("brittle, it cracks", "ભંગુર, તૂટે"),
                    tr("tough if the carbon is low", "carbon ઓછો હોય તો tough")],
                   [tr("Cost of a complex shape", "ગૂંચવાડાભરી આકૃતિનો ખર્ચ"),
                    tr("low - cast to shape, little machining", "ઓછો - આકારમાં cast, ઓછું machining"),
                    tr("high - needs forging and machining", "વધુ - forging અને machining જોઈએ")]]),
            math("grey iron: UTS 200 MPa in tension, 700 MPa in compression",
                 "steel C45: UTS 600 MPa in tension and 600 MPa in compression",
                 "damping capacity of grey iron is 5 to 10 times that of steel",
                 "",
                 "so a lathe bed is cast iron: it is loaded in compression, it must not vibrate,",
                 "and its shape is complicated - three reasons for the same answer"),
            check("If a question asks why a part is cast iron, look for compression, vibration or a "
                  "complicated shape. If it is loaded in tension or shock, the answer is steel.",
                  "કોઈ ભાગ cast iron કેમ છે તે પૂછે તો compression, vibration કે ગૂંચવાડાભરી આકૃતિ શોધો. "
                  "Tension કે shock નો ભાર હોય તો જવાબ steel છે."),
        ),
    ],
})

NOTES_B.append({
    "title": tr("3.4 Copper and its alloys", "3.4 Copper અને તેના alloys"),
    "items": [
        card(
            "Copper, brass, bronze and gunmetal",
            "Copper, brass, bronze અને gunmetal",
            p("Pure copper conducts better than any metal except silver - 385 W/(m K) and 100 % of "
              "the international annealed copper standard - but it is soft, 220 MPa, and expensive. "
              "Adding a second metal raises its strength and hardness and destroys part of that "
              "conductivity, because the dissolved atoms scatter the free electrons. With "
              "<b>zinc</b> it becomes <b>brass</b>: 70/30 is soft and ductile, ideal for deep drawing "
              "and radiator fins, while 60/40 is stronger and is extruded into rod for screws. With "
              "<b>tin</b> it becomes <b>bronze</b>, harder and very wear resistant, the classic "
              "bearing and bell metal. Adding both gives <b>gunmetal</b>, which resists sea water and "
              "is cast into pump bodies and valve chests.",
              "શુદ્ધ copper silver સિવાય દરેક ધાતુ કરતાં સારું વહન કરે - 385 W/(m K) અને international "
              "annealed copper standard ના 100 % - પણ તે નરમ, 220 MPa, અને મોંઘું છે. બીજી ધાતુ ઉમેરો તો "
              "તાકાત અને hardness વધે અને વાહકતાનો ભાગ નાશ પામે, કારણ કે ઓગળેલા atoms free electrons ને "
              "અથડાવે. <b>Zinc</b> સાથે તે <b>brass</b> બને: 70/30 નરમ અને ductile, deep drawing તથી "
              "radiator fins માટે ઉત્તમ, જ્યારે 60/40 વધુ મજબૂત અને screw માટે rod સ્વરૂપે extrude થાય. "
              "<b>Tin</b> સાથે તે <b>bronze</b> બને, વધુ સખત અને wear પ્રતિરોધક, પરંપરાગત bearing અને "
              "ઘંટડીની ધાતુ. બંને ઉમેરો તો <b>gunmetal</b> મળે, જે દરિયાના પાણી સામે ટકે અને pump bodies તથા "
              "valve chests માં cast થાય."),
            table([tr("Alloy", "Alloy"), tr("Composition", "Composition"), tr("UTS", "UTS"),
                   tr("Conductivity", "વાહકતા"), tr("Why it is chosen", "કેમ પસંદ થાય")],
                  [[tr("Copper", "Copper"), tr("99.9 % Cu", "99.9 % Cu"), tr("220 MPa", "220 MPa"),
                    tr("100 % IACS", "100 % IACS"), tr("busbar, winding, electrode", "busbar, winding, electrode (વીજ)")],
                   [tr("Brass 70/30", "Brass 70/30"), tr("Cu 70, Zn 30", "Cu 70, Zn 30"), tr("350 MPa", "350 MPa"),
                    tr("28 % IACS", "28 % IACS"), tr("deep drawing, cartridge, fins", "deep drawing, cartridge, fins (ખેંચાઈને બને)")],
                   [tr("Brass 60/40", "Brass 60/40"), tr("Cu 60, Zn 40", "Cu 60, Zn 40"), tr("420 MPa", "420 MPa"),
                    tr("26 % IACS", "26 % IACS"), tr("hot stamping, screws, rod", "hot stamping, screws, rod (બોલ્ટ)")],
                   [tr("Phosphor bronze", "Phosphor bronze"), tr("Cu 94.8, Sn 5, P 0.2", "Cu 94.8, Sn 5, P 0.2 (રચના)"),
                    tr("350 MPa", "350 MPa"), tr("12 % IACS", "12 % IACS"), tr("springs, bearings, gears", "સ્પ્રિંગ, bearings, gears")],
                   [tr("Gunmetal", "Gunmetal"), tr("Cu 88, Sn 10, Zn 2", "Cu 88, Sn 10, Zn 2"),
                    tr("280 MPa", "280 MPa"), tr("12 % IACS", "12 % IACS"), tr("valves, pumps, worms, bells", "valves, pumps, worms, bells (વાલ્વ, પંપ)")],
                   [tr("Cupronickel", "Cupronickel"), tr("Cu 70, Ni 30", "Cu 70, Ni 30"),
                    tr("380 MPa", "380 MPa"), tr("5 % IACS", "5 % IACS"), tr("condenser tubes, coinage", "condenser tubes, coinage (સિક્કા)")]]),
            math("conductivity of a metal falls as soon as anything is dissolved in it",
                 "Cu 100 % IACS -> brass 70/30 28 % -> bronze 13 % -> cupronickel 5 %",
                 "resistivity:  copper 1.7e-8,  brass 6.4e-8,  bronze 1.5e-7 ohm m",
                 "",
                 "%IACS = conductivity/5.8e7 x 100   (5.8e7 S/m is annealed copper)"),
            why("A pure metal conducts well because its electrons see a perfectly regular lattice. A "
                "zinc atom in copper is a different size, so the lattice around it is strained and the "
                "electron is scattered - and scattering is resistance. This is the same reason an "
                "alloy is stronger than a pure metal: the same distortion that stops a dislocation "
                "stops an electron.",
                "શુદ્ધ ધાતુ સારું વહન કરે કારણ કે તેના electrons ને સંપૂર્ણ નિયમિત lattice દેખાય. Copper "
                "માં zinc atom જુદા માપનો હોય તેથી તેની આસપાસનું lattice તણાય અને electron અથડાય - અને "
                "અથડામણ એ જ resistance. એ જ કારણે alloy શુદ્ધ ધાતુ કરતાં મજબૂત હોય છે: જે વિકૃતિ "
                "dislocation ને રોકે છે તે જ electron ને રોકે છે."),
            check("For an electrical question choose copper; for a bearing choose bronze; for a "
                  "casting in sea water choose gunmetal; for something to deep-draw choose 70/30 "
                  "brass. The alloy follows the duty, not the price list.",
                  "Electrical પ્રશ્નમાં copper પસંદ કરો; bearing માટે bronze; દરિયાના પાણીમાં casting માટે "
                  "gunmetal; deep drawing માટે 70/30 brass. Alloy કામ પ્રમાણે પસંદ થાય, ભાવ પ્રમાણે નહીં."),
            diagram="u3_cu",
        ),
    ],
})
