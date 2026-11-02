"""Draws the diagrams for DI04005041 Unit 3 "PVT Behavior".

    python3 tools/diagrams_DI04005041_u3.py

Writes content/chemical/sem4/DI04005041/diagrams/*.svg
Original teaching schematics (Narayanan; Smith, Van Ness & Abbott; Gavhane).
"""
import d1chem_lib as L
from d1draw import (AMBER, AMBER_FILL, BLUE, BLUE_FILL, Canvas, GREEN, GREEN_FILL, GREY_FILL,
                    INK, LAV, LINE, MUTED, P, PD, RED, RED_FILL, save)

CODE, BRANCH, SEM = "DI04005041", "chemical", 4


def _p(name):
    return L.out_path(BRANCH, SEM, CODE, name)


# ------------------------------------------------------- 3.1 PV diagram with regions
def pv_diagram():
    c = Canvas(960, 660, "The P–V diagram of a pure substance")
    pt = L.axes(c, 150, 120, 520, 330, "volume  V  →", "pressure  P  →",
                [0.2, 0.4, 0.6, 0.8, 1.0], [0.2, 0.4, 0.6, 0.8, 1.0])

    def poly(pts, color, sw=2.4, dash=None):
        xy = [pt(*q) for q in pts]
        for i in range(len(xy) - 1):
            c.line(*xy[i], *xy[i + 1], color, sw, dash)
        return xy

    LIQ = [(0.16, 0.18), (0.19, 0.27), (0.23, 0.36), (0.28, 0.45), (0.34, 0.54), (0.44, 0.64)]
    VAP = [(0.44, 0.64), (0.56, 0.53), (0.70, 0.42), (0.86, 0.30), (1.04, 0.20)]
    C = (0.44, 0.64)
    c.poly([pt(*q) for q in LIQ + VAP[1:]], "#F6EFFD", RED, 2.0, "6 4")

    def sub(psat, vl, vv, col):
        pts = [(vl - 0.03, 1.02), (vl - 0.02, 0.80), (vl - 0.008, 0.48), (vl, psat), (vv, psat)]
        pts += [(vv + (1.05 - vv) * i / 6, psat * vv / (vv + (1.05 - vv) * i / 6))
                for i in range(1, 7)]
        poly(pts, col)

    sub(0.28, 0.205, 0.92, P)
    sub(0.44, 0.300, 0.680, BLUE)
    poly([(0.10, 1.02), (0.17, 0.92), (0.26, 0.80), (0.35, 0.70), C,
          (0.56, 0.50), (0.74, 0.37), (1.05, 0.24)], "#7E57C2", 2.4, "7 5")
    poly([(0.10, 1.06), (0.22, 0.97), (0.38, 0.85), (0.58, 0.72), (0.82, 0.58), (1.08, 0.47)],
         GREEN, 2.2)

    c.circle(*pt(*C), 6, "#FFFFFF", RED, 2.4)
    c.text(pt(*C)[0] - 14, pt(*C)[1] - 10, "critical point C", 11.5, "end", RED, "bold")

    c.text(*pt(0.105, 0.60), "liquid", 12, "middle", PD, "bold")
    c.text(*pt(0.48, 0.33), "two-phase", 11.5, "middle", RED, "bold")
    c.text(*pt(0.48, 0.305), "liquid + vapour", 9.5, "middle", RED)
    c.text(*pt(0.72, 0.80), "superheated vapour", 11.5, "middle", PD, "bold")
    c.text(*pt(0.66, 0.90), "supercritical fluid", 10.5, "middle", GREEN, "bold")

    leg = [(P, "T₁ < Tc"), (BLUE, "T₂ < Tc"), ("#7E57C2", "T₃ = Tc"), (GREEN, "T₄ > Tc"),
           (RED, "saturation dome")]
    LX, LY = 686, 130
    c.rbox(LX, LY, 240, 126, "", "#FFFFFF", LINE, rx=6)
    for i, (col, name) in enumerate(leg):
        y = LY + 20 + i * 21
        c.line(LX + 14, y, LX + 44, y, col, 2.6)
        c.text(LX + 54, y, name, 10.5, "start", INK)

    c.title_band("READING THE DIAGRAM", 516)
    notes = ["Below Tc every isotherm has a flat plateau where liquid and vapour coexist.",
             "The plateau shortens as T rises and vanishes at C, where the two phases become identical.",
             "Above Tc no phase change occurs: the substance is a supercritical fluid.",
             "The dashed dome joins the plateau ends — left line saturated liquid, right line saturated vapour."]
    for i, n in enumerate(notes):
        c.text(30, 550 + i * 23, "• " + n, 11.5, "start", INK)
    c.footer()
    return c


