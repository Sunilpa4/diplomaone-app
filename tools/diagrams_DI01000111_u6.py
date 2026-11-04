"""Five figures for Engineering Graphics (DI01000111) Unit 6 - isometric drawing.

The three isometric axes are 30 degrees above the horizontal, and every true length along them is
either drawn full size (isometric drawing) or multiplied by 0.816 (isometric projection). The circles
are drawn as the exact projection of a circle, so the ellipse in the figure is the right one.
"""
import math

from flowchart_lib import svg, text
from diagrams_DI01000111_lib import (INK, GREY, THIN, BLUE, GREEN, ORANGE, RED, PURPLE, TEAL,
                                     ln, poly, arrow, dot, ring, heading, foot, xy, tag, dash_box)

TITLES = {
    "u6_axes": "The three isometric axes and the scale",
    "u6_box": "The box method: three views to one picture",
    "u6_offsets": "Points off the axes: offsets and a slope",
    "u6_cylinder": "A cylinder: two ellipses and two tangents",
    "u6_solids": "Prism, pyramid and cone in isometric",
}

CAPTIONS = {
    "u6_axes": "Thirty degrees above the horizontal both ways, and one axis up: that is the whole "
               "frame. Lines off the frame are not drawn true.",
    "u6_box": "Box the object in first, then cut the corners away - the outline of the isometric is "
              "always a hexagon that holds the object.",
    "u6_offsets": "A point that is not on an axis is fixed by measuring along the axes from a known "
                  "corner, never by guessing.",
    "u6_cylinder": "The isometric circle is an ellipse 1.22 d by 0.71 d, drawn inside the isometric "
                   "square of side d and touching it at four points.",
    "u6_solids": "Base first - a rhombus for the square, a polygon for the prism - then the vertical "
                 "edges, then the apex or the second base.",
}


def iso(ox, oy, s, x, y, z):
    c = math.cos(math.radians(30))
    return (ox + (x - y) * c * s, oy + (x + y) * 0.5 * s - z * s)


def axes():
    b = heading("Thirty degrees each way, and one axis up", "isometric drawing at full scale")
    ox, oy = 118.0, 152.0
    L = 80.0
    c, s30 = math.cos(math.radians(30)), math.sin(math.radians(30))
    b += ln(ox, oy, ox + L * c, oy - L * s30, RED, 1.8)
    b += ln(ox, oy, ox - L * c, oy - L * s30, GREEN, 1.8)
    b += ln(ox, oy, ox, oy - L, BLUE, 1.8)
    b += f'<path d="M{ox+34:.1f} {oy:.1f}A34 34 0 0 0 {ox+34*c:.1f} {oy-34*s30:.1f}" fill="none" stroke="{GREY}" stroke-width="0.7"/>'
    b += text(ox + 40, oy - 6, "30", 6.6, anchor="start", color=GREY)
    b += text(ox - 40, oy - 6, "30", 6.6, anchor="end", color=GREY)
    b += tag(ox + L * c, oy - L * s30, "X", RED, dx=2, dy=6)
    b += tag(ox - L * c, oy - L * s30, "Y", GREEN, dx=-2, dy=6, anchor="end")
    b += tag(ox, oy - L, "Z", BLUE, dx=0, dy=-8, anchor="middle")
    b += text(ox, oy + 16, "O", 7.2, anchor="middle", color=INK, weight="bold")
    # the scale
    b += text(180, 224, "one 30 mm edge, drawn two ways", 7.6, color=GREY)
    b += ln(118, 248, 118 + 60, 248, INK, 2.0)
    b += text(118 + 30, 242, "true 30 mm", 6.6, anchor="middle", color=INK)
    b += ln(118, 272, 118 + 60 * 0.816, 272, PURPLE, 2.0)
    b += text(118 + 34, 264, "isometric 24.5 mm", 6.6, anchor="middle", color=PURPLE)
    b += text(198, 252, "drawing: use 30 mm", 6.6, anchor="start", color=INK)
    b += text(198, 276, "projection: use 24.5", 6.6, anchor="start", color=PURPLE)
    b += foot(300, "Three axes at 120 degrees in space become two lines at 30 degrees",
              "and one straight up - all three equally foreshortened.")
    return svg(360, 326, b)


