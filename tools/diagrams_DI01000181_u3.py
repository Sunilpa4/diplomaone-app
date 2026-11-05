"""Seven figures for Engineering Materials Science (DI01000181) Unit 3 - metals and their alloys.

The numbers on these figures are the handbook values quoted in the notes: the strengths of the plain
carbon steels rise from about 400 MPa at 0.1 % C to about 900 MPa at 1.2 % C while the elongation
falls from 30 % to 5 %, the brasses and bronzes carry the compositions printed beside their bars, and
the aluminium series are the standard 1xxx to 8xxx groups. Nothing is sketched by eye.
"""
import math

from diagrams_DI01000181_lib import (INK, GREY, THIN, BLUE, GREEN, ORANGE, RED, PURPLE, TEAL, W,
                                     AMBER, SKY, GLASS, STEEL, svg, text, ln, arrow, heading, foot,
                                     panel, note_box, lbl, leader, poly, curve, dots, axes, guide,
                                     atom, electron, grain_field)


def _map(x0, y0, w, h, xlo, xhi, ylo, yhi):
    def mx(v):
        return x0 + (v - xlo) / (xhi - xlo) * w

    def my(v):
        return y0 + h - (v - ylo) / (yhi - ylo) * h

    return mx, my


# ---------------------------------------------------------------- 1 the family tree
def metal_tree():
    b = heading("Classification of the metals used in machines", "ferrous on the left, non-ferrous right")
    b += panel(6, 44, 168, 120, fill="#EEF4FC")
    b += text(90, 58, "FERROUS", 8.6, weight="bold", color=BLUE)
    b += text(90, 72, "steel, 0.02 - 2.14 % C", 6.4, color=GREY)
    for i, (name, tail) in enumerate((("plain carbon", "low / medium / high C"),
                                      ("alloy steel", "stainless, tool, HSLA"),
                                      ("cast iron", "2.14 - 6.67 % C"))):
        b += poly([(14, 82 + i * 25), (166, 82 + i * 25), (166, 103 + i * 25), (14, 103 + i * 25)],
                  BLUE, 0.8, close=True, fill="#FFFFFF")
        b += text(90, 91 + i * 25, name, 7.2, weight="bold")
        b += text(90, 99 + i * 25, tail, 5.8, color=GREY)

    b += panel(186, 44, 168, 120, fill="#FFF6EC")
    b += text(270, 58, "NON-FERROUS", 8.6, weight="bold", color=ORANGE)
    b += text(270, 72, "no iron, so no rust", 6.4, color=GREY)
    for i, (name, tail) in enumerate((("copper alloys", "brass, bronze, gunmetal"),
                                      ("aluminium alloys", "wrought 1xxx-7xxx, cast"),
                                      ("others", "Zn, Ni, Ti, Mg, Pb, Sn"))):
        b += poly([(194, 82 + i * 25), (346, 82 + i * 25), (346, 103 + i * 25), (194, 103 + i * 25)],
                  ORANGE, 0.8, close=True, fill="#FFFFFF")
        b += text(270, 91 + i * 25, name, 7.2, weight="bold")
        b += text(270, 99 + i * 25, tail, 5.8, color=GREY)

    b += note_box(6, 172, 348, 58, "the three families inside each branch",
                  ["steel: carbon steels by %C, alloy steels by the element added (Cr, Ni, Mo, V)",
                   "cast iron: grey, white, malleable, ductile and alloy - named by the graphite shape",
                   "non-ferrous: one base metal (Cu, Al, Zn, Ni) plus the elements that strengthen it"])
    b += foot(240, "Nine of every ten tonnes of metal in engineering are ferrous, because iron ore,",
              "coke and limestone make steel cheap; the non-ferrous tenth carries current, saves")
    b += foot(268, "weight or resists corrosion where steel cannot.", "")
    return svg(W, 296, b)


