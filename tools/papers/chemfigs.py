"""Diagram builders shared by the hand-written solved papers."""
from svgdiag import (svg, box, label, arrow, line, circle, path, notes,
                     PURPLE, BLUE, GREEN, ORANGE, RED, GREY,
                     PURPLE_F, BLUE_F, GREEN_F, ORANGE_F, RED_F, GREY_F)


def lime_soda(cold=True):
    """Cold / hot lime-soda softener, flow top to bottom."""
    t = 'Cold lime–soda softening' if cold else 'Hot lime–soda softening'
    b = []
    # raw water inlet
    b.append(box(18, 30, 78, 30, 'Raw water', stroke=GREY, fill=GREY_F, fs=9))
    b.append(arrow(96, 45, 126, 45))
    b.append(box(126, 30, 108, 30, 'Lime + soda feed', stroke=ORANGE, fill=ORANGE_F, fs=9))
    # chemical mixer
    b.append(box(96, 76, 168, 34, ['Chemical mixer', 'with slow stirrer'], stroke=ORANGE, fill=ORANGE_F))
    b.append(arrow(180, 60, 180, 76))
    # flocculation / settling chamber
    b.append(box(40, 126, 280, 96, [], stroke=BLUE, fill=BLUE_F, radius=8))
    b.append(label(52, 143, 'Flocculation + settling tank', fs=9.5, bold=True, color=BLUE))
    b.append(label(52, 158, 'CaCO3 and Mg(OH)2 settle as sludge', fs=8.0, color='#40505f'))
    for yy in (170, 182, 194):
        b.append(line(52, yy, 300, yy, color='#b9cddf', width=1))
    b.append(label(300, 214, 'sludge', fs=8.4, anchor='end', color=GREY, italic=True))
    b.append(arrow(180, 110, 180, 126))
    # sludge draw-off
    b.append(line(180, 222, 180, 236, color=GREY))
    b.append(label(184, 248, 'sludge blow-down', fs=8.4, color=GREY))
    # filter
    b.append(box(96, 258, 168, 32, ['Pressure sand filter'], stroke=GREEN, fill=GREEN_F))
    b.append(arrow(180, 236, 180, 258))
    # soft water out
    b.append(box(74, 300, 212, 30, 'Soft water, hardness below 50 ppm', stroke=GREEN, fill=GREEN_F, fs=8.8))
    b.append(arrow(180, 290, 180, 300))
    note = ('Chemicals: Ca(OH)2 + Na2CO3. Cold process runs at 20–30 °C.'
            if cold else
            'Hot process runs at 90–110 °C: faster reaction and less sludge, but heat is needed.')
    n = notes(18, 344, note)
    b.append(n)
    return svg(''.join(b), n.bottom, t)


def zeolite():
    b = []
    b.append(label(180, 18, 'Zeolite (ion-exchange) softener', fs=9.6, anchor='middle', bold=True, color=PURPLE))
    b.append(box(18, 44, 86, 28, 'Hard water in', stroke=GREY, fill=GREY_F, fs=8.4))
    b.append(arrow(104, 58, 128, 58))
    b.append(label(20, 86, 'water carries Ca2+, Mg2+', fs=7.2, color=GREY))
    # bed vessel
    b.append(box(128, 40, 88, 150, [], stroke=PURPLE, fill='#FBF7FD', radius=10))
    b.append(label(172, 56, 'Zeolite bed', fs=8.8, anchor='middle', bold=True, color=PURPLE))
    for i, yy in enumerate(range(66, 166, 12)):
        b.append(circle(146 + (i % 4) * 16, yy, 3.2, stroke=PURPLE, fill=PURPLE_F, width=1))
        b.append(circle(154 + ((i + 2) % 4) * 16, yy + 5, 3.2, stroke=PURPLE, fill=PURPLE_F, width=1))
    b.append(label(172, 182, 'Na2O·Al2O3·nSiO2', fs=7.4, anchor='middle', color=PURPLE))
    b.append(box(128, 190, 88, 24, 'support gravel', stroke=GREY, fill=GREY_F, fs=8))
    b.append(arrow(172, 214, 172, 232))
    b.append(box(112, 232, 120, 28, 'Soft water out', stroke=GREEN, fill=GREEN_F, fs=8.8))
    # brine regeneration in at the top, waste brine out at the bottom
    b.append(box(232, 62, 106, 30, 'NaCl brine', stroke=ORANGE, fill=ORANGE_F, fs=8.6))
    b.append(arrow(232, 77, 216, 77, color=ORANGE))
    b.append(box(232, 216, 106, 26, 'Brine + CaCl2 out', stroke=ORANGE, fill=ORANGE_F, fs=8))
    b.append(arrow(216, 196, 232, 224, color=ORANGE))
    n = notes(18, 282, 'Exchange: the Ca2+ and Mg2+ of the water replace Na+ on the zeolite.',
              'Regeneration: zeolite-Ca + 2NaCl → zeolite-Na2 + CaCl2.')
    b.append(n)
    return svg(''.join(b), n.bottom, None)


