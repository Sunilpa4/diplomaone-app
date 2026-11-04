"""Six compact mobile SVGs for Engineering Mathematics (DI02000021) Unit 3: Integration."""
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
    "i1_family": "One slope, a family of curves",
    "i2_method": "Which integration method?",
    "i3_sub": "Substitution undoes the chain rule",
    "i4_parts": "Parts: split the product",
    "i5_definite": "A definite integral is an area",
    "i6_volume": "Spin the area to get a volume",
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


# ---------------------------------------------------------------- 1. family of curves
def family():
    b = heading("One slope, a family of curves", "∫ 2x dx = x² + c : every c has the same slope 2x")
    ox, oy, sx, sy = 56, 252, 100, 22

    def pt(x, y):
        return (ox + x * sx, oy - y * sy)

    b += line(f"M{ox} {oy} H336", INK, 1.2)
    b += line(f"M{ox} {oy} V84", INK, 1.2)
    b += text(330, oy - 8, "x", 10, color=INK, anchor="end")
    b += text(ox + 8, 92, "y", 10, color=INK, anchor="start")
    for c, col, lab in ((-1.0, RED, "c = −1"), (0.0, BLUE, "c = 0"), (1.6, GREEN, "c = 1.6")):
        pts = [pt(x / 20, (x / 20) ** 2 + c) for x in range(0, 45)]
        b += polyline([(px, min(oy - 2, py)) for px, py in pts], col, 2.0)
        lab_y = oy - (2.25 ** 2 + c) * sy + 4
        b += text(300, lab_y, lab, 9.4, color=col, anchor="start")
    b += rbox(180, 300, 330, 24, "the constant c is fixed only by a condition", BF, BLUE, 10.2)
    b += foot(334, "Different curves, identical slope at every x.",
              "That is why an indefinite integral ends with + c.")
    return svg(360, 372, b)


# ---------------------------------------------------------------- 2. method choice
def method():
    b = heading("Which integration method?", "look at the shape of the integrand first")
    b += rbox(180, 80, 300, 26, "can you write it as a standard form?", BF, BLUE, 10.4)
    b += arr([(180, 94), (180, 116)], GREY)
    b += rbox(180, 134, 300, 26, "no: does one part look like the derivative of another?", OF, ORANGE, 10.0)
    b += arr([(180, 148), (180, 170)], GREY)
    b += rbox(180, 188, 300, 26, "yes  →  substitution (u = that part)", GF, GREEN, 10.2)
    b += arr([(180, 202), (180, 224)], GREY)
    b += rbox(180, 242, 300, 26, "no: is it a product of unlike functions?", RF, RED, 10.2)
    b += arr([(180, 256), (180, 278)], GREY)
    b += rbox(180, 296, 300, 26, "yes  →  integration by parts (u dv)", RF, RED, 10.2)
    b += foot(332, "Always check by differentiating the answer.",
              "The result must give the original integrand back.")
    return svg(360, 366, b)


# ---------------------------------------------------------------- 3. substitution
def sub():
    b = heading("Substitution undoes the chain rule", "∫ 2x(x² + 1)³ dx  becomes  ∫ u³ du")
    b += rbox(180, 82, 330, 26, "let u = x² + 1  (the inside of the power)", BF, BLUE, 10.4)
    b += rbox(180, 122, 330, 26, "then du = 2x dx  - and 2x dx is already in the question", OF, ORANGE, 10.0)
    b += rbox(180, 162, 330, 26, "the integral is now  ∫ u³ du = u⁴/4 + c", GF, GREEN, 10.4)
    b += rbox(180, 202, 330, 26, "put u back:  (x² + 1)⁴/4 + c", GF, GREEN, 10.4)
    b += text(180, 236, "Check: differentiate the answer", 10.2, color=P, weight="bold")
    b += rbox(180, 264, 330, 24, "4(x² + 1)³/4 × 2x = 2x(x² + 1)³  ✓", BF, BLUE, 10.2)
    b += rbox(180, 304, 330, 24, "choose u so that du appears (or can be made to appear)", OF, ORANGE, 9.8)
    b += foot(340, "Substitution is the chain rule read backwards.",
              "Change the limits too when the integral is definite.")
    return svg(360, 368, b)


