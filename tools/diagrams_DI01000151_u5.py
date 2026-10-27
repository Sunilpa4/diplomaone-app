"""SVG diagrams for Basics of Electronics - Unit 5 (IC 555 Timer). Mobile-first (360 wide)."""
import os, sys, math
sys.path.insert(0, os.path.dirname(__file__))
from diagrams_DI01000151_u1 import svg, text, arrow, arrowhead, box, P, INK
from diagrams_DI01000151_u3 import line, dot, resistor_v, diode, RED, BLUE, GREEN, ORANGE, OUT
from diagrams_DI01000151_u4 import bjt

IC_FILL = "#F4EEFC"


def cap_v(x, y1, y2, label=None, side="left"):
    m = (y1 + y2) / 2
    s = line(f"M{x} {y1} V{m-4} M{x} {m+4} V{y2}") + line(f"M{x-13} {m-4} H{x+13} M{x-13} {m+4} H{x+13}", w=2.6)
    if label:
        s += text(x + (-18 if side == "left" else 18), m, label, 11, anchor="end" if side == "left" else "start", weight="bold")
    return s


def gnd(x, y):
    return line(f"M{x} {y-6} V{y} M{x-10} {y} H{x+10} M{x-6} {y+4} H{x+6} M{x-2} {y+8} H{x+2}")


def term(x, y):
    return f'<circle cx="{x}" cy="{y}" r="4" fill="#fff" stroke="{INK}" stroke-width="1.6"/>'


# IC body used in the application circuits
ICX0, ICX1, ICY0, ICY1 = 160, 250, 70, 210
PIN = {8: (180, ICY0), 4: (230, ICY0), 7: (ICX0, 90), 6: (ICX0, 160), 2: (ICX0, 185),
       3: (ICX1, 130), 1: (185, ICY1), 5: (230, ICY1)}


def ic555_body():
    s = f'<rect x="{ICX0}" y="{ICY0}" width="{ICX1-ICX0}" height="{ICY1-ICY0}" rx="6" fill="{IC_FILL}" stroke="{P}" stroke-width="2"/>'
    s += text((ICX0 + ICX1) / 2, 132, "IC\n555", 15, weight="bold", color=P)
    names = {8: ("8", 0, 12), 4: ("4", 0, 12), 1: ("1", 0, -12), 5: ("5", 0, -12),
             7: ("7", 10, 0), 6: ("6", 10, 0), 2: ("2", 10, 0), 3: ("3", -10, 0)}
    for p, (lab, dx, dy) in names.items():
        x, y = PIN[p]
        s += text(x + dx, y + dy, lab, 10.5, weight="bold", color="#555")
    return s

# ====================================================================== 1. pin diagram


def pin_diagram():
    b = text(180, 18, "IC 555 – Pin Diagram (8-pin DIP)", 15, weight="bold", color=P)
    x0, x1, y0, y1 = 130, 230, 46, 226
    b += f'<rect x="{x0}" y="{y0}" width="{x1-x0}" height="{y1-y0}" rx="8" fill="#2f2f2f"/>'
    b += f'<path d="M168 {y0} A12 12 0 0 0 192 {y0}" fill="#fff"/>'
    b += f'<circle cx="146" cy="{y0+18}" r="4" fill="#ddd"/>'
    b += text(180, 136, "NE555", 14, weight="bold", color="#fff")
    left = [(1, "GND"), (2, "Trigger"), (3, "Output"), (4, "Reset")]
    right = [(8, "+V_CC"), (7, "Discharge"), (6, "Threshold"), (5, "Control V")]
    for i in range(4):
        y = y0 + 28 + i * 42
        b += f'<rect x="{x0-18}" y="{y-6}" width="18" height="12" fill="#bdbdbd"/>'
        b += f'<rect x="{x1}" y="{y-6}" width="18" height="12" fill="#bdbdbd"/>'
        b += text(x0 + 12, y, str(left[i][0]), 12, weight="bold", color="#fff")
        b += text(x1 - 12, y, str(right[i][0]), 12, weight="bold", color="#fff")
        b += text(x0 - 24, y, left[i][1], 12, anchor="end", weight="bold", color=BLUE if i != 2 else GREEN)
        b += text(x1 + 24, y, right[i][1], 12, anchor="start", weight="bold", color=BLUE)
    b += text(180, 248, "Notch / dot marks Pin 1; pins counted anticlockwise (top view)", 10, color="#444")
    return svg(360, 262, b)

