"""DI01000031 Communication Skills in English - Unit 1: Theory of Communication.

GTU 1.1-1.5, 6 h, 20 %, 14 marks, CO1: effective communication, the S+E+C+D+R+N+F model, upward and
downward levels, the types of communication, and the barriers that block it.

Author's policy for this subject: every rule is one line and is followed by examples, so a reader
can copy the pattern rather than memorise prose.
"""
from subject_DI01000031 import tr as _tr


class Txt(dict):
    """An English-only text node that can be concatenated with a plain string."""

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
    """A block of examples - the main teaching device in this subject."""
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
    ("British Council LearnEnglish - speaking, listening and writing skills",
     "https://learnenglish.britishcouncil.org/skills"),
    ("Cambridge Dictionary - definitions and usage examples",
     "https://dictionary.cambridge.org/dictionary/english/"),
    ("Kulbhushan Kumar - Effective Communication Skills (Khanna Publishing House, 2018)",
     "https://www.khannapublishers.in/"),
    ("MindTools - the communication process and the seven Cs",
     "https://www.mindtools.com/"),
]

NOTES = [
    {"title": tr("1. Communication and the Four Skills"),
     "items": [
         card("1.1 What communication means",
              h4("Definition")
              + p("<b>Communication is the exchange of ideas, information or feelings between two or "
                  "more people so that the receiver understands what the sender meant.</b>")
              + p("The key words are <i>exchange</i> (it goes both ways) and <i>understands</i> (the "
                  "message has to arrive, not just leave).")
              + h4("One idea, many forms")
              + table(["Situation", "What is sent", "How it travels"],
                      [("Supervisor tells a fitter to check the bearing", "an instruction", "spoken words"),
                       ("A notice on the workshop board", "a safety rule", "written words"),
                       ("A red lamp on a machine panel", "a warning", "a visual signal"),
                       ("A thumbs-up after a job is checked", "approval", "a gesture")])
              + h4("Why a diploma engineer needs it")
              + p("On site you will give instructions, read drawings, write reports, explain a fault "
                  "and speak to a customer. Each of those is communication, and each can go wrong.")
              + h4("Examples of everyday messages")
              + eg("Short messages you already send", [
                  "\"Bring the 12 mm spanner.\" - instruction",
                  "\"The motor is hot, stop the line.\" - warning",
                  "\"Job finished at 4 pm.\" - information",
                  "\"Well done, the alignment is perfect.\" - appreciation"])
              + h4("Common mistake")
              + p("Treating communication as 'sending'. If the receiver did not understand, the "
                  "message did not happen."),
              syllabus_item="1.1"),
         card("1.2 The four language skills: LSRW",
              h4("The four skills")
              + table(["Skill", "What you do", "Example from a workshop"],
                      [("Listening", "receive and interpret speech",
                        "following a briefing before a shutdown"),
                       ("Speaking", "produce speech",
                        "explaining a fault to the supervisor on the phone"),
                       ("Reading", "interpret written text",
                        "reading the maintenance manual and the drawing"),
                       ("Writing", "produce written text",
                        "writing the job card entry and an e-mail to the vendor")])
              + h4("Receptive and productive")
              + p("Listening and reading are <b>receptive</b> (you take in); speaking and writing are "
                  "<b>productive</b> (you put out). A balanced course practises all four.")
              + h4("Examples of each skill in one day")
              + eg("A technician's day", [
                  "7:30 - listens to the shift handover (listening)",
                  "9:00 - reads the wiring diagram before opening the panel (reading)",
                  "11:00 - tells the helper which tools to bring (speaking)",
                  "4:30 - writes the breakdown entry in the log book (writing)"])
              + h4("Common mistake")
              + p("Calling listening 'hearing'. Hearing is passive; listening is active and takes "
                  "attention."),
              syllabus_item="1.1"),
         card("1.3 Listening is the skill that is used most",
              h4("Hearing and listening are different")
              + p("<b>Hearing</b> is the ear receiving sound. <b>Listening</b> is paying attention, "
                  "understanding and remembering.")
              + h4("Examples that show the difference")
              + eg("Same sound, different result", [
                  "You hear the machine alarm but keep working - hearing only.",
                  "You hear the alarm, stop, and check the coolant level - listening.",
                  "You hear a customer say 'make it fast' and you speed up the wrong job - poor "
                  "listening.",
                  "You repeat back 'so the 40 mm shaft is urgent, the rest later?' - active listening."])
              + h4("Three habits of a good listener")
              + ol("Face the speaker and keep eye contact.",
                   "Do not plan your reply while the other person is still talking.",
                   "Repeat the key point back in your own words.")
              + h4("Common mistake")
              + p("Nodding while thinking about something else. The nod is not evidence of "
                  "understanding."),
              syllabus_item="1.1"),
         card("1.4 Communication skills at work",
              h4("What employers notice first")
              + p("Technical knowledge gets you the interview; clear communication keeps you on the "
                  "team. The four skills appear in every job advertisement as 'good communication "
                  "skills'.")
              + h4("Examples by situation")
              + table(["Situation", "Skill needed", "A good version"],
                      [("Client asks why the pump failed", "speaking + explaining",
                        "\"The seal dried out during the shutdown; we have replaced it and run the pump for an hour.\""),
                       ("Writing a daily report", "writing",
                        "\"Line 2 stopped 10:15-11:00 due to belt slip. Belt replaced, alignment checked.\""),
                       ("Handover to the next shift", "speaking + listening",
                        "\"Panel 3 is on manual; do not reset until the vendor calls.\""),
                       ("Reading a vendor's mail", "reading",
                        "noticing that the delivery date changed from 5th to 12th")])
              + h4("One example of a costly misunderstanding")
              + p("\"Grease the bearing weekly\" is read as \"grease the motor weekly\". The bearing "
                  "seizes, the motor survives. Twelve words, one breakdown.")
              + h4("Common mistake")
              + p("Believing grammar alone is communication skill. Accuracy helps, but clarity and "
                  "courtesy carry the message."),
              syllabus_item="1.1"),
         card("1.5 What communication skill is not",
              h4("Three wrong ideas")
              + ul("<b>\"It means big words.\"</b> No - \"Please send the drawing\" works better than "
                   "\"Kindly expedite the despatch of the requisite drawing.\"",
                   "<b>\"It is only speaking.\"</b> No - a badly written e-mail can cost a contract "
                   "before anyone speaks.",
                   "<b>\"It is fixed at birth.\"</b> No - it is a skill, so it improves with "
                   "practice and feedback.")
              + h4("Simple words, complete message")
              + table(["Wordy", "Clear"],
                      [("at this point in time", "now"),
                       ("in the event that", "if"),
                       ("utilise", "use"),
                       ("please revert", "please reply")])
              + h4("Examples of the same message at three levels")
              + eg("Asking for a report", [
                  "Too blunt: \"Send report.\"",
                  "Too heavy: \"You are hereby requested to furnish the said report at the earliest.\"",
                  "Right: \"Please send the line-2 report by Friday 5 pm.\""])
              + h4("Common mistake")
              + p("Adding length to sound professional. Length hides the request; short sentences "
                  "deliver it."),
              syllabus_item="1.1"),
     ]},

    {"title": tr("2. Effective Communication and the Seven Cs"),
     "items": [
         card("2.1 What makes communication effective",
              h4("The test")
              + p("Communication is <b>effective</b> when the receiver's understanding matches the "
                  "sender's intention, and the reply or action shows it.")
              + h4("Four conditions")
              + ul("A clear purpose - what should the reader or listener do next?",
                   "A suitable channel - a phone call for an urgent stop, an e-mail for a record.",
                   "Simple, correct language.",
                   "Feedback - a reply, a nod, a completed job, a signature.")
              + h4("Examples: effective and ineffective")
              + table(["Message", "Verdict", "Why"],
                      [("\"Stop the conveyor, the guard is loose.\"", "effective",
                        "one action, one reason, no doubt"),
                       ("\"Something seems wrong with the machine, maybe check it.\"", "vague",
                        "no action, no machine named"),
                       ("\"Meeting shifted to 3 pm, Room 4.\"", "effective", "two facts, no padding"),
                       ("\"As per discussion, needful will be done.\"", "useless",
                        "no one knows what will be done")])
              + h4("Common mistake")
              + p("Judging your own message by how much effort you put in. Judge it by what the "
                  "receiver does next."),
              syllabus_item="1.1"),
         card("2.2 The seven Cs",
              h4("The checklist")
              + p("A good message is <b>clear, concise, concrete, correct, coherent, complete and "
                  "courteous</b>. Seven words, ten seconds, most misunderstandings prevented.")
              + h4("One example for each C")
              + table(["C", "Weak", "Better"],
                      [("Clear", "\"Do the needful.\"", "\"Replace the gasket and refit the cover.\""),
                       ("Concise", "\"At this point of time we are not in a position to...\"",
                        "\"We cannot supply before Monday.\""),
                       ("Concrete", "\"The motor is faulty.\"",
                        "\"The motor draws 9 A against a rated 6 A.\""),
                       ("Correct", "\"The bolts is loose.\"", "\"The bolts are loose.\""),
                       ("Coherent", "\"Belt replaced. Also the pump. Yesterday.\"",
                        "\"Yesterday we replaced the pump, then the belt.\""),
                       ("Complete", "\"Meeting on Monday.\"",
                        "\"Meeting on Monday 10 am, Room 4, agenda: line-2 downtime.\""),
                       ("Courteous", "\"Send it now.\"",
                        "\"Please send it by 4 pm so we can finish today.\"")])
              + h4("Common mistake")
              + p("Chasing courtesy and forgetting completeness - a polite message without the date "
                  "or the part number still stops the work."),
              "c5_seven", syllabus_item="1.1"),
         card("2.3 Rewriting a weak message",
              h4("Method")
              + ol("Name the purpose - what must the reader do?",
                   "Write one sentence for that action.",
                   "Add only the facts needed: what, where, when, how much.",
                   "Close with a courteous request or a thank-you.")
              + h4("Worked example: the same message, rewritten")
              + p("<b>Before:</b> \"Respected sir, as per telephonic conversation with your good "
                  "self, the material which was supposed to come has not come, so kindly do the "
                  "needful at the earliest and oblige.\"")
              + p("<b>After:</b> \"Sir, the 12 mm MS plates promised on 5 March have not arrived. "
                  "Please confirm dispatch today, as the job is stopped.\"")
              + h4("What changed")
              + ul("One paragraph of padding became two short sentences.",
                   "The vague 'material' became '12 mm MS plates'.",
                   "The date and the consequence (job stopped) were added.",
                   "The request is specific: confirm dispatch today.")
              + h4("Common mistake")
              + p("Rewriting only the grammar. The weakness is usually missing facts, not missing "
                  "politeness."),
              syllabus_item="1.1"),
     ]},

    {"title": tr("3. The Communication Model"),
     "items": [
         card("3.1 The seven parts, in order",
              h4("The model")
              + p("<b>S + E + C + D + R + N + F</b>: Sender, Encoding, Channel, Decoding, Receiver, "
                  "Noise, Feedback.")
              + table(["Part", "Meaning", "Example"],
                      [("Sender", "the person with the idea", "the supervisor"),
                       ("Encoding", "turning the idea into words or signs", "choosing the sentence"),
                       ("Channel", "the route the message travels", "a phone call"),
                       ("Decoding", "the receiver interprets it", "the fitter understands"),
                       ("Receiver", "the person the message is for", "the fitter"),
                       ("Noise", "anything that disturbs the message", "machine noise on the line"),
                       ("Feedback", "the reply that closes the loop",
                        "\"Bearing checked, no play.\"")])
              + h4("Read the model as a loop")
              + p("Feedback puts the receiver back in the sender's place, so the loop closes and the "
                  "next message starts from a shared understanding.")
              + h4("Common mistake")
              + p("Learning the seven words without an example each. In an exam, one example per part "
                  "is what earns the marks."),
              "c1_cycle", syllabus_item="1.2"),
         card("3.2 Encoding and decoding",
              h4("What encoding means")
              + p("<b>Encoding</b> is choosing the symbols - words, numbers, gestures, drawings - that "
                  "will carry the idea. <b>Decoding</b> is the receiver turning those symbols back "
                  "into meaning.")
              + h4("Examples of encoding choices")
              + eg("The same idea, encoded three ways", [
                  "\"Torque to 45 N·m\" - words and a number for a technician.",
                  "A torque wrench with a dial set at 45 - a visual and physical code.",
                  "A drawing with the symbol for 'tighten to 45 N·m' - a standard engineering code."])
              + h4("When decoding fails")
              + table(["Sent", "Understood", "Why"],
                      [("\"Check the bearing clearance.\"", "cleaned the bearing",
                        "similar sound, careless listening"),
                       ("\"Use the 6 mm bit.\"", "used the 6 inch bit", "unit dropped in speech"),
                       ("\"Cut it 2 m long.\"", "cut it 2 feet long", "mixed units")])
              + h4("Common mistake")
              + p("Assuming the other person uses your code. Units, abbreviations and slang differ "
                  "between trades and regions."),
              syllabus_item="1.2"),
         card("3.3 Choosing the channel",
              h4("Channel choice is part of the message")
              + p("The channel decides how fast the message travels, how much detail survives, and "
                  "whether there is a record.")
              + table(["Channel", "Best for", "Example"],
                      [("Face to face", "instruction, correction, bad news",
                        "explaining a job to a new helper"),
                       ("Phone call", "urgent, short, needs an answer now",
                        "\"Stop the line, the guard is loose.\""),
                       ("E-mail", "record, detail, attachment",
                        "sending a drawing revision to a vendor"),
                       ("Notice board", "everyone at once, rules",
                        "the new safety helmet rule"),
                       ("Drawing or chart", "shapes, positions, quantities",
                        "the panel layout before wiring"),
                       ("WhatsApp group", "quick coordination on site",
                        "\"Material reached gate 2.\"")])
              + h4("One message, wrong channel")
              + p("A 40-line specification sent as a voice note: it will be misheard and lost. The same "
                  "text as an e-mail with a table is used for years.")
              + h4("Common mistake")
              + p("Using the fastest channel for a message that needs a record, or the most formal "
                  "channel for a question that needs an answer in one minute."),
              syllabus_item="1.2"),
         card("3.4 Noise and feedback in practice",
              h4("Noise")
              + p("<b>Noise</b> is anything that reduces the fidelity of the message. It is not only "
                  "sound.")
              + h4("Examples of noise")
              + table(["Type of noise", "Example"],
                      [("Physical", "compressor running beside the phone"),
                       ("Technical", "a weak signal cutting half a sentence"),
                       ("Semantic", "jargon the receiver does not know"),
                       ("Psychological", "the receiver is worried about a breakdown"),
                       ("Organisational", "the message passes through four people before it arrives")])
              + h4("Feedback")
              + p("Feedback can be verbal (\"understood, 45 N·m\"), written (a signed job card), or "
                  "non-verbal (a nod, a completed task).")
              + h4("Examples of feedback that actually checks understanding")
              + eg("Better than \"ok\"", [
                  "\"So the pump runs for one hour, then we check the seal - right?\"",
                  "\"I will send the drawing by 4 pm and call you after the test.\"",
                  "A job card signed by the supervisor after the work is inspected."])
              + h4("Common mistake")
              + p("Accepting silence as agreement. Silence is the absence of feedback, not proof of "
                  "understanding."),
              syllabus_item="1.2"),
     ]},

    {"title": tr("4. Levels of Communication"),
     "items": [
         card("4.1 Downward communication",
              h4("Definition")
              + p("<b>Downward communication</b> flows from a higher level to a lower level: "
                  "management to supervisors to workers. Its purpose is to direct, inform and "
                  "explain.")
              + h4("What travels down")
              + eg("Examples", [
                  "An order: \"Run line 2 this afternoon.\"",
                  "A circular: \"Safety helmets compulsory from Monday.\"",
                  "A policy: \"Overtime needs written approval.\"",
                  "A job instruction with a drawing.",
                  "Feedback on performance: \"Your rejection rate has dropped to 0.5 %.\""])
              + h4("Strengths and risks")
              + p("It is fast and carries authority. The risk is dilution - each level trims or "
                  "rewords, and the last person hears a different message.")
              + h4("Example of dilution")
              + p("Management: \"Reduce material wastage by 10 % this quarter.\" Third level: "
                  "\"Don't waste material.\" The number has gone, so no one knows what to do.")
              + h4("Common mistake")
              + p("Sending a downward message once, in one channel, and assuming it has been "
                  "received."),
              "c3_levels", syllabus_item="1.3"),
         card("4.2 Upward communication",
              h4("Definition")
              + p("<b>Upward communication</b> flows from a lower level to a higher level: workers to "
                  "supervisors to management. Its purpose is to report, suggest and warn.")
              + h4("What travels up")
              + eg("Examples", [
                  "A report: \"Line 2 was down 45 minutes; belt replaced.\"",
                  "A suggestion: \"A roller stand here would save two men.\"",
                  "A grievance: \"The night shift has no drinking water.\"",
                  "A warning: \"Stock of 6205 bearings will finish by Thursday.\"",
                  "A clarification question: \"Do we hold the batch until the test report arrives?\""])
              + h4("Why organisations need it")
              + p("The people closest to the machine know the problems first. If upward flow is weak, "
                  "management plans with old information.")
              + h4("Example of a blocked upward message")
              + p("A fitter notices a crack but says nothing because \"nobody listens\". Three weeks "
                  "later the coupling fails. The information existed; the channel did not.")
              + h4("Common mistake")
              + p("Reporting only good news. Upward communication is most valuable when it carries "
                  "bad news early."),
              syllabus_item="1.3"),
         card("4.3 Difference between the two levels",
              h4("Side by side")
              + table(["Point", "Downward", "Upward"],
                      [("Direction", "top to bottom", "bottom to top"),
                       ("Purpose", "order, inform, explain", "report, suggest, warn"),
                       ("Typical form", "circular, instruction, appraisal",
                        "report, grievance, suggestion box"),
                       ("Tone", "directive", "respectful, factual"),
                       ("Risk", "dilution and distortion", "filtering and fear"),
                       ("Example", "\"Helmets compulsory from Monday.\"",
                        "\"Two helmets are missing in our section.\"")])
              + h4("Both directions carry the same message")
              + p("A policy goes down, and the confirmation comes back up. Without the return path, "
                  "the sender never learns whether the policy arrived.")
              + h4("Common mistake")
              + p("Calling every internal message 'downward'. Ask who writes to whom; the direction "
                  "follows from that."),
              syllabus_item="1.3"),
         card("4.4 Improving flow in both directions",
              h4("Fixes that work")
              + ul("Shorten the chain: fewer levels between the decision and the machine.",
                   "Use one channel per message, and confirm receipt.",
                   "Hold a two-minute shift handover in person.",
                   "Keep a suggestion register with visible responses.",
                   "Answer grievances within a stated time.")
              + h4("Examples of a fix in action")
              + table(["Problem", "Fix", "Result"],
                      [("Instructions reach the shop floor changed",
                        "a one-page job card with the drawing", "same message at every level"),
                       ("Workers never hear back on suggestions",
                        "a weekly note listing accepted ideas", "upward flow increases"),
                       ("Supervisors are flooded with e-mails",
                        "one daily digest at 9 am", "important messages are read")])
              + h4("Common mistake")
              + p("Adding another level to 'improve control'. Every extra level is another place "
                  "where the message can change."),
              syllabus_item="1.3"),
     ]},

    {"title": tr("5. Types of Communication"),
     "items": [
         card("5.1 Verbal communication: oral and written",
              h4("Definition")
              + p("<b>Verbal communication uses words</b>, spoken or written. It is the type you use "
                  "most, and the one that carries the detail.")
              + h4("Oral and written compared")
              + table(["Point", "Oral", "Written"],
                      [("Speed", "instant, with tone", "slower to produce"),
                       ("Record", "none unless recorded", "permanent and traceable"),
                       ("Feedback", "immediate", "delayed"),
                       ("Best for", "quick decisions, corrections, discussion",
                        "specifications, orders, reports, contracts"),
                       ("Example", "\"Hold the job, I am coming.\"",
                        "\"Job No. 118 is on hold pending inspection.\"")])
              + h4("Examples in a workshop")
              + eg("Ten seconds of verbal communication", [
                  "Spoken instruction: \"Tighten the gland nut, not the body.\"",
                  "Written record: \"Gland nut tightened, no leak after 30 minutes.\"",
                  "Spoken warning: \"Stand clear, starting the motor.\"",
                  "Written rule: \"Never open the panel without isolation.\""])
              + h4("Common mistake")
              + p("Leaving an important instruction only in speech. If it must be remembered, write "
                  "it."),
              "c2_types", syllabus_item="1.4"),
         card("5.2 Non-verbal communication",
              h4("Definition")
              + p("<b>Non-verbal communication</b> passes meaning without words - through the body, "
                  "the voice and the use of space.")
              + h4("Five channels with examples")
              + table(["Channel", "Meaning", "Example"],
                      [("Kinesics (body movement)", "gesture, posture",
                        "a thumbs-up after inspection; folded arms during a discussion"),
                       ("Proxemics (space)", "distance and territory",
                        "standing close to a machine to point at a fault"),
                       ("Paralanguage", "tone, pitch, speed, pause",
                        "\"Fine.\" said flatly means the opposite"),
                       ("Haptics (touch)", "physical contact",
                        "a hand on the shoulder in encouragement"),
                       ("Chronemics (time)", "punctuality as a message",
                        "arriving late for a handover signals little respect for it")])
              + h4("Why it matters")
              + p("In face-to-face talk, the body carries a large share of the meaning. A supervisor "
                  "who says \"take your time\" while looking at the clock is not believed.")
              + h4("Common mistake")
              + p("Reading one gesture as a fixed truth. Arms folded may mean cold, not angry - look "
                  "at the whole situation."),
              syllabus_item="1.4"),
         card("5.3 Visual communication",
              h4("Definition")
              + p("<b>Visual communication</b> uses images: drawings, charts, graphs, maps, signs, "
                  "icons and colour codes.")
              + h4("Examples you already meet")
              + table(["Visual", "What it replaces"],
                      [("A wiring diagram", "a page of text about connections"),
                       ("A bar chart of monthly breakdowns", "a table of figures"),
                       ("A red sign with a crossed circle", "\"Do not enter\""),
                       ("A Gantt chart", "paragraphs about the schedule"),
                       ("A floor plan with escape routes", "a written evacuation description")])
              + h4("Why engineers rely on it")
              + p("A drawing shows shape, position and size at once, in a way no sentence can. "
                  "Standards (IS, ISO) exist so the same symbol means the same thing everywhere.")
              + h4("Examples of visual communication going wrong")
              + eg("When a picture misleads", [
                  "A chart with a cut y-axis makes a 2 % rise look like a doubling.",
                  "A sign in a language the visitor cannot read.",
                  "A drawing without a revision number - two versions in use at once."])
              + h4("Common mistake")
              + p("Assuming a picture is automatically clear. Every visual needs a caption, a scale "
                  "and a date."),
              syllabus_item="1.4"),
         card("5.4 Interpersonal communication",
              h4("Definition")
              + p("<b>Interpersonal communication</b> is communication between two people, or within "
                  "a small group, where each can see and answer the other.")
              + h4("Features")
              + ul("Two-way and immediate.",
                   "Carries feeling as well as information.",
                   "Depends on listening, tone and body language.")
              + h4("Examples")
              + eg("Interpersonal moments at work", [
                  "Explaining a mistake to a helper without humiliating him.",
                  "A five-minute conversation with a supplier on the phone.",
                  "A supervisor and an apprentice agreeing on the order of jobs.",
                  "Apologising to a customer for a late delivery."])
              + h4("Why the tone matters")
              + p("\"You did it wrong\" closes the conversation; \"Let us see why the bore is "
                  "oversize\" keeps it open and solves the problem.")
              + h4("Common mistake")
              + p("Sending an interpersonal message by e-mail. Criticism, apology and encouragement "
                  "work better face to face."),
              syllabus_item="1.5"),
         card("5.5 Intrapersonal, extra personal and mass communication",
              h4("Intrapersonal")
              + p("<b>Intrapersonal communication</b> is communication with yourself - thinking, "
                  "self-talk, planning, rehearsing.")
              + eg("Examples", ["\"Check the torque twice today.\"",
                                "Rehearsing a sentence before a phone call.",
                                "Writing a to-do list and reading it back."])
              + h4("Extra personal")
              + p("<b>Extra personal communication</b> is between a human being and a non-human: an "
                  "animal, a machine, or a system that answers.")
              + eg("Examples", ["Telling a dog to sit.",
                                "Talking to a machine that will not start.",
                                "Reading a sensor's beep as a message and answering by pressing stop."])
              + h4("Mass")
              + p("<b>Mass communication</b> reaches a large, unknown audience at once through a "
                  "medium: newspaper, radio, television, website, social media.")
              + eg("Examples", ["A plant's safety week campaign on the notice boards and the website.",
                                "A government advisory on the radio.",
                                "A company's recruitment post on LinkedIn."])
              + h4("Common mistake")
              + p("Calling a notice board 'mass communication' when it serves forty workers. Mass "
                  "means a large, scattered, anonymous audience."),
              syllabus_item="1.5"),
         card("5.6 Choosing the type for the situation",
              h4("Method: match the type to the situation")
              + p("Ask three questions - how urgent is it, how much detail must survive, and how "
                  "many people must receive it? The answers pick the type.")
              + table(["Situation", "Type", "Why"],
                      [("Correcting a dangerous habit", "interpersonal, verbal + non-verbal",
                        "needs tone, eye contact and immediate feedback"),
                       ("Announcing a new policy to 300 workers", "mass / downward written",
                        "same words to everyone, with a record"),
                       ("Recording that a bearing was replaced", "written verbal",
                        "traceable later"),
                       ("Showing a crack to a colleague", "visual + verbal",
                        "pointing shows it faster than describing it"),
                       ("Talking yourself through a startup sequence", "intrapersonal",
                        "no second person involved"),
                       ("Congratulating a team", "interpersonal", "feeling must travel with the words")])
              + h4("Rule of thumb")
              + p("Urgent and personal - speak. Detailed and lasting - write. Shape or position - "
                  "draw. Many people, one message - publish.")
              + h4("Worked examples")
              + ul("A guard rail is broken during the shift: speak to the supervisor at once "
                   "(interpersonal, verbal) and log it the same evening (written).",
                   "A crack on a coupling: call the fitter, point at it (visual), then photograph it "
                   "for the report.",
                   "A safety rule for 300 workers: a written circular plus a notice-board display "
                   "(mass, visual).")
              + h4("Common mistake")
              + p("Using one favourite type for everything. A team that writes everything wastes "
                  "time; a team that only speaks keeps no record."),
              syllabus_item="1.5"),
     ]},

    {"title": tr("6. Barriers to Effective Communication"),
     "items": [
         card("6.1 Physical barriers",
              h4("Definition")
              + p("<b>Physical barriers</b> are conditions in the environment or the medium that stop "
                  "the message travelling intact.")
              + h4("Examples")
              + eg("Noise, distance and equipment", [
                  "Two machines running beside a conversation in which a torque figure is given.",
                  "A phone call made from a workshop instead of a quiet corner.",
                  "A weak network dropping the last words of a voice message.",
                  "A guard's whistle lost inside ear protection.",
                  "A handwritten note blurred by rain on a site board."])
              + h4("Cures")
              + ul("Move to a quiet place before giving a number.",
                   "Repeat the key figure and make the listener repeat it.",
                   "Put critical instructions in writing.",
                   "Use the right channel: a drawing for shape, a call for urgency.")
              + h4("Example of the cost")
              + p("\"20 thou\" and \"20 mm\" sound alike through noise. The first is a tolerance, the "
                  "second is scrap.")
              + h4("Common mistake")
              + p("Shouting louder instead of changing the channel. Louder does not remove a language "
                  "or noise problem."),
              syllabus_item="1.6"),
         card("6.2 Language and semantic barriers",
              h4("Definition")
              + p("<b>Language barriers</b> come from the words themselves: jargon, ambiguity, poor "
                  "grammar, different meanings for the same word.")
              + h4("Examples")
              + table(["Language problem", "Example"],
                      [("Jargon", "\"Fix the DOB and reset the VFD.\" to a first-year apprentice"),
                       ("Ambiguity", "\"Send it tomorrow\" - which tomorrow, and what is 'it'?"),
                       ("Wrong word", "\"The pump is not working properly\" instead of \"the pump "
                                      "leaks at the seal\""),
                       ("Grammar", "\"The bolts is loose\" - the reader hesitates"),
                       ("False friend", "British \"chips\" means fried potatoes, American \"chips\" means crisps"
                                        "foods"),
                       ("Abbreviation", "MS means mild steel here and Microsoft in an e-mail elsewhere")])
              + h4("Cures")
              + ul("Define a term the first time you use it.",
                   "Prefer one short word to three long ones.",
                   "Give numbers with units.",
                   "Ask the receiver to state the instruction back.")
              + h4("Worked example")
              + p("\"Do the needful\" is not English that carries meaning. \"Replace the gasket and "
                  "tighten to 20 N·m\" does.")
              + h4("Common mistake")
              + p("Using jargon to look expert. Jargon excludes the person who must act on the "
                  "message."),
              syllabus_item="1.6"),
         card("6.3 Psychological barriers",
              h4("Definition")
              + p("<b>Psychological barriers</b> sit inside the people: fear, prejudice, stress, "
                  "inattention, mistrust, or a fixed idea.")
              + h4("Examples")
              + eg("Inside the sender and the receiver", [
                  "A helper does not report a mistake because he fears the supervisor's anger.",
                  "A supervisor stops listening to an operator he has decided is careless.",
                  "A technician is so anxious about a breakdown that he hears only the first "
                  "sentence.",
                  "A manager's \"suggestion\" is received as a criticism.",
                  "Everyone agrees in the meeting, and nothing changes afterwards."])
              + h4("Cures")
              + ul("Separate the person from the problem: discuss the bore, not the person.",
                   "Ask what the other person understood before replying.",
                   "Keep bad news safe to report - reward early warnings.",
                   "Pause, breathe and finish the sentence before answering.")
              + h4("Example")
              + p("Reporting a crack two days late costs a coupling. Reporting it in the first hour "
                  "costs a chat.")
              + h4("Common mistake")
              + p("Treating fear as a personal weakness. It is a communication barrier, and it is "
                  "removed by behaviour, not by orders."),
              "c4_barriers", syllabus_item="1.6"),
         card("6.4 Cultural and organisational barriers",
              h4("Cultural barriers")
              + p("<b>Cultural barriers</b> arise when customs, values or gestures differ between "
                  "people.")
              + eg("Examples", ["Direct \"no\" is rude in some cultures, so silence is used instead.",
                                "The same hand gesture can be friendly in one region and offensive in "
                                "another.",
                                "Hierarchy: a junior may not correct a senior, even when the senior "
                                "is wrong.",
                                "A festival greeting is expected before business in some regions."])
              + h4("Organisational barriers")
              + p("<b>Organisational barriers</b> come from the structure: too many levels, unclear "
                  "channels, overload, or a culture that does not listen.")
              + eg("Examples", ["Six signatures needed before a spare is ordered.",
                                "Workers are told of a change after the machine has moved.",
                                "Everyone copies everyone, and the important mail is lost.",
                                "A suggestion box that is never opened."])
              + h4("Cures")
              + ul("Flatten the chain and name one owner per message.",
                   "Fix a channel per purpose (safety, quality, stores).",
                   "Set a response time and keep it.",
                   "Train the team in listening, not only in tools.")
              + h4("Summary of the five families")
              + table(["Barrier", "First question to ask"],
                      [("Physical", "Can we hear and see each other?"),
                       ("Language", "Do we use the same words for the same thing?"),
                       ("Psychological", "Is either of us afraid, angry or tired?"),
                       ("Cultural", "Does this gesture mean the same to both of us?"),
                       ("Organisational", "Is there a clear channel and one owner?")])
              + h4("Common mistake")
              + p("Blaming the receiver (\"he does not listen\") without checking the channel, the "
                  "wording and the timing."),
              syllabus_item="1.6"),
     ]},

    {"title": tr("7. Practice Questions with Model Answers"),
     "items": []},  # filled by the builder
]

