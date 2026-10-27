"""DI03000041 Fundamentals of Operating System - Unit 4 diagrams: file paths, permissions, directory structures,
allocation methods, disk structure, SCAN and C-SCAN."""
import os, math
from flowchart_lib import *
from diagrams_DI03000021_u1 import box, BLUE, BLUEF, GREEN, GREENF, ORANGE, ORANGEF, RED, REDF, TEAL, TEALF
from diagrams_DI03000011_u1 import note
from diagrams_DI03000041_u1 import GREY
import os_disk as D

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "content", "computer", "sem3", "DI03000041", "diagrams")
PF = "#F1E8FC"


# ------------------------------------------------------------------ tree helpers
def dw(label):
    return max(34, len(label) * 6.4 + 14)


def fw(label):
    return len(label) * 3.4 + 9


def dnode(cx, cy, label, stroke=P, fill=PF, sw=1.5):
    w = dw(label)
    return box(cx - w / 2, cy - 10, w, 20, fill, stroke, 5, sw) + text(cx, cy, label, 9.6, weight="bold", color=stroke)


def fnode(cx, cy, label, stroke=GREEN, fill=GREENF):
    rx = fw(label)
    return (f'<ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="10" fill="{fill}" stroke="{stroke}" stroke-width="1.3"/>'
            + text(cx, cy, label, 9, color=INK))


def edge(x1, y1, x2, y2, color=GREY, w=1.3, dash=None):
    return line(f"M{x1} {y1 + 10} L{x2} {y2 - 10}", color, w, dash)


def tree(nodes, edges, hi_edges=(), dash_edges=()):
    """nodes: {name: (cx, cy, label, kind)}; edges: [(a, b)]."""
    b = ""
    for a, c in edges:
        (x1, y1, *_), (x2, y2, *_) = nodes[a], nodes[c]
        if (a, c) in hi_edges:
            b += edge(x1, y1, x2, y2, RED, 2.2)
        elif (a, c) in dash_edges:
            b += edge(x1, y1, x2, y2, RED, 1.6, "4 3")
        else:
            b += edge(x1, y1, x2, y2)
    for k, (x, y, lab, kind) in nodes.items():
        if kind == "d":
            b += dnode(x, y, lab)
        elif kind == "cwd":
            b += dnode(x, y, lab, ORANGE, ORANGEF, 2.2)
        else:
            b += fnode(x, y, lab)
    return b


# ------------------------------------------------------------------ 4.1
def paths():
    b = title("Absolute and Relative File Paths")
    n = {"r": (180, 50, "/", "d"), "bin": (60, 100, "bin", "d"), "home": (180, 100, "home", "d"), "etc": (300, 100, "etc", "d"),
         "ls": (40, 150, "ls", "f"), "ravi": (140, 150, "ravi", "cwd"), "priya": (250, 150, "priya", "d"), "pw": (310, 150, "passwd", "f"),
         "os": (100, 200, "os", "d"), "c": (180, 200, "c", "d"), "ac": (250, 200, "a.c", "f"),
         "nt": (100, 250, "notes.txt", "f"), "pc": (180, 250, "prog.c", "f")}
    e = [("r", "bin"), ("r", "home"), ("r", "etc"), ("bin", "ls"), ("home", "ravi"), ("home", "priya"), ("etc", "pw"),
         ("ravi", "os"), ("ravi", "c"), ("priya", "ac"), ("os", "nt"), ("c", "pc")]
    b += tree(n, e, hi_edges={("r", "home"), ("home", "ravi"), ("ravi", "os"), ("os", "nt")})
    b += text(116, 151, "cwd", 8.4, color=ORANGE, weight="bold", anchor="end")
    b += note(12, 272, 336, [("Absolute path (red, from root /): /home/ravi/os/notes.txt", RED),
                             "Relative path (cwd = /home/ravi): os/notes.txt",
                             "Relative path to a.c: ../priya/a.c   (.. = parent)".replace("   ", "\u00a0\u00a0\u00a0")], size=9.4)
    return svg(360, 332, b)


