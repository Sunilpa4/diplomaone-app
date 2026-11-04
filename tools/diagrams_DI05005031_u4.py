"""Nine figures for Chemical Reaction Engineering (DI05005031) Unit 4 - the reactors themselves.

Each equipment figure is drawn part by part (shell, jacket, impeller, baffles, distributor, packing,
overflow, cyclone ...) so that a student can name every part, and each carries the working note that
matters for that reactor. The three-panel figure at the top of the set fixes the ideal mixing models
that every later design equation is written against."""
import math

from diagrams_DI05005031_lib import (INK, GREY, THIN, BLUE, GREEN, ORANGE, RED, PURPLE, TEAL, W,
                                     AMBER, SKY, GLASS, svg, text, ln, arrow, heading, foot, panel,
                                     box, note_box, vessel, liquid, jacket, hatch_band, shaft, motor,
                                     impeller, baffle, distributor, bubbles, packing, droplets,
                                     spray_cone, pump, valve, bubble_glass, lbl, leader, curve,
                                     dots, axes, guide)

TITLES = {
    "u4_models": "The three ideal mixing models",
    "u4_batch": "The batch reactor, part by part",
    "u4_semibatch": "The semi-batch reactor",
    "u4_cstr": "The CSTR (mixed flow reactor)",
    "u4_pfr": "The tubular reactor (plug flow)",
    "u4_fixed": "The fixed bed reactor",
    "u4_fluidised": "The fluidised bed reactor",
    "u4_slurry": "Slurry and bubble column reactors",
    "u4_spray": "Spray tower and trickle bed",
}

CAPTIONS = {
    "u4_models": "Batch: no flow, one composition. CSTR: flow, and the outlet is the same as the "
                 "contents. PFR: flow, and the composition slides along the tube with no back-mixing.",
    "u4_batch": "A stirred tank with a jacket and a drain: everything goes in at the start, nothing "
                "leaves until the end, and the whole batch sees the same composition.",
    "u4_semibatch": "One reactant is fed into the other at a controlled rate, so its concentration "
                    "can be held low - the standard way to control a fast or exothermic reaction.",
    "u4_cstr": "Feed in, product out through the overflow, and an impeller fast enough that the "
               "outlet composition equals the composition everywhere inside.",
    "u4_pfr": "A tube with no back-mixing: every fluid element spends the same time inside, and the "
              "concentration falls along the length like a batch reactor in time.",
    "u4_fixed": "Catalyst pellets sit between a distributor and a support grid; the gas or liquid "
                "threads through the voids, so pressure drop and hot spots are the design worries.",
    "u4_fluidised": "The gas enters through a distributor fast enough to lift the particles: the bed "
                    "behaves like a boiling liquid, which carries heat beautifully and back-mixes badly.",
    "u4_slurry": "Gas bubbles through a liquid that holds the catalyst: the bubble column has no "
                 "moving parts, the slurry reactor adds a stirrer to keep the solids suspended.",
    "u4_spray": "Liquid falls as drops or as a film over packing while gas rises: the spray tower "
                "gives the gas a huge contact area, the trickle bed keeps the catalyst wetted.",
}


