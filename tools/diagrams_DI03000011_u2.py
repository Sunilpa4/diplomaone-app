"""DI03000011 Digital Electronics - Unit 2 diagrams: binary logic, logic gates, universal gates, Boolean algebra."""
import os
from flowchart_lib import *
from diagrams_DI03000021_u1 import box, BLUE, BLUEF, GREEN, GREENF, ORANGE, ORANGEF, RED, REDF, YEL
from de_gates import gate, wire, dot, lab, simple_gate, tt_svg, truth, OPS, bexpr, minterms, GS, HI, WIRE, _bubble
from diagrams_DI03000011_u1 import note

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "content", "computer", "sem3", "DI03000011", "diagrams")


# ------------------------------------------------------------------ small circuit parts
def switch(x, y, name):
    b = f'<circle cx="{x}" cy="{y}" r="2.6" fill="#fff" stroke="{WIRE}" stroke-width="1.5"/>'
    b += f'<circle cx="{x + 26}" cy="{y}" r="2.6" fill="#fff" stroke="{WIRE}" stroke-width="1.5"/>'
    b += line(f"M{x + 2} {y - 1} L{x + 24} {y - 11}", WIRE, 1.6) + text(x + 13, y - 16, name, 10, weight="bold", color=BLUE)
    return b


def lamp(cx, cy):
    return (f'<circle cx="{cx}" cy="{cy}" r="9" fill="{YEL}" stroke="{WIRE}" stroke-width="1.5"/>'
            + line(f"M{cx - 6} {cy - 6} L{cx + 6} {cy + 6} M{cx + 6} {cy - 6} L{cx - 6} {cy + 6}", WIRE, 1.2))


def battery(x, y1, y2):
    m = (y1 + y2) / 2
    return (wire([(x, y1), (x, m - 4)]) + line(f"M{x - 10} {m - 4} L{x + 10} {m - 4}", WIRE, 2) +
            line(f"M{x - 5} {m + 3} L{x + 5} {m + 3}", WIRE, 3) + wire([(x, m + 3), (x, y2)]) + text(x - 14, m, "V", 9, color="#666"))


def series_circuit(y0):
    T, B = y0, y0 + 50
    b = battery(30, T, B) + wire([(30, T), (80, T)]) + switch(80, T, "A") + wire([(106, T), (150, T)]) + switch(150, T, "B")
    b += wire([(176, T), (221, T)]) + lamp(230, T) + wire([(239, T), (290, T), (290, B), (30, B)]) + text(230, T + 22, "Y (lamp)", 9, color="#666")
    return b


def parallel_circuit(y0):
    T, B = y0, y0 + 64
    b = battery(30, T, B) + wire([(30, T), (90, T)]) + switch(90, T, "A") + wire([(116, T), (170, T)])
    b += wire([(70, T), (70, T + 30), (90, T + 30)]) + switch(90, T + 30, "B") + wire([(116, T + 30), (150, T + 30), (150, T)])
    b += dot(70, T) + dot(150, T) + wire([(170, T), (221, T)]) + lamp(230, T) + wire([(239, T), (290, T), (290, B), (30, B)])
    b += text(230, T + 22, "Y (lamp)", 9, color="#666")
    return b


def square(x0, y, bits, w=34, h=22, color=BLUE, name=""):
    d, yy = "", None
    for i, bt in enumerate(bits):
        ny = y - h if bt else y
        d += (f"M{x0} {ny}" if yy is None else (f" L{x0 + i * w} {ny}" if ny != yy else "")) + f" L{x0 + (i + 1) * w} {ny}"
        yy = ny
    b = f'<path d="{d}" fill="none" stroke="{color}" stroke-width="2"/>' + text(x0 - 8, y - h / 2, name, 10.5, anchor="end", weight="bold")
    return b


