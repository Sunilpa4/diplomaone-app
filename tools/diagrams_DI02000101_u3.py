"""DI02000101 Scripting Language (Python) - Unit 3 diagrams (lists, tuples, sets, dictionaries)."""
import os
from flowchart_lib import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "content", "computer", "sem2", "DI02000101", "diagrams")
CELL = "#F5EEFD"; BLUE = "#1565C0"; BLUEF = "#E3F0FC"; GREEN = "#2E7D32"; GREENF = "#E3F5E6"
ORANGE = "#E07B00"; ORANGEF = "#FFF1DE"; RED = "#C62828"; REDF = "#FDECEC"; YEL = "#FFF6D6"; YELS = "#B88A00"
PYB = "#306998"; GREYF = "#F0F0F0"
NB = "\u00a0"


def box(x, y, w, h, fill=CELL, stroke=P, rx=6, sw=1.5):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>'


def sp(s):
    return s.replace("  ", NB + NB)


def cells(x, y, vals, w=40, h=28, fill=CELL, st=P, size=11.5, hl=None, hlf=YEL, hls=YELS):
    o = ""
    for i, v in enumerate(vals):
        f, s = (hlf, hls) if hl and i in hl else (fill, st)
        o += box(x + i * w, y, w, h, f, s, 0, 1.3) + text(x + i * w + w / 2, y + h / 2, str(v), size, mono=True, weight="bold")
    return o


# ------------------------------------------------------------------ 1. list indexing
def list_index():
    b = title("List: Indexing and Slicing")
    b += text(180, 40, sp("a = [10, 20, 30, 40, 50, 60]"), 11.5, mono=True, color=P, weight="bold")
    x0, w, y = 60, 40, 72
    b += text(x0 - 8, y - 10, "+ve", 9.5, anchor="end", color=GREEN, weight="bold")
    b += text(x0 - 8, y + 46, "−ve", 9.5, anchor="end", color=RED, weight="bold")
    vals = [10, 20, 30, 40, 50, 60]
    for i in range(6):
        b += text(x0 + i * w + w / 2, y - 10, str(i), 10.5, mono=True, color=GREEN, weight="bold")
        b += text(x0 + i * w + w / 2, y + 46, str(i - 6), 10.5, mono=True, color=RED, weight="bold")
    b += cells(x0, y, vals, w, 30)
    rows = [("a[0]", "10"), ("a[-1]", "60"), ("a[1:4]", "[20, 30, 40]"), ("a[:3]", "[10, 20, 30]"), ("a[3:]", "[40, 50, 60]"),
            ("a[::2]", "[10, 30, 50]"), ("a[::-1]", "[60, 50, 40, 30, 20, 10]"), ("a[1] = 25", "[10, 25, 30, …]  (mutable)"),
            ("a[1:3] = [7, 8]", "replaces a slice")]
    y = 142
    for e, r in rows:
        b += text(18, y, e, 10.5, anchor="start", mono=True, weight="bold", color=PYB)
        b += text(140, y, sp("→ " + r), 10.2, anchor="start", mono=True, color=GREEN)
        y += 17
    b += text(180, y + 6, "a[10] → IndexError: list index out of range", 10, mono=True, color=RED)
    return svg(360, y + 18, b)


# ------------------------------------------------------------------ 2. list methods
def list_methods():
    b = title("List Methods: Before → After")
    b += text(180, 38, sp("Start every row with  a = [3, 1, 2]"), 10.5, color="#555")
    rows = [("a.append(5)", "[3, 1, 2, 5]", "add at end"), ("a.insert(1, 9)", "[3, 9, 1, 2]", "add at index"),
            ("a.extend([7, 8])", "[3, 1, 2, 7, 8]", "add many"), ("a.remove(1)", "[3, 2]", "delete by value"),
            ("a.pop()", "[3, 1]  returns 2", "delete last"), ("a.pop(0)", "[1, 2]  returns 3", "delete by index"),
            ("del a[1]", "[3, 2]", "statement"), ("a.sort()", "[1, 2, 3]", "ascending"),
            ("a.sort(reverse=True)", "[3, 2, 1]", "descending"), ("a.reverse()", "[2, 1, 3]", "reverse order"),
            ("a.index(2)", "2", "position of 2"), ("a.count(3)", "1", "occurrences"), ("a.clear()", "[]", "empty list")]
    y = 54
    for i, (m, r, n) in enumerate(rows):
        b += f'<rect x="8" y="{y}" width="344" height="21" fill="{"#F6F0FE" if i % 2 == 0 else "#fff"}"/>'
        b += text(14, y + 10.5, m, 10.2, anchor="start", mono=True, weight="bold", color=PYB)
        b += text(160, y + 10.5, sp(r), 10, anchor="start", mono=True, color=GREEN, weight="bold")
        b += text(348, y + 10.5, n, 9, anchor="end", color="#666")
        y += 21
    b += text(180, y + 14, "sort(), reverse(), append() … change the list and return None.", 9.8, color=RED, weight="bold")
    return svg(360, y + 26, b)


