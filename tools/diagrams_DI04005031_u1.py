"""Draws the diagrams for DI04005031 Unit 1 "Introduction to Pollution and its Impact".

    python3 tools/diagrams_DI04005031_u1.py

Original teaching schematics. Sources: C. S. Rao, Environmental Pollution Control
Engineering; S. P. Mahajan, Pollution Control in Process Industries; CPCB / GPCB
standards.
"""
import d1chem_lib as L
from d1draw import (AMBER, AMBER_FILL, BLUE, BLUE_FILL, Canvas, GREEN, GREEN_FILL, GREY_FILL,
                    INK, LAV, LINE, MUTED, P, PD, RED, RED_FILL, save)

CODE, BRANCH, SEM = "DI04005031", "chemical", 4


def _p(name):
    return L.out_path(BRANCH, SEM, CODE, name)


# ------------------------------------------------------------------ 1.1 sources of pollution
def sources_of_pollution():
    c = Canvas(980, 650, "Five sources of pollution, and how each one travels")
    kinds = [
        ("AIR", 30, RED, "stack gas, dust, SO₂"),
        ("WATER", 220, BLUE, "effluent, sewage"),
        ("LAND", 410, AMBER, "dumping, sludge"),
        ("NOISE", 600, GREEN, "machines, traffic"),
        ("RADIOACTIVE", 790, PD, "isotopes, nuclear"),
    ]
    for name, x, col, sub in kinds:
        c.rbox(x, 96, 160, 58, "", "#FFFFFF", col, rx=8)
        c.text(x + 80, 118, name, 12.5, "middle", col, "bold")
        c.text(x + 80, 138, sub, 9.5, "middle", MUTED)
        c.arrow(x + 80, 156, x + 80, 190, col, 2)

    # receiving media row
    c.rbox(30, 200, 920, 56, "", GREY_FILL, LINE, rx=10)
    c.text(490, 220, "RECEIVING ENVIRONMENT  —  air · water · soil", 12.5, "middle", PD, "bold")
    c.text(490, 240, "the pollutant is diluted, transported and sometimes chemically changed on the way",
           10.5, "middle", MUTED)

    # three arrows down to impact
    for x in (170, 490, 810):
        c.arrow(x, 256, x, 300, PD, 2.2)

    c.title_band("WHO IS EXPOSED", 292)
    groups = [("HUMANS", 30, RED, "respiratory and water-borne disease"),
              ("PLANTS", 260, GREEN, "leaf damage, lower yield"),
              ("ANIMALS", 490, AMBER, "bioaccumulation up the food chain"),
              ("MATERIALS", 720, BLUE, "corrosion, soiling, stone decay")]
    for name, x, col, sub in groups:
        c.rbox(x, 310, 210, 62, "", "#FFFFFF", col, rx=8)
        c.text(x + 105, 333, name, 12, "middle", col, "bold")
        c.text(x + 105, 354, sub, 9.5, "middle", MUTED)

    c.title_band("THE FOUR ROUTES INTO THE BODY", 402)
    c.text(30, 432, "inhalation", 11.5, "start", RED, "bold")
    c.text(130, 432, "→ lungs, the fastest route: gases and particles below 10 μm reach the alveoli",
           11, "start", INK)
    c.text(30, 458, "ingestion", 11.5, "start", BLUE, "bold")
    c.text(130, 458, "→ drinking water, food, and hand-to-mouth dust",
           11, "start", INK)
    c.text(30, 484, "dermal contact", 11.5, "start", AMBER, "bold")
    c.text(130, 484, "→ absorption through skin, mainly solvents and pesticides",
           11, "start", INK)
    c.text(30, 510, "radiation", 11.5, "start", PD, "bold")
    c.text(130, 510, "→ ionising dose from external exposure or inhaled radon",
           11, "start", INK)

    c.title_band("ONE POLLUTANT, MANY PATHS", 548)
    c.text(30, 578, "A pollutant released to air settles on land, is washed into water, enters crops and",
           11.5, "start", INK)
    c.text(30, 600, "returns to people — so control belongs at the source, never at the victim.",
           11.5, "start", INK)
    c.footer()
    return c


