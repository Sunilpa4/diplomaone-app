"""DI01000181 Unit 1, part D: section 1.4 properties, the formulas, the viva and six numericals."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from subject_DI01000181 import tr  # noqa: E402
from content_DI01000181_lib import (p, h4, table, math, eq, why, check, pit, body,
                                    card)  # noqa: E402

NOTES_D = []

NOTES_D.append({
    "title": tr("1.4 Properties of materials", "1.4 સામગ્રીના ગુણધર્મો"),
    "items": [
        card(
            "Mechanical properties and the tensile test",
            "Mechanical ગુણધર્મો અને tensile test",
            p("Mechanical properties say how a material answers a force. The tensile test answers all "
              "of them at once: a standard specimen is pulled until it breaks, and the load and the "
              "extension are recorded. Stress is the load divided by the original area, strain is the "
              "extension divided by the original length, and the curve of one against the other gives "
              "the modulus, the yield strength, the ultimate strength and the ductility.",
              "Mechanical ગુણધર્મો કહે છે કે સામગ્રી બળને કેવો જવાબ આપે. Tensile test એ બધાનો જવાબ "
              "એકસાથે આપે: પ્રમાણભૂત specimen તૂટે ત્યાં સુધી ખેંચાય, અને load તથા લંબાઈ નોંધાય. "
              "Stress એ load ભાગ્યું મૂળ area, strain એ લંબાઈ ભાગ્યું મૂળ લંબાઈ, અને એક સામે બીજાનો "
              "વક્ર modulus, yield strength, ultimate strength અને ductility આપે."),
            math("stress sigma = P/A0        strain epsilon = dL/L0",
                 "elastic: sigma = E epsilon, so E = slope of the straight part (steel 200 GPa)",
                 "yield strength: the stress at which 0.2 % permanent strain is left behind",
                 "UTS: the highest stress on the curve (necking starts here)",
                 "ductility: % elongation = 100 (Lf - L0)/L0;  % reduction in area = 100 (A0 - Af)/A0",
                 "toughness = area under the stress-strain curve up to fracture"),
            table([tr("Property", "ગુણધર્મ"), tr("Meaning", "અર્થ"), tr("Mild steel value", "Mild steel મૂલ્ય")],
                  [[tr("elasticity", "elasticity"), tr("returns to shape after the load", "load હટે પછી આકાર પાછો"),
                    tr("E = 200 GPa", "E = 200 GPa")],
                   [tr("yield strength", "yield strength"), tr("first permanent deformation", "પહેલું કાયમી વિકાર"),
                    tr("250 MPa", "250 MPa")],
                   [tr("ultimate strength", "ultimate strength"), tr("highest stress before necking", "necking પહેલા સૌથી ઊંચો stress"),
                    tr("450 MPa", "450 MPa")],
                   [tr("ductility", "ductility"), tr("stretch before fracture", "તૂટતા પહેલા ખેંચાય"),
                    tr("25 % elongation", "25 % elongation")],
                   [tr("hardness", "hardness"), tr("resistance to indentation and wear", "દબાવટ અને ઘસારાનો અવરોધ"),
                    tr("150 HB", "150 HB")],
                   [tr("toughness", "toughness"), tr("energy absorbed before fracture", "તૂટતા પહેલા શોષાતી ઊર્જા"),
                    tr("high - it bends before it breaks", "ઊંચી - તૂટતા પહેલા વળે")]]),
            why("The straight part and the curved part answer two different questions. In the straight "
                "part the bonds stretch and spring back, so the slope is a property of the bond and not "
                "of the part. Past the yield point the atoms slide over one another and the change is "
                "permanent, so the shape and the grain size now matter as much as the material.",
                "સીધો ભાગ અને વળાંકવાળો ભાગ બે જુદા પ્રશ્નોના જવાબ આપે. સીધા ભાગમાં bonds ખેંચાય અને "
                "પાછા આવે, તેથી ઢોળાવ bond નું લક્ષણ છે, ભાગનું નહીં. Yield પછી atoms એકબીજા પર સરકે અને "
                "ફેરફાર કાયમી થાય, તેથી હવે આકાર અને grain size પણ સામગ્રી જેટલા જ મહત્વના બને."),
            check("Two numbers must agree with the curve you drew: the UTS is the highest point (not "
                  "the fracture point) and the fracture stress is usually lower than the UTS, because "
                  "the area has already necked down. If the drawn curve peaks at the fracture, it is "
                  "wrong.",
                  "તમે દોરેલા વક્ર સાથે બે આંકડા મળવા જોઈએ: UTS સૌથી ઊંચું બિંદુ છે (તૂટવાનું બિંદુ નહીં) "
                  "અને fracture stress સામાન્ય રીતે UTS કરતાં નીચો હોય, કારણ કે area ત્યાં સુધીમાં "
                  "necked થઈ ગઈ છે. દોરેલો વક્ર fracture પર ટોચે પહોંચે તો તે ખોટો છે."),
            pit("Quoting the UTS as the safe working stress. The allowable stress is the yield "
                "strength divided by a factor of safety, and for a brittle material it is the UTS "
                "divided by a much larger factor, because there is no yield to warn you.",
                    "UTS ને સલામત working stress તરીકે લખવું. Allowable stress એ yield strength ભાગ્યું "
                    "factor of safety છે, અને ભંગુર સામગ્રી માટે UTS ભાગ્યું ઘણો મોટો factor, કારણ કે "
                    "ચેતવણી આપે તેવું yield ત્યાં હોતું નથી."),
            diagram="u1_stress",
            syllabus_item="1.4",
        ),
        card(
            "Physical, chemical, electrical, electromagnetic and thermal properties",
            "Physical, chemical, electrical, electromagnetic અને thermal ગુણધર્મો",
            p("The other five property groups decide whether a material survives the place it is put "
              "in. Physical properties are density and melting point; chemical properties are "
              "corrosion and oxidation resistance; electrical properties are resistivity and "
              "conductivity; electromagnetic properties are permeability and coercivity, which decide "
              "motor and transformer cores; thermal properties are conductivity, expansion and "
              "specific heat.",
              "બાકીના પાંચ ગુણધર્મ સમૂહ નક્કી કરે કે સામગ્રી જ્યાં મૂકાય છે ત્યાં ટકશે કે નહીં. Physical "
              "ગુણધર્મ density અને ગલનબિંદુ છે; chemical ગુણધર્મ કાટ અને oxidation નો અવરોધ છે; "
              "electrical ગુણધર્મ resistivity અને conductivity છે; electromagnetic ગુણધર્મ permeability "
              "અને coercivity છે, જે motor તથા transformer ના core નક્કી કરે; thermal ગુણધર્મ "
              "conductivity, expansion અને specific heat છે."),
            math("thermal expansion: dL = alpha L0 dT     steel 12e-6/K, aluminium 23e-6/K",
                 "resistance: R = rho_e L/A       copper 1.7e-8, aluminium 2.8e-8 ohm m",
                 "heat to warm a part: Q = m c dT   steel 490, aluminium 900 J/(kg K)",
                 "conductivity: copper 385, aluminium 205, steel 50, rubber 0.15 W/(m K)"),
            table([tr("Group", "સમૂહ"), tr("Property", "ગુણધર્મ"), tr("Where it decides the design", "design માં ક્યાં નક્કી કરે")],
                  [[tr("Physical", "Physical"), tr("density, melting point", "density, ગલનબિંદુ"),
                    tr("weight of the part, safe working temperature", "ભાગનું વજન, સલામત temperature")],
                   [tr("Chemical", "Chemical"), tr("corrosion, oxidation resistance", "કાટ, oxidation અવરોધ"),
                    tr("pipe, tank, marine and food equipment", "pipe, tank, marine અને food equipment")],
                   [tr("Electrical", "Electrical"), tr("resistivity, conductivity", "resistivity, conductivity"),
                    tr("busbar, heating element, insulator", "busbar, heating element, insulator")],
                   [tr("Electromagnetic", "Electromagnetic"), tr("permeability, coercivity", "permeability, coercivity"),
                    tr("motor and transformer core, magnet", "motor અને transformer core, magnet")],
                   [tr("Thermal", "Thermal"), tr("conductivity, expansion, specific heat", "conductivity, expansion, specific heat"),
                    tr("heat exchanger, bearing clearance, welding distortion", "heat exchanger, bearing clearance, welding distortion")]]),
            eq("dL = alpha L0 dT", "R = rho_e L / A", "Q = m c dT"),
            why("Thermal expansion is the property that breaks parts quietly. Two materials bolted "
              "together at 25 C and heated to 200 C expand by different amounts, and the difference "
              "becomes a stress: steel against aluminium over 200 mm gives about 0.5 mm of mismatch, "
              "which is enough to bow a flange or crack a weld.",
                "Thermal expansion એ ગુણધર્મ છે જે ભાગોને ચૂપચાપ તોડે. 25 C પર બોલ્ટ કરેલી બે સામગ્રી "
                "200 C પર જુદા પ્રમાણમાં પ્રસરે, અને ફરક stress બને: 200 mm પર steel સામે aluminium "
                "લગભગ 0.5 mm ફરક આપે, જે flange વાળવા કે weld તોડવા પૂરતું છે."),
            check("Compare conductivities as ratios, not as numbers: copper conducts 385/50 = 7.7 "
                  "times better than steel and 385/0.15 = 2570 times better than rubber. The ratios "
                  "are what a designer uses; the absolute values only look impressive.",
                  "Conductivity ને ગુણોત્તર તરીકે સરખાવો, આંકડા તરીકે નહીં: copper steel કરતાં "
                  "385/50 = 7.7 ગણું અને rubber કરતાં 385/0.15 = 2570 ગણું સારું વહન કરે. ગુણોત્તર જ "
                  "designer વાપરે છે; નિરપેક્ષ મૂલ્યો ફક્ત પ્રભાવક લાગે."),
            pit("Treating resistivity as a single number for an alloy family. Adding 1 % of alloying "
                "element can double or triple the resistivity of copper, which is why a brass terminal "
                "runs hotter than a copper one of the same size.",
                "એલોય કુટુંબ માટે resistivity ને એક જ આંકડો ગણવો. 1 % alloying element ઉમેરવાથી copper "
                "નું resistivity બમણું કે ત્રણ ગણું થઈ શકે, તેથી જ સરખા માપનું brass terminal copper "
                "કરતાં વધુ ગરમ થાય."),
            diagram="u1_thermal",
            syllabus_item="1.4",
        ),
    ],
})

EQUATIONS = [
    {"title": tr("Crystal geometry", "Crystal ભૂમિતિ"),
     "items": [
         {"name": tr("BCC cell edge", "BCC cell edge"),
          "f": "a = 4R/sqrt(3) = 2.309 R",
          "terms": tr("Atoms touch along the body diagonal of the cube.",
                      "Atoms cube ના body diagonal પર સ્પર્શે છે.")},
         {"name": tr("FCC cell edge", "FCC cell edge"),
          "f": "a = 2 sqrt(2) R = 2.828 R",
          "terms": tr("Atoms touch along the face diagonal, the close-packed direction.",
                      "Atoms face diagonal પર સ્પર્શે છે, જે close-packed દિશા છે.")},
         {"name": tr("HCP ratio", "HCP ગુણોત્તર"),
          "f": "c/a = sqrt(8/3) = 1.633",
          "terms": tr("The ideal ratio for touching spheres; Mg and Zn are near it.",
                      "સ્પર્શતા ગોળા માટેનો આદર્શ ગુણોત્તર; Mg અને Zn તેની નજીક છે.")},
         {"name": tr("Packing fraction", "Packing fraction"),
          "f": "APF = n (4/3 pi R^3)/a^3 = 0.68 (BCC), 0.74 (FCC, HCP)",
          "terms": tr("Depends only on the stacking, not on the metal.",
                      "ફક્ત ગોઠવણી પર આધારે છે, ધાતુ પર નહીં.")},
     ]},
    {"title": tr("Density and atom count", "Density અને atoms ની ગણતરી"),
     "items": [
         {"name": tr("Atoms per cell", "cell દીઠ atoms"),
          "f": "n = 2 (BCC), 4 (FCC), 6 (HCP)",
          "terms": tr("Count corner atoms as 1/8 and face atoms as 1/2.",
                      "Corner atoms 1/8 અને face atoms 1/2 ગણો.")},
         {"name": tr("Density from the cell", "cell પરથી density"),
          "f": "rho = n A/(N_A a^3)",
          "terms": tr("A is the atomic mass in g/mol and a the cell edge in cm.",
                      "A એ g/mol માં atomic mass અને a એ cm માં cell edge છે.")},
         {"name": tr("Atoms per unit volume", "એકમ volume દીઠ atoms"),
          "f": "N_v = n/a^3",
          "terms": tr("Used for atoms per mm3 and for the number of interstitial sites.",
                      "mm3 દીઠ atoms અને interstitial sites ની સંખ્યા માટે વપરાય.")},
     ]},
    {"title": tr("Mechanical properties", "Mechanical ગુણધર્મો"),
     "items": [
         {"name": tr("Engineering stress", "Engineering stress"),
          "f": "sigma = P/A0",
          "terms": tr("Load divided by the original cross-section, not the current one.",
                      "Load ભાગ્યું મૂળ cross-section, હાલનું નહીં.")},
         {"name": tr("Engineering strain", "Engineering strain"),
          "f": "epsilon = dL/L0",
          "terms": tr("Extension divided by the original gauge length.",
                      "લંબાઈ ભાગ્યું મૂળ gauge length.")},
         {"name": tr("Hooke's law", "Hooke's law"),
          "f": "sigma = E epsilon,  E = 200 GPa for steel",
          "terms": tr("Holds only in the straight part of the curve.",
                      "વક્રના ફક્ત સીધા ભાગમાં લાગુ પડે.")},
         {"name": tr("Ductility", "Ductility"),
          "f": "% elongation = 100 (Lf - L0)/L0;  % RA = 100 (A0 - Af)/A0",
          "terms": tr("Two measures of the same thing: how far it stretched.",
                      "એક જ બાબતનાં બે માપ: કેટલું ખેંચાયું.")},
         {"name": tr("Allowable stress", "Allowable stress"),
          "f": "sigma_allow = sigma_yield / FOS",
          "terms": tr("FOS is 2 to 4 for ductile parts, 6 to 10 for brittle ones.",
                      "Ductile ભાગો માટે FOS 2 થી 4, ભંગુર માટે 6 થી 10.")},
     ]},
    {"title": tr("Thermal and electrical", "Thermal અને electrical"),
     "items": [
         {"name": tr("Thermal expansion", "Thermal expansion"),
          "f": "dL = alpha L0 dT",
          "terms": tr("Steel 12e-6/K, aluminium 23e-6/K, invar 1.2e-6/K.",
                      "આંકડા: steel 12e-6/K, aluminium 23e-6/K, invar 1.2e-6/K.")},
         {"name": tr("Resistance", "Resistance"),
          "f": "R = rho_e L/A",
          "terms": tr("Copper 1.7e-8, aluminium 2.8e-8, iron 1.0e-7 ohm m.",
                      "આંકડા: copper 1.7e-8, aluminium 2.8e-8, iron 1.0e-7 ohm m.")},
         {"name": tr("Heat to warm a part", "ભાગ ગરમ કરવાની ઉષ્મા"),
          "f": "Q = m c dT",
          "terms": tr("Steel 490, aluminium 900 J/(kg K).",
                      "આંકડા: steel 490, aluminium 900 J/(kg K).")},
     ]},
    {"title": tr("Selection and mixtures", "પસંદગી અને મિશ્રણ"),
     "items": [
         {"name": tr("Specific strength", "Specific strength"),
          "f": "specific strength = UTS/rho   (kN m/kg when UTS is in MPa)",
          "terms": tr("The design number for anything that moves.",
                      "હલતી કોઈપણ વસ્તુ માટેનો design આંકડો.")},
         {"name": tr("Composite density", "Composite ની density"),
          "f": "rho_c = f rho_f + (1 - f) rho_m",
          "terms": tr("Rule of mixtures by volume fraction f of fibre.",
                      "Fibre ના volume fraction f પ્રમાણે rule of mixtures.")},
         {"name": tr("Composite modulus", "Composite નું modulus"),
          "f": "E_c = f E_f + (1 - f) E_m",
          "terms": tr("For continuous fibres loaded along their length only.",
                      "ફક્ત લંબાઈ સાથે load થતા સતત fibres માટે.")},
     ]},
]

VIVA = [
    {"title": tr("Atoms and bonds", "Atoms અને bonds"),
     "items": [
         {"q": tr("Why does a metal conduct electricity while a ceramic does not?",
                  "ધાતુ current વહન કરે પણ ceramic ન કરે, કેમ?"),
          "a": tr("Because of where the electrons are. In a metal the outer electrons are shared by "
                  "the whole crystal and move freely, so a voltage drives a current. In a ceramic the "
                  "electrons are locked into ionic or covalent bonds and cannot move, so the material "
                  "is an insulator until the voltage is high enough to break the bond.",
                  "કારણ electrons ક્યાં છે તે છે. ધાતુમાં બહારના electrons આખા crystal ના હોય અને મુક્ત "
                  "હલે, તેથી voltage current ચલાવે. Ceramic માં electrons ionic કે covalent bonds માં "
                  "બંધ હોય અને હલી ન શકે, તેથી bond તોડવા પૂરતું voltage ન આવે ત્યાં સુધી તે અવાહક રહે.")},
         {"q": tr("Diamond and graphite are both pure carbon. Why is one the hardest material and the "
                  "other a lubricant?", "Diamond અને graphite બંને શુદ્ધ carbon છે. એક સૌથી સખત અને "
                  "બીજો lubricant કેમ?"),
          "a": tr("The bond is the same (covalent C-C), the arrangement is not. In diamond every "
                  "carbon is bonded to four others in three dimensions, so nothing can slide. In "
                  "graphite each carbon is bonded to three others in flat sheets that are held to one "
                  "another only by weak forces, so the sheets slide easily - which is what a "
                  "lubricant has to do.",
                  "Bond એ જ છે (covalent C-C), ગોઠવણી નથી. Diamond માં દરેક carbon ચાર બીજા સાથે "
                  "ત્રણ આયામોમાં જોડાયેલો છે, તેથી કંઈ સરકી ન શકે. Graphite માં દરેક carbon ત્રણ સાથે "
                  "સપાટ પાનમાં જોડાયેલો છે અને પાન એકબીજા સાથે ફક્ત નબળા બળથી જોડાય છે, તેથી પાન સહેલાઈથી "
                  "સરકે - lubricant એ જ કરવાનું હોય છે.")},
         {"q": tr("Which bond explains the low melting point of polythene?",
                  "Polythene નું નીચું ગલનબિંદુ કયું બંધન સમજાવે?"),
          "a": tr("Within the chain the bonds are strong covalent C-C bonds, but between the chains "
                  "there are only weak van der Waals and hydrogen forces. Melting means separating the "
                  "chains, not breaking them, so polythene softens near 110 C while the molecule "
                  "itself is stable to well above 300 C.",
                  "શૃંખલાની અંદર મજબૂત covalent C-C bonds છે, પણ શૃંખલાઓ વચ્ચે ફક્ત નબળા van der Waals "
                  "અને hydrogen બળ છે. ગલન એટલે શૃંખલાઓ અલગ થવી, તૂટવી નહીં, તેથી polythene 110 C "
                  "આસપાસ મૃદુ પડે જ્યારે molecule પોતે 300 C ઉપર પણ ટકે.")},
     ]},
    {"title": tr("Crystal structure", "Crystal રચના"),
     "items": [
         {"q": tr("Why is FCC iron able to dissolve far more carbon than BCC iron?",
                  "FCC iron BCC iron કરતાં ઘણું વધુ carbon કેમ ઓગાળે?"),
          "a": tr("Because of the holes. FCC packs 74 % of the space and leaves larger interstitial "
                  "holes, which take up to 2 % carbon by weight; BCC packs only 68 % but the holes are "
                  "smaller and distorted, so it takes about 0.025 %. That difference is the basis of "
                  "carburising and of the whole heat treatment.",
                  "કારણ છિદ્રો છે. FCC 74 % જગ્યા ભરે અને મોટા interstitial છિદ્રો રાખે, જે વજનથી 2 % "
                  "સુધી carbon લે; BCC ફક્ત 68 % ભરે પણ છિદ્રો નાનાં અને વિકૃત હોય, તેથી લગભગ 0.025 % "
                  "લે. એ ફરક જ carburising અને આખા heat treatment નો પાયો છે.")},
         {"q": tr("Why do FCC metals such as copper and aluminium bend so easily?",
                  "Copper અને aluminium જેવી FCC ધાતુઓ સહેલાઈથી વળે, કેમ?"),
          "a": tr("Close packing gives twelve slip systems on four planes, so a dislocation can move "
                  "in many directions without breaking a bond. HCP metals have only a few slip systems "
                  "and BCC fewer than FCC, which is why they are less ductile at room temperature.",
                  "Close packing ચાર planes પર બાર slip systems આપે, તેથી dislocation bond તોડ્યા વગર "
                  "ઘણી દિશામાં હલી શકે. HCP ધાતુઓમાં થોડા જ slip systems હોય અને BCC માં FCC કરતાં ઓછા, "
                  "તેથી તે room temperature પર ઓછી ductile હોય.")},
         {"q": tr("A density calculated from the unit cell is 0.3 % higher than the handbook value. "
                  "Explain.", "Unit cell પરથી ગણેલી density handbook મૂલ્ય કરતાં 0.3 % વધારે છે. "
                  "સમજાવો."),
          "a": tr("The cell model assumes a perfect crystal at zero kelvin with no defects. A real "
                  "metal has vacancies, dislocations and grain boundaries, and it is slightly expanded "
                  "at room temperature, so the measured density is a little lower. An agreement within "
                  "a few tenths of a per cent confirms the model.",
                  "Cell model શૂન્ય kelvin પર દોષરહિત crystal ધારે છે. સાચી ધાતુમાં vacancies, "
                  "dislocations અને grain boundaries હોય, અને room temperature પર તે થોડી પ્રસરેલી હોય, "
                  "તેથી માપેલી density થોડી ઓછી આવે. થોડા દશાંશ ટકાની સરખામણી model સાચું છે તે "
                  "સાબિત કરે.")},
     ]},
    {"title": tr("Properties and testing", "ગુણધર્મો અને પરીક્ષણ"),
     "items": [
         {"q": tr("What is the difference between strength and toughness?",
                  "Strength અને toughness માં શું ફરક છે?"),
          "a": tr("Strength is how large a stress the material can take; toughness is how much energy "
                  "it absorbs before it breaks. Glass is strong in compression and weak in toughness, "
                  "mild steel is less strong than hardened steel but far tougher, which is why springs "
                  "are not made of the hardest steel.",
                  "Strength એટલે સામગ્રી કેટલો stress સહી શકે; toughness એટલે તૂટતા પહેલા કેટલી ઊર્જા "
                  "શોષે. કાચ compression માં મજબૂત પણ toughness માં નબળો છે, mild steel hardened steel "
                  "કરતાં ઓછું મજબૂત પણ ઘણું tough છે, તેથી springs સૌથી સખત steel ના બનતા નથી.")},
         {"q": tr("Why does the test specimen have a standard shape and gauge length?",
                  "Test specimen નો આકાર અને gauge length પ્રમાણભૂત કેમ હોય?"),
          "a": tr("So that results can be compared. A thin specimen necks earlier and a short gauge "
                  "length hides the localised elongation; the standard 50 mm gauge and the specified "
                  "shoulder radius make the elongation and the UTS reproducible between laboratories.",
                  "જેથી પરિણામો સરખાવી શકાય. પાતળો specimen વહેલો necked થાય અને ટૂંકી gauge length "
                  "સ્થાનિક લંબાઈ છુપાવે; પ્રમાણભૂત 50 mm gauge અને નિર્દિષ્ટ shoulder radius elongation "
                  "તથા UTS ને પ્રયોગશાળાઓ વચ્ચે પુનરાવર્તનીય બનાવે.")},
         {"q": tr("Why is hardness measured on a polished surface?",
                  "Hardness પોલિશ કરેલી સપાટી પર કેમ મપાય?"),
          "a": tr("Because hardness is read from the size of an indentation a few tenths of a "
                  "millimetre across, and a rough or decarburised surface changes that size. The "
                  "specimen is polished so that the indenter meets the true material and the diameter "
                  "can be measured accurately.",
                  "કારણ કે hardness થોડા દશાંશ મિલીમીટરના indentation ના માપ પરથી વંચાય, અને ખરબચડી કે "
                  "decarburised સપાટી એ માપ બદલે. Indenter સાચી સામગ્રીને મળે અને વ્યાસ ચોક્કસ મપાય તે "
                  "માટે specimen પોલિશ કરાય.")},
     ]},
    {"title": tr("Choosing a material", "સામગ્રીની પસંદગી"),
     "items": [
         {"q": tr("Why is the specific strength used in transport and not the strength?",
                  "વાહનમાં strength નહીં, specific strength કેમ વપરાય?"),
          "a": tr("Because every kilogram saved also saves the fuel needed to move it and the force "
                  "needed to accelerate it. A material with a third of the strength but a fifth of the "
                  "density carries the same load at less weight, so strength per kilogram decides the "
                  "choice.",
                  "કારણ કે બચેલો દરેક કિલોગ્રામ તેને ખસેડવાનું fuel અને accelerate કરવાનું બળ પણ "
                  "બચાવે. ત્રીજા ભાગની strength પણ પાંચમા ભાગની density વાળી સામગ્રી એ જ load ઓછા "
                  "વજનમાં ઉપાડે, તેથી કિલોગ્રામ દીઠ strength પસંદગી નક્કી કરે.")},
         {"q": tr("Give one application where a low thermal conductivity is wanted and one where a "
                  "high one is wanted.", "એક ઉપયોગ કહો જ્યાં નીચી thermal conductivity જોઈએ અને એક "
                  "જ્યાં ઊંચી જોઈએ."),
          "a": tr("Low: the handle of a welding torch or a furnace door, where heat must not reach the "
                  "hand, and a refrigerator body, where heat must not leak in. High: the cylinder head "
                  "of an engine or the pot of a cooking vessel, where heat must be carried away or "
                  "spread quickly.",
                  "નીચી: welding torch નું હેન્ડલ કે furnace ના દરવાજા, જ્યાં ગરમી હાથ સુધી ન પહોંચવી "
                  "જોઈએ, અને ફ્રિજનું શરીર, જ્યાં ગરમી અંદર ન ઘૂસવી જોઈએ. ઊંચી: engine નું cylinder head કે "
                  "રાંધવાના પાત્રનું તળિયું, જ્યાં ગરમી ઝડપથી દૂર થવી કે ફેલાવવી જોઈએ.")},
         {"q": tr("Why can the same part be made from four different families of material?",
                  "એક જ ભાગ ચાર જુદા કુટુંબની સામગ્રીમાંથી કેમ બની શકે?"),
          "a": tr("Because the drawing fixes only the shape and the load, not the material. A gear "
                  "can be cut from steel for strength, sintered from ceramic for wear at high "
                  "temperature, moulded from nylon for quiet running, or laid up from carbon composite "
                  "for low inertia - and each answer is right for its own duty.",
                  "કારણ કે દોરડું ફક્ત આકાર અને load નક્કી કરે, સામગ્રી નહીં. ગિયર તાકાત માટે steel "
                  "માંથી કાપી શકાય, ઊંચા temperature પર ઘસારા માટે ceramic થી sinter કરી શકાય, શાંત "
                  "ચાલવા માટે nylon માંથી mould કરી શકાય, કે ઓછી inertia માટે carbon composite થી બનાવી "
                  "શકાય - અને દરેક જવાબ પોતાના કામ માટે સાચો છે.")},
     ]},
]

_PRACTICE = [
    ("Cell geometry and atoms per cubic millimetre of iron",
     "Iron ના cell ની ભૂમિતિ અને ઘન મિલીમીટર દીઠ atoms",
     "Iron at room temperature is BCC with a cell edge of 0.2866 nm and an atomic mass of 55.85. Find "
     "the atomic radius, the number of atoms in one cubic millimetre and the packing fraction, and say "
     "how far the calculated density is from the handbook value of 7.87 g/cm3.",
     "Room temperature પર iron BCC છે, cell edge 0.2866 nm અને atomic mass 55.85 છે. Atomic radius, "
     "એક ઘન મિલીમીટરમાં atoms ની સંખ્યા અને packing fraction શોધો, અને ગણેલી density handbook ના "
     "7.87 g/cm3 થી કેટલી દૂર છે તે કહો.",
     [h4("Step 1 - the atomic radius", "પગલું 1 - atomic radius"),
      math("BCC: atoms touch along the body diagonal, 4R = a sqrt(3)",
           "R = a sqrt(3)/4 = 0.2866 x 1.732/4 = 0.1241 nm"),
      h4("Step 2 - atoms per cubic millimetre", "પગલું 2 - ઘન મિલીમીટર દીઠ atoms"),
      math("a = 0.2866 nm = 2.866e-7 mm, so a^3 = 2.354e-20 mm3",
           "n = 2 atoms per cell",
           "N_v = 2/2.354e-20 = 8.50e19 atoms per mm3"),
      h4("Step 3 - packing fraction and density", "પગલું 3 - packing fraction અને density"),
      math("APF = pi sqrt(3)/8 = 0.680  (68 %)",
           "rho = 2 x 55.85/(6.022e23 x 2.354e-23) = 7.88 g/cm3",
           "against 7.87 measured: 0.1 % high"),
      eq("R = 0.124 nm,  N_v = 8.5e19 per mm3,  APF = 0.68,  rho = 7.88 g/cm3"),
      p("The calculation lands within a tenth of a per cent of the handbook value, which is the "
        "standard proof that the BCC assignment for room-temperature iron is right. The small excess "
        "comes from the ideal-crystal assumption: a real metal has vacancies and is slightly expanded.",
        "ગણતરી handbook મૂલ્યની એક દશાંશ ટકાની અંદર આવે છે, જે room-temperature iron માટે BCC "
        "સોંપણી સાચી છે તેનો પ્રમાણભૂત પુરાવો છે. થોડો વધારો આદર્શ-crystal ધારણામાંથી આવે: સાચી "
        "ધાતુમાં vacancies હોય અને તે થોડી પ્રસરેલી હોય."),
      check("exp of the two routes: from R, APF = 2 x (4/3 pi R^3)/a^3 gives the same 0.68, so the "
            "radius and the packing fraction are consistent.",
            "બે રસ્તા ચકાસો: R પરથી APF = 2 x (4/3 pi R^3)/a^3 પણ એ જ 0.68 આપે, તેથી radius અને "
            "packing fraction સુસંગત છે."),
      pit("Using a = 0.2866 nm with the radius formula of FCC. In BCC the contact is along the body "
          "diagonal (4R = a sqrt 3); using the FCC relation would give R = 0.101 nm and a wrong "
          "density.",
          "BCC માટે FCC નું radius સૂત્ર વાપરવું. BCC માં સ્પર્શ body diagonal પર છે (4R = a sqrt 3); "
          "FCC સંબંધ વાપરવાથી R = 0.101 nm આવે અને density ખોટી થાય.")],
     6),
    ("Density and radius of copper from its FCC cell",
     "FCC cell પરથી copper ની density અને radius",
     "Copper is FCC with a cell edge of 0.3615 nm and an atomic mass of 63.55. Calculate the density, "
     "the atomic radius and the number of atoms per cubic centimetre, and compare the density with the "
     "handbook value 8.96 g/cm3.",
     "Copper FCC છે, cell edge 0.3615 nm અને atomic mass 63.55 છે. Density, atomic radius અને ઘન "
     "સેન્ટીમીટર દીઠ atoms ગણો, અને density ને handbook ના 8.96 g/cm3 સાથે સરખાવો.",
     [h4("Step 1 - density", "પગલું 1 - density"),
      math("a = 0.3615 nm = 3.615e-8 cm,  a^3 = 4.725e-23 cm3,  n = 4",
           "rho = n A/(N_A a^3) = 4 x 63.55/(6.022e23 x 4.725e-23)",
           "    = 254.2/28.45 = 8.93 g/cm3"),
      h4("Step 2 - atomic radius", "પગલું 2 - atomic radius"),
      math("FCC: 4R = a sqrt(2)  ->  R = 3.615 x 1.4142/4 = 0.1278 nm"),
      h4("Step 3 - atoms per cubic centimetre", "પગલું 3 - ઘન સેન્ટીમીટર દીઠ atoms"),
      math("N_v = n/a^3 = 4/4.725e-23 = 8.47e22 atoms per cm3"),
      eq("rho = 8.93 g/cm3,  R = 0.128 nm,  N_v = 8.5e22 per cm3"),
      p("The density is 0.3 % below the handbook value, which is the usual agreement for a defect-free "
        "cell at room temperature. Copper and aluminium are both FCC, and that is why both are easy to "
        "draw into wire.",
        "Density handbook મૂલ્ય કરતાં 0.3 % નીચી આવે છે, જે room temperature પર દોષરહિત cell માટે "
        "સામાન્ય સરખામણી છે. Copper અને aluminium બંને FCC છે, તેથી જ બંનેને wire માં ખેંચવા સહેલા છે."),
      check("Compare with iron: copper 8.93 against iron 7.88, a ratio of 1.13, while their atomic "
            "masses are 63.55 against 55.85, a ratio of 1.14. The two ratios agree because the cell "
            "volumes per atom are similar.",
            "Iron સાથે સરખાવો: copper 8.93 સામે iron 7.88, ગુણોત્તર 1.13, જ્યારે atomic mass 63.55 "
            "સામે 55.85, ગુણોત્તર 1.14. બંને ગુણોત્તર મળે કારણ કે પ્રતિ atom cell volume સરખું છે."),
      pit("Forgetting that n = 4 for FCC. Using n = 2 halves the answer and makes copper 4.5 g/cm3, "
          "which is lighter than titanium - a result easy to spot if the order of magnitude is known.",
          "FCC માટે n = 4 છે તે ભૂલવું. n = 2 વાપરવાથી જવાબ અડધો થાય અને copper 4.5 g/cm3 આવે, જે "
          "titanium કરતાં પણ હલકું છે - order of magnitude ખબર હોય તો સહેલાઈથી પકડાય.")],
     7),
    ("Reading a tensile test",
     "Tensile test નું વાંચન",
     "A 12.5 mm diameter, 50 mm gauge length specimen of steel is tested. It yields at 40 kN, reaches "
     "a maximum load of 62 kN and breaks at a gauge length of 62.5 mm with a diameter at the neck of "
     "9.5 mm. Find the yield strength, the ultimate tensile strength, the percentage elongation and "
     "the percentage reduction in area.",
     "12.5 mm વ્યાસ અને 50 mm gauge length વાળો steel specimen test કરાય. 40 kN પર yield થાય, 62 kN "
     "પર મહત્તમ load આવે, અને 62.5 mm gauge length તથા neck પર 9.5 mm વ્યાસ સાથે તૂટે. Yield strength, "
     "ultimate tensile strength, ટકાવારી elongation અને ટકાવારી reduction in area શોધો.",
     [h4("Step 1 - the areas", "પગલું 1 - areas"),
      math("A0 = pi d0^2/4 = pi (12.5)^2/4 = 122.7 mm2",
           "Af = pi (9.5)^2/4 = 70.9 mm2"),
      h4("Step 2 - the strengths", "પગલું 2 - strengths"),
      math("sigma_y = 40 000/122.7 = 326 MPa",
           "sigma_UTS = 62 000/122.7 = 505 MPa"),
      h4("Step 3 - the ductility", "પગલું 3 - ductility"),
      math("elongation = 100 (62.5 - 50)/50 = 25 %",
           "reduction in area = 100 (122.7 - 70.9)/122.7 = 42.2 %"),
      eq("sigma_y = 326 MPa,  sigma_UTS = 505 MPa,  25 % elongation,  42 % RA"),
      p("Both strengths are above the textbook mild-steel values (250 and 450 MPa), so this is a "
        "medium-carbon or a work-hardened steel. An elongation of 25 % with a 42 % reduction in area "
        "marks a ductile material: it would have warned before breaking.",
        "બંને strength textbook માંના mild steel મૂલ્ય (250 અને 450 MPa) કરતાં ઊંચા છે, તેથી આ "
        "medium-carbon કે work-hardened steel છે. 25 % elongation અને 42 % reduction in area ductile "
        "સામગ્રી દર્શાવે: તે તૂટતા પહેલા ચેતવણી આપત."),
      check("The safety factor on yield: 326/250 is not the check, but sigma_y/1.5 = 217 MPa is the "
            "allowable stress for a ductile part with a factor of safety of 1.5.",
            "Yield પર safety factor: 326/250 ચકાસણી નથી, પણ sigma_y/1.5 = 217 MPa એ 1.5 factor of "
            "safety વાળા ductile ભાગ માટે allowable stress છે."),
      pit("Dividing the breaking load by the necked area and calling it the UTS. The UTS is defined on "
          "the original area; the true stress at fracture is higher and is a different quantity.",
          "તૂટવાના load ને necked area થી ભાગી તેને UTS કહેવું. UTS મૂળ area પર વ્યાખ્યાયિત છે; "
          "fracture પરનો true stress ઊંચો હોય છે અને તે જુદી રાશિ છે.")],
     8),
    ("Thermal expansion of a rail",
     "રેલનું thermal expansion",
     "A steel rail is 20 m long at 20 C. The rail may reach 55 C in summer. Taking the expansion "
     "coefficient of steel as 11.7e-6 per K, find the expansion and the gap to be left between rails. "
     "If the gap were zero, estimate the thermal stress with E = 200 GPa.",
     "Steel રેલ 20 C પર 20 m લાંબી છે. ઉનાળામાં 55 C સુધી પહોંચી શકે. Steel નો expansion coefficient "
     "11.7e-6 પ્રતિ K લઈ, પ્રસરણ અને રેલ વચ્ચે રાખવાનું અંતર શોધો. અંતર શૂન્ય હોય તો E = 200 GPa "
     "સાથે thermal stress અંદાજો.",
     [h4("Step 1 - temperature rise", "પગલું 1 - temperature વધારો"),
      math("dT = 55 - 20 = 35 K"),
      h4("Step 2 - expansion", "પગલું 2 - પ્રસરણ"),
      math("dL = alpha L0 dT = 11.7e-6 x 20 000 x 35 = 8.19 mm"),
      h4("Step 3 - the stress if the rail cannot expand",
      "પગલું 3 - રેલ પ્રસરી ન શકે તો stress"),
      math("sigma = E alpha dT = 200e9 x 11.7e-6 x 35 = 81.9e6 Pa = 82 MPa"),
      eq("dL = 8.2 mm,  thermal stress if restrained = 82 MPa"),
      p("82 MPa is a third of the yield strength of mild steel, so a restrained rail is not far from "
        "yielding on a hot day; a few joints with the wrong gap will buckle the track. Welded track "
        "uses the same number to set the stress-free temperature.",
        "82 MPa mild steel ની yield strength ના ત્રીજા ભાગ જેટલું છે, તેથી ગરમ દિવસે રોકાયેલી રેલ "
        "yield ની નજીક હોય; ખોટા અંતરવાળા થોડા joints track ને વાળી નાખે. Welded track એ જ આંકડાથી "
        "stress-free temperature ઠરાવે."),
      check("Unit check: 11.7e-6 per K times 20 m times 35 K is a length, so metres; 8.19e-3 m is "
            "8.19 mm. A result in metres that looks like millimetres means the 1e-6 was dropped.",
            "એકમ ચકાસો: 11.7e-6 પ્રતિ K ગુણ્યા 20 m ગુણ્યા 35 K એ લંબાઈ છે, તેથી મીટર; 8.19e-3 m એટલે "
            "8.19 mm. મીટરમાં જવાબ મિલીમીટર જેવો લાગે તો 1e-6 ખૂટે છે."),
      pit("Leaving the gap equal to the expansion of one rail only. The gap is set for the expansion "
          "over the installation temperature range, and two rails meet at each joint, so the practical "
          "allowance is arrived at from the design temperature, not from one day's weather.",
          "એક રેલના પ્રસરણ જેટલું જ અંતર રાખવું. અંતર installation temperature ની રેન્જ પરના પ્રસરણ "
          "માટે ઠરાવાય, અને દરેક joint પર બે રેલ મળે, તેથી વ્યવહારની છૂટ design temperature પરથી "
          "આવે, એક દિવસના હવામાન પરથી નહીં.")],
     7),
    ("Copper against aluminium for a conductor",
     "Conductor માટે copper સામે aluminium",
     "A 100 m run of conductor has a cross-section of 2.5 mm2. Find the resistance with copper "
     "(rho = 1.72e-8 ohm m) and with aluminium (rho = 2.82e-8 ohm m), and compare the masses "
     "(densities 8.96 and 2.70 g/cm3). State which you would use for an overhead line and why.",
     "100 m લાંબા conductor નો cross-section 2.5 mm2 છે. Copper (rho = 1.72e-8 ohm m) અને aluminium "
     "(rho = 2.82e-8 ohm m) સાથે resistance શોધો, અને દળની સરખામણી કરો (density 8.96 અને "
     "2.70 g/cm3). Overhead line માટે કયું વાપરશો અને કેમ તે કહો.",
     [h4("Step 1 - resistances", "પગલું 1 - resistances"),
      math("R = rho L/A,  A = 2.5 mm2 = 2.5e-6 m2,  L = 100 m",
           "copper: R = 1.72e-8 x 100/2.5e-6 = 0.688 ohm",
           "aluminium: R = 2.82e-8 x 100/2.5e-6 = 1.128 ohm"),
      h4("Step 2 - masses", "પગલું 2 - દળ"),
      math("volume = 2.5e-6 x 100 = 2.5e-4 m3 = 250 cm3",
           "copper: 250 x 8.96 = 2240 g",
           "aluminium: 250 x 2.70 = 675 g"),
      eq("R: 0.69 ohm copper, 1.13 ohm aluminium;  mass: 2.24 kg against 0.68 kg"),
      p("Aluminium has 1.64 times the resistance but only 0.30 of the mass, so for the same conductance "
        "it still weighs half as much. That is why overhead lines are ACSR - aluminium conductors with "
        "a steel core - while a switchgear busbar, where space matters, stays copper.",
        "Aluminium નું resistance 1.64 ગણું પણ દળ ફક્ત 0.30 ગણું છે, તેથી એ જ conductance માટે પણ તે "
        "અડધું વજન ધરાવે. તેથી overhead lines ACSR - steel core વાળા aluminium conductors - હોય છે, "
        "જ્યારે જ્યાં જગ્યા મહત્વની છે તેવા switchgear busbar copper જ રહે."),
      check("Ratios: 1.128/0.688 = 1.64 = 2.82/1.72, the resistivity ratio, and 8.96/2.70 = 3.32, the "
            "density ratio. Every answer in this problem is one of those two ratios.",
            "ગુણોત્તર: 1.128/0.688 = 1.64 = 2.82/1.72, જે resistivity ગુણોત્તર છે, અને "
            "8.96/2.70 = 3.32, જે density ગુણોત્તર છે. આ દાખલાનો દરેક જવાબ એ બે ગુણોત્તરમાંથી એક છે."),
      pit("Comparing resistances of equal mass instead of equal size. A fair comparison for a line is "
          "at equal conductance and equal span, which means a larger aluminium section - and only then "
          "does the mass advantage become the 2:1 that the industry quotes.",
          "સરખા દળની જગ્યાએ સરખા માપની resistance સરખાવવી. લાઇન માટે ન્યાયી સરખામણી સરખા conductance "
          "અને સરખા span પર થાય, એટલે aluminium નું section મોટું લેવાય - ત્યારે જ દળનો ફાયદો ઉદ્યોગ "
          "કહે તે 2:1 થાય.")],
     6),
    ("Specific stiffness of a carbon composite",
     "Carbon composite ની specific stiffness",
     "A carbon-fibre composite contains 60 % by volume of fibre (E = 230 GPa, density 1.8 g/cm3) in an "
     "epoxy matrix (E = 3.5 GPa, density 1.2 g/cm3). Find the density, the modulus along the fibre and "
     "the specific stiffness, and compare it with steel (E = 200 GPa, density 7.85 g/cm3).",
     "Carbon-fibre composite માં volume પ્રમાણે 60 % fibre (E = 230 GPa, density 1.8 g/cm3) અને epoxy "
     "matrix (E = 3.5 GPa, density 1.2 g/cm3) છે. Density, fibre દિશામાં modulus અને specific stiffness "
     "શોધો, અને steel (E = 200 GPa, density 7.85 g/cm3) સાથે સરખાવો.",
     [h4("Step 1 - density by the rule of mixtures", "પગલું 1 - rule of mixtures થી density"),
      math("rho_c = f rho_f + (1 - f) rho_m = 0.6 x 1.8 + 0.4 x 1.2",
           "      = 1.08 + 0.48 = 1.56 g/cm3"),
      h4("Step 2 - modulus along the fibre", "પગલું 2 - fibre દિશામાં modulus"),
      math("E_c = f E_f + (1 - f) E_m = 0.6 x 230 + 0.4 x 3.5",
           "    = 138 + 1.4 = 139.4 GPa"),
      h4("Step 3 - specific stiffness", "પગલું 3 - specific stiffness"),
      math("composite: 139.4/1.56 = 89.4 GPa per g/cm3",
           "steel: 200/7.85 = 25.5 GPa per g/cm3",
           "ratio = 89.4/25.5 = 3.5"),
      eq("rho = 1.56 g/cm3,  E = 139 GPa,  specific stiffness 3.5 times steel"),
      p("The composite is barely stiffer than steel in absolute terms (139 against 200 GPa) but 3.5 "
        "times stiffer for the same weight, which is the whole argument for a Formula-style chassis or "
        "a wind-turbine blade. The price is cost and a fibre direction that must be designed, not "
        "assumed.",
        "Composite સંપૂર્ણ રીતે steel કરતાં ભાગ્યે જ વધુ stiff છે (139 સામે 200 GPa) પણ એ જ વજન માટે "
        "3.5 ગણું stiff છે, જે Formula-style chassis કે wind-turbine blade ની આખી દલીલ છે. કિંમત ખર્ચ "
        "અને fibre ની દિશા છે, જે design કરવી પડે, ધારી ન લેવાય."),
      check("The rule of mixtures must lie between the two values: 1.2 < 1.56 < 1.8 for density and "
            "3.5 < 139 < 230 for the modulus. A result outside those bounds means the fractions were "
            "added to 1.1 or 0.9.",
            "Rule of mixtures બે મૂલ્યો વચ્ચે જ હોવું જોઈએ: density માટે 1.2 < 1.56 < 1.8 અને modulus "
            "માટે 3.5 < 139 < 230. સીમાની બહાર જવાબ આવે તો fractions નો સરવાળો 1.1 કે 0.9 થયો છે."),
      pit("Using the rule of mixtures across the fibres. Loaded across the fibre direction the modulus "
          "falls to a series combination, about 6 GPa for this lay-up, so a composite is highly "
          "anisotropic and the direction has to be stated with every value.",
          "Fibres ની આડી દિશામાં rule of mixtures વાપરવું. Fibre દિશાની આડી load માં modulus series "
          "સંયોજન થાય, આ lay-up માટે લગભગ 6 GPa, તેથી composite ખૂબ anisotropic છે અને દરેક મૂલ્ય સાથે "
          "દિશા જણાવવી પડે.")],
     7),
]

PRACTICE = [(tr(h_en, h_gu), tr(q_en, q_gu), body(*parts_), m)
            for (h_en, h_gu, q_en, q_gu, parts_, m) in _PRACTICE]

EXAM = [{"q": q, "marks": m} for _, q, _, m in PRACTICE]
PRACTICE_ANSWERS = [a for _, _, a, _ in PRACTICE]

SOURCES = [
    ("GTU DI01000181 Engineering Materials Science syllabus (uploaded PDF, w.e.f. 2024-25)",
     "https://syllabus.gtu.ac.in/"),
    ("G. B. S. Narang - Materials Science, Khanna Publishers (bonding, crystal structure, properties)",
     "https://www.khannapublishers.in/"),
    ("V. Raghavan - Materials Science and Engineering, Prentice Hall India (crystal geometry, unit "
     "cells, density calculations)", "https://www.pearson.com/"),
    ("Substech open materials science reference - crystal structures and the iron-carbon diagram",
     "https://www.substech.com/dokuwiki/doku.php?id=iron_carbon_phase_diagram"),
    ("NPTEL / virtual labs on materials science and metallography", "https://vlab.co.in/"),
]