# ------------------------------------------------------------------ 3. aliasing vs copy
def list_copy():
    b = title("Aliasing vs Copying a List")
    # alias
    b += text(90, 42, "b = a  (alias)", 11.5, mono=True, weight="bold", color=RED)
    b += box(20, 60, 40, 28, BLUEF, BLUE) + text(40, 74, "a", 12, mono=True, weight="bold")
    b += box(20, 104, 40, 28, BLUEF, BLUE) + text(40, 118, "b", 12, mono=True, weight="bold")
    b += box(96, 80, 72, 30, YEL, YELS, 6) + text(132, 95, "[1, 2, 9]", 10.5, mono=True, weight="bold")
    b += arr([(60, 74), (94, 90)], BLUE) + arr([(60, 118), (94, 100)], BLUE)
    b += text(90, 150, "b[2] = 9 changes a too", 10, color=RED, weight="bold")
    b += text(90, 166, "a is b → True", 10, mono=True, color="#444")
    b += line("M180 36 V180", "#E0D3F2", 1)
    # copy
    b += text(270, 42, "b = a.copy()", 11.5, mono=True, weight="bold", color=GREEN)
    b += box(196, 60, 40, 28, BLUEF, BLUE) + text(216, 74, "a", 12, mono=True, weight="bold")
    b += box(196, 104, 40, 28, BLUEF, BLUE) + text(216, 118, "b", 12, mono=True, weight="bold")
    b += box(270, 59, 76, 30, YEL, YELS, 6) + text(308, 74, "[1, 2, 3]", 10.5, mono=True, weight="bold")
    b += box(270, 103, 76, 30, GREENF, GREEN, 6) + text(308, 118, "[1, 2, 9]", 10.5, mono=True, weight="bold")
    b += arr([(236, 74), (268, 74)], BLUE) + arr([(236, 118), (268, 118)], BLUE)
    b += text(270, 150, "b[2] = 9: a unchanged", 10, color=GREEN, weight="bold")
    b += text(270, 166, "a is b → False", 10, mono=True, color="#444")
    ways = ["Ways to copy:", "b = a.copy()", "b = a[:]", "b = list(a)", "import copy; b = copy.deepcopy(a)  (nested)"]
    y = 196
    for i, s in enumerate(ways):
        b += text(20, y + i * 16, sp(s), 10.2, anchor="start", mono=i > 0, weight="bold" if i == 0 else "normal", color=P if i == 0 else INK)
    return svg(360, y + 5 * 16 + 4, b)


# ------------------------------------------------------------------ 4. tuple packing / unpacking
def tuple_pack():
    b = title("Tuple Packing and Unpacking")
    b += text(180, 42, "Packing", 12, weight="bold", color=BLUE)
    b += text(180, 62, sp('t = 101, "Amit", 78.5'), 11.5, mono=True, color=INK, weight="bold")
    vals = ["101", '"Amit"', "78.5"]
    for i, v in enumerate(vals):
        b += box(72 + i * 72, 78, 72, 30, BLUEF, BLUE, 0, 1.3) + text(108 + i * 72, 93, v, 11, mono=True, weight="bold")
    b += text(40, 93, "t", 13, mono=True, weight="bold", color=BLUE) + arr([(48, 93), (70, 93)], BLUE)
    for i in range(3):
        b += text(108 + i * 72, 122, f"t[{i}]", 9.5, mono=True, color="#777")
    b += text(180, 152, "Unpacking", 12, weight="bold", color=GREEN)
    b += text(180, 172, sp("roll, name, marks = t"), 11.5, mono=True, color=INK, weight="bold")
    names = ["roll", "name", "marks"]
    for i, n in enumerate(names):
        x = 108 + i * 72
        b += box(x - 36, 188, 72, 30, BLUEF, BLUE, 0, 1.3) + text(x, 203, vals[i], 11, mono=True, weight="bold")
        b += down(x, 218, 240, GREEN)
        b += box(x - 32, 242, 64, 26, GREENF, GREEN, 13) + text(x, 255, n, 11, mono=True, weight="bold", color=GREEN)
    notes = ["Number of variables must match the items,", "else ValueError.", "a, b = b, a   (swap = pack + unpack)",
             "first, *rest = (1, 2, 3)  →  rest = [2, 3]"]
    y = 290
    for i, s in enumerate(notes):
        b += text(180, y + i * 16, sp(s), 10.2, mono=(i >= 2), color=INK if i >= 2 else "#444", weight="bold" if i >= 2 else "normal")
    return svg(360, y + 4 * 16, b)


