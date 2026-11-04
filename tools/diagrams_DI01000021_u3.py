"""Seven compact mobile SVGs for Mathematics-I Unit 3 (Vectors)."""
import math

from flowchart_lib import svg, text, arr, rbox, line, P

BLUE, BF = "#1565C0", "#EAF3FD"
GREEN, GF = "#2E7D32", "#EAF6EC"
ORANGE, OF = "#B66A00", "#FFF4DF"
RED, RF = "#BD2543", "#FDECF0"
GREY = "#666"

TITLES = {
    "v1_vector": "A vector has length and direction",
    "v2_add": "Adding vectors: two equivalent laws",
    "v3_dot": "The dot product measures a shadow",
    "v4_cross": "The cross product gives a perpendicular",
    "v5_angle": "Angle between two vectors",
    "v6_work": "Work done: only the along-motion part counts",
    "v7_moment": "Moment of a force about a point",
}


def heading(t, sub=None):
    body = text(180, 24, t, 14, weight="bold", color=P)
    if sub:
        body += text(180, 46, sub, 10.5, color=GREY)
    return body


def foot(y, *lines):
    return "".join(text(180, y + 16 * i, s, 10.2, color=GREY) for i, s in enumerate(lines))


def axes(b, ox, oy, xmax=330, ytop=70):
    b += line(f"M30 {oy} H{xmax}", "#333", 1.4)
    b += f'<polygon points="{xmax+6},{oy} {xmax-4},{oy-4} {xmax-4},{oy+4}" fill="#333"/>'
    b += line(f"M{ox} {ytop} V{oy+40}", "#333", 1.4)
    b += text(xmax + 2, oy - 8, "x", 10, color="#333", anchor="end")
    b += text(ox + 10, ytop + 8, "y", 10, color="#333", anchor="end")
    return b


# ---------------------------------------------------------------- 1. a vector
def vector():
    b = heading("A vector has length and direction", "Displacement, velocity, force - not mass or time")
    ox, oy = 74, 206
    b = axes(b, ox, oy)
    tipx, tipy = 262, 104
    b += line(f"M{ox} {oy} H{tipx}", "#B9A7D6", 1.2, dash="5 4")
    b += line(f"M{tipx} {oy} V{tipy}", "#B9A7D6", 1.2, dash="5 4")
    b += arr([(ox, oy), (tipx, tipy)], BLUE)
    b += text((ox + tipx) / 2 - 4, 198, "a₁", 11, color=BLUE, weight="bold")
    b += text(tipx + 12, (oy + tipy) / 2, "a₂", 11, color=BLUE, weight="bold", anchor="start")
    b += text(150, 138, "a", 13, color=BLUE, weight="bold")
    b += text(ox + 34, oy - 26, "θ", 10.5, color=ORANGE, weight="bold")
    b += f'<path d="M{ox+34} {oy} A34 34 0 0 0 {ox+22} {oy-24}" fill="none" stroke="{ORANGE}" stroke-width="1.4"/>'
    b += rbox(180, 258, 320, 28, "a = a₁i + a₂j,   |a| = √(a₁² + a₂²)", BF, BLUE, 10.6)
    b += foot(300, "The arrow carries the direction; its length carries the magnitude.",
              "Moving a vector parallel to itself changes nothing.")
    return svg(360, 336, b)


# ---------------------------------------------------------------- 2. addition
def add():
    b = heading("Adding vectors: two equivalent laws", "Triangle law and parallelogram law give a + b")
    ox, oy = 70, 212
    b = axes(b, ox, oy, 334, 78)
    A = (152, 118)
    B = (186, 178)
    C = (A[0] + B[0] - ox, A[1] + B[1] - oy)
    b += line(f"M{ox} {oy} L{B[0]} {B[1]}", "#B9A7D6", 1.2, dash="5 4")
    b += line(f"M{B[0]} {B[1]} L{C[0]} {C[1]}", "#B9A7D6", 1.2, dash="5 4")
    b += arr([(ox, oy), A], BLUE)
    b += arr([A[0], A[1]], GREEN) if False else arr([(A[0], A[1]), (C[0], C[1])], GREEN)
    b += arr([(ox, oy), (C[0], C[1])], RED)
    b += text(98, 164, "a", 12, color=BLUE, weight="bold")
    b += text(240, 112, "b", 12, color=GREEN, weight="bold")
    b += text(132, 200, "a + b", 11.5, color=RED, weight="bold")
    b += text(286, 190, "parallelogram", 9, color=GREY, anchor="end")
    b += rbox(180, 262, 320, 28, "a + b = (a₁ + b₁)i + (a₂ + b₂)j", BF, BLUE, 10.6)
    b += foot(306, "Triangle: tail to head. Parallelogram: the diagonal.",
              "Order does not matter - addition is commutative.")
    return svg(360, 342, b)