# ------------------------------------------------------------------ 1. ideal mixing models
def models():
    b = heading("Three ideal pictures of a reactor", "what each model assumes about mixing")
    cols = [(6, BLUE, "BATCH", "no flow, uniform"),
            (126, GREEN, "CSTR", "flow, perfect mixing"),
            (246, ORANGE, "PFR", "flow, no back-mixing")]
    for x, color, name, sub in cols:
        b += panel(x, 48, 108, 132)
        b += text(x + 54, 64, name, 9.0, weight="bold", color=color)
        b += text(x + 54, 76, sub, 7.2, color=GREY)
    # batch: a tank with a stirrer, nothing crossing the wall
    b += vessel(36, 84, 48, 54, INK, 1.5, GLASS, rx=4)
    b += liquid(36, 84, 48, 54, 96, SKY, BLUE)
    b += shaft(60, 84, 122, INK, 1.6)
    b += impeller(60, 120, 13, INK, 4)
    b += text(60, 106, "same", 6.4, color=PURPLE, weight="bold")
    b += text(60, 114, "everywhere", 6.4, color=PURPLE, weight="bold")
    b += text(60, 152, "t is the variable", 7.0, color=INK)
    # CSTR: in on the left, out on the right, strong swirl
    b += vessel(144, 84, 56, 54, INK, 1.5, GLASS, rx=4)
    b += liquid(144, 84, 56, 54, 94, SKY, BLUE)
    b += arrow(126, 96, 143, 96, INK, 1.3)
    b += arrow(201, 128, 222, 128, INK, 1.3)
    b += shaft(172, 84, 124, INK, 1.6)
    b += impeller(172, 122, 15, INK, 4)
    b += curve([(150, 112), (158, 104), (172, 108), (186, 104), (194, 112)], PURPLE, 1.2)
    b += text(172, 152, "out = inside", 7.0, color=INK)
    # PFR: a tube with a shading that deepens along the length
    b += f'<rect x="252" y="92" width="96" height="30" rx="6" fill="{GLASS}" stroke="{INK}" ' \
         f'stroke-width="1.5"/>'
    b += arrow(250, 107, 262, 107, INK, 1.3)
    b += arrow(338, 107, 350, 107, INK, 1.3)
    for i, (xx, col) in enumerate([(268, "#CFE7FB"), (288, "#9FCBF4"), (308, "#6BA9E8"),
                                  (328, "#3D7FC0")]):
        b += f'<circle cx="{xx}" cy="107" r="6.5" fill="{col}" stroke="{BLUE}" stroke-width="0.7"/>'
    b += text(300, 152, "changes along z", 7.0, color=INK)
    b += note_box(6, 190, 348, 44, "the assumption that makes each model solvable",
                  ["batch and CSTR: composition is the same at every point (perfect mixing)",
                   "PFR: no mixing in the flow direction, perfect mixing across the tube"], PURPLE,
                  "#F5EEFD")
    b += foot(250, "Every design equation of Unit 5 is written for one of these three pictures; the")
    b += foot(262, "real reactor is then judged by how far it sits from the picture chosen for it.")
    return svg(W, 274, b)


# ------------------------------------------------------------------ 2. batch reactor
def batch():
    b = heading("The batch reactor, part by part", "a stirred tank that is filled, run and emptied")
    # shell, jacket, internals
    b += vessel(120, 100, 120, 150, INK, 2.0, GLASS, rx=6)
    b += liquid(120, 100, 120, 150, 118, SKY, BLUE)
    b += jacket(120, 100, 120, 150, TEAL, 1.2)
    b += ln(113, 108, 113, 242, TEAL, 0.6)
    b += ln(247, 108, 247, 242, TEAL, 0.6)
    b += motor(180, 84, 26, 14)
    b += shaft(180, 92, 214, INK, 2.2)
    b += impeller(180, 218, 24, INK, 4)
    b += baffle(132, 112, 240, INK)
    b += baffle(228, 112, 240, INK)
    # charge nozzle on the top head
    b += f'<rect x="132" y="93" width="14" height="8" rx="2" fill="#fff" stroke="{INK}" ' \
         f'stroke-width="1.1"/>'
    # thermometer pocket and sight glass on the right wall
    b += f'<rect x="236" y="130" width="7" height="46" rx="3" fill="#fff" stroke="{INK}" ' \
         f'stroke-width="1.0"/>'
    b += f'<circle cx="239.5" cy="174" r="3.0" fill="{RED}"/>'
    b += bubble_glass(236, 186, 9, 26)
    # bottom outlet and drain valve
    b += ln(180, 250, 180, 260, INK, 1.8)
    b += valve(180, 264, 5.0)
    b += ln(180, 269, 180, 274, INK, 1.4)
    b += text(126, 112, "liquid level", 6.8, anchor="start", color=GREY)
    # left-hand labels
    for ly, tx, ty, name in [(104, 132, 96, "charge nozzle"),
                             (136, 180, 150, "motor drive and shaft"),
                             (168, 132, 168, "baffles: stop the swirl"),
                             (222, 158, 218, "turbine impeller"),
                             (246, 113, 226, "cooling-water jacket")]:
        b += leader(tx, ty, 100, ly - 3.5, THIN)
        b += text(6, ly, name, 7.2, anchor="start", color=INK)
    # right-hand labels
    for ly, tx, ty, name in [(124, 243, 130, "thermometer pocket"),
                             (200, 245, 199, "sight glass"),
                             (268, 186, 264, "drain valve")]:
        b += leader(tx, ty, 254, ly - 3.5, THIN)
        b += text(254, ly, name, 7.2, anchor="start", color=INK)
    b += foot(292, "Working: charge both reactants, start the stirrer and the jacket, run for the")
    b += foot(304, "calculated time, then empty through the bottom valve and clean the tank.")
    return svg(W, 316, b)


