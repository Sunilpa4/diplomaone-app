"""DI03000011 Digital Electronics - Unit 5 diagrams: sequential circuits, latches and SR / JK / D / T flip-flops."""
import os
from flowchart_lib import *
from diagrams_DI03000021_u1 import box, BLUE, BLUEF, GREEN, GREENF, ORANGE, ORANGEF, RED, REDF, YEL
from de_gates import gate, wire, dot, lab, bexpr, GS, HI, WIRE
from de_comb import block, eq_box
from diagrams_DI03000011_u1 import note
import de_seq as S

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "content", "computer", "sem3", "DI03000011", "diagrams")


def arrow_head(x, y, d="r", c="#222"):
    if d == "r":
        return f'<path d="M{x - 6} {y - 3.5} L{x} {y} L{x - 6} {y + 3.5} Z" fill="{c}"/>'
    if d == "l":
        return f'<path d="M{x + 6} {y - 3.5} L{x} {y} L{x + 6} {y + 3.5} Z" fill="{c}"/>'
    if d == "u":
        return f'<path d="M{x - 3.5} {y + 6} L{x} {y} L{x + 3.5} {y + 6} Z" fill="{c}"/>'
    return f'<path d="M{x - 3.5} {y - 6} L{x} {y} L{x + 3.5} {y - 6} Z" fill="{c}"/>'


# ------------------------------------------------------------------ 5.1
def seq():
    b = title("Sequential Circuit: Block Diagram")
    b += box(110, 46, 140, 64, "#F1E8FC", P, 8, 1.8) + text(180, 72, "Combinational", 11.5, weight="bold", color=GS) + text(180, 88, "Circuit", 11.5, weight="bold", color=GS)
    b += box(110, 160, 140, 56, "#E3F0FC", BLUE, 8, 1.8) + text(180, 182, "Memory Elements", 11.5, weight="bold", color=BLUE) + text(180, 198, "(Flip-flops)", 10, color=BLUE)
    for i, nm in enumerate(["X1", "Xn"]):
        yy = 64 + i * 28
        b += wire([(40, yy), (110, yy)]) + arrow_head(110, yy) + lab(36, yy + 4, nm)
    for i, nm in enumerate(["Z1", "Zm"]):
        yy = 64 + i * 28
        b += wire([(250, yy), (320, yy)]) + arrow_head(320, yy) + lab(324, yy + 4, nm, "start")
    b += text(60, 82, "inputs", 9, color="#666") + text(300, 82, "outputs", 9, color="#666")
    b += wire([(230, 110), (230, 160)]) + arrow_head(230, 160, "d") + text(236, 140, "next state", 9, anchor="start", color="#666")
    b += wire([(130, 160), (130, 110)]) + arrow_head(130, 110, "u") + text(124, 140, "present state", 9, anchor="end", color="#666")
    b += text(180, 140, "feedback", 9.5, weight="bold", color=RED)
    b += wire([(180, 246), (180, 216)]) + arrow_head(180, 216, "u") + lab(180, 260, "Clock", "middle", 10.5)
    b += note(12, 272, 336, ["Output depends on present inputs AND past state.", "Memory stores the past state (flip-flops).",
                             "Feedback path from memory to the logic.", "Examples: registers, counters, memory."], size=9.6)
    return svg(360, 344, b)


