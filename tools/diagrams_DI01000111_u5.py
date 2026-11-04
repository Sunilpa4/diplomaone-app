"""Six figures for Engineering Graphics (DI01000111) Unit 5 - orthographic projections.

The object is given as a pictorial (isometric) sketch and the three views are built from it in first
angle: the top view below the front view and the side view to its right.
"""
import math

from flowchart_lib import svg, text
from diagrams_DI01000111_lib import (INK, GREY, THIN, BLUE, GREEN, ORANGE, RED, PURPLE, TEAL,
                                     ln, poly, arrow, dot, ring, heading, foot, xy, tag, dash_box)

TITLES = {
    "u5_layout": "First angle: where each view goes",
    "u5_stepped": "A stepped block and its three views",
    "u5_cylinder": "A cylinder and its three views",
    "u5_hidden": "Hidden edges: the hole you cannot see",
    "u5_missing": "Two views given, the third to draw",
    "u5_freehand": "Free-hand sketches you must be able to make",
}

CAPTIONS = {
    "u5_layout": "In first angle the object sits between you and the paper, so the top view lands "
                 "below the front view and the side view to its right.",
    "u5_stepped": "Same height in the front and the side view, same width in the front and the top, "
                  "same depth in the top and the side - that is the whole grammar.",
    "u5_cylinder": "A cylinder gives two rectangles and one circle; the centre line in both "
                   "rectangles marks the axis.",
    "u5_hidden": "The hole is invisible from the front and the side, so it is drawn as a dashed "
                 "outline there and as a solid circle only in the top view.",
    "u5_missing": "Build the missing view from two rules: project every corner, and repeat each "
                  "height and each depth that the given views already show.",
    "u5_freehand": "Six shapes, six habits: box first, then diagonals, then the curve - the same "
                   "construction you use with instruments, only faster.",
}


def iso(ox, oy, s, x, y, z):
    """Isometric projection: x recedes to the right, y to the left, z stands up."""
    c = math.cos(math.radians(30))
    return (ox + (x - y) * c * s, oy + (x + y) * 0.5 * s - z * s)


def layout():
    b = heading("Where each view goes in first angle")
    fx, fy, fw, fh = 60.0, 74.0, 96.0, 58.0
    b += f'<rect x="{fx}" y="{fy}" width="{fw}" height="{fh}" fill="{BLUE}" fill-opacity="0.12" stroke="{BLUE}" stroke-width="1.8"/>'
    b += text(fx + fw / 2, fy + fh / 2 + 3, "FRONT", 8.4, weight="bold", color=BLUE)
    b += text(fx + fw / 2, fy + fh / 2 + 15, "elevation", 6.6, color=GREY)
    tx, ty = fx, fy + fh + 26
    b += f'<rect x="{tx}" y="{ty}" width="{fw}" height="46" fill="{PURPLE}" fill-opacity="0.12" stroke="{PURPLE}" stroke-width="1.8"/>'
    b += text(tx + fw / 2, ty + 27, "TOP  (plan)", 8.0, weight="bold", color=PURPLE)
    sx = fx + fw + 26
    b += f'<rect x="{sx}" y="{fy}" width="52" height="{fh}" fill="{GREEN}" fill-opacity="0.12" stroke="{GREEN}" stroke-width="1.8"/>'
    b += text(sx + 26, fy + fh / 2 - 2, "SIDE", 8.0, weight="bold", color=GREEN)
    b += text(sx + 26, fy + fh / 2 + 10, "from the left", 6.4, color=GREY)
    b += arrow(fx + fw / 2, fy + fh + 4, fx + fw / 2, ty - 4, PURPLE, 1.1)
    b += arrow(fx + fw + 4, fy + fh / 2, sx - 4, fy + fh / 2, GREEN, 1.1)
    b += text(fx + fw / 2 + 6, fy + fh + 16, "swings down", 6.4, anchor="start", color=PURPLE)
    b += text(fx + fw + 12, fy + fh / 2 - 6, "turns", 6.2, anchor="start", color=GREEN)
    b += text(180, 246, "The side view is placed on the right, the top view below: no view ever", 8.0,
              color=GREY)
    b += text(180, 259, "overlaps another, and every corner lines up on a projector.", 8.0, color=GREY)
    b += dash_box(8, 272, 344, 34)
    b += text(180, 287, "First angle: view placed beyond the object.  Third angle: view placed", 7.2)
    b += text(180, 299, "between the observer and the object, so the top view goes above.", 7.2)
    return svg(360, 314, b)


