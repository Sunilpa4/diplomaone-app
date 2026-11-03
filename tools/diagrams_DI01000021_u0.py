"""Six compact mobile SVGs for Mathematics-I Unit 0 ("Start Mathematics From Zero").

360 px wide, white background, no <marker>/<style>/<image>/href, text kept inside the canvas.
"""
from flowchart_lib import svg, text, arr, rbox, line, P

BLUE, BF = "#1565C0", "#EAF3FD"
GREEN, GF = "#2E7D32", "#EAF6EC"
ORANGE, OF = "#B66A00", "#FFF4DF"
RED, RF = "#BD2543", "#FDECF0"
GREY = "#666"

TITLES = {
    "m0_numberline": "The number line and absolute value",
    "m0_bodmas": "BODMAS: one fixed order",
    "m0_factor": "Area model for (x + 2)(x + 3)",
    "m0_parabola": "A quadratic is a parabola",
    "m0_quadrants": "The four quadrants",
    "m0_cycle": "The five-step study cycle",
}


def heading(t, sub=None):
    body = text(180, 24, t, 14, weight="bold", color=P)
    if sub:
        body += text(180, 46, sub, 10.5, color=GREY)
    return body


def foot(y, *lines):
    return "".join(text(180, y + 16 * i, s, 10.2, color=GREY) for i, s in enumerate(lines))


# ---------------------------------------------------------------- 1. number line
def numberline():
    b = heading("One line holds every number", "Right adds, left subtracts, |x| is the distance from 0")
    y = 150
    b += line(f"M24 {y} H330", "#333", 2.0)
    b += f'<polygon points="342,{y} 332,{y-4} 332,{y+4}" fill="#333"/>'
    for v in range(-6, 7):
        x = 24 + (v + 6) * 26
        b += line(f"M{x} {y-5} V{y+5}", "#333", 1.5)
        b += text(x, y + 20, ("−" if v < 0 else "") + str(abs(v)), 9, color="#333")
    # the distance between −3 and 2
    b += line(f"M{24+3*26} {y-46} H{24+8*26}", GREEN, 1.6, dash="4 3")
    b += text(180, y - 56, "distance = |2 − (−3)| = 5", 10.2, color=GREEN, weight="bold")
    b += f'<circle cx="{24+3*26}" cy="{y}" r="4" fill="{RED}"/>'
    b += f'<circle cx="{24+8*26}" cy="{y}" r="4" fill="{BLUE}"/>'
    b += text(24 + 3 * 26, y - 14, "−3", 10, color=RED, weight="bold")
    b += text(24 + 8 * 26, y - 14, "2", 10, color=BLUE, weight="bold")
    b += foot(y + 46, "−5 < −2 because −5 is further left.", "|−3| = 3 and |2| = 2: absolute value drops the sign.")
    return svg(360, y + 90, b)


# ---------------------------------------------------------------- 2. BODMAS
def bodmas():
    b = heading("BODMAS: one fixed order of work", "Different orders give different answers")
    steps = [("B  Brackets", "(5 − 3) = 2", BF, BLUE),
             ("O  Orders", "2² = 4", GF, GREEN),
             ("D  Division", "none here", "#F4F4F4", "#888"),
             ("M  Multiplication", "2 × 4 = 8", OF, ORANGE),
             ("A  Addition", "8 + 8 = 16", GF, GREEN),
             ("S  Subtraction", "none here", "#F4F4F4", "#888")]
    y = 64
    for name, detail, fill, stroke in steps:
        b += f'<rect x="18" y="{y}" width="324" height="38" rx="8" fill="{fill}" stroke="{stroke}" stroke-width="1.5"/>'
        b += text(108, y + 19, name, 11.5, weight="bold", color=stroke)
        b += text(258, y + 19, detail, 10.8, color="#333")
        y += 44
    b += foot(y + 6, "8 + 2 × (5 − 3)² = 8 + 2(4) = 16", "2 + 3 × 4 = 14, never 20")
    return svg(360, y + 56, b)


