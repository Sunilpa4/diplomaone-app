"""Eight figures for Engineering Materials Science (DI01000181) Unit 2 - solidification and phase diagrams.

Every number on these figures is a standard, printed value and the geometry is computed from it: the
cooling curves are plotted from their own temperature-time points, the Cu-Ni and Pb-Sn liquids and
solids are drawn from tabulated compositions, the tie lines are solved by linear interpolation of
those same points and the lever-rule fractions printed in the notes come out of those tie lines. The
Fe-Fe3C figure carries the usual points - A 1538, H 0.09, J 0.17, B 0.53, N 1394, D 1227, E 2.14,
C 4.3, F 6.67, G 912, S 0.8, P 0.02, K 6.67, A1 727 and eutectic 1147 C - and the carbon axis is
compressed beyond 2.2 % so the steel corner stays readable on a phone.
"""
import math

from diagrams_DI01000181_lib import (INK, GREY, THIN, BLUE, GREEN, ORANGE, RED, PURPLE, TEAL, W,
                                     AMBER, SKY, GLASS, STEEL, svg, text, ln, arrow, heading, foot,
                                     panel, note_box, lbl, leader, poly, curve, dots, axes, guide,
                                     atom, electron, grain_field)

TITLES = {
    "u2_coolcurve": "Cooling curves of a pure metal and an alloy",
    "u2_ingot": "Grain structure of a cast ingot",
    "u2_solution": "Substitutional and interstitial solid solutions",
    "u2_cuni": "Copper-nickel: an isomorphous system",
    "u2_pbsn": "Lead-tin: a eutectic system",
    "u2_fec": "The iron-iron carbide diagram",
    "u2_micro": "Microstructures across the eutectoid",
    "u2_hallpetch": "Grain size sets the yield strength",
}

CAPTIONS = {
    "u2_coolcurve": "A pure metal freezes at one temperature and the curve stays flat while the "
                    "latent heat comes out; an alloy freezes over a range between its liquidus and "
                    "solidus, so the curve only changes slope.",
    "u2_ingot": "The mould wall chills the metal first, so fine equiaxed grains form there, "
                "columnar grains grow inwards along the heat flow, and the hot centre freezes last "
                "as coarse equiaxed grains.",
    "u2_solution": "A substitutional solution swaps one atom for another of similar size (Cu-Ni); "
                   "an interstitial solution hides a small atom in the gaps (carbon in iron) - which "
                   "is why carbon fits in iron only up to 2.14 %.",
    "u2_cuni": "Copper and nickel dissolve in each other in every proportion, so the diagram has no "
               "eutectic: one liquidus above one solidus, and a tie line that gives both phases.",
    "u2_pbsn": "Lead and tin barely dissolve in each other, so the two liquidus branches meet at the "
               "eutectic 183 C and 61.9 % tin, where the alloy freezes at a single temperature.",
    "u2_fec": "Carbon up to 2.14 % dissolves in austenite; at 0.8 % and 727 C that austenite turns "
              "into pearlite, the eutectoid reaction that every heat treatment of steel works "
              "around.",
    "u2_micro": "Below 0.8 % carbon the pearlite sits in a field of ferrite, at 0.8 % it fills the "
                "micrograph, and above 0.8 % cementite appears on the grain boundaries as a brittle "
                "network.",
    "u2_hallpetch": "Yield strength rises with the square root of the reciprocal grain size: halving "
                    "the grain size raises the strength by about 40 % for the same steel.",
}


def _map(x0, y0, w, h, xlo, xhi, ylo, yhi):
    """Linear data-to-canvas mapping; every curve below is plotted through it."""
    def mx(v):
        return x0 + (v - xlo) / (xhi - xlo) * w

    def my(v):
        return y0 + h - (v - ylo) / (yhi - ylo) * h

    return mx, my


