"""Draws the diagrams for DI04005041 Unit 5 "Refrigeration Cycles and Systems".

    python3 tools/diagrams_DI04005041_u5.py

Original teaching schematics (Narayanan; Smith, Van Ness & Abbott; Gavhane; Rajput).
"""
import d1chem_lib as L
from d1draw import (AMBER, AMBER_FILL, BLUE, BLUE_FILL, Canvas, GREEN, GREEN_FILL, GREY_FILL,
                    INK, LAV, LINE, MUTED, P, PD, RED, RED_FILL, save)

CODE, BRANCH, SEM = "DI04005041", "chemical", 4


def _p(name):
    return L.out_path(BRANCH, SEM, CODE, name)


# ------------------------------------------------------- 5.1 the refrigeration loop
def refrigeration_loop():
    c = Canvas(960, 645, "A vapour-compression refrigerator: four components, four state points")

    # cold space sits behind the evaporator
    c.rect(248, 366, 250, 132, "#EAF3FD", LINE, 1.4, rx=12)

    c.rbox(330, 150, 190, 70, "compressor", LAV, P, 12.5, "bold", PD, rx=8)
    c.rbox(590, 150, 190, 70, "condenser", RED_FILL, RED, 12.5, "bold", RED, rx=8)
    c.rbox(590, 400, 190, 70, "expansion valve", LAV, P, 12.5, "bold", PD, rx=8)
    c.rbox(330, 400, 190, 70, "evaporator", BLUE_FILL, BLUE, 12.5, "bold", BLUE, rx=8)

    def pipe(x1, y1, x2, y2, color):
        c.arrow(x1, y1, x2, y2, color, 2.4, head=9)

    pipe(522, 185, 588, 185, RED)      # compressor -> condenser
    pipe(685, 222, 685, 398, AMBER)    # condenser -> valve
    pipe(588, 435, 522, 435, AMBER)    # valve -> evaporator
    pipe(425, 398, 425, 222, BLUE)     # evaporator -> compressor

    # state points on the pipes
    for x, y, name, dx, dy in [(505, 185, "2", 0, -14), (685, 320, "3", 16, 0),
                               (505, 435, "4", 0, 16), (425, 320, "1", -16, 0)]:
        c.circle(x, y, 11, "#FFFFFF", PD, 2)
        c.text(x + dx, y + dy, name, 11.5, "middle", PD, "bold")

    # labels on the four lines
    c.text(555, 208, "hot gas", 10, "middle", RED, "bold")
    c.text(700, 268, "liquid", 10, "start", AMBER, "bold")
    c.text(556, 452, "wet\nvapour", 10, "middle", AMBER, "bold")
    c.text(410, 268, "cold vapour", 10, "end", BLUE, "bold")

    # work in and heat out
    c.arrow(258, 185, 328, 185, GREEN, 2.6)
    c.text(252, 185, "W in", 11.5, "end", GREEN, "bold")
    c.arrow(685, 148, 685, 96, RED, 2.6)
    c.text(700, 122, "Q_H rejected at T_H", 11.5, "start", RED, "bold")

    # cold space label and the heat leaking in
    c.text(373, 490, "COLD SPACE at T_C", 11.5, "middle", BLUE, "bold")
    c.arrow(373, 550, 373, 500, BLUE, 2.4)
    c.text(386, 528, "Q_C from the space being cooled", 10.5, "start", BLUE, "bold")

    c.title_band("ENERGY:  Q_H = Q_C + W", 578)
    c.text(30, 612, "The same kilogram of refrigerant goes round for ever; work enters only at the "
                    "compressor and leaves only as heat at the condenser.",
           11.5, "start", INK)
    c.footer()
    return c


