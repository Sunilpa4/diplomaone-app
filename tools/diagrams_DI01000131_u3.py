"""DI01000131 Computer Programming Fundamentals - Unit 3 diagrams (arrays, pointers)."""
import os
from flowchart_lib import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "content", "computer", "sem1", "DI01000131", "diagrams")
T_ = "True"; F_ = "False"
CELL = "#F5EEFD"; HL = "#FFF1C2"; HL_S = "#C99A00"; OK = "#E3F5E6"; OK_S = "#2E7D32"


def cell(x, y, w, h, label="", fill=CELL, stroke=P, size=12, weight="bold", mono=True, color=INK):
    """Box by top-left corner."""
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{fill}" stroke="{stroke}" stroke-width="1.5"/>'
            + (text(x + w / 2, y + h / 2, label, size, color=color, weight=weight, mono=mono) if label != "" else ""))


def small(x, y, s, anchor="middle", color="#444", size=10, mono=True, weight="normal"):
    return text(x, y, s, size, anchor=anchor, color=color, mono=mono, weight=weight)


# ------------------------------------------------------------------ 1. types of arrays
def array_types():
    b = title("Types of Arrays")
    # 1-D
    b += text(14, 44, "One-dimensional", 11.5, anchor="start", weight="bold", color=P)
    b += small(346, 44, "int a[5];", anchor="end", size=10.5, color=INK)
    for i in range(5):
        b += cell(80 + i * 40, 56, 40, 28)
        b += small(100 + i * 40, 98, f"a[{i}]")
    # 2-D
    b += text(14, 124, "Two-dimensional", 11.5, anchor="start", weight="bold", color=P)
    b += small(346, 124, "int m[3][4];", anchor="end", size=10.5, color=INK)
    for r in range(3):
        b += small(92, 148 + r * 24, f"row {r}", anchor="end")
        for c in range(4):
            b += cell(100 + c * 40, 136 + r * 24, 40, 24)
    for c in range(4):
        b += small(120 + c * 40, 222, f"col {c}")
    b += small(270, 172, "3 rows ×", anchor="start", mono=False, size=10.5) + small(270, 186, "4 columns", anchor="start", mono=False, size=10.5)
    # 3-D
    b += text(14, 250, "Multi-dimensional", 11.5, anchor="start", weight="bold", color=P)
    b += small(346, 250, "int x[2][3][4];", anchor="end", size=10.5, color=INK)
    for lx, ly, f in ((124, 262, "#EADDF7"), (110, 274, CELL)):
        for r in range(3):
            for c in range(4):
                b += cell(lx + c * 34, ly + r * 20, 34, 20, fill=f)
    b += small(262, 300, "2 tables of", anchor="start", mono=False, size=10.5) + small(262, 314, "3 × 4 each", anchor="start", mono=False, size=10.5)
    return svg(360, 348, b)


# ------------------------------------------------------------------ 2. 1-D array in memory
def mem_1d():
    b = title("One-dimensional Array in Memory")
    b += text(180, 42, "int a[5] = {10, 20, 30, 40, 50};", 11, color=P, mono=True, weight="bold")
    vals = [10, 20, 30, 40, 50]
    x0, w = 74, 54
    b += small(66, 90, "Value", anchor="end", mono=False, size=10.5, color="#333", weight="bold")
    b += small(66, 126, "Element", anchor="end", mono=False, size=10.5, color="#333", weight="bold")
    b += small(66, 144, "Address", anchor="end", mono=False, size=10.5, color="#333", weight="bold")
    for i, v in enumerate(vals):
        b += cell(x0 + i * w, 70, w, 40, str(v), HL if i == 3 else CELL, HL_S if i == 3 else P, 13)
        b += small(x0 + i * w + w / 2, 126, f"a[{i}]", color=INK, size=10.5)
        b += small(x0 + i * w + w / 2, 144, str(1000 + 4 * i), color="#1565C0", size=10.5)
    b += line(f"M{x0} 156 V162 H{x0 + 5 * w} V156", GREY, 1.2)
    b += text(180, 178, "5 elements × 4 bytes = 20 bytes (contiguous)", 10.5, color="#444")
    b += text(180, 202, "Address of a[i] = Base + i × size", 11, weight="bold", color=INK)
    b += text(180, 220, "a[3] = 1000 + 3 × 4 = 1012", 10.5, color="#8D6E00", mono=True)
    b += text(180, 240, "Index starts at 0, last index = size − 1", 10.5, color="#444")
    return svg(360, 254, b)