def stepped():
    b = heading("One block, three views", "base 60 x 40 x 15, upright 20 x 40 x 25")
    s = 1.0
    ox, oy = 92.0, 84.0
    P = lambda x, y, z: iso(ox, oy, s, x, y, z)
    prof = [(0, 0), (60, 0), (60, 15), (20, 15), (20, 40), (0, 40)]
    # the L profile at the front face, then the same profile carried back
    b += poly([P(x, 0, z) for x, z in prof], BLUE, 1.8, close=True)
    b += ln(*P(60, 0, 0)[:2], *P(60, 40, 0)[:2], BLUE, 1.5)
    b += ln(*P(60, 0, 15)[:2], *P(60, 40, 15)[:2], BLUE, 1.5)
    b += ln(*P(60, 40, 0)[:2], *P(60, 40, 15)[:2], BLUE, 1.5)
    b += ln(*P(20, 0, 15)[:2], *P(20, 40, 15)[:2], RED, 1.5)
    b += ln(*P(20, 0, 40)[:2], *P(20, 40, 40)[:2], RED, 1.5)
    b += ln(*P(0, 0, 40)[:2], *P(0, 40, 40)[:2], RED, 1.5)
    b += ln(*P(20, 40, 40)[:2], *P(0, 40, 40)[:2], RED, 1.5)
    b += ln(*P(20, 40, 40)[:2], *P(20, 40, 15)[:2], RED, 1.5)
    b += ln(*P(20, 40, 15)[:2], *P(60, 40, 15)[:2], BLUE, 1.5)
    b += text(ox - 22, oy + 78, "pictorial view", 7.0, color=GREY)
    # the three views
    fx, fy = 214.0, 66.0
    b += f'<path d="M{fx} {fy+40}L{fx} {fy+15}L{fx+20} {fy+15}L{fx+20} {fy}L{fx+60} {fy}L{fx+60} {fy+40}Z" fill="none" stroke="{BLUE}" stroke-width="1.7"/>'
    b += text(fx + 30, fy + 52, "FRONT", 7.0, anchor="middle", color=GREY)
    ty = fy + 62
    b += f'<rect x="{fx}" y="{ty}" width="60" height="40" fill="none" stroke="{PURPLE}" stroke-width="1.7"/>'
    b += ln(fx + 20, ty, fx + 20, ty + 40, PURPLE, 1.2)
    b += text(fx + 30, ty + 52, "TOP", 7.0, anchor="middle", color=GREY)
    sx = fx + 74
    b += f'<rect x="{sx}" y="{fy}" width="40" height="40" fill="none" stroke="{GREEN}" stroke-width="1.7"/>'
    b += ln(sx, fy + 25, sx + 40, fy + 25, GREEN, 1.0, "5 3")
    b += text(sx + 20, fy + 52, "SIDE", 7.0, anchor="middle", color=GREY)
    for dy in (0, 15, 40):
        b += ln(fx + 60, fy + dy, sx, fy + dy, THIN, 0.6, "3 4")
    b += ln(fx, fy + 40, fx, ty, THIN, 0.6, "3 4")
    b += ln(fx + 60, fy + 40, fx + 60, ty, THIN, 0.6, "3 4")
    b += ln(fx + 20, fy + 15, fx + 20, ty, THIN, 0.6, "3 4")
    b += text(fx + 30, fy + 76, "60", 6.4, anchor="middle", color=GREY)
    b += text(fx + 64, ty + 22, "40", 6.4, anchor="start", color=GREY)
    b += text(sx + 20, fy + 36, "40", 6.4, anchor="middle", color=GREY)
    b += foot(300, "Front and side share the height; front and top share the width;",
              "top and side share the depth. The dashed line in the side view is a hidden edge.")
    return svg(360, 326, b)