# ------------------------------------------------------------------ 5. set operations (Venn)
def set_ops():
    b = title("Set Operations")
    b += text(180, 38, sp("A = {1, 2, 3, 4}    B = {3, 4, 5, 6}"), 10.5, mono=True, color=INK, weight="bold")
    ops = [("A | B", "union()", "{1, 2, 3, 4, 5, 6}", "AB"), ("A & B", "intersection()", "{3, 4}", "M"),
           ("A - B", "difference()", "{1, 2}", "A"), ("A ^ B", "symmetric_difference()", "{1, 2, 5, 6}", "X")]
    for k, (op, meth, res, mode) in enumerate(ops):
        c, r = k % 2, k // 2
        ox, oy = 8 + c * 176, 46 + r * 150
        cx1, cx2, cy, rad = ox + 62, ox + 106, oy + 56, 36
        clip = f"clipA{k}"
        b += f'<clipPath id="{clip}"><circle cx="{cx1}" cy="{cy}" r="{rad}"/></clipPath>'
        fa = GREENF if mode in ("AB", "A", "X") else "#fff"
        fb = GREENF if mode in ("AB", "X") else "#fff"
        fm = GREENF if mode in ("AB", "M") else "#fff"
        b += f'<circle cx="{cx1}" cy="{cy}" r="{rad}" fill="{fa}"/>'
        b += f'<circle cx="{cx2}" cy="{cy}" r="{rad}" fill="{fb}"/>'
        b += f'<circle cx="{cx2}" cy="{cy}" r="{rad}" fill="{fm}" clip-path="url(#{clip})"/>'
        if mode in ("AB", "A", "X", "M"):
            pass
        b += f'<circle cx="{cx1}" cy="{cy}" r="{rad}" fill="none" stroke="{BLUE}" stroke-width="1.6"/>'
        b += f'<circle cx="{cx2}" cy="{cy}" r="{rad}" fill="none" stroke="{ORANGE}" stroke-width="1.6"/>'
        b += text(cx1 - 16, cy, "1 2", 10.5, mono=True, weight="bold") + text(cx1 + 22, cy, "3 4", 10.5, mono=True, weight="bold")
        b += text(cx2 + 16, cy, "5 6", 10.5, mono=True, weight="bold")
        b += text(cx1 - 30, oy + 16, "A", 11, weight="bold", color=BLUE) + text(cx2 + 30, oy + 16, "B", 11, weight="bold", color=ORANGE)
        b += text(ox + 84, oy + 108, op + "   " .replace(" ", NB) + meth, 10, mono=True, weight="bold", color=P)
        b += text(ox + 84, oy + 124, res, 10, mono=True, color=GREEN, weight="bold")
    b += text(180, 354, "Also: A <= B (subset), A >= B (superset), A.isdisjoint(B)", 9.8, color="#444")
    return svg(360, 366, b)


# ------------------------------------------------------------------ 6. dictionary structure
def dict_struct():
    b = title("Dictionary: Keys Map to Values")
    b += text(180, 40, sp('d = {"roll": 101, "name": "Amit", "sem": 2}'), 10.2, mono=True, color=P, weight="bold")
    b += text(86, 62, "Keys (unique, immutable)", 10, weight="bold", color=BLUE)
    b += text(270, 62, "Values (any type)", 10, weight="bold", color=GREEN)
    pairs = [('"roll"', "101"), ('"name"', '"Amit"'), ('"sem"', "2")]
    for i, (k, v) in enumerate(pairs):
        y = 76 + i * 44
        b += box(30, y, 100, 30, BLUEF, BLUE, 15) + text(80, y + 15, k, 11.5, mono=True, weight="bold")
        b += box(220, y, 100, 30, GREENF, GREEN, 6) + text(270, y + 15, v, 11.5, mono=True, weight="bold")
        b += arr([(130, y + 15), (218, y + 15)], P)
    rows = [('d["name"]', '"Amit"'), ('d.get("city")', "None  (no error)"), ('d["city"]', "KeyError"),
            ('d["sem"] = 3', "update value"), ('d["city"] = "Surat"', "add new pair"), ('del d["roll"]', "delete pair"),
            ('"roll" in d', "True  (checks keys)")]
    y = 220
    for e, r in rows:
        b += text(18, y, e, 10.2, anchor="start", mono=True, weight="bold", color=PYB)
        b += text(176, y, sp("→ " + r), 10, anchor="start", mono=True, color=RED if "Error" in r else GREEN)
        y += 17
    return svg(360, y + 2, b)


