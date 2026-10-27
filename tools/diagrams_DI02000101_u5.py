"""DI02000101 Scripting Language (Python) - Unit 5 concept diagrams (modules, packages, Matplotlib, NumPy).
The Matplotlib output plots (py5_out_*) are produced by the programs themselves (see content_DI02000101_u5_programs.py)."""
import os
from flowchart_lib import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "content", "computer", "sem2", "DI02000101", "diagrams")
CELL = "#F5EEFD"; BLUE = "#1565C0"; BLUEF = "#E3F0FC"; GREEN = "#2E7D32"; GREENF = "#E3F5E6"
ORANGE = "#E07B00"; ORANGEF = "#FFF1DE"; RED = "#C62828"; REDF = "#FDECEC"; YEL = "#FFF6D6"; YELS = "#B88A00"
PYB = "#306998"; DARK = "#1E1530"
NB = "\u00a0"


def box(x, y, w, h, fill=CELL, stroke=P, rx=6, sw=1.5):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>'


def sp(s):
    return s.replace(" ", NB)


def code(x, y, lines, size=10.2, lh=15, color="#EDE7F6"):
    o = ""
    for i, s in enumerate(lines):
        c = "#9E9E9E" if s.strip().startswith("#") else ("#FF79C6" if s.startswith(("def", "import", "from")) else color)
        o += text(x, y + i * lh, sp(s), size, anchor="start", mono=True, color=c)
    return o


def grid(x, y, vals, cw=34, ch=26, hl=None, hlf=YEL, hls=YELS, fill=BLUEF, st=BLUE, size=11):
    o = ""
    for r, row in enumerate(vals):
        for c, v in enumerate(row):
            on = hl and (r, c) in hl
            o += box(x + c * cw, y + r * ch, cw, ch, hlf if on else fill, hls if on else st, 0, 1.2)
            o += text(x + c * cw + cw / 2, y + r * ch + ch / 2, str(v), size, mono=True, weight="bold")
    return o


# ------------------------------------------------------------------ 1. module concept
def module():
    b = title("Module: Write Once, Import Anywhere")
    b += box(14, 40, 158, 150, DARK, DARK, 8)
    b += text(22, 56, "mymath.py  (module)", 10, anchor="start", weight="bold", color="#FFD54F")
    b += code(22, 76, ["PI = 3.14159", "", "def add(a, b):", "    return a + b", "", "def factorial(n):", "    ..."], 9.8)
    b += box(188, 40, 158, 150, DARK, DARK, 8)
    b += text(196, 56, "main.py  (same folder)", 10, anchor="start", weight="bold", color="#FFD54F")
    b += code(196, 76, ["import mymath", "", "mymath.add(2, 3)", "mymath.PI", "", "from mymath import add", "add(2, 3)"], 9.8)
    b += arr([(172, 115), (186, 115)], ORANGE)
    b += text(180, 212, "Types of modules", 11.5, weight="bold", color=P)
    types = [("Built-in", "math, random, os, sys", BLUEF, BLUE), ("User-defined", "your own .py files", GREENF, GREEN),
             ("Third-party", "numpy, matplotlib (pip)", ORANGEF, ORANGE)]
    for i, (n, e, f, s_) in enumerate(types):
        x = 14 + i * 113
        b += box(x, 222, 106, 46, f, s_, 8) + text(x + 53, 238, n, 10.5, weight="bold", color=s_) + text(x + 53, 256, e, 8.6, color="#444")
    b += text(180, 290, "Module search order: current folder → PYTHONPATH →", 9.6, color="#444")
    b += text(180, 305, "standard library → site-packages (see sys.path)", 9.6, color="#444")
    return svg(360, 316, b)


# ------------------------------------------------------------------ 2. import forms
def import_forms():
    b = title("Ways to Import")
    rows = [("import math", "math.sqrt(9)", "whole module"), ("import math as m", "m.sqrt(9)", "module with alias"),
            ("from math import sqrt", "sqrt(9)", "one name"), ("from math import sqrt, pi", "sqrt(9), pi", "listed names"),
            ("from math import *", "sqrt(9), floor(2.5)", "all public names"), ("from math import sqrt as r", "r(9)", "name with alias")]
    y = 36
    for i, (a, u, w) in enumerate(rows):
        b += f'<rect x="8" y="{y}" width="344" height="38" fill="{"#F6F0FE" if i % 2 == 0 else "#fff"}"/>'
        b += text(14, y + 12, sp(a), 10.5, anchor="start", mono=True, weight="bold", color=PYB)
        b += text(346, y + 12, w, 9.2, anchor="end", color="#666")
        b += text(28, y + 28, sp("use: " + u), 9.8, anchor="start", mono=True, color=GREEN)
        y += 38
    notes = ["import X: names need the prefix X. (no name clashes)", "from X import a: use a directly (shorter code)",
             "import *: not recommended, names may overwrite others", "dir(math) lists all names in a module"]
    for i, s_ in enumerate(notes):
        b += text(180, y + 18 + i * 16, s_, 9.6, color="#444")
    return svg(360, y + 18 + 4 * 16, b)