# ------------------------------------------------------------------ 1.2 classification tree
def pollutant_classification():
    c = Canvas(980, 680, "Classifying pollutants three ways")
    # root
    c.rbox(390, 78, 200, 46, "", LAV, P, rx=8)
    c.text(490, 101, "POLLUTANT", 14, "middle", PD, "bold")

    cols = [
        ("BY ORIGIN", 40, RED, [("Primary", "released as it is: CO, dust, SO₂"),
                                ("Secondary", "formed in air: ozone, PAN, acid mist")]),
        ("BY NATURE", 350, BLUE, [("Physical", "heat, noise, radiation, sediment"),
                                  ("Chemical", "gases, acids, heavy metals, salts"),
                                  ("Biological", "bacteria, virus, algae")]),
        ("BY MEDIUM", 660, GREEN, [("Air", "gases and particles in the atmosphere"),
                                   ("Water", "effluent discharged to a water body"),
                                   ("Land", "solid and hazardous waste")]),
    ]
    for head, x, col, kids in cols:
        c.arrow(490, 126, x + 140, 168, LINE, 1.6)
        c.rbox(x, 170, 280, 40, "", col, "none", rx=6)
        c.text(x + 140, 190, head, 11.5, "middle", "#FFFFFF", "bold")
        y = 220
        for name, desc in kids:
            c.rbox(x, y, 280, 66, "", "#FFFFFF", col, rx=6)
            c.text(x + 14, y + 24, name, 11.5, "start", col, "bold")
            c.text(x + 14, y + 46, desc, 10, "start", MUTED)
            y += 76

    c.title_band("THE THREE QUESTIONS THAT DECIDE THE ANSWERS", 500)
    c.text(30, 530, "1.  When was it released — unchanged from the source, or created later by sunlight and chemistry?",
           11.5, "start", INK)
    c.text(30, 556, "2.  What is it made of — so which detection method and which control equipment will work?",
           11.5, "start", INK)
    c.text(30, 582, "3.  Where did it go — which decides whether the permit is a stack consent, an effluent consent or a landfill licence.",
           11.5, "start", INK)
    c.note("One pollutant can be all three at once: SO₂ is primary, chemical and air-borne.", 630)
    c.footer()
    return c


# ------------------------------------------------------------------ 1.3 pollutant effects
def pollutant_effects():
    c = Canvas(960, 672, "What each pollutant does, and at what concentration")
    rows = [
        ("SO₂", "air", "bronchospasm, acid rain, stone corrosion", "80 μg/m³ annual", RED),
        ("NOₓ", "air", "photochemical smog, ground-level ozone, acid rain", "40 μg/m³ annual", AMBER),
        ("CO", "air", "binds haemoglobin 200× more strongly than O₂", "2 mg/m³ 8-hour", PD),
        ("PM10 / PM2.5", "air", "reaches alveoli, carries metals into blood", "60 / 40 μg/m³", INK),
        ("BOD load", "water", "oxygen sag, fish kill, foul odour", "30 mg/L inlet", BLUE),
        ("Heavy metals", "water", "Hg, Pb, Cr accumulate in tissue, neurotoxic", "0.001–0.05 mg/L", GREEN),
        ("Noise", "physical", "hearing loss above 85 dB(A) over 8 h", "75 dB(A) zone", MUTED),
    ]
    c.rbox(30, 84, 900, 34, "", LAV, "none", rx=5)
    for x, label in ((42, "POLLUTANT"), (250, "MEDIUM"), (400, "EFFECT"), (760, "TYPICAL LIMIT")):
        c.text(x, 106, label, 11, "start", PD, "bold")

    y = 122
    for name, medium, effect, limit, col in rows:
        c.rect(30, y, 900, 50, "#FFFFFF", LINE, 1.1, rx=4)
        c.rect(30, y, 5, 50, col, "none", 0, rx=2)
        c.text(46, y + 22, name, 12, "start", col, "bold")
        c.text(250, y + 22, medium, 11, "start", INK)
        c.text(400, y + 22, effect, 11, "start", INK)
        c.text(760, y + 22, limit, 10.5, "start", MUTED)
        y += 56

    c.title_band("THE CHAIN FROM DOSE TO DAMAGE", 532)
    c.text(30, 562, "release  →  transport and dilution  →  concentration at the receptor  →  exposure  →  dose  →  response",
           12, "start", PD, "bold")
    c.text(30, 590, "Control can be applied at any arrow. The cheapest place is the first one: prevent the release, "
                    "because dilution is not treatment.", 11, "start", INK)
    c.note("Limits are indicative NAQ / CPCB values for orientation; always quote the current gazette notification.", 628)
    c.footer()
    return c


