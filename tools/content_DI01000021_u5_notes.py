"""DI01000021 Mathematics-I - Unit 5: Limit (GTU 5.1-5.2, 7 h, 17 %, 12 marks)."""
from subject_DI01000021 import tr


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
    ("GTU DI01000021, Mathematics-I, Branch: All, Semester 1, w.e.f. 2024-25 (uploaded syllabus)",
     "https://s3-ap-southeast-1.amazonaws.com/gtusitecirculars/Syallbus/DI01000021.pdf"),
    ("NCERT - Class 11 Mathematics, chapter 13 (limits and derivatives)",
     "https://ncert.nic.in/textbook.php"),
    ("OpenStax - Calculus Volume 1, chapter 2 (limits)",
     "https://openstax.org/details/books/calculus-volume-1"),
    ("Khan Academy - limits and continuity",
     "https://www.khanacademy.org/math/ap-calculus-ab/ab-limits-new"),
]

NOTES = [
    {"title": tr("1. What a Limit Means"),
     "items": [
         card("1.1 The idea and the notation",
              h4("Definition")
              + p("The <b>limit</b> of f(x) as x approaches a is the single value that f(x) closes in on when x "
                  "gets arbitrarily close to a, <i>without</i> ever needing x to equal a. We write "
                  "lim<sub>x→a</sub> f(x) = L.")
              + h4("Read it as a question")
              + p("\"If x creeps up to <i>a</i>, where does the output go?\" The value f(a) itself is irrelevant: "
                  "the function may be undefined at a, may have a different value there, or may be perfectly "
                  "well behaved. A limit describes the <i>approach</i>, not the arrival.")
              + h4("A hole in a graph")
              + p("Take f(x) = (x² − 1)/(x − 1). At x = 1 the formula gives 0/0, which means nothing. But for "
                  "every x ≠ 1, (x² − 1)/(x − 1) = x + 1, so the graph is the line y = x + 1 with a single "
                  "missing point at (1, 2). The limit exists and equals 2, even though f(1) does not.")
              + h4("Why engineers care")
              + p("Velocity is a limit of an average speed as the time gap shrinks to zero, current is a limit "
                  "of charge per unit time, and stress is a limit of force per unit area. Every derivative in "
                  "the next semester is built from exactly this idea.")
              + sc("Is the limit the same as the value of the function?", "No. The limit is what the function "
                     "approaches; the value is what it actually equals. They agree only when the function is "
                     "continuous at that point."),
              "l1_hole", examples=["lm1n1", "lm1n2"], syllabus_item="5.1"),
         card("1.2 Left-hand, right-hand and two-sided limits",
              h4("Two approaches")
              + p("The <b>left-hand limit</b> lim<sub>x→a⁻</sub> f(x) uses x &lt; a. The <b>right-hand limit</b> "
                  "lim<sub>x→a⁺</sub> f(x) uses x &gt; a. Each one is a one-way approach.")
              + h4("Existence rule")
              + p("The two-sided limit exists <b>only when both one-sided limits exist and are equal</b>: "
                  "lim<sub>x→a⁻</sub> f = lim<sub>x→a⁺</sub> f = L. If they differ, the limit does not exist, "
                  "however close the two values happen to be.")
              + h4("Worked example")
              + p("For f(x) = x + 2 when x &lt; 1 and f(x) = 4x when x ≥ 1: the left limit is 1 + 2 = 3 and the "
                  "right limit is 4(1) = 4. They differ, so lim<sub>x→1</sub> f(x) does not exist; the graph jumps.")
              + h4("Modulus example")
              + p("f(x) = |x|/x gives −1 from the left and +1 from the right, so the limit at 0 fails even though "
                  "the function is defined on both sides. Writing the two cases explicitly is the safe method.")
              + sc("Can a limit exist if the function is not defined at a?", "Yes. Both one-sided limits can "
                     "agree without f(a) being defined at all."),
              "l2_sided", examples=["lm1n21"], syllabus_item="5.1"),
         card("1.3 When a limit does not exist",
              h4("Three standard reasons")
              + ol("The two one-sided limits disagree (a jump).",
                   "The values grow without bound, as in 1/x² near 0 (an infinite blow-up).",
                   "The values never settle, as in sin(1/x) near 0 (oscillation).")
              + h4("What to write in an answer")
              + p("Say \"does not exist\" and give the evidence: \"left limit = 3, right limit = 4, so the limit "
                  "does not exist\". The reason earns the mark; the phrase alone does not.")
              + h4("Infinite limits")
              + p("When a function tends to +∞ we sometimes write lim = ∞, but that is a description of the "
                  "behaviour, not a real number, so the limit is still said not to exist.")
              + h4("Common mistake")
              + p("Substituting x = a first and writing 0/0 as the answer. 0/0 is not a value - it is a signal "
                  "that algebra is still needed."),
              examples=["lm1n22"], syllabus_item="5.1")]},

    {"title": tr("2. Algebra of Limits"),
     "items": [
         card("2.1 The limit laws",
              h4("Rules")
              + p("If lim f = L and lim g = M both exist, then lim (f ± g) = L ± M, lim (fg) = LM, "
                  "lim (f/g) = L/M (provided M ≠ 0) and lim (k f) = kL. A constant has limit equal to itself, "
                  "and lim x = a.")
              + h4("Direct substitution")
              + p("For a polynomial, or a ratio of polynomials with a non-zero denominator, the limit is simply "
                  "the value at the point: substitute and finish. The laws above are what make that legal.")
              + h4("Worked example")
              + p("lim<sub>x→2</sub> (3x² − 5x + 1) = 3(4) − 5(2) + 1 = 12 − 10 + 1 = 3, by substitution and the "
                  "sum and product rules. No algebra needed.")
              + h4("Order matters")
              + p("Check the denominator first. If it is non-zero at the point, substitution ends the question. "
                  "If it is zero, the algebra has not started yet.")
              + sc("Does the quotient law apply when the denominator limit is zero?", "No. That case is an "
                     "indeterminate form and needs factorisation, rationalisation or a standard limit."),
              "l3_table", examples=["lm1n1", "lm1n7"], syllabus_item="5.2"),
         card("2.2 Indeterminate forms",
              h4("What 0/0 means")
              + p("A form such as 0/0 or ∞/∞ is called <b>indeterminate</b>: it tells you the answer is not yet "
                  "decided. Two different functions can both give 0/0 at the same point and still have limits 0, "
                  "5 or ∞.")
              + h4("A numerical check")
              + p("For (x² − 1)/(x − 1), substituting x = 1.1, 1.01 and 1.001 gives 2.1, 2.01 and 2.001. The "
                  "table points at 2. A table of values is the quickest way to guess a limit and a natural way "
                  "to confirm an algebra answer.")
              + h4("Forms that are not indeterminate")
              + p("3/0 is not 0/0 - it is an infinite blow-up. 0/5 is simply 0. 5/0 is unbounded. Only 0/0, "
                  "∞/∞, 0·∞, ∞ − ∞, 1<sup>∞</sup>, 0⁰ and ∞⁰ need work.")
              + h4("The three workhorses")
              + p("Factorise and cancel (removes a common zero), rationalise (removes a root), or divide by the "
                  "highest power (handles infinity). Almost every question in this unit is one of the three.")
              + sc("Is 0/0 equal to 1?", "No. 0/0 has no value. The phrase only says the numerator and the "
                     "denominator both vanish at the point."),
              examples=["lm1n3", "lm1n8"], syllabus_item="5.2")]},

    {"title": tr("3. Techniques that Remove the 0/0"),
     "items": [
         card("3.1 Factorisation and cancellation",
              h4("Method")
              + ol("Substitute; if you get a non-zero number, stop.",
                   "If you get 0/0, factorise the numerator and the denominator.",
                   "Cancel the common factor that caused the zero.",
                   "Substitute again into what is left.")
              + h4("Worked example")
              + p("lim<sub>x→3</sub> (x² − 9)/(x − 3) = lim (x − 3)(x + 3)/(x − 3) = lim (x + 3) = 6. The "
                  "cancellation is legal because x ≠ 3 while the limit is being taken, so the factor is never "
                  "actually zero.")
              + h4("Extension to xⁿ − aⁿ")
              + p("x³ − 1 = (x − 1)(x² + x + 1), and in general xⁿ − aⁿ = (x − a)(xⁿ⁻¹ + xⁿ⁻²a + … + "
                  "aⁿ⁻¹). That identity settles every (xⁿ − aⁿ)/(x − a) question at once.")
              + h4("Common mistake")
              + p("Cancelling terms that are added rather than multiplied. Only factors cancel: (x² − 9)/(x − 3) "
                  "is fine, but (x² − 9)/(x − 3) is not x² − 3."),
              "l6_flow", examples=["lm1n2", "lm1n3", "lm1n4"], syllabus_item="5.2"),
         card("3.2 Rationalising a square root",
              h4("Method")
              + p("When a square root causes the 0/0, multiply the numerator and the denominator by the "
                  "<b>conjugate</b> of the root expression. This uses (A − B)(A + B) = A² − B² and turns the "
                  "difference of roots into a plain expression.")
              + h4("Worked example")
              + p("lim<sub>x→0</sub> (√(1 + x) − 1)/x, multiplied by (√(1 + x) + 1)/(√(1 + x) + 1), becomes "
                  "lim x/(x(√(1 + x) + 1)) = lim 1/(√(1 + x) + 1) = 1/2.")
              + h4("What to expect")
              + p("The answer is usually <i>not</i> zero, because the root grows more slowly than x. For "
                  "√(1 + x) − 1 the linear behaviour is x/2, which is exactly why the limit is 1/2.")
              + h4("Common mistake")
              + p("Multiplying only the numerator. The value of the fraction must not change, so both parts get "
                  "the conjugate."),
              examples=["lm1n5", "lm1n6"], syllabus_item="5.2"),
         card("3.3 Limits at infinity",
              h4("The degree rule")
              + p("For a ratio of polynomials as x → ∞, divide every term by the highest power of x in the "
                  "denominator. Equivalent shortcut: compare degrees.")
              + table(["Degrees", "Limit as x → ∞", "Example"],
                      [("numerator &lt; denominator", "0", "x/(x² + 1) → 0"),
                       ("equal", "ratio of leading coefficients", "(3x² + 2x)/(5x² − 1) → 3/5"),
                       ("numerator &gt; denominator", "unbounded (±∞)", "x³/(x + 1) → ∞")])
              + h4("Roots at infinity")
              + p("For √(x² + 3x) − x, multiply by the conjugate: the numerator becomes 3x and the denominator "
                  "√(x² + 3x) + x ≈ 2x, so the limit is 3/2.")
              + h4("Useful fact")
              + p("As x → ∞, 1/x → 0, 1/x² → 0, and k/xⁿ → 0 for any positive power. Every finite limit at "
                  "infinity comes from throwing away those vanishing terms.")
              + sc("What is lim x→∞ (5x + 3)/(2x − 7)?", "5/2 - equal degrees, so the ratio of the leading "
                     "coefficients."),
              examples=["lm1n8", "lm1n9", "lm1n10"], syllabus_item="5.2")]},

    {"title": tr("4. Standard Limits"),
     "items": [
         card("4.1 The trigonometric limits",
              h4("The key limit")
              + p("<b>lim<sub>x→0</sub> (sin x)/x = 1</b> (x in radians). It is the reason the derivative of sin x "
                  "comes out as cos x, and it is true only in radian measure.")
              + h4("Companions")
              + p("lim (tan x)/x = 1, lim (1 − cos x)/x² = 1/2, and lim (sin ax)/(bx) = a/b. Each follows from "
                  "the key limit by rewriting: tan x = (sin x)/x · 1/(cos x), and 1 − cos x = 2sin²(x/2).")
              + h4("Worked example")
              + p("lim<sub>x→0</sub> (sin 3x)/(sin 7x) = (3/7) · [(sin 3x)/(3x)] · [(7x)/(sin 7x)] = 3/7, "
                  "because both bracketed factors tend to 1.")
              + h4("Common mistake")
              + p("Writing sin x ≈ x and then cancelling x in a sum such as (x − sin x)/x³. The first-order "
                  "approximation is too coarse there; you need the next term (sin x = x − x³/6 + …)."),
              "l4_sinx", examples=["lm1n11", "lm1n12", "lm1n13", "lm1n14"], syllabus_item="5.2"),
         card("4.2 The number e",
              h4("Definition")
              + p("<b>lim<sub>x→0</sub> (1 + x)<sup>1/x</sup> = e</b> and <b>lim<sub>n→∞</sub> (1 + 1/n)<sup>n</sup> "
                  "= e</b>, where e ≈ 2.718281828. The number e is defined by this limit, not assumed.")
              + h4("General form")
              + p("lim<sub>x→0</sub> (1 + ax)<sup>b/x</sup> = e<sup>ab</sup>, and "
                  "lim<sub>x→∞</sub> (1 + a/x)<sup>bx</sup> = e<sup>ab</sup>. The exponent multiplies with the "
                  "coefficient inside - that product is the exponent of e.")
              + h4("Worked example")
              + p("lim<sub>x→0</sub> (1 + 3x)<sup>1/x</sup> = e³. Check with x = 0.001: (1.003)¹⁰⁰⁰ ≈ 20.0, and "
                  "e³ ≈ 20.09 - a good match.")
              + h4("Where it comes from")
              + p("Compounding interest n times a year at rate r gives (1 + r/n)<sup>n</sup>. As n → ∞ the growth "
                  "factor becomes e<sup>r</sup>: continuous compounding is a limit, not a new rule.")
              + sc("Why is e important in engineering?", "Exponential growth, decay, RC circuits and cooling "
                     "curves all have e as their natural base, so limits of this form appear everywhere."),
              "l5_e", examples=["lm1n16", "lm1n17"], syllabus_item="5.2"),
         card("4.3 Exponential, logarithmic and power limits",
              h4("Three more standards")
              + p("<b>lim<sub>x→0</sub> (e<sup>x</sup> − 1)/x = 1</b>, <b>lim<sub>x→0</sub> (a<sup>x</sup> − 1)/x "
                  "= log a</b>, and <b>lim<sub>x→0</sub> log(1 + x)/x = 1</b>.")
              + h4("Power form")
              + p("lim<sub>x→0</sub> ((1 + x)<sup>n</sup> − 1)/x = n for any constant n, and more generally "
                  "lim<sub>x→a</sub> (x<sup>n</sup> − a<sup>n</sup>)/(x − a) = n a<sup>n−1</sup>.")
              + h4("Worked example")
              + p("lim<sub>x→0</sub> (3<sup>x</sup> − 1)/x = log 3 ≈ 1.0986. If the base is e the answer is log e "
                  "= 1, which is exactly the first formula in this card.")
              + h4("Reading the log")
              + p("In this syllabus log means the natural logarithm (base e). With base 10 the same question would "
                  "give log₁₀a, so state the convention whenever the base matters.")
              + h4("Common mistake")
              + p("Forgetting that the denominator must be exactly x. For (e<sup>2x</sup> − 1)/x the answer is 2, "
                  "not 1: substitute u = 2x and carry the factor."),
              examples=["lm1n18", "lm1n19", "lm1n20", "lm1n22"], syllabus_item="5.2")]},

    {"title": tr("5. Continuity and Exam Technique"),
     "items": [
         card("5.1 Continuity at a point",
              h4("Definition")
              + p("f is <b>continuous</b> at x = a when three things hold: f(a) is defined, lim<sub>x→a</sub> f(x) "
                  "exists, and the two are equal. In one line: lim<sub>x→a</sub> f(x) = f(a).")
              + h4("Types of discontinuity")
              + table(["Type", "What happens", "Example"],
                      [("Removable", "the limit exists but f(a) is missing or wrong", "(x² − 1)/(x − 1) at 1"),
                       ("Jump", "the two one-sided limits differ", "x + 2 for x &lt; 1, 4x for x ≥ 1"),
                       ("Infinite", "values blow up", "1/x² at 0")])
              + h4("How to test a piecewise function")
              + ol("Find the left limit.", "Find the right limit.", "Compare both with f(a).",
                   "Conclude: equal to f(a) means continuous; equal to each other but not f(a) means removable; "
                   "different means a jump.")
              + h4("Exam wording")
              + p("A continuity question almost always hides a limit question. Do the limits first, then quote "
                  "the definition - never the other way round."),
              "l2_sided", examples=["lm1n21"], syllabus_item="5.1"),
         card("5.2 A checking routine and common errors",
              h4("Five-step routine")
              + ol("Substitute the point. A finite number is the answer.",
                   "If you get 0/0, factorise, rationalise or use a standard limit.",
                   "If the variable tends to infinity, divide by the highest power.",
                   "For a piecewise function, do both one-sided limits.",
                   "Check the sign and the size of the answer against a nearby value in a table.")
              + h4("Errors that cost marks")
              + ul("Writing 0/0 as the final answer.",
                   "Cancelling before factorising, or cancelling added terms.",
                   "Using degrees in sin x/x - the limit 1 needs radians.",
                   "Dropping the constant in (e<sup>2x</sup> − 1)/x, which is 2, not 1.",
                   "Forgetting that a one-sided limit is still a limit and must be labelled.")
              + h4("Answer format")
              + p("State the form you started with, show the algebra, then give the value: \"form 0/0; "
                  "factorising gives (x + 3); limit = 6\". Two lines of reasoning is usually enough for full marks.")
              + sc("What is the first thing to try in any limit question?", "Direct substitution - it settles "
                     "the easy cases instantly and tells you which of the three methods you need."),
              examples=["lm1n15", "lm1n23", "lm1n24"], syllabus_item="5.2")]},

    {"title": tr("6. Answered Practice (Unit 5 level, suggested marks)"),
     "items": []}]

