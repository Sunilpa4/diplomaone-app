"""Seven compact mobile SVGs for Mathematics-I Unit 1 (Determinant and Function).

360 px wide, white background, no <marker>/<style>/<image>/href, text kept inside the canvas.
"""
import math

from flowchart_lib import svg, text, arr, rbox, decision, terminal, line, P

BLUE, BF = "#1565C0", "#EAF3FD"
GREEN, GF = "#2E7D32", "#EAF6EC"
ORANGE, OF = "#B66A00", "#FFF4DF"
RED, RF = "#BD2543", "#FDECF0"
GREY = "#666"

TITLES = {
    "m1_det2": "A second-order determinant",
    "m1_det3": "Expanding a third-order determinant",
    "m1_cramer": "Cramer's rule in four steps",
    "m1_function": "A function is a one-output machine",
    "m1_graphs": "Three shapes you must recognise",
    "m1_exp_log": "Exponential and logarithm are mirrors",
    "m1_loglaws": "The four logarithm laws",
}


def heading(t, sub=None):
    body = text(180, 24, t, 14, weight="bold", color=P)
    if sub:
        body += text(180, 46, sub, 10.5, color=GREY)
    return body


def foot(y, *lines):
    return "".join(text(180, y + 16 * i, s, 10.2, color=GREY) for i, s in enumerate(lines))


# ---------------------------------------------------------------- 1. 2x2 determinant
def det2():
    b = heading("A second-order determinant", "Main diagonal minus the other diagonal")
    b += line("M112 118 V246", "#333", 2.2) + line("M226 118 V246", "#333", 2.2)
    for x, y, t in ((146, 160, "a"), (196, 160, "b"), (146, 216, "c"), (196, 216, "d")):
        b += text(x, y, t, 22, weight="bold", color="#222")
    b += line("M138 170 L204 206", BLUE, 2.0)
    b += f'<polygon points="208,208 198,206 202,198" fill="{BLUE}"/>'
    b += line("M204 170 L138 206", RED, 2.0)
    b += f'<polygon points="134,208 144,206 140,198" fill="{RED}"/>'
    b += text(258, 150, "a × d", 11, color=BLUE, weight="bold")
    b += text(258, 168, "(add)", 9.6, color=BLUE)
    b += text(258, 216, "b × c", 11, color=RED, weight="bold")
    b += text(258, 234, "(subtract)", 9.6, color=RED)
    b += rbox(180, 282, 324, 34, "value = ad − bc", GF, GREEN, 12.5, weight="bold", color="#1B5E20")
    b += text(180, 314, "|3 5; 2 4| = 12 − 10 = 2", 11, color="#333")
    b += foot(334, "Vertical bars mean a number; square brackets mean a matrix.")
    return svg(360, 380, b)


# ---------------------------------------------------------------- 2. 3x3 expansion
def det3():
    b = heading("Expanding a third-order determinant", "Signs belong to the position: + − +")
    x0, y0, cw, ch = 126, 64, 36, 32
    signs = [["+", "−", "+"], ["−", "+", "−"], ["+", "−", "+"]]
    for r in range(3):
        for c in range(3):
            x, y = x0 + c * cw, y0 + r * ch
            fill = GF if (r == 0) else "#F6F2FB"
            stroke = GREEN if r == 0 else "#B9A7D6"
            b += f'<rect x="{x}" y="{y}" width="{cw}" height="{ch}" fill="{fill}" stroke="{stroke}" stroke-width="1.3"/>'
            s = signs[r][c]
            b += text(x + cw / 2, y + ch / 2, s, 13, weight="bold", color=RED if s == "−" else GREEN)
    b += text(x0 + 3 * cw + 12, y0 + ch / 2, "row 1", 9.6, color=GREY, anchor="start")
    b += text(x0 + 3 * cw + 12, y0 + ch / 2 + 16, "is used", 9.6, color=GREY, anchor="start")
    rows = [("+ a₁ × det[b₂ c₂; b₃ c₃]", GREEN, GF),
            ("− b₁ × det[a₂ c₂; a₃ c₃]", RED, RF),
            ("+ c₁ × det[a₂ b₂; a₃ b₃]", GREEN, GF)]
    y = 188
    for label, stroke, fill in rows:
        b += rbox(180, y, 324, 30, label, fill, stroke, 11.4, color="#222")
        y += 38
    b += foot(y + 6, "Any row or column gives the same value.", "Choose the line with the most zeros.")
    return svg(360, y + 62, b)


