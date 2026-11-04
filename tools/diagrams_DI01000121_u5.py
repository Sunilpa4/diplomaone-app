"""Six compact mobile SVGs for Applied Physics (DI01000121) Unit 5: waves, acoustics, ultrasonics
and semiconductors."""
import math

from diagrams_DI01000121_u1 import (svg, text, rbox, P, ln, heading, foot,
                                   BLUE, BF, GREEN, GF, ORANGE, OF, RED, RF, PURPLE, PF,
                                   GREY, INK)
from diagrams_DI01000121_u3 import arrow

TITLES = {
    "u5_wave": "A transverse wave and a longitudinal wave",
    "u5_stationary": "Two waves add up to a stationary wave",
    "u5_reverb": "How the sound level decays in a hall",
    "u5_ultrasonic": "Hearing ranges and the SONAR echo",
    "u5_band": "Band gaps of the three classes of solid",
    "u5_doping": "Donor and acceptor levels in doped silicon",
}

TITLES_GU = {
    "u5_wave": "અનુપ્રસ્થ તરંગ અને સંગત તરંગ",
    "u5_stationary": "બે તરંગો મળીને સ્થિર તરંગ બનાવે",
    "u5_reverb": "હોલમાં ધ્વનિનું સ્તર કેવી રીતે ઘટે",
    "u5_ultrasonic": "શ્રવણ શ્રેણી અને પડઘાથી સોનાર",
    "u5_band": "ત્રણ વર્ગના ઘનનાં પટ્ટા અંતર",
    "u5_doping": "ડોપ કરેલા સિલિકોનમાં દાતા અને ગ્રાહક સ્તર",
}

CAPTIONS = {
    "u5_wave": "In a transverse wave the motion is at right angles to the wave; in a longitudinal one "
               "it is along the wave.",
    "u5_stationary": "Nodes never move and antinodes swing the most; both are fixed in space.",
    "u5_reverb": "Reverberation time is the 60 dB drop, which is why it is written T60.",
    "u5_ultrasonic": "Ultrasound is still sound: it needs a medium, and the echo gives the distance.",
    "u5_band": "No gap means a conductor, a small gap a semiconductor, a large gap an insulator.",
    "u5_doping": "A donor sits just below the conduction band, an acceptor just above the valence band.",
}

CAPTIONS_GU = {
    "u5_wave": "અનુપ્રસ્થ તરંગમાં ગતિ તરંગને લંબરૂપે, સંગત તરંગમાં તરંગની દિશામાં જ હોય.",
    "u5_stationary": "નિસ્પંદ કદી ખસતાં નથી અને પ્રસ્પંદ સૌથી વધુ દોલિત થાય; બંને અવકાશમાં સ્થિર રહે.",
    "u5_reverb": "પ્રતિધ્વનિ સમય એ 60 dB નો ઘટાડો છે, તેથી જ તેને T60 લખાય.",
    "u5_ultrasonic": "અલ્ટ્રાસાઉન્ડ પણ ધ્વનિ જ છે: માધ્યમ જોઈએ, અને પડઘો અંતર આપે.",
    "u5_band": "અંતર ન હોય તો વાહક, નાનું અંતર અર્ધવાહક, મોટું અંતર અવાહક.",
    "u5_doping": "દાતા વહન પટ્ટાના થોડું નીચે, ગ્રાહક સંયોજક પટ્ટાના થોડું ઉપર બેસે.",
}


