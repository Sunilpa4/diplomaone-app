"""DI02000021 Engineering Mathematics - Unit 3: Integration and its Applications.

GTU 3.1-3.6, 10 h, 20 %, 14 marks, CO3: integration as anti-differentiation, standard integrals and
working rules, substitution, integration by parts, the definite integral and its properties, and the
applications (area under a curve and volume of revolution).
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
    ("Khan Academy - integrals: rules, substitution and definite integrals",
     "https://www.khanacademy.org/math/integral-calculus"),
    ("OpenStax - Calculus Volume 1, chapters 5 and 6",
     "https://openstax.org/details/books/calculus-volume-1"),
    ("GeoGebra - shade the area under a curve and change the limits",
     "https://www.geogebra.org/m/Bh4gGz8p"),
    ("B. S. Grewal - Elementary Engineering Mathematics (Khanna Publishers)",
     "https://www.khannapublishers.in/"),
]

NOTES = [
    {"title": tr("1. Integration as Anti-differentiation"),
     "items": [
         card("1.1 The indefinite integral and the constant c",
              h4("Definition")
              + p("<b>Integration is the reverse of differentiation.</b> If dF/dx = f(x), then "
                  "∫ f(x) dx = F(x) + c, where c is any constant.")
              + p("The symbol ∫ means 'integrate', f(x) is the <b>integrand</b>, dx names the variable "
                  "and the answer F(x) is called the <b>primitive</b> or anti-derivative.")
              + h4("Why the + c is compulsory")
              + p("x², x² + 3 and x² − 7 all differentiate to 2x, so from the slope alone you cannot "
                  "recover the height. Every indefinite integral carries + c until a condition (a "
                  "point on the curve) fixes it.")
              + h4("Worked example")
              + p("∫ 2x dx = x² + c. If you are also told that the curve passes through (1, 5), then "
                  "5 = 1 + c gives c = 4 and the answer is y = x² + 4.")
              + h4("Check every answer")
              + p("Differentiate the result; it must return the integrand exactly. This one habit "
                  "catches nearly every integration error."),
              "i1_family", examples=["ig1"], syllabus_item="3.1"),
         card("1.2 The power rule for integration",
              h4("Rule")
              + p("<b>∫ xⁿ dx = xⁿ⁺¹/(n + 1) + c</b>, valid for every n except n = −1.")
              + h4("Worked examples")
              + p("∫ x⁵ dx = x⁶/6 + c;  ∫ x² dx = x³/3 + c;  ∫ x dx = x²/2 + c.")
              + p("For a root, write it as a power first: ∫ √x dx = ∫ x^(1/2) dx = "
                  "(2/3)x^(3/2) + c.")
              + p("For a reciprocal power: ∫ x⁻² dx = x⁻¹/(−1) + c = −1/x + c.")
              + h4("The special case n = −1")
              + p("The rule fails for ∫ x⁻¹ dx because dividing by zero is impossible; the answer is "
                  "the logarithm: ∫ (1/x) dx = log|x| + c.")
              + h4("Common mistake")
              + p("Subtracting one instead of adding one. Integration raises the power, "
                  "differentiation lowers it."),
              examples=["ig3", "ig4"], syllabus_item="3.2"),
         card("1.3 Integrals of sums and constant multiples",
              h4("Rules")
              + ul("∫ [f(x) ± g(x)] dx = ∫ f(x) dx ± ∫ g(x) dx",
                   "∫ k f(x) dx = k ∫ f(x) dx for a constant k")
              + h4("Worked example")
              + p("∫ (3x² + 2x + 1) dx = x³ + x² + x + c - integrate term by term and add one c at "
                  "the end, never one per term.")
              + h4("Constants")
              + p("∫ 5 dx = 5x + c, because the derivative of 5x is 5. A bare constant integrates to "
                  "that constant times x.")
              + h4("Common mistake")
              + p("Writing a separate + c for every bracket. One constant of integration is enough; "
                  "three constants would simply combine into one."),
              examples=["ig2"], syllabus_item="3.2"),
         card("1.4 Reading an integration question",
              h4("What is being asked")
              + table(["The question says", "The answer is"],
                      [("∫ f(x) dx", "a function plus c"),
                       ("∫ from a to b", "a number"),
                       ("find the area", "a number with square units"),
                       ("find y given dy/dx and a point", "a particular curve - find c")])
              + h4("Notation")
              + p("The dx is part of the symbol and tells you the variable: ∫ t² dt is a different "
                  "question from ∫ t² dx (the latter treats t as a constant, giving t²x + c).")
              + h4("A sanity check on size")
              + p("Integrating raises the degree by one: a quadratic integrand gives a cubic answer. If "
                  "your answer has the same degree as the integrand, something went wrong."),
              syllabus_item="3.1"),
     ]},

    {"title": tr("2. Standard Integrals and Working Rules"),
     "items": [
         card("2.1 The standard table",
              h4("Learn these by heart")
              + table(["∫ f(x) dx", "Answer"],
                      [("xⁿ (n ≠ −1)", "xⁿ⁺¹/(n + 1) + c"),
                       ("1/x", "log|x| + c"),
                       ("eˣ", "eˣ + c"),
                       ("aˣ", "aˣ/log a + c"),
                       ("sin x", "−cos x + c"),
                       ("cos x", "sin x + c"),
                       ("sec²x", "tan x + c"),
                       ("k (constant)", "kx + c")])
              + h4("Reading the table backwards")
              + p("Each line is a derivative read right to left. Because d(cos x)/dx = −sin x, the "
                  "integral of sin x carries a minus sign.")
              + h4("Common mistake")
              + p("Integrating cos x to −sin x. Differentiation of sin x gives +cos x, so the integral "
                  "of cos x is +sin x."),
              syllabus_item="3.2"),
         card("2.2 Exponential, logarithmic and reciprocal forms",
              h4("Three families")
              + ul("∫ eˣ dx = eˣ + c - the only function that is its own integral.",
                   "∫ (1/x) dx = log|x| + c - the modulus because 1/x exists on both sides of 0.",
                   "∫ aˣ dx = aˣ/log a + c.")
              + h4("Worked example")
              + p("∫ (eˣ + 1/x) dx = eˣ + log|x| + c. Differentiating gives eˣ + 1/x straight back.")
              + h4("With a linear inside")
              + p("∫ e^(3x) dx = e^(3x)/3 + c: divide by the inside derivative. The same idea gives "
                  "∫ e^(−2x) dx = −e^(−2x)/2 + c.")
              + h4("Common mistake")
              + p("Dropping the modulus in log|x|. For an integrand such as 1/x, negative x is "
                  "allowed, so the absolute value must stay."),
              examples=["ig5"], syllabus_item="3.2"),
         card("2.3 Trigonometric integrals you will meet",
              h4("Direct forms")
              + p("∫ sin x dx = −cos x + c and ∫ cos x dx = sin x + c. A sum integrates term by term: "
                  "∫ (sin x − cos x) dx = −cos x − sin x + c.")
              + h4("Squared and product forms")
              + p("∫ sec²x dx = tan x + c comes straight from d(tan x)/dx = sec²x.")
              + h4("Angles with a coefficient")
              + p("∫ sin 3x dx = −cos(3x)/3 + c and ∫ cos 5x dx = sin(5x)/5 + c: integrate as usual, "
                  "then divide by the inside derivative.")
              + h4("Common mistake")
              + p("Forgetting the division when the angle has a coefficient. Differentiating "
                  "−cos(3x)/3 gives sin 3x, which proves the factor 3 belongs underneath."),
              examples=["ig6"], syllabus_item="3.2"),
         card("2.4 Choosing a method before you start",
              h4("The decision tree")
              + ol("Is it a standard form or a sum of them? Integrate directly.",
                   "Does one part look like the derivative of another? Substitute.",
                   "Is it a product of unlike functions (x times eˣ, x times sin x, log x alone)? "
                   "Use parts.")
              + h4("Examples of the choice")
              + table(["Integrand", "Method"],
                      [("3x² + 2x", "standard, term by term"),
                       ("2x(x² + 1)³", "substitution u = x² + 1"),
                       ("x eˣ", "parts with u = x"),
                       ("log x", "parts with u = log x, dv = dx")])
              + h4("Verification")
              + p("Whatever method you use, differentiate the answer and compare with the integrand. "
                  "It takes ten seconds and catches the majority of slips."),
              "i2_method", syllabus_item="3.2"),
     ]},

    {"title": tr("3. Integration by Substitution"),
     "items": [
         card("3.1 Undoing the chain rule",
              h4("Idea")
              + p("If the integrand contains a function and (nearly) its derivative, replace the inner "
                  "function by u. Then du = u′ dx, and the integral becomes a standard one in u.")
              + h4("Worked example")
              + p("∫ 2x(x² + 1)³ dx: take u = x² + 1, so du = 2x dx. The integral is ∫ u³ du = "
                  "u⁴/4 + c = <b>(x² + 1)⁴/4 + c</b>.")
              + h4("Check")
              + p("Differentiating (x² + 1)⁴/4 gives 4(x² + 1)³/4 × 2x = 2x(x² + 1)³, which is the "
                  "integrand, so the answer is right.")
              + h4("Common mistake")
              + p("Substituting but forgetting to replace dx. Every dx must be rewritten in terms of "
                  "du before you integrate."),
              "i3_sub", examples=["ig9"], syllabus_item="3.3"),
         card("3.2 Choosing u",
              h4("Good choices")
              + ul("Inside a power or root: u = the whole bracket.",
                   "Inside a logarithm: u = the argument of the log.",
                   "The denominator: u = the bottom of a fraction.",
                   "The exponent: u = the power of e.")
              + h4("Examples")
              + p("∫ (2x + 3)⁴ dx with u = 2x + 3 gives ∫ u⁴ (du/2) = u⁵/10 + c = "
                  "(2x + 3)⁵/10 + c.")
              + p("∫ sin³x cos x dx with u = sin x gives ∫ u³ du = sin⁴x/4 + c.")
              + h4("Rule of thumb")
              + p("After substituting, everything must be in u - if an x survives, the choice was "
                  "wrong or a constant has to be adjusted."),
              examples=["ig8", "ig11"], syllabus_item="3.3"),
         card("3.3 Adjusting constants",
              h4("The constant factor trick")
              + p("If du is a multiple of what is present, adjust the constant rather than the "
                  "variable.")
              + h4("Worked example")
              + p("∫ x(x² + 1)³ dx: u = x² + 1 gives du = 2x dx, but only x dx is present. Write "
                  "x dx = du/2, so the integral is (1/2)∫ u³ du = (1/2)(u⁴/4) + c = "
                  "<b>(x² + 1)⁴/8 + c</b>.")
              + h4("Logarithmic results")
              + p("When the top is exactly the derivative of the bottom, the answer is a logarithm: "
                  "∫ 2x/(x² + 1) dx = log(x² + 1) + c.")
              + h4("Common mistake")
              + p("A constant may be moved in or out; a variable may not. Never write x = du/2 unless "
                  "the x really cancels."),
              examples=["ig10"], syllabus_item="3.3"),
         card("3.4 Definite integrals with a substitution",
              h4("Two safe routes")
              + ol("Change the limits: when u = x² + 1, the limit x = 0 becomes u = 1 and x = 1 becomes "
                   "u = 2.",
                   "Or integrate in u, put x back, and only then substitute the original limits.")
              + h4("Worked idea")
              + p("∫₀¹ 2x(x² + 1)³ dx. With u = x² + 1 the limits 0 and 1 become 1 and 2, so the "
                  "integral is ∫₁² u³ du = [u⁴/4]₁² = 4 − 1/4 = 15/4.")
              + h4("Why limits must follow u")
              + p("A limit written as 0 refers to x = 0. Once the variable is u, the old limits are "
                  "meaningless - the most common error in definite substitution.")
              + p("No + c appears in a definite integral, because it cancels when the limits are "
                  "subtracted."),
              examples=["ig7"], syllabus_item="3.3"),
     ]},

    {"title": tr("4. Integration by Parts"),
     "items": [
         card("4.1 The formula",
              h4("Rule")
              + p("<b>∫ u dv = uv − ∫ v du</b> - it comes from the product rule rearranged, and it "
                  "trades one integral for a simpler one.")
              + h4("Worked example")
              + p("∫ x eˣ dx: choose u = x (so du = dx) and dv = eˣ dx (so v = eˣ). Then the integral "
                  "is x eˣ − ∫ eˣ dx = x eˣ − eˣ + c = <b>eˣ(x − 1) + c</b>.")
              + h4("Check")
              + p("Differentiating eˣ(x − 1) gives eˣ(x − 1) + eˣ = x eˣ, the integrand.")
              + h4("Common mistake")
              + p("Swapping u and dv. Choosing u = eˣ makes the new integral harder, not easier - the "
                  "point of parts is to reduce the work."),
              "i4_parts", examples=["ig12"], syllabus_item="3.4"),
         card("4.2 Choosing u: the LIATE order",
              h4("Priority for u")
              + p("<b>L</b>ogarithm, <b>I</b>nverse trig, <b>A</b>lgebraic (x, x²), <b>T</b>rig, "
                  "<b>E</b>xponential - take u as the function that comes first in this list, and dv "
                  "as the rest.")
              + h4("Why")
              + p("Logarithms and inverse trig functions have no elementary derivative in the table but "
                  "become simple when differentiated; exponentials and sines stay simple when "
                  "integrated.")
              + h4("Examples of the choice")
              + table(["Integral", "u", "dv"],
                      [("∫ x eˣ dx", "x", "eˣ dx"),
                       ("∫ x cos x dx", "x", "cos x dx"),
                       ("∫ x log x dx", "log x", "x dx"),
                       ("∫ log x dx", "log x", "dx")])
              + h4("Common mistake")
              + p("Choosing u = x when a logarithm is present. With log in the integrand, u = log x "
                  "always wins."),
              examples=["ig13"], syllabus_item="3.4"),
         card("4.3 Worked examples with trigonometric and logarithmic partners",
              h4("Trigonometric")
              + p("∫ x cos x dx: u = x, dv = cos x dx, so v = sin x. The integral is x sin x − "
                  "∫ sin x dx = <b>x sin x + cos x + c</b>.")
              + h4("Logarithmic with algebra")
              + p("∫ x log x dx: u = log x, dv = x dx, so du = dx/x and v = x²/2. Then the integral is "
                  "(x²/2)log x − ∫ (x²/2)(1/x) dx = (x²/2)log x − x²/4 + c.")
              + h4("When parts is needed twice")
              + p("∫ x² eˣ dx needs two rounds; each round lowers the power of x by one until only eˣ "
                  "is left.")
              + h4("Common mistake")
              + p("Leaving the answer as (x²/2)log x − ∫ x/2 dx. The second integral must be evaluated "
                  "before the answer is complete."),
              examples=["ig14", "ig15"], syllabus_item="3.4"),
         card("4.4 The special case ∫ log x dx",
              h4("A product in disguise")
              + p("There is only one function, but you may take dv = dx, that is v = x.")
              + h4("Working")
              + p("u = log x (du = dx/x) and dv = dx (v = x), so ∫ log x dx = x log x − ∫ x(1/x) dx = "
                  "x log x − ∫ 1 dx = <b>x log x − x + c</b>.")
              + h4("Check")
              + p("d/dx[x log x − x] = log x + x(1/x) − 1 = log x, so the answer is correct.")
              + h4("Same idea elsewhere")
              + p("∫ log x dx, ∫ sin⁻¹x dx and ∫ tan⁻¹x dx are all done by taking dv = dx. This is a "
                  "standard exam pattern worth memorising."),
              examples=["ig15"], syllabus_item="3.4"),
     ]},

    {"title": tr("5. Definite Integrals and Their Properties"),
     "items": [
         card("5.1 From area to a number",
              h4("Definition")
              + p("A definite integral has limits: <b>∫ from a to b of f(x) dx = F(b) − F(a)</b>, "
                  "written with square brackets [F(x)] from a to b.")
              + p("The answer is a number, not a function, and it equals the signed area between the "
                  "curve and the x-axis from a to b.")
              + h4("Worked example")
              + p("∫₀² (x² + 1) dx = [x³/3 + x]₀² = (8/3 + 2) − 0 = 14/3.")
              + h4("Why no + c")
              + p("(F(b) + c) − (F(a) + c) = F(b) − F(a): the constant cancels, so it is never written "
                  "in a definite integral.")
              + h4("Common mistake")
              + p("Subtracting in the wrong order. The upper limit goes in first: F(b) − F(a), not "
                  "F(a) − F(b)."),
              "i5_definite", examples=["ig17"], syllabus_item="3.5"),
         card("5.2 Evaluating definite integrals",
              h4("Procedure")
              + ol("Find the indefinite integral (ignore c).",
                   "Write it in square brackets with the limits.",
                   "Substitute the upper limit, then the lower limit, and subtract.",
                   "Simplify to a single number.")
              + h4("Worked examples")
              + p("∫₁³ 2x dx = [x²]₁³ = 9 − 1 = <b>8</b>.")
              + p("∫₀^(π/2) sin x dx = [−cos x]₀^(π/2) = 0 − (−1) = <b>1</b>.")
              + p("∫₀¹ e^(2x) dx = [e^(2x)/2]₀¹ = (e² − 1)/2.")
              + h4("Check the sign")
              + p("An area found below the x-axis comes out negative. That is mathematically correct "
                  "for the integral, but an area question expects the positive value, so split the "
                  "interval at the crossing point."),
              examples=["ig18", "ig19", "ig20"], syllabus_item="3.5"),
         card("5.3 Properties worth knowing",
              h4("The four properties")
              + ul("∫ from a to a = 0",
                   "∫ from a to b = − ∫ from b to a (swapping the limits changes the sign)",
                   "∫ from a to b = ∫ from a to c + ∫ from c to b (splitting the interval)",
                   "∫ from −a to a of an odd function = 0, and of an even function = 2∫ from 0 to a")
              + h4("Using odd and even")
              + p("x³ is odd, so ∫₋₁¹ x³ dx = 0 without any calculation. x² is even, so "
                  "∫₋₂² x² dx = 2∫₀² x² dx = 16/3.")
              + h4("Using the split")
              + p("If ∫₀¹ f = 2 and ∫₁³ f = 5, then ∫₀³ f = 7. This is how a table of measured values "
                  "is combined in engineering data work.")
              + h4("Common mistake")
              + p("Using the odd-function rule on an even function, or forgetting that the rule needs "
                  "symmetric limits about zero."),
              examples=["ig21", "ig22"], syllabus_item="3.5"),
         card("5.4 Interpreting the number",
              h4("Signed area")
              + p("Above the axis the integral is positive; below it is negative. The <b>total area</b> "
                  "is the sum of the absolute values, which is why a curve that crosses the axis has "
                  "to be split.")
              + h4("Example")
              + p("For y = x from −2 to 2, ∫ x dx = 0, yet the area between the curve and the axis is "
                  "2 + 2 = 4: the two triangles cancel in the integral but not in the area.")
              + h4("Engineering reading")
              + p("An integral of a rate gives a total: ∫ velocity dt is distance, ∫ current dt is "
                  "charge, ∫ force dx is work. The units of the answer are the units of the integrand "
                  "times the units of the variable.")
              + sc("Can a definite integral be negative?",
                   "Yes - whenever the curve lies below the axis. A negative answer is a warning to "
                   "stop and think about geometry, not an error in the method."),
              syllabus_item="3.5"),
     ]},

    {"title": tr("6. Area Under a Curve"),
     "items": [
         card("6.1 The area formula",
              h4("Rule")
              + p("The area between y = f(x), the x-axis and the lines x = a and x = b is "
                  "<b>∫ from a to b of y dx</b>, provided the curve stays above the axis.")
              + h4("Worked example")
              + p("Area under y = x² from x = 0 to x = 3 is ∫₀³ x² dx = [x³/3]₀³ = 9 square units.")
              + h4("Method")
              + ol("Sketch the curve and mark the limits - the sketch tells you whether the area is "
                   "above or below the axis.",
                   "Integrate y with respect to x.",
                   "Substitute the limits and subtract.",
                   "Take the modulus if the question asks for area and the answer is negative.")
              + h4("Common mistake")
              + p("Integrating the wrong way round (dx when the boundary is y = c). Read the diagram "
                  "before choosing the variable."),
              examples=["ig23"], syllabus_item="3.6"),
         card("6.2 Curves that cross the axis",
              h4("Why you must split")
              + p("If the curve crosses the axis between the limits, the integral subtracts the part "
                  "below. For the area, integrate each piece separately and add the sizes.")
              + h4("Worked example")
              + p("Area between y = 4x − x² and the x-axis: the curve meets the axis at x = 0 and "
                  "x = 4 and stays above it in between, so the area is ∫₀⁴ (4x − x²) dx = "
                  "[2x² − x³/3]₀⁴ = 32 − 64/3 = <b>32/3</b> square units.")
              + h4("If it crossed")
              + p("For y = x² − 1 between −2 and 2 the integral is 16/3 − 4 = 4/3, but the true area "
                  "is 4 (split at x = ±1); the middle piece is below the axis and cancels part of the "
                  "rest.")
              + h4("Reading the answer")
              + p("Area is always positive and carries square units (cm², m²). A negative number means "
                  "the geometry was not checked first."),
              examples=["ig24"], syllabus_item="3.6"),
         card("6.3 Area between two curves, and a check",
              h4("Between two curves")
              + p("When y = f(x) is above y = g(x) on the interval, the area between them is "
                  "∫ (f − g) dx. Take the upper curve minus the lower one; the difference is positive.")
              + h4("Example")
              + p("Between y = x and y = x² from 0 to 1: ∫₀¹ (x − x²) dx = 1/2 − 1/3 = 1/6.")
              + h4("A quick sanity check")
              + p("Estimate the area as a rectangle first: width (b − a) times an average height. If "
                  "the exact answer is far from the estimate, one of the limits or a sign is wrong.")
              + h4("Common mistake")
              + p("Subtracting the lower curve from the upper one only where they actually cross. Find "
                  "the crossing points first and use them as limits."),
              syllabus_item="3.6"),
     ]},

    {"title": tr("7. Volume of Revolution and Exam Routine"),
     "items": [
         card("7.1 Rotating an area about the x-axis",
              h4("Rule")
              + p("When the area under y = f(x) from a to b is rotated about the x-axis, each thin "
                  "slice is a disc of radius y and thickness dx, so <b>V = π ∫ y² dx</b> between the "
                  "limits.")
              + h4("Worked example")
              + p("y = x from x = 0 to x = 2 rotating about the x-axis: V = π∫₀² x² dx = π[x³/3]₀² = "
                  "<b>8π/3</b> cubic units.")
              + h4("Second example")
              + p("y = √x from 0 to 4: V = π∫₀⁴ x dx = π[x²/2]₀⁴ = 8π.")
              + h4("Method")
              + ol("Square the given y (or the given x if the rotation is about the y-axis).",
                   "Integrate between the limits.",
                   "Multiply by π and state the cubic units.")
              + h4("Common mistake")
              + p("Squaring after integrating. The square is taken first: V = π∫ y² dx, never "
                  "π(∫ y dx)²."),
              "i6_volume", examples=["ig25"], syllabus_item="3.6"),
         card("7.2 A two-part volume and the shape of the answer",
              h4("One question, two solids")
              + p("A single question often asks for both y = x (0 to 2) and y = √x (0 to 4). Keep the "
                  "two results separate and label them; comparing them shows how the shape changes the "
                  "volume.")
              + h4("Values")
              + p("y = x gives 8π/3 ≈ 8.38 and y = √x gives 8π ≈ 25.13. The square-root curve encloses "
                  "far more, because it is further from the axis across most of the interval.")
              + h4("Reading the units")
              + p("If x and y are in cm, the volume is in cm³. The π is often left in the answer; a "
                  "decimal is only needed when the question says so.")
              + h4("Common mistake")
              + p("Using y instead of y². The disc area is πr² with r = y, so the square is "
                  "unavoidable."),
              examples=["ig26"], syllabus_item="3.6"),
         card("7.3 Exam routine for an integration question",
              h4("Five lines that earn the method marks")
              + ol("Write the integral and say which rule or substitution you are using.",
                   "Show the substitution or the u and dv, not just the answer.",
                   "Integrate and keep the + c (indefinite) or the square brackets (definite).",
                   "Substitute the limits carefully, upper first.",
                   "For an application, state the units and answer the question that was asked "
                   "(area, volume, distance).")
              + h4("Time savers")
              + p("Quote the standard table rather than re-deriving it. Check with differentiation - it "
                  "takes seconds and settles the answer.")
              + h4("Accuracy habits")
              + p("Keep fractions rather than converting early to decimals, and put brackets around "
                  "negative limits. In a definite integral, (−2)² = 4, not −4.")
              + h4("What the examiners reward")
              + p("A clear statement of the formula, one correct integration and the correct limit "
                  "arithmetic score nearly all the marks, even if the final simplification is clumsy."),
              syllabus_item="3.6"),
     ]},

    {"title": tr("8. Practice Questions with Model Answers"),
     "items": []},  # filled by the builder
]

_NUM = [
    ("ig1", "Evaluate ∫ x⁵ dx.",
     [p("Use the power rule: raise the power by one and divide by the new power."),
      p("∫ x⁵ dx = x⁶/6 + c."),
      p("Check: d(x⁶/6)/dx = 6x⁵/6 = x⁵, which is the integrand.")]),
    ("ig2", "Evaluate ∫ (3x² + 2x + 1) dx.",
     [p("Integrate term by term: 3x² gives x³, 2x gives x², and 1 gives x."),
      p("So the answer is x³ + x² + x + c."),
      p("Check: 3x² + 2x + 1, exactly the integrand.")]),
    ("ig3", "Evaluate ∫ √x dx.",
     [p("Write the root as a power: √x = x^(1/2)."),
      p("∫ x^(1/2) dx = x^(3/2)/(3/2) + c = (2/3)x^(3/2) + c."),
      p("In root form this is (2/3)x√x + c.")]),
    ("ig4", "Evaluate ∫ (1/x²) dx.",
     [p("Write the integrand as a power: 1/x² = x⁻²."),
      p("∫ x⁻² dx = x⁻¹/(−1) + c = −1/x + c."),
      p("Check: d(−x⁻¹)/dx = x⁻² = 1/x².")]),
    ("ig5", "Evaluate ∫ (eˣ + 1/x) dx.",
     [p("Both parts are standard forms: eˣ integrates to eˣ and 1/x integrates to log|x|."),
      p("So the answer is eˣ + log|x| + c."),
      p("The modulus sign is needed because 1/x is defined for negative x as well.")]),
    ("ig6", "Evaluate ∫ (sin x − cos x) dx.",
     [p("∫ sin x dx = −cos x and ∫ cos x dx = sin x, so the difference is −cos x − sin x + c."),
      p("Check: differentiating gives sin x − cos x, the integrand."),
      p("Watch the double negative: −(−sin x) = +sin x.")]),
    ("ig7", "Evaluate ∫₀¹ 2x(x² + 1)³ dx by substitution.",
     [p("Let u = x² + 1, so du = 2x dx. The limits change too: x = 0 gives u = 1 and x = 1 gives "
        "u = 2."),
      p("The integral becomes ∫₁² u³ du = [u⁴/4]₁² = 4 − 1/4 = 15/4."),
      p("No + c appears, and the old limits must not be used with u.")]),
    ("ig8", "Evaluate ∫ (2x + 3)⁴ dx.",
     [p("Substitute u = 2x + 3, so du = 2 dx and dx = du/2."),
      p("The integral becomes (1/2)∫ u⁴ du = u⁵/10 + c = (2x + 3)⁵/10 + c."),
      p("Check: 5(2x + 3)⁴ × 2/10 = (2x + 3)⁴.")]),
    ("ig9", "Evaluate ∫ x(x² + 1)³ dx.",
     [p("Take u = x² + 1, so du = 2x dx, that is x dx = du/2."),
      p("The integral becomes (1/2)∫ u³ du = u⁴/8 + c = (x² + 1)⁴/8 + c."),
      p("Check by differentiating: 4(x² + 1)³ × 2x/8 = x(x² + 1)³.")]),
    ("ig10", "Evaluate ∫ 2x/(x² + 1) dx.",
     [p("The numerator is exactly the derivative of the denominator, so the answer is a logarithm."),
      p("With u = x² + 1, du = 2x dx, the integral is ∫ du/u = log|u| + c = log(x² + 1) + c."),
      p("No modulus is needed because x² + 1 is always positive.")]),
    ("ig11", "Evaluate ∫ sin³x cos x dx.",
     [p("Take u = sin x, so du = cos x dx."),
      p("The integral becomes ∫ u³ du = u⁴/4 + c = sin⁴x/4 + c."),
      p("Check: 4 sin³x cos x/4 = sin³x cos x, the integrand.")]),
    ("ig12", "Evaluate ∫ x eˣ dx by parts.",
     [p("Take u = x (du = dx) and dv = eˣ dx (v = eˣ)."),
      p("∫ u dv = uv − ∫ v du = x eˣ − ∫ eˣ dx = x eˣ − eˣ + c."),
      p("So the answer is eˣ(x − 1) + c. Check: eˣ(x − 1) + eˣ = x eˣ.")]),
    ("ig13", "Evaluate ∫ x cos x dx by parts.",
     [p("Take u = x (du = dx) and dv = cos x dx (v = sin x)."),
      p("The integral is x sin x − ∫ sin x dx = x sin x − (−cos x) + c = x sin x + cos x + c."),
      p("Check: differentiating gives sin x + x cos x − sin x = x cos x.")]),
    ("ig14", "Evaluate ∫ x log x dx.",
     [p("By LIATE the logarithm becomes u: u = log x (du = dx/x) and dv = x dx (v = x²/2)."),
      p("The integral = (x²/2)log x − ∫ (x²/2)(1/x) dx = (x²/2)log x − ∫ (x/2) dx."),
      p("So the answer is (x²/2)log x − x²/4 + c.")]),
    ("ig15", "Evaluate ∫ log x dx.",
     [p("There is one function, so take u = log x and dv = dx, giving v = x."),
      p("∫ log x dx = x log x − ∫ x(1/x) dx = x log x − ∫ 1 dx = x log x − x + c."),
      p("Check: log x + 1 − 1 = log x.")]),
    ("ig17", "Evaluate ∫₀² (x² + 1) dx.",
     [p("Integrate: [x³/3 + x]₀²."),
      p("Upper limit: 8/3 + 2 = 14/3. Lower limit: 0."),
      p("So the value is 14/3. No + c is written in a definite integral.")]),
    ("ig18", "Evaluate ∫₁³ 2x dx.",
     [p("The integral of 2x is x², so the definite integral is [x²]₁³."),
      p("9 − 1 = 8."),
      p("Check by geometry: the area is a trapezium with parallel sides 2 and 6 and width 2, that is "
        "(2 + 6)/2 × 2 = 8.")]),
    ("ig19", "Evaluate ∫₀^(π/2) sin x dx.",
     [p("The integral of sin x is −cos x, so the value is [−cos x] from 0 to π/2."),
      p("cos(π/2) = 0 and cos 0 = 1, so 0 − (−1) = 1."),
      p("The area under one arch of the sine curve from 0 to π/2 is exactly 1 square unit.")]),
    ("ig20", "Evaluate ∫₀¹ e^(2x) dx.",
     [p("The integral of e^(2x) is e^(2x)/2 (divide by the inside derivative)."),
      p("So the value is [e^(2x)/2]₀¹ = (e² − 1)/2."),
      p("Numerically (7.389 − 1)/2 ≈ 3.19, which is reasonable for a curve rising from 1 to 7.4.")]),
    ("ig21", "Evaluate ∫₋₁¹ x³ dx using a property.",
     [p("x³ is an odd function: f(−x) = −f(x)."),
      p("For an odd function the integral over symmetric limits is zero, so ∫₋₁¹ x³ dx = 0."),
      p("Check directly: [x⁴/4]₋₁¹ = 1/4 − 1/4 = 0. The areas above and below the axis cancel.")]),
    ("ig22", "If ∫₀¹ f(x) dx = 2 and ∫₁³ f(x) dx = 5, find ∫₀³ f(x) dx.",
     [p("Use the splitting property: the integral over 0 to 3 is the sum of the two pieces."),
      p("∫₀³ f = ∫₀¹ f + ∫₁³ f = 2 + 5 = 7."),
      p("This is how a table of measured values is combined when the readings stop at a point.")]),
    ("ig23", "Find the area under y = x² from x = 0 to x = 3.",
     [p("The curve is above the axis on this interval, so the area is ∫₀³ x² dx."),
      p("= [x³/3]₀³ = 27/3 − 0 = 9."),
      p("The area is 9 square units. Integrating raises the degree, so the answer divided by the "
        "width (3) gives an average height of 3, which matches the curve at its midpoint.")]),
    ("ig24", "Find the area between y = 4x − x² and the x-axis.",
     [p("First find where the curve meets the axis: 4x − x² = x(4 − x) = 0, so x = 0 and x = 4."),
      p("The curve is above the axis between them, so the area is ∫₀⁴ (4x − x²) dx = "
        "[2x² − x³/3]₀⁴."),
      p("= 32 − 64/3 = 96/3 − 64/3 = 32/3 ≈ 10.67 square units.")]),
    ("ig25", "Find the volume when y = x is rotated about the x-axis from x = 0 to x = 2.",
     [p("Each slice is a disc of radius y = x, so V = π∫ y² dx."),
      p("V = π∫₀² x² dx = π[x³/3]₀² = 8π/3."),
      p("The volume is 8π/3 ≈ 8.38 cubic units - a cone of height 2 and base radius 2, which has "
        "volume (1/3)πr²h = 8π/3 exactly.")]),
    ("ig26", "Find the volume when y = √x is rotated about the x-axis from x = 0 to x = 4.",
     [p("The radius of each slice is y = √x, so V = π∫ y² dx = π∫₀⁴ x dx."),
      p("= π[x²/2]₀⁴ = π(8 − 0) = 8π."),
      p("The volume is 8π ≈ 25.13 cubic units, three times the volume of the cone in the previous "
        "example because the curve stays further from the axis.")]),
]

NUMERICALS = [{"id": i, "q": tr(q), "a": tr("".join(parts))} for i, q, parts in _NUM]

EQUATIONS = [
    {"title": tr("Standard integrals"),
     "items": [
         {"terms": tr("Power rule"), "a": tr("∫ xⁿ dx = xⁿ⁺¹/(n + 1) + c,  n ≠ −1")},
         {"terms": tr("Reciprocal"), "a": tr("∫ (1/x) dx = log|x| + c")},
         {"terms": tr("Exponential"), "a": tr("∫ eˣ dx = eˣ + c ;  ∫ e^(ax) dx = e^(ax)/a + c")},
         {"terms": tr("Sine and cosine"), "a": tr("∫ sin x dx = −cos x + c ;  ∫ cos x dx = sin x + c")},
         {"terms": tr("Tangent family"), "a": tr("∫ sec²x dx = tan x + c")},
         {"terms": tr("Constant"), "a": tr("∫ k dx = kx + c")},
     ]},
    {"title": tr("Methods"),
     "items": [
         {"terms": tr("Sum and constant multiple"), "a": tr("∫ (f ± g) = ∫f ± ∫g ;  ∫ kf = k∫f")},
         {"terms": tr("Substitution"), "a": tr("∫ f(u) du with u = g(x), du = g′(x) dx")},
         {"terms": tr("Substitution in a power"), "a": tr("∫ [g(x)]ⁿ g′(x) dx = [g(x)]ⁿ⁺¹/(n + 1) + c")},
         {"terms": tr("Integration by parts"), "a": tr("∫ u dv = uv − ∫ v du")},
         {"terms": tr("LIATE order for u"), "a": tr("log, inverse trig, algebra, trig, exponential")},
         {"terms": tr("Logarithm by parts"), "a": tr("∫ log x dx = x log x − x + c")},
     ]},
    {"title": tr("Definite integrals and applications"),
     "items": [
         {"terms": tr("Fundamental theorem"), "a": tr("∫ from a to b of f(x) dx = F(b) − F(a)")},
         {"terms": tr("Reversed limits"), "a": tr("∫ from a to b = − ∫ from b to a")},
         {"terms": tr("Splitting the interval"), "a": tr("∫ from a to b = ∫ from a to c + ∫ from c to b")},
         {"terms": tr("Odd and even functions"), "a": tr("odd: ∫ from −a to a = 0 ;  even: ∫ from −a to a = 2∫ from 0 to a")},
         {"terms": tr("Area under a curve"), "a": tr("A = ∫ from a to b of y dx")},
         {"terms": tr("Volume of revolution"), "a": tr("V = π ∫ from a to b of y² dx")},
     ]},
]

VIVA = [
    {"title": tr("Basics"),
     "items": [
         {"q": tr("What is integration?"),
          "a": tr("The reverse of differentiation: finding a function whose derivative is the given "
                  "integrand.")},
         {"q": tr("Why does an indefinite integral end with + c?"),
          "a": tr("Because every constant differentiates to zero, so all the curves F(x) + c have the "
                  "same slope. A condition on the curve fixes c.")},
         {"q": tr("What is the difference between a definite and an indefinite integral?"),
          "a": tr("An indefinite integral gives a function plus c; a definite integral has limits and "
                  "gives a number.")},
         {"q": tr("Why is there no + c in a definite integral?"),
          "a": tr("The constant cancels when the limits are subtracted: (F(b) + c) − (F(a) + c) = "
                  "F(b) − F(a).")},
         {"q": tr("What is ∫ (1/x) dx and why is the modulus there?"),
          "a": tr("log|x| + c. The modulus is needed because 1/x is defined for negative x too, and "
                  "log of a negative number does not exist.")},
     ]},
    {"title": tr("Methods"),
     "items": [
         {"q": tr("When do you use substitution?"),
          "a": tr("When one part of the integrand is (a constant multiple of) the derivative of "
                  "another part, so the integral reduces to a standard form in u.")},
         {"q": tr("In a definite integral, what must be done to the limits after substituting?"),
          "a": tr("They must be converted to the new variable using u = g(x); keeping the old x-limits "
                  "with a u-integral is a common error.")},
         {"q": tr("State the formula for integration by parts."),
          "a": tr("∫ u dv = uv − ∫ v du.")},
         {"q": tr("How do you choose u in integration by parts?"),
          "a": tr("By LIATE: logarithm, inverse trig, algebraic, trigonometric, exponential - u is the "
                  "function that comes first in the list.")},
         {"q": tr("How do you integrate log x?"),
          "a": tr("By parts with u = log x and dv = dx, giving x log x − x + c.")},
         {"q": tr("How can you check any indefinite integral?"),
          "a": tr("Differentiate the answer; it must give the integrand back exactly.")},
     ]},
    {"title": tr("Applications"),
     "items": [
         {"q": tr("What does a definite integral represent geometrically?"),
          "a": tr("The signed area between the curve and the x-axis over the interval: positive above "
                  "the axis, negative below it.")},
         {"q": tr("How do you find the area under a curve?"),
          "a": tr("Integrate y with respect to x between the two limits, splitting the interval where "
                  "the curve crosses the axis.")},
         {"q": tr("Give the formula for the volume of revolution about the x-axis."),
          "a": tr("V = π ∫ y² dx between the limits, because each slice is a disc of radius y.")},
         {"q": tr("Why is y squared in the volume formula?"),
          "a": tr("The disc area is πr² with r = y, so the square comes from the geometry of the "
                  "circle, not from the integration.")},
         {"q": tr("What happens to the sign of an integral when the limits are swapped?"),
          "a": tr("The sign changes: ∫ from a to b = − ∫ from b to a.")},
         {"q": tr("An integral of zero over symmetric limits - what does it mean?"),
          "a": tr("The areas above and below the axis are equal in size; this always happens for an "
                  "odd function such as x³.")},
     ]},
]

_PRACTICE = [
    ("Evaluate ∫ 6x⁵ dx.", 3,
     [p("Use the power rule: raise the power by one and divide by the new power."),
      p("∫ 6x⁵ dx = 6x⁶/6 + c = x⁶ + c."),
      p("Check by differentiating: d(x⁶)/dx = 6x⁵, which is exactly the integrand, so the answer is "
        "right.")]),
    ("Evaluate ∫ (4x³ − 6x + 5) dx.", 3,
     [p("Integrate term by term: 4x³ gives x⁴, −6x gives −3x², and 5 gives 5x."),
      p("So the answer is x⁴ − 3x² + 5x + c."),
      p("Check: differentiating x⁴ − 3x² + 5x gives 4x³ − 6x + 5, exactly the integrand, so no term "
        "has been lost.")]),
    ("Evaluate ∫ (3/x + eˣ) dx.", 3,
     [p("Both terms are standard forms: 3/x integrates to 3 log|x| and eˣ to eˣ."),
      p("So the answer is 3 log|x| + eˣ + c."),
      p("The modulus is needed because 3/x exists for negative x as well.")]),
    ("Evaluate ∫ cos 4x dx.", 3,
     [p("Integrate cos to sin and divide by the derivative of the angle, which is 4."),
      p("∫ cos 4x dx = sin(4x)/4 + c."),
      p("Check: differentiating sin(4x)/4 gives 4 cos(4x)/4 = cos 4x, so the division by the angle's "
        "derivative is correct.")]),
    ("Evaluate ∫ (3x + 2)⁵ dx.", 4,
     [p("Substitute u = 3x + 2, so du = 3 dx and dx = du/3."),
      p("The integral becomes (1/3)∫ u⁵ du = u⁶/18 + c = (3x + 2)⁶/18 + c."),
      p("Check: differentiating (3x + 2)⁶/18 gives 6(3x + 2)⁵ × 3/18 = (3x + 2)⁵, so the answer is "
        "correct.")]),
    ("Evaluate ∫ x²(x³ + 1)⁴ dx.", 4,
     [p("Take u = x³ + 1, so du = 3x² dx, that is x² dx = du/3."),
      p("The integral becomes (1/3)∫ u⁴ du = u⁵/15 + c = (x³ + 1)⁵/15 + c."),
      p("Check by differentiating: 5(x³ + 1)⁴ × 3x²/15 = x²(x³ + 1)⁴.")]),
    ("Evaluate ∫ (2x + 1)/(x² + x) dx.", 4,
     [p("The numerator is the derivative of the denominator: d(x² + x)/dx = 2x + 1."),
      p("So with u = x² + x the integral is ∫ du/u = log|u| + c = log|x² + x| + c."),
      p("The modulus matters here, because x² + x is negative for x between −1 and 0.")]),
    ("Evaluate ∫ x sin x dx by parts.", 4,
     [p("Take u = x (du = dx) and dv = sin x dx (v = −cos x)."),
      p("∫ x sin x dx = −x cos x − ∫ (−cos x) dx = −x cos x + sin x + c."),
      p("Check: differentiating gives −cos x + x sin x + cos x = x sin x.")]),
    ("Evaluate ∫ x² log x dx.", 4,
     [p("By LIATE choose u = log x and dv = x² dx, so du = dx/x and v = x³/3."),
      p("The integral = (x³/3)log x − ∫ (x³/3)(1/x) dx = (x³/3)log x − ∫ (x²/3) dx."),
      p("So the answer is (x³/3)log x − x³/9 + c.")]),
    ("Evaluate ∫₁² (2x + 3) dx.", 3,
     [p("Integrate: [x² + 3x]₁²."),
      p("Upper limit: 4 + 6 = 10. Lower limit: 1 + 3 = 4."),
      p("The value is 10 − 4 = 6, and no + c is written because the constant cancels in a definite "
        "integral.")]),
    ("Evaluate ∫₀¹ x e^(x²) dx.", 4,
     [p("Substitute u = x², so du = 2x dx and x dx = du/2. The limits 0 and 1 become 0 and 1."),
      p("The integral is (1/2)∫₀¹ eᵘ du = (1/2)[eᵘ]₀¹ = (e − 1)/2."),
      p("Numerically this is about 0.859.")]),
    ("Evaluate ∫₀^(π/2) cos x dx.", 3,
     [p("The integral of cos x is sin x, so the value is [sin x] from 0 to π/2."),
      p("sin(π/2) = 1 and sin 0 = 0, so the answer is 1."),
      p("The area under one quarter of the cosine curve is exactly 1 square unit.")]),
    ("Find the area under y = x³ from x = 0 to x = 2.", 4,
     [p("The curve is above the axis on 0 to 2, so the area is ∫₀² x³ dx."),
      p("= [x⁴/4]₀² = 16/4 = 4."),
      p("The area is 4 square units; a rectangle of the same width with average height 2 would have "
        "the same area.")]),
    ("Find the area between y = x² and the x-axis from x = 1 to x = 3.", 4,
     [p("The curve is above the axis throughout, so the area is ∫₁³ x² dx."),
      p("= [x³/3]₁³ = 27/3 − 1/3 = 26/3."),
      p("The area is 26/3 ≈ 8.67 square units. The average height over the interval is the area "
        "divided by the width, about 4.33, which sits between the curve heights 1 and 9.")]),
    ("Find the volume when y = √x is rotated about the x-axis from x = 0 to x = 4.", 4,
     [p("Each slice is a disc of radius y = √x, so V = π∫₀⁴ y² dx = π∫₀⁴ x dx."),
      p("= π[x²/2]₀⁴ = π(8 − 0) = 8π."),
      p("The volume is 8π ≈ 25.13 cubic units, and the answer is left in terms of π because the "
        "question gives no decimals.")]),
]

EXAM = [{"q": tr(q), "marks": m} for q, m, _parts in _PRACTICE]
PRACTICE_ANSWERS = [tr("".join(parts)) for _q, _m, parts in _PRACTICE]

LESSON_COUNT = sum(len(s["items"]) for s in NOTES)
