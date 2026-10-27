"""DI02000101 Scripting Language (Python) - Unit 1 diagrams."""
import os
from flowchart_lib import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "content", "computer", "sem2", "DI02000101", "diagrams")
CELL = "#F5EEFD"; BLUE = "#1565C0"; BLUEF = "#E3F0FC"; GREEN = "#2E7D32"; GREENF = "#E3F5E6"
ORANGE = "#E07B00"; ORANGEF = "#FFF1DE"; RED = "#C62828"; REDF = "#FDECEC"; YEL = "#FFF6D6"; YELS = "#B88A00"
PYB = "#306998"; PYY = "#FFD43B"


def box(x, y, w, h, fill=CELL, stroke=P, rx=6, sw=1.5):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>'


# ------------------------------------------------------------------ 1. history timeline
def history():
    b = title("History of Python")
    ev = [("1989", "Guido van Rossum starts Python at CWI,", "Netherlands (Christmas holidays)"),
          ("1991", "Python 0.9.0 released (Feb 1991):", "functions, exceptions, modules"),
          ("1994", "Python 1.0: lambda, map,", "filter, reduce"),
          ("2000", "Python 2.0: list comprehensions,", "garbage collection, Unicode"),
          ("2008", "Python 3.0: cleaner language,", "not backward compatible with 2.x"),
          ("2020", "Python 2 reaches end of life", "(1 January 2020)"),
          ("Today", "Python 3.x is used worldwide;", "managed by the PSF")]
    x0, y0, gap = 70, 48, 40
    b += line(f"M{x0} {y0} V{y0 + gap * (len(ev) - 1)}", "#C9B3EE", 3)
    for i, (yr, l1, l2) in enumerate(ev):
        y = y0 + i * gap
        b += f'<circle cx="{x0}" cy="{y}" r="7" fill="{PYY if i % 2 else PYB}" stroke="#fff" stroke-width="2"/>'
        b += text(x0 - 14, y, yr, 11, anchor="end", weight="bold", color=PYB)
        b += text(x0 + 16, y - 6, l1, 10.2, anchor="start", color=INK, weight="bold")
        b += text(x0 + 16, y + 8, l2, 10, anchor="start", color="#555")
    y = y0 + gap * len(ev) - 8
    b += text(180, y, 'Named after the BBC comedy show "Monty Python\'s Flying Circus",', 9.6, color="#555")
    b += text(180, y + 14, "not after the snake.", 9.6, color="#555")
    return svg(360, y + 26, b)


# ------------------------------------------------------------------ 2. features
def features():
    b = title("Features of Python")
    f = [("Simple & easy", "English-like syntax"), ("Interpreted", "executes line by line"),
         ("Free & open source", "PSF licence"), ("High-level", "no memory management"),
         ("Dynamically typed", "no type declaration"), ("Portable", "Windows / Linux / macOS"),
         ("Object-oriented", "classes and objects"), ("Large library", '"batteries included"'),
         ("Extensible", "mix with C, C++, Java"), ("Interactive mode", ">>> prompt (REPL)")]
    b += f'<circle cx="180" cy="44" r="0" fill="none"/>'
    for i, (h, s) in enumerate(f):
        c, r = i % 2, i // 2
        x, y = 12 + c * 172, 36 + r * 50
        fill, st = (BLUEF, PYB) if (r + c) % 2 == 0 else (YEL, YELS)
        b += box(x, y, 164, 42, fill, st, 8)
        b += f'<circle cx="{x + 15}" cy="{y + 21}" r="9" fill="{st}"/>' + text(x + 15, y + 21, str(i + 1), 10, color="#fff", weight="bold")
        b += text(x + 30, y + 14, h, 10.8, anchor="start", weight="bold", color=INK)
        b += text(x + 30, y + 29, s, 9.6, anchor="start", color="#555")
    return svg(360, 36 + 5 * 50 + 4, b)


# ------------------------------------------------------------------ 3. how python executes
def exec_flow():
    b = title("How a Python Program is Executed")
    steps = [("hello.py", "Source code (written by you)", BLUEF, BLUE),
             ("Python Compiler", "checks syntax, translates", CELL, P),
             ("Byte code (.pyc)", "platform-independent code", YEL, YELS),
             ("PVM", "Python Virtual Machine", ORANGEF, ORANGE),
             ("Output", "result on screen", GREENF, GREEN)]
    y = 40
    for i, (h, s, f, st) in enumerate(steps):
        b += box(24, y, 150, 40, f, st, 8, 1.7) + text(99, y + 20, h, 12, weight="bold", mono=(i in (0, 2)))
        b += text(184, y + 20, s, 9.8, anchor="start", color="#444")
        if i < len(steps) - 1:
            b += down(99, y + 40, y + 60)
        y += 60
    b += text(180, y + 4, "Steps 2–4 happen automatically when you run:", 10, color="#444")
    b += text(180, y + 20, "python hello.py", 11.5, mono=True, color=P, weight="bold")
    return svg(360, y + 32, b)


