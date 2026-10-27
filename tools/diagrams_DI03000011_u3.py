"""DI03000011 Digital Electronics - Unit 3 diagrams: K-map simplification. All groups come from de_kmap.minimise (exact)."""
import os
from flowchart_lib import *
from diagrams_DI03000021_u1 import box, BLUE, BLUEF, GREEN, GREENF, ORANGE, ORANGEF, RED, REDF, YEL
from diagrams_DI03000011_u1 import note
import de_kmap as K
from de_gates import bexpr

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "content", "computer", "sem3", "DI03000011", "diagrams")

# ---- the worked examples used in notes (shared with the notes/extras files)
EX3 = (3, [1, 3, 5, 6, 7], [])
EX4 = (4, [0, 1, 2, 4, 5, 6, 8, 9, 12, 13, 14], [])
EXDC = (4, [1, 3, 7, 11, 15], [0, 2, 5])
EXPOS = (4, [0, 1, 2, 5, 8, 9, 10], [])
EXBCD = (4, [5, 6, 7, 8, 9], [10, 11, 12, 13, 14, 15])


def solved(n, ones, dc):
    g = K.minimise(n, ones, dc)
    K.check(n, ones, dc, g)
    return g


def answer_box(y, n, ones, dc, g, label="Y", pos=False):
    f = ("Y = Σm(" + ", ".join(map(str, ones)) + ")") + (" + d(" + ", ".join(map(str, dc)) + ")" if dc else "")
    ans = (K.pos_str(g) if pos else K.sop_str(g))
    b = box(12, y, 336, 50, "#FCFAFF", "#D9C8F0", 8, 1)
    b += text(180, y + 15, f, 9.6, mono=True, color="#444")
    b += bexpr(180, y + 38, f"{label} = {ans}", 13, color=P)
    return b


# ------------------------------------------------------------------ 1. need for simplification
def need():
    b = title("Why Simplify? Same Function, Fewer Gates")
    b += bexpr(180, 42, "Y = !A!BC + !ABC + A!BC + ABC", 11.5, color=P)
    cubes = ["001", "011", "101", "111"]
    c, h = K.sop_circuit(cubes, 3, y0=68)
    b += c
    y = h + 6
    b += box(12, y, 160, 54, REDF, RED, 8, 1.1) + text(92, y + 16, "Before", 10, weight="bold", color=RED)
    b += text(92, y + 33, "4 AND + 1 OR + 2 NOT", 9.4) + text(92, y + 46, "= 7 gates", 9.4, weight="bold")
    b += box(188, y, 160, 54, GREENF, GREEN, 8, 1.1) + text(268, y + 16, "After (K-map)", 10, weight="bold", color=GREEN)
    b += bexpr(268, y + 36, "Y = C", 13, color=GREEN) + text(268, y + 49, "no gate at all", 9.2)
    return svg(360, y + 64, b)


# ------------------------------------------------------------------ cell-term maps
def term_map(n, x, y, cell):
    m, _ = K.kmap_svg(x, y, n, [], cell=cell, show_zero=False)
    rv, cv, rb, cb = K.layout(n)
    for r in range(len(rv)):
        for c in range(len(cv)):
            mm = K.cell_min(n, r, c)
            t = "".join((v if (mm >> (n - 1 - i)) & 1 else "!" + v) for i, v in enumerate("ABCD"[:n]))
            m += bexpr(x + c * cell + cell / 2, y + r * cell + cell / 2 + 6, t, 10 if n < 4 else 8.6, color="#333", weight="normal")
            m += text(x + c * cell + cell / 2, y + r * cell + cell - 6, f"m{mm}", 7.4, color=BLUE) if False else ""
    return m


def kmap2():
    b = title("Two-Variable K-map")
    b += text(96, 36, "Cells and minterms", 9.8, weight="bold", color=BLUE) + term_map(2, 64, 90, 50)
    n, ones, dc = 2, [1, 2, 3], []
    g = solved(n, ones, dc)
    b += text(270, 36, "Example: Σm(1, 2, 3)", 9.8, weight="bold", color=BLUE)
    m, _ = K.kmap_svg(230, 90, n, ones, dc, g, cell=50)
    b += m + K.legend(232, 212, g)
    b += note(12, 248, 336, ["4 cells (2² = 4). Row = A, column = B.", "Adjacent cells differ in only ONE variable.",
                             ("Result: Y = A + B (an OR gate).", GREEN)], size=9.6)
    return svg(360, 310, b)


def kmap3():
    b = title("Three-Variable K-map")
    b += term_map(3, 92, 70, 60)
    b += text(212, 46, "Gray code order: 00, 01, 11, 10", 9, color=RED, weight="bold") if False else ""
    b += note(12, 202, 336, ["8 cells (2³). Rows: A = 0, 1. Columns: BC in", "Gray code order 00, 01, 11, 10 (not 00 01 10 11),",
                             "so neighbouring cells differ in only one bit.", ("Left and right edges are also adjacent (wrap).", RED),
                             "Small number in each cell = minterm number."], size=9.6)
    return svg(360, 288, b)


def kmap4():
    b = title("Four-Variable K-map")
    m, _ = K.kmap_svg(118, 76, 4, [], cell=46, show_zero=False)
    b += m
    rv, cv, rb, cb = K.layout(4)
    for r in range(4):
        for c in range(4):
            mm = K.cell_min(4, r, c)
            b += text(118 + c * 46 + 23, 76 + r * 46 + 25, f"m{mm}", 12, weight="bold", color="#555")
    b += note(12, 270, 336, ["16 cells (2⁴). Rows AB and columns CD both use", "Gray code: 00, 01, 11, 10.",
                             ("Top-bottom and left-right edges are adjacent;", RED), ("the four corners are also adjacent.", RED)], size=9.6)
    return svg(360, 342, b)