# ---------------------------------------------------------------- 3. area model
def factor():
    b = heading("Area model: (x + 2)(x + 3)", "Every cell is one product of the expansion")
    x0, y0, w1, w2, h1, h2 = 60, 84, 170, 70, 130, 50
    b += f'<rect x="{x0}" y="{y0}" width="{w1}" height="{h1}" fill="{BF}" stroke="{BLUE}" stroke-width="1.4"/>'
    b += f'<rect x="{x0+w1}" y="{y0}" width="{w2}" height="{h1}" fill="{OF}" stroke="{ORANGE}" stroke-width="1.4"/>'
    b += f'<rect x="{x0}" y="{y0+h1}" width="{w1}" height="{h2}" fill="{OF}" stroke="{ORANGE}" stroke-width="1.4"/>'
    b += f'<rect x="{x0+w1}" y="{y0+h1}" width="{w2}" height="{h2}" fill="{GF}" stroke="{GREEN}" stroke-width="1.4"/>'
    b += f'<rect x="{x0}" y="{y0}" width="{w1+w2}" height="{h1+h2}" fill="none" stroke="#333" stroke-width="2"/>'
    b += text(x0 + w1 / 2, y0 + h1 / 2, "x²", 15, weight="bold", color=BLUE)
    b += text(x0 + w1 + w2 / 2, y0 + h1 / 2, "2x", 14, weight="bold", color=ORANGE)
    b += text(x0 + w1 / 2, y0 + h1 + h2 / 2, "3x", 14, weight="bold", color=ORANGE)
    b += text(x0 + w1 + w2 / 2, y0 + h1 + h2 / 2, "6", 14, weight="bold", color=GREEN)
    b += text(x0 + w1 / 2, y0 - 8, "x", 11, color="#333")
    b += text(x0 + w1 + w2 / 2, y0 - 8, "2", 11, color="#333")
    b += text(x0 - 6, y0 + h1 / 2, "x", 11, color="#333", anchor="end")
    b += text(x0 - 6, y0 + h1 + h2 / 2, "3", 11, color="#333", anchor="end")
    b += foot(y0 + h1 + h2 + 26, "Area = x² + 2x + 3x + 6 = x² + 5x + 6", "Missing the cross terms is the classic expansion error.")
    return svg(360, y0 + h1 + h2 + 78, b)


# ---------------------------------------------------------------- 4. parabola
def parabola():
    b = heading("y = x² − 4x + 3 is a parabola", "Roots where y = 0, vertex where the curve turns")
    ox, oy, ux, uy = 70, 300, 55, 45

    def X(v):
        return ox + v * ux

    def Y(v):
        return oy - v * uy

    b += line(f"M34 {oy} H336", "#333", 1.6)
    b += f'<polygon points="342,{oy} 332,{oy-4} 332,{oy+4}" fill="#333"/>'
    b += line(f"M{ox} 96 V{oy+26}", "#333", 1.6)
    b += text(336, oy - 10, "x", 11, color="#333", anchor="end")
    b += text(ox + 12, 100, "y", 11, color="#333", anchor="end")
    pts = []
    v = -0.35
    while v <= 4.001:
        pts.append(f"{X(v):.1f} {Y(v*v - 4*v + 3):.1f}")
        v += 0.1
    b += f'<polyline points="{" ".join(pts)}" fill="none" stroke="{P}" stroke-width="2.4"/>'
    for t in (0, 1, 2, 3, 4):
        b += line(f"M{X(t)} {oy-4} V{oy+4}", "#333", 1.3)
        b += text(X(t), oy + 18, str(t), 9.5, color="#333")
    b += f'<circle cx="{X(1)}" cy="{oy}" r="4.2" fill="{GREEN}"/>'
    b += f'<circle cx="{X(3)}" cy="{oy}" r="4.2" fill="{GREEN}"/>'
    b += f'<circle cx="{X(2)}" cy="{Y(-1)}" r="4.2" fill="{RED}"/>'
    b += text(X(2) + 76, Y(-1) + 4, "vertex (2, −1)", 10.2, color=RED, weight="bold")
    b += text(X(1) - 12, oy - 12, "root 1", 9.6, color=GREEN, weight="bold")
    b += text(X(3) + 26, oy - 12, "root 3", 9.6, color=GREEN, weight="bold")
    b += text(268, 118, "y = x² − 4x + 3", 10.4, color=P, weight="bold")
    b += foot(oy + 70, "a > 0 so the parabola opens upward.", "D = b² − 4ac = 4 > 0 gives two real roots.")
    return svg(360, oy + 118, b)


