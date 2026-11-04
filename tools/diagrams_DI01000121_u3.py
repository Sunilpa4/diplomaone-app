"""Five compact mobile SVGs for Applied Physics (DI01000121) Unit 3: properties of matter."""
from diagrams_DI01000121_u1 import (svg, text, rbox, P, ln, down, heading, foot,
                                   BLUE, BF, GREEN, GF, ORANGE, OF, RED, RF, PURPLE, PF,
                                   GREY, INK)

TITLES = {
    "u3_stress": "The stress-strain curve and its four key points",
    "u3_moduli": "Three moduli for three kinds of deformation",
    "u3_surface": "Why the surface of a liquid pulls inwards",
    "u3_capillary": "Capillary rise and the angle of contact",
    "u3_viscosity": "Velocity profile and terminal velocity",
}

TITLES_GU = {
    "u3_stress": "પ્રતિબળ-વિકૃતિ વક્ર અને તેના ચાર મુખ્ય બિંદુ",
    "u3_moduli": "ત્રણ પ્રકારની વિકૃતિ માટે ત્રણ ગુણાંક",
    "u3_surface": "પ્રવાહીની સપાટી અંદર તરફ કેમ ખેંચાય છે",
    "u3_capillary": "કેશનળી ચઢાણ અને સંપર્ક કોણ",
    "u3_viscosity": "વેગ રૂપરેખા અને અંતિમ વેગ",
}

CAPTIONS = {
    "u3_stress": "Design stays on the straight part OA; the safety factor keeps the working stress "
                 "well below B.",
    "u3_moduli": "Young's modulus for a wire, bulk modulus for a compressed liquid, shear modulus "
                 "for a twisted block.",
    "u3_surface": "A molecule inside has a full sphere of influence; one at the surface has half, so "
                  "the net pull is inward.",
    "u3_capillary": "The meniscus climbs until the weight of the column balances the upward pull of "
                    "surface tension.",
    "u3_viscosity": "The layer at the wall is at rest and the drag grows with speed, so the ball "
                    "settles at a constant terminal velocity.",
}

CAPTIONS_GU = {
    "u3_stress": "રચના સીધા ભાગ OA પર જ રહે; સલામતી અવયવ કાર્યકારી પ્રતિબળને B થી ઘણું નીચે રાખે.",
    "u3_moduli": "તાર માટે યંગ ગુણાંક, દબાયેલા પ્રવાહી માટે બલ્ક ગુણાંક, વળેલા બ્લોક માટે શિયર ગુણાંક.",
    "u3_surface": "અંદરના અણુનો પ્રભાવ ગોળો પૂરો, સપાટી પરના અણુનો અડધો, તેથી ચોખ્ખું ખેંચાણ અંદર તરફ.",
    "u3_capillary": "સ્તંભનું વજન પૃષ્ઠતાણના ઉપર તરફના ખેંચાણ સાથે સંતુલિત થાય ત્યાં સુધી મેનિસ્કસ ચઢે.",
    "u3_viscosity": "દીવાલ પાસેનું સ્તર સ્થિર અને પ્રતિરોધ ઝડપ સાથે વધે, તેથી દડો અચળ અંતિમ વેગે બેસે.",
}


def arrow(x1, y1, x2, y2, color=INK, w=1.2):
    """Line with a solid head at (x2, y2)."""
    import math
    ang = math.atan2(y2 - y1, x2 - x1)
    L = 5.0
    bx, by = x2 - L * math.cos(ang), y2 - L * math.sin(ang)
    p1 = (bx + 3.0 * math.sin(ang), by - 3.0 * math.cos(ang))
    p2 = (bx - 3.0 * math.sin(ang), by + 3.0 * math.cos(ang))
    return (ln(x1, y1, bx, by, color, w) +
            f'<path d="M{p1[0]:.1f} {p1[1]:.1f}L{x2} {y2}L{p2[0]:.1f} {p2[1]:.1f}Z" fill="{color}"/>')


