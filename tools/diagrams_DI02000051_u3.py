"""Six compact mobile SVGs for Environmental Sustainability (DI02000051) Unit 3.

Labels stay in English (diagrams are English in every bilingual subject here); the card text carries
both languages. Every shape is plain rect/path/text, 360 px wide for a phone.
"""
import math

from flowchart_lib import svg, text, rbox, P

BLUE, BF = "#1565C0", "#EAF3FD"
GREEN, GF = "#2E7D32", "#EAF6EC"
ORANGE, OF = "#B66A00", "#FFF4DF"
RED, RF = "#BD2543", "#FDECF0"
PURPLE, PF = "#7B2CD9", "#F3EBFD"
TEAL, TF = "#00695C", "#E0F2F1"
GREY = "#666"
INK = "#222"

TITLES = {
    "u3_mix": "The energy mix and what each source costs the air",
    "u3_pv": "How a solar cell turns light into current",
    "u3_cells": "Efficiency of the solar cell families",
    "u3_wind": "Horizontal axis and vertical axis wind turbines",
    "u3_bio": "Routes from biomass to fuel",
    "u3_new": "Geothermal, ocean and hydrogen at a glance",
}

TITLES_GU = {
    "u3_mix": "ઊર્જા મિશ્રણ અને દરેક સ્રોત હવાને કેટલું ખર્ચે",
    "u3_pv": "સૌર સેલ પ્રકાશને પ્રવાહમાં કેવી રીતે ફેરવે",
    "u3_cells": "સૌર સેલ કુટુંબોની કાર્યક્ષમતા",
    "u3_wind": "આડી અક્ષ અને ઊભી અક્ષની પવન ટર્બાઇન",
    "u3_bio": "બાયોમાસથી ઇંધણ સુધીના રસ્તા",
    "u3_new": "ભૂતાપ, મહાસાગર અને હાઇડ્રોજન એક નજરે",
}

CAPTIONS = {
    "u3_mix": "Solar and wind cost nothing to run and emit nothing at the plant; the small life-cycle "
              "share comes from making the panels and turbines.",
    "u3_pv": "Photons free electrons at the junction, the built-in field separates them, and the "
             "contacts collect the current; heat and unused photons are the main losses.",
    "u3_cells": "Monocrystalline wins on area, thin film wins on price and weak light, perovskite "
                "promises more but is not yet proven outdoors.",
    "u3_wind": "A HAWT sweeps a big disc and reaches Cp 0.45-0.50; a VAWT accepts wind from any side "
               "and reaches only 0.15-0.35.",
    "u3_bio": "Burn it, digest it, ferment it or gasify it - the route decides whether you get heat, "
              "gas, ethanol or producer gas.",
    "u3_new": "Geothermal gives firm heat, the ocean gives predictable tides and OTEC, hydrogen "
              "carries renewable electricity to places a wire cannot reach.",
}

CAPTIONS_GU = {
    "u3_mix": "સૌર અને પવન ચલાવવા મફત છે અને સ્ટેશન પર કંઈ છોડતા નથી; થોડો જીવનચક્ર હિસ્સો પેનલ અને "
              "ટર્બાઇન બનાવવામાંથી આવે.",
    "u3_pv": "ફોટોન સંધિ પર ઇલેક્ટ્રોન મુક્ત કરે, આંતરિક ક્ષેત્ર તેમને અલગ કરે અને સંપર્ક પ્રવાહ એકઠો કરે; "
             "ઉષ્મા અને ન વપરાયેલા ફોટોન મુખ્ય ખોટ છે.",
    "u3_cells": "મોનોક્રિસ્ટાલાઇન જગ્યામાં જીતે, પાતળી ફિલ્મ ભાવ અને નબળા પ્રકાશમાં જીતે, પેરોવસ્કાઇટ વધુ "
                "વચન આપે પણ બહાર પુરવાર થયું નથી.",
    "u3_wind": "HAWT મોટી ડિસ્ક ઘેરે અને Cp 0.45-0.50 પામે; VAWT ગમે તે બાજુથી પવન સ્વીકારે અને ફક્ત "
               "0.15-0.35 પામે.",
    "u3_bio": "બાળો, પચાવો, આથો લાવો કે ગેસિફાય કરો - રસ્તો નક્કી કરે કે ઉષ્મા, ગેસ, ઇથેનોલ કે પ્રોડ્યુસર "
              "ગેસ મળશે.",
    "u3_new": "ભૂતાપ નિશ્ચિત ઉષ્મા આપે, મહાસાગર અનુમાનિત ભરતી અને OTEC, હાઇડ્રોજન પુનઃપ્રાપ્ય વીજળી તાર "
              "પહોંચે નહીં ત્યાં લઈ જાય.",
}


