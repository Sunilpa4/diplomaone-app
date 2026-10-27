"""DI01000131 Computer Programming Fundamentals - Unit 1 diagrams (flowcharts, C structure, tokens, data types ...)."""
import os
from flowchart_lib import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "content", "computer", "sem1", "DI01000131", "diagrams")


# ------------------------------------------------------------------ 1. flowchart symbols
def fc_symbols():
    b = title("Flowchart Symbols")
    b += f'<rect x="10" y="32" width="340" height="24" fill="{P}"/>'
    b += text(60, 44, "Symbol", 11.5, color="#fff", weight="bold") + text(160, 44, "Name", 11.5, color="#fff", weight="bold") \
        + text(272, 44, "Use", 11.5, color="#fff", weight="bold")
    rows = [
        (lambda y: terminal(60, y, "Start/Stop", 84, 26, 10.5), "Terminal", "Start or end of\nthe program"),
        (lambda y: io(60, y, "Read / Print", 84, 26, 10.5, 10), "Input / Output", "Read input or\ndisplay output"),
        (lambda y: process(60, y, "x = a + b", 84, 26, 10.5), "Process", "Calculation /\nassignment"),
        (lambda y: decision(60, y, "a > b ?", 84, 36, 10.5), "Decision", "Condition check,\nYes / No branches"),
        (lambda y: arr([(28, y), (92, y)]), "Flow lines", "Show direction\nof flow"),
        (lambda y: connector(48, y, "A") + connector(78, y, "A"), "Connector", "Join parts of a\nlong flowchart"),
        (lambda y: predefined(60, y, "fact( )", 84, 26, 10.5), "Predefined\nprocess", "Function / sub-\nroutine call"),
    ]
    y = 80
    for i, (shape, name, use) in enumerate(rows):
        if i % 2:
            b += f'<rect x="10" y="{y-24}" width="340" height="48" fill="#FAF7FE"/>'
        b += shape(y) + text(160, y, name, 11.5, weight="bold", color="#333") + text(272, y, use, 10.5, color="#444")
        y += 48
    b += line(f"M10 {y-24} H350", "#E0D3F2", 1)
    return svg(360, y - 14, b)


# ------------------------------------------------------------------ 2. flowchart: sum of two numbers
def fc_sum():
    b = title("Flowchart: Sum of Two Numbers")
    b += terminal(180, 50, "Start")
    b += down(180, 66, 92) + io(180, 110, "Read A, B")
    b += down(180, 127, 152) + process(180, 170, "SUM = A + B")
    b += down(180, 187, 212) + io(180, 230, "Print SUM")
    b += down(180, 247, 272) + terminal(180, 288, "Stop")
    b += text(300, 110, "Input", 10.5, color=S_IO, weight="bold") + text(300, 170, "Process", 10.5, color=S_PROC, weight="bold") \
        + text(300, 230, "Output", 10.5, color=S_IO, weight="bold")
    return svg(360, 316, b)


# ------------------------------------------------------------------ 3. flowchart: largest of three
def fc_largest():
    b = title("Flowchart: Largest of Three Numbers")
    b += terminal(180, 46, "Start")
    b += down(180, 62, 82) + io(180, 98, "Read A, B, C")
    b += down(180, 115, 133) + decision(180, 160, "A > B ?", 96, 54)
    b += arr([(132, 160), (100, 160), (100, 196)], label="Yes", lpos=(118, 151))
    b += arr([(228, 160), (260, 160), (260, 196)], label="No", lpos=(242, 151))
    b += decision(100, 222, "A > C ?", 88, 52) + decision(260, 222, "B > C ?", 88, 52)
    b += arr([(56, 222), (45, 222), (45, 282)], label="Yes", lpos=(40, 212))
    b += arr([(144, 222), (170, 222), (170, 282)], label="No", lpos=(156, 212))
    b += arr([(216, 222), (190, 222), (190, 282)], label="No", lpos=(204, 212))
    b += arr([(304, 222), (315, 222), (315, 282)], label="Yes", lpos=(322, 212))
    b += io(45, 298, "Print A", 72, 30, 11) + io(180, 298, "Print C", 72, 30, 11) + io(315, 298, "Print B", 72, 30, 11)
    b += line("M45 313 V336 H315 V313") + line("M180 313 V336")
    b += down(180, 336, 356) + terminal(180, 372, "Stop")
    return svg(360, 396, b)


# ------------------------------------------------------------------ 4. flowchart: factorial (loop)
def fc_factorial():
    b = title("Flowchart: Factorial of N (Loop)")
    x = 150
    b += terminal(x, 46, "Start")
    b += down(x, 62, 80) + io(x, 96, "Read N")
    b += down(x, 113, 130) + process(x, 147, "F = 1, i = 1")
    b += down(x, 164, 192) + decision(x, 220, "i <= N ?", 100, 54)
    b += arr([(x, 247), (x, 268)], label="Yes", lpos=(x + 18, 257)) + process(x, 285, "F = F × i")
    b += down(x, 302, 320) + process(x, 337, "i = i + 1")
    b += arr([(x, 354), (x, 366), (40, 366), (40, 178), (x, 178)])
    b += text(30, 272, "Loop", 10.5, color=GREY, weight="bold", anchor="middle").replace("<text ", '<text transform="rotate(-90 30 272)" ')
    b += arr([(x + 50, 220), (290, 220), (290, 268)], label="No", lpos=(250, 211))
    b += io(290, 285, "Print F", 90, 34) + down(290, 302, 330) + terminal(290, 346, "Stop", 80)
    return svg(360, 382, b)


