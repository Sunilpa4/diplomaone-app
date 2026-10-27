"""DI02000101 Scripting Language (Python) - Unit 4 diagrams (built-ins, strings, files, functions)."""
import os
from flowchart_lib import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "content", "computer", "sem2", "DI02000101", "diagrams")
CELL = "#F5EEFD"; BLUE = "#1565C0"; BLUEF = "#E3F0FC"; GREEN = "#2E7D32"; GREENF = "#E3F5E6"
ORANGE = "#E07B00"; ORANGEF = "#FFF1DE"; RED = "#C62828"; REDF = "#FDECEC"; YEL = "#FFF6D6"; YELS = "#B88A00"
PYB = "#306998"
NB = "\u00a0"


def box(x, y, w, h, fill=CELL, stroke=P, rx=6, sw=1.5, dash=None):
    da = f' stroke-dasharray="{dash}"' if dash else ""
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"{da}/>'


def sp(s):
    return s.replace(" ", NB)


def table_rows(rows, y, x1=14, x2=170, size=10.2, rh=20, c1=PYB, c2=GREEN, f2=9.8):
    b = ""
    for i, (a, r) in enumerate(rows):
        b += f'<rect x="8" y="{y}" width="344" height="{rh}" fill="{"#F6F0FE" if i % 2 == 0 else "#fff"}"/>'
        b += text(x1, y + rh / 2, sp(a), size, anchor="start", mono=True, weight="bold", color=c1)
        b += text(x2, y + rh / 2, sp(r), f2, anchor="start", mono=True, color=RED if "Error" in r else c2)
        y += rh
    return b, y


# ------------------------------------------------------------------ 1. types of functions
def func_types():
    b = title("Types of Functions in Python")
    b += rbox(180, 52, 120, 32, "Functions", P, P, 13, "bold", "#fff")
    b += line("M180 68 V84 M76 84 H284 M76 84 V96 M284 84 V96", P)
    b += rbox(76, 114, 136, 34, "Built-in Functions", BLUEF, BLUE, 11.5, "bold", BLUE)
    b += rbox(284, 114, 136, 34, "User-defined", GREENF, GREEN, 11.5, "bold", GREEN)
    left = ["Ready-made, part of Python", "No def needed", "", "Type conversion:", " int() float() str()", " list() set() dict()",
            "Math:", " abs() round() pow()", " divmod() sum() max()", "String methods:", " upper() find() strip()", "File:", " open() read() write()"]
    right = ["Written by programmer", "Created with def", "", "def area(r):", "  return 3.14*r*r", "", "Arguments:",
             " positional", " keyword, default", " *args, **kwargs", "Special kinds:", " recursive", " lambda"]
    for i, s in enumerate(left):
        mono = s.startswith(" ")
        b += text(14, 148 + i * 15, sp(s), 9.8 if mono else 10, anchor="start", mono=mono,
                  weight="bold" if s.endswith(":") else "normal", color=PYB if mono else ("#444" if not s.endswith(":") else BLUE))
    for i, s in enumerate(right):
        mono = s.startswith(" ") or s.startswith("def")
        b += text(220, 148 + i * 15, sp(s), 9.8 if mono else 10, anchor="start", mono=mono,
                  weight="bold" if s.endswith(":") and not s.startswith("def") else "normal",
                  color=PYB if mono else ("#444" if not s.endswith(":") else GREEN))
    b += line("M180 100 V340", "#E0D3F2", 1)
    return svg(360, 350, b)


# ------------------------------------------------------------------ 2. type conversion
def conversion():
    b = title("Type / Data Conversion Functions")
    rows = [('int("25")', "25"), ("int(9.99)", "9   (truncates)"), ('int("1010", 2)', "10  (binary → int)"), ('int("abc")', "ValueError"),
            ('float("3.5")', "3.5"), ("float(7)", "7.0"), ("str(12.5)", "'12.5'"), ("bool(0), bool('')", "False False"),
            ('bool(5), bool("0")', "True True"), ("complex(2, 3)", "(2+3j)"), ('list("abc")', "['a', 'b', 'c']"),
            ("tuple([1, 2])", "(1, 2)"), ("set([1, 1, 2])", "{1, 2}"), ('dict([("a", 1)])', "{'a': 1}"),
            ("frozenset([1, 2])", "frozenset({1, 2})"), ('bytes("Hi", "utf-8")', "b'Hi'"),
            ("bytearray(b'Hi')", "bytearray(b'Hi')")]
    tb, y = table_rows(rows, 34, x2=176)
    b += tb
    b += text(180, y + 15, "Implicit: 3 + 2.5 → 5.5 (int becomes float automatically)", 9.8, color="#444")
    b += text(180, y + 31, "Explicit: done by the programmer with these functions", 9.8, color="#444")
    return svg(360, y + 42, b)


