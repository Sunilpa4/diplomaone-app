"""DI05005031 Unit 5, part A: sections 5.1 and 5.2 - the performance equation and the batch reactor."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from subject_DI05005031 import tr  # noqa: E402
from content_DI05005031_lib import (p, h4, table, math, eq, why, check, pit, derive,
                                    card)  # noqa: E402

NOTES_A = []

NOTES_A.append({
    "title": tr("5.1 The performance equation of a single ideal reactor",
                "5.1 એક આદર્શ reactor નું performance equation"),
    "items": [
        card(
            "One mole balance, three design equations",
            "એક mole balance, ત્રણ design equations",
            p("Every design calculation in this subject answers one of two questions: how long must "
              "the material stay, or how big must the vessel be? Both come out of a single mole "
              "balance on the reactant A, written first as words - in minus out plus generation "
              "equals accumulation - and then written for the mixing picture of the reactor.",
              "આ subject ની દરેક design ગણતરી બેમાંથી એક પ્રશ્નનો જવાબ આપે છે: material કેટલો સમય "
              "રહેવું જોઈએ, કે પાત્ર કેટલું મોટું જોઈએ? બંને એક જ mole balance માંથી નીકળે છે, જે "
              "reactant A પર લખાય - પહેલા શબ્દોમાં: અંદર આવે તે ઓછા બહાર જાય તે વત્તા ઉત્પન્ન થાય તે "
              "બરાબર સંચિત થાય તે - અને પછી reactor ની mixing પ્રમાણે લખાય."),
            derive("mole balance on A: in - out + generation = accumulation",
                   "batch (no in, no out): NA0 dX/dt = (-rA) V   ->   t = NA0 x integral dX/(-rA V)",
                   "CSTR (steady, perfectly mixed): FA0 - FA - (-rA) V = 0   ->   V = FA0 X / (-rA)",
                   "PFR (steady, plug flow): FA0 dX/dV = -rA   ->   V = FA0 x integral dX/(-rA)",
                   "the balance is the same in all three; only the mixing and the unknown differ"),
            eq("batch: t = NA0 x integral dX/(-rA V)", "CSTR: V = FA0 X/(-rA)exit",
               "PFR: V = FA0 x integral dX/(-rA)"),
            p("The batch asks for a time and gives no flow term at all. The CSTR asks for a volume "
              "and answers with one algebraic line, because the contents have a single composition "
              "and the balance is written at that composition. The PFR asks for a volume and answers "
              "with an integral, because the composition changes continuously from inlet to outlet.",
              "Batch સમય માંગે છે અને flow નો કોઈ ભાગ આપતું નથી. CSTR volume માંગે છે અને એક જ "
              "બીજગણિતીય લીટીથી જવાબ આપે, કારણ કે અંદરની રચના એક જ છે અને balance તે જ રચના પર "
              "લખાય. PFR volume માંગે છે અને integral થી જવાબ આપે, કારણ કે રચના inlet થી outlet સુધી "
              "સતત બદલાય છે."),
            why("The three equations are the same physics: A is consumed at the local rate -rA and "
                "the balance simply asks how long, or how much volume, is needed before the required "
                "amount has gone. What changes is whether the material is well mixed (one "
                "composition, so one rate), unmixed along the flow (a rate at every point, so an "
                "integral) or simply left alone in a vessel (a rate at every instant, so a time).",
                "ત્રણેય equations એક જ ભૌતિક વિજ્ઞાન છે: A સ્થાનિક rate -rA પ્રમાણે વપરાય છે અને "
                "balance ફક્ત પૂછે છે કે જરૂરી જથ્થો ખતમ થવા કેટલો સમય કે કેટલું volume જોઈએ. ફેર "
                "ફક્ત એ છે કે material સરખી રીતે મિક્સ છે (એક રચના, તેથી એક rate), flow સાથે મિક્સ "
                "નથી (દરેક બિંદુએ rate, તેથી integral) કે પાત્રમાં એમ જ પડ્યું છે (દરેક ક્ષણે rate, "
                "તેથી સમય)."),
            check("Check the units of each line before using it: FA0 is kmol/h, -rA is kmol/(m3 h), "
                  "so FA0 X/(-rA) is in m3. The batch line gives hours only if -rA is per hour.",
                  "વાપરતા પહેલા દરેક લીટીના એકમ ચકાસો: FA0 kmol/h છે, -rA kmol/(m3 h) છે, તેથી "
                  "FA0 X/(-rA) m3 માં આવે. Batch ની લીટી કલાક આપે છે જો -rA કલાક દીઠ હોય."),
            pit("Mixing the three equations. A very common exam error is to answer a CSTR question "
                "with the batch first order time, or to put a square root of a CSTR volume into a "
                "PFR duty. Write the balance for the reactor named in the question, not the one you "
                "last practised.",
                "ત્રણ equations ભેગી કરી નાખવી. પરીક્ષામાં ખૂબ સામાન્ય ભૂલ છે CSTR ના પ્રશ્નનો જવાબ "
                "batch ના first order સમયથી આપવો, કે CSTR ના volume નું વર્ગમૂળ PFR ના કામમાં "
                "નાખવું. પ્રશ્નમાં જે reactor કહ્યો છે તેના માટે balance લખો, જે છેલ્લે પ્રેક્ટિસ "
                "કર્યો તેના માટે નહીં."),
            diagram="u5_perf",
            syllabus_item="5.1",
        ),
        card(
            "Constant density: turning the rate into a function of conversion",
            "Constant density: rate ને conversion નું વિધેય બનાવવું",
            p("An equation with two unknowns - concentration and conversion - cannot be integrated. "
              "The constant density assumption removes one of them. For a liquid, or for a gas "
              "reaction in which the number of moles does not change, the volume flow stays the same "
              "through the reactor, so the concentration is a straight line down from the feed value.",
              "બે અજાણ્યાં - concentration અને conversion - વાળું equation integrate થઈ શકે નહીં. "
              "Constant density ધારણા તેમાંથી એક કાઢી નાખે છે. પ્રવાહી માટે, કે જે gas પ્રક્રિયામાં "
              "moles ની સંખ્યા બદલાતી નથી તે માટે, volume flow reactor માં સરખો રહે છે, તેથી "
              "concentration feed ના મૂલ્યથી સીધી લીટીમાં નીચે આવે છે."),
            derive("constant volume: CA = NA/V = NA0(1 - X)/V = CA0 (1 - X)",
                   "nth order: -rA = k CA^n = k CA0^n (1 - X)^n",
                   "first order: -rA = k CA0 (1 - X);  zero order: -rA = k",
                   "second order with CA0 = CB0: -rA = k CA0^2 (1 - X)^2",
                   "so every design equation becomes an integral in X alone, at fixed temperature"),
            h4("What is lost if the density changes", "density બદલાય તો શું ખોવાય"),
            math("gas with mole change (Unit 3): CA = CA0 (1 - X)/(1 + eps X)",
                 "so -rA = k CA0 (1 - X)/(1 + eps X)   for first order",
                 "the design equations still hold, but the integral is no longer elementary"),
            table([tr("Feed", "Feed"), tr("v changes?", "v બદલાય?"),
                   tr("Use", "વાપરો")],
                  [[tr("liquid phase", "પ્રવાહી phase"), tr("no", "ના"),
                    tr("CA = CA0 (1 - X)", "CA = CA0 (1 - X)")],
                   [tr("gas, A -> B", "gas, A -> B"), tr("no", "ના"),
                    tr("CA = CA0 (1 - X)", "CA = CA0 (1 - X)")],
                   [tr("gas, A -> 2B", "gas, A -> 2B"), tr("yes, doubles", "હા, બમણું થાય"),
                    tr("CA = CA0(1-X)/(1+eps X), eps = 1", "CA = CA0(1-X)/(1+eps X), eps = 1")]]),
            why("Conversion is only a convenient variable if the rate can be written in terms of it. "
                "At constant density the proportionality is direct, and that is why every closed "
                "form in this subject - exponential decay for first order, straight line for zero "
                "order, reciprocal for second order - is written in constant-density form.",
                "Rate ને conversion ના પદમાં લખી શકાય તો જ conversion સગવડભરી ચલ બને. Constant "
                "density પર સંબંધ સીધો છે, અને તેથી જ આ subject નું દરેક closed form - first order માટે "
                "exponential decay, zero order માટે સીધી લીટી, second order માટે વ્યસ્ત - "
                "constant-density સ્વરૂપમાં લખાય છે."),
            check("At X = 0.5 the first order rate is exactly half the initial rate, and CA is half "
                  "CA0. If an answer gives a rate that does not fall in step with the concentration, "
                  "the density assumption has been used on a reaction that does not allow it.",
                  "X = 0.5 પર first order rate શરૂઆતના rate કરતાં બરાબર અડધો થાય, અને CA એ CA0 નું "
                  "અડધું થાય. જવાબમાં rate concentration સાથે ડગલે ને પગલે ન ઘટે તો જે પ્રક્રિયા "
                  "પરવાનગી આપતી નથી તેના પર density ધારણા વપરાઈ છે."),
            pit("Applying the constant-density form to a gas reaction with a mole change. For "
                "A -> 2B the volume flow doubles by full conversion and the true concentration falls "
                "faster than (1 - X); the error at X = 0.8 is about 45 % on the rate.",
                "Mole change વાળી gas પ્રક્રિયા પર constant-density સ્વરૂપ લગાડવું. A -> 2B માટે પૂર્ણ "
                "conversion સુધી volume flow બમણો થાય અને સાચું concentration (1 - X) કરતાં ઝડપથી "
                "ઘટે; X = 0.8 પર rate માં લગભગ 45 % જેટલી ભૂલ થાય."),
            syllabus_item="5.1",
        ),
    ],
})

NOTES_A.append({
    "title": tr("5.2 The ideal batch reactor", "5.2 આદર્શ batch reactor"),
    "items": [
        card(
            "Designing the batch reactor in time",
            "Batch reactor ની design સમયમાં",
            p("A batch reactor is designed in time. The vessel is charged, mixed, brought to "
              "temperature, held for the reaction time, then emptied and cleaned. The reaction time "
              "comes from the integrated design equation; the cycle time - reaction plus filling, "
              "heating, emptying and cleaning - decides how many batches a day the vessel can make.",
              "Batch reactor ની design સમયમાં થાય. પાત્ર ભરાય, હલાવાય, temperature પર લાવાય, "
              "reaction time સુધી રખાય, પછી ખાલી અને સાફ થાય. Reaction time સંકલિત design equation "
              "માંથી આવે; cycle time - reaction વત્તા ભરવું, ગરમ કરવું, ખાલી કરવું અને સાફ કરવું - "
              "પાત્ર દિવસમાં કેટલા batch કરી શકે તે નક્કી કરે."),
            math("zero order:  t = X/(k CA0)",
                 "first order: t = (1/k) ln[1/(1 - X)]     (independent of CA0)",
                 "second order, CA0 = CB0:  t = X/[k CA0 (1 - X)]",
                 "cycle time = t + filling + heating + emptying + cleaning"),
            eq("t = (1/k) ln[1/(1 - X)]", "cycle = t + turnaround",
               "batches per day = 1440/cycle"),
            h4("How many batches, and how much product", "કેટલા batch, અને કેટલું ઉત્પાદન"),
            math("A charged per batch = CA0 V",
                 "A reacted per batch = CA0 V X",
                 "daily production = (1440/cycle) x CA0 V X"),
            why("The reaction time and the cycle time are two different numbers, and only the second "
                "one costs money. A batch that takes 150 min to react but 180 min in total turns "
                "5.5 h of vessel time into 5 h of product, which is exactly why plants chase "
                "turnaround time as hard as they chase kinetics.",
                "Reaction time અને cycle time બે જુદા આંકડા છે, અને પૈસા ફક્ત બીજા પર ખર્ચાય છે. જે "
                "batch ને react થવા 150 min જોઈએ પણ કુલ 180 min લાગે તે 5.5 h vessel time ના 5 h "
                "product બનાવે, તેથી જ plants kinetics જેટલી જ મહેનત turnaround time પર કરે છે."),
            check("Work backwards from the answer: with k = 0.02 min-1 and 150 min of reaction, "
                  "exp(-0.02 x 150) = 0.050, so 5 % of A is left and X = 0.95. If the numbers do not "
                  "return to the conversion you started with, the unit of k is wrong.",
                  "જવાબ પરથી પાછળ જાઓ: k = 0.02 min-1 અને 150 min reaction સાથે "
                  "exp(-0.02 x 150) = 0.050, તેથી 5 % A બાકી અને X = 0.95. આંકડા શરૂઆતના "
                  "conversion પર પાછા ન આવે તો k નો એકમ ખોટો છે."),
            pit("Sizing the vessel from the reaction volume alone. A batch vessel is charged to "
                "70-80 % to leave freeboard for foam and for the stirrer, so a 1.0 m3 charge needs "
                "about a 1.3 m3 vessel - and the jacket, nozzle and manway have to fit around it.",
                "ફક્ત reaction volume પરથી પાત્ર માપવું. Batch પાત્ર foam અને stirrer માટે જગ્યા "
                "રાખવા 70-80 % સુધી ભરાય છે, તેથી 1.0 m3 ચાર્જ માટે લગભગ 1.3 m3 પાત્ર જોઈએ - અને "
                "તેની આસપાસ jacket, nozzle અને manway ગોઠવવા પડે."),
            diagram="u5_batch",
            syllabus_item="5.2",
        ),
    ],
})