# ------------------------------------------------------------------ 1. two kinds of wave
def wave():
    b = heading("One wave seen two ways", "transverse above, longitudinal below")
    x0, x1 = 26, 334
    axis = 104
    amp = 30

    b += ln(x0, axis, x1, axis, "#CCCCCC", 1.0)
    pts = []
    for i in range(0, 161):
        x = x0 + i * (x1 - x0) / 160.0
        y = axis - amp * math.sin(2 * math.pi * i / 80.0)
        pts.append(f"{x:.1f} {y:.1f}")
    b += f'<path d="M{"L".join(pts)}" fill="none" stroke="{BLUE}" stroke-width="2.0"/>'

    b += arrow(64, axis, 64, axis - amp + 2, GREEN, 1.0)
    b += arrow(64, axis - amp + 2, 64, axis, GREEN, 1.0)
    b += text(64, axis - amp - 8, "amplitude a", 8.2, anchor="middle", color=GREEN)

    y_lab = axis + 16
    b += arrow(x0 + 10, y_lab, x0 + 10 + 80 * (x1 - x0) / 160.0, y_lab, ORANGE, 1.0)
    b += arrow(x0 + 10 + 80 * (x1 - x0) / 160.0, y_lab, x0 + 10, y_lab, ORANGE, 1.0)
    b += text(x0 + 12, y_lab + 12, "wavelength λ", 8.4, anchor="start", color=ORANGE)

    # longitudinal: density of vertical strokes
    ly = 186
    for i in range(0, 60):
        x = x0 + 8 + i * 5.0
        s = math.sin(2 * math.pi * i / 26.0)
        gap = 2.2 + 3.4 * (0.5 + 0.5 * s)
        b += ln(x, ly - 10, x, ly + 10, GREY if s < 0 else INK, gap / 2.4)
    b += text(180, ly + 26, "compressions and rarefactions", 8.6, color=GREY)
    b += text(180, ly - 22, "longitudinal: air molecules", 8.8, color=INK)

    y = 234
    b += rbox(180, y, 336, 26, "v = f λ   ·   T = 1/f", BF, BLUE, 10.0)
    b += foot(y + 30, "Energy travels through the medium; the medium itself stays in place.")
    return svg(360, y + 52, b)


# ------------------------------------------------------------------ 2. stationary wave
def stationary():
    b = heading("Two opposite waves add up", "nodes stay still, antinodes swing")
    x0, x1 = 30, 330
    rows = ((62, 15, "wave 1", BLUE, 0.0), (104, 15, "wave 2", ORANGE, math.pi))
    for yc, amp, lab, col, ph in rows:
        pts = []
        for i in range(0, 151):
            x = x0 + i * (x1 - x0) / 150.0
            y = yc - amp * math.sin(2 * math.pi * i / 75.0 + ph)
            pts.append(f"{x:.1f} {y:.1f}")
        b += f'<path d="M{"L".join(pts)}" fill="none" stroke="{col}" stroke-width="1.6"/>'
        b += ln(x0, yc, x1, yc, "#E8E8E8", 0.8)
        b += text(x0 + 2, yc - amp - 5, lab, 8.2, anchor="start", color=col)

    # the sum: a standing wave swinging between +A and -A
    yc, amp = 168, 26
    b += ln(x0, yc, x1, yc, "#CFCFCF", 0.9)
    for sign, dash, op in ((1, None, 1.0), (-1, "4 3", 0.55)):
        pts = []
        for i in range(0, 151):
            x = x0 + i * (x1 - x0) / 150.0
            y = yc - sign * amp * math.sin(2 * math.pi * i / 75.0)
            pts.append(f"{x:.1f} {y:.1f}")
        da = f' stroke-dasharray="{dash}"' if dash else ""
        b += (f'<path d="M{"L".join(pts)}" fill="none" stroke="{PURPLE}" stroke-width="2.0" '
              f'opacity="{op}"{da}/>')
    b += text(x0 + 2, yc - amp - 10, "sum: standing wave", 8.4, anchor="start", color=PURPLE)

    # vertical swing arrows at the antinodes
    for k in (0.5, 1.5, 2.5):
        x = x0 + k * (x1 - x0) / 4.0
        b += arrow(x, yc - amp, x, yc + amp, PURPLE, 0.9)
        b += arrow(x, yc + amp, x, yc - amp, PURPLE, 0.9)
    b += text(x0 + 0.5 * (x1 - x0) / 4.0 + 12, yc + 16, "A", 8.6, weight="bold", anchor="start", color=PURPLE)

    nodes = [x0 + k * (x1 - x0) / 4.0 for k in range(5)]
    for x in nodes:
        b += f'<circle cx="{x:.1f}" cy="{yc}" r="3.0" fill="{RED}"/>'
    b += text(nodes[0], yc + 15, "N", 8.6, weight="bold", color=RED)
    b += text(nodes[1], yc + 15, "N", 8.6, weight="bold", color=RED)

    b += arrow(nodes[0], yc + 30, nodes[1], yc + 30, ORANGE, 1.0)
    b += arrow(nodes[1], yc + 30, nodes[0], yc + 30, ORANGE, 1.0)
    b += text((nodes[0] + nodes[1]) / 2, yc + 42, "λ/2 between nodes", 8.4, color=ORANGE)

    y = 236
    b += rbox(180, y, 336, 26, "steady interference needs coherent sources", GF, GREEN, 9.2)
    b += foot(y + 30, "A plucked string is a stationary wave: fixed ends can only be nodes.")
    return svg(360, y + 52, b)


