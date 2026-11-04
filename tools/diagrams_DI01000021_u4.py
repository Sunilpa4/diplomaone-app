"""Seven compact mobile SVGs for Mathematics-I Unit 4 (Coordinate Geometry)."""
import math

from flowchart_lib import svg, text, arr, rbox, line, P

BLUE, BF = "#1565C0", "#EAF3FD"
GREEN, GF = "#2E7D32", "#EAF6EC"
ORANGE, OF = "#B66A00", "#FFF4DF"
RED, RF = "#BD2543", "#FDECF0"
GREY = "#666"

TITLES = {
    "cg1_slope": "Slope is rise over run",
    "cg2_forms": "Four forms of a straight line",
    "cg3_parallel": "Parallel and perpendicular",
    "cg4_angle": "Angle between two lines",
    "cg5_circle": "Centre, radius, tangent and normal",
    "cg6_general": "Reading the general circle",
    "cg7_tangent": "Tangent from an external point",
}


def heading(t, sub=None):
    body = text(180, 24, t, 14, weight="bold", color=P)
    if sub:
        body += text(180, 46, sub, 10.5, color=GREY)
    return body


def foot(y, *lines):
    return "".join(text(180, y + 16 * i, s, 10.2, color=GREY) for i, s in enumerate(lines))


def grid(x0, x1, y0, y1, step=40):
    b = ""
    x = x0
    while x <= x1:
        b += line(f"M{x} {y0} V{y1}", "#EFEAF5", 1.0)
        x += step
    y = y0
    while y <= y1:
        b += line(f"M{x0} {y} H{x1}", "#EFEAF5", 1.0)
        y += step
    return b


# ---------------------------------------------------------------- 1. slope
def slope():
    b = heading("Slope is rise over run", "m = (y₂ − y₁)/(x₂ − x₁) = tan θ")
    x0, y0, x1, y1 = 50, 70, 320, 250
    b += grid(x0, x1, y0, y1)
    b += line(f"M{x0} {y1} H{x1}", "#333", 1.5)
    b += line(f"M{x0} {y1} V{y0}", "#333", 1.5)
    p1, p2 = (104, 208), (270, 108)
    b += line(f"M{p1[0]} {p1[1]} L{p2[0]} {p2[1]}", BLUE, 2.2)
    b += line(f"M{p1[0]} {p1[1]} H{p2[0]}", ORANGE, 1.6, dash="5 4")
    b += line(f"M{p2[0]} {p1[1]} V{p2[1]}", GREEN, 1.6, dash="5 4")
    b += f'<circle cx="{p1[0]}" cy="{p1[1]}" r="4" fill="{RED}"/>'
    b += f'<circle cx="{p2[0]}" cy="{p2[1]}" r="4" fill="{RED}"/>'
    b += text(p1[0] - 8, p1[1] + 18, "(x₁, y₁)", 9.2, color=RED, anchor="end")
    b += text(p2[0] + 8, p2[1] - 8, "(x₂, y₂)", 9.2, color=RED, anchor="start")
    b += text((p1[0] + p2[0]) / 2, p1[1] + 16, "run", 9.6, color=ORANGE)
    b += text(p2[0] + 10, (p1[1] + p2[1]) / 2, "rise", 9.6, color=GREEN, anchor="start")
    b += f'<path d="M{p1[0]+46} {p1[1]} A46 46 0 0 0 {p1[0]+42} {p1[1]-17}" fill="none" stroke="{P}" stroke-width="1.3"/>'
    b += text(p1[0] + 54, p1[1] - 6, "θ", 10, color=P, weight="bold")
    b += rbox(180, 282, 320, 30, "m = rise/run = tan θ", BF, BLUE, 11.2)
    b += foot(330, "A larger slope means a steeper line; a negative slope falls.",
              "Vertical line: slope undefined, x = a.")
    return svg(360, 360, b)


# ---------------------------------------------------------------- 2. four forms
def forms():
    b = heading("Four forms of a straight line", "Pick the one that matches what you know")
    rows = [("Slope-intercept", "y = mx + c", "slope + y-intercept", GF, GREEN),
            ("Point-slope", "y − y₁ = m(x − x₁)", "one point + slope", BF, BLUE),
            ("Two-point", "(y − y₁)/(y₂ − y₁) = (x − x₁)/(x₂ − x₁)", "two points", OF, ORANGE),
            ("Intercept", "x/a + y/b = 1", "both intercepts", RF, RED)]
    y = 64
    for name, eq, when, fill, stroke in rows:
        b += f'<rect x="16" y="{y}" width="328" height="52" rx="8" fill="{fill}" stroke="{stroke}" stroke-width="1.4"/>'
        b += text(28, y + 20, name, 10.4, weight="bold", color=stroke, anchor="start")
        b += text(28, y + 40, eq, 11.6, color="#222", anchor="start")
        b += text(332, y + 20, when, 8.8, color=GREY, anchor="end")
        y += 60
    b += foot(y + 4, "All four describe the same object - a straight line.", "Convert to ax + by + c = 0 for a final answer.")
    return svg(360, y + 52, b)


