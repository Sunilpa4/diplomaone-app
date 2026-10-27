"""DI01000131 Computer Programming Fundamentals - Unit 4 diagrams (user-defined functions, recursion, scope)."""
import os
from flowchart_lib import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "content", "computer", "sem1", "DI01000131", "diagrams")
CELL = "#F5EEFD"; HL = "#FFF1C2"; HL_S = "#C99A00"; OK = "#E3F5E6"; OK_S = "#2E7D32"; BLUE = "#1565C0"; RED = "#C62828"
CW = 6.32  # width of one monospace char at 10.5px


def code(x, y0, lines, step=18, size=10.5, colors=None):
    """Monospace code lines; leading spaces converted to x offset (SVG collapses spaces)."""
    out = ""
    for i, s in enumerate(lines):
        ind = len(s) - len(s.lstrip())
        col = (colors or {}).get(i, INK)
        out += text(x + ind * CW, y0 + i * step, s.strip(), size, anchor="start", mono=True, color=col,
                    weight="bold" if col != INK else "normal")
    return out


def panel(x, y, w, h, fill="#F7F2FD", stroke="#C9B3EC"):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="8" fill="{fill}" stroke="{stroke}" stroke-width="1.2"/>'


def cell(x, y, w, h, label="", fill=CELL, stroke=P, size=12, weight="bold", mono=True, color=INK):
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{fill}" stroke="{stroke}" stroke-width="1.5"/>'
            + (text(x + w / 2, y + h / 2, label, size, color=color, weight=weight, mono=mono) if label != "" else ""))


# ------------------------------------------------------------------ 1. types of functions
def func_types():
    b = title("Types of Functions in C")
    b += rbox(180, 50, 130, 30, "C Functions", P, P, 12.5, "bold", "#fff")
    b += line("M180 65 V80") + line("M95 80 H265")
    for x, name, sub, items, f, s in (
            (95, "Library Functions", "(built-in / predefined)", ["printf()  scanf()", "sqrt()  pow()", "strlen()  strcpy()", "getchar()  toupper()"], "#E3F0FC", BLUE),
            (265, "User-defined", "Functions", ["main()", "sum()  fact()", "isPrime()", "display()"], OK, OK_S)):
        b += arr([(x, 80), (x, 96)])
        b += rbox(x, 118, 156, 42, name + "\n" + sub, f, s, 11, "bold", "#333")
        b += line(f"M{x} 139 V{160 + 3 * 28}", s, 1.2)
        for i, it in enumerate(items):
            b += rbox(x, 160 + i * 28, 140, 22, it, "#fff", s, 10.5, mono=True)
    b += text(95, 268, "Declared in header files", 10.5, color="#444") + text(95, 282, "stdio.h, math.h, string.h", 10.5, color="#444", mono=True)
    b += text(265, 268, "Written by the programmer", 10.5, color="#444") + text(265, 282, "for a specific task", 10.5, color="#444")
    return svg(360, 296, b)


# ------------------------------------------------------------------ 2. modular programming
def modular():
    b = title("Modular (Top-down) Programming")
    b += rbox(180, 56, 120, 32, "main()", P, P, 12.5, "bold", "#fff", mono=True)
    b += line("M180 72 V92") + line("M62 92 H298")
    mods = [(62, "read_data()"), (180, "calculate()"), (298, "display()")]
    for x, n in mods:
        b += arr([(x, 92), (x, 112)])
        b += rbox(x, 128, 108, 30, n, CELL, P, 11, mono=True)
    b += line("M180 143 V170") + line("M128 170 H232")
    for x, n in ((128, "tax()"), (232, "grade()")):
        b += arr([(x, 170), (x, 188)])
        b += rbox(x, 202, 92, 28, n, "#fff", "#9C6ADE", 11, mono=True)
    pts = ["Big program divided into small modules (functions)", "Each function does one well-defined task",
           "main() calls functions; functions can call others", "Easy to write, test, debug and reuse"]
    for i, s in enumerate(pts):
        b += text(22, 252 + i * 17, "• " + s, 10.5, anchor="start", color="#333")
    return svg(360, 252 + 4 * 17, b)


