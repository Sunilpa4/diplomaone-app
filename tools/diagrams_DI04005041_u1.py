"""Draws the diagrams for DI04005041 (Chemical Engineering Thermodynamics) Unit 1.

    python3 tools/diagrams_DI04005041_u1.py

Writes content/chemical/sem4/DI04005041/diagrams/*.svg

Figures are original teaching schematics drawn from the standard reference matter
for GTU Chemical Engineering Thermodynamics (Narayanan; Smith, Van Ness & Abbott;
Gavhane). They are conceptual — not construction or operating drawings.
"""
import d1chem_lib as L
from d1draw import (AMBER, AMBER_FILL, BLUE, BLUE_FILL, Canvas, GREEN, GREEN_FILL, GREY_FILL,
                    INK, LAV, LINE, MUTED, P, PD, RED, RED_FILL, save)

CODE, BRANCH, SEM = "DI04005041", "chemical", 4


def _p(name):
    return L.out_path(BRANCH, SEM, CODE, name)


# --------------------------------------------------------------- 1.1 system boundary
def system_boundary():
    c = Canvas(920, 560, "System, surroundings and the three classes of boundary")
    c.text(24, 74, "The boundary is drawn where the analysis needs it; everything outside it is the surroundings.",
           12.5, "start", MUTED)

    panels = [
        ("CLOSED SYSTEM", "fixed mass, energy crosses", 24, 110),
        ("OPEN SYSTEM (control volume)", "mass and energy cross", 322, 110),
        ("ISOLATED SYSTEM", "no mass, no energy crosses", 620, 110),
    ]
    for title, sub, x, y in panels:
        c.rect(x, y, 276, 330, "#FFFFFF", LINE, 1.6, rx=10)
        c.text(x + 138, y + 26, title, 13, "middle", PD, "bold")
        c.text(x + 138, y + 46, sub, 11, "middle", MUTED)

    # closed: a vessel, arrow of heat crossing the wall, no pipe
    x, y = 24, 110
    L.tank(c, x + 74, y + 78, 128, 176, "#FFFFFF")
    c.arrow(x + 20, y + 150, x + 68, y + 150, RED, 2.2, label="Q", lpos=(x + 40, y + 138))
    c.text(x + 138, y + 280, "gas  m = constant", 11.5, "middle", INK)
    c.text(x + 138, y + 300, "piston or rigid wall", 11, "middle", MUTED)

    # open: tank with inlet and outlet streams
    x, y = 322, 110
    L.tank(c, x + 74, y + 88, 128, 166, "#FFFFFF")
    L.arrow_stream(c, [(x + 34, y + 62), (x + 34, y + 116), (x + 100, y + 116)], "in", (x + 8, y + 58))
    L.arrow_stream(c, [(x + 182, y + 220), (x + 250, y + 220)], "out", (x + 206, y + 208))
    c.arrow(x + 60, y + 268, x + 112, y + 268, RED, 2.0, label="Q", lpos=(x + 78, y + 256))
    c.arrow(x + 214, y + 268, x + 268, y + 300, BLUE, 2.0, label="W", lpos=(x + 244, y + 258))
    c.text(x + 138, y + 302, "control volume", 11, "middle", MUTED)

    # isolated: thick dashed box, nothing crosses
    x, y = 620, 110
    c.rect(x + 40, y + 62, 196, 190, "#FFFFFF", PD, 2.4, rx=8, dash="7 6")
    c.circle(x + 138, y + 157, 46, LAV, P, 2)
    c.text(x + 138, y + 152, "hot body +", 11.5, "middle", PD, "bold")
    c.text(x + 138, y + 170, "cold body", 11.5, "middle", PD, "bold")
    c.text(x + 138, y + 282, "no heat, no work, no mass", 11.5, "middle", INK)
    c.text(x + 138, y + 302, "state may still change inside", 11, "middle", MUTED)

    c.title_band("SURROUNDINGS  —  everything not inside the boundary", 486)
    c.note("Boundary may be real (vessel wall) or imaginary (a section of pipe). "
           "It may be fixed or moving (piston face).", 528)
    c.footer()
    return c


