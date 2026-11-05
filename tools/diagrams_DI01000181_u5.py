"""Eight figures for Engineering Materials Science (DI01000181) Unit 5.

Surfaces, coatings, oil and corrosion. The numbers are the ones quoted in the notes and used in the
six numericals: 11.7 micron of nickel from 300 A/m2 for 20 minutes, the coating thicknesses that
separate a PVD film from a paint system, the Walther viscosity curves of a VI 70 and a VI 150 oil
that are both 10 cSt at 100 C, and the 0.116 mm per year that 0.1 A/m2 of corrosion current eats out
of steel. Nothing is sketched by eye.
"""
import math

from diagrams_DI01000181_lib import (INK, GREY, THIN, BLUE, GREEN, ORANGE, RED, PURPLE, TEAL, W,
                                     AMBER, SKY, GLASS, STEEL, svg, text, ln, arrow, heading, foot,
                                     panel, note_box, lbl, leader, poly, curve, dots, axes, guide,
                                     film_stack)


def _map(x0, y0, w, h, xlo, xhi, ylo, yhi):
    def mx(v):
        return x0 + (v - xlo) / (xhi - xlo) * w

    def my(v):
        return y0 + h - (v - ylo) / (yhi - ylo) * h

    return mx, my


def _walther(nu40, nu100):
    """Fit log10(log10(nu + 0.7)) = A - B log10(T) through two measured points."""
    def z(nu):
        return math.log10(math.log10(nu + 0.7))

    t1, t2 = math.log10(40 + 273.15), math.log10(100 + 273.15)
    b = (z(nu40) - z(nu100)) / (t2 - t1)
    a = z(nu40) + b * t1
    return a, b


def _nu(a, b, temp_c):
    lg = a - b * math.log10(temp_c + 273.15)
    return 10 ** (10 ** lg) - 0.7


# ---------------------------------------------------------------- 1 the surface zone
def surface_zone():
    b = heading("The surface is a different material", "the top micrometres decide the life")
    b += poly([(40, 52), (230, 52), (230, 62), (40, 62)], ORANGE, 1.1, close=True, fill="#F6E3C5")
    b += poly([(40, 62), (230, 62), (230, 92), (40, 92)], BLUE, 1.1, close=True, fill="#DCEEFB")
    b += poly([(40, 92), (230, 92), (230, 150), (40, 150)], THIN, 1.1, close=True, fill=STEEL)

    b += text(135, 80, "diffused or work-hardened zone, 0.1 - 1 mm", 6.4, color=BLUE,
              weight="bold")
    b += text(135, 125, "bulk metal: unchanged", 6.4, color=GREY)

    b += leader(230, 57, 240, 57)
    b += text(244, 55, "coating or converted", 6.4, anchor="start", color=ORANGE, weight="bold")
    b += text(244, 64, "layer, 5 - 25 micron", 6.2, anchor="start", color=ORANGE)
    b += text(40, 164, "bending stress is highest at the surface: the outer 10 % of a",
              6.4, anchor="start", color=GREY)
    b += text(40, 174, "shaft carries 19 % of the moment, the outer 1 % carries 2 %.", 6.4,
              anchor="start", color=GREY)

    b += note_box(6, 184, 348, 68, "four things a surface has to do, and the process for each",
                  ["wear: a hard film or a nitrided skin, 900 - 1100 HV on a tough core",
                   "corrosion: a barrier of paint, plating or oxide, or a sacrificial zinc",
                   "fatigue: a compressive skin from shot peening or roller burnishing",
                   "friction: phosphate plus oil, or a low-friction coating such as PTFE"])
    b += foot(264, "A part almost never fails in the middle: fretting, pitting, fatigue and wear all",
              "begin in the first few micrometres, which is why the surface is engineered.")
    return svg(W, 286, b)


