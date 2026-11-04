"""Five compact mobile SVGs for Applied Physics (DI01000121) Unit 2: circular motion.

English labels, 360 px canvas, plain rect/path/text only (same rules as Unit 1).
"""
from flowchart_lib import svg, text, rbox, P
from diagrams_DI01000121_u1 import ln, down, heading as _heading, foot as _foot, INK, GREY, \
    BLUE, BF, GREEN, GF, ORANGE, OF, RED, RF, PURPLE, PF

TITLES = {
    "u2_momentum": "Momentum before and after a collision",
    "u2_recoil": "Recoil of a gun: total momentum stays zero",
    "u2_angular": "Angular displacement, velocity and acceleration",
    "u2_centripetal": "Centripetal force points at the centre",
    "u2_banking": "Why a banked road holds a fast car",
}

TITLES_GU = {
    "u2_momentum": "અથડામણ પહેલાં અને પછીનું વેગમાન",
    "u2_recoil": "બંદૂકનો રીકોઇલ: કુલ વેગમાન શૂન્ય જ રહે",
    "u2_angular": "કોણીય સ્થાનાંતરણ, વેગ અને પ્રવર્ગ",
    "u2_centripetal": "કેન્દ્રગામી બળ કેન્દ્ર તરફ હોય",
    "u2_banking": "બેન્ક કરેલો રસ્તો ઝડપી કારને કેમ સંભાળે",
}

CAPTIONS = {
    "u2_momentum": "Two trolleys: momentum is conserved, energy is not.",
    "u2_recoil": "A 20 g bullet at 400 m/s gives a 5 kg rifle 1.6 m/s of recoil.",
    "u2_angular": "One circle, three angular quantities and their linear links.",
    "u2_centripetal": "The velocity is tangential, the force and acceleration are radial.",
    "u2_banking": "Resolving N and m g gives tan θ = v²/rg.",
}

CAPTIONS_GU = {
    "u2_momentum": "બે ટ્રોલી: વેગમાન સંરક્ષિત રહે, ઊર્જા નહીં.",
    "u2_recoil": "400 m/s પરની 20 g ગોળી 5 kg રાયફલને 1.6 m/s રીકોઇલ આપે.",
    "u2_angular": "એક વર્તુળ, ત્રણ કોણીય રાશિઓ અને તેમના રેખીય સંબંધ.",
    "u2_centripetal": "વેગ સ્પર્શીય, બળ અને પ્રવર્ગ ત્રિજ્યાકીય.",
    "u2_banking": "N અને m g ના ઘટકો પાડતાં tan θ = v²/rg મળે.",
}


def heading(t, sub=None):
    return _heading(t, sub)


def foot(y, *lines):
    return _foot(y, *lines)


def arrow(x1, y1, x2, y2, color, w=2.0):
    """A straight arrow with a solid head, used for force and velocity vectors."""
    import math
    ang = math.atan2(y2 - y1, x2 - x1)
    hx, hy = x2 - 6 * math.cos(ang), y2 - 6 * math.sin(ang)
    left = (hx + 3.4 * math.sin(ang), hy - 3.4 * math.cos(ang))
    right = (hx - 3.4 * math.sin(ang), hy + 3.4 * math.cos(ang))
    return (ln(x1, y1, hx, hy, color, w) +
            f'<path d="M{x2} {y2}L{left[0]:.1f} {left[1]:.1f}L{right[0]:.1f} {right[1]:.1f}Z" '
            f'fill="{color}"/>')


