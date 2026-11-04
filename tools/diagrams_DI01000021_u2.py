"""Eight compact mobile SVGs for Mathematics-I Unit 2 (Trigonometry)."""
import math

from flowchart_lib import svg, text, arr, rbox, line, P

BLUE, BF = "#1565C0", "#EAF3FD"
GREEN, GF = "#2E7D32", "#EAF6EC"
ORANGE, OF = "#B66A00", "#FFF4DF"
RED, RF = "#BD2543", "#FDECF0"
GREY = "#666"

TITLES = {
    "t1_deg_rad": "Degrees and radians on one circle",
    "t2_quadrants": "ASTC: which functions are positive",
    "t3_allied": "Allied angles: sign first, then the value",
    "t4_compound": "Compound angles: two terms each",
    "t5_double": "Double angle from one triangle",
    "t6_sincos": "Graphs of sine and cosine",
    "t7_sumprod": "Sum and product formulae",
    "t8_inverse": "Principal ranges of the inverses",
}


def heading(t, sub=None):
    body = text(180, 24, t, 14, weight="bold", color=P)
    if sub:
        body += text(180, 46, sub, 10.5, color=GREY)
    return body


def foot(y, *lines):
    return "".join(text(180, y + 16 * i, s, 10.2, color=GREY) for i, s in enumerate(lines))


def _pt(cx, cy, r, deg):
    a = math.radians(deg)
    return cx + r * math.cos(a), cy - r * math.sin(a)


# ---------------------------------------------------------------- 1. degrees and radians
def deg_rad():
    b = heading("Degrees and radians on one circle", "π radians = 180°, one full turn = 2π")
    cx, cy, r = 150, 170, 78
    b += f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="#FCFCFD" stroke="#333" stroke-width="1.6"/>'
    b += line(f"M{cx-r-14} {cy} H{cx+r+16}", "#999", 1.2, dash="4 3")
    b += line(f"M{cx} {cy-r-14} V{cy+r+14}", "#999", 1.2, dash="4 3")
    marks = [(0, "0°", "0"), (90, "90°", "π/2"), (180, "180°", "π"), (270, "270°", "3π/2")]
    for deg, dlabel, rlabel in marks:
        x, y = _pt(cx, cy, r, deg)
        b += f'<circle cx="{x:.1f}" cy="{y:.1f}" r="3.4" fill="{P}"/>'
        lx, ly = _pt(cx, cy, r + 26, deg)
        b += text(lx, ly + 4, dlabel, 10, color="#222", weight="bold")
        rx, ry = _pt(cx, cy, r - 26, deg)
        b += text(rx, ry + 4, rlabel, 10, color=BLUE)
    b += line(f"M{cx} {cy} L{cx+r*math.cos(math.radians(30)):.1f} {cy-r*math.sin(math.radians(30)):.1f}", ORANGE, 1.8)
    b += text(cx + 50, cy - 26, "θ", 11, color=ORANGE, weight="bold")
    b += rbox(150, 302, 300, 30, "radians = degrees × π/180", BF, BLUE, 11.6)
    b += foot(342, "Degrees sit outside the circle, radians inside.", "1 radian ≈ 57.3°.")
    return svg(360, 380, b)


# ---------------------------------------------------------------- 2. ASTC
def quadrants():
    b = heading("ASTC: which functions are positive", "All · Silver · Tea · Cups, anticlockwise")
    cx, cy, r = 180, 168, 78
    b += f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="#FFFFFF" stroke="#D9D2E6" stroke-width="1.2"/>'
    b += line(f"M{cx-r-16} {cy} H{cx+r+16}", "#333", 1.5)
    b += line(f"M{cx} {cy-r-16} V{cy+r+16}", "#333", 1.5)
    quads = [(45, "I", "A", "all six positive", GF, GREEN),
             (135, "II", "S", "sin, cosec", BF, BLUE),
             (225, "III", "T", "tan, cot", OF, ORANGE),
             (315, "IV", "C", "cos, sec", RF, RED)]
    for deg, num, letter, detail, fill, stroke in quads:
        x, y = _pt(cx, cy, r * 0.55, deg)
        b += f'<circle cx="{x:.1f}" cy="{y:.1f}" r="26" fill="{fill}" stroke="{stroke}" stroke-width="1.3"/>'
        b += text(x, y - 2, letter, 17, weight="bold", color=stroke)
        b += text(x, y + 14, num, 8.6, color=stroke)
    b += text(180, 286, "A all  ·  S sin  ·  T tan  ·  C cos", 10.6, weight="bold", color="#333")
    b += text(180, 303, "sin, cosec in II · tan, cot in III · cos, sec in IV", 9.4, color=GREY)
    b += foot(328, "x negative on the left, y negative below the axis.",
              "The ratio of two negatives is positive - that is why tan wins in Q III.")
    return svg(360, 366, b)


