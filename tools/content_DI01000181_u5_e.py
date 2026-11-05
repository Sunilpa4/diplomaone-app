"""DI01000181 Unit 5, part E: equations, viva, six solved numericals and sources."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from subject_DI01000181 import tr  # noqa: E402
from content_DI01000181_lib import (p, h4, table, math, eq, why, check, pit,  # noqa: E402
                                    body, ul, ol)

EQUATIONS = [
    {"title": tr("Plating and coating thickness", "Plating અને કોટિંગની જાડાઈ"),
     "items": [
         {"name": tr("Faraday's law of deposition", "Faraday નો નિક્ષેપ નિયમ"),
          "f": "m = M I t/(n F)",
          "terms": tr("M is the molar mass, n the electrons per ion and F 96500 C/mol, so a coulomb "
                      "always deposits the same mass.",
                      "M એ molar mass, n એ ion દીઠ electrons અને F 96500 C/mol, તેથી એક કૂલમ્બ હંમેશા એ જ "
                      "દળ જમા કરે.")},
         {"name": tr("Plating thickness", "Plating ની જાડાઈ"),
          "f": "t = M i t_sec eta/(n F rho)",
          "terms": tr("300 A/m2 of nickel at 95 % efficiency for 20 min gives 11.7 micron.",
                      "95 % efficiency પર 300 A/m2 nickel 20 મિનિટમાં 11.7 માઇક્રોમીટર આપે.")},
         {"name": tr("Deposit per ampere-hour", "પ્રતિ ampere-hour નિક્ષેપ"),
          "f": "m(1 A h) = 3600 M/(n F) = 1.095 g for nickel",
          "terms": tr("The number a plating shop keeps in its head: 1.095 g/Ah for nickel, 1.22 for "
                      "copper, 6.86 for zinc.",
                      "Plating દુકાન યાદ રાખે તે આંકડો: nickel 1.095 g/Ah, copper 1.22, zinc 6.86.")},
         {"name": tr("Wet and dry film", "ભીની અને સૂકી ફિલ્મ"),
          "f": "DFT = WFT x %volume solids/100",
          "terms": tr("75 micron dry at 60 % solids means 125 micron wet, and that is what the "
                      "gauge is laid on.",
                      "60 % solids પર 75 માઇક્રોમીટર સૂકી એટલે 125 માઇક્રોમીટર ભીની, અને ગેજ એ જ માપે.")},
     ]},
    {"title": tr("Corrosion", "કાટ"),
     "items": [
         {"name": tr("Corrosion current to metal loss", "Corrosion current થી ધાતુનો વ્યય"),
          "f": "rate = M i/(n F rho)",
          "terms": tr("0.1 A per m2 on steel is 0.116 mm a year - the same Faraday law, running "
                      "backwards.",
                      "સ્ટીલ પર 0.1 A પ્રતિ m2 એટલે વર્ષે 0.116 mm - એ જ Faraday નિયમ, ઊલટો ચાલે છે.")},
         {"name": tr("Rate from a mass loss", "દળના વ્યય પરથી દર"),
          "f": "CR (mm/year) = 87.6 W/(rho A t)",
          "terms": tr("W in mg, A in cm2, t in hours and rho in g/cm3: 1.2 g from 29.5 cm2 in 90 "
                      "days is 0.21 mm/year.",
                      "W mg માં, A cm2 માં, t કલાકમાં અને rho g/cm3 માં: 29.5 cm2 માંથી 90 દિવસમાં 1.2 g "
                      "એટલે વર્ષે 0.21 mm.")},
         {"name": tr("Corrosion allowance", "Corrosion allowance"),
          "f": "allowance = rate x design life",
          "terms": tr("0.25 mm/year over 12 years is 3.0 mm of extra wall, written on the drawing.",
                      "12 વર્ષ માટે 0.25 mm/વર્ષ એટલે 3.0 mm વધારાની દીવાલ, ડ્રોઇંગ પર લખાય.")},
         {"name": tr("Cell voltage", "Cell નું વોલ્ટેજ"),
          "f": "E(cell) = E(cathode) - E(anode)",
          "terms": tr("Zinc -0.76 V and copper +0.34 V give 1.10 V; zinc and iron give only 0.32 V.",
                      "Zinc -0.76 V અને copper +0.34 V એટલે 1.10 V; zinc અને iron ફક્ત 0.32 V.")},
     ]},
    {"title": tr("Surface finish and film", "Surface finish અને ફિલ્મ"),
     "items": [
         {"name": tr("Theoretical turned roughness", "Theoretical turned ખરબચડાઈ"),
          "f": "Ra = f^2/(32 r)",
          "terms": tr("0.20 mm/rev over a 0.8 mm nose radius is 1.56 micron; halving the feed quarters "
                      "the roughness.",
                      "0.8 mm nose radius પર 0.20 mm/rev એટલે 1.56 માઇક્રોમીટર; feed અડધું કરો તો "
                      "ખરબચડાઈ ચોથા ભાગની.")},
         {"name": tr("Film parameter", "ફિલ્મ parameter"),
          "f": "lambda = h_min/sqrt(Ra1^2 + Ra2^2)",
          "terms": tr("Above 3 the surfaces are fully separated, 1 to 3 is mixed and below 1 is metal "
                      "contact.",
                      "3 ઉપર સપાટી પૂરી અલગ, 1 થી 3 mixed અને 1 ની નીચે ધાતુ ધાતુને અડે.")},
         {"name": tr("Roughness conversion", "ખરબચડાઈનું રૂપાંતર"),
          "f": "Rz ~ 4 Ra",
          "terms": tr("A drawing in Ra and a gauge in Rz are not the same number; multiply before you "
                      "argue.",
                      "Ra માં ડ્રોઇંગ અને Rz માં ગેજ એક જ આંકડો નથી; દલીલ પહેલાં ગુણો.")},
     ]},
    {"title": tr("Oils", "તેલ"),
     "items": [
         {"name": tr("ISO viscosity grade", "ISO viscosity grade"),
          "f": "grade = nominal viscosity at 40 C, +/- 10 %",
          "terms": tr("VG 68 covers 61.2 to 74.8 cSt, which is why two brands of VG 68 are not "
                      "identical.",
                      "VG 68 એટલે 61.2 થી 74.8 cSt, તેથી બે બ્રાન્ડના VG 68 સરખા નથી.")},
         {"name": tr("Viscosity index", "Viscosity index"),
          "f": "VI = (L - U)/(L - H) x 100",
          "terms": tr("U is the oil at 40 C, L and H are reference oils of VI 0 and VI 100 with the "
                      "same 100 C viscosity.",
                      "U એ 40 C પરનું તેલ, L અને H એ સમાન 100 C viscosity વાળા VI 0 અને VI 100 ના "
                      "સંદર્ભ તેલ.")},
         {"name": tr("Walther equation", "Walther સમીકરણ"),
          "f": "log10(log10(nu + 0.7)) = A - B log10(T)",
          "terms": tr("Two measured viscosities fix A and B, and then any other temperature can be "
                      "calculated.",
                      "બે માપેલી viscosity A અને B નક્કી કરે, અને પછી કોઈ પણ તાપમાનની ગણતરી થાય.")},
     ]},
    {"title": tr("Paint quantities", "પેન્ટના જથ્થા"),
     "items": [
         {"name": tr("Wet film volume", "ભીની ફિલ્મનું ઘનફળ"),
          "f": "V = A x WFT",
          "terms": tr("120 m2 at 125 micron wet is 0.015 m3, which is 15 litres of paint.",
                      "125 માઇક્રોમીટર ભીની પર 120 m2 એટલે 0.015 m3, એટલે 15 લિટર પેન્ટ.")},
         {"name": tr("Coverage of a paint", "પેન્ટનું coverage"),
          "f": "coverage (m2/L) = 10 x %solids/DFT(micron)",
          "terms": tr("60 % solids at 75 micron covers 8 m2 per litre, so 120 m2 takes 15 litres.",
                      "75 માઇક્રોમીટર પર 60 % solids લિટર દીઠ 8 m2 ઢાંકે, તેથી 120 m2 ને 15 લિટર.")},
         {"name": tr("Mass of paint", "પેન્ટનું દળ"),
          "f": "m = V x rho",
          "terms": tr("17.25 litres at 1.4 kg/L is 24.2 kg, which is what the store issues.",
                      "1.4 kg/L પર 17.25 લિટર એટલે 24.2 kg, જેટલું સ્ટોર આપે.")},
     ]},
]

VIVA = [
    {"title": tr("Surfaces and cleaning", "સપાટી અને સફાઈ"),
     "items": [
         {"q": tr("Why does a part usually fail at the surface and not in the middle?",
                  "ભાગ સામાન્ય રીતે વચ્ચે નહીં, સપાટી પર કેમ નિષ્ફળ જાય?"),
          "a": tr("Because the bending stress is highest there, the environment only touches there and "
                  "two sliding parts only meet there: the outer 10 % of the radius already carries 19 % "
                  "of the moment.",
                  "કારણ કે ત્યાં bending stress સૌથી વધુ હોય, પર્યાવરણ ફક્ત ત્યાં જ અડે અને સરકતા બે ભાગ ફક્ત "
                  "ત્યાં મળે: ત્રિજ્યાના બહારના 10 % જ moment ના 19 % ઉપાડે.")},
         {"q": tr("What is the cleaning sequence before a coating, and why is the order fixed?",
                  "કોટિંગ પહેલાં સફાઈનો ક્રમ શું, અને ક્રમ નિશ્ચિત કેમ?"),
          "a": tr("Degrease, pickle to remove scale, rinse, blast to a 50 - 75 micron profile and coat "
                  "the same day. Oil stops the acid from working, so grease must go first, and steel "
                  "starts to rust again within hours.",
                  "Degrease, scale કાઢવા pickle, rinse, 50 - 75 માઇક્રોમીટર profile સુધી blast અને એ જ "
                  "દિવસે કોટ. તેલ એસિડને કામ કરવા દે નહીં, તેથી grease પહેલાં જવું પડે, અને સ્ટીલ થોડા "
                  "કલાકમાં ફરી કાટ ખાવા લાગે.")},
         {"q": tr("Why does a paint specification give a blast profile in microns?",
                  "પેન્ટની specification blast profile માઇક્રોમીટરમાં કેમ આપે?"),
          "a": tr("Because the paint keys into the profile mechanically, like a key in a lock. A "
                  "polished surface gives nothing to grip and a coarse one leaves peaks that the film "
                  "cannot cover, so 50 - 75 micron is specified.",
                  "કારણ કે પેન્ટ profile માં યાંત્રિક રીતે પકડાય, ચાવી તાળામાં જેમ. ચળકતી સપાટી પકડવા "
                  "કંઈ આપતી નથી અને જાડી સપાટી એવી ટોચ છોડે જે ફિલ્મ ઢાંકી શકે નહીં, તેથી 50 - 75 માઇક્રોમીટર "
                  "લખાય.")},
     ]},
    {"title": tr("Coatings", "કોટિંગ"),
     "items": [
         {"q": tr("How does electroplating deposit a metal on to a part?",
                  "Electroplating ભાગ પર ધાતુ કેમ જમા કરે?"),
          "a": tr("The part is the cathode in a bath of the metal's own salt and a plate of that metal "
                  "is the anode. Metal dissolves at the anode, crosses as an ion and is reduced on the "
                  "part; Faraday's law gives the mass.",
                  "ભાગ એ ધાતુના પોતાના ક્ષારના સ્નાનમાં cathode છે અને એ ધાતુની પ્લેટ anode. ધાતુ anode પર "
                  "ઓગળે, ion તરીકે પસાર થાય અને ભાગ પર reduce થાય; Faraday નો નિયમ દળ આપે.")},
         {"q": tr("What is the difference between a sacrificial and a barrier coating?",
                  "Sacrificial અને barrier કોટિંગમાં શું ફરક?"),
          "a": tr("Zinc is sacrificial: it corrodes in place of the steel, so it still protects a "
                  "scratched area. Nickel, chrome and paint are barriers: they protect only while they "
                  "are continuous, and a scratch is a failure.",
                  "Zinc sacrificial છે: સ્ટીલને બદલે પોતે કાટ ખાય, તેથી ખરોચેલા ભાગને પણ રક્ષે. Nickel, chrome "
                  "અને પેન્ટ barrier છે: જ્યાં સુધી સતત હોય ત્યાં સુધી રક્ષે, અને ખરોચ એ નિષ્ફળતા છે.")},
         {"q": tr("Why is PVD used on a cutting tool and not on a large steel structure?",
                  "PVD cutting tool પર કેમ વપરાય, મોટા સ્ટીલ ઢાંચા પર નહીં?"),
          "a": tr("PVD makes a very hard, very thin film of 1 - 5 micron at under 500 C, but it is line "
                  "of sight and needs a vacuum chamber, so it suits a small, high-value tool and not a "
                  "bridge.",
                  "PVD 500 C ની નીચે 1 - 5 માઇક્રોમીટરની ખૂબ સખત, ખૂબ પાતળી ફિલ્મ બનાવે, પણ તે line of "
                  "sight છે અને vacuum chamber જોઈએ, તેથી નાના, મોંઘા tool ને શોભે, પુલને નહીં.")},
     ]},
    {"title": tr("Oils", "તેલ"),
     "items": [
         {"q": tr("What does the viscosity index of an oil tell you?",
                  "તેલનો viscosity index શું કહે છે?"),
          "a": tr("How little its viscosity falls when it is heated. Two oils can both be 10 cSt at "
                  "100 C, but at 30 C one is 110 cSt and the other 316 cSt, and the high-VI oil keeps "
                  "the film at running temperature.",
                  "ગરમ થતાં તેની viscosity કેટલી ઓછી ઘટે છે તે. બે તેલ 100 C પર 10 cSt હોઈ શકે, પણ 30 C પર એક "
                  "110 cSt અને બીજું 316 cSt, અને ઊંચા VI વાળું તેલ ચાલુ તાપમાને ફિલ્મ રાખે.")},
         {"q": tr("Why is an oil grade quoted at 40 C and not at room temperature?",
                  "તેલનો grade 40 C પર કેમ લખાય, રૂમ તાપમાને નહીં?"),
          "a": tr("Because 40 C is close to the running temperature of most industrial machines and it "
                  "is reproducible in a viscometer, so the grade means the same on every drum in every "
                  "country.",
                  "કારણ કે 40 C મોટા ભાગનાં ઔદ્યોગિક મશીનોના ચાલુ તાપમાનની નજીક છે અને viscometer માં પુનરાવર્તિત "
                  "થાય, તેથી grade દરેક દેશના દરેક ડ્રમ પર એક જ અર્થ આપે.")},
         {"q": tr("What does an anti-wear additive such as ZDDP actually do?",
                  "ZDDP જેવું anti-wear additive ખરેખર શું કરે?"),
          "a": tr("It reacts at the hot spots where asperities touch and builds a thin sacrificial film "
                  "of sulphide and phosphate, so the two surfaces slide on the film instead of "
                  "shearing each other.",
                  "તે એ ગરમ જગ્યાએ react કરે જ્યાં asperities અડે અને sulphide તથી phosphate ની પાતળી "
                  "બલિદાન ફિલ્મ બનાવે, તેથી બે સપાટી એકબીજા પર કાપવાને બદલે ફિલ્મ પર સરકે.")},
     ]},
    {"title": tr("Paint and corrosion", "પેન્ટ અને કાટ"),
     "items": [
         {"q": tr("What are the four things a corrosion cell needs?",
                  "Corrosion cell ને કઈ ચાર વસ્તુ જોઈએ?"),
          "a": tr("An anode that dissolves, a cathode that consumes electrons, an electrolyte to carry "
                  "the ions and a metallic path for the electrons. Remove any one and the corrosion "
                  "stops.",
                  "ઓગળતો anode, electrons વાપરતો cathode, ions લઈ જતું electrolyte અને electrons માટે ધાતુનો "
                  "રસ્તો. એક પણ દૂર કરો તો કાટ અટકે.")},
         {"q": tr("Why does stainless steel pit in sea water?",
                  "Stainless steel દરિયાના પાણીમાં pitting કેમ ખાય?"),
          "a": tr("Its protection is a passive chromium oxide film a few atoms thick. Chloride breaks "
                  "that film locally and stops it re-forming, so the attack goes in deep at one point "
                  "instead of spreading.",
                  "તેનું રક્ષણ થોડા atoms જાડી passive chromium oxide ફિલ્મ છે. Chloride એ ફિલ્મ સ્થાનિક રીતે "
                  "તોડે અને ફરી બનવા દે નહીં, તેથી હુમલો ફેલાવાને બદલે એક જગ્યાએ ઊંડો જાય.")},
         {"q": tr("What do the primer and the topcoat each do?",
                  "Primer અને topcoat દરેક શું કરે?"),
          "a": tr("The primer sticks to the blast and carries the inhibitive pigment that keeps the "
                  "steel passive where the film is damaged; the topcoat carries the colour and resists "
                  "UV and rain, so it protects the primer.",
                  "Primer blast સાથે ચોંટે અને inhibitive pigment ધરાવે જે ફિલ્મ બગડ્યાં જ્યાં સ્ટીલને passive "
                  "રાખે; topcoat રંગ ધરાવે અને UV તથી વરસાદ સામે ટકે, તેથી primer ને રક્ષે.")},
     ]},
]

_PRACTICE = [
    ("How long to plate twenty microns of nickel",
     "વીસ માઇક્રોમીટર nickel plating માટે કેટલો સમય",
     "A steel panel of 0.5 m2 is to be nickel plated to 20 micron. The current density is 300 A/m2, "
     "the cathode efficiency is 95 %, and for nickel M 58.7, n 2 and rho 8.9 g/cm3. Find the current, "
     "the mass of nickel needed and the plating time.",
     "0.5 m2 ના સ્ટીલ પેનલ પર 20 માઇક્રોમીટર nickel plating કરવાનું છે. Current density 300 A/m2, cathode "
     "efficiency 95 %, અને nickel માટે M 58.7, n 2 તથી rho 8.9 g/cm3. Current, જરૂરી nickel નું દળ અને "
     "plating નો સમય શોધો.",
     [h4("Step 1 - the current and the volume", "પગલું 1 - current અને ઘનફળ"),
      math("I = i A = 300 x 0.5 = 150 A",
           "V = 0.5 x 20e-6 = 1.0e-5 m3 = 10 cm3",
           "m = rho V = 8.9 x 10 = 89 g"),
      h4("Step 2 - Faraday for the time", "પગલું 2 - સમય માટે Faraday"),
      math("m = M I t eta/(n F)  ->  t = m n F/(M I eta)",
           "t = 89 x 2 x 96500/(58.7 x 150 x 0.95)",
           "t = 17177000/8365 = 2053 s"),
      h4("Step 3 - in minutes, and a check", "પગલું 3 - મિનિટમાં, અને ચકાસણી"),
      math("2053/60 = 34.2 min",
           "check with the rate: 300 A/m2 x 34.2 min = 11.7 micron per 20 min, so 20 micron",
           "needs 34 min - the two routes agree"),
      eq("150 A,  89 g of nickel,  34 minutes"),
      p("The 150 A is 5 A per square decimetre, which is a normal nickel bath. If the job must be "
        "faster, the answer is not more current - a higher current density burns the deposit, gives a "
        "dull, brittle, nodular film - but a bigger bath or two anodes and a rotating fixture.",
        "150 A એટલે પ્રતિ ચોરસ ડેસિમીટર 5 A, જે સામાન્ય nickel સ્નાન છે. કામ ઝડપી કરવું હોય તો જવાબ વધુ "
        "current નથી - વધુ current density deposit બાળે, ઝાંખી, ભંગુર, ગાંઠવાળી ફિલ્મ આપે - પણ મોટું સ્નાન કે "
        "બે anode અને ફરતું fixture."),
      check("Keep the units straight: M in kg/mol with m in kg, or M in g/mol with m in g - mixing them "
            "is a factor of a thousand. 89 g is right for 10 cm3 of nickel.",
            "એકમ સીધા રાખો: m kg માં હોય તો M kg/mol, m g માં હોય તો M g/mol - મિશ્ર કરવાથી હજાર ગણો ફરક "
            "પડે. 10 cm3 nickel માટે 89 g સાચું છે.")],
     7),

    ("Corrosion rate from a mass loss",
     "દળના વ્યય પરથી corrosion rate",
     "A steel coupon 50 mm x 25 mm x 3 mm is exposed for 90 days and loses 1.2 g. Taking rho 7.85 "
     "g/cm3, find the corrosion rate in mm per year and the wall it would lose in 10 years.",
     "50 mm x 25 mm x 3 mm નો સ્ટીલ coupon 90 દિવસ રાખ્યા પછી 1.2 g ગુમાવે છે. rho 7.85 g/cm3 લઈને "
     "mm પ્રતિ વર્ષમાં corrosion rate અને 10 વર્ષમાં જતી દીવાલ શોધો.",
     [h4("Step 1 - the exposed area and the time", "પગલું 1 - ખુલ્લું area અને સમય"),
      math("A = 2(50x25 + 50x3 + 25x3) = 2(1250 + 150 + 75) = 2950 mm2 = 29.5 cm2",
           "t = 90 x 24 = 2160 h"),
      h4("Step 2 - the rate", "પગલું 2 - દર"),
      math("CR = 87.6 W/(rho A t)   with W in mg",
           "CR = 87.6 x 1200/(7.85 x 29.5 x 2160)",
           "CR = 105120/500239 = 0.21 mm per year"),
      h4("Step 3 - and over ten years", "પગલું 3 - દસ વર્ષમાં"),
      math("loss = 0.21 x 10 = 2.1 mm"),
      eq("0.21 mm per year,  so 2.1 mm of wall in 10 years"),
      p("Two millimetres on a 6 mm pipe wall is the difference between a serviceable line and a leak. "
        "That is why a corrosion rate is always quoted as a thickness per year and never as a mass "
        "loss: the drawing is in millimetres.",
        "6 mm પાઇપની દીવાલ પર બે મિલીમીટર એટલે વાપરી શકાય તેવી લાઇન અને ગળતર વચ્ચેનો ફરક. તેથી corrosion "
        "rate હંમેશા વર્ષ દીઠ જાડાઈ તરીકે લખાય, દળના વ્યય તરીકે કદી નહીં: ડ્રોઇંગ મિલીમીટરમાં છે."),
      check("The formula needs W in milligrams, A in square centimetres and t in hours: 1.2 g is 1200 "
            "mg and 29.5 cm2 is not 2950.",
            "સૂત્રમાં W મિલિગ્રામમાં, A ચોરસ સેન્ટીમીટરમાં અને t કલાકમાં જોઈએ: 1.2 g એટલે 1200 mg અને "
            "29.5 cm2, 2950 નહીં.")],
     7),

    ("The zinc anode that protects a tank",
     "ટાંકીને રક્ષતો zinc anode",
     "A steel water tank has 2.5 m2 of wetted surface and is protected at a current density of 20 "
     "mA/m2 for 2 years. For zinc M 65.4 and n 2, and an anode utilisation of 90 %, find the zinc "
     "that is consumed and the anode mass to fit.",
     "સ્ટીલની પાણીની ટાંકીની ભીની સપાટી 2.5 m2 છે અને તેને 20 mA/m2 ના current density પર 2 વર્ષ રક્ષવાની "
     "છે. Zinc માટે M 65.4 અને n 2, અને anode નો 90 % ઉપયોગ લઈને ખર્ચાતું zinc અને લગાવવાનો anode દળ શોધો.",
     [h4("Step 1 - the current and the time", "પગલું 1 - current અને સમય"),
      math("I = 20e-3 x 2.5 = 0.050 A",
           "t = 2 x 365 x 24 x 3600 = 6.31e7 s"),
      h4("Step 2 - Faraday for the zinc", "પગલું 2 - zinc માટે Faraday"),
      math("m = M I t/(n F) = 65.4 x 0.050 x 6.31e7/(2 x 96500)",
           "m = 2.06e8/193000 = 1069 g = 1.07 kg"),
      h4("Step 3 - the anode to fit", "પગલું 3 - લગાવવાનો anode"),
      math("at 90 % utilisation: 1.07/0.90 = 1.19 kg",
           "a 2 kg anode therefore covers the two years with a margin"),
      eq("0.050 A,  1.07 kg of zinc consumed,  a 2 kg anode fitted"),
      p("This is cathodic protection in its simplest form: the zinc is the anode of a cell whose "
        "cathode is the whole tank, so the tank cannot corrode at all while a scrap of zinc remains. "
        "The same sum with an impressed current replaces the zinc with a rectifier and a inert anode.",
        "આ cathodic protection નું સાદું સ્વરૂપ છે: zinc એ cell નો anode છે જેનો cathode આખી ટાંકી છે, તેથી zinc "
        "જ્યાં સુધી બાકી છે ત્યાં સુધી ટાંકી કાટ ખાઈ શકે નહીં. એ જ ગણતરી impressed current સાથે zinc ને "
        "rectifier અને inert anode થી બદલે."),
      check("Convert years to seconds before Faraday, and remember that only 90 % of the anode actually "
            "dissolves usefully - the rest is the part that corrodes away holding the bracket.",
            "Faraday પહેલાં વર્ષને સેકન્ડમાં ફેરવો, અને યાદ રાખો કે anode ના ફક્ત 90 % કામમાં ઓગળે - બાકીનો "
            "ભાગ bracket પકડતો કાટ ખાઈ જાય છે.")],
     7),

    ("Viscosity at the running temperature",
     "ચાલુ તાપમાને viscosity",
     "An oil has 68 cSt at 40 C and 8.6 cSt at 100 C. Use the Walther equation to find its viscosity "
     "at the running temperature of 60 C, and say what the drop means for the pump.",
     "એક તેલ 40 C પર 68 cSt અને 100 C પર 8.6 cSt છે. Walther સમીકરણ વાપરીને 60 C ના ચાલુ તાપમાને તેની "
     "viscosity શોધો, અને આ ઘટાડો pump માટે શું અર્થ ધરાવે તે કહો.",
     [h4("Step 1 - the two points in Walther form", "પગલું 1 - બે બિંદુ Walther સ્વરૂપમાં"),
      math("Z = nu + 0.7;  Y = log10(log10 Z);  T in kelvin",
           "40 C: Z = 68.7, log10 Z = 1.83696, Y = 0.26406, log10 T = 2.49575",
           "100 C: Z = 9.3, log10 Z = 0.96848, Y = -0.01391, log10 T = 2.57188"),
      h4("Step 2 - the two constants", "પગલું 2 - બે અચળાંક"),
      math("B = (0.26406 + 0.01391)/(2.57188 - 2.49575) = 0.27797/0.07613 = 3.651",
           "A = 0.26406 + 3.651 x 2.49575 = 9.377"),
      h4("Step 3 - the viscosity at 60 C", "પગલું 3 - 60 C પર viscosity"),
      math("log10 T = log10(333.15) = 2.52258",
           "Y = 9.377 - 3.651 x 2.52258 = 0.1667",
           "log10 Z = 10^0.1667 = 1.4679  ->  Z = 29.4  ->  nu = 28.7 cSt"),
      eq("28.7 cSt at 60 C, from 68 cSt at 40 C"),
      p("The viscosity falls by 58 % over 20 K, which is normal for a mineral oil of VI about 100. "
        "That is why a pump is selected for the viscosity it will see at its running temperature and "
        "why a cold start is the case that decides the pipe size: at 30 C the same oil is near 300 cSt "
        "and needs a much bigger suction line.",
        "20 K માં viscosity 58 % ઘટે, જે VI લગભગ 100 વાળા ખનીજ તેલ માટે સામાન્ય છે. તેથી pump તેની ચાલુ "
        "તાપમાનની viscosity માટે પસંદ થાય અને ઠંડી શરૂઆત જ પાઇપનું માપ નક્કી કરે: 30 C પર એ જ તેલ લગભગ "
        "300 cSt હોય અને ઘણી મોટી suction લાઇન માંગે."),
      check("A sanity check is always available: the answer at 60 C must lie between 8.6 and 68 cSt, "
            "and nearer the low end because viscosity falls fast. 28.7 satisfies both.",
            "ચકાસણી હંમેશા શક્ય છે: 60 C નો જવાબ 8.6 અને 68 cSt વચ્ચે હોવો જોઈએ, અને નીચેની ધારની નજીક, "
            "કારણ કે viscosity ઝડપથી ઘટે. 28.7 બંને પૂરા કરે.")],
     6),

    ("How much paint for a hundred and twenty square metres",
     "સો વીસ ચોરસ મીટર માટે કેટલો પેન્ટ",
     "A steel structure of 120 m2 is to have a zinc-rich primer at 75 micron dry film. The paint is "
     "60 % solids by volume at 1.4 kg per litre, application loss is 15 % and it costs Rs 450 a "
     "litre. Find the wet film thickness, the litres and kilograms to buy, and the paint cost.",
     "120 m2 ના સ્ટીલ ઢાંચા પર 75 માઇક્રોમીટર સૂકી ફિલ્મનો zinc ભરપૂર primer ચઢાવવાનો છે. પેન્ટમાં "
     "volume પ્રમાણે 60 % solids, લિટર દીઠ 1.4 kg, ચઢાવતાં 15 % વ્યય અને લિટરનો ભાવ Rs 450 છે. ભીની "
     "ફિલ્મની જાડાઈ, ખરીદવાના લિટર અને કિલો, અને પેન્ટનો ખર્ચ શોધો.",
     [h4("Step 1 - wet film and volume", "પગલું 1 - ભીની ફિલ્મ અને ઘનફળ"),
      math("WFT = 75 x 100/60 = 125 micron",
           "V = 120 x 125e-6 = 0.015 m3 = 15 L"),
      h4("Step 2 - with the application loss", "પગલું 2 - ચઢાવવાના વ્યય સાથે"),
      math("15 x 1.15 = 17.25 L, so 18 L are bought",
           "m = 17.25 x 1.4 = 24.2 kg"),
      h4("Step 3 - the money", "પગલું 3 - પૈસા"),
      math("cost = 17.25 x 450 = Rs 7,763"),
      eq("125 micron wet,  17.25 litres,  24.2 kg,  Rs 7,763 of paint"),
      p("The 15 % loss is not a mistake in the sum, it is part of the method: 5 % stays in the tin and "
        "the pump, 5 % is overspray and 5 % is lost on edges and welds where the film cannot be "
        "controlled. A specification that ignores it runs out of paint on the last two metres.",
        "15 % વ્યય ગણતરીની ભૂલ નથી, પદ્ધતિનો ભાગ છે: 5 % ડબ્બા અને pump માં રહે, 5 % overspray જાય અને 5 % "
        "ધાર તથી welds પર જાય જ્યાં ફિલ્મ નિયંત્રિત ન થાય. જે specification તેને ગણે નહીં તે છેલ્લા બે મીટરમાં "
        "પેન્ટ વગર રહે."),
      check("Coverage is a quick cross-check: 10 x 60/75 = 8 m2 per litre, and 120/8 = 15 litres "
            "without loss. Two independent routes, the same 15 litres.",
            "Coverage ઝડપી ચકાસણી છે: 10 x 60/75 = લિટર દીઠ 8 m2, અને વ્યય વગર 120/8 = 15 લિટર. બે અલગ "
            "રસ્તા, એ જ 15 લિટર.")],
     6),

    ("Does a six millimetre pipe last twelve years",
     "6 મિલીમીટરની પાઇપ 12 વર્ષ ટકશે?",
     "A cooling water line is 6.0 mm wall plain carbon steel with a minimum allowable wall of 4.5 mm. "
     "The measured corrosion rate is 0.25 mm per year. Find the life of the line, the wall needed for "
     "a 12 year life, and one alternative.",
     "કૂલિંગ વોટર લાઇનની દીવાલ 6.0 mm સાદું carbon steel છે અને લઘુતમ માન્ય દીવાલ 4.5 mm છે. માપેલો "
     "corrosion rate 0.25 mm પ્રતિ વર્ષ છે. લાઇનનું આયુષ્ય, 12 વર્ષ માટે જરૂરી દીવાલ, અને એક વિકલ્પ શોધો.",
     [h4("Step 1 - the metal available", "પગલું 1 - ઉપલબ્ધ ધાતુ"),
      math("available = 6.0 - 4.5 = 1.5 mm"),
      h4("Step 2 - the life", "પગલું 2 - આયુષ્ય"),
      math("life = 1.5/0.25 = 6 years"),
      h4("Step 3 - the wall for twelve years, and an alternative", "પગલું 3 - 12 વર્ષ માટે દીવાલ, અને વિકલ્પ"),
      math("allowance needed = 0.25 x 12 = 3.0 mm  ->  wall 4.5 + 3.0 = 7.5 mm",
           "or keep 6.0 mm and bring the rate below 1.5/12 = 0.125 mm/year",
           "a coating or an inhibitor is what buys that half rate"),
      eq("6 years as it stands,  7.5 mm wall for 12 years,  or halve the corrosion rate"),
      p("Every line like this is a choice between three costs: a thicker wall once, a treatment that "
        "is maintained for ever, or a replacement in six years. The calculation is not the hard part; "
        "the hard part is that the rate must be measured where the line actually runs, because a "
        "cooling line corrodes eight times faster at a weld than in the straight.",
        "આવી દરેક લાઇન ત્રણ ખર્ચ વચ્ચેની પસંદગી છે: એક વાર જાડી દીવાલ, કાયમ જાળવવી પડતી સારવાર, કે છ વર્ષે "
        "બદલી. ગણતરી કઠિન ભાગ નથી; કઠિન ભાગ એ છે કે દર ત્યાં માપવો પડે જ્યાં લાઇન ખરેખર ચાલે, કારણ કે "
        "કૂલિંગ લાઇન weld પર સીધા ભાગ કરતાં આઠ ગણી ઝડપથી કાટ ખાય."),
      check("The minimum wall is a code number, not a preference: the 4.5 mm is what the line needs at "
            "the design pressure, so the corrosion allowance is added on top of it and never taken out "
            "of it.",
            "લઘુતમ દીવાલ code નો આંકડો છે, પસંદગી નહીં: 4.5 mm design pressure પર લાઇનને જોઈએ તેટલું છે, "
            "તેથી corrosion allowance તેની ઉપર ઉમેરાય, તેમાંથી કદી બાદ ન થાય.")],
     6),
]

PRACTICE = [(tr(h_en, h_gu), tr(q_en, q_gu), body(*parts_), m)
            for (h_en, h_gu, q_en, q_gu, parts_, m) in _PRACTICE]

EXAM = [{"q": q, "marks": m} for _, q, _, m in PRACTICE]
PRACTICE_ANSWERS = [a for _, _, a, _ in PRACTICE]

SOURCES = [
    ("GTU DI01000181 Engineering Materials Science syllabus (uploaded PDF, w.e.f. 2024-25)",
     "https://syllabus.gtu.ac.in/"),
    ("O. P. Khanna - Material Science and Metallurgy, Dhanpat Rai (corrosion, surface treatment, "
     "lubricants)", "https://www.dhanpatrai.com/"),
    ("V. Raghavan - Materials Science and Engineering, Prentice Hall India (corrosion, oxidation)",
     "https://www.pearson.com/"),
    ("Substech open materials science reference - electrochemical corrosion, protective coatings",
     "https://www.substech.com/dokuwiki/doku.php?id=corrosion"),
    ("NACE / AMPP corrosion basics - corrosion rate, cathodic protection, forms of attack",
     "https://www.ampp.org/"),
    ("BIS - IS 3448 viscosity grades, IS 1448 methods of test for petroleum products",
     "https://www.bis.gov.in/"),
]