# ====================================================================== 2. block diagram


def comparator(xl, yc, label):
    s = f'<path d="M{xl} {yc-22} L{xl+45} {yc} L{xl} {yc+22} Z" fill="#fff" stroke="{BLUE}" stroke-width="2"/>'
    s += text(xl + 18, yc + 32, label, 9.5, weight="bold", color=BLUE)
    return s


def block_diagram():
    b = text(180, 16, "IC 555 – Functional Block Diagram", 15, weight="bold", color=P)
    g = ""
    g += f'<rect x="40" y="30" width="260" height="230" rx="8" fill="#FBF8FF" stroke="{P}" stroke-width="2" stroke-dasharray="6 3"/>'
    # resistor ladder x=70
    g += line("M70 30 V46") + resistor_v(70, 46, 106) + resistor_v(70, 106, 176) + resistor_v(70, 176, 236) + line("M70 236 V260")
    for y in (76, 141, 206):
        g += text(82, y, "5k", 9.5, anchor="start", weight="bold", color="#555")
    g += dot(70, 106) + dot(70, 176)
    g += text(84, 116, "⅔V_CC", 9, anchor="start", weight="bold", color=GREEN) + text(82, 166, "⅓V_CC", 9, anchor="start", weight="bold", color=GREEN)
    # comparator 1 (upper)
    g += comparator(120, 90, "Comp 1")
    g += text(126, 80, "+", 11, weight="bold") + text(126, 100, "−", 12, weight="bold")
    g += line("M105 30 V80 H120") + line("M70 106 H100 V100 H120")
    # comparator 2 (lower)
    g += comparator(120, 190, "Comp 2")
    g += text(126, 180, "+", 11, weight="bold") + text(126, 200, "−", 12, weight="bold")
    g += line("M70 176 H95 V180 H120") + line("M105 260 V200 H120")
    # flip-flop
    g += f'<rect x="190" y="110" width="50" height="62" rx="4" fill="#FFF3E0" stroke="{ORANGE}" stroke-width="2"/>'
    g += text(215, 102, "Flip-Flop", 9.5, weight="bold", color=ORANGE)
    g += text(198, 125, "R", 11, weight="bold") + text(198, 157, "S", 11, weight="bold") + text(230, 141, "Q̄", 11, weight="bold")
    g += line("M165 90 H178 V125 H190") + line("M165 190 H178 V155 H190")
    g += line("M215 30 V110")   # reset pin 4
    # output stage
    g += line("M240 141 H252")
    g += f'<path d="M252 128 L280 141 L252 154 Z" fill="#fff" stroke="{GREEN}" stroke-width="2"/><circle cx="284" cy="141" r="4" fill="#fff" stroke="{GREEN}" stroke-width="2"/>'
    g += line("M288 141 H300") + text(266, 166, "Output\nstage", 9, weight="bold", color=GREEN)
    # discharge transistor
    t, pts = bjt(244, 214, "npn", circle=True)
    g += t
    g += line(f"M205 172 V214 H{pts['B'][0]}")
    g += line(f"M{pts['C'][0]} {pts['C'][1]} V186 H300") + line(f"M{pts['E'][0]} {pts['E'][1]} V252") + gnd(pts['E'][0], 252)
    g += text(244, 246, "Discharge\ntransistor", 8.5, anchor="end", weight="bold", color="#555") if False else ""
    g += text(296, 228, "Q_d", 9.5, anchor="end", weight="bold", color="#555")
    # pin stubs + labels
    pins = [(70, 30, 0, -1, "8", "V_CC"), (105, 30, 0, -1, "6", "THR"), (215, 30, 0, -1, "4", "RESET"),
            (70, 260, 0, 1, "1", "GND"), (105, 260, 0, 1, "2", "TRIG"),
            (40, 106, -1, 0, "5", "CV"), (300, 141, 1, 0, "3", "OUT"), (300, 186, 1, 0, "7", "DIS")]
    for x, y, dx, dy, n, nm in pins:
        x2, y2 = x + dx * 12, y + dy * 12
        g += line(f"M{x} {y} L{x2} {y2}") + f'<rect x="{x2-4}" y="{y2-4}" width="8" height="8" fill="{P}"/>'
        if dy == -1:
            g += text(x2, y2 - 22, n, 9.5, weight="bold", color=P) + text(x2, y2 - 11, nm, 9, weight="bold", color=P)
        elif dy == 1:
            g += text(x2, y2 + 13, n, 9.5, weight="bold", color=P) + text(x2, y2 + 24, nm, 9, weight="bold", color=P)
        elif dx == -1:
            g += text(x2 - 2, y2 - 12, f"{n} {nm}", 9.5, weight="bold", color=P)
        else:
            g += text(x2 - 6, y2 - 12, f"{n} {nm}", 9.5, anchor="start", weight="bold", color=P)
    b += f'<g transform="translate(0 32)">{g}</g>'
    b += text(180, 344, "THR = Threshold, TRIG = Trigger, CV = Control voltage, DIS = Discharge", 9.5, color="#444")
    return svg(360, 354, b)

