"""Extra Plant Utilities diagrams (DI01005011 Summer-2026).

Same rules as chemfigs.py: 360 px canvas, whitelisted primitives only, wrapped text.
"""
from svgdiag import (svg, box, label, arrow, line, circle, path, notes,
                     PURPLE, BLUE, GREEN, ORANGE, RED, GREY,
                     PURPLE_F, BLUE_F, GREEN_F, ORANGE_F, RED_F, GREY_F)


def steam_generator():
    """Water-tube boiler: drum, tubes, furnace, economiser, superheater."""
    b = []
    b.append(label(180, 18, 'Water-tube steam generator', fs=9.4, anchor='middle', bold=True, color=PURPLE))
    # furnace box
    b.append(f'<rect x="56" y="54" width="150" height="150" fill="#FDF6EE" stroke="{ORANGE}" stroke-width="1.2"/>')
    b.append(label(131, 214, 'furnace', fs=7.4, anchor='middle', color=ORANGE))
    # flame
    b.append(path('M92 190 C 88 168 104 156 100 138 C 112 152 118 168 114 190', stroke=ORANGE, width=1.4))
    b.append(path('M124 190 C 120 166 138 152 134 130 C 148 148 154 168 150 190', stroke=RED, width=1.4))
    # water walls (tubes along the walls)
    for x in (60, 202):
        for y in range(62, 200, 14):
            b.append(circle(x, y, 3, stroke=BLUE, fill=BLUE_F, width=1))
    for y in range(62, 200, 14):
        b.append(circle(74, y, 3, stroke=BLUE, fill=BLUE_F, width=1))
    b.append(label(66, 46, 'water walls', fs=7, anchor='middle', color=BLUE))
    # steam drum
    b.append(f'<rect x="94" y="34" width="80" height="20" rx="10" fill="{BLUE_F}" stroke="{BLUE}" stroke-width="1.3"/>')
    b.append(label(134, 30, 'steam drum', fs=7.2, anchor='middle', color=BLUE))
    b.append(line(134, 54, 134, 60, color=BLUE, dash='3 3'))
    # superheater
    b.append(f'<rect x="212" y="60" width="46" height="52" rx="4" fill="{PURPLE_F}" stroke="{PURPLE}" stroke-width="1.2"/>')
    b.append(label(235, 74, 'super', fs=7, anchor='middle', color=PURPLE))
    b.append(label(235, 84, 'heater', fs=7, anchor='middle', color=PURPLE))
    b.append(arrow(174, 48, 212, 66, color=PURPLE))
    b.append(arrow(258, 86, 300, 86, color=PURPLE))
    b.append(label(302, 82, 'to turbine', fs=7, color=PURPLE))
    # economiser
    b.append(f'<rect x="212" y="130" width="46" height="48" rx="4" fill="{GREEN_F}" stroke="{GREEN}" stroke-width="1.2"/>')
    b.append(label(235, 144, 'econo-', fs=7, anchor='middle', color=GREEN))
    b.append(label(235, 154, 'miser', fs=7, anchor='middle', color=GREEN))
    b.append(arrow(258, 170, 300, 170, color=GREEN))
    b.append(label(302, 166, 'feed in', fs=7, color=GREEN))
    b.append(line(214, 130, 206, 120, color=GREEN))
    b.append(line(206, 120, 206, 44, color=GREEN))
    b.append(arrow(206, 44, 176, 44, color=GREEN))
    b.append(label(200, 38, 'feed water', fs=6.6, anchor='end', color=GREEN))
    # air preheater and flue
    b.append(box(212, 200, 46, 26, 'air pre-heater', stroke=GREY, fill=GREY_F, fs=6.6))
    b.append(arrow(206, 190, 212, 206, color=GREY))
    b.append(arrow(258, 213, 300, 213, color=GREY))
    b.append(label(302, 209, 'flue gas', fs=7, color=GREY))
    n = notes(14, 240, 'Feed water is heated in the economiser, boiled in the tubes and the drum,',
              'then dried and superheated before it leaves for the turbine.')
    b.append(n)
    return svg(''.join(b), n.bottom, None)