def box():
    b = heading("Box the object in, then cut it out", "block 60 x 40 x 30")
    s = 0.95
    ox, oy = 108.0, 92.0
    P = lambda x, y, z: iso(ox, oy, s, x, y, z)
    # the enclosing box, faint
    b += poly([P(0, 0, 0), P(60, 0, 0), P(60, 40, 0), P(0, 40, 0)], THIN, 0.8, "4 3", close=True)
    b += poly([P(0, 0, 30), P(60, 0, 30), P(60, 40, 30), P(0, 40, 30)], THIN, 0.8, "4 3", close=True)
    for v in ((60, 0), (60, 40), (0, 40)):
        b += ln(*P(v[0], v[1], 0)[:2], *P(v[0], v[1], 30)[:2], THIN, 0.8, "4 3")
    # the block: front face, right face, top face
    b += poly([P(0, 0, 0), P(60, 0, 0), P(60, 0, 30), P(0, 0, 30)], BLUE, 1.8, close=True)
    b += poly([P(60, 0, 0), P(60, 40, 0), P(60, 40, 30), P(60, 0, 30)], BLUE, 1.6, close=True)
    b += poly([P(0, 0, 30), P(60, 0, 30), P(60, 40, 30), P(0, 40, 30)], BLUE, 1.6, close=True)
    b += text((P(0, 0, 0)[0] + P(60, 0, 0)[0]) / 2, P(0, 0, 0)[1] + 14, "60", 6.6, color=GREY)
    b += text(P(60, 0, 0)[0] + 12, (P(60, 0, 0)[1] + P(60, 40, 0)[1]) / 2 + 6, "40", 6.6,
              anchor="start", color=GREY)
    b += text(P(60, 0, 0)[0] + 5, (P(60, 0, 0)[1] + P(60, 0, 30)[1]) / 2, "30", 6.6,
              anchor="start", color=GREY)
    # the three views, small, on the right
    fx, fy = 250.0, 62.0
    b += f'<rect x="{fx}" y="{fy}" width="60" height="30" fill="none" stroke="{PURPLE}" stroke-width="1.3"/>'
    b += text(fx + 30, fy + 40, "front 60 x 30", 6.2, anchor="middle", color=GREY)
    b += f'<rect x="{fx}" y="{fy+52}" width="60" height="40" fill="none" stroke="{PURPLE}" stroke-width="1.3"/>'
    b += text(fx + 30, fy + 102, "top 60 x 40", 6.2, anchor="middle", color=GREY)
    b += f'<rect x="{fx}" y="{fy+114}" width="40" height="30" fill="none" stroke="{PURPLE}" stroke-width="1.3"/>'
    b += text(fx + 20, fy + 154, "side 40 x 30", 6.2, anchor="middle", color=GREY)
    b += foot(286, "Draw the three axes from one corner, measure the three sizes along them, then",
              "draw the three visible faces - no view is needed for the hidden edges.")
    return svg(360, 308, b)


def offsets():
    b = heading("A sloping face is found by offsets", "wedge 50 x 30, height 20 at one end")
    s = 0.95
    ox, oy = 118.0, 104.0
    P = lambda x, y, z: iso(ox, oy, s, x, y, z)
    # base rhombus
    b += poly([P(0, 0, 0), P(50, 0, 0), P(50, 30, 0), P(0, 30, 0)], BLUE, 1.6, close=True)
    # vertical edges
    b += ln(*P(0, 0, 0)[:2], *P(0, 0, 20)[:2], BLUE, 1.8)
    b += ln(*P(50, 0, 0)[:2], *P(50, 0, 0)[:2], BLUE, 1.6)
    b += ln(*P(0, 30, 0)[:2], *P(0, 30, 20)[:2], BLUE, 1.6)
    b += ln(*P(0, 0, 20)[:2], *P(0, 30, 20)[:2], BLUE, 1.6)
    b += ln(*P(50, 30, 0)[:2], *P(50, 30, 0)[:2], BLUE, 1.6)
    # the sloping face: from the top at x=0 down to the far edge at x=50
    b += poly([P(0, 0, 20), P(0, 30, 20), P(50, 30, 0), P(50, 0, 0)], RED, 1.8, close=True)
    b += ln(*P(0, 0, 20)[:2], *P(50, 0, 0)[:2], RED, 1.8)
    b += text(P(0, 0, 20)[0] - 10, P(0, 0, 20)[1] - 4, "20", 6.4, anchor="end", color=GREY)
    b += text((P(0, 0, 0)[0] + P(50, 0, 0)[0]) / 2, P(0, 0, 0)[1] + 14, "50", 6.4, color=GREY)
    # offsets to a point on the sloping face
    mid = P(25, 15, 10)
    b += dot(mid[0], mid[1], PURPLE, 2.6)
    b += ln(*P(25, 15, 0)[:2], mid[0], mid[1], PURPLE, 0.9, "4 3")
    b += ln(*P(25, 0, 0)[:2], *P(25, 15, 0)[:2], PURPLE, 0.8, "4 3")
    b += ln(*P(0, 15, 0)[:2], *P(25, 15, 0)[:2], PURPLE, 0.8, "4 3")
    b += tag(mid[0], mid[1], "P", PURPLE, dx=4, dy=-4)
    b += text(180, 210, "P is 25 along X, 15 along Y and 10 up: measure the three offsets from O,",
              7.2, color=GREY)
    b += text(180, 223, "then join P to the corners of the sloping face.", 7.2, color=GREY)
    b += foot(252, "A line that is not parallel to an isometric axis has no true length in the",
              "drawing: its ends must be located by offsets, then joined.")
    return svg(360, 274, b)


