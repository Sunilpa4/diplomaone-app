"""Six figures for Engineering Materials Science (DI01000181) Unit 6 - green and advanced materials.

The numbers are the ones the notes and the six numericals use: the embodied energy of a kilogram of
each material and what recycling saves, the 1500 kg of an electric car split by material, the five
layers of a lithium-ion cell, the 1000 W/m2 that becomes 200 W/m2 of electricity and 1.28 kWh a day,
and the specific strength that decides a lightweight part. Nothing is sketched by eye.
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


# ---------------------------------------------------------------- 1 the life cycle
def life_cycle():
    b = heading("The life of a material, and where it can be closed",
                "cradle to grave on the outside, cradle to cradle on the inside")
    boxes = (
        ("RAW MATERIAL", 6, 48, "ore, oil, biomass", GREY),
        ("MANUFACTURE", 186, 48, "melting, forming, joining", BLUE),
        ("END OF LIFE", 6, 152, "scrap, shredding, sorting", ORANGE),
        ("USE", 186, 152, "the service life", TEAL),
    )
    for name, px, py, sub, col in boxes:
        b += panel(px, py, 168, 58, fill="#FBFCFD")
        b += text(px + 84, py + 24, name, 7.6, weight="bold", color=col)
        b += text(px + 84, py + 42, sub, 6.2, color=GREY)
    b += arrow(176, 76, 184, 76, INK, 1.2, 5)
    b += arrow(270, 108, 270, 150, INK, 1.2, 5)
    b += arrow(184, 180, 176, 180, INK, 1.2, 5)
    b += arrow(64, 150, 64, 108, GREEN, 1.5, 5)
    b += text(74, 126, "recycle closes the loop", 6.4, anchor="start", color=GREEN,
              weight="bold")
    b += arrow(64, 212, 64, 234, RED, 1.5, 5)
    b += text(74, 228, "landfill leaves it open", 6.4, anchor="start", color=RED)

    b += note_box(6, 242, 348, 72, "a green material is green on four counts, and never on one",
                  ["renewable: grown again in a human lifetime - wood, cork, jute, bamboo",
                   "recyclable: a second life with a fraction of the first energy - all metals",
                   "low impact: little energy, water or toxicity per kilogram delivered",
                   "durable: the greenest part is the one that does not have to be replaced"])
    b += foot(330, "Ask for the whole life, not the label: a bamboo chair glued with formaldehyde and",
              "flown across the world is not greener than a steel one that lasts forty years.")
    return svg(W, 350, b)


# ---------------------------------------------------------------- 2 embodied energy
def embodied_energy():
    b = heading("Embodied energy per kg, and what recycling saves",
                "MJ to deliver one kilogram, on a linear scale")
    rows = (("concrete", 1.0, 0.9, GREY), ("glass", 15.0, 12.0, TEAL), ("steel", 25.0, 10.0, BLUE),
            ("PET plastic", 80.0, 40.0, ORANGE), ("aluminium", 170.0, 8.0, PURPLE),
            ("CFRP", 500.0, 300.0, RED))
    x0, top, span = 104, 58, 190
    for i, (name, virgin, rec, col) in enumerate(rows):
        yy = top + i * 20
        b += text(x0 - 8, yy + 4, name, 6.8, anchor="end")
        wid = virgin / 500 * span
        b += poly([(x0, yy - 3.5), (x0 + wid, yy - 3.5), (x0 + wid, yy + 4.5), (x0, yy + 4.5)],
                  col, 0.7, close=True,
                  fill={"#666666": "#E9EDF1", "#00695C": "#D8EDEA", "#1565C0": "#DCEEFB",
                        "#B66A00": "#F6E3C5", "#7B2CD9": "#EFE4FB", "#BD2543": "#F7DDE3"}[col])
        b += text(x0 + wid + 5, yy + 4, f"{virgin:g}", 6.2, anchor="start", color=GREY)
        b += text(x0 + wid + 26, yy + 4, f"rec {rec:g}", 5.8, anchor="start", color=GREEN)

    b += note_box(6, 190, 348, 58, "why aluminium is the recycling material",
                  ["170 MJ/kg new against 8 MJ/kg from scrap: a saving of 95 % of the energy",
                   "steel saves 60 %, glass 20 %, and a plastic only 50 % because it is a polymer",
                   "one aluminium can recycled saves enough electricity to run a television for 3 h"])
    b += foot(262, "The energy is in the metal, not in the shape: melting scrap takes a furnace, but",
              "winning it from ore takes a mine, a refinery and a great deal of electricity.")
    return svg(W, 282, b)


# ---------------------------------------------------------------- 3 what an electric car is made of
def ev_materials():
    b = heading("What a 1500 kg electric car is made of", "mass in kilograms, and share of the car")
    rows = (("steel and AHSS", 675, GREY),
            ("aluminium", 300, BLUE),
            ("battery pack", 225, PURPLE),
            ("polymers and composites", 180, ORANGE),
            ("copper", 75, ORANGE),
            ("glass and other", 45, TEAL))
    total = sum(r[1] for r in rows)
    x0, top, span = 118, 56, 156
    for i, (name, kg, col) in enumerate(rows):
        yy = top + i * 21
        b += text(x0 - 6, yy + 4, name, 6.4, anchor="end")
        wid = kg / total * span
        b += poly([(x0, yy - 4), (x0 + wid, yy - 4), (x0 + wid, yy + 5), (x0, yy + 5)],
                  col, 0.7, close=True,
                  fill={"#B66A00": "#F6E3C5", "#1565C0": "#DCEEFB", "#7B2CD9": "#EFE4FB",
                        "#666666": "#E9EDF1", "#00695C": "#D8EDEA"}[col])
        b += text(x0 + wid + 5, yy + 4, f"{kg} kg", 6.2, anchor="start", color=GREY)
        b += text(x0 + wid + 40, yy + 4, f"{kg / total * 100:.0f} %", 6.0, anchor="start",
                  color=INK)
    b += text(x0, top + len(rows) * 21 + 2, "total 1500 kg, of which 15 % is the battery",
              6.2, anchor="start", color=GREY)

    b += note_box(6, 204, 348, 58, "three numbers that shape the material choice",
                  ["every 100 kg removed is about 0.4 kWh less energy per 100 km",
                   "the pack is 225 kg and 35 kWh: 155 Wh per kg of pack, not of cell",
                   "an EV uses 3 times the copper of a car with an engine: 75 kg against 23"])
    b += foot(276, "The green car is not a different material world: it is the same steel, aluminium",
              "and copper, rearranged around a battery that was not there before.")
    return svg(W, 296, b)


# ---------------------------------------------------------------- 4 the lithium-ion cell
def battery_stack():
    b = heading("The five materials in one lithium-ion cell", "each layer has one job")
    layers = ((10, "#E9EDF1", THIN, ""),
              (20, "#EFE4FB", PURPLE, "cathode: NMC or LFP, 60 um"),
              (14, "#FFF6EC", ORANGE, "separator plus electrolyte, 20 um"),
              (18, "#D8EEDA", GREEN, "anode: graphite, 50 um"),
              (10, "#E9EDF1", THIN, ""))
    b += film_stack(40, 56, 190, layers, size=5.8)
    b += text(40, 48, "a single cell, 3.7 V", 6.6, anchor="start", weight="bold")

    b += leader(232, 61, 240, 61)
    b += text(244, 63, "aluminium foil, 15 um", 6.0, anchor="start", color=GREY)
    b += leader(232, 123, 240, 123)
    b += text(244, 125, "copper foil, 10 um", 6.0, anchor="start", color=GREY)
    b += leader(232, 76, 240, 76)
    b += text(244, 79, "holds the lithium", 6.0, anchor="start", color=PURPLE)
    b += leader(232, 93, 240, 93)
    b += text(244, 96, "keeps the plates apart", 6.0, anchor="start", color=ORANGE)

    b += note_box(6, 146, 348, 74, "the four numbers of a cell, and what they mean for the car",
                  ["cell 3.7 V and 50 Ah: energy 185 Wh, and a 96 cell pack is 355 V and 17.8 kWh",
                   "specific energy: LFP 140, NMC 220 Wh/kg of cell; the pack is 30 % less",
                   "life is counted in cycles: 1500 to 3000 for a car, 5000 for a stationary pack",
                   "at end of life the metals are worth recovering: Li, Ni, Co and the copper"])
    b += foot(242, "A battery is the only part of a machine whose material is chosen for its chemistry",
              "rather than its strength, and the only one whose second life is a problem.")
    return svg(W, 264, b)


# ---------------------------------------------------------------- 5 the solar panel
def solar_chain():
    b = heading("From 1000 W/m2 of sunlight to 1.28 kWh a day", "the losses at each step")
    steps = (("sunlight on the panel", 1000, GREY, "#E9EDF1"),
             ("after reflection and heat", 850, BLUE, "#DCEEFB"),
             ("converted by the cells at 20 %", 200, TEAL, "#D8EDEA"),
             ("after inverter and wiring", 170, GREEN, "#D8EEDA"))
    x0, top, span = 150, 58, 150
    for i, (name, val, col, tint) in enumerate(steps):
        yy = top + i * 24
        b += text(x0 - 8, yy + 4, name, 6.2, anchor="end")
        wid = val / 1000 * span
        b += poly([(x0, yy - 5), (x0 + wid, yy - 5), (x0 + wid, yy + 6), (x0, yy + 6)],
                  col, 0.8, close=True, fill=tint)
        b += text(x0 + wid + 6, yy + 4, f"{val} W/m2", 6.2, anchor="start", color=col)

    b += text(150, 158, "2 m2 panel at 200 W/m2 = 400 W peak", 6.6, anchor="start",
              weight="bold")
    b += text(150, 170, "4 peak sun hours at 0.8 performance ratio", 6.2, anchor="start",
              color=GREY)
    b += text(150, 182, "= 400 x 4 x 0.8 = 1280 Wh = 1.28 kWh per day", 6.4, anchor="start",
              color=GREEN, weight="bold")

    b += note_box(6, 196, 348, 58, "the materials behind the number",
                  ["mono silicon 20 - 22 %, poly 16 - 18 %, CdTe and CIGS 16 - 18 % of module area",
                   "a module is glass, EVA, cells, backsheet and an aluminium frame: 70 % is not cell",
                   "energy payback 1 to 3 years against 25: nine tenths of its output is carbon free"])
    b += foot(268, "Efficiency is a material property, so the panel is chosen for the area it can use:",
              "a roof short of area buys mono silicon, a field buys whatever is cheapest per kWh.")
    return svg(W, 288, b)


# ---------------------------------------------------------------- 6 specific strength
def lightweight():
    b = heading("Specific strength: the fair comparison",
                "UTS divided by density, in kN m per kg")
    rows = (("mild steel", 57, 7.85, GREY), ("aluminium 6061-T6", 115, 2.70, BLUE),
            ("magnesium AZ91", 115, 1.74, TEAL), ("GFRP laminate", 158, 1.90, ORANGE),
            ("titanium 6Al-4V", 260, 4.43, PURPLE), ("CFRP laminate", 938, 1.60, RED))
    x0, top, span = 126, 58, 178
    for i, (name, ss, rho, col) in enumerate(rows):
        yy = top + i * 20
        b += text(x0 - 6, yy + 4, name, 6.4, anchor="end")
        wid = ss / 950 * span
        b += poly([(x0, yy - 3.5), (x0 + wid, yy - 3.5), (x0 + wid, yy + 4.5), (x0, yy + 4.5)],
                  col, 0.7, close=True,
                  fill={"#666666": "#E9EDF1", "#1565C0": "#DCEEFB", "#00695C": "#D8EDEA",
                        "#B66A00": "#F6E3C5", "#7B2CD9": "#EFE4FB", "#BD2543": "#F7DDE3"}[col])
        b += text(x0 + wid + 5, yy + 4, f"{ss}", 6.2, anchor="start", color=GREY)
        b += text(x0 + wid + 30, yy + 4, f"rho {rho:g}", 5.8, anchor="start", color=THIN)

    b += note_box(6, 190, 348, 58, "the same number, two engineering meanings",
                  ["lightweighting: 100 kg off a car is 0.4 kWh per 100 km less to move",
                   "green: half the material is half the embodied energy and half the fuel",
                   "but stiffness, not strength, decides a panel: CFRP needs a thicker section"])
    b += foot(262, "A moving part is judged by specific strength and a static part by stiffness, which",
              "is why the same two materials win in two different places on the same car.")
    return svg(W, 282, b)


TITLES = {
    "u6_cycle": "The life cycle of a material",
    "u6_energy": "Embodied energy and recycling",
    "u6_ev": "Materials in an electric car",
    "u6_batt": "The layers of a lithium-ion cell",
    "u6_solar": "From sunlight to kWh",
    "u6_light": "Specific strength for lightweighting",
}

CAPTIONS = {
    "u6_cycle": "Raw material, manufacture, use and end of life, with recycling closing the loop and "
                "landfill leaving it open - the difference between cradle to grave and cradle to cradle.",
    "u6_energy": "One kilogram of aluminium carries 170 MJ of primary energy and one kilogram of "
                 "concrete carries one; recycling the aluminium saves 95 % of that energy, which is "
                 "why scrap is a raw material.",
    "u6_ev": "A 1500 kg electric car is 675 kg of steel, 300 kg of aluminium and 225 kg of battery, "
             "and the battery is the part that did not exist in the material list before.",
    "u6_batt": "Current collector, cathode, separator and electrolyte, anode, current collector: five "
               "materials stacked 150 micrometres thick, and one cell of 3.7 V and 185 Wh.",
    "u6_solar": "1000 W/m2 arrives, 200 W/m2 leaves the cells as electricity, and a 2 m2 panel on four "
                "peak sun hours delivers 1.28 kWh a day after the inverter.",
    "u6_light": "Steel 57 against CFRP 938 kN m per kg: specific strength is what decides a moving "
                "part, and stiffness is what usually decides a panel.",
}

DIAGRAMS = {
    "u6_cycle": life_cycle,
    "u6_energy": embodied_energy,
    "u6_ev": ev_materials,
    "u6_batt": battery_stack,
    "u6_solar": solar_chain,
    "u6_light": lightweight,
}
