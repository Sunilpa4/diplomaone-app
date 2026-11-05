"""Eight figures for Engineering Materials Science (DI01000181) Unit 1 - materials, bonds, crystals.

Every number on these figures is computed from the formula in the notes: the packing fractions are
pi*sqrt(3)/8 = 0.68 and pi/(3*sqrt(2)) = 0.74, the densities are n A/(N_A a^3), the specific
strengths are UTS/rho, and the tensile curve carries the standard mild-steel values (E 200 GPa,
yield 250 MPa, UTS 450 MPa, 25 % elongation). Nothing is drawn by eye.
"""
import math

from diagrams_DI01000181_lib import (INK, GREY, THIN, BLUE, GREEN, ORANGE, RED, PURPLE, TEAL, W,
                                     AMBER, SKY, GLASS, STEEL, svg, text, ln, arrow, heading, foot,
                                     panel, note_box, lbl, leader, poly, curve, dots, axes, guide,
                                     atom, electron, unit_cell, hcp_cell)

TITLES = {
    "u1_class": "Classification of engineering materials",
    "u1_select": "Choosing by strength per unit weight",
    "u1_bonds": "The five kinds of bond",
    "u1_bondenergy": "Bond strength decides the melting point",
    "u1_cells": "BCC, FCC and HCP unit cells",
    "u1_packing": "Packing fraction of the four structures",
    "u1_stress": "The tensile test and its properties",
    "u1_thermal": "Thermal and electrical properties",
}

CAPTIONS = {
    "u1_class": "Four families cover almost every machine part - metals, ceramics, polymers and "
                "composites; semiconductors and smart materials are the two modern additions.",
    "u1_select": "Plot tensile strength against density and the lines of constant strength per unit "
                 "weight appear: titanium and carbon fibre sit on much steeper lines than steel.",
    "u1_bonds": "Bonds differ only in where the electrons go - transferred, shared, donated by one "
                "atom, shared through a hydrogen bridge, or pooled in a metal.",
    "u1_bondenergy": "The stronger the bond, the more heat it takes to break it and the higher the "
                     "melting point: 20 kJ/mol for a hydrogen bond against 787 for rock salt.",
    "u1_cells": "BCC has two atoms per cell and 68 % packing, FCC four and HCP six with 74 % - which "
                "is why the close-packed metals are the ductile ones.",
    "u1_packing": "Simple cubic wastes 48 % of the space, BCC 32 % and the close-packed structures "
                  "only 26 %; the packing fraction is what sets the density.",
    "u1_stress": "A tensile test gives the modulus from the slope, the yield and ultimate strengths "
                 "from the two peaks, and ductility from how far the specimen stretches first.",
    "u1_thermal": "Metals conduct heat and current through the same free electrons: copper conducts "
                  "eight times better than steel and two thousand times better than rubber.",
}


def classification():
    b = heading("Classification of engineering materials", "four families, and two modern additions")
    cols = [(6, BLUE, "METALS", ["ferrous: steel,", "cast iron",
                                 "non-ferrous: Cu, Al,", "brass, bronze"]),
            (126, ORANGE, "CERAMICS", ["alumina, silicon", "carbide, refractories",
                                       "glass, cement", ""]),
            (246, GREEN, "POLYMERS", ["thermoplastic:", "PE, PVC, nylon",
                                      "thermoset:", "epoxy, bakelite"])]
    for x, col, name, lines in cols:
        b += panel(x, 46, 108, 92)
        b += text(x + 54, 62, name, 8.6, weight="bold", color=col)
        for i, line in enumerate([s for s in lines if s]):
            b += text(x + 54, 78 + 11 * i, line, 6.2, color=GREY)
    b += panel(66, 148, 228, 56)
    b += text(180, 164, "COMPOSITES", 8.6, weight="bold", color=PURPLE)
    b += text(180, 180, "fibre + matrix: CFRP, GFRP, MMC, cermet, plywood", 6.4, color=GREY)
    b += text(180, 194, "the fibre carries the load, the matrix holds and protects it", 6.2,
              color=GREY)
    b += note_box(6, 214, 348, 56, "the two modern additions",
                  ["semiconductors: silicon, germanium - conductivity between metal and insulator",
                   "smart materials: shape-memory alloy, piezoelectric, magnetostrictive",
                   "a part is chosen from a family by its property, then by cost and process"])
    b += foot(286, "The same part can be made from four different families: a gear may be steel,")
    b += foot(298, "sintered ceramic, nylon or a carbon composite - the duty decides which one.")
    return svg(W, 310, b)