# ====================================================================== 3. monostable circuit


def common_ic(b, out_label=True, vx=330):
    b += ic555_body()
    # Vcc rail, gnd rail
    b += line("M30 34 H330") + line("M30 240 H330")
    b += text(vx, 48, "+V_CC", 11.5, anchor="end", weight="bold", color=RED)
    b += text(30, 254, "GND", 11, anchor="start", weight="bold", color="#555")
    x8, y8 = PIN[8]; x4, y4 = PIN[4]; x1, y1 = PIN[1]; x5, y5 = PIN[5]
    b += line(f"M{x8} 34 V{y8}") + line(f"M{x4} 34 V{y4}") + dot(x8, 34) + dot(x4, 34)
    b += line(f"M{x1} {y1} V240") + dot(x1, 240)
    b += line(f"M{x5} {y5} V214") + cap_v(x5, 214, 240, "0.01µF", "right") + dot(x5, 240)
    return b


def mono_circuit():
    b = text(180, 14, "555 as Monostable Multivibrator", 15, weight="bold", color=P)
    b = common_ic(b)
    x7, y7 = PIN[7]; x6, y6 = PIN[6]; x2, y2 = PIN[2]; x3, y3 = PIN[3]
    b += line("M110 34 V40") + resistor_v(110, 40, 84) + line(f"M110 84 V{y7}") + dot(110, 34)
    b += line(f"M110 {y7} H{x7}") + line(f"M110 {y7} V{y6} H{x6}") + dot(110, y7) + dot(110, y6)
    b += line(f"M110 {y6} V200") + cap_v(110, 200, 240, "C", "left") + dot(110, 240)
    b += text(96, 62, "R", 12, anchor="end", weight="bold")
    # trigger: pull-up + push button
    b += line("M56 34 V100") + resistor_v(56, 100, 150) + line(f"M56 150 V{y2} H{x2}") + dot(56, 34) + dot(56, y2)
    b += text(46, 125, "10k", 10, anchor="end", weight="bold")
    b += line(f"M56 {y2} V198") + dot(56, 198, 2.6) + line("M56 198 L66 218") + dot(56, 220, 2.6) + line("M56 220 V240") + dot(56, 240)
    b += line("M62 204 H74", INK, 1.6) + text(44, 210, "Trigger\nswitch", 9.5, anchor="end", weight="bold", color=BLUE)
    # output with LED
    b += line(f"M{x3} {y3} H300 V146") + diode(300, 162, 90, 16, "led", "#FFCDD2", RED) + line("M300 178 V188")
    b += resistor_v(300, 188, 232) + line("M300 232 V240") + dot(300, 240) + dot(300, y3)
    b += text(318, 164, "LED", 10.5, anchor="start", weight="bold", color=RED) + text(318, y3 - 10, "V_out", 10.5, anchor="end", weight="bold", color=GREEN)
    b += f'<rect x="70" y="268" width="220" height="30" rx="8" fill="#F4EEFC" stroke="{P}" stroke-opacity="0.4"/>'
    b += text(180, 283, "Pulse width  T = 1.1 R C", 13, weight="bold", color=P)
    return svg(360, 308, b)

