"""SVG diagrams for Basics of Electronics - Unit 3 (Diodes & Rectifiers). Mobile-first (360 wide)."""
import os, math, sys
sys.path.insert(0, os.path.dirname(__file__))
from diagrams_DI01000151_u1 import svg, text, box, arrow, arrowhead, P, INK

OUT = os.path.join(os.path.dirname(__file__), "..", "content", "computer", "sem1", "DI01000151", "diagrams")
RED, BLUE, GREEN, ORANGE = "#C62828", "#1565C0", "#2E7D32", "#EF6C00"
W = 'fill="none" stroke="#222" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"'


def g(body, extra=""):
    return f'<g {W} {extra}>{body}</g>'


def line(d, color=INK, w=2, dash=None):
    da = f' stroke-dasharray="{dash}"' if dash else ""
    return f'<path d="{d}" fill="none" stroke="{color}" stroke-width="{w}" stroke-linecap="round" stroke-linejoin="round"{da}/>'


def dot(x, y, r=3.2, c=INK):
    return f'<circle cx="{x}" cy="{y}" r="{r}" fill="{c}"/>'


def diode(x, y, ang=0, lead=22, kind="normal", fill="#ffffff", color=INK, scale=1.0):
    """Diode centred at (x,y) pointing in direction `ang` (deg, 0 = anode left, cathode right)."""
    s = f'<path d="M{-lead} 0 H-10 M10 0 H{lead}" fill="none" stroke="{color}" stroke-width="2"/>'
    s += f'<path d="M-10 -10 L-10 10 L10 0 Z" fill="{fill}" stroke="{color}" stroke-width="2" stroke-linejoin="round"/>'
    if kind == "zener":
        s += f'<path d="M4 -14 L10 -10 V10 L16 14" fill="none" stroke="{color}" stroke-width="2"/>'
    else:
        s += f'<path d="M10 -10 V10" fill="none" stroke="{color}" stroke-width="2.4"/>'
    if kind == "varactor":
        s += f'<path d="M16 -10 V10" fill="none" stroke="{color}" stroke-width="2.4"/>'
        s = s.replace(f'M10 0 H{lead}', f'M16 0 H{lead}')
    if kind in ("led", "photo"):
        for dx in (-3, 6):
            if kind == "led":
                s += f'<path d="M{dx} -13 L{dx+9} -24" fill="none" stroke="{ORANGE}" stroke-width="1.8"/>'
                s += arrowhead(dx + 10, -25.5, -50, 6, ORANGE)
            else:
                s += f'<path d="M{dx+12} -27 L{dx+3} -16" fill="none" stroke="{ORANGE}" stroke-width="1.8"/>'
                s += arrowhead(dx + 2, -14.5, 130, 6, ORANGE)
    return f'<g transform="translate({x} {y}) rotate({ang}) scale({scale})">{s}</g>'


def resistor_h(x1, x2, y, color=INK):
    mid = (x1 + x2) / 2
    d = f"M{x1} {y} H{mid-24}"
    for i in range(6):
        d += f" L{mid-24+4+i*8} {y + (-7 if i % 2 == 0 else 7)}"
    d += f" L{mid+24} {y} H{x2}"
    return line(d, color)


def resistor_v(x, y1, y2, color=INK):
    mid = (y1 + y2) / 2
    d = f"M{x} {y1} V{mid-24}"
    for i in range(6):
        d += f" L{x + (7 if i % 2 == 0 else -7)} {mid-24+4+i*8}"
    d += f" L{x} {mid+24} V{y2}"
    return line(d, color)


def coil_v(x, y0, n, bulge_right=True, color=INK):
    d = f"M{x} {y0}"
    for _ in range(n):
        d += f" a10 10 0 0 {1 if bulge_right else 0} 0 20"
    return line(d, color)


def battery_h(x, y, plus_left=True):
    """Battery across a horizontal wire gap from x-8 to x+8. Long plate = +."""
    lx, sx = (x - 5, x + 5) if plus_left else (x + 5, x - 5)
    s = line(f"M{lx} {y-14} V{y+14}", w=2.4) + line(f"M{sx} {y-8} V{y+8}", w=4)
    s += text(lx + (-9 if plus_left else 9), y - 16, "+", 12, weight="bold")
    s += text(sx + (9 if plus_left else -9), y - 16, "−", 12, weight="bold")
    return s


