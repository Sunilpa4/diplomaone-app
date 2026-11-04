"""Seven figures for Chemical Reaction Engineering (DI05005031) Unit 5 - designing one ideal reactor.

This is a working set rather than a set of pictures. The CSTR, PFR and series figures are all drawn
from the same first-order rate law, 1/(-rA) = 1/(k CA0 (1 - X)), so the rectangle of one reactor and
the area of another can be compared on identical axes; the staircase uses the two-CSTR numbers of
Unit 4 and the bar chart repeats the volumes those numbers gave. Nothing is sketched by eye.
"""
import math

from diagrams_DI05005031_lib import (INK, GREY, THIN, BLUE, GREEN, ORANGE, RED, PURPLE, TEAL, W,
                                     AMBER, SKY, GLASS, svg, text, ln, arrow, heading, foot, panel,
                                     note_box, vessel, liquid, jacket, shaft, motor, impeller,
                                     curve, dots, axes, guide, lbl, leader)

TITLES = {
    "u5_perf": "One balance, three design equations",
    "u5_batch": "Designing a batch reactor",
    "u5_cstr": "Designing a CSTR: one rectangle",
    "u5_pfr": "Designing a PFR: the area",
    "u5_series": "Two CSTRs in series",
    "u5_space": "Space time against holding time",
    "u5_bars": "Volumes for the same duty",
}

CAPTIONS = {
    "u5_perf": "The same mole balance written three ways: for a batch it gives a time, for a CSTR an "
               "algebraic volume, for a PFR an integral along the tube.",
    "u5_batch": "The batch reactor is designed in time: the slope of the concentration curve at any "
                "instant is the rate, so the steeper the curve the sooner the conversion arrives.",
    "u5_cstr": "On a plot of 1/(-rA) against X the CSTR is one rectangle: width X, height the rate at "
               "the exit, area V/FA0. At 80 % conversion that area is k tau = 4.",
    "u5_pfr": "The PFR is the area under the same curve. At 80 % conversion it is ln 5 = 1.61, so the "
              "tube needs 2.5 times less volume than the tank for the same duty.",
    "u5_series": "Two equal CSTRs in series are two rectangles of k tau = 1.236 each, and together "
                 "they reach 80 % - the geometry behind the numbers of Unit 4.",
    "u5_space": "Space time is fixed by the feed volume flow; holding time is what the fluid really "
                "spends inside, and for a gas it moves with temperature and pressure.",
    "u5_bars": "Same duty (80 % of a first order reaction, k = 0.25 h-1, v0 = 7.2 m3/h): one CSTR "
               "115 m3, two CSTRs 71 m3, one PFR 46 m3.",
}

Y0, H, YMAX = 76, 88, 10.0   # plot band used by the three Levenspiel figures
BOT = Y0 + H                 # 164 - the X axis
X0, PW = 62, 236             # left edge and width of the plotting area


def _plot(b, colour, xticks, x0=X0, w=PW):
    """Axes for 1/(-rA) against X plus the first-order curve 1/(1 - X)."""
    b += axes(x0, Y0, w, H, "X", "1/(-rA) x k CA0", xticks=xticks,
              yticks=((1 / YMAX, "1"), (0.5, "5"), (1 - 1 / YMAX, "9")))
    pts = [(x0 + 0.9 * i / 90 * w, BOT - (1 / (1 - 0.9 * i / 90)) * H / YMAX) for i in range(91)]
    return b + curve(pts, colour, 2.0)


def _y(x):
    """Pixel height on the plot for 1/(-rA) at conversion X = (x - X0)/PW."""
    return BOT - (1 / (1 - (x - X0) / PW)) * H / YMAX


def perf():
    b = heading("One balance, three design equations", "the performance equation of a single reactor")
    b += panel(6, 48, 348, 106)
    b += text(180, 64, "mole balance on A:   in - out + generation = accumulation", 7.8,
              weight="bold", color=INK)
    rows = [(BLUE, "BATCH", "t = NA0 x integral dX/(-rA V)", "the answer is a time"),
            (GREEN, "CSTR", "V = FA0 X / (-rA)exit", "a volume, no integral"),
            (ORANGE, "PFR", "V = FA0 x integral dX/(-rA)", "a volume, one integral")]
    for i, (col, name, eq, note) in enumerate(rows):
        y = 84 + 22 * i
        b += text(16, y, name, 8.4, anchor="start", weight="bold", color=col)
        b += text(68, y, eq, 7.4, anchor="start", color=INK)
        b += text(342, y, note, 7.0, anchor="end", color=GREY)
    b += note_box(6, 166, 348, 54, "what changes from one equation to the next",
                  ["batch: no flow at all, so the balance runs in time",
                   "CSTR: perfectly mixed, so the exit is the inside composition",
                   "PFR: plug flow, so the balance runs along the length"])
    b += foot(238, "Constant density: v = v0, so CA = CA0 (1 - X) and the rate becomes a")
    b += foot(250, "function of X alone. That is what lets all three equations be")
    b += foot(262, "integrated by hand instead of solved numerically.")
    return svg(W, 272, b)


