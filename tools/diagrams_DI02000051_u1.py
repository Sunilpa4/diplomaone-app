"""Five compact mobile SVGs for Environmental Sustainability (DI02000051) Unit 1: sustainability,
ecosystems, natural cycles and biodiversity.

All labels stay in English (like every bilingual subject in the app) and each canvas is 360 px wide.
Every drawing is built from plain rect/path/text, so the app needs no markers or CSS.
"""
from flowchart_lib import svg, text, rbox, P

BLUE, BF = "#1565C0", "#EAF3FD"
GREEN, GF = "#2E7D32", "#EAF6EC"
ORANGE, OF = "#B66A00", "#FFF4DF"
RED, RF = "#BD2543", "#FDECF0"
PURPLE, PF = "#7B2CD9", "#F3EBFD"
GREY = "#666"
INK = "#222"

TITLES = {
    "u1_pillars": "Three pillars carry one idea",
    "u1_ecosystem": "The trophic pyramid of a pond",
    "u1_energy": "Ten per cent passes, ninety per cent is lost",
    "u1_carbon": "Where the carbon goes",
    "u1_nitrogen": "Five steps of the nitrogen cycle",
}

TITLES_GU = {
    "u1_pillars": "ત્રણ સ્તંભ એક વિચારને ટકાવે",
    "u1_ecosystem": "તળાવનો પોષણ પિરામિડ",
    "u1_energy": "દસ ટકા પસાર થાય, નેવું ટકા ખર્ચાય",
    "u1_carbon": "કાર્બન ક્યાં જાય છે",
    "u1_nitrogen": "નાઇટ્રોજન ચક્રનાં પાંચ પગલાં",
}

CAPTIONS = {
    "u1_pillars": "A project is sustainable only when the environment, society and the economy all "
                  "hold together.",
    "u1_ecosystem": "Width shows how much energy and how many organisms each level holds.",
    "u1_energy": "Each step keeps about a tenth, so a food chain runs out of energy after four "
                 "or five levels.",
    "u1_carbon": "Fossil carbon is the one arrow with no way back, which is why the air is "
                 "filling up.",
    "u1_nitrogen": "N₂ is inert until bacteria, lightning or a fertiliser plant break the triple "
                   "bond.",
}

CAPTIONS_GU = {
    "u1_pillars": "પર્યાવરણ, સમાજ અને અર્થતંત્ર - ત્રણેય સાથે ટકે તો જ પ્રોજેક્ટ ટકાઉ.",
    "u1_ecosystem": "પહોળાઈ દર્શાવે કે દરેક સ્તરમાં કેટલી ઊર્જા અને કેટલા જીવ છે.",
    "u1_energy": "દરેક પગથિયે લગભગ દશમાંશ બચે, તેથી ચાર-પાંચ સ્તર પછી ખોરાક શૃંખલાની ઊર્જા ખતમ થાય.",
    "u1_carbon": "અશ્મિ કાર્બન એ એકમાત્ર એવું તીર છે જે પાછું વળે નહીં, તેથી જ હવા ભરાય છે.",
    "u1_nitrogen": "જીવાણુ, વીજળી કે ખાતર કારખાનું ત્રિબંધ તોડે ત્યાં સુધી N₂ નિષ્ક્રિય રહે.",
}


def ln(x1, y1, x2, y2, color=INK, w=1.2, dash=None):
    da = f' stroke-dasharray="{dash}"' if dash else ""
    return (f'<path d="M{x1} {y1}L{x2} {y2}" fill="none" stroke="{color}" stroke-width="{w}" '
            f'stroke-linecap="round"{da}/>')


def arrow(x1, y1, x2, y2, color=INK, w=1.5):
    """A straight arrow with a solid head at (x2, y2)."""
    dx, dy = x2 - x1, y2 - y1
    d = (dx * dx + dy * dy) ** 0.5 or 1
    ux, uy = dx / d, dy / d
    bx, by = x2 - 7 * ux, y2 - 7 * uy
    px, py = -uy * 4, ux * 4
    head = (f'<path d="M{x2} {y2}L{bx + px} {by + py}L{bx - px} {by - py}Z" fill="{color}"/>')
    return ln(x1, y1, bx, by, color, w) + head


