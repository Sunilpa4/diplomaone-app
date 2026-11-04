"""DI02000021 Engineering Mathematics - Unit 1: Matrices (GTU 1.1-1.6, 10 h, 23 %, 16 marks).

Concept and types of matrices, addition/subtraction/scalar multiplication, the product of two
matrices, the adjoint and inverse of 2x2 and 3x3 matrices, and the solution of two simultaneous
linear equations by the inverse method and by Cramer's rule.
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


def mx(*rows):
    """A matrix drawn as a compact table (entries separated by cells)."""
    return ("<table><tr>" + "".join(f"<th>{c}</th>" for c in rows[0]) + "</tr>"
            + "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in rows[1:]) + "</table>")


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
    ("Khan Academy - matrices, determinants and inverses",
     "https://www.khanacademy.org/math/precalculus/x9e81a4f98389efdf:matrices"),
    ("OpenStax - College Algebra 2e, chapter 7 (systems of equations and matrices)",
     "https://openstax.org/details/books/college-algebra-2e"),
    ("GeoGebra - two straight lines and the number of solutions they share",
     "https://www.geogebra.org/"),
    ("B. S. Grewal - Elementary Engineering Mathematics (Khanna Publishers)",
     "https://www.khannapublishers.in/"),
]

NOTES = [
    {"title": tr("1. What a Matrix Is"),
     "items": [
         card("1.1 Order, entries and the meaning of aᵢⱼ",
              h4("Definition")
              + p("A <b>matrix</b> is a rectangular arrangement of numbers written inside brackets. "
                  "The numbers inside are called <b>elements</b> or <b>entries</b>. A matrix has no "
                  "value of its own: it is an array, so it is never equal to a single number.")
              + p("A matrix with m rows and n columns has <b>order m × n</b>. The entry in row i and "
                  "column j is written <b>aᵢⱼ</b> - the row number always comes first.")
              + h4("Counting the entries")
              + ul("A 2 × 3 matrix has 2 × 3 = 6 entries.",
                   "A 3 × 3 matrix has 9 entries and is called <b>square</b>.",
                   "a₂₃ means row 2, column 3 - not row 3, column 2.")
              + h4("Worked reading")
              + p("For A = " + mx(["2", "−1", "3"], ["0", "5", "4"]) + " the order is 2 × 3, so "
                  "a₁₃ = 3 and a₂₂ = 5. There is no a₃₁: the matrix has only two rows.")
              + h4("Common mistake")
              + p("Writing the order as 3 × 2 because three columns are visible. Read rows first: "
                  "count the horizontal lines, then the vertical ones."),
              "mx1_anatomy", examples=["mm1n1"], syllabus_item="1.1"),
         card("1.2 Building a matrix from a rule, and equality",
              h4("Definition")
              + p("A matrix may be described by a formula for its general entry, for example "
                  "<b>aᵢⱼ = 2i + j</b> for a 2 × 3 matrix. Substitute every (i, j) pair in turn.")
              + h4("Worked example")
              + p("a₁₁ = 2(1) + 1 = 3, a₁₂ = 4, a₁₃ = 5, a₂₁ = 5, a₂₂ = 6, a₂₃ = 7, so the matrix "
                  "is " + mx(["3", "4", "5"], ["5", "6", "7"]) + ".")
              + h4("When two matrices are equal")
              + ul("The orders must be identical, and",
                   "every pair of matching entries must be equal.")
              + p("So " + mx(["x + 1", "3"], ["2", "y − 2"]) + " = " + mx(["5", "3"], ["2", "4"])
                  + " gives x + 1 = 5 and y − 2 = 4, that is x = 4 and y = 6.")
              + sc("Can a 2 × 2 matrix equal a 2 × 3 matrix?",
                   "Never. Equality starts with the order; different orders mean different arrays."),
              examples=["mm1n2", "mm1n3"], syllabus_item="1.1"),
         card("1.3 The transpose of a matrix",
              h4("Definition")
              + p("The <b>transpose</b> Aᵀ is made by turning rows into columns: the first row of A "
                  "becomes the first column of Aᵀ. A 2 × 3 matrix has a 3 × 2 transpose.")
              + h4("Worked example")
              + p("A = " + mx(["1", "2", "3"], ["4", "5", "6"]) + " gives Aᵀ = "
                  + mx(["1", "4"], ["2", "5"], ["3", "6"]) + ", and transposing again returns A: "
                  "(Aᵀ)ᵀ = A.")
              + h4("Rules")
              + ul("(Aᵀ)ᵀ = A", "(A + B)ᵀ = Aᵀ + Bᵀ", "(kA)ᵀ = kAᵀ",
                   "(AB)ᵀ = BᵀAᵀ - the order reverses, as it does for inverses.")
              + p("A square matrix that equals its own transpose is <b>symmetric</b>."),
              examples=["mm1n4"], syllabus_item="1.2"),
         card("1.4 Why engineers use matrices",
              h4("Where matrices appear")
              + ul("A network of currents or forces is written as one matrix of coefficients - one "
                   "row per equation.",
                   "A transformation (rotation, scaling, mirror) is stored as a 2 × 2 matrix, and "
                   "multiplying it by a position vector gives the new position.",
                   "A spreadsheet, a digital photograph and a table of readings are all matrices: "
                   "row and column positions locate each number.")
              + h4("The three questions this unit answers")
              + ol("How do I add and multiply these arrays?",
                   "How do I undo a square matrix (the inverse)?",
                   "How do I read the solution of two equations straight out of the matrices?")
              + p("Everything later in the semester - differentiation, integration, differential "
                  "equations - is built on these three skills."),
              syllabus_item="1.1"),
     ]},

    {"title": tr("2. Types of Matrices"),
     "items": [
         card("2.1 Square, diagonal, scalar, identity and zero matrices",
              h4("Definitions")
              + ul("<b>Square</b>: number of rows equals number of columns (2 × 2, 3 × 3).",
                   "<b>Diagonal</b>: square, and every entry off the main diagonal is zero.",
                   "<b>Scalar</b>: a diagonal matrix whose diagonal entries are all equal.",
                   "<b>Identity I</b>: a scalar matrix with 1 on the diagonal - the matrix version "
                   "of the number 1.",
                   "<b>Zero matrix O</b>: every entry is 0 - the matrix version of 0.")
              + h4("Why the identity matters")
              + p("AI = IA = A for every matrix A that can be multiplied with I. It is the reason a "
                  "matrix can have an inverse at all: A⁻¹ is defined by A A⁻¹ = I.")
              + h4("Reading the diagram")
              + p("Each panel shows the pattern only. A diagonal matrix may have any numbers on its "
                  "diagonal - what makes it diagonal is the ring of zeros everywhere else."),
              "mx2_types", syllabus_item="1.2"),
         card("2.2 Row, column, rectangular and triangular matrices",
              h4("Definitions")
              + ul("<b>Row matrix</b>: a single row (order 1 × n).",
                   "<b>Column matrix</b> (column vector): a single column (order m × 1).",
                   "<b>Rectangular</b>: rows ≠ columns.",
                   "<b>Upper triangular</b>: square, every entry below the main diagonal is zero.",
                   "<b>Lower triangular</b>: square, every entry above the main diagonal is zero.")
              + h4("Worked reading")
              + p(mx(["2", "7"], ["0", "4"]) + " is upper triangular and " + mx(["2", "0"], ["5", "4"])
                  + " is lower triangular. A matrix can be both only if it is diagonal.")
              + h4("Useful fact")
              + p("The determinant of a triangular matrix is simply the product of its diagonal "
                  "entries, so |" + mx(["2", "7"], ["0", "4"]) + "| = 2 × 4 = 8 - no expansion needed.")
              + p("A row matrix is the same idea as a vector, so Unit 3 of semester 1 (vectors) and "
                  "this unit speak the same language."),
              examples=[], syllabus_item="1.2"),
         card("2.3 Symmetric and skew-symmetric matrices",
              h4("Definitions")
              + ul("<b>Symmetric</b>: Aᵀ = A, so aᵢⱼ = aⱼᵢ - the entries mirror across the main "
                   "diagonal.",
                   "<b>Skew-symmetric</b>: Aᵀ = −A, so aᵢⱼ = −aⱼᵢ and every diagonal entry must be 0.")
              + h4("A construction that always works")
              + p("For any square matrix A, the sum A + Aᵀ is symmetric and the difference A − Aᵀ is "
                  "skew-symmetric. Check: (A + Aᵀ)ᵀ = Aᵀ + A = A + Aᵀ.")
              + h4("Worked example")
              + p("A = " + mx(["1", "2"], ["3", "4"]) + " gives Aᵀ = " + mx(["1", "3"], ["2", "4"])
                  + " and A + Aᵀ = " + mx(["2", "5"], ["5", "8"]) + ", which is symmetric because "
                  "5 = 5 across the diagonal.")
              + p("Symmetric matrices appear wherever a quantity is measured in both directions: a "
                  "distance table, a stiffness matrix, a correlation table."),
              examples=["mm1n8"], syllabus_item="1.2"),
         card("2.4 Singular and non-singular matrices",
              h4("Definitions")
              + ul("<b>Non-singular</b>: |A| ≠ 0. The matrix has an inverse.",
                   "<b>Singular</b>: |A| = 0. No inverse exists.")
              + h4("Why the determinant decides")
              + p("The inverse formula is A⁻¹ = adj A ÷ |A|. If |A| = 0 the division is impossible, "
                  "so the inverse does not exist - it is not that the answer is zero, it is that "
                  "there is no answer.")
              + h4("The geometric reading")
              + p("Two equations with determinant 0 have proportional rows, so their lines are "
                  "parallel (no solution) or identical (infinitely many). A matrix with an inverse "
                  "always gives exactly one solution.")
              + h4("Common mistake")
              + p("Writing A⁻¹ = 1/|A| without the adjoint. The determinant is a number, the adjoint "
                  "is a matrix, and the inverse is the adjoint scaled by that number."),
              examples=["mm1n17"], syllabus_item="1.5"),
     ]},

    {"title": tr("3. Addition, Subtraction and Scalar Multiplication"),
     "items": [
         card("3.1 Adding and subtracting matrices",
              h4("Rule")
              + p("Two matrices can be added or subtracted only when they have the <b>same order</b>. "
                  "The answer keeps that order and each entry is added or subtracted separately: "
                  "<b>Cᵢⱼ = aᵢⱼ ± bᵢⱼ</b>.")
              + h4("Worked example")
              + p("A = " + mx(["1", "2", "3"], ["4", "5", "6"]) + " and B = "
                  + mx(["6", "5", "4"], ["3", "2", "1"]) + " give A + B = "
                  + mx(["7", "7", "7"], ["7", "7", "7"]) + " and A − B = "
                  + mx(["−5", "−3", "−1"], ["1", "3", "5"]) + ".")
              + h4("Laws")
              + ul("A + B = B + A (addition commutes)",
                   "A + (B + C) = (A + B) + C (associates)",
                   "A + O = A, and A + (−A) = O")
              + p("So the change B − A is not the same matrix as A − B: subtraction reverses every "
                  "sign."),
              examples=["mm1n5"], syllabus_item="1.3"),
         card("3.2 Multiplication by a scalar",
              h4("Rule")
              + p("A scalar is a single number. Multiply <i>every</i> entry: <b>(kA)ᵢⱼ = k aᵢⱼ</b>. "
                  "The order does not change.")
              + h4("Worked example")
              + p("4A with A = " + mx(["1/2", "3"], ["−1", "1/4"]) + " gives "
                  + mx(["2", "12"], ["−4", "1"]) + ".")
              + h4("Laws")
              + ul("k(A + B) = kA + kB", "(k + m)A = kA + mA", "k(mA) = (km)A",
                   "1A = A and 0A = O")
              + h4("Common mistake")
              + p("Scaling only the first row or only the diagonal. A scalar multiplies every entry, "
                  "which is exactly why kA ≠ A for most matrices - and why 2I is not the identity."),
              examples=["mm1n7"], syllabus_item="1.3"),
         card("3.3 Mixed expressions such as 3A − 2B",
              h4("Method")
              + ol("Work out 3A on its own.",
                   "Work out 2B on its own.",
                   "Subtract entry by entry, keeping the order of the two matrices.")
              + h4("Worked example")
              + p("A = " + mx(["2", "−1"], ["3", "0"]) + " and B = " + mx(["1", "4"], ["−2", "5"])
                  + ": 3A = " + mx(["6", "−3"], ["9", "0"]) + ", 2B = " + mx(["2", "8"], ["−4", "10"])
                  + ", so 3A − 2B = " + mx(["4", "−11"], ["13", "−10"]) + ".")
              + h4("Conditions")
              + ul("Both matrices must have the same order.",
                   "There is no matrix division: never write 3A/2B.",
                   "A scalar outside the bracket multiplies every entry inside it.")
              + p("This is the sort of expression that appears when you compute A² − 3A + 2I in the "
                  "next section."),
              examples=["mm1n6"], syllabus_item="1.3"),
         card("3.4 Checking your arithmetic",
              h4("Three quick checks")
              + ol("Order check: both input matrices and the answer must carry the same order.",
                   "Sign check: in a subtraction, the second matrix reverses every one of its signs.",
                   "Corner check: recompute the top-left and the bottom-right entries by hand; if "
                   "either disagrees, the whole matrix is suspect.")
              + h4("Why it matters later")
              + p("The same three checks catch errors in AB, in the adjoint and in Cramer's rule. "
                  "Almost every lost mark in a matrices question is an arithmetic slip in one entry, "
                  "not a wrong method.")
              + p("Keep the working as a matrix - write the unsimplified sum first, then simplify in "
                  "a second line. That way the marker can see the method even if one entry is wrong."),
              syllabus_item="1.3"),
     ]},

    {"title": tr("4. Product of Two Matrices"),
     "items": [
         card("4.1 Row into column: the definition of AB",
              h4("Definition")
              + p("The product AB exists only when the number of <b>columns of A</b> equals the "
                  "number of <b>rows of B</b>. The answer then has the rows of A and the columns "
                  "of B: an m × n matrix times an n × p matrix gives an m × p matrix.")
              + p("Each entry is a row-times-column sum: <b>(AB)ᵢⱼ = aᵢ₁b₁ⱼ + aᵢ₂b₂ⱼ + ... + aᵢₙbₙⱼ</b>.")
              + h4("Step by step")
              + ol("Take row i of A and column j of B.",
                   "Multiply the first pair, the second pair, and so on.",
                   "Add the products - that single number is the (i, j) entry of AB.")
              + h4("Worked example")
              + p("A = " + mx(["1", "2"], ["3", "4"]) + " and B = " + mx(["2", "0"], ["1", "3"])
                  + " give AB = " + mx(["4", "6"], ["10", "12"]) + ": the top-left entry is "
                  "1(2) + 2(1) = 4 and the bottom-right is 3(0) + 4(3) = 12."),
              "mx3_product", examples=["mm1n9"], syllabus_item="1.4"),
         card("4.2 AB is usually not BA",
              h4("The rule")
              + p("Matrix multiplication is <b>not commutative</b>: AB ≠ BA in general. Often both "
                  "products exist but they are different matrices; sometimes only one of them can "
                  "be formed at all.")
              + h4("Worked comparison")
              + p("With A = " + mx(["1", "2"], ["3", "4"]) + " and B = " + mx(["2", "0"], ["1", "3"])
                  + ", AB = " + mx(["4", "6"], ["10", "12"]) + " but BA = "
                  + mx(["2", "4"], ["10", "14"]) + ". Same order, different entries.")
              + h4("What does survive")
              + ul("(AB)C = A(BC) - multiplication is associative.",
                   "A(B + C) = AB + AC - it distributes over addition.",
                   "(AB)ᵀ = BᵀAᵀ and (AB)⁻¹ = B⁻¹A⁻¹ - both reverse the order.")
              + h4("Common mistake")
              + p("Swapping AB for BA to make the answer look nicer. In a transformation problem "
                  "that changes the physical meaning: rotate-then-scale is not scale-then-rotate."),
              examples=["mm1n10"], syllabus_item="1.4"),
         card("4.3 Checking conformability before you multiply",
              h4("The size test")
              + p("Write the two orders side by side and cross out the inner numbers: "
                  "<b>(m × n)(n × p) = m × p</b>. If the inner numbers differ, the product does not "
                  "exist - no working, no marks.")
              + h4("Examples of the test")
              + table(["Product", "Inner numbers", "Result"],
                      [("(2 × 3)(3 × 2)", "3 and 3 - match", "2 × 2"),
                       ("(3 × 2)(2 × 4)", "2 and 2 - match", "3 × 4"),
                       ("(2 × 3)(2 × 3)", "3 and 2 - differ", "not defined")])
              + h4("Worked example")
              + p("A = " + mx(["1", "2", "3"], ["4", "5", "6"]) + " is 2 × 3 and B = "
                  + mx(["1", "0"], ["2", "1"], ["0", "3"]) + " is 3 × 2, so AB exists and is 2 × 2: "
                  "AB = " + mx(["5", "11"], ["14", "23"]) + ".")
              + p("Note that BA would be 3 × 3 - a different size entirely. The two products cannot "
                  "be compared entry by entry."),
              examples=["mm1n11"], syllabus_item="1.4"),
         card("4.4 Powers of a matrix and matrix polynomials",
              h4("Definition")
              + p("A² means A × A, so it exists only for a square matrix. The expression "
                  "<b>A² − 3A + 2I</b> is evaluated term by term: a matrix minus a matrix plus a "
                  "matrix, where 2I is <i>not</i> the number 2.")
              + h4("Worked example")
              + p("A = " + mx(["2", "1"], ["1", "0"]) + ": A² = " + mx(["5", "2"], ["2", "1"])
                  + ", 3A = " + mx(["6", "3"], ["3", "0"]) + ", 2I = " + mx(["2", "0"], ["0", "2"])
                  + ", so A² − 3A + 2I = " + mx(["1", "−1"], ["−1", "3"]) + ".")
              + h4("The trap")
              + p("Filling the 2I positions with 2 instead of 2 on the diagonal and 0 elsewhere. In "
                  "an expression like this, the number k always means kI for the size of A.")
              + sc("Is (A + B)² equal to A² + 2AB + B²?",
                   "Only when AB = BA. In general (A + B)² = A² + AB + BA + B², and AB + BA is not "
                   "2AB."),
              examples=["mm1n12"], syllabus_item="1.4"),
         card("4.5 Zero products and unknown entries",
              h4("A surprise that is not a surprise")
              + p("AB = O does not force A = O or B = O. Numbers behave differently: if xy = 0 then "
                  "x = 0 or y = 0, but matrices can multiply to the zero matrix while both are "
                  "non-zero.")
              + h4("Example")
              + p("A = " + mx(["1", "1"], ["1", "1"]) + " and B = " + mx(["1", "−1"], ["−1", "1"])
                  + " both have non-zero entries, yet AB = " + mx(["0", "0"], ["0", "0"]) + ".")
              + h4("Finding an unknown entry")
              + ol("Multiply the matrices completely, keeping the unknown in place.",
                   "Compare each entry with the given product.",
                   "Solve the resulting equation, then check it in a second entry.")
              + p("That check is essential: a wrong k often satisfies one entry and fails the next."),
              examples=["mm1n13", "mm1n14"], syllabus_item="1.4"),
     ]},

    {"title": tr("5. Adjoint and Inverse of a 2x2 Matrix"),
     "items": [
         card("5.1 Determinant and adjoint of a 2x2 matrix",
              h4("Definitions")
              + p("For A = " + mx(["a", "b"], ["c", "d"]) + " the determinant is <b>|A| = ad − bc</b> "
                  "and the adjoint is <b>adj A = " + mx(["d", "−b"], ["−c", "a"]) + "</b>: swap the "
                  "main diagonal and change the sign of the other two entries.")
              + h4("Worked example")
              + p("A = " + mx(["3", "1"], ["5", "2"]) + ": |A| = 3(2) − 1(5) = 1 and adj A = "
                  + mx(["2", "−1"], ["−5", "3"]) + ". Because |A| = 1 the inverse equals the adjoint.")
              + h4("Why the adjoint works")
              + p("Multiplying A by its adjoint always gives |A|I: the diagonal entries become ad − bc "
                  "and the off-diagonal entries cancel. Dividing by |A| therefore leaves exactly I.")
              + h4("Common mistake")
              + p("Changing the signs of the diagonal instead of the off-diagonal. Write the pattern "
                  "once - keep a and d, flip b and c - and copy it every time."),
              "mx4_inverse2", examples=["mm1n15"], syllabus_item="1.5"),
         card("5.2 The inverse formula and the verification",
              h4("Formula")
              + p("<b>A⁻¹ = adj A ÷ |A| = (1/|A|) × " + mx(["d", "−b"], ["−c", "a"]) + "</b>, "
                  "defined only when |A| ≠ 0.")
              + h4("Worked example")
              + p("A = " + mx(["2", "3"], ["1", "4"]) + ": |A| = 8 − 3 = 5, adj A = "
                  + mx(["4", "−3"], ["−1", "2"]) + ", so A⁻¹ = (1/5)" + mx(["4", "−3"], ["−1", "2"])
                  + " = " + mx(["4/5", "−3/5"], ["−1/5", "2/5"]) + ".")
              + h4("Always verify")
              + p("Multiply A by A⁻¹ and confirm that the result is I. One line of checking catches "
                  "every sign slip: the top-left entry must come out as 1 and the others as 0.")
              + h4("Two properties worth remembering")
              + ul("(A⁻¹)⁻¹ = A", "(AB)⁻¹ = B⁻¹A⁻¹, and the order reverses")
              + p("The inverse is how a matrix is 'divided out': to solve AX = B you multiply on the "
                  "left by A⁻¹, giving X = A⁻¹B."),
              examples=["mm1n16"], syllabus_item="1.5"),
         card("5.3 Reading the answer: what the inverse tells you",
              h4("Three readings")
              + table(["Value of |A|", "Inverse", "Meaning for two equations"],
                      [("|A| ≠ 0", "exists", "one unique solution"),
                       ("|A| = 0, constants inconsistent", "does not exist", "no solution - parallel lines"),
                       ("|A| = 0, rows proportional", "does not exist", "infinitely many solutions")])
              + h4("Engineering reading")
              + p("A singular coefficient matrix means the equations are not independent: one of them "
                  "repeats information already given. In a circuit or a truss that is the signature "
                  "of a redundant or a floating element.")
              + h4("Common mistake")
              + p("Finding |A| = 0 and then writing A⁻¹ = O. A zero determinant means the inverse "
                  "does not exist, not that it is the zero matrix."),
              syllabus_item="1.5"),
     ]},

    {"title": tr("6. Adjoint, Inverse (3x3) and Two Equations"),
     "items": [
         card("6.1 Minors, cofactors and the 3x3 determinant",
              h4("Definitions")
              + p("The <b>minor</b> Mᵢⱼ of an entry is the 2 × 2 determinant left after deleting its "
                  "row and column. The <b>cofactor</b> carries the positional sign: "
                  "<b>Cᵢⱼ = (−1)^(i+j) Mᵢⱼ</b>.")
              + h4("The sign board")
              + p("+ − + / − + − / + − + . The sign belongs to the position, not to the number, so a "
                  "negative entry inside the matrix does not change the pattern.")
              + h4("Worked example")
              + p("A = " + mx(["2", "1", "3"], ["0", "4", "1"], ["5", "2", "0"]) + ": expanding "
                  "along the first row gives 2(0 − 2) − 1(0 − 5) + 3(0 − 20) = −4 + 5 − 60 = <b>−59</b>.")
              + h4("Shortcut")
              + p("Expand along the row or column with the most zeros. Every zero removes a whole "
                  "2 × 2 determinant from the work."),
              examples=["mm1n18"], syllabus_item="1.5"),
         card("6.2 The adjoint of a 3x3 matrix",
              h4("Method")
              + ol("Write the cofactor of all nine entries.",
                   "Transpose that cofactor matrix - its rows become the columns of adj A.")
              + h4("Why the transpose")
              + p("A × (transpose of its cofactor matrix) = |A|I. That identity is exactly what makes "
                  "the inverse formula work, and it holds for every order.")
              + h4("Worked example")
              + p("A = " + mx(["1", "2", "3"], ["0", "1", "4"], ["5", "6", "0"]) + " has |A| = 1 and "
                  "cofactor matrix " + mx(["−24", "20", "−5"], ["18", "−15", "4"], ["5", "−4", "1"])
                  + ", so adj A = " + mx(["−24", "18", "5"], ["20", "−15", "−4"], ["−5", "4", "1"])
                  + " - the entries have moved across the diagonal.")
              + h4("Common mistake")
              + p("Forgetting the transpose and calling the cofactor matrix the adjoint. The two are "
                  "equal only when the cofactor matrix happens to be symmetric."),
              "mx5_adj3", examples=["mm1n19"], syllabus_item="1.5"),
         card("6.3 The inverse of a 3x3 matrix",
              h4("Formula")
              + p("<b>A⁻¹ = adj A ÷ |A|</b>, again only when |A| ≠ 0. Every entry of the adjoint is "
                  "divided by the same number.")
              + h4("Worked example")
              + p("A = " + mx(["1", "1", "1"], ["1", "2", "3"], ["1", "4", "9"]) + ": |A| = 2 and "
                  "adj A = " + mx(["6", "−5", "1"], ["−6", "8", "−2"], ["2", "−3", "1"]) + ", so "
                  "A⁻¹ = (1/2)" + mx(["6", "−5", "1"], ["−6", "8", "−2"], ["2", "−3", "1"]) + ".")
              + h4("Work order that avoids errors")
              + ol("Find |A| first. If it is 0, stop - there is no inverse.",
                   "Build the cofactor matrix, one 2 × 2 determinant at a time.",
                   "Transpose to get adj A, then divide every entry by |A|.",
                   "Check one row of A × A⁻¹: it must give the matching row of I.")
              + p("A 3 × 3 inverse needs nine minors, so a tidy layout on paper matters more than "
                  "speed."),
              examples=["mm1n20"], syllabus_item="1.5"),
         card("6.4 Cramer's rule for two equations",
              h4("Setup")
              + p("For a₁x + b₁y = c₁ and a₂x + b₂y = c₂ write <b>D = a₁b₂ − a₂b₁</b>, then replace "
                  "the x-column by the constants to get Dₓ, and the y-column to get D_y.")
              + p("<b>x = Dₓ/D and y = D_y/D</b>, valid only when D ≠ 0.")
              + h4("Worked example")
              + p("x + y = 7 and 2x − y = 2: D = (1)(−1) − (2)(1) = −3, Dₓ = (7)(−1) − (2)(1) = −9, "
                  "D_y = (1)(2) − (2)(7) = −12. So x = 3 and y = 4, which satisfy both equations.")
              + h4("Reading the three cases")
              + p("D ≠ 0 gives one solution; D = 0 with Dₓ or D_y non-zero gives none; D = Dₓ = D_y = 0 "
                  "gives infinitely many. The diagram shows the three pictures.")
              + h4("Common mistake")
              + p("Replacing the wrong column. Dₓ swaps the coefficients of x, D_y swaps the "
                  "coefficients of y - never the constants."),
              "mx6_solve", examples=["mm1n21"], syllabus_item="1.6"),
         card("6.5 The inverse-matrix method",
              h4("Method")
              + p("Write the pair as AX = B with A the coefficient matrix, X the column of unknowns "
                  "and B the column of constants. Then <b>X = A⁻¹B</b>.")
              + h4("Worked example")
              + p("2x + y = 8 and x + 3y = 9: A = " + mx(["2", "1"], ["1", "3"]) + " has |A| = 5 and "
                  "A⁻¹ = (1/5)" + mx(["3", "−1"], ["−1", "2"]) + ", so X = A⁻¹B = "
                  "(1/5)" + mx(["3", "−1"], ["−1", "2"]) + mx(["8"], ["9"]) + " = "
                  + mx(["3"], ["2"]) + ". Hence x = 3 and y = 2.")
              + h4("Word problems")
              + p("Translate first, solve second. 'Two numbers add to 30 and differ by 8' becomes "
                  "x + y = 30 and x − y = 8, which gives x = 19 and y = 11.")
              + h4("Which method should I use?")
              + ul("Cramer's rule is faster when you only need one unknown.",
                   "The inverse method is better when several right-hand sides share the same A.",
                   "Both need the same determinant - compute it once and reuse it.")
              + p("Always substitute the answer back into the original equations; that single step "
                  "converts a guess into a verified solution."),
              examples=["mm1n22", "mm1n23"], syllabus_item="1.6"),
         card("6.6 Consistent, inconsistent and dependent equations",
              h4("Three cases from the determinant")
              + table(["Determinants", "Name", "Geometry"],
                      [("D ≠ 0", "consistent, independent", "two lines crossing at one point"),
                       ("D = 0, Dₓ or D_y ≠ 0", "inconsistent", "parallel lines - no solution"),
                       ("D = Dₓ = D_y = 0", "dependent", "the same line twice - infinitely many")])
              + h4("Worked example")
              + p("2x + 3y = 7 with 4x + 6y = 14: the second row is twice the first, so D = 0 and "
                  "Dₓ = D_y = 0 - every point of the line is a solution. Change the right side to 20 "
                  "and the same left side becomes 4x + 6y = 20, so Dₓ ≠ 0 and there is no solution.")
              + h4("What to write in an exam")
              + p("State D, then state the case by name, then give the conclusion. 'D = 0 and Dₓ ≠ 0, "
                  "so the equations are inconsistent and have no solution' earns the mark; a bare "
                  "'no solution' may not.")
              + h4("Engineering reading")
              + p("A dependent pair describes one physical law written twice; an inconsistent pair "
                  "describes two laws that contradict each other - usually a sign error in the data."),
              examples=["mm1n24"], syllabus_item="1.6"),
     ]},

    {"title": tr("7. Practice Questions with Model Answers"),
     "items": []},  # filled by the builder from EXAM
]

NUMERICALS = [
    {"id": "mm1n1",
     "q": tr("Write the order of A = " + mx(["2", "−1", "3"], ["0", "5", "4"])
             + " and state the values of a₁₃ and a₂₂."),
     "a": tr(p("A has 2 rows and 3 columns, so the <b>order is 2 × 3</b> and it holds 2 × 3 = 6 "
               "entries.")
            + p("a₁₃ means row 1, column 3, so <b>a₁₃ = 3</b>.")
            + p("a₂₂ means row 2, column 2, so <b>a₂₂ = 5</b>.")
            + p("There is no a₃₁ because the matrix has only two rows."))},
    {"id": "mm1n2",
     "q": tr("If " + mx(["x + 1", "3"], ["2", "y − 2"]) + " = " + mx(["5", "3"], ["2", "4"])
             + ", find x and y."),
     "a": tr(p("Both matrices are 2 × 2, so equality means each matching pair of entries is equal.")
            + p("Top-left: x + 1 = 5, hence <b>x = 4</b>.")
            + p("Bottom-right: y − 2 = 4, hence <b>y = 6</b>.")
            + p("The other two entries are 3 = 3 and 2 = 2, which are already satisfied, so the "
                "answer is consistent."))},
    {"id": "mm1n3",
     "q": tr("Construct the 2 × 3 matrix whose entries are aᵢⱼ = 2i + j."),
     "a": tr(p("Substitute the six (i, j) pairs, taking i = 1, 2 and j = 1, 2, 3.")
            + p(mx(["3", "4", "5"], ["5", "6", "7"]))
            + p("Row 1 (i = 1): 2 + 1 = 3, 2 + 2 = 4, 2 + 3 = 5.")
            + p("Row 2 (i = 2): 4 + 1 = 5, 4 + 2 = 6, 4 + 3 = 7."))},
    {"id": "mm1n4",
     "q": tr("Find the transpose of A = " + mx(["1", "2", "3"], ["4", "5", "6"])
             + " and show that (Aᵀ)ᵀ = A."),
     "a": tr(p("Turn rows into columns: the first row (1, 2, 3) becomes the first column of Aᵀ.")
            + p("Aᵀ = " + mx(["1", "4"], ["2", "5"], ["3", "6"]) + " - order 3 × 2.")
            + p("Transposing Aᵀ again returns a 2 × 3 matrix whose rows are the columns of Aᵀ, that "
                "is " + mx(["1", "2", "3"], ["4", "5", "6"]) + " = A. Hence <b>(Aᵀ)ᵀ = A</b>."))},
    {"id": "mm1n5",
     "q": tr("For A = " + mx(["1", "2", "3"], ["4", "5", "6"]) + " and B = "
             + mx(["6", "5", "4"], ["3", "2", "1"]) + ", find A + B and A − B."),
     "a": tr(p("Both matrices are 2 × 3, so both operations are allowed and each entry is combined "
               "separately.")
            + p("A + B = " + mx(["7", "7", "7"], ["7", "7", "7"]) + ".")
            + p("A − B = " + mx(["−5", "−3", "−1"], ["1", "3", "5"]) + ".")
            + p("Check one entry: 1 + 6 = 7 and 1 − 6 = −5, as shown."))},
    {"id": "mm1n6",
     "q": tr("If A = " + mx(["2", "−1"], ["3", "0"]) + " and B = " + mx(["1", "4"], ["−2", "5"])
             + ", evaluate 3A − 2B."),
     "a": tr(p("Scale first: 3A = " + mx(["6", "−3"], ["9", "0"]) + " and 2B = "
               + mx(["2", "8"], ["−4", "10"]) + ".")
            + p("Subtract entry by entry: 3A − 2B = " + mx(["4", "−11"], ["13", "−10"]) + ".")
            + p("Check the top-left entry: 6 − 2 = 4. Because B has negative entries, subtracting "
                "2B adds in places - 0 − 10 = −10, not +10."))},
    {"id": "mm1n7",
     "q": tr("Find 4A when A = " + mx(["1/2", "3"], ["−1", "1/4"]) + "."),
     "a": tr(p("A scalar multiplies every entry, so each of the four numbers is multiplied by 4.")
            + p("4A = " + mx(["2", "12"], ["−4", "1"]) + ".")
            + p("Check: 4 × 1/2 = 2, 4 × 3 = 12, 4 × (−1) = −4, 4 × 1/4 = 1.")
            + p("The order stays 2 × 2 - a scalar never changes the shape of a matrix."))},
    {"id": "mm1n8",
     "q": tr("Show that A + Aᵀ is symmetric for A = " + mx(["1", "2"], ["3", "4"]) + "."),
     "a": tr(p("Aᵀ = " + mx(["1", "3"], ["2", "4"]) + ", so A + Aᵀ = "
               + mx(["2", "5"], ["5", "8"]) + ".")
            + p("The entries across the main diagonal are equal (5 = 5), so the sum is symmetric.")
            + p("General proof: (A + Aᵀ)ᵀ = Aᵀ + (Aᵀ)ᵀ = Aᵀ + A = A + Aᵀ, which is exactly the "
                "definition of a symmetric matrix."))},
    {"id": "mm1n9",
     "q": tr("Multiply A = " + mx(["1", "2"], ["3", "4"]) + " and B = "
             + mx(["2", "0"], ["1", "3"]) + " to find AB."),
     "a": tr(p("Each entry of AB is a row of A times a column of B.")
            + p("Top-left: 1(2) + 2(1) = 4. Top-right: 1(0) + 2(3) = 6.")
            + p("Bottom-left: 3(2) + 4(1) = 10. Bottom-right: 3(0) + 4(3) = 12.")
            + p("So AB = " + mx(["4", "6"], ["10", "12"]) + ", a 2 × 2 matrix."))},
    {"id": "mm1n10",
     "q": tr("For the same A = " + mx(["1", "2"], ["3", "4"]) + " and B = "
             + mx(["2", "0"], ["1", "3"]) + ", find BA and compare it with AB."),
     "a": tr(p("BA takes rows of B into columns of A.")
            + p("Top-left: 2(1) + 0(3) = 2. Top-right: 2(2) + 0(4) = 4.")
            + p("Bottom-left: 1(1) + 3(3) = 10. Bottom-right: 1(2) + 3(4) = 14.")
            + p("BA = " + mx(["2", "4"], ["10", "14"]) + " while AB = " + mx(["4", "6"], ["10", "12"])
                + ", so <b>AB ≠ BA</b>: matrix multiplication does not commute."))},
    {"id": "mm1n11",
     "q": tr("Find AB for the 2 × 3 matrix A = " + mx(["1", "2", "3"], ["4", "5", "6"])
             + " and the 3 × 2 matrix B = " + mx(["1", "0"], ["2", "1"], ["0", "3"])
             + ", and state the order of the product."),
     "a": tr(p("Inner numbers 3 and 3 match, so AB exists and its order is 2 × 2.")
            + p("Row 1: 1(1) + 2(2) + 3(0) = 5 and 1(0) + 2(1) + 3(3) = 11.")
            + p("Row 2: 4(1) + 5(2) + 6(0) = 14 and 4(0) + 5(1) + 6(3) = 23.")
            + p("AB = " + mx(["5", "11"], ["14", "23"]) + "."))},
    {"id": "mm1n12",
     "q": tr("If A = " + mx(["2", "1"], ["1", "0"]) + ", evaluate A² − 3A + 2I."),
     "a": tr(p("A² = A × A = " + mx(["5", "2"], ["2", "1"]) + ".")
            + p("3A = " + mx(["6", "3"], ["3", "0"]) + " and 2I = " + mx(["2", "0"], ["0", "2"])
                + " - the 2 sits on the diagonal only.")
            + p("A² − 3A + 2I = " + mx(["5 − 6 + 2", "2 − 3 + 0"], ["2 − 3 + 0", "1 − 0 + 2"])
                + " = " + mx(["1", "−1"], ["−1", "3"]) + "."))},
    {"id": "mm1n13",
     "q": tr("Show that AB can be the zero matrix even when neither A nor B is zero, using "
             "A = " + mx(["1", "1"], ["1", "1"]) + " and B = " + mx(["1", "−1"], ["−1", "1"]) + "."),
     "a": tr(p("Multiply row by column: top-left 1(1) + 1(−1) = 0; top-right 1(−1) + 1(1) = 0.")
            + p("Bottom-left 1(1) + 1(−1) = 0; bottom-right 1(−1) + 1(1) = 0.")
            + p("So AB = " + mx(["0", "0"], ["0", "0"]) + " = O while both matrices have non-zero "
                "entries. Matrices have no zero-product rule."))},
    {"id": "mm1n14",
     "q": tr("Find k if A = " + mx(["1", "2"], ["3", "k"]) + " satisfies A² = "
             + mx(["7", "10"], ["15", "22"]) + "."),
     "a": tr(p("First find A² = " + mx(["1 + 6", "2 + 2k"], ["3 + 3k", "6 + k²"]) + ".")
            + p("Comparing the top-right entries: 2 + 2k = 10, so <b>k = 4</b>.")
            + p("Check with the other entries: 3 + 3(4) = 15 (matches) and 6 + 16 = 22 (matches), so "
                "k = 4 is consistent."))},
    {"id": "mm1n15",
     "q": tr("Find the determinant, the adjoint and the inverse of A = "
             + mx(["3", "1"], ["5", "2"]) + "."),
     "a": tr(p("|A| = 3(2) − 1(5) = <b>1</b>, so the matrix is non-singular.")
            + p("Swap the diagonal and negate the other two: adj A = " + mx(["2", "−1"], ["−5", "3"])
                + ".")
            + p("A⁻¹ = adj A ÷ |A| = " + mx(["2", "−1"], ["−5", "3"]) + " because dividing by 1 "
                "changes nothing.")
            + p("Check: " + mx(["3", "1"], ["5", "2"]) + mx(["2", "−1"], ["−5", "3"]) + " = "
                + mx(["1", "0"], ["0", "1"]) + " = I."))},
    {"id": "mm1n16",
     "q": tr("Find A⁻¹ for A = " + mx(["2", "3"], ["1", "4"]) + " and verify the answer."),
     "a": tr(p("|A| = 2(4) − 3(1) = 5, which is not zero, so the inverse exists.")
            + p("adj A = " + mx(["4", "−3"], ["−1", "2"]) + ", so A⁻¹ = (1/5)"
                + mx(["4", "−3"], ["−1", "2"]) + " = " + mx(["4/5", "−3/5"], ["−1/5", "2/5"]) + ".")
            + p("Verification: row 1 of A into column 1 of A⁻¹ gives 2(4/5) + 3(−1/5) = 1, and into "
                "column 2 gives 2(−3/5) + 3(2/5) = 0. So A A⁻¹ = I."))},
    {"id": "mm1n17",
     "q": tr("For what values of x is A = " + mx(["x", "2"], ["8", "x"]) + " singular?"),
     "a": tr(p("A square matrix is singular when its determinant is zero.")
            + p("|A| = x·x − 2(8) = x² − 16. Setting x² − 16 = 0 gives x = 4 or x = −4.")
            + p("So A has <b>no inverse when x = 4 or x = −4</b>; for every other x the inverse exists.")
            + p("Note the two answers: a squared equation never gives just one root."))},
    {"id": "mm1n18",
     "q": tr("Evaluate |A| for A = " + mx(["2", "1", "3"], ["0", "4", "1"], ["5", "2", "0"])
             + " by expanding along the first row."),
     "a": tr(p("|A| = 2(4(0) − 1(2)) − 1(0(0) − 1(5)) + 3(0(2) − 4(5)).")
            + p("= 2(0 − 2) − 1(0 − 5) + 3(0 − 20) = −4 + 5 − 60.")
            + p("So <b>|A| = −59</b>.")
            + p("The middle term has a minus sign in front of it, and the inner minus inside the "
                "bracket makes it positive: −1 × (−5) = +5."))},
    {"id": "mm1n19",
     "q": tr("Find the adjoint of A = " + mx(["1", "2", "3"], ["0", "1", "4"], ["5", "6", "0"]) + "."),
     "a": tr(p("Cofactors: C₁₁ = −24, C₁₂ = 20, C₁₃ = −5; C₂₁ = 18, C₂₂ = −15, C₂₃ = 4; "
               "C₃₁ = 5, C₃₂ = −4, C₃₃ = 1.")
            + p("Cofactor matrix = " + mx(["−24", "20", "−5"], ["18", "−15", "4"], ["5", "−4", "1"])
                + ".")
            + p("Transpose it: adj A = " + mx(["−24", "18", "5"], ["20", "−15", "−4"], ["−5", "4", "1"])
                + ".")
            + p("Because |A| = 1 here, the same array is also A⁻¹."))},
    {"id": "mm1n20",
     "q": tr("Find A⁻¹ for A = " + mx(["1", "1", "1"], ["1", "2", "3"], ["1", "4", "9"]) + "."),
     "a": tr(p("Expand along row 1: |A| = 1(18 − 12) − 1(9 − 3) + 1(4 − 2) = 6 − 6 + 2 = 2.")
            + p("Cofactors give " + mx(["6", "−6", "2"], ["−5", "8", "−3"], ["1", "−2", "1"])
                + ", so adj A = " + mx(["6", "−5", "1"], ["−6", "8", "−2"], ["2", "−3", "1"]) + ".")
            + p("A⁻¹ = (1/2)" + mx(["6", "−5", "1"], ["−6", "8", "−2"], ["2", "−3", "1"]) + ".")
            + p("Check the top-left entry of A A⁻¹: 1(3) + 1(−3) + 1(1) = 1, as required."))},
    {"id": "mm1n21",
     "q": tr("Solve x + y = 7 and 2x − y = 2 by Cramer's rule."),
     "a": tr(p("Coefficient matrix A = " + mx(["1", "1"], ["2", "−1"])
               + " gives D = 1(−1) − 1(2) = <b>−3</b>.")
            + p("Replace the x-column by " + mx(["7"], ["2"]) + ": Dₓ = 7(−1) − 2(1) = −9.")
            + p("Replace the y-column: D_y = 1(2) − 2(7) = −12.")
            + p("x = Dₓ/D = −9/−3 = <b>3</b> and y = D_y/D = −12/−3 = <b>4</b>.")
            + p("Check: 3 + 4 = 7 and 2(3) − 4 = 2, so both equations are satisfied."))},
    {"id": "mm1n22",
     "q": tr("Solve 2x + y = 8 and x + 3y = 9 by the inverse-matrix method."),
     "a": tr(p("Write AX = B with A = " + mx(["2", "1"], ["1", "3"]) + ", B = "
               + mx(["8"], ["9"]) + ".")
            + p("|A| = 6 − 1 = 5 and adj A = " + mx(["3", "−1"], ["−1", "2"])
                + ", so A⁻¹ = (1/5)" + mx(["3", "−1"], ["−1", "2"]) + ".")
            + p("X = A⁻¹B = (1/5)" + mx(["24 − 9"], ["−8 + 18"]) + " = (1/5)"
                + mx(["15"], ["10"]) + " = " + mx(["3"], ["2"]) + ".")
            + p("Hence x = 3 and y = 2, which check out in both original equations."))},
    {"id": "mm1n23",
     "q": tr("Two numbers add up to 30 and differ by 8. Set up the equations as matrices and "
             "solve them."),
     "a": tr(p("Let the numbers be x and y: x + y = 30 and x − y = 8, so A = "
               + mx(["1", "1"], ["1", "−1"]) + " and B = " + mx(["30"], ["8"]) + ".")
            + p("|A| = −1 − 1 = −2, adj A = " + mx(["−1", "−1"], ["−1", "1"])
                + ", so A⁻¹ = (1/−2)" + mx(["−1", "−1"], ["−1", "1"]) + ".")
            + p("X = A⁻¹B = (1/−2)" + mx(["−38"], ["−22"]) + " = " + mx(["19"], ["11"]) + ".")
            + p("The numbers are <b>19 and 11</b>: 19 + 11 = 30 and 19 − 11 = 8."))},
    {"id": "mm1n24",
     "q": tr("Decide the number of solutions for (a) 2x + 3y = 7 with 4x + 6y = 14 and "
             "(b) 2x + 3y = 7 with 4x + 6y = 20."),
     "a": tr(p("(a) D = 2(6) − 3(4) = 0. Also Dₓ = 7(6) − 3(14) = 0 and D_y = 2(14) − 7(4) = 0, "
               "so every point on 2x + 3y = 7 is a solution: <b>infinitely many</b>.")
            + p("(b) D = 0 again but Dₓ = 7(6) − 3(20) = −18 ≠ 0, so the equations contradict each "
                "other: <b>no solution</b> (parallel lines).")
            + p("Rule: D = 0 always means the coefficient rows are proportional; the constants then "
                "decide between 'the same line' and 'parallel lines'."))},
]

EQUATIONS = [
    {"title": tr("Matrix arithmetic"),
     "items": [
         {"terms": tr("Order of a matrix with m rows and n columns"), "a": tr("m × n (row count first)")},
         {"terms": tr("Equality of two matrices"), "a": tr("same order, and aᵢⱼ = bᵢⱼ for every i, j")},
         {"terms": tr("Addition and subtraction"), "a": tr("(A ± B)ᵢⱼ = aᵢⱼ ± bᵢⱼ  (same order required)")},
         {"terms": tr("Scalar multiplication"), "a": tr("(kA)ᵢⱼ = k aᵢⱼ")},
         {"terms": tr("Transpose rules"), "a": tr("(Aᵀ)ᵀ = A,  (A + B)ᵀ = Aᵀ + Bᵀ,  (AB)ᵀ = BᵀAᵀ")},
         {"terms": tr("Product entry"), "a": tr("(AB)ᵢⱼ = aᵢ₁b₁ⱼ + aᵢ₂b₂ⱼ + ... + aᵢₙbₙⱼ")},
         {"terms": tr("Size rule for a product"), "a": tr("(m × n)(n × p) = m × p; inner numbers must match")},
     ]},
    {"title": tr("Determinant, adjoint and inverse"),
     "items": [
         {"terms": tr("Determinant of a 2 × 2 matrix"), "a": tr("|A| = ad − bc for A = [a b; c d]")},
         {"terms": tr("Adjoint of a 2 × 2 matrix"), "a": tr("adj A = [d −b; −c a]  (swap a, d; negate b, c)")},
         {"terms": tr("Inverse of a 2 × 2 matrix"), "a": tr("A⁻¹ = adj A / |A| ,  valid only if |A| ≠ 0")},
         {"terms": tr("Cofactor of an entry"), "a": tr("Cᵢⱼ = (−1)^(i+j) × minor of aᵢⱼ")},
         {"terms": tr("Determinant of a 3 × 3 matrix"), "a": tr("|A| = a₁₁C₁₁ + a₁₂C₁₂ + a₁₃C₁₃ (any row or column)")},
         {"terms": tr("Adjoint of a 3 × 3 matrix"), "a": tr("adj A = transpose of the cofactor matrix")},
         {"terms": tr("Singular test"), "a": tr("|A| = 0  ⇒  A⁻¹ does not exist")},
         {"terms": tr("Verification"), "a": tr("A A⁻¹ = A⁻¹A = I")},
         {"terms": tr("Inverse of a product"), "a": tr("(AB)⁻¹ = B⁻¹A⁻¹")},
     ]},
    {"title": tr("Two simultaneous equations"),
     "items": [
         {"terms": tr("Matrix form"), "a": tr("AX = B  ⇒  X = A⁻¹B")},
         {"terms": tr("Cramer's rule"), "a": tr("x = Dₓ/D ,  y = D_y/D ,  using D = a₁b₂ − a₂b₁")},
         {"terms": tr("Unique solution"), "a": tr("D ≠ 0  ⇒  exactly one solution")},
         {"terms": tr("No solution"), "a": tr("D = 0 and Dₓ or D_y ≠ 0  ⇒  parallel lines")},
         {"terms": tr("Infinitely many solutions"), "a": tr("D = Dₓ = D_y = 0  ⇒  the same line twice")},
     ]},
]

VIVA = [
    {"title": tr("Basics"),
     "items": [
         {"q": tr("What is a matrix?"),
          "a": tr("A rectangular arrangement of numbers inside brackets. It has no value of its own; "
                  "it is described by its order and its entries.")},
         {"q": tr("What does the order m × n tell you?"),
          "a": tr("m rows and n columns, so the matrix holds m × n entries.")},
         {"q": tr("In a₂₃, which number is the row?"),
          "a": tr("The first, 2. The row is always quoted before the column.")},
         {"q": tr("When are two matrices equal?"),
          "a": tr("When they have the same order and every matching pair of entries is equal.")},
         {"q": tr("What is a square matrix?"),
          "a": tr("One whose number of rows equals its number of columns, such as 2 × 2 or 3 × 3. "
                  "Only square matrices have determinants and inverses.")},
         {"q": tr("Name four special square matrices."),
          "a": tr("Diagonal (zeros off the diagonal), scalar (equal diagonal entries), identity "
                  "(ones on the diagonal) and zero (all entries zero).")},
     ]},
    {"title": tr("Operations"),
     "items": [
         {"q": tr("When can two matrices be added?"),
          "a": tr("Only when they have the same order; then each pair of matching entries is added.")},
         {"q": tr("When does the product AB exist?"),
          "a": tr("When the number of columns of A equals the number of rows of B. The answer then "
                  "has the rows of A and the columns of B.")},
         {"q": tr("Is AB equal to BA?"),
          "a": tr("Usually not. Matrix multiplication is not commutative, and sometimes one of the "
                  "two products cannot be formed at all.")},
         {"q": tr("How do you find the entry in row 2 and column 1 of AB?"),
          "a": tr("Take row 2 of A and column 1 of B, multiply matching entries and add the products.")},
         {"q": tr("Does AB = O mean A = O or B = O?"),
          "a": tr("No. Two non-zero matrices can multiply to the zero matrix; matrices have no "
                  "zero-product rule.")},
         {"q": tr("What is the transpose used for?"),
          "a": tr("To turn rows into columns. It defines symmetric matrices (Aᵀ = A) and appears in "
                  "the rules (AB)ᵀ = BᵀAᵀ.")},
     ]},
    {"title": tr("Adjoint, inverse and equations"),
     "items": [
         {"q": tr("How do you write the adjoint of a 2 × 2 matrix?"),
          "a": tr("Swap the two diagonal entries and change the signs of the other two: for "
                  "[a b; c d] the adjoint is [d −b; −c a].")},
         {"q": tr("When does a matrix have no inverse?"),
          "a": tr("When its determinant is zero. Such a matrix is called singular, and A⁻¹ = adj A/|A| "
                  "cannot be evaluated.")},
         {"q": tr("How do you check an inverse?"),
          "a": tr("Multiply A by A⁻¹ in either order; the answer must be the identity matrix I.")},
         {"q": tr("What does the determinant of a coefficient matrix tell you?"),
          "a": tr("If D ≠ 0 there is exactly one solution. If D = 0 the equations are either "
                  "inconsistent (no solution) or dependent (infinitely many).")},
         {"q": tr("State Cramer's rule for two equations."),
          "a": tr("x = Dₓ/D and y = D_y/D, where Dₓ is formed by replacing the x-column with the "
                  "constants and D_y by replacing the y-column.")},
         {"q": tr("Why must you check a solution in the original equations?"),
          "a": tr("Because an arithmetic slip in one entry of the inverse or one determinant gives a "
                  "wrong answer that still looks tidy; substitution is the only reliable check.")},
     ]},
]

EXAM = [
    {"q": tr("Write the order of A = " + mx(["1", "−2", "4"], ["7", "0", "3"])
             + ", state a₂₃ and count the entries."), "marks": 3},
    {"q": tr("If " + mx(["x + 2", "4"], ["3", "y − 1"]) + " = " + mx(["6", "4"], ["3", "5"])
             + ", find x and y."), "marks": 3},
    {"q": tr("Construct the 2 × 3 matrix with aᵢⱼ = i + 3j."), "marks": 3},
    {"q": tr("For A = " + mx(["2", "−1", "0"], ["3", "4", "1"]) + " and B = "
             + mx(["1", "2", "3"], ["0", "−2", "5"]) + ", find A + B and A − B."), "marks": 3},
    {"q": tr("Evaluate 2A − 3B for A = " + mx(["1", "2"], ["3", "4"]) + " and B = "
             + mx(["0", "1"], ["2", "−1"]) + "."), "marks": 3},
    {"q": tr("For A = " + mx(["2", "3"], ["1", "4"]) + ", verify that A + Aᵀ is symmetric."),
     "marks": 3},
    {"q": tr("Find AB and BA for A = " + mx(["1", "2"], ["3", "4"]) + " and B = "
             + mx(["0", "1"], ["1", "0"]) + ", and comment on the result."), "marks": 4},
    {"q": tr("Multiply A = " + mx(["1", "2", "3"], ["4", "5", "6"]) + " by B = "
             + mx(["1", "0"], ["2", "1"], ["0", "3"]) + " and state the order of AB."), "marks": 4},
    {"q": tr("If A = " + mx(["1", "2"], ["3", "x"]) + " and A² = " + mx(["7", "10"], ["15", "22"])
             + ", find x."), "marks": 4},
    {"q": tr("Find the adjoint and inverse of A = " + mx(["4", "5"], ["2", "3"]) + "."), "marks": 4},
    {"q": tr("For what values of k is A = " + mx(["k", "3"], ["2", "k − 1"]) + " singular?"),
     "marks": 3},
    {"q": tr("Find |A|, adj A and A⁻¹ for A = " + mx(["1", "2", "3"], ["0", "1", "4"], ["5", "6", "0"])
             + "."), "marks": 4},
    {"q": tr("Solve x + y = 7 and 2x − y = 2 by Cramer's rule."), "marks": 4},
    {"q": tr("Solve 2x + y = 8 and x + 3y = 9 by the inverse-matrix method."), "marks": 4},
    {"q": tr("Two numbers add to 30 and differ by 8. Form the matrix equation and solve it."),
     "marks": 4},
]

# Model answers for the practice section, keyed by practice number.
PRACTICE_ANSWERS = [
    tr(p("A has 2 rows and 3 columns, so the order is <b>2 × 3</b>; the matrix therefore holds "
         "2 × 3 = 6 entries.")
       + p("a₂₃ means row 2, column 3, so <b>a₂₃ = 3</b>.")
       + p("Read the row first and the column second: a₃₂ does not exist here, because the matrix "
           "has only two rows.")),
    tr(p("The orders match (2 × 2), so compare the entries that contain unknowns."))
    + p("x + 2 = 6 gives <b>x = 4</b>, and y − 1 = 5 gives <b>y = 6</b>. The other two entries, "
        "4 = 4 and 3 = 3, are already satisfied."),
    tr(p("Put aᵢⱼ = i + 3j for i = 1, 2 and j = 1, 2, 3.")) + p(mx(["4", "7", "10"], ["5", "8", "11"]))
    + p("Row 1: 1 + 3 = 4, 1 + 6 = 7, 1 + 9 = 10. Row 2: 2 + 3 = 5, 2 + 6 = 8, 2 + 9 = 11."),
    tr(p("Both matrices are 2 × 3, so add and subtract entry by entry."))
    + p("A + B = " + mx(["3", "1", "3"], ["3", "2", "6"]) + " and A − B = "
        + mx(["1", "−3", "−3"], ["3", "6", "−4"]) + ".")
    + p("Check one entry: 0 + 3 = 3 and 0 − 3 = −3."),
    tr(p("Scale first: 2A = " + mx(["2", "4"], ["6", "8"]) + " and 3B = "
        + mx(["0", "3"], ["6", "−3"]) + "."))
    + p("Subtracting: 2A − 3B = " + mx(["2", "1"], ["0", "11"]) + ".")
    + p("The bottom-right entry is 8 − (−3) = 11, since subtracting a negative adds."),
    tr(p("Aᵀ = " + mx(["2", "1"], ["3", "4"]) + ", so A + Aᵀ = " + mx(["4", "4"], ["4", "8"]) + "."))
    + p("The entries across the diagonal are equal, so the sum is symmetric.")
    + p("In general (A + Aᵀ)ᵀ = Aᵀ + A = A + Aᵀ, which proves the result for every square matrix."),
    tr(p("AB = " + mx(["2", "3"], ["4", "7"]) + " and BA = " + mx(["3", "4"], ["1", "2"]) + "."))
    + p("The two products are different matrices, so <b>AB ≠ BA</b>: matrix multiplication is not "
        "commutative, even when both products exist and have the same order."),
    tr(p("The inner numbers are 3 and 3, so AB exists and its order is 2 × 2."))
    + p("AB = " + mx(["5", "11"], ["14", "23"]) + ".")
    + p("Row 1 into column 2: 1(0) + 2(1) + 3(3) = 11. Row 2 into column 1: 4(1) + 5(2) + 6(0) = 14."),
    tr(p("A² = " + mx(["7", "2 + 2x"], ["3 + 3x", "6 + x²"]) + "."))
    + p("Comparing top-right entries: 2 + 2x = 10, so <b>x = 4</b>.")
    + p("Check: 3 + 12 = 15 and 6 + 16 = 22, exactly the given entries, so x = 4 is correct."),
    tr(p("|A| = 4(3) − 5(2) = 12 − 10 = 2, so the inverse exists."))
    + p("adj A = " + mx(["3", "−5"], ["−2", "4"]) + " and A⁻¹ = (1/2)"
        + mx(["3", "−5"], ["−2", "4"]) + ".")
    + p("Check: 4(3/2) + 5(−2/2) = 6 − 5 = 1, the top-left entry of I."),
    tr(p("A is singular when |A| = 0: k(k − 1) − (3)(2) = k² − k − 6 = 0."))
    + p("Factorising: (k − 3)(k + 2) = 0, so <b>k = 3 or k = −2</b>.")
    + p("For every other value of k the determinant is non-zero and the inverse exists."),
    tr(p("|A| = 1(0 − 24) − 2(0 − 20) + 3(0 − 5) = −24 + 40 − 15 = <b>1</b>."))
    + p("adj A = " + mx(["−24", "18", "5"], ["20", "−15", "−4"], ["−5", "4", "1"]) + ".")
    + p("Since |A| = 1, A⁻¹ = adj A; multiplying A by it gives I, which verifies the answer."),
    tr(p("Coefficient matrix A = " + mx(["1", "1"], ["2", "−1"]) + " gives D = −1 − 2 = −3."))
    + p("Dₓ = 7(−1) − 2(1) = −9 and D_y = 1(2) − 2(7) = −12.")
    + p("Hence x = −9/−3 = <b>3</b> and y = −12/−3 = <b>4</b>, which satisfy both equations."),
    tr(p("A = " + mx(["2", "1"], ["1", "3"]) + ", B = " + mx(["8"], ["9"])
        + ", |A| = 6 − 1 = 5 and A⁻¹ = (1/5)" + mx(["3", "−1"], ["−1", "2"]) + "."))
    + p("X = A⁻¹B = (1/5)" + mx(["24 − 9"], ["−8 + 18"]) + " = " + mx(["3"], ["2"]) + ".")
    + p("So x = 3 and y = 2; substituting gives 6 + 2 = 8 and 3 + 6 = 9."),
    tr(p("Let the numbers be x and y. Then x + y = 30 and x − y = 8, so A = "
        + mx(["1", "1"], ["1", "−1"]) + " and B = " + mx(["30"], ["8"]) + "."))
    + p("|A| = −1 − 1 = −2 and A⁻¹ = (1/−2)" + mx(["−1", "−1"], ["−1", "1"]) + ".")
    + p("X = A⁻¹B = " + mx(["19"], ["11"]) + ", so the numbers are <b>19 and 11</b>: they add to 30 "
        "and differ by 8."),
]

LESSON_COUNT = sum(len(s["items"]) for s in NOTES)