# ------------------------------------------------------------------ 3. string testing methods
def str_is():
    b = title("String Testing Methods (return True/False)")
    cols = ['"Py3"', '"abc"', '"123"', '"ABC"', '"  "']
    meths = [("isalnum()", "TTTTF"), ("isalpha()", "FTFTF"), ("isdigit()", "FFTFF"), ("islower()", "FTFFF"),
             ("isupper()", "FFFTF"), ("isspace()", "FFFFT"), ("isidentifier()", "TTFTF")]
    x0, cw = 126, 45
    b += f'<rect x="8" y="34" width="344" height="24" fill="{P}"/>'
    b += text(14, 46, "method", 10.5, anchor="start", weight="bold", color="#fff")
    for j, c in enumerate(cols):
        b += text(x0 + j * cw + cw / 2, 46, sp(c), 10, mono=True, weight="bold", color="#fff")
    y = 58
    for i, (m, tf) in enumerate(meths):
        b += f'<rect x="8" y="{y}" width="344" height="22" fill="{"#F6F0FE" if i % 2 == 0 else "#fff"}"/>'
        b += text(14, y + 11, m, 10.2, anchor="start", mono=True, weight="bold", color=PYB)
        for j, ch in enumerate(tf):
            b += text(x0 + j * cw + cw / 2, y + 11, "True" if ch == "T" else "False", 9.6, mono=True, weight="bold",
                      color=GREEN if ch == "T" else RED)
        y += 22
    notes = ['"Py3".isupper() is False because "y" is lowercase.', "Digits and spaces are ignored by islower()/isupper().",
             "An empty string \"\" gives False for every is…() method.", 'isidentifier(): valid variable name? "2x" → False']
    for i, s in enumerate(notes):
        b += text(180, y + 18 + i * 15, s, 9.6, color="#444")
    return svg(360, y + 18 + 4 * 15, b)


# ------------------------------------------------------------------ 4. alignment & strip
def align():
    b = title("Alignment and Strip Methods")
    b += text(180, 38, sp('s = "Py"    width = 10, fill "*"'), 10.5, mono=True, color=P, weight="bold")
    rows = [('s.ljust(10, "*")', "Py********"), ('s.rjust(10, "*")', "********Py"), ('s.center(10, "*")', "****Py****")]
    cw = 16
    y = 54
    for e, r in rows:
        b += text(14, y + 11, e, 10.2, anchor="start", mono=True, weight="bold", color=PYB)
        for k, ch in enumerate(r):
            f = YEL if ch != "*" else "#fff"
            b += box(186 + k * cw, y, cw, 22, f, "#C9B6E8", 0, 1) + text(186 + k * cw + cw / 2, y + 11, ch, 10.5, mono=True,
                                                                         weight="bold", color=INK if ch != "*" else "#999")
        y += 30
    b += text(180, y + 6, sp("f-string:  f\"{s:<10}\"  f\"{s:>10}\"  f\"{s:^10}\""), 9.8, mono=True, color="#444")
    y += 30
    b += line(f"M10 {y - 8} H350", "#E0D3F2", 1)
    b += text(180, y + 8, sp('t = "  hello  "   (2 spaces each side)'), 10.5, mono=True, color=P, weight="bold")
    rows = [("t.strip()", "hello", "both sides"), ("t.lstrip()", "hello  ", "left only"), ("t.rstrip()", "  hello", "right only")]
    y += 22
    for e, r, n in rows:
        b += text(14, y + 11, e, 10.2, anchor="start", mono=True, weight="bold", color=PYB)
        for k, ch in enumerate(r):
            b += box(120 + k * cw, y, cw, 22, YEL if ch != " " else "#fff", "#C9B6E8", 0, 1) + text(120 + k * cw + cw / 2, y + 11,
                                                                                               ch if ch != " " else "·", 10.5, mono=True, weight="bold")
        b += text(348, y + 11, n, 9.5, anchor="end", color="#666")
        y += 28
    b += text(180, y + 8, sp('"--Hi--".strip("-") → "Hi"   (chars to remove)'), 9.8, mono=True, color="#444")
    return svg(360, y + 20, b)