EQUATIONS = [
    {"title": tr("The model in one line"),
     "items": [
         {"terms": tr("Communication cycle"),
          "a": tr("Sender → Encoding → Channel → Decoding → Receiver, with Noise throughout and "
                  "Feedback closing the loop")},
         {"terms": tr("Effective communication"),
          "a": tr("the receiver's understanding equals the sender's intention")},
         {"terms": tr("Seven Cs"),
          "a": tr("clear, concise, concrete, correct, coherent, complete, courteous")},
         {"terms": tr("Four language skills"),
          "a": tr("listening, speaking, reading, writing (LSRW)")},
     ]},
    {"title": tr("Levels and types"),
     "items": [
         {"terms": tr("Downward"),
          "a": tr("top to bottom: orders, circulars, policy, instructions")},
         {"terms": tr("Upward"),
          "a": tr("bottom to top: reports, suggestions, grievances, warnings")},
         {"terms": tr("Verbal / non-verbal / visual"),
          "a": tr("words / body and voice / images and signs")},
         {"terms": tr("Interpersonal / intrapersonal"),
          "a": tr("between people / with yourself")},
         {"terms": tr("Extra personal / mass"),
          "a": tr("with a non-human / with a large anonymous audience")},
     ]},
    {"title": tr("Barriers"),
     "items": [
         {"terms": tr("Physical"), "a": tr("noise, distance, weak signal, bad handwriting")},
         {"terms": tr("Language"), "a": tr("jargon, ambiguity, wrong word, poor grammar")},
         {"terms": tr("Psychological"), "a": tr("fear, prejudice, stress, inattention")},
         {"terms": tr("Cultural"), "a": tr("customs, gestures, hierarchy")},
         {"terms": tr("Organisational"), "a": tr("too many levels, unclear channel, overload")},
     ]},
]

