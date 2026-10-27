"""DI03000041 Fundamentals of Operating System - Unit 2 diagrams: process, states, PCB, scheduling (Gantt charts), schedulers,
queues, context switch, synchronisation, deadlock and RAG."""
import math, os
from flowchart_lib import *
from diagrams_DI03000021_u1 import box, BLUE, BLUEF, GREEN, GREENF, ORANGE, ORANGEF, RED, REDF, TEAL, TEALF
from diagrams_DI03000011_u1 import note
from diagrams_DI03000041_u1 import lines, card, GREY
import os_sched as S

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "content", "computer", "sem3", "DI03000041", "diagrams")
PF = "#F1E8FC"
PAL = {"P0": (GREENF, GREEN), "P1": (BLUEF, BLUE), "P2": (ORANGEF, ORANGE), "P3": (REDF, RED), "P4": (TEALF, TEAL), "P5": (PF, P)}
PA = S.P(["P0", "P1", "P2", "P3"], [0, 1, 2, 3], [5, 3, 8, 6])          # Practical 2(a)


def curve(x1, y1, cx, cy, x2, y2, c=INK, w=1.5):
    ang = math.degrees(math.atan2(y2 - cy, x2 - cx))
    return line(f"M{x1} {y1} Q{cx} {cy} {x2} {y2}", c, w) + arrowhead(x2, y2, ang, 7, c)


def ell(cx, cy, w, h, label, f, s, size=10.5):
    return (f'<ellipse cx="{cx}" cy="{cy}" rx="{w / 2}" ry="{h / 2}" fill="{f}" stroke="{s}" stroke-width="1.7"/>'
            + text(cx, cy, label, size, weight="bold", color=s))


# ------------------------------------------------------------------ RAG helpers
def pnode(x, y, n, r=15):
    return f'<circle cx="{x}" cy="{y}" r="{r}" fill="{BLUEF}" stroke="{BLUE}" stroke-width="1.6"/>' + text(x, y, n, 9.6, weight="bold", color=BLUE)


def rnode(x, y, n, k=1, w=38, h=26, side="t"):
    b = box(x - w / 2, y - h / 2, w, h, ORANGEF, ORANGE, 3, 1.6)
    for i in range(k):
        dx = (i - (k - 1) / 2) * 10
        b += f'<circle cx="{x + dx}" cy="{y + 3}" r="2.6" fill="{ORANGE}"/>'
    if side == "t":
        return b + text(x, y - h / 2 - 7, n, 9.4, weight="bold", color=ORANGE)
    sx = -1 if side == "l" else 1
    return b + text(x + sx * (w / 2 + 4), y, n, 9.4, weight="bold", color=ORANGE, anchor="end" if sx < 0 else "start")


def edge(a, b, c=INK, r=15, w=38, h=26):
    """a, b = (x, y, kind) with kind 'p' (circle) or 'r' (rect). Arrow from a to b clipped at both shapes."""
    (x1, y1, k1), (x2, y2, k2) = a, b
    dx, dy = x2 - x1, y2 - y1
    L = math.hypot(dx, dy); ux, uy = dx / L, dy / L

    def clip(kind):
        if kind == "p":
            return r + 1
        return min((w / 2) / abs(ux) if ux else 1e9, (h / 2) / abs(uy) if uy else 1e9) + 1
    sx, sy = x1 + ux * clip(k1), y1 + uy * clip(k1)
    ex, ey = x2 - ux * clip(k2), y2 - uy * clip(k2)
    return arr([(round(sx, 1), round(sy, 1)), (round(ex, 1), round(ey, 1))], c)


