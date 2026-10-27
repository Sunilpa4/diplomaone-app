"""DI03000041 Fundamentals of Operating System - Unit 1 diagrams: role, goals, services, types and structure of OS, case study."""
import math, os
from flowchart_lib import *
from diagrams_DI03000021_u1 import box, BLUE, BLUEF, GREEN, GREENF, ORANGE, ORANGEF, RED, REDF, YEL, TEAL, TEALF
from diagrams_DI03000011_u1 import note

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "content", "computer", "sem3", "DI03000041", "diagrams")
GREY = "#666"


def lines(cx, y, ls, size=10, color=INK, lh=14, weight="normal", anchor="middle"):
    return "".join(text(cx, y + i * lh, s, size, color=color, weight=weight, anchor=anchor) for i, s in enumerate(ls))


def card(x, y, w, h, ttl, ls, f, s, size=9.6, lh=14):
    b = box(x, y, w, h, f, s, 8, 1.4) + text(x + w / 2, y + 15, ttl, 11, weight="bold", color=s)
    return b + lines(x + w / 2, y + 34, ls, size, lh=lh)


def user_icon(cx, cy, c=BLUE):
    return (f'<circle cx="{cx}" cy="{cy - 7}" r="5" fill="{c}"/>'
            f'<path d="M{cx - 9} {cy + 9} Q{cx} {cy - 6} {cx + 9} {cy + 9} Z" fill="{c}"/>')


# ------------------------------------------------------------------ 1.1
def role():
    b = title("OS: Interface between User and Hardware")
    for i, x in enumerate([110, 180, 250]):
        b += user_icon(x, 48) + text(x, 70, f"User {i + 1}", 9, color=GREY)
    b += down(180, 76, 92)
    b += box(40, 94, 280, 50, GREENF, GREEN, 8, 1.5) + text(180, 110, "Application Programs", 11.5, weight="bold", color=GREEN)
    b += text(180, 128, "browser, compiler, MS Word, games", 9.5, color=GREY)
    b += down(180, 144, 160)
    b += box(40, 162, 280, 54, "#F1E8FC", P, 8, 2) + text(180, 182, "Operating System", 13, weight="bold", color=P)
    b += text(180, 202, "kernel + system programs", 9.5, color=GREY)
    b += down(180, 216, 232)
    b += box(40, 234, 280, 50, BLUEF, BLUE, 8, 1.5) + text(180, 252, "Computer Hardware", 11.5, weight="bold", color=BLUE)
    b += text(180, 270, "CPU, memory, disk, I/O devices", 9.5, color=GREY)
    b += note(12, 296, 336, ["OS = interface between user and hardware.", "OS = resource manager (CPU, memory, files, I/O).",
                             "OS = control program: runs and controls user programs.", "Examples: Windows, Linux, macOS, Android, iOS."], size=9.6)
    return svg(360, 368, b)


def functions():
    b = title("Functions of an Operating System")
    cx, cy = 180, 176
    items = ["Process\nmanagement", "Memory\nmanagement", "File\nmanagement", "Device (I/O)\nmanagement",
             "Storage\nmanagement", "Security and\nprotection", "Networking", "User\ninterface"]
    POS = [(180, 62), (292, 104), (300, 176), (292, 248), (180, 290), (68, 248), (60, 176), (68, 104)]
    for k, it in enumerate(items):
        x, y = POS[k]
        b += line(f"M{cx} {cy} L{x:.1f} {y:.1f}", "#C9B3EC", 1.5)
    for k, it in enumerate(items):
        x, y = POS[k]
        ls = it.split("\n")
        b += box(x - 52, y - 20, 104, 40, BLUEF if k % 2 else GREENF, BLUE if k % 2 else GREEN, 8, 1.3)
        b += lines(x, y - (len(ls) - 1) * 6.5, ls, 9.6, lh=13, weight="bold", color=BLUE if k % 2 else GREEN)
    b += f'<circle cx="{cx}" cy="{cy}" r="42" fill="#F1E8FC" stroke="{P}" stroke-width="2"/>'
    b += text(cx, cy - 7, "Operating", 11, weight="bold", color=P) + text(cx, cy + 9, "System", 11, weight="bold", color=P)
    b += note(12, 322, 336, [("Fundamental goals of an OS:", P), "1. Convenience: easy to use computer",
                             "2. Efficiency: best use of resources", "3. Ability to evolve: new features can be added"], size=9.6)
    return svg(360, 394, b)


