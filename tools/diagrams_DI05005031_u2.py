"""Five figures for Chemical Reaction Engineering (DI05005031) Unit 2 - kinetics of homogeneous
reactions: the two terms of a rate law, the Arrhenius plot, activation energy from data, the energy
barrier with and without a catalyst, and the chain mechanism that makes an order fractional."""
import math

from diagrams_DI05005031_lib import (INK, GREY, THIN, BLUE, GREEN, ORANGE, RED, PURPLE, TEAL, W,
                                     svg, text, ln, arrow, heading, foot, panel, axes, curve, dots,
                                     guide, box, note_box)

TITLES = {
    "u2_terms": "A rate law is two terms multiplied",
    "u2_arrhenius": "The Arrhenius law, as k(T) and as a straight line",
    "u2_ea": "Activation energy from ln k against 1/T",
    "u2_barrier": "The barrier, with and without a catalyst",
    "u2_chain": "Why a chain reaction gives a fractional order",
}

CAPTIONS = {
    "u2_terms": "The concentration term is chemistry and the temperature term is exponential; a rate "
                "law is measured once and then used at any temperature through k(T).",
    "u2_arrhenius": "k rises exponentially with T, but ln k falls linearly with 1/T - which is why "
                    "the laboratory plot is a straight line whose slope gives Ea.",
    "u2_ea": "Three rate constants at three temperatures fix the line; the slope is -Ea/R, so Ea is "
             "read off in J/mol without any curve fitting.",
    "u2_barrier": "A catalyst opens a second route with a lower peak; the two levels of reactant and "
                  "product, and therefore dH and K_eq, are untouched.",
    "u2_chain": "Bromine atoms start and carry the reaction; because a termination step competes with "
                "propagation, the measured order in Br2 is 1.5 and not the molecularity 2.",
}


def terms():
    b = heading("The rate law: chemistry x temperature")
    b += f'<rect x="46" y="50" width="268" height="34" rx="6" fill="#F5EEFD" stroke="{PURPLE}" ' \
         f'stroke-width="1.5"/>'
    b += text(180, 72, "-rA = k(T) x f(C)", 12.6, weight="bold", color=PURPLE)
    for x, color, title, formula, note in [
            (24, RED, "k(T): temperature term", "k = A exp(-Ea/RT)", "one number per T"),
            (186, BLUE, "f(C): concentration term", "f(C) = CA^a CB^b ...", "the order lives here")]:
        b += f'<rect x="{x}" y="104" width="150" height="66" rx="5" fill="#FFFFFF" ' \
             f'stroke="{color}" stroke-width="1.3"/>'
        b += text(x + 75, 119, title, 8.2, weight="bold", color=color)
        b += text(x + 75, 139, formula, 8.6, weight="bold", color=INK)
        b += text(x + 75, 155, note, 7.2, color=GREY)
    b += ln(99, 84, 99, 104, THIN, 1.0)
    b += ln(261, 84, 261, 104, THIN, 1.0)
    b += text(180, 192, "measured together at one temperature (Unit 3)", 7.6, color=INK)
    b += text(180, 206, "then k is re-computed for any other T with Arrhenius", 7.6, color=INK)
    b += text(180, 221, "f(C) never changes with temperature", 7.6, color=TEAL, weight="bold")
    b += foot(238, "This split is the reason a kineticist reports an order and an activation energy:")
    b += foot(250, "those two numbers carry the whole rate law over the whole plant.")
    return svg(W, 262, b)