# ---------------------------------------------------------------- 2 surface finish
def surface_finish():
    b = heading("Mechanical finishing, and the roughness you buy",
                "each step roughly halves the roughness")
    rows = (("drilling", 6.3, GREY), ("turning", 3.2, BLUE), ("milling", 1.6, BLUE),
            ("grinding", 0.8, TEAL), ("honing", 0.2, ORANGE), ("lapping", 0.05, PURPLE))
    x0, top, span = 96, 58, 200
    lo, hi = 0.04, 12.5
    for i, (name, ra, col) in enumerate(rows):
        yy = top + i * 20
        b += text(x0 - 8, yy + 4, name, 6.8, anchor="end")
        wid = (math.log10(hi) - math.log10(ra)) / (math.log10(hi) - math.log10(lo)) * span
        b += poly([(x0, yy - 4), (x0 + wid, yy - 4), (x0 + wid, yy + 5), (x0, yy + 5)],
                  col, 0.7, close=True,
                  fill={"#666666": "#E9EDF1", "#1565C0": "#DCEEFB", "#00695C": "#D8EDEA",
                        "#B66A00": "#F6E3C5", "#7B2CD9": "#EFE4FB"}[col])
        b += text(x0 + wid + 5, yy + 4, f"{ra:g} um", 6.2, anchor="start", color=GREY)
    b += text(x0, top + len(rows) * 20 + 2, "longer bar = finer finish, log scale", 6.2,
              anchor="start", color=GREY)

    b += note_box(6, 190, 348, 58, "clean first, finish second - and never the other way round",
                  ["degrease with alkali or solvent, pickle to descale, then blast or brush",
                   "blast profile 50 - 75 um is what a paint keys into; a polished face has nothing",
                   "pickling too long on a hardened part puts hydrogen in: bake it at 200 C"])
    b += foot(262, "A coating cannot hide a scratch and a plating copies the profile it grows on, so",
              "the roughness is chosen before the coating, not after it.")
    return svg(W, 284, b)


# ---------------------------------------------------------------- 3 plating cell
def plating_cell():
    b = heading("Electroplating: nickel anode, work cathode", "the metal moves atom by atom")
    b += poly([(52, 58), (308, 58), (308, 176), (52, 176)], INK, 1.4, close=True, fill="#F7FBFF")
    b += poly([(55, 84), (305, 84), (305, 173), (55, 173)], BLUE, 0.0, close=True, fill="#DCEEFB")

    # anode and cathode plates
    b += poly([(92, 76), (104, 76), (104, 160), (92, 160)], ORANGE, 1.2, close=True, fill="#F6E3C5")
    b += poly([(250, 76), (262, 76), (262, 160), (250, 160)], THIN, 1.2, close=True, fill=STEEL)
    b += poly([(243, 76), (250, 76), (250, 160), (243, 160)], GREEN, 1.0, close=True, fill="#D8EEDA")

    b += text(98, 54, "anode (+)", 6.4, color=ORANGE, weight="bold")
    b += text(256, 54, "cathode (-)", 6.4, color=INK, weight="bold")
    b += text(98, 168, "nickel", 6.2, color=ORANGE)
    b += text(256, 168, "work", 6.2, color=INK)
    b += text(240, 142, "deposit", 6.0, anchor="end", color=GREEN)

    # battery and wires
    b += ln(98, 76, 98, 44, INK, 1.3) + ln(256, 76, 256, 44, INK, 1.3)
    b += ln(98, 44, 166, 44, INK, 1.3) + ln(188, 44, 256, 44, INK, 1.3)
    b += ln(170, 36, 170, 52, INK, 1.8) + ln(180, 40, 180, 48, INK, 1.0)
    b += text(175, 55, "d.c. supply", 6.2, weight="bold")

    # ions in the bath
    b += text(175, 96, "Ni2+", 7.0, color=BLUE, weight="bold")
    for i in range(4):
        b += dots([(128 + i * 30, 112), (140 + i * 28, 132), (132 + i * 30, 150)], BLUE, 1.6)
    b += arrow(196, 120, 238, 120, BLUE, 1.0, 4)
    b += text(175, 176 + 12, "electrolyte: NiSO4 + NiCl2 + boric acid", 6.2, color=INK)

    b += note_box(6, 196, 348, 58, "Faraday's law is the whole calculation",
                  ["1 ampere-hour deposits 1.095 g of nickel: m = M I t /(n F) = 58.7/(2 x 96500)",
                   "300 A/m2 for 20 min at 95 % efficiency gives 11.7 micron of nickel",
                   "throwing power: chromium covers a recess badly, cyanide zinc covers it well"])
    b += foot(268, "The anode dissolves as the cathode grows, so the bath keeps its metal;",
              "only the addition agent decides bright or dull, hard or soft.")
    return svg(W, 290, b)