NUMERICALS = []


def num(nid, q, chunks):
    return {"id": nid, "q": tr(q), "a": tr("".join(chunks))}


NUMERICALS += [
    num("lm1n1", "Evaluate lim (3x² − 5x + 1) as x → 2.",
        [h4("Given and assumptions"),
         p("A polynomial, so the limit laws allow direct substitution."),
         h4("Formula"), p("lim<sub>x→a</sub> f(x) = f(a) when f is a polynomial."),
         h4("Step-by-step solution"),
         p("3(2)² − 5(2) + 1 = 12 − 10 + 1 = 3"),
         h4("Interpretation and check"),
         p("<b>3.</b> A polynomial has no holes or jumps, so the limit equals the value: f(2) = 3 ✓. "
           "Substituting x = 2.001 gives 3.001, confirming the approach from the right.")]),
    num("lm1n2", "Evaluate lim (x² − 9)/(x − 3) as x → 3.",
        [h4("Given and assumptions"),
         p("Substituting x = 3 gives 0/0, an indeterminate form; the factor (x − 3) is common."),
         h4("Formula"), p("x² − a² = (x − a)(x + a)."),
         h4("Step-by-step solution"),
         ol("Substitute: (9 − 9)/(3 − 3) = 0/0 - indeterminate.",
            "Factorise: x² − 9 = (x − 3)(x + 3).",
            "Cancel (x − 3), valid because x ≠ 3.",
            "lim (x + 3) = 6."),
         h4("Interpretation and check"),
         p("<b>6.</b> The graph is the line y = x + 3 with a hole at (3, 6). A table gives x = 2.9 → 5.9 and "
           "x = 3.1 → 6.1, so both sides close in on 6 ✓.")]),
    num("lm1n3", "Evaluate lim (x³ − 1)/(x − 1) as x → 1.",
        [h4("Given and assumptions"),
         p("Substitution gives 0/0. The numerator is a difference of cubes with a = 1."),
         h4("Formula"), p("x³ − a³ = (x − a)(x² + ax + a²)."),
         h4("Step-by-step solution"),
         ol("x³ − 1 = (x − 1)(x² + x + 1)",
            "Cancel (x − 1)",
            "lim (x² + x + 1) = 1 + 1 + 1 = 3"),
         h4("Interpretation and check"),
         p("<b>3.</b> Using the standard form (xⁿ − aⁿ)/(x − a) → n a<sup>n−1</sup> with n = 3, a = 1 gives "
           "3 ✓. At x = 1.01 the expression equals 3.0301, which is close to 3.")]),
    num("lm1n4", "Evaluate lim (x² − 4)/(x² − 5x + 6) as x → 2.",
        [h4("Given and assumptions"),
         p("0/0 at x = 2. Both quadratics factor with (x − 2)."),
         h4("Formula"), p("Factorise numerator and denominator, cancel the common factor."),
         h4("Step-by-step solution"),
         ol("x² − 4 = (x − 2)(x + 2)", "x² − 5x + 6 = (x − 2)(x − 3)",
            "Cancel (x − 2): lim (x + 2)/(x − 3)",
            "Substitute x = 2: 4/(−1) = −4"),
         h4("Interpretation and check"),
         p("<b>−4.</b> The denominator is negative just above 2 (x − 3 &lt; 0) while the numerator is positive, "
           "so a negative limit is expected. At x = 2.01 the value is ≈ −4.01 ✓.")]),
    num("lm1n5", "Evaluate lim (√(1 + x) − 1)/x as x → 0.",
        [h4("Given and assumptions"),
         p("0/0 at x = 0, caused by the square root. Rationalise with the conjugate √(1 + x) + 1."),
         h4("Formula"), p("(A − B)(A + B) = A² − B²."),
         h4("Step-by-step solution"),
         ol("Multiply above and below by (√(1 + x) + 1)",
            "Numerator becomes (1 + x) − 1 = x",
            "lim x/[x(√(1 + x) + 1)] = lim 1/(√(1 + x) + 1)",
            "Substitute x = 0: 1/(1 + 1) = 1/2"),
         h4("Interpretation and check"),
         p("<b>1/2.</b> This is the standard binomial result √(1 + x) ≈ 1 + x/2 for small x, so the limit 1/2 is "
           "exact. At x = 0.01 the expression is 0.4988 ✓.")]),
    num("lm1n6", "Evaluate lim (√x − 2)/(x − 4) as x → 4.",
        [h4("Given and assumptions"),
         p("0/0 at x = 4. The denominator is a difference of squares in √x."),
         h4("Formula"), p("x − 4 = (√x − 2)(√x + 2)."),
         h4("Step-by-step solution"),
         ol("Factorise the denominator: x − 4 = (√x)² − 2² = (√x − 2)(√x + 2)",
            "Cancel (√x − 2)",
            "lim 1/(√x + 2)",
            "Substitute x = 4: 1/(2 + 2) = 1/4"),
         h4("Interpretation and check"),
         p("<b>1/4.</b> Since d(√x)/dx = 1/(2√x), at x = 4 the slope is 1/4 - the limit is that slope ✓. "
           "At x = 4.01 the value is 0.2498.")]),
    num("lm1n7", "Evaluate lim (1/x − 1/3)/(x − 3) as x → 3.",
        [h4("Given and assumptions"),
         p("0/0 at x = 3. Combine the fractions in the numerator first."),
         h4("Formula"), p("1/x − 1/3 = (3 − x)/(3x)."),
         h4("Step-by-step solution"),
         ol("1/x − 1/3 = (3 − x)/(3x)",
            "Divide by (x − 3): (3 − x)/(3x(x − 3)) = −1/(3x)",
            "lim −1/(3x) = −1/9"),
         h4("Interpretation and check"),
         p("<b>−1/9.</b> The slope of 1/x at x = 3 is −1/x² = −1/9, so the answer is the derivative there ✓. "
           "At x = 3.01 the expression ≈ −0.111, consistent with −1/9 ≈ −0.1111.")]),
    num("lm1n8", "Evaluate lim (3x² + 2x − 1)/(5x² − x + 4) as x → ∞.",
        [h4("Given and assumptions"),
         p("Both polynomials have degree 2, so the leading coefficients decide."),
         h4("Formula"), p("Divide every term by x², the highest power in the denominator."),
         h4("Step-by-step solution"),
         ol("(3 + 2/x − 1/x²)/(5 − 1/x + 4/x²)",
            "As x → ∞ each term with 1/x or 1/x² tends to 0",
            "Limit = 3/5"),
         h4("Interpretation and check"),
         p("<b>3/5 = 0.6.</b> Equal degrees give the ratio of leading coefficients ✓. At x = 1000 the value is "
           "≈ 0.599, converging to 0.6.")]),
    num("lm1n9", "Evaluate lim (2x³ − x)/(x³ + 4x²) as x → ∞.",
        [h4("Given and assumptions"),
         p("Both have degree 3. Divide by x³."),
         h4("Formula"), p("Term-by-term division by the highest power."),
         h4("Step-by-step solution"),
         ol("(2 − 1/x²)/(1 + 4/x)",
            "1/x² → 0 and 4/x → 0",
            "Limit = 2/1 = 2"),
         h4("Interpretation and check"),
         p("<b>2.</b> The cubes dominate both the numerator and the denominator, and the ratio of the leading "
           "coefficients is 2 ✓. At x = 100 the value is 1.96.")]),
    num("lm1n10", "Evaluate lim (√(x² + 3x) − x) as x → ∞.",
        [h4("Given and assumptions"),
         p("∞ − ∞ is indeterminate, so multiply by the conjugate to turn it into a fraction."),
         h4("Formula"), p("(√(x² + 3x) − x)(√(x² + 3x) + x) = 3x."),
         h4("Step-by-step solution"),
         ol("Multiply and divide by (√(x² + 3x) + x)",
            "Numerator becomes (x² + 3x) − x² = 3x",
            "Expression = 3x/(√(x² + 3x) + x)",
            "Divide above and below by x: 3/(√(1 + 3/x) + 1)",
            "Limit = 3/(1 + 1) = 3/2"),
         h4("Interpretation and check"),
         p("<b>3/2 = 1.5.</b> At x = 100 the expression is 1.488, and at x = 10 000 it is 1.4999 ✓. The answer "
           "is finite because the square root grows only like x plus a correction of 3/2.")]),
    num("lm1n11", "Evaluate lim (sin 5x)/x as x → 0.",
        [h4("Given and assumptions"),
         p("sin 5x → 0 and x → 0, so the form is 0/0. Build the standard limit by inserting 5."),
         h4("Formula"), p("lim<sub>u→0</sub> (sin u)/u = 1 with u = 5x (radians)."),
         h4("Step-by-step solution"),
         ol("(sin 5x)/x = 5 · (sin 5x)/(5x)",
            "(sin 5x)/(5x) → 1 as x → 0",
            "Limit = 5 · 1 = 5"),
         h4("Interpretation and check"),
         p("<b>5.</b> In general (sin ax)/(bx) → a/b, so a = 5, b = 1 gives 5 ✓. At x = 0.001 the value is "
           "4.99999.")]),
    num("lm1n12", "Evaluate lim (sin 3x)/(sin 7x) as x → 0.",
        [h4("Given and assumptions"),
         p("0/0 form. Split each sine from its own angle."),
         h4("Formula"), p("(sin 3x)/(sin 7x) = (3x/7x) · [(sin 3x)/(3x)] · [(7x)/(sin 7x)]."),
         h4("Step-by-step solution"),
         ol("Write the ratio with 3x and 7x in place",
            "Each bracketed ratio tends to 1",
            "Limit = 3/7"),
         h4("Interpretation and check"),
         p("<b>3/7 ≈ 0.4286.</b> The ratio a/b rule gives 3/7 directly ✓. At x = 0.001 the value is 0.4286, so "
           "the approximation sin t ≈ t is already excellent.")]),
    num("lm1n13", "Evaluate lim (1 − cos x)/x² as x → 0.",
        [h4("Given and assumptions"),
         p("0/0 at x = 0. Use 1 − cos x = 2 sin²(x/2)."),
         h4("Formula"), p("lim (sin u)/u = 1, so lim (sin²u)/u² = 1."),
         h4("Step-by-step solution"),
         ol("1 − cos x = 2 sin²(x/2)",
            "(1 − cos x)/x² = 2 sin²(x/2)/x² = (1/2)[sin(x/2)/(x/2)]²",
            "The bracket tends to 1",
            "Limit = 1/2"),
         h4("Interpretation and check"),
         p("<b>1/2.</b> Because cos x ≈ 1 − x²/2 near 0, the numerator is x²/2 and the limit is 1/2 ✓. At "
           "x = 0.01 the value is 0.49999.")]),
    num("lm1n14", "Evaluate lim (tan x)/x as x → 0.",
        [h4("Given and assumptions"),
         p("0/0 form. Write tan x = sin x/cos x."),
         h4("Formula"), p("(tan x)/x = [(sin x)/x] · (1/cos x)."),
         h4("Step-by-step solution"),
         ol("(tan x)/x = (sin x)/(x cos x)",
            "(sin x)/x → 1 and cos x → 1",
            "Limit = 1/1 = 1"),
         h4("Interpretation and check"),
         p("<b>1.</b> Near 0 the tangent and the angle agree to first order, which is the geometric meaning of "
           "the limit ✓. At x = 0.01 the value is 1.00003.")]),
    num("lm1n15", "Evaluate lim (1 − cos 2x)/x² as x → 0.",
        [h4("Given and assumptions"),
         p("0/0 form with a doubled angle. Either use 1 − cos 2x = 2 sin²x or scale the standard result."),
         h4("Formula"), p("1 − cos 2x = 2 sin²x, and (sin x)/x → 1."),
         h4("Step-by-step solution"),
         ol("1 − cos 2x = 2 sin²x",
            "(1 − cos 2x)/x² = 2 (sin x/x)²",
            "Limit = 2 · 1 = 2"),
         h4("Interpretation and check"),
         p("<b>2.</b> Scaling the standard limit (1 − cos u)/u² → 1/2 with u = 2x multiplies by 4 and gives "
           "4 · 1/2 = 2 ✓. At x = 0.001 the value is 1.9999.")]),
    num("lm1n16", "Evaluate lim (1 + 3x)^(1/x) as x → 0.",
        [h4("Given and assumptions"),
         p("The form is 1<sup>∞</sup>, which is indeterminate. Compare with the definition of e."),
         h4("Formula"), p("lim (1 + ax)^(b/x) = e<sup>ab</sup>."),
         h4("Step-by-step solution"),
         ol("Write (1 + 3x)^(1/x) = [(1 + 3x)^(1/(3x))]³",
            "The bracket tends to e",
            "Limit = e³"),
         h4("Interpretation and check"),
         p("<b>e³ ≈ 20.09.</b> With x = 0.001 the expression is (1.003)¹⁰⁰⁰ ≈ 20.0 ✓, so the exact answer sits "
           "just above the numerical estimate.")]),
    num("lm1n17", "Evaluate lim (1 + 2/x)^x as x → ∞.",
        [h4("Given and assumptions"),
         p("1<sup>∞</sup> form as x → ∞; match it to lim (1 + 1/n)<sup>n</sup> = e."),
         h4("Formula"), p("lim (1 + a/x)<sup>bx</sup> = e<sup>ab</sup>."),
         h4("Step-by-step solution"),
         ol("(1 + 2/x)^x = [(1 + 2/x)^(x/2)]²",
            "The bracket tends to e",
            "Limit = e²"),
         h4("Interpretation and check"),
         p("<b>e² ≈ 7.389.</b> At x = 1000 the value is ≈ 7.374, approaching e² from below ✓ - the same "
           "undershoot seen in the sequence (1 + 1/n)<sup>n</sup>.")]),
    num("lm1n18", "Evaluate lim (e^x − 1)/x as x → 0.",
        [h4("Given and assumptions"),
         p("0/0 form. This is a standard limit, not something to differentiate."),
         h4("Formula"), p("(e<sup>x</sup> − 1)/x → 1 as x → 0."),
         h4("Step-by-step solution"),
         ol("Substitute the series e<sup>x</sup> = 1 + x + x²/2 + …",
            "e<sup>x</sup> − 1 = x + x²/2 + …",
            "Divide by x: 1 + x/2 + … → 1"),
         h4("Interpretation and check"),
         p("<b>1.</b> The gradient of e<sup>x</sup> at x = 0 is 1, and this limit <i>is</i> that gradient ✓. At "
           "x = 0.001 the value is 1.0005.")]),
    num("lm1n19", "Evaluate lim log(1 + x)/x as x → 0.",
        [h4("Given and assumptions"),
         p("0/0 form with the natural logarithm. Put 1 + x = e<sup>u</sup> or use the series."),
         h4("Formula"), p("log(1 + x) = x − x²/2 + x³/3 − …"),
         h4("Step-by-step solution"),
         ol("Expand: log(1 + x) = x − x²/2 + …",
            "Divide by x: 1 − x/2 + …",
            "Limit = 1"),
         h4("Interpretation and check"),
         p("<b>1.</b> Equivalently log(1 + x)/x = log[(1 + x)<sup>1/x</sup>] → log e = 1 ✓. At x = 0.001 the "
           "value is 0.9995.")]),
    num("lm1n20", "Evaluate lim (3^x − 1)/x as x → 0.",
        [h4("Given and assumptions"),
         p("0/0 form with an exponential of base 3. Use 3<sup>x</sup> = e<sup>x log 3</sup>."),
         h4("Formula"), p("(a<sup>x</sup> − 1)/x → log a."),
         h4("Step-by-step solution"),
         ol("3<sup>x</sup> = e<sup>x log 3</sup>",
            "Put u = x log 3, so (e<sup>u</sup> − 1)/x = log 3 · (e<sup>u</sup> − 1)/u",
            "The bracket tends to 1, so the limit is log 3"),
         h4("Interpretation and check"),
         p("<b>log 3 ≈ 1.0986.</b> The base-3 exponential grows faster than e<sup>x</sup> would at the same "
           "point only because 3 &gt; e, so a limit above 1 is expected ✓.")]),
    num("lm1n21", "The function is f(x) = x + 2 for x &lt; 1 and f(x) = 4x for x ≥ 1. Find lim f(x) as x → 1.",
        [h4("Given and assumptions"),
         p("A piecewise definition, so both one-sided limits are needed."),
         h4("Formula"), p("The limit exists only if the left and right limits agree."),
         h4("Step-by-step solution"),
         ol("Left limit: x → 1⁻ uses x + 2, giving 1 + 2 = 3",
            "Right limit: x → 1⁺ uses 4x, giving 4",
            "3 ≠ 4, so the limit does not exist"),
         h4("Interpretation and check"),
         p("The two branches meet the vertical line x = 1 at different heights, so the graph jumps from 3 to 4. "
           "Because the one-sided limits differ, no single L can be the answer ✓.")]),
    num("lm1n22", "Evaluate lim ((1 + x)^5 − 1)/x as x → 0.",
        [h4("Given and assumptions"),
         p("0/0 form. This is the power standard limit with n = 5."),
         h4("Formula"), p("((1 + x)<sup>n</sup> − 1)/x → n as x → 0."),
         h4("Step-by-step solution"),
         ol("Expand (1 + x)⁵ = 1 + 5x + 10x² + …",
            "Subtract 1 and divide by x: 5 + 10x + …",
            "Limit = 5"),
         h4("Interpretation and check"),
         p("<b>5.</b> Equivalently (xⁿ − aⁿ)/(x − a) → n a<sup>n−1</sup> at a = 1 gives 5 · 1⁴ = 5 ✓. At "
           "x = 0.001 the value is 5.010.")]),
    num("lm1n23", "Evaluate lim (x^5 − 32)/(x − 2) as x → 2.",
        [h4("Given and assumptions"),
         p("0/0 at x = 2 with a fifth power; use the standard power limit with a = 2."),
         h4("Formula"), p("(x<sup>n</sup> − a<sup>n</sup>)/(x − a) → n a<sup>n−1</sup>."),
         h4("Step-by-step solution"),
         ol("n = 5 and a = 2",
            "n a<sup>n−1</sup> = 5 · 2⁴",
            "5 · 16 = 80"),
         h4("Interpretation and check"),
         p("<b>80.</b> Factorising as (x − 2)(x⁴ + 2x³ + 4x² + 8x + 16) and substituting x = 2 gives "
           "16 + 16 + 16 + 16 + 16 = 80 ✓.")]),
    num("lm1n24", "Evaluate lim (x² + 2x)/(x) as x → 0.",
        [h4("Given and assumptions"),
         p("Substitution gives 0/0, but here the common factor is simply x."),
         h4("Formula"), p("Cancel the common factor x, valid for x ≠ 0."),
         h4("Step-by-step solution"),
         ol("x² + 2x = x(x + 2)",
            "Cancel x: lim (x + 2)",
            "Substitute x = 0: 2"),
         h4("Interpretation and check"),
         p("<b>2.</b> The function equals x + 2 everywhere except at 0, where it is undefined, so the hole sits "
           "at (0, 2) ✓. A table gives −0.01 → 1.99 and 0.01 → 2.01.")]),
]

