"""DI03000021 Data Structures - Unit 1 diagrams (360-wide SVG, no CSS/markers)."""
import math, os
from flowchart_lib import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "content", "computer", "sem3", "DI03000021", "diagrams")
CELL = "#F5EEFD"; BLUE = "#1565C0"; BLUEF = "#E3F0FC"; GREEN = "#2E7D32"; GREENF = "#E3F5E6"
ORANGE = "#E07B00"; ORANGEF = "#FFF1DE"; RED = "#C62828"; REDF = "#FDECEC"; YEL = "#FFF6D6"; YELS = "#B88A00"
TEAL = "#00796B"; TEALF = "#E0F2F1"; GREY_F = "#F2F2F2"


def box(x, y, w, h, fill=CELL, stroke=P, rx=6, sw=1.5):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>'


def cells(x, y, vals, w=38, h=30, fill="#fff", stroke=P, hi=None, hifill=YEL, size=12, mono=True):
    """Row of array cells. hi = set of indexes to highlight."""
    b = ""
    for i, v in enumerate(vals):
        f = hifill if hi and i in hi else fill
        b += box(x + i * w, y, w, h, f, stroke, 0, 1.4)
        if v != "":
            b += text(x + i * w + w / 2, y + h / 2, str(v), size, mono=mono, weight="bold")
    return b


# ------------------------------------------------------------------ 1. data -> information
def data_info():
    b = title("Data, Processing and Information")
    b += box(10, 40, 100, 120, BLUEF, BLUE, 8)
    b += text(60, 56, "DATA", 12.5, weight="bold", color=BLUE)
    for i, s in enumerate(["Ravi  67", "Meena 82", "Amit  45", "Sara  91"]):
        b += text(60, 80 + i * 18, s, 10.5, mono=True)
    b += box(130, 72, 100, 56, ORANGEF, ORANGE, 8)
    b += text(180, 92, "PROCESSING", 11, weight="bold", color=ORANGE)
    b += text(180, 110, "sort, average,", 9.6, color="#444") + text(180, 122, "compare", 9.6, color="#444")
    b += arr([(110, 100), (128, 100)]) + arr([(230, 100), (248, 100)])
    b += box(250, 40, 100, 120, GREENF, GREEN, 8)
    b += text(300, 56, "INFORMATION", 11, weight="bold", color=GREEN)
    for i, s in enumerate(["Topper: Sara", "Average: 71.25", "Passed: 4", "Highest: 91"]):
        b += text(300, 80 + i * 18, s, 9.8)
    b += text(180, 182, "Raw facts (data) have no meaning by themselves.", 10, color="#444")
    b += text(180, 198, "Processed, meaningful data = information.", 10, color="#444", weight="bold")
    b += text(180, 222, "A data structure decides HOW the data is stored", 10, color=P)
    b += text(180, 237, "so that processing becomes fast and easy.", 10, color=P)
    return svg(360, 252, b)