# ---------------------------------------------------------------- 3. Cramer's rule
def cramer():
    b = heading("Cramer's rule in four steps", "Determinants replace the constants column")
    b += rbox(180, 78, 300, 34, "2x + 3y = 12    and    x − y = 1", BF, BLUE, 11.6)
    b += arr([(180, 95), (180, 116)], P)
    b += rbox(180, 134, 300, 34, "D = |2 3; 1 −1| = −5", "#F6F2FB", P, 11.6)
    b += arr([(180, 151), (180, 174)], P)
    b += decision(180, 204, "D ≠ 0 ?", 96, 52, 11.5)
    b += arr([(228, 204), (300, 204), (300, 236)], GREEN, label="yes", lpos=(262, 196))
    b += rbox(268, 254, 150, 34, "x = Dx/D,  y = Dy/D", GF, GREEN, 11.2)
    b += arr([(132, 204), (66, 204), (66, 236)], RED, label="no", lpos=(96, 196))
    b += rbox(74, 262, 108, 46, "D = 0\nthen check Dx, Dy", RF, RED, 9.8)
    b += arr([(268, 271), (268, 300)], P)
    b += terminal(268, 318, "check both equations", 170, 30, 10)
    b += foot(352, "Wrong column replaced is the classic error: Dx uses the", "constants in the x-column.")
    return svg(360, 402, b)


# ---------------------------------------------------------------- 4. function machine
def machine():
    b = heading("A function is a one-output machine", "Here f(x) = x² + 1")
    b += text(62, 80, "INPUT  x", 10, weight="bold", color=GREY)
    b += text(300, 80, "OUTPUT  f(x)", 10, weight="bold", color=GREY)
    b += rbox(180, 172, 88, 150, "", "#F6F2FB", P, rx=10)
    b += text(180, 158, "f", 24, weight="bold", color=P)
    b += text(180, 186, "x² + 1", 11.5, color=P)
    b += text(180, 216, "one rule", 9.8, color=GREY)
    b += text(180, 232, "one output", 9.8, color=GREY)
    y = 118
    for xin, out in (("x = −2", "5"), ("x = 0", "1"), ("x = 2", "5")):
        b += rbox(62, y, 84, 32, xin, RF, RED, 11)
        b += arr([(106, y), (128, y)], "#333")
        b += arr([(226, y), (250, y)], "#333")
        b += rbox(300, y, 84, 32, out, GF, GREEN, 13, weight="bold", color="#1B5E20")
        y += 54
    b += foot(290, "Every input gives exactly one output, but two inputs may",
              "share an output: f(−2) = f(2) = 5.")
    return svg(360, 334, b)


# ---------------------------------------------------------------- 5. three shapes
def shapes():
    b = heading("Three shapes you must recognise", "The curve tells you the domain and the range")

    def panel(cx, kind):
        s = line(f"M{cx-46} 176 H{cx+46}", "#333", 1.4)
        s += line(f"M{cx-22} 84 V176", "#333", 1.4)
        if kind == "linear":
            s += line(f"M{cx-40} 168 L{cx+34} 92", BLUE, 2.2)
        elif kind == "quad":
            pts = []
            for i in range(41):
                xv = -1.0 + 2.2 * i / 40
                yv = xv * xv - 0.2
                pts.append(f"{cx + 6 + xv * 22:.1f} {150 - yv * 26:.1f}")
            s += f'<polyline points="{" ".join(pts)}" fill="none" stroke="{P}" stroke-width="2.2"/>'
        else:
            pts = []
            for i in range(41):
                xv = -1.0 + 2.0 * i / 40
                yv = 1.6 ** xv
                pts.append(f"{cx - 14 + xv * 22:.1f} {168 - (yv - 0.35) * 40:.1f}")
            s += f'<polyline points="{" ".join(pts)}" fill="none" stroke="{GREEN}" stroke-width="2.2"/>'
        return s

    data = [(72, "linear", "linear", "y = mx + c", BLUE),
            (180, "quad", "quadratic", "y = ax² + bx + c", P),
            (288, "exp", "exponential", "y = aˣ", GREEN)]
    for cx, kind, name, rule, _c in data:
        b += f'<rect x="{cx-52}" y="70" width="104" height="112" rx="8" fill="#FCFCFD" stroke="#DDD"/>'
        b += panel(cx, kind)
        b += text(cx, 200, name, 11, weight="bold", color=_c)
        b += text(cx, 216, rule, 8.8, color=GREY)
    b += foot(240, "Only the exponential never touches the x-axis: its range is y > 0.",
              "The logarithm is its mirror image, so its domain is x > 0.")
    return svg(360, 292, b)


