"""DI02000101 Scripting Language (Python) - Unit 2 diagrams (operators, control flow)."""
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
    """keep runs of spaces in SVG text"""
    return s.replace("  ", NB + NB)


# ------------------------------------------------------------------ 1. operator types
def operators():
    b = title("Types of Operators in Python")
    rows = [("Arithmetic", "+  -  *  /  //  %  **", BLUE, BLUEF),
            ("Comparison", "==  !=  >  <  >=  <=", GREEN, GREENF),
            ("Logical", "and   or   not", ORANGE, ORANGEF),
            ("Assignment", "=  +=  -=  *=  /=  //=  **=", P, CELL),
            ("Bitwise", "&   |   ^   ~   <<   >>", RED, REDF),
            ("Membership", "in    not in", YELS, YEL),
            ("Identity", "is    is not", PYB, "#E8EEF5")]
    y = 36
    for name, ops, st, f in rows:
        b += box(10, y, 112, 32, f, st, 7) + text(66, y + 16, name, 11, weight="bold", color=st)
        b += box(128, y, 222, 32, "#fff", st, 7) + text(239, y + 16, sp(ops), 11, mono=True, weight="bold", color=INK)
        y += 38
    b += text(180, y + 6, "Python has no ++ / -- operators; use x += 1.", 10, color=RED, weight="bold")
    return svg(360, y + 18, b)


# ------------------------------------------------------------------ 2. bitwise
def bitwise():
    b = title("Bitwise Operators (a = 12, b = 10)")
    w, x0 = 20, 120

    def bits(y, n, label, res, col=INK, fill=CELL, st=P):
        o = text(14, y + 10, label, 10.5, anchor="start", mono=True, weight="bold", color=col)
        for i, ch in enumerate(format(n & 0xFF, "08b")):
            o += box(x0 + i * w, y, w, 20, fill if ch == "1" else "#fff", st, 0, 1.1) + text(x0 + i * w + w / 2, y + 10, ch, 10.5, mono=True, weight="bold", color=col)
        o += text(x0 + 8 * w + 10, y + 10, sp(res), 10.5, anchor="start", mono=True, weight="bold", color=col)
        return o
    y = 38
    b += bits(y, 12, "a", "= 12"); y += 24
    b += bits(y, 10, "b", "= 10"); y += 30
    b += line(f"M10 {y - 4} H350", "#E0D3F2", 1)
    b += bits(y, 12 & 10, "a & b", "= 8   AND", GREEN, GREENF, GREEN); y += 24
    b += bits(y, 12 | 10, "a | b", "= 14  OR", BLUE, BLUEF, BLUE); y += 24
    b += bits(y, 12 ^ 10, "a ^ b", "= 6   XOR", ORANGE, ORANGEF, ORANGE); y += 24
    b += bits(y, 12 << 2, "a << 2", "= 48  ×4", P, CELL, P); y += 24
    b += bits(y, 12 >> 2, "a >> 2", "= 3   ÷4", RED, REDF, RED); y += 30
    notes = ["&  : 1 only if both bits are 1", "|  : 1 if any bit is 1", "^  : 1 if bits are different",
             "~a : -(a+1)  →  ~12 = -13", "<< n : multiply by 2ⁿ     >> n : divide by 2ⁿ"]
    for s in notes:
        b += text(18, y, sp(s), 10, anchor="start", mono=True, color="#333")
        y += 16
    return svg(360, y + 2, b)


# ------------------------------------------------------------------ 3. precedence
def precedence():
    b = title("Operator Precedence (High → Low)")
    rows = [("( )", "Parentheses"), ("**", "Exponent (right to left)"), ("+x  -x  ~x", "Unary plus, minus, NOT"),
            ("*  /  //  %", "Multiplication, division"), ("+  -", "Addition, subtraction"), ("<<  >>", "Bitwise shifts"),
            ("&", "Bitwise AND"), ("^", "Bitwise XOR"), ("|", "Bitwise OR"),
            ("==  !=  >  <  >=  <=\nis  is not  in  not in", "Comparison, identity,\nmembership"),
            ("not", "Logical NOT"), ("and", "Logical AND"), ("or", "Logical OR"), ("=  +=  -=  …", "Assignment (lowest)")]
    y = 32
    for i, (op, d) in enumerate(rows):
        h = 34 if "\n" in op else 20
        shade = int(255 - (len(rows) - i) * 6)
        f = f"#{shade:02x}{min(255, shade + 8):02x}ff" if i < len(rows) else "#fff"
        b += f'<rect x="10" y="{y}" width="340" height="{h}" fill="{"#F3ECFD" if i % 2 == 0 else "#fff"}"/>'
        b += text(22, y + h / 2, str(i + 1), 10, anchor="start", weight="bold", color=P)
        b += text(44, y + h / 2, sp(op), 10.2, anchor="start", mono=True, weight="bold", color=INK)
        b += text(212, y + h / 2, d, 9.8, anchor="start", color="#444")
        y += h
    b += f'<rect x="10" y="32" width="340" height="{y - 32}" fill="none" stroke="#D9C8F0"/>'
    ex = [("2 + 3 * 4", "14"), ("(2 + 3) * 4", "20"), ("2 ** 3 ** 2", "512   (3**2 first)"), ("10 - 4 - 3", "3     (left to right)"),
          ("not 5 > 3 or 2 > 1", "True")]
    y += 18
    b += text(180, y - 2, "Examples", 10.5, weight="bold", color=P)
    for e, r in ex:
        y += 16
        b += text(30, y, e, 10, anchor="start", mono=True, color=BLUE, weight="bold") + text(180, y, sp("→ " + r), 10, anchor="start", mono=True, color=GREEN)
    return svg(360, y + 12, b)