# ---------------------------------------------------------------- 3. dot product
def dot():
    b = heading("The dot product measures a shadow", "a · b = |a||b| cos θ")
    ox, oy = 66, 218
    b = axes(b, ox, oy, 330, 80)
    bx, by = 300, 218
    ax, ay = 190, 116
    b += arr([(ox, oy), (bx, by)], GREEN)
    b += arr([(ox, oy), (ax, ay)], BLUE)
    # foot of perpendicular from a to b (b along x-axis here)
    b += line(f"M{ax} {ay} V{oy}", "#B9A7D6", 1.2, dash="4 4")
    b += line(f"M{ox} {oy} H{ax}", ORANGE, 4.0)
    b += text((ox + ax) / 2, oy + 18, "(a · b)/|b|", 10.2, color=ORANGE, weight="bold")
    b += text(bx - 8, oy - 10, "b", 12, color=GREEN, weight="bold", anchor="end")
    b += text(150, 130, "a", 12, color=BLUE, weight="bold")
    b += text(94, oy - 10, "θ", 10, color=GREY, weight="bold")
    b += rbox(180, 268, 320, 28, "projection of a on b = (a · b)/|b|", OF, ORANGE, 10.4)
    b += foot(312, "If θ = 90° the shadow vanishes, so a · b = 0.",
              "The sign of a · b tells you whether θ is acute or obtuse.")
    return svg(360, 348, b)


# ---------------------------------------------------------------- 4. cross product
def cross():
    b = heading("The cross product gives a perpendicular", "a × b points along n, the right-hand rule")
    ox, oy = 120, 232
    # axes: x right-down, y right-up (isometric)
    b += line(f"M{ox} {oy} H320", "#333", 1.3)
    b += text(322, oy - 6, "x", 9.6, color="#333", anchor="end")
    b += line(f"M{ox} {oy} L40 180", "#333", 1.3)
    b += text(50, 176, "y", 9.6, color="#333", anchor="end")
    b += line(f"M{ox} {oy} V96", "#333", 1.3)
    b += text(ox + 10, 104, "z", 9.6, color="#333", anchor="start")
    a_tip = (250, 232)
    b_tip = (176, 148)
    b += f'<polygon points="{ox},{oy} {a_tip[0]},{a_tip[1]} {a_tip[0]+(b_tip[0]-ox)},{a_tip[1]+(b_tip[1]-oy)} {b_tip[0]},{b_tip[1]}" fill="{BF}" stroke="{BLUE}" stroke-width="1.1" opacity="0.75"/>'
    b += arr([(ox, oy), a_tip], BLUE)
    b += arr([(ox, oy), b_tip], GREEN)
    b += arr([(ox, oy), (ox, 108)], RED)
    b += text(232, 224, "a", 12, color=BLUE, weight="bold")
    b += text(160, 158, "b", 12, color=GREEN, weight="bold")
    b += text(ox + 12, 120, "a × b", 11, color=RED, weight="bold", anchor="start")
    b += text(258, 138, "area = |a × b|", 9.6, color=GREY)
    b += rbox(180, 282, 320, 28, "a × b = i(a₂b₃ − a₃b₂) − j(...) + k(...)", RF, RED, 10.2)
    b += foot(326, "Order matters: a × b = −(b × a).", "Parallel vectors give a zero cross product.")
    return svg(360, 360, b)


# ---------------------------------------------------------------- 5. angle
def angle():
    b = heading("Angle between two vectors", "cos θ = (a · b)/(|a||b|)")
    ox, oy = 96, 220
    b = axes(b, ox, oy, 330, 84)
    p1 = (296, 150)
    p2 = (275, 232)
    b += arr([(ox, oy), p1], BLUE)
    b += arr([(ox, oy), p2], GREEN)
    b += f'<path d="M{ox+44} {oy} A44 44 0 0 0 {ox+42} {oy-22}" fill="none" stroke="{ORANGE}" stroke-width="1.5"/>'
    b += text(ox + 56, oy - 14, "θ", 11, color=ORANGE, weight="bold")
    b += text((ox + p1[0]) / 2 - 6, (oy + p1[1]) / 2 - 8, "a", 12, color=BLUE, weight="bold")
    b += text((ox + p2[0]) / 2 + 2, (oy + p2[1]) / 2 + 16, "b", 12, color=GREEN, weight="bold")
    b += rbox(180, 278, 320, 26, "θ = cos⁻¹[(a · b)/(|a||b|)]", BF, BLUE, 10.4)
    b += foot(318, "Positive cosine: acute. Zero: right angle. Negative: obtuse.",
              "The formula is the definition of the dot product rearranged.")
    return svg(360, 352, b)