# ------------------------------------------------------------------ 2.1
def memory():
    b = title("Process in Memory")
    secs = [("Stack", "function calls, local variables,", "return addresses", BLUEF, BLUE, 44),
            ("free", "", "", "#FFFFFF", "#BBB", 56),
            ("Heap", "memory allocated at run time", "(malloc / new)", ORANGEF, ORANGE, 40),
            ("Data", "global and static variables", "", GREENF, GREEN, 36),
            ("Text (code)", "program instructions", "", PF, P, 36)]
    y = 40
    b += text(30, y - 2, "max", 8.6, color=GREY, anchor="end")
    for nm, d1, d2, f, s, h in secs:
        b += box(36, y, 104, h, f, s, 0, 1.4) + text(88, y + h / 2, nm, 10.5, weight="bold", color=s)
        if d1:
            b += text(152, y + h / 2 - (6 if d2 else 0), d1, 9.2, anchor="start") + (text(152, y + h / 2 + 7, d2, 9.2, anchor="start") if d2 else "")
        if nm == "free":
            b += arr([(88, y + 4), (88, y + 18)], BLUE) + arr([(88, y + h - 4), (88, y + h - 18)], ORANGE)
            b += text(152, y + h / 2, "stack and heap grow", 9.2, anchor="start", color=GREY)
        y += h
    b += text(30, y, "0", 8.6, color=GREY, anchor="end")
    b += note(12, y + 14, 336, ["Program = passive entity (file on disk).", "Process = program in execution (active entity).",
                                "A process also has a program counter, registers", "and a PCB kept by the OS."], size=9.6)
    return svg(360, y + 86, b)


def states():
    b = title("Process State Diagram (5 States)")
    N, R, U, W, Tm = (52, 58), (88, 150), (272, 150), (180, 246), (308, 58)
    b += ell(*N, 76, 32, "New", GREENF, GREEN) + ell(*Tm, 92, 32, "Terminated", REDF, RED, 10)
    b += ell(*R, 80, 34, "Ready", BLUEF, BLUE) + ell(*U, 84, 34, "Running", PF, P) + ell(*W, 84, 34, "Waiting", ORANGEF, ORANGE)
    b += arr([(62, 74), (80, 133)]) + text(40, 104, "admitted", 9, color=GREEN, weight="bold", anchor="start")
    b += curve(120, 136, 180, 106, 236, 136, P) + text(180, 108, "scheduler dispatch", 9, color=P, weight="bold")
    b += curve(236, 164, 180, 194, 124, 164, BLUE) + text(180, 190, "interrupt (time up)", 9, color=BLUE, weight="bold")
    b += arr([(284, 133), (300, 75)], RED) + text(300, 106, "exit", 9, color=RED, weight="bold", anchor="start")
    b += arr([(268, 168), (212, 232)], ORANGE) + text(258, 216, "I/O or event", 9, color=ORANGE, weight="bold", anchor="start")
    b += text(258, 228, "wait", 9, color=ORANGE, weight="bold", anchor="start")
    b += arr([(148, 232), (94, 168)], GREEN) + text(18, 214, "I/O or event", 9, color=GREEN, weight="bold", anchor="start")
    b += text(18, 226, "completion", 9, color=GREEN, weight="bold", anchor="start")
    b += note(12, 274, 336, ["New: being created.  Ready: waiting for the CPU.", "Running: instructions are executing.",
                             "Waiting: waiting for I/O or an event.", "Terminated: finished execution."], size=9.6)
    return svg(360, 346, b)


def pcb():
    b = title("Process Control Block (PCB)")
    rows = [("Pointer  |  Process state", "link in a queue; new, ready, running…"), ("Process ID (PID)", "unique number of the process"),
            ("Program counter", "address of the next instruction"), ("CPU registers", "accumulator, index, stack pointer…"),
            ("CPU-scheduling info", "priority, pointers to queues"), ("Memory-management info", "base/limit registers, page table"),
            ("Accounting info", "CPU time used, time limits"), ("I/O status info", "devices allocated, open files")]
    y = 36
    for i, (a, d) in enumerate(rows):
        f = PF if i % 2 == 0 else "#FBF8FF"
        b += box(40, y, 280, 36, f, P, 0, 1.3) + text(180, y + 12, a, 10.5, weight="bold", color=P) + text(180, y + 26, d, 8.8, color=GREY)
        y += 36
    b += note(12, y + 12, 336, ["PCB (task control block) stores all information", "about one process. The OS keeps one PCB per process;",
                                "it is saved and reloaded during a context switch."], size=9.6)
    return svg(360, y + 70, b)