def selection():
    b = heading("Choosing by strength per unit weight", "tensile strength against density")
    x0, y0, w, h = 54, 62, 268, 170
    b += axes(x0, y0, w, h, "density (g/cm3)", "UTS (MPa)",
              xticks=((0, "0"), (3 / 9, "3"), (6 / 9, "6"), (1, "9")),
              yticks=((0, "0"), (250 / 1000, "250"), (500 / 1000, "500"),
                      (750 / 1000, "750"), (1, "1000")))
    # iso-lines of constant specific strength, UTS = K x rho, K in MPa/(g/cm3) = kN m/kg
    for K in (50, 100, 200, 400):
        rho_end = min(9.0, 1000 / K)
        b += ln(x0, y0 + h, x0 + rho_end * w / 9,
                y0 + h - min(1000, K * rho_end) * h / 1000, THIN, 0.9, "4,3")
    mats = [("steel", 7.85, 450, BLUE, "end", -7, -6),
            ("stainless", 8.0, 600, BLUE, "end", -7, -6),
            ("al 6061", 2.70, 310, TEAL, "end", -8, -7),
            ("titanium", 4.43, 950, ORANGE, "start", 8, -6),
            ("CFRP", 1.60, 700, PURPLE, "start", 8, 11),
            ("nylon 66", 1.14, 80, GREEN, "start", 8, 3),
            ("wood", 0.70, 50, ORANGE, "end", -8, -7),
            ("alumina", 3.90, 300, RED, "start", 9, 12)]
    for name, rho, uts, col, anch, ddx, ddy in mats:
        px, py = x0 + rho * w / 9, y0 + h - uts * h / 1000
        b += f'<circle cx="{px:.1f}" cy="{py:.1f}" r="3.4" fill="{col}"/>'
        b += text(px + ddx, py + ddy, name, 6.4, anchor=anch, color=col)
    b += note_box(6, 268, 348, 56, "what the plot decides",
                  ["dashed lines: constant UTS/density, 50, 100, 200 and 400 kN m/kg",
                   "steel 57, aluminium 115, titanium 214, CFRP 438 kN m/kg",
                   "the same line is why an aircraft part is not made of steel"])
    b += foot(340, "A bicycle frame or an aircraft part moves to the upper left; a machine bed stays")
    b += foot(352, "with cast iron, where weight is an advantage and stiffness matters more.")
    return svg(W, 364, b)


def bonds():
    b = heading("The five kinds of bond", "where the electrons go decides everything else")
    specs = [(6, 44, 108, 124, BLUE, "ELECTROVALENT", "electron transferred"),
             (126, 44, 108, 124, GREEN, "COVALENT", "electrons shared"),
             (246, 44, 108, 124, ORANGE, "COORDINATE", "one atom donates both")]
    for x, y, w, h, col, name, sub in specs:
        b += panel(x, y, w, h)
        b += text(x + w / 2, y + 15, name, 7.2, weight="bold", color=col)
        b += text(x + w / 2, y + 26, sub, 6.2, color=GREY)
    # electrovalent: Na gives one electron to Cl
    b += atom(38, 92, 10, "Na", INK, "#FFF2E0")
    b += atom(84, 92, 12, "Cl", INK, "#E8F1FE")
    b += electron(62, 106, 2.4)
    b += arrow(56, 106, 74, 106, RED, 1.1, 4)
    b += text(38, 116, "Na+", 6.6, color=RED)
    b += text(84, 118, "Cl-", 6.6, color=BLUE)
    b += text(60, 142, "ions held by attraction", 6.0, color=GREY)
    b += text(60, 152, "hard, brittle, soluble", 6.0, color=GREY)
    # covalent: two atoms share a pair
    b += atom(152, 92, 11, None, INK, "#EAF6EC")
    b += atom(188, 92, 11, None, INK, "#EAF6EC")
    b += electron(166, 88, 2.2, GREEN) + electron(174, 96, 2.2, GREEN)
    b += text(170, 116, "H - H, C - C, Si - O", 6.0, color=GREY)
    b += text(170, 142, "strong, directional,", 6.0, color=GREY)
    b += text(170, 152, "hard, high melting", 6.0, color=GREY)
    # coordinate: one atom donates both electrons
    b += atom(272, 92, 11, "N", INK, "#FFF3E3")
    b += atom(308, 92, 11, "B", INK, "#FFF3E3")
    b += electron(284, 88, 2.2, ORANGE) + electron(284, 96, 2.2, ORANGE)
    b += arrow(288, 92, 297, 92, ORANGE, 1.1, 4)
    b += text(290, 116, "NH3 -> BF3", 6.0, color=GREY)
    b += text(290, 142, "both electrons from", 6.0, color=GREY)
    b += text(290, 152, "the same atom", 6.0, color=GREY)
    # hydrogen bond: two water molecules bridged
    b += panel(66, 176, 108, 124, "none")
    b += text(120, 191, "HYDROGEN", 7.2, weight="bold", color=PURPLE)
    b += text(120, 202, "a bridge between molecules", 6.2, color=GREY)
    for hx in (96, 150):
        b += atom(hx, 226, 9, "O", INK, "#EDE7FB")
        b += atom(hx - 12, 212, 5, "H", INK, "#FFFFFF")
        b += atom(hx + 12, 212, 5, "H", INK, "#FFFFFF")
    b += ln(105, 226, 141, 226, PURPLE, 1.6, "2,2")
    b += text(120, 248, "O - H ... O", 6.4, color=PURPLE)
    b += text(120, 264, "weak, 20 kJ/mol", 6.0, color=GREY)
    b += text(120, 275, "ice, water, DNA", 6.0, color=GREY)
    # metallic: ion cores in an electron sea
    b += panel(192, 176, 108, 124, "none")
    b += text(246, 191, "METALLIC", 7.2, weight="bold", color=TEAL)
    b += text(246, 202, "electrons pooled", 6.2, color=GREY)
    b += f'<rect x="204" y="212" width="84" height="52" rx="4" fill="#E6F2F1" stroke="{TEAL}" ' \
         f'stroke-width="1"/>'
    for i in range(4):
        for j in range(2):
            b += atom(218 + i * 18, 226 + j * 22, 6, "+", TEAL, "#D6EAE8", 6.0)
    for i in range(14):
        b += electron(209 + (i * 23) % 76, 216 + (i * 17) % 44, 1.7, BLUE)
    b += text(246, 276, "free electrons give", 6.0, color=GREY)
    b += text(246, 287, "conduction and ductility", 6.0, color=GREY)
    b += foot(320, "Read the group in one line: transferred gives brittle salts, shared gives hard")
    b += foot(332, "solids, pooled gives workable metals, and hydrogen gives low melting points.")
    return svg(W, 344, b)