# ------------------------------------------------------- 5.2 the cycle on P-h
def ph_cycle():
    c = Canvas(960, 660, "The vapour-compression cycle on a P–h diagram")
    pt = L.axes(c, 185, 110, 520, 350, "enthalpy  h  →", "pressure  P  →")
    PC, PH = 0.28, 0.74

    # saturation dome: y from 0.10 to 0.88, apex at the critical point
    def limb(sign, a, power):
        pts = []
        for i in range(41):
            t = i / 40
            y = 0.10 + 0.78 * t
            x = 0.46 + sign * a * (1 - t) ** power
            pts.append(pt(x, y))
        return pts

    left = limb(-1, 0.26, 1.7)
    right = limb(+1, 0.19, 1.35)
    c.poly(left + list(reversed(right)), "#F4F1F7", LINE, 1.4)

    def xl(yv):      # saturated liquid enthalpy at pressure y
        t = (yv - 0.10) / 0.78
        return 0.46 - 0.26 * (1 - t) ** 1.7

    def xr(yv):      # saturated vapour enthalpy at pressure y
        t = (yv - 0.10) / 0.78
        return 0.46 + 0.19 * (1 - t) ** 1.35

    h3, h1 = xl(PH), xr(PC)
    h4, h2 = h3, h1 + 0.115
    c.text(*pt(0.46, 0.905), "critical point", 10, "middle", MUTED)
    c.circle(*pt(0.46, 0.88), 3.5, MUTED, MUTED, 1)
    c.text(*pt(0.46, 0.185), "wet region", 11, "middle", MUTED)

    # guide lines at the two pressures
    for q, lab in ((PH, "P_H"), (PC, "P_C")):
        c.line(*pt(0.055, q), *pt(0.97, q), LINE, 1.1, dash="5 5")
        c.text(*pt(0.035, q), lab, 11, "end", MUTED, "bold")

    # 1 -> 2 compression (curving), 2 -> 3 condensation, 3 -> 4 throttling, 4 -> 1 evaporation
    seq = [pt(h1 + (h2 - h1) * (i / 30), PC + (PH - PC) * (i / 30) ** 0.85) for i in range(31)]
    for a, b in zip(seq, seq[1:]):
        c.line(*a, *b, GREEN, 2.8)
    c.arrow(*seq[-2], *seq[-1], GREEN, 2.8, head=9)
    c.arrow(*pt(h2, PH), *pt(h3 + 0.01, PH), RED, 2.8, head=9)
    c.arrow(*pt(h3, PH), *pt(h3, PC + 0.01), AMBER, 2.8, head=9, dash="7 5")
    c.arrow(*pt(h4, PC), *pt(h1 - 0.01, PC), BLUE, 2.8, head=9)

    for (hh, q), name, dx, dy, anchor in [((h1, PC), "1", 6, 16, "start"),
                                         ((h2, PH), "2", 14, -4, "start"),
                                         ((h3, PH), "3", -14, -4, "end"),
                                         ((h4, PC), "4", -14, 16, "end")]:
        x, y = pt(hh, q)
        c.circle(x, y, 7.5, "#FFFFFF", PD, 2.2)
        c.text(x + dx, y + dy, name, 12.5, anchor, PD, "bold")

    c.text(*pt(0.618, 0.44), "compression", 10, "end", GREEN, "bold")
    c.text(*pt(0.505, PH - 0.075), "condensation   Q_H out", 10.5, "start", RED, "bold")
    c.text(*pt(h3 - 0.02, 0.50), "throttling", 10, "end", AMBER, "bold")
    c.text(*pt((h1 + h4) / 2 - 0.02, PC - 0.155), "evaporation   Q_C in", 10.5, "middle", BLUE, "bold")

    c.title_band("THE FOUR PROCESSES AND WHAT EACH ONE DOES", 502)
    rows = [("1→2", "compression, roughly isentropic", "work in; pressure rises from P_C to P_H", GREEN),
            ("2→3", "condensation at constant P", "Q_H rejected to the surroundings", RED),
            ("3→4", "throttling, h constant", "pressure falls, temperature drops to T_C", AMBER),
            ("4→1", "evaporation at constant P", "Q_C absorbed from the cold space", BLUE)]
    for i, (tag, what, why, col) in enumerate(rows):
        y = 536 + i * 27
        c.text(40, y, tag, 11.5, "start", col, "bold")
        c.text(100, y, what, 11.5, "start", INK)
        c.text(390, y, why, 11.5, "start", MUTED)
    c.footer()
    return c


