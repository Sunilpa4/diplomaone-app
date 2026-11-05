"""DI01000181 Unit 2, part A: sections 2.1 and 2.2 - phases, the phase rule, solidification, grains."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from subject_DI01000181 import tr  # noqa: E402
from content_DI01000181_lib import (p, h4, table, math, eq, why, check, pit, card,  # noqa: E402
                                    ul, ol)

NOTES_A = []

NOTES_A.append({
    "title": tr("2.1 Phase, component and the phase rule",
                "2.1 Phase, component અને phase rule"),
    "items": [
        card(
            "Phase, component and degrees of freedom",
            "Phase, component અને degrees of freedom",
            p("A <b>phase</b> is a part of the material that is the same everywhere in it: same "
              "crystal structure, same composition, and a boundary you could draw round it. Ice and "
              "water in one glass are two phases; a Cu-Ni solid solution is one phase however much "
              "nickel it holds. A <b>component</b> is the smallest set of chemical species needed to "
              "describe every phase present, and the <b>degrees of freedom</b> tell you how many of "
              "the variables (temperature, pressure, composition) you may change without losing a "
              "phase.",
              "કોઈ સામગ્રીનો જે ભાગ બધે એકસરખો હોય તે <b>phase</b> છે: એક જ crystal structure, એક જ "
              "composition, અને તેની આસપાસ સીમા દોરી શકાય. એક ગ્લાસમાં ice અને water બે phase છે; Cu-Ni "
              "solid solution માં nickel ગમે તેટલું હોય તો પણ તે એક જ phase છે. <b>Component</b> એ "
              "હાજર બધા phase વર્ણવવા માટે જરૂરી લઘુતમ chemical species છે, અને <b>degrees of "
              "freedom</b> કહે છે કે phase ગુમાવ્યા વગર તમે temperature, pressure અને composition "
              "માંથી કેટલા બદલી શકો."),
            math("Gibbs phase rule:   F = C - P + 2",
                 "every diagram in this subject is drawn at 1 atmosphere, so the pressure is fixed:",
                 "condensed phase rule:   F = C - P + 1",
                 "",
                 "pure iron, 1450 C (austenite only):        C=1 P=1 -> F = 1-1+1 = 1",
                 "pure iron at 1538 C (solid + liquid):      C=1 P=2 -> F = 1-2+1 = 0",
                 "Pb-Sn eutectic, 183 C (L + alpha + beta):  C=2 P=3 -> F = 2-3+1 = 0",
                 "40 % Sn at 200 C (alpha + liquid):         C=2 P=2 -> F = 2-2+1 = 1"),
            why("F = 0 means the point is <b>invariant</b>: the eutectic of lead-tin freezes at one "
                "temperature and one composition and you cannot move either without losing a phase. "
                "F = 1 means you may pick the temperature and the compositions then follow the two "
                "boundaries of the field - which is exactly what a tie line does.",
                "F = 0 એટલે બિંદુ <b>invariant</b> છે: lead-tin નું eutectic એક જ temperature અને એક જ "
                "composition પર થીજે છે, અને phase ગુમાવ્યા વગર એમાંથી એક પણ બદલી શકાતું નથી. F = 1 એટલે "
                "તમે temperature પસંદ કરી શકો અને પછી composition field ની બે સીમાં પર ચાલે - tie line "
                "બરાબર એ જ કરે છે."),
            table([tr("Phase in steel", "સ્ટીલમાં phase"), tr("Structure", "રચના"),
                   tr("Carbon it holds", "કાર્બનની માત્રા"), tr("Nature", "સ્વભાવ")],
                  [[tr("Ferrite, α", "Ferrite, α"), tr("BCC iron", "BCC iron"),
                    tr("0.02 % at 727 C", "727 C પર 0.02 %"), tr("soft and ductile", "નરમ અને ductile")],
                   [tr("Austenite, γ", "Austenite, γ"), tr("FCC iron", "FCC iron"),
                    tr("2.14 % at 1147 C", "1147 C પર 2.14 %"), tr("ductile, non-magnetic", "ductile, non-magnetic (બિન-ચુંબકીય)")],
                   [tr("Cementite, Fe3C", "Cementite, Fe3C"), tr("orthorhombic compound", "orthorhombic compound (સંયોજન)"),
                    tr("6.67 %", "6.67 %"), tr("very hard and brittle", "ખૂબ સખત અને ભંગુર")],
                   [tr("Pearlite", "Pearlite"), tr("lamellae of α + Fe3C", "α + Fe3C ની lamellae"),
                    tr("0.8 %", "0.8 %"), tr("the eutectoid mixture", "eutectoid મિશ્રણ")]]),
            check("Count the phases with a microscope, not with the formula sheet: the formula only "
                  "counts what is there. Two phases that look alike but have different compositions "
                  "are still two phases.",
                  "Phase ગણવા માટે સૂત્ર નહીં, microscope જુઓ: સૂત્ર ફક્ત જે હાજર છે તે ગણે છે. બે phase "
                  "દેખાવમાં સરખા પણ composition જુદું હોય તો પણ તે બે phase જ છે."),
            diagram=None,
        ),
        card(
            "Cooling curves: what a foundryman reads off them",
            "Cooling curves: ફાઉન્ડ્રીવાળો તેમાંથી શું વાંચે છે",
            p("Pour a metal into a mould, put a thermocouple in it and plot temperature against time. "
              "A <b>pure metal</b> cools in a straight line until it reaches its freezing point, then "
              "the curve goes flat: the latent heat of fusion is coming out as fast as the mould takes "
              "heat away, so the temperature does not fall until every atom has solidified. An "
              "<b>alloy</b> freezes over a range - the liquidus where the first solid appears and the "
              "solidus where the last liquid goes - so the curve only changes slope, and the slushy "
              "band in between is the <b>mushy zone</b>.",
              "Mould માં ધાતુ રેડો, તેમાં thermocouple નાખો અને time સામે temperature દોરો. "
              "<b>Pure metal</b> ગલનબિંદુ સુધી સીધી રેખામાં ઠંડું થાય, પછી રેખા સપાટ થઈ જાય: latent heat "
              "of fusion એટલી ઝડપથી બહાર નીકળે છે જેટલી ઝડપથી mould ગરમી લે છે, તેથી બધું ઘન ન થાય ત્યાં "
              "સુધી temperature ઘટતું નથી. <b>Alloy</b> એક range માં થીજે છે - liquidus જ્યાં પ્રથમ ઘન "
              "દેખાય અને solidus જ્યાં છેલ્લું પ્રવાહી જાય - તેથી રેખા ફક્ત ઢાળ બદલે છે, અને વચ્ચેનો "
              "લપટાવાળો પટ્ટો <b>mushy zone</b> છે."),
            math("latent heat released in time dt:  dQ = m Lf",
                 "held flat while the mould removes heat at q W:  t_arrest = m Lf / q",
                 "",
                 "example: 2 kg of iron, Lf = 247 kJ/kg, mould takes 500 W",
                 "t_arrest = 2 x 247000 / 500 = 988 s = 16.5 min of flat curve",
                 "",
                 "alloy freezing range = T_liquidus - T_solidus",
                 "the 70/30 alloy of figure: 1500 - 1380 = 120 C of mushy zone"),
            why("The flat part is the melting point measured from outside; the length of the flat part "
                "is the latent heat divided by the rate at which the mould removes heat. That is why a "
                "thin casting freezes quickly and a heavy section keeps its heat - and why the heavy "
                "section is the one that ends up with shrinkage porosity.",
                "સપાટ ભાગ એ બહારથી માપેલું ગલનબિંદુ છે; સપાટ ભાગની લંબાઈ એ latent heat ભાગ્યા mould "
                "ગરમી લે તેવા દર જેટલી છે. તેથી પાતળું casting જલદી થીજે છે અને જાડો ભાગ ગરમી રાખે છે - "
                "અને તેથી જ જાડા ભાગમાં shrinkage porosity રહી જાય છે."),
            pit("A small dip below the freezing point before the flat part is <b>undercooling</b>, not "
                "a lower melting point: the metal has to be pushed below its freezing point before "
                "nuclei form, and the temperature then jumps back up as they grow (recalescence). Read "
                "the flat part, not the dip.",
                "સપાટ ભાગ પહેલાં ગલનબિંદુથી થોડું નીચે જવું તે <b>undercooling</b> છે, ગલનબિંદુ નીચું "
                "થયું નથી: nuclei બનતા પહેલાં ધાતુને તેના ગલનબિંદુથી નીચે ધકેલવી પડે છે, અને પછી nuclei "
                "વધતાં temperature પાછું ઉપર કૂદે છે (recalescence). સપાટ ભાગ વાંચો, ખાડો નહીં."),
            diagram="u2_coolcurve",
        ),
    ],
})

NOTES_A.append({
    "title": tr("2.2 Solidification, grain structure and grain size",
                "2.2 Solidification, grain structure અને grain size"),
    "items": [
        card(
            "Nucleation, dendrites and the three zones of an ingot",
            "Nucleation, dendrites અને ingot ના ત્રણ zone",
            p("Solidification needs somewhere to start. <b>Homogeneous nucleation</b> is a cluster of "
              "atoms forming on its own in the melt; it needs a large undercooling because the new "
              "surface costs energy. <b>Heterogeneous nucleation</b> uses a ready-made surface - the "
              "mould wall, an oxide skin, or a deliberately added particle - and needs only a small "
              "undercooling, so it is what actually happens in a foundry. Once a nucleus exists it "
              "grows fastest along the directions where it can reject its latent heat, which gives the "
              "tree-shaped <b>dendrite</b>; the arms of neighbouring dendrites meet and leave a "
              "<b>grain boundary</b>.",
              "ઘન થવા માટે શરૂઆતનું સ્થળ જોઈએ. <b>Homogeneous nucleation</b> એ પ્રવાહીમાં પોતાની જાતે "
              "બનતું atoms નું ટોળું છે; નવી surface ઊર્જા માંગે છે તેથી તેને ઘણું undercooling જોઈએ. "
              "<b>Heterogeneous nucleation</b> તૈયાર surface વાપરે છે - mould ની દીવાલ, oxide નો પડ, કે "
              "જાણીને ઉમેરેલો કણ - અને થોડું જ undercooling માંગે છે, તેથી ફાઉન્ડ્રીમાં ખરેખર એ જ બને "
              "છે. Nucleus બન્યા પછી જ્યાં latent heat સહેલાઈથી નીકળે તે દિશામાં તે સૌથી ઝડપથી વધે છે, "
              "જેનાથી ઝાડ જેવું <b>dendrite</b> બને છે; પાડોશી dendrite ના ડાળા મળે ત્યાં <b>grain "
              "boundary</b> રહી જાય છે."),
            math("critical radius of a nucleus:  r* = 2 gamma Tm / (L dT)",
                 "energy barrier:  dG* = 16 pi gamma^3 Tm^2 / (3 L^2 dT^2)",
                 "",
                 "iron: gamma = 0.2 J/m2, Tm = 1811 K, L = 1.9e9 J/m3, dT = 100 K",
                 "r* = 2 x 0.2 x 1811 / (1.9e9 x 100) = 3.8e-9 m = 3.8 nm",
                 "dT = 200 K -> r* = 1.9 nm: double the undercooling, half the nucleus"),
            table([tr("Zone", "Zone"), tr("Where it freezes", "ક્યાં થીજે"),
                   tr("Grains", "Grains"), tr("Why", "કેમ")],
                  [[tr("Chill zone", "Chill zone"), tr("against the mould wall", "mould ની દીવાલ પાસે"),
                    tr("fine, equiaxed", "નાના, equiaxed"),
                    tr("wall nucleates many grains at once", "દીવાલ એકસાથે ઘણા grains બનાવે")],
                   [tr("Columnar zone", "Columnar zone"), tr("next to it, growing inwards", "તેની બાજુમાં, અંદર તરફ વધતા"),
                    tr("long, parallel", "લાંબા, સમાંતર"),
                    tr("heat leaves through the wall, so they grow that way", "ગરમી દીવાલ તરફ જાય તેથી તે દિશામાં વધે")],
                   [tr("Equiaxed centre", "Equiaxed centre"), tr("last, in the hot middle", "છેલ્લે, ગરમ વચ્ચે"),
                    tr("coarse, random", "જાડા, અવ્યવસ્થિત"),
                    tr("slow cooling, few nuclei left", "ધીમું ઠંડું, ઓછા nuclei બચ્યા")]]),
            pit("The three zones are not always there. A thin section or a well-inoculated alloy may be "
                "all equiaxed, and a pure metal poured into a cold metal mould may be almost all "
                "columnar. The zones are a description of the heat flow, not a rule.",
                "ત્રણ zone હંમેશા હોતા નથી. પાતળો ભાગ કે સારી રીતે inoculated alloy આખો equiaxed હોઈ "
                "શકે, અને ઠંડા metal mould માં રેડેલી શુદ્ધ ધાતુ લગભગ આખી columnar હોઈ શકે. Zone એ ગરમીના "
                "પ્રવાહનું વર્ણન છે, નિયમ નહીં."),
            diagram="u2_ingot",
        ),
        card(
            "Casting defects that come from solidification",
            "Solidification થી થતી casting defects",
            p("Almost every casting defect is a consequence of one fact: the metal shrinks when it "
              "freezes, and it freezes from the outside in. The last liquid is trapped somewhere "
              "inside, and when it finally freezes there is nothing left to fill the hole it leaves. "
              "A <b>shrinkage cavity</b> (pipe) forms where the feeder could not reach, <b>porosity</b> "
              "where gas or shrinkage is spread out as small holes, <b>segregation</b> where alloying "
              "elements are pushed ahead of the growing dendrites, and <b>hot tears</b> where a "
              "contracting skin is pulled apart while it is still weak.",
              "લગભગ દરેક casting defect એક જ હકીકતમાંથી આવે છે: ધાતુ થીજતી વખતે સંકોચાય છે, અને બહારથી "
              "અંદર તરફ થીજે છે. છેલ્લું પ્રવાહી અંદર ક્યાંક ફસાય છે, અને જ્યારે તે થીજે ત્યારે તે જગ્યા "
              "ભરવા માટે કંઈ બચતું નથી. Feeder પહોંચી શકે તેમ ન હોય ત્યાં <b>shrinkage cavity</b> "
              "(pipe) બને, gas કે shrinkage નાના છિદ્રો સ્વરૂપે ફેલાય ત્યાં <b>porosity</b>, વધતા "
              "dendrites આગળ alloying elements ધકેલાય ત્યાં <b>segregation</b>, અને સંકોચાતી skin હજી "
              "નરમ હોય ત્યારે ફાટે તો <b>hot tear</b> બને."),
            math("linear contraction of iron on freezing ~ 1 %, solid contraction to room ~ 1 %",
                 "shrinkage allowance left on a pattern: 10 mm/m for cast iron, 20 mm/m for steel",
                 "",
                 "a 1 m cast-iron pattern is made 1.010 m long",
                 "riser volume must feed the shrinkage of the section it feeds"),
            ul((tr("Feed the hot spot: put the riser on the thickest section, not on the thin one.",
                   "Hot spot ને feed કરો: riser જાડા ભાગ પર મૂકો, પાતળા પર નહીં.")),
               (tr("Directional solidification: chill the far end so the metal freezes towards the riser.",
                   "Directional solidification: દૂરનો છેડો ઠંડો કરો જેથી ધાતુ riser તરફ થીજે.")),
               (tr("Degas the melt and inoculate it: less gas, more nuclei, finer grains, less segregation.",
                   "Melt ને degas અને inoculate કરો: ઓછો gas, વધુ nuclei, નાના grains, ઓછું segregation."))),
            diagram=None,
        ),
        card(
            "Grain size sets the strength: Hall-Petch",
            "Grain size તાકાત નક્કી કરે: Hall-Petch",
            p("A dislocation gliding along its slip plane stops at a grain boundary, because the next "
              "grain has its lattice at a different angle. The pile-up of dislocations at the boundary "
              "raises the stress there until the neighbouring grain yields too. Make the grains "
              "smaller and there are more boundaries, so the pile-ups are shorter and a larger stress "
              "is needed to push the slip across: this is the <b>Hall-Petch</b> relation. It is the "
              "one strengthening method that also raises toughness, which is why normalising and grain "
              "refining are so common.",
              "Slip plane પર સરતું dislocation grain boundary પર અટકે છે, કારણ કે પછીના grain નું "
              "lattice જુદા ખૂણે છે. Boundary પર dislocations નું થતું ઢગલો ત્યાં stress વધારે છે જ્યાં "
              "સુધી પાડોશી grain પણ yield ન થાય. Grains નાના કરો તો boundaries વધે, ઢગલા ટૂંકા રહે અને "
              "slip પસાર કરવા મોટું stress જોઈએ: આ <b>Hall-Petch</b> સંબંધ છે. તાકાત વધારવાની આ એક જ "
              "રીત છે જે toughness પણ વધારે છે, તેથી normalising અને grain refining ખૂબ વપરાય છે."),
            math("sigma_y = sigma_0 + k d^(-1/2)      sigma_0 = 100 MPa, k = 23.4 MPa mm^0.5",
                 "",
                 "d = 0.0625 mm -> d^-1/2 = 4.00 -> sigma_y = 100 + 93.6 = 194 MPa",
                 "d = 0.0156 mm -> d^-1/2 = 8.00 -> sigma_y = 100 + 187.2 = 287 MPa",
                 "half the grain size, + 93 MPa on the yield strength"),
            math("ASTM grain size number:  n = 2^(N-1) grains per square inch at 100x",
                 "N = 6 -> n = 32 -> d = 25.4/(100 x sqrt(32)) = 0.045 mm",
                 "N = 10 -> n = 512 -> d = 25.4/(100 x sqrt(512)) = 0.011 mm"),
            check("The relation is a straight line only when plotted against d^(-1/2). Plot against d "
                  "itself and it curves, which is exactly what a student loses marks for.",
                  "આ સંબંધ સીધી રેખા ત્યારે જ બને જ્યારે d^(-1/2) સામે દોરો. d સામે દોરો તો વળાંક "
                  "આવે, અને વિદ્યાર્થી ત્યાં જ ગુણ ગુમાવે છે."),
            diagram="u2_hallpetch",
        ),
    ],
})
