"""Six figures for Chemical Reaction Engineering (DI05005031) Unit 1 - basics of chemical reactions.

Each figure answers one question of the unit: where the subject sits among its neighbours, how the
reactions are classified, what an energy profile is, on what basis a rate can be written, what changes
a rate, and how an enzyme reaction behaves.
"""
import math

from diagrams_DI05005031_lib import (INK, GREY, THIN, BLUE, GREEN, ORANGE, RED, PURPLE, TEAL, W,
                                     svg, text, ln, arrow, heading, foot, panel, box, axes, curve,
                                     dots, guide)

TITLES = {
    "u1_map": "Where reaction engineering sits",
    "u1_tree": "Six ways to classify a reaction",
    "u1_energy": "Energy profile: exothermic and endothermic",
    "u1_basis": "Four bases on which a rate is written",
    "u1_variables": "What changes the rate of a reaction",
    "u1_mm": "Enzyme kinetics: the Michaelis-Menten curve",
}

CAPTIONS = {
    "u1_map": "A reactor is sized with kinetics, but it must also be fed, stirred, heated and paid "
              "for - that is why the design pulls six other subjects together.",
    "u1_tree": "The same reaction can be described by its phases, its catalyst, its direction, its "
               "molecularity, its heat and its order; the exam may ask for any one of the six.",
    "u1_energy": "The peak is the activation energy, the step between the two levels is the heat of "
                 "reaction; the catalyst lowers the peak, never the step.",
    "u1_basis": "The same moles per second is divided by a volume, a mass of catalyst, an area or a "
                "mass of solid, and the unit of the rate constant changes with it.",
    "u1_variables": "Concentration and temperature are the two the designer controls directly; the "
                    "rest - catalyst, area, light, solvent - are chosen when the reactor is built.",
    "u1_mm": "An enzyme saturates: at low substrate the rate is first order in S, at high substrate "
             "it is zero order and the rate locks at Vmax.",
}


def map_():
    b = heading("Reaction engineering borrows from six sides")
    cx, cy = 180, 132
    b += f'<circle cx="{cx}" cy="{cy}" r="40" fill="#F5EEFD" stroke="{PURPLE}" stroke-width="1.8"/>'
    b += text(cx, cy - 8, "Reactor", 10.4, weight="bold", color=PURPLE)
    b += text(cx, cy + 6, "design", 10.4, weight="bold", color=PURPLE)
    b += text(cx, cy + 22, "V, T, X, t", 8.0, color=GREY)
    spots = [(64, 54, "Thermodynamics", "how far it goes"),
             (296, 54, "Kinetics", "how fast it goes"),
             (58, 132, "Fluid mechanics", "how it is mixed"),
             (302, 132, "Heat transfer", "how T is held"),
             (64, 210, "Mass transfer", "how it reaches"),
             (296, 210, "Economics", "what it costs")]
    for x, y, name, sub in spots:
        b += f'<rect x="{x - 52}" y="{y - 15}" width="104" height="30" rx="6" fill="#FFFFFF" ' \
             f'stroke="{BLUE}" stroke-width="1.2"/>'
        b += text(x, y - 3, name, 8.2, weight="bold", color=INK)
        b += text(x, y + 9, sub, 7.0, color=GREY)
        dx, dy = cx - x, cy - y
        d = math.hypot(dx, dy)
        b += ln(x + dx / d * 56, y + dy / d * 18, cx - dx / d * 42, cy - dy / d * 42, THIN, 0.9)
    b += foot(246, "The reactor is where the six meet: kinetics fixes the size,")
    b += foot(258, "the others decide whether it can be fed, stirred and heated.")
    return svg(W, 270, b)


def tree():
    b = heading("Six classifications the syllabus asks for")
    b += box(120, 44, 120, 24, "Chemical reactions", color=PURPLE, size=8.8)
    b += ln(180, 68, 180, 78, THIN, 1.0)
    cats = [
        (12, 88, "By phase", "homogeneous", "one phase only", "heterogeneous", "two phases"),
        (124, 88, "By catalyst", "catalytic", "a catalyst is used", "non-catalytic", "no catalyst"),
        (236, 88, "By direction", "reversible", "runs both ways", "irreversible", "runs one way"),
        (12, 158, "By molecularity", "unimolecular", "A -> P", "bimolecular", "A + B -> P"),
        (124, 158, "By heat", "exothermic", "gives out heat", "endothermic", "takes in heat"),
        (236, 158, "By order", "zero, first", "order n", "second, nth", "from data"),
    ]
    for x, y, name, a1, a2, b1, b2 in cats:
        b += f'<rect x="{x}" y="{y}" width="112" height="58" rx="5" fill="#FFFFFF" ' \
             f'stroke="{BLUE}" stroke-width="1.1"/>'
        b += f'<rect x="{x}" y="{y}" width="112" height="17" rx="5" fill="#EAF2FB"/>'
        b += text(x + 56, y + 12, name, 7.6, weight="bold", color=INK)
        b += text(x + 56, y + 30, f"{a1}  -  {a2}", 6.8, color=INK)
        b += text(x + 56, y + 45, f"{b1}  -  {b2}", 6.8, color=GREY)
    b += foot(228, "Molecularity counts molecules in one step; order is what")
    b += foot(240, "the experiment measures - they agree only when elementary.")
    return svg(W, 252, b)


