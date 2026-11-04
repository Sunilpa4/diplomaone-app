"""DI02000021 Engineering Mathematics - Unit 2: Differentiation and its Applications.

GTU 2.1-2.8, 11 h, 23 %, 16 marks, CO2: first principles, sum/product/quotient rules, chain rule,
implicit and parametric functions, logarithmic differentiation, successive differentiation up to the
second order, and the applications (velocity, acceleration, maxima and minima).
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
    ("Khan Academy - derivatives: definition, rules and applications",
     "https://www.khanacademy.org/math/calculus-1"),
    ("OpenStax - Calculus Volume 1, chapters 3 and 4",
     "https://openstax.org/details/books/calculus-volume-1"),
    ("GeoGebra - slide Q towards P and watch the secant become a tangent",
     "https://www.geogebra.org/m/svXqgRbF"),
    ("B. S. Grewal - Elementary Engineering Mathematics (Khanna Publishers)",
     "https://www.khannapublishers.in/"),
]

NOTES = [
    {"title": tr("1. The Derivative from First Principles"),
     "items": [
         card("1.1 What a derivative is",
              h4("Definition")
              + p("The derivative of y = f(x) at a point is the <b>slope of the tangent</b> to the "
                  "curve there. It is obtained as the limit of the slope of a chord when one end of "
                  "the chord slides towards the other:")
              + p("<b>dy/dx = lim (h → 0) [f(x + h) − f(x)] / h</b>")
              + h4("The three-step method")
              + ol("Write f(x + h) and subtract f(x).",
                   "Divide the difference by h and simplify until the h cancels.",
                   "Put h = 0 in the simplified expression.")
              + h4("Worked example")
              + p("For f(x) = x²: [f(x + h) − f(x)]/h = (x² + 2xh + h² − x²)/h = 2x + h, and with "
                  "h = 0 the answer is <b>2x</b>. At x = 1 the slope is 2, which matches the tangent "
                  "in the diagram.")
              + h4("Reading dy/dx")
              + p("dy/dx is a single symbol for the derivative - not a fraction to be cancelled, and "
                  "not dy divided by dx at the end of a question."),
              "d1_tangent", examples=["dd1"], syllabus_item="2.1"),
         card("1.2 First principles for roots and other awkward functions",
              h4("The rationalising trick")
              + p("When f(x) contains a square root, multiply the numerator and denominator by the "
                  "conjugate first; the root disappears from the top and h cancels.")
              + h4("Worked example")
              + p("For f(x) = √x: [√(x + h) − √x]/h, multiplied by [√(x + h) + √x]/[√(x + h) + √x], "
                  "becomes h / {h[√(x + h) + √x]} = 1/[√(x + h) + √x]. With h = 0 this gives "
                  "<b>1/(2√x)</b>.")
              + h4("When to use first principles")
              + ul("The syllabus asks for it directly, usually for x², x³, √x or 1/x.",
                   "It proves a standard result once; afterwards you may quote the table.",
                   "It is never the fastest route for a complicated function - use the rules.")
              + h4("Common mistake")
              + p("Putting h = 0 too early. If h = 0 is substituted before the h in the denominator "
                  "is cancelled, every question becomes 0/0 and no answer appears."),
              examples=["dd2"], syllabus_item="2.1"),
         card("1.3 The standard derivatives you must know",
              h4("Table (learn these)")
              + table(["y", "dy/dx"],
                      [("xⁿ", "n xⁿ⁻¹"),
                       ("constant k", "0"),
                       ("eˣ", "eˣ"),
                       ("aˣ", "aˣ log a"),
                       ("log x", "1/x"),
                       ("sin x", "cos x"),
                       ("cos x", "−sin x"),
                       ("tan x", "sec²x")])
              + h4("Using the table")
              + p("For y = 3x² − 5x + 2 each term is differentiated separately: 6x − 5 + 0. At x = 2 "
                  "the slope is 12 − 5 = <b>7</b>.")
              + h4("Common mistake")
              + p("Differentiating a constant to 1. The derivative of 2 is 0; only x (that is x¹) "
                  "gives 1."),
              examples=["dd3", "dd4"], syllabus_item="2.2"),
         card("1.4 Notation, and when a derivative does not exist",
              h4("Four ways to write the same thing")
              + ul("f′(x)", "dy/dx", "y′", "D(f(x))")
              + h4("A derivative can fail to exist")
              + p("At a sharp corner or a vertical tangent the two one-sided slopes disagree, so the "
                  "limit of the chord slope has no single value. The function is then not "
                  "differentiable at that point, even though it may be continuous there.")
              + h4("What the sign tells you")
              + table(["dy/dx", "The curve is"],
                      [("positive", "rising as x increases"),
                       ("negative", "falling as x increases"),
                       ("zero", "flat - a stationary point (Unit 2.8)")])
              + sc("Is every continuous function differentiable?",
                   "No. Continuity is necessary but not sufficient: a corner such as y = |x| at x = 0 "
                   "is continuous yet has no derivative there."),
              syllabus_item="2.1"),
     ]},

    {"title": tr("2. Working Rules: Sum, Product and Division"),
     "items": [
         card("2.1 Sum and difference",
              h4("Rule")
              + p("<b>(u ± v)′ = u′ ± v′</b> - differentiate term by term, keeping the signs.")
              + h4("Worked example")
              + p("y = x³ + 2x² − 7x + 1 gives dy/dx = 3x² + 4x − 7. The constant 1 disappears.")
              + h4("With other functions")
              + p("y = sin x + cos x gives cos x − sin x; y = 3eˣ − 2 log x gives 3eˣ − 2/x.")
              + h4("Common mistake")
              + p("Applying the product rule to a sum. The product rule is for u <i>times</i> v, not "
                  "u plus v."),
              "d2_rules", examples=["dd4"], syllabus_item="2.2"),
         card("2.2 The product rule",
              h4("Rule")
              + p("<b>(uv)′ = u′v + uv′</b> - differentiate the first and keep the second, then keep "
                  "the first and differentiate the second, and add.")
              + h4("Worked example")
              + p("y = x²(3x + 5): u = x², v = 3x + 5, so dy/dx = 2x(3x + 5) + x²(3) = 6x² + 10x + 3x² "
                  "= <b>9x² + 10x</b>.")
              + h4("Second example")
              + p("y = (x + 1)(x² + 3) gives 1·(x² + 3) + (x + 1)(2x) = 3x² + 2x + 3.")
              + h4("Common mistake")
              + p("Writing (uv)′ = u′v′. For the example above that would give 2x·3 = 6x instead of "
                  "9x² + 10x.")
              + sc("Can you expand first instead?",
                   "Yes, when the bracket is easy: x²(3x + 5) = 3x³ + 5x² differentiates to 9x² + 10x "
                   "as well. Use whichever is quicker, but the product rule is compulsory when the "
                   "factors are trig, log or exponential."),
              examples=["dd5", "dd6"], syllabus_item="2.2"),
         card("2.3 The quotient rule",
              h4("Rule")
              + p("<b>(u/v)′ = (u′v − uv′) / v²</b> - note the minus sign and the order: the "
                  "derivative of the top comes first.")
              + h4("Worked example")
              + p("y = (2x + 1)/(x − 1): u = 2x + 1, v = x − 1, u′ = 2, v′ = 1. Then dy/dx = "
                  "[2(x − 1) − (2x + 1)(1)]/(x − 1)² = (2x − 2 − 2x − 1)/(x − 1)² = "
                  "<b>−3/(x − 1)²</b>.")
              + h4("Second example")
              + p("y = x/(x² + 1) gives [(1)(x² + 1) − x(2x)]/(x² + 1)² = <b>(1 − x²)/(x² + 1)²</b>.")
              + h4("Common mistake")
              + p("Swapping u and v, which flips the sign of the whole answer. Write u above v before "
                  "you start, and keep the v² denominator until the last line."),
              examples=["dd7", "dd8"], syllabus_item="2.2"),
         card("2.4 Choosing the rule before you differentiate",
              h4("A five-second check")
              + table(["The expression is", "Use"],
                      [("a sum of terms", "term by term"),
                       ("a product of two functions", "product rule"),
                       ("one function over another", "quotient rule"),
                       ("a function of a bracket, root or power", "chain rule (next section)"),
                       ("x both in the base and in the power", "logarithmic differentiation")])
              + h4("Order of work")
              + ol("Name u and v (or u inside the bracket) on paper.",
                   "Write the rule with u′ and v′ in place before substituting anything.",
                   "Simplify only at the end, and cancel common factors.")
              + h4("Why the naming helps")
              + p("Most lost marks in this unit are not wrong rules but wrong substitutions: u and v "
                  "swapped, a missing minus, or a factor dropped in the middle line."),
              syllabus_item="2.2"),
     ]},

    {"title": tr("3. The Chain Rule"),
     "items": [
         card("3.1 A function of a function",
              h4("Rule")
              + p("<b>dy/dx = dy/du × du/dx</b> - differentiate the outside, then multiply by the "
                  "derivative of the inside.")
              + h4("Worked example")
              + p("y = (3x + 2)⁵ with u = 3x + 2: dy/du = 5u⁴ and du/dx = 3, so dy/dx = "
                  "5u⁴ × 3 = <b>15(3x + 2)⁴</b>.")
              + h4("The quick version")
              + p("For y = [f(x)]ⁿ, dy/dx = n[f(x)]ⁿ⁻¹ × f′(x). For y = (2x − 1)⁷ that gives "
                  "7(2x − 1)⁶ × 2 = 14(2x − 1)⁶.")
              + h4("Common mistake")
              + p("Forgetting the inside derivative. (3x + 2)⁵ differentiates to 5(3x + 2)⁴ only if "
                  "the inside were x; with 3x + 2 the factor 3 is compulsory."),
              "d3_chain", examples=["dd9"], syllabus_item="2.3"),
         card("3.2 Chain rule with trigonometric and exponential functions",
              h4("Patterns")
              + ul("y = sin(5x) → 5 cos(5x)",
                   "y = cos(3x) → −3 sin(3x)",
                   "y = e^(3x) → 3e^(3x)",
                   "y = e^(x²) → 2x e^(x²)")
              + h4("Worked examples")
              + p("y = sin 5x: the outside is sin and the inside is 5x, so dy/dx = cos(5x) × 5 = "
                  "<b>5 cos 5x</b>.")
              + p("y = e^(3x): the derivative of e^u is e^u, so dy/dx = e^(3x) × 3 = <b>3e^(3x)</b>.")
              + h4("Common mistake")
              + p("Writing 5 cos x (inside untouched) or cos 5x (factor lost). Both parts must appear: "
                  "the outer derivative evaluated at the inside, times the inside derivative."),
              examples=["dd10", "dd11"], syllabus_item="2.3"),
         card("3.3 Chain rule with roots and logarithms",
              h4("Roots are powers")
              + p("Write √(x² + 1) as (x² + 1)^(1/2); then dy/dx = (1/2)(x² + 1)^(−1/2) × 2x = "
                  "<b>x/√(x² + 1)</b>.")
              + h4("Logarithms")
              + p("For y = log[f(x)], dy/dx = f′(x)/f(x). So y = log(sin x) gives cos x / sin x = "
                  "<b>cot x</b>.")
              + h4("Deeper nesting")
              + p("With three layers, multiply three factors. y = sin²(3x) is [sin 3x]², so "
                  "dy/dx = 2 sin 3x × cos 3x × 3 = 6 sin 3x cos 3x.")
              + h4("Common mistake")
              + p("Cancelling the root too early. Keep the fractional power until the last line, then "
                  "convert back to a root form if the answer looks tidier."),
              examples=["dd12", "dd13"], syllabus_item="2.3"),
         card("3.4 A checklist for any chain-rule question",
              h4("Four questions, in order")
              + ol("What is the outermost operation? (power, sin, log, e)",
                   "What is the whole inside expression? Call it u.",
                   "What is du/dx?",
                   "Multiply and then put u back in terms of x.")
              + h4("Speed check")
              + p("y = (5x − 1)⁴ → 20(5x − 1)³; y = √(3x + 4) → 3/(2√(3x + 4)); "
                  "y = log(2x + 5) → 2/(2x + 5).")
              + h4("Where it is used later")
              + p("Every implicit, parametric and logarithmic derivative in this unit ends with a "
                  "chain rule. Get this section solid and the next four become bookkeeping."),
              syllabus_item="2.3"),
     ]},

    {"title": tr("4. Derivatives of Implicit Functions"),
     "items": [
         card("4.1 When y is not given as a formula",
              h4("Definition")
              + p("An <b>implicit</b> function is one where x and y are mixed in a single equation, "
                  "such as x² + y² = 25. y is still a function of x, but it is not isolated.")
              + h4("Method")
              + ol("Differentiate every term with respect to x.",
                   "Every time you differentiate a y-term, multiply by dy/dx (chain rule).",
                   "Collect the dy/dx terms on one side and factorise.",
                   "Divide to finish.")
              + h4("Worked example")
              + p("x² + y² = 25 gives 2x + 2y(dy/dx) = 0, so dy/dx = <b>−x/y</b>. At the point "
                  "(3, 4) the slope is −3/4.")
              + h4("Why the minus appears")
              + p("The dy/dx term arrives with a plus sign; moving it to the other side makes the "
                  "answer negative - the standard shape for a circle."),
              examples=["dd14"], syllabus_item="2.4"),
         card("4.2 Products and squares inside an implicit equation",
              h4("Worked example")
              + p("x² + xy + y² = 7. The middle term is a product, so it takes the product rule: "
                  "1·y + x·(dy/dx).")
              + p("Differentiating: 2x + y + x(dy/dx) + 2y(dy/dx) = 0.")
              + p("Factorising: (x + 2y)(dy/dx) = −(2x + y), so dy/dx = <b>−(2x + y)/(x + 2y)</b>.")
              + h4("A useful check")
              + p("The formula is symmetric in x and y except for the swap, which is what you expect "
                  "from a symmetric equation. Symmetry checks catch sign errors.")
              + h4("Common mistake")
              + p("Writing the derivative of y² as 2y. It is 2y(dy/dx) - the chain rule never "
                  "switches off for a y-term."),
              examples=["dd15"], syllabus_item="2.4"),
         card("4.3 Using an implicit derivative",
              h4("Slope and tangent at a point")
              + p("Differentiate, then substitute the coordinates. For x² + y² = 25 at (3, 4) the "
                  "slope is −3/4, so the tangent is y − 4 = (−3/4)(x − 3), that is 3x + 4y = 25.")
              + h4("Vertical tangents")
              + p("Where the denominator of dy/dx becomes zero the slope is infinite: the tangent is "
                  "vertical. On 2y = 0, that is at (5, 0) and (−5, 0) for the circle.")
              + h4("Why implicit differentiation is needed")
              + p("Many engineering curves - a circle, an ellipse, a level curve of a graph - are "
                  "given in implicit form. Isolating y would need two branches, and the slope formula "
                  "would need a case split."),
              syllabus_item="2.4"),
     ]},

    {"title": tr("5. Derivatives of Parametric Functions"),
     "items": [
         card("5.1 x and y given separately in terms of t",
              h4("Rule")
              + p("When x = f(t) and y = g(t), <b>dy/dx = (dy/dt) ÷ (dx/dt)</b>.")
              + h4("Worked example")
              + p("x = at², y = 2at: dx/dt = 2at and dy/dt = 2a, so dy/dx = 2a/(2at) = <b>1/t</b>.")
              + h4("Why it works")
              + p("Both x and y depend on t, so the slope is the rate of y per unit of t divided by "
                  "the rate of x per unit of t. The chain rule in the form dy/dx = (dy/dt)/(dx/dt) "
                  "says exactly that.")
              + h4("Common mistake")
              + p("Inverting the ratio. dy/dx is dy/dt over dx/dt, not the other way round; the wrong "
                  "way gives 2at/2a = t instead of 1/t."),
              examples=["dd16"], syllabus_item="2.5"),
         card("5.2 Parametric circles and ellipses",
              h4("Worked example")
              + p("x = a cos θ, y = a sin θ (a circle of radius a): dx/dθ = −a sin θ and "
                  "dy/dθ = a cos θ, so dy/dx = a cos θ / (−a sin θ) = <b>−cot θ</b>.")
              + h4("Checking against the implicit form")
              + p("The same circle is x² + y² = a², whose implicit slope is −x/y = −a cos θ / a sin θ "
                  "= −cot θ. Both methods agree - a good self-check in an exam.")
              + h4("Ellipse")
              + p("For x = a cos θ, y = b sin θ the slope is −(b/a) cot θ, so the ellipse is flatter "
                  "than the circle in the y-direction.")
              + h4("Common mistake")
              + p("Differentiating sin θ to −cos θ. The derivative of sin is +cos; only cos gives "
                  "−sin."),
              examples=["dd17"], syllabus_item="2.5"),
         card("5.3 Slopes, tangents and the value of the parameter",
              h4("Finding the point first")
              + p("A parametric question usually gives the value of t or θ. Substitute that value into "
                  "x and y to get the point, and into dy/dx to get the slope.")
              + h4("Example")
              + p("x = t², y = 2t at t = 3: the point is (9, 6) and dy/dx = 1/t = 1/3, so the tangent "
                  "is 3y = x − 9 + 18, that is x − 3y + 9 = 0.")
              + h4("What the parameter means")
              + p("In kinematics t is time, so the parametric curve is the path of a particle and "
                  "dy/dx is the direction of motion. In geometry t or θ is simply a label that runs "
                  "along the curve.")
              + sc("Do you need d²y/dx² here?",
                   "The syllabus asks only for dy/dx of parametric curves. If asked, differentiate "
                   "dy/dx with respect to t and divide by dx/dt."),
              syllabus_item="2.5"),
     ]},

    {"title": tr("6. Logarithmic Differentiation"),
     "items": [
         card("6.1 When the power contains x",
              h4("The problem")
              + p("xˣ is neither xⁿ (power fixed) nor aˣ (base fixed), so neither the power rule nor "
                  "the exponential rule applies. Take logarithms first and the product rule does the "
                  "work.")
              + h4("Method")
              + ol("Take log of both sides: log y = x log x.",
                   "Differentiate both sides: (1/y)(dy/dx) = 1·log x + x·(1/x).",
                   "Simplify the right side: 1 + log x.",
                   "Multiply by y: dy/dx = xˣ(1 + log x).")
              + h4("Why it is allowed")
              + p("Both sides are positive for x > 0, so the logarithm is defined, and the chain rule "
                  "gives the (1/y)(dy/dx) factor on the left."),
              "d4_logdiff", examples=["dd18"], syllabus_item="2.6"),
         card("6.2 Products, quotients and powers together",
              h4("The trick in general")
              + p("For y = (1 + x)ˣ: log y = x log(1 + x), so (1/y)(dy/dx) = log(1 + x) + x/(1 + x), "
                  "giving dy/dx = <b>(1 + x)ˣ[log(1 + x) + x/(1 + x)]</b>.")
              + h4("Also useful for long products and quotients")
              + p("For y = x²(x + 1)³/(x − 2)⁴ the product and quotient rules give a very long "
                  "expression. Taking logs turns it into a sum of three simple derivatives:")
              + p("(1/y)(dy/dx) = 2/x + 3/(x + 1) − 4/(x − 2), then multiply by y.")
              + h4("Common mistake")
              + p("Writing log(xˣ) = x log x and then forgetting to finish - the answer must be "
                  "multiplied by y, not left as 1 + log x."),
              examples=["dd19"], syllabus_item="2.6"),
         card("6.3 Deciding to take the logarithm",
              h4("Take logs when")
              + ul("the variable appears in the exponent (xˣ, (sin x)ˣ, x^(1/x));",
                   "the expression is a long product or quotient that would need several rule "
                   "applications;",
                   "an engineering formula is given as a product of powers, such as y = A x^n e^(−kx).")
              + h4("Do not take logs when")
              + p("The base is a constant: aˣ differentiates straight to aˣ log a, and eˣ to eˣ. "
                  "Logarithms there add work and a stray factor.")
              + h4("Worked mini-example")
              + p("y = x^(1/x): log y = (1/x) log x = log x / x, so (1/y)(dy/dx) = "
                  "(1 − log x)/x², giving dy/dx = x^(1/x)(1 − log x)/x².")
              + p("The maximum of x^(1/x) is at x = e, which is exactly where that derivative "
                  "vanishes - a neat link to the next section."),
              syllabus_item="2.6"),
     ]},

    {"title": tr("7. Successive Differentiation and Applications"),
     "items": [
         card("7.1 The second derivative",
              h4("Definition")
              + p("Differentiating dy/dx gives the <b>second derivative</b> d²y/dx², written y″ or "
                  "f″(x). The syllabus asks for the second order; higher orders follow the same idea.")
              + h4("Worked examples")
              + p("y = x⁴: y′ = 4x³ and y″ = <b>12x²</b>.")
              + p("y = sin 3x: y′ = 3 cos 3x and y″ = −9 sin 3x - each differentiation multiplies by "
                  "3 and shifts the function.")
              + h4("What the second derivative means")
              + table(["y″", "The graph is"],
                      [("positive", "curving upwards (concave up)"),
                       ("negative", "curving downwards (concave down)"),
                       ("zero", "possibly a point of inflexion - check the sign change")])
              + h4("Notation trap")
              + p("d²y/dx² is not (dy/dx)². The first is a second derivative; the second is the "
                  "square of the first."),
              examples=["dd20", "dd21"], syllabus_item="2.7"),
         card("7.2 Velocity and acceleration",
              h4("Kinematics from calculus")
              + p("If s(t) is the position, then <b>v = ds/dt</b> and <b>a = dv/dt = d²s/dt²</b>.")
              + h4("Worked example")
              + p("s = t³ − 6t² + 8t − 4 gives v = 3t² − 12t + 8 and a = 6t − 12. At t = 3: "
                  "v = 27 − 36 + 8 = <b>−1</b> and a = 18 − 12 = <b>6</b>.")
              + h4("Reading the signs")
              + ul("v > 0: moving in the positive direction; v &lt; 0: moving backwards.",
                   "v = 0: momentarily at rest - a turning point of the motion.",
                   "a > 0 with v > 0: speeding up; a &lt; 0 with v > 0: slowing down.")
              + h4("Units")
              + p("If s is in metres and t in seconds, v is m/s and a is m/s². Keep the units in the "
                  "final line; examiners give a mark for them."),
              "d5_sva", examples=["dd22"], syllabus_item="2.8"),
         card("7.3 Maxima and minima: the method",
              h4("Steps")
              + ol("Find f′(x).",
                   "Solve f′(x) = 0 for the stationary points.",
                   "Find f″(x) and evaluate it at each stationary point.",
                   "f″ &lt; 0 gives a maximum, f″ > 0 gives a minimum, f″ = 0 needs the first-derivative "
                   "sign test.",
                   "Substitute back into f(x) for the maximum or minimum value.")
              + h4("Worked example")
              + p("f(x) = x³ − 3x + 2: f′ = 3x² − 3 = 0 gives x = 1 and x = −1; f″ = 6x, so f″(−1) = −6 "
                  "(maximum, value 4) and f″(1) = 6 (minimum, value 0).")
              + h4("Common mistake")
              + p("Answering with the x-value only. A maximum/minimum question normally asks for both "
                  "the point and the value of the function there."),
              "d6_maxmin", examples=["dd23"], syllabus_item="2.8"),
         card("7.4 A second maxima and minima example",
              h4("Worked example")
              + p("f(x) = 2x³ − 9x² + 12x: f′ = 6x² − 18x + 12 = 6(x − 1)(x − 2), so the stationary "
                  "points are x = 1 and x = 2.")
              + p("f″ = 12x − 18 gives f″(1) = −6 (maximum, value 5) and f″(2) = 6 (minimum, value 4).")
              + h4("Word problems")
              + p("For a rectangle of perimeter 20 cm, let the length be x; then the width is 10 − x "
                  "and the area A = x(10 − x) = 10x − x². A′ = 10 − 2x = 0 gives x = 5, and A″ = −2 &lt; 0 "
                  "confirms a maximum of 25 cm² - a square.")
              + h4("Reading the answer back")
              + p("Always say what the numbers mean in the words of the question (cm, cm², seconds, "
                  "rupees). The calculus gives the turning point; the sentence gives the mark."),
              examples=["dd24"], syllabus_item="2.8"),
         card("7.5 Exam routine for a differentiation question",
              h4("Six lines that earn marks")
              + ol("Write the function and name the rule you will use.",
                   "Show u, v (or u inside) explicitly.",
                   "Write the rule with u′, v′ before substituting.",
                   "Simplify once, carefully.",
                   "For applications, state f′(x) = 0 and solve.",
                   "Finish with the second derivative, the sign test and a sentence.")
              + h4("Time saving")
              + p("Standard derivatives (sin, cos, eˣ, log, xⁿ) should be quoted, not re-derived. "
                  "First principles is only used when the question says so.")
              + h4("Accuracy habits")
              + p("Keep brackets around negative terms until the last line, and never cancel across a "
                  "plus sign. Most marks lost in this unit are sign and bracket slips, not method."),
              syllabus_item="2.8"),
     ]},

    {"title": tr("8. Practice Questions with Model Answers"),
     "items": []},  # filled by the builder from EXAM
]

NUMERICALS = [
    {"id": "dd1", "q": tr("Differentiate f(x) = x² from first principles."),
     "a": tr(p("Step 1: f(x + h) − f(x) = (x + h)² − x² = 2xh + h².")
     + p("Step 2: divide by h → 2x + h.")
     + p("Step 3: let h → 0, so f′(x) = <b>2x</b>.")
     + p("At x = 1 the slope is 2 and at x = 3 it is 6 - the tangent gets steeper as x grows."))},
    {"id": "dd2", "q": tr("Differentiate f(x) = √x from first principles."),
     "a": tr(p("Write [√(x + h) − √x]/h and multiply top and bottom by the conjugate "
               "√(x + h) + √x.")
     + p("The numerator becomes (x + h) − x = h, so the expression is h / {h[√(x + h) + √x]} = "
         "1/[√(x + h) + √x].")
     + p("Let h → 0: f′(x) = 1/(√x + √x) = <b>1/(2√x)</b>."))},
    {"id": "dd3", "q": tr("Differentiate y = 3x² − 5x + 2 and find the slope at x = 2."),
     "a": tr(p("Term by term: d(3x²)/dx = 6x, d(−5x)/dx = −5, d(2)/dx = 0.")
     + p("So dy/dx = <b>6x − 5</b>.")
     + p("At x = 2 the slope is 12 − 5 = <b>7</b>."))},
    {"id": "dd4", "q": tr("Differentiate y = x³ + 2x² − 7x + 1."),
     "a": tr(p("Each term is a power of x, so differentiate term by term.")
     + p("3x² + 4x − 7 + 0, that is dy/dx = <b>3x² + 4x − 7</b>.")
     + p("The constant 1 differentiates to 0, and −7x differentiates to −7."))},
    {"id": "dd5", "q": tr("Differentiate y = x²(3x + 5) using the product rule."),
     "a": tr(p("Take u = x² and v = 3x + 5, so u′ = 2x and v′ = 3.")
     + p("(uv)′ = u′v + uv′ = 2x(3x + 5) + x²(3) = 6x² + 10x + 3x².")
     + p("So dy/dx = <b>9x² + 10x</b>.")
     + p("Check by expanding first: y = 3x³ + 5x², whose derivative is the same."))},
    {"id": "dd6", "q": tr("Differentiate y = (x + 1)(x² + 3)."),
     "a": tr(p("u = x + 1, v = x² + 3, so u′ = 1 and v′ = 2x.")
     + p("(uv)′ = 1(x² + 3) + (x + 1)(2x) = x² + 3 + 2x² + 2x.")
     + p("So dy/dx = <b>3x² + 2x + 3</b>."))},
    {"id": "dd7", "q": tr("Differentiate y = (2x + 1)/(x − 1) using the quotient rule."),
     "a": tr(p("u = 2x + 1, v = x − 1, so u′ = 2 and v′ = 1.")
     + p("(u/v)′ = [2(x − 1) − (2x + 1)(1)]/(x − 1)² = (2x − 2 − 2x − 1)/(x − 1)².")
     + p("So dy/dx = <b>−3/(x − 1)²</b>, which is negative for every x ≠ 1."))},
    {"id": "dd8", "q": tr("Differentiate y = x/(x² + 1)."),
     "a": tr(p("u = x, v = x² + 1, so u′ = 1 and v′ = 2x.")
     + p("(u/v)′ = [1(x² + 1) − x(2x)]/(x² + 1)² = (x² + 1 − 2x²)/(x² + 1)².")
     + p("So dy/dx = <b>(1 − x²)/(x² + 1)²</b>.")
     + p("The slope is zero at x = 1, which is where this curve has its maximum."))},
    {"id": "dd9", "q": tr("Differentiate y = (3x + 2)⁵."),
     "a": tr(p("This is a function of a function: the outside is a fifth power and the inside is "
               "3x + 2.")
     + p("Take u = 3x + 2: dy/du = 5u⁴ and du/dx = 3.")
     + p("dy/dx = 5u⁴ × 3 = <b>15(3x + 2)⁴</b>.")
     + p("The factor 3 is compulsory - without it the answer would only be right for (x + 2)⁵."))},
    {"id": "dd10", "q": tr("Differentiate y = sin 5x."),
     "a": tr(p("The outside is sin and the inside is 5x, whose derivative is 5.")
     + p("dy/dx = cos(5x) × 5 = <b>5 cos 5x</b>.")
     + p("At x = 0 the slope is 5, which is why the graph of sin 5x rises five times as fast as "
         "sin x."))},
    {"id": "dd11", "q": tr("Differentiate y = e^(3x)."),
     "a": tr(p("The derivative of e^u is e^u, so the only extra work is the inside derivative.")
     + p("dy/dx = e^(3x) × 3 = <b>3e^(3x)</b>.")
     + p("Similarly y = e^(−2x) gives −2e^(−2x): a negative inside derivative makes the function "
         "decrease."))},
    {"id": "dd12", "q": tr("Differentiate y = √(x² + 1)."),
     "a": tr(p("Write the root as a power: y = (x² + 1)^(1/2).")
     + p("dy/dx = (1/2)(x² + 1)^(−1/2) × 2x = x(x² + 1)^(−1/2).")
     + p("So dy/dx = <b>x/√(x² + 1)</b>.")
     + p("At x = 0 the slope is 0, which matches the flat bottom of the curve there."))},
    {"id": "dd13", "q": tr("Differentiate y = log(sin x)."),
     "a": tr(p("For y = log[f(x)] the derivative is f′(x)/f(x).")
     + p("Here f(x) = sin x and f′(x) = cos x, so dy/dx = cos x/sin x.")
     + p("That is dy/dx = <b>cot x</b>."))},
    {"id": "dd14", "q": tr("Find dy/dx for x² + y² = 25 and hence the slope at (3, 4)."),
     "a": tr(p("Differentiate every term with respect to x, remembering that y is a function of x: "
               "2x + 2y(dy/dx) = 0.")
     + p("So dy/dx = <b>−x/y</b>.")
     + p("At (3, 4): dy/dx = −3/4. The tangent there is y − 4 = (−3/4)(x − 3), that is 3x + 4y = 25."))},
    {"id": "dd15", "q": tr("Find dy/dx for x² + xy + y² = 7."),
     "a": tr(p("The middle term is a product, so use the product rule on xy: derivative = "
               "y + x(dy/dx).")
     + p("Differentiating the whole equation: 2x + y + x(dy/dx) + 2y(dy/dx) = 0.")
     + p("Factorise: (x + 2y)(dy/dx) = −(2x + y), so dy/dx = <b>−(2x + y)/(x + 2y)</b>."))},
    {"id": "dd16", "q": tr("Find dy/dx for the parametric curve x = at², y = 2at."),
     "a": tr(p("Differentiate each with respect to t: dx/dt = 2at and dy/dt = 2a.")
     + p("dy/dx = (dy/dt)/(dx/dt) = 2a/(2at) = <b>1/t</b>.")
     + p("At t = 2 the slope is 1/2, and the point is (4a, 4a)."))},
    {"id": "dd17", "q": tr("Find dy/dx for x = a cos θ, y = a sin θ."),
     "a": tr(p("dx/dθ = −a sin θ and dy/dθ = a cos θ.")
     + p("dy/dx = a cos θ /(−a sin θ) = <b>−cot θ</b>.")
     + p("This matches the implicit answer for x² + y² = a², where dy/dx = −x/y = −cot θ."))},
    {"id": "dd18", "q": tr("Differentiate y = xˣ."),
     "a": tr(p("The variable is in both the base and the power, so take logarithms: "
               "log y = x log x.")
     + p("Differentiate both sides: (1/y)(dy/dx) = 1·log x + x·(1/x) = 1 + log x.")
     + p("Multiply by y: dy/dx = <b>xˣ(1 + log x)</b>.")
     + p("Note that 1 + log x = 0 at x = 1/e, the minimum of the curve for x > 0."))},
    {"id": "dd19", "q": tr("Differentiate y = (1 + x)ˣ."),
     "a": tr(p("Take logs: log y = x log(1 + x).")
     + p("Differentiate: (1/y)(dy/dx) = log(1 + x) + x/(1 + x).")
     + p("So dy/dx = <b>(1 + x)ˣ[log(1 + x) + x/(1 + x)]</b>.")
     + p("At x = 0 this gives 1·(0 + 0) = 0, and indeed the curve of (1 + x)ˣ is flat at x = 0."))},
    {"id": "dd20", "q": tr("Find the second derivative of y = x⁴."),
     "a": tr(p("First derivative: y′ = 4x³.")
     + p("Differentiate again: y″ = <b>12x²</b>.")
     + p("Since y″ ≥ 0 everywhere, the curve y = x⁴ is concave up on both sides of the origin."))},
    {"id": "dd21", "q": tr("Find the second derivative of y = sin 3x."),
     "a": tr(p("First derivative: y′ = 3 cos 3x (chain rule brings the factor 3).")
     + p("Differentiate again: y″ = 3 × (−3 sin 3x) = <b>−9 sin 3x</b>.")
     + p("Each differentiation multiplies by 3, and the function moves sin → cos → −sin."))},
    {"id": "dd22", "q": tr("A particle moves with s = t³ − 6t² + 8t − 4 (s in metres, t in seconds). "
                           "Find the velocity and acceleration at t = 3 s."),
     "a": tr(p("v = ds/dt = 3t² − 12t + 8 and a = dv/dt = 6t − 12.")
     + p("At t = 3: v = 27 − 36 + 8 = <b>−1 m/s</b> and a = 18 − 12 = <b>6 m/s²</b>.")
     + p("The negative velocity means the particle is moving backwards at that instant, while the "
         "positive acceleration means the velocity is increasing - it is slowing down."))},
    {"id": "dd23", "q": tr("Find the stationary points of f(x) = x³ − 3x + 2 and classify them."),
     "a": tr(p("f′(x) = 3x² − 3 = 3(x² − 1), so f′(x) = 0 at x = 1 and x = −1.")
     + p("f″(x) = 6x, so f″(−1) = −6 &lt; 0 → <b>maximum at x = −1</b>, and f″(1) = 6 > 0 → "
         "<b>minimum at x = 1</b>.")
     + p("The values are f(−1) = −1 + 3 + 2 = 4 and f(1) = 1 − 3 + 2 = 0."))},
    {"id": "dd24", "q": tr("Find and classify the stationary points of f(x) = 2x³ − 9x² + 12x."),
     "a": tr(p("f′(x) = 6x² − 18x + 12 = 6(x − 1)(x − 2), so f′(x) = 0 at x = 1 and x = 2.")
     + p("f″(x) = 12x − 18: f″(1) = −6 &lt; 0 → <b>maximum, value f(1) = 5</b>; f″(2) = 6 > 0 → "
         "<b>minimum, value f(2) = 4</b>.")
     + p("The curve rises to 5, dips to 4 and then climbs again."))},
]

EQUATIONS = [
    {"title": tr("Definition and standard derivatives"),
     "items": [
         {"terms": tr("Derivative from first principles"), "a": tr("f′(x) = lim (h→0) [f(x+h) − f(x)]/h")},
         {"terms": tr("Power rule"), "a": tr("d(xⁿ)/dx = n xⁿ⁻¹ ;  d(constant)/dx = 0")},
         {"terms": tr("Exponential"), "a": tr("d(eˣ)/dx = eˣ ;  d(aˣ)/dx = aˣ log a")},
         {"terms": tr("Logarithm"), "a": tr("d(log x)/dx = 1/x")},
         {"terms": tr("Sine and cosine"), "a": tr("d(sin x)/dx = cos x ;  d(cos x)/dx = −sin x")},
         {"terms": tr("Tangent"), "a": tr("d(tan x)/dx = sec²x")},
     ]},
    {"title": tr("Working rules"),
     "items": [
         {"terms": tr("Sum and difference"), "a": tr("(u ± v)′ = u′ ± v′")},
         {"terms": tr("Product"), "a": tr("(uv)′ = u′v + uv′")},
         {"terms": tr("Quotient"), "a": tr("(u/v)′ = (u′v − uv′)/v²")},
         {"terms": tr("Chain rule"), "a": tr("dy/dx = dy/du × du/dx")},
         {"terms": tr("Power of a function"), "a": tr("d[f(x)]ⁿ/dx = n[f(x)]ⁿ⁻¹ f′(x)")},
         {"terms": tr("Logarithm of a function"), "a": tr("d log[f(x)]/dx = f′(x)/f(x)")},
     ]},
    {"title": tr("Implicit, parametric and applications"),
     "items": [
         {"terms": tr("Implicit differentiation"), "a": tr("differentiate every term by x; each y-term gains a dy/dx factor")},
         {"terms": tr("Parametric slope"), "a": tr("dy/dx = (dy/dt)/(dx/dt)")},
         {"terms": tr("Logarithmic differentiation"), "a": tr("log y = log f(x); then (1/y)dy/dx = d[log f]/dx")},
         {"terms": tr("Second derivative"), "a": tr("y″ = d²y/dx² = d(dy/dx)/dx")},
         {"terms": tr("Velocity and acceleration"), "a": tr("v = ds/dt ;  a = dv/dt = d²s/dt²")},
         {"terms": tr("Stationary points"), "a": tr("f′(x) = 0 ;  f″ &lt; 0 maximum, f″ > 0 minimum")},
     ]},
]

VIVA = [
    {"title": tr("Meaning of the derivative"),
     "items": [
         {"q": tr("What does dy/dx mean geometrically?"),
          "a": tr("The slope of the tangent to the curve at that point - the rate at which y changes "
                  "with x.")},
         {"q": tr("Define the derivative in words."),
          "a": tr("The limit of [f(x + h) − f(x)]/h as h tends to zero.")},
         {"q": tr("Why can h not be put equal to zero at the start?"),
          "a": tr("Because the expression would become 0/0. The h in the denominator must be "
                  "cancelled first, and only then is h taken to zero.")},
         {"q": tr("What is the derivative of a constant, and why?"),
          "a": tr("Zero: a horizontal line has no change, so its slope is 0.")},
         {"q": tr("Can a continuous function fail to have a derivative?"),
          "a": tr("Yes. At a sharp corner, such as y = |x| at x = 0, the left and right slopes differ, "
                  "so no single tangent slope exists.")},
     ]},
    {"title": tr("Rules"),
     "items": [
         {"q": tr("State the product rule."),
          "a": tr("(uv)′ = u′v + uv′ - differentiate one factor at a time and add.")},
         {"q": tr("State the quotient rule."),
          "a": tr("(u/v)′ = (u′v − uv′)/v², with the derivative of the numerator first.")},
         {"q": tr("Why is (uv)′ not u′v′?"),
          "a": tr("Because y = x²(3x + 5) would then differentiate to 6x, while the true answer is "
                  "9x² + 10x. The rule accounts for both factors changing at once.")},
         {"q": tr("State the chain rule."),
          "a": tr("dy/dx = dy/du × du/dx: differentiate the outside, then multiply by the derivative "
                  "of the inside.")},
         {"q": tr("Differentiate sin 5x."),
          "a": tr("5 cos 5x. The inside derivative 5 must be included.")},
         {"q": tr("Differentiate (3x + 2)⁵."),
          "a": tr("15(3x + 2)⁴: 5(3x + 2)⁴ from the power and 3 from the inside.")},
     ]},
    {"title": tr("Implicit, parametric, logarithmic and applications"),
     "items": [
         {"q": tr("What is an implicit function?"),
          "a": tr("One where x and y are mixed in a single equation, such as x² + y² = 25, so y is "
                  "not written alone.")},
         {"q": tr("When differentiating an implicit equation, what extra factor appears?"),
          "a": tr("dy/dx. Every y-term gains one, because y is a function of x (chain rule).")},
         {"q": tr("How do you find dy/dx for a parametric curve?"),
          "a": tr("Differentiate both x and y with respect to the parameter, then divide: "
                  "dy/dx = (dy/dt)/(dx/dt).")},
         {"q": tr("When do you use logarithmic differentiation?"),
          "a": tr("When the variable appears in the power (xˣ), or when the expression is a long "
                  "product or quotient.")},
         {"q": tr("What do velocity and acceleration mean in calculus?"),
          "a": tr("v = ds/dt (rate of change of position) and a = dv/dt = d²s/dt² (rate of change of "
                  "velocity).")},
         {"q": tr("How do you test whether a stationary point is a maximum or a minimum?"),
          "a": tr("Use the second derivative: f″ &lt; 0 gives a maximum, f″ > 0 a minimum. If f″ = 0, "
                  "check the sign of f′ on both sides.")},
     ]},
]

EXAM = [
    {"q": tr("Differentiate f(x) = x² from first principles."), "marks": 3},
    {"q": tr("Differentiate √x from first principles."), "marks": 4},
    {"q": tr("Differentiate y = 4x³ − 6x² + 2x − 5 and find the slope at x = 1."), "marks": 3},
    {"q": tr("Differentiate y = x²(2x − 3) by the product rule."), "marks": 3},
    {"q": tr("Differentiate y = (3x + 1)/(x + 2) by the quotient rule."), "marks": 4},
    {"q": tr("Differentiate y = (2x + 5)⁶."), "marks": 3},
    {"q": tr("Differentiate y = cos 4x and y = e^(5x)."), "marks": 3},
    {"q": tr("Differentiate y = √(3x + 4)."), "marks": 3},
    {"q": tr("Find dy/dx if x² + y² = 36, and the slope at (4, √20)."), "marks": 4},
    {"q": tr("Find dy/dx if x² + 4xy + y² = 10."), "marks": 4},
    {"q": tr("Find dy/dx for x = 3t², y = 6t, and the slope at t = 2."), "marks": 3},
    {"q": tr("Find dy/dx for x = a sec θ, y = b tan θ."), "marks": 4},
    {"q": tr("Differentiate y = xˣ by taking logarithms."), "marks": 4},
    {"q": tr("Find the second derivative of y = x⁵ + sin 2x."), "marks": 3},
    {"q": tr("A particle moves with s = 2t³ − 9t² + 12t. Find its velocity and acceleration at "
             "t = 2 s."), "marks": 4},
    {"q": tr("Find and classify the stationary points of f(x) = x³ − 6x² + 9x."), "marks": 4},
]

PRACTICE_ANSWERS = [
    tr(p("Step 1: f(x + h) − f(x) = (x + h)² − x² = x² + 2xh + h² − x² = 2xh + h².")
    + p("Step 2: divide by h, allowed because h ≠ 0, giving 2x + h.")
    + p("Step 3: let h → 0, so f′(x) = <b>2x</b>.")
    + p("At x = 2 the slope is 4 and at x = −1 it is −2: the tangent falls left of the origin and "
        "rises to the right.")),
    tr(p("Multiply numerator and denominator by the conjugate √(x + h) + √x.")
    + p("The numerator becomes h, so the expression is 1/[√(x + h) + √x], and with h → 0 the "
        "derivative is <b>1/(2√x)</b>. At x = 4 the slope is 1/4.")),
    tr(p("Differentiate term by term: 12x² − 12x + 2.")
    + p("At x = 1 the slope is 12 − 12 + 2 = <b>2</b>. The constant −5 disappears because the "
        "derivative of a constant is zero.")),
    tr(p("u = x², v = 2x − 3, so u′ = 2x and v′ = 2.")
    + p("(uv)′ = 2x(2x − 3) + x²(2) = 4x² − 6x + 2x² = <b>6x² − 6x</b>.")
    + p("Check by expanding: y = 2x³ − 3x² differentiates to 6x² − 6x.")),
    tr(p("u = 3x + 1, v = x + 2, so u′ = 3 and v′ = 1.")
    + p("dy/dx = [3(x + 2) − (3x + 1)]/(x + 2)² = (3x + 6 − 3x − 1)/(x + 2)² = <b>5/(x + 2)²</b>.")
    + p("The answer is positive everywhere, so the curve always rises.")),
    tr(p("This is a function of a function, so use the chain rule with u = 2x + 5.")
    + p("dy/dx = 6(2x + 5)⁵ × 2 = <b>12(2x + 5)⁵</b>.")
    + p("The factor 2 is compulsory; forgetting it is the most common error in this type.")),
    tr(p("For y = cos 4x the inside is 4x, so dy/dx = −sin(4x) × 4 = <b>−4 sin 4x</b>.")
    + p("For y = e^(5x) the derivative of e^u is e^u, so dy/dx = e^(5x) × 5 = <b>5e^(5x)</b>.")
    + p("Notice that each derivative keeps the same function and only the inside factor changes.")),
    tr(p("Write the root as a power, y = (3x + 4)^(1/2), and use the chain rule with u = 3x + 4.")
    + p("dy/dx = (1/2)(3x + 4)^(−1/2) × 3, and the negative power puts the root underneath: "
        "dy/dx = <b>3/(2√(3x + 4))</b>.")
    + p("At x = 0 the slope is 3/(2√4) = 3/4, and the slope falls as x grows because the root in "
        "the denominator becomes larger.")),
    tr(p("Differentiate implicitly: 2x + 2y(dy/dx) = 0, so dy/dx = <b>−x/y</b>.")
    + p("At (4, √20) the slope is −4/√20 = −2/√5.")
    + p("The tangent there is y − √20 = (−2/√5)(x − 4), which can be left in this form.")),
    tr(p("Differentiate term by term, using the product rule on 4xy: 2x + 4[y + x(dy/dx)] + "
         "2y(dy/dx) = 0.")
    + p("Collect the dy/dx terms: (4x + 2y)(dy/dx) = −(2x + 4y).")
    + p("So dy/dx = <b>−(x + 2y)/(2x + y)</b> after dividing by 2.")),
    tr(p("dx/dt = 6t and dy/dt = 6, so dy/dx = 6/(6t) = <b>1/t</b>.")
    + p("At t = 2 the slope is 1/2, and the point is x = 12, y = 12.")
    + p("The curve is a parabola and the slope falls as t grows, which matches the shape.")),
    tr(p("dx/dθ = a sec θ tan θ and dy/dθ = b sec²θ.")
    + p("So dy/dx = b sec²θ /(a sec θ tan θ) = <b>(b/a)(sec θ/tan θ) = (b/a) cosec θ</b>.")
    + p("Writing it as (b/a)·(1/sin θ) is the tidiest final form.")),
    tr(p("Take logarithms: log y = x log x.")
    + p("Differentiate: (1/y)(dy/dx) = log x + 1, so dy/dx = <b>xˣ(1 + log x)</b>.")
    + p("At x = 1 the slope is 1(0 + 1) = 1, and at x = 1/e it is zero, which is the minimum of the "
        "curve.")),
    tr(p("y′ = 5x⁴ + 2 cos 2x, using the chain rule on sin 2x.")
    + p("Differentiate again: y″ = <b>20x³ − 4 sin 2x</b>.")
    + p("Each differentiation of sin 2x brings a factor 2, so cos 2x becomes −4 sin 2x.")),
    tr(p("v = ds/dt = 6t² − 18t + 12 and a = dv/dt = 12t − 18.")
    + p("At t = 2: v = 24 − 36 + 12 = <b>0 m/s</b> and a = 24 − 18 = <b>6 m/s²</b>.")
    + p("A zero velocity means the particle is momentarily at rest, yet it still has acceleration - "
        "the turning point of its motion.")),
    tr(p("f′(x) = 3x² − 12x + 9 = 3(x − 1)(x − 3), so the stationary points are x = 1 and x = 3.")
    + p("f″(x) = 6x − 12: f″(1) = −6 &lt; 0 → maximum, f(1) = 4; f″(3) = 6 > 0 → minimum, f(3) = 0.")
    + p("The curve rises to 4, falls to 0 and then climbs again.")),
]

LESSON_COUNT = sum(len(s["items"]) for s in NOTES)
