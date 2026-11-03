"""Six compact mobile SVGs for Mathematics-I Unit 5 (Limit)."""
import math

from flowchart_lib import svg, text, arr, rbox, line, P

BLUE, BF = "#1565C0", "#EAF3FD"
GREEN, GF = "#2E7D32", "#EAF6EC"
ORANGE, OF = "#B66A00", "#FFF4DF"
RED, RF = "#BD2543", "#FDECF0"
GREY = "#666"

TITLES = {
    "l1_hole": "A limit fills in the hole",
    "l2_sided": "Two one-sided limits must agree",
    "l3_table": "A table shows where the values go",
    "l4_sinx": "Why sin x / x tends to 1",
    "l5_e": "e as the end of (1 + 1/n)^n",
    "l6_flow": "Which technique should I use?",
}


def heading(t, sub=None):
    body = text(180, 24, t, 14, weight="bold", color=P)
    if sub:
        body += text(180, 46, sub, 10.5, color=GREY)
    return body


def foot(y, *lines):
    return "".join(text(180, y + 16 * i, s, 10.2, color=GREY) for i, s in enumerate(lines))


# ---------------------------------------------------------------- 1. hole
def hole():
    b = heading("A limit fills in the hole", "f(x) = (x² − 1)/(x − 1)  is  y = x + 1  with one point missing")
    ox, oy = 70, 250
    b += line(f"M{ox} {oy} H320", "#333", 1.4)
    b += f'<polygon points="326,{oy} 316,{oy-4} 316,{oy+4}" fill="#333"/>'
    b += line(f"M{ox} {oy} V80", "#333", 1.4)
    b += text(ox - 6, oy + 16, "O", 9.5, color="#333", anchor="end")
    b += text(318, oy - 8, "x", 10, color="#333", anchor="end")
    b += text(ox + 10, 86, "y", 10, color="#333", anchor="start")
    # y = x + 1 drawn from x = 0.2 to x = 3.4 in maths units
    def pt(x):
        return (ox + x * 62, oy - (x + 1) * 42)

    x_lo, x_hi = 0.15, 3.5
    b += line(f"M{pt(x_lo)[0]:.1f} {pt(x_lo)[1]:.1f} L{pt(x_hi)[0]:.1f} {pt(x_hi)[1]:.1f}", BLUE, 2.2)
    # the hole at x = 1, y = 2
    hx, hy = pt(1.0)
    b += f'<circle cx="{hx:.1f}" cy="{hy:.1f}" r="4.6" fill="#ffffff" stroke="{RED}" stroke-width="2"/>'
    b += text(96, 110, "f(1) is undefined: a hole", 9, color=RED, anchor="start")
    b += text(hx + 18, hy - 17, "(1, 2)", 9.4, color=RED, anchor="start")
    b += line(f"M{hx + 40:.1f} {hy:.1f} H300", "#B9A7D6", 1.0, dash="4 3")
    b += text(302, hy + 4, "2", 10, color=P, weight="bold", anchor="start")
    b += rbox(180, 292, 320, 28, "limit = 2 although f(1) does not exist", BF, BLUE, 10.6)
    b += foot(334, "The graph is a straight line with a single missing point.",
              "A limit asks where the curve is heading, not whether it arrives.")
    return svg(360, 366, b)


