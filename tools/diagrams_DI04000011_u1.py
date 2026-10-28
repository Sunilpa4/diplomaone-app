"""DI04000011 Software Engineering - Unit 1 diagrams: software domains and process models."""
import os
from flowchart_lib import *
from diagrams_DI03000021_u1 import box, BLUE, BLUEF, GREEN, GREENF, ORANGE, ORANGEF, RED, REDF, YEL, TEAL, TEALF
from diagrams_DI03000011_u1 import note
from diagrams_DI03000031_u1 import lines, rarrow, grid, PF, GREY
from diagrams_DI03000061_u1 import code, OUT


def domains():
    b = title("Software Application Domains")
    cells = [
        ("System", "OS, compilers,\ndrivers", BLUE, BLUEF),
        ("Application", "accounts, ERP,\nword tools", GREEN, GREENF),
        ("Embedded", "firmware in devices:\nABS, microwaves", ORANGE, ORANGEF),
        ("Web", "sites + web apps,\ncloud backends", P, PF),
        ("AI based", "predict, recognise,\nrecommend", RED, REDF),
        ("Green Hydrogen", "production + supply\ncontrol software", TEAL, TEALF),
    ]
    for i, (t, d, c, cf) in enumerate(cells):
        x = 12 + (i % 2) * 176
        y = 46 + (i // 2) * 64
        b += box(x, y, 160, 56, cf, c, 8, 1.3)
        b += text(x + 80, y + 18, t, 9.6, weight="bold", color=c)
        for j, ln in enumerate(d.split("\n")):
            b += text(x + 80, y + 34 + j * 12, ln, 8.0, color=GREY)
    b += note(12, 248, 336, ["Same discipline, very different stakes:",
                             "an embedded crash could brake a car, a",
                             "web bug costs a shopping cart."], size=9.2)
    return svg(360, 298, b)


def layers():
    b = title("Software Engineering: A Layered Approach")
    cols = [(BLUE, BLUEF, "TOOLS", "editors, IDEs, testing\nframeworks, CI pipelines"),
            (GREEN, GREENF, "METHODS", "how-to: analysis, design,\ncoding + testing practices"),
            (ORANGE, ORANGEF, "PROCESS", "the scaffold: activities,\nmilestones, quality gates"),
            (RED, REDF, "QUALITY FOCUS", "the bedrock - every layer\nserves quality")]
    for i, (c, cf, t, d) in enumerate(cols):
        y = 46 + i * 56
        b += box(24, y, 312, 48, cf, c, 8, 1.3)
        b += text(180, y + 18, t, 10, weight="bold", color=c)
        for j, ln in enumerate(d.split("\n")):
            b += text(180, y + 33 + j * 11, ln, 8.0, color=GREY)
    b += note(12, 276, 336, ["Read top-down: tools AUTOMATE methods;",
                             "methods support the process; the process",
                             "keeps quality on schedule."], size=9.2)
    return svg(360, 326, b)


def framework():
    b = title("Generic Process Model")
    acts = ["Communication", "Planning", "Modeling", "Construction", "Deployment"]
    for i, a in enumerate(acts):
        x = 10 + i * 70
        b += rbox(x + 34, 74, 64, 30, a, PF, P, 7.8)
        if i < 4:
            b += rarrow(x + 68, x + 74, 89, GREY)
    b += text(180, 42, "five framework activities - EVERY project, any model", 8.4, color=GREY)
    b += box(10, 122, 340, 64, TEALF, TEAL, 8, 1.3)
    b += text(180, 140, "UMBRELLA ACTIVITIES (run all along)", 9.0, weight="bold", color=TEAL)
    b += text(180, 156, "progress tracking  |  risk management", 8.4, color=INK)
    b += text(180, 170, "quality assurance  |  change & review mgmt", 8.4, color=INK)
    b += grid(12, 200, [110, 226], [
        ["activity", "what it means"],
        ["communication", "gather what users actually need"],
        ["planning", "scope, cost, schedule, risks"],
        ["modeling", "analysis + design sketches of solution"],
        ["construction", "code and test it"],
        ["deployment", "deliver, train, support"],
    ], rh=19, size=8.2)
    b += note(12, 320, 336, ["Every process model (waterfall, spiral,",
                             "Scrum...) just SERIALISES these same five",
                             "differently."], size=9.2)
    return svg(360, 396, b)


def waterfall():
    b = title("Waterfall Model (1970)")
    steps = ["Requirements", "Design", "Implement", "Testing", "Deployment", "Maintenance"]
    for i, s in enumerate(steps):
        x = 8 + i * 48
        y = 52 + i * 30
        b += box(x, y, 86, 26, BLUEF, BLUE, 6, 1.2)
        b += text(x + 43, y + 16, s, 8.0, weight="bold", color=BLUE)
        if i < 5:
            b += line(f"M{x+43} {y+26} L{x+54} {y+30}", GREY, 1.3)
            b += f'<polygon points="{x+54},{y+30} {x+46},{y+25} {x+52},{y+21}" fill="{GREY}"/>'
    b += grid(12, 236, [150, 186], [
        ["strength", "weakness"],
        ["documents each phase fully", "working software comes LATE"],
        ["easy for fixed, known scope", "requirements rarely stand still"],
        ["milestones crystal clear", "returning upstream is painful"],
    ], rh=19, size=8.2)
    b += note(12, 316, 336, ["Use when requirements are stable and",
                             "well understood - like a college",
                             "attendance register upgrade."], size=9.2)
    return svg(360, 386, b)


def incremental():
    b = title("Incremental Model: Deliver in Slices")
    b += text(12, 52, "core product v1 ", 8.2, anchor="start", color=GREY)
    b += text(12, 96, "increment 2 ", 8.2, anchor="start", color=GREY)
    b += text(12, 140, "increment 3 ", 8.2, anchor="start", color=GREY)
    for i in range(3):
        y = 60 + i * 44
        for j, (t, c, cf) in enumerate([("req", BLUE, BLUEF), ("design", GREEN, GREENF),
                                        ("code", ORANGE, ORANGEF), ("test", RED, REDF)]):
            x = 96 + j * 62
            b += box(x, y, 56, 22, cf, c, 5, 1.1)
            b += text(x + 28, y + 14, t, 8.0, weight="bold", color=c)
    b += rarrow(344, 420, 71, GREY) if False else ""
    b += f'<path d="M348 71 L356 71" stroke="{GREY}" stroke-width="1.4"/><polygon points="356,71 349,67 349,75" fill="{GREY}"/>'
    for yv in (115, 159):
        b += f'<path d="M348 {yv} L356 {yv}" stroke="{GREY}" stroke-width="1.4"/><polygon points="356,{yv} 349,{yv-4} 349,{yv+4}" fill="{GREY}"/>'
    b += text(180, 214, "each slice = a mini-waterfall", 8.6, weight="bold", color=P)
    b += note(12, 228, 336, ["v1 ships the CORE; later increments add",
                             "features. Customers touch real software",
                             "early - feedback arrives while there is",
                             "still time to react."], size=9.2)
    return svg(360, 298, b)


def prototype():
    b = title("Prototyping Model: Learn by Showing")
    steps = [(180, 60, "requirements\nlisten (roughly)", BLUE, BLUEF),
             (180, 116, "quick design", GREEN, GREENF),
             (180, 172, "build prototype", ORANGE, ORANGEF),
             (180, 228, "customer evaluates", RED, REDF)]
    for cx, cy, t, c, cf in steps:
        b += rbox(cx, cy, 150, 30, t.split("\n")[0], cf, c, 9.0)
    for y1, y2 in ((75, 101), (131, 157), (187, 213)):
        b += line(f"M180 {y1} L180 {y2}", GREY, 1.4)
        b += f'<polygon points="180,{y2} 176,{y2-8} 184,{y2-8}" fill="{GREY}"/>'
    b += line("M255 228 L330 228 L330 60 L255 60", GREY, 1.4, dash="6 3")
    b += f'<polygon points="255,60 262,63 262,57" fill="{GREY}"/>'
    b += text(330, 148, "refine + repeat", 8.2, color=GREY)
    b += line("M180 243 L180 258", GREY, 1.4)
    b += f'<polygon points="180,258 176,250 184,250" fill="{GREY}"/>'
    b += rbox(180, 276, 190, 30, "final system (full build)", TEALF, TEAL, 8.8)
    b += note(12, 302, 336, ["Best when users 'know it when they see",
                             "it': the throwaway mock exposes hidden",
                             "requirements cheaply, before real code."], size=9.2)
    return svg(360, 350, b)


def spiral():
    b = title("Spiral Model: Risk-first Cycles")
    import math as M
    cx, cy = 180, 158
    for i, r in enumerate((30, 58, 86, 114)):
        c = [BLUE, GREEN, ORANGE, RED][i]
        b += f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{c}" stroke-width="1.6"/>'
    quads = [(cx, cy - 98, "Planning", BLUE), (cx + 88, cy, "Risk analysis", RED),
             (cx, cy + 122, "Engineering", GREEN), (cx - 88, cy, "Evaluation", ORANGE)]
    for x, y, t, c in quads:
        b += text(x, y, t, 9.0, weight="bold", color=c)
    b += text(cx, cy + 4, "start", 8.6, weight="bold", color=GREY)
    b += line(f"M{cx} {cy} L{cx} {cy - 26}", INK, 1.4)
    b += f'<polygon points="{cx},{cy-26} {cx-4},{cy-18} {cx+4},{cy-18}" fill="{INK}"/>'
    b += note(12, 292, 336, ["Each loop = one phase: plan it, analyse",
                             "RISKS, build a bit, review with the",
                             "customer, loop again. Big projects love",
                             "it; small ones find it heavy."], size=9.0)
    return svg(360, 356, b)


def vmodel():
    b = title("V-Model: Every Build Step Pairs a Test")
    left = [("requirements", 60), ("system design", 108), ("module design", 156), ("CODING", 204)]
    right = [("acceptance test", 60), ("system test", 108), ("integration test", 156)]
    for i, (t, y) in enumerate(left):
        x = 90 - i * 0  # vertical, left side descends
        x = 20 + i * 30
        w = 104
        b += box(x, y - 14, w, 26, BLUEF, BLUE, 6, 1.2)
        b += text(x + w / 2, y + 3, t, 8.4, weight="bold", color=BLUE)
        if i < 3:
            b += line(f"M{x+w} {y+6} L{x+30+w} {y+30}", GREY, 1.2)
            b += f'<polygon points="{x+30+w},{y+30} {x+24+w},{y+25} {x+30+w},{y+22}" fill="{GREY}"/>'
    for i, (t, y) in enumerate(right):
        x = 272 - i * 30
        b += box(x, y - 14, 104, 26, GREENF, GREEN, 6, 1.2)
        b += text(x + 52, y + 3, t, 8.4, weight="bold", color=GREEN)
    for i in range(3):
        y = 60 + i * 48
        x1 = 20 + i * 30 + 104
        x2 = 272 - i * 30
        b += line(f"M{x1} {y} L{x2} {y}", RED, 1.2, dash="5 3")
    b += text(180, 236, "each left step writes its test PLAN", 8.2, color=RED)
    b += note(12, 250, 336, ["Testing is PLANNED opposite its build",
                             "stage: acceptance test cases are written",
                             "from requirements, long before code.",
                             "Favoured where verification is audited."], size=9.0)
    return svg(360, 316, b)


def agile_values():
    b = title("Agile Manifesto: The Four Values")
    rows = [("working SOFTWARE", "over full documentation"),
            ("responding to CHANGE", "over following the plan"),
            ("INDIVIDUALS + interactions", "over processes and tools"),
            ("CUSTOMER collaboration", "over contract negotiation")]
    for i, (l, r) in enumerate(rows):
        y = 48 + i * 40
        b += box(12, y, 158, 32, GREENF, GREEN, 7, 1.2)
        b += text(91, y + 20, l, 7.8, weight="bold", color=GREEN)
        b += box(190, y, 158, 32, PF, P, 7, 1.2)
        b += text(269, y + 20, r, 7.4, color=P)
        b += text(180, y + 20, ">", 11, weight="bold", color=GREY)
    b += text(180, 224, "the right sides are still valued - the left more", 8.2, color=GREY)
    b += note(12, 240, 336, ["12 principles behind it - the heart three:",
                             "satisfy the customer with EARLY, continuous",
                             "delivery; welcome change; deliver working",
                             "software every few WEEKS."], size=9.2)
    return svg(360, 306, b)


def scrum():
    b = title("Scrum Framework")
    pts = [(64, 66, "product\nbacklog", BLUE, BLUEF), (186, 66, "sprint\nbacklog", GREEN, GREENF),
           (300, 66, "sprint\n2-4 weeks", ORANGE, ORANGEF), (300, 178, "ship-able\nincrement", RED, REDF)]
    for cx, cy, t, c, cf in pts:
        b += rbox(cx, cy, 96, 34, t.split("\n")[0], cf, c, 9.0)
        b += text(cx, cy + 28, t.split("\n")[1], 7.6, color=GREY)
    b += rarrow(112, 138, 66, GREY)
    b += rarrow(234, 252, 66, GREY)
    b += line("M300 83 L300 161", GREY, 1.4)
    b += f'<polygon points="300,161 296,153 304,153" fill="{GREY}"/>'
    b += line("M252 178 L64 178 L64 83", GREY, 1.4, dash="6 3")
    b += f'<polygon points="64,83 60,91 68,91" fill="{GREY}"/>'
    b += text(150, 172, "review + retrospective feed the backlog", 7.6, color=GREY)
    b += box(226, 108, 148, 40, YEL, ORANGE, 7, 1.2)
    b += text(300, 124, "inside a sprint:", 7.8, weight="bold", color=ORANGE)
    b += text(300, 138, "daily 15-min stand-up", 7.8, color=INK)
    b += note(12, 210, 336, ["Roles: Product Owner (what), Scrum Master",
                             "(clears obstacles), Developers (how).",
                             "A sprint is timeboxed - scope slips,",
                             "the deadline does not."], size=9.2)
    return svg(360, 276, b)


def xp():
    b = title("Extreme Programming (XP)")
    cx, cy = 180, 160
    b += f'<circle cx="{cx}" cy="{cy}" r="34" fill="{PF}" stroke="{P}" stroke-width="1.5"/>'
    b += text(cx, cy, "XP", 13, weight="bold", color=P)
    pract = ["pair programming", "test-driven dev", "continuous integration",
             "refactoring", "small releases", "simple design"]
    import math as M
    for i, t in enumerate(pract):
        ang = -M.pi / 2 + i * M.pi / 3
        x = cx + 118 * M.cos(ang)
        y = cy + 106 * M.sin(ang)
        b += box(x - 62, y - 13, 124, 26, GREENF, GREEN, 6, 1.1)
        b += text(x, y + 4, t, 8.2, weight="bold", color=GREEN)
        b += line(f"M{cx + 40 * M.cos(ang)} {cy + 40 * M.sin(ang)} L{x - 70 * M.cos(ang)} {y - 20 * M.sin(ang)}", GREY, 1.1)
    b += note(12, 306, 336, ["XP pushes good practice to '11':",
                             "if tests help, write them FIRST; if reviews",
                             "help, review constantly (pair programming);",
                             "if design matters, improve it daily (refactor)."], size=9.0)
    return svg(360, 380, b)


DIAGRAM_TITLES = {
    "se1_domains": ("Software Application Domains", domains),
    "se1_layers": ("Software Engineering: A Layered Approach", layers),
    "se1_framework": ("Generic Process Model", framework),
    "se1_waterfall": ("Waterfall Model", waterfall),
    "se1_incremental": ("Incremental Model", incremental),
    "se1_prototype": ("Prototyping Model", prototype),
    "se1_spiral": ("Spiral Model", spiral),
    "se1_vmodel": ("V-Model", vmodel),
    "se1_agile": ("Agile Manifesto: The Four Values", agile_values),
    "se1_scrum": ("Scrum Framework", scrum),
    "se1_xp": ("Extreme Programming (XP) Practices", xp),
}

if __name__ == "__main__":
    import subject_DI04000011 as S
    out = S.DIAG_DIR
    os.makedirs(out, exist_ok=True)
    for k, (t, fn) in DIAGRAM_TITLES.items():
        open(os.path.join(out, k + ".svg"), "w").write(fn())
    print("written", len(DIAGRAM_TITLES))
