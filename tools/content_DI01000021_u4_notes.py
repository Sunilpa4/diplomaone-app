"""DI01000021 Mathematics-I - Unit 4: Coordinate Geometry (GTU 4.1-4.7, 8 h, 20 %, 14 marks)."""
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
    ("Khan Academy - analytic geometry: lines and circles",
     "https://www.khanacademy.org/math/geometry/hs-geo-analytic-geometry"),
    ("GeoGebra - draw a circle and slide its centre and radius",
     "https://www.geogebra.org/m/circle"),
    ("OpenStax - College Algebra 2e, chapter 2 (equations of lines) and chapter 7 (conics)",
     "https://openstax.org/details/books/college-algebra-2e"),
    ("NCERT - Class 11 Mathematics, chapter 10 (straight lines) and chapter 11 (conic sections)",
     "https://ncert.nic.in/textbook.php"),
]

NOTES = [
    {"title": tr("1. Straight Lines and Slope"),
     "items": [
         card("1.1 Slope and the two-point form",
              h4("Definition")
              + p("The <b>slope</b> of a line is m = tan θ, where θ is the angle it makes with the positive "
                  "x-axis. Between two points it is <b>m = (y₂ − y₁)/(x₂ − x₁)</b> - rise over run.")
              + h4("Two-point form")
              + p("The line through (x₁, y₁) and (x₂, y₂) is <b>(y − y₁)(x₂ − x₁) = (y₂ − y₁)(x − x₁)</b>, which "
                  "is just the slope formula written as an equation.")
              + h4("Worked example")
              + p("Through (1, 2) and (3, 8): m = 6/2 = 3, so y − 2 = 3(x − 1), that is <b>3x − y − 1 = 0</b>. "
                  "Check the second point: 9 − 8 − 1 = 0 ✓.")
              + h4("Common mistake / conditions")
              + p("A vertical line has no finite slope (x₂ = x₁) and its equation is x = a. Never write y = mx + c "
                  "for a vertical line - that form cannot represent it."),
              "cg1_slope", examples=["cg1n1", "cg1n2"], syllabus_item="4.1"),
         card("1.2 Slope-point and intercept forms",
              h4("The four forms")
              + table(["Form", "Equation", "Use it when you know"],
                      [("Slope-intercept", "y = mx + c", "slope and y-intercept"),
                       ("Point-slope", "y − y₁ = m(x − x₁)", "one point and the slope"),
                       ("Two-point", "(y − y₁)/(y₂ − y₁) = (x − x₁)/(x₂ − x₁)", "two points"),
                       ("Intercept", "x/a + y/b = 1", "the intercepts a on x and b on y")])
              + h4("Worked examples")
              + p("Through (−2, 3) with m = 1/2: y − 3 = ½(x + 2) → 2y − 6 = x + 2 → <b>x − 2y + 8 = 0</b>.")
              + p("Intercepts 3 and −4: x/3 + y/(−4) = 1 → 4x − 3y = 12.")
              + h4("Conditions")
              + p("The intercept form needs both intercepts non-zero. A line through the origin has no "
                  "intercept form; use y = mx."),
              "cg2_forms", examples=["cg1n4", "cg1n5"], syllabus_item="4.2"),
         card("1.3 The general form and converting between forms",
              h4("Definition")
              + p("Every line can be written <b>ax + by + c = 0</b> with a and b not both zero. From it, slope = "
                  "−a/b and intercepts are −c/a (x) and −c/b (y).")
              + h4("Worked example")
              + p("3x + 4y − 12 = 0 → y = −(3/4)x + 3 (slope −3/4, y-intercept 3) and x/4 + y/3 = 1 (intercepts "
                  "4 and 3). Both come from the same equation - choose the form the question asks for.")
              + h4("Common mistake / conditions")
              + p("The slope is −a/b, not a/b. A quick check: for 3x + 4y = 12 the line falls as x grows, so "
                  "the slope must be negative ✓."),
              examples=["cg1n6"], syllabus_item="4.2")]},

    {"title": tr("2. Parallel and Perpendicular Lines"),
     "items": [
         card("2.1 The two slope conditions",
              h4("Conditions")
              + p("<b>Parallel:</b> m₁ = m₂. <b>Perpendicular:</b> m₁m₂ = −1, that is m₂ = −1/m₁.")
              + h4("In general form")
              + p("For a₁x + b₁y + c₁ = 0 and a₂x + b₂y + c₂ = 0: parallel when a₁/a₂ = b₁/b₂, perpendicular "
                  "when <b>a₁a₂ + b₁b₂ = 0</b>.")
              + h4("Worked example")
              + p("3x + 4y = 7 and 6x + 8y = 15 are parallel (coefficient ratios 1/2 and 1/2, constants "
                  "different). 3x + 4y = 7 and 4x − 3y = 2 are perpendicular because 3(4) + 4(−3) = 0.")
              + h4("Why m₁m₂ = −1")
              + p("Rotating a line by 90° turns its rise into a run: a slope of p/q becomes −q/p. Their product "
                  "is −pq/qp = −1. That is the whole proof, and it explains the sign change."),
              "cg3_parallel", examples=["cg1n3", "cg1n11", "cg1n12"], syllabus_item="4.3"),
         card("2.2 Lines parallel or perpendicular to a given line",
              h4("The two-line trick")
              + p("To draw a line parallel to ax + by + c = 0 through a point, keep a and b and change only c. "
                  "To draw a perpendicular, swap a and b and change the sign of one of them.")
              + h4("Worked examples")
              + p("Parallel to 3x − 4y + 5 = 0 through (2, −3): the family is 3x − 4y + k = 0. Substituting "
                  "gives 6 + 12 + k = 0, so k = −18 and the line is <b>3x − 4y − 18 = 0</b>.")
              + p("Perpendicular to 2x + 3y = 6 through (1, 2): the family is 3x − 2y + k = 0, and "
                  "3 − 4 + k = 0 gives k = 1, so <b>3x − 2y + 1 = 0</b>.")
              + h4("Common mistake / conditions")
              + p("Substituting the point into the <i>family</i>, not into the original line, is what finds k. "
                  "Writing the original constant again gives a parallel line that misses the point."),
              "cg3_parallel", examples=["cg1n7", "cg1n8", "cg1n24"], syllabus_item="4.4")]},

    {"title": tr("3. Angle between Two Lines and Distances"),
     "items": [
         card("3.1 The angle formula",
              h4("Formula")
              + p("<b>tan θ = |(m₁ − m₂)/(1 + m₁m₂)|</b>, the acute angle between two lines of slopes m₁ and m₂.")
              + h4("Procedure")
              + ol("Write both lines in slope form and read m₁, m₂.",
                   "Substitute into the formula; the modulus makes θ acute.",
                   "If the question wants the obtuse angle, subtract from 180°.")
              + h4("Worked example")
              + p("y = 2x + 1 and y = −x + 3: tan θ = |(2 + 1)/(1 − 2)| = 3, so θ = tan⁻¹3 ≈ <b>71.57°</b>.")
              + h4("Special cases")
              + p("If 1 + m₁m₂ = 0 the denominator vanishes and θ = 90° - the perpendicular condition. If "
                  "m₁ = m₂ the numerator vanishes and θ = 0°: the lines are parallel."),
              "cg4_angle", examples=["cg1n9", "cg1n10"], syllabus_item="4.5"),
         card("3.2 Distance from a point to a line, and between parallel lines",
              h4("Formulae")
              + p("<b>Point to line:</b> d = |ax₁ + by₁ + c| / √(a² + b²) for the point (x₁, y₁) and the line "
                  "ax + by + c = 0.")
              + p("<b>Between parallel lines</b> ax + by + c₁ = 0 and ax + by + c₂ = 0: "
                  "d = |c₁ − c₂| / √(a² + b²).")
              + h4("Worked examples")
              + p("(2, 3) to 3x + 4y − 5 = 0: |6 + 12 − 5|/√25 = 13/5 = <b>2.6 units</b>. The lines "
                  "3x + 4y = 5 and 3x + 4y = 15 are |5 − 15|/5 = <b>2 units</b> apart.")
              + h4("Conditions")
              + p("Both lines must be in the same form before comparing constants. The distance is never "
                  "negative - the modulus is part of the formula."),
              examples=["cg1n22", "cg1n23"], syllabus_item="4.5")]},

    {"title": tr("4. The Circle"),
     "items": [
         card("4.1 Centre-radius form",
              h4("Definition")
              + p("A circle is the set of points at a fixed distance r from a fixed point (h, k). Its equation is")
              + p("<b>(x − h)² + (y − k)² = r²</b>.")
              + h4("From the definition")
              + p("For any point P(x, y) on the circle, the distance CP equals r. Squaring the distance formula "
                  "√((x − h)² + (y − k)²) = r gives the equation - no memorising needed.")
              + h4("Worked example")
              + p("Centre (2, −3), radius 5: (x − 2)² + (y + 3)² = 25, which expands to "
                  "x² + y² − 4x + 6y − 12 = 0.")
              + h4("Conditions")
              + p("Watch the signs: centre (2, −3) gives (y + 3)², not (y − 3)². The right side is r², so a "
                  "radius of 5 puts 25 there."),
              "cg5_circle", examples=["cg1n13", "cg1n15"], syllabus_item="4.6"),
         card("4.2 The general equation and how to read it",
              h4("Definition")
              + p("The general circle is <b>x² + y² + 2gx + 2fy + c = 0</b>, with <b>centre (−g, −f)</b> and "
                  "<b>radius √(g² + f² − c)</b>.")
              + h4("Where it comes from")
              + p("Expand (x − h)² + (y − k)² = r²: x² + y² − 2hx − 2ky + h² + k² − r² = 0. Comparing with the "
                  "general form gives g = −h, f = −k and c = h² + k² − r², hence the radius formula.")
              + h4("Worked example")
              + p("x² + y² − 6x + 8y − 11 = 0: g = −3, f = 4, c = −11, so centre (3, −4) and radius "
                  "√(9 + 16 + 11) = <b>6</b>.")
              + h4("Conditions")
              + p("The coefficients of x² and y² must both be 1 before reading g and f; divide through if they "
                  "are not. If g² + f² − c &lt; 0 the equation has no real circle."),
              "cg6_general", examples=["cg1n14", "cg1n25"], syllabus_item="4.7"),
         card("4.3 Circle from a diameter or three conditions",
              h4("Diameter form")
              + p("If (x₁, y₁) and (x₂, y₂) are the ends of a diameter, the circle is "
                  "<b>(x − x₁)(x − x₂) + (y − y₁)(y − y₂) = 0</b>, because the angle in a semicircle is 90°.")
              + h4("Worked example")
              + p("Diameter ends (1, 2) and (5, 8): centre (3, 5) and radius ½√(16 + 36) = √13, so "
                  "(x − 3)² + (y − 5)² = 13. The diameter form gives the same circle.")
              + h4("Three points")
              + p("A circle through three points needs all three in the general equation, which gives three "
                  "linear equations in g, f, c. Through the origin c = 0 immediately, which is why exam "
                  "questions like to pass circles through (0, 0)."),
              examples=["cg1n15", "cg1n25", "cg1n16"], syllabus_item="4.6")]},

    {"title": tr("5. Tangent and Normal to a Circle"),
     "items": [
         card("5.1 Tangent at a point on the circle",
              h4("Definition")
              + p("A <b>tangent</b> touches the circle at exactly one point. At the point of contact it is "
                  "perpendicular to the radius, so its slope is the negative reciprocal of the radius slope.")
              + h4("Formula for x² + y² = a²")
              + p("The tangent at (x₁, y₁) on the circle is <b>xx₁ + yy₁ = a²</b> - replace x² by xx₁ and y² by "
                  "yy₁. For a general circle, use the point-slope form with the perpendicular slope.")
              + h4("Worked example")
              + p("At (3, 4) on x² + y² = 25: the tangent is 3x + 4y = 25. Its slope is −3/4 while the radius "
                  "slope is 4/3, and (4/3)(−3/4) = −1 ✓.")
              + h4("Common mistake / conditions")
              + p("The formula needs the point to lie on the circle: check 3² + 4² = 25 first. Using an "
                  "external point with this formula gives the chord of contact, not the tangent."),
              "cg7_tangent", examples=["cg1n17", "cg1n18"], syllabus_item="4.8"),
         card("5.2 Tangents of a given slope, and the normal",
              h4("Tangent with slope m")
              + p("For x² + y² = a² the tangents of slope m are <b>y = mx ± a√(1 + m²)</b>. The ± gives two "
                  "parallel tangents, one on each side.")
              + h4("Worked example")
              + p("Slope 3/4 to x² + y² = 25: c = ±5√(1 + 9/16) = ±25/4, so the tangents are "
                  "y = (3/4)x ± 25/4, that is <b>3x − 4y ± 25 = 0</b>.")
              + h4("Normal")
              + p("The normal at a point passes through the centre, so for x² + y² = a² it is simply the line "
                  "joining the centre to that point: through (3, 4) it is <b>y = (4/3)x</b>, or 4x − 3y = 0.")
              + h4("Length of a tangent from an external point")
              + p("From P(x₁, y₁) to x² + y² + 2gx + 2fy + c = 0 the length is "
                  "√(x₁² + y₁² + 2gx₁ + 2fy₁ + c). From (5, 1) to x² + y² = 25 it is √(26 − 25) = 1."),
              "cg7_tangent", examples=["cg1n19", "cg1n20", "cg1n21"], syllabus_item="4.8"),
         card("5.3 Tangency condition: when a line just touches",
              h4("The test")
              + p("A line touches a circle when the <b>perpendicular distance from the centre equals the "
                  "radius</b>. That single condition replaces every \"show that the line is a tangent\" proof.")
              + h4("Worked example")
              + p("Is y = 2x + c tangent to x² + y² = 25? The distance from (0, 0) to 2x − y + c = 0 is "
                  "|c|/√5, so tangency requires |c|/√5 = 5, giving c = <b>±5√5</b>.")
              + h4("Three cases")
              + table(["Distance from centre", "Line meets the circle", "Name"],
                      [("d < r", "at two points", "secant"),
                       ("d = r", "at exactly one point", "tangent"),
                       ("d > r", "not at all", "external line")])
              + h4("Why this is the safest method")
              + p("Solving the line and circle simultaneously gives a quadratic; the discriminant then decides "
                  "the case. Both routes are correct, but the distance test is shorter and has fewer sign traps."),
              "cg7_tangent", examples=["cg1n26"], syllabus_item="4.8")]},

    {"title": tr("6. Answered Practice (Unit 4 level)"), "items": []},
]

