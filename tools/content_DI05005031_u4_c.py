"""DI05005031 Unit 4, part C: section 4.3 (multiphase reactors), the formulas, the viva and the six
solved numericals."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from subject_DI05005031 import tr  # noqa: E402
from content_DI05005031_lib import (p, h4, ul, ol, table, math, eq, why, check, pit, derive,
                                    parts, working, body, card)  # noqa: E402

NOTES_C = []

NOTES_C.append({
    "title": tr("4.3 Multiphase reactors: gas, liquid and solid together",
                "4.3 Multiphase reactors: gas, liquid અને solid સાથે"),
    "items": [
        card(
            "Slurry and bubble column reactors",
            "Slurry અને bubble column reactors",
            p("When a gas must react with a liquid, or with a solid catalyst suspended in a liquid, "
              "the contact area between the phases becomes the design problem. Two of the simplest "
              "answers are the bubble column - gas bubbled through a liquid with no moving parts - "
              "and the slurry reactor - the same, plus a stirrer to keep the solid in suspension.",
              "જ્યારે gas ને પ્રવાહી સાથે, કે પ્રવાહીમાં તરતા ઘન catalyst સાથે પ્રક્રિયા કરવી હોય ત્યારે "
              "phases વચ્ચેનું contact area design ની સમસ્યા બને. બે સાદા જવાબ છે bubble column - ન હલતા "
              "ભાગ સાથે પ્રવાહીમાં gas ના bubbles - અને slurry reactor - એ જ, પણ ઘનને તરતો રાખવા "
              "stirrer સાથે."),
            parts(("Sparger or distributor at the bottom - makes many small bubbles, because small "
                   "bubbles mean more interfacial area.", "તળિયે sparger કે distributor - ઘણા નાના "
                   "bubbles બનાવે, કારણ કે નાના bubbles વધુ interfacial area આપે."),
                  ("Column or vessel - the liquid is the continuous phase and holds the gas long "
                   "enough for it to dissolve.", "Column કે પાત્ર - પ્રવાહી સતત phase છે અને gas ને "
                   "ઓગળવા પૂરતો સમય રોકે."),
                  ("Stirrer (slurry reactor only) - keeps the fine catalyst in suspension and breaks "
                   "the bubbles.", "Stirrer (ફક્ત slurry reactor) - બારીક catalyst તરતો રાખે અને "
                   "bubbles તોડે."),
                  ("Jacket or coil - these reactions are usually exothermic hydrogenations or "
                   "oxidations.", "Jacket કે coil - આ પ્રક્રિયાઓ સામાન્ય રીતે exothermic "
                   "hydrogenation કે oxidation હોય."),
                  ("Settler, filter or cyclone on the outlet - keeps the catalyst in the reactor.",
                   "Outlet પર settler, filter કે cyclone - catalyst ને reactor માં રાખે.")),
            working(("Gas enters through the sparger and rises as a swarm of bubbles.",
                     "Gas sparger થી આવે અને bubbles ના ઝુંડ તરીકે ઉપર જાય."),
                    ("It dissolves into the liquid film; the dissolved gas then diffuses to the "
                     "catalyst.", "તે પ્રવાહીના પડમાં ઓગળે; ઓગળેલો gas પછી catalyst સુધી ફેલાય."),
                    ("Reaction takes place on or in the solid; the product leaves with the liquid.",
                     "પ્રક્રિયા ઘન પર કે અંદર થાય; product પ્રવાહી સાથે નીકળે."),
                    ("The slowest of the three steps - dissolution, diffusion, reaction - sets the "
                     "overall rate.", "ત્રણ પૈકી સૌથી ધીમું પગલું - ઓગળવું, ફેલાવો, પ્રક્રિયા - કુલ rate "
                     "નક્કી કરે.")),
            h4("The rate when mass transfer interferes", "જ્યારે mass transfer વચ્ચે આવે ત્યારે rate"),
            derive("gas film and liquid film resistances in series:",
                   "1/K = 1/(kG a) + 1/(kL a H) + 1/(k' a H)",
                   "if the reaction is fast, kL a controls: rate = kL a (CA* - CA)",
                   "if it is slow, the kinetics control and the reactor is a well-mixed vessel"),
            table([tr("Reactor", "Reactor"), tr("Moving parts", "હલતા ભાગ"),
                   tr("Typical duty", "સામાન્ય કામ"), tr("Main worry", "મુખ્ય ચિંતા")],
                  [[tr("Bubble column", "Bubble column"), tr("none", "કંઈ નહીં"),
                    tr("oxidation, fermentation, ozonation", "oxidation, fermentation, ozonation"),
                    tr("bubble coalescence and back-mixing", "bubble જોડાવું અને back-mixing")],
                   [tr("Slurry reactor", "Slurry reactor"), tr("stirrer", "stirrer"),
                    tr("hydrogenation with a fine catalyst",
                       "બારીક catalyst સાથે hydrogenation"),
                    tr("catalyst attrition and separation",
                       "catalyst ઘસાવું અને અલગ કરવું")]]),
            why("A slurry reactor gives up plug flow and gains a uniform temperature and a catalyst "
                "that can be very fine - which is what a fast, exothermic three-phase reaction needs.",
                "Slurry reactor plug flow ગુમાવે અને સરખું temperature તથા ખૂબ બારીક catalyst મેળવે - જે "
                "ઝડપી, exothermic three-phase પ્રક્રિયાને જોઈએ."),
            check("If kL a is doubled by better sparging, a mass-transfer-limited reaction doubles its "
                  "rate while a kinetically limited one does not move at all.",
                  "સારા sparging થી kL a બમણું થાય તો mass-transfer-limited પ્રક્રિયાનો rate બમણો થાય "
                  "જ્યારે kinetically limited પ્રક્રિયા જરાય ન બદલાય."),
            pit("Treating a bubble column as a CSTR of liquid. Gas hold-up can be 10-20 % of the "
                "volume, so the liquid residence time is shorter than V/vL suggests.",
                "Bubble column ને પ્રવાહીના CSTR ગણવું. Gas hold-up volume ના 10-20 % હોઈ શકે, તેથી "
                "પ્રવાહીનો residence time V/vL કહે તેના કરતાં ટૂંકો હોય."),
            diagram="u4_slurry",
            syllabus_item="4.3",
        ),
        card(
            "Spray tower and trickle bed",
            "Spray tower અને trickle bed",
            p("The other two multiphase arrangements put the phases in contact in opposite ways: in a "
              "spray tower the liquid is broken into drops, in a trickle bed the liquid is spread as "
              "a film over a fixed packing.",
              "બાકીની બે multiphase ગોઠવણી phasesને વિરુદ્ધ રીતે સંપર્કમાં લાવે: spray tower માં પ્રવાહી "
              "ટીપાંમાં તૂટે, trickle bed માં પ્રવાહી સ્થિર packing પર પડ તરીકે ફેલાય."),
            parts(("Spray tower: nozzle or atomiser at the top - makes drops of 100-1000 micron, and "
                   "the drop size sets the area.", "Spray tower: ઉપર nozzle કે atomiser - 100-1000 "
                   "micron ના ટીપાં બનાવે, અને ટીપાંનું size જ area નક્કી કરે."),
                  ("Spray tower: empty shell with a gas inlet at the bottom - counter-current, no "
                   "packing to foul or block.", "Spray tower: તળિયે gas inlet વાળું ખાલી પાત્ર - "
                   "counter-current, ગંદું થાય કે બંધાય તેવું packing નહીં."),
                  ("Spray tower: liquid outlet and pump - the liquid is recirculated many times.",
                   "Spray tower: પ્રવાહીનું outlet અને pump - પ્રવાહી ઘણી વાર recirculate થાય."),
                  ("Trickle bed: liquid distributor tray above the packing, drilled with many holes.",
                   "Trickle bed: packing ઉપર liquid distributor tray, ઘણા છિદ્રો સાથે."),
                  ("Trickle bed: fixed bed of catalyst pellets, with gas and liquid both flowing down.",
                   "Trickle bed: catalyst pellets નો fixed bed, gas અને પ્રવાહી બંને નીચે વહે."),
                  ("Trickle bed: support grid, gas outlet at the bottom and liquid draw-off, so the "
                   "catalyst stays wetted and in place.", "Trickle bed: support grid, તળિયે gas outlet "
                   "અને liquid draw-off, જેથી catalyst ભીનો અને જગ્યાએ રહે.")),
            working(("Spray tower: liquid is pumped to the nozzle and falls as a spray against the "
                     "rising gas.", "Spray tower: પ્રવાહી nozzle સુધી pump થાય અને ચઢતા gas સામે "
                     "spray તરીકે પડે."),
                    ("Spray tower: the gas is absorbed into the drops; the liquid is collected at the "
                     "bottom and recycled.", "Spray tower: gas ટીપાંમાં શોષાય; પ્રવાહી તળિયે ભેગું થાય "
                     "અને ફરી વપરાય."),
                    ("Trickle bed: liquid trickles down as a thin film over the pellets while gas "
                     "flows down (or up) through the same voids.", "Trickle bed: પ્રવાહી pellets પર "
                     "પાતળા પડ તરીકે નીચે ટપકે જ્યારે gas એ જ voids માંથી નીચે (કે ઉપર) વહે."),
                    ("Trickle bed: the reaction happens on the wetted catalyst, so the liquid film "
                     "thickness controls the rate.", "Trickle bed: પ્રક્રિયા ભીની catalyst પર થાય, "
                     "તેથી પ્રવાહી પડની જાડાઈ rate નક્કી કરે."),
                    ("Both: pressure drop and maldistribution are the practical limits, and a "
                     "distributor that wets the whole cross-section is essential.",
                     "બંને: pressure drop અને ખરાબ distribution વ્યવહારની મર્યાદા છે, અને આખું "
                     "cross-section ભીનું કરતો distributor જરૂરી છે.")),
            table([tr("Reactor", "Reactor"), tr("Contact", "સંપર્ક"), tr("Best for", "કોના માટે સારું")],
                  [[tr("Spray tower", "Spray tower"),
                    tr("drops falling through gas", "gas માંથી પડતાં ટીપાં"),
                    tr("absorption, gas cooling, fast gas-liquid reactions",
                       "absorption, gas ઠંડું કરવું, ઝડપી gas-liquid પ્રક્રિયા")],
                   [tr("Trickle bed", "Trickle bed"),
                    tr("liquid film on a fixed catalyst", "સ્થિર catalyst પર પ્રવાહી પડ"),
                    tr("hydrotreating, hydrogenation, slow three-phase reactions",
                       "hydrotreating, hydrogenation, ધીમી three-phase પ્રક્રિયા")],
                   [tr("Slurry", "Slurry"), tr("bubbles in a stirred slurry", "હલાવેલા slurry માં "
                                              "bubbles"),
                    tr("fine catalyst, uniform temperature", "બારીક catalyst, સરખું temperature")],
                   [tr("Bubble column", "Bubble column"), tr("bubbles in a liquid", "પ્રવાહીમાં bubbles"),
                    tr("large volumes, no maintenance", "મોટા volumes, જાળવણી વગર")]]),
            math("area per unit volume: a = 6 eps_g/d_b   for bubbles,   6 eps_d/d_p   for drops",
                 "contact time: hold-up / flow, so a tall column buys time and a spray buys area"),
            why("The four multiphase reactors differ only in which phase is dispersed: drops, bubbles "
                "or a film. Once that choice is made, the area per unit volume and the residence "
                "time follow, and with them the size of the vessel.",
                "ચાર multiphase reactors માં ફરક ફક્ત એટલો છે કે કયો phase વેરાય છે: ટીપાં, bubbles કે "
                "પડ. એ પસંદગી થાય પછી પ્રતિ volume area અને residence time મળે, અને તેમની સાથે પાત્રનું "
                "size."),
            check("A spray tower has a large area but a tiny liquid hold-up, so it suits fast "
                  "absorption; a trickle bed has a large area and a long contact time, so it suits "
                  "slow reactions.",
                  "Spray tower માં મોટું area પણ ખૂબ ઓછું liquid hold-up છે, તેથી ઝડપી absorption માટે "
                  "યોગ્ય; trickle bed માં મોટું area અને લાંબો contact time છે, તેથી ધીમી પ્રક્રિયા "
                  "માટે."),
            pit("Choosing a trickle bed for a reaction that produces a solid. The packing blinds, the "
                "pressure drop climbs and the run ends in a shutdown.",
                "ઘન પદાર્થ બનાવતી પ્રક્રિયા માટે trickle bed પસંદ કરવો. Packing બંધાય, pressure drop "
                "વધે અને રન shutdown પર પૂરો થાય."),
            diagram="u4_spray",
            syllabus_item="4.3",
        ),
    ],
})

# ---------------------------------------------------------------- equations
EQUATIONS = [
    {"title": tr("Ideal models", "આદર્શ models"),
     "items": [
         {"name": tr("Batch", "Batch"),
          "f": "t = NA0 x integral dX/(-rA V)",
          "terms": tr("No flow term: the batch equation is a function of time alone.",
                      "કોઈ flow ભાગ નહીં: batch equation ફક્ત સમયનું વિધેય છે.")},
         {"name": tr("CSTR", "CSTR"),
          "f": "V = FA0 X / (-rA)",
          "terms": tr("One algebraic line, evaluated at the exit condition.",
                      "એક બીજગણિતીય લીટી, exit શરત પર ગણાય.")},
         {"name": tr("PFR", "PFR"),
          "f": "V = FA0 x integral dX/(-rA)",
          "terms": tr("An integral along the tube, from inlet to outlet.",
                      "નળીની લંબાઈ પર integral, inlet થી outlet સુધી.")},
     ]},
    {"title": tr("Space time", "Space time"),
     "items": [
         {"name": tr("Space time", "Space time"),
          "f": "tau = V/v0 = CA0 X/(-rA)",
          "terms": tr("The time a volume element would spend inside at inlet conditions.",
                      "Inlet શરતો પર volume element અંદર ગાળે તે સમય.")},
         {"name": tr("First order duty", "First order કામ"),
          "f": "CSTR: k tau = X/(1-X);   PFR: k tau = ln[1/(1-X)]",
          "terms": tr("The comparison that decides which reactor to buy.",
                      "કયો reactor લેવો તે નક્કી કરતી સરખામણી.")},
         {"name": tr("Space velocity", "Space velocity"),
          "f": "SV = 1/tau = v0/V",
          "terms": tr("The reciprocal of space time, quoted in h-1: how many reactor volumes of "
                      "feed pass per hour.", "Space time નો વ્યસ્ત, h-1 માં: કલાક દીઠ કેટલા reactor "
                      "volumes feed પસાર થાય.")},
         {"name": tr("CSTRs in series", "Series માં CSTR"),
          "f": "1 - X = 1/(1 + k tau)^n   for n equal tanks",
          "terms": tr("A train of tanks approaches plug flow as n grows.",
                      "Tanks ની શ્રેણી n વધે તેમ plug flow ની નજીક જાય.")},
     ]},
    {"title": tr("Packed beds", "Packed beds"),
     "items": [
         {"name": tr("Catalyst basis", "Catalyst આધાર"),
          "f": "W = FA0 x integral dX/(-rA')",
          "terms": tr("The PFR equation with mass of catalyst in place of volume.",
                      "Volume ની જગ્યાએ catalyst ના દળ સાથેનું PFR equation.")},
         {"name": tr("Space velocity", "Space velocity"),
          "f": "WHSV = feed mass per hour / catalyst mass",
          "terms": tr("The reciprocal of a space time measured in kilograms.",
                      "કિલોગ્રામમાં માપેલા space time નો વ્યસ્ત.")},
         {"name": tr("Void fraction", "Void fraction"),
          "f": "V_bed = W / [rho_p (1 - eps)]",
          "terms": tr("Only the voids carry gas, so eps sets the residence time.",
                      "ફક્ત voids gas ધરાવે, તેથી eps residence time નક્કી કરે.")},
         {"name": tr("Ergun pressure drop", "Ergun pressure drop"),
          "f": "dP/L = 150 mu u (1-eps)^2/(eps^3 dp^2) + 1.75 rho u^2 (1-eps)/(eps^3 dp)",
          "terms": tr("Viscous term first, inertial term second.",
                      "પહેલા viscous ભાગ, પછી inertial ભાગ.")},
     ]},
    {"title": tr("Fluidisation", "Fluidisation"),
     "items": [
         {"name": tr("Minimum fluidisation", "ન્યૂનતમ fluidisation velocity"),
          "f": "Umf = dp^2 (rho_p - rho_g) g / (1650 mu)",
          "terms": tr("Valid for small particles; the bed lifts above this velocity.",
                      "નાના particles માટે માન્ય; આ velocity ઉપર bed ઊંચકાય.")},
         {"name": tr("Bed expansion", "Bed expansion"),
          "f": "H/H_mf = (1 - eps_mf)/(1 - eps)",
          "terms": tr("The same mass of solids in a taller, more open bed.",
                      "એ જ ઘન દળ વધુ ઊંચા અને વધુ ખુલ્લા bed માં.")},
         {"name": tr("Solids hold-up", "Solids hold-up"),
          "f": "W = rho_p A H (1 - eps)",
          "terms": tr("Fixes the bed height for a given charge of catalyst.",
                      "આપેલા catalyst ચાર્જ માટે bed ની ઊંચાઈ નક્કી કરે.")},
     ]},
    {"title": tr("Multiphase contact", "Multiphase સંપર્ક"),
     "items": [
         {"name": tr("Resistances in series", "Series માં resistances"),
          "f": "1/K = 1/(kG a) + 1/(kL a H) + 1/(k' a H)",
          "terms": tr("The slowest of gas film, liquid film and reaction controls.",
                      "Gas film, liquid film અને પ્રક્રિયા પૈકી સૌથી ધીમું નિયંત્રણ કરે.")},
         {"name": tr("Mass transfer limited", "Mass transfer મર્યાદિત"),
          "f": "rate = kL a (CA* - CA)",
          "terms": tr("Doubling kL a doubles the rate - the test for a diffusion-limited reaction.",
                      "kL a બમણું કરતાં rate બમણો - diffusion-limited પ્રક્રિયાની ચકાસણી.")},
         {"name": tr("Gas hold-up", "Gas hold-up"),
          "f": "eps_g = V_gas / V_total;   liquid residence time = V(1 - eps_g)/vL",
          "terms": tr("Bubbles occupy volume, so the liquid leaves sooner than V/vL.",
                      "Bubbles volume રોકે, તેથી પ્રવાહી V/vL કરતાં વહેલું નીકળે.")},
         {"name": tr("Film thickness", "પડની જાડાઈ"),
          "f": "rate_trickle ~ kL a (CA* - CA) with a from the wetted packing area",
          "terms": tr("A dry patch has no area: wetting the whole bed is the design aim.",
                      "સૂકો ભાગ area આપતો નથી: આખો bed ભીનો કરવો એ design નો ધ્યેય છે.")},
     ]},
]

# ---------------------------------------------------------------- viva
VIVA = [
    {"title": tr("Ideal and real reactors", "આદર્શ અને સાચા reactors"),
     "items": [
         {"q": tr("Why does a CSTR need a larger volume than a PFR for the same conversion?",
                  "એ જ conversion માટે CSTR ને PFR કરતાં મોટું volume કેમ જોઈએ?"),
          "a": tr("Because it always works at the outlet concentration, which is the lowest in the "
                  "system, so the rate is at its lowest for the whole residence time. A PFR starts "
                  "at the inlet concentration and its rate is high where the concentration is high, "
                  "so the same conversion needs less volume.",
                  "કારણ કે તે હંમેશા outlet concentration પર કામ કરે, જે system માં સૌથી નીચું છે, "
                  "તેથી આખા residence time દરમિયાન rate સૌથી નીચો રહે. PFR inlet concentration પર "
                  "શરૂ થાય અને જ્યાં concentration ઊંચું ત્યાં rate ઊંચો, તેથી એ જ conversion ને ઓછું "
                  "volume જોઈએ.")},
         {"q": tr("What would you measure to prove a reactor is not ideal?",
                  "Reactor આદર્શ નથી તે સાબિત કરવા શું માપશો?"),
          "a": tr("A tracer response: inject a pulse and record the exit concentration. A perfect "
                  "CSTR gives one exponential decay, a perfect PFR gives a single delayed spike, and "
                  "a real reactor gives a curve in between, with a tail that shows dead volume or "
                  "bypassing.",
                  "Tracer response: pulse નાખો અને exit concentration નોંધો. સંપૂર્ણ CSTR એક "
                  "exponential decay આપે, સંપૂર્ણ PFR એક જ વિલંબિત spike આપે, અને સાચો reactor વચ્ચેનો "
                  "વક્ર આપે, જેની પૂંછડી dead volume કે bypassing દર્શાવે.")},
         {"q": tr("Why is a batch reactor preferred in a pharmaceutical plant?",
                  "Pharmaceutical plant માં batch reactor કેમ પસંદ થાય?"),
          "a": tr("Because many different products are made in the same vessel, each with its own "
                  "recipe, and the batch record gives complete traceability for every lot - which a "
                  "continuous unit cannot offer without a great deal of extra work.",
                  "કારણ કે એક જ પાત્રમાં ઘણા જુદા products બને, દરેકની પોતાની recipe હોય, અને batch "
                  "record દરેક લોટની સંપૂર્ણ traceability આપે - જે continuous unit ઘણા વધારાના કામ "
                  "વગર આપી શકતું નથી.")},
     ]},
    {"title": tr("CSTR and PFR in practice", "વ્યવહારમાં CSTR અને PFR"),
     "items": [
         {"q": tr("Why are several CSTRs often put in series?", "ઘણી વાર ઘણા CSTR series માં કેમ મૂકાય?"),
          "a": tr("A train of equal tanks behaves more and more like a PFR as the number grows, so "
                  "the total volume for a given conversion falls sharply - two tanks already halve "
                  "the volume needed for 90 % conversion at first order - while each tank stays "
                  "simple and easy to control.",
                  "સરખા tanks ની શ્રેણી સંખ્યા વધે તેમ plug flow જેવી વર્તે, તેથી આપેલા conversion માટે "
                  "કુલ volume ઝડપથી ઘટે - first order માં 90 % માટે બે tanks પહેલેથી અડધું volume કરે - "
                  "જ્યારે દરેક tank સાદું અને નિયંત્રણમાં સહેલું રહે.")},
         {"q": tr("What breaks plug flow in a tube?", "નળીમાં plug flow શું તોડે?"),
          "a": tr("Axial dispersion, a laminar velocity profile, natural convection, and too short a "
                  "tube for its diameter. All of them let fluid of different ages mix, so the "
                  "residence times spread out and the reactor drifts towards CSTR behaviour.",
                  "Axial dispersion, laminar velocity profile, natural convection, અને વ્યાસ કરતાં "
                  "ખૂબ ટૂંકી નળી. તે બધા જુદી ઉંમરનું પ્રવાહી ભેળવે, તેથી residence times ફેલાય અને "
                  "reactor CSTR વર્તન તરફ જાય.")},
         {"q": tr("When would you deliberately choose a CSTR for a reaction that needs a big volume?",
                  "મોટું volume જોઈએ તેવી પ્રક્રિયા માટે ક્યારે જાણી જોઈને CSTR પસંદ કરશો?"),
          "a": tr("For an autocatalytic or a strongly exothermic reaction, or one that must be held "
                  "at a low concentration to avoid a side product. In those cases a low concentration "
                  "is an advantage, not a penalty, and the excellent temperature control matters more "
                  "than the volume.",
                  "Autocatalytic કે તીવ્ર exothermic પ્રક્રિયા માટે, અથવા જે side product ટાળવા નીચા "
                  "concentration પર રાખવી પડે તેના માટે. તે કિસ્સામાં નીચું concentration ગેરફાયદો નહીં "
                  "પણ ફાયદો છે, અને ઉત્તમ temperature control volume કરતાં વધુ મહત્ત્વનું છે.")},
     ]},
    {"title": tr("Packed and fluidised beds", "Packed અને fluidised beds"),
     "items": [
         {"q": tr("Why does a fixed bed suffer hot spots but a fluidised bed does not?",
                  "Fixed bed માં hot spots કેમ થાય પણ fluidised bed માં નહીં?"),
          "a": tr("In a fixed bed the gas moves in channels and the solid cannot move, so heat "
                  "released locally can only leave by conduction through the pellets - slowly. In a "
                  "fluidised bed the solids circulate violently, so any hot particle is carried into "
                  "the cooler bulk within seconds and the bed is isothermal.",
                  "Fixed bed માં gas channels માં ચાલે અને ઘન હલી શકે નહીં, તેથી સ્થાનિક રીતે છૂટેલી heat "
                  "ફક્ત pellets દ્વારા conduction થી જ નીકળે - ધીમે. Fluidised bed માં ઘન જોરદાર "
                  "રીતે ફરે, તેથી ગરમ particle સેકન્ડોમાં ઠંડા જથ્થામાં આવી જાય અને bed isothermal રહે.")},
         {"q": tr("Why is a cyclone compulsory on a fluidised bed?", "Fluidised bed પર cyclone કેમ "
                  "ફરજિયાત છે?"),
          "a": tr("Because the gas leaving the bed always entrains fine catalyst. Without a cyclone "
                  "and a dipleg to return it, the inventory is carried out of the reactor within days "
                  "and both the conversion and the catalyst bill collapse.",
                  "કારણ કે bed માંથી નીકળતો gas હંમેશા બારીક catalyst ઉપાડી જાય. પાછો મોકલતો cyclone "
                  "અને dipleg ન હોય તો inventory દિવસોમાં reactor ની બહાર જાય અને conversion તથા "
                  "catalyst નો ખર્ચ બંને બગડે.")},
         {"q": tr("What does WHSV mean, and why is it used instead of space time?",
                  "WHSV નો અર્થ શું, અને space time ને બદલે તે કેમ વપરાય?"),
          "a": tr("Weight hourly space velocity is the mass of feed per hour divided by the mass of "
                  "catalyst. Catalyst is bought and loaded by weight and its activity is quoted per "
                  "kilogram, so WHSV is the natural variable for a solid-catalysed reactor, just as "
                  "space time is natural for a homogeneous one.",
                  "Weight hourly space velocity એ કલાક દીઠ feed નું દળ ભાગ્યું catalyst ના દળ. Catalyst "
                  "વજનથી ખરીદાય અને ભરાય, અને તેની activity પ્રતિ કિલોગ્રામ લખાય, તેથી ઘન-ઉત્પ્રેરિત "
                  "reactor માટે WHSV સ્વાભાવિક ચલ છે, જેમ homogeneous માટે space time.")},
     ]},
    {"title": tr("Multiphase reactors", "Multiphase reactors"),
     "items": [
         {"q": tr("Which phase is dispersed in a bubble column, and which in a spray tower?",
                  "Bubble column માં કયો phase વેરાય છે, અને spray tower માં કયો?"),
          "a": tr("In a bubble column the gas is dispersed as bubbles in a continuous liquid; in a "
                  "spray tower the liquid is dispersed as drops in a continuous gas. The choice "
                  "decides the hold-up, the interfacial area and therefore the size of the vessel.",
                  "Bubble column માં gas સતત પ્રવાહીમાં bubbles તરીકે વેરાય; spray tower માં પ્રવાહી "
                  "સતત gas માં ટીપાં તરીકે વેરાય. આ પસંદગી hold-up, interfacial area અને તેથી પાત્રનું "
                  "size નક્કી કરે.")},
         {"q": tr("How do you know that a three-phase reaction is limited by mass transfer?",
                  "Three-phase પ્રક્રિયા mass transfer થી મર્યાદિત છે તે કેમ ખબર પડે?"),
          "a": tr("Increase the stirring or the gas rate: if the rate rises, mass transfer was "
                  "controlling; if it does not move, the kinetics were. The other test is temperature "
                  "- a mass-transfer-limited reaction is nearly insensitive to it.",
                  "Stirring કે gas rate વધારો: rate વધે તો mass transfer નિયંત્રણ કરતું હતું; ન બદલાય તો "
                  "kinetics. બીજી ચકાસણી temperature છે - mass-transfer-limited પ્રક્રિયા તેના પર "
                  "લગભગ સંવેદનશીલ નથી.")},
         {"q": tr("Why is a trickle bed preferred for hydrotreating?",
                  "Hydrotreating માટે trickle bed કેમ પસંદ થાય?"),
          "a": tr("Because the reaction is slow and needs a large amount of catalyst held in place at "
                  "high pressure, with both gas and liquid passing continuously. A slurry would need "
                  "a catalyst separation step at pressure, which is far more expensive.",
                  "કારણ કે પ્રક્રિયા ધીમી છે અને ઊંચા pressure પર જગ્યાએ પકડેલો મોટો catalyst જથ્થો "
                  "જોઈએ, જ્યાં gas અને પ્રવાહી બંને સતત પસાર થાય. Slurry માં pressure પર જ catalyst "
                  "અલગ કરવાનું પગલું જોઈએ, જે ઘણું ખર્ચાળ છે.")},
     ]},
]

# ---------------------------------------------------------------- solved numericals
_PRACTICE = [
    ("Batch time and daily production",
     "Batch time અને રોજનું ઉત્પાદન",
     "A 1.0 m3 batch reactor is charged with CA0 = 2.0 kmol/m3 of A. The reaction is first order "
     "with k = 0.020 min-1 and is run to 95 % conversion. Find the reaction time, the cycle time "
     "with 30 min of filling, heating and emptying, and the daily production of A reacted.",
     "1.0 m3 ના batch reactor માં CA0 = 2.0 kmol/m3 A ભરાય છે. પ્રક્રિયા first order છે, "
     "k = 0.020 min-1, અને 95 % conversion સુધી ચલાવાય છે. Reaction time, ભરવા-ગરમ કરવા-ખાલી કરવાના "
     "30 min સાથે cycle time, અને રોજ પ્રક્રિયા થતા A નું ઉત્પાદન શોધો.",
     [h4("Step 1 - the reaction time", "પગલું 1 - reaction time"),
      math("t = (1/k) ln[1/(1 - X)] = (1/0.020) ln(1/0.05)",
           "  = 50 x 2.996 = 149.8 min"),
      h4("Step 2 - the cycle", "પગલું 2 - cycle"),
      math("cycle = 149.8 + 30 = 179.8 min, so 1440/179.8 = 8 batches a day"),
      h4("Step 3 - production", "પગલું 3 - ઉત્પાદન"),
      math("A charged per batch = CA0 V = 2.0 x 1.0 = 2.0 kmol",
           "A reacted per batch = 0.95 x 2.0 = 1.90 kmol",
           "per day = 8 x 1.90 = 15.2 kmol"),
      eq("t = 150 min,  8 batches/day,  15.2 kmol of A reacted per day"),
      p("The reactor is only producing for 150 min out of every 180, which is the real cost of a "
        "batch plant: about one sixth of the day is filling, heating and emptying.",
        "180 માંથી ફક્ત 150 min reactor ઉત્પાદન કરે છે, જે batch plant ની ખરી કિંમત છે: દિવસનો "
        "લગભગ છઠ્ઠો ભાગ ભરવા, ગરમ કરવા અને ખાલી કરવામાં જાય."),
      check("exp(-0.020 x 149.8) = exp(-3.00) = 0.050, so 5 % of A is left.",
            "exp(-0.020 x 149.8) = exp(-3.00) = 0.050, તેથી 5 % A બાકી."),
      pit("Quoting the reactor volume without the freeboard. A vessel is never filled more than "
          "70-80 % full, so a 1.0 m3 charge needs a 1.3 m3 vessel.",
          "Freeboard વગર reactor નું volume લખવું. પાત્ર 70-80 % થી વધુ ભરાતું નથી, તેથી 1.0 m3 "
          "ચાર્જ માટે 1.3 m3 પાત્ર જોઈએ.")],
     6),
    ("CSTR volume for a first order reaction",
     "First order પ્રક્રિયા માટે CSTR નું volume",
     "A first order reaction with k = 0.25 h-1 must be carried out to 80 % conversion in a CSTR. The "
     "feed rate is 7.2 m3/h. Find the space time and the reactor volume.",
     "k = 0.25 h-1 વાળી first order પ્રક્રિયા CSTR માં 80 % conversion સુધી કરવી છે. Feed rate "
     "7.2 m3/h છે. Space time અને reactor નું volume શોધો.",
     [h4("Step 1 - the space time", "પગલું 1 - space time"),
      math("tau = X/[k(1 - X)] = 0.80/(0.25 x 0.20)",
           "    = 0.80/0.050 = 16 h"),
      h4("Step 2 - the volume", "પગલું 2 - volume"),
      math("tau = V/v0  ->  V = v0 tau = 7.2 x 16 = 115.2 m3"),
      eq("tau = 16 h,  V = 115 m3"),
      h4("Step 3 - what a PFR would need", "પગલું 3 - PFR ને કેટલું જોઈએ"),
      math("tau_PFR = ln[1/(1 - X)]/k = ln(5)/0.25 = 1.609/0.25 = 6.44 h",
           "V_PFR = 7.2 x 6.44 = 46.4 m3"),
      p("The CSTR needs 2.5 times the volume of a PFR for the same job at 80 % conversion. The ratio "
        "grows with conversion: at 95 % it would be 3.8, at 99 % about 5.",
        "80 % conversion પર એ જ કામ માટે CSTR ને PFR કરતાં 2.5 ગણું volume જોઈએ. ગુણોત્તર conversion "
        "સાથે વધે: 95 % પર 3.8, 99 % પર લગભગ 5."),
      check("Put the numbers back: -rA at the exit = k CA0(1-X) = 0.25 x CA0 x 0.2 = 0.05 CA0, and "
            "V = v0 CA0 X/(-rA) = 7.2 CA0 x 0.8/(0.05 CA0) = 115 m3.",
            "આંકડા પાછા મૂકો: exit પર -rA = k CA0(1-X) = 0.25 x CA0 x 0.2 = 0.05 CA0, અને "
            "V = v0 CA0 X/(-rA) = 7.2 CA0 x 0.8/(0.05 CA0) = 115 m3."),
      pit("Using the batch time in place of the space time. For a CSTR the space time is the volume "
          "divided by the feed rate; it equals the batch time only in the limit of zero conversion.",
          "Space time ની જગ્યાએ batch time વાપરવો. CSTR માટે space time એ volume ભાગ્યું feed rate છે; "
          "તે batch time સાથે ફક્ત શૂન્ય conversion ની મર્યાદામાં સરખો થાય.")],
     7),
    ("Two CSTRs in series against one",
     "એક CSTR સામે series માં બે CSTR",
     "The same feed (v0 = 7.2 m3/h, k = 0.25 h-1, X = 0.80) is now to be treated in two equal CSTRs "
     "in series. Find the volume of each and compare the total with the single tank of the previous "
     "problem.",
     "એ જ feed (v0 = 7.2 m3/h, k = 0.25 h-1, X = 0.80) હવે series માં બે સરખા CSTR માં લેવાની છે. દરેકનું "
     "volume શોધો અને કુલ volume ને પાછલા દાખલાની એક tank સાથે સરખાવો.",
     [h4("Step 1 - the relation for n equal tanks", "પગલું 1 - n સરખા tanks માટેનો સંબંધ"),
      math("1 - X = 1/(1 + k tau)^n",
           "0.20 = 1/(1 + k tau)^2  ->  1 + k tau = 2.236",
           "k tau = 1.236  ->  tau = 1.236/0.25 = 4.94 h"),
      h4("Step 2 - the volume of each tank", "પગલું 2 - દરેક tank નું volume"),
      math("V1 = V2 = v0 tau = 7.2 x 4.94 = 35.6 m3",
           "total = 71.2 m3"),
      eq("each tank 36 m3, total 71 m3 against 115 m3 for one tank"),
      p("Two tanks in series save 44 m3 for the same duty, and the first tank does most of the work: "
        "it takes the feed to about 55 % conversion at a high rate, and the second finishes the job at "
        "a lower rate but a much lower concentration.",
        "Series માં બે tanks એ જ કામ માટે 44 m3 બચાવે, અને પહેલી tank વધુ કામ કરે: તે feed ને ઊંચા rate "
        "પર લગભગ 55 % conversion સુધી લઈ જાય, અને બીજી ઓછા rate પણ ઘણા નીચા concentration પર કામ પૂરું "
        "કરે."),
      check("Stage 1: X1 = k tau/(1 + k tau) = 1.236/2.236 = 0.553; stage 2 gives X2 = 0.553 + "
            "(1-0.553)(0.553) = 0.800. The two stages reach the target.",
            "તબક્કો 1: X1 = k tau/(1 + k tau) = 1.236/2.236 = 0.553; તબક્કો 2 આપે X2 = 0.553 + "
            "(1-0.553)(0.553) = 0.800. બંને તબક્કા લક્ષ્ય સુધી પહોંચે."),
      pit("Splitting an existing tank into two halves and expecting the same conversion. Two tanks "
          "of 57.6 m3 each are far more than 71 m3 and would give a higher conversion, while two "
          "tanks of 35.6 m3 are the size that reproduces the duty - the volumes must be recomputed, "
          "never halved.",
          "હાલની tank ને બે ભાગમાં વહેંચીને એ જ conversionની અપેક્ષા રાખવી. દરેક 57.6 m3 હોય તો કુલ "
          "71 m3 કરતાં ઘણું વધારે થાય અને conversion ઊંચું આવે, જ્યારે કામ પાર પાડવા દરેક 35.6 m3 "
          "જોઈએ - volumes ફરી ગણવા પડે, અડધા નહીં કરવા.")],
     8),
    ("PFR volume and space time",
     "PFR નું volume અને space time",
     "A gas reaction follows first order kinetics with k = 0.50 h-1 and is to reach 90 % conversion "
     "at a feed rate of 10 m3/h. Find the PFR volume, the space time, and the volume a single CSTR "
     "would need for the same duty.",
     "Gas પ્રક્રિયા k = 0.50 h-1 સાથે first order છે અને 10 m3/h feed rate પર 90 % conversion સુધી "
     "લઈ જવી છે. PFR નું volume, space time, અને એ જ કામ માટે એક CSTR ને લાગતું volume શોધો.",
     [h4("Step 1 - the PFR space time", "પગલું 1 - PFR નું space time"),
      math("tau = ln[1/(1 - X)]/k = ln(10)/0.50 = 2.303/0.50 = 4.61 h"),
      h4("Step 2 - the volume", "પગલું 2 - volume"),
      math("V = v0 tau = 10 x 4.61 = 46.1 m3"),
      h4("Step 3 - the CSTR comparison", "પગલું 3 - CSTR સાથે સરખામણી"),
      math("tau_CSTR = X/[k(1 - X)] = 0.90/(0.50 x 0.10) = 18 h",
           "V_CSTR = 10 x 18 = 180 m3"),
      eq("PFR: tau = 4.61 h, V = 46 m3;  CSTR: 180 m3 - 3.9 times more"),
      p("This ratio of 3.9 at 90 % conversion is the standard number to quote when someone asks why "
        "tubular reactors are used for high conversion duties.",
        "90 % conversion પર 3.9 નો આ ગુણોત્તર એ પ્રમાણભૂત આંકડો છે જે કોઈ પૂછે કે ઊંચા conversion ના કામ "
        "માટે tubular reactors કેમ વપરાય."),
      check("PFR: CA/CA0 = exp(-k tau) = exp(-2.303) = 0.100, so conversion is 90 %.",
            "PFR: CA/CA0 = exp(-k tau) = exp(-2.303) = 0.100, તેથી conversion 90 %."),
      pit("Forgetting that a PFR's volume is not the volume of the pipe fittings. The design volume "
          "is the tube volume; heads, bends and the jacket add steel but not residence time.",
          "PFR નું volume pipe fittings નું volume નથી તે ભૂલવું. Design volume નળીનું volume છે; heads, "
          "bends અને jacket steel ઉમેરે પણ residence time નહીં.")],
     7),
    ("Fixed bed: WHSV, bed volume and pressure drop",
     "Fixed bed: WHSV, bed volume અને pressure drop",
     "A fixed bed reactor treats 500 kg/h of gas over 250 kg of catalyst of bulk density 600 kg/m3 "
     "and particle density 1100 kg/m3. The bed is in a tube of 0.60 m inside diameter. Find the "
     "space velocity, the bed volume, the bed height and the void fraction.",
     "Fixed bed reactor 500 kg/h gas ને 250 kg catalyst પર પ્રક્રિયા કરાવે છે, જેની bulk density "
     "600 kg/m3 અને particle density 1100 kg/m3 છે. Bed 0.60 m આંતરિક વ્યાસની નળીમાં છે. Space "
     "velocity, bed volume, bed height અને void fraction શોધો.",
     [h4("Step 1 - space velocity", "પગલું 1 - space velocity"),
      math("WHSV = feed/catalyst = 500/250 = 2.0 h-1"),
      h4("Step 2 - bed volume", "પગલું 2 - bed volume"),
      math("V_bed = W/rho_b = 250/600 = 0.417 m3"),
      h4("Step 3 - bed height", "પગલું 3 - bed height"),
      math("A = pi D^2/4 = 3.142 x 0.36/4 = 0.2827 m2",
           "H = V_bed/A = 0.417/0.2827 = 1.48 m"),
      h4("Step 4 - void fraction", "પગલું 4 - void fraction"),
      math("rho_b = rho_p (1 - eps)  ->  1 - eps = 600/1100 = 0.545",
           "eps = 0.455"),
      eq("WHSV = 2.0 h-1,  V_bed = 0.42 m3,  H = 1.48 m,  eps = 0.46"),
      p("A void fraction of 0.46 is typical for 3-5 mm pellets. Only that 46 % of the bed carries "
        "gas, so the actual gas velocity is 1/(1-eps) = 1.8 times the superficial velocity - and the "
        "pressure drop follows the Ergun equation with that velocity.",
        "3-5 mm pellets માટે 0.46 નું void fraction સામાન્ય છે. Bed ના ફક્ત એ 46 % ભાગમાં gas જાય, "
        "તેથી ખરી gas velocity superficial velocity કરતાં 1/(1-eps) = 1.8 ગણી છે - અને pressure drop "
        "એ velocity સાથે Ergun equation પ્રમાણે થાય."),
      check("Mass of solids from the height: rho_p A H (1-eps) = 1100 x 0.2827 x 1.48 x 0.545 = "
            "250 kg, the charge given.",
            "ઊંચાઈ પરથી ઘનનું દળ: rho_p A H (1-eps) = 1100 x 0.2827 x 1.48 x 0.545 = 250 kg, જે "
            "આપેલો ચાર્જ છે."),
      pit("Using the empty-tube velocity in the Ergun equation. The equation already contains "
          "(1-eps) and eps^3, but the velocity in it is the superficial one - mixing the two is the "
          "usual mistake.",
          "Ergun equation માં ખાલી નળીની velocity વાપરવી. Equation માં (1-eps) અને eps^3 પહેલેથી છે, "
          "પણ તેમાં velocity superficial છે - બંને ભેળવવી સામાન્ય ભૂલ છે.")],
     6),
    ("Fluidised bed: minimum fluidisation and bed height",
     "Fluidised bed: minimum fluidisation અને bed height",
     "A powder of dp = 100 micron and rho_p = 2500 kg/m3 is to be fluidised by a gas of density "
     "1.2 kg/m3 and viscosity 1.8e-5 Pa s in a bed of 0.30 m diameter carrying 40 kg of solids. "
     "Find Umf, the bed height at eps = 0.45, and say whether an operating velocity of 0.05 m/s "
     "fluidises the bed.",
     "dp = 100 micron અને rho_p = 2500 kg/m3 વાળો પાવડર 1.2 kg/m3 density અને 1.8e-5 Pa s viscosity "
     "વાળા gas થી 0.30 m વ્યાસના bed માં fluidise કરવો છે, જેમાં 40 kg ઘન છે. Umf, eps = 0.45 પર bed "
     "ની ઊંચાઈ શોધો, અને 0.05 m/s ની operating velocity bed ને fluidise કરશે કે નહીં કહો.",
     [h4("Step 1 - minimum fluidisation velocity", "પગલું 1 - minimum fluidisation velocity"),
      math("Umf = dp^2 (rho_p - rho_g) g/(1650 mu)",
           "    = (1.0e-4)^2 x (2500 - 1.2) x 9.81/(1650 x 1.8e-5)",
           "    = 1.0e-8 x 24513/0.0297 = 8.25e-3 m/s"),
      h4("Step 2 - the bed height", "પગલું 2 - bed ની ઊંચાઈ"),
      math("A = pi D^2/4 = 3.142 x 0.09/4 = 0.0707 m2",
           "W = rho_p A H (1 - eps)  ->  H = 40/(2500 x 0.0707 x 0.55)",
           "   = 40/97.2 = 0.412 m"),
      h4("Step 3 - is 0.05 m/s enough?", "પગલું 3 - 0.05 m/s પૂરતું છે?"),
      math("U/Umf = 0.050/0.00825 = 6.1"),
      eq("Umf = 8.3 mm/s,  H = 0.41 m,  U/Umf = 6.1 so the bed is vigorously bubbling"),
      p("Six times the minimum fluidisation velocity is the normal operating range of a bubbling "
        "bed: enough to keep the particles moving, not so much that the catalyst is carried out "
        "faster than the cyclone can return it.",
        "Minimum fluidisation velocity કરતાં છ ગણી એ bubbling bed ની સામાન્ય કાર્યશ્રેણી છે: particles "
        "હલતા રહે તેટલું, પણ cyclone પાછું લાવી શકે તેનાથી વધુ ઝડપથી catalyst ન ઊડે તેટલું."),
      check("At eps = 0.45 the bed holds 2500 x 0.0707 x 0.412 x 0.55 = 40.0 kg, the charge given.",
            "eps = 0.45 પર bed માં 2500 x 0.0707 x 0.412 x 0.55 = 40.0 kg રહે, જે આપેલો ચાર્જ છે."),
      pit("Applying the small-particle formula to coarse sand. Above about 500 micron the inertial "
          "term of the Ergun equation dominates and the simple Umf formula under-predicts by a wide "
          "margin.",
          "બારીક સૂત્ર જાડી રેતી પર વાપરવું. લગભગ 500 micron ઉપર Ergun equation નો inertial ભાગ પ્રભાવી "
          "થાય અને સાદું Umf સૂત્ર ઘણું ઓછું આંકે.")],
     7),
]

PRACTICE = [(tr(h_en, h_gu), tr(q_en, q_gu), body(*parts_), m)
            for (h_en, h_gu, q_en, q_gu, parts_, m) in _PRACTICE]

EXAM = [{"q": q, "marks": m} for _, q, _, m in PRACTICE]
PRACTICE_ANSWERS = [a for _, _, a, _ in PRACTICE]

SOURCES = [
    ("GTU DI05005031 Chemical Reaction Engineering syllabus (uploaded PDF, w.e.f. 2026-27)",
     "https://syllabus.gtu.ac.in/"),
    ("Octave Levenspiel - Chemical Reaction Engineering, 3rd ed., Wiley (chapter 5: ideal reactors "
     "for a single reaction; chapter 6: design for single reactions)",
     "https://www.wiley.com/"),
    ("H. Scott Fogler - Essentials of Chemical Reaction Engineering, 4th ed., Prentice Hall "
     "(chapters 2, 4, 8 and 10: conversion, CSTR and PFR design, fluidised beds)",
     "https://www.pearson.com/"),
    ("Kunii and Levenspiel - Fluidization Engineering, 2nd ed., Butterworth-Heinemann "
     "(distributors, bubbling beds, cyclones)", "https://www.elsevier.com/"),
    ("NPTEL Chemical Reaction Engineering lectures - reactors and fluidisation",
     "https://nptel.ac.in/"),
]
