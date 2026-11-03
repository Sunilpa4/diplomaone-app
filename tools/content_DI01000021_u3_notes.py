"""DI01000021 Mathematics-I - Unit 3: Vectors (GTU 3.1-3.4, 9 h, 20 %, 14 marks).

Vectors and their algebra, the scalar and vector products with properties, the angle between two vectors,
and the two engineering applications the syllabus names: work done and moment of force.
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
    ("Khan Academy - vectors, dot product and cross product",
     "https://www.khanacademy.org/math/linear-algebra/vectors-and-spaces"),
    ("GeoGebra 3D - build two vectors and watch the cross product",
     "https://www.geogebra.org/3d"),
    ("OpenStax - University Physics Volume 1, chapter 2 (vectors) and chapter 10 (torque)",
     "https://openstax.org/details/books/university-physics-volume-1"),
    ("Narayan Shanti, Mittal P.K - A Text Book of Vector Analysis (S. Chand)",
     "https://www.schandpublishing.com/"),
]

NOTES = [
    {"title": tr("1. Vectors and their Representation"),
     "items": [
         card("1.1 Scalar or vector: the first question",
              h4("Definition")
              + p("A <b>scalar</b> has size only (mass, time, temperature, work). A <b>vector</b> has size "
                  "<i>and</i> direction (displacement, velocity, acceleration, force, momentum).")
              + h4("Notation")
              + ul("A vector is written <b>a</b> (bold) or with an arrow above it; its magnitude is |a| or a.",
                   "Geometrically a vector is a directed line segment: length = magnitude, arrow = direction.",
                   "A vector is unchanged by moving it parallel to itself - only length and direction matter.",
                   "Equal vectors have the same magnitude and direction; they need not start at the same point.")
              + h4("Worked example")
              + p("A displacement of 5 m east is a vector; 5 m is its magnitude and east is its direction. "
                  "Saying \"the car went 60 km\" describes a scalar, while \"60 km north\" describes a vector."),
              "v1_vector", examples=["v1n1"], syllabus_item="3.1"),
         card("1.2 Magnitude, unit vector and direction cosines",
              h4("Definition")
              + p("For a = a₁i + a₂j + a₃k the <b>magnitude</b> is |a| = √(a₁² + a₂² + a₃²) - Pythagoras in "
                  "three dimensions. The <b>unit vector</b> a-hat = a/|a| has length 1 and points the same way.")
              + h4("Direction cosines")
              + p("The angles α, β, γ that a makes with the x, y and z axes have cosines cos α = a₁/|a|, "
                  "cos β = a₂/|a|, cos γ = a₃/|a|, and <b>cos²α + cos²β + cos²γ = 1</b>.")
              + h4("Worked example")
              + p("For a = 2i + 3j − 6k: |a| = √(4 + 9 + 36) = 7, so a-hat = (2i + 3j − 6k)/7 and the "
                  "direction cosines are 2/7, 3/7, −6/7. Check: (4 + 9 + 36)/49 = 1 ✓.")
              + h4("Common mistake / conditions")
              + p("Divide every component by the same magnitude. A unit vector must come out with length 1 - "
                  "square its components as a check before moving on."),
              "v1_vector", examples=["v1n1", "v1n2", "v1n3"], syllabus_item="3.1"),
         card("1.3 Types of vectors you will meet",
              h4("The vocabulary")
              + table(["Name", "Meaning", "Example"],
                      [("Zero (null)", "magnitude 0, no direction", "a − a = 0"),
                       ("Unit", "magnitude exactly 1", "i, j, k"),
                       ("Equal", "same magnitude and direction", "AB and CD in a parallelogram"),
                       ("Negative of a", "same length, opposite direction", "−a"),
                       ("Collinear", "parallel, so one is a scalar multiple of the other", "2i + 4j and i + 2j"),
                       ("Coplanar", "all lie in one plane", "any three vectors with zero scalar triple product")])
              + h4("Why the vocabulary matters")
              + p("Two vectors are parallel exactly when their cross product is zero, and perpendicular exactly "
                  "when their dot product is zero. Those two sentences answer a large share of the paper."),
              examples=["v1n4"], syllabus_item="3.1")]},

    {"title": tr("2. Algebra of Vectors"),
     "items": [
         card("2.1 Addition: triangle and parallelogram laws",
              h4("Definition")
              + p("<b>Triangle law:</b> place the tail of b at the head of a; then a + b runs from the tail of a "
                  "to the head of b. <b>Parallelogram law:</b> if a and b are adjacent sides, a + b is the "
                  "diagonal through the common point.")
              + h4("Properties")
              + ul("Commutative: a + b = b + a.",
                   "Associative: (a + b) + c = a + (b + c).",
                   "Zero vector: a + 0 = a.",
                   "Addition is done component by component in i, j, k form.")
              + h4("Worked example")
              + p("a = 2i + 3j − k and b = i − 2j + 4k give a + b = <b>3i + j + 3k</b> and |a + b| = "
                  "√(9 + 1 + 9) = √19 ≈ 4.36.")
              + h4("Common mistake / conditions")
              + p("Magnitudes do not add like numbers: |a + b| = 4.36 while |a| + |b| = 3.74 + 4.58 = 8.32. "
                  "The triangle inequality only promises |a + b| ≤ |a| + |b|."),
              "v2_add", examples=["v1n4"], syllabus_item="3.1"),
         card("2.2 Subtraction and position vectors",
              h4("Definition")
              + p("a − b = a + (−b): reverse b, then add. In components subtract directly. The vector from "
                  "point A to point B is <b>AB = OB − OA</b> (head minus tail).")
              + h4("Worked examples")
              + p("With the vectors above, a − b = <b>i + 5j − 5k</b>, of magnitude √51 ≈ 7.14.")
              + p("For A(1, 2, 3) and B(4, 6, 3): AB = (4 − 1)i + (6 − 2)j + (3 − 3)k = 3i + 4j + 0k, so "
                  "|AB| = 5 - the distance formula in three dimensions.")
              + h4("Common mistake / conditions")
              + p("Subtract in the order head minus tail. AB and BA are negatives of each other; choosing the "
                  "wrong order flips every sign and usually the final answer's sign too."),
              "v2_add", examples=["v1n22"], syllabus_item="3.1"),
         card("2.3 Components, i j k form and scalar multiplication",
              h4("Definition")
              + p("i, j, k are unit vectors along x, y, z. Any vector is <b>a = a₁i + a₂j + a₃k</b>, where the "
                  "components are the projections on the three axes.")
              + h4("Rules")
              + table(["Operation", "Rule", "Example"],
                      [("Scalar multiple", "k(a₁i + a₂j + a₃k) = ka₁i + ka₂j + ka₃k", "3(2i − j) = 6i − 3j"),
                       ("Addition", "add matching components", "(2i + j) + (i + 4j) = 3i + 5j"),
                       ("Magnitude", "√(a₁² + a₂² + a₃²)", "|3i + 4j| = 5"),
                       ("Parallel test", "b = k a for some scalar k", "(2, 4) = 2(1, 2)")])
              + h4("Worked example")
              + p("If a = i − 2j + 3k and b = 2i + j − k, then 2a − 3b = (2 − 6)i + (−4 − 3)j + (6 + 3)k = "
                  "<b>−4i − 7j + 9k</b>, of magnitude √(16 + 49 + 81) = √146 ≈ 12.08."),
              examples=["v1n20", "v1n21"], syllabus_item="3.1")]},

    {"title": tr("3. Scalar (Dot) Product"),
     "items": [
         card("3.1 Definition and properties",
              h4("Definition")
              + p("<b>a · b = |a||b| cos θ</b>, where θ is the angle between the vectors (0° to 180°). The "
                  "answer is a <b>scalar</b> - a number, not a vector.")
              + h4("In components")
              + p("<b>a · b = a₁b₁ + a₂b₂ + a₃b₃</b>. Multiply matching components and add: this is why the dot "
                  "product is easy in i, j, k form.")
              + h4("Properties")
              + ul("Commutative: a · b = b · a.",
                   "Distributive: a · (b + c) = a · b + a · c.",
                   "a · a = |a|², so |a| = √(a · a).",
                   "i · i = j · j = k · k = 1 and i · j = j · k = k · i = 0.",
                   "a · b = 0 ⇔ a and b are perpendicular (or one is zero).")
              + h4("Worked example")
              + p("(i + 2j + 3k) · (4i − 5j + 6k) = 4 − 10 + 18 = <b>12</b>."),
              "v3_dot", examples=["v1n6", "v1n8"], syllabus_item="3.2"),
         card("3.2 Angle between two vectors",
              h4("Formula")
              + p("<b>cos θ = (a · b)/(|a||b|)</b>, so θ = cos⁻¹ of that value. The formula is just the "
                  "definition rearranged.")
              + h4("Procedure")
              + ol("Compute a · b in components.",
                   "Compute |a| and |b| separately.",
                   "Divide, then take the inverse cosine - keep the answer in degrees or radians as asked.")
              + h4("Worked example")
              + p("a = 2i − j + k and b = i + j + 2k: a · b = 2 − 1 + 2 = 3, |a| = |b| = √6, so cos θ = 3/6 = "
                  "1/2 and <b>θ = 60°</b>.")
              + h4("Common mistake / conditions")
              + p("If cos θ comes out negative, θ is obtuse - do not \"fix\" the sign. A zero dot product means "
                  "90°, and cos⁻¹(1) = 0° means the vectors are parallel in the same direction."),
              "v5_angle", examples=["v1n5", "v1n7", "v1n23"], syllabus_item="3.3"),
         card("3.3 Projection and the perpendicularity condition",
              h4("Definition")
              + p("The <b>scalar projection</b> of a on b is the length of a's shadow along b: "
                  "<b>(a · b)/|b|</b>. The vector projection is that length times the unit vector b-hat.")
              + h4("Geometry")
              + p("In a · b = |a||b| cos θ, the factor |a| cos θ is exactly the projection of a on b. That is "
                  "why work is F · d: only the component of force along the displacement does work.")
              + h4("Worked example")
              + p("Projection of a = 3i + j − 2k on b = i + j + k: a · b = 3 + 1 − 2 = 2 and |b| = √3, so the "
                  "projection is <b>2/√3 ≈ 1.155</b>.")
              + h4("Finding an unknown")
              + p("If 2i + λj + k must be perpendicular to i − 2j + 3k, set the dot product to zero: "
                  "2 − 2λ + 3 = 0, so λ = 5/2. One equation, one unknown - always the same pattern."),
              "v3_dot", examples=["v1n9", "v1n8"], syllabus_item="3.2")]},

    {"title": tr("4. Vector (Cross) Product"),
     "items": [
         card("4.1 Definition and the determinant form",
              h4("Definition")
              + p("<b>a × b = |a||b| sin θ n-hat</b>, where n-hat is the unit vector perpendicular to both, "
                  "given by the right-hand rule. The answer is a <b>vector</b>.")
              + h4("Determinant form")
              + p("<b>a × b = |i j k; a₁ a₂ a₃; b₁ b₂ b₃|</b> = i(a₂b₃ − a₃b₂) − j(a₁b₃ − a₃b₁) + "
                  "k(a₁b₂ − a₂b₁).")
              + h4("Worked example")
              + p("a = 2i + j + 3k, b = i − 2j + k: expanding the determinant gives (1 + 6)i − (2 − 3)j + "
                  "(−4 − 1)k = <b>7i + j − 5k</b>, of magnitude √75 = 5√3 ≈ 8.66.")
              + h4("Common mistake / conditions")
              + p("The middle term carries a minus. Writing +j(...) instead of −j(...) is the single most common "
                  "error in this question; check by taking a × a, which must be 0."),
              "v4_cross", examples=["v1n10", "v1n13"], syllabus_item="3.2"),
         card("4.2 Properties of the cross product",
              h4("Properties")
              + table(["Property", "Statement", "Consequence"],
                      [("Anti-commutative", "a × b = −(b × a)", "order matters - unlike the dot product"),
                       ("Zero for parallel", "a × a = 0", "parallel vectors give a zero cross product"),
                       ("Distributive", "a × (b + c) = a × b + a × c", "expand and collect"),
                       ("Scalar", "(ka) × b = k(a × b)", "pull constants out"),
                       ("Basis", "i × j = k, j × k = i, k × i = j", "cyclic order, anticlockwise")])
              + h4("Right-hand rule")
              + p("Curl the fingers of the right hand from a to b; the thumb points along a × b. Reversing the "
                  "order reverses the thumb, which is the anti-commutative property in physical form.")
              + h4("Magnitude as an area")
              + p("|a × b| = |a||b| sin θ is the area of the parallelogram with sides a and b, because the "
                  "height is |b| sin θ. This is the fastest way to compute areas in three dimensions."),
              "v4_cross", examples=["v1n19"], syllabus_item="3.2"),
         card("4.3 Area of a parallelogram and a triangle",
              h4("Formulae")
              + p("<b>Parallelogram:</b> area = |a × b| for adjacent sides a and b.")
              + p("<b>Triangle:</b> area = ½|a × b|, because a triangle is half of the parallelogram.")
              + h4("Three vertices")
              + p("With A, B, C given, take a = AB = B − A and b = AC = C − A, then area = ½|a × b|. Starting "
                  "from one vertex matters - using two different starting points gives the wrong vectors.")
              + h4("Worked example")
              + p("A(1, 1, 1), B(2, 3, 4), C(4, 2, 3): AB = i + 2j + 3k, AC = 3i + j + 2k, and "
                  "AB × AC = i(4 − 3) − j(2 − 9) + k(1 − 6) = i + 7j − 5k. |a × b| = √75 = 5√3, so the area is "
                  "<b>5√3/2 ≈ 4.33</b> square units.")
              + h4("Collinearity")
              + p("Three points are collinear exactly when a × b = 0. That is the 3-D version of the "
                  "determinant test from Unit 1."),
              "v4_cross", examples=["v1n11", "v1n12"], syllabus_item="3.3")]},

    {"title": tr("5. Applications: Work Done and Moment of Force"),
     "items": [
         card("5.1 Work done by a force",
              h4("Definition")
              + p("<b>W = F · d = |F||d| cos θ</b>, where θ is the angle between the force and the "
                  "displacement. Work is a <b>scalar</b> measured in joules (N·m).")
              + h4("Why the dot product")
              + p("Only the component of the force along the motion contributes. If F is perpendicular to d "
                  "(carrying a bag horizontally), cos 90° = 0 and no work is done - which matches everyday "
                  "experience and the formula.")
              + h4("Worked example")
              + p("F = 3i + 2j − k newton moves an object through d = 2i − j + 3k metre. "
                  "W = 6 − 2 − 3 = <b>1 J</b>. A small positive value means the force mostly pushes sideways.")
              + h4("Conditions")
              + p("Use the displacement, not the distance travelled; and keep the units consistent (N and m "
                  "give J). A negative dot product means the force opposes the motion."),
              "v6_work", examples=["v1n14", "v1n15", "v1n24"], syllabus_item="3.4"),
         card("5.2 Moment of a force about a point",
              h4("Definition")
              + p("<b>M = r × F</b>, where r is the position vector of the point of application measured from "
                  "the point about which the moment is taken. The moment is a <b>vector</b>, in N·m, and its "
                  "direction gives the axis of rotation.")
              + h4("Magnitude")
              + p("|M| = |r||F| sin θ = F × (perpendicular distance). Both forms appear in exams; the second is "
                  "faster when the perpendicular distance is given directly.")
              + h4("Worked example")
              + p("r = 3i − j + 2k and F = 2i + j − k give M = r × F = |i j k; 3 −1 2; 2 1 −1| = "
                  "−i + 7j + 5k, of magnitude √75 = 5√3 ≈ <b>8.66 N·m</b>.")
              + h4("Common mistake / conditions")
              + p("Take r from the correct point. A moment \"about A\" needs r = position of the force minus "
                  "position of A, not the position of the force from the origin."),
              "v7_moment", examples=["v1n16", "v1n17", "v1n18", "v1n25"], syllabus_item="3.4"),
         card("5.3 Choosing dot or cross: a decision guide",
              h4("The question behind every problem")
              + table(["Question wording", "Product", "Because"],
                      [("\"Find the angle between\"", "dot", "cos θ comes from a · b"),
                       ("\"Work done by the force\"", "dot", "W = F · d is a scalar"),
                       ("\"Show the vectors are perpendicular\"", "dot", "a · b = 0"),
                       ("\"Find the area / a perpendicular vector\"", "cross", "|a × b| is an area"),
                       ("\"Moment of the force\"", "cross", "M = r × F is a vector"),
                       ("\"Show the vectors are parallel\"", "cross", "a × b = 0")])
              + h4("Mixed-problem routine")
              + ol("Write both vectors in i, j, k form.",
                   "Decide dot or cross from the table above.",
                   "Compute carefully, keeping the minus in the cross product's middle term.",
                   "State units and the geometric meaning of the answer.")
              + h4("Check worth doing")
              + p("For any pair, |a × b|² + (a · b)² = |a|²|b|². Testing this on your numbers catches almost "
                  "every arithmetic slip before it costs marks."),
              "v5_angle", examples=["v1n26"], syllabus_item="3.4")]},

    {"title": tr("6. Answered Practice (Unit 3 level)"), "items": []},
]

GIVEN = h4("Given and assumptions")
FORMULA = h4("Formula")
STEPS = h4("Step-by-step solution")
CHECK = h4("Interpretation and check")


def num(nid, q, chunks):
    return {"id": nid, "q": tr(q), "a": tr("".join(chunks))}


NUMERICALS = [
    num("v1n1", "Find the magnitude of a = 3i − 4j + 12k.",
        [GIVEN + p("Three components, one negative."),
         FORMULA + p("|a| = √(a₁² + a₂² + a₃²)"),
         STEPS + ol("3² = 9, (−4)² = 16, 12² = 144", "Sum = 169", "|a| = √169 = 13"),
         CHECK + p("<b>13 units.</b> The 3-4-12 triple always gives 13 - worth remembering, like 3-4-5 in two "
                   "dimensions.")]),
    num("v1n2", "Write the unit vector along a = 2i + 3j − 6k.",
        [GIVEN + p("First find the magnitude, then divide every component by it."),
         FORMULA + p("a-hat = a/|a|"),
         STEPS + ol("|a| = √(4 + 9 + 36) = √49 = 7", "a-hat = (2i + 3j − 6k)/7"),
         CHECK + p("<b>(2/7)i + (3/7)j − (6/7)k.</b> Check the length: (4 + 9 + 36)/49 = 1 ✓. A unit vector is "
                   "the fastest way to answer \"find a vector of magnitude 10 in this direction\" - multiply "
                   "a-hat by 10.")]),
    num("v1n3", "Find the direction cosines of a = i + 2j + 2k.",
        [GIVEN + p("Direction cosines are the components divided by the magnitude."),
         FORMULA + p("cos α = a₁/|a|, cos β = a₂/|a|, cos γ = a₃/|a|"),
         STEPS + ol("|a| = √(1 + 4 + 4) = 3", "cos α = 1/3, cos β = 2/3, cos γ = 2/3",
                    "α ≈ 70.5°, β ≈ 48.2°, γ ≈ 48.2°"),
         CHECK + p("<b>1/3, 2/3, 2/3.</b> Check the identity: (1 + 4 + 4)/9 = 1 ✓. All three angles are "
                   "between 0° and 180°, as direction angles must be.")]),
    num("v1n4", "For a = 2i + 3j − k and b = i − 2j + 4k find a + b, a − b and their magnitudes.",
        [GIVEN + p("Add and subtract component by component."),
         FORMULA + p("(a₁ ± b₁)i + (a₂ ± b₂)j + (a₃ ± b₃)k"),
         STEPS + ol("a + b = 3i + j + 3k", "|a + b| = √(9 + 1 + 9) = √19 ≈ 4.36",
                    "a − b = i + 5j − 5k", "|a − b| = √(1 + 25 + 25) = √51 ≈ 7.14"),
         CHECK + p("<b>√19 ≈ 4.36 and √51 ≈ 7.14.</b> Note that |a| + |b| = 3.74 + 4.58 = 8.32 is larger than "
                   "both, so the triangle inequality holds but magnitudes do not add directly.")]),
    num("v1n5", "Find the angle between a = 2i − j + k and b = i + j + 2k.",
        [GIVEN + p("Dot product and both magnitudes."),
         FORMULA + p("cos θ = (a · b)/(|a||b|)"),
         STEPS + ol("a · b = 2 − 1 + 2 = 3", "|a| = √6 and |b| = √6", "cos θ = 3/6 = 1/2", "θ = 60°"),
         CHECK + p("<b>60°.</b> The symmetry (|a| = |b|) is a hint: equal lengths often give a standard angle. "
                   "A positive cosine confirms the angle is acute.")]),
    num("v1n6", "Find the dot product of p = i + 2j + 3k and q = 4i − 5j + 6k.",
        [GIVEN + p("Multiply matching components and add."),
         FORMULA + p("p · q = p₁q₁ + p₂q₂ + p₃q₃"),
         STEPS + ol("1 × 4 = 4", "2 × (−5) = −10", "3 × 6 = 18", "4 − 10 + 18 = 12"),
         CHECK + p("<b>12.</b> A positive dot product means the angle between them is acute. Since the vectors "
                   "are nowhere near parallel (their components differ a lot), a moderate positive value is "
                   "expected.")]),
    num("v1n7", "Find the angle between 2i + 2j − k and 6i − 3j + 2k.",
        [GIVEN + p("Both magnitudes are Pythagorean, which keeps the arithmetic exact."),
         FORMULA + p("cos θ = (a · b)/(|a||b|)"),
         STEPS + ol("a · b = 12 − 6 − 2 = 4", "|a| = √9 = 3, |b| = √49 = 7",
                    "cos θ = 4/21 ≈ 0.1905", "θ ≈ 79.0°"),
         CHECK + p("<b>θ ≈ 79°.</b> A small positive cosine means an angle just under 90°, so the vectors are "
                   "nearly - but not quite - perpendicular. Check with |a × b|: √(441 − 16) = √425 ≈ 20.6, so "
                   "sin θ = 20.6/21 ≈ 0.98 ✓.")]),
    num("v1n8", "Find λ so that 2i + λj + k is perpendicular to i − 2j + 3k.",
        [GIVEN + p("Perpendicular means the dot product is zero."),
         FORMULA + p("a · b = 0"),
         STEPS + ol("2(1) + λ(−2) + 1(3) = 0", "5 − 2λ = 0", "λ = 5/2"),
         CHECK + p("<b>λ = 2.5.</b> Check: 2 − 5 + 3 = 0 ✓. This \"find the unknown from perpendicularity\" "
                   "pattern appears in almost every paper.")]),
    num("v1n9", "Find the projection of a = 3i + j − 2k on b = i + j + k.",
        [GIVEN + p("Projection means the shadow length of a along b."),
         FORMULA + p("projection = (a · b)/|b|"),
         STEPS + ol("a · b = 3 + 1 − 2 = 2", "|b| = √3", "projection = 2/√3 ≈ 1.155"),
         CHECK + p("<b>2/√3 ≈ 1.15.</b> Rationalising gives 2√3/3. The projection is shorter than |a| = √14 "
                   "≈ 3.74, as it must be for any non-zero angle.")]),
    num("v1n10", "Find a × b for a = 2i + j + 3k and b = i − 2j + k.",
        [GIVEN + p("Expand the determinant, keeping the minus on the j-term."),
         FORMULA + p("a × b = |i j k; 2 1 3; 1 −2 1|"),
         STEPS + ol("i(1×1 − 3×(−2)) = i(1 + 6) = 7i",
                    "−j(2×1 − 3×1) = −j(2 − 3) = +j",
                    "k(2×(−2) − 1×1) = k(−4 − 1) = −5k",
                    "a × b = 7i + j − 5k"),
         CHECK + p("<b>7i + j − 5k.</b> Two checks: dot the answer with a and with b - both must be zero "
                   "(7(2) + 1(1) − 5(3) = 0 ✓, 7 − 2 − 5 = 0 ✓), which proves it is perpendicular to both.")]),
    num("v1n11", "Find the area of the parallelogram whose adjacent sides are a = 2i + j + 3k and "
                 "b = i − 2j + k.",
        [GIVEN + p("Adjacent sides - so the cross product gives the area directly."),
         FORMULA + p("area = |a × b|"),
         STEPS + ol("a × b = 7i + j − 5k", "|a × b| = √(49 + 1 + 25) = √75", "= 5√3 ≈ 8.66"),
         CHECK + p("<b>5√3 ≈ 8.66 square units.</b> A parallelogram area can exceed the product of the side "
                   "lengths only if the angle is right - here |a||b| = 3.74 × 2.45 = 9.17, slightly more than "
                   "8.66, so the angle is not 90° ✓.")]),
    num("v1n12", "Find the area of the triangle with vertices A(1, 1, 1), B(2, 3, 4) and C(4, 2, 3).",
        [GIVEN + p("Take both vectors from the same vertex A."),
         FORMULA + p("area = ½|AB × AC|"),
         STEPS + ol("AB = i + 2j + 3k and AC = 3i + j + 2k",
                    "AB × AC = i(4 − 3) − j(2 − 9) + k(1 − 6) = i + 7j − 5k",
                    "|AB × AC| = √(1 + 49 + 25) = √75 = 5√3", "area = 5√3/2 ≈ 4.33"),
         CHECK + p("<b>5√3/2 ≈ 4.33 square units.</b> The triangle is exactly half of the parallelogram on the "
                   "same two sides - which is where the ½ comes from, not a coincidence.")]),
    num("v1n13", "Find a unit vector perpendicular to both i + j and j + k.",
        [GIVEN + p("A vector perpendicular to both is their cross product."),
         FORMULA + p("n = ±(a × b)/|a × b|"),
         STEPS + ol("a × b = |i j k; 1 1 0; 0 1 1| = i(1 − 0) − j(1 − 0) + k(1 − 0) = i − j + k",
                    "|a × b| = √3", "n = ±(i − j + k)/√3"),
         CHECK + p("<b>±(i − j + k)/√3.</b> Two answers exist because \"perpendicular to both\" leaves the "
                   "direction up or down. Check: (1 − 1 + 0)/√3 = 0 and (0 − 1 + 1)/√3 = 0 ✓.")]),
    num("v1n14", "Find the work done by F = 3i + 2j − k when the displacement is d = 2i − j + 3k.",
        [GIVEN + p("Force and displacement in newton and metre."),
         FORMULA + p("W = F · d"),
         STEPS + ol("3(2) = 6", "2(−1) = −2", "(−1)(3) = −3", "W = 6 − 2 − 3 = 1 J"),
         CHECK + p("<b>1 joule.</b> The small positive value means the force is partly along the motion and "
                   "partly sideways. If the answer had been negative, the force would be retarding.")]),
    num("v1n15", "A force of 20 N acts at 60° to a displacement of 5 m. Find the work done.",
        [GIVEN + p("Magnitudes and the angle between them."),
         FORMULA + p("W = |F||d| cos θ"),
         STEPS + ol("W = 20 × 5 × cos 60°", "= 100 × 0.5", "= 50 J"),
         CHECK + p("<b>50 J.</b> At 0° the work would be 100 J and at 90° it would be 0 J; 50 J sits exactly "
                   "between, as cos 60° = 0.5 predicts.")]),
    num("v1n16", "Find the moment of F = 2i + j − k acting at r = 3i − j + 2k about the origin.",
        [GIVEN + p("Moment about O is M = r × F."),
         FORMULA + p("M = |i j k; 3 −1 2; 2 1 −1|"),
         STEPS + ol("i((−1)(−1) − 2(1)) = i(1 − 2) = −i",
                    "−j(3(−1) − 2(2)) = −j(−3 − 4) = 7j",
                    "k(3(1) − (−1)(2)) = k(3 + 2) = 5k", "M = −i + 7j + 5k"),
         CHECK + p("<b>−i + 7j + 5k, magnitude √75 = 5√3 ≈ 8.66 N·m.</b> Check M · r = −3 − 7 + 10 = 0 and "
                   "M · F = −2 + 7 − 5 = 0 ✓ - a moment is perpendicular to both r and F.")]),
    num("v1n17", "Find the moment of F = i + 2j acting at B(3, 4, 0) about the point A(1, 1, 0).",
        [GIVEN + p("The moment arm is measured from A, so r = OB − OA."),
         FORMULA + p("M = r × F with r = B − A"),
         STEPS + ol("r = (3 − 1)i + (4 − 1)j = 2i + 3j",
                    "M = |i j k; 2 3 0; 1 2 0|", "= i(0) − j(0) + k(4 − 3) = k"),
         CHECK + p("<b>M = k, magnitude 1 N·m.</b> The moment points along z because both r and F lie in the "
                   "xy-plane - a rotation about the z-axis. Using OB instead of B − A is the usual error.")]),
    num("v1n18", "A force of 40 N acts at a perpendicular distance of 0.5 m from a hinge. Find the moment.",
        [GIVEN + p("Perpendicular distance given, so the scalar form is fastest."),
         FORMULA + p("|M| = F × perpendicular distance"),
         STEPS + ol("|M| = 40 × 0.5", "= 20"),
         CHECK + p("<b>20 N·m.</b> Same answer as |r × F| with sin θ = 1. Doubling the distance doubles the "
                   "moment - the reason a longer spanner loosens a bolt more easily.")]),
    num("v1n19", "If |a + b| = |a − b|, show that a and b are perpendicular.",
        [GIVEN + p("Square both sides instead of working with roots."),
         FORMULA + p("|a ± b|² = |a|² ± 2a · b + |b|²"),
         STEPS + ol("|a|² + 2a · b + |b|² = |a|² − 2a · b + |b|²", "4a · b = 0", "a · b = 0, so a ⊥ b"),
         CHECK + p("<b>a · b = 0, therefore perpendicular.</b> Geometrically the two diagonals of the "
                   "parallelogram are equal exactly when it is a rectangle - the same statement in words.")]),
    num("v1n20", "If a = i − 2j + 3k and b = 2i + j − k, find |2a − 3b|.",
        [GIVEN + p("Form the combination first, then take the magnitude."),
         FORMULA + p("k a scales every component"),
         STEPS + ol("2a = 2i − 4j + 6k and 3b = 6i + 3j − 3k",
                    "2a − 3b = −4i − 7j + 9k",
                    "|2a − 3b| = √(16 + 49 + 81) = √146 ≈ 12.08"),
         CHECK + p("<b>√146 ≈ 12.08.</b> Estimate first: |2a| ≈ 2(3.74) = 7.5 and |3b| ≈ 3(2.45) = 7.3, so the "
                   "difference lies between 0.2 and 14.8 - and 12.08 does.")]),
    num("v1n21", "Find a vector of magnitude 10 in the direction of 3i + 4j.",
        [GIVEN + p("Find the unit vector, then multiply by the required magnitude."),
         FORMULA + p("required = magnitude × a-hat"),
         STEPS + ol("|a| = 5", "a-hat = (3i + 4j)/5", "10 a-hat = 6i + 8j"),
         CHECK + p("<b>6i + 8j.</b> Check: √(36 + 64) = 10 ✓. Direction is unchanged because scaling by a "
                   "positive number does not rotate a vector.")]),
    num("v1n22", "For A(1, 2, 3) and B(3, 4, 5) find AB, |AB| and the midpoint.",
        [GIVEN + p("AB = OB − OA; the midpoint is the average of the coordinates."),
         FORMULA + p("AB = (x₂ − x₁)i + (y₂ − y₁)j + (z₂ − z₁)k"),
         STEPS + ol("AB = 2i + 2j + 2k", "|AB| = √12 = 2√3 ≈ 3.46",
                    "midpoint = (2, 3, 4)"),
         CHECK + p("<b>2i + 2j + 2k, 2√3 ≈ 3.46, midpoint (2, 3, 4).</b> Check the midpoint is halfway: "
                   "AM = i + j + k with magnitude √3 = half of 2√3 ✓.")]),
    num("v1n23", "If a · b = 6, |a| = 3 and |b| = 4, find the angle between a and b.",
        [GIVEN + p("All three quantities in the dot-product definition are known except θ."),
         FORMULA + p("cos θ = (a · b)/(|a||b|)"),
         STEPS + ol("cos θ = 6/(3 × 4) = 6/12", "cos θ = 0.5", "θ = 60°"),
         CHECK + p("<b>60°.</b> Since a · b is positive and smaller than |a||b| = 12, the angle must be "
                   "between 0° and 90° - 60° fits.")]),
    num("v1n24", "Find the work done by F = i + j + k along the displacement from (1, 2, 3) to (4, 6, 3).",
        [GIVEN + p("The displacement vector is the difference of the points."),
         FORMULA + p("W = F · d, with d = B − A"),
         STEPS + ol("d = 3i + 4j + 0k", "W = 1(3) + 1(4) + 1(0)", "W = 7 J"),
         CHECK + p("<b>7 J.</b> The z-component contributes nothing because the displacement has no z-part - "
                   "only the component of force along the motion does work.")]),
    num("v1n25", "Find the magnitude of the moment of F = i − j + 2k acting at r = 2i + 3j + k.",
        [GIVEN + p("Cross product first, then its magnitude."),
         FORMULA + p("M = r × F and |M| = √(M₁² + M₂² + M₃²)"),
         STEPS + ol("M = i(3×2 − 1×(−1)) − j(2×2 − 1×1) + k(2×(−1) − 3×1)",
                    "= i(6 + 1) − j(4 − 1) + k(−2 − 3) = 7i − 3j − 5k",
                    "|M| = √(49 + 9 + 25) = √83 ≈ 9.11"),
         CHECK + p("<b>√83 ≈ 9.11 N·m.</b> Check M · r = 14 − 9 − 5 = 0 ✓ and M · F = 7 + 3 − 10 = 0 ✓, so "
                   "the moment is perpendicular to both vectors as it must be.")]),
    num("v1n26", "For |a| = 3, |b| = 4 and a · b = 6, find |a × b| and verify the identity "
                 "|a × b|² + (a · b)² = |a|²|b|².",
        [GIVEN + p("Use the angle from the dot product, then both formulas."),
         FORMULA + p("|a × b| = |a||b| sin θ and sin²θ = 1 − cos²θ"),
         STEPS + ol("cos θ = 6/12 = 0.5, so sin θ = √3/2",
                    "|a × b| = 12 × √3/2 = 6√3 ≈ 10.39",
                    "Check: (6√3)² + 6² = 108 + 36 = 144 = 9 × 16 ✓"),
         CHECK + p("<b>6√3 ≈ 10.39.</b> The identity holds for every pair of vectors, so it doubles as a check "
                   "on any dot-and-cross question - compute whichever magnitude is easier and derive the other.")]),
]

EQUATIONS = [
    {"title": tr("Vector basics"), "items": [
        {"name": tr("Magnitude"), "f": "|a| = √(a₁² + a₂² + a₃²)",
         "terms": tr("Pythagoras extended to three dimensions.")},
        {"name": tr("Unit vector"), "f": "a-hat = a/|a|",
         "terms": tr("Same direction, length 1; multiply it by any magnitude to scale.")},
        {"name": tr("Direction cosines"), "f": "cos²α + cos²β + cos²γ = 1",
         "terms": tr("Each cosine is a component divided by the magnitude.")},
        {"name": tr("Vector between points"), "f": "AB = OB − OA",
         "terms": tr("Head minus tail; the order decides every sign.")},
    ]},
    {"title": tr("Products"), "items": [
        {"name": tr("Dot product"), "f": "a · b = a₁b₁ + a₂b₂ + a₃b₃ = |a||b| cos θ",
         "terms": tr("A scalar; zero means perpendicular.")},
        {"name": tr("Cross product"), "f": "a × b = |i j k; a₁ a₂ a₃; b₁ b₂ b₃|",
         "terms": tr("A vector; zero means parallel. Keep the minus on the j-term.")},
        {"name": tr("Angle between vectors"), "f": "cos θ = (a · b)/(|a||b|)",
         "terms": tr("A negative cosine means an obtuse angle - do not change the sign.")},
        {"name": tr("Projection"), "f": "projection of a on b = (a · b)/|b|",
         "terms": tr("The shadow length of a along b.")},
        {"name": tr("Area"), "f": "parallelogram |a × b|, triangle ½|a × b|",
         "terms": tr("Adjacent sides from the same vertex.")},
    ]},
    {"title": tr("Applications"), "items": [
        {"name": tr("Work done"), "f": "W = F · d = |F||d| cos θ",
         "terms": tr("Joules; only the along-motion component works.")},
        {"name": tr("Moment of a force"), "f": "M = r × F,  |M| = F × perpendicular distance",
         "terms": tr("Newton-metre; r is measured from the point about which the moment is taken.")},
        {"name": tr("Identity check"), "f": "|a × b|² + (a · b)² = |a|²|b|²",
         "terms": tr("Fast verification of any dot/cross numerical.")},
    ]},
]

VIVA = [
    {"title": tr("Vectors and algebra"), "items": [
        {"q": tr("What is the difference between a scalar and a vector?"),
         "a": tr("A scalar has magnitude only; a vector has magnitude and direction.")},
        {"q": tr("How is the magnitude of a vector found?"),
         "a": tr("|a| = √(a₁² + a₂² + a₃²), the square root of the sum of squared components.")},
        {"q": tr("What is a unit vector?"),
         "a": tr("A vector of length 1 in the direction of a, written a/|a|.")},
        {"q": tr("State the triangle law of addition."),
         "a": tr("Place the tail of b on the head of a; a + b joins the free tail to the free head.")},
        {"q": tr("How do you find the vector AB from two points?"),
         "a": tr("AB = OB − OA, that is head minus tail.")},
        {"q": tr("When are two vectors parallel?"),
         "a": tr("When one is a scalar multiple of the other, equivalently when a × b = 0.")},
    ]},
    {"title": tr("Dot and cross product"), "items": [
        {"q": tr("Define the scalar product."),
         "a": tr("a · b = |a||b| cos θ; in components it is a₁b₁ + a₂b₂ + a₃b₃.")},
        {"q": tr("What does a · b = 0 mean?"),
         "a": tr("The vectors are perpendicular (or one of them is the zero vector).")},
        {"q": tr("How is the angle between two vectors found?"),
         "a": tr("cos θ = (a · b)/(|a||b|), then θ = cos⁻¹ of that value.")},
        {"q": tr("Define the vector product."),
         "a": tr("a × b = |a||b| sin θ n-hat, a vector perpendicular to both by the right-hand rule.")},
        {"q": tr("What does a × b = 0 mean?"),
         "a": tr("The vectors are parallel or antiparallel.")},
        {"q": tr("Is the cross product commutative?"),
         "a": tr("No: a × b = −(b × a). Only the dot product is commutative.")},
        {"q": tr("What does |a × b| represent geometrically?"),
         "a": tr("The area of the parallelogram with a and b as adjacent sides.")},
        {"q": tr("State the identity linking dot and cross products."),
         "a": tr("|a × b|² + (a · b)² = |a|²|b|².")},
    ]},
    {"title": tr("Applications"), "items": [
        {"q": tr("Write the formula for work done."),
         "a": tr("W = F · d = |F||d| cos θ, measured in joules.")},
        {"q": tr("Why is no work done when the force is perpendicular to the motion?"),
         "a": tr("Because cos 90° = 0, so only the along-motion component contributes.")},
        {"q": tr("Define the moment of a force."),
         "a": tr("M = r × F, a vector in N·m giving the turning effect about a point.")},
        {"q": tr("What is the scalar form of the moment?"),
         "a": tr("|M| = force × perpendicular distance from the pivot.")},
        {"q": tr("From which point is r measured in M = r × F?"),
         "a": tr("From the point about which the moment is taken, to the point of application of the force.")},
        {"q": tr("Which product gives the area of a triangle from two vectors?"),
         "a": tr("Half the magnitude of their cross product, ½|a × b|.")},
        {"q": tr("How do you test three points for collinearity in 3-D?"),
         "a": tr("Take two vectors from one point; the points are collinear when their cross product is zero.")},
        {"q": tr("Give one practical use of the dot product."),
         "a": tr("Finding the work done, or the component of a force along a direction.")},
    ]},
]

PRACTICE = [
    ("Find the magnitude and unit vector of a = 6i + 2j − 3k.", 3,
     h4("Working") + ol("|a| = √(36 + 4 + 9) = √49 = 7", "a-hat = (6i + 2j − 3k)/7")
     + h4("Answer") + p("<b>7 and (6i + 2j − 3k)/7.</b> Check the unit vector's length: (36 + 4 + 9)/49 = 1 ✓.")),
    ("For a = i + j and b = i − j, find a · b and the angle between them.", 4,
     h4("Working") + ol("a · b = 1 − 1 = 0", "|a| = |b| = √2", "cos θ = 0, so θ = 90°")
     + h4("Check") + p("A zero dot product is the perpendicularity test, so 90° must be the answer - the two "
                        "vectors are the diagonals of a square.")),
    ("Find the angle between i + 2j + 2k and 2i + j − 2k.", 4,
     h4("Working") + ol("a · b = 2 + 2 − 4 = 0", "Both magnitudes are 3", "cos θ = 0, so θ = 90°")
     + h4("Answer") + p("<b>90°.</b> Since the dot product vanished, the vectors are perpendicular; there is no "
                        "need to compute the magnitudes at all, but they confirm the result is not a division "
                        "by zero.")),
    ("Find a × b for a = 3i − j + 2k and b = i + 2j − k.", 4,
     h4("Working") + ol("i((−1)(−1) − 2(2)) = i(1 − 4) = −3i",
                        "−j(3(−1) − 2(1)) = −j(−3 − 2) = 5j",
                        "k(3(2) − (−1)(1)) = k(6 + 1) = 7k")
     + h4("Answer") + p("<b>−3i + 5j + 7k.</b> Check with the dot product: (−3)(3) + 5(−1) + 7(2) = 0 ✓ and "
                        "(−3)(1) + 5(2) + 7(−1) = 0 ✓.")),
    ("Find the area of the parallelogram with sides i + 2j + 3k and 2i + j + k.", 4,
     h4("Working") + ol("a × b = i(2 − 3) − j(1 − 6) + k(1 − 4) = −i + 5j − 3k",
                        "|a × b| = √(1 + 25 + 9) = √35 ≈ 5.92")
     + h4("Answer") + p("<b>√35 ≈ 5.92 square units.</b> The area must be less than |a||b| = 3.74 × 2.45 = 9.17, "
                        "and it is ✓.")),
    ("Find λ so that 3i + λj − 2k is perpendicular to 2i − j + 4k.", 3,
     h4("Working") + ol("Perpendicular means a · b = 0",
                        "3(2) + λ(−1) + (−2)(4) = 0", "6 − λ − 8 = 0", "λ = −2")
     + h4("Answer") + p("<b>λ = −2.</b> Check: 6 + 2 − 8 = 0 ✓. One equation, one unknown - this "
                        "\"perpendicularity gives the unknown\" pattern is worth recognising instantly.")),
    ("Find the work done by F = 4i − j + 2k along d = 2i + 3j − k.", 3,
     h4("Working") + p("W = 8 − 3 − 2 = 3 J.")
     + h4("Answer") + p("<b>3 J.</b> Positive work means the force has a component along the displacement; the "
                        "j-components partially cancel.")),
    ("Find the moment of F = 3i + j acting at r = 2i − j about the origin.", 4,
     h4("Working") + ol("M = |i j k; 2 −1 0; 3 1 0|", "= i(0) − j(0) + k(2 + 3) = 5k")
     + h4("Answer") + p("<b>5k N·m, magnitude 5.</b> The moment is about the z-axis because everything lies in "
                        "the xy-plane; check M · r = 0 ✓.")),
    ("Find the projection of 2i + 3j − k on i + j + k.", 4,
     h4("Working") + ol("a · b = 2 + 3 − 1 = 4", "|b| = √3", "projection = 4/√3 ≈ 2.31")
     + h4("Answer") + p("<b>4/√3 ≈ 2.31.</b> Rationalised: 4√3/3. The projection is smaller than |a| = √14 ≈ "
                        "3.74 ✓.")),
    ("Show that the points A(1, 2, 3), B(2, 3, 4) and C(3, 4, 5) are collinear.", 4,
     h4("Working") + ol("AB = i + j + k", "AC = 2i + 2j + 2k = 2AB",
                        "Since AC is a scalar multiple of AB, the cross product is zero")
     + h4("Answer") + p("<b>Collinear.</b> The points lie on the line through (1, 2, 3) with direction i + j + k, "
                        "which is x − 1 = y − 2 = z − 3.")),
    ("If |a| = 5, |b| = 12 and a · b = 30, find the angle between a and b.", 3,
     h4("Working") + p("cos θ = 30/(5 × 12) = 0.5, so θ = 60°.")
     + h4("Answer") + p("<b>60°.</b> Check with the cross product: |a × b| = 60 sin 60° = 30√3 ≈ 51.96, and "
                        "51.96² + 30² = 3600 = 25 × 144 ✓.")),
    ("Find a vector of magnitude 6 perpendicular to both i + j and i − j.", 4,
     h4("Working") + ol("(i + j) × (i − j) = i(0) − j(0) + k(−1 − 1) = −2k",
                        "Unit perpendicular = ±k", "Required vector = ±6k")
     + h4("Answer") + p("<b>±6k.</b> Both given vectors lie in the xy-plane, so any perpendicular is along z - "
                        "the answer must have no i or j component.")),
    ("Find the moment of F = 2i + 3j + k acting at A(1, 1, 1) about B(0, 1, 1).", 4,
     h4("Working") + ol("r = OA − OB = i + 0j + 0k",
                        "M = |i j k; 1 0 0; 2 3 1| = i(0) − j(1) + k(3) = −j + 3k")
     + h4("Answer") + p("<b>−j + 3k N·m, magnitude √10 ≈ 3.16.</b> The arm has no y or z component, so only two "
                        "terms survive - subtract the right point to keep it that way.")),
    ("Find the area of the triangle with vertices (0, 0, 0), (2, 1, 0) and (1, 3, 4).", 4,
     h4("Working") + ol("a = 2i + j, b = i + 3j + 4k",
                        "a × b = i(4 − 0) − j(8 − 0) + k(6 − 1) = 4i − 8j + 5k",
                        "|a × b| = √(16 + 64 + 25) = √105", "area = √105/2 ≈ 5.12")
     + h4("Answer") + p("<b>√105/2 ≈ 5.12 square units.</b> Half the parallelogram area is expected, since the "
                        "triangle is exactly half of it.")),
    ("A force F = 2i − j + 3k acts at the point P(1, 2, 3). Find its moment about Q(2, 0, 1) and the work done "
     "if the point moves from P to Q.", 4,
     h4("Working") + ol("r = OP − OQ = −i + 2j + 2k",
                        "M = |i j k; −1 2 2; 2 −1 3| = i(6 + 2) − j(−3 − 4) + k(1 − 4) = 8i + 7j − 3k",
                        "d = OQ − OP = i − 2j − 2k, so W = 2 − (−2) + (−6) = −2 J")
     + h4("Answer") + p("<b>M = 8i + 7j − 3k (|M| = √122 ≈ 11.05 N·m); W = −2 J.</b> Negative work means the "
                        "force opposes that displacement - consistent with the moment's large magnitude.")),
]

ANSWERED = {"title": tr("6. Answered Practice (Unit 3 level, suggested marks)"),
            "items": [{"h": tr(f"Practice {i}. {q}"), "body": tr(a)} for i, (q, _m, a) in enumerate(PRACTICE, 1)]}
NOTES[-1] = ANSWERED
EXAM = [{"q": tr("Practice: " + q), "marks": m} for q, m, _ in PRACTICE]
LESSON_COUNT = sum(len(s["items"]) for s in NOTES) - len(ANSWERED["items"])