# ------------------------------------------------------------------ 1.4 GPCB standards
def standards_chart():
    c = Canvas(980, 672, "What a consent to operate actually limits")
    c.rbox(30, 84, 440, 232, "", "#F8FDF9", GREEN, rx=10)
    c.text(46, 110, "STACK / AMBIENT AIR", 12, "start", GREEN, "bold")
    air = [("SPM", "500 μg/m³ (industrial zone)"), ("SO₂", "120 μg/m³ 24-hour"),
           ("NOₓ", "120 μg/m³ 24-hour"), ("CO", "2 mg/m³ 8-hour"), ("Stack height", "H = 14 (Q)^0.3 m")]
    y = 140
    for k, v in air:
        c.text(46, y, k, 11, "start", INK, "bold")
        c.text(190, y, v, 11, "start", MUTED)
        y += 30

    c.rbox(500, 84, 450, 232, "", "#F5F8FD", BLUE, rx=10)
    c.text(516, 110, "EFFLUENT DISCHARGE", 12, "start", BLUE, "bold")
    water = [("pH", "6.5 – 8.5"), ("BOD₃", "30 mg/L (into inland surface water)"),
             ("COD", "250 mg/L"), ("Suspended solids", "100 mg/L"), ("Oil and grease", "10 mg/L")]
    y = 140
    for k, v in water:
        c.text(516, y, k, 11, "start", INK, "bold")
        c.text(700, y, v, 11, "start", MUTED)
        y += 30

    c.title_band("WHO SETS AND WHO ENFORCES", 340)
    steps = [("CPCB", "Central Pollution Control Board — sets national standards, classifies industries red / orange / green / white"),
             ("GPCB", "Gujarat Pollution Control Board — issues the Consent to Establish and the Consent to Operate"),
             ("Consent", "fixes the stack height, the effluent quality and the volume you may discharge"),
             ("Monitoring", "returns, sampling by the board, and closure for non-compliance")]
    for i, (who, what) in enumerate(steps):
        y = 368 + i * 52
        c.circle(52, y, 15, LAV, P, 1.6)
        c.text(52, y, str(i + 1), 11.5, "middle", PD, "bold")
        c.text(80, y - 8, who, 12, "start", PD, "bold")
        c.text(80, y + 12, what, 10.5, "start", INK)

    c.title_band("THE FOUR LEGISLATIONS A CHEMICAL ENGINEER MUST KNOW", 588)
    c.text(30, 616, "Water Act 1974  ·  Air Act 1981  ·  Environment (Protection) Act 1986  ·  "
                    "Waste Management Rules (solid, hazardous, plastic, e-waste)", 11, "start", INK)
    c.footer()
    return c


FIGURES = [
    ("d1_sources_pollution", sources_of_pollution),
    ("d1_pollutant_class", pollutant_classification),
    ("d1_pollutant_effects", pollutant_effects),
    ("d1_standards_consent", standards_chart),
]


def main():
    for name, fn in FIGURES:
        save(fn(), _p(name))
        print("wrote", _p(name))
    return [n for n, _ in FIGURES]


if __name__ == "__main__":
    main()