def superheater():
    b = []
    b.append(label(180, 16, 'Convection superheater', fs=9.4, anchor='middle', bold=True, color=PURPLE))
    b.append(label(180, 32, 'flue-gas pass of the boiler', fs=7.2, anchor='middle', color=GREY))
    b.append(f'<rect x="30" y="44" width="300" height="136" rx="6" fill="#FCFBFD" stroke="{GREY}" stroke-width="1.2"/>')
    # serpentine coil block
    b.append(f'<rect x="118" y="88" width="124" height="64" rx="4" fill="#F7F2FB" stroke="{PURPLE}" stroke-width="1.4"/>')
    for y in (104, 120, 136):
        b.append(f'<path d="M126 {y} L142 {y} L142 {y+8} L158 {y+8} L158 {y} L174 {y} L174 {y+8} '
                 f'L190 {y+8} L190 {y} L206 {y}" fill="none" stroke="{PURPLE}" stroke-width="1.1"/>')
    b.append(label(180, 82, 'serpentine coils', fs=6.8, anchor='middle', color=PURPLE))
    # gas flow above and below the coil
    for y in (60, 166):
        b.append(arrow(44, y, 110, y, color=GREY, head=4))
        b.append(arrow(250, y, 318, y, color=ORANGE, head=4))
    b.append(label(77, 52, 'hot gas in', fs=6.6, anchor='middle', color=GREY))
    b.append(label(284, 52, 'gas out', fs=6.6, anchor='middle', color=ORANGE))
    # steam in from the drum, steam out to the turbine
    b.append(box(40, 96, 46, 26, 'drum', stroke=BLUE, fill=BLUE_F, fs=7.6))
    b.append(label(63, 88, 'saturated steam', fs=6.4, anchor='middle', color=BLUE))
    b.append(arrow(86, 110, 116, 110, color=BLUE))
    b.append(arrow(242, 110, 316, 110, color=RED))
    b.append(label(276, 102, 'superheated out', fs=6.5, anchor='middle', color=RED))
    n = notes(14, 190, 'The coil sits in the gas path, so the steam picks up heat without any flame',
              'touching the tube. Rating: steam leaves 30–60 °C above saturation.')
    b.append(n)
    return svg(''.join(b), n.bottom, None)


def economizer_trap():
    b = []
    b.append(label(180, 18, 'Economiser and steam trap', fs=9.4, anchor='middle', bold=True, color=PURPLE))
    # ---- economiser (left half)
    b.append(label(96, 36, 'Economiser', fs=8.4, anchor='middle', bold=True, color=GREEN))
    b.append(f'<rect x="44" y="44" width="104" height="96" rx="5" fill="{GREEN_F}" stroke="{GREEN}" stroke-width="1.2"/>')
    for y in (58, 76, 94, 112):
        b.append(path(f'M52 {y} L64 {y} L64 {y+8} L76 {y+8} L76 {y}', stroke=BLUE, width=1.3))
        b.append(path(f'M84 {y} L96 {y} L96 {y+8} L108 {y+8} L108 {y}', stroke=BLUE, width=1.3))
        b.append(path(f'M116 {y} L128 {y} L128 {y+8} L140 {y+8} L140 {y}', stroke=BLUE, width=1.3))
    b.append(arrow(20, 70, 44, 70, color=BLUE))
    b.append(label(18, 66, 'feed', fs=6.2, anchor='end', color=BLUE))
    b.append(arrow(148, 66, 162, 66, color=GREEN))
    b.append(label(96, 132, 'water tubes', fs=6.6, anchor='middle', color=BLUE))
    b.append(label(146, 162, 'hot gas rises', fs=6.2, anchor='start', color=ORANGE))
    for x in (52, 74, 96, 118, 140):
        b.append(arrow(x, 150, x, 140, color=ORANGE, head=3))
    # ---- steam trap (right half)
    b.append(label(268, 36, 'Steam trap', fs=8.4, anchor='middle', bold=True, color=PURPLE))
    b.append(box(200, 44, 136, 22, 'steam + condensate', stroke=BLUE, fill=BLUE_F, fs=7))
    b.append(arrow(268, 66, 268, 80, color=BLUE))
    b.append(f'<rect x="228" y="80" width="80" height="46" rx="6" fill="#FCFBFD" stroke="{PURPLE}" stroke-width="1.4"/>')
    b.append(label(268, 100, 'trap', fs=7.6, anchor='middle', bold=True, color=PURPLE))
    b.append(label(268, 112, 'valve + float', fs=6.6, anchor='middle', color=GREY))
    # condensate out, steam stopped
    b.append(arrow(268, 126, 268, 148, color=GREEN))
    b.append(label(272, 146, 'condensate out', fs=6.8, color=GREEN))
    b.append(label(222, 104, 'steam cannot pass', fs=6.2, anchor='end', color=BLUE))
    n = notes(14, 176, 'The economiser heats the feed water with the leaving flue gas; the trap',
              'passes condensate but holds the live steam back.')
    b.append(n)
    return svg(''.join(b), n.bottom, None)