GIVEN = h4("Given and assumptions")
FORMULA = h4("Formula")
STEPS = h4("Step-by-step solution")
CHECK = h4("Interpretation and check")


def num(nid, q, chunks):
    return {"id": nid, "q": tr(q), "a": tr("".join(chunks))}


NUMERICALS = [
    num("cg1n1", "Find the slope of the line joining (2, 3) and (6, 11).",
        [GIVEN + p("Two points on the line."),
         FORMULA + p("m = (y₂ − y₁)/(x₂ − x₁)"),
         STEPS + ol("Rise = 11 − 3 = 8", "Run = 6 − 2 = 4", "m = 8/4 = 2"),
         CHECK + p("<b>m = 2.</b> The line rises 2 units for every 1 to the right, so the angle with the "
                   "x-axis is tan⁻¹2 ≈ 63.4° - consistent with a fairly steep line.")]),
    num("cg1n2", "Find the equation of the line through (1, 2) and (3, 8).",
        [GIVEN + p("Two points, so use the two-point form."),
         FORMULA + p("(y − y₁)/(y₂ − y₁) = (x − x₁)/(x₂ − x₁)"),
         STEPS + ol("Slope = (8 − 2)/(3 − 1) = 3", "y − 2 = 3(x − 1)", "y = 3x − 1, that is 3x − y − 1 = 0"),
         CHECK + p("<b>3x − y − 1 = 0.</b> Check both points: 3 − 2 − 1 = 0 ✓ and 9 − 8 − 1 = 0 ✓. Always "
                   "substitute both points - one is enough to catch most sign errors.")]),
    num("cg1n3", "Find the slope of a line perpendicular to the line joining (0, 0) and (3, 4).",
        [GIVEN + p("First the slope of the given line, then the negative reciprocal."),
         FORMULA + p("m₁m₂ = −1"),
         STEPS + ol("m₁ = 4/3", "m₂ = −3/4"),
         CHECK + p("<b>−3/4.</b> Check the product: (4/3)(−3/4) = −1 ✓. The perpendicular to a rising line must "
                   "fall, so a negative slope is expected.")]),
    num("cg1n4", "Find the equation of the line through (−2, 3) with slope 1/2.",
        [GIVEN + p("One point and the slope - point-slope form."),
         FORMULA + p("y − y₁ = m(x − x₁)"),
         STEPS + ol("y − 3 = ½(x + 2)", "2y − 6 = x + 2", "x − 2y + 8 = 0"),
         CHECK + p("<b>x − 2y + 8 = 0.</b> Check the point: −2 − 6 + 8 = 0 ✓, and the slope −a/b = −1/(−2) = ½ "
                   "✓.")]),
    num("cg1n5", "Find the equation of the line with x-intercept 3 and y-intercept −4.",
        [GIVEN + p("Both intercepts are given, so use the intercept form."),
         FORMULA + p("x/a + y/b = 1"),
         STEPS + ol("x/3 + y/(−4) = 1", "Multiply by 12: 4x − 3y = 12"),
         CHECK + p("<b>4x − 3y = 12.</b> Check both intercepts: at y = 0, x = 3 ✓; at x = 0, y = −4 ✓. The line "
                   "crosses the y-axis below the origin, which the negative intercept records.")]),
    num("cg1n6", "Reduce 3x + 4y − 12 = 0 to slope-intercept and intercept forms.",
        [GIVEN + p("Solve for y for the first, and divide by 12 for the second."),
         FORMULA + p("slope = −a/b; intercepts = −c/a and −c/b"),
         STEPS + ol("y = −(3/4)x + 3", "x/4 + y/3 = 1"),
         CHECK + p("<b>Slope −3/4, y-intercept 3, x-intercept 4.</b> Check: 3(4) + 0 − 12 = 0 ✓ and "
                   "0 + 4(3) − 12 = 0 ✓.")]),
    num("cg1n7", "Find the line through (2, −3) parallel to 3x − 4y + 5 = 0.",
        [GIVEN + p("Parallel lines differ only in the constant term."),
         FORMULA + p("family 3x − 4y + k = 0, then substitute the point"),
         STEPS + ol("3(2) − 4(−3) + k = 0", "6 + 12 + k = 0 → k = −18", "3x − 4y − 18 = 0"),
         CHECK + p("<b>3x − 4y − 18 = 0.</b> Check the point: 6 + 12 − 18 = 0 ✓, and the slope 3/4 matches the "
                   "original line's 3/4 ✓.")]),
    num("cg1n8", "Find the line through (1, 2) perpendicular to 2x + 3y = 6.",
        [GIVEN + p("Swap the coefficients and change one sign, then fit the point."),
         FORMULA + p("perpendicular family 3x − 2y + k = 0"),
         STEPS + ol("3(1) − 2(2) + k = 0", "k = 1", "3x − 2y + 1 = 0"),
         CHECK + p("<b>3x − 2y + 1 = 0.</b> Check perpendicularity from the general forms: a₁a₂ + b₁b₂ = "
                   "2(3) + 3(−2) = 0 ✓, and the point satisfies the equation ✓.")]),
    num("cg1n9", "Find the acute angle between y = 2x + 1 and y = −x + 3.",
        [GIVEN + p("Slopes m₁ = 2 and m₂ = −1."),
         FORMULA + p("tan θ = |(m₁ − m₂)/(1 + m₁m₂)|"),
         STEPS + ol("Numerator: |2 − (−1)| = 3", "Denominator: |1 + (2)(−1)| = 1", "tan θ = 3, θ = 71.57°"),
         CHECK + p("<b>θ ≈ 71.6°.</b> The lines are nowhere near parallel (slopes 2 and −1) and not "
                   "perpendicular (product −2 ≠ −1), so a large acute angle is expected.")]),
    num("cg1n10", "Find the angle between 3x − y + 4 = 0 and x + 2y − 5 = 0.",
        [GIVEN + p("Convert both to slope form first."),
         FORMULA + p("tan θ = |(m₁ − m₂)/(1 + m₁m₂)|"),
         STEPS + ol("m₁ = 3 and m₂ = −1/2",
                    "Numerator: |3 + 0.5| = 3.5, denominator: |1 − 1.5| = 0.5",
                    "tan θ = 7, θ = 81.87°"),
         CHECK + p("<b>θ ≈ 81.9°.</b> Nearly perpendicular: a₁a₂ + b₁b₂ = 3(1) + (−1)(2) = 1, which is close "
                   "to zero - so the angle must be close to 90° ✓.")]),
    num("cg1n11", "Show that 2x + 3y = 5 and 4x + 6y = 11 are parallel.",
        [GIVEN + p("Compare the coefficient ratios."),
         FORMULA + p("parallel when a₁/a₂ = b₁/b₂ ≠ c₁/c₂"),
         STEPS + ol("2/4 = 3/6 = 1/2", "5/11 ≠ 1/2", "The slopes are equal and the constants are not"),
         CHECK + p("<b>Parallel.</b> Both have slope −2/3. Because 5/11 ≠ 1/2, the lines are distinct - if the "
                   "ratios had matched they would be the same line.")]),
    num("cg1n12", "Show that 3x + 4y = 7 and 4x − 3y = 2 are perpendicular.",
        [GIVEN + p("Use the general-form test, which avoids fractions."),
         FORMULA + p("a₁a₂ + b₁b₂ = 0"),
         STEPS + ol("3(4) + 4(−3)", "= 12 − 12 = 0"),
         CHECK + p("<b>Perpendicular.</b> Slope check: m₁ = −3/4 and m₂ = 4/3, product −1 ✓. The coefficient "
                   "test is faster and has no sign traps.")]),
    num("cg1n13", "Find the equation of the circle with centre (2, −3) and radius 5.",
        [GIVEN + p("Centre-radius form, then expand if the general form is wanted."),
         FORMULA + p("(x − h)² + (y − k)² = r²"),
         STEPS + ol("(x − 2)² + (y + 3)² = 25",
                    "x² − 4x + 4 + y² + 6y + 9 = 25", "x² + y² − 4x + 6y − 12 = 0"),
         CHECK + p("<b>(x − 2)² + (y + 3)² = 25.</b> Check a point: (7, −3) is 5 units right of the centre and "
                   "satisfies 25 = 25 ✓. In the expanded form, −g = 2 and −f = −3 restore the centre.")]),
    num("cg1n14", "Find the centre and radius of x² + y² − 6x + 8y − 11 = 0.",
        [GIVEN + p("Compare with x² + y² + 2gx + 2fy + c = 0."),
         FORMULA + p("centre (−g, −f), radius √(g² + f² − c)"),
         STEPS + ol("2g = −6 → g = −3; 2f = 8 → f = 4; c = −11",
                    "Centre = (3, −4)",
                    "r = √(9 + 16 + 11) = √36 = 6"),
         CHECK + p("<b>Centre (3, −4), radius 6.</b> Check by completing the square: (x − 3)² + (y + 4)² = "
                   "9 + 16 + 11 = 36 ✓.")]),
    num("cg1n15", "Find the circle with (1, 2) and (5, 8) as ends of a diameter.",
        [GIVEN + p("The midpoint is the centre and half the distance is the radius."),
         FORMULA + p("centre = midpoint, r = ½√((x₂−x₁)² + (y₂−y₁)²)"),
         STEPS + ol("Centre = (3, 5)", "Diameter = √(16 + 36) = √52 = 2√13, so r = √13",
                    "(x − 3)² + (y − 5)² = 13"),
         CHECK + p("<b>(x − 3)² + (y − 5)² = 13.</b> Check both diameter ends: (1 − 3)² + (2 − 5)² = 4 + 9 = 13 ✓ "
                   "and (5 − 3)² + (8 − 5)² = 4 + 9 = 13 ✓.")]),
    num("cg1n16", "Find k so that (2, 3) lies on x² + y² + kx − 4y − 6 = 0.",
        [GIVEN + p("A point on the circle must satisfy its equation."),
         FORMULA + p("Substitute x = 2, y = 3"),
         STEPS + ol("4 + 9 + 2k − 12 − 6 = 0", "2k − 5 = 0", "k = 5/2"),
         CHECK + p("<b>k = 2.5.</b> Check: 4 + 9 + 5 − 12 − 6 = 0 ✓. Substituting the point is the whole test - "
                   "no geometry needed.")]),
    num("cg1n17", "Find the tangent to x² + y² = 25 at (3, 4).",
        [GIVEN + p("The point lies on the circle because 9 + 16 = 25."),
         FORMULA + p("tangent at (x₁, y₁) to x² + y² = a² is xx₁ + yy₁ = a²"),
         STEPS + ol("3x + 4y = 25"),
         CHECK + p("<b>3x + 4y = 25.</b> Check the slopes: radius slope 4/3, tangent slope −3/4, product −1 ✓. "
                   "The point (3, 4) satisfies the tangent equation ✓.")]),
    num("cg1n18", "Find the tangent to x² + y² = 13 at (2, 3).",
        [GIVEN + p("Check the point first: 4 + 9 = 13 ✓."),
         FORMULA + p("xx₁ + yy₁ = a²"),
         STEPS + ol("2x + 3y = 13"),
         CHECK + p("<b>2x + 3y = 13.</b> The radius slope is 3/2 and the tangent slope is −2/3; their product is "
                   "−1 ✓.")]),
    num("cg1n19", "Find the tangents to x² + y² = 25 that have slope 3/4.",
        [GIVEN + p("Use the slope form of the tangent."),
         FORMULA + p("y = mx ± a√(1 + m²)"),
         STEPS + ol("m = 3/4 and a = 5", "√(1 + 9/16) = 5/4", "c = ±5 × 5/4 = ±25/4",
                    "y = (3/4)x ± 25/4, that is 3x − 4y ± 25 = 0"),
         CHECK + p("<b>3x − 4y + 25 = 0 and 3x − 4y − 25 = 0.</b> Check the distance from the centre: "
                   "|25|/√(9 + 16) = 5 = radius ✓, so both lines just touch the circle.")]),
    num("cg1n20", "Find the normal to x² + y² = 25 at (3, 4).",
        [GIVEN + p("The normal passes through the centre (0, 0)."),
         FORMULA + p("the line through the centre and the point of contact"),
         STEPS + ol("Slope = (4 − 0)/(3 − 0) = 4/3", "y = (4/3)x, that is 4x − 3y = 0"),
         CHECK + p("<b>4x − 3y = 0.</b> Check the point: 12 − 12 = 0 ✓, and the normal is perpendicular to the "
                   "tangent 3x + 4y = 25 since (4/3)(−3/4) = −1 ✓.")]),
    num("cg1n21", "Find the length of the tangent from (5, 1) to x² + y² = 25.",
        [GIVEN + p("Use the power of the point."),
         FORMULA + p("length = √(x₁² + y₁² − a²)"),
         STEPS + ol("= √(25 + 1 − 25)", "= √1", "= 1"),
         CHECK + p("<b>1 unit.</b> The point is just outside the circle (distance from centre √26 ≈ 5.099 > 5), "
                   "so a short tangent is expected ✓.")]),
    num("cg1n22", "Find the distance from (2, 3) to the line 3x + 4y − 5 = 0.",
        [GIVEN + p("The line is already in general form."),
         FORMULA + p("d = |ax₁ + by₁ + c|/√(a² + b²)"),
         STEPS + ol("Numerator: |6 + 12 − 5| = 13", "Denominator: √25 = 5", "d = 13/5 = 2.6"),
         CHECK + p("<b>2.6 units.</b> The distance is positive by construction. Note that (2, 3) is far from "
                   "the origin, so a distance of a few units from this line is plausible.")]),
    num("cg1n23", "Find the distance between 3x + 4y = 5 and 3x + 4y = 15.",
        [GIVEN + p("Parallel lines with the same coefficients."),
         FORMULA + p("d = |c₁ − c₂|/√(a² + b²)"),
         STEPS + ol("|5 − 15| = 10", "√(9 + 16) = 5", "d = 10/5 = 2"),
         CHECK + p("<b>2 units.</b> Check with a point: (1.667, 0) lies on the first line and its distance from "
                   "the second is |5 − 15|/5 = 2 ✓.")]),
    num("cg1n24", "Find the line through (2, 3) parallel to the line joining (1, 1) and (4, 5).",
        [GIVEN + p("First find the slope of the joining line."),
         FORMULA + p("m = (5 − 1)/(4 − 1) = 4/3, then use point-slope"),
         STEPS + ol("y − 3 = (4/3)(x − 2)", "3y − 9 = 4x − 8", "4x − 3y + 1 = 0"),
         CHECK + p("<b>4x − 3y + 1 = 0.</b> Check the point: 8 − 9 + 1 = 0 ✓ and the slope 4/3 matches ✓.")]),
    num("cg1n25", "Find the circle through (0, 0), (4, 0) and (0, 3).",
        [GIVEN + p("Because it passes through the origin, c = 0 in the general form."),
         FORMULA + p("x² + y² + 2gx + 2fy + c = 0"),
         STEPS + ol("Through (0, 0): c = 0",
                    "Through (4, 0): 16 + 8g = 0 → g = −2",
                    "Through (0, 3): 9 + 6f = 0 → f = −3/2",
                    "x² + y² − 4x − 3y = 0"),
         CHECK + p("<b>x² + y² − 4x − 3y = 0.</b> Centre (2, 1.5) and radius √(4 + 2.25) = 2.5 - exactly half the "
                   "hypotenuse of the 3-4-5 triangle, as a circle through the three vertices of a right triangle "
                   "must be.")]),
    num("cg1n26", "Find c so that y = 2x + c is a tangent to x² + y² = 25.",
        [GIVEN + p("Tangency means the distance from the centre equals the radius."),
         FORMULA + p("distance from (0, 0) to 2x − y + c = 0 equals 5"),
         STEPS + ol("|c|/√(4 + 1) = 5", "|c| = 5√5", "c = ±5√5 ≈ ±11.18"),
         CHECK + p("<b>c = ±5√5.</b> Two parallel tangents, one on each side of the circle. Check: the distance "
                   "from the origin to 2x − y + 5√5 = 0 is 5√5/√5 = 5 = r ✓.")]),
]