VIVA = [
    {"title": tr("Definitions"),
     "items": [
         {"q": tr("What is communication?"),
          "a": tr("The exchange of ideas, information or feelings between people so that the "
                  "receiver understands what the sender meant.")},
         {"q": tr("What are the four language skills?"),
          "a": tr("Listening and speaking (oral), reading and writing (written) - LSRW.")},
         {"q": tr("What is the difference between hearing and listening?"),
          "a": tr("Hearing is the ear receiving sound; listening is paying attention, understanding "
                  "and remembering.")},
         {"q": tr("When is communication called effective?"),
          "a": tr("When the receiver's understanding matches the sender's intention and the reply or "
                  "action shows it.")},
         {"q": tr("Name the seven Cs."),
          "a": tr("Clear, concise, concrete, correct, coherent, complete, courteous.")},
         {"q": tr("Give one example of ineffective communication and say why."),
          "a": tr("\"Do the needful\" - it names no action, no object and no time, so the reader "
                  "cannot act on it.")},
     ]},
    {"title": tr("Model, levels and types"),
     "items": [
         {"q": tr("Expand S+E+C+D+R+N+F."),
          "a": tr("Sender, Encoding, Channel, Decoding, Receiver, Noise, Feedback.")},
         {"q": tr("What is encoding? Give an example."),
          "a": tr("Turning an idea into words, numbers or signs - for example saying \"torque to "
                  "45 N·m\" instead of pointing at the bolt.")},
         {"q": tr("What is feedback and why is it important?"),
          "a": tr("The receiver's reply or action; it closes the loop and proves the message "
                  "arrived, for example \"bearing checked, no play\".")},
         {"q": tr("What is noise in communication?"),
          "a": tr("Anything that reduces the fidelity of the message - machine noise, a weak "
                  "signal, jargon, or a distracted receiver.")},
         {"q": tr("Define downward communication with two examples."),
          "a": tr("Message from a higher to a lower level: an order to run line 2, or a circular "
                  "making helmets compulsory.")},
         {"q": tr("Define upward communication with two examples."),
          "a": tr("Message from a lower to a higher level: a breakdown report, or a suggestion about "
                  "a roller stand.")},
         {"q": tr("Name the three main types of communication by medium."),
          "a": tr("Verbal (words), non-verbal (body and voice) and visual (images and signs).")},
         {"q": tr("Give an example of intrapersonal communication."),
          "a": tr("Talking yourself through a startup sequence, or writing a to-do list and reading "
                  "it back.")},
         {"q": tr("What is mass communication?"),
          "a": tr("Communication with a large, scattered, anonymous audience through a medium such as "
                  "a newspaper, radio, website or social media.")},
     ]},
    {"title": tr("Barriers"),
     "items": [
         {"q": tr("Name the five families of barriers."),
          "a": tr("Physical, language (semantic), psychological, cultural and organisational.")},
         {"q": tr("Give a physical barrier and its cure."),
          "a": tr("Machine noise beside a phone call; the cure is to move to a quiet place and "
                  "confirm the figure back.")},
         {"q": tr("Give a language barrier and its cure."),
          "a": tr("\"Fix the DOB and reset the VFD\" to an apprentice; the cure is to define the term "
                  "or use plain words.")},
         {"q": tr("Give a psychological barrier and its cure."),
          "a": tr("A helper hides a mistake out of fear; the cure is to make early reporting safe "
                  "and to discuss the problem, not the person.")},
         {"q": tr("How does an organisation create barriers?"),
          "a": tr("Through too many levels, unclear channels, overload and a culture that does not "
                  "answer suggestions.")},
     ]},
]

