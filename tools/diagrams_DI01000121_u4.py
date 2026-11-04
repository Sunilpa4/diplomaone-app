"""Five compact mobile SVGs for Applied Physics (DI01000121) Unit 4: heat and thermometry."""
from diagrams_DI01000121_u1 import (svg, text, rbox, P, ln, heading, foot,
                                   BLUE, BF, GREEN, GF, ORANGE, OF, RED, RF, PURPLE, PF,
                                   GREY, INK)
from diagrams_DI01000121_u3 import arrow

TITLES = {
    "u4_transfer": "Conduction, convection and radiation",
    "u4_scales": "The three temperature scales side by side",
    "u4_conduction": "Heat flow through a slab",
    "u4_expansion": "Expansion of a rod and the bimetallic strip",
    "u4_thermometer": "Reading a mercury thermometer",
}

TITLES_GU = {
    "u4_transfer": "વહન, સંવહન અને વિકિરણ",
    "u4_scales": "ત્રણ તાપમાન માપક્રમ સાથે સાથે",
    "u4_conduction": "પટ્ટામાંથી ઉષ્મા પ્રવાહ",
    "u4_expansion": "સળિયાનું પ્રસરણ અને બાયમેટાલિક પટ્ટી",
    "u4_thermometer": "પારા થર્મોમીટરનું વાંચન",
}

CAPTIONS = {
    "u4_transfer": "Conduction needs a solid, convection needs a fluid, radiation needs nothing at all.",
    "u4_scales": "180 Fahrenheit degrees cover the same span as 100 Celsius degrees.",
    "u4_conduction": "The rate is proportional to the area and the temperature difference, and "
                     "inversely proportional to the thickness.",
    "u4_expansion": "The rod grows by α L ΔT; joined to a metal with a smaller α it must bend.",
    "u4_thermometer": "The reading is taken at the top of the column, where the meniscus is convex.",
}

CAPTIONS_GU = {
    "u4_transfer": "વહનને ઘન જોઈએ, સંવહનને પ્રવાહી જોઈએ, વિકિરણને કંઈ જ ન જોઈએ.",
    "u4_scales": "180 ફેરનહીટ અંશ એ 100 સેલ્સિયસ અંશ જેટલી જ શ્રેણી આવરે.",
    "u4_conduction": "દર ક્ષેત્રફળ અને તાપમાન તફાવતના સમપ્રમાણમાં, અને જાડાઈના વ્યસ્ત પ્રમાણમાં.",
    "u4_expansion": "સળિયો α L ΔT જેટલો વધે; ઓછા α વાળી ધાતુ સાથે જોડાય તો વળવું પડે.",
    "u4_thermometer": "વાંચન સ્તંભની ટોચે લેવાય, જ્યાં મેનિસ્કસ બહિર્ગોળ હોય.",
}


# ------------------------------------------------------------------ 1. three modes
def transfer():
    b = heading("Three ways for heat to travel", "only radiation crosses a vacuum")
    panels = ((12, "conduction", "solid, no bulk motion", BLUE, BF),
              (180, "convection", "the fluid itself moves", ORANGE, OF))
    for x, name, sub, col, fill in panels:
        b += f'<rect x="{x}" y="58" width="168" height="120" rx="8" fill="{fill}" stroke="{col}" stroke-width="0.9"/>'
        b += text(x + 84, 76, name, 9.6, weight="bold", color=col)
        b += text(x + 84, 89, sub, 8.2, color=GREY)

    # conduction: a bar with a hot left end, arrows of energy moving right
    x0, y0 = 30, 104
    b += f'<rect x="{x0}" y="{y0 + 14}" width="132" height="18" fill="#FFFFFF" stroke="{BLUE}" stroke-width="1.2"/>'
    b += f'<rect x="{x0}" y="{y0 + 14}" width="26" height="18" fill="{RED}" opacity="0.65"/>'
    b += text(x0 + 13, y0 + 56, "hot", 8.4, color=RED)
    b += text(x0 + 119, y0 + 56, "cold", 8.4, color=BLUE)
    for dx in (32, 50, 68, 86, 104):
        b += arrow(x0 + dx, y0 + 23, x0 + dx + 12, y0 + 23, BLUE, 1.2)

    # convection: a loop with rising hot and falling cold arrows
    cx, cy = 264, 120
    b += f'<rect x="{cx - 46}" y="{cy - 34}" width="92" height="68" rx="6" fill="#FFFFFF" stroke="{ORANGE}" stroke-width="1.2"/>'
    b += arrow(cx + 20, cy + 26, cx + 20, cy - 26, RED, 1.5)
    b += arrow(cx - 20, cy - 26, cx - 20, cy + 26, BLUE, 1.5)
    b += text(cx + 30, cy + 2, "up", 8.2, anchor="start", color=RED)
    b += text(cx - 30, cy + 2, "down", 8.2, anchor="end", color=BLUE)

    # radiation: the Sun to the Earth through vacuum
    b += text(180, 196, "radiation: the Sun to the Earth", 9.4, weight="bold", color=PURPLE)
    sx, ex = 66, 300
    b += f'<circle cx="{sx}" cy="232" r="17" fill="{OF}" stroke="{ORANGE}" stroke-width="1.2"/>'
    b += text(sx, 262, "Sun", 8.4, color=ORANGE)
    b += f'<circle cx="{ex}" cy="232" r="13" fill="{BF}" stroke="{BLUE}" stroke-width="1.2"/>'
    b += text(ex, 262, "Earth", 8.4, color=BLUE)
    for dy in (-6, 0, 6):
        b += arrow(sx + 22, 232 + dy, ex - 18, 232 + dy, ORANGE, 1.1)
    b += text(180, 210, "no medium needed", 8.4, color=GREY)

    y = 292
    b += foot(y, "A thermos blocks all three: vacuum, silvered walls and a tight stopper.")
    return svg(360, y + 18, b)


