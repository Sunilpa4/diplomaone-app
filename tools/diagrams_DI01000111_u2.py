"""Seven construction diagrams for Engineering Graphics (DI01000111) Unit 2 - engineering curves.

English only. Thin lines are construction, thick lines are the finished curve, and every figure is
built from computed points so that the drawing matches the arithmetic in the notes.
"""
import math

from flowchart_lib import svg, text

INK = "#222"
GREY = "#666"
THIN = "#9AA3AD"
BLUE = "#1565C0"
GREEN = "#2E7D32"
ORANGE = "#B66A00"
RED = "#BD2543"
PURPLE = "#7B2CD9"
TEAL = "#00695C"

TITLES = {
    "u2_conic": "Three conics, one ratio: the eccentricity",
    "u2_ellipse": "Ellipse by concentric circles, 100 x 60",
    "u2_parabola": "Parabola: ordinates, focus and directrix",
    "u2_hyperbola": "Rectangular hyperbola from its asymptotes",
    "u2_cycloid": "Cycloid of a 25 mm radius circle",
    "u2_involute": "Involute of a 20 mm radius circle",
    "u2_spiral": "Archimedean spiral, one turn",
}

CAPTIONS = {
    "u2_conic": "e below 1 closes the curve into an ellipse, e = 1 leaves it open as a parabola, e "
                "above 1 opens two branches - and the ratio to the directrix is what fixes it.",
    "u2_ellipse": "Every point is the crossing of a vertical from the major circle and a horizontal "
                  "from the minor circle, so twelve rays give twenty-four points.",
    "u2_parabola": "The height falls with the square of the distance from the axis; the focus is a = "
                   "10.4 mm from the vertex and the directrix the same distance behind it.",
    "u2_hyperbola": "x times y is constant, so a table of six pairs sets out a branch - and the curve "
                    "approaches both asymptotes without ever touching them.",
    "u2_cycloid": "One turn of the circle lays 2 pi r on the base; the normal at any point passes "
                  "through the point of contact with the base line.",
    "u2_involute": "The string is always taut, so every tangent length grows by one eighth of the "
                   "circumference and the normal always touches the circle.",
    "u2_spiral": "One part out at every 30 degrees: the radius grows by R/12 at each ray, so the "
                 "pitch is the same on every turn.",
}


def ln(x1, y1, x2, y2, color=INK, w=1.0, dash=None):
    da = f' stroke-dasharray="{dash}"' if dash else ""
    return (f'<path d="M{x1:.1f} {y1:.1f}L{x2:.1f} {y2:.1f}" fill="none" stroke="{color}" '
            f'stroke-width="{w}" stroke-linecap="round"{da}/>')


def poly(points, color=INK, w=1.8, dash=None):
    da = f' stroke-dasharray="{dash}"' if dash else ""
    d = "M" + "L".join(f"{x:.1f} {y:.1f}" for x, y in points)
    return (f'<path d="{d}" fill="none" stroke="{color}" stroke-width="{w}" '
            f'stroke-linejoin="round" stroke-linecap="round"{da}/>')


def arrow(x1, y1, x2, y2, color=INK, w=1.0):
    ang = math.atan2(y2 - y1, x2 - x1)
    s = 5.0
    p1 = (x2 - s * math.cos(ang) + s * 0.32 * math.sin(ang), y2 - s * math.sin(ang) - s * 0.32 * math.cos(ang))
    p2 = (x2 - s * math.cos(ang) - s * 0.32 * math.sin(ang), y2 - s * math.sin(ang) + s * 0.32 * math.cos(ang))
    return (ln(x1, y1, x2, y2, color, w) +
            f'<path d="M{p1[0]:.1f} {p1[1]:.1f}L{x2:.1f} {y2:.1f}L{p2[0]:.1f} {p2[1]:.1f}Z" fill="{color}"/>')


def dot(x, y, color=RED, r=2.2):
    return f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r}" fill="{color}"/>'


def heading(t, sub=None):
    b = text(180, 21, t, 12.4, weight="bold", color=INK)
    if sub:
        b += text(180, 39, sub, 9.4, color=GREY)
    return b


