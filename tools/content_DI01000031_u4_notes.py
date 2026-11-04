"""DI01000031 Communication Skills in English - Unit 4: Techniques of Writing.

GTU 4.1-4.2, 8 h, 20 %, 14 marks, CO4: compose different types of written communication.

Author's policy for this subject (user instruction): the writing unit is taught by model - format,
then one complete e-mail or paragraph the student can copy the shape of.
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


def mail(lines):
    """A model e-mail as a boxed block, one line per row."""
    return "<p>" + "<br>".join(lines) + "</p>"


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
    ("Purdue Online Writing Lab - e-mail etiquette and paragraph structure",
     "https://owl.purdue.edu/"),
    ("British Council LearnEnglish - writing: e-mails and paragraphs",
     "https://learnenglish.britishcouncil.org/skills/writing"),
    ("William Sanborn Pfeiffer and T. V. S. Padmaja - Technical Communication: A Practical "
     "Approach (Pearson, 2007)", "https://www.pearson.com/"),
]

NOTES = [
    {"title": tr("1. The Shape of a Business E-mail"),
     "items": [
         card("1.1 The eight parts of an e-mail",
              h4("The blocks, top to bottom")
              + table(["Part", "What goes there", "Example"],
                      [("To", "the person who must act", "purchase@shreetools.in"),
                       ("Cc", "people who must know", "stores@abctools.in"),
                       ("Bcc", "people who must know, without the others seeing",
                        "your project manager"),
                       ("Subject", "one line naming the topic and the action",
                        "Inquiry - 12 mm MS plates, 2 tonnes"),
                       ("Salutation", "the greeting", "Dear Sir / Dear Ms Shah / Dear Sir or Madam"),
                       ("Opening", "why you are writing, in one sentence",
                        "We need 2 tonnes of 12 mm MS plates for our Surat site."),
                       ("Body", "the details, in short paragraphs or a list",
                        "quantity, delivery place, expected date, payment terms"),
                       ("Closing and signature", "the courteous close and who you are",
                        "Regards, / R. Patel, Site Engineer, ABC Engineering, Surat")])
              + h4("A model to copy")
              + mail(["To: purchase@shreetools.in",
                      "Cc: stores@abctools.in",
                      "Subject: Inquiry - 12 mm MS plates, 2 tonnes",
                      "",
                      "Dear Sir,",
                      "",
                      "We need 2 tonnes of 12 mm MS plates for a fabrication job at our Surat site.",
                      "Please send us your rate per tonne, the earliest delivery date and your",
                      "payment terms.",
                      "",
                      "We plan to place the order on Friday, so a reply by Thursday evening would",
                      "help us keep the schedule.",
                      "",
                      "Regards,",
                      "R. Patel",
                      "Site Engineer, ABC Engineering, Surat",
                      "+91 98xxxxxx21"])
              + h4("Common mistake")
              + p("Loading the subject line with the whole message, or leaving it empty. One clear "
                  "line: <i>Inquiry - 12 mm MS plates, 2 tonnes</i>."),
              "w1_email", syllabus_item="4.1"),
         card("1.2 Subject lines",
              h4("Four rules")
              + ol("Name the topic in two to five words.",
                   "Add the action or the document number.",
                   "No greetings, no \"urgent\" without a reason.",
                   "Keep it under about sixty characters so a phone shows it fully.")
              + h4("Weak and strong subjects")
              + table(["Weak", "Strong"],
                      [("Hello", "Inquiry - 12 mm MS plates, 2 tonnes"),
                       ("Invoice", "Invoice INV-2291 dated 4 March - payment status"),
                       ("Problem", "Complaint - 6 of 20 bearings undersize, PO-4471"),
                       ("Pls do the needful", "Approval needed: drawing DRG-118 revision B"),
                       ("Meeting", "Meeting - Friday 10 am, Room 4, line-2 downtime"),
                       ("Regards", "Status update - pump repair at Bhilad site")])
              + h4("What a subject line does")
              + p("It decides whether the mail is opened, filed or forgotten. A reader who searches "
                  "\"PO-4471\" six months later must find this mail.")
              + h4("Examples for the four e-mail types")
              + ul("<b>Inquiry:</b> Inquiry - 12 mm MS plates, 2 tonnes",
                   "<b>Reply:</b> Re: Inquiry - 12 mm MS plates: rate, delivery and terms",
                   "<b>Order:</b> Order PO-4471 - 20 bearings 6205, delivery by 20 March",
                   "<b>Complaint:</b> Complaint - short supply in PO-4471, 6 of 20 bearings")
              + h4("Common mistake")
              + p("Writing \"Re:\" yourself on a new mail. <i>Re:</i> belongs to a reply that the "
                  "system has already marked."),
              syllabus_item="4.1"),
         card("1.3 Salutations and closings",
              h4("Choose by relationship")
              + table(["Situation", "Salutation", "Closing"],
                      [("You do not know the name", "Dear Sir or Madam", "Yours faithfully"),
                       ("You know the name, formal", "Dear Mr Mehta / Dear Ms Shah", "Yours sincerely"),
                       ("Colleague or regular supplier", "Dear Amit / Dear Ritu", "Best regards"),
                       ("Customer you meet often", "Dear Sir / Dear Madam", "Regards"),
                       ("Team or group", "Dear Team / Dear All", "Regards"),
                       ("Very informal (not for exams)", "Hi Amit", "Thanks / Cheers")])
              + h4("Examples in place")
              + mail(["Dear Ms Shah,",
                      "",
                      "Thank you for your quotation of 6 March. We would like to place an order.",
                      "",
                      "Yours sincerely,",
                      "R. Patel, Site Engineer"])
              + h4("Three rules that save marks")
              + ul("Never open with \"Respected sir\" in a business mail unless your organisation "
                   "requires it; \"Dear Sir\" is standard.",
                   "Never close with \"Thanking you\" as a final line on its own; end with an action "
                   "sentence.",
                   "Do not mix registers: \"Dear Sir\" with \"Cheers\" looks careless.")
              + h4("Common mistake")
              + p("Using one closing for everybody. A complaint to a stranger and a note to a "
                  "colleague do not end the same way."),
              syllabus_item="4.1"),
         card("1.4 Tone: formal, neutral and informal",
              h4("Same request, three registers")
              + table(["Register", "Model sentence", "Use it when"],
                      [("Formal", "We should be grateful if you could confirm the delivery date by "
                                  "Friday.", "first contact, senior person, written record"),
                       ("Neutral", "Please confirm the delivery date by Friday.", "regular suppliers, "
                                                                                 "colleagues"),
                       ("Informal", "Can you confirm the date by Friday?", "people you work with "
                                                                           "every day")])
              + h4("What \"formal\" does not mean")
              + ul("It does not mean long. \"Please confirm by Friday\" is formal and clear.",
                   "It does not mean old-fashioned. Avoid \"kindly do the needful\" and \"revert back\".",
                   "It does not mean impersonal. \"Thank you\" is correct in a formal mail.")
              + h4("Examples of the same mail at two tones")
              + p("<b>Too harsh:</b> \"Send the report immediately. You are delaying the project.\"")
              + p("<b>Firm and polite:</b> \"The report is needed for Monday's review. Could you send "
                  "it by Friday afternoon?\"")
              + h4("Common mistake")
              + p("Thinking that politeness means weakness in a complaint. Facts plus a clear request "
                  "is the strongest tone there is."),
              syllabus_item="4.1"),
         card("1.5 Ten mistakes that cost marks",
              h4("The list")
              + table(["Mistake", "Fix"],
                      [("no subject", "one clear subject line"),
                       ("\"do the needful\"", "say exactly what you want done"),
                       ("a wall of text", "two or three short paragraphs, or a list"),
                       ("attachment not attached", "attach first, then write the mail"),
                       ("reply all by habit", "check the Cc list before you send"),
                       ("angry capitals", "facts, evidence, remedy - in that order"),
                       ("no signature", "name, role, organisation, phone"),
                       ("\"revert back\"", "\"reply\" or \"get back to me\""),
                       ("vague dates", "\"by Friday 5 pm\" not \"as soon as possible\""),
                       ("no closing action", "end with the one thing you want")])
              + h4("Examples: the same mail before and after")
              + ul("Before: \"Pls do the needful by EOD.\" After: \"Please send the inspection "
                   "report by 5 pm today.\"",
                   "Before: \"Mail attached.\" After: \"The inspection report is attached; see page "
                   "2 for the bore readings.\"",
                   "Before: \"Reaching shortly.\" After: \"I will reach the Sachin site by 11 am.\"")
              + h4("A checklist before you press send")
              + ol("Subject names the topic.",
                   "First line says why you are writing.",
                   "Every question is answered or asked.",
                   "Dates, numbers and part numbers are correct.",
                   "Attachment present, signature complete, Cc list right.")
              + h4("Common mistake")
              + p("Sending a long mail with no request in it. The reader finishes and still does not "
                  "know what to do."),
              syllabus_item="4.1"),
     ]},

    {"title": tr("2. The Four Types of E-mail"),
     "items": [
         card("2.1 Inquiry",
              h4("Structure")
              + ol("Who you are and what you need - one sentence.",
                   "The details: item, specification, quantity, place and date needed.",
                   "The questions: rate, stock, delivery, payment terms, warranty.",
                   "The deadline and a courteous close.")
              + h4("Model inquiry")
              + mail(["Subject: Inquiry - 12 mm MS plates, 2 tonnes",
                      "",
                      "Dear Sir,",
                      "",
                      "We are a fabrication unit in Surat and we need 2 tonnes of 12 mm MS plates",
                      "for a structural job.",
                      "",
                      "Please send us:",
                      "1. your rate per tonne, inclusive of GST;",
                      "2. the earliest delivery date to Surat;",
                      "3. your payment terms and any discount for 5 tonnes.",
                      "",
                      "We shall place the order on Friday, so a reply by Thursday evening would help",
                      "us plan the work.",
                      "",
                      "Regards,",
                      "R. Patel, Site Engineer, ABC Engineering, Surat"])
              + h4("Why this works")
              + ul("The first line says who is asking, so the supplier can judge the enquiry.",
                   "The questions are numbered, so they can be answered one by one.",
                   "The deadline is stated with the reason for it.")
              + h4("Common mistake")
              + p("Writing \"Please send details\" with no list. The supplier replies with a catalogue "
                  "and you still do not know the delivery date."),
              "w3_types", syllabus_item="4.1"),
         card("2.2 Reply to an inquiry",
              h4("Structure")
              + ol("Thank the sender and refer to their mail and date.",
                   "Answer their questions <b>in the same order</b>.",
                   "Add what they did not ask but need: packing, transport, validity.",
                   "Close with the next step and an offer of help.")
              + h4("Model reply")
              + mail(["Subject: Re: Inquiry - 12 mm MS plates: rate, delivery and terms",
                      "",
                      "Dear Mr Patel,",
                      "",
                      "Thank you for your inquiry of 6 March. Our answers are below, in your order.",
                      "",
                      "1. Rate: Rs 58,400 per tonne, inclusive of GST, ex-works Surat.",
                      "2. Delivery: 4 working days from the date of your purchase order.",
                      "3. Payment: 50 % with the order, 50 % against delivery.",
                      "4. For 5 tonnes we can offer a 2 % discount on the basic rate.",
                      "",
                      "The quotation is valid for 15 days. If you confirm by Friday, we can dispatch",
                      "on Monday.",
                      "",
                      "Please call me on +91 98xxxxxx10 if you need any clarification.",
                      "",
                      "Regards,",
                      "N. Shah, Sales Executive, Shree Tools Pvt Ltd"])
              + h4("Why this works")
              + ul("Every question is answered, numbered as asked.",
                   "The reply adds packing, validity and a phone number.",
                   "It ends with a date and a next step.")
              + h4("Common mistake")
              + p("Answering only the easy question and leaving the delivery date out. The customer "
                  "then has to write again, and the sale slows down."),
              syllabus_item="4.1"),
         card("2.3 Order",
              h4("Structure")
              + ol("Refer to the quotation and its date.",
                   "List item, specification, quantity, rate - in a table or numbered list.",
                   "State delivery address, date and mode.",
                   "State payment terms and ask for an acknowledgement.")
              + h4("Model order")
              + mail(["Subject: Order PO-4471 - 20 bearings 6205, delivery by 20 March",
                      "",
                      "Dear Ms Shah,",
                      "",
                      "With reference to your quotation of 6 March, please supply the following:",
                      "",
                      "Item: deep-groove ball bearing 6205 ZZ",
                      "Quantity: 20 numbers",
                      "Rate: Rs 212 per number, plus GST",
                      "Delivery: ABC Engineering, Plot 42, GIDC Sachin, Surat, by 20 March",
                      "",
                      "Payment will be made by NEFT within 15 days of delivery, as agreed.",
                      "",
                      "Please acknowledge this order and confirm the dispatch date.",
                      "",
                      "Regards,",
                      "R. Patel, Site Engineer, ABC Engineering"])
              + h4("Why this works")
              + ul("The quotation is referenced, so the price is not in dispute later.",
                   "Specification, quantity and rate sit together, which prevents the wrong part.",
                   "Delivery address and date are exact, and an acknowledgement is requested.")
              + h4("Common mistake")
              + p("Writing \"send 20 bearings\" with no size, no rate and no date. The supplier "
                  "chooses for you, and the wrong part arrives."),
              syllabus_item="4.1"),
         card("2.4 Complaint",
              h4("Structure - four moves")
              + table(["Move", "Content", "Example"],
                      [("1. Facts", "order number, date, what arrived",
                        "PO-4471, delivered 18 March; 6 of 20 bearings"),
                       ("2. Problem", "what is wrong, with measurement",
                        "bore 24.98 mm against 25.00 mm; they do not fit the shaft"),
                       ("3. Evidence", "photographs, test report, measurement sheet",
                        "photographs and our inspection sheet attached"),
                       ("4. Remedy", "replacement, credit note, or visit - one clear request",
                        "replace the 6 pieces by 25 March or issue a credit note")])
              + h4("Model complaint")
              + mail(["Subject: Complaint - 6 of 20 bearings undersize, PO-4471",
                      "",
                      "Dear Ms Shah,",
                      "",
                      "We received our order PO-4471 on 18 March. On inspection, 6 of the 20 bearings",
                      "have a bore of 24.98 mm against the specified 25.00 mm, so they will not fit",
                      "the shaft.",
                      "",
                      "Our inspection sheet and photographs are attached. The remaining 14 pieces are",
                      "correct and have been accepted.",
                      "",
                      "Please replace the 6 undersize pieces by 25 March, or issue a credit note for",
                      "Rs 1,272 plus GST. The line is waiting for these bearings, so an early reply",
                      "would help.",
                      "",
                      "Regards,",
                      "R. Patel, Site Engineer, ABC Engineering"])
              + h4("Why this works")
              + ul("It states facts and measurements, not anger.",
                   "It separates the good pieces from the bad, which is fair and speeds the answer.",
                   "It offers the supplier two clear options and a date.")
              + h4("Common mistake")
              + p("Sending an angry mail with no order number and no measurement. The supplier cannot "
                  "act, and the delay grows."),
              syllabus_item="4.1"),
         card("2.5 Exam strategy for the e-mail question",
              h4("Marks are usually given for these five things")
              + table(["Component", "What the examiner looks for"],
                      [("Format", "To, Subject, Salutation, Body, Closing, Signature"),
                       ("Content", "all the points in the question are covered"),
                       ("Organisation", "short paragraphs, numbered questions, logical order"),
                       ("Language", "correct grammar, spelling and punctuation"),
                       ("Tone", "polite, firm where needed, no slang")])
              + h4("Ten-minute plan")
              + ol("One minute: underline every point in the question.",
                   "Two minutes: write the subject line and list the points in order.",
                   "Five minutes: write the body, one point per sentence or line.",
                   "One minute: salutation, closing, signature.",
                   "One minute: check numbers, dates, spelling and that nothing is missing.")
              + h4("Model answer skeleton")
              + mail(["Subject: [topic + action]",
                      "",
                      "Dear [name],",
                      "",
                      "[why I am writing]",
                      "[the details, in the order asked]",
                      "[the request and the date]",
                      "",
                      "[closing],",
                      "[name, role, organisation]"])
              + h4("Common mistake")
              + p("Writing a beautiful paragraph that never names the item, the quantity or the date. "
                  "In a business mail, missing facts lose more marks than imperfect grammar."),
              syllabus_item="4.1"),
     ]},

    {"title": tr("3. Paragraph Writing"),
     "items": [
         card("3.1 What a paragraph must do",
              h4("Three parts")
              + table(["Part", "Work", "Example (topic: festivals)"],
                      [("Topic sentence", "states the one idea",
                        "Festivals are the calendar of a community's feelings."),
                       ("Supporting sentences", "3 to 5 facts, examples or reasons",
                        "Diwali brings lights and sweets; Navratri brings dance; Holi brings colour "
                        "and forgiveness."),
                       ("Concluding sentence", "rounds off or looks ahead",
                        "A festival is therefore not a holiday from life but a rehearsal of it.")])
              + h4("Word budget for 150 words")
              + ul("Topic sentence: 20-25 words.",
                   "Three to five supporting sentences: 90-110 words.",
                   "Concluding sentence: 20-25 words.")
              + h4("A model paragraph (149 words)")
              + p("Festivals are the calendar of a community's feelings. Every Indian month seems to "
                  "carry one, and each carries a different emotion. Diwali arrives with lamps, sweets "
                  "and a house swept clean, and it teaches that light is something people make "
                  "together. Navratri brings nine nights of dance, when neighbours who rarely speak "
                  "share the same ground. Holi is louder and more forgiving; it lets old quarrels "
                  "dissolve in colour and cold water. In towns like Surat, these festivals also keep "
                  "the economy moving, from potters and sweet-makers to the flower sellers at the "
                  "crossroads. What matters most is not the ritual but the return: the cousin who "
                  "comes home, the friend who is remembered, the meal that is eaten late and "
                  "together. A festival is therefore not a holiday from life; it is life, rehearsed "
                  "in colour and shared once a year.")
              + h4("Common mistake")
              + p("Writing four sentences that are all topic sentences. A paragraph needs support, not "
                  "a list of headings."),
              "w2_paragraph", syllabus_item="4.2"),
         card("3.2 Unity, coherence and linkers",
              h4("Unity")
              + p("One paragraph carries <b>one idea</b>. If a second idea arrives, it gets a second "
                  "paragraph. A reader should be able to name the topic in three words after the first "
                  "sentence.")
              + h4("Coherence")
              + p("The sentences must follow in a logical order: general to particular, cause to "
                  "effect, or problem to solution. Linkers make that order visible.")
              + h4("Linkers and what they signal")
              + table(["Signal", "Linkers"],
                      [("addition", "and, also, moreover, in addition, besides"),
                       ("contrast", "but, however, yet, on the other hand, although"),
                       ("cause", "because, since, as, due to"),
                       ("effect", "so, therefore, as a result, hence, consequently"),
                       ("example", "for example, for instance, such as, namely"),
                       ("sequence", "first, then, next, finally, meanwhile"),
                       ("conclusion", "in short, to sum up, therefore, in the end")])
              + h4("Examples")
              + p("<b>Without linkers:</b> \"The machine was old. It broke often. We replaced it.\"")
              + p("<b>With linkers:</b> \"The machine was old and, as a result, it broke often; "
                  "therefore we replaced it.\"")
              + h4("Common mistake")
              + p("Starting every sentence with a linker. Two or three in a paragraph are enough; more "
                  "makes the writing sound mechanical."),
              syllabus_item="4.2"),
         card("3.3 Planning 150 words in five minutes",
              h4("The five-minute plan")
              + ol("Underline the key word in the topic: <i>festivals</i>, <i>environment</i>, "
                   "<i>sport</i>.",
                   "Choose one angle - do not try to say everything. For festivals: what they do to "
                   "people, not a list of dates.",
                   "Write the topic sentence in one line.",
                   "Jot three or four supports as single words: lights, dance, colour, return.",
                   "Write, then cut. A 165-word draft becomes a 150-word paragraph.")
              + h4("Worked planning sheet (topic: nature and environment)")
              + table(["Step", "Your note"],
                      [("Angle", "nature gives free services that money cannot replace"),
                       ("Topic sentence", "A tree is the cheapest machine a city owns."),
                       ("Support 1", "shade and cool air in a Surat summer"),
                       ("Support 2", "roots hold soil in the monsoon"),
                       ("Support 3", "birds and insects return when trees return"),
                       ("Conclusion", "planting is a civic duty, not a decoration")])
              + h4("Why 150 words")
              + p("It is long enough for an idea and its proof, and short enough to be read in one "
                  "breath. Counting words is not the aim; covering the idea is.")
              + h4("Common mistake")
              + p("Writing 250 words to be safe. Long paragraphs lose unity and lose marks for "
                  "relevance."),
              syllabus_item="4.2"),
         card("3.4 Model paragraph: Festivals",
              h4("The paragraph (152 words)")
              + p("A festival is a date on which a whole town agrees to remember something together. "
                  "In Gujarat the year turns on such dates: Uttarayan fills the sky with kites and the "
                  "terraces with cousins; Navratri fills nine nights with garba until the street "
                  "itself seems to dance; Diwali fills the dark with lamps and the doorways with "
                  "rangoli. Each one looks like celebration, but each one is also a lesson. Uttarayan "
                  "teaches that the wind is a friend if the string is strong. Navratri teaches that a "
                  "community is made by people who move together. Diwali teaches that light is "
                  "something people make, not something they wait for. The best part arrives after "
                  "the rituals, when the family sits down to eat far too late and talks far too long. "
                  "Festivals, then, are not breaks from ordinary life; they are ordinary life, "
                  "remembered properly once a year.")
              + h4("Why it works")
              + ul("One idea: festivals teach while they celebrate.",
                   "Three supports, one per festival, each with a lesson.",
                   "A concrete ending: the late meal and the long talk.")
              + h4("Common mistake")
              + p("Describing five festivals in one line each. Three, with a lesson attached, is a "
                  "paragraph; five is a list."),
              syllabus_item="4.2"),
         card("3.5 Model paragraph: Nature and environment",
              h4("The paragraph (151 words)")
              + p("A tree is the cheapest machine a city owns. It costs nothing to run, needs no "
                  "electricity and quietly does the work of an air-conditioner, a water tank and a "
                  "bird sanctuary at the same time. In a Surat summer, the difference between a road "
                  "with trees and a road without them can be felt within ten steps. When the monsoon "
                  "comes, the same roots hold the soil that would otherwise silt the drains. When the "
                  "leaves fall, they return to the earth the food the tree took from it, and nothing "
                  "is wasted. Birds and insects come back within a season of planting, which is the "
                  "clearest sign that a place is alive. None of this appears in a budget, which is "
                  "why it is so easily forgotten. Planting a tree, then, is not decoration; it is "
                  "civic maintenance of the cheapest and most useful kind.")
              + h4("Why it works")
              + ul("The topic sentence is an image, not a slogan.",
                   "Each support answers a different question: heat, water, soil, life.",
                   "The conclusion turns the image into an argument about duty.")
              + h4("Common mistake")
              + p("Writing \"we should save trees because they are important\". That is an opinion "
                  "without a single detail to hold it up."),
              syllabus_item="4.2"),
         card("3.6 Model paragraph: A famous personality",
              h4("The paragraph (150 words)")
              + p("Dr A. P. J. Abdul Kalam is remembered less for the posts he held than for the way he "
                  "used them. He came from Rameswaram, sold newspapers as a boy, studied physics and "
                  "aerospace engineering, and went on to lead India's missile programmes at a time "
                  "when the country had very little of the technology it needed. What made him "
                  "unusual was not the success but the audience he chose afterwards: schoolchildren. "
                  "For twenty years he spoke in classrooms, answered questions for hours and told "
                  "students that a dream is not what you see in sleep but what does not let you "
                  "sleep. He carried his own bag, kept a modest room and refused the comforts his "
                  "position could have bought. When he died in 2015, in Shillong, he was teaching. "
                  "That is the sentence his life deserves: a scientist who spent his last hour "
                  "explaining something to students.")
              + h4("Why it works")
              + ul("Facts, not adjectives: Rameswaram, newspapers, missiles, Shillong.",
                   "The paragraph chooses one angle - what he did with success.",
                   "The last line closes the idea and the life together.")
              + h4("Common mistake")
              + p("Listing every award from memory. Two or three facts used well beat ten facts used "
                  "as a list."),
              syllabus_item="4.2"),
         card("3.7 Model paragraph: Favourite sport",
              h4("The paragraph (148 words)")
              + p("Cricket is a slow game that rewards patience more than speed, which is why it suits "
                  "a country that has learned to wait. A Test match takes five days and can still end "
                  "without a result, yet people sit in the sun for all five, because the interest lies "
                  "in the small contest inside the large one: a bowler against a batsman, over after "
                  "over, each one adjusting to the other. On the street outside my house the game is "
                  "simpler. A tennis ball, a broomstick for a stump and a rule that a shot into the "
                  "neighbour's compound is out. Nobody keeps a score for long, and nobody minds. What "
                  "the game teaches is easy to state and hard to practise: watch the ball, play the "
                  "one you can reach, and stay at the crease. Everything else, including the result, "
                  "is a bonus.")
              + h4("Why it works")
              + ul("A clear angle: patience, in the stadium and on the street.",
                   "Two settings compared, which keeps the paragraph moving.",
                   "The ending gives a rule of life drawn from the game.")
              + h4("Common mistake")
              + p("Describing the rules of the game. The reader wants to know why you like it, not how "
                  "many players are on each side."),
              syllabus_item="4.2"),
         card("3.8 Model paragraph: Friends and family",
              h4("The paragraph (150 words)")
              + p("A family is given to you; a friend is chosen, and the two are more alike than they "
                  "look. In a family you are known before you have done anything, which is a comfort "
                  "and sometimes a trap. With a friend you are known for what you do, and the knowing "
                  "has to be earned conversation by conversation. The best families contain "
                  "friendship, and the best friendships slowly become family: the friend who comes to "
                  "the hospital at two in the morning, the one who remembers your father's name, the "
                  "one who tells you the truth about your work when nobody else will. My own "
                  "arrangement is simple. At home there are four people who know my worst moods and "
                  "ignore them. Outside there are two friends who know my best plans and test them. "
                  "Between the two, a person is held steady.")
              + h4("Why it works")
              + ul("A comparison gives the paragraph its structure: given versus chosen.",
                   "Examples are specific: the hospital, the father's name, the honest friend.",
                   "The last line answers the topic in a single image.")
              + h4("Common mistake")
              + p("Writing only about family or only about friends when the topic names both. The "
                  "comparison is the paragraph."),
              syllabus_item="4.2"),
     ]},

    {"title": tr("4. Practice Questions with Model Answers"),
     "items": []},
]

EQUATIONS = [
    {"title": tr("E-mail skeleton"),
     "items": [
         {"terms": tr("Header"), "a": tr("To, Cc, Bcc, Subject")},
         {"terms": tr("Salutation"), "a": tr("Dear Sir / Dear Ms Shah / Dear Sir or Madam")},
         {"terms": tr("Body"), "a": tr("purpose, details in order, request with a date")},
         {"terms": tr("Closing"), "a": tr("Yours faithfully / Yours sincerely / Regards")},
         {"terms": tr("Signature"), "a": tr("name, role, organisation, phone")},
     ]},
    {"title": tr("Paragraph skeleton"),
     "items": [
         {"terms": tr("Topic sentence"), "a": tr("one idea in 20-25 words")},
         {"terms": tr("Support"), "a": tr("3-5 facts, examples or reasons, 90-110 words")},
         {"terms": tr("Conclusion"), "a": tr("rounds off or looks ahead, 20-25 words")},
         {"terms": tr("Length"), "a": tr("about 150 words, one idea per paragraph")},
     ]},
]

VIVA = [
    {"title": tr("E-mail"),
     "items": [
         {"q": tr("Name the parts of a business e-mail."),
          "a": tr("To, Cc, Bcc, Subject, Salutation, Opening, Body, and Closing with signature.")},
         {"q": tr("What makes a good subject line?"),
          "a": tr("It names the topic in two to five words and adds the action or the document "
                  "number, for example \"Inquiry - 12 mm MS plates, 2 tonnes\".")},
         {"q": tr("How do you close a mail to a person whose name you know?"),
          "a": tr("\"Yours sincerely\" with the name; \"Yours faithfully\" is for \"Dear Sir or "
                  "Madam\", where the name is unknown.")},
         {"q": tr("What is the difference between Cc and Bcc?"),
          "a": tr("Cc shows the copied person to everybody; Bcc copies without the other recipients "
                  "seeing the address.")},
         {"q": tr("What four things must an inquiry e-mail contain?"),
          "a": tr("Who you are, the specification and quantity, the questions (rate, delivery, "
                  "terms), and the date by which you need the reply.")},
         {"q": tr("What four moves make a good complaint?"),
          "a": tr("Facts with the order number, the problem with a measurement, the evidence, and one "
                  "clear remedy with a date.")},
     ]},
    {"title": tr("Paragraph"),
     "items": [
         {"q": tr("What are the three parts of a paragraph?"),
          "a": tr("A topic sentence, three to five supporting sentences, and a concluding sentence.")},
         {"q": tr("What is unity in a paragraph?"),
          "a": tr("Every sentence serves one idea; a second idea needs a second paragraph.")},
         {"q": tr("What is coherence?"),
          "a": tr("The sentences follow in a clear logical order, and linkers such as however, "
                  "therefore and for example make that order visible.")},
         {"q": tr("How many words is the paragraph in this syllabus?"),
          "a": tr("About 150 words, which is roughly twelve to fifteen lines.")},
         {"q": tr("Give four linkers of contrast and result."),
          "a": tr("Contrast: but, however, on the other hand, although. Result: so, therefore, as a "
                  "result, consequently.")},
         {"q": tr("How should a 150-word paragraph be planned?"),
          "a": tr("Choose one angle, write the topic sentence, jot three or four supports as single "
                  "words, write the draft, then cut it down to about 150 words.")},
     ]},
]

_PRACTICE = [
    ("Write an inquiry e-mail to a supplier asking for the rate and delivery of 50 safety helmets.",
     5,
     [p("<b>Subject:</b> Inquiry - 50 safety helmets, delivery to Surat"),
      p("Dear Sir,"),
      p("We are a fabrication unit at GIDC Sachin, Surat, and we need 50 industrial safety helmets "
        "(IS 2925 certified) for our shop floor."),
      p("Please send us your rate per piece inclusive of GST, the earliest delivery date to Sachin, "
        "the brand and certification you supply, and your payment terms. We shall place the order on "
        "Monday, so a reply by Friday evening would help us plan."),
      p("Regards,<br>R. Patel<br>Site Engineer, ABC Engineering, Surat<br>+91 98xxxxxx21"),
      p("<b>Why it scores:</b> the subject names topic and quantity; the first line says who is "
        "asking; the questions are listed; the deadline comes with the reason for it.")]),
    ("Reply to that inquiry, giving a rate of Rs 240 per helmet, delivery in five days and 30 days "
     "credit.", 5,
     [p("<b>Subject:</b> Re: Inquiry - 50 safety helmets: rate, delivery and terms"),
      p("Dear Mr Patel,"),
      p("Thank you for your inquiry of 6 March. We can supply 50 IS 2925 certified helmets at "
        "Rs 240 per piece inclusive of GST."),
      p("Delivery will be made to your Sachin address within five working days of your order. We "
        "offer 30 days credit to regular customers, and the rate is valid for 30 days. Our helmets "
        "carry a one-year replacement guarantee against manufacturing defects."),
      p("If you confirm by Monday, we can dispatch on Tuesday. Please call me on +91 98xxxxxx10 for "
        "any clarification."),
      p("Regards,<br>N. Shah<br>Sales Executive, Shree Tools Pvt Ltd"),
      p("<b>Why it scores:</b> every question is answered in the order it was asked, and the reply "
        "adds two useful facts the buyer did not ask for: the guarantee and the validity.")]),
    ("Place an order for 20 ball bearings 6205 ZZ at Rs 212 each, delivery by 20 March.",
     5,
     [p("<b>Subject:</b> Order PO-4471 - 20 bearings 6205 ZZ, delivery by 20 March"),
      p("Dear Ms Shah,"),
      p("With reference to your quotation of 6 March, please supply the following:"),
      p("Item: deep-groove ball bearing 6205 ZZ<br>Quantity: 20 numbers<br>Rate: Rs 212 per number, "
        "plus GST<br>Delivery: ABC Engineering, Plot 42, GIDC Sachin, Surat, by 20 March"),
      p("Payment will be made by NEFT within 15 days of delivery, as agreed in your quotation. Please "
        "acknowledge this order and confirm the dispatch date."),
      p("Regards,<br>R. Patel<br>Site Engineer, ABC Engineering"),
      p("<b>Why it scores:</b> the quotation is referenced, the specification sits next to the "
        "quantity, the delivery address is complete, and an acknowledgement is requested.")]),
    ("Write a complaint about 6 of 20 bearings that are undersize.", 5,
     [p("<b>Subject:</b> Complaint - 6 of 20 bearings undersize, PO-4471"),
      p("Dear Ms Shah,"),
      p("We received order PO-4471 on 18 March. On inspection, 6 of the 20 bearings measure 24.98 mm "
        "at the bore against the specified 25.00 mm, so they do not fit the shaft."),
      p("Our inspection sheet and photographs are attached. The other 14 pieces are correct and have "
        "been accepted."),
      p("Please replace the 6 undersize pieces by 25 March, or issue a credit note for Rs 1,272 plus "
        "GST. The line is waiting for these bearings, so an early reply would help."),
      p("Regards,<br>R. Patel<br>Site Engineer, ABC Engineering"),
      p("<b>Why it scores:</b> facts first, measured; the good pieces are separated from the bad; two "
        "clear remedies with a date; the tone is firm without a single angry word.")]),
    ("Rewrite these subject lines: (a) Hello (b) Problem (c) Pls do the needful.", 3,
     [p("(a) \"Hello\" says nothing. Rewrite: <b>Inquiry - 12 mm MS plates, 2 tonnes</b>."),
      p("(b) \"Problem\" does not say where or how big. Rewrite: <b>Complaint - 6 of 20 bearings "
        "undersize, PO-4471</b>."),
      p("(c) \"Pls do the needful\" asks for nothing in particular. Rewrite: <b>Approval needed: "
        "drawing DRG-118 revision B</b>."),
      p("A good subject line names the topic and the action in five words or fewer, so that the "
        "reader knows before opening whether to act now or later.")]),
    ("Describe the format of a business e-mail.", 4,
     [p("A business e-mail has eight blocks: To, Cc and Bcc for the recipients, a Subject line, a "
        "Salutation, an opening sentence, the body, and a closing with a signature."),
      p("The subject names the topic and the action; the salutation matches the relationship (\"Dear "
        "Sir or Madam\" with \"Yours faithfully\", \"Dear Ms Shah\" with \"Yours sincerely\"); the "
        "opening says why you are writing; the body gives the details in short paragraphs or a "
        "numbered list."),
      p("The closing states the one action you want and the date, and the signature carries name, "
        "role, organisation and phone number. Format earns marks because it shows the reader at once "
        "who the mail is for and what it is about.")]),
    ("Write a paragraph of about 150 words on Festivals.", 5,
     [p("Festivals are the days on which a community agrees to remember what it values. In Surat, "
        "Uttarayan turns the terraces into a meeting place, and the sky becomes a field of kites "
        "flown by every generation at once. Navratri gathers nine nights of garba, so that neighbours "
        "who only nod to each other during the year end up dancing in the same circle. Diwali is "
        "quieter and closer: lamps on the window, rangoli at the door, sweets carried from house to "
        "house until nobody can eat another. Each festival looks like entertainment, but each one "
        "carries a lesson about living together - share the terrace, share the circle, share the "
        "food. The best moment usually comes late at night, when the rituals are over and the family "
        "sits talking far longer than planned. A festival, then, is not an escape from ordinary life; "
        "it is ordinary life, carefully remembered once a year.")]),
    ("Write a paragraph of about 150 words on Nature and Environment.", 5,
     [p("A city that plants trees is buying services it could never afford to install. A single "
        "shade tree cools a stretch of road, holds the dust down and gives a hundred birds somewhere "
        "to sit, all without a rupee of maintenance. In a Surat summer the difference is easy to "
        "test: walk ten steps from a bare footpath to a shaded one and feel the temperature change. "
        "When the monsoon arrives, the same roots hold the soil that would otherwise silt the drains "
        "and flood the low-lying streets. Fallen leaves return to the soil the food the tree has "
        "taken, so nothing is wasted in the whole cycle. Birds and insects come back within a season "
        "of planting, which is the clearest proof that a place is alive again. None of this appears "
        "in a municipal budget, and that is exactly why it is neglected. Planting, then, is not "
        "decoration; it is the cheapest maintenance a city can do.")]),
    ("Write a paragraph of about 150 words on your favourite sport.", 5,
     [p("Kabaddi is the only sport I know that begins with a single person walking into a crowd of "
        "seven. There is no equipment, no field to book and no excuse: a line in the dust is enough. "
        "The raider has thirty seconds to tag an opponent and get back, and in those thirty seconds "
        "everything is decided by breath, balance and nerve. That is what makes it worth watching. "
        "The defender who stands still is lost; the raider who hesitates is caught. In my village the "
        "game is played after the evening meal, under one tube light, with the whole street as "
        "spectators and commentators. Nobody keeps a record of wins and losses, and nobody minds. "
        "What the game teaches can be said in one line: go in alone, keep breathing, and come back "
        "before you are held. Everything else is a scoreboard.")]),
    ("Write a paragraph of about 150 words on a famous personality you admire.", 5,
     [p("Kalpana Chawla is remembered for a sentence she wrote in her school magazine: that a "
        "dream is not what you see in sleep, but what does not let you sleep. She grew up in "
        "Karnal, studied aeronautical engineering in Chandigarh, and then crossed an ocean to study "
        "and work in a field that hardly had room for a woman from a small Indian town. She became an "
        "astronaut, flew on Columbia in 1997, and died with her crew in 2003 when the shuttle broke "
        "apart on its way home. What I admire is not the tragedy but the arithmetic behind the career: "
        "one application after another, one refusal after another, until the answer changed. She "
        "never pretended the work was easy, and she never suggested that the difficulty was a reason "
        "to stop. That is a useful thing to remember in an examination hall and, more importantly, in "
        "a workshop.")]),
    ("Write a paragraph of about 150 words on Friends and Family members.", 5,
     [p("A family is given and a friend is chosen, and the two arrangements support each other more "
        "than we usually admit. At home a person is known before he has done anything, which is a "
        "comfort on bad days and a small trap on good ones, because nobody there expects you to "
        "change. With friends you are known for what you do, and that knowledge has to be renewed "
        "conversation by conversation, which keeps a person honest. The best families contain "
        "friendship, and the best friendships slowly become family: the friend who reaches the "
        "hospital at two in the morning, the one who remembers your father's name, the one who tells "
        "you plainly that your work is not good enough. In my own life there are four people at home "
        "who ignore my worst moods and two friends outside who test my best plans. Held between those "
        "two, a person stays steady.")]),
    ("Identify the topic sentence, the supports and the conclusion in this paragraph: \"A workshop "
     "is a noisy place, and noise is a safety hazard. It hides the sound of a bearing beginning to "
     "fail, so a fault is noticed late. It makes instructions hard to hear, so mistakes multiply. It "
     "tires the ear over eight hours, so attention drops exactly when it is needed. A quiet machine "
     "is therefore not a luxury; it is part of the guard.\"", 4,
     [p("<b>Topic sentence:</b> \"A workshop is a noisy place, and noise is a safety hazard.\" It "
        "states the one idea that the rest of the paragraph proves."),
      p("<b>Supports:</b> the three sentences beginning \"It hides...\", \"It makes...\" and \"It "
        "tires...\". Each names one effect of noise - late fault detection, wrong instructions, "
        "dropping attention."),
      p("<b>Concluding sentence:</b> \"A quiet machine is therefore not a luxury; it is part of the "
        "guard.\" The word \"therefore\" shows that the sentence draws the idea together, and it "
        "leaves the reader with a policy, not just a fact.")]),
    ("Improve this paragraph: \"Sports are good. Everyone should play. It keeps us healthy. "
     "It teaches us discipline. So we should play sports.\"", 4,
     [p("Improved: \"Sport is the cheapest form of self-education a student can get. It keeps the "
        "body healthy, but that is the least of it. A player learns to lose in public and to try "
        "again the next week; a team learns that a good pass matters more than a good shot; a captain "
        "learns that shouting is not the same as leading. These lessons arrive without a lecture and "
        "stay longer than most lectures do. A school without a ground, then, is not short of a "
        "playground; it is short of a classroom.\""),
      p("What changed: a topic sentence with an idea instead of a slogan, three distinct supports "
        "instead of three repetitions, a linker (\"then\") before the conclusion, and a closing line "
        "that says something the first line did not."),
      p("The original paragraph had four sentences making one point; the improved one has one idea "
        "supported from four angles, which is what the examiner is looking for.")]),
]

EXAM = [{"q": tr(q), "marks": m} for q, m, _parts in _PRACTICE]
PRACTICE_ANSWERS = [tr("".join(parts)) for _q, _m, parts in _PRACTICE]

LESSON_COUNT = sum(len(s["items"]) for s in NOTES)