# ------------------------------------------------------------------ grouping types
def groups():
    b = title("Types of Groups in a 4-Variable K-map")
    cases = [("Pair (2 cells)", [5, 13]), ("Quad, wrap (4 cells)", [4, 6, 12, 14]),
             ("Octet, wrap (8 cells)", [0, 1, 2, 3, 8, 9, 10, 11]), ("Four corners (quad)", [0, 2, 8, 10])]
    for i, (nm, ones) in enumerate(cases):
        x = 52 + (i % 2) * 176
        y = 70 + (i // 2) * 160
        g = solved(4, ones, [])
        b += text(x + 44, y - 40, nm, 9.8, weight="bold", color=BLUE)
        m, _ = K.kmap_svg(x, y, 4, ones, (), g, cell=22, show_zero=False, numbers=False)
        b += m + bexpr(x + 44, y + 106, "Y = " + K.sop_str(g), 11, color=K.COLORS[0])
    b += note(12, 382, 336, ["Group size must be 1, 2, 4, 8 or 16 (power of 2).", "Pair removes 1 variable, quad 2, octet 3."], size=9.6)
    return svg(360, 426, b)


# ------------------------------------------------------------------ steps flowchart
def steps():
    b = title("Steps of K-map Simplification (SOP)")
    labels = ["Draw map with 2ⁿ cells", "Write 1 for each minterm, X for", "Group 1s: octets, then quads,", "Every 1 covered at least once;",
              "Write the term of each group", "OR all terms: minimal SOP"]
    sub = ["(Gray code order)", "don't-cares, 0 elsewhere", "pairs, singles (largest first)", "use fewest, largest groups",
           "(keep variables that don't change)", "then draw with gates"]
    y = 52
    b += terminal(180, y - 12, "Start", 80, 24, 11)
    for i, (l, s) in enumerate(zip(labels, sub)):
        yy = y + 18 + i * 56
        b += down(180, yy - 18 if i else y, yy) if i else down(180, y, yy)
        b += rbox(180, yy + 18, 250, 40, "", F_PROC, S_PROC)
        b += text(180, yy + 13, f"{i + 1}. {l}", 10.4, weight="bold") + text(180, yy + 28, s, 9.2, color="#555")
    return svg(360, y + 18 + 6 * 56 + 4, b)


# ------------------------------------------------------------------ worked examples
def example_map(ttl, data, pos=False, cell=44, impl_note=None):
    n, ones, dc = data
    b = title(ttl)
    if pos:
        zeros = [m for m in range(2 ** n) if m not in ones and m not in dc]
        g = K.minimise(n, zeros, dc)
        K.check(n, zeros, dc, g)
    else:
        g = solved(n, ones, dc)
    x = 92 if n == 4 else 110
    m, (mx, my) = K.kmap_svg(x, 72, n, ones, dc, g, cell=cell, zeros_mode=pos)
    b += m
    lx = mx + 12 if n == 3 else 14
    if n == 4:
        b += K.legend(mx + 10 if mx < 290 else 250, my + 18, g, pos=pos) if False else ""
    ly = my + 22
    b += K.legend(30, ly, g, pos=pos, size=10.5)
    sizes = [K.size_name(c)[0] for c in g]
    for i, s in enumerate(sizes):
        b += text(220, ly + i * 20 + 3, s, 9.4, anchor="start", color="#666")
    y2 = ly + len(g) * 20 + 4
    b += answer_box(y2, n, ones, dc, g, pos=pos)
    return svg(360, y2 + 60, b), g


def ex3():
    return example_map("Example: 3-Variable K-map", EX3, cell=52)[0]


def ex4():
    return example_map("Example: 4-Variable K-map", EX4)[0]


def dontcare():
    return example_map("K-map with Don't-Care Conditions", EXDC)[0]


def pos_map():
    return example_map("POS: Grouping the 0s", EXPOS, pos=True)[0]


def bcd():
    return example_map("BCD Input ≥ 5 Detector (don't-cares)", EXBCD)[0]


def impl():
    n, ones, dc = EX4
    g = solved(n, ones, dc)
    b = title("Implementation with Basic Gates")
    b += bexpr(180, 42, "Y = " + K.sop_str(g), 12.5, color=P)
    c, h = K.sop_circuit(g, n, y0=70)
    b += c
    b += note(12, h + 4, 336, ["NOT gates make complemented inputs; one AND", "gate per product term; one OR gate adds them.",
                               ("Single-literal term needs no AND gate.", GREEN)], size=9.6)
    return svg(360, h + 66, b)


DIAGRAMS = {"de3_need": need, "de3_kmap2": kmap2, "de3_kmap3": kmap3, "de3_kmap4": kmap4, "de3_groups": groups,
            "de3_steps": steps, "de3_ex3": ex3, "de3_ex4": ex4, "de3_pos": pos_map, "de3_dontcare": dontcare,
            "de3_bcd": bcd, "de3_impl": impl}

if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    for k, f in DIAGRAMS.items():
        with open(os.path.join(OUT, k + ".svg"), "w", encoding="utf-8") as fh:
            fh.write(f())
    print("written", len(DIAGRAMS))
    for nm, d in [("EX3", EX3), ("EX4", EX4), ("EXDC", EXDC), ("EXBCD", EXBCD)]:
        print(nm, K.sop_str(solved(*d)))
    z = [m for m in range(16) if m not in EXPOS[1]]
    print("EXPOS", K.pos_str(K.minimise(4, z)), "| SOP", K.sop_str(solved(*EXPOS)))