def _interp(points, v):
    """Composition (or temperature) where a tabulated curve reaches the value v."""
    seq = sorted(points)
    for (a1, a2), (b1, b2) in zip(seq, seq[1:]):
        if (a2 - v) * (b2 - v) <= 0 and a2 != b2:
            return a1 + (b1 - a1) * (v - a2) / (b2 - a2)
    return seq[-1][0]


# ---------------------------------------------------------------- 1 cooling curves
def cooling_curves():
    b = heading("Cooling curves: pure metal and alloy", "temperature against time in a mould")
    x0, y0, w, h = 46, 58, 288, 178
    mx, my = _map(x0, y0, w, h, 0, 100, 1300, 1700)
    b += axes(x0, y0, w, h, "time", "T (C)",
              xticks=((0, "0"), (0.25, "1"), (0.5, "2"), (0.75, "3"), (1, "4")),
              yticks=((0, "1300"), (0.25, "1400"), (0.5, "1500"), (0.75, "1600"), (1, "1700")))
    pure = [(0, 1680), (26, 1520), (30, 1538), (64, 1538), (100, 1410)]
    alloy = [(0, 1680), (30, 1560), (46, 1500), (70, 1380), (100, 1320)]
    b += guide(x0, my(1538), mx(30), my(1538))
    b += curve([(mx(a), my(c)) for a, c in pure], BLUE, 2.1)
    b += curve([(mx(a), my(c)) for a, c in alloy], ORANGE, 2.1, dash="5,3")
    b += dots([(mx(26), my(1520))], RED, 2.4)
    b += text(mx(26) + 4, my(1520) + 10, "undercooling", 6.4, anchor="start", color=RED)

    # keys sit in the empty lower right corner, below both curves
    b += ln(118, 203, 134, 203, BLUE, 2)
    b += text(138, 206, "pure metal: flat arrest at 1538 C", 6.6, anchor="start", color=INK)
    b += ln(118, 219, 134, 219, ORANGE, 2, dash="5,3")
    b += text(138, 222, "alloy: liquidus to solidus, 1500 to 1380 C", 6.6, anchor="start",
              color=INK)
    b += foot(268, "A pure metal releases its latent heat at one temperature, so the curve is flat ",
              "for as long as the metal takes to freeze; an alloy releases it across a range.")
    b += foot(294, "Read off the liquidus where the first solid appears and the solidus where the ",
              "last liquid disappears - the gap between them is the freezing range.")
    return svg(W, 320, b)