def services():
    b = title("Operating System Services")
    b += rbox(180, 46, 300, 26, "User and other system programs", "#F7F7F7", "#999", 10.5, "bold")
    b += rbox(180, 82, 300, 26, "User interfaces: GUI, touch, command line (CLI)", GREENF, GREEN, 10)
    b += rbox(180, 118, 300, 26, "System calls", ORANGEF, ORANGE, 10.5, "bold")
    b += box(16, 138, 328, 194, "#FBF8FF", P, 9, 1.6)
    b += text(180, 154, "Services", 11, weight="bold", color=P)
    user = ["Program execution", "I/O operations", "File-system manipulation", "Communication", "Error detection"]
    system = ["Resource allocation", "Accounting", "Protection and security"]
    for i, s in enumerate(user):
        b += rbox(98, 178 + i * 30, 150, 24, s, GREENF, GREEN, 9.6)
    for i, s in enumerate(system):
        b += rbox(262, 178 + i * 30, 150, 24, s, BLUEF, BLUE, 9.6)
    b += text(98, 326, "help the user", 9, color=GREEN, weight="bold") + text(262, 268, "efficient system", 9, color=BLUE, weight="bold")
    b += text(262, 282, "operation", 9, color=BLUE, weight="bold")
    b += rbox(180, 352, 300, 26, "Hardware", BLUEF, BLUE, 10.5, "bold")
    return svg(360, 374, b)


# ------------------------------------------------------------------ 1.2 types
MP_SEG = [("J1", 0, 2, "cpu"), ("J1", 2, 5, "io"), ("J2", 2, 4, "cpu"), ("J2", 4, 7, "io"), ("J3", 4, 6, "cpu"), ("J3", 6, 8, "io"),
          ("J1", 6, 8, "cpu"), ("J2", 8, 10, "cpu")]
_cpu = sorted((s, e) for _, s, e, k in MP_SEG if k == "cpu")
assert all(_cpu[i][1] <= _cpu[i + 1][0] for i in range(len(_cpu) - 1)) and _cpu[0][0] == 0
assert all(_cpu[i][1] == _cpu[i + 1][0] for i in range(len(_cpu) - 1))      # CPU never idle


def multiprog():
    b = title("Multiprogramming Operating System")
    b += text(70, 44, "Main memory", 10, weight="bold", color=GREY)
    parts = [("OS", "#F1E8FC", P), ("Job 1", GREENF, GREEN), ("Job 2", BLUEF, BLUE), ("Job 3", ORANGEF, ORANGE), ("free", "#fff", "#BBB")]
    for i, (nm, f, s) in enumerate(parts):
        b += box(20, 52 + i * 34, 100, 34, f, s, 0, 1.3) + text(70, 69 + i * 34, nm, 9.8, weight="bold", color=s)
    x0, sc = 168, 17.5
    rows = ["J1", "J2", "J3"]
    b += text(258, 44, "CPU and I/O activity", 10, weight="bold", color=GREY)
    for i, r in enumerate(rows):
        y = 64 + i * 32
        b += text(x0 - 10, y + 9, r, 10, anchor="end", weight="bold")
        b += line(f"M{x0} {y + 9} L{x0 + 10 * sc} {y + 9}", "#EEE", 1)
    for r, s, e, k in MP_SEG:
        y = 64 + rows.index(r) * 32
        f, st = (("#7B2CD9", "#7B2CD9") if k == "cpu" else (ORANGEF, ORANGE))
        b += box(x0 + s * sc, y, (e - s) * sc, 18, f, st, 3, 1.2)
        b += text(x0 + (s + e) / 2 * sc, y + 9, "CPU" if k == "cpu" else "I/O", 8.4, color="#fff" if k == "cpu" else ORANGE, weight="bold")
    yb = 64 + 3 * 32
    b += line(f"M{x0} {yb} L{x0 + 10 * sc} {yb}", INK, 1.2)
    for t in range(0, 11, 2):
        b += line(f"M{x0 + t * sc} {yb} L{x0 + t * sc} {yb + 4}", INK, 1) + text(x0 + t * sc, yb + 13, str(t), 8.6, color=GREY)
    b += text(x0 + 5 * sc, yb + 27, "time →  (CPU is never idle)", 9, color=GREEN, weight="bold")
    b += note(12, 240, 336, ["Several jobs are kept in memory at the same time.", "When the running job waits for I/O, the OS switches",
                             "the CPU to another job.", "Goal: maximum CPU utilisation. Single CPU, one job", "runs at a time."], size=9.6)
    return svg(360, 330, b)