def bond_energy():
    b = heading("Bond strength decides the melting point", "bond energy in kJ per mole")
    base, top = 196, 88
    b += ln(66, base, 344, base, INK, 1.3)
    b += ln(66, base, 66, top, INK, 1.3)
    b += text(66, top - 10, "kJ/mol", 7.2, anchor="start", weight="bold")
    for val in (0, 250, 500, 750):
        yy = base - val / 850 * 100
        b += ln(61, yy, 66, yy, INK, 1.0)
        b += text(57, yy + 2.6, str(val), 6.4, anchor="end", color=GREY)
    data = [("H-bond", 20, "0 C ice", PURPLE),
            ("C - C", 348, "3650 C", GREEN),
            ("Fe - Fe", 415, "1538 C", BLUE),
            ("NaCl", 787, "801 C", ORANGE)]
    for i, (name, val, mp, col) in enumerate(data):
        x = 86 + i * 62
        hh = val / 850 * 100
        b += f'<rect x="{x}" y="{base - hh:.1f}" width="40" height="{hh:.1f}" rx="2" ' \
             f'fill="{col}" fill-opacity="0.28" stroke="{col}" stroke-width="1.3"/>'
        b += text(x + 20, base - hh - 13, str(val), 7.2, weight="bold", color=col)
        b += text(x + 20, base - hh - 4, mp, 5.8, color=GREY)
        b += text(x + 20, base + 12, name, 6.6, color=INK)
    b += note_box(6, 220, 348, 52, "the rule in one line",
                  ["melting point rises with bond energy: 20, 348, 415, 787 kJ/mol",
                   "ice melts at 0 C, iron at 1538 C, rock salt at 801 C",
                   "but a strong ionic bond gives no impact resistance: salt is brittle"])
    b += foot(292, "The C - C bar belongs to graphite, which sublimes near 3650 C rather than")
    b += foot(304, "melting. Compare like with like: bond energy is only one consequence.")
    return svg(W, 316, b)


