"""DI01000181 Unit 2, part D: equations, viva, six solved numericals and sources."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from subject_DI01000181 import tr  # noqa: E402
from content_DI01000181_lib import (p, h4, table, math, eq, why, check, pit,  # noqa: E402
                                    body, ul, ol)

EQUATIONS = [
    {"title": tr("Phase rule and the lever rule", "Phase rule અને lever rule"),
     "items": [
         {"name": tr("Gibbs phase rule", "Gibbs phase rule"),
          "f": "F = C - P + 2   (F = C - P + 1 at fixed pressure)",
          "terms": tr("F degrees of freedom, C components, P phases. F = 0 means an invariant point.",
                      "F degrees of freedom, C components, P phases. F = 0 એટલે invariant બિંદુ.")},
         {"name": tr("Amount of liquid", "પ્રવાહીની માત્રા"),
          "f": "W_L = (C_s - C0)/(C_s - C_l)",
          "terms": tr("Compositions read at the two ends of the tie line at that temperature.",
                      "તે temperature પરની tie line ના બે છેડે composition વંચાય છે.")},
         {"name": tr("Amount of solid", "ઘનની માત્રા"),
          "f": "W_s = (C0 - C_l)/(C_s - C_l)",
          "terms": tr("The phase farther from C0 is present in smaller amount.",
                      "C0 થી દૂરનો phase ઓછી માત્રામાં હોય છે.")},
         {"name": tr("Balance check", "સંતુલન ચકાસણી"),
          "f": "W_L + W_s = 1",
          "terms": tr("Use it on every lever-rule answer before writing the final line.",
                      "દરેક lever-rule જવાબમાં અંતિમ લીટી પહેલાં આ વાપરો.")},
     ]},
    {"title": tr("Solidification", "Solidification"),
     "items": [
         {"name": tr("Critical nucleus radius", "Critical nucleus ની ત્રિજ્યા"),
          "f": "r* = 2 gamma Tm/(L dT)",
          "terms": tr("gamma surface energy, L latent heat per volume, dT undercooling.",
                      "gamma surface energy, L volume દીઠ latent heat, dT undercooling.")},
         {"name": tr("Nucleation barrier", "Nucleation નો અવરોધ"),
          "f": "dG* = 16 pi gamma^3 Tm^2/(3 L^2 dT^2)",
          "terms": tr("Falls as 1/dT^2, so a little more undercooling gives many more nuclei.",
                      "1/dT^2 જેટલું ઘટે, તેથી થોડું વધુ undercooling ઘણા વધુ nuclei આપે.")},
         {"name": tr("Length of the thermal arrest", "Thermal arrest ની લંબાઈ"),
          "f": "t_arrest = m Lf/q",
          "terms": tr("m mass of metal, q the rate at which the mould removes heat.",
                      "m ધાતુનું દળ, q એ mould ગરમી લે તેવો દર.")},
         {"name": tr("Freezing range", "Freezing range"),
          "f": "range = T_liquidus - T_solidus",
          "terms": tr("The mushy zone where liquid and solid coexist.",
                      "Mushy zone જ્યાં પ્રવાહી અને ઘન સાથે રહે.")},
     ]},
    {"title": tr("Grain size and strength", "Grain size અને તાકાત"),
     "items": [
         {"name": tr("Hall-Petch", "Hall-Petch"),
          "f": "sigma_y = sigma_0 + k d^(-1/2)",
          "terms": tr("d in mm gives k in MPa mm^0.5; 100 and 23.4 for the steel of this unit.",
                      "d mm માં હોય તો k MPa mm^0.5 માં; આ unit ના સ્ટીલ માટે 100 અને 23.4.")},
         {"name": tr("ASTM grain size number", "ASTM grain size નો આંકડો"),
          "f": "n = 2^(N-1)",
          "terms": tr("n is the number of grains per square inch at 100 magnification.",
                      "n એ 100 magnification પર પ્રતિ ચોરસ ઇંચ grains ની સંખ્યા છે.")},
         {"name": tr("ASTM number from a count", "ગણતરી પરથી ASTM number"),
          "f": "N = 1 + 3.32 log10(n_100)",
          "terms": tr("The 3.32 is 1/log10(2); count three fields and average.",
                      "3.32 એ 1/log10(2) છે; ત્રણ જગ્યાએ ગણીને સરેરાશ લો.")},
         {"name": tr("Grain diameter", "Grain diameter"),
          "f": "d = 25.4/(100 sqrt(2^(N-1))) mm",
          "terms": tr("N = 6 gives 0.045 mm and N = 10 gives 0.011 mm.",
                      "N = 6 માટે 0.045 mm અને N = 10 માટે 0.011 mm.")},
     ]},
    {"title": tr("Iron-carbon fractions", "Iron-carbon ના પ્રમાણ"),
     "items": [
         {"name": tr("Pearlite fraction", "Pearlite નું પ્રમાણ"),
          "f": "pearlite % = (C - 0.02)/(0.80 - 0.02) x 100",
          "terms": tr("Lever rule between the ferrite limit 0.02 and the eutectoid 0.80.",
                      "Ferrite મર્યાદા 0.02 અને eutectoid 0.80 વચ્ચેનો lever rule.")},
         {"name": tr("Cementite fraction", "Cementite નું પ્રમાણ"),
          "f": "Fe3C % = (C - 0.80)/(6.67 - 0.80) x 100",
          "terms": tr("Only for hypereutectoid steels; below 0.8 % it gives a negative number.",
                      "ફક્ત hypereutectoid સ્ટીલ માટે; 0.8 % ની નીચે તે ઋણ આંકડો આપે.")},
         {"name": tr("The two invariant reactions", "બે invariant પ્રક્રિયાઓ"),
          "f": "eutectic: L(4.3) -> gamma + Fe3C at 1147;  eutectoid: gamma(0.8) -> alpha + Fe3C at 727",
          "terms": tr("The first makes ledeburite in cast iron, the second makes pearlite in steel.",
                      "પહેલી cast iron માં ledeburite બનાવે, બીજી સ્ટીલમાં pearlite.")},
     ]},
    {"title": tr("Heat treatment temperatures", "Heat treatment ના temperature"),
     "items": [
         {"name": tr("The eutectoid line", "Eutectoid રેખા"),
          "f": "A1 = 727 C",
          "terms": tr("The same for every steel; nothing transforms below it except tempering.",
                      "દરેક સ્ટીલ માટે એ જ; તેની નીચે tempering સિવાય કંઈ બદલાતું નથી.")},
         {"name": tr("A3 for a hypoeutectoid steel", "Hypoeutectoid સ્ટીલ માટે A3"),
          "f": "A3 = 912 - 231 C   (C in % by weight)",
          "terms": tr("An approximation of the G-S line, good to about 10 C up to 0.8 % C.",
                      "G-S રેખાનો અંદાજ, 0.8 % C સુધી લગભગ 10 C સુધી સાચો.")},
         {"name": tr("Acm for a hypereutectoid steel", "Hypereutectoid સ્ટીલ માટે Acm"),
          "f": "Acm = 727 + 313 (C - 0.80)",
          "terms": tr("The S-E line; hardening temperature is kept just above A1 for these steels.",
                      "S-E રેખા; આ સ્ટીલ માટે hardening temperature A1 થી થોડું ઉપર રખાય.")},
     ]},
]

VIVA = [
    {"title": tr("Phases and the phase rule", "Phase અને phase rule"),
     "items": [
         {"q": tr("What is a phase, and how many phases are in a 0.4 % carbon steel at room "
                  "temperature?",
                  "Phase એટલે શું, અને room temperature પર 0.4 % carbon સ્ટીલમાં કેટલા phase છે?"),
          "a": tr("A part of the material with the same structure and composition everywhere. Two: "
                  "ferrite and cementite, arranged as ferrite grains and pearlite.",
                  "સામગ્રીનો જે ભાગ બધે એક જ રચના અને composition ધરાવે. બે: ferrite અને cementite, "
                  "જે ferrite grains અને pearlite સ્વરૂપે ગોઠવાયેલા છે.")},
         {"q": tr("State the Gibbs phase rule and give one invariant point from this unit.",
                  "Gibbs phase rule કહો અને આ unit માંથી એક invariant બિંદુ આપો."),
          "a": tr("F = C - P + 2, and F = C - P + 1 once the pressure is fixed at one atmosphere. "
                  "The lead-tin eutectic at 183 C and 61.9 % tin has C = 2 P = 3, so F = 0 - an "
                  "invariant point.",
                  "F = C - P + 2, અને pressure એક જ atmosphere પર નિશ્ચિત હોય તો F = C - P + 1. 183 C "
                  "અને 61.9 % tin પરનું lead-tin eutectic માં C = 2, P = 3, તેથી F = 0 - invariant બિંદુ.")},
         {"q": tr("Why does a pure metal show a flat arrest on its cooling curve but an alloy does not?",
                  "શુદ્ધ ધાતુની cooling curve સપાટ arrest કેમ દેખાય પણ alloy માં નહીં?"),
          "a": tr("A pure metal freezes at one temperature, so the latent heat holds the curve flat. "
                  "An alloy freezes over a range, releasing latent heat gradually, so only the slope "
                  "changes.",
                  "શુદ્ધ ધાતુ એક જ temperature પર થીજે તેથી latent heat રેખા સપાટ રાખે. Alloy એક "
                  "range માં થીજે અને latent heat ધીમે છોડે, તેથી ફક્ત ઢાળ બદલાય.")},
     ]},
    {"title": tr("Solid solutions and diagrams", "Solid solution અને diagram"),
     "items": [
         {"q": tr("State any three Hume-Rothery rules.",
                  "Hume-Rothery ના કોઈ પણ ત્રણ નિયમ કહો."),
          "a": tr("Size difference below 15 %; the same crystal structure; similar valency and "
                  "electronegativity. Break them and solubility falls or a compound forms.",
                  "માપનો ફરક 15 % થી ઓછો; એક જ crystal structure; સરખી valency અને electronegativity. "
                  "તૂટે તો solubility ઘટે કે compound બને.")},
         {"q": tr("Why is carbon interstitial in iron while nickel is substitutional?",
                  "Iron માં carbon interstitial અને nickel substitutional કેમ છે?"),
          "a": tr("Carbon's radius is 77 pm against iron's 126 pm, far too small for a lattice site, "
                  "so it sits in the gaps. Nickel is 125 pm, almost exactly iron's size.",
                  "Carbon ની radius 77 pm છે જ્યારે iron ની 126 pm, lattice ની જગ્યા માટે ઘણી નાની, "
                  "તેથી તે ખાલી જગ્યામાં બેસે. Nickel 125 pm છે, લગભગ iron જેટલી જ.")},
         {"q": tr("Read out the compositions of the two phases at 1300 C in the Cu-Ni diagram.",
                  "Cu-Ni diagram માં 1300 C પર બે phase નું composition કહો."),
          "a": tr("40 % nickel in the liquid and 60 % nickel in the solid, from the two ends of the "
                  "tie line, and the lever rule then gives half of each for a 50 % alloy.",
                  "Tie line ના બે છેડે પ્રવાહીમાં 40 % nickel અને ઘનમાં 60 % nickel, અને પછી lever "
                  "rule 50 % alloy માટે દરેકનો અડધો ભાગ આપે.")},
     ]},
    {"title": tr("The iron-carbon diagram", "Iron-carbon diagram"),
     "items": [
         {"q": tr("What is the difference between the eutectic and the eutectoid of the Fe-C diagram?",
                  "Fe-C diagram ના eutectic અને eutectoid માં શું ફરક છે?"),
          "a": tr("The eutectic at 1147 C and 4.3 % C turns liquid into two solids. The eutectoid at "
                  "727 C and 0.8 % C turns one solid (austenite) into two solids (ferrite and "
                  "cementite).",
                  "1147 C અને 4.3 % C પરનું eutectic પ્રવાહીને બે ઘનમાં ફેરવે. 727 C અને 0.8 % C પરનું "
                  "eutectoid એક ઘન (austenite) ને બે ઘન (ferrite અને cementite) માં ફેરવે.")},
         {"q": tr("Why can austenite hold 2.14 % carbon but ferrite only 0.02 %?",
                  "Austenite 2.14 % carbon કેમ રાખી શકે પણ ferrite ફક્ત 0.02 %?"),
          "a": tr("Austenite is FCC and its interstitial hole is larger and there are more of them per "
                  "cell; ferrite is BCC with a smaller, distorted hole.",
                  "Austenite FCC છે અને તેની interstitial જગ્યા મોટી તથા cell દીઠ વધુ છે; ferrite BCC "
                  "છે જેની જગ્યા નાની અને વળેલી છે.")},
         {"q": tr("What happens to the microstructure of a 1.2 % carbon steel cooled slowly?",
                  "1.2 % carbon સ્ટીલને ધીમે ઠંડું કરો તો microstructure શું થાય?"),
          "a": tr("Proeutectoid cementite forms a network on the austenite grain boundaries and the "
                  "rest becomes pearlite - about 6.8 % cementite and 93 % pearlite.",
                  "Proeutectoid cementite austenite grain boundary પર જાળી બનાવે અને બાકીનું pearlite "
                  "થાય - લગભગ 6.8 % cementite અને 93 % pearlite.")},
     ]},
    {"title": tr("Heat treatment", "Heat treatment"),
     "items": [
         {"q": tr("What are the three steps of any heat treatment?",
                  "કોઈ પણ heat treatment નાં ત્રણ પગલાં કયાં છે?"),
          "a": tr("Heat to a chosen temperature above the critical line, hold until the structure is "
                  "uniform, and cool at a chosen rate.",
                  "Critical line ઉપર પસંદ કરેલા temperature સુધી ગરમ કરવું, રચના સરખી થાય ત્યાં સુધી "
                  "રાખવું, અને પસંદ કરેલા દરથી ઠંડું કરવું.")},
         {"q": tr("What is the difference between annealing and normalising?",
                  "Annealing અને normalising માં શું ફરક છે?"),
          "a": tr("The temperature is the same; the cooling is different. Annealing cools in the "
                  "furnace and gives soft coarse pearlite, normalising cools in air and gives finer, "
                  "stronger pearlite.",
                  "Temperature એ જ છે; ઠંડું કરવાની રીત જુદી છે. Annealing furnace માં ઠંડું કરે અને નરમ "
                  "જાડું pearlite આપે, normalising હવામાં ઠંડું કરે અને નાનું, વધુ મજબૂત pearlite આપે.")},
         {"q": tr("Why is a hardened steel always tempered?",
                  "Hardened સ્ટીલને હંમેશા temper કેમ કરાય છે?"),
          "a": tr("Quenching traps carbon and leaves martensite, which is very hard but brittle. "
                  "Tempering below A1 relieves the strain and restores toughness at some cost in "
                  "hardness.",
                  "Quenching carbon ફસાવે અને martensite રહે, જે ખૂબ સખત પણ ભંગુર છે. A1 ની નીચે "
                  "tempering તણાવ ઘટાડે અને hardness થોડી ગુમાવીને toughness પાછી આપે.")},
     ]},
]


_PRACTICE = [
    ("Phase rule on four points",
     "ચાર બિંદુ પર phase rule",
     "Apply the phase rule at four points and state what the number means: (a) pure iron at 1450 C in "
     "the austenite field, (b) pure iron at 1538 C where solid and liquid coexist, (c) the lead-tin "
     "eutectic at 183 C, (d) a 40 % tin alloy at 200 C where alpha and liquid coexist.",
     "ચાર બિંદુ પર phase rule લાગુ કરો અને આંકડાનો અર્થ કહો: (a) austenite વિસ્તારમાં 1450 C પર શુદ્ધ "
     "iron, (b) 1538 C પર જ્યાં ઘન અને પ્રવાહી સાથે છે, (c) 183 C પરનું lead-tin eutectic, (d) 200 C પર "
     "40 % tin નું alloy જ્યાં alpha અને પ્રવાહી સાથે છે.",
     [h4("Step 1 - the formula and the components", "પગલું 1 - સૂત્ર અને components"),
      math("F = C - P + 2, and at the fixed pressure of 1 atm we use F = C - P + 1",
           "pure iron: C = 1     iron-carbon or lead-tin: C = 2"),
      h4("Step 2 - one point at a time", "પગલું 2 - એક એક બિંદુ"),
      math("(a) C=1, P=1 (austenite only)        F = 1-1+1 = 1",
           "(b) C=1, P=2 (solid + liquid)        F = 1-2+1 = 0",
           "(c) C=2, P=3 (L + alpha + beta)      F = 2-3+1 = 0",
           "(d) C=2, P=2 (alpha + liquid)        F = 2-2+1 = 1"),
      h4("Step 3 - what the numbers mean", "પગલું 3 - આંકડાનો અર્થ"),
      math("F = 1: choose the temperature, the compositions then follow the field boundaries",
           "F = 0: nothing is free - the point is invariant",
           "at the melting point of iron the temperature stays at 1538 C until it is all liquid",
           "at 183 C the lead-tin eutectic freezes completely at that one temperature"),
      eq("(a) F = 1,  (b) F = 0 invariant,  (c) F = 0 invariant,  (d) F = 1"),
      p("Point (c) is the reason a eutectic alloy freezes at a single temperature: with three phases "
        "in a two-component system there is no freedom left, so the temperature cannot fall until one "
        "phase disappears. Point (d) is the ordinary two-phase field - you pick the temperature and "
        "the tie line then fixes both compositions, which is why the lever rule works there.",
        "બિંદુ (c) એ જ કારણ છે કે eutectic alloy એક જ temperature પર થીજે: બે-component system માં ત્રણ "
        "phase હોય તો કોઈ સ્વતંત્રતા બચતી નથી, તેથી એક phase જાય નહીં ત્યાં સુધી temperature ઘટી શકે નહીં. "
        "બિંદુ (d) સામાન્ય બે-phase field છે - તમે temperature પસંદ કરો અને પછી tie line બંને composition "
        "નક્કી કરે, તેથી જ ત્યાં lever rule ચાલે છે."),
      check("If you use F = C - P + 2 without fixing the pressure, every answer here goes up by one. "
            "Say which rule you are using - the examiner is looking for that sentence.",
            "Pressure નિશ્ચિત કર્યા વગર F = C - P + 2 વાપરો તો અહીંનો દરેક જવાબ એક વધે. તમે કયો નિયમ "
            "વાપરો છો તે લખો - પરીક્ષક એ જ વાક્ય શોધે છે.")],
     6),

    ("Lever rule on a lead-tin alloy",
     "Lead-tin alloy પર lever rule",
     "A 40 % tin solder is held at 200 C. Read the compositions of the two phases from the diagram, "
     "find the mass of each in 2 kg of alloy, and say what happens to the last liquid when the alloy "
     "cools to 183 C.",
     "40 % tin નું solder 200 C પર રખાય છે. Diagram પરથી બે phase નું composition વાંચો, 2 kg alloy માં "
     "દરેકનું દળ શોધો, અને alloy 183 C સુધી ઠંડું થાય ત્યારે છેલ્લા પ્રવાહીનું શું થાય તે કહો.",
     [h4("Step 1 - read the tie line", "પગલું 1 - tie line વાંચો"),
      math("at 200 C the tie line runs from C_alpha to C_liquid",
           "alpha (lead-rich, left end):  C_alpha = 17 % Sn",
           "liquid (right end):            C_L     = 55 % Sn",
           "alloy:                         C0      = 40 % Sn"),
      h4("Step 2 - the lever rule", "પગલું 2 - lever rule"),
      math("W_L     = (C0 - C_alpha)/(C_L - C_alpha) = (40 - 17)/(55 - 17) = 23/38 = 0.605",
           "W_alpha = (C_L - C0)/(C_L - C_alpha)      = (55 - 40)/(55 - 17) = 15/38 = 0.395",
           "check: 0.605 + 0.395 = 1.000"),
      h4("Step 3 - the masses in 2 kg", "પગલું 3 - 2 kg માં દળ"),
      math("m_L     = 0.605 x 2 = 1.21 kg of liquid, 55 % Sn",
           "m_alpha = 0.395 x 2 = 0.79 kg of alpha, 17 % Sn",
           "the liquid is the phase farther from C0, so it is the larger one"),
      eq("17 % and 55 % Sn,  60.5 % liquid and 39.5 % alpha,  1.21 kg and 0.79 kg"),
      p("As the alloy cools further the liquid follows the liquidus down to the eutectic point: the "
        "last drop of liquid is 61.9 % tin and it freezes at 183 C into alpha and beta together. That "
        "is why the microstructure of a 40 % solder shows primary alpha with eutectic between the "
        "arms.",
        "Alloy વધુ ઠંડું થાય તો પ્રવાહી liquidus પર ચાલીને eutectic બિંદુ સુધી જાય: છેલ્લું ટીપું 61.9 % "
        "tin નું હોય અને 183 C પર alpha તથા beta સાથે થીજે. તેથી જ 40 % solder ના microstructure માં "
        "primary alpha વચ્ચે eutectic દેખાય."),
      pit("The lever rule arms are measured from C0, not from zero: taking (40 - 0)/(55 - 17) is the "
          "commonest mistake and it gives an answer larger than 1.",
          "Lever rule ના arms C0 થી મપાય છે, શૂન્યથી નહીં: (40 - 0)/(55 - 17) લેવી એ સૌથી સામાન્ય ભૂલ "
          "છે અને તે 1 થી મોટો જવાબ આપે છે.")],
     7),

    ("Copper-nickel: tie line, fractions and a check at a lower temperature",
     "Copper-nickel: tie line, પ્રમાણ અને નીચા temperature પર ચકાસણી",
     "A 50 % nickel cupro-nickel is at 1300 C. Find the composition of the liquid and of the solid, "
     "the mass of each in 3 kg, and show that the same alloy at 1250 C is completely solid.",
     "50 % nickel નું cupro-nickel 1300 C પર છે. પ્રવાહી અને ઘનનું composition, 3 kg માં દરેકનું દળ "
     "શોધો, અને એ જ alloy 1250 C પર સંપૂર્ણ ઘન છે તે દર્શાવો.",
     [h4("Step 1 - the tie line at 1300 C", "પગલું 1 - 1300 C પરની tie line"),
      math("liquidus at 1300 C:  C_L = 40 % Ni",
           "solidus  at 1300 C:  C_s = 60 % Ni",
           "alloy:               C0  = 50 % Ni"),
      h4("Step 2 - the lever rule and the masses", "પગલું 2 - lever rule અને દળ"),
      math("W_L = (60 - 50)/(60 - 40) = 0.50",
           "W_s = (50 - 40)/(60 - 40) = 0.50",
           "m_L = 1.50 kg,  m_s = 1.50 kg in 3 kg of alloy"),
      h4("Step 3 - the check at 1250 C", "પગલું 3 - 1250 C પર ચકાસણી"),
      math("solidus at 50 % Ni: interpolate between (40, 1240) and (60, 1300)",
           "T_solidus = 1240 + (50 - 40)/(60 - 40) x 60 = 1270 C",
           "1250 C is below 1270 C, so the alloy has already finished freezing",
           "W_L = 0 - it is 100 % solid solution, 50 % Ni throughout"),
      eq("40 % and 60 % Ni,  half and half (1.5 kg each),  and at 1250 C it is 100 % solid"),
      why("Both answers come from the same diagram, which is the point of drawing one. The tie line "
          "gives the compositions, the lever rule gives the amounts, and the boundary of the field "
          "tells you when an answer of zero must be expected.",
          "બંને જવાબ એક જ diagram પરથી આવે, અને diagram દોરવાનો આ જ ફાયદો છે. Tie line composition "
          "આપે, lever rule માત્રા આપે, અને field ની સીમા કહે કે શૂન્ય જવાબ ક્યારે આવવો જોઈએ."),
      check("A single-phase field always answers 100 % of one phase; if your lever rule gives a "
            "negative weight, the alloy is not in the two-phase field at all.",
            "Single-phase field હંમેશા એક phase નું 100 % આપે; તમારો lever rule ઋણ weight આપે તો alloy "
            "બે-phase field માં જ નથી.")],
     7),

    ("Pearlite and cementite in two steels",
     "બે સ્ટીલમાં pearlite અને cementite",
     "Using the eutectoid values, find the percentage of pearlite and of proeutectoid ferrite in a "
     "0.4 % carbon steel, and the percentage of cementite in a 1.2 % carbon steel. Give the masses in "
     "5 kg of each and explain the difference in properties.",
     "Eutectoid મૂલ્યો વાપરીને 0.4 % carbon સ્ટીલમાં pearlite અને proeutectoid ferrite ની ટકાવારી, અને "
     "1.2 % carbon સ્ટીલમાં cementite ની ટકાવારી શોધો. દરેકના 5 kg માં દળ આપો અને ગુણધર્મોમાં ફરક "
     "સમજાવો.",
     [h4("Step 1 - the phase boundaries", "પગલું 1 - phase સીમાઓ"),
      math("ferrite at 727 C:      0.02 % C",
           "eutectoid austenite:   0.80 % C",
           "cementite:             6.67 % C"),
      h4("Step 2 - the 0.4 % steel", "પગલું 2 - 0.4 % સ્ટીલ"),
      math("pearlite % = (0.40 - 0.02)/(0.80 - 0.02) x 100 = 0.38/0.78 x 100 = 48.7 %",
           "proeutectoid ferrite = 100 - 48.7 = 51.3 %",
           "in 5 kg: pearlite 2.44 kg, ferrite 2.56 kg"),
      h4("Step 3 - the 1.2 % steel", "પગલું 3 - 1.2 % સ્ટીલ"),
      math("Fe3C %  = (1.20 - 0.80)/(6.67 - 0.80) x 100 = 0.40/5.87 x 100 = 6.8 %",
           "pearlite = 100 - 6.8 = 93.2 %",
           "in 5 kg: cementite 0.34 kg, pearlite 4.66 kg"),
      eq("0.4 % C: 48.7 % pearlite;  1.2 % C: 6.8 % cementite;  masses 2.44 / 0.34 kg"),
      p("The 0.4 % steel is half soft ferrite, so it is tough and is used for shafts and axles. The "
        "1.2 % steel has a cementite network round every grain, so it is much harder and much more "
        "brittle - the right choice for a file, the wrong one for a shaft.",
        "0.4 % સ્ટીલ અડધું નરમ ferrite છે, તેથી તે tough છે અને shafts તથા axles માટે વપરાય. 1.2 % સ્ટીલમાં "
        "દરેક grain ફરતે cementite ની જાળી હોય છે, તેથી તે ઘણું સખત અને ઘણું ભંગુર છે - file માટે યોગ્ય, "
        "shaft માટે ખોટું."),
      pit("Below 0.8 % carbon the formula for cementite gives a negative number - that is the signal "
          "that there is no proeutectoid cementite in the steel, not that the formula is wrong.",
          "0.8 % થી નીચે carbon હોય તો cementite નું સૂત્ર ઋણ આંકડો આપે - એ સંકેત છે કે સ્ટીલમાં "
          "proeutectoid cementite નથી, સૂત્ર ખોટું નથી.")],
     8),

    ("Hall-Petch: two grain sizes and a target strength",
     "Hall-Petch: બે grain size અને એક લક્ષ્ય તાકાત",
     "For a low carbon steel sigma_0 = 100 MPa and k = 23.4 MPa mm^0.5. Find the yield strength for "
     "grain sizes of 0.25 mm and 0.04 mm, and the grain size needed for a yield strength of 300 MPa.",
     "ઓછા carbon ના સ્ટીલ માટે sigma_0 = 100 MPa અને k = 23.4 MPa mm^0.5 છે. 0.25 mm અને 0.04 mm "
     "grain size માટે yield strength શોધો, અને 300 MPa yield strength માટે જરૂરી grain size શોધો.",
     [h4("Step 1 - the relation", "પગલું 1 - સંબંધ"),
      math("sigma_y = sigma_0 + k d^(-1/2)",
           "d must be in mm, otherwise k has a different value"),
      h4("Step 2 - the two grain sizes", "પગલું 2 - બે grain size"),
      math("d = 0.25 mm:   d^-1/2 = 1/0.5 = 2.00 -> sigma_y = 100 + 23.4 x 2.00 = 147 MPa",
           "d = 0.04 mm:   d^-1/2 = 1/0.2 = 5.00 -> sigma_y = 100 + 23.4 x 5.00 = 217 MPa",
           "the finer grain is 70 MPa stronger, with the same composition"),
      h4("Step 3 - the grain size for 300 MPa", "પગલું 3 - 300 MPa માટે grain size"),
      math("300 = 100 + 23.4 d^(-1/2)",
           "d^(-1/2) = 200/23.4 = 8.547",
           "d = 1/8.547^2 = 0.0137 mm = 13.7 micrometre"),
      eq("147 MPa, 217 MPa, and d = 0.0137 mm for 300 MPa"),
      why("The 13.7 micrometre grain is fine but not impossible: normalising a 0.2 % steel gives about "
          "20 micrometre and a controlled rolling schedule reaches 10. The limit is that very fine "
          "grains coarsen when the steel is welded or held hot.",
          "13.7 micrometre નું grain નાનું છે પણ અશક્ય નહીં: 0.2 % સ્ટીલ normalise કરો તો લગભગ 20 "
          "micrometre મળે અને નિયંત્રિત rolling થી 10 સુધી પહોંચાય. મર્યાદા એ છે કે ખૂબ નાના grains "
          "વેલ્ડિંગ કે ગરમ રાખવાથી જાડા થઈ જાય."),
      check("Put the answers back: 100 + 23.4/0.5 = 147 and 100 + 23.4/0.2 = 217, and for the third "
            "100 + 23.4 x 8.547 = 300. All three close.",
            "જવાબ પાછા મૂકો: 100 + 23.4/0.5 = 147 અને 100 + 23.4/0.2 = 217, અને ત્રીજા માટે "
            "100 + 23.4 x 8.547 = 300. ત્રણેય મળે છે.")],
     6),

    ("From an ASTM grain size number to a yield strength",
     "ASTM grain size number થી yield strength સુધી",
     "A micrograph of a steel shows ASTM grain size 6, another shows 10. Convert both to a grain "
     "diameter in millimetres and then to a yield strength with sigma_0 = 100 MPa and "
     "k = 23.4 MPa mm^0.5, and state the percentage gain.",
     "એક સ્ટીલના micrograph માં ASTM grain size 6 છે, બીજામાં 10. બંનેને મિલીમીટરમાં grain diameter "
     "અને પછી sigma_0 = 100 MPa તથા k = 23.4 MPa mm^0.5 સાથે yield strength માં ફેરવો, અને ટકાવારી "
     "વધારો કહો.",
     [h4("Step 1 - the ASTM number to a grain diameter", "પગલું 1 - ASTM number થી grain diameter"),
      math("d = 25.4/(100 x sqrt(2^(N-1))) mm",
           "N = 6:  n = 2^5 = 32,  d = 25.4/(100 x 5.657) = 0.0449 mm",
           "N = 10: n = 2^9 = 512, d = 25.4/(100 x 22.63) = 0.0112 mm"),
      h4("Step 2 - Hall-Petch for each", "પગલું 2 - દરેક માટે Hall-Petch"),
      math("N = 6:  d^-1/2 = 1/sqrt(0.0449) = 4.72 -> sigma_y = 100 + 23.4 x 4.72 = 210 MPa",
           "N = 10: d^-1/2 = 1/sqrt(0.0112) = 9.45 -> sigma_y = 100 + 23.4 x 9.45 = 321 MPa"),
      h4("Step 3 - the gain", "પગલું 3 - વધારો"),
      math("gain = (321 - 210)/210 x 100 = 52.9 %",
           "for four ASTM numbers, about 53 % more yield strength"),
      eq("0.045 mm and 0.011 mm;  210 MPa and 321 MPa;  a 53 % gain"),
      p("Four ASTM numbers is a factor of four in grain size, which is a factor of two in d^-1/2 - and "
        "that is why the gain is not 400 % but 53 %. Hall-Petch is linear in d^-1/2, not in d.",
        "ચાર ASTM number એ grain size માં ચાર ગણો ફરક છે, જે d^-1/2 માં બે ગણો ફરક છે - અને તેથી જ "
        "વધારો 400 % નહીં પણ 53 % છે. Hall-Petch d^-1/2 માં રેખીય છે, d માં નહીં."),
      pit("d must be in millimetres for this k. Feed the value in micrometres and the answer comes out "
          "about thirty times too large.",
          "આ k માટે d મિલીમીટરમાં જ જોઈએ. Micrometre માં મૂકો તો જવાબ લગભગ ત્રીસ ગણો મોટો આવે.")],
     7),
]

PRACTICE = [(tr(h_en, h_gu), tr(q_en, q_gu), body(*parts_), m)
            for (h_en, h_gu, q_en, q_gu, parts_, m) in _PRACTICE]

EXAM = [{"q": q, "marks": m} for _, q, _, m in PRACTICE]
PRACTICE_ANSWERS = [a for _, _, a, _ in PRACTICE]

SOURCES = [
    ("GTU DI01000181 Engineering Materials Science syllabus (uploaded PDF, w.e.f. 2024-25)",
     "https://syllabus.gtu.ac.in/"),
    ("G. B. S. Narang - Materials Science, Khanna Publishers (phase diagrams, solidification, "
     "iron-carbon diagram)", "https://www.khannapublishers.in/"),
    ("V. Raghavan - Materials Science and Engineering, Prentice Hall India (phase rule, lever rule, "
     "heat treatment)", "https://www.pearson.com/"),
    ("Substech open materials science reference - iron-carbon diagram and cooling curves",
     "https://www.substech.com/dokuwiki/doku.php?id=iron_carbon_phase_diagram"),
    ("NPTEL course on phase transformations and heat treatment of steels",
     "https://nptel.ac.in/courses/113106032"),
]
