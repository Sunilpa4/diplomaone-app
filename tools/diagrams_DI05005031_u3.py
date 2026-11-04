"""Six figures for Chemical Reaction Engineering (DI05005031) Unit 3 - interpretation of batch reactor
data: the three routes to a rate equation, the differential method, the integral (straight-line) test,
the half-life log-log line, pressure data turned into concentration, and the integrated laws of every
order side by side."""
import math

from diagrams_DI05005031_lib import (INK, GREY, THIN, BLUE, GREEN, ORANGE, RED, PURPLE, TEAL, W,
                                     svg, text, ln, arrow, heading, foot, panel, axes, curve, dots,
                                     guide, box, note_box, vessel, liquid, lbl, leader)

TITLES = {
    "u3_paths": "Three roads from one table of data",
    "u3_diff": "The differential method: slopes, then a log-log line",
    "u3_integral_test": "The integral method: which plot is straight",
    "u3_halflife": "Half-life against starting concentration",
    "u3_pressure": "Pressure data turned into concentration",
    "u3_orders": "The integrated laws, order by order",
}

CAPTIONS = {
    "u3_paths": "The same C against t table can be read three ways; the differential method fits a "
                "power law, the integral method tests a guess, the half-life method reads the order "
                "off the way the half-life changes.",
    "u3_diff": "Tangents to the C-t curve give a rate at each concentration; a straight line through "
               "ln(-rA) against ln CA then gives the order as its slope and k as its intercept.",
    "u3_integral_test": "Guess an order, integrate, plot the matching function of C: only the correct "
                        "order gives a straight line, and its slope is k.",
    "u3_halflife": "On log-log paper the half-life is a straight line of slope 1 - n: flat means first "
                   "order, rising means zero order, falling means second order.",
    "u3_pressure": "In a constant-volume gas reaction the gauge reads the total pressure; the "
                   "stoichiometry converts it into the partial pressure of A, and the gas law turns "
                   "that into a concentration.",
    "u3_orders": "The conserved straight-line variable differs with order - C, ln C, 1/C - and the "
                 "half-life carries the same information in one number.",
}


# ------------------------------------------------------------------ 1. three routes
def paths():
    b = heading("Three roads from one table of data", "the same C against t table, three plots")
    b += f'<rect x="60" y="50" width="240" height="30" rx="6" fill="#F5EEFD" stroke="{PURPLE}" ' \
         f'stroke-width="1.5"/>'
    b += text(180, 69, "Batch data: CA measured against t", 8.6, weight="bold", color=PURPLE)
    b += ln(180, 80, 180, 92, INK, 1.3)
    b += ln(60, 92, 300, 92, INK, 1.3)
    for cx in (60, 180, 300):
        b += arrow(cx, 92, cx, 104, INK, 1.3)
    routes = [(60, RED, "Differential", ["tangent slopes", "plot ln(-rA)", "against ln CA", "slope = n"]),
              (180, BLUE, "Integral", ["guess n", "integrate the law", "plot the linear form", "straight line = n"]),
              (300, GREEN, "Half-life", ["t1/2 at several CA0", "plot log t1/2", "against log CA0", "slope = 1 - n"])]
    for cx, color, title, lines in routes:
        x = cx - 48
        b += f'<rect x="{x}" y="106" width="96" height="78" rx="5" fill="#FFFFFF" stroke="{color}" ' \
             f'stroke-width="1.4"/>'
        b += text(cx, 122, title, 8.2, weight="bold", color=color)
        for i, s in enumerate(lines):
            b += text(cx, 136 + 12 * i, s, 7.4, color=INK)
    b += foot(206, "Each route needs the same raw data and gives the same answer if the order is")
    b += foot(218, "real; run two of them and let them agree before you trust the number.")
    return svg(W, 236, b)


# ------------------------------------------------------------------ 2. differential method
def _decay(x, x0, w, top, h):
    """A smooth first-order-looking C-t curve over [x0, x0+w]."""
    u = (x - x0) / w
    return top + h * (1 - math.exp(-2.4 * u))


