"""Six construction diagrams for Engineering Graphics (DI01000111) Unit 1.

English only, like the subject. Every drawing is shown as a construction: thin lines are the
construction, thick lines are the finished outline, and small numbered badges repeat the step order
used in the notes. 360 px wide for a phone.
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
    "u1_sheet": "The A2 sheet: border, filing margin, title block",
    "u1_lines": "Eight BIS line types and what they mean",
    "u1_dim": "Anatomy of a dimension on a plate",
    "u1_scale": "Plain scale, RF 1:50, six metres",
    "u1_poly": "Pentagon by the general method, 5 steps",
    "u1_hex": "Hexagon by compass, octagon in a square",
}

CAPTIONS = {
    "u1_sheet": "Fix the sheet square, draw the border 10 mm in and 20 mm on the left, and put the "
                "65 mm title block in the bottom right corner before any view.",
    "u1_lines": "Two thicknesses only, 0.5 mm and 0.25 mm: the weight of a line tells the reader "
                "what the line is.",
    "u1_dim": "Extension line, dimension line, arrowhead and figure - and the figure is 3 mm high, "
              "1 mm above a thin unbroken line.",
    "u1_scale": "120 mm of paper carries six metres: the leftmost 20 mm is split into ten 2 mm "
                "decimetres, so 3.7 m is read without arithmetic.",
    "u1_poly": "Divide the vertical diameter into n parts, arc from the top with the diameter, and "
               "two rays give the first chord - then step it round the circle.",
    "u1_hex": "A chord equal to the radius steps the hexagon in six; in a square, 0.414 of the side "
              "is the octagon side.",
}


def ln(x1, y1, x2, y2, color=INK, w=1.0, dash=None):
    da = f' stroke-dasharray="{dash}"' if dash else ""
    return (f'<path d="M{x1} {y1}L{x2} {y2}" fill="none" stroke="{color}" stroke-width="{w}" '
            f'stroke-linecap="round"{da}/>')


def arrow(x1, y1, x2, y2, color=INK, w=1.0):
    ang = math.atan2(y2 - y1, x2 - x1)
    s = 5.0
    p1 = (x2 - s * math.cos(ang) + s * 0.32 * math.sin(ang), y2 - s * math.sin(ang) - s * 0.32 * math.cos(ang))
    p2 = (x2 - s * math.cos(ang) - s * 0.32 * math.sin(ang), y2 - s * math.sin(ang) + s * 0.32 * math.cos(ang))
    return (ln(x1, y1, x2, y2, color, w) +
            f'<path d="M{p1[0]:.1f} {p1[1]:.1f}L{x2:.1f} {y2:.1f}L{p2[0]:.1f} {p2[1]:.1f}Z" fill="{color}"/>')


def heading(t, sub=None):
    b = text(180, 21, t, 12.4, weight="bold", color=INK)
    if sub:
        b += text(180, 39, sub, 9.4, color=GREY)
    return b


def foot(y, *lines):
    return "".join(text(180, y + 13 * i, s, 8.8, color=GREY) for i, s in enumerate(lines))


def badge(x, y, n, color=BLUE):
    return (f'<circle cx="{x}" cy="{y}" r="6.6" fill="#FFFFFF" stroke="{color}" stroke-width="1.2"/>'
            + text(x, y + 3, str(n), 7.6, color=color, weight="bold"))


# ------------------------------------------------------------------ 1. sheet layout
def sheet():
    b = heading("The sheet first, the drawing after", "A2, 420 x 594 mm, landscape")
    x0, y0, x1, y1 = 22, 54, 232, 206            # trimming edge
    b += f'<rect x="{x0}" y="{y0}" width="{x1 - x0}" height="{y1 - y0}" fill="none" stroke="{INK}" stroke-width="1.1"/>'
    bx0, by0, bx1, by1 = x0 + 5, y0 + 5, x1 - 5, y1 - 5
    b += (f'<rect x="{bx0 + 9}" y="{by0}" width="{bx1 - bx0 - 9}" height="{by1 - by0}" fill="none" '
          f'stroke="{BLUE}" stroke-width="1.0"/>')
    # filing margin shading
    b += (f'<rect x="{bx0}" y="{by0}" width="9" height="{by1 - by0}" fill="{BLUE}" fill-opacity="0.10" '
          f'stroke="none"/>')
    # title block
    tx0, ty0, tx1, ty1 = bx1 - 74, by1 - 30, bx1, by1
    b += f'<rect x="{tx0}" y="{ty0}" width="{tx1 - tx0}" height="{ty1 - ty0}" fill="#FFFFFF" stroke="{GREEN}" stroke-width="1.2"/>'
    b += ln(tx0, ty0 + 10, tx1, ty0 + 10, GREEN, 0.8)
    b += ln(tx0, ty0 + 20, tx1, ty0 + 20, GREEN, 0.8)
    b += text((tx0 + tx1) / 2, ty0 + 7, "TITLE", 6.4, color=GREEN, weight="bold")
    b += text((tx0 + tx1) / 2, ty0 + 17, "name / roll no", 5.8, color=INK)
    b += text((tx0 + tx1) / 2, ty0 + 27, "scale / sheet", 5.8, color=INK)
    # leaders
    b += ln(x0 + 2, y0 + 2, 248, 62, THIN, 0.7)
    b += ln(x0 + 4.5, (by0 + by1) / 2, 248, 96, THIN, 0.7)
    b += ln(tx0 + 4, ty0 + 4, 248, 150, THIN, 0.7)
    b += text(250, 60, "trimming edge", 7.4, anchor="start", color=GREY)
    b += text(250, 94, "filing margin 20 mm", 7.4, anchor="start", color=BLUE)
    b += text(250, 106, "border 10 mm", 7.4, anchor="start", color=BLUE)
    b += text(250, 148, "title block 65 x 30 mm", 7.4, anchor="start", color=GREEN)
    b += text(250, 160, "bottom right corner", 7.4, anchor="start", color=GREY)
    b += f'<rect x="8" y="216" width="344" height="26" rx="5" fill="#F4F6F8" stroke="{THIN}" stroke-width="0.9"/>'
    b += text(180, 228, "2H construction  |  H final outline  |  HB lettering", 7.4, color=INK)
    b += text(180, 238, "3 mm dimension figures, 5 mm entries, 7 mm title", 7.0, color=GREY)
    b += foot(256, "The left margin is punched for filing - nothing is drawn in it.",
              "Check the diagonals of the sheet before taping: a skewed sheet stays skewed.")
    return svg(360, 276, b)


# ------------------------------------------------------------------ 2. line types
def lines():
    b = heading("Eight lines, eight meanings", "thickness 0.5 mm or 0.25 mm, ratio 2 : 1")
    rows = [
        ("continuous thick", "0.5", "visible outline and visible edge", None, 2.0),
        ("continuous thin", "0.25", "dimension, extension, leader, hatching", None, 0.9),
        ("dashed thin", "0.25", "hidden edge or hidden outline", "6 3", 0.9),
        ("wavy thin", "0.25", "limit of a partial view", "wavy", 0.9),
        ("zig-zag thin", "0.25", "limit of a broken-out section", "zig", 0.9),
        ("chain thin", "0.25", "centre line, pitch circle", "10 3 2 3", 0.9),
        ("chain, thick ends", "0.25/0.5", "cutting plane line of a section", "cut", 0.9),
        ("double dash thin", "0.25", "adjacent part or alternate position", "9 2.5 1.5 2.5", 0.9),
    ]
    y = 52
    x1, x2 = 40, 108
    for name, thick, use, pat, w in rows:
        if pat == "wavy":
            pts = [(x1 + i * 4, y + 6 + 2.4 * (1 if (i // 2) % 2 else -1)) for i in range(20)]
            b += (f'<polyline points="{" ".join(f"{px},{py:.1f}" for px, py in pts)}" fill="none" '
                  f'stroke="{INK}" stroke-width="0.9"/>')
        elif pat == "zig":
            pts = [(x1 + i * 4, (y + 6) if (i // 2) % 2 else (y + 9)) for i in range(20)]
            b += (f'<polyline points="{" ".join(f"{px},{py:.1f}" for px, py in pts)}" fill="none" '
                  f'stroke="{INK}" stroke-width="0.9"/>')
        elif pat == "cut":
            b += ln(x1, y + 6, x1 + 8, y + 6, INK, 2.0)
            b += ln(x2 - 8, y + 6, x2, y + 6, INK, 2.0)
            b += ln(x1 + 12, y + 6, x2 - 12, y + 6, INK, 0.9, "10 3 2 3")
        else:
            b += ln(x1, y + 6, x2, y + 6, INK, w, pat)
        b += text(114, y + 3, name, 7.6, anchor="start", color=BLUE, weight="bold")
        b += text(114, y + 13, use, 6.8, anchor="start", color=GREY)
        b += text(10, y + 3, thick, 5.6, anchor="start", color=THIN)
        y += 24
    b += foot(y + 10, "A hidden edge starts and ends with a dash, never with a gap.",
              "A centre line runs 2 to 3 mm past the outline on both sides.")
    return svg(360, y + 34, b)


# ------------------------------------------------------------------ 3. dimensioning
def dim():
    b = heading("One dimension, four parts", "plate 100 x 60, hole Ø 20, chamfer 45 x 5")
    ox0, oy0, ox1, oy1 = 78, 88, 268, 172      # the plate, 190 x 84 px = 100 x 60 mm
    b += (f'<path d="M{ox0} {oy0}L{ox1 - 18} {oy0}L{ox1} {oy0 + 18}L{ox1} {oy1}L{ox0} {oy1}Z" '
          f'fill="none" stroke="{INK}" stroke-width="2.0"/>')
    cx, cy, r = 116, 140, 15
    b += f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{INK}" stroke-width="2.0"/>'
    b += ln(cx - r - 6, cy, cx + r + 6, cy, BLUE, 0.8, "8 2 2 2")
    b += ln(cx, cy - r - 6, cx, cy + r + 6, BLUE, 0.8, "8 2 2 2")
    # horizontal overall 100
    b += ln(ox0, oy1 + 2, ox0, oy1 + 22, BLUE, 0.8)
    b += ln(ox1, oy1 + 2, ox1, oy1 + 22, BLUE, 0.8)
    b += arrow(ox0, oy1 + 16, ox1, oy1 + 16, BLUE, 0.9)
    b += f'<rect x="{ox0 + 88}" y="{oy1 + 10}" width="14" height="9" fill="#FFFFFF"/>'
    b += text((ox0 + ox1) / 2, oy1 + 12, "100", 7.6, color=BLUE, weight="bold")
    # vertical 60
    b += ln(ox0 - 2, oy0, ox0 - 22, oy0, BLUE, 0.8)
    b += ln(ox0 - 2, oy1, ox0 - 22, oy1, BLUE, 0.8)
    b += arrow(ox0 - 16, oy0, ox0 - 16, oy1, BLUE, 0.9)
    b += f'<rect x="{ox0 - 26}" y="{(oy0 + oy1) / 2 - 5}" width="17" height="10" fill="#FFFFFF"/>'
    b += text(ox0 - 17, (oy0 + oy1) / 2 + 2, "60", 7.6, color=BLUE, weight="bold")
    # diameter leader
    b += ln(cx + r * 0.72, cy - r * 0.72, 214, 66, BLUE, 0.8)
    b += ln(214, 66, 238, 66, BLUE, 0.8)
    b += text(240, 69, "Ø 20", 7.8, anchor="start", color=BLUE, weight="bold")
    # chamfer note
    b += ln(ox1 - 12, oy0 + 12, ox1 + 6, oy0 - 6, ORANGE, 0.8)
    b += ln(ox1 + 6, oy0 - 6, ox1 + 34, oy0 - 6, ORANGE, 0.8)
    b += text(ox1 + 36, oy0 - 3, "45 x 5", 7.8, anchor="start", color=ORANGE, weight="bold")
    b += f'<rect x="8" y="196" width="344" height="34" rx="5" fill="#F4F6F8" stroke="{THIN}" stroke-width="0.9"/>'
    b += text(180, 208, "extension line: 2 mm gap at the object, 3 mm past the arrow", 7.0, color=ORANGE)
    b += text(180, 220, "arrowhead 3 : 1 filled   |   figure 3 mm high, 1 mm above the line", 7.0, color=INK)
    b += foot(246, "Millimetres, no unit symbol; nothing dimensioned twice.",
              "Location dimensions from one datum, sizes once - and never on a hidden line.")
    return svg(360, 266, b)


# ------------------------------------------------------------------ 4. plain scale
def scale():
    b = heading("Six metres on 120 mm of paper", "RF = 1 : 50, reads metres and decimetres")
    px = 2.2                      # px per mm on paper
    x_left = 30.0                 # left end of the scale
    div = 20 * px                 # one metre = 20 mm on paper
    x_zero = x_left + div
    y_top, y_bot = 112, 126
    b += f'<rect x="{x_left}" y="{y_top}" width="{6 * div:.1f}" height="{y_bot - y_top}" fill="#FFFFFF" stroke="{INK}" stroke-width="1.1"/>'
    for k in range(7):
        x = x_left + k * div
        b += ln(x, y_top, x, y_bot, INK, 0.9)
    for k in range(1, 10):
        x = x_zero - k * div / 10
        b += ln(x, y_top, x, y_bot, INK, 0.6)
    for k in range(6):
        b += text(x_zero + k * div, y_top - 6, str(k), 7.6, color=INK, weight="bold")
    b += text(x_zero, y_bot + 13, "0", 7.6, color=RED, weight="bold")
    b += text(x_zero - 5 * div / 10, y_bot + 13, "0.5", 6.0, color=GREY)
    b += text(x_left + 2, y_bot + 13, "1.0", 5.8, anchor="start", color=GREY)
    b += text(x_zero + 2.6 * div, y_top - 15, "metres", 6.8, color=GREY)
    b += text(x_zero - div / 2, y_bot + 25, "ten parts of 2 mm = 0.1 m", 6.6, color=GREY)
    # a measured distance 3.7 m
    xa, xb = x_zero - 7 * div / 10, x_zero + 3 * div
    b += arrow(xa, y_top - 34, xb, y_top - 34, RED, 0.9)
    b += ln(xa, y_top - 38, xa, y_top - 30, RED, 0.8)
    b += ln(xb, y_top - 38, xb, y_top - 30, RED, 0.8)
    b += text((xa + xb) / 2, y_top - 40, "3.7 m = 74 mm", 7.4, color=RED, weight="bold")
    b += f'<rect x="8" y="52" width="344" height="24" rx="5" fill="#F4F6F8" stroke="{THIN}" stroke-width="0.9"/>'
    b += text(180, 62, "length of scale = (1/50) x 6000 mm = 120 mm", 7.6, color=INK, weight="bold")
    b += text(180, 71, "six parts of 20 mm = 1 m; the left part in ten of 2 mm = 1 dm", 7.0, color=GREY)
    b += foot(168, "A plain scale reads two units, because a 2 mm division is the finest that can be",
              "drawn and read. A diagonal scale splits that 2 mm again and reads a third unit.")
    return svg(360, 190, b)


# ------------------------------------------------------------------ 5. pentagon general method
def poly():
    b = heading("Any polygon, one construction", "pentagon in a circle of radius R")
    cx, cy, R = 180.0, 152.0, 70.0
    A, B = (cx, cy - R), (cx, cy + R)
    b += f'<circle cx="{cx}" cy="{cy}" r="{R}" fill="none" stroke="{THIN}" stroke-width="1.0"/>'
    b += ln(cx - 8, cy, cx + 8, cy, THIN, 0.8)
    b += ln(cx - R - 6, cy, cx + R + 6, cy, THIN, 0.8, "1 3")
    b += ln(A[0], A[1] - 8, B[0], B[1] + 8, THIN, 1.0)
    # five equal parts of the diameter
    step = 2 * R / 5
    for k in range(1, 5):
        y = A[1] + k * step
        b += ln(cx - 5, y, cx + 5, y, BLUE, 1.2)
    # arcs from A with radius = diameter
    cut = math.sqrt((2 * R) ** 2 - R ** 2)
    P, Q = (cx - cut, cy), (cx + cut, cy)
    b += (f'<path d="M{P[0]:.1f} {P[1]:.1f} A{2 * R} {2 * R} 0 0 0 {Q[0]:.1f} {Q[1]:.1f}" '
          f'fill="none" stroke="{ORANGE}" stroke-width="0.9" stroke-dasharray="5 3"/>')
    b += f'<circle cx="{P[0]}" cy="{P[1]}" r="2.2" fill="{ORANGE}"/>'
    b += f'<circle cx="{Q[0]}" cy="{Q[1]}" r="2.2" fill="{ORANGE}"/>'
    b += text(P[0] - 8, P[1] + 3, "P", 7.6, anchor="end", color=ORANGE, weight="bold")
    b += text(Q[0] + 8, Q[1] + 3, "Q", 7.6, anchor="start", color=ORANGE, weight="bold")
    # rays from P and Q through the second division point
    d2 = (cx, A[1] + 2 * step)
    b += ln(P[0], P[1], cx + 78, d2[1] - 6, RED, 0.9)
    b += ln(Q[0], Q[1], cx - 78, d2[1] - 6, RED, 0.9)
    b += f'<circle cx="{d2[0]}" cy="{d2[1]}" r="2.4" fill="{RED}"/>'
    b += text(d2[0] - 8, d2[1] - 3, "2", 7.2, anchor="end", color=RED, weight="bold")
    # the pentagon
    pts = []
    for k in range(5):
        ang = math.radians(-90 + 72 * k)
        pts.append((cx + R * math.cos(ang), cy + R * math.sin(ang)))
    b += (f'<path d="M{pts[0][0]:.1f} {pts[0][1]:.1f}' +
          "".join(f"L{px:.1f} {py:.1f}" for px, py in pts[1:]) + 'Z" fill="none" stroke="' + PURPLE +
          '" stroke-width="2.0"/>')
    b += text(pts[0][0], pts[0][1] - 8, "A", 7.6, color=PURPLE, weight="bold")
    b += text(pts[2][0] + 8, pts[2][1] + 10, "step CD five times", 6.8, anchor="start", color=PURPLE)
    b += text(180, 246, "1 circle and vertical diameter  >  2 divide it into n parts  >  "
                        "3 arcs from A, radius = diameter", 6.6, color=BLUE)
    b += text(180, 258, "4 rays P and Q through point 2 give C and D  >  5 step the chord CD "
                        "round the circle n times", 6.6, color=BLUE)
    b += foot(276, "The chord found is one side: it closes after exactly n steps round the circle.",
              "For a pentagon of 40 mm side the circle radius is 0.8507 x 40 = 34 mm.")
    return svg(360, 296, b)


# ------------------------------------------------------------------ 6. hexagon and octagon
def hexagon():
    b = heading("Two short cuts worth knowing", "hexagon R = side, octagon 0.414 a")
    # left: hexagon in a circle
    cx, cy, R = 92.0, 138.0, 56.0
    b += f'<circle cx="{cx}" cy="{cy}" r="{R}" fill="none" stroke="{THIN}" stroke-width="1.0"/>'
    b += ln(cx - 8, cy, cx + 8, cy, THIN, 0.8)
    b += ln(cx, cy - R - 8, cx, cy + R + 8, THIN, 0.8)
    hp = []
    for k in range(6):
        ang = math.radians(60 * k)
        hp.append((cx + R * math.cos(ang), cy - R * math.sin(ang)))
    b += (f'<path d="M{hp[0][0]:.1f} {hp[0][1]:.1f}' + "".join(f"L{a:.1f} {c:.1f}" for a, c in hp[1:])
          + 'Z" fill="none" stroke="%s" stroke-width="2.0"/>' % GREEN)
    b += arrow(cx, cy, hp[0][0], hp[0][1], GREEN, 0.9)
    b += text(cx + 32, cy + 4, "R", 7.6, color=GREEN, weight="bold")
    b += arrow(hp[1][0], hp[1][1], hp[2][0], hp[2][1], ORANGE, 0.9)
    b += text(hp[1][0] + 2, hp[1][1] - 8, "side = R", 7.0, anchor="end", color=ORANGE)
    b += text(cx, 62, "hexagon: step R six times", 7.4, color=GREEN, weight="bold")
    # right: octagon in a square
    ax, ay, a = 216.0, 88.0, 100.0
    b += f'<rect x="{ax}" y="{ay}" width="{a}" height="{a}" fill="none" stroke="{THIN}" stroke-width="1.0"/>'
    b += ln(ax, ay, ax + a, ay + a, THIN, 0.7, "4 3")
    b += ln(ax + a, ay, ax, ay + a, THIN, 0.7, "4 3")
    b += f'<circle cx="{ax + a / 2}" cy="{ay + a / 2}" r="{a / 2}" fill="none" stroke="{THIN}" stroke-width="0.8" stroke-dasharray="3 3"/>'
    t = 0.293 * a
    op = [(ax + t, ay), (ax + a - t, ay), (ax + a, ay + t), (ax + a, ay + a - t),
          (ax + a - t, ay + a), (ax + t, ay + a), (ax, ay + a - t), (ax, ay + t)]
    b += (f'<path d="M{op[0][0]:.1f} {op[0][1]:.1f}' + "".join(f"L{p:.1f} {q:.1f}" for p, q in op[1:])
          + 'Z" fill="none" stroke="%s" stroke-width="2.0"/>' % PURPLE)
    b += text(ax + a / 2, ay + a + 13, "side = 0.414 a", 7.0, color=PURPLE, weight="bold")
    b += text(ax + a / 2, 62, "octagon in a square", 7.4, color=PURPLE, weight="bold")
    b += foot(224, "60 degrees is a set-square edge, and the octagon corner is trimmed by 0.293 a",
              "on each side, so the side left is 0.414 a. Both close if nothing is re-set.")
    return svg(360, 244, b)


DIAGRAMS = {
    "u1_sheet": sheet,
    "u1_lines": lines,
    "u1_dim": dim,
    "u1_scale": scale,
    "u1_poly": poly,
    "u1_hex": hexagon,
}