# ---------------------------------------------------------------- 4 coating thicknesses
def coating_thickness():
    b = heading("Every coating, on one scale of thickness", "from 0.3 micron to 220 micron")
    rows = (("chromate passivation", 0.3, PURPLE), ("PVD TiN film", 3.0, TEAL),
            ("phosphate coating", 5.0, ORANGE), ("CVD coating", 10.0, TEAL),
            ("electroplated zinc", 15.0, BLUE), ("anodised aluminium", 20.0, BLUE),
            ("hot dip galvanising", 80.0, GREY), ("paint system, 3 coats", 220.0, GREEN))
    x0, top, span = 126, 58, 172
    for i, (name, t, col) in enumerate(rows):
        yy = top + i * 18
        b += text(x0 - 6, yy + 4, name, 6.4, anchor="end")
        wid = max(2.0, t / 240 * span)
        b += poly([(x0, yy - 3.5), (x0 + wid, yy - 3.5), (x0 + wid, yy + 4.5), (x0, yy + 4.5)],
                  col, 0.7, close=True,
                  fill={"#7B2CD9": "#EFE4FB", "#00695C": "#D8EDEA", "#B66A00": "#F6E3C5",
                        "#1565C0": "#DCEEFB", "#666666": "#E9EDF1", "#2E7D32": "#D8EEDA"}[col])
        b += text(x0 + wid + 5, yy + 4, f"{t:g} um", 6.2, anchor="start", color=GREY)

    b += note_box(6, 208, 348, 58, "what the thickness buys, and what it costs",
                  ["PVD is thin because it is hard and dense; paint is thick because it is a barrier",
                   "zinc protects by being consumed, so its thickness is a life in years, not a finish",
                   "hot dip 80 um in a rural atmosphere is 20 years; the same steel painted is 8"])
    b += foot(280, "Thickness is the first number on any coating specification, and the second is",
              "adhesion: a thick coat that lifts is worse than a thin one that stays.")
    return svg(W, 300, b)


# ---------------------------------------------------------------- 5 viscosity against temperature
def viscosity_temperature():
    b = heading("Viscosity against temperature, and what VI means",
                "the same 10 cSt at 100 C, and a different oil at 30 C")
    x0, y0, w, h = 46, 62, 250, 132
    mx, my = _map(x0, y0, w, h, 30, 120, 0, 340)
    b += axes(x0, y0, w, h, "", "cSt", xticks=[(0, "30"), (30 / 90, "60"), (60 / 90, "90"),
                                              (90 / 90, "120")],
              yticks=[(0, "0"), (100 / 340, "100"), (200 / 340, "200"), (300 / 340, "300")], size=7.4)
    b += text(x0 + w + 4, y0 + h + 24, "temperature, C", 6.8, anchor="end", weight="bold")

    for nu40, nu100, col, name in ((150, 10, RED, "VI 70"), (68, 10, GREEN, "VI 150")):
        a, bb = _walther(nu40, nu100)
        pts = [(mx(t), my(min(340, _nu(a, bb, t)))) for t in range(30, 121, 5)]
        b += curve(pts, col, 2.2)
        lab_t, lab_v = (46, 114) if name == "VI 70" else (46, 62)
        b += text(mx(lab_t), my(lab_v), name, 6.8, anchor="start", color=col, weight="bold")

    b += guide(mx(30), my(10), mx(120), my(10))
    b += text(mx(86), my(250), "both oils: 10 cSt at 100 C", 6.4, color=GREY)
    b += dots([(mx(100), my(10))], INK, 2.2)
    b += text(mx(31), my(316) - 6, "316 cSt at 30 C", 6.2, anchor="start", color=RED)
    b += text(mx(31), my(110) - 6, "110 cSt", 6.2, anchor="start", color=GREEN)

    b += note_box(6, 216, 348, 58, "the three numbers on an oil drum that matter first",
                  ["ISO VG is the nominal viscosity at 40 C: VG 68 runs 61.2 to 74.8 cSt, a spread of 10 %",
                   "VI says how little it thins when hot: 70 is a plain mineral oil, 150 a good multigrade",
                   "pour point is the cold limit, flash point the fire limit: -9 C and 200 C for VG 68"])
    b += foot(288, "An oil is chosen for its viscosity at the running temperature, not at the drum, so a",
              "high-VI oil is worth its price on a machine that starts cold and runs hot.")
    return svg(W, 308, b)