def arrhenius():
    b = heading("The same law drawn two ways")
    ea, R, lnA = 50000.0, 8.314, 21.0
    # left: k against T, normalised to its value at 350 K
    b += panel(8, 44, 168, 168)
    b += text(92, 58, "k against T", 8.0, weight="bold", color=INK)
    x0, y0, w, h = 30, 72, 122, 100
    b += axes(x0, y0, w, h, "T", "k", xticks=[(0.0, "290"), (1.0, "350")], yticks=[])
    top = math.exp(-ea / (R * 350))
    pts = []
    for k in range(61):
        T = 290 + k / 60 * 60
        pts.append((x0 + k / 60 * w, y0 + h - 0.92 * h * math.exp(-ea / (R * T)) / top))
    b += curve(pts, BLUE, 2.0)
    # right: ln k against 1/T, a straight line
    b += panel(184, 44, 168, 168)
    b += text(268, 58, "ln k against 1/T", 8.0, weight="bold", color=INK)
    x1, y1, w1, h1 = 208, 72, 118, 100
    b += axes(x1, y1, w1, h1, "1/T", "ln k", xticks=[(0.0, "1/350"), (1.0, "1/290")], yticks=[])
    lo, hi = lnA - (ea / R) / 290.0, lnA - (ea / R) / 350.0

    def yy(inv):
        v = lnA - (ea / R) * inv
        return y1 + h1 - 0.06 * h1 - (v - lo) / (hi - lo) * 0.86 * h1

    a = (x1, yy(1 / 350.0))
    c = (x1 + w1, yy(1 / 290.0))
    b += curve([a, c], RED, 2.0)
    b += dots([a, c], RED, 2.4)
    b += text(x1 + w1 * 0.34, y1 + h1 * 0.30, "slope = -Ea/R", 7.8, color=RED, weight="bold")
    b += foot(224, "Left: doubling every 10 K near room temperature. Right: the")
    b += foot(236, "same data, but a straight line whose slope is -Ea/R.")
    return svg(W, 250, b)


def ea():
    b = heading("Reading Ea off the line")
    x0, y0, w, h = 52, 58, 232, 150
    b += axes(x0, y0, w, h, "1/T  (K-1)", "ln k", xticks=[(0.0, "3.1"), (0.5, "3.3"),
                                                          (1.0, "3.5")], yticks=[])
    # data: ln k from -8.2 to -5.6 as 1/T goes 3.10e-3 -> 3.50e-3
    pts = []
    for f in (0.0, 0.5, 1.0):
        lnk = -8.2 + f * 2.6
        pts.append((x0 + f * w, y0 + h - (lnk + 8.6) / 3.4 * h))
    b += curve([(pts[0][0] - 6, pts[0][1] + 6), (pts[-1][0] + 6, pts[-1][1] - 6)], RED, 1.8)
    b += dots(pts, RED, 2.6)
    for i, p in enumerate(pts):
        b += text(p[0] + (6 if i == 0 else 0), p[1] - 9, f"T{i + 1}", 7.4, color=INK,
                  weight="bold")
    # slope triangle
    ax, ay = pts[0]
    bx, by = pts[-1]
    b += guide(ax, by, bx, by, THIN)
    b += guide(ax, ay, ax, by, THIN)
    b += text((ax + bx) / 2, by - 6, "d(1/T)", 7.4, color=GREY)
    b += text(ax - 6, (ay + by) / 2, "d ln k", 7.4, anchor="end", color=GREY)
    b += note_box(20, 218, 320, 36, "Ea = -R x slope: three points give three checks", (), size=7.4)
    b += text(180, 244, "slope = d ln k / d(1/T) = -Ea/R, so Ea = 8.314 x |slope| J/mol", 7.4,
              color=INK)
    b += foot(270, "Two points are enough for an exam answer; a line through three")
    b += foot(282, "or more is what a report needs, because it shows the scatter.")
    return svg(W, 294, b)


def _route(ax, w, yr, yp, peak, f_peak=0.40, f_end=0.62):
    """Energy profile from R through a peak to P: flat, rise, fall, flat - never dipping."""
    pts = []
    for k in range(81):
        f = k / 80
        if f <= f_peak:
            t = f / f_peak
            y = yr + (peak - yr) * (0.5 - 0.5 * math.cos(math.pi * t))
        elif f <= f_end:
            t = (f - f_peak) / (f_end - f_peak)
            y = peak + (yp - peak) * (0.5 - 0.5 * math.cos(math.pi * t))
        else:
            y = yp
        pts.append((ax + f * w, y))
    return pts