# ------------------------------------------------------------------ 4. identity vs equality
def identity():
    b = title("Identity (is) vs Equality (==)")
    b += text(180, 40, sp("a = [1, 2, 3]   b = a   c = [1, 2, 3]"), 10.8, mono=True, color=P, weight="bold")
    for i, n in enumerate("abc"):
        y = 62 + i * 46 if n != "c" else 160
        y = {"a": 64, "b": 106, "c": 164}[n]
        b += box(30, y, 46, 30, BLUEF, BLUE) + text(53, y + 15, n, 13, mono=True, weight="bold")
    b += box(190, 82, 140, 34, YEL, YELS, 8) + text(260, 99, "[1, 2, 3]", 12, mono=True, weight="bold")
    b += text(260, 128, "object 1", 9.5, color="#777")
    b += box(190, 160, 140, 34, GREENF, GREEN, 8) + text(260, 177, "[1, 2, 3]", 12, mono=True, weight="bold")
    b += text(260, 206, "object 2", 9.5, color="#777")
    b += arr([(76, 79), (188, 95)], BLUE) + arr([(76, 121), (188, 105)], BLUE) + arr([(76, 179), (188, 177)], BLUE)
    rows = [("a == b", "True", "same value"), ("a is b", "True", "same object"), ("a == c", "True", "same value"),
            ("a is c", "False", "different objects"), ("a is not c", "True", "")]
    y = 232
    for e, r, n in rows:
        b += text(30, y, e, 10.8, anchor="start", mono=True, weight="bold", color=PYB)
        b += text(130, y, r, 10.8, anchor="start", mono=True, weight="bold", color=GREEN if r == "True" else RED)
        b += text(190, y, n, 10, anchor="start", color="#444")
        y += 18
    b += text(180, y + 6, "== compares values; is compares identity (id).", 10, color=P, weight="bold")
    b += text(180, y + 22, "Use  x is None  to test for None.", 10, color="#444")
    return svg(360, y + 34, b)


# ------------------------------------------------------------------ 5. if and if-else flowcharts
def fc_ifelse():
    b = title("Flowchart: if and if…else")
    b += text(90, 40, "if", 12, mono=True, weight="bold", color=P) + text(270, 40, "if … else", 12, mono=True, weight="bold", color=P)
    b += line("M180 34 V300", "#E0D3F2", 1)
    # if
    b += down(90, 50, 66)
    b += decision(90, 94, "condition?", 100, 54, 10.5)
    b += arr([(90, 121), (90, 150)], label="True", lpos=(108, 136))
    b += process(90, 168, "if-block", 100, 34, 11)
    b += down(90, 185, 226)
    b += arr([(140, 94), (164, 94), (164, 212), (92, 212)], label="False", lpos=(158, 82))
    b += process(90, 244, "next statement", 120, 34, 10.5)
    # if-else
    b += down(270, 50, 66)
    b += decision(270, 94, "condition?", 100, 54, 10.5)
    b += arr([(220, 94), (222 - 6, 94), (216, 150)], label="True", lpos=(206, 82))
    b += arr([(320, 94), (330, 94), (330, 150)], label="False", lpos=(336, 82))
    b += process(216, 168, "if-block", 64, 34, 10.5)
    b += process(330, 168, "else-\nblock", 50, 34, 10)
    b += line("M216 185 V208 H330 V185")
    b += down(270, 208, 226)
    b += process(270, 244, "next statement", 120, 34, 10.5)
    for j, ln in enumerate(["if marks >= 35:", "    print('Pass')"]):
        b += text(26, 284 + j * 14, ln.replace(" ", NB), 9.8, anchor="start", mono=True, color="#333")
    for j, ln in enumerate(["if n % 2 == 0:", "    print('Even')", "else:", "    print('Odd')"]):
        b += text(206, 278 + j * 13, ln.replace(" ", NB), 9.6, anchor="start", mono=True, color="#333")
    return svg(360, 328, b)


