"""DI03000041 Fundamentals of Operating System - Unit 5 diagrams: Unix architecture, Linux structure, directory hierarchy,
shell cycle, ls -l fields, vi modes, gcc stages, and flowcharts for if-else, case, while and for."""
import os, math
from flowchart_lib import *
from diagrams_DI03000021_u1 import box, BLUE, BLUEF, GREEN, GREENF, ORANGE, ORANGEF, RED, REDF, TEAL, TEALF
from diagrams_DI03000011_u1 import note
from diagrams_DI03000041_u1 import GREY

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "content", "computer", "sem3", "DI03000041", "diagrams")
PF = "#F1E8FC"


# ------------------------------------------------------------------ 5.1
def arch():
    b = title("Architecture of Unix / Linux")
    cx, cy = 180, 172
    rings = [(132, ORANGEF, ORANGE), (98, GREENF, GREEN), (64, BLUEF, BLUE), (32, "#EEE", GREY)]
    for r, f, s in rings:
        b += f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{f}" stroke="{s}" stroke-width="1.6"/>'
    b += text(cx, cy, "Hardware", 10, weight="bold", color=INK)
    b += text(cx, cy - 48, "Kernel", 10.5, weight="bold", color=BLUE)
    b += text(cx, cy + 50, "system calls", 8.4, color=BLUE)
    b += text(cx, cy - 81, "Shell", 10.5, weight="bold", color=GREEN)
    b += text(cx, cy + 82, "sh, bash, csh, ksh", 8.4, color=GREEN)
    b += text(cx, cy - 114, "Utilities / Applications", 10, weight="bold", color=ORANGE)
    for i, t in enumerate(["ls", "cp", "grep", "vi", "gcc", "sort", "who", "cat"]):
        a = math.radians(200 + i * 20) if i < 4 else math.radians(-20 + (i - 4) * 20 + 0)
        if i >= 4:
            a = math.radians(-20 + (i - 4) * 20)
        x, y = cx + 115 * math.cos(a), cy + 115 * math.sin(a)
        if i < 4:
            a = math.radians(160 + i * 16)
            x, y = cx + 115 * math.cos(a), cy + 115 * math.sin(a)
        else:
            a = math.radians(20 - (i - 4) * 16)
            x, y = cx + 115 * math.cos(a), cy + 115 * math.sin(a)
        b += text(x, y, t, 8.6, color=INK, weight="bold", mono=True)
    b += text(cx, cy + 116, "Users", 9, color=ORANGE, weight="bold")
    b += note(12, 312, 336, ["Kernel: core; manages processes, memory, files, devices.",
                             "Shell: command interpreter between user and kernel.",
                             "Utilities: commands and programs used by the users."], size=9.4)
    return svg(360, 370, b)


def kernel():
    b = title("Linux System Structure")
    x, w = 74, 274
    rows = [(44, "User applications (browser, editor, games)", ORANGEF, ORANGE),
            (80, "Shell and system utilities (bash, ls, cp)", GREENF, GREEN),
            (116, "System libraries (glibc)", TEALF, TEAL),
            (152, "System call interface", "#FFF1DE", "#E07B00")]
    for y, t, f, s in rows:
        b += box(x, y, w, 28, f, s, 6, 1.4) + text(x + w / 2, y + 14, t, 9.4, weight="bold", color=s)
    b += box(x, 188, w, 78, BLUEF, BLUE, 6, 1.4) + text(x + w / 2, 200, "Kernel", 10, weight="bold", color=BLUE)
    parts = [("Process mgmt", 0, 0), ("Memory mgmt", 1, 0), ("File system", 2, 0), ("Device drivers", 0, 1), ("Networking", 1, 1), ("IPC", 2, 1)]
    for t, c, r in parts:
        bx, by = x + 8 + c * 87, 210 + r * 27
        b += box(bx, by, 84, 22, "#fff", BLUE, 4, 1) + text(bx + 42, by + 11, t, 8.6, color=INK)
    b += box(x, 274, w, 28, "#EEE", GREY, 6, 1.4) + text(x + w / 2, 288, "Hardware (CPU, memory, disk, I/O)", 9.4, weight="bold", color=INK)
    for y1, y2, t, c in [(44, 144, "User space", GREEN), (152, 266, "Kernel space", BLUE)]:
        b += line(f"M60 {y1} L60 {y2}", c, 2)
        b += f'<g transform="rotate(-90 44 {(y1 + y2) / 2})">' + text(44, (y1 + y2) / 2, t, 9.4, weight="bold", color=c) + "</g>"
    return svg(360, 312, b)


