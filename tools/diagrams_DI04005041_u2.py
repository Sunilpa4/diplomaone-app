"""Draws the diagrams for DI04005041 (Chemical Engineering Thermodynamics) Unit 2
"First Law of Thermodynamics".

    python3 tools/diagrams_DI04005041_u2.py

Writes content/chemical/sem4/DI04005041/diagrams/*.svg

Original teaching schematics drawn from Narayanan; Smith, Van Ness & Abbott;
Gavhane. Conceptual, not construction or operating drawings.
"""
import d1chem_lib as L
from d1draw import (AMBER, AMBER_FILL, BLUE, BLUE_FILL, Canvas, GREEN, GREEN_FILL, GREY_FILL,
                    INK, LAV, LINE, MUTED, P, PD, RED, RED_FILL, save)

CODE, BRANCH, SEM = "DI04005041", "chemical", 4


def _p(name):
    return L.out_path(BRANCH, SEM, CODE, name)


# --------------------------------------------------- 2.1 energy forms and bookkeeping
def energy_forms():
    c = Canvas(920, 540, "The energy account of a closed system")
    c.text(24, 74, "Total energy E = internal + kinetic + potential + other stored forms",
           12.5, "start", MUTED)

    # the system boundary
    c.rect(300, 120, 320, 300, "#FBFAFE", P, 2.2, rx=12, dash="7 6")
    c.text(460, 146, "SYSTEM", 13, "middle", PD, "bold")
    c.text(460, 168, "mass m fixed", 11, "middle", MUTED)

    # internal energy box inside
    c.rbox(340, 196, 240, 116, "", "#FFFFFF", LINE, rx=10)
    c.text(460, 222, "internal energy  U", 12.5, "middle", PD, "bold")
    c.text(460, 246, "sensible + latent + chemical", 10.5, "middle", MUTED)
    c.text(460, 268, "+ nuclear + electrical", 10.5, "middle", MUTED)
    c.mono(460, 294, "u = U/m   [kJ/kg]", 12, "middle", INK)

    # kinetic and potential
    c.rbox(340, 326, 116, 74, "", "#FFFFFF", GREEN, rx=8)
    c.text(398, 348, "kinetic", 11.5, "middle", GREEN, "bold")
    c.mono(398, 372, "½ m c²", 12, "middle", INK)
    c.text(398, 390, "velocity c", 10, "middle", MUTED)
    c.rbox(464, 326, 116, 74, "", "#FFFFFF", BLUE, rx=8)
    c.text(522, 348, "potential", 11.5, "middle", BLUE, "bold")
    c.mono(522, 372, "m g z", 12, "middle", INK)
    c.text(522, 390, "height z", 10, "middle", MUTED)

    # crossing arrows
    c.arrow(150, 180, 296, 180, RED, 2.2)
    c.text(160, 166, "Q  heat in (+) / out (−)", 11, "start", RED, "bold")
    c.arrow(296, 380, 150, 380, BLUE, 2.2)
    c.text(160, 366, "W  work out (+) / in (−)", 11, "start", BLUE, "bold")

    c.title_band("FIRST LAW FOR A CLOSED SYSTEM BETWEEN TWO STATES", 446)
    c.mono(30, 482, "Q − W = ΔU + Δ(KE) + Δ(PE)", 15, "start", PD, "bold")
    c.note("ΔU is independent of the path; Q and W are not. Their difference is fixed.", 508)
    c.footer()
    return c


# --------------------------------------------------- 2.2 non-flow path comparison
def nonflow_paths():
    c = Canvas(900, 600, "Same two states, two paths: Q and W differ, ΔU does not")
    pt = L.axes(c, 170, 120, 520, 340, "volume  V  (m³) →", "pressure  P  (bar) →",
                [0.2, 0.4, 0.6, 0.8, 1.0], [0.2, 0.4, 0.6, 0.8, 1.0])

    A = (0.25, 0.80)
    B = (0.90, 0.30)
    PA = pt(*A)
    PB = pt(*B)
    C = (0.25, 0.30)
    PC = pt(*C)

    # path 1: isothermal curve A -> B
    last = None
    for i in range(41):
        v = A[0] + (B[0] - A[0]) * i / 40
        p = A[1] * A[0] / v
        if last:
            c.line(*last, *pt(v, p), P, 2.5)
        last = pt(v, p)

    # path 2: A down at constant V, then across at constant P
    c.line(*PA, *PC, BLUE, 2.3, "7 5")
    c.line(*PC, *PB, BLUE, 2.3, "7 5")

    c.circle(PA[0], PA[1], 6, "#FFFFFF", P, 2.4)
    c.circle(PB[0], PB[1], 6, "#FFFFFF", P, 2.4)
    c.text(PA[0] - 12, PA[1] - 14, "state 1", 11.5, "end", PD, "bold")
    c.text(PB[0] + 12, PB[1] - 10, "state 2", 11.5, "start", PD, "bold")

    c.text(*pt(0.50, 0.70), "path 1: reversible isothermal", 11, "start", P, "bold")
    c.text(*pt(0.30, 0.40), "path 2a: constant V", 10.5, "start", BLUE, "bold")
    c.text(*pt(0.56, 0.335), "path 2b: constant P", 10.5, "start", BLUE, "bold")

    c.title_band("WHAT CHANGES AND WHAT DOES NOT", 512)
    rows = [("ΔU", "same by both paths — U is a state function", GREEN),
            ("Q", "different: Q₁ ≠ Q₂", RED),
            ("W", "different: W₁ ≠ W₂", BLUE),
            ("Q − W", "equal: both give ΔU", GREEN)]
    for i, (k, v, col) in enumerate(rows):
        x = 24 + i * 216
        c.rbox(x, 538, 204, 46, "", "#FFFFFF", col, rx=6)
        c.text(x + 12, 552, k, 12.5, "start", col, "bold")
        c.text(x + 12, 570, v, 9.5, "start", MUTED)
    c.footer("Original teaching schematic · areas under the path are not equal, so W is not equal")
    return c