# ------------------------------------------------------------------ 2. classification tree
def classification():
    b = title("Classification of Data Structures")
    b += rbox(180, 50, 150, 32, "Data Structure", P, P, 12.5, "bold", "#fff")
    b += line("M180 66 V82 M90 82 H270 M90 82 V96 M270 82 V96")
    b += rbox(90, 114, 140, 36, "Primitive", BLUEF, BLUE, 12, "bold", BLUE)
    b += rbox(270, 114, 140, 36, "Non-Primitive", ORANGEF, ORANGE, 12, "bold", ORANGE)
    for i, s in enumerate(["int", "float", "char", "double", "pointer"]):
        y = 150 + i * 26
        b += line(f"M30 132 V{y + 11} H40", BLUE, 1.4)
        b += rbox(85, y + 11, 90, 22, s, "#fff", BLUE, 11, mono=True)
    b += line("M270 132 V148 M215 148 H325 M215 148 V160 M325 148 V160", ORANGE, 1.6)
    b += rbox(215, 176, 92, 32, "Linear", YEL, YELS, 11.5, "bold")
    b += rbox(325, 176, 64, 32, "Non-\nLinear", TEALF, TEAL, 10.5, "bold")
    for i, s in enumerate(["Array", "Stack", "Queue", "Linked List"]):
        y = 206 + i * 26
        b += line(f"M178 192 V{y + 11} H186", YELS, 1.4)
        b += rbox(222, y + 11, 72, 22, s, "#fff", YELS, 10.5)
    for i, s in enumerate(["Tree", "Graph"]):
        y = 206 + i * 26
        b += line(f"M300 192 V{y + 11} H306", TEAL, 1.4)
        b += rbox(327, y + 11, 42, 22, s, "#fff", TEAL, 10)
    b += text(85, 300, "Directly operated by", 9.6, color="#555") + text(85, 313, "machine instructions", 9.6, color="#555")
    b += text(255, 330, "Built from primitive types", 9.6, color="#555")
    return svg(360, 344, b)


# ------------------------------------------------------------------ 3. linear vs non-linear
def linear_nonlinear():
    b = title("Linear vs Non-Linear Data Structure")
    b += text(180, 42, "LINEAR: elements in a sequence (one after another)", 10.5, weight="bold", color=YELS)
    b += cells(40, 54, [10, 20, 30, 40, 50, 60, 70], 40, 30, YEL, YELS)
    b += text(180, 98, "Array: each element has one predecessor and one successor", 9.6, color="#555")
    x0 = 22
    for i, v in enumerate([10, 20, 30]):
        x = x0 + i * 108
        b += box(x, 112, 56, 28, "#fff", YELS, 4) + line(f"M{x + 38} 112 V140", YELS, 1.2)
        b += text(x + 19, 126, str(v), 12, mono=True, weight="bold")
        if i < 2:
            b += f'<circle cx="{x + 47}" cy="126" r="3" fill="{INK}"/>' + arr([(x + 47, 126), (x + 106, 126)])
        else:
            b += text(x + 47, 126, "X", 10, color=RED, weight="bold")
    b += text(180, 154, "Linked list: nodes joined in a single line", 9.6, color="#555")
    b += line("M10 168 H350", "#DDD", 1)
    b += text(180, 184, "NON-LINEAR: elements in a hierarchy / network", 10.5, weight="bold", color=TEAL)
    # tree
    nodes = {"A": (90, 210), "B": (55, 252), "C": (125, 252), "D": (35, 294), "E": (75, 294), "F": (125, 294)}
    for a, c in [("A", "B"), ("A", "C"), ("B", "D"), ("B", "E"), ("C", "F")]:
        b += line(f"M{nodes[a][0]} {nodes[a][1]} L{nodes[c][0]} {nodes[c][1]}", TEAL, 1.6)
    for k, (x, y) in nodes.items():
        b += f'<circle cx="{x}" cy="{y}" r="13" fill="{TEALF}" stroke="{TEAL}" stroke-width="1.6"/>' + text(x, y, k, 11.5, weight="bold")
    b += text(90, 322, "Tree (hierarchy)", 10, weight="bold", color=TEAL)
    # graph
    g = {"1": (230, 214), "2": (310, 214), "3": (200, 268), "4": (270, 296), "5": (330, 266)}
    for a, c in [("1", "2"), ("1", "3"), ("1", "4"), ("2", "5"), ("3", "4"), ("4", "5"), ("2", "4")]:
        b += line(f"M{g[a][0]} {g[a][1]} L{g[c][0]} {g[c][1]}", TEAL, 1.6)
    for k, (x, y) in g.items():
        b += f'<circle cx="{x}" cy="{y}" r="13" fill="{TEALF}" stroke="{TEAL}" stroke-width="1.6"/>' + text(x, y, k, 11.5, weight="bold")
    b += text(268, 322, "Graph (network)", 10, weight="bold", color=TEAL)
    return svg(360, 336, b)