def perm():
    b = title("Unix File Permissions (rwx)")
    s = "-rwxr-xr--"
    fills = [("#EEE", GREY)] + [(BLUEF, BLUE)] * 3 + [(GREENF, GREEN)] * 3 + [(ORANGEF, ORANGE)] * 3
    x0, cw, y0 = 40, 28, 46
    for i, ch in enumerate(s):
        f, st = fills[i]
        b += box(x0 + i * cw, y0, cw, 30, f, st, 0, 1.3) + text(x0 + i * cw + cw / 2, y0 + 15, ch, 15, weight="bold", color=st, mono=True)
    groups = [(0, 1, "Type", "- file, d dir", GREY), (1, 4, "Owner (u)", "rwx = 4+2+1 = 7", BLUE),
              (4, 7, "Group (g)", "r-x = 4+0+1 = 5", GREEN), (7, 10, "Others (o)", "r-- = 4+0+0 = 4", ORANGE)]
    for a, z, t1, t2, c in groups:
        cx = x0 + (a + z) * cw / 2
        b += line(f"M{x0 + a * cw + 3} 82 L{x0 + z * cw - 3} 82", c, 2)
        b += text(cx, 96, t1, 9.4, weight="bold", color=c)
        if a:
            b += text(cx, 112, t2, 8.6, color=INK)
    b += text(52, 112, "- / d", 8.6, color=INK)
    b += rbox(180, 140, 170, 26, "chmod 754 report.txt", PF, P, 11, "bold", P, mono=True)
    b += note(12, 166, 336, ["r = read (4), w = write (2), x = execute (1).",
                             "Access types: read, write, execute, append, delete, list.",
                             "Other methods: access-control list (ACL), passwords."], size=9.4)
    return svg(360, 226, b)


# ------------------------------------------------------------------ 4.2 directories
def single():
    b = title("Single-Level Directory")
    names = ["cat", "bo", "a", "test", "data", "mail", "cont", "hex"]
    x0, cw, y0 = 28, 38, 56
    b += text(180, 46, "Directory (one for all users)", 9.4, weight="bold", color=P)
    for i, nm in enumerate(names):
        x = x0 + i * cw
        b += box(x, y0, cw, 24, PF, P, 0, 1.3) + text(x + cw / 2, y0 + 12, nm, 9.4, weight="bold", color=P)
        b += line(f"M{x + cw / 2} {y0 + 24} L{x + cw / 2} 120", GREY, 1.2)
        b += f'<ellipse cx="{x + cw / 2}" cy="130" rx="14" ry="10" fill="{GREENF}" stroke="{GREEN}" stroke-width="1.3"/>'
    b += text(180, 154, "Files", 9.4, color=GREEN, weight="bold")
    b += note(12, 166, 336, ["All files of all users are in the same directory.",
                             "Problem: every file needs a unique name; no grouping."], size=9.4)
    return svg(360, 212, b)


def two_level():
    b = title("Two-Level Directory")
    users = ["user1", "user2", "user3", "user4"]
    ufd = [["cat", "bo", "a"], ["a", "data"], ["a", "test", "x"], ["x", "data"]]
    b += text(180, 40, "Master file directory (MFD)", 9.4, weight="bold", color=P)
    for i, u in enumerate(users):
        x = 60 + i * 60
        b += box(x, 46, 60, 22, PF, P, 0, 1.3) + text(x + 30, 57, u, 9.4, weight="bold", color=P)
        ux, n = 18 + i * 84, len(ufd[i])
        uw = n * 26
        b += line(f"M{x + 30} 68 L{ux + uw / 2} 108", GREY, 1.3)
        for j, f in enumerate(ufd[i]):
            cx = ux + j * 26 + 13
            b += box(ux + j * 26, 108, 26, 22, BLUEF, BLUE, 0, 1.2) + text(cx, 119, f, 8.6, weight="bold", color=BLUE)
            b += line(f"M{cx} 130 L{cx} 158", GREY, 1.1)
            b += f'<ellipse cx="{cx}" cy="166" rx="9" ry="8" fill="{GREENF}" stroke="{GREEN}" stroke-width="1.2"/>'
    b += text(180, 190, "Blue = user file directories (UFD); green = files", 8.8, color=BLUE, weight="bold")
    b += note(12, 200, 336, ["MFD: one entry per user, pointing to that user's UFD.",
                             "Same name (a, x, data) allowed for different users.",
                             "Path name: /user1/a.  No sharing between users."], size=9.4)
    return svg(360, 260, b)