# ---------------------------------------------------------------- 2 ingot grains
def ingot_grains():
    b = heading("Grain structure of a cast ingot", "chill, columnar and equiaxed zones")
    top, bot = 56, 214
    outer = [(66, top), (192, top), (168, bot), (90, bot)]
    mid = [(76, top + 9), (182, top + 9), (159, bot - 9), (99, bot - 9)]
    inner = [(88, top + 21), (170, top + 21), (148, bot - 21), (110, bot - 21)]

    def grain(cx, cy, r=4.4, color=INK, fill="#E8F1FA"):
        pts = [(cx + r * math.cos(math.radians(60 * k)), cy + r * 0.72 * math.sin(math.radians(60 * k)))
               for k in range(6)]
        return poly(pts, color, 0.7, close=True, fill=fill)

    b += poly(outer, INK, 1.4, close=True, fill="#D8E6F5")   # chill band
    b += poly(mid, INK, 0.8, close=True, fill="#E9F0F7")     # columnar band
    b += poly(inner, "#FBFCFE", 0.9, close=True, fill="#FBFCFE")  # equiaxed centre

    # chill zone: many small grains in the thin band next to the mould
    for t in (0.12, 0.30, 0.48, 0.66, 0.84):
        b += grain(71 + 23.5 * t, 60.5 + 149 * t)
        b += grain(187 - 23.5 * t, 60.5 + 149 * t)
    for i in range(6):
        b += grain(71 + i * 23.2, 60.5)
    for i in range(3):
        b += grain(107 + i * 22, 209.0)

    # columnar zone: grains grow inwards along the heat flow, so the strokes are long and parallel
    col = "#8FA3B8"
    for t in (0.12, 0.32, 0.52, 0.72):
        xm, ym = 76 + 23 * t, 65 + 140 * t
        xi, yi = 88 + 22 * t, 77 + 116 * t
        b += ln(xm, ym, xi, yi, col, 0.9)
        b += ln(xm + 6, ym + 2, xi + 6, yi + 2, col, 0.7)
        xm2, ym2 = 182 - 23 * t, 65 + 140 * t
        xi2, yi2 = 170 - 22 * t, 77 + 116 * t
        b += ln(xm2, ym2, xi2, yi2, col, 0.9)
        b += ln(xm2 - 6, ym2 + 2, xi2 - 6, yi2 + 2, col, 0.7)
    for i in range(4):
        xm, xi = 86 + i * 26, 98 + i * 20
        b += ln(xm, 65, xi, 77, col, 0.8)
        b += ln(xm + 6, 205, xi + 4, 193, col, 0.8)

    # equiaxed centre: the coarse grains that froze last, laid out row by row so they stay inside
    for y, n in ((90, 4), (108, 4), (126, 4), (144, 3), (162, 3), (180, 2)):
        for i in range(n):
            b += grain(129 - (n - 1) * 8 + i * 16, y, r=7.6, color=INK, fill="#F1F5FA")

    # mould wall
    b += poly([(60, top - 4), (66, top), (90, bot), (84, bot + 4)], INK, 1.2, close=True,
              fill="#EDEDED")
    b += poly([(198, top - 4), (192, top), (168, bot), (174, bot + 4)], INK, 1.2, close=True,
              fill="#EDEDED")

    b += leader(78, 105, 206, 92, GREY)
    b += text(210, 88, "chill zone: fine", 6.6, anchor="start")
    b += text(210, 98, "equiaxed grains", 6.6, anchor="start", color=GREY)
    b += leader(84, 138, 206, 132, GREY)
    b += text(210, 128, "columnar grains:", 6.6, anchor="start")
    b += text(210, 138, "long, inward,", 6.6, anchor="start", color=GREY)
    b += text(210, 148, "along heat flow", 6.6, anchor="start", color=GREY)
    b += leader(130, 168, 206, 170, GREY)
    b += text(210, 166, "equiaxed centre:", 6.6, anchor="start")
    b += text(210, 176, "coarse, last to freeze", 6.6, anchor="start", color=GREY)
    b += text(129, bot + 16, "mould wall cools the metal first", 6.4, color=GREY)

    b += note_box(6, 224, 348, 58, "solidification starts at a nucleus",
                  ["homogeneous: atoms of the melt cluster on their own - needs large undercooling",
                   "heterogeneous: the mould wall or an oxide particle does the job - needs little",
                   "a grain refiner (Ti, B in aluminium) adds such nuclei and makes many small grains"])
    b += foot(292, "Small grains raise the yield strength (Hall-Petch) and spread the shrinkage",
              "porosity, so a refiner is added to almost every casting alloy.")
    return svg(W, 326, b)