# ------------------------------------------------------------------ 4. structure of program
def structure():
    b = title("Basic Structure of a Python Program")
    parts = [("1. Documentation", "# Program: Area of circle\n# Author : Ravi", "#8E9AAF"),
             ("2. Import section", "import math", PYB),
             ("3. Global variables /\n    constants", "PI = 3.14159", YELS),
             ("4. Function definitions", "def area(r):\n    return PI * r * r", P),
             ("5. Main program", "r = float(input(\"r: \"))\nprint(area(r))", GREEN)]
    y = 34
    for h, code, col in parts:
        n = code.count("\n") + 1
        hh = 20 + 15 * n
        b += box(10, y, 340, hh, "#FAF7FE", col, 6)
        b += f'<rect x="10" y="{y}" width="6" height="{hh}" rx="3" fill="{col}"/>'
        b += text(24, y + hh / 2, h, 10.5, anchor="start", weight="bold", color=INK)
        for j, ln in enumerate(code.split("\n")):
            ln = "\u00a0" * (len(ln) - len(ln.lstrip(" "))) + ln.lstrip(" ")
            b += text(160, y + 17 + 15 * j, ln, 10.2, anchor="start", mono=True, color="#333")
        y += hh + 6
    b += text(180, y + 8, "Only the main statements are compulsory;", 10, color="#444")
    b += text(180, y + 22, "blocks are marked by indentation, not { }.", 10, color="#444")
    return svg(360, y + 34, b)


# ------------------------------------------------------------------ 5. variables / references
def variables():
    b = title("Variables are Names that Refer to Objects")
    b += text(180, 40, "a = 10      b = a      a = 20", 11.5, mono=True, color=P, weight="bold").replace("      ", "\u00a0\u00a0\u00a0\u00a0")
    # names
    b += text(60, 66, "Names", 10.5, weight="bold", color="#555") + text(260, 66, "Objects (in memory)", 10.5, weight="bold", color="#555")
    b += box(30, 84, 60, 32, BLUEF, BLUE) + text(60, 100, "a", 13, mono=True, weight="bold")
    b += box(30, 144, 60, 32, BLUEF, BLUE) + text(60, 160, "b", 13, mono=True, weight="bold")
    b += box(210, 80, 110, 40, YEL, YELS, 20) + text(265, 94, "20", 13, mono=True, weight="bold") + text(265, 110, "int  id: 0x…a0", 9, color="#666")
    b += box(210, 140, 110, 40, GREENF, GREEN, 20) + text(265, 154, "10", 13, mono=True, weight="bold") + text(265, 170, "int  id: 0x…48", 9, color="#666")
    b += arr([(90, 100), (208, 100)], BLUE)
    b += arr([(90, 160), (208, 160)], BLUE)
    b += line("M90 106 L208 154", "#AAA", 1.4, "4 3") + text(128, 142, "old link", 9, color="#999")
    pts = ["No declaration: the type comes from the value.",
           "b = a  makes b refer to the SAME object (10).",
           "a = 20  creates a new object; b still refers to 10.",
           "type(a) → <class 'int'>,  id(a) → its address"]
    for i, s in enumerate(pts):
        b += text(20, 204 + i * 17, "• " + s, 10, anchor="start", color=INK)
    return svg(360, 204 + 4 * 17 + 4, b)


