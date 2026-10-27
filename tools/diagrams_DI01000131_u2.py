"""DI01000131 Computer Programming Fundamentals - Unit 2 diagrams (decision making, looping)."""
import os
from flowchart_lib import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "content", "computer", "sem1", "DI01000131", "diagrams")
T_ = "True"; F_ = "False"


# ------------------------------------------------------------------ 1. classification of control statements
def control_tree():
    b = title("Classification of Control Statements")
    b += rbox(180, 52, 170, 30, "Control Statements", P, P, 12.5, "bold", "#fff")
    cols = [
        (62, "Decision Making\n(Branching)", ["simple if", "if-else", "nested if-else", "else-if ladder", "switch"]),
        (180, "Looping\n(Iteration)", ["while", "do-while", "for"]),
        (298, "Jump\n(Unconditional)", ["break", "continue", "goto", "return"]),
    ]
    b += line("M180 67 V82") + line("M62 82 H298")
    ymax = 0
    for x, name, items in cols:
        b += arr([(x, 82), (x, 96)])
        ylast = 160 + (len(items) - 1) * 32
        b += line(f"M{x} 136 V{ylast}", "#9C6ADE", 1.4)
        b += rbox(x, 116, 108, 40, name, "#EADDF7", P, 11, "bold", "#333")
        for i, it in enumerate(items):
            b += rbox(x, 160 + i * 32, 100, 24, it, "#fff", "#9C6ADE", 11, mono=True)
        ymax = max(ymax, ylast)
    return svg(360, ymax + 28, b)


# ------------------------------------------------------------------ 2. simple if
def fc_if():
    b = title("Flowchart of Simple if Statement")
    b += terminal(180, 44, "Entry")
    b += down(180, 60, 90) + decision(180, 120, "Test\nexpression?", 120, 60)
    b += arr([(180, 150), (180, 178)], label=T_, lpos=(200, 165))
    b += process(180, 195, "Statement-block", 140)
    b += line("M180 212 V232")
    b += arr([(240, 120), (295, 120), (295, 232), (184, 232)], label=F_, lpos=(268, 111))
    b += down(180, 232, 245) + process(180, 262, "Statement-x", 140)
    b += down(180, 279, 300) + terminal(180, 316, "Next statement", 130)
    b += text(180, 352, "Block runs only when the expression is true.", 10.5, color="#444")
    return svg(360, 366, b)


# ------------------------------------------------------------------ 3. if-else
def fc_ifelse():
    b = title("Flowchart of if-else Statement")
    b += terminal(180, 44, "Entry")
    b += down(180, 60, 90) + decision(180, 120, "Test\nexpression?", 120, 60)
    b += arr([(120, 120), (80, 120), (80, 175)], label=T_, lpos=(98, 111))
    b += arr([(240, 120), (280, 120), (280, 175)], label=F_, lpos=(262, 111))
    b += process(80, 195, "True-block\nstatements", 120, 40) + process(280, 195, "False-block\nstatements", 120, 40)
    b += line("M80 215 V240 H280 V215") + down(180, 240, 258)
    b += process(180, 275, "Statement-x", 140)
    b += down(180, 292, 312) + terminal(180, 328, "Next statement", 130)
    b += text(180, 364, "Exactly one of the two blocks is executed.", 10.5, color="#444")
    return svg(360, 378, b)


# ------------------------------------------------------------------ 4. nested if-else
def fc_nested():
    b = title("Flowchart of Nested if-else")
    b += terminal(180, 44, "Entry")
    b += down(180, 60, 88) + decision(180, 116, "Condition-1?", 120, 56)
    b += arr([(240, 116), (300, 116), (300, 251)], label=F_, lpos=(270, 107))
    b += arr([(120, 116), (90, 116), (90, 160)], label=T_, lpos=(104, 107))
    b += decision(90, 188, "Condition-2?", 110, 56)
    b += arr([(90, 216), (90, 251)], label=T_, lpos=(110, 234))
    b += arr([(145, 188), (195, 188), (195, 251)], label=F_, lpos=(170, 179))
    b += process(90, 268, "Statement-1", 96) + process(195, 268, "Statement-2", 96) + process(300, 268, "Statement-3", 96)
    b += line("M90 285 V310 H300 V285") + line("M195 285 V310")
    b += down(180, 310, 328) + process(180, 345, "Statement-x", 140)
    b += down(180, 362, 380) + terminal(180, 396, "Next statement", 130)
    return svg(360, 422, b)


