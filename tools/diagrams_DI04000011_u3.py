"""DI04000011 Software Engineering - Unit 3 diagrams: estimation, scheduling, risk."""
import os
from flowchart_lib import *
from diagrams_DI03000021_u1 import box, BLUE, BLUEF, GREEN, GREENF, ORANGE, ORANGEF, RED, REDF, YEL, TEAL, TEALF
from diagrams_DI03000011_u1 import note
from diagrams_DI03000031_u1 import lines, rarrow, grid, PF, GREY
from diagrams_DI03000061_u1 import code, OUT


def pm_duties():
    b = title("Software Project Manager: Duties")
    b += rbox(180, 70, 130, 34, "Project\nManager", PF, P, 9.6)
    pts = ["estimate size/cost/time", "plan schedule + tasks", "assign and track work",
           "manage risks + changes", "report to stakeholders", "guard quality gates"]
    for i, t in enumerate(pts):
        x = 12 + (i % 2) * 178
        y = 118 + (i // 2) * 44
        b += box(x, y, 168, 34, BLUEF, BLUE, 6, 1.1)
        b += text(x + 84, y + 20, t, 7.8, color=BLUE)
    b += line("M140 87 L96 116", GREY, 1.1) + line("M220 87 L272 116", GREY, 1.1)
    b += note(12, 262, 336, ["A PM's day is the umbrella activities",
                             "made flesh: estimating (12/13),",
                             "scheduling (14), risk-watching."], size=9.2)
    return svg(360, 316, b)


def loc_fp():
    b = title("LOC vs Function Points")
    b += grid(12, 44, [96, 110, 130], [
        ["aspect", "LOC (code lines)", "Function Points"],
        ["measures", "code volume", "functionality given"],
        ["needs code?", "yes - late", "no - from SRS, early"],
        ["language-indep?", "no", "yes"],
        ["weakness", "padding pays", "subjective weights"],
    ], rh=19, size=8.0)
    b += box(12, 148, 336, 44, TEALF, TEAL, 7, 1.2)
    b += text(180, 165, "exam anchor sentence:", 8.6, weight="bold", color=TEAL)
    b += text(180, 180, "LOC counts bricks; FP counts the house's rooms.", 8.6, color=INK)
    b += note(12, 206, 336, ["FP estimate happens before design starts -",
                             "that is its scheduling superpower."], size=9.2)
    return svg(360, 264, b)


def fp_calc():
    b = title("Function Point Calculation (5 ingredients)")
    b += grid(12, 44, [96, 70, 70, 100], [
        ["component", "simple", "avg", "complex"],
        ["external inputs", "3", "4", "6"],
        ["external outputs", "4", "5", "7"],
        ["user inquiries", "3", "4", "6"],
        ["internal files", "7", "10", "15"],
        ["external files", "5", "7", "10"],
    ], rh=18, size=8.2)
    b += code(14, 170, ["FP = count_total x [0.65 + 0.01 x S Fi]",
                        "   Fi: 14 influence factors (0..5 each)",
                        "   count_total = sum(count x weight)"], 8.6, 15)
    b += box(12, 226, 336, 60, YEL, ORANGE, 7, 1.2)
    b += text(180, 244, "worked mini (avg weights):", 8.4, weight="bold", color=ORANGE)
    b += code(24, 258, ["2 inp + 1 out + 1 inquiry + 1 int file",
                        "= 8 + 5 + 4 + 10 = 27"], 8.2, 13)
    b += note(12, 300, 336, ["Practical 12: count your own project's",
                             "tables/screens/actions into the grid."], size=9.2)
    return svg(360, 356, b)


def cocomo():
    b = title("Basic COCOMO (Boehm, 1981)")
    b += code(14, 48, ["Effort (person-months):  E = a x (KLOC)^b",
                       "Duration (months):        D = c x (E)^d",
                       "People needed:            N = E / D"], 8.6, 16)
    b += grid(12, 108, [128, 208], [
        ["class", "a     b       c     d"],
        ["organic (small, familiar)", "2.4  1.05  2.5  0.38"],
        ["semi-detached (mixed)", "3.0  1.12  2.5  0.35"],
        ["embedded (hard limits)", "3.6  1.20  2.5  0.32"],
    ], rh=20, size=8.2)
    b += box(12, 184, 336, 62, GREENF, GREEN, 7, 1.2)
    b += text(180, 200, "worked: organic app of about 10 KLOC", 8.4, weight="bold", color=GREEN)
    b += code(24, 214, ["E = 2.4 x 10^1.05 ~ 27 person-months",
                        "D = 2.5 x 27^0.38 ~ 8.7 months;  N ~ 3"], 8.2, 13)
    b += note(12, 258, 336, ["Practical 13: basic COCOMO for your",
                             "project; intermediate adds 15 cost-",
                             "drivers, detailed splits per phase."], size=9.2)
    return svg(360, 324, b)


def gantt():
    b = title("Gantt Chart: 8-Week Project Plan")
    tasks = [("requirements", 0, 2, BLUE, BLUEF), ("design", 2, 2, GREEN, GREENF),
             ("coding", 4, 2, ORANGE, ORANGEF), ("testing", 6, 1.5, RED, REDF),
             ("deploy+docs", 7, 1, TEAL, TEALF)]
    b += text(92, 52, "W1  W2  W3  W4  W5  W6  W7  W8", 8.0, mono=True, anchor="start", color=GREY)
    for j in range(9):
        x = 96 + j * 30
        b += line(f"M{x} 58 L{x} 178", "#E5E5E5", 1)
    for i, (t, s, d, c, cf) in enumerate(tasks):
        y = 64 + i * 24
        b += text(88, y + 10, t, 7.6, anchor="end", color=INK)
        x = 96 + s * 30
        b += box(x, y, d * 30, 16, cf, c, 3, 1.1)
    b += line("M96 64 L96 178", GREY, 1.2)
    b += note(12, 192, 336, ["Read: horizontal bars over calendar weeks.",
                             "Overlap means parallel work; a bar's END",
                             "feeds the next bar's start - dependencies",
                             "made visible to the whole team at a glance."], size=9.2)
    return svg(360, 264, b)


def burndown():
    b = title("Sprint Burndown Chart (Agile, Practical 14)")
    b += text(32, 52, "work left", 7.8, anchor="start", color=GREY)
    b += text(180, 262, "days of sprint", 7.8, color=GREY)
    b += line("M56 60 L56 240 M56 240 L316 240", INK, 1.4)
    b += text(52, 66, "40", 7, anchor="end", color=GREY)
    b += text(52, 150, "20", 7, anchor="end", color=GREY)
    b += text(52, 238, "0", 7, anchor="end", color=GREY)
    b += line("M56 64 L316 240", GREY, 1.2, dash="6 3")
    b += text(302, 226, "ideal", 7.4, color=GREY, anchor="end")
    b += f'<path d="M56 64 L110 96 L164 88 L218 150 L272 170 L316 208" fill="none" stroke="{RED}" stroke-width="2"/>'
    b += text(306, 200, "actual", 7.4, color=RED, anchor="start")
    b += note(12, 274, 336, ["Each day the team plots remaining effort;",
                             "above the dashed ideal = behind schedule;",
                             "below = ahead. Reality of one look."], size=9.2)
    return svg(360, 340, b)


def flow_sched():
    b = title("Flow Chart: Building the Schedule")
    steps = [(180, 60, "list all tasks (WBS)"),
             (180, 108, "estimate each task"),
             (180, 156, "find dependencies"),
             (180, 204, "draw Gantt / burndown"),
             (180, 252, "track weekly; re-plan")]
    for cx, cy, t in steps:
        b += rbox(cx, cy, 220, 28, t, BLUEF, BLUE, 8.6)
    for y1, y2 in ((74, 94), (122, 142), (170, 190), (218, 238)):
        b += line(f"M180 {y1} L180 {y2}", GREY, 1.3)
        b += f'<polygon points="180,{y2} 176,{y2-7} 184,{y2-7}" fill="{GREY}"/>'
    b += line("M290 252 L330 252 L330 60 L290 60", GREY, 1.2, dash="6 3")
    b += line("M290 60 L290 60", GREY, 0)
    b += f'<polygon points="290,60 284,68 296,68" fill="{GREY}"/>'
    b += text(330, 160, "loop back", 7.6, color=GREY)
    b += note(12, 278, 336, ["Tracking never ends: every status note",
                             "feeds the plan again. A schedule is a",
                             "prediction ONE ITERATION away from wrong."], size=9.2)
    return svg(360, 340, b)


def risk_cycle():
    b = title("Risk Management Cycle")
    import math as M
    cx, cy = 180, 150
    nodes = [("identify risks", 100), ("assess P x I", 176), ("plan mitigation", 252), ("monitor weekly", 340)]
    for i, (t, angdeg) in enumerate(nodes):
        ang = -M.pi / 2 + 2 * M.pi * i / 4
        x = cx + 116 * M.cos(ang)
        y = cy + 96 * M.sin(ang)
        c = [BLUE, ORANGE, GREEN, RED][i]
        cf = [BLUEF, ORANGEF, GREENF, REDF][i]
        b += rbox(x, y, 100, 30, t, cf, c, 8.2)
    arcs = [(-38, 38), (52, 128), (142, 218), (232, 308)]
    for a1, a2 in arcs:
        pass
    b += f'<path d="M268 100 A140 104 0 0 1 240 210" fill="none" stroke="{GREY}" stroke-width="1.4"/>'
    b += f'<polygon points="240,210 236,202 246,204" fill="{GREY}"/>'
    b += f'<path d="M120 232 A140 104 0 0 1 92 128" fill="none" stroke="{GREY}" stroke-width="1.4"/>'
    b += f'<polygon points="92,128 100,136 88,136" fill="{GREY}"/>'
    b += note(12, 272, 336, ["One pass per week keeps risks current;",
                             "the register holds: risk, P, I, R = P x I,",
                             "owner, mitigation, trigger date."], size=9.2)
    return svg(360, 332, b)


def risk_matrix():
    b = title("Risk Assessment: Probability x Impact Grid")
    b += text(46, 60, "high", 7.8, color=RED, anchor="start")
    b += text(46, 156, "low", 7.8, color=GREEN, anchor="start")
    b += text(180, 250, "impact", 8.2, color=GREY)
    b += text(34, 124, "probability", 8.2, color=GREY, anchor="middle")
    cols = [("WATCH", YEL, GREY), ("PLAN", ORANGEF, ORANGE), ("ACT NOW", REDF, RED)]
    grid_map = [["act", "plan", "plan"], ["plan", "plan", "watch"], ["watch", "watch", "pl"]]
    fills = {"pl": YEL, "plan": ORANGEF, "watch": GREENF, "act": REDF}
    cc = {"pl": "#B8860B", "plan": ORANGE, "watch": GREEN, "act": RED}
    for i, rowv in enumerate(grid_map):
        for j, k in enumerate(rowv):
            x = 56 + (2 - j) * 92
            y = 64 + i * 56
            b += box(x, y, 88, 52, fills[k], cc[k], 5, 1.1)
            t = {"pl": "monitor", "plan": "plan B", "watch": "accept", "act": "MITIGATE"}[k]
            b += text(x + 44, y + 30, t, 8.4, weight="bold", color=cc[k])
    b += text(180, 40, "impact grows  ->  (right = worse)", 7.8, color=GREY)
    b += note(12, 254, 336, ["Score every risk P x I: top-right (high P,",
                             "high I) demands planned mitigation NOW;",
                             "low-low risks are simply accepted."], size=9.2)
    return svg(360, 322, b)


DIAGRAM_TITLES = {
    "se3_pm_duties": ("Software Project Manager: Duties", pm_duties),
    "se3_loc_fp": ("LOC vs Function Points", loc_fp),
    "se3_fp_calc": ("Function Point Calculation (5 ingredients)", fp_calc),
    "se3_cocomo": ("Basic COCOMO", cocomo),
    "se3_gantt": ("Gantt Chart: 8-Week Project Plan", gantt),
    "se3_flow": ("Flow Chart: Building the Schedule", flow_sched),
    "se3_burndown": ("Sprint Burndown Chart", burndown),
    "se3_risk_cycle": ("Risk Management Cycle", risk_cycle),
    "se3_risk_matrix": ("Risk Assessment: Probability x Impact Grid", risk_matrix),
}

if __name__ == "__main__":
    import subject_DI04000011 as S
    out = S.DIAG_DIR
    os.makedirs(out, exist_ok=True)
    for k, (t, fn) in DIAGRAM_TITLES.items():
        open(os.path.join(out, k + ".svg"), "w").write(fn())
    print("written", len(DIAGRAM_TITLES))