# ------------------------------------------------------------------ 5. structure of C program
def c_structure():
    b = title("Basic Structure of a C Program")
    secs = [
        ("Documentation Section", "/* comments */"),
        ("Link Section", "#include <stdio.h>"),
        ("Definition Section", "#define PI 3.14"),
        ("Global Declaration Section", "int count;"),
        (None, None),
        ("Subprogram Section", "user-defined functions"),
    ]
    y = 38
    for name, ex in secs:
        if name is None:
            h = 104
            b += f'<rect x="14" y="{y}" width="190" height="{h}" rx="6" fill="#EADDF7" stroke="{P}" stroke-width="1.6"/>'
            b += text(109, y + 14, "main() Function Section", 11.5, weight="bold", color=P)
            b += text(109, y + 32, "{", 12, weight="bold")
            b += rbox(109, y + 51, 160, 24, "Declaration part", "#fff", "#9C6ADE", 11)
            b += rbox(109, y + 79, 160, 24, "Executable part", "#fff", "#9C6ADE", 11)
            b += text(109, y + 97, "}", 12, weight="bold")
            b += text(214, y + 51, "int a, b;", 10.5, anchor="start", color="#444", mono=True)
            b += text(214, y + 79, 'printf("...");', 10.5, anchor="start", color="#444", mono=True)
            y += h + 6
            continue
        b += rbox(109, y + 17, 190, 34, name, "#F5EEFD", P, 11.5, "bold", "#333", 6)
        b += text(214, y + 17, ex, 10.5, anchor="start", color="#444", mono=ex.startswith(("#", "int", "/*")))
        y += 40
    b += text(180, y + 12, "Only main() is compulsory; other sections are optional.", 10.5, color=GREY)
    return svg(360, y + 26, b)


# ------------------------------------------------------------------ 6. executing a C program
def c_execute():
    b = title("Executing a C Program")
    x = 160
    b += process(x, 50, "Write / Edit program\n(prog.c)", 160, 38, 11)
    b += down(x, 69, 88) + process(x, 104, "Preprocessor\n(#include, #define)", 160, 34, 11)
    b += down(x, 121, 140) + process(x, 156, "Compiler", 160, 30, 11.5)
    b += down(x, 171, 188) + decision(x, 214, "Syntax\nerrors?", 100, 52, 10.5)
    b += arr([(x - 50, 214), (30, 214), (30, 50), (x - 80, 50)], label="Yes", lpos=(56, 205))
    b += arr([(x, 240), (x, 260)], label="No", lpos=(x + 16, 250))
    b += process(x, 276, "Object code (prog.o / .obj)", 180, 30, 11)
    b += down(x, 291, 310) + process(x, 326, "Linker", 160, 30, 11.5)
    b += rbox(300, 326, 90, 34, "Library\nfunctions", "#FFF8E1", "#8D6E00", 10.5)
    b += arr([(255, 326), (x + 80, 326)])
    b += down(x, 341, 360) + process(x, 376, "Executable (prog.exe / a.out)", 180, 30, 11)
    b += down(x, 391, 410) + process(x, 426, "Loader → Run", 160, 30, 11.5)
    b += rbox(300, 426, 90, 30, "Input data", F_IO, S_IO, 10.5) + arr([(255, 426), (x + 80, 426)])
    b += down(x, 441, 460) + decision(x, 486, "Correct\noutput?", 100, 52, 10.5)
    b += arr([(x - 50, 486), (18, 486), (18, 40), (x - 80, 40)], label="No", lpos=(44, 477), lcolor="#C62828")
    b += text(10, 300, "Logic errors", 10, color="#C62828", weight="bold").replace("<text ", '<text transform="rotate(-90 10 300)" ')
    b += arr([(x, 512), (x, 532)], label="Yes", lpos=(x + 18, 522)) + terminal(x, 548, "Stop")
    return svg(360, 574, b)


# ------------------------------------------------------------------ 7. C tokens
def tree_left(root, leaves, ttl, h_row=42, root_fill="#7B2CD9", rx=62, rw=92, lx=205, lw=106):
    b = title(ttl)
    n = len(leaves)
    y0 = 52
    ys = [y0 + i * h_row for i in range(n)]
    cy = (ys[0] + ys[-1]) / 2
    bx = lx - lw / 2 - 20
    b += rbox(rx, cy, rw, 40, root, root_fill, root_fill, 12.5, "bold", "#fff")
    b += line(f"M{rx + rw / 2} {cy} H{bx}") + line(f"M{bx} {ys[0]} V{ys[-1]}")
    for y, (name, ex) in zip(ys, leaves):
        b += arr([(bx, y), (lx - lw / 2, y)])
        b += rbox(lx, y, lw, 32, name, "#F5EEFD", P, 11.5, "bold", "#333")
        b += text(lx + lw / 2 + 6, y, ex, 10.5, anchor="start", color="#444", mono=True)
    return svg(360, ys[-1] + 30, b)