def ln(x1, y1, x2, y2, color=INK, w=1.2, dash=None):
    da = f' stroke-dasharray="{dash}"' if dash else ""
    return (f'<path d="M{x1} {y1}L{x2} {y2}" fill="none" stroke="{color}" stroke-width="{w}" '
            f'stroke-linecap="round"{da}/>')


def arrow(x1, y1, x2, y2, color=INK, w=1.4):
    ang = math.degrees(math.atan2(y2 - y1, x2 - x1))
    a = math.radians(ang)
    s = 6.0
    p1 = (x2 - s * math.cos(a) + s * 0.42 * math.sin(a), y2 - s * math.sin(a) - s * 0.42 * math.cos(a))
    p2 = (x2 - s * math.cos(a) - s * 0.42 * math.sin(a), y2 - s * math.sin(a) + s * 0.42 * math.cos(a))
    return (ln(x1, y1, x2 - s * 0.7 * math.cos(a), y2 - s * 0.7 * math.sin(a), color, w) +
            f'<path d="M{p1[0]:.1f} {p1[1]:.1f}L{x2:.1f} {y2:.1f}L{p2[0]:.1f} {p2[1]:.1f}Z" fill="{color}"/>')


def heading(t, sub=None, size=12.6):
    body = text(180, 21, t, size, weight="bold", color=P)
    if sub:
        body += text(180, 39, sub, 9.6, color=GREY)
    return body


def foot(y, *lines):
    return "".join(text(180, y + 14 * i, s, 9.0, color=GREY) for i, s in enumerate(lines))


# ------------------------------------------------------------------ 1. energy mix
def mix():
    b = heading("Two costs per source: money and carbon",
                "levelised cost in rupees per kWh, emissions per kWh")
    b += text(20, 66, "source", 8.4, anchor="start", color=GREY, weight="bold")
    b += text(180, 66, "cost, Rs/kWh", 8.4, color=GREY, weight="bold")
    b += text(348, 66, "g CO2/kWh", 8.4, anchor="end", color=GREY, weight="bold")
    rows = [("solar PV", 2.5, 3.2, 45, GREEN),
            ("on-shore wind", 3.0, 3.8, 12, TEAL),
            ("new coal", 4.5, 6.0, 900, RED),
            ("natural gas", 5.0, 6.5, 450, ORANGE),
            ("diesel genset", 18.0, 22.0, 780, PURPLE)]
    y = 74
    for name, lo, hi, co2, col in rows:
        b += f'<rect x="12" y="{y}" width="336" height="30" rx="5" fill="#F7F9FC" stroke="{col}" stroke-width="1.3"/>'
        b += text(20, y + 19, name, 9.0, anchor="start", color=INK, weight="bold")
        b += text(180, y + 19, f"{lo:.1f} - {hi:.1f}", 9.0, color=col)
        b += text(340, y + 19, str(co2), 9.0, anchor="end", color=col)
        y += 36
    b += rbox(180, y + 14, 344, 30,
              "cost per unit is not the same as cost per firm unit", OF, ORANGE, 8.8)
    b += foot(y + 46, "Solar and wind are cheapest to run but variable; coal is firm and dirty.",
              "Add storage or gas for the evening peak before comparing.")
    return svg(360, y + 68, b)


