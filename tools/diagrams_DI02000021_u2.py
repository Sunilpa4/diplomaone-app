"""Six compact mobile SVGs for Engineering Mathematics (DI02000021) Unit 2: Differentiation."""
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
    "d1_tangent": "From chord to tangent",
    "d2_rules": "The three working rules",
    "d3_chain": "Chain rule: one link at a time",
    "d4_logdiff": "Logarithmic differentiation for xˣ",
    "d5_sva": "Position, velocity, acceleration",
    "d6_maxmin": "Where the curve turns",
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


# ---------------------------------------------------------------- 1. tangent
def tangent():
    b = heading("From chord to tangent", "slope of PQ → slope of the tangent as Q slides to P")
    ox, oy, sx, sy = 52, 286, 104, 48

    def pt(x, y):
        return (ox + x * sx, oy - y * sy)

    curve = [pt(x / 20, (x / 20) ** 2) for x in range(0, 41)]
    b += line(f"M{ox} {oy} H332", INK, 1.3)
    b += line(f"M{ox} {oy} V76", INK, 1.3)
    b += text(326, oy - 8, "x", 10, color=INK, anchor="end")
    b += text(ox + 8, 84, "y", 10, color=INK, anchor="start")
    b += polyline(curve, BLUE, 2.2)

    px, py = pt(1, 1)
    qx, qy = pt(1.6, 2.56)
    b += line(f"M{px:.1f} {py:.1f} L{qx:.1f} {qy:.1f}", ORANGE, 1.8, dash="5 3")
    b += f'<circle cx="{px:.1f}" cy="{py:.1f}" r="4" fill="{RED}"/>'
    b += f'<circle cx="{qx:.1f}" cy="{qy:.1f}" r="4" fill="{ORANGE}"/>'
    b += text(px - 44, py - 8, "P(1, 1)", 9.4, color=RED, anchor="end")
    b += text(qx + 8, qy - 6, "Q", 9.6, color=ORANGE, anchor="start")
    t1, t2 = pt(0.55, 2 * 0.55 - 1), pt(1.55, 2 * 1.55 - 1)
    b += line(f"M{t1[0]:.1f} {t1[1]:.1f} L{t2[0]:.1f} {t2[1]:.1f}", GREEN, 2.2)
    b += text(60, 246, "tangent: slope 2", 9.4, color=GREEN, anchor="start")
    b += text(238, 152, "chord PQ: slope 2.6", 9.2, color=ORANGE, anchor="start")
    b += rbox(180, 320, 330, 24, "dy/dx = limit of Δy/Δx as Δx → 0", BF, BLUE, 10.4)
    b += foot(354, "The derivative is the slope of the tangent at a point.")
    return svg(360, 372, b)


# ---------------------------------------------------------------- 2. rules
def rules():
    b = heading("The three working rules", "differentiate part by part, then combine")
    b += rbox(180, 82, 330, 26, "sum / difference:   (u ± v)′ = u′ ± v′", BF, BLUE, 10.4)
    b += rbox(180, 124, 330, 26, "product:   (uv)′ = u′v + uv′", GF, GREEN, 10.4)
    b += rbox(180, 166, 330, 26, "quotient:   (u/v)′ = (u′v − uv′)/v²", RF, RED, 10.4)
    b += text(180, 202, "u and v are both functions of x", 10, color=GREY)
    b += text(180, 236, "Take the product rule apart", 10.6, color=P, weight="bold")
    b += rbox(180, 262, 330, 24, "y = x²(3x + 5)  →  u = x²,  v = 3x + 5", OF, ORANGE, 10.2)
    b += text(180, 296, "u′v + uv′ = 2x(3x + 5) + x²(3) = 9x² + 10x", 10.4, color="#7B1030", weight="bold")
    b += rbox(180, 330, 330, 24, "power rule first:  (xⁿ)′ = n xⁿ⁻¹", BF, BLUE, 10.4)
    b += foot(360, "Never multiply the derivatives: (uv)′ is not u′v′.")
    return svg(360, 378, b)


# ---------------------------------------------------------------- 3. chain
def chain():
    b = heading("Chain rule: one link at a time", "y = (3x + 2)⁵ is a function of a function")
    b += rbox(46, 96, 62, 34, "x", BF, BLUE, 11.4)
    b += rbox(188, 96, 150, 34, "u = 3x + 2", OF, ORANGE, 10.8)
    b += rbox(316, 96, 62, 34, "y = u⁵", GF, GREEN, 10.8)
    b += arr([(82, 96), (108, 96)], GREY)
    b += arr([(268, 96), (280, 96)], GREY)
    b += text(188, 132, "inside", 9, color=ORANGE)
    b += text(316, 132, "outside", 9, color=GREEN)
    b += text(180, 162, "dy/dx = dy/du  ×  du/dx", 12, color=P, weight="bold")
    b += rbox(180, 196, 330, 24, "dy/du = 5u⁴    and    du/dx = 3", BF, BLUE, 10.4)
    b += rbox(180, 236, 330, 26, "dy/dx = 5u⁴ × 3 = 15(3x + 2)⁴", GF, GREEN, 10.6)
    b += text(180, 272, "Put u back before you finish.", 10, color=GREY)
    b += rbox(180, 306, 330, 24, "log(sin x) → (1/sin x)·cos x = cot x", OF, ORANGE, 10.2)
    b += foot(340, "Differentiate the outside, then multiply by the inside.",
              "Each extra layer adds one more factor.")
    return svg(360, 372, b)