# ------------------------------------------------------------------ 3. elements of a function
def elements():
    b = title("Elements of a User-defined Function")
    lines = ["#include <stdio.h>", "int sum(int, int);", "", "int main(void)", "{", "    int s;", "    s = sum(10, 20);",
             '    printf("%d", s);', "    return 0;", "}", "", "int sum(int a, int b)", "{", "    return a + b;", "}"]
    y0 = 52; st = 17
    b += panel(10, 34, 340, len(lines) * st + 12)
    hls = [(1, "#E3F0FC", BLUE), (6, HL, HL_S), (11, OK, OK_S), (12, OK, OK_S), (13, OK, OK_S), (14, OK, OK_S)]
    for i, f, s in hls:
        b += f'<rect x="16" y="{y0 + i * st - 9}" width="176" height="{st}" fill="{f}"/>'
    b += code(22, y0, lines, st, colors={1: BLUE, 6: "#8D6E00"})
    lab = [(1, "1. Function declaration", "(prototype)", BLUE), (6, "2. Function call", "(actual arguments)", "#8D6E00")]
    for i, l1, l2, c in lab:
        y = y0 + i * st
        b += arr([(214, y), (196, y)], c)
        b += text(220, y - 3, l1, 10.5, anchor="start", weight="bold", color=c) + text(220, y + 11, l2, 10, anchor="start", color="#444")
    yh, yb1, yb2 = y0 + 11 * st, y0 + 12 * st - 8, y0 + 14 * st + 6
    b += arr([(214, yh), (196, yh)], OK_S)
    b += text(220, yh - 3, "3. Function definition", 10.5, anchor="start", weight="bold", color=OK_S)
    b += text(220, yh + 11, "header (parameters)", 10, anchor="start", color="#444")
    b += line(f"M200 {yb1} H206 V{yb2} H200", OK_S, 1.4)
    b += text(212, (yb1 + yb2) / 2 + 4, "function body", 10, anchor="start", color="#444")
    return svg(360, 34 + len(lines) * st + 24, b)


# ------------------------------------------------------------------ 4. flow of control in a call
def call_flow():
    b = title("Flow of Control in a Function Call")
    mlines = ["int main(void)", "{", "    int s;", "    s = sum(10, 20);", '    printf("%d", s);', "}"]
    slines = ["int sum(int a, int b)", "{", "    int c = a + b;", "    return c;", "}"]
    b += panel(8, 44, 166, 128) + text(91, 58, "calling function", 10, color="#666", weight="bold")
    b += code(16, 78, mlines, 18, colors={3: "#8D6E00"})
    b += panel(190, 86, 162, 110) + text(271, 100, "called function", 10, color="#666", weight="bold")
    b += code(196, 120, slines, 18, colors={3: OK_S})
    # call arrow: s = sum(...) line y=132 -> header y=120
    b += arr([(146, 127), (180, 127), (180, 116), (193, 116)], RED)
    b += arr([(258, 174), (258, 186)], OK_S) if False else ""
    b += arr([(193, 172), (186, 172), (186, 139), (148, 139)], OK_S)
    b += text(164, 113, "①", 11, color=RED, weight="bold") + text(166, 161, "④", 11, color=OK_S, weight="bold")
    steps = [("①", "main() calls sum(10, 20); control jumps to sum", RED),
             ("②", "values 10, 20 are copied into a, b", INK),
             ("③", "body of sum executes: c = 30", INK),
             ("④", "return c sends 30 back; s = 30; main continues", OK_S)]
    for i, (n, s, c) in enumerate(steps):
        b += text(16, 222 + i * 18, n, 11, anchor="start", color=c, weight="bold") + text(34, 222 + i * 18, s, 10.5, anchor="start", color="#333")
    return svg(360, 222 + 4 * 18, b)


