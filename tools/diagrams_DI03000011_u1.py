"""DI03000011 Digital Electronics - Unit 1 diagrams: digital systems, number systems, conversions, binary arithmetic."""
import os, math
from flowchart_lib import *
from diagrams_DI03000021_u1 import box, BLUE, BLUEF, GREEN, GREENF, ORANGE, ORANGEF, RED, REDF, YEL
import de_num as D

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "content", "computer", "sem3", "DI03000011", "diagrams")


def note(x, y, w, lines, fill=BLUEF, stroke=BLUE, size=9.6, lh=15, mono=False):
    b = box(x, y, w, 10 + lh * len(lines), fill, stroke, 7, 1.1)
    for i, s in enumerate(lines):
        c = INK
        if isinstance(s, tuple):
            s, c = s
        b += text(x + 8, y + 15 + i * lh, s.replace(" ", "\u00a0") if mono else s, size, anchor="start", mono=mono, color=c)
    return b


def cellrow(x, y, vals, w=30, h=26, fills=None, size=11.5, stroke=P):
    fills = fills or {}
    b = ""
    for i, v in enumerate(vals):
        b += box(x + i * w, y, w, h, fills.get(i, "#fff"), stroke, 0, 1.3)
        b += text(x + i * w + w / 2, y + h / 2, str(v), size, mono=True, weight="bold")
    return b


# ------------------------------------------------------------------ 1. analog vs digital
def analog_digital():
    b = title("Analog and Digital Signals")
    b += text(14, 44, "Analog signal", 10.6, anchor="start", weight="bold", color=BLUE)
    b += line("M20 110 L340 110", "#999", 1) + line("M20 54 L20 120", "#999", 1)
    pts = " ".join(f"L{20 + t:.1f} {84 - 26 * math.sin(t / 320 * 4 * math.pi):.1f}" for t in range(0, 321, 4))
    b += f'<path d="M20 84 {pts[1:]}" fill="none" stroke="{BLUE}" stroke-width="2"/>'
    b += text(336, 124, "time", 8.8, anchor="end", color="#888")
    b += text(14, 152, "Digital signal", 10.6, anchor="start", weight="bold", color=GREEN)
    bits = [1, 0, 1, 1, 0, 0, 1, 0]
    d, x = "", 20
    hi, lo = 170, 214
    y = hi if bits[0] else lo
    d = f"M20 {y}"
    for i, bt in enumerate(bits):
        ny = hi if bt else lo
        if ny != y:
            d += f" L{x} {ny}"
            y = ny
        x += 40
        d += f" L{x} {y}"
        b += text(x - 20, 230, str(bt), 10, mono=True, weight="bold", color=GREEN)
    b += line("M20 214 L340 214", "#999", 1) + f'<path d="{d}" fill="none" stroke="{GREEN}" stroke-width="2"/>'
    b += text(14, 172, "1", 9, anchor="start", color="#888") + text(14, 214, "0", 9, anchor="start", color="#888")
    b += note(12, 244, 336, [("Analog: continuous, infinite values", BLUE), ("Digital: discrete, only two levels 0 and 1", GREEN),
                             "Digital: less noise, easy storage, accurate"], size=9.6)
    return svg(360, 306, b)


# ------------------------------------------------------------------ 2. digital system block
def digital_system():
    b = title("Digital System")
    b += rbox(60, 80, 96, 46, "Input", F_IO, S_IO, 11, "bold")
    b += rbox(180, 80, 104, 58, "Digital", F_PROC, S_PROC, 11, "bold") + text(180, 98, "processing", 9.6, color=P)
    b += rbox(300, 80, 96, 46, "Output", F_TERM, S_TERM, 11, "bold")
    b += arr([(108, 80), (127, 80)], INK) + arr([(233, 80), (251, 80)], INK)
    b += text(60, 120, "keyboard, switch,", 8.8, color="#555") + text(60, 132, "sensor + ADC", 8.8, color="#555")
    b += text(180, 124, "gates, flip-flops,", 8.8, color="#555") + text(180, 136, "processor, memory", 8.8, color="#555")
    b += text(300, 120, "display, LED,", 8.8, color="#555") + text(300, 132, "printer, DAC", 8.8, color="#555")
    b += note(12, 152, 336, ["A digital system processes information in", "binary form (0 and 1) using electronic circuits.",
                             ("Examples: computer, calculator, mobile phone,", P), ("digital watch, digital camera, ATM.", P)], size=9.8)
    return svg(360, 228, b)


