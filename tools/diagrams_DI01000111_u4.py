"""Five figures for Engineering Graphics (DI01000111) Unit 4 - planes.

A plane perpendicular to a reference plane shows as an edge in that view; the other view is the
apparent shape, in which one dimension is multiplied by the cosine of the angle of tilt. Every figure
is drawn from that one rule.
"""
import math

from flowchart_lib import svg, text
from diagrams_DI01000111_lib import (INK, GREY, THIN, BLUE, GREEN, ORANGE, RED, PURPLE, TEAL,
                                     ln, poly, arrow, dot, ring, heading, foot, xy, tag, dash_box)

TITLES = {
    "u4_basic": "Three positions that show the true shape",
    "u4_edge_vp": "Square plane, edge view in the elevation",
    "u4_edge_hp": "Hexagonal plane, edge view in the plan",
    "u4_circle": "Circular plane inclined to HP",
    "u4_both": "Inclined to both planes: two stages",
}

CAPTIONS = {
    "u4_basic": "Parallel to a plane: that view is the true shape, the other is an edge. "
                "Perpendicular to both: two edges.",
    "u4_edge_vp": "The elevation collapses to the edge lying at 40 degrees, and the plan keeps 50 mm "
                  "across but only 38.3 mm along XY.",
    "u4_edge_hp": "Now the plan is the edge at 45 degrees and the elevation is the squeezed hexagon: "
                  "60 mm stays 42.4 mm across.",
    "u4_circle": "A circle seen at an angle is an ellipse: the diameter parallel to the hinge stays "
                 "60 mm, the other shortens to 52 mm.",
    "u4_both": "Stage 1 gives the edge view at the first angle; the plan is then swung to the second "
               "angle and the final elevation is read off the locus.",
}


def basic():
    b = heading("Edge or true shape: the plane decides")
    panels = [(2.0, "parallel to HP"), (122.0, "parallel to VP"), (242.0, "perpendicular to both")]
    for x0, name in panels:
        b += f'<rect x="{x0 + 2}" y="52" width="112" height="176" rx="6" fill="#FBFCFD" stroke="{THIN}" stroke-width="0.9"/>'
        b += text(x0 + 58, 66, name, 7.6, weight="bold", color=INK)
        b += ln(x0 + 8, 138, x0 + 108, 138, INK, 0.9)
        b += text(x0 + 106, 134, "XY", 6.0, anchor="end", color=GREY)
    # (1) parallel to HP: plan is the true shape
    x0 = 2.0
    b += ln(x0 + 22, 120, x0 + 88, 120, RED, 2.2)
    b += ln(x0 + 22, 120, x0 + 22, 86, THIN, 0.7, "4 3")
    b += ln(x0 + 88, 120, x0 + 88, 86, THIN, 0.7, "4 3")
    b += text(x0 + 58, 82, "edge", 6.4, color=RED)
    b += f'<rect x="{x0 + 22}" y="156" width="66" height="48" fill="{BLUE}" fill-opacity="0.14" stroke="{BLUE}" stroke-width="2"/>'
    b += text(x0 + 58, 214, "true shape", 6.8, color=BLUE)
    b += text(x0 + 58, 226, "in the plan", 6.4, color=GREY)
    # (2) parallel to VP: elevation is the true shape
    x0 = 122.0
    b += f'<rect x="{x0 + 22}" y="74" width="66" height="48" fill="{BLUE}" fill-opacity="0.14" stroke="{BLUE}" stroke-width="2"/>'
    b += text(x0 + 58, 86, "true shape", 6.8, anchor="middle", color=BLUE)
    b += ln(x0 + 22, 160, x0 + 88, 160, RED, 2.2)
    b += ln(x0 + 22, 160, x0 + 22, 180, THIN, 0.7, "4 3")
    b += ln(x0 + 88, 160, x0 + 88, 180, THIN, 0.7, "4 3")
    b += text(x0 + 58, 206, "edge", 6.4, color=RED)
    b += text(x0 + 58, 220, "in the plan", 6.4, color=GREY)
    # (3) perpendicular to both: two edges
    x0 = 242.0
    b += ln(x0 + 56, 78, x0 + 56, 130, RED, 2.4)
    b += ln(x0 + 56, 146, x0 + 56, 198, RED, 2.4)
    b += text(x0 + 60, 84, "edge", 6.4, anchor="start", color=RED)
    b += text(x0 + 60, 192, "edge", 6.4, anchor="start", color=RED)
    b += text(x0 + 56, 214, "both views are edges", 6.6, anchor="middle", color=GREY)
    b += text(x0 + 56, 226, "square to XY", 6.4, anchor="middle", color=GREY)
    b += foot(252, "A plane parallel to a reference plane is seen in its true shape there,",
              "and as a straight edge, parallel to XY, in the other view.")
    return svg(360, 274, b)