def meter(x, y, label, r=15):
    return (f'<circle cx="{x}" cy="{y}" r="{r}" fill="#fff" stroke="{INK}" stroke-width="2"/>'
            + text(x, y, label, 11 if len(label) > 1 else 13, weight="bold"))


def sine_path(x0, y0, w, a, cycles=2, mode="full", n=120):
    pts = []
    for i in range(n + 1):
        t = i / n
        s = math.sin(t * cycles * 2 * math.pi)
        if mode == "half":
            s = max(s, 0)
        elif mode == "fw":
            s = abs(s)
        pts.append(f"{x0 + t*w:.1f},{y0 - a*s:.1f}")
    return f'<polyline points="{" ".join(pts)}" fill="none" stroke="{P}" stroke-width="2.2"/>'


def axes(x0, y0, w, label_y, label_t="t"):
    x0 = x0 + 12
    s = line(f"M{x0} {y0} H{x0+w}", "#888", 1.3) + arrowhead(x0 + w + 2, y0, 0, 6, "#888")
    s += line(f"M{x0} {y0+42} V{y0-48}", "#888", 1.3) + arrowhead(x0, y0 - 50, -90, 6, "#888")
    s += text(x0 + w + 4, y0 + 12, label_t, 11, color="#555")
    s += text(x0 + 8, y0 - 46, label_y, 11.5, anchor="start", weight="bold", color=P)
    return s


def transformer(x_in, y_top, y_bot, xp=60, xs=96, n=4, ct=False):
    """Input terminals at x_in; primary coil at xp; secondary at xs. Returns svg + secondary ends."""
    s = dot(x_in, y_top, 4, "#fff") + f'<circle cx="{x_in}" cy="{y_top}" r="4" fill="#fff" stroke="{INK}" stroke-width="1.6"/>'
    s += f'<circle cx="{x_in}" cy="{y_bot}" r="4" fill="#fff" stroke="{INK}" stroke-width="1.6"/>'
    mid = (y_top + y_bot) / 2
    p0 = mid - n * 10
    s += line(f"M{x_in+4} {y_top} H{xp} V{p0}") + coil_v(xp, p0, n, True) + line(f"M{xp} {p0+n*20} V{y_bot} H{x_in+4}")
    s += line(f"M{xp+16} {p0-8} V{p0+n*20+8} M{xp+20} {p0-8} V{p0+n*20+8}", INK, 1.8)
    if ct:
        sn = n + 2
        s0 = mid - sn * 10
        s += line(f"M{xs} {y_top} V{s0}") + coil_v(xs, s0, sn, False) + line(f"M{xs} {s0+sn*20} V{y_bot}")
    else:
        s += line(f"M{xs} {y_top} V{p0}") + coil_v(xs, p0, n, False) + line(f"M{xs} {p0+n*20} V{y_bot}")
    return s

# ====================================================================== 1. PN junction