def tree_dir():
    b = title("Tree-Structured Directory")
    n = {"r": (180, 50, "root", "d"), "sp": (70, 100, "spell", "d"), "bin": (180, 100, "bin", "d"), "pr": (290, 100, "programs", "d"),
         "st": (36, 150, "stat", "f"), "ml": (100, 150, "mail", "cwd"), "fd": (150, 150, "find", "f"), "ct": (212, 150, "count", "f"),
         "p": (262, 150, "p", "f"), "e": (310, 150, "e", "d"), "pg": (70, 200, "prog", "f"), "cp": (132, 200, "copy", "f"),
         "e1": (310, 200, "list", "f")}
    e = [("r", "sp"), ("r", "bin"), ("r", "pr"), ("sp", "st"), ("sp", "ml"), ("bin", "fd"), ("bin", "ct"), ("pr", "p"), ("pr", "e"),
         ("ml", "pg"), ("ml", "cp"), ("e", "e1")]
    b += tree(n, e)
    b += text(330, 50, "directory", 8.4, color=P, anchor="end", weight="bold")
    b += f'<ellipse cx="300" cy="66" rx="11" ry="7" fill="{GREENF}" stroke="{GREEN}" stroke-width="1.2"/>' + text(316, 66, "file", 8.4, anchor="start", color=GREEN, weight="bold")
    b += note(12, 222, 336, ["Directories contain files and subdirectories (any depth).",
                             "Each process has a current directory (orange = cwd).",
                             "Absolute path: /spell/mail/prog;  relative: prog.",
                             "Easy grouping and searching; no sharing of files."], size=9.4)
    return svg(360, 292, b)


def acyclic():
    b = title("Acyclic-Graph Directory")
    n = {"r": (180, 50, "root", "d"), "dc": (90, 100, "dict", "d"), "sp": (270, 100, "spell", "d"),
         "al": (40, 150, "all", "f"), "w": (100, 150, "w", "f"), "ls": (180, 150, "list", "f"),
         "ct": (250, 150, "count", "f"), "wd": (312, 150, "words", "d"), "w7": (312, 200, "w7", "f")}
    e = [("r", "dc"), ("r", "sp"), ("dc", "al"), ("dc", "w"), ("dc", "ls"), ("sp", "ls"), ("sp", "ct"), ("sp", "wd"), ("wd", "w7")]
    b += tree(n, e, dash_edges={("sp", "ls")})
    b += text(206, 120, "link", 8.6, color=RED, weight="bold")
    b += text(180, 172, "shared file", 8.4, color=RED, weight="bold")
    b += note(12, 222, 336, ["A file or subdirectory can be shared: it appears in two", "directories (via a link), but no cycles are allowed.",
                             "Problems: one file has many names (aliasing); deleting", "it may leave dangling links → use a reference count."], size=9.4)
    return svg(360, 292, b)


def general():
    b = title("General Graph Directory")
    n = {"r": (180, 54, "root", "d"), "av": (70, 104, "avi", "d"), "tc": (180, 104, "tc", "d"), "jm": (290, 104, "jim", "d"),
         "tx": (40, 154, "text", "f"), "ml": (100, 154, "mail", "f"), "ct": (180, 154, "count", "f"),
         "bk": (250, 154, "book", "d"), "uh": (316, 154, "unhex", "f")}
    e = [("r", "av"), ("r", "tc"), ("r", "jm"), ("av", "tx"), ("av", "ml"), ("tc", "ct"), ("jm", "bk"), ("jm", "uh")]
    b += tree(n, e)
    b += line("M250 164 C250 200 150 200 150 140 C150 120 165 80 172 66", RED, 1.6, "4 3") + arrowhead(172, 65, -70, 7, RED)
    b += text(200, 204, "link back to root → cycle", 8.8, color=RED, weight="bold")
    b += note(12, 220, 336, ["Links may point to any directory, so cycles can form.",
                             "Searching may loop forever; a file may never reach a", "reference count of 0.",
                             "Fix: garbage collection, or cycle detection on each link."], size=9.4)
    return svg(360, 290, b)