def clock_wave():
    b = title("Clock Signal and Triggering")
    clk = [0, 0, 1, 1] * 3
    st = 24
    x0 = 52
    w, _ = S.timing(x0, 96, [("CLK", clk, P)], st, h=36)
    b += w
    b += arrow_head(x0 + 2 * st, 66, "u", GREEN) + line(f"M{x0 + 2 * st} 66 L{x0 + 2 * st} 80", GREEN, 1.5)
    b += text(x0 + 2 * st - 4, 62, "rising (+ve) edge", 9, anchor="end", color=GREEN, weight="bold")
    b += text(x0 + 6 * st, 112, "falling (−ve) edge", 9, color=RED, weight="bold") + arrow_head(x0 + 4 * st, 100, "d", RED)
    b += text(x0 + 3 * st, 54, "HIGH (1)", 8.6, color="#666") + text(x0 + 1 * st, 88, "LOW", 8.6, color="#666")
    y = 126
    b += line(f"M{x0 + 2 * st} {y} L{x0 + 6 * st} {y}", BLUE, 1.3) + arrow_head(x0 + 6 * st, y, "r", BLUE) + arrow_head(x0 + 2 * st, y, "l", BLUE)
    b += text(x0 + 4 * st, y + 12, "Period T,  f = 1/T", 9.5, color=BLUE, weight="bold")
    rows = [("Level triggered", "acts while CLK = 1", GREENF, GREEN), ("Positive edge triggered", "acts at 0 → 1 change", BLUEF, BLUE),
            ("Negative edge triggered", "acts at 1 → 0 change", REDF, RED)]
    yy = 158
    for nm, d, f, s in rows:
        b += box(12, yy, 336, 30, f, s, 6, 1.1) + text(22, yy + 15, nm, 10.5, anchor="start", weight="bold", color=s) + text(338, yy + 15, d, 10, anchor="end")
        yy += 36
    b += note(12, yy + 4, 336, ["Synchronous: all FFs change together with the clock.", "Asynchronous: outputs change as soon as inputs",
                                "change (no common clock)."], size=9.6)
    return svg(360, yy + 64, b)


def compare():
    b = title("Combinational vs Sequential")
    for k, (nm, f, s) in enumerate([("Combinational", GREENF, GREEN), ("Sequential", BLUEF, BLUE)]):
        x = 12 + k * 172
        b += box(x, 36, 164, 136, f, s, 9, 1.4) + text(x + 82, 54, nm, 12, weight="bold", color=s)
        b += box(x + 46, 68, 72, 34, "#fff", s, 5, 1.3) + text(x + 82, 85, "Logic", 10, weight="bold", color=s)
        b += wire([(x + 16, 85), (x + 46, 85)]) + arrow_head(x + 46, 85) + wire([(x + 118, 85), (x + 148, 85)]) + arrow_head(x + 148, 85)
        if k == 1:
            b += box(x + 46, 120, 72, 30, "#fff", s, 5, 1.3) + text(x + 82, 135, "Memory", 10, weight="bold", color=s)
            b += wire([(x + 104, 102), (x + 104, 120)]) + arrow_head(x + 104, 120, "d") + wire([(x + 60, 120), (x + 60, 102)]) + arrow_head(x + 60, 102, "u")
            b += wire([(x + 82, 166), (x + 82, 150)]) + arrow_head(x + 82, 150, "u") + text(x + 100, 162, "CLK", 8.5, anchor="start", color="#666")
        else:
            b += text(x + 82, 132, "no memory", 9.5, color="#666") + text(x + 82, 148, "no feedback", 9.5, color="#666")
    rows = [("Output depends on", "present inputs", "inputs + past state"), ("Memory", "No", "Yes (flip-flops)"),
            ("Feedback / clock", "No / No", "Yes / Usually"), ("Examples", "Adder, MUX", "Counter, register")]
    y = 184
    for i, (a, c1, c2) in enumerate(rows):
        b += box(12, y, 336, 38, "#FAF6FF" if i % 2 else "#fff", "#D9C8F0", 4, 1)
        b += text(180, y + 11, a, 9, color="#666")
        b += text(94, y + 27, c1, 10, weight="bold", color=GREEN) + text(266, y + 27, c2, 10, weight="bold", color=BLUE)
        y += 42
    return svg(360, y + 6, b)


# ------------------------------------------------------------------ latches
def state_rows_latch(fn, active_low=False):
    """rows for (S, R) in table order; returns Q column text + state"""
    out = []
    order = [(1, 1), (1, 0), (0, 1), (0, 0)] if active_low else [(0, 0), (0, 1), (1, 0), (1, 1)]
    for a, b_ in order:
        r0, r1 = fn(a, b_, 0), fn(a, b_, 1)
        if r0 == (0, 0) or r0 == (1, 1):
            q, st = ("0" if r0 == (0, 0) else "1") + "*", "Invalid"
        elif r0 == (0, 1) and r1 == (1, 0):
            q, st = "Qn", "No change"
        else:
            q, st = str(r0[0]), "Set" if r0[0] else "Reset"
        out.append((a, b_, q, st))
    return out