def diff():
    b = heading("The differential method: slopes, then a log-log line",
                "each tangent is one rate; the line gives n and k")
    # left panel: C against t with two tangents
    b += panel(6, 52, 168, 198)
    b += text(90, 68, "1. draw the C-t curve", 8.0, weight="bold", color=INK)
    b += axes(34, 96, 116, 100, "t", "CA", xticks=(), yticks=())
    x0, w, top, h = 34, 116, 96, 100
    pts = [(x0 + i * 4, _decay(x0 + i * 4, x0, w, top, h)) for i in range(30)]
    b += curve(pts, BLUE, 2.0)
    for n_, xt in enumerate((74, 112), start=1):
        y = _decay(xt, x0, w, top, h)
        m = h * 2.4 / w * math.exp(-2.4 * (xt - x0) / w)      # dC/dt at that point (downward)
        b += ln(xt - 11, y - 11 * m, xt + 11, y + 11 * m, RED, 1.9)
        b += f'<circle cx="{xt:.1f}" cy="{y:.1f}" r="2.0" fill="{RED}"/>'
        b += f'<circle cx="{xt - 12:.1f}" cy="{y - 16 * m - 15:.1f}" r="5.2" fill="#FFFFFF" ' \
             f'stroke="{RED}" stroke-width="1"/>'
        b += text(xt - 12, y - 16 * m - 12.4, str(n_), 6.6, color=RED, weight="bold")
    b += text(90, 236, "each red tangent is one rate", 7.4, color=GREY)
    # right panel: ln(-rA) against ln CA
    b += panel(184, 52, 170, 198)
    b += text(269, 68, "2. plot ln(-rA) against ln CA", 8.0, weight="bold", color=INK)
    b += axes(216, 96, 116, 100, "ln CA", "ln(-rA)", xticks=(), yticks=())
    lp = [(219, 190), (250, 172), (281, 154), (312, 136), (330, 125)]
    b += guide(219, 190, 330, 125, THIN)
    b += curve(lp, GREEN, 2.0)
    b += dots([(228, 185), (272, 160), (316, 134)], RED, 2.2)
    b += text(330, 112, "slope = n", 7.6, anchor="end", color=GREEN, weight="bold")
    b += text(269, 236, "the intercept is ln k", 7.4, color=GREY)
    b += foot(268, "A tangent is a derivative, so read the rate at the mid-point of its interval;")
    b += foot(280, "a few points on a straight log-log line beat one cleverly drawn tangent.")
    return svg(W, 292, b)


# ------------------------------------------------------------------ 3. integral test
def integral_test():
    b = heading("The integral method: which plot is straight",
                "guess the order, integrate, then look at the plot")
    rows = [(52, "Zero:  -rA = k", "CA0 - CA = k t", 0.0, "C against t is a straight line", "slope = -k"),
            (110, "First:  -rA = k CA", "ln(CA0/CA) = k t", 1.0, "ln C against t is straight", "slope = -k"),
            (168, "Second:  -rA = k CA^2", "1/CA - 1/CA0 = k t", 2.0, "1/C against t is straight", "slope = k")]
    for y0, name, law, order, test_line, slope_line in rows:
        b += panel(6, y0, 348, 50)
        b += text(14, y0 + 20, name, 8.0, anchor="start", weight="bold", color=INK)
        b += text(14, y0 + 34, law, 7.2, anchor="start", color=GREY)
        # mini sketch of the C-t shape
        ax, ay, aw, ah = 118, y0 + 8, 54, 34
        b += ln(ax, ay, ax, ay + ah, INK, 1.0)
        b += ln(ax, ay + ah, ax + aw, ay + ah, INK, 1.0)
        pts = []
        for i in range(24):
            u = i / 23.0
            if order == 0.0:
                frac = 0.95 * u
            elif order == 1.0:
                frac = 0.96 * (1 - math.exp(-3.0 * u))
            else:
                frac = 0.96 * (1 - 1 / (1 + 6.0 * u))
            pts.append((ax + 4 + u * (aw - 6), ay + 4 + frac * (ah - 8)))
        b += curve(pts, BLUE, 1.8)
        b += text(190, y0 + 20, test_line, 7.6, anchor="start", color=GREEN, weight="bold")
        b += text(190, y0 + 34, slope_line, 7.6, anchor="start", color=INK)
    b += foot(230, "Only one of the three plots can be straight for a given set of data - that plot")
    b += foot(242, "names the order, and its slope is the rate constant.")
    return svg(W, 262, b)


# ------------------------------------------------------------------ 4. half-life
def halflife():
    b = heading("Half-life against starting concentration",
                "t1/2 = const x CA0^(1-n), so the slope is 1 - n")
    b += axes(46, 60, 262, 118, "log CA0", "log t1/2", xticks=(), yticks=())
    xc, yc, m = 160, 120, 0.36
    ends = []
    for slope, color, tag in [(1.0, ORANGE, "n = 0: zero order, t1/2 rises with CA0"),
                              (0.0, BLUE, "n = 1: first order, t1/2 is fixed"),
                              (-1.0, GREEN, "n = 2: second order, t1/2 falls with CA0")]:
        xa, xb = 76, 296
        ya, yb = yc - m * slope * (xa - xc), yc - m * slope * (xb - xc)
        b += ln(xa, ya, xb, yb, color, 2.0)
        ends.append((color, ya, yb))
    b += dots([(xc, yc)], RED, 2.4)
    # legend strip under the plot, so no label sits on a line
    b += f'<rect x="14" y="196" width="332" height="46" rx="5" fill="#FBFCFD" stroke="{THIN}" ' \
         f'stroke-width="0.9"/>'
    for i, (color, slot, tag) in enumerate([(ORANGE, 0, "n = 0: t1/2 doubles when CA0 doubles"),
                                            (BLUE, 1, "n = 1: t1/2 does not depend on CA0"),
                                            (GREEN, 2, "n = 2: t1/2 halves when CA0 doubles")]):
        y = 208 + 12 * i
        b += ln(24, y - 3, 44, y - 3, color, 2.4)
        b += text(52, y, tag, 7.6, anchor="start", color=INK)
    b += foot(256, "Plot log t1/2 against log CA0 and measure the slope: 1 - n gives the order without")
    b += foot(268, "ever integrating the rate law, which is why the method is used on new reactions.")
    return svg(W, 280, b)