def pn_junction():
    b = text(180, 18, "P-N Junction (Unbiased)", 15, weight="bold", color=P)
    b += '<rect x="30" y="40" width="150" height="120" fill="#FDECEE" stroke="#C62828" stroke-width="1.5"/>'
    b += '<rect x="180" y="40" width="150" height="120" fill="#E8F0FD" stroke="#1565C0" stroke-width="1.5"/>'
    b += '<rect x="148" y="40" width="64" height="120" fill="#EEEEEE" opacity="0.9"/>'
    b += line("M148 40 V160 M212 40 V160", "#777", 1.4, "4 3")
    for r in range(4):
        for c in range(4):
            x, y = 45 + c * 28, 58 + r * 28
            b += f'<circle cx="{x}" cy="{y}" r="5" fill="#fff" stroke="{RED}" stroke-width="2"/>'
            b += f'<circle cx="{223 + c*28}" cy="{y}" r="4.6" fill="{BLUE}"/>'
    for r in range(4):
        y = 58 + r * 28
        b += f'<circle cx="164" cy="{y}" r="8.5" fill="#fff" stroke="{BLUE}" stroke-width="1.6"/>' + text(164, y, "−", 13, weight="bold", color=BLUE)
        b += f'<circle cx="196" cy="{y}" r="8.5" fill="#fff" stroke="{RED}" stroke-width="1.6"/>' + text(196, y, "+", 12, weight="bold", color=RED)
    b += text(80, 172, "P-type", 13, weight="bold", color=RED) + text(275, 172, "N-type", 13, weight="bold", color=BLUE)
    b += line("M150 180 H210", INK, 1.4) + arrowhead(148, 180, 180, 6) + arrowhead(212, 180, 0, 6)
    b += text(180, 194, "Depletion layer", 11.5, weight="bold")
    # potential hill
    b += line("M30 270 H148 C178 270 182 230 212 230 H330", GREEN, 2.2)
    b += line("M222 270 H330", "#999", 1, "3 3") + line("M318 230 V270", INK, 1.3)
    b += arrowhead(318, 230, -90, 6) + arrowhead(318, 270, 90, 6)
    b += text(312, 250, "V₀", 12, anchor="end", weight="bold", color=GREEN)
    b += text(30, 218, "Barrier potential:", 11.5, anchor="start", weight="bold")
    b += text(30, 236, "Si ≈ 0.7 V, Ge ≈ 0.3 V", 11.5, anchor="start", color="#444")
    # legend
    y = 298
    b += f'<circle cx="34" cy="{y}" r="5" fill="#fff" stroke="{RED}" stroke-width="2"/>' + text(44, y, "Hole", 11, anchor="start")
    b += f'<circle cx="94" cy="{y}" r="4.6" fill="{BLUE}"/>' + text(104, y, "Electron", 11, anchor="start")
    b += f'<circle cx="178" cy="{y}" r="7" fill="#fff" stroke="{BLUE}" stroke-width="1.4"/>' + text(178, y, "−", 11, weight="bold", color=BLUE)
    b += f'<circle cx="194" cy="{y}" r="7" fill="#fff" stroke="{RED}" stroke-width="1.4"/>' + text(194, y, "+", 10, weight="bold", color=RED)
    b += text(206, y, "Immobile ions", 11, anchor="start")
    return svg(360, 312, b)

# ====================================================================== 2. diode symbol


def diode_symbol():
    b = text(180, 18, "P-N Junction Diode", 15, weight="bold", color=P)
    b += f'<g transform="translate(180 70) scale(2)">' + diode(0, 0, 0, 40)[len('<g transform="translate(0 0) rotate(0) scale(1.0)">'):-4] + '</g>'
    b += text(70, 104, "Anode (A)", 12.5, weight="bold", color=RED) + text(70, 122, "P-side", 11, color="#555")
    b += text(290, 104, "Cathode (K)", 12.5, weight="bold", color=BLUE) + text(290, 122, "N-side", 11, color="#555")
    b += line("M140 32 H220", GREEN, 1.8) + arrowhead(224, 32, 0, 7, GREEN)
    b += text(180, 146, "Conventional current flows A → K (forward)", 11, color=GREEN, weight="bold")
    b += line("M60 190 H110 M250 190 H300", "#888", 4)
    b += '<rect x="110" y="174" width="140" height="32" rx="6" fill="#2b2b2b"/>'
    b += '<rect x="222" y="174" width="12" height="32" fill="#d9d9d9"/>'
    b += text(180, 225, "Silver band marks the Cathode", 11.5, weight="bold")
    return svg(360, 240, b)

# ====================================================================== 3/4. biasing