# ---------------------------------------------------------------- 5. quadrants
def quadrants():
    b = heading("The four quadrants", "The sign of x and y names the quadrant")
    ox, oy = 180, 200
    b += line(f"M34 {oy} H332", "#333", 1.7)
    b += f'<polygon points="338,{oy} 328,{oy-4} 328,{oy+4}" fill="#333"/>'
    b += line(f"M{ox} 82 V{oy+72}", "#333", 1.7)
    b += f'<polygon points="{ox},78 {ox-4} 86 {ox+4} 86" fill="#333"/>'
    cells = [(60, 92, "II", "x −, y +", "(−4, 3)", BF, BLUE),
             (200, 92, "I", "x +, y +", "(3, 2)", GF, GREEN),
             (60, 212, "III", "x −, y −", "(−2, −5)", OF, ORANGE),
             (200, 212, "IV", "x +, y −", "(6, −1)", RF, RED)]
    for x, y, q, signs, ex, fill, stroke in cells:
        b += f'<rect x="{x}" y="{y}" width="100" height="76" rx="8" fill="{fill}" stroke="{stroke}" stroke-width="1.5"/>'
        b += text(x + 50, y + 24, q, 13, weight="bold", color=stroke)
        b += text(x + 50, y + 44, signs, 10.2)
        b += text(x + 50, y + 63, ex, 10.2, color=GREY)
    b += text(ox + 10, oy + 16, "O", 10, color="#333", anchor="start")
    b += foot(310, "Plot x first, then y.", "A point on the x-axis has y = 0.")
    return svg(360, 350, b)


# ---------------------------------------------------------------- 6. study cycle
def cycle():
    b = heading("The five-step study cycle", "Learn by doing, then loop back and revise")
    rows = [("1  Read a solved example", "Cover the solution, predict each line"),
            ("2  Copy it closed-book", "Compare line by line and mark the gap"),
            ("3  Change the numbers", "Same skeleton, your own values"),
            ("4  Attempt an unsolved one", "Write every step, even the wrong ones"),
            ("5  Log the error, revise", "After 1 day, 1 week, 1 month")]
    y = 76
    for name, detail in rows:
        b += rbox(212, y + 21, 272, 42, "", BF if y < 200 else GF, BLUE if y < 200 else GREEN, rx=8)
        b += text(212, y + 14, name, 11.2, weight="bold", color=BLUE if y < 200 else GREEN)
        b += text(212, y + 31, detail, 10.2, color="#333")
        y += 50
    b += line("M54 302 V104", ORANGE, 1.6, dash="4 3")
    b += f'<polygon points="54,96 50,104 58,104" fill="{ORANGE}"/>'
    b += foot(y + 8, "One numerical daily beats two hours on Sunday.", "Loop back to step 1 for every new topic.")
    return svg(360, y + 62, b)


ALL = {
    "m0_numberline": numberline,
    "m0_bodmas": bodmas,
    "m0_factor": factor,
    "m0_parabola": parabola,
    "m0_quadrants": quadrants,
    "m0_cycle": cycle,
}