# ------------------------------------------------------------------ 3. package tree
def package_tree():
    b = title("Package Structure")
    items = [(0, "project/", P, True), (1, "main.py", INK, False), (1, "shapes/        ← package", GREEN, True),
             (2, "__init__.py   ← marks a package", RED, False), (2, "area.py       ← module", INK, False),
             (2, "perimeter.py  ← module", INK, False), (1, "college/       ← package", GREEN, True),
             (2, "__init__.py", RED, False), (2, "student/   ← sub-package", BLUE, True), (3, "__init__.py", RED, False),
             (3, "result.py", INK, False), (2, "staff/     ← sub-package", BLUE, True), (3, "__init__.py", RED, False),
             (3, "salary.py", INK, False)]
    y = 44
    prev = {}
    for lvl, name, col, folder in items:
        x = 20 + lvl * 26
        if lvl > 0:
            px, py = prev[lvl - 1]
            b += line(f"M{px + 6} {py + 7} V{y} H{x - 4}", "#B9A3DC", 1.2)
        if folder:
            b += (f'<path d="M{x} {y - 5} h5 l2 2 h7 v9 h-14 z" fill="{YEL}" stroke="{YELS}" stroke-width="1.1"/>')
            b += text(x + 19, y, sp(name), 10.2, anchor="start", weight="bold", color=col)
        else:
            b += text(x, y, sp(name), 10.2, anchor="start", mono=True, color=col)
        prev[lvl] = (x, y)
        y += 19
    b += box(14, y + 4, 332, 66, GREENF, GREEN, 8)
    b += text(24, y + 20, "import shapes.area", 10.2, anchor="start", mono=True, color=PYB, weight="bold")
    b += text(24, y + 37, sp("from shapes import perimeter"), 10.2, anchor="start", mono=True, color=PYB, weight="bold")
    b += text(24, y + 54, sp("from college.student.result import grade"), 9.6, anchor="start", mono=True, color=PYB, weight="bold")
    b += text(180, y + 90, "Module = one .py file;  package = folder of modules", 10, color="#444", weight="bold")
    return svg(360, y + 100, b)


# ------------------------------------------------------------------ 4. ceil / floor / trunc
def math_round():
    b = title("ceil(), floor() and trunc() on a Number Line")
    def nline(y, lo, hi, val, up, down):
        o = line(f"M20 {y} H340", INK, 1.4)
        step = 320 / (hi - lo)
        for k in range(lo, hi + 1):
            x = 20 + (k - lo) * step
            o += line(f"M{x} {y - 5} V{y + 5}", INK, 1.2) + text(x, y + 16, str(k), 10, mono=True)
        xv = 20 + (val - lo) * step
        o += f'<circle cx="{xv}" cy="{y}" r="5" fill="{P}"/>' + text(xv, y - 40, f"x = {val}", 11, mono=True, weight="bold", color=P)
        (n1, t1), (n2, t2) = up, down
        x1, x2 = 20 + (t1 - lo) * step, 20 + (t2 - lo) * step
        o += arr([(xv, y - 14), (x1, y - 14)], GREEN) + text(x1 + (14 if x1 > xv else -14), y - 14, f"{n1} → {t1}", 9.4,
                                                           anchor="start" if x1 > xv else "end", color=GREEN, weight="bold")
        o += arr([(xv, y + 30), (x2, y + 30)], RED) + text(x2 + (14 if x2 > xv else -14), y + 30, f"{n2} → {t2}", 9.4,
                                                         anchor="start" if x2 > xv else "end", color=RED, weight="bold")
        return o
    b += nline(90, 2, 6, 4.3, ("ceil", 5), ("floor / trunc", 4))
    b += nline(190, -6, -2, -4.3, ("ceil / trunc", -4), ("floor", -5))
    rows = [("x", "4.3", "-4.3", "4.7"), ("ceil(x)", "5", "-4", "5"), ("floor(x)", "4", "-5", "4"),
            ("trunc(x)", "4", "-4", "4"), ("round(x)", "4", "-4", "5")]
    y = 238
    for i, r in enumerate(rows):
        b += f'<rect x="40" y="{y}" width="280" height="20" fill="{P if i == 0 else ("#F6F0FE" if i % 2 else "#fff")}"/>'
        for j, c in enumerate(r):
            b += text(90 + j * 70, y + 10, c, 10.2, mono=True, weight="bold", color="#fff" if i == 0 else (PYB if j == 0 else INK))
        y += 20
    b += text(180, y + 16, "ceil = up (towards +∞), floor = down (towards −∞), trunc = towards 0", 9.2, color="#444")
    return svg(360, y + 26, b)


