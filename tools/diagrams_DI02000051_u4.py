"""Six compact mobile SVGs for Environmental Sustainability (DI02000051) Unit 4.

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
    "u4_balance": "The energy balance and the greenhouse effect",
    "u4_ghg": "Greenhouse gases by strength and by source",
    "u4_temp": "Warming since 1850, and the fingerprints",
    "u4_sea": "Three routes to a higher sea",
    "u4_impacts": "What a warmer world does to land and sea",
    "u4_mitigation": "The mitigation ladder from efficiency to net zero",
}

TITLES_GU = {
    "u4_balance": "પૃથ્વીનું ઊર્જા સંતુલન અને હરિતગૃહ પ્રભાવ",
    "u4_ghg": "શક્તિ અને સ્રોત પ્રમાણે હરિતગૃહ વાયુ",
    "u4_temp": "1850થી ગરમી, અને કારણ બતાવતાં અંગૂઠાનાં નિશાન",
    "u4_sea": "ઊંચા દરિયા સુધીના ત્રણ રસ્તા",
    "u4_impacts": "ગરમ દુનિયા જમીન અને દરિયા સાથે શું કરે",
    "u4_mitigation": "કાર્યક્ષમતાથી નેટ ઝીરો સુધીનું શમન સોપાન",
}

CAPTIONS = {
    "u4_balance": "Sunlight comes in short, leaves as infrared; the greenhouse gases slow the exit and "
                  "lift the surface from -18 C to 15 C.",
    "u4_ghg": "CO2 is the largest share, methane the fastest lever, fluorinated gases the strongest per "
              "kilogram.",
    "u4_temp": "The average moved 1.2 C, but the pattern with height and with the seasons is what proves "
               "the cause.",
    "u4_sea": "Expansion, glaciers and ice sheets add about 4.5 mm a year; melting sea ice adds nothing "
              "because it already floats.",
    "u4_impacts": "Species move, the ocean turns more acidic, dry land degrades - three different "
                  "mechanisms from the same warming.",
    "u4_mitigation": "Save it, electrify it, clean it, capture what is left; offsets are the last step, "
                     "not the first.",
}

CAPTIONS_GU = {
    "u4_balance": "સૂર્યપ્રકાશ ટૂંકા તરંગે આવે અને ઇન્ફ્રારેડ તરીકે નીકળે; હરિતગૃહ વાયુ નીકળવાનું ધીમું કરે અને "
                  "સપાટી -18 Cથી 15 C કરે.",
    "u4_ghg": "CO₂ સૌથી મોટો હિસ્સો, મિથેન સૌથી ઝડપી લિવર, ફ્લોરિનવાળા વાયુ પ્રતિ કિલો સૌથી શક્તિશાળી.",
    "u4_temp": "સરેરાશ 1.2 C ખસ્યું, પણ ઊંચાઈ અને ઋતુ પ્રમાણેનો નમૂનો જ કારણ પુરવાર કરે.",
    "u4_sea": "વિસ્તરણ, હિમનદી અને બરફનાં પડ વર્ષે લગભગ 4.5 mm ઉમેરે; દરિયાઈ બરફ પીગળવાથી કંઈ વધતું નથી કારણ કે "
              "તે પહેલેથી તરે છે.",
    "u4_impacts": "જાતિઓ ખસે, મહાસાગર વધુ અમ્લીય બને, સૂકી જમીન ક્ષીણ થાય - એક જ ગરમીની ત્રણ જુદી રીતો.",
    "u4_mitigation": "બચાવો, વીજીકરણ કરો, સ્વચ્છ કરો, બાકીનું પકડો; ઓફસેટ પહેલું નહીં, છેલ્લું પગલું છે.",
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


# ------------------------------------------------------------------ 1. energy balance
def balance():
    b = heading("Short waves in, long waves out", "340 W/m2 arrives, 340 W/m2 leaves")
    b += f'<circle cx="52" cy="72" r="13" fill="{OF}" stroke="{ORANGE}" stroke-width="1.4"/>'
    b += text(52, 94, "sun", 8.2, color=ORANGE)
    b += f'<circle cx="222" cy="112" r="30" fill="{BF}" stroke="{BLUE}" stroke-width="1.6"/>'
    b += f'<circle cx="222" cy="112" r="42" fill="none" stroke="{PURPLE}" stroke-width="1.0" stroke-dasharray="4 3"/>'
    b += text(222, 110, "earth", 8.8, color=BLUE, weight="bold")
    b += text(222, 122, "15 C", 8.2, color=BLUE)
    b += text(222, 168, "the greenhouse layer", 8.0, color=PURPLE)
    # incoming short wave
    b += arrow(68, 78, 192, 102, ORANGE, 1.6)
    b += text(118, 74, "short wave, 340", 8.0, color=ORANGE)
    # reflected
    b += arrow(198, 92, 142, 62, GREY, 1.3)
    b += text(126, 54, "100 reflected", 7.8, color=GREY)
    # infrared out
    b += arrow(222, 80, 222, 52, RED, 1.6)
    b += text(232, 50, "240 out", 8.2, anchor="start", color=RED)
    # back radiation
    b += arrow(288, 56, 288, 102, PURPLE, 1.6)
    b += text(294, 74, "back", 8.0, anchor="start", color=PURPLE)
    b += text(294, 86, "radiation", 8.0, anchor="start", color=PURPLE)
    b += rbox(180, 196, 344, 28,
              "without the layer the surface would be -18 C, not 15 C", GF, GREEN, 8.4)
    b += rbox(180, 232, 344, 28,
              "we have added about 3 W/m2 of forcing since 1750", RF, RED, 8.4)
    b += foot(268, "Balance the flows and the temperature holds; unbalance them and it moves.",
              "Water vapour is the strongest absorber but it follows the temperature.")
    return svg(360, 300, b)


# ------------------------------------------------------------------ 2. greenhouse gases
def ghg():
    b = heading("GWP and share of the warming", "strength per kilogram, then share")
    rows = [("CO2", "1", 64, BLUE),
            ("CH4", "28", 17, GREEN),
            ("N2O", "265", 6, ORANGE),
            ("F-gases", "up to 14 800", 3, PURPLE)]
    y = 62
    for name, gwp, share, col in rows:
        b += f'<rect x="12" y="{y}" width="336" height="34" rx="5" fill="#FFFFFF" stroke="{col}" stroke-width="1.3"/>'
        b += text(22, y + 15, name, 9.0, anchor="start", color=col, weight="bold")
        b += text(22, y + 27, f"GWP {gwp}", 7.6, anchor="start", color=GREY)
        b += f'<rect x="150" y="{y + 9}" width="{share * 2.1:.0f}" height="16" rx="3" fill="{col}" fill-opacity="0.30" stroke="{col}" stroke-width="0.8"/>'
        b += text(296, y + 21, f"{share} %", 8.0, anchor="start", color=col)
        y += 40
    b += text(180, y + 6, "bar = share of the observed warming", 7.6, color=GREY)
    b += rbox(180, y + 36, 344, 28,
              "a tonne of landfill methane warms like 28 t of CO2", OF, ORANGE, 8.4)
    b += foot(y + 68, "CO2 sets the long trend; methane sets the speed.",
              "Water vapour is a feedback and is not counted as a forcing.")
    return svg(360, y + 94, b)


# ------------------------------------------------------------------ 3. temperature
def temp():
    b = heading("The curve, and the two fingerprints", "global mean surface temperature")
    x0, y0, x1, y1 = 52, 150, 200, 58
    b += ln(x0, y0, x1 + 8, y0, GREY, 1.2)
    b += ln(x0, y0, x0, y1 - 8, GREY, 1.2)
    b += text(44, 62, "+1.2 C", 7.6, anchor="end", color=GREY)
    b += text(44, 152, "0", 7.6, anchor="end", color=GREY)
    b += text(52, 166, "1850", 7.6, anchor="start", color=GREY)
    b += text(204, 166, "2023", 7.6, color=GREY)
    pts = [(52, 148), (76, 147), (96, 144), (116, 143), (136, 139), (156, 133), (176, 120), (194, 96), (200, 84)]
    b += f'<path d="M' + "L".join(f"{px} {py}" for px, py in pts) + f'" fill="none" stroke="{RED}" stroke-width="2.2"/>'
    b += text(120, 182, "measured record and proxies", 7.6, color=GREY)
    b += text(268, 60, "two fingerprints", 8.6, color=PURPLE, weight="bold")
    b += f'<rect x="210" y="70" width="138" height="42" rx="5" fill="{BF}" stroke="{BLUE}" stroke-width="1.2"/>'
    b += text(279, 84, "with greenhouse gases", 7.6, color=BLUE)
    b += text(279, 96, "troposphere warms,", 7.2, color=INK)
    b += text(279, 106, "stratosphere cools", 7.2, color=INK)
    b += f'<rect x="210" y="118" width="138" height="42" rx="5" fill="{RF}" stroke="{RED}" stroke-width="1.2"/>'
    b += text(279, 132, "with a brighter sun", 7.6, color=RED)
    b += text(279, 144, "both layers warm,", 7.2, color=INK)
    b += text(279, 154, "so this is not it", 7.2, color=INK)
    b += rbox(180, 208, 344, 28,
              "nights warm faster than days, winters faster than summers", PF, PURPLE, 8.4)
    b += foot(246, "Ice cores hold 800 000 years of air; CO2 stayed under 300 ppm.",
              "One cold winter is weather; the thirty-year average is climate.")
    return svg(360, 276, b)


# ------------------------------------------------------------------ 4. sea level
def sea():
    b = heading("Three routes into the same bathtub", "millimetres per year")
    parts = [("thermal expansion", 1.4, ORANGE, "water expands as it warms"),
             ("mountain glaciers", 0.8, TEAL, "Himalaya, Alps, Andes"),
             ("ice sheets", 0.8, BLUE, "Greenland, West Antarctica")]
    y = 66
    for name, mm, col, note in parts:
        b += f'<rect x="12" y="{y}" width="336" height="36" rx="5" fill="#FFFFFF" stroke="{col}" stroke-width="1.3"/>'
        b += text(22, y + 15, name, 8.8, anchor="start", color=col, weight="bold")
        b += text(22, y + 28, note, 7.4, anchor="start", color=GREY)
        b += f'<rect x="196" y="{y + 10}" width="{mm * 46:.0f}" height="14" rx="3" fill="{col}" fill-opacity="0.35" stroke="{col}" stroke-width="0.8"/>'
        b += text(200 + mm * 46, y + 21, f"{mm} mm", 7.8, anchor="start", color=col)
        y += 42
    b += ln(12, y + 6, 348, y + 6, GREY, 1.0, dash="3 2")
    b += text(180, y + 24, "total about 4.5 mm a year, 20 cm since 1900", 8.6, color=INK, weight="bold")
    # basin sketch
    b += f'<rect x="60" y="{y + 44}" width="240" height="34" rx="2" fill="{BF}" stroke="{BLUE}" stroke-width="1.2"/>'
    b += text(180, y + 65, "1 mm of sea level = 361 Gt of water", 7.8, color=BLUE)
    b += foot(y + 100, "Melting sea ice adds nothing: it already floats.",
              "The ice sheets hold enough water for 65 m, and respond over centuries.")
    return svg(360, y + 128, b)


# ------------------------------------------------------------------ 5. impacts
def impacts():
    b = heading("Three mechanisms, one warming", "land, sea and the living world")
    cols = [("land", "hotter, drier soil", ["desertification", "40 % of India degraded", "crop yield down"], ORANGE, 62),
            ("ocean", "warmer and more acidic", ["pH 8.2 -> 8.1", "corals bleach", "shells grow slowly"], TEAL, 180),
            ("life", "ranges and timing shift", ["species move 10 km/decade", "9 % at risk at 1.5 C", "29 % at 3 C"], RED, 298)]
    for name, sub, lines, col, cx in cols:
        b += f'<rect x="{cx - 54}" y="56" width="108" height="106" rx="7" fill="#FFFFFF" stroke="{col}" stroke-width="1.5"/>'
        b += text(cx, 74, name, 9.2, color=col, weight="bold")
        b += text(cx, 88, sub, 7.2, color=GREY)
        for i, t in enumerate(lines):
            b += text(cx, 104 + i * 15, t, 7.2, color=INK)
    b += f'<rect x="8" y="170" width="344" height="34" rx="6" fill="{PF}" stroke="{PURPLE}" stroke-width="1.4"/>'
    b += text(180, 185, "risk = hazard x exposure x vulnerability", 8.4, color=PURPLE, weight="bold")
    b += text(180, 197, "the same heat kills more where people are poor", 7.8, color=INK)
    b += foot(226, "Reefs shelter a quarter of marine species and protect the coast.",
              "Adaptation is local and immediate; mitigation is global and slow.")
    return svg(360, 262, b)


# ------------------------------------------------------------------ 6. mitigation ladder
def mitigation():
    b = heading("Climb from the cheapest rung", "cost per tonne of CO2 avoided, roughly")
    rungs = [("1 save it", "efficiency, LEDs, cool roofs", "pays back on its own", GREEN),
             ("2 electrify it", "heat pumps, buses, two wheelers", "cuts fuel use by 3x", TEAL),
             ("3 clean the supply", "solar, wind, hydro, nuclear", "Rs 2.5 - 3.8 a unit", BLUE),
             ("4 capture the rest", "CCS on cement and steel", "20-30 % energy penalty", PURPLE),
             ("5 offset the last", "forest, soil, direct air", "limited and reversible", ORANGE)]
    y = 58
    for i, (name, how, note, col) in enumerate(rungs):
        x = 12 + i * 14
        w = 348 - x
        b += f'<rect x="{x}" y="{y}" width="{w}" height="34" rx="5" fill="{col}" fill-opacity="0.10" stroke="{col}" stroke-width="1.3"/>'
        b += text(x + 10, y + 15, name, 8.8, anchor="start", color=col, weight="bold")
        b += text(x + 10, y + 28, how, 7.2, anchor="start", color=INK)
        b += text(340, y + 22, note, 7.2, anchor="end", color=GREY)
        y += 40
    b += rbox(180, y + 14, 344, 28,
              "net zero = every rung, plus sinks for what is left", GF, GREEN, 8.4)
    b += foot(y + 46, "The first three rungs can deliver most of the 2030 cut.",
              "An offset is not a substitute for a rung you have not climbed.")
    return svg(360, y + 68, b)


DIAGRAMS = {
    "u4_balance": balance,
    "u4_ghg": ghg,
    "u4_temp": temp,
    "u4_sea": sea,
    "u4_impacts": impacts,
    "u4_mitigation": mitigation,
}
