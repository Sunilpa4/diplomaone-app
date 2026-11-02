"""Draws the diagrams for DI04005041 Unit 4 "Second Law of Thermodynamics".

    python3 tools/diagrams_DI04005041_u4.py

Original teaching schematics (Narayanan; Smith, Van Ness & Abbott; Gavhane).
"""
import d1chem_lib as L
from d1draw import (AMBER, AMBER_FILL, BLUE, BLUE_FILL, Canvas, GREEN, GREEN_FILL, GREY_FILL,
                    INK, LAV, LINE, MUTED, P, PD, RED, RED_FILL, save)

CODE, BRANCH, SEM = "DI04005041", "chemical", 4


def _p(name):
    return L.out_path(BRANCH, SEM, CODE, name)


# ------------------------------------------------------- 4.1 heat engine / pump / refrigerator
def heat_devices():
    c = Canvas(960, 620, "Heat engine, refrigerator and heat pump")
    panels = [
        ("HEAT ENGINE", 24, GREEN, "supplies work"),
        ("REFRIGERATOR", 340, BLUE, "cools a cold space"),
        ("HEAT PUMP", 656, RED, "heats a warm space"),
    ]
    for title, x, col, sub in panels:
        c.rect(x, 110, 280, 400, "#FFFFFF", LINE, 1.6, rx=12)
        c.text(x + 140, 136, title, 13, "middle", col, "bold")
        c.text(x + 140, 156, sub, 10.5, "middle", MUTED)
        # hot reservoir
        c.rbox(x + 40, 176, 200, 42, "", "#FDF1F1", RED, rx=6)
        c.text(x + 140, 197, "hot reservoir  T_H", 11, "middle", RED, "bold")
        # cold reservoir
        c.rbox(x + 40, 402, 200, 42, "", "#EEF5FD", BLUE, rx=6)
        c.text(x + 140, 423, "cold reservoir  T_C", 11, "middle", BLUE, "bold")
        # device
        c.circle(x + 140, 310, 44, LAV, P, 2)
        c.text(x + 140, 306, "device", 10.5, "middle", PD, "bold")
        c.text(x + 140, 322, "cyclic", 9.5, "middle", MUTED)

    # engine arrows: Q_H in from hot, W out, Q_C out to cold
    x = 24
    c.arrow(x + 140, 220, x + 140, 262, RED, 2.2)
    c.text(x + 152, 244, "Q_H", 11, "start", RED, "bold")
    c.arrow(x + 184, 310, x + 246, 310, GREEN, 2.2)
    c.text(x + 196, 294, "W", 11, "start", GREEN, "bold")
    c.arrow(x + 140, 356, x + 140, 398, BLUE, 2.2)
    c.text(x + 152, 382, "Q_C", 11, "start", BLUE, "bold")

    # refrigerator: W in, Q_C in from cold, Q_H out to hot
    x = 340
    c.arrow(x + 246, 310, x + 184, 310, GREEN, 2.2)
    c.text(x + 236, 294, "W", 11, "end", GREEN, "bold")
    c.arrow(x + 140, 398, x + 140, 356, BLUE, 2.2)
    c.text(x + 152, 382, "Q_C", 11, "start", BLUE, "bold")
    c.arrow(x + 140, 262, x + 140, 220, RED, 2.2)
    c.text(x + 152, 244, "Q_H", 11, "start", RED, "bold")

    # heat pump: W in, Q_C in, Q_H out (larger)
    x = 656
    c.arrow(x + 246, 310, x + 184, 310, GREEN, 2.2)
    c.text(x + 236, 294, "W", 11, "end", GREEN, "bold")
    c.arrow(x + 140, 398, x + 140, 356, BLUE, 2.2)
    c.text(x + 152, 382, "Q_C", 11, "start", BLUE, "bold")
    c.arrow(x + 140, 262, x + 140, 220, RED, 2.6)
    c.text(x + 152, 244, "Q_H = Q_C + W", 10.5, "start", RED, "bold")

    c.title_band("THE ENERGY ACCOUNT OF EACH DEVICE", 536)
    c.text(30, 566, "Engine: W = Q_H − Q_C ,  η = W/Q_H.        "
                    "Refrigerator: COP_R = Q_C/W.        Heat pump: COP_HP = Q_H/W = COP_R + 1.",
           11.5, "start", INK)
    c.note("All three obey the first law; only the second law says which direction is possible.", 596)
    c.footer()
    return c