# ---------------------------------------------------------------- 2. one-sided
def sided():
    b = heading("Two one-sided limits must agree", "f(x) = x + 2 for x < 1,   f(x) = 4x for x ≥ 1")
    ox, oy = 70, 262
    b += line(f"M{ox} {oy} H320", "#333", 1.4)
    b += f'<polygon points="326,{oy} 316,{oy-4} 316,{oy+4}" fill="#333"/>'
    b += line(f"M{ox} {oy} V92", "#333", 1.4)
    b += text(318, oy - 8, "x", 10, color="#333", anchor="end")

    def u(x):
        return ox + x * 100

    def v(y):
        return oy - y * 34

    # left branch y = x + 2, open at (1, 3)
    b += line(f"M{u(0.15):.1f} {v(2.15):.1f} L{u(0.97):.1f} {v(2.97):.1f}", BLUE, 2.2)
    b += f'<circle cx="{u(1):.1f}" cy="{v(3):.1f}" r="4.4" fill="#ffffff" stroke="{BLUE}" stroke-width="2"/>'
    # right branch y = 4x, closed at (1, 4)
    b += line(f"M{u(1):.1f} {v(4):.1f} L{u(1.3):.1f} {v(5.2):.1f}", GREEN, 2.2)
    b += f'<circle cx="{u(1):.1f}" cy="{v(4):.1f}" r="4.4" fill="{GREEN}"/>'
    b += text(84, 148, "left limit = 3", 9.6, color=BLUE, anchor="start")
    b += text(240, 122, "right limit = 4", 9.6, color=GREEN, anchor="start")
    b += text(u(1) + 8, oy - 8, "x = 1", 9.4, color="#333", anchor="start")
    b += line(f"M{u(1) + 10:.1f} {v(4) - 6:.1f} V{v(3) + 6:.1f}", "#A99BBF", 1.0, dash="3 3")
    b += text(u(1) + 14, (v(3) + v(4)) / 2 + 4, "jump", 8.8, color=GREY, anchor="start")
    b += rbox(180, 296, 320, 28, "3 ≠ 4  ⇒  the limit does not exist (a jump)", RF, RED, 10.6)
    b += foot(338, "Both branches exist at x = 1, but they end at different heights.",
              "When the one-sided limits differ, no single L works.")
    return svg(360, 368, b)


# ---------------------------------------------------------------- 3. table
def table_diagram():
    b = heading("A table shows where the values go", "f(x) = (x² − 1)/(x − 1) near x = 1")
    rows = [("0.9", "1.9"), ("0.99", "1.99"), ("0.999", "1.999"), ("1.001", "2.001"), ("1.01", "2.01")]
    b += (f'<rect x="34" y="66" width="292" height="{34 + 24 * len(rows)}" rx="8" fill="#FBF8FD" '
          f'stroke="#C9B4E4" stroke-width="1.3"/>')
    b += text(104, 84, "x approaching 1", 9.6, color=P, weight="bold")
    b += text(266, 84, "f(x)", 9.6, color=P, weight="bold")
    b += line("M42 92 H318", "#D8C8EC", 1.1)
    for i, (x, y) in enumerate(rows):
        yy = 112 + 24 * i
        b += text(104, yy, x, 10.4, color="#333")
        b += text(266, yy, y, 10.4, color=BLUE, weight="bold")
        if i < len(rows) - 1:
            b += line(f"M42 {yy + 8} H318", "#EFE6F8", 0.9)
    b += text(180, 128 + 24 * len(rows), "both sides head for 2", 10.4, color=GREEN, weight="bold")
    b += rbox(180, 300, 320, 26, "a table guesses the limit; algebra proves it", OF, ORANGE, 10.2)
    b += foot(340, "The values below 1 and above 1 close in on the same number.",
              "Note that f(1) itself is never evaluated.")
    return svg(360, 372, b)