# ------------------------------------------------------------------ 1. stress-strain curve
def stress():
    b = heading("Stress against strain for a ductile metal", "the slope of OA is Young's modulus")
    ox, oy, ex, ey = 54, 206, 340, 54
    b += arrow(ox, oy, ex, oy, GREY, 1.1)
    b += arrow(ox, oy, ox, ey, GREY, 1.1)
    b += text(ex - 26, oy + 15, "strain", 8.8, anchor="middle", color=GREY)
    b += text(ox - 6, ey - 4, "stress", 8.8, color=GREY)

    A = (112, 160); B = (152, 146); D = (240, 90); E = (306, 134)
    b += ln(ox, oy, A[0], A[1], BLUE, 2.2)
    b += (f'<path d="M{A[0]} {A[1]}C{A[0] + 14} {A[1] - 8} {A[0] + 25} {B[1] + 2} {B[0]} {B[1]}'
          f'C{B[0] + 34} {B[1] - 14} {D[0] - 40} {D[1] + 10} {D[0]} {D[1]}'
          f'C{D[0] + 24} {D[1] + 12} {E[0] - 26} {E[1] - 14} {E[0]} {E[1]}" fill="none" '
          f'stroke="{BLUE}" stroke-width="2.2" stroke-linecap="round"/>')

    for pt, lab, dx, dy, col in ((A, "A", -2, -10, GREEN), (B, "B", 8, -4, ORANGE),
                                 (D, "D", 3, -9, RED), (E, "E", 9, 13, PURPLE)):
        b += f'<circle cx="{pt[0]}" cy="{pt[1]}" r="3.4" fill="{col}"/>'
        b += text(pt[0] + dx, pt[1] + dy, lab, 10.4, weight="bold", color=col)
    b += text(ox - 12, oy + 11, "O", 10.4, weight="bold", color=INK)

    y = 256
    b += rbox(180, y, 336, 44, "", GF, GREEN, 9.0)
    b += text(180, y - 8, "A proportional limit  ·  B elastic limit", 9.4, color=INK)
    b += text(180, y + 7, "D maximum stress  ·  E fracture point", 9.4, color=INK)

    b += foot(y + 34, "Loading past B leaves a permanent stretch; past E the wire breaks.")
    return svg(360, y + 56, b)


# ------------------------------------------------------------------ 2. three moduli
def moduli():
    b = heading("Three moduli, three kinds of deformation", "each measures a different resistance")
    top, bot = 66, 168
    panels = ((64, "tension", "Y", BLUE, BF), (180, "volume", "K", GREEN, GF), (296, "shear", "G", ORANGE, OF))
    for cx, name, sym, col, fill in panels:
        b += f'<rect x="{cx - 48}" y="{top - 6}" width="96" height="{bot - top + 12}" rx="8" fill="{fill}" stroke="{col}" stroke-width="0.9"/>'
        b += text(cx, top + 10, name, 9.4, weight="bold", color=col)

    # tension: a bar pulled at both ends
    cx = 64
    b += f'<rect x="{cx - 11}" y="{top + 24}" width="22" height="54" fill="#FFFFFF" stroke="{BLUE}" stroke-width="1.4"/>'
    b += arrow(cx - 11, top + 51, cx - 30, top + 51, BLUE)
    b += arrow(cx + 11, top + 51, cx + 30, top + 51, BLUE)
    b += text(cx - 20, top + 40, "F", 9.0, color=BLUE)
    b += text(cx + 20, top + 40, "F", 9.0, color=BLUE)
    b += text(cx, bot - 6, "longer", 8.6, color=GREY)

    # volume: square squeezed from all sides
    cx = 180
    b += f'<rect x="{cx - 20}" y="{top + 36}" width="40" height="40" fill="#FFFFFF" stroke="{GREEN}" stroke-width="1.4"/>'
    b += arrow(cx - 34, top + 56, cx - 21, top + 56, GREEN)
    b += arrow(cx + 34, top + 56, cx + 21, top + 56, GREEN)
    b += arrow(cx, top + 24, cx, top + 35, GREEN)
    b += arrow(cx, top + 88, cx, top + 77, GREEN)
    b += text(cx, bot - 6, "smaller", 8.6, color=GREY)

    # shear: a parallelogram
    cx = 296
    b += (f'<path d="M{cx - 22} {top + 40}L{cx + 8} {top + 40}L{cx + 22} {top + 76}'
          f'L{cx - 8} {top + 76}Z" fill="#FFFFFF" stroke="{ORANGE}" stroke-width="1.4"/>')
    b += arrow(cx + 8, top + 30, cx + 26, top + 30, ORANGE)
    b += text(cx + 17, top + 21, "F", 9.0, color=ORANGE)
    b += text(cx, bot - 6, "slanted", 8.6, color=GREY)

    y = bot + 46
    b += rbox(180, y, 336, 44, "", BF, BLUE, 9.2)
    b += text(180, y - 7, "Y = σ/ε  (wire)   ·   K = −ΔP/(ΔV/V)  (liquid)", 9.2, color=INK)
    b += text(180, y + 8, "G = τ/φ  (block sheared sideways)", 9.2, color=INK)
    b += foot(y + 32, "Solids have all three; liquids and gases only a bulk modulus.")
    return svg(360, y + 54, b)