# ------------------------------------------------------------------ 5. file modes
def file_modes():
    b = title("File Opening Modes: open(name, mode)")
    hdr = ["Mode", "Purpose", "File missing", "Pointer", "Old data"]
    xs = [12, 54, 168, 248, 300]
    b += f'<rect x="8" y="34" width="344" height="24" fill="{P}"/>'
    for x, h in zip(xs, hdr):
        b += text(x, 46, h, 9.8, anchor="start", weight="bold", color="#fff")
    rows = [('"r"', "Read (default)", "Error", "Start", "Kept"), ('"w"', "Write", "Creates", "Start", "Erased"),
            ('"a"', "Append", "Creates", "End", "Kept"), ('"x"', "Create only", "Creates*", "Start", "–"),
            ('"r+"', "Read + write", "Error", "Start", "Kept"), ('"w+"', "Write + read", "Creates", "Start", "Erased"),
            ('"a+"', "Append + read", "Creates", "End", "Kept")]
    y = 58
    for i, r in enumerate(rows):
        b += f'<rect x="8" y="{y}" width="344" height="22" fill="{"#F6F0FE" if i % 2 == 0 else "#fff"}"/>'
        for j, (x, c) in enumerate(zip(xs, r)):
            col = PYB if j == 0 else (RED if c in ("Error", "Erased") else (GREEN if c in ("Creates", "Kept") else INK))
            b += text(x, y + 11, c, 10.2 if j == 0 else 9.8, anchor="start", mono=j == 0, weight="bold" if j in (0, 4) or c == "Error" else "normal", color=col)
        y += 22
    notes = ['*"x" raises FileExistsError if the file already exists.', 'Add "b" for binary files: "rb", "wb", "ab".',
             'Add "t" for text (default): "rt" = "r".', 'Missing file in "r" mode → FileNotFoundError']
    for i, s in enumerate(notes):
        b += text(180, y + 18 + i * 15, s, 9.8, color="#444")
    return svg(360, y + 18 + 4 * 15, b)


# ------------------------------------------------------------------ 6. file handling steps
def file_flow():
    b = title("Steps of File Handling")
    b += terminal(110, 50, "Start")
    b += down(110, 66, 82)
    b += process(110, 102, 'f = open("a.txt", "r")', 196, 36, 10.5, mono=True)
    b += text(110, 132, "1. Open: get a file object", 9.6, color="#666")
    b += down(110, 138, 154)
    b += process(110, 176, "f.read() / f.write(s)", 196, 36, 10.5, mono=True)
    b += text(110, 206, "2. Read or write data", 9.6, color="#666")
    b += down(110, 212, 228)
    b += process(110, 248, "f.close()", 196, 36, 10.5, mono=True)
    b += text(110, 278, "3. Close: save + free resources", 9.6, color="#666")
    b += down(110, 284, 300)
    b += terminal(110, 316, "End")
    b += box(222, 72, 130, 236, GREENF, GREEN, 8)
    lines = ["Better: with", "", "with open(", ' "a.txt") as f:', "    data = f.read()", "", "File is closed", "automatically,", "even if an error", "occurs.",
             "", "No close() needed."]
    for i, s in enumerate(lines):
        mono = i in (2, 3, 4)
        b += text(230, 92 + i * 17, sp(s), 9.8 if mono else 10.2, anchor="start", mono=mono, weight="bold" if i in (0, 11) else "normal",
                  color=GREEN if i in (0, 11) else (PYB if mono else INK))
    return svg(360, 340, b)