# ------------------------------------------------------------------ 3. reverberation decay
def reverb():
    b = heading("Sound level after the source stops", "reverberation time = 60 dB drop")
    x0, ytop, x1, ybot = 56, 84, 330, 232
    b += arrow(x0, ybot, x1, ybot, GREY, 1.1)
    b += arrow(x0, ybot, x0, ytop, GREY, 1.1)
    b += text(x0 - 6, ytop - 6, "dB", 8.6, color=GREY)
    b += text(x1 - 20, ybot + 15, "time", 8.6, color=GREY)

    for lvl in (0, -20, -40, -60):
        y = ytop + (-lvl) * (ybot - ytop) / 60.0
        b += ln(x0 - 4, y, x1, y, "#EDEDED", 0.8)
        b += text(x0 - 8, y + 3.2, str(lvl).replace("-", "−"), 8.2, anchor="end", color=GREY)

    t60, span = 1.6, 2.0
    pts = []
    for i in range(0, 121):
        t = i * span / 120.0
        lvl = -60 * min(t / t60, 1.0)
        x = x0 + t * (x1 - x0) / span
        y = ytop + (-lvl) * (ybot - ytop) / 60.0
        pts.append(f"{x:.1f} {y:.1f}")
    b += f'<path d="M{"L".join(pts)}" fill="none" stroke="{BLUE}" stroke-width="2.1"/>'

    x60 = x0 + t60 * (x1 - x0) / span
    b += ln(x60, ytop, x60, ybot, BLUE, 0.9, dash="3 3")
    b += ln(x0, ybot - 0.5, x60, ybot - 0.5, BLUE, 0.9, dash="3 3")
    b += text(x60 + 7, ytop + 16, "T = 1.6 s", 8.6, anchor="start", color=BLUE)

    y = 272
    b += rbox(180, y, 336, 26, "T = 0.161 V / A   ·   A = Σ α S", PF, PURPLE, 9.4)
    b += foot(y + 30, "A speech hall wants about 1 s; a concert hall about 2 s.")
    return svg(360, y + 52, b)


# ------------------------------------------------------------------ 4. hearing ranges and SONAR
def ultrasonic():
    b = heading("Hearing ranges and the SONAR echo", "ultrasound is above 20 kHz")

    # frequency scale (log-ish, just a schematic three-zone bar)
    y = 84
    zones = ((24, 118, "infrasonic", "< 20 Hz", GREY, "#F2F2F2"),
             (118, 214, "audible", "20 Hz – 20 kHz", GREEN, GF),
             (214, 336, "ultrasonic", "> 20 kHz", BLUE, BF))
    for xs, xe, name, rng, col, fill in zones:
        b += f'<rect x="{xs}" y="{y}" width="{xe - xs}" height="26" fill="{fill}" stroke="{col}" stroke-width="1.0"/>'
        b += text((xs + xe) / 2, y + 11, name, 8.6, weight="bold", color=col)
        b += text((xs + xe) / 2, y + 22, rng, 7.8, color=GREY)
    b += text(180, y - 8, "frequency", 8.4, color=GREY)

    # SONAR: ship, seabed, echo path
    sy, bed = 150, 226
    b += f'<rect x="18" y="{bed}" width="324" height="14" fill="#DCE9D5"/>'
    b += ln(18, bed, 342, bed, GREEN, 1.0)
    b += text(300, bed + 12, "seabed", 8.0, color=GREEN)
    b += f'<rect x="150" y="{sy - 12}" width="58" height="12" fill="#BFC7D1" stroke="#7A8794" stroke-width="1.0"/>'
    b += text(179, sy - 18, "ship", 8.4, color=INK)
    b += arrow(179, sy, 179, bed - 4, BLUE, 1.3)
    b += arrow(196, bed - 4, 196, sy, ORANGE, 1.3)
    b += text(210, (sy + bed) / 2, "pulse down", 8.2, anchor="start", color=BLUE)
    b += text(210, (sy + bed) / 2 + 12, "echo back", 8.2, anchor="start", color=ORANGE)
    b += text(32, (sy + bed) / 2, "d = v t / 2", 9.2, anchor="start", color=INK)
    b += text(32, (sy + bed) / 2 + 14, "v ≈ 1500 m/s", 8.2, anchor="start", color=GREY)

    y = 262
    b += rbox(180, y, 336, 26, "40 kHz → λ = 8.6 mm in air, 3.7 cm in water", OF, ORANGE, 9.0)
    b += foot(y + 30, "A narrow beam and a short wavelength are what make a sharp image.")
    return svg(360, y + 52, b)


