"""DI01000031 Communication Skills in English - Unit 3: Prose and Poetry.

GTU 3.1-3.3, 6 h, 20 %, 14 marks, CO3: develop reading and listening skills.

Author's policy for this subject (user instruction): the literature unit carries full summaries and
question-answer sets, unlike the grammar and writing units, which stay example-driven.
"""
from subject_DI01000031 import tr as _tr


class Txt(dict):
    def __add__(self, other):
        tail = other.get("en") if isinstance(other, dict) else str(other)
        return Txt({"en": self["en"] + tail})

    def __radd__(self, other):
        head = other.get("en") if isinstance(other, dict) else str(other)
        return Txt({"en": head + self["en"]})


def tr(s):
    return Txt({"en": s})


def p(x):
    return f"<p>{x}</p>"


def h4(x):
    return f"<h4>{x}</h4>"


def ul(*items):
    return "<ul>" + "".join(f"<li>{i}</li>" for i in items) + "</ul>"


def ol(*items):
    return "<ol>" + "".join(f"<li>{i}</li>" for i in items) + "</ol>"


def table(head, rows):
    return ("<table><tr>" + "".join(f"<th>{h}</th>" for h in head) + "</tr>"
            + "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in rows) + "</table>")


def card(heading, body, diagram=None, syllabus_item=None):
    item = {"h": tr(heading), "body": tr(body)}
    if diagram:
        item["diagram"] = diagram
    if syllabus_item:
        item["syllabus_item"] = syllabus_item
    return item


SOURCES = [
    ("GTU DI01000031, Communication Skills in English, Semester 1, HSMC-1 (uploaded syllabus)",
     "https://syllabus.gtu.ac.in/"),
    ("Ruskin Bond - The Leopard, in Time Stops at Shamli and Other Stories (Penguin)",
     "https://www.penguinrandomhouseindia.com/"),
    ("O. Henry - After Twenty Years (public domain text, 1906)",
     "https://www.gutenberg.org/ebooks/1595"),
    ("Robert Frost - Stopping by Woods on a Snowy Evening (New Hampshire, 1923)",
     "https://www.poetryfoundation.org/poems/42891/stopping-by-woods-on-a-snowy-evening"),
    ("Poetry Foundation - Robert Frost, biography and works",
     "https://www.poetryfoundation.org/poets/robert-frost"),
]

NOTES = [
    {"title": tr("1. Prose: The Leopard - Ruskin Bond"),
     "items": [
         card("1.1 The writer and the story",
              h4("About the writer")
              + p("<b>Ruskin Bond</b> (born 1934) is an Indian writer of English who has lived most of "
                  "his life in the Himalayan foothills, at Dehradun, Shimla and now Landour near "
                  "Mussoorie. He writes simply, about small towns, children, and the animals and "
                  "trees around him.")
              + table(["Work", "What to remember"],
                      [("The Room on the Roof (1956)", "written at seventeen; won the John Llewellyn "
                                                       "Rhys Prize"),
                       ("The Blue Umbrella", "a short novel about a girl and her umbrella"),
                       ("A Flight of Pigeons", "set in 1857; filmed as Junoon"),
                       ("The Leopard", "a short story about a leopard, hunters and a broken trust"),
                       ("Rusty stories", "the boy Rusty, who is close to Bond's own childhood")])
              + h4("The story at a glance")
              + table(["Point", "Detail"],
                      [("Form", "short story, first-person narration"),
                       ("Setting", "a deep ravine with a stream, below a hill station in the "
                                   "Himalayan foothills"),
                       ("Time", "a few weeks in one season"),
                       ("Narrator", "a writer who walks the ravine every day"),
                       ("Main events", "a leopard is met, trusted, hidden, then killed"),
                       ("Tone", "quiet, observant, sad at the end")])
              + h4("Example of the writing")
              + p("Bond describes the ravine as a place of ferns, bird calls and running water, so "
                  "that the reader feels the quiet before the hunters bring noise into it.")
              + h4("Common mistake")
              + p("Calling the narrator \"the author\" and the story \"a true story\". The narrator "
                  "speaks in the first person, which is a technique; the events are fiction shaped "
                  "from the writer's hill life."),
              syllabus_item="3.1"),
         card("1.2 The setting and the narrator's walks",
              h4("Summary")
              + p("The narrator lives near a hill station. Below the town a deep ravine runs down to a "
                  "stream, thick with ferns, moss, and the trees of the lower Himalaya. Most people "
                  "never go down there; he goes almost every day.")
              + p("Because he walks the same path quietly and carries no gun, the animals stop "
                  "treating him as a danger. Birds go on feeding while he stands a few metres away; "
                  "deer and a red fox cross his path without alarm.")
              + h4("Why the setting matters")
              + ul("The ravine is a <b>sanctuary</b>: a small piece of wild land left alone by the town.",
                   "It is <b>below</b> the hill station, so the town's growth presses on it from above.",
                   "Its quiet is the story's most valuable possession, and it is what the ending "
                   "takes away.")
              + h4("Examples from the text")
              + p("The narrator notices small things - the sound of the stream, the call of a bird, the "
                  "way a deer lifts its head - rather than large events. That habit of noticing is "
                  "what makes the leopard's trust believable.")
              + h4("Common mistake")
              + p("Treating the ravine as scenery only. In this story the place is a character: it "
                  "shelters the leopard, and its silence at the end reports the loss."),
              syllabus_item="3.1"),
         card("1.3 The meeting with the leopard",
              h4("Summary")
              + p("One evening the narrator sees a leopard at the stream. Both freeze. The leopard "
                  "drinks, looks at him, and goes back into the trees.")
              + p("After that the meeting repeats. Over days and weeks the leopard learns that this "
                  "man does not throw stones, does not shout and does not carry a gun. They begin to "
                  "share the ravine: the leopard drinks while the narrator sits at a distance, and "
                  "neither runs.")
              + p("The trust is never friendship. He does not feed it or touch it. It is a "
                  "<b>tolerance</b> - two animals, one of them human, agreeing to leave each other "
                  "alone.")
              + h4("Details that carry the meaning")
              + table(["Detail", "What it shows"],
                      [("the leopard drinks without hurry", "it no longer fears him"),
                       ("the narrator keeps his distance", "his respect for the wild"),
                       ("he tells nobody at first", "the ravine is a private world"),
                       ("no gun, no camera, no crowd", "trust needs silence")])
              + h4("Example of the change")
              + p("Early in the story a movement in the grass makes the narrator hold his breath; "
                  "later the same movement only makes him look up. The change is in him as much as in "
                  "the leopard.")
              + h4("Common mistake")
              + p("Writing that \"the narrator tamed the leopard\". Nothing is tamed: the leopard "
                  "stays wild, and that is exactly why its death matters."),
              syllabus_item="3.1"),
         card("1.4 The hunters arrive",
              h4("Summary")
              + p("Word reaches the town that a leopard has been seen near the village. Hunters - "
                  "shikaris - come up with guns, looking for a skin. They meet the narrator on the "
                  "path and ask him whether he has seen the leopard.")
              + p("He says he has seen nothing. The lie is a choice: he knows where the leopard drinks "
                  "and when, and he refuses to sell that knowledge.")
              + p("The hunters talk openly about money. A leopard skin, they say, sells in Delhi for "
                  "more than a thousand rupees. That single figure turns the animal into a price.")
              + h4("The moral choice")
              + table(["Choice open to the narrator", "Consequence"],
                      [("tell the hunters where it drinks", "quick money, a dead leopard"),
                       ("say nothing", "buys time, but does not stop the hunt"),
                       ("report the hunters to the authorities", "would need proof, and he has none")])
              + h4("Examples of the hunters' talk")
              + p("They describe the animal by the money it will bring, not by its size, age or "
                  "beauty. Their language is a market language; his is a watcher's language.")
              + h4("Common mistake")
              + p("Saying the narrator \"saved\" the leopard. His silence delays the hunt; it does not "
                  "end it. A story about a small good act that is not enough is stronger than a story "
                  "about a rescue."),
              "lit4_conflict", syllabus_item="3.1"),
         card("1.5 The kill and the silent forest",
              h4("Summary")
              + p("The hunters find the leopard without his help and shoot it. They take the skin and "
                  "leave. The ravine, which had been full of small sounds, becomes silent: no bird "
                  "call, no deer, no fox.")
              + p("The narrator walks home through that silence. Bond's closing thought is that it was "
                  "\"almost as though the birds and animals knew their trust had been violated\".")
              + p("The story ends without a speech, a trial or a punishment. The loss is simply there, "
                  "and the reader is left with it.")
              + h4("Why the ending works")
              + ul("The silence is <b>evidence</b>: the reader hears the absence.",
                   "The animals' imagined knowledge makes the whole wild world a witness.",
                   "No revenge is shown, so the injustice stays open in the reader's mind.")
              + h4("Examples of what has changed")
              + table(["Before the hunters", "After the hunters"],
                      [("birds feed close by", "no bird call"),
                       ("the leopard drinks at the stream", "the stream runs alone"),
                       ("the ravine is a refuge", "the ravine is a killing ground"),
                       ("the narrator belongs there", "he walks home as an outsider")])
              + h4("Common mistake")
              + p("Reading the ending as only sad. It is also an accusation: the trust was broken by "
                  "the people who came for money, and the narrator's silence made him part of the "
                  "human side of that break."),
              "lit1_plot", syllabus_item="3.1"),
         card("1.6 Themes",
              h4("The five themes")
              + table(["Theme", "Where it appears"],
                      [("Man and nature", "the ravine shared by a man and a leopard"),
                       ("Trust and betrayal", "the leopard trusts; the hunters kill; the forest falls "
                                              "silent"),
                       ("Greed and the skin trade", "a skin worth over a thousand rupees in Delhi"),
                       ("Conservation", "a small wild place pressed by a growing hill station"),
                       ("The limits of individual goodness", "the narrator's silence is honest but "
                                                             "not enough")])
              + h4("How to write about a theme")
              + p("Name the theme, give one moment from the story, and say what the story suggests. "
                  "For example: <i>The theme of greed appears when the hunters price the leopard at a "
                  "thousand rupees; Bond suggests that a market value can erase a living creature.</i>")
              + h4("Examples of theme sentences you can reuse")
              + ul("Trust in this story is a habit of not harming, not a promise.",
                   "The forest's silence is Bond's way of showing grief without a funeral.",
                   "The hill station grows, the ravine shrinks, and the leopard has nowhere else to "
                   "go.")
              + h4("Common mistake")
              + p("Writing a paragraph on \"environment\" without once mentioning this story. Every "
                  "theme answer needs a moment from the text."),
              syllabus_item="3.1"),
         card("1.7 Characters",
              h4("The narrator")
              + p("A writer and a walker. Quiet, observant, patient, and physically unarmed. He loves "
                  "the ravine and is accepted by its animals. His strength is attention; his weakness "
                  "is that he acts only by silence.")
              + h4("The leopard")
              + p("Wild, cautious and, in the end, defenceless. It is not a pet and does not seek the "
                  "man out; it simply stops fearing him. It stands for the wild itself - beautiful, "
                  "dangerous to others, and unable to defend itself against a rifle.")
              + h4("The hunters")
              + p("Professional, cheerful and commercial. They are not shown as monsters; that is what "
                  "makes them frightening. They talk about money while the narrator talks about the "
                  "stream.")
              + h4("Character table for revision")
              + table(["Character", "Three words", "One line of evidence"],
                      [("Narrator", "quiet, watchful, honest",
                        "he says he has seen nothing"),
                       ("Leopard", "wild, trusting, doomed",
                        "it drinks while he sits nearby"),
                       ("Hunters", "businesslike, boastful, greedy",
                        "\"skins sell in Delhi for over a thousand rupees\"")])
              + h4("Common mistake")
              + p("Describing the hunters as \"evil men\". Bond gives them ordinary manners, which "
                  "makes the point sharper: ordinary people do this for money."),
              syllabus_item="3.1"),
         card("1.8 Style, symbols and exam notes",
              h4("Style")
              + ul("First-person narration, so the reader sees only what the narrator sees.",
                   "Calm, short sentences; the excitement is in the animal, not the language.",
                   "Sensory description: sound, light, water, leaf-fall.",
                   "Contrast: the quiet ravine against the loud hunters.")
              + h4("Symbols")
              + table(["Symbol", "Meaning"],
                      [("the ravine and stream", "a last refuge of the wild"),
                       ("the skin", "the animal turned into money"),
                       ("silence at the end", "grief, guilt, and a broken contract"),
                       ("the narrator's silence", "the small, insufficient good act")])
              + h4("Answer plan for \"Describe the theme of the story\"")
              + ol("One line naming the theme.",
                   "The ravine and the trust (two or three sentences).",
                   "The hunters and the price of the skin.",
                   "The kill and the silent forest.",
                   "Closing sentence: what Bond wants the reader to feel.")
              + h4("Common mistake")
              + p("Retelling the plot and calling it a theme answer. The plot earns marks only when it "
                  "is used as evidence for an idea."),
              syllabus_item="3.1"),
     ]},

    {"title": tr("2. Short Story: After Twenty Years - O. Henry"),
     "items": [
         card("2.1 The writer and the setting",
              h4("About the writer")
              + p("<b>O. Henry</b> is the pen name of William Sydney Porter (1862-1910), an American "
                  "short-story writer famous for warm, witty stories with a twist in the last "
                  "paragraph. His best-known stories are <i>The Gift of the Magi</i>, <i>The Last "
                  "Leaf</i> and <i>The Cop and the Anthem</i>.")
              + h4("The setting")
              + table(["Point", "Detail"],
                      [("City", "New York"),
                       ("Time", "about ten o'clock on a cold, windy night"),
                       ("Place", "a street where a hardware store now stands; twenty years earlier "
                                 "the restaurant \"Big Joe\" Brady's was there"),
                       ("Weather", "chilly gusts, few people on the street"),
                       ("Mood", "quiet, slightly nostalgic, then tense")])
              + h4("Why the setting is chosen")
              + p("The old restaurant is gone and a hardware store has taken its place: the city has "
                  "changed, and so has everything except the promise. The empty street also lets two "
                  "men talk without a crowd, which the plot needs.")
              + h4("Common mistake")
              + p("Saying the story happens in Chicago. Chicago is where Bob is <i>wanted</i>; the "
                  "meeting is in New York."),
              syllabus_item="3.2"),
         card("2.2 The plot in order",
              h4("Summary")
              + p("A policeman on his beat walks up a quiet New York street at about ten at night. In "
                  "the doorway of a hardware store stands a man with an unlit cigar.")
              + p("The man explains that he is waiting for his dearest friend, Jimmy Wells. Exactly "
                  "twenty years ago they dined at \"Big Joe\" Brady's restaurant on that spot and "
                  "promised to meet again there at the same hour on the same date, wherever life had "
                  "taken them. Bob went West and did well; Jimmy stayed in New York, a steady man.")
              + p("The policeman wishes him luck and walks on. Twenty minutes later a tall man in a "
                  "long overcoat hurries up, greets him as Bob, and the two walk arm in arm.")
              + p("Under a bright street light Bob stops. The man beside him is not Jimmy: the nose is "
                  "wrong. The stranger says he is a plain-clothes officer and that Bob has been under "
                  "arrest for ten minutes. He hands him a note.")
              + h4("The note")
              + p("Jimmy writes that he came to the meeting place on time, and that when Bob struck a "
                  "match to light his cigar, he saw the face of the man wanted in Chicago. He could "
                  "not arrest him himself, so he sent another officer.")
              + h4("Order of events for an exam answer")
              + ol("Policeman on the beat; Bob waiting in the doorway.",
                   "Bob tells the story of the promise made twenty years ago.",
                   "The policeman leaves; Bob waits alone.",
                   "A tall man arrives and greets him as Jimmy.",
                   "Under the light Bob sees the nose and is arrested.",
                   "The note reveals that the first policeman was Jimmy Wells.")
              + h4("Common mistake")
              + p("Mixing the order of the two meetings. The policeman comes first; the plain-clothes "
                  "man comes second; the note explains both."),
              "lit2_twenty", syllabus_item="3.2"),
         card("2.3 Characters",
              h4("Bob - the man from the West")
              + p("Sentimental, talkative and confident. He has travelled, made money, and wears a "
                  "watch set with small diamonds. He keeps the appointment exactly, which shows real "
                  "loyalty - and he is also the man wanted in Chicago, which shows what his success "
                  "cost.")
              + h4("Jimmy Wells - the policeman")
              + p("Steady, dutiful and quietly emotional. He recognises his friend's face by matchlight "
                  "and still keeps the appointment. He cannot arrest Bob himself, and he cannot let "
                  "him go, so he sends another officer and leaves a note. He is the story's moral "
                  "centre.")
              + h4("The plain-clothes officer")
              + p("Polite and businesslike. He plays the friend for a block of street so that the "
                  "arrest can happen quietly, which is a small kindness inside an official duty.")
              + h4("Comparison")
              + table(["Point", "Bob", "Jimmy"],
                      [("Moved", "West, made money", "stayed in New York"),
                       ("Temperament", "impulsive, sentimental", "steady, dutiful"),
                       ("Position now", "wanted criminal", "police officer"),
                       ("Keeps the promise", "yes", "yes"),
                       ("Ends the story", "arrested", "writes the note")])
              + h4("Common mistake")
              + p("Calling Jimmy disloyal. He keeps the appointment and refuses to arrest his friend "
                  "with his own hands - loyalty and duty are both present, which is the point."),
              syllabus_item="3.2"),
         card("2.4 The twist ending",
              h4("What the twist is")
              + p("The reader believes that the tall man is Jimmy Wells. He is not: he is a "
                  "plain-clothes officer, and the real Jimmy was the policeman at the start.")
              + h4("How O. Henry prepares it")
              + table(["Clue", "Where", "What it does"],
                      [("the policeman's interest in Bob's story", "first meeting",
                        "makes him more than a passing figure"),
                       ("the match Bob strikes to light his cigar", "first meeting",
                        "gives Jimmy a clear look at his face"),
                       ("\"I'll be on my way\"", "first meeting",
                        "ends the scene without explanation"),
                       ("the wrong nose", "second meeting",
                        "the detail that breaks the illusion")])
              + h4("The sentence that turns the story")
              + p("Bob says that twenty years is long enough to change many things, \"but not long "
                  "enough to change a man's nose from a Roman to a pug\". The officer answers that it "
                  "sometimes changes \"a good man into a bad one\" - and the arrest follows.")
              + h4("Common mistake")
              + p("Calling the ending a trick. Every clue is in plain sight, and the twist makes a "
                  "moral point: the friend who kept faith is the one who has to act against his "
                  "friend."),
              syllabus_item="3.2"),
         card("2.5 Themes",
              h4("The four themes")
              + table(["Theme", "Evidence"],
                      [("Friendship against duty", "Jimmy keeps the appointment but sends an officer "
                                                   "to arrest Bob"),
                       ("Time and change", "twenty years alter a restaurant, a face and a life"),
                       ("Loyalty", "Bob travels across the country to stand in a doorway at ten at "
                                   "night"),
                       ("Crime and its cost", "Bob's fortune has made him a wanted man")])
              + h4("Writing about a theme")
              + p("Name the theme, give the moment, and say what O. Henry suggests. Example: <i>The "
                  "theme of duty appears when Jimmy steps aside and sends another officer; O. Henry "
                  "suggests that friendship can be honoured even when it cannot be protected.</i>")
              + h4("Examples of theme sentences")
              + ul("Bob's loyalty is real, and so is his crime; the story refuses to make him only a "
                   "villain.",
                   "Jimmy's note is the most affectionate act in the story and the most official.",
                   "Twenty years change the city faster than it changes the promise.")
              + h4("Common mistake")
              + p("Discussing friendship without duty, or duty without friendship. The story is built "
                  "on both at once."),
              syllabus_item="3.2"),
         card("2.6 Title, irony and key lines",
              h4("The title")
              + p("\"After Twenty Years\" measures the whole story: the promise is twenty years old, "
                  "and the men are measured by what those years made of them. The title carries no "
                  "hint of the ending, which is why the twist lands.")
              + h4("Irony in the story")
              + ul("Bob praises Jimmy's steadiness while Jimmy stands in front of him in uniform.",
                   "The friend who arrives is not the friend.",
                   "The reunion Bob waited twenty years for ends in an arrest.")
              + h4("Key lines and what they do")
              + table(["Line (short quote)", "Function"],
                      [("\"We figured that in twenty years each of us ought to have our destiny "
                        "worked out\"", "sets up the theme of time"),
                       ("\"not long enough to change a man's nose from a Roman to a pug\"",
                        "the moment of recognition"),
                       ("\"It sometimes changes a good man into a bad one\"", "the moral of the twist"),
                       ("the signed note", "resolves the plot without a scene")])
              + h4("Common mistake")
              + p("Calling the note a letter of betrayal. Jimmy explains, apologises in his way, and "
                  "signs his name - it is a farewell from a friend as much as a report from an "
                  "officer."),
              syllabus_item="3.2"),
         card("2.7 How to answer questions on the story",
              h4("Question types")
              + table(["Question", "What to include"],
                      [("Describe the plot", "six steps in order, ending with the note"),
                       ("Sketch the character of Jimmy Wells", "steady, dutiful, loyal; two moments"),
                       ("Why is the ending surprising?", "the tall man is not Jimmy; clues listed"),
                       ("What is the theme?", "friendship against duty, with evidence"),
                       ("Justify the title", "twenty years shapes the promise and the men")])
              + h4("Model opening for a plot answer")
              + p("\"O. Henry's <i>After Twenty Years</i> opens on a quiet New York street at ten at "
                  "night, where a man waits in a doorway for a friend he has not seen for twenty "
                  "years...\"")
              + h4("Model opening for a character answer")
              + p("\"Jimmy Wells is a policeman first and a friend always; the story tests which of "
                  "the two he will obey, and his answer is the note he leaves behind.\"")
              + h4("Common mistake")
              + p("Writing the ending first. Keep the order, and let the reader meet the twist where "
                  "O. Henry put it."),
              syllabus_item="3.2"),
     ]},

    {"title": tr("3. Poetry: Stopping by Woods on a Snowy Evening - Robert Frost"),
     "items": [
         card("3.1 The poet and the poem",
              h4("About the poet")
              + p("<b>Robert Frost</b> (1874-1963) was an American poet who wrote about rural New "
                  "England in plain, spoken language. He won the Pulitzer Prize four times. His "
                  "best-known poems are <i>The Road Not Taken</i>, <i>Mending Wall</i> and "
                  "<i>Birches</i>.")
              + h4("The poem")
              + table(["Point", "Detail"],
                      [("Published", "1923, in the collection New Hampshire (written 1922)"),
                       ("Form", "four quatrains (four-line stanzas)"),
                       ("Metre", "iambic tetrameter - four beats to a line"),
                       ("Rhyme", "aaba bbcb ccdc dddd: the third line of each stanza sets up the next "
                                 "stanza's rhyme"),
                       ("Speaker", "a traveller who has stopped on a road beside woods"),
                       ("Situation", "snowfall, evening, a horse, a journey not yet finished")])
              + h4("The rhyme scheme in practice")
              + p("Stanza one rhymes <i>know / though / here / snow</i> (aaba). The sound <i>know</i> "
                  "is picked up by <i>though</i> and <i>snow</i>; the odd line out, <i>here</i>, is "
                  "answered by <i>queer / near / year</i> in stanza two. In the last stanza all four "
                  "lines rhyme, and the closing line repeats.")
              + h4("Why the form matters")
              + p("The chain rhyme pulls the reader forward, line by line, exactly as the traveller is "
                  "pulled onward by his promises. The poem never quite stops, until the repeated last "
                  "line makes it stop.")
              + h4("Common mistake")
              + p("Calling the poem a sonnet. It has four quatrains, not fourteen lines."),
              "lit3_poem", syllabus_item="3.3"),
         card("3.2 Stanza 1: stopping to watch",
              h4("The stanza")
              + p("\"Whose woods these are I think I know. / His house is in the village though; / He "
                  "will not see me stopping here / To watch his woods fill up with snow.\"")
              + h4("Summary")
              + p("The traveller stops on a road beside a wood. He thinks he knows who owns it, and he "
                  "knows the owner is in the village, so no one will see him stop. That privacy lets "
                  "him enjoy the sight of snow filling the trees.")
              + h4("What the stanza establishes")
              + table(["Detail", "Effect"],
                      [("\"I think I know\"", "not quite certain; the speaker is a visitor, not an "
                                              "owner"),
                       ("\"His house is in the village\"", "the human world is close but absent"),
                       ("\"He will not see me\"", "a private moment, almost stolen"),
                       ("\"fill up with snow\"", "slow, silent movement; the woods are becoming "
                                                 "another thing")])
              + h4("Example of a good comment")
              + p("The line \"He will not see me stopping here\" makes the reader a companion in a "
                  "small act of trespass that harms nothing.")
              + h4("Common mistake")
              + p("Saying the speaker is trespassing in a serious sense. He is on the road, looking at "
                  "the woods; the point is that he has permission to look, not to enter."),
              syllabus_item="3.3"),
         card("3.3 Stanza 2: the horse's view",
              h4("The stanza")
              + p("\"My little horse must think it queer / To stop without a farmhouse near / Between "
                  "the woods and frozen lake / The darkest evening of the year.\"")
              + h4("Summary")
              + p("The speaker imagines what the horse makes of the stop. There is no farmhouse to "
                  "explain it: only woods on one side, a frozen lake on the other, and the year's "
                  "darkest evening.")
              + h4("What the stanza adds")
              + ul("A second point of view - the horse stands for the practical world that expects the "
                   "journey to continue.",
                   "A colder, emptier landscape: <i>frozen lake</i>, <i>darkest evening</i>.",
                   "The first hint that the stop is unusual, not simply a rest.")
              + h4("Examples of detail you can quote")
              + p("\"The darkest evening of the year\" places the moment at the winter solstice: the "
                  "longest night, the deepest dark, the point at which a journey feels hardest.")
              + h4("Common mistake")
              + p("Reading the horse as a comic detail. It is the poem's voice of ordinary sense - the "
                  "one that will finally get the traveller home."),
              syllabus_item="3.3"),
         card("3.4 Stanza 3: the sound of the snow",
              h4("The stanza")
              + p("\"He gives his harness bells a shake / To ask if there is some mistake. / The only "
                  "other sound's the sweep / Of easy wind and downy flake.\"")
              + h4("Summary")
              + p("The horse shakes its harness bells, as if asking whether they have stopped by "
                  "mistake. Apart from the bells there is only the soft sweep of wind and falling "
                  "snow.")
              + h4("What the stanza does")
              + table(["Sound", "Effect"],
                      [("harness bells", "a small, sharp, human-made sound"),
                       ("easy wind", "soft, continuous, natural"),
                       ("downy flake", "snowfall so light it is almost silent"),
                       ("the contrast of the three", "the silence is not empty; it is full of quiet "
                                                     "sound")])
              + h4("Example of a comment")
              + p("Frost makes silence audible: after the bells stop, the reader hears the wind "
                  "because there is nothing else to hear.")
              + h4("Common mistake")
              + p("Calling the poem silent. It is full of quiet sound - that is a different thing, and "
                  "a better observation."),
              syllabus_item="3.3"),
         card("3.5 Stanza 4: the promises",
              h4("The stanza")
              + p("\"The woods are lovely, dark and deep, / But I have promises to keep, / And miles to "
                  "go before I sleep, / And miles to go before I sleep.\"")
              + h4("Summary")
              + p("The speaker admits the woods are beautiful - lovely, dark and deep - and then turns "
                  "away from them. He has promises to keep and a long way still to travel before he "
                  "can sleep. The last line repeats, and the poem ends without his moving.")
              + h4("Reading the ending")
              + table(["Reading", "Support"],
                      [("Duty before beauty", "\"But I have promises to keep\""),
                       ("Tiredness", "the repeated line sounds like a sigh"),
                       ("Resolve", "the repetition is a decision, said twice to be believed"),
                       ("A hint of death", "\"sleep\" can mean rest, or the long sleep, but the poem "
                                           "does not say so")])
              + h4("Example of a balanced comment")
              + p("The repetition can be heard both ways at once: the traveller is weary enough to "
                  "want the woods and dutiful enough to leave them. Frost does not choose for the "
                  "reader.")
              + h4("Common mistake")
              + p("Announcing that the poem is \"about death\". It can be read that way, but a good "
                  "answer gives the literal journey first and the deeper reading second, marked as a "
                  "reading."),
              syllabus_item="3.3"),
         card("3.6 Themes and symbols",
              h4("Themes")
              + table(["Theme", "Evidence"],
                      [("The pull of beauty and the pull of duty", "the woods against the promises"),
                       ("Solitude and privacy", "\"He will not see me stopping here\""),
                       ("The journey of life", "\"miles to go before I sleep\""),
                       ("Human responsibility", "\"promises to keep\"")])
              + h4("Symbols")
              + table(["Symbol", "Suggests"],
                      [("the woods", "beauty, rest, withdrawal, and maybe death"),
                       ("snow", "silence, purity, cold, change"),
                       ("the frozen lake", "stillness, a hard season"),
                       ("the horse", "ordinary life and its duties"),
                       ("the miles", "the work still to be done"),
                       ("sleep", "rest, or the end of life")])
              + h4("Example of a theme answer")
              + p("The poem sets two goods against each other - the loveliness of the woods and the "
                  "claims of a promise - and lets the traveller choose the harder one, without "
                  "pretending the choice is easy.")
              + h4("Common mistake")
              + p("Using a symbol without evidence. Say \"the woods suggest rest, because the traveller "
                  "longs to stay and must leave\" - symbol plus reason."),
              syllabus_item="3.3"),
         card("3.7 Poetic devices",
              h4("Devices with examples from the poem")
              + table(["Device", "Example", "Effect"],
                      [("Rhyme (chain rhyme)", "aaba bbcb ccdc dddd", "pulls the reader forward"),
                       ("Repetition", "\"And miles to go before I sleep\" twice", "weariness and "
                                                                                "resolve together"),
                       ("Alliteration", "\"sound's the sweep\", \"downy flake\"", "imitates soft "
                                                                                  "movement and sound"),
                       ("Personification", "the woods \"fill up with snow\"; the horse \"thinks\" and "
                                           "\"asks\"", "gives the scene a quiet inner life"),
                       ("Imagery", "\"easy wind and downy flake\"", "appeals to touch and hearing"),
                       ("Symbolism", "woods, snow, sleep", "carries the deeper meaning"),
                       ("Contrast", "lovely woods / promises to keep", "creates the poem's tension"),
                       ("Understatement", "\"But I have promises to keep\"", "the plain word "
                                                                            "\"but\" carries the "
                                                                            "whole choice")])
              + h4("How to write a device answer")
              + p("Name the device, quote it, then say what it does. For example: <i>The alliteration "
                  "in \"sound's the sweep\" slows the line down, so the reader hears the softness of "
                  "the wind.</i>")
              + h4("Common mistake")
              + p("Listing ten devices without a single effect. Two devices explained well score more "
                  "than ten named."),
              syllabus_item="3.3"),
         card("3.8 Central idea and exam notes",
              h4("Central idea")
              + p("A traveller stops to watch snow falling in woods he does not own, and then moves on "
                  "because he has promises to keep. The small event carries a large idea: beauty and "
                  "rest are real, and so are duty and the journey; a grown life is the balancing of "
                  "the two.")
              + h4("Answer plan for \"Explain the central idea of the poem\"")
              + ol("One sentence: what happens in the poem.",
                   "The attraction of the woods (stanza 1-3).",
                   "The pull of the promises (stanza 4).",
                   "The repetition and what it suggests.",
                   "One sentence on why the poem still matters.")
              + h4("Questions that are usually asked")
              + table(["Question", "Short answer"],
                      [("Why does the speaker stop?", "to watch the woods fill up with snow"),
                       ("Why does he not stay?", "he has promises to keep and miles to travel"),
                       ("What does the horse do?", "shakes its harness bells, as if asking why they "
                                                   "stopped"),
                       ("What is the rhyme scheme?", "aaba bbcb ccdc dddd"),
                       ("Name two devices.", "repetition and alliteration, with examples")])
              + h4("Common mistake")
              + p("Writing a summary and stopping there. The question asks for the idea, so the "
                  "summary must lead to a statement about duty, beauty or rest."),
              syllabus_item="3.3"),
     ]},

    {"title": tr("4. Practice Questions with Model Answers"),
     "items": []},
]

EQUATIONS = [
    {"title": tr("The three texts at a glance"),
     "items": [
         {"terms": tr("The Leopard - author"), "a": tr("Ruskin Bond, Indian writer of the Himalayan "
                                                       "foothills")},
         {"terms": tr("The Leopard - one line"), "a": tr("a leopard trusts a daily walker, hunters "
                                                         "kill it for its skin, the forest falls "
                                                         "silent")},
         {"terms": tr("After Twenty Years - author"), "a": tr("O. Henry, American master of the twist "
                                                             "ending")},
         {"terms": tr("After Twenty Years - one line"), "a": tr("a reunion after twenty years ends "
                                                               "in an arrest by a friend's "
                                                               "colleague")},
         {"terms": tr("Stopping by Woods - poet"), "a": tr("Robert Frost, American poet of rural New "
                                                          "England")},
         {"terms": tr("Stopping by Woods - one line"), "a": tr("a traveller watches snow in the woods, "
                                                              "then leaves for the promises he must "
                                                              "keep")},
     ]},
    {"title": tr("Poem form"),
     "items": [
         {"terms": tr("Stanzas"), "a": tr("four quatrains")},
         {"terms": tr("Rhyme scheme"), "a": tr("aaba bbcb ccdc dddd")},
         {"terms": tr("Metre"), "a": tr("iambic tetrameter, four beats a line")},
         {"terms": tr("Repeated line"), "a": tr("\"And miles to go before I sleep\"")},
     ]},
]

VIVA = [
    {"title": tr("The Leopard"),
     "items": [
         {"q": tr("Who wrote The Leopard, and where is it set?"),
          "a": tr("Ruskin Bond wrote it; it is set in a deep ravine with a stream below a hill station "
                  "in the Himalayan foothills.")},
         {"q": tr("Why do the animals of the ravine accept the narrator?"),
          "a": tr("He walks the same path quietly every day and carries no gun, so the birds and "
                  "animals stop treating him as a danger.")},
         {"q": tr("How does the narrator meet the leopard?"),
          "a": tr("He sees it drinking at the stream one evening; both freeze, and over the following "
                  "days the meetings repeat until neither runs away.")},
         {"q": tr("What do the hunters ask him, and what does he answer?"),
          "a": tr("They ask whether he has seen the leopard; he says he has seen nothing, which "
                  "protects it for a time.")},
         {"q": tr("What does the story say about the price of a leopard skin?"),
          "a": tr("The hunters say that skins sell in Delhi for more than a thousand rupees each, "
                  "which turns the animal into a market price.")},
         {"q": tr("How does the story end?"),
          "a": tr("The hunters kill the leopard and take the skin; the forest falls silent, and the "
                  "narrator feels that the animals know their trust has been violated.")},
         {"q": tr("State two themes of The Leopard."),
          "a": tr("Man against nature, and trust betrayed for money; the story also warns about the "
                  "shrinking forest as the hill station grows.")},
     ]},
    {"title": tr("After Twenty Years"),
     "items": [
         {"q": tr("Where and when does the story take place?"),
          "a": tr("On a New York street at about ten at night, where a hardware store now stands "
                  "where \"Big Joe\" Brady's restaurant used to be.")},
         {"q": tr("What promise does Bob keep?"),
          "a": tr("Twenty years ago he and Jimmy Wells agreed to meet at the same spot at the same "
                  "hour; Bob has come from the West to keep that appointment.")},
         {"q": tr("Who is the first policeman, and why does it matter?"),
          "a": tr("He is Jimmy Wells, though the reader does not know it; he recognises Bob in the "
                  "matchlight and later sends another officer to arrest him.")},
         {"q": tr("How does Bob discover that the tall man is not Jimmy?"),
          "a": tr("Under a street light he sees the nose: twenty years may change many things, but not "
                  "a Roman nose into a pug nose.")},
         {"q": tr("What does Jimmy's note say?"),
          "a": tr("That he came on time, recognised Bob as the man wanted in Chicago when he struck "
                  "the match, could not arrest him himself, and so sent a plain-clothes officer.")},
         {"q": tr("State the main conflict in the story."),
          "a": tr("Friendship against duty: Jimmy keeps the appointment as a friend but has to act as "
                  "a policeman.")},
         {"q": tr("Why is the title appropriate?"),
          "a": tr("The whole story is measured by twenty years - the promise, the changes in the city "
                  "and in the two men, and the arrest that the years have made inevitable.")},
     ]},
    {"title": tr("Stopping by Woods"),
     "items": [
         {"q": tr("Who wrote the poem, and when was it published?"),
          "a": tr("Robert Frost; it was written in 1922 and published in 1923 in the collection New "
                  "Hampshire.")},
         {"q": tr("Why does the traveller stop?"),
          "a": tr("To watch the woods fill up with snow, in a place where the owner lives in the "
                  "village and will not see him.")},
         {"q": tr("What is the rhyme scheme?"),
          "a": tr("aaba bbcb ccdc dddd - the third line of each stanza sets up the rhyme of the next.")},
         {"q": tr("What does the horse do, and why?"),
          "a": tr("It shakes its harness bells as if asking whether there is some mistake, because "
                  "they have stopped with no farmhouse near.")},
         {"q": tr("Why does the traveller not stay in the woods?"),
          "a": tr("He has promises to keep and miles to go before he sleeps, so duty takes him away "
                  "from the beauty he is watching.")},
         {"q": tr("Name two poetic devices used in the poem."),
          "a": tr("Repetition in the closing line, and alliteration in \"sound's the sweep\" and "
                  "\"downy flake\".")},
     ]},
]

_PRACTICE = [
    ("Describe the setting of The Leopard and explain why it matters to the story.", 4,
     [p("The story is set in a deep ravine below a hill station in the Himalayan foothills, a place of "
        "ferns, moss, running water and small animals, which almost nobody from the town visits."),
      p("The narrator walks there every day and, because he is quiet and unarmed, the birds and "
        "animals come to accept him. That acceptance is what makes the meeting with the leopard "
        "possible."),
      p("The ravine therefore works as a refuge: it shelters the leopard and gives the narrator a "
        "private world. When the hunters arrive and kill the leopard, the same place falls silent, so "
        "the setting carries the loss as well as the beauty.")]),
    ("Summarise the plot of The Leopard in about 150 words.", 4,
     [p("The narrator lives near a hill station and walks daily in a ravine below it, where the birds "
        "and animals grow used to him. One evening he sees a leopard drinking at the stream, and over "
        "the following weeks the two learn to share the place without fear or friendship - a "
        "tolerance, not a taming."),
      p("Hunters then arrive looking for a leopard, and ask him whether he has seen one. He says he "
        "has seen nothing, although he knows exactly where it drinks. They talk of skins selling in "
        "Delhi for over a thousand rupees each."),
      p("The hunters eventually find and kill the leopard and take the skin. The narrator walks home "
        "through a forest that has gone silent, feeling that the birds and animals know their trust "
        "has been violated.")]),
    ("What is the theme of The Leopard? Support your answer with evidence from the story.", 4,
     [p("The central theme is the conflict between man and nature, and the way trust is betrayed for "
        "money."),
      p("The leopard learns not to fear the narrator because he never harms it, and the two share the "
        "ravine in silence. When the hunters come, they value the animal only as a skin worth more "
        "than a thousand rupees in Delhi - the narrator's silence delays them but cannot stop them."),
      p("Bond closes with a silent forest and the thought that the animals know their trust has been "
        "violated, so the theme is carried by the setting as much as by the events.")]),
    ("Sketch the character of the narrator in The Leopard.", 3,
     [p("He is a writer and a daily walker: quiet, patient and observant, and he carries no gun."),
      p("His love of the ravine is shown in the small things he notices - the stream, a bird call, a "
        "deer lifting its head - and in the way the animals accept him."),
      p("His one action is a refusal: asked by the hunters whether he has seen the leopard, he says he "
        "has seen nothing. It is honest to the animal and dishonest to the men, and it is not enough. "
        "That limitation is what makes him a believable character.")]),
    ("How does the story After Twenty Years end, and why is the ending effective?", 4,
     [p("Bob waits in a doorway for Jimmy Wells, the friend he has not seen for twenty years. A "
        "policeman on the beat hears his story and moves on; twenty minutes later a tall man greets "
        "him as Jimmy and they walk arm in arm."),
      p("Under a street light Bob sees the nose and knows the man is not Jimmy. The stranger is a "
        "plain-clothes officer, and Bob has been under arrest for ten minutes. He hands Bob a note."),
      p("In the note Jimmy explains that he came on time, recognised Bob as the man wanted in Chicago "
        "when he struck the match, and could not arrest him himself, so he sent another officer. The "
        "ending is effective because every clue was in plain sight, and because the friend who kept "
        "faith is the one who had to act against his friend.")]),
    ("Compare the characters of Bob and Jimmy Wells.", 4,
     [p("Bob is impulsive, talkative and sentimental. He has gone West, made money and wears a "
        "diamond-set watch, and he keeps the appointment exactly - but he is also the man wanted in "
        "Chicago, so his success has a criminal price."),
      p("Jimmy is steady and dutiful. He stayed in New York and became a policeman, and he too keeps "
        "the appointment, though for him it means standing in uniform and recognising his friend's "
        "face."),
      p("Both men are loyal, and that is the point of the comparison: the same loyalty leads one to a "
        "doorway and the other to a note that ends the meeting in an arrest.")]),
    ("What is the theme of After Twenty Years? Give evidence.", 4,
     [p("The main theme is the conflict between friendship and duty."),
      p("Jimmy Wells keeps the promise made twenty years earlier, which shows his loyalty as a friend. "
        "But when the matchlight shows him Bob's face, he knows he is looking at a wanted man, and he "
        "sends a plain-clothes officer rather than let him go."),
      p("O. Henry adds a second theme, time and change: the restaurant has become a hardware store, "
        "Bob's fortune has made him a criminal, and only the promise has stayed as it was. The note "
        "brings both themes together in one short paragraph.")]),
    ("Why is the title After Twenty Years appropriate?", 3,
     [p("Every important thing in the story is measured by twenty years: the promise made in the "
        "restaurant, the separate lives the two friends have lived, and the changes in the street and "
        "in the men."),
      p("The title also carries the story's irony. Bob expects the years to have preserved his friend, "
        "and they have - but they have also turned Bob into a man his friend must arrest."),
      p("Without giving the twist away, the title sets the reader thinking about time, which is "
        "exactly what the last paragraph turns on.")]),
    ("Summarise the poem Stopping by Woods on a Snowy Evening stanza by stanza.", 5,
     [p("Stanza 1: the traveller stops beside woods that he thinks he knows; the owner lives in the "
        "village and will not see him watching the woods fill up with snow."),
      p("Stanza 2: he imagines that his little horse finds the stop strange, since there is no "
        "farmhouse near - only woods, a frozen lake and the darkest evening of the year."),
      p("Stanza 3: the horse shakes its harness bells as if asking whether there is a mistake, and "
        "the only other sound is the sweep of easy wind and downy snow."),
      p("Stanza 4: he calls the woods lovely, dark and deep, but says he has promises to keep and "
        "miles to go before he sleeps; the last line is repeated, and the poem ends without his "
        "moving.")]),
    ("What is the central idea of Stopping by Woods on a Snowy Evening?", 4,
     [p("The poem is about the pull of two things at once: the beauty and rest offered by the woods, "
        "and the duty that requires the traveller to move on."),
      p("For three stanzas he simply watches - the snow, the dark, the horse's bells - and the poem "
        "lets the reader feel how attractive that stillness is."),
      p("Then the word \"But\" turns the poem: he has promises to keep and miles to go before he "
        "sleeps. The repeated last line sounds both weary and resolved, so the central idea is not "
        "that duty wins easily, but that it wins at a cost.")]),
    ("Name four poetic devices used in the poem with examples.", 4,
     [p("<b>Repetition:</b> \"And miles to go before I sleep\" is repeated, which makes the line sound "
        "like a decision said twice."),
      p("<b>Alliteration:</b> \"sound's the sweep\" and \"downy flake\" repeat soft consonants, so the "
        "line moves slowly, like the snow."),
      p("<b>Personification:</b> the horse \"thinks\" and \"asks\", and the woods \"fill up with "
        "snow\", which gives the scene an inner life. <b>Symbolism:</b> the woods suggest rest or "
        "withdrawal, the miles suggest the work still to be done.")]),
    ("Justify the last stanza as the heart of the poem.", 4,
     [p("The first three stanzas build an atmosphere: snow, darkness, a frozen lake, a horse's bells "
        "and then a deep quiet."),
      p("The last stanza names the choice in four short lines. \"The woods are lovely, dark and "
        "deep\" admits the attraction; \"But I have promises to keep\" states the claim that "
        "overrides it; the two closing lines measure the distance still to be travelled."),
      p("The rhyme also completes itself here, with all four lines rhyming, so the poem's form settles "
        "at the same moment as its meaning.")]),
    ("Compare the treatment of nature in The Leopard and Stopping by Woods on a Snowy Evening.", 4,
     [p("In Bond's story nature is a shared place: the ravine is home to the narrator, the birds, the "
        "deer and the leopard, and the drama is about whether a human being can live there without "
        "harming it. The hunters enter that place and destroy it for money."),
      p("In Frost's poem nature is a beauty that asks nothing: the woods belong to somebody else and "
        "are simply watched. No one is harmed, and the tension is inside the traveller, between "
        "watching and leaving."),
      p("So Bond writes about responsibility towards nature, and Frost about the human cost of "
        "leaving it; both make a quiet place the centre of the story.")]),
    ("What moral do you draw from After Twenty Years?", 3,
     [p("The story asks whether a person can be both loyal and just, and answers that he can, but only "
        "by giving up the pleasure of the meeting."),
      p("Jimmy Wells does not betray his friend and does not break the law: he comes, he recognises, "
        "he steps aside and leaves a note that explains everything."),
      p("The moral is that true friendship is not the same as shielding someone from the consequences "
        "of his choices - and that the honest course usually costs the person who takes it.")]),
    ("How does Frost create a sense of silence in the poem?", 3,
     [p("He does it with sound rather than its absence. The only sounds named are the horse's harness "
        "bells and the sweep of easy wind and downy flake, and they are quiet ones."),
      p("The bells come first, sharp and brief, so that the soft wind is heard more clearly afterwards. "
        "Words like \"easy\" and \"downy\" slow the line down."),
      p("The final stanza has no sound image at all, only the repeated line, so the silence of the "
        "ending is created by the withdrawal of detail.")]),
]

EXAM = [{"q": tr(q), "marks": m} for q, m, _parts in _PRACTICE]
PRACTICE_ANSWERS = [tr("".join(parts)) for _q, _m, parts in _PRACTICE]

LESSON_COUNT = sum(len(s["items"]) for s in NOTES)