EQUATIONS = [
    {"title": tr("Limit laws (a, b finite and the limits existing)"),
     "items": [
         {"terms": tr("lim (f ± g) = lim f ± lim g"), "note": tr("Sums and differences split")},
         {"terms": tr("lim (f · g) = lim f · lim g"), "note": tr("Products split")},
         {"terms": tr("lim (f/g) = lim f / lim g, lim g ≠ 0"), "note": tr("Quotients split only when the "
                                                                        "denominator is non-zero")},
         {"terms": tr("lim (k f) = k lim f, lim c = c, lim x = a"), "note": tr("Constants and the identity")},
     ]},
    {"title": tr("Standard limits"),
     "items": [
         {"terms": tr("lim (sin x)/x = 1  (x in radians)"), "note": tr("The key trigonometric limit")},
         {"terms": tr("lim (tan x)/x = 1,  lim (sin ax)/(bx) = a/b"), "note": tr("Companions of the key limit")},
         {"terms": tr("lim (1 − cos x)/x² = 1/2"), "note": tr("Follows from 1 − cos x = 2sin²(x/2)")},
         {"terms": tr("lim (xⁿ − aⁿ)/(x − a) = n aⁿ⁻¹"), "note": tr("Settles every power limit")},
     ]},
    {"title": tr("The number e, exponentials and logarithms"),
     "items": [
         {"terms": tr("lim (1 + 1/x)ˣ = e,  lim (1 + x)^(1/x) = e"), "note": tr("The two definitions of e")},
         {"terms": tr("lim (1 + ax)^(b/x) = e^(ab)"), "note": tr("Product of the two constants")},
         {"terms": tr("lim (eˣ − 1)/x = 1"), "note": tr("Gradient of eˣ at 0")},
         {"terms": tr("lim (aˣ − 1)/x = log a"), "note": tr("Natural log; base e gives 1")},
         {"terms": tr("lim log(1 + x)/x = 1"), "note": tr("Series of log(1 + x)")},
     ]},
]

