"""Five compact mobile SVGs for Engineering Mathematics (DI02000021) Unit 5: Complex Numbers."""
import math

from flowchart_lib import svg, text, arr, rbox, line, P

BLUE, BF = "#1565C0", "#EAF3FD"
GREEN, GF = "#2E7D32", "#EAF6EC"
ORANGE, OF = "#B66A00", "#FFF4DF"
RED, RF = "#BD2543", "#FDECF0"
PURPLE = "#7B2CD9"
GREY = "#666"
INK = "#333"

TITLES = {
    "n1_argand": "The Argand diagram",
    "n2_arg": "The argument depends on the quadrant",
    "n3_polar": "Polar form: multiply or rotate",
    "n4_unity": "The three cube roots of unity",
    "n5_demoivre": "De Moivre in four lines",
}


def heading(t, sub=None):
    body = text(180, 24, t, 14, weight="bold", color=P)
    if sub:
        body += text(180, 46, sub, 10.4, color=GREY)
    return body


def foot(y, *lines):
    return "".join(text(180, y + 16 * i, s, 10.2, color=GREY) for i, s in enumerate(lines))


def polyline(pts, color, w=2.1, dash=None):
    d = "M" + " L".join(f"{x:.1f} {y:.1f}" for x, y in pts)
    return line(d, color, w, dash=dash)


def arc(cx, cy, r, a0, a1, color, w=1.4):
    x0, y0 = cx + r * math.cos(a0), cy - r * math.sin(a0)
    x1, y1 = cx + r * math.cos(a1), cy - r * math.sin(a1)
    large = 1 if abs(a1 - a0) > math.pi else 0
    sweep = 1 if a1 > a0 else 0
    return line(f"M{x0:.1f} {y0:.1f} A{r} {r} 0 {large} {sweep} {x1:.1f} {y1:.1f}", color, w)


# ---------------------------------------------------------------- 1. Argand diagram
def argand():
    b = heading("The Argand diagram", "a + ib is the point (a, b)")
    ox, oy, u = 150, 250, 20

    def pt(a, bi):
        return (ox + a * u, oy - bi * u)

    b += line(f"M40 {oy} H330", INK, 1.2)
    b += line(f"M{ox} {oy + 10} V100", INK, 1.2)
    b += text(324, oy - 8, "real", 9.6, color=INK, anchor="end")
    b += text(ox + 8, 108, "imaginary", 9.6, color=INK, anchor="start")
    for a, bi, col, lab in ((3, 4, BLUE, "3 + 4i"), (-2, 2, GREEN, "−2 + 2i")):
        px, py = pt(a, bi)
        b += line(f"M{ox} {oy} L{px:.1f} {py:.1f}", col, 2.0)
        b += line(f"M{ox} {oy} L{px:.1f} {oy} M{px:.1f} {oy} L{px:.1f} {py:.1f}", col, 1.0,
                  dash="3 3")
        b += f'<circle cx="{px:.1f}" cy="{py:.1f}" r="3.6" fill="{col}"/>'
        if a > 0:
            b += text(px + 8, py - 6, lab, 9.4, color=col, anchor="start")
        else:
            b += text(px - 9, py + 2, lab, 9.4, color=col, anchor="end")
    px, py = pt(3, 4)
    b += text(172, 178, "r = |z| = 5", 9.4, color=BLUE, anchor="end")
    b += arc(ox, oy, 62, 0, math.atan2(4, 3), ORANGE)
    b += text(ox + 68, oy - 18, "θ", 10.4, color=ORANGE, anchor="start")
    b += rbox(180, 296, 336, 24, "z = a + ib : a is real, b is imaginary", BF, BLUE, 10.2)
    b += rbox(180, 332, 336, 24, "|z| = √(a² + b²) is the distance from the origin", GF, GREEN, 9.8)
    b += foot(364, "Multiply by i and the point turns 90° anticlockwise.")
    return svg(360, 386, b)


# ---------------------------------------------------------------- 2. argument
def argument():
    b = heading("The argument depends on the quadrant", "θ = tan⁻¹(b/a), fixed by where z lies")
    ox, oy, s = 180, 200, 58
    b += (f'<rect x="{ox - s}" y="{oy - s}" width="{2 * s}" height="{2 * s}" fill="{BF}" '
          f'stroke="{BLUE}" stroke-width="1.0" stroke-dasharray="4 4"/>')
    b += line(f"M{ox - 92} {oy} H{ox + 92}", INK, 1.2)
    b += line(f"M{ox} {oy - 92} V{oy + 92}", INK, 1.2)
    labels = (("Q2", "π − α", ox - 32, oy - 36), ("Q1", "α", ox + 32, oy - 36),
              ("Q3", "−(π − α)", ox - 34, oy + 28), ("Q4", "−α", ox + 32, oy + 28))
    for tag, expr, x, y in labels:
        b += text(x, y, tag, 10.0, color=PURPLE, weight="bold")
        b += text(x, y + 16, expr, 9.6, color=INK)
    b += text(ox + 84, oy - 7, "real", 9.0, color=GREY, anchor="end")
    b += text(ox + 7, oy - 82, "imag", 9.0, color=GREY, anchor="start")
    b += text(180, 306, "α = tan⁻¹|b/a| is the angle from the real axis", 9.8, color=GREY)
    b += rbox(180, 336, 336, 24, "Q1 and Q4 give α directly; Q2 and Q3 need a sign fix", OF, ORANGE,
              9.6)
    b += foot(368, "Always draw the point before writing the argument.")
    return svg(360, 390, b)