# ------------------------------------------------------------------ 1. momentum before / after
def momentum():
    b = heading("Two trolleys, one conserved quantity", "before and after a perfectly sticky hit")
    y1, y2 = 70, 156
    b += text(14, y1 - 26, "before", 9.0, anchor="start", color=GREY)
    b += rbox(66, y1, 74, 24, "2 kg", BF, BLUE, 9.2)
    b += arrow(106, y1 - 4, 140, y1 - 4, BLUE)
    b += text(122, y1 + 18, "3 m/s", 8.4, color=BLUE)
    b += rbox(258, y1, 74, 24, "1 kg", GF, GREEN, 9.2)
    b += text(295, y1 + 18, "at rest", 8.4, color=GREEN)
    b += rbox(180, y1 + 40, 336, 22, "p = 2 × 3 + 1 × 0 = 6 kg·m/s", PF, PURPLE, 9.2)

    b += text(14, y2 - 10, "after", 9.0, anchor="start", color=GREY)
    b += rbox(126, y2, 108, 24, "3 kg together", OF, ORANGE, 9.2)
    b += arrow(240, y2 - 4, 286, y2 - 4, ORANGE)
    b += text(262, y2 + 18, "2 m/s", 8.4, color=ORANGE)
    b += rbox(180, y2 + 30, 336, 22, "p = 3 × 2 = 6 kg·m/s, so v = 6/3 = 2 m/s", OF, ORANGE, 9.2)
    b += foot(y2 + 70, "Momentum is a vector: opposite directions carry opposite signs.",
              "Sticky collisions keep momentum but lose kinetic energy.")
    return svg(360, y2 + 92, b)


# ------------------------------------------------------------------ 2. recoil
def recoil():
    b = heading("A gun at rest fires a bullet", "the total momentum cannot change")
    b += rbox(180, 60, 336, 24, "before firing: bullet 0 + rifle 0 = 0", BF, BLUE, 9.0)
    b += down(180, 72, 104)
    y = 112
    b += rbox(96, y, 152, 26, "bullet 20 g", GF, GREEN, 9.4)
    b += rbox(266, y, 152, 26, "rifle 5 kg", RF, RED, 9.4)
    b += arrow(32, y + 40, 140, y + 40, GREEN)
    b += arrow(330, y + 40, 222, y + 40, RED)
    b += text(86, y + 58, "400 m/s", 8.8, color=GREEN)
    b += text(276, y + 58, "1.6 m/s", 8.8, color=RED)
    b += text(96, y + 74, "p = 8 kg·m/s  →", 8.4, color=GREEN)
    b += text(266, y + 74, "p = 8 kg·m/s  ←", 8.4, color=RED)
    b += rbox(180, y + 100, 336, 24, "equal and opposite: the total stays zero", PF, PURPLE, 8.8)
    b += rbox(180, y + 132, 336, 24, "V = m v / M = (0.020 × 400)/5 = 1.6 m/s", OF, ORANGE, 9.2)
    b += foot(y + 168, "Small speed, large momentum: the rifle is 250 times heavier.",
              "A stock and a spring spread the change over a longer time.")
    return svg(360, y + 190, b)


# ------------------------------------------------------------------ 3. angular quantities
def angular():
    b = heading("One turn of the radius", "θ in radians, ω and α are its rates")
    import math
    cx, cy, r = 132, 138, 58
    b += f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="#BBB" stroke-width="1.3"/>'
    b += f'<circle cx="{cx}" cy="{cy}" r="2.6" fill="{INK}"/>'
    b += text(cx, cy + 15, "centre", 7.6, color=GREY)
    b += ln(cx, cy, cx + r, cy, GREY, 1.1, dash="3 2")          # reference radius along 0°
    bx, by = cx + r * 0.5, cy - r * 0.866                        # body at 60°
    b += ln(cx, cy, bx, by, INK, 1.6)
    b += f'<circle cx="{bx}" cy="{by}" r="4.4" fill="{BLUE}"/>'
    ax, ay = cx + 34, cy                                         # arc of the swept angle
    b += (f'<path d="M{ax} {ay} A34 34 0 0 0 {cx + 17} {cy - 29.4}" fill="none" '
          f'stroke="{ORANGE}" stroke-width="1.6"/>')
    b += text(cx + 40, cy - 14, "θ", 11.5, color=ORANGE, weight="bold")
    b += text(cx + 10, cy - 34, "r", 9.2, color=INK)
    b += arrow(bx + 4, by - 2, bx + 34, by - 19, GREEN)
    b += text(bx + 40, by - 20, "v", 9.8, color=GREEN, weight="bold")
    y = 216
    b += rbox(180, y, 336, 22, "θ = s/r   (radian, no unit)", BF, BLUE, 8.8)
    b += rbox(180, y + 26, 336, 22, "ω = Δθ/Δt = 2π/T   (rad/s)", GF, GREEN, 8.8)
    b += rbox(180, y + 52, 336, 22, "α = Δω/Δt   (rad/s²)", OF, ORANGE, 8.8)
    b += foot(y + 84, "v = rω and a = rα: one ω for every point, different v.",
              "1 rad = 57.3°, one full turn = 2π rad.")
    return svg(360, y + 106, b)