# ------------------------------------------------------------------ 7. read methods
def read_methods():
    b = title("read() vs readline() vs readlines()")
    b += text(14, 40, "notes.txt", 10.5, anchor="start", weight="bold", color=P)
    b += box(14, 48, 150, 62, "#fff", "#999", 4)
    for i, s in enumerate(["Python↵", "is easy↵", "Bye"]):
        b += text(22, 62 + i * 18, s, 10.5, anchor="start", mono=True)
    b += text(176, 56, "↵ = newline character \\n", 9.6, anchor="start", color="#666")
    b += text(176, 74, "Each call moves the file", 9.6, anchor="start", color="#666")
    b += text(176, 90, "pointer forward.", 9.6, anchor="start", color="#666")
    rows = [("f.read()", "'Python\\nis easy\\nBye'", "whole file → one str"), ("f.read(4)", "'Pyth'", "first 4 characters"),
            ("f.readline()", "'Python\\n'", "one line (with \\n)"), ("f.readline()  (again)", "'is easy\\n'", "next line"),
            ("f.readlines()", "['Python\\n', 'is easy\\n', 'Bye']", "list of all lines"),
            ("for line in f:", "one line per loop", "memory-efficient"), ("At end of file", "read() → ''", "empty string")]
    y = 124
    for i, (m, r, n) in enumerate(rows):
        b += f'<rect x="8" y="{y}" width="344" height="34" fill="{"#F6F0FE" if i % 2 == 0 else "#fff"}"/>'
        b += text(14, y + 10, m, 10.2, anchor="start", mono=True, weight="bold", color=PYB)
        b += text(346, y + 10, n, 9.2, anchor="end", color="#666")
        b += text(24, y + 25, sp("→ " + r), 9.8, anchor="start", mono=True, color=GREEN)
        y += 34
    b += text(180, y + 14, "Each call above is on a freshly opened file, except 'again'.", 9.4, color="#444")
    return svg(360, y + 24, b)


# ------------------------------------------------------------------ 8. function anatomy
def func_anatomy():
    b = title("Defining and Calling a Function")
    code = [("def", " add(a, b):", "#C2185B"), ("", '    """Return sum."""', "#777"), ("", "    s = a + b", INK), ("", "    return s", INK)]
    b += box(30, 40, 300, 92, "#1E1530", "#1E1530", 8)
    ys = [62, 82, 102, 122]
    b += text(46, 62, "def", 12, anchor="start", mono=True, weight="bold", color="#FF79C6")
    b += text(78, 62, sp("add(a, b):"), 12, anchor="start", mono=True, weight="bold", color="#EDE7F6")
    b += text(46, 82, sp('    """Return sum."""'), 11, anchor="start", mono=True, color="#9E9E9E")
    b += text(46, 102, sp("    s = a + b"), 12, anchor="start", mono=True, color="#EDE7F6")
    b += text(46, 122, sp("    return s"), 12, anchor="start", mono=True, color="#EDE7F6")
    ann = [(57, 154, "keyword", "#C2185B"), (89, 170, "name", BLUE), (122, 154, "parameters", GREEN), (147, 170, "colon", ORANGE)]
    for x, ly, s_, c in ann:
        b += line(f"M{x} 136 V{ly - 9}", c, 1.4) + text(x + {"colon": 14, "parameters": 14}.get(s_, 0), ly, s_, 9.6, color=c, weight="bold")
    b += text(270, 82, "docstring", 9.6, color="#ccc")
    b += text(270, 104, "body (indented)", 9.6, color="#ccc")
    b += text(270, 124, "result sent back", 9.6, color="#ccc")
    b += text(180, 198, "Calling the function", 12, weight="bold", color=P)
    b += box(60, 210, 240, 34, YEL, YELS, 8) + text(180, 227, sp("total = add(10, 20)"), 12, mono=True, weight="bold")
    b += text(150, 262, "arguments: a = 10, b = 20", 10, color=GREEN, weight="bold")
    steps = ["1. Control jumps into add() with a = 10, b = 20", "2. Body runs: s = 30", "3. return s sends 30 back to the caller",
             "4. total = 30; execution continues after the call"]
    for i, s in enumerate(steps):
        b += text(30, 288 + i * 17, s, 10, anchor="start", color=INK)
    b += text(180, 364, "Parameter = variable in the definition; argument = value in the call.", 9.4, color="#666")
    return svg(360, 376, b)