def timeshare():
    b = title("Time-Sharing (Multitasking) OS")
    cx, cy = 180, 120
    for k in range(4):
        a = math.radians(-135 + k * 90)
        x, y = cx + 120 * math.cos(a), cy + 62 * math.sin(a)
        b += line(f"M{cx} {cy} L{x:.1f} {y:.1f}", "#C9B3EC", 1.5)
        b += box(x - 34, y - 16, 68, 32, BLUEF, BLUE, 6, 1.3) + text(x, y, f"User {k + 1}", 10, weight="bold", color=BLUE)
    b += f'<circle cx="{cx}" cy="{cy}" r="34" fill="#F1E8FC" stroke="{P}" stroke-width="2"/>'
    b += text(cx, cy - 6, "CPU", 11.5, weight="bold", color=P) + text(cx, cy + 9, "shared", 9, color=GREY)
    y = 214
    b += text(180, y - 10, "Time slices (quantum q) given in turn", 10, weight="bold", color=GREY)
    cols = [GREENF, BLUEF, ORANGEF, REDF]
    strokes = [GREEN, BLUE, ORANGE, RED]
    for i in range(8):
        k = i % 4
        b += box(28 + i * 38, y, 38, 26, cols[k], strokes[k], 0, 1.2) + text(47 + i * 38, y + 13, f"U{k + 1}", 9.6, weight="bold", color=strokes[k])
    b += text(332, y + 13, "…", 12, anchor="start")
    b += note(12, y + 40, 336, ["CPU time is divided into small slices (e.g. 10–100 ms).", "The OS switches quickly between users / programs,",
                                "so each user feels the computer is dedicated to him.", "Goal: minimum response time. Example: Unix, Linux."], size=9.6)
    return svg(360, y + 112, b)


def realtime():
    b = title("Real-Time Operating System (RTOS)")
    y = 70
    b += line(f"M30 {y} L330 {y}", INK, 1.4) + arrowhead(330, y, 0, 7, INK)
    b += text(336, y + 4, "t", 10, anchor="start")
    b += line(f"M60 {y - 26} L60 {y}", RED, 2) + text(60, y - 32, "event", 9.5, color=RED, weight="bold")
    b += box(84, y - 18, 120, 18, "#7B2CD9", "#7B2CD9", 3, 1) + text(144, y - 9, "task runs", 9, color="#fff", weight="bold")
    b += line(f"M250 {y - 30} L250 {y + 6}", GREEN, 2, "4 3") + text(250, y - 36, "deadline", 9.5, color=GREEN, weight="bold")
    b += line(f"M60 {y + 16} L204 {y + 16}", BLUE, 1.2) + arrowhead(204, y + 16, 0, 6, BLUE) + text(132, y + 29, "response time", 9, color=BLUE)
    b += text(180, y + 50, "Result must be correct AND produced before the deadline", 9.8, weight="bold", color=P)
    b += card(12, y + 66, 164, 150, "Hard real-time", ["Deadline must ALWAYS", "be met; a miss means", "system failure.", "", "Airbag, pacemaker,", "ABS brakes, missile",
                                                      "and flight control"], REDF, RED, 9.4, 14)
    b += card(184, y + 66, 164, 150, "Soft real-time", ["Occasional deadline", "miss is tolerated", "(quality drops).", "", "Video streaming,", "online games,",
                                                       "VoIP, multimedia"], GREENF, GREEN, 9.4, 14)
    b += text(180, y + 236, "RTOS examples: VxWorks, QNX, FreeRTOS, RTLinux", 9.6, color=GREY)
    return svg(360, y + 250, b)


def thread_line(x, y1, y2, c):
    d = f"M{x} {y1}"
    yy, s = y1, 1
    while yy < y2:
        d += f" Q{x + 6 * s} {yy + 6} {x} {yy + 12}"
        yy += 12
        s = -s
    return line(d, c, 1.8)


