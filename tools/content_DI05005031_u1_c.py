"""DI05005031 Unit 1, part C: sections 1.6 and 1.7, the formula list, the viva and the numericals."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from subject_DI05005031 import tr  # noqa: E402
from content_DI05005031_lib import (p, h4, ul, table, math, eq, why, check, pit, derive, body,
                                    card)  # noqa: E402

NOTES_C = []

# ---------------------------------------------------------------- 1.6 rate bases
NOTES_C.append({
    "title": tr("1.6 The rate of reaction on four different bases",
                "1.6 ચાર જુદા આધાર પર reaction rate"),
    "items": [
        card(
            "One rate, four denominators: volume, mass, area, mass of solid",
            "એક rate, ચાર denominator: volume, mass, area, mass of solid",
            h4("Definition, derived from the moles balance", "વ્યાખ્યા, moles balance પરથી"),
            p("Take a vessel and count the moles of A inside it at time t. In a small interval dt the "
              "count falls by dnA. The rate of disappearance of A per unit volume is that fall divided "
              "by dt and by the volume:",
              "vessel લો અને t સમયે તેમાં A ના moles ગણો. નાના interval dt માં ગણતરી dnA જેટલી "
              "ઘટે. A ના disappearance નો rate પ્રતિ unit volume એ ઘટાડો dt અને volume વડે ભાગ્યા "
              "પછી મળે:"),
            derive("-rA = -(1/V) dnA/dt                [mol m-3 s-1]",
                   "constant volume: nA = CA V with V constant",
                   "so  -rA = -dCA/dt",
                   "if the volume changes with conversion, keep 1/V:",
                   "-rA = -(1/V) dnA/dt   (never -dCA/dt)"),
            p("The negative sign makes the rate positive, because A is disappearing. The four bases "
              "below are the same ledger divided by four different quantities, chosen by what the "
              "reaction is happening <b>on</b>.",
              "A વપરાતું હોવાથી negative sign rate ને ધન બનાવે છે. નીચેના ચાર આધાર એ જ હિસાબને ચાર "
              "જુદા જથ્થા વડે ભાગ્યા પછી મળે છે, અને પ્રક્રિયા <b>શેના પર</b> થાય છે તેના આધારે "
              "પસંદ થાય છે."),
            table(
                [tr("Basis", "આધાર"), tr("Symbol", "Symbol"), tr("Unit", "એકમ"),
                 tr("Used for", "ક્યાં વપરાય")],
                [[tr("volume of reacting fluid", "reacting fluid નું volume"), "-rA", "mol m-3 s-1",
                  tr("homogeneous liquid or gas", "homogeneous liquid કે gas")],
                 [tr("mass of catalyst", "catalyst નું mass"), "-rA'", "mol kg-1 s-1",
                  tr("fixed and fluidized beds", "fixed અને fluidized beds")],
                 [tr("area of catalyst or interface", "catalyst કે interface નું area"), "-rA''",
                  "mol m-2 s-1",
                  tr("gas-liquid and gas-solid contact", "gas-liquid અને gas-solid સંપર્ક")],
                 [tr("mass of solid reactant", "solid reactant નું mass"), "-rA'''",
                  "mol kg-1 s-1", tr("roasting, leaching, burning", "roasting, leaching, burning")]]),
            h4("How the unit of k follows the order", "Order સાથે k નું એકમ કેવી રીતે આવે"),
            p("Put the power law -rA = k CA^n into the unit balance and k must carry whatever is left "
              "over. That is where the familiar table comes from:",
              "Power law -rA = k CA^n ને એકમના સંતુલનમાં મૂકો, તો k માં જે વધે તે ભરવું પડે. ત્યાંથી "
              "જ પરિચિત કોષ્ટક આવે છે:"),
            math("n = 0: mol m-3 s-1 = k            -> k: mol m-3 s-1",
                 "n = 1: mol m-3 s-1 = k (mol m-3)  -> k: s-1",
                 "n = 2: mol m-3 s-1 = k (mol m-3)^2-> k: m3 mol-1 s-1",
                 "n = 3:                                k: m6 mol-2 s-1",
                 "general: k: (mol m-3)^(1-n) s-1"),
            p("On a catalyst basis the moles per second are divided by kg of catalyst instead of m3 "
              "of fluid, so a first order constant becomes m3 kg-1 s-1:",
              "Catalyst ના આધાર પર પ્રતિ second ના moles fluid ના m3 ને બદલે catalyst ના kg વડે "
              "ભાગાય છે, તેથી first order constant m3 kg-1 s-1 થાય:"),
            math("-rA' = k' CA          k': m3 kg-1 s-1",
                 "-rA = (Wc / V) -rA'   to convert a bed to a volume"),
            check("A rate of 2.0e-3 mol m-3 s-1 in a bed of 1.8 m3 holding 300 kg of catalyst is "
                  "-rA' = 2.0e-3 x 1.8 / 300 = 1.2e-5 mol kg-1 s-1. The two numbers describe one "
                  "reaction; only the denominator differs.",
                  "1.8 m3 ના bed માં 300 kg catalyst સાથે 2.0e-3 mol m-3 s-1 નો rate એટલે "
                  "-rA' = 2.0e-3 x 1.8 / 300 = 1.2e-5 mol kg-1 s-1. બંને આંકડા એક જ પ્રક્રિયા કહે "
                  "છે; ફક્ત denominator જુદો છે."),
            pit("Writing -rA = -dCA/dt for a gas reaction in a PFR, where the volume grows with "
                "conversion. The correct form keeps 1/V inside, and dropping it overstates the rate "
                "by up to 50 % at high conversion.",
                "PFR માં gas પ્રક્રિયા માટે -rA = -dCA/dt લખવું, જ્યાં volume conversion સાથે વધે "
                "છે. સાચા સ્વરૂપમાં 1/V અંદર રહે છે, અને તે છોડી દેવાથી ઊંચા conversion પર rate "
                "50 % સુધી વધારે દેખાય છે."),
            diagram="u1_basis",
            syllabus_item="1.4",
        ),
    ],
})

# ---------------------------------------------------------------- 1.7 variables
NOTES_C.append({
    "title": tr("1.7 What changes the rate of a reaction",
                "1.7 પ્રક્રિયાનો rate શું બદલે છે"),
    "items": [
        card(
            "Concentration, temperature, and the five things fixed at construction",
            "Concentration, temperature અને બાંધકામ વખતે નક્કી થતી પાંચ બાબતો",
            h4("Concentration, and with it pressure", "Concentration, અને તેની સાથે pressure"),
            p("More molecules in the same volume means more collisions per second, so the rate rises "
              "with each concentration raised to its order. For gases the same effect is reached "
              "through pressure, because p = C R T: doubling the pressure doubles every partial "
              "pressure and multiplies the rate of a second order reaction by four.",
              "એ જ volume માં વધુ molecules એટલે પ્રતિ second વધુ અથડામણો, તેથી દરેક concentration "
              "તેના order ના ઘાત સુધી rate વધારે છે. Gases માટે એ જ અસર pressure થી મળે, કારણ કે "
              "p = C R T: pressure બમણું કરો તો દરેક partial pressure બમણું થાય અને second order "
              "પ્રક્રિયાનો rate ચાર ગણો થાય."),
            h4("Temperature - derived from the Arrhenius law",
               "Temperature - Arrhenius law પરથી"),
            p("The rate constant is not constant: it rises steeply with temperature because only the "
              "molecules carrying enough energy can react.",
              "Rate constant અચળ નથી: temperature સાથે તે ઝડપથી વધે છે, કારણ કે ફક્ત પૂરતી energy "
              "ધરાવતા molecules જ પ્રક્રિયા કરી શકે."),
            math("k = A exp(-Ea / R T)",
                 "ln k = ln A - (Ea/R)(1/T)",
                 "ln(k2/k1) = (Ea/R)(1/T1 - 1/T2)"),
            p("The last line is the working form: two rate constants at two temperatures give the "
              "activation energy, and the same line predicts a third temperature. For Ea about "
              "50 kJ/mol near room temperature the rate roughly doubles every 10 K - the '10 degree "
              "rule' of the older textbooks.",
              "છેલ્લી લાઇન કામનું સ્વરૂપ છે: બે temperature ના બે rate constants activation energy "
              "આપે છે, અને એ જ લાઇન ત્રીજા temperature ની આગાહી કરે છે. Room temperature નજીક "
              "50 kJ/mol જેટલી Ea માટે દર 10 K દીઠ rate લગભગ બમણો થાય - જૂની પુસ્તકોનો '10 degree "
              "rule'."),
            h4("Catalyst, area, solvent and light", "Catalyst, area, solvent અને light"),
            ul(("<b>Catalyst</b> supplies a path with lower Ea. It multiplies k, never K_eq, and it "
                "is the only variable that can be changed without changing the temperature.",
                "<b>Catalyst</b> ઓછી Ea વાળો માર્ગ આપે છે. તે k ને ગુણે છે, K_eq ને નહીં, અને "
                "temperature બદલ્યા વિના બદલી શકાય તેવો એકમાત્ર ચલ છે."),
               ("<b>Surface area</b> decides the rate of a heterogeneous reaction: a lump of "
                "limestone reacts on its skin, a powder reacts all through the bed. Grinding and "
                "packing are design decisions, not details.",
                "<b>Surface area</b> heterogeneous પ્રક્રિયાનો rate નક્કી કરે: ચૂનાનો ગઠ્ઠો તેની "
                "સપાટી પર પ્રક્રિયા કરે, પાવડર આખા bed માં કરે. દળવું અને packing design ના નિર્ણય "
                "છે, નાની વિગત નહીં."),
               ("<b>Solvent</b> changes the ionic strength and the polarity around the reacting "
                "molecules, so a constant measured in water is not the constant for the plant "
                "solvent.",
                "<b>Solvent</b> ionic strength અને reacting molecules આસપાસની polarity બદલે છે, "
                "તેથી પાણીમાં માપેલો constant plant ના solvent માટેનો નથી હોતો."),
               ("<b>Light</b> starts photochemical reactions: the photon breaks a bond, so the rate "
                "depends on how much light is absorbed rather than on temperature.",
                "<b>Light</b> photochemical પ્રક્રિયાઓ શરૂ કરે છે: photon bond તોડે છે, તેથી rate "
                "temperature પર નહીં, કેટલું light શોષાય તેના પર રહે છે.")),
            why("Every variable acts through the same equation, -rA = k(T) f(C): the f(C) part is "
                "chemistry you read from the order, and the k(T) part is exponential - which is why "
                "10 K matters more than a 10 % change in concentration.",
                "દરેક ચલ એક જ સમીકરણ દ્વારા કામ કરે છે, -rA = k(T) f(C): f(C) ભાગ order પરથી "
                "વંચાય તેવી chemistry છે, અને k(T) ભાગ exponential છે - તેથી 10 K નો ફેરફાર "
                "concentration માં 10 % ફેરફાર કરતાં વધુ અસર કરે છે."),
            pit("Cooling a reaction to 'slow it down' after a runaway has started. The rate falls, "
                "but the heat already generated is still in the vessel; control must be designed "
                "from the energy balance, and the coolant must be able to take the full dT_ad.",
                "Runaway શરૂ થયા પછી 'ધીમું કરવા' પ્રક્રિયા ઠંડી કરવી. Rate ઘટે છે, પણ પેદા થઈ ગયેલી "
                "heat vessel માં જ હોય છે; control energy balance પરથી design કરવો પડે અને coolant "
                "આખું dT_ad લઈ શકે તેવું હોવું જોઈએ."),
            diagram="u1_variables",
            syllabus_item="1.4",
        ),
    ],
})

# ---------------------------------------------------------------- equations
EQUATIONS = [
    {"title": tr("Rate of reaction", "પ્રક્રિયાનો rate"),
     "items": [
         {"name": tr("Rate of disappearance of A", "A ના disappearance નો rate"),
          "f": "-rA = -(1/V) dnA/dt",
          "terms": tr("Moles per second per unit volume of reacting fluid, mol m-3 s-1; the negative "
                      "sign makes it positive because A disappears.",
                      "Reacting fluid ના unit volume દીઠ પ્રતિ second moles, mol m-3 s-1; A વપરાતું "
                      "હોવાથી negative sign તેને ધન બનાવે છે.")},
         {"name": tr("Constant volume form", "Constant volume સ્વરૂપ"),
          "f": "-rA = -dCA/dt",
          "terms": tr("Valid only when the volume does not change with conversion - a liquid phase "
                      "batch, or a gas at constant density.",
                      "ફક્ત ત્યારે જ્યારે volume conversion સાથે ન બદલાય - liquid phase batch, "
                      "અથવા constant density નો gas.")},
         {"name": tr("Catalyst and area bases", "Catalyst અને area ના આધાર"),
          "f": "-rA' = -(1/Wc) dnA/dt,  -rA'' = -(1/S) dnA/dt",
          "terms": tr("mol kg-1 s-1 and mol m-2 s-1; used for fixed beds and for gas-liquid contact.",
                      "mol kg-1 s-1 અને mol m-2 s-1; fixed beds અને gas-liquid સંપર્ક માટે.")},
         {"name": tr("Moles left after conversion X", "Conversion X પછી બાકી moles"),
          "f": "nA = nA0 (1 - X)",
          "terms": tr("Conversion is the fraction of the feed A that has reacted.",
                      "Conversion એ feed ના A માંથી પ્રક્રિયા પામેલો ભાગ છે.")},
     ]},
    {"title": tr("Order and the rate constant", "Order અને rate constant"),
     "items": [
         {"name": tr("Power law", "Power law"),
          "f": "-rA = k CA^n",
          "terms": tr("n is the order with respect to A; the overall order is the sum of the "
                      "exponents.",
                      "n એ A પ્રતિ order છે; કુલ order ઘાતોનો સરવાળો છે.")},
         {"name": tr("Unit of k", "k નું એકમ"),
          "f": "k: (mol m-3)^(1-n) s-1",
          "terms": tr("s-1 for first order, m3 mol-1 s-1 for second order, mol m-3 s-1 for zero "
                      "order.", "first order માટે s-1, second order માટે m3 mol-1 s-1, zero order "
                      "માટે mol m-3 s-1.")},
         {"name": tr("Elementary reaction", "Elementary પ્રક્રિયા"),
          "f": "order = molecularity",
          "terms": tr("True only for a single-step reaction; every disagreement proves a multi-step "
                      "mechanism.", "ફક્ત એક-step પ્રક્રિયા માટે સાચું; દરેક અસંમતિ બહુ-step "
                      "mechanism સાબિત કરે છે.")},
     ]},
    {"title": tr("Temperature dependence", "Temperature અવલંબન"),
     "items": [
         {"name": tr("Arrhenius law", "Arrhenius law"),
          "f": "k = A exp(-Ea/RT)",
          "terms": tr("A is the frequency factor, Ea the activation energy in J/mol and "
                      "R = 8.314 J mol-1 K-1.",
                      "A frequency factor, Ea J/mol માં activation energy અને R = 8.314 J mol-1 "
                      "K-1.")},
         {"name": tr("Two-temperature form", "બે-temperature સ્વરૂપ"),
          "f": "ln(k2/k1) = (Ea/R)(1/T1 - 1/T2)",
          "terms": tr("The working form for the laboratory; two k values at two temperatures give "
                      "Ea.", "Laboratory માટે કામનું સ્વરૂપ; બે temperature ના બે k Ea આપે છે.")},
         {"name": tr("Ten degree rule", "દસ ડિગ્રીનો નિયમ"),
          "f": "k(T+10)/k(T) ~ 2 to 3",
          "terms": tr("A rough rule for Ea about 50 to 80 kJ/mol near room temperature - never a "
                      "substitute for the two-temperature calculation.",
                      "Room temperature નજીક 50 થી 80 kJ/mol ની Ea માટે અંદાજી નિયમ - બે-temperature "
                      "ગણતરીનો વિકલ્પ કદી નહીં.")},
     ]},
    {"title": tr("Enzyme kinetics", "Enzyme kinetics"),
     "items": [
         {"name": tr("Michaelis-Menten", "Michaelis-Menten"),
          "f": "v = Vmax [S] / (Km + [S])",
          "terms": tr("The saturating rate law of an enzyme-catalysed reaction.",
                      "Enzyme-catalysed પ્રક્રિયાનો saturating rate law.")},
         {"name": tr("The constants", "Constants"),
          "f": "Vmax = k2 [E0],  Km = (k-1 + k2)/k1",
          "terms": tr("Vmax depends on how much enzyme is charged; Km is the substrate "
                      "concentration at half of Vmax.",
                      "Vmax કેટલું enzyme ભરેલું છે તેના પર રહે; Km એ અડધા Vmax વાળું substrate "
                      "concentration છે.")},
         {"name": tr("Lineweaver-Burk", "Lineweaver-Burk"),
          "f": "1/v = (Km/Vmax)(1/[S]) + 1/Vmax",
          "terms": tr("A straight line with intercept 1/Vmax and slope Km/Vmax.",
                      "સીધી રેખા જેનો intercept 1/Vmax અને slope Km/Vmax છે.")},
     ]},
    {"title": tr("Heat effects", "Heat ની અસરો"),
     "items": [
         {"name": tr("Heat of reaction", "Heat of reaction"),
          "f": "dH_r negative = exothermic, positive = endothermic",
          "terms": tr("Per mole of the limiting reactant at the reaction temperature.",
                      "પ્રક્રિયાના temperature પર limiting reactant ના mole દીઠ.")},
         {"name": tr("Adiabatic temperature rise", "Adiabatic temperature વધારો"),
          "f": "dT_ad = (-dH_r) X / (sum Theta_i Cp_i)",
          "terms": tr("The rise the mixture would take if no heat were removed; it sizes the "
                      "cooling system.",
                      "heat ન કાઢો તો મિશ્રણ જેટલું ગરમ થાય; તેના પરથી cooling system નું size "
                      "નક્કી થાય.")},
         {"name": tr("Equilibrium", "Equilibrium"),
          "f": "K_eq = k1/k2 = products / reactants",
          "terms": tr("Sets the ceiling on conversion for a reversible reaction; a catalyst does not "
                      "move it.", "Reversible પ્રક્રિયાના conversion ની મર્યાદા નક્કી કરે; catalyst "
                      "તેને ખસેડતું નથી.")},
     ]},
]

# ---------------------------------------------------------------- viva
VIVA = [
    {"title": tr("Scope of the subject", "Subject નું ક્ષેત્ર"),
     "items": [
         {"q": tr("What does chemical reaction engineering add to chemical kinetics?",
                  "Chemical reaction engineering chemical kinetics માં શું ઉમેરે છે?"),
          "a": tr("Kinetics measures how fast a reaction goes in a small flask. CRE turns that rate "
                  "law into a vessel: it fixes the volume, the temperature, the heat duty, the "
                  "contact between phases and the way the feed enters and leaves.",
                  "Kinetics નાના flask માં પ્રક્રિયા કેટલી ઝડપી થાય તે માપે છે. CRE એ rate law ને "
                  "vessel માં ફેરવે છે: volume, temperature, heat duty, phases વચ્ચેનો સંપર્ક અને "
                  "feed ના પ્રવેશ-નિકાસની રીત નક્કી કરે છે.")},
         {"q": tr("Name the four questions a reactor design has to answer.",
                  "Reactor design એ કયા ચાર પ્રશ્નોના જવાબ આપવા પડે?"),
          "a": tr("How fast the reaction goes (kinetics), how far it can go (equilibrium), how much "
                  "heat is released or needed (energy balance), and what the vessel must look like "
                  "for the phases to meet (fluid mechanics and mass transfer).",
                  "પ્રક્રિયા કેટલી ઝડપી થાય (kinetics), કેટલી દૂર જાય (equilibrium), કેટલી heat "
                  "છૂટે કે જોઈએ (energy balance), અને phases મળે તે માટે vessel કેવું હોવું જોઈએ "
                  "(fluid mechanics અને mass transfer).")},
     ]},
    {"title": tr("Classification", "વર્ગીકરણ"),
     "items": [
         {"q": tr("Is a reaction between a dissolved salt and an acid homogeneous?",
                  "ઓગળેલું મીઠું અને acid વચ્ચેની પ્રક્રિયા homogeneous છે?"),
          "a": tr("Yes. Once the salt is dissolved there is only one liquid phase, so the reaction is "
                  "homogeneous even though the salt was weighed as a solid. Heterogeneous means the "
                  "reaction happens at a boundary between phases.",
                  "હા. મીઠું ઓગળી જાય પછી ફક્ત એક જ liquid phase હોય છે, તેથી પ્રક્રિયા "
                  "homogeneous છે ભલે મીઠું solid તરીકે તોળાયું હતું. Heterogeneous એટલે પ્રક્રિયા "
                  "phases વચ્ચેની સીમા પર થાય.")},
         {"q": tr("What is the difference between molecularity and order?",
                  "Molecularity અને order માં શું ફરક છે?"),
          "a": tr("Molecularity is the number of molecules in one elementary step, so it is a small "
                  "whole number taken from the mechanism. Order is the exponent in the rate law that "
                  "fits the experiment, so it can be zero, fractional or negative. They are equal "
                  "only for an elementary reaction.",
                  "Molecularity એ એક elementary step માંના molecules ની સંખ્યા છે, તેથી તે mechanism "
                  "પરથી મળતી નાની પૂર્ણ સંખ્યા છે. Order એ rate law માંનો ઘાત છે જે પ્રયોગ સાથે મેળ "
                  "ખાય, તેથી તે શૂન્ય, અપૂર્ણાંક કે ઋણાત્મક હોઈ શકે. બંને ફક્ત elementary પ્રક્રિયામાં "
                  "સરખા હોય.")},
         {"q": tr("Why is the hydrolysis of cane sugar called pseudo first order?",
                  "શેરા ખાંડનું hydrolysis pseudo first order કેમ કહેવાય?"),
          "a": tr("The true law is second order, first in sugar and first in water, but water is the "
                  "solvent and is present in such excess that its concentration hardly changes. The "
                  "measured law looks first order and the constant contains the water concentration.",
                  "સાચો law second order છે - sugar માં first અને water માં first - પણ water solvent "
                  "હોવાથી એટલા વધારામાં છે કે તેનું concentration લગભગ બદલાતું નથી. માપેલો law first "
                  "order દેખાય છે અને constant માં water નું concentration સમાયેલું હોય છે.")},
         {"q": tr("Does a catalyst change the equilibrium conversion?",
                  "Catalyst equilibrium conversion બદલે છે?"),
          "a": tr("No. It lowers the activation energy of the forward and the reverse reaction by the "
                  "same amount, so equilibrium arrives sooner but does not move. Only temperature, or "
                  "removing a product, changes it.",
                  "ના. તે forward અને reverse બંનેની activation energy સરખી માત્રામાં ઘટાડે છે, તેથી "
                  "equilibrium વહેલું આવે પણ ખસે નહીં. ફક્ત temperature કે product કાઢી લેવાથી તે "
                  "બદલાય છે.")},
     ]},
    {"title": tr("Rates and units", "Rates અને units"),
     "items": [
         {"q": tr("Why is the rate of a heterogeneous reaction written per unit area or per kg of "
                  "catalyst?", "Heterogeneous પ્રક્રિયાનો rate per unit area કે catalyst ના kg દીઠ "
                  "કેમ લખાય?"),
          "a": tr("Because the reaction can only happen where the phases meet. Doubling the volume "
                  "without adding surface changes nothing, while adding area or catalyst changes the "
                  "rate in proportion.",
                  "કારણ કે પ્રક્રિયા ફક્ત ત્યાં જ થઈ શકે જ્યાં phases મળે. Surface વધાર્યા વિના "
                  "volume બમણું કરવાથી કંઈ બદલાતું નથી, જ્યારે area કે catalyst ઉમેરવાથી rate "
                  "પ્રમાણમાં બદલાય છે.")},
         {"q": tr("What are the units of k for zero, first and second order?",
                  "Zero, first અને second order માટે k ના units કયા?"),
          "a": tr("Zero order: mol m-3 s-1. First order: s-1. Second order: m3 mol-1 s-1. In general "
                  "(mol m-3)^(1-n) s-1, straight from the unit balance of -rA = k CA^n.",
                  "Zero order: mol m-3 s-1. First order: s-1. Second order: m3 mol-1 s-1. સામાન્ય "
                  "રીતે (mol m-3)^(1-n) s-1, જે -rA = k CA^n ના unit સંતુલન પરથી સીધું આવે છે.")},
         {"q": tr("When may -rA be written as -dCA/dt?",
                  "ક્યારે -rA ને -dCA/dt લખી શકાય?"),
          "a": tr("Only when the volume of the reacting fluid does not change with conversion: a "
                  "liquid phase reaction, or a gas reaction with no change in the number of moles at "
                  "constant temperature and pressure. If the volume changes, 1/V stays inside the "
                  "derivative.",
                  "ફક્ત ત્યારે જ્યારે reacting fluid નું volume conversion સાથે ન બદલાય: liquid "
                  "phase પ્રક્રિયા, અથવા moles ની સંખ્યા ન બદલાતી gas પ્રક્રિયા અચળ temperature અને "
                  "pressure પર. Volume બદલાય તો 1/V derivative ની અંદર રહે.")},
     ]},
    {"title": tr("Heat and enzymes", "Heat અને enzymes"),
     "items": [
         {"q": tr("What is the adiabatic temperature rise, and why does it matter?",
                  "Adiabatic temperature rise શું છે અને તે કેમ મહત્વનું છે?"),
          "a": tr("It is the rise a mixture would take if none of the heat of reaction were removed: "
                  "dT_ad = (-dH_r) X / (sum Theta Cp). It tells the designer how strong the cooling "
                  "system must be and whether the reaction could run away.",
                  "reaction ની heat જરાય ન કાઢવામાં આવે તો મિશ્રણ જેટલું ગરમ થાય તે છે: "
                  "dT_ad = (-dH_r) X / (sum Theta Cp). તે કહે છે કે cooling system કેટલું મજબૂત "
                  "જોઈએ અને પ્રક્રિયા runaway થઈ શકે કે નહીં.")},
         {"q": tr("Why does an enzyme reaction become zero order at high substrate concentration?",
                  "ઊંચા substrate concentration પર enzyme પ્રક્રિયા zero order કેમ થાય?"),
          "a": tr("Because every active site is already occupied. More substrate cannot make more ES "
                  "complex, so the rate stops rising at Vmax and is limited by the amount of enzyme.",
                  "કારણ કે દરેક active site પહેલેથી ભરેલું છે. વધુ substrate થી વધુ ES complex બનતું "
                  "નથી, તેથી rate Vmax પર અટકે છે અને enzyme ના જથ્થા થી મર્યાદિત થાય છે.")},
         {"q": tr("How are Vmax and Km found from laboratory data?",
                  "Laboratory data પરથી Vmax અને Km કેવી રીતે શોધાય?"),
          "a": tr("Plot 1/v against 1/[S]. The intercept is 1/Vmax and the slope is Km/Vmax, so "
                  "Vmax = 1/intercept and Km = slope x Vmax. Reading the plateau and the half-rate "
                  "point is quicker but less accurate.",
                  "1/v ને 1/[S] સામે દોરો. Intercept 1/Vmax અને slope Km/Vmax, તેથી Vmax = 1/"
                  "intercept અને Km = slope x Vmax. Plateau અને અડધા-rate નું બિંદુ વાંચવું ઝડપી છે "
                  "પણ ઓછું ચોકસાઈવાળું.")},
     ]},
]

# ---------------------------------------------------------------- solved numericals
_PRACTICE = [
    ("Rate, rate constant and units",
     "Rate, rate constant અને units",
     "In a constant volume batch reactor the concentration of A falls from 2.0 to 1.2 mol/L in "
     "8 minutes. Find the average rate of disappearance of A in mol m-3 s-1 and in kmol m-3 h-1.",
     "Constant volume batch reactor માં A નું concentration 8 મિનિટમાં 2.0 થી 1.2 mol/L થાય છે. "
     "A ના disappearance નો સરેરાશ rate mol m-3 s-1 અને kmol m-3 h-1 માં શોધો.",
     [h4("Step 1 - the change", "પગલું 1 - ફેરફાર"),
      math("dCA = 1.2 - 2.0 = -0.8 mol/L",
           "dt  = 8 min = 480 s"),
      h4("Step 2 - the rate", "પગલું 2 - rate"),
      math("-rA = -dCA/dt = 0.8 / 480 = 1.667e-3 mol L-1 s-1"),
      p("1 L = 1e-3 m3, so per m3 the number is 1000 times larger:",
        "1 L = 1e-3 m3, તેથી per m3 આંકડો 1000 ગણો થાય:"),
      eq("-rA = 1.667 mol m-3 s-1"),
      h4("Step 3 - the same rate per hour", "પગલું 3 - એ જ rate કલાક દીઠ"),
      math("1.667 x 3600 = 6000 mol m-3 h-1 = 6.0 kmol m-3 h-1"),
      check("The mol/L s form is what a titration gives; the kmol m-3 h form is what a plant balance "
            "wants. Both describe the same reaction.",
            "mol/L s સ્વરૂપ titration આપે છે; kmol m-3 h સ્વરૂપ plant balance માં વપરાય છે. બંને એક "
            "જ પ્રક્રિયા કહે છે."),
      pit("Treating 0.8 mol/L as 0.8 mol/m3. It is 800 mol/m3.",
          "0.8 mol/L ને 0.8 mol/m3 ગણવું. તે 800 mol/m3 છે.")],
     6),
    ("Unit of the rate constant for any order",
     "કોઈ પણ order માટે rate constant નું એકમ",
     "A third order reaction has a rate of 4.0 x 10-3 mol m-3 s-1 at CA = 0.50 mol m-3. Find k with "
     "its unit, and state the unit k would have if the same reaction were second order.",
     "Third order પ્રક્રિયાનો rate CA = 0.50 mol m-3 પર 4.0 x 10-3 mol m-3 s-1 છે. k તેના એકમ સાથે "
     "શોધો, અને એ જ પ્રક્રિયા second order હોય તો k નું એકમ શું થાય તે જણાવો.",
     [h4("Step 1 - the law", "પગલું 1 - law"),
      math("-rA = k CA^3"),
      h4("Step 2 - solve for k", "પગલું 2 - k માટે ઉકેલો"),
      math("k = 4.0e-3 / (0.50)^3 = 4.0e-3 / 0.125 = 3.2e-2"),
      h4("Step 3 - the unit from the balance", "પગલું 3 - સંતુલન પરથી એકમ"),
      math("mol m-3 s-1 = [k] (mol m-3)^3",
           "[k] = (mol m-3)^(1-3) s-1 = m6 mol-2 s-1"),
      eq("k = 3.2 x 10-2 m6 mol-2 s-1"),
      p("For second order the same balance gives (mol m-3)^(1-2) s-1 = m3 mol-1 s-1.",
        "Second order માટે એ જ સંતુલન (mol m-3)^(1-2) s-1 = m3 mol-1 s-1 આપે છે."),
      check("3.2e-2 x 0.125 = 4.0e-3 mol m-3 s-1, the rate you started from.",
            "3.2e-2 x 0.125 = 4.0e-3 mol m-3 s-1, જે શરૂઆતનો rate છે.")],
     4),
    ("The same rate on a catalyst basis",
     "Catalyst ના આધાર પર એ જ rate",
     "A fixed bed of 1.8 m3 holds 300 kg of catalyst. The rate measured per unit volume of bed is "
     "2.5 x 10-3 mol m-3 s-1. Find the rate per kg of catalyst and the rate constant if the reaction "
     "is first order in A with CA = 0.8 mol m-3.",
     "1.8 m3 ના fixed bed માં 300 kg catalyst છે. Bed ના unit volume દીઠ rate 2.5 x 10-3 mol m-3 s-1 "
     "છે. પ્રતિ kg catalyst rate અને A માં first order તથા CA = 0.8 mol m-3 હોય તો rate constant "
     "શોધો.",
     [h4("Step 1 - convert the basis", "પગલું 1 - આધાર બદલો"),
      math("-rA V = -rA' Wc",
           "-rA' = 2.5e-3 x 1.8 / 300 = 1.5e-5 mol kg-1 s-1"),
      h4("Step 2 - the constant", "પગલું 2 - constant"),
      math("k' = -rA' / CA = 1.5e-5 / 0.8 = 1.875e-5"),
      eq("k' = 1.88 x 10-5 m3 kg-1 s-1"),
      p("The bed volume cancels; what matters is how much catalyst it holds, which is why a bed "
        "datasheet always states kg of catalyst per m3 of bed.",
        "Bed નું volume રદ થાય છે; મહત્વનું એ છે કે તેમાં કેટલું catalyst છે, તેથી bed ના datasheet "
        "માં હંમેશા kg catalyst per m3 bed લખાય છે."),
      check("1.875e-5 x 0.8 x 300 / 1.8 = 2.5e-3 mol m-3 s-1 - back to the measured rate.",
            "1.875e-5 x 0.8 x 300 / 1.8 = 2.5e-3 mol m-3 s-1 - માપેલા rate પર પાછા.")],
     5),
    ("Activation energy from two rate constants",
     "બે rate constants પરથી activation energy",
     "The rate constant is 2.4 x 10-4 s-1 at 300 K and 9.6 x 10-4 s-1 at 320 K. Find the activation "
     "energy and predict k at 340 K.",
     "Rate constant 300 K પર 2.4 x 10-4 s-1 અને 320 K પર 9.6 x 10-4 s-1 છે. Activation energy શોધો "
     "અને 340 K પર k ની આગાહી કરો.",
     [h4("Step 1 - the working form", "પગલું 1 - કામનું સ્વરૂપ"),
      math("ln(k2/k1) = (Ea/R)(1/T1 - 1/T2)"),
      h4("Step 2 - substitute", "પગલું 2 - મૂકો"),
      math("k2/k1 = 4.0,  ln 4.0 = 1.386",
           "1/300 - 1/320 = 2.083e-4 K-1",
           "Ea = 8.314 x 1.386 / 2.083e-4 = 5.53e4 J/mol"),
      eq("Ea = 55.3 kJ/mol"),
      h4("Step 3 - predict at 340 K", "પગલું 3 - 340 K પર આગાહી"),
      math("ln(k3/k2) = (55300/8.314)(1/320 - 1/340)",
           "           = 6652 x 1.838e-4 = 1.223",
           "k3 = 9.6e-4 x e^1.223 = 9.6e-4 x 3.40 = 3.26e-3 s-1"),
      check("k doubles from 300 to 320 K and again from 320 to 340 K, which is the 10 degree rule "
            "with a slightly steeper slope.",
            "300 થી 320 K માં k બમણો અને 320 થી 340 K માં ફરી બમણો, જે થોડો તીવ્ર ઢાળ વાળો 10 "
            "degree rule છે."),
      pit("Using degrees Celsius in the Arrhenius equation. R is per kelvin, so T must be in kelvin.",
          "Arrhenius equation માં Celsius મૂકવું. R પ્રતિ kelvin છે, તેથી T kelvin માં જ હોવું જોઈએ.")],
     7),
    ("Michaelis-Menten constants from two runs",
     "બે રન પરથી Michaelis-Menten constants",
     "An enzyme gives v = 0.60 mmol L-1 min-1 at [S] = 2.0 mmol/L and v = 0.90 at [S] = 6.0 mmol/L. "
     "Find Vmax and Km, and the rate at [S] = 20 mmol/L.",
     "Enzyme [S] = 2.0 mmol/L પર v = 0.60 mmol L-1 min-1 અને [S] = 6.0 mmol/L પર v = 0.90 આપે છે. "
     "Vmax અને Km તથા [S] = 20 mmol/L પર rate શોધો.",
     [h4("Step 1 - two equations", "પગલું 1 - બે સમીકરણો"),
      math("0.60 = Vmax (2) / (Km + 2)",
           "0.90 = Vmax (6) / (Km + 6)"),
      h4("Step 2 - divide them", "પગલું 2 - ભાગો"),
      math("1.5 = 6 (Km + 2) / [2 (Km + 6)]",
           "3 Km + 18 = 6 Km + 12   ->   Km = 2.0 mmol/L"),
      h4("Step 3 - Vmax", "પગલું 3 - Vmax"),
      math("0.60 = Vmax (2) / (2 + 2)  ->  Vmax = 1.2 mmol L-1 min-1"),
      eq("Km = 2.0 mmol/L,   Vmax = 1.2 mmol L-1 min-1"),
      h4("Step 4 - the rate at 20 mmol/L", "પગલું 4 - 20 mmol/L પર rate"),
      math("v = 1.2 x 20 / (2 + 20) = 1.09 mmol L-1 min-1"),
      p("That is 91 % of Vmax, so the enzyme is nearly saturated and more substrate buys almost "
        "nothing.", "તે Vmax ના 91 % છે, તેથી enzyme લગભગ saturated છે અને વધુ substrate થી લગભગ "
        "કંઈ મળતું નથી."),
      check("Vmax x 2/(2+2) = 1.2 x 0.5 = 0.60, the measured value.",
            "Vmax x 2/(2+2) = 1.2 x 0.5 = 0.60, માપેલું મૂલ્ય.")],
     6),
    ("Reading a rate law: order, molecularity and heat duty",
     "Rate law વાંચવું: order, molecularity અને heat duty",
     "For 2 NO + O2 -> 2 NO2 the measured law is -rNO = k CNO^2 CO2. State the order and the "
     "molecularity, and find the adiabatic temperature rise at 70 % conversion if dH_r = -114 kJ per "
     "mol NO, the feed holds 1.6 kmol/m3 of NO, the mean heat capacity is 2.1 kJ/(kg K) and the mean "
     "density is 1150 kg/m3.",
     "2 NO + O2 -> 2 NO2 માટે માપેલો law -rNO = k CNO^2 CO2 છે. Order અને molecularity જણાવો, અને "
     "dH_r = -114 kJ પ્રતિ mol NO, feed માં NO 1.6 kmol/m3, સરેરાશ heat capacity 2.1 kJ/(kg K) અને "
     "સરેરાશ density 1150 kg/m3 હોય તો 70 % conversion પર adiabatic temperature rise શોધો.",
     [h4("Step 1 - order", "પગલું 1 - order"),
      p("The exponents are 2 in NO and 1 in O2, so the reaction is third order overall, second order "
        "in NO and first order in O2.",
        "ઘાત NO માં 2 અને O2 માં 1 છે, તેથી પ્રક્રિયા કુલ third order, NO માં second order અને "
        "O2 માં first order છે."),
      h4("Step 2 - molecularity", "પગલું 2 - molecularity"),
      p("Three molecules stand on the left, so an elementary step would have molecularity 3 - and "
        "here the measured order agrees with it, which is consistent with a single step (but does "
        "not prove one).", "ડાબી બાજુ ત્રણ molecules છે, તેથી elementary step ની molecularity 3 થાય - "
        "અને અહીં માપેલો order તેની સાથે મેળ ખાય છે, જે એક step સાથે સુસંગત છે (પણ સાબિત કરતું નથી)."),
      h4("Step 3 - heat released per m3", "પગલું 3 - per m3 છૂટતી heat"),
      math("heat = (-dH_r) CA0 X = 114 000 x 1600 x 0.70",
           "     = 1.277e8 J per m3 of feed"),
      h4("Step 4 - temperature rise", "પગલું 4 - temperature વધારો"),
      math("capacity per m3 = 1150 x 2100 = 2.415e6 J m-3 K-1",
           "dT_ad = 1.277e8 / 2.415e6 = 52.9 K"),
      eq("dT_ad = 53 K"),
      p("A 53 K rise on a 320 K feed reaches 373 K, and because k is exponential in temperature that "
        "multiplies the rate several times - the reactor must be cooled, and the coolant must be "
        "sized for the full 53 K.",
        "320 K ના feed પર 53 K વધારો 373 K સુધી લઈ જાય, અને k, T માં exponential હોવાથી rate ઘણા "
        "ગણો થાય - reactor ઠંડું કરવું પડે અને coolant આખા 53 K માટે ગણવો પડે."),
      pit("Multiplying by X twice. The heat is (-dH_r) x moles reacted, and the moles reacted are "
          "already CA0 X, not CA0 X^2.",
          "X વડે બે વાર ગુણવું. Heat = (-dH_r) x reacted moles, અને reacted moles પહેલેથી CA0 X છે, "
          "CA0 X^2 નહીં.")],
     7),
]

PRACTICE = [(tr(h_en, h_gu), tr(q_en, q_gu), body(*parts), m)
            for (h_en, h_gu, q_en, q_gu, parts, m) in _PRACTICE]

EXAM = [{"q": q, "marks": m} for _, q, _, m in PRACTICE]
PRACTICE_ANSWERS = [a for _, _, a, _ in PRACTICE]

SOURCES = [
    ("GTU DI05005031 Chemical Reaction Engineering syllabus (uploaded PDF, w.e.f. 2026-27)",
     "https://syllabus.gtu.ac.in/"),
    ("Octave Levenspiel - Chemical Reaction Engineering, 3rd ed., John Wiley and Sons (chapters 1-2)",
     "https://www.wiley.com/"),
    ("H. Scott Fogler - Essentials of Chemical Reaction Engineering, 4th ed., Prentice Hall "
     "(chapter 1, mole balances and rate laws)", "https://www.pearson.com/"),
    ("NPTEL course on Chemical Reaction Engineering - https://nptel.ac.in/", "https://nptel.ac.in/"),
]