EQUATIONS = [
    {"title": tr("The straight line"), "items": [
        {"name": tr("Slope"), "f": "m = (y₂ − y₁)/(x₂ − x₁) = tan θ",
         "terms": tr("Rise over run; vertical lines have no finite slope.")},
        {"name": tr("Point-slope"), "f": "y − y₁ = m(x − x₁)",
         "terms": tr("The workhorse when one point and the slope are known.")},
        {"name": tr("Two-point"), "f": "(y − y₁)/(y₂ − y₁) = (x − x₁)/(x₂ − x₁)",
         "terms": tr("Same statement as the slope formula, rearranged.")},
        {"name": tr("Intercept"), "f": "x/a + y/b = 1",
         "terms": tr("Only when both intercepts are non-zero.")},
        {"name": tr("General form"), "f": "ax + by + c = 0, slope −a/b",
         "terms": tr("Every line can be written this way.")},
    ]},
    {"title": tr("Pairs of lines"), "items": [
        {"name": tr("Parallel"), "f": "m₁ = m₂  or  a₁/a₂ = b₁/b₂",
         "terms": tr("Different constants; the same constants would mean one line.")},
        {"name": tr("Perpendicular"), "f": "m₁m₂ = −1  or  a₁a₂ + b₁b₂ = 0",
         "terms": tr("In general form the test needs no division.")},
        {"name": tr("Angle between lines"), "f": "tan θ = |(m₁ − m₂)/(1 + m₁m₂)|",
         "terms": tr("The modulus gives the acute angle.")},
        {"name": tr("Distance to a line"), "f": "d = |ax₁ + by₁ + c|/√(a² + b²)",
         "terms": tr("Between parallels, use |c₁ − c₂|/√(a² + b²).")},
    ]},
    {"title": tr("The circle"), "items": [
        {"name": tr("Centre-radius form"), "f": "(x − h)² + (y − k)² = r²",
         "terms": tr("Centre (h, k), radius r.")},
        {"name": tr("General form"), "f": "x² + y² + 2gx + 2fy + c = 0",
         "terms": tr("Centre (−g, −f), radius √(g² + f² − c).")},
        {"name": tr("Tangent at a point"), "f": "xx₁ + yy₁ = a²  for  x² + y² = a²",
         "terms": tr("For other circles use the perpendicular-to-radius slope.")},
        {"name": tr("Tangent of slope m"), "f": "y = mx ± a√(1 + m²)",
         "terms": tr("Two tangents, one on each side.")},
        {"name": tr("Tangency test"), "f": "distance from centre = radius",
         "terms": tr("Less than r: secant. Greater than r: no contact.")},
    ]},
]

