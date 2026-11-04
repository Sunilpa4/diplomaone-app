"""DI01000031 Communication Skills in English - Unit 2: Grammar.

GTU 2.1-2.5, 10 h, 40 %, 28 marks, CO2: construct grammatically correct sentences.

Author's policy for this subject (user instruction): grammar is taught by example - one rule line,
then tables of forms and model sentences. No long theory paragraphs.
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


def eg(title, items):
    return h4(title) + ul(*items)


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
    ("Cambridge Dictionary - grammar reference",
     "https://dictionary.cambridge.org/grammar/british-grammar/"),
    ("British Council LearnEnglish - English grammar",
     "https://learnenglish.britishcouncil.org/grammar"),
    ("N. K. Aggrawal - Essentials of English Grammar and Composition (Goyal Brothers, 2015)",
     "https://www.goyalpublishers.com/"),
    ("W. S. Allen - Living English Structures (Pearson Education India)",
     "https://www.pearson.com/"),
]

NOTES = [
    {"title": tr("1. Parts of Speech"),
     "items": [
         card("1.1 Noun",
              h4("Rule")
              + p("A <b>noun</b> names a person, place, thing or idea.")
              + h4("Five kinds, with examples")
              + table(["Kind", "What it names", "Examples"],
                      [("Proper", "one particular name, always with a capital",
                        "Surat, Gujarat, Ashok, TATA, Monday"),
                       ("Common", "any one of a class", "engineer, motor, workshop, city"),
                       ("Collective", "a group as one unit", "team, crowd, batch, fleet"),
                       ("Material", "what a thing is made of", "steel, brass, rubber, cement"),
                       ("Abstract", "a quality, state or idea", "honesty, safety, patience, speed")])
              + h4("Countable and uncountable")
              + ul("<b>Countable:</b> one bolt, two bolts, three bolts.",
                   "<b>Uncountable:</b> water, oil, information, advice, equipment, furniture - "
                   "no plural, no <i>a</i>.")
              + h4("Examples in sentences")
              + eg("Same noun doing different work", [
                  "The <b>motor</b> is hot. (subject)",
                  "We replaced the <b>motor</b>. (object)",
                  "The <b>motor</b> casing cracked. (modifier)",
                  "<b>Ashok</b> works in the <b>tool room</b> at <b>TATA Motors</b>."])
              + h4("Common mistake")
              + p("\"Informations\", \"advices\", \"equipments\" and \"furnitures\" do not exist. Say "
                  "\"a piece of information\", \"two pieces of equipment\"."),
              "g1_pos", syllabus_item="2.1"),
         card("1.2 Verb",
              h4("Rule")
              + p("A <b>verb</b> shows an action (run, weld, check) or a state (be, seem, have, know).")
              + h4("Kinds of verb")
              + table(["Kind", "Work", "Examples"],
                      [("Main / lexical", "carries the meaning", "weld, replace, measure, fail"),
                       ("Auxiliary", "helps the main verb", "is, are, was, has, have, do, will, can"),
                       ("Transitive", "needs an object", "replace <i>the belt</i>, check <i>the oil</i>"),
                       ("Intransitive", "no object needed", "run, arrive, sleep, rise"),
                       ("Regular", "past in -ed", "check → checked, test → tested"),
                       ("Irregular", "past changes form", "write → wrote → written, run → ran → run")])
              + h4("Examples")
              + eg("Auxiliary + main verb", [
                  "The pump <b>is running</b>.",
                  "We <b>have replaced</b> the seal.",
                  "The belt <b>was slipping</b>.",
                  "He <b>can weld</b> aluminium."])
              + h4("Common mistake")
              + p("Dropping the auxiliary: \"He going to the site\" is wrong; write \"He is going to "
                  "the site\"."),
              syllabus_item="2.1"),
         card("1.3 Pronoun",
              h4("Rule")
              + p("A <b>pronoun</b> stands in place of a noun so that the noun is not repeated.")
              + h4("Kinds, with examples")
              + table(["Kind", "Examples"],
                      [("Personal (subject / object)", "I / me, we / us, he / him, they / them"),
                       ("Possessive", "my, our, his, their, mine, ours"),
                       ("Reflexive", "myself, ourselves, himself, themselves"),
                       ("Demonstrative", "this, that, these, those"),
                       ("Relative", "who, whom, which, that, whose"),
                       ("Interrogative", "who? what? which? whose?"),
                       ("Indefinite", "someone, anything, everybody, none")])
              + h4("Examples")
              + eg("In sentences", [
                  "<b>She</b> checked the panel and <b>I</b> recorded the reading.",
                  "The bearing <b>that</b> failed was new.",
                  "<b>This</b> is the drawing; <b>those</b> are the spares.",
                  "The fitter repaired it <b>himself</b>."])
              + h4("Common mistake")
              + p("\"Myself Raj\" and \"Please contact to myself\" are wrong. Write \"I am Raj\" and "
                  "\"Please contact me\"."),
              syllabus_item="2.1"),
         card("1.4 Adjective",
              h4("Rule")
              + p("An <b>adjective</b> describes or limits a noun: a <i>hot</i> motor, <i>three</i> "
                  "bolts, <i>brass</i> washers.")
              + h4("Kinds")
              + table(["Kind", "Examples"],
                      [("Quality", "hot, long, careful, worn"),
                       ("Quantity", "some, enough, little, plenty of"),
                       ("Number", "three, tenth, several"),
                       ("Demonstrative", "this panel, those wires"),
                       ("Possessive", "my tools, their workshop")])
              + h4("Degrees of comparison")
              + table(["Positive", "Comparative", "Superlative"],
                      [("long", "longer", "longest"),
                       ("heavy", "heavier", "heaviest"),
                       ("good", "better", "best"),
                       ("bad", "worse", "worst"),
                       ("careful", "more careful", "most careful")])
              + h4("Order before a noun")
              + p("opinion - size - age - colour - origin - material - noun: <i>a useful small old "
                  "grey Indian steel box</i>.")
              + h4("Examples")
              + eg("Comparison in use", [
                  "This belt is <b>longer</b> than that one.",
                  "Line 2 is the <b>busiest</b> line in the plant.",
                  "Today's reading is <b>better</b> than yesterday's.",
                  "Use the <b>most careful</b> method for the bearing."])
              + h4("Common mistake")
              + p("\"More better\", \"most best\" and \"more easier\" double the comparison. Use one "
                  "form only."),
              syllabus_item="2.1"),
         card("1.5 Adverb",
              h4("Rule")
              + p("An <b>adverb</b> describes a verb, an adjective or another adverb: runs "
                  "<i>smoothly</i>, <i>very</i> hot, <i>quite</i> slowly.")
              + h4("Kinds")
              + table(["Kind", "Question it answers", "Examples"],
                      [("Manner", "how?", "quickly, carefully, badly, well"),
                       ("Time", "when?", "now, yesterday, soon, already"),
                       ("Place", "where?", "here, outside, everywhere"),
                       ("Frequency", "how often?", "always, often, rarely, never"),
                       ("Degree", "how much?", "very, too, almost, enough")])
              + h4("How they are formed")
              + ul("adjective + -ly: quick → quickly, careful → carefully.",
                   "irregular: good → well, fast → fast, hard → hard, late → late.",
                   "Some words are both: <i>a fast motor</i> (adjective), <i>the motor runs fast</i> "
                   "(adverb).")
              + h4("Examples")
              + eg("Position", [
                  "The pump runs <b>smoothly</b>. (after the verb)",
                  "He <b>carefully</b> measured the bore. (before the verb)",
                  "The line stops <b>twice daily</b>. (frequency at the end)",
                  "The motor is <b>very</b> hot. (degree before an adjective)"])
              + h4("Common mistake")
              + p("\"He works good\" is wrong because <i>good</i> is an adjective; write \"He works "
                  "well\"."),
              syllabus_item="2.1"),
         card("1.6 Preposition",
              h4("Rule")
              + p("A <b>preposition</b> links a noun or pronoun to another word and shows place, time, "
                  "direction or agent: <i>under</i> the bench, <i>at</i> 9 am, <i>by</i> the fitter.")
              + h4("Place and time")
              + table(["Preposition", "Use", "Example"],
                      [("at", "a point, an exact time", "at the gate, at 9 am, at night"),
                       ("on", "a surface, a day or date", "on the bench, on Monday, on 5 March"),
                       ("in", "an enclosed space, a month or year", "in the panel, in May, in 2026"),
                       ("under / over", "below / above", "under the bench, over the pipe"),
                       ("between / among", "two / more than two", "between the two pumps, among the workers"),
                       ("by", "agent, or not later than", "welded by Ashok, by Friday"),
                       ("with", "instrument or company", "cut with a hacksaw, with the supervisor"),
                       ("since / for", "point of time / length of time", "since Monday, for two hours")])
              + h4("Examples")
              + eg("Common pairs", [
                  "The drawing is <b>on</b> the board and the tools are <b>in</b> the box.",
                  "The job must finish <b>by</b> Friday, and it has been open <b>since</b> Monday.",
                  "The fault is <b>between</b> the pump and the tank.",
                  "The report was written <b>by</b> the trainee <b>for</b> the supervisor."])
              + h4("Common mistake")
              + p("\"Discuss about the problem\", \"married with her\", \"different than\" - write "
                  "\"discuss the problem\", \"married to her\", \"different from\"."),
              syllabus_item="2.1"),
         card("1.7 Conjunction",
              h4("Rule")
              + p("A <b>conjunction</b> joins words, phrases or clauses: belt <i>and</i> pulley, stop "
                  "<i>because</i> the guard is loose.")
              + h4("Three kinds")
              + table(["Kind", "Work", "Examples"],
                      [("Coordinating", "joins equals", "and, but, or, so, for, yet, nor"),
                       ("Subordinating", "joins a dependent clause", "because, although, if, when, "
                                                                     "while, since, unless, after"),
                       ("Correlative", "works in pairs", "either ... or, neither ... nor, "
                                                         "not only ... but also, both ... and")])
              + h4("Examples")
              + eg("In sentences", [
                  "The belt <b>and</b> the pulley were replaced.",
                  "The line stopped <b>because</b> the coolant ran out.",
                  "<b>Although</b> the load was high, the motor stayed cool.",
                  "<b>Either</b> the seal <b>or</b> the gland is leaking.",
                  "<b>Neither</b> the fitter <b>nor</b> the helper was present.",
                  "<b>Not only</b> the bearing <b>but also</b> the shaft was damaged."])
              + h4("Common mistake")
              + p("Using two conjunctions for one link: \"Although it was hot, but we finished\" is "
                  "wrong; keep \"Although it was hot, we finished\"."),
              syllabus_item="2.1"),
         card("1.8 Interjection",
              h4("Rule")
              + p("An <b>interjection</b> expresses a sudden feeling. It stands apart from the "
                  "sentence and takes an exclamation mark.")
              + h4("Common interjections")
              + table(["Feeling", "Interjection", "Example"],
                      [("joy", "hurray!, wow!", "Hurray! The test passed."),
                       ("surprise", "oh!, what!", "Oh! The panel is live."),
                       ("pain", "ouch!, ah!", "Ouch! That edge is sharp."),
                       ("relief", "phew!", "Phew! The leak has stopped."),
                       ("sorrow", "alas!", "Alas! The batch is scrap."),
                       ("warning", "hush!, look out!", "Look out! The load is slipping.")])
              + h4("Register")
              + p("Interjections belong in speech and informal writing. A technical report says "
                  "\"The batch was rejected\", not \"Alas! The batch was rejected\".")
              + h4("Common mistake")
              + p("Overusing them in written work. One \"oh\" in a report looks careless; use a plain "
                  "statement instead."),
              syllabus_item="2.1"),
     ]},

    {"title": tr("2. Tenses"),
     "items": [
         card("2.1 Present simple",
              h4("Form")
              + table(["Type", "Structure", "Example"],
                      [("Affirmative", "subject + V1 (V1+s with he/she/it)", "The pump runs."),
                       ("Negative", "do / does + not + V1", "The pump does not run."),
                       ("Question", "do / does + subject + V1?", "Does the pump run?")])
              + h4("Use")
              + ul("Habits and routines: <i>I check the panel every morning.</i>",
                   "Facts and laws: <i>Water boils at 100 °C.</i>",
                   "Timetables: <i>The shift starts at 7 am.</i>",
                   "Instructions: <i>Switch off the mains first.</i>")
              + h4("Examples")
              + eg("Correct forms", [
                  "The fitter <b>checks</b> the oil level daily.",
                  "The fitters <b>check</b> the oil level daily.",
                  "The motor <b>does not draw</b> more than 6 A.",
                  "<b>Do</b> you <b>record</b> the reading in the log book?"])
              + h4("Common mistake")
              + p("\"He run the machine\" - with he, she or it the verb takes -s: \"he runs\"."),
              syllabus_item="2.2"),
         card("2.2 Present continuous",
              h4("Form")
              + table(["Type", "Structure", "Example"],
                      [("Affirmative", "am / is / are + V-ing", "The line is running."),
                       ("Negative", "am / is / are + not + V-ing", "The line is not running."),
                       ("Question", "am / is / are + subject + V-ing?", "Is the line running?")])
              + h4("Use")
              + ul("Happening now: <i>I am checking the bearing.</i>",
                   "Around now, these days: <i>We are using a new coolant.</i>",
                   "Fixed near future: <i>We are starting the trial at 4 pm.</i>",
                   "Complaints with <i>always</i>: <i>He is always losing the spanner.</i>")
              + h4("Examples")
              + eg("Now and around now", [
                  "The compressor <b>is making</b> a noise right now.",
                  "Two operators <b>are working</b> on the panel.",
                  "I <b>am not using</b> the crane today.",
                  "<b>Are</b> you <b>reading</b> the new drawing?"])
              + h4("Common mistake")
              + p("Stative verbs take the simple form: \"I am knowing the answer\" is wrong; write "
                  "\"I know the answer\"."),
              syllabus_item="2.2"),
         card("2.3 Present perfect",
              h4("Form")
              + table(["Type", "Structure", "Example"],
                      [("Affirmative", "have / has + V3", "We have replaced the seal."),
                       ("Negative", "have / has + not + V3", "We have not replaced the seal."),
                       ("Question", "have / has + subject + V3?", "Have you replaced the seal?")])
              + h4("Use")
              + ul("Finished action with a present result: <i>I have finished the job, so the line can "
                   "start.</i>",
                   "Experience with no fixed time: <i>He has worked in three plants.</i>",
                   "With <i>just, already, yet, ever, never, since, for</i>.")
              + h4("Present perfect or past simple?")
              + table(["Present perfect", "Past simple"],
                      [("no time mentioned", "a finished time is named"),
                       ("I have checked the panel.", "I checked the panel at 9 am."),
                       ("He has worked here for 3 years.", "He worked here in 2022.")])
              + h4("Examples")
              + eg("With markers", [
                  "The job <b>has</b> just <b>finished</b>.",
                  "I <b>have</b> not <b>received</b> the drawing yet.",
                  "She <b>has been</b> on this machine <b>since</b> January.",
                  "<b>Have</b> you ever <b>welded</b> aluminium?"])
              + h4("Common mistake")
              + p("\"I have seen him yesterday\" is wrong because <i>yesterday</i> is a finished time; "
                  "write \"I saw him yesterday\"."),
              syllabus_item="2.2"),
         card("2.4 Present perfect continuous",
              h4("Form")
              + table(["Type", "Structure", "Example"],
                      [("Affirmative", "have / has been + V-ing", "He has been welding for an hour."),
                       ("Negative", "have / has not been + V-ing", "He has not been welding."),
                       ("Question", "have / has + subject + been + V-ing?",
                        "Has he been welding since 9 am?")])
              + h4("Use")
              + p("An action that started in the past and is <b>still going on</b> now, usually with "
                  "<i>for</i> (length of time) or <i>since</i> (starting point).")
              + h4("Examples")
              + eg("Still happening", [
                  "The pump <b>has been running for</b> three hours.",
                  "I <b>have been looking for</b> that spanner since morning.",
                  "The line <b>has been stopping</b> repeatedly all week.",
                  "How long <b>have</b> you <b>been working</b> on this panel?"])
              + h4("Present perfect or present perfect continuous?")
              + table(["Perfect: result", "Perfect continuous: duration"],
                      [("I have painted the guard.", "I have been painting the guard."),
                       ("The job is finished.", "The job is still going on.")])
              + h4("Common mistake")
              + p("Using it for a finished amount: \"I have been finishing three jobs\" is wrong; "
                  "write \"I have finished three jobs\"."),
              syllabus_item="2.2"),
         card("2.5 Past simple",
              h4("Form")
              + table(["Type", "Structure", "Example"],
                      [("Affirmative", "subject + V2", "The belt broke."),
                       ("Negative", "did not + V1", "The belt did not break."),
                       ("Question", "did + subject + V1?", "Did the belt break?")])
              + h4("Use")
              + ul("A finished action at a finished time: <i>We replaced the belt yesterday.</i>",
                   "A series of past events: <i>He opened the panel, tested the relay and closed it.</i>",
                   "Past habits: <i>He worked night shift in 2023.</i>")
              + h4("Markers")
              + p("yesterday, last week, in 2024, two days ago, then, after that, when.")
              + h4("Examples")
              + eg("Right and wrong", [
                  "The line <b>stopped</b> at 10:15 am.",
                  "We <b>did not find</b> the cause yesterday.",
                  "<b>Did</b> you <b>check</b> the coolant before starting?",
                  "Wrong: \"We have replaced it yesterday.\" Right: \"We replaced it yesterday.\"",
                  "Wrong: \"He did not checked it.\" Right: \"He did not check it.\""])
              + h4("Common mistake")
              + p("After <i>did</i> or <i>did not</i> the verb stays in V1 - no -ed, no V2."),
              syllabus_item="2.2"),
         card("2.6 Past continuous",
              h4("Form")
              + table(["Type", "Structure", "Example"],
                      [("Affirmative", "was / were + V-ing", "The pump was running."),
                       ("Negative", "was / were + not + V-ing", "The pump was not running."),
                       ("Question", "was / were + subject + V-ing?", "Was the pump running?")])
              + h4("Use")
              + ul("An action in progress at a past moment: <i>At 10 am we were testing the motor.</i>",
                   "A longer action interrupted by a shorter one: <i>I was checking the panel when the "
                   "light went off.</i>",
                   "Two actions going on together: <i>While he was welding, I was grinding.</i>")
              + h4("Examples")
              + eg("With when and while", [
                  "The operator <b>was cleaning</b> the guard when the alarm rang.",
                  "<b>While</b> we <b>were waiting</b>, the supervisor called.",
                  "They <b>were not working</b> after 6 pm.",
                  "<b>Were</b> you <b>testing</b> the relay at that time?"])
              + h4("Common mistake")
              + p("Using it for a completed single action: \"I was replaced the belt\" is wrong; write "
                  "\"I replaced the belt\"."),
              syllabus_item="2.2"),
         card("2.7 Past perfect",
              h4("Form")
              + table(["Type", "Structure", "Example"],
                      [("Affirmative", "had + V3", "The belt had broken."),
                       ("Negative", "had not + V3", "The belt had not broken."),
                       ("Question", "had + subject + V3?", "Had the belt broken?")])
              + h4("Use")
              + p("The <b>earlier</b> of two past actions: both happened in the past, and one happened "
                  "first.")
              + h4("Examples")
              + eg("Which came first?", [
                  "The line was already down when I reached - the belt <b>had broken</b> before 7 am.",
                  "We <b>had</b> already <b>replaced</b> the seal before the inspector arrived.",
                  "He <b>had not</b> <b>checked</b> the torque, so the joint leaked.",
                  "<b>Had</b> you <b>read</b> the manual before you opened the panel?"])
              + h4("Order words")
              + p("before, after, by the time, already, when - these make the order clear: <i>After we "
                  "had tested the pump, we started the line.</i>")
              + h4("Common mistake")
              + p("Using the past perfect for a single past action: \"I had gone to the site "
                  "yesterday\" is unnecessary; write \"I went to the site yesterday\"."),
              syllabus_item="2.2"),
         card("2.8 Future simple",
              h4("Form")
              + table(["Type", "Structure", "Example"],
                      [("Affirmative", "will + V1", "The vendor will deliver on Monday."),
                       ("Negative", "will not (won't) + V1", "The vendor will not deliver today."),
                       ("Question", "will + subject + V1?", "Will the vendor deliver today?")])
              + h4("Use")
              + ul("Prediction: <i>The load will increase in summer.</i>",
                   "Promise or offer: <i>I will send the drawing today.</i>",
                   "Decision taken now: <i>The seal is leaking - I will replace it.</i>",
                   "Polite request: <i>Will you check the panel?</i>")
              + h4("Examples")
              + eg("Plans and predictions", [
                  "We <b>will start</b> the trial tomorrow at 10 am.",
                  "The bearing <b>will not last</b> at this speed.",
                  "<b>Will</b> the spare reach before Friday?",
                  "I <b>will call</b> you after the test."])
              + h4("Common mistake")
              + p("After <i>will</i> the verb never takes -s or a past form: \"will comes\", \"will "
                  "came\" are wrong; write \"will come\". Also \"will can\" is wrong - use \"will be "
                  "able to\"."),
              "g2_tenses", syllabus_item="2.2"),
     ]},

    {"title": tr("3. Modal Auxiliaries"),
     "items": [
         card("3.1 Can and could",
              h4("Rule")
              + p("<b>Can</b> and <b>could</b> express ability, permission, request and possibility. "
                  "They take a bare verb: <i>can weld</i>, not <i>can welds</i>.")
              + h4("Uses and examples")
              + table(["Use", "Example"],
                      [("Ability, present", "I <b>can</b> weld aluminium."),
                       ("Ability, past", "He <b>could</b> weld at sixteen."),
                       ("Permission, informal", "<b>Can</b> I open the panel?"),
                       ("Request, polite", "<b>Could</b> you send the drawing?"),
                       ("Possibility", "The seal <b>could</b> leak at high pressure."),
                       ("Negative ability", "I <b>cannot</b> lift 50 kg alone.")])
              + h4("Examples in a workshop")
              + eg("One form, four jobs", [
                  "\"<b>Can</b> you read this drawing?\" - ability",
                  "\"<b>Can</b> I use the crane for ten minutes?\" - permission",
                  "\"<b>Could</b> you check the torque once more?\" - polite request",
                  "\"The motor <b>could</b> overheat in this weather.\" - possibility"])
              + h4("Common mistake")
              + p("\"He cans weld\" and \"He could to weld\" are both wrong. Modals never take -s and "
                  "never take <i>to</i> (except <i>ought to</i>)."),
              "g3_modal", syllabus_item="2.3"),
         card("3.2 May and might",
              h4("Rule")
              + p("<b>May</b> is formal permission and real possibility; <b>might</b> is a weaker "
                  "possibility.")
              + h4("Uses and examples")
              + table(["Use", "Example"],
                      [("Formal permission", "<b>May</b> I come in, sir?"),
                       ("Giving permission", "You <b>may</b> start the trial."),
                       ("Possibility, strong", "The relay <b>may</b> be faulty."),
                       ("Possibility, weak", "The relay <b>might</b> be faulty, but I doubt it."),
                       ("Wish", "<b>May</b> you succeed in the exam."),
                       ("Prohibition", "Visitors <b>may not</b> enter the shop floor.")])
              + h4("Examples")
              + eg("Choosing between them", [
                  "\"<b>May</b> I borrow the torque wrench?\" - formal, to a senior",
                  "\"The pump <b>may</b> need a new seal.\" - likely",
                  "\"The pump <b>might</b> need a new seal.\" - less certain",
                  "\"<b>May</b> I suggest a shorter route for the pipe?\""])
              + h4("Common mistake")
              + p("\"May you please send it?\" is not a request in modern English; use \"Could you "
                  "please send it?\"."),
              syllabus_item="2.3"),
         card("3.3 Must, should and ought to",
              h4("Rule")
              + ul("<b>Must</b> - strong obligation, order, or a logical certainty.",
                   "<b>Should</b> - advice, expectation, mild obligation.",
                   "<b>Ought to</b> - moral duty or advice; the only modal with <i>to</i>.")
              + h4("Uses and examples")
              + table(["Use", "Example"],
                      [("Strong obligation", "You <b>must</b> wear goggles."),
                       ("Rule or law", "Every panel <b>must</b> be earthed."),
                       ("Logical certainty", "The tank is empty; it <b>must</b> have leaked."),
                       ("Prohibition", "You <b>must not</b> open the panel live."),
                       ("Advice", "You <b>should</b> torque the bolts in two stages."),
                       ("Expectation", "The vendor <b>should</b> call by noon."),
                       ("Duty", "We <b>ought to</b> report the near miss.")])
              + h4("Examples")
              + eg("Same situation, three strengths", [
                  "\"You <b>must</b> isolate the supply.\" - rule",
                  "\"You <b>should</b> isolate the supply.\" - advice",
                  "\"You <b>ought to</b> isolate the supply.\" - duty",
                  "\"You <b>need not</b> isolate it for a visual check.\" - no obligation"])
              + h4("Common mistake")
              + p("<b>Must not</b> is prohibition, <b>need not</b> is no obligation. \"You must not "
                  "come\" and \"You need not come\" are opposite instructions."),
              syllabus_item="2.3"),
         card("3.4 Shall, will and would",
              h4("Rule")
              + ul("<b>Shall</b> - offers and suggestions with I/we; formal rules.",
                   "<b>Will</b> - future, promise, willingness.",
                   "<b>Would</b> - polite request, past habit, unreal condition.")
              + h4("Uses and examples")
              + table(["Use", "Example"],
                      [("Offer", "<b>Shall</b> I open the window?"),
                       ("Suggestion", "<b>Shall</b> we start the trial?"),
                       ("Formal rule", "The contractor <b>shall</b> submit the report weekly."),
                       ("Future", "The line <b>will</b> start at 7 am."),
                       ("Polite request", "<b>Would</b> you check this reading?"),
                       ("Past habit", "He <b>would</b> arrive at 7 am every day."),
                       ("Unreal condition", "If I had the drawing, I <b>would</b> check it.")])
              + h4("Examples")
              + eg("In speech and in writing", [
                  "\"<b>Shall</b> we begin?\" - suggestion in a meeting",
                  "\"The supervisor <b>shall</b> sign the job card.\" - a written rule",
                  "\"I <b>will</b> send it today.\" - promise",
                  "\"<b>Would</b> you mind waiting ten minutes?\" - polite request"])
              + h4("Common mistake")
              + p("\"I will like a coffee\" is wrong; write \"I would like a coffee\". <i>Would</i> "
                  "softens a wish."),
              syllabus_item="2.3"),
         card("3.5 Need and the full modal table",
              h4("Need as a modal")
              + p("<b>Need</b> behaves as a modal in the negative and the question: <i>need not</i>, "
                  "<i>need I?</i> As a normal verb it takes -s and <i>to</i>: <i>he needs to go</i>.")
              + h4("Examples")
              + eg("Need and need not", [
                  "You <b>need not</b> come tomorrow; the job is done.",
                  "The panel <b>need not</b> be opened for a visual check.",
                  "<b>Need</b> I sign both copies?",
                  "He <b>needs to</b> submit the report today. (normal verb)"])
              + h4("All eleven modals by function")
              + table(["Function", "Modals", "Model sentence"],
                      [("Ability", "can, could", "She can weld."),
                       ("Permission", "may, can, could", "May I enter?"),
                       ("Possibility", "may, might, could", "It may rain."),
                       ("Obligation", "must, should, ought to", "You must report it."),
                       ("Advice", "should, ought to", "You should rest."),
                       ("Future and offer", "shall, will, would", "Shall I help?"),
                       ("No obligation", "need not", "You need not wait."),
                       ("Prohibition", "must not, may not", "You must not smoke."),
                       ("Past habit", "would, used to", "He would arrive at 7.")])
              + h4("Common mistake")
              + p("\"You need not to come\" is wrong: after <i>need not</i> the verb is bare - \"you "
                  "need not come\"."),
              syllabus_item="2.3"),
     ]},

    {"title": tr("4. Subject-Verb Agreement"),
     "items": [
         card("4.1 The basic rule",
              h4("Rule")
              + p("A singular subject takes a singular verb; a plural subject takes a plural verb. In "
                  "the present simple the difference is the -s: <i>the motor runs</i>, <i>the motors "
                  "run</i>.")
              + h4("Examples")
              + table(["Subject", "Verb", "Sentence"],
                      [("one machine", "is / runs", "The pump <b>is</b> running."),
                       ("two machines", "are / run", "The pumps <b>are</b> running."),
                       ("he, she, it", "has / does", "It <b>has</b> a new seal."),
                       ("I, we, they, you", "have / do", "They <b>have</b> new seals.")])
              + h4("Find the subject first")
              + eg("Words between subject and verb do not change it", [
                  "The <b>box</b> of bolts <b>is</b> heavy. (subject: box)",
                  "The <b>boxes</b> of bolts <b>are</b> heavy. (subject: boxes)",
                  "The <b>reading</b> on both meters <b>was</b> the same.",
                  "The <b>fitters</b> in the second shift <b>work</b> on line 3."])
              + h4("Common mistake")
              + p("Matching the verb to the nearest noun instead of the subject: \"The list of items "
                  "are ready\" is wrong; write \"The list of items is ready\"."),
              "g4_agreement", syllabus_item="2.4"),
         card("4.2 And, or, and words that do not count",
              h4("Rules")
              + table(["Pattern", "Verb", "Example"],
                      [("A and B", "plural", "The motor and the pump <b>are</b> new."),
                       ("A or B, either ... or, neither ... nor", "nearest subject",
                        "Either the belt or the bearings <b>are</b> worn."),
                       ("A with B, as well as, along with, together with", "first subject",
                        "The supervisor, along with two fitters, <b>was</b> present."),
                       ("Each / every + singular", "singular",
                        "Each machine <b>has</b> its own meter."),
                       ("Two subjects seen as one pair", "singular",
                        "Bread and butter <b>is</b> his breakfast.")])
              + h4("Examples")
              + eg("In sentences", [
                  "The fitter and the helper <b>were</b> on site.",
                  "<b>Neither</b> the seal <b>nor</b> the gland <b>was</b> damaged.",
                  "<b>Neither</b> the seals <b>nor</b> the gland <b>was</b> damaged.",
                  "The manager, with his team, <b>is</b> visiting the plant."])
              + h4("Common mistake")
              + p("\"As well as\" is not <i>and</i>: \"The pump as well as the motor are new\" should "
                  "be \"is new\"."),
              syllabus_item="2.4"),
         card("4.3 Collective nouns, uncountables and amounts",
              h4("Collective nouns")
              + p("A group noun takes a singular verb when the group acts as one unit, and a plural "
                  "verb when the members act separately.")
              + eg("Examples", [
                  "The <b>team is</b> ready for the trial. (one unit)",
                  "The <b>team are</b> arguing among themselves. (members)",
                  "The <b>batch has</b> been dispatched.",
                  "The <b>staff is</b> trained in first aid."])
              + h4("Uncountables and amounts")
              + table(["Subject", "Verb", "Example"],
                      [("uncountable", "singular", "The water <b>is</b> hot."),
                       ("a sum of money", "singular", "Fifty rupees <b>is</b> enough."),
                       ("a distance or period", "singular", "Ten kilometres <b>is</b> a long walk."),
                       ("a pair", "plural", "The scissors <b>are</b> blunt.")])
              + h4("Common mistake")
              + p("\"The equipment are new\" is wrong; <i>equipment</i>, <i>information</i>, "
                  "<i>advice</i> and <i>furniture</i> are uncountable and take singular verbs."),
              syllabus_item="2.4"),
         card("4.4 Indefinite subjects and there is / there are",
              h4("Rules")
              + table(["Subject", "Verb", "Example"],
                      [("everyone, everybody, someone, nobody, each, either, neither", "singular",
                        "Everybody <b>is</b> ready."),
                       ("none of + plural", "singular or plural", "None of the bolts <b>is</b> loose."),
                       ("some / most / half of + plural", "plural",
                        "Most of the fitters <b>are</b> trained."),
                       ("some / most / half of + uncountable", "singular",
                        "Most of the oil <b>has</b> leaked."),
                       ("there is + singular", "singular", "<b>There is</b> one spare left."),
                       ("there are + plural", "plural", "<b>There are</b> two spares left.")])
              + h4("Examples")
              + eg("Agreement in practice", [
                  "<b>Nobody</b> <b>knows</b> the cause yet.",
                  "<b>Each of the panels</b> <b>has</b> a label.",
                  "<b>None of the readings</b> <b>is</b> outside the limit.",
                  "<b>There are</b> three items on the checklist."])
              + h4("Common mistake")
              + p("\"Everyone are here\" and \"There is two spares\" are wrong. <i>Everyone</i> is "
                  "singular; <i>two spares</i> is plural."),
              syllabus_item="2.4"),
         card("4.5 Five traps that come up in exams",
              h4("The traps")
              + table(["Trap", "Right", "Why"],
                      [("news, mathematics, physics", "The news <b>is</b> good.",
                        "-s but singular"),
                       ("police, cattle, people", "The police <b>are</b> here.", "always plural"),
                       ("one of + plural noun", "One of the bolts <b>is</b> missing.",
                        "the subject is <i>one</i>"),
                       ("a number of + plural", "A number of faults <b>were</b> found.",
                        "means <i>many</i>"),
                       ("the number of + plural", "The number of faults <b>was</b> small.",
                        "means <i>the count</i>"),
                       ("percentage or fraction", "Ten per cent of the batch <b>was</b> rejected.",
                        "agrees with the noun after <i>of</i>")])
              + h4("Examples")
              + eg("Corrected sentences", [
                  "Wrong: \"The news are bad.\" Right: \"The <b>news is</b> bad.\"",
                  "Wrong: \"One of the pumps are leaking.\" Right: \"One of the pumps <b>is</b> "
                  "leaking.\"",
                  "Wrong: \"A number of men was present.\" Right: \"A number of men <b>were</b> "
                  "present.\"",
                  "Wrong: \"Twenty per cent of the oil have leaked.\" Right: \"Twenty per cent of the "
                  "oil <b>has</b> leaked.\""])
              + h4("Common mistake")
              + p("Reading \"one of the pumps\" and matching <i>are</i> to <i>pumps</i>. The subject "
                  "is <i>one</i>."),
              syllabus_item="2.4"),
     ]},

    {"title": tr("5. Basic Sentence Patterns"),
     "items": [
         card("5.1 SV: subject + verb",
              h4("Rule")
              + p("<b>SV</b> is the shortest complete sentence: a subject and an intransitive verb. "
                  "Nothing else is needed.")
              + h4("Examples")
              + table(["Subject", "Verb", "Full sentence"],
                      [("The motor", "failed", "The motor failed."),
                       ("The line", "stopped", "The line stopped."),
                       ("The pump", "leaked", "The pump leaked."),
                       ("The bell", "rang", "The bell rang."),
                       ("The operator", "left", "The operator left.")])
              + h4("Longer SV sentences")
              + eg("Still SV, with extra information", [
                  "The motor <b>failed</b> suddenly. (adverb added)",
                  "The line <b>stopped</b> at ten. (time added)",
                  "The pump <b>leaked</b> badly. (adverb added)",
                  "The old motor on line 2 <b>failed</b>. (subject expanded)"])
              + h4("Common mistake")
              + p("Adding an object to an intransitive verb: \"The motor failed the test\" changes the "
                  "meaning; if you name what failed, you need a transitive verb (<i>damaged, stopped, "
                  "broke</i>)."),
              "g5_patterns", syllabus_item="2.5"),
         card("5.2 SVO: subject + verb + object",
              h4("Rule")
              + p("<b>SVO</b> uses a transitive verb, and the object answers <i>what?</i> or "
                  "<i>whom?</i> after the verb.")
              + h4("Examples")
              + table(["Subject", "Verb", "Object", "Sentence"],
                      [("The fitter", "replaced", "the belt", "The fitter replaced the belt."),
                       ("The operator", "checked", "the oil", "The operator checked the oil."),
                       ("We", "tested", "the relay", "We tested the relay."),
                       ("The company", "ordered", "two pumps", "The company ordered two pumps."),
                       ("She", "signed", "the job card", "She signed the job card.")])
              + h4("Find the object")
              + eg("Question test", [
                  "\"The helper cleaned the filter.\" - cleaned <i>what</i>? the filter → SVO",
                  "\"The helper cleaned carefully.\" - cleaned <i>how</i>? → SV (A), no object",
                  "\"We tested the relay at 4 pm.\" - tested <i>what</i>? the relay → SVO"])
              + h4("Common mistake")
              + p("Putting the object in the wrong place: \"Replaced the fitter the belt\" is wrong; "
                  "the order is subject, verb, object."),
              syllabus_item="2.5"),
         card("5.3 SVA: subject + verb + adverbial",
              h4("Rule")
              + p("<b>SVA</b> needs an adverbial - a word or phrase saying where, when or how - "
                  "because without it the sentence is incomplete.")
              + h4("Examples")
              + table(["Subject", "Verb", "Adverbial", "Sentence"],
                      [("The pump", "runs", "smoothly", "The pump runs smoothly."),
                       ("He", "lives", "in Surat", "He lives in Surat."),
                       ("The line", "starts", "at 7 am", "The line starts at 7 am."),
                       ("The tools", "are", "on the bench", "The tools are on the bench."),
                       ("The meeting", "ended", "at noon", "The meeting ended at noon.")])
              + h4("How to test for SVA")
              + eg("Remove the adverbial and see what happens", [
                  "\"He lives.\" - incomplete, so the adverbial is necessary → SVA",
                  "\"The pump runs.\" - complete, so <i>smoothly</i> is optional → SV",
                  "\"The tools are on the bench.\" - <i>are</i> needs a place → SVA",
                  "\"The line starts at 7 am.\" - when is part of the meaning → SVA"])
              + h4("Common mistake")
              + p("Calling the adverbial an object. \"He lives in Surat\" has no object; <i>in "
                  "Surat</i> answers <i>where</i>, not <i>what</i>."),
              syllabus_item="2.5"),
         card("5.4 SVC: subject + verb + complement",
              h4("Rule")
              + p("<b>SVC</b> uses a linking verb (<i>be, become, seem, look, feel, smell, taste</i>) "
                  "and a complement that describes the subject. The complement is never an object: it "
                  "refers to the subject, not to something new.")
              + h4("Examples")
              + table(["Subject", "Verb", "Complement", "Sentence"],
                      [("The panel", "is", "hot", "The panel is hot."),
                       ("The fitter", "became", "a supervisor", "The fitter became a supervisor."),
                       ("The bearing", "looks", "worn", "The bearing looks worn."),
                       ("The coolant", "smells", "burnt", "The coolant smells burnt."),
                       ("The drawing", "seems", "incorrect", "The drawing seems incorrect.")])
              + h4("Object or complement?")
              + eg("Swap test: if the two words can be swapped, it is a complement", [
                  "\"The panel is hot.\" → \"Hot is the panel\" still makes sense → complement, SVC.",
                  "\"The fitter replaced the belt.\" → \"The belt replaced the fitter\" does not → "
                  "object, SVO.",
                  "\"He became an engineer.\" → \"An engineer became he\" works → SVC.",
                  "\"He checked the relay.\" → no swap → SVO."])
              + h4("Common mistake")
              + p("\"The motor is run\" (passive) is not SVC; SVC needs a describing complement: "
                  "\"The motor is noisy\"."),
              syllabus_item="2.5"),
         card("5.5 Telling the four apart",
              h4("Four questions")
              + table(["Question", "Answer", "Pattern"],
                      [("Is the sentence complete after the verb?", "yes", "SV"),
                       ("Does <i>what?</i> or <i>whom?</i> give the rest?", "yes", "SVO"),
                       ("Does the rest answer where, when or how?", "yes", "SVA"),
                       ("Does the rest describe the subject, after be / become / seem?", "yes", "SVC")])
              + h4("Worked examples: six sentences, sorted")
              + table(["Sentence", "Pattern", "Why"],
                      [("The compressor started.", "SV", "complete after the verb"),
                       ("The operator closed the valve.", "SVO", "closed <i>what</i>?"),
                       ("The valve is closed.", "SVC", "closed describes the valve"),
                       ("The gauge reads 4 bar.", "SVO", "reads <i>what</i>?"),
                       ("The gauge is on the panel.", "SVA", "<i>where</i>"),
                       ("The gauge looks faulty.", "SVC", "describes the gauge")])
              + h4("Beyond the syllabus")
              + p("Two more patterns appear in longer sentences: <b>SVOO</b> (<i>The store gave the "
                  "fitter a new seal</i>) and <b>SVOC</b> (<i>The inspector found the panel hot</i>). "
                  "The syllabus examines SV, SVO, SVA and SVC.")
              + h4("Common mistake")
              + p("Deciding by the last word instead of the question the rest answers. Always ask "
                  "<i>what?</i> before you call something an object."),
              syllabus_item="2.5"),
     ]},

    {"title": tr("6. Practice Questions with Model Answers"),
     "items": []},
]

EQUATIONS = [
    {"title": tr("Tense forms at a glance"),
     "items": [
         {"terms": tr("Present simple"), "a": tr("V1 / V1+s - he runs")},
         {"terms": tr("Present continuous"), "a": tr("am/is/are + V-ing - he is running")},
         {"terms": tr("Present perfect"), "a": tr("have/has + V3 - he has run")},
         {"terms": tr("Present perfect continuous"), "a": tr("have/has been + V-ing - he has been running")},
         {"terms": tr("Past simple"), "a": tr("V2 - he ran")},
         {"terms": tr("Past continuous"), "a": tr("was/were + V-ing - he was running")},
         {"terms": tr("Past perfect"), "a": tr("had + V3 - he had run")},
         {"terms": tr("Future simple"), "a": tr("will + V1 - he will run")},
     ]},
    {"title": tr("Sentence patterns"),
     "items": [
         {"terms": tr("SV"), "a": tr("The motor failed.")},
         {"terms": tr("SVO"), "a": tr("The fitter replaced the belt.")},
         {"terms": tr("SVA"), "a": tr("The pump runs smoothly.")},
         {"terms": tr("SVC"), "a": tr("The panel is hot.")},
     ]},
]

VIVA = [
    {"title": tr("Parts of speech and tenses"),
     "items": [
         {"q": tr("Name the eight parts of speech."),
          "a": tr("Noun, verb, pronoun, adjective, adverb, preposition, conjunction and interjection.")},
         {"q": tr("What is the difference between a common noun and a proper noun? Give an example."),
          "a": tr("A common noun names any member of a class (city, engineer) and takes no capital; a "
                  "proper noun names one particular one (Surat, Ashok) and always takes a capital.")},
         {"q": tr("Give three uncountable nouns used in a workshop."),
          "a": tr("Water, oil and equipment - they have no plural form, so we say \"two pieces of "
                  "equipment\".")},
         {"q": tr("What is the difference between an adjective and an adverb?"),
          "a": tr("An adjective describes a noun (a hot motor); an adverb describes a verb, adjective "
                  "or another adverb (the motor runs smoothly).")},
         {"q": tr("Give the three degrees of comparison of \"good\"."),
          "a": tr("Good, better, best - and never \"more better\".")},
         {"q": tr("State the rule for the present simple with he, she and it."),
          "a": tr("The verb takes -s: he runs, she checks, it leaks.")},
         {"q": tr("When do we use the present perfect?"),
          "a": tr("For a finished action with a present result or an experience with no time "
                  "mentioned: \"I have finished the job, so the line can start.\"")},
         {"q": tr("What is the difference between past simple and past perfect?"),
          "a": tr("Past simple reports one past action (\"the belt broke\"); past perfect reports the "
                  "earlier of two past actions (\"the belt had broken before I arrived\").")},
     ]},
    {"title": tr("Modals, agreement and patterns"),
     "items": [
         {"q": tr("List the modal auxiliaries in your syllabus."),
          "a": tr("Can, could, may, might, must, shall, will, should, would, ought to and need.")},
         {"q": tr("What is the difference between must not and need not?"),
          "a": tr("Must not is prohibition (\"you must not open the panel live\"); need not means no "
                  "obligation (\"you need not come tomorrow\").")},
         {"q": tr("Give one sentence each with can, could and may."),
          "a": tr("Ability: \"I can weld aluminium.\" Polite request: \"Could you send the drawing?\" "
                  "Formal permission: \"May I enter the shop floor?\"")},
         {"q": tr("State two rules of subject-verb agreement with examples."),
          "a": tr("A singular subject takes a singular verb (the motor runs) and a plural subject a "
                  "plural verb (the motors run); and two subjects joined by and take a plural verb "
                  "(the motor and the pump are new).")},
         {"q": tr("Which verb agrees with \"one of the pumps\"?"),
          "a": tr("A singular verb, because the subject is one: \"one of the pumps is leaking\".")},
         {"q": tr("Name the four basic sentence patterns with one example each."),
          "a": tr("SV - the motor failed; SVO - the fitter replaced the belt; SVA - the pump runs "
                  "smoothly; SVC - the panel is hot.")},
         {"q": tr("How do you tell an object from a complement?"),
          "a": tr("An object answers what or whom and is a different thing from the subject; a "
                  "complement describes the subject and can be swapped with it in meaning - \"the "
                  "panel is hot\" / \"hot is the panel\".")},
         {"q": tr("What is a transitive verb?"),
          "a": tr("A verb that needs an object to complete its meaning, such as replace, check or "
                  "measure: \"replace the belt\".")},
     ]},
]

_PRACTICE = [
    ("Name the parts of speech of the underlined words: The (a) fitter quickly (b) replaced the "
     "brass (c) valve and (d) smiled.", 4,
     [p("(a) <b>fitter</b> - noun (common noun, doeser of the action)."),
      p("(b) <b>quickly</b> - adverb of manner, describing <i>replaced</i>."),
      p("(c) <b>brass</b> - adjective (material adjective describing <i>valve</i>; it can also be a "
        "noun). (d) <b>and</b> - conjunction, joining two verb phrases."),
      p("The sentence uses four classes in nine words; label a word by the work it does in that "
        "sentence, not by a fixed label.")]),
    ("Rewrite these sentences with the correct present simple form: (a) The pump run daily. "
     "(b) He do not check the oil. (c) Does they test the relay?", 3,
     [p("(a) The pump <b>runs</b> daily. - the subject is singular, so the verb takes -s."),
      p("(b) He <b>does not check</b> the oil. - with he, she, it use <i>does</i>, and the main verb "
        "stays in V1."),
      p("(c) <b>Do</b> they <b>test</b> the relay? - with they use <i>do</i>, and again the main verb "
        "stays in V1.")]),
    ("Fill in the correct tense: (a) The line ___ (stop) at 10:15 am yesterday. (b) I ___ (check) "
     "the panel when the alarm rang. (c) She ___ (work) here since 2022. (d) We ___ (finish) the job, "
     "so the line can start.", 4,
     [p("(a) <b>stopped</b> - past simple, because <i>yesterday</i> is a finished time."),
      p("(b) <b>was checking</b> - past continuous, an action in progress when a shorter action "
        "happened."),
      p("(c) <b>has been working</b> - present perfect continuous with <i>since</i>, for an action "
        "that began in the past and is still going on; <b>has worked</b> is also accepted."),
      p("(d) <b>have finished</b> - present perfect, because the result matters now: the line can "
        "start.")]),
    ("Correct these sentences: (a) I have seen him yesterday. (b) He did not checked the torque. "
     "(c) They are knowing the answer.", 3,
     [p("(a) I <b>saw</b> him yesterday. - <i>yesterday</i> is a finished time, so the past simple "
        "is used, not the present perfect."),
      p("(b) He did not <b>check</b> the torque. - after <i>did not</i> the verb stays in V1."),
      p("(c) They <b>know</b> the answer. - <i>know</i> is a stative verb, so it takes the simple "
        "present, not the continuous.")]),
    ("Use the correct modal: (a) ___ you please send the drawing? (polite request) (b) You ___ wear "
     "goggles in the shop. (strong obligation) (c) You ___ come tomorrow; the job is done. (no "
     "obligation) (d) The relay ___ be faulty, but I am not sure. (weak possibility)", 4,
     [p("(a) <b>Could</b> you please send the drawing? - <i>could</i> is the modal used for a polite request."),
      p("(b) You <b>must</b> wear goggles in the shop. - must marks a rule and a strong obligation."),
      p("(c) You <b>need not</b> come tomorrow. - need not means there is no obligation; must not "
        "would mean prohibition, which is a different instruction."),
      p("(d) The relay <b>might</b> be faulty. - might expresses a weaker possibility than may.")]),
    ("Explain the difference between must not and need not with one example each.", 3,
     [p("<b>Must not</b> forbids an action: \"You must not open the panel while the supply is on.\" "
        "It is a rule with a safety reason."),
      p("<b>Need not</b> removes an obligation: \"You need not open the panel for a visual check.\" "
        "The action is allowed, simply not necessary."),
      p("The two are opposites in practice: one stops you, the other lets you off.")]),
    ("Correct the subject-verb agreement: (a) The box of bolts are heavy. (b) One of the pumps are "
     "leaking. (c) Neither the seal nor the gland were damaged. (d) The news are bad.", 4,
     [p("(a) The box of bolts <b>is</b> heavy. - the subject is <i>box</i>; <i>of bolts</i> only "
        "describes it."),
      p("(b) One of the pumps <b>is</b> leaking. - the subject is <i>one</i>, not <i>pumps</i>."),
      p("(c) Neither the seal nor the gland <b>was</b> damaged. - with neither ... nor the verb "
        "agrees with the nearer subject, which is singular here."),
      p("(d) The news <b>is</b> bad. - <i>news</i> ends in -s but is singular.")]),
    ("Give two rules of subject-verb agreement with one example each.", 3,
     [p("A singular subject takes a singular verb and a plural subject a plural verb: \"The motor "
        "runs\" and \"The motors run\"."),
      p("Words placed between the subject and the verb do not change the verb: \"The list of items "
        "<b>is</b> ready\", where the subject is <i>list</i>."),
      p("Two subjects joined by <i>and</i> take a plural verb: \"The motor and the pump <b>are</b> "
        "new\", while <i>along with</i> and <i>as well as</i> do not: \"The supervisor, along with "
        "two fitters, <b>was</b> present\".")]),
    ("Identify the pattern of each sentence: (a) The compressor started. (b) The operator closed the "
     "valve. (c) The valve is closed. (d) The gauge is on the panel.", 4,
     [p("(a) <b>SV</b> - the sentence is complete after the intransitive verb <i>started</i>."),
      p("(b) <b>SVO</b> - <i>closed</i> what? the valve; the object is a different thing from the "
        "subject."),
      p("(c) <b>SVC</b> - <i>closed</i> describes the valve, and the two can be swapped in meaning, "
        "so it is a complement."),
      p("(d) <b>SVA</b> - <i>on the panel</i> answers where, and without it <i>the gauge is</i> is "
        "incomplete.")]),
    ("Write one sentence for each pattern SV, SVO, SVA and SVC about a workshop.", 4,
     [p("<b>SV:</b> The drill stopped. - the sentence is complete after the intransitive verb, so "
        "nothing else is needed."),
      p("<b>SVO:</b> The apprentice cleaned the filter. - <i>cleaned</i> what? the filter, which is "
        "the object."),
      p("<b>SVA:</b> The compressor is in the corner. - <i>in the corner</i> answers where, and it "
        "cannot be left out."),
      p("<b>SVC:</b> The bearing feels rough. - <i>rough</i> describes the bearing after the linking "
        "verb <i>feels</i>, so it is a complement. Keep each sentence short in the exam, then name "
        "the pattern from the question that the rest of the sentence answers.")]),
    ("Change these into the tense asked for: (a) He checks the oil. (past continuous) (b) They "
     "replaced the belt. (present perfect) (c) The line stops at 10. (past simple) (d) I write the "
     "report. (future simple)", 4,
     [p("(a) He <b>was checking</b> the oil."),
      p("(b) They <b>have replaced</b> the belt."),
      p("(c) The line <b>stopped</b> at 10."),
      p("(d) I <b>will write</b> the report. Notice that only the auxiliary and the tense-carrying "
        "verb form change; the subject, the object and the rest of the sentence stay exactly as they "
        "are."),
      p("Check every answer the same way: name the tense of the original, name the tense asked for, "
        "then change only what that tense needs.")]),
    ("Explain the difference between the present perfect and the past simple, with one example "
     "each.", 3,
     [p("The <b>past simple</b> reports a finished action at a finished time: \"We replaced the belt "
        "yesterday.\" The time is named or understood."),
      p("The <b>present perfect</b> reports a finished action whose result matters now, with no time "
        "named: \"We have replaced the belt, so the line can start.\""),
      p("So \"I have seen him yesterday\" is wrong - the moment you name <i>yesterday</i>, the past "
        "simple is needed.")]),
    ("Correct these sentences and name the error: (a) He works good. (b) Myself Raj. (c) Discuss "
     "about the problem. (d) Although it was hot, but we finished.", 4,
     [p("(a) He works <b>well</b>. - an adverb is needed, not the adjective <i>good</i>."),
      p("(b) <b>I am</b> Raj. - <i>myself</i> is reflexive and cannot replace the subject pronoun."),
      p("(c) <b>Discuss</b> the problem. - <i>discuss</i> is transitive and takes no preposition."),
      p("(d) <b>Although</b> it was hot, we finished. - one conjunction per link; <i>although</i> "
        "and <i>but</i> together is a double conjunction.")]),
    ("Give one example each of a preposition of place, time and agent.", 3,
     [p("Place: \"The tools are <b>on</b> the bench.\""),
      p("Time: \"The line starts <b>at</b> 7 am.\""),
      p("Agent: \"The joint was welded <b>by</b> Ashok.\" The agent preposition names who did the "
        "action, which is why passive sentences use <i>by</i>."),
      p("Keep the three questions separate in the exam: <i>where</i> gives a preposition of place, "
        "<i>when</i> a preposition of time, and <i>by whom</i> the agent.")]),
    ("Join each pair with a suitable conjunction: (a) The belt was loose. The line vibrated. (b) The "
     "load was high. The motor stayed cool.", 3,
     [p("(a) <b>Because</b> the belt was loose, the line vibrated. - subordinating conjunction for "
        "cause."),
      p("(b) <b>Although</b> the load was high, the motor stayed cool. - subordinating conjunction "
        "for contrast."),
      p("(a) can also be joined with <i>so</i> in the other order: \"The belt was loose, so the line "
        "vibrated.\" Both are correct; the choice changes which half is the main clause.")]),
]

EXAM = [{"q": tr(q), "marks": m} for q, m, _parts in _PRACTICE]
PRACTICE_ANSWERS = [tr("".join(parts)) for _q, _m, parts in _PRACTICE]

LESSON_COUNT = sum(len(s["items"]) for s in NOTES)