def multithread():
    b = title("Single-Threaded vs Multithreaded Process")
    for k, (nm, n) in enumerate([("Single-threaded", 1), ("Multithreaded", 3)]):
        x = 12 + k * 172
        b += box(x, 34, 164, 196, "#FBF8FF", P, 8, 1.4) + text(x + 82, 52, nm, 11, weight="bold", color=P)
        for i, s in enumerate(["code", "data", "files"]):
            b += box(x + 10 + i * 48, 62, 48, 24, GREENF, GREEN, 0, 1.2) + text(x + 34 + i * 48, 74, s, 9.6, weight="bold", color=GREEN)
        w = 144 / n
        for t in range(n):
            tx = x + 10 + t * w
            b += box(tx, 92, w, 22, BLUEF, BLUE, 0, 1.1) + text(tx + w / 2, 103, "registers" if n == 1 else "regs", 8.6, color=BLUE, weight="bold")
            b += box(tx, 114, w, 22, BLUEF, BLUE, 0, 1.1) + text(tx + w / 2, 125, "stack", 8.6, color=BLUE, weight="bold")
            b += thread_line(tx + w / 2, 144, 206, RED)
        b += text(x + 82, 222, f"{n} thread" + ("s" if n > 1 else ""), 9.4, color=RED, weight="bold")
    b += note(12, 240, 336, ["Thread = light-weight process: a unit of CPU use.", "Threads of a process share code, data and files;",
                             "each thread has its own registers, PC and stack.", "Benefits: responsiveness, resource sharing, economy,",
                             "use of multi-core CPUs. Example: browser tabs."], size=9.6)
    return svg(360, 330, b)


def distributed():
    b = title("Distributed Operating System")
    cx, cy = 180, 150
    b += f'<ellipse cx="{cx}" cy="{cy}" rx="70" ry="30" fill="#F1E8FC" stroke="{P}" stroke-width="1.8"/>'
    b += text(cx, cy - 5, "Communication", 10, weight="bold", color=P) + text(cx, cy + 9, "network", 10, weight="bold", color=P)
    pos = [(70, 70), (290, 70), (70, 232), (290, 232)]
    for i, (x, y) in enumerate(pos):
        b += line(f"M{x} {y} L{cx + (x - cx) * 0.38:.1f} {cy + (y - cy) * 0.38:.1f}", BLUE, 1.6)
    for i, (x, y) in enumerate(pos):
        b += box(x - 56, y - 26, 112, 52, BLUEF, BLUE, 8, 1.4) + text(x, y - 9, f"Site {'ABCD'[i]}", 10.5, weight="bold", color=BLUE)
        b += text(x, y + 9, "CPU + memory + disk", 8.6, color=GREY)
    b += note(12, 270, 336, ["Many independent computers connected by a network,", "managed by one OS: the user sees a single system.",
                             "Advantages: resource sharing, speed-up (load sharing),", "reliability (one site fails, others work), communication."], size=9.6)
    return svg(360, 342, b)


def embedded():
    b = title("Embedded Operating System")
    b += rbox(54, 92, 84, 60, "Sensors /", BLUEF, BLUE, 10, "bold", BLUE) + text(54, 106, "buttons", 10, weight="bold", color=BLUE)
    b += box(118, 48, 124, 96, "#F1E8FC", P, 9, 2) + text(180, 66, "Embedded system", 10.5, weight="bold", color=P)
    for i, s in enumerate(["Microcontroller", "Embedded OS / RTOS", "ROM + small RAM"]):
        b += rbox(180, 86 + i * 20, 108, 18, s, "#fff", "#C9B3EC", 8.6)
    b += rbox(306, 92, 84, 60, "Motors /", GREENF, GREEN, 10, "bold", GREEN) + text(306, 106, "display", 10, weight="bold", color=GREEN)
    b += arr([(96, 92), (118, 92)]) + arr([(242, 92), (264, 92)])
    b += text(54, 136, "input", 9, color=GREY) + text(306, 136, "output", 9, color=GREY)
    b += card(12, 160, 164, 110, "Examples", ["Washing machine", "Microwave oven", "Smart TV, set-top box", "Car engine control",
                                              "Smartwatch, printer"], GREENF, GREEN, 9.4, 14)
    b += card(184, 160, 164, 110, "Embedded OS", ["FreeRTOS", "Embedded Linux", "VxWorks", "Zephyr", "Android Things"], BLUEF, BLUE, 9.4, 14)
    b += note(12, 280, 336, ["Built into a device to do a fixed, dedicated job.", "Small, fast, low power and low cost; stored in ROM.",
                             "Often real-time; little or no user interface."], size=9.6)
    return svg(360, 338, b)