# ------------------------------------------------------------------ 2.2 scheduling
def times():
    b = title("Scheduling Times of a Process")
    x0, sc, y = 30, 30, 70
    b += line(f"M{x0} {y} L{x0 + 10 * sc} {y}", INK, 1.3) + arrowhead(x0 + 10 * sc + 4, y, 0, 7, INK)
    for t in range(0, 11):
        b += line(f"M{x0 + t * sc} {y} L{x0 + t * sc} {y + 4}", INK, 1) + text(x0 + t * sc, y + 13, str(t), 8.6, color=GREY)
    b += box(x0 + 2 * sc, y - 22, 3 * sc, 18, "#fff", ORANGE, 2, 1.3) + text(x0 + 3.5 * sc, y - 13, "waiting", 8.8, color=ORANGE, weight="bold")
    b += box(x0 + 5 * sc, y - 22, 4 * sc, 18, P, P, 2, 1.3) + text(x0 + 7 * sc, y - 13, "running on CPU", 8.8, color="#fff", weight="bold")
    for t, lab_, c in [(2, "arrival (AT=2)", GREEN), (9, "completion (CT=9)", RED)]:
        b += line(f"M{x0 + t * sc} {y - 34} L{x0 + t * sc} {y}", c, 1.6, "3 2") + text(x0 + t * sc, y - 40, lab_, 9, color=c, weight="bold")

    def brace(a, e, yy, lab_, c):
        return (line(f"M{x0 + a * sc} {yy} L{x0 + e * sc} {yy}", c, 1.4) + line(f"M{x0 + a * sc} {yy - 4} L{x0 + a * sc} {yy + 4}", c, 1.4)
                + line(f"M{x0 + e * sc} {yy - 4} L{x0 + e * sc} {yy + 4}", c, 1.4) + text(x0 + (a + e) / 2 * sc, yy + 11, lab_, 9, color=c, weight="bold"))
    b += brace(2, 5, y + 28, "WT = 3", ORANGE) + brace(5, 9, y + 28, "BT = 4", P) + brace(2, 9, y + 54, "TAT = CT − AT = 9 − 2 = 7", BLUE)
    b += note(12, y + 82, 336, ["TAT (turnaround time) = CT − AT", "WT (waiting time) = TAT − BT = 7 − 4 = 3",
                                "RT (response time) = first CPU start − AT = 5 − 2 = 3"], size=9.8)
    return svg(360, y + 140, b)


def gantt_card(ttl, procs, segs, res, extra=None, pr=False):
    b = title(ttl)
    cols = ["Process", "AT", "BT"] + (["Priority"] if pr else []) + ["CT", "TAT", "WT"]
    cw = 336 / len(cols)
    y = 32
    for i, c in enumerate(cols):
        b += box(12 + i * cw, y, cw, 20, PF, P, 0, 1) + text(12 + (i + .5) * cw, y + 10, c, 9.4, weight="bold", color=P)
    for r, p in enumerate(procs):
        yy = y + 20 + r * 18
        rr = res[p["n"]]
        vals = [p["n"], p["at"], p["bt"]] + ([p["pr"]] if pr else []) + [rr["ct"], rr["tat"], rr["wt"]]
        for i, v in enumerate(vals):
            b += box(12 + i * cw, yy, cw, 18, "#fff", "#D9C8F0", 0, 1) + text(12 + (i + .5) * cw, yy + 9, str(v), 9.4, weight="bold" if i == 0 else "normal")
    y = y + 20 + len(procs) * 18 + 22
    b += text(180, y, "Gantt chart" + (f" ({extra})" if extra else ""), 10, weight="bold", color=GREY)
    b += S.gantt_svg_body(segs, 16, y + 10, 328, 30, PAL, 9.6 if len(segs) < 10 else 8.6)
    y += 74
    b += text(180, y, f"Average TAT = {S.fmt(S.avg(res, 'tat'))}  |  Average WT = {S.fmt(S.avg(res, 'wt'))}", 10.5, weight="bold", color=P)
    return svg(360, y + 14, b)


def fcfs_d():
    s, r = S.fcfs(PA)
    return gantt_card("FCFS Scheduling (Practical 2a)", PA, s, r)


def sjf_d():
    s, r = S.sjf(PA)
    return gantt_card("SJF (Non-preemptive) Scheduling", PA, s, r)


def rr_d():
    s, r = S.rr(PA, 2)
    return gantt_card("Round Robin Scheduling", PA, s, r, "time quantum = 2")


PRI = S.P(["P1", "P2", "P3", "P4", "P5"], [0] * 5, [10, 1, 2, 1, 5], [3, 1, 4, 5, 2])