def ion_exchange():
    b = []
    b.append(label(180, 18, 'Ion-exchange (demineralisation) plant', fs=9.6, anchor='middle', bold=True, color=PURPLE))
    # raw water in
    b.append(box(16, 46, 92, 26, 'Hard water in', stroke=GREY, fill=GREY_F, fs=8.6))
    b.append(arrow(108, 59, 130, 59))
    # cation resin vessel
    b.append(box(130, 34, 84, 128, [], stroke=BLUE, fill='#F4FAFF', radius=10))
    b.append(label(172, 46, 'cation resin', fs=7.6, anchor='middle', bold=True, color=BLUE))
    for yy in range(56, 152, 15):
        b.append(line(142, yy, 202, yy, color='#b9d3ea', width=2.2))
    b.append(label(178, 180, 'H+ released', fs=7.4, anchor='start', color=BLUE))
    b.append(arrow(172, 162, 172, 190))
    # anion vessel
    b.append(box(130, 190, 84, 74, [], stroke=GREEN, fill='#F6FCF7', radius=10))
    b.append(label(172, 202, 'anion resin', fs=7.6, anchor='middle', bold=True, color=GREEN))
    for yy in range(212, 258, 14):
        b.append(line(142, yy, 202, yy, color='#c3e3ca', width=2.2))
    b.append(label(178, 280, 'OH- released', fs=7.4, anchor='start', color=GREEN))
    b.append(arrow(172, 264, 172, 288))
    # demineralised water out
    b.append(box(126, 288, 92, 26, 'Demineralised water', stroke=GREEN, fill=GREEN_F, fs=7.6))
    # regeneration columns
    b.append(label(294, 44, 'Regeneration', fs=8.4, anchor='middle', bold=True, color=ORANGE))
    b.append(box(240, 54, 108, 26, 'dilute HCl / H2SO4', stroke=ORANGE, fill=ORANGE_F, fs=8))
    b.append(arrow(240, 67, 216, 67, color=ORANGE))
    b.append(box(240, 172, 108, 26, 'dilute NaOH', stroke=ORANGE, fill=ORANGE_F, fs=8))
    b.append(arrow(240, 185, 216, 185, color=ORANGE))
    b.append(box(240, 288, 108, 26, 'Ca2+, Mg2+ waste', stroke=GREY, fill=GREY_F, fs=7.8))
    b.append(line(222, 301, 240, 301, color=GREY, dash='3 3'))
    n = notes(18, 330, 'Cation exchange: 2R-H + Ca2+ → R2-Ca + 2H+.',
              'Anion exchange follows: R-OH + Cl- → R-Cl + OH-, giving demineralised water.')
    b.append(n)
    return svg(''.join(b), n.bottom, None)