def cylinder():
    b = heading("A standing cylinder, and its ellipse", "diameter 40 mm, height 40 mm")
    s = 1.0
    ox, oy = 96.0, 120.0
    r = 20.0
    c = math.cos(math.radians(30))

    def circ(cz, t):
        return iso(ox, oy, s, r * math.cos(t), r * math.sin(t), cz)

    top = [circ(40, 2 * math.pi * i / 60) for i in range(60)]
    bot = [circ(0, 2 * math.pi * i / 60) for i in range(60)]
    b += poly(bot, THIN, 1.1, "5 3")
    b += poly(top, BLUE, 1.8, close=True)
    e = 1.2247 * r * s
    cx0, cy0 = iso(ox, oy, s, 0, 0, 0)
    b += ln(cx0 - e, cy0, cx0 - e, cy0 - 40 * s, BLUE, 1.6)
    b += ln(cx0 + e, cy0, cx0 + e, cy0 - 40 * s, BLUE, 1.6)
    b += ln(*iso(ox, oy, s, 0, 0, 0)[:2], *iso(ox, oy, s, 0, 0, 44)[:2], THIN, 0.7, "6 3")
    b += text(cx0 - e - 6, cy0 - 22, "40", 6.4, anchor="end", color=GREY)
    # the ellipse inside its rhombus
    cx2, cy2 = 268.0, 100.0
    s2 = 0.9

    def c2(x, y, z=0):
        return iso(cx2, cy2, s2, x, y, z)
    rh = [c2(20, 20), c2(-20, 20), c2(-20, -20), c2(20, -20)]
    b += poly(rh, THIN, 1.0, "4 3", close=True)
    ell = [c2(20 * math.cos(2 * math.pi * i / 60), 20 * math.sin(2 * math.pi * i / 60))
           for i in range(60)]
    b += poly(ell, PURPLE, 1.8, close=True)
    for t in (0, 90, 180, 270):
        px, py = c2(20 * math.cos(math.radians(t)), 20 * math.sin(math.radians(t)))
        b += dot(px, py, RED, 2.0)
    b += text(cx2, cy2 + 60, "ellipse 1.22 d by 0.71 d", 6.6, color=PURPLE)
    b += text(cx2, 52, "the isometric square", 6.4, color=GREY)
    b += foot(240, "Long axis 1.22 x 40 = 49 mm, short axis 0.71 x 40 = 28 mm;",
              "the ellipse touches the rhombus at the mid-points of its sides.")
    return svg(360, 264, b)


def solids():
    b = heading("Prism, pyramid and cone", "base 30 mm, axis 45 mm")
    s = 0.85
    # triangular prism
    ox, oy = 78.0, 116.0
    s3 = 0.75

    def P(x, y, z):
        return iso(ox, oy, s3, x, y, z)
    tri = [(0, 0), (30, 0), (15, 26)]

    def Q(x, y, z=0):
        return iso(ox, oy, s3, x, y, z)
    b += poly([Q(x, y, 0) for x, y in tri], BLUE, 1.6, close=True)
    b += poly([Q(x, y, 40) for x, y in tri], BLUE, 1.6, close=True)
    for x, y in tri:
        b += ln(*Q(x, y, 0)[:2], *Q(x, y, 40)[:2], BLUE, 1.4)
    b += text(ox, oy + 62, "triangular prism", 6.6, color=GREY)
    # square pyramid
    ox, oy = 196.0, 116.0

    def R(x, y, z):
        return iso(ox, oy, s3, x, y, z)
    sq = [(0, 0), (30, 0), (30, 30), (0, 30)]
    b += poly([R(x, y, 0) for x, y in sq], RED, 1.6, close=True)
    apex = R(15, 15, 45)
    for x, y in sq:
        b += ln(*R(x, y, 0)[:2], apex[0], apex[1], RED, 1.3)
    b += text(ox, oy + 62, "square pyramid", 6.6, color=GREY)
    # cone
    ox, oy = 306.0, 112.0
    r = 15.0

    def C(t, z=0):
        return iso(ox, oy, s3, r * math.cos(t), r * math.sin(t), z)
    base = [C(2 * math.pi * i / 60) for i in range(60)]
    b += poly(base, GREEN, 1.5, close=True)
    apex = iso(ox, oy, s3, 0, 0, 45)
    b += ln(*C(math.pi / 2)[:2], apex[0], apex[1], GREEN, 1.5)
    b += ln(*C(-math.pi / 2)[:2], apex[0], apex[1], GREEN, 1.5)
    b += dot(apex[0], apex[1], GREEN, 2.2)
    b += text(ox, oy + 62, "cone", 6.6, color=GREY)
    b += foot(232, "The base polygon is drawn true in isometric (a rhombus for a square);",
              "vertical edges are full length and the apex sits on the axis.")
    return svg(360, 254, b)


DIAGRAMS = {
    "u6_axes": axes,
    "u6_box": box,
    "u6_offsets": offsets,
    "u6_cylinder": cylinder,
    "u6_solids": solids,
}