def priority_d():
    s, r = S.priority(PRI)
    pal = dict(zip(["P1", "P2", "P3", "P4", "P5"], [PAL[k] for k in ["P1", "P2", "P3", "P0", "P4"]]))
    global PAL
    old, PAL = PAL, pal
    try:
        return gantt_card("Non-preemptive Priority Scheduling", PRI, s, r, "smaller number = higher priority", pr=True)
    finally:
        PAL = old


# ------------------------------------------------------------------ 2.3 schedulers
def queues():
    b = title("Queueing Diagram of Process Scheduling")
    y0 = 50
    b += text(16, y0 - 18, "ready queue", 9.4, anchor="start", color=BLUE, weight="bold")
    for i in range(5):
        b += box(30 + i * 26, y0 - 13, 26, 26, BLUEF, BLUE, 0, 1.2)
    b += arr([(160, y0), (212, y0)])
    b += f'<circle cx="236" cy="{y0}" r="22" fill="{PF}" stroke="{P}" stroke-width="1.8"/>' + text(236, y0, "CPU", 11, weight="bold", color=P)
    b += arr([(258, y0), (340, y0)]) + text(318, y0 - 10, "exit", 9, color=RED, weight="bold")
    rows = [("I/O request", "I/O queue → I/O"), ("time slice expired", None), ("fork a child", "child executes"), ("wait for an interrupt", "interrupt occurs")]
    bus_r, bus_l = 290, 14
    b += line(f"M{bus_r} {y0} L{bus_r} {y0 + 50 + 3 * 46}", INK, 1.4)
    for k, (ev, wt) in enumerate(rows):
        y = y0 + 50 + k * 46
        if wt:
            b += rbox(226, y, 116, 28, ev, ORANGEF, ORANGE, 9) + rbox(92, y, 112, 28, wt, GREENF, GREEN, 9)
            b += arr([(bus_r, y), (284, y)]) + arr([(168, y), (148, y)]) + line(f"M36 {y} L{bus_l} {y}", INK, 1.4)
        else:
            b += line(f"M{bus_r} {y} L{bus_l} {y}", INK, 1.4) + text(170, y - 8, ev, 9.2, color=BLUE, weight="bold")
    b += line(f"M{bus_l} {y0 + 50 + 3 * 46} L{bus_l} {y0}", INK, 1.4) + arr([(bus_l, y0), (30, y0)])
    y = y0 + 50 + 3 * 46 + 24
    b += note(12, y, 336, ["New processes enter the job queue and then the ready", "queue. A running process may leave the CPU for I/O,",
                           "time-out, a child or an interrupt, and then comes", "back to the ready queue until it exits."], size=9.6)
    return svg(360, y + 72, b)


def schedulers():
    b = title("Long, Short and Medium Term Schedulers")
    y = 70
    b += rbox(62, y, 96, 46, "", "#F7F7F7", "#888") + lines(62, y - 7, ["Job pool", "(new jobs, disk)"], 9.4, lh=14, weight="bold", color="#555")
    b += rbox(196, y, 92, 46, "", BLUEF, BLUE) + lines(196, y - 7, ["Ready queue", "(memory)"], 9.4, lh=14, weight="bold", color=BLUE)
    b += f'<circle cx="310" cy="{y}" r="24" fill="{PF}" stroke="{P}" stroke-width="1.8"/>' + text(310, y, "CPU", 11, weight="bold", color=P)
    b += arr([(110, y), (150, y)], GREEN) + text(130, y - 30, "LTS", 10, color=GREEN, weight="bold")
    b += arr([(242, y), (286, y)], RED) + text(264, y - 30, "STS", 10, color=RED, weight="bold")
    b += arr([(310, y + 24), (310, y + 44)]) + text(318, y + 40, "end", 9, anchor="start", color=GREY)
    b += rbox(196, y + 100, 172, 40, "", ORANGEF, ORANGE) + lines(196, y + 93, ["Swapped-out (partially", "executed) processes, disk"], 9.2, lh=14, weight="bold", color=ORANGE)
    b += arr([(180, y + 23), (180, y + 80)], ORANGE) + arr([(212, y + 80), (212, y + 23)], ORANGE)
    b += text(176, y + 52, "swap out", 8.8, anchor="end", color=ORANGE, weight="bold") + text(216, y + 52, "swap in", 8.8, anchor="start", color=ORANGE, weight="bold")
    b += text(300, y + 100, "MTS", 10, color=ORANGE, weight="bold")
    y2 = y + 136
    rows = [("LTS", "Long-term (job) scheduler: job pool → ready queue.", "Controls the degree of multiprogramming. Slow.", GREEN),
            ("STS", "Short-term (CPU) scheduler: ready queue → CPU.", "Runs very often (every few ms). Fastest.", RED),
            ("MTS", "Medium-term scheduler: swaps processes out/in.", "Reduces the degree of multiprogramming.", ORANGE)]
    for i, (k, l1, l2, c) in enumerate(rows):
        yy = y2 + i * 44
        b += box(12, yy, 336, 40, "#FFFFFF", c, 6, 1.3) + text(20, yy + 13, l1, 9.4, anchor="start", weight="bold", color=c)
        b += text(20, yy + 28, l2, 9.2, anchor="start")
    return svg(360, y2 + 3 * 44 + 6, b)