# ------------------------------------------------------------------ 3. semi-batch
def semibatch():
    b = heading("The semi-batch reactor", "one reactant is fed into the other while it reacts")
    # vessel and internals
    b += vessel(168, 92, 112, 148, INK, 2.0, GLASS, rx=6)
    b += liquid(168, 92, 112, 148, 124, SKY, BLUE)
    b += jacket(168, 92, 112, 148, TEAL, 1.2)
    b += motor(224, 64, 24, 13)
    b += shaft(224, 71, 230, INK, 2.0)
    b += impeller(224, 226, 22, INK, 4)
    b += baffle(180, 104, 232, INK)
    b += baffle(268, 104, 232, INK)
    # feed train: tank -> pump -> control valve -> over the top -> dip tube
    b += f'<rect x="12" y="120" width="40" height="34" rx="4" fill="{GLASS}" stroke="{INK}" ' \
         f'stroke-width="1.4"/>'
    b += liquid(12, 120, 40, 34, 134, SKY, BLUE)
    b += ln(52, 137, 64, 137, INK, 1.5)
    b += pump(72, 137, 8)
    b += ln(80, 137, 96, 137, INK, 1.5)
    b += valve(104, 137, 4.6)
    b += ln(112, 137, 120, 137, INK, 1.5)
    b += ln(120, 137, 120, 80, INK, 1.5)
    b += ln(120, 80, 196, 80, INK, 1.5)
    b += arrow(196, 80, 196, 210, INK, 1.4)
    # labels under the feed train
    b += text(12, 186, "feed tank", 7.2, anchor="start", color=INK)
    b += leader(32, 154, 32, 178, THIN)
    b += leader(104, 133, 104, 124, THIN)
    b += text(104, 120, "control valve", 7.2, anchor="middle", color=INK)
    b += leader(72, 146, 72, 156, THIN)
    b += text(72, 166, "pump", 7.2, anchor="middle", color=INK)
    # dip tube and jacket labels on the right
    b += leader(196, 190, 150, 190, THIN)
    b += text(146, 190, "dip tube", 7.2, anchor="end", color=INK)
    b += text(292, 150, "jacket:", 7.2, anchor="start", color=TEAL)
    b += text(292, 162, "cooling water", 7.2, anchor="start", color=TEAL)
    b += leader(287, 148, 290, 148, THIN)
    b += arrow(252, 216, 252, 186, GREY, 1.1, 4)
    b += text(252, 180, "level", 6.6, color=GREY)
    b += note_box(6, 258, 348, 42, "why feed one reactant instead of charging both",
                  ["the fed reactant never builds up, so a fast or exothermic reaction stays tame",
                   "its low concentration also favours the wanted product over a side reaction"],
                  PURPLE, "#F5EEFD")
    b += foot(316, "Working: charge A, bring it to temperature, then start the feed and the stirrer")
    b += foot(328, "together, hold the feed rate, stop when the dose is in and let the batch finish.")
    return svg(W, 340, b)