# ------------------------------------------------------------------ 5. call by value vs reference
def value_ref():
    b = title("Call by Value vs Call by Reference")
    # ---- value
    b += panel(8, 32, 344, 132)
    b += text(180, 48, "Call by Value:  swap(a, b);", 11.5, weight="bold", color=BLUE, mono=True)
    b += text(80, 68, "main()", 10.5, weight="bold", color="#555", mono=True) + text(275, 68, "swap(int x, int y)", 10.5, weight="bold", color="#555", mono=True)
    for cx, n, v in ((52, "a", "10"), (110, "b", "20")):
        b += text(cx, 84, n, 11, mono=True, weight="bold") + cell(cx - 24, 90, 48, 30, v)
    for cx, n, v in ((246, "x", "10 → 20"), (306, "y", "20 → 10")):
        b += text(cx, 84, n, 11, mono=True, weight="bold") + cell(cx - 28, 90, 56, 30, v, HL, HL_S, 10.5)
    b += line("M134 105 H214", GREY, 1.4, "5 4") + arrowhead(216, 105, 0, 6, GREY)
    b += text(175, 98, "copies", 10, color=GREY, weight="bold")
    b += text(180, 140, "Only the copies x, y are swapped.", 10.5, color="#333")
    b += text(180, 155, "a = 10, b = 20 remain unchanged.", 10.5, color=RED, weight="bold")
    # ---- reference
    y = 176
    b += panel(8, y, 344, 150)
    b += text(180, y + 16, "Call by Reference:  swap(&a, &b);", 11.5, weight="bold", color=OK_S, mono=True)
    b += text(80, y + 36, "main()", 10.5, weight="bold", color="#555", mono=True) + text(275, y + 36, "swap(int *x, int *y)", 10.5, weight="bold", color="#555", mono=True)
    for cx, n, v, ad in ((52, "a", "10 → 20", "1000"), (110, "b", "20 → 10", "1004")):
        b += text(cx, y + 52, n, 11, mono=True, weight="bold") + cell(cx - 28, y + 58, 56, 30, v, OK, OK_S, 10.5)
        b += small_txt(cx, y + 101, ad)
    for cx, n, v in ((246, "x", "1000"), (306, "y", "1004")):
        b += text(cx, y + 52, n, 11, mono=True, weight="bold") + cell(cx - 24, y + 58, 48, 30, v, HL, HL_S)
    b += arr([(222, y + 80), (190, y + 112), (60, y + 112), (52, y + 89)], RED)
    b += arr([(306, y + 89), (306, y + 118), (118, y + 118), (110, y + 89)], RED)
    b += text(180, y + 136, "Addresses passed: *x, *y change the original a, b.", 10.5, color="#333")
    return svg(360, y + 160, b)


def small_txt(x, y, s):
    return text(x, y, s, 10, mono=True, color=BLUE)


# ------------------------------------------------------------------ 6. categories
def categories():
    b = title("Categories of User-defined Functions")
    pans = [(10, 34, "1. No arguments, no return", False, False, "void f(void);"),
            (185, 34, "2. Arguments, no return", True, False, "void f(int x);"),
            (10, 178, "3. Arguments with return", True, True, "int f(int x);"),
            (185, 178, "4. No arguments, returns value", False, True, "int f(void);")]
    for x, y, t, a, r, proto in pans:
        b += panel(x, y, 165, 136)
        b += text(x + 82, y + 17, t, 10.5, weight="bold", color=P)
        b += rbox(x + 36, y + 66, 52, 46, "main", "#E3F0FC", BLUE, 11, "bold", mono=True)
        b += rbox(x + 129, y + 66, 52, 46, "f( )", OK, OK_S, 11, "bold", mono=True)
        # arguments arrow (top)
        if a:
            b += arr([(x + 63, y + 54), (x + 101, y + 54)], RED) + text(x + 82, y + 46, "args", 9.5, color=RED, weight="bold")
        else:
            b += line(f"M{x + 63} {y + 54} H{x + 101}", "#BBB", 1.4, "3 3") + text(x + 82, y + 46, "no args", 9.5, color="#999")
        # return arrow (bottom)
        if r:
            b += arr([(x + 101, y + 78), (x + 63, y + 78)], OK_S) + text(x + 82, y + 92, "value", 9.5, color=OK_S, weight="bold")
        else:
            b += line(f"M{x + 63} {y + 78} H{x + 101}", "#BBB", 1.4, "3 3") + text(x + 82, y + 92, "no return", 9.5, color="#999")
        b += text(x + 82, y + 118, proto, 10.5, mono=True, color=INK, weight="bold")
    b += text(180, 330, "Data flow: arguments go in, return value comes out.", 10.5, color="#444")
    return svg(360, 342, b)


