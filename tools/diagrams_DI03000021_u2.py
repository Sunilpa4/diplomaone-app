"""DI03000021 Data Structures - Unit 2 diagrams: stack, expressions, recursion, queue, circular queue."""
import math, os
from flowchart_lib import *
from diagrams_DI03000021_u1 import (box, cells, CELL, BLUE, BLUEF, GREEN, GREENF, ORANGE, ORANGEF, RED, REDF,
                                    YEL, YELS, TEAL, TEALF)

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "content", "computer", "sem3", "DI03000021", "diagrams")


def vstack(x, y, vals, size=5, w=56, h=26, top_label=True, color=P, fill="#fff", hi=None):
    """Vertical stack drawn bottom-up. vals = list from bottom. Returns svg."""
    b = ""
    for i in range(size):
        yy = y + (size - 1 - i) * h
        v = vals[i] if i < len(vals) else ""
        f = (YEL if hi == i else "#F1E8FC") if v != "" else fill
        b += box(x, yy, w, h, f, color, 0, 1.4)
        if v != "":
            b += text(x + w / 2, yy + h / 2, str(v), 12, mono=True, weight="bold")
        b += text(x - 6, yy + h / 2, str(i), 9, anchor="end", color="#888", mono=True)
    if top_label:
        t = len(vals) - 1
        if t >= 0:
            yy = y + (size - 1 - t) * h + h / 2
            b += arr([(x + w + 26, yy), (x + w + 4, yy)], RED) + text(x + w + 28, yy, "TOP", 9.6, anchor="start", color=RED, weight="bold")
        else:
            b += text(x + w / 2, y + size * h + 12, "TOP = -1", 9.6, color=RED, weight="bold")
    return b


# ------------------------------------------------------------------ 1. stack array representation
def stack_array():
    b = title("Stack: Array Representation (LIFO)")
    b += vstack(60, 40, [10, 20, 30], 6, 70, 30)
    b += text(95, 236, "int stack[MAX];  MAX = 6", 10, mono=True, color=P, weight="bold")
    b += box(190, 44, 160, 168, "#FCFAFF", "#D9C8F0", 8, 1)
    lines = [("TOP", "index of the top element", P), ("TOP = -1", "stack is EMPTY", GREEN), ("TOP = MAX-1", "stack is FULL", RED),
             ("PUSH", "TOP++, then store", BLUE), ("POP", "read, then TOP--", ORANGE)]
    for i, (h, s, c) in enumerate(lines):
        y = 64 + i * 31
        b += text(200, y, h, 11, anchor="start", weight="bold", color=c, mono=True)
        b += text(200, y + 14, s, 9.6, anchor="start", color="#444")
    b += text(180, 262, "Last In, First Out: 30 was pushed last,", 10, color="#444")
    b += text(180, 277, "so 30 is the first to be popped.", 10, color="#444")
    return svg(360, 290, b)


# ------------------------------------------------------------------ 2. push / pop sequence
def push_pop():
    b = title("PUSH and POP Operations")
    steps = [([], "Empty", "TOP=-1"), ([10], "PUSH 10", "TOP=0"), ([10, 20], "PUSH 20", "TOP=1"),
             ([10, 20, 30], "PUSH 30", "TOP=2"), ([10, 20], "POP → 30", "TOP=1")]
    for k, (vals, lab, t) in enumerate(steps):
        x = 14 + k * 69
        for i in range(4):
            yy = 50 + (3 - i) * 26
            v = vals[i] if i < len(vals) else ""
            hi = (k in (1, 2, 3) and i == len(vals) - 1)
            b += box(x, yy, 52, 26, (GREENF if hi else "#F1E8FC") if v != "" else "#fff", P, 0, 1.3)
            if v != "":
                b += text(x + 26, yy + 13, str(v), 11.5, mono=True, weight="bold")
        col = RED if "POP" in lab else (GREEN if "PUSH" in lab else "#555")
        b += text(x + 26, 168, lab, 10, weight="bold", color=col)
        b += text(x + 26, 184, t, 9.4, mono=True, color="#555")
        if k == 4:
            b += box(x, 50 + 1 * 26, 52, 26, REDF, RED, 0, 1.3) + text(x + 26, 50 + 26 + 13, "30", 11.5, mono=True, color=RED)
            b += line(f"M{x + 6} {50 + 26 + 20} L{x + 46} {50 + 26 + 6}", RED, 1.5)
    b += box(12, 200, 336, 60, BLUEF, BLUE, 8)
    b += text(180, 216, "Overflow: PUSH when TOP = MAX − 1 (full)", 10.4, color=RED, weight="bold")
    b += text(180, 234, "Underflow: POP when TOP = −1 (empty)", 10.4, color=RED, weight="bold")
    b += text(180, 250, "PUSH and POP both take O(1) time", 10, color=BLUE)
    return svg(360, 272, b)