# ---------------------------------------------------------------- 2 carbon against strength
def carbon_strength():
    b = heading("Carbon buys strength and sells ductility", "plain carbon steels, slowly cooled")
    x0, y0, w, h = 50, 58, 278, 138
    mx, my = _map(x0, y0, w, h, 0, 1.3, 0, 1000)
    b += axes(x0, y0, w, h, "", "UTS (MPa)", xticks=(),
              yticks=((0, "0"), (0.25, "250"), (0.5, "500"), (0.75, "750"), (1, "1000")))
    b += text(x0 + w + 6, y0 + h + 30, "carbon (% by weight)", 8.8, anchor="end",
              weight="bold")
    for c, s_ in ((0, "0"), (0.2, "0.2"), (0.4, "0.4"), (0.6, "0.6"), (0.8, "0.8"),
                  (1.0, "1.0"), (1.2, "1.2")):
        b += ln(mx(c), y0 + h, mx(c), y0 + h + 3, INK, 1.0)
        b += text(mx(c), y0 + h + 13, s_, 7.0, color=GREY)
    uts = [(0.1, 400), (0.2, 450), (0.4, 600), (0.6, 700), (0.8, 800), (1.0, 870), (1.2, 900)]
    b += curve([(mx(a), my(c)) for a, c in uts], BLUE, 2.2)
    b += dots([(mx(a), my(c)) for a, c in uts], INK, 1.8)
    for a, c in uts:
        b += text(mx(a), my(c) - 7, f"{c}", 6.2, color=BLUE)
    b += text(mx(0.62), my(930), "UTS rises with carbon", 6.6, anchor="start", color=BLUE)

    # elongation on the same plot area, scaled to its own axis drawn on the right
    x1 = x0 + w
    b += arrow(x1, y0 + h, x1, y0 - 4, GREY, 1.1, 4)
    for e, s_ in ((0, "0"), (10, "10"), (20, "20"), (30, "30")):
        yy = y0 + h - e / 40 * h
        b += ln(x1 - 3, yy, x1, yy, GREY, 1.0)
        b += text(x1 - 5, yy + 2.6, s_, 6.6, anchor="end", color=GREY)
    b += text(x1 + 3, y0 - 10, "elongation (%)", 7.6, anchor="end", weight="bold", color=GREY)
    el = [(0.1, 30), (0.2, 27), (0.4, 20), (0.6, 15), (0.8, 10), (1.0, 7), (1.2, 5)]
    b += curve([(mx(a), y0 + h - c / 40 * h) for a, c in el], GREEN, 1.9, dash="5,3")
    b += dots([(mx(a), y0 + h - c / 40 * h) for a, c in el], GREEN, 1.5)


    b += note_box(6, 240, 348, 52, "what the two curves say together",
                  ["0.1 % C: 400 MPa but 30 % elongation - sheet, wire, car body",
                   "0.4 % C: 600 MPa and 20 % - shafts and axles, the engineering compromise",
                   "0.8 % C and above: 800 to 900 MPa with under 10 % - springs and cutting tools"])
    b += foot(302, "Strength x ductility is largest around 0.2 to 0.4 % C; above the eutectoid the",
              "cementite network makes the steel brittle faster than it makes it strong.")
    return svg(W, 328, b)