# ------------------------------------------------------------------ 3. linear search flowchart
def fc_search():
    b = title("Flowchart: Linear Search")
    x = 120
    b += terminal(x, 46, "Start")
    b += down(x, 62, 80) + io(x, 96, "Read n, a[ ], key", 170)
    b += down(x, 113, 129) + process(x, 146, "i = 0", 100, mono=True)
    b += down(x, 163, 177) + decision(x, 204, "i < n ?", 100, 54, mono=True)
    b += arr([(x, 231), (x, 253)], label=T_, lpos=(x + 20, 243))
    b += decision(x, 282, "a[i]==key ?", 130, 58, mono=True)
    b += arr([(185, 282), (199, 282)])
    b += text(190, 256, T_, 10.5, color="#2E7D32", weight="bold")
    b += io(244, 282, "Found at i", 92, 34)
    b += arr([(x, 311), (x, 333)], label=F_, lpos=(x + 22, 322))
    b += process(x, 350, "i = i + 1", 110, mono=True)
    b += arr([(x, 367), (x, 382), (24, 382), (24, 170), (x - 4, 170)])
    b += arr([(170, 204), (340, 204), (340, 344)], label=F_, lpos=(200, 195))
    b += io(300, 361, "Not found", 92, 34)
    b += line("M244 299 V404") + line("M300 378 V404") + line("M244 404 H300")
    b += down(272, 404, 420) + terminal(272, 436, "Stop", 80)
    return svg(360, 462, b)


# ------------------------------------------------------------------ 4. bubble sort passes
def bubble():
    b = title("Bubble Sort – Pass by Pass (Ascending)")
    rows = [("Initial", [50, 20, 40, 10, 30], 0), ("Pass 1", [20, 40, 10, 30, 50], 1), ("Pass 2", [20, 10, 30, 40, 50], 2),
            ("Pass 3", [10, 20, 30, 40, 50], 3), ("Pass 4", [10, 20, 30, 40, 50], 5)]
    x0, w, h = 84, 44, 30
    for r, (lab, vals, fixed) in enumerate(rows):
        y = 44 + r * 42
        b += text(20, y + h / 2, lab, 11.5, anchor="start", weight="bold", color="#333")
        for i, v in enumerate(vals):
            ok = i >= 5 - fixed
            b += cell(x0 + i * w, y, w, h, str(v), OK if ok else CELL, OK_S if ok else P, 12.5)
        if r:
            b += small(x0 + 5 * w + 8, y + h / 2, f"{5 - r} comp.", anchor="start", mono=False, size=10)
    yb = 44 + 5 * 42 + 6
    b += cell(20, yb, 16, 14, "", OK, OK_S) + small(42, yb + 7, "= reached final position", anchor="start", mono=False, size=10.5)
    b += text(180, yb + 34, "Adjacent elements are compared and swapped", 10.5, color="#444")
    b += text(180, yb + 50, "if a[j] > a[j+1]. After each pass the largest", 10.5, color="#444")
    b += text(180, yb + 66, "remaining element 'bubbles' to the end.", 10.5, color="#444")
    b += text(180, yb + 88, "n elements → n − 1 passes", 11, weight="bold", color=INK)
    return svg(360, yb + 102, b)


