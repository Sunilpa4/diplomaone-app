"""DI05005031 Unit 3, part C: section 3.4 - the integrated rate equations - plus formulas, viva and the
six solved numericals."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from subject_DI05005031 import tr  # noqa: E402
from content_DI05005031_lib import (p, h4, ul, ol, table, math, eq, why, check, pit, derive, body,
                                    card)  # noqa: E402

NOTES_C = []

NOTES_C.append({
    "title": tr("3.4 Integrated rate equations, order by order",
                "3.4 દરેક order માટેના integrated rate equations"),
    "items": [
        card(
            "Integrate -dCA/dt = k CA^n once, and every order falls out",
            "એક વાર -dCA/dt = k CA^n integrate કરો, અને દરેક order મળી જાય",
            p("All the laws of this section come from one line: the power law for a constant-volume "
              "batch, separated so that the concentration stays on the left and time on the right.",
              "આ વિભાગના બધા laws એક જ લીટીમાંથી આવે છે: અચળ volume વાળી batch માટેનો power law, "
              "એવી રીતે અલગ કરેલો કે concentration ડાબે અને time જમણે રહે."),
            derive("-dCA/dt = k CA^n",
                   "separate:  CA^-n dCA = -k dt",
                   "integrate from CA0 at t = 0 to CA at t:",
                   "n not equal to 1:  [CA^(1-n)/(1-n)] - [CA0^(1-n)/(1-n)] = -k t",
                   "so  CA^(1-n) - CA0^(1-n) = (n-1) k t",
                   "n = 1:  ln(CA0/CA) = k t"),
            p("Everything else is a substitution into that pair. Put n = 0, 2 or 3 and the familiar "
              "forms appear; the table below is not a list to memorise but the same equation five "
              "times.",
              "બાકીનું બધું એ જ જોડીમાં મૂકવાનું છે. n = 0, 2 કે 3 મૂકો અને જાણીતાં સ્વરૂપ આવે; નીચેનું "
              "કોષ્ટક યાદ કરવાની યાદી નથી પણ એક જ સમીકરણ પાંચ વાર છે."),
            h4("Zero order (n = 0)", "Zero order (n = 0)"),
            math("CA0 - CA = k t            linear in CA",
                 "t1/2 = CA0/(2k)            half-life proportional to CA0"),
            h4("First order (n = 1)", "First order (n = 1)"),
            math("ln(CA0/CA) = k t          linear in ln CA",
                 "CA = CA0 exp(-k t)         exponential decay",
                 "t1/2 = ln2/k = 0.693/k     independent of CA0"),
            h4("Second order (n = 2)", "Second order (n = 2)"),
            math("equal starting concentrations, A + A -> products or CA0 = CB0:",
                 "1/CA - 1/CA0 = k t        linear in 1/CA",
                 "t1/2 = 1/(k CA0)           half-life inversely proportional to CA0"),
            p("When the two reactants start at different concentrations the integration needs partial "
              "fractions, and the result is a logarithm of a ratio instead of a reciprocal:",
              "બે reactants જુદા concentrations પર શરૂ થાય તો integration માટે partial fractions જોઈએ, "
              "અને પરિણામ reciprocal ને બદલે ગુણોત્તરનો logarithm બને છે:"),
            derive("A + B -> products,  CA0 not equal to CB0",
                   "-dCA/dt = k CA CB,  with CB = CB0 - CA0 + CA",
                   "integrate between CA0 and CA:",
                   "ln(CB CA0 / (CA CB0)) = (CB0 - CA0) k t",
                   "check: if CA0 = CB0 the limit of this line is 1/CA - 1/CA0 = k t"),
            h4("Third order (n = 3)", "Third order (n = 3)"),
            math("1/CA^2 - 1/CA0^2 = 2 k t      linear in 1/CA^2",
                 "t1/2 = 3/(2 k CA0^2)"),
            h4("The general nth order law and its half-life", "સામાન્ય nth order law અને તેની half-life"),
            derive("CA^(1-n) - CA0^(1-n) = (n-1) k t",
                   "put CA = CA0/2 and solve for t:",
                   "t1/2 = (2^(n-1) - 1) / ((n-1) k CA0^(n-1))",
                   "n = 0 gives CA0/2k, n = 2 gives 1/(k CA0), n = 3 gives 3/(2k CA0^2)"),
            h4("Which plot is straight, and in what unit k is measured", "કયો પ્લોટ સીધો, અને k નું એકમ"),
            table([tr("Order", "Order"), tr("Straight line", "સીધી રેખા"),
                   tr("Slope", "ઢાળ"), tr("Unit of k", "k નું એકમ")],
                  [["0", tr("CA against t", "CA અને t"), "-k", "mol m-3 s-1"],
                   ["1", tr("ln CA against t", "ln CA અને t"), "-k", "s-1"],
                   ["2", tr("1/CA against t", "1/CA અને t"), "k", "m3 mol-1 s-1"],
                   ["3", tr("1/CA^2 against t", "1/CA^2 અને t"), "2k", "m6 mol-2 s-1"],
                   ["n", tr("CA^(1-n) against t", "CA^(1-n) અને t"), "(n-1)k",
                    tr("(mol m-3)^(1-n) s-1", "(mol m-3)^(1-n) s-1")]]),
            p("For first order only, conversion is independent of the starting concentration: 50 % "
              "takes the same time whether you begin at 1 mol/L or at 0.01 mol/L. That single fact "
              "is the quickest way to recognise first order behaviour in a set of runs.",
              "ફક્ત first order માટે conversion શરૂઆતના concentration પર આધારિત નથી: 1 mol/L થી શરૂ "
              "કરો કે 0.01 mol/L થી, 50 % થવા માટે એ જ સમય લાગે. એ એક હકીકત રનના સેટમાં first order "
              "ઓળખવાની સૌથી ઝડપી રીત છે."),
            why("The order fixes the straight-line variable, so the integrated laws are the integral "
                "method of the previous cards in table form. A rate law integrated once also gives "
                "the batch time directly, which is what a reactor is designed from.",
                "Order એ સીધી રેખાનું ચલ નક્કી કરે છે, તેથી integrated laws એ પાછલા cards ની integral "
                "method જ કોષ્ટક સ્વરૂપમાં છે. એક વાર integrate કરેલો rate law batch time પણ સીધો "
                "આપે છે, અને reactor ની design એના પરથી જ થાય છે."),
            check("Take the second order row with k = 0.05 L mol-1 min-1 and CA0 = 1.0 mol/L. At "
                  "t = 60 min, 1/CA = 1 + 0.05 x 60 = 4.0, so CA = 0.25 mol/L - the last row of the "
                  "table used in 3.1.",
                  "Second order હાર લો: k = 0.05 L mol-1 min-1 અને CA0 = 1.0 mol/L. t = 60 min પર "
                  "1/CA = 1 + 0.05 x 60 = 4.0, તેથી CA = 0.25 mol/L - 3.1 માં વપરાયેલા કોષ્ટકની "
                  "છેલ્લી હાર."),
            pit("Quoting a half-life without its order. \"t1/2 = 20 min\" means nothing until you "
                "say at what CA0 and for which order; the same 20 min at a doubled concentration "
                "means a different order and a different k.",
                "Order વગર half-life લખવી. \"t1/2 = 20 min\" નો અર્થ ત્યાં સુધી નથી જ્યાં સુધી CA0 "
                "અને order ન કહો; બમણા concentration પર એ જ 20 min જુદો order અને જુદો k દર્શાવે છે."),
            diagram="u3_orders",
            syllabus_item="3.4",
        ),
    ],
})

# ---------------------------------------------------------------- equations
EQUATIONS = [
    {"title": tr("Reading the data", "Data વાંચવું"),
     "items": [
         {"name": tr("Power law", "Power law"),
          "f": "-rA = k CA^n",
          "terms": tr("The law all three methods are trying to find.", "ત્રણેય રીતો જે law શોધે છે.")},
         {"name": tr("Logarithmic form", "Logarithmic સ્વરૂપ"),
          "f": "ln(-rA) = ln k + n ln CA",
          "terms": tr("Slope n, intercept ln k; the basis of the differential method.",
                      "ઢાળ n, intercept ln k; differential method નો આધાર.")},
         {"name": tr("Order from two half-lives", "બે half-lives પરથી order"),
          "f": "n = 1 + ln(t1/2,2 / t1/2,1) / ln(CA0,1 / CA0,2)",
          "terms": tr("Two runs at the same temperature are enough.",
                      "એ જ temperature પરની બે રન પૂરતી છે.")},
         {"name": tr("Half-life against concentration", "Concentration સામે half-life"),
          "f": "t1/2 = (2^(n-1) - 1) / ((n-1) k CA0^(n-1))",
          "terms": tr("A log-log plot of t1/2 against CA0 has slope 1 - n.",
                      "t1/2 અને CA0 ના log-log પ્લોટનો ઢાળ 1 - n છે.")},
     ]},
    {"title": tr("Constant-volume batch", "અચળ volume વાળી batch"),
     "items": [
         {"name": tr("Conversion and concentration", "Conversion અને concentration"),
          "f": "CA = CA0 (1 - X)",
          "terms": tr("True only at constant volume; eps = 0 is a special case, not a law.",
                      "ફક્ત અચળ volume પર સાચું; eps = 0 ખાસ કિસ્સો છે, નિયમ નહીં.")},
         {"name": tr("Rate from conversion", "Conversion પરથી rate"),
          "f": "-rA = CA0 dX/dt",
          "terms": tr("A rate in dX/dt is a rate in dCA/dt divided by CA0.",
                      "dX/dt માંનો rate એ dCA/dt માંનો rate ભાગ્યો CA0.")},
         {"name": tr("Batch time", "Batch time"),
          "f": "t = CA0 x integral of dX/(-rA) from 0 to X",
          "terms": tr("The design equation of every batch reactor.",
                      "દરેક batch reactor નું design equation.")},
         {"name": tr("Variable volume", "બદલાતું volume"),
          "f": "CA = CA0 (1 - X) / (1 + eps_A X)",
          "terms": tr("eps_A = yA0 x delta, the fractional volume change at full conversion.",
                      "eps_A = yA0 x delta, પૂરા conversion પર volume નો ભાગાકાર ફેરફાર.")},
     ]},
    {"title": tr("Pressure data", "Pressure data"),
     "items": [
         {"name": tr("Partial pressure and conversion", "Partial pressure અને conversion"),
          "f": "pA = pA0 (1 - X)",
          "terms": tr("Ideal gas at constant volume and temperature.",
                      "અચળ volume અને temperature પર ideal gas.")},
         {"name": tr("Conversion from the gauge", "Gauge પરથી conversion"),
          "f": "X = (p - p0) / ((delta/a) pA0)",
          "terms": tr("delta is the change in total moles per mole of A reacted.",
                      "delta એ A ના એક mole દીઠ total moles માં થતો ફેરફાર છે.")},
         {"name": tr("Partial pressure from the gauge", "Gauge પરથી partial pressure"),
          "f": "pA = pA0 - (a/delta)(p - p0)",
          "terms": tr("A -> B + C: pA = 2pA0 - p;  A -> B: pA = pA0.",
                      "A -> B + C માટે pA = 2pA0 - p;  A -> B માટે pA = pA0.")},
         {"name": tr("Concentration from pressure", "Pressure પરથી concentration"),
          "f": "CA = pA / (R T)",
          "terms": tr("Subtract any inert before you do this.",
                      "આ કરતા પહેલાં inert બાદ કરો.")},
     ]},
    {"title": tr("Integrated laws", "Integrated laws"),
     "items": [
         {"name": tr("Zero order", "Zero order"),
          "f": "CA0 - CA = k t;   t1/2 = CA0/(2k)",
          "terms": tr("A straight line of CA against t with slope -k.",
                      "CA અને t ની સીધી રેખા, ઢાળ -k.")},
         {"name": tr("First order", "First order"),
          "f": "ln(CA0/CA) = k t;   t1/2 = 0.693/k",
          "terms": tr("The half-life does not depend on the starting concentration.",
                      "Half-life શરૂઆતના concentration પર આધારિત નથી.")},
         {"name": tr("Second order", "Second order"),
          "f": "1/CA - 1/CA0 = k t;   t1/2 = 1/(k CA0)",
          "terms": tr("With CA0 not equal to CB0: ln(CB CA0/(CA CB0)) = (CB0 - CA0) k t.",
                      "CA0 અને CB0 જુદા હોય તો: ln(CB CA0/(CA CB0)) = (CB0 - CA0) k t.")},
         {"name": tr("Third order", "Third order"),
          "f": "1/CA^2 - 1/CA0^2 = 2 k t;   t1/2 = 3/(2 k CA0^2)",
          "terms": tr("Rare in practice, frequent in examinations.",
                      "વ્યવહારમાં દુર્લભ, પરીક્ષામાં સામાન્ય.")},
     ]},
    {"title": tr("Any order", "કોઈ પણ order"),
     "items": [
         {"name": tr("General integral", "સામાન્ય integral"),
          "f": "CA^(1-n) - CA0^(1-n) = (n-1) k t",
          "terms": tr("Holds for every n except 1; n = 1 has its own logarithmic form.",
                      "n = 1 સિવાય દરેક n માટે લાગુ; n = 1 નું પોતાનું logarithmic સ્વરૂપ છે.")},
         {"name": tr("Unit of k", "k નું એકમ"),
          "f": "k: (mol m-3)^(1-n) s-1",
          "terms": tr("n = 1 gives s-1, n = 2 gives m3 mol-1 s-1; the unit is the cheapest check.",
                      "n = 1 માટે s-1, n = 2 માટે m3 mol-1 s-1; એકમ સૌથી સસ્તી ચકાસણી છે.")},
     ]},
]

# ---------------------------------------------------------------- viva
VIVA = [
    {"title": tr("Methods of analysis", "Analysis ની રીતો"),
     "items": [
         {"q": tr("Why do we need more than one method to find the order?",
                  "Order શોધવા એક કરતાં વધુ રીત કેમ જોઈએ?"),
          "a": tr("Because each method has a different weakness: the differential method amplifies "
                  "experimental noise, the integral method can only test an order you have guessed, "
                  "and the half-life method uses just one point per run. Two methods that agree "
                  "turn a guess into a result.",
                  "કારણ કે દરેક રીતની નબળાઈ જુદી છે: differential method noise વધારે, integral "
                  "method ફક્ત ધારેલો order ચકાસી શકે, અને half-life method પ્રતિ રન એક જ બિંદુ "
                  "વાપરે. બે રીતો મળે તો ધારણા પરિણામ બની જાય.")},
         {"q": tr("Which method would you use for noisy plant data, and why?",
                  "Noisy plant data માટે કઈ રીત વાપરશો, અને કેમ?"),
          "a": tr("The integral method, because integration averages the noise: one bad point moves "
                  "the slope of the test plot far less than it moves a tangent. The differential "
                  "method should be used only to confirm the order.",
                  "Integral method, કારણ કે integration noise નું સરેરાશ કાઢે: એક ખરાબ બિંદુ test "
                  "plot ના ઢાળને સ્પર્શક કરતાં ઘણો ઓછો ખસેડે. Differential method ફક્ત order "
                  "પુષ્ટિ કરવા વાપરવી જોઈએ.")},
         {"q": tr("What does a straight line in the integral method prove?",
                  "Integral method માં સીધી રેખા શું સાબિત કરે છે?"),
          "a": tr("It proves that the guessed order is consistent with the data over the whole "
                  "concentration range measured, and that the rate constant is genuinely constant. "
                  "It does not prove the mechanism - a mechanism needs a rate law plus other "
                  "evidence.",
                  "તે સાબિત કરે કે ધારેલો order માપેલી આખી concentration પરાસ સાથે સુસંગત છે, અને "
                  "rate constant ખરેખર અચળ છે. તે mechanism સાબિત કરતું નથી - mechanism માટે rate law "
                  "સાથે બીજા પુરાવા જોઈએ.")},
     ]},
    {"title": tr("Constant volume and pressure data", "અચળ volume અને pressure data"),
     "items": [
         {"q": tr("When is CA = CA0(1 - X) valid?", "CA = CA0(1 - X) ક્યારે માન્ય છે?"),
          "a": tr("Only when the volume of the reacting mixture is constant, that is for a liquid "
                  "phase or for a gas reaction with no change in the number of moles. Otherwise the "
                  "expansion factor form CA = CA0(1 - X)/(1 + eps X) must be used.",
                  "ફક્ત ત્યારે જ્યારે પ્રક્રિયા મિશ્રણનું volume અચળ હોય, એટલે પ્રવાહી phase માટે કે "
                  "moles ની સંખ્યા ન બદલાતી gas પ્રક્રિયા માટે. નહીં તો expansion factor વાળું સ્વરૂપ "
                  "CA = CA0(1 - X)/(1 + eps X) વાપરવું પડે.")},
         {"q": tr("A gas reaction A -> 2R runs at constant pressure. How does the concentration of "
                  "A fall compared with the constant-volume case?",
                  "A -> 2R gas પ્રક્રિયા અચળ pressure પર ચાલે છે. અચળ volume ના કિસ્સા સાથે સરખાવતાં "
                  "A નું concentration કેવી રીતે ઘટે?"),
          "a": tr("Faster. The volume doubles as the reaction goes to completion, so the mixture is "
                  "diluted as well as consumed: CA = CA0(1 - X)/(1 + X) falls below CA0(1 - X). At "
                  "X = 0.5 the constant-volume value is 0.5 CA0 but the true value is 0.333 CA0.",
                  "વધુ ઝડપથી. પ્રક્રિયા પૂરી થતાં volume બમણું થાય, તેથી મિશ્રણ વપરાવા સાથે પાતળું પણ "
                  "થાય: CA = CA0(1 - X)/(1 + X) એ CA0(1 - X) થી નીચે જાય. X = 0.5 પર અચળ volume નું "
                  "મૂલ્ય 0.5 CA0 છે પણ સાચું મૂલ્ય 0.333 CA0 છે.")},
         {"q": tr("Why must an inert gas be subtracted before the pressure is used?",
                  "Pressure વાપરતા પહેલાં inert gas કેમ બાદ કરવો પડે?"),
          "a": tr("Because the gauge reads the total, and the inert contributes a constant pressure "
                  "that does not change with conversion. Left in, it is interpreted as reacting "
                  "material, so the calculated conversion comes out too high and the rate constant "
                  "with it.",
                  "કારણ કે gauge total વાંચે છે, અને inert અચળ pressure ઉમેરે છે જે conversion સાથે "
                  "બદલાતું નથી. તેને રહેવા દેવાથી તે પ્રક્રિયા કરતો દ્રવ્ય ગણાય, તેથી ગણેલું "
                  "conversion અને તેની સાથે rate constant પણ વધારે આવે.")},
     ]},
    {"title": tr("Integrated laws", "Integrated laws"),
     "items": [
         {"q": tr("For which order is the half-life independent of the starting concentration?",
                  "કયા order માટે half-life શરૂઆતના concentration પર આધારિત નથી?"),
          "a": tr("First order, because t1/2 = ln 2/k contains no concentration at all. That is also "
                  "why radioactive decay and many isomerisations are quoted by half-life alone.",
                  "First order, કારણ કે t1/2 = ln 2/k માં concentration જ નથી. તેથી જ radioactive "
                  "decay અને ઘણી isomerisation ફક્ત half-life થી લખાય છે.")},
         {"q": tr("Derive the second order half-life.", "Second order half-life derive કરો."),
          "a": tr("Start from 1/CA - 1/CA0 = k t, put CA = CA0/2 and solve: 2/CA0 - 1/CA0 = k t, so "
                  "1/CA0 = k t and t1/2 = 1/(k CA0). The half-life is inversely proportional to the "
                  "starting concentration.",
                  "1/CA - 1/CA0 = k t થી શરૂ કરો, CA = CA0/2 મૂકો અને ઉકેલો: 2/CA0 - 1/CA0 = k t, "
                  "તેથી 1/CA0 = k t અને t1/2 = 1/(k CA0). Half-life શરૂઆતના concentration ના "
                  "વ્યસ્ત પ્રમાણમાં છે.")},
         {"q": tr("What happens to the integrated laws when CA0 is not equal to CB0 for a "
                  "bimolecular reaction?",
                  "Bimolecular પ્રક્રિયા માટે CA0 અને CB0 જુદા હોય તો integrated laws નું શું થાય?"),
          "a": tr("The simple reciprocal form no longer applies. The correct result contains a "
                  "logarithm, ln(CB CA0/(CA CB0)) = (CB0 - CA0) k t, because the two concentrations "
                  "stay in a fixed relationship that is not a constant ratio. The reciprocal form is "
                  "the limit CA0 = CB0.",
                  "સાદું reciprocal સ્વરૂપ લાગુ ન પડે. સાચા પરિણામમાં logarithm આવે, "
                  "ln(CB CA0/(CA CB0)) = (CB0 - CA0) k t, કારણ કે બંને concentrations નો સંબંધ અચળ "
                  "ગુણોત્તર નથી. Reciprocal સ્વરૂપ એ CA0 = CB0 ની મર્યા છે.")},
     ]},
    {"title": tr("Numbers and traps", "આંકડા અને ભૂલો"),
     "items": [
         {"q": tr("A reaction is 50 % complete in 8 min and 75 % complete in 24 min from the same "
                  "starting concentration. What is the order?",
                  "એ જ શરૂઆતના concentration થી પ્રક્રિયા 8 min માં 50 % અને 24 min માં 75 % પૂરી "
                  "થાય છે. Order કેટલો?"),
          "a": tr("Second order. For first order the 75 % point would come at 2 x 8 = 16 min, and "
                  "for zero order at 1.5 x 8 = 12 min; only second order gives three times the "
                  "half-life time, because t(75 %) = 3/(k CA0) against t1/2 = 1/(k CA0).",
                  "Second order. First order માં 75 % બિંદુ 2 x 8 = 16 min પર આવત, અને zero order માં "
                  "1.5 x 8 = 12 min પર; ફક્ત second order ત્રણ ગણો સમય આપે, કારણ કે t(75 %) = "
                  "3/(k CA0) જ્યારે t1/2 = 1/(k CA0).")},
         {"q": tr("Why is the differential method so sensitive to experimental error?",
                  "Differential method experimental error માટે કેમ સંવેદનશીલ છે?"),
          "a": tr("Because a rate is a slope, and a slope is a difference of two concentrations "
                  "divided by a small time interval. A fixed error in each concentration becomes a "
                  "much larger relative error in the slope, and the error grows as the interval "
                  "shrinks.",
                  "કારણ કે rate એ ઢાળ છે, અને ઢાળ એ બે concentrations નો તફાવત નાના time interval થી "
                  "ભાગ્યો. દરેક concentration માંની અચળ ભૂલ ઢાળમાં ઘણી મોટી સાપેક્ષ ભૂલ બને છે, અને "
                  "interval નાનો થાય તેમ ભૂલ વધે છે.")},
         {"q": tr("What is the unit of k for a third order reaction?", "Third order પ્રક્રિયા માટે "
                  "k નું એકમ શું?"),
          "a": tr("(mol m-3)^(1-3) s-1, that is m6 mol-2 s-1. The unit follows from the balance in "
                  "-rA = k CA^3 with -rA in mol m-3 s-1, and it is the first thing an examiner checks.",
                  "(mol m-3)^(1-3) s-1, એટલે m6 mol-2 s-1. એકમ -rA = k CA^3 માંના સંતુલન પરથી આવે, "
                  "જ્યાં -rA mol m-3 s-1 માં છે, અને પરીક્ષક સૌથી પહેલાં એ જ ચકાસે છે.")},
     ]},
]

# ---------------------------------------------------------------- solved numericals
_PRACTICE = [
    ("A first order reaction: k, half-life and the 90 % time",
     "First order પ્રક્રિયા: k, half-life અને 90 % નો સમય",
     "A first order reaction starts at CA0 = 1.00 mol/L and is left with 0.25 mol/L after 30 min at "
     "constant volume and temperature. Find k, the half-life, and the time needed for 90 % "
     "conversion.",
     "First order પ્રક્રિયા CA0 = 1.00 mol/L થી શરૂ થાય છે અને અચળ volume તથા temperature પર 30 min "
     "પછી 0.25 mol/L બાકી રહે છે. k, half-life અને 90 % conversion માટે જરૂરી સમય શોધો.",
     [h4("Step 1 - the rate constant", "પગલું 1 - rate constant"),
      math("k = (1/t) ln(CA0/CA) = (1/30) ln(1.00/0.25)",
           "  = (1/30) ln 4 = 1.386/30 = 0.0462 min-1"),
      h4("Step 2 - the half-life", "પગલું 2 - half-life"),
      math("t1/2 = ln 2 / k = 0.693/0.0462 = 15.0 min"),
      eq("k = 4.62 x 10-2 min-1,  t1/2 = 15 min"),
      h4("Step 3 - the time for 90 % conversion", "પગલું 3 - 90 % conversion નો સમય"),
      math("X = 0.90:  CA/CA0 = 0.10",
           "t = (1/k) ln(1/0.10) = (1/0.0462) x 2.303 = 49.8 min"),
      eq("t(90 %) = 50 min (3.3 half-lives)"),
      p("Two half-lives take the reaction to 75 %, three to 87.5 %, so 90 % must come a little after "
        "three half-lives - which is exactly what 49.8 min against 45 min shows.",
        "બે half-lives પ્રક્રિયાને 75 % સુધી, ત્રણ 87.5 % સુધી લઈ જાય, તેથી 90 % ત્રણ half-lives પછી "
        "થોડું મોડું આવવું જોઈએ - 45 min સામે 49.8 min એ જ દર્શાવે છે."),
      check("exp(-0.0462 x 49.8) = exp(-2.30) = 0.10, so 10 % of A is left.",
            "exp(-0.0462 x 49.8) = exp(-2.30) = 0.10, તેથી 10 % A બાકી."),
      pit("Writing t1/2 = 0.693 k instead of 0.693/k. The half-life must get shorter as k gets "
          "larger, and the units (min-1 below the line) make that obvious.",
          "t1/2 = 0.693 k લખવું, 0.693/k ને બદલે. k મોટો થાય તેમ half-life નાની થવી જોઈએ, અને "
          "એકમ (min-1 નીચે) એ સ્પષ્ટ કરે છે.")],
     6),
    ("Second order with equal concentrations",
     "સરખા concentrations વાળો second order",
     "A second order reaction A + A -> products starts at CA0 = 0.10 mol/L and has a half-life of "
     "20 min. Find k, the concentration after 40 min, and the conversion at that time.",
     "Second order પ્રક્રિયા A + A -> products CA0 = 0.10 mol/L થી શરૂ થાય છે અને half-life 20 min છે. "
     "k, 40 min પછીનું concentration અને તે સમયનું conversion શોધો.",
     [h4("Step 1 - k from the half-life", "પગલું 1 - half-life પરથી k"),
      math("t1/2 = 1/(k CA0)  ->  k = 1/(t1/2 CA0)",
           "k = 1/(20 x 0.10) = 1/2.0 = 0.50 L mol-1 min-1"),
      h4("Step 2 - the concentration after 40 min", "પગલું 2 - 40 min પછીનું concentration"),
      math("1/CA = 1/CA0 + k t = 1/0.10 + 0.50 x 40",
           "     = 10 + 20 = 30 L/mol"),
      math("CA = 1/30 = 0.0333 mol/L"),
      h4("Step 3 - the conversion", "પગલું 3 - conversion"),
      math("X = 1 - CA/CA0 = 1 - 0.0333/0.10 = 0.667"),
      eq("k = 0.50 L mol-1 min-1,  CA = 3.3 x 10-2 mol/L,  X = 66.7 %"),
      p("Two half-lives of a second order reaction do not give 75 %; they give 67 %, because each "
        "half-life is longer than the one before it (1/kCA0 grows as CA0 falls).",
        "Second order પ્રક્રિયાની બે half-lives 75 % નથી આપતી; તે 67 % આપે છે, કારણ કે દરેક half-life "
        "પાછલી કરતાં લાંબી થાય છે (CA0 ઘટે તેમ 1/kCA0 વધે)."),
      check("Put CA = 0.0333 back: 1/0.0333 = 30, and 10 + 0.5 x 40 = 30. Consistent.",
            "CA = 0.0333 પાછું મૂકો: 1/0.0333 = 30, અને 10 + 0.5 x 40 = 30. સુસંગત."),
      pit("Using t1/2 = 0.693/k for a second order reaction. That number belongs to first order "
          "only; for second order the half-life changes with every run.",
          "Second order પ્રક્રિયા માટે t1/2 = 0.693/k વાપરવું. એ આંકડો ફક્ત first order નો છે; second "
          "order માં half-life દરેક રન સાથે બદલાય છે.")],
     7),
    ("Order and k by the differential method",
     "Differential method થી order અને k",
     "A constant-volume batch gives CA = 1.00, 0.80, 0.60, 0.40 and 0.25 mol/L at t = 0, 5, 13.3, 30 "
     "and 60 min. Find the order and the rate constant by the differential method.",
     "અચળ volume વાળી batch t = 0, 5, 13.3, 30 અને 60 min પર CA = 1.00, 0.80, 0.60, 0.40 અને "
     "0.25 mol/L આપે છે. Differential method થી order અને rate constant શોધો.",
     [h4("Step 1 - rates from the intervals", "પગલું 1 - intervals પરથી rates"),
      math("-rA = -(CA2 - CA1)/(t2 - t1)   at the mean CA:",
           "(1.00-0.80)/5      = 0.040 at CA = 0.90",
           "(0.80-0.60)/8.3    = 0.024 at CA = 0.70",
           "(0.60-0.40)/16.7   = 0.012 at CA = 0.50"),
      h4("Step 2 - the log-log line", "પગલું 2 - log-log રેખા"),
      math("ln(-rA) = -3.22, -3.73, -4.42",
           "ln CA    = -0.105, -0.357, -0.693",
           "slope n = (-4.42 + 3.22)/(-0.693 + 0.105) = (-1.20)/(-0.588) = 2.04"),
      h4("Step 3 - the rate constant", "પગલું 3 - rate constant"),
      math("ln k = ln(-rA) - n ln CA = -3.22 - 2(-0.105) = -3.01",
           "k = exp(-3.01) = 0.049 L mol-1 min-1"),
      eq("order n = 2,  k = 4.9 x 10-2 L mol-1 min-1"),
      p("The order comes out 2.04 rather than 2.00 because each rate is a chord over an interval, "
        "not a true tangent. Report n = 2 and quote k to two figures - the third figure is larger "
        "than the error of the method.",
        "Order 2.04 આવે, 2.00 નહીં, કારણ કે દરેક rate એ interval પરની chord છે, સાચો સ્પર્શક નહીં. "
        "n = 2 લખો અને k બે આંકડામાં આપો - ત્રીજો આંકડો રીતની ભૂલ કરતાં મોટો છે."),
      check("k CA^2 at each row: 0.049 x 0.81 = 0.040, 0.049 x 0.49 = 0.024, 0.049 x 0.25 = 0.012. "
            "All three give back the measured rates.",
            "દરેક હારમાં k CA^2: 0.049 x 0.81 = 0.040, 0.049 x 0.49 = 0.024, 0.049 x 0.25 = 0.012. "
            "ત્રણેય માપેલા rates પાછા આપે છે."),
      pit("Averaging the three k values before checking the order. If the order is wrong, the three "
          "k values will not even be close, and averaging hides the real problem.",
          "Order ચકાસ્યા પહેલાં ત્રણ k ની સરેરાશ લેવી. Order ખોટો હોય તો ત્રણ k એકબીજાની નજીક પણ "
          "નહીં આવે, અને સરેરાશ સાચી સમસ્યા ઢાંકી દે.")],
     8),
    ("Order from half-lives at three concentrations",
     "ત્રણ concentrations પરની half-lives પરથી order",
     "The half-life of a reaction is 25 min at CA0 = 0.80 mol/L, 50 min at 0.40 mol/L and 100 min at "
     "0.20 mol/L. Find the order and k.",
     "પ્રક્રિયાની half-life CA0 = 0.80 mol/L પર 25 min, 0.40 mol/L પર 50 min અને 0.20 mol/L પર "
     "100 min છે. Order અને k શોધો.",
     [h4("Step 1 - the order", "પગલું 1 - order"),
      math("n = 1 + ln(t1/2,2/t1/2,1) / ln(CA0,1/CA0,2)",
           "  = 1 + ln(50/25) / ln(0.80/0.40)",
           "  = 1 + 0.693/0.693 = 2"),
      h4("Step 2 - the rate constant", "પગલું 2 - rate constant"),
      math("n = 2:  k = 1/(t1/2 CA0)",
           "run 1: 1/(25 x 0.80) = 0.050",
           "run 2: 1/(50 x 0.40) = 0.050",
           "run 3: 1/(100 x 0.20) = 0.050"),
      eq("order n = 2,  k = 0.050 L mol-1 min-1"),
      p("All three runs give the same k, which is what a correct order must do. Halving the starting "
        "concentration doubled the half-life every time - the fingerprint of second order.",
        "ત્રણેય રન એક જ k આપે છે, જે સાચો order હોવાનું લક્ષણ છે. શરૂઆતનું concentration અડધું કરતાં "
        "દર વખતે half-life બમણી થઈ - second order ની ઓળખ."),
      check("Prediction: at CA0 = 0.10 mol/L the half-life must be 200 min and k still 0.050. "
            "1/(200 x 0.10) = 0.050.",
            "અનુમાન: CA0 = 0.10 mol/L પર half-life 200 min અને k હજી 0.050 હોવો જોઈએ. "
            "1/(200 x 0.10) = 0.050."),
      pit("Taking the order from one pair and not checking it on the third run. Any two points fit "
          "any two-parameter model; the third run is the test.",
          "એક જોડી પરથી order લઈને ત્રીજી રન પર ન ચકાસવો. કોઈ પણ બે બિંદુ કોઈ પણ બે-parameter model "
          "માં બેસે; ત્રીજી રન એ ચકાસણી છે.")],
     6),
    ("Conversion and k from pressure readings",
     "Pressure વાંચન પરથી conversion અને k",
     "The gas reaction A -> B + C runs in a rigid vessel at 500 K, starting with pure A at "
     "p0 = 1.00 bar. After 20 min the gauge reads 1.60 bar. Find the conversion, the concentration "
     "of A, and k, taking the reaction as first order.",
     "Gas પ્રક્રિયા A -> B + C 500 K પર કઠણ પાત્રમાં ચાલે છે, શરૂઆતમાં શુદ્ધ A p0 = 1.00 bar પર. "
     "20 min પછી gauge 1.60 bar વાંચે છે. Conversion, A નું concentration અને first order ધારીને k "
     "શોધો.",
     [h4("Step 1 - partial pressure of A", "પગલું 1 - A નું partial pressure"),
      math("A -> B + C gives delta/a = +1, so pA = 2pA0 - p",
           "pA = 2(1.00) - 1.60 = 0.40 bar"),
      h4("Step 2 - conversion", "પગલું 2 - conversion"),
      math("X = 1 - pA/pA0 = 1 - 0.40/1.00 = 0.60",
           "check from the total: X = (p - p0)/[(delta/a) pA0] = 0.60/1.00 = 0.60"),
      h4("Step 3 - concentrations", "પગલું 3 - concentrations"),
      math("CA0 = pA0/(RT) = 1.00e5/(8.314 x 500) = 24.1 mol/m3",
           "CA = CA0(1 - X) = 24.1 x 0.40 = 9.6 mol/m3",
           "or directly: CA = pA/(RT) = 0.40e5/(8.314 x 500) = 9.6 mol/m3"),
      h4("Step 4 - the rate constant", "પગલું 4 - rate constant"),
      math("k = (1/t) ln[1/(1 - X)] = (1/20) ln(2.5)",
           "  = 0.916/20 = 0.0458 min-1"),
      eq("X = 60 %,  CA = 9.6 mol/m3,  k = 4.6 x 10-2 min-1"),
      p("The gauge alone gave the conversion, and the conversion alone gave k: no sample was taken. "
        "That is why pressure is the standard measurement for gas-phase batch kinetics.",
        "એકલા gauge એ conversion આપ્યું, અને conversion એ k: કોઈ sample લેવો પડ્યો નહીં. તેથી જ "
        "gas-phase batch kinetics માટે pressure પ્રમાણભૂત માપ છે."),
      check("pA/pA0 must equal CA/CA0: 0.40 and 9.6/24.1 = 0.398. Agreement to two figures.",
            "pA/pA0 એ CA/CA0 બરાબર હોવું જોઈએ: 0.40 અને 9.6/24.1 = 0.398. બે આંકડા સુધી મેળ."),
      pit("Using pA = p0 - p. That would give 1.00 - 1.60 = -0.60 bar, a negative concentration - "
          "the sign is telling you that the total pressure rises as A disappears.",
          "pA = p0 - p વાપરવું. તેથી 1.00 - 1.60 = -0.60 bar આવે, ઋણ concentration - નિશાની જ "
          "કહે છે કે A ઘટે તેમ total pressure વધે છે.")],
     7),
    ("Order from 50 % and 75 % times",
     "50 % અને 75 % ના સમય પરથી order",
     "From CA0 = 2.0 mol/L a reaction reaches 50 % conversion in 8 min and 75 % conversion in 24 min "
     "at the same temperature. Find the order and k.",
     "CA0 = 2.0 mol/L થી પ્રક્રિયા એ જ temperature પર 8 min માં 50 % અને 24 min માં 75 % conversion "
     "પર પહોંચે છે. Order અને k શોધો.",
     [h4("Step 1 - test the three simple orders", "પગલું 1 - ત્રણ સાદા orders ચકાસો"),
      math("zero order :  t(75 %)/t(50 %) = 0.75/0.50 = 1.50",
           "first order:  t(75 %)/t(50 %) = ln4/ln2 = 2.00",
           "second order, CA0 = CB0:  t(50 %) = 1/(kCA0), t(75 %) = 3/(kCA0) -> ratio 3.00"),
      math("measured ratio = 24/8 = 3.00  ->  second order"),
      h4("Step 2 - the rate constant", "પગલું 2 - rate constant"),
      math("k = 1/(t(50 %) x CA0) = 1/(8 x 2.0) = 0.0625 L mol-1 min-1"),
      math("check at 75 %: t = 3/(k CA0) = 3/(0.0625 x 2.0) = 24 min"),
      eq("order n = 2,  k = 6.25 x 10-2 L mol-1 min-1"),
      p("The ratio of two times is enough to name the order because each order has its own "
        "signature ratio, and the ratio is independent of k - a very quick check when the data "
        "consist of two conversions only.",
        "બે સમયનો ગુણોત્તર order કહેવા પૂરતો છે, કારણ કે દરેક order નો પોતાનો ગુણોત્તર છે અને તે k પર "
        "આધારિત નથી - ફક્ત બે conversions હોય ત્યારે તે ખૂબ ઝડપી ચકાસણી છે."),
      check("Split the run into quarter steps with k = 0.0625 and CA0 = 2.0: 0-25 % takes 2.7 min, "
            "25-50 % another 5.3 min, 50-75 % another 16 min. The steps grow (2.7 + 5.3 = 8 and "
            "8 + 16 = 24), exactly as the data show.",
            "k = 0.0625 અને CA0 = 2.0 સાથે રનને ચોથા ભાગમાં વહેંચો: 0-25 % ને 2.7 min, 25-50 % ને "
            "બીજા 5.3 min, 50-75 % ને બીજા 16 min લાગે. પગલાં વધે છે (2.7 + 5.3 = 8 અને "
            "8 + 16 = 24), જે data બતાવે છે તેમ જ."),
      pit("Assuming the 75 % time is one and a half times the 50 % time, which is true only for "
          "zero order. Check the ratio before you use it.",
          "75 % નો સમય 50 % ના ડેઢ ગણો માની લેવો, જે ફક્ત zero order માટે સાચું છે. વાપરતા પહેલાં "
          "ગુणોત્તર ચકાસો.")],
     7),
]

PRACTICE = [(tr(h_en, h_gu), tr(q_en, q_gu), body(*parts), m)
            for (h_en, h_gu, q_en, q_gu, parts, m) in _PRACTICE]

EXAM = [{"q": q, "marks": m} for _, q, _, m in PRACTICE]
PRACTICE_ANSWERS = [a for _, _, a, _ in PRACTICE]

SOURCES = [
    ("GTU DI05005031 Chemical Reaction Engineering syllabus (uploaded PDF, w.e.f. 2026-27)",
     "https://syllabus.gtu.ac.in/"),
    ("Octave Levenspiel - Chemical Reaction Engineering, 3rd ed., Wiley (chapter 3: interpretation "
     "of batch reactor data, differential and integral methods)", "https://www.wiley.com/"),
    ("H. Scott Fogler - Essentials of Chemical Reaction Engineering, 4th ed., Prentice Hall "
     "(chapter 5: conversion and reactor sizing; chapter 6: pressure data)", "https://www.pearson.com/"),
    ("NPTEL Chemical Reaction Engineering lectures - kinetics from batch data", "https://nptel.ac.in/"),
]
