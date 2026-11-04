"""Five compact mobile SVGs for Communication Skills in English (DI01000031) Unit 1."""
import math

from flowchart_lib import svg, text, arr, rbox, line, P

BLUE, BF = "#1565C0", "#EAF3FD"
GREEN, GF = "#2E7D32", "#EAF6EC"
ORANGE, OF = "#B66A00", "#FFF4DF"
RED, RF = "#BD2543", "#FDECF0"
PURPLE = "#7B2CD9"
GREY = "#666"
INK = "#333"

TITLES = {
    "c1_cycle": "The communication cycle: S E C D R N F",
    "c2_types": "Three kinds of communication",
    "c3_levels": "Upward and downward communication",
    "c4_barriers": "Five families of barriers",
    "c5_seven": "The seven Cs of a good message",
}


def heading(t, sub=None):
    body = text(180, 24, t, 14, weight="bold", color=P)
    if sub:
        body += text(180, 46, sub, 10.4, color=GREY)
    return body


def foot(y, *lines):
    return "".join(text(180, y + 16 * i, s, 10.2, color=GREY) for i, s in enumerate(lines))


# ---------------------------------------------------------------- 1. the cycle
def cycle():
    b = heading("The communication cycle", "seven parts, in this order")
    rows = [
        ("S - Sender: the person who has the idea", BF, BLUE),
        ("E - Encoding: the idea becomes words, signs or pictures", BF, BLUE),
        ("C - Channel: speech, e-mail, phone call, notice board", GF, GREEN),
        ("D - Decoding: the receiver works out what the words mean", GF, GREEN),
        ("R - Receiver: the person the message is meant for", GF, GREEN),
        ("F - Feedback: the reply that closes the loop", OF, ORANGE),
    ]
    y = 74
    for i, (label, fill, stroke) in enumerate(rows):
        b += rbox(180, y, 330, 26, label, fill, stroke, 9.9)
        if i < len(rows) - 1:
            b += arr([(180, y + 13), (180, y + 32)], GREY)
        y += 45
    b += rbox(180, y - 4, 330, 26, "N - Noise: anything that disturbs a part of the cycle", RF, RED, 9.9)
    b += foot(y + 32, "Feedback is what makes it communication, not just a broadcast.",
              "Noise can enter at any stage - the room, the words, or the mood.")
    return svg(360, y + 56, b)


# ---------------------------------------------------------------- 2. three kinds
def types():
    b = heading("Three kinds of communication", "verbal, non-verbal and visual")
    b += rbox(180, 76, 334, 26, "Verbal: words - spoken or written", BF, BLUE, 10.4)
    b += rbox(180, 108, 334, 26, "spoken: viva, phone call, lecture, interview", BF, BLUE, 9.6)
    b += rbox(180, 140, 334, 26, "written: e-mail, report, notice, WhatsApp text", BF, BLUE, 9.6)
    b += rbox(180, 178, 334, 26, "Non-verbal: body and voice, without words", GF, GREEN, 10.4)
    b += rbox(180, 210, 334, 26, "gesture, posture, eye contact, tone, personal space", GF, GREEN, 9.4)
    b += rbox(180, 248, 334, 26, "Visual: pictures and layouts", OF, ORANGE, 10.4)
    b += rbox(180, 280, 334, 26, "graph, chart, map, safety sign, icon, flowchart", OF, ORANGE, 9.6)
    b += rbox(180, 318, 334, 24, "most messages mix all three at once", RF, RED, 9.8)
    b += foot(356, "A safety sign is visual, the warning shout is verbal,",
              "and the raised hand that stops the gang is non-verbal.")
    return svg(360, 380, b)


# ---------------------------------------------------------------- 3. levels
def levels():
    b = heading("Upward and downward", "who sends, who receives")
    b += rbox(180, 78, 150, 26, "Top management", BF, BLUE, 10.0)
    b += rbox(180, 148, 150, 26, "Middle level", GF, GREEN, 10.0)
    b += rbox(180, 218, 150, 26, "Workers and operators", OF, ORANGE, 10.0)
    for y0, y1 in ((91, 135), (161, 205)):
        b += arr([(180, y0), (180, y1)], GREY)
    b += arr([(96, 205), (96, 161)], RED)
    b += arr([(96, 135), (96, 91)], RED)
    b += text(70, 200, "upward", 9.4, color=RED, anchor="end")
    b += arr([(264, 91), (264, 135)], BLUE)
    b += arr([(264, 161), (264, 205)], BLUE)
    b += text(292, 200, "downward", 9.4, color=BLUE, anchor="start")
    b += rbox(180, 266, 336, 24, "downward: orders, circulars, policy, instructions", BF, BLUE, 9.6)
    b += rbox(180, 298, 336, 24, "upward: reports, suggestions, grievances, feedback", RF, RED, 9.6)
    b += foot(334, "Downward flows as authority; upward flows as information.",
              "A one-way downward flow quickly loses the workers' ideas.")
    return svg(360, 356, b)


# ---------------------------------------------------------------- 4. barriers
def barriers():
    b = heading("Five families of barriers", "and one example of each")
    rows = [
        ("Physical: noise, distance, weak network", BF, BLUE),
        ("Language: jargon, wrong word, poor grammar", GF, GREEN),
        ("Psychological: fear, stress, prejudice, no attention", OF, ORANGE),
        ("Cultural: customs, gestures that mean different things", RF, RED),
        ("Organisational: too many levels, no clear channel", BF, BLUE),
    ]
    y = 78
    for label, fill, stroke in rows:
        b += rbox(180, y, 336, 26, label, fill, stroke, 9.7)
        y += 36
    b += rbox(180, y + 10, 336, 30, "cure: plan the message, use simple words,\nlisten, and confirm by feedback",
              GF, GREEN, 9.8)
    b += foot(y + 58, "Name the barrier first; the cure follows almost by itself.")
    return svg(360, y + 92, b)


# ---------------------------------------------------------------- 5. seven Cs
def seven_cs():
    b = heading("The seven Cs of a good message", "check the list before you send")
    items = [
        ("Clear", "one idea per sentence, no jargon"),
        ("Concise", "short - say it in the fewest words"),
        ("Concrete", "facts, figures and examples"),
        ("Correct", "right grammar, spelling and data"),
        ("Coherent", "logical order, one topic"),
        ("Complete", "all the details the reader needs"),
        ("Courteous", "polite, respectful tone"),
    ]
    y = 72
    for name, note in items:
        b += rbox(180, y, 336, 26, f"{name} - {note}", BF if y < 160 else GF, BLUE if y < 160 else GREEN,
                  9.8)
        y += 34
    b += foot(y + 8, "Seven Cs take ten seconds and prevent most misunderstandings.")
    return svg(360, y + 34, b)


ALL = {
    "c1_cycle": cycle,
    "c2_types": types,
    "c3_levels": levels,
    "c4_barriers": barriers,
    "c5_seven": seven_cs,
}