def fs_tree():
    b = title("Linux Directory Hierarchy")
    rows = [("/bin", "essential commands (ls, cp, cat)"), ("/boot", "kernel and boot loader files"), ("/dev", "device files (sda, tty)"),
            ("/etc", "configuration files (passwd)"), ("/home", "users' home dirs (/home/student)"), ("/lib", "shared libraries"),
            ("/root", "home of the superuser"), ("/tmp", "temporary files"), ("/usr", "user programs (/usr/bin, /usr/lib)"),
            ("/var", "variable data (logs, mail)")]
    b += box(18, 40, 36, 22, PF, P, 5, 1.5) + text(36, 51, "/", 11, weight="bold", color=P)
    y0, st = 78, 25
    b += line(f"M36 62 L36 {y0 + (len(rows) - 1) * st}", GREY, 1.3)
    for i, (d, t) in enumerate(rows):
        y = y0 + i * st
        b += line(f"M36 {y} L64 {y}", GREY, 1.3)
        b += box(64, y - 10, 52, 20, PF, P, 4, 1.3) + text(90, y, d, 9.4, weight="bold", color=P, mono=True)
        b += text(124, y, t, 9.2, anchor="start")
    return svg(360, y0 + len(rows) * st + 4, b)


# ------------------------------------------------------------------ 5.2
def shell():
    b = title("How the Shell Executes a Command")
    steps = [("Display prompt  $", PF, P), ("Read the command line", BLUEF, BLUE), ("Parse: command, options, args;", BLUEF, BLUE),
             ("Find command (built-in or PATH)", BLUEF, BLUE), ("fork() a child, exec() program", GREENF, GREEN),
             ("Kernel runs it; output shown", ORANGEF, ORANGE)]
    cx, y0, st = 196, 52, 44
    for i, (t, f, s) in enumerate(steps):
        y = y0 + i * st
        h = 30 if i != 2 else 34
        b += rbox(cx, y, 236, h, "", f, s, 9.6)
        if i == 2:
            b += text(cx, y - 7, t, 9.4, weight="bold", color=s) + text(cx, y + 8, "expand  *  ?  $var".replace("  ", "\u00a0\u00a0"), 9, color=INK, mono=True)
        else:
            b += text(cx, y, t.replace("  ", "\u00a0\u00a0"), 9.6, weight="bold", color=s)
        if i < len(steps) - 1:
            b += down(cx, y + h / 2, y0 + (i + 1) * st - 15 - (2 if i + 1 == 2 else 0))
    yl = y0 + 5 * st
    b += arr([(cx - 118, yl), (40, yl), (40, y0), (cx - 118, y0)], GREY)
    b += f'<g transform="rotate(-90 30 {(y0 + yl) / 2})">' + text(30, (y0 + yl) / 2, "shell waits, then repeats", 8.6, color=GREY, weight="bold") + "</g>"
    b += note(12, yl + 26, 336, ["Format:  command  [options]  [arguments]".replace("  ", "\u00a0\u00a0"), ("$ ls -l /home      $ wc -l notes.txt".replace("  ", "\u00a0\u00a0"), BLUE)], size=9.4)
    return svg(360, yl + 72, b)


def ls_l():
    b = title("Fields of  ls -l  Output".replace("  ", "\u00a0\u00a0"))
    s = "-rw-r--r-- 1 student student 1024 Oct 27 10:30 notes.txt"
    cw, x0, y = 5.72, 18, 52
    b += box(10, y - 13, 340, 26, "#272335", "#272335", 5, 1)
    b += text(x0, y, s.replace(" ", "\u00a0"), 9.5, anchor="start", color="#fff", mono=True)
    fields = [(0, 10, "permissions", BLUE, 0), (11, 12, "links", GREY, 1), (13, 20, "owner", GREEN, 0), (21, 28, "group", TEAL, 1),
              (29, 33, "size (bytes)", ORANGE, 0), (34, 46, "modification time", RED, 1), (47, 56, "file name", P, 0)]
    for a, z, t, c, lvl in fields:
        xa, xz = x0 + a * cw, x0 + z * cw
        b += line(f"M{xa:.1f} 68 L{xz:.1f} 68", c, 2.2)
        xm = (xa + xz) / 2
        ly = 92 if lvl == 0 else 118
        b += line(f"M{xm:.1f} 70 L{xm:.1f} {ly - 9}", c, 1)
        b += text(min(max(xm, 32), 326), ly, t, 8.8, weight="bold", color=c)
    b += note(12, 134, 336, ["First character: - file, d directory, l link.",
                             "ls -a  all (hidden)    ls -R  recursive".replace("  ", "\u00a0\u00a0"),
                             "ls -t  by time    ls -r  reverse    ls -i  inode".replace("  ", "\u00a0\u00a0")], size=9.4)
    return svg(360, 194, b)