def rotary_compressor():
    b = []
    b.append(label(180, 18, 'Rotary compressors', fs=9.4, anchor='middle', bold=True, color=PURPLE))
    # ---- sliding vane (left)
    b.append(label(88, 36, 'Sliding vane', fs=8.2, anchor='middle', bold=True, color=BLUE))
    b.append(circle(88, 92, 46, stroke=BLUE, fill='#F7FBFE', width=1.5))
    b.append(circle(80, 92, 12, stroke=GREY, fill=GREY_F, width=1.3))
    b.append(label(80, 95, 'rotor', fs=6.2, anchor='middle', color=GREY))
    import math
    for deg in range(0, 360, 45):
        a = math.radians(deg)
        x1, y1 = 80 + 12 * math.cos(a), 92 + 12 * math.sin(a)
        x2, y2 = 80 + 44 * math.cos(a), 92 + 44 * math.sin(a)
        b.append(f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{PURPLE}" '
                 f'stroke-width="2.4"/>')
    b.append(arrow(24, 92, 44, 92, color=GREEN))
    b.append(label(30, 84, 'in', fs=6.6, color=GREEN))
    b.append(arrow(132, 92, 152, 92, color=ORANGE))
    b.append(label(140, 84, 'out', fs=6.6, color=ORANGE))
    b.append(label(88, 152, 'eccentric rotor, vanes slide out', fs=6.4, anchor='middle', color=GREY))
    # ---- screw (right): two rotors seen end-on, inside the casing
    b.append(label(268, 36, 'Twin screw', fs=8.2, anchor='middle', bold=True, color=PURPLE))
    b.append(f'<rect x="206" y="46" width="126" height="92" rx="10" fill="#FCFBFD" stroke="{PURPLE}" stroke-width="1.3"/>')
    import math as _m
    for cx, lobes, phase, col in ((248, 4, 0, BLUE), (288, 6, 20, GREEN)):
        b.append(circle(cx, 92, 24, stroke=col, fill='#FFFFFF', width=1.3))
        for k in range(lobes):
            a = _m.radians(phase + k * 360 / lobes)
            x1, y1 = cx + 8 * _m.cos(a), 92 + 8 * _m.sin(a)
            x2, y2 = cx + 25 * _m.cos(a), 92 + 25 * _m.sin(a)
            b.append(line(x1, y1, x2, y2, color=col, width=2.6))
    b.append(label(268, 148, 'male and female rotor, end view', fs=6.4, anchor='middle', color=GREY))
    b.append(arrow(198, 70, 206, 70, color=GREEN))
    b.append(label(202, 62, 'in', fs=6.4, color=GREEN))
    b.append(arrow(332, 112, 344, 112, color=ORANGE))
    b.append(label(338, 104, 'out', fs=6.4, color=ORANGE))
    n = notes(14, 166, 'Vane: the rotor is off-centre in the casing, so the space between two vanes '
              'shrinks and the air is squeezed.',
              'Screw: two meshing rotors trap air in the gaps and push it along the axis as the gaps close.')
    b.append(n)
    return svg(''.join(b), n.bottom, None)