# ------------------------------------------------------------------ 3. surface molecules
def surface():
    b = heading("Molecular range and sphere of influence", "range about 10⁻⁹ m")
    liq_top, liq_bot = 104, 246
    b += f'<rect x="14" y="{liq_top}" width="332" height="{liq_bot - liq_top}" fill="#EAF3FD"/>'
    b += ln(14, liq_top, 346, liq_top, BLUE, 1.8)
    b += text(120, liq_top - 8, "liquid surface", 8.8, color=BLUE)

    # inside molecule: eight equal pulls, they cancel
    ax, ay, rad = 100, 166, 34
    b += f'<circle cx="{ax}" cy="{ay}" r="{rad}" fill="none" stroke="{GREEN}" stroke-width="1" stroke-dasharray="3 3"/>'
    for ux, uy in ((0, -1), (0, 1), (-1, 0), (1, 0), (-.71, -.71), (.71, -.71), (-.71, .71), (.71, .71)):
        b += arrow(ax + ux * 44, ay + uy * 44, ax + ux * 21, ay + uy * 21, GREEN, 1.0)
    b += f'<circle cx="{ax}" cy="{ay}" r="4.2" fill="{INK}"/>'
    b += text(ax, ay + 54, "inside: full sphere", 8.6, color=GREEN)
    b += text(ax, ay + 66, "pulls cancel", 8.6, color=GREEN)

    # surface molecule: only the lower half is filled, net pull inward
    bx, by = 262, liq_top
    b += f'<path d="M{bx - rad} {by}A{rad} {rad} 0 0 0 {bx + rad} {by}" fill="none" stroke="{ORANGE}" stroke-width="1" stroke-dasharray="3 3"/>'
    for sx, sy, tx, ty in ((-24, 30, -10, 14), (0, 34, 0, 14), (24, 30, 10, 14)):
        b += arrow(bx + sx, by + sy, bx + tx, by + ty, ORANGE, 1.0)
    b += f'<circle cx="{bx}" cy="{by}" r="4.2" fill="{INK}"/>'
    b += text(bx, by + 56, "surface: half sphere", 8.6, color=ORANGE)
    b += text(bx, by + 68, "net pull inward", 8.6, color=ORANGE)

    y = 272
    b += rbox(180, y, 336, 26, "surface energy  T = W/ΔA  (J/m² = N/m)", OF, ORANGE, 9.2)
    b += foot(y + 32, "The inward pull is why a free drop becomes a sphere.")
    return svg(360, y + 54, b)


