"""Six compact mobile SVGs for Engineering Mathematics (DI02000021) Unit 1: Matrices."""
from flowchart_lib import svg, text, arr, rbox, line, P

BLUE, BF = "#1565C0", "#EAF3FD"
GREEN, GF = "#2E7D32", "#EAF6EC"
ORANGE, OF = "#B66A00", "#FFF4DF"
RED, RF = "#BD2543", "#FDECF0"
PURPLE = "#7B2CD9"
GREY = "#666"

TITLES = {
    "mx1_anatomy": "A matrix is a block of numbers",
    "mx2_types": "Six matrix types to recognise",
    "mx3_product": "Row times column gives an entry of AB",
    "mx4_inverse2": "The 2x2 inverse in three steps",
    "mx5_adj3": "Adjoint of a 3x3 matrix",
    "mx6_solve": "Three outcomes of two equations",
}


def heading(t, sub=None):
    body = text(180, 24, t, 14, weight="bold", color=P)
    if sub:
        body += text(180, 46, sub, 10.4, color=GREY)
    return body


def foot(y, *lines):
    return "".join(text(180, y + 16 * i, s, 10.2, color=GREY) for i, s in enumerate(lines))


def brackets(x, y, w, h, color):
    return (line(f"M{x - 8} {y - 4} h-4 V{y + h + 4} h4", color, 1.5)
            + line(f"M{x + w + 8} {y - 4} h4 V{y + h + 4} h-4", color, 1.5))


def mat(x, y, data, cw=26, ch=22, size=10.4, color=P, hot=None, hc=RED):
    """Draw a matrix with square brackets; (x, y) is the top-left of the entries."""
    rows, cols = len(data), len(data[0])
    w, h = cols * cw, rows * ch
    out = brackets(x, y, w, h, color)
    for i, row in enumerate(data):
        for j, val in enumerate(row):
            cx = x + cw * (j + 0.5)
            cy = y + ch * (i + 0.5)
            if hot and (i, j) in hot:
                out += (f'<rect x="{cx - cw / 2 + 1:.1f}" y="{cy - ch / 2 + 1:.1f}" width="{cw - 2:.1f}" '
                        f'height="{ch - 2:.1f}" rx="3" fill="{RF}"/>')
                out += text(cx, cy + size * 0.36, val, size, color=hc, weight="bold")
            else:
                out += text(cx, cy + size * 0.36, val, size, color=color)
    return out


# ---------------------------------------------------------------- 1. anatomy
def anatomy():
    b = heading("A matrix is a block of numbers", "order = rows × columns, and aᵢⱼ means row i, column j")
    x, y, cw, ch = 120, 96, 44, 34
    b += mat(x, y, [["a₁₁", "a₁₂", "a₁₃"], ["a₂₁", "a₂₂", "a₂₃"]], cw, ch, 12.2,
             hot=[(1, 2)], hc="#7B1030")
    for j in range(3):
        b += text(x + cw * (j + 0.5), 84, f"col {j + 1}", 9.4, color=BLUE)
    for i in range(2):
        b += text(x - 16, y + ch * (i + 0.5) + 4, f"row {i + 1}", 9.4, color=BLUE, anchor="end")
    b += rbox(180, 196, 322, 26, "2 rows and 3 columns  ⇒  order 2 × 3", BF, BLUE, 10.6)
    b += text(180, 240, "a₂₃ = row 2, column 3 (the red entry)", 10.6, color="#7B1030", weight="bold")
    b += rbox(180, 282, 322, 26, "a matrix is an array, not a single number", OF, ORANGE, 10.4)
    b += foot(316, "A matrix has no value of its own - it is an arrangement.",
              "Equality needs the same order and matching entries.")
    return svg(360, 348, b)