# ------------------------------------------------------------------ 5. pressure data
def pressure():
    b = heading("Pressure data turned into concentration",
                "constant volume, gas phase: the gauge measures the total")
    b += vessel(20, 70, 88, 100, INK, 2.0, "#F7FBFF", rx=4)
    b += f'<rect x="22" y="72" width="84" height="96" rx="2" fill="#EAF3FE"/>'
    for gx, gy in [(40, 96), (66, 104), (86, 90), (52, 120), (78, 130), (36, 140), (60, 152), (88, 148)]:
        b += f'<circle cx="{gx}" cy="{gy}" r="1.7" fill="{BLUE}"/>'
    b += vessel(20, 70, 88, 100, INK, 2.0, "none", rx=4)
    b += f'<circle cx="64" cy="60" r="9" fill="#FFFFFF" stroke="{INK}" stroke-width="1.6"/>'
    b += ln(64, 60, 60, 54, INK, 1.2)
    b += ln(64, 69, 64, 70, INK, 1.6)
    b += text(78, 52, "gauge: total p", 7.4, anchor="start", color=INK, weight="bold")
    b += leader(72, 57, 78, 54, THIN)
    b += text(64, 184, "V and T fixed", 7.6, color=GREY)
    b += text(64, 196, "batch, gas phase", 7.4, color=GREY)
    steps = [(56, RED, "1. gauge", "p = pA + pB + pC ..."),
             (100, ORANGE, "2. stoichiometry", "pA from the mole change"),
             (144, BLUE, "3. gas law", "CA = pA / (R T)")]
    for y, color, title, sub in steps:
        b += f'<rect x="140" y="{y}" width="206" height="34" rx="5" fill="#FFFFFF" stroke="{color}" ' \
             f'stroke-width="1.3"/>'
        b += text(148, y + 14, title, 7.8, anchor="start", weight="bold", color=color)
        b += text(148, y + 27, sub, 7.4, anchor="start", color=INK)
    for y in (90, 134):
        b += arrow(243, y, 243, y + 9, GREY, 1.2)
    b += note_box(14, 210, 332, 40, "for  A -> products  with a mole change",
                  ["pA = pA0 - (a/dn)(p - p0)   and   CA = CA0 (1 - X)"], PURPLE, "#F5EEFD")
    b += foot(268, "Air, or an inert, changes the total but not the partial pressure of A - subtract it")
    b += foot(280, "before you divide by RT, or the calculated conversion comes out too high.")
    return svg(W, 296, b)


# ------------------------------------------------------------------ 6. integrated laws
def orders():
    b = heading("The integrated laws, order by order", "one straight-line variable and one half-life each")
    heads = [("order", 12, "start"), ("the law, from -dCA/dt = k CA^n", 58, "start"), ("half-life", 250, "start")]
    b += f'<rect x="8" y="48" width="344" height="22" rx="4" fill="#F5EEFD" stroke="{PURPLE}" ' \
         f'stroke-width="1.2"/>'
    for name, x, anchor in heads:
        b += text(x, 62, name, 7.8, anchor=anchor, weight="bold", color=PURPLE)
    rows = [("0", "CA0 - CA = k t", "CA0 / (2k)"),
            ("1", "ln(CA0/CA) = k t", "0.693 / k"),
            ("2", "1/CA - 1/CA0 = k t", "1 / (k CA0)"),
            ("n", "CA^(1-n) - CA0^(1-n) = (n-1) k t", "")]
    for i, (order, law, half) in enumerate(rows):
        y = 70 + i * 30
        b += f'<rect x="8" y="{y}" width="344" height="30" rx="4" fill="{"#FFFFFF" if i % 2 == 0 else "#FAFAFC"}" ' \
             f'stroke="{THIN}" stroke-width="0.9"/>'
        b += text(24, y + 19, order, 9.0, weight="bold", color=INK)
        b += text(58, y + 19, law, 7.6, anchor="start", color=BLUE)
        if order == "n":
            b += text(238, y + 14, "(2^(n-1)-1)", 7.0, anchor="start", color=GREEN)
            b += text(238, y + 25, "/ ((n-1) k CA0^(n-1))", 7.0, anchor="start", color=GREEN)
        else:
            b += text(250, y + 19, half, 7.2, anchor="start", color=GREEN)
    b += foot(206, "k carries the order too: mol m-3 s-1, s-1, m3 mol-1 s-1 ... (mol m-3)^(1-n) s-1;")
    b += foot(218, "an answer in the wrong unit of k is the fastest way to lose the marks for it.")
    return svg(W, 238, b)


DIAGRAMS = {
    "u3_paths": paths,
    "u3_diff": diff,
    "u3_integral_test": integral_test,
    "u3_halflife": halflife,
    "u3_pressure": pressure,
    "u3_orders": orders,
}