def cylinder():
    b = heading("Revolved shapes: two rectangles and a circle", "diameter 40 mm, height 50 mm")
    s = 1.0
    ox, oy = 96.0, 108.0
    rx = 20 * s
    ry = rx * 0.5
    top = oy - 50 * s
    b += f'<ellipse cx="{ox}" cy="{top}" rx="{rx:.1f}" ry="{ry:.1f}" fill="none" stroke="{BLUE}" stroke-width="1.6"/>'
    b += ln(ox - rx, top, ox - rx, oy, BLUE, 1.6)
    b += ln(ox + rx, top, ox + rx, oy, BLUE, 1.6)
    b += f'<path d="M{ox-rx:.1f} {oy:.1f}A{rx:.1f} {ry:.1f} 0 0 0 {ox+rx:.1f} {oy:.1f}" fill="none" stroke="{BLUE}" stroke-width="1.6"/>'
    b += ln(ox, top, ox, oy + ry, THIN, 0.6, "4 3")
    b += text(ox + rx + 6, top + 8, "40", 6.4, anchor="start", color=GREY)
    b += text(ox + 4, top + 30, "50", 6.4, anchor="start", color=GREY)
    b += text(ox, oy + ry + 14, "pictorial view", 7.0, color=GREY)
    fx, fy = 216.0, 74.0
    b += f'<rect x="{fx}" y="{fy}" width="40" height="50" fill="none" stroke="{BLUE}" stroke-width="1.6"/>'
    b += ln(fx, fy + 25, fx + 40, fy + 25, THIN, 0.7, "6 3")
    b += text(fx + 20, fy + 60, "FRONT", 7.0, anchor="middle", color=GREY)
    ty = fy + 76
    b += f'<circle cx="{fx+20}" cy="{ty+20}" r="20" fill="none" stroke="{PURPLE}" stroke-width="1.6"/>'
    b += ln(fx - 6, ty + 20, fx + 46, ty + 20, THIN, 0.6, "6 3")
    b += ln(fx + 20, ty - 6, fx + 20, ty + 46, THIN, 0.6, "6 3")
    b += text(fx + 20, ty + 46, "TOP", 7.0, anchor="middle", color=GREY)
    sx = fx + 54
    b += f'<rect x="{sx}" y="{fy}" width="40" height="50" fill="none" stroke="{GREEN}" stroke-width="1.6"/>'
    b += ln(sx, fy + 25, sx + 40, fy + 25, THIN, 0.7, "6 3")
    b += text(sx + 20, fy + 60, "SIDE", 7.0, anchor="middle", color=GREY)
    b += foot(300, "A circular edge seen square-on is a circle, seen edge-on a line, and seen at an",
              "angle an ellipse - which is why the top view is the only place the circle appears.")
    return svg(360, 322, b)