# ---------------------------------------------------------------- 3. parallel
def parallel():
    b = heading("Parallel and perpendicular", "m₁ = m₂   and   m₁m₂ = −1")
    # upper panel: a parallel pair
    b += text(34, 72, "parallel", 9.4, color=GREY, anchor="start")
    b += line("M46 150 L206 82", BLUE, 2.1)
    b += line("M46 184 L206 116", BLUE, 2.1)
    b += text(214, 88, "m₁ = m₂", 9.8, color=BLUE, anchor="start")
    b += text(214, 106, "same slope", 8.8, color=GREY, anchor="start")
    # lower panel: a perpendicular pair with a right-angle marker
    b += text(34, 206, "perpendicular", 9.4, color=GREY, anchor="start")
    b += line("M84 250 H268", GREEN, 2.1)
    b += line("M176 198 V250", GREEN, 2.1)
    b += f'<path d="M176 238 h12 v12" fill="none" stroke="{GREEN}" stroke-width="1.2"/>'
    b += text(186, 220, "90°", 9.4, color=GREEN, anchor="start")
    b += text(276, 238, "m₁m₂ = −1", 9.8, color=GREEN, anchor="end")
    b += rbox(180, 288, 320, 26, "general form:  a₁/a₂ = b₁/b₂   and   a₁a₂ + b₁b₂ = 0", BF, BLUE, 9.6)
    b += foot(322, "Parallel lines never meet; perpendicular lines cross at 90°.",
              "Change only the constant to slide a line without turning it.")
    return svg(360, 376, b)


# ---------------------------------------------------------------- 4. angle
def angle():
    b = heading("Angle between two lines", "tan θ = |(m₁ − m₂)/(1 + m₁m₂)|")
    x0, y0, x1, y1 = 44, 66, 322, 232
    b += grid(x0, x1, y0, y1)
    b += line(f"M{x0} {y1} H{x1}", "#333", 1.4)
    b += line(f"M{x0} {y1} V{y0}", "#333", 1.4)
    c = (180, 172)
    b += line(f"M{c[0]-120} {c[1]+68} L{c[0]+120} {c[1]-54}", BLUE, 2.1)
    b += line(f"M{c[0]-116} {c[1]-60} L{c[0]+118} {c[1]+62}", GREEN, 2.1)
    b += f'<path d="M{c[0]+52} {c[1]-24} A56 56 0 0 0 {c[0]+50} {c[1]+20}" fill="none" stroke="{ORANGE}" stroke-width="1.5"/>'
    b += text(c[0] + 74, c[1] + 10, "θ", 11, color=ORANGE, weight="bold")
    b += text(c[0] - 34, c[1] + 8, "m₁", 10, color=BLUE, weight="bold", anchor="end")
    b += text(c[0] + 36, c[1] + 32, "m₂", 10, color=GREEN, weight="bold", anchor="start")
    b += rbox(180, 268, 320, 28, "vertical denominator ⇒ θ = 90°; equal slopes ⇒ θ = 0°", OF, ORANGE, 9.6)
    b += foot(314, "The modulus gives the acute angle between the lines.",
              "Subtract the result from 180° when the obtuse angle is asked.")
    return svg(360, 344, b)


# ---------------------------------------------------------------- 5. circle
def circle():
    b = heading("Centre, radius, tangent and normal", "The tangent is perpendicular to the radius")
    cx, cy, r = 158, 172, 76
    b += line("M40 258 H324", "#333", 1.3)
    b += line("M56 268 V70", "#333", 1.3)
    b += f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="#FBF8FD" stroke="{P}" stroke-width="1.8"/>'
    ang = math.radians(35)
    ux, uy = math.cos(ang), -math.sin(ang)
    px, py = cx + r * ux, cy + r * uy
    tx, ty = -uy, ux
    # normal = the whole diameter through P and C
    b += line(f"M{cx - r*ux:.1f} {cy - r*uy:.1f} L{px:.1f} {py:.1f}", BLUE, 1.5, dash="6 4")
    b += f'<circle cx="{cx}" cy="{cy}" r="4" fill="{P}"/>'
    b += text(cx - 10, cy + 20, "C(h, k)", 9.6, color=P, anchor="end")
    b += text((cx + px) / 2 - 10, (cy + py) / 2 - 10, "r", 11, color=BLUE, weight="bold")
    # tangent at P
    b += line(f"M{px - 86*tx:.1f} {py - 86*ty:.1f} L{px + 60*tx:.1f} {py + 60*ty:.1f}", GREEN, 2.2)
    b += f'<circle cx="{px:.1f}" cy="{py:.1f}" r="4" fill="{RED}"/>'
    b += text(px + 8, py - 6, "P(x₁, y₁)", 9.4, color=RED, anchor="start")
    b += text(px + 66 * tx + 6, py + 66 * ty + 6, "tangent", 9.6, color=GREEN, anchor="start")
    b += text(cx - 76 * ux - 8, cy - 76 * uy + 12, "normal", 9.4, color=BLUE, anchor="end")
    # right angle between radius and tangent at P
    ax_, ay_ = px - 12 * ux, py - 12 * uy
    bx_, by_ = px + 12 * tx, py + 12 * ty
    b += (f'<path d="M{ax_:.1f} {ay_:.1f} L{ax_ + 12*tx:.1f} {ay_ + 12*ty:.1f} '
          f'L{bx_:.1f} {by_:.1f}" fill="none" stroke="{ORANGE}" stroke-width="1.3"/>')
    b += rbox(180, 292, 320, 28, "tangent: xx₁ + yy₁ = a²   for  x² + y² = a²", GF, GREEN, 10.2)
    b += foot(334, "The normal always passes through the centre.", "Slopes of tangent and radius multiply to −1.")
    return svg(360, 366, b)