_PRACTICE = [
    ("Define communication and name its four language skills.", 3,
     [p("<b>Communication</b> is the exchange of ideas, information or feelings between two or more "
        "people so that the receiver understands what the sender meant."),
      p("The four language skills are <b>listening, speaking, reading and writing</b> (LSRW). "
        "Listening and reading are receptive; speaking and writing are productive."),
      p("Example: a technician listens to the handover, reads the drawing, tells the helper which "
        "tools to bring and writes the entry in the log book - all four skills in one day.")]),
    ("Explain the communication cycle with its seven parts.", 4,
     [p("The cycle is <b>S + E + C + D + R + N + F</b>: Sender, Encoding, Channel, Decoding, "
        "Receiver, Noise and Feedback."),
      p("The sender has the idea, encodes it into words or signs, sends it through a channel such as "
        "a phone call, and the receiver decodes it. Noise can disturb any stage, and feedback closes "
        "the loop."),
      p("Example: the supervisor says \"torque the head bolts to 45 N·m\" (encode, channel = speech); "
        "the fitter repeats it back (feedback); a compressor running nearby is the noise.")]),
    ("What is the difference between hearing and listening?", 3,
     [p("<b>Hearing</b> is the physical reception of sound by the ear; it happens whether or not you "
        "pay attention."),
      p("<b>Listening</b> is active: you pay attention, interpret and remember, and often reply."),
      p("Example: you hear the machine alarm and keep working (hearing); you hear it, stop the line "
        "and check the coolant level (listening).")]),
    ("When is communication called effective? Give one example in favour and one against.", 4,
     [p("Communication is effective when the receiver's understanding matches the sender's intention, "
        "and the reply or action shows that it does."),
      p("Effective: \"Stop the conveyor, the guard is loose.\" One machine, one action, one reason."),
      p("Ineffective: \"Something seems wrong with the machine, maybe check it.\" No machine, no "
        "action, no urgency, so nothing happens until something breaks.")]),
    ("Name the seven Cs of effective communication with one example each.", 4,
     [p("The seven Cs are clear, concise, concrete, correct, coherent, complete and courteous."),
      p("Weak to better: \"Do the needful\" becomes \"replace the gasket and refit the cover\" "
        "(clear). \"At this point of time we are not in a position to supply\" becomes \"we cannot "
        "supply before Monday\" (concise). \"The motor is faulty\" becomes \"the motor draws 9 A "
        "against a rated 6 A\" (concrete)."),
      p("\"The bolts is loose\" becomes \"the bolts are loose\" (correct). A jumbled list is put in "
        "time order (coherent). \"Meeting on Monday\" gains a time, a room and an agenda (complete). "
        "\"Send it now\" becomes \"please send it by 4 pm so we can finish today\" (courteous).")]),
    ("Define downward communication and give three examples.", 3,
     [p("<b>Downward communication</b> flows from a higher level to a lower level of an organisation "
        "- from management to supervisors to workers."),
      p("Its purpose is to direct, inform and explain. Examples: an order (\"run line 2 this "
        "afternoon\"), a circular (\"safety helmets compulsory from Monday\") and a policy (\"overtime "
        "needs written approval\")."),
      p("The main risk is dilution: the number in \"reduce wastage by 10 %\" disappears by the time "
        "it reaches the shop floor.")]),
    ("Define upward communication and give three examples.", 3,
     [p("<b>Upward communication</b> flows from a lower level to a higher level - from workers to "
        "supervisors to management."),
      p("Its purpose is to report, suggest and warn. Examples: a breakdown report (\"line 2 down 45 "
        "minutes, belt replaced\"), a suggestion (\"a roller stand here would save two men\") and a "
        "warning (\"6205 bearings will finish by Thursday\")."),
      p("It is most valuable when it carries bad news early, as a fitter's report of a small crack "
        "prevents a coupling failure.")]),
    ("Differentiate between downward and upward communication.", 4,
     [p("Downward flows from top to bottom; upward flows from bottom to top."),
      p("Downward carries orders, circulars, policy and instructions, in a directive tone; upward "
        "carries reports, suggestions, grievances and warnings, in a factual tone."),
      p("Examples: \"helmets compulsory from Monday\" goes down, and \"two helmets are missing in our "
        "section\" comes up. The risk of downward flow is dilution; the risk of upward flow is "
        "filtering through fear.")]),
    ("What is verbal communication? Compare its oral and written forms.", 4,
     [p("<b>Verbal communication</b> uses words, either spoken or written."),
      p("Oral is instant, carries tone and gives immediate feedback, but leaves no record; written is "
        "slower, permanent and traceable, but feedback is delayed."),
      p("Examples: orally - \"hold the job, I am coming\"; in writing - \"job no. 118 is on hold "
        "pending inspection\". Details and orders belong in writing; quick corrections belong in "
        "speech.")]),
    ("Explain non-verbal communication with three examples.", 4,
     [p("<b>Non-verbal communication</b> carries meaning without words, through the body, the voice "
        "and the use of space."),
      p("Kinesics: a thumbs-up after inspection shows approval. Paralanguage: a flat \"fine\" can mean "
        "the opposite of the word. Proxemics: standing close to a machine to point at a fault shows "
        "where the problem is."),
      p("Two more channels are haptics (touch, such as a hand on the shoulder) and chronemics (time - "
        "arriving late for a handover signals that it is not important).")]),
    ("Give two examples of visual communication and say why engineers use it.", 3,
     [p("<b>Visual communication</b> uses drawings, charts, graphs, maps and signs."),
      p("Examples: a wiring diagram shows connections faster than a page of text, and a bar chart of "
        "monthly breakdowns shows a trend that a table of figures hides."),
      p("Engineers rely on it because a drawing carries shape, position and size at once, and because "
        "standard symbols (IS, ISO) mean the same thing to every reader - provided the drawing has a "
        "scale, a caption and a revision number.")]),
    ("Explain interpersonal, intrapersonal, extra personal and mass communication.", 4,
     [p("<b>Interpersonal</b> is between two people or in a small group, two-way and immediate - a "
        "supervisor explaining a mistake to a helper."),
      p("<b>Intrapersonal</b> is with yourself - rehearsing a phone call or writing a to-do list. "
        "<b>Extra personal</b> is between a human being and a non-human - telling a dog to sit, or "
        "reading a sensor's beep as a message."),
      p("<b>Mass</b> reaches a large, scattered, anonymous audience through a medium - a newspaper, "
        "radio, website or social-media post.")]),
    ("Name the five families of barriers and give one example of each.", 4,
     [p("<b>Physical</b>: two machines running beside a phone call in which a torque figure is given. "
        "<b>Language</b>: \"fix the DOB and reset the VFD\" to a first-year apprentice."),
      p("<b>Psychological</b>: a helper hides a mistake because he fears the supervisor's anger. "
        "<b>Cultural</b>: a junior will not correct a senior, even when the senior is wrong."),
      p("<b>Organisational</b>: six signatures are needed before a spare is ordered, so the machine "
        "stays down.")]),
    ("How can the barriers to communication be removed?", 4,
     [p("First name the barrier, then remove its cause."),
      p("For physical barriers, move to a quiet place and confirm key figures back. For language "
        "barriers, define terms, use plain words and give numbers with units. For psychological "
        "barriers, make early reporting safe and discuss the problem rather than the person."),
      p("For cultural barriers, ask what a gesture means before judging it; for organisational "
        "barriers, shorten the chain, keep one owner per message and answer grievances within a "
        "stated time.")]),
]

EXAM = [{"q": tr(q), "marks": m} for q, m, _parts in _PRACTICE]
PRACTICE_ANSWERS = [tr("".join(parts)) for _q, _m, parts in _PRACTICE]

LESSON_COUNT = sum(len(s["items"]) for s in NOTES)