# ------------------------------------------------------- 4.2 Carnot cycle
def carnot_cycle():
    """A genuinely closed cycle: two isotherms and two adiabats that share their corners."""
    c = Canvas(960, 660, "The Carnot cycle on a P–V diagram")
    pt = L.axes(c, 170, 120, 520, 330, "volume  V  →", "pressure  P  →",
                [0.25, 0.5, 0.75, 1.0], [0.25, 0.5, 0.75, 1.0])

    # corners chosen from T_H/T_C = 0.6 and gamma = 1.4, then scaled to the axes
    G = 1.4
    V1, P1 = 0.136, 0.845
    V2, P2 = 0.255, 0.451
    V3, P3 = 0.915, 0.0754
    V4, P4 = 0.489, 0.1410

    def seg(v1, p1, v2, p2, color, iso=True):
        pts = []
        for i in range(41):
            v = v1 + (v2 - v1) * i / 40
            p = (p1 * v1 / v) if iso else p1 * (v1 / v) ** G
            pts.append(pt(v, p))
        for i in range(len(pts) - 1):
            c.line(*pts[i], *pts[i + 1], color, 2.6)

    seg(V1, P1, V2, P2, RED, iso=True)      # 1 -> 2 isothermal at T_H
    seg(V2, P2, V3, P3, AMBER, iso=False)   # 2 -> 3 adiabatic
    seg(V3, P3, V4, P4, BLUE, iso=True)     # 3 -> 4 isothermal at T_C
    seg(V4, P4, V1, P1, AMBER, iso=False)   # 4 -> 1 adiabatic

    for (v, q), name, dx, dy, anchor in [((V1, P1), "1", -13, -8, "end"),
                                         ((V2, P2), "2", 13, -6, "start"),
                                         ((V3, P3), "3", 12, 12, "start"),
                                         ((V4, P4), "4", -13, 12, "end")]:
        px, py = pt(v, q)
        c.circle(px, py, 7, "#FFFFFF", PD, 2.2)
        c.text(px + dx, py + dy, name, 12.5, anchor, PD, "bold")

    c.text(*pt(0.175, 0.90), "1→2   isothermal at T_H", 10.5, "start", RED, "bold")
    c.text(*pt(0.40, 0.30), "2→3   adiabatic", 10, "start", AMBER, "bold")
    c.text(*pt(0.60, 0.135), "3→4   isothermal at T_C", 10.5, "start", BLUE, "bold")
    c.text(*pt(0.30, 0.395), "4→1  adiabatic", 10.5, "end", AMBER, "bold")

    c.title_band("WHY IT IS THE MOST EFFICIENT CYCLE POSSIBLE", 490)
    notes = ["Every process is reversible: heat is added and rejected isothermally at the two "
             "reservoir temperatures.",
             "No heat crosses a finite temperature difference, so no entropy is generated.",
             "The enclosed area is the net work  W = Q_H − Q_C.",
             "Its efficiency depends only on the two temperatures:   η = 1 − T_C/T_H."]
    for i, n in enumerate(notes):
        c.text(30, 524 + i * 23, "• " + n, 11.5, "start", INK)
    c.footer()
    return c


# ------------------------------------------------------- 4.3 T-s diagram
def ts_diagram():
    c = Canvas(940, 640, "The same Carnot cycle on a T–S diagram")
    pt = L.axes(c, 170, 120, 500, 330, "entropy  S  →", "temperature  T  →",
                [0.25, 0.5, 0.75, 1.0], [0.4, 0.6, 0.8, 1.0])

    A = pt(0.20, 0.95)
    B = pt(0.80, 0.95)
    C = pt(0.80, 0.45)
    D = pt(0.20, 0.45)

    c.line(*A, *B, RED, 2.8)
    c.line(*B, *C, AMBER, 2.8)
    c.line(*C, *D, BLUE, 2.8)
    c.line(*D, *A, AMBER, 2.8)

    # shaded area = net work
    c.poly([A, B, C, D], "#EFE4FB", "none", 0)

    for q, name, dx, dy, anchor in [(A, "1", -16, 4, "end"), (B, "2", 14, 4, "start"),
                                    (C, "3", 14, 4, "start"), (D, "4", -16, 4, "end")]:
        c.circle(q[0], q[1], 7, "#FFFFFF", PD, 2.2)
        c.text(q[0] + dx, q[1] + dy, name, 12.5, anchor, PD, "bold")

    c.text((A[0] + B[0]) / 2, A[1] - 16, "T_H = constant", 11, "middle", RED, "bold")
    c.text((C[0] + D[0]) / 2, C[1] + 22, "T_C = constant", 11, "middle", BLUE, "bold")
    c.text((A[0] + B[0]) / 2, (A[1] + C[1]) / 2, "net work = shaded area", 12, "middle", PD, "bold")
    c.text((A[0] + B[0]) / 2, (A[1] + C[1]) / 2 + 20, "W = (T_H − T_C)(S₂ − S₁)", 11, "middle", INK)

    c.title_band("THE RECTANGLE IS THE REASON", 486)
    notes = ["Heat added at T_H is the area under 1→2:  Q_H = T_H (S₂ − S₁).",
             "Heat rejected at T_C is the area under 3→4:  Q_C = T_C (S₂ − S₁).",
             "Net work is the difference of the two rectangles, hence η = 1 − T_C/T_H.",
             "On this diagram a reversible cycle is a closed loop; the area inside it is the work."]
    for i, n in enumerate(notes):
        c.text(30, 520 + i * 23, "• " + n, 11.5, "start", INK)
    c.footer()
    return c