def heading(t, sub=None, size=13.0):
    body = text(180, 21, t, size, weight="bold", color=P)
    if sub:
        body += text(180, 40, sub, 9.6, color=GREY)
    return body


def foot(y, *lines):
    return "".join(text(180, y + 14 * i, s, 9.2, color=GREY) for i, s in enumerate(lines))


# ------------------------------------------------------------------ 1. three pillars
def pillars():
    b = heading("Three pillars carry one idea", "environment · society · economy")
    b += rbox(72, 62, 112, 34, "environment", BF, BLUE, 9.4)
    b += text(72, 90, "air · water · soil", 8.4, color=GREY)
    b += rbox(288, 62, 112, 34, "society", GF, GREEN, 9.4)
    b += text(288, 90, "health · equity", 8.4, color=GREY)
    b += rbox(180, 226, 132, 34, "economy", OF, ORANGE, 9.4)
    b += text(180, 254, "cost · jobs · payback", 8.4, color=GREY)
    b += f'<circle cx="180" cy="152" r="44" fill="{PF}" stroke="{P}" stroke-width="1.6"/>'
    b += text(180, 146, "sustain-", 10.2, weight="bold", color=P)
    b += text(180, 162, "ability", 10.2, weight="bold", color=P)
    b += arrow(112, 92, 148, 128, "#999", 1.4)
    b += arrow(248, 92, 212, 128, "#999", 1.4)
    b += arrow(180, 209, 180, 198, "#999", 1.4)
    b += foot(272, "Two pillars only = a weak project.", "All three = sustainability.")
    return svg(360, 300, b)


# ------------------------------------------------------------------ 2. trophic pyramid
def ecosystem():
    b = heading("The trophic pyramid of a pond", "numbers and energy shrink upwards")
    rows = [(198, 300, "producers: algae, plants", GF, GREEN),
            (164, 236, "primary consumers: zooplankton", BF, BLUE),
            (130, 172, "secondary: small fish", OF, ORANGE),
            (96, 112, "top consumer: heron", RF, RED)]
    for cy, w, label, fill, stroke in rows:
        b += rbox(180, cy, w, 30, label, fill, stroke, 8.8)
    b += arrow(18, 196, 18, 86, "#999", 1.5)
    b += foot(244, "Energy flows up the pyramid, about 10 % a step,",
              "so it must be wide at the bottom and narrow",
              "at the top - the heron needs many fish.")
    return svg(360, 288, b)


# ------------------------------------------------------------------ 3. energy loss
def energy():
    b = heading("Ten per cent passes, ninety per cent is lost", "the rest leaves as heat")
    rows = [(64, "producers", "100 %", GF, GREEN),
            (114, "herbivores", "10 %", BF, BLUE),
            (164, "carnivores", "1 %", OF, ORANGE),
            (214, "top carnivore", "0.1 %", RF, RED)]
    for cy, label, pct, fill, stroke in rows:
        b += rbox(86, cy, 128, 32, f"{label}  {pct}", fill, stroke, 8.8)
        b += arrow(156, cy, 214, cy, "#B66A00", 1.4)
        b += text(268, cy - 2, "-90 %", 9.0, color=ORANGE, weight="bold")
        b += text(268, cy + 11, "heat", 8.4, color=GREY)
    b += foot(252, "Check: 100 % -> 10 % -> 1 % -> 0.1 %", "Overall efficiency = 0.1 / 100 = 0.1 %.")
    return svg(360, 288, b)


