"""DI01000021 Mathematics-I - Unit 0: "Start Mathematics From Zero" (DiplomaOne foundation chapter).

Not part of the official GTU syllabus (hours 0, weightage 0). It rebuilds exactly the prerequisites the
syllabus itself lists - fractions, LCM/GCD, factorisation, quadratics, coordinate geometry, sets - with
worked examples and twenty solved numericals.
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
    ("Khan Academy - arithmetic, algebra basics and quadratics",
     "https://www.khanacademy.org/math/algebra"),
    ("GeoGebra - plot functions, lines and circles to check your answers",
     "https://www.geogebra.org/"),
    ("OpenStax - Elementary Algebra 2e (free textbook)",
     "https://openstax.org/details/books/elementary-algebra-2e"),
    ("NCERT - Class 10 Mathematics textbook (fractions, polynomials, coordinate geometry)",
     "https://ncert.nic.in/textbook.php"),
]

NOTES = [
    {"title": tr("1. Numbers, Signs and Fractions"),
     "items": [
         card("1.1 The number line and the families of numbers",
              h4("Definition")
              + p("Every number you will use this semester sits on one line. Moving right adds, moving left "
                  "subtracts, and the distance from zero is the <b>absolute value</b> |x|.")
              + h4("The families, from smallest to largest")
              + table(["Family", "Symbol", "Examples", "What it adds"],
                      [("Natural", "N", "1, 2, 3, …", "Counting"),
                       ("Whole", "W", "0, 1, 2, 3, …", "Zero"),
                       ("Integers", "Z", "…, −2, −1, 0, 1, 2, …", "Negative direction"),
                       ("Rational", "Q", "3/4, −2.5, 0.333…", "Every fraction of integers"),
                       ("Irrational", "R − Q", "√2, π, e", "Cannot be written as a fraction"),
                       ("Real", "R", "All of the above", "Every point on the line")])
              + h4("Rules you will use daily")
              + ul("|−7| = 7 and |7| = 7: absolute value removes the sign.",
                   "On the line, −5 < −2 because −5 lies to the left.",
                   "A rational number has a terminating or repeating decimal; √2 = 1.41421… never repeats.",
                   "Between any two rational numbers there is another rational number - the line is dense, "
                   "which is why graphs look continuous.")
              + sc("Is 0.75 rational?", "Yes: 0.75 = 3/4, a fraction of integers."),
              "m0_numberline", syllabus_item="foundation:1"),
         card("1.2 Sign rules for integers",
              h4("Definition")
              + p("Two signs next to each other combine into one: <b>same signs give +, different signs give "
                  "−</b>. Then apply the operation.")
              + h4("Explanation and application")
              + table(["Expression", "Combine", "Result"],
                      [("(−3) + (+7) − (−2)", "−3 + 7 + 2", "6"),
                       ("(−8) − (−5)", "−8 + 5", "−3"),
                       ("(−4) × (−3)", "same signs → positive", "12"),
                       ("(−12) ÷ (+4)", "different signs → negative", "−3"),
                       ("−2² vs (−2)²", "−2² = −(2×2); (−2)² = (−2)(−2)", "−4 vs 4")])
              + h4("Common mistake / conditions")
              + p("The last row decides many exam marks: <b>−2² = −4</b> because the power applies to 2 only, "
                  "while <b>(−2)² = 4</b> because the bracket carries the sign. Write brackets when you mean them."),
              examples=["m0n1"], syllabus_item="foundation:1"),
         card("1.3 Fractions: simplify, add, multiply, divide",
              h4("Definition")
              + p("A fraction a/b means a parts out of b equal parts. It is simplified when no number except 1 "
                  "divides both a and b.")
              + h4("The four operations")
              + ol("<b>Simplify:</b> divide top and bottom by their GCD. 18/24 → 3/4.",
                   "<b>Add or subtract:</b> take the LCM of the denominators, rewrite both fractions, then add "
                   "the numerators: 5/6 + 3/4 = 10/12 + 9/12 = 19/12.",
                   "<b>Multiply:</b> multiply tops and bottoms, then simplify: 5/6 × 9/10 = 45/60 = 3/4.",
                   "<b>Divide:</b> flip the second fraction and multiply: 2/3 ÷ 4/9 = 2/3 × 9/4 = 18/12 = 3/2.")
              + h4("Common mistake / conditions")
              + p("Denominators are never added: 5/6 + 3/4 is not 8/10. If the answer is bigger than 1, give it "
                  "as a mixed number too - 19/12 = 1 7/12 - because that is how marks are usually written."),
              examples=["m0n2", "m0n3"], syllabus_item="foundation:1"),
         card("1.4 GCD and LCM by prime factorisation",
              h4("Definition")
              + p("<b>GCD</b> (HCF) is the largest number dividing both; <b>LCM</b> is the smallest number both "
                  "divide. Prime factorisation gives both in one step.")
              + h4("Method")
              + ol("Write each number as a product of primes: 48 = 2⁴ × 3 and 180 = 2² × 3² × 5.",
                   "For the GCD take the <b>common primes with the smallest</b> powers: 2² × 3 = 12.",
                   "For the LCM take <b>every prime with the largest</b> power: 2⁴ × 3² × 5 = 720.",
                   "Check with GCD × LCM = product: 12 × 720 = 8640 = 48 × 180. ✓")
              + h4("Where it is used")
              + p("Adding fractions (LCM of denominators), simplifying ratios, timing problems (two bells ring "
                  "together again after the LCM of their intervals) and factorising algebraic expressions "
                  "(GCD of coefficients)."),
              examples=["m0n4"], syllabus_item="foundation:1"),
         card("1.5 Decimals, percentages and averages",
              h4("Definition")
              + p("A percentage is a fraction with denominator 100: 75 % = 75/100 = 0.75 = 3/4. An average "
                  "(mean) divides a total equally among the count.")
              + h4("Three conversions you must do without thinking")
              + ul("Fraction → decimal: divide top by bottom (3/8 = 0.375).",
                   "Decimal → percentage: multiply by 100 (0.375 = 37.5 %).",
                   "Percentage → fraction: put over 100 and simplify (36 % = 9/25).")
              + h4("Application")
              + p("15 % of 240 = 0.15 × 240 = 36. Increasing 240 by 15 % gives 240 + 36 = 276, which is the same "
                  "as 240 × 1.15. Averages are used for internal marks and for reading graphs: the mean of "
                  "62, 78, 85 and 55 is 280/4 = 70."),
              examples=["m0n5"], syllabus_item="foundation:1")]},

    {"title": tr("2. Order of Operations, Powers and Roots"),
     "items": [
         card("2.1 BODMAS: the only order that gives one answer",
              h4("Definition")
              + p("An expression with several operations is evaluated in a fixed order: <b>B</b>rackets, "
                  "<b>O</b>rders (powers and roots), <b>D</b>ivision and <b>M</b>ultiplication (left to right), "
                  "<b>A</b>ddition and <b>S</b>ubtraction (left to right).")
              + h4("Worked example")
              + p("8 + 2 × (5 − 3)² = 8 + 2 × 2² = 8 + 2 × 4 = 8 + 8 = <b>16</b>. Brackets first, then the "
                  "power, then multiplication, then addition.")
              + h4("Common mistake / conditions")
              + p("2 + 3 × 4 is <b>14</b>, not 20: multiplication is done before addition. Similarly 12 ÷ 3 × 2 "
                  "is <b>8</b>, because division and multiplication are evaluated left to right - not 12 ÷ 6."),
              "m0_bodmas", examples=["m0n6"], syllabus_item="foundation:2"),
         card("2.2 Laws of indices",
              h4("Definition")
              + p("An index counts repeated multiplication: aⁿ = a × a × … (n times). The laws follow from that "
                  "definition, so they never need to be memorised blindly.")
              + h4("The five laws")
              + table(["Law", "Example", "Reason"],
                      [("aᵐ × aⁿ = aᵐ⁺ⁿ", "2³ × 2⁴ = 2⁷", "count the factors"),
                       ("aᵐ ÷ aⁿ = aᵐ⁻ⁿ", "2⁵ ÷ 2² = 2³", "cancel common factors"),
                       ("(aᵐ)ⁿ = aᵐⁿ", "(2³)² = 2⁶", "three factors, repeated twice"),
                       ("a⁰ = 1 (a ≠ 0)", "7⁰ = 1", "aⁿ ÷ aⁿ = 1"),
                       ("a⁻ⁿ = 1/aⁿ", "2⁻³ = 1/8", "negative index means reciprocal")])
              + h4("Application")
              + p("In electronics, 10⁻⁶ means micro and 10³ means kilo; in units, m/s = m·s⁻¹. A fractional "
                  "index is a root: a^(1/2) = √a and a^(2/3) = ∛(a²)."),
              examples=["m0n7"], syllabus_item="foundation:2"),
         card("2.3 Roots and surds",
              h4("Definition")
              + p("√a is the positive number whose square is a. A <b>surd</b> is a root that cannot be simplified "
                  "to a whole number, such as √2 or 3√5.")
              + h4("Simplifying a surd")
              + ol("Factor out the largest perfect square: √72 = √(36 × 2) = 6√2.",
                   "Only like surds combine: √72 − √18 = 6√2 − 3√2 = 3√2 ≈ 4.243.",
                   "Rationalise a denominator by multiplying top and bottom by the surd: "
                   "1/√2 = √2/2 ≈ 0.707.")
              + h4("Common mistake / conditions")
              + p("√(a + b) is not √a + √b. For a = 9 and b = 16, √25 = 5 but 3 + 4 = 7. Check any rule with "
                  "numbers before using it in an exam."),
              examples=["m0n8"], syllabus_item="foundation:2"),
         card("2.4 Standard form (scientific notation)",
              h4("Definition")
              + p("A number is in standard form when it is written as <b>a × 10ⁿ</b> with 1 ≤ a < 10. It keeps "
                  "very large and very small engineering quantities readable.")
              + h4("Rules")
              + ul("Multiply: multiply the front numbers, add the powers - (3.6 × 10⁴)(2.5 × 10³) = 9.0 × 10⁷.",
                   "Divide: divide the front numbers, subtract the powers.",
                   "Add or subtract: make the powers equal first, then add - 3.6 × 10⁴ + 2.5 × 10³ = "
                   "36,000 + 2,500 = 38,500.",
                   "Move the decimal point right → smaller power; left → larger power.")
              + p("A calculator display of 4.2E−3 means 4.2 × 10⁻³ = 0.0042, not 4200."),
              examples=["m0n9"], syllabus_item="foundation:2")]},

    {"title": tr("3. Algebra: Expressions, Expansion and Factorisation"),
     "items": [
         card("3.1 Terms, coefficients and substitution",
              h4("Definition")
              + p("In 5x² − 3x + 7 the parts 5x², −3x and 7 are <b>terms</b>; 5 and −3 are <b>coefficients</b>; "
                  "7 is the constant. Only <b>like terms</b> (same letter, same power) may be combined.")
              + p("Such a sum of terms with whole-number powers is a <b>polynomial</b>. Its highest power is the "
                  "<b>degree</b> - 2 here, so it is a quadratic - and the degree tells you how many solutions "
                  "the related equation can have: one for a linear polynomial, up to two for a quadratic, "
                  "three for a cubic.")
              + h4("Explanation and application")
              + ul("3x + 5x = 8x, but 3x + 5x² cannot be simplified - different powers.",
                   "Multiply powers by adding indices: x² · x³ = x⁵.",
                   "Substitution means replacing the letter by a number in brackets: 2x² − 3x + 1 at x = −2 is "
                   "2(−2)² − 3(−2) + 1 = 8 + 6 + 1 = 15.")
              + h4("Common mistake / conditions")
              + p("Always put a negative value in brackets before substituting. Squaring without brackets gives "
                  "−4 instead of 4 and the whole answer is wrong."),
              examples=["m0n10"], syllabus_item="foundation:3"),
         card("3.2 Expansion and the three identities",
              h4("Definition")
              + p("Expanding means multiplying every term of one bracket by every term of the other. Three "
                  "patterns appear so often that they are worth knowing by sight.")
              + h4("The identities")
              + table(["Identity", "Expanded form", "Typical use"],
                      [("(a + b)²", "a² + 2ab + b²", "(x + 4)² = x² + 8x + 16"),
                       ("(a − b)²", "a² − 2ab + b²", "(2a − 3b)² = 4a² − 12ab + 9b²"),
                       ("(a + b)(a − b)", "a² − b²", "(x + 5)(x − 5) = x² − 25")])
              + h4("General expansion")
              + p("(x + 3)(x − 5) = x² − 5x + 3x − 15 = <b>x² − 2x − 15</b>. The middle term is the sum of the "
                  "cross products; that is why the sign matters.")
              + h4("Common mistake / conditions")
              + p("(a + b)² is not a² + b². The middle term 2ab is the most frequently forgotten term in the "
                  "paper."),
              "m0_factor", examples=["m0n11"], syllabus_item="foundation:3"),
         card("3.3 Factorisation: the reverse of expansion",
              h4("Definition")
              + p("Factorising writes a sum as a product. Always try the steps in this order.")
              + h4("Four-step checklist")
              + ol("<b>Common factor:</b> 6x² + 9x = 3x(2x + 3).",
                   "<b>Difference of squares:</b> 4x² − 25 = (2x − 5)(2x + 5).",
                   "<b>Quadratic trinomial:</b> find two numbers whose product is c and sum is b. "
                   "x² − 7x + 12 → −3 and −4 → (x − 3)(x − 4).",
                   "<b>Check by expanding:</b> (x − 3)(x − 4) = x² − 7x + 12 ✓ - this check takes ten seconds and "
                   "saves the whole question.")
              + h4("When the leading coefficient is not 1")
              + p("For 2x² + 7x − 15, multiply 2 × (−15) = −30; find 10 and −3 (product −30, sum 7); split the "
                  "middle term and group: 2x² + 10x − 3x − 15 = 2x(x + 5) − 3(x + 5) = (x + 5)(2x − 3)."),
              examples=["m0n12"], syllabus_item="foundation:3"),
         card("3.4 Which tool for which expression?",
              h4("Definition")
              + p("Choosing the right first move is most of the work in algebra. Use this decision table before "
                  "writing anything.")
              + h4("Decision table")
              + table(["Expression looks like", "First move"],
                      [("Every term shares a factor", "Take the common factor out"),
                       ("Two squares with a minus between", "a² − b² = (a + b)(a − b)"),
                       ("ax² + bx + c with a = 1", "Two numbers with product c, sum b"),
                       ("ax² + bx + c with a ≠ 1", "Split the middle term, then group"),
                       ("Fraction with a common factor on top and bottom", "Factorise both, then cancel")])
              + h4("Why it matters later")
              + p("Quadratic equations in Section 5, limits in Unit 5 and partial fractions in later semesters all "
                  "begin with factorisation. A student who cannot factorise loses marks across the paper, not "
                  "only in one question."),
              syllabus_item="foundation:3")]},

    {"title": tr("4. Linear Equations and Simultaneous Equations"),
     "items": [
         card("4.1 One variable: transposition",
              h4("Definition")
              + p("An equation is a balance. Whatever you do to one side you must do to the other, which is why "
                  "moving a term across the equals sign changes its sign.")
              + h4("Worked example")
              + p("3(x − 2) = 2x + 5 → 3x − 6 = 2x + 5 → 3x − 2x = 5 + 6 → <b>x = 11</b>.")
              + h4("The safe procedure")
              + ol("Remove brackets.",
                   "Collect the letter terms on one side and numbers on the other.",
                   "Divide by the coefficient of the letter.",
                   "Substitute the answer back into the original equation - both sides must agree.")
              + h4("Common mistake / conditions")
              + p("Do not divide by a variable that could be zero, and never drop a minus sign while moving a "
                  "term. The check step is not optional: 3(11 − 2) = 27 and 2(11) + 5 = 27 ✓."),
              examples=["m0n13"], syllabus_item="foundation:4"),
         card("4.2 Turning a word problem into an equation",
              h4("Definition")
              + p("Every word problem is a translation exercise: name the unknown, write the relation, solve, "
                  "then answer the question that was asked.")
              + h4("Pattern: sum and difference")
              + p("Two numbers add to 45 and differ by 9. Let them be x and x + 9 (because the difference is "
                  "fixed). Then x + (x + 9) = 45 → 2x = 36 → x = 18, so the numbers are <b>18 and 27</b>.")
              + h4("Pattern: ages, speeds, mixtures")
              + ul("Age problem: write both ages now, then add the same number of years to both.",
                   "Speed problem: distance = speed × time; keep the units consistent.",
                   "Mixture problem: track the amount of the substance, not only the volume.")
              + h4("Condition")
              + p("State what the letter means before solving. \"Let x be the number of pens\" prevents the "
                  "common error of finding a number and then reporting the wrong quantity."),
              examples=["m0n15"], syllabus_item="foundation:4"),
         card("4.3 Two variables: elimination and substitution",
              h4("Definition")
              + p("A linear equation in two variables, such as 2x + 3y = 12, has infinitely many solutions on "
                  "its own; two such equations are needed for two unknowns. <b>Elimination</b> removes one "
                  "variable by adding or subtracting multiples of the equations; <b>substitution</b> replaces "
                  "one variable using the other equation.")
              + h4("Worked example (substitution)")
              + p("2x + 3y = 12 and x − y = 1. From the second, x = y + 1. Substitute: 2(y + 1) + 3y = 12 → "
                  "5y = 10 → y = 2, x = 3. Check: 2(3) + 3(2) = 12 ✓.")
              + h4("Worked example (elimination)")
              + p("3p + 2q = 80 and 2p + 3q = 70. Multiply the first by 3 and the second by 2: 9p + 6q = 240 and "
                  "4p + 6q = 140. Subtract: 5p = 100 → p = 20, then q = 10.")
              + h4("Which to choose")
              + p("Use substitution when one equation already gives a variable (x = …). Use elimination when both "
                  "equations look alike - multiply to match the coefficients, then subtract."),
              examples=["m0n14"], syllabus_item="foundation:4"),
         card("4.4 Checking, and what no solution means",
              h4("Definition")
              + p("A pair of linear equations can meet once, never, or everywhere. The graph is two straight "
                  "lines, and their relationship tells you the answer before you solve anything.")
              + h4("Three cases")
              + table(["Case", "Graph", "Algebraic sign", "Answer"],
                      [("One solution", "Lines cross once", "Different slopes", "Unique (x, y)"),
                       ("No solution", "Parallel lines", "Same slope, different intercept", "Inconsistent"),
                       ("Infinite solutions", "Same line", "One equation is a multiple of the other",
                        "Infinitely many")])
              + h4("Check routine")
              + ol("Substitute the pair into <b>both</b> original equations.",
                   "Confirm the units and answer the question in words.",
                   "If a substitution fails, the algebra - not the method - is wrong; solve again slowly.")
              + p("In the pens example, 3(20) + 2(10) = 80 and 2(20) + 3(10) = 70, so a pen is ₹20 and a pencil "
                  "₹10."),
              examples=["m0n15"], syllabus_item="foundation:4")]},

    {"title": tr("5. Quadratic Equations"),
     "items": [
         card("5.1 Standard form and the three methods",
              h4("Definition")
              + p("A quadratic equation has the form <b>ax² + bx + c = 0</b> with a ≠ 0. It can have two, one or "
                  "no real solutions, and its graph is a parabola.")
              + h4("Three methods")
              + table(["Method", "Use it when", "Speed"],
                      [("Factorisation", "The factors are obvious integers", "Fastest, no calculator"),
                       ("Quadratic formula", "Always", "Never fails; needs care with signs"),
                       ("Completing the square", "You need the vertex or a proof", "Slow, shows the structure")])
              + h4("Before choosing")
              + p("Write the equation in standard form first. 3x(x − 2) = 15 must become 3x² − 6x − 15 = 0 (or "
                  "x² − 2x − 5 = 0) before any method is applied."),
              syllabus_item="foundation:5"),
         card("5.2 Factorisation method",
              h4("Definition")
              + p("If two factors multiply to zero, at least one of them is zero. That single idea turns a "
                  "quadratic into two linear equations.")
              + h4("Worked examples")
              + p("x² − 5x + 6 = 0 → (x − 2)(x − 3) = 0 → <b>x = 2 or x = 3</b>.")
              + p("2x² + 7x − 15 = 0 → (2x − 3)(x + 5) = 0 → <b>x = 3/2 or x = −5</b>.")
              + h4("Procedure for a ≠ 1")
              + ol("Multiply a and c: 2 × (−15) = −30.",
                   "Find two numbers with product −30 and sum 7: 10 and −3.",
                   "Split the middle term, group and factorise.",
                   "Set each bracket to zero and solve.")
              + h4("Common mistake / conditions")
              + p("(2x − 3) = 0 gives x = 3/2, not 3. Divide by the coefficient of x inside the bracket, and "
                  "check both roots in the original equation."),
              "m0_parabola", examples=["m0n12"], syllabus_item="foundation:5"),
         card("5.3 The quadratic formula and the discriminant",
              h4("Formula")
              + p("For ax² + bx + c = 0, <b>x = (−b ± √(b² − 4ac)) / 2a</b>, and D = b² − 4ac is the "
                  "<b>discriminant</b>.")
              + h4("What D tells you before you finish")
              + table(["D", "Roots", "Graph"],
                      [("D > 0", "Two distinct real roots", "Parabola cuts the x-axis twice"),
                       ("D = 0", "One repeated root, x = −b/2a", "Parabola touches the x-axis"),
                       ("D < 0", "No real roots", "Parabola stays above or below the axis")])
              + h4("Worked example")
              + p("3x² − 4x + 5 = 0: D = (−4)² − 4(3)(5) = 16 − 60 = <b>−44</b>. D < 0, so there is no real "
                  "solution - do not force the formula and invent a root.")
              + h4("Check with the sum and product")
              + p("The roots satisfy x₁ + x₂ = −b/a and x₁x₂ = c/a. For 2x² + 7x − 15: sum = −7/2 = 1.5 + (−5) ✓ "
                  "and product = −15/2 = 1.5 × (−5) ✓."),
              "m0_parabola", examples=["m0n16"], syllabus_item="foundation:5"),
         card("5.4 Word problems that become quadratic",
              h4("Definition")
              + p("Any situation with an area, a product, or a squared unknown produces a quadratic. The "
                  "physical meaning then decides which root to keep.")
              + h4("Worked example")
              + p("A rectangle is 5 m longer than it is wide and its area is 84 m². Let the width be w; then "
                  "w(w + 5) = 84 → w² + 5w − 84 = 0 → (w + 12)(w − 7) = 0 → w = 7 or w = −12.")
              + h4("Choosing the root")
              + p("A length cannot be negative, so w = −12 is rejected. Width = <b>7 m</b>, length = <b>12 m</b>, "
                  "and 7 × 12 = 84 ✓. Always state the rejected root and why."),
              examples=["m0n17"], syllabus_item="foundation:5")]},

    {"title": tr("6. Sets, Ratio, Percentage and Average"),
     "items": [
         card("6.1 Sets and the three operations",
              h4("Definition")
              + p("A set is a collection of distinct objects. If A = {1, 2, 3, 4} and B = {3, 4, 5}, then the "
                  "three operations give:")
              + table(["Operation", "Meaning", "Answer for A and B", "Count"],
                      [("A ∪ B (union)", "Everything in A or B", "{1, 2, 3, 4, 5}", "5"),
                       ("A ∩ B (intersection)", "Only what is in both", "{3, 4}", "2"),
                       ("A − B (difference)", "In A but not in B", "{1, 2}", "2")])
              + h4("Why it is in the prerequisite list")
              + p("Domain and range in Unit 1, solution sets of inequalities, and probability in later "
                  "semesters are all written in set notation. The counting rule n(A ∪ B) = n(A) + n(B) − "
                  "n(A ∩ B) explains double counting: 4 + 3 − 2 = 5 ✓."),
              examples=["m0n21"], syllabus_item="foundation:6"),
         card("6.2 Ratio and proportion",
              h4("Definition")
              + p("A ratio compares parts of the same whole; a proportion says two ratios are equal (a : b = "
                  "c : d, so ad = bc).")
              + h4("Dividing an amount in a ratio")
              + ol("Add the ratio parts: 2 + 3 + 4 = 9.",
                   "One part = total / 9 = 4500 / 9 = 500.",
                   "Multiply: 2 × 500 = 1000, 3 × 500 = 1500, 4 × 500 = 2000.",
                   "Check: 1000 + 1500 + 2000 = 4500 ✓.")
              + h4("Application")
              + p("Mixing concrete 1 : 2 : 4, dividing profit between partners, scaling a map or a drawing, and "
                  "resolving a force into components all use the same arithmetic."),
              examples=["m0n18"], syllabus_item="foundation:6"),
         card("6.3 Percentage change and reverse percentage",
              h4("Definition")
              + p("Percentage change compares the change with the <b>original</b> value: change % = "
                  "(new − old)/old × 100.")
              + h4("Worked examples")
              + ul("Price 800 → 920: change = +120, so 120/800 × 100 = <b>+15 %</b>.",
                   "Price 920 → 800: change = −120, and the original is now 920, so 120/920 × 100 = "
                   "<b>−13.04 %</b>.",
                   "A 15 % rise followed by a 15 % fall does not return to the start: 800 × 1.15 × 0.85 = 782.")
              + h4("Common mistake / conditions")
              + p("Always divide by the value <b>before</b> the change, and remember that successive percentages "
                  "multiply. The GST-style question \"price before tax\" is a reverse percentage: divide by "
                  "(1 + rate), do not subtract the rate from the final price."),
              examples=["m0n19"], syllabus_item="foundation:6"),
         card("6.4 Average, and when it misleads",
              h4("Definition")
              + p("Mean = sum of values / number of values. It is the balance point of the data, and the only "
                  "average you need this semester.")
              + h4("Worked example")
              + p("Marks 62, 78, 85, 55: sum = 280, count = 4, mean = <b>70</b>. If the next test is 90, the new "
                  "mean is 370/5 = 74 - one high score lifts the average by 4 marks.")
              + h4("Limitation")
              + p("A single extreme value pulls the mean. The median (middle value when sorted) is safer for "
                  "salaries or house prices. State which average you used and why."),
              examples=["m0n22"], syllabus_item="foundation:6")]},

    {"title": tr("7. The Coordinate Plane"),
     "items": [
         card("7.1 Axes, quadrants and plotting a point",
              h4("Definition")
              + p("Two perpendicular number lines give every point a unique address (x, y): x is measured along "
                  "the horizontal axis, y along the vertical axis.")
              + h4("The four quadrants")
              + table(["Quadrant", "x", "y", "Example"],
                      [("I", "positive", "positive", "(3, 2)"),
                       ("II", "negative", "positive", "(−4, 3)"),
                       ("III", "negative", "negative", "(−2, −5)"),
                       ("IV", "positive", "negative", "(6, −1)")])
              + h4("Rules")
              + ul("A point on the x-axis has y = 0; on the y-axis x = 0; the origin is (0, 0).",
                   "Plot by counting along x first, then along y - in that order.",
                   "Always write the bracket and the comma; (3, 2) and (2, 3) are different points.")
              + p("This section is the bridge to Unit 4: distance, midpoint and slope are all measured on this "
                  "grid."),
              "m0_quadrants", syllabus_item="foundation:7"),
         card("7.2 Distance between two points",
              h4("Formula")
              + p("For A(x₁, y₁) and B(x₂, y₂): <b>AB = √((x₂ − x₁)² + (y₂ − y₁)²)</b> - Pythagoras on the "
                  "horizontal and vertical gaps.")
              + h4("Worked example")
              + p("A(2, 3) and B(6, 6): gaps are 4 and 3, so AB = √(16 + 9) = √25 = <b>5 units</b>.")
              + h4("Checks that catch errors")
              + ul("Distance is never negative; a negative answer means a sign slip.",
                   "Order does not matter, because both gaps are squared.",
                   "If the points share an x or a y, the distance is simply the other gap.")
              + h4("Application")
              + p("Length of a side of a plot, distance between two machines on a layout, error between a "
                  "measured point and a nominal point."),
              examples=["m0n20"], syllabus_item="foundation:7"),
         card("7.3 Midpoint and slope",
              h4("Formulae")
              + p("Midpoint M = ((x₁ + x₂)/2, (y₁ + y₂)/2). Slope m = (y₂ − y₁)/(x₂ − x₁) = rise / run.")
              + h4("Worked example")
              + p("A(2, 3) and B(6, 6): midpoint = (4, 4.5) and slope = (6 − 3)/(6 − 2) = 3/4 = 0.75. A line "
                  "rising 3 units for every 4 to the right.")
              + h4("Reading the slope")
              + table(["Slope", "Meaning"],
                      [("positive", "line rises left to right"),
                       ("negative", "line falls left to right"),
                       ("zero", "horizontal line"),
                       ("undefined", "vertical line (x₂ = x₁)")])
              + p("Slope is the first thing Unit 4 asks for: it appears in the two-point form, the slope-point "
                  "form, the parallel and perpendicular conditions, and the tangent to a circle."),
              examples=["m0n20"], syllabus_item="foundation:7")]},

    {"title": tr("8. How to Study Mathematics: The Five-Step Method"),
     "items": [
         card("8.1 The five steps",
              h4("The method")
              + p("Mathematics is learnt by <b>doing</b>, not by reading. Use the same five steps for every topic "
                  "in this subject.")
              + ol("<b>Read a solved example</b> with a pen in hand: cover the solution, predict the next line, "
                   "then check.",
                   "<b>Copy it closed-book</b> immediately, then compare line by line. Any line you cannot "
                   "reproduce is the line you did not understand.",
                   "<b>Change the numbers</b> and solve the same skeleton again - same method, your values.",
                   "<b>Attempt an unsolved problem</b> and write every step, even the wrong ones.",
                   "<b>Log the error</b> in one line (\"moved −3 without changing sign\") and revise it after 1 "
                   "day, 1 week and 1 month.")
              + h4("Why it works")
              + p("Steps 1-2 build recognition, step 3 builds transfer, step 4 exposes gaps, and step 5 stops the "
                  "same mistake from returning in the exam."),
              "m0_cycle", syllabus_item="foundation:8"),
         card("8.2 A weekly routine that fits a diploma timetable",
              h4("The plan")
              + ul("<b>20 minutes daily:</b> one numerical from the current unit, written fully.",
                   "<b>Twice a week:</b> five viva answers spoken aloud - speaking exposes fake understanding.",
                   "<b>Once a week:</b> one timed 12-mark set from the Exam tab, closed book.",
                   "<b>Before a test:</b> re-solve only the questions in your error log, not the whole chapter.")
              + h4("How to use this app")
              + ol("Open the unit, read a card, then close it and say the definition aloud.",
                   "Open the gold <b>EX</b> box only after trying the numerical yourself.",
                   "Use <b>Viva</b> for one-line answers and <b>Exam Qs</b> for written practice.",
                   "Check your answer against the \"Interpretation and check\" line; a right number with no "
                   "check is half an answer.")
              + h4("Condition")
              + p("Do not read mathematics like a story. If your pen has not moved in five minutes, you are not "
                  "studying - you are watching."),
              syllabus_item="foundation:8"),
         card("8.3 Exam strategy for a 70-mark paper",
              h4("Before you write")
              + ul("Read the whole paper once and mark the questions you can finish (usually 60-70 % of it).",
                   "Attempt in order of confidence, not in order of the paper.",
                   "For each question, write the formula first - formula marks are awarded even if arithmetic "
                   "fails.")
              + h4("During the paper")
              + ol("Show every step; a correct answer with no working loses method marks.",
                   "Carry units and brackets; write the final answer as a sentence with units.",
                   "Leave 5 minutes for arithmetic checks and for unanswered one-mark parts.")
              + h4("Where the marks are")
              + p("The official specification splits 70 marks as R 19, U 27, A 24 - more than half the paper is "
                  "understanding and application. Memorising definitions alone cannot reach a pass."),
              syllabus_item="foundation:8")]},

    {"title": tr("9. Answered Practice (foundation level)"),
     "items": []},
]

# --------------------------------------------------------------------------- numericals (20)
GIVEN = h4("Given and assumptions")
FORMULA = h4("Formula")
STEPS = h4("Step-by-step solution")
CHECK = h4("Interpretation and check")


def num(nid, q, chunks):
    return {"id": nid, "q": tr(q), "a": tr("".join(chunks))}


NUMERICALS = [
    num("m0n1", "Simplify: (−3) + (+7) − (−2).",
        [GIVEN + p("Two signs together combine first: same signs give +, different signs give −."),
         FORMULA + p("a − (−b) = a + b and a + (−b) = a − b"),
         STEPS + ol("(−3) + (+7) = 4",
                    "4 − (−2) = 4 + 2",
                    "= 6"),
         CHECK + p("<b>6.</b> Sanity: starting at −3, moving 7 right reaches 4, then 2 more right reaches 6.")]),
    num("m0n2", "Add 5/6 + 3/4 and give the answer as a mixed number.",
        [GIVEN + p("Denominators 6 and 4; LCM(6, 4) = 12."),
         FORMULA + p("a/b + c/d = (ad + bc)/bd, then simplify"),
         STEPS + ol("5/6 = 10/12 and 3/4 = 9/12",
                    "10/12 + 9/12 = 19/12",
                    "19/12 = 1 7/12"),
         CHECK + p("<b>19/12 ≈ 1.583.</b> Estimate 0.833 + 0.75 = 1.583 ✓ - the answer must be close to the "
                   "estimate.")]),
    num("m0n3", "Divide (2/3) ÷ (4/9).",
        [GIVEN + p("Dividing by a fraction is multiplying by its reciprocal."),
         FORMULA + p("a/b ÷ c/d = a/b × d/c"),
         STEPS + ol("2/3 × 9/4", "= 18/12", "= 3/2 = 1.5"),
         CHECK + p("<b>3/2.</b> Check by multiplication: (3/2)(4/9) = 12/18 = 2/3 ✓.")]),
    num("m0n4", "Find the GCD and LCM of 48 and 180.",
        [GIVEN + p("Prime factorisation of both numbers."),
         FORMULA + p("GCD = common primes, smallest powers; LCM = all primes, largest powers"),
         STEPS + ol("48 = 2⁴ × 3",
                    "180 = 2² × 3² × 5",
                    "GCD = 2² × 3 = 12",
                    "LCM = 2⁴ × 3² × 5 = 720"),
         CHECK + p("<b>GCD 12, LCM 720.</b> Check GCD × LCM = 12 × 720 = 8640 = 48 × 180 ✓.")]),
    num("m0n5", "Find 15 % of 240, and the value after a 15 % increase.",
        [GIVEN + p("Base value 240; rate 15 %."),
         FORMULA + p("part = rate × base; increased value = base × (1 + rate)"),
         STEPS + ol("15 % = 0.15",
                    "0.15 × 240 = 36",
                    "240 + 36 = 276, or 240 × 1.15 = 276"),
         CHECK + p("<b>36 and 276.</b> Check: 10 % of 240 is 24 and 5 % is 12, so 15 % is 36 ✓.")]),
    num("m0n6", "Evaluate 8 + 2 × (5 − 3)².",
        [GIVEN + p("Apply BODMAS: brackets, orders, multiplication, addition."),
         FORMULA + p("B → O → D/M left to right → A/S left to right"),
         STEPS + ol("(5 − 3) = 2", "2² = 4", "2 × 4 = 8", "8 + 8 = 16"),
         CHECK + p("<b>16.</b> The common wrong answer 100 comes from squaring 8 + 2 first, which ignores the "
                   "brackets.")]),
    num("m0n7", "Simplify (2³ × 2⁻⁵) ÷ 2⁻¹.",
        [GIVEN + p("Laws of indices with the same base 2."),
         FORMULA + p("aᵐ × aⁿ = aᵐ⁺ⁿ and aᵐ ÷ aⁿ = aᵐ⁻ⁿ"),
         STEPS + ol("2³ × 2⁻⁵ = 2⁻²", "2⁻² ÷ 2⁻¹ = 2⁻² ⁺ ¹ = 2⁻¹", "2⁻¹ = 1/2"),
         CHECK + p("<b>1/2 = 0.5.</b> Check numerically: (8 × 1/32) ÷ (1/2) = (1/4) × 2 = 1/2 ✓.")]),
    num("m0n8", "Simplify √72 − √18, and give the decimal value.",
        [GIVEN + p("Extract the largest perfect square from each surd."),
         FORMULA + p("√(a²b) = a√b"),
         STEPS + ol("√72 = √(36 × 2) = 6√2",
                    "√18 = √(9 × 2) = 3√2",
                    "6√2 − 3√2 = 3√2 = 3 × 1.41421 = 4.243"),
         CHECK + p("<b>3√2 ≈ 4.243.</b> Check: 6 × 1.414 = 8.485 and 3 × 1.414 = 4.243; the difference is "
                   "4.243 ✓.")]),
    num("m0n9", "Multiply (3.6 × 10⁴) by (2.5 × 10³) and write the answer in standard form.",
        [GIVEN + p("Front numbers and powers handled separately."),
         FORMULA + p("(a × 10ᵐ)(b × 10ⁿ) = ab × 10ᵐ⁺ⁿ"),
         STEPS + ol("3.6 × 2.5 = 9.0", "10⁴ × 10³ = 10⁷", "= 9.0 × 10⁷ = 90,000,000"),
         CHECK + p("<b>9.0 × 10⁷.</b> Estimate 4 × 10⁴ × 2.5 × 10³ = 10 × 10⁷ = 1 × 10⁸, so 9 × 10⁷ is right.")]),
    num("m0n10", "Evaluate 2x² − 3x + 1 at x = −2.",
        [GIVEN + p("Substitute the negative value inside brackets."),
         FORMULA + p("Replace x by (−2) everywhere, then apply BODMAS"),
         STEPS + ol("2(−2)² − 3(−2) + 1", "= 2(4) + 6 + 1", "= 8 + 6 + 1 = 15"),
         CHECK + p("<b>15.</b> The common error is writing −2² for (−2)², which gives 8 − 6 + 1 = 3 instead of "
                   "15.")]),
    num("m0n11", "Expand (x + 3)(x − 5).",
        [GIVEN + p("Two binomials; multiply every term of the first by every term of the second."),
         FORMULA + p("(x + a)(x + b) = x² + (a + b)x + ab"),
         STEPS + ol("x(x − 5) = x² − 5x", "3(x − 5) = 3x − 15", "x² − 5x + 3x − 15 = x² − 2x − 15"),
         CHECK + p("<b>x² − 2x − 15.</b> Check with x = 1: LHS (4)(−4) = −16; RHS 1 − 2 − 15 = −16 ✓.")]),
    num("m0n12", "Factorise 2x² + 7x − 15 and solve 2x² + 7x − 15 = 0.",
        [GIVEN + p("a = 2, b = 7, c = −15; product a·c = −30."),
         FORMULA + p("Find two numbers with product a·c and sum b, split the middle term, group"),
         STEPS + ol("10 × (−3) = −30 and 10 + (−3) = 7",
                    "2x² + 10x − 3x − 15 = 2x(x + 5) − 3(x + 5)",
                    "= (x + 5)(2x − 3)",
                    "x + 5 = 0 → x = −5; 2x − 3 = 0 → x = 3/2"),
         CHECK + p("<b>(x + 5)(2x − 3), roots −5 and 3/2.</b> Sum = −7/2 = −b/a ✓; product = −15/2 = c/a ✓.")]),
    num("m0n13", "Solve 3(x − 2) = 2x + 5.",
        [GIVEN + p("One variable, one equation; remove the bracket first."),
         FORMULA + p("The same operation on both sides keeps the balance"),
         STEPS + ol("3x − 6 = 2x + 5", "3x − 2x = 5 + 6", "x = 11"),
         CHECK + p("<b>x = 11.</b> Check: 3(11 − 2) = 27 and 2(11) + 5 = 27 ✓.")]),
    num("m0n14", "Solve 2x + 3y = 12 and x − y = 1.",
        [GIVEN + p("Two equations, two unknowns; substitution is easiest because the second gives x."),
         FORMULA + p("x = y + 1 from the second equation"),
         STEPS + ol("2(y + 1) + 3y = 12", "2y + 2 + 3y = 12", "5y = 10 → y = 2", "x = 2 + 1 = 3"),
         CHECK + p("<b>x = 3, y = 2.</b> Check both: 2(3) + 3(2) = 12 ✓ and 3 − 2 = 1 ✓.")]),
    num("m0n15", "Three pens and two pencils cost ₹80; two pens and three pencils cost ₹70. Find the price of "
                 "each.",
        [GIVEN + p("Let a pen cost p and a pencil q. The words become two equations."),
         FORMULA + p("3p + 2q = 80 and 2p + 3q = 70"),
         STEPS + ol("Multiply the first by 3: 9p + 6q = 240",
                    "Multiply the second by 2: 4p + 6q = 140",
                    "Subtract: 5p = 100 → p = 20",
                    "Then 3(20) + 2q = 80 → q = 10"),
         CHECK + p("<b>Pen ₹20, pencil ₹10.</b> Check the second equation: 2(20) + 3(10) = 70 ✓. Always answer "
                   "in words with units.")]),
    num("m0n16", "Solve 3x² − 4x + 5 = 0 and comment on the roots.",
        [GIVEN + p("a = 3, b = −4, c = 5."),
         FORMULA + p("x = (−b ± √(b² − 4ac)) / 2a; D = b² − 4ac"),
         STEPS + ol("D = (−4)² − 4(3)(5) = 16 − 60 = −44",
                    "D < 0, so √D is not a real number",
                    "No real solution exists"),
         CHECK + p("<b>D = −44, no real roots.</b> The correct conclusion is \"no real roots\", not \"x = 0\". "
                   "The parabola y = 3x² − 4x + 5 stays above the x-axis.")]),
    num("m0n17", "A rectangle is 5 m longer than it is wide and has area 84 m². Find its dimensions.",
        [GIVEN + p("Let width = w metres, so length = w + 5 metres."),
         FORMULA + p("area = width × length"),
         STEPS + ol("w(w + 5) = 84",
                    "w² + 5w − 84 = 0",
                    "(w + 12)(w − 7) = 0",
                    "w = 7 or w = −12"),
         CHECK + p("<b>7 m × 12 m.</b> A width cannot be negative, so −12 is rejected; 7 × 12 = 84 ✓.")]),
    num("m0n18", "Divide ₹4,500 in the ratio 2 : 3 : 4.",
        [GIVEN + p("Total 4500; ratio parts 2, 3 and 4."),
         FORMULA + p("one part = total / sum of parts"),
         STEPS + ol("Sum of parts = 9", "One part = 4500 / 9 = 500",
                    "Shares = 1000, 1500, 2000"),
         CHECK + p("<b>₹1,000, ₹1,500 and ₹2,000.</b> Check the total: 1000 + 1500 + 2000 = 4500 ✓.")]),
    num("m0n19", "A price rises from ₹800 to ₹920 and later falls back to ₹800. Find both percentage changes.",
        [GIVEN + p("Percentage change is measured against the original value each time."),
         FORMULA + p("change % = (new − old)/old × 100"),
         STEPS + ol("Rise: (920 − 800)/800 × 100 = 15 %",
                    "Fall: (800 − 920)/920 × 100 = −13.04 %",
                    "Net: 800 × 1.15 × 0.8696 = 800 (back to the start only because 920 → 800 is a different "
                    "base)"),
         CHECK + p("<b>+15 % then −13.04 %.</b> The two percentages are not equal because the bases differ - "
                   "this is the classic successive-percentage trap.")]),
    num("m0n20", "For A(2, 3) and B(6, 6) find the distance AB, the midpoint and the slope of AB.",
        [GIVEN + p("x₁ = 2, y₁ = 3 and x₂ = 6, y₂ = 6; gaps are 4 and 3."),
         FORMULA + p("AB = √((x₂−x₁)² + (y₂−y₁)²); M = ((x₁+x₂)/2, (y₁+y₂)/2); m = (y₂−y₁)/(x₂−x₁)"),
         STEPS + ol("AB = √(4² + 3²) = √25 = 5",
                    "M = (8/2, 9/2) = (4, 4.5)",
                    "m = 3/4 = 0.75"),
         CHECK + p("<b>AB = 5, midpoint (4, 4.5), slope 0.75.</b> Check slope with the midpoint: (4.5 − 3)/"
                   "(4 − 2) = 1.5/2 = 0.75 ✓.")]),
    num("m0n21", "If A = {1, 2, 3, 4} and B = {3, 4, 5}, find n(A ∪ B), A ∩ B and A − B.",
        [GIVEN + p("Two sets with two elements in common."),
         FORMULA + p("n(A ∪ B) = n(A) + n(B) − n(A ∩ B)"),
         STEPS + ol("A ∩ B = {3, 4}, so n(A ∩ B) = 2",
                    "n(A ∪ B) = 4 + 3 − 2 = 5, and indeed A ∪ B = {1, 2, 3, 4, 5}",
                    "A − B = {1, 2}"),
         CHECK + p("<b>5, {3, 4} and {1, 2}.</b> Check the parts: 1 and 2 only in A (2 elements), 3 and 4 in "
                   "both (2), 5 only in B (1) → 2 + 2 + 1 = 5 ✓.")]),
    num("m0n22", "The marks of a student are 62, 78, 85 and 55. Find the mean. What is the new mean if the next "
                 "test is 90?",
        [GIVEN + p("Four values, then five values after the next test."),
         FORMULA + p("mean = sum of values / count"),
         STEPS + ol("Sum = 62 + 78 + 85 + 55 = 280",
                    "Mean = 280 / 4 = 70",
                    "After 90: (280 + 90) / 5 = 370 / 5 = 74"),
         CHECK + p("<b>70, then 74.</b> Check the change: the new value is 20 above the old mean, so the mean "
                   "rises by 20/5 = 4 ✓.")]),
]

# --------------------------------------------------------------------------- formula sheet
EQUATIONS = [
    {"title": tr("Identities"), "items": [
        {"name": tr("Square of a sum"), "f": "(a + b)² = a² + 2ab + b²",
         "terms": tr("The middle term 2ab is the one most often forgotten.")},
        {"name": tr("Square of a difference"), "f": "(a − b)² = a² − 2ab + b²",
         "terms": tr("Sign of the middle term follows the bracket.")},
        {"name": tr("Difference of squares"), "f": "a² − b² = (a + b)(a − b)",
         "terms": tr("Use it in both directions: expand and factorise.")},
        {"name": tr("Trinomial with a = 1"), "f": "x² + (p + q)x + pq = (x + p)(x + q)",
         "terms": tr("Find two numbers whose sum is the middle coefficient and product is the constant.")},
    ]},
    {"title": tr("Quadratics"), "items": [
        {"name": tr("Standard form"), "f": "ax² + bx + c = 0, a ≠ 0",
         "terms": tr("Always arrange the equation in this form before choosing a method.")},
        {"name": tr("Quadratic formula"), "f": "x = (−b ± √(b² − 4ac)) / 2a",
         "terms": tr("Works for every quadratic; substitute signs carefully.")},
        {"name": tr("Discriminant"), "f": "D = b² − 4ac",
         "terms": tr("D > 0: two real roots; D = 0: one repeated root; D < 0: no real root.")},
        {"name": tr("Sum and product of roots"), "f": "x₁ + x₂ = −b/a, x₁x₂ = c/a",
         "terms": tr("Fastest check of a factorisation or of the formula.")},
    ]},
    {"title": tr("Arithmetic tools"), "items": [
        {"name": tr("LCM and GCD"), "f": "GCD(a,b) × LCM(a,b) = a × b",
         "terms": tr("Find both from prime factorisation: common primes (smallest) and all primes (largest).")},
        {"name": tr("Percentage change"), "f": "change % = (new − old) / old × 100",
         "terms": tr("Divide by the value before the change; successive changes multiply.")},
        {"name": tr("Mean"), "f": "mean = sum of values / count",
         "terms": tr("Sensitive to extreme values; the median is safer for skewed data.")},
        {"name": tr("Ratio share"), "f": "one part = total / sum of ratio parts",
         "terms": tr("Multiply one part by each ratio term and check the total.")},
    ]},
    {"title": tr("Coordinate geometry (bridge to Unit 4)"), "items": [
        {"name": tr("Distance"), "f": "AB = √((x₂−x₁)² + (y₂−y₁)²)",
         "terms": tr("Pythagoras on the horizontal and vertical gaps.")},
        {"name": tr("Midpoint"), "f": "M = ((x₁+x₂)/2, (y₁+y₂)/2)",
         "terms": tr("Average the x-coordinates and the y-coordinates separately.")},
        {"name": tr("Slope"), "f": "m = (y₂−y₁)/(x₂−x₁)",
         "terms": tr("Rise over run; vertical line (x₂ = x₁) has no finite slope.")},
    ]},
]

# --------------------------------------------------------------------------- viva
VIVA = [
    {"title": tr("Numbers, fractions and indices"), "items": [
        {"q": tr("Is every integer a rational number?"),
         "a": tr("Yes: any integer n can be written as n/1.")},
        {"q": tr("What is the difference between GCD and LCM?"),
         "a": tr("GCD is the largest number dividing both values; LCM is the smallest number both values divide.")},
        {"q": tr("How do you add two fractions with different denominators?"),
         "a": tr("Take the LCM of the denominators, rewrite both fractions over it, then add the numerators.")},
        {"q": tr("State the BODMAS order."),
         "a": tr("Brackets, Orders (powers and roots), Division and Multiplication left to right, Addition and "
                 "Subtraction left to right.")},
        {"q": tr("What is a⁻ⁿ?"),
         "a": tr("The reciprocal of aⁿ: a⁻ⁿ = 1/aⁿ, so 2⁻³ = 1/8.")},
        {"q": tr("What is a surd?"),
         "a": tr("An irrational root such as √2 or 3√5 that cannot be simplified to a whole number.")},
    ]},
    {"title": tr("Algebra"), "items": [
        {"q": tr("Expand (a + b)²."),
         "a": tr("a² + 2ab + b² - the middle term must not be dropped.")},
        {"q": tr("Factorise a² − b²."),
         "a": tr("(a + b)(a − b), the difference of two squares.")},
        {"q": tr("How do you factorise 2x² + 7x − 15?"),
         "a": tr("Split the middle term using numbers with product −30 and sum 7 (10 and −3), group, then "
                 "write (x + 5)(2x − 3).")},
        {"q": tr("What does it mean if a quadratic has D < 0?"),
         "a": tr("The equation has no real roots; the parabola does not meet the x-axis.")},
        {"q": tr("Give the quadratic formula."),
         "a": tr("x = (−b ± √(b² − 4ac)) / 2a for ax² + bx + c = 0.")},
    ]},
    {"title": tr("Equations and word problems"), "items": [
        {"q": tr("Why do you substitute the answer back into the equation?"),
         "a": tr("To verify the solution satisfies the original equation and to catch sign or arithmetic errors.")},
        {"q": tr("When do two linear equations have no solution?"),
         "a": tr("When their slopes are equal but intercepts differ, that is the lines are parallel.")},
        {"q": tr("Which method is faster for x − y = 1 and 2x + 3y = 12?"),
         "a": tr("Substitution, because the first equation already gives x = y + 1.")},
        {"q": tr("In a rectangle word problem, why is the negative root rejected?"),
         "a": tr("Because a physical length cannot be negative; state the rejection explicitly.")},
    ]},
    {"title": tr("Ratio, percentage, sets, coordinates"), "items": [
        {"q": tr("How do you divide an amount in a given ratio?"),
         "a": tr("Divide the total by the sum of the ratio parts, then multiply by each part.")},
        {"q": tr("Why is a 15 % rise followed by a 15 % fall not a return to the original price?"),
         "a": tr("The percentages are taken on different bases; the factors 1.15 and 0.85 multiply to 0.9775.")},
        {"q": tr("What is A ∩ B?"),
         "a": tr("The set of elements present in both A and B.")},
        {"q": tr("State the distance formula."),
         "a": tr("AB = √((x₂ − x₁)² + (y₂ − y₁)²).")},
        {"q": tr("What does a slope of zero mean?"),
         "a": tr("The line is horizontal: y does not change as x changes.")},
        {"q": tr("Why is the mean not always a good average?"),
         "a": tr("A single extreme value can pull it far from the typical value; the median resists this.")},
    ]},
]

# --------------------------------------------------------------------------- practice
PRACTICE = [
    ("Simplify (−8) − (−5) + (−3) × 2.", 3,
     h4("Working") + ol("(−3) × 2 = −6 (multiplication before addition)",
                        "(−8) + 5 = −3",
                        "−3 + (−6) = −9")
     + h4("Answer") + p("<b>−9.</b> Check by counting on the number line from −8: right 5 → −3, left 6 → −9.")),
    ("Add 3/8 + 5/6 and simplify.", 3,
     h4("Working") + ol("LCM(8, 6) = 24", "3/8 = 9/24 and 5/6 = 20/24", "9/24 + 20/24 = 29/24")
     + h4("Answer") + p("<b>29/24 = 1 5/24 ≈ 1.208.</b> Both fractions are close to 1/2 and 5/6 is close to 1, so "
                        "an answer near 1.2 is expected; 8/14 - adding the tops and the bottoms - is the "
                        "classic wrong answer and does not even keep the size of the number.")),
    ("Find the GCD and LCM of 36 and 60.", 4,
     h4("Working") + ol("36 = 2² × 3²", "60 = 2² × 3 × 5", "GCD = 2² × 3 = 12",
                        "LCM = 2² × 3² × 5 = 180")
     + h4("Check") + p("12 × 180 = 2160 = 36 × 60 ✓. The GCD is a factor of both numbers and the LCM is a "
                       "multiple of both: 36 = 12 × 3 and 60 = 12 × 5, while 180/36 = 5 and 180/60 = 3 - the "
                       "cross-values match, which is a quick second check.")),
    ("Evaluate 12 ÷ 3 × 2 + (4 − 1)².", 3,
     h4("Working") + ol("(4 − 1)² = 9", "12 ÷ 3 = 4, then 4 × 2 = 8 (left to right)",
                        "8 + 9 = 17")
     + h4("Answer") + p("<b>17.</b> Dividing as 12 ÷ 6 = 2 is the classic wrong path: division and "
                        "multiplication have equal priority, so they are read left to right. A calculator "
                        "entered as 12 ÷ 3 × 2 also returns 8, which is a fast way to confirm the order.")),
    ("Simplify 3x² − 5x + 2x² + 7 − x.", 3,
     h4("Working") + p("Collect like terms: (3x² + 2x²) + (−5x − x) + 7 = 5x² − 6x + 7. Nothing else combines, "
                       "because 5x², −6x and 7 are unlike terms.")
     + h4("Answer") + p("<b>5x² − 6x + 7.</b> Check by substituting x = 2: the original expression gives "
                        "12 − 10 + 8 + 7 − 2 = 15, and 5(4) − 12 + 7 = 15 ✓. A substitution check works for any "
                        "simplification question.")),
    ("Expand (2x − 3)(x + 4).", 4,
     h4("Working") + ol("2x(x + 4) = 2x² + 8x", "−3(x + 4) = −3x − 12", "2x² + 8x − 3x − 12")
     + h4("Answer") + p("<b>2x² + 5x − 12.</b> Check at x = 1: (2 − 3)(1 + 4) = −5 and 2 + 5 − 12 = −5 ✓.")),
    ("Factorise x² − 9x + 20.", 3,
     h4("Working") + p("Two numbers with product 20 and sum −9: −4 and −5, because (−4)(−5) = 20 and "
                       "(−4) + (−5) = −9. Therefore x² − 9x + 20 = (x − 4)(x − 5).")
     + h4("Check") + p("Expanding gives x² − 5x − 4x + 20 = x² − 9x + 20 ✓, so the roots of the related "
                       "equation would be x = 4 and x = 5.")),
    ("Solve 5(x + 1) = 3x + 17.", 3,
     h4("Working") + ol("5x + 5 = 3x + 17", "5x − 3x = 17 − 5", "2x = 12", "x = 6")
     + h4("Check") + p("Left: 5(6 + 1) = 35. Right: 3(6) + 17 = 35 ✓. Both sides agree, so x = 6 is correct; "
                       "divide by the coefficient only at the last step, never before collecting the terms.")),
    ("Solve 3x + 2y = 16 and x − y = 2.", 4,
     h4("Working") + ol("From the second equation, x = y + 2", "3(y + 2) + 2y = 16", "5y + 6 = 16 → y = 2",
                        "x = 2 + 2 = 4")
     + h4("Check") + p("3(4) + 2(2) = 16 ✓ and 4 − 2 = 2 ✓. The lines have different slopes (−3/2 and 1), so "
                       "exactly one pair (4, 2) exists - the answer is consistent with the geometry.")),
    ("Solve x² + 2x − 8 = 0 and state the nature of the roots.", 4,
     h4("Working") + p("Two numbers with product −8 and sum 2 are 4 and −2, so x² + 2x − 8 = (x + 4)(x − 2) = 0, "
                       "giving x = −4 or x = 2. Independently, D = 2² − 4(1)(−8) = 36 > 0, which confirms two "
                       "distinct real roots.")
     + h4("Check") + p("Sum = −4 + 2 = −2 = −b/a ✓ and product = (−4)(2) = −8 = c/a ✓. Because a > 0 the "
                       "parabola opens upward and cuts the x-axis at −4 and 2.")),
    ("A number plus its square is 30. Find the number.", 4,
     h4("Working") + p("x + x² = 30 → x² + x − 30 = 0 → (x + 6)(x − 5) = 0 → x = 5 or x = −6.")
     + h4("Answer") + p("Both satisfy the words: 5 + 25 = 30 and −6 + 36 = 30. Unless the question says "
                        "\"positive number\", give both.")),
    ("Find the distance, midpoint and slope for P(1, 2) and Q(7, 10).", 4,
     h4("Working") + ol("Gaps: 6 and 8", "PQ = √(36 + 64) = 10",
                        "Midpoint = (4, 6)", "Slope = 8/6 = 4/3 ≈ 1.33")
     + h4("Check") + p("(6 − 2)/(4 − 1) = 4/3, the same slope from the midpoint ✓.")),
    ("What is 18 % of 250, and what is 250 increased by 18 %?", 3,
     h4("Working") + ol("18 % = 0.18", "0.18 × 250 = 45", "250 + 45 = 295, and 250 × 1.18 = 295")
     + h4("Answer") + p("<b>45 and 295.</b> Note the difference between the two parts of the question: "
                        "\"18 % of 250\" is the part, while \"increased by 18 %\" is the new whole. GST of "
                        "18 % on a ₹250 item is added the same way.")),
    ("A sum of ₹6,000 is divided in the ratio 3 : 5. Find both shares.", 3,
     h4("Working") + ol("Sum of parts = 3 + 5 = 8", "One part = 6000 / 8 = ₹750",
                        "Shares = 3 × 750 = ₹2,250 and 5 × 750 = ₹3,750")
     + h4("Check") + p("2250 + 3750 = 6000 ✓, and dividing both shares by 750 returns 3 : 5 ✓. State the answer "
                       "with the rupee symbol and a comma for thousands, as a marker expects.")),
]

ANSWERED = {"title": tr("9. Answered Practice (foundation level, suggested marks)"),
            "items": [{"h": tr(f"Practice {i}. {q}"), "body": tr(a)} for i, (q, _m, a) in enumerate(PRACTICE, 1)]}
NOTES[-1] = ANSWERED
EXAM = [{"q": tr("Practice: " + q), "marks": m} for q, m, _ in PRACTICE]
LESSON_COUNT = sum(len(s["items"]) for s in NOTES) - len(ANSWERED["items"])
