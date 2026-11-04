"""DI05005031 Unit 5, part C: section 5.5, the formulas, the viva and the six solved numericals."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from subject_DI05005031 import tr  # noqa: E402
from content_DI05005031_lib import (p, h4, table, math, eq, why, check, pit, derive,
                                    body, card)  # noqa: E402

NOTES_C = []

NOTES_C.append({
    "title": tr("5.5 Space time, space velocity and holding time",
                "5.5 Space time, space velocity અને holding time"),
    "items": [
        card(
            "Space time, space velocity and holding time",
            "Space time, space velocity અને holding time",
            p("Three numbers describe how long material stays in a flow reactor, and students mix "
              "them up because two of them look like a time. Space time divides the reactor volume "
              "by the feed rate measured at the inlet; holding time divides the same volume by the "
              "flow actually inside the reactor. Space velocity is simply the reciprocal of space "
              "time and is what a plant quotes on its data sheet.",
              "Flow reactor માં material કેટલો સમય રહે તે ત્રણ આંકડા કહે છે, અને વિદ્યાર્થીઓ તેમાં "
              "ગૂંચવાય છે કારણ કે બે તો સમય જેવા લાગે. Space time reactor ના volume ને inlet પર માપેલા "
              "feed rate થી ભાગે; holding time એ જ volume ને reactor ની અંદરના ખરા flow થી ભાગે. "
              "Space velocity એ space time નો વ્યસ્ત છે અને plant તેને data sheet પર લખે."),
            math("space time:     tau = V/v0        v0 = feed volume flow at inlet T and P",
                 "space velocity: SV = 1/tau = v0/V   quoted in h-1",
                 "holding time:   t_bar = V/v        v = actual flow at reactor T and P",
                 "first order duty: tau = CA0 X/(-rA)exit  or  tau = X/[k(1 - X)]"),
            h4("For a gas, the two are not the same", "Gas માટે બંને સરખા નથી"),
            math("ideal gas: v/v0 = (P0/P)(T/T0)   for the same molar flow",
                 "example: V = 2 m3, v0 = 0.2 m3/min  ->  tau = 10 min",
                 "at 5 bar and 400 K from 1 bar and 300 K: v = 0.0533 m3/min, t_bar = 37.5 min"),
            eq("tau = V/v0", "SV = 1/tau = v0/V", "t_bar = V/v"),
            why("Space time is a property of the feed and the vessel only, which is why it is used "
                "in design: two reactors of the same space time will give the same conversion at the "
                "same kinetics, whatever the temperature and pressure inside. Holding time is a "
                "property of the conditions, which is why it is used for safety: a vessel at high "
                "pressure holds its inventory much longer than its space time suggests.",
                "Space time ફક્ત feed અને પાત્રનું લક્ષણ છે, તેથી design માં વપરાય: એ જ space time "
                "વાળા બે reactors એ જ kinetics પર એ જ conversion આપે, અંદરનું temperature અને pressure "
                "ગમે તે હોય. Holding time શરતોનું લક્ષણ છે, તેથી safety માં વપરાય: ઊંચા pressure વાળું "
                "પાત્ર તેના space time કહે તેના કરતાં ઘણો વધુ સમય પોતાનો જથ્થો રાખે."),
            check("Reciprocal check: SV = 1/tau, so tau = 10 min = 1/6 h goes with SV = 6 h-1. If a "
                  "data sheet quotes both and they are not reciprocals, one of them is on a "
                  "different basis - usually per mass of catalyst instead of per reactor volume.",
                  "વ્યસ્ત ચકાસો: SV = 1/tau, તેથી tau = 10 min = 1/6 h સાથે SV = 6 h-1 બને. Data "
                  "sheet બંને લખે અને તે વ્યસ્ત ન હોય તો એક જુદા આધાર પર છે - સામાન્ય રીતે reactor "
                  "volume ની જગ્યાએ catalyst ના દળ પર."),
            pit("Quoting a space velocity without its basis. GHSV in h-1 can mean per volume of "
                "reactor, per volume of catalyst or per mass of catalyst, and the numbers differ by "
                "the bed voidage and the bulk density - a factor of two is ordinary.",
                "આધાર વગર space velocity લખવો. h-1 માં GHSV નો અર્થ reactor ના volume દીઠ, catalyst "
                "ના volume દીઠ કે catalyst ના દળ દીઠ હોઈ શકે, અને આંકડા bed voidage તથા bulk density "
                "જેટલા જુદા પડે - બે ગણો ફેર સામાન્ય છે."),
            diagram="u5_space",
            syllabus_item="5.5",
        ),
        card(
            "From the equation to a vessel: the six design steps",
            "Equation થી પાત્ર સુધી: design ના છ પગલાં",
            p("A design equation gives a theoretical volume. A vessel has to be built, filled with "
              "catalyst, cleaned, inspected and kept away from a runaway, so the calculated volume is "
              "only the starting point. The same six steps are used whether the answer is a batch "
              "time or a reactor volume.",
              "Design equation સૈદ્ધાંતિક volume આપે. પાત્ર બનાવવું પડે, catalyst ભરવો પડે, સાફ કરવું "
              "પડે, તપાસવું પડે અને runaway થી દૂર રાખવું પડે, તેથી ગણેલું volume ફક્ત શરૂઆત છે. "
              "જવાબ batch time હોય કે reactor volume, એ જ છ પગલાં વપરાય."),
            derive("1. fix the stoichiometry and the rate law, from the laboratory data of Unit 3",
                   "2. fix the target conversion and the feed rate, from the material balance",
                   "3. choose the model - batch, CSTR, train of CSTRs or PFR - and take its equation",
                   "4. calculate the ideal time or volume at the design temperature",
                   "5. add the margin: freeboard, fouling, catalyst decay, turndown",
                   "6. check what the equation does not model: heat transfer, pressure drop, mixing"),
            table([tr("Item", "બાબત"), tr("Typical margin", "સામાન્ય માર્જિન"),
                   tr("Why", "કેમ")],
                  [[tr("batch freeboard", "batch freeboard"), tr("20-30 %", "20-30 %"),
                    tr("foam, stirrer vortex, thermal expansion",
                       "foam, stirrer નો ભંગાણ, thermal expansion")],
                   [tr("catalyst decay", "catalyst decay"), tr("10-30 %", "10-30 %"),
                    tr("activity falls before the next shutdown",
                       "આગલા shutdown પહેલા activity ઘટે")],
                   [tr("fouling and scale", "fouling અને scale"), tr("10-20 %", "10-20 %"),
                    tr("heat transfer, not volume, is usually the limit",
                       "મર્યાદા સામાન્ય રીતે heat transfer હોય, volume નહીં")],
                   [tr("turndown", "turndown"), tr("20 % above minimum", "લઘુતમથી 20 % ઉપર"),
                    tr("the plant rarely runs at nameplate",
                       "plant ભાગ્યે જ nameplate પર ચાલે")]]),
            eq("V_vessel = V_design x (1 + margin)", "t_cycle = t_reaction + t_turnaround"),
            why("The design equation is exact for the model and wrong for the plant, and the two "
                "errors are not the same size. Mixing, heat transfer and pressure drop can each cut "
                "the achievable conversion by several points, while the margin only adds volume, so "
                "the margin is spent where the physics is least certain.",
                "Design equation model માટે સાચું છે અને plant માટે ખોટું, અને બંને ભૂલો સરખી નથી. "
                "Mixing, heat transfer અને pressure drop દરેક મળીને conversion કેટલાક ટકા ઘટાડી શકે, "
                "જ્યારે માર્જિન ફક્ત volume ઉમેરે, તેથી માર્જિન ત્યાં વાપરાય જ્યાં ભૌતિકશાસ્ત્ર સૌથી "
                "ઓછું ચોક્કસ છે."),
            check("Cross-check the finished size against a known plant: a 46 m3 PFR is a tube of "
                  "0.6 m diameter and about 160 m long, or a bundle of 60 tubes of 2.7 m. If the "
                  "geometry looks impossible, the rate constant or the flow rate is out by a factor "
                  "of ten.",
                  "તૈયાર માપ જાણીતા plant સાથે ચકાસો: 46 m3 નો PFR 0.6 m વ્યાસ અને લગભગ 160 m લાંબી "
                  "નળી છે, કે 2.7 m ની 60 નળીઓનું bundle. ભૂમિતિ અશક્ય લાગે તો rate constant કે flow "
                  "rate દશ ગણો ખોટો છે."),
            pit("Sending the ideal volume to the fabricator. The ideal volume is what the kinetics "
                "asks for; the vessel also needs a jacket, a distributor, nozzles, a manway and a "
                "support, and those take space that the reaction volume cannot use.",
                "Ideal volume સીધું fabricator ને મોકલવું. Ideal volume kinetics માંગે તે છે; પાત્રને "
                "jacket, distributor, nozzles, manway અને support પણ જોઈએ, અને તે જગ્યા reaction "
                "volume વાપરી શકતું નથી."),
            syllabus_item="5.5",
        ),
    ],
})

EQUATIONS = [
    {"title": tr("The performance equation", "Performance equation ના સૂત્રો"),
     "items": [
         {"name": tr("Batch", "Batch"),
          "f": "t = NA0 x integral dX/(-rA V)",
          "terms": tr("No flow term: the answer is a time.",
                      "કોઈ flow ભાગ નહીં: જવાબ સમય છે.")},
         {"name": tr("CSTR", "CSTR"),
          "f": "V = FA0 X / (-rA)exit",
          "terms": tr("One algebraic line taken at the outlet composition.",
                      "Outlet રચના પર લેવાયેલી એક બીજગણિતીય લીટી.")},
         {"name": tr("PFR", "PFR"),
          "f": "V = FA0 x integral dX/(-rA)",
          "terms": tr("An integral along the tube, because the composition keeps changing.",
                      "નળી પર integral, કારણ કે રચના સતત બદલાય છે.")},
     ]},
    {"title": tr("Constant density", "Constant density"),
     "items": [
         {"name": tr("Concentration", "Concentration"),
          "f": "CA = CA0 (1 - X)",
          "terms": tr("Holds for liquids and for gases with no mole change.",
                      "પ્રવાહી માટે અને mole change ન હોય તેવા gases માટે સાચું.")},
         {"name": tr("nth order rate", "nth order rate"),
          "f": "-rA = k CA0^n (1 - X)^n",
          "terms": tr("Turns the design equation into an integral in X alone.",
                      "Design equation ને ફક્ત X ના integral માં ફેરવે.")},
         {"name": tr("Gas with mole change", "Mole change વાળો gas"),
          "f": "CA = CA0 (1 - X)/(1 + eps X)",
          "terms": tr("The expansion factor of Unit 3; the simple closed forms no longer apply.",
                      "Unit 3 નો expansion factor; સાદાં closed forms હવે લાગુ ન પડે.")},
     ]},
    {"title": tr("Space time and space velocity", "Space time અને space velocity"),
     "items": [
         {"name": tr("Space time", "Space time"),
          "f": "tau = V/v0 = CA0 X/(-rA)exit",
          "terms": tr("Feed flow measured at the inlet temperature and pressure.",
                      "Inlet temperature અને pressure પર માપેલો feed flow.")},
         {"name": tr("Space velocity", "Space velocity"),
          "f": "SV = 1/tau = v0/V",
          "terms": tr("Quoted in h-1; always state the basis - reactor, catalyst volume or mass.",
                      "h-1 માં લખાય; આધાર હંમેશા જણાવો - reactor, catalyst volume કે દળ.")},
         {"name": tr("Holding time", "Holding time"),
          "f": "t_bar = V/v",
          "terms": tr("v is the flow at the reactor conditions, so it moves with T and P.",
                      "v એ reactor ની શરતો પરનો flow છે, તેથી T અને P સાથે બદલાય.")},
         {"name": tr("Gas correction", "Gas સુધારો"),
          "f": "v/v0 = (P0/P)(T/T0)",
          "terms": tr("Ideal gas, same molar flow: compress the gas and it stays longer.",
                      "Ideal gas, એ જ molar flow: gas દબાવો તો તે વધુ સમય રહે.")},
     ]},
    {"title": tr("First order yardsticks", "First order ના માપદંડ"),
     "items": [
         {"name": tr("CSTR", "CSTR"),
          "f": "k tau = X/(1 - X)",
          "terms": tr("4 at 80 %, 9 at 90 %, 19 at 95 %.",
                      "80 % પર 4, 90 % પર 9, 95 % પર 19.")},
         {"name": tr("PFR", "PFR"),
          "f": "k tau = ln[1/(1 - X)]",
          "terms": tr("1.61 at 80 %, 2.30 at 90 %, 4.61 at 99 %.",
                      "80 % પર 1.61, 90 % પર 2.30, 99 % પર 4.61.")},
         {"name": tr("Volume ratio", "Volume ગુણોત્તર"),
          "f": "V_CSTR/V_PFR = [X/(1 - X)] / ln[1/(1 - X)]",
          "terms": tr("2.5 at 80 %, 3.9 at 90 %, 21 at 99 %.",
                      "80 % પર 2.5, 90 % પર 3.9, 99 % પર 21.")},
     ]},
    {"title": tr("Trains and margins", "શ્રેણી અને માર્જિન"),
     "items": [
         {"name": tr("Equal CSTRs in series", "Series માં સરખા CSTR"),
          "f": "1 - X = 1/(1 + k tau/n)^n",
          "terms": tr("The train approaches a PFR as n grows.",
                      "n વધે તેમ શ્રેણી PFR ની નજીક જાય.")},
         {"name": tr("Two tanks", "બે ટાંકી"),
          "f": "k tau each = (1 - X)^(-1/2) - 1",
          "terms": tr("1.236 each for 80 %: half the volume of one tank.",
                      "80 % માટે દરેક 1.236: એક ટાંકી કરતાં અડધું volume.")},
         {"name": tr("Vessel size", "પાત્રનું માપ"),
          "f": "V_vessel = V_design (1 + margin)",
          "terms": tr("Freeboard, fouling, catalyst decay and turndown.",
                      "Freeboard, fouling, catalyst decay અને turndown.")},
         {"name": tr("Batches per day", "દિવસના batch"),
          "f": "N = 1440/(t_reaction + t_turnaround)",
          "terms": tr("Minutes per day divided by the cycle time.",
                      "દિવસના મિનિટ ભાગ્યા cycle time.")},
     ]},
]

VIVA = [
    {"title": tr("The performance equation", "Performance equation ના સૂત્રો"),
     "items": [
         {"q": tr("How can one mole balance give three different design equations?",
                  "એક mole balance ત્રણ જુદાં design equations કેવી રીતે આપે?"),
          "a": tr("Because the balance contains in, out, generation and accumulation, and each "
                  "reactor model deletes a different one. A batch has no in and no out, so it keeps "
                  "accumulation and gives a time. A CSTR has accumulation zero and one composition, "
                  "so it gives an algebraic volume. A PFR has accumulation zero but a composition "
                  "that changes along the length, so it gives an integral.",
                  "કારણ કે balance માં અંદર, બહાર, ઉત્પન્ન અને સંચય છે, અને દરેક reactor model જુદો "
                  "ભાગ કાઢી નાખે. Batch માં અંદર કે બહાર નથી, તેથી સંચય રહે અને સમય મળે. CSTR માં "
                  "સંચય શૂન્ય અને એક જ રચના, તેથી બીજગણિતીય volume મળે. PFR માં સંચય શૂન્ય પણ રચના "
                  "લંબાઈ પર બદલાય, તેથી integral મળે.")},
         {"q": tr("What does the constant density assumption buy us?",
                  "Constant density ધારણા આપણને શું આપે?"),
          "a": tr("It removes the volume flow from the problem. With v = v0 the concentration is a "
                  "straight-line function of conversion, the rate law becomes a function of "
                  "conversion alone, and every design equation can be integrated by hand into the "
                  "closed forms used in practice.",
                  "તે volume flow ને સમસ્યામાંથી કાઢી નાખે. v = v0 સાથે concentration conversion નું "
                  "સીધી લીટીનું વિધેય બને, rate law ફક્ત conversion નું વિધેય બને, અને દરેક design "
                  "equation હાથે integrate કરી વ્યવહારમાં વપરાતાં closed forms માં આવે.")},
         {"q": tr("When is the assumption unsafe?", "ધારણા ક્યારે ખોટી પડે?"),
          "a": tr("Whenever the number of moles changes in the gas phase, or the temperature rises "
                  "enough to change the density of a liquid. A -> 2B at 80 % conversion has a true "
                  "rate about 45 % lower than the constant-density formula predicts, so the volume "
                  "is under-designed.",
                  "જ્યારે gas phase માં moles ની સંખ્યા બદલાય, કે temperature એટલું વધે કે પ્રવાહીની "
                  "density બદલાય. A -> 2B માટે 80 % conversion પર સાચો rate constant-density સૂત્ર "
                  "કહે તેના કરતાં લગભગ 45 % નીચો હોય, તેથી volume ઓછું ગણાય.")},
     ]},
    {"title": tr("Space time and space velocity", "Space time અને space velocity"),
     "items": [
         {"q": tr("What is the difference between space time and holding time?",
                  "Space time અને holding time માં શું ફરક છે?"),
          "a": tr("Space time divides the volume by the feed rate at inlet conditions; holding time "
                  "divides it by the flow actually inside the reactor. For a liquid they are nearly "
                  "equal; for a gas they can differ by the pressure and temperature ratio, and the "
                  "vessel then holds its inventory much longer than the space time says.",
                  "Space time volume ને inlet શરતોના feed rate થી ભાગે; holding time એ જ volume ને "
                  "reactor ની અંદરના ખરા flow થી ભાગે. પ્રવાહી માટે બંને લગભગ સરખા; gas માટે pressure "
                  "અને temperature ના ગુણોત્તર જેટલા ફરક પડે, અને પાત્ર પોતાનો જથ્થો space time કહે તેના "
                  "કરતાં ઘણો વધુ સમય રાખે.")},
         {"q": tr("Why do plants quote space velocity instead of space time?",
                  "Plants space time ની જગ્યાએ space velocity કેમ લખે?"),
          "a": tr("Because productivity is easier to read from it: a higher space velocity means more "
                  "feed per cubic metre per hour. It also lets a plant compare reactors of very "
                  "different sizes at a glance, provided the basis is stated.",
                  "કારણ કે તેમાંથી ઉત્પાદનક્ષમતા સહેલી વંચાય: ઊંચો space velocity એટલે કલાક દીઠ ઘન "
                  "મીટર પ્રતિ વધુ feed. તેનાથી ખૂબ જુદા માપના reactorsની તુલના એક નજરે થાય, જો આધાર "
                  "જણાવેલો હોય.")},
         {"q": tr("A reactor is quoted as 3000 h-1 GHSV. What else must you know?",
                  "Reactor 3000 h-1 GHSV લખેલો છે. બીજું શું જાણવું પડે?"),
          "a": tr("The basis - gas volume per reactor volume, per catalyst volume or per catalyst "
                  "mass - and the conditions of the gas volume. Bed voidage and bulk density alone "
                  "can shift the number by a factor of two.",
                  "આધાર - gas volume reactor volume દીઠ, catalyst volume દીઠ કે catalyst દળ દીઠ - "
                  "અને gas volume ની શરતો. ફક્ત bed voidage અને bulk density આંકડો બે ગણો બદલી શકે.")},
     ]},
    {"title": tr("Choosing the reactor", "Reactor પસંદગી"),
     "items": [
         {"q": tr("Why does a CSTR need more volume than a PFR?",
                  "CSTR ને PFR કરતાં વધુ volume કેમ જોઈએ?"),
          "a": tr("Because a CSTR works at the outlet concentration for the whole of its residence "
                  "time, and that is the lowest concentration in the system. For a positive order "
                  "reaction, the lowest concentration means the lowest rate, so more volume is needed "
                  "to remove the same amount of A.",
                  "કારણ કે CSTR આખા residence time દરમિયાન outlet concentration પર કામ કરે, અને તે "
                  "system નું સૌથી નીચું concentration છે. Positive order માટે સૌથી નીચું concentration "
                  "એટલે સૌથી નીચો rate, તેથી એટલો જ A દૂર કરવા વધુ volume જોઈએ.")},
         {"q": tr("If the PFR is smaller, why is most of the chemical industry stirred tanks?",
                  "PFR નાનું હોય તો પણ chemical industry માં ઘણા ટાંકા કેમ?"),
          "a": tr("Because volume is rarely the deciding cost. A stirred tank handles solids, can be "
                  "opened and cleaned, can be run batch-wise for many products, removes heat through "
                  "a jacket and is easy to control at part load. A tube cannot do most of those.",
                  "કારણ કે volume ભાગ્યે જ નિર્ણાયક ખર્ચ હોય. હલાવેલી ટાંકી solids સંભાળે, ખોલી સાફ "
                  "થઈ શકે, ઘણા products માટે batch માં ચાલે, jacket થી heat કાઢે અને અડધા load પર "
                  "સહેલી નિયંત્રિત થાય. નળી એમાંનું ઘણું કરી શકતી નથી.")},
         {"q": tr("What does a second CSTR in series actually buy?",
                  "Series માં બીજો CSTR ખરેખર શું આપે?"),
          "a": tr("It lets the first tank work between the feed and the mid-point composition, so the "
                  "average rate is higher and the total volume falls - 38 % less steel at 80 % "
                  "conversion. A third tank buys much less, so trains are usually two or three.",
                  "તે પહેલી ટાંકીને feed અને વચ્ચેની રચના વચ્ચે કામ કરવા દે, તેથી સરેરાશ rate ઊંચો "
                  "રહે અને કુલ volume ઘટે - 80 % conversion પર 38 % ઓછું steel. ત્રીજી ટાંકી ઘણું ઓછું "
                  "આપે, તેથી શ્રેણી સામાન્ય રીતે બે કે ત્રણ હોય.")},
     ]},
    {"title": tr("Design in practice", "વ્યવહારમાં design"),
     "items": [
         {"q": tr("Why build a vessel larger than the design equation asks for?",
                  "Design equation માંગે તેના કરતાં મોટું પાત્ર કેમ બનાવવું?"),
          "a": tr("Freeboard for foam and for the stirrer vortex, space for catalyst decay, allowance "
                  "for fouling on the heat transfer surface, and turndown so the plant can still make "
                  "product at part load. The equation models the kinetics; the margin covers "
                  "everything it does not.",
                  "Foam અને stirrer ના ભંગાણ માટે freeboard, catalyst decay માટે જગ્યા, heat transfer "
                  "સપાટી પર fouling માટે છૂટ, અને turndown જેથી plant અડધા load પર પણ product બનાવી "
                  "શકે. Equation kinetics model કરે; માર્જિન બાકીનું બધું સંભાળે.")},
         {"q": tr("How would you prove that a reactor is behaving as designed?",
                  "Reactor design પ્રમાણે વર્તે છે તે કેવી રીતે સાબિત કરશો?"),
          "a": tr("Three measurements: a tracer test for the residence time distribution, a "
                  "conversion and temperature profile for the kinetics, and a pressure drop for the "
                  "bed. If all three agree with the model the design equation was applied correctly; "
                  "if only the conversion agrees, the model is right for the wrong reason.",
                  "ત્રણ માપ: residence time distribution માટે tracer test, kinetics માટે conversion "
                  "અને temperature profile, અને bed માટે pressure drop. ત્રણેય model સાથે મળે તો "
                  "design equation યોગ્ય રીતે લાગુ થયું; ફક્ત conversion મળે તો model ખોટા કારણથી "
                  "સાચું છે.")},
         {"q": tr("Which single number would you change to raise the capacity of an existing CSTR?",
                  "ચાલુ CSTR ની ક્ષમતા વધારવા કયો એક આંકડો બદલશો?"),
          "a": tr("The temperature, if the catalyst allows it, because k rises exponentially and the "
                  "volume is fixed. Everything else - feed rate, conversion or volume - either costs "
                  "capital or breaks the duty; temperature costs only a little more jacket duty until "
                  "selectivity or catalyst life becomes the limit.",
                  "Temperature, જો catalyst પરવાનગી આપે, કારણ કે k ઝડપથી વધે અને volume નિશ્ચિત છે. "
                  "બાકીનું - feed rate, conversion કે volume - કાં તો ખર્ચ વધારે કાં તો કામ બગડે; "
                  "temperature ફક્ત થોડું વધુ jacket કામ માંગે, જ્યાં સુધી selectivity કે catalyst "
                  "આયુ મર્યાદા ન બને.")},
     ]},
]

_PRACTICE = [
    ("Batch time, cycle and daily output",
     "Batch time, cycle અને રોજનું ઉત્પાદન",
     "A 1.5 m3 batch reactor is charged with CA0 = 2.0 kmol/m3 of A. The reaction is first order with "
     "k = 0.030 min-1 and is run to 90 % conversion. Filling, heating, emptying and cleaning take 25 "
     "min. Find the reaction time, the cycle time, the number of batches per day and the daily "
     "production of A reacted.",
     "1.5 m3 ના batch reactor માં CA0 = 2.0 kmol/m3 A ભરાય છે. પ્રક્રિયા first order છે, "
     "k = 0.030 min-1, અને 90 % conversion સુધી ચલાવાય છે. ભરવું, ગરમ કરવું, ખાલી કરવું અને સફાઈ "
     "25 min લે છે. Reaction time, cycle time, દિવસના batch અને રોજ પ્રક્રિયા થતા A નું ઉત્પાદન શોધો.",
     [h4("Step 1 - reaction time", "પગલું 1 - reaction time"),
      math("t = (1/k) ln[1/(1 - X)] = (1/0.030) ln(1/0.10)",
           "  = 33.33 x 2.303 = 76.8 min"),
      h4("Step 2 - cycle time", "પગલું 2 - cycle time"),
      math("cycle = 76.8 + 25 = 101.8 min",
           "batches a day = 1440/101.8 = 14.1  ->  14 whole batches"),
      h4("Step 3 - daily production", "પગલું 3 - રોજનું ઉત્પાદન"),
      math("A charged = CA0 V = 2.0 x 1.5 = 3.0 kmol",
           "A reacted per batch = 0.90 x 3.0 = 2.70 kmol",
           "per day = 14 x 2.70 = 37.8 kmol"),
      eq("t = 76.8 min,  cycle = 101.8 min,  14 batches/day,  37.8 kmol of A a day"),
      p("Only 75 % of the day is reaction time. Cutting the turnaround from 25 to 10 min would give "
        "16.6 batches, i.e. 18 % more product from the same vessel - which is why turnaround is "
        "measured and argued about in every batch plant.",
        "દિવસના ફક્ત 75 % સમય reaction છે. Turnaround 25 થી 10 min કરવાથી 16.6 batch મળે, એટલે એ જ "
        "પાત્રમાંથી 18 % વધુ ઉત્પાદન - તેથી જ દરેક batch plant માં turnaround માપાય અને તેના પર "
        "ચર્ચા થાય."),
      check("exp(-0.030 x 76.8) = exp(-2.30) = 0.100, so 10 % of A is left.",
            "exp(-0.030 x 76.8) = exp(-2.30) = 0.100, તેથી 10 % A બાકી."),
      pit("Rounding the number of batches up. A plant can run 14 batches, not 14.1; rounding up "
          "overstates capacity by a few per cent every time.",
          "Batch ની સંખ્યાને ઉપર ગોળ કરવી. Plant 14 batch ચલાવી શકે, 14.1 નહીં; ઉપર ગોળ કરવાથી દર "
          "વખતે ક્ષમતા થોડા ટકા વધારે દેખાય.")],
     6),
    ("CSTR volume and space velocity",
     "CSTR નું volume અને space velocity",
     "A first order reaction with k = 0.20 h-1 and CA0 = 1.5 kmol/m3 is to be carried out to 85 % "
     "conversion at a feed rate of 4.0 m3/h. Find the space time, the reactor volume, the exit rate "
     "of reaction and the space velocity.",
     "k = 0.20 h-1 અને CA0 = 1.5 kmol/m3 વાળી first order પ્રક્રિયા 4.0 m3/h ના feed rate પર 85 % "
     "conversion સુધી કરવી છે. Space time, reactor volume, exit પરનો rate of reaction અને space "
     "velocity શોધો.",
     [h4("Step 1 - space time", "પગલું 1 - space time"),
      math("tau = X/[k(1 - X)] = 0.85/(0.20 x 0.15)",
           "    = 0.85/0.0300 = 28.3 h"),
      h4("Step 2 - volume", "પગલું 2 - volume"),
      math("V = v0 tau = 4.0 x 28.3 = 113 m3"),
      h4("Step 3 - the exit rate, as a check", "પગલું 3 - exit rate, ચકાસણી તરીકે"),
      math("FA0 = v0 CA0 = 4.0 x 1.5 = 6.0 kmol/h",
           "-rA,exit = k CA0 (1 - X) = 0.20 x 1.5 x 0.15 = 0.045 kmol/(m3 h)",
           "V = FA0 X/(-rA) = 6.0 x 0.85/0.045 = 113 m3"),
      h4("Step 4 - space velocity", "પગલું 4 - space velocity"),
      math("SV = 1/tau = 1/28.3 = 0.0353 h-1"),
      eq("tau = 28.3 h,  V = 113 m3,  SV = 0.035 h-1"),
      p("A space time of 28 h is long, and it is the price of 85 % conversion in one tank. Two tanks "
        "in series would need 2 x 9.6 h, i.e. about 77 m3 in all, for the same duty.",
        "28 h નો space time લાંબો છે, અને એ એક ટાંકીમાં 85 % conversion ની કિંમત છે. Series માં બે "
        "ટાંકીને દરેક 9.6 h જોઈએ, એટલે એ જ કામ માટે કુલ લગભગ 77 m3."),
      check("The two routes to V agree - from tau and from the exit rate - which is the whole point "
            "of the rectangle: V/FA0 is both X times the height and the space time times CA0.",
            "V સુધીના બંને રસ્તા - tau થી અને exit rate થી - સરખા આવે, જે લંબચોરસનો આખો મુદ્દો છે: "
            "V/FA0 એ X ગુણ્યા ઊંચાઈ અને space time ગુણ્યા CA0 બંને છે."),
      pit("Using CA0 instead of CA0(1 - X) in the exit rate. The rate in a CSTR must be taken at the "
          "composition that actually leaves the vessel.",
          "Exit rate માં CA0(1 - X) ની જગ્યાએ CA0 વાપરવું. CSTR માં rate પાત્રમાંથી ખરેખર નીકળતી "
          "રચના પર લેવો પડે.")],
     7),
    ("The same duty in a PFR and in a train of CSTRs",
     "એ જ કામ PFR માં અને CSTR ની શ્રેણીમાં",
     "The duty of the previous problem (k = 0.20 h-1, v0 = 4.0 m3/h, X = 0.85) is to be met with a "
     "PFR and, separately, with three equal CSTRs in series. Find both volumes and compare them "
     "with the single CSTR.",
     "આગલા દાખલાનું કામ (k = 0.20 h-1, v0 = 4.0 m3/h, X = 0.85) PFR થી અને અલગથી series માં ત્રણ "
     "સરખા CSTR થી કરવું છે. બંને volumes શોધો અને એક CSTR સાથે સરખાવો.",
     [h4("Step 1 - PFR", "પગલું 1 - PFR"),
      math("tau = ln[1/(1 - X)]/k = ln(1/0.15)/0.20 = 1.897/0.20 = 9.49 h",
           "V = 4.0 x 9.49 = 37.9 m3"),
      h4("Step 2 - three equal CSTRs", "પગલું 2 - ત્રણ સરખા CSTR"),
      math("1 - X = 1/(1 + k tau/3)^3  ->  1 + k tau/3 = (1/0.15)^(1/3) = 1.882",
           "k tau total = 3 x 0.882 = 2.646  ->  tau each = 0.882/0.20 = 4.41 h",
           "V each = 4.0 x 4.41 = 17.6 m3,  total = 52.9 m3"),
      h4("Step 3 - comparison", "પગલું 3 - સરખામણી"),
      math("one CSTR 113 m3 : three CSTRs 53 m3 : one PFR 37.9 m3",
           "PFR/CSTR = 37.9/113 = 0.34,  train/CSTR = 53/113 = 0.47"),
      eq("PFR 37.9 m3, three CSTRs 52.9 m3, one CSTR 113 m3"),
      p("Three tanks recover 62 % of the volume saving a PFR would give, at much lower risk: each "
        "tank is a standard stirred vessel. This is the usual compromise in a plant that must also "
        "handle solids or changing products.",
        "ત્રણ ટાંકી PFR આપે તે volume બચતના 62 % પાછી મેળવે, ઘણા ઓછા જોખમે: દરેક ટાંકી પ્રમાણભૂત "
        "હલાવેલું પાત્ર છે. જે plant ને solids કે બદલાતા products સંભાળવા હોય ત્યાં આ સામાન્ય "
        "સમાધાન છે."),
      check("(1 + 0.882) cubed = 6.67 = 1/0.15, so 1 - X = 0.15 and X = 0.85.",
            "(1 + 0.882) નો ઘન = 6.67 = 1/0.15, તેથી 1 - X = 0.15 અને X = 0.85."),
      pit("Splitting the single-CSTR space time by three. The space time per tank of a train is not "
          "one third of the single tank's; it comes from the nth-root relation above.",
          "એક CSTR નો space time ત્રણે ભાગવો. શ્રેણીમાં દરેક ટાંકીનો space time એક ટાંકીના ત્રીજા "
          "ભાગ જેટલો નથી; તે ઉપરના nth-root સંબંધમાંથી આવે.")],
     8),
    ("Second order reaction: CSTR against PFR",
     "Second order પ્રક્રિયા: CSTR સામે PFR",
     "A + B -> products is second order overall with CA0 = CB0 = 1.2 kmol/m3 and "
     "k = 0.020 m3/(kmol min). The feed is 0.5 m3/min and the conversion required is 75 %. Find the "
     "volume needed in a CSTR and in a PFR, and the ratio between them.",
     "A + B -> products કુલ મળીને second order છે, CA0 = CB0 = 1.2 kmol/m3 અને "
     "k = 0.020 m3/(kmol min). Feed 0.5 m3/min છે અને 75 % conversion જોઈએ. CSTR અને PFR માં જરૂરી "
     "volume અને તેમનો ગુણોત્તર શોધો.",
     [h4("Step 1 - CSTR: rate at the exit", "પગલું 1 - CSTR: exit પર rate"),
      math("-rA = k CA0^2 (1 - X)^2 = 0.020 x 1.44 x (0.25)^2",
           "    = 0.020 x 1.44 x 0.0625 = 1.80e-3 kmol/(m3 min)"),
      h4("Step 2 - CSTR volume", "પગલું 2 - CSTR નું volume"),
      math("V = v0 CA0 X/(-rA) = 0.5 x 1.2 x 0.75/1.80e-3",
           "  = 0.45/1.80e-3 = 250 m3      (tau = 500 min)"),
      h4("Step 3 - PFR volume", "પગલું 3 - PFR નું volume"),
      math("tau = X/[k CA0 (1 - X)] = 0.75/(0.020 x 1.2 x 0.25)",
           "    = 0.75/0.0060 = 125 min  ->  V = 0.5 x 125 = 62.5 m3"),
      eq("CSTR 250 m3,  PFR 62.5 m3,  ratio 4.0"),
      p("For second order with equal feed concentrations the ratio is exactly 1/(1 - X), i.e. 4 at "
        "75 %. That is a neat result worth remembering: for this kinetics the CSTR penalty is simply "
        "the reciprocal of the unconverted fraction.",
        "સરખા feed concentrations વાળી second order માટે ગુણોત્તર બરાબર 1/(1 - X) થાય, એટલે 75 % પર "
        "4. આ સરસ પરિણામ યાદ રાખવા જેવું છે: આ kinetics માટે CSTR ની સજા ફક્ત ન વપરાયેલા અંશનો "
        "વ્યસ્ત છે."),
      check("General check for second order: V_CSTR/V_PFR = 1/(1 - X). At 50 % it is 2, at 90 % it is "
            "10 - both are easy to confirm from the two formulas.",
            "Second order માટે સામાન્ય ચકાસણી: V_CSTR/V_PFR = 1/(1 - X). 50 % પર 2, 90 % પર 10 - બંને "
            "બે સૂત્રોમાંથી સહેલાઈથી ચકાસાય."),
      pit("Using the first order form of the CSTR equation for second order kinetics. The rate must "
          "be written with the squared concentration term before it is put into the balance.",
          "Second order kinetics માટે CSTR equation નું first order સ્વરૂપ વાપરવું. Rate balance માં "
          "મૂકતા પહેલા વર્ગવાળા concentration પદ સાથે લખવો પડે.")],
     7),
    ("Space time, space velocity and holding time",
     "Space time, space velocity અને holding time",
     "A gas phase reaction runs in a 2.4 m3 CSTR. The feed is 0.8 m3/min measured at 2 bar and "
     "350 K; inside the reactor the gas is at 6 bar and 400 K. Find the space time, the space "
     "velocity and the holding time, and explain the difference.",
     "Gas phase પ્રક્રિયા 2.4 m3 ના CSTR માં ચાલે છે. Feed 0.8 m3/min છે, જે 2 bar અને 350 K પર "
     "માપેલો છે; reactor ની અંદર gas 6 bar અને 400 K પર છે. Space time, space velocity અને holding "
     "time શોધો અને ફરક સમજાવો.",
     [h4("Step 1 - space time", "પગલું 1 - space time"),
      math("tau = V/v0 = 2.4/0.8 = 3.0 min = 0.050 h"),
      h4("Step 2 - space velocity", "પગલું 2 - space velocity"),
      math("SV = 1/tau = 1/0.050 = 20 h-1"),
      h4("Step 3 - the flow inside", "પગલું 3 - અંદરનો flow"),
      math("v = v0 (P0/P)(T/T0) = 0.8 x (2/6) x (400/350)",
           "  = 0.8 x 0.333 x 1.143 = 0.305 m3/min"),
      h4("Step 4 - holding time", "પગલું 4 - holding time"),
      math("t_bar = V/v = 2.4/0.305 = 7.9 min"),
      eq("tau = 3.0 min,  SV = 20 h-1,  holding time = 7.9 min"),
      p("The gas is compressed to three times the feed pressure, so it occupies a third of the volume "
        "it did and stays nearly three times as long as the space time says. Space time is the "
        "design number; holding time is the number that matters for a side reaction or for a "
        "thermal hazard.",
        "Gas feed pressure કરતાં ત્રણ ગણું દબાય છે, તેથી તે પહેલા કરતાં ત્રીજા ભાગની જગ્યા લે અને "
        "space time કહે તેના કરતાં લગભગ ત્રણ ગણો સમય રહે. Space time design નો આંકડો છે; holding time "
        "side reaction કે thermal hazard માટે મહત્વનો આંકડો છે."),
      check("Both numbers must satisfy V = tau v0 = t_bar v: 3.0 x 0.8 = 2.4 and 7.9 x 0.305 = 2.4.",
            "બંને આંકડાએ V = tau v0 = t_bar v પૂરું કરવું પડે: 3.0 x 0.8 = 2.4 અને 7.9 x 0.305 = 2.4."),
      pit("Quoting the space velocity as a residence time. 20 h-1 is not 20 hours; it means twenty "
          "reactor volumes of feed pass every hour, so the space time is three minutes.",
          "Space velocity ને residence time ગણવો. 20 h-1 એટલે 20 કલાક નહીં; તેનો અર્થ કલાક દીઠ "
          "વીસ reactor volumes feed પસાર થાય, તેથી space time ત્રણ મિનિટ છે.")],
     6),
    ("Choosing the smallest vessel for 90 % conversion",
     "90 % conversion માટે સૌથી નાનું પાત્ર પસંદ કરવું",
     "A first order reaction has k = 0.15 h-1 and the feed rate is 3.0 m3/h. The product must reach "
     "90 % conversion. Compare the volume of one CSTR, two equal CSTRs in series and one PFR, and "
     "state which you would recommend and why.",
     "First order પ્રક્રિયાનો k = 0.15 h-1 છે અને feed rate 3.0 m3/h છે. Product 90 % conversion સુધી "
     "પહોંચવું જોઈએ. એક CSTR, series માં બે સરખા CSTR અને એક PFR ના volume સરખાવો, અને કયો સૂચવશો "
     "તે કારણ સાથે કહો.",
     [h4("Step 1 - one CSTR", "પગલું 1 - એક CSTR"),
      math("k tau = X/(1 - X) = 0.90/0.10 = 9.0  ->  tau = 60 h",
           "V = 3.0 x 60 = 180 m3"),
      h4("Step 2 - two equal CSTRs", "પગલું 2 - બે સરખા CSTR"),
      math("1 + k tau/2 = (1/0.10)^(1/2) = 3.162",
           "k tau each = 2.162  ->  tau each = 14.4 h",
           "V each = 3.0 x 14.4 = 43.2 m3,  total = 86.4 m3"),
      h4("Step 3 - one PFR", "પગલું 3 - એક PFR"),
      math("k tau = ln(1/0.10) = 2.303  ->  tau = 15.35 h",
           "V = 3.0 x 15.35 = 46.1 m3"),
      eq("CSTR 180 m3,  two CSTRs 86.4 m3,  PFR 46.1 m3"),
      p("Recommendation: the PFR if the reaction is clean, single phase and the plant can take a "
        "tube; two tanks if solids, cleaning or product changes rule a tube out. One tank alone would "
        "be 180 m3 at 90 % - nearly four times the tube - and is only chosen for a small campaign.",
        "સૂચન: પ્રક્રિયા સ્વચ્છ, single phase અને plant નળી લઈ શકે તો PFR; solids, સફાઈ કે product "
        "બદલાવ નળી ન રહેવા દે તો બે ટાંકી. એક ટાંકી 90 % પર 180 m3 થાય - નળી કરતાં લગભગ ચાર ગણી - "
        "અને નાના campaign માટે જ પસંદ થાય."),
      check("Ratios: 180/46.1 = 3.9 and 86.4/46.1 = 1.9, matching the yardsticks of the formula "
            "sheet for 90 % conversion.",
            "ગુણોત્તર: 180/46.1 = 3.9 અને 86.4/46.1 = 1.9, જે 90 % conversion માટે formula sheet ના "
            "માપદંડ સાથે મળે."),
      pit("Recommending the smallest volume without a heat transfer check. A 46 m3 PFR at 90 % of a "
          "fast exothermic reaction may be impossible to cool; the tube that wins on volume can lose "
          "on temperature control.",
          "Heat transfer ચકાસ્યા વગર સૌથી નાનું volume સૂચવવું. ઝડપી exothermic પ્રક્રિયાના 90 % પર "
          "46 m3 નો PFR ઠંડો કરવો અશક્ય હોઈ શકે; volume પર જીતતી નળી temperature control પર હારી "
          "શકે.")],
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
     "(chapter 4: conversion and reactor sizing; chapter 5: isothermal reactor design)",
     "https://www.pearson.com/"),
    ("P. Trambouze and J.-P. Euzen - Chemical Reactors: From Design to Operation, Editions Technip "
     "(space time, space velocity and reactor comparison)",
     "https://www.editionstechnip.com/"),
    ("NPTEL Chemical Reaction Engineering lectures - isothermal reactor design and reactor sizing",
     "https://nptel.ac.in/"),
]
