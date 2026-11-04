"""Six compact mobile SVGs for Environmental Sustainability (DI02000051) Unit 5.

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
    "u5_law": "From an Act of Parliament to a consent order",
    "u5_iso": "ISO 14001 as a plan-do-check-act loop",
    "u5_rwh": "Rain water harvesting: roof to recharge pit",
    "u5_credits": "From a project to a retired carbon credit",
    "u5_5r": "The 5R ladder, refuse first, recycle last",
    "u5_eco": "The three tests of eco tourism",
}

TITLES_GU = {
    "u5_law": "સંસદના અધિનિયમથી સંમતિના આદેશ સુધી",
    "u5_iso": "આયોજન-અમલ-તપાસ-સુધારો ચક્ર તરીકે ISO 14001",
    "u5_rwh": "વરસાદી જળ સંગ્રહ: છતથી ભરાવ ખાડા સુધી",
    "u5_credits": "પ્રોજેક્ટથી રદ થયેલી કાર્બન ક્રેડિટ સુધી",
    "u5_5r": "5R સોપાન, પહેલાં નકારો, છેલ્લે રિસાયકલ",
    "u5_eco": "પર્યાવરણ પર્યટનની ત્રણ કસોટી",
}

CAPTIONS = {
    "u5_law": "Parliament sets the duty, the ministry sets the number, the board grants the consent - "
              "and the tribunal hears the complaint.",
    "u5_iso": "Plan, do, check, act: the certificate says the loop is running, not that the emissions "
              "are low.",
    "u5_rwh": "Catch it, clean it, store it, and let the surplus recharge the ground instead of the "
              "drain.",
    "u5_credits": "Measure against a baseline, verify, issue, sell, retire - and watch additionality, "
                  "permanence and leakage.",
    "u5_5r": "Every step down the ladder needs more energy and more market; refuse needs neither.",
    "u5_eco": "Conservation, local benefit and education together; a capacity that exists only on paper "
              "is not a capacity.",
}

CAPTIONS_GU = {
    "u5_law": "સંસદ ફરજ નક્કી કરે, મંત્રાલય આંકડો નક્કી કરે, બોર્ડ સંમતિ આપે - અને ટ્રિબ્યુનલ ફરિયાદ સાંભળે.",
    "u5_iso": "આયોજન, અમલ, તપાસ, સુધારો: પ્રમાણપત્ર કહે કે ચક્ર ચાલે છે, એ નહીં કે ઉત્સર્જન ઓછું છે.",
    "u5_rwh": "પકડો, સાફ કરો, સંગ્રહો, અને વધારાનું ગટરને બદલે જમીનમાં ભરાવા દો.",
    "u5_credits": "આધાર રેખા સામે માપો, ચકાસો, આપો, વેચો, રદ કરો - અને અતિરિક્તતા, ટકાઉપણું તથા લીકેજ જુઓ.",
    "u5_5r": "સોપાનમાં નીચે દરેક પગથિયાને વધુ ઊર્જા અને વધુ બજાર જોઈએ; નકારવાને કંઈ જ નહીં.",
    "u5_eco": "સંરક્ષણ, સ્થાનિક લાભ અને શિક્ષણ સાથે; ફક્ત કાગળ પરની ક્ષમતા ક્ષમતા નથી.",
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


# ------------------------------------------------------------------ 1. law to consent
def law():
    b = heading("The chain from statute to compliance", "who does what, in that order")
    rows = [("Parliament - the Act", "Water 1974, Air 1981, EP Act 1986 umbrella", PURPLE),
            ("MoEFCC - rules and standards", "EIA 2006, waste rules, emission limits", BLUE),
            ("SPCB - consent to establish", "site, process and planned control checked", TEAL),
            ("SPCB - consent to operate", "quantity, quality, monitoring, conditions", GREEN)]
    y = 56
    for i, (name, note, col) in enumerate(rows):
        b += f'<rect x="22" y="{y}" width="316" height="36" rx="6" fill="#FFFFFF" stroke="{col}" stroke-width="1.5"/>'
        b += text(180, y + 15, name, 8.8, color=col, weight="bold")
        b += text(180, y + 28, note, 7.4, color=INK)
        if i < len(rows) - 1:
            b += arrow(180, y + 36, 180, y + 46, GREY, 1.2)
        y += 47
    b += f'<rect x="8" y="{y}" width="344" height="28" rx="6" fill="{PF}" stroke="{PURPLE}" stroke-width="1.4"/>'
    b += text(180, y + 18, "NGT 2010: appeal, compensation, restitution", 8.2, color=PURPLE, weight="bold")
    b += foot(y + 46, "An Act gives power, a rule gives a number, a consent gives permission.",
              "Working outside a consent is an offence, not a paperwork issue.")
    return svg(360, y + 70, b)


# ------------------------------------------------------------------ 2. ISO 14001 PDCA
def iso():
    b = heading("Four steps, repeated, never finished", "ISO 14001: the system, not the score")
    quads = [("P - Plan", ["aspects and impacts", "legal register", "objectives, targets"], BLUE, 10, 56),
             ("D - Do", ["roles and training", "operating procedures", "emergency drills"], GREEN, 200, 56),
             ("C - Check", ["monitor and measure", "calibrate, audit", "record non-conformity"], ORANGE, 200, 132),
             ("A - Act", ["fix the root cause", "update the risk score", "review and re-plan"], PURPLE, 10, 132)]
    for name, lines, col, x, y in quads:
        b += f'<rect x="{x}" y="{y}" width="150" height="64" rx="7" fill="#FFFFFF" stroke="{col}" stroke-width="1.5"/>'
        b += text(x + 75, y + 16, name, 8.8, color=col, weight="bold")
        for i, s in enumerate(lines):
            b += text(x + 75, y + 31 + i * 12, s, 7.2, color=INK)
    b += arrow(162, 88, 198, 88, GREY, 1.3)
    b += arrow(275, 120, 275, 132, GREY, 1.3)
    b += arrow(198, 164, 162, 164, GREY, 1.3)
    b += arrow(85, 132, 85, 120, GREY, 1.3)
    b += text(180, 108, "PDCA", 8.4, color=GREY, weight="bold")
    b += f'<rect x="8" y="206" width="344" height="28" rx="6" fill="{TF}" stroke="{TEAL}" stroke-width="1.4"/>'
    b += text(180, 224, "aspect > impact > significant > objective", 8.2, color=TEAL, weight="bold")
    b += foot(252, "The certificate audits the system; it does not measure the emissions.",
              "A certified plant with weak targets is still a polluting plant.")
    return svg(360, 288, b)


# ------------------------------------------------------------------ 3. rain water harvesting
def rwh():
    b = heading("Five stages from the terrace to the ground", "a school roof of 800 m2")
    rows = [("1 roof catchment", "800 m2 terrace, sloping to four outlets", BLUE),
            ("2 gutter and first flush", "mesh strainer; the first 2 mm is thrown away", TEAL),
            ("3 filter", "sand, gravel and a charcoal layer", GREEN),
            ("4 storage tank", "40 m3 RCC, mosquito-proof cover, overflow pipe", ORANGE),
            ("5 recharge pit", "3 m x 3 m of boulders, gravel and sand", PURPLE)]
    y = 54
    for i, (name, note, col) in enumerate(rows):
        b += f'<rect x="14" y="{y}" width="332" height="34" rx="6" fill="#FFFFFF" stroke="{col}" stroke-width="1.4"/>'
        b += text(24, y + 14, name, 8.6, anchor="start", color=col, weight="bold")
        b += text(24, y + 27, note, 7.4, anchor="start", color=INK)
        if i < len(rows) - 1:
            b += arrow(180, y + 34, 180, y + 41, GREY, 1.2)
        y += 41
    b += f'<rect x="8" y="{y}" width="344" height="28" rx="6" fill="{GF}" stroke="{GREEN}" stroke-width="1.4"/>'
    b += text(180, y + 12, "V = roof area x rain x runoff coefficient", 8.2, color=GREEN, weight="bold")
    b += text(180, y + 23, "800 x 1.0 m x 0.85 = 680 m3, about 6,80,000 litres a year", 7.2, color=INK)
    b += foot(y + 44, "Store what the school needs, recharge the rest into the aquifer.",
              "A tank that is not cleaned is a mosquito farm, not a water source.")
    return svg(360, y + 68, b)


# ------------------------------------------------------------------ 4. carbon credits
def credits():
    b = heading("Follow one tonne of CO2e through the market", "who measures, who pays")
    chips = [("1 the project", ["cuts beyond law"], 14, BLUE),
             ("2 the verifier", ["checks baseline"], 128, TEAL),
             ("3 one credit", ["= 1 t CO2e"], 242, PURPLE)]
    for name, sub, x, col in chips:
        b += f'<rect x="{x}" y="56" width="104" height="42" rx="6" fill="#FFFFFF" stroke="{col}" stroke-width="1.5"/>'
        b += text(x + 52, 72, name, 8.4, color=col, weight="bold")
        b += text(x + 52, 86, sub[0], 7.2, color=INK)
    b += arrow(118, 77, 128, 77, GREY, 1.2)
    b += arrow(232, 77, 242, 77, GREY, 1.2)
    b += f'<rect x="8" y="108" width="344" height="32" rx="6" fill="{GF}" stroke="{GREEN}" stroke-width="1.4"/>'
    b += text(180, 122, "the buyer pays, then the credit is retired", 8.2, color=GREEN, weight="bold")
    b += text(180, 134, "one credit, one owner, one use - then cancelled", 7.4, color=INK)
    cols = [("what it gains", ["cheapest cut first", "private money", "a tradeable unit"], GREEN, 10),
            ("what it risks", ["additionality", "permanence, leakage", "double counting"], RED, 186)]
    for name, lines, col, x in cols:
        b += f'<rect x="{x}" y="150" width="164" height="86" rx="6" fill="#FFFFFF" stroke="{col}" stroke-width="1.4"/>'
        b += text(x + 82, 166, name, 8.2, color=col, weight="bold")
        for i, s in enumerate(lines):
            b += text(x + 82, 184 + i * 14, s, 7.2, color=INK)
    b += foot(252, "A credit for what would have happened anyway is a payment.",
              "Use the market last: cut your own emissions, then offset what is left.")
    return svg(360, 292, b)


# ------------------------------------------------------------------ 5. the 5R ladder
def five_r():
    b = heading("Prefer the top rung whenever you can", "each rung down costs energy and market")
    rungs = [("1 Refuse", "say no to the bag, the straw, the sampler", "no waste at all", GREEN),
             ("2 Reduce", "five-star AC, bucket bath, half the print", "less per use", TEAL),
             ("3 Reuse", "steel bottle, refill pack, returnable crate", "same object, many uses", BLUE),
             ("4 Repurpose", "tyre planter, tub storage, crate shelf", "new job, no remaking", ORANGE),
             ("5 Recycle", "paper, metal, glass and PET to a recycler", "energy is spent", PURPLE)]
    y = 56
    for i, (name, how, note, col) in enumerate(rungs):
        x = 12 + i * 14
        w = 348 - x
        b += (f'<rect x="{x}" y="{y}" width="{w}" height="34" rx="5" fill="{col}" fill-opacity="0.10" '
              f'stroke="{col}" stroke-width="1.3"/>')
        b += text(x + 10, y + 15, name, 8.8, anchor="start", color=col, weight="bold")
        b += text(x + 10, y + 28, how, 7.2, anchor="start", color=INK)
        b += text(338, y + 22, note, 6.8, anchor="end", color=GREY)
        y += 40
    b += rbox(180, y + 14, 344, 28, "the top three rungs need no energy and no market", GF, GREEN, 8.4)
    b += foot(y + 44, "Segregate at the source: mixed waste cannot be recycled, only dumped.",
              "The fifth rung is the last resort, not the first plan.")
    return svg(360, y + 68, b)


# ------------------------------------------------------------------ 6. eco tourism
def eco():
    b = heading("All three, or it is just mass tourism", "the tests a site has to pass")
    cols = [("conserves", ["fee funds the", "trail and the reef", "capacity is set"], GREEN, 10),
            ("benefits locals", ["guides, homestays,", "craft and produce", "money stays here"], BLUE, 128),
            ("educates", ["interpretation", "boards, and a", "guide who explains"], ORANGE, 246)]
    for name, lines, col, x in cols:
        b += f'<rect x="{x}" y="56" width="104" height="92" rx="7" fill="#FFFFFF" stroke="{col}" stroke-width="1.5"/>'
        b += text(x + 52, 74, name, 8.4, color=col, weight="bold")
        for i, s in enumerate(lines):
            b += text(x + 52, 92 + i * 14, s, 7.2, color=INK)
    b += f'<rect x="8" y="160" width="344" height="30" rx="6" fill="{TF}" stroke="{TEAL}" stroke-width="1.4"/>'
    b += text(180, 174, "carrying capacity = visitors a day the place can absorb", 8.0, color=TEAL, weight="bold")
    b += text(180, 185, "enforced by permits, a closed day and a peak-season fee", 7.2, color=INK)
    b += foot(206, "Greenwashing, leakage to enclave resorts and sewage are the usual failures.",
              "A village committee that keeps the gate fee keeps the forest.")
    return svg(360, 244, b)


DIAGRAMS = {
    "u5_law": law,
    "u5_iso": iso,
    "u5_rwh": rwh,
    "u5_credits": credits,
    "u5_5r": five_r,
    "u5_eco": eco,
}