def steam_jet_refrigeration():
    b = []
    b.append(label(180, 18, 'Steam-jet (ejector) refrigeration', fs=9.2, anchor='middle', bold=True, color=PURPLE))
    # motive steam in
    b.append(box(12, 58, 62, 26, 'motive steam', stroke=RED, fill=RED_F, fs=7.2))
    b.append(arrow(74, 71, 92, 71, color=RED))
    # ejector: converging-diverging
    b.append(path('M92 52 L124 64 L124 78 L92 90 Z', stroke=PURPLE, width=1.4))
    b.append(path('M124 64 L166 50 L166 92 L124 78 Z', stroke=PURPLE, width=1.4))
    b.append(label(129, 108, 'ejector', fs=6.8, anchor='middle', color=PURPLE))
    # condenser
    b.append(box(186, 44, 96, 34, ['condenser', 'at 35–40 °C'], stroke=ORANGE, fill=ORANGE_F, fs=7.2))
    b.append(arrow(166, 71, 186, 61, color=PURPLE))
    b.append(arrow(282, 61, 302, 61, color=GREY))
    b.append(label(304, 56, 'air out', fs=6.4, color=GREY))
    # condensate return down the right side
    b.append(line(234, 78, 234, 96, color=GREY))
    b.append(arrow(234, 96, 234, 112, color=GREY, head=0))
    b.append(label(240, 106, 'condensate', fs=6.4, color=GREY))
    # flash chamber
    b.append(f'<rect x="96" y="152" width="112" height="58" rx="6" fill="{BLUE_F}" stroke="{BLUE}" stroke-width="1.3"/>')
    b.append(label(152, 172, 'flash chamber', fs=7.4, anchor='middle', color=BLUE))
    b.append(label(152, 184, 'chilled water 5–10 °C', fs=6.4, anchor='middle', color=BLUE))
    b.append(arrow(234, 112, 196, 152, color=GREY))
    # vapour from chamber up to the ejector throat
    b.append(arrow(130, 152, 132, 92, color=BLUE))
    b.append(label(112, 120, 'vapour', fs=6.6, anchor='end', color=BLUE))
    # chilled water out and warm return
    b.append(arrow(96, 178, 64, 178, color=GREEN))
    b.append(label(60, 172, 'chilled', fs=6.4, anchor='end', color=GREEN))
    b.append(label(60, 182, 'water', fs=6.4, anchor='end', color=GREEN))
    b.append(arrow(152, 210, 152, 226, color=GREY, head=0))
    b.append(label(158, 224, 'warm water return', fs=6.4, color=GREY))
    n = notes(14, 246, 'High-pressure steam expands through the ejector and drags vapour out of the',
              'flash chamber. The chamber pressure falls, water flashes at 5–10 °C and cools,',
              'and the mixture is compressed to condenser pressure. No compressor is needed.')
    b.append(n)
    return svg(''.join(b), n.bottom, None)