# ---------------------------------------------------------------- 6 the paint film
def paint_film():
    b = heading("A paint system in section, on a blasted steel plate",
                "four coats, each with a job")
    layers = ((16, "#DCEEFB", BLUE, "topcoat: colour and weather, 40 um"),
              (22, "#E8F3E9", GREEN, "intermediate: build and barrier, 100 um"),
              (20, "#F6E3C5", ORANGE, "zinc-rich primer: adhesion and protection, 75 um"),
              (46, "#E7EDF3", THIN, "steel, blast cleaned to Sa 2 1/2"))
    b += film_stack(46, 52, 190, layers, size=6.4)

    b += leader(236, 60, 244, 60)
    b += text(248, 63, "UV, rain", 6.2, anchor="start", color=BLUE)
    b += leader(236, 92, 244, 92)
    b += text(248, 95, "oxygen and water", 6.2, anchor="start", color=GREEN)
    b += leader(236, 118, 244, 118)
    b += text(248, 121, "rust if it gets in", 6.2, anchor="start", color=ORANGE)
    b += text(248, 148, "215 um total", 6.4, anchor="start", weight="bold")

    b += note_box(6, 164, 348, 58, "the specification, written in three numbers",
                  ["blast to Sa 2 1/2 with a 50 - 75 um profile: that profile is what the paint grips",
                   "wet film = dry film x 100/% solids: 75 um dry at 60 % solids is 125 um wet",
                   "120 m2 at 75 um with 60 % solids needs 15 litres, and 17.3 with a 15 % loss"])
    b += foot(236, "Paint is a system of coats, each with its own job, and 80 % of the failures are",
              "preparation failures: the film let go of the steel, it did not wear out.")
    return svg(W, 256, b)


# ---------------------------------------------------------------- 7 the corrosion cell
def corrosion_cell():
    b = heading("Why steel rusts: a cell on one surface",
                "an anode, a cathode and an electrolyte between them")
    b += poly([(30, 112), (330, 112), (330, 158), (30, 158)], THIN, 1.2, close=True, fill=STEEL)
    b += poly([(30, 84), (330, 84), (330, 112), (30, 112)], BLUE, 0.8, close=True, fill="#DCEEFB")
    b += text(180, 96, "water film with dissolved oxygen: the electrolyte", 6.4, color=BLUE)
    b += text(180, 136, "steel: the electron path", 6.4, color=GREY)


    # anodic pit and rust
    b += poly([(84, 112), (100, 112), (92, 126)], RED, 1.4, close=True, fill="#F7DDE3")
    b += text(92, 64, "anode", 7.0, color=RED, weight="bold")
    b += text(92, 73, "Fe -> Fe2+ + 2e-", 6.2, color=RED)
    b += arrow(92, 78, 92, 90, RED, 1.0, 4)
    b += text(92, 103, "rust", 6.0, color=RED)

    b += text(258, 64, "cathode", 7.0, color=BLUE, weight="bold")
    b += text(258, 73, "O2 + 2H2O + 4e- -> 4OH-", 6.2, color=BLUE)
    b += arrow(258, 78, 258, 92, BLUE, 1.0, 4)

    b += arrow(104, 128, 244, 128, INK, 1.2, 5)
    b += text(174, 124, "electrons in the metal", 6.2, color=INK)

    b += note_box(6, 168, 348, 68, "the four things every corrosion cell needs",
                  ["an anode that dissolves, a cathode that consumes electrons, an electrolyte, a path",
                   "standard potentials: Mg -2.37, Zn -0.76, Fe -0.44, Cu +0.34 V against hydrogen",
                   "a zinc to copper couple is 1.10 V, a zinc to iron couple is 0.32 V",
                   "0.1 A per m2 of corrosion current is 0.116 mm of steel a year"])
    b += foot(254, "The cathode does not corrode and the anode does, so a small anode joined to a",
              "large cathode - a stainless bolt in a steel frame - pits through fast.")
    return svg(W, 274, b)