VIVA = [
    {"title": tr("Lines"), "items": [
        {"q": tr("Define the slope of a line."),
         "a": tr("m = tan θ, the tangent of the angle with the positive x-axis; also (y₂ − y₁)/(x₂ − x₁).")},
        {"q": tr("Write the two-point form."),
         "a": tr("(y − y₁)/(y₂ − y₁) = (x − x₁)/(x₂ − x₁).")},
        {"q": tr("What is the slope of a vertical line?"),
         "a": tr("It is not defined; the equation is x = a.")},
        {"q": tr("Write the intercept form of a line."),
         "a": tr("x/a + y/b = 1, where a and b are the x- and y-intercepts.")},
        {"q": tr("How do you find the slope from ax + by + c = 0?"),
         "a": tr("m = −a/b.")},
        {"q": tr("Give the condition for two lines to be parallel."),
         "a": tr("m₁ = m₂, or a₁/a₂ = b₁/b₂ in general form.")},
        {"q": tr("Give the condition for two lines to be perpendicular."),
         "a": tr("m₁m₂ = −1, or a₁a₂ + b₁b₂ = 0.")},
    ]},
    {"title": tr("Angles and distances"), "items": [
        {"q": tr("State the angle-between-lines formula."),
         "a": tr("tan θ = |(m₁ − m₂)/(1 + m₁m₂)|.")},
        {"q": tr("What does the formula give when 1 + m₁m₂ = 0?"),
         "a": tr("The denominator vanishes, so θ = 90° - the lines are perpendicular.")},
        {"q": tr("Write the distance from a point to a line."),
         "a": tr("d = |ax₁ + by₁ + c|/√(a² + b²).")},
        {"q": tr("How do you find the distance between two parallel lines?"),
         "a": tr("Write both in the same form and use |c₁ − c₂|/√(a² + b²).")},
    ]},
    {"title": tr("Circles"), "items": [
        {"q": tr("Write the equation of a circle with centre (h, k) and radius r."),
         "a": tr("(x − h)² + (y − k)² = r².")},
        {"q": tr("What are the centre and radius of x² + y² + 2gx + 2fy + c = 0?"),
         "a": tr("Centre (−g, −f), radius √(g² + f² − c).")},
        {"q": tr("How do you find the centre when the ends of a diameter are given?"),
         "a": tr("The midpoint of the two ends; the radius is half the distance between them.")},
        {"q": tr("What is the tangent at (x₁, y₁) to x² + y² = a²?"),
         "a": tr("xx₁ + yy₁ = a².")},
        {"q": tr("Why is the tangent perpendicular to the radius?"),
         "a": tr("The radius to the point of contact is the shortest distance to the tangent, so the two are "
                 "perpendicular.")},
        {"q": tr("Write the normal to a circle at a point."),
         "a": tr("The line joining the centre to that point, because every normal passes through the centre.")},
        {"q": tr("How do you test whether a line is tangent to a circle?"),
         "a": tr("The perpendicular distance from the centre equals the radius.")},
        {"q": tr("Give the tangents of slope m to x² + y² = a²."),
         "a": tr("y = mx ± a√(1 + m²).")},
        {"q": tr("What is the length of the tangent from (x₁, y₁) to x² + y² = a²?"),
         "a": tr("√(x₁² + y₁² − a²).")},
    ]},
]