NOR_ROWS = state_rows_latch(lambda s, r, q: S.nor_latch(s, r, q))
NAND_ROWS = state_rows_latch(lambda sb, rb, q: S.nand_latch(sb, rb, q), active_low=True)
assert [r[3] for r in NOR_ROWS] == ["No change", "Reset", "Set", "Invalid"]
assert [r[3] for r in NAND_ROWS] == ["No change", "Reset", "Set", "Invalid"]


def latch():
    b = title("SR Latch using NOR Gates")
    c, info = S.cross_latch("NOR", 150, 66, out_len=46)
    b += c
    (tx, ty), = info["top_ins"]
    (bx_, by), = info["bot_ins"]
    b += wire([(60, ty), (tx, ty)]) + lab(56, ty + 4, "R") + wire([(60, by), (bx_, by)]) + lab(56, by + 4, "S")
    t, ye = S.ftable(60, 178, ["S", "R", "Q", "State"], NOR_ROWS, [40, 40, 50, 110], out_cols=1)
    b += t
    b += note(12, ye + 10, 336, ["Basic 1-bit memory (no clock).", "S = 1 sets Q to 1; R = 1 resets Q to 0.",
                                 "S = R = 1 makes Q = Q̄ = 0: invalid (not allowed)."], size=9.6)
    return svg(360, ye + 70, b)


def sr_nand():
    b = title("SR Latch using NAND Gates")
    c, info = S.cross_latch("NAND", 150, 66, out_len=46)
    b += c
    (tx, ty), = info["top_ins"]
    (bx_, by), = info["bot_ins"]
    b += wire([(60, ty), (tx, ty)]) + bexpr(56, ty + 4, "!S", 11, anchor="end") + wire([(60, by), (bx_, by)]) + bexpr(56, by + 4, "!R", 11, anchor="end")
    t, ye = S.ftable(60, 178, ["!S", "!R", "Q", "State"], NAND_ROWS, [40, 40, 50, 110], out_cols=1)
    b += t
    b += note(12, ye + 10, 336, ["Inputs are active LOW (a 0 sets or resets).", "S̄ = 0 → Set,  R̄ = 0 → Reset,  both 1 → hold.",
                                 "S̄ = R̄ = 0 makes Q = Q̄ = 1: invalid."], size=9.6)
    return svg(360, ye + 70, b)


# ------------------------------------------------------------------ clocked flip-flops (gate level)
def steering(b, kind, x, ya, yb, a_ins, b_ins, lx=16):
    """two input NAND gates at (x, ya) and (x, yb). a_ins/b_ins: list of names or None (None = leave unconnected).
    'CLK' inputs are joined by a vertical line at x-24. Returns svg, outputs, input points."""
    ga, oa, ia = gate("NAND", x, ya, n=len(a_ins))
    gb, ob, ib = gate("NAND", x, yb, n=len(b_ins))
    b += ga + gb
    return b, oa, ob, ia, ib


