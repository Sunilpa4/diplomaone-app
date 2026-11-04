"""DI01000021 Mathematics-I - Unit 1: Determinant and Function (GTU 1.1-1.4, 9 h, 23 %, 16 marks).

Determinants up to the third order (no properties - expansion by minors and cofactors, as the syllabus
says), then functions and the logarithm as a function, with the laws of logarithms and their numericals.
"""
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
    ("Khan Academy - determinants and logarithms",
     "https://www.khanacademy.org/math/algebra2"),
    ("GeoGebra - plot y = log x beside y = a^x and slide the base",
     "https://www.geogebra.org/"),
    ("OpenStax - College Algebra 2e, chapters on functions and exponential/logarithmic functions",
     "https://openstax.org/details/books/college-algebra-2e"),
    ("John Bird - Understanding Engineering Mathematics (Routledge)",
     "https://www.routledge.com/Understanding-Engineering-Mathematics/Bird/p/book/9780415662840"),
]

NOTES = [
    {"title": tr("1. Determinant of the Second Order"),
     "items": [
         card("1.1 What a determinant is",
              h4("Definition")
              + p("A <b>determinant</b> is a single number calculated from a square array of numbers. For a "
                  "second-order determinant the array has two rows and two columns:")
              + p("<b>|a b; c d| = ad − bc</b> - the product of the main diagonal minus the product of the "
                  "other diagonal.")
              + h4("Notation that matters")
              + ul("Vertical bars mean <i>value</i>: |3 5; 2 4| = 2. Brackets [3 5; 2 4] mean a "
                   "<i>matrix</i>, which is an array, not a number.",
                   "The determinant of matrix A is written |A| or det(A).",
                   "Read it as <b>[a b; c d]</b> in the same layout as the array: a and d are on the main "
                   "diagonal (top-left to bottom-right).")
              + h4("Worked example")
              + p("|3 5; 2 4| = (3)(4) − (5)(2) = 12 − 10 = <b>2</b>.")
              + sc("Is |2 4; 1 2| zero?", "Yes: (2)(2) − (4)(1) = 0. Rows (and columns) are proportional, "
                                        "which is exactly what a zero determinant signals."),
              "m1_det2", examples=["m1n1", "m1n2"], syllabus_item="1.1"),
         card("1.2 Second-order determinants with a variable, and what a zero says",
              h4("Definition")
              + p("The entries may be expressions, so the determinant becomes an equation in x. Solve it "
                  "exactly as a quadratic once the expansion is done.")
              + h4("Worked example")
              + p("Find x if |x 2; 3 x| = 10. Expand: x·x − 2·3 = 10 → x² − 6 = 10 → x² = 16 → "
                  "<b>x = 4 or x = −4</b>.")
              + h4("Reading a zero determinant")
              + table(["Determinant", "Meaning for two equations in x and y"],
                      [("D ≠ 0", "Unique solution - the two lines cross once"),
                       ("D = 0 but Dx or Dy ≠ 0", "No solution - the lines are parallel"),
                       ("D = 0 and Dx = Dy = 0", "Infinitely many solutions - the same line twice")])
              + h4("Common mistake / conditions")
              + p("Do not write x² = 16 and answer x = 4 only. A squared equation has two roots; in a "
                  "geometry question you may reject the negative one, but you must say so."),
              examples=["m1n3"], syllabus_item="1.1")]},

    {"title": tr("2. Determinant of the Third Order"),
     "items": [
         card("2.1 Expansion along the first row",
              h4("Definition")
              + p("A third-order determinant is expanded into three second-order determinants, with alternating "
                  "signs <b>+ − +</b> along the first row:")
              + p("<b>|a₁ b₁ c₁; a₂ b₂ c₂; a₃ b₃ c₃| = a₁(b₂c₃ − b₃c₂) − b₁(a₂c₃ − a₃c₂) + c₁(a₂b₃ − a₃b₂)</b>")
              + h4("The three steps")
              + ol("<b>Cover</b> the row and column of the entry you are multiplying.",
                   "<b>Write</b> the 2×2 determinant that is left (this is the <i>minor</i>).",
                   "<b>Attach</b> the sign from the pattern + − + / − + − / + − + and add the three terms.")
              + h4("Worked example")
              + p("|1 2 3; 4 5 6; 7 8 10| = 1(5×10 − 6×8) − 2(4×10 − 6×7) + 3(4×8 − 5×7) = 1(2) − 2(−2) + 3(−3) = "
                  "2 + 4 − 9 = <b>−3</b>.")
              + h4("Common mistake / conditions")
              + p("The signs belong to the <i>position</i>, not to the entry. If b₁ is already negative, its "
                  "term is −(−3)(minor) = +3(minor). Write the sign in brackets before substituting."),
              "m1_det3", examples=["m1n4", "m1n5"], syllabus_item="1.1"),
         card("2.2 Minors and cofactors",
              h4("Definition")
              + p("The <b>minor</b> Mᵢⱼ of an entry is the 2×2 determinant left after deleting row i and column j. "
                  "The <b>cofactor</b> is the same number with the positional sign:")
              + p("<b>Cᵢⱼ = (−1)^(i+j) Mᵢⱼ</b>")
              + h4("The sign board")
              + table(["", "column 1", "column 2", "column 3"],
                      [("row 1", "+", "−", "+"),
                       ("row 2", "−", "+", "−"),
                       ("row 3", "+", "−", "+")])
              + h4("Worked idea")
              + p("For A = [2 3 1; 4 0 5; 1 2 3], the minor of the 4 (row 2, column 1) is |3 1; 2 3| = 9 − 2 = 7, "
                  "and its cofactor is −7 because position (2, 1) carries a minus.")
              + h4("Why both names exist")
              + p("The determinant equals the sum a₁₁C₁₁ + a₁₂C₁₂ + a₁₃C₁₃ along <i>any</i> row or column. "
                  "Cofactors are also the raw material of the adjoint and the inverse in later semesters."),
              examples=["m1n6"], syllabus_item="1.1"),
         card("2.3 Choosing the easiest row, and the Sarrus shortcut",
              h4("Definition")
              + p("Because any row or column may be used, choose the one with the most zeros: every zero kills "
                  "a whole 2×2 determinant and saves arithmetic.")
              + h4("Worked example")
              + p("|2 −1 3; 0 4 −2; 5 1 0| - the second row has a zero, but the third column has one too. "
                  "Expanding along the third column: 3(0×1 − 4×5) − (−2)(2×1 − (−1)×5) + 0 = −60 + 2(7) = "
                  "<b>−46</b>.")
              + h4("Sarrus rule (third order only)")
              + p("Copy the first two columns to the right and add the three down-right diagonals, then "
                  "subtract the three down-left diagonals. It is a check, not a substitute for the expansion: "
                  "for the matrix above Sarrus gives 0 + (−10) + 0 − (60 + 0 + 0) = −46 ✓.")
              + h4("Conditions")
              + p("Sarrus works only for 3×3. Never try it on a 4×4 - the diagonal trick does not generalise."),
              "m1_det3", examples=["m1n5"], syllabus_item="1.1")]},

    {"title": tr("3. Applications of Determinants"),
     "items": [
         card("3.1 Cramer's rule for two equations",
              h4("Definition")
              + p("For a₁x + b₁y = c₁ and a₂x + b₂y = c₂, build three determinants:")
              + p("<b>D = |a₁ b₁; a₂ b₂|,  Dx = |c₁ b₁; c₂ b₂|,  Dy = |a₁ c₁; a₂ c₂|</b>")
              + p("then <b>x = Dx/D</b> and <b>y = Dy/D</b>, provided D ≠ 0.")
              + h4("Worked example")
              + p("2x + 3y = 12, x − y = 1. D = (2)(−1) − (3)(1) = −5; Dx = (12)(−1) − (3)(1) = −15; "
                  "Dy = (2)(1) − (12)(1) = −10. So x = 3, y = 2.")
              + h4("Common mistake / conditions")
              + p("The column that is replaced is the one of the variable you are finding: for Dx replace the "
                  "<b>x-column</b> (the first) by the constants. Swapping the wrong column gives the other "
                  "variable's value and is the most common error in this question."),
              "m1_cramer", examples=["m1n7"], syllabus_item="1.1"),
         card("3.2 Cramer's rule for three equations",
              h4("Definition")
              + p("Three equations in x, y, z need four determinants: D, Dx, Dy, Dz, each third order. Replace "
                  "one column of the coefficient determinant by the constants each time.")
              + h4("Worked example")
              + p("x + y + z = 6, x − y + z = 2, 2x + y − z = 1. Expanding the coefficient determinant by the "
                  "first row gives D = 6; then Dx = 6, Dy = 12, Dz = 18, so x = 1, y = 2, z = 3 - which checks "
                  "in all three equations.")
              + h4("Practical advice")
              + p("Cramer is long for 3×3. Use it when the question <i>asks</i> for determinants, and use "
                  "elimination when it only asks for the solution. Either way the check is the same: substitute "
                  "all three values into all three equations."),
              examples=["m1n8"], syllabus_item="1.1"),
         card("3.3 Area of a triangle and the collinearity test",
              h4("Formula")
              + p("For vertices (x₁, y₁), (x₂, y₂), (x₃, y₃):")
              + p("<b>Area = ½ |x₁(y₂ − y₃) + x₂(y₃ − y₁) + x₃(y₁ − y₂)|</b>, equal to ½ |det| of the "
                  "3×3 determinant with a final column of 1s.")
              + h4("Worked example")
              + p("(1, 2), (4, 6), (7, 2): ½|1(6 − 2) + 4(2 − 2) + 7(2 − 6)| = ½|4 + 0 − 28| = <b>12 square "
                  "units</b>.")
              + h4("Collinearity")
              + p("If the three points lie on one line the triangle has no area, so the determinant is zero. "
                  "That single test answers every \"show that the points are collinear\" question - and its "
                  "converse is a fast check of your own answer."),
              examples=["m1n9", "m1n10"], syllabus_item="1.1")]},

    {"title": tr("4. Function and Simple Examples"),
     "items": [
         card("4.1 Definition, notation, domain, codomain and range",
              h4("Definition")
              + p("A <b>function</b> f from set A to set B assigns <i>exactly one</i> element of B to every "
                  "element of A. Written <b>f : A → B, y = f(x)</b>.")
              + h4("The four words")
              + table(["Word", "Meaning", "Example for f(x) = x², A = {−2, −1, 0, 1, 2}"],
                      [("Domain", "Everything you may put in", "{−2, −1, 0, 1, 2} (or all real x)"),
                       ("Codomain", "The set you are mapping into", "the real numbers"),
                       ("Range", "What actually comes out", "{0, 1, 4}"),
                       ("Image", "Output for one particular input", "f(2) = 4")])
              + h4("One input, one output")
              + p("The rule \"one value in, exactly one value out\" is what makes it a function. y² = x is "
                  "<i>not</i> a function of x, because x = 4 gives both y = 2 and y = −2. On a graph, a "
                  "vertical line may meet a function's curve only once."),
              "m1_function", examples=["m1n11"], syllabus_item="1.2"),
         card("4.2 Finding the domain",
              h4("Definition")
              + p("The domain is restricted by two things only at this level: a denominator may not be zero, "
                  "and an even root may not be negative.")
              + h4("Rules")
              + table(["Function", "Restriction", "Domain"],
                      [("1/(x − 3)", "x − 3 ≠ 0", "all real x except 3"),
                       ("√(x − 2)", "x − 2 ≥ 0", "x ≥ 2, that is [2, ∞)"),
                       ("1/√(x − 2)", "x − 2 > 0", "x > 2"),
                       ("log x", "x > 0", "(0, ∞)"),
                       ("polynomial", "none", "all real x")])
              + h4("Common mistake / conditions")
              + p("In 1/√(x − 2) the root already forbids negatives, and the denominator forbids zero, so the "
                  "endpoint 2 is excluded (<b>&gt;</b>, not ≥). One word changes the whole answer - write the "
                  "condition before the interval."),
              examples=["m1n12"], syllabus_item="1.2"),
         card("4.3 Standard functions and their graphs",
              h4("Definition")
              + p("Five shapes cover almost every question in this unit. Knowing the shape lets you read the "
                  "domain and range straight off the picture.")
              + table(["Function", "Rule", "Shape", "Range (a > 0)"],
                      [("Constant", "y = c", "horizontal line", "{c}"),
                       ("Linear", "y = mx + c", "straight line", "all real y"),
                       ("Quadratic", "y = ax² + bx + c", "parabola", "y ≥ vertex value"),
                       ("Exponential", "y = aˣ", "always rising, asymptotic to the x-axis", "y > 0"),
                       ("Logarithmic", "y = logₐ x", "mirror of the exponential", "all real y")])
              + h4("Reading a graph")
              + ol("Domain: project the curve onto the x-axis.",
                   "Range: project it onto the y-axis.",
                   "A hole or a vertical asymptote is a value the function never takes - exclude it.")
              + h4("Worked example")
              + p("For y = x² − 4x + 7, completing the square gives y = (x − 2)² + 3, so the range is "
                  "<b>y ≥ 3</b> with the vertex at (2, 3)."),
              "m1_graphs", examples=["m1n13"], syllabus_item="1.2"),
         card("4.4 Even, odd and piecewise functions",
              h4("Definition")
              + p("A function is <b>even</b> if f(−x) = f(x) (symmetric about the y-axis) and <b>odd</b> if "
                  "f(−x) = −f(x) (symmetric about the origin). A <b>piecewise</b> function uses a different "
                  "rule on different parts of its domain.")
              + h4("Test procedure")
              + ol("Replace every x by −x.",
                   "Simplify and compare with f(x) and −f(x).",
                   "Equal to f(x): even. Equal to −f(x): odd. Neither: neither - and say so.")
              + h4("Worked examples")
              + p("f(x) = x³ − x: f(−x) = −x³ + x = −(x³ − x) → <b>odd</b>. g(x) = x² + 1: g(−x) = x² + 1 = g(x) "
                  "→ <b>even</b>. h(x) = x² + x: h(−x) = x² − x, which is neither → <b>neither</b>.")
              + p("For f(x) = x + 1 when x &lt; 0 and f(x) = x² when x ≥ 0: f(−2) = −1 and f(3) = 9. Choose the "
                  "rule by the input, never by the answer."),
              examples=["m1n14", "m1n15"], syllabus_item="1.2")]},

    {"title": tr("5. Logarithm as a Function"),
     "items": [
         card("5.1 Definition: the inverse of the exponential",
              h4("Definition")
              + p("<b>y = logₐ x  ⇔  aʸ = x</b>, where a &gt; 0, a ≠ 1 and x &gt; 0. The logarithm answers the "
                  "question \"to what power must the base be raised?\"")
              + h4("The two directions")
              + table(["Logarithm form", "Exponential form", "Read as"],
                      [("log₂ 32 = 5", "2⁵ = 32", "2 to the power 5 is 32"),
                       ("log₅ 1 = 0", "5⁰ = 1", "any base to the power 0 is 1"),
                       ("log₃ (1/27) = −3", "3⁻³ = 1/27", "a negative logarithm means a fraction"),
                       ("log₁₀ 1000 = 3", "10³ = 1000", "common logarithm")])
              + h4("Two values worth memorising")
              + p("<b>logₐ 1 = 0</b> and <b>logₐ a = 1</b>. Both follow from the definition and both are used "
                  "to simplify answers.")
              + h4("Common mistake / conditions")
              + p("The base is written small and low: logₐ x. log 100 with no base means base 10, and ln x "
                  "means base e ≈ 2.718. Never take the log of a negative number or of zero - the domain is "
                  "x &gt; 0."),
              "m1_exp_log", examples=["m1n16", "m1n17"], syllabus_item="1.3"),
         card("5.2 Domain, range and the graph",
              h4("Definition")
              + p("Because aˣ is always positive, only positive numbers have logarithms: the <b>domain of "
                  "logₐ x is (0, ∞)</b>. The output can be any real number, so the <b>range is (−∞, ∞)</b>.")
              + h4("The mirror")
              + p("Swap x and y in y = aˣ and you get x = aʸ, that is y = logₐ x. The two graphs are reflections "
                  "of each other in the line y = x. The exponential has a horizontal asymptote y = 0; the "
                  "logarithm has a vertical asymptote x = 0 and crosses the x-axis at (1, 0).")
              + h4("Shape warnings")
              + ul("a &gt; 1: the curve rises slowly; log₁₀ 1000 = 3 while log₁₀ 10 = 1.",
                   "0 &lt; a &lt; 1: the curve falls - a decreasing logarithm.",
                   "The curve never touches x = 0; it dives without reaching it.")
              + h4("Application")
              + p("Logarithms turn multiplication into addition, which is why they appear wherever a quantity "
                  "grows by a fixed <i>factor</i> - sound level, earthquake magnitude, pH, and the number of "
                  "digits of a large power."),
              "m1_exp_log", examples=["m1n16"], syllabus_item="1.3"),
         card("5.3 Common and natural logarithms",
              h4("Definition")
              + p("<b>log x</b> (base 10) is used in engineering data tables; <b>ln x</b> (base e) is used in "
                  "calculus and in growth/decay formulae. Both obey the same laws - only the base changes.")
              + h4("Useful numbers")
              + table(["Quantity", "Value", "Why it is useful"],
                      [("log₁₀ 2", "0.3010", "halving and doubling times"),
                       ("log₁₀ 3", "0.4771", "powers of 3"),
                       ("log₁₀ e", "0.4343", "convert ln to log"),
                       ("ln 2", "0.6931", "half-life and doubling time"),
                       ("ln 10", "2.3026", "convert log to ln")])
              + h4("Converting")
              + p("<b>ln x = 2.3026 log x</b> and <b>log x = 0.4343 ln x</b>. The conversion is just the change "
                  "of base formula with base e, which appears in the next section.")
              + h4("Common mistake / conditions")
              + p("log 2 + log 3 = log 6, but log 2 × log 3 is <i>not</i> log 6 - the laws apply to the sum of "
                  "logs, not to their product. Keep the operation and the law matched."),
              examples=["m1n20"], syllabus_item="1.3")]},

    {"title": tr("6. Laws of Logarithm"),
     "items": [
         card("6.1 The three main laws",
              h4("Definition")
              + p("For a &gt; 0, a ≠ 1 and positive x, y:")
              + table(["Law", "Statement", "Example"],
                      [("Product", "logₐ(xy) = logₐ x + logₐ y", "log 6 = log 2 + log 3"),
                       ("Quotient", "logₐ(x/y) = logₐ x − logₐ y", "log 1.5 = log 3 − log 2"),
                       ("Power", "logₐ(xⁿ) = n logₐ x", "log 8 = 3 log 2")])
              + h4("Why they hold")
              + p("Write x = aᵐ and y = aⁿ. Then xy = aᵐ⁺ⁿ, so logₐ(xy) = m + n = logₐ x + logₐ y. The laws "
                  "are consequences of the index laws - not new rules to memorise.")
              + h4("Using them in both directions")
              + p("<b>Expand:</b> log(3x²/y) = log 3 + 2 log x − log y. <b>Condense:</b> 2 log 3 + log 4 − log 6 = "
                  "log(9 × 4 / 6) = log 6. Exams ask for both directions, so practise both."),
              "m1_loglaws", examples=["m1n18", "m1n19"], syllabus_item="1.4"),
         card("6.2 Change of base and the derived laws",
              h4("Definition")
              + p("<b>logₐ x = log_b x / log_b a</b>. Choosing b = 10 turns any base into a calculator "
                  "evaluation; choosing b = x gives logₐ x · log_x a = 1.")
              + h4("Derived results")
              + table(["Result", "How it follows"],
                      [("logₐ(1/x) = −logₐ x", "power law with n = −1"),
                       ("logₐ b = 1 / log_b a", "change of base, then simplify"),
                       ("logₐ a = 1 and logₐ 1 = 0", "definition"),
                       ("a^(logₐ x) = x", "the two operations undo each other")])
              + h4("Worked example")
              + p("log₄ 8 = log 8 / log 4 = 3 log 2 / 2 log 2 = 3/2 = 1.5. The powers of 2 cancel, so no "
                  "calculator is needed - always look for a common base first.")
              + h4("Common mistake / conditions")
              + p("log(x + y) is not log x + log y, and (log x)² is not 2 log x. The laws act on products, "
                  "quotients and powers - nothing else."),
              "m1_loglaws", examples=["m1n21", "m1n25"], syllabus_item="1.4"),
         card("6.3 Solving equations with logarithms",
              h4("Definition")
              + p("Two moves solve almost everything: convert a log equation to exponential form, or take logs "
                  "of both sides of an exponential equation.")
              + h4("Worked examples")
              + p("<b>log₂(x + 3) = 4</b> → x + 3 = 2⁴ = 16 → x = 13. <b>2ˣ = 32</b> → x = log₂ 32 = 5, or take "
                  "log₁₀ of both sides: x log 2 = log 32 → x = 1.505/0.301 = 5.")
              + h4("Check every root")
              + p("A solution that makes any argument zero or negative is rejected: log₂(x − 5) = 2 gives "
                  "x = 9, which is fine, but a computed x = 3 would be rejected because log₂(3 − 5) does not "
                  "exist. Write the domain condition first, then solve.")
              + h4("Engineering use")
              + p("pH = −log₁₀[H⁺] and sound level L = 10 log₁₀(I/I₀). A pH of 4 means [H⁺] = 10⁻⁴ mol/L; a "
                  "20 dB increase is a hundredfold increase in intensity, not double."),
              examples=["m1n22", "m1n23", "m1n24"], syllabus_item="1.4")]},

    {"title": tr("7. Answered Practice (Unit 1 level)"), "items": []},
]