# ------------------------------------------------------------------ 5. 2-D array in memory
def mem_2d():
    b = title("Two-dimensional Array: Row-major Storage")
    b += text(180, 40, "int m[2][3] = {{1, 2, 3}, {4, 5, 6}};", 10.5, color=P, mono=True, weight="bold")
    x0, y0, w, h = 120, 66, 56, 34
    for c in range(3):
        b += small(x0 + c * w + w / 2, y0 - 6, f"col {c}", mono=False, size=10.5, color="#333")
    for r in range(2):
        b += small(x0 - 8, y0 + r * h + h / 2, f"row {r}", anchor="end", mono=False, size=10.5, color="#333")
        for c in range(3):
            b += cell(x0 + c * w, y0 + r * h, w, h, "", CELL if r == 0 else "#E3F0FC", P if r == 0 else S_IO)
            b += text(x0 + c * w + w / 2, y0 + r * h + 13, str(r * 3 + c + 1), 12.5, weight="bold", mono=True)
            b += small(x0 + c * w + w / 2, y0 + r * h + 27, f"m[{r}][{c}]", size=9)
    b += text(180, 152, "Logical view (table)  ↓  Memory (one row after another)", 10.5, color="#444")
    x1, w1 = 30, 50
    for k in range(6):
        r, c = divmod(k, 3)
        b += cell(x1 + k * w1, 166, w1, 32, str(k + 1), CELL if r == 0 else "#E3F0FC", P if r == 0 else S_IO, 12.5)
        b += small(x1 + k * w1 + w1 / 2, 212, f"m[{r}][{c}]", size=9.5, color=INK)
        b += small(x1 + k * w1 + w1 / 2, 228, str(1000 + 4 * k), size=10, color="#1565C0")
    b += line(f"M{x1} 238 V244 H{x1 + 3 * w1 - 3} V238", P, 1.2) + line(f"M{x1 + 3 * w1 + 3} 238 V244 H{x1 + 6 * w1} V238", S_IO, 1.2)
    b += small(x1 + 1.5 * w1, 258, "Row 0", mono=False, size=10.5, color=P, weight="bold") + small(x1 + 4.5 * w1, 258, "Row 1", mono=False, size=10.5, color=S_IO, weight="bold")
    b += text(180, 284, "Address of m[i][j] = Base + (i × cols + j) × size", 10.5, weight="bold", color=INK)
    b += text(180, 302, "m[1][2] = 1000 + (1 × 3 + 2) × 4 = 1020", 10.5, color="#8D6E00", mono=True)
    return svg(360, 316, b)


# ------------------------------------------------------------------ 6. matrix multiplication
def matmul():
    b = title("Matrix Multiplication (Row × Column)")
    A = [[1, 2], [3, 4]]; B = [[5, 6], [7, 8]]; C = [[19, 22], [43, 50]]
    w = 34; y0 = 52

    def mat(x, M, hl):
        out = ""
        for r in range(2):
            for c in range(2):
                on = hl(r, c)
                out += cell(x + c * w, y0 + r * w, w, w, str(M[r][c]), HL if on else CELL, HL_S if on else P, 12.5)
        return out
    b += mat(22, A, lambda r, c: r == 0) + text(110, y0 + w, "×", 18, weight="bold")
    b += mat(128, B, lambda r, c: c == 0) + text(216, y0 + w, "=", 18, weight="bold")
    b += mat(234, C, lambda r, c: r == 0 and c == 0)
    for x, n in ((22, "A (2×2)"), (128, "B (2×2)"), (234, "C (2×2)")):
        b += small(x + w, y0 + 2 * w + 16, n, mono=False, size=10.5, color="#333", weight="bold")
    lines = ["C[0][0] = 1×5 + 2×7 = 19", "C[0][1] = 1×6 + 2×8 = 22", "C[1][0] = 3×5 + 4×7 = 43", "C[1][1] = 3×6 + 4×8 = 50"]
    for i, s in enumerate(lines):
        b += text(180, 162 + i * 18, s, 11, mono=True, color="#8D6E00" if i == 0 else INK, weight="bold" if i == 0 else "normal")
    b += text(180, 244, "C[i][j] = Σ A[i][k] × B[k][j]   (k = 0 … n−1)", 11, weight="bold", color=P)
    b += text(180, 264, "Condition: columns of A = rows of B", 10.5, color="#444")
    b += text(180, 280, "Order: (m × n) × (n × p) → (m × p)", 10.5, color="#444")
    b += text(180, 296, "Needs 3 nested loops (i, j, k)", 10.5, color="#444")
    return svg(360, 310, b)