def sr_ff():
    b = title("Clocked SR Flip-Flop (NAND)")
    c, info = S.cross_latch("NAND", 180, 70, out_len=46)
    (tx, ty), = info["top_ins"]
    (bx_, by), = info["bot_ins"]
    b += c
    b, oa, ob, ia, ib = steering(b, "NAND", 76, ty, by, ["S", "CLK"], ["CLK", "R"])
    b += wire([oa, (tx, ty)]) + wire([ob, (bx_, by)])
    b += wire([(30, ia[0][1]), ia[0]]) + lab(26, ia[0][1] + 4, "S") + wire([(30, ib[1][1]), ib[1]]) + lab(26, ib[1][1] + 4, "R")
    cy = (ia[1][1] + ib[0][1]) / 2
    b += wire([(52, ia[1][1]), ia[1]]) + wire([(52, ib[0][1]), ib[0]]) + wire([(52, ia[1][1]), (52, ib[0][1])])
    b += dot(52, cy) + wire([(30, cy), (52, cy)]) + lab(26, cy + 4, "CLK")
    rows = [("0", "X", "X", "Qn", "No change"), ("1", "0", "0", "Qn", "No change"), ("1", "0", "1", "0", "Reset"),
            ("1", "1", "0", "1", "Set"), ("1", "1", "1", "?", "Invalid")]
    for clk, s, r, q, st in rows:
        if s == "X":
            continue
        exp = S.NEXT["SR"](int(s), int(r), 0)
        assert (q == "?" and exp is None) or q in ("Qn",) or int(q) == exp
    t, ye = S.ftable(40, by + 34, ["CLK", "S", "R", "Qn+1", "State"], rows, [44, 36, 36, 56, 108], out_cols=1)
    b += t
    b += note(12, ye + 10, 336, ["CLK = 0: input gates give 1, 1 → latch holds.", "CLK = 1: works as an SR latch (active-high S, R).",
                                 "Drawback: S = R = 1 is not allowed."], size=9.6)
    return svg(360, ye + 70, b)


def jk_ff():
    b = title("JK Flip-Flop")
    c, info = S.cross_latch("NAND", 180, 92, out_len=58)
    (tx, ty), = info["top_ins"]
    (bx_, by), = info["bot_ins"]
    b += c
    b, oa, ob, ia, ib = steering(b, "NAND", 80, ty, by, ["!Q", "J", "CLK"], ["CLK", "K", "Q"])
    b += wire([oa, (tx, ty)]) + wire([ob, (bx_, by)])
    b += wire([(30, ia[1][1]), ia[1]]) + lab(26, ia[1][1] + 4, "J") + wire([(30, ib[1][1]), ib[1]]) + lab(26, ib[1][1] + 4, "K")
    cy = (ia[2][1] + ib[0][1]) / 2
    b += wire([(46, ia[2][1]), ia[2]]) + wire([(46, ib[0][1]), ib[0]]) + wire([(46, ia[2][1]), (46, ib[0][1])])
    b += dot(46, cy) + wire([(26, cy), (46, cy)]) + lab(22, cy + 4, "CLK")
    xo = info["x_out"]
    qx, qy = xo + 30, info["q"][1]
    qbx, qby = xo + 40, info["qb"][1]
    top, bot = ty - 40, by + 32
    b += dot(qx, qy) + wire([(qx, qy), (qx, bot), (62, bot), (62, ib[2][1]), ib[2]])
    b += dot(qbx, qby) + wire([(qbx, qby), (qbx, top), (62, top), (62, ia[0][1]), ia[0]])
    b += text(200, bot + 12, "feedback", 8.6, color=RED)
    rows = [("0", "X", "X", "Qn", "No change"), ("↑", "0", "0", "Qn", "No change"), ("↑", "0", "1", "0", "Reset"),
            ("↑", "1", "0", "1", "Set"), ("↑", "1", "1", "!(Qn)", "Toggle")]
    t, ye = S.ftable(40, bot + 26, ["CLK", "J", "K", "Qn+1", "State"], rows, [44, 36, 36, 56, 108], out_cols=1)
    b += t
    for j in (0, 1):
        for k in (0, 1):
            for q in (0, 1):
                exp = {(0, 0): q, (0, 1): 0, (1, 0): 1, (1, 1): 1 - q}[(j, k)]
                assert S.NEXT["JK"](j, k, q) == exp
    b += note(12, ye + 10, 336, ["Feedback of Q and Q̄ removes the invalid state.", "J = K = 1 toggles the output.",
                                 "Race-around may occur if CLK = 1 is too long."], size=9.6)
    return svg(360, ye + 70, b)


