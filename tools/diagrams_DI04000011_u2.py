"""DI04000011 Software Engineering - Unit 2 diagrams: requirements, design, DFD, UML."""
import os
from flowchart_lib import *
from diagrams_DI03000021_u1 import box, BLUE, BLUEF, GREEN, GREENF, ORANGE, ORANGEF, RED, REDF, YEL, TEAL, TEALF
from diagrams_DI03000011_u1 import note
from diagrams_DI03000031_u1 import lines, rarrow, grid, PF, GREY
from diagrams_DI03000061_u1 import code, OUT


def req_types():
    b = title("Functional vs Non-Functional Requirements")
    b += box(12, 46, 160, 122, GREENF, GREEN, 8, 1.3)
    b += text(92, 64, "FUNCTIONAL", 9.4, weight="bold", color=GREEN)
    b += text(92, 78, "what the system DOES", 7.8, color=GREY)
    b += code(22, 94, ["- student books a seat",
                       "- system issues a receipt",
                       "- admin adds a route",
                       "- search by date"], 8.2, 14)
    b += box(188, 46, 160, 122, BLUEF, BLUE, 8, 1.3)
    b += text(268, 64, "NON-FUNCTIONAL", 9.4, weight="bold", color=BLUE)
    b += text(268, 78, "constraints & qualities", 7.8, color=GREY)
    b += code(198, 94, ["- reply within 2 seconds",
                        "- 1000 users together",
                        "- encrypted passwords",
                        "- works on Android 10+"], 8.2, 14)
    b += note(12, 186, 336, ["Test: functional requirements appear as",
                             "VERBS of the system; non-functionals",
                             "measure HOW WELL it performs them."], size=9.2)
    return svg(360, 246, b)


