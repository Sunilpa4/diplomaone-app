"""DI05005031 Unit 3, part A: section 3.1 - the three methods for reading batch reactor data."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from subject_DI05005031 import tr  # noqa: E402
from content_DI05005031_lib import (p, h4, ul, ol, table, math, eq, why, check, pit, derive,
                                    card)  # noqa: E402

NOTES_A = []

NOTES_A.append({
    "title": tr("3.1 Reading batch data: the differential and integral routes",
                "3.1 Batch data વાંચવું: differential અને integral રીતો"),
    "items": [
        card(
            "One table of data, three roads to the rate equation",
            "એક કોષ્ટક, rate equation સુધીની ત્રણ રીતો",
            p("A batch experiment gives one table: concentration against time, at one temperature. "
              "Three methods turn that table into a rate equation, and all three answer the same two "
              "questions - what is the order n, and what is the rate constant k:",
              "Batch experiment એક જ કોષ્ટક આપે છે: એક temperature પર concentration અને time. ત્રણ "
              "રીતો એ કોષ્ટકને rate equation માં ફેરવે છે, અને ત્રણેય એ જ બે પ્રશ્નોના જવાબ આપે છે - "
              "order n કેટલો અને rate constant k કેટલો:"),
            table([tr("Method", "રીત"), tr("What you plot", "શું દોરો"),
                   tr("What the plot gives", "પ્લોટ શું આપે")],
                  [[tr("Differential", "Differential"),
                    tr("-rA from the slope of C against t, then ln(-rA) against ln CA",
                       "C અને t ના ઢાળ પરથી -rA, પછી ln(-rA) અને ln CA"),
                    tr("slope = n, intercept = ln k", "ઢાળ = n, intercept = ln k")],
                   [tr("Integral", "Integral"),
                    tr("the integrated law for a guessed n, in its straight-line form",
                       "ધારેલા n માટેનો integrated law, સીધી રેખાના સ્વરૂપમાં"),
                    tr("a straight line proves n, its slope is k", "સીધી રેખા n સાબિત કરે, ઢાળ k આપે")],
                   [tr("Half-life", "Half-life"),
                    tr("log t1/2 against log CA0", "log t1/2 અને log CA0"),
                    tr("slope = 1 - n, then k from one half-life",
                       "ઢાળ = 1 - n, પછી એક half-life પરથી k")]]),
            math("-rA = k CA^n            the one law all three methods test",
                 "differential:  ln(-rA) = ln k + n ln CA",
                 "integral:      CA^(1-n) - CA0^(1-n) = (n-1) k t",
                 "half-life:     t1/2 = (2^(n-1) - 1)/((n-1) k CA0^(n-1))"),
            h4("The order of work that never fails", "જે ક્રમ કદી નિષ્ફળ ન જાય"),
            ol(("Check the data first: is the temperature constant, is the volume constant, is "
                "there a mole change?",
                "પહેલા data ચકાસો: temperature અચળ છે? volume અચળ છે? mole change છે?"),
               ("Find the order by two independent methods and accept it only if they agree.",
                "order બે સ્વતંત્ર રીતોથી શોધો અને બંને મળે તો જ સ્વીકારો."),
               ("Take k from the method that uses all the points, not from one interval.",
                "k એ રીતમાંથી લો જે બધા બિંદુઓ વાપરે, એક interval પરથી નહીં.")),
            p("The three methods are not alternatives to memorise; they are cross-checks. A report "
              "that says \"order 2 by the integral method, order 2 by half-lives\" is worth far more "
              "than one that says \"order 2\" with a single plot behind it.",
              "ત્રણ રીતો યાદ કરવા માટેના વિકલ્પો નથી; તે એકબીજાની ચકાસણી છે. \"integral method થી "
              "order 2, half-lives થી પણ order 2\" કહેતો report એવા report કરતાં ઘણો કિંમતી છે જે "
              "એક જ પ્લોટ પાછળ \"order 2\" કહે."),
            why("Every method is a different way of testing the same power law, -rA = k CA^n. The "
                "differential method tests it after taking logarithms, the integral method tests it "
                "after integrating, and the half-life method tests it at one particular conversion. "
                "Same law, three windows.",
                "દરેક રીત એ જ power law -rA = k CA^n ચકાસવાની જુદી રીત છે. Differential method તેને "
                "logarithm લીધા પછી ચકાસે છે, integral method integrate કર્યા પછી, અને half-life "
                "method એક ખાસ conversion પર. એક જ law, ત્રણ બારી."),
            check("If you are given only three points and no time to waste, use the integral method: "
                  "one plot per guessed order tells you at once whether the guess was right.",
                  "ફક્ત ત્રણ બિંદુ અને સમય ઓછો હોય તો integral method વાપરો: દરેક ધારેલા order માટે "
                  "એક પ્લોટ તરત કહે કે ધારણા સાચી હતી કે નહીં."),
            pit("Mixing data from two runs. If the temperature drifted between runs, the two halves "
                "of the table belong to two different k, and no method will give a clean answer.",
                "બે રનના data ભેળવવા. રન વચ્ચે temperature બદલાયું હોય તો કોષ્ટકના બે ભાગ બે જુદા k ના "
                "છે, અને કોઈ રીત સ્વચ્છ જવાબ નહીં આપે."),
            diagram="u3_paths",
            syllabus_item="3.1",
        ),
        card(
            "The differential method: differentiate, then take logarithms",
            "Differential method: પહેલા derivative, પછી logarithm",
            p("Write the power law, take logarithms, and the problem becomes a straight line:",
              "Power law લખો, logarithm લો, અને સમસ્યા સીધી રેખા બની જાય છે:"),
            math("-rA = k CA^n",
                 "ln(-rA) = ln k + n ln CA   <- straight line in ln CA"),
            h4("The three steps", "ત્રણ પગલાં"),
            ol(("Plot CA against t and draw a tangent at each concentration; the slope of the "
                "tangent, with its sign removed, is -rA at that CA.",
                "CA અને t નો પ્લોટ દોરો અને દરેક concentration પર સ્પર્શક દોરો; સ્પર્શકનો ઢાળ, નિશાની "
                "કાઢી નાખ્યા પછી, તે CA પરનો -rA છે."),
               ("Plot ln(-rA) against ln CA.", "ln(-rA) અને ln CA નો પ્લોટ દોરો."),
               ("Read the slope as the order and the intercept as ln k.",
                "ઢાળને order અને intercept ને ln k વાંચો.")),
            h4("When the data are a table, not a curve", "Data કોષ્ટક હોય, વક્ર નહીં"),
            p("Two neighbouring points give the rate at the mid-point of the interval without drawing "
              "anything. Use the central difference for interior points and the forward difference at "
              "the ends:",
              "પાસેના બે બિંદુઓ interval ના મધ્યબિંદુ પરનો rate આપે છે, કંઈ દોરવાની જરૂર નહીં. "
              "વચ્ચેના બિંદુઓ માટે central difference અને છેડે forward difference વાપરો:"),
            derive("-rA(mid) = -(CA2 - CA1) / (t2 - t1)",
                   "assign that rate to the mean concentration (CA1 + CA2)/2",
                   "repeat for every interval, then plot ln(-rA) against ln CA"),
            h4("A worked table", "ઉકેલેલું કોષ્ટક"),
            p("A batch reactor at constant volume, constant temperature, gives the table below. The "
              "order is not obvious from CA alone:",
              "અચળ volume અને temperature પરનો batch reactor નીચેનું કોષ્ટક આપે છે. ફક્ત CA જોઈને "
              "order સ્પષ્ટ થતો નથી:"),
            table([tr("t, min", "t, min"), tr("CA, mol/L", "CA, mol/L"),
                   tr("mean CA", "mean CA"), tr("-rA, mol L-1 min-1", "-rA, mol L-1 min-1")],
                  [["0", "1.00", "-", "-"],
                   ["5", "0.80", "0.90", "0.040"],
                   ["13.3", "0.60", "0.70", "0.024"],
                   ["30", "0.40", "0.50", "0.012"],
                   ["60", "0.25", "-", "-"]]),
            math("ln(-rA):  -3.22   -3.73   -4.42",
                 "ln CA :   -0.105  -0.357  -0.693",
                 "slope = (-4.42 + 3.22) / (-0.693 + 0.105) = 2.04",
                 "intercept: ln k = -3.22 - 2(-0.105) = -3.01 -> k = 0.049"),
            eq("order n = 2,  k = 0.049 L mol-1 min-1"),
            p("The slope of 2.04 is an order of 2 within the scatter of a hand-drawn tangent. Report "
              "it as 2 and say that the data support a second order law between 0.25 and 1.0 mol/L.",
              "2.04 નો ઢાળ હાથે દોરેલા સ્પર્શકના scatter માં order 2 જ છે. તેને 2 લખો અને કહો કે "
              "0.25 થી 1.0 mol/L વચ્ચેનો data second order law ને ટેકો આપે છે."),
            why("Differentiation is the most direct test because it never assumes a form: the power "
                "law itself becomes linear. It is also the most sensitive to noise, because a small "
                "error in CA becomes a large error in the slope.",
                "Differentiation સૌથી સીધી ચકાસણી છે કારણ કે તે કોઈ સ્વરૂપ ધારતું નથી: power law પોતે "
                "રેખીય બની જાય છે. તે noise માટે પણ સૌથી સંવેદનશીલ છે, કારણ કે CA ની નાની ભૂલ ઢાળમાં "
                "મોટી ભૂલ બની જાય છે."),
            check("A second order law must also give k CA^2 = -rA at every row: 0.049 x 0.81 = 0.040, "
                  "0.049 x 0.49 = 0.024, 0.049 x 0.25 = 0.012 - all three rows agree.",
                  "Second order law એ દરેક હારમાં k CA^2 = -rA આપવું જોઈએ: 0.049 x 0.81 = 0.040, "
                  "0.049 x 0.49 = 0.024, 0.049 x 0.25 = 0.012 - ત્રણેય હાર મળે છે."),
            pit("Drawing one tangent at t = 0 and calling it the order. The initial slope gives one "
                "rate at one concentration; an order needs at least three points spread over the "
                "concentration range.",
                "t = 0 પર એક સ્પર્શક દોરીને તેને order કહેવું. શરૂઆતનો ઢાળ એક concentration પર એક "
                "rate આપે છે; order માટે concentration ની પરાસમાં ઓછામાં ઓછા ત્રણ બિંદુ જોઈએ."),
            diagram="u3_diff",
            syllabus_item="3.1",
        ),
    ],
})

NOTES_A.append({
    "title": tr("3.1 The half-life route and how to choose between the three",
                "3.1 Half-life રીત અને ત્રણમાંથી કઈ પસંદ કરવી"),
    "items": [
        card(
            "The integral method: guess, integrate, then look for a straight line",
            "Integral method: ધારો, integrate કરો, પછી સીધી રેખા શોધો",
            p("The integral method works the other way round. Guess an order, integrate the rate law, "
              "and plot the combination of concentrations that should then be linear in time. If the "
              "plot is straight, the guess was right and the slope is k; if it bends, try the next "
              "order.",
              "Integral method ઊલટી રીતે કામ કરે છે. order ધારો, rate law integrate કરો, અને "
              "concentration નું એ સંયોજન દોરો જે ત્યારે time સાથે રેખીય થવું જોઈએ. પ્લોટ સીધો હોય તો "
              "ધારણા સાચી અને ઢાળ k છે; વળે તો બીજો order અજમાવો."),
            table([tr("Guessed order", "ધારેલો order"), tr("Integrate -dCA/dt = k CA^n", "integrate કરો"),
                   tr("Plot this against t", "t સામે આ દોરો")],
                  [[tr("0", "0"), tr("CA0 - CA = k t", "CA0 - CA = k t"), tr("CA", "CA")],
                   [tr("1", "1"), tr("ln(CA0/CA) = k t", "ln(CA0/CA) = k t"), tr("ln CA", "ln CA")],
                   [tr("2", "2"), tr("1/CA - 1/CA0 = k t", "1/CA - 1/CA0 = k t"), tr("1/CA", "1/CA")],
                   [tr("3", "3"), tr("1/CA^2 - 1/CA0^2 = 2 k t", "1/CA^2 - 1/CA0^2 = 2 k t"),
                    tr("1/CA^2", "1/CA^2")]]),
            h4("The same table, tested three times", "એ જ કોષ્ટક, ત્રણ વાર ચકાસ્યું"),
            p("For the five points of the previous card, the three test functions give:",
              "પાછલા card ના પાંચ બિંદુઓ માટે ત્રણ test function આપે છે:"),
            math("t:      0     5    13.3    30    60",
                 "CA:    1.00  0.80  0.60  0.40  0.25",
                 "ln CA:  0.00 -0.22 -0.51 -0.92 -1.39",
                 "1/CA:   1.00  1.25  1.67  2.50  4.00"),
            math("steps in 1/CA per minute:",
                 "(1.25-1.00)/5 = 0.050        (1.67-1.25)/8.3 = 0.050",
                 "(2.50-1.67)/16.7 = 0.050     (4.00-2.50)/30 = 0.050"),
            p("The differences of 1/CA are constant, so 1/CA against t is a straight line and the "
              "order is 2. The same steps in ln CA (0.044, 0.035, 0.025, 0.016 per minute) fall away, "
              "so first order is ruled out; the steps in CA themselves (0.040, 0.024, 0.012, 0.010) "
              "also fall, so zero order is ruled out.",
              "1/CA ના તફાવત અચળ છે, તેથી 1/CA અને t સીધી રેખા છે અને order 2 છે. ln CA માં એ જ "
              "પગલાં (પ્રતિ મિનિટ 0.044, 0.035, 0.025, 0.016) ઘટે છે, તેથી first order નકારાય; CA માં "
              "પગલાં (0.040, 0.024, 0.012, 0.010) પણ ઘટે છે, તેથી zero order નકારાય."),
            eq("order 2,  k = 0.050 L mol-1 min-1 (differential gave 0.049)"),
            why("Integration smooths the data: a small error in one concentration changes the slope "
                "of the test plot only slightly, which is why the integral method is the one used on "
                "noisy plant data. The price is that you must guess, and a wrong guess is only "
                "noticed when the plot bends.",
                "Integration data ને સરખું કરે છે: એક concentration માંની નાની ભૂલ test plot ના ઢાળને "
                "થોડો જ બદલે છે, તેથી noisy plant data પર integral method વપરાય છે. કિંમત એ છે કે "
                "ધારવું પડે, અને ખોટી ધારણા પ્લોટ વળે ત્યારે જ દેખાય."),
            check("With k = 0.050, the time to reach 0.25 mol/L is (4.00 - 1.00)/0.050 = 60 min, "
                  "which is the last row of the table.",
                  "k = 0.050 સાથે 0.25 mol/L સુધી પહોંચવાનો સમય (4.00 - 1.00)/0.050 = 60 min છે, જે "
                  "કોષ્ટકની છેલ્લી હાર છે."),
            pit("Testing only the order you expect. Plot all three, look at which one is straight, "
                "and let the data choose - examiners award the marks for the comparison, not for the "
                "final number.",
                "ફક્ત અપેક્ષિત order જ ચકાસવો. ત્રણેય દોરો, કયો સીધો છે તે જુઓ, અને data ને પસંદ "
                "કરવા દો - પરીક્ષક સરખામણી માટે ગુણ આપે છે, અંતિમ આંકડા માટે નહીં."),
            diagram="u3_integral_test",
            syllabus_item="3.1",
        ),
        card(
            "The half-life method: one number per run",
            "Half-life method: દરેક રન માટે એક જ આંકડો",
            p("Start a fresh batch at a different CA0 and measure how long it takes to fall to half. "
              "The way that half-life changes with CA0 is the order, because for -rA = k CA^n:",
              "જુદા CA0 પર નવો batch શરૂ કરો અને અડધું થવા માટે કેટલો સમય લાગે તે માપો. CA0 સાથે "
              "half-life કેવી રીતે બદલાય તે જ order છે, કારણ કે -rA = k CA^n માટે:"),
            derive("t1/2 = (2^(n-1) - 1) / ((n-1) k CA0^(n-1))     for n not equal to 1",
                   "t1/2 = ln 2 / k                              for n = 1",
                   "take logarithms: log t1/2 = const + (1 - n) log CA0",
                   "so a plot of log t1/2 against log CA0 has slope (1 - n)"),
            math("two runs are enough:  n = 1 + ln(t1/2 second / t1/2 first) / ln(CA0 first / CA0 second)",
                 "check: n = 2 -> t1/2 proportional to 1/CA0;  n = 0 -> t1/2 proportional to CA0"),
            h4("Worked example", "ઉકેલેલું ઉદાહરણ"),
            p("Two runs of the same reaction at the same temperature give t1/2 = 20 min at CA0 = 1.00 "
              "mol/L and t1/2 = 40 min at CA0 = 0.50 mol/L. Find the order and k.",
              "એ જ temperature પરની બે રન આપે છે: CA0 = 1.00 mol/L પર t1/2 = 20 min અને "
              "CA0 = 0.50 mol/L પર t1/2 = 40 min. order અને k શોધો."),
            math("n = 1 + ln(40/20) / ln(1.00/0.50)",
                 "  = 1 + 0.693/0.693 = 2",
                 "for n = 2:  k = 1/(t1/2 CA0) = 1/(20 x 1.00) = 0.050",
                 "check with the second run: 1/(40 x 0.50) = 0.050  (same k)"),
            eq("order 2,  k = 0.050 L mol-1 min-1"),
            p("Halving the starting concentration doubled the half-life; that doubling is the "
              "signature of second order. For a first order reaction the half-life would not have "
              "moved at all, and for a zero order reaction it would have halved.",
              "શરૂઆતનું concentration અડધું કરતાં half-life બમણી થઈ; એ બમણું થવું second order ની "
              "ઓળખ છે. First order પ્રક્રિયામાં half-life જરાય બદલાત નહીં, અને zero order માં તે અડધી "
              "થઈ જાત."),
            why("The half-life method needs no calculus at all: each run gives a single number, and "
                "the order is read from how those numbers change. That is why it is the method of "
                "choice for a quick laboratory screening, and why it is so easy to mark in an "
                "examination.",
                "Half-life method ને calculus ની જરૂર જ નથી: દરેક રન એક જ આંકડો આપે છે, અને એ આંકડા "
                "કેવી રીતે બદલાય તેમાંથી order વંચાય છે. તેથી જ ઝડપી laboratory screening માટે તે "
                "પસંદગીની રીત છે, અને તેથી જ પરીક્ષામાં તેના ગુણ આપવા સહેલા છે."),
            check("For this reaction a third run at CA0 = 0.25 mol/L must give t1/2 = 80 min. If it "
                  "does not, the order is not 2 - or the temperature moved between runs.",
                  "આ પ્રક્રિયા માટે CA0 = 0.25 mol/L પર ત્રીજી રન t1/2 = 80 min આપવી જોઈએ. ન આપે તો "
                  "order 2 નથી - અથવા રન વચ્ચે temperature બદલાયું છે."),
            pit("Using a fractional life without adjusting the formula. The 3/4 life is not 1.5 "
                "times the half-life for every order; the half-life itself has a different "
                "concentration dependence for each order, so always convert to a fraction you can "
                "derive.",
                "fractional life ને સૂત્ર બદલ્યા વગર વાપરવું. દરેક order માટે 3/4 life એ half-life ના "
                "1.5 ગણી હોતી નથી; half-life ની concentration પરની અસર દરેક order માટે જુદી હોય છે, "
                "તેથી હંમેશા એવા fraction માં ફેરવો જેનું સૂત્ર તમે derive કરી શકો."),
            diagram="u3_halflife",
            syllabus_item="3.1",
        ),
    ],
})