# ------------------------------------------------------------------ 4. operations on data structures
def operations():
    b = title("Operations on Data Structures")
    ops = [("Traversing", "visit every element once", BLUEF, BLUE), ("Searching", "find location of a value", GREENF, GREEN),
           ("Insertion", "add a new element", YEL, YELS), ("Deletion", "remove an element", REDF, RED),
           ("Sorting", "arrange in an order", ORANGEF, ORANGE), ("Merging", "combine two structures", TEALF, TEAL)]
    for i, (h, s, f, st) in enumerate(ops):
        c, r = i % 2, i // 2
        x, y = 12 + c * 172, 36 + r * 56
        b += box(x, y, 164, 48, f, st, 8)
        b += f'<circle cx="{x + 17}" cy="{y + 24}" r="10" fill="{st}"/>' + text(x + 17, y + 24, str(i + 1), 10.5, color="#fff", weight="bold")
        b += text(x + 34, y + 17, h, 11.5, anchor="start", weight="bold")
        b += text(x + 34, y + 33, s, 9.6, anchor="start", color="#555")
    b += text(180, 36 + 3 * 56 + 10, "The choice of data structure decides how fast", 10, color=P)
    b += text(180, 36 + 3 * 56 + 25, "each of these operations can be done.", 10, color=P)
    return svg(360, 36 + 3 * 56 + 38, b)


# ------------------------------------------------------------------ 5. characteristics of algorithm
def characteristics():
    b = title("Characteristics of an Algorithm")
    b += f'<circle cx="180" cy="150" r="44" fill="{P}"/>' + text(180, 150, "Algorithm", 12.5, color="#fff", weight="bold")
    items = [("Input", "zero or more", BLUE, BLUEF), ("Output", "at least one", GREEN, GREENF),
             ("Definiteness", "clear, unambiguous", ORANGE, ORANGEF), ("Finiteness", "ends after finite steps", RED, REDF),
             ("Effectiveness", "basic, do-able steps", TEAL, TEALF)]
    for i, (h, s, st, f) in enumerate(items):
        a = math.radians(-90 + i * 72)
        cx, cy = 180 + 118 * math.cos(a), 150 + 100 * math.sin(a)
        b += line(f"M{180 + 44 * math.cos(a):.1f} {150 + 44 * math.sin(a):.1f} L{cx - 50 * math.cos(a) * 0.6:.1f} {cy - 22 * math.sin(a):.1f}", st, 1.6, "4 3")
        b += box(cx - 58, cy - 21, 116, 42, f, st, 10, 1.7)
        b += text(cx, cy - 7, h, 11.5, weight="bold", color=st) + text(cx, cy + 9, s, 9.6, color="#444")
    return svg(360, 284, b)


# ------------------------------------------------------------------ 6. growth rates
def growth():
    b = title("Growth of Common Time Complexities")
    ox, oy, W, H = 44, 270, 290, 220
    b += line(f"M{ox} {oy - H - 6} V{oy + 12} H{ox + W + 6}", INK, 1.6)
    b += arrowhead(ox, oy - H - 8, -90) + arrowhead(ox + W + 8, oy + 12, 0)
    b += text(ox + W, oy + 26, "n (input size)", 10, anchor="end", color="#444")
    b += f'<text x="14" y="{oy - H / 2}" font-size="10" fill="#444" text-anchor="middle" transform="rotate(-90 14 {oy - H / 2})">time (steps)</text>'
    nmax, ymax = 16.0, 64.0
    curves = [("O(1)", lambda n: 2, GREEN), ("O(log n)", lambda n: math.log2(n) if n > 1 else 0, TEAL),
              ("O(n)", lambda n: n, BLUE), ("O(n log n)", lambda n: n * math.log2(n) if n > 1 else 0, ORANGE),
              ("O(n²)", lambda n: n * n, RED), ("O(2ⁿ)", lambda n: 2 ** n, "#6A1B9A")]
    for name, f, col in curves:
        pts = []
        n = 1.0
        while n <= nmax:
            v = f(n)
            if v > ymax:
                break
            pts.append((ox + n / nmax * W, oy - v / ymax * H))
            n += 0.1
        b += line("M" + " L".join(f"{x:.1f} {y:.1f}" for x, y in pts), col, 2.2)
        lx, ly = pts[-1]
        dy = {"O(1)": 8, "O(log n)": -10}.get(name, -6)
        b += text(min(lx + 3, 350), max(ly + dy, 40), name, 10.5, anchor="end" if lx > 300 else "start", color=col, weight="bold")
    b += text(180, oy + 44, "O(1) < O(log n) < O(n) < O(n log n) < O(n²) < O(2ⁿ)", 10.2, weight="bold", color=P)
    b += text(180, oy + 60, "lower curve = faster algorithm for large n", 9.6, color="#555")
    return svg(360, oy + 72, b)