def bias(forward=True):
    title = "Forward Bias" if forward else "Reverse Bias"
    b = text(180, 18, title, 15, weight="bold", color=GREEN if forward else RED)
    dl, dr = (172, 188) if forward else (140, 220)
    b += '<rect x="50" y="40" width="130" height="90" fill="#FDECEE" stroke="#C62828" stroke-width="1.5"/>'
    b += '<rect x="180" y="40" width="130" height="90" fill="#E8F0FD" stroke="#1565C0" stroke-width="1.5"/>'
    b += f'<rect x="{dl}" y="40" width="{dr-dl}" height="90" fill="#E0E0E0"/>'
    b += text(70, 56, "P", 15, weight="bold", color=RED) + text(292, 56, "N", 15, weight="bold", color=BLUE)
    holes_x = [70, 98, 126, 154] if forward else [66, 92, 118]
    elec_x = [206, 234, 262, 290] if forward else [242, 268, 294]
    for i, x in enumerate(holes_x):
        y = 78 + (i % 2) * 26
        b += f'<circle cx="{x}" cy="{y}" r="5" fill="#fff" stroke="{RED}" stroke-width="2"/>'
    for i, x in enumerate(elec_x):
        y = 78 + (i % 2) * 26
        b += f'<circle cx="{x}" cy="{y}" r="4.6" fill="{BLUE}"/>'
    if forward:
        b += arrow(100, 122, 140, 122, RED, 1.6) + arrow(260, 122, 220, 122, BLUE, 1.6)
        b += text(180, 146, "Narrow depletion layer", 11, weight="bold")
    else:
        b += arrow(140, 122, 100, 122, RED, 1.6) + arrow(220, 122, 260, 122, BLUE, 1.6)
        b += text(180, 146, "Wide depletion layer", 11, weight="bold")
    # circuit
    b += line("M50 85 H24 V230 H150 M166 230 H220") + resistor_h(220, 300, 230) + line("M300 230 H336 V85 H310")
    b += battery_h(158, 230, plus_left=forward)
    b += text(260, 252, "R", 12, weight="bold")
    if forward:
        b += arrow(24, 190, 24, 150, GREEN, 2.2) + text(32, 172, "I (mA)", 11.5, anchor="start", weight="bold", color=GREEN)
        cap = "P → +ve, N → −ve : large current"
    else:
        b += text(32, 172, "I ≈ 0 (μA)", 11.5, anchor="start", weight="bold", color=RED)
        cap = "P → −ve, N → +ve : very small current"
    b += f'<rect x="10" y="266" width="340" height="30" rx="8" fill="#F7F2FD" stroke="#E0D2F3"/>'
    b += text(180, 281, cap, 12, weight="bold", color=P)
    return svg(360, 304, b)

# ====================================================================== 5. VI characteristics


def vi_char(zener=False):
    title = "Zener Diode V-I Characteristics" if zener else "V-I Characteristics of P-N Diode"
    b = text(180, 18, title, 14.5, weight="bold", color=P)
    ox, oy = 190, 175
    b += line(f"M20 {oy} H340", "#666", 1.4) + arrowhead(342, oy, 0, 7, "#666")
    b += line(f"M{ox} 300 V40", "#666", 1.4) + arrowhead(ox, 38, -90, 7, "#666")
    b += text(338, oy + 16, "V_F (V)", 11, anchor="end", color="#444")
    b += text(24, oy + 16, "V_R (V)", 11, anchor="start", color="#444")
    b += text(ox + 6, 46, "I_F (mA)", 11, anchor="start", color="#444")
    b += text(ox + 6, 298, "I_R (μA / mA)", 11, anchor="start", color="#444")
    # forward
    b += line(f"M{ox} {oy} C{ox+25} {oy-1} {ox+40} {oy-4} {ox+46} {oy-14} S{ox+58} {oy-95} {ox+64} {oy-130}", P, 2.6)
    b += line(f"M{ox+46} {oy-14} V{oy}", "#999", 1.2, "3 3")
    b += text(ox + 50, oy + 14, "V_K", 11, weight="bold", color=GREEN)
    b += text(ox + 80, oy - 70, "Forward\nregion", 11, anchor="start", color=GREEN, weight="bold")
    b += text(ox + 74, oy - 22, "Knee ≈ 0.7 V (Si)\n0.3 V (Ge)", 10.5, anchor="start", color="#444")
    if zener:
        vz = ox - 110
        b += line(f"M{ox} {oy} L{vz+6} {oy+4} C{vz} {oy+8} {vz-2} {oy+20} {vz-4} {oy+115}", P, 2.6)
        b += line(f"M{vz-1} {oy+28} H{ox}", "#999", 1.2, "3 3") + line(f"M{vz-4} {oy+105} H{ox}", "#999", 1.2, "3 3")
        b += text(ox + 6, oy + 28, "I_Z(min)", 10.5, anchor="start", color="#444")
        b += text(ox + 6, oy + 105, "I_Z(max)", 10.5, anchor="start", color="#444")
        b += text(vz - 4, oy - 10, "V_Z", 11.5, weight="bold", color=RED)
        b += line(f"M{vz} {oy-4} V{oy}", RED, 1.4)
        b += text(vz - 10, oy + 60, "Zener\nregion", 11, anchor="end", color=RED, weight="bold")
        b += text(28, 70, "Symbol:", 11, anchor="start", weight="bold") + diode(110, 70, 0, 26, "zener")
    else:
        bx = ox - 120
        b += line(f"M{ox} {oy} L{bx+6} {oy+5} C{bx} {oy+10} {bx-2} {oy+30} {bx-5} {oy+115}", P, 2.6)
        b += text(bx - 4, oy - 10, "V_BR", 11.5, weight="bold", color=RED)
        b += line(f"M{bx} {oy-4} V{oy}", RED, 1.4)
        b += text(bx + 8, oy + 88, "Breakdown", 11, anchor="start", color=RED, weight="bold")
        b += text(ox - 8, oy + 20, "I₀ (reverse saturation\ncurrent)", 10, anchor="end", color="#444")
        b += text(60, 70, "Reverse\nregion", 11, color=RED, weight="bold")
    b += text(180, 318, "Note: different scales for forward and reverse axes", 10, color="#777")
    return svg(360, 326, b)