def hidden():
    b = heading("A hole is drawn where it can be seen", "plate 60 x 40 x 15, hole 20 dia")
    fx, fy, fw, fh = 40.0, 70.0, 60.0, 40.0
    b += f'<rect x="{fx}" y="{fy}" width="{fw}" height="{fh}" fill="none" stroke="{BLUE}" stroke-width="1.7"/>'
    b += ln(fx + 20, fy + 4, fx + 20, fy + fh - 4, RED, 1.2, "5 3")
    b += ln(fx + 40, fy + 4, fx + 40, fy + fh - 4, RED, 1.2, "5 3")
    b += text(fx + fw / 2, fy + fh + 12, "FRONT", 7.0, anchor="middle", color=GREY)
    ty = fy + fh + 22
    b += f'<rect x="{fx}" y="{ty}" width="{fw}" height="44" fill="none" stroke="{PURPLE}" stroke-width="1.7"/>'
    b += f'<circle cx="{fx+30}" cy="{ty+22}" r="20" fill="none" stroke="{RED}" stroke-width="1.2"/>'
    b += ln(fx + 22, ty + 22, fx + 38, ty + 22, THIN, 0.6, "6 3")
    b += ln(fx + 30, ty + 14, fx + 30, ty + 30, THIN, 0.6, "6 3")
    b += text(fx + fw / 2, ty + 56, "TOP", 7.0, anchor="middle", color=GREY)
    sx = fx + fw + 30
    b += f'<rect x="{sx}" y="{fy}" width="44" height="{fh}" fill="none" stroke="{GREEN}" stroke-width="1.7"/>'
    b += ln(sx + 12, fy + 4, sx + 12, fy + fh - 4, RED, 1.2, "5 3")
    b += ln(sx + 32, fy + 4, sx + 32, fy + fh - 4, RED, 1.2, "5 3")
    b += text(sx + 22, fy + fh + 12, "SIDE", 7.0, anchor="middle", color=GREY)
    b += text(sx + 22, fy + fh + 24, "from the left", 6.2, anchor="middle", color=GREY)
    b += dash_box(8, 232, 344, 46)
    b += text(180, 248, "Solid line: an edge you can see. Dashed line: an edge hidden behind", 7.4)
    b += text(180, 262, "material. Centre line: the axis of a hole or a cylinder.", 7.4)
    b += text(180, 274, "Never draw the hole solid in a view where the material hides it.", 7.2,
              color=GREY)
    b += foot(300, "The hole is 20 mm across in every view and its position is repeated exactly,",
              "because the three views are three looks at one object.")
    return svg(360, 322, b)


def missing():
    b = heading("Front and top given: build the side view", "an L block, 60 x 40 x 40")
    fx, fy = 52.0, 66.0
    b += f'<path d="M{fx} {fy+40}L{fx} {fy+25}L{fx+20} {fy+25}L{fx+20} {fy}L{fx+60} {fy}L{fx+60} {fy+40}Z" fill="none" stroke="{BLUE}" stroke-width="1.7"/>'
    b += text(fx + 30, fy + 54, "FRONT (given)", 6.8, anchor="middle", color=GREY)
    ty = fy + 64
    b += f'<rect x="{fx}" y="{ty}" width="60" height="40" fill="none" stroke="{PURPLE}" stroke-width="1.7"/>'
    b += ln(fx + 20, ty, fx + 20, ty + 40, PURPLE, 1.2)
    b += text(fx + 30, ty + 54, "TOP (given)", 6.8, anchor="middle", color=GREY)
    sx = fx + 76
    b += f'<rect x="{sx}" y="{fy}" width="40" height="40" fill="none" stroke="{GREEN}" stroke-width="1.6" stroke-dasharray="6 4"/>'
    b += ln(sx, fy + 25, sx + 40, fy + 25, GREEN, 1.0, "5 3")
    b += text(sx + 20, fy + 54, "SIDE (to draw)", 6.8, anchor="middle", color=GREEN)
    for dy in (0, 25, 40):
        b += ln(fx + 60, fy + dy, sx, fy + dy, THIN, 0.7, "3 4")
    b += ln(fx, fy + 40, fx, ty, THIN, 0.7, "3 4")
    b += ln(fx + 60, fy + 40, fx + 60, ty, THIN, 0.7, "3 4")
    b += ln(fx, ty + 40, fx, ty + 70, THIN, 0.7, "3 4")
    b += ln(fx + 60, ty + 40, fx + 60, ty + 70, THIN, 0.7, "3 4")
    b += dash_box(8, 246, 344, 34)
    b += text(180, 261, "Width from the front view, height from the front view, depth from", 7.4)
    b += text(180, 274, "the top view - the side view is the depth by the height.", 7.4)
    b += foot(316, "Project each corner across from the front view and carry each depth round",
              "from the top view; the hidden edge of the step becomes dashed.")
    return svg(360, 340, b)


