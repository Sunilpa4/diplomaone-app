"""DI01000181 Unit 6, part E: equations, viva, six solved numericals and sources."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from subject_DI01000181 import tr  # noqa: E402
from content_DI01000181_lib import (p, h4, table, math, eq, why, check, pit,  # noqa: E402
                                    body, ul, ol)

EQUATIONS = [
    {"title": tr("Green material accounting", "Green સામગ્રીનો હિસાબ"),
     "items": [
         {"name": tr("Embodied energy of a part", "ભાગની embodied energy"),
          "f": "EE = sum(m_i x e_i)",
          "terms": tr("Mass of each material in kilograms times its MJ per kilogram. A 20 kg aluminium "
                      "part is 3400 MJ; the same part in steel is 500 MJ.",
                      "દરેક સામગ્રીનું દળ કિલોગ્રામમાં ગુણ્યું તેના MJ પ્રતિ કિલોગ્રામ સાથે. 20 કિલોનો "
                      "aluminium ભાગ 3400 MJ; એ જ ભાગ સ્ટીલમાં 500 MJ.")},
         {"name": tr("Energy payback distance", "Energy payback અંતર"),
          "f": "d = dEE/(saving per km)",
          "terms": tr("The extra embodied energy of the lighter part divided by the energy it saves "
                      "per kilometre: 752 MJ against 0.836 MJ/km is 900 km.",
                      "હલકા ભાગની વધારાની embodied energy ભાગ્યા પ્રતિ કિલોમીટરની બચત: 752 MJ સામે "
                      "0.836 MJ/km એટલે 900 કિલોમીટર.")},
         {"name": tr("Recycling saving", "Recycling બચત"),
          "f": "saving % = (1 - e_rec/e_new) x 100",
          "terms": tr("Aluminium 8 against 170 saves 95 %, steel 10 against 25 saves 60 %, glass 12 "
                      "against 15 saves 20 %.",
                      "aluminium 170 સામે 8 એટલે 95 % બચત, સ્ટીલ 25 સામે 10 એટલે 60 %, કાચ 15 સામે 12 "
                      "એટલે 20 %.")},
         {"name": tr("Specific strength and stiffness", "Specific strength અને stiffness"),
          "f": "specific strength = sigma/rho,  specific stiffness = E/rho",
          "terms": tr("Steel 57, aluminium 115, GFRP 158, CFRP 938 kN m per kg. For a panel the "
                      "stiffness version is nearer the truth.",
                      "સ્ટીલ 57, aluminium 115, GFRP 158, CFRP 938 kN m પ્રતિ kg. પેનલ માટે stiffness "
                      "વાળું સૂત્ર સત્યની નજીક છે.")},
     ]},
    {"title": tr("Solar photovoltaics", "સોલાર ફોટોવોલ્ટેઇક"),
     "items": [
         {"name": tr("Peak power of a module", "Module ની peak power"),
          "f": "P = G A eta",
          "terms": tr("At G 1000 W/m2, 2 m2 and 20 % the answer is 400 W - the number on the label.",
                      "G 1000 W/m2, 2 m2 અને 20 % પર જવાબ 400 W - લેબલ પરનો આંકડો.")},
         {"name": tr("Daily energy", "દૈનિક ઊર્જા"),
          "f": "E_day = P x PSH x PR",
          "terms": tr("Peak sun hours and a performance ratio of 0.8 for dust, heat and the inverter: "
                      "0.4 x 5 x 0.8 = 1.6 kWh in Surat.",
                      "Peak sun hour અને ધૂળ, ગરમી તથી inverter માટે 0.8 performance ratio: સુરતમાં "
                      "0.4 x 5 x 0.8 = 1.6 kWh.")},
         {"name": tr("Area for a load", "ભાર માટે ક્ષેત્ર"),
          "f": "A = E/(G eta PSH PR)",
          "terms": tr("4 kWh a day needs 5 m2 of 20 % module, and the roof, not the module, is usually "
                      "the limit.",
                      "દિવસના 4 kWh માટે 20 % module ના 5 m2 જોઈએ, અને મર્યાદા સામાન્ય રીતે છત હોય, "
                      "module નહીં.")},
     ]},
    {"title": tr("Battery and electric vehicle", "Battery અને ઇલેક્ટ્રિક વાહન"),
     "items": [
         {"name": tr("Cell and pack energy", "Cell અને pack ની ઊર્જા"),
          "f": "E = V x Ah   (pack: V = n_s V_cell, Ah = n_p Ah_cell)",
          "terms": tr("96 cells of 3.7 V and 50 Ah in series gives 355 V and 17.8 kWh; two strings in "
                      "parallel give 35.5 kWh.",
                      "3.7 V અને 50 Ah ના 96 cell series માં 355 V અને 17.8 kWh આપે; બે string parallel માં "
                      "35.5 kWh.")},
         {"name": tr("Specific energy", "Specific energy"),
          "f": "e = E/m",
          "terms": tr("Cells 205 Wh/kg, the pack 150 Wh/kg, and the difference is the casing, the "
                      "cooling plate and the busbars.",
                      "cell 205 Wh/kg, pack 150 Wh/kg, અને ફરક casing, cooling plate અને busbar નો છે.")},
         {"name": tr("Range", "અંતર"),
          "f": "range = E/consumption",
          "terms": tr("35.5 kWh at 0.15 kWh per km is 237 km - and 0.05 kWh per km of that is the mass "
                      "of the pack itself.",
                      "0.15 kWh પ્રતિ km આગળ 35.5 kWh એટલે 237 km - અને એમાં 0.05 kWh પ્રતિ km pack ના "
                      "પોતાના દળનો છે.")},
         {"name": tr("CO2 per kilometre", "પ્રતિ કિલોમીટર CO2"),
          "f": "g/km = EF x consumption",
          "terms": tr("0.71 kg CO2 per kWh on the Indian grid at 0.15 kWh/km is 107 g/km, against 139 "
                      "g/km for a petrol car at 6 L/100 km.",
                      "ભારતીય grid પર 0.71 kg CO2 પ્રતિ kWh, 0.15 kWh/km આગળ 107 g/km, જ્યારે 6 L/100 km "
                      "વાળી પેટ્રોલ કાર 139 g/km.")},
     ]},
    {"title": tr("Recycling and life", "Recycling અને આયુષ્ય"),
     "items": [
         {"name": tr("Scrap recovered", "વસૂલ થતો ભંગાર"),
          "f": "m_rec = m_total x scrap % x recovery %",
          "terms": tr("1000 t of pressings at 18 % scrap and 92 % recovery gives 165.6 t back to the "
                      "furnace.",
                      "18 % scrap અને 92 % recovery આગળ 1000 ટન pressings પૈકી 165.6 ટન ભઠ્ઠીમાં "
                      "પાછા.")},
         {"name": tr("Value of the scrap", "ભંગારની કિંમત"),
          "f": "value = m_rec x rate",
          "terms": tr("165.6 t at Rs 32 per kg is Rs 53 lakh a year - a material account, not a waste "
                      "account.",
                      "165.6 ટન, કિલોએ રૂ 32 એટલે વર્ષે રૂ 53 લાખ - એ કચરાનું નહીં, સામગ્રીનું ખાતું છે.")},
         {"name": tr("CO2 avoided by recycling", "Recycling થી ટળતું CO2"),
          "f": "dCO2 = m x (c_new - c_rec)",
          "terms": tr("20 kg of aluminium: 230 kg of CO2 new against 10 kg from scrap, so 220 kg "
                      "avoided on one part.",
                      "20 કિલો aluminium: નવું 230 કિલો CO2 સામે scrap થી 10 કિલો, એટલે એક ભાગ પર 220 કિલો "
                      "ટળે.")},
     ]},
]

VIVA = [
    {"title": tr("Green materials", "Green materials"),
     "items": [
         {"q": tr("What makes a material green?", "સામગ્રી green ક્યારે કહેવાય?"),
          "a": tr("Four counts, and none of them alone: renewable, recyclable, low impact per kilogram "
                  "delivered, and durable. A material that is grown but thrown away, or recycled but "
                  "weak, fails the test.",
                  "ચાર ગણતરી, અને એકલી કોઈ નહીં: renewable, recyclable, પ્રતિ કિલોગ્રામ ઓછી અસર, અને "
                  "ટકાઉ. ઊગે પણ ફેંકાય તેવી, કે recycle થાય પણ નબળી હોય તેવી સામગ્રી કસોટીમાં નિષ્ફળ જાય.")},
         {"q": tr("What is embodied energy, and why is it quoted per kilogram?",
                  "Embodied energy શું, અને પ્રતિ કિલોગ્રામ કેમ?"),
          "a": tr("The primary energy needed to deliver a kilogram of the material ready to use, from "
                  "the mine to the loading bay. Per kilogram is what makes two materials comparable, "
                  "because the part's mass then multiplies it into the bill.",
                  "ખાણથી લોડિંગ બે થી વાપરવા તૈયાર એક કિલોગ્રામ પહોંચાડવા જોઈતી પ્રાથમિક ઊર્જા. પ્રતિ "
                  "કિલોગ્રામ હોવાથી બે સામગ્રી સરખાવી શકાય, કારણ કે ભાગનું દળ ગુણાઈને બિલ બનાવે.")},
         {"q": tr("Why does recycling aluminium save so much more than recycling glass?",
                  "Recycling થી aluminium માં કાચ કરતાં ઘણી વધુ બચત કેમ?"),
          "a": tr("Because smelting aluminium from alumina is an electrolytic process with a very high "
                  "energy input, and re-melting the metal needs only 5 % of it. Glass is already made by "
                  "melting, so its second melt saves only the 20 % that the raw materials and the "
                  "reaction cost.",
                  "કારણ કે alumina થી aluminium smelt કરવું ખૂબ ઊંચી ઊર્જા માંગતી electrolytic પ્રક્રિયા છે, "
                  "અને ધાતુ ફરી ઓગાળવા તેના ફક્ત 5 % જોઈએ. કાચ તો ઓગાળીને જ બનેલો હોય, તેથી બીજા ઓગળવામાં "
                  "ફક્ત કાચો માલ અને પ્રક્રિયાના 20 % બચે.")},
     ]},
    {"title": tr("Vehicles and batteries", "વાહન અને battery"),
     "items": [
         {"q": tr("Is an electric car made of different materials from a petrol car?",
                  "ઇલેક્ટ્રિક કાર પેટ્રોલ કાર કરતાં જુદી સામગ્રીની બને છે?"),
          "a": tr("Mostly not: steel, aluminium and polymer are the same list. What changes is"
                  " the copper, three times as much, and the 225 kg battery that did not exist before.",
                  "મોટે ભાગે નહીં: સ્ટીલ, aluminium અને polymer એ જ યાદી છે. બદલાય છે copper - ત્રણ ગણું - "
                  "અને 225 કિલોની battery જે પહેલાં નહોતી.")},
         {"q": tr("What are the five materials in a lithium-ion cell?",
                  "લિથિયમ-ion cell માં પાંચ સામગ્રી કઈ?"),
          "a": tr("Aluminium current collector, lithium metal oxide cathode, separator with "
                  "electrolyte, graphite anode and copper current collector - 150 micrometres in all, "
                  "3.7 V and 185 Wh for the cell.",
                  "aluminium current collector, lithium metal oxide cathode, electrolyte સાથે separator, "
                  "graphite anode અને copper current collector - કુલ 150 માઇક્રોમીટર, cell માટે 3.7 V અને "
                  "185 Wh.")},
         {"q": tr("Why has LFP come back against NMC?", "NMC સામે LFP પાછું કેમ આવ્યું?"),
          "a": tr("LFP is iron and phosphorus instead of nickel and cobalt: cheaper, safer, and 3000 "
                  "cycles instead of 1500. It gives 140 Wh/kg against 220, so it wins where there is "
                  "room for a bigger pack.",
                  "LFP માં nickel અને cobalt ને બદલે લોહ અને ફોસ્ફરસ છે: સસ્તું, સલામત, અને 1500 ને બદલે "
                  "3000 cycle. તે 220 સામે 140 Wh/kg આપે, તેથી જ્યાં મોટું pack ગોઠવાય ત્યાં જીતે.")},
     ]},
    {"title": tr("Renewable energy", "નવીનીકરણીય ઊર્જા"),
     "items": [
         {"q": tr("A panel is 20 % efficient. What is the other 80 %?",
                  "પેનલ 20 % efficient છે. બાકીના 80 % શું?"),
          "a": tr("Four fifths of the sunlight is reflected, absorbed as heat below the band gap or lost "
                  "as heat from the excited electrons; and by mass it is the glass, frame, encapsulant "
                  "and backsheet that hold the cells, not the cells.",
                  "પાંચમાંથી ચાર ભાગ સૂર્યપ્રકાશ પરાવર્તિત થાય, band gap નીચે ગરમી તરીકે શોષાય કે "
                  "ઉત્તેજિત electrons ની ગરમી તરીકે જાય; અને દળ પ્રમાણે એ કાચ, frame, encapsulant અને "
                  "backsheet છે જે cell પકડે, cell નહીં.")},
         {"q": tr("Why is a wind blade a composite and the tower steel?",
                  "પવન blade composite અને tower સ્ટીલ કેમ?"),
          "a": tr("The blade must be stiff and light because every kilogram at 80 m radius is a bending "
                  "moment, and carbon epoxy gives 75 GPa per g/cm3 against 25 for steel. The tower only "
                  "has to carry compression, so plate steel is cheaper and weldable.",
                  "blade કઠોર અને હલકું જોઈએ કારણ કે 80 મીટર ત્રિજ્યા પર દરેક કિલોગ્રામ bending moment છે, "
                  "અને carbon epoxy પ્રતિ g/cm3 75 GPa આપે, સ્ટીલ 25. tower ને ફક્ત compression ઉપાડવું "
                  "પડે, તેથી પ્લેટ સ્ટીલ સસ્તું અને weldable છે.")},
         {"q": tr("What is the end-of-life problem of a wind blade?",
                  "પવન blade ની end-of-life સમસ્યા શું?"),
          "a": tr("It is a thermoset: cross-linked epoxy that cannot be melted, so 60 tonnes per turbine "
                  "goes to cement kilns or landfill. Thermoplastic resins and recyclable epoxy are the "
                  "answer being built now.",
                  "એ thermoset છે: cross-linked epoxy જે ઓગળે નહીં, તેથી પ્રતિ turbine 60 ટન સિમેન્ટ ભઠ્ઠી કે "
                  "landfill જાય. thermoplastic resin અને recyclable epoxy એ હવે બનતો જવાબ છે.")},
     ]},
    {"title": tr("Advanced materials", "Advanced materials"),
     "items": [
         {"q": tr("Why is specific strength used instead of strength?",
                  "મજબૂતાઈને બદલે specific strength કેમ?"),
          "a": tr("Because a moving part carries its own mass: UTS divided by density compares what a "
                  "kilogram of material can do, and that is the fair comparison between steel at 57 and "
                  "CFRP at 938 kN m per kg.",
                  "કારણ કે ચાલતો ભાગ પોતાનું દળ ઉપાડે: UTS ભાગ્યા ઘનતા સરખાવે કે એક કિલોગ્રામ સામગ્રી શું "
                  "કરી શકે, અને એ જ 57 વાળા સ્ટીલ અને 938 kN m પ્રતિ kg વાળા CFRP વચ્ચેની ન્યાયી તુલના છે.")},
         {"q": tr("What does an NdFeB magnet give a motor that a ferrite does not?",
                  "NdFeB magnet ferrite કરતાં motor ને શું આપે?"),
          "a": tr("Energy product: 250 to 400 kJ/m3 against 30, and 1.3 T against 0.4 T. The same torque "
                  "comes from a much smaller and lighter motor, which is why a 150 kW unit fits in 40 kg.",
                  "Energy product: 30 સામે 250 - 400 kJ/m3, અને 0.4 T સામે 1.3 T. એ જ torque ઘણા નાના અને "
                  "હલકા motor માંથી મળે, તેથી 150 kW એકમ 40 કિલોમાં આવે.")},
         {"q": tr("Is the lightest material always the greenest choice?",
                  "સૌથી હલકી સામગ્રી હંમેશા સૌથી green પસંદગી છે?"),
          "a": tr("No. CFRP is the lightest structural choice at 938 kN m per kg but carries 500 MJ/kg "
                  "and cannot be melted, so on a hatchback aluminium at 170 MJ/kg and 8 from scrap is "
                  "the greener answer - check the payback distance.",
                  "ના. CFRP 938 kN m પ્રતિ kg સાથે સૌથી હલકી માળખાકીય પસંદગી છે પણ 500 MJ/kg ધરાવે અને "
                  "ઓગળે નહીં, તેથી hatchback પર 170 MJ/kg અને scrap થી 8 વાળું aluminium વધુ green જવાબ છે "
                  "- payback અંતર ચકાસો.")},
     ]},
]

_PRACTICE = [
    ("A lightweight subframe, and whether it pays back",
     "હલકું subframe, અને તે payback થાય છે કે નહીં",
     "A steel subframe of 12 kg is to be replaced by an aluminium one of equal stiffness, which needs "
     "1.5 times the section area. Steel is 7.85 g/cm3 and 25 MJ/kg; aluminium is 2.70 g/cm3, 170 MJ/kg "
     "primary and 8 MJ/kg secondary. The car covers 200 000 km and saves 0.4 kWh per 100 km per 100 kg. "
     "Find the new mass, the mass saved, and the distance over which the extra embodied energy is paid "
     "back for primary aluminium, for 60 % recycled aluminium, and for scrap-only aluminium.",
     "12 કિલોનું સ્ટીલ subframe એ જ કઠોરતા વાળા aluminium થી બદલવાનું છે, જેના માટે 1.5 ગણું section area "
     "જોઈએ. સ્ટીલ 7.85 g/cm3 અને 25 MJ/kg; aluminium 2.70 g/cm3, primary 170 MJ/kg અને secondary 8 MJ/kg. "
     "કાર 200,000 km ચાલે અને પ્રતિ 100 km પ્રતિ 100 kg 0.4 kWh બચાવે. નવું દળ, બચેલું દળ, અને primary "
     "aluminium, 60 % recycled aluminium તથી ફક્ત scrap ના aluminium માટે વધારાની embodied energy કેટલા "
     "અંતરે payback થાય તે શોધો.",
     [h4("Step 1 - the mass of the aluminium part", "પગલું 1 - aluminium ભાગનું દળ"),
      math("m = 12 x (2.70/7.85) x 1.5 = 12 x 0.344 x 1.5",
           "m = 6.19 kg, so 5.81 kg saved, 48 %",
           "the 1.5 is the price of stiffness: aluminium has a third of the modulus of steel"),
      h4("Step 2 - the extra embodied energy, three routes", "પગલું 2 - વધારાની embodied energy, ત્રણ માર્ગ"),
      math("primary: 6.19 x 170 = 1052 MJ - 12 x 25 = 300  ->  + 752 MJ",
           "60 % recycled: e = 0.6 x 8 + 0.4 x 170 = 72.8 MJ/kg -> 451 MJ  ->  + 151 MJ",
           "scrap only: 6.19 x 8 = 50 MJ  ->  - 250 MJ, lighter than the steel it replaces"),
      h4("Step 3 - the payback distance", "પગલું 3 - payback અંતર"),
      math("saving = 0.4 x 0.0581 = 0.0232 kWh per 100 km = 0.000232 kWh/km = 0.836 kJ/km",
           "primary: 752/0.000836 = 900 000 km - four times the life of the car",
           "60 % recycled: 151/0.000836 = 180 000 km - paid back inside the 200 000 km"),
      eq("6.19 kg,  5.81 kg saved,  752 MJ extra,  payback 900 000 km primary / 180 000 km recycled"),
      p("The answer is uncomfortable and useful: primary aluminium is the wrong way to build a green "
        "car. The same part is green only when the metal is secondary, and the specification that "
        "decides it is the recycled content written on the drawing - 60 % is enough to pay back inside "
        "the life, 100 % saves energy from the first kilometre. Lightweighting is not a material "
        "choice, it is a specification choice.",
        "જવાબ અઘરો અને ઉપયોગી છે: primary aluminium green કાર બનાવવાનો ખોટો રસ્તો છે. એ જ ભાગ ત્યારે જ "
        "green છે જ્યારે ધાતુ secondary હોય, અને તે નક્કી કરતી specification ડ્રોઇંગ પર લખાયેલું recycled "
        "content છે - 60 % જીવનકાળમાં payback થવા પૂરતું છે, 100 % પહેલા કિલોમીટરથી ઊર્જા બચાવે. "
        "Lightweighting સામગ્રીની પસંદગી નહીં, specification ની પસંદગી છે."),
      check("watch the units, because this is the step that goes wrong: 0.0232 kWh per 100 km is "
            "0.000232 kWh per km, which is 0.836 kJ/km - not 0.836 MJ/km. Slip one decimal and the "
            "payback changes from 900 000 km to 900 km.",
            "એકમ પર ધ્યાન રાખો, કારણ કે આ પગલું જ ખોટું પડે: 0.0232 kWh પ્રતિ 100 km એટલે 0.000232 kWh "
            "પ્રતિ km, એટલે 0.836 kJ/km - 0.836 MJ/km નહીં. એક દશાંશ ખસે તો payback 900,000 km થી 900 km "
            "થઈ જાય.")],
     7),

    ("Sizing a rooftop array for a house",
     "ઘર માટે છત પરની array નું માપ",
     "A house in Surat needs 4 kWh a day. Choose a module of 2 m2 and 20 % cell efficiency, with a "
     "performance ratio of 0.8 and 5 peak sun hours a day. Find the peak power of one module, the "
     "energy it gives in a day, the number of modules, the roof area and the CO2 avoided per year at "
     "0.71 kg per kWh.",
     "સુરતમાં ઘરને દિવસના 4 kWh જોઈએ. 2 m2 અને 20 % cell efficiency વાળું module પસંદ કરો, performance "
     "ratio 0.8 અને દિવસના 5 peak sun hour. એક module ની peak power, દિવસમાં તે આપે તે ઊર્જા, module ની "
     "સંખ્યા, છતનું ક્ષેત્ર અને 0.71 kg પ્રતિ kWh આગળ વર્ષે ટળતું CO2 શોધો.",
     [h4("Step 1 - one module", "પગલું 1 - એક module"),
      math("P = 1000 x 2 x 0.20 = 400 W peak",
           "E_day = 0.4 x 5 x 0.8 = 1.6 kWh",
           "so one module is 40 % of the daily need"),
      h4("Step 2 - how many, and the area", "પગલું 2 - કેટલા, અને ક્ષેત્ર"),
      math("n = 4/1.6 = 2.5  ->  3 modules",
           "area = 3 x 2 = 6 m2, array 1.2 kW peak",
           "yearly output = 3 x 1.6 x 365 = 1752 kWh"),
      h4("Step 3 - the carbon", "પગલું 3 - કાર્બન"),
      math("CO2 avoided = 1752 x 0.71 = 1244 kg a year",
           "over 25 years with 0.5 % a year degradation: about 29 tonnes",
           "against 25 x 1.9 GJ of module and frame, about 1300 kg of CO2 to build it"),
      eq("400 W per module,  3 modules,  6 m2,  1244 kg of CO2 a year"),
      p("Three modules is the answer for the arithmetic and four is the answer for the weather: a wet "
        "monsoon week, a dusty panel and a 20 % margin all argue for one more. The size of the array is "
        "set by the worst week, and the cost of the array by the average one.",
        "ગણિતનો જવાબ ત્રણ module છે અને હવામાનનો જવાબ ચાર: ભીનું ચોમાસું, ધૂળવાળી પેનલ અને 20 % margin "
        "બધા એક વધુ માંગે. Array નું માપ સૌથી ખરાબ અઠવાડિયું નક્કી કરે, અને કિંમત સરેરાશ અઠવાડિયું."),
      check("use the peak sun hours of the site, not of a textbook: Surat gives about 5, Jaisalmer 6, "
            "Kolkata 4.2, and London 2.8 - the same panel is a different power plant in each.",
            "સાઇટના peak sun hour વાપરો, પુસ્તકના નહીં: સુરત લગભગ 5, જેસલમેર 6, કોલકાતા 4.2 અને લંડન "
            "2.8 આપે - એ જ પેનલ દરેક જગ્યાએ જુદો પાવર પ્લાન્ટ છે.")],
     6),

    ("An electric car against a petrol car, in grams of CO2",
     "ઇલેક્ટ્રિક કાર સામે પેટ્રોલ કાર, CO2 ગ્રામમાં",
     "An electric car uses 0.15 kWh per km and charges on the Indian grid at 0.71 kg CO2 per kWh. A "
     "petrol car in the same class uses 6 L per 100 km, and petrol releases 2.31 kg of CO2 per litre. "
     "Find the g/km of each, the annual difference at 15 000 km, and the g/km of the electric car "
     "charged from its own roof.",
     "ઇલેક્ટ્રિક કાર 0.15 kWh પ્રતિ km વાપરે છે અને ભારતીય grid પર 0.71 kg CO2 પ્રતિ kWh આગળ charge થાય. "
     "એ જ વર્ગની પેટ્રોલ કાર 6 L પ્રતિ 100 km વાપરે, અને પેટ્રોલ પ્રતિ લિટર 2.31 kg CO2 છોડે. દરેકના g/km, "
     "15,000 km પર વાર્ષિક ફરક, અને પોતાની છત પરથી charge થતી ઇલેક્ટ્રિક કારના g/km શોધો.",
     [h4("Step 1 - the electric car", "પગલું 1 - ઇલેક્ટ્રિક કાર"),
      math("CO2 = 0.15 x 0.71 = 0.1065 kg/km",
           "= 107 g/km on the Indian grid",
           "on solar from the roof: about 0.04 kg/kWh, so 6 g/km"),
      h4("Step 2 - the petrol car", "પગલું 2 - પેટ્રોલ કાર"),
      math("6 L/100 km = 0.06 L/km",
           "CO2 = 0.06 x 2.31 = 0.1386 kg/km",
           "= 139 g/km, and 30 % of it is the carbon the fuel carries"),
      h4("Step 3 - the year, and the honest note", "પગલું 3 - વર્ષ, અને પ્રામાણિક નોંધ"),
      math("electric: 107 x 15000 = 1605 kg     petrol: 139 x 15000 = 2085 kg",
           "difference = 480 kg a year, and 12 tonnes over 25 000 km a year for 10 years",
           "a 35 kWh pack takes about 5 tonnes of CO2 to make, so the pack is paid back in 10 years"),
      eq("107 g/km electric,  139 g/km petrol,  480 kg a year saved"),
      p("The electric car is cleaner on this grid and much cleaner on a solar roof, but the gap is not "
        "the factor of ten that the brochure implies: the pack carries 5 tonnes of CO2 before the first "
        "kilometre. On a coal-heavy grid the honest answer is 'about 25 % less', and on a rooftop it is "
        "'almost nothing'.",
        "આ grid પર ઇલેક્ટ્રિક કાર સ્વચ્છ છે અને સોલાર છત પર ઘણી વધુ સ્વચ્છ, પણ ફરક બ્રોશર કહે તેવો દસ ગણો "
        "નથી: પહેલા કિલોમીટર પહેલાં pack 5 ટન CO2 ઉપાડી લે છે. કોલસા-ભારે grid પર પ્રામાણિક જવાબ "
        "'લગભગ 25 % ઓછું' છે, અને છત પર 'લગભગ કંઈ નહીં'."),
      check("quote the grid factor you used, because it decides the answer: 0.71 kg/kWh in India, 0.4 in "
            "the UK, 0.05 in Norway. The same car is a different climate argument in each.",
            "વાપરેલો grid factor કહો, કારણ કે તે જવાબ નક્કી કરે: ભારતમાં 0.71 kg/kWh, UK માં 0.4, "
            "નોર્વેમાં 0.05. એ જ કાર દરેક જગ્યાએ જુદી climate દલીલ છે.")],
     6),

    ("The energy and mass of a battery pack",
     "Battery pack ની ઊર્જા અને દળ",
     "A pack is built from 192 cells of 3.7 V and 50 Ah, arranged 96 in series and 2 in parallel. Each "
     "cell is 0.9 kg and the finished pack is 236 kg. Find the pack voltage, capacity, energy, the "
     "specific energy of the cells and of the pack, and the range at 0.15 kWh per km.",
     "Pack 3.7 V અને 50 Ah ના 192 cell થી બને છે, 96 series અને 2 parallel માં. દરેક cell 0.9 કિલો અને "
     "તૈયાર pack 236 કિલો. Pack નો voltage, capacity, ઊર્જા, cell અને pack ની specific energy, અને "
     "0.15 kWh પ્રતિ km આગળ અંતર શોધો.",
     [h4("Step 1 - voltage and capacity", "પગલું 1 - voltage અને capacity"),
      math("V = 96 x 3.7 = 355 V",
           "Ah = 2 x 50 = 100 Ah",
           "number of cells = 96 x 2 = 192"),
      h4("Step 2 - the energy", "પગલું 2 - ઊર્જા"),
      math("E = 355 x 100 = 35 500 Wh = 35.5 kWh",
           "cells: 192 x 0.9 = 172.8 kg, so 35 500/172.8 = 205 Wh per kg of cell",
           "pack: 35 500/236 = 150 Wh per kg, so 73 % of the pack is cells"),
      h4("Step 3 - the range", "પગલું 3 - અંતર"),
      math("range = 35.5/0.15 = 237 km",
           "of the 0.15 kWh/km, the pack's own 236 kg costs about 0.001 kWh/km per kg x 2.36... = 0.05",
           "so a 10 % lighter pack would add 10 km, which is why cell chemistry matters"),
      eq("355 V,  100 Ah,  35.5 kWh,  205 Wh/kg cell,  150 Wh/kg pack,  237 km"),
      p("The gap between 205 and 150 is the casing, the cooling plate, the busbars and the BMS - 63 kg "
        "of material that stores nothing. That is where a pack designer earns a living: not in the cell, "
        "which is bought, but in the 27 % of the mass that carries it.",
        "205 અને 150 વચ્ચેનો ફરક casing, cooling plate, busbar અને BMS છે - 63 કિલો એવી સામગ્રી જે કંઈ "
        "સંગ્રહતી નથી. ત્યાં જ pack designerની કમાણી છે: cell માં નહીં, જે ખરીદાય છે, પણ એને ઉપાડતા દળના "
        "27 % માં."),
      check("keep Wh and Ah apart: a 355 V pack at 100 Ah is 35.5 kWh, and quoting 100 Ah alone says "
            "nothing about the energy. The unit that a customer buys is kWh, and the unit that a welder "
            "sizes a cable for is A.",
            "Wh અને Ah અલગ રાખો: 355 V નું 100 Ah pack 35.5 kWh છે, અને ફક્ત 100 Ah કહેવાથી ઊર્જા વિશે કંઈ "
            "ન કહેવાય. ગ્રાહક kWh ખરીદે, અને welder કેબલ માપે A પર.")],
     5),

    ("Embodied energy and carbon of one aluminium part",
     "એક aluminium ભાગની embodied energy અને કાર્બન",
     "A bracket is 20 kg of aluminium. Primary aluminium is 170 MJ/kg and 11.5 kg CO2 per kg; secondary "
     "is 8 MJ/kg and 0.5 kg CO2 per kg; 4 kg of bauxite are mined per kg of primary metal. Find the "
     "embodied energy, the CO2 and the bauxite for both routes, and the saving.",
     "એક bracket 20 કિલો aluminium નું છે. Primary aluminium 170 MJ/kg અને પ્રતિ કિલો 11.5 kg CO2; "
     "secondary 8 MJ/kg અને 0.5 kg CO2; પ્રતિ કિલો primary ધાતુ માટે 4 કિલો bauxite ખોદાય. બંને માર્ગની "
     "embodied energy, CO2 અને bauxite, અને બચત શોધો.",
     [h4("Step 1 - the primary route", "પગલું 1 - primary માર્ગ"),
      math("EE = 20 x 170 = 3400 MJ = 0.94 MWh",
           "CO2 = 20 x 11.5 = 230 kg",
           "bauxite = 20 x 4 = 80 kg of ore, and 8 kg of alumina"),
      h4("Step 2 - the secondary route", "પગલું 2 - secondary માર્ગ"),
      math("EE = 20 x 8 = 160 MJ",
           "CO2 = 20 x 0.5 = 10 kg",
           "no bauxite, no alumina, no red mud"),
      h4("Step 3 - the saving", "પગલું 3 - બચત"),
      math("energy saved = 3400 - 160 = 3240 MJ = 0.9 MWh, 95 %",
           "CO2 saved = 230 - 10 = 220 kg on one bracket",
           "a fleet of 10 000 brackets: 2200 tonnes of CO2, 8 000 tonnes of ore"),
      eq("3400 MJ and 230 kg CO2 new,  160 MJ and 10 kg from scrap,  95 % saved"),
      p("This is the arithmetic behind the recycled-content target in every automotive contract: the "
        "metal does not change, only the route it took to the press shop. A part with 60 % recycled "
        "content is 86 % of the way to the secondary figure, which is why the percentage is written on "
        "the drawing.",
        "દરેક ઓટોમોબાઇલ કરારમાં recycled-content લક્ષ્ય પાછળ આ ગણિત છે: ધાતુ બદલાતી નથી, ફક્ત press shop "
        "સુધીનો તેનો રસ્તો બદલાય. 60 % recycled content વાળો ભાગ secondary આંકડાના 86 % સુધી પહોંચે, તેથી જ "
        "ટકાવારી ડ્રોઇંગ પર લખાય."),
      check("do not add the transport to the bauxite figure and leave out the alumina: a full account is "
            "ore, alumina, smelt, cast, roll, truck. The 170 MJ/kg already contains all of them, which is "
            "why it is used as a single number.",
            "bauxite ના આંકડામાં વહન ઉમેરીને alumina ભૂલશો નહીં: પૂરો હિસાબ ore, alumina, smelt, cast, roll, "
            "ટ્રક છે. 170 MJ/kg એ બધું સમાવે છે, તેથી જ તે એક આંકડા તરીકે વપરાય.")],
     5),

    ("Scrap recovery in a press shop",
     "પ્રેસ શોપમાં ભંગાર વસૂલાત",
     "A press shop runs 2000 hours a year at 500 kg of steel parts an hour. Scrap is 18 % of the sheet "
     "consumed, 92 % of the scrap is recovered as a clean grade, and the grade sells at Rs 32 a "
     "kilogram. Find the annual scrap, the mass recovered, its value, and what the recovery does to "
     "the material cost of a 2.5 kg part that sells for Rs 180.",
     "પ્રેસ શોપ વર્ષે 2000 કલાક ચાલે, કલાકે 500 કિલો સ્ટીલ ભાગ. વપરાયેલી શીટના 18 % ભંગાર થાય, તેમાંથી "
     "92 % સાફ grade તરીકે વસૂલાય, અને grade કિલોએ રૂ 32 વેચાય. વાર્ષિક ભંગાર, વસૂલાયેલું દળ, તેની કિંમત, "
     "અને રૂ 180 માં વેચાતા 2.5 કિલોના ભાગની સામગ્રી કિંમત પર recovery ની અસર શોધો.",
     [h4("Step 1 - the output and the scrap", "પગલું 1 - ઉત્પાદન અને ભંગાર"),
      math("output = 500 x 2000 = 1 000 000 kg = 1000 t of parts",
           "sheet consumed = 1000/0.82 = 1220 t",
           "scrap = 1220 - 1000 = 220 t, which is 18 % of the sheet"),
      h4("Step 2 - recovered and its value", "પગલું 2 - વસૂલાત અને કિંમત"),
      math("recovered = 220 x 0.92 = 202.4 t",
           "value = 202 400 x 32 = Rs 64.8 lakh a year",
           "unrecovered = 17.6 t, which is Rs 5.6 lakh lost as mixed swarf"),
      h4("Step 3 - what it means per part", "પગલું 3 - પ્રતિ ભાગ શું અર્થ"),
      math("sheet per part = 2.5/0.82 = 3.05 kg at Rs 55/kg = Rs 168",
           "scrap credit = (3.05 - 2.5) x 32 x 0.92 = Rs 16.2 per part",
           "material cost = 168 - 16 = Rs 152, so the scrap account is 9 % of the price"),
      eq("220 t of scrap,  202 t recovered,  Rs 64.8 lakh a year,  Rs 16 per part"),
      p("The segregation is the whole trick: 220 tonnes sold as a clean grade is Rs 64.8 lakh, the same "
        "220 tonnes sold as mixed swarf is about half of that and a reprocessing problem for somebody "
        "else. On a shop floor, a labelled bin is a green measure that pays for itself in a month.",
        "અલગ કરવું એ જ આખી યુક્તિ છે: 220 ટન સાફ grade તરીકે રૂ 64.8 લાખ, એ જ 220 ટન mixed swarf તરીકે "
        "લગભગ અડધું અને બીજા કોઈની reprocessing સમસ્યા. કારખાનામાં લેબલવાળી ડબ્બી એ green પગલું છે જે "
        "એક મહિનામાં પોતાનો ખર્ચ કાઢી લે."),
      check("count the sheet consumed, not the parts sold: 18 % scrap means 1000 t of parts needs 1220 t "
            "of sheet, and using 1000 t in the sum understates both the scrap and the credit.",
            "વેચાયેલા ભાગ નહીં, વપરાયેલી શીટ ગણો: 18 % ભંગાર એટલે 1000 ટન ભાગ માટે 1220 ટન શીટ, અને "
            "ગણતરીમાં 1000 ટન વાપરવાથી ભંગાર અને credit બંને ઓછા આવે.")],
     5),
]

PRACTICE = [(tr(h_en, h_gu), tr(q_en, q_gu), body(*parts_), m)
            for (h_en, h_gu, q_en, q_gu, parts_, m) in _PRACTICE]

EXAM = [{"q": q, "marks": m} for _, q, _, m in PRACTICE]
PRACTICE_ANSWERS = [a for _, _, a, _ in PRACTICE]

SOURCES = [
    ("GTU DI01000181 Engineering Materials Science syllabus (uploaded PDF, w.e.f. 2024-25)",
     "https://syllabus.gtu.ac.in/"),
    ("M. F. Ashby - Materials and the Environment: eco-informed material choice, Butterworth-Heinemann "
     "(embodied energy, eco-audit, energy payback)",
     "https://www.elsevier.com/books/materials-and-the-environment/ashby/978-0-12-385971-6"),
    ("V. Raghavan - Materials Science and Engineering, Prentice Hall India (energy materials, "
     "semiconductors for photovoltaics)", "https://www.pearson.com/"),
    ("O. P. Khanna - Material Science and Metallurgy, Dhanpat Rai (advanced materials, composite "
     "materials)", "https://www.dhanpatrai.com/"),
    ("Central Electricity Authority - CO2 Baseline Database for the Indian Power Sector (grid emission "
     "factor)", "https://cea.nic.in/"),
    ("IEA - Global EV Outlook (battery chemistry, pack specific energy, recycling)",
     "https://www.iea.org/reports/global-ev-outlook-2024"),
    ("MNRE - solar photovoltaic grid connected systems, module and balance of system specifications",
     "https://mnre.gov.in/"),
]