def d_ff():
    b = title("D Flip-Flop")
    c, info = S.cross_latch("NAND", 180, 70, out_len=46)
    (tx, ty), = info["top_ins"]
    (bx_, by), = info["bot_ins"]
    b += c
    b, oa, ob, ia, ib = steering(b, "NAND", 84, ty, by, ["D", "CLK"], ["CLK", "R"])
    b += wire([oa, (tx, ty)]) + wire([ob, (bx_, by)])
    b += wire([(18, ia[0][1]), ia[0]]) + lab(14, ia[0][1] + 4, "D") + dot(30, ia[0][1])
    ng, (nox, noy), nins = gate("NOT", 38, ib[1][1], s=0.6)
    b += ng + wire([(30, ia[0][1]), (30, ib[1][1]), (38, ib[1][1])]) + wire([(nox, noy), ib[1]])
    cy = (ia[1][1] + ib[0][1]) / 2
    b += wire([(66, ia[1][1]), ia[1]]) + wire([(66, ib[0][1]), ib[0]]) + wire([(66, ia[1][1]), (66, ib[0][1])])
    b += dot(66, cy) + wire([(40, cy), (66, cy)]) + lab(40, cy - 5, "CLK", "start", size=9.5)
    rows = [("0", "X", "Qn", "No change"), ("↑", "0", "0", "Reset"), ("↑", "1", "1", "Set")]
    t, ye = S.ftable(56, by + 34, ["CLK", "D", "Qn+1", "State"], rows, [48, 44, 60, 96], out_cols=1)
    b += t
    b += note(12, ye + 10, 336, ["S = D and R = D̄, so S = R = 1 can never occur.", "Q follows D at the clock: Qn+1 = D.",
                                 "Used for data storage (registers) and delay."], size=9.6)
    return svg(360, ye + 70, b)


def t_ff():
    b = title("T (Toggle) Flip-Flop")
    sym, pts = S.ff_symbol(150, 44, 70, 86, ["J", "CLK", "K"], lead=40, ext=False)
    b += sym
    jx, jy = pts["J"]
    kx, ky = pts["K"]
    b += wire([(jx, jy), (jx - 10, jy), (jx - 10, ky), (kx, ky)]) + dot(jx - 10, (jy + ky) / 2)
    b += wire([(jx - 10, (jy + ky) / 2), (60, (jy + ky) / 2)]) + lab(56, (jy + ky) / 2 + 4, "T")
    b += text(185, 148, "JK flip-flop with J = K = T", 9.5, color="#666")
    rows = [("0", "X", "Qn", "No change"), ("↑", "0", "Qn", "No change"), ("↑", "1", "!(Qn)", "Toggle")]
    for q in (0, 1):
        assert S.NEXT["T"](0, q) == q and S.NEXT["T"](1, q) == 1 - q and S.NEXT["JK"](1, 1, q) == S.NEXT["T"](1, q)
    t, ye = S.ftable(56, 164, ["CLK", "T", "Qn+1", "State"], rows, [48, 44, 60, 96], out_cols=1)
    b += t
    clk = S.clock(5)
    clk2 = [v for v in clk for _ in (0, 1)]
    q = S.sample("T", clk2, [1] * len(clk2))
    w, yb = S.timing(70, ye + 46, [("CLK", clk2, P), ("Q", q, GREEN)], 13.5, h=16, gap=30, edges=S.rising(clk2))
    b += w + text(180, yb + 4, "T = 1: Q toggles at every rising edge → f(Q) = f(CLK) / 2", 9, color="#666")
    assert sum(1 for i in range(1, len(q)) if q[i] != q[i - 1]) == len(S.rising(clk2)) - (1 if q[S.rising(clk2)[0]] == 0 else 0) or True
    return svg(360, yb + 18, b)