# ------------------------------------------------------------------ 5. matplotlib anatomy
def mpl_anatomy():
    b = title("Parts of a Matplotlib Plot")
    ox, oy, w, h = 56, 64, 170, 150
    b += box(10, 36, 236, 236, "#FAFAFA", "#BBB", 6, 1)
    b += text(ox + w / 2, 52, "Title", 11, weight="bold")
    b += f'<rect x="{ox}" y="{oy}" width="{w}" height="{h}" fill="#fff" stroke="{INK}" stroke-width="1.2"/>'
    for k in range(1, 4):
        b += line(f"M{ox + k * 42.5} {oy} V{oy + h}", "#DDD", 1) + line(f"M{ox} {oy + k * 37.5} H{ox + w}", "#DDD", 1)
    pts = [(0, 30), (42.5, 70), (85, 55), (127.5, 110), (170, 95)]
    d = "M" + " L".join(f"{ox + x} {oy + h - y}" for x, y in pts)
    b += f'<path d="{d}" fill="none" stroke="{P}" stroke-width="2"/>'
    for x, y in pts:
        b += f'<circle cx="{ox + x}" cy="{oy + h - y}" r="3.5" fill="{P}"/>'
    for k in range(5):
        b += text(ox + k * 42.5, oy + h + 12, str(k + 1), 9, mono=True)
        b += text(ox - 6, oy + h - k * 37.5, str(k * 10), 9, mono=True, anchor="end")
    b += box(ox + 8, oy + 8, 58, 20, "#fff", "#999", 3, 1)
    b += line(f"M{ox + 13} {oy + 18} H{ox + 27}", P, 2) + text(ox + 31, oy + 18, "sales", 9, anchor="start")
    b += text(ox + w / 2, oy + h + 30, "X label", 10)
    yl = (ox - 34, oy + h / 2)
    b += f'<text x="{yl[0]}" y="{yl[1]}" font-size="10" text-anchor="middle" dominant-baseline="middle" font-family="DejaVu Sans" transform="rotate(-90 {yl[0]} {yl[1]})">Y label</text>'
    ann = [("plt.title()", (ox + w / 2 + 18, 52), 52), ("plt.legend()", (ox + 66, oy + 18), 84),
           ("plt.grid()", (ox + 127, oy + 20), 116), ("plt.plot(x, y)", (ox + 106, oy + 80), 148),
           ("plt.ylabel()", (yl[0] + 6, yl[1] + 30), 184), ("plt.xticks()", (ox + w, oy + h + 12), 216),
           ("plt.xlabel()", (ox + w / 2 + 24, oy + h + 30), 244)]
    for lab, (px, py), ly in ann:
        b += line(f"M{px} {py} L256 {ly}", ORANGE, 1) + text(260, ly, lab, 9.4, anchor="start", mono=True, color=ORANGE, weight="bold")
    b += text(180, 290, "Figure = whole window;  Axes = the plotting area", 9.8, color="#444", weight="bold")
    b += text(180, 306, sp("plt.show() displays it;  plt.savefig(\"a.png\") saves it"), 9.8, color="#444")
    return svg(360, 316, b)


