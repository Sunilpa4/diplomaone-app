"""SVG diagrams for Basics of Electronics - Unit 4 (Bipolar Junction Transistors). Mobile-first (360 wide)."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from diagrams_DI01000151_u1 import svg, text, arrow, arrowhead, P, INK
from diagrams_DI01000151_u3 import (line, dot, resistor_h, resistor_v, meter, RED, BLUE, GREEN, ORANGE, OUT)

N_FILL, P_FILL = "#E8F0FD", "#FDECEE"


def battery_v(x, y, plus_top=True, label=None, label_side="left", variable=False):
    """Vertical battery: wire gap from y-8 to y+8. Long plate = +."""
    ly, sy = (y - 5, y + 5) if plus_top else (y + 5, y - 5)
    s = line(f"M{x-14} {ly} H{x+14}", w=2.4) + line(f"M{x-8} {sy} H{x+8}", w=4)
    tx = x + (20 if label_side == "left" else -20)
    s += text(tx, ly + (-7 if plus_top else 7), "+", 12, weight="bold")
    s += text(tx, sy + (7 if plus_top else -7), "−", 12, weight="bold")
    if variable:
        s += line(f"M{x-16} {y+14} L{x+14} {y-14}", P, 1.6) + arrowhead(x + 16, y - 16, -43, 7, P)
    if label:
        ax = x - 22 if label_side == "left" else x + 22
        s += text(ax, y, label, 11.5, anchor="end" if label_side == "left" else "start", weight="bold")
    return s


def bjt(x, y, kind="npn", m=(1, 0, 0, 1), circle=True, color=INK):
    """Transistor symbol centred at (x,y). Default: base left, collector up-right, emitter down-right.
    m = (a,b,c,d) linear transform. Returns (svg, {'B':(x,y),'C':..,'E':..})."""
    a, b, c, d = m
    s = ""
    if circle:
        s += f'<circle cx="8" cy="0" r="25" fill="#fff" stroke="{color}" stroke-width="1.6"/>'
    s += f'<path d="M-26 0 H0 M20 -20 L0 -7 M0 7 L20 20 M20 -20 V-34 M20 20 V34" fill="none" stroke="{color}" stroke-width="2" stroke-linecap="round"/>'
    s += f'<path d="M0 -15 V15" stroke="{color}" stroke-width="3.4"/>'
    if kind == "npn":
        s += arrowhead(17, 18, 33, 8, color)
    else:
        s += arrowhead(3, 9, 213, 8, color)
    g = f'<g transform="matrix({a} {b} {c} {d} {x} {y})">{s}</g>'

    def tp(px, py):
        return (x + a * px + c * py, y + b * px + d * py)
    return g, {"B": tp(-26, 0), "C": tp(20, -34), "E": tp(20, 34)}


def ax_graph(ox, oy, w, h, xl, yl, color="#666"):
    s = line(f"M{ox} {oy} H{ox+w}", color, 1.4) + arrowhead(ox + w + 2, oy, 0, 7, color)
    s += line(f"M{ox} {oy} V{oy-h}", color, 1.4) + arrowhead(ox, oy - h - 2, -90, 7, color)
    s += text(ox + w, oy + 16, xl, 11, anchor="end", color="#444")
    s += text(ox + 6, oy - h - 2, yl, 11, anchor="start", color="#444")
    return s


def cur(x1, y1, x2, y2, lab, lx, ly, color=GREEN, anchor="start"):
    return arrow(x1, y1, x2, y2, color, 1.8) + text(lx, ly, lab, 11.5, anchor=anchor, weight="bold", color=color)

# ====================================================================== 1. structure


def structure():
    b = text(180, 18, "Construction of Transistor", 15, weight="bold", color=P)

    def block(y0, kind):
        e, bb, cc = (N_FILL, P_FILL, N_FILL) if kind == "npn" else (P_FILL, N_FILL, P_FILL)
        el, bl, cl = ("N", "P", "N") if kind == "npn" else ("P", "N", "P")
        ec, bc, ccc = (BLUE, RED, BLUE) if kind == "npn" else (RED, BLUE, RED)
        s = text(20, y0 - 12, kind.upper() + " transistor", 13, anchor="start", weight="bold", color=INK)
        s += f'<rect x="60" y="{y0}" width="80" height="60" fill="{e}" stroke="{ec}" stroke-width="1.6"/>'
        s += f'<rect x="140" y="{y0}" width="30" height="60" fill="{bb}" stroke="{bc}" stroke-width="1.6"/>'
        s += f'<rect x="170" y="{y0}" width="130" height="60" fill="{cc}" stroke="{ccc}" stroke-width="1.6"/>'
        s += text(100, y0 + 24, el + "⁺⁺" if False else el, 18, weight="bold", color=ec)
        s += text(155, y0 + 24, bl, 16, weight="bold", color=bc) + text(235, y0 + 24, cl, 18, weight="bold", color=ccc)
        s += text(100, y0 + 44, "Emitter", 11, color="#333") + text(155, y0 + 72, "Base", 11, color="#333")
        s += text(235, y0 + 44, "Collector", 11, color="#333")
        s += line(f"M30 {y0+30} H60", INK, 2) + line(f"M300 {y0+30} H330", INK, 2) + line(f"M155 {y0+60} V{y0+64}", INK, 2)
        s += text(24, y0 + 30, "E", 13, anchor="end", weight="bold") + text(336, y0 + 30, "C", 13, anchor="start", weight="bold")
        s += text(140, y0 - 4, "J_E", 10, color=GREEN, weight="bold") + text(170, y0 - 4, "J_C", 10, color=GREEN, weight="bold")
        return s
    b += block(52, "npn") + block(170, "pnp")
    rows = [("Emitter", "Heavily doped, medium size"), ("Base", "Lightly doped, very thin"),
            ("Collector", "Moderately doped, largest")]
    y = 270
    for i, (k, v) in enumerate(rows):
        b += text(30, y + i * 18, k + ":", 11.5, anchor="start", weight="bold", color=P)
        b += text(108, y + i * 18, v, 11.5, anchor="start", color="#333")
    return svg(360, 318, b)

# ====================================================================== 2. symbols


def symbols():
    b = text(180, 18, "Transistor Symbols and Currents", 15, weight="bold", color=P)
    for i, kind in enumerate(["npn", "pnp"]):
        cx = 95 + i * 175
        g, t = bjt(cx, 110, kind)
        b += g
        bx, by = t["B"]; cx_, cy_ = t["C"]; ex, ey = t["E"]
        b += line(f"M{bx} {by} H{bx-26}") + line(f"M{cx_} {cy_} V{cy_-16}") + line(f"M{ex} {ey} V{ey+16}")
        b += text(bx - 32, by, "B", 13, anchor="end", weight="bold")
        b += text(cx_ + 8, cy_ - 14, "C", 13, anchor="start", weight="bold") + text(ex + 8, ey + 14, "E", 13, anchor="start", weight="bold")
        if kind == "npn":
            b += cur(bx - 46, by - 12, bx - 22, by - 12, "I_B", bx - 52, by - 24)
            b += cur(cx_ - 10, cy_ - 22, cx_ - 10, cy_ - 4, "I_C", cx_ - 16, cy_ - 16, anchor="end")
            b += cur(ex - 10, ey + 4, ex - 10, ey + 22, "I_E", ex - 16, ey + 14, anchor="end")
        else:
            b += cur(bx - 22, by - 12, bx - 46, by - 12, "I_B", bx - 52, by - 24)
            b += cur(cx_ - 10, cy_ - 4, cx_ - 10, cy_ - 22, "I_C", cx_ - 16, cy_ - 16, anchor="end")
            b += cur(ex - 10, ey + 22, ex - 10, ey + 4, "I_E", ex - 16, ey + 14, anchor="end")
        b += text(cx, 190, kind.upper(), 14, weight="bold", color=BLUE if kind == "npn" else RED)
        b += text(cx, 208, "Arrow points OUT" if kind == "npn" else "Arrow points IN", 11, color="#444")
    b += f'<rect x="40" y="226" width="280" height="40" rx="8" fill="#F4EEFC" stroke="{P}" stroke-opacity="0.4"/>'
    b += text(180, 238, "Arrow on emitter = direction of conventional current", 10.5, color="#333")
    b += text(180, 255, "I_E = I_B + I_C", 13, weight="bold", color=P)
    return svg(360, 280, b)

# ====================================================================== 3/4. working


def working(kind="npn"):
    npn = kind == "npn"
    b = text(180, 18, ("NPN" if npn else "PNP") + " Transistor – Working", 15, weight="bold", color=P)
    e, bb, cc = (N_FILL, P_FILL, N_FILL) if npn else (P_FILL, N_FILL, P_FILL)
    ec, bc = (BLUE, RED) if npn else (RED, BLUE)
    y0, y1 = 46, 116
    # regions + depletion
    b += f'<rect x="40" y="{y0}" width="100" height="70" fill="{e}" stroke="{ec}" stroke-width="1.6"/>'
    b += f'<rect x="140" y="{y0}" width="34" height="70" fill="{bb}" stroke="{bc}" stroke-width="1.6"/>'
    b += f'<rect x="174" y="{y0}" width="146" height="70" fill="{cc}" stroke="{ec}" stroke-width="1.6"/>'
    b += f'<rect x="136" y="{y0}" width="8" height="70" fill="#D6D6D6"/>'
    b += f'<rect x="168" y="{y0}" width="26" height="70" fill="#D6D6D6"/>'
    lab = ("N", "P", "N") if npn else ("P", "N", "P")
    b += text(60, y0 + 14, lab[0], 14, weight="bold", color=ec) + text(157, y0 + 14, lab[1], 13, weight="bold", color=bc)
    b += text(300, y0 + 14, lab[2], 14, weight="bold", color=ec)
    # carriers flow
    col = BLUE if npn else RED
    b += arrow(60, 86, 300, 86, col, 2.4)
    b += text(180, 102, "electrons (majority) E → C" if npn else "holes (majority) E → C", 10.5, weight="bold", color=col)
    b += text(90, y0 - 8, "Emitter", 11, weight="bold") + text(157, y0 - 8, "Base", 11, weight="bold") + text(250, y0 - 8, "Collector", 11, weight="bold")
    # wiring
    yb = 196
    b += line(f"M60 {y1} V{yb} H86") + line(f"M104 {yb} H230") + line(f"M157 {y1} V{yb}") + line(f"M248 {yb} H300 V{y1}")
    b += dot(157, yb)
    # batteries (horizontal) – VEE between E and B, VCC between B and C
    for x, lbl in ((95, "V_EE"), (239, "V_CC")):
        plus_right = npn
        lx, sx = (x + 5, x - 5) if plus_right else (x - 5, x + 5)
        b += line(f"M{lx} {yb-14} V{yb+14}", w=2.4) + line(f"M{sx} {yb-8} V{yb+8}", w=4)
        b += text(lx + (8 if plus_right else -8), yb - 18, "+", 12, weight="bold") + text(sx + (-8 if plus_right else 8), yb - 18, "−", 12, weight="bold")
        b += text(x, yb + 26, lbl, 11.5, weight="bold")
    # junction bias labels
    b += text(108, 136, "J_E: forward", 10.5, weight="bold", color=GREEN)
    b += text(236, 136, "J_C: reverse", 10.5, weight="bold", color=RED)
    # conventional currents
    if npn:
        b += cur(48, 140, 48, 168, "I_E", 44, 154, anchor="end")
        b += cur(166, 176, 166, 150, "I_B", 172, 162)
        b += cur(310, 176, 310, 140, "I_C", 316, 158)
    else:
        b += cur(48, 168, 48, 140, "I_E", 44, 154, anchor="end")
        b += cur(166, 150, 166, 176, "I_B", 172, 162)
        b += cur(310, 140, 310, 176, "I_C", 316, 158)
    b += f'<rect x="30" y="240" width="300" height="40" rx="8" fill="#F4EEFC" stroke="{P}" stroke-opacity="0.4"/>'
    b += text(180, 252, "I_E = I_B + I_C ;  I_B ≈ 1–5 % of I_E", 12, weight="bold", color=P)
    b += text(180, 269, "Narrow, lightly doped base → most carriers reach collector", 10, color="#333")
    return svg(360, 292, b)

# ====================================================================== 5/6/7. configurations


def cfg_frame(title, common):
    return text(180, 18, title, 15, weight="bold", color=P), common


def cb_circuit():
    b = text(180, 18, "Common Base (CB) Configuration", 15, weight="bold", color=P)
    g, t = bjt(180, 92, "npn", m=(0, -1, -1, 0))
    b += g
    ex, ey = t["E"]; cx, cy = t["C"]; bx, by = t["B"]
    yb = 196
    b += line(f"M{ex} {ey} V60 H50 V128") + battery_v(50, 136, plus_top=False, label="V_EE", label_side="right") + line(f"M50 144 V{yb} H310 V144")
    b += line(f"M{cx} {cy} V60 H226") + resistor_h(226, 290, 60) + line(f"M290 60 H310 V128")
    b += battery_v(310, 136, plus_top=True, label="V_CC", label_side="left")
    b += line(f"M{bx} {by} V{yb}") + dot(bx, yb)
    b += text(258, 44, "R_L", 11.5, weight="bold")
    b += text(ex - 6, ey + 18, "E", 12, weight="bold", anchor="end") + text(cx + 6, cy + 18, "C", 12, weight="bold", anchor="start")
    b += text(bx + 8, by + 22, "B", 12, weight="bold", anchor="start")
    b += cur(108, 50, 80, 50, "I_E", 82, 38) + cur(222, 50, 200, 50, "I_C", 198, 38)
    b += text(105, 160, "Input\n(E–B)", 11, weight="bold", color=BLUE) + text(250, 160, "Output\n(C–B)", 11, weight="bold", color=BLUE)
    b += text(180, yb + 16, "Base is common to input and output", 11, weight="bold", color=GREEN)
    b += f'<rect x="60" y="226" width="240" height="30" rx="8" fill="#F4EEFC" stroke="{P}" stroke-opacity="0.4"/>'
    b += text(180, 241, "Current gain α = I_C / I_E  (0.95 – 0.99)", 12, weight="bold", color=P)
    return svg(360, 268, b)


def ce_circuit():
    b = text(180, 18, "Common Emitter (CE) Configuration", 15, weight="bold", color=P)
    g, t = bjt(196, 104, "npn")
    b += g
    bx, by = t["B"]; cx, cy = t["C"]; ex, ey = t["E"]
    yb = 196
    b += line(f"M{bx} {by} H142") + resistor_h(84, 142, by) + line(f"M84 {by} H50 V{by+16}")
    b += battery_v(50, by + 24, plus_top=True, label="V_BB", label_side="right") + line(f"M50 {by+32} V{yb} H310 V{136}")
    b += line(f"M{cx} {cy} V48 H310 V62") + resistor_v(310, 62, 112) + line("M310 112 V120")
    b += battery_v(310, 128, plus_top=True, label="V_CC", label_side="left")
    b += line(f"M{ex} {ey} V{yb}") + dot(ex, yb)
    b += text(113, by - 16, "R_B", 11.5, weight="bold") + text(326, 87, "R_C", 11.5, weight="bold", anchor="start")
    b += text(bx - 2, by + 16, "B", 12, weight="bold", anchor="end") + text(cx + 6, cy + 6, "C", 12, weight="bold", anchor="start")
    b += text(ex + 6, ey + 4, "E", 12, weight="bold", anchor="start")
    b += cur(56, by - 10, 80, by - 10, "I_B", 56, by - 22) + cur(262, 38, 232, 38, "I_C", 268, 38)
    b += text(110, 165, "Input (B–E)", 11, weight="bold", color=BLUE) + text(262, 165, "Output (C–E)", 11, weight="bold", color=BLUE)
    b += text(180, yb + 16, "Emitter is common to input and output", 11, weight="bold", color=GREEN)
    b += f'<rect x="60" y="226" width="240" height="30" rx="8" fill="#F4EEFC" stroke="{P}" stroke-opacity="0.4"/>'
    b += text(180, 241, "Current gain β = I_C / I_B  (20 – 500)", 12, weight="bold", color=P)
    return svg(360, 268, b)


def cc_circuit():
    b = text(180, 18, "Common Collector (CC) Configuration", 15, weight="bold", color=P)
    g, t = bjt(176, 84, "npn")
    b += g
    bx, by = t["B"]; cx, cy = t["C"]; ex, ey = t["E"]
    yb = 200
    b += line(f"M{bx} {by} H120") + resistor_h(70, 120, by) + line(f"M70 {by} H46 V{by+30}")
    b += battery_v(46, by + 38, plus_top=True, label="V_BB", label_side="right") + line(f"M46 {by+46} V{yb} H312 V{124}")
    b += line(f"M{cx} {cy} V36 H312 V108") + battery_v(312, 116, plus_top=True, label="V_CC", label_side="left")
    b += line(f"M{ex} {ey} V128") + resistor_v(ex, 128, 186) + line(f"M{ex} 186 V{yb}") + dot(ex, yb)
    b += text(95, by - 16, "R_B", 11.5, weight="bold") + text(ex + 14, 157, "R_E\n(load)", 11, weight="bold", anchor="start")
    b += text(bx - 2, by + 16, "B", 12, weight="bold", anchor="end") + text(cx + 6, cy + 4, "C", 12, weight="bold", anchor="start")
    b += text(ex - 8, ey + 6, "E", 12, weight="bold", anchor="end")
    b += cur(50, by - 10, 66, by - 10, "I_B", 48, by - 22) + cur(ex - 12, 130, ex - 12, 156, "I_E", ex - 16, 143, anchor="end")
    b += text(272, 178, "Output\nacross R_E", 11, weight="bold", color=BLUE) + text(100, 170, "Input (B–C)", 11, weight="bold", color=BLUE)
    b += text(180, yb + 16, "Collector is common (through V_CC)", 11, weight="bold", color=GREEN)
    b += f'<rect x="50" y="230" width="260" height="30" rx="8" fill="#F4EEFC" stroke="{P}" stroke-opacity="0.4"/>'
    b += text(180, 245, "Current gain γ = I_E / I_B = β + 1 ; A_v ≈ 1", 12, weight="bold", color=P)
    return svg(360, 272, b)

# ====================================================================== 8. CE characteristics circuit


def ce_test_circuit():
    b = text(180, 18, "Circuit for CE Characteristics (NPN)", 15, weight="bold", color=P)
    g, t = bjt(196, 112, "npn")
    b += g
    bx, by = t["B"]; cx, cy = t["C"]; ex, ey = t["E"]
    yb = 200
    # input side
    b += line(f"M30 {yb} V172") + battery_v(30, 164, plus_top=True, variable=True) + line(f"M30 156 V{by} H44")
    b += resistor_h(44, 92, by) + line(f"M92 {by} H102") + meter(117, by, "µA", 14) + line(f"M131 {by} H{bx}")
    b += dot(150, by) + line(f"M150 {by} V140") + meter(150, 155, "V", 14) + line(f"M150 169 V{yb}") + dot(150, yb)
    b += text(68, by - 16, "R_B", 11, weight="bold") + text(166, 156, "V_BE", 10.5, anchor="start", weight="bold", color=BLUE)
    b += text(18, 128, "V_BB", 11, anchor="start", weight="bold")
    # output side
    b += line(f"M{cx} {cy} V50 H262") + meter(277, 50, "mA", 14) + line(f"M291 50 H330 V156")
    b += battery_v(330, 164, plus_top=True, variable=True) + line(f"M330 172 V{yb} H30")
    b += dot(240, 50) + line(f"M240 50 V108") + meter(240, 123, "V", 14) + line(f"M240 137 V{yb}") + dot(240, yb)
    b += line(f"M{ex} {ey} V{yb}") + dot(ex, yb)
    b += text(256, 98, "V_CE", 10.5, anchor="start", weight="bold", color=BLUE) + text(342, 128, "V_CC", 11, anchor="end", weight="bold")
    b += text(bx - 2, by + 14, "B", 11, weight="bold", anchor="end") + text(cx - 6, cy - 4, "C", 11, weight="bold", anchor="end")
    b += text(ex - 6, ey + 6, "E", 11, weight="bold", anchor="end")
    b += f'<rect x="30" y="218" width="300" height="40" rx="8" fill="#F4EEFC" stroke="{P}" stroke-opacity="0.4"/>'
    b += text(180, 230, "Input: I_B vs V_BE (V_CE constant)", 11, weight="bold", color=P)
    b += text(180, 247, "Output: I_C vs V_CE (I_B constant)", 11, weight="bold", color=P)
    return svg(360, 270, b)

# ====================================================================== 9. CE input characteristics


def ce_input():
    b = text(180, 18, "CE Input Characteristics", 15, weight="bold", color=P)
    ox, oy = 50, 250
    b += ax_graph(ox, oy, 280, 210, "V_BE (V)", "I_B (µA)")
    for vce, sh, c in (("V_CE = 1 V", 0, P), ("V_CE = 5 V", 22, BLUE)):
        x0 = ox + 120 + sh
        b += line(f"M{ox} {oy} L{x0-40} {oy-2} C{x0} {oy-6} {x0+14} {oy-40} {x0+40} {oy-190}", c, 2.6)
        b += (text(x0 + 46, oy - 178, vce, 11, anchor="start", weight="bold", color=c) if sh else
              text(x0 + 32, oy - 196, vce, 11, anchor="end", weight="bold", color=c))
    b += line(f"M{ox+134} {oy} V{oy-30}", "#999", 1.2, "3 3")
    b += text(ox + 134, oy + 16, "0.7 V", 11, weight="bold", color=GREEN)
    b += text(ox + 10, oy - 150, "Like a forward-biased\ndiode curve", 11, anchor="start", color="#444")
    b += text(ox + 10, oy - 100, "Higher V_CE → curve\nshifts right (Early effect)", 10.5, anchor="start", color="#444")
    b += text(180, oy + 34, "Input resistance r_i = ΔV_BE / ΔI_B (V_CE const.)", 11, weight="bold", color=P)
    return svg(360, 296, b)

# ====================================================================== 10. CE output characteristics


def ce_output():
    b = text(180, 18, "CE Output Characteristics", 15, weight="bold", color=P)
    ox, oy, w = 50, 250, 270
    b += f'<rect x="{ox}" y="{oy-210}" width="22" height="210" fill="#FFF3E0"/>'
    b += f'<rect x="{ox+22}" y="{oy-14}" width="{w-22}" height="14" fill="#FDECEE"/>'
    b += ax_graph(ox, oy, w, 214, "V_CE (V)", "I_C (mA)")
    for k, ib in enumerate(["I_B = 0", "20 µA", "40 µA", "60 µA", "80 µA"]):
        y = oy - 6 - k * 38
        if k == 0:
            b += line(f"M{ox} {oy} L{ox+18} {y} L{ox+w-16} {y-2}", "#999", 2)
        else:
            b += line(f"M{ox} {oy} C{ox+10} {y+20} {ox+14} {y+2} {ox+30} {y} L{ox+w-16} {y-8}", P, 2.4)
        b += text(ox + w - 14, y - (8 if k else 2) - 10, ib, 10.5, anchor="end", weight="bold", color=P if k else "#777")
    b += text(ox + 11, oy - 196, "Sat.", 10, weight="bold", color=ORANGE)
    b += text(ox + 140, oy - 196, "Active region", 11.5, weight="bold", color=GREEN)
    b += text(ox + 150, oy + 30, "Cut-off region (I_B = 0, I_C = I_CEO)", 10.5, weight="bold", color=RED)
    b += text(ox + 140, oy - 182, "(amplifier)", 10.5, color=GREEN)
    b += text(180, oy + 50, "β = ΔI_C / ΔI_B ;  r_o = ΔV_CE / ΔI_C", 11.5, weight="bold", color=P)
    return svg(360, 314, b)

# ====================================================================== 11. CB characteristics


def cb_char():
    b = text(180, 18, "CB Characteristics (NPN)", 15, weight="bold", color=P)
    # input
    ox, oy, w, h = 30, 200, 130, 150
    b += text(ox + 65, 38, "Input", 12, weight="bold", color=BLUE)
    b += ax_graph(ox, oy, w, h, "V_EB (V)", "I_E (mA)")
    for sh, lab, c in ((0, "V_CB=0", P), (16, "V_CB=10V", BLUE)):
        x0 = ox + 50 - sh
        b += line(f"M{ox} {oy} L{x0} {oy-3} C{x0+20} {oy-8} {x0+28} {oy-60} {x0+38} {oy-140}", c, 2.2)
    b += text(ox + 4, oy + 34, "— V_CB = 0", 10, anchor="start", weight="bold", color=P)
    b += text(ox + 4, oy + 50, "— V_CB = 10 V", 10, anchor="start", weight="bold", color=BLUE)
    # output
    ox2 = 200
    b += text(ox2 + 70, 38, "Output", 12, weight="bold", color=BLUE)
    b += ax_graph(ox2, oy, 140, h, "V_CB (V)", "I_C (mA)")
    for k in range(1, 4):
        y = oy - k * 38
        b += line(f"M{ox2-14} {oy} C{ox2-6} {y+4} {ox2-2} {y} {ox2+6} {y} L{ox2+128} {y-2}", P, 2.2)
        b += text(ox2 + 128, y - 10, f"I_E={k} mA", 9.5, anchor="end", weight="bold", color=P)
    b += text(270, 238, "I_C ≈ I_E, almost\nindependent of V_CB", 10.5, weight="bold", color=GREEN)
    b += text(180, 272, "r_i = ΔV_EB/ΔI_E (low) ;  r_o = ΔV_CB/ΔI_C (very high)", 10.5, color="#333")
    return svg(360, 286, b)

# ====================================================================== 12. transistor as switch


def switch():
    b = text(180, 18, "Transistor as a Switch", 15, weight="bold", color=P)
    g, t = bjt(140, 130, "npn")
    b += g
    bx, by = t["B"]; cx, cy = t["C"]; ex, ey = t["E"]
    # Vcc rail and load (LED + R_C)
    b += line(f"M{cx} 40 V56") + resistor_v(cx, 56, 76 + 0) if False else ""
    b += text(cx - 8, 44, "+V_CC (5 V)", 11.5, weight="bold", anchor="end")
    b += line(f"M{cx} 40 V48") + resistor_v(cx, 48, 76)
    b += f'<g transform="translate({cx} 86) rotate(90)"><path d="M-10 -9 L-10 9 L6 0 Z" fill="#FFCDD2" stroke="{RED}" stroke-width="2"/><path d="M6 -9 V9" stroke="{RED}" stroke-width="2.4"/></g>'
    b += line(f"M{cx} 76 V78") + line(f"M{cx} 94 V{cy}", INK)
    b += text(cx + 14, 62, "R_C", 11, weight="bold", anchor="start") + text(cx + 14, 87, "LED (load)", 11, weight="bold", anchor="start", color=RED)
    b += line(f"M{ex} {ey} V184") + line(f"M{ex-14} 184 H{ex+14} M{ex-9} 189 H{ex+9} M{ex-4} 194 H{ex+4}")
    b += line(f"M{bx} {by} H96") + resistor_h(48, 96, by) + line(f"M48 {by} H30")
    b += f'<circle cx="26" cy="{by}" r="4" fill="#fff" stroke="{INK}" stroke-width="1.6"/>'
    b += text(72, by - 16, "R_B", 11, weight="bold") + text(20, by + 18, "V_in", 11, weight="bold", anchor="start")
    # right side: two states
    def state(y, title, c, lines_, closed):
        s = f'<rect x="200" y="{y}" width="150" height="74" rx="8" fill="#fff" stroke="{c}" stroke-width="1.6"/>'
        s += text(275, y + 13, title, 11.5, weight="bold", color=c)
        for i, ln in enumerate(lines_):
            s += text(210, y + 32 + i * 15, ln, 10, anchor="start", color="#333")
        sx = 318
        s += line(f"M{sx} {y+26} V{y+36}") + dot(sx, y + 36, 2.6)
        s += line(f"M{sx} {y+36} L{sx + (0 if closed else 9)} {y+56}") + dot(sx, y + 58, 2.6) + line(f"M{sx} {y+58} V{y+68}")
        return s
    b += state(44, "OFF – Cut-off", RED, ["V_in = 0 (LOW)", "I_B = 0, I_C ≈ 0", "V_CE ≈ V_CC", ], False)
    b += state(128, "ON – Saturation", GREEN, ["V_in = HIGH", "I_C = I_C(sat), LED glows", "V_CE ≈ 0.2 V"], True)
    b += f'<rect x="20" y="214" width="320" height="40" rx="8" fill="#F4EEFC" stroke="{P}" stroke-opacity="0.4"/>'
    b += text(180, 226, "I_C(sat) ≈ V_CC / R_C ;  I_B > I_C(sat) / β", 11.5, weight="bold", color=P)
    b += text(180, 243, "Switch works between cut-off and saturation", 10.5, color="#333")
    return svg(360, 266, b)

# ====================================================================== 13. load line


def load_line():
    b = text(180, 18, "DC Load Line and Operating Regions", 15, weight="bold", color=P)
    ox, oy, w = 50, 236, 270
    b += ax_graph(ox, oy, w, 200, "V_CE (V)", "I_C (mA)")
    for k in range(1, 5):
        y = oy - 6 - k * 38
        b += line(f"M{ox} {oy} C{ox+10} {y+20} {ox+14} {y+2} {ox+30} {y} L{ox+w-20} {y-6}", "#B39DDB", 1.8)
    x1, y1 = ox + 200, oy
    x2, y2 = ox, oy - 186
    b += line(f"M{x2} {y2} L{x1} {y1}", RED, 2.6)
    b += dot(x2 + 22, y2 + 20.5, 5, GREEN) + text(x2 + 60, y2 + 20, "Saturation (ON)", 11, anchor="start", weight="bold", color=GREEN)
    b += dot(x1 - 10, y1 - 9.3, 5, RED) + text(x1 - 22, y1 - 34, "Cut-off (OFF)", 11, anchor="end", weight="bold", color=RED)
    qx, qy = ox + 100, oy - 93
    b += dot(qx, qy, 5, P) + text(qx + 10, qy - 10, "Q-point (active,\namplifier)", 10.5, anchor="start", weight="bold", color=P)
    b += text(x1, oy + 16, "V_CC", 11, weight="bold", color=RED) if False else text(x1, oy - 8 + 24, "", 1)
    b += text(ox - 6, y2, "V_CC/R_C", 10, anchor="end", weight="bold", color=RED) if False else ""
    b += text(ox + 60, y2 - 4, "I_C(sat) = V_CC / R_C", 10.5, anchor="start", weight="bold", color=RED)
    b += line(f"M{x1} {oy} V{oy+4}", RED, 2) + text(x1, oy + 16, "V_CC", 10.5, weight="bold", color=RED)
    b += text(180, oy + 48, "Load line: V_CE = V_CC − I_C R_C", 12, weight="bold", color=P)
    return svg(360, 300, b)


DIAGRAMS = {
    "u4_structure": structure,
    "u4_symbols": symbols,
    "u4_npn_working": lambda: working("npn"),
    "u4_pnp_working": lambda: working("pnp"),
    "u4_cb": cb_circuit,
    "u4_ce": ce_circuit,
    "u4_cc": cc_circuit,
    "u4_ce_test": ce_test_circuit,
    "u4_ce_input": ce_input,
    "u4_ce_output": ce_output,
    "u4_cb_char": cb_char,
    "u4_switch": switch,
    "u4_load_line": load_line,
}

if __name__ == "__main__":
    for name, fn in DIAGRAMS.items():
        with open(os.path.join(OUT, name + ".svg"), "w", encoding="utf-8") as f:
            f.write(fn())
    print("written", len(DIAGRAMS))