# ------------------------------------------------------------------ 4. carbon cycle
def carbon():
    b = heading("Where the carbon goes", "air, life, soil, sea and fossil rock")
    b += rbox(180, 66, 180, 32, "atmosphere CO2", BF, BLUE, 9.2)
    b += rbox(88, 134, 104, 42, "plants\nphotosynthesis", GF, GREEN, 8.6)
    b += rbox(272, 134, 96, 42, "animals\nrespiration", OF, ORANGE, 8.6)
    b += rbox(44, 222, 84, 36, "ocean\ndissolves CO2", "#E6F4F7", "#087F8C", 8.2)
    b += rbox(180, 222, 104, 40, "soil and\ndecomposers", "#EFEFEF", "#888", 8.4)
    b += rbox(316, 222, 84, 36, "fossil fuel\n+ cement", RF, RED, 8.2)
    # photosynthesis
    b += arrow(152, 80, 106, 112, "#999", 1.4)
    b += text(64, 98, "photosynthesis", 8.2, color=GREY)
    # feeding
    b += arrow(142, 134, 222, 134, "#999", 1.4)
    b += text(182, 126, "feeding", 8.2, color=GREY)
    # respiration
    b += arrow(250, 112, 208, 84, "#999", 1.4)
    b += text(302, 100, "respiration", 8.2, color=GREY)
    # litter and waste
    b += arrow(72, 154, 122, 202, "#999", 1.4)
    b += text(30, 178, "litter + death", 8.2, color=GREY, anchor="start")
    b += arrow(288, 154, 238, 202, "#999", 1.4)
    b += text(332, 178, "waste", 8.2, color=GREY, anchor="end")
    # decomposition up the middle
    b += arrow(180, 202, 180, 84, "#999", 1.4)
    b += text(190, 152, "CO2", 8.2, color=GREY, anchor="start")
    # ocean exchange up the left margin
    b += ln(16, 204, 16, 94, "#087F8C", 1.3, "4 3")
    b += arrow(16, 94, 88, 80, "#087F8C", 1.3)
    # fossil carbon up the right margin
    b += ln(344, 204, 344, 94, RED, 1.5, "4 3")
    b += arrow(344, 94, 272, 80, RED, 1.5)
    b += text(316, 196, "burning", 8.2, color=RED)
    b += foot(252, "Fossil carbon has no way back into the ground,",
              "so the air fills up a little every year;",
              "the ocean absorbs about a quarter of it.")
    return svg(360, 300, b)


# ------------------------------------------------------------------ 5. nitrogen cycle
def nitrogen():
    b = heading("Five steps of the nitrogen cycle", "N2 -> NH3 -> NO3- -> life -> N2")
    b += rbox(56, 84, 100, 38, "N2 in air\n78 %", BF, BLUE, 8.8)
    b += rbox(180, 84, 104, 38, "fixation\nNH3 / NH4+", GF, GREEN, 8.6)
    b += rbox(304, 84, 100, 38, "nitrification\nNO3-", OF, ORANGE, 8.6)
    b += rbox(304, 186, 100, 38, "plants absorb", GF, GREEN, 8.8)
    b += rbox(180, 186, 104, 38, "animals eat", OF, ORANGE, 8.8)
    b += rbox(56, 186, 100, 38, "decomposers\nback to NH3", "#EFEFEF", "#888", 8.6)
    b += arrow(108, 84, 126, 84, "#999", 1.4)
    b += arrow(234, 84, 252, 84, "#999", 1.4)
    b += arrow(304, 105, 304, 165, "#999", 1.4)
    b += arrow(252, 186, 234, 186, "#999", 1.4)
    b += arrow(126, 186, 108, 186, "#999", 1.4)
    b += arrow(24, 165, 24, 105, RED, 1.6)
    b += text(32, 138, "de-nitrification", 8.0, color=RED, anchor="start")
    b += foot(232, "Bacteria, lightning or the Haber-Bosch plant do the fixing;",
              "excess nitrate washes out and causes eutrophication;",
              "nitrous oxide from soil is a strong greenhouse gas.")
    return svg(360, 292, b)


DIAGRAMS = {
    "u1_pillars": pillars,
    "u1_ecosystem": ecosystem,
    "u1_energy": energy,
    "u1_carbon": carbon,
    "u1_nitrogen": nitrogen,
}


def main():
    from pathlib import Path
    out = Path(__file__).resolve().parent.parent / "content/common/sem2/DI02000051/diagrams"
    out.mkdir(parents=True, exist_ok=True)
    for key, fn in DIAGRAMS.items():
        (out / f"{key}.svg").write_text(fn(), encoding="utf-8")
        print("wrote", key)


if __name__ == "__main__":
    main()