def foot(y, *lines):
    return "".join(text(180, y + 13 * i, s, 8.8, color=GREY) for i, s in enumerate(lines))


# ------------------------------------------------------------------ 1. the three conics
def conic():
    b = heading("One ratio decides the curve", "e = distance from the focus / distance to the directrix")
    # ellipse
    cx, cy, a, bb = 62.0, 106.0, 42.0, 27.0
    pts = [(cx + a * math.cos(t), cy - bb * math.sin(t))
           for t in [i * math.pi / 36 for i in range(73)]]
    b += poly(pts, PURPLE, 2.0)
    b += ln(10, 66, 10, 146, GREEN, 0.9, "5 3")
    b += dot(cx - 0.6 * a, cy, RED)
    b += text(10, 60, "directrix", 6.4, anchor="start", color=GREEN)
    b += text(cx, 160, "e < 1", 8.2, color=PURPLE, weight="bold")
    b += text(cx, 172, "ellipse", 7.4, color=GREY)
    # parabola
    vx, vy = 148.0, cy
    pts = [(vx + (dy * dy) / 44.0, vy + dy) for dy in
           [-38 + 2 * i for i in range(39)]]
    b += poly(pts, BLUE, 2.0)
    b += ln(134, 66, 134, 146, GREEN, 0.9, "5 3")
    b += dot(vx + 10.5, vy, RED)
    b += text(180, 160, "e = 1", 8.2, color=BLUE, weight="bold")
    b += text(180, 172, "parabola", 7.4, color=GREY)
    # hyperbola
    hx, hy, ha, hb = 296.0, cy, 12.0, 10.0
    for sgn in (1, -1):
        pts = [(hx + sgn * ha * math.cosh(u), hy - hb * math.sinh(u))
               for u in [-1.6 + 0.05 * i for i in range(65)]]
        b += poly(pts, ORANGE, 2.0)
    b += ln(286, 66, 286, 146, GREEN, 0.9, "5 3")
    b += dot(hx + 15, hy, RED)
    b += text(298, 160, "e > 1", 8.2, color=ORANGE, weight="bold")
    b += text(298, 172, "hyperbola", 7.4, color=GREY)
    b += text(180, 190, "focus red, directrix green: the ratio of the two distances is e", 7.2, color=GREY)
    b += f'<rect x="8" y="200" width="344" height="24" rx="5" fill="#F4F6F8" stroke="{THIN}" stroke-width="0.9"/>'
    b += text(180, 215, "e < 1 ellipse   |   e = 1 parabola   |   e > 1 hyperbola", 7.8, color=INK)
    b += foot(238, "Given the focus and the directrix: distance from focus = e x distance to it.",
              "Given the axes, or the base and height: project, intersect and join.")
    return svg(360, 262, b)


# ------------------------------------------------------------------ 2. ellipse by concentric circles
def ellipse():
    b = heading("Every point is a projection", "major 100 mm, minor 60 mm")
    cx, cy, a, bb = 180.0, 158.0, 100.0, 60.0
    b += f'<circle cx="{cx}" cy="{cy}" r="{a}" fill="none" stroke="{THIN}" stroke-width="0.9"/>'
    b += f'<circle cx="{cx}" cy="{cy}" r="{bb}" fill="none" stroke="{THIN}" stroke-width="0.9" stroke-dasharray="4 3"/>'
    b += ln(cx - a - 8, cy, cx + a + 8, cy, THIN, 0.8, "1 3")
    b += ln(cx, cy - a - 8, cx, cy + a + 8, THIN, 0.8, "1 3")
    for k in range(12):
        t = math.radians(30 * k)
        b += ln(cx + a * math.cos(t), cy - a * math.sin(t),
                cx + bb * math.cos(t), cy - bb * math.sin(t), THIN, 0.7, "3 3")
    # elbow projections at four rays
    for deg in (30, 60, 120, 150):
        t = math.radians(deg)
        px = cx + a * math.cos(t)
        py = cy - bb * math.sin(t)
        b += ln(cx + a * math.cos(t), cy - a * math.sin(t), cx + a * math.cos(t), cy, BLUE, 0.8, "4 2")
        b += ln(cx, cy - bb * math.sin(t), cx + a * math.cos(t), cy - bb * math.sin(t), ORANGE, 0.8, "4 2")
        b += dot(px, py, RED, 2.4)
    pts = [(cx + a * math.cos(i * math.pi / 36), cy - bb * math.sin(i * math.pi / 36))
           for i in range(73)]
    b += poly(pts, PURPLE, 2.0)
    b += dot(cx + a * math.cos(math.radians(30)), cy - bb * math.sin(math.radians(30)), RED, 2.8)
    b += text(cx + 74, cy - 36, "P", 8.0, color=RED, weight="bold")
    b += text(cx + 8, cy - bb - 8, "r = 30", 7.0, anchor="start", color=GREY)
    b += text(cx + 8, cy - a - 8, "R = 50", 7.0, anchor="start", color=GREY)
    b += foot(272, "Blue: drop a vertical from the major circle. Orange: take a horizontal",
              "from the minor circle. Check: foci 80 mm apart, so e = 40 / 50 = 0.8.")
    return svg(360, 292, b)