# ------------------------------------------------------------------ 2. three scales
def scales():
    b = heading("Celsius, Fahrenheit and Kelvin", "same heat, three numbering systems")
    x0, x1 = 62, 330
    top, bot = 76, 236

    def t_of(c):
        return bot - (c / 100.0) * (bot - top)

    for x, name, col in ((x0, "°C", BLUE), (x0 + 96, "°F", ORANGE), (x0 + 192, "K", GREEN)):
        b += ln(x, top - 8, x, bot + 8, col, 2.0)
        b += text(x, top - 18, name, 10.4, weight="bold", color=col)

    ticks = ((0, "0", "32", "273"), (50, "50", "122", "323"), (100, "100", "212", "373"))
    for c, cv, fv, kv in ticks:
        y = t_of(c)
        b += ln(x0 - 5, y, x1 + 6, y, "#DDDDDD", 0.9)
        b += text(x0 - 10, y + 3.4, cv, 8.8, anchor="end", color=BLUE)
        b += text(x0 + 96 - 9, y + 3.4, fv, 8.8, anchor="end", color=ORANGE)
        b += text(x0 + 192 + 9, y + 3.4, kv, 8.8, anchor="start", color=GREEN)

    b += text(180, 268, "F = 9/5 C + 32   ·   K = C + 273.15", 9.2, color=INK)
    b += foot(298, "Ice point and steam point are the two fixed points of every scale.")
    return svg(360, 322, b)


# ------------------------------------------------------------------ 3. conduction through a slab
def conduction():
    b = heading("Heat flow through a wall", "Q/t = k A ΔT / L")
    xl, xr, top, bot = 84, 262, 84, 196
    b += f'<rect x="{xl}" y="{top}" width="{xr - xl}" height="{bot - top}" fill="{OF}" stroke="{ORANGE}" stroke-width="1.3"/>'
    b += text((xl + xr) / 2, top - 10, "face area A", 8.6, color=GREY)

    b += ln(xl, top - 24, xl, bot + 24, RED, 2.4)
    b += ln(xr, top - 24, xr, bot + 24, BLUE, 2.4)
    b += text(xl - 10, top - 14, "hot face", 8.6, anchor="end", color=RED)
    b += text(xl - 10, top + 40, "T₁", 9.4, weight="bold", anchor="end", color=RED)
    b += text(xr + 10, top - 14, "cold face", 8.6, anchor="start", color=BLUE)
    b += text(xr + 10, top + 40, "T₂", 9.4, weight="bold", anchor="start", color=BLUE)

    for y in (top + 30, top + 62, top + 94):
        b += arrow(xl + 16, y, xr - 16, y, ORANGE, 1.3)
    b += text((xl + xr) / 2, bot + 18, "heat flows from hot to cold", 8.6, color=GREY)

    # thickness arrow below
    b += arrow(xl, bot + 34, xr, bot + 34, INK, 1.0)
    b += arrow(xr, bot + 34, xl, bot + 34, INK, 1.0)
    b += text((xl + xr) / 2, bot + 48, "thickness L", 8.6, color=INK)

    y = 286
    b += rbox(180, y, 336, 26, "k in W/(m·K): copper 400, brick 0.6, air 0.026", RF, RED, 9.0)
    b += foot(y + 30, "Double the thickness and the loss halves; double the area and it doubles.")
    return svg(360, y + 52, b)


