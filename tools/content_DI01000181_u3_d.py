"""DI01000181 Unit 3, part D: equations, viva, six solved numericals and sources."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from subject_DI01000181 import tr  # noqa: E402
from content_DI01000181_lib import (p, h4, table, math, eq, why, check, pit,  # noqa: E402
                                    body, ul, ol)

EQUATIONS = [
    {"title": tr("Composition and density", "Composition અને density"),
     "items": [
         {"name": tr("Weight per cent", "Weight ટકા"),
          "f": "w(i) % = m(i)/sum(m) x 100",
          "terms": tr("How every alloy composition in a datasheet is written.",
                      "Datasheet માં દરેક alloy composition આમ જ લખાય છે.")},
         {"name": tr("Atomic per cent", "Atomic ટકા"),
          "f": "at(i) % = (w(i)/A(i))/sum(w/A) x 100",
          "terms": tr("A is the atomic mass; needed whenever atoms, not grams, do the work.",
                      "A એ atomic mass; જ્યાં atoms કામ કરે ત્યાં grams નહીં, આ જોઈએ.")},
         {"name": tr("Density of an alloy", "Alloy ની density"),
          "f": "1/rho = sum(w(i)/rho(i))",
          "terms": tr("Volume-additive estimate; 2 to 3 % low when the atoms pack better than ideal.",
                      "Volume-ઉમેરાતો અંદાજ; atoms આદર્શ કરતાં સારા ગોઠવાય તો 2-3 % ઓછો આવે.")},
         {"name": tr("Carbon equivalent of a cast iron", "Cast iron નું carbon equivalent"),
          "f": "CE = %C + (%Si + %P)/3",
          "terms": tr("Silicon graphitises a third as strongly as carbon; CE near 4.3 casts best.",
                      "Silicon, carbon ના ત્રીજા ભાગ જેટલું graphitise કરે; CE 4.3 ની આસપાસ સૌથી સારું cast થાય.")},
     ]},
    {"title": tr("Selection numbers", "પસંદગીના આંકડા"),
     "items": [
         {"name": tr("Specific strength", "Specific strength"),
          "f": "specific strength = UTS/rho",
          "terms": tr("MPa/(g/cm3) is the same number as kN m/kg; the fair comparison for weight.",
                      "MPa/(g/cm3) એ kN m/kg જ છે; વજન માટેની ન્યાયી સરખામણી.")},
         {"name": tr("Conductivity in IACS", "IACS માં વાહકતા"),
          "f": "%IACS = sigma/5.8e7 x 100",
          "terms": tr("5.8e7 S/m is annealed copper; brass 70/30 is 28 % of it.",
                      "5.8e7 S/m એ annealed copper છે; brass 70/30 તેના 28 % જેટલું.")},
         {"name": tr("Mass from volume", "Volume પરથી દળ"),
          "f": "m = rho V",
          "terms": tr("Steel 7.85, cast iron 7.2, copper 8.96, aluminium 2.70 g/cm3.",
                      "આંકડા: steel 7.85, cast iron 7.2, copper 8.96, aluminium 2.70 g/cm3.")},
     ]},
    {"title": tr("Steel", "Steel"),
     "items": [
         {"name": tr("The carbon bands", "Carbon ના પટ્ટા"),
          "f": "low <= 0.30 %;  medium 0.30 - 0.60 %;  high 0.60 - 2.14 %",
          "terms": tr("Steel ends at 2.14 % C; cast iron runs from there to 6.67 %.",
                      "Steel 2.14 % C પર પૂરું થાય; cast iron ત્યાંથી 6.67 % સુધી.")},
         {"name": tr("Stainless steel", "Stainless steel"),
          "f": "Cr >= 12 % for a continuous passive film",
          "terms": tr("18/8 means 18 % Cr and 8 % Ni: austenitic and non-magnetic.",
                      "18/8 એટલે 18 % Cr અને 8 % Ni: austenitic અને non-magnetic.")},
         {"name": tr("Reading a designation", "Designation વાંચવું"),
          "f": "C 45 = 0.45 % C;  EN8 is the same steel under the old BS name",
          "terms": tr("The number is the carbon in hundredths of a per cent.",
                      "આંકડો એટલે ટકાના સોમાં ભાગમાં carbon.")},
     ]},
    {"title": tr("Cast iron", "Cast iron"),
     "items": [
         {"name": tr("Graphite shape", "Graphite નો આકાર"),
          "f": "flake = grey,  nodule = ductile,  rosette = malleable,  none = white",
          "terms": tr("The shape, not the carbon content, sets the strength.",
                      "તાકાત carbon content નહીં, આકાર નક્કી કરે.")},
         {"name": tr("Tension against compression", "Tension સામે compression"),
          "f": "sigma(compression) = 3 to 4 x sigma(tension) for grey iron",
          "terms": tr("A flake is a crack, so it opens in tension and closes in compression.",
                      "Flake એ તિરાડ છે, તેથી tension માં ખૂલે અને compression માં બંધ થાય.")},
         {"name": tr("Damping", "Damping"),
          "f": "damping of grey iron = 5 to 10 x that of steel",
          "terms": tr("The reason a lathe bed and a surface plate are cast iron.",
                      "Lathe bed અને surface plate cast iron કેમ હોય તેનું કારણ.")},
     ]},
    {"title": tr("Copper and aluminium", "Copper અને aluminium"),
     "items": [
         {"name": tr("The aluminium series", "Aluminium ની series"),
          "f": "series 1 = 99 % Al; 2 = Cu; 3 = Mn; 4 = Si; 5 = Mg; 6 = Mg+Si; 7 = Zn; 8 = other",
          "terms": tr("The number says the main alloying element of a wrought alloy.",
                      "આંકડો wrought alloy નું મુખ્ય alloying element કહે છે.")},
         {"name": tr("Temper letters", "Temper ના અક્ષરો"),
          "f": "temper: O = annealed, H = strain hardened, T = solution treated + aged, F = as fabricated",
          "terms": tr("Always written with the alloy: 6061-T6, not 6061.",
                      "હંમેશા alloy સાથે લખાય: 6061-T6, ફક્ત 6061 નહીં.")},
         {"name": tr("The conductivity trade-off", "વાહકતાનો સોદો"),
          "f": "Cu 100 % IACS -> brass 70/30 28 % -> bronze 13 %",
          "terms": tr("Every dissolved atom scatters electrons, so strength costs conductivity.",
                      "દરેક ઓગળેલો atom electrons ને અથડાવે, તેથી તાકાત વાહકતાનો ભોગ લે.")},
     ]},
]

VIVA = [
    {"title": tr("Classification", "વર્ગીકરણ"),
     "items": [
         {"q": tr("What separates steel from cast iron?", "Steel અને cast iron ને શું વહેંચે છે?"),
          "a": tr("The carbon content. Up to 2.14 % it is steel, above it cast iron, and 2.14 % is "
                  "the most carbon austenite can dissolve.",
                  "Carbon content. 2.14 % સુધી steel, ઉપર cast iron, અને 2.14 % એ austenite ઓગાળી "
                  "શકે તે વધુમાં વધુ carbon.")},
         {"q": tr("Give three differences between a metal and a non-metal.",
                  "Metal અને non-metal વચ્ચે ત્રણ ફરક આપો."),
          "a": tr("A metal conducts heat and current, is malleable and ductile, and has lustre; a "
                  "non-metal insulates, is brittle, and is dull. All three come from free electrons.",
                  "Metal ગરમી અને current વહન કરે, malleable તથી ductile છે, અને lustre ધરાવે; non-metal "
                  "અવાહક, ભંગુર અને ઝાંખું છે. ત્રણેય free electrons થી આવે.")},
         {"q": tr("Why is silicon called a metalloid?", "Silicon ને metalloid કેમ કહે છે?"),
          "a": tr("It looks like a metal - shiny and grey - but it is brittle and is a semiconductor, "
                  "not a conductor.",
                  "તે ધાતુ જેવું દેખાય - ચળકતું અને ભૂખરું - પણ તે ભંગુર છે અને conductor નહીં, "
                  "semiconductor છે.")},
     ]},
    {"title": tr("Steels", "Steels"),
     "items": [
         {"q": tr("Why does strength rise with carbon and ductility fall?",
                  "Carbon વધતાં તાકાત કેમ વધે અને ductility કેમ ઘટે?"),
          "a": tr("More carbon means more cementite in the pearlite, and cementite is hard and "
                  "brittle; the ferrite that used to deform is replaced by it.",
                  "વધુ carbon એટલે pearlite માં વધુ cementite, અને cementite સખત તથી ભંગુર છે; જે "
                  "ferrite deform થતું હતું તેની જગ્યાએ તે આવે છે.")},
         {"q": tr("What does EN19 steel contain and where is it used?",
                  "EN19 સ્ટીલમાં શું છે અને ક્યાં વપરાય?"),
          "a": tr("0.4 % carbon with about 1 % chromium and 0.25 % molybdenum, so it hardens right "
                  "through a thick section: gears, crankshafts and axles.",
                  "0.4 % carbon સાથે લગભગ 1 % chromium અને 0.25 % molybdenum, તેથી જાડો ભાગ પણ આખો "
                  "harden થાય: gears, crankshafts અને axles.")},
         {"q": tr("Why is stainless steel called stainless?", "Stainless steel ને stainless કેમ કહે છે?"),
          "a": tr("Because its chromium forms a thin passive oxide film that heals itself in air. "
                  "Without oxygen, or in chloride water, it is not stainless at all.",
                  "કારણ કે તેનું chromium પાતળું passive oxide પડ બનાવે જે હવામાં પોતાની જાતે સંધાય. "
                  "Oxygen ન હોય કે chloride વાળા પાણીમાં તે stainless જ નથી.")},
     ]},
    {"title": tr("Cast irons, copper and aluminium", "Cast irons, copper અને aluminium"),
     "items": [
         {"q": tr("Why is grey cast iron good for a lathe bed?",
                  "Lathe bed માટે grey cast iron કેમ સારું છે?"),
          "a": tr("It is loaded in compression, where it is strong; the graphite damps vibration so "
                  "the finish stays accurate; and the complicated shape is cast, not machined.",
                  "તેના પર compression નો ભાર હોય જ્યાં તે મજબૂત છે; graphite vibration શોષે તેથી finish "
                  "ચોક્કસ રહે; અને ગૂંચવાડાભરી આકૃતિ cast થાય, machined નહીં.")},
         {"q": tr("What is the difference between brass and bronze?",
                  "Brass અને bronze માં શું ફરક છે?"),
          "a": tr("Brass is copper with zinc, and bronze is copper with tin; brass is more ductile "
                  "and cheaper, bronze is harder and better under wear.",
                  "Brass એ copper સાથે zinc, અને bronze એ copper સાથે tin; brass વધુ ductile અને સસ્તું, "
                  "bronze વધુ સખત અને wear માં સારું.")},
         {"q": tr("Why does adding zinc to copper reduce its conductivity?",
                  "Copper માં zinc ઉમેરતાં વાહકતા કેમ ઘટે છે?"),
          "a": tr("The zinc atoms are a different size, so they strain the lattice and scatter the "
                  "conduction electrons; scattering is resistance.",
                  "Zinc atoms જુદા માપના હોય તેથી lattice તણાય અને conduction electrons અથડાય; અથડામણ એ "
                  "resistance છે.")},
     ]},
    {"title": tr("Aluminium", "Aluminium"),
     "items": [
         {"q": tr("What does the 6 in 6061 mean?", "6061 માં 6 શું કહે છે?"),
          "a": tr("The main alloying addition is magnesium plus silicon in a series 6 alloy; the other "
                  "digits identify the particular composition.",
                  "series 6 alloy માં મુખ્ય alloying ઉમેરો magnesium અને silicon છે; બાકીના અંક ચોક્કસ "
                  "composition ઓળખે છે.")},
         {"q": tr("What does the T6 temper mean?", "T6 temper એટલે શું?"),
          "a": tr("Solution heat treated, quenched and then artificially aged, so that fine "
                  "precipitates block dislocations and raise the strength.",
                  "Solution heat treatment, quench અને પછી artificial ageing, જેથી નાના precipitates "
                  "dislocation રોકે અને તાકાત વધારે.")},
         {"q": tr("Why can aluminium not simply replace steel part for part?",
                  "Aluminium સ્ટીલની જગ્યાએ ભાગ-બદલ ભાગ કેમ ન લઈ શકે?"),
          "a": tr("It is a third of the density but also a third of the modulus, so a part of the "
                  "same size deflects three times as much; a strength-limited part must be compared "
                  "on specific strength.",
                  "તેની density ત્રીજા ભાગની છે પણ modulus પણ ત્રીજા ભાગનો, તેથી સરખા માપનો ભાગ ત્રણ ગણો "
                  "વળે; તાકાત-મર્યાદિત ભાગ specific strength પર સરખાવવો પડે.")},
     ]},
]


_PRACTICE = [
    ("Density of a 70/30 brass from the rule of mixtures",
     "Rule of mixtures થી 70/30 brass ની density",
     "A 70/30 brass is made by weight from copper (8.96 g/cm3) and zinc (7.14 g/cm3). Estimate its "
     "density by adding volumes, compare it with the measured 8.53 g/cm3 and say why the estimate is "
     "low.",
     "70/30 brass વજન પ્રમાણે copper (8.96 g/cm3) અને zinc (7.14 g/cm3) થી બને છે. Volume ઉમેરીને તેની "
     "density નો અંદાજ કાઢો, માપેલા 8.53 g/cm3 સાથે સરખાવો અને અંદાજ ઓછો કેમ આવે તે કહો.",
     [h4("Step 1 - the volume of 100 g of alloy", "પગલું 1 - 100 g alloy નું volume"),
      math("take 100 g of brass: 70 g copper and 30 g zinc",
           "V(Cu) = 70/8.96 = 7.8125 cm3",
           "V(Zn) = 30/7.14 = 4.2017 cm3",
           "V(total) = 12.0142 cm3"),
      h4("Step 2 - the density", "પગલું 2 - density"),
      math("rho = m/V = 100/12.0142 = 8.32 g/cm3",
           "in the rule form: 1/rho = 0.70/8.96 + 0.30/7.14 = 0.12014"),
      h4("Step 3 - compare and explain", "પગલું 3 - સરખાવો અને સમજાવો"),
      math("measured 8.53 g/cm3, estimated 8.32 g/cm3",
           "error = (8.32 - 8.53)/8.53 x 100 = -2.5 %"),
      eq("rho = 8.32 g/cm3 against 8.53 measured: 2.5 % low"),
      p("The rule of mixtures assumes the atoms simply add their volumes, but a zinc atom is smaller "
        "than a copper atom and fits into the lattice without pushing it apart, so the real alloy is "
        "denser than the sum of its parts. The same assumption is why the rule is only used for an "
        "estimate, never for a purchase specification.",
        "Rule of mixtures ધારે છે કે atoms ફક્ત પોતાનું volume ઉમેરે, પણ zinc atom copper atom કરતાં "
        "નાનો હોય તેથી lattice ને ધકેલ્યા વગર અંદર બેસે, અને સાચો alloy તેના ભાગોના સરવાળા કરતાં "
        "ઘનતાવાળો નીકળે. એ જ કારણે આ નિયમ ફક્ત અંદાજ માટે વપરાય, ખરીદીના specification માટે નહીં."),
      check("A rough check: the answer must lie between 7.14 and 8.96, and nearer to copper because "
            "there is more copper. 8.32 satisfies both.",
            "ઝડપી ચકાસણી: જવાબ 7.14 અને 8.96 વચ્ચે અને copper ની નજીક હોવો જોઈએ કારણ કે copper વધુ છે. "
            "8.32 બંને શરત પૂરી કરે છે.")],
     7),

    ("Cost of a brass melt",
     "Brass melt નો ખર્ચ",
     "A foundry needs 250 kg of sound 70/30 brass castings. Melting loss is 3 % of the charge. Copper "
     "costs Rs 820 per kg and zinc Rs 280 per kg. Find the charge mass and the metal cost of the "
     "heat.",
     "એક ફાઉન્ડ્રીને 250 kg સાચા 70/30 brass castings જોઈએ. Melting loss charge ના 3 % છે. Copper "
     "Rs 820 પ્રતિ kg અને zinc Rs 280 પ્રતિ kg. Charge નું દળ અને heat નો metal ખર્ચ શોધો.",
     [h4("Step 1 - the charge mass", "પગલું 1 - charge નું દળ"),
      math("3 % is lost, so 97 % of the charge becomes casting",
           "0.97 x charge = 250 kg",
           "charge = 250/0.97 = 257.7 kg"),
      h4("Step 2 - cost of one kilogram of charge", "પગલું 2 - એક kg charge નો ખર્ચ"),
      math("70 % copper: 0.70 x 820 = Rs 574.00",
           "30 % zinc:   0.30 x 280 = Rs  84.00",
           "cost per kg = Rs 658.00"),
      h4("Step 3 - the cost of the heat", "પગલું 3 - heat નો ખર્ચ"),
      math("cost = 257.7 x 658 = Rs 1,69,587",
           "per kilogram of good casting: 169587/250 = Rs 678.3"),
      eq("charge 257.7 kg,  Rs 1,69,587 for the heat,  Rs 678 per kg of casting"),
      p("The melting loss is what makes the casting cost more than the metal in it: 3 % of the "
        "charge is lost, so about Rs 20 per kilogram of casting is paid for metal that went up the "
        "flue or into the slag. That is why a foundry weighs its charge and its returns carefully.",
        "Melting loss એ જ casting ને તેમાંના metal કરતાં મોંઘું બનાવે: charge ના 3 % જાય છે, તેથી "
        "casting ના પ્રતિ kg લગભગ Rs 20 એવી ધાતુના મળે જે ચીમનીમાં કે slag માં ગઈ. તેથી ફાઉન્ડ્રી "
        "પોતાનું charge અને returns કાળજીથી તોલે છે."),
      pit("Do not add 3 % to 250 kg. The loss is taken from the charge, so the charge is larger than "
          "the casting by 250/0.97, not 250 x 1.03.",
          "250 kg માં 3 % ઉમેરશો નહીં. Loss charge માંથી જાય છે, તેથી charge casting કરતાં 250/0.97 "
          "જેટલું મોટું હોય, 250 x 1.03 નહીં.")],
     7),

    ("Carbon equivalent of two cast irons",
     "બે cast irons નું carbon equivalent",
     "A grey iron contains 3.4 % C, 2.1 % Si and 0.3 % P; a ductile iron contains 3.6 % C, 2.4 % Si "
     "and 0.05 % P. Find the carbon equivalent of each and say what it means for casting.",
     "એક grey iron માં 3.4 % C, 2.1 % Si અને 0.3 % P છે; એક ductile iron માં 3.6 % C, 2.4 % Si અને "
     "0.05 % P છે. દરેકનું carbon equivalent શોધો અને casting માટે તેનો અર્થ કહો.",
     [h4("Step 1 - the formula", "પગલું 1 - સૂત્ર"),
      math("CE = %C + (%Si + %P)/3",
           "silicon graphitises a third as strongly as carbon, hence the divisor 3"),
      h4("Step 2 - the grey iron", "પગલું 2 - grey iron"),
      math("CE = 3.4 + (2.1 + 0.3)/3 = 3.4 + 0.80 = 4.20"),
      h4("Step 3 - the ductile iron", "પગલું 3 - ductile iron"),
      math("CE = 3.6 + (2.4 + 0.05)/3 = 3.6 + 0.817 = 4.42"),
      eq("grey iron CE = 4.20,  ductile iron CE = 4.42,  the eutectic is 4.3"),
      p("Both are close to the eutectic value of 4.3, which is what a foundry wants: a metal that "
        "freezes in a narrow range, feeds itself, and casts without shrinkage cavities. The grey iron "
        "at 4.20 is slightly hypoeutectic and will show a little primary austenite; the ductile iron "
        "at 4.42 is slightly hypereutectic, and it is the magnesium addition, not the carbon, that "
        "makes its graphite nodular.",
        "બંને eutectic મૂલ્ય 4.3 ની નજીક છે, જે ફાઉન્ડ્રીને જોઈએ: એવી ધાતુ જે નાની range માં થીજે, પોતાને "
        "feed કરે અને shrinkage છિદ્રો વગર cast થાય. 4.20 વાળું grey iron થોડું hypoeutectic છે અને થોડું "
        "primary austenite દેખાશે; 4.42 વાળું ductile iron થોડું hypereutectic છે, અને તેનું graphite "
        "nodular magnesium ઉમેરવાથી થાય છે, carbon થી નહીં."),
      check("CE must not be far above 4.3 in a thin section, or kish graphite forms and the casting "
            "surface becomes rough and weak.",
            "પાતળા ભાગમાં CE 4.3 થી ઘણું ઉપર ન જોઈએ, નહીં તો kish graphite બને અને casting ની સપાટી "
            "ખરબચડી તથી નબળી થાય.")],
     6),

    ("Replacing a steel bracket with aluminium",
     "Steel bracket ને aluminium થી બદલવું",
     "A bracket has a volume of 260 cm3 and is made of steel of density 7.85 g/cm3. Find its mass, the "
     "mass if it is made of aluminium alloy of density 2.70 g/cm3, and the percentage saved. The steel "
     "has UTS 450 MPa and the aluminium alloy 310 MPa - comment on whether the swap is safe at the "
     "same dimensions.",
     "એક bracket નું volume 260 cm3 છે અને તે 7.85 g/cm3 density ના સ્ટીલનું બનેલું છે. તેનું દળ, "
     "2.70 g/cm3 density ના aluminium alloy નું બન્યું હોય તો દળ, અને થતી ટકાવારી બચત શોધો. સ્ટીલનું "
     "UTS 450 MPa અને aluminium alloy નું 310 MPa છે - સરખા માપ પર આ બદલી સલામત છે કે નહીં તે કહો.",
     [h4("Step 1 - the two masses", "પગલું 1 - બે દળ"),
      math("m(steel) = rho V = 7.85 x 260 = 2041 g = 2.04 kg",
           "m(aluminium) = 2.70 x 260 = 702 g = 0.70 kg"),
      h4("Step 2 - the saving", "પગલું 2 - બચત"),
      math("saving = 2.041 - 0.702 = 1.339 kg",
           "percentage = 1.339/2.041 x 100 = 65.6 %"),
      h4("Step 3 - is it safe at the same size?", "પગલું 3 - સરખા માપ પર સલામત છે?"),
      math("section area is unchanged, so the load capacity falls in the ratio of the strengths",
           "310/450 = 0.69 - the aluminium part carries 69 % of the load",
           "specific strength: steel 450/7.85 = 57, aluminium 310/2.70 = 115 kN m/kg",
           "so the swap is safe only if the part was over-designed by 45 % or can be thickened"),
      eq("2.04 kg -> 0.70 kg,  65.6 % lighter,  but 31 % weaker at the same section"),
      p("This is the standard trap of a material substitution question. Weight falls by two thirds, "
        "but strength falls by a third, and stiffness falls by two thirds as well because the modulus "
        "of aluminium is 70 GPa against 200 GPa for steel. A part that is stiffness-limited must be "
        "redesigned, not just swapped.",
        "સામગ્રી બદલવાના પ્રશ્નની આ પ્રમાણભૂત ભૂલ છે. વજન બે-તૃતીયાંશ ઘટે, પણ તાકાત એક-તૃતીયાંશ ઘટે, અને "
        "stiffness પણ બે-તૃતીયાંશ ઘટે કારણ કે aluminium નો modulus 70 GPa છે જ્યારે સ્ટીલનો 200 GPa. "
        "Stiffness-મર્યાદિત ભાગ ફરી design કરવો પડે, ફક્ત બદલી નાખવાથી ન થાય."),
      check("Check the units: 260 cm3 x 7.85 g/cm3 gives grams, so divide by 1000 for kilograms.",
            "એકમ ચકાસો: 260 cm3 x 7.85 g/cm3 ગ્રામ આપે, તેથી kg માટે 1000 વડે ભાગો.")],
     6),

    ("Copper or brass for a wire",
     "Wire માટે copper કે brass",
     "A 30 m run of 2.5 mm2 wire is to carry 16 A. Compare the resistance and the power lost if the "
     "wire is copper (1.72e-8 ohm m) and if it is brass (6.4e-8 ohm m), and say which one a "
     "switchboard uses.",
     "2.5 mm2 ની 30 m લાંબી wire 16 A વહન કરે છે. Wire copper (1.72e-8 ohm m) હોય અને brass (6.4e-8 "
     "ohm m) હોય તો resistance અને ગુમાવાતી power સરખાવો, અને switchboard કઈ વાપરે તે કહો.",
     [h4("Step 1 - the resistance of each", "પગલું 1 - દરેકનું resistance"),
      math("R = rho L/A,  A = 2.5 mm2 = 2.5e-6 m2,  L = 30 m",
           "R(Cu)    = 1.72e-8 x 30/2.5e-6 = 0.2064 ohm",
           "R(brass) = 6.40e-8 x 30/2.5e-6 = 0.7680 ohm"),
      h4("Step 2 - the power lost at 16 A", "પગલું 2 - 16 A પર ગુમાવાતી power"),
      math("P = I^2 R",
           "P(Cu)    = 16^2 x 0.2064 = 52.8 W",
           "P(brass) = 16^2 x 0.7680 = 196.6 W"),
      h4("Step 3 - compare", "પગલું 3 - સરખામણી"),
      math("resistance ratio = 6.4/1.72 = 3.72",
           "extra loss = 196.6 - 52.8 = 143.8 W in 30 m of wire",
           "over a 10 hour day: 1.44 kWh wasted per run"),
      eq("0.206 ohm against 0.768 ohm;  52.8 W against 196.6 W;  copper by a factor of 3.7"),
      p("A switchboard uses copper, or aluminium where the weight matters more than the loss, and "
        "never brass. Brass is for a terminal stud or a plug pin, where its strength and its "
        "machinability matter and the current path is a few millimetres long.",
        "Switchboard copper વાપરે, અથવા જ્યાં ગુમાવેલા power કરતાં વજન વધુ મહત્વનું હોય ત્યાં aluminium, "
        "અને brass કદી નહીં. Brass terminal stud કે plug pin માટે છે, જ્યાં તેની તાકાત અને machining "
        "ઉપયોગી છે અને current નો રસ્તો થોડા મિલીમીટરનો છે."),
      pit("Area in mm2 must be converted to m2 before it goes into R = rho L/A, otherwise the answer "
          "is a million times too small.",
          "R = rho L/A માં નાખતાં પહેલાં mm2 નું area m2 માં ફેરવવું પડે, નહીં તો જવાબ દસ લાખ ગણો નાનો આવે.")],
     7),

    ("From weight per cent to atomic per cent",
     "Weight ટકા થી atomic ટકા",
     "A 70/30 brass and a gunmetal of composition Cu 88, Sn 10, Zn 2 are given by weight. Convert "
     "both to atomic per cent (Cu 63.55, Zn 65.38, Sn 118.71) and say why a metallurgist prefers the "
     "atomic figure.",
     "70/30 brass અને Cu 88, Sn 10, Zn 2 ના gunmetal વજન પ્રમાણે આપેલા છે. બંનેને atomic ટકામાં ફેરવો "
     "(Cu 63.55, Zn 65.38, Sn 118.71) અને metallurgist atomic આંકડો કેમ પસંદ કરે તે કહો.",
     [h4("Step 1 - moles in 100 g of brass", "પગલું 1 - 100 g brass માં moles"),
      math("n(Cu) = 70/63.55 = 1.1015 mol",
           "n(Zn) = 30/65.38 = 0.4589 mol",
           "total  = 1.5604 mol"),
      h4("Step 2 - atomic per cent of the brass", "પગલું 2 - brass ના atomic ટકા"),
      math("Cu = 1.1015/1.5604 x 100 = 70.6 at %",
           "Zn = 0.4589/1.5604 x 100 = 29.4 at %"),
      h4("Step 3 - the gunmetal", "પગલું 3 - gunmetal"),
      math("n(Cu) = 88/63.55 = 1.3847,  n(Sn) = 10/118.71 = 0.0842,  n(Zn) = 2/65.38 = 0.0306",
           "total = 1.4995 mol",
           "Cu 92.3 at %,  Sn 5.6 at %,  Zn 2.0 at %"),
      eq("brass 70.6 / 29.4 at %,  gunmetal 92.3 / 5.6 / 2.0 at %"),
      p("A phase diagram, a lattice parameter and a density calculation all count atoms, not grams, "
        "so the atomic per cent is the composition you need for any structural argument. A datasheet "
        "gives weight per cent because that is what the foundry weighs out.",
        "Phase diagram, lattice parameter અને density ની ગણતરી બધું atoms ગણે, ગ્રામ નહીં, તેથી કોઈ પણ "
        "રચનાની દલીલ માટે atomic ટકા જોઈએ. Datasheet વજનના ટકા આપે કારણ કે ફાઉન્ડ્રી તોલે છે તે વજન."),
      check("The atomic percentages must still add to 100: 70.6 + 29.4 = 100.0 and "
            "92.3 + 5.6 + 2.0 = 99.9, which is rounding.",
            "Atomic ટકાનો સરવાળો પણ 100 થવો જોઈએ: 70.6 + 29.4 = 100.0 અને 92.3 + 5.6 + 2.0 = 99.9, જે "
            "rounding છે.")],
     6),
]

PRACTICE = [(tr(h_en, h_gu), tr(q_en, q_gu), body(*parts_), m)
            for (h_en, h_gu, q_en, q_gu, parts_, m) in _PRACTICE]

EXAM = [{"q": q, "marks": m} for _, q, _, m in PRACTICE]
PRACTICE_ANSWERS = [a for _, _, a, _ in PRACTICE]

SOURCES = [
    ("GTU DI01000181 Engineering Materials Science syllabus (uploaded PDF, w.e.f. 2024-25)",
     "https://syllabus.gtu.ac.in/"),
    ("O. P. Khanna - Material Science and Metallurgy, Dhanpat Rai (steels, cast irons, alloys)",
     "https://www.dhanpatrai.com/"),
    ("V. Raghavan - Materials Science and Engineering, Prentice Hall India (alloy systems, "
     "non-ferrous metals)", "https://www.pearson.com/"),
    ("Substech open materials science reference - cast irons, copper alloys, aluminium alloys",
     "https://www.substech.com/dokuwiki/doku.php?id=classification_of_metals"),
    ("BIS / IS 210 grey iron and IS 1572 aluminium alloy designation data",
     "https://www.bis.gov.in/"),
]