# ------------------------------------------------------------------ 3. number systems table
def number_systems():
    b = title("Number Systems")
    head = ["System", "Base", "Digits", "Example"]
    rows = [("Binary", "2", "0, 1", "(1011)₂"), ("Octal", "8", "0 to 7", "(257)₈"), ("Decimal", "10", "0 to 9", "(349)₁₀"),
            ("Hexadecimal", "16", "0-9, A-F", "(2AF)₁₆")]
    xs, ws = [12, 116, 166, 256], [104, 50, 90, 92]
    y = 34
    for i, h in enumerate(head):
        b += box(xs[i], y, ws[i], 26, P, P, 0, 1) + text(xs[i] + ws[i] / 2, y + 13, h, 10.4, color="#fff", weight="bold")
    cols = [BLUEF, GREENF, ORANGEF, "#F1E8FC"]
    for r, row in enumerate(rows):
        y = 60 + r * 28
        for i, v in enumerate(row):
            b += box(xs[i], y, ws[i], 28, cols[r], P, 0, 1) + text(xs[i] + ws[i] / 2, y + 14, v, 10.4, weight="bold" if i == 0 else "normal", mono=i > 0)
    b += text(180, 190, "Hex letters:  A=10  B=11  C=12  D=13  E=14  F=15", 10, mono=True, color=RED, weight="bold")
    b += note(12, 202, 336, ["Base (radix) = number of different digits used.", "Largest digit = base − 1.",
                             "Value = Σ digit × base^position"], size=9.8)
    return svg(360, 264, b)


# ------------------------------------------------------------------ 4. positional weights
def positional():
    b = title("Positional Weights: (1101.101)₂")
    bits = "1101.101"
    pw = [3, 2, 1, 0, None, -1, -2, -3]
    x0 = 30
    for i, (c, p) in enumerate(zip(bits, pw)):
        x = x0 + i * 38
        if p is None:
            b += text(x + 17, 76, ".", 20, weight="bold", color=RED)
            continue
        b += box(x, 56, 34, 34, GREENF if p >= 0 else ORANGEF, P, 4, 1.3) + text(x + 17, 73, c, 14, mono=True, weight="bold")
        b += text(x + 17, 106, f"2^{p}", 9.6, mono=True, color=BLUE)
        b += text(x + 17, 122, D.fmt(D.Fraction(2) ** p), 9.6, mono=True, color="#555")
    b += text(14, 106, "wt", 9, anchor="start", color=BLUE) if False else ""
    tot, expr, _ = D.to_decimal(bits, 2)
    b += text(180, 46, "MSB ← integer part | fraction part → LSB", 9.4, color="#666")
    b += note(12, 138, 336, ["= 1×8 + 1×4 + 0×2 + 1×1 + 1×0.5 + 0×0.25 + 1×0.125", "= 8 + 4 + 1 + 0.5 + 0.125",
                             (f"= ({D.fmt(tot)})₁₀", GREEN)], size=9.6)
    b += text(180, 212, "Integer weights 1, 2, 4, 8 ...   Fraction weights 0.5, 0.25 ...", 9.2, color="#444")
    return svg(360, 226, b)