def edge_vp():
    b = heading("Perpendicular to VP, inclined to HP", "square 50 mm, 40 deg, side AB in HP")
    s = 1.3
    yl = 152.0
    x0 = 96.0
    b += xy(yl, 20, 340)
    ax, ay = x0, yl
    dx_, dy_ = x0 + 50 * s * math.cos(math.radians(40)), yl - 50 * s * math.sin(math.radians(40))
    b += ln(ax, ay, dx_, dy_, RED, 2.2)
    b += ring(ax, ay, RED, 2.6)
    b += ring(dx_, dy_, RED, 2.6)
    b += tag(ax, ay, "a' b'", RED, dx=-6, dy=-4, anchor="end")
    b += tag(dx_, dy_, "d' c'", RED, dx=5, dy=-4)
    b += text(ax + 26, ay - 10, "50 at 40 deg", 6.6, anchor="start", color=RED)
    py = yl + 20 * s
    b += ln(x0, py, x0, py + 50 * s, BLUE, 2.0)
    b += ln(dx_, py, dx_, py + 50 * s, BLUE, 2.0)
    b += ln(x0, py, dx_, py, BLUE, 2.0)
    b += ln(x0, py + 50 * s, dx_, py + 50 * s, BLUE, 2.0)
    b += ln(ax, ay, x0, py, THIN, 0.7, "4 3")
    b += ln(dx_, dy_, dx_, py, THIN, 0.7, "4 3")
    b += ln(x0, py, x0, py + 50 * s, THIN, 0.6, "2 3")
    b += dot(x0, py, BLUE, 2.4)
    b += dot(dx_, py, BLUE, 2.4)
    b += dot(x0, py + 50 * s, BLUE, 2.4)
    b += dot(dx_, py + 50 * s, BLUE, 2.4)
    b += tag(x0, py, "a d", BLUE, dx=-6, dy=2, anchor="end")
    b += tag(x0, py + 50 * s, "b c", BLUE, dx=-6, dy=12, anchor="end")
    b += text(x0 + 12, py + 10, "50 cos 40 = 38.3", 6.8, anchor="start", color=BLUE)
    b += text(dx_ + 6, py + 34, "50", 6.6, anchor="start", color=BLUE)
    b += text(x0 - 4, py - 6, "20", 6.2, anchor="end", color=GREY)
    b += foot(292, "The elevation is the edge because VP looks along the plane; the plan is the",
              "apparent shape - 50 mm deep, only 38.3 mm across.")
    return svg(360, 316, b)


def edge_hp():
    b = heading("Perpendicular to HP, inclined to VP", "hexagon 30 mm side, 45 deg to VP")
    s = 1.25
    yl = 152.0
    R = 30 * s
    cos45 = math.cos(math.radians(45))
    cx = 172.0
    cy = 104.0
    verts = [(cx + R * math.cos(math.radians(60 * k)) * cos45,
              cy - R * math.sin(math.radians(60 * k))) for k in range(6)]
    b += xy(yl, 20, 340)
    b += poly(verts, BLUE, 2.0, close=True)
    for vx, vy in verts:
        b += dot(vx, vy, BLUE, 2.0)
    b += text(cx, cy - R - 8, "apparent shape", 6.6, color=BLUE)
    b += text(cx, cy - R - 19, "60 cos 45 = 42.4 across", 6.2, color=GREY)
    origin = (cx, yl + 46)
    tip = (origin[0] + R * cos45 * 1.0 + 0, origin[1] + R * cos45 * 1.0)
    p0 = (origin[0] - R * cos45, origin[1] - R * cos45)
    p1 = (origin[0] + R * cos45, origin[1] + R * cos45)
    b += ln(p0[0], p0[1], p1[0], p1[1], RED, 2.4)
    for k, (vx, vy) in enumerate(verts):
        px = origin[0] + (vx - cx)
        py = origin[1] + (vx - cx)
        if p0[1] - 1 <= py <= p1[1] + 1:
            b += dot(px, py, RED, 2.2)
            b += ln(vx, vy, px, py, THIN, 0.7, "4 3")
    b += text(origin[0] - 30, origin[1] - 22, "edge at 45 deg", 6.6, anchor="end", color=RED)
    b += text(origin[0] - 30, origin[1] - 12, "60 mm long in plan", 6.4, anchor="end", color=GREY)
    b += foot(300, "Now HP looks along the plane, so the plan is the edge. The elevation is",
              "the apparent hexagon: 42.4 mm across, 52 mm from flat to flat.")
    return svg(360, 324, b)