# ------------------------------------------------------------------ 3. parabola
def parabola():
    b = heading("Height falls as the square of the distance", "base 100 mm, height 60 mm")
    bx, vy = 80.0, 110.0        # base left, vertex height (2 px per mm)
    base_y = 230.0
    x0, x1 = 80.0, 280.0
    cx = 180.0
    b += ln(x0 - 6, base_y, x1 + 6, base_y, THIN, 1.0)
    b += ln(cx, vy - 14, cx, base_y + 10, THIN, 0.8, "8 3 2 3")
    pts = []
    for i in range(81):
        x = x0 + (x1 - x0) * i / 80
        h = 120.0 * (1 - ((x - cx) / 100.0) ** 2)
        pts.append((x, base_y - h))
    b += poly(pts, BLUE, 2.0)
    for mm in (10, 20, 30, 40, 50):
        for sgn in (1, -1):
            x = cx + sgn * 2 * mm
            h = 120.0 * (1 - (mm / 50.0) ** 2)
            b += ln(x, base_y, x, base_y - h, THIN, 0.7, "3 3")
            b += dot(x, base_y - h, RED, 2.2)
    b += ln(cx - 50, base_y, cx - 50, base_y - 90, ORANGE, 0.9)
    b += text(cx - 56, base_y - 92, "45 at 25", 6.6, anchor="end", color=ORANGE)
    b += text(cx + 4, vy - 6, "V", 7.6, anchor="start", color=INK)
    b += text(x0 - 4, base_y + 12, "A", 7.4, anchor="end", color=INK)
    b += text(x1 + 4, base_y + 12, "B", 7.4, anchor="start", color=INK)
    # foci and directrix
    b += ln(x0 - 6, vy - 22, x1 + 6, vy - 22, GREEN, 0.9, "6 3")
    b += dot(cx, vy + 21, RED, 2.6)
    b += text(x1 + 2, vy - 26, "directrix", 6.6, anchor="start", color=GREEN)
    b += ln(cx + 16, vy + 24, cx + 30, vy + 34, THIN, 0.7)
    b += text(cx + 32, vy + 36, "a = 10.4", 6.6, anchor="start", color=RED)
    b += text(cx + 5, vy + 24, "F", 7.4, anchor="start", color=RED)
    b += foot(262, "h = r (1 - x squared / s squared): 57.6, 50.4, 38.4, 21.6, 0 mm at",
              "x = 10 to 50 mm. 4a = 41.7 mm is the latus rectum, the width at the focus.")
    return svg(360, 284, b)