# ---------------------------------------------------------------- 3. polar form
def polar():
    b = heading("Polar form: multiply or rotate", "z = r(cos θ + i sin θ) = r cis θ")
    b += rbox(180, 82, 336, 26, "r = |z|  and  θ = arg z", BF, BLUE, 10.4)
    b += arr([(180, 95), (180, 117)], GREY)
    b += rbox(180, 136, 336, 26, "multiply: moduli multiply, arguments add", GF, GREEN, 10.0)
    b += rbox(180, 172, 336, 26, "r₁ cis θ₁ × r₂ cis θ₂ = r₁r₂ cis (θ₁ + θ₂)", GF, GREEN, 9.8)
    b += arr([(180, 185), (180, 207)], GREY)
    b += rbox(180, 226, 336, 26, "divide: moduli divide, arguments subtract", OF, ORANGE, 10.0)
    b += rbox(180, 262, 336, 26, "(r₁/r₂) cis (θ₁ − θ₂)", OF, ORANGE, 10.0)
    b += arr([(180, 275), (180, 297)], GREY)
    b += rbox(180, 316, 336, 26, "De Moivre: (r cis θ)ⁿ = rⁿ cis (nθ)", RF, RED, 10.2)
    b += foot(356, "Trig form and cis form are the same statement.",
              "Keep θ in radians when nθ is substituted back.")
    return svg(360, 390, b)


# ---------------------------------------------------------------- 4. cube roots of unity
def unity():
    b = heading("The three cube roots of unity", "z³ = 1 has exactly three roots")
    cx, cy, r = 180, 188, 64
    b += f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{BLUE}" stroke-width="1.2" ' \
         f'stroke-dasharray="4 4"/>'
    b += line(f"M{cx - r - 22} {cy} H{cx + r + 22}", INK, 1.1)
    b += line(f"M{cx} {cy - r - 22} V{cy + r + 22}", INK, 1.1)
    for ang, col, lab, dx, dy, anc in ((0, GREEN, "1", 9, -11, "start"),
                                       (2 * math.pi / 3, BLUE, "ω", -9, -2, "end"),
                                       (4 * math.pi / 3, ORANGE, "ω²", -9, 3, "end")):
        px, py = cx + r * math.cos(ang), cy - r * math.sin(ang)
        b += line(f"M{cx} {cy} L{px:.1f} {py:.1f}", col, 1.8)
        b += f'<circle cx="{px:.1f}" cy="{py:.1f}" r="4" fill="{col}"/>'
        b += text(px + dx, py + dy, lab, 11.0, color=col, weight="bold", anchor=anc)
    b += rbox(180, 286, 336, 24, "ω = −1/2 + i√3/2 ,  ω² = −1/2 − i√3/2", BF, BLUE, 9.8)
    b += rbox(180, 322, 336, 24, "1 + ω + ω² = 0   and   ω³ = 1", GF, GREEN, 10.2)
    b += foot(354, "Every cube root of 1 sits on the unit circle, 120° apart.")
    return svg(360, 376, b)


# ---------------------------------------------------------------- 5. De Moivre routine
def demoivre():
    b = heading("De Moivre in four lines", "worked: z = 1 + i√3, find z⁶")
    b += rbox(180, 82, 336, 26, "step 1: r = √(1 + 3) = 2", BF, BLUE, 10.2)
    b += arr([(180, 95), (180, 117)], GREY)
    b += rbox(180, 136, 336, 26, "step 2: θ = tan⁻¹(√3/1) = π/3 (first quadrant)", BF, BLUE, 9.6)
    b += arr([(180, 149), (180, 171)], GREY)
    b += rbox(180, 190, 336, 26, "step 3: z = 2 cis (π/3)", GF, GREEN, 10.4)
    b += arr([(180, 203), (180, 225)], GREY)
    b += rbox(180, 244, 336, 28, "step 4: z⁶ = 2⁶ cis (6 × π/3) = 64 cis 2π", GF, GREEN, 10.0)
    b += rbox(180, 286, 336, 24, "= 64 (cos 2π + i sin 2π) = 64", OF, ORANGE, 10.2)
    b += rbox(180, 322, 336, 24, "final answer is real - the argument completed a full turn", RF, RED,
              9.4)
    b += foot(354, "Modulus to the power, argument times the power.",
              "Reduce the angle to its principal value before the final answer.")
    return svg(360, 376, b)


ALL = {
    "n1_argand": argand,
    "n2_arg": argument,
    "n3_polar": polar,
    "n4_unity": unity,
    "n5_demoivre": demoivre,
}