GIVEN = h4("Given and assumptions")
FORMULA = h4("Formula")
STEPS = h4("Step-by-step solution")
CHECK = h4("Interpretation and check")


def num(nid, q, chunks):
    return {"id": nid, "q": tr(q), "a": tr("".join(chunks))}


NUMERICALS = [
    num("m1n1", "Evaluate the determinant |3 5; 2 4|.",
        [GIVEN + p("A second-order determinant: rows (3, 5) and (2, 4)."),
         FORMULA + p("|a b; c d| = ad − bc"),
         STEPS + ol("Main diagonal: 3 × 4 = 12", "Other diagonal: 5 × 2 = 10", "12 − 10 = 2"),
         CHECK + p("<b>2.</b> The determinant is a single number, so the answer must not be written as an "
                   "array. A quick mental check: 12 is bigger than 10, so the sign is positive.")]),
    num("m1n2", "Evaluate |−4 7; 3 −2|.",
        [GIVEN + p("Negative entries - keep each sign with its number."),
         FORMULA + p("ad − bc"),
         STEPS + ol("a = −4, d = −2 → (−4)(−2) = 8", "b = 7, c = 3 → (7)(3) = 21", "8 − 21 = −13"),
         CHECK + p("<b>−13.</b> Check by expanding along the second row instead: −(3)(7) + (−2)(−4) = −21 + 8 = "
                   "−13 ✓ - the value is the same whichever row you use.")]),
    num("m1n3", "Find x if |x 2; 3 x| = 10.",
        [GIVEN + p("The entries contain x, so the determinant becomes an equation."),
         FORMULA + p("|x 2; 3 x| = x·x − 2·3"),
         STEPS + ol("x² − 6 = 10", "x² = 16", "x = 4 or x = −4"),
         CHECK + p("<b>x = ±4.</b> Check both: for x = 4 the determinant is 16 − 6 = 10 ✓; for x = −4 it is also "
                   "16 − 6 = 10 ✓. Both roots are valid unless the question names a positive x.")]),
    num("m1n4", "Evaluate |1 2 3; 4 5 6; 7 8 10| by expanding along the first row.",
        [GIVEN + p("Third-order determinant with the sign pattern + − + along row 1."),
         FORMULA + p("a₁(b₂c₃ − b₃c₂) − b₁(a₂c₃ − a₃c₂) + c₁(a₂b₃ − a₃b₂)"),
         STEPS + ol("1 × (5×10 − 6×8) = 1 × 2 = 2",
                    "−2 × (4×10 − 6×7) = −2 × (−2) = +4",
                    "3 × (4×8 − 5×7) = 3 × (−3) = −9",
                    "2 + 4 − 9 = −3"),
         CHECK + p("<b>−3.</b> Sarrus check: (1·5·10 + 2·6·7 + 3·4·8) − (3·5·7 + 1·6·8 + 2·4·10) = "
                   "(50 + 84 + 96) − (105 + 48 + 80) = 230 − 233 = −3 ✓.")]),
    num("m1n5", "Evaluate |2 −1 3; 0 4 −2; 5 1 0| using the most convenient line.",
        [GIVEN + p("Two zeros: entry (2, 1) and entry (3, 3)."),
         FORMULA + p("Expand along the third column (entries 3, −2, 0)"),
         STEPS + ol("3 × (0×1 − 4×5) = 3 × (−20) = −60",
                    "−(−2) × (2×1 − (−1)×5) = +2 × 7 = +14",
                    "0 × (minor) = 0",
                    "−60 + 14 + 0 = −46"),
         CHECK + p("<b>−46.</b> The same answer comes from row 2: −0(...) + 4(2×0 − 3×5) − (−2)(2×1 − (−1)5) = "
                   "−60 + 14 = −46 ✓. Choosing the line with zeros halves the arithmetic.")]),
    num("m1n6", "For A = [2 3 1; 4 0 5; 1 2 3] write the cofactor of each entry and find |A|.",
        [GIVEN + p("Nine minors, each with the positional sign from the + − + board."),
         FORMULA + p("Cᵢⱼ = (−1)^(i+j) Mᵢⱼ"),
         STEPS + ol("C₁₁ = +(0×3 − 5×2) = −10; C₁₂ = −(4×3 − 5×1) = −7; C₁₃ = +(4×2 − 0×1) = 8",
                    "C₂₁ = −(3×3 − 1×2) = −7; C₂₂ = +(2×3 − 1×1) = 5; C₂₃ = −(2×2 − 3×1) = −1",
                    "C₃₁ = +(3×5 − 1×0) = 15; C₃₂ = −(2×5 − 1×4) = −6; C₃₃ = +(2×0 − 3×4) = −12",
                    "|A| = 2(−10) + 3(−7) + 1(8) = −20 − 21 + 8 = −33"),
         CHECK + p("<b>|A| = −33.</b> Sarrus: (0 + 15 + 8) − (0 + 36 + 20) = 23 − 56 = −33 ✓. Note that the "
                   "cofactors are <i>not</i> all positive - the board alternates by position.")]),
    num("m1n7", "Solve 2x + 3y = 12 and x − y = 1 by Cramer's rule.",
        [GIVEN + p("Coefficients a₁ = 2, b₁ = 3, c₁ = 12 and a₂ = 1, b₂ = −1, c₂ = 1."),
         FORMULA + p("D = |a₁ b₁; a₂ b₂|, Dx = |c₁ b₁; c₂ b₂|, Dy = |a₁ c₁; a₂ c₂|, x = Dx/D, y = Dy/D"),
         STEPS + ol("D = (2)(−1) − (3)(1) = −5",
                    "Dx = (12)(−1) − (3)(1) = −15, so x = −15/−5 = 3",
                    "Dy = (2)(1) − (12)(1) = −10, so y = −10/−5 = 2"),
         CHECK + p("<b>x = 3, y = 2.</b> Check in the original equations: 2(3) + 3(2) = 12 ✓ and 3 − 2 = 1 ✓. "
                   "D ≠ 0, so the system has exactly one solution - consistent with the lines crossing once.")]),
    num("m1n8", "Solve x + y + z = 6, x − y + z = 2, 2x + y − z = 1 by determinants.",
        [GIVEN + p("Coefficient matrix [1 1 1; 1 −1 1; 2 1 −1]; constants (6, 2, 1)."),
         FORMULA + p("D, Dx, Dy, Dz - replace one column of coefficients by the constants each time"),
         STEPS + ol("D = 1(1 − 1) − 1(−1 − 2) + 1(1 + 2) = 0 + 3 + 3 = 6",
                    "Dx = 6(1 − 1) − 1(−2 − 1) + 1(2 + 1) = 0 + 3 + 3 = 6 → x = 1",
                    "Dy = 1(−2 − 1) − 6(−1 − 2) + 1(1 − 4) = −3 + 18 − 3 = 12 → y = 2",
                    "Dz = 1(−1 − 2) − 1(1 − 4) + 6(1 + 2) = −3 + 3 + 18 = 18 → z = 3"),
         CHECK + p("<b>x = 1, y = 2, z = 3.</b> Check all three: 1 + 2 + 3 = 6 ✓; 1 − 2 + 3 = 2 ✓; "
                   "2(1) + 2 − 3 = 1 ✓. D = 6 ≠ 0 guarantees a unique solution.")]),
    num("m1n9", "Find the area of the triangle with vertices A(1, 2), B(4, 6), C(7, 2).",
        [GIVEN + p("Three vertices; the base AC is horizontal at y = 2 from x = 1 to x = 7."),
         FORMULA + p("Area = ½|x₁(y₂ − y₃) + x₂(y₃ − y₁) + x₃(y₁ − y₂)|"),
         STEPS + ol("1(6 − 2) = 4", "4(2 − 2) = 0", "7(2 − 6) = −28",
                    "Area = ½|4 + 0 − 28| = ½ × 24 = 12"),
         CHECK + p("<b>12 square units.</b> Geometric check: base AC = 7 − 1 = 6 units and the height of B "
                   "above the base is 6 − 2 = 4 units, so area = ½ × 6 × 4 = 12 ✓.")]),
    num("m1n10", "Show that the points (1, 2), (3, 6) and (5, 10) are collinear.",
        [GIVEN + p("Collinear points enclose no area, so the determinant form must vanish."),
         FORMULA + p("½|x₁(y₂ − y₃) + x₂(y₃ − y₁) + x₃(y₁ − y₂)| = 0 means collinear"),
         STEPS + ol("1(6 − 10) = −4", "3(10 − 2) = 24", "5(2 − 6) = −20",
                    "−4 + 24 − 20 = 0, so the area is 0"),
         CHECK + p("<b>Collinear.</b> Confirmation by slope: the slope from (1, 2) to (3, 6) is 4/2 = 2 and from "
                   "(3, 6) to (5, 10) is also 4/2 = 2, so all three lie on y = 2x.")]),
    num("m1n11", "For f(x) = 2x² − 3x + 1 find f(0), f(2) and f(−1).",
        [GIVEN + p("Substitute each value in brackets and apply BODMAS."),
         FORMULA + p("Replace x by the given number everywhere"),
         STEPS + ol("f(0) = 0 − 0 + 1 = 1",
                    "f(2) = 2(4) − 6 + 1 = 3",
                    "f(−1) = 2(1) + 3 + 1 = 6"),
         CHECK + p("<b>1, 3 and 6.</b> Check f(2) by factorising the answer: 2x² − 3x + 1 = (2x − 1)(x − 1), so "
                   "f(2) = (3)(1) = 3 ✓. The bracket rule saves the sign in f(−1).")]),
    num("m1n12", "Find the domain of f(x) = 1/(x − 3) and of g(x) = √(x − 2).",
        [GIVEN + p("A denominator must not be zero; a square root must not be negative."),
         FORMULA + p("denominator ≠ 0, radicand ≥ 0"),
         STEPS + ol("x − 3 ≠ 0 → x ≠ 3, so the domain of f is all real x except 3",
                    "x − 2 ≥ 0 → x ≥ 2, so the domain of g is [2, ∞)"),
         CHECK + p("<b>R − {3} and [2, ∞).</b> Test one value outside each answer: f(3) is undefined, and "
                   "g(1) = √(−1) is not real ✓. Write the domain as a set or an interval, never as a word.")]),
    num("m1n13", "Find the domain and range of f(x) = x² − 4x + 7.",
        [GIVEN + p("A quadratic; complete the square to read the vertex."),
         FORMULA + p("x² + bx + c = (x + b/2)² + c − b²/4"),
         STEPS + ol("x² − 4x + 7 = (x − 2)² + 3",
                    "Domain: every real x, because a polynomial has no restriction",
                    "Range: (x − 2)² ≥ 0, so f(x) ≥ 3"),
         CHECK + p("<b>Domain R, range [3, ∞), vertex (2, 3).</b> Check f(2) = 4 − 8 + 7 = 3, and f(0) = 7 ≥ 3 ✓. "
                   "The bracket (x − 2)² can never be negative, which is why 3 is the minimum.")]),
    num("m1n14", "Evaluate the piecewise function f(x) = x + 1 for x &lt; 0 and f(x) = x² for x ≥ 0 at "
                 "x = −2, 0 and 3.",
        [GIVEN + p("The rule is chosen by the input, and the boundary value x = 0 belongs to the second rule "
                   "because it is written x ≥ 0."),
         FORMULA + p("Use the branch whose condition the input satisfies"),
         STEPS + ol("x = −2 &lt; 0, so f(−2) = −2 + 1 = −1",
                    "x = 0 ≥ 0, so f(0) = 0² = 0",
                    "x = 3 ≥ 0, so f(3) = 3² = 9"),
         CHECK + p("<b>−1, 0 and 9.</b> Each output is a single number - if you get two answers for one input, "
                   "the branches overlap and the relation is not a function at that point.")]),
    num("m1n15", "Test whether f(x) = x³ − x is even, odd or neither; then test g(x) = x² + x.",
        [GIVEN + p("Replace x by −x and compare."),
         FORMULA + p("Even: f(−x) = f(x); odd: f(−x) = −f(x)"),
         STEPS + ol("f(−x) = (−x)³ − (−x) = −x³ + x = −(x³ − x) = −f(x) → odd",
                    "g(−x) = (−x)² + (−x) = x² − x",
                    "x² − x is neither g(x) = x² + x nor −g(x) = −x² − x → neither"),
         CHECK + p("<b>f is odd, g is neither.</b> Check numerically: f(2) = 6 and f(−2) = −6 (opposite ✓); "
                   "g(2) = 6 but g(−2) = 2, which is neither 6 nor −6 ✓.")]),
    num("m1n16", "Evaluate log₂ 32, log₃ (1/27), log₁₀ 1000 and log₅ 1.",
        [GIVEN + p("Use the definition: logₐ x is the power that turns a into x."),
         FORMULA + p("y = logₐ x ⇔ aʸ = x"),
         STEPS + ol("2⁵ = 32 → log₂ 32 = 5",
                    "3⁻³ = 1/27 → log₃ (1/27) = −3",
                    "10³ = 1000 → log₁₀ 1000 = 3",
                    "5⁰ = 1 → log₅ 1 = 0"),
         CHECK + p("<b>5, −3, 3 and 0.</b> Two sanity rules cover all four: logₐ 1 = 0 always, and a logarithm "
                   "is negative exactly when the argument is below 1 (for base &gt; 1).")]),
    num("m1n17", "Find a if logₐ 8 = 3/2.",
        [GIVEN + p("An unknown base; convert to exponential form."),
         FORMULA + p("logₐ x = y ⇔ aʸ = x"),
         STEPS + ol("a^(3/2) = 8", "Square both sides: a³ = 64", "a = 4"),
         CHECK + p("<b>a = 4.</b> Check: 4^(3/2) = (√4)³ = 2³ = 8 ✓. The base must be positive and not 1 - "
                   "4 satisfies both.")]),
    num("m1n18", "Expand log(3x²/y) using the laws of logarithm.",
        [GIVEN + p("All arguments are positive (x &gt; 0, y &gt; 0), so every law applies."),
         FORMULA + p("log(xy) = log x + log y; log(x/y) = log x − log y; log xⁿ = n log x"),
         STEPS + ol("log(3x²) − log y  (quotient law)",
                    "log 3 + log x² − log y  (product law)",
                    "log 3 + 2 log x − log y  (power law)"),
         CHECK + p("<b>log 3 + 2 log x − log y.</b> Combine it back: log 3 + log x² − log y = log(3x²/y) ✓. The "
                   "number of terms in the answer equals the number of factors in the argument.")]),
    num("m1n19", "Write 2 log 3 + log 4 − log 6 as a single logarithm.",
        [GIVEN + p("Condensing is the reverse of the expansion."),
         FORMULA + p("n log x = log xⁿ, then product and quotient laws"),
         STEPS + ol("2 log 3 = log 9", "log 9 + log 4 = log 36", "log 36 − log 6 = log 6"),
         CHECK + p("<b>log 6.</b> Numerically: 2(0.4771) + 0.6021 − 0.7782 = 0.7781 ≈ log 6 = 0.7782 ✓ (the tiny "
                   "gap is rounding in the tables).")]),
    num("m1n20", "Given log 2 = 0.3010 and log 3 = 0.4771, find log 72.",
        [GIVEN + p("72 is not in the tables, so break it into primes: 72 = 8 × 9 = 2³ × 3²."),
         FORMULA + p("log(xy) = log x + log y and log xⁿ = n log x"),
         STEPS + ol("log 72 = log(2³ × 3²)", "= 3 log 2 + 2 log 3",
                    "= 3(0.3010) + 2(0.4771)", "= 0.9030 + 0.9542 = 1.8572"),
         CHECK + p("<b>1.8572.</b> Check the size: 72 lies between 10 and 100, so log 72 must lie between 1 and "
                   "2 ✓. A result outside that range means a slip in the table values.")]),
    num("m1n21", "Evaluate log₄ 8 without a calculator.",
        [GIVEN + p("Both numbers are powers of 2."),
         FORMULA + p("logₐ x = log_b x / log_b a"),
         STEPS + ol("log₄ 8 = log₂ 8 / log₂ 4", "= 3 / 2", "= 1.5"),
         CHECK + p("<b>3/2.</b> Check by the definition: 4^(3/2) = (√4)³ = 8 ✓. Choosing the common base 2 made "
                   "the division exact - always look for a shared base before reaching for a calculator.")]),
    num("m1n22", "Solve 2ˣ = 32 and log₂(x + 3) = 4.",
        [GIVEN + p("One exponential equation and one logarithmic equation, both base 2."),
         FORMULA + p("Take logarithms of both sides; or convert log form to exponential form"),
         STEPS + ol("2ˣ = 32 = 2⁵ → x = 5",
                    "log₂(x + 3) = 4 → x + 3 = 2⁴ = 16",
                    "x = 13"),
         CHECK + p("<b>x = 5 and x = 13.</b> Check: 2⁵ = 32 ✓ and log₂(13 + 3) = log₂ 16 = 4 ✓. The argument "
                   "13 + 3 = 16 is positive, so no rejection is needed.")]),
    num("m1n23", "Find the pH of a solution with hydrogen-ion concentration [H⁺] = 1 × 10⁻⁴ mol/L.",
        [GIVEN + p("pH = −log₁₀[H⁺]."),
         FORMULA + p("pH = −log₁₀[H⁺]"),
         STEPS + ol("pH = −log₁₀(10⁻⁴)", "log₁₀(10⁻⁴) = −4", "pH = −(−4) = 4"),
         CHECK + p("<b>pH = 4</b>, an acidic solution (below 7). A tenfold increase in [H⁺] lowers the pH by "
                   "exactly 1, because each decade is one unit on a logarithmic scale.")]),
    num("m1n24", "A bacterial culture doubles every 20 minutes. Starting with 1000 bacteria, when will it reach "
                 "8000?",
        [GIVEN + p("Growth by a fixed factor, so the count after t minutes is 1000 × 2^(t/20)."),
         FORMULA + p("1000 × 2^(t/20) = 8000"),
         STEPS + ol("2^(t/20) = 8", "2^(t/20) = 2³", "t/20 = 3", "t = 60 minutes = 1 hour"),
         CHECK + p("<b>60 minutes.</b> Check by counting doublings: 1000 → 2000 (20 min) → 4000 (40 min) → "
                   "8000 (60 min) ✓. With logs: t = 20 log₂ 8 = 20 × 3 = 60.")]),
    num("m1n25", "Show that log₂ 8 × log₈ 2 = 1, and state the general result.",
        [GIVEN + p("log₂ 8 = 3 and log₈ 2 is the same question reversed."),
         FORMULA + p("logₐ b = 1 / log_b a"),
         STEPS + ol("log₂ 8 = 3", "log₈ 2 = 1/3, because 8^(1/3) = 2",
                    "Product = 3 × 1/3 = 1"),
         CHECK + p("<b>1.</b> General rule: logₐ b · log_b a = 1 for any valid bases. It is the change-of-base "
                   "formula with the two bases swapped, and it turns \"evaluate in another base\" questions "
                   "into one division.")]),
]