# ------------------------------------------------------------------ 7. dict methods
def dict_methods():
    b = title("Dictionary Methods")
    b += text(180, 38, sp('d = {"a": 1, "b": 2}'), 11, mono=True, color=P, weight="bold")
    rows = [("d.keys()", "dict_keys(['a', 'b'])"), ("d.values()", "dict_values([1, 2])"), ("d.items()", "[('a', 1), ('b', 2)]"),
            ('d.get("c", 0)', "0  (default)"), ('d.update({"c": 3})', "adds / updates pairs"), ('d.pop("a")', "removes, returns 1"),
            ("d.popitem()", "removes last pair"), ('d.setdefault("z", 9)', "adds z: 9 if missing"),
            ('dict.fromkeys("ab", 0)', "{'a': 0, 'b': 0}"), ("d.copy()", "shallow copy"), ("d.clear()", "{}"), ("len(d)", "2  (number of pairs)")]
    y = 54
    for i, (m, r) in enumerate(rows):
        b += f'<rect x="8" y="{y}" width="344" height="21" fill="{"#F6F0FE" if i % 2 == 0 else "#fff"}"/>'
        b += text(14, y + 10.5, m, 10.2, anchor="start", mono=True, weight="bold", color=PYB)
        b += text(178, y + 10.5, sp(r), 9.8, anchor="start", mono=True, color=GREEN)
        y += 21
    b += text(180, y + 16, "for k, v in d.items():  print(k, v)".replace("  ", NB + NB), 10.5, mono=True, color=P, weight="bold")
    return svg(360, y + 28, b)


# ------------------------------------------------------------------ 8. nested structures
def nested():
    b = title("Nested Data Structures")
    b += text(14, 44, "List of lists (matrix)", 11, anchor="start", weight="bold", color=BLUE)
    b += text(14, 62, sp("m = [[1, 2, 3], [4, 5, 6]]"), 10.5, anchor="start", mono=True, color=INK)
    for r in range(2):
        b += text(30, 88 + r * 28, f"m[{r}]", 10, mono=True, color="#777")
        b += cells(56, 76 + r * 28, [r * 3 + 1, r * 3 + 2, r * 3 + 3], 34, 24, BLUEF, BLUE, 11, hl={1} if r == 1 else None)
    b += text(250, 96, "m[1][1] → 5", 11, mono=True, color=YELS, weight="bold")
    b += line("M10 140 H350", "#E0D3F2", 1)
    b += text(14, 160, "List of dictionaries (records)", 11, anchor="start", weight="bold", color=GREEN)
    recs = [("101", "Amit", "78"), ("102", "Riya", "85")]
    for i, (r, n, m) in enumerate(recs):
        y = 172 + i * 34
        b += text(30, y + 14, f"s[{i}]", 10, mono=True, color="#777")
        b += box(56, y, 290, 28, GREENF, GREEN, 6) + text(201, y + 14, sp(f'{{"roll": {r}, "name": "{n}", "marks": {m}}}'), 10, mono=True)
    b += text(180, 256, sp('s[1]["name"] → "Riya"'), 11, mono=True, color=YELS, weight="bold")
    b += line("M10 272 H350", "#E0D3F2", 1)
    b += text(14, 292, "Dictionary of lists", 11, anchor="start", weight="bold", color=ORANGE)
    b += text(14, 310, sp('marks = {"Amit": [78, 82], "Riya": [85, 90]}'), 10.2, anchor="start", mono=True, color=INK)
    b += text(180, 332, sp('marks["Riya"][0] → 85'), 11, mono=True, color=YELS, weight="bold")
    return svg(360, 346, b)