# ------------------------------------------------------------------ 7. asymptotic notations
def asymptotic():
    b = title("Asymptotic Notations: O, Ω, Θ")
    panels = [("Big O : upper bound", "f(n) ≤ c·g(n) for n ≥ n₀", RED, "worst case"),
              ("Big Ω : lower bound", "f(n) ≥ c·g(n) for n ≥ n₀", GREEN, "best case"),
              ("Big Θ : tight bound", "c₁·g(n) ≤ f(n) ≤ c₂·g(n)", BLUE, "average / exact")]
    y0 = 34
    for k, (h, cond, col, case) in enumerate(panels):
        y = y0 + k * 128
        b += box(8, y, 344, 120, "#FCFAFF", "#D9C8F0", 8, 1)
        b += text(18, y + 14, h, 11.5, anchor="start", weight="bold", color=col)
        b += text(18, y + 30, cond, 10, anchor="start", mono=True)
        b += text(18, y + 46, "(" + case + ")", 9.6, anchor="start", color="#555")
        ox, oy, W, H = 190, y + 108, 150, 88
        b += line(f"M{ox} {oy - H} V{oy} H{ox + W}", INK, 1.3)
        n0 = ox + 52
        b += line(f"M{n0} {oy} V{oy - H + 6}", "#999", 1, "3 3") + text(n0, oy + 8, "n₀", 9.5, color="#555")
        f = lambda t: 20 + 46 * t + 10 * math.sin(t * 9)    # wavy f(n)
        def path(fn):
            return "M" + " L".join(f"{ox + t * W:.1f} {oy - fn(t):.1f}" for t in [i / 40 for i in range(41)])
        b += line(path(f), INK, 2)
        if k == 0:
            b += line(path(lambda t: 14 + 72 * t), col, 2, "6 3")
            b += text(ox + W - 2, oy - 86, "c·g(n)", 9.6, anchor="end", color=col, weight="bold")
        elif k == 1:
            b += line(path(lambda t: 4 + 40 * t), col, 2, "6 3")
            b += text(ox + W - 2, oy - 30, "c·g(n)", 9.6, anchor="end", color=col, weight="bold")
        else:
            b += line(path(lambda t: 14 + 72 * t), col, 2, "6 3") + line(path(lambda t: 4 + 40 * t), col, 2, "6 3")
            b += text(ox + W - 2, oy - 86, "c₂·g(n)", 9.6, anchor="end", color=col, weight="bold")
            b += text(ox + W - 2, oy - 30, "c₁·g(n)", 9.6, anchor="end", color=col, weight="bold")
        b += text(ox + 26, oy - f(0.16) - 9, "f(n)", 9.6, color=INK, weight="bold")
    return svg(360, y0 + 3 * 128, b)