# ====================================================================== waveforms helpers


def axis_trace(x0, y0, w, label):
    s = line(f"M{x0} {y0} H{x0+w}", "#999", 1.2) + arrowhead(x0 + w + 2, y0, 0, 6, "#999")
    s += text(x0 - 6, y0 - 14, label, 10.5, anchor="end", weight="bold", color=P)
    return s


def mono_wave():
    b = text(180, 16, "Monostable – Waveforms", 15, weight="bold", color=P)
    x0, w = 78, 262
    t1, T = 120, 110
    # trigger
    y = 70
    b += axis_trace(x0, y, w, "Trigger\n(pin 2)")
    b += line(f"M{x0} {y-30} H{t1} V{y-4} H{t1+8} V{y-30} H{x0+w-4}", BLUE, 2.2)
    b += line(f"M{x0} {y-12} H{x0+w-4}", "#bbb", 1, "4 3") + text(x0 + w, y - 16, "⅓V_CC", 9, anchor="end", color="#777")
    # output
    y = 150
    b += axis_trace(x0, y, w, "Output\n(pin 3)")
    b += line(f"M{x0} {y} H{t1} V{y-40} H{t1+T} V{y} H{x0+w-4}", GREEN, 2.4)
    b += line(f"M{t1} {y+8} H{t1+T}", INK, 1.2) + arrowhead(t1, y + 8, 180, 6) + arrowhead(t1 + T, y + 8, 0, 6)
    b += text(t1 + T / 2, y + 18, "T = 1.1RC", 10.5, weight="bold")
    # capacitor voltage
    y = 250
    b += axis_trace(x0, y, w, "V_C\n(pins 6,7)")
    pts = []
    for i in range(41):
        tt = i / 40
        v = (1 - math.exp(-tt * 1.1)) / (1 - math.exp(-1.1)) * (2 / 3)
        pts.append(f"{t1 + tt*T:.1f},{y - v*60:.1f}")
    b += line(f"M{x0} {y} H{t1}", RED, 2.2) + f'<polyline points="{" ".join(pts)}" fill="none" stroke="{RED}" stroke-width="2.2"/>'
    b += line(f"M{t1+T} {y-40} V{y} H{x0+w-4}", RED, 2.2)
    b += line(f"M{x0} {y-40} H{x0+w-4}", "#bbb", 1, "4 3") + text(x0 + w, y - 46, "⅔V_CC", 9, anchor="end", color="#777")
    for x in (t1, t1 + T):
        b += line(f"M{x} 40 V{y}", "#ccc", 1, "3 3")
    b += text(t1, 276, "trigger", 10, color="#555") + text(t1 + T, 276, "V_C = ⅔V_CC → reset", 10, color="#555")
    return svg(360, 290, b)

# ====================================================================== astable