# ------------------------------------------------------------------ 5. else-if ladder
def fc_ladder():
    b = title("Flowchart of else-if Ladder")
    b += terminal(90, 42, "Entry")
    b += down(90, 58, 74)
    for i, y in enumerate((100, 170, 240)):
        b += decision(90, y, f"Condition-{i + 1}?", 120, 52)
        b += arr([(150, y), (200, y)], label=T_, lpos=(175, y - 9))
        b += process(255, y, f"Statement-{i + 1}", 110, 32)
        b += line(f"M310 {y} H335")
        nxt = y + 44 if i < 2 else 290
        b += arr([(90, y + 26), (90, nxt)], label=F_, lpos=(110, y + 36))
    b += process(90, 307, "Default statement", 130)
    b += line("M335 100 V350") + line("M90 324 V350 H335")
    b += down(210, 350, 368) + process(210, 385, "Statement-x", 140)
    b += down(210, 402, 420) + terminal(210, 436, "Next statement", 130)
    b += text(18, 380, "Conditions are", 10.5, anchor="start", color="#444") \
        + text(18, 394, "checked top to", 10.5, anchor="start", color="#444") \
        + text(18, 408, "bottom.", 10.5, anchor="start", color="#444")
    return svg(360, 460, b)


# ------------------------------------------------------------------ 6. switch
def fc_switch():
    b = title("Flowchart of switch Statement")
    b += terminal(180, 42, "Entry")
    b += down(180, 58, 75) + process(180, 92, "Evaluate switch expression", 200)
    b += arr([(180, 109), (180, 116), (100, 116), (100, 124)])
    labels = ["= value-1 ?", "= value-2 ?", "= value-n ?"]
    for i, y in enumerate((150, 220, 290)):
        b += decision(100, y, labels[i], 130, 52, mono=True)
        b += arr([(165, y), (200, y)], label=T_, lpos=(182, y - 9))
        blk = f"block-{i + 1 if i < 2 else 'n'}; break;"
        b += process(262, y, blk, 124, 32, 10.5, mono=True)
        b += line(f"M324 {y} H342")
        nxt = y + 44 if i < 2 else 334
        b += arr([(100, y + 26), (100, nxt)], label=F_, lpos=(120, y + 36))
    b += process(100, 351, "default block", 130, 34, mono=True)
    b += line("M342 150 V400") + line("M100 368 V400 H342")
    b += down(220, 400, 418) + process(220, 435, "Statement-x", 140)
    b += down(220, 452, 470) + terminal(220, 486, "Next statement", 130)
    b += text(20, 430, "break sends", 10.5, anchor="start", color="#444") + text(20, 444, "control out", 10.5, anchor="start", color="#444") \
        + text(20, 458, "of switch.", 10.5, anchor="start", color="#444")
    return svg(360, 510, b)


# ------------------------------------------------------------------ 7. entry vs exit controlled
def loop_types():
    b = title("Entry-controlled vs Exit-controlled Loop")
    b += line("M180 36 V340", "#C9B3EC", 1.2, "4 4")
    # ---- left: while
    b += text(90, 44, "Entry-controlled", 11.5, weight="bold", color=S_IO) + text(90, 58, "(while, for)", 10.5, color="#444", mono=True)
    b += process(90, 86, "Initialization", 120, 30)
    b += down(90, 101, 122) + decision(90, 150, "Test\ncondition?", 110, 56)
    b += arr([(90, 178), (90, 198)], label=T_, lpos=(108, 188))
    b += process(90, 215, "Body of loop", 120, 32)
    b += arr([(90, 231), (90, 244), (22, 244), (22, 112), (86, 112)])
    b += arr([(145, 150), (164, 150), (164, 260), (90, 260), (90, 272)], label=F_, lpos=(158, 140))
    b += process(90, 289, "Next statement", 120, 32)
    # ---- right: do-while
    b += text(270, 44, "Exit-controlled", 11.5, weight="bold", color=S_DEC) + text(270, 58, "(do-while)", 10.5, color="#444", mono=True)
    b += process(270, 86, "Initialization", 120, 30)
    b += down(270, 101, 124) + process(270, 140, "Body of loop", 120, 32)
    b += down(270, 156, 176) + decision(270, 204, "Test\ncondition?", 110, 56)
    b += arr([(325, 204), (345, 204), (345, 114), (274, 114)], label=T_, lpos=(330, 222))
    b += arr([(270, 232), (270, 272)], label=F_, lpos=(290, 252))
    b += process(270, 289, "Next statement", 120, 32)
    for x, l1, l2 in ((90, "Condition tested first", "Body may run 0 times"), (270, "Condition tested last", "Body runs at least once")):
        b += text(x, 322, l1, 10.5, color="#333", weight="bold") + text(x, 337, l2, 10.5, color="#444")
    return svg(360, 350, b)