# ------------------------------------------------------------------ 4. CSTR
def cstr():
    b = heading("The CSTR (mixed flow reactor)", "feed in, product out, one composition inside")
    b += vessel(118, 100, 122, 144, INK, 2.0, GLASS, rx=6)
    b += liquid(118, 100, 122, 144, 124, SKY, BLUE)
    b += jacket(118, 100, 122, 144, TEAL, 1.2)
    b += motor(179, 72, 26, 14)
    b += shaft(179, 79, 234, INK, 2.2)
    b += impeller(179, 230, 24, INK, 4)
    b += baffle(130, 112, 238, INK)
    b += baffle(228, 112, 238, INK)
    # feed line with pump, and the overflow outlet at the liquid level
    b += ln(8, 168, 74, 168, INK, 1.5)
    b += pump(82, 168, 8)
    b += ln(90, 168, 116, 168, INK, 1.5)
    b += arrow(112, 168, 117, 168, INK, 1.3)
    b += ln(240, 132, 272, 132, INK, 1.5)
    b += arrow(268, 132, 273, 132, INK, 1.3)
    b += text(10, 156, "feed A + B", 7.2, anchor="start", color=INK)
    b += leader(82, 177, 82, 186, THIN)
    b += text(82, 196, "pump", 7.2, anchor="middle", color=INK)
    b += text(276, 132, "overflow", 7.2, anchor="start", color=INK)
    b += text(276, 144, "level fixed", 6.8, anchor="start", color=GREY)
    # internals on the left
    for ly, tx, ty, name in [(130, 130, 130, "baffles"),
                             (230, 158, 230, "impeller"),
                             (232, 113, 232, "jacket")]:
        b += leader(tx, ty, 100, ly - 3.5, THIN)
        b += text(6, ly, name, 7.2, anchor="start", color=INK)
    b += text(179, 112, "same composition", 6.8, color=PURPLE)
    b += note_box(6, 262, 348, 30, "the model in one line",
                  ["outlet concentration = concentration inside = feed concentration after reaction"])
    b += foot(310, "Working: feed and product leave continuously, so the reactor runs at one")
    b += foot(322, "composition; the stirrer must beat the feed, so mixing time << space time.")
    return svg(W, 334, b)


# ------------------------------------------------------------------ 5. PFR
def pfr():
    b = heading("The tubular reactor (plug flow)", "no back-mixing: composition slides along the tube")
    # jacket shell around the tube
    b += ln(44, 106, 316, 106, TEAL, 1.3)
    b += ln(44, 168, 316, 168, TEAL, 1.3)
    b += ln(50, 106, 50, 88, TEAL, 1.3)
    b += arrow(50, 94, 50, 86, TEAL, 1.2)
    b += ln(310, 168, 310, 186, TEAL, 1.3)
    b += arrow(310, 180, 310, 188, TEAL, 1.2)
    b += text(56, 84, "coolant out", 6.8, anchor="start", color=TEAL)
    b += text(304, 200, "coolant in", 6.8, anchor="end", color=TEAL)
    # the tube itself with the reacting plug
    b += f'<rect x="44" y="116" width="272" height="42" rx="8" fill="{GLASS}" stroke="{INK}" ' \
         f'stroke-width="2.0"/>'
    b += arrow(8, 137, 42, 137, INK, 1.5)
    b += arrow(318, 137, 348, 137, INK, 1.5)
    for xx, col in [(62, "#D8ECFC"), (96, "#AFD3F5"), (130, "#86B9EC"), (164, "#5F9DDE"),
                    (198, "#3F82C8"), (232, "#2C69AC"), (266, "#1E5290"), (300, "#173F70")]:
        b += f'<circle cx="{xx}" cy="137" r="8" fill="{col}" stroke="{BLUE}" stroke-width="0.7"/>'
    b += text(8, 126, "feed", 7.2, anchor="start", color=INK)
    b += text(348, 126, "product", 7.2, anchor="end", color=INK)
    b += text(180, 184, "jacket around the tube", 7.2, color=INK)
    b += text(180, 100, "the plug: one colour deepens as A is used up", 6.8, color=PURPLE)
    # concentration profile along the length
    b += axes(60, 210, 232, 54, "length z", "CA", xticks=(), yticks=())
    pts = [(60 + i * 6, 214 + 46 * (1 - math.exp(-2.2 * i / 38))) for i in range(39)]
    b += curve(pts, BLUE, 2.0)
    b += text(300, 232, "steep at first,", 6.8, anchor="end", color=GREY)
    b += text(300, 244, "then flat", 6.8, anchor="end", color=GREY)
    b += note_box(6, 288, 348, 30, "the model in one line",
                  ["no mixing along the tube: each slice behaves like a tiny batch reactor"])
    b += foot(332, "Working: fluid moves as plugs, so every element has the same residence time;")
    b += foot(344, "a PFR needs less volume than a CSTR for the same conversion above order zero.")
    return svg(W, 356, b)