# ------------------------------------------------------------------ 4. expansion
def expansion():
    b = heading("A rod grows, a bimetallic strip bends", "ΔL = α L ΔT")
    # rod before and after
    y1, y2 = 96, 132
    b += f'<rect x="40" y="{y1}" width="180" height="14" fill="{BF}" stroke="{BLUE}" stroke-width="1.2"/>'
    b += f'<rect x="40" y="{y2}" width="196" height="14" fill="{OF}" stroke="{ORANGE}" stroke-width="1.2"/>'
    b += text(40, y1 - 8, "at 20 °C", 8.6, anchor="start", color=BLUE)
    b += text(40, y2 + 30, "at 120 °C", 8.6, anchor="start", color=ORANGE)
    b += ln(40, y1 + 7, 40, y2 + 7, GREY, 0.8, dash="2 2")
    b += arrow(220, y2 + 24, 236, y2 + 24, ORANGE, 1.1)
    b += arrow(236, y2 + 24, 220, y2 + 24, ORANGE, 1.1)
    b += ln(220, y2 + 12, 220, y2 + 28, "#BBBBBB", 0.8, dash="2 2")
    b += ln(236, y2 + 12, 236, y2 + 28, "#BBBBBB", 0.8, dash="2 2")
    b += text(243, y2 + 27, "ΔL = 4.6 mm", 8.4, anchor="start", color=ORANGE)
    b += text(130, y1 + 7 + 3, "L", 9.0, color=INK)

    # bimetallic strip: flat then curved
    b += text(180, 196, "bimetallic strip: brass above, iron below", 8.8, color=GREY)
    b += f'<rect x="56" y="212" width="112" height="7" fill="#E8C46A" stroke="{ORANGE}" stroke-width="0.9"/>'
    b += f'<rect x="56" y="219" width="112" height="7" fill="#BFC7D1" stroke="#7A8794" stroke-width="0.9"/>'
    b += text(112, 240, "cold: straight", 8.4, color=GREY)
    b += (f'<path d="M214 212Q256 212 288 232" fill="none" stroke="{ORANGE}" stroke-width="4.4"/>')
    b += (f'<path d="M214 219Q256 219 288 239" fill="none" stroke="#7A8794" stroke-width="4.4"/>')
    b += text(252, 256, "hot: bends, iron inside", 8.4, color=INK)

    y = 276
    b += rbox(180, y, 336, 26, "steel α = 12 × 10⁻⁶ K⁻¹   ·   invar ≈ 1 × 10⁻⁶ K⁻¹", GF, GREEN, 9.0)
    b += foot(y + 30, "A 10 m rail warms by 40 K and grows 4.8 mm, so joints need a gap.")
    return svg(360, y + 52, b)


# ------------------------------------------------------------------ 5. mercury thermometer
def thermometer():
    b = heading("Reading a mercury thermometer", "mercury does not wet glass")
    x, top, bot = 168, 74, 236
    b += f'<rect x="{x - 6}" y="{top}" width="12" height="{bot - top - 26}" rx="5" fill="#F2F5F8" stroke="#9AA5B1" stroke-width="1.1"/>'
    b += f'<circle cx="{x}" cy="{bot - 14}" r="14" fill="#C62828" stroke="#8E1B1B" stroke-width="1.1"/>'
    level = 138
    b += f'<rect x="{x - 3.2}" y="{level}" width="6.4" height="{bot - 30 - level}" fill="#C62828"/>'

    marks = ((86, "100"), (110, "80"), (134, "60"), (158, "40"), (182, "20"), (206, "0"))
    for y, lab in marks:
        b += ln(x + 7, y, x + 15, y, GREY, 0.9)
        b += text(x + 20, y + 3.2, lab, 8.6, anchor="start", color=INK)
    b += text(x + 20, 74 - 10, "°C", 9.0, anchor="start", color=GREY)

    b += arrow(x - 26, level, x - 12, level, RED, 1.2)
    b += text(x - 30, level + 3.4, "read here", 8.6, anchor="end", color=RED)
    b += text(x - 30, level + 16, "top of column", 8.2, anchor="end", color=GREY)
    b += text(x, bot + 16, "bulb", 8.4, color=GREY)

    y = 272
    b += rbox(180, y, 336, 26, "range −39 °C to 357 °C: mercury freezes at −39", OF, ORANGE, 9.0)
    b += foot(y + 30, "Read it in place: the column falls as soon as it leaves the body.")
    return svg(360, y + 52, b)


DIAGRAMS = {
    "u4_transfer": transfer,
    "u4_scales": scales,
    "u4_conduction": conduction,
    "u4_expansion": expansion,
    "u4_thermometer": thermometer,
}
