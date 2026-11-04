"""Five compact mobile SVGs for Applied Physics (DI01000121) Unit 1: units and measurements.

All labels stay in English, like every other bilingual subject in the app; the text of the cards
carries both languages. Every drawing is built from plain rect/path/text so the app needs no font
trickery, and each canvas is 360 px wide for a phone.
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
    "u1_units": "SI base units and what they measure",
    "u1_vernier": "Reading a vernier caliper: 2.36 cm",
    "u1_micrometer": "Reading a screw gauge: 4.82 mm",
    "u1_accuracy": "Accuracy and precision compared",
    "u1_sigfig": "How many digits do you keep?",
}


def ln(x1, y1, x2, y2, color=INK, w=1.2, dash=None):
    da = f' stroke-dasharray="{dash}"' if dash else ""
    return (f'<path d="M{x1} {y1}L{x2} {y2}" fill="none" stroke="{color}" stroke-width="{w}" '
            f'stroke-linecap="round"{da}/>')


def down(x, y1, y2, color=INK, w=1.4):
    return (ln(x, y1, x, y2 - 5, color, w) +
            f'<path d="M{x - 3.4} {y2 - 5.2}L{x} {y2}L{x + 3.4} {y2 - 5.2}Z" fill="{color}"/>')


def heading(t, sub=None, size=13.2):
    body = text(180, 21, t, size, weight="bold", color=P)
    if sub:
        body += text(180, 40, sub, 9.7, color=GREY)
    return body


def foot(y, *lines):
    return "".join(text(180, y + 15 * i, s, 9.3, color=GREY) for i, s in enumerate(lines))


# ------------------------------------------------------------------ 1. SI base units
def units():
    b = heading("Seven base units carry every measurement", "everything else is built from these")
    rows = [("length", "metre", "m"), ("mass", "kilogram", "kg"), ("time", "second", "s"),
            ("current", "ampere", "A"), ("temperature", "kelvin", "K"),
            ("substance", "mole", "mol"), ("light", "candela", "cd")]
    top = 54
    y = top
    for i, (what, unit, sym) in enumerate(rows):
        fill = BF if i % 2 == 0 else "#FFFFFF"
        b += f'<rect x="12" y="{y}" width="336" height="20" fill="{fill}"/>'
        b += text(20, y + 14, what, 9.8, anchor="start", color=INK)
        b += text(150, y + 14, unit, 9.8, anchor="start", color=BLUE)
        b += text(300, y + 14, sym, 10.2, anchor="middle", color=BLUE, weight="bold")
        y += 20
    b += text(300, top - 5, "symbol", 8.4, color=GREY)
    b += ln(12, top, 348, top, "#BBB", 1)
    for yy in (top, y):
        b += ln(12, yy, 348, yy, "#BBB", 1)
    b += ln(12, top, 12, y, "#BBB", 1) + ln(348, top, 348, y, "#BBB", 1)
    b += rbox(180, y + 22, 336, 28, "derived: 1 N = 1 kg·m/s² | 1 J = 1 N·m | 1 Pa = 1 N/m²",
              GF, GREEN, 9.0)
    b += foot(y + 56, "A number without a unit is not a measurement.",
              "Convert to one system before you add or multiply.")
    return svg(360, y + 78, b)


# ------------------------------------------------------------------ 2. vernier caliper
def vernier():
    b = heading("Main scale 2.3 cm, 6th vernier line matches", "least count 0.01 cm gives 2.36 cm")
    x0, cm = 18, 96.0                  # 1 cm on the drawing
    y = 82                             # main-scale axis
    b += text(18, y - 30, "main scale (cm)", 8.8, anchor="start", color=GREY)
    b += ln(x0, y, x0 + 3.15 * cm, y, INK, 1.4)
    for i in range(0, 32):             # 1 mm ticks, long tick at every cm
        x = x0 + i * cm / 10
        h = 13 if i % 10 == 0 else (8 if i % 5 == 0 else 4)
        b += ln(x, y, x, y - h, INK, 1.1)
        if i % 10 == 0 and i <= 30:
            b += text(x, y - 18, f"{i // 10}", 9.2, color=INK)
    # vernier scale: 10 divisions over 9 mm, its zero at 2.3 cm
    vy = y + 12
    vx = x0 + 2.3 * cm
    vspan = 0.9 * cm
    b += f'<rect x="{vx - 3}" y="{vy}" width="{vspan + 6}" height="15" fill="{BF}" stroke="{BLUE}" stroke-width="1.2"/>'
    for i in range(11):
        x = vx + i * vspan / 10
        b += ln(x, vy + 15, x, vy + 15 - 9, BLUE, 1.1)
    b += text(vx, vy + 28, "0", 8.6, color=BLUE)
    b += text(vx + vspan, vy + 28, "10", 8.6, color=BLUE)
    b += text(180, vy + 44, "vernier: 10 divisions over 9 mm", 8.8, color=BLUE)
    coinc = vx + 6 * vspan / 10
    b += ln(coinc, vy + 15, coinc, y - 2, RED, 1.5, dash="3 2")
    b += text(min(coinc, 292), y - 30, "6th line matches", 8.8, color=RED, anchor="middle")
    b += rbox(180, vy + 66, 336, 26, "2.3 cm + 6 × 0.01 cm = 2.36 cm", OF, ORANGE, 9.6)
    b += foot(vy + 100, "Zero error? Positive: subtract it. Negative: add it.",
              "L.C. = 1 M.S.D. − 1 V.S.D. = M.S.D. / n")
    return svg(360, vy + 124, b)


# ------------------------------------------------------------------ 3. screw gauge
def micrometer():
    b = heading("Sleeve 4.5 mm, thimble 32 divisions", "least count 0.01 mm gives 4.82 mm")
    y = 74                                  # sleeve axis
    mm = 60.0                               # 1 mm on the drawing
    x3 = 16                                 # the 3 mm mark
    b += f'<rect x="{x3}" y="{y}" width="{1.5 * mm}" height="20" fill="{GF}" stroke="{GREEN}" stroke-width="1.3"/>'
    for i in range(0, 4):                   # 3.0, 3.5, 4.0, 4.5 mm
        x = x3 + i * mm / 2
        b += ln(x, y + 20, x, y + 20 + (9 if i % 2 == 0 else 5), GREEN, 1.2)
        b += text(x - (2 if i == 3 else 0), y + 40, f"{3 + i / 2:g}", 8.0, color=GREY)
    b += text(x3 + 0.75 * mm, y + 58, "sleeve: 4.5 mm exposed", 8.8, color=GREEN)
    # thimble starts exactly at the 4.5 mm datum
    tx = x3 + 1.5 * mm + 10
    b += f'<rect x="{tx}" y="{y - 16}" width="100" height="58" rx="6" fill="{BF}" stroke="{BLUE}" stroke-width="1.4"/>'
    b += text(tx + 50, y + 1, "thimble", 9.2, color=BLUE)
    b += text(tx + 50, y + 20, "32 div", 12.5, color=BLUE, weight="bold")
    b += text(tx + 50, y + 33, "on the reference line", 7.6, color=GREY)
    b += ln(tx - 4, y + 6, tx + 2, y + 6, RED, 1.6)
    b += rbox(180, y + 82, 336, 26, "reading = S.S.R. + C.S.R. × L.C.", OF, ORANGE, 9.6)
    b += rbox(180, y + 112, 336, 26, "4.5 + 32 × 0.01 = 4.82 mm", GF, GREEN, 9.8)
    b += foot(y + 146, "L.C. = pitch / circular divisions = 0.5 / 50 = 0.01 mm",
              "A zero error of +0.02 mm makes the true diameter 4.80 mm.")
    return svg(360, y + 170, b)


# ------------------------------------------------------------------ 4. accuracy vs precision
def accuracy():
    b = heading("Same true value, different habits", "the black dot is the true value")
    cells = [
        ("accurate + precise", GREEN, (-2, -1), (5, -4), (-5, 4), (3, 7)),
        ("precise, not accurate", ORANGE, (-16, -12), (-12, -8), (-18, -6), (-13, -16)),
        ("neither", RED, (-22, -18), (20, 14), (-12, 22), (18, -20)),
        ("accurate on average", BLUE, (-26, -16), (26, 18), (6, -24), (-4, 24)),
    ]
    centres = [(104, 86), (256, 86), (104, 188), (256, 188)]
    for (label, colour, *dots), (cx, cy) in zip(cells, centres):
        b += f'<circle cx="{cx}" cy="{cy}" r="38" fill="#FFFFFF" stroke="#CCC" stroke-width="1.2"/>'
        b += f'<circle cx="{cx}" cy="{cy}" r="17" fill="none" stroke="#E2E2E2" stroke-width="1" stroke-dasharray="3 3"/>'
        b += f'<circle cx="{cx}" cy="{cy}" r="2.8" fill="{INK}"/>'
        for (dx, dy) in dots:
            b += f'<circle cx="{cx + dx}" cy="{cy + dy}" r="3.4" fill="{colour}"/>'
        b += text(cx, cy + 51, label, 9.2, color=colour, weight="bold")
    b += foot(262, "Accuracy = close to the true value. Precision = close to each other.",
              "Calibration buys accuracy; careful technique buys precision.")
    return svg(360, 302, b)


# ------------------------------------------------------------------ 5. significant figures
def sigfig():
    b = heading("How many digits do you keep?", "round once, at the very end")
    b += rbox(180, 60, 336, 26, "count the significant figures of every input", PF, PURPLE, 9.4)
    b += down(180, 73, 100)
    b += rbox(180, 100, 336, 26, "is the operation × / ÷ or + / − ?", BF, BLUE, 9.4)
    b += down(96, 113, 142)
    b += down(264, 113, 142)
    b += rbox(96, 158, 148, 44, "× or ÷", GF, GREEN, 10)
    b += text(96, 174, "keep the fewest s.f.", 8.4, color=GREEN)
    b += rbox(264, 158, 148, 44, "+ or −", OF, ORANGE, 10)
    b += text(264, 174, "keep the fewest decimals", 7.8, color=ORANGE)
    b += rbox(96, 218, 148, 30, "2.5 × 1.25 = 3.1", GF, GREEN, 8.8)
    b += rbox(264, 218, 148, 30, "12.11 + 18.0 = 31.1", OF, ORANGE, 8.4)
    b += foot(270, "Dropped digit > 5: round up. < 5: keep. Exactly 5: make it even.",
              "Never copy every digit of a calculator into your answer.")
    return svg(360, 304, b)


DIAGRAMS = {
    "u1_units": units,
    "u1_vernier": vernier,
    "u1_micrometer": micrometer,
    "u1_accuracy": accuracy,
    "u1_sigfig": sigfig,
}

CAPTIONS = {
    "u1_units": "The seven SI base units, with the derived units a diploma engineer uses every day.",
    "u1_vernier": "A 2.36 cm vernier reading: main scale 2.3 cm plus 6 × 0.01 cm.",
    "u1_micrometer": "A 4.82 mm screw-gauge reading: sleeve 4.5 mm plus 32 × 0.01 mm.",
    "u1_accuracy": "Four habits of measurement compared with one true value.",
    "u1_sigfig": "How many digits to keep in a product and in a sum.",
}

TITLES_GU = {
    "u1_units": "SI પાયાના એકમો અને તે શું માપે છે",
    "u1_vernier": "વર્નિયર કેલિપરનું વાંચન: 2.36 cm",
    "u1_micrometer": "સ્ક્રુ ગેજનું વાંચન: 4.82 mm",
    "u1_accuracy": "ચોકસાઈ અને પરિશુદ્ધતાની સરખામણી",
    "u1_sigfig": "કેટલા અંક રાખવા?",
}

CAPTIONS_GU = {
    "u1_units": "સાત SI પાયાના એકમો અને દરરોજ વપરાતા વ્યુત્પન્ન એકમો.",
    "u1_vernier": "2.36 cm નું વર્નિયર વાંચન: મુખ્ય સ્કેલ 2.3 cm ઉપર 6 × 0.01 cm.",
    "u1_micrometer": "4.82 mm નું સ્ક્રુ ગેજ વાંચન: સ્લીવ 4.5 mm ઉપર 32 × 0.01 mm.",
    "u1_accuracy": "એક જ સાચા મૂલ્ય સામે માપનની ચાર આદતો.",
    "u1_sigfig": "ગુણાકાર અને સરવાળામાં કેટલા અંક રાખવા.",
}