# ------------------------------------------------------------------ 4. capillary rise
def capillary():
    b = heading("Water rising in a thin glass tube", "h = 2T cos θ / (ρ g r)")
    res_top, res_bot = 206, 248
    b += f'<rect x="18" y="{res_top}" width="324" height="{res_bot - res_top}" fill="#EAF3FD"/>'
    b += ln(18, res_top, 342, res_top, BLUE, 1.6)
    b += text(292, res_top + 18, "water", 8.8, color=BLUE)

    xl, xr, top, men = 154, 190, 54, 106
    b += f'<path d="M{xl + 3} {res_top}L{xl + 3} {men}Q{(xl + xr) / 2} {men + 22} {xr - 3} {men}'
    b += f'L{xr - 3} {res_top}Z" fill="#8FC4EE" opacity="0.8"/>'
    b += ln(xl, top, xl, res_bot, "#9AA5B1", 3.0)
    b += ln(xr, top, xr, res_bot, "#9AA5B1", 3.0)

    # height from the flat surface to the bottom of the meniscus
    b += arrow(132, res_top - 1, 132, men + 20, INK, 1.0)
    b += arrow(132, men + 20, 132, res_top - 1, INK, 1.0)
    b += text(114, 166, "h", 10.6, weight="bold", color=INK)
    b += text(102, 180, "7.35 cm", 8.4, color=GREY)
    b += ln(132, men + 20, xl + 6, men + 20, "#BBBBBB", 0.8, dash="2 2")
    b += ln(132, res_top - 1, xl + 6, res_top - 1, "#BBBBBB", 0.8, dash="2 2")

    # contact angle: wall (downwards) against the meniscus tangent
    b += ln(xl + 3, men, xl + 3, men + 20, ORANGE, 1.0, dash="2 2")
    b += f'<path d="M{xl + 3} {men + 18}A18 18 0 0 1 {xl + 14} {men + 3}" fill="none" stroke="{ORANGE}" stroke-width="1.2"/>'
    b += text(202, 158, "θ ≈ 0°: water wets glass", 8.8, anchor="start", color=ORANGE)
    b += ln(206, 150, xr + 8, 118, "#BBBBBB", 0.8, dash="2 2")

    b += text(258, 88, "tube radius r = 0.2 mm", 8.8, color=GREY)
    b += ln(252, 92, xr + 4, 100, "#BBBBBB", 0.8, dash="2 2")

    y = 276
    b += rbox(180, y, 336, 26, "weight of the column = upward pull of surface tension", GF, GREEN, 9.2)
    b += foot(y + 32, "Mercury has θ ≈ 140°, so h is negative and the level drops.")
    return svg(360, y + 54, b)


# ------------------------------------------------------------------ 5. viscosity
def viscosity():
    b = heading("Velocity profile and terminal velocity", "F = η A dv/dx")
    # left: flow between a fixed and a moving plate
    plate_top, plate_bot = 86, 200
    b += ln(40, plate_top, 178, plate_top, INK, 2.2)
    b += ln(40, plate_bot, 178, plate_bot, INK, 2.2)
    b += text(109, plate_top - 8, "moving plate, v", 8.4, color=GREY)
    b += text(109, plate_bot + 14, "fixed plate", 8.4, color=GREY)
    b += ln(40, plate_top + 2, 40, plate_bot - 2, "#BBBBBB", 0.9)
    for i, y in enumerate((192, 176, 160, 144, 128, 112, 96)):
        b += arrow(46, y, 46 + 10 + i * 9, y, BLUE, 1.4)
    b += text(109, plate_bot + 28, "velocity profile", 8.6, color=BLUE)

    # right: the three forces on a settling ball
    cx, cy, r = 274, 146, 17
    b += f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{BF}" stroke="{BLUE}" stroke-width="1.6"/>'
    b += arrow(cx, cy + r + 34, cx, cy + r + 2, GREEN, 1.3)
    b += text(cx, cy + r + 48, "weight", 8.6, color=GREEN)
    b += arrow(cx - 15, cy - r - 26, cx - 7, cy - r - 1, RED, 1.3)
    b += text(cx - 34, cy - r - 30, "drag", 8.6, color=RED)
    b += arrow(cx + 17, cy - r - 26, cx + 7, cy - r - 1, ORANGE, 1.3)
    b += text(cx + 34, cy - r - 30, "upthrust", 8.6, color=ORANGE)

    y = 252
    b += rbox(180, y, 336, 26, "v = 2r²(ρ − σ)g / (9η)", PF, PURPLE, 10.0)
    b += foot(y + 32, "Bigger or denser balls fall faster; thicker oil slows them down.")
    return svg(360, y + 54, b)


DIAGRAMS = {
    "u3_stress": stress,
    "u3_moduli": moduli,
    "u3_surface": surface,
    "u3_capillary": capillary,
    "u3_viscosity": viscosity,
}