# ------------------------------------------------------------------ 4. rectangular hyperbola
def hyperbola():
    b = heading("x times y is constant along the curve", "x y = 40 x 30 = 1200 mm squared")
    ox, oy = 180.0, 158.0
    b += ln(14, oy, 346, oy, THIN, 0.9)
    b += ln(ox, 62, ox, 268, THIN, 0.9)
    b += text(342, oy - 6, "asymptote", 6.6, anchor="end", color=GREY)
    b += text(ox + 6, 70, "asymptote", 6.6, anchor="start", color=GREY)
    q1 = [(ox + xv, oy - 1200.0 / xv) for xv in [14 + 1.2 * i for i in range(123)]]
    b += poly([(x, y) for x, y in q1 if 64 <= y <= 256], PURPLE, 2.0)
    q3 = [(ox - xv, oy + 1200.0 / xv) for xv in [14 + 1.2 * i for i in range(123)]]
    b += poly([(x, y) for x, y in q3 if 64 <= y <= 256], PURPLE, 2.0)
    for xv, yv in ((20, 60), (30, 40), (40, 30), (60, 20), (80, 15), (120, 10)):
        b += dot(ox + xv, oy - yv, RED, 2.2)
        b += dot(ox - xv, oy + yv, RED, 2.2)
    b += dot(ox + 40, oy - 30, RED, 3.0)
    b += text(ox + 44, oy - 34, "P (40, 30)", 7.0, anchor="start", color=RED, weight="bold")
    b += text(ox + 62, oy - 15, "60, 20", 6.4, anchor="start", color=GREY)
    b += text(ox + 82, oy - 10, "80, 15", 6.4, anchor="start", color=GREY)
    b += text(ox + 16, oy - 56, "20, 60", 6.4, anchor="end", color=GREY)
    b += text(ox - 44, oy + 40, "mirror branch", 6.6, anchor="end", color=PURPLE)
    b += f'<rect x="8" y="274" width="344" height="22" rx="5" fill="#F4F6F8" stroke="{THIN}" stroke-width="0.9"/>'
    b += text(180, 288, "x = 20 y = 60   |   x = 40 y = 30   |   x = 60 y = 20   |   x = 120 y = 10",
              7.0, color=INK)
    b += foot(314, "Set each pair off along the asymptotes and mark the crossing.",
              "The branches approach both asymptotes and never touch them.")
    return svg(360, 336, b)


# ------------------------------------------------------------------ 5. cycloid
def cycloid():
    b = heading("A point on a rolling circle", "r = 25 mm, base = 2 pi r = 157 mm")
    r = 38.0
    base_y = 214.0
    x0 = 44.0
    b += ln(x0 - 10, base_y, x0 + 2 * math.pi * r + 10, base_y, THIN, 1.0)
    pts = []
    for i in range(121):
        th = 2 * math.pi * i / 120
        pts.append((x0 + r * th - r * math.sin(th), base_y - r + r * math.cos(th)))
    b += poly(pts, BLUE, 2.0)
    for k in (0, 1, 2, 3, 4):
        th = k * math.pi / 2
        cxx = x0 + r * th
        b += f'<circle cx="{cxx:.1f}" cy="{base_y - r}" r="{r}" fill="none" stroke="{THIN}" stroke-width="0.8" stroke-dasharray="4 3"/>'
        px = cxx - r * math.sin(th)
        py = base_y - r + r * math.cos(th)
        b += dot(px, py, RED, 2.6)
        b += ln(cxx, base_y - r, px, py, ORANGE, 0.8, "3 2")
    # normal at 3/4 turn
    th = 1.5 * math.pi
    cxx = x0 + r * th
    px = cxx - r * math.sin(th)
    py = base_y - r + r * math.cos(th)
    b += ln(cxx, base_y, px, py, GREEN, 1.2)
    b += dot(cxx, base_y, GREEN, 2.4)
    b += text(cxx + 4, base_y + 12, "T", 7.2, anchor="start", color=GREEN, weight="bold")
    b += text(px + 4, py - 6, "P", 7.4, anchor="start", color=RED, weight="bold")
    b += text(x0 + 2 * math.pi * r - 6, base_y + 12, "157 mm", 7.0, anchor="end", color=GREY)
    b += text(x0 + r, base_y - 2 * r - 8, "2 r = 50", 7.0, color=GREY)
    b += foot(244, "Divide the circle and the base into the same twelve parts.",
              "The normal passes through the point of contact with the base line.")
    return svg(360, 266, b)