# ---------------------------------------------------------------- 3 solid solutions
def solid_solution():
    b = heading("Substitutional and interstitial solid solutions", "where the second atom goes")
    b += panel(6, 46, 168, 128)
    b += panel(186, 46, 168, 128)
    b += text(90, 62, "substitutional: Cu-Ni", 8.0, weight="bold", color=BLUE)
    b += text(270, 62, "interstitial: C in Fe", 8.0, weight="bold", color=RED)

    swap = {5, 10, 12, 15}
    for j in range(4):
        for i in range(4):
            k = j * 4 + i
            ni = k in swap
            b += atom(34 + i * 38, 82 + j * 26, 9.5, "Ni" if ni else "Cu",
                      ORANGE if ni else BLUE, "#FFF3E4" if ni else "#FFFFFF", size=5.2)
    b += text(90, 186, "Cu radius 128 pm, Ni 125 pm: a 2 % difference", 6.2, color=GREY)
    b += text(90, 196, "so either atom can take the other's place", 6.2, color=GREY)

    for j in range(4):
        for i in range(4):
            b += atom(214 + i * 38, 82 + j * 26, 11, "Fe", "#8894A6", "#EEF2F7", size=5.4)
    for j in range(3):
        for i in range(3):
            b += electron(233 + i * 38, 95 + j * 26, 3.2, RED)
    b += text(270, 186, "carbon radius 77 pm against iron 126 pm", 6.2, color=GREY)
    b += text(270, 196, "so carbon sits in the gaps, not on a site", 6.2, color=GREY)

    b += note_box(6, 206, 348, 68, "the four Hume-Rothery rules for a substitutional solution",
                  ["1  size factor: the radii differ by less than 15 %",
                   "2  crystal structure: the same lattice type",
                   "3  valency: the same valency, or one metal dissolves less of a higher-valency one",
                   "4  electronegativity: close values, else a compound forms instead of a solution"])
    b += foot(286, "Substitutional: brass (Zn in Cu), stainless steel (Cr, Ni in Fe).  Interstitial:",
              "carbon or nitrogen in iron - small atoms, few by count, but they control hardness.")
    return svg(W, 320, b)


# ---------------------------------------------------------------- 4 Cu-Ni
def cuni_diagram():
    b = heading("Copper-nickel: an isomorphous system", "complete solubility in both states")
    x0, y0, w, h = 50, 56, 282, 158
    mx, my = _map(x0, y0, w, h, 0, 100, 1000, 1500)
    b += axes(x0, y0, w, h, "nickel (% by weight)", "T (C)",
              xticks=((0, "0"), (0.2, "20"), (0.4, "40"), (0.6, "60"), (0.8, "80"), (1, "100")),
              yticks=((0, "1000"), (0.2, "1100"), (0.4, "1200"), (0.6, "1300"), (0.8, "1400"),
                      (1, "1500")))
    liquidus = [(0, 1085), (20, 1230), (40, 1300), (60, 1355), (80, 1400), (100, 1455)]
    solidus = [(0, 1085), (20, 1170), (40, 1240), (60, 1300), (80, 1370), (100, 1455)]
    b += curve([(mx(a), my(c)) for a, c in liquidus], ORANGE, 2.1)
    b += curve([(mx(a), my(c)) for a, c in solidus], BLUE, 2.1)

    t = 1300
    c_l = _interp(liquidus, t)          # 40 % Ni
    c_s = _interp(solidus, t)           # 60 % Ni
    c0 = 50.0
    b += guide(mx(0), my(t), mx(c_s), my(t))
    b += ln(mx(c_l), my(t) - 4, mx(c_l), my(t) + 4, ORANGE, 1.4)
    b += ln(mx(c_s), my(t) - 4, mx(c_s), my(t) + 4, BLUE, 1.4)
    b += dots([(mx(c_l), my(t)), (mx(c_s), my(t))], INK, 2.0)
    b += text(mx(c_l), my(t) - 7, f"{c_l:.0f}", 6.2, color=ORANGE)
    b += text(mx(c_s), my(t) - 7, f"{c_s:.0f}", 6.2, color=BLUE)
    b += ln(mx(c0), my(t) - 4, mx(c0), my(t) + 4, INK, 1.3)

    b += lbl(mx(72), my(1440), "L (liquid)", size=7.4, weight="bold")
    b += lbl(mx(26), my(1230), "L + α", size=6.4, color=ORANGE)
    b += lbl(mx(22), my(1100), "α solid solution", size=7.0, color=BLUE)
    b += text(mx(0) + 5, my(1085) + 11, "1085 C", 6.4, anchor="start", color=GREY)
    b += text(mx(100) - 4, my(1455) - 7, "1455 C", 6.4, anchor="end", color=GREY)

    b += note_box(6, 248, 348, 44, "lever rule on the same tie line at 1300 C",
                  [f"W(liquid) = ({c_s:.0f} - 50)/({c_s:.0f} - {c_l:.0f}) = 0.50   and   W(α) = 0.50",
                   "the chemical composition of each phase is read at the ends of the tie line"])
    b += foot(302, "Cu and Ni share an FCC lattice and almost the same atom size, so they dissolve",
              "in each other from 0 to 100 % - no eutectic and no two-phase gap.")
    return svg(W, 326, b)