def astable_circuit(flasher=False):
    title = "555 as LED Flasher (Pulse Generator)" if flasher else "555 as Astable Multivibrator"
    b = text(180, 14, title, 15, weight="bold", color=P)
    b = common_ic(b, vx=286 if flasher else 330)
    x7, y7 = PIN[7]; x6, y6 = PIN[6]; x2, y2 = PIN[2]; x3, y3 = PIN[3]
    b += dot(110, 34) + line("M110 34 V38") + resistor_v(110, 38, 84) + line(f"M110 84 V{y7}")
    b += line(f"M110 {y7} H{x7}") + dot(110, y7) + resistor_v(110, y7, y6 - 6) + line(f"M110 {y6-6} V{y6}")
    b += line(f"M110 {y6} H{x6}") + dot(110, y6) + line(f"M110 {y6} V{y2} H{x2}") + dot(110, y2)
    b += line(f"M110 {y2} V204") + cap_v(110, 204, 240, "C", "left") + dot(110, 240)
    b += text(96, 62, "R_A", 12, anchor="end", weight="bold") + text(96, 125, "R_B", 12, anchor="end", weight="bold")
    if not flasher:
        b += line(f"M{x3} {y3} H310") + term(314, y3) + text(314, y3 - 16, "V_out", 11, weight="bold", color=GREEN)
        b += f'<rect x="20" y="266" width="320" height="44" rx="8" fill="#F4EEFC" stroke="{P}" stroke-opacity="0.4"/>'
        b += text(180, 279, "t_H = 0.693(R_A + R_B)C ;  t_L = 0.693 R_B C", 11, weight="bold", color=P)
        b += text(180, 297, "f = 1.44 / [(R_A + 2R_B) C]", 12, weight="bold", color=P)
        return svg(360, 320, b)
    # two LEDs on output: LED1 to Vcc (ON when output LOW), LED2 to GND (ON when output HIGH)
    b += line(f"M{x3} {y3} H296") + dot(296, y3)
    b += line("M296 34 V40") + resistor_v(296, 40, 78) + diode(296, 100, 90, 14, "led", "#FFCDD2", RED) + line(f"M296 114 V{y3}") + dot(296, 34)
    b += line(f"M296 {y3} V150") + diode(296, 166, 90, 14, "led", "#C8E6C9", GREEN) + line("M296 180 V190") + resistor_v(296, 190, 234) + line("M296 234 V240") + dot(296, 240)
    b += text(318, 102, "LED1", 10, anchor="start", weight="bold", color=RED) + text(318, 168, "LED2", 10, anchor="start", weight="bold", color=GREEN)
    b += text(312, 60, "470Ω", 9.5, anchor="start", weight="bold") + text(312, 212, "470Ω", 9.5, anchor="start", weight="bold")
    b += f'<rect x="20" y="266" width="320" height="44" rx="8" fill="#F4EEFC" stroke="{P}" stroke-opacity="0.4"/>'
    b += text(180, 279, "Output HIGH → LED2 ON ;  Output LOW → LED1 ON", 11, weight="bold", color=P)
    b += text(180, 297, "R_A = 10k, R_B = 68k, C = 10µF → about 1 flash/s", 11, weight="bold", color=P)
    return svg(360, 320, b)


def astable_wave():
    b = text(180, 16, "Astable – Waveforms", 15, weight="bold", color=P)
    x0, w = 78, 262
    tH, tL = 46, 34
    # capacitor voltage
    y = 120
    b += axis_trace(x0, y, w, "V_C\n(pins 2,6)")
    hi, lo = y - 70, y - 35
    b += line(f"M{x0} {hi} H{x0+w-4}", "#bbb", 1, "4 3") + line(f"M{x0} {lo} H{x0+w-4}", "#bbb", 1, "4 3")
    b += text(x0 + w, hi - 6, "⅔V_CC", 9, anchor="end", color="#777") + text(x0 + w, lo + 10, "⅓V_CC", 9, anchor="end", color="#777")
    pts = []
    # first charge from 0 to 2/3
    x = x0 + 8
    pts.append(f"{x0},{y}")
    n = 20
    first = 44
    for i in range(n + 1):
        tt = i / n
        v = (1 - math.exp(-tt * 1.1)) / (1 - math.exp(-1.1))
        pts.append(f"{x0 + tt*first:.1f},{y - v*70:.1f}")
    xc = x0 + first
    edges = [xc]
    while xc < x0 + w - 20:
        for i in range(1, n + 1):  # discharge 2/3 -> 1/3
            tt = i / n
            v = 70 - 35 * (1 - math.exp(-tt * 2)) / (1 - math.exp(-2))
            pts.append(f"{xc + tt*tL:.1f},{y - v:.1f}")
        xc += tL
        edges.append(xc)
        if xc >= x0 + w - 20:
            break
        for i in range(1, n + 1):  # charge 1/3 -> 2/3
            tt = i / n
            v = 35 + 35 * (1 - math.exp(-tt * 1.5)) / (1 - math.exp(-1.5))
            pts.append(f"{xc + tt*tH:.1f},{y - v:.1f}")
        xc += tH
        edges.append(xc)
    b += f'<polyline points="{" ".join(pts)}" fill="none" stroke="{RED}" stroke-width="2.2"/>'
    # output
    y2 = 220
    b += axis_trace(x0, y2, w, "Output\n(pin 3)")
    d = f"M{x0} {y2-50} H{edges[0]}"
    level_high = False
    for e in edges[1:]:
        d += f" V{y2 if not level_high else y2-50} H{e}"
        level_high = not level_high
    d += f" V{y2 if not level_high else y2-50}"
    b += line(d, GREEN, 2.4)
    for e in edges:
        b += line(f"M{e} 48 V{y2}", "#ddd", 1, "3 3")
    a, c = edges[1], edges[2]
    e3 = edges[3]
    b += line(f"M{c} {y2+10} H{e3}", INK, 1.1) + arrowhead(c, y2 + 10, 180, 5) + arrowhead(e3, y2 + 10, 0, 5) + text((c + e3) / 2, y2 + 20, "t_H", 10, weight="bold")
    b += line(f"M{a} {y2+10} H{c}", INK, 1.1) + arrowhead(a, y2 + 10, 180, 5) + arrowhead(c, y2 + 10, 0, 5) + text((a + c) / 2, y2 + 20, "t_L", 10, weight="bold")
    b += line(f"M{a} {y2+34} H{e3}", INK, 1.1) + arrowhead(a, y2 + 34, 180, 5) + arrowhead(e3, y2 + 34, 0, 5) + text((a + e3) / 2, y2 + 44, "T = t_H + t_L", 10, weight="bold")
    b += text(180, 286, "Charging via R_A + R_B (t_H) ; discharging via R_B (t_L)", 10.5, weight="bold", color=P)
    return svg(360, 300, b)