# ------------------------------------------------------------------ 6. fixed bed
def fixed():
    b = heading("The fixed bed reactor", "catalyst pellets held between a distributor and a grid")
    b += vessel(120, 100, 120, 150, INK, 2.0, GLASS, rx=6)
    b += jacket(120, 100, 120, 150, TEAL, 1.2)
    b += distributor(126, 118, 108, INK, 8)
    b += packing(126, 130, 108, 78, TEAL, 11, 4.2)
    b += f'<rect x="126" y="212" width="108" height="4" rx="2" fill="{INK}"/>'
    for xx in (140, 180, 220):
        b += ln(xx, 216, xx, 246, INK, 1.4)
    b += arrow(180, 78, 180, 99, INK, 1.6)
    b += ln(180, 250, 180, 262, INK, 1.8)
    b += arrow(180, 258, 180, 266, INK, 1.4)
    b += text(186, 84, "feed in", 7.2, anchor="start", color=INK)
    b += text(186, 272, "product out", 7.2, anchor="start", color=INK)
    for ly, tx, ty, name in [(112, 126, 118, "distributor"),
                             (156, 128, 160, "catalyst pellets"),
                             (196, 128, 196, "voids: gas path"),
                             (218, 126, 214, "support grid"),
                             (246, 113, 238, "jacket")]:
        b += leader(tx, ty, 104, ly - 3.5, THIN)
        b += text(6, ly, name, 7.2, anchor="start", color=INK)
    b += text(248, 130, "one pass only:", 7.0, anchor="start", color=PURPLE)
    b += text(248, 142, "no back-mixing", 7.0, anchor="start", color=PURPLE)
    b += note_box(6, 288, 348, 30, "the two design worries",
                  ["pressure drop through the voids, and hot spots where the gas slows down"])
    b += foot(332, "Working: gas threads through the voids and reacts on the pellet surface; the bed")
    b += foot(344, "gives a big area in a small volume but cannot be emptied without stopping.")
    return svg(W, 356, b)