# ---------------------------------------------------------------- 6. work
def work():
    b = heading("Work done: only the along part counts", "W = F · d = |F||d| cos θ")
    oy = 226
    ox = 96
    b += line(f"M40 {oy} H332", "#333", 1.6)
    b += f'<polygon points="338,{oy} 328,{oy-4} 328,{oy+4}" fill="#333"/>'
    b += text(320, oy + 18, "displacement d", 9.4, color="#333", anchor="end")
    tip = (238, 116)
    b += line(f"M{tip[0]} {tip[1]} V{oy}", "#B9A7D6", 1.2, dash="4 3")
    b += line(f"M{ox} {oy} H{tip[0]}", ORANGE, 4.0)
    b += arr([(ox, oy), tip], RED)
    b += text(tip[0] + 12, 150, "F sin θ", 9.4, color=GREY, anchor="start")
    b += text(tip[0] - 10, oy - 14, "F cos θ", 9.4, color=ORANGE, anchor="end")
    b += f'<path d="M{ox+52} {oy} A52 52 0 0 0 {ox+40} {oy-33}" fill="none" stroke="{P}" stroke-width="1.4"/>'
    b += text(ox + 62, oy - 16, "θ", 10.4, color=P, weight="bold")
    b += text(tip[0] + 10, 120, "F", 12, color=RED, weight="bold", anchor="start")
    b += rbox(180, 282, 320, 28, "W = |F||d| cos θ   (joule = N·m)", GF, GREEN, 10.6)
    b += foot(322, "Only F cos θ does work; F sin θ presses the object down.",
              "Force at 90° to the motion does no work at all.")
    return svg(360, 352, b)


# ---------------------------------------------------------------- 7. moment
def moment():
    b = heading("Moment of a force about a point", "M = r × F, |M| = F × perpendicular distance")
    ox, oy = 84, 228
    b += line(f"M36 {oy} H324", "#333", 1.4)
    b += f'<polygon points="330,{oy} 320,{oy-4} 320,{oy+4}" fill="#333"/>'
    b += line(f"M{ox} 96 V{oy+30}", "#333", 1.4)
    pt = (254, 138)
    b += f'<circle cx="{ox}" cy="{oy}" r="5" fill="{P}"/>'
    b += text(ox - 12, oy + 20, "O", 10.5, color=P, weight="bold", anchor="end")
    b += arr([(ox, oy), pt], BLUE)
    b += text((ox + pt[0]) / 2 - 4, (oy + pt[1]) / 2 + 18, "r", 12, color=BLUE, weight="bold")
    b += f'<circle cx="{pt[0]}" cy="{pt[1]}" r="4.5" fill="{ORANGE}"/>'
    b += arr([(pt[0], pt[1] - 8), (pt[0], 74)], RED)
    b += text(pt[0] + 12, 104, "F", 12, color=RED, weight="bold", anchor="start")
    # perpendicular distance dimension
    b += line(f"M{ox} 250 H{pt[0]}", "#B9A7D6", 1.1, dash="4 4")
    b += line(f"M{ox} {oy+4} V258", "#B9A7D6", 0.9)
    b += line(f"M{pt[0]} {oy+4} V258", "#B9A7D6", 0.9)
    b += text((ox + pt[0]) / 2, 266, "perpendicular distance", 9, color=GREY)
    b += f'<path d="M{ox+52} {oy} A52 52 0 0 0 {ox+44} {oy-26}" fill="none" stroke="{GREEN}" stroke-width="1.4"/>'
    b += text(ox + 60, oy - 12, "θ", 10.4, color=GREEN, weight="bold")
    b += rbox(180, 294, 320, 28, "|M| = |r||F| sin θ = F × perpendicular distance", RF, RED, 10.2)
    b += foot(336, "The moment is a vector, perpendicular to both r and F.",
              "Measure r from the point the moment is taken about.")
    return svg(360, 366, b)


ALL = {
    "v1_vector": vector,
    "v2_add": add,
    "v3_dot": dot,
    "v4_cross": cross,
    "v5_angle": angle,
    "v6_work": work,
    "v7_moment": moment,
}
