"""Seven figures for Engineering Graphics (DI01000111) Unit 3 - points and lines.

The XY reference line is drawn once per figure (or once per panel); everything above it is an
elevation, everything below it a plan. Coordinates are computed from the millimetre data, so a
student can measure the figure and find the same numbers as in the notes.
"""
import math

from flowchart_lib import svg, text
from diagrams_DI01000111_lib import (INK, GREY, THIN, BLUE, GREEN, ORANGE, RED, PURPLE, TEAL,
                                     ln, poly, arrow, dot, ring, heading, foot, xy, tag, dash_box)

TITLES = {
    "u3_quadrants": "Four quadrants, one XY line",
    "u3_points": "Six points and what their projectors say",
    "u3_line_basic": "Three easy positions of a line",
    "u3_line_hp": "Inclined to HP, parallel to VP",
    "u3_line_vp": "Inclined to VP, parallel to HP",
    "u3_line_both": "Line inclined to both planes",
    "u3_traces": "True length, inclinations and traces",
}

CAPTIONS = {
    "u3_quadrants": "The elevation goes above XY and the plan below it; whether the point is above "
                    "HP or in front of VP only decides how far and on which side.",
    "u3_points": "A point and both its views always sit on one thin projector drawn square to XY - "
                 "that single line is the whole grammar of this unit.",
    "u3_line_basic": "Parallel to both planes: two true-length views. Perpendicular to HP: the "
                     "elevation collapses to a point. Parallel to HP: the plan shows the true length.",
    "u3_line_hp": "The elevation carries the true length and the angle to XY; the plan comes down "
                  "on the projectors, parallel to XY and shortened to L cos of the angle.",
    "u3_line_vp": "The mirror image of the previous figure: now the plan carries the true length "
                  "and the elevation is the shortened view.",
    "u3_line_both": "Assume the line parallel to VP first, then swing the plan round to the second "
                    "angle - the elevation finishes on the locus of the first attempt.",
    "u3_traces": "The traces are found where the produced views meet XY and drop back onto the "
                 "other view: the plan gives the VT, the elevation gives the HT.",
}