# ---------------------------------------------------------------- 5 Pb-Sn
def pbsn_diagram():
    b = heading("Lead-tin: a eutectic system", "two solid solutions and one eutectic point")
    x0, y0, w, h = 50, 56, 282, 168
    mx, my = _map(x0, y0, w, h, 0, 100, 150, 350)
    b += axes(x0, y0, w, h, "tin (% by weight)", "T (C)",
              xticks=((0, "0"), (0.2, "20"), (0.4, "40"), (0.6, "60"), (0.8, "80"), (1, "100")),
              yticks=((0, "150"), (0.25, "200"), (0.5, "250"), (0.75, "300"), (1, "350")))
    liquidus = [(0, 327), (10, 305), (20, 280), (30, 258), (40, 232), (50, 212), (61.9, 183),
                (70, 193), (80, 205), (90, 218), (100, 232)]
    alpha_sol = [(0, 327), (5, 300), (10, 270), (19.2, 183)]
    alpha_solv = [(19.2, 183), (8, 165), (2, 150)]
    beta_sol = [(100, 232), (98.5, 205), (97.5, 183)]
    beta_solv = [(97.5, 183), (99, 165), (100, 150)]
    b += ln(mx(19.2), my(183), mx(97.5), my(183), INK, 1.0)
    b += curve([(mx(a), my(c)) for a, c in liquidus], ORANGE, 2.0)
    b += curve([(mx(a), my(c)) for a, c in alpha_sol], BLUE, 1.8)
    b += curve([(mx(a), my(c)) for a, c in alpha_solv], BLUE, 1.4, dash="4,3")
    b += curve([(mx(a), my(c)) for a, c in beta_sol], GREEN, 1.8)
    b += curve([(mx(a), my(c)) for a, c in beta_solv], GREEN, 1.4, dash="4,3")
    b += dots([(mx(61.9), my(183))], RED, 2.6)
    b += text(mx(61.9), my(183) + 12, "eutectic 183 C, 61.9 % Sn", 6.4, color=RED)

    b += lbl(mx(72), my(300), "L (liquid)", size=7.4, weight="bold")
    b += lbl(mx(24), my(250), "L + α", size=6.8, color=BLUE)
    b += lbl(mx(74), my(240), "L + β", size=6.8, color=GREEN)
    b += lbl(mx(7), my(232), "α", size=7.2, color=BLUE, weight="bold")
    b += leader(mx(90.5), my(214), mx(98.4), my(199), GREY)
    b += text(mx(90), my(216), "β", 7.2, anchor="end", color=GREEN, weight="bold")
    b += text(mx(80), my(158), "α + β below the eutectic line", 6.2, color=GREY)

    t = 200
    c_l = _interp(liquidus, t)
    c_s = _interp(alpha_sol, t)
    b += guide(mx(0), my(t), mx(c_l), my(t))
    b += dots([(mx(c_s), my(t)), (mx(c_l), my(t))], INK, 2.0)
    b += text(mx(c_s) + 3, my(t) - 5, f"{c_s:.0f} %", 6.4, anchor="start", color=BLUE)
    b += text(mx(c_l) + 3, my(t) - 5, f"{c_l:.0f} %", 6.4, anchor="start", color=ORANGE)

    b += note_box(6, 240, 348, 46, "lever rule for a 40 % Sn alloy at 200 C",
                  [f"W(liquid) = (40 - {c_s:.0f})/({c_l:.0f} - {c_s:.0f}) = 0.60   and   W(α) = 0.40",
                   "only 19 % tin dissolves in lead at 183 C, so solder is a two-phase alloy"])
    b += foot(296, "Solder and type metal sit near a eutectic because a eutectic alloy melts and",
              "freezes at one low temperature, with no pasty range.")
    return svg(W, 320, b)