# ---------------------------------------------------------------- 4. parts
def parts():
    b = heading("Parts: split the product", "∫ u dv = uv − ∫ v du")
    b += rbox(180, 82, 330, 26, "pick u by LIATE: log, inverse trig, algebra, trig, exp", BF, BLUE, 9.8)
    b += text(180, 116, "worked example:  ∫ x eˣ dx", 10.6, color=P, weight="bold")
    b += rbox(180, 144, 330, 24, "u = x  →  du = dx", OF, ORANGE, 10.2)
    b += rbox(180, 176, 330, 24, "dv = eˣ dx  →  v = eˣ", GF, GREEN, 10.2)
    b += rbox(180, 212, 330, 26, "= x eˣ − ∫ eˣ dx  =  x eˣ − eˣ + c", GF, GREEN, 10.4)
    b += rbox(180, 252, 330, 26, "= eˣ (x − 1) + c", GF, GREEN, 10.4)
    b += rbox(180, 292, 330, 24, "choose u so that du is simpler than u", OF, ORANGE, 10.0)
    b += foot(326, "Differentiate the answer to check: eˣ(x − 1) + eˣ = x eˣ.")
    return svg(360, 344, b)


# ---------------------------------------------------------------- 5. definite integral
def definite():
    b = heading("A definite integral is an area", "area under y = f(x) from a to b is F(b) − F(a)")
    ox, oy, sx, sy = 58, 282, 80, 40

    def f(x):
        return 0.6 + 0.35 * x * x

    def pt(x, y):
        return (ox + x * sx, oy - y * sy)

    b += line(f"M{ox} {oy} H330", INK, 1.2)
    b += line(f"M{ox} {oy} V100", INK, 1.2)
    b += text(324, oy - 8, "x", 10, color=INK, anchor="end")
    b += text(ox + 8, 108, "y", 10, color=INK, anchor="start")
    x0, x1 = 1.0, 2.4
    shade = [(pt(x0, 0)[0], oy)]
    for k in range(25):
        x = x0 + (x1 - x0) * k / 24
        shade.append(pt(x, f(x)))
    shade.append((pt(x1, 0)[0], oy))
    b += ('<polygon points="' + " ".join(f"{x:.1f},{y:.1f}" for x, y in shade)
          + f'" fill="{BF}" stroke="{BLUE}" stroke-width="1.2"/>')
    curve = [pt(k / 20, f(k / 20)) for k in range(0, 66)]
    b += polyline(curve, BLUE, 2.2)
    b += text(112, 128, "y = f(x)", 9.8, color=BLUE, anchor="start")
    b += text(pt(x0, 0)[0], oy + 18, "a", 10.4, color=INK)
    b += text(pt(x1, 0)[0], oy + 18, "b", 10.4, color=INK)
    b += rbox(180, 322, 330, 24, "F(b) − F(a): no + c survives a definite integral", GF, GREEN, 9.6)
    b += foot(356, "The constant cancels: (F(b) + c) − (F(a) + c) = F(b) − F(a).")
    return svg(360, 374, b)


# ---------------------------------------------------------------- 6. volume
def volume():
    b = heading("Spin the area to get a volume", "rotating y = f(x) about the x-axis gives discs")
    ox, oy = 58, 250
    b += line(f"M{ox} {oy} H330", INK, 1.2)
    b += line(f"M{ox} {oy} V104", INK, 1.2)
    b += text(324, oy - 8, "x", 10, color=INK, anchor="end")
    b += text(ox + 8, 112, "y", 10, color=INK, anchor="start")
    profile = [(90 + k * 22, oy - (18 + k * 6)) for k in range(10)]
    b += polyline(profile, BLUE, 2.2)
    # one slice in side view: the upper half of the disc stands on the axis
    cx, r = 200, 40
    b += (f'<path d="M{cx - r} {oy} A{r} {r} 0 0 1 {cx + r} {oy} Z" fill="{OF}" fill-opacity="0.4" '
          f'stroke="{ORANGE}" stroke-width="1.8"/>')
    b += line(f"M{cx} {oy} V{oy - r}", RED, 1.4)
    b += text(cx + 6, oy - 12, "radius y", 9.4, color=RED, anchor="start")
    b += text(cx, oy + 18, "one slice", 9.2, color=ORANGE)
    b += text(96, oy + 16, "x = a", 9.2, color=GREY, anchor="start")
    b += text(292, oy + 16, "x = b", 9.2, color=GREY, anchor="start")
    b += rbox(180, 302, 336, 24, "each slice is a disc of radius y and thickness dx", BF, BLUE, 10.0)
    b += rbox(180, 338, 336, 26, "V = π ∫ y² dx  between a and b", GF, GREEN, 10.6)
    b += foot(368, "Square the radius, integrate, then multiply by π.")
    return svg(360, 384, b)


ALL = {
    "i1_family": family,
    "i2_method": method,
    "i3_sub": sub,
    "i4_parts": parts,
    "i5_definite": definite,
    "i6_volume": volume,
}
