"""Seven figures for Engineering Materials Science (DI01000181) Unit 4 - non-metallic materials.

The numbers are the ones quoted in the notes: the service limits of the three families, the 1200 C to
50 C gradient through a 230 mm firebrick plus 115 mm insulating wall, the 968 W/m2 that gradient
carries, the dielectric strengths that decide how thick an insulator has to be, and the Mohs ladder
that says which mineral can cut which. Nothing is sketched by eye.
"""
import math

from diagrams_DI01000181_lib import (INK, GREY, THIN, BLUE, GREEN, ORANGE, RED, PURPLE, TEAL, W,
                                     AMBER, SKY, GLASS, STEEL, svg, text, ln, arrow, heading, foot,
                                     panel, note_box, lbl, leader, poly, curve, dots, axes, guide)


def _map(x0, y0, w, h, xlo, xhi, ylo, yhi):
    def mx(v):
        return x0 + (v - xlo) / (xhi - xlo) * w

    def my(v):
        return y0 + h - (v - ylo) / (yhi - ylo) * h

    return mx, my


# ---------------------------------------------------------------- 1 the four families
def family_tree():
    b = heading("Classification of non-metallic materials", "four families, and what each one is for")
    fams = (
        ("POLYMERS", BLUE, "#EEF4FC", ("thermoplastic: PE, PP, PVC, nylon", "thermoset: epoxy, bakelite, PU",
                                       "elastomer: natural, SBR, NBR")),
        ("CERAMICS", ORANGE, "#FFF6EC", ("traditional: brick, tile, cement", "advanced: alumina, SiC, Si3N4",
                                         "glass, porcelain, enamel")),
        ("COMPOSITES", TEAL, "#EAF4F2", ("FRP: glass or carbon in epoxy", "MMC: SiC particles in aluminium",
                                         "plywood, GRP tank, blade")),
        ("NATURAL AND ORGANIC", GREEN, "#EDF6EE", ("wood, cork, leather, cotton", "felt, paper, bitumen",
                                                   "gaskets, packing, damping")),
    )
    for i, (name, col, fill, lines) in enumerate(fams):
        px = 6 + (i % 2) * 176
        py = 46 + (i // 2) * 104
        b += panel(px, py, 172, 98, fill=fill)
        b += text(px + 86, py + 15, name, 8.0, weight="bold", color=col)
        for j, s in enumerate(lines):
            b += text(px + 86, py + 34 + j * 12, s, 6.5, color=INK)
        b += text(px + 86, py + 84, ("rubber, seals, tanks", "bricks, inserts, pots",
                                     "light panels, blades", "cheap, quiet, soft")[i], 6.2, color=GREY)

    b += note_box(6, 258, 348, 58, "why a machine needs a non-metal at all",
                  ["light and cheap and they do not rust: guards, tanks, handles, seals",
                   "they insulate - a busbar is useless without a porcelain support",
                   "they run quiet: nylon gears, rubber mounts, cork and felt gaskets"])
    b += foot(326, "Metals are strong and stiff; non-metals are light, insulating, quiet and cheap.",
              "A design that uses only metal is either noisy, heavy or dangerous to touch.")
    return svg(W, 348, b)


# ---------------------------------------------------------------- 2 vulcanisation
def vulcanisation():
    b = heading("Vulcanisation: what sulphur does to rubber", "raw gum against a cured compound")
    x0, y0, w, h = 44, 64, 268, 150
    mx, my = _map(x0, y0, w, h, 0, 700, 0, 25)
    b += axes(x0, y0, w, h, "", "stress, MPa", xticks=[(0, "0"), (200 / 700, "200"),
                                                      (400 / 700, "400"), (600 / 700, "600")],
              yticks=[(0, "0"), (10 / 25, "10"), (20 / 25, "20")], size=7.6)
    b += text(x0 + w - 4, y0 + h - 8, "elongation, %", 7.2, anchor="end", weight="bold")

    cured = [(0, 0), (100, 1.6), (200, 3.2), (300, 5.4), (400, 9.0), (500, 15.5), (560, 21.5)]
    gum = [(0, 0), (100, 0.9), (200, 1.5), (300, 2.0), (400, 2.4), (450, 2.1)]
    b += curve([(mx(x), my(y)) for x, y in cured], GREEN, 2.2)
    b += curve([(mx(x), my(y)) for x, y in gum], RED, 2.0, dash="4,3")
    b += ln(58, 72, 74, 72, GREEN, 2.2)
    b += text(78, 74, "vulcanised", 6.6, anchor="start", color=GREEN, weight="bold")
    b += ln(58, 84, 74, 84, RED, 2.0, "4,3")
    b += text(78, 86, "raw gum", 6.6, anchor="start", color=RED, weight="bold")

    b += note_box(6, 232, 348, 58, "the crosslink is the whole trick",
                  ["1 - 3 % sulphur at 140 - 160 C ties the chains together every few hundred atoms",
                   "cured: 22 MPa and 550 %; raw gum: 2 MPa and 450 % with no elastic return",
                   "Shore A 40 - 90: shoe sole 70, tyre tread 60, hard roller 90, soft gasket 45"])
    b += foot(300, "Rubber is the one material that can be strained 500 % and come back; the",
              "sulphur bridges stop the chains sliding past each other for good.")
    return svg(W, 322, b)


# ---------------------------------------------------------------- 3 service temperature
def service_temperature():
    b = heading("How hot each material family can work", "the bond sets the ceiling")
    rows = (("HDPE", 90, BLUE), ("natural rubber", 100, BLUE), ("epoxy resin", 150, BLUE),
            ("aluminium alloy", 200, ORANGE), ("plain carbon steel", 500, ORANGE),
            ("stainless steel 316", 800, ORANGE), ("alumina ceramic", 1500, TEAL),
            ("silicon carbide", 1600, TEAL))
    x0, top = 132, 58
    span = 208
    for i, (name, t, col) in enumerate(rows):
        yy = top + i * 19
        b += text(x0 - 6, yy + 4, name, 6.8, anchor="end")
        wid = t / 1700 * span
        b += poly([(x0, yy - 3.5), (x0 + wid, yy - 3.5), (x0 + wid, yy + 4.5), (x0, yy + 4.5)],
                  col, 0.7, close=True, fill={"#1565C0": "#DCEEFB", "#B66A00": "#F6E3C5",
                                              "#00695C": "#D8EDEA"}[col])
        b += text(x0 + wid + 5, yy + 4, f"{t} C", 6.4, anchor="start", color=GREY)
    b += text(x0, top + len(rows) * 19 + 2, "polymer", 6.4, anchor="start", color=BLUE, weight="bold")
    b += text(x0 + 52, top + len(rows) * 19 + 2, "metal", 6.4, anchor="start", color=ORANGE,
              weight="bold")
    b += text(x0 + 92, top + len(rows) * 19 + 2, "ceramic", 6.4, anchor="start", color=TEAL,
              weight="bold")

    b += note_box(6, 226, 348, 58, "why the order never changes",
                  ["van der Waals between chains, then metallic, then ionic and covalent: that is the order",
                   "a ceramic is hard because a dislocation cannot move in a rigid ionic lattice",
                   "and it is brittle for that same reason: a crack has nothing to blunt it"])
    b += foot(294, "A polymer above its ceiling softens or creeps, a metal above its ceiling oxidises",
              "and loses strength, a ceramic keeps its shape until it cracks without warning.")
    return svg(W, 314, b)


# ---------------------------------------------------------------- 4 three families compared
def three_families():
    b = heading("Metals, ceramics and polymers side by side", "eight properties, one answer for each")
    cols = (("property", 6, 74), ("METAL", 84, 84), ("CERAMIC", 172, 84), ("POLYMER", 260, 88))
    for name, cx, cw in cols:
        b += panel(cx, 46, cw, 16, fill="#EFF2F6")
        b += text(cx + cw / 2, 57, name, 6.8, weight="bold",
                  color={"property": INK, "METAL": ORANGE, "CERAMIC": TEAL, "POLYMER": BLUE}[name])
    rows = (
        ("bond", "metallic", "ionic, covalent", "van der Waals"),
        ("strength", "400 - 1200 MPa", "100 - 1000 MPa", "10 - 100 MPa"),
        ("ductility", "high", "none, it cracks", "high, low modulus"),
        ("ceiling", "500 - 1500 C", "1500 - 2000 C", "100 - 200 C"),
        ("density", "2.7 - 8.0", "2.5 - 4.0", "0.9 - 1.4"),
        ("current", "conducts", "insulates", "insulates"),
        ("k, W/mK", "15 - 400", "2 - 30", "0.1 - 0.5"),
        ("failure", "yields first", "fractures sharply", "creeps, softens"),
    )
    for i, row in enumerate(rows):
        yy = 76 + i * 15
        b += text(cols[0][1] + 4, yy, row[0], 6.4, anchor="start", weight="bold")
        for j in range(1, 4):
            b += text(cols[j][1] + 4, yy, row[j], 6.2, anchor="start", color=INK)
        if i < len(rows) - 1:
            b += ln(8, yy + 5, 346, yy + 5, "#E3E7EC", 0.7)

    b += note_box(6, 202, 348, 58, "choosing between them",
                  ["a polymer for a cover, a ceramic for a hot face, a metal for a load",
                   "the word for it is a hybrid: a glass tank, a steel frame, nylon bushes",
                   "the property you cannot change by design is the bond - choose the family first"])
    b += foot(270, "Every value in the table follows from the bond, so the table does not have to be",
              "memorised: derive it. Compare the ceiling, the density and the failure first.")
    return svg(W, 292, b)


# ---------------------------------------------------------------- 5 furnace wall
def furnace_wall():
    b = heading("A two-layer refractory wall", "1200 C outside-in, and where the drop happens")
    # wall section
    b += poly([(40, 48), (152, 48), (152, 98), (40, 98)], ORANGE, 1.0, close=True, fill="#F6E3C5")
    b += poly([(152, 48), (232, 48), (232, 98), (152, 98)], BLUE, 1.0, close=True, fill="#DCEEFB")
    b += poly([(232, 48), (240, 48), (240, 98), (232, 98)], INK, 1.0, close=True, fill="#BFC6CE")
    b += text(96, 66, "firebrick", 7.4, weight="bold", color=ORANGE)
    b += text(96, 79, "230 mm, k 1.0", 6.4, color=INK)
    b += text(192, 66, "insulation", 7.4, weight="bold", color=BLUE)
    b += text(192, 79, "115 mm, k 0.12", 6.4, color=INK)
    b += text(44, 94, "hot face 1200 C", 6.2, anchor="start", color=RED, weight="bold")
    b += text(246, 94, "50 C", 6.2, anchor="start", color=GREY, weight="bold")
    b += text(246, 66, "steel", 6.2, anchor="start", color=GREY)
    b += text(246, 77, "shell", 6.2, anchor="start", color=GREY)

    # temperature plot
    x0, y0, w, h = 40, 118, 200, 68
    mx, my = _map(x0, y0, w, h, 0, 200, 0, 1300)
    b += ln(x0, y0 + h, x0 + w, y0 + h, INK, 1.2)
    b += ln(x0, y0 - 6, x0, y0 + h, INK, 1.2)
    for t in (400, 800, 1200):
        b += guide(x0, my(t), x0 + w, my(t))
        b += text(x0 - 4, my(t) + 2.6, str(t), 6.2, anchor="end", color=GREY)
    b += curve([(mx(0), my(1200)), (mx(112), my(977))], RED, 2.2)
    b += curve([(mx(112), my(977)), (mx(192), my(50))], BLUE, 2.2)
    b += dots([(mx(0), my(1200)), (mx(112), my(977)), (mx(192), my(50))], INK, 1.8)
    b += text(mx(112) + 8, my(977) - 6, "977 C", 6.4, anchor="start", color=INK, weight="bold")
    b += text(x0 + w, y0 + h + 12, "thickness, mm", 6.6, anchor="end", color=INK, weight="bold")
    b += text(8, y0 - 12, "C", 6.8, anchor="start", color=INK, weight="bold")

    b += text(250, y0 + 6, "q = 1150 / 1.188", 6.6, anchor="start", weight="bold")
    b += text(250, y0 + 18, "= 968 W/m2", 6.6, anchor="start", color=BLUE)
    b += text(250, y0 + 34, "without the", 6.2, anchor="start", color=GREY)
    b += text(250, y0 + 44, "insulation:", 6.2, anchor="start", color=GREY)
    b += text(250, y0 + 56, "5000 W/m2", 6.4, anchor="start", color=RED, weight="bold")
    b += text(250, y0 + 68, "80 % saved", 6.4, anchor="start", color=GREEN, weight="bold")

    b += note_box(6, 206, 348, 68, "refractory families, and the slag rule",
                  ["acidic silica (SiO2) for glass tanks; basic magnesia and dolomite for steel ladles",
                   "neutral chromite and graphite where the slag swings either way",
                   "an acid brick against a basic slag is eaten in one campaign - match the slag",
                   "the working face must also resist spalling: heat cycles crack a dense brick"])
    b += foot(288, "The firebrick takes 223 C of the drop and the thin insulation layer takes 927 C:",
              "the cheaper material does the hot work, the thin one does the saving.")
    return svg(W, 310, b)


# ---------------------------------------------------------------- 6 dielectric strength
def dielectric_strength():
    b = heading("Dielectric strength and the thickness it needs", "breakdown voltage per mm")
    rows = (("air", 3.0, GREY), ("transformer oil", 12.0, BLUE), ("window glass", 14.0, BLUE),
            ("porcelain", 15.0, TEAL), ("bakelite", 18.0, ORANGE), ("epoxy resin", 20.0, ORANGE),
            ("PTFE", 24.0, PURPLE))
    x0, top, span = 104, 58, 200
    for i, (name, k, col) in enumerate(rows):
        yy = top + i * 19
        b += text(x0 - 6, yy + 4, name, 6.8, anchor="end")
        wid = k / 26 * span
        b += poly([(x0, yy - 3.5), (x0 + wid, yy - 3.5), (x0 + wid, yy + 4.5), (x0, yy + 4.5)],
                  col, 0.7, close=True, fill={"#666666": "#E9EDF1", "#1565C0": "#DCEEFB",
                                              "#00695C": "#D8EDEA", "#B66A00": "#F6E3C5",
                                              "#7B2CD9": "#EFE4FB"}[col])
        b += text(x0 + wid + 5, yy + 4, f"{k:.0f}", 6.4, anchor="start", color=GREY)
    b += text(x0 - 6, top + len(rows) * 19 + 4, "kV/mm", 6.4, anchor="end", color=GREY, weight="bold")

    b += note_box(6, 206, 348, 68, "an insulator is a material, not a gap",
                  ["an insulator is judged by resistivity above 1e8 ohm m and by this breakdown figure",
                   "thermal insulation is a different job: glass wool 0.04, aerogel 0.015 W/m K",
                   "porcelain outdoor: a long creepage path, and it dries itself when it wets",
                   "moisture, heat and time all lower the figure, so the test is done in kV/mm"])
    b += foot(288, "3 mm of bakelite at 18 kV/mm holds 54 kV; an 11 kV busbar with a factor of",
              "three needs 33 kV, so 2.75 mm - and 3 mm is what the drawing calls out.")
    return svg(W, 310, b)


# ---------------------------------------------------------------- 7 the Mohs ladder
def mohs_ladder():
    b = heading("The Mohs ladder, and which rung cuts what", "an abrasive must be harder than the work")
    names = ("talc", "gypsum", "calcite", "fluorite", "apatite", "feldspar", "quartz", "topaz",
             "corundum", "diamond")
    x0, span, yy = 26, 306, 96
    b += ln(x0, yy, x0 + span, yy, INK, 1.6)
    for i, name in enumerate(names):
        xx = x0 + i / 9 * span
        hot = i in (6, 8, 9)
        b += ln(xx, yy - 5, xx, yy + 5, INK, 1.4)
        b += text(xx, yy + 19, str(i + 1), 7.2, weight="bold", color=RED if hot else GREY)
        b += text(xx, yy + 31 if i % 2 == 0 else yy + 42, name, 6.0,
                  color=RED if hot else GREY)

    b += arrow(230, 69, 230, yy - 7, RED, 1.0, 4)
    b += text(230, 64, "7 quartz", 6.8, color=RED, weight="bold")
    b += arrow(297, 51, 297, yy - 7, RED, 1.0, 4)
    b += text(297, 46, "9 corundum", 6.8, color=RED, weight="bold")
    b += arrow(330, 69, 330, yy - 7, RED, 1.0, 4)
    b += text(356, 64, "10 diamond", 6.8, anchor="end", color=RED, weight="bold")

    b += note_box(6, 152, 348, 58, "the four abrasives a workshop actually buys",
                  ["natural: sandstone, emery (60 % alumina), corundum, diamond",
                   "synthetic: silicon carbide Knoop 2500, alumina 2100, CBN 4500, diamond 7000",
                   "bond: vitrified for a bench wheel, resinoid for a cut-off, paper for finishing"])
    b += note_box(6, 216, 348, 58, "grit number runs the other way from the grain",
                  ["coarse 8 - 24 for snagging castings; medium 30 - 60 for a general bench wheel",
                   "fine 80 - 180 for a cutting edge; 220 - 600 for lapping and a mirror finish",
                   "a harder wheel is used on soft work, a softer wheel on hard work - never the reverse"],
                  color=TEAL, fill="#EAF4F2")
    b += foot(288, "Abrasive, bond and grit are three separate choices: the grit cuts, the bond lets",
              "the dull grain fall out, and the abrasive decides what it can possibly cut.")
    return svg(W, 310, b)


TITLES = {
    "u4_tree": "Classification of non-metallic materials",
    "u4_rubber": "Vulcanisation of rubber",
    "u4_ceramic": "Service temperature of each family",
    "u4_compare": "Metals, ceramics and polymers compared",
    "u4_refract": "A two-layer refractory wall",
    "u4_insul": "Dielectric strength of insulators",
    "u4_abrasive": "The Mohs ladder and the abrasives",
}

CAPTIONS = {
    "u4_tree": "Polymers, ceramics, composites and natural materials: four families that a mechanical "
               "drawing uses for weight, insulation, quiet running and cost, not for strength.",
    "u4_rubber": "Sulphur bridges turn a soft gum that stretches and stays stretched into a rubber that "
                 "returns; the same 500 % elongation now comes back to zero.",
    "u4_ceramic": "The ceiling on service temperature runs with the bond: van der Waals forces in a "
                  "polymer, metallic bonds in a metal, ionic and covalent bonds in a ceramic.",
    "u4_compare": "Bond, strength, ductility, ceiling, density and failure mode - six questions asked of "
                  "all three families, so a choice is made from properties and not from habit.",
    "u4_refract": "1200 C at the hot face and 50 C at the shell, with 977 C at the joint: the firebrick "
                  "carries most of the temperature drop and the thin insulation layer saves 80 % of "
                  "the heat.",
    "u4_insul": "Dielectric strength decides the thickness: air is 3 kV/mm and PTFE is 24, so the same "
                "busbar needs a very different wall around it.",
    "u4_abrasive": "Quartz at 7, corundum at 9 and diamond at 10 on the Mohs scale, and the synthetic "
                   "abrasives placed between them by Knoop hardness.",
}

DIAGRAMS = {
    "u4_tree": family_tree,
    "u4_rubber": vulcanisation,
    "u4_ceramic": service_temperature,
    "u4_compare": three_families,
    "u4_refract": furnace_wall,
    "u4_insul": dielectric_strength,
    "u4_abrasive": mohs_ladder,
}