# ------------------------------------------------------------------ 2. PV cell
def pv():
    b = heading("Light in, current out", "five layers and one junction")
    # sun and photons
    b += f'<circle cx="36" cy="58" r="12" fill="{OF}" stroke="{ORANGE}" stroke-width="1.4"/>'
    for dx, dy in ((-1, -1), (0, -1.3), (1, -1), (-1.3, 0)):
        b += ln(36 + dx * 16, 58 + dy * 16, 36 + dx * 25, 58 + dy * 25, ORANGE, 1.4)
    for i in range(3):
        b += arrow(52, 64 + i * 9, 88, 92 + i * 8, ORANGE, 1.2)
    b += text(58, 128, "photons", 8.2, color=ORANGE)
    # the cell stack
    b += f'<rect x="92" y="74" width="132" height="14" rx="2" fill="#DDE9F8" stroke="{BLUE}" stroke-width="1.2"/>'
    b += f'<rect x="92" y="88" width="132" height="14" rx="2" fill="#CFE3FA" stroke="{BLUE}" stroke-width="1.2"/>'
    b += ln(92, 102, 224, 102, PURPLE, 1.8, dash="4 2")
    b += f'<rect x="92" y="102" width="132" height="14" rx="2" fill="#F6DFE6" stroke="{RED}" stroke-width="1.2"/>'
    b += f'<rect x="92" y="116" width="132" height="12" rx="2" fill="#E8E8E8" stroke="{GREY}" stroke-width="1.2"/>'
    b += text(230, 85, "glass + ARC", 8.0, anchor="start", color=BLUE)
    b += text(230, 100, "n-silicon", 8.0, anchor="start", color=BLUE)
    b += text(230, 114, "p-silicon", 8.0, anchor="start", color=RED)
    b += text(230, 128, "back contact", 8.0, anchor="start", color=GREY)
    b += text(84, 120, "junction", 8.0, anchor="end", color=PURPLE)
    b += ln(86, 116, 91, 103, PURPLE, 0.9)
    # carriers move opposite ways
    b += arrow(112, 99, 112, 90, BLUE, 1.3)
    b += text(118, 97, "e-", 8.2, anchor="start", color=BLUE)
    b += arrow(150, 106, 150, 113, RED, 1.3)
    b += text(156, 111, "h+", 8.2, anchor="start", color=RED)
    # external circuit: front contact over the top, back contact round the left
    b += ln(200, 74, 200, 58, INK, 1.3)
    b += ln(200, 58, 330, 58, INK, 1.3)
    b += ln(330, 58, 330, 190, INK, 1.3)
    b += ln(330, 190, 186, 190, INK, 1.3)
    b += f'<rect x="146" y="181" width="40" height="18" rx="2" fill="#FFFFFF" stroke="{INK}" stroke-width="1.3"/>'
    b += text(166, 194, "load", 7.8, color=INK)
    b += ln(146, 190, 92, 190, INK, 1.3)
    b += ln(92, 190, 92, 122, INK, 1.3)
    b += arrow(120, 190, 143, 190, BLUE, 1.3)
    b += text(120, 204, "current", 8.0, color=BLUE)
    b += rbox(180, 226, 344, 28,
              "0.6 V per cell, about 10 A per module - series adds volts, parallel adds amps",
              GF, GREEN, 8.4)
    b += foot(266, "Efficiency = power out / sunlight in; heat costs 0.4 % per degree.",
              "Below the band gap the photon is wasted, above it the surplus becomes heat.")
    return svg(360, 302, b)