EQUATIONS = [
    {"title": tr("Determinants"), "items": [
        {"name": tr("Second order"), "f": "|a b; c d| = ad − bc",
         "terms": tr("Main diagonal minus the other diagonal.")},
        {"name": tr("Third order by row 1"), "f": "a₁M₁₁ − b₁M₁₂ + c₁M₁₃",
         "terms": tr("Minors are the 2×2 determinants left after deleting a row and a column.")},
        {"name": tr("Cofactor"), "f": "Cᵢⱼ = (−1)^(i+j) Mᵢⱼ",
         "terms": tr("Signs follow the + − + board of the position, not the entry.")},
        {"name": tr("Cramer's rule"), "f": "x = Dx/D, y = Dy/D (D ≠ 0)",
         "terms": tr("Replace the column of the variable being found by the constants.")},
        {"name": tr("Area of a triangle"), "f": "½ |x₁(y₂ − y₃) + x₂(y₃ − y₁) + x₃(y₁ − y₂)|",
         "terms": tr("Area 0 means the three points are collinear.")},
    ]},
    {"title": tr("Functions"), "items": [
        {"name": tr("Function notation"), "f": "y = f(x), f : A → B",
         "terms": tr("One input gives exactly one output; A is the domain, B the codomain.")},
        {"name": tr("Domain restrictions"), "f": "denominator ≠ 0, radicand ≥ 0, log argument > 0",
         "terms": tr("These three conditions cover every domain question in this unit.")},
        {"name": tr("Even and odd"), "f": "f(−x) = f(x)  or  f(−x) = −f(x)",
         "terms": tr("Even is symmetric about the y-axis, odd about the origin.")},
        {"name": tr("Vertex form"), "f": "ax² + bx + c = a(x + b/2a)² + (c − b²/4a)",
         "terms": tr("Reads off the vertex, hence the range of a quadratic.")},
    ]},
    {"title": tr("Logarithms"), "items": [
        {"name": tr("Definition"), "f": "y = logₐ x ⇔ aʸ = x, x > 0, a > 0, a ≠ 1",
         "terms": tr("A logarithm is an exponent: it answers \"what power of a gives x?\".")},
        {"name": tr("Product and quotient"), "f": "logₐ(xy) = logₐ x + logₐ y;  logₐ(x/y) = logₐ x − logₐ y",
         "terms": tr("Multiplication becomes addition; division becomes subtraction.")},
        {"name": tr("Power law"), "f": "logₐ(xⁿ) = n logₐ x",
         "terms": tr("Brings the exponent down in front - the workhorse of every log numerical.")},
        {"name": tr("Change of base"), "f": "logₐ x = log_b x / log_b a",
         "terms": tr("Use base 10 for a calculator, or the common base of the two numbers.")},
        {"name": tr("Special values"), "f": "logₐ 1 = 0, logₐ a = 1, a^(logₐ x) = x",
         "terms": tr("Immediate from the definition; useful for simplifying final answers.")},
    ]},
]