# ------------------------------------------------------------------ 8. 1-D array in memory
def array_memory():
    b = title("One-Dimensional Array in Memory")
    b += text(180, 40, "int A[6] = {15, 7, 42, 9, 23, 31};", 11, mono=True, color=P, weight="bold")
    x0 = 30
    vals = [15, 7, 42, 9, 23, 31]
    b += cells(x0, 62, vals, 50, 34, "#fff", P, {2}, YEL, 13)
    for i in range(6):
        b += text(x0 + i * 50 + 25, 56 - 2, f"A[{i}]", 9.6, mono=True, color="#555")
        b += text(x0 + i * 50 + 25, 108, str(1000 + 4 * i), 10, mono=True, color=BLUE, weight="bold")
    b += text(x0 - 4, 108, "", 9)
    b += text(180, 126, "address (each int = 4 bytes, base = 1000)", 9.6, color=BLUE)
    b += box(16, 142, 328, 76, BLUEF, BLUE, 8)
    b += text(180, 160, "Address of A[i] = Base + w × (i − LB)", 11.5, weight="bold", mono=True, color=BLUE)
    b += text(180, 180, "w = size of one element, LB = lower bound (0 in C)", 9.6, color="#333")
    b += text(180, 200, "A[2] → 1000 + 4 × (2 − 0) = 1008", 11, mono=True, weight="bold", color=GREEN)
    b += text(180, 238, "Contiguous memory: any element can be reached", 10, color="#444")
    b += text(180, 253, "directly by its index (random access, O(1)).", 10, color="#444")
    return svg(360, 266, b)