def gather():
    b = title("Requirement Gathering Techniques")
    items = [("interviews", "1-to-1 with users", BLUE, BLUEF),
             ("questionnaires", "many users, fast", GREEN, GREENF),
             ("brainstorming/workshops", "stakeholders together", ORANGE, ORANGEF),
             ("observation", "watch work happen", RED, REDF),
             ("document study", "old forms, logs, files", P, PF),
             ("prototyping", "show-and-learn demo", TEAL, TEALF)]
    for i, (t, d, c, cf) in enumerate(items):
        x = 12 + (i % 2) * 176
        y = 44 + (i // 2) * 56
        b += box(x, y, 160, 48, cf, c, 7, 1.2)
        b += text(x + 80, y + 17, t, 8.4, weight="bold", color=c)
        b += text(x + 80, y + 33, d, 7.8, color=GREY)
    b += note(12, 222, 336, ["Blend them: interview the registrar,",
                             "questionnaire the students, watch the",
                             "counter clerks actually work."], size=9.2)
    return svg(360, 278, b)


def srs():
    b = title("SRS: Structure and Qualities")
    b += box(12, 44, 158, 168, PF, P, 8, 1.3)
    b += text(91, 62, "SRS skeleton", 9.0, weight="bold", color=P)
    b += code(22, 78, ["1. Introduction",
                       "   purpose, scope",
                       "2. Overall description",
                       "   users, constraints",
                       "3. Specific requirements",
                       "   functional +",
                       "   non-functional",
                       "4. Appendices"], 8.0, 13.5)
    b += box(188, 44, 160, 168, GREENF, GREEN, 8, 1.3)
    b += text(268, 62, "a GOOD SRS is...", 9.0, weight="bold", color=GREEN)
    b += code(198, 78, ["correct", "unambiguous", "complete", "consistent",
                        "ranked (must/nice)", "verifiable", "modifiable",
                        "traceable"], 8.4, 15)
    b += note(12, 230, 336, ["'Unambiguous' is tested in exams: every",
                             "sentence must have ONE meaning, else two",
                             "developers build two different systems.",
                             "Customer req = plain words of the client;",
                             "functional req = testable system action."], size=9.0)
    return svg(360, 324, b)


def analysis_vs_design():
    b = title("Analysis vs Design: WHAT vs HOW")
    b += box(14, 48, 156, 74, TEALF, TEAL, 8, 1.3)
    b += text(92, 66, "ANALYSIS", 10, weight="bold", color=TEAL)
    b += code(24, 82, ["what the system must do",
                       "for USERS: requirements,",
                       "use cases, DFD of needs"], 7.8, 12.5)
    b += box(190, 48, 156, 74, ORANGEF, ORANGE, 8, 1.3)
    b += text(268, 66, "DESIGN", 10, weight="bold", color=ORANGE)
    b += code(200, 82, ["how to build it: modules,",
                        "classes, algorithms, db",
                        "schema, interfaces"], 7.8, 12.5)
    b += f'<polygon points="172,84 182,79 182,89" fill="{GREY}"/>'
    b += f'<polygon points="188,84 178,79 178,89" fill="{GREY}"/>'
    b += grid(12, 136, [100, 116, 116], [
        ["viewpoint", "analysis", "design"],
        ["question", "what?", "how?"],
        ["audience", "customer, analyst", "developers"],
        ["artifacts", "SRS, use cases", "class/DFD design"],
    ], rh=19, size=8.2)
    b += note(12, 224, 336, ["Good design is: correct, complete,",
                             "understandable, and CHANGEABLE - the",
                             "last is why cohesion/coupling matter."], size=9.2)
    return svg(360, 290, b)


def cohesion():
    b = title("Cohesion: Best to Worst")
    lv = [("functional", "one clear job: addMarks()", GREEN),
          ("sequential", "output feeds next step", GREEN),
          ("communicational", "same data, few jobs", TEAL),
          ("procedural", "a fixed sequence of steps", ORANGE),
          ("temporal", "things done 'at the same time'", ORANGE),
          ("logical", "'all the print functions'", RED),
          ("coincidental", "laundry basket module", RED)]
    for i, (t, d, c) in enumerate(lv):
        y = 44 + i * 30
        w = 236
        hf = {"#2E7D32": GREENF, "#00796B": TEALF, "#E07B00": ORANGEF, "#C62828": REDF}[c]
        b += box(60, y, w, 24, hf, c, 6, 1.1)
        b += text(60 + w / 2, y + 15, t + "  -  " + d, 8.0, weight="bold", color=c)
        b += text(52, y + 15, str(7 - i), 8.6, weight="bold", color=c, anchor="end")
    b += text(56, 38, "best", 7.8, color=GREEN, anchor="start")
    b += text(56, 50 + 6 * 30 + 18, "worst", 7.8, color=RED, anchor="start")
    b += line("M36 56 L36 232", GREY, 1.2)
    b += f'<polygon points="36,232 32,224 40,224" fill="{GREY}"/>'
    b += note(12, 262, 336, ["Cohesion = how strongly items INSIDE one",
                             "module belong together. Aim functional;",
                             "split anything coincidental."], size=9.2)
    return svg(360, 312, b)


def coupling():
    b = title("Coupling: Worst to Best")
    lv = [("content", "one module rewrites another's code", RED),
          ("common", "share global data", RED),
          ("external", "share a file format/protocol", ORANGE),
          ("control", "pass flags steering logic", ORANGE),
          ("stamp", "pass whole records partly unused", "#F9A825"),
          ("data", "pass just the needed parameters", GREEN),
          ("message", "talk only via messages/events", GREEN)]
    for i, (t, d, c) in enumerate(lv):
        y = 44 + i * 30
        hf = {"#C62828": REDF, "#E07B00": ORANGEF, "#2E7D32": GREENF, "#F9A825": "#FFF9E0"}[c]
        b += box(60, y, 286, 24, hf, c, 6, 1.1)
        b += text(203, y + 15, t + "  -  " + d, 8.0, weight="bold", color=INK if c == "#F9A825" else c)
        b += text(52, y + 15, str(i + 1), 8.6, weight="bold", color=c if c != "#F9A825" else GREY, anchor="end")
    b += text(56, 38, "worst", 7.8, color=RED, anchor="start")
    b += text(56, 50 + 6 * 30 + 18, "best", 7.8, color=GREEN, anchor="start")
    b += line("M36 56 L36 232", GREY, 1.2)
    b += f'<polygon points="36,232 32,224 40,224" fill="{GREY}"/>'
    b += note(12, 262, 336, ["Coupling = how much modules DEPEND on",
                             "one another. High cohesion + low coupling",
                             "= modules you can change, test and reuse",
                             "independently."], size=9.2)
    return svg(360, 312, b)


def dfd_symbols():
    b = title("DFD Symbols (Yourdon-DeMarco)")
    rows = [(64, "process", "action/work on data"),
            (124, "external entity", "outside person/system"),
            (184, "data store", "kept data (file/db)"),
            (244, "data flow", "arrow with a label")]
    # row 1: process circle
    b += f'<circle cx="66" cy="64" r="16" fill="{GREENF}" stroke="{GREEN}" stroke-width="1.4"/>'
    # row 2: entity
    b += box(22, 110, 88, 28, BLUEF, BLUE, 2, 1.2)
    # row 3: data store parallel lines
    b += line("M26 178 L110 178", RED, 1.8) + line("M26 190 L110 190", RED, 1.8)
    # row 4: flow arrow
    b += line("M26 244 L100 244", GREY, 1.6)
    b += f'<polygon points="100,244 92,240 92,248" fill="{GREY}"/>'
    for y, t, d in rows:
        b += text(126, y + 3, t, 8.8, weight="bold", color=INK, anchor="start")
        b += text(232, y + 3, d, 8.0, color=GREY, anchor="start")
    b += note(12, 276, 336, ["Rule: data flows through processes; never",
                             "entity-to-entity directly; every store is",
                             "written/read only via a process bubble."], size=9.2)
    return svg(360, 340, b)


def dfd_levels():
    b = title("DFD Levels: Food Ordering System")
    b += text(60, 50, "context level", 9.2, weight="bold", color=P)
    b += box(12, 58, 76, 30, BLUEF, BLUE, 2, 1.2) + text(50, 77, "customer", 7.8, color=BLUE)
    b += f'<circle cx="196" cy="73" r="24" fill="{GREENF}" stroke="{GREEN}" stroke-width="1.4"/>'
    b += text(196, 76, "OrderFood", 8.4, weight="bold", color=GREEN)
    b += box(296, 58, 60, 30, BLUEF, BLUE, 2, 1.2) + text(326, 77, "payment", 7.8, color=BLUE)
    b += line("M88 73 L170 73", GREY, 1.4) + f'<polygon points="170,73 162,69 162,77" fill="{GREY}"/>'
    b += text(129, 68, "order details", 7.2, color=GREY)
    b += line("M220 73 L294 73", GREY, 1.4) + f'<polygon points="294,73 286,69 286,77" fill="{GREY}"/>'
    b += text(257, 68, "bill", 7.2, color=GREY)
    b += text(14, 130, "level 1: blow up the one bubble", 9.2, weight="bold", color=P, anchor="start")
    steps = ["1. browse menu", "2. place order", "3. pay", "4. notify kitchen"]
    for i, s in enumerate(steps):
        x = 14 + i * 88
        b += f'<circle cx="{x+34}" cy="176" r="26" fill="{ORANGEF}" stroke="{ORANGE}" stroke-width="1.4"/>'
        w1, w2 = s.split(" ", 1)
        b += text(x + 34, 171, w1, 7.0, weight="bold", color=ORANGE)
        b += text(x + 34, 183, w2, 7.0, weight="bold", color=ORANGE)
        if i < 3:
            b += line(f"M{x+60} 176 L{x+84} 176", GREY, 1.3)
            b += f'<polygon points="{x+84},176 {x+78},172 {x+78},180" fill="{GREY}"/>'
    b += line("M12 158 L60 158", GREY, 0)
    b += line("M34 162 L170 162"[:0], GREY, 0)
    b += line("M34 202 L326 202", RED, 1.4) + line("M34 212 L326 212", RED, 1.4)
    b += text(180, 229, "order store (data store under the pipeline)", 7.6, color=RED)
    b += note(12, 240, 336, ["Numbers stay consistent: bubble 2 splits",
                             "into 2.1/2.2... on level 2. Balancing =",
                             "flows in/out match between levels."], size=9.2)
    return svg(360, 300, b)


def usecase():
    b = title("Use Case Diagram: Food App")
    b += box(96, 44, 220, 168, PF, P, 10, 1.3)
    b += text(206, 60, "system boundary", 7.6, color=GREY)
    ucs = [("browse menu", 84), ("place order", 122), ("pay online", 160), ("track status", 192)]
    for t, yy in ucs:
        b += f'<ellipse cx="206" cy="{yy}" rx="66" ry="14" fill="white" stroke="{P}" stroke-width="1.2"/>'
        b += text(206, yy + 3, t, 7.8, color=P)
    b += stick(48, 96) if False else ""
    b += stickman(46, 116)
    b += text(46, 168, "student", 8.0, weight="bold", color=BLUE)
    b += stickman(46, 208)
    b += text(46, 260, "kitchen", 8.0, weight="bold", color=BLUE)
    for (x1, y1) in [(56, 122), (56, 214)]:
        pass
    b += line("M58 110 L138 88", GREY, 1.1) + line("M58 116 L138 122", GREY, 1.1)
    b += line("M58 122 L138 158", GREY, 1.1)
    b += line("M58 208 L138 196", GREY, 1.1)
    b += note(12, 232, 336, ["Oval = a goal of the actor (a 'case');",
                             "stick figure = role, not a person;",
                             "line = 'this actor can do this'."], size=9.2)
    b += note(12, 268, 336, ["<<include>>: reused sub-case; <<extend>>:",
                             "optional add-on behaviour."], size=9.2)
    return svg(360, 330, b)


def stickman(cx, cy):
    s = f'<circle cx="{cx}" cy="{cy-14}" r="7" fill="{BLUEF}" stroke="{BLUE}" stroke-width="1.4"/>'
    s += line(f"M{cx} {cy-7} L{cx} {cy+12}", BLUE, 1.4)
    s += line(f"M{cx-10} {cy} L{cx+10} {cy}", BLUE, 1.4)
    s += line(f"M{cx} {cy+12} L{cx-8} {cy+26}", BLUE, 1.4) + line(f"M{cx} {cy+12} L{cx+8} {cy+26}", BLUE, 1.4)
    return s


def classd():
    b = title("Class Diagram: Library Slice")
    def cls(x, y, name, attrs, meths, c=BLUE, cf=BLUEF):
        h = 26 + 13 * len(attrs) + 13 * len(meths)
        s = box(x, y, 150, h, "white", c, 4, 1.3)
        s += box(x, y, 150, 24, cf, c, 4, 1.3)
        s += text(x + 75, y + 15, name, 8.8, weight="bold", color=c)
        yy = y + 36
        for a in attrs:
            s += text(x + 8, yy, a, 7.6, anchor="start", color=INK); yy += 13
        s += line(f"M{x} {y + 24 + 13*len(attrs) + 6} L{x+150} {y + 24 + 13*len(attrs) + 6}", c, 1)
        for m in meths:
            s += text(x + 8, yy, m, 7.6, anchor="start", color=GREY); yy += 13
        return s, h
    s1, h1 = cls(14, 48, "Member", ["name", "memberId"], ["borrowBook()", "returnBook()"])
    b += s1
    s2, h2 = cls(196, 48, "Book", ["title", "isbn"], ["reserve()"])
    b += s2
    b += line("M164 84 L196 84", GREY, 1.3)
    b += f'<polygon points="164,84 172,79 172,89" fill="white" stroke="{GREY}" stroke-width="1.2"/>'
    b += text(180, 70, "borrows", 7.2, color=GREY)
    b += text(164, 96, "1..*", 7.2, color=GREY, anchor="start")
    b += text(196, 96, "0..*", 7.2, color=GREY, anchor="end")
    s3, h3 = cls(105, 150, "EBook", ["fileSize"], [], ORANGE, ORANGEF)
    b += s3
    b += line("M180 146 L180 131 L271 131 L271 125", GREY, 1.3)
    b += f'<polygon points="271,113 265,125 277,125" fill="white" stroke="{GREY}" stroke-width="1.2"/>'
    b += note(12, 236, 336, ["Solid line + open diamond = association",
                             "(a Member borrows Books); hollow triangle",
                             "= generalisation (EBook IS-A Book).",
                             "Multiplicity tells how many on each end."], size=9.2)
    return svg(360, 306, b)


def sequenced():
    b = title("Sequence Diagram: Place Order")
    actors = [("student", 46), ("app server", 148), ("payment gw", 250), ("kitchen", 332)]
    for t, x in actors:
        b += rbox(x, 48, 74, 24, t, BLUEF, BLUE, 7.8)
        b += line(f"M{x} 60 L{x} 282", GREY, 1.1, dash="5 3")
    msgs = [(46, 148, "pick items", 92), (148, 250, "charge card", 132),
            (250, 148, "payment OK", 172), (148, 332, "new order", 212),
            (332, 148, "accepted +ETA", 246), (148, 46, "ETA on screen", 272)]
    for x1, x2, t, y in msgs:
        dash = "5 3" if x2 < x1 else None
        b += line(f"M{x1} {y} L{x2} {y}", INK, 1.2, dash=dash)
        hx = x2 if x2 > x1 else x2
        b += f'<polygon points="{x2},{y} {x2 - 7 * (1 if x2 > x1 else -1)},{y-3} {x2 - 7 * (1 if x2 > x1 else -1)},{y+3}" fill="{INK}"/>'
        b += text((x1 + x2) / 2, y - 4, t, 7.2, color=GREY)
    b += note(12, 290, 336, ["Time runs DOWNWARD; lifelines are dashed;",
                             "solid arrows = calls, dashed returns;",
                             "boxes on lifelines = activation bars."], size=9.2)
    return svg(360, 354, b)


def activityd():
    b = title("Activity Diagram: Place Order Flow")
    b += f'<circle cx="180" cy="52" r="7" fill="{INK}"/>'
    b += line("M180 59 L180 72", GREY, 1.3) + f'<polygon points="180,72 176,66 184,66" fill="{GREY}"/>'
    b += rbox(180, 90, 130, 26, "browse menu", GREENF, GREEN, 8.6)
    b += line("M180 103 L180 116", GREY, 1.3) + f'<polygon points="180,116 176,110 184,110" fill="{GREY}"/>'
    b += f'<polygon points="180,122 218,146 180,170 142,146" fill="{YEL}" stroke="{ORANGE}" stroke-width="1.3"/>'
    b += text(180, 150, "pay online?", 7.8, weight="bold", color=ORANGE)
    b += line("M218 146 L262 146", GREY, 1.3) + f'<polygon points="262,146 254,142 254,150" fill="{GREY}"/>'
    b += text(232, 140, "no", 7.6, color=GREY)
    b += rbox(300, 146, 76, 26, "cash COD", BLUEF, BLUE, 8.2)
    b += line("M180 170 L180 186", GREY, 1.3) + f'<polygon points="180,186 176,180 184,180" fill="{GREY}"/>'
    b += text(188, 180, "yes", 7.6, color=GREY, anchor="start")
    b += rbox(180, 204, 130, 26, "gateway payment", GREENF, GREEN, 8.6)
    b += line("M262 154 L262 204 L249 204", GREY, 1.3)
    b += f'<polygon points="249,204 249,200 256,204 249,208" fill="{GREY}"/>'
    b += line("M180 217 L180 234", GREY, 1.3) + f'<polygon points="180,234 176,228 184,228" fill="{GREY}"/>'
    b += rbox(180, 252, 150, 26, "notify kitchen", GREENF, GREEN, 8.6)
    b += line("M180 265 L180 282", GREY, 1.3) + f'<polygon points="180,282 176,276 184,276" fill="{GREY}"/>'
    b += f'<circle cx="180" cy="292" r="7" fill="none" stroke="{INK}" stroke-width="2"/><circle cx="180" cy="292" r="3.4" fill="{INK}"/>'
    b += note(12, 306, 336, ["Black dot starts; ringed dot ends; diamond",
                             "= decision. Fork/join bars (bold lines)",
                             "would split parallel work."], size=9.2)
    return svg(360, 368, b)


def componentd():
    b = title("Component Diagram: Food App Backend")
    b += box(14, 52, 150, 150, BLUEF, BLUE, 6, 1.2)
    b += text(89, 68, "OrderService", 8.8, weight="bold", color=BLUE)
    b += text(141, 58, "«component»", 6.6, color=GREY)
    b += box(24, 82, 86, 20, "white", BLUE, 2, 1.1) + text(67, 96, "order API", 7.2, color=BLUE)
    b += box(24, 110, 86, 20, "white", BLUE, 2, 1.1) + text(67, 124, "menu cache", 7.2, color=BLUE)
    b += box(24, 138, 86, 20, "white", BLUE, 2, 1.1) + text(67, 152, "DB writer", 7.2, color=BLUE)
    b += box(200, 52, 148, 92, GREENF, GREEN, 6, 1.2)
    b += text(274, 68, "PaymentGateway", 8.8, weight="bold", color=GREEN)
    b += text(322, 58, "«component»", 6.6, color=GREY)
    b += box(212, 82, 96, 20, "white", GREEN, 2, 1.1) + text(260, 96, "charge card", 7.2, color=GREEN)
    b += box(200, 158, 148, 44, ORANGEF, ORANGE, 6, 1.2)
    b += text(274, 174, "Notifier", 8.8, weight="bold", color=ORANGE)
    b += text(322, 164, "«component»", 6.6, color=GREY)
    b += f'<circle cx="166" cy="92" r="5" fill="none" stroke="{GREY}" stroke-width="1.4"/>'
    b += line("M164 92 L200 92", GREY, 1.3)
    b += line("M164 180 L200 180", GREY, 1.3)
    b += f'<path d="M196 186 a6 6 0 0 1 0 -12" fill="none" stroke="{GREY}" stroke-width="1.4"/>'
    b += note(12, 224, 336, ["Box = a replaceable unit with its own",
                             "interfaces. Lollipop = PROVIDED interface",
                             "(order API); socket = REQUIRED one -",
                             "components snap together via contracts."], size=9.2)
    return svg(360, 294, b)


DIAGRAM_TITLES = {
    "se2_req_types": ("Functional vs Non-Functional Requirements", req_types),
    "se2_gather": ("Requirement Gathering Techniques", gather),
    "se2_srs": ("SRS: Structure and Qualities", srs),
    "se2_analysis_vs_design": ("Analysis vs Design: WHAT vs HOW", analysis_vs_design),
    "se2_cohesion": ("Cohesion: Best to Worst", cohesion),
    "se2_coupling": ("Coupling: Worst to Best", coupling),
    "se2_dfd_symbols": ("DFD Symbols (Yourdon-DeMarco)", dfd_symbols),
    "se2_dfd_levels": ("DFD Levels: Food Ordering System", dfd_levels),
    "se2_usecase": ("Use Case Diagram: Food App", usecase),
    "se2_class": ("Class Diagram: Library Slice", classd),
    "se2_sequence": ("Sequence Diagram: Place Order", sequenced),
    "se2_activity": ("Activity Diagram: Place Order Flow", activityd),
    "se2_component": ("Component Diagram: Food App Backend", componentd),
}

if __name__ == "__main__":
    import subject_DI04000011 as S
    out = S.DIAG_DIR
    os.makedirs(out, exist_ok=True)
    for k, (t, fn) in DIAGRAM_TITLES.items():
        open(os.path.join(out, k + ".svg"), "w").write(fn())
    print("written", len(DIAGRAM_TITLES))
