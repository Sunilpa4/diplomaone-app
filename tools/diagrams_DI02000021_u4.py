"""Five compact mobile SVGs for Engineering Mathematics (DI02000021) Unit 4: Differential Equations."""
import math

from flowchart_lib import svg, text, arr, rbox, line, P

BLUE, BF = "#1565C0", "#EAF3FD"
GREEN, GF = "#2E7D32", "#EAF6EC"
ORANGE, OF = "#B66A00", "#FFF4DF"
RED, RF = "#BD2543", "#FDECF0"
PURPLE = "#7B2CD9"
GREY = "#666"
INK = "#333"

TITLES = {
    "d1_order": "Order and degree of a DE",
    "d2_separable": "Variable separable: split x from y",
    "d3_linear": "Linear DE and the integrating factor",
    "d4_choice": "Separable or linear?",
    "d5_family": "One family, many solutions",
}


def heading(t, sub=None):
    body = text(180, 24, t, 14, weight="bold", color=P)
    if sub:
        body += text(180, 46, sub, 10.4, color=GREY)
    return body


def foot(y, *lines):
    return "".join(text(180, y + 16 * i, s, 10.2, color=GREY) for i, s in enumerate(lines))


def polyline(pts, color, w=2.1, dash=None):
    d = "M" + " L".join(f"{x:.1f} {y:.1f}" for x, y in pts)
    return line(d, color, w, dash=dash)


# ---------------------------------------------------------------- 1. order and degree
def order_degree():
    b = heading("Order and degree of a DE", "read the equation before you try to solve it")
    b += text(180, 78, "d²y/dx²  +  3 (dy/dx)²  =  x", 13, weight="bold", color=P)
    b += rbox(180, 112, 320, 24, "order = 2 : the highest derivative that appears", BF, BLUE, 10.0)
    b += rbox(180, 146, 320, 24, "degree = 1 : the power of that highest derivative", GF, GREEN, 10.0)
    b += rbox(180, 180, 320, 24, "the (dy/dx)² does not change either of them", OF, ORANGE, 10.0)
    b += text(180, 212, "quick check", 10.4, color=P, weight="bold")
    for i, (eq, res) in enumerate((("dy/dx + y = x", "order 1, degree 1"),
                                   ("(dy/dx)³ + y = x²", "order 1, degree 3"),
                                   ("d²y/dx² + y² = 0", "order 2, degree 1"))):
        b += rbox(180, 240 + i * 34, 320, 24, f"{eq}    →    {res}", RF, RED, 9.8)
    b += foot(344, "Order first, then degree.", "Order counts derivatives; degree counts their powers.")
    return svg(360, 378, b)


# ---------------------------------------------------------------- 2. separable
def separable():
    b = heading("Variable separable: split x from y", "works when the right side factors")
    b += rbox(180, 82, 330, 26, "dy/dx = f(x) · g(y)", BF, BLUE, 11.0)
    b += arr([(180, 95), (180, 117)], GREY)
    b += rbox(180, 136, 330, 26, "divide by g(y) and multiply by dx", BF, BLUE, 10.2)
    b += arr([(180, 149), (180, 171)], GREY)
    b += rbox(180, 190, 330, 26, "∫ dy/g(y)  =  ∫ f(x) dx", GF, GREEN, 11.0)
    b += arr([(180, 203), (180, 225)], GREY)
    b += rbox(180, 244, 330, 26, "integrate both sides, add one c", GF, GREEN, 10.2)
    b += rbox(180, 288, 330, 26, "dy/dx = x/y  →  y dy = x dx  →  y² = x² + c", OF, ORANGE, 9.8)
    b += rbox(180, 326, 330, 24, "a point such as y(0) = 3 fixes the constant", RF, RED, 9.8)
    b += foot(360, "Keep y on the left of dy and x on the left of dx.",
              "Then each side integrates with respect to one variable only.")
    return svg(360, 392, b)