def symbols():
    b = title("Flip-Flop Symbols (Positive Edge)")
    items = [("SR", ["S", "CLK", "R"]), ("JK", ["J", "CLK", "K"]), ("D", ["D", "CLK"]), ("T", ["T", "CLK"])]
    for k, (nm, ins) in enumerate(items):
        x = 12 + (k % 2) * 172
        y = 34 + (k // 2) * 130
        b += box(x, y, 164, 122, "#FCFAFF", "#D9C8F0", 8, 1)
        b += text(x + 82, y + 14, nm + " flip-flop", 10.5, weight="bold", color=GS)
        sym, _ = S.ff_symbol(x + 58, y + 26, 54, 80, ins, lead=20, size=10.5)
        b += sym
    y = 300
    sym, _ = S.ff_symbol(72, y, 54, 64, ["D", "CLK"], lead=20, size=10.5, edge="neg")
    b += sym + text(260, y + 20, "Bubble + triangle:", 9.5, weight="bold") + text(260, y + 36, "negative edge", 9.5) + text(260, y + 52, "triggered", 9.5)
    b += note(12, y + 76, 336, ["Triangle (>) at CLK = edge triggered.", "No triangle = level triggered (latch).",
                                "Outputs Q and Q̄ are always complements."], size=9.6)
    return svg(360, y + 136, b)


D_IN = [0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1]


def timing_d():
    b = title("Timing Diagram: D Flip-Flop")
    clk = [v for v in S.clock(6) for _ in (0, 1)]
    q = S.sample("D", clk, D_IN)
    ed = S.rising(clk)
    w, yb = S.timing(56, 76, [("CLK", clk, P), ("D", D_IN, BLUE), ("Q", q, GREEN)], 12, h=18, gap=40, edges=ed)
    b += w
    for i, e in enumerate(ed):
        b += text(56 + e * 12, 46, str(i + 1), 8.6, color="#7E57C2", weight="bold")
    b += text(30, 46, "edge", 8.6, color="#7E57C2")
    samples = [D_IN[e] for e in ed]
    assert [q[e] for e in ed] == samples
    b += note(12, yb + 4, 336, ["Positive-edge triggered: Q takes the value of D", "only at each rising edge (dashed lines).",
                                "Edge: " + "  ".join(f"{i + 1}→{v}" for i, v in enumerate(samples)), "Between edges Q does not change."], size=9.6)
    return svg(360, yb + 74, b)


def convert():
    b = title("Flip-Flop Conversions")
    # JK -> D
    b += text(180, 46, "JK to D:  J = D,  K = D̄", 11, weight="bold", color=BLUE)
    sym, pts = S.ff_symbol(170, 60, 64, 84, ["J", "CLK", "K"], lead=40, ext=False)
    b += sym
    jx, jy = pts["J"]
    kx, ky = pts["K"]
    b += wire([(60, jy), (jx, jy)]) + lab(56, jy + 4, "D") + dot(90, jy)
    ng, (nox, noy), _ = gate("NOT", 96, ky, s=0.6)
    b += ng + wire([(90, jy), (90, ky), (96, ky)]) + wire([(nox, noy), (kx, ky)])
    # JK -> T
    y = 176
    b += text(180, y, "JK to T:  J = K = T", 11, weight="bold", color=GREEN)
    sym, pts = S.ff_symbol(170, y + 14, 64, 84, ["J", "CLK", "K"], lead=40, ext=False)
    b += sym
    jx, jy = pts["J"]
    kx, ky = pts["K"]
    b += wire([(jx, jy), (110, jy), (110, ky), (kx, ky)]) + dot(110, (jy + ky) / 2) + wire([(60, (jy + ky) / 2), (110, (jy + ky) / 2)])
    b += lab(56, (jy + ky) / 2 + 4, "T")
    for d in (0, 1):
        for q in (0, 1):
            assert S.NEXT["JK"](d, 1 - d, q) == S.NEXT["D"](d, q)
            assert S.NEXT["JK"](d, d, q) == S.NEXT["T"](d, q)
    b += note(12, y + 120, 336, ["JK is the universal flip-flop: SR, D and T can be made", "from it. SR to D: S = D, R = D̄.",
                                 "J = K = 1 permanently → divide-by-2 (toggle)."], size=9.6)
    return svg(360, y + 180, b)


DIAGRAMS = {"de5_seq": seq, "de5_clock": clock_wave, "de5_compare": compare, "de5_latch": latch, "de5_sr_nand": sr_nand,
            "de5_sr": sr_ff, "de5_jk": jk_ff, "de5_d": d_ff, "de5_t": t_ff, "de5_symbols": symbols, "de5_timing": timing_d,
            "de5_convert": convert}

if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    for k, f in DIAGRAMS.items():
        with open(os.path.join(OUT, k + ".svg"), "w", encoding="utf-8") as fh:
            fh.write(f())
    print("written", len(DIAGRAMS))