def freehand():
    b = heading("Six shapes, drawn free-hand in one minute")
    cells = [("square", 0, 0), ("triangle", 1, 0), ("circle", 2, 0),
             ("semicircle", 0, 1), ("hexagon", 1, 1), ("pentagon", 2, 1)]
    for name, cx_, cy_ in cells:
        x0 = 10 + cx_ * 116
        y0 = 58 + cy_ * 116
        b += f'<rect x="{x0}" y="{y0}" width="106" height="106" rx="6" fill="#FBFCFD" stroke="{THIN}" stroke-width="0.9"/>'
        b += text(x0 + 53, y0 + 14, name, 7.4, weight="bold", color=INK)
        cxx, cyy = x0 + 53, y0 + 60
        if name == "square":
            b += f'<rect x="{cxx-26}" y="{cyy-26}" width="52" height="52" fill="none" stroke="{BLUE}" stroke-width="1.8"/>'
            b += ln(cxx - 34, cyy - 34, cxx + 34, cyy + 34, THIN, 0.6, "3 3")
            b += ln(cxx + 34, cyy - 34, cxx - 34, cyy + 34, THIN, 0.6, "3 3")
        elif name == "triangle":
            b += poly([(cxx, cyy - 30), (cxx + 27, cyy + 24), (cxx - 27, cyy + 24)], BLUE, 1.8,
                      close=True)
            b += ln(cxx, cyy - 30, cxx, cyy + 24, THIN, 0.6, "3 3")
            b += ln(cxx - 13, cyy - 3, cxx + 13, cyy - 3, THIN, 0.6, "3 3")
        elif name == "circle":
            b += f'<circle cx="{cxx}" cy="{cyy}" r="27" fill="none" stroke="{BLUE}" stroke-width="1.8"/>'
            b += ln(cxx - 33, cyy, cxx + 33, cyy, THIN, 0.6, "4 3")
            b += ln(cxx, cyy - 33, cxx, cyy + 33, THIN, 0.6, "4 3")
        elif name == "semicircle":
            b += f'<path d="M{cxx-30} {cyy+12}A30 30 0 0 1 {cxx+30} {cyy+12}" fill="none" stroke="{BLUE}" stroke-width="1.8"/>'
            b += ln(cxx - 30, cyy + 12, cxx + 30, cyy + 12, BLUE, 1.8)
            b += ln(cxx, cyy - 18, cxx, cyy + 12, THIN, 0.6, "4 3")
        elif name == "hexagon":
            pts = [(cxx + 28 * math.cos(math.radians(60 * k)),
                    cyy + 28 * math.sin(math.radians(60 * k))) for k in range(6)]
            b += poly(pts, BLUE, 1.8, close=True)
            b += ln(cxx - 30, cyy, cxx + 30, cyy, THIN, 0.6, "3 3")
        else:
            pts = [(cxx + 28 * math.cos(math.radians(90 + 72 * k)),
                    cyy + 28 * math.sin(math.radians(90 + 72 * k))) for k in range(5)]
            b += poly(pts, BLUE, 1.8, close=True)
            b += f'<circle cx="{cxx}" cy="{cyy}" r="28" fill="none" stroke="{THIN}" stroke-width="0.7" stroke-dasharray="4 3"/>'
    b += foot(286, "Every sketch starts with a light box or a light circle to hold the proportions,",
              "then the construction lines, then the shape in one confident stroke.")
    return svg(360, 310, b)


DIAGRAMS = {
    "u5_layout": layout,
    "u5_stepped": stepped,
    "u5_cylinder": cylinder,
    "u5_hidden": hidden,
    "u5_missing": missing,
    "u5_freehand": freehand,
}