# ---------------------------------------------------------------- 3. allied angles
def allied():
    b = heading("Allied angles: sign first, then value", "Even multiple of 90° keeps the name")
    rows = [("sin(180° − θ) =  sin θ", GF, GREEN, "Q II, sine positive"),
            ("cos(180° − θ) = −cos θ", RF, RED, "Q II, cosine negative"),
            ("sin(180° + θ) = −sin θ", RF, RED, "Q III, sine negative"),
            ("tan(360° − θ) = −tan θ", RF, RED, "Q IV, tangent negative"),
            ("cos(−θ)      =  cos θ", GF, GREEN, "cosine is even")]
    y = 66
    for law, fill, stroke, note in rows:
        b += f'<rect x="16" y="{y}" width="328" height="44" rx="7" fill="{fill}" stroke="{stroke}" stroke-width="1.4"/>'
        b += text(26, y + 20, law, 12.2, color="#222", anchor="start")
        b += text(334, y + 20, note, 8.8, color=GREY, anchor="end")
        y += 52
    b += foot(y + 4, "For 90° and 270° the function also changes: sin ↔ cos.",
              "Worked example: sin 150° = sin 30° = 1/2.")
    return svg(360, y + 58, b)


# ---------------------------------------------------------------- 4. compound
def compound():
    b = heading("Compound angles: two terms each", "Known angles replace an unknown one")
    b += rbox(180, 70, 300, 30, "75°  =  45° + 30°", "#F4F4F4", "#999", 11.4, color="#333")
    b += arr([(180, 85), (180, 106)], P)
    b += rbox(180, 124, 300, 32, "sin(A + B)", BF, BLUE, 12.4, weight="bold", color=BLUE)
    b += arr([(150, 140), (106, 164)], "#333")
    b += arr([(210, 140), (254, 164)], "#333")
    b += rbox(96, 182, 150, 32, "sin A cos B", GF, GREEN, 11.2)
    b += text(180, 187, "+", 14, weight="bold", color="#333")
    b += rbox(264, 182, 150, 32, "cos A sin B", OF, ORANGE, 11.2)
    b += rbox(180, 232, 300, 30, "cos(A + B) = cos A cos B − sin A sin B", RF, RED, 10.8)
    b += rbox(180, 276, 300, 30, "tan(A + B) = (tan A + tan B)/(1 − tan A tan B)", "#F6F2FB", P, 10.2)
    b += foot(320, "Sine keeps the sign of the bracket; cosine flips it.",
              "Check: sin 75° = (√6 + √2)/4 ≈ 0.966.")
    return svg(360, 358, b)


# ---------------------------------------------------------------- 5. double angle
def double():
    b = heading("Double angle from one triangle", "Put B = A in the compound formulae")
    b += rbox(180, 72, 240, 34, "sin A = 3/5,  cos A = 4/5", BF, BLUE, 11.4)
    b += arr([(150, 90), (110, 116)], "#333")
    b += arr([(210, 90), (250, 116)], "#333")
    b += rbox(106, 134, 144, 34, "sin 2A = 2 sin A cos A", GF, GREEN, 10.2)
    b += rbox(254, 134, 144, 34, "cos 2A = 1 − 2 sin²A", OF, ORANGE, 10.2)
    b += arr([(106, 152), (106, 176)], "#333")
    b += arr([(254, 152), (254, 176)], "#333")
    b += rbox(106, 194, 144, 30, "= 24/25", GF, GREEN, 12, weight="bold", color="#1B5E20")
    b += rbox(254, 194, 144, 30, "= 7/25", OF, ORANGE, 12, weight="bold", color=ORANGE)
    b += rbox(180, 244, 320, 30, "check: (24/25)² + (7/25)² = 1", "#F4F4F4", "#999", 10.6, color="#333")
    b += foot(288, "Three forms of cos 2A: cos²A − sin²A, 2cos²A − 1, 1 − 2sin²A.",
              "Pick the form that uses what the question gives you.")
    return svg(360, 326, b)