# --------------------------------------------------------------- 1.2 reversible vs irreversible
def reversible_path():
    c = Canvas(900, 620, "Reversible and irreversible paths between the same two states")
    pt = L.axes(c, 165, 120, 580, 360, "volume  V  (m\u00b3)", "pressure  P  (bar)",
                [0.25, 0.5, 0.75, 1.0], [0.25, 0.5, 0.75, 1.0])

    # reversible isotherm  P = 0.30/V  (drawn as a smooth curve)
    last = None
    for i in range(61):
        v = 0.30 + i * (0.95 - 0.30) / 60
        p = 0.30 / v
        if p > 1.0:
            continue
        px, py = pt(v / 1.1, p / 1.1)
        if last:
            c.parts.append(f'<line x1="{last[0]:.1f}" y1="{last[1]:.1f}" x2="{px:.1f}" y2="{py:.1f}" '
                           f'stroke="{P}" stroke-width="2.4" fill="none"/>')
        last = (px, py)

    a = pt(0.36 / 1.1, 0.833 / 1.1)
    b = pt(0.90 / 1.1, 0.333 / 1.1)
    c.circle(a[0], a[1], 7, "#FFFFFF", P, 2.4)
    c.circle(b[0], b[1], 7, "#FFFFFF", P, 2.4)
    c.text(a[0] - 22, a[1] + 4, "state 1", 12, "end", PD, "bold")
    c.text(a[0] - 22, a[1] + 20, "(P\u2081, V\u2081)", 11, "end", MUTED)
    c.text(b[0] + 16, b[1] + 4, "state 2", 12, "start", PD, "bold")
    c.text(b[0] + 16, b[1] + 20, "(P\u2082, V\u2082)", 11, "start", MUTED)

    # irreversible zig-zag: sudden drop then hold
    z1 = pt(0.36 / 1.1, 0.333 / 1.1)
    z2 = pt(0.90 / 1.1, 0.333 / 1.1)
    c.line(*a, *z1, RED, 2.2, "6 5")
    c.line(*z1, *z2, RED, 2.2, "6 5")
    c.text(z2[0] - 150, z2[1] - 14, "sudden release", 11, "end", RED, "bold")

    c.text(390, 132, "reversible isothermal path", 12.5, "start", P, "bold")
    c.text(390, 150, "P V = constant, drawn through a continuous series of equilibrium states",
           11, "start", MUTED)
    c.text(150, 455, "irreversible path: pressure is released suddenly, so the intermediate",
           11.5, "start", RED)
    c.text(150, 473, "states are not equilibrium states and the path cannot be drawn exactly",
           11.5, "start", RED)
    c.note("Area under the reversible curve is the maximum work the same change can deliver; "
           "the irreversible path delivers less.", 556)
    c.footer()
    return c