def phosphate():
    b = []
    b.append(box(20, 32, 96, 30, 'Hard water +', stroke=GREY, fill=GREY_F, fs=8.8))
    b.append(box(20, 64, 96, 30, 'Na3PO4 dose', stroke=ORANGE, fill=ORANGE_F, fs=8.8))
    b.append(arrow(116, 47, 146, 47))
    b.append(arrow(116, 79, 146, 79))
    b.append(box(146, 30, 130, 66, ['Reaction / heating tank', '70–100 °C, 15–20 min'], stroke=PURPLE, fill=PURPLE_F))
    b.append(arrow(211, 96, 211, 120))
    b.append(box(126, 120, 170, 74, ['Settling tank', 'Ca3(PO4)2 and Mg3(PO4)2 sludge'], stroke=BLUE, fill=BLUE_F))
    b.append(line(211, 194, 211, 214, color=GREY))
    b.append(label(215, 226, 'sludge to disposal', fs=8.3, color=GREY))
    b.append(arrow(211, 218, 211, 238, color='#3c4655'))
    b.append(box(126, 238, 170, 30, 'Soft water, hardness ~ 5 ppm', stroke=GREEN, fill=GREEN_F, fs=8.7))
    n = notes(18, 288, '3Ca(HCO3)2 + 2Na3PO4 → Ca3(PO4)2 down + 6NaHCO3; the same pattern applies to Mg salts.',
                   'Phosphate gives very low residual hardness; it is costly, so it is used for boiler feed.')
    b.append(n)
    return svg(''.join(b), n.bottom, 'Phosphate (calgon) softening process')


def locomotive_boiler():
    b = []
    b.append(label(180, 20, 'Locomotive boiler (fire-tube)', fs=9.8, anchor='middle', bold=True, color=PURPLE))
    # shell
    b.append(f'<rect x="24" y="66" width="268" height="140" rx="16" fill="#FBF7FD" stroke="{PURPLE}" stroke-width="1.6"/>')
    # water level
    b.append(line(30, 96, 286, 96, color='#4a90c2', width=1.3, dash='5 3'))
    b.append(label(32, 92, 'water level', fs=7.6, color='#2b6c96'))
    b.append(label(150, 86, 'steam space', fs=8, anchor='middle', color=BLUE))
    # fire box
    b.append(box(38, 112, 66, 68, ['Fire box', 'grate'], stroke=RED, fill=RED_F, fs=8.2))
    b.append(label(71, 194, 'coal + air', fs=7.4, anchor='middle', color=RED))
    # combustion chamber
    b.append(box(104, 134, 62, 24, 'combustion chamber', stroke=ORANGE, fill=ORANGE_F, fs=7.2))
    # fire tubes
    for yy in (112, 124, 158, 170):
        b.append(line(166, yy, 288, yy, color='#b0899a', width=4))
    b.append(label(226, 104, 'fire tubes (hot gas)', fs=7.6, anchor='middle', color='#8c6b78'))
    # smoke box + chimney
    b.append(f'<rect x="288" y="66" width="26" height="140" fill="{GREY_F}" stroke="{GREY}" stroke-width="1.2"/>')
    b.append(label(301, 216, 'smoke', fs=7, anchor='middle', color=GREY))
    b.append(label(301, 226, 'box', fs=7, anchor='middle', color=GREY))
    b.append(f'<rect x="293" y="30" width="16" height="36" fill="{GREY_F}" stroke="{GREY}" stroke-width="1.2"/>')
    b.append(label(301, 26, 'chimney', fs=7.4, anchor='middle', color=GREY))
    # dome and safety valve on top of the shell
    b.append(box(56, 44, 44, 22, 'dome', stroke=BLUE, fill=BLUE_F, fs=7.8))
    b.append(box(200, 46, 48, 20, 'safety valve', stroke=BLUE, fill=BLUE_F, fs=6.6))
    b.append(arrow(152, 66, 152, 42, color=BLUE))
    b.append(label(146, 38, 'steam to cylinders', fs=7.2, anchor='end', color=BLUE))
    n = notes(18, 248, 'Fire-tube: hot gases pass through tubes surrounded by water, giving a high evaporation rate.',
              'It is mounted on the locomotive frame, so it must stay compact and be able to move.')
    b.append(n)
    return svg(''.join(b), n.bottom, None)