# ------------------------------------------------------------------ 6. elif ladder
def fc_elif():
    b = title("Flowchart: if…elif…else Ladder (Grade)")
    b += terminal(90, 44, "Start", 80, 26, 11)
    b += down(90, 57, 70)
    b += io(90, 86, "read per", 104, 30, 10.5)
    conds = [("per>=75", "Distinction"), ("per>=60", "First Class"), ("per>=50", "Second Class"), ("per>=35", "Pass Class")]
    y = 101
    ys = []
    for i, (c, r) in enumerate(conds):
        b += down(90, y, y + 12)
        cy = y + 12 + 22
        b += decision(90, cy, c, 104, 44, 10, mono=True)
        b += arr([(142, cy), (206, cy)], label="True", lpos=(172, cy - 9))
        b += process(270, cy, r, 120, 28, 10.5)
        b += line(f"M330 {cy} H346")
        ys.append(cy)
        y = cy + 22
        b += text(100, y + 7, "False", 9.5, anchor="start", color=RED, weight="bold")
    b += down(90, y, y + 16)
    b += process(90, y + 30, "Fail", 104, 28, 10.5)
    yj = y + 64
    b += line(f"M346 {ys[0]} V{yj} H92") + arrowhead(92, yj, 180)
    b += line(f"M90 {y + 44} V{yj - 8}") + arrowhead(90, yj - 2, 90)
    b += down(90, yj, yj + 16)
    b += terminal(90, yj + 30, "Stop", 80, 26, 11)
    b += text(270, yj + 30, "Only ONE block executes.", 10, color=P, weight="bold")
    return svg(360, yj + 50, b)


# ------------------------------------------------------------------ 7. while loop
def fc_while():
    b = title("Flowchart: while Loop")
    b += terminal(110, 44, "Start", 80, 26, 11)
    b += down(110, 57, 72)
    b += process(110, 88, "i = 1", 100, 30, 11, mono=True)
    b += down(110, 103, 122)
    b += decision(110, 150, "i <= 5 ?", 110, 54, 10.5, mono=True)
    b += arr([(110, 177), (110, 200)], label="True", lpos=(128, 188))
    b += io(110, 216, "print(i)", 100, 30, 10.5, mono=True)
    b += down(110, 231, 248)
    b += process(110, 264, "i += 1", 100, 30, 11, mono=True)
    b += line("M60 264 H36 V112 H108") + arrowhead(108, 112, 0)
    b += text(28, 190, "repeat", 9.5, color="#777").replace("<text ", '<text transform="rotate(-90 28 190)" ')
    b += arr([(165, 150), (196, 150), (196, 312), (152, 312)], label="False", lpos=(186, 138))
    b += terminal(110, 312, "Stop", 80, 24, 11)
    code = ["i = 1", "while i <= 5:", "    print(i)", "    i += 1", "", "Output: 1 2 3 4 5", "", "Condition checked", "BEFORE each pass:", "may run 0 times."]
    for j, s in enumerate(code):
        b += text(222, 90 + j * 16, sp(s), 10, anchor="start", mono=j < 4, color=P if j < 4 else ("#2E7D32" if j == 5 else "#444"), weight="bold" if j == 5 else "normal")
    b += f'<rect x="214" y="78" width="138" height="72" rx="6" fill="none" stroke="#D9C8F0"/>'
    return svg(360, 330, b)


# ------------------------------------------------------------------ 8. for loop
def fc_for():
    b = title("Flowchart: for Loop")
    b += terminal(110, 44, "Start", 80, 26, 11)
    b += down(110, 57, 80)
    b += decision(110, 112, "more items\nin sequence?", 130, 60, 10)
    b += arr([(110, 142), (110, 166)], label="True", lpos=(128, 154))
    b += process(110, 182, "item = next item", 130, 30, 10.5)
    b += down(110, 197, 214)
    b += process(110, 230, "loop body", 130, 30, 11)
    b += line("M45 230 H26 V70 H108") + arrowhead(108, 70, 0)
    b += arr([(175, 112), (200, 112), (200, 286), (152, 286)], label="False", lpos=(192, 100))
    b += terminal(110, 286, "Stop", 80, 24, 11)
    code = ["for ch in \"GTU\":", "    print(ch)", "", "Output:", "G", "T", "U"]
    for j, s in enumerate(code):
        b += text(214, 92 + j * 16, sp(s), 10.2, anchor="start", mono=True, color=P if j < 2 else GREEN, weight="bold" if j >= 3 else "normal")
    b += text(180, 318, "Works on any sequence: str, list, tuple, set, dict, range.", 9.8, color="#444")
    return svg(360, 330, b)