def circle():
    b = heading("A circle at an angle is an ellipse", "diameter 60 mm, 30 deg to HP")
    s = 1.6
    yl = 150.0
    x0 = 84.0
    b += xy(yl, 20, 340)
    d = 60 * s * math.cos(math.radians(30))
    b += ln(x0, yl, x0 + 60 * s, yl - d, RED, 2.4)
    b += ring(x0, yl, RED, 2.6)
    b += ring(x0 + 60 * s, yl - d, RED, 2.6)
    b += tag(x0, yl, "a'", RED, dx=-6, dy=-4, anchor="end")
    b += tag(x0 + 60 * s, yl - d, "b'", RED, dx=4, dy=-4)
    b += text(x0 + 20, yl - d - 12, "edge: 60 at 30 deg", 6.6, anchor="start", color=RED)
    cy = yl + 76
    a_axis = 30 * s
    b_axis = a_axis * math.cos(math.radians(30))
    pts = [(x0 + a_axis + a_axis * math.cos(t), cy - b_axis * math.sin(t))
           for t in [2 * math.pi * i / 72 for i in range(72)]]
    b += poly(pts, PURPLE, 2.0, close=True)
    b += ln(x0, cy, x0 + 2 * a_axis, cy, THIN, 0.7, "6 3")
    b += ln(x0 + a_axis, cy - b_axis, x0 + a_axis, cy + b_axis, THIN, 0.7, "6 3")
    b += ln(x0, yl, x0, cy, THIN, 0.7, "4 3")
    b += ln(x0 + 60 * s, yl - d, x0 + 2 * a_axis, cy, THIN, 0.7, "4 3")
    b += text(x0 + a_axis, cy + b_axis + 12, "ellipse 60 x 52", 6.8, color=PURPLE)
    b += text(x0 + a_axis, cy + b_axis + 23, "the diameter across the tilt shortens", 6.2,
              color=GREY)
    b += foot(300, "Divide the circle as usual, project each point into the plan and set its",
              "depth off as d cos 30 from the line through the centre.")
    return svg(360, 322, b)


def both():
    b = heading("Inclined to both planes: two stages", "square 50 mm, 45 deg to HP, 30 deg to VP")
    s = 1.1
    yl = 168.0
    x0 = 168.0
    b += xy(yl, 16, 344)
    e = 50 * s * math.cos(math.radians(45))          # 35.4 mm along XY, and the rise
    # stage 1: edge view in the elevation, apparent shape in the plan
    b += ln(x0, yl, x0 + e, yl - e, PURPLE, 1.3, "5 3")
    b += ln(x0, yl + 22, x0 + e, yl + 22, PURPLE, 1.2, "5 3")
    b += ln(x0, yl + 22, x0, yl + 22 + 50 * s, PURPLE, 1.2, "5 3")
    b += ln(x0 + e, yl + 22, x0 + e, yl + 22 + 50 * s, PURPLE, 1.2, "5 3")
    b += ln(x0, yl + 22 + 50 * s, x0 + e, yl + 22 + 50 * s, PURPLE, 1.2, "5 3")
    b += text(x0 - 6, yl - e - 8, "stage 1: edge 50 at 45 deg", 6.2, anchor="start", color=PURPLE)
    # stage 2: swing the plan 30 deg about a
    dxv, dyv = e * math.cos(math.radians(30)), e * math.sin(math.radians(30))
    bxv = -50 * s * math.sin(math.radians(30))
    byv = 50 * s * math.cos(math.radians(30))
    d2 = (x0 + dxv, yl + 22 + dyv)
    b2 = (x0 + bxv, yl + 22 + byv)
    c2 = (d2[0] + bxv, d2[1] + byv)
    b += poly([(x0, yl + 22), d2, c2, b2], BLUE, 2.0, close=True)
    b += f'<path d="M{x0 + e:.1f} {yl + 22:.1f}A{e:.1f} {e:.1f} 0 0 1 {d2[0]:.1f} {d2[1]:.1f}" fill="none" stroke="{GREEN}" stroke-width="0.9" stroke-dasharray="4 3"/>' 
    b += text(d2[0] + 4, d2[1] + 14, "plan swung 30 deg", 6.2, anchor="start", color=BLUE)
    # final elevation off the loci
    b += ln(x0 - 8, yl - e, x0 + e + 30, yl - e, THIN, 0.7, "4 3")
    b += ln(x0 - 8, yl, x0 + e + 30, yl, THIN, 0.7, "4 3")
    d2p = (d2[0], yl - e)
    c2p = (c2[0], yl - e)
    b += poly([(x0, yl), d2p, c2p, (b2[0], yl)], RED, 2.0, close=True)
    for a_, b_ in ((d2, d2p), (c2, c2p), (b2, (b2[0], yl))):
        b += ln(a_[0], a_[1], b_[0], b_[1], THIN, 0.6, "3 3")
    b += tag(x0, yl, "a'", RED, dx=-6, dy=-4, anchor="end")
    b += tag(d2p[0], d2p[1], "d'", RED, dx=2, dy=-4)
    b += tag(b2[0], yl, "b'", RED, dx=-6, dy=-4, anchor="end")
    b += text(x0 + e + 34, yl - e + 3, "locus of d'", 6.2, anchor="end", color=GREY)
    b += dash_box(8, 286, 344, 38)
    b += text(180, 300, "stage 1 edge 50 at 45 deg   |   stage 2 plan swung to 30 deg", 7.2)
    b += text(180, 314, "50 cos 45 = 35.4 across, and the depth 50 cos 30 = 43.3", 7.2, color=GREY)
    b += foot(336, "Make the plane perpendicular to VP first and finish the edge view; swing the",
              "plan for the second angle and read the final elevation off the locus lines.")
    return svg(360, 366, b)


DIAGRAMS = {
    "u4_basic": basic,
    "u4_edge_vp": edge_vp,
    "u4_edge_hp": edge_hp,
    "u4_circle": circle,
    "u4_both": both,
}
