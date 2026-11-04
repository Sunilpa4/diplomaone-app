"""DI05005031 Unit 2, part A: sections 2.1 - 2.3 (rate law, concentration term, elementary steps)."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from subject_DI05005031 import tr  # noqa: E402
from content_DI05005031_lib import (p, h4, ul, table, math, eq, why, check, pit, derive,
                                    card)  # noqa: E402

NOTES_A = []

NOTES_A.append({
    "title": tr("2.1 The rate law and its two terms",
                "2.1 Rate law અને તેના બે ભાગ"),
    "items": [
        card(
            "A rate law is a product: k(T) times f(C)",
            "Rate law એ ગુણાકાર છે: k(T) ગુણ્યું f(C)",
            h4("Definition", "વ્યાખ્યા"),
            p("A <b>rate law</b> (or rate equation) is the experimental relation between the rate of "
              "reaction and the concentrations of the species present. For a homogeneous reaction it "
              "is written as two factors multiplied: a number that depends only on temperature, k(T), "
              "and a function of composition, f(C).",
              "<b>Rate law</b> (કે rate equation) એ પ્રક્રિયાના rate અને હાજર species ના "
              "concentrations વચ્ચેનો પ્રયોગથી મળેલો સંબંધ છે. Homogeneous પ્રક્રિયા માટે તેને બે "
              "અવયવના ગુણાકાર તરીકે લખાય છે: ફક્ત temperature પર આધારિત સંખ્યા k(T), અને રચના પર "
              "આધારિત વિધેય f(C)."),
            math("-rA = k(T) f(C)",
                 "f(C) = CA^a CB^b ...",
                 "a + b + ... = overall order n",
                 "example: -rA = k CA CB^2   (order 1 in A, 2 in B, 3 overall)"),
            p("The order with respect to a species is the exponent of its concentration; the overall "
              "order is the sum. Neither is copied from the stoichiometric equation unless the "
              "reaction is elementary - they are read off the experiment.",
              "કોઈ species પ્રતિ order એ તેના concentration નો ઘાત છે; કુલ order એ સરવાળો છે. "
              "પ્રક્રિયા elementary ન હોય તો બંને stoichiometric સમીકરણ પરથી લેવાય નહીં - તે "
              "પ્રયોગ પરથી વંચાય છે."),
            h4("Why the two factors separate", "બે અવયવ કેમ અલગ પડે"),
            p("Temperature changes the energy of the molecules, while composition changes how often "
              "they meet. To a very good approximation the two act independently, so a rate measured "
              "at one temperature can be moved to another simply by replacing k:",
              "Temperature molecules ની energy બદલે છે, જ્યારે રચના તેઓ કેટલી વાર મળે તે બદલે છે. "
              "ખૂબ સારા અંદાજ સુધી બંને સ્વતંત્ર રીતે કામ કરે છે, તેથી એક temperature પર માપેલો rate "
              "બીજા temperature પર ફક્ત k બદલીને લઈ જઈ શકાય:"),
            derive("-rA(T1) = k(T1) f(C)",
                   "-rA(T2) = k(T2) f(C)",
                   "divide:  -rA(T2) / -rA(T1) = k(T2) / k(T1)",
                   "and k(T2)/k(T1) comes from Arrhenius (2.4)"),
            why("f(C) carries the chemistry of the mixture and k(T) carries the energy; a plant that "
                "changes its temperature does not change its order, and a plant that changes its "
                "concentration does not change its activation energy.",
                "f(C) મિશ્રણની chemistry ઉપાડે છે અને k(T) energy ઉપાડે છે; temperature બદલતા "
                "plant નો order બદલાતો નથી, અને concentration બદલતા plant ની activation energy "
                "બદલાતી નથી."),
            check("A rate law must predict the units: with -rA in mol m-3 s-1, the order 3 law "
                  "k CA CB^2 needs k in m6 mol-2 s-1.",
                  "Rate law એ એકમ પણ આપવા જોઈએ: -rA mol m-3 s-1 માં હોય તો order 3 ના law "
                  "k CA CB^2 માટે k m6 mol-2 s-1 માં જોઈએ."),
            pit("Writing the rate law from the equation. 2A + B -> products is third order only if "
                "the reaction is elementary; measure it before you write it.",
                "સમીકરણ પરથી rate law લખવો. 2A + B -> products ત્રીજા orderની ફક્ત ત્યારે જ છે જ્યારે "
                "પ્રક્રિયા elementary હોય; લખતા પહેલાં માપો."),
            diagram="u2_terms",
            syllabus_item="2.1",
        ),
    ],
})

NOTES_A.append({
    "title": tr("2.2 The concentration term and the rate constant",
                "2.2 Concentration વાળો ભાગ અને rate constant"),
    "items": [
        card(
            "What the rate constant is - and what it is not",
            "Rate constant શું છે - અને શું નથી",
            h4("The constant is not a constant of nature", "Constant એ કુદરતનો અચળ નથી"),
            p("The rate constant k of a given reaction is fixed only for a given <b>temperature, "
              "solvent and catalyst</b>. Change any of the three and it changes; that is why a "
              "laboratory value can never be typed into a plant design without the temperature being "
              "checked.",
              "આપેલી પ્રક્રિયાનો rate constant k ફક્ત આપેલા <b>temperature, solvent અને catalyst</b> "
              "માટે અચળ છે. ત્રણમાંથી કોઈ પણ બદલો તો તે બદલાય છે; તેથી laboratory નું મૂલ્ય "
              "temperature ચકાસ્યા વિના plant design માં કદી નાખી શકાય નહીં."),
            h4("Derivation: what k means when the concentrations are one", "Derivation: concentrations એક હોય ત્યારે k નો અર્થ"),
            p("Put every concentration equal to unity in the power law:",
              "Power law માં દરેક concentration એક મૂકો:"),
            derive("-rA = k CA^a CB^b ...",
                   "set CA = CB = ... = 1 mol m-3",
                   "-rA = k",
                   "so k is the rate when every concentration is 1"),
            p("That is the practical meaning: k is not 'the speed of the reaction' but the speed at a "
              "reference composition. Two reactions with the same k can run at very different rates, "
              "because their concentrations and orders differ.",
              "તેનો વ્યવહારુ અર્થ આ છે: k 'પ્રક્રિયાની ઝડપ' નથી, પણ સંદર્ભ રચના પરની ઝડપ છે. એક જ "
              "k વાળી બે પ્રક્રિયાઓ ખૂબ જુદી ઝડપે ચાલી શકે, કારણ કે તેમના concentrations અને "
              "orders જુદા છે."),
            table(
                [tr("Order", "Order"), tr("Law", "Law"), tr("Unit of k", "k નું એકમ"),
                 tr("What a plot of C against t looks like", "C vs t નો ગ્રાફ")],
                [[tr("0", "0"), "-rA = k", "mol m-3 s-1", tr("a straight falling line", "સીધી ઊતરતી લાઇન")],
                 [tr("1", "1"), "-rA = k CA", "s-1", tr("an exponential decay", "exponential ઘટાડો")],
                 [tr("2", "2"), "-rA = k CA^2", "m3 mol-1 s-1",
                  tr("a curve tailing to zero slowly", "ધીમે શૂન્ય તરફ જતો વક્ર")],
                 [tr("n", "n"), "-rA = k CA^n", "(mol m-3)^(1-n) s-1",
                  tr("depends on n - Unit 3", "n પર આધારિત - Unit 3")]]),
            h4("Pseudo order: when the law hides a reactant", "Pseudo order: જ્યારે law એક reactant છુપાવે"),
            math("true:  -rA = k CA CB      (second order)",
                 "with CB >> CA:  CB ~ constant",
                 "measured: -rA = k' CA   k' = k CB"),
            p("A pseudo first order constant therefore carries the concentration of the excess "
              "reactant inside it. Change the amount of water in a hydrolysis and the 'constant' "
              "changes - a favourite examination question and a real trap in a plant.",
              "Pseudo first order constant માં વધારાના reactant નું concentration સમાયેલું હોય છે. "
              "Hydrolysis માં પાણીનો જથ્થો બદલો તો 'constant' બદલાય - પરીક્ષામાં પૂછાતો પ્રિય પ્રશ્ન "
              "અને plant માં ખરેખર ફસાવતી બાબત."),
            why("Units are the quickest audit of a rate law: if k does not carry (mol m-3)^(1-n) s-1, "
                "the exponents or the rate units are wrong.",
                "Units એ rate law ચકાસવાનો સૌથી ઝડપી ઉપાય છે: k માં (mol m-3)^(1-n) s-1 ન હોય તો ઘાત "
                "કે rate ના units ખોટા છે."),
            pit("Reporting k to four figures from two runs. Two points give an order and a constant "
                "with large error; a report needs the scatter of several runs.",
                "બે રન પરથી k ને ચાર આંકડામાં લખવો. બે બિંદુ order અને constant મોટી ભૂલ સાથે આપે "
                "છે; રિપોર્ટને ઘણા રનનું scatter જોઈએ."),
            syllabus_item="2.2",
        ),
    ],
})

NOTES_A.append({
    "title": tr("2.3 Elementary and non-elementary reactions",
                "2.3 Elementary અને non-elementary પ્રક્રિયાઓ"),
    "items": [
        card(
            "Two molecules colliding, or a chain of steps?",
            "બે molecules ની અથડામણ, કે steps ની શૃંખલા?",
            h4("The definition", "વ્યાખ્યા"),
            p("An <b>elementary</b> reaction happens in a single molecular event: the equation as "
              "written is the step, so order equals molecularity and the rate law can be written from "
              "the equation. A <b>non-elementary</b> reaction is a sequence of such events - "
              "initiation, propagation, termination, or an adsorption and a surface reaction - and its "
              "rate law has to be derived from the sequence.",
              "<b>Elementary</b> પ્રક્રિયા એક જ molecular ઘટનામાં થાય છે: લખેલું સમીકરણ એ જ step છે, "
              "તેથી order અને molecularity સરખા થાય અને rate law સમીકરણ પરથી લખી શકાય. "
              "<b>Non-elementary</b> પ્રક્રિયા એવી ઘટનાઓની શૃંખલા છે - initiation, propagation, "
              "termination, અથવા adsorption અને surface પ્રક્રિયા - અને તેનો rate law શૃંખલા પરથી "
              "derive કરવો પડે."),
            table(
                [tr("Test", "કસોટી"), tr("Elementary", "Elementary"),
                 tr("Non-elementary", "Non-elementary")],
                [[tr("Number of steps", "steps ની સંખ્યા"), tr("one", "એક"),
                  tr("two or more", "બે કે વધુ")],
                 [tr("Order from the equation?", "સમીકરણ પરથી order?"), tr("yes", "હા"),
                  tr("no, from experiment", "ના, પ્રયોગ પરથી")],
                 [tr("Molecularity = order?", "Molecularity = order?"), tr("always", "હંમેશા"),
                  tr("only by accident", "કદાચ જ")],
                 [tr("Example", "ઉદાહરણ"), tr("NO2 + CO -> NO + CO2 (one step)",
                                               "NO2 + CO -> NO + CO2 (એક step)"),
                  tr("H2 + Br2 -> 2 HBr (chain)", "H2 + Br2 -> 2 HBr (chain)")]]),
            h4("Derivation: the steady state on a chain carrier",
               "Derivation: chain carrier પર steady state"),
            p("For H2 + Br2 the chain is started by Br2 splitting, carried by Br. and H., and stopped "
              "when two Br. meet. Writing kI, kp1, kp2 and kt for the four steps and assuming the atom "
              "concentrations are steady:",
              "H2 + Br2 માં શૃંખલા Br2 તૂટવાથી શરૂ થાય, Br. અને H. દ્વારા ચાલે, અને બે Br. મળતાં "
              "અટકે. ચાર steps માટે kI, kp1, kp2 અને kt લખીને atoms ના concentrations steady "
              "ધારીએ:"),
            derive("initiation:  Br2 -> 2 Br.        rate kI [Br2]",
                   "propagation: Br. + H2 -> HBr + H.",
                   "             H. + Br2 -> HBr + Br.",
                   "termination: 2 Br. -> Br2       rate kt [Br.]^2",
                   "steady on [Br.]: 2 kI [Br2] = 2 kt [Br.]^2",
                   "so  [Br.] = (kI [Br2] / kt)^0.5",
                   "rate = kp2 [H.] [Br2], with [H.] from the other balance",
                   "r = k [H2] [Br2]^1.5 / ([Br2] + k' [HBr])"),
            p("Two lessons come out of that line. The square root in [Br.] becomes <b>1.5</b> as the "
              "order in Br2, and the HBr in the denominator shows <b>product inhibition</b> - the "
              "reaction gets slower as its own product accumulates.",
              "તે લાઇનમાંથી બે પાઠ મળે. [Br.] માંનું વર્ગમૂળ Br2 માં <b>1.5</b> order બની જાય, અને "
              "denominator માંનું HBr <b>product inhibition</b> દર્શાવે - પોતાનું જ product વધતાં "
              "પ્રક્રિયા ધીમી પડે."),
            why("An elementary step obeys the law of mass action exactly; a sequence does not, "
                "because the concentrations of intermediates set the rate. That is why a fractional "
                "order is evidence of a mechanism, not of a measurement error.",
                "Elementary step mass action ના નિયમને ચોક્કસ પાળે છે; શૃંખલા નહીં, કારણ કે rate "
                "intermediates ના concentrations નક્કી કરે છે. તેથી અપૂર્ણાંક order measurement ની "
                "ભૂલ નહીં, mechanism નો પુરાવો છે."),
            pit("Applying the steady-state assumption to the reactants instead of the intermediates. "
                "Reactants change by design - only the short-lived radicals are steady.",
                "Steady-state ધારણા intermediates ને બદલે reactants પર લગાડવી. Reactants તો ડિઝાઇનથી "
                "બદલાય છે - ફક્ત ટૂંકું જીવતાં radicals steady હોય છે."),
            diagram="u2_chain",
            syllabus_item="2.2",
        ),
    ],
})