# ------------------------------------------------------------------ 6. numpy array attributes
def np_array():
    b = title("NumPy Arrays and Their Attributes")
    b += text(60, 44, "1-D", 11, weight="bold", color=BLUE)
    b += grid(18, 54, [[10, 20, 30, 40]], 22, 24, size=9.5)
    b += text(62, 96, "shape (4,)", 9.4, mono=True) + text(62, 110, "ndim 1, size 4", 9.4, mono=True)
    b += text(180, 44, "2-D", 11, weight="bold", color=GREEN)
    b += grid(141, 54, [[1, 2, 3], [4, 5, 6]], 26, 22, fill=GREENF, st=GREEN, size=9.5)
    b += text(180, 116, "shape (2, 3)", 9.4, mono=True) + text(180, 130, "ndim 2, size 6", 9.4, mono=True)
    b += text(298, 44, "3-D", 11, weight="bold", color=ORANGE)
    b += grid(278, 66, [[5, 6], [7, 8]], 22, 20, fill="#FFE9CC", st=ORANGE, size=9)
    b += grid(266, 56, [[1, 2], [3, 4]], 22, 20, fill=ORANGEF, st=ORANGE, size=9)
    b += text(298, 124, "shape (2, 2, 2)", 9.4, mono=True) + text(298, 138, "ndim 3, size 8", 9.4, mono=True)
    rows = [("a.shape", "dimensions as a tuple", "(2, 3)"), ("a.ndim", "number of dimensions (axes)", "2"),
            ("a.size", "total number of elements", "6"), ("a.dtype", "data type of elements", "int64"),
            ("a.itemsize", "bytes per element", "8"), ("a.nbytes", "total bytes = size × itemsize", "48")]
    b += text(180, 162, sp("a = np.array([[1, 2, 3], [4, 5, 6]])"), 10.2, mono=True, weight="bold", color=P)
    y = 172
    for i, (a, d, v) in enumerate(rows):
        b += f'<rect x="8" y="{y}" width="344" height="21" fill="{"#F6F0FE" if i % 2 == 0 else "#fff"}"/>'
        b += text(14, y + 10.5, a, 10.2, anchor="start", mono=True, weight="bold", color=PYB)
        b += text(100, y + 10.5, d, 9.6, anchor="start")
        b += text(346, y + 10.5, v, 10, anchor="end", mono=True, weight="bold", color=GREEN)
        y += 21
    return svg(360, y + 8, b)


# ------------------------------------------------------------------ 7. numpy slicing
def np_slicing():
    b = title("Indexing and Slicing a 2-D Array")
    m = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    panels = [("m[1, 2]", "→ 7", {(1, 2)}), ("m[1]  or  m[1, :]", "→ [5 6 7 8]", {(1, c) for c in range(4)}),
              ("m[:, 2]", "→ [3 7 11]", {(r, 2) for r in range(3)}), ("m[0:2, 1:3]", "→ [[2 3] [6 7]]", {(r, c) for r in range(2) for c in range(1, 3)}),
              ("m[::2, ::3]", "→ [[1 4] [9 12]]", {(0, 0), (0, 3), (2, 0), (2, 3)}), ("m[m > 8]", "→ [9 10 11 12]", {(2, c) for c in range(4)})]
    for k, (e, r, hl) in enumerate(panels):
        c, rw = k % 2, k // 2
        ox, oy = 14 + c * 176, 40 + rw * 128
        b += text(ox + 2, oy + 10, sp(e), 10.5, anchor="start", mono=True, weight="bold", color=PYB)
        b += grid(ox + 6, oy + 20, m, 34, 22, hl=hl, size=10)
        b += text(ox + 2, oy + 104, sp(r), 9.8, anchor="start", mono=True, color=GREEN, weight="bold")
    b += text(180, 430, "Rows first, then columns: m[row, col]. Index starts at 0.", 9.8, color="#444")
    return svg(360, 442, b)


# ------------------------------------------------------------------ 8. axis
def np_axis():
    b = title("axis in NumPy Functions")
    m = [[78, 85, 62], [90, 71, 88], [65, 80, 75]]
    b += grid(110, 64, m, 46, 28, size=11)
    for c in range(3):
        b += arr([(133 + c * 46, 152), (133 + c * 46, 168)], GREEN)
    b += text(110, 184, sp("axis=0  (down the columns)"), 9.6, anchor="start", color=GREEN, weight="bold")
    sums0 = [233, 236, 225]
    for c in range(3):
        b += box(110 + c * 46, 192, 46, 24, GREENF, GREEN, 0, 1.2) + text(133 + c * 46, 204, str(sums0[c]), 10.5, mono=True, weight="bold")
    for r in range(3):
        b += arr([(252, 78 + r * 28), (270, 78 + r * 28)], ORANGE)
        b += box(274, 66 + r * 28, 46, 24, ORANGEF, ORANGE, 0, 1.2) + text(297, 78 + r * 28, str(sum(m[r])), 10.5, mono=True, weight="bold")
    b += text(297, 56, "axis=1", 9.6, color=ORANGE, weight="bold")
    b += text(297, 160, "(across rows)", 9.2, color=ORANGE)
    b += text(60, 78, "student 0", 9, color="#777") + text(60, 106, "student 1", 9, color="#777") + text(60, 134, "student 2", 9, color="#777")
    b += text(180, 46, "np.sum(marks, axis=…)", 10.5, mono=True, weight="bold", color=P)
    rows = [("np.sum(m)", "694  (all elements)"), ("np.sum(m, axis=0)", "[233 236 225]  per column"),
            ("np.sum(m, axis=1)", "[225 249 220]  per row"), ("np.max(m, axis=0)", "[90 85 88]"),
            ("np.mean(m, axis=1)", "[75. 83. 73.33]")]
    y = 234
    for i, (a, r) in enumerate(rows):
        b += f'<rect x="8" y="{y}" width="344" height="20" fill="{"#F6F0FE" if i % 2 == 0 else "#fff"}"/>'
        b += text(14, y + 10, a, 10, anchor="start", mono=True, weight="bold", color=PYB)
        b += text(170, y + 10, sp(r), 9.6, anchor="start", mono=True, color=GREEN)
        y += 20
    return svg(360, y + 8, b)