# ------------------------------------------------------------------ 7. passing array
def pass_array():
    b = title("Passing an Array to a Function")
    b += text(180, 40, "float avg(int x[], int n);   avg(a, 5);", 10.5, color=P, mono=True, weight="bold")
    b += text(24, 66, "main():", 10.5, anchor="start", mono=True, weight="bold", color="#555")
    b += text(24, 82, "int a[5]", 10.5, anchor="start", mono=True, color=INK)
    x0, w = 90, 50
    for i in range(5):
        b += cell(x0 + i * w, 64, w, 34, str((i + 1) * 10), OK, OK_S)
        b += text(x0 + i * w + w / 2, 110, f"a[{i}]", 10, mono=True, color="#444")
        b += text(x0 + i * w + w / 2, 124, str(1000 + 4 * i), 10, mono=True, color=BLUE)
    b += text(24, 172, "avg():", 10.5, anchor="start", mono=True, weight="bold", color="#555")
    b += text(115, 158, "x", 11, mono=True, weight="bold") + cell(90, 164, 50, 30, "1000", HL, HL_S)
    b += text(185, 158, "n", 11, mono=True, weight="bold") + cell(160, 164, 50, 30, "5", HL, HL_S)
    b += arr([(90, 179), (78, 179), (78, 81), (88, 81)], RED)
    b += text(230, 175, "x holds the", 10.5, anchor="start", color="#333")
    b += text(230, 190, "base address", 10.5, anchor="start", color="#333")
    pts = ["Only the array name is passed (no [ ] in call)", "Base address is passed → call by reference",
           "Changes made in the function affect the original", "Size must be passed separately (n)",
           "2-D: column size is compulsory: int m[][3]"]
    for i, s in enumerate(pts):
        b += text(22, 222 + i * 17, "• " + s, 10.5, anchor="start", color="#333")
    return svg(360, 222 + 5 * 17, b)


# ------------------------------------------------------------------ 8. recursion stack factorial
def recursion_fact():
    b = title("Recursion: How fact(4) Works")
    b += text(180, 40, "fact(n) = n * fact(n-1),  fact(1) = 1", 10.5, color=P, mono=True, weight="bold")
    rows = ["fact(4) = 4 * fact(3)", "fact(3) = 3 * fact(2)", "fact(2) = 2 * fact(1)", "fact(1) = 1"]
    rets = ["24", "6", "2", "1"]
    for i, s in enumerate(rows):
        x = 20 + i * 26; y = 56 + i * 52
        base = i == 3
        b += cell(x, y, 182, 30, s, OK if base else CELL, OK_S if base else P, 10.5, "bold" if base else "normal")
        if i < 3:
            b += arr([(x + 18, y + 30), (x + 18 + 26 - 8, y + 52)], BLUE)
            b += text(x + 4, y + 44, "call", 9.5, color=BLUE, weight="bold", anchor="start")
            # return arrow on right
            xr1 = x + 26 + 182; xr0 = x + 182
            b += arr([(xr1, y + 52 + 15), (xr1 + 26, y + 52 + 15), (xr1 + 26, y + 15), (xr0 + 4, y + 15)], OK_S)
            b += text(xr1 + 30, y + 40, f"returns {rets[i + 1]}", 10, color=OK_S, weight="bold", anchor="start")
    b += text(110, 270, "base case", 10, color=OK_S, weight="bold") if False else ""
    b += text(180, 284, "Result: 4 × 3 × 2 × 1 = 24", 11.5, weight="bold", color=INK)
    b += text(180, 304, "Calls go down until the base case; then results", 10.5, color="#444")
    b += text(180, 319, "return upward. Each call waits on the stack.", 10.5, color="#444")
    return svg(360, 332, b)


# ------------------------------------------------------------------ 9. fibonacci tree
def fib_tree():
    b = title("Recursion Tree: fib(4)")
    b += text(180, 40, "fib(n) = fib(n-1) + fib(n-2);  fib(0)=0, fib(1)=1", 10, color=P, mono=True, weight="bold")
    nodes = {"r": (180, 66, "fib(4)"), "a": (104, 124, "fib(3)"), "b": (272, 124, "fib(2)"),
             "c": (59, 182, "fib(2)"), "d": (150, 182, "fib(1)"), "e": (232, 182, "fib(1)"), "f": (312, 182, "fib(0)"),
             "g": (30, 240, "fib(1)"), "h": (90, 240, "fib(0)")}
    edges = [("r", "a"), ("r", "b"), ("a", "c"), ("a", "d"), ("b", "e"), ("b", "f"), ("c", "g"), ("c", "h")]
    vals = {"r": 3, "a": 2, "b": 1, "c": 1, "d": 1, "e": 1, "f": 0, "g": 1, "h": 0}
    for p_, c_ in edges:
        x1, y1, _ = nodes[p_]; x2, y2, _ = nodes[c_]
        b += line(f"M{x1} {y1 + 12} L{x2} {y2 - 12}", "#9C6ADE", 1.4)
    for k, (x, y, s) in nodes.items():
        leaf = k in "defgh"
        dup = k in "bc"
        f, st = (OK, OK_S) if leaf else ((HL, HL_S) if dup else (CELL, P))
        b += cell(x - 27, y - 12, 54, 24, s, f, st, 10.5)
        if k in "gh":
            b += text(x, y + 24, f"={vals[k]}", 9.5, color=OK_S, weight="bold")
        else:
            b += text(x + 31, y - 12, f"={vals[k]}", 9.5, color=OK_S if leaf else "#8D6E00", anchor="start", weight="bold")
    b += cell(24, 276, 14, 12, "", OK, OK_S) + text(44, 282, "base case", 10, anchor="start", color="#333")
    b += cell(124, 276, 14, 12, "", HL, HL_S) + text(144, 282, "fib(2) computed twice", 10, anchor="start", color="#333")
    b += text(180, 306, "fib(4) = 3, but 9 calls are made → recursion", 10.5, color="#444")
    b += text(180, 321, "can repeat work and is slower than a loop.", 10.5, color="#444")
    return svg(360, 334, b)