# ---------------------------------------------------------------- 6 Fe-Fe3C
def fec_diagram():
    b = heading("The iron-iron carbide diagram", "carbon steel on the left, cast iron on the right")
    x0, y0, w, h = 44, 60, 292, 180
    ylo, yhi = 600, 1600
    split, keep = 2.2, 0.5

    def mx(c):
        if c <= split:
            return x0 + c / split * keep * w
        return x0 + keep * w + (c - split) / (6.67 - split) * (1 - keep) * w

    def my(t):
        return y0 + h - (t - ylo) / (yhi - ylo) * h

    b += axes(x0, y0, w, h, "carbon (% by weight)", "", xticks=(),
              yticks=((0, "600"), (0.2, "800"), (0.4, "1000"), (0.6, "1200"), (0.8, "1400"),
                      (1, "1600")))
    b += text(x0 + 2, y0 - 10, "T (C)", 8.8, anchor="start", weight="bold")
    # an axis break, because the steel corner needs the room
    for dx in (4, 9):
        b += ln(x0 + keep * w + dx - 4, y0 + h + 4, x0 + keep * w + dx + 2, y0 + h - 4, INK, 1.1)
    for c, s_, anchor in ((0, "0", "middle"), (0.8, "0.8", "middle"), (2.14, "2.14", "end"),
                          (4.3, "4.3", "middle"), (6.67, "6.67", "middle")):
        b += ln(mx(c), y0 + h, mx(c), y0 + h + 3, INK, 1.0)
        b += text(mx(c), y0 + h + 13, s_, 7.0, anchor=anchor, color=GREY)
    b += text(x0 + 2, y0 + h + 26, "carbon axis compressed beyond 2.2 %", 6.2, anchor="start",
              color=GREY)

    A, H, J, Bn, N, D, E, C, Fp, G, S, P, K = ((0, 1538), (0.09, 1493), (0.17, 1493),
                                               (0.53, 1493), (0, 1394), (6.67, 1227),
                                               (2.14, 1147), (4.3, 1147), (6.67, 1147),
                                               (0, 912), (0.8, 727), (0.02, 727), (6.67, 727))

    def line(p1, p2, col=INK, wd=1.5, dash=None):
        return ln(mx(p1[0]), my(p1[1]), mx(p2[0]), my(p2[1]), col, wd, dash)

    b += line(A, Bn, ORANGE, 1.9)
    b += line(Bn, C, ORANGE, 1.9)
    b += line(C, D, ORANGE, 1.9)
    b += line(A, H, BLUE, 1.7)
    b += line(H, Bn, INK, 1.2)
    b += line(H, N, BLUE, 1.3, "4,3")
    b += line(J, N, BLUE, 1.5)
    b += line(J, E, BLUE, 1.7)
    b += line(E, C, INK, 1.2)
    b += line(C, Fp, INK, 1.2)
    b += line(E, S, PURPLE, 1.6)
    b += line(G, S, PURPLE, 1.6)
    b += line(P, S, INK, 1.2)
    b += line(S, K, INK, 1.2)
    b += line(P, (0.008, 620), BLUE, 1.0, "3,2")
    b += dots([(mx(0.8), my(727)), (mx(4.3), my(1147)), (mx(2.14), my(1147))], INK, 1.9)

    b += lbl(mx(1.30), my(1450), "L (liquid)", size=7.4, weight="bold")
    b += lbl(mx(3.00), my(1200), "L + γ", size=6.8, color=ORANGE)
    b += leader(mx(5.30), my(1252), mx(5.10), my(1150), GREY)
    b += text(mx(5.30) + 2, my(1252) - 3, "L + Fe3C", 6.4, anchor="start", color=ORANGE)
    b += lbl(mx(1.00), my(1275), "γ austenite", size=7.2, color=BLUE, weight="bold")
    b += text(mx(0.09) + 5, my(1445), "δ", 7.2, anchor="start", color=BLUE, weight="bold")
    b += lbl(mx(0.40), my(805), "α + γ", size=6.6, color=BLUE)
    b += lbl(mx(0.25), my(880), "A3", size=6.2, color=PURPLE)
    b += lbl(mx(1.92), my(822), "Acm", size=6.2, color=PURPLE)
    b += lbl(mx(2.70), my(950), "γ + Fe3C", size=6.6, color=PURPLE)
    b += text(mx(6.67) - 3, my(900), "Fe3C (cementite)", 6.4, anchor="end", color=GREY)
    b += text(mx(0.05) + 4, my(690), "α", 7.2, anchor="start", color=BLUE, weight="bold")
    b += text(mx(0.30), my(660), "α + Fe3C (pearlite)", 6.2, anchor="start", color=GREY)
    b += text(mx(4.30), my(1147) + 12, "eutectic line 1147 C", 6.2, color=INK)
    b += text(mx(4.60), my(727) - 5, "A1 727 C", 6.2, anchor="start", color=INK)

    b += note_box(6, 280, 348, 40, "eutectoid, the reaction every heat treatment works around",
                  ["cool 0.8 % C austenite through 727 C: γ -> α + Fe3C, and the two grow as pearlite"])
    b += foot(328, "Steel holds up to 2.14 % C and cast iron above it; hypoeutectoid steel is ferrite",
              "plus pearlite, hypereutectoid steel is pearlite plus a brittle cementite network.")
    return svg(W, 362, b)