# ------------------------------------------------------------------ 3. applications of stack
def stack_apps():
    b = title("Applications of Stack")
    apps = [("Expression conversion", "infix → postfix / prefix"), ("Expression evaluation", "postfix, prefix"),
            ("Recursion", "function call stack"), ("Parenthesis matching", "( [ { } ] ) balanced?"),
            ("Reversing", "string, number, list"), ("Undo / Redo", "editors, Ctrl+Z"),
            ("Browser back", "visited pages"), ("Backtracking", "maze, DFS of graph")]
    for i, (h, s) in enumerate(apps):
        c, r = i % 2, i // 2
        x, y = 12 + c * 172, 36 + r * 52
        f, st = [(BLUEF, BLUE), (YEL, YELS), (GREENF, GREEN), (ORANGEF, ORANGE)][r]
        b += box(x, y, 164, 44, f, st, 8)
        b += text(x + 10, y + 16, h, 10.8, anchor="start", weight="bold")
        b += text(x + 10, y + 32, s, 9.6, anchor="start", color="#555", mono=("(" in s))
    return svg(360, 36 + 4 * 52 + 6, b)


# ------------------------------------------------------------------ 4. notations
def notations():
    b = title("Infix, Prefix and Postfix Notation")
    rows = [("Infix", "operand OP operand", "A + B", BLUE, BLUEF), ("Prefix (Polish)", "OP operand operand", "+ A B", ORANGE, ORANGEF),
            ("Postfix (Reverse Polish)", "operand operand OP", "A B +", GREEN, GREENF)]
    for i, (h, f, ex, c, fl) in enumerate(rows):
        y = 34 + i * 54
        b += box(10, y, 340, 46, fl, c, 8)
        b += text(20, y + 15, h, 11.5, anchor="start", weight="bold", color=c)
        b += text(20, y + 33, f, 10, anchor="start", color="#444")
        b += text(338, y + 23, ex, 14, anchor="end", mono=True, weight="bold")
    y = 34 + 3 * 54 + 8
    b += text(180, y, "Operator precedence (high → low)", 11, weight="bold", color=P)
    pr = [("^", "exponent", "right to left"), ("* / %", "multiply, divide", "left to right"), ("+ -", "add, subtract", "left to right")]
    for i, (o, n, a) in enumerate(pr):
        yy = y + 14 + i * 24
        b += box(30, yy, 300, 22, "#fff" if i % 2 else CELL, "#D9C8F0", 0, 1)
        b += text(70, yy + 11, o, 12, mono=True, weight="bold") + text(170, yy + 11, n, 10) + text(280, yy + 11, a, 9.6, color="#555")
    y += 14 + 3 * 24 + 16
    b += text(180, y, "Example: (A + B) * C", 11, mono=True, weight="bold")
    b += text(180, y + 18, "Prefix : * + A B C", 10.5, mono=True, color=ORANGE, weight="bold")
    b += text(180, y + 34, "Postfix: A B + C *", 10.5, mono=True, color=GREEN, weight="bold")
    b += text(180, y + 54, "Prefix and postfix need no brackets", 9.6, color="#555")
    return svg(360, y + 66, b)