# ------------------------------------------------------------------ 4.3 allocation
GX, GW, GH, GY = 36, 36, 28, 44


def grid(colour_of, label_of=None):
    b = ""
    for k in range(32):
        r, c = divmod(k, 8)
        x, y = GX + c * GW, GY + r * GH
        f, s = colour_of.get(k, ("#fff", "#CCC"))
        b += box(x, y, GW, GH, f, s, 0, 1.1) + text(x + 7, y + 7, str(k), 7, color=GREY)
        if label_of and k in label_of:
            b += text(x + GW / 2, y + GH / 2 + 3, label_of[k], 9, weight="bold", color=s)
    return b


def dir_table(x, y, head, rows, widths):
    b, cx = "", x
    for i, h in enumerate(head):
        b += box(cx, y, widths[i], 18, PF, P, 0, 1.1) + text(cx + widths[i] / 2, y + 9, h, 9, weight="bold", color=P)
        cx += widths[i]
    for r, row in enumerate(rows):
        cx = x
        for i, v in enumerate(row):
            b += box(cx, y + 18 * (r + 1), widths[i], 18, "#fff", "#CCC", 0, 1) + text(cx + widths[i] / 2, y + 18 * (r + 1) + 9, str(v), 9)
            cx += widths[i]
    return b


def contig():
    b = title("Contiguous Allocation")
    files = [("count", 0, 2, BLUEF, BLUE), ("tr", 14, 3, GREENF, GREEN), ("mail", 19, 6, ORANGEF, ORANGE),
             ("list", 28, 4, REDF, RED), ("f", 6, 2, TEALF, TEAL)]
    col, lab = {}, {}
    for nm, st, ln, f, s in files:
        for k in range(st, st + ln):
            col[k], lab[k] = (f, s), nm
    b += grid(col, lab)
    b += dir_table(90, 170, ["file", "start", "length"], [(nm, st, ln) for nm, st, ln, *_ in files], [70, 55, 55])
    b += note(12, 286, 336, ["+ Simple; fast sequential and direct access.",
                             "− External fragmentation; file size must be known", "  in advance and the file is hard to grow."], size=9.4)
    return svg(360, 344, b)


JEEP = [9, 16, 1, 10, 25]


def linked():
    b = title("Linked Allocation")
    col = {k: (ORANGEF, ORANGE) for k in JEEP}
    lab = {k: ("→" + str(JEEP[i + 1]) if i + 1 < len(JEEP) else "-1") for i, k in enumerate(JEEP)}
    b += grid(col, lab)
    b += text(180, 172, "Chain of the file jeep (each block: data | next)", 9.2, weight="bold", color=P)
    x = 23
    for i, k in enumerate(JEEP):
        nx = str(JEEP[i + 1]) if i + 1 < len(JEEP) else "-1"
        b += box(x, 182, 28, 24, ORANGEF, ORANGE, 0, 1.2) + text(x + 14, 194, str(k), 9.6, weight="bold", color=ORANGE)
        b += box(x + 28, 182, 22, 24, "#fff", ORANGE, 0, 1.2) + text(x + 39, 194, nx, 8)
        if i + 1 < len(JEEP):
            b += arr([(x + 51, 194), (x + 65, 194)], ORANGE)
        x += 66
    b += dir_table(90, 218, ["file", "start", "end"], [("jeep", 9, 25)], [70, 55, 55])
    b += note(12, 264, 336, ["+ No external fragmentation; file can grow easily.",
                             "− Sequential access only; pointers use space;", "  one broken pointer loses the rest of the file.",
                             "FAT: next pointers kept in a table (MS-DOS)."], size=9.4)
    return svg(360, 334, b)