# ---------------------------------------------------------------- 7 microstructures
def microstructures():
    b = heading("Microstructures across the eutectoid", "0.4 %, 0.8 % and 1.2 % carbon")
    for x in (6, 126, 246):
        b += panel(x, 46, 108, 118)

    def colonies(px, dark=False, network=False):
        out = ""
        for cx, cy in ((30, 26), (72, 24), (90, 58), (42, 60), (30, 96), (72, 96)):
            X, Y = px + cx, 46 + cy
            pts = [(X - 16, Y - 13), (X + 16, Y - 12), (X + 17, Y + 12), (X - 15, Y + 13)]
            if dark:
                out += poly(pts, INK, 0.8, close=True, fill="#5A6472")
                for k in range(3):
                    out += ln(X - 14, Y + 6 - 3 * k, X + 14, Y + 8 - 3 * k, "#C9D2DC", 0.5)
            else:
                out += poly(pts, INK, 0.9, close=True, fill="#EEF2F7")
                for k in range(7):
                    out += ln(X - 14 + k * 4, Y - 10, X - 12 + k * 4, Y + 10, "#5A6472", 0.7)
                if network:
                    out += poly(pts, "#FFFFFF", 3.0, close=True, fill="none")
                    out += poly(pts, "#8A94A2", 0.7, close=True, fill="none")
        return out

    # 0.4 % C: a ferrite field with 49 % pearlite in it
    b += grain_field(9, 49, 102, 112, cols=4, rows=4, seed=5, lw=0.6,
                     fills=("#FDFDFB", "#F7F8F3", "#FBFBF6"))
    b += colonies(6, dark=True)
    # 0.8 % C: pearlite fills the field
    b += f'<rect x="127" y="47" width="106" height="116" fill="#E6ECF3"/>'
    b += colonies(126)
    # 1.2 % C: pearlite plus a cementite network on the colony boundaries
    b += f'<rect x="247" y="47" width="106" height="116" fill="#E6ECF3"/>'
    b += colonies(246, network=True)

    for x, top, mid, tail in (
            (60, "0.4 % C", "ferrite + pearlite", "49 % pearlite"),
            (180, "0.8 % C", "100 % pearlite", "the eutectoid"),
            (300, "1.2 % C", "pearlite + Fe3C", "6.8 % cementite")):
        b += text(x, 178, top, 8.2, weight="bold")
        b += text(x, 190, mid, 6.4, color=GREY)
        b += text(x, 200, tail, 6.2, color=GREY)
    b += text(180, 214, "pearlite = alternate lamellae of soft ferrite and hard cementite", 8.6,
              color=GREY)

    b += note_box(6, 226, 348, 58, "why the carbon content is read off the micrograph",
                  ["pearlite % = (C - 0.02)/(0.8 - 0.02) x 100 : 0.4 % C gives 49 %, 0.8 % gives 100",
                   "cementite % = (C - 0.8)/(6.67 - 0.8) x 100 : 1.2 % C gives 6.8 % network",
                   "more carbon means more cementite: harder, stronger, and much less ductile"])
    b += foot(292, "Dark lamellae are cementite and the pale ones ferrite; a faster cool gives a",
              "finer spacing, and a finer pearlite is a harder one.")
    return svg(W, 316, b)