def _profile(ax, ay, w, h, up, color):
    """One energy profile: reactant level, a peak, a product level `up` pixels above (or below)."""
    yr = ay + h * 0.55
    yp = yr - up
    peak = min(yr, yp) - h * 0.46
    pts = []
    for k in range(81):
        f = k / 80
        base = yr + (yp - yr) * (1 / (1 + math.exp(-(f - 0.62) * 16)))
        hump = (yr - peak) * math.exp(-((f - 0.42) ** 2) / 0.010)
        pts.append((ax + f * w, base - hump))
    return pts, yr, yp, peak


def energy():
    b = heading("Potential energy along the reaction coordinate")
    for x0, title, drop, color, level_tag in [
            (8, "Exothermic: products lower", -26, RED, "dH negative, heat given out"),
            (186, "Endothermic: products higher", 26, ORANGE, "dH positive, heat taken in")]:
        b += panel(x0, 46, 166, 158)
        b += text(x0 + 83, 60, title, 8.0, weight="bold", color=INK)
        ax, ay, w, h = x0 + 24, 90, 120, 80
        pts, yr, yp, peak = _profile(ax, ay, w, h, drop, color)
        b += ln(ax - 6, yr, ax + 6, yr, BLUE, 2.0)
        b += ln(ax + w - 6, yp, ax + w + 6, yp, GREEN, 2.0)
        b += curve(pts, color, 2.0)
        b += ln(ax - 8, yr, ax + w + 8, yr, THIN, 0.8, dash="2,2")
        b += ln(ax - 8, yp, ax + w + 8, yp, THIN, 0.8, dash="2,2")
        b += text(ax - 10, yr + 3, "R", 7.4, anchor="end", color=BLUE, weight="bold")
        b += text(ax + w + 10, yp + 3, "P", 7.4, anchor="start", color=GREEN, weight="bold")
        px = ax + 0.30 * w
        pk_x = ax + 0.42 * w
        b += ln(px, peak, pk_x, peak, PURPLE, 0.9, dash="2,2")
        b += arrow(px, yr - 2, px, peak + 2, PURPLE, 1.1, 4)
        b += text(px - 4, (yr + peak) / 2 + 3, "Ea", 8.2, anchor="end", color=PURPLE,
                  weight="bold")
        bx = ax + w + 13
        b += ln(bx, yr, bx, yp, ORANGE, 1.1)
        b += ln(bx - 3, yr, bx + 3, yr, ORANGE, 1.1)
        b += ln(bx - 3, yp, bx + 3, yp, ORANGE, 1.1)
        b += text(bx, min(yr, yp) - 6, "dH", 7.2, anchor="middle", color=ORANGE,
                  weight="bold")
        b += text(x0 + 83, 176, level_tag, 7.4, color=color, weight="bold")
        b += text(x0 + 83, 190, "a catalyst lowers Ea, not dH", 7.0, color=TEAL)
    b += foot(220, "Left: products below the reactants, so the reactor is cooled.")
    b += foot(232, "Right: products above, so it is heated. In both, the molecules")
    b += foot(244, "must clear the peak Ea - that peak is what T and catalyst act on.")
    return svg(W, 256, b)