# ------------------------------------------------------------------ 5. band gaps
def band():
    b = heading("Three classes, three band gaps", "the gap decides the class")
    top, bot = 70, 196
    panels = ((22, "conductor", "no gap", BLUE, BF, 0),
              (140, "semiconductor", "1.1 eV", GREEN, GF, 16),
              (258, "insulator", "8 eV", ORANGE, OF, 40))
    for x, name, gap, col, fill, g in panels:
        w = 82
        b += text(x + w / 2, 64, name, 9.2, weight="bold", color=col)
        b += text(x + w / 2, 77, ("no gap: bands touch" if not g else gap), 8.0, color=GREY)
        vb_top = bot - 34
        b += f'<rect x="{x}" y="{vb_top}" width="{w}" height="34" fill="{fill}" stroke="{col}" stroke-width="1.0"/>'
        b += text(x + w / 2, vb_top + 20, "valence", 7.8, color=col)
        cb_bot = vb_top - g
        b += f'<rect x="{x}" y="{cb_bot - 34}" width="{w}" height="34" fill="#FFFFFF" stroke="{col}" stroke-width="1.0"/>'
        b += text(x + w / 2, cb_bot - 14, "conduction", 7.6, color=GREY)
        if g:
            b += arrow(x + w / 2, vb_top - 2, x + w / 2, cb_bot + 2, RED, 1.2)
            b += text(x + w / 2 + 12, (vb_top + cb_bot) / 2 + 3, gap, 8.0, anchor="start", color=RED)
        else:
            b += ln(x, vb_top, x + w, vb_top, RED, 1.0, dash="4 3")

    y = 236
    b += rbox(180, y, 336, 26, "silicon 1.1 eV   ·   germanium 0.7 eV   ·   diamond 5.5 eV", RF, RED, 9.0)
    b += foot(y + 30, "Heating a semiconductor lifts electrons across; a metal needs no help.")
    return svg(360, y + 52, b)


# ------------------------------------------------------------------ 6. doping
def doping():
    b = heading("Doping moves a level into the gap", "donor or acceptor")
    panels = ((22, "N type: P, As, Sb", "electrons", BLUE, BF, "donor", "below"),
              (190, "P type: B, Al, Ga", "holes", ORANGE, OF, "acceptor", "above"))
    vtop, vbot = 186, 218
    ctop, cbot = 92, 124
    for x, name, carrier, col, fill, level, where in panels:
        w = 148
        b += text(x + w / 2, 82, name, 9.0, weight="bold", color=col)
        b += f'<rect x="{x}" y="{ctop}" width="{w}" height="{cbot - ctop}" fill="#FFFFFF" stroke="{col}" stroke-width="1.0"/>'
        b += text(x + w / 2, ctop + 20, "conduction band", 7.8, color=GREY)
        b += f'<rect x="{x}" y="{vtop}" width="{w}" height="{vbot - vtop}" fill="{fill}" stroke="{col}" stroke-width="1.0"/>'
        b += text(x + w / 2, vtop + 20, "valence band", 7.8, color=col)
        ly = cbot + 22 if where == "below" else vtop - 22
        b += ln(x + 16, ly, x + w - 16, ly, RED, 1.2, dash="4 3")
        b += text(x + w - 14, ly - 5, level, 7.8, anchor="end", color=RED)
        if where == "below":
            b += arrow(x + 34, ly - 2, x + 34, ctop + 6, BLUE, 1.1)
            b += text(x + 34, ly + 12, "e⁻", 8.2, color=BLUE)
        else:
            b += arrow(x + 34, vbot - 6, x + 34, ly + 2, ORANGE, 1.1)
            b += text(x + 46, ly + 18, "h⁺", 8.2, color=ORANGE)
        b += text(x + w / 2, vbot + 15, f"majority: {carrier}", 8.2, color=col)

    y = 264
    b += rbox(180, y, 336, 26, "1 dopant atom per 10⁶ raises conductivity by orders", GF, GREEN, 9.0)
    b += foot(y + 30, "Both types stay electrically neutral; only the carrier count changes.")
    return svg(360, y + 52, b)


DIAGRAMS = {
    "u5_wave": wave,
    "u5_stationary": stationary,
    "u5_reverb": reverb,
    "u5_ultrasonic": ultrasonic,
    "u5_band": band,
    "u5_doping": doping,
}
