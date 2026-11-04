"""Three compact mobile SVGs for Communication Skills in English (DI01000031) Unit 4 (writing)."""
from flowchart_lib import svg, text, arr, rbox, line, P

BLUE, BF = "#1565C0", "#EAF3FD"
GREEN, GF = "#2E7D32", "#EAF6EC"
ORANGE, OF = "#B66A00", "#FFF4DF"
RED, RF = "#BD2543", "#FDECF0"
PURPLE = "#7B2CD9"
GREY = "#666"

TITLES = {
    "w1_email": "The parts of a business e-mail",
    "w2_paragraph": "The shape of a paragraph",
    "w3_types": "Four e-mails you will write",
}


def heading(t, sub=None):
    body = text(180, 24, t, 14, weight="bold", color=P)
    if sub:
        body += text(180, 46, sub, 10.3, color=GREY)
    return body


def foot(y, *lines):
    return "".join(text(180, y + 16 * i, s, 9.9, color=GREY) for i, s in enumerate(lines))


# ---------------------------------------------------------------- 1. e-mail anatomy
def email():
    b = heading("The parts of a business e-mail", "eight blocks, top to bottom")
    fields = [
        ("To:  purchase@shreetools.in", BF, BLUE),
        ("Cc:  stores@abctools.in", BF, BLUE),
        ("Subject:  Inquiry - 12 mm MS plates, 2 tonnes", RF, RED),
    ]
    y = 70
    for label, fill, stroke in fields:
        b += rbox(180, y, 336, 24, label, fill, stroke, 9.3)
        y += 30
    b += line([(14, y - 6), (346, y - 6)], "#BBB", 1)
    body = [
        ("Dear Sir,", GREEN),
        ("We need 2 tonnes of 12 mm MS plates for a", GREY),
        ("fabrication job at our Surat site.", GREY),
        ("Please send your rate, delivery time and", GREY),
        ("payment terms by Friday.", GREY),
    ]
    y += 8
    for label, colour in body:
        b += text(20, y, label, 9.3, color=colour, anchor="start")
        y += 18
    b += text(20, y + 4, "Regards,", 9.3, color=GREEN, anchor="start")
    b += text(20, y + 22, "R. Patel, Site Engineer, ABC Engineering", 9.0, color=GREY, anchor="start")
    b += foot(y + 52, "Subject and closing carry the most marks: one clear subject line,",
              "one polite close, one signature with your name and role.")
    return svg(360, y + 76, b)


# ---------------------------------------------------------------- 2. paragraph shape
def paragraph():
    b = heading("The shape of a paragraph", "one idea, supported, then closed")
    y = 76
    rows = [
        ("Topic sentence: the one idea of the paragraph", BF, BLUE),
        ("Support 1: a fact, an example or a reason", GF, GREEN),
        ("Support 2: another fact or example", GF, GREEN),
        ("Support 3: a detail that makes it vivid", GF, GREEN),
        ("Concluding sentence: rounds off or looks ahead", OF, ORANGE),
    ]
    for label, fill, stroke in rows:
        b += rbox(180, y, 330, 28, label, fill, stroke, 9.4)
        y += 38
    b += rbox(180, y + 8, 330, 30, "about 150 words = 12 to 15 lines\n3 to 5 supporting sentences",
              RF, RED, 9.5)
    b += foot(y + 58, "One paragraph, one idea. A second idea needs a second paragraph.")
    return svg(360, y + 84, b)


# ---------------------------------------------------------------- 3. four types
def types():
    b = heading("Four e-mails you will write", "purpose and one line each")
    rows = [
        ("Inquiry: ask for rate, stock, delivery or terms", BF, BLUE),
        ("Reply to inquiry: answer every question, in order", GF, GREEN),
        ("Order: item, quantity, price, delivery, payment", OF, ORANGE),
        ("Complaint: what is wrong, the evidence, the remedy", RF, RED),
    ]
    y = 78
    for label, fill, stroke in rows:
        b += rbox(180, y, 334, 30, label, fill, stroke, 9.4)
        y += 40
    b += foot(y + 4, "All four share one shape: purpose, details, action, close.",
              "The only thing that changes is what you ask the reader to do.")
    return svg(360, y + 30, b)


ALL = {
    "w1_email": email,
    "w2_paragraph": paragraph,
    "w3_types": types,
}