# ------------------------------------------------------- 3.2 the five ideal-gas processes
def ideal_processes():
    c = Canvas(960, 700, "The five ideal-gas processes on a P–V diagram")
    pt = L.axes(c, 150, 110, 560, 320, "volume  V  →", "pressure  P  →",
                [0.25, 0.5, 0.75, 1.0], [0.25, 0.5, 0.75, 1.0])

    a = pt(0.20, 0.80)
    c.line(*a, *pt(0.20, 0.20), BLUE, 2.4)
    c.line(*a, *pt(1.02, 0.80), GREEN, 2.4)

    last = None
    for i in range(41):
        v = 0.20 + (1.02 - 0.20) * i / 40
        p = 0.20 * 0.80 / v
        if last:
            c.line(*last, *pt(v, p), P, 2.4)
        last = pt(v, p)

    last = None
    for i in range(41):
        v = 0.20 + (0.78 - 0.20) * i / 40
        p = 0.80 * (0.20 / v) ** 1.4
        if p < 0.05:
            break
        if last:
            c.line(*last, *pt(v, p), RED, 2.4, "6 4")
        last = pt(v, p)

    last = None
    for i in range(41):
        v = 0.20 + (0.95 - 0.20) * i / 40
        p = 0.80 * (0.20 / v) ** 1.2
        if p < 0.05:
            break
        if last:
            c.line(*last, *pt(v, p), AMBER, 2.2, "2 4")
        last = pt(v, p)

    c.circle(a[0], a[1], 6, "#FFFFFF", PD, 2.4)
    c.text(a[0] - 10, a[1] - 16, "state 1", 11.5, "end", PD, "bold")

    c.text(*pt(0.215, 0.55), "isochoric", 10.5, "start", BLUE, "bold")
    c.text(*pt(0.215, 0.505), "V = c", 10, "start", BLUE)
    c.text(*pt(0.66, 0.845), "isobaric   P = c", 10.5, "start", GREEN, "bold")
    c.text(*pt(0.86, 0.245), "isothermal  T = c", 10.5, "start", P, "bold")
    c.text(*pt(0.30, 0.235), "adiabatic", 10.5, "start", RED, "bold")
    c.text(*pt(0.30, 0.195), "PV^γ = c", 10, "start", RED)
    c.text(*pt(0.60, 0.63), "polytropic  PV^n = c", 10.5, "start", AMBER, "bold")

    c.title_band("WORK AND HEAT FOR EACH PATH (reversible, ideal gas)", 470)
    rows = [("isochoric", "V = c", "W = 0", "Q = m c_v ΔT", BLUE),
            ("isobaric", "P = c", "W = P ΔV", "Q = m c_p ΔT", GREEN),
            ("isothermal", "T = c", "W = Q = mRT ln(V₂/V₁)", "ΔU = 0", P),
            ("adiabatic", "PV^γ = c", "W = m c_v (T₁ − T₂)", "Q = 0", RED),
            ("polytropic", "PV^n = c", "W = mR(T₁−T₂)/(n−1)", "Q = W (γ−n)/(γ−1)", AMBER)]
    c.text(30, 486, "path", 10, "start", MUTED, "bold")
    c.text(160, 486, "law", 10, "start", MUTED, "bold")
    c.text(300, 486, "work", 10, "start", MUTED, "bold")
    c.text(620, 486, "heat", 10, "start", MUTED, "bold")
    for i, (name, law, w, q, col) in enumerate(rows):
        y = 514 + i * 26
        c.rect(30, y - 10, 6, 18, col, "none", 0)
        c.text(44, y, name, 11, "start", col, "bold")
        c.mono(160, y, law, 10.5, "start", INK)
        c.text(300, y, w, 10.5, "start", INK)
        c.text(620, y, q, 10.5, "start", MUTED)
    c.footer("Original teaching schematic · n = 0 isobaric, n = 1 isothermal, n = γ adiabatic, n = ∞ isochoric")
    return c