def cells():
    b = heading("BCC, FCC and HCP unit cells", "two, four and six atoms per cell")
    b += unit_cell(14, 82, 70, "bcc", INK, BLUE)
    b += unit_cell(128, 82, 70, "fcc", INK, GREEN)
    b += hcp_cell(292, 118, 36, INK, ORANGE)
    b += text(58, 188, "BCC", 8.4, weight="bold", color=BLUE)
    b += text(58, 200, "2 atoms, CN 8", 6.4, color=INK)
    b += text(58, 211, "APF 0.68", 6.4, color=INK)
    b += text(58, 222, "Fe-alpha, Cr, W", 6.2, color=GREY)
    b += text(172, 188, "FCC", 8.4, weight="bold", color=GREEN)
    b += text(172, 200, "4 atoms, CN 12", 6.4, color=INK)
    b += text(172, 211, "APF 0.74", 6.4, color=INK)
    b += text(172, 222, "Cu, Al, Ni, Fe-gamma", 6.2, color=GREY)
    b += text(292, 188, "HCP", 8.4, weight="bold", color=ORANGE)
    b += text(292, 200, "6 atoms, CN 12", 6.4, color=INK)
    b += text(292, 211, "APF 0.74, c/a 1.633", 6.2, color=INK)
    b += text(292, 222, "Mg, Zn, Ti, Cd", 6.2, color=GREY)
    b += note_box(6, 234, 348, 52, "why the numbers matter",
                  ["a corner atom is shared by 8 cells, a face atom by 2, so count fractions",
                   "BCC: 8 x 1/8 + 1 = 2;  FCC: 8 x 1/8 + 6 x 1/2 = 4",
                   "FCC and HCP are close packed: 12 neighbours, 74 % of the space filled"])
    b += foot(304, "Iron is BCC below 912 C and FCC between 912 and 1394 C; that change of cell")
    b += foot(316, "is what makes steel hardenable, because FCC iron dissolves 2 % carbon.")
    return svg(W, 328, b)


def packing():
    b = heading("Packing fraction of the four structures", "fraction of the cell filled by atoms")
    base = 196
    b += ln(62, base, 344, base, INK, 1.3)
    b += ln(62, base, 62, 84, INK, 1.3)
    b += text(62, 76, "APF", 7.2, anchor="start", weight="bold")
    for frac in (0, 0.5, 1.0):
        yy = base - frac * 100
        b += ln(57, yy, 62, yy, INK, 1.0)
        b += text(53, yy + 2.6, f"{frac:.1f}", 6.6, anchor="end", color=GREY)
    data = [("SC", 0.5236, "polonium only", GREY),
            ("BCC", 0.6802, "Fe-alpha, Cr", BLUE),
            ("FCC", 0.7405, "Cu, Al, Ni", GREEN),
            ("HCP", 0.7405, "Mg, Zn, Ti", ORANGE)]
    for i, (name, apf, ex, col) in enumerate(data):
        x = 80 + i * 66
        hh = apf * 100
        b += f'<rect x="{x}" y="{base - hh:.1f}" width="44" height="{hh:.1f}" rx="2" ' \
             f'fill="{col}" fill-opacity="0.28" stroke="{col}" stroke-width="1.3"/>'
        b += text(x + 22, base - hh - 8, f"{apf:.2f}", 7.4, weight="bold", color=col)
        b += text(x + 22, base + 13, name, 7.6, weight="bold", color=INK)
        b += text(x + 22, base + 24, ex, 5.9, color=GREY)
    b += note_box(6, 236, 348, 52, "where the numbers come from",
                  ["BCC: a = 4R/sqrt(3), n = 2 -> APF = pi sqrt(3)/8 = 0.68",
                   "FCC: a = 2 sqrt(2) R, n = 4 -> APF = pi/(3 sqrt(2)) = 0.74",
                   "HCP: c/a = 1.633, n = 6 -> the same 0.74, the close-packed value"])
    b += foot(308, "Denser packing means a higher density and less empty space for carbon to sit in -")
    b += foot(320, "the reason FCC iron dissolves more carbon than BCC iron.")
    return svg(W, 330, b)