def indexed():
    b = title("Indexed Allocation")
    col = {k: (GREENF, GREEN) for k in JEEP}
    col[19] = (ORANGEF, ORANGE)
    lab = {k: f"#{i + 1}" for i, k in enumerate(JEEP)}
    lab[19] = "index"
    b += grid(col, lab)
    cx19 = GX + 3 * GW + GW / 2
    b += arr([(cx19, GY + 3 * GH - 4), (cx19, 184)], ORANGE)
    b += text(cx19 + 8, 168, "contents of block 19", 8.8, anchor="start", color=ORANGE, weight="bold")
    vals = JEEP + [-1, -1, -1]
    for i, v in enumerate(vals):
        x = 44 + i * 34
        b += box(x, 186, 34, 24, ORANGEF if v >= 0 else "#fff", ORANGE, 0, 1.2) + text(x + 17, 198, str(v), 9.6, weight="bold" if v >= 0 else "normal", color=INK)
    b += dir_table(90, 222, ["file", "index block"], [("jeep", 19)], [80, 100])
    b += note(12, 268, 336, ["+ Direct access; no external fragmentation.",
                             "− Index block overhead (wasted for small files).",
                             "Large files: linked / multilevel index, or combined", "scheme (UNIX inode)."], size=9.4)
    return svg(360, 338, b)


# ------------------------------------------------------------------ 4.4 disk
def disk():
    b = title("Physical Structure of a Disk")
    # side view
    b += line("M90 60 L90 190", INK, 3)
    for y in (78, 122, 166):
        b += f'<ellipse cx="90" cy="{y}" rx="64" ry="13" fill="{BLUEF}" stroke="{BLUE}" stroke-width="1.4"/>'
        b += line(f"M90 {y - 13} L90 {y + 13}", INK, 3)
        b += line(f"M172 {y - 4} L130 {y - 4}", GREY, 2.4) + box(120, y - 8, 12, 7, RED, RED, 1, 1)
    b += line("M172 56 L172 186", GREY, 3)
    b += text(58, 78, "platter", 8.4, color=BLUE, weight="bold")
    b += text(150, 48, "read-write heads", 8.6, color=RED, weight="bold")
    b += text(90, 202, "spindle", 8.6, weight="bold")
    b += text(172, 202, "arm", 8.6, color=GREY, weight="bold")
    # top view
    cx, cy = 286, 125
    a0, a1, r0, r1 = 0, math.radians(45), 46, 62
    p = (f"M{cx + r0 * math.cos(a0):.1f} {cy + r0 * math.sin(a0):.1f} L{cx + r1 * math.cos(a0):.1f} {cy + r1 * math.sin(a0):.1f} "
         f"A{r1} {r1} 0 0 1 {cx + r1 * math.cos(a1):.1f} {cy + r1 * math.sin(a1):.1f} L{cx + r0 * math.cos(a1):.1f} {cy + r0 * math.sin(a1):.1f} "
         f"A{r0} {r0} 0 0 0 {cx + r0 * math.cos(a0):.1f} {cy + r0 * math.sin(a0):.1f} Z")
    b += f'<circle cx="{cx}" cy="{cy}" r="62" fill="{BLUEF}" stroke="{BLUE}" stroke-width="1.4"/>'
    b += f'<path d="{p}" fill="{ORANGEF}" stroke="{ORANGE}" stroke-width="1.4"/>'
    for r in (46, 30, 14):
        b += f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{BLUE}" stroke-width="1"/>'
    b += f'<circle cx="{cx}" cy="{cy}" r="38" fill="none" stroke="{RED}" stroke-width="2.2"/>'
    for k in range(8):
        a = math.radians(k * 45)
        b += line(f"M{cx + 14 * math.cos(a):.1f} {cy + 14 * math.sin(a):.1f} L{cx + 62 * math.cos(a):.1f} {cy + 62 * math.sin(a):.1f}", BLUE, 0.8)
    b += f'<circle cx="{cx}" cy="{cy}" r="4" fill="{INK}"/>'
    b += text(286, 50, "track", 8.8, color=RED, weight="bold") + line(f"M286 55 L286 {cy - 38}", RED, 1.1)
    b += text(330, 202, "sector", 8.8, color=ORANGE, weight="bold") + line("M330 194 L334 150", ORANGE, 1.1)
    b += text(286, 202, "top view", 8.4, color=GREY)
    b += note(12, 214, 336, ["Track: one ring on a surface. Sector: part of a track.",
                             "Cylinder: the same track on all surfaces.",
                             "Access time = seek time + rotational latency", "                + transfer time.".replace(" ", "\u00a0")], size=9.4)
    return svg(360, 284, b)