def c_tokens():
    return tree_left("C Tokens", [
        ("Keywords", "int, if, while"),
        ("Identifiers", "sum, main, x1"),
        ("Constants", "10, 3.14, 'A'"),
        ("Strings", '"Hello"'),
        ("Special symbols", "{ } [ ] ( ) ;"),
        ("Operators", "+ - * / = <"),
    ], "C Tokens (smallest units of a program)", rx=52, rw=80, lx=190, lw=120)


# ------------------------------------------------------------------ 8. data types
def datatypes():
    b = title("Classification of Data Types in C")
    b += rbox(180, 52, 140, 30, "C Data Types", P, P, 12.5, "bold", "#fff")
    b += line("M180 67 V82 M62 82 H298") + "".join(arr([(x, 82), (x, 98)]) for x in (62, 180, 298))
    cols = [(62, "Primary\n(Built-in)", ["int", "char", "float", "double", "void"]),
            (180, "Derived", ["Array", "Pointer", "Function"]),
            (298, "User-defined", ["struct", "union", "enum", "typedef"])]
    for x, name, items in cols:
        b += rbox(x, 118, 104, 38, name, "#F5EEFD", P, 11.5, "bold", "#333")
        b += line(f"M{x} 137 V{150 + (len(items) - 1) * 30}", "#9C6ADE", 1.4)
        for i, it in enumerate(items):
            y = 160 + i * 30
            b += rbox(x, y, 84, 24, it, "#fff", "#9C6ADE", 11, mono=True)
    return svg(360, 160 + 4 * 30 + 24, b)


# ------------------------------------------------------------------ 9. type conversion hierarchy
def type_hierarchy():
    b = title("Implicit Type Conversion Hierarchy")
    levels = ["long double", "double", "float", "unsigned long int", "long int", "unsigned int", "int", "char, short int"]
    y0 = 46
    for i, lv in enumerate(levels):
        y = y0 + i * 36
        shade = ["#5B1BB0", "#6A25C4", "#7B2CD9", "#8E47E0", "#A066E6", "#B285EC", "#C5A3F1", "#D8C2F6"][i]
        b += rbox(150, y, 150, 26, lv, shade, shade, 11.5, "bold", "#fff" if i < 5 else "#2a1650", mono=True)
        if i < len(levels) - 1:
            b += arr([(150, y + 28), (150, y + 21)], "#999") if False else ""
    # side arrow lower -> higher
    b += arr([(262, y0 + 7 * 36), (262, y0)], "#C62828")
    b += text(290, y0 + 3.5 * 36 - 14, "Lower", 10.5, color="#C62828", weight="bold") + text(290, y0 + 3.5 * 36, "to", 10.5, color="#C62828") \
        + text(290, y0 + 3.5 * 36 + 14, "higher", 10.5, color="#C62828", weight="bold")
    b += text(40, y0, "Highest", 10.5, color=GREY, weight="bold") + text(40, y0 + 7 * 36, "Lowest", 10.5, color=GREY, weight="bold")
    yb = y0 + 7 * 36 + 34
    b += text(180, yb, "In a mixed expression, the lower type is promoted", 10.5, color="#444")
    b += text(180, yb + 15, "to the higher type before the operation.", 10.5, color="#444")
    return svg(360, yb + 28, b)


# ------------------------------------------------------------------ 10. operators
def operators():
    return tree_left("Operators", [
        ("Arithmetic", "+ - * / %"),
        ("Relational", "< <= > >= == !="),
        ("Logical", "&& || !"),
        ("Assignment", "= += -= *= /="),
        ("Incr / Decr", "++ --"),
        ("Conditional", "? :"),
        ("Bitwise", "& | ^ ~ << >>"),
        ("Special", "sizeof , & * . ->"),
    ], "Classification of C Operators", h_row=38, rx=46, rw=80, lx=166, lw=100)


DIAGRAMS = {
    "c1_fc_symbols": fc_symbols, "c1_fc_sum": fc_sum, "c1_fc_largest": fc_largest, "c1_fc_factorial": fc_factorial,
    "c1_structure": c_structure, "c1_execute": c_execute, "c1_tokens": c_tokens, "c1_datatypes": datatypes,
    "c1_type_hierarchy": type_hierarchy, "c1_operators": operators,
}

if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    for k, f in DIAGRAMS.items():
        with open(os.path.join(OUT, k + ".svg"), "w", encoding="utf-8") as fh:
            fh.write(f())
    print("written", len(DIAGRAMS))