def lancashire_boiler():
    b = []
    b.append(label(180, 16, 'Lancashire boiler (two flue fire-tube)', fs=9.4, anchor='middle', bold=True, color=PURPLE))
    # shell
    b.append(f'<rect x="20" y="46" width="290" height="124" rx="50" fill="#FBF7FD" stroke="{PURPLE}" stroke-width="1.6"/>')
    b.append(line(26, 72, 304, 72, color='#4a90c2', width=1.3, dash='5 3'))
    b.append(label(34, 88, 'water level', fs=7.4, color='#2b6c96'))
    b.append(label(250, 90, 'steam space', fs=7.8, anchor='middle', color=BLUE))
    # dome + safety valve sitting on the shell
    b.append(box(112, 28, 38, 18, 'dome', stroke=BLUE, fill=BLUE_F, fs=7.4))
    b.append(box(184, 30, 56, 16, 'safety valve', stroke=BLUE, fill=BLUE_F, fs=6.6))
    # furnace and grate, inside the shell at the front end
    b.append(box(24, 104, 58, 54, ['grate', 'furnace'], stroke=RED, fill=RED_F, fs=7.8))
    b.append(label(53, 187, 'coal + air', fs=7, anchor='middle', color=RED))
    # two internal flues
    b.append(box(96, 100, 106, 22, '1st flue (hot gas)', stroke=ORANGE, fill=ORANGE_F, fs=7.6))
    b.append(box(96, 138, 106, 22, '2nd flue (return gas)', stroke=ORANGE, fill=ORANGE_F, fs=7.4))
    b.append(arrow(82, 111, 96, 111, color=ORANGE))
    b.append(arrow(202, 111, 224, 111, color=ORANGE))
    b.append(path('M224 111 C 240 111 240 149 224 149', stroke=ORANGE, width=1.4))
    b.append(arrow(224, 149, 206, 149, color=ORANGE))
    # smoke box + chimney at the back
    b.append(box(312, 96, 26, 64, [], stroke=GREY, fill=GREY_F))
    b.append(label(325, 176, 'smoke', fs=6.8, anchor='middle', color=GREY))
    b.append(label(325, 185, 'box', fs=6.8, anchor='middle', color=GREY))
    b.append(f'<rect x="318" y="50" width="14" height="46" fill="{GREY_F}" stroke="{GREY}" stroke-width="1.2"/>')
    b.append(label(325, 44, 'chimney', fs=7, anchor='middle', color=GREY))
    b.append(arrow(304, 120, 312, 120, color=GREY))
    # feed water in, blow-down out
    b.append(arrow(278, 30, 278, 48, color=GREEN))
    b.append(label(272, 28, 'feed water', fs=7.2, anchor='end', color=GREEN))
    b.append(line(210, 170, 210, 186, color=GREY))
    b.append(label(214, 187, 'blow-down', fs=7.2, color=GREY))
    n = notes(18, 206, 'Two large internal flues double the heating surface of a plain shell.',
              'It needs a large brick setting; used for steady steam demand, not for a moving plant.')
    b.append(n)
    return svg(''.join(b), n.bottom, None)


def vapour_compression():
    b = []
    b.append(label(180, 22, 'Vapour-compression refrigeration cycle', fs=9.6, anchor='middle', bold=True, color=PURPLE))
    b.append(box(26, 44, 128, 40, ['Compressor', 'low P vapour → high P vapour'], stroke=BLUE, fill=BLUE_F, fs=8.4))
    b.append(box(206, 44, 128, 40, ['Condenser', 'high P vapour → liquid'], stroke=ORANGE, fill=ORANGE_F, fs=8.4))
    b.append(box(206, 150, 128, 40, ['Expansion valve', 'liquid → low P mixture'], stroke=PURPLE, fill=PURPLE_F, fs=8.4))
    b.append(box(26, 150, 128, 40, ['Evaporator', 'liquid → vapour, absorbs heat'], stroke=GREEN, fill=GREEN_F, fs=8.4))
    b.append(arrow(154, 64, 206, 64, color=BLUE))
    b.append(label(180, 58, '2 → 3', fs=8, anchor='middle', color=BLUE))
    b.append(arrow(270, 84, 270, 150, color=ORANGE))
    b.append(label(276, 120, '3 → 4', fs=8, color=ORANGE))
    b.append(arrow(206, 170, 154, 170, color=PURPLE))
    b.append(label(180, 164, '4 → 1', fs=8, anchor='middle', color=PURPLE))
    b.append(arrow(90, 150, 90, 84, color=GREEN))
    b.append(label(96, 120, '1 → 2', fs=8, color=GREEN))
    n = notes(18, 206, 'Work input W at the compressor; heat rejected QH at the condenser; heat absorbed QL at the evaporator.',
                   'Coefficient of performance, COP = QL / W.')
    b.append(n)
    return svg(''.join(b), n.bottom, None)