def context():
    b = title("Context Switch between Two Processes")
    X0, XO, X1 = 50, 180, 310
    b += text(X0, 40, "Process P0", 10.5, weight="bold", color=GREEN) + text(XO, 40, "Operating system", 10.5, weight="bold", color=P)
    b += text(X1, 40, "Process P1", 10.5, weight="bold", color=BLUE)

    def bar(x, y1, y2, run, c):
        return line(f"M{x} {y1} L{x} {y2}", c if run else "#BBB", 6 if run else 1.5, None if run else "4 3")
    b += bar(X0, 52, 100, True, GREEN) + text(X0 + 8, 76, "executing", 8.6, anchor="start", color=GREEN)
    b += bar(X0, 100, 300, False, GREEN) + text(X0 + 8, 200, "idle", 8.6, anchor="start", color=GREY)
    b += bar(X0, 300, 344, True, GREEN) + text(X0 + 8, 322, "executing", 8.6, anchor="start", color=GREEN)
    b += bar(X1, 52, 176, False, BLUE) + text(X1 - 8, 110, "idle", 8.6, anchor="end", color=GREY)
    b += bar(X1, 176, 224, True, BLUE) + text(X1 - 8, 200, "executing", 8.6, anchor="end", color=BLUE)
    b += bar(X1, 224, 344, False, BLUE) + text(X1 - 8, 290, "idle", 8.6, anchor="end", color=GREY)
    b += rbox(XO, 120, 130, 24, "save state into PCB0", PF, P, 9.2) + rbox(XO, 156, 130, 24, "reload state from PCB1", PF, P, 9.2)
    b += rbox(XO, 244, 130, 24, "save state into PCB1", PF, P, 9.2) + rbox(XO, 280, 130, 24, "reload state from PCB0", PF, P, 9.2)
    b += arr([(X0 + 4, 100), (XO - 66, 116)], RED) + text(XO, 100, "interrupt or system call", 8.6, color=RED, weight="bold")
    b += arr([(XO + 66, 160), (X1 - 4, 176)], INK)
    b += arr([(X1 - 4, 224), (XO + 66, 240)], RED) + text(XO, 224, "interrupt or system call", 8.6, color=RED, weight="bold")
    b += arr([(XO - 66, 284), (X0 + 4, 300)], INK)
    b += line(f"M{XO - 74} 108 L{XO - 80} 108 L{XO - 80} 168 L{XO - 74} 168", ORANGE, 1.3) + text(XO - 84, 138, "overhead", 8.4, anchor="end", color=ORANGE, weight="bold")
    b += note(12, 356, 336, ["Context = CPU registers, PC, state, memory info (PCB).", "Context switch: save the context of the old process",
                             "and load the saved context of the new process.", "It is pure overhead: no useful work is done meanwhile."], size=9.6)
    return svg(360, 428, b)