# ====================================================================== 6. VI test circuit


def vi_circuit():
    b = text(180, 18, "Circuit for Forward V-I Characteristics", 14, weight="bold", color=P)
    b += line("M40 120 V50 H80") + resistor_h(80, 150, 50) + line("M150 50 H175 M205 50 H290 V82")
    b += meter(190, 50, "mA")
    b += diode(290, 120, 90, 38)
    b += line("M290 158 V200 H40 V140")
    # battery vertical (variable)
    b += line("M26 120 H54", INK, 2.4) + line("M32 140 H48", INK, 4)
    b += line("M22 146 L58 112", P, 1.6) + arrowhead(60, 110, -43, 7, P)
    b += text(18, 118, "+", 12, anchor="end", weight="bold")
    b += line("M290 70 H335 V110 M290 175 H335 V140") + meter(335, 125, "V")
    b += dot(290, 70) + dot(290, 175)
    b += text(115, 34, "R (current limiting)", 10.5, color="#444")
    b += text(64, 150, "Variable\nDC supply", 10.5, anchor="start", color="#444")
    b += text(262, 120, "D", 13, weight="bold", anchor="end")
    b += f'<rect x="10" y="216" width="340" height="44" rx="8" fill="#F7F2FD" stroke="#E0D2F3"/>'
    b += text(180, 230, "For reverse characteristics: reverse the supply", 11, weight="bold", color=P)
    b += text(180, 248, "and use a μA meter in place of mA meter", 11, weight="bold", color=P)
    return svg(360, 268, b)

# ====================================================================== 8. zener regulator


def zener_regulator():
    b = text(180, 18, "Zener Diode as Voltage Regulator", 14.5, weight="bold", color=P)
    b += f'<circle cx="30" cy="50" r="4" fill="#fff" stroke="{INK}" stroke-width="1.6"/><circle cx="30" cy="190" r="4" fill="#fff" stroke="{INK}" stroke-width="1.6"/>'
    b += line("M34 50 H70") + resistor_h(70, 150, 50) + line("M150 50 H326 M34 190 H326")
    b += f'<circle cx="330" cy="50" r="4" fill="#fff" stroke="{INK}" stroke-width="1.6"/><circle cx="330" cy="190" r="4" fill="#fff" stroke="{INK}" stroke-width="1.6"/>'
    b += diode(190, 120, -90, 70, "zener")
    b += resistor_v(265, 50, 190)
    b += dot(190, 50) + dot(265, 50) + dot(190, 190) + dot(265, 190)
    b += text(110, 34, "R_S", 12, weight="bold")
    b += text(252, 120, "R_L", 12, weight="bold", anchor="end")
    b += text(158, 124, "D_Z", 12, weight="bold", anchor="end")
    b += arrow(160, 62, 182, 62, GREEN, 1.6) + text(171, 76, "I", 11, weight="bold", color=GREEN)
    b += arrow(205, 82, 205, 104, GREEN, 1.6) + text(212, 94, "I_Z", 11, anchor="start", weight="bold", color=GREEN)
    b += arrow(280, 70, 280, 92, GREEN, 1.6) + text(287, 80, "I_L", 11, anchor="start", weight="bold", color=GREEN)
    b += text(85, 120, "V_in\n(unregulated)", 11, color="#444")
    b += text(30, 34, "+", 13, weight="bold") + text(30, 208, "−", 14, weight="bold")
    b += text(330, 34, "+", 13, weight="bold") + text(330, 208, "−", 14, weight="bold")
    b += text(338, 120, "V_out\n= V_Z", 11, anchor="end", color=P, weight="bold")
    b += f'<rect x="10" y="222" width="340" height="30" rx="8" fill="#F7F2FD" stroke="#E0D2F3"/>'
    b += text(180, 237, "I = I_Z + I_L ,   I = (V_in − V_Z) / R_S", 12, weight="bold", color=P)
    return svg(360, 260, b)