# ------------------------------------------------------------------ 7. pointer concept
def pointer():
    b = title("Pointer: Variable that Stores an Address")
    b += text(180, 42, "int x = 25;    int *p = &x;", 11.5, color=P, mono=True, weight="bold")
    for cx, name, val, addr, f, s in ((90, "x", "25", "1000", CELL, P), (270, "p", "1000", "2000", HL, HL_S)):
        b += text(cx, 72, name, 13, weight="bold", mono=True)
        b += cell(cx - 45, 82, 90, 42, val, f, s, 14)
        b += small(cx, 140, "address " + addr, size=10.5, color="#1565C0")
    b += arr([(225, 103), (137, 103)], "#C62828")
    b += text(181, 94, "points to", 10.5, color="#C62828", weight="bold")
    b += small(90, 156, "(int variable)", mono=False, size=10) + small(270, 156, "(pointer to int)", mono=False, size=10)
    rows = [("x", "25", "value of x"), ("&x", "1000", "address of x"), ("p", "1000", "value of p = address of x"),
            ("*p", "25", "value at address in p"), ("&p", "2000", "address of p itself")]
    y = 176
    b += f'<rect x="20" y="{y}" width="320" height="22" fill="{P}"/>'
    b += text(60, y + 11, "Expression", 10.5, color="#fff", weight="bold") + text(122, y + 11, "Value", 10.5, color="#fff", weight="bold") \
        + text(250, y + 11, "Meaning", 10.5, color="#fff", weight="bold")
    for i, (e, v, m) in enumerate(rows):
        yy = y + 22 + i * 22
        if i % 2:
            b += f'<rect x="20" y="{yy}" width="320" height="22" fill="#FAF7FE"/>'
        b += text(60, yy + 11, e, 11, mono=True, weight="bold") + text(122, yy + 11, v, 11, mono=True) + text(250, yy + 11, m, 10.5, color="#333")
    yy = y + 22 + 5 * 22
    b += line(f"M20 {yy} H340", "#E0D3F2", 1)
    return svg(360, yy + 14, b)


# ------------------------------------------------------------------ 8. pointer to pointer
def ptr_ptr():
    b = title("Pointer to Pointer (Double Pointer)")
    b += text(180, 42, "int x = 25;  int *p = &x;  int **q = &p;", 10.5, color=P, mono=True, weight="bold")
    items = [(62, "q", "2000", "3000", "int **"), (180, "p", "1000", "2000", "int *"), (298, "x", "25", "1000", "int")]
    for cx, n, v, a, t in items:
        b += text(cx, 72, n, 13, weight="bold", mono=True)
        b += cell(cx - 40, 82, 80, 40, v, HL if n != "x" else CELL, HL_S if n != "x" else P, 13)
        b += small(cx, 138, a, size=10.5, color="#1565C0") + small(cx, 154, t, size=10, color="#444")
    b += arr([(102, 102), (138, 102)], "#C62828") + arr([(220, 102), (256, 102)], "#C62828")
    rows = [("q", "2000", "address of p"), ("*q", "1000", "value of p (address of x)"), ("**q", "25", "value of x"),
            ("&q", "3000", "address of q")]
    y = 176
    for i, (e, v, m) in enumerate(rows):
        yy = y + i * 22
        if i % 2 == 0:
            b += f'<rect x="20" y="{yy - 11}" width="320" height="22" fill="#FAF7FE"/>'
        b += text(60, yy, e, 11, mono=True, weight="bold") + text(118, yy, v, 11, mono=True) + text(240, yy, m, 10.5, color="#333")
    b += text(180, y + 4 * 22 + 6, "Each * goes one level deeper.", 10.5, color="#444")
    return svg(360, y + 4 * 22 + 20, b)