# ------------------------------------------------------------------ 3. cell types
def cells():
    b = heading("Efficiency of the cell families", "laboratory best and commercial module")
    rows = [("perovskite / tandem", 33, 27, PURPLE),
            ("monocrystalline Si", 26, 22, BLUE),
            ("CIGS thin film", 23, 19, TEAL),
            ("polycrystalline Si", 22, 17, BLUE),
            ("CdTe thin film", 22, 18, ORANGE),
            ("amorphous Si", 14, 8, GREY)]
    y = 64
    for name, lab, mod, col in rows:
        b += text(12, y + 10, name, 8.6, anchor="start", color=INK)
        b += f'<rect x="146" y="{y}" width="{lab * 4.5:.0f}" height="7" rx="2" fill="{col}" fill-opacity="0.28" stroke="{col}" stroke-width="0.8"/>'
        b += f'<rect x="146" y="{y + 8}" width="{mod * 4.5:.0f}" height="7" rx="2" fill="{col}"/>'
        b += text(348, y + 11, f"{mod} / {lab} %", 7.8, anchor="end", color=col)
        y += 34
    b += text(146, y + 4, "module now", 7.6, anchor="start", color=GREY)
    b += text(146, y + 16, "laboratory record", 7.6, anchor="start", color=GREY)
    b += rbox(180, y + 46, 344, 28,
              "a 22 % module on 2.1 m2 makes 460 W under 1 000 W/m2", TF, TEAL, 8.6)
    b += foot(y + 78, "Choose by area, climate and budget, not by the record in a laboratory.",
              "Perovskite still fails in damp heat; thin film loses less in high temperature.")
    return svg(360, y + 106, b)


# ------------------------------------------------------------------ 4. wind turbines
def wind():
    b = heading("One axis points at the wind, one does not", "Cp 0.45-0.50 vs 0.15-0.35")
    # HAWT
    b += text(96, 60, "HAWT", 9.4, color=BLUE, weight="bold")
    b += ln(96, 76, 96, 150, GREY, 2.6)
    b += f'<circle cx="96" cy="76" r="4" fill="{INK}"/>'
    for ang in (210, 270, 330):
        a = math.radians(ang)
        b += ln(96, 76, 96 + 30 * math.cos(a), 76 + 30 * math.sin(a), BLUE, 2.2)
    b += text(136, 90, "3 blades", 7.6, anchor="start", color=BLUE)
    b += ln(60, 150, 132, 150, INK, 2.0)
    b += text(96, 166, "tower, 120 m", 7.8, color=GREY)
    b += arrow(40, 76, 58, 76, GREY, 1.3)
    b += text(40, 66, "wind", 7.8, color=GREY)
    # VAWT
    b += text(264, 60, "VAWT", 9.4, color=GREEN, weight="bold")
    b += ln(264, 62, 264, 150, GREY, 2.6)
    b += f'<ellipse cx="264" cy="100" rx="30" ry="34" fill="none" stroke="{GREEN}" stroke-width="2.0" stroke-dasharray="0"/>'
    b += ln(240, 78, 288, 122, GREEN, 1.4)
    b += ln(288, 78, 240, 122, GREEN, 1.4)
    b += ln(200, 150, 328, 150, INK, 2.0)
    b += text(264, 166, "generator at ground", 7.8, color=GREY)
    b += arrow(300, 90, 288, 96, GREY, 1.3)
    b += text(302, 82, "wind", 7.8, anchor="start", color=GREY)
    # comparison rows
    y = 184
    rows = [("needs yaw to face the wind", "yes", "no"),
            ("Cp, share of wind power", "0.45-0.50", "0.15-0.35"),
            ("typical size", "2-15 MW", "1-100 kW"),
            ("uses", "wind farms", "roof, street, pump")]
    b += text(96, y, "point", 8.0, color=GREY, weight="bold")
    b += text(214, y, "HAWT", 8.0, color=BLUE, weight="bold")
    b += text(320, y, "VAWT", 8.0, color=GREEN, weight="bold")
    for i, (a, c, d) in enumerate(rows):
        yy = y + 16 + i * 16
        b += text(96, yy, a, 8.2, color=INK)
        b += text(214, yy, c, 8.2, color=BLUE)
        b += text(320, yy, d, 8.2, color=GREEN)
    b += rbox(180, y + 96, 344, 26,
              "bladeless mast: silent and simple, but only a few per cent efficient",
              PF, PURPLE, 8.4)
    b += foot(y + 126, "Betz: no rotor can take more than 59.3 % of the power in the wind.",
              "Power goes with the cube of speed and the square of the rotor diameter.")
    return svg(360, y + 148, b)