def batch():
    b = heading("Designing a batch reactor", "time is the design variable")
    b += vessel(22, 70, 92, 112, INK, 2.0, GLASS, rx=5)
    b += liquid(22, 70, 92, 112, 104, SKY, BLUE)
    b += jacket(22, 70, 92, 112, TEAL, 1.1)
    b += motor(68, 62, 22, 11)
    b += shaft(68, 68, 174, INK, 2.0)
    b += impeller(68, 170, 18, INK, 3)
    b += text(68, 128, "charge once,", 6.8, color=PURPLE)
    b += text(68, 138, "no outlet", 6.8, color=PURPLE)
    b += text(10, 62, "jacket sets T", 6.6, anchor="start", color=TEAL)
    b += text(68, 194, "batch vessel", 7.0, anchor="middle", color=INK)
    # the design plot
    ax0, ay, aw, ah = 160, 78, 156, 86
    b += axes(ax0, ay, aw, ah, "time t", "CA",
              xticks=((0.0, "0"), (0.5, "75"), (0.94, "150")),
              yticks=((0.05, "0"), (0.5, "0.5"), (0.95, "1.0")))
    ca = lambda t: math.exp(-0.02 * t)   # noqa: E731 - CA/CA0 for k = 0.02 min-1
    b += curve([(ax0 + aw * t / 160, ay + ah - (ah - 4) * ca(t)) for t in range(0, 161, 4)],
               BLUE, 2.0)
    # one tangent, drawn with the true slope: dCA/dt = -k CA
    t0 = 40.0
    yc = ay + ah - (ah - 4) * ca(t0)
    xc = ax0 + aw * t0 / 160
    dx_px = 26
    dy_px = (0.02 * ca(t0)) * (dx_px * 160 / aw) / 1.0 * (ah - 4)
    b += ln(xc - dx_px, yc + dy_px, xc + dx_px, yc - dy_px, RED, 1.3)
    b += text(xc + dx_px + 4, yc - dy_px - 2, "tangent", 6.6, anchor="start", color=RED)
    b += text(xc + dx_px + 4, yc - dy_px + 8, "slope = -rA", 6.6, anchor="start", color=RED)
    b += guide(ax0 + aw * 0.94, ay, ax0 + aw * 0.94, BOT + 4, THIN)
    b += text(348, 60, "X = 0.95 at t = 150 min", 6.8, anchor="end", color=BLUE)

    b += note_box(6, 204, 348, 54, "the design step, in order",
                  ["1. isothermal, constant volume: t = (1/k) ln[1/(1 - X)] first order",
                   "2. add filling, heating, emptying and cleaning to get the cycle time",
                   "3. divide the daily duty by one batch to get the number of batches"])
    b += foot(276, "150 min of reaction with a 30 min turnaround gives 8 batches a day, each")
    b += foot(288, "delivering 1.9 kmol from 1 m3: 15.2 kmol a day out of one vessel.")
    return svg(W, 298, b)