# ------------------------------------------------------------------ 1. positive and negative logic
def pos_neg():
    b = title("Positive and Negative Logic")
    bits = [1, 0, 1, 1, 0, 0, 1]
    x0, w = 100, 34
    b += line(f"M{x0} 96 L{x0 + w * 7} 96", "#bbb", 1) + line(f"M{x0} 54 L{x0 + w * 7} 54", "#bbb", 1, "3 3")
    b += square(x0, 96, bits, w, 42, ORANGE, "")
    b += text(x0 - 6, 58, "+5 V", 9.4, anchor="end", color="#555") + text(x0 - 6, 99, "0 V", 9.4, anchor="end", color="#555")
    b += text(14, 122, "Positive", 9.6, anchor="start", weight="bold", color=GREEN)
    b += text(14, 144, "Negative", 9.6, anchor="start", weight="bold", color=RED)
    for i, bt in enumerate(bits):
        cx = x0 + 36 + i * w - 18 + 18
        b += text(x0 + i * w + w / 2 + 40, 122, str(bt), 11, mono=True, weight="bold", color=GREEN) if False else ""
    xs = [x0 + i * w + w / 2 for i in range(7)]
    for x, bt in zip(xs, bits):
        b += box(x - 11, 110, 22, 18, GREENF, GREEN, 3, 1) + text(x, 119, str(bt), 10.5, mono=True, weight="bold", color=GREEN)
        b += box(x - 11, 134, 22, 18, REDF, RED, 3, 1) + text(x, 143, str(1 - bt), 10.5, mono=True, weight="bold", color=RED)
    b += box(14, 166, 160, 64, GREENF, GREEN, 8, 1.1) + text(94, 182, "Positive logic", 10, weight="bold", color=GREEN)
    b += text(94, 200, "HIGH (+5 V) = 1", 9.8, mono=True) + text(94, 217, "LOW  (0 V)  = 0".replace(" ", "\u00a0"), 9.8, mono=True)
    b += box(186, 166, 160, 64, REDF, RED, 8, 1.1) + text(266, 182, "Negative logic", 10, weight="bold", color=RED)
    b += text(266, 200, "HIGH (+5 V) = 0", 9.8, mono=True) + text(266, 217, "LOW  (0 V)  = 1".replace(" ", "\u00a0"), 9.8, mono=True)
    b += note(12, 240, 336, ["The same voltage waveform gives opposite bits.", "A positive-logic AND gate acts as a",
                             "negative-logic OR gate (and OR ↔ AND)."], size=9.6)
    return svg(360, 302, b)


# ------------------------------------------------------------------ gate cards
def gate_card(kind, ttl, expr, rule, f, extra=None, extra_h=0, n=2):
    b = title(ttl)
    g, _ = simple_gate(kind, 60, 82, n, names="AB" if n == 2 else "A", lead=26, tail=24)
    b += g
    rows = truth(f, n)
    head = ["A", "B", "Y"] if n == 2 else ["A", "Y"]
    b += tt_svg(220 if n == 2 else 240, 36, head, rows, 36, 20)
    b += box(12, 138, 336, 46, "#FCFAFF", "#D9C8F0", 8, 1)
    b += bexpr(180, 158, expr, 14, color=P) + text(180, 176, rule, 9.6, color="#444")
    y = 196
    if extra:
        b += extra(y)
    return svg(360, y + extra_h, b)


def and_card():
    def ex(y):
        return text(14, y + 6, "Switch analogy: switches in SERIES", 9.6, anchor="start", weight="bold", color=BLUE) + series_circuit(y + 34)
    return gate_card("AND", "AND Gate", "Y = A·B", "Output is 1 only when ALL inputs are 1", OPS["AND"], ex, 98)


def or_card():
    def ex(y):
        return text(14, y + 6, "Switch analogy: switches in PARALLEL", 9.6, anchor="start", weight="bold", color=BLUE) + parallel_circuit(y + 34)
    return gate_card("OR", "OR Gate", "Y = A + B", "Output is 1 when ANY input is 1", OPS["OR"], ex, 112)


def not_card():
    def ex(y):
        a = [0, 1, 1, 0, 1, 0, 0, 1]
        b = text(14, y + 6, "Waveforms (output is inverted)", 9.6, anchor="start", weight="bold", color=BLUE)
        b += square(60, y + 44, a, 34, 22, BLUE, "A") + square(60, y + 84, [1 - v for v in a], 34, 22, GREEN, "Y")
        return b
    return gate_card("NOT", "NOT Gate (Inverter)", "Y = !A", "Output is the complement of the input", OPS["NOT"], ex, 96, n=1)