# ------------------------------------------------------------------ 5. bioenergy routes
def bio():
    b = heading("Five routes out of the same heap", "the route decides the product")
    b += rbox(180, 62, 344, 30, "biomass: dung, straw, wood, oil and sugar", TF, TEAL, 8.6)
    b += arrow(180, 77, 180, 88, TEAL, 1.3)
    rows = [("burn it", "heat and steam", ORANGE),
            ("digest it in a sealed tank", "biogas, 55-65 % methane", GREEN),
            ("ferment it with yeast", "ethanol, then distilled", BLUE),
            ("gasify it with little air", "producer gas, CO + H2", PURPLE),
            ("react oil with methanol", "biodiesel + glycerol", RED)]
    y = 94
    for route, product, col in rows:
        b += f'<rect x="12" y="{y}" width="156" height="26" rx="5" fill="#FFFFFF" stroke="{col}" stroke-width="1.3"/>'
        b += text(90, y + 17, route, 8.4, color=INK)
        b += arrow(170, y + 13, 184, y + 13, col, 1.3)
        b += f'<rect x="186" y="{y}" width="162" height="26" rx="5" fill="{col}" fill-opacity="0.08" stroke="{col}" stroke-width="1.3"/>'
        b += text(267, y + 17, product, 8.0, color=col)
        y += 34
    b += rbox(180, y + 16, 344, 28,
              "1 t molasses -> 245 L ethanol;  1 t dung -> 40 m3 of biogas", OF, ORANGE, 8.4)
    b += foot(y + 48, "Wet waste goes to a digester, dry waste to a gasifier, sugar to a fermenter.",
              "Only a life-cycle sum tells you the real carbon saving.")
    return svg(360, y + 70, b)


# ------------------------------------------------------------------ 6. new sources
def new():
    b = heading("Three sources for three different jobs", "firm heat, tidal motion, clean carrier")
    cols = [("geothermal", "heat from 3 km down", "160 C brine -> 12 % cycle -> 5 MW", ORANGE, 62),
            ("ocean", "tide, wave, OTEC", "E = 0.5 A rho g R^2 per filling", TEAL, 180),
            ("hydrogen", "electrolysis, fuel cell", "50 kWh -> 1 kg -> 33 kWh -> 17 kWh", BLUE, 298)]
    for name, sub, formula, col, cx in cols:
        b += f'<rect x="{cx - 54}" y="58" width="108" height="118" rx="7" fill="#FFFFFF" stroke="{col}" stroke-width="1.5"/>'
        b += text(cx, 76, name, 9.2, color=col, weight="bold")
        b += text(cx, 92, sub, 7.4, color=GREY)
    b += text(62, 116, "binary", 7.4, color=ORANGE)
    b += text(62, 128, "cycle", 7.4, color=ORANGE)
    b += text(62, 146, "firm, 80 %", 7.4, color=ORANGE)
    b += text(62, 158, "capacity", 7.4, color=ORANGE)
    b += text(180, 116, "barrage,", 7.4, color=TEAL)
    b += text(180, 128, "stream,", 7.4, color=TEAL)
    b += text(180, 140, "OTEC, wave", 7.4, color=TEAL)
    b += text(180, 158, "predictable", 7.4, color=TEAL)
    b += text(298, 116, "green H2", 7.4, color=BLUE)
    b += text(298, 128, "fuel cell", 7.4, color=BLUE)
    b += text(298, 146, "zero at use", 7.4, color=BLUE)
    b += text(298, 158, "30-35 %", 7.4, color=BLUE)
    b += rbox(180, 196, 344, 30,
              "geothermal 44 MW heat in, 5.3 MW out - a tidal basin 362 GJ per filling",
              OF, ORANGE, 8.2)
    b += foot(238, "Hydrogen is a carrier, not a source: it must be made first.",
              "Tidal timing is fixed by the moon, so the output can be sold years ahead.")
    return svg(360, 274, b)


DIAGRAMS = {
    "u3_mix": mix,
    "u3_pv": pv,
    "u3_cells": cells,
    "u3_wind": wind,
    "u3_bio": bio,
    "u3_new": new,
}