# ------------------------------------------------------------------ 5. postfix evaluation states
def postfix_eval():
    b = title("Evaluating Postfix: 5 3 + 8 2 - *")
    seq = [("5", [5]), ("3", [5, 3]), ("+", [8]), ("8", [8, 8]), ("2", [8, 8, 2]), ("-", [8, 6]), ("*", [48])]
    for k, (s, st) in enumerate(seq):
        x = 8 + k * 50
        op = s in "+-*"
        b += text(x + 22, 40, s, 14, mono=True, weight="bold", color=RED if op else BLUE)
        for i in range(3):
            yy = 56 + (2 - i) * 24
            v = st[i] if i < len(st) else ""
            b += box(x + 2, yy, 40, 24, (YEL if op and i == len(st) - 1 else "#F1E8FC") if v != "" else "#fff", P, 0, 1.2)
            if v != "":
                b += text(x + 22, yy + 12, str(v), 11, mono=True, weight="bold")
    b += box(10, 138, 340, 92, BLUEF, BLUE, 8)
    b += text(20, 154, "Rules (scan left to right):", 10.5, anchor="start", weight="bold", color=BLUE)
    b += text(20, 172, "1. Operand → PUSH it on the stack", 10, anchor="start")
    b += text(20, 189, "2. Operator → POP B, POP A, PUSH (A op B)", 10, anchor="start")
    b += text(20, 206, "3. At the end, the single value left = result", 10, anchor="start")
    b += text(20, 222, "(5 + 3) * (8 − 2) = 8 * 6 = 48", 10.5, anchor="start", mono=True, weight="bold", color=GREEN)
    return svg(360, 242, b)


# ------------------------------------------------------------------ 6. recursion call stack (factorial)
def recursion_fact():
    b = title("Recursion: Call Stack for fact(4)")
    calls = ["fact(4)", "fact(3)", "fact(2)", "fact(1)"]
    rets = ["4 * 6 = 24", "3 * 2 = 6", "2 * 1 = 2", "returns 1"]
    for i, c in enumerate(calls):
        y = 40 + i * 44
        x = 14 + i * 18
        b += box(x, y, 150 - i * 18, 34, ORANGEF if i < 3 else GREENF, ORANGE if i < 3 else GREEN, 6)
        b += text(x + 8, y + 11, c, 11, anchor="start", mono=True, weight="bold")
        b += text(x + 8, y + 25, "4 * fact(3)" if i == 0 else ("3 * fact(2)" if i == 1 else ("2 * fact(1)" if i == 2 else "base case n<=1")), 9.4, anchor="start", mono=True, color="#555")
        if i < 3:
            b += arr([(x + 30, y + 34), (x + 40, y + 44)], ORANGE)
        b += text(330, y + 17, rets[i], 10.5, anchor="end", mono=True, color=GREEN, weight="bold")
        b += arr([(250, y + 17 + 44), (250, y + 21)], GREEN) if i < 3 else ""
    b += text(82, 226, "winding (calls go down)", 9.6, color=ORANGE, weight="bold")
    b += text(285, 226, "unwinding (returns go up)", 9.6, color=GREEN, weight="bold")
    b += box(10, 238, 340, 46, BLUEF, BLUE, 8)
    b += text(180, 254, "Each call is PUSHED on the system stack;", 10, color=BLUE)
    b += text(180, 270, "it is POPPED when the call returns.", 10, color=BLUE)
    return svg(360, 296, b)