# ------------------------------------------------------- 3.3 compressibility chart
def compressibility():
    c = Canvas(960, 680, "Generalised compressibility chart")
    pt = L.axes(c, 160, 120, 520, 300, "reduced pressure  P_r →", "Z  →",
                [0.25, 0.5, 0.75, 1.0], [0.6, 0.8, 1.0, 1.2])

    c.line(*pt(0.0, 1.0), *pt(1.05, 1.0), MUTED, 1.6, "6 5")
    c.text(*pt(0.02, 1.035), "ideal gas, Z = 1", 10.5, "start", MUTED, "bold")

    def curve(Tr, dip, col, label, yoff=0):
        pts = []
        for i in range(81):
            pr = i / 80 * 1.02
            z = (1 - dip * (1 - (1 - min(pr / 1.0, 1)) ** 2) * (1 - 0.45 * pr)
                 + 0.55 * max(pr - 0.55, 0) ** 2.0)
            pts.append(pt(pr, min(max(z, 0.55), 1.35)))
        for i in range(len(pts) - 1):
            c.line(*pts[i], *pts[i + 1], col, 2.3)
        c.circle(pts[-1][0], pts[-1][1], 3.5, col, col, 1.0)
        c.text(pts[-1][0] + 10, pts[-1][1] + yoff, label, 10.5, "start", col, "bold")

    curve(2.00, 0.02, GREEN, "T_r = 2.0", -4)
    curve(1.30, 0.09, BLUE, "T_r = 1.3", 0)
    curve(1.05, 0.17, "#7E57C2", "T_r = 1.05", 6)

    c.title_band("HOW THE CHART IS USED", 476)
    steps = ["1.  Find the critical constants Tc and Pc of the gas.",
             "2.  Reduced values:   P_r = P / P_c    and    T_r = T / T_c.",
             "3.  Read Z from the chart at that (P_r , T_r).",
             "4.  Then   V = Z R T / P   — the ideal-gas law corrected by one number."]
    for i, t in enumerate(steps):
        c.text(30, 512 + i * 24, t, 11.5, "start", INK)
    c.mono(30, 622, "Z = P V / R T", 16, "start", PD, "bold")
    c.text(230, 622, "Z < 1 attraction dominates,   Z > 1 repulsion dominates", 11.5, "start", MUTED)
    c.footer("Original teaching schematic · every gas approaches Z = 1 as P → 0")
    return c


# ------------------------------------------------------- 3.4 real gas: Z deviation
def real_gas_z():
    c = Canvas(920, 660, "Why real gases deviate from the ideal-gas law")
    pt = L.axes(c, 160, 120, 540, 290, "pressure  P  →", "Z  →",
                [0.25, 0.5, 0.75, 1.0], [0.6, 0.8, 1.0, 1.2, 1.4])

    c.line(*pt(0, 1.0), *pt(1.05, 1.0), MUTED, 1.6, "6 5")
    c.text(*pt(0.02, 1.03), "Z = 1  (ideal)", 10.5, "start", MUTED, "bold")

    pts = []
    for i in range(81):
        x = i / 80
        z = 1 - 0.42 * x * (1 - x) * 3.4 + 0.30 * x ** 3.6
        pts.append(pt(x, min(max(z, 0.5), 1.32)))
    for i in range(len(pts) - 1):
        c.line(*pts[i], *pts[i + 1], P, 2.6)

    c.text(*pt(0.26, 0.63), "attraction dominates", 11, "middle", RED, "bold")
    c.text(*pt(0.26, 0.60), "Z < 1  — volume smaller than ideal", 10, "middle", RED)
    c.text(*pt(0.82, 1.235), "repulsion dominates", 10.5, "middle", GREEN, "bold")
    c.text(*pt(0.82, 1.185), "Z > 1 — molecular volume matters", 9.5, "middle", GREEN)

    c.title_band("THE TWO COMPETING EFFECTS", 478)
    c.text(30, 512, "Attraction between molecules pulls them together, so the measured volume is "
                    "smaller than the ideal value and Z falls below 1.", 11.5, "start", INK)
    c.text(30, 536, "At high pressure the molecules themselves occupy volume, leaving less free "
                    "space, so Z rises above 1.", 11.5, "start", INK)
    c.text(30, 566, "At very low pressure both effects vanish and Z → 1: the gas behaves ideally.",
           11.5, "start", MUTED)
    c.mono(30, 616, "Z = P V / R T   =   V_actual / V_ideal", 15, "start", PD, "bold")
    c.footer()
    return c


FIGURES = [
    ("d3_pv_diagram", pv_diagram),
    ("d3_ideal_processes", ideal_processes),
    ("d3_compressibility", compressibility),
    ("d3_real_gas_z", real_gas_z),
]


def main():
    for name, fn in FIGURES:
        save(fn(), _p(name))
        print("wrote", _p(name))
    return [n for n, _ in FIGURES]


if __name__ == "__main__":
    main()