# ---------------------------------------------------------------- 6. general circle
def general():
    b = heading("Reading the general circle", "Centre and radius straight from the coefficients")
    b += rbox(180, 74, 320, 30, "x² + y² + 2gx + 2fy + c = 0", BF, BLUE, 11.6)
    b += arr([(180, 89), (180, 110)], P)
    b += rbox(180, 128, 320, 30, "complete the square in x and in y", "#F4F4F4", "#999", 10.6, color="#333")
    b += arr([(180, 143), (180, 164)], P)
    b += rbox(180, 182, 320, 30, "(x + g)² + (y + f)² = g² + f² − c", GF, GREEN, 10.6)
    b += arr([(128, 197), (96, 218)], "#333")
    b += arr([(232, 197), (264, 218)], "#333")
    b += rbox(96, 236, 150, 34, "centre (−g, −f)", OF, ORANGE, 10.6)
    b += rbox(266, 236, 150, 34, "radius √(g² + f² − c)", RF, RED, 10)
    b += rbox(180, 288, 320, 30, "example: x² + y² − 6x + 8y − 11 = 0", "#F6F2FB", P, 10.2)
    b += foot(326, "gives centre (3, −4) and radius 6.", "Divide by 2 first if the coefficients are not 1.")
    return svg(360, 356, b)


# ---------------------------------------------------------------- 7. tangent length
def tangent():
    b = heading("Tangent from an external point", "Length = √(x₁² + y₁² − a²)")
    cx, cy, r = 106, 196, 58
    px, py = 300, 196
    b += f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="#FBF8FD" stroke="{P}" stroke-width="1.7"/>'
    b += f'<circle cx="{cx}" cy="{cy}" r="3.4" fill="{P}"/>'
    b += text(cx - 8, cy + 20, "C", 10, color=P, anchor="end")
    b += f'<circle cx="{px}" cy="{py}" r="4" fill="{RED}"/>'
    b += text(px - 4, py + 24, "P(x₁, y₁)", 9.4, color=RED, anchor="end")
    d = px - cx
    t = r * r / d
    tx_, ty_ = cx + t, cy - math.sqrt(r * r - t * t)
    b += line(f"M{px} {py} H{cx}", "#999", 1.2, dash="5 4")
    b += line(f"M{px} {py} L{tx_:.1f} {ty_:.1f}", GREEN, 2.1)
    b += line(f"M{cx} {cy} L{tx_:.1f} {ty_:.1f}", BLUE, 1.5, dash="5 3")
    b += f'<circle cx="{tx_:.1f}" cy="{ty_:.1f}" r="3.8" fill="{ORANGE}"/>'
    b += text(tx_ - 6, ty_ - 10, "T", 10, color=ORANGE, weight="bold", anchor="middle")
    # right angle at T between radius TC and tangent TP
    v1 = (cx - tx_, cy - ty_)
    v2 = (px - tx_, py - ty_)
    n1 = math.hypot(*v1); n2 = math.hypot(*v2)
    u1 = (v1[0] / n1, v1[1] / n1)
    u2 = (v2[0] / n2, v2[1] / n2)
    m = 12
    a1 = (tx_ + m * u1[0], ty_ + m * u1[1])
    a2 = (tx_ + m * u2[0], ty_ + m * u2[1])
    cr = (a1[0] + m * u2[0], a1[1] + m * u2[1])
    b += (f'<path d="M{a1[0]:.1f} {a1[1]:.1f} L{cr[0]:.1f} {cr[1]:.1f} '
          f'L{a2[0]:.1f} {a2[1]:.1f}" fill="none" stroke="{ORANGE}" stroke-width="1.3"/>')
    b += text((cx + px) / 2 - 14, cy + 18, "CP", 9.6, color=GREY, weight="bold")
    b += text(206, 158, "tangent", 9.6, color=GREEN, anchor="middle")
    b += rbox(180, 270, 320, 26, "CT² = CP² − r²,  so  tangent = √(CP² − r²)", GF, GREEN, 10.4)
    b += foot(312, "CP is the distance from the centre; CT is the radius r.",
              "CT is perpendicular to the tangent at T.")
    return svg(360, 344, b)


ALL = {
    "cg1_slope": slope,
    "cg2_forms": forms,
    "cg3_parallel": parallel,
    "cg4_angle": angle,
    "cg5_circle": circle,
    "cg6_general": general,
    "cg7_tangent": tangent,
}