def quadrants():
    b = heading("Where the point is decides where its views fall")
    cells = [("1st quadrant", "above HP, in front of VP", True, True),
             ("2nd quadrant", "above HP, behind VP", True, False),
             ("3rd quadrant", "below HP, behind VP", False, False),
             ("4th quadrant", "below HP, in front of VP", False, True)]
    for k, (name, sub, above, front) in enumerate(cells):
        x0 = 8 + (k % 2) * 174
        y0 = 56 + (k // 2) * 132
        b += f'<rect x="{x0}" y="{y0}" width="168" height="124" rx="6" fill="#FBFCFD" stroke="{THIN}" stroke-width="0.9"/>'
        b += text(x0 + 84, y0 + 16, name, 8.6, weight="bold", color=INK)
        b += text(x0 + 84, y0 + 27, sub, 7.0, color=GREY)
        yline = y0 + 68
        b += ln(x0 + 12, yline, x0 + 156, yline, INK, 1.0)
        px = x0 + 96
        ey = yline - 32 if above else yline + 32
        py = yline - 24 if front else yline + 24
        b += ln(px, ey, px, py, THIN, 0.7, "3 3")
        b += ln(px, yline, px, ey, THIN, 0.6, "1 3")
        b += ln(px, yline, px, py, THIN, 0.6, "1 3")
        b += ring(px, ey, RED, 2.8)
        b += dot(px, py, BLUE, 2.4)
        b += tag(px, ey, "a'", RED, dx=6, dy=-2, size=7.0)
        b += tag(px, py, "a", BLUE, dx=6, dy=10, size=7.0)
        b += text(x0 + 14, yline - 6, "VP", 6.4, anchor="start", color=GREY)
        b += text(x0 + 14, yline + 12, "HP", 6.4, anchor="start", color=GREY)
    b += foot(318, "Elevation above XY: the point is above HP.",
              "Plan below XY: the point is in front of VP.")
    return svg(360, 340, b)


def points():
    b = heading("Six points, six pairs of views", "one projector per point, square to XY")
    s = 1.2
    yl = 168.0
    b += xy(yl)
    data = [("A", 25, 30, RED), ("B", -20, 35, ORANGE), ("C", 30, -25, PURPLE),
            ("D", -15, -40, TEAL), ("E", 0, 25, BLUE), ("F", 20, 0, GREEN)]
    for k, (name, above, front, col) in enumerate(data):
        x = 44 + k * 52
        ey = yl - above * s
        py = yl + front * s
        b += ln(x, min(ey, py) - 8, x, max(ey, py) + 8, THIN, 0.7, "4 3")
        b += ring(x, ey, col, 2.8)
        b += dot(x, py, col, 2.4)
        b += tag(x, ey, f"{name}'", col, dx=7, dy=-4, size=7.4, weight="bold")
        b += tag(x, py, name.lower(), col, dx=7, dy=10, size=7.4, weight="bold")
    b += dash_box(8, 250, 344, 44)
    b += text(180, 266, "A 25 above HP, 30 in front   B 20 below HP, 35 in front", 7.4)
    b += text(180, 280, "C 30 above HP, 25 behind   D 15 below HP, 40 behind   E on HP   F on VP", 7.4)
    b += foot(312, "A point on HP has its elevation on XY; a point on VP has its plan on XY.")
    return svg(360, 330, b)


def line_basic():
    b = heading("The three positions worth memorising")
    panels = [(0.0, "parallel to both"), (120.0, "perpendicular to HP"), (240.0, "parallel to HP")]
    for x0, name in panels:
        b += f'<rect x="{x0 + 4}" y="52" width="112" height="176" rx="6" fill="#FBFCFD" stroke="{THIN}" stroke-width="0.9"/>'
        b += text(x0 + 60, 66, name, 7.6, weight="bold", color=INK)
        b += ln(x0 + 10, 140, x0 + 110, 140, INK, 0.9)
        b += text(x0 + 108, 136, "XY", 6.0, anchor="end", color=GREY)
    # (1) parallel to both planes
    x0 = 4.0
    b += ln(x0 + 22, 122, x0 + 67, 122, BLUE, 1.8)
    b += ln(x0 + 22, 158, x0 + 67, 158, BLUE, 1.8)
    b += ln(x0 + 22, 118, x0 + 22, 162, THIN, 0.6, "3 3")
    b += ln(x0 + 67, 118, x0 + 67, 162, THIN, 0.6, "3 3")
    b += ring(x0 + 22, 122, RED, 2.4)
    b += ring(x0 + 67, 122, RED, 2.4)
    b += dot(x0 + 22, 158, BLUE, 2.2)
    b += dot(x0 + 67, 158, BLUE, 2.2)
    b += text(x0 + 60, 196, "TL 60 in both views", 6.6, color=GREY)
    b += text(x0 + 60, 208, "25 above HP, 30 in front", 6.4, color=GREY)
    # (2) perpendicular to HP
    x0 = 124.0
    b += dot(x0 + 44, 122, RED, 3.0)
    b += text(x0 + 44, 116, "a' and b'", 6.4, anchor="middle", color=RED)
    b += ln(x0 + 44, 152, x0 + 44, 186, BLUE, 1.8)
    b += ln(x0 + 44, 140, x0 + 44, 152, THIN, 0.6, "3 3")
    b += ring(x0 + 44, 152, BLUE, 2.2)
    b += dot(x0 + 44, 186, BLUE, 2.4)
    b += text(x0 + 44, 200, "plan shows TL", 6.6, anchor="middle", color=GREY)
    b += text(x0 + 44, 212, "elevation is a point", 6.4, anchor="middle", color=GREY)
    # (3) parallel to HP, inclined to VP
    x0 = 244.0
    ex = x0 + 26
    px, py = ex + 37.3, 122
    qx, qy = ex + 37.3, 150 + 31.3
    b += ln(ex, 122, px, py, BLUE, 1.8)
    b += ln(ex, 150, qx, qy, BLUE, 1.8)
    b += ln(ex, 122, ex, 150, THIN, 0.6, "3 3")
    b += ln(qx, qy, qx, 150, THIN, 0.6, "3 3")
    b += ring(ex, 122, RED, 2.4)
    b += dot(ex, 150, BLUE, 2.4)
    b += text(x0 + 60, 200, "plan TL at 40 deg", 6.6, anchor="middle", color=GREY)
    b += text(x0 + 60, 212, "elevation 65 cos 40 = 49.8", 6.4, anchor="middle", color=GREY)
    b += foot(252, "An elevation is the view from the front, a plan from above;",
              "vertical projectors keep the two views tied together.")
    return svg(360, 280, b)


def line_hp():
    b = heading("Inclined to HP, parallel to VP", "AB 70 mm at 30 deg - the elevation is true")
    s = 1.2
    yl = 176.0
    x0 = 96.0
    b += xy(yl)
    ay = yl - 20 * s
    bx, by = x0 + 70 * s * math.cos(math.radians(30)), ay - 70 * s * math.sin(math.radians(30))
    py = yl + 25 * s
    qx = x0 + 70 * s * math.cos(math.radians(30))
    b += ln(x0, ay, bx, by, PURPLE, 2.0)
    b += ln(x0, py, qx, py, BLUE, 2.0)
    b += ln(x0, ay, x0, py, THIN, 0.7, "5 3")
    b += ln(bx, by, qx, py, THIN, 0.7, "5 3")
    b += ln(x0, ay, qx, ay, THIN, 0.6, "2 4")
    b += ln(x0, py, x0, py, THIN, 0.6, "1 3")
    b += ln(bx, py, qx, py, THIN, 0.6, "1 3")
    b += ring(x0, ay, RED, 2.6)
    b += ring(bx, by, RED, 2.6)
    b += dot(x0, py, BLUE, 2.4)
    b += dot(qx, py, BLUE, 2.4)
    b += tag(x0, ay, "a'", RED, dx=-8, dy=-4, anchor="end")
    b += tag(bx, by, "b'", RED, dx=2, dy=-2)
    b += tag(x0, py, "a", BLUE, dx=-8, dy=10, anchor="end")
    b += tag(qx, py, "b", BLUE, dx=3, dy=10)
    b += text(x0 + 24, ay - 8, "TL 70 at 30 deg", 6.8, anchor="start", color=PURPLE)
    b += text(x0 + 30, py + 26, "plan 70 cos 30 = 60.6, parallel to XY", 6.8, anchor="start", color=BLUE)
    b += text(x0 - 10, ay + 2, "20 above", 6.4, anchor="end", color=GREY)
    b += text(x0 - 10, py + 12, "25 in front", 6.4, anchor="end", color=GREY)
    b += foot(244, "Parallel to VP, so no depth is lost: the elevation is the true length.",
              "The plan is the elevation dropped down, shortened to L cos 30.")
    return svg(360, 268, b)


def line_vp():
    b = heading("Inclined to VP, parallel to HP", "AB 65 mm at 40 deg - the plan is true")
    s = 1.2
    yl = 176.0
    x0 = 96.0
    b += xy(yl)
    py = yl + 25 * s
    qx = x0 + 65 * s * math.cos(math.radians(40))
    qy = py + 65 * s * math.sin(math.radians(40))
    ay = yl - 20 * s
    b += ln(x0, ay, qx, ay, PURPLE, 2.0)
    b += ln(x0, py, qx, qy, BLUE, 2.0)
    b += ln(x0, ay, x0, py, THIN, 0.7, "5 3")
    b += ln(qx, ay, qx, qy, THIN, 0.7, "5 3")
    b += ring(x0, ay, RED, 2.6)
    b += ring(qx, ay, RED, 2.6)
    b += dot(x0, py, BLUE, 2.4)
    b += dot(qx, qy, BLUE, 2.4)
    b += tag(x0, ay, "a'", RED, dx=-8, dy=-4, anchor="end")
    b += tag(qx, ay, "b'", RED, dx=3, dy=-4)
    b += tag(x0, py, "a", BLUE, dx=-8, dy=10, anchor="end")
    b += tag(qx, qy, "b", BLUE, dx=3, dy=10)
    b += text(x0 + 34, py + 12, "TL 65 at 40 deg", 6.8, anchor="start", color=BLUE)
    b += text(x0 + 8, ay - 10, "elevation 65 cos 40 = 49.8", 6.8, anchor="start", color=PURPLE)
    b += foot(276, "Every point keeps the same height, so the elevation is parallel to XY.",
              "The plan carries the true length and the 40 deg.")
    return svg(360, 300, b)


def line_both():
    b = heading("Inclined to both planes: two rotations", "AB 80 mm, 35 deg to HP, plan at 45 deg")
    s = 1.0
    yl = 172.0
    x0 = 122.0
    b += xy(yl)
    ay = yl - 20 * s
    by = yl + 25 * s
    b1x = x0 + 80 * s * math.cos(math.radians(35))
    b1y = ay - 80 * s * math.sin(math.radians(35))
    b2x = x0 + 65.5 * s * math.cos(math.radians(45))
    b2y = by + 65.5 * s * math.sin(math.radians(45))
    # stage 1: assume parallel to VP
    b += ln(x0 - 8, b1y, x0 + 96, b1y, THIN, 0.7, "4 3")
    b += ln(x0, ay, b1x, b1y, PURPLE, 1.3, "5 3")
    b += ln(x0, by, b1x, by, PURPLE, 1.3, "5 3")
    b += f'<path d="M{b1x:.1f} {by:.1f}A65.5 65.5 0 0 1 {b2x:.1f} {b2y:.1f}" fill="none" stroke="{GREEN}" stroke-width="0.9" stroke-dasharray="4 3"/>'
    # stage 2: the final views
    b += ln(x0, ay, b2x, b1y, RED, 2.0)
    b += ln(x0, by, b2x, b2y, BLUE, 2.0)
    b += ln(b2x, b2y, b2x, b1y, THIN, 0.7, "3 3")
    b += ln(x0, ay, x0, by, THIN, 0.7, "5 3")
    b += ring(x0, ay, RED, 2.6)
    b += ring(x0, by, BLUE, 2.6)
    b += dot(b1x, b1y, PURPLE, 2.2)
    b += dot(b1x, by, PURPLE, 2.2)
    b += dot(b2x, b1y, RED, 2.4)
    b += dot(b2x, b2y, BLUE, 2.4)
    b += tag(x0, ay, "a'", RED, dx=-8, dy=-4, anchor="end")
    b += tag(x0, by, "a", BLUE, dx=-8, dy=10, anchor="end")
    b += tag(b1x, b1y, "b1'", PURPLE, dx=4, dy=-4)
    b += tag(b1x, by, "b1", PURPLE, dx=6, dy=10)
    b += tag(b2x, b1y, "b'", RED, dx=4, dy=-6)
    b += tag(b2x, b2y, "b", BLUE, dx=6, dy=10)
    b += text(x0 + 20, ay - 12, "TL 80 at 35 deg", 6.6, anchor="start", color=PURPLE)
    b += text(b2x + 6, by + 20, "plan 65.5", 6.6, anchor="start", color=BLUE)
    b += text(x0 + 14, by + 44, "45 deg", 6.6, anchor="start", color=GREEN)
    b += text(x0 - 6, b1y - 6, "locus of b'", 6.4, anchor="start", color=GREY)
    b += text(x0 - 6, by - 5, "locus of b", 6.4, anchor="start", color=GREY)
    b += dash_box(8, 274, 344, 40)
    b += text(180, 289, "plan 65.5 at 45 deg   |   elevation 65.2   |   b1' stands 45.9 above a'",
              7.4)
    b += text(180, 303, "the arc keeps the plan length, the locus keeps the height", 7.2,
              color=GREY)
    b += foot(324, "Stage 1 assumes the line parallel to VP; stage 2 swings the plan",
              "about a, and that swing cannot change any height.")
    return svg(360, 352, b)


def traces():
    b = heading("From two views to true length and traces", "plan 45 at 30 deg, elevation 50")
    s = 1.2
    yl = 158.0
    x0 = 150.0
    b += xy(yl)
    ay = yl - 20 * s
    by = yl + 25 * s
    dx = 45 * s * math.cos(math.radians(30))
    b1x, b1y = x0 + dx, ay - 50 * s * math.sin(math.radians(38.8))
    b2x, b2y = x0 + dx, by + 45 * s * math.sin(math.radians(30))
    b += ln(x0, ay, b1x, b1y, RED, 1.9)
    b += ln(x0, by, b2x, b2y, BLUE, 1.9)
    hx = x0 - (20 * s) / math.tan(math.radians(38.8))
    vx = x0 - (25 * s) / math.tan(math.radians(30))
    b += ln(x0, ay, hx, yl, RED, 0.9, "4 3")
    b += ln(x0, by, vx, yl, BLUE, 0.9, "4 3")
    htx = hx
    hty = by - (x0 - hx) * math.tan(math.radians(30))
    b += ln(htx, yl, htx, hty, THIN, 0.7, "3 3")
    vty = ay + (x0 - vx) * math.tan(math.radians(38.8))
    b += ln(vx, yl, vx, vty, THIN, 0.7, "3 3")
    b += ln(x0, ay, x0, by, THIN, 0.7, "5 3")
    b += dot(htx, hty, TEAL, 3.0)
    b += dot(vx, vty, TEAL, 3.0)
    b += ring(x0, ay, RED, 2.6)
    b += ring(b1x, b1y, RED, 2.6)
    b += dot(x0, by, BLUE, 2.4)
    b += dot(b2x, b2y, BLUE, 2.4)
    b += tag(x0, ay, "a'", RED, dx=-8, dy=-4, anchor="end")
    b += tag(b1x, b1y, "b'", RED, dx=3, dy=-4)
    b += tag(x0, by, "a", BLUE, dx=-8, dy=10, anchor="end")
    b += tag(b2x, b2y, "b", BLUE, dx=3, dy=10)
    b += tag(htx, hty, "HT", TEAL, dx=-4, dy=12, anchor="end")
    b += tag(vx, vty, "VT", TEAL, dx=-4, dy=-6, anchor="end")
    b += text(hx, yl - 6, "h'", 6.6, anchor="middle", color=RED)
    b += text(vx, yl + 12, "v", 6.6, anchor="middle", color=BLUE)
    b += text(b2x - 22, b2y + 20, "TL 54.8", 6.6, anchor="end", color=TEAL)
    b += foot(272, "Plan up to XY, then up again to the VT.",
              "Elevation down to XY, then down again to the HT.",
              "Parallel to HP: no HT. Parallel to VP: no VT.")
    return svg(360, 314, b)


DIAGRAMS = {
    "u3_quadrants": quadrants,
    "u3_points": points,
    "u3_line_basic": line_basic,
    "u3_line_hp": line_hp,
    "u3_line_vp": line_vp,
    "u3_line_both": line_both,
    "u3_traces": traces,
}