# ====================================================================== 9. varactor


def varactor():
    b = text(180, 18, "Varactor (Varicap) Diode", 15, weight="bold", color=P)
    b += text(20, 56, "Symbol:", 11.5, anchor="start", weight="bold") + diode(130, 56, 0, 34, "varactor")
    b += text(180, 90, "Used in reverse bias  •  C decreases as V_R increases", 11, color=RED, weight="bold")
    ox, oy = 60, 270
    b += line(f"M{ox} {oy} H335", "#666", 1.4) + arrowhead(337, oy, 0, 7, "#666")
    b += line(f"M{ox} {oy} V112", "#666", 1.4) + arrowhead(ox, 110, -90, 7, "#666")
    b += line(f"M{ox+6} 124 C{ox+40} 200 {ox+120} 234 {ox+270} 248", P, 2.6)
    b += text(ox + 8, 116, "C_T (pF)", 11, anchor="start", color="#444")
    b += text(330, oy + 16, "Reverse voltage V_R (V)", 11, anchor="end", color="#444")
    b += text(ox + 90, 170, "C_T ∝ 1 / √V_R", 12, anchor="start", weight="bold", color=P)
    return svg(360, 296, b)

# ====================================================================== 10. photodiode


def photodiode():
    b = text(180, 18, "Photodiode", 15, weight="bold", color=P)
    b += text(20, 62, "Symbol:", 11.5, anchor="start", weight="bold") + diode(130, 62, 0, 34, "photo")
    b += text(180, 96, "Light falls on junction  •  Operated in reverse bias", 11, color=RED, weight="bold")
    ox, oy = 50, 290
    b += line(f"M{ox} {oy} H335", "#666", 1.4) + arrowhead(337, oy, 0, 7, "#666")
    b += line(f"M{ox} {oy} V122", "#666", 1.4) + arrowhead(ox, 120, -90, 7, "#666")
    for i, (lab, h) in enumerate([("Dark", 6), ("L1", 50), ("L2", 95), ("L3", 140)]):
        y = oy - h
        b += line(f"M{ox} {oy} L{ox+22} {y} H296", P if i else "#999", 2.2 if i else 1.8)
        b += text(306, y, lab, 11, anchor="start", weight="bold", color=P if i else "#777")
    b += text(ox + 8, 124, "I_R (μA)", 11, anchor="start", color="#444")
    b += text(330, oy + 16, "Reverse voltage V_R", 11, anchor="end", color="#444")
    b += text(180, oy + 36, "L3 > L2 > L1 (light intensity); Dark = dark current", 11, color=ORANGE, weight="bold")
    return svg(360, 336, b)

# ====================================================================== 11. LED


def led():
    b = text(180, 18, "Light Emitting Diode (LED)", 15, weight="bold", color=P)
    b += text(20, 62, "Symbol:", 11.5, anchor="start", weight="bold") + diode(130, 62, 0, 34, "led")
    b += text(225, 50, "Forward biased", 11, anchor="start", color=GREEN, weight="bold")
    b += text(225, 66, "Anode = longer leg", 11, anchor="start", color="#444")
    b += '<rect x="40" y="120" width="140" height="70" fill="#FDECEE" stroke="#C62828" stroke-width="1.5"/>'
    b += '<rect x="180" y="120" width="140" height="70" fill="#E8F0FD" stroke="#1565C0" stroke-width="1.5"/>'
    b += text(60, 136, "P", 14, weight="bold", color=RED) + text(302, 136, "N", 14, weight="bold", color=BLUE)
    for x in (80, 120, 150):
        b += f'<circle cx="{x}" cy="160" r="5" fill="#fff" stroke="{RED}" stroke-width="2"/>'
    for x in (210, 240, 280):
        b += f'<circle cx="{x}" cy="160" r="4.6" fill="{BLUE}"/>'
    b += arrow(90, 178, 130, 178, RED, 1.5) + arrow(270, 178, 230, 178, BLUE, 1.5)
    for dx in (-16, 0, 16):
        x = 180 + dx
        d = f"M{x} 116"
        for k in range(4):
            d += f" q{4 if k % 2 == 0 else -4} -5 0 -10"
        b += line(d, ORANGE, 1.8) + arrowhead(x, 74, -90, 6, ORANGE)
    b += text(180, 210, "Electron–hole recombination at junction → light (photons)", 10.5, weight="bold")
    b += f'<rect x="10" y="222" width="340" height="30" rx="8" fill="#F7F2FD" stroke="#E0D2F3"/>'
    b += text(180, 237, "GaAs: IR | GaAsP: Red/Yellow | GaP: Green | InGaN: Blue", 10.5, weight="bold", color=P)
    return svg(360, 260, b)

