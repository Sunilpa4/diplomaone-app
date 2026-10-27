"""DI03000011 Digital Electronics - Unit 4 diagrams: combinational circuits (adders, subtractors, encoder, decoder, MUX, DEMUX)."""
import os
from flowchart_lib import *
from diagrams_DI03000021_u1 import box, BLUE, BLUEF, GREEN, GREENF, ORANGE, ORANGEF, RED, REDF, YEL
from de_gates import gate, wire, dot, lab, tt_svg, truth, bexpr, minterms, equiv, GS, HI, WIRE
from de_comb import bus_circuit, block, eq_box, term, bar
from diagrams_DI03000011_u1 import note
import de_kmap as K

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "content", "computer", "sem3", "DI03000011", "diagrams")

# ------------------------------------------------------------------ the logic functions (checked against arithmetic)
HA = lambda a, b: (a ^ b, a & b)
FA = lambda a, b, c: (a ^ b ^ c, (a & b) | (b & c) | (a & c))
HS = lambda a, b: (a ^ b, (1 - a) & b)
FS = lambda a, b, c: (a ^ b ^ c, ((1 - a) & b) | ((1 - a) & c) | (b & c))
for a in (0, 1):
    for b_ in (0, 1):
        assert HA(a, b_) == ((a + b_) % 2, (a + b_) // 2)
        assert HS(a, b_) == ((a - b_) % 2, int(a - b_ < 0))
        for c in (0, 1):
            assert FA(a, b_, c) == ((a + b_ + c) % 2, (a + b_ + c) // 2)
            assert FS(a, b_, c) == ((a - b_ - c) % 2, int(a - b_ - c < 0))


def rows(f, n):
    from itertools import product
    return [(*bits, *f(*bits)) for bits in product((0, 1), repeat=n)]


def mins(f, n, k):
    return [i for i, r in enumerate(rows(f, n)) if r[n + k]]


FA_S, FA_C = mins(FA, 3, 0), mins(FA, 3, 1)
FS_D, FS_B = mins(FS, 3, 0), mins(FS, 3, 1)
assert (FA_S, FA_C, FS_B) == ([1, 2, 4, 7], [3, 5, 6, 7], [1, 2, 3, 7])


def tt_mid(y, head, rws, cw, out_cols, total_w=360):
    return tt_svg((total_w - cw * len(head)) / 2, y, head, rws, cw=cw, out_cols=out_cols)


# ------------------------------------------------------------------ 4.1
def comb():
    b = title("Combinational Circuit")
    bb, _ = block(118, 44, 124, 96, "Combinational\nLogic Circuit", ["X1", "X2", "Xn"], ["Y1", "Y2", "Ym"], lead=34, sub="(logic gates)")
    b += bb
    b += text(60, 158, "n inputs", 10, color="#666") + text(300, 158, "m outputs", 10, color="#666")
    b += note(12, 172, 336, ["Output depends ONLY on the present inputs.", "No memory, no clock, no feedback path.",
                             "Described by a truth table or Boolean equations."], size=9.6)
    y = 248
    b += rbox(180, y, 190, 30, "Combinational Circuits", F_PROC, P, 11.5, "bold")
    b += line(f"M180 {y + 15} L180 {y + 26} M95 {y + 26} L265 {y + 26} M95 {y + 26} L95 {y + 36} M265 {y + 26} L265 {y + 36}", INK, 1.5)
    b += rbox(95, y + 52, 160, 30, "Arithmetic / Logical", GREENF, GREEN, 10.5, "bold")
    b += rbox(265, y + 52, 160, 30, "Data Transmission", BLUEF, BLUE, 10.5, "bold")
    for i, (l, r) in enumerate(zip(["Half Adder", "Full Adder", "Half Subtractor", "Full Subtractor"],
                                   ["Encoder (4:2)", "Decoder (2:4)", "Multiplexer (4:1)", "Demultiplexer (1:4)"])):
        b += text(95, y + 88 + i * 17, l, 10) + text(265, y + 88 + i * 17, r, 10)
    return svg(360, y + 160, b)


def design():
    b = title("Design Procedure")
    steps = ["1. State the problem clearly", "2. Find number of inputs and outputs; name them",
             "3. Write the truth table", "4. Get the Boolean expression of each output",
             "5. Simplify each expression (K-map / algebra)", "6. Draw the logic diagram", "7. Verify (truth table / simulation)"]
    y = 40
    for i, s in enumerate(steps):
        fill, st = ((GREENF, GREEN) if i in (0, 6) else (F_PROC, P))
        b += rbox(180, y + 16, 300, 30, s, fill, st, 10.5)
        if i < len(steps) - 1:
            b += down(180, y + 31, y + 44)
        y += 44
    b += note(12, y + 6, 336, [("Example: Half adder", P), "Inputs: A, B (2)    Outputs: Sum S, Carry C (2)",
                               "S = A ⊕ B,  C = AB  → one XOR + one AND gate"], size=9.6)
    return svg(360, y + 66, b)


# ------------------------------------------------------------------ 4.2 adders
def ha():
    b = title("Half Adder: Block Diagram and Truth Table")
    bb, _ = block(110, 44, 120, 70, "Half Adder", ["A", "B"], ["S (Sum)", "C (Carry)"], lead=30, sub="(HA)")
    b += bb
    b += text(180, 136, "Adds two 1-bit numbers A and B", 10, color="#666")
    b += tt_mid(150, ["A", "B", "S", "C"], rows(HA, 2), 44, 2)
    b += eq_box(40, 260, 280, ["S = !AB + A!B = A ⊕ B", "C = AB"])
    b += text(180, 330, "1 + 1 = 10 (sum 0, carry 1)", 10, color="#666")
    return svg(360, 344, b)


def ha_logic():
    b = title("Half Adder: Logic Diagram")
    c, bot, _ = bus_circuit(["A", "B"], [dict(k="XOR", i=["A", "B"], y=20, o="S = A⊕B"),
                                         dict(k="AND", i=["A", "B"], y=90, o="C = AB")], x0=70, y0=50, pitch=24)
    b += c
    b += note(12, bot + 10, 336, ["XOR gate gives the Sum; AND gate gives the Carry.", "ICs: 7486 (XOR) and 7408 (AND).",
                                  "Limitation: no input for a carry from a previous stage."], size=9.6)
    return svg(360, bot + 70, b)


def fa():
    b = title("Full Adder: Block Diagram and Truth Table")
    bb, _ = block(112, 42, 120, 80, "Full Adder", ["A", "B", "Cin"], ["S (Sum)", "Cout"], lead=30, sub="(FA)")
    b += bb
    b += text(180, 142, "Adds three bits: A, B and carry-in Cin", 10, color="#666")
    b += tt_mid(154, ["A", "B", "Cin", "S", "Cout"], rows(FA, 3), 44, 2)
    y = 154 + 19 * 9 + 10
    b += eq_box(30, y, 300, ["S = Σm(1, 2, 4, 7)", "Cout = Σm(3, 5, 6, 7)"], size=11)
    return svg(360, y + 64, b)


def kmap_with_eq(x, y, ones, names, out_name, groups, rtxt, cell=34):
    m, (xe, ye) = K.kmap_svg(x, y, 3, ones, groups=groups, cell=cell, names=names)
    b = m + text(x + 2 * cell, y - 50, "K-map for " + out_name, 11, weight="bold", color=GS)
    for i, (s, col) in enumerate(rtxt):
        b += bexpr(xe + 12, y + 14 + i * 20, s, 10.5, anchor="start", color=col)
    return b, ye


def legend_terms(groups, names):
    out = []
    for gi, g in enumerate(groups):
        lits = [("!" if ch == "0" else "") + nm for nm, ch in zip(names, g) if ch != "-"]
        out.append((term(lits), K.COLORS[gi % len(K.COLORS)]))
    return out


def fa_kmap():
    b = title("Full Adder: K-map Simplification")
    nm = ["A", "B", "Cin"]
    gs = K.minimise(3, FA_S)
    m, ye = kmap_with_eq(64, 92, FA_S, nm, "S", [], [("No two 1s are", INK), ("adjacent: no", INK), ("grouping possible", INK)])
    b += m
    b += eq_box(12, ye + 10, 336, ["S = !A!B·Cin + !AB·!(Cin) + A!B·!(Cin) + AB·Cin", "= A ⊕ B ⊕ Cin"], size=10, lh=20)
    gc = K.minimise(3, FA_C)
    K.check(3, FA_C, (), gc)
    y2 = ye + 136
    lt = legend_terms(gc, nm)
    m, ye2 = kmap_with_eq(64, y2, FA_C, nm, "Cout", gc, lt)
    b += m
    b += eq_box(12, ye2 + 10, 336, ["Cout = AB + B·Cin + A·Cin"], size=11)
    assert len(gs) == 4 and sorted(t for t, _ in lt) == sorted(["AB", "B·Cin", "A·Cin"])
    return svg(360, ye2 + 54, b)


def fa_logic():
    b = title("Full Adder: Logic Diagram")
    gates = [dict(k="XOR", i=["A", "B"], y=20), dict(k="XOR", i=["g0", "Cin"], y=40, l=2, o="S"),
             dict(k="AND", i=["A", "B"], y=96), dict(k="AND", i=["B", "Cin"], y=146), dict(k="AND", i=["A", "Cin"], y=196),
             dict(k="OR", i=["g2", "g3", "g4"], y=146, l=2, o="Cout")]
    c, bot, _ = bus_circuit(["A", "B", "Cin"], gates, x0=40, y0=48, pitch=26)
    b += c
    b += eq_box(12, bot + 6, 336, ["S = A ⊕ B ⊕ Cin", "Cout = AB + B·Cin + A·Cin"], size=11)
    b += text(180, bot + 70, "Gates: 2 XOR, 3 AND, 1 three-input OR", 10, color="#666")
    return svg(360, bot + 84, b)


def fa_2ha():
    b = title("Full Adder using Two Half Adders")
    b += box(60, 60, 64, 60, "#F1E8FC", P, 8, 1.8) + text(92, 90, "HA1", 12, weight="bold", color=GS)
    b += box(176, 40, 64, 60, "#F1E8FC", P, 8, 1.8) + text(208, 70, "HA2", 12, weight="bold", color=GS)
    b += wire([(30, 75), (60, 75)]) + lab(26, 79, "A") + wire([(30, 105), (60, 105)]) + lab(26, 109, "B")
    b += wire([(30, 26), (166, 26), (166, 55), (176, 55)]) + lab(26, 30, "Cin")
    b += wire([(124, 75), (152, 75), (152, 85), (176, 85)]) + lab(140, 70, "S1", "middle", 9.5, BLUE)
    og, (ox, oy), oins = gate("OR", 262, 110)
    b += og
    b += wire([(240, 85), (254, 85), (254, oins[0][1]), oins[0]]) + lab(250, 80, "C2", "middle", 9.5, BLUE)
    b += wire([(124, 105), (140, 105), (140, 140), (246, 140), (246, oins[1][1]), oins[1]]) + lab(170, 135, "C1", "middle", 9.5, BLUE)
    b += wire([(240, 55), (320, 55)]) + lab(324, 59, "S", "start")
    b += wire([(ox, oy), (320, oy)]) + lab(324, oy + 4, "Cout", "start")
    b += eq_box(12, 160, 336, ["S1 = A ⊕ B,   C1 = AB", "S = S1 ⊕ Cin = A ⊕ B ⊕ Cin", "C2 = S1·Cin = (A ⊕ B)·Cin",
                               "Cout = C1 + C2 = AB + (A ⊕ B)·Cin"], size=10.5, lh=21)
    b += text(180, 268, "Cout = AB + (A⊕B)Cin is the same as AB + B·Cin + A·Cin", 9.4, color="#666")
    assert equiv(lambda a, b_, c: (a & b_) | ((a ^ b_) & c), lambda a, b_, c: FA(a, b_, c)[1], 3)
    return svg(360, 282, b)


# ------------------------------------------------------------------ 4.2 subtractors
def hs():
    b = title("Half Subtractor")
    bb, _ = block(56, 40, 96, 64, "Half\nSubtractor", ["A", "B"], ["D", "Bo"], lead=24, size=10)
    b += bb + text(104, 122, "A − B (two 1-bit numbers)", 9.4, color="#666")
    b += tt_svg(204, 38, ["A", "B", "D", "Bo"], rows(HS, 2), cw=34, out_cols=2)
    c, bot, _ = bus_circuit(["A", "B"], [dict(k="XOR", i=["A", "B"], y=16, o="D = A⊕B"),
                                         dict(k="AND", i=["!A", "B"], y=74, o="Bo = !AB")], x0=50, y0=152, pitch=24)
    b += c
    b += eq_box(12, bot + 6, 336, ["D = !AB + A!B = A ⊕ B", "Bo = !AB"], size=11)
    b += text(180, bot + 70, "0 − 1 = 1 with borrow 1  (D = Difference, Bo = Borrow)", 9.4, color="#666")
    return svg(360, bot + 84, b)


def fs():
    b = title("Full Subtractor: Block & Truth Table")
    bb, _ = block(112, 42, 120, 80, "Full\nSubtractor", ["A", "B", "Bin"], ["D", "Bout"], lead=30, sub="(FS)")
    b += bb
    b += text(180, 142, "Computes A − B − Bin (Bin = borrow-in)", 10, color="#666")
    b += tt_mid(154, ["A", "B", "Bin", "D", "Bout"], rows(FS, 3), 44, 2)
    y = 154 + 19 * 9 + 10
    b += eq_box(30, y, 300, ["D = Σm(1, 2, 4, 7)", "Bout = Σm(1, 2, 3, 7)"], size=11)
    return svg(360, y + 64, b)


def fs_logic():
    b = title("Full Subtractor: K-map and Logic")
    nm = ["A", "B", "Bin"]
    g = K.minimise(3, FS_B)
    K.check(3, FS_B, (), g)
    lt = legend_terms(g, nm)
    m, ye = kmap_with_eq(64, 92, FS_B, nm, "Bout", g, lt, cell=32)
    b += m
    assert sorted(t for t, _ in lt) == sorted(["!AB", "!A·Bin", "B·Bin"])
    b += eq_box(12, ye + 8, 336, ["D = A ⊕ B ⊕ Bin", "Bout = !AB + !A·Bin + B·Bin"], size=10.5, lh=20)
    gates = [dict(k="XOR", i=["A", "B"], y=14), dict(k="XOR", i=["g0", "Bin"], y=34, l=2, o="D"),
             dict(k="AND", i=["!A", "B"], y=88), dict(k="AND", i=["!A", "Bin"], y=136), dict(k="AND", i=["B", "Bin"], y=184),
             dict(k="OR", i=["g2", "g3", "g4"], y=136, l=2, o="Bout")]
    c, bot, _ = bus_circuit(["A", "B", "Bin"], gates, x0=24, y0=ye + 74, pitch=22, lvl_gap=72)
    b += c
    return svg(360, bot + 8, b)


# ------------------------------------------------------------------ 4.3 data transmission
ENC_ROWS = [(0, 0, 0, 1, 0, 0), (0, 0, 1, 0, 0, 1), (0, 1, 0, 0, 1, 0), (1, 0, 0, 0, 1, 1)]
for r in ENC_ROWS:
    d3, d2, d1, d0, y1, y0 = r
    assert (y1, y0) == (d2 | d3, d1 | d3)


def enc():
    b = title("4-to-2 Encoder")
    bb, _ = block(46, 40, 90, 92, "4 : 2\nEncoder", ["D0", "D1", "D2", "D3"], ["Y1", "Y0"], lead=24, size=10)
    b += bb
    b += tt_svg(188, 44, ["D3", "D2", "D1", "D0", "Y1", "Y0"], ENC_ROWS, cw=26, out_cols=2)
    b += text(266, 152, "(only one input high at a time)", 8.8, color="#666")
    c, bot, _ = bus_circuit(["D0", "D1", "D2", "D3"], [dict(k="OR", i=["D2", "D3"], y=10, o="Y1 = D2 + D3"),
                                                     dict(k="OR", i=["D1", "D3"], y=70, o="Y0 = D1 + D3")],
                            x0=40, y0=184, pitch=26)
    b += c
    b += note(12, bot + 6, 336, ["2ⁿ inputs → n-bit binary code (here 4 → 2).", "D0 is not connected: it gives Y1Y0 = 00.",
                                 "Uses two 2-input OR gates (IC 7432)."], size=9.6)
    return svg(360, bot + 66, b)


def dec():
    b = title("2-to-4 Decoder")
    bb, _ = block(36, 40, 84, 92, "2 : 4\nDecoder", ["A", "B"], ["Y0", "Y1", "Y2", "Y3"], lead=20, size=10)
    b += bb
    drows = [(a, b_, *[int(2 * a + b_ == k) for k in range(4)]) for a in (0, 1) for b_ in (0, 1)]
    b += tt_svg(186, 44, ["A", "B", "Y0", "Y1", "Y2", "Y3"], drows, cw=26, out_cols=4)
    b += text(264, 152, "(A = MSB)", 9, color="#666")
    gates = [dict(k="AND", i=["!A", "!B"], y=12, o="Y0 = !A!B"), dict(k="AND", i=["!A", "B"], y=60, o="Y1 = !AB"),
             dict(k="AND", i=["A", "!B"], y=108, o="Y2 = A!B"), dict(k="AND", i=["A", "B"], y=156, o="Y3 = AB")]
    c, bot, _ = bus_circuit(["A", "B"], gates, x0=60, y0=186, pitch=22)
    b += c
    b += note(12, bot + 6, 336, ["n inputs → 2ⁿ outputs; exactly one output is 1.", "Each output is one minterm of the inputs.",
                                 "With an enable input E, every AND gate gets E."], size=9.6)
    return svg(360, bot + 66, b)


def mux():
    b = title("4-to-1 Multiplexer: Block Diagram")
    bb, _ = block(110, 44, 110, 110, "4 : 1\nMUX", ["I0", "I1", "I2", "I3"], ["Y"], lead=30, bottom=["S1", "S0"])
    b += bb
    b += text(60, 172, "data inputs", 9.4, color="#666") + text(165, 210, "select lines", 9.4, color="#666")
    b += text(268, 122, "1 output", 9.4, color="#666")
    b += tt_svg(110, 230, ["S1", "S0", "Y"], [(0, 0, "I0"), (0, 1, "I1"), (1, 0, "I2"), (1, 1, "I3")], cw=46, out_cols=1)
    b += note(12, 336, 336, ["Selects ONE of many inputs and sends it to the output.", "2ⁿ data inputs need n select lines (4 → 2).",
                             "Also called a data selector; 'many to one'."], size=9.6)
    return svg(360, 396, b)


def mux_logic():
    b = title("4-to-1 Multiplexer: Logic Diagram")
    gates = [dict(k="AND", i=["!S1", "!S0", "I0"], y=12), dict(k="AND", i=["!S1", "S0", "I1"], y=62),
             dict(k="AND", i=["S1", "!S0", "I2"], y=112), dict(k="AND", i=["S1", "S0", "I3"], y=162),
             dict(k="OR", i=["g0", "g1", "g2", "g3"], y=87, l=2, o="Y")]
    c, bot, _ = bus_circuit(["S1", "S0", "I0", "I1", "I2", "I3"], gates, x0=20, y0=46, pitch=17, lvl_gap=64, out_pad=12)
    b += c
    b += eq_box(12, bot + 6, 336, ["Y = !(S1)!(S0)I0 + !(S1)S0I1", "+ S1!(S0)I2 + S1S0I3"], size=11, lh=21)
    return svg(360, bot + 60, b)


def demux():
    b = title("1-to-4 Demultiplexer: Block Diagram")
    bb, _ = block(130, 44, 100, 110, "1 : 4\nDEMUX", ["D"], ["Y0", "Y1", "Y2", "Y3"], lead=30, bottom=["S1", "S0"])
    b += bb
    b += text(84, 86, "data input", 9.4, color="#666") + text(180, 210, "select lines", 9.4, color="#666")
    drows = [(s1, s0, *["D" if 2 * s1 + s0 == k else 0 for k in range(4)]) for s1 in (0, 1) for s0 in (0, 1)]
    b += tt_svg(87, 230, ["S1", "S0", "Y0", "Y1", "Y2", "Y3"], drows, cw=31, out_cols=4)
    b += note(12, 336, 336, ["Sends ONE input to one of many outputs.", "n select lines choose one of 2ⁿ outputs (1 → 4).",
                             "Also called a data distributor; 'one to many'."], size=9.6)
    return svg(360, 396, b)


def demux_logic():
    b = title("1-to-4 Demultiplexer: Logic Diagram")
    gates = [dict(k="AND", i=["D", "!S1", "!S0"], y=12, o="Y0"), dict(k="AND", i=["D", "!S1", "S0"], y=62, o="Y1"),
             dict(k="AND", i=["D", "S1", "!S0"], y=112, o="Y2"), dict(k="AND", i=["D", "S1", "S0"], y=162, o="Y3")]
    c, bot, _ = bus_circuit(["D", "S1", "S0"], gates, x0=40, y0=46, pitch=26)
    b += c
    b += eq_box(12, bot + 6, 336, ["Y0 = D!(S1)!(S0)    Y1 = D!(S1)S0", "Y2 = DS1!(S0)    Y3 = DS1S0"], size=10.5, lh=21)
    b += text(180, bot + 66, "With D = 1 it works as a 2-to-4 decoder (D = enable).", 9.4, color="#666")
    return svg(360, bot + 80, b)


def compare():
    b = title("Data Transmission Circuits at a Glance")
    cards = [("Encoder", "2ⁿ inputs → n outputs", "4 → 2", GREENF, GREEN, 4, 2, False),
             ("Decoder", "n inputs → 2ⁿ outputs", "2 → 4", BLUEF, BLUE, 2, 4, False),
             ("Multiplexer", "2ⁿ inputs → 1 output", "4 → 1", ORANGEF, ORANGE, 4, 1, True),
             ("Demultiplexer", "1 input → 2ⁿ outputs", "1 → 4", REDF, RED, 1, 4, True)]
    for k, (nm, rule, short, f, s, ni, no, sel) in enumerate(cards):
        x = 12 + (k % 2) * 172
        y = 38 + (k // 2) * 150
        b += box(x, y, 164, 140, f, s, 9, 1.4) + text(x + 82, y + 18, nm, 12, weight="bold", color=s)
        b += box(x + 58, y + 34, 48, 60, "#fff", s, 5, 1.4)
        for i in range(ni):
            yy = y + 34 + 60 * (i + 1) / (ni + 1)
            b += wire([(x + 30, yy), (x + 58, yy)])
        for i in range(no):
            yy = y + 34 + 60 * (i + 1) / (no + 1)
            b += wire([(x + 106, yy), (x + 134, yy)])
        if sel:
            b += wire([(x + 74, y + 94), (x + 74, y + 104)]) + wire([(x + 90, y + 94), (x + 90, y + 104)])
            b += text(x + 82, y + 113, "select", 8.4, color="#666")
        b += text(x + 82, y + 66, short, 8.6, weight="bold", color=s)
        b += text(x + 82, y + 130, rule, 9.4)
    b += note(12, 344, 336, ["Encoder ↔ Decoder are opposite operations.", "MUX ↔ DEMUX are opposite operations.",
                             "A DEMUX with input D = 1 acts as a decoder."], size=9.6)
    return svg(360, 404, b)


DIAGRAMS = {"de4_comb": comb, "de4_design": design, "de4_ha": ha, "de4_ha_logic": ha_logic, "de4_fa": fa, "de4_fa_kmap": fa_kmap,
            "de4_fa_logic": fa_logic, "de4_fa_2ha": fa_2ha, "de4_hs": hs, "de4_fs": fs, "de4_fs_logic": fs_logic,
            "de4_enc": enc, "de4_dec": dec, "de4_mux": mux, "de4_mux_logic": mux_logic, "de4_demux": demux,
            "de4_demux_logic": demux_logic, "de4_compare": compare}

if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    for k, f in DIAGRAMS.items():
        with open(os.path.join(OUT, k + ".svg"), "w", encoding="utf-8") as fh:
            fh.write(f())
    print("written", len(DIAGRAMS))