# ------------------------------------------------------------------ 9. recursion
def recursion():
    b = title("Recursion: fact(4)")
    b += text(180, 38, sp("def fact(n):  if n == 1: return 1;  return n * fact(n-1)"), 8.8, mono=True, color="#444")
    calls = ["fact(4)", "fact(3)", "fact(2)", "fact(1)"]
    rets = ["4 * fact(3)", "3 * fact(2)", "2 * fact(1)", "return 1"]
    vals = ["24", "6", "2", "1"]
    for i in range(4):
        x, y = 20 + i * 26, 56 + i * 50
        base = i == 3
        b += box(x, y, 170, 34, ORANGEF if base else BLUEF, ORANGE if base else BLUE, 6)
        b += text(x + 10, y + 17, calls[i], 11, anchor="start", mono=True, weight="bold")
        b += text(x + 164, y + 17, rets[i], 10, anchor="end", mono=True, color=RED if base else INK)
        if i < 3:
            b += arr([(x + 40, y + 34), (x + 40, y + 50 + 0)], BLUE)
            b += text(x + 50, y + 44, "call", 8.8, anchor="start", color=BLUE)
        rx = 300
        if i > 0:
            pass
    # return path on the right
    for i in range(3, 0, -1):
        y1 = 56 + i * 50 + 17
        y0 = 56 + (i - 1) * 50 + 17
        x = 20 + i * 26 + 170
        b += arr([(x, y1), (x + 30 + (3 - i) * 0, y1), (x + 30, y0), (x - 26 + 4, y0)], GREEN)
        b += text(x + 36, (y0 + y1) / 2, "returns " + vals[i], 9.4, anchor="start", color=GREEN, weight="bold")
    b += text(180, 268, sp("Result: 4 * 3 * 2 * 1 = 24"), 12, mono=True, weight="bold", color=P)
    notes = [("Base case", "stops the recursion (n == 1)", ORANGE), ("Recursive case", "calls itself with a smaller n", BLUE),
             ("No base case", "RecursionError (max depth ≈ 1000)", RED)]
    for i, (a, c, col) in enumerate(notes):
        b += text(20, 294 + i * 17, a + ":", 10.2, anchor="start", weight="bold", color=col)
        b += text(128, 294 + i * 17, c, 10, anchor="start", color=INK)
    return svg(360, 340, b)


# ------------------------------------------------------------------ 10. scope
def scope():
    b = title("Scope of Variables: Local and Global")
    b += box(14, 34, 332, 214, BLUEF, BLUE, 10)
    b += text(26, 52, "Global scope (whole program)", 10.5, anchor="start", weight="bold", color=BLUE)
    b += text(26, 74, sp("x = 10          # global"), 11, anchor="start", mono=True, weight="bold")
    b += box(30, 88, 300, 98, GREENF, GREEN, 8)
    b += text(40, 104, "Local scope of show()", 10, anchor="start", weight="bold", color=GREEN)
    b += text(40, 124, sp("def show():"), 11, anchor="start", mono=True, weight="bold", color="#C2185B")
    b += text(40, 142, sp("    y = 5      # local"), 11, anchor="start", mono=True)
    b += text(40, 160, sp("    print(x, y)  # 10 5"), 11, anchor="start", mono=True)
    b += text(40, 176, sp("    (can READ global x)"), 9.4, anchor="start", color="#666")
    b += text(26, 206, sp("show()"), 11, anchor="start", mono=True)
    b += text(26, 226, sp("print(y)        # NameError"), 11, anchor="start", mono=True, color=RED, weight="bold")
    b += text(26, 242, sp("(local y does not exist outside)"), 9.4, anchor="start", color="#666")
    b += text(180, 272, "To CHANGE a global inside a function:", 10.5, weight="bold", color=P)
    b += box(60, 282, 240, 76, "#1E1530", "#1E1530", 8)
    for i, s in enumerate(["count = 0", "def inc():", "    global count", "    count += 1"]):
        b += text(76, 298 + i * 17, sp(s), 10.8, anchor="start", mono=True, color="#FFD54F" if "global" in s else "#EDE7F6",
                  weight="bold" if "global" in s else "normal")
    b += text(180, 376, "Without global → UnboundLocalError", 10, color=RED, weight="bold")
    b += text(180, 392, "Name lookup order: Local → Enclosing → Global → Built-in", 9.6, color="#444")
    return svg(360, 404, b)


DIAGRAMS = {"py4_func_types": func_types, "py4_conversion": conversion, "py4_str_is": str_is, "py4_align": align,
            "py4_file_modes": file_modes, "py4_file_flow": file_flow, "py4_read_methods": read_methods,
            "py4_func_anatomy": func_anatomy, "py4_recursion": recursion, "py4_scope": scope}

if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    for k, f in DIAGRAMS.items():
        with open(os.path.join(OUT, k + ".svg"), "w", encoding="utf-8") as fh:
            fh.write(f())
    print("written", len(DIAGRAMS))