# ====================================================================== 12. multicolour LED


def multicolour_led():
    b = text(180, 18, "Multi-colour LEDs", 15, weight="bold", color=P)
    # bi-colour (2 leads, anti-parallel)
    b += text(90, 40, "Bi-colour (2 leads)", 12, weight="bold")
    b += f'<circle cx="20" cy="115" r="4" fill="#fff" stroke="{INK}" stroke-width="1.6"/><circle cx="160" cy="115" r="4" fill="#fff" stroke="{INK}" stroke-width="1.6"/>'
    b += line("M24 115 H45 V85 M45 115 V145 M156 115 H135 V85 M135 115 V145")
    b += diode(90, 85, 0, 45, "led", "#FFCDD2", "#C62828") + diode(90, 145, 180, 45, "led", "#C8E6C9", "#2E7D32")
    b += text(90, 186, "Red: A→B | Green: B→A", 10.5, color="#444")
    b += text(20, 100, "A", 12, weight="bold") + text(160, 100, "B", 12, weight="bold")
    # RGB common cathode
    b += text(270, 40, "RGB (common cathode)", 12, weight="bold")
    cols = [(220, "R", "#C62828", "#FFCDD2"), (270, "G", "#2E7D32", "#C8E6C9"), (320, "B", "#1565C0", "#BBDEFB")]
    for x, lab, c, f in cols:
        b += f'<circle cx="{x}" cy="62" r="4" fill="#fff" stroke="{INK}" stroke-width="1.6"/>' + text(x - 12, 62, lab, 12, weight="bold", color=c)
        b += diode(x, 112, 90, 46, "led", f, c)
    b += line("M220 158 V168 H320 V158 M270 158 V168") + line("M270 168 V182")
    b += f'<circle cx="270" cy="186" r="4" fill="#fff" stroke="{INK}" stroke-width="1.6"/>'
    b += text(270, 202, "Common (−) – longest leg", 10.5, color="#444")
    b += f'<rect x="10" y="218" width="340" height="44" rx="8" fill="#F7F2FD" stroke="#E0D2F3"/>'
    b += text(180, 232, "Mix R + G = Yellow, R + B = Magenta, G + B = Cyan", 11, weight="bold", color=P)
    b += text(180, 250, "R + G + B = White; vary currents → many colours", 11, weight="bold", color=P)
    return svg(360, 270, b)

# ====================================================================== 13-15. rectifiers


def wave_block(y_in, y_out, mode, labels=None):
    b = axes(40, y_in, 280, "V_in") + sine_path(52, y_in, 280, 34, 2, "full")
    b += axes(40, y_out, 280, "V_out") + sine_path(52, y_out, 280, 34, 2, mode)
    for k in range(1, 4):
        x = 52 + k * 70
        b += line(f"M{x} {y_in+40} V{y_out+10}", "#ccc", 1, "3 3")
    if labels:
        for k, lab in enumerate(labels):
            b += text(52 + 35 + k * 70, y_out + 22, lab, 10.5, weight="bold", color=GREEN if "ON" in lab or "D1" in lab else (RED if "OFF" in lab else BLUE))
    return b


def hwr():
    b = text(180, 18, "Half Wave Rectifier", 15, weight="bold", color=P)
    b += transformer(20, 40, 160)
    b += line("M96 40 H140") + diode(160, 40, 0, 20) + line("M180 40 H240") + resistor_v(240, 40, 160)
    b += line("M96 160 H300 M240 40 H300")
    b += f'<circle cx="300" cy="40" r="4" fill="#fff" stroke="{INK}" stroke-width="1.6"/><circle cx="300" cy="160" r="4" fill="#fff" stroke="{INK}" stroke-width="1.6"/>'
    b += dot(240, 40) + dot(240, 160)
    b += text(160, 64, "D", 13, weight="bold") + text(256, 100, "R_L", 12, weight="bold", anchor="start")
    b += text(318, 100, "V_out", 11.5, weight="bold", color=P) + text(300, 26, "+", 12, weight="bold") + text(300, 178, "−", 13, weight="bold")
    b += text(20, 182, "230 V AC", 10.5, anchor="start", color="#444") + text(78, 196, "Transformer", 10.5, color="#444")
    b += wave_block(262, 362, "half", ["D ON", "D OFF", "D ON", "D OFF"])
    return svg(360, 400, b)