# --------------------------------------------------------------- 1.3 PVT surface
def pvt_surface():
    """P-V isotherms of a pure substance: two subcritical plateaus, the critical
    isotherm with its inflection, and one supercritical isotherm."""
    c = Canvas(900, 600, "The P\u2013V\u2013T surface as P\u2013V isotherms of a pure substance")
    pt = L.axes(c, 180, 110, 500, 340, "molar volume  V  \u2192", "pressure  P  \u2192",
                [0.2, 0.4, 0.6, 0.8, 1.0], [0.2, 0.4, 0.6, 0.8, 1.0])

    def poly(pts, color, sw=2.4, dash=None):
        xy = [pt(*q) for q in pts]
        for i in range(len(xy) - 1):
            c.line(*xy[i], *xy[i + 1], color, sw, dash)
        return xy

    # ---- saturation dome (drawn first, so isotherms sit on top)
    LIQ = [(0.17, 0.20), (0.20, 0.28), (0.24, 0.36), (0.29, 0.44), (0.34, 0.52), (0.42, 0.62)]
    VAP = [(0.42, 0.62), (0.52, 0.55), (0.63, 0.46), (0.78, 0.34), (0.95, 0.24)]
    C_PT = (0.42, 0.62)
    c.poly([pt(*q) for q in LIQ + VAP[1:]], "#F6EFFD", RED, 2.0, "6 4")

    # ---- subcritical isotherm: steep liquid branch, plateau, 1/V vapour branch
    def subcritical(psat, v_liq, v_vap, color, label):
        liq = [(v_liq - 0.030, 1.02), (v_liq - 0.022, 0.86), (v_liq - 0.012, 0.62),
               (v_liq - 0.004, 0.44), (v_liq, psat)]
        plateau = [(v_liq, psat), (v_vap, psat)]
        vap = [(v_vap + (1.02 - v_vap) * i / 6, psat * v_vap / (v_vap + (1.02 - v_vap) * i / 6))
               for i in range(7)]
        poly(liq, color); poly(plateau, color); xy = poly(vap, color)

    subcritical(0.32, 0.215, 0.81, P, None)
    subcritical(0.46, 0.300, 0.625, BLUE, None)

    # ---- critical isotherm: horizontal inflection exactly at C
    poly([(0.115, 1.02), (0.175, 0.93), (0.245, 0.82), (0.320, 0.71),
          (0.380, 0.655), C_PT, (0.500, 0.545), (0.640, 0.435),
          (0.820, 0.345), (1.02, 0.285)], "#7E57C2", 2.4, "7 5")

    # ---- supercritical isotherm: smooth, always above the critical one
    xy = poly([(0.115, 1.04), (0.200, 0.955), (0.300, 0.855), (0.430, 0.745),
               (0.600, 0.635), (0.800, 0.535), (1.02, 0.455)], GREEN, 2.4)

    c.circle(*pt(*C_PT), 6, "#FFFFFF", RED, 2.4)
    c.text(pt(*C_PT)[0] - 13, pt(*C_PT)[1] - 12, "critical point C", 11.5, "end", RED, "bold")

    # legend in the empty upper-right corner
    leg = [(P, "T\u2081 < Tc  (has a plateau)"), (BLUE, "T\u2082 < Tc  (shorter plateau)"),
           ("#7E57C2", "T\u2083 = Tc  (inflection at C)"), (GREEN, "T\u2084 > Tc  (no plateau)"),
           (RED, "saturation dome  P = 1, F = 1")]
    c.rbox(590, 128, 288, 132, "", "#FFFFFF", LINE, rx=6)
    for i, (col, name) in enumerate(leg):
        y = 148 + i * 22
        c.line(604, y, 634, y, col, 2.6)
        c.text(644, y, name, 10.5, "start", INK)

    c.text(*pt(0.62, 0.385), "two-phase region (liquid + vapour)", 10.5, "middle", RED, "bold")
    c.text(*pt(0.20, 0.135), "saturated liquid line", 10.5, "start", RED, "bold")
    c.text(*pt(0.66, 0.150), "saturated vapour line", 10.5, "start", RED, "bold")

    c.title_band("READING THE SAME SURFACE THREE WAYS", 512)
    views = [("P\u2013V diagram (drawn)", "plateau at every T below Tc; it shrinks to a point at C"),
             ("P\u2013T diagram", "vapour-pressure curve ends at C; F = 1 along it"),
             ("V\u2013T diagram", "isobars; volume jumps at boiling")]
    for i, (name, sub) in enumerate(views):
        x = 24 + i * 292
        c.rbox(x, 538, 278, 46, "", "#FFFFFF", LINE, rx=6)
        c.text(x + 12, 550, name, 11.5, "start", PD, "bold")
        c.text(x + 12, 570, sub, 10, "start", MUTED)
    c.footer("Original teaching schematic \u2022 drawn for unit 1; the full PVT surface is three-dimensional")
    return c


# --------------------------------------------------------------- 1.4 first law device
def energy_bookkeeping():
    c = Canvas(900, 520, "First law as bookkeeping on a control volume")
    L.tank(c, 340, 150, 220, 210, "#FFFFFF")
    L.agitator(c, 450, 168, 330, 52)
    L.impeller_top(c, 450, 150)
    c.text(505, 200, "process fluid", 11.5, "middle", MUTED)
    c.text(505, 222, "U, H, T", 12, "middle", PD, "bold")

    L.arrow_stream(c, [(150, 96), (150, 190), (336, 190)], None)
    c.text(200, 172, "m_in ,  h_in", 12, "middle", PD, "bold")
    L.arrow_stream(c, [(564, 300), (740, 300)], None)
    c.text(660, 282, "m_out ,  h_out", 12, "middle", PD, "bold")
    c.arrow(250, 150, 322, 150, RED, 2.2, label="Q", lpos=(286, 136))
    c.arrow(450, 340, 450, 392, BLUE, 2.2)
    c.text(462, 372, "W\u209b  (shaft work)", 12, "start", BLUE, "bold")

    c.title_band("ENERGY ACCOUNTING FOR A STEADY-FLOW DEVICE", 410)
    rows = [("in with the feed", "m_in  h_in", GREEN),
            ("out with the product", "m_out  h_out", RED),
            ("heat added", "Q", AMBER),
            ("shaft work done by the fluid", "W\u209b", BLUE)]
    for i, (name, sym, col) in enumerate(rows):
        x = 30 + i * 218
        c.rbox(x, 432, 204, 50, "", "#FFFFFF", col, rx=6)
        c.text(x + 12, 446, name, 10.5, "start", INK)
        c.mono(x + 12, 468, sym, 13, "start", col, "bold")
    c.footer("Original teaching schematic \u2022 steady state, changes in kinetic and potential energy neglected")
    return c


