"""Six compact mobile SVGs for Environmental Sustainability (DI02000051) Unit 2.

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
    "u2_air": "Where air pollution comes from and what it does",
    "u2_control": "Choosing a dust collector by particle size",
    "u2_wwt": "The wastewater treatment train",
    "u2_msw": "The waste hierarchy and where each stream goes",
    "u2_noise": "The decibel scale and the Indian zone limits",
    "u2_ewaste": "What is inside one tonne of e-waste",
}

TITLES_GU = {
    "u2_air": "વાયુ પ્રદૂષણ ક્યાંથી આવે અને શું કરે",
    "u2_control": "કણના કદ પ્રમાણે ધૂળ સંગ્રહકની પસંદગી",
    "u2_wwt": "ગંદા પાણીની સારવારની શૃંખલા",
    "u2_msw": "કચરાનું સોપાન અને દરેક પ્રવાહ ક્યાં જાય",
    "u2_noise": "ડેસિબલ માપક્રમ અને ભારતીય વિસ્તાર મર્યાદા",
    "u2_ewaste": "એક ટન ઇ-કચરામાં શું હોય છે",
}

CAPTIONS = {
    "u2_air": "Vehicles and coal give the gases, construction and burning give the particles; the "
              "health damage is mostly from the invisible fractions.",
    "u2_control": "Coarse dust in a cyclone, fine dust in a bag filter or ESP, and soluble gas in a "
                  "scrubber - match the device to the size.",
    "u2_wwt": "Screens and grit first, then settling, then biology, then polishing; sludge returns to "
              "the start and the dried cake leaves the plant.",
    "u2_msw": "Segregate first: wet waste to compost or biogas, dry waste to recycling or RDF, and "
              "only the inert reject to the landfill.",
    "u2_noise": "3 dB is a doubling of energy, 10 dB sounds twice as loud; the limit depends on the "
                "zone and the time of day.",
    "u2_ewaste": "Half the mass is metal worth recovering; the circuit boards and batteries carry the "
                 "lead, mercury and cadmium.",
}

CAPTIONS_GU = {
    "u2_air": "વાહનો અને કોલસો વાયુઓ આપે, બાંધકામ અને દહન કણ આપે; આરોગ્યને નુકસાન મુખ્યત્વે અદૃશ્ય "
              "ભાગોમાંથી થાય.",
    "u2_control": "જાડી ધૂળ સાયક્લોનમાં, બારીક ધૂળ બેગ ફિલ્ટર કે ESP માં, અને દ્રાવ્ય વાયુ સ્ક્રબરમાં - "
                  "કદ પ્રમાણે સાધન મેળવો.",
    "u2_wwt": "પહેલાં સ્ક્રીન અને ગ્રિટ, પછી સેટલિંગ, પછી જૈવિક, પછી પોલિશિંગ; કાદવ શરૂઆતમાં પાછો જાય અને "
              "સૂકો પિંડ પ્લાન્ટમાંથી નીકળે.",
    "u2_msw": "પહેલાં અલગ કરો: ભીનો કચરો કમ્પોસ્ટ કે બાયોગેસમાં, સૂકો રિસાયકલ કે RDF માં, અને ફક્ત નિષ્ક્રિય "
              "અવશેષ લેન્ડફિલમાં.",
    "u2_noise": "3 dB એટલે ઊર્જા બમણી, 10 dB બમણો સંભળાય; મર્યાદા વિસ્તાર અને દિવસ-રાત્રિ પ્રમાણે બદલાય.",
    "u2_ewaste": "અડધું દળ પુનઃપ્રાપ્ત કરવા લાયક ધાતુ છે; સર્કિટ બોર્ડ અને બેટરીમાં સીસું, પારો અને "
                 "કેડમિયમ હોય છે.",
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


def heading(t, sub=None, size=12.8):
    body = text(180, 21, t, size, weight="bold", color=P)
    if sub:
        body += text(180, 39, sub, 9.6, color=GREY)
    return body


def foot(y, *lines):
    return "".join(text(180, y + 14 * i, s, 9.0, color=GREY) for i, s in enumerate(lines))


# ------------------------------------------------------------------ 1. air pollution
def air():
    b = heading("Sources on the left, effects on the right", "PM2.5 does most of the health damage")
    sources = [("vehicles", "NOx, CO, PM2.5"), ("coal and oil", "SO2, PM2.5, CO2"),
               ("construction", "coarse and fine dust"), ("open burning", "PM2.5, dioxins")]
    effects = [("lungs and heart", "PM2.5, ozone"), ("acid rain", "SO2, NOx"),
               ("smog and haze", "NOx + VOC"), ("climate", "CO2, black carbon")]
    y = 56
    for (s1, s2), (e1, e2) in zip(sources, effects):
        b += f'<rect x="8" y="{y}" width="146" height="34" rx="5" fill="{OF}" stroke="{ORANGE}" stroke-width="1.2"/>'
        b += text(14, y + 14, s1, 9.0, anchor="start", color=INK, weight="bold")
        b += text(14, y + 26, s2, 8.0, anchor="start", color=GREY)
        b += arrow(158, y + 17, 200, y + 17, GREY)
        b += f'<rect x="206" y="{y}" width="146" height="34" rx="5" fill="{RF}" stroke="{RED}" stroke-width="1.2"/>'
        b += text(212, y + 14, e1, 9.0, anchor="start", color=INK, weight="bold")
        b += text(212, y + 26, e2, 8.0, anchor="start", color=GREY)
        y += 42
    b += rbox(180, y + 22, 344, 30,
              "control at the source, collect what is left, never rely on a taller stack",
              TF, TEAL, 8.8)
    b += foot(y + 52, "Primary pollutants are emitted as such; secondary ones form in the air.",
              "A clear plume is not clean air - CO and PM2.5 are invisible.")
    return svg(360, y + 74, b)


# ------------------------------------------------------------------ 2. dust collectors
def control():
    b = heading("Match the collector to the particle", "smaller particles need a finer device")
    rows = [("settling chamber", "50 um and above, about 70 %", GREY),
            ("cyclone separator", "10 - 50 um, about 85 %", TEAL),
            ("bag filter", "1 - 10 um, 99 % plus", BLUE),
            ("electrostatic precipitator", "below 1 um, 99.5 %", PURPLE),
            ("wet scrubber", "dust plus soluble gas, 95 %", GREEN)]
    y = 56
    for i, (name, spec, col) in enumerate(rows):
        fill = "#FFFFFF" if i % 2 == 0 else "#F7F7F7"
        b += f'<rect x="12" y="{y}" width="336" height="28" rx="4" fill="{fill}" stroke="{col}" stroke-width="1.3"/>'
        b += text(20, y + 18, name, 8.9, anchor="start", color=INK, weight="bold")
        b += text(340, y + 18, spec, 8.2, anchor="end", color=col)
        y += 36
    b += rbox(180, y + 14, 344, 30,
              "gas too hot, wet or corrosive? a scrubber cools and absorbs in one step", GF, GREEN, 8.6)
    b += foot(y + 46, "A cyclone is a pre-cleaner; a bag filter or ESP is the final stage.",
              "Check the pressure drop and where the collected dust will go.")
    return svg(360, y + 68, b)


# ------------------------------------------------------------------ 3. wastewater train
def wwt():
    b = heading("Screens, settling, biology, polishing", "each stage protects the one after it")
    boxes = [(72, "raw sewage", "screen, grit, oil trap", GREY),
             (124, "primary clarifier", "TSS down 50-65 %", TEAL),
             (176, "aeration tank", "bacteria eat the organics", BLUE),
             (228, "secondary clarifier", "sludge settles", TEAL),
             (280, "tertiary + disinfection", "nutrients, colour, germs", GREEN)]
    for cy, name, sub, col in boxes:
        b += f'<rect x="30" y="{cy-20}" width="300" height="40" rx="6" fill="#F7F9FC" stroke="{col}" stroke-width="1.4"/>'
        b += text(180, cy - 3, name, 9.6, color=INK, weight="bold")
        b += text(180, cy + 10, sub, 8.2, color=GREY)
    for cy in (92, 144, 196, 248):
        b += arrow(180, cy, 180, cy + 12, GREY)
    b += arrow(180, 300, 180, 318, GREEN)
    b += text(188, 316, "to river or reuse", 8.4, color=GREEN, anchor="start")
    b += rbox(180, 344, 344, 26, "30-50 % of the settled sludge returns to the aeration tank",
              OF, ORANGE, 8.6)
    b += foot(386, "BOD 300 mg/L comes in, about 20 mg/L goes out.",
              "UASB replaces the aeration tank where the waste is warm and strong.")
    return svg(360, 412, b)


# ------------------------------------------------------------------ 4. waste hierarchy
def msw():
    b = heading("The hierarchy decides the route", "segregation at source makes it possible")
    steps = [("1 refuse and reduce", "buy less, design out the waste", GREEN),
             ("2 reuse", "bottles, crates, refills", TEAL),
             ("3 recycle", "paper, metal, glass, PET", BLUE),
             ("4 recover", "compost, biogas, RDF, heat", ORANGE),
             ("5 dispose", "sanitary landfill, inert only", RED)]
    y = 54
    for i, (name, sub, col) in enumerate(steps):
        w = 336 - i * 26
        b += f'<rect x="{180 - w/2}" y="{y}" width="{w}" height="30" rx="5" fill="#FFFFFF" stroke="{col}" stroke-width="1.5"/>'
        b += text(180, y + 13, name, 9.4, color=col, weight="bold")
        b += text(180, y + 25, sub, 8.0, color=GREY)
        y += 38
    b += arrow(348, 60, 348, y - 16, GREY)
    b += rbox(180, y + 18, 344, 26, "wet 55 % to compost, dry 30 % to recycling or RDF", TF, TEAL, 8.8)
    b += foot(y + 48, "Only the inert reject should reach the landfill.",
              "Mixed waste goes nowhere useful - it can only be dumped.")
    return svg(360, y + 70, b)


# ------------------------------------------------------------------ 5. noise scale
def noise():
    b = heading("Decibels grow by powers of ten", "add 3 dB for a doubling of energy")
    y0, y1 = 62, 250
    b += ln(60, y0, 60, y1, INK, 1.4)
    for lvl, label in ((0, "0"), (20, "20"), (40, "40"), (60, "60"), (80, "80"), (100, "100"),
                       (120, "120")):
        yy = y1 - (lvl - 0) / 120 * (y1 - y0)
        b += ln(56, yy, 64, yy, INK, 1.2)
        b += text(50, yy + 3, label, 8.2, anchor="end", color=GREY)
    marks = [(20, "leaves", GREEN), (60, "conversation", TEAL), (80, "busy road", ORANGE),
             (95, "factory floor", RED), (120, "jet at 50 m", RED)]
    for lvl, label, col in marks:
        yy = y1 - (lvl - 0) / 120 * (y1 - y0)
        b += ln(64, yy, 200, yy, col, 1.2, dash="3 2")
        b += text(206, yy + 3, f"{label} - {lvl} dB", 8.6, anchor="start", color=col)
    b += rbox(180, 268, 344, 26,
              "day limits: 50 silence, 55 home, 65 market, 75 industry", PF, PURPLE, 8.6)
    b += foot(296, "Hearing is at risk above 85 dB for 8 hours; night limits are 5 dB lower.",
              "Control at the source, then along the path, then at the ear.")
    return svg(360, 320, b)


# ------------------------------------------------------------------ 6. e-waste
def ewaste():
    b = heading("One tonne of e-waste, by mass", "the small fractions carry the hazard")
    parts = [("metal", 500, "worth recovering", GREY),
             ("plastic", 210, "flame retardants", ORANGE),
             ("glass and ceramic", 130, "screens, boards", TEAL),
             ("circuit boards", 60, "lead, gold, beryllium", RED),
             ("cables and other", 70, "copper if stripped", BLUE),
             ("batteries and lamps", 30, "mercury, cadmium, lithium", RED)]
    x = 16
    total = sum(p[1] for p in parts)
    h0, hmax = 130, 40
    for name, kg, note, col in parts:
        w = 328 * kg / total
        b += f'<rect x="{x:.1f}" y="70" width="{w - 2:.1f}" height="34" fill="{col}" fill-opacity="0.25" stroke="{col}" stroke-width="1.2"/>'
        if w > 62:
            b += text(x + w / 2, 90, f"{kg} kg", 8.6, color=col, weight="bold")
        x += w
    y = 122
    for name, kg, note, col in parts:
        b += f'<rect x="16" y="{y - 9}" width="4" height="14" fill="{col}"/>'
        b += text(26, y, name, 8.8, anchor="start", color=INK, weight="bold")
        b += text(160, y, note, 8.2, anchor="start", color=GREY)
        b += text(344, y, f"{kg * 100 // total} %", 8.6, anchor="end", color=col)
        y += 24
    b += rbox(180, y + 8, 344, 28,
              "burning cables and acid baths release dioxins and lead over the workers",
              RF, RED, 8.6)
    b += foot(y + 38, "Hand it to an authorised recycler against a manifest.",
              "Extended producer responsibility pays for the take-back.")
    return svg(360, y + 60, b)


DIAGRAMS = {
    "u2_air": air,
    "u2_control": control,
    "u2_wwt": wwt,
    "u2_msw": msw,
    "u2_noise": noise,
    "u2_ewaste": ewaste,
}