# ------------------------------------------------------------------ 7. fibonacci recursion tree
def fib_tree():
    b = title("Recursion Tree for fib(4)")
    nodes = {"f4": (180, 50, "fib(4)"), "f3": (110, 104, "fib(3)"), "f2b": (262, 104, "fib(2)"),
             "f2": (66, 158, "fib(2)"), "f1a": (158, 158, "fib(1)"), "f1b": (226, 158, "fib(1)"), "f0b": (298, 158, "fib(0)"),
             "f1": (36, 212, "fib(1)"), "f0": (104, 212, "fib(0)")}
    edges = [("f4", "f3"), ("f4", "f2b"), ("f3", "f2"), ("f3", "f1a"), ("f2b", "f1b"), ("f2b", "f0b"), ("f2", "f1"), ("f2", "f0")]
    for a, c in edges:
        b += line(f"M{nodes[a][0]} {nodes[a][1] + 12} L{nodes[c][0]} {nodes[c][1] - 12}", "#999", 1.4)
    vals = {"f4": 3, "f3": 2, "f2b": 1, "f2": 1, "f1a": 1, "f1b": 1, "f0b": 0, "f1": 1, "f0": 0}
    for k, (x, y, s) in nodes.items():
        base = s in ("fib(1)", "fib(0)")
        rep = k in ("f2b",)
        b += box(x - 30, y - 12, 60, 24, GREENF if base else (REDF if rep else ORANGEF), GREEN if base else (RED if rep else ORANGE), 12)
        b += text(x, y, s, 10, mono=True, weight="bold")
        if not base:
            b += text(x + 33, y - 12, f"= {vals[k]}", 9.6, anchor="start", color=BLUE, weight="bold")
    b += text(180, 244, "fib(n) = fib(n−1) + fib(n−2),  fib(0)=0, fib(1)=1", 10, mono=True, color=P)
    b += text(180, 262, "fib(2) is computed twice: 9 calls for fib(4)", 9.8, color=RED)
    b += text(180, 278, "Calls grow exponentially → O(2ⁿ) time", 9.8, color="#444", weight="bold")
    return svg(360, 290, b)


# ------------------------------------------------------------------ 8. queue array representation
def queue_array():
    b = title("Queue: Array Representation (FIFO)")
    b += cells(40, 66, ["", 20, 30, 40, "", ""], 46, 34, "#fff", P, {1, 2, 3}, "#F1E8FC", 13)
    for i in range(6):
        b += text(40 + i * 46 + 23, 112, str(i), 9.6, mono=True, color="#888")
    b += arr([(40 + 1 * 46 + 23, 44), (40 + 1 * 46 + 23, 63)], GREEN) + text(40 + 46 + 23, 36, "FRONT=1", 9.6, color=GREEN, weight="bold", mono=True)
    b += arr([(40 + 3 * 46 + 23, 44), (40 + 3 * 46 + 23, 63)], BLUE) + text(40 + 3 * 46 + 23, 36, "REAR=3", 9.6, color=BLUE, weight="bold", mono=True)
    b += text(20, 84, "delete", 9.6, color=GREEN, weight="bold") + arr([(40, 92), (14, 92)], GREEN)
    b += text(342, 84, "insert", 9.6, color=BLUE, weight="bold") + arr([(318, 92), (346, 92)], BLUE)
    b += box(12, 128, 336, 112, "#FCFAFF", "#D9C8F0", 8, 1)
    items = [("Insert (enqueue)", "at REAR:  REAR++, Q[REAR] = item", BLUE), ("Delete (dequeue)", "from FRONT: item = Q[FRONT], FRONT++", GREEN),
             ("Empty", "FRONT = -1  or  FRONT > REAR", ORANGE), ("Full", "REAR = MAX - 1", RED)]
    for i, (h, s, c) in enumerate(items):
        y = 144 + i * 25
        b += text(22, y, h, 10.5, anchor="start", weight="bold", color=c)
        b += text(22, y + 12, s, 9.4, anchor="start", mono=True, color="#333")
    b += text(180, 258, "First In, First Out: like a ticket counter line", 10, color="#444")
    return svg(360, 270, b)


# ------------------------------------------------------------------ 9. simple queue limitation
def queue_limitation():
    b = title("Limitation of a Simple Queue")
    b += text(12, 36, "After 5 inserts and 3 deletes (MAX = 5):", 10.5, anchor="start", weight="bold")
    b += cells(55, 60, ["", "", "", 40, 50], 50, 32, "#fff", P, {3, 4}, "#F1E8FC", 13)
    for i in range(5):
        b += text(55 + i * 50 + 25, 104, str(i), 9.6, mono=True, color="#888")
    b += box(55, 60, 150, 32, "none", RED, 0, 2)
    b += text(130, 120, "free but unusable", 10, color=RED, weight="bold")
    b += text(55 + 3 * 50 + 25, 52, "FRONT=3", 9.4, color=GREEN, mono=True, weight="bold")
    b += text(55 + 4 * 50 + 25, 120, "REAR=4", 9.4, color=BLUE, mono=True, weight="bold")
    b += box(12, 136, 336, 70, REDF, RED, 8)
    b += text(180, 154, "Insert 60 → REAR = MAX − 1 → \"Queue Full\"", 10.5, color=RED, weight="bold")
    b += text(180, 172, "even though 3 places at the front are empty.", 10, color="#444")
    b += text(180, 192, "Memory is wasted: REAR only moves forward.", 10, color="#444")
    b += box(12, 216, 336, 52, GREENF, GREEN, 8)
    b += text(180, 234, "Solution: CIRCULAR QUEUE", 11, color=GREEN, weight="bold")
    b += text(180, 252, "after the last index, REAR wraps back to 0", 10, color="#333")
    return svg(360, 280, b)