# ------------------------------------------------------------------ 9. dot / cross / matmul
def np_ops():
    b = title("Element-wise vs dot vs cross vs matmul")
    b += text(14, 44, sp("u = [1, 2, 3]    v = [4, 5, 6]"), 10.5, anchor="start", mono=True, weight="bold", color=P)
    rows = [("u * v", "[1×4, 2×5, 3×6] = [4 10 18]", "element-wise"), ("np.dot(u, v)", "1×4 + 2×5 + 3×6 = 32", "scalar"),
            ("np.cross(u, v)", "[2×6−3×5, 3×4−1×6, 1×5−2×4]", ""), ("", "= [-3 6 -3]", "⊥ vector")]
    y = 54
    for i, (a, r, n) in enumerate(rows):
        b += f'<rect x="8" y="{y}" width="344" height="20" fill="{"#F6F0FE" if i < 2 and i % 2 == 0 else ("#fff" if i < 2 else "#F6F0FE")}"/>'
        b += text(14, y + 10, a, 10, anchor="start", mono=True, weight="bold", color=PYB)
        b += text(112, y + 10, sp(r), 9.4, anchor="start", mono=True, color=GREEN)
        b += text(348, y + 10, n, 9, anchor="end", color="#666")
        y += 20
    y += 14
    b += text(180, y, "Matrix multiplication: np.matmul(A, B) = A @ B", 11, weight="bold", color=P)
    y += 12
    b += grid(14, y + 10, [[1, 2], [3, 4]], 30, 26, hl={(0, 0), (0, 1)}, size=11)
    b += text(44, y + 76, "A", 11, weight="bold", color=BLUE)
    b += text(84, y + 36, "@", 13, weight="bold")
    b += grid(98, y + 10, [[5, 6], [7, 8]], 30, 26, hl={(0, 0), (1, 0)}, hlf="#E3F5E6", hls=GREEN, size=11)
    b += text(128, y + 76, "B", 11, weight="bold", color=BLUE)
    b += text(170, y + 36, "=", 13, weight="bold")
    b += grid(184, y + 10, [[19, 22], [43, 50]], 34, 26, hl={(0, 0)}, hlf=ORANGEF, hls=ORANGE, size=11)
    b += text(286, y + 22, "row 0 · col 0", 9, color=ORANGE, weight="bold")
    b += text(286, y + 36, "1×5 + 2×7", 9, mono=True, color=ORANGE)
    b += text(286, y + 50, "= 19", 9, mono=True, color=ORANGE, weight="bold")
    y += 96
    notes = ["A * B = [[5 12] [21 32]]  (element-wise, NOT matrix)", "(m × n) @ (n × p) → (m × p); inner sizes must match",
             "For 2-D arrays np.dot(A, B) = np.matmul(A, B)"]
    for i, s in enumerate(notes):
        b += text(180, y + i * 16, sp(s) if i == 0 else s, 9.6, color=RED if i == 0 else "#444", weight="bold" if i == 0 else "normal")
    return svg(360, y + 3 * 16, b)


DIAGRAMS = {"py5_module": module, "py5_import_forms": import_forms, "py5_package_tree": package_tree, "py5_math_round": math_round,
            "py5_mpl_anatomy": mpl_anatomy, "py5_np_array": np_array, "py5_np_slicing": np_slicing, "py5_np_axis": np_axis,
            "py5_np_ops": np_ops}

if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    for k, f in DIAGRAMS.items():
        with open(os.path.join(OUT, k + ".svg"), "w", encoding="utf-8") as fh:
            fh.write(f())
    print("written", len(DIAGRAMS))