# ------------------------------------------------------------------ 9. pointer and array
def ptr_array():
    b = title("Pointers and Arrays")
    b += text(180, 42, "int a[5] = {10, 20, 30, 40, 50};  int *p = a;", 10, color=P, mono=True, weight="bold")
    x0, w = 40, 56
    labels = ["p", "p+1", "p+2", "p+3", "p+4"]
    for i in range(5):
        cx = x0 + i * w + w / 2
        b += text(cx, 66, labels[i], 11, mono=True, weight="bold", color="#C62828")
        b += arr([(cx, 72), (cx, 92)], "#C62828")
        b += cell(x0 + i * w, 94, w, 38, str(10 * (i + 1)), HL if i == 2 else CELL, HL_S if i == 2 else P, 13)
        b += small(cx, 146, f"a[{i}]", size=10.5, color=INK) + small(cx, 162, str(1000 + 4 * i), size=10, color="#1565C0")
    ls = [("a  =  &a[0]  =  p  =  1000", True), ("a[i]  ≡  *(a + i)  ≡  *(p + i)  ≡  p[i]", True),
          ("*(p + 2) = a[2] = 30", False), ("p + 1 → 1004 (moves by sizeof(int) = 4)", False)]
    for i, (s, bold) in enumerate(ls):
        b += text(180, 190 + i * 19, s, 10.5, mono=True, color="#8D6E00" if i == 2 else INK, weight="bold" if bold else "normal")
    return svg(360, 190 + 4 * 19 + 2, b)


# ------------------------------------------------------------------ 10. void and null pointer
def void_null():
    b = title("void Pointer and NULL Pointer")
    b += line("M180 34 V258", "#C9B3EC", 1.2, "4 4")
    # void
    b += text(90, 44, "void pointer", 12, weight="bold", color=S_IO)
    b += rbox(90, 72, 120, 28, "void *vp;", "#E3F0FC", S_IO, 11.5, "bold", mono=True)
    for cx, t, v in ((36, "int", "10"), (90, "float", "2.5"), (144, "char", "'A'")):
        b += line(f"M90 86 L{cx} 128", S_IO, 1.4, "4 3") + arrowhead(cx, 130, 90 if cx == 90 else (115 if cx < 90 else 65), 6, S_IO)
        b += cell(cx - 25, 132, 50, 38, "", CELL, P)
        b += small(cx, 145, t, size=9.5) + text(cx, 160, v, 11.5, mono=True, weight="bold")
    b += text(90, 194, "Generic pointer: can hold", 10.5, color="#333") + text(90, 208, "address of any type", 10.5, color="#333")
    b += text(90, 230, "Cast before using *:", 10.5, color="#444") + text(90, 246, "*(int *)vp", 11, mono=True, weight="bold", color="#8D6E00")
    # null
    b += text(270, 44, "NULL pointer", 12, weight="bold", color="#C62828")
    b += rbox(270, 72, 150, 28, "int *np = NULL;", "#FDECEC", "#C62828", 11.5, "bold", mono=True)
    b += arr([(270, 86), (270, 124)], "#C62828")
    b += line("M250 128 H290", "#C62828", 2) + line("M257 135 H283", "#C62828", 2) + line("M264 142 H276", "#C62828", 2)
    b += text(270, 162, "NULL (address 0)", 10.5, mono=True, color="#C62828")
    b += text(270, 194, "Points to no valid", 10.5, color="#333") + text(270, 208, "memory location", 10.5, color="#333")
    b += text(270, 230, "Check before using *:", 10.5, color="#444") + text(270, 246, "if (np != NULL)", 11, mono=True, weight="bold", color="#8D6E00")
    return svg(360, 262, b)


DIAGRAMS = {
    "c3_array_types": array_types, "c3_1d_memory": mem_1d, "c3_fc_search": fc_search, "c3_bubble": bubble,
    "c3_2d_memory": mem_2d, "c3_matmul": matmul, "c3_pointer": pointer, "c3_ptr_ptr": ptr_ptr,
    "c3_ptr_array": ptr_array, "c3_void_null": void_null,
}

if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    for k, f in DIAGRAMS.items():
        with open(os.path.join(OUT, k + ".svg"), "w", encoding="utf-8") as fh:
            fh.write(f())
    print("written", len(DIAGRAMS))