def cstr():
    b = heading("Designing a CSTR: one rectangle", "area of the rectangle = V/FA0 = k tau")
    b += _plot(b, GREEN, ((0.0, "0"), (0.5, "0.5"), (0.8, "0.8"), (1.0, "1.0")))
    x1 = X0 + 0.8 * PW
    top = _y(x1)   # 1/(-rA) = 5 at X = 0.8
    b += f'<rect x="{X0}" y="{top:.1f}" width="{0.8 * PW:.1f}" height="{BOT - top:.1f}" ' \
         f'fill="{ORANGE}" fill-opacity="0.14" stroke="{ORANGE}" stroke-width="1.4"/>'
    b += text(X0 + 8, top + 14, "area = k tau = 4.0", 7.4, anchor="start", weight="bold",
              color=ORANGE)
    b += text(X0 + 8, top + 26, "height 5 at X = 0.8", 6.8, anchor="start", color=ORANGE)
    b += text(x1 - 6, BOT - 6, "width 0.8", 6.8, anchor="end", color=ORANGE)
    b += text(180, 202, "with k = 0.25 h-1 and v0 = 7.2 m3/h: tau = 16 h, V = 115 m3", 7.0,
              color=INK, weight="bold")
    b += note_box(6, 212, 348, 54, "read the size straight off the plot",
                  ["V = FA0 x area = v0 CA0 x 4.0/(k CA0) = 4 v0/k",
                   "first order: k tau = X/(1 - X) = 4 at 80 %, 9 at 90 %, 19 at 95 %",
                   "the tank works at the exit rate - the slowest rate inside it"])
    b += foot(286, "The cost of a CSTR rises faster than the conversion it buys: doubling the")
    b += foot(298, "conversion from 80 to 90 % more than doubles the volume.")
    return svg(W, 308, b)


def pfr():
    b = heading("Designing a PFR: the area", "area under the curve = V/FA0 = k tau")
    b += _plot(b, BLUE, ((0.0, "0"), (0.5, "0.5"), (0.8, "0.8"), (1.0, "1.0")))
    for i in range(30):
        xa = X0 + 0.8 * PW * i / 30
        xb = X0 + 0.8 * PW * (i + 1) / 30
        yy = _y((xa + xb) / 2)
        b += f'<rect x="{xa:.1f}" y="{yy:.1f}" width="{xb - xa - 0.4:.1f}" ' \
             f'height="{BOT - yy:.1f}" fill="{BLUE}" fill-opacity="0.15"/>'
    b += text(X0 + 8, 96, "area = k tau = ln[1/(1 - 0.8)] = 1.61", 7.4, anchor="start",
              weight="bold", color=BLUE)
    b += text(180, 202, "the same duty in a CSTR: tau = 16 h, 115 m3", 7.0, color=INK,
              weight="bold")
    b += note_box(6, 212, 348, 54, "why the tube wins for a positive order",
                  ["the reactant is held at its highest concentration for as long as possible",
                   "V = 1.61 v0/k = 46 m3, 2.5 times smaller than the CSTR's 115 m3",
                   "at 90 % the pair is 2.30 against 9, a factor of 3.9"])
    b += foot(286, "A pipe is only a PFR while axial dispersion stays small: a laminar")
    b += foot(298, "profile or a wide vessel is neither plug flow nor a CSTR, but something between.")
    return svg(W, 308, b)


def series():
    b = heading("Two CSTRs in series", "each tank is one rectangle; together they reach 80 %")
    b += _plot(b, GREEN, ((0.0, "0"), (0.553, "0.55"), (0.8, "0.8"), (1.0, "1.0")))
    x1 = X0 + 0.553 * PW
    x2 = X0 + 0.8 * PW
    y1, y2 = _y(x1), _y(x2)
    b += f'<rect x="{X0}" y="{y1:.1f}" width="{x1 - X0:.1f}" height="{BOT - y1:.1f}" ' \
         f'fill="{AMBER}" fill-opacity="0.28" stroke="{ORANGE}" stroke-width="1.3"/>'
    b += f'<rect x="{x1:.1f}" y="{y2:.1f}" width="{x2 - x1:.1f}" height="{BOT - y2:.1f}" ' \
         f'fill="{PURPLE}" fill-opacity="0.16" stroke="{PURPLE}" stroke-width="1.3"/>'
    b += text(X0 + 4, y1 - 14, "tank 1", 6.8, anchor="start", color=ORANGE)
    b += text(X0 + 4, y1 - 5, "k tau = 1.24", 6.8, anchor="start", color=ORANGE)
    b += text(x1 + 6, y2 - 14, "tank 2", 6.8, anchor="start", color=PURPLE)
    b += text(x1 + 6, y2 - 5, "k tau = 1.24", 6.8, anchor="start", color=PURPLE)
    b += text(180, 202, "4.94 h and 35.6 m3 in each tank: 71 m3 in all", 7.0, color=INK,
              weight="bold")
    b += note_box(6, 212, 348, 54, "why a train of tanks is common",
                  ["one CSTR needs k tau = 4.0; two equal tanks need 1.24 each",
                   "71 m3 instead of 115 m3 - 38 % less steel for the same duty",
                   "the gain per tank falls away: three need 0.86 each, four 0.68"])
    b += foot(286, "In practice the first tank takes most of the conversion and the last polishes")
    b += foot(298, "it; both must still mix faster than their own space time.")
    return svg(W, 308, b)