# ---------------------------------------------------------------- 4. sin x / x
def sinx():
    b = heading("Why sin x / x tends to 1", "sin x < x < tan x for 0 < x < π/2, then divide by sin x")
    ox, oy = 180, 210
    b += line("M28 210 H332", "#333", 1.4)
    b += line(f"M{ox} 96 V268", "#333", 1.4)
    b += text(324, 200, "x", 10, color="#333", anchor="end")
    b += text(ox + 10, 104, "y", 10, color="#333", anchor="start")
    # y = 1 dashed
    b += line("M34 128 H326", GREEN, 1.1, dash="5 4")
    b += text(320, 108, "y = 1", 9.4, color=GREEN, anchor="end")
    # plot sin x / x over [-9, 9] avoiding 0
    xmin, xmax, scale = -9.4, 9.4, 15.0
    pts = []
    x = xmin
    while x <= xmax:
        if abs(x) > 0.28:
            y = math.sin(x) / x
            pts.append((ox + x * scale, oy - y * 84))
        x += 0.12
    d = "M" + " L".join(f"{px:.1f} {py:.1f}" for px, py in pts)
    b += f'<path d="{d}" fill="none" stroke="{BLUE}" stroke-width="2.1" stroke-linejoin="round"/>'
    b += f'<circle cx="{ox}" cy="{oy - 84}" r="4.2" fill="#ffffff" stroke="{RED}" stroke-width="1.9"/>'

    b += line(f"M{ox - 26} {oy - 84} H{ox - 10}", RED, 1.0, dash="4 3")
    b += rbox(180, 292, 320, 28, "limit = 1, so sin x ≈ x for small x (in radians)", BF, BLUE, 10.2)
    b += foot(334, "The curve settles at height 1 as it approaches the y-axis.",
              "The same sandwich argument gives tan x / x → 1.")
    return svg(360, 366, b)


# ---------------------------------------------------------------- 5. e
def e_limit():
    b = heading("e as the end of (1 + 1/n)^n", "each bar is one more step; the values level off at e")
    base, left = 236, 44
    b += line(f"M{left} {base} H322", "#333", 1.3)
    b += line(f"M{left} {base} V74", "#333", 1.3)
    vals = [(1, 2.0), (2, 2.25), (3, 2.370), (4, 2.441), (5, 2.488), (6, 2.522)]
    for i, (n, v) in enumerate(vals):
        x = left + 16 + i * 44
        h = (v - 1.95) * 200
        b += (f'<rect x="{x}" y="{base - h:.1f}" width="26" height="{h:.1f}" rx="4" '
              f'fill="{BF}" stroke="{BLUE}" stroke-width="1.3"/>')
        b += text(x + 13, base + 18, f"n={n}", 8.6, color="#333")
        b += text(x + 13, base - h - 7, f"{v:.2f}", 8.6, color=BLUE)
    ye = base - (2.71828 - 1.95) * 200
    b += line(f"M{left + 4} {ye:.1f} H322", GREEN, 1.3, dash="5 4")
    b += text(320, ye - 7, "e ≈ 2.718", 9.4, color=GREEN, anchor="end")
    b += text(60, 96, "(1 + 1/n)^n", 9.4, color=GREY, anchor="start")
    b += rbox(180, 286, 320, 28, "the sequence climbs but never passes e", GF, GREEN, 10.4)
    b += foot(328, "e = lim (1 + 1/n)^n = lim (1 + x)^(1/x).",
              "Compounding interest every instant is this same limit.")
    return svg(360, 362, b)


# ---------------------------------------------------------------- 6. flow
def flow():
    b = heading("Which technique should I use?", "work down the list until the 0/0 disappears")
    steps = [
        ("1.  Substitute x = a", BF, BLUE),
        ("2.  finite value?  that is the answer", GF, GREEN),
        ("3.  0/0  →  factorise or rationalise", OF, ORANGE),
        ("4.  trigonometric or e?  use a standard limit", OF, ORANGE),
        ("5.  x → ∞  →  divide by the highest power", RF, RED),
    ]
    y = 74
    for label, fill, stroke in steps:
        b += rbox(180, y, 322, 30, label, fill, stroke, 10.0)
        y += 44
    for i in range(len(steps) - 1):
        top = 74 + 44 * i + 16
        b += arr([(180, top), (180, top + 12)], P)
    b += foot(y + 18, "Stop as soon as substituting gives a number.",
              "Each step is a rewrite, never a guess.")
    return svg(360, y + 70, b)


ALL = {
    "l1_hole": hole,
    "l2_sided": sided,
    "l3_table": table_diagram,
    "l4_sinx": sinx,
    "l5_e": e_limit,
    "l6_flow": flow,
}