# ------------------------------------------------------------------ 5. repeated division
def division():
    b = title("Decimal to Binary: Repeated Division")
    res, _ = D.int_to_base(45, 2)
    q, rows = 45, []
    while q:
        rows.append((q, q // 2, q % 2)); q //= 2
    y0 = 42
    for i, (n, qq, r) in enumerate(rows):
        y = y0 + i * 28
        b += text(40, y + 14, "2", 12, mono=True, color=P, weight="bold")
        b += line(f"M52 {y + 2} L52 {y + 26} L130 {y + 26}", P, 1.4)
        b += text(90, y + 14, str(n), 12, mono=True, weight="bold")
        b += text(160, y + 14, f"remainder {r}", 10, anchor="start", color=RED, weight="bold")
    b += text(90, y0 + len(rows) * 28 + 14, "0", 12, mono=True, weight="bold")
    b += arr([(278, y0 + len(rows) * 28 - 6), (278, y0 + 8)], GREEN, None) + text(290, y0 + 80, "read", 9.6, anchor="start", color=GREEN, weight="bold")
    b += text(290, y0 + 94, "upward", 9.6, anchor="start", color=GREEN, weight="bold")
    yb = y0 + len(rows) * 28 + 30
    b += note(12, yb, 336, [(f"(45)₁₀ = ({res})₂", GREEN), "Divide by the base until the quotient is 0.",
                            "First remainder = LSB, last remainder = MSB.", "Same method: ÷8 for octal, ÷16 for hex."], size=9.8)
    return svg(360, yb + 76, b)


# ------------------------------------------------------------------ 6. fraction multiplication
def fraction():
    b = title("Decimal Fraction to Binary: Multiply by 2")
    f = D.Fraction(5, 8)
    y = 46
    digs = ""
    while f:
        p = f * 2
        d = int(p)
        b += text(40, y + 13, f"{float(f):g} × 2", 12, anchor="start", mono=True, weight="bold")
        b += text(170, y + 13, f"= {float(p):g}", 12, anchor="start", mono=True)
        b += box(262, y, 34, 26, YEL, ORANGE, 4, 1.2) + text(279, y + 13, str(d), 12, mono=True, weight="bold")
        digs += str(d)
        f = p - d
        y += 34
    b += text(279, 36, "integer", 9, color=ORANGE, weight="bold")
    b += arr([(318, 50), (318, y - 10)], GREEN) + text(326, (50 + y) / 2, "read", 9.4, anchor="start", color=GREEN, weight="bold")
    b += text(326, (50 + y) / 2 + 13, "down", 9.4, anchor="start", color=GREEN, weight="bold")
    b += note(12, y + 6, 336, [(f"(0.625)₁₀ = (0.{digs})₂", GREEN), "Multiply the fraction by 2; the integer part",
                               "is the next bit. Stop at 0 (or after 4-6 bits).", "0.1 and 0.3 never end: answer is approximate."], size=9.8)
    return svg(360, y + 80, b)


# ------------------------------------------------------------------ 7. grouping
def grouping():
    b = title("Binary ↔ Octal and Hexadecimal")
    bits = "11010110"
    o, gi, _, _ = D.bin_group(bits, 3)
    h, hi, _, _ = D.bin_group(bits, 4)
    b += text(180, 44, f"Binary: {bits}", 11, mono=True, weight="bold")
    b += text(14, 70, "Octal: groups of 3 (from the right)", 10, anchor="start", weight="bold", color=BLUE)
    for i, g in enumerate(gi):
        x = 50 + i * 96
        b += box(x, 80, 74, 28, BLUEF, BLUE, 4, 1.2) + text(x + 37, 94, g, 12, mono=True, weight="bold")
        b += arr([(x + 37, 110), (x + 37, 126)], BLUE) + text(x + 37, 138, str(int(g, 2)), 13, mono=True, weight="bold", color=BLUE)
    b += text(180, 162, f"= ({o})₈   (a 0 is added on the left)", 10, color=BLUE, weight="bold")
    b += text(14, 190, "Hexadecimal: groups of 4", 10, anchor="start", weight="bold", color=GREEN)
    for i, g in enumerate(hi):
        x = 80 + i * 120
        b += box(x, 200, 84, 28, GREENF, GREEN, 4, 1.2) + text(x + 42, 214, g, 12, mono=True, weight="bold")
        b += arr([(x + 42, 230), (x + 42, 246)], GREEN) + text(x + 42, 258, D.DIG[int(g, 2)] + f"  ({int(g, 2)})", 12, mono=True, weight="bold", color=GREEN)
    b += text(180, 282, f"= ({h})₁₆", 10.4, color=GREEN, weight="bold")
    b += note(12, 294, 336, ["Integer part: group from the point to the LEFT.", "Fraction part: group from the point to the RIGHT.",
                             "Reverse: write each digit as 3 or 4 bits."], size=9.6)
    return svg(360, 356, b)


# ------------------------------------------------------------------ 8. conversion map
def conv_map():
    b = title("Conversion Methods: Summary")
    pos = {"Decimal": (180, 60), "Binary": (180, 200), "Octal": (60, 300), "Hex": (300, 300)}
    for k, (x, y) in pos.items():
        b += rbox(x, y, 92, 34, k, GREENF if k == "Binary" else F_PROC, GREEN if k == "Binary" else P, 11, "bold")
    b += arr([(160, 78), (160, 182)], BLUE) + text(154, 120, "÷2 (integer)", 8.8, anchor="end", color=BLUE)
    b += text(154, 132, "×2 (fraction)", 8.8, anchor="end", color=BLUE)
    b += arr([(200, 182), (200, 78)], RED) + text(206, 126, "Σ bit × 2ⁿ", 8.8, anchor="start", color=RED)
    b += arr([(150, 217), (80, 282)], ORANGE) + text(96, 240, "group 3", 8.8, anchor="end", color=ORANGE)
    b += arr([(210, 217), (280, 282)], ORANGE) + text(264, 240, "group 4", 8.8, anchor="start", color=ORANGE)
    b += arr([(106, 300), (253, 300)], "#666") + text(180, 292, "via binary", 8.8, color="#666")
    b += arr([(140, 60), (40, 60), (40, 282)], P) + text(46, 120, "÷8", 9, anchor="start", color=P)
    b += arr([(220, 60), (320, 60), (320, 282)], P) + text(314, 120, "÷16", 9, anchor="end", color=P)
    b += text(180, 340, "Any base → decimal: multiply each digit by its weight and add", 9.2, color="#444")
    return svg(360, 352, b)


# ------------------------------------------------------------------ 9. binary addition
def binary_add():
    b = title("Binary Addition")
    rules = [("0 + 0", "0", ""), ("0 + 1", "1", ""), ("1 + 0", "1", ""), ("1 + 1", "0", "carry 1"), ("1 + 1 + 1", "1", "carry 1")]
    b += box(12, 32, 160, 150, "#FCFAFF", "#D9C8F0", 8, 1) + text(92, 48, "Rules", 10.4, weight="bold", color=P)
    for i, (a, s, c) in enumerate(rules):
        y = 70 + i * 22
        b += text(24, y, a, 11, anchor="start", mono=True) + text(100, y, "= " + s, 11, anchor="start", mono=True, weight="bold")
        if c:
            b += text(124, y + 1, c, 8.8, anchor="start", color=RED)
    res, _ = D.add_work("1011", "1101")
    s, c, cr = D.add_bits("1011", "1101")
    x0 = 214
    carry = ("1" if c else " ") + "".join("1" if x else " " for x in cr[:-1]) + " "
    lines = [(carry, RED, "carry"), (" 1011", INK, "(11)"), (" 1101", INK, "(13)"), (res.rjust(5), GREEN, "(24)")]
    for i, (t, col, lab) in enumerate(lines):
        y = 60 + i * 26 + (8 if i == 3 else 0)
        for k, ch in enumerate(t):
            if ch != " ":
                b += text(x0 + k * 16, y, ch, 13 if i else 10, mono=True, weight="bold", color=col)
        b += text(x0 + 96, y, lab, 9, anchor="start", color="#666" if i else RED)
    b += text(x0 - 12, 112, "+", 13, weight="bold")
    b += line(f"M{x0 - 14} 124 L{x0 + 76} 124", INK, 1.4)
    b += note(12, 196, 336, ["Add column by column from the right (LSB),", "carrying 1 to the next column when the sum ≥ 2.",
                             ("Check: 11 + 13 = 24 = (11000)₂", GREEN)], size=9.8)
    return svg(360, 258, b)


# ------------------------------------------------------------------ 10. complements
def complement():
    b = title("1's and 2's Complement")
    n = "10110"
    c1, c2 = D.ones(n), D.twos(n)
    b += text(60, 54, "Number", 10, anchor="end", weight="bold") + cellrow(80, 40, list(n), 36)
    b += arr([(170, 70), (170, 92)], BLUE) + text(180, 84, "invert every bit (0↔1)", 9.4, anchor="start", color=BLUE)
    b += text(60, 110, "1's comp", 10, anchor="end", weight="bold", color=BLUE) + cellrow(80, 96, list(c1), 36, fills={i: BLUEF for i in range(5)})
    b += arr([(170, 126), (170, 148)], GREEN) + text(180, 140, "add 1 to the LSB", 9.4, anchor="start", color=GREEN)
    b += text(60, 166, "2's comp", 10, anchor="end", weight="bold", color=GREEN) + cellrow(80, 152, list(c2), 36, fills={i: GREENF for i in range(5)})
    b += note(12, 194, 336, ["Shortcut for 2's complement: from the right, keep", "bits up to and including the first 1, then invert",
                             "the rest:  10110 → keep '10', invert '101' → 01010", "r's complement = (r−1)'s complement + 1"], size=9.6)
    return svg(360, 270, b)


# ------------------------------------------------------------------ 11. subtraction flow (2's complement)
def sub_flow():
    b = title("Subtraction using 2's Complement (A − B)")
    b += terminal(180, 50, "Start", 90, 28)
    b += down(180, 64, 82) + process(180, 100, "Make A, B equal length", 200, 32)
    b += down(180, 116, 134) + process(180, 152, "Find 2's complement of B", 200, 32)
    b += down(180, 168, 186) + process(180, 204, "Add: A + 2's comp of B", 200, 32)
    b += down(180, 220, 236) + decision(180, 266, "Carry?", 110, 56)
    b += arr([(235, 266), (300, 266), (300, 304)], INK) + text(268, 258, "Yes", 9.6, weight="bold", color=GREEN)
    b += arr([(125, 266), (60, 266), (60, 304)], INK) + text(92, 258, "No", 9.6, weight="bold", color=RED)
    b += rbox(300, 330, 110, 44, "", F_TERM, S_TERM) + text(300, 322, "Discard carry", 9.6, weight="bold") + text(300, 338, "result +ve", 9.6, color=GREEN, weight="bold")
    b += rbox(60, 330, 110, 44, "", F_CON, S_CON) + text(60, 322, "Result −ve:", 9.6, weight="bold") + text(60, 338, "take 2's comp", 9.6, color=RED, weight="bold")
    b += note(12, 364, 336, ["1's complement method: if carry, add it back to", "the LSB (end-around carry); if no carry, the",
                             "result is negative: take its 1's complement."], ORANGEF, ORANGE, 9.6)
    return svg(360, 424, b)


DIAGRAMS = {"de1_analog_digital": analog_digital, "de1_digital_system": digital_system, "de1_number_systems": number_systems,
            "de1_positional": positional, "de1_division": division, "de1_fraction": fraction, "de1_grouping": grouping,
            "de1_conv_map": conv_map, "de1_binary_add": binary_add, "de1_complement": complement, "de1_sub_flow": sub_flow}

if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    for k, f in DIAGRAMS.items():
        with open(os.path.join(OUT, k + ".svg"), "w", encoding="utf-8") as fh:
            fh.write(f())
    print("written", len(DIAGRAMS))