def equiv_row(y, k1, k2, res, lbl):
    """AND/OR followed by NOT  =  NAND/NOR"""
    b = text(14, y + 6, lbl, 9.6, anchor="start", weight="bold", color=BLUE)
    g1, (ox, oy), ins = gate(k1, 40, y + 40)
    g2, (o2, _), _ = gate("NOT", ox + 16, oy, s=0.8)
    b += g1 + g2 + wire([(ox, oy), (ox + 16, oy)]) + wire([(o2, oy), (o2 + 12, oy)])
    for (ix, iy) in ins:
        b += wire([(26, iy), (ix, iy)])
    b += text(o2 + 26, y + 44, "=", 16, weight="bold")
    g3, (o3, _), ins3 = gate(res, o2 + 46, y + 40)
    b += g3 + wire([(o3, y + 40), (o3 + 16, y + 40)])
    for (ix, iy) in ins3:
        b += wire([(o2 + 34, iy), (ix, iy)])
    return b


def nand_card():
    return gate_card("NAND", "NAND Gate (NOT-AND)", "Y = !(A·B)", "Output is 0 only when ALL inputs are 1",
                     OPS["NAND"], lambda y: equiv_row(y, "AND", "NOT", "NAND", "NAND = AND followed by NOT"), 78)


def nor_card():
    return gate_card("NOR", "NOR Gate (NOT-OR)", "Y = !(A+B)", "Output is 1 only when ALL inputs are 0",
                     OPS["NOR"], lambda y: equiv_row(y, "OR", "NOT", "NOR", "NOR = OR followed by NOT"), 78)


def xor_card():
    def ex(y):
        b = text(14, y + 6, "Implementation with basic gates", 9.6, anchor="start", weight="bold", color=BLUE)
        top, bot = y + 22, y + 152
        XA, XB, XNA, XNB = 34, 50, 108, 124
        b += lab(XA + 4, top - 2, "A", "middle") + lab(XB + 4, top - 2, "B", "middle")
        b += wire([(XA, top + 4), (XA, bot)]) + wire([(XB, top + 4), (XB, bot)])
        n1, (n1x, _), _ = gate("NOT", 66, top + 18, s=0.7)
        n2, (n2x, _), _ = gate("NOT", 66, top + 48, s=0.7)
        b += n1 + n2 + dot(XA, top + 18) + wire([(XA, top + 18), (66, top + 18)]) + dot(XB, top + 48) + wire([(XB, top + 48), (66, top + 48)])
        b += wire([(n1x, top + 18), (XNA, top + 18), (XNA, bot)]) + wire([(n2x, top + 48), (XNB, top + 48), (XNB, bot)])
        b += bexpr(XNA, bot + 12, "!A", 9.5, color="#666") + bexpr(XNB + 4, bot + 12, "!B", 9.5, color="#666")
        a1, (a1x, a1y), ai1 = gate("AND", 172, top + 74)
        a2, (a2x, a2y), ai2 = gate("AND", 172, top + 118)
        o, (ox, oy), oi = gate("OR", 254, top + 96)
        b += a1 + a2 + o
        for (ix, iy), bx in [(ai1[0], XA), (ai1[1], XNB), (ai2[0], XNA), (ai2[1], XB)]:
            b += dot(bx, iy) + wire([(bx, iy), (ix, iy)])
        b += wire([(a1x, a1y), (236, a1y), (236, oi[0][1]), oi[0]]) + wire([(a2x, a2y), (236, a2y), (236, oi[1][1]), oi[1]])
        b += wire([(ox, oy), (ox + 16, oy)]) + lab(ox + 20, oy + 4, "Y", "start")
        b += bexpr(222, a1y - 8, "A!B", 9.5, color=GREEN) + bexpr(222, a2y + 18, "!AB", 9.5, color=GREEN)
        return b
    return gate_card("XOR", "EX-OR Gate (Exclusive-OR)", "Y = A⊕B = A!B + !AB", "Output is 1 when the inputs are DIFFERENT",
                     OPS["XOR"], ex, 172)


def xnor_card():
    def ex(y):
        b = equiv_row(y, "XOR", "NOT", "XNOR", "EX-NOR = EX-OR followed by NOT")
        b += note(12, y + 74, 336, ["Also called the equality / coincidence gate:", "Y = 1 when A = B. Used in comparators."], size=9.6)
        return b
    return gate_card("XNOR", "EX-NOR Gate (Exclusive-NOR)", "Y = !(A⊕B) = AB + !A!B", "Output is 1 when the inputs are EQUAL",
                     OPS["XNOR"], ex, 120)