# ---------------------------------------------------------------- 3 cast irons
def cast_irons():
    b = heading("The four cast irons", "the same iron, four shapes of graphite")
    panels = ((6, "GREY", "flake graphite in pearlite", "150 - 300 MPa", "#5A6472"),
              (90, "WHITE", "all cementite, no graphite", "300 - 500 MPa", "#E8EDF4"),
              (174, "MALLEABLE", "rosettes of temper carbon", "350 - 450 MPa", "#3D4450"),
              (258, "DUCTILE", "nodules of graphite", "400 - 600 MPa", "#2E3339"))
    for x, name, tail, strength, tone in panels:
        b += panel(x, 46, 96, 104)
        b += text(x + 48, 60, name, 7.4, weight="bold", color=INK)
        b += grain_field(x + 7, 70, 82, 54, cols=3, rows=3, seed=7, lw=0.5)
        for i in range(5):
            gx = x + 16 + (i % 3) * 28
            gy = 78 + (i // 3) * 30
            if name == "DUCTILE":
                b += atom(gx, gy, 4.6, None, INK, tone)
            elif name == "MALLEABLE":
                for k in range(4):
                    b += ln(gx, gy + k, gx + 7, gy + k, tone, 1.6)
            elif name == "WHITE":
                b += poly([(gx - 8, gy - 6), (gx + 8, gy - 6), (gx + 8, gy + 6), (gx - 8, gy + 6)],
                          "#8A94A2", 1.4, close=True, fill="#F4F7FB")
            else:
                b += ln(gx - 6, gy, gx + 7, gy + 1, "#3D4450", 1.8)
                b += ln(gx - 2, gy - 4, gx + 2, gy + 5, "#3D4450", 1.4)
        b += text(x + 48, 137, tail, 5.6, color=GREY)
        b += text(x + 48, 146, strength, 5.6, color=GREY)

    b += note_box(6, 158, 348, 68, "how the graphite got that shape",
                  ["grey: slow cooling in a sand mould lets carbon come out as flakes",
                   "white: fast cooling or low silicon keeps carbon in cementite - hard, unmachinable",
                   "malleable: white iron is annealed, the cementite decomposes into temper carbon",
                   "ductile: a little magnesium or cerium is added, so the graphite grows as nodules"])
    b += foot(236, "A flake acts like a crack, so grey iron is weak in tension but excellent in",
              "compression and damping - machine beds, housings and manhole covers.")
    b += foot(264, "A nodule does not, so ductile iron reaches 600 MPa with 15 % elongation and",
              "replaces steel castings: crankshafts, gears, pipe and wagon wheels.")
    return svg(W, 292, b)


# ---------------------------------------------------------------- 4 copper alloys
def copper_alloys():
    b = heading("Copper and its alloys", "strength bought with conductivity")
    rows = (("copper 99.9 %", "Cu", 220, 100),
            ("brass 70/30", "Cu 70, Zn 30", 350, 28),
            ("brass 60/40", "Cu 60, Zn 40", 420, 26),
            ("bronze", "Cu 90, Sn 10", 320, 13),
            ("gunmetal", "Cu 88, Sn 10, Zn 2", 280, 12))
    x0, w = 112, 150
    for i, (name, comp, uts, iacs) in enumerate(rows):
        y = 62 + i * 34
        b += text(6, y + 4, name, 7.0, anchor="start", weight="bold")
        b += text(6, y + 12, comp, 5.6, anchor="start", color=GREY)
        b += poly([(x0, y - 7), (x0 + uts / 450 * w, y - 7), (x0 + uts / 450 * w, y + 5),
                   (x0, y + 5)], ORANGE, 0.8, close=True, fill="#F7C88A")
        b += text(x0 + uts / 450 * w + 4, y + 3, f"{uts} MPa", 6.4, anchor="start", color=INK)
        b += text(352, y + 3, f"{iacs} % IACS", 6.2, anchor="end", color=BLUE)
    b += ln(6, 232, 352, 232, THIN, 0.8)
    b += text(6, 244, "bar length = tensile strength;  the figure on the right is electrical",
              6.2, anchor="start", color=GREY)
    b += text(6, 254, "conductivity as % of the international annealed copper standard.",
              6.2, anchor="start", color=GREY)

    b += note_box(6, 260, 348, 68, "which one to pick",
                  ["copper: busbars, windings, electrodes - conductivity first, strength second",
                   "brass 70/30: deep drawing, cartridge cases, radiator fins - ductile and pretty",
                   "brass 60/40: hot stamping, screws, free-cutting rod on a capstan lathe",
                   "bronze and gunmetal: bearings, worm wheels, pump bodies, bells - wear and sea water"])
    b += foot(336, "Adding zinc raises strength but destroys conductivity, because the dissolved",
              "atoms scatter the free electrons; that trade-off decides every copper-alloy choice.")
    return svg(W, 372, b)


# ---------------------------------------------------------------- 5 common steel designations
def steel_designations():
    b = heading("Steels a workshop actually orders", "Indian designation, carbon and use")
    head = (("C10 / EN32", "0.10", "sheet, wire, nails"), ("C20 / EN3B", "0.20", "shafts, studs"),
            ("C40 / EN8", "0.40", "axles, gears"), ("C45 / EN9", "0.45", "shafts, keys"),
            ("C60 / EN42", "0.60", "springs, clips"), ("C80 / EN43", "0.80", "springs, wire rope"),
            ("EN19 (Cr-Mo)", "0.40", "gears, crank"), ("EN31 (1 % C, Cr)", "1.00", "ball bearings"),
            ("SS 304 (18/8)", "0.08", "food, kitchen"), ("SS 316 (16/10/2 Mo)", "0.08", "sea water, plant"))
    for i, (name, c, use) in enumerate(head):
        col, row = i % 2, i // 2
        x = 6 + col * 176
        y = 48 + row * 30
        b += poly([(x, y), (x + 168, y), (x + 168, y + 25), (x, y + 25)], THIN, 0.8, close=True,
                  fill="#FBFCFD" if row % 2 == 0 else "#F4F7FA")
        b += text(x + 6, y + 10, name, 7.0, anchor="start", weight="bold")
        b += text(x + 6, y + 20, f"{c} % C   {use}", 6.0, anchor="start", color=GREY)
    b += note_box(6, 206, 348, 58, "reading the designation",
                  ["C 45 = plain carbon steel with 0.45 % carbon, EN9 is the old BS name for the same",
                   "EN19 = 0.4 % C with chromium and molybdenum: through-hardenable, tough core",
                   "SS 304 = 18 % Cr, 8 % Ni, 0.08 % C: austenitic, non-magnetic, weldable"])
    b += foot(276, "The letter gives the family and the number gives the carbon in hundredths of a",
              "per cent; everything after that is the alloying element that does the special work.")
    return svg(W, 302, b)


# ---------------------------------------------------------------- 6 aluminium
def aluminium_series():
    b = heading("Aluminium: the eight series and what they are for", "wrought alloys, 1xxx to 8xxx")
    series = (("1xxx", "99 % Al", "foil, busbar", 110),
              ("2xxx", "Cu", "aircraft skin", 470),
              ("3xxx", "Mn", "cooking utensils", 130),
              ("4xxx", "Si", "brazing sheet", 170),
              ("5xxx", "Mg", "marine plate", 300),
              ("6xxx", "Mg + Si", "extrusion, frames", 310),
              ("7xxx", "Zn", "aircraft wing", 570),
              ("8xxx", "other", "bearings, foil", 200))
    for i, (code, element, use, uts) in enumerate(series):
        col, row = i % 2, i // 2
        x = 6 + col * 176
        y = 48 + row * 30
        b += poly([(x, y), (x + 168, y), (x + 168, y + 26), (x, y + 26)], ORANGE, 0.7, close=True,
                  fill="#FFF8EF")
        b += text(x + 6, y + 11, code, 7.6, anchor="start", weight="bold", color=ORANGE)
        b += text(x + 34, y + 11, element, 6.6, anchor="start")
        b += text(x + 34, y + 21, use, 5.8, anchor="start", color=GREY)
        b += poly([(x + 108, y + 15), (x + 108 + uts / 600 * 54, y + 15),
                   (x + 108 + uts / 600 * 54, y + 21), (x + 108, y + 21)], BLUE, 0.6, close=True,
                  fill="#C9DCF2")

    b += panel(6, 176, 168, 66)
    b += text(90, 190, "wrought alloys", 7.4, weight="bold", color=BLUE)
    b += text(90, 204, "rolled, forged, extruded", 6.0, color=GREY)
    b += text(90, 218, "1xxx - 8xxx, work hardened", 6.0, color=GREY)
    b += text(90, 232, "temper: O, H, T, F, W", 6.0, color=GREY)
    b += panel(186, 176, 168, 66)
    b += text(270, 190, "cast alloys", 7.4, weight="bold", color=PURPLE)
    b += text(270, 204, "sand, die, gravity cast", 6.0, color=GREY)
    b += text(270, 218, "LM6 (Al-Si 12): pistons", 6.0, color=GREY)
    b += text(270, 232, "A356-T6: wheels, housings", 6.0, color=GREY)

    b += text(180, 172, "bar length = tensile strength, 0 to 600 MPa", 6.0, color=GREY)
    b += note_box(6, 250, 348, 46, "why aluminium wins where weight matters",
                  ["density 2.70 against 7.85 for steel: the same part is 66 % lighter",
                   "pure aluminium 110 MPa, 7075-T6 570 MPa - alloying and ageing do the work"])
    b += foot(306, "Aluminium is the third most abundant element but it never occurs free: it is won",
              "from bauxite by electrolysis, which is why its price follows the price of electricity.")
    return svg(W, 330, b)


# ---------------------------------------------------------------- 7 metals against non-metals
def metals_vs_nonmetals():
    b = heading("Metals against non-metals", "the test is the free electron")
    b += panel(6, 46, 166, 150, fill="#EEF4FC")
    b += panel(188, 46, 166, 150, fill="#F6F1FB")
    b += text(89, 62, "METALS", 9.0, weight="bold", color=BLUE)
    b += text(271, 62, "NON-METALS", 9.0, weight="bold", color=PURPLE)
    left = ("free electrons", "conduct heat and current", "lustrous", "malleable and ductile",
            "sonorous", "melting point usually high", "opaque", "form cations, react with acids",
            "density high, 2.7 to 19")
    right = ("electrons held in bonds", "insulators, a few semiconductors", "no lustre, dull",
             "brittle, or soft as graphite", "no ring", "low or very high, no rule",
             "transparent or coloured", "form anions, react with alkalis", "density low, under 5")
    for i in range(len(left)):
        b += text(12, 80 + i * 12.5, "-", 7.2, anchor="start", color=BLUE)
        b += text(20, 80 + i * 12.5, left[i], 6.6, anchor="start")
        b += text(194, 80 + i * 12.5, "-", 7.2, anchor="start", color=PURPLE)
        b += text(202, 80 + i * 12.5, right[i], 6.6, anchor="start")
    b += note_box(6, 204, 348, 58, "the borderline cases worth knowing",
                  ["silicon and germanium are metalloids: shiny and brittle, and semiconductors",
                   "graphite is a non-metal that conducts - its electrons move within a layer",
                   "diamond, silicon carbide and alumina are non-metals harder than any steel"])
    b += foot(274, "Every difference in the two columns comes from one thing: whether the outer",
              "electrons are free to move through the solid. That is the definition to write first.")
    return svg(W, 300, b)


TITLES = {
    "u3_tree": "Classification of metals",
    "u3_carbon": "Carbon against strength and ductility",
    "u3_ci": "The four cast irons",
    "u3_cu": "Copper and its alloys",
    "u3_desig": "Steels a workshop orders",
    "u3_al": "Aluminium: the eight series",
    "u3_compare": "Metals against non-metals",
}

CAPTIONS = {
    "u3_tree": "Ferrous means iron-based: steel up to 2.14 % carbon and cast iron above it, split by "
               "the carbon content and the graphite shape. Non-ferrous means everything else, one "
               "base metal plus what is added to it.",
    "u3_carbon": "Raising carbon from 0.1 % to 1.2 % nearly doubles the tensile strength and cuts "
                 "the elongation from 30 % to 5 %; the best combination is in the middle.",
    "u3_ci": "All four cast irons hold more than 2 % carbon; what changes is the shape the carbon "
             "takes - flakes, cementite, temper carbon or nodules - and that shape decides the "
             "strength.",
    "u3_cu": "Zinc raises the strength of copper and destroys its conductivity at the same time, so "
             "electrical work uses copper and bearing work uses bronze.",
    "u3_desig": "A steel is ordered by its designation, and the number in the middle is the carbon in "
                "hundredths of a per cent.",
    "u3_al": "The aluminium series number says which element is the main alloying addition; a series "
             "7 zinc alloy reaches 570 MPa, more than twice what plain carbon steel gives at the same "
             "weight.",
    "u3_compare": "Metals and non-metals are separated by one property - whether the outer electrons "
                  "are free - and every other difference in the table follows from it.",
}

DIAGRAMS = {
    "u3_tree": metal_tree,
    "u3_carbon": carbon_strength,
    "u3_ci": cast_irons,
    "u3_cu": copper_alloys,
    "u3_desig": steel_designations,
    "u3_al": aluminium_series,
    "u3_compare": metals_vs_nonmetals,
}