# ---------------------------------------------------------------- 3. linear DE and IF
def linear():
    b = heading("Linear DE: dy/dx + P y = Q", "first order, first degree, y only to power 1")
    b += rbox(180, 82, 336, 26, "write it in this exact form first", BF, BLUE, 10.2)
    b += arr([(180, 95), (180, 117)], GREY)
    b += rbox(180, 136, 336, 26, "P = coefficient of y ;  Q = the rest", OF, ORANGE, 10.2)
    b += arr([(180, 149), (180, 171)], GREY)
    b += rbox(180, 190, 336, 28, "integrating factor  IF = e^(∫P dx)", GF, GREEN, 11.0)
    b += arr([(180, 204), (180, 226)], GREY)
    b += rbox(180, 246, 336, 26, "multiply through: d/dx ( y · IF ) = Q · IF", BF, BLUE, 10.0)
    b += arr([(180, 259), (180, 281)], GREY)
    b += rbox(180, 300, 336, 26, "y · IF = ∫ Q · IF dx  +  c", GF, GREEN, 10.4)
    b += rbox(180, 338, 336, 26, "y = ( ∫ Q·IF dx + c ) / IF", RF, RED, 10.6)
    b += foot(376, "The IF turns the left side into one exact derivative.")
    return svg(360, 394, b)


# ---------------------------------------------------------------- 4. which method
def choice():
    b = heading("Separable or linear?", "test the shape of the right-hand side")
    b += rbox(180, 82, 334, 26, "can you write it as (x part) × (y part)?", BF, BLUE, 10.2)
    b += rbox(180, 118, 334, 24, "yes  →  variable separable", GF, GREEN, 10.6)
    b += rbox(180, 158, 334, 26, "otherwise: is y only to the first power?", OF, ORANGE, 10.2)
    b += rbox(180, 194, 334, 24, "yes  →  linear, use the IF", GF, GREEN, 10.6)
    b += rbox(180, 234, 334, 26, "no  →  not in this unit's syllabus", RF, RED, 10.2)
    b += text(180, 268, "spot them by example", 10.4, color=P, weight="bold")
    for i, (eq, res) in enumerate((("dy/dx = x y²", "separable"),
                                   ("dy/dx + 2y = eˣ", "linear"),
                                   ("dy/dx = (x + 1)/y", "separable"))):
        b += rbox(180, 296 + i * 34, 334, 24, f"{eq}    →    {res}", BF, BLUE, 9.8)
    b += foot(400, "Always try to separate first - it is usually quicker.")
    return svg(360, 430, b)


# ---------------------------------------------------------------- 5. family of solutions
def family():
    b = heading("One family, many solutions", "y = c e^(−x) solves dy/dx = −y for every c")
    ox, oy, sx, sy = 62, 276, 88, 76

    def pt(x, y):
        return (ox + x * sx, oy - y * sy)

    b += line(f"M{ox} {oy} H318", INK, 1.2)
    b += line(f"M{ox} {oy} V96", INK, 1.2)
    b += text(312, oy - 8, "x", 10, color=INK, anchor="end")
    b += text(ox + 8, 104, "y", 10, color=INK, anchor="start")
    for c, col, lab, dy_lab in ((2.0, GREEN, "c = 2", -8), (1.0, BLUE, "c = 1", -8),
                                (0.5, RED, "c = 0.5", 13)):
        pts = [pt(-0.02 + 2.9 * k / 90, c * math.exp(-(-0.02 + 2.9 * k / 90))) for k in range(91)]
        b += polyline(pts, col, 2.0)
        lx, ly = pt(0.16, c * math.exp(-0.16))
        b += text(lx + 6, ly + dy_lab, lab, 9.2, color=col, anchor="start")
    cx, cy = pt(0, 1.0)
    b += (f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="3.6" fill="{ORANGE}" '
          f'stroke="#fff" stroke-width="1.2"/>')
    b += rbox(180, 314, 336, 24, "general solution: the whole family, constant c free", BF, BLUE, 9.8)
    b += rbox(180, 350, 336, 24, "particular solution: one curve - here y(0) = 1 gives c = 1", GF, GREEN, 9.2)
    b += foot(382, "Different c, same slope rule - the curves never meet.")
    return svg(360, 404, b)


ALL = {
    "d1_order": order_degree,
    "d2_separable": separable,
    "d3_linear": linear,
    "d4_choice": choice,
    "d5_family": family,
}