# ------------------------------------------------------------------ 10. scope
def scope():
    b = title("Scope and Lifetime of Variables")
    b += f'<rect x="10" y="32" width="340" height="306" rx="10" fill="#FAF7FE" stroke="{P}" stroke-width="1.6"/>'
    b += text(20, 50, "Program file", 10.5, anchor="start", weight="bold", color=P)
    b += text(20, 70, "int g = 10;", 11, anchor="start", mono=True, weight="bold", color=RED)
    b += text(110, 70, "global: visible in all functions", 10, anchor="start", color="#444")
    b += f'<rect x="22" y="84" width="316" height="132" rx="8" fill="#EEF5FD" stroke="{BLUE}" stroke-width="1.4"/>'
    b += text(32, 100, "int main(void) {", 10.5, anchor="start", mono=True, weight="bold", color=BLUE)
    b += text(46, 120, "int a = 5;", 10.5, anchor="start", mono=True, color=INK) + text(126, 120, "local to main()", 10, anchor="start", color="#444")
    b += text(46, 138, "static int c;", 10.5, anchor="start", mono=True, color=INK) + text(148, 138, "local, but keeps value", 10, anchor="start", color="#444")
    b += f'<rect x="40" y="148" width="284" height="44" rx="6" fill="#E9F6EA" stroke="{OK_S}" stroke-width="1.3"/>'
    b += text(50, 164, "{", 10.5, anchor="start", mono=True, weight="bold", color=OK_S)
    b += text(62, 180, "int b = 2;", 10.5, anchor="start", mono=True, color=INK) + text(142, 180, "block scope: only inside { }", 10, anchor="start", color="#444")
    b += text(32, 207, "}", 10.5, anchor="start", mono=True, weight="bold", color=BLUE)
    b += f'<rect x="22" y="226" width="316" height="62" rx="8" fill="#FFF8E1" stroke="{HL_S}" stroke-width="1.4"/>'
    b += text(32, 242, "void fun(void) {", 10.5, anchor="start", mono=True, weight="bold", color="#8D6E00")
    b += text(46, 262, "int a = 7;", 10.5, anchor="start", mono=True, color=INK) + text(126, 262, "different a (local to fun)", 10, anchor="start", color="#444")
    b += text(46, 279, "g++;", 10.5, anchor="start", mono=True, color=INK) + text(126, 279, "global g is accessible here", 10, anchor="start", color="#444")
    b += text(180, 308, "Scope = where a variable is visible", 10.5, color="#333", weight="bold")
    b += text(180, 325, "Lifetime = how long it exists in memory", 10.5, color="#333", weight="bold")
    return svg(360, 350, b)


DIAGRAMS = {
    "c4_func_types": func_types, "c4_modular": modular, "c4_elements": elements, "c4_call_flow": call_flow,
    "c4_value_ref": value_ref, "c4_categories": categories, "c4_pass_array": pass_array,
    "c4_recursion_fact": recursion_fact, "c4_fib_tree": fib_tree, "c4_scope": scope,
}

if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    for k, f in DIAGRAMS.items():
        with open(os.path.join(OUT, k + ".svg"), "w", encoding="utf-8") as fh:
            fh.write(f())
    print("written", len(DIAGRAMS))