def xs(t):
    return 32 + t * 296 / 199


def head_chart(path, ttl, jump=None, notes=()):
    b = title(ttl)
    b += line(f"M{xs(0)} 50 L{xs(199)} 50", GREY, 1.2)
    for t in (0, 50, 100, 150, 199):
        b += line(f"M{xs(t)} 46 L{xs(t)} 54", GREY, 1.2) + text(xs(t), 40, str(t), 8.4, color=GREY)
    y0, st = 68, 20
    pts = [(xs(t), y0 + i * st) for i, t in enumerate(path)]
    for i in range(len(pts) - 1):
        (x1, y1), (x2, y2) = pts[i], pts[i + 1]
        if jump is not None and i == jump:
            b += line(f"M{x1:.1f} {y1} L{x2:.1f} {y2}", GREY, 1.4, "5 4")
            b += text(180, y1 - 4, "return jump", 8.6, color=GREY, weight="bold")
        else:
            b += line(f"M{x1:.1f} {y1} L{x2:.1f} {y2}", P, 1.8)
    for i, ((x, y), t) in enumerate(zip(path_pts := pts, path)):
        end = t in (0, 199) and i > 0
        f = "#888" if end else (ORANGE if i == 0 else P)
        b += f'<circle cx="{x:.1f}" cy="{y}" r="9.5" fill="{f}"/>' + text(x, y, str(t), 7.8, color="#fff", weight="bold")
    yl = pts[-1][1] + 26
    b += text(180, yl, notes[0], 11, weight="bold", color=P)
    b += note(12, yl + 12, 336, list(notes[1:]), size=9.4)
    return svg(360, yl + 12 + 10 + 15 * (len(notes) - 1) + 8, b)


def scan_d():
    p, tot = D.scan(D.P5_Q, D.P5_H, "left")
    assert tot == 216
    return head_chart(p, "SCAN (Practical 5, head 46 → left)", notes=(
        f"Total head movement = {tot} tracks",
        "Order: " + " → ".join(map(str, p)),
        "= (46 − 0) + (170 − 0) = 46 + 170 = 216",
        ("Orange = start; grey = disk end reached.", GREY)))


def cscan_d():
    p, tot, tot2 = D.cscan(D.P5_Q, D.P5_H, "left")
    assert (tot, tot2) == (394, 195)
    return head_chart(p, "C-SCAN (Practical 5, head 46 → left)", jump=3, notes=(
        f"Total head movement = {tot} tracks",
        "Order: 46 → 40 → 10 → 0 ⇒ 199 → 170 → 135 → 90", "        → 75 → 65 → 50".replace(" ", "\u00a0"),
        "= (46 − 0) + (199 − 0) + (199 − 50) = 394",
        "Without counting the return jump: 46 + 149 = 195"))


DIAGRAMS = {"os4_paths": paths, "os4_perm": perm, "os4_single": single, "os4_two": two_level, "os4_tree": tree_dir,
            "os4_acyclic": acyclic, "os4_general": general, "os4_contig": contig, "os4_linked": linked, "os4_indexed": indexed,
            "os4_disk": disk, "os4_scan": scan_d, "os4_cscan": cscan_d}

if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    for k, f in DIAGRAMS.items():
        with open(os.path.join(OUT, k + ".svg"), "w", encoding="utf-8") as fh:
            fh.write(f())
    print("written", len(DIAGRAMS))