# ------------------------------------------------------------------ universal gates
def tied_nand(x, y, kind="NAND", s=1.0):
    """NAND / NOR with both inputs tied = inverter; returns svg, out point, input point"""
    g, (ox, oy), ins = gate(kind, x, y, s=s)
    jx = x - 10
    b = g + wire([(jx, ins[0][1]), (ins[0][0], ins[0][1])]) + wire([(jx, ins[1][1]), (ins[1][0], ins[1][1])])
    b += wire([(jx, ins[0][1]), (jx, ins[1][1])]) + dot(jx, y)
    return b, (ox, oy), (jx, y)


def universal(kind):
    K = kind
    inv = "!A"
    b = title(f"{K} as a Universal Gate")
    # NOT
    b += text(14, 44, "NOT", 10, anchor="start", weight="bold", color=BLUE)
    t, (ox, oy), (jx, jy) = tied_nand(110, 66, K)
    b += t + wire([(60, 66), (jx, 66)]) + lab(56, 70, "A") + wire([(ox, oy), (ox + 20, oy)]) + bexpr(ox + 40, oy + 4, "Y=!A", 11, color=GREEN)
    # AND / OR (direct gate + inverter)
    first = "AND" if K == "NAND" else "OR"
    b += text(14, 108, first, 10, anchor="start", weight="bold", color=BLUE)
    g, (gx, gy), ins = gate(K, 80, 136)
    b += g + wire([(60, ins[0][1]), (ins[0][0], ins[0][1])]) + wire([(60, ins[1][1]), (ins[1][0], ins[1][1])])
    b += lab(56, ins[0][1] + 4, "A") + lab(56, ins[1][1] + 4, "B")
    t, (ox, oy), (jx, jy) = tied_nand(gx + 34, 136, K)
    b += t + wire([(gx, gy), (jx, jy)]) + wire([(ox, oy), (ox + 14, oy)])
    b += bexpr(ox + 44, oy + 4, "Y=AB" if K == "NAND" else "Y=A+B", 11, color=GREEN)
    b += bexpr((gx + jx) / 2 + 2, gy - 8, "!(AB)" if K == "NAND" else "!(A+B)", 9, color="#666")
    # OR / AND (invert both inputs, then the gate)
    second = "OR" if K == "NAND" else "AND"
    b += text(14, 184, second, 10, anchor="start", weight="bold", color=BLUE)
    t1, (o1x, o1y), (j1x, _) = tied_nand(90, 212, K)
    t2, (o2x, o2y), (j2x, _) = tied_nand(90, 272, K)
    g, (gx, gy), ins = gate(K, 200, 242)
    b += t1 + t2 + g + wire([(60, 212), (j1x, 212)]) + wire([(60, 272), (j2x, 272)]) + lab(56, 216, "A") + lab(56, 276, "B")
    b += wire([(o1x, o1y), (170, o1y), (170, ins[0][1]), (ins[0][0], ins[0][1])])
    b += wire([(o2x, o2y), (170, o2y), (170, ins[1][1]), (ins[1][0], ins[1][1])])
    b += bexpr(152, 204, "!A", 9.5, color="#666") + bexpr(152, 264, "!B", 9.5, color="#666")
    b += wire([(gx, gy), (gx + 14, gy)]) + bexpr(gx + 44, gy + 4, "Y=A+B" if K == "NAND" else "Y=AB", 11, color=GREEN)
    count = "NOT: 1   AND: 2   OR: 3" if K == "NAND" else "NOT: 1   OR: 2   AND: 3"
    b += note(12, 296, 336, [f"Gates needed ({K}):  {count}", f"Any logic circuit can be built using only {K} gates."], size=9.6)
    return svg(360, 342, b)


def nand_universal():
    return universal("NAND")


def nor_universal():
    return universal("NOR")