def barrier():
    b = heading("Two routes over the same barrier")
    ax, ay, w, h = 40, 70, 280, 120
    yr = ay + h * 0.62
    yp = yr - 22
    b += curve(_route(ax, w, yr, yp, yr - 60), RED, 2.2)
    b += curve(_route(ax, w, yr, yp, yr - 30, f_end=0.56), GREEN, 2.2)
    b += ln(ax - 8, yr, ax + w + 8, yr, THIN, 0.8, dash="2,2")
    b += ln(ax - 8, yp, ax + w + 8, yp, THIN, 0.8, dash="2,2")
    b += text(ax - 10, yr + 3, "R", 7.4, anchor="end", color=BLUE, weight="bold")
    b += text(ax + w + 10, yp + 3, "P", 7.4, anchor="start", color=GREEN, weight="bold")
    b += arrow(ax + 0.24 * w, yr - 2, ax + 0.24 * w, yr - 60 + 2, RED, 1.1, 4)
    b += text(ax + 0.24 * w - 6, yr - 34, "Ea", 8.0, anchor="end", color=RED, weight="bold")
    b += arrow(ax + 0.52 * w, yr - 2, ax + 0.52 * w, yr - 30 + 2, GREEN, 1.1, 4)
    b += text(ax + 0.55 * w, yr - 40, "Ea' catalysed", 8.0, anchor="start", color=GREEN,
              weight="bold")
    b += text(180, 62, "uncatalysed route in red, catalysed in green", 7.6, color=GREY)
    b += foot(228, "Both routes start at R and finish at P: the catalysed one merely passes a lower")
    b += foot(240, "peak, so more molecules have enough energy at the same temperature.")
    b += foot(254, "dH is the vertical gap R to P and does not move; K_eq does not move either.")
    return svg(W, 266, b)


def chain():
    b = heading("H2 + Br2 -> 2 HBr: a chain with three kinds of step")
    rows = [
        (52, "Initiation", "Br2 -> 2 Br.", RED, "start the chain"),
        (100, "Propagation 1", "Br. + H2 -> HBr + H.", BLUE, "carry it on"),
        (134, "Propagation 2", "H. + Br2 -> HBr + Br.", BLUE, "regenerate Br."),
        (184, "Termination", "2 Br. -> Br2", TEAL, "kill the chain"),
    ]
    for y, name, rxn, color, note in rows:
        b += f'<rect x="18" y="{y - 14}" width="150" height="30" rx="5" fill="#FFFFFF" ' \
             f'stroke="{color}" stroke-width="1.3"/>'
        b += text(26, y - 2, name, 7.6, anchor="start", weight="bold", color=color)
        b += text(26, y + 10, rxn, 7.4, anchor="start", color=INK)
        b += text(200, y + 2, note, 7.0, anchor="start", color=GREY)
    # the propagation loop
    b += text(18, 210, "Rate law that comes out of the steady state on [Br.] :", 7.6,
              anchor="start", color=INK, weight="bold")
    b += text(180, 226, "r = k [H2] [Br2]^1.5 / ([Br2] + k' [HBr])", 8.6, color=PURPLE,
              weight="bold")
    b += foot(252, "The equation needs two molecules, so an elementary step would be")
    b += foot(264, "second order in all; measured it is 1 in H2 and 1.5 in Br2 - the")
    b += foot(276, "chain, not the equation, decides the law.")
    return svg(W, 288, b)


DIAGRAMS = {
    "u2_terms": terms,
    "u2_arrhenius": arrhenius,
    "u2_ea": ea,
    "u2_barrier": barrier,
    "u2_chain": chain,
}