VIVA = [
    {"title": tr("Meaning of a limit"),
     "items": [
         {"q": tr("What is meant by lim x→a f(x) = L?"),
          "a": tr("f(x) can be made as close to L as we like by taking x close enough to a, without x equalling a.")},
         {"q": tr("Does the limit depend on the value at the point?"),
          "a": tr("No. f(a) may be undefined or different; the limit describes the approach only.")},
         {"q": tr("What is a left-hand limit?"),
          "a": tr("The value approached using x &lt; a, written lim x→a⁻ f(x).")},
         {"q": tr("When does a two-sided limit exist?"),
          "a": tr("Only when both one-sided limits exist and are equal.")},
         {"q": tr("Give one reason a limit may fail to exist."),
          "a": tr("The one-sided limits differ, the values blow up, or the values oscillate.")},
         {"q": tr("Why is 0/0 called indeterminate?"),
          "a": tr("Because it does not fix a value - different functions giving 0/0 can have different limits.")},
     ]},
    {"title": tr("Techniques"),
     "items": [
         {"q": tr("What is the first step in any limit question?"),
          "a": tr("Direct substitution. A finite value is the answer; 0/0 means more algebra is needed.")},
         {"q": tr("How does factorisation help?"),
          "a": tr("It exposes the factor that makes both numerator and denominator zero, which then cancels.")},
         {"q": tr("When do we rationalise?"),
          "a": tr("When a square root causes the 0/0; multiply above and below by the conjugate.")},
         {"q": tr("Which identity is used in rationalising?"),
          "a": tr("(A − B)(A + B) = A² − B².")},
         {"q": tr("How do you handle a limit at infinity for polynomials?"),
          "a": tr("Divide by the highest power in the denominator: smaller degree gives 0, equal degree gives the "
                  "ratio of leading coefficients, larger degree gives ±∞.")},
         {"q": tr("Why is sin x/x = 1 only in radians?"),
          "a": tr("The limit compares an arc with the angle; in degrees the arc-length ratio carries a factor π/180.")},
         {"q": tr("What is the value of (1 − cos x)/x² as x → 0?"),
          "a": tr("1/2, obtained from 1 − cos x = 2sin²(x/2).")},
     ]},
    {"title": tr("e, continuity and exam points"),
     "items": [
         {"q": tr("Define the number e by a limit."),
          "a": tr("e = lim (1 + 1/n)ⁿ as n → ∞ = lim (1 + x)^(1/x) as x → 0, approximately 2.71828.")},
         {"q": tr("What is lim (aˣ − 1)/x as x → 0?"),
          "a": tr("log a with the natural logarithm; the base e gives 1.")},
         {"q": tr("State the three conditions for continuity at a point."),
          "a": tr("f(a) is defined, the limit exists, and the limit equals f(a).")},
         {"q": tr("What is a removable discontinuity?"),
          "a": tr("A hole where the limit exists but f(a) is missing or has the wrong value.")},
         {"q": tr("What is the main error to avoid in a limit answer?"),
          "a": tr("Writing 0/0 as the final answer, or cancelling terms that are added rather than multiplied.")},
     ]},
]