# ------------------------------------------------------------------ 10. circular queue
def circular():
    b = title("Circular Queue (MAX = 6)")
    cx, cy, R, r = 120, 150, 92, 48
    vals = {3: 40, 4: 50, 5: 60, 0: 70}
    for i in range(6):
        a1, a2 = math.radians(-90 + i * 60), math.radians(-90 + (i + 1) * 60)
        p = [(cx + R * math.cos(a1), cy + R * math.sin(a1)), (cx + R * math.cos(a2), cy + R * math.sin(a2)),
             (cx + r * math.cos(a2), cy + r * math.sin(a2)), (cx + r * math.cos(a1), cy + r * math.sin(a1))]
        d = (f"M{p[0][0]:.1f} {p[0][1]:.1f} A{R} {R} 0 0 1 {p[1][0]:.1f} {p[1][1]:.1f} L{p[2][0]:.1f} {p[2][1]:.1f} "
             f"A{r} {r} 0 0 0 {p[3][0]:.1f} {p[3][1]:.1f} Z")
        fill = "#F1E8FC" if i in vals else "#fff"
        b += f'<path d="{d}" fill="{fill}" stroke="{P}" stroke-width="1.5"/>'
        am = math.radians(-90 + i * 60 + 30)
        b += text(cx + (R + r) / 2 * math.cos(am), cy + (R + r) / 2 * math.sin(am), str(vals.get(i, "")), 12, mono=True, weight="bold")
        b += text(cx + (R + 12) * math.cos(am), cy + (R + 12) * math.sin(am), f"[{i}]", 9, mono=True, color="#888")
    b += text(cx, cy, "Q", 14, weight="bold", color=P)
    b += arr([(46, 266), (72, 234)], GREEN) + text(46, 278, "FRONT=3", 9.6, color=GREEN, weight="bold", mono=True)
    b += arr([(204, 44), (170, 68)], BLUE) + text(204, 36, "REAR=0", 9.6, color=BLUE, weight="bold", mono=True)
    x0 = 238
    b += box(x0, 40, 116, 224, "#FCFAFF", "#D9C8F0", 8, 1)
    tx = [("Insert:", P), ("REAR =", None), ("(REAR+1)%MAX", None), ("", None), ("Delete:", P), ("FRONT =", None), ("(FRONT+1)%MAX", None),
          ("", None), ("Full:", RED), ("(REAR+1)%MAX", None), ("== FRONT", None), ("", None), ("Empty: FRONT=-1", ORANGE)]
    for i, (s, c) in enumerate(tx):
        b += text(x0 + 8, 56 + i * 16, s, 9.6 if c is None else 10, anchor="start", mono=c is None, color=c or INK, weight="bold" if c else "normal")
    b += text(180, 298, "70 was inserted after [5], so REAR wrapped to [0]", 10, color="#444")
    return svg(360, 310, b)


DIAGRAMS = {"ds2_stack_array": stack_array, "ds2_push_pop": push_pop, "ds2_stack_apps": stack_apps, "ds2_notations": notations,
            "ds2_postfix_eval": postfix_eval, "ds2_recursion_fact": recursion_fact, "ds2_fib_tree": fib_tree,
            "ds2_queue_array": queue_array, "ds2_queue_limit": queue_limitation, "ds2_circular": circular}

if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    for k, f in DIAGRAMS.items():
        with open(os.path.join(OUT, k + ".svg"), "w", encoding="utf-8") as fh:
            fh.write(f())
    print("written", len(DIAGRAMS))