# ------------------------------------------------------------------ 6. data types tree
def datatypes():
    b = title("Built-in Data Types in Python")
    b += rbox(180, 46, 120, 28, "Data Types", P, P, 12, "bold", "#fff")
    groups = [("Numeric", ["int", "float", "complex"], BLUE, BLUEF),
              ("Sequence", ["str", "list", "tuple"], GREEN, GREENF),
              ("Set", ["set", "frozenset"], ORANGE, ORANGEF),
              ("Mapping", ["dict"], RED, REDF),
              ("Boolean", ["bool"], YELS, YEL)]
    xs = [38, 108, 180, 252, 322]
    b += line("M180 60 V76 M38 76 H322", INK, 1.5)
    for (g, items, st, f), x in zip(groups, xs):
        b += down(x, 76, 92, INK)
        b += rbox(x, 106, 66, 26, g, f, st, 10.2, "bold")
        b += line(f"M{x} 119 V{126 + 30 * (len(items) - 1) + 12}", st, 1.2)
        for j, it in enumerate(items):
            y = 138 + 30 * j
            b += rbox(x, y, 62, 22, it, "#fff", st, 10.5, "bold", st, 11, mono=True)
    ex = [("int", "10, -5, 0b101"), ("float", "3.14, 2e3"), ("complex", "3+4j"), ("str", "'GTU', \"Hi\""),
          ("list", "[1, 2, 3]"), ("tuple", "(1, 2, 3)"), ("set", "{1, 2, 3}"), ("dict", "{'a': 1}"), ("bool", "True, False")]
    y0 = 236
    b += text(180, y0 - 8, "Examples   (NoneType: None = no value)", 10.5, weight="bold", color=P)
    for i, (t, e) in enumerate(ex):
        c, r = i % 2, i // 2
        x, y = 16 + c * 176, y0 + 6 + r * 18
        b += text(x, y, t, 10, anchor="start", mono=True, weight="bold", color=PYB) + text(x + 56, y, e, 9.8, anchor="start", mono=True, color="#333")
    return svg(360, y0 + 6 + 5 * 18 + 2, b)


# ------------------------------------------------------------------ 7. string indexing
def string_index():
    b = title("String Indexing and Slicing")
    b += text(180, 40, 's = "PYTHON"', 12, mono=True, color=P, weight="bold")
    w, x0, y = 44, 48, 70
    b += text(x0 - 8, y - 10, "+ve", 9.5, anchor="end", color=GREEN, weight="bold")
    b += text(x0 - 8, y + 50, "−ve", 9.5, anchor="end", color=RED, weight="bold")
    for i, ch in enumerate("PYTHON"):
        x = x0 + i * w
        b += text(x + w / 2, y - 10, str(i), 10.5, mono=True, color=GREEN, weight="bold")
        b += box(x, y, w, 34, CELL, P, 0) + text(x + w / 2, y + 17, ch, 14, mono=True, weight="bold")
        b += text(x + w / 2, y + 50, str(i - 6), 10.5, mono=True, color=RED, weight="bold")
    rows = [("s[0]", "'P'", "first character"), ("s[-1]", "'N'", "last character"), ("s[2:5]", "'THO'", "index 2 to 4 (end excluded)"),
            ("s[:3]", "'PYT'", "from start"), ("s[3:]", "'HON'", "till end"), ("s[::2]", "'PTO'", "every 2nd character"),
            ("s[::-1]", "'NOHTYP'", "reverse"), ("len(s)", "6", "number of characters")]
    y = 146
    for e, r, n in rows:
        b += text(20, y, e, 10.5, anchor="start", mono=True, weight="bold", color=PYB)
        b += text(92, y, "→ " + r, 10.5, anchor="start", mono=True, color=GREEN, weight="bold")
        b += text(196, y, n, 9.8, anchor="start", color="#444")
        y += 18
    b += text(180, y + 6, "Strings are immutable: s[0] = 'J' gives TypeError.", 10, color=RED, weight="bold")
    return svg(360, y + 18, b)


# ------------------------------------------------------------------ 8. type casting
def typecasting():
    b = title("Type Conversion (Type Casting)")
    b += rbox(90, 46, 160, 26, "Implicit (automatic)", GREENF, GREEN, 11, "bold")
    b += rbox(270, 46, 160, 26, "Explicit (by programmer)", BLUEF, BLUE, 11, "bold")
    chain = ["bool", "int", "float", "complex"]
    for i, c in enumerate(chain):
        y = 84 + i * 34
        b += rbox(90, y, 76, 24, c, "#fff", GREEN, 11, "bold", GREEN, 12, mono=True)
        if i < 3:
            b += down(90, y + 12, y + 22, GREEN)
    b += text(90, 84 + 4 * 34 - 6, "lower → higher type", 9.6, color="#555")
    b += text(90, 84 + 4 * 34 + 10, "3 + 2.5 → 5.5 (float)", 10, mono=True, color=GREEN, weight="bold")
    b += text(90, 84 + 4 * 34 + 26, "True + 5 → 6 (int)", 10, mono=True, color=GREEN, weight="bold")
    ex = [('int("25")', "25"), ("int(9.8)", "9"), ('float("3.5")', "3.5"), ("float(7)", "7.0"),
          ("str(100)", "'100'"), ("bool(0)", "False"), ("complex(2, 3)", "(2+3j)"), ('list("ab")', "['a','b']")]
    for i, (e, r) in enumerate(ex):
        y = 82 + i * 21
        b += text(196, y, e, 10, anchor="start", mono=True, color=BLUE, weight="bold")
        b += text(290, y, "→ " + r, 9.6, anchor="start", mono=True, color=INK)
    b += line("M180 64 V250", "#E0D3F2", 1)
    b += text(180, 270, 'int("12.5") → ValueError', 9.8, mono=True, color=RED)
    b += text(180, 286, 'int("abc")  → ValueError'.replace("  ", "\u00a0\u00a0"), 9.8, mono=True, color=RED)
    return svg(360, 298, b)