# ------------------------------------------------------------------ 2.4 synchronisation
def race():
    b = title("Race Condition: counter = 5")
    b += text(180, 40, "P1: counter++    P2: counter--".replace(" ", "\u00a0"), 10, weight="bold", color=GREY, mono=True)
    rows = [("T0", "P1", "reg1 = counter", "reg1 = 5"), ("T1", "P1", "reg1 = reg1 + 1", "reg1 = 6"), ("T2", "P2", "reg2 = counter", "reg2 = 5"),
            ("T3", "P2", "reg2 = reg2 - 1", "reg2 = 4"), ("T4", "P1", "counter = reg1", "counter = 6"), ("T5", "P2", "counter = reg2", "counter = 4")]
    cw = [36, 36, 150, 114]
    xs = [12, 48, 84, 234]
    hd = ["Time", "Proc", "Machine instruction", "Result"]
    y = 52
    for i, h in enumerate(hd):
        b += box(xs[i], y, cw[i], 22, PF, P, 0, 1) + text(xs[i] + cw[i] / 2, y + 11, h, 9.4, weight="bold", color=P)
    for r, (t, p_, ins, res) in enumerate(rows):
        yy = y + 22 + r * 22
        c, f = (GREEN, GREENF) if p_ == "P1" else (BLUE, BLUEF)
        for i, v in enumerate([t, p_, ins, res]):
            b += box(xs[i], yy, cw[i], 22, f, "#D9C8F0", 0, 1) + text(xs[i] + cw[i] / 2, yy + 11, v, 9.2, color=c if i < 2 else INK, mono=i >= 2,
                                                                     weight="bold" if i == 1 or (r == 5 and i == 3) else "normal")
    y = y + 22 + 6 * 22 + 18
    b += text(180, y, "Final counter = 4, but the correct value is 5!", 10.5, weight="bold", color=RED)
    b += note(12, y + 16, 336, ["Race condition: the result depends on the order in", "which processes access shared data.",
                                "Solution: allow only one process at a time in the", "critical section (mutual exclusion)."], size=9.6)
    return svg(360, y + 88, b)


def cs():
    b = title("General Structure of a Process (CS)")
    secs = [("do {", None, None), ("    entry section", ORANGEF, ORANGE), ("        critical section", REDF, RED), ("    exit section", GREENF, GREEN),
            ("        remainder section", BLUEF, BLUE), ("} while (true);", None, None)]
    y = 36
    for s, f, c in secs:
        if f:
            b += box(40, y, 280, 28, f, c, 4, 1.3)
        b += text(52, y + 14, s.replace(" ", "\u00a0"), 10.5, anchor="start", mono=True, weight="bold", color=c or INK)
        y += 32
    y += 6
    reqs = [("1. Mutual exclusion", "only one process in its CS at a time."), ("2. Progress", "if no one is in the CS, a waiting process"),
            ("", "must be allowed to enter without delay."), ("3. Bounded waiting", "a limit on how many times others enter"),
            ("", "before a waiting process gets its turn.")]
    b += box(12, y, 336, 96, "#FBF8FF", P, 8, 1.3) + text(180, y + 14, "Requirements of a solution", 10.5, weight="bold", color=P)
    for i, (a, d) in enumerate(reqs):
        b += text(20, y + 32 + i * 14, a, 9.4, anchor="start", weight="bold") + text(130, y + 32 + i * 14, d, 9, anchor="start")
    return svg(360, y + 106, b)


def mutex():
    b = title("Mutual Exclusion using Critical Regions")
    x0, sc = 70, 2.6       # time 0..100
    ya, yb = 64, 124
    b += text(x0 - 8, ya + 12, "Process A", 9.6, anchor="end", weight="bold", color=GREEN)
    b += text(x0 - 8, yb + 12, "Process B", 9.6, anchor="end", weight="bold", color=BLUE)
    b += line(f"M{x0} {ya + 12} L{x0 + 100 * sc} {ya + 12}", "#CCC", 1.2) + line(f"M{x0} {yb + 12} L{x0 + 100 * sc} {yb + 12}", "#CCC", 1.2)
    b += box(x0 + 15 * sc, ya, 40 * sc, 24, GREEN, GREEN, 3, 1) + text(x0 + 35 * sc, ya + 12, "A in critical region", 9, color="#fff", weight="bold")
    b += box(x0 + 30 * sc, yb, 25 * sc, 24, "#fff", RED, 3, 1.3) + text(x0 + 42.5 * sc, yb + 12, "B blocked", 9, color=RED, weight="bold")
    b += box(x0 + 55 * sc, yb, 40 * sc, 24, BLUE, BLUE, 3, 1) + text(x0 + 75 * sc, yb + 12, "B in critical region", 8.6, color="#fff", weight="bold")
    for t, lab_, txt in [(15, "T1", "A enters"), (30, "T2", "B tries"), (55, "T3", "A leaves, B enters"), (95, "T4", "B leaves")]:
        x = x0 + t * sc
        b += line(f"M{x} 54 L{x} 166", P, 1.2, "3 3") + text(x, 176, lab_, 9.4, weight="bold", color=P)
    b += text(x0 + 50 * sc, 196, "time →", 9, color=GREY)
    b += note(12, 208, 336, ["Mutual exclusion: if one process is using a shared", "variable or file, other processes are kept out.",
                             "Methods: disabling interrupts, lock variable, strict", "alternation, Peterson's solution, TSL instruction,",
                             "semaphores and mutex locks."], size=9.6)
    return svg(360, 296, b)