def space():
    b = heading("Space time against holding time", "one is fixed by the feed, the other by conditions")
    b += vessel(112, 76, 100, 104, INK, 2.0, GLASS, rx=6)
    b += liquid(112, 76, 100, 104, 102, SKY, BLUE)
    b += arrow(8, 150, 108, 150, INK, 1.6)
    b += text(8, 140, "feed v0 = 0.2 m3/min", 6.9, anchor="start", color=INK)
    b += text(8, 162, "1 bar, 300 K", 6.9, anchor="start", color=GREY)
    b += arrow(214, 112, 268, 112, INK, 1.6)
    b += text(272, 108, "product", 6.9, anchor="start", color=INK)
    b += text(272, 120, "5 bar, 400 K", 6.9, anchor="start", color=GREY)
    b += text(162, 96, "V = 2 m3", 7.6, color=PURPLE, weight="bold")
    b += text(162, 188, "the gas is compressed to 5 bar as it enters", 6.6, color=GREY)
    b += panel(6, 200, 170, 76)
    b += text(91, 216, "SPACE TIME", 7.4, weight="bold", color=BLUE)
    b += text(91, 232, "tau = V/v0 = 2/0.2", 7.0, color=INK)
    b += text(91, 246, "= 10 min", 7.0, color=INK, weight="bold")
    b += text(91, 262, "a property of the feed", 6.6, color=GREY)
    b += panel(184, 200, 170, 76)
    b += text(269, 216, "HOLDING TIME", 7.4, weight="bold", color=TEAL)
    b += text(269, 232, "v = 0.2 x (1/5) x (400/300)", 6.8, color=INK)
    b += text(269, 246, "t = 2/0.0533 = 37.5 min", 7.0, color=INK, weight="bold")
    b += text(269, 262, "a property of the conditions", 6.6, color=GREY)
    b += foot(292, "Space velocity is the reciprocal: SV = v0/V = 1/tau = 0.1 min-1 = 6 h-1.")
    b += foot(304, "Doubling the feed halves tau, doubles SV, and lowers the conversion.")
    return svg(W, 314, b)


def bars():
    b = heading("Volumes for the same duty", "80 % of a first order reaction, k = 0.25 h-1")
    base, scale_top = 226, 118
    b += ln(48, base, 348, base, INK, 1.4)
    b += ln(48, base, 48, scale_top - 10, INK, 1.4)
    b += text(48, scale_top - 20, "V (m3)", 7.6, anchor="start", weight="bold")
    for val in (0, 50, 100):
        yy = base - val / 120 * (base - scale_top)
        b += ln(43, yy, 48, yy, INK, 1.0)
        b += text(38, yy + 2.6, str(val), 7.0, anchor="end", color=GREY)
    barsd = [("1 CSTR", 115.2, ORANGE, "tau = 16 h"),
             ("2 CSTRs", 71.2, PURPLE, "4.94 h each"),
             ("1 PFR", 46.4, BLUE, "tau = 6.44 h")]
    for i, (name, v, col, sub) in enumerate(barsd):
        x = 80 + i * 88
        hh = v / 120 * (base - scale_top)
        b += f'<rect x="{x}" y="{base - hh:.1f}" width="56" height="{hh:.1f}" rx="3" ' \
             f'fill="{col}" fill-opacity="0.26" stroke="{col}" stroke-width="1.4"/>'
        b += text(x + 28, base - hh - 17, f"{v:.0f} m3", 7.6, weight="bold", color=col)
        b += text(x + 28, base - hh - 6, sub, 6.6, color=GREY)
        b += text(x + 28, base + 14, name, 7.4, color=INK)
    b += note_box(6, 254, 348, 34, "the one number to remember",
                  ["same feed, same conversion, same k: the tube needs 2.5 times less volume"])
    b += foot(304, "v0 = 7.2 m3/h throughout. Two CSTRs in series close the gap to 1.5.")
    return svg(W, 316, b)


DIAGRAMS = {
    "u5_perf": perf,
    "u5_batch": batch,
    "u5_cstr": cstr,
    "u5_pfr": pfr,
    "u5_series": series,
    "u5_space": space,
    "u5_bars": bars,
}