PRACTICE = [
    ("Evaluate lim (x² + 3x − 4)/(x − 1) as x → 1.", 3,
     h4("Working") + ol("Substitute: (1 + 3 − 4)/(1 − 1) = 0/0", "Factorise: (x + 4)(x − 1)",
                        "Cancel (x − 1): lim (x + 4)", "Substitute x = 1: 5")
     + h4("Answer") + p("<b>5.</b> Check with x = 1.01: the expression is 5.01 ✓, so the value closes in on 5 "
                        "from above.")),
    ("Evaluate lim (x³ − 8)/(x² − 4) as x → 2.", 3,
     h4("Working") + ol("0/0 at x = 2",
                        "x³ − 8 = (x − 2)(x² + 2x + 4)",
                        "x² − 4 = (x − 2)(x + 2)",
                        "Cancel (x − 2): (x² + 2x + 4)/(x + 2)",
                        "Substitute x = 2: 12/4 = 3")
     + h4("Answer") + p("<b>3.</b> Note that the cube factor leaves a quadratic while the square leaves a linear "
                        "term, which is why the answer is finite and not zero ✓.")),
    ("Evaluate lim (√(4 + x) − 2)/x as x → 0.", 3,
     h4("Working") + ol("0/0 at x = 0",
                        "Multiply by (√(4 + x) + 2)/(√(4 + x) + 2)",
                        "Numerator becomes (4 + x) − 4 = x",
                        "lim x/[x(√(4 + x) + 2)] = lim 1/(√(4 + x) + 2)",
                        "Substitute x = 0: 1/4")
     + h4("Answer") + p("<b>1/4.</b> This is d(√x)/dx at x = 4, namely 1/(2√4) = 1/4 ✓, which is a useful "
                        "independent check.")),
    ("Evaluate lim (5x³ − 2x + 1)/(2x³ + 7) as x → ∞.", 4,
     h4("Working") + ol("Divide by x³", "(5 − 2/x² + 1/x³)/(2 + 7/x³)",
                        "All the reciprocal terms tend to 0", "Limit = 5/2")
     + h4("Answer") + p("<b>5/2 = 2.5.</b> Equal degrees, so the ratio of leading coefficients decides ✓. At "
                        "x = 1000 the value is 2.4997.")),
    ("Evaluate lim (sin 4x)/(sin 2x) as x → 0.", 3,
     h4("Working") + ol("(sin 4x)/(sin 2x) = (4x/2x) · [(sin 4x)/(4x)] · [(2x)/(sin 2x)]",
                        "Both brackets tend to 1", "Limit = 2")
     + h4("Answer") + p("<b>2.</b> The a/b rule gives 4/2 = 2 ✓. At x = 0.001 the value is 2.0000, since the "
                        "small-angle approximation is already accurate at that scale.")),
    ("Evaluate lim (1 − cos 4x)/x² as x → 0.", 4,
     h4("Working") + ol("1 − cos 4x = 2 sin²(2x)",
                        "(1 − cos 4x)/x² = 2 · [sin(2x)/x]² = 8 · [sin(2x)/(2x)]²",
                        "The bracket tends to 1", "Limit = 8")
     + h4("Answer") + p("<b>8.</b> Scaling (1 − cos u)/u² → 1/2 by u = 4x multiplies by 16 and gives 16/2 = 8 ✓.")),
    ("Evaluate lim (1 + 5x)^(2/x) as x → 0.", 4,
     h4("Working") + ol("Write [(1 + 5x)^(1/(5x))]^(10)", "The bracket tends to e", "Limit = e¹⁰")
     + h4("Answer") + p("<b>e¹⁰ ≈ 22026.</b> The exponent is the product 5 × 2, so a large answer is expected. "
                        "With x = 0.001, (1.005)²⁰⁰⁰ ≈ 21860, just below e¹⁰ ✓.")),
    ("Evaluate lim (2^x − 1)/x as x → 0.", 3,
     h4("Working") + ol("2^x = e^(x log 2)", "Put u = x log 2: the expression is log 2 · (eᵘ − 1)/u",
                        "(eᵘ − 1)/u → 1", "Limit = log 2")
     + h4("Answer") + p("<b>log 2 ≈ 0.6931.</b> The pattern (aˣ − 1)/x → log a fits with a = 2 ✓, and the value "
                        "is below 1 because 2 &lt; e.")),
    ("Evaluate lim ((1 + x)^7 − 1)/x as x → 0.", 3,
     h4("Working") + ol("Expand (1 + x)⁷ = 1 + 7x + 21x² + …", "Subtract 1 and divide by x: 7 + 21x + …",
                        "Limit = 7")
     + h4("Answer") + p("<b>7.</b> The power rule gives n a<sup>n−1</sup> = 7 · 1⁶ = 7 ✓. At x = 0.001 the value "
                        "is 7.021, converging to 7.")),
    ("Evaluate lim (2x² − 7x + 3)/(x − 3) as x → 3.", 4,
     h4("Working") + ol("0/0 at x = 3", "Factorise: 2x² − 7x + 3 = (2x − 1)(x − 3)",
                        "Cancel (x − 3): lim (2x − 1)", "Substitute x = 3: 5")
     + h4("Answer") + p("<b>5.</b> Check by multiplying back: (2x − 1)(x − 3) = 2x² − 7x + 3 ✓. At x = 3.001 the "
                        "value is 5.002.")),
    ("For f(x) = 2x + 1 when x &lt; 2 and f(x) = x² + 1 when x ≥ 2, find lim f(x) as x → 2 and test continuity.",
     4,
     h4("Working") + ol("Left limit: 2(2) + 1 = 5", "Right limit: 2² + 1 = 5", "f(2) = 5",
                        "Both limits equal f(2), so f is continuous at x = 2")
     + h4("Answer") + p("<b>Limit = 5 and the function is continuous there.</b> The two branches join at the point "
                        "(2, 5), so the graph has no hole and no jump ✓.")),
    ("Evaluate lim (√(x² + 5x) − x) as x → ∞.", 4,
     h4("Working") + ol("Multiply by (√(x² + 5x) + x)/(√(x² + 5x) + x)",
                        "Numerator becomes 5x", "Divide above and below by x: 5/(√(1 + 5/x) + 1)",
                        "Limit = 5/2")
     + h4("Answer") + p("<b>5/2 = 2.5.</b> At x = 100 the expression is 2.469, and at 10 000 it is 2.4997 ✓ - a "
                        "finite correction, not a blow-up.")),
    ("Evaluate lim (tan 3x)/(sin 5x) as x → 0.", 4,
     h4("Working") + ol("tan 3x = (sin 3x)/(cos 3x)",
                        "Write (sin 3x)/(sin 5x) · 1/(cos 3x) = (3/5) · brackets that tend to 1",
                        "cos 3x → 1", "Limit = 3/5")
     + h4("Answer") + p("<b>3/5 = 0.6.</b> The ratio of the angles decides when both functions are sines or "
                        "tangents of small angles ✓. At x = 0.001 the value is 0.6000.")),
    ("Evaluate lim (e^(3x) − 1)/x as x → 0.", 3,
     h4("Working") + ol("Put u = 3x, so x = u/3",
                        "(e^(3x) − 1)/x = 3 · (eᵘ − 1)/u", "(eᵘ − 1)/u → 1", "Limit = 3")
     + h4("Answer") + p("<b>3.</b> The standard limit (eᵘ − 1)/u → 1 picks up the inner coefficient, so the answer "
                        "is 3 and not 1 ✓.")),
]

ANSWERED = {"title": tr("6. Answered Practice (Unit 5 level, suggested marks)"),
            "items": [{"h": tr(f"Practice {i}. {q}"), "body": tr(a)} for i, (q, _m, a) in enumerate(PRACTICE, 1)]}
NOTES[-1] = ANSWERED
EXAM = [{"q": tr("Practice: " + q), "marks": m} for q, m, _ in PRACTICE]
LESSON_COUNT = sum(len(s["items"]) for s in NOTES) - len(ANSWERED["items"])