# ------------------------------------------------------------------ 5.3
def vi_modes():
    b = title("Modes of the vi / vim Editor")
    b += rbox(180, 56, 120, 26, "$ vi notes.txt", "#272335", "#272335", 9.6, "bold", "#fff", mono=True)
    b += down(180, 69, 104)
    b += rbox(180, 126, 150, 42, "", PF, P)
    b += text(180, 120, "Command mode", 11, weight="bold", color=P) + text(180, 135, "(default: move, delete, copy)", 8.4, color=GREY)
    b += rbox(80, 246, 128, 42, "", GREENF, GREEN)
    b += text(80, 240, "Insert mode", 11, weight="bold", color=GREEN) + text(80, 255, "(type text)", 8.4, color=GREY)
    b += rbox(280, 246, 128, 42, "", ORANGEF, ORANGE)
    b += text(280, 240, "Last-line (ex)", 11, weight="bold", color=ORANGE) + text(280, 255, "(save, quit, search)", 8.4, color=GREY)
    b += arr([(116, 147), (66, 225)], GREEN) + text(62, 180, "i a o", 9.4, weight="bold", color=GREEN, mono=True) + text(62, 193, "I A O", 9.4, weight="bold", color=GREEN, mono=True)
    b += arr([(96, 225), (140, 147)], P) + text(136, 196, "Esc", 9.6, weight="bold", color=P)
    b += arr([(220, 147), (264, 225)], ORANGE) + text(226, 196, ":", 12, weight="bold", color=ORANGE, mono=True)
    b += arr([(294, 225), (244, 147)], P) + text(304, 180, "Enter", 9.4, weight="bold", color=P) + text(304, 193, "/ Esc", 9.4, weight="bold", color=P)
    b += note(12, 282, 336, [":w save   :q quit   :wq or ZZ save and quit".replace("   ", "\u00a0\u00a0\u00a0"),
                             ":q! quit without saving    /word search".replace("    ", "\u00a0\u00a0\u00a0\u00a0"),
                             "dd delete line  yy copy  p paste  u undo".replace("  ", "\u00a0\u00a0")], size=9.4, mono=False)
    return svg(360, 340, b)


def gcc_d():
    b = title("Compiling a C Program with gcc")
    files = [("hello.c", "source code", BLUEF, BLUE), ("hello.i", "expanded source", "#fff", GREY), ("hello.s", "assembly code", "#fff", GREY),
             ("hello.o", "object code", "#fff", GREY), ("hello", "executable", GREENF, GREEN)]
    tools = [("Preprocessor", "gcc -E  (#include)"), ("Compiler", "gcc -S"), ("Assembler", "gcc -c"), ("Linker", "adds libraries (printf)")]
    cx, y0, st = 92, 52, 58
    for i, (f, d, fl, s) in enumerate(files):
        y = y0 + i * st
        b += rbox(cx, y, 132, 30, "", fl, s)
        b += text(cx, y - 6, f, 10, weight="bold", color=s, mono=True) + text(cx, y + 8, d, 8.4, color=GREY)
        if i < 4:
            b += down(cx, y + 15, y + st - 15)
            b += text(cx + 14, y + st / 2, tools[i][0], 9.6, anchor="start", weight="bold", color=P)
            b += text(194, y + st / 2, tools[i][1].replace("  ", "\u00a0\u00a0"), 8.6, anchor="start", color=INK)
    yb = y0 + 4 * st + 26
    b += note(12, yb, 336, [("$ gcc hello.c -o hello", BLUE), ("$ ./hello", BLUE), "Hello, Linux!",
                            "Without -o the executable is named a.out."], size=9.4, mono=True)
    return svg(360, yb + 76, b)


# ------------------------------------------------------------------ 5.4 flowcharts
def if_else():
    b = title("if ... else ... fi")
    b += terminal(180, 50, "Start", 80, 26, 10.5)
    b += down(180, 63, 82)
    b += io(180, 98, "read n", 110, 30, 10, mono=True)
    b += down(180, 113, 128)
    b += decision(180, 158, "[ $n -gt 0 ]", 134, 58, 10, mono=True)
    b += arr([(113, 158), (80, 158), (80, 198)], label="true", lpos=(94, 150))
    b += arr([(247, 158), (280, 158), (280, 198)], label="false", lpos=(266, 150))
    b += process(80, 214, 'echo "Positive"', 134, 32, 9.6, mono=True)
    b += process(280, 214, 'echo "Not positive"', 134, 32, 9.2, mono=True)
    b += line("M80 230 L80 254 L280 254 L280 230")
    b += down(180, 254, 272)
    b += terminal(180, 286, "fi / Stop", 92, 26, 10)
    b += note(12, 306, 336, ['if [ $n -gt 0 ]; then echo "Positive"', 'else echo "Not positive"; fi'], size=9.2, mono=True)
    return svg(360, 352, b)