# ---------------------------------------------------------------- 2. types
def types():
    b = heading("Six matrix types to recognise", "name the pattern, not the numbers")
    cells = [
        ("Identity I", [["1", "0"], ["0", "1"]], "diagonal ones", (88, 92)),
        ("Diagonal", [["3", "0"], ["0", "5"]], "diagonal only", (188, 92)),
        ("Zero O", [["0", "0"], ["0", "0"]], "all entries 0", (288, 92)),
        ("Triangular", [["2", "7"], ["0", "4"]], "zeros on one side", (88, 210)),
        ("Symmetric", [["1", "3"], ["3", "5"]], "Aᵀ = A", (188, 210)),
        ("Row / column", [["4", "2"]], "one line of entries", (288, 210)),
    ]
    for name, data, note, (cx, cy) in cells:
        b += text(cx, cy, name, 9.6, weight="bold", color=P)
        cw = 20 if len(data[0]) == 2 else 24
        top = cy + 22 if len(data) == 1 else cy + 12
        b += mat(cx - cw * len(data[0]) / 2, top, data, cw, 20, 10, color="#333")
        b += text(cx, cy + 74, note, 8.8, color=GREY)
    b += rbox(180, 324, 336, 26, "square = rows equal columns;  singular = |A| = 0", GF, GREEN, 10.4)
    b += foot(356, "Diagonal, scalar and identity matrices are square.",
              "A triangular matrix is square too - one side is all zeros.")
    return svg(360, 388, b)


# ---------------------------------------------------------------- 3. product
def product():
    b = heading("Row times column gives an entry of AB", "A is 2 × 3 and B is 3 × 2, so AB is 2 × 2")
    a = [["1", "2", "3"], ["4", "5", "6"]]
    bb = [["1", "0"], ["2", "1"], ["0", "3"]]
    c = [["5", "11"], ["14", "23"]]
    b += text(74, 80, "A (2×3)", 9.8, weight="bold", color=BLUE)
    b += mat(36, 92, a, 26, 22, 10.4, color=BLUE, hot=[(0, 0), (0, 1), (0, 2)], hc="#0D47A1")
    b += text(142, 120, "×", 14, weight="bold", color=P)
    b += text(196, 80, "B (3×2)", 9.8, weight="bold", color=GREEN)
    b += mat(162, 92, bb, 26, 22, 10.4, color=GREEN, hot=[(0, 0), (1, 0), (2, 0)], hc="#1B5E20")
    b += text(233, 120, "=", 14, weight="bold", color=P)
    b += text(288, 80, "C (2×2)", 9.8, weight="bold", color=RED)
    b += mat(252, 92, c, 30, 22, 10.4, color=RED, hot=[(0, 0)], hc="#7B1030")
    b += rbox(180, 186, 330, 26, "c₁₁ = row 1 of A · column 1 of B", RF, RED, 10.6)
    b += text(180, 222, "= 1×1 + 2×2 + 3×0 = 5", 11.6, color="#7B1030", weight="bold")
    b += rbox(180, 262, 330, 26, "inner sizes must match: (2×3)(3×2)", BF, BLUE, 10.4)
    b += rbox(180, 302, 330, 26, "AB ≠ BA in general - order matters", OF, ORANGE, 10.4)
    b += foot(336, "Multiply each row of A into each column of B.",
              "The answer has rows of A and columns of B.")
    return svg(360, 368, b)


# ---------------------------------------------------------------- 4. inverse 2x2
def inverse2():
    b = heading("The 2x2 inverse in three steps", "A⁻¹ exists only when |A| ≠ 0")
    b += rbox(180, 74, 330, 26, "step 1:  |A| = ad − bc  (it must not be 0)", BF, BLUE, 10.4)
    b += rbox(180, 112, 330, 26, "step 2:  swap a and d, negate b and c", BF, BLUE, 10.4)
    b += text(80, 168, "A =", 10.8, color=P, anchor="end")
    b += mat(96, 142, [["a", "b"], ["c", "d"]], 32, 24, 11.4, color=P,
             hot=[(0, 0), (1, 1)], hc="#7B1030")
    b += arr([(176, 166), (198, 166)], GREY)
    b += text(232, 130, "adj A", 10.4, color=GREEN, weight="bold")
    b += mat(214, 142, [["d", "−b"], ["−c", "a"]], 32, 24, 11.4, color=GREEN)
    b += rbox(180, 214, 330, 26, "step 3: divide the adjoint by the determinant", GF, GREEN, 10.4)
    b += rbox(180, 252, 330, 26, "A⁻¹ = adj A ÷ |A|  =  1/(ad − bc) · [d −b; −c a]", GF, GREEN, 10.4)
    b += rbox(180, 294, 330, 26, "A = [3 1; 5 2]  ⇒  |A| = 1,  A⁻¹ = [2 −1; −5 3]", BF, BLUE, 10.2)
    b += rbox(180, 332, 330, 26, "|A| = 0  ⇒  singular, so A⁻¹ does not exist", RF, RED, 10.4)
    b += foot(362, "Always check A · A⁻¹ = I before you trust the answer.")
    return svg(360, 382, b)


