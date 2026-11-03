"""DI01000021 Mathematics-I - Unit 2: Trigonometry (GTU 2.1-2.7, 12 h, 20 %, 14 marks).

Degree and radian measure, the six functions, allied and compound angles, multiple and submultiple angles,
the graphs of sine and cosine with periodicity, the sum and factor formulae, and inverse functions.
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
    ("Khan Academy - trigonometry, unit circle and inverse functions",
     "https://www.khanacademy.org/math/trigonometry"),
    ("GeoGebra - slide A and B to watch sin(A + B) change",
     "https://www.geogebra.org/m/trigonometry"),
    ("OpenStax - Algebra and Trigonometry 2e (free textbook)",
     "https://openstax.org/details/books/algebra-and-trigonometry-2e"),
    ("NCERT - Class 11 Mathematics, chapters 3 and 4",
     "https://ncert.nic.in/textbook.php"),
]

NOTES = [
    {"title": tr("1. Angles and their Measurement"),
     "items": [
         card("1.1 Degree and radian measure",
              h4("Definition")
              + p("An angle is the amount of rotation from an initial arm to a terminal arm. The two <b>units "
                  "of angles</b> are the <b>degree</b> (one full turn = 360°) and the <b>radian</b> (one full "
                  "turn = 2π); the same rotation gives the same angle in either unit.")
              + h4("The conversion")
              + p("<b>π radians = 180°</b>, so <b>radians = degrees × π/180</b> and <b>degrees = radians × "
                  "180/π</b>. One radian is about 57.3°.")
              + h4("Angles you should know instantly")
              + table(["Degrees", "0°", "30°", "45°", "60°", "90°", "180°", "360°"],
                      [("Radians", "0", "π/6", "π/4", "π/3", "π/2", "π", "2π")])
              + h4("Why radians")
              + p("A radian is defined by arc length: 1 radian subtends an arc equal to the radius. That is why "
                  "arc length, sector area and angular speed formulas only work when θ is in radians - and why "
                  "calculus in later semesters uses radians only."),
              "t1_deg_rad", examples=["t1n1"], syllabus_item="2.1"),
         card("1.2 Arc length and area of a sector",
              h4("Formulae")
              + p("For a circle of radius r and an angle θ <b>in radians</b>:")
              + p("<b>arc length s = rθ</b> and <b>sector area A = ½ r²θ</b>.")
              + h4("Derivation")
              + p("A full turn is 2π radians and its arc is the circumference 2πr. So a fraction θ/2π of the "
                  "circle has arc (θ/2π)(2πr) = rθ. The full area is πr², so the same fraction gives "
                  "(θ/2π)(πr²) = ½r²θ. Both formulas are proportions - nothing new is memorised.")
              + h4("Common mistake / conditions")
              + p("Substituting degrees directly gives nonsense: for θ = 60° and r = 7, rθ = 420, which is far "
                  "larger than the whole circumference. Convert to π/3 first, then s = 7π/3 ≈ 7.33 cm."),
              examples=["t1n2"], syllabus_item="2.1"),
         card("1.3 Angular speed and linear speed",
              h4("Definition")
              + p("<b>Angular speed</b> ω is the angle swept per second (rad/s); <b>linear speed</b> v is the "
                  "distance travelled per second along the circle. They are linked by <b>v = rω</b>.")
              + h4("Conversions")
              + ul("1 revolution = 2π radians, so rpm × 2π/60 gives rad/s.",
                   "1 rad/s at radius r gives v = r m/s with r in metres.",
                   "Frequency f (revolutions per second) gives ω = 2πf.")
              + h4("Worked example")
              + p("A wheel of radius 30 cm turns at 300 rpm. ω = 300 × 2π/60 = 10π ≈ 31.42 rad/s, so "
                  "v = 0.30 × 31.42 ≈ <b>9.42 m/s</b>. Doubling the radius doubles the rim speed at the same "
                  "rpm - the reason a larger wheel covers more ground per turn."),
              examples=["t1n3"], syllabus_item="2.1")]},

    {"title": tr("2. Trigonometric Functions"),
     "items": [
         card("2.1 The six ratios, from triangle to unit circle",
              h4("Definition")
              + p("In a right triangle, for an acute angle θ: sin θ = opposite/hypotenuse, cos θ = "
                  "adjacent/hypotenuse, tan θ = opposite/adjacent, with cosec, sec and cot as their reciprocals.")
              + h4("The unit-circle definition")
              + p("Take a point P(x, y) on the circle of radius 1 at angle θ from the positive x-axis. Then "
                  "<b>cos θ = x</b>, <b>sin θ = y</b> and tan θ = y/x. This extends the ratios to every angle, "
                  "including obtuse, negative and reflex angles, because x and y carry signs.")
              + h4("Signs are automatic here")
              + p("A point in the second quadrant has x &lt; 0, so cos θ &lt; 0 there while sin θ &gt; 0. You do "
                  "not need a rule to remember - just picture the point."),
              "t2_quadrants", examples=["t1n4"], syllabus_item="2.2"),
         card("2.2 Signs in the four quadrants",
              h4("Definition")
              + p("The <b>ASTC rule</b> (All, Sin, Tan, Cos) says which functions are positive in each "
                  "quadrant, counting anticlockwise from the positive x-axis.")
              + table(["Quadrant", "Angle range", "Positive functions", "Memory line"],
                      [("I", "0° to 90°", "all six", "All"),
                       ("II", "90° to 180°", "sin and cosec", "Silver"),
                       ("III", "180° to 270°", "tan and cot", "Tea"),
                       ("IV", "270° to 360°", "cos and sec", "Cups")])
              + h4("Reading it from the circle")
              + p("In Q II the x-coordinate is negative and y positive, so only sin (= y) is positive. In Q III "
                  "both are negative, so their ratio tan is positive. In Q IV x is positive, so cos is positive.")
              + h4("Common mistake / conditions")
              + p("tan θ is undefined at 90° and 270° (the point has x = 0, so y/x divides by zero), and cot θ, "
                  "cosec θ, sec θ are undefined wherever their own denominators vanish. State the excluded "
                  "angles when the question asks for the domain."),
              "t2_quadrants", examples=["t1n4"], syllabus_item="2.2"),
         card("2.3 The standard-angle table",
              h4("Definition")
              + p("Five angles carry almost every numerical in this unit. Learn the table and you can evaluate "
                  "any allied angle without a calculator.")
              + table(["θ", "0°", "30°", "45°", "60°", "90°"],
                      [("sin θ", "0", "1/2", "1/√2", "√3/2", "1"),
                       ("cos θ", "1", "√3/2", "1/√2", "1/2", "0"),
                       ("tan θ", "0", "1/√3", "1", "√3", "not defined")])
              + h4("Pattern worth noticing")
              + p("sin runs 0, 1/2, 1/√2, √3/2, 1 - the values are √0/2, √1/2, √2/2, √3/2, √4/2. cos is the same "
                  "list reversed, which is why sin 30° = cos 60°.")
              + h4("Conditions")
              + p("tan 90° is undefined, not infinite; write \"not defined\" in an exam. The table is for "
                  "exact values - use decimals only when a question asks for them."),
              examples=["t1n5"], syllabus_item="2.2"),
         card("2.4 The three fundamental identities",
              h4("Identities")
              + p("<b>sin²θ + cos²θ = 1</b>,  <b>1 + tan²θ = sec²θ</b>,  <b>1 + cot²θ = cosec²θ</b>.")
              + h4("Where the first one comes from")
              + p("On the unit circle P(x, y) has x² + y² = 1 by Pythagoras, and x = cos θ, y = sin θ. Divide "
                  "that same equation by cos²θ and you get the second identity; divide by sin²θ and you get the "
                  "third. One equation produces all three.")
              + h4("How they are used")
              + p("To turn a sum into a single term: 1 − sin²θ = cos²θ; to simplify a fraction; and to find the "
                  "third ratio from one given value plus a quadrant. Given sin θ = 3/5 with θ in Q II, "
                  "cos²θ = 1 − 9/25 = 16/25, so cos θ = −4/5 (negative because the quadrant says so)."),
              examples=["t1n6"], syllabus_item="2.2")]},

    {"title": tr("3. Allied Angles"),
     "items": [
         card("3.1 The allied-angle rules",
              h4("Definition")
              + p("Allied angles are built from θ using 180°, 360° and the negative sign. Two steps always "
                  "work: decide the <b>sign</b> from the quadrant, then use θ itself as the angle.")
              + table(["Angle", "sin", "cos", "tan"],
                      [("−θ", "−sin θ", "cos θ", "−tan θ"),
                       ("90° − θ", "cos θ", "sin θ", "cot θ"),
                       ("90° + θ", "cos θ", "−sin θ", "−cot θ"),
                       ("180° − θ", "sin θ", "−cos θ", "−tan θ"),
                       ("180° + θ", "−sin θ", "−cos θ", "tan θ"),
                       ("270° − θ", "−cos θ", "−sin θ", "cot θ"),
                       ("360° − θ", "−sin θ", "cos θ", "−tan θ")])
              + h4("The rule in words")
              + p("For odd multiples of 90° the function changes (sin ↔ cos); for even multiples it stays. The "
                  "sign comes from the quadrant of the original angle. Example: sin(180° + θ) keeps the name "
                  "sin, lies in Q III where sin is negative, so the answer is −sin θ."),
              "t3_allied", examples=["t1n7", "t1n8"], syllabus_item="2.3"),
         card("3.2 Evaluating large and negative angles",
              h4("Procedure")
              + ol("Reduce the angle into 0°-360° by adding or subtracting 360° (the functions are periodic).",
                   "Use the allied-angle rule to bring it into 0°-90°.",
                   "Substitute the standard value.")
              + h4("Worked examples")
              + p("sin 150° = sin(180° − 30°) = sin 30° = <b>1/2</b>. cos 240° = cos(180° + 60°) = −cos 60° = "
                  "<b>−1/2</b>. tan 315° = tan(360° − 45°) = −tan 45° = <b>−1</b>. sin(−330°) = −sin 330° = "
                  "−(−1/2) = <b>1/2</b>.")
              + h4("Common mistake / conditions")
              + p("Do not drop the sign because the numbers look small: 240° is in Q III, so its cosine must be "
                  "negative even though cos 60° = 1/2. Write the quadrant in the margin before evaluating."),
              examples=["t1n8"], syllabus_item="2.3")]},

    {"title": tr("4. Compound Angles"),
     "items": [
         card("4.1 sin(A ± B) and cos(A ± B)",
              h4("Formulae")
              + p("<b>sin(A + B) = sin A cos B + cos A sin B</b>,  <b>sin(A − B) = sin A cos B − cos A sin B</b>")
              + p("<b>cos(A + B) = cos A cos B − sin A sin B</b>,  <b>cos(A − B) = cos A cos B + sin A sin B</b>")
              + h4("How the pattern is remembered")
              + p("sin keeps the signs it is given; cos flips them. In sin the two terms are sine-cosine and "
                  "cosine-sine; in cos the cosines come first in both terms.")
              + h4("Where it is used")
              + p("It turns an unknown angle into two known ones: 75° = 45° + 30° and 15° = 45° − 30°. That is "
                  "why sin 75° can be written exactly as (√6 + √2)/4 ≈ 0.966 without a calculator."),
              "t4_compound", examples=["t1n9", "t1n10"], syllabus_item="2.3"),
         card("4.2 tan(A ± B)",
              h4("Formula")
              + p("<b>tan(A + B) = (tan A + tan B)/(1 − tan A tan B)</b> and "
                  "<b>tan(A − B) = (tan A − tan B)/(1 + tan A tan B)</b>.")
              + h4("Derivation (two lines)")
              + p("Write tan(A + B) = sin(A + B)/cos(A + B), substitute the two formulas above, and divide "
                  "numerator and denominator by cos A cos B. The result follows.")
              + h4("Worked example")
              + p("tan 75° = tan(45° + 30°) = (1 + 1/√3)/(1 − 1/√3) = (√3 + 1)/(√3 − 1) = <b>2 + √3 ≈ "
                  "3.732</b> (rationalise by multiplying by (√3 + 1)/(√3 + 1), since (√3 − 1)(√3 + 1) = 2).")
              + h4("Conditions")
              + p("The formula fails when a denominator is zero - for example tan(A + B) when A + B = 90°. "
                  "Check the angle before substituting."),
              examples=["t1n11"], syllabus_item="2.3"),
         card("4.3 Compound-angle numericals with given ratios",
              h4("Method")
              + ol("Draw a right triangle (or use sin² + cos² = 1) to find the missing ratios.",
                   "Fix each sign by the quadrant given in the question.",
                   "Substitute into the compound-angle formula and simplify.")
              + h4("Worked example")
              + p("If sin A = 3/5 and cos B = 5/13 with A, B acute, then cos A = 4/5 and sin B = 12/13. So "
                  "sin(A + B) = (3/5)(5/13) + (4/5)(12/13) = 15/65 + 48/65 = <b>63/65 ≈ 0.969</b>.")
              + h4("Why the check matters")
              + p("A and B are acute, so A + B is between 0° and 180°; sin(A + B) must be positive, and 63/65 "
                  "is. If you get a negative sine, a quadrant sign is wrong."),
              examples=["t1n12"], syllabus_item="2.3"),
         card("4.4 Heights and distances: the engineering use",
              h4("Definition")
              + p("Surveying, civil and mechanical work all reduce to one right triangle: a horizontal "
                  "distance d, a vertical height h, and the <b>angle of elevation</b> (looking up) or "
                  "<b>depression</b> (looking down).")
              + h4("The three relations")
              + ul("tan θ = h/d - the workhorse, because it links the two distances.",
                   "sin θ = h/L where L is the slant length (a ladder, a cable, a ramp).",
                   "cos θ = d/L - use it when the sloping length is the known quantity.")
              + h4("Worked example")
              + p("From 50 m away the top of a tower is seen at 30° above the horizontal: h = 50 tan 30° = "
                  "50/√3 ≈ <b>28.87 m</b>. If the angle were 45°, the height would equal the distance - the "
                  "quickest sanity check in the field.")
              + h4("Conditions")
              + p("Both angles are measured from the horizontal, and the instrument height is added to h. "
                  "Sketch the triangle and mark the right angle before writing any ratio."),
              examples=["t1n26"], syllabus_item="2.3")]},

    {"title": tr("5. Multiple and Submultiple Angles"),
     "items": [
         card("5.1 Double-angle formulae",
              h4("Formulae")
              + p("<b>sin 2A = 2 sin A cos A</b>;  <b>cos 2A = cos²A − sin²A = 2cos²A − 1 = 1 − 2sin²A</b>;")
              + p("<b>tan 2A = 2 tan A / (1 − tan²A)</b>.")
              + h4("Derivation")
              + p("Put B = A in the compound formulas: sin(A + A) = sin A cos A + cos A sin A = 2 sin A cos A, "
                  "and cos(A + A) = cos²A − sin²A. Replacing sin²A by 1 − cos²A (or the reverse) gives the two "
                  "other forms of cos 2A - choose the one that matches what the question gives you.")
              + h4("Worked example")
              + p("sin A = 3/5 with A acute gives cos A = 4/5, so sin 2A = 2(3/5)(4/5) = <b>24/25</b> and "
                  "cos 2A = 16/25 − 9/25 = <b>7/25</b>."),
              "t5_double", examples=["t1n13", "t1n14"], syllabus_item="2.4"),
         card("5.2 Submultiple (half-angle) formulae",
              h4("Formulae")
              + p("From cos 2A = 1 − 2sin²A, with 2A replaced by θ: <b>sin(θ/2) = ±√((1 − cos θ)/2)</b>;")
              + p("<b>cos(θ/2) = ±√((1 + cos θ)/2)</b>;  <b>tan(θ/2) = (1 − cos θ)/sin θ = sin θ/(1 + cos θ)</b>.")
              + h4("The sign question")
              + p("The ± is decided by the quadrant of θ/2, not of θ. If θ = 300°, then θ/2 = 150° lies in Q II, "
                  "where sine is positive and cosine negative - so the sine takes + and the cosine takes −.")
              + h4("Worked example")
              + p("sin 15° = √((1 − cos 30°)/2) = √((1 − √3/2)/2) = √(2 − √3)/2 ≈ <b>0.2588</b>, which agrees "
                  "with sin(45° − 30°) computed by the compound formula."),
              "t5_double", examples=["t1n15"], syllabus_item="2.4"),
         card("5.3 Triple-angle formulae",
              h4("Formulae")
              + p("<b>sin 3A = 3 sin A − 4 sin³A</b>;  <b>cos 3A = 4 cos³A − 3 cos A</b>;")
              + p("<b>tan 3A = (3 tan A − tan³A)/(1 − 3 tan²A)</b>.")
              + h4("Derivation")
              + p("Write 3A = 2A + A and apply sin(A + B) with B = 2A, then substitute the double-angle results "
                  "and replace cos²A by 1 − sin²A. Every multiple-angle formula is built this way.")
              + h4("Worked example")
              + p("With sin A = 1/2: sin 3A = 3(1/2) − 4(1/8) = 1.5 − 0.5 = <b>1</b>, and indeed 3A = 90° when "
                  "A = 30°. The formula is a check on itself."),
              examples=["t1n16"], syllabus_item="2.4")]},

    {"title": tr("6. Graphs and Periodicity"),
     "items": [
         card("6.1 Graphs of sin x and cos x",
              h4("Shape")
              + p("Both curves oscillate between −1 and 1. sin x starts at 0 and rises; cos x starts at 1 and "
                  "falls. They are the same wave shifted by 90°: <b>cos x = sin(x + 90°)</b>.")
              + h4("Key points of one cycle")
              + table(["x", "0", "π/2", "π", "3π/2", "2π"],
                      [("sin x", "0", "1", "0", "−1", "0"),
                       ("cos x", "1", "0", "−1", "0", "1")])
              + h4("Words used with graphs")
              + ul("<b>Amplitude</b>: half the distance between maximum and minimum (1 for both curves).",
                   "<b>Period</b>: length of one complete cycle (2π for both).",
                   "<b>Zeros</b>: where the curve crosses the axis - sin at 0, π, 2π; cos at π/2, 3π/2.",
                   "<b>Maximum / minimum</b>: 1 and −1, reached once per cycle.")
              + p("Sketching five points and joining them with a smooth wave is enough for an exam answer - a "
                  "table of values plus the shape earns the marks."),
              "t6_sincos", syllabus_item="2.5"),
         card("6.2 Periodic functions and the period of sin kx",
              h4("Definition")
              + p("A function is <b>periodic</b> with period T if f(x + T) = f(x) for every x, and T is the "
                  "smallest such positive number. sin x and cos x have period 2π; tan x has period π.")
              + h4("Changing the frequency")
              + table(["Function", "Amplitude", "Period"],
                      [("sin x, cos x", "1", "2π"),
                       ("sin kx, cos kx", "1", "2π/|k|"),
                       ("tan kx", "none", "π/|k|"),
                       ("a sin kx", "|a|", "2π/|k|")])
              + h4("Worked examples")
              + p("sin 3x has period 2π/3, so three cycles fit in 0 to 2π. cos(x/2) has period 4π - it is "
                  "slower, not faster. tan 2x has period π/2. A common error is dividing by k in the wrong "
                  "direction; test with k = 2: the curve repeats twice as often, so the period must be halved."),
              "t6_sincos", examples=["t1n17"], syllabus_item="2.5"),
         card("6.3 Reading y = a sin(bx + c) + d",
              h4("The four numbers")
              + table(["Letter", "Name", "What it does"],
                      [("a", "amplitude", "stretches vertically; range becomes d − |a| to d + |a|"),
                       ("b", "frequency", "period becomes 2π/|b|"),
                       ("c", "phase", "shifts left by c/b (right if negative)"),
                       ("d", "vertical shift", "moves the whole graph up or down")])
              + h4("Worked example")
              + p("y = 3 sin(2x − π/3) + 1: amplitude 3, period π, phase shift π/6 to the right, centre line "
                  "y = 1, so the range is <b>−2 to 4</b> and the maximum 4 occurs when sin(...) = 1.")
              + h4("Conditions")
              + p("The phase shift is c/b only when the bracket is written as b(x + c/b) - factor b out first. "
                  "Without that step the shift is reported as c, which is the standard mistake."),
              examples=["t1n18", "t1n19"], syllabus_item="2.5")]},

    {"title": tr("7. Sum and Factor Formulae"),
     "items": [
         card("7.1 Sum and difference into product",
              h4("Formulae")
              + p("<b>sin C + sin D = 2 sin((C + D)/2) cos((C − D)/2)</b>")
              + p("<b>sin C − sin D = 2 cos((C + D)/2) sin((C − D)/2)</b>")
              + p("<b>cos C + cos D = 2 cos((C + D)/2) cos((C − D)/2)</b>")
              + p("<b>cos C − cos D = −2 sin((C + D)/2) sin((C − D)/2)</b> - note the leading minus.")
              + h4("Derivation")
              + p("Add the two compound formulas sin(A + B) and sin(A − B): the cosine terms cancel and "
                  "2 sin A cos B remains. Put A = (C + D)/2 and B = (C − D)/2 and the first formula appears. "
                  "Subtracting instead of adding gives the second; the cosine pair works the same way.")
              + h4("Worked example")
              + p("sin 75° + sin 15° = 2 sin 45° cos 30° = 2 × (√2/2)(√3/2) = <b>√6/2 ≈ 1.225</b>, which matches "
                  "0.966 + 0.259 = 1.225 ✓."),
              "t7_sumprod", examples=["t1n20"], syllabus_item="2.6"),
         card("7.2 Product into sum or difference",
              h4("Formulae")
              + p("<b>2 sin A cos B = sin(A + B) + sin(A − B)</b>")
              + p("<b>2 cos A sin B = sin(A + B) − sin(A − B)</b>")
              + p("<b>2 cos A cos B = cos(A + B) + cos(A − B)</b>")
              + p("<b>2 sin A sin B = cos(A − B) − cos(A + B)</b>")
              + h4("How to use them")
              + p("These turn a product (hard to integrate later) into a sum. Choose the pair whose sum and "
                  "difference are the angles you have: 2 sin 40° cos 20° = sin 60° + sin 20° ≈ 0.866 + 0.342 = "
                  "<b>1.208</b>.")
              + h4("Simplifications worth knowing")
              + p("(sin A + sin 3A)/(cos A + cos 3A) = (2 sin 2A cos A)/(2 cos 2A cos A) = <b>tan 2A</b>. "
                  "Questions of this type are always solved by converting every sum into a product and "
                  "cancelling."),
              "t7_sumprod", examples=["t1n21", "t1n22"], syllabus_item="2.6")]},

    {"title": tr("8. Inverse Trigonometric Functions"),
     "items": [
         card("8.1 Definition and principal values",
              h4("Definition")
              + p("sin⁻¹x is the angle in a fixed <b>principal range</b> whose sine is x. The restriction makes "
                  "the inverse a genuine function, because the original sine repeats.")
              + table(["Function", "Domain", "Principal range"],
                      [("sin⁻¹x", "−1 ≤ x ≤ 1", "−π/2 to π/2"),
                       ("cos⁻¹x", "−1 ≤ x ≤ 1", "0 to π"),
                       ("tan⁻¹x", "all real x", "−π/2 to π/2"),
                       ("cot⁻¹x", "all real x", "0 to π")])
              + h4("Notation warning")
              + p("sin⁻¹x means arcsin x, not 1/sin x. The reciprocal is cosec x. Write arcsin x if the "
                  "distinction matters.")
              + h4("Reading the ranges")
              + p("cos⁻¹(−1/2) = 2π/3, not −π/3: −π/3 is outside the principal range 0 to π, and the inverse "
                  "must return a value inside it."),
              "t8_inverse", examples=["t1n23"], syllabus_item="2.7"),
         card("8.2 Compositions and the range trap",
              h4("Definition")
              + p("sin⁻¹(sin x) = x only when x already lies in the principal range. Outside it, reduce the "
                  "angle first.")
              + h4("Worked examples")
              + p("sin⁻¹(sin 5π/6): 5π/6 = 150° is outside −90° to 90°, but sin 150° = sin 30°, so the answer is "
                  "<b>π/6</b>, not 5π/6. By contrast sin(sin⁻¹ 0.4) = 0.4 always, because 0.4 is in the "
                  "domain.")
              + h4("The complement identity")
              + p("<b>sin⁻¹x + cos⁻¹x = π/2</b> for every x in [−1, 1], and <b>tan⁻¹x + cot⁻¹x = π/2</b>. These "
                  "follow from the cofunction relation sin(π/2 − θ) = cos θ.")
              + h4("Common mistake / conditions")
              + p("Do not cancel sin⁻¹ and sin blindly. Ask first: is the angle inside the principal range? If "
                  "not, use an allied angle to bring it in."),
              "t8_inverse", examples=["t1n24"], syllabus_item="2.7"),
         card("8.3 Sum of two inverse tangents",
              h4("Formula")
              + p("<b>tan⁻¹x + tan⁻¹y = tan⁻¹((x + y)/(1 − xy))</b> when xy &lt; 1, and the answer shifts by π "
                  "when xy &gt; 1 (because the sum passes 90°).")
              + h4("Worked example")
              + p("tan⁻¹1 + tan⁻¹2 + tan⁻¹3: first 1 and 2 give (3)/(1 − 2) = −3, an angle in Q II, so the pair "
                  "sums to π − tan⁻¹3; adding tan⁻¹3 gives <b>π</b>. Numerically 45° + 63.43° + 71.57° = 180° ✓.")
              + h4("Why the condition matters")
              + p("With x = y = 2 the fraction is 4/(1 − 4) = −4/3, a negative number, but both angles are "
                  "positive and their sum is about 126.9°, which is π − tan⁻¹(4/3). Forgetting the π shift is "
                  "the usual error in this question."),
              examples=["t1n25"], syllabus_item="2.7")]},

    {"title": tr("9. Answered Practice (Unit 2 level)"), "items": []},
]

GIVEN = h4("Given and assumptions")
FORMULA = h4("Formula")
STEPS = h4("Step-by-step solution")
CHECK = h4("Interpretation and check")


def num(nid, q, chunks):
    return {"id": nid, "q": tr(q), "a": tr("".join(chunks))}


NUMERICALS = [
    num("t1n1", "Convert 135° into radians and 5π/6 radians into degrees.",
        [GIVEN + p("Use π radians = 180°."),
         FORMULA + p("radians = degrees × π/180;  degrees = radians × 180/π"),
         STEPS + ol("135 × π/180 = 3π/4", "5π/6 × 180/π = 150"),
         CHECK + p("<b>3π/4 and 150°.</b> Check the first: 135° is three quarters of 180°, so three quarters of "
                   "π ✓. A radian answer larger than 2π for an angle under 360° is always wrong.")]),
    num("t1n2", "Find the arc length and the sector area for r = 7 cm and θ = 60°.",
        [GIVEN + p("θ must be in radians before either formula is used: 60° = π/3."),
         FORMULA + p("s = rθ and A = ½r²θ"),
         STEPS + ol("θ = π/3 ≈ 1.0472 rad", "s = 7 × 1.0472 = 7.33 cm",
                    "A = ½ × 49 × 1.0472 = 25.66 cm²"),
         CHECK + p("<b>s ≈ 7.33 cm, A ≈ 25.66 cm².</b> Check the arc: it is one sixth of the circumference "
                   "2π(7) = 43.98, and 43.98/6 = 7.33 ✓.")]),
    num("t1n3", "A wheel of radius 30 cm rotates at 300 rpm. Find its angular speed and the linear speed of a "
                 "point on the rim.",
        [GIVEN + p("300 revolutions per minute; radius 0.30 m."),
         FORMULA + p("ω = rpm × 2π/60 rad/s;  v = rω"),
         STEPS + ol("ω = 300 × 2π/60 = 10π ≈ 31.42 rad/s", "v = 0.30 × 31.42 = 9.42 m/s"),
         CHECK + p("<b>ω ≈ 31.42 rad/s, v ≈ 9.42 m/s.</b> Sanity: 5 revolutions per second means the rim "
                   "travels 5 × 2π(0.30) = 9.42 m each second ✓.")]),
    num("t1n4", "If sin θ = 3/5 and θ lies in the second quadrant, find cos θ and tan θ.",
        [GIVEN + p("θ in Q II: sine positive, cosine and tangent negative."),
         FORMULA + p("sin²θ + cos²θ = 1 and tan θ = sin θ / cos θ"),
         STEPS + ol("cos²θ = 1 − 9/25 = 16/25", "cos θ = −4/5 because Q II makes cosine negative",
                    "tan θ = (3/5)/(−4/5) = −3/4"),
         CHECK + p("<b>cos θ = −4/5, tan θ = −3/4.</b> Check the identity: 9/25 + 16/25 = 1 ✓. The quadrant "
                   "decides the signs; without it the answer is ambiguous.")]),
    num("t1n5", "Evaluate sin 30° cos 60° + cos 30° sin 60°.",
        [GIVEN + p("This is exactly the expansion of sin(A + B) with A = 30°, B = 60°."),
         FORMULA + p("sin(A + B) = sin A cos B + cos A sin B"),
         STEPS + ol("Recognise the pattern: sin(30° + 60°) = sin 90°", "= 1",
                    "Direct check: (1/2)(1/2) + (√3/2)(√3/2) = 1/4 + 3/4 = 1"),
         CHECK + p("<b>1.</b> Recognising the pattern is faster and safer than multiplying decimals. Both routes "
                   "must agree - a mismatch means a wrong standard value.")]),
    num("t1n6", "Evaluate sin²30° + cos²60° + tan²45°.",
        [GIVEN + p("Standard values only; no identity needed, but the first identity can be used as a check."),
         FORMULA + p("sin 30° = 1/2, cos 60° = 1/2, tan 45° = 1"),
         STEPS + ol("(1/2)² = 1/4", "(1/2)² = 1/4", "1² = 1", "1/4 + 1/4 + 1 = 3/2"),
         CHECK + p("<b>3/2 = 1.5.</b> Notice sin²30° + cos²60° = 1/2 only because both angles give 1/2; in "
                   "general sin²θ + cos²θ = 1 uses the <i>same</i> angle.")]),
    num("t1n7", "Write sin(180° + θ), cos(180° − θ) and tan(360° − θ) in terms of θ.",
        [GIVEN + p("Use the quadrant sign plus the unchanged function name (even multiple of 90°)."),
         FORMULA + p("Sign from the quadrant; name stays for 180° and 360°"),
         STEPS + ol("180° + θ is in Q III, sine negative → sin(180° + θ) = −sin θ",
                    "180° − θ is in Q II, cosine negative → cos(180° − θ) = −cos θ",
                    "360° − θ is in Q IV, tangent negative → tan(360° − θ) = −tan θ"),
         CHECK + p("<b>−sin θ, −cos θ and −tan θ.</b> Test with θ = 30°: sin 210° = −0.5 ✓, cos 150° = −0.866 ✓, "
                   "tan 330° = −0.577 ✓.")]),
    num("t1n8", "Evaluate sin 150°, cos 240°, tan 315° and sin(−330°).",
        [GIVEN + p("Reduce each angle with an allied-angle rule first."),
         FORMULA + p("sin(180° − θ) = sin θ, cos(180° + θ) = −cos θ, tan(360° − θ) = −tan θ, sin(−θ) = −sin θ"),
         STEPS + ol("sin 150° = sin 30° = 1/2", "cos 240° = −cos 60° = −1/2",
                    "tan 315° = −tan 45° = −1", "sin(−330°) = −sin 330° = −(−1/2) = 1/2"),
         CHECK + p("<b>1/2, −1/2, −1 and 1/2.</b> Each answer matches the ASTC sign of its quadrant: Q II sine "
                   "positive, Q III cosine negative, Q IV tangent negative, and −330° is coterminal with 30°.")]),
    num("t1n9", "Find sin 75° exactly.",
        [GIVEN + p("75° = 45° + 30°, both standard angles."),
         FORMULA + p("sin(A + B) = sin A cos B + cos A sin B"),
         STEPS + ol("= sin 45 cos 30 + cos 45 sin 30",
                    "= (√2/2)(√3/2) + (√2/2)(1/2)", "= (√6 + √2)/4"),
         CHECK + p("<b>(√6 + √2)/4 ≈ 0.9659.</b> 75° is close to 90°, so its sine should be close to 1 - and "
                   "0.966 is. A calculator gives 0.96593 ✓.")]),
    num("t1n10", "Find cos 15° exactly.",
        [GIVEN + p("15° = 45° − 30°."),
         FORMULA + p("cos(A − B) = cos A cos B + sin A sin B"),
         STEPS + ol("= cos 45 cos 30 + sin 45 sin 30",
                    "= (√2/2)(√3/2) + (√2/2)(1/2)", "= (√6 + √2)/4"),
         CHECK + p("<b>(√6 + √2)/4 ≈ 0.9659.</b> This is the same value as sin 75°, which is expected because "
                   "15° and 75° are complementary: cos 15° = sin 75° ✓.")]),
    num("t1n11", "Find tan 75° in surd form.",
        [GIVEN + p("75° = 45° + 30°."),
         FORMULA + p("tan(A + B) = (tan A + tan B)/(1 − tan A tan B)"),
         STEPS + ol("= (1 + 1/√3)/(1 − 1/√3)", "Multiply top and bottom by √3: (√3 + 1)/(√3 − 1)",
                    "Rationalise: ((√3 + 1)²)/((√3)² − 1²) = (4 + 2√3)/2 = 2 + √3"),
         CHECK + p("<b>2 + √3 ≈ 3.732.</b> Check: tan 75° must exceed tan 60° = 1.732 ✓, and 2 + 1.732 = "
                   "3.732 matches a calculator.")]),
    num("t1n12", "If sin A = 3/5 and cos B = 5/13 with A and B acute, find sin(A + B).",
        [GIVEN + p("Acute angles, so every ratio is positive."),
         FORMULA + p("sin(A + B) = sin A cos B + cos A sin B"),
         STEPS + ol("cos A = √(1 − 9/25) = 4/5", "sin B = √(1 − 25/169) = 12/13",
                    "sin(A + B) = (3/5)(5/13) + (4/5)(12/13)", "= 15/65 + 48/65 = 63/65"),
         CHECK + p("<b>63/65 ≈ 0.969.</b> Both angles are acute so A + B &lt; 180° and the sine is positive ✓. "
                   "The Pythagorean triples 3-4-5 and 5-12-13 make the arithmetic exact.")]),
    num("t1n13", "If sin A = 3/5 with A acute, find sin 2A and cos 2A.",
        [GIVEN + p("cos A = 4/5 from the same triangle."),
         FORMULA + p("sin 2A = 2 sin A cos A;  cos 2A = 1 − 2 sin²A"),
         STEPS + ol("sin 2A = 2(3/5)(4/5) = 24/25", "cos 2A = 1 − 2(9/25) = 7/25"),
         CHECK + p("<b>24/25 and 7/25.</b> Check with the identity: (24/25)² + (7/25)² = (576 + 49)/625 = 1 ✓. "
                   "Since A ≈ 36.87°, 2A ≈ 73.74° lies in Q I, so both values must be positive.")]),
    num("t1n14", "Find cos 2A when cos A = 1/2.",
        [GIVEN + p("Choose the form of cos 2A that uses cos A only."),
         FORMULA + p("cos 2A = 2 cos²A − 1"),
         STEPS + ol("= 2(1/4) − 1", "= 1/2 − 1 = −1/2"),
         CHECK + p("<b>−1/2.</b> A = 60°, so 2A = 120° and cos 120° = −1/2 ✓. Choosing the wrong form "
                   "(1 − 2sin²A) would need sin A first - extra work, same answer.")]),
    num("t1n15", "Find sin 15° using a half-angle formula.",
        [GIVEN + p("15° = 30°/2, so use θ = 30° with the positive root (15° is in Q I)."),
         FORMULA + p("sin(θ/2) = √((1 − cos θ)/2)"),
         STEPS + ol("= √((1 − √3/2)/2)", "= √((2 − √3)/4)", "= √(2 − √3)/2"),
         CHECK + p("<b>√(2 − √3)/2 ≈ 0.2588.</b> Check against the compound formula: sin(45° − 30°) = "
                   "(√6 − √2)/4 ≈ 0.2588 ✓. The two surd forms are equal.")]),
    num("t1n16", "Using the triple-angle formula, evaluate sin 3A when sin A = 1/2 and A is acute.",
        [GIVEN + p("A = 30°, so 3A = 90°; the formula must reproduce sin 90° = 1."),
         FORMULA + p("sin 3A = 3 sin A − 4 sin³A"),
         STEPS + ol("= 3(1/2) − 4(1/8)", "= 1.5 − 0.5", "= 1"),
         CHECK + p("<b>1.</b> The known value of sin 90° confirms the formula. This is a useful exam habit: "
                   "when a formula can be checked against a standard angle, do it.")]),
    num("t1n17", "Find the period of sin 3x, cos(x/2) and tan 2x.",
        [GIVEN + p("Period of sin kx and cos kx is 2π/|k|; of tan kx it is π/|k|."),
         FORMULA + p("T = 2π/|k| for sine and cosine, T = π/|k| for tangent"),
         STEPS + ol("sin 3x: T = 2π/3", "cos(x/2): k = 1/2, T = 2π/(1/2) = 4π", "tan 2x: T = π/2"),
         CHECK + p("<b>2π/3, 4π and π/2.</b> Sanity: the larger the k, the faster the oscillation and the "
                   "smaller the period - sin 3x repeats three times in 2π, so its period is one third of 2π ✓.")]),
    num("t1n18", "For y = 3 sin(2x − π/3) state the amplitude, period, phase shift and range.",
        [GIVEN + p("Compare with y = a sin(bx + c) + d: a = 3, b = 2, c = −π/3, d = 0."),
         FORMULA + p("amplitude |a|, period 2π/|b|, shift −c/b, range d ± |a|"),
         STEPS + ol("Amplitude = 3", "Period = 2π/2 = π", "Shift = π/6 to the right", "Range = −3 to 3"),
         CHECK + p("<b>3, π, π/6 right, [−3, 3].</b> Check one extreme: the maximum 3 occurs when "
                   "2x − π/3 = π/2, that is x = 5π/12, inside the first period ✓.")]),
    num("t1n19", "Find the maximum and minimum of y = 2 + 3 cos x.",
        [GIVEN + p("cos x varies between −1 and 1."),
         FORMULA + p("y = d + a cos x has range d ± |a|"),
         STEPS + ol("Maximum when cos x = 1: y = 2 + 3 = 5", "Minimum when cos x = −1: y = 2 − 3 = −1"),
         CHECK + p("<b>Maximum 5, minimum −1.</b> The centre line is y = 2 and the amplitude 3, so the range is "
                   "2 ± 3 ✓. The maxima occur at x = 0, 2π, … and the minima at x = π, 3π, ….")]),
    num("t1n20", "Express sin 75° + sin 15° as a product and evaluate it.",
        [GIVEN + p("C = 75°, D = 15°, so (C + D)/2 = 45° and (C − D)/2 = 30°."),
         FORMULA + p("sin C + sin D = 2 sin((C + D)/2) cos((C − D)/2)"),
         STEPS + ol("= 2 sin 45° cos 30°", "= 2 × (√2/2) × (√3/2)", "= √6/2"),
         CHECK + p("<b>√6/2 ≈ 1.2247.</b> Direct check: 0.9659 + 0.2588 = 1.2247 ✓. The product form also "
                   "shows why the sum exceeds 1 even though each term is below 1.")]),
    num("t1n21", "Convert 2 sin 40° cos 20° into a sum and evaluate it.",
        [GIVEN + p("A = 40°, B = 20° in the product-to-sum formula."),
         FORMULA + p("2 sin A cos B = sin(A + B) + sin(A − B)"),
         STEPS + ol("= sin 60° + sin 20°", "= 0.8660 + 0.3420", "= 1.2080"),
         CHECK + p("<b>sin 60° + sin 20° ≈ 1.208.</b> Check the product directly: 2(0.6428)(0.9397) = 1.208 ✓.")]),
    num("t1n22", "Simplify (sin A + sin 3A)/(cos A + cos 3A).",
        [GIVEN + p("Convert both sums to products; the common factor should cancel."),
         FORMULA + p("sin C + sin D = 2 sin((C + D)/2) cos((C − D)/2); cos C + cos D = 2 cos((C + D)/2) cos((C − D)/2)"),
         STEPS + ol("Numerator: 2 sin 2A cos(−A) = 2 sin 2A cos A",
                    "Denominator: 2 cos 2A cos(−A) = 2 cos 2A cos A", "Ratio = tan 2A"),
         CHECK + p("<b>tan 2A.</b> Check with A = 20°: numerator = sin 20 + sin 60 = 0.342 + 0.866 = 1.208, "
                   "denominator = cos 20 + cos 60 = 0.940 + 0.500 = 1.440, ratio = 0.839 = tan 40° ✓.")]),
    num("t1n23", "Evaluate sin⁻¹(1/2), cos⁻¹(−1/2) and tan⁻¹(1).",
        [GIVEN + p("Use the principal ranges: sin⁻¹ in [−π/2, π/2], cos⁻¹ in [0, π], tan⁻¹ in (−π/2, π/2)."),
         FORMULA + p("y = sin⁻¹x ⇔ sin y = x within the principal range"),
         STEPS + ol("sin 30° = 1/2 → sin⁻¹(1/2) = π/6", "cos 120° = −1/2 → cos⁻¹(−1/2) = 2π/3",
                    "tan 45° = 1 → tan⁻¹(1) = π/4"),
         CHECK + p("<b>π/6, 2π/3 and π/4.</b> The trap is cos⁻¹(−1/2): −π/3 has the right cosine but lies "
                   "outside 0 to π, so it is not the principal value.")]),
    num("t1n24", "Evaluate sin⁻¹(sin 5π/6).",
        [GIVEN + p("5π/6 = 150° is outside the principal range [−90°, 90°]."),
         FORMULA + p("sin⁻¹(sin x) = x only when x is inside the principal range"),
         STEPS + ol("sin 150° = sin 30° = 1/2", "sin⁻¹(1/2) = π/6",
                    "Therefore sin⁻¹(sin 5π/6) = π/6"),
         CHECK + p("<b>π/6, not 5π/6.</b> Check: sin π/6 = 1/2 = sin 5π/6 ✓, and π/6 is inside the principal "
                   "range. This question exists to test exactly that restriction.")]),
    num("t1n25", "Show that tan⁻¹1 + tan⁻¹2 + tan⁻¹3 = π.",
        [GIVEN + p("Combine the first two with the addition formula, then add the third."),
         FORMULA + p("tan⁻¹x + tan⁻¹y = tan⁻¹((x + y)/(1 − xy)) with a π shift when xy > 1"),
         STEPS + ol("For 1 and 2: (1 + 2)/(1 − 2) = −3, and xy = 2 > 1, so the sum is π − tan⁻¹3",
                    "Add tan⁻¹3: π − tan⁻¹3 + tan⁻¹3 = π"),
         CHECK + p("<b>π.</b> Numerically 45° + 63.43° + 71.57° = 180° ✓. Without the π shift the algebra gives "
                   "tan⁻¹(−3) + tan⁻¹3 = 0, which is clearly wrong for a sum of three positive angles.")]),
    num("t1n26", "The angle of elevation of the top of a tower is 30° from a point 50 m from its base. Find the "
                 "height of the tower.",
        [GIVEN + p("Right triangle: adjacent = 50 m, angle = 30°, opposite = height h."),
         FORMULA + p("tan θ = opposite / adjacent"),
         STEPS + ol("tan 30° = h/50", "h = 50 × tan 30° = 50/√3", "h = 50√3/3 ≈ 28.87 m"),
         CHECK + p("<b>h ≈ 28.87 m.</b> Sanity: tan 30° ≈ 0.577, so the height is a little more than half the "
                   "distance ✓. Rationalise the surd: 50/√3 = 50√3/3.")]),
]

EQUATIONS = [
    {"title": tr("Measurement and ratios"), "items": [
        {"name": tr("Degree to radian"), "f": "radians = degrees × π/180",
         "terms": tr("π radians = 180°; one radian ≈ 57.3°.")},
        {"name": tr("Arc and sector"), "f": "s = rθ,  A = ½r²θ  (θ in radians)",
         "terms": tr("Proportions of the circumference and the circle's area.")},
        {"name": tr("Linear speed"), "f": "v = rω",
         "terms": tr("ω in rad/s; rpm × 2π/60 converts to rad/s.")},
        {"name": tr("Fundamental identity"), "f": "sin²θ + cos²θ = 1",
         "terms": tr("Dividing it by cos²θ gives 1 + tan²θ = sec²θ; by sin²θ gives the cosec form.")},
    ]},
    {"title": tr("Compound and multiple angles"), "items": [
        {"name": tr("Sine of a sum"), "f": "sin(A ± B) = sin A cos B ± cos A sin B",
         "terms": tr("The sign travels with the bracket in the sine formulas.")},
        {"name": tr("Cosine of a sum"), "f": "cos(A ± B) = cos A cos B ∓ sin A sin B",
         "terms": tr("The sign flips in the cosine formulas.")},
        {"name": tr("Tangent of a sum"), "f": "tan(A ± B) = (tan A ± tan B)/(1 ∓ tan A tan B)",
         "terms": tr("Fails when the denominator is zero, i.e. at 90°.")},
        {"name": tr("Double angle"), "f": "sin 2A = 2 sin A cos A;  cos 2A = 1 − 2sin²A",
         "terms": tr("Three equivalent forms for cos 2A - pick the one that fits the given data.")},
        {"name": tr("Triple angle"), "f": "sin 3A = 3 sin A − 4sin³A; cos 3A = 4cos³A − 3 cos A",
         "terms": tr("Built from 2A + A, never memorised blindly.")},
    ]},
    {"title": tr("Graphs, factors and inverses"), "items": [
        {"name": tr("Period"), "f": "sin kx and cos kx: 2π/|k|;  tan kx: π/|k|",
         "terms": tr("Larger k packs more cycles into the same interval.")},
        {"name": tr("Sinusoid"), "f": "y = a sin(bx + c) + d  →  amplitude |a|, shift −c/b",
         "terms": tr("Range is d ± |a|; factor b out before reading the shift.")},
        {"name": tr("Sum to product"), "f": "sin C + sin D = 2 sin((C+D)/2) cos((C−D)/2)",
         "terms": tr("The cosine version has a minus in front for cos C − cos D.")},
        {"name": tr("Product to sum"), "f": "2 sin A cos B = sin(A+B) + sin(A−B)",
         "terms": tr("Turns a product into a sum - the standard first step in simplification.")},
        {"name": tr("Inverse range"), "f": "sin⁻¹: [−π/2, π/2];  cos⁻¹: [0, π];  tan⁻¹: (−π/2, π/2)",
         "terms": tr("The principal range is what makes the inverse single-valued.")},
    ]},
]

VIVA = [
    {"title": tr("Measurement and functions"), "items": [
        {"q": tr("How many radians make 180°?"),
         "a": tr("π radians, so 1 radian ≈ 57.3°.")},
        {"q": tr("Write the arc-length formula and state the unit of θ."),
         "a": tr("s = rθ, with θ in radians.")},
        {"q": tr("Write the sector-area formula."),
         "a": tr("A = ½r²θ, with θ in radians.")},
        {"q": tr("How do you convert rpm into rad/s?"),
         "a": tr("Multiply by 2π/60, because one revolution is 2π radians in 60 seconds.")},
        {"q": tr("State the ASTC rule."),
         "a": tr("Quadrant I all positive, II sin positive, III tan positive, IV cos positive.")},
        {"q": tr("Which functions are positive in the third quadrant?"),
         "a": tr("tan θ and cot θ only, because both coordinates are negative and their ratio is positive.")},
        {"q": tr("Give the three fundamental identities."),
         "a": tr("sin²θ + cos²θ = 1, 1 + tan²θ = sec²θ, 1 + cot²θ = cosec²θ.")},
    ]},
    {"title": tr("Allied and compound angles"), "items": [
        {"q": tr("Write sin(180° − θ)."),
         "a": tr("sin θ: the angle is in Q II where sine is positive, and the name stays.")},
        {"q": tr("Write cos(180° + θ)."),
         "a": tr("−cos θ: Q III makes cosine negative.")},
        {"q": tr("State sin(A + B)."),
         "a": tr("sin A cos B + cos A sin B.")},
        {"q": tr("State cos(A − B)."),
         "a": tr("cos A cos B + sin A sin B - the cosine formula flips the sign.")},
        {"q": tr("State tan(A + B)."),
         "a": tr("(tan A + tan B)/(1 − tan A tan B).")},
        {"q": tr("Why is sin 75° equal to sin 45° cos 30° + cos 45° sin 30°?"),
         "a": tr("Because 75° = 45° + 30° and the compound-angle formula expands sin(A + B).")},
    ]},
    {"title": tr("Multiple angles, graphs, inverses"), "items": [
        {"q": tr("State sin 2A."),
         "a": tr("2 sin A cos A.")},
        {"q": tr("Give the three forms of cos 2A."),
         "a": tr("cos²A − sin²A, 2cos²A − 1 and 1 − 2sin²A.")},
        {"q": tr("State sin 3A."),
         "a": tr("3 sin A − 4 sin³A.")},
        {"q": tr("What is the period of sin 3x?"),
         "a": tr("2π/3, because the frequency is 3.")},
        {"q": tr("What is the amplitude of y = 3 sin(2x − π/3)?"),
         "a": tr("3, the magnitude of the coefficient of the sine.")},
        {"q": tr("Write sin C + sin D as a product."),
         "a": tr("2 sin((C + D)/2) cos((C − D)/2).")},
        {"q": tr("Write 2 sin A cos B as a sum."),
         "a": tr("sin(A + B) + sin(A − B).")},
        {"q": tr("What is the principal range of sin⁻¹?"),
         "a": tr("−π/2 to π/2, inclusive.")},
        {"q": tr("What is sin⁻¹x + cos⁻¹x?"),
         "a": tr("π/2 for every x in [−1, 1].")},
    ]},
]

PRACTICE = [
    ("Convert 210° into radians and 3π/4 radians into degrees.", 3,
     h4("Working") + ol("210 × π/180 = 7π/6", "3π/4 × 180/π = 135°")
     + h4("Answer") + p("<b>7π/6 and 135°.</b> 210° is 30° past 180°, so it must be a little more than π - and "
                        "7π/6 ≈ 1.17π ✓.")),
    ("Find the arc length and sector area for r = 12 cm, θ = 45°.", 4,
     h4("Working") + ol("θ = π/4", "s = 12 × π/4 = 3π ≈ 9.42 cm", "A = ½ × 144 × π/4 = 18π ≈ 56.55 cm²")
     + h4("Check") + p("The arc is one eighth of the circumference 2π(12) = 75.4 cm, and 75.4/8 = 9.42 ✓.")),
    ("If cos θ = −5/13 and θ is in the third quadrant, find sin θ and tan θ.", 4,
     h4("Working") + ol("sin²θ = 1 − 25/169 = 144/169", "In Q III sine is negative: sin θ = −12/13",
                        "tan θ = (−12/13)/(−5/13) = 12/5")
     + h4("Check") + p("25/169 + 144/169 = 1 ✓, and tan is positive in Q III as ASTC predicts ✓.")),
    ("Evaluate tan 120° and cos 315° without a calculator.", 3,
     h4("Working") + p("tan 120° = tan(180° − 60°) = −tan 60° = −√3. cos 315° = cos(360° − 45°) = cos 45° = "
                       "1/√2 = √2/2.")
     + h4("Answer") + p("<b>−√3 and √2/2.</b> Q II gives tangent a negative sign; Q IV gives cosine a positive "
                        "sign.")),
    ("Find cos 105° exactly using a compound angle.", 4,
     h4("Working") + ol("105° = 60° + 45°", "cos(60 + 45) = cos 60 cos 45 − sin 60 sin 45",
                        "= (1/2)(√2/2) − (√3/2)(√2/2) = (√2 − √6)/4")
     + h4("Check") + p("105° is in Q II, so the cosine must be negative: (√2 − √6)/4 ≈ −0.2588 ✓.")),
    ("If tan A = 3/4 and A is acute, find sin 2A and cos 2A.", 4,
     h4("Working") + ol("sin A = 3/5, cos A = 4/5 (3-4-5 triangle)",
                        "sin 2A = 2(3/5)(4/5) = 24/25", "cos 2A = 2(16/25) − 1 = 7/25")
     + h4("Check") + p("(24/25)² + (7/25)² = 1 ✓. A ≈ 36.87°, so 2A ≈ 73.74° is still in Q I and both values "
                       "are positive.")),
    ("Find the period and amplitude of y = 5 cos(3x + π/4).", 3,
     h4("Working") + p("Amplitude = |5| = 5 and period = 2π/3; the phase shift is π/12 to the left because "
                       "c/b = (π/4)/3.")
     + h4("Answer") + p("<b>Amplitude 5, period 2π/3.</b> Range is −5 to 5, centre line y = 0.")),
    ("Express cos 40° − cos 20° as a product.", 4,
     h4("Working") + ol("Use cos C − cos D = −2 sin((C + D)/2) sin((C − D)/2)",
                        "= −2 sin 30° sin 10°", "= −2(1/2) sin 10° = −sin 10°")
     + h4("Check") + p("Numerically: 0.766 − 0.940 = −0.174, and −sin 10° = −0.1736 ✓. The leading minus in the "
                       "cosine formula is what makes the answer negative.")),
    ("Simplify sin 5θ + sin 3θ over cos 5θ + cos 3θ.", 4,
     h4("Working") + ol("Numerator: 2 sin 4θ cos θ", "Denominator: 2 cos 4θ cos θ", "Ratio = tan 4θ")
     + h4("Answer") + p("<b>tan 4θ.</b> The cos θ cancels for every θ where it is not zero, which is why the "
                        "identity holds wherever the original expression is defined.")),
    ("Evaluate sin⁻¹(−1/2), cos⁻¹(1/2) and tan⁻¹(−1).", 3,
     h4("Working") + p("sin⁻¹(−1/2) = −π/6 (principal range −π/2 to π/2). cos⁻¹(1/2) = π/3. tan⁻¹(−1) = −π/4.")
     + h4("Answer") + p("<b>−π/6, π/3, −π/4.</b> Odd inverse functions keep the sign of the input; the cosine "
                        "inverse does not, because its range starts at 0.")),
    ("Find the principal value of cos⁻¹(cos 7π/6).", 4,
     h4("Working") + ol("cos 7π/6 = cos 210° = −√3/2", "cos⁻¹(−√3/2) = 5π/6",
                        "So the answer is 5π/6, not 7π/6")
     + h4("Check") + p("cos 5π/6 = −√3/2 ✓ and 5π/6 lies in [0, π] ✓. 7π/6 is outside the principal range, which "
                       "is exactly why it cannot be the answer.")),
    ("A ladder makes 60° with the ground and reaches 6 m up a wall. How far is its foot from the wall?", 4,
     h4("Working") + ol("tan 60° = 6/d", "d = 6/tan 60° = 6/√3", "d = 2√3 ≈ 3.46 m")
     + h4("Check") + p("The ladder length is 6/sin 60° = 6.93 m, and 3.46² + 6² = 48 = 6.93² ✓.")),
    ("Solve 2 sin²θ − 1 = 0 for 0° ≤ θ ≤ 360°.", 4,
     h4("Working") + ol("sin²θ = 1/2, so sin θ = ±1/√2", "sin θ = +1/√2 → θ = 45°, 135°",
                        "sin θ = −1/√2 → θ = 225°, 315°")
     + h4("Answer") + p("<b>θ = 45°, 135°, 225°, 315°.</b> Four solutions are expected because sine takes each "
                        "value twice per full turn.")),
    ("Find sin 22.5° using a half-angle formula.", 4,
     h4("Working") + ol("22.5° = 45°/2", "sin(θ/2) = √((1 − cos θ)/2) = √((1 − √2/2)/2)",
                        "= √((2 − √2)/4) = √(2 − √2)/2")
     + h4("Check") + p("√(2 − √2)/2 ≈ 0.3827, which is sin 22.5° as a calculator confirms. The positive root is "
                       "correct because 22.5° lies in Q I.")),
    ("Prove that sin 2A/(1 + cos 2A) = tan A.", 4,
     h4("Working") + p("Left side = 2 sin A cos A / (2cos²A), using sin 2A = 2 sin A cos A and "
                       "1 + cos 2A = 2cos²A. Cancel 2 cos A: = sin A/cos A = tan A.")
     + h4("Check") + p("Test A = 30°: left = sin 60/(1 + cos 60) = 0.866/1.5 = 0.577 and tan 30° = 0.577 ✓. "
                       "Choosing the form 1 + cos 2A = 2cos²A is what makes the proof work.")),
]

ANSWERED = {"title": tr("9. Answered Practice (Unit 2 level, suggested marks)"),
            "items": [{"h": tr(f"Practice {i}. {q}"), "body": tr(a)} for i, (q, _m, a) in enumerate(PRACTICE, 1)]}
NOTES[-1] = ANSWERED
EXAM = [{"q": tr("Practice: " + q), "marks": m} for q, m, _ in PRACTICE]
LESSON_COUNT = sum(len(s["items"]) for s in NOTES) - len(ANSWERED["items"])