def air_compressor_reciprocating():
    b = []
    b.append(label(180, 22, 'Single-stage reciprocating air compressor', fs=9.6, anchor='middle', bold=True, color=PURPLE))
    # cylinder
    b.append(f'<rect x="118" y="46" width="124" height="120" rx="6" fill="#F4FAFF" stroke="{BLUE}" stroke-width="1.6"/>')
    b.append(label(180, 76, 'cylinder', fs=8.6, anchor='middle', color=BLUE))
    # piston
    b.append(f'<rect x="126" y="120" width="108" height="16" fill="{BLUE_F}" stroke="{BLUE}" stroke-width="1.4"/>')
    b.append(label(180, 132, 'piston', fs=8, anchor='middle', color=BLUE))
    # rod + crank
    b.append(line(180, 136, 180, 190, color=GREY, width=3))
    b.append(circle(180, 200, 14, stroke=GREY, fill=GREY_F))
    b.append(label(180, 232, 'crank + connecting rod', fs=8, anchor='middle', color=GREY))
    # valves
    b.append(box(96, 46, 40, 26, ['suction', 'valve'], stroke=GREEN, fill=GREEN_F, fs=7.6))
    b.append(arrow(60, 59, 96, 59, color=GREEN, head=0))
    b.append(label(18, 55, 'air in', fs=7.8, color=GREEN))
    b.append(box(224, 46, 40, 26, ['delivery', 'valve'], stroke=ORANGE, fill=ORANGE_F, fs=7.6))
    b.append(arrow(264, 59, 306, 59, color=ORANGE, head=0))
    b.append(label(308, 55, 'to', fs=7.8, color=ORANGE))
    b.append(label(308, 68, 'receiver', fs=7.8, color=ORANGE))
    # cooling fins hint
    for yy in range(86, 118, 8):
        b.append(line(124, yy, 236, yy, color='#cfe0ef', width=1))
    n = notes(18, 246, 'Suction stroke: the piston moves down, the inlet valve opens, and air at P1 fills the cylinder.',
                   'Compression and delivery: both valves shut, the air is compressed, then pushed out at P2.',
                   'Clearance volume is kept small because it lowers the volumetric efficiency.')
    b.append(n)
    return svg(''.join(b), n.bottom, None)


def ice_plant():
    b = []
    b.append(label(180, 22, 'Ice refrigeration (ice plant)', fs=9.6, anchor='middle', bold=True, color=PURPLE))
    b.append(box(26, 44, 150, 46, ['Refrigeration unit', 'compressor, condenser, coil'], stroke=BLUE, fill=BLUE_F, fs=8.2))
    b.append(box(30, 108, 122, 62, ['Brine tank', 'CaCl2 brine at −10 °C'], stroke=PURPLE, fill=PURPLE_F, fs=8.4))
    b.append(box(186, 108, 148, 62, ['Ice cans in brine', 'water freezes to ice'], stroke=GREEN, fill=GREEN_F, fs=8.4))
    b.append(arrow(91, 90, 91, 108, color=BLUE))
    b.append(label(96, 103, 'cooling coil', fs=7.6, color=BLUE))
    b.append(arrow(152, 132, 186, 132, color=GREEN))
    b.append(label(169, 127, 'cold', fs=7.6, anchor='middle', color=GREEN))
    b.append(arrow(186, 158, 152, 158, color=ORANGE))
    b.append(label(169, 172, 'warm', fs=7.6, anchor='middle', color=ORANGE))
    b.append(box(186, 192, 148, 30, 'Ice blocks to storage', stroke=GREY, fill=GREY_F, fs=8.2))
    b.append(arrow(260, 170, 260, 192, color=GREY))
    b.append(box(30, 192, 122, 30, 'Brine pump', stroke=PURPLE, fill=PURPLE_F, fs=8.2))
    n = notes(18, 250, 'Ice stores latent heat of fusion: 1 kg of ice absorbs about 334 kJ while melting.',
                   'Cheap and simple, but bulky, needs handling of ice, and gives no temperature control.')
    b.append(n)
    return svg(''.join(b), n.bottom, None)