# ------------------------------------------------------------------ 9. input / output
def io_flow():
    b = title("Input and Output in Python")
    b += rbox(60, 50, 90, 30, "Keyboard", BLUEF, BLUE, 11, "bold")
    b += rbox(200, 50, 150, 30, 'input("Prompt: ")', CELL, P, 10.5, "bold", mono=True)
    b += arr([(105, 50), (124, 50)], BLUE)
    b += down(200, 65, 88, P)
    b += rbox(200, 104, 150, 30, "always returns str", YEL, YELS, 10.5, "bold")
    b += down(200, 119, 142, P)
    b += rbox(200, 158, 190, 30, "int() / float() to convert", GREENF, GREEN, 10.5, "bold")
    b += text(20, 196, 'age = int(input("Age: "))', 10.5, anchor="start", mono=True, color=P, weight="bold")
    b += line("M15 210 H345", "#E0D3F2", 1)
    b += text(180, 228, "print(*values, sep=' ', end='\\n')", 11, mono=True, color=PYB, weight="bold")
    rows = [('print("A", "B", 5)', "A B 5"), ('print("A", "B", sep="-")', "A-B"),
            ('print("Hi", end=" ")', "Hi ␣ (no newline)"), ('print(f"Sum = {a+b}")', "Sum = 30"),
            ('print("%d %.2f" % (5, 2.5))', "5 2.50"), ('print("{} {}".format(1, 2))', "1 2")]
    y = 250
    for c, o in rows:
        b += text(14, y, c, 9.8, anchor="start", mono=True, color=INK)
        b += text(250, y, o, 9.8, anchor="start", mono=True, color=GREEN, weight="bold")
        y += 18
    return svg(360, y, b)


# ------------------------------------------------------------------ 10. collections compare
def collections():
    b = title("List vs Tuple vs Set vs Dictionary")
    cols = [("", 66), ("list", 70), ("tuple", 70), ("set", 70), ("dict", 74)]
    x = 6
    xs = []
    for h, w in cols:
        xs.append((x, w))
        x += w
    rows = [("Brackets", "[ ]", "( )", "{ }", "{k: v}"),
            ("Example", "[1,2,2]", "(1,2,2)", "{1,2}", "{'a':1}"),
            ("Ordered", "Yes", "Yes", "No", "Yes*"),
            ("Mutable", "Yes", "No", "Yes", "Yes"),
            ("Duplicates", "Allowed", "Allowed", "No", "Keys: No"),
            ("Indexing", "a[0]", "t[0]", "No", "d['a']"),
            ("Empty", "[]", "()", "set()", "{}")]
    y = 34
    b += f'<rect x="6" y="{y}" width="{x - 6}" height="24" fill="{P}"/>'
    for (h, w), (xx, ww) in zip(cols, xs):
        b += text(xx + ww / 2, y + 12, h, 11, mono=True, color="#fff", weight="bold")
    y += 24
    for i, r in enumerate(rows):
        b += f'<rect x="6" y="{y}" width="{x - 6}" height="26" fill="{"#F8F4FD" if i % 2 else "#fff"}"/>'
        for j, (v, (xx, ww)) in enumerate(zip(r, xs)):
            col = INK
            if v in ("Yes", "Allowed"):
                col = GREEN
            elif v.startswith("No"):
                col = RED
            b += text(xx + ww / 2, y + 13, v, 10 if j else 9.8, mono=(j > 0 and i in (0, 1, 5, 6)), color=col, weight="bold" if j == 0 else "normal")
        y += 26
    b += line(f"M6 {y} H{x}", "#D9C8F0", 1)
    b += text(180, y + 14, "* dict keeps insertion order from Python 3.7.", 9.6, color="#555")
    b += text(180, y + 29, "{} creates an empty dict, not a set.", 9.6, color=RED, weight="bold")
    return svg(360, y + 40, b)


DIAGRAMS = {"py1_history": history, "py1_features": features, "py1_exec": exec_flow, "py1_structure": structure,
            "py1_variables": variables, "py1_datatypes": datatypes, "py1_string_index": string_index,
            "py1_typecasting": typecasting, "py1_io": io_flow, "py1_collections": collections}

if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    for k, f in DIAGRAMS.items():
        with open(os.path.join(OUT, k + ".svg"), "w", encoding="utf-8") as fh:
            fh.write(f())
    print("written", len(DIAGRAMS))