def basis():
    b = heading("One rate, four denominators")
    cells = [
        (14, 54, "Per volume of fluid", "-rA = (1/V) dnA/dt", "mol / (m3 s)", "batch, CSTR, PFR",
         BLUE),
        (190, 54, "Per mass of catalyst", "-rA' = (1/Wc) dnA/dt", "mol / (kg s)", "fixed bed",
         GREEN),
        (14, 148, "Per area of catalyst", "-rA'' = (1/S) dnA/dt", "mol / (m2 s)", "gas-liquid",
         ORANGE),
        (190, 148, "Per mass of solid", "-rA''' = (1/m) dnA/dt", "mol / (kg s)", "fluid-solid",
         PURPLE),
    ]
    for x, y, name, formula, unit, use, color in cells:
        b += f'<rect x="{x}" y="{y}" width="156" height="82" rx="6" fill="#FFFFFF" ' \
             f'stroke="{color}" stroke-width="1.2"/>'
        b += text(x + 78, y + 16, name, 8.2, weight="bold", color=color)
        b += text(x + 78, y + 36, formula, 8.6, weight="bold", color=INK)
        b += text(x + 78, y + 52, unit, 8.0, color=GREY)
        b += text(x + 78, y + 67, use, 7.4, color=GREY)
    b += foot(248, "The moles per second are the same in all four; only the")
    b += foot(260, "denominator changes, and with it the unit of k.")
    return svg(W, 284, b)


def variables():
    b = heading("Rate as a function of what you can change")
    cx, cy, r = 180, 136, 44
    b += f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="#F5EEFD" stroke="{PURPLE}" stroke-width="1.7"/>'
    b += text(cx, cy - 10, "r = f (", 9.6, weight="bold", color=PURPLE)
    b += text(cx, cy + 4, "C, T,", 9.6, weight="bold", color=PURPLE)
    b += text(cx, cy + 18, "catalyst, ...)", 9.0, weight="bold", color=PURPLE)
    spokes = [
        (60, 52, "Concentration", "r = k C^n", BLUE, "more collisions"),
        (300, 52, "Temperature", "k = A e^(-Ea/RT)", RED, "about doubles in 10 K"),
        (62, 140, "Pressure", "p = C R T", TEAL, "gas volume shrinks"),
        (298, 140, "Catalyst", "lowers Ea", GREEN, "new path, same dH"),
        (72, 232, "Surface area", "area per volume", ORANGE, "grinding, packing"),
        (290, 232, "Solvent, light", "changes k", GREY, "photolysis, polarity"),
    ]
    for x, y, name, formula, color, sub in spokes:
        b += f'<rect x="{x - 54}" y="{y - 22}" width="108" height="44" rx="6" fill="#FFFFFF" ' \
             f'stroke="{color}" stroke-width="1.2"/>'
        b += text(x, y - 8, name, 8.0, weight="bold", color=INK)
        b += text(x, y + 4, formula, 7.2, color=color)
        b += text(x, y + 16, sub, 6.6, color=GREY)
        dx, dy = cx - x, cy - y
        d = math.hypot(dx, dy)
        b += ln(x + dx / d * 56, y + dy / d * 24, cx - dx / d * r, cy - dy / d * r, THIN, 0.9)
    b += foot(266, "Only the first two are knobs the operator turns; the rest are fixed when the reactor")
    b += foot(278, "is built, which is why the reactor is chosen after the kinetics is known.")
    return svg(W, 290, b)


def mm():
    b = heading("Enzymatic rate against substrate concentration",
                "v = Vmax [S] / (Km + [S])")
    x0, y0, w, h = 52, 58, 236, 118
    b += axes(x0, y0, w, h, "[S]", "v", xticks=[], yticks=[])
    vmax = 0.92
    pts = []
    for k in range(81):
        s_ = k / 80 * 4.0
        v = vmax * s_ / (1.0 + s_)
        pts.append((x0 + s_ / 4.0 * w, y0 + h - v * h))
    b += curve(pts, BLUE, 2.0)
    yv = y0 + h - vmax * h
    b += guide(x0, yv, x0 + w + 6, yv, THIN)
    b += text(x0 + w + 10, yv + 3, "Vmax", 8.0, anchor="start", color=GREY, weight="bold")
    xk = x0 + 1.0 / 4.0 * w
    yk = y0 + h - (vmax * 0.5) * h
    b += guide(xk, yk, xk, y0 + h, GREY)
    b += guide(xk, yk, x0 - 4, yk, GREY)
    b += dots([(xk, yk)], RED, 2.6)
    b += text(xk + 5, y0 + h + 13, "Km", 8.0, anchor="start", color=RED, weight="bold")
    b += text(x0 - 8, yk + 3, "Vmax/2", 7.2, anchor="end", color=GREY)
    b += text(x0 + 10, y0 + 18, "first order in S", 7.2, anchor="start", color=TEAL)
    b += foot(206, "First order while substrate is scarce, zero order once the")
    b += foot(218, "enzyme is saturated; Km gives exactly half of Vmax.")
    return svg(W, 230, b)


DIAGRAMS = {
    "u1_map": map_,
    "u1_tree": tree,
    "u1_energy": energy,
    "u1_basis": basis,
    "u1_variables": variables,
    "u1_mm": mm,
}