def ozone_sterilizer():
    b = []
    b.append(label(180, 18, 'Ozone sterilisation of water', fs=9.4, anchor='middle', bold=True, color=PURPLE))
    b.append(box(14, 52, 70, 26, 'air / O2', stroke=GREY, fill=GREY_F, fs=7.4))
    b.append(arrow(84, 65, 104, 65))
    b.append(box(104, 46, 86, 38, ['ozone generator', 'silent discharge'], stroke=PURPLE, fill=PURPLE_F, fs=7.2))
    b.append(arrow(190, 65, 208, 65, color=PURPLE))
    # contact column
    b.append(f'<rect x="208" y="40" width="80" height="118" rx="8" fill="{BLUE_F}" stroke="{BLUE}" stroke-width="1.3"/>')
    b.append(label(248, 58, 'contact', fs=7.4, anchor='middle', color=BLUE))
    b.append(label(248, 68, 'column', fs=7.4, anchor='middle', color=BLUE))
    for i in range(6):
        y = 84 + i * 8
        b.append(circle(226 + (i % 3) * 14, y, 2.4, stroke=PURPLE, fill=PURPLE_F, width=0.9))
    b.append(label(248, 150, 'water + O3', fs=6.6, anchor='middle', color=BLUE))
    b.append(arrow(248, 158, 248, 178, color=GREEN))
    b.append(box(200, 178, 96, 26, 'sterile water', stroke=GREEN, fill=GREEN_F, fs=7.4))
    b.append(arrow(238, 40, 238, 26, color=GREY, head=0))
    b.append(label(226, 24, 'vent O3', fs=6.4, anchor='end', color=GREY))
    b.append(label(300, 114, 'ozone bubbles', fs=6.6, color=PURPLE))
    b.append(arrow(298, 120, 288, 120, color=PURPLE, head=3))
    n = notes(14, 218, 'Ozone is made on site from dry air by a silent electric discharge',
              'and bubbled through the water for 5–15 minutes. It kills bacteria,',
              'viruses and cysts, and leaves no residue.')
    b.append(n)
    return svg(''.join(b), n.bottom, None)


def water_sources():
    b = []
    b.append(label(180, 18, 'Sources of water', fs=9.4, anchor='middle', bold=True, color=PURPLE))
    b.append(box(12, 34, 100, 44, ['Surface', 'river, lake, canal'], stroke=BLUE, fill=BLUE_F, fs=7.4))
    b.append(box(130, 34, 100, 44, ['Ground', 'well, bore well'], stroke=ORANGE, fill=ORANGE_F, fs=7.4))
    b.append(box(248, 34, 100, 44, ['Rain / sea', 'rain water, sea'], stroke=GREEN, fill=GREEN_F, fs=7.4))
    b.append(label(62, 96, 'turbid, organic', fs=6.6, anchor='middle', color=GREY))
    b.append(label(180, 96, 'clear, hard', fs=6.6, anchor='middle', color=GREY))
    b.append(label(298, 96, 'soft / very salty', fs=6.6, anchor='middle', color=GREY))
    # ground cross-section: hill, lake basin, bore well, sea
    b.append(line(14, 152, 346, 152, color=GREY, width=1.4))
    b.append(path('M26 152 L56 112 L86 152', stroke=GREY, width=1.2))
    b.append(label(80, 116, 'hill', fs=6.4, anchor='start', color=GREY))
    b.append(f'<rect x="110" y="152" width="58" height="14" fill="{BLUE_F}" stroke="{BLUE}" stroke-width="1"/>')
    b.append(label(139, 146, 'lake', fs=6.4, anchor='middle', color=BLUE))
    b.append(f'<rect x="220" y="132" width="14" height="26" fill="{GREY_F}" stroke="{GREY}" stroke-width="1"/>')
    b.append(label(227, 128, 'bore well', fs=6.2, anchor='middle', color=GREY))
    b.append(line(196, 158, 300, 158, color=BLUE, width=1, dash='4 3'))
    b.append(label(190, 172, 'water table', fs=6.0, anchor='middle', color=BLUE))
    b.append(f'<rect x="300" y="152" width="46" height="14" fill="#DCEBF6" stroke="{BLUE}" stroke-width="1"/>')
    b.append(label(323, 146, 'sea', fs=6.4, anchor='middle', color=BLUE))
    n = notes(14, 192, 'Surface water needs the most treatment, ground water is clear but hard,',
              'rain water is soft but seasonal, and sea water needs desalination before use.')
    b.append(n)
    return svg(''.join(b), n.bottom, None)