# --------------------------------------------------- 2.3 steady flow energy equation
def steady_flow():
    c = Canvas(920, 640, "Steady-flow energy equation across a control volume")
    c.rect(330, 150, 260, 250, "#FBFAFE", P, 2.2, rx=12)
    c.text(460, 172, "CONTROL VOLUME", 12.5, "middle", PD, "bold")
    c.text(460, 192, "steady: no change with time", 10.5, "middle", MUTED)

    c.line(460, 150, 460, 330, INK, 1.8, "6 4")   # shaft (work transfer), dashed = imaginary
    c.circle(460, 150, 9, "#FFFFFF", INK, 1.8)
    c.text(478, 226, "shaft", 10.5, "start", MUTED)

    # inlet
    L.arrow_stream(c, [(120, 210), (326, 210)])
    c.mono(150, 192, "m_in ,  h_in ,  c_in ,  z_in", 11.5, "start", GREEN, "bold")
    c.text(150, 232, "state 1", 10.5, "start", MUTED)

    # outlet
    L.arrow_stream(c, [(594, 340), (800, 340)])
    c.mono(636, 322, "m_out ,  h_out ,  c_out ,  z_out", 11.5, "start", RED, "bold")
    c.text(636, 362, "state 2", 10.5, "start", MUTED)

    # heat and work
    c.arrow(220, 130, 326, 130, AMBER, 2.2)
    c.text(150, 118, "Q  (+ into the fluid)", 11, "start", AMBER, "bold")
    c.arrow(460, 400, 460, 452, BLUE, 2.2)
    c.text(472, 432, "W_s  shaft work out", 11, "start", BLUE, "bold")

    c.title_band("ENERGY IN = ENERGY OUT  (steady state, no accumulation)", 486)
    c.mono(30, 520, "Q − W_s = m [ (h₂ − h₁) + ½(c₂² − c₁²) + g(z₂ − z₁) ]",
           14, "start", PD, "bold")
    c.text(30, 550, "per unit mass:   q − w_s = (h₂ − h₁) + ½(c₂² − c₁²) + g(z₂ − z₁)",
           12, "start", INK)
    c.note("Assumptions: steady flow, uniform properties at each section, no change of "
           "potential or kinetic energy neglected, single inlet and single outlet.", 592)
    c.footer()
    return c


# --------------------------------------------------- 2.4 heat capacity
def heat_capacity():
    c = Canvas(900, 660, "Heat capacity at constant volume and at constant pressure")
    pt = L.axes(c, 170, 120, 520, 320, "temperature  T  (K) →", "energy  (kJ/kg) →",
                [0.25, 0.5, 0.75, 1.0], [0.25, 0.5, 0.75, 1.0])

    # two straight lines with different slopes (slope = heat capacity)
    c.line(*pt(0.0, 0.05), *pt(1.0, 0.55), P, 2.6)
    c.line(*pt(0.0, 0.05), *pt(1.0, 0.80), BLUE, 2.6)
    c.text(*pt(0.62, 0.36), "slope = c_v", 11.5, "start", P, "bold")
    c.text(*pt(0.55, 0.72), "slope = c_p", 11.5, "start", BLUE, "bold")

    c.title_band("WHY c_p IS ALWAYS BIGGER THAN c_v FOR A GAS", 512)
    c.text(30, 546, "At constant volume all the heat raises the temperature (and pressure).",
           11.5, "start", INK)
    c.text(30, 568, "At constant pressure the gas also expands, so part of the heat leaves as work.",
           11.5, "start", INK)
    c.mono(30, 606, "c_p − c_v = R", 16, "start", PD, "bold")
    c.text(250, 606, "(ideal gas, per mole;   c_p / c_v = γ)", 12, "start", INK)
    c.footer()
    return c


# --------------------------------------------------- driver
FIGURES = [
    ("d2_energy_forms", energy_forms),
    ("d2_nonflow_paths", nonflow_paths),
    ("d2_steady_flow", steady_flow),
    ("d2_heat_capacity", heat_capacity),
]


def main():
    for name, fn in FIGURES:
        save(fn(), _p(name))
        print("wrote", _p(name))
    return [n for n, _ in FIGURES]


if __name__ == "__main__":
    main()