PRACTICE = [
    ("Find the slope and equation of the line through (0, 5) and (3, 11).", 4,
     h4("Working") + ol("m = (11 − 5)/(3 − 0) = 2", "y − 5 = 2(x − 0)", "y = 2x + 5")
     + h4("Answer") + p("<b>Slope 2, equation 2x − y + 5 = 0.</b> Check both points: 0 − 5 + 5 = 0 ✓ and "
                        "6 − 11 + 5 = 0 ✓.")),
    ("Find the equation of the line with slope −3 passing through (2, 4).", 3,
     h4("Working") + ol("Start from y − y₁ = m(x − x₁) with m = −3 and (x₁, y₁) = (2, 4)",
                        "y − 4 = −3(x − 2)", "y − 4 = −3x + 6", "y = −3x + 10, that is 3x + y − 10 = 0")
     + h4("Answer") + p("<b>3x + y − 10 = 0.</b> Check: 6 + 4 − 10 = 0 ✓, the y-intercept is 10 ✓, and the "
                        "slope −a/b = −3 ✓. As a final form, a straight-line answer is safest with integer "
                        "coefficients and a positive x-term.")),
    ("Find the equation of the line whose intercepts are −2 on x and 5 on y.", 3,
     h4("Working") + ol("x/(−2) + y/5 = 1", "Multiply by 10: −5x + 2y = 10", "5x − 2y + 10 = 0")
     + h4("Answer") + p("<b>5x − 2y + 10 = 0.</b> Check the intercepts: at y = 0, x = −2 ✓; at x = 0, y = 5 ✓.")),
    ("Show that the lines 5x − 2y + 3 = 0 and 10x − 4y − 7 = 0 are parallel.", 3,
     h4("Working") + ol("For ax + by + c = 0 the slope is −a/b",
                        "First line: −5/(−2) = 5/2",
                        "Second line: −10/(−4) = 5/2",
                        "Ratio test: 5/10 = (−2)/(−4) = 1/2, but 3/(−7) ≠ 1/2")
     + h4("Answer") + p("<b>Parallel and distinct.</b> Both have slope 5/2, and because the constant ratio "
                        "differs the two lines never meet. Had all three ratios matched, they would be the "
                        "same line rather than two parallel ones.")),
    ("Find the equation of the line through (3, −1) perpendicular to 4x − 3y + 7 = 0.", 4,
     h4("Working") + ol("Perpendicular family: 3x + 4y + k = 0", "3(3) + 4(−1) + k = 0", "k = −5",
                        "3x + 4y − 5 = 0")
     + h4("Check") + p("a₁a₂ + b₁b₂ = 4(3) + (−3)(4) = 0 ✓ and the point satisfies the new line ✓.")),
    ("Find the acute angle between 2x − y + 3 = 0 and x + 3y − 2 = 0.", 4,
     h4("Working") + ol("m₁ = 2 and m₂ = −1/3",
                        "tan θ = |(2 + 1/3)/(1 − 2/3)| = |(7/3)/(1/3)| = 7", "θ = 81.87°")
     + h4("Answer") + p("<b>θ ≈ 81.9°.</b> The coefficient test gives 2(1) + (−1)(3) = −1, close to zero, so the "
                        "lines are nearly perpendicular ✓.")),
    ("Find the distance between the parallel lines 4x + 3y − 9 = 0 and 4x + 3y + 6 = 0.", 4,
     h4("Working") + ol("|−9 − 6| = 15", "√(16 + 9) = 5", "d = 15/5 = 3")
     + h4("Answer") + p("<b>3 units.</b> Check with a point: (0, 3) lies on the first line and its distance from "
                        "the second is |0 + 9 + 6|/5 = 3 ✓.")),
    ("Find the centre and radius of x² + y² + 4x − 6y − 12 = 0.", 4,
     h4("Working") + ol("2g = 4 → g = 2; 2f = −6 → f = −3; c = −12",
                        "Centre (−2, 3)", "r = √(4 + 9 + 12) = √25 = 5")
     + h4("Answer") + p("<b>Centre (−2, 3), radius 5.</b> Check by completing the square: (x + 2)² + (y − 3)² = "
                        "25 ✓.")),
    ("Find the equation of the circle with centre (−1, 2) passing through (3, 5).", 4,
     h4("Working") + ol("r = √((3 + 1)² + (5 − 2)²) = √(16 + 9) = 5",
                        "(x + 1)² + (y − 2)² = 25", "x² + y² + 2x − 4y − 20 = 0")
     + h4("Check") + p("The point (3, 5) satisfies 16 + 9 = 25 ✓. The expanded form has centre (−1, 2) again ✓.")),
    ("Find the tangent to x² + y² = 169 at (5, 12).", 3,
     h4("Working") + p("The point is on the circle because 25 + 144 = 169. The tangent is 5x + 12y = 169.")
     + h4("Answer") + p("<b>5x + 12y = 169.</b> Radius slope 12/5, tangent slope −5/12, product −1 ✓.")),
    ("Find the normal to x² + y² = 25 at (−4, 3).", 3,
     h4("Working") + p("The normal joins the centre (0, 0) to (−4, 3): slope 3/(−4) = −3/4, so y = −(3/4)x, "
                       "that is 3x + 4y = 0.")
     + h4("Check") + p("The point satisfies −12 + 12 = 0 ✓, and this line is perpendicular to the tangent "
                       "−4x + 3y = 25 ✓.")),
    ("Find k if the line 3x + 4y + k = 0 is tangent to x² + y² = 25.", 4,
     h4("Working") + ol("Distance from centre = |k|/5", "Set it equal to the radius: |k|/5 = 5",
                        "k = ±25")
     + h4("Answer") + p("<b>k = ±25.</b> Two tangents, 3x + 4y = ±25. Check: |25|/5 = 5 = r ✓.")),
    ("Find the length of the tangent from (7, 1) to x² + y² − 4x + 2y − 4 = 0.", 4,
     h4("Working") + ol("Value at the point: 49 + 1 − 28 + 2 − 4 = 20",
                        "Length = √20 = 2√5 ≈ 4.47")
     + h4("Answer") + p("<b>2√5 ≈ 4.47 units.</b> The circle has centre (2, −1) and radius 3, and the point is "
                        "√((7−2)² + (1+1)²) = √29 ≈ 5.39 from the centre, so a tangent of about 4.47 is "
                        "consistent with √(29 − 9) ✓.")),
    ("A circle passes through (2, 3) and has centre (2, 0). Find its equation and the tangent at (2, 3).", 4,
     h4("Working") + ol("r = 3, so (x − 2)² + y² = 9",
                        "At (2, 3) the radius is vertical, so the tangent is horizontal: y = 3")
     + h4("Answer") + p("<b>(x − 2)² + y² = 9 and the tangent y = 3.</b> The tangent is perpendicular to a "
                        "vertical radius, which is exactly what the horizontal line gives.")),
    ("Find the equation of the line through the point of intersection of x + y = 4 and x − y = 2 that is "
     "parallel to 3x + 2y = 5.", 4,
     h4("Working") + ol("Solving the pair: x = 3, y = 1",
                        "Slope of 3x + 2y = 5 is −3/2", "y − 1 = −(3/2)(x − 3)", "3x + 2y − 11 = 0")
     + h4("Check") + p("The point (3, 1) satisfies 9 + 2 − 11 = 0 ✓ and the slope is −3/2 ✓.")),
]

ANSWERED = {"title": tr("6. Answered Practice (Unit 4 level, suggested marks)"),
            "items": [{"h": tr(f"Practice {i}. {q}"), "body": tr(a)} for i, (q, _m, a) in enumerate(PRACTICE, 1)]}
NOTES[-1] = ANSWERED
EXAM = [{"q": tr("Practice: " + q), "marks": m} for q, m, _ in PRACTICE]
LESSON_COUNT = sum(len(s["items"]) for s in NOTES) - len(ANSWERED["items"])