# ------------------------------------------------------------------ 9. row major vs column major
def row_col_major():
    b = title("Row Major vs Column Major (2 × 3)")
    vals = [["a", "b", "c"], ["d", "e", "f"]]
    x0, y0 = 120, 40
    for r in range(2):
        for c in range(3):
            b += box(x0 + c * 40, y0 + r * 32, 40, 32, "#fff", P, 0, 1.4)
            b += text(x0 + c * 40 + 20, y0 + r * 32 + 16, vals[r][c], 13, mono=True, weight="bold")
    b += text(x0 - 8, y0 + 16, "row 0", 9.6, anchor="end", color="#555") + text(x0 - 8, y0 + 48, "row 1", 9.6, anchor="end", color="#555")
    for c in range(3):
        b += text(x0 + c * 40 + 20, y0 + 74, f"col {c}", 9, color="#555")
    # row major
    y = 140
    b += text(12, y, "Row major (row by row) – used by C", 11, anchor="start", weight="bold", color=BLUE)
    seq = ["a", "b", "c", "d", "e", "f"]; idx = ["0,0", "0,1", "0,2", "1,0", "1,1", "1,2"]
    for i, v in enumerate(seq):
        f = BLUEF if i < 3 else "#C9DFF7"
        b += box(30 + i * 50, y + 12, 50, 30, f, BLUE, 0, 1.3) + text(55 + i * 50, y + 27, v, 13, mono=True, weight="bold")
        b += text(55 + i * 50, y + 52, idx[i], 9.4, mono=True, color="#555")
        b += text(55 + i * 50, y + 66, str(2000 + 2 * i), 9.6, mono=True, color=BLUE)
    b += text(180, y + 86, "LOC(A[i][j]) = Base + w × [ (i−LR) × N + (j−LC) ]", 10, mono=True, weight="bold", color=BLUE)
    # column major
    y = 252
    b += text(12, y, "Column major (column by column) – FORTRAN", 11, anchor="start", weight="bold", color=ORANGE)
    seq = ["a", "d", "b", "e", "c", "f"]; idx = ["0,0", "1,0", "0,1", "1,1", "0,2", "1,2"]
    for i, v in enumerate(seq):
        f = ORANGEF if (i // 2) % 2 == 0 else "#FFE0B2"
        b += box(30 + i * 50, y + 12, 50, 30, f, ORANGE, 0, 1.3) + text(55 + i * 50, y + 27, v, 13, mono=True, weight="bold")
        b += text(55 + i * 50, y + 52, idx[i], 9.4, mono=True, color="#555")
        b += text(55 + i * 50, y + 66, str(2000 + 2 * i), 9.6, mono=True, color=ORANGE)
    b += text(180, y + 86, "LOC(A[i][j]) = Base + w × [ (j−LC) × M + (i−LR) ]", 10, mono=True, weight="bold", color=ORANGE)
    b += text(180, y + 108, "M = rows, N = columns, w = 2 bytes, Base = 2000", 9.6, color="#555")
    return svg(360, y + 120, b)


# ------------------------------------------------------------------ 10. insertion in array
def insert_delete():
    b = title("Insertion and Deletion in an Array")
    b += text(12, 42, "INSERT 25 at position 2 (index 2), N = 5", 11, anchor="start", weight="bold", color=GREEN)
    x0 = 30
    b += text(12, 66, "Before", 9.6, anchor="start", color="#555")
    b += cells(x0 + 40, 54, [10, 20, 30, 40, 50, ""], 40, 26, "#fff", P, None, YEL, 11.5)
    for i, s in enumerate([4, 3, 2]):          # shift arrows (right to left order)
        x = x0 + 40 + s * 40 + 20
        b += line(f"M{x} 82 Q{x + 20} 98 {x + 38} 84", GREEN, 1.4) + arrowhead(x + 38, 84, -40, 6, GREEN)
        b += text(x + 20, 104, f"{i + 1}", 9, color=GREEN, weight="bold")
    b += text(180, 120, "shift A[4], A[3], A[2] one place right (from the end)", 9.6, color="#555")
    b += text(12, 146, "After", 9.6, anchor="start", color="#555")
    b += cells(x0 + 40, 134, [10, 20, 25, 30, 40, 50], 40, 26, "#fff", P, {2}, GREENF, 11.5)
    b += text(180, 174, "N becomes 6   |   worst case: O(n) shifts", 10, weight="bold", color=GREEN)
    b += line("M10 188 H350", "#DDD", 1)
    b += text(12, 206, "DELETE element at index 1 (value 20), N = 6", 11, anchor="start", weight="bold", color=RED)
    b += text(12, 230, "Before", 9.6, anchor="start", color="#555")
    b += cells(x0 + 40, 218, [10, 20, 25, 30, 40, 50], 40, 26, "#fff", P, {1}, REDF, 11.5)
    for i, s in enumerate([2, 3, 4, 5]):
        x = x0 + 40 + s * 40 + 20
        b += line(f"M{x} 246 Q{x - 20} 262 {x - 38} 248", RED, 1.4) + arrowhead(x - 38, 248, -140, 6, RED)
        b += text(x - 20, 268, f"{i + 1}", 9, color=RED, weight="bold")
    b += text(180, 284, "shift A[2] … A[5] one place left (from the front)", 9.6, color="#555")
    b += text(12, 310, "After", 9.6, anchor="start", color="#555")
    b += cells(x0 + 40, 298, [10, 25, 30, 40, 50, ""], 40, 26, "#fff", P, None, YEL, 11.5)
    b += text(180, 338, "N becomes 5   |   worst case: O(n) shifts", 10, weight="bold", color=RED)
    return svg(360, 352, b)


DIAGRAMS = {"ds1_data_info": data_info, "ds1_classification": classification, "ds1_linear_nonlinear": linear_nonlinear,
            "ds1_operations": operations, "ds1_characteristics": characteristics, "ds1_growth": growth,
            "ds1_asymptotic": asymptotic, "ds1_array_memory": array_memory, "ds1_row_col_major": row_col_major,
            "ds1_insert_delete": insert_delete}

if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    for k, f in DIAGRAMS.items():
        with open(os.path.join(OUT, k + ".svg"), "w", encoding="utf-8") as fh:
            fh.write(f())
    print("written", len(DIAGRAMS))
