"""DI02000021 Engineering Mathematics - Unit 4: Differential Equations.

GTU 4.1-4.3, 7 h, 17 %, 12 marks, CO4: concept, order and degree, solution by the variable separable
method, and the solution of a first-order linear equation with an integrating factor.
"""
from subject_DI02000021 import tr as _tr


class Txt(dict):
    """An English-only text node that can be concatenated with a plain string."""

    def __add__(self, other):
        tail = other.get("en") if isinstance(other, dict) else str(other)
        return Txt({"en": self["en"] + tail})

    def __radd__(self, other):
        head = other.get("en") if isinstance(other, dict) else str(other)
        return Txt({"en": head + self["en"]})


def tr(s):
    return Txt({"en": s})


def p(x):
    return f"<p>{x}</p>"


def h4(x):
    return f"<h4>{x}</h4>"


def ul(*items):
    return "<ul>" + "".join(f"<li>{i}</li>" for i in items) + "</ul>"


def ol(*items):
    return "<ol>" + "".join(f"<li>{i}</li>" for i in items) + "</ol>"


def table(head, rows):
    return ("<table><tr>" + "".join(f"<th>{h}</th>" for h in head) + "</tr>"
            + "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in rows) + "</table>")


def sc(q, a):
    return f'<details class="self-check"><summary>{q}</summary><p>{a}</p></details>'


def card(heading, body, diagram=None, examples=None, syllabus_item=None):
    item = {"h": tr(heading), "body": tr(body)}
    if diagram:
        item["diagram"] = diagram
    if examples:
        item["examples"] = examples
    if syllabus_item:
        item["syllabus_item"] = syllabus_item
    return item


SOURCES = [
    ("GTU DI02000021, Engineering Mathematics, Semester 2, BSC (uploaded syllabus)",
     "https://syllabus.gtu.ac.in/"),
    ("Khan Academy - differential equations: separable and first-order linear",
     "https://www.khanacademy.org/math/differential-equations"),
    ("OpenStax - Calculus Volume 2, chapter 4 (Differential Equations)",
     "https://openstax.org/details/books/calculus-volume-2"),
    ("MIT OCW 18.03 - solving first-order linear equations",
     "https://ocw.mit.edu/courses/18-03-differential-equations-spring-2010/"),
    ("B. S. Grewal - Elementary Engineering Mathematics (Khanna Publishers)",
     "https://www.khannapublishers.in/"),
]

NOTES = [
    {"title": tr("1. What a Differential Equation Is"),
     "items": [
         card("1.1 An equation with a derivative in it",
              h4("Definition")
              + p("A <b>differential equation</b> (DE) is an equation that contains derivatives of an "
                  "unknown function. Solving it means finding that function.")
              + p("Ordinary examples: dy/dx = 2x, dy/dx + y = eˣ, d²y/dx² + y = 0.")
              + h4("Why engineering needs them")
              + p("Almost every law of engineering is written as a rate: cooling is a rate of "
                  "temperature change, a capacitor charges at a rate set by the current, a falling body "
                  "accelerates at a rate set by gravity. Solving the DE turns the law into a formula "
                  "you can evaluate.")
              + h4("What a solution looks like")
              + p("A solution is a function y(x) - not a number - that satisfies the equation "
                  "identically when substituted. For dy/dx = 2x the solution is y = x² + c.")
              + h4("Common mistake")
              + p("Treating the derivative as a fraction to be simplified away before separating the "
                  "variables. dy/dx behaves like a fraction only when the variables are separated."),
              examples=["de4"], syllabus_item="4.1"),
         card("1.2 Order and degree",
              h4("Order")
              + p("The <b>order</b> is the order of the highest derivative present: dy/dx makes it "
                  "first order, d²y/dx² makes it second order.")
              + h4("Degree")
              + p("The <b>degree</b> is the power of that highest derivative after the equation has "
                  "been cleared of fractions and radicals in the derivatives.")
              + h4("Examples")
              + table(["Equation", "Order", "Degree"],
                      [("dy/dx + y = x", "1", "1"),
                       ("(dy/dx)³ + y = x²", "1", "3"),
                       ("d²y/dx² + 3(dy/dx)² = x", "2", "1"),
                       ("d²y/dx² + y² = 0", "2", "1")])
              + h4("Common mistake")
              + p("Reading the degree from the wrong term. In d²y/dx² + 3(dy/dx)² = x the order is 2, "
                  "so the degree is the power of d²y/dx², which is 1 - the square on dy/dx is "
                  "irrelevant."),
              "d1_order", examples=["de1", "de2"], syllabus_item="4.1"),
         card("1.3 General and particular solutions",
              h4("General solution")
              + p("Solving a first-order DE produces one arbitrary constant, so the answer is a family "
                  "of curves: y = c e^(−x) for dy/dx = −y, one curve for every c.")
              + h4("Particular solution")
              + p("One extra condition - usually y = y₀ when x = 0 - fixes c and selects a single "
                  "curve. The condition must match the order: one condition for a first-order DE, two "
                  "for a second-order one.")
              + h4("Singleton and singular solutions")
              + p("A <b>singleton</b> solution has no arbitrary constant at all; a curve that cannot be "
                  "obtained from the general family is called <b>singular</b>. For this unit only "
                  "general and particular solutions matter.")
              + h4("Common mistake")
              + p("Calling y = c e^(−x) 'the' solution. Without a condition it is the general solution, "
                  "and the constant must stay."),
              "d5_family", examples=["de11"], syllabus_item="4.1"),
         card("1.4 Verifying a solution",
              h4("The test")
              + p("Substitute y and its derivatives into the equation. If both sides come out equal for "
                  "every x, the function is a solution - there is nothing else to check.")
              + h4("Worked example")
              + p("Does y = e^(2x) solve y′ − 2y = 0? Here y′ = 2e^(2x), so y′ − 2y = 2e^(2x) − "
                  "2e^(2x) = 0 for every x. Yes.")
              + h4("With two constants")
              + p("y = A cos x + B sin x gives y′ = −A sin x + B cos x and y″ = −y, so y″ + y = 0 for "
                  "any A and B - that is why the second-order equation has two constants.")
              + h4("Why it matters")
              + p("Verification is the fastest way to earn full marks when time is short: it proves an "
                  "answer without re-deriving it."),
              examples=["de5"], syllabus_item="4.1"),
     ]},

    {"title": tr("2. Forming and Classifying Equations"),
     "items": [
         card("2.1 Forming a DE by eliminating constants",
              h4("Method")
              + ol("Write the family with its arbitrary constant(s).",
                   "Differentiate as many times as there are constants.",
                   "Eliminate the constants between the original equation and the derivatives.")
              + h4("Worked example")
              + p("From y = cx², differentiation gives y′ = 2cx. Dividing, c = y′/(2x), and "
                  "substituting back gives y = (y′/(2x))x² = xy′/2, that is <b>x y′ − 2y = 0</b>.")
              + h4("One constant, one differentiation")
              + p("From y = a e^(2x) we get y′ = 2a e^(2x) = 2y, so <b>y′ = 2y</b> - the constant has "
                  "disappeared because it cancels.")
              + h4("Common mistake")
              + p("Differentiating twice when there is only one constant. Each constant needs exactly "
                  "one differentiation."),
              examples=["de6", "de7"], syllabus_item="4.1"),
         card("2.2 First order and first degree: what this unit solves",
              h4("The shape")
              + p("Every equation in this unit is first order and first degree, so it can be written as "
                  "<b>dy/dx = f(x, y)</b> or in the differential form M dx + N dy = 0.")
              + h4("Two methods only")
              + ul("Variable separable: the right side factorises into an x-part times a y-part.",
                   "Linear: the equation is dy/dx + P(x) y = Q(x), with y and dy/dx to the first power.")
              + h4("Example of each")
              + p("dy/dx = x²/y is separable. dy/dx + 2y = eˣ is linear. (dy/dx)² = x + y is first "
                  "order but second degree, so it is outside this syllabus.")
              + h4("Common mistake")
              + p("Starting to solve before deciding which of the two shapes the equation has. One look "
                  "at the form saves the whole attempt."),
              examples=["de3"], syllabus_item="4.1"),
         card("2.3 Notation you will meet",
              h4("Three ways to write the same thing")
              + table(["Notation", "Meaning"],
                      [("dy/dx or y′", "derivative of y with respect to x"),
                       ("M dx + N dy = 0", "differential form, convenient for separation"),
                       ("dy/dx + P y = Q", "the linear standard form")])
              + h4("Reading the differential form")
              + p("From (x + 1) dy = y dx you can move straight to dy/y = dx/(x + 1) - no rearrangement "
                  "needed. That is the value of writing the equation with both differentials.")
              + h4("Independent variable")
              + p("In dy/dt the independent variable is t (often time). The method is identical; only "
                  "the letter changes, so do not panic when a physics question uses t or T.")
              + h4("Common mistake")
              + p("Mixing variables mid-solution, e.g. integrating an expression in y with respect to x. "
                  "Keep one variable per side until the integration is done."),
              examples=["de1"], syllabus_item="4.1"),
         card("2.4 Turning a word problem into an equation",
              h4("The translation table")
              + table(["The words", "The mathematics"],
                      [("rate of change of y", "dy/dt"),
                       ("proportional to y", "dy/dt = k y"),
                       ("proportional to the excess over the surroundings", "dT/dt = −k (T − T₀)"),
                       ("proportional to the amount present", "dy/dt = k y"),
                       ("initially / at t = 0", "y(0) = the starting value")])
              + h4("Three steps")
              + ol("Name the unknown and its rate - the variables and units come from the wording.",
                   "Write the law as an equation with a constant of proportionality k.",
                   "Note the initial condition, then solve and use it to fix c.")
              + h4("Common mistake")
              + p("Forgetting that k may be negative. In cooling the temperature falls towards the "
                  "room, so the sign must make dT/dt negative when T is above the room."),
              syllabus_item="4.1"),
     ]},

    {"title": tr("3. The Variable Separable Method"),
     "items": [
         card("3.1 The idea: split x from y",
              h4("When it works")
              + p("If the equation can be written as dy/dx = f(x) · g(y), the variables separate: "
                  "divide by g(y) and multiply by dx to get dy/g(y) = f(x) dx.")
              + h4("Worked example")
              + p("dy/dx = x/y gives y dy = x dx. Integrating, y²/2 = x²/2 + c₁, that is "
                  "<b>y² = x² + c</b> - one constant, absorbed on one side.")
              + h4("Why the constant appears only once")
              + p("Each side produces its own constant, but two constants combine into one. Writing c "
                  "once, on one side, is the accepted form.")
              + h4("Common mistake")
              + p("Separating only one term in a sum. dy/dx = x + y does not separate; dy/dx = xy does."),
              "d2_separable", examples=["de8"], syllabus_item="4.2"),
         card("3.2 Worked examples with powers",
              h4("Example 1")
              + p("dy/dx = x²/y: separate to y dy = x² dx, integrate to y²/2 = x³/3 + c, so "
                  "<b>y² = 2x³/3 + c</b>.")
              + h4("Example 2")
              + p("dy/dx = y/x: separate to dy/y = dx/x, integrate to log|y| = log|x| + c = log|x| + "
                  "log C, so <b>y = Cx</b> - straight lines through the origin.")
              + h4("Why log C instead of c")
              + p("Writing the constant as log C lets the logs combine into a single logarithm, which "
                  "then removes the log altogether. It is a legal step because C is still arbitrary.")
              + h4("Common mistake")
              + p("Leaving the answer as log y = log x + c when a clean closed form is asked for. "
                  "Exponentiate at the end."),
              examples=["de9", "de12"], syllabus_item="4.2"),
         card("3.3 Exponential and logarithmic forms",
              h4("Example 1")
              + p("dy/dx = 2xy: dy/y = 2x dx, so log|y| = x² + c and <b>y = C e^(x²)</b>.")
              + h4("Example 2")
              + p("dy/dx = e^(x+y): the right side is eˣ eʸ, so e^(−y) dy = eˣ dx. Integrating, "
                  "−e^(−y) = eˣ + c.")
              + h4("Reading the result")
              + p("The same idea handles dy/dx = e^(x−y) (write eˣ/eʸ and cross-multiply) and "
                  "dy/dx = aˣ y, so do not memorise cases - factor, then split.")
              + h4("Common mistake")
              + p("Treating e^(x+y) as e^x + e^y. The exponent law is a product, and only a product "
                  "separates."),
              examples=["de13", "de11"], syllabus_item="4.2"),
         card("3.4 Trigonometric and rational forms",
              h4("Example 1")
              + p("dy/dx = (1 + y²)/(1 + x²): dy/(1 + y²) = dx/(1 + x²), so "
                  "<b>tan⁻¹y = tan⁻¹x + c</b>.")
              + h4("Example 2")
              + p("dy/dx = x(y² + 1): dy/(1 + y²) = x dx, so tan⁻¹y = x²/2 + c. With y(0) = 1, "
                  "c = tan⁻¹1 = π/4, giving y = tan(x²/2 + π/4).")
              + h4("Recognising the standard integrals")
              + p("These answers use ∫ dy/(1 + y²) = tan⁻¹y and ∫ dy/y = log|y|. Both are standard "
                  "forms from the integration table, so the separable step usually reduces a DE to a "
                  "table integral.")
              + h4("Common mistake")
              + p("Forgetting the inverse tangent is in radians when a numerical value is substituted."),
              examples=["de10", "de15"], syllabus_item="4.2"),
     ]},

    {"title": tr("4. Initial Conditions and Applications"),
     "items": [
         card("4.1 Fixing the constant with an initial condition",
              h4("Method")
              + ol("Solve the DE to get the general solution with c.",
                   "Put x = 0 and y = y₀ (or the given pair) into the general solution.",
                   "Solve for c and write the particular solution.")
              + h4("Worked example")
              + p("Solve dy/dx = y cos x with y(0) = 1. Separating: log y = sin x + c, so y = C e^(sin "
                  "x). At x = 0, 1 = C e⁰ = C, hence <b>y = e^(sin x)</b>.")
              + h4("Check")
              + p("Differentiating gives y cos x, and y(0) = e⁰ = 1, so both the DE and the condition "
                  "hold.")
              + h4("Common mistake")
              + p("Substituting the condition before integrating. The constant exists only after the "
                  "integration step."),
              examples=["de14"], syllabus_item="4.2"),
         card("4.2 Growth and decay",
              h4("The model")
              + p("When a quantity changes at a rate proportional to itself, dy/dt = k y, the solution "
                  "is <b>y = y₀ e^(kt)</b>. Positive k is growth, negative k is decay.")
              + h4("Doubling time")
              + p("For growth, y = 2y₀ when e^(kt) = 2, that is t = log 2/k. So k = log 2/(doubling "
                  "time); for a doubling time of 5 hours, k = log 2/5 ≈ 0.1386 per hour.")
              + h4("Halving time")
              + p("For decay, e^(kt) = 1/2 gives t = log 2/|k| - the same number, a useful symmetry.")
              + h4("Reading the units")
              + p("k carries 'per hour' or 'per second', so kt is dimensionless. If kt were not "
                  "dimensionless the exponential would be meaningless, which is a quick way to catch a "
                  "units slip."),
              examples=["de16"], syllabus_item="4.2"),
         card("4.3 Newton's law of cooling",
              h4("The law")
              + p("The rate of cooling is proportional to the difference between the body and its "
                  "surroundings: dT/dt = −k (T − T₀), where T₀ is the room temperature.")
              + h4("The solution")
              + p("Separating and integrating gives <b>T = T₀ + (T(0) − T₀) e^(−kt)</b>. The temperature "
                  "starts at T(0) and settles towards T₀ as t grows.")
              + h4("Worked example")
              + p("A body at 100 °C cools in a room at 20 °C, and reaches 60 °C after 10 minutes. Then "
                  "60 = 20 + 80 e^(−10k), so e^(−10k) = 0.5 and <b>k = log 2/10 ≈ 0.0693 per "
                  "minute</b>.")
              + h4("Common mistake")
              + p("Using T instead of (T − T₀) on the right. The body cools towards the room, not "
                  "towards zero."),
              examples=["de17"], syllabus_item="4.2"),
     ]},

    {"title": tr("5. First-Order Linear Equations"),
     "items": [
         card("5.1 The standard form",
              h4("Definition")
              + p("A first-order DE is <b>linear</b> when it can be written as <b>dy/dx + P(x) y = "
                  "Q(x)</b>, where P and Q depend on x only. Both y and dy/dx appear to the first "
                  "power, and there is no y², no √y and no y·(dy/dx).")
              + h4("Getting to the standard form")
              + p("Divide through by the coefficient of dy/dx first. From x dy/dx + 2y = x², division "
                  "by x gives dy/dx + (2/x) y = x, so P = 2/x and Q = x.")
              + h4("Two checks")
              + ul("Is y to the power 1 only? If not, the equation is not linear.",
                   "Is Q free of y? If y appears in Q, it is not in standard form yet.")
              + h4("Common mistake")
              + p("Reading P as the coefficient of y before dividing by the coefficient of dy/dx. "
                  "Never skip the division."),
              syllabus_item="4.3"),
         card("5.2 The integrating factor",
              h4("Rule")
              + p("Multiply the standard form by <b>IF = e^(∫P dx)</b>. The left side then collapses "
                  "into d/dx (y · IF), so the equation becomes d/dx (y · IF) = Q · IF.")
              + h4("Then integrate")
              + p("<b>y · IF = ∫ Q · IF dx + c</b>, and finally y = (∫ Q·IF dx + c)/IF.")
              + h4("Why it works")
              + p("d/dx (y e^(∫P dx)) = e^(∫P dx)(dy/dx + P y), which is exactly the left side times "
                  "the IF. The factor is built to make the product rule run backwards.")
              + h4("Common mistake")
              + p("Applying the IF to only one side, or forgetting to divide by the IF at the end. The "
                  "IF multiplies the whole equation and must be removed before the answer is stated."),
              "d3_linear", syllabus_item="4.3"),
         card("5.3 First worked examples",
              h4("Example 1")
              + p("dy/dx + 2y = 4. Here P = 2, so IF = e^(2x), and (y e^(2x))′ = 4 e^(2x). Integrating, "
                  "y e^(2x) = 2 e^(2x) + c, so <b>y = 2 + c e^(−2x)</b>.")
              + h4("Example 2")
              + p("dy/dx + y = eˣ. IF = eˣ, so (y eˣ)′ = e^(2x) and y eˣ = e^(2x)/2 + c, giving "
                  "<b>y = eˣ/2 + c e^(−x)</b>.")
              + h4("Reading the answer")
              + p("The term with e^(−x) dies away as x grows; it is the transient part, while 2 or eˣ/2 "
                  "is the steady part. Engineering answers often split this way.")
              + h4("Common mistake")
              + p("Quoting IF = e^(∫P dx) and then never multiplying Q by it. Both sides need the "
                  "factor."),
              examples=["de18", "de19"], syllabus_item="4.3"),
         card("5.4 When P is not a constant",
              h4("Worked example")
              + p("Solve x dy/dx + 2y = x². Divide by x: dy/dx + (2/x) y = x, so P = 2/x and "
                  "∫P dx = 2 log x = log x². Hence IF = e^(log x²) = x².")
              + h4("Finish it")
              + p("(y x²)′ = x² · x = x³, so y x² = x⁴/4 + c and <b>y = x²/4 + c/x²</b>.")
              + h4("Two habits that save time")
              + ul("Simplify e^(log f) to f at once - do not leave it as an exponential.",
                   "The IF is never unique; the simplest form is the right one.")
              + h4("Common mistake")
              + p("Writing IF = e^(2 log x) and leaving it. It is x², and using the simplified form is "
                  "what makes the integration possible."),
              examples=["de20"], syllabus_item="4.3"),
     ]},

    {"title": tr("6. Linear Equations in Other Shapes"),
     "items": [
         card("6.1 When P is tan x or sec x",
              h4("Worked example")
              + p("Solve dy/dx + y tan x = sec x. Here P = tan x and ∫tan x dx = log|sec x|, so "
                  "<b>IF = sec x</b>.")
              + h4("Finish it")
              + p("(y sec x)′ = sec x · sec x = sec²x, so y sec x = tan x + c and "
                  "<b>y = sin x + c cos x</b>.")
              + h4("The two integrals to remember")
              + p("∫tan x dx = log|sec x| and ∫sec²x dx = tan x. With these, every tangent-type "
                  "question becomes routine.")
              + h4("Common mistake")
              + p("Integrating tan x as log|tan x|. Differentiate log|sec x| to convince yourself: "
                  "sec x tan x / sec x = tan x."),
              examples=["de21"], syllabus_item="4.3"),
         card("6.2 Using x as the dependent variable",
              h4("When y cannot be the subject")
              + p("If the equation is linear in x rather than in y, treat x as the unknown: "
                  "<b>dx/dy + P(y) x = Q(y)</b>. The method is identical, with y as the independent "
                  "variable.")
              + h4("Worked example")
              + p("dx/dy + x = y: P = 1, so IF = eʸ and (x eʸ)′ = y eʸ. Since ∫y eʸ dy = eʸ(y − 1), "
                  "x eʸ = eʸ(y − 1) + c and <b>x = y − 1 + c e^(−y)</b>.")
              + h4("How to spot it")
              + p("The equation is linear in x when x appears only to the first power and dy/dx appears "
                  "as dx/dy. Rewrite it with dx/dy and check.")
              + h4("Common mistake")
              + p("Trying to force such an equation into dy/dx + Py = Q, where it does not fit, instead "
                  "of swapping the roles."),
              examples=["de22"], syllabus_item="4.3"),
         card("6.3 Choosing between the two methods",
              h4("Order of checks")
              + ol("Can the right side be factorised into (x part) × (y part)? Then separate.",
                   "If not, is the equation linear in y? Then bring it to dy/dx + Py = Q and use the IF.",
                   "If neither holds, it is outside this syllabus - do not invent a method.")
              + h4("Examples of the decision")
              + table(["Equation", "Method"],
                      [("dy/dx = x y²", "separable"),
                       ("dy/dx = x + y", "neither (not separable, not linear)"),
                       ("dy/dx + 2y = eˣ", "linear, IF = e^(2x)"),
                       ("dy/dx = (x + 1)/y", "separable")])
              + h4("A common confusion")
              + p("dy/dx = xy is separable and also linear, so either method works and both give "
                  "y = C e^(x²/2). When both apply, choose the easier one.")
              + h4("Common mistake")
              + p("Calling dy/dx = x + y separable because it is a sum. A sum does not factor."),
              "d4_choice", syllabus_item="4.3"),
         card("6.4 Common mistakes in this unit",
              h4("Six errors to avoid")
              + ol("Forgetting to divide by the coefficient of dy/dx before reading P.",
                   "Using e^(∫P dx) without simplifying, e.g. leaving e^(2 log x) instead of x².",
                   "Losing the constant c, or adding two of them when one is enough.",
                   "Substituting the initial condition before integrating.",
                   "Writing the IF on one side only.",
                   "Not stating the final answer for y (or x) explicitly.")
              + h4("How to self-check")
              + p("Substitute your y back into the original equation and simplify. If the two sides "
                  "agree identically, the solution is right.")
              + h4("Marking pattern")
              + p("Most schemes give marks for the standard form, the IF, the integration and the final "
                  "answer separately, so show all four lines even if the arithmetic is rushed."),
              syllabus_item="4.3"),
     ]},

    {"title": tr("7. Exam Routine and Checks"),
     "items": [
         card("7.1 Five lines that earn the method marks",
              h4("For a separable equation")
              + ol("Write dy/dx = f(x) g(y) and state that it is separable.",
                   "Separate: dy/g(y) = f(x) dx.",
                   "Integrate both sides and add c.",
                   "Apply the initial condition if one is given.",
                   "State y explicitly and check by differentiating.")
              + h4("For a linear equation")
              + ol("Bring it to dy/dx + Py = Q and name P and Q.",
                   "Write IF = e^(∫P dx) and simplify it.",
                   "Multiply through and write d/dx (y·IF) = Q·IF.",
                   "Integrate, add c, then divide by the IF.")
              + h4("Time and marks")
              + p("The IF and the standard form together usually carry about half the marks, so write "
                  "them down even if the integration is incomplete."),
              syllabus_item="4.3"),
         card("7.2 Checking a solution properly",
              h4("Three-part check")
              + ol("Differentiate your answer and substitute into the original equation.",
                   "Check the initial condition, if one was given.",
                   "Check the algebra of the constant - a wrong c passes the first test but fails the "
                   "second.")
              + h4("Example")
              + p("For dy/dx + 2y = 4, the answer y = 2 + c e^(−2x) gives y′ = −2c e^(−2x), so y′ + 2y "
                  "= −2c e^(−2x) + 4 + 2c e^(−2x) = 4. Correct for every c.")
              + h4("Reading an answer graphically")
              + p("A solution curve must have the slope the DE prescribes at every point: on the family "
                  "y = c e^(−x) the slope is always −y, which matches dy/dx = −y.")
              + sc("Is a wrong constant c an error if the DE is satisfied?",
                   "Yes - the DE alone does not fix c, so an initial-condition question is only "
                   "finished when c is right."),
              syllabus_item="4.3"),
         card("7.3 Summary of the two methods",
              h4("Side by side")
              + table(["", "Variable separable", "Linear (IF)"],
                      [("Form", "dy/dx = f(x) g(y)", "dy/dx + P y = Q"),
                       ("Step", "split and integrate", "multiply by e^(∫P dx)"),
                       ("Work", "two standard integrals", "one product integration"),
                       ("Answer", "implicit is often fine", "state y explicitly")])
              + h4("Where each appears")
              + p("Cooling, growth and decay, and many rate laws are separable. Circuits, mixing with a "
                  "steady inflow and any equation with a free y term are usually linear.")
              + h4("What the syllabus asks")
              + p("Only these two methods, first order and first degree. Anything of second degree or "
                  "second order is outside DI02000021 Unit 4 and should not appear in an answer."),
              syllabus_item="4.3"),
     ]},

    {"title": tr("8. Practice Questions with Model Answers"),
     "items": []},  # filled by the builder
]

_NUM = [
    ("de1", "Find the order and degree of d²y/dx² + 3(dy/dx)² = x.",
     [p("The highest derivative present is d²y/dx², so the order is 2."),
      p("The degree is the power of that highest derivative once the equation is free of radicals and "
        "fractions, which gives degree 1."),
      p("The square on dy/dx is a lower derivative and does not affect the degree.")]),
    ("de2", "Find the order and degree of (dy/dx)³ + y = x².",
     [p("Only the first derivative appears, so the order is 1."),
      p("It is raised to the power 3, so the degree is 3."),
      p("Answer: order 1, degree 3.")]),
    ("de3", "Find the order and degree of d³y/dx³ + x(dy/dx)⁵ = 0.",
     [p("The highest derivative is d³y/dx³, so the order is 3."),
      p("Its power is 1, so the degree is 1 - the fifth power belongs to dy/dx, a lower derivative."),
      p("Answer: order 3, degree 1.")]),
    ("de4", "Show that y = e^(2x) is a solution of dy/dx − 2y = 0.",
     [p("Differentiate: dy/dx = 2e^(2x)."),
      p("Substitute: dy/dx − 2y = 2e^(2x) − 2e^(2x) = 0."),
      p("The equation holds for every x, so y = e^(2x) is a solution. Note the more general solution is "
        "y = c e^(2x).")]),
    ("de5", "Show that y = A cos x + B sin x satisfies d²y/dx² + y = 0.",
     [p("First derivative: y′ = −A sin x + B cos x."),
      p("Second derivative: y″ = −A cos x − B sin x = −y."),
      p("So y″ + y = −y + y = 0 for every x and for every choice of A and B. The two constants match "
        "the second order of the equation.")]),
    ("de6", "Form the differential equation from y = cx² by eliminating c.",
     [p("Differentiate once (one constant, one differentiation): y′ = 2cx."),
      p("Eliminate c: from the original, c = y/x², so y′ = 2(y/x²)x = 2y/x."),
      p("Clearing the fraction gives x y′ − 2y = 0, which contains no c.")]),
    ("de7", "Form the differential equation from y = a e^(2x).",
     [p("Differentiate: y′ = 2a e^(2x)."),
      p("But a e^(2x) is y itself, so y′ = 2y."),
      p("The constant disappears in the differentiation: the answer is y′ − 2y = 0, a first-order "
        "equation as expected from one constant.")]),
    ("de8", "Solve dy/dx = x/y.",
     [p("The right side is a product of an x-part and a y-part, so the equation is separable."),
      p("Separate: y dy = x dx."),
      p("Integrate: y²/2 = x²/2 + c₁, that is y² = x² + c after multiplying by 2."),
      p("The answer is the family of hyperbolas y² − x² = c.")]),
    ("de9", "Solve dy/dx = x²/y.",
     [p("Separate: y dy = x² dx."),
      p("Integrate: y²/2 = x³/3 + c₁."),
      p("Multiply by 2: y² = 2x³/3 + c, which is the general solution; y can be made explicit as "
        "y = ±√(2x³/3 + c).")]),
    ("de10", "Solve dy/dx = (1 + y²)/(1 + x²).",
     [p("Separate: dy/(1 + y²) = dx/(1 + x²)."),
      p("Both sides are standard integrals giving tan⁻¹."),
      p("So tan⁻¹y = tan⁻¹x + c, or tan⁻¹y − tan⁻¹x = c. Taking tangents gives y explicitly if "
        "needed.")]),
    ("de11", "Solve dy/dx = 2xy.",
     [p("Separate: dy/y = 2x dx."),
      p("Integrate: log|y| = x² + c."),
      p("Exponentiate: y = C e^(x²), with C = e^c, the general solution - a family of curves with the "
        "same bell-shaped slope pattern.")]),
    ("de12", "Solve dy/dx = y/x.",
     [p("Separate: dy/y = dx/x."),
      p("Integrate: log|y| = log|x| + c."),
      p("Write c = log C and combine the logs: log|y| = log|Cx|, so y = Cx - the straight lines "
        "through the origin.")]),
    ("de13", "Solve dy/dx = e^(x+y).",
     [p("Write the right side as a product: e^(x+y) = eˣ · eʸ."),
      p("Separate: e^(−y) dy = eˣ dx."),
      p("Integrate: −e^(−y) = eˣ + c."),
      p("Rearrange if an explicit y is wanted: e^(−y) = −eˣ − c, so y = −log(−eˣ − c).")]),
    ("de14", "Solve dy/dx = y cos x given y(0) = 1.",
     [p("Separate: dy/y = cos x dx."),
      p("Integrate: log|y| = sin x + c, so y = C e^(sin x)."),
      p("Apply y(0) = 1: 1 = C e⁰ = C."),
      p("The particular solution is y = e^(sin x), which is positive for every x.")]),
    ("de15", "Solve dy/dx = x(y² + 1) given y(0) = 1.",
     [p("Separate: dy/(1 + y²) = x dx."),
      p("Integrate: tan⁻¹y = x²/2 + c."),
      p("Apply y(0) = 1: tan⁻¹1 = π/4, so c = π/4."),
      p("The solution is tan⁻¹y = x²/2 + π/4, that is y = tan(x²/2 + π/4).")]),
    ("de16", "A quantity grows at a rate proportional to itself and doubles in 5 hours. Find y(t).",
     [p("The model is dy/dt = ky with y(0) = y₀, whose solution is y = y₀ e^(kt)."),
      p("Doubling means e^(5k) = 2, so k = log 2/5 ≈ 0.1386 per hour."),
      p("Hence y = y₀ e^(0.1386 t), or equivalently y = y₀ 2^(t/5) - the form many data questions "
        "expect.")]),
    ("de17", "A body at 100 °C cools in a room at 20 °C and reaches 60 °C in 10 minutes. Find T(t).",
     [p("Newton's law: dT/dt = −k(T − 20), which separates to dT/(T − 20) = −k dt."),
      p("Integrating: log(T − 20) = −kt + c, so T = 20 + A e^(−kt) with A = T(0) − 20 = 80."),
      p("Use T(10) = 60: 40 = 80 e^(−10k), so e^(−10k) = 0.5 and k = log 2/10 ≈ 0.0693 per minute."),
      p("Answer: T = 20 + 80 e^(−0.0693 t) °C, which settles towards the room temperature of 20 °C.")]),
    ("de18", "Solve dy/dx + 2y = 4.",
     [p("The equation is linear with P = 2 and Q = 4, so the integrating factor is e^(2x)."),
      p("Multiplying: d/dx (y e^(2x)) = 4 e^(2x)."),
      p("Integrate: y e^(2x) = 2 e^(2x) + c."),
      p("Divide by the IF: y = 2 + c e^(−2x). The constant term 2 is the steady state.")]),
    ("de19", "Solve dy/dx + y = eˣ.",
     [p("Here P = 1 and Q = eˣ, so IF = e^(∫1 dx) = eˣ."),
      p("Multiplying: d/dx (y eˣ) = eˣ · eˣ = e^(2x)."),
      p("Integrate: y eˣ = e^(2x)/2 + c."),
      p("Divide by eˣ: y = eˣ/2 + c e^(−x). The first term is the steady part and the second the "
        "transient that dies away.")]),
    ("de20", "Solve x dy/dx + 2y = x².",
     [p("Divide by x first: dy/dx + (2/x) y = x, so P = 2/x and Q = x."),
      p("∫P dx = 2 log x = log x², hence IF = x²."),
      p("Multiplying: d/dx (y x²) = x³."),
      p("Integrate: y x² = x⁴/4 + c, so y = x²/4 + c/x².")]),
    ("de21", "Solve dy/dx + y tan x = sec x.",
     [p("P = tan x, and ∫tan x dx = log|sec x|, so IF = sec x."),
      p("Multiplying: d/dx (y sec x) = sec x · sec x = sec²x."),
      p("Integrate: y sec x = tan x + c."),
      p("Divide by sec x, i.e. multiply by cos x: y = sin x + c cos x.")]),
    ("de22", "Solve dx/dy + x = y by treating x as the unknown.",
     [p("The equation is linear in x with y as the independent variable: P = 1 and Q = y."),
      p("IF = e^(∫1 dy) = eʸ, so d/dy (x eʸ) = y eʸ."),
      p("Integrate by parts: ∫y eʸ dy = eʸ(y − 1)."),
      p("So x eʸ = eʸ(y − 1) + c and x = y − 1 + c e^(−y).")]),
]

NUMERICALS = [{"id": i, "q": tr(q), "a": tr("".join(parts))} for i, q, parts in _NUM]

EQUATIONS = [
    {"title": tr("Definitions"),
     "items": [
         {"terms": tr("Order"), "a": tr("the order of the highest derivative in the equation")},
         {"terms": tr("Degree"), "a": tr("the power of the highest derivative, after clearing radicals")},
         {"terms": tr("General solution"), "a": tr("contains one arbitrary constant for a first-order DE")},
         {"terms": tr("Particular solution"), "a": tr("the general solution with c fixed by a condition")},
         {"terms": tr("Linear standard form"), "a": tr("dy/dx + P(x) y = Q(x)")},
         {"terms": tr("Separable form"), "a": tr("dy/dx = f(x) · g(y)")},
     ]},
    {"title": tr("Methods"),
     "items": [
         {"terms": tr("Separation"), "a": tr("dy/g(y) = f(x) dx, then integrate both sides")},
         {"terms": tr("Integrating factor"), "a": tr("IF = e^(∫P dx)")},
         {"terms": tr("After multiplying"), "a": tr("d/dx (y · IF) = Q · IF")},
         {"terms": tr("Solution of a linear DE"), "a": tr("y · IF = ∫ Q · IF dx + c")},
         {"terms": tr("Linear in x"), "a": tr("dx/dy + P(y) x = Q(y), same IF method")},
         {"terms": tr("Log form of the constant"), "a": tr("c = log C, so that logs combine")},
     ]},
    {"title": tr("Models and results"),
     "items": [
         {"terms": tr("Growth and decay"), "a": tr("dy/dt = k y  →  y = y₀ e^(kt)")},
         {"terms": tr("Doubling time"), "a": tr("t = log 2 / k")},
         {"terms": tr("Newton's law of cooling"), "a": tr("dT/dt = −k(T − T₀)  →  T = T₀ + (T(0) − T₀) e^(−kt)")},
         {"terms": tr("∫ tan x dx"), "a": tr("log|sec x| + c")},
         {"terms": tr("∫ sec²x dx"), "a": tr("tan x + c")},
         {"terms": tr("∫ dy/(1 + y²)"), "a": tr("tan⁻¹y + c")},
     ]},
]

VIVA = [
    {"title": tr("Definitions"),
     "items": [
         {"q": tr("What is a differential equation?"),
          "a": tr("An equation containing derivatives of an unknown function; solving it gives the "
                  "function, not a number.")},
         {"q": tr("How do you find the order of a DE?"),
          "a": tr("Look at the highest derivative present: dy/dx means first order, d²y/dx² means "
                  "second order.")},
         {"q": tr("How do you find the degree?"),
          "a": tr("Raise the question of the power of the highest derivative after the equation is "
                  "cleared of fractions and radicals in the derivatives.")},
         {"q": tr("What is the difference between a general and a particular solution?"),
          "a": tr("The general solution keeps the arbitrary constant; a particular solution has c fixed "
                  "by an initial or boundary condition.")},
         {"q": tr("How many arbitrary constants does a first-order DE have?"),
          "a": tr("Exactly one, because one integration is performed.")},
         {"q": tr("When is a first-order DE called linear?"),
          "a": tr("When it can be written as dy/dx + P(x) y = Q(x), with y and dy/dx only to the first "
                  "power.")},
     ]},
    {"title": tr("Methods"),
     "items": [
         {"q": tr("When can you use the variable separable method?"),
          "a": tr("When the right-hand side factorises into a function of x times a function of y.")},
         {"q": tr("Why is only one constant of integration kept?"),
          "a": tr("Each side produces a constant, but they combine into a single arbitrary constant.")},
         {"q": tr("What is an integrating factor?"),
          "a": tr("e^(∫P dx): multiplying the standard form by it turns the left side into the single "
                  "derivative d/dx (y · IF).")},
         {"q": tr("Why does the integrating factor work?"),
          "a": tr("Because d/dx(y e^(∫P dx)) = e^(∫P dx)(dy/dx + Py), which is the left side "
                  "multiplied by the IF - the product rule run backwards.")},
         {"q": tr("What must be done before reading P and Q?"),
          "a": tr("Divide the whole equation by the coefficient of dy/dx, so that dy/dx has "
                  "coefficient 1.")},
         {"q": tr("How do you solve dx/dy + x = y?"),
          "a": tr("Treat x as the unknown and y as the independent variable; IF = eʸ, giving "
                  "x = y − 1 + c e^(−y).")},
     ]},
    {"title": tr("Applications and checks"),
     "items": [
         {"q": tr("What is the model for growth or decay?"),
          "a": tr("dy/dt = ky, giving y = y₀ e^(kt); k > 0 grows and k < 0 decays.")},
         {"q": tr("State Newton's law of cooling."),
          "a": tr("dT/dt = −k(T − T₀), so the body approaches the surrounding temperature "
                  "exponentially.")},
         {"q": tr("How do you find the doubling time?"),
          "a": tr("Set y = 2y₀ in y = y₀ e^(kt): t = log 2/k.")},
         {"q": tr("How do you check the solution of a DE?"),
          "a": tr("Differentiate the answer, substitute into the original equation and confirm both "
                  "sides agree; then check any initial condition.")},
         {"q": tr("Give one engineering use of a first-order DE."),
          "a": tr("An RC circuit charging follows dV/dt + V/(RC) = E/(RC), a linear first-order "
                  "equation solved with an integrating factor.")},
     ]},
]

_PRACTICE = [
    ("Find the order and degree of d²y/dx² + 5 dy/dx + 6y = 0.", 3,
     [p("The highest derivative is d²y/dx², so the order is 2."),
      p("It appears to the first power and the equation has no radicals, so the degree is 1."),
      p("Answer: order 2, degree 1 - a second-order linear equation with constant coefficients.")]),
    ("Find the order and degree of (dy/dx)⁴ + y³ = x.", 3,
     [p("Only dy/dx appears, so the order is 1."),
      p("It is raised to the fourth power, so the degree is 4."),
      p("Answer: order 1, degree 4. The y³ does not affect the degree, which counts only the "
        "derivative.")]),
    ("Verify that y = x² satisfies dy/dx = 2y/x.", 3,
     [p("Differentiate: dy/dx = 2x."),
      p("Right side: 2y/x = 2x²/x = 2x."),
      p("The two sides are equal for every x ≠ 0, so y = x² is a solution; the general solution of the "
        "equation is y = cx².")]),
    ("Form the differential equation from y = c e^(3x).", 3,
     [p("One constant means one differentiation: y′ = 3c e^(3x)."),
      p("Replace c e^(3x) by y: y′ = 3y."),
      p("The answer is y′ − 3y = 0, a first-order equation with no arbitrary constant left.")]),
    ("Solve dy/dx = x/y given y(0) = 3.", 4,
     [p("Separate: y dy = x dx, then integrate to y²/2 = x²/2 + c₁, that is y² = x² + c."),
      p("Apply y(0) = 3: 9 = 0 + c, so c = 9."),
      p("The particular solution is y² = x² + 9, or y = √(x² + 9) for the branch through (0, 3).")]),
    ("Solve dy/dx = y/x.", 3,
     [p("Separate: dy/y = dx/x, then integrate to log|y| = log|x| + c."),
      p("Write c = log C and combine: log|y| = log|Cx|, so y = Cx."),
      p("The solution is the family of straight lines through the origin, confirmed by substituting "
        "back: dy/dx = C = y/x.")]),
    ("Solve dy/dx = (1 + y²)/(1 + x²).", 4,
     [p("Separate: dy/(1 + y²) = dx/(1 + x²)."),
      p("Both sides are standard tangent-inverse integrals, so tan⁻¹y = tan⁻¹x + c."),
      p("The answer may be left in this implicit form, or written as y = tan(tan⁻¹x + c) using the "
        "tangent addition formula.")]),
    ("Solve dy/dx = y cos x given y(0) = 2.", 4,
     [p("Separate: dy/y = cos x dx and integrate: log|y| = sin x + c, so y = C e^(sin x)."),
      p("Apply y(0) = 2: 2 = C e⁰, so C = 2."),
      p("The particular solution is y = 2 e^(sin x). Differentiating gives 2 e^(sin x) cos x = y cos x, "
        "which matches the equation.")]),
    ("Solve dy/dx + 3y = 6.", 4,
     [p("The equation is linear with P = 3 and Q = 6, so IF = e^(3x)."),
      p("Multiplying: d/dx (y e^(3x)) = 6 e^(3x), so y e^(3x) = 2 e^(3x) + c."),
      p("Divide by the integrating factor: y = 2 + c e^(−3x), the constant term 2 being the steady "
        "state.")]),
    ("Solve dy/dx + y/x = x².", 4,
     [p("Here P = 1/x, so ∫P dx = log x and IF = x."),
      p("Multiplying: d/dx (y x) = x³, so y x = x⁴/4 + c."),
      p("Divide by x: y = x³/4 + c/x. Substituting back checks both terms.")]),
    ("Solve x dy/dx − y = x³.", 4,
     [p("Divide by x: dy/dx − (1/x) y = x², so P = −1/x and Q = x²."),
      p("∫P dx = −log x, so IF = 1/x."),
      p("Multiplying: d/dx (y/x) = x, hence y/x = x²/2 + c."),
      p("The answer is y = x³/2 + cx.")]),
    ("Solve dy/dx + 2xy = 2x.", 4,
     [p("P = 2x, so ∫P dx = x² and IF = e^(x²)."),
      p("Multiplying: d/dx (y e^(x²)) = 2x e^(x²), which integrates to y e^(x²) = e^(x²) + c."),
      p("Divide by the IF: y = 1 + c e^(−x²). As x grows the second term vanishes, so y tends to 1.")]),
    ("A body at 90 °C is placed in a room at 30 °C and cools to 70 °C in 5 minutes. Find T(t).", 4,
     [p("The law dT/dt = −k(T − 30) separates to dT/(T − 30) = −k dt, giving T = 30 + A e^(−kt)."),
      p("At t = 0, T = 90, so A = 60 and T = 30 + 60 e^(−kt)."),
      p("Use T(5) = 70: 40 = 60 e^(−5k), so e^(−5k) = 2/3 and k = log(1.5)/5 ≈ 0.0811 per minute."),
      p("The temperature is T = 30 + 60 e^(−0.0811 t) °C, tending to the room value 30 °C.")]),
    ("Bacteria in a culture double every 3 hours, starting from 1000. Find N(t) and the count at 9 h.",
     4,
     [p("Growth at a rate proportional to the number gives N = N₀ e^(kt) with N₀ = 1000."),
      p("Doubling in 3 h means e^(3k) = 2, so k = log 2/3 ≈ 0.231."),
      p("Hence N = 1000 e^(0.231 t), or more neatly N = 1000 × 2^(t/3)."),
      p("At t = 9 h the count is 1000 × 2³ = 8000, three doublings.")]),
    ("Solve dx/dy + 2x = y, treating x as the unknown.", 4,
     [p("With y as the independent variable, P = 2 and Q = y, so IF = e^(2y)."),
      p("Multiplying: d/dy (x e^(2y)) = y e^(2y)."),
      p("Integrating by parts, ∫y e^(2y) dy = e^(2y)(y/2 − 1/4)."),
      p("So x e^(2y) = e^(2y)(y/2 − 1/4) + c and x = y/2 − 1/4 + c e^(−2y).")]),
]

EXAM = [{"q": tr(q), "marks": m} for q, m, _parts in _PRACTICE]
PRACTICE_ANSWERS = [tr("".join(parts)) for _q, _m, parts in _PRACTICE]

LESSON_COUNT = sum(len(s["items"]) for s in NOTES)