# ------------------------------------------------------- 4.4 entropy and the Clausius inequality
def clausius():
    c = Canvas(940, 640, "Entropy generation and the Clausius inequality")
    c.text(24, 76, "∮ δQ/T ≤ 0 for any cycle:  equality for reversible, less than zero for real cycles",
           12, "start", MUTED)

    # reversible path vs real path
    c.rbox(40, 120, 400, 120, "", "#F8FDF9", GREEN, rx=10)
    c.text(60, 148, "REVERSIBLE", 12.5, "start", GREEN, "bold")
    c.text(60, 176, "∮ δQ/T = 0", 15, "start", PD, "bold")
    c.text(60, 204, "no entropy is generated inside the system", 10.5, "start", MUTED)
    c.text(60, 224, "S₂ − S₁ = ∫ δQ_rev / T", 11, "start", INK)

    c.rbox(480, 120, 420, 120, "", "#FEF8F8", RED, rx=10)
    c.text(500, 148, "IRREVERSIBLE (every real cycle)", 12.5, "start", RED, "bold")
    c.text(500, 176, "∮ δQ/T < 0", 15, "start", PD, "bold")
    c.text(500, 204, "entropy is generated: S_gen > 0", 10.5, "start", MUTED)
    c.text(500, 224, "S₂ − S₁ = ∫ δQ/T + S_gen", 11, "start", INK)

    c.title_band("WHERE THE ENTROPY COMES FROM", 268)
    items = [("friction", "mechanical work turns into heat inside the fluid"),
             ("unrestrained expansion", "a gas rushing into vacuum creates entropy"),
             ("heat across a finite ΔT", "the classic irreversibility in any exchanger"),
             ("mixing of two streams", "different compositions blend irreversibly"),
             ("electrical resistance", "all the electrical work becomes heat"),
             ("chemical reaction", "reaction at a finite rate always generates entropy")]
    for i, (name, why) in enumerate(items):
        x = 40 + (i % 2) * 460
        y = 302 + (i // 2) * 44
        c.rect(x, y - 12, 6, 16, RED, "none", 0)
        c.text(x + 16, y, name, 11.5, "start", RED, "bold")
        c.text(x + 16, y + 18, why, 10.5, "start", MUTED)

    c.title_band("THE THREE STATEMENTS ARE THE SAME LAW", 492)
    c.text(40, 526, "Kelvin–Planck: no engine can convert all the heat from one reservoir into work.",
           11.5, "start", INK)
    c.text(40, 550, "Clausius: heat cannot flow by itself from a colder to a hotter body.",
           11.5, "start", INK)
    c.text(40, 574, "Entropy: the entropy of the universe never decreases.   ΔS_universe ≥ 0",
           12, "start", PD, "bold")
    c.footer()
    return c


FIGURES = [
    ("d4_heat_devices", heat_devices),
    ("d4_carnot_cycle", carnot_cycle),
    ("d4_ts_diagram", ts_diagram),
    ("d4_clausius", clausius),
]


def main():
    for name, fn in FIGURES:
        save(fn(), _p(name))
        print("wrote", _p(name))
    return [n for n, _ in FIGURES]


if __name__ == "__main__":
    main()