# --------------------------------------------------------------- 1.5 phase rule
def phase_rule():
    c = Canvas(920, 610, "Gibbs phase rule: degrees of freedom on a P\u2013T diagram")
    pt = L.axes(c, 170, 110, 570, 350, "temperature  T  \u2192", "P  \u2192",
                [0.25, 0.5, 0.75, 1.0], [0.25, 0.5, 0.75, 1.0])

    # sublimation, fusion (near vertical), vaporisation
    c.line(*pt(0.05, 0.18), *pt(0.42, 0.56), P, 2.4)
    c.line(*pt(0.42, 0.56), *pt(0.46, 1.0), P, 2.4)
    c.line(*pt(0.42, 0.56), *pt(1.0, 0.74), P, 2.4)
    c.circle(*pt(0.42, 0.56), 6, "#FFFFFF", RED, 2.4)
    c.text(pt(0.42, 0.56)[0] - 12, pt(0.42, 0.56)[1] - 12, "triple point  3 phases  F = 0", 11.5, "end", RED, "bold")

    c.text(210, 420, "solid", 13, "middle", PD, "bold")
    c.text(690, 440, "vapour", 13, "middle", PD, "bold")
    c.text(320, 215, "liquid", 13, "middle", PD, "bold")

    c.title_band("F = C \u2212 P + 2     (C = components,  P = phases present)", 528)
    cases = [("single phase region", "P = 1", "F = 2", "both T and P may be chosen"),
             ("on a curve", "P = 2", "F = 1", "one degree of freedom (e.g. boiling T fixes P)"),
             ("at the triple point", "P = 3", "F = 0", "fixed T and P, no choice")]
    for i, (name, p_, f_, why) in enumerate(cases):
        x = 30 + i * 300
        c.rbox(x, 546, 288, 46, "", "#FFFFFF", LINE, rx=6)
        c.text(x + 12, 558, f"{name}  ({p_})  \u2192  {f_}", 11, "start", PD, "bold")
        c.text(x + 12, 578, why, 10, "start", MUTED)
    c.footer()
    return c


# --------------------------------------------------------------- 1.6 zeroth law
def zeroth_law():
    c = Canvas(880, 420, "The zeroth law: thermal equilibrium is transitive")
    boxes = [(60, "A", "hot", RED), (350, "B", "cold", BLUE), (640, "C", "cold", BLUE)]
    for x, name, note, col in boxes:
        c.rbox(x, 150, 170, 120, "", "#FFFFFF", col, rx=14)
        c.text(x + 85, 186, name, 26, "middle", col, "bold")
        c.text(x + 85, 220, note, 12, "middle", MUTED)
        c.text(x + 85, 244, "T", 12, "middle", INK, "bold")

    c.line(232, 210, 348, 210, PD, 2.2)
    c.text(290, 196, "diathermic", 11, "middle", PD, "bold")
    c.text(290, 232, "no heat flows", 10.5, "middle", MUTED)
    c.line(522, 210, 638, 210, PD, 2.2)
    c.text(580, 196, "diathermic", 11, "middle", PD, "bold")
    c.text(580, 232, "no heat flows", 10.5, "middle", MUTED)

    c.elbow([(145, 150), (145, 90), (725, 90), (725, 150)], GREEN, 2.0)
    c.text(435, 78, "A and C also in equilibrium \u2014 no heat flows if they are joined", 11.5, "middle", GREEN, "bold")

    c.title_band("CONSEQUENCE", 310)
    c.text(60, 340, "Two bodies in thermal equilibrium with a third are in thermal equilibrium with each other.", 12, "start", INK)
    c.text(60, 362, "Therefore a single property \u2014 temperature \u2014 can label the state, and a thermometer is possible.", 12, "start", PD, "bold")
    c.footer()
    return c


# ------------------------------------------------------------------ driver
FIGURES = [
    ("d1_system_boundary", system_boundary),
    ("d1_reversible_path", reversible_path),
    ("d1_pvt_surface", pvt_surface),
    ("d1_energy_bookkeeping", energy_bookkeeping),
    ("d1_phase_rule", phase_rule),
    ("d1_zeroth_law", zeroth_law),
]


def main():
    for name, fn in FIGURES:
        p = _p(name)
        save(fn(), p)
        print("wrote", p)
    return [n for n, _ in FIGURES]


if __name__ == "__main__":
    main()