# ------------------------------------------------------------------ 7. fluidised bed
def fluidised():
    b = heading("The fluidised bed reactor", "gas fast enough to lift the particles: a boiling bed")
    b += vessel(112, 96, 118, 162, INK, 2.0, GLASS, rx=6)
    b += distributor(118, 226, 106, INK, 9)
    # dense bed of particles with a bubbling surface
    for j in range(6):
        yy = 214 - j * 13
        off = 4 if j % 2 else 0
        for xx in range(122 + off, 224, 9):
            b += f'<circle cx="{xx}" cy="{yy}" r="2.4" fill="none" stroke="{ORANGE}" ' \
                 f'stroke-width="0.8"/>'
    b += curve([(118, 152), (140, 146), (164, 154), (188, 147), (212, 153), (224, 148)],
               ORANGE, 1.6)
    b += bubbles(168, 118, 148, 70, 8, 5, BLUE, 1.6, 3.4)
    # gas in at the bottom (below the distributor), gas out through the cyclone
    b += ln(168, 268, 168, 258, INK, 1.6)
    b += arrow(168, 265, 168, 257, INK, 1.4)
    b += text(186, 274, "gas in", 7.2, anchor="start", color=INK)
    b += ln(230, 110, 268, 110, INK, 1.4)
    b += f'<circle cx="284" cy="104" r="14" fill="#fff" stroke="{INK}" stroke-width="1.5"/>'
    b += curve([(276, 96), (284, 104), (292, 96)], GREY, 1.0)
    b += ln(284, 90, 284, 66, INK, 1.4)
    b += arrow(284, 70, 284, 64, INK, 1.3)
    b += ln(284, 118, 284, 140, INK, 1.4)
    b += ln(284, 140, 220, 140, INK, 1.4)
    b += arrow(224, 140, 219, 140, INK, 1.2)
    b += text(292, 62, "gas out", 7.0, anchor="start", color=INK)
    b += text(302, 106, "cyclone", 7.0, anchor="start", color=INK)
    b += text(292, 148, "dipleg back", 6.8, anchor="start", color=GREY)
    b += text(292, 160, "to the bed", 6.8, anchor="start", color=GREY)
    # left-hand labels
    for ly, tx, ty, name in [(122, 118, 120, "freeboard"),
                             (152, 128, 152, "bed surface"),
                             (192, 124, 190, "dense bed"),
                             (232, 118, 228, "distributor")]:
        b += leader(tx, ty, 96, ly - 3.5, THIN)
        b += text(6, ly, name, 7.2, anchor="start", color=INK)
    b += note_box(6, 284, 348, 42, "what fluidisation buys and what it costs",
                  ["buys: uniform temperature, no hot spots, catalyst can be withdrawn and replaced",
                   "costs: gas back-mixes, attrition of the particles, and a cyclone is compulsory"])
    b += foot(340, "Working: gas through the distributor lifts the particles once the velocity passes")
    b += foot(352, "the minimum fluidisation value; bubbles then carry the gas up through the bed.")
    return svg(W, 364, b)


# ------------------------------------------------------------------ 8. slurry and bubble column
def slurry():
    b = heading("Slurry and bubble column reactors", "gas, liquid and solid in one vessel")
    # panel A: bubble column - no moving parts at all
    b += panel(6, 48, 168, 220)
    b += text(90, 62, "bubble column", 8.4, weight="bold", color=BLUE)
    b += vessel(40, 78, 100, 146, INK, 1.8, GLASS, rx=5)
    b += liquid(40, 78, 100, 146, 98, SKY, BLUE)
    b += distributor(46, 208, 88, INK, 7)
    b += bubbles(90, 102, 202, 78, 12, 7, BLUE, 1.5, 3.6)
    b += ln(118, 78, 118, 68, INK, 1.4)
    b += arrow(118, 72, 118, 66, INK, 1.2)
    b += text(124, 70, "gas out", 6.6, anchor="start", color=INK)
    b += arrow(90, 240, 90, 231, INK, 1.3)
    b += text(90, 252, "gas in", 6.6, color=INK)
    b += text(90, 264, "no moving parts", 6.6, color=PURPLE)
    # panel B: slurry reactor - the same three phases with a stirrer
    b += panel(186, 48, 168, 220)
    b += text(270, 62, "slurry reactor", 8.4, weight="bold", color=GREEN)
    b += vessel(220, 80, 100, 144, INK, 1.8, GLASS, rx=5)
    b += liquid(220, 80, 100, 144, 100, SKY, BLUE)
    b += jacket(220, 80, 100, 144, TEAL, 1.1)
    b += motor(270, 76, 20, 10)
    b += shaft(270, 81, 202, INK, 1.8)
    b += impeller(270, 198, 20, INK, 4)
    b += distributor(226, 210, 88, INK, 6)
    for cx, cy in [(238, 128), (258, 148), (286, 136), (302, 158), (246, 172), (292, 180),
                   (266, 116), (310, 120)]:
        b += f'<circle cx="{cx}" cy="{cy}" r="2.2" fill="{ORANGE}"/>'
    b += arrow(270, 240, 270, 231, INK, 1.3)
    b += text(270, 252, "gas in through the sparger", 6.6, color=INK)
    b += text(270, 264, "catalyst stays suspended", 6.6, color=PURPLE)
    b += note_box(6, 276, 348, 42, "why the three phases are put together",
                  ["gas dissolves into the liquid, the liquid carries the solid catalyst, the solid",
                   "does the chemistry: the slowest of the three steps sets the overall rate"])
    b += foot(332, "Working: gas enters at the bottom, the liquid (or slurry) is continuous, and the")
    b += foot(344, "product leaves with the liquid; a settler or filter keeps the catalyst at home.")
    return svg(W, 356, b)