# ====================================================================== frequency counter


def freq_counter():
    b = text(180, 16, "Frequency Counter using 555", 15, weight="bold", color=P)
    col = 120
    items = [(50, "Unknown signal f_x", "#E3F2FD", BLUE), (100, "Wave shaper\n(Schmitt trigger)", "#E3F2FD", BLUE),
             (156, "AND gate", "#FFF3E0", ORANGE), (210, "Decade counter", "#E8F5E9", GREEN),
             (262, "Decoder / driver", "#E8F5E9", GREEN), (314, "7-segment display", "#F4EEFC", P)]
    for i, (y, lab, fill, st) in enumerate(items):
        b += box(col, y, 150, 34 if "\n" not in lab else 40, lab, fill, st, 11, "bold")
        if i:
            py = items[i - 1][0]
            b += arrow(col, py + (20 if "\n" in items[i-1][1] else 17), col, y - (20 if "\n" in lab else 17) - 1, INK, 1.8)
    b += box(290, 156, 120, 52, "555 timer\nGate pulse\nT = 1 s", "#FCE4EC", RED, 10.5, "bold")
    b += arrow(230, 156, 196, 156, RED, 2)
    b += line("M290 182 V210 H196", RED, 1.6, "5 3") + arrowhead(196, 210, 180, 7, RED)
    b += text(292, 224, "reset / latch", 9.5, weight="bold", color=RED)
    b += f'<rect x="20" y="344" width="320" height="30" rx="8" fill="#F4EEFC" stroke="{P}" stroke-opacity="0.4"/>'
    b += text(180, 359, "f_x = Count N / Gate time T  (T = 1 s → f = N Hz)", 11.5, weight="bold", color=P)
    return svg(360, 384, b)


DIAGRAMS = {
    "u5_pin_diagram": pin_diagram,
    "u5_block_diagram": block_diagram,
    "u5_mono_circuit": mono_circuit,
    "u5_mono_wave": mono_wave,
    "u5_astable_circuit": astable_circuit,
    "u5_astable_wave": astable_wave,
    "u5_led_flasher": lambda: astable_circuit(True),
    "u5_freq_counter": freq_counter,
}

if __name__ == "__main__":
    for name, fn in DIAGRAMS.items():
        with open(os.path.join(OUT, name + ".svg"), "w", encoding="utf-8") as f:
            f.write(fn())
    print("written", len(DIAGRAMS))