# ------------------------------------------------------------------ 2.5 deadlock
def deadlock():
    b = title("Deadlock: Circular Wait")
    P1, P2, R1, R2 = (90, 80, "p"), (270, 180, "p"), (270, 80, "r"), (90, 180, "r")
    b += pnode(90, 80, "P1", 20) + pnode(270, 180, "P2", 20) + rnode(270, 80, "R1", 1, 46, 30, "r") + rnode(90, 180, "R2", 1, 46, 30, "l")
    b += edge(R1, P1, GREEN, 20, 46, 30) + text(180, 70, "R1 held by P1", 9.4, color=GREEN, weight="bold")
    b += edge(P1, R2, RED, 20, 46, 30) + text(84, 130, "P1 waits", 9.4, color=RED, weight="bold", anchor="end")
    b += text(84, 142, "for R2", 9.4, color=RED, weight="bold", anchor="end")
    b += edge(R2, P2, GREEN, 20, 46, 30) + text(180, 198, "R2 held by P2", 9.4, color=GREEN, weight="bold")
    b += edge(P2, R1, RED, 20, 46, 30) + text(276, 130, "P2 waits", 9.4, color=RED, weight="bold", anchor="start")
    b += text(276, 142, "for R1", 9.4, color=RED, weight="bold", anchor="start")
    b += text(180, 132, "cycle", 10, color=P, weight="bold")
    b += note(12, 224, 336, ["Each process holds one resource and waits for the", "resource held by the other: neither can continue.",
                             "Example: two trains on one track, or two cars on a", "one-lane bridge from opposite sides."], size=9.6)
    return svg(360, 296, b)


def rag():
    b = title("Resource Allocation Graph (RAG)")
    b += pnode(34, 50, "Pi") + text(56, 50, "process", 9, anchor="start")
    b += rnode(150, 52, "Rj", 2) + text(174, 52, "resource, 2 instances", 9, anchor="start")
    b += edge((24, 92, "p"), (100, 92, "r"), RED, 0, 0.1, 0.1) + text(110, 92, "request edge  Pi → Rj", 9, anchor="start", color=RED, weight="bold")
    b += edge((24, 112, "p"), (100, 112, "r"), GREEN, 0, 0.1, 0.1) + text(110, 112, "assignment edge  Rj → Pi", 9, anchor="start", color=GREEN, weight="bold")
    b += line("M12 128 L348 128", "#DDD", 1)
    X, y = 12, 150
    b += text(X + 82, y - 6, "(a) Cycle → deadlock", 9.8, weight="bold", color=RED)
    A = {"P1": (X + 34, y + 40, "p"), "R2": (X + 134, y + 40, "r"), "P2": (X + 134, y + 130, "p"), "R1": (X + 34, y + 130, "r")}
    b += pnode(*A["P1"][:2], "P1") + pnode(*A["P2"][:2], "P2") + rnode(*A["R1"][:2], "R1", side="l") + rnode(*A["R2"][:2], "R2")
    b += edge(A["P1"], A["R2"], RED) + edge(A["R2"], A["P2"], GREEN) + edge(A["P2"], A["R1"], RED) + edge(A["R1"], A["P1"], GREEN)
    X = 186
    b += text(X + 82, y - 6, "(b) Cycle, no deadlock", 9.8, weight="bold", color=GREEN)
    B = {"R1": (X + 62, y + 26, "r"), "R2": (X + 62, y + 144, "r"), "P1": (X + 16, y + 85, "p"), "P3": (X + 108, y + 85, "p"),
         "P2": (X + 146, y + 26, "p"), "P4": (X + 146, y + 144, "p")}
    for k, v in B.items():
        b += pnode(v[0], v[1], k) if v[2] == "p" else rnode(v[0], v[1], k, 2)
    b += edge(B["P1"], B["R1"], RED) + edge(B["R1"], B["P3"], GREEN) + edge(B["P3"], B["R2"], RED) + edge(B["R2"], B["P1"], GREEN)
    b += edge(B["R1"], B["P2"], GREEN) + edge(B["R2"], B["P4"], GREEN)
    b += note(12, y + 172, 336, ["No cycle → no deadlock.", "Cycle + one instance per resource → deadlock.",
                                 "Cycle + many instances → maybe deadlock: in (b), P4", "can release R2, so P3 gets it and the cycle breaks."], size=9.6)
    return svg(360, y + 244, b)