# ------------------------------------------------------------------ 4. centripetal force
def centripetal():
    b = heading("Velocity tangential, force radial", "a body on a string at constant speed")
    cx, cy, r = 148, 110, 62
    b += f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="#CCC" stroke-width="1.2" ' \
         f'stroke-dasharray="4 3"/>'
    b += f'<circle cx="{cx}" cy="{cy}" r="2.8" fill="{INK}"/>'
    b += text(cx, cy - 8, "centre", 7.6, color=GREY)
    bx, by = cx + r * 0.707, cy + r * 0.707
    b += arrow(bx, by, cx + 13, cy + 13, PURPLE, 1.9)
    b += text(cx + 26, cy + 34, "F", 11, color=PURPLE, weight="bold")
    b += f'<circle cx="{bx}" cy="{by}" r="5" fill="{BLUE}"/>'
    b += arrow(bx + 3, by - 3, bx + 33, by - 33, GREEN, 1.9)
    b += text(bx + 40, by - 36, "v", 10.5, color=GREEN, weight="bold")
    b += rbox(180, 196, 336, 24, "F = m v²/r = m r ω², aimed at the centre", PF, PURPLE, 9.2)
    b += rbox(180, 226, 336, 24, "v is always along the tangent", GF, GREEN, 9.2)
    b += foot(262, "Speed constant, velocity not: the direction turns every instant.",
              "Cut the string and the body leaves along the tangent, not outward.")
    return svg(360, 288, b)


# ------------------------------------------------------------------ 5. banking
def banking():
    b = heading("Resolving the forces on a banked curve", "friction ignored, so N does all the work")
    left, right, base, rise = 22, 336, 172, 76
    top = base - rise
    b += (f'<path d="M{left} {base}L{right} {top}L{right} {base}Z" fill="{GF}" stroke="{GREEN}" '
          f'stroke-width="1.4"/>')
    b += text(112, base - 12, "road surface", 8.6, color=GREEN)
    # angle at the left vertex
    b += (f'<path d="M{left + 46} {base} A46 46 0 0 0 {left + 44:.1f} {base - 10.8:.1f}" fill="none" '
          f'stroke="{ORANGE}" stroke-width="1.5"/>')
    b += text(left + 52, base - 12, "θ", 10.5, color=ORANGE, weight="bold")
    # the car, sitting on the slope
    sx = 186
    sy = base - (sx - left) / (right - left) * rise
    b += (f'<g transform="rotate(-13.4 {sx} {sy})">'
          f'<rect x="{sx - 15}" y="{sy - 20}" width="30" height="18" rx="3" fill="{BF}" '
          f'stroke="{BLUE}" stroke-width="1.4"/></g>')
    # normal reaction, perpendicular to the road
    b += arrow(sx, sy - 10, sx - 11, sy - 58, PURPLE)
    b += text(sx - 30, sy - 62, "N", 10.5, color=PURPLE, weight="bold")
    # weight, straight down
    b += arrow(sx + 8, sy + 2, sx + 8, sy + 40, RED)
    b += text(sx + 18, sy + 32, "m g", 9.6, color=RED, weight="bold")
    b += rbox(180, 196, 336, 24, "N cos θ = m g   and   N sin θ = m v²/r", BF, BLUE, 9.2)
    b += rbox(180, 226, 336, 24, "divide: tan θ = v²/(r g)", OF, ORANGE, 9.6)
    b += foot(262, "For r = 100 m at 20 m/s: tan θ = 0.408, θ = 22.2°.",
              "A cyclist leans by the same angle, tan θ = v²/rg.")
    return svg(360, 288, b)


DIAGRAMS = {
    "u2_momentum": momentum,
    "u2_recoil": recoil,
    "u2_angular": angular,
    "u2_centripetal": centripetal,
    "u2_banking": banking,
}
