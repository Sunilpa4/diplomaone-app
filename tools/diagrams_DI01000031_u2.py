"""Five compact mobile SVGs for Communication Skills in English (DI01000031) Unit 2 (Grammar)."""
from flowchart_lib import svg, text, arr, rbox, line, P

BLUE, BF = "#1565C0", "#EAF3FD"
GREEN, GF = "#2E7D32", "#EAF6EC"
ORANGE, OF = "#B66A00", "#FFF4DF"
RED, RF = "#BD2543", "#FDECF0"
PURPLE = "#7B2CD9"
GREY = "#666"

TITLES = {
    "g1_pos": "The eight parts of speech",
    "g2_tenses": "Tenses on a timeline",
    "g3_modal": "Modal auxiliaries by function",
    "g4_agreement": "Subject-verb agreement rules",
    "g5_patterns": "The four sentence patterns",
}


def heading(t, sub=None):
    body = text(180, 24, t, 14, weight="bold", color=P)
    if sub:
        body += text(180, 46, sub, 10.4, color=GREY)
    return body


def foot(y, *lines):
    return "".join(text(180, y + 16 * i, s, 10.0, color=GREY) for i, s in enumerate(lines))


# ---------------------------------------------------------------- 1. parts of speech
def pos():
    b = heading("The eight parts of speech", "word class - one example each")
    rows = [
        ("Noun - names: motor, Surat, honesty", BF, BLUE),
        ("Pronoun - replaces a noun: it, they, who", BF, BLUE),
        ("Verb - action or state: run, is, replace", GF, GREEN),
        ("Adjective - describes a noun: hot, three, brass", GF, GREEN),
        ("Adverb - describes a verb: quickly, daily, very", OF, ORANGE),
        ("Preposition - links to a place or time: under, at, after", OF, ORANGE),
        ("Conjunction - joins: and, but, because", RF, RED),
        ("Interjection - sudden feeling: oh!, alas!, hurray!", RF, RED),
    ]
    y = 72
    for label, fill, stroke in rows:
        b += rbox(180, y, 336, 26, label, fill, stroke, 9.6)
        y += 34
    b += foot(y + 6, "Same word, different class: \"paint\" is a verb in \"paint the wall\",",
              "and a noun in \"the paint is wet\".")
    return svg(360, y + 30, b)


# ---------------------------------------------------------------- 2. tenses
def tenses():
    b = heading("Tenses on a timeline", "what the verb does, and when")
    b += line([(24, 74), (336, 74)], GREY, 1.4)
    b += arr([(316, 74), (338, 74)], GREY)
    b += text(40, 66, "past", 9.6, color=GREY)
    b += text(180, 66, "now", 9.6, color=GREY)
    b += text(316, 66, "future", 9.6, color=GREY)
    b += rbox(180, 104, 336, 44,
              "PAST: wrote / was writing / had written\nreported, described, finished before now",
              GF, GREEN, 9.4)
    b += rbox(180, 158, 336, 62,
              "PRESENT: writes / is writing / has written / has been writing\n"
              "habits, facts, right now, finished with a present result, still going on",
              BF, BLUE, 9.4)
    b += rbox(180, 230, 336, 44,
              "FUTURE: will write\nplans, promises, predictions",
              OF, ORANGE, 9.4)
    b += foot(300, "Markers decide the tense: yesterday, since Monday, tomorrow.",
              "One sentence can mix tenses: \"He has finished, so he will go home.\"")
    return svg(360, 330, b)


# ---------------------------------------------------------------- 3. modals
def modal():
    b = heading("Modal auxiliaries by function", "one meaning, one example")
    rows = [
        ("Ability: can, could", "\"I can weld.\" / \"He could weld at 16.\"", BF, BLUE),
        ("Permission: may, can, could", "\"May I open the panel?\"", BF, BLUE),
        ("Possibility: may, might, could", "\"The seal may leak.\"", GF, GREEN),
        ("Obligation: must, should, ought to", "\"You must wear goggles.\"", OF, ORANGE),
        ("Advice: should, ought to", "\"You should torque it twice.\"", OF, ORANGE),
        ("Future and offers: shall, will, would", "\"Shall we start?\" / \"I will call.\"", RF, RED),
        ("Need and absence of need: need, need not", "\"You need not come.\"", RF, RED),
    ]
    y = 70
    for label, example, fill, stroke in rows:
        b += rbox(180, y, 336, 24, label, fill, stroke, 9.5)
        b += text(180, y + 27, example, 9.3, color="#444")
        y += 62
    b += foot(y + 2, "No -s and no -ed: \"he can\", \"must\".",
              "One modal per verb: \"will can\" becomes \"will be able to\".")
    return svg(360, y + 32, b)


# ---------------------------------------------------------------- 4. agreement
def agreement():
    b = heading("Subject-verb agreement", "five rules that cover most sentences")
    rows = [
        ("One subject - one verb: The motor runs.", BF, BLUE),
        ("Two subjects with and - plural: The motor and the pump run.", BF, BLUE),
        ("either / or - the nearer subject decides:\nEither the belt or the bearings are worn.", GF, GREEN),
        ("Collective noun as one unit: The team is ready.", OF, ORANGE),
        ("Uncountable and amounts: The water is hot. Fifty rupees is enough.", RF, RED),
    ]
    y = 74
    for label, fill, stroke in rows:
        b += rbox(180, y, 336, 38, label, fill, stroke, 9.4)
        y += 48
    b += foot(y + 4, "Find the subject first, ignore the words between it and the verb.",
              "\"The box of bolts is heavy\" - the subject is box, not bolts.")
    return svg(360, y + 28, b)


# ---------------------------------------------------------------- 5. patterns
def patterns():
    b = heading("The four sentence patterns", "subject, verb, and what follows")
    rows = [
        ("SV", ["The motor", "failed", ""], GREEN),
        ("SVO", ["The fitter", "replaced", "the belt"], BLUE),
        ("SVA", ["The pump", "runs", "smoothly"], ORANGE),
        ("SVC", ["The panel", "is", "hot"], RED),
    ]
    y = 76
    for name, parts, colour in rows:
        b += text(26, y + 17, name, 11.5, weight="bold", color=colour, anchor="middle")
        xs = [104, 180, 262]
        widths = [66, 66, 84]
        for x, w, label in zip(xs, widths, parts):
            if not label:
                continue
            b += rbox(x, y, w, 26, label, "#FFFFFF", colour, 8.8)
        y += 46
    b += foot(y + 4, "SVO needs an object, SVA an adverb, SVC a complement.",
              "\"Hot\" describes the panel, so it is a complement, not an object.")
    return svg(360, y + 30, b)


ALL = {
    "g1_pos": pos,
    "g2_tenses": tenses,
    "g3_modal": modal,
    "g4_agreement": agreement,
    "g5_patterns": patterns,
}