# ---------------------------------------------------------------- 6. exp vs log
def exp_log():
    b = heading("Exponential and logarithm are mirrors", "Reflect y = 2ˣ in the line y = x")
    ox, oy, u = 104, 262, 52

    def X(v):
        return ox + v * u

    def Y(v):
        return oy - v * u

    b += line(f"M28 {oy} H338", "#333", 1.5)
    b += f'<polygon points="344,{oy} 334,{oy-4} 334,{oy+4}" fill="#333"/>'
    b += line(f"M{ox} 54 V{oy+62}", "#333", 1.5)
    b += text(332, oy - 10, "x", 11, color="#333", anchor="end")
    b += text(ox + 10, 62, "y", 11, color="#333", anchor="end")
    b += line(f"M{X(-1.3):.1f} {Y(-1.3):.1f} L{X(2.6):.1f} {Y(2.6):.1f}", "#999", 1.3, dash="5 4")
    # y = 2^x
    pts = []
    for i in range(61):
        xv = -1.55 + 3.0 * i / 60
        pts.append(f"{X(xv):.1f} {Y(2 ** xv):.1f}")
    b += f'<polyline points="{" ".join(pts)}" fill="none" stroke="{BLUE}" stroke-width="2.3"/>'
    # y = log2 x
    pts = []
    for i in range(61):
        xv = 0.45 + 2.73 * i / 60
        pts.append(f"{X(xv):.1f} {Y(math.log2(xv)):.1f}")
    b += f'<polyline points="{" ".join(pts)}" fill="none" stroke="{GREEN}" stroke-width="2.3"/>'
    b += f'<circle cx="{X(1)}" cy="{Y(0)}" r="3.6" fill="{ORANGE}"/>'
    b += f'<circle cx="{X(0)}" cy="{Y(1)}" r="3.6" fill="{ORANGE}"/>'
    b += text(X(1) + 10, Y(0) + 18, "(1, 0)", 9.4, color=ORANGE, anchor="start")
    b += text(X(0) - 8, Y(1) - 8, "(0, 1)", 9.4, color=ORANGE, anchor="end")
    b += text(X(1.35), Y(2.75), "y = 2ˣ", 11, color=BLUE, weight="bold", anchor="start")
    b += text(258, 244, "y = log₂ x", 11, color=GREEN, weight="bold")
    b += text(292, 104, "y = x", 10, color="#777", anchor="end")
    b += foot(348, "Domain of log₂ x: x > 0.  Range: every real y.",
              "Neither curve ever touches the axis it approaches.")
    return svg(360, 392, b)


# ---------------------------------------------------------------- 7. log laws
def loglaws():
    b = heading("The four logarithm laws", "All four come from the index laws")
    rows = [("Product", "log(xy) = log x + log y", "log 6 = log 2 + log 3", GF, GREEN),
            ("Quotient", "log(x/y) = log x − log y", "log 1.5 = log 3 − log 2", BF, BLUE),
            ("Power", "log(xⁿ) = n log x", "log 8 = 3 log 2", OF, ORANGE),
            ("Change of base", "logₐ x = log_b x / log_b a", "log₄ 8 = log₂ 8 / log₂ 4", RF, RED)]
    y = 64
    for name, law, example, fill, stroke in rows:
        b += f'<rect x="16" y="{y}" width="328" height="56" rx="8" fill="{fill}" stroke="{stroke}" stroke-width="1.5"/>'
        b += text(30, y + 22, name, 10.6, weight="bold", color=stroke, anchor="start")
        b += text(30, y + 42, law, 12.4, color="#222", anchor="start")
        b += text(330, y + 22, example, 9.6, color=GREY, anchor="end")
        y += 64
    b += foot(y + 6, "The laws need positive arguments and a base a > 0, a ≠ 1.",
              "log(x + y) does not split: only products, quotients and powers do.")
    return svg(360, y + 58, b)


ALL = {
    "m1_det2": det2,
    "m1_det3": det3,
    "m1_cramer": cramer,
    "m1_function": machine,
    "m1_graphs": shapes,
    "m1_exp_log": exp_log,
    "m1_loglaws": loglaws,
}