VIVA = [
    {"title": tr("Determinants"), "items": [
        {"q": tr("What is a determinant?"),
         "a": tr("A single number calculated from a square array of numbers, written with vertical bars.")},
        {"q": tr("State the value of a 2×2 determinant."),
         "a": tr("ad − bc: the product of the main diagonal minus the product of the other diagonal.")},
        {"q": tr("What is the minor of an entry?"),
         "a": tr("The determinant left after deleting the row and the column containing that entry.")},
        {"q": tr("How does a cofactor differ from a minor?"),
         "a": tr("The cofactor adds the positional sign: Cᵢⱼ = (−1)^(i+j) Mᵢⱼ.")},
        {"q": tr("Which row should you choose to expand a third-order determinant?"),
         "a": tr("The one with the most zeros, because each zero removes a whole 2×2 determinant.")},
        {"q": tr("If D = 0 in Cramer's rule, what can you say?"),
         "a": tr("Either there is no solution (parallel lines) or there are infinitely many (the same line); Dx "
                 "and Dy decide which.")},
        {"q": tr("How do you test whether three points are collinear?"),
         "a": tr("The area formula must give zero, that is the determinant of the three points is zero.")},
    ]},
    {"title": tr("Functions"), "items": [
        {"q": tr("Define a function."),
         "a": tr("A rule that assigns exactly one element of the codomain to every element of the domain.")},
        {"q": tr("What is the domain of 1/(x − 3)?"),
         "a": tr("All real numbers except 3, because the denominator must not be zero.")},
        {"q": tr("What is the domain of √(x − 2)?"),
         "a": tr("x ≥ 2, because a square root of a negative number is not real.")},
        {"q": tr("When is a function even?"),
         "a": tr("When f(−x) = f(x) for every x in the domain; its graph is symmetric about the y-axis.")},
        {"q": tr("When is a function odd?"),
         "a": tr("When f(−x) = −f(x) for every x; its graph is symmetric about the origin.")},
        {"q": tr("What is the range of a quadratic with a positive leading coefficient?"),
         "a": tr("From the vertex's y-value upward, y ≥ k, because the parabola opens upward.")},
        {"q": tr("What does the vertical line test check?"),
         "a": tr("That no vertical line meets the graph twice, which means each input has only one output.")},
    ]},
    {"title": tr("Logarithms"), "items": [
        {"q": tr("Define logₐ x."),
         "a": tr("The exponent to which a must be raised to get x: y = logₐ x ⇔ aʸ = x.")},
        {"q": tr("What is the domain of a logarithm?"),
         "a": tr("x > 0, because no power of a positive base gives zero or a negative number.")},
        {"q": tr("State the product law."),
         "a": tr("logₐ(xy) = logₐ x + logₐ y.")},
        {"q": tr("State the quotient law."),
         "a": tr("logₐ(x/y) = logₐ x − logₐ y.")},
        {"q": tr("State the power law."),
         "a": tr("logₐ(xⁿ) = n logₐ x.")},
        {"q": tr("How do you change the base of a logarithm?"),
         "a": tr("logₐ x = log_b x / log_b a, for any valid new base b.")},
        {"q": tr("What are logₐ 1 and logₐ a?"),
         "a": tr("logₐ 1 = 0 and logₐ a = 1, for every valid base a.")},
        {"q": tr("Is log(x + y) equal to log x + log y?"),
         "a": tr("No. The product law applies to log(xy); a sum inside a logarithm cannot be split.")},
        {"q": tr("Why is a 20 dB increase a hundredfold, not a doubling?"),
         "a": tr("Sound level uses 10 log₁₀; +20 dB means the ratio grew by 10² = 100.")},
    ]},
]