def case_d():
    b = title("case ... esac (menu)")
    b += io(180, 50, "read ch", 110, 28, 10, mono=True)
    b += down(180, 64, 80)
    b += decision(180, 108, "case $ch in", 136, 56, 10, mono=True)
    xs_ = [52, 136, 222, 306]
    labs = [("1)", "sum"), ("2)", "diff"), ("3)", "mult"), ("*)", "invalid")]
    b += line("M180 136 L180 152")
    b += line(f"M{xs_[0]} 152 L{xs_[-1]} 152")
    for x, (pat, t) in zip(xs_, labs):
        b += arr([(x, 152), (x, 186)])
        b += text(x + 12, 170, pat, 9.6, weight="bold", color=RED, mono=True, anchor="start")
        b += process(x, 202, t, 74, 30, 10)
        b += line(f"M{x} 217 L{x} 240")
    b += line(f"M{xs_[0]} 240 L{xs_[-1]} 240")
    b += down(180, 240, 258)
    b += terminal(180, 272, "esac", 80, 26, 10.5)
    b += note(12, 292, 336, ["case $ch in", "  1) echo $((a+b)) ;;", "  *) echo \"Invalid\" ;;", "esac"], size=9.2, mono=True, lh=14)
    return svg(360, 360, b)


def while_d():
    b = title("while loop")
    b += terminal(180, 48, "Start", 80, 26, 10.5)
    b += down(180, 61, 78)
    b += process(180, 92, "i=1", 100, 28, 10, mono=True)
    b += down(180, 106, 122)
    b += decision(180, 150, "[ $i -le 5 ]", 134, 56, 10, mono=True)
    b += down(180, 178, 200)
    b += text(188, 191, "true", 10.5, anchor="start", weight="bold", color="#2E7D32")
    b += process(180, 214, "echo $i", 120, 28, 10, mono=True)
    b += down(180, 228, 244)
    b += process(180, 258, "i=$((i+1))", 120, 28, 10, mono=True)
    b += arr([(120, 258), (70, 258), (70, 150), (113, 150)], GREY)
    b += arr([(247, 150), (300, 150), (300, 296), (226, 296)], label="false", lpos=(276, 142))
    b += terminal(180, 296, "done", 92, 26, 10.5)
    b += note(12, 318, 336, ["i=1", "while [ $i -le 5 ]; do echo $i; i=$((i+1)); done"], size=9, mono=True)
    return svg(360, 364, b)


def for_d():
    b = title("for loop")
    b += process(180, 50, "for i in 1 2 3 4 5", 170, 28, 10, mono=True)
    b += down(180, 64, 86)
    b += decision(180, 114, "items left?", 128, 54, 10)
    b += down(180, 141, 164)
    b += text(188, 155, "yes", 10.5, anchor="start", weight="bold", color="#2E7D32")
    b += process(180, 178, "i = next item", 140, 28, 10)
    b += down(180, 192, 208)
    b += process(180, 222, "echo $i", 120, 28, 10, mono=True)
    b += arr([(120, 222), (70, 222), (70, 114), (116, 114)], GREY)
    b += arr([(244, 114), (300, 114), (300, 262), (226, 262)], label="no", lpos=(282, 106))
    b += terminal(180, 262, "done", 92, 26, 10.5)
    b += note(12, 284, 336, ["for i in 1 2 3 4 5; do echo $i; done", "for f in *.txt; do wc -l $f; done",
                             "for (( i=1; i<=5; i++ )); do echo $i; done"], size=9, mono=True)
    return svg(360, 344, b)


DIAGRAMS = {"os5_arch": arch, "os5_kernel": kernel, "os5_fs_tree": fs_tree, "os5_shell": shell, "os5_ls_l": ls_l, "os5_vi_modes": vi_modes,
            "os5_gcc": gcc_d, "os5_if": if_else, "os5_case": case_d, "os5_while": while_d, "os5_for": for_d}

if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    for k, f in DIAGRAMS.items():
        with open(os.path.join(OUT, k + ".svg"), "w", encoding="utf-8") as fh:
            fh.write(f())
    print("written", len(DIAGRAMS))