# ------------------------------------------------------------------ IC 7400 pin diagram
def ic7400():
    b = title("IC 7400: Quad 2-input NAND Gate")
    X0, X1, YT, YB = 66, 294, 80, 170
    b += box(X0, YT, X1 - X0, YB - YT, "#2B2B2B", "#111", 6, 1.2)
    b += f'<path d="M{X0} 113 A12 12 0 0 1 {X0} 137" fill="#555" stroke="#111"/>'
    top = ["VCC", "4B", "4A", "4Y", "3B", "3A", "3Y"]
    bot = ["1A", "1B", "1Y", "2A", "2B", "2Y", "GND"]
    for i in range(7):
        x = 84 + i * 32
        b += box(x - 5, YT - 14, 10, 14, "#BDBDBD", "#777", 1, 1) + box(x - 5, YB, 10, 14, "#BDBDBD", "#777", 1, 1)
        b += text(x, YT - 22, str(14 - i), 9, color="#555") + text(x, YT - 36, top[i], 9.4, weight="bold", color=BLUE)
        b += text(x, YB + 24, str(i + 1), 9, color="#555") + text(x, YB + 38, bot[i], 9.4, weight="bold", color=BLUE)
    W = "#F2E9FF"
    for gx, pa, pb, py in [(128, 148, 116, 180), (224, 244, 212, 276)]:     # top gates (4 and 3)
        g, (ox, oy), ins = gate("NAND", gx, 112, s=0.5)
        b += g + wire([(pb, YT), (pb, ins[1][1]), (gx, ins[1][1])], W, 1.3)
        b += wire([(pa, YT), (pa, 96), (gx - 6, 96), (gx - 6, ins[0][1]), (gx, ins[0][1])], W, 1.3)
        b += wire([(ox, oy), (py, oy), (py, YT)], W, 1.3)
    for gx, pa, pb, py in [(96, 84, 116, 148), (192, 180, 212, 244)]:      # bottom gates (1 and 2)
        g, (ox, oy), ins = gate("NAND", gx, 148, s=0.5)
        b += g + wire([(pa, YB), (pa, ins[0][1]), (gx, ins[0][1])], W, 1.3)
        b += wire([(pb, YB), (pb, 164), (gx - 6, 164), (gx - 6, ins[1][1]), (gx, ins[1][1])], W, 1.3)
        b += wire([(ox, oy), (py, oy), (py, YB)], W, 1.3)
    b += wire([(84, YT), (84, 90)], "#FFCDD2", 1.3) + wire([(276, YB), (276, 160)], "#B0BEC5", 1.3)
    rows = [("7408", "AND (quad 2-input)"), ("7432", "OR (quad 2-input)"), ("7404", "NOT (hex inverter)"), ("7400", "NAND (quad 2-input)"),
            ("7402", "NOR (quad, other pinout)"), ("7486", "EX-OR (quad 2-input)"), ("74266", "EX-NOR (quad)")]
    y = 226
    b += box(12, y, 336, 18 + 15 * 4, "#FCFAFF", "#D9C8F0", 8, 1)
    for i, (ic, nm) in enumerate(rows):
        cx = 22 + (i % 2) * 168
        yy = y + 16 + (i // 2) * 15
        b += text(cx, yy, ic, 9.6, anchor="start", mono=True, weight="bold", color=P) + text(cx + 44, yy, nm, 9, anchor="start")
    b += text(180, y + 92, "VCC = +5 V (pin 14), GND = pin 7 for 14-pin TTL ICs", 9, color=RED)
    return svg(360, y + 102, b)


# ------------------------------------------------------------------ summary of all gates
def summary():
    b = title("Logic Gates: Summary")
    gates = [("AND", "Y=AB"), ("OR", "Y=A+B"), ("NOT", "Y=!A"), ("NAND", "Y=!(AB)"), ("NOR", "Y=!(A+B)"), ("XOR", "Y=A⊕B"), ("XNOR", "Y=!(A⊕B)")]
    y0 = 32
    hx = [14, 98, 166, 236]
    b += box(12, y0, 336, 22, P, P, 0, 1)
    b += text(52, y0 + 11, "Symbol", 9.6, color="#fff", weight="bold") + text(126, y0 + 11, "Gate", 9.6, color="#fff", weight="bold")
    b += text(196, y0 + 11, "Expression", 9.6, color="#fff", weight="bold")
    for i, ab in enumerate(["00", "01", "10", "11"]):
        b += text(250 + i * 26, y0 + 11, ab, 9.4, color="#fff", weight="bold", mono=True)
    for r, (k, ex) in enumerate(gates):
        y = y0 + 22 + r * 36
        b += box(12, y, 336, 36, "#FAF6FF" if r % 2 else "#fff", "#D9C8F0", 0, 1)
        n = 1 if k == "NOT" else 2
        g, (ox, oy), ins = gate(k, 36, y + 18, n, s=0.6)
        b += g
        for ix, iy in ins:
            b += wire([(24, iy), (ix, iy)], WIRE, 1.2)
        b += wire([(ox, oy), (ox + 8, oy)], WIRE, 1.2)
        b += text(126, y + 18, "EX-NOR" if k == "XNOR" else ("EX-OR" if k == "XOR" else k), 10, weight="bold", color=P)
        b += bexpr(198, y + 22, ex, 10.5)
        for i in range(4):
            a_, b_ = i >> 1, i & 1
            v = OPS[k](a_) if k == "NOT" else OPS[k](a_, b_)
            if k == "NOT":
                v = "" if i in (1, 3) else v
                v = {0: 1, 2: 0}.get(i, "")
                if i == 0:
                    b += text(276, y + 18, "A=0→1, A=1→0", 8.6, color="#444")
                continue
            b += text(250 + i * 26, y + 18, str(v), 11, mono=True, weight="bold", color=HI if v else "#999")
    yb = y0 + 22 + 7 * 36 + 10
    b += text(180, yb + 4, "Universal gates: NAND, NOR  |  Basic gates: AND, OR, NOT", 9.2, color=RED, weight="bold")
    return svg(360, yb + 14, b)


# ------------------------------------------------------------------ De Morgan
def bubbled(kind, x, y):
    g, (ox, oy), ins = gate(kind, x, y)
    b = g
    pts = []
    for ix, iy in ins:
        b += _bubble(ix - 4.5, iy)
        pts.append((ix - 9, iy))
    return b, (ox, oy), pts


def demorgan():
    b = title("De Morgan's Theorems")
    for r, (k1, k2, e1, e2, t) in enumerate([("NAND", "OR", "!(A·B)", "!A + !B", "Theorem 1: NAND = bubbled OR"),
                                            ("NOR", "AND", "!(A+B)", "!A · !B", "Theorem 2: NOR = bubbled AND")]):
        y = 70 + r * 94
        b += text(14, y - 26, t, 10, anchor="start", weight="bold", color=BLUE)
        g, (ox, oy), ins = gate(k1, 50, y)
        b += g + wire([(ox, oy), (ox + 12, oy)])
        for ix, iy in ins:
            b += wire([(30, iy), (ix, iy)])
        b += lab(26, ins[0][1] + 4, "A", size=9.6) + lab(26, ins[1][1] + 4, "B", size=9.6)
        b += text(146, y + 5, "=", 16, weight="bold")
        g, (ox2, oy2), pts = bubbled(k2, 196, y)
        b += g + wire([(ox2, oy2), (ox2 + 12, oy2)])
        for px, py in pts:
            b += wire([(172, py), (px, py)])
        b += lab(168, pts[0][1] + 4, "A", size=9.6) + lab(168, pts[1][1] + 4, "B", size=9.6)
        b += bexpr(180, y + 40, f"{e1} = {e2}", 13, color=P)
    # proof table for theorem 1
    rows = [(a, c, a & c, 1 - (a & c), 1 - a, 1 - c, (1 - a) | (1 - c)) for a in (0, 1) for c in (0, 1)]
    assert all(r[3] == r[6] for r in rows)
    y = 236
    b += text(14, y - 6, "Proof of theorem 1 by truth table", 9.6, anchor="start", weight="bold", color=BLUE)
    heads = ["A", "B", "AB", "!(AB)", "!A", "!B", "!A+!B"]
    cw = 47
    for i, h in enumerate(heads):
        isout = i in (3, 6)
        b += box(16 + i * cw, y, cw, 22, HI if isout else P, P, 0, 1) + bexpr(16 + i * cw + cw / 2, y + 15, h, 10, color="#fff")
    for r, row in enumerate(rows):
        yy = y + 22 + r * 19
        for i, v in enumerate(row):
            isout = i in (3, 6)
            b += box(16 + i * cw, yy, cw, 19, "#E3F5E6" if isout and v else "#fff", "#C9B3EC", 0, 1)
            b += text(16 + i * cw + cw / 2, yy + 9.5, str(v), 10.5, mono=True, weight="bold" if isout else "normal")
    b += text(180, y + 22 + 4 * 19 + 16, "Columns 4 and 7 are identical, so the theorem is proved.", 9.2, color=GREEN, weight="bold")
    return svg(360, y + 22 + 4 * 19 + 28, b)


# ------------------------------------------------------------------ implementing a Boolean function
def func_impl():
    b = title("Logic Diagram of Y = AB + !AC".replace("!AC", "A'C"))
    b = title("Implementing a Boolean Function")
    b += bexpr(180, 44, "Y = A·B + !A·C", 13, color=P)
    a1, (a1x, a1y), i1 = gate("AND", 170, 84)
    a2, (a2x, a2y), i2 = gate("AND", 170, 168)
    o, (ox, oy), io = gate("OR", 262, 126)
    n, (nx, ny), _ = gate("NOT", 100, 158, s=0.8)
    b += a1 + a2 + o + n
    b += lab(26, i1[0][1] + 4, "A") + wire([(30, i1[0][1]), i1[0]]) + dot(70, i1[0][1]) + wire([(70, i1[0][1]), (70, 158), (100, 158)])
    b += lab(26, i1[1][1] + 4, "B") + wire([(30, i1[1][1]), i1[1]])
    b += lab(26, i2[1][1] + 4, "C") + wire([(30, i2[1][1]), i2[1]])
    b += wire([(nx, ny), i2[0]]) + bexpr(150, ny - 6, "!A", 9.6, color="#666")
    b += wire([(a1x, a1y), (240, a1y), (240, io[0][1]), io[0]]) + wire([(a2x, a2y), (240, a2y), (240, io[1][1]), io[1]])
    b += bexpr(226, a1y - 6, "AB", 9.6, color=GREEN) + bexpr(222, a2y + 16, "!AC", 9.6, color=GREEN)
    b += wire([(ox, oy), (ox + 14, oy)]) + lab(ox + 18, oy + 4, "Y", "start")
    f = lambda a, c_, d: (a & c_) | ((1 - a) & d)
    rows = truth(f, 3)
    b += tt_svg(24, 204, ["A", "B", "C", "Y"], rows, 30, 17)
    m = minterms(f, 3)
    assert m == [1, 3, 6, 7]
    b += note(160, 214, 188, ["Y = 1 for rows", f"{', '.join(map(str, m))} (minterms)", "", "Gates used:", "1 NOT, 2 AND, 1 OR"], size=9.6)
    return svg(360, 204 + 9 * 17 + 10, b)


# ------------------------------------------------------------------ SOP and POS structures
def sop_pos():
    b = title("SOP (AND-OR) and POS (OR-AND) Circuits")
    for r, (k1, k2, e, nm) in enumerate([("AND", "OR", "Y = AB + CD", "SOP: Sum of Products"), ("OR", "AND", "Y = (A+B)(C+D)", "POS: Product of Sums")]):
        y0 = 40 + r * 140
        b += text(14, y0, nm, 10, anchor="start", weight="bold", color=BLUE) + bexpr(250, y0, e, 11.5, color=P)
        g1, (o1x, o1y), i1 = gate(k1, 90, y0 + 34)
        g2, (o2x, o2y), i2 = gate(k1, 90, y0 + 94)
        g3, (o3x, o3y), i3 = gate(k2, 200, y0 + 64)
        b += g1 + g2 + g3
        for (ix, iy), nmx in zip(i1 + i2, "ABCD"):
            b += wire([(46, iy), (ix, iy)]) + lab(42, iy + 4, nmx)
        b += wire([(o1x, o1y), (170, o1y), (170, i3[0][1]), i3[0]]) + wire([(o2x, o2y), (170, o2y), (170, i3[1][1]), i3[1]])
        b += wire([(o3x, o3y), (o3x + 16, o3y)]) + lab(o3x + 20, o3y + 4, "Y", "start")
        b += text(110, y0 + 122, f"Level 1: {k1}", 9, color="#666") + text(225, y0 + 122, f"Level 2: {k2}", 9, color="#666")
    b += note(12, 318, 336, ["Minterm: product (AND) term containing every variable", "Maxterm: sum (OR) term containing every variable",
                             "Both are two-level circuits."], size=9.4)
    return svg(360, 374, b)


DIAGRAMS = {"de2_pos_neg": pos_neg, "de2_and": and_card, "de2_or": or_card, "de2_not": not_card, "de2_nand": nand_card,
            "de2_nor": nor_card, "de2_xor": xor_card, "de2_xnor": xnor_card, "de2_nand_universal": nand_universal,
            "de2_nor_universal": nor_universal, "de2_ic7400": ic7400, "de2_summary": summary, "de2_demorgan": demorgan,
            "de2_func_impl": func_impl, "de2_sop_pos": sop_pos}

if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    for k, f in DIAGRAMS.items():
        with open(os.path.join(OUT, k + ".svg"), "w", encoding="utf-8") as fh:
            fh.write(f())
    print("written", len(DIAGRAMS))