PRACTICE = [
    ("Evaluate |5 −2; 3 4|.", 3,
     h4("Working") + ol("Main diagonal: 5 × 4 = 20", "Other diagonal: (−2) × 3 = −6",
                        "20 − (−6) = 26")
     + h4("Answer") + p("<b>26.</b> Subtracting a negative product adds: keep the sign of b with b when you "
                        "multiply.")),
    ("Find x if |x 3; 4 x| = 12.", 4,
     h4("Working") + ol("x² − 12 = 12", "x² = 24", "x = √24 = 2√6 ≈ 4.899 or x = −2√6")
     + h4("Answer") + p("<b>x = ±2√6.</b> Both roots satisfy the determinant; leave the answer in surd form "
                        "unless decimals are asked for.")),
    ("Evaluate |3 1 2; 0 4 1; 2 0 5| by expanding along the first column.", 4,
     h4("Working") + ol("3 × (4×5 − 1×0) = 60", "−0 × (…) = 0", "+2 × (1×1 − 2×4) = 2 × (−7) = −14",
                        "60 + 0 − 14 = 46")
     + h4("Check") + p("Expanding along the first row: 3(20 − 0) − 1(0 − 2) + 2(0 − 8) = 60 + 2 − 16 = 46 ✓ - "
                       "the value does not depend on the chosen line.")),
    ("Find the cofactor of the entry 4 in [1 2 3; 4 5 6; 7 8 9].", 3,
     h4("Working") + p("Position (2, 1) carries a minus sign. Delete row 2 and column 1: the minor is "
                       "|2 3; 8 9| = 18 − 24 = −6. Cofactor = −(−6) = 6.")
     + h4("Answer") + p("<b>6.</b> Note the determinant of the whole matrix is 0 (row 3 = 2 × row 2 − row 1), "
                        "which does not stop a single cofactor from being non-zero.")),
    ("Solve 3x + 2y = 16, x + y = 6 by Cramer's rule.", 4,
     h4("Working") + ol("D = 3(1) − 2(1) = 1", "Dx = 16(1) − 2(6) = 4 → x = 4",
                        "Dy = 3(6) − 16(1) = 2 → y = 2")
     + h4("Check") + p("3(4) + 2(2) = 16 ✓ and 4 + 2 = 6 ✓. D = 1 makes the division exact, which is a good sign "
                       "that the coefficients were copied correctly.")),
    ("Find the area of the triangle (0, 0), (5, 0), (0, 4).", 3,
     h4("Working") + p("Area = ½|0(0 − 4) + 5(4 − 0) + 0(0 − 0)| = ½|20| = 10.")
     + h4("Answer") + p("<b>10 square units</b> - the familiar right triangle with legs 5 and 4, so ½ × 5 × 4 = "
                        "10 confirms it.")),
    ("For f(x) = x² + 2x find f(−3) and f(1/2).", 3,
     h4("Working") + ol("f(−3) = 9 − 6 = 3", "f(1/2) = 1/4 + 1 = 5/4")
     + h4("Answer") + p("<b>3 and 5/4.</b> Bracket every substituted value, especially a fraction: (1/2)² = 1/4, "
                        "not 1/2.")),
    ("Find the domain and range of f(x) = √(4 − x).", 4,
     h4("Working") + ol("4 − x ≥ 0 → x ≤ 4, so the domain is (−∞, 4]",
                        "A principal square root is never negative and reaches 0 at x = 4",
                        "Range = [0, ∞)")
     + h4("Check") + p("f(4) = 0 and f(0) = 2: outputs start at 0 and grow without limit as x becomes very "
                       "negative ✓.")),
    ("Is f(x) = x⁴ + 2x² even, odd or neither?", 3,
     h4("Working") + p("f(−x) = (−x)⁴ + 2(−x)² = x⁴ + 2x² = f(x), so the function is even.")
     + h4("Answer") + p("<b>Even.</b> Every power of x is even, and that is a quick rule: a polynomial with only "
                        "even powers is even, only odd powers is odd, mixed is neither.")),
    ("Evaluate log₃ 81 and log₇ (1/49).", 3,
     h4("Working") + ol("3⁴ = 81 → log₃ 81 = 4", "7⁻² = 1/49 → log₇ (1/49) = −2")
     + h4("Answer") + p("<b>4 and −2.</b> A fraction smaller than 1 always gives a negative log (base > 1).")),
    ("Expand log(5x³/y²).", 3,
     h4("Working") + p("log(5x³) − log(y²) = log 5 + log x³ − log y² = log 5 + 3 log x − 2 log y.")
     + h4("Answer") + p("<b>log 5 + 3 log x − 2 log y.</b> Check by condensing: the terms rebuild "
                        "log(5x³/y²) exactly.")),
    ("Simplify log 8 + log 125 − log 10.", 4,
     h4("Working") + ol("log 8 + log 125 = log 1000", "log 1000 − log 10 = log 100", "log 100 = 2")
     + h4("Answer") + p("<b>2.</b> A calculator confirms 0.903 + 2.097 − 1 = 2.000 ✓.")),
    ("Solve log₂(x − 1) = 3.", 3,
     h4("Working") + ol("Domain first: x − 1 > 0, so x > 1", "Convert to exponential form: x − 1 = 2³ = 8",
                        "x = 9")
     + h4("Check") + p("log₂(9 − 1) = log₂ 8 = 3 ✓, and 9 satisfies x > 1. The domain condition is not "
                        "decoration: without it a computed root such as x = 0 would be accepted wrongly.")),
    ("A sound is 1000 times more intense than the threshold I₀. Find its level in dB.", 4,
     h4("Working") + ol("L = 10 log₁₀(I/I₀)", "= 10 log₁₀ 1000", "= 10 × 3 = 30")
     + h4("Answer") + p("<b>30 dB.</b> Each factor of 10 adds 10 dB, so a 1000-fold intensity is 3 × 10 dB - "
                        "never 1000 dB.")),
]

ANSWERED = {"title": tr("7. Answered Practice (Unit 1 level, suggested marks)"),
            "items": [{"h": tr(f"Practice {i}. {q}"), "body": tr(a)} for i, (q, _m, a) in enumerate(PRACTICE, 1)]}
NOTES[-1] = ANSWERED
EXAM = [{"q": tr("Practice: " + q), "marks": m} for q, m, _ in PRACTICE]
LESSON_COUNT = sum(len(s["items"]) for s in NOTES) - len(ANSWERED["items"])