# ------------------------------------------------------------------ 1.3 structure
def mode_band(y, h, label, f, s):
    return box(10, y, 340, h, f, s, 6, 1, ) + text(16, y + 12, label, 8.6, anchor="start", color=s, weight="bold")


def monolithic():
    b = title("Monolithic Kernel Structure")
    b += mode_band(32, 62, "USER MODE", "#F7F7F7", "#999")
    for i, s in enumerate(["App 1", "App 2", "Shell", "App 3"]):
        b += rbox(70 + i * 74, 66, 62, 26, s, GREENF, GREEN, 9.8, "bold", GREEN)
    b += rbox(180, 112, 300, 24, "System call interface", ORANGEF, ORANGE, 10, "bold")
    b += mode_band(132, 158, "KERNEL MODE", "#FBF8FF", P)
    b += box(30, 150, 300, 128, "#F1E8FC", P, 8, 2) + text(180, 166, "One large kernel (single program)", 10.5, weight="bold", color=P)
    svc = ["Process mgmt", "Memory mgmt", "File system", "Device drivers", "Networking", "IPC"]
    for i, s in enumerate(svc):
        b += rbox(108 + (i % 2) * 144, 192 + (i // 2) * 30, 128, 24, s, "#fff", "#C9B3EC", 9.6)
    b += rbox(180, 306, 300, 26, "Hardware", BLUEF, BLUE, 10.5, "bold")
    b += note(12, 328, 336, ["All OS services run together in kernel space.", "+ Fast (direct function calls), simple design.",
                             "− One bug can crash the whole system; hard to extend.", "Examples: MS-DOS, Unix, Linux (modular monolithic)."], size=9.6)
    return svg(360, 400, b)


def layered():
    b = title("Layered Structure")
    layers = [("Layer 5: User programs / interface", GREENF, GREEN), ("Layer 4: I/O management", BLUEF, BLUE),
              ("Layer 3: Operator–process communication", BLUEF, BLUE), ("Layer 2: Memory management", BLUEF, BLUE),
              ("Layer 1: CPU scheduling", BLUEF, BLUE), ("Layer 0: Hardware", "#F1E8FC", P)]
    for i, (s, f, st) in enumerate(layers):
        w = 300 - i * 0
        b += rbox(160, 50 + i * 34, w, 28, s, f, st, 10, "bold", st)
    b += arr([(326, 60), (326, 214)], RED) + text(334, 140, "uses", 9, color=RED, anchor="start")
    b += text(334, 152, "lower", 9, color=RED, anchor="start")
    b += note(12, 250, 336, ["OS is divided into layers; layer 0 = hardware, top", "layer = user interface.",
                             "Each layer uses only the services of the layer below", "it and gives services to the layer above.",
                             "+ Easy to build, debug and verify, layer by layer.", "− Hard to define layers; slower (many layers to cross).",
                             "Example: THE OS (Dijkstra), Windows NT (partly)."], size=9.6)
    return svg(360, 374, b)


def microkernel():
    b = title("Microkernel Structure")
    b += mode_band(32, 96, "USER MODE", "#F7F7F7", "#999")
    srv = [("Application", GREENF, GREEN), ("File server", BLUEF, BLUE), ("Device driver", BLUEF, BLUE), ("Network server", BLUEF, BLUE)]
    for i, (s, f, st) in enumerate(srv):
        ls = s.split(" ")
        b += rbox(56 + i * 83, 80, 76, 40, "", f, st) + lines(56 + i * 83, 80 - (len(ls) - 1) * 6.5, ls, 9.6, lh=13, weight="bold", color=st)
    b += mode_band(136, 70, "KERNEL MODE", "#FBF8FF", P)
    b += rbox(188, 180, 276, 34, "Microkernel: IPC, basic scheduling, memory", "#F1E8FC", P, 9.6, "bold", P)
    b += arr([(56, 100), (56, 163)], RED) + arr([(139, 163), (139, 100)], RED)
    b += text(97, 116, "messages", 8.6, color=RED, weight="bold")
    b += rbox(180, 230, 300, 26, "Hardware", BLUEF, BLUE, 10.5, "bold")
    b += note(12, 254, 336, ["Only the most basic functions stay in the kernel;", "other services run as user-mode servers.",
                             "They communicate by message passing (IPC).", "+ Reliable, secure, easy to extend and port.",
                             "− Slower due to many messages / mode switches.", "Examples: QNX, MINIX 3, L4, Mach (in macOS XNU)."], size=9.6)
    return svg(360, 364, b)


# ------------------------------------------------------------------ 1.4 case study
def linux():
    b = title("Linux: Layers")
    cx, cy = 180, 150
    rings = [(118, "Applications / utilities", GREENF, GREEN), (88, "Shell", ORANGEF, ORANGE), (58, "Kernel", "#F1E8FC", P), (28, "Hardware", BLUEF, BLUE)]
    for r, s, f, st in rings:
        b += f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{f}" stroke="{st}" stroke-width="1.6"/>'
    b += text(cx, cy + 4, "Hardware", 9.4, weight="bold", color=BLUE)
    b += text(cx, cy - 40, "Kernel", 10, weight="bold", color=P)
    b += text(cx, cy - 70, "Shell", 10, weight="bold", color=ORANGE)
    b += text(cx, cy - 100, "Applications", 10, weight="bold", color=GREEN)
    b += note(12, 278, 336, [("Linux: free, open-source, Unix-like OS (Linus Torvalds, 1991).", P), "Monolithic but modular kernel; GPL licence.",
                             "Multi-user, multitasking, secure, portable.", "Distributions: Ubuntu, Fedora, Debian, Mint, RHEL.",
                             "Runs servers, supercomputers, Android phones."], size=9.4)
    return svg(360, 372, b)


CASE = [("Developer", ["Linus Torvalds +", "community"], ["Microsoft"], ["Apple"]),
        ("Latest", ["Many distros,", "e.g. Ubuntu"], ["Windows 11,", "version 26H2"], ["macOS 27", "Golden Gate"]),
        ("Kernel", ["Monolithic", "(modular)"], ["Hybrid", "(NT kernel)"], ["Hybrid", "(XNU)"]),
        ("Source", ["Open source", "(GPL)"], ["Closed", "source"], ["Closed (Darwin", "core is open)"]),
        ("File system", ["ext4, Btrfs,", "XFS"], ["NTFS"], ["APFS"]),
        ("Cost", ["Free"], ["Paid licence"], ["Free with", "a Mac"]),
        ("Hardware", ["Almost any:", "PC, server, phone"], ["PCs (x86,", "ARM)"], ["Apple Macs only", "(Apple silicon)"]),
        ("Default shell", ["bash"], ["PowerShell,", "cmd"], ["zsh"])]


def case():
    b = title("Linux vs Windows vs macOS")
    cw = [78, 90, 90, 90]
    xs = [12, 90, 180, 270]
    heads = [("", "#fff", "#fff"), ("Linux", GREEN, GREEN), ("Windows", BLUE, BLUE), ("macOS", "#555", "#555")]
    for i, (h, f, s) in enumerate(heads):
        if h:
            b += box(xs[i], 32, cw[i], 24, f, s, 0, 1) + text(xs[i] + cw[i] / 2, 44, h, 10.5, weight="bold", color="#fff")
    y = 56
    for r, (lab_, *cells) in enumerate(CASE):
        h = 34
        fill = "#FAF6FF" if r % 2 else "#fff"
        b += box(xs[0], y, cw[0], h, "#F1E8FC", "#D9C8F0", 0, 1) + text(xs[0] + 6, y + h / 2, lab_, 9.2, anchor="start", weight="bold", color=P)
        for i, c in enumerate(cells):
            b += box(xs[i + 1], y, cw[i + 1], h, fill, "#D9C8F0", 0, 1)
            b += lines(xs[i + 1] + cw[i + 1] / 2, y + h / 2 - (len(c) - 1) * 5.5, c, 8.8, lh=11)
        y += h
    b += text(180, y + 16, "Versions as of October 2026", 9, color=GREY)
    return svg(360, y + 28, b)


DIAGRAMS = {"os1_role": role, "os1_functions": functions, "os1_services": services, "os1_multiprog": multiprog, "os1_timeshare": timeshare,
            "os1_realtime": realtime, "os1_multithread": multithread, "os1_distributed": distributed, "os1_embedded": embedded,
            "os1_monolithic": monolithic, "os1_layered": layered, "os1_microkernel": microkernel, "os1_linux": linux, "os1_case": case}

if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    for k, f in DIAGRAMS.items():
        with open(os.path.join(OUT, k + ".svg"), "w", encoding="utf-8") as fh:
            fh.write(f())
    print("written", len(DIAGRAMS))