# ---------------------------------------------------------------- 6. sine and cosine
def sincos():
    b = heading("Graphs of sine and cosine", "Same wave, shifted by 90°")
    ox, oy, ux, uy = 48, 198, 140 / math.pi, 34.0

    def X(v):
        return ox + v * ux

    def Y(v):
        return oy - v * uy

    b += line(f"M24 {oy} H340", "#333", 1.5)
    b += f'<polygon points="346,{oy} 336,{oy-4} 336,{oy+4}" fill="#333"/>'
    b += line(f"M{ox} 134 V{oy+42}", "#333", 1.5)
    b += text(330, oy - 12, "x", 10.5, color="#333", anchor="end")
    b += text(ox - 8, 140, "y", 10.5, color="#333", anchor="end")
    b += line(f"M{ox} {Y(1):.1f} H{X(2*math.pi):.1f}", "#CFCFCF", 0.9, dash="4 3")
    b += line(f"M{ox} {Y(-1):.1f} H{X(2*math.pi):.1f}", "#CFCFCF", 0.9, dash="4 3")
    b += text(X(0) - 8, Y(1) + 3, "1", 9, color="#777", anchor="end")
    b += text(X(0) - 8, Y(-1) + 3, "−1", 9, color="#777", anchor="end")
    for k, lab in ((0.5, "π/2"), (1, "π"), (1.5, "3π/2"), (2, "2π")):
        x = X(k * math.pi)
        b += line(f"M{x:.1f} {oy-4} V{oy+4}", "#333", 1.2)
        b += text(x, oy + 19, lab, 9.6, color="#333")
    for fn, color, width in ((math.sin, BLUE, 2.2), (math.cos, GREEN, 2.0)):
        pts = []
        for i in range(97):
            v = 2 * math.pi * i / 96
            pts.append(f"{X(v):.1f} {Y(fn(v)):.1f}")
        b += f'<polyline points="{" ".join(pts)}" fill="none" stroke="{color}" stroke-width="{width}"/>'
    b += rbox(180, 268, 320, 26, "sin x starts at 0   ·   cos x starts at 1", BF, BLUE, 10.2)
    b += foot(310, "Both have period 2π and amplitude 1.",
              "cos x = sin(x + 90°): the cosine leads by a quarter turn.")
    return svg(360, 350, b)


# ---------------------------------------------------------------- 7. sum and product
def sumprod():
    b = heading("Sum and product formulae", "Two directions, one derivation")
    b += rbox(180, 70, 300, 30, "add  sin(A+B) and sin(A−B)", "#F4F4F4", "#999", 10.6, color="#333")
    b += arr([(180, 85), (180, 106)], P)
    b += rbox(180, 124, 320, 30, "sin A cos B = ½[sin(A+B) + sin(A−B)]", BF, BLUE, 10.4)
    b += arr([(180, 139), (180, 160)], P)
    b += rbox(180, 178, 320, 30, "2 sin A cos B = sin(A+B) + sin(A−B)", GF, GREEN, 10.4)
    b += arr([(180, 193), (180, 214)], P)
    b += rbox(180, 232, 320, 30, "sin C + sin D = 2 sin((C+D)/2) cos((C−D)/2)", OF, ORANGE, 9.8)
    b += rbox(180, 286, 320, 34, "cos C + cos D = 2 cos((C+D)/2) cos((C−D)/2)", RF, RED, 9.8)
    b += foot(336, "cos C − cos D carries a leading minus.", "Use these to cancel common factors in simplification.")
    return svg(360, 376, b)


# ---------------------------------------------------------------- 8. inverse ranges
def inverse():
    b = heading("Principal ranges of the inverses", "The range is what makes the inverse a function")
    rows = [("sin⁻¹ x", 92, 100, 280, [("−π/2", 100), ("0", 190), ("π/2", 280)], BF, BLUE),
            ("cos⁻¹ x", 148, 100, 280, [("0", 100), ("π/2", 190), ("π", 280)], GF, GREEN),
            ("tan⁻¹ x", 204, 100, 280, [("−π/2", 100), ("0", 190), ("π/2", 280)], OF, ORANGE)]
    for name, y, x1, x2, ticks, fill, stroke in rows:
        b += text(24, y + 4, name, 11.4, weight="bold", color=stroke, anchor="start")
        b += f'<rect x="{x1}" y="{y-8}" width="{x2-x1}" height="18" rx="9" fill="{fill}" stroke="{stroke}" stroke-width="1.4"/>'
        for lab, tx in ticks:
            b += line(f"M{tx} {y-10} V{y+12}", stroke, 1.2)
            b += text(tx, y + 24, lab, 9.2, color=GREY)
        b += text(x1 - 8, y + 4, "", 9)
    b += foot(258, "Endpoints: sin⁻¹ and tan⁻¹ include −π/2, π/2 (tan⁻¹ open).",
              "cos⁻¹ is the only one whose range starts at 0, so cos⁻¹(−x) > π/2.")
    return svg(360, 302, b)


ALL = {
    "t1_deg_rad": deg_rad,
    "t2_quadrants": quadrants,
    "t3_allied": allied,
    "t4_compound": compound,
    "t5_double": double,
    "t6_sincos": sincos,
    "t7_sumprod": sumprod,
    "t8_inverse": inverse,
}