# ------------------------------------------------------------------ 9. built-in functions matrix
def builtin_matrix():
    b = title("Common Built-in Functions")
    cols = ["list", "tuple", "set", "dict"]
    funcs = [("len(x)", "YYYY", "number of items"), ("max(x) / min(x)", "YYYY", "dict: on keys"), ("sum(x)", "YYYY", "numbers; dict: keys"),
             ("sorted(x)", "YYYY", "returns a new list"), ("x[i]", "YYNK", "dict: x[key]"), ("x.append()", "YNNN", ""),
             ("x.add()", "NNYN", ""), ("x.count()", "YYNN", ""), ("x.index()", "YYNN", ""), ("x.pop()", "YNYY", ""),
             ("x.remove()", "YNYN", ""), ("x.update()", "NNYY", ""), ("x.clear() / copy()", "YNYY", "")]
    x0, cw = 156, 49
    b += f'<rect x="8" y="34" width="344" height="22" fill="{P}"/>'
    b += text(14, 45, "Function", 10.5, anchor="start", weight="bold", color="#fff")
    for j, c in enumerate(cols):
        b += text(x0 + j * cw + cw / 2, 45, c, 10.5, mono=True, weight="bold", color="#fff")
    y = 56
    for i, (f, yn, n) in enumerate(funcs):
        b += f'<rect x="8" y="{y}" width="344" height="20" fill="{"#F6F0FE" if i % 2 == 0 else "#fff"}"/>'
        b += text(14, y + 10, f, 9.8, anchor="start", mono=True, weight="bold", color=PYB)
        for j, ch in enumerate(yn):
            sym, col = {"Y": ("✓", GREEN), "N": ("✗", RED), "K": ("key", ORANGE)}[ch]
            b += text(x0 + j * cw + cw / 2, y + 10, sym, 11 if ch != "K" else 9.5, weight="bold", color=col)
        y += 20
    notes = ["For a dict, len/max/min/sum/sorted work on the KEYS.", "sorted(x) always returns a new list.",
             "Tuples are immutable: no append/remove/pop."]
    for i, s_ in enumerate(notes):
        b += text(180, y + 16 + i * 15, s_, 9.8, color=RED if i == 2 else "#444", weight="bold" if i == 2 else "normal")
    return svg(360, y + 16 + 3 * 15, b)


# ------------------------------------------------------------------ 10. choose a data structure
def choose():
    b = title("Which Data Structure Should I Use?")
    b += decision(110, 70, "key → value\nlookup?", 130, 56, 10)
    b += arr([(175, 70), (232, 70)], label="Yes", lpos=(204, 60))
    b += rbox(290, 70, 100, 30, "dict", REDF, RED, 12, "bold", RED, mono=True)
    b += arr([(110, 98), (110, 124)], label="No", lpos=(124, 111))
    b += decision(110, 152, "only unique\nitems?", 130, 56, 10)
    b += arr([(175, 152), (232, 152)], label="Yes", lpos=(204, 142))
    b += rbox(290, 152, 100, 30, "set", ORANGEF, ORANGE, 12, "bold", ORANGE, mono=True)
    b += arr([(110, 180), (110, 206)], label="No", lpos=(124, 193))
    b += decision(110, 234, "will items\nchange?", 130, 56, 10)
    b += arr([(175, 234), (232, 234)], label="Yes", lpos=(204, 224))
    b += rbox(290, 234, 100, 30, "list", BLUEF, BLUE, 12, "bold", BLUE, mono=True)
    b += arr([(110, 262), (110, 286)], label="No", lpos=(124, 274))
    b += rbox(110, 302, 100, 30, "tuple", GREENF, GREEN, 12, "bold", GREEN, mono=True)
    ex = [("dict", "phone book, student record", RED), ("set", "unique visitors, tags", ORANGE),
          ("list", "marks, shopping cart", BLUE), ("tuple", "days of week, (x, y)", GREEN)]
    y = 338
    for n, e, c in ex:
        b += text(40, y, n, 10.5, anchor="start", mono=True, weight="bold", color=c) + text(100, y, e, 10, anchor="start", color="#444")
        y += 16
    return svg(360, y + 2, b)


DIAGRAMS = {"py3_list_index": list_index, "py3_list_methods": list_methods, "py3_list_copy": list_copy,
            "py3_tuple_pack": tuple_pack, "py3_set_ops": set_ops, "py3_dict_struct": dict_struct,
            "py3_dict_methods": dict_methods, "py3_nested": nested, "py3_builtin_matrix": builtin_matrix, "py3_choose": choose}

if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    for k, f in DIAGRAMS.items():
        with open(os.path.join(OUT, k + ".svg"), "w", encoding="utf-8") as fh:
            fh.write(f())
    print("written", len(DIAGRAMS))
