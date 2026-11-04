"""DI05005031 Unit 3, part B: sections 3.2 and 3.3 - the constant-volume batch and pressure data."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from subject_DI05005031 import tr  # noqa: E402
from content_DI05005031_lib import (p, h4, ul, ol, table, math, eq, why, check, pit, derive,
                                    card)  # noqa: E402

NOTES_B = []

NOTES_B.append({
    "title": tr("3.2 The constant-volume batch system: conversion and concentration",
                "3.2 અચળ volume વાળી batch system: conversion અને concentration"),
    "items": [
        card(
            "From conversion to concentration, and back",
            "Conversion થી concentration સુધી, અને પાછું",
            p("Almost every batch experiment is run in a closed vessel, so the volume is fixed and "
              "the reaction is followed by the fall of concentration. The working variable is the "
              "<b>fractional conversion</b> X, defined so that it is zero at the start and one when "
              "the limiting reactant is used up:",
              "લગભગ દરેક batch experiment બંધ પાત્રમાં થાય છે, તેથી volume અચળ રહે છે અને પ્રક્રિયા "
              "concentration ઘટવાથી અનુસરાય છે. કામનું ચલ છે <b>fractional conversion</b> X, જે "
              "શરૂઆતમાં શૂન્ય અને limiting reactant પૂરો થાય ત્યારે એક થાય:"),
            derive("X = (NA0 - NA) / NA0        so   NA = NA0 (1 - X)",
                   "constant volume: CA = NA/V and CA0 = NA0/V",
                   "CA = CA0 (1 - X)              the working relation"),
            h4("The rate in terms of conversion", "Conversion ના સંદર્ભમાં rate"),
            p("Differentiate the last line with respect to time. The volume is a constant, so it "
              "comes out of the derivative:",
              "છેલ્લી લીટીનો time સાપેક્ષ derivative લો. Volume અચળ છે, તેથી derivative બહાર આવે છે:"),
            math("-rA = -dCA/dt = CA0 dX/dt",
                 "so a rate measured as dCA/dt and a rate measured as dX/dt differ only by CA0"),
            p("For several reactants the same law holds for each, with its own stoichiometric "
              "coefficient. For aA + bB -> products, X_A and X_B are related by b X_A = a X_B, and "
              "the concentration of B follows from the conversion of A without a second measurement:",
              "ઘણા reactants માટે એ જ law દરેક પર લાગુ પડે, તેના પોતાના stoichiometric coefficient "
              "સાથે. aA + bB -> products માટે X_A અને X_B નો સંબંધ b X_A = a X_B છે, અને B નું "
              "concentration બીજા માપ વગર A ના conversion પરથી મળે:"),
            math("CB = CB0 - (b/a) CA0 X_A"),
            h4("The batch time - the general design equation", "Batch time - સામાન્ય design equation"),
            p("Integrate the rate over the conversion. For constant volume the result is the working "
              "equation of every batch reactor:",
              "Conversion પર rate integrate કરો. અચળ volume માટે પરિણામ એ દરેક batch reactor નું "
              "કામનું સમીકરણ છે:"),
            derive("-rA = CA0 dX/dt",
                   "dt = CA0 dX / (-rA)",
                   "t = CA0 x integral from X = 0 to X of dX / (-rA)",
                   "for first order: t = (1/k) ln[1/(1 - X)]",
                   "for second order, CA0 = CB0: t = X / [k CA0 (1 - X)]"),
            h4("When the volume is not constant: the expansion factor", "Volume અચળ ન હોય ત્યારે: "
                "expansion factor"),
            p("A gas-phase reaction with a mole change cannot stay at constant volume in a "
              "free-piston or bag reactor. The volume then follows the conversion through one "
              "number, the expansion factor ε_A: the fractional change in volume between no "
              "conversion and complete conversion.",
              "Mole change વાળી gas-phase પ્રક્રિયા free-piston કે bag reactor માં અચળ volume રહી "
              "શકતી નથી. ત્યારે volume conversion સાથે એક જ આંકડા દ્વારા બદલાય, expansion factor "
              "ε_A: શૂન્ય conversion અને પૂરા conversion વચ્ચેના volume નો ભાગાકાર ફેરફાર."),
            derive("eps_A = (V at X = 1 - V at X = 0) / V at X = 0 = yA0 x delta",
                   "delta = moles of product - moles of reactant, per mole of A reacted",
                   "at constant T and p: V = V0 (1 + eps_A X)",
                   "CA = nA/V = CA0 (1 - X) / (1 + eps_A X)"),
            math("example 1: pure A -> 2R          yA0 = 1, delta = 1  ->  eps = 1",
                 "example 2: A -> 2R with 50 % inert  yA0 = 0.5  ->  eps = 0.5",
                 "example 3: A + B -> R (delta = -1)  yA0 = 0.5  ->  eps = -0.5",
                 "liquid phase: volume change negligible -> eps = 0"),
            h4("Why the correction matters", "આ સુધારો કેમ જરૂરી છે"),
            p("Take A -> 2R, pure A, CA0 = 10 mol/m3, at 50 % conversion. The naive constant-volume "
              "answer is CA = 5.0 mol/m3; the correct variable-volume answer is",
              "A -> 2R, શુદ્ધ A, CA0 = 10 mol/m3, 50 % conversion લો. અચળ volume વાળો સીધો જવાબ "
              "CA = 5.0 mol/m3 છે; સાચો variable-volume જવાબ છે"),
            math("CA = 10 x (1 - 0.5)/(1 + 1.0 x 0.5) = 5/1.5 = 3.33 mol/m3"),
            eq("the naive answer is 50 % too high - a rate constant taken from it would be badly wrong"),
            why("The constant-volume relation CA = CA0(1 - X) is not a law of nature; it is the "
                "special case eps_A = 0 of the general line. Liquids, and gases with no mole change, "
                "sit in that special case, which is why so much of the subject can be written "
                "without eps at all.",
                "અચળ volume નો સંબંધ CA = CA0(1 - X) કુદરતનો નિયમ નથી; તે સામાન્ય લીટીનો ખાસ કિસ્સો "
                "eps_A = 0 છે. પ્રવાહી અને mole change વગરના gases એ ખાસ કિસ્સામાં આવે છે, તેથી જ "
                "વિષયનો ઘણો ભાગ eps વગર લખાઈ જાય છે."),
            check("At X = 0 the formula must return CA0 and at X = 1 it must return zero for a "
                  "reactant: 10 x (1 - 0)/(1 + 0) = 10 and 10 x 0/2 = 0. Both hold.",
                  "X = 0 પર સૂત્ર CA0 આપવું જોઈએ અને X = 1 પર reactant માટે શૂન્ય: "
                  "10 x (1 - 0)/(1 + 0) = 10 અને 10 x 0/2 = 0. બંને મળે છે."),
            pit("Using the conversion of the wrong reactant. If B is in excess, X_A can be 1.0 while "
                "X_B is only 0.4; the concentration of B must then come from the stoichiometry, not "
                "from CA0(1 - X_A).",
                "ખોટા reactant નું conversion વાપરવું. B excess માં હોય તો X_A 1.0 થઈ શકે જ્યારે X_B "
                "ફક્ત 0.4 હોય; ત્યારે B નું concentration stoichiometry પરથી લેવું, "
                "CA0(1 - X_A) પરથી નહીં."),
            syllabus_item="3.2",
        ),
    ],
})

NOTES_B.append({
    "title": tr("3.3 Total pressure, partial pressure, concentration and conversion",
                "3.3 Total pressure, partial pressure, concentration અને conversion"),
    "items": [
        card(
            "A pressure gauge as a concentration meter",
            "Pressure gauge એ concentration માપવાનું સાધન",
            p("Many gas reactions are run in a closed, rigid vessel where the only easy measurement "
              "is the pressure. For an ideal gas at constant volume and temperature the pressure of "
              "a component is proportional to its amount, so the gauge is a concentration meter in "
              "disguise:",
              "ઘણી gas પ્રક્રિયાઓ બંધ, કઠણ પાત્રમાં થાય છે જ્યાં સહેલું માપ ફક્ત pressure છે. અચળ "
              "volume અને temperature પર ideal gas માટે ઘટકનું pressure તેના જથ્થાના પ્રમાણમાં હોય છે, "
              "તેથી gauge એ છદ્મવેશમાં concentration માપનું સાધન છે:"),
            derive("pA V = nA R T   and   pA0 V = nA0 R T",
                   "divide: pA / pA0 = nA / nA0 = CA / CA0",
                   "and nA/nA0 = 1 - X, so pA = pA0 (1 - X)",
                   "concentration: CA = pA / (R T)"),
            h4("When the mole number changes", "જ્યારે mole સંખ્યા બદલાય"),
            p("If the reaction changes the number of moles, the total pressure moves even when the "
              "reactant pressure falls. Write nT = nT0 + (delta/a) nA0 X and multiply by RT/V:",
              "પ્રક્રિયા moles ની સંખ્યા બદલે તો reactant નું pressure ઘટે તોપણ total pressure બદલાય. "
              "nT = nT0 + (delta/a) nA0 X લખો અને RT/V થી ગુણો:"),
            derive("nT = nT0 + (delta/a) nA0 X        delta = total moles product - reactant",
                   "multiply by RT/V:  p = p0 + (delta/a) pA0 X",
                   "solve for X:  X = (p - p0) / [(delta/a) pA0]",
                   "and pA = pA0 (1 - X) = pA0 - (a/delta)(p - p0)"),
            math("A -> B + C     delta/a = +1 :  pA = 2 pA0 - p",
                 "A -> B         delta/a =  0 :  pA = pA0 (no change in total)",
                 "2A -> B        delta/a = -1/2 : pA = pA0 + 2(p - p0)"),
            h4("A worked gauge reading", "ઉકેલેલું gauge વાંચન"),
            p("A -> B + C in a rigid vessel at 500 K, starting with pure A at p0 = 1.00 bar. After "
              "20 min the gauge reads 1.60 bar. Find the conversion, the concentration of A and the "
              "first order rate constant.",
              "500 K પર કઠણ પાત્રમાં A -> B + C, શરૂઆતમાં શુદ્ધ A p0 = 1.00 bar પર. 20 min પછી gauge "
              "1.60 bar વાંચે છે. conversion, A નું concentration અને first order rate constant શોધો."),
            math("pA = 2 pA0 - p = 2.00 - 1.60 = 0.40 bar",
                 "X = 1 - pA/pA0 = 1 - 0.40/1.00 = 0.60",
                 "CA0 = pA0/(RT) = 100000/(8.314 x 500) = 24.1 mol/m3",
                 "CA = 0.40 x 24.1 = 9.6 mol/m3   (or CA0(1 - X) = 24.1 x 0.40)",
                 "k = (1/t) ln[1/(1 - X)] = (1/20) ln(2.5) = 0.0458 min-1"),
            eq("X = 60 %,  CA = 9.6 mol/m3,  k = 4.58 x 10-2 min-1"),
            h4("Inerts and the partial pressure", "Inert અને partial pressure"),
            p("If the vessel starts with an inert as well as A, the gauge reads the sum of both. The "
              "inert does not react, so its pressure is constant and can be subtracted. Forgetting it "
              "is the commonest error in this topic, and it always makes the conversion look larger "
              "than it is.",
              "પાત્રમાં A સાથે inert પણ હોય તો gauge બંનેનો સરવાળો વાંચે છે. Inert પ્રક્રિયા કરતું "
              "નથી, તેથી તેનું pressure અચળ રહે અને બાદ કરી શકાય. તે ભૂલવું આ topic ની સૌથી સામાન્ય "
              "ભૂલ છે, અને તેનાથી conversion હંમેશા વાસ્તવિકતા કરતાં મોટું દેખાય છે."),
            math("p(total, reacting) = p(gauge) - p(inert)",
                 "with inert present at the start:  pA0 = yA0 p0  (not p0)"),
            why("Pressure is the cheapest and fastest measurement in a gas reactor, and the "
                "stoichiometry turns it into a concentration without sampling. The price is that the "
                "conversion is inferred, not measured, so an error in delta or a forgotten inert "
                "goes straight into k.",
                "Gas reactor માં pressure સૌથી સસ્તું અને ઝડપી માપ છે, અને stoichiometry તેને sample "
                "લીધા વગર concentration માં ફેરવે છે. કિંમત એ છે કે conversion અનુમાનિત છે, માપેલું "
                "નથી, તેથી delta માં ભૂલ કે ભૂલાયેલો inert સીધો k માં જાય છે."),
            check("The two routes to the conversion must agree: from pA, X = 1 - 0.40/1.00 = 0.60; "
                  "from the total, X = (1.60 - 1.00)/(1.00 x 1.00) = 0.60. They do.",
                  "conversion સુધીની બે રીત મળવી જોઈએ: pA પરથી X = 1 - 0.40/1.00 = 0.60; total પરથી "
                  "X = (1.60 - 1.00)/(1.00 x 1.00) = 0.60. બંને મળે છે."),
            pit("Reading the total pressure as the partial pressure of A. For a reaction with a "
                "mole change the total rises while A is disappearing; the two numbers move in "
                "opposite directions, and only the stoichiometry connects them.",
                "Total pressure ને A નું partial pressure ગણવું. Mole change વાળી પ્રક્રિયામાં A ઘટતું "
                "હોય તોપણ total વધે છે; બંને આંકડા વિરુદ્ધ દિશામાં જાય છે, અને ફક્ત stoichiometry તેમને "
                "જોડે છે."),
            diagram="u3_pressure",
            syllabus_item="3.3",
        ),
    ],
})