def stress():
    b = heading("The tensile test and its properties", "stress against strain for mild steel")
    x0, y0, w, h = 58, 74, 232, 150
    b += axes(x0, y0, w, h, "strain (%)", "stress (MPa)",
              xticks=((0, "0"), (0.2, "5"), (0.4, "10"), (0.6, "15"), (0.8, "20"), (1, "25")),
              yticks=((0, "0"), (0.25, "150"), (0.5, "300"), (0.75, "450"), (1, "600")))
    px = lambda s: x0 + s * w          # noqa: E731  strain in % of 25
    py = lambda sg: y0 + h - sg / 600 * h   # noqa: E731  stress in MPa

    # curve: elastic line (drawn steep and flagged as exaggerated), yield plateau,
    # strain hardening to the UTS at 15 %, then necking to fracture at 25 %
    pts = [(px(0), py(0))]
    pts.append((px(0.032), py(250)))
    pts.append((px(0.08), py(250)))
    for i in range(1, 26):
        t = i / 25
        pts.append((px(0.08 + 0.52 * t), py(250 + 200 * math.sin(math.pi * t / 2))))
    for i in range(1, 21):
        t = i / 20
        pts.append((px(0.60 + 0.40 * t), py(450 - 300 * t ** 1.7)))
    b += f'<polygon points="{pts[0][0]:.1f},{py(0):.1f} ' + \
         " ".join(f"{a:.1f},{c:.1f}" for a, c in pts) + \
         f' {pts[-1][0]:.1f},{py(0):.1f}" fill="{BLUE}" fill-opacity="0.10"/>'
    b += curve(pts, BLUE, 2.0)
    marks = [(px(0.032), py(250), "yield 250 MPa", "start", 6, 12),
             (px(0.60), py(450), "UTS 450 MPa", "end", -4, -9),
             (px(1.0), py(150), "fracture", "end", -6, -6)]
    for mx, my, lab, anch, ddx, ddy in marks:
        b += f'<circle cx="{mx:.1f}" cy="{my:.1f}" r="2.8" fill="{RED}"/>'
        b += text(mx + ddx, my + ddy, lab, 6.6, anchor=anch, color=RED)
    b += text(px(0.075), py(196), "slope = E", 6.4, color=BLUE)
    b += text(px(0.02), py(560), "elastic part drawn", 5.8, anchor="start", color=GREY)
    b += text(px(0.02), py(515), "wider than scale", 5.8, anchor="start", color=GREY)
    b += text(px(0.86), py(520), "toughness", 6.2, anchor="end", color=GREY)
    b += text(px(0.86), py(478), "= shaded area", 6.2, anchor="end", color=GREY)
    b += note_box(6, 244, 348, 52, "what each point is used for",
                  ["E = 200 GPa from the slope; yield 250 MPa decides the allowable stress",
                   "UTS 450 MPa is the highest stress, not a safe working stress",
                   "elongation 25 % and reduction in area 55 % measure the ductility"])
    b += foot(312, "A brittle material such as cast iron has almost no plastic part: the curve stops")
    b += foot(324, "just after the straight line, which is why it is never loaded near its UTS.")
    return svg(W, 336, b)


def thermal():
    b = heading("Thermal and electrical properties", "why copper cools and rubber insulates")
    base, top = 190, 84
    b += ln(78, base, 344, base, INK, 1.3)
    b += ln(78, base, 78, top, INK, 1.3)
    b += text(78, top - 10, "W/(m K)", 7.2, anchor="start", weight="bold")
    b += text(344, top - 10, "log scale", 6.2, anchor="end", color=GREY)

    def bar_h(v):
        return math.log10(v / 0.1 + 1) / math.log10(385 / 0.1 + 1) * 96

    for val, lab in ((1, "1"), (10, "10"), (100, "100")):
        yy = base - bar_h(val)
        b += ln(73, yy, 78, yy, INK, 1.0)
        b += text(69, yy + 2.6, lab, 6.2, anchor="end", color=GREY)
    data = [("copper", 385, BLUE), ("aluminium", 205, TEAL), ("steel", 50, GREY),
            ("stainless", 16, ORANGE), ("glass", 1.0, GREEN), ("rubber", 0.15, RED)]
    for i, (name, val, col) in enumerate(data):
        x = 86 + i * 43
        hh = bar_h(val)
        b += f'<rect x="{x}" y="{base - hh:.1f}" width="30" height="{hh:.1f}" rx="2" ' \
             f'fill="{col}" fill-opacity="0.30" stroke="{col}" stroke-width="1.3"/>'
        b += text(x + 15, base - hh - 7, f"{val:g}", 6.6, weight="bold", color=col)
        b += text(x + 15, base + 13, name, 6.0, color=INK)
    b += note_box(6, 214, 348, 54, "the numbers a designer carries in his head",
                  ["thermal conductivity: copper 385, aluminium 205, steel 50 W/(m K)",
                   "electrical resistivity: copper 1.7e-8, aluminium 2.8e-8, iron 1.0e-7 ohm m",
                   "thermal expansion: steel 12e-6, aluminium 23e-6, invar 1.2e-6 per K"])
    b += foot(288, "The same free electrons carry heat and current, so the two lists run in the same")
    b += foot(300, "order. A busbar is aluminium when weight matters, copper when space matters.")
    return svg(W, 312, b)


DIAGRAMS = {
    "u1_class": classification,
    "u1_select": selection,
    "u1_bonds": bonds,
    "u1_bondenergy": bond_energy,
    "u1_cells": cells,
    "u1_packing": packing,
    "u1_stress": stress,
    "u1_thermal": thermal,
}