# ---------------------------------------------------------------- 5. adjoint 3x3
def adj3():
    b = heading("Adjoint of a 3x3 matrix", "adj A = transpose of the cofactor matrix")
    b += text(80, 78, "A (3×3)", 9.8, weight="bold", color=BLUE)
    b += mat(26, 86, [["a₁₁", "a₁₂", "a₁₃"], ["a₂₁", "a₂₂", "a₂₃"], ["a₃₁", "a₃₂", "a₃₃"]],
             36, 22, 8.4, color=BLUE)
    b += text(152, 122, "×", 11, color=GREY)
    b += text(199, 78, "signs", 9.8, weight="bold", color=ORANGE)
    b += mat(166, 86, [["+", "−", "+"], ["−", "+", "−"], ["+", "−", "+"]], 22, 22, 10.6, color=ORANGE)
    b += text(250, 122, "×", 11, color=GREY)
    b += text(300, 78, "cofactors Cᵢⱼ", 9.8, weight="bold", color=GREEN)
    b += mat(264, 86, [["C₁₁", "C₁₂", "C₁₃"], ["C₂₁", "C₂₂", "C₂₃"], ["C₃₁", "C₃₂", "C₃₃"]],
             24, 22, 8.2, color=GREEN)
    b += rbox(180, 178, 330, 24, "Cᵢⱼ = (−1)^(i+j) × minor of aᵢⱼ", BF, BLUE, 10.2)
    b += rbox(180, 216, 330, 24, "a minor is the 2x2 left after deleting its row and column", OF, ORANGE, 9.6)
    b += rbox(180, 254, 330, 24, "reflect the cofactor matrix: rows become columns", GF, GREEN, 10.2)
    b += rbox(180, 294, 330, 26, "A⁻¹ = adj A ÷ |A| ,  only when |A| ≠ 0", RF, RED, 10.4)
    b += foot(328, "On the diagonal the sign is +, off the diagonal it is −.",
              "A 3x3 inverse needs 9 cofactors, so work slowly.")
    return svg(360, 360, b)


# ---------------------------------------------------------------- 6. two equations
def solve():
    b = heading("Three outcomes of two equations", "D = a₁b₂ − a₂b₁ decides which one you get")

    def panel(cx, cy, kind):
        out = (line(f"M{cx - 42} {cy + 26} H{cx + 42}", "#333", 1.2)
               + line(f"M{cx - 30} {cy + 26} V{cy - 32}", "#333", 1.2))
        if kind == "unique":
            out += line(f"M{cx - 38} {cy + 22} L{cx + 36} {cy - 26}", BLUE, 2)
            out += line(f"M{cx - 34} {cy - 28} L{cx + 34} {cy + 28}", GREEN, 2)
            out += f'<circle cx="{cx + 3}" cy="{cy - 2}" r="3.6" fill="{RED}"/>'
            return out + text(cx, cy + 52, "D ≠ 0: one point", 9.4, color=GREEN, weight="bold")
        if kind == "parallel":
            out += line(f"M{cx - 36} {cy + 16} L{cx + 34} {cy - 30}", BLUE, 2)
            out += line(f"M{cx - 22} {cy + 30} L{cx + 40} {cy - 12}", GREEN, 2)
            return out + text(cx, cy + 52, "D = 0: no solution", 9.4, color=RED, weight="bold")
        out += line(f"M{cx - 36} {cy + 18} L{cx + 34} {cy - 28}", PURPLE, 2.4)
        return out + text(cx, cy + 52, "infinite solutions", 9.4, color=ORANGE, weight="bold")

    for cx, kind in ((72, "unique"), (180, "parallel"), (288, "coincident")):
        b += panel(cx, 134, kind)
    b += rbox(180, 224, 332, 24, "unique:  x = Dx/D  and  y = Dy/D", GF, GREEN, 10.4)
    b += rbox(180, 264, 332, 24, "no solution:  the lines are parallel", RF, RED, 10.4)
    b += rbox(180, 304, 332, 24, "infinite:  the same line written twice", OF, ORANGE, 10.4)
    b += foot(338, "Cramer's rule works only in the first case - check D first.",
              "Dx swaps the x-column for the constants; Dy swaps y's.")
    return svg(360, 370, b)


ALL = {
    "mx1_anatomy": anatomy,
    "mx2_types": types,
    "mx3_product": product,
    "mx4_inverse2": inverse2,
    "mx5_adj3": adj3,
    "mx6_solve": solve,
}