# ---------------------------------------------------------------- 8 Hall-Petch
def hall_petch():
    b = heading("Grain size sets the yield strength", "Hall-Petch: σy = σ0 + k d^-1/2")
    x0, y0, w, h = 52, 60, 276, 134
    mx, my = _map(x0, y0, w, h, 2, 12, 100, 420)
    b += axes(x0, y0, w, h, "d^-1/2  (mm^-1/2)", "yield (MPa)",
              xticks=((0, "2"), (0.2, "4"), (0.4, "6"), (0.6, "8"), (0.8, "10"), (1, "12")),
              yticks=((0, "100"), (0.25, "180"), (0.5, "260"), (0.75, "340"), (1, "420")))
    s0, k = 100.0, 23.4
    pts = [(d, s0 + k * d) for d in (2, 3, 4, 5, 6, 8, 10, 12)]
    b += curve([(mx(a), my(c)) for a, c in pts], PURPLE, 2.2)
    b += dots([(mx(a), my(c)) for a, c in pts], INK, 1.8)
    b += text(mx(2) + 6, my(s0 + k * 2) + 11, "grain size 0.25 mm", 6.2, anchor="start",
              color=GREY)
    b += text(mx(12) - 4, my(s0 + k * 12) - 7, "grain size 0.007 mm", 6.2, anchor="end",
              color=GREY)
    b += text(mx(9.6), my(178), "σ0 = 100 MPa", 6.6, anchor="end", color=GREY)
    b += text(mx(9.6), my(160), "k = 23.4 MPa mm^0.5", 6.6, anchor="end", color=GREY)

    b += note_box(6, 226, 348, 58, "same steel, two grain sizes",
                  ["d = 0.0625 mm (ASTM 6):  σy = 100 + 23.4 x 4 = 194 MPa",
                   "d = 0.0156 mm (ASTM 10): σy = 100 + 23.4 x 8 = 287 MPa",
                   "grain refinement is the one strengthening method that also raises toughness"])
    b += foot(294, "A grain boundary blocks a moving dislocation, so a finer grain forces the",
              "dislocation to turn more often; normalising a steel is done for this.")
    return svg(W, 330, b)


DIAGRAMS = {
    "u2_coolcurve": cooling_curves,
    "u2_ingot": ingot_grains,
    "u2_solution": solid_solution,
    "u2_cuni": cuni_diagram,
    "u2_pbsn": pbsn_diagram,
    "u2_fec": fec_diagram,
    "u2_micro": microstructures,
    "u2_hallpetch": hall_petch,
}