def uv_sterilizer():
    b = []
    b.append(label(180, 20, 'UV sterilisation of water', fs=9.6, anchor='middle', bold=True, color=PURPLE))
    b.append(box(12, 48, 82, 28, 'Filtered water', stroke=GREY, fill=GREY_F, fs=8.2))
    b.append(arrow(94, 62, 108, 62))
    b.append(f'<rect x="108" y="40" width="124" height="44" rx="8" fill="#F7F3FB" stroke="{PURPLE}" stroke-width="1.4"/>')
    b.append(label(170, 58, 'UV chamber', fs=8.2, anchor='middle', color=PURPLE))
    b.append(label(170, 72, '(stainless steel)', fs=7.4, anchor='middle', color=PURPLE))
    b.append(arrow(232, 62, 248, 62, color=GREEN))
    b.append(box(248, 44, 98, 36, ['Sterile water', 'no chemical residue'], stroke=GREEN, fill=GREEN_F, fs=7.8))
    # lamp under the chamber with its rays going up
    b.append(box(120, 104, 100, 26, 'UV lamp 254 nm', stroke=PURPLE, fill=PURPLE_F, fs=8.2))
    b.append(arrow(170, 104, 170, 86, color=PURPLE))
    for x in range(126, 214, 14):
        b.append(line(x, 104, x + 10, 90, color='#b294c4', width=1))
    b.append(label(170, 146, 'quartz sleeve protects the lamp', fs=7.4, anchor='middle', color=GREY))
    n = notes(18, 172, 'UV light damages the DNA of bacteria, viruses and spores, so they cannot multiply.',
              'Contact time is only a few seconds; the water must be clear, because turbidity shields microbes.',
              'Green technique: no chlorine, no taste, no harmful by-product; only electricity is used.')
    b.append(n)
    return svg(''.join(b), n.bottom, None)


def water_softening_summary():
    b = []
    b.append(label(180, 20, 'Hardness and softening methods', fs=9.6, anchor='middle', bold=True, color=PURPLE))
    b.append(box(110, 34, 140, 26, 'Hard water (Ca2+, Mg2+)', stroke='#8c6b78', fill='#FBF1F4', fs=8.8))
    cols = [
        ('Boiling / lime-soda', 'precipitates carbonate hardness', ORANGE, ORANGE_F),
        ('Zeolite', 'ion exchange on Na-zeolite', PURPLE, PURPLE_F),
        ('Ion exchange', 'H+ and OH− resins, DM water', BLUE, BLUE_F),
        ('Phosphate', 'very low residual hardness', GREEN, GREEN_F),
    ]
    y = 78
    for name, note, c, f in cols:
        b.append(box(18, y, 150, 34, name, stroke=c, fill=f, fs=8.4))
        b.append(arrow(168, y + 17, 186, y + 17))
        b.append(label(190, y + 13, note, fs=8, color=GREY))
        b.append(line(126, 60, 126, 78, color='#c9bcc4', dash='3 3'))
        y += 46
    n = notes(18, y + 14, 'Carbonate hardness is removed by boiling; non-carbonate hardness needs soda, zeolite or resin.')
    b.append(n)
    return svg(''.join(b), n.bottom, None)
