"""Four compact mobile SVGs for Communication Skills in English (DI01000031) Unit 3 (literature)."""
from flowchart_lib import svg, text, arr, rbox, line, P

BLUE, BF = "#1565C0", "#EAF3FD"
GREEN, GF = "#2E7D32", "#EAF6EC"
ORANGE, OF = "#B66A00", "#FFF4DF"
RED, RF = "#BD2543", "#FDECF0"
PURPLE = "#7B2CD9"
GREY = "#666"

TITLES = {
    "lit1_plot": "The Leopard: the plot in five steps",
    "lit2_twenty": "After Twenty Years: the two meetings",
    "lit3_poem": "The poem: four stanzas, four steps",
    "lit4_conflict": "The Leopard: who is against whom",
}


def heading(t, sub=None):
    body = text(180, 24, t, 14, weight="bold", color=P)
    if sub:
        body += text(180, 46, sub, 10.4, color=GREY)
    return body


def foot(y, *lines):
    return "".join(text(180, y + 16 * i, s, 9.9, color=GREY) for i, s in enumerate(lines))


# ---------------------------------------------------------------- 1. plot of The Leopard
def plot_leopard():
    b = heading("The Leopard: the plot", "five steps, from trust to betrayal")
    rows = [
        ("1. The narrator walks the ravine every day", BF, BLUE),
        ("2. He meets a leopard at the stream; neither runs away", GF, GREEN),
        ("3. Hunters come and ask where it is; he says he has seen nothing", OF, ORANGE),
        ("4. The leopard is killed and its skin is taken and sold", RF, RED),
        ("5. He walks home through a silent forest - the trust is broken", BF, BLUE),
    ]
    y = 76
    for label, fill, stroke in rows:
        b += rbox(180, y, 336, 30, label, fill, stroke, 9.4)
        y += 42
    b += foot(y + 2, "Turning point: the arrival of the shikaris - the narrator has to choose",
              "between the hunters and the animal that trusted him.")
    return svg(360, y + 30, b)


# ---------------------------------------------------------------- 2. After Twenty Years
def twenty():
    b = heading("After Twenty Years", "two meetings, twenty years apart")
    rows = [
        ("Twenty years ago: Bob and Jimmy dine at Big Joe Brady's", BF, BLUE),
        ("They promise to meet on the same spot, same date", BF, BLUE),
        (None, None, None),
        ("10 pm tonight: Bob waits in a hardware-store doorway", GF, GREEN),
        ("A policeman on the beat stops; Bob tells his story", GF, GREEN),
        (None, None, None),
        ("The policeman moves on - he is Jimmy Wells", OF, ORANGE),
        ("A tall man arrives, calls him Bob, and they walk", OF, ORANGE),
        (None, None, None),
        ("Under the light Bob sees it is not Jimmy - he is arrested", RF, RED),
        ("Note from Jimmy: 'I saw the face of the man wanted in Chicago'", RF, RED),
    ]
    y = 74
    for label, fill, stroke in rows:
        if label is None:
            y += 10
            continue
        b += rbox(180, y, 336, 26, label, fill, stroke, 9.3)
        y += 32
    b += foot(y + 8, "Jimmy kept the appointment, but sent an officer to arrest him.")
    return svg(360, y + 32, b)


# ---------------------------------------------------------------- 3. poem
def poem():
    b = heading("Stopping by Woods", "four quatrains, one decision")
    rows = [
        ("1  He stops to watch the woods fill up with snow", BF, BLUE),
        ("2  The horse finds it strange: no farmhouse near", GF, GREEN),
        ("3  The horse shakes its bells; the only other sound is the wind", OF, ORANGE),
        ("4  'But I have promises to keep' - he moves on", RF, RED),
    ]
    y = 78
    for label, fill, stroke in rows:
        b += rbox(180, y, 336, 28, label, fill, stroke, 9.5)
        y += 40
    b += rbox(180, y + 8, 336, 40, "Rhyme: aaba bbcb ccdc dddd\nThe last two lines repeat", GF, GREEN, 9.5)
    b += foot(y + 62, "Movement: attraction of the woods, then the pull of duty.",
              "The repeated line sounds weary and resolved at once.")
    return svg(360, y + 90, b)


# ---------------------------------------------------------------- 4. conflicts
def conflict():
    b = heading("The Leopard: the conflicts", "four tensions in one short story")
    rows = [
        ("Narrator against hunters: he hides the leopard; they hunt it", BF, BLUE),
        ("Man against nature: the hill station grows, the forest shrinks", GF, GREEN),
        ("Greed against care: a skin worth over 1,000 rupees in Delhi", OF, ORANGE),
        ("Silence against speech: he says nothing; the forest falls silent", RF, RED),
    ]
    y = 80
    for label, fill, stroke in rows:
        b += rbox(180, y, 336, 34, label, fill, stroke, 9.4)
        y += 46
    b += foot(y + 2, "Each conflict ends the same way: the animal loses.",
              "The narrator's silence protects the leopard for a while, then fails.")
    return svg(360, y + 30, b)


ALL = {
    "lit1_plot": plot_leopard,
    "lit2_twenty": twenty,
    "lit3_poem": poem,
    "lit4_conflict": conflict,
}