# ------------------------------------------------------- 5.3 air refrigeration
def air_refrigeration():
    c = Canvas(960, 660, "The reversed Brayton (air) refrigeration cycle")
    c.text(24, 74, "The same four processes, but the working fluid is air and it never changes phase.",
           11.5, "start", MUTED)

    # layout: compressor, cooler, expander, cold chamber in a ring
    c.rbox(150, 130, 200, 74, "compressor", LAV, P, 12.5, "bold", PD, rx=8)
    c.rbox(610, 130, 200, 74, "aftercooler", RED_FILL, RED, 12.5, "bold", RED, rx=8)
    c.rbox(610, 380, 200, 74, "expander / turbine", LAV, P, 12.5, "bold", PD, rx=8)
    c.rbox(150, 380, 200, 74, "cold chamber", BLUE_FILL, BLUE, 12.5, "bold", BLUE, rx=8)

    # flow
    c.arrow(350, 167, 608, 167, GREEN, 2.2)
    c.text(479, 150, "high-pressure hot air", 10.5, "middle", GREEN, "bold")
    c.arrow(710, 204, 710, 378, RED, 2.2)
    c.text(722, 291, "cooled air, 25–40 °C", 10.5, "start", RED, "bold")
    c.arrow(608, 417, 352, 417, AMBER, 2.2)
    c.text(480, 400, "cold air, −40 to −70 °C", 10.5, "middle", AMBER, "bold")
    c.arrow(250, 380, 250, 206, BLUE, 2.2)
    c.text(238, 293, "warm air back", 10.5, "end", BLUE, "bold")

    # heat arrows
    c.arrow(710, 130, 710, 88, RED, 2.4)
    c.text(724, 108, "heat to atmosphere", 10.5, "start", RED, "bold")
    c.arrow(250, 454, 250, 496, BLUE, 2.4)
    c.text(250, 528, "Q_C from the cold space", 10.5, "middle", BLUE, "bold")

    # work
    c.arrow(96, 167, 148, 167, GREEN, 2.4)
    c.text(92, 167, "W in", 11, "end", GREEN, "bold")
    c.arrow(812, 417, 760, 417, AMBER, 2.4)
    c.text(816, 411, "W out", 11, "start", AMBER, "bold")
    c.text(816, 428, "(recovered)", 9.5, "start", MUTED)

    c.title_band("WHERE IT IS USED AND WHY IT IS SO SIMPLE", 580)
    c.text(30, 614, "No refrigerant, no phase change, so no charging or leak problem — hence aircraft "
                    "cabin cooling. The price is a low COP at small temperature lifts.", 11.5, "start", INK)
    c.footer()
    return c


# ------------------------------------------------------- 5.4 choosing a refrigerant
def refrigerant_choice():
    c = Canvas(960, 640, "Choosing a refrigerant: the five things that decide it")
    rows = [
        ("Pressure range", "P_H must be modest so the condenser wall stays thin; P_C must stay "
                           "above atmospheric so air cannot leak in.", RED),
        ("Latent heat", "A high latent heat means a small circulation rate and a small compressor "
                        "for the same duty.", GREEN),
        ("Toxicity and flammability", "Safety class A1 is the goal; ammonia is B2L, hydrocarbons are A3.", AMBER),
        ("Environmental impact", "ODP must be zero (Montreal) and GWP low (Kyoto / Kigali).", BLUE),
        ("Cost and availability", "Must be cheap, stable, non-corrosive and easy to recover and recycle.", PD),
    ]
    for i, (head, body, col) in enumerate(rows):
        y = 86 + i * 96
        c.rect(40, y, 880, 78, "#FFFFFF", LINE, 1.4, rx=10)
        c.rect(40, y, 7, 78, col, "none", 0, rx=3)
        c.text(66, y + 26, head, 13, "start", col, "bold")
        c.text(66, y + 52, body, 11.5, "start", INK)

    c.title_band("THE CODING SYSTEM", 570)
    c.text(40, 600, "R-134a  =  CH₂FCF₃:  R = refrigerant, 1 = 1 C, 3 = 3 F, 4 = 4 H, a = isomer "
                    "suffix.   R-717 = NH₃.   R-744 = CO₂.",
           12, "start", PD, "bold")
    c.footer()
    return c


FIGURES = [
    ("d5_refrigeration_loop", refrigeration_loop),
    ("d5_ph_cycle", ph_cycle),
    ("d5_air_refrigeration", air_refrigeration),
    ("d5_refrigerant_choice", refrigerant_choice),
]


def main():
    for name, fn in FIGURES:
        save(fn(), _p(name))
        print("wrote", _p(name))
    return [n for n, _ in FIGURES]


if __name__ == "__main__":
    main()