# ------------------------------------------------------------------ 9. range()
def range_fn():
    b = title("range(start, stop, step)")
    b += text(180, 40, "stop is NOT included", 11, color=RED, weight="bold")
    rows = [("range(5)", list(range(5)), "start=0, step=1"), ("range(2, 8)", list(range(2, 8)), "2 … 7"),
            ("range(1, 10, 2)", list(range(1, 10, 2)), "odd numbers"), ("range(10, 0, -3)", list(range(10, 0, -3)), "counting down"),
            ("range(5, 1)", [], "empty (start > stop)")]
    y = 58
    for e, vals, n in rows:
        b += text(14, y, e, 10.8, anchor="start", mono=True, weight="bold", color=PYB)
        b += text(346, y, n, 9.6, anchor="end", color="#666")
        y += 10
        if vals:
            for i, v in enumerate(vals):
                b += box(14 + i * 34, y, 30, 24, GREENF, GREEN, 4) + text(29 + i * 34, y + 12, str(v), 11, mono=True, weight="bold", color=GREEN)
        else:
            b += box(14, y, 80, 24, GREYF, "#BBB", 4) + text(54, y + 12, "(nothing)", 10, color="#888")
        y += 46
    b += text(180, y - 6, sp("list(range(1, 6)) → [1, 2, 3, 4, 5]"), 10.5, mono=True, color=P, weight="bold")
    b += text(180, y + 12, "range() gives integers only; step cannot be 0.", 10, color="#444")
    return svg(360, y + 24, b)


# ------------------------------------------------------------------ 10. break / continue / pass
def break_continue():
    b = title("break vs continue vs pass")
    panels = [("break", "if i == 4: break", ["ok", "ok", "ok", "stop", "no", "no", "no"], "Output: 1 2 3   (loop ends)"),
              ("continue", "if i == 4: continue", ["ok", "ok", "ok", "skip", "ok", "ok", "ok"], "Output: 1 2 3 5 6 7"),
              ("pass", "if i == 4: pass", ["ok"] * 7, "Output: 1 2 3 4 5 6 7  (does nothing)")]
    b += text(180, 40, sp("for i in range(1, 8):"), 11, mono=True, color=P, weight="bold")
    y = 58
    for name, code, st, out in panels:
        b += box(8, y, 344, 96, "#FCFAFF", "#D9C8F0", 8)
        b += text(20, y + 16, name, 12, anchor="start", mono=True, weight="bold", color=RED if name == "break" else (ORANGE if name == "continue" else GREEN))
        b += text(120, y + 16, sp("    " + code), 10.2, anchor="start", mono=True, color="#333")
        for i, s in enumerate(st):
            x = 30 + i * 44
            f, c, lab = {"ok": (GREENF, GREEN, ""), "stop": (REDF, RED, "break"), "no": (GREYF, "#BBB", ""), "skip": (ORANGEF, ORANGE, "skip")}[s]
            b += box(x, y + 30, 36, 28, f, c, 5) + text(x + 18, y + 44, str(i + 1), 12, mono=True, weight="bold", color=c if s != "no" else "#AAA")
            if lab:
                b += text(x + 18, y + 68, lab, 9, color=c, weight="bold")
            if s == "skip":
                b += line(f"M{x + 4} {y + 34} L{x + 32} {y + 54}", ORANGE, 1.6)
        b += text(20, y + 84, sp(out), 10, anchor="start", mono=True, color="#333", weight="bold")
        y += 104
    b += text(180, y + 4, "break: exit loop · continue: next iteration · pass: placeholder", 9.6, color=P, weight="bold")
    return svg(360, y + 16, b)


DIAGRAMS = {"py2_operators": operators, "py2_bitwise": bitwise, "py2_precedence": precedence, "py2_identity": identity,
            "py2_fc_ifelse": fc_ifelse, "py2_fc_elif": fc_elif, "py2_fc_while": fc_while, "py2_fc_for": fc_for,
            "py2_range": range_fn, "py2_break_continue": break_continue}

if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    for k, f in DIAGRAMS.items():
        with open(os.path.join(OUT, k + ".svg"), "w", encoding="utf-8") as fh:
            fh.write(f())
    print("written", len(DIAGRAMS))
