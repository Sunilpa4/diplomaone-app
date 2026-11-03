"""DI02000021 Engineering Mathematics - Unit 5: Complex Numbers.

GTU 5.1-5.6, 7 h, 17 %, 12 marks, CO5: the concept and algebra of complex numbers, conjugate, modulus
and inverse, argument and polar form, De Moivre's theorem, and the square root of a complex number
together with the cube roots of unity.
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
    ("Khan Academy - complex numbers: algebra, polar form and De Moivre",
     "https://www.khanacademy.org/math/precalculus/x9e81a4f98389efdf:complex"),
    ("OpenStax - Algebra and Trigonometry, chapter 10 (Complex Numbers in Polar Form)",
     "https://openstax.org/details/books/algebra-and-trigonometry"),
    ("GeoGebra - Argand diagram with modulus and argument",
     "https://www.geogebra.org/m/k3xVjKzT"),
    ("B. S. Grewal - Elementary Engineering Mathematics (Khanna Publishers)",
     "https://www.khannapublishers.in/"),
]

NOTES = [
    {"title": tr("1. The Complex Number"),
     "items": [
         card("1.1 Why a new kind of number",
              h4("The problem")
              + p("The equation x² + 1 = 0 has no real solution, because no real number squares to −1. "
                  "Engineering needs the missing root: a circuit's characteristic equation, a rotation "
                  "matrix and a differential equation all produce it.")
              + h4("The definition")
              + p("Introduce <b>i = √(−1)</b>, so <b>i² = −1</b>. A <b>complex number</b> is "
                  "z = a + ib, where a and b are real.")
              + ul("a is the <b>real part</b>, written Re(z)",
                   "b is the <b>imaginary part</b>, written Im(z)",
                   "if b = 0 the number is real; if a = 0 it is purely imaginary")
              + h4("Examples")
              + p("3 + 4i has Re = 3 and Im = 4. The number −5i is purely imaginary, and 7 is real. "
                  "There is no order: 3 + 4i is neither bigger nor smaller than 1 + i.")
              + h4("Common mistake")
              + p("Writing Im(3 + 4i) = 4i. The imaginary part is the real number 4; the i is part of "
                  "the symbol, not of the number b."),
              syllabus_item="5.1"),
         card("1.2 Powers of i follow a cycle of four",
              h4("The cycle")
              + table(["Power", "Value"],
                      [("i¹", "i"), ("i²", "−1"), ("i³", "−i"), ("i⁴", "1")])
              + p("After four steps the values repeat, so iⁿ depends only on the remainder of n divided "
                  "by 4.")
              + h4("Worked examples")
              + p("i¹⁵: 15 = 4 × 3 + 3, so i¹⁵ = i³ = <b>−i</b>.")
              + p("i²²: 22 = 4 × 5 + 2, so i²² = i² = <b>−1</b>.")
              + h4("Why it works")
              + p("i⁴ = (i²)² = (−1)² = 1, so every group of four powers multiplies by 1 and can be "
                  "dropped.")
              + h4("Common mistake")
              + p("Dividing by 4 and using the quotient instead of the remainder. It is the remainder "
                  "that picks the row of the table."),
              examples=["cm1"], syllabus_item="5.1"),
         card("1.3 The Argand diagram",
              h4("Plotting")
              + p("A complex number a + ib is drawn as the point (a, b): a along the real axis, b along "
                  "the imaginary axis. The plane is called the <b>Argand diagram</b> or the complex "
                  "plane.")
              + h4("Distance and direction")
              + p("The length of the arrow from the origin is the modulus |z| = √(a² + b²), and the "
                  "angle it makes with the real axis is the argument θ.")
              + h4("Useful pictures")
              + ul("The conjugate a − ib is the reflection in the real axis.",
                   "Multiplying by i turns the arrow 90° anticlockwise.",
                   "Adding two numbers completes a parallelogram.")
              + h4("Common mistake")
              + p("Plotting a + ib at (b, a). Real part first, imaginary second - exactly like (x, y)."),
              "n1_argand", syllabus_item="5.1"),
         card("1.4 Equality and finding unknowns",
              h4("The rule")
              + p("Two complex numbers are equal only when both parts match: a + ib = c + id means "
                  "<b>a = c and b = d</b>. One complex equation carries two real equations.")
              + h4("Worked example")
              + p("If (x + 2) + (y − 3)i = 5 + 4i, then x + 2 = 5 and y − 3 = 4, so x = 3 and y = 7.")
              + h4("With a product")
              + p("For (x + iy)(2 + i) = 7 + 4i, expand to (2x − y) + (x + 2y)i = 7 + 4i, then solve "
                  "the pair 2x − y = 7, x + 2y = 4.")
              + h4("Common mistake")
              + p("Comparing only the real parts and forgetting the imaginary equation - half the "
                  "information is then unused."),
              examples=["cm2"], syllabus_item="5.2"),
     ]},

    {"title": tr("2. Algebra of Complex Numbers"),
     "items": [
         card("2.1 Addition and subtraction",
              h4("Rule")
              + p("Add (or subtract) the real parts together and the imaginary parts together: "
                  "(a + ib) ± (c + id) = (a ± c) + i(b ± d).")
              + h4("Worked example")
              + p("(5 − 2i) + (−3 + 4i) = (5 − 3) + (−2 + 4)i = <b>2 + 2i</b>.")
              + p("Subtraction: (5 − 2i) − (−3 + 4i) = 8 − 6i.")
              + h4("Geometric meaning")
              + p("On the Argand diagram the sum is the diagonal of the parallelogram built on the two "
                  "arrows, exactly like vector addition.")
              + h4("Common mistake")
              + p("Adding 3 + 4i and 1 + 2i as 4 + 6i² - the parts combine, they are not multiplied."),
              examples=["cm3"], syllabus_item="5.2"),
         card("2.2 Multiplication",
              h4("Rule")
              + p("Expand like brackets and then replace i² by −1: "
                  "(a + ib)(c + id) = (ac − bd) + i(ad + bc).")
              + h4("Worked example")
              + p("(3 + 2i)(4 − 5i) = 12 − 15i + 8i − 10i² = 12 − 7i + 10 = <b>22 − 7i</b>.")
              + h4("Special products")
              + ul("(a + ib)(a − ib) = a² + b², always real and positive",
                   "(1 + i)² = 2i, a result worth remembering for powers",
                   "i(a + ib) = −b + ia, a rotation through 90°")
              + h4("Common mistake")
              + p("Leaving the answer as 12 − 7i − 10i². The i² must be replaced by −1 before the "
                  "answer is in the form a + ib."),
              examples=["cm4"], syllabus_item="5.2"),
         card("2.3 Division",
              h4("Method")
              + p("Multiply the top and bottom by the <b>conjugate of the denominator</b>. The "
                  "denominator then becomes real, and the answer splits into real and imaginary parts.")
              + h4("Worked example")
              + p("(1 + 2i)/(3 − 4i): multiply by (3 + 4i)/(3 + 4i). The denominator is "
                  "3² + 4² = 25, and the numerator is (1 + 2i)(3 + 4i) = −5 + 10i.")
              + p("So the answer is (−5 + 10i)/25 = <b>−1/5 + (2/5)i</b>.")
              + h4("Why multiply by the conjugate")
              + p("(a + ib)(a − ib) = a² + b² has no i in it, so the denominator clears in one step. "
                  "This is the same trick that rationalises a surd.")
              + h4("Common mistake")
              + p("Multiplying by the denominator itself instead of its conjugate, which leaves the i in "
                  "place."),
              examples=["cm5"], syllabus_item="5.2"),
         card("2.4 Working with powers by repeated squaring",
              h4("The trick")
              + p("For small powers, square instead of expanding: (1 + i)² = 2i, so "
                  "(1 + i)⁴ = (2i)² = −4 and (1 + i)⁶ = (1 + i)⁴(1 + i)² = (−4)(2i) = −8i.")
              + h4("Reading off the parts")
              + p("From −8i the real part is <b>0</b> and the imaginary part is <b>−8</b>.")
              + h4("When to prefer De Moivre")
              + p("Repeated squaring is quick for powers up to about 8. For larger powers, or when the "
                  "answer must be a single number, De Moivre's theorem in section 5 is safer.")
              + h4("Common mistake")
              + p("Squaring a sum term by term: (1 + i)² is 2i, not 1 + i² = 0."),
              examples=["cm20"], syllabus_item="5.2"),
     ]},

    {"title": tr("3. Conjugate, Modulus and Inverse"),
     "items": [
         card("3.1 The conjugate",
              h4("Definition")
              + p("The <b>conjugate</b> of z = a + ib is z̄ = a − ib: same real part, opposite "
                  "imaginary part. On the Argand diagram it is the mirror image in the real axis.")
              + h4("Properties")
              + ul("z + z̄ = 2a, which is twice the real part",
                   "z − z̄ = 2bi, which is twice the imaginary part",
                   "z · z̄ = a² + b², always real and never negative",
                   "the conjugate of a sum is the sum of the conjugates, and the same for a product")
              + h4("Worked example")
              + p("For z = 3 − 4i, the conjugate is 3 + 4i, and z z̄ = 9 + 16 = 25.")
              + h4("Common mistake")
              + p("Changing the sign of the real part instead of the imaginary part."),
              examples=["cm6"], syllabus_item="5.3"),
         card("3.2 The modulus",
              h4("Definition")
              + p("The <b>modulus</b> |z| = √(a² + b²) is the distance of the point from the origin, and "
                  "it is always a non-negative real number.")
              + h4("Worked example")
              + p("|3 − 4i| = √(9 + 16) = <b>5</b>. For z = −1 + i√3, "
                  "|z| = √(1 + 3) = 2.")
              + h4("Properties")
              + ul("|z₁ z₂| = |z₁| |z₂| and |z₁/z₂| = |z₁|/|z₂|",
                   "|z|² = z z̄ = a² + b²",
                   "|z| = 0 only for z = 0")
              + h4("Common mistake")
              + p("Dropping the i before squaring, or forgetting the square root at the end. The answer "
                  "is a plain number, not a complex one."),
              examples=["cm6", "cm7"], syllabus_item="5.3"),
         card("3.3 The multiplicative inverse",
              h4("Formula")
              + p("<b>z⁻¹ = 1/z = z̄/|z|²</b>. Multiplying z by this gives 1, so it really is the "
                  "inverse.")
              + h4("Worked example")
              + p("For z = 3 − 4i, |z|² = 25 and z̄ = 3 + 4i, so z⁻¹ = (3 + 4i)/25 = "
                  "<b>3/25 + (4/25)i</b>.")
              + h4("Check")
              + p("(3 − 4i)(3 + 4i)/25 = 25/25 = 1, so the answer is right.")
              + h4("Common mistake")
              + p("Writing 1/z = 1/a + 1/(ib). The reciprocal of a complex number is not the sum of the "
                  "reciprocals of its parts."),
              examples=["cm5"], syllabus_item="5.3"),
         card("3.4 Division seen as multiplication by the inverse",
              h4("Two views of the same step")
              + p("Dividing z₁ by z₂ means multiplying by z₂⁻¹ = z̄₂/|z₂|², which is exactly the "
                  "'multiply top and bottom by the conjugate' rule of section 2.")
              + h4("Worked example")
              + p("(2 + i)/(1 − i): the conjugate of the bottom is 1 + i and |1 − i|² = 2. The "
                  "numerator becomes (2 + i)(1 + i) = 1 + 3i, so the answer is (1 + 3i)/2 = "
                  "<b>1/2 + (3/2)i</b>.")
              + h4("Useful consequences")
              + p("|z₁/z₂| = |z₁|/|z₂| and the conjugate of a quotient is the quotient of the "
                  "conjugates - both follow at once from this view.")
              + h4("Common mistake")
              + p("Forgetting to divide the whole numerator by |z₂|² after multiplying."),
              examples=["cm5"], syllabus_item="5.3"),
     ]},

    {"title": tr("4. Argument and Polar Form"),
     "items": [
         card("4.1 The argument and its quadrant",
              h4("Definition")
              + p("The <b>argument</b> θ is the angle the arrow makes with the positive real axis, "
                  "measured anticlockwise. The principal value lies between −π and π.")
              + h4("Finding it")
              + p("Compute α = tan⁻¹|b/a| first, then fix the quadrant: first quadrant θ = α, second "
                  "θ = π − α, third θ = −(π − α), fourth θ = −α.")
              + h4("Worked example")
              + p("For z = −1 + i√3, α = tan⁻¹(√3) = π/3 and the point is in the second quadrant, so "
                  "θ = π − π/3 = <b>2π/3</b>.")
              + h4("Common mistake")
              + p("Taking tan⁻¹(b/a) and stopping there. The calculator only returns values between −π/2 "
                  "and π/2, so quadrants 2 and 3 always need the correction."),
              "n2_arg", examples=["cm7"], syllabus_item="5.4"),
         card("4.2 Polar form",
              h4("The form")
              + p("<b>z = r(cos θ + i sin θ) = r cis θ</b>, where r = |z| and θ = arg z. It is the same "
                  "number written by length and direction instead of by coordinates.")
              + h4("Worked example")
              + p("For z = 1 + i: r = √2 and θ = π/4, so z = <b>√2 cis (π/4)</b>.")
              + h4("Converting both ways")
              + ul("Cartesian to polar: r = √(a² + b²), θ from the quadrant rule",
                   "Polar to Cartesian: a = r cos θ and b = r sin θ")
              + h4("Common mistake")
              + p("Mixing the two forms in one answer, such as √2(cos 45° + i) - either write cos and "
                  "sin, or write r cis θ."),
              "n3_polar", examples=["cm8"], syllabus_item="5.4"),
         card("4.3 Worked conversions",
              h4("Third quadrant")
              + p("For z = −3 − 3i: r = √(9 + 9) = 3√2 and the point is in the third quadrant, so "
                  "θ = −(π − π/4) = −3π/4 (the same angle as 5π/4).")
              + p("Hence z = <b>3√2 cis (−3π/4)</b>.")
              + h4("Back to Cartesian")
              + p("4 cis (π/3) = 4(cos 60° + i sin 60°) = 4(1/2 + i√3/2) = <b>2 + 2√3 i</b>.")
              + h4("Choosing the angle")
              + p("Both −3π/4 and 5π/4 describe the same point. The principal value, inside (−π, π], "
                  "is the one normally marked and the one De Moivre works with most cleanly.")
              + h4("Common mistake")
              + p("Using r sin θ for the real part. cos goes with the real axis, sin with the imaginary "
                  "axis."),
              examples=["cm9"], syllabus_item="5.4"),
         card("4.4 Multiplication and division in polar form",
              h4("Rules")
              + ul("multiply: r₁ cis θ₁ × r₂ cis θ₂ = r₁r₂ cis (θ₁ + θ₂)",
                   "divide: r₁ cis θ₁ ÷ r₂ cis θ₂ = (r₁/r₂) cis (θ₁ − θ₂)")
              + p("Multiplying multiplies the lengths and adds the angles; dividing divides the lengths "
                  "and subtracts the angles.")
              + h4("Example")
              + p("(2 cis 30°)(3 cis 50°) = 6 cis 80°, and (6 cis 80°) ÷ (3 cis 50°) = 2 cis 30°, which "
                  "returns the original number.")
              + h4("Why it matters")
              + p("This is the reason phasors work in AC circuits: the product of two phasors is another "
                  "phasor whose angle is the sum.")
              + h4("Common mistake")
              + p("Adding the moduli or multiplying the arguments. It is the other way round."),
              examples=["cm8", "cm9"], syllabus_item="5.4"),
     ]},

    {"title": tr("5. De Moivre's Theorem"),
     "items": [
         card("5.1 The theorem",
              h4("Statement")
              + p("<b>(r cis θ)ⁿ = rⁿ cis (nθ)</b> for every integer n. In cosine form, "
                  "(cos θ + i sin θ)ⁿ = cos nθ + i sin nθ.")
              + h4("Reading it")
              + p("Raise the modulus to the power and multiply the argument by the power. That single "
                  "line replaces pages of binomial expansion.")
              + h4("Why it is true")
              + p("Multiplying by r cis θ adds θ to the argument, so repeating the multiplication n "
                  "times adds θ exactly n times. Induction makes the argument precise.")
              + h4("Routine")
              + ol("Write z in polar form: find r and θ.",
                   "Apply the theorem: modulus rⁿ, argument nθ.",
                   "Bring nθ back into the principal range and finish in a + ib if asked.")
              + h4("Common mistake")
              + p("Raising the angle to the power as well. It is n times θ, not θⁿ."),
              "n5_demoivre", syllabus_item="5.5"),
         card("5.2 Powers in practice",
              h4("Example 1")
              + p("(1 + i)⁸: r = √2 and θ = π/4, so the answer is (√2)⁸ cis (8 × π/4) = 16 cis 2π = "
                  "<b>16</b>.")
              + h4("Example 2")
              + p("(1 − i√3)⁶: r = 2 and θ = −π/3, so the answer is 2⁶ cis (−2π) = 64 cis 0 = <b>64</b>.")
              + h4("Reading the answer")
              + p("When nθ lands on a whole multiple of 2π the answer is real and positive; a half turn "
                  "makes it real and negative; a quarter turn makes it purely imaginary.")
              + h4("Common mistake")
              + p("Adding 2π to the modulus instead of to the argument, or forgetting that a negative "
                  "angle is allowed."),
              examples=["cm10", "cm11"], syllabus_item="5.5"),
         card("5.3 Roots of a complex number",
              h4("Formula")
              + p("The n roots of z are <b>r^(1/n) cis ((θ + 2kπ)/n)</b> for k = 0, 1, …, n − 1. They "
                  "sit on a circle of radius r^(1/n), equally spaced.")
              + h4("Worked example")
              + p("The fourth roots of 16 = 16 cis 0 are 2 cis 0, 2 cis (π/2), 2 cis π and 2 cis (3π/2), "
                  "that is <b>2, 2i, −2, −2i</b>.")
              + h4("Why equally spaced")
              + p("Each root is the previous one multiplied by cis (2π/n), so the angle steps by 360°/n "
                  "- here 90°.")
              + h4("Common mistake")
              + p("Giving only the principal root. An n-th root question expects n answers, unless the "
                  "question says 'principal value'."),
              examples=["cm19"], syllabus_item="5.5"),
         card("5.4 De Moivre inside an equation",
              h4("Example 1: a power")
              + p("(√3 + i)⁴: r = 2 and θ = π/6, so the answer is 16 cis (2π/3) = "
                  "16(−1/2 + i√3/2) = <b>−8 + 8√3 i</b>.")
              + h4("Example 2: solving z³ = 8")
              + p("Write 8 = 8 cis 0, then z = 2 cis (2kπ/3) for k = 0, 1, 2, giving <b>2, 2ω, "
                  "2ω²</b>.")
              + h4("The three roots of any cube")
              + p("The roots of z³ = a³ are a, aω and aω², where ω and ω² are the complex cube roots of "
                  "unity. Recognising this saves the full calculation.")
              + h4("Common mistake")
              + p("Solving z³ = 8 and giving only z = 2. The real cube root is one of three complex "
                  "roots."),
              examples=["cm12"], syllabus_item="5.5"),
     ]},

    {"title": tr("6. Square Roots and the Cube Roots of Unity"),
     "items": [
         card("6.1 The square-root formula",
              h4("Setting it up")
              + p("Let √(a + ib) = x + iy. Squaring gives x² − y² = a and 2xy = b, and also "
                  "x² + y² = r = √(a² + b²). Adding and subtracting the first and third give the "
                  "formula.")
              + h4("The formula")
              + p("<b>√(a + ib) = ±[√((r + a)/2) + i·sign(b)·√((r − a)/2)]</b>, where "
                  "r = √(a² + b²) and sign(b) is + for b > 0 and − for b < 0.")
              + h4("Worked example")
              + p("For 3 + 4i: r = 5, so the real part is √(8/2) = 2 and the imaginary part is "
                  "√(2/2) = 1. Hence √(3 + 4i) = <b>±(2 + i)</b>.")
              + h4("Check")
              + p("(2 + i)² = 4 + 4i − 1 = 3 + 4i, so the answer is right.")
              + h4("Common mistake")
              + p("Reporting only the positive root. Every non-zero complex number has two square "
                  "roots, opposite in sign."),
              examples=["cm13"], syllabus_item="5.6"),
         card("6.2 More square roots",
              h4("Example 1")
              + p("For 8 − 6i: r = 10, so the real part is √(18/2) = 3 and, since b < 0, the imaginary "
                  "part is −√(2/2) = −1. The answer is <b>±(3 − i)</b>.")
              + h4("Example 2")
              + p("For −5 + 12i: r = 13, so the real part is √(8/2) = 2 and the imaginary part is "
                  "√(18/2) = 3. The answer is <b>±(2 + 3i)</b>.")
              + h4("A shortcut")
              + p("For a number of the form a + ib with a² + b² a perfect square, the root has integer "
                  "parts - try small values first, then confirm by squaring.")
              + h4("Common mistake")
              + p("Using r = a² + b² without the square root, which doubles every answer."),
              examples=["cm14", "cm15"], syllabus_item="5.6"),
         card("6.3 The cube roots of unity",
              h4("Solving z³ = 1")
              + p("Write 1 = 1 cis 0. Then z = cis (2kπ/3) for k = 0, 1, 2, giving three roots:")
              + ul("<b>1</b> (k = 0)",
                   "<b>ω = −1/2 + i√3/2</b> (k = 1, argument 120°)",
                   "<b>ω² = −1/2 − i√3/2</b> (k = 2, argument 240°)")
              + h4("The picture")
              + p("All three lie on the unit circle and are 120° apart, with 1 on the real axis. Their "
                  "sum is zero, which is the symmetry you can see in the diagram.")
              + h4("Common mistake")
              + p("Writing ω = 1/2 + i√3/2. The real part is negative: −1/2."),
              "n4_unity", examples=["cm16"], syllabus_item="5.6"),
         card("6.4 Working with ω",
              h4("Three facts")
              + ul("ω³ = 1",
                   "1 + ω + ω² = 0, so ω² = −1 − ω",
                   "ω and ω² are conjugates, and each is the square of the other")
              + h4("Worked example")
              + p("Simplify (1 + ω − ω²)³. Replace ω² by −1 − ω: 1 + ω − ω² = 1 + ω + 1 + ω = "
                  "2(1 + ω) = −2ω².")
              + p("Cubing: (−2ω²)³ = −8ω⁶ = <b>−8</b>, because ω⁶ = (ω³)² = 1.")
              + h4("Why the sum is zero")
              + p("1 + ω + ω² = (ω³ − 1)/(ω − 1) = 0 for ω ≠ 1, since ω³ = 1.")
              + h4("Common mistake")
              + p("Substituting ω = 1 to simplify. ω is a specific complex number, not 1; only ω³ is 1."),
              examples=["cm17", "cm18"], syllabus_item="5.6"),
     ]},

    {"title": tr("7. Exam Routine and Common Mistakes"),
     "items": [
         card("7.1 Five steps for any complex-number question",
              h4("The routine")
              + ol("Write the given number in the form asked for - a + ib or r cis θ.",
                   "For a power or a root, convert to polar form first.",
                   "Apply De Moivre, or the conjugate trick for a quotient.",
                   "Return to a + ib and simplify the angle to the principal range.",
                   "State modulus and argument separately if the question asks for them.")
              + h4("Marks and layout")
              + p("Most schemes award marks for the polar form, the value of rⁿ and the final angle "
                  "separately, so show the conversion even if the arithmetic is short.")
              + h4("Time saver")
              + p("Learn (1 + i)² = 2i, i³ = −i and the three cube roots of unity by heart; between them "
                  "they cover a large share of the questions."),
              syllabus_item="5.6"),
         card("7.2 Mistakes to avoid, and quick checks",
              h4("Six recurring errors")
              + ol("Im(3 + 4i) written as 4i instead of 4.",
                   "Using tan⁻¹(b/a) without the quadrant correction.",
                   "Replacing i² by +1 instead of −1.",
                   "Raising the argument to the power instead of multiplying it.",
                   "Giving one square root or one cube root when two or three exist.",
                   "Writing ω = 1 when simplifying expressions in ω.")
              + h4("Quick checks")
              + p("Verify a square root by squaring it, verify a quotient by multiplying back, and "
                  "verify a power by comparing the modulus (rⁿ) with the size of the answer.")
              + sc("Why does a complex power sometimes come out real?",
                   "Because the new argument nθ is a multiple of π, so the sine term vanishes and only "
                   "the cosine term survives."),
              syllabus_item="5.6"),
     ]},

    {"title": tr("8. Practice Questions with Model Answers"),
     "items": []},  # filled by the builder
]

_NUM = [
    ("cm1", "Simplify i¹⁵.",
     [p("Write the exponent as 4 × 3 + 3, so i¹⁵ = (i⁴)³ · i³."),
      p("Since i⁴ = 1 and i³ = −i, the value is 1 × (−i) = −i."),
      p("The powers of i repeat every four, so only the remainder on division by 4 matters.")]),
    ("cm2", "Find x and y if (x + 2) + (y − 3)i = 5 + 4i.",
     [p("Equate the real parts: x + 2 = 5, so x = 3."),
      p("Equate the imaginary parts: y − 3 = 4, so y = 7."),
      p("Two complex numbers are equal only when both parts agree, which is why one equation gives two "
        "real conditions.")]),
    ("cm3", "Add and subtract 5 − 2i and −3 + 4i.",
     [p("Add the real parts and the imaginary parts separately: (5 − 3) + (−2 + 4)i = 2 + 2i."),
      p("Subtract: (5 + 3) + (−2 − 4)i = 8 − 6i."),
      p("On the Argand diagram the sum is the diagonal of the parallelogram on the two arrows.")]),
    ("cm4", "Multiply (3 + 2i)(4 − 5i).",
     [p("Expand: 12 − 15i + 8i − 10i²."),
      p("Use i² = −1, so −10i² = +10: the expression becomes 12 − 7i + 10."),
      p("The answer is 22 − 7i, with real part 22 and imaginary part −7.")]),
    ("cm5", "Divide (1 + 2i) by (3 − 4i).",
     [p("Multiply top and bottom by the conjugate 3 + 4i."),
      p("Denominator: (3 − 4i)(3 + 4i) = 9 + 16 = 25. Numerator: (1 + 2i)(3 + 4i) = 3 + 4i + 6i + "
        "8i² = −5 + 10i."),
      p("So the quotient is (−5 + 10i)/25 = −1/5 + (2/5)i.")]),
    ("cm6", "Find the conjugate and the modulus of z = 3 − 4i.",
     [p("The conjugate keeps the real part and flips the imaginary part: z̄ = 3 + 4i."),
      p("The modulus is the distance from the origin: |z| = √(3² + (−4)²) = √25 = 5."),
      p("Check with the product: z z̄ = 9 + 16 = 25 = |z|², as the theory requires.")]),
    ("cm7", "Find the modulus and argument of z = −1 + i√3.",
     [p("Modulus: |z| = √(1 + 3) = 2."),
      p("The point (−1, √3) lies in the second quadrant, and α = tan⁻¹(√3) = π/3."),
      p("For the second quadrant θ = π − α = π − π/3 = 2π/3."),
      p("So z = 2 cis (2π/3).")]),
    ("cm8", "Express 1 + i in polar form.",
     [p("Modulus: r = √(1 + 1) = √2."),
      p("The point (1, 1) is in the first quadrant, so θ = tan⁻¹(1) = π/4."),
      p("Hence 1 + i = √2 (cos π/4 + i sin π/4) = √2 cis (π/4).")]),
    ("cm9", "Express −3 − 3i in polar form.",
     [p("Modulus: r = √(9 + 9) = √18 = 3√2."),
      p("The point is in the third quadrant and α = tan⁻¹(1) = π/4, so θ = −(π − π/4) = −3π/4."),
      p("Hence z = 3√2 cis (−3π/4), the same angle as 5π/4 if a positive argument is preferred.")]),
    ("cm10", "Evaluate (1 + i)⁸ using De Moivre's theorem.",
     [p("Polar form: 1 + i = √2 cis (π/4)."),
      p("De Moivre: (√2 cis π/4)⁸ = (√2)⁸ cis (8 × π/4) = 16 cis 2π."),
      p("Since cos 2π = 1 and sin 2π = 0, the answer is 16.")]),
    ("cm11", "Evaluate (1 − i√3)⁶.",
     [p("Modulus √(1 + 3) = 2, and the fourth-quadrant angle is θ = −π/3, so z = 2 cis (−π/3)."),
      p("De Moivre gives 2⁶ cis (−6π/3) = 64 cis (−2π)."),
      p("A full turn gives cos(−2π) = 1 and sin(−2π) = 0, so the answer is 64.")]),
    ("cm12", "Evaluate (√3 + i)⁴.",
     [p("Modulus √(3 + 1) = 2 and θ = tan⁻¹(1/√3) = π/6, so z = 2 cis (π/6)."),
      p("Then z⁴ = 16 cis (4π/6) = 16 cis (2π/3)."),
      p("Now cos 2π/3 = −1/2 and sin 2π/3 = √3/2, so the answer is −8 + 8√3 i.")]),
    ("cm13", "Find the square roots of 3 + 4i.",
     [p("Here a = 3, b = 4, r = √(9 + 16) = 5."),
      p("Real part: √((r + a)/2) = √(8/2) = 2. Imaginary part: √((r − a)/2) = √(2/2) = 1, positive "
        "because b > 0."),
      p("So √(3 + 4i) = ±(2 + i). Check: (2 + i)² = 4 + 4i − 1 = 3 + 4i.")]),
    ("cm14", "Find the square roots of 8 − 6i.",
     [p("a = 8, b = −6, so r = √(64 + 36) = 10."),
      p("Real part: √((10 + 8)/2) = √9 = 3. Since b < 0 the imaginary part is negative: −√((10 − 8)/2) "
        "= −1."),
      p("The roots are ±(3 − i). Check: (3 − i)² = 9 − 6i − 1 = 8 − 6i.")]),
    ("cm15", "Find the square roots of −5 + 12i.",
     [p("a = −5, b = 12, so r = √(25 + 144) = 13."),
      p("Real part: √((13 − 5)/2) = √4 = 2. Imaginary part: √((13 + 5)/2) = √9 = 3, positive because "
        "b > 0."),
      p("The roots are ±(2 + 3i). Check: (2 + 3i)² = 4 + 12i − 9 = −5 + 12i.")]),
    ("cm16", "Solve z³ = 1 and write all three roots.",
     [p("Write 1 = 1 cis 0. By De Moivre the roots are z = cis (2kπ/3) for k = 0, 1, 2."),
      p("k = 0 gives 1; k = 1 gives cis (2π/3) = −1/2 + i√3/2 = ω; k = 2 gives cis (4π/3) = "
        "−1/2 − i√3/2 = ω²."),
      p("All three lie on the unit circle at 120° intervals, and their sum is 1 + ω + ω² = 0.")]),
    ("cm17", "Simplify (1 + ω²)³, where ω is a complex cube root of unity.",
     [p("From 1 + ω + ω² = 0 we get ω² = −1 − ω, so 1 + ω² = −ω."),
      p("Cubing: (−ω)³ = −ω³."),
      p("Since ω³ = 1, the value is −1.")]),
    ("cm18", "Simplify (1 + ω − ω²)³.",
     [p("Replace ω² by −1 − ω: 1 + ω − ω² = 1 + ω + 1 + ω = 2 + 2ω = 2(1 + ω)."),
      p("But 1 + ω = −ω², so the bracket is −2ω²."),
      p("Cubing: (−2ω²)³ = −8ω⁶, and ω⁶ = (ω³)² = 1, so the value is −8.")]),
    ("cm19", "Find all fourth roots of 16.",
     [p("Write 16 = 16 cis 0, then the roots are 16^(1/4) cis (2kπ/4) = 2 cis (kπ/2) for k = 0, 1, 2, "
        "3."),
      p("k = 0 gives 2, k = 1 gives 2i, k = 2 gives −2 and k = 3 gives −2i."),
      p("They lie on the circle of radius 2 at 90° intervals, so each is the previous one multiplied by "
        "i.")]),
    ("cm20", "Find the real and imaginary parts of (1 + i)⁶.",
     [p("Use (1 + i)² = 2i, so (1 + i)⁶ = (2i)³ = 8i³."),
      p("Since i³ = −i, the value is −8i."),
      p("Therefore the real part is 0 and the imaginary part is −8: the number is purely imaginary.")]),
]

NUMERICALS = [{"id": i, "q": tr(q), "a": tr("".join(parts))} for i, q, parts in _NUM]

EQUATIONS = [
    {"title": tr("Definitions and algebra"),
     "items": [
         {"terms": tr("Imaginary unit"), "a": tr("i = √(−1),  i² = −1")},
         {"terms": tr("Complex number"), "a": tr("z = a + ib,  a = Re z,  b = Im z")},
         {"terms": tr("Equality"), "a": tr("a + ib = c + id  ⇔  a = c and b = d")},
         {"terms": tr("Addition"), "a": tr("(a + ib) ± (c + id) = (a ± c) + i(b ± d)")},
         {"terms": tr("Multiplication"), "a": tr("(a + ib)(c + id) = (ac − bd) + i(ad + bc)")},
         {"terms": tr("Powers of i"), "a": tr("i¹ = i, i² = −1, i³ = −i, i⁴ = 1, repeating")},
     ]},
    {"title": tr("Conjugate, modulus, polar form"),
     "items": [
         {"terms": tr("Conjugate"), "a": tr("z̄ = a − ib ;  z z̄ = a² + b²")},
         {"terms": tr("Modulus"), "a": tr("|z| = √(a² + b²) ;  |z₁z₂| = |z₁||z₂|")},
         {"terms": tr("Inverse"), "a": tr("z⁻¹ = z̄/|z|²")},
         {"terms": tr("Polar form"), "a": tr("z = r(cos θ + i sin θ) = r cis θ")},
         {"terms": tr("Argument"), "a": tr("θ = tan⁻¹(b/a) adjusted for the quadrant, −π < θ ≤ π")},
         {"terms": tr("Product and quotient"), "a": tr("r₁r₂ cis (θ₁ + θ₂) ;  (r₁/r₂) cis (θ₁ − θ₂)")},
     ]},
    {"title": tr("De Moivre and roots"),
     "items": [
         {"terms": tr("De Moivre"), "a": tr("(r cis θ)ⁿ = rⁿ cis (nθ)")},
         {"terms": tr("n-th roots"), "a": tr("r^(1/n) cis ((θ + 2kπ)/n),  k = 0, 1, …, n − 1")},
         {"terms": tr("Square root"), "a": tr("√(a + ib) = ±[√((r + a)/2) + i·sign(b)√((r − a)/2)]")},
         {"terms": tr("Cube roots of unity"), "a": tr("1, ω = −1/2 + i√3/2, ω² = −1/2 − i√3/2")},
         {"terms": tr("Properties of ω"), "a": tr("ω³ = 1 and 1 + ω + ω² = 0")},
         {"terms": tr("Roots of z³ = a³"), "a": tr("a, aω, aω²")},
     ]},
]

VIVA = [
    {"title": tr("Basics"),
     "items": [
         {"q": tr("What is a complex number?"),
          "a": tr("A number of the form a + ib with a and b real; a is the real part and b the imaginary "
                  "part.")},
         {"q": tr("Why do we need complex numbers?"),
          "a": tr("Because equations such as x² + 1 = 0 have no real root, and rotations, AC circuits "
                  "and vibrations are described most simply with them.")},
         {"q": tr("What is the value of i²?"),
          "a": tr("−1, since i = √(−1).")},
         {"q": tr("What is the imaginary part of 3 + 4i?"),
          "a": tr("4 - the imaginary part is the real coefficient b, not 4i.")},
         {"q": tr("How many complex roots does z³ = 1 have?"),
          "a": tr("Three: 1, ω and ω², all on the unit circle 120° apart.")},
         {"q": tr("Can two complex numbers be compared as larger or smaller?"),
          "a": tr("No - the complex numbers have no order, although their moduli can be compared.")},
     ]},
    {"title": tr("Conjugate, modulus, polar form"),
     "items": [
         {"q": tr("Define the conjugate of z = a + ib."),
          "a": tr("z̄ = a − ib, the reflection of z in the real axis.")},
         {"q": tr("What is z z̄?"),
          "a": tr("a² + b² = |z|², a non-negative real number.")},
         {"q": tr("Define the modulus and give its geometric meaning."),
          "a": tr("|z| = √(a² + b²), the distance of the point (a, b) from the origin.")},
         {"q": tr("Write the inverse of z in terms of the conjugate."),
          "a": tr("z⁻¹ = z̄/|z|², valid for every z ≠ 0.")},
         {"q": tr("How is division of complex numbers performed?"),
          "a": tr("Multiply the numerator and denominator by the conjugate of the denominator, so the "
                  "denominator becomes real.")},
         {"q": tr("How do you find the argument of a complex number?"),
          "a": tr("Take α = tan⁻¹|b/a| and then adjust for the quadrant: θ = α, π − α, −(π − α) or −α.")},
     ]},
    {"title": tr("De Moivre and roots"),
     "items": [
         {"q": tr("State De Moivre's theorem."),
          "a": tr("(r cis θ)ⁿ = rⁿ cis (nθ) for any integer n.")},
         {"q": tr("How do you multiply two numbers in polar form?"),
          "a": tr("Multiply the moduli and add the arguments: r₁r₂ cis (θ₁ + θ₂).")},
         {"q": tr("How many n-th roots does a non-zero complex number have?"),
          "a": tr("Exactly n, equally spaced on a circle of radius r^(1/n).")},
         {"q": tr("What are the cube roots of unity?"),
          "a": tr("1, ω = −1/2 + i√3/2 and ω² = −1/2 − i√3/2.")},
         {"q": tr("Why is 1 + ω + ω² = 0?"),
          "a": tr("Because ω³ = 1 and ω ≠ 1, so 1 + ω + ω² = (ω³ − 1)/(ω − 1) = 0.")},
         {"q": tr("How do you find the square root of a + ib?"),
          "a": tr("Let it be x + iy; use x² − y² = a, 2xy = b and x² + y² = r to obtain "
                  "x = √((r + a)/2) and y = ±√((r − a)/2).")},
     ]},
]

_PRACTICE = [
    ("Simplify i²¹ + i³⁶.", 3,
     [p("Reduce each power modulo 4: 21 = 4 × 5 + 1, so i²¹ = i¹ = i."),
      p("36 = 4 × 9, so i³⁶ = (i⁴)⁹ = 1, because any power of i⁴ is 1."),
      p("The sum is i + 1 = 1 + i, which is already in the standard form a + ib with a = 1 and b = "
        "1.")]),
    ("Find x and y if (x − 2) + (y + 5)i = 3 − 2i.", 3,
     [p("Equate the real parts: x − 2 = 3, so x = 5."),
      p("Equate the imaginary parts: y + 5 = −2, so y = −7."),
      p("Answer: x = 5, y = −7. One complex equation gives two real equations, which is why two "
        "unknowns can be found.")]),
    ("For z₁ = 4 − 3i and z₂ = −2 + 5i, find z₁ + z₂ and z₁z₂.", 4,
     [p("Sum: (4 − 2) + (−3 + 5)i = 2 + 2i."),
      p("Product: (4 − 3i)(−2 + 5i) = −8 + 20i + 6i − 15i² = −8 + 26i + 15."),
      p("So z₁z₂ = 7 + 26i, and both answers are in the standard form a + ib.")]),
    ("Divide (2 + 3i) by (4 − i).", 4,
     [p("Multiply top and bottom by the conjugate 4 + i."),
      p("Denominator: (4 − i)(4 + i) = 16 + 1 = 17."),
      p("Numerator: (2 + 3i)(4 + i) = 8 + 2i + 12i + 3i² = 5 + 14i."),
      p("The quotient is (5 + 14i)/17 = 5/17 + (14/17)i.")]),
    ("Find the conjugate and modulus of z = 6 − 8i.", 3,
     [p("The conjugate flips the imaginary part: z̄ = 6 + 8i."),
      p("The modulus is √(6² + 8²) = √100 = 10."),
      p("Check: z z̄ = 36 + 64 = 100 = |z|², which confirms both numbers.")]),
    ("Express −1 − i in polar form.", 4,
     [p("Modulus: r = √(1 + 1) = √2."),
      p("The point (−1, −1) is in the third quadrant, and α = tan⁻¹(1) = π/4, so θ = −(π − π/4) = "
        "−3π/4."),
      p("Hence −1 − i = √2 cis (−3π/4), equivalently √2 cis (5π/4) with a positive angle.")]),
    ("Express 2 + 2√3 i in polar form.", 4,
     [p("Modulus: r = √(4 + 12) = 4."),
      p("The point is in the first quadrant and tan θ = 2√3/2 = √3, so θ = π/3."),
      p("Therefore 2 + 2√3 i = 4 cis (π/3), and converting back gives 4(1/2 + i√3/2) = 2 + 2√3 i, "
        "which checks the answer.")]),
    ("Evaluate (1 − i)⁶ using De Moivre's theorem.", 4,
     [p("Polar form: r = √2 and θ = −π/4, so 1 − i = √2 cis (−π/4)."),
      p("De Moivre: (√2)⁶ cis (6 × (−π/4)) = 8 cis (−3π/2)."),
      p("cos(−3π/2) = 0 and sin(−3π/2) = 1, so the value is 8i - purely imaginary.")]),
    ("Evaluate (1 + i√3)⁶.", 4,
     [p("Modulus r = √(1 + 3) = 2 and θ = tan⁻¹(√3) = π/3, so z = 2 cis (π/3)."),
      p("Then z⁶ = 2⁶ cis (6 × π/3) = 64 cis 2π."),
      p("A full turn brings the point back to the real axis, so the answer is 64.")]),
    ("Evaluate (1 − i)⁴.", 3,
     [p("Square first: (1 − i)² = 1 − 2i + i² = −2i."),
      p("Square again: (−2i)² = 4i² = −4."),
      p("So (1 − i)⁴ = −4, a real number, which matches De Moivre with the angle −π making a half "
        "turn.")]),
    ("Find the square roots of 8 + 6i.", 4,
     [p("Here a = 8, b = 6 and r = √(64 + 36) = 10."),
      p("Real part: √((10 + 8)/2) = √9 = 3. Imaginary part: √((10 − 8)/2) = 1, positive since b > 0."),
      p("The roots are ±(3 + i). Check: (3 + i)² = 9 + 6i − 1 = 8 + 6i.")]),
    ("Find the square roots of −15 − 8i.", 4,
     [p("Here a = −15, b = −8 and r = √(225 + 64) = 17."),
      p("Real part: √((17 − 15)/2) = 1. Imaginary part: −√((17 + 15)/2) = −4, negative because b < 0."),
      p("The roots are ±(1 − 4i). Check: (1 − 4i)² = 1 − 8i + 16i² = −15 − 8i.")]),
    ("Solve z³ = 1 and verify that the three roots add to zero.", 4,
     [p("Writing 1 = 1 cis 0, the roots are cis (2kπ/3) for k = 0, 1, 2, that is 1, ω = −1/2 + i√3/2 and "
        "ω² = −1/2 − i√3/2."),
      p("Sum of the real parts: 1 − 1/2 − 1/2 = 0. Sum of the imaginary parts: √3/2 − √3/2 = 0."),
      p("So 1 + ω + ω² = 0, as expected from (ω³ − 1)/(ω − 1) = 0. Each root also has modulus 1 and "
        "they are 120° apart.")]),
    ("Simplify (1 + ω − ω²)³, where ω³ = 1 and 1 + ω + ω² = 0.", 4,
     [p("Use ω² = −1 − ω: then 1 + ω − ω² = 1 + ω + 1 + ω = 2(1 + ω)."),
      p("But 1 + ω = −ω², so the bracket equals −2ω²."),
      p("Cubing: (−2ω²)³ = −8ω⁶ = −8(ω³)² = −8, because ω³ = 1.")]),
    ("Find all cube roots of 27.", 4,
     [p("Write 27 = 27 cis 0, so the cube roots are 3 cis (2kπ/3) for k = 0, 1, 2."),
      p("That gives 3, 3ω and 3ω², with ω = −1/2 + i√3/2."),
      p("Explicitly: 3, −3/2 + (3√3/2)i and −3/2 − (3√3/2)i. Each has modulus 3 and they are 120° "
        "apart; cubing any of them returns 27.")]),
]

EXAM = [{"q": tr(q), "marks": m} for q, m, _parts in _PRACTICE]
PRACTICE_ANSWERS = [tr("".join(parts)) for _q, _m, parts in _PRACTICE]

LESSON_COUNT = sum(len(s["items"]) for s in NOTES)