# ---------------------------------------------------------------- 8 six corrosion types
def corrosion_types():
    b = heading("Six ways a surface corrodes",
                "the shape of the damage names the mechanism, and so does the defence")
    cells = (
        ("UNIFORM", GREY, "even loss over the whole area", "allow a corrosion allowance"),
        ("GALVANIC", BLUE, "two metals joined, the less noble goes", "insulate the joint, coat both"),
        ("PITTING", RED, "chloride breaks a passive film", "higher Mo grade, keep it clean"),
        ("CREVICE", ORANGE, "stagnant liquid under a gasket", "weld instead of lap, seal the gap"),
        ("STRESS CRACKING", PURPLE, "tensile stress plus chloride", "stress relieve, lower the load"),
        ("EROSION", TEAL, "fast wet flow scours the film", "change the geometry, hard facing"),
    )
    for i, (name, col, what, fix) in enumerate(cells):
        px = 6 + (i % 2) * 176
        py = 46 + (i // 2) * 78
        b += panel(px, py, 172, 72, fill="#FBFCFD")
        b += text(px + 86, py + 13, name, 7.0, weight="bold", color=col)
        # a small sketch of the damage on a surface line
        sy = py + 32
        b += poly([(px + 14, sy - 6), (px + 158, sy - 6), (px + 158, sy + 6), (px + 14, sy + 6)],
                  THIN, 0.9, close=True, fill=STEEL)
        if name == "UNIFORM":
            b += ln(px + 14, sy, px + 158, sy, col, 2.0, "3,2")
        elif name == "GALVANIC":
            b += ln(px + 86, sy - 6, px + 86, sy + 6, INK, 1.0)
            b += poly([(px + 16, sy - 6), (px + 62, sy - 6), (px + 74, sy - 1),
                       (px + 62, sy + 6), (px + 16, sy + 6)], col, 1.0, close=True,
                      fill="#F7DDE3")
            b += text(px + 40, sy + 2.4, "eaten", 5.6, color=col)
        elif name == "PITTING":
            for k in range(4):
                xx = px + 30 + k * 32
                b += poly([(xx - 6, sy - 6), (xx, sy + 4), (xx + 6, sy - 6)], col, 1.0,
                          close=True, fill="#F7DDE3")
        elif name == "CREVICE":
            b += poly([(px + 40, sy - 14), (px + 120, sy - 14), (px + 120, sy - 6),
                       (px + 40, sy - 6)], GREY, 1.0, close=True, fill="#E9EDF1")
            b += poly([(px + 52, sy - 6), (px + 108, sy - 6), (px + 108, sy + 2),
                       (px + 52, sy + 2)], col, 1.0, close=True, fill="#F6E3C5")
        elif name == "STRESS CRACKING":
            b += poly([(px + 74, sy - 6), (px + 78, sy - 2), (px + 72, sy + 2),
                       (px + 80, sy + 6)], col, 1.6)
            b += arrow(px + 30, sy - 12, px + 60, sy - 12, col, 1.0, 4)
            b += arrow(px + 120, sy - 12, px + 90, sy - 12, col, 1.0, 4)
        elif name == "EROSION":
            for k in range(5):
                xx = px + 34 + k * 24
                b += poly([(xx, sy - 6), (xx + 12, sy - 2), (xx + 24, sy - 6)], col, 1.4)
        b += text(px + 86, py + 50, what, 6.0, color=INK)
        b += text(px + 86, py + 62, fix, 6.0, color=GREEN)

    b += foot(288, "Uniform loss can be paid for with thickness; the other five cannot, so they",
              "have to be designed out rather than allowed for.")
    return svg(W, 308, b)


TITLES = {
    "u5_surface": "The surface zone",
    "u5_finish": "Surface finish and what it costs",
    "u5_plate": "An electroplating cell",
    "u5_thick": "Coating thickness on one scale",
    "u5_visc": "Viscosity against temperature",
    "u5_paint": "A paint system in section",
    "u5_corr": "The corrosion cell",
    "u5_types": "Six types of corrosion",
}

CAPTIONS = {
    "u5_surface": "The coating, the treated zone beneath it and the untouched bulk: a part fails at the "
                  "surface because that is where the stress, the wear and the environment meet.",
    "u5_finish": "Drilling at 6.3 micron to lapping at 0.05 micron, each step buying a quarter of the "
                 "roughness - and none of it working unless the surface is clean first.",
    "u5_plate": "The anode dissolves into the electrolyte and the work as cathode grows the same metal "
                "back, one Faraday at a time: 300 A/m2 for twenty minutes is 11.7 micron of nickel.",
    "u5_thick": "A PVD film at 3 micron protects a cutting edge, a paint system at 220 micron protects a "
                "bridge, and hot dip zinc at 80 micron protects by being consumed, not by being hard.",
    "u5_visc": "Two oils that are both 10 cSt at 100 C: at 30 C one is 110 cSt and the other 316, and that "
               "difference is what the viscosity index measures.",
    "u5_paint": "Four coats on a blasted plate, each with its own job, and a total dry film of 215 micron "
                "that only works if every coat keyed to the one below it.",
    "u5_corr": "An anode, a cathode, an electrolyte and a path: steel rusts where the oxygen arrives and "
               "the metal gives up electrons, and 0.1 A/m2 costs 0.116 mm a year.",
    "u5_types": "Uniform, galvanic, pitting, crevice, stress cracking and erosion: only the first can be "
                "paid for with a corrosion allowance, so the other five have to be designed out.",
}

DIAGRAMS = {
    "u5_surface": surface_zone,
    "u5_finish": surface_finish,
    "u5_plate": plating_cell,
    "u5_thick": coating_thickness,
    "u5_visc": viscosity_temperature,
    "u5_paint": paint_film,
    "u5_corr": corrosion_cell,
    "u5_types": corrosion_types,
}