def safe():
    b = title("Safe, Unsafe and Deadlock States")
    b += f'<ellipse cx="180" cy="120" rx="160" ry="84" fill="#FAFAFA" stroke="#999" stroke-width="1.4"/>'
    b += f'<ellipse cx="102" cy="120" rx="74" ry="60" fill="{GREENF}" stroke="{GREEN}" stroke-width="1.6"/>' + text(102, 120, "Safe", 12, weight="bold", color=GREEN)
    b += f'<ellipse cx="250" cy="120" rx="78" ry="64" fill="{ORANGEF}" stroke="{ORANGE}" stroke-width="1.6"/>' + text(250, 76, "Unsafe", 11.5, weight="bold", color=ORANGE)
    b += f'<ellipse cx="256" cy="134" rx="46" ry="30" fill="{REDF}" stroke="{RED}" stroke-width="1.6"/>' + text(256, 134, "Deadlock", 10.5, weight="bold", color=RED)
    b += note(12, 216, 336, ["Safe state: a safe sequence exists in which every", "process can get its needs and finish: no deadlock.",
                             "Unsafe state: may lead to deadlock (not always).", "Avoidance (Banker's algorithm) grants a request only",
                             "if the system stays in a safe state."], size=9.6)
    return svg(360, 304, b)


def waitfor():
    b = title("RAG and its Wait-for Graph")
    X, y = 12, 50
    b += text(X + 82, y - 12, "(a) Resource allocation graph", 9.6, weight="bold", color=P)
    A = {"P1": (X + 25, y + 20, "p"), "R1": (X + 90, y + 20, "r"), "P2": (X + 150, y + 80, "p"), "R2": (X + 90, y + 140, "r"),
         "P3": (X + 25, y + 140, "p"), "R3": (X + 25, y + 80, "r")}
    for k, v in A.items():
        b += pnode(v[0], v[1], k) if v[2] == "p" else rnode(v[0], v[1], k, side="r" if k == "R3" else "t")
    for a, c in [("P1", "R1"), ("R1", "P2"), ("P2", "R2"), ("R2", "P3"), ("P3", "R3"), ("R3", "P1")]:
        b += edge(A[a], A[c], RED if a[0] == "P" else GREEN)
    X = 196
    b += text(X + 76, y - 12, "(b) Wait-for graph", 9.6, weight="bold", color=P)
    W = {"P1": (X + 30, y + 30, "p"), "P2": (X + 130, y + 80, "p"), "P3": (X + 30, y + 130, "p")}
    for k, v in W.items():
        b += pnode(v[0], v[1], k)
    b += edge(W["P1"], W["P2"], RED) + edge(W["P2"], W["P3"], RED) + edge(W["P3"], W["P1"], RED)
    b += arr([(182, y + 80), (200, y + 80)], P)
    b += note(12, y + 168, 336, ["Remove the resource nodes: Pi → Pj means Pi waits", "for a resource held by Pj.",
                                 "A cycle in the wait-for graph = deadlock (when each", "resource has a single instance). Here: P1 → P2 → P3 → P1."], size=9.6)
    return svg(360, y + 240, b)


DIAGRAMS = {"os2_memory": memory, "os2_states": states, "os2_pcb": pcb, "os2_times": times, "os2_fcfs": fcfs_d, "os2_sjf": sjf_d,
            "os2_rr": rr_d, "os2_priority": priority_d, "os2_queues": queues, "os2_schedulers": schedulers, "os2_context": context,
            "os2_race": race, "os2_cs": cs, "os2_mutex": mutex, "os2_deadlock": deadlock, "os2_rag": rag, "os2_safe": safe,
            "os2_waitfor": waitfor}

if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    for k, f in DIAGRAMS.items():
        with open(os.path.join(OUT, k + ".svg"), "w", encoding="utf-8") as fh:
            fh.write(f())
    print("written", len(DIAGRAMS))