# ---------------------------------------------------------------- 4. log differentiation
def logdiff():
    b = heading("Logarithmic differentiation for xˣ", "a variable in the power needs a logarithm first")
    b += text(180, 78, "y = xˣ", 13, color=P, weight="bold")
    b += rbox(180, 112, 330, 24, "1. take log of both sides:  log y = x log x", BF, BLUE, 10.2)
    b += rbox(180, 150, 330, 24, "2. differentiate:  (1/y)·dy/dx = x·(1/x) + log x·1", BF, BLUE, 10.2)
    b += rbox(180, 188, 330, 24, "3. tidy the right side: 1 + log x", OF, ORANGE, 10.2)
    b += rbox(180, 228, 330, 26, "dy/dx = y (1 + log x) = xˣ (1 + log x)", GF, GREEN, 10.4)
    b += text(180, 264, "Use it when the power also contains x", 10, color=GREY)
    b += rbox(180, 300, 330, 24, "xˣ is not xⁿ and not aˣ - it needs this method", RF, RED, 10.0)
    b += foot(334, "Take the log, differentiate both sides, then multiply by y.",
              "The same trick handles (1 + x)ˣ and x^(sin x).")
    return svg(360, 368, b)


# ---------------------------------------------------------------- 5. s, v, a
def sva():
    b = heading("Position, velocity, acceleration", "s = t³ − 6t² + 8t  gives  v = s′  and  a = v′")
    b += rbox(180, 86, 330, 28, "position:  s = t³ − 6t² + 8t", BF, BLUE, 10.6)
    b += arr([(180, 104), (180, 130)], GREY)
    b += text(258, 118, "differentiate", 9.4, color=GREY, anchor="start")
    b += rbox(180, 148, 330, 28, "velocity:  v = ds/dt = 3t² − 12t + 8", GF, GREEN, 10.6)
    b += arr([(180, 166), (180, 192)], GREY)
    b += text(258, 180, "differentiate again", 9.4, color=GREY, anchor="start")
    b += rbox(180, 210, 330, 28, "acceleration:  a = dv/dt = 6t − 12", OF, ORANGE, 10.6)
    b += rbox(180, 262, 336, 26, "at t = 3:  v = 27 − 36 + 8 = −1,  a = 18 − 12 = 6", BF, BLUE, 10.2)
    b += rbox(180, 306, 336, 26, "v = 0 → at rest;  a < 0 → slowing down", RF, RED, 10.0)
    b += foot(340, "Differentiate position to get velocity, then again for acceleration.",
              "Units: metres, metres per second, metres per second squared.")
    return svg(360, 376, b)


# ---------------------------------------------------------------- 6. max / min
def maxmin():
    b = heading("Where the curve turns", "y = x³ − 3x + 2 has a maximum and a minimum")
    ox, oy, sx, sy = 180, 262, 52, 32

    def pt(x, y):
        return (ox + x * sx, oy - y * sy)

    pts = []
    x = -2.0
    while x <= 2.06:
        y = x ** 3 - 3 * x + 2
        if y >= -0.05:
            pts.append(pt(x, y))
        x += 0.05
    b += line("M28 262 H332", INK, 1.2)
    b += line(f"M{ox} 84 V280", INK, 1.2)
    b += polyline(pts, BLUE, 2.2)
    mx, my = pt(-1, 4)
    nx, ny = pt(1, 0)
    b += f'<circle cx="{mx:.1f}" cy="{my:.1f}" r="4.2" fill="{RED}"/>'
    b += f'<circle cx="{nx:.1f}" cy="{ny:.1f}" r="4.2" fill="{GREEN}"/>'
    b += text(mx - 10, my - 10, "maximum at x = −1", 9.4, color=RED, anchor="end")
    b += text(nx + 10, ny + 20, "minimum at x = 1", 9.4, color=GREEN, anchor="start")
    b += rbox(180, 314, 330, 24, "stationary points come from f′(x) = 0", BF, BLUE, 10.2)
    b += rbox(180, 348, 330, 24, "f″ < 0 → maximum,   f″ > 0 → minimum", OF, ORANGE, 10.2)
    b += foot(378, "A zero slope alone is not enough: the second derivative decides.")
    return svg(360, 394, b)


ALL = {
    "d1_tangent": tangent,
    "d2_rules": rules,
    "d3_chain": chain,
    "d4_logdiff": logdiff,
    "d5_sva": sva,
    "d6_maxmin": maxmin,
}