# ------------------------------------------------------------------ 8. for loop
def fc_for():
    b = title("Flowchart of for Loop")
    b += text(180, 40, "for (i = 1; i <= n; i++)", 11.5, color=P, mono=True, weight="bold")
    x = 150
    b += process(x, 76, "1. Initialization (i = 1)", 170, 32)
    b += down(x, 92, 118) + decision(x, 148, "2. Test\ni <= n ?", 112, 58)
    b += arr([(x, 177), (x, 200)], label=T_, lpos=(x + 20, 189))
    b += process(x, 217, "3. Body of loop", 150, 32)
    b += down(x, 233, 252) + process(x, 269, "4. Update (i++)", 150, 32)
    b += arr([(x, 285), (x, 300), (40, 300), (40, 106), (x - 4, 106)])
    b += text(30, 210, "Loop", 10.5, color=GREY, weight="bold").replace("<text ", '<text transform="rotate(-90 30 210)" ')
    b += arr([(x + 56, 148), (290, 148), (290, 186)], label=F_, lpos=(250, 139))
    b += process(290, 207, "Exit loop", 100, 40)
    b += text(180, 324, "Initialization runs once; then test → body → update repeats.", 10.5, color="#444")
    return svg(360, 338, b)


# ------------------------------------------------------------------ 9. break and continue
def break_continue():
    b = title("Jumps in Loops: break and continue")
    lines = ["while (test) {", "    ....", "    if (cond)", "        {kw};", "    ....", "}", "next stmt;"]
    cw = 6.32
    for x0, kw, col, cap1, cap2 in ((10, "break", "#C62828", "Exits the loop", "immediately"),
                                    (185, "continue", "#1565C0", "Skips rest of body,", "next iteration")):
        b += f'<rect x="{x0}" y="32" width="165" height="172" rx="8" fill="#F7F2FD" stroke="#C9B3EC" stroke-width="1.2"/>'
        b += text(x0 + 82, 48, kw, 12.5, weight="bold", color=col, mono=True)
        tx = x0 + 8
        ys = [72 + i * 19 for i in range(len(lines))]
        for y, s in zip(ys, lines):
            s = s.replace("{kw}", kw)
            ind = len(s) - len(s.lstrip())
            s = s.strip()
            b += text(tx + ind * cw, y, s, 10.5, anchor="start", color=col if kw in s else INK, mono=True, weight="bold" if kw in s else "normal")
        yk = ys[3]
        xk = tx + len("        " + kw + ";") * cw + 4
        xr = x0 + 155
        if kw == "break":
            b += arr([(xk, yk), (xr, yk), (xr, ys[6]), (tx + len("next stmt;") * cw + 5, ys[6])], col)
        else:
            b += arr([(xk, yk), (xr, yk), (xr, ys[0]), (tx + len("while (test) {") * cw + 5, ys[0])], col)
        b += text(x0 + 82, 222, cap1, 10.5, color="#333", weight="bold") + text(x0 + 82, 237, cap2, 10.5, color="#444")
    return svg(360, 250, b)


# ------------------------------------------------------------------ 10. reverse a number
def fc_reverse():
    b = title("Flowchart: Reverse of a Number")
    b += '<g transform="translate(0,12)">'
    b += terminal(180, 40, "Start")
    b += down(180, 56, 75) + io(180, 92, "Read n", 120)
    b += down(180, 109, 127) + process(180, 144, "rev = 0", 120, mono=True)
    b += down(180, 161, 179) + decision(180, 207, "n > 0 ?", 100, 56, mono=True)
    b += arr([(180, 235), (180, 251)], label=T_, lpos=(200, 244))
    b += process(180, 268, "d = n % 10", 140, mono=True)
    b += down(180, 285, 299) + process(180, 316, "rev = rev*10 + d", 150, mono=True)
    b += down(180, 333, 347) + process(180, 364, "n = n / 10", 140, mono=True)
    b += arr([(180, 381), (180, 396), (50, 396), (50, 170), (176, 170)])
    b += text(40, 290, "Loop", 10.5, color=GREY, weight="bold").replace("<text ", '<text transform="rotate(-90 40 290)" ')
    b += arr([(230, 207), (300, 207), (300, 251)], label=F_, lpos=(264, 198))
    b += io(300, 268, "Print rev", 86)
    b += down(300, 285, 312) + terminal(300, 328, "Stop", 76)
    b += text(180, 424, "Example: n = 472 → rev = 274", 10.5, color="#444", mono=True)
    b += "</g>"
    return svg(360, 450, b)


DIAGRAMS = {
    "c2_control_tree": control_tree, "c2_fc_if": fc_if, "c2_fc_ifelse": fc_ifelse, "c2_fc_nested": fc_nested,
    "c2_fc_ladder": fc_ladder, "c2_fc_switch": fc_switch, "c2_loop_types": loop_types, "c2_fc_for": fc_for,
    "c2_break_continue": break_continue, "c2_fc_reverse": fc_reverse,
}

if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    for k, f in DIAGRAMS.items():
        with open(os.path.join(OUT, k + ".svg"), "w", encoding="utf-8") as fh:
            fh.write(f())
    print("written", len(DIAGRAMS))
