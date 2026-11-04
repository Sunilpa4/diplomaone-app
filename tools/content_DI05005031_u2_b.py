"""DI05005031 Unit 2, part B: sections 2.4 - 2.5, formulas, viva and solved numericals."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from subject_DI05005031 import tr  # noqa: E402
from content_DI05005031_lib import (p, h4, ul, table, math, eq, why, check, pit, derive, body,
                                    card)  # noqa: E402

NOTES_B = []

NOTES_B.append({
    "title": tr("2.4 The temperature term: the Arrhenius law",
                "2.4 Temperature વાળો ભાગ: Arrhenius law"),
    "items": [
        card(
            "Where exp(-Ea/RT) comes from",
            "exp(-Ea/RT) ક્યાંથી આવે છે",
            h4("The observation first", "પહેલાં અવલોકન"),
            p("Svante Arrhenius noticed in 1889 that a plot of ln k against 1/T is a straight line "
              "with a negative slope for a very large number of reactions. A straight line in those "
              "coordinates has exactly one form:",
              "1889 માં Svante Arrhenius એ જોયું કે ઘણી બધી પ્રક્રિયાઓ માટે ln k અને 1/T નો ગ્રાફ "
              "ઋણાત્મક ઢાળ વાળી સીધી રેખા છે. તે coordinates માં સીધી રેખાનું ફક્ત એક જ સ્વરૂપ હોઈ "
              "શકે:"),
            derive("ln k = ln A - (Ea/R)(1/T)",
                   "take the exponential of both sides:",
                   "k = A exp(-Ea / R T)"),
            eq("k = A exp(-Ea/RT)"),
            p("A is the <b>frequency factor</b> (how often molecules meet with the right orientation) "
              "and Ea the <b>activation energy</b> (how much energy that meeting needs). A is nearly "
              "independent of temperature; the exponential is not.",
              "A <b>frequency factor</b> છે (molecules કેટલી વાર યોગ્ય દિશામાં મળે) અને Ea "
              "<b>activation energy</b> (તે મુલાકાતને કેટલી energy જોઈએ). A લગભગ temperature પર "
              "આધારિત નથી; exponential છે."),
            h4("Derivation from the van't Hoff relation",
               "van't Hoff સંબંધ પરથી derivation"),
            p("Treat the reaction as an equilibrium between reactants and an activated complex, apply "
              "the van't Hoff equation to that equilibrium, and identify the enthalpy of the complex "
              "with the activation energy:",
              "પ્રક્રિયાને reactants અને activated complex વચ્ચેના સંતુલન તરીકે લો, તે સંતુલન પર van't "
              "Hoff સમીકરણ લગાડો, અને complex ની enthalpy ને activation energy સાથે સરખાવો:"),
            derive("van't Hoff:  d ln K / dT = dH / (R T^2)",
                   "with K = k1/k-1 for the activated step:",
                   "d ln k / dT = Ea / (R T^2)",
                   "integrate with Ea constant:",
                   "ln k = const - Ea/(R T)",
                   "k = A exp(-Ea/RT)"),
            h4("Derivation from collision theory", "Collision theory પરથી derivation"),
            p("Molecules collide with a spread of energies. The fraction whose energy exceeds Ea "
              "follows the Boltzmann distribution, which gives an exponential tail:",
              "Molecules જુદી જુદી energy સાથે અથડાય છે. Ea થી વધુ energy ધરાવતા molecules નો ભાગ "
              "Boltzmann distribution પાળે છે, જે exponential પૂંછ આપે છે:"),
            math("fraction with E > Ea  ~  exp(-Ea / R T)",
                 "k = (collisions per s) x (fraction) x (steric factor)",
                 "  = A exp(-Ea/RT),  A = Z x p"),
            p("Both routes give the same law. The first explains <b>why the line is straight</b>; the "
              "second explains <b>what A and Ea physically are</b>.",
              "બંને માર્ગ એક જ law આપે છે. પહેલો સમજાવે કે <b>રેખા કેમ સીધી છે</b>; બીજો સમજાવે કે "
              "<b>A અને Ea ભૌતિક રીતે શું છે</b>."),
            why("The exponent is the whole story of temperature sensitivity: at 300 K an Ea of "
                "50 kJ/mol makes exp(-Ea/RT) = 2e-9, and a 10 K rise multiplies it by about 2.0 - "
                "which is the '10 degree rule' seen from the inside.",
                "આખી temperature સંવેદનશીલતા exponent માં છે: 300 K પર 50 kJ/mol ની Ea માટે "
                "exp(-Ea/RT) = 2e-9 થાય, અને 10 K વધારો તેને લગભગ 2.0 ગણો કરે - જે '10 degree rule' "
                "અંદરથી દેખાય છે."),
            check("k(T1)/k(T2) must be independent of A: 300 -> 310 K with Ea = 50 kJ/mol gives "
                  "exp[(50000/8.314)(1/300 - 1/310)] = exp(0.647) = 1.91.",
                  "k(T1)/k(T2) એ A પર આધારિત ન હોવું જોઈએ: Ea = 50 kJ/mol સાથે 300 થી 310 K માટે "
                  "exp[(50000/8.314)(1/300 - 1/310)] = exp(0.647) = 1.91."),
            pit("Using the two-temperature form with temperatures in Celsius, or with 1/T in "
                "minutes. Both T and the reciprocal must be in kelvin and K-1.",
                "બે-temperature સ્વરૂપમાં Celsius કે મિનિટમાં 1/T વાપરવું. T અને તેનો વ્યસ્ત બંને "
                "kelvin અને K-1 માં જ જોઈએ."),
            diagram="u2_arrhenius",
            syllabus_item="2.4",
        ),
    ],
})

NOTES_B.append({
    "title": tr("2.5 Activation energy", "2.5 Activation energy (સક્રિયણ ઊર્જા)"),
    "items": [
        card(
            "The barrier every reaction has to clear",
            "દરેક પ્રક્રિયાને પાર કરવો પડતો અવરોધ",
            h4("What Ea is", "Ea શું છે"),
            p("<b>Activation energy</b> is the extra energy a pair of molecules must have before the "
              "bonds can break and re-form. At any temperature most molecules have less, so only the "
              "high-energy tail reacts. Ea therefore controls <b>how fast the rate grows with "
              "temperature</b>: the larger Ea, the steeper the rise.",
              "<b>Activation energy</b> એ બોન્ડ તૂટીને ફરી બની શકે તે પહેલાં molecules ની જોડી પાસે "
              "હોવી જોઈએ તે વધારાની energy છે. કોઈ પણ temperature પર મોટા ભાગના molecules પાસે તે "
              "ઓછી હોય છે, તેથી ફક્ત ઊંચી energy વાળી પૂંછ પ્રક્રિયા કરે છે. તેથી Ea નક્કી કરે છે કે "
              "<b>rate temperature સાથે કેટલી ઝડપથી વધે</b>: Ea જેટલી મોટી, વધારો તેટલો તીવ્ર."),
            h4("Derivation: why a higher Ea means a more sensitive rate",
               "Derivation: ઊંચી Ea એ વધુ સંવેદનશીલ rate કેમ"),
            p("Differentiate the Arrhenius law with respect to temperature:",
              "Arrhenius law ને temperature પ્રતિ differentiate કરો:"),
            derive("ln k = ln A - Ea/(R T)",
                   "d ln k / dT = Ea / (R T^2)",
                   "d ln k = (Ea / R T^2) dT",
                   "for a small step dT:  dk/k = (Ea/(R T^2)) dT"),
            p("The fractional change in k per kelvin is Ea/(RT^2). At 300 K that is 0.00134 per kJ/mol: "
              "an Ea of 50 kJ/mol gives 6.7 % per kelvin, while a slow reaction with Ea of 10 kJ/mol "
              "gives only 1.3 % - which is why some reactions can be run in a simple kettle and "
              "others need a controller.",
              "પ્રતિ kelvin k માં થતો ભાગાકાર ફેરફાર Ea/(RT^2) છે. 300 K પર તે પ્રતિ kJ/mol 0.00134 "
              "છે: 50 kJ/mol ની Ea 6.7 % પ્રતિ kelvin આપે છે, જ્યારે 10 kJ/mol વાળી ધીમી પ્રક્રિયા "
              "ફક્ત 1.3 % - તેથી કેટલીક પ્રક્રિયા સાદા kettle માં ચાલે છે અને કેટલીકને controller "
              "જોઈએ."),
            h4("A catalyst lowers Ea, never dH", "Catalyst Ea ઘટાડે છે, dH નહીં"),
            p("A catalyst provides a different route to the same product. That route has a lower "
              "peak, so Ea falls and k rises at the same temperature. The starting and finishing "
              "levels are unchanged, so dH, K_eq and the equilibrium conversion are unchanged too.",
              "Catalyst એ જ product સુધીનો બીજો માર્ગ આપે છે. તે માર્ગનું શિખર નીચું હોવાથી Ea ઘટે "
              "અને એ જ temperature પર k વધે. શરૂઆત અને અંતની સપાટી ન બદલાય, તેથી dH, K_eq અને "
              "equilibrium conversion પણ ન બદલાય."),
            math("catalysed:  k' = A exp(-Ea'/RT)  with Ea' < Ea",
                 "ratio: k'/k = exp[(Ea - Ea')/RT]",
                 "20 kJ/mol lower Ea at 500 K: e^(20000/4157) = 123"),
            p("A 20 kJ/mol reduction is therefore worth a factor of about 120 at 500 K - the whole "
              "economic case for a catalyst in one line.",
              "તેથી 20 kJ/mol ઘટાડો 500 K પર લગભગ 120 ગણો ફાયદો આપે - catalyst નો આખો આર્થિક "
              "તર્ક એક લીટીમાં."),
            why("Ea is a property of the route, not of the reaction: the same overall reaction can "
                "have one Ea on a clean surface, another on a poisoned one, and a third in solution. "
                "That is why a catalyst's Ea is always quoted with its conditions.",
                "Ea પ્રક્રિયાની નહીં, માર્ગની લાક્ષણિકતા છે: એક જ પ્રક્રિયાની Ea સ્વચ્છ surface પર "
                "એક, poisoned surface પર બીજી અને દ્રાવણમાં ત્રીજી હોઈ શકે. તેથી catalyst ની Ea "
                "હંમેશા તેની શરતો સાથે લખાય છે."),
            pit("Believing a catalyst 'adds energy' to the reaction. It adds no energy at all - it "
                "finds a lower hill to climb.",
                "Catalyst પ્રક્રિયામાં 'energy ઉમેરે' છે તેવું માનવું. તે જરાય energy ઉમેરતું નથી - "
                "તે ચઢવા માટે નીચો ટેકરો શોધે છે."),
            diagram="u2_barrier",
            syllabus_item="2.5",
        ),
        card(
            "Measuring Ea: two temperatures or a straight line",
            "Ea માપવી: બે temperature કે સીધી રેખા",
            h4("Two points", "બે બિંદુ"),
            p("Two rate constants at two temperatures are enough for an examination answer: solve the "
              "two-temperature form for Ea.",
              "પરીક્ષાના જવાબ માટે બે temperature પરના બે rate constants પૂરતા છે: બે-temperature "
              "સ્વરૂપને Ea માટે ઉકેલો."),
            derive("ln(k2/k1) = (Ea/R)(1/T1 - 1/T2)",
                   "Ea = R ln(k2/k1) / (1/T1 - 1/T2)"),
            h4("A line through many points", "ઘણા બિંદુઓમાંથી રેખા"),
            p("Run the reaction at four or five temperatures, plot ln k against 1/T and take the slope. "
              "The slope is -Ea/R, so Ea = -R x slope, and the intercept is ln A, which gives the "
              "frequency factor as well.",
              "પ્રક્રિયા ચાર-પાંચ temperature પર ચલાવો, ln k ને 1/T સામે દોરો અને ઢાળ લો. ઢાળ "
              "-Ea/R છે, તેથી Ea = -R x ઢાળ, અને intercept ln A છે, જે frequency factor પણ આપે છે."),
            math("slope = -Ea/R      intercept = ln A",
                 "Ea = -R x slope     A = exp(intercept)"),
            p("The line is better than two points because it shows the scatter: a set of points that "
              "bends upwards means Ea is not constant, which usually means the mechanism changes with "
              "temperature, or that diffusion has started to control the rate.",
              "બે બિંદુ કરતાં રેખા સારી છે કારણ કે તે scatter દર્શાવે: ઉપર તરફ વળતા બિંદુઓ એટલે Ea "
              "અચળ નથી, જેનો અર્થ સામાન્ય રીતે mechanism temperature સાથે બદલાય છે અથવા diffusion એ "
              "rate નિયંત્રિત કરવા માંડ્યું છે."),
            why("The slope is read in the units the data demand: if 1/T is in K-1 and ln k is "
                "dimensionless, the slope is in kelvin and R x slope is J/mol. Almost every wrong "
                "answer in this topic is a unit slip of that kind.",
                "ઢાળ data ના એકમમાં જ વંચાય: 1/T K-1 માં અને ln k dimensionless હોય તો ઢાળ kelvin "
                "માં અને R x ઢાળ J/mol માં. આ topic ના લગભગ દરેક ખોટા જવાબનું કારણ આવી એકમની ભૂલ છે."),
            check("For 2.4e-4 s-1 at 300 K and 9.6e-4 s-1 at 320 K the slope is 1.386/2.083e-4 = "
                  "6652 K, so Ea = 8.314 x 6652 = 55.3 kJ/mol.",
                  "300 K પર 2.4e-4 s-1 અને 320 K પર 9.6e-4 s-1 માટે ઢાળ 1.386/2.083e-4 = 6652 K, "
                  "તેથી Ea = 8.314 x 6652 = 55.3 kJ/mol."),
            diagram="u2_ea",
            syllabus_item="2.5",
        ),
    ],
})

# ---------------------------------------------------------------- equations
EQUATIONS = [
    {"title": tr("Rate law", "Rate law"),
     "items": [
         {"name": tr("Two-term form", "બે ભાગનું સ્વરૂપ"),
          "f": "-rA = k(T) f(C)",
          "terms": tr("The concentration term carries the order, the temperature term carries the "
                      "energy.", "Concentration ભાગ order ઉપાડે, temperature ભાગ energy.")},
         {"name": tr("Power law", "Power law"),
          "f": "-rA = k CA^a CB^b ...",
          "terms": tr("a, b are the orders with respect to A and B; a + b is the overall order.",
                      "a, b એ A અને B પ્રતિ orders છે; a + b કુલ order છે.")},
         {"name": tr("Pseudo first order", "Pseudo first order"),
          "f": "k' = k CB   when CB >> CA",
          "terms": tr("The excess reactant is absorbed into the constant, so it changes if that "
                      "reactant changes.", "વધારાનો reactant constant માં સમાઈ જાય છે, તેથી તે "
                      "બદલાય તો constant પણ બદલાય.")},
     ]},
    {"title": tr("Units of the rate constant", "Rate constant ના units"),
     "items": [
         {"name": tr("General", "સામાન્ય"),
          "f": "k: (mol m-3)^(1-n) s-1",
          "terms": tr("Straight from the unit balance of -rA = k CA^n.",
                      "-rA = k CA^n ના unit સંતુલન પરથી સીધું.")},
         {"name": tr("Common orders", "સામાન્ય orders"),
          "f": "n=0: mol m-3 s-1;  n=1: s-1;  n=2: m3 mol-1 s-1",
          "terms": tr("The unit is the fastest check that a rate law is written correctly.",
                      "Rate law સાચો લખાયો છે તેની સૌથી ઝડપી ચકાસણી units છે.")},
     ]},
    {"title": tr("Arrhenius law", "Arrhenius law"),
     "items": [
         {"name": tr("Exponential form", "Exponential સ્વરૂપ"),
          "f": "k = A exp(-Ea/RT)",
          "terms": tr("A is the frequency factor and Ea the activation energy in J/mol.",
                      "A frequency factor અને Ea J/mol માં activation energy.")},
         {"name": tr("Logarithmic form", "Logarithmic સ્વરૂપ"),
          "f": "ln k = ln A - (Ea/R)(1/T)",
          "terms": tr("A straight line of slope -Ea/R against 1/T.",
                      "1/T સામે ઢાળ -Ea/R વાળી સીધી રેખા.")},
         {"name": tr("Two-temperature form", "બે-temperature સ્વરૂપ"),
          "f": "ln(k2/k1) = (Ea/R)(1/T1 - 1/T2)",
          "terms": tr("The working form: two k values give Ea, or Ea gives the third value of k.",
                      "કામનું સ્વરૂપ: બે k Ea આપે, અથવા Ea ત્રીજું k આપે.")},
         {"name": tr("Temperature sensitivity", "Temperature સંવેદનશીલતા"),
          "f": "d ln k/dT = Ea/(R T^2)",
          "terms": tr("The fractional change of k per kelvin; at 300 K it is 0.0134 per kJ/mol.",
                      "પ્રતિ kelvin k માં ભાગાકાર ફેરફાર; 300 K પર પ્રતિ kJ/mol 0.0134.")},
     ]},
    {"title": tr("Activation energy from data", "Data પરથી activation energy"),
     "items": [
         {"name": tr("From a plot", "ગ્રાફ પરથી"),
          "f": "Ea = -R x slope of ln k against 1/T",
          "terms": tr("Slope in kelvin, Ea in J/mol; the intercept gives A.",
                      "ઢાળ kelvin માં, Ea J/mol માં; intercept A આપે.")},
         {"name": tr("From two points", "બે બિંદુ પરથી"),
          "f": "Ea = R ln(k2/k1) / (1/T1 - 1/T2)",
          "terms": tr("Temperatures in kelvin, always.", "Temperatures હંમેશા kelvin માં.")},
         {"name": tr("Catalyst effect", "Catalyst ની અસર"),
          "f": "k'/k = exp[(Ea - Ea')/RT]",
          "terms": tr("A lower Ea multiplies k at the same temperature and leaves K_eq alone.",
                      "નીચી Ea એ જ temperature પર k ને ગુણે છે અને K_eq ને અડતી નથી.")},
     ]},
]

# ---------------------------------------------------------------- viva
VIVA = [
    {"title": tr("Rate laws", "Rate laws"),
     "items": [
         {"q": tr("Why is a rate law written as k(T) times f(C)?",
                  "Rate law k(T) ગુણ્યું f(C) કેમ લખાય?"),
          "a": tr("Because the two influences are almost independent: temperature changes the energy "
                  "of the molecules and composition changes how often they meet. Measuring f(C) at "
                  "one temperature then lets k be recomputed for any other temperature.",
                  "કારણ કે બંને અસરો લગભગ સ્વતંત્ર છે: temperature molecules ની energy બદલે અને રચના "
                  "તેઓ કેટલી વાર મળે તે બદલે. એક temperature પર f(C) માપી લીધા પછી કોઈ પણ બીજા "
                  "temperature માટે k ગણી શકાય.")},
         {"q": tr("What does the rate constant physically mean?",
                  "Rate constant ભૌતિક રીતે શું દર્શાવે?"),
          "a": tr("It is the rate when every concentration is one unit, so it is the rate at a "
                  "reference composition. It is constant only for a fixed temperature, solvent and "
                  "catalyst.",
                  "દરેક concentration એક એકમ હોય ત્યારનો rate, એટલે સંદર્ભ રચના પરનો rate. તે ફક્ત "
                  "નિશ્ચિત temperature, solvent અને catalyst માટે અચળ છે.")},
         {"q": tr("What is a pseudo first order reaction?", "Pseudo first order પ્રક્રિયા શું છે?"),
          "a": tr("One in which a reactant is present in such large excess that its concentration "
                  "hardly changes, so its concentration hides inside the measured constant and the "
                  "law looks first order.",
                  "એવી પ્રક્રિયા જેમાં એક reactant એટલા વધારામાં હોય કે તેનું concentration લગભગ ન "
                  "બદલાય, તેથી તેનું concentration માપેલા constant માં સમાઈ જાય અને law first order "
                  "દેખાય.")},
     ]},
    {"title": tr("Mechanism", "Mechanism"),
     "items": [
         {"q": tr("How do you recognise an elementary reaction?",
                  "Elementary પ્રક્રિયા કેવી રીતે ઓળખાય?"),
          "a": tr("Only by its behaviour: order equals molecularity, the law can be written from the "
                  "equation, and it holds over a wide range of concentrations. A change of order with "
                  "conditions proves the reaction is not elementary.",
                  "ફક્ત તેની વર્તણૂકથી: order અને molecularity સરખા, law સમીકરણ પરથી લખી શકાય અને "
                  "તે પ્રશસ્ત concentration શ્રેણીમાં ટકે. શરતો સાથે order બદલાય તો પ્રક્રિયા "
                  "elementary નથી.")},
         {"q": tr("Why can a non-elementary reaction have a fractional order?",
                  "Non-elementary પ્રક્રિયાનો order અપૂર્ણાંક કેમ હોઈ શકે?"),
          "a": tr("Because the rate depends on the concentration of an intermediate, and the balance "
                  "that fixes that intermediate usually contains a square root. That square root "
                  "reaches the rate law as a fractional exponent.",
                  "કારણ કે rate intermediate ના concentration પર રહે છે, અને તે intermediate નક્કી "
                  "કરતું સંતુલન સામાન્ય રીતે વર્ગમૂળ ધરાવે છે. તે વર્ગમૂળ rate law માં અપૂર્ણાંક "
                  "ઘાત તરીકે આવે.")},
         {"q": tr("What are the three kinds of step in a chain reaction?",
                  "Chain પ્રક્રિયામાં ત્રણ પ્રકારના steps કયા?"),
          "a": tr("Initiation, which creates the first radicals; propagation, which produces product "
                  "and regenerates a radical; and termination, which destroys radicals. The "
                  "propagation steps are fast and repeat many times.",
                  "Initiation - પહેલા radicals બનાવે; propagation - product આપે અને radical ફરી "
                  "બનાવે; અને termination - radicals નષ્ટ કરે. Propagation steps ઝડપી અને ઘણી વાર "
                  "પુનરાવર્તિત થાય.")},
     ]},
    {"title": tr("Temperature", "Temperature"),
     "items": [
         {"q": tr("State the Arrhenius law and explain each term.",
                  "Arrhenius law લખો અને દરેક પદ સમજાવો."),
          "a": tr("k = A exp(-Ea/RT): A is the frequency factor, the number of collisions with the "
                  "right orientation per second; Ea is the activation energy, the barrier the "
                  "collision must clear; R is 8.314 J mol-1 K-1 and T is the absolute temperature.",
                  "k = A exp(-Ea/RT): A frequency factor - પ્રતિ second યોગ્ય દિશા વાળી અથડામણોની "
                  "સંખ્યા; Ea activation energy - અથડામણે પાર કરવો પડતો અવરોધ; R = 8.314 J mol-1 K-1 "
                  "અને T પૂર્ણ temperature.")},
         {"q": tr("Why does a plot of ln k against 1/T give a straight line?",
                  "ln k અને 1/T નો ગ્રાફ સીધી રેખા કેમ આપે?"),
          "a": tr("Because taking logarithms of k = A exp(-Ea/RT) gives ln k = ln A - (Ea/R)(1/T), "
                  "which is y = c + m x with m = -Ea/R. A is almost constant, so the line is straight.",
                  "k = A exp(-Ea/RT) નું log લેવાથી ln k = ln A - (Ea/R)(1/T) મળે, જે y = c + m x છે "
                  "જ્યાં m = -Ea/R. A લગભગ અચળ હોવાથી રેખા સીધી રહે.")},
         {"q": tr("What does a curved Arrhenius plot indicate?",
                  "Arrhenius ગ્રાફ વળેલો હોય તો શું સૂચવે?"),
          "a": tr("That the activation energy is not constant: the mechanism changes with "
                  "temperature, or the rate at high temperature becomes limited by diffusion rather "
                  "than by the chemical step.",
                  "Activation energy અચળ નથી: mechanism temperature સાથે બદલાય છે, અથવા ઊંચા "
                  "temperature પર rate chemical step ને બદલે diffusion થી મર્યાદિત થાય છે.")},
     ]},
    {"title": tr("Activation energy and catalysts", "Activation energy અને catalysts"),
     "items": [
         {"q": tr("How do you find Ea from experimental data?",
                  "પ્રયોગના data પરથી Ea કેવી રીતે શોધાય?"),
          "a": tr("Either from two rate constants with Ea = R ln(k2/k1)/(1/T1 - 1/T2), or better from "
                  "the slope of ln k against 1/T, because the line shows whether Ea is constant.",
                  "કાં બે rate constants પરથી Ea = R ln(k2/k1)/(1/T1 - 1/T2), અથવા વધુ સારી રીતે "
                  "ln k અને 1/T ના ઢાળ પરથી, કારણ કે રેખા બતાવે કે Ea અચળ છે કે નહીં.")},
         {"q": tr("Does a catalyst change the activation energy of the forward and the reverse "
                  "reaction equally?", "Catalyst forward અને reverse પ્રક્રિયાની activation energy "
                  "સરખી બદલે?"),
          "a": tr("Yes. It lowers both by the same number of joules, so the difference between them "
                  "- the heat of reaction - is unchanged. That is exactly why the equilibrium "
                  "constant does not move.",
                  "હા. તે બંનેને સરખા joules ઘટાડે છે, તેથી તેમની વચ્ચેનો તફાવત - heat of reaction - "
                  "ન બદલાય. તેથી જ equilibrium constant ખસતું નથી.")},
         {"q": tr("Why is a reaction with a large Ea dangerous in a plant?",
                  "મોટી Ea વાળી પ્રક્રિયા plant માં જોખમી કેમ?"),
          "a": tr("Because its rate is extremely sensitive to temperature: d ln k/dT = Ea/RT^2, so a "
                  "small rise in temperature gives a large rise in rate, which releases more heat, "
                  "which raises the temperature further - the runaway loop.",
                  "કારણ કે તેનો rate temperature પ્રતિ અત્યંત સંવેદનશીલ છે: d ln k/dT = Ea/RT^2, "
                  "તેથી temperature થોડું વધે તો rate ઘણો વધે, વધુ heat છૂટે, temperature વધુ "
                  "વધે - runaway લૂપ.")},
     ]},
]

# ---------------------------------------------------------------- solved numericals
_PRACTICE = [
    ("Order, rate and the unit of k",
     "Order, rate અને k નું એકમ",
     "The rate law of a reaction is -rA = k CA CB^2. At CA = 0.40 mol/L and CB = 0.20 mol/L the rate "
     "is 1.6 x 10-3 mol L-1 s-1. Find k with its unit, the overall order, and the rate if CA is "
     "doubled.",
     "પ્રક્રિયાનો rate law -rA = k CA CB^2 છે. CA = 0.40 mol/L અને CB = 0.20 mol/L પર rate "
     "1.6 x 10-3 mol L-1 s-1 છે. k તેના એકમ સાથે, કુલ order અને CA બમણું કરતાં rate શોધો.",
     [h4("Step 1 - order", "પગલું 1 - order"),
      math("order = 1 (in A) + 2 (in B) = 3"),
      h4("Step 2 - k", "પગલું 2 - k"),
      math("k = -rA / (CA CB^2)",
           "  = 1.6e-3 / (0.40 x 0.20^2)",
           "  = 1.6e-3 / 0.016 = 0.100"),
      h4("Step 3 - the unit", "પગલું 3 - એકમ"),
      math("mol L-1 s-1 = [k] (mol L-1)^3",
           "[k] = (mol L-1)^(1-3) s-1 = L2 mol-2 s-1"),
      eq("k = 0.100 L2 mol-2 s-1,  overall order 3"),
      h4("Step 4 - double CA", "પગલું 4 - CA બમણું"),
      math("-rA' / -rA = (2 CA / CA)^1 = 2",
           "-rA' = 3.2e-3 mol L-1 s-1"),
      p("Doubling A doubles the rate because it is first order in A; doubling B instead would have "
        "multiplied the rate by four.",
        "A બમણું કરવાથી rate બમણો થાય કારણ કે A માં તે first order છે; તેના બદલે B બમણું કરતાં rate "
        "ચાર ગણો થાત."),
      check("0.100 x 0.40 x 0.04 = 1.6e-3 mol L-1 s-1, the rate given.",
            "0.100 x 0.40 x 0.04 = 1.6e-3 mol L-1 s-1, જે આપેલો rate છે.")],
     6),
    ("Rate constant at another temperature",
     "બીજા temperature પર rate constant",
     "A first order reaction has k = 4.0 x 10-4 s-1 at 300 K and an activation energy of 60 kJ/mol. "
     "Find k at 320 K and the percentage increase per 10 K.",
     "First order પ્રક્રિયાનો 300 K પર k = 4.0 x 10-4 s-1 અને activation energy 60 kJ/mol છે. 320 K પર "
     "k અને પ્રતિ 10 K ટકાવારી વધારો શોધો.",
     [h4("Step 1 - the ratio", "પગલું 1 - ગુણોત્તર"),
      math("ln(k2/k1) = (Ea/R)(1/T1 - 1/T2)",
           "= (60000/8.314)(1/300 - 1/320)",
           "= 7217 x 2.083e-4 = 1.503"),
      h4("Step 2 - k at 320 K", "પગલું 2 - 320 K પર k"),
      math("k2 = k1 e^1.503 = 4.0e-4 x 4.50 = 1.80e-3 s-1"),
      eq("k(320 K) = 1.80 x 10-3 s-1"),
      h4("Step 3 - per 10 K", "પગલું 3 - પ્રતિ 10 K"),
      math("ln(k(310)/k(300)) = 7217 x (1/300 - 1/310) = 0.776",
           "ratio = e^0.776 = 2.17,  so + 117 % per 10 K"),
      p("A 60 kJ/mol barrier nearly doubles the rate every 10 K. Running the reactor 10 K hotter "
        "than the recipe says is not a small change.",
        "60 kJ/mol નો અવરોધ દર 10 K દીઠ rate લગભગ બમણો કરે. Recipe કરતાં 10 K ગરમ ચલાવવું નાનો "
        "ફેરફાર નથી."),
      pit("Comparing k at two temperatures with the ratio of the temperatures (320/300). The rate "
          "constant is exponential, not proportional.", "બે temperature ના k ની સરખામણી temperature ના "
          "ગુણોત્તર (320/300) સાથે કરવી. Rate constant exponential છે, પ્રમાણસર નહીં.")],
     7),
    ("Activation energy from a rate-constant table",
     "Rate-constant કોષ્ટક પરથી activation energy",
     "Using k = 1.2 x 10-5 s-1 at 290 K, 2.4 x 10-5 at 300 K and 4.7 x 10-5 at 310 K, find Ea and A.",
     "290 K પર k = 1.2 x 10-5 s-1, 300 K પર 2.4 x 10-5 અને 310 K પર 4.7 x 10-5 વાપરીને Ea અને A "
     "શોધો.",
     [h4("Step 1 - check that the data is consistent", "પગલું 1 - data સુસંગત છે કે નહીં"),
      math("ln(2.4/1.2) = 0.693 for 1/290 - 1/300 = 1.149e-4",
           "ln(4.7/2.4) = 0.672 for 1/300 - 1/310 = 1.075e-4",
           "Ea = 8.314 x 0.693 / 1.149e-4 = 50.1 kJ/mol",
           "Ea = 8.314 x 0.672 / 1.075e-4 = 52.0 kJ/mol"),
      h4("Step 2 - take the mean", "પગલું 2 - સરેરાશ લો"),
      eq("Ea = 51 kJ/mol  (two steps agree within 4 %)"),
      h4("Step 3 - the frequency factor", "પગલું 3 - frequency factor"),
      math("A = k exp(Ea/RT) = 1.2e-5 exp(51000/(8.314 x 290))",
           "  = 1.2e-5 x e^21.15 = 1.2e-5 x 1.68e9 = 2.0e4 s-1"),
      eq("A = 2.0 x 10^4 s-1"),
      p("A frequency factor of 2e4 s-1 is of the size expected for a unimolecular step: the molecule "
        "tries the reaction about twenty thousand times a second and succeeds only when it has "
        "enough energy.",
        "2e4 s-1 નો frequency factor unimolecular step માટે અપેક્ષિત કદનો છે: molecule પ્રતિ second "
        "લગભગ વીસ હજાર વાર પ્રયત્ન કરે છે અને ફક્ત પૂરતી energy હોય ત્યારે જ સફળ થાય છે."),
      check("Both temperature pairs give Ea near 51 kJ/mol, so a single Ea describes the data - the "
            "reaction does not change mechanism over 290-310 K.",
            "બંને temperature જોડી Ea લગભગ 51 kJ/mol આપે છે, તેથી એક જ Ea data નું વર્ણન કરે - 290-310 "
            "K વચ્ચે પ્રક્રિયા mechanism બદલતી નથી.")],
     8),
    ("Order from initial rates",
     "Initial rates પરથી order",
     "Three runs give: run 1, CA = 0.10, CB = 0.10, rate 2.0 x 10-4; run 2, CA = 0.20, CB = 0.10, "
     "rate 8.0 x 10-4; run 3, CA = 0.10, CB = 0.20, rate 2.0 x 10-4 (all mol/L and mol L-1 s-1). "
     "Find the order in A and in B and the rate constant.",
     "ત્રણ રન આપે છે: રન 1, CA = 0.10, CB = 0.10, rate 2.0 x 10-4; રન 2, CA = 0.20, CB = 0.10, rate "
     "8.0 x 10-4; રન 3, CA = 0.10, CB = 0.20, rate 2.0 x 10-4 (બધા mol/L અને mol L-1 s-1). A અને B માં "
     "order તથા rate constant શોધો.",
     [h4("Step 1 - order in A (runs 1 and 2)", "પગલું 1 - A માં order (રન 1 અને 2)"),
      math("8.0e-4 / 2.0e-4 = (0.20/0.10)^a",
           "4 = 2^a   ->  a = 2"),
      h4("Step 2 - order in B (runs 1 and 3)", "પગલું 2 - B માં order (રન 1 અને 3)"),
      math("2.0e-4 / 2.0e-4 = (0.20/0.10)^b",
           "1 = 2^b   ->  b = 0"),
      h4("Step 3 - rate constant", "પગલું 3 - rate constant"),
      math("k = -rA / CA^2 = 2.0e-4 / 0.010 = 0.020 L mol-1 s-1"),
      eq("order 2 in A, zero in B:  -rA = k CA^2,  k = 2.0 x 10-2 L mol-1 s-1"),
      p("A zero order in B does not mean B is not needed - it means the surface, or a catalyst, is "
        "already saturated with B, so adding more changes nothing.",
        "B માં zero order એટલે B ની જરૂર નથી એમ નહીં - એટલે surface કે catalyst પહેલેથી B થી "
        "સંતૃપ્ત છે, તેથી વધુ ઉમેરવાથી કંઈ બદલાતું નથી."),
      pit("Changing two concentrations in one run. Each run must change exactly one variable, "
          "otherwise the two orders cannot be separated.",
          "એક જ રનમાં બે concentrations બદલવા. દરેક રનમાં ફક્ત એક જ ચલ બદલવો જોઈએ, નહીં તો બે orders "
          "અલગ ન પડે.")],
     6),
    ("A catalyst that lowers Ea by 15 kJ/mol",
     "15 kJ/mol Ea ઘટાડતો catalyst",
     "An uncatalysed reaction has Ea = 75 kJ/mol and A = 5.0 x 10^9 s-1. A catalyst lowers Ea to "
     "60 kJ/mol without changing A. Find the ratio of the rates at 400 K, and the temperature "
     "at which the uncatalysed reaction would be as fast as the catalysed one at 400 K.",
     "Uncatalysed પ્રક્રિયાની Ea = 75 kJ/mol અને A = 5.0 x 10^9 s-1 છે. Catalyst Ea ને 60 kJ/mol "
     "કરે છે અને A ન બદલે. 400 K પર rates નો ગુણોત્તર શોધો, અને એ temperature પણ શોધો જ્યાં "
     "uncatalysed પ્રક્રિયા 400 K ની catalysed પ્રક્રિયા જેટલી ઝડપી થાય.",
     [h4("Step 1 - the ratio at 400 K", "પગલું 1 - 400 K પર ગુણોત્તર"),
      math("k'/k = exp[(Ea - Ea')/RT]",
           "= exp[(75000 - 60000)/(8.314 x 400)]",
           "= exp(4.51) = 91"),
      eq("the catalysed rate is 91 times faster at 400 K"),
      h4("Step 2 - the temperature that replaces the catalyst",
        "પગલું 2 - catalyst ને બદલતું temperature"),
      math("uncatalysed at T  =  catalysed at 400 K:",
           "A exp(-75000/(8.314 T)) = A exp(-60000/(8.314 x 400))",
           "75000/T = 60000/400 = 150   ->   T = 500 K"),
      p("The uncatalysed reaction needs 500 K to reach the rate the catalysed one gives at 400 K, so "
        "the catalyst is worth 100 K of heating. Notice what had to match: the ratio Ea/T, because "
        "75000/500 = 150 and 60000/400 = 150 J mol-1 K-1.",
        "400 K પર catalysed પ્રક્રિયા જેટલી ઝડપ uncatalysed ને 500 K પર મળે છે, એટલે catalyst "
        "100 K ગરમીના બરાબર છે. ધ્યાન આપો કે શું મેળવવું પડ્યું: Ea/T નો ગુણોત્તર, કારણ કે "
        "75000/500 = 150 અને 60000/400 = 150 J mol-1 K-1."),
      check("Catalysed at 400 K: 5e9 exp(-18.04) = 7.3e-5 s-1. Uncatalysed at 500 K: "
            "5e9 exp(-18.04) = 7.3e-5 s-1 - identical, as they must be. Uncatalysed at 400 K is "
            "5e9 exp(-22.55) = 8.0e-7 s-1, and 7.3e-5 / 8.0e-7 = 91, the ratio of step 1.",
            "400 K પર catalysed: 5e9 exp(-18.04) = 7.3e-5 s-1. 500 K પર uncatalysed: "
            "5e9 exp(-18.04) = 7.3e-5 s-1 - બંને સરખા, જેમ હોવા જોઈએ. 400 K પર uncatalysed "
            "5e9 exp(-22.55) = 8.0e-7 s-1, અને 7.3e-5 / 8.0e-7 = 91, એટલે પગલું 1 નો ગુણોત્તર."),
      pit("Confusing the two ways of quoting a catalyst. The <i>rate ratio</i> k'/k = exp[(Ea - Ea')/RT] "
          "is largest at low temperature, while the <i>kelvin saved</i> is a fixed fraction of the "
          "operating temperature - here T_u = T_c x Ea/Ea' = 1.25 T_c, so 25 % of it at any T.",
          "Catalyst ને માપવાની બે રીત ભેળવી દેવી. <i>Rate ratio</i> k'/k = exp[(Ea - Ea')/RT] "
          "નીચા temperature પર સૌથી મોટો હોય, જ્યારે <i>બચતના kelvin</i> operating temperature નો "
          "અચળ ભાગ હોય - અહીં T_u = T_c x Ea/Ea' = 1.25 T_c, એટલે કોઈ પણ T પર તેનો 25 %.")],
     7),
    ("Chain reaction: order from the mechanism",
     "Chain પ્રક્રિયા: mechanism પરથી order",
     "For the chain H2 + Br2 -> 2 HBr the steady-state treatment gives r = k [H2][Br2]^1.5/([Br2] + "
     "k'[HBr]). State the order at the start (no HBr), the order late in the run, and the effect of "
     "doubling [Br2] at the start.",
     "Chain H2 + Br2 -> 2 HBr માટે steady-state પરથી r = k [H2][Br2]^1.5/([Br2] + k'[HBr]) મળે છે. "
     "શરૂઆતમાં (HBr વગર) order, પછીના સમયે order, અને શરૂઆતમાં [Br2] બમણું કરવાની અસર જણાવો.",
     [h4("Step 1 - at the start", "પગલું 1 - શરૂઆતમાં"),
      math("[HBr] ~ 0:  r = k [H2] [Br2]^0.5",
           "order 1 in H2, 0.5 in Br2, 1.5 overall"),
      h4("Step 2 - late in the run", "પગલું 2 - પછીના સમયે"),
      math("[HBr] large:  r ~ (k/k') [H2][Br2]^1.5/[HBr]",
           "the product slows the reaction (inhibition)"),
      h4("Step 3 - doubling Br2 at the start", "પગલું 3 - શરૂઆતમાં Br2 બમણું"),
      math("r' / r = (2)^0.5 = 1.41"),
      eq("rate rises only 41 %, not 100 %"),
      p("An examiner's favourite: the equation has one Br2 on the left, yet the rate depends on the "
        "square root of bromine. Only the mechanism explains that, and only the mechanism earns the "
        "marks.",
        "પરીક્ષકનો પ્રિય પ્રશ્ન: સમીકરણમાં ડાબે એક Br2 છે, છતાં rate bromine ના વર્ગમૂળ પર રહે છે. "
        "તે ફક્ત mechanism સમજાવે છે, અને ફક્ત mechanism જ ગુણ આપે છે."),
      check("Half order appears whenever the steady-state concentration of an atom goes as the square "
            "root of a molecular concentration - the square root comes from the termination step "
            "being second order in the atom.",
            "Half order ત્યારે આવે જ્યારે atom નું steady-state concentration કોઈ molecular "
            "concentration ના વર્ગમૂળ પ્રમાણે હોય - વર્ગમૂળ termination step atom માં second order "
            "હોવાથી આવે છે.")],
     7),
]

PRACTICE = [(tr(h_en, h_gu), tr(q_en, q_gu), body(*parts), m)
            for (h_en, h_gu, q_en, q_gu, parts, m) in _PRACTICE]

EXAM = [{"q": q, "marks": m} for _, q, _, m in PRACTICE]
PRACTICE_ANSWERS = [a for _, _, a, _ in PRACTICE]

SOURCES = [
    ("GTU DI05005031 Chemical Reaction Engineering syllabus (uploaded PDF, w.e.f. 2026-27)",
     "https://syllabus.gtu.ac.in/"),
    ("Octave Levenspiel - Chemical Reaction Engineering, 3rd ed., Wiley (chapter 2: kinetics, "
     "elementary and non-elementary reactions)", "https://www.wiley.com/"),
    ("H. Scott Fogler - Essentials of Chemical Reaction Engineering, 4th ed., Prentice Hall "
     "(chapter 3: rate laws, Arrhenius, activation energy)", "https://www.pearson.com/"),
    ("NPTEL Chemical Reaction Engineering lectures - https://nptel.ac.in/", "https://nptel.ac.in/"),
]