def fwr_ct():
    b = text(180, 18, "Full Wave Centre-Tap Rectifier", 15, weight="bold", color=P)
    b += transformer(20, 40, 180, ct=True)
    b += line("M96 40 H140") + diode(160, 40, 0, 20) + line("M180 40 H280 V180 H180")
    b += diode(160, 180, 0, 20) + line("M140 180 H96")
    b += line("M96 110 H150") + resistor_h(150, 250, 110) + line("M250 110 H280")
    b += dot(280, 110) + dot(96, 110)
    b += text(160, 64, "D1", 12.5, weight="bold") + text(160, 202, "D2", 12.5, weight="bold")
    b += text(200, 94, "R_L", 12, weight="bold")
    b += text(150, 126, "−", 13, weight="bold") + text(266, 126, "+", 13, weight="bold")
    b += text(318, 110, "V_out", 11.5, color=P, weight="bold")
    b += text(110, 104, "CT", 10.5, weight="bold", color="#555", anchor="start")
    b += text(20, 204, "230 V AC", 10.5, anchor="start", color="#444")
    b += wave_block(282, 382, "fw", ["D1 ON", "D2 ON", "D1 ON", "D2 ON"])
    return svg(360, 420, b)


def bridge():
    b = text(180, 18, "Full Wave Bridge Rectifier", 15, weight="bold", color=P)
    b += transformer(20, 50, 170)
    T, B_, Lf, R = (220, 40), (220, 180), (160, 110), (280, 110)
    b += line("M96 50 V28 H220 V40") + line("M96 170 V196 H220 V180")
    ang = math.degrees(math.atan2(70, 60))
    for (p1, p2, lab, lx, ly) in [(T, R, "D1", 262, 64), (B_, R, "D2", 262, 160), (Lf, T, "D3", 176, 64), (Lf, B_, "D4", 176, 160)]:
        mx, my = (p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2
        a = math.degrees(math.atan2(p2[1] - p1[1], p2[0] - p1[0]))
        L = math.hypot(p2[0] - p1[0], p2[1] - p1[1]) / 2
        b += diode(mx, my, round(a, 1), round(L, 1))
        b += text(lx, ly, lab, 11.5, weight="bold", anchor="middle")
    for p in (T, B_, Lf, R):
        b += dot(*p)
    # load: R(+) -> right -> down -> RL -> left -> up to Lf(-), hop over secondary wire
    b += line("M280 110 H326 V150") + resistor_v(326, 150, 240) + line("M326 240 V256 H160 V204 a8 8 0 0 0 0 -16 V110")
    b += text(312, 196, "R_L", 12, weight="bold", anchor="end")
    b += text(336, 128, "+", 13, weight="bold") + text(336, 252, "−", 14, weight="bold")
    b += text(20, 192, "230 V AC", 10.5, anchor="start", color="#444")
    b += wave_block(318, 418, "fw", ["D1,D4", "D2,D3", "D1,D4", "D2,D3"])
    return svg(360, 452, b)


DIAGRAMS = {
    "u3_pn_junction": pn_junction,
    "u3_diode_symbol": diode_symbol,
    "u3_forward_bias": lambda: bias(True),
    "u3_reverse_bias": lambda: bias(False),
    "u3_vi_char": lambda: vi_char(False),
    "u3_vi_circuit": vi_circuit,
    "u3_zener_char": lambda: vi_char(True),
    "u3_zener_regulator": zener_regulator,
    "u3_varactor": varactor,
    "u3_photodiode": photodiode,
    "u3_led": led,
    "u3_multicolour_led": multicolour_led,
    "u3_hwr": hwr,
    "u3_fwr_ct": fwr_ct,
    "u3_bridge": bridge,
}

if __name__ == "__main__":
    for name, fn in DIAGRAMS.items():
        with open(os.path.join(OUT, name + ".svg"), "w", encoding="utf-8") as f:
            f.write(fn())
    print("written", len(DIAGRAMS))