# ------------------------------------------------------------------ 6. involute
def involute():
    b = heading("A taut string unwinding", "r = 20 mm, one turn = 2 pi r = 125.7 mm")
    r = 22.0
    cx, cy = 116.0, 112.0
    b += f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{THIN}" stroke-width="1.0"/>'
    n = 8
    for k in range(n):
        t = 2 * math.pi * k / n
        px = cx + r * math.cos(t)
        py = cy - r * math.sin(t)
        ex = cx + r * (math.cos(t) + t * math.sin(t))
        ey = cy - r * (math.sin(t) - t * math.cos(t))
        b += ln(px, py, ex, ey, ORANGE, 0.8, "4 3")
        b += dot(ex, ey, RED, 2.2)
        b += dot(px, py, THIN, 1.6)
    pts = []
    for i in range(97):
        t = 2 * math.pi * i / 96
        pts.append((cx + r * (math.cos(t) + t * math.sin(t)),
                    cy - r * (math.sin(t) - t * math.cos(t))))
    b += poly(pts, BLUE, 2.0)
    b += text(cx + 44, cy + 34, "r = 20", 6.8, anchor="start", color=GREY)
    b += ln(cx + 42, cy + 30, cx + 14, cy + 16, THIN, 0.6)
    b += dot(cx + r, cy, GREEN, 2.6)
    b += text(cx + r + 4, cy - 8, "start", 6.6, anchor="start", color=GREEN)
    b += dot(cx + r, cy + 2 * math.pi * r, GREEN, 2.8)
    b += text(cx + r + 6, cy + 2 * math.pi * r + 3, "one turn", 6.6, anchor="start", color=GREEN)
    b += text(300, 120, "1/8 of 125.7", 6.8, anchor="end", color=ORANGE)
    b += text(300, 132, "= 15.7 mm per step", 6.8, anchor="end", color=ORANGE)
    b += ln(240, 140, 214, 164, THIN, 0.7)
    b += foot(278, "Tangent lengths grow 15.7 mm a step: 15.7, 31.4 ... 125.7 mm.",
              "The normal at any point is the tangent to the circle drawn from it.")
    return svg(360, 300, b)


# ------------------------------------------------------------------ 7. spiral
def spiral():
    b = heading("Outward at a steady rate while turning", "R = 50 mm, one turn, twelve rays")
    cx, cy = 180.0, 160.0
    R = 108.0
    b += f'<circle cx="{cx}" cy="{cy}" r="{R}" fill="none" stroke="{THIN}" stroke-width="0.9" stroke-dasharray="4 3"/>'
    for k in range(12):
        t = math.radians(30 * k)
        b += ln(cx, cy, cx + R * math.cos(t), cy - R * math.sin(t), THIN, 0.6, "3 4")
    pts = []
    for i in range(145):
        t = 2 * math.pi * i / 144
        rr = R * t / (2 * math.pi)
        pts.append((cx + rr * math.cos(t), cy - rr * math.sin(t)))
    b += poly(pts, PURPLE, 2.0)
    for k in range(1, 12):
        t = math.radians(30 * k)
        rr = R * k / 12
        b += dot(cx + rr * math.cos(t), cy - rr * math.sin(t), RED, 2.2)
    b += dot(cx, cy, INK, 2.2)
    b += text(cx + 4, cy - 6, "O", 7.2, anchor="start", color=INK)
    b += text(cx + R * 0.55, cy + 34, "r grows by 4.17 mm", 6.8, color=PURPLE)
    b += text(cx + R * 0.55, cy + 46, "every 30 degrees", 6.8, color=PURPLE)
    b += foot(288, "Divide the largest circle and one radius into the same twelve parts.",
              "Pitch = R / turns: a 50 mm one-turn spiral has a 50 mm pitch.")
    return svg(360, 310, b)


DIAGRAMS = {
    "u2_conic": conic,
    "u2_ellipse": ellipse,
    "u2_parabola": parabola,
    "u2_hyperbola": hyperbola,
    "u2_cycloid": cycloid,
    "u2_involute": involute,
    "u2_spiral": spiral,
}