# ------------------------------------------------------------------ 9. spray tower and trickle bed
def spray():
    b = heading("Spray tower and trickle bed", "gas and liquid in counter-current contact")
    # panel A: spray tower, liquid dispersed as drops
    b += panel(6, 48, 168, 220)
    b += text(90, 62, "spray tower", 8.4, weight="bold", color=BLUE)
    b += vessel(42, 80, 96, 144, INK, 1.8, GLASS, rx=5)
    b += liquid(42, 198, 96, 26, 198, SKY, BLUE)
    b += ln(90, 80, 90, 90, INK, 1.6)
    b += text(62, 76, "liquid in", 6.6, anchor="end", color=INK)
    b += ln(90, 90, 64, 132, BLUE, 1.0)
    b += ln(90, 90, 116, 132, BLUE, 1.0)
    b += droplets(90, 96, 18, 8, BLUE)
    b += ln(118, 80, 118, 70, INK, 1.4)
    b += arrow(118, 74, 118, 68, INK, 1.2)
    b += text(124, 72, "gas out", 6.6, anchor="start", color=INK)
    b += arrow(90, 240, 90, 231, INK, 1.3)
    b += text(90, 252, "gas in", 6.6, color=INK)
    b += text(90, 264, "huge area, tiny hold-up", 6.6, color=PURPLE)
    # panel B: trickle bed, liquid films over fixed packing
    b += panel(186, 48, 168, 220)
    b += text(270, 62, "trickle bed", 8.4, weight="bold", color=GREEN)
    b += vessel(222, 80, 96, 144, INK, 1.8, GLASS, rx=5)
    b += distributor(228, 94, 84, INK, 6)
    b += droplets(270, 98, 20, 6, BLUE)
    b += packing(228, 108, 84, 84, TEAL, 11, 4.0)
    b += arrow(270, 72, 270, 84, INK, 1.3)
    b += text(338, 72, "gas in", 6.6, anchor="end", color=INK)
    b += ln(270, 224, 270, 234, INK, 1.6)
    b += arrow(270, 229, 270, 237, INK, 1.3)
    b += text(270, 250, "liquid + product out", 6.6, color=INK)
    b += text(270, 264, "catalyst stays wetted", 6.6, color=PURPLE)
    b += note_box(6, 276, 348, 42, "the choice between the two",
                  ["spray tower: liquid is the dispersed phase, good for absorption and fast reactions",
                   "trickle bed: liquid films over a fixed catalyst, good for slow three-phase reactions"])
    b += foot(332, "Working: gas rises, liquid falls, and the two meet on drops or on a wetted")
    b += foot(344, "catalyst surface; the contact area per unit volume is what decides the size.")
    return svg(W, 356, b)


DIAGRAMS = {
    "u4_models": models,
    "u4_batch": batch,
    "u4_semibatch": semibatch,
    "u4_cstr": cstr,
    "u4_pfr": pfr,
    "u4_fixed": fixed,
    "u4_fluidised": fluidised,
    "u4_slurry": slurry,
    "u4_spray": spray,
}
