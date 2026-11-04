# -*- coding: utf-8 -*-
"""Real-type diagrams: Unit 1 (4) + Unit 2 (5)."""
from equip_lib import *

def ref1_trap():
    b = ""
    # strata bands with anticline arch
    b += path("M8,96 Q180,26 352,96 L352,124 Q180,54 8,124 Z", "#C7CED6", "#8A97A5", 1.2)          # cap rock
    b += path("M8,124 Q180,54 352,124 L352,152 Q180,82 8,152 Z", "#F6E3B4", "#C9A44C", 1.2)          # reservoir top (gas)
    b += path("M8,140 Q180,72 352,140 L352,168 Q180,100 8,168 Z", "#F9C6CF", "#BD2543", 1.0)          # gas zone tint
    b += path("M8,152 Q180,84 352,152 L352,182 Q180,114 8,182 Z", "#4C5B4C", "#33402F", 1.0)          # oil zone
    b += path("M8,182 Q180,114 352,182 L352,206 Q180,138 8,206 Z", "#BCD9F7", "#1565C0", 1.0)         # water zone
    b += path("M8,206 Q180,138 352,206 L352,238 Q180,170 8,238 Z", "#8D6E63", "#5D4037", 1.2)          # source rock
    b += rect(8, 238, 344, 26, "#E4E0D8", "#A8A29A", 1.0, 0)
    # well bore
    b += line(180, 40, 180, 108, INK, 2.2) + line(174, 40, 174, 100, INK, 1.0) + line(186, 40, 186, 100, INK, 1.0)
    b += t(192, 46, "producing well", 8.5, INK, True, "start")
    # labels
    b += lbl(14, 76, "cap rock — impermeable shale", "start", 8.5) + leader(105, 80, 120, 66)
    b += lbl(238, 128, "gas cap", "start", 8.5, GAS, True) + leader(236, 130, 205, 122)
    b += lbl(246, 158, "oil", "start", 8.5, "#33402F", True) + leader(244, 160, 215, 150)
    b += lbl(240, 182, "water", "start", 8.5, WAT, True) + leader(238, 184, 210, 172)
    b += lbl(14, 134, "porous reservoir", "start", 8) + lbl(14, 145, "rock (sandstone)", "start", 8)
    b += lbl(14, 224, "source rock (organic-rich)", "start", 8.5) + leader(120, 220, 140, 210)
    b += lbl(14, 256, "older basement rock", "start", 8)
    b += note(180, 284, "Oil formed in source rock migrates up until the cap rock traps it")
    return svg_doc("How oil is trapped underground", "Anticline trap: gas over oil over water", 292, b)

def _hex(cx, cy, r, fill="#FFFFFF", stroke=STEEL):
    import math
    pts = " ".join(f"{cx + r * math.cos(math.radians(60 * i - 30)):.1f},{cy + r * math.sin(math.radians(60 * i - 30)):.1f}" for i in range(6))
    return f'<polygon points="{pts}" fill="{fill}" stroke="{stroke}" stroke-width="1.6"/>'

def ref1_families():
    b = ""
    panels = [(12, 46), (184, 46), (12, 196), (184, 196)]
    titles = [("Paraffins  CₙH₂ₙ₊₂", "straight / branched chains — petrol, LPG"), 
              ("Naphthenes  CₙH₂ₙ", "saturated rings — stable, in most crudes"),
              ("Aromatics", "benzene rings — high octane, solvents"),
              ("Resins &amp; asphaltenes", "big fused-ring sheets — residue, bitumen")]
    for (x, y), (ti, de) in zip(panels, titles):
        b += rect(x, y, 164, 138, "#FBFAFF", "#C9BCE0", 1.1, 6)
        b += t(x + 82, y + 16, ti, 9.5, PUR, True)
        b += t(x + 82, y + 128, de, 7.3, "#555555")
    # paraffin zigzag
    pts = [(30, 120), (52, 100), (74, 120), (96, 100), (118, 120), (140, 100), (158, 112)]
    b += pipe(pts, STEEL, 2.2, None, "ahB", arrow=False)
    b += t(30, 132, "CH₃", 8, STEEL, True) + t(160, 124, "CH₃", 8, STEEL, True)
    b += t(94, 88, "chain of C–C single bonds", 7.5, GRAY)
    # naphthene ring
    b += _hex(266, 108, 30, "#EFF6EE", CAT)
    b += t(266, 88, "ring", 7.5, GRAY) + t(266, 112, "C", 9, CAT, True)
    # aromatic ring with circle
    b += _hex(94, 258, 30, "#FFF6EC", HOT) + circ(94, 258, 17, "none", HOT, 1.4)
    b += t(94, 262, "π", 11, HOT, True)
    # asphaltene fused rings
    b += _hex(250, 248, 20, "#F3E5F5", PUR) + _hex(284, 248, 20, "#F3E5F5", PUR) + _hex(267, 276, 20, "#E7D8F5", PUR)
    b += t(322, 240, "S, N, O", 7.5, PUR, True) + t(214, 292, "", 7)
    b += t(267, 252, "fused", 7, PUR, True)
    return svg_doc("The four hydrocarbon families in crude", "Same elements — different structures, different products", 344, b)

def ref1_refinery_block():
    b = ""
    # row 1 equipment
    b += h_vessel(10, 96, 44, 26) + t(32, 88, "crude", 8, STEEL, True) + t(32, 132, "storage", 7.5, GRAY)
    b += pipe([(54, 109), (66, 109)])
    b += h_vessel(66, 92, 58, 34) + t(95, 84, "desalter", 8, STEEL, True)
    b += pipe([(124, 109), (136, 109)])
    b += furnace(136, 74, 46, 62) + t(159, 66, "pipe-still", 8, HOT, True) + t(159, 148, "heater", 7.5, GRAY)
    b += pipe([(182, 105), (194, 120)])
    b += column(196, 52, 36, 96, 6) + t(214, 44, "ADU", 9, STEEL, True)
    b += pipe([(214, 155), (214, 168), (244, 168)])
    b += furnace(244, 140, 40, 44) + t(264, 132, "vacuum heater", 7.5, HOT, True)
    b += pipe([(284, 162), (296, 150)])
    b += column(298, 66, 38, 92, 4) + t(317, 58, "VDU", 9, STEEL, True)
    # products from ADU top/side
    b += pipe([(214, 52), (214, 40)], marker="ahG")
    b += t(248, 202, "ADU light products (gas–diesel) → finishing", 7.5, CAT, True)
    b += lbl(180, 162, "atmospheric residue", "end", 7.5, GRAY)
    # VDU outs
    b += pipe([(336, 84), (348, 84)], marker="ahG") + lbl(350, 80, "VGO", "end", 7.5, CAT, True)
    b += pipe([(317, 165), (317, 178)], marker="ahR") + lbl(352, 190, "vacuum residue ↓", "end", 7.5, GAS, True)
    # row 2 conversion
    b += rect(20, 216, 320, 66, "#FBFAFF", "#C9BCE0", 1.1, 6)
    b += t(180, 232, "CONVERSION &amp; TREATING (Units III–IV)", 8.5, PUR, True)
    b += v_reactor(40, 240, 30, 34, (), "#FDF6EC", HOT) + t(55, 284 - 96 + 96, "", 7)
    b += t(55, 268 + 14, "FCC / coker", 7.3, HOT, True)
    b += sphere(140, 256, 15) + t(140, 282, "reformer", 7.3, HOT, True)
    b += v_reactor(205, 240, 30, 34, ((("HDS", 0.5)),), "#FDF6EC", HOT) + t(220, 282, "hydrotreater", 7.3, HOT, True)
    b += h_vessel(268, 244, 52, 24, CAT_F, CAT) + t(294, 282, "blending", 7.3, CAT, True)
    b += pipe([(70, 257), (120, 257)]) + pipe([(158, 257), (202, 257)]) + pipe([(236, 257), (266, 257)])
    b += note(180, 306, "Distillation separates (Unit II) — conversion units then change the molecules")
    return svg_doc("Inside a modern refinery", "Separation first, then conversion and treating", 314, b)

def ref1_product_slate():
    rows = [("LPG", -20, 40, GAS), ("Petrol (gasoline)", 30, 180, "#E8873A"), ("Kerosene / ATF", 150, 275, "#E3B505"),
            ("Diesel (HSD)", 200, 360, CAT), ("Vacuum gas oil", 360, 540, WAT), ("Residue / bitumen", 540, 620, "#5D4037")]
    b = ""
    x0, x1 = 118, 348  # 0..620 degC
    def X(temp): return x0 + (temp + 20) / 640 * (x1 - x0)
    b += line(x0, 44, x0, 268, GRAY, 1.0) 
    for temp in (0, 100, 200, 300, 400, 500, 600):
        b += line(X(temp), 262, X(temp), 268, GRAY, 1.0) + t(X(temp), 280, str(temp), 7.5, GRAY)
    b += t(233, 294, "boiling range, °C  (approximate, overlapping cuts)", 8, GRAY)
    y = 58
    for name, lo, hi, c in rows:
        b += lbl(112, y + 12, name, "end", 8.5, INK, True)
        b += rect(X(lo), y, max(X(hi) - X(lo), 5), 15, c, c, 0, 2)
        if lo < 0:
            b += lbl(X(hi) + 4, y + 12, "below 40 °C", "start", 7.8, c, True)
        elif hi >= 620:
            b += lbl(X(lo) - 4, y + 12, ">540 °C", "end", 7.8, c, True)
        elif X(hi) + 52 > 356:
            b += lbl(X(hi) - 4, y + 12, f"{lo}–{hi} °C", "end", 7.8, "#FFFFFF", True)
        else:
            b += lbl(X(hi) + 4, y + 12, f"{lo}–{hi} °C", "start", 7.8, c, True)
        y += 33
    b += note(180, 268 + 44, "Lighter products boil first — the basis of fractionation in Unit II")
    return svg_doc("One barrel, many products", "Products in order of boiling range", 322, b)

def ref2_desalter():
    b = ""
    b += t(52, 66, "transformer", 8, STEEL, True) + rect(30, 72, 46, 20, "#EFF3F9", STEEL, 1.3, 2)
    b += line(46, 92, 46, 108, STEEL, 1.2) + line(62, 92, 62, 108, STEEL, 1.2)
    b += pipe([(8, 138), (38, 138)], marker="ahB")
    b += h_vessel(38, 108, 262, 78)
    # water layer
    b += path("M52,164 H286 A14,14 0 0 1 272,180 H66 A14,14 0 0 1 52,164 Z", "#BCD9F7", WAT, 0.8)
    # electrodes: grids hanging
    for gx in (110, 150, 190):
        b += line(gx, 110, gx, 148, GAS, 1.6) + line(gx + 8, 110, gx + 8, 148, GAS, 1.6)
        b += line(gx, 118, gx + 8, 118, GAS, 1.0) + line(gx, 130, gx + 8, 130, GAS, 1.0) + line(gx, 142, gx + 8, 142, GAS, 1.0)
    b += line(46, 104, 194, 104, GAS, 1.0, "3,3")
    b += lbl(200, 100, "electrode grids (high-voltage field)", "middle", 8, GAS, True)
    b += t(96, 160, "droplets join &amp; settle", 7.8, "#7A4A21")
    b += pipe([(300, 122), (330, 122), (330, 104)], marker="ahG")
    b += lbl(334, 94, "desalted crude → ADU", "end", 8.5, CAT, True)
    b += lbl(6, 128, "crude + wash water in", "start", 8, WAT, True)
    b += line(250, 186, 250, 206, WAT, 1.6) + pipe([(250, 206), (250, 214)], marker="ahB")
    b += lbl(256, 202, "brine + mud out", "start", 8.5, WAT, True)
    b += lbl(60, 178, "water layer", "start", 7.8, WAT, True)
    b += note(180, 246, "Electric field makes tiny salty water droplets merge so they can settle out")
    return svg_doc("Electrostatic desalter / dehydrator", "Card 2.1(a): parts numbered as in the text", 254, b)

def ref2_heater():
    b = ""
    b += rect(160, 44, 22, 26, "#E8E2D9", GRAY, 1.3, 1) + t(190, 40, "stack", 8, GRAY, True, "start")
    b += pipe([(171, 44), (171, 34)], marker="ahO")
    b += furnace(92, 70, 176, 190)
    b += rect(92, 70, 176, 62, "#F3E7FB", PUR, 1.2, 0)
    b += t(180, 84, "CONVECTION section", 8, PUR, True) + t(180, 96, "flue gas heats incoming crude", 7.3, GRAY)
    b += t(180, 150, "RADIANT section", 8, HOT, True) + t(180, 162, "flame heat, hottest tubes", 7.3, GRAY)
    for gx in (106, 254):  # radiant wall tubes
        for i in range(6):
            b += line(gx, 140 + i * 18, gx + (8 if gx < 180 else -8), 140 + i * 18 + 12, HOT, 1.6)
    # crude path
    b += pipe([(8, 104), (92, 104)], marker="ahB") + lbl(6, 94, "cold crude in", "start", 8.5, WAT, True)
    b += pipe([(268, 110), (286, 110), (286, 218), (268, 218)], marker="ahO")
    b += pipe([(268, 232), (330, 232)], marker="ahR") + lbl(332, 224, "hot crude out", "end", 8.5, GAS, True) + lbl(332, 238, "to ADU flash zone", "end", 7.8, GAS)
    b += pipe([(94, 106), (250, 106), (250, 120), (112, 120)], STEEL, 1.3, None, "ahB", arrow=False)
    b += pipe([(112, 148), (112, 232), (128, 148), (146, 232), (162, 148), (180, 232), (196, 148), (214, 232), (230, 148), (246, 226)], HOT, 1.3, None, "ahO", arrow=False)
    b += lbl(96, 276, "burners: fuel gas / oil", "start", 8, HOT) + leader(150, 262, 150, 254)
    b += lbl(196, 52, "flue gas", "start", 7.8, GRAY)
    b += note(180, 300, "Coldest crude meets coolest gas first — heat is recovered, not wasted")
    return svg_doc("Pipe-still heater (furnace)", "Card 2.1(b): convection first, then radiant", 308, b)

def _side_stripper(x, y, label, color):
    b = column(x, y, 20, 40, 3)
    b += pipe([(x + 10, y + 40 + 7), (x + 10, y + 54)], marker="ahG")
    b += t(x + 10, y + 66, label, 7.3, color, True)
    return b

def ref2_adu():
    b = ""
    b += column(150, 58, 52, 252, 9)
    b += t(176, 50, "ADU column", 9, STEEL, True)
    # overhead
    b += pipe([(176, 58), (176, 44), (238, 44)], marker="ahB")
    b += exch(238, 34, 36, 20) + t(250, 64, "condenser", 7, CAT, True, "end")
    b += h_vessel(282, 32, 52, 24) + t(308, 66, "reflux drum", 7.5, GRAY)
    b += pipe([(334, 40), (350, 40)], marker="ahG") + lbl(352, 34, "gas+LPG", "end", 7.5, CAT, True)
    b += pipe([(290, 56), (290, 66), (202, 66)], marker="ahB")  # reflux return (approx to top)
    b += lbl(232, 82, "reflux", "end", 7.3, WAT)
    # side draws + strippers
    draws = [(104, "naphtha"), (170, "kerosene"), (236, "diesel")]
    for dy, name in draws:
        b += pipe([(202, dy), (238, dy)], marker="ahG")
        b += _side_stripper(238, dy - 8, name, CAT)
    # feed
    b += pipe([(8, 262), (150, 262)], marker="ahR")
    b += lbl(6, 252, "heated crude in", "start", 8.5, GAS, True) + lbl(6, 278, "(from pipe-still heater)", "start", 7.5, GRAY)
    b += t(176, 252, "flash zone", 7.5, GAS, True)
    # bottoms
    b += pipe([(176, 317), (176, 336)], marker="ahR")
    b += lbl(182, 332, "atmospheric residue → VDU", "start", 8.5, GAS, True)
    b += pipe([(120, 336), (150, 322)], marker="ahB") + lbl(118, 344, "stripping steam", "end", 7.8, WAT)
    # temperature gradient
    b += pipe([(128, 300), (128, 84)], marker="ahB")
    b += t(118, 200, "hotter below, cooler above", 7.8, WAT, style_rotate := True) if False else t(60, 200, "", 7)
    b += lbl(124, 74, "cool top", "end", 7.8, WAT) + lbl(124, 306, "hot bottom", "end", 7.8, GAS)
    b += note(180, 372, "One column, many boiling ranges: each tray is cooler than the one below")
    return svg_doc("Atmospheric distillation unit (ADU)", "Card 2.2: side draws take off the products", 380, b)

def ref2_vdu():
    b = ""
    b += furnace(16, 196, 52, 66) + t(42, 188, "vacuum", 7.8, HOT, True) + t(42, 274, "heater", 7.5, GRAY)
    b += pipe([(68, 226), (128, 226)], marker="ahR")
    b += column(128, 84, 96, 216, 5)
    b += t(176, 106, "VDU column", 9, STEEL, True) + t(176, 120, "(wide: vapour volume is large)", 7, GRAY)
    # vacuum top
    b += pipe([(176, 84), (176, 62), (238, 62)], marker="ahB")
    b += path("M238,54 L262,62 L238,70 Z", "#DCE9F5", STEEL, 1.3) + path("M268,54 L292,62 L268,70 Z", "#DCE9F5", STEEL, 1.3)
    b += t(265, 46, "steam-jet ejectors", 8, STEEL, True)
    b += rect(298, 50, 44, 24, "#EFF3F9", STEEL, 1.2, 2) + t(320, 65, "condenser", 6.6, STEEL, True)
    b += t(320, 86, "vacuum held here", 7.3, GRAY)
    b += t(176, 134, "vacuum gas oil draws", 7.3, CAT, True)
    b += pipe([(224, 140), (262, 140)], marker="ahG") + lbl(266, 136, "LVGO", "start", 8, CAT, True)
    b += pipe([(224, 196), (262, 196)], marker="ahG") + lbl(266, 192, "HVGO / lube cuts", "start", 8, CAT, True)
    b += lbl(266, 206, "→ FCC / lube plant", "start", 7.3, GRAY)
    b += t(176, 216, "flash zone", 7.5, GAS, True)
    b += pipe([(176, 307), (176, 330)], marker="ahR")
    b += lbl(182, 326, "vacuum residue → bitumen / coker", "start", 8.5, GAS, True)
    b += note(180, 356, "Low pressure lowers boiling points, so heavy oil vaporises without cracking")
    return svg_doc("Vacuum distillation unit (VDU)", "Card 2.3: distillation continues under vacuum", 364, b)

def ref2_tests():
    b = ""
    panels = [(10, 44, "Flash &amp; fire point", "Pensky–Martens closed cup", "petrol, diesel, kerosene safety"),
              (186, 44, "Viscosity", "Redwood viscometer", "lube oil flow quality"),
              (10, 208, "Cloud &amp; pour point", "test jar in cooling bath", "diesel &amp; lube cold behaviour"),
              (186, 208, "Grease consistency", "cone penetrometer", "grease grade (NLGI)")]
    for x, y, ti, ap, de in panels:
        b += rect(x, y, 164, 150, "#FBFAFF", "#C9BCE0", 1.1, 6)
        b += t(x + 82, y + 15, ti, 9, PUR, True) + t(x + 82, y + 29, ap, 7.5, GRAY)
        b += t(x + 82, y + 140, de, 7.3, "#555555")
    # Pensky: cup with lid, stirrer, thermometer
    x, y = 10, 44
    b += path(f"M{x + 52},{y + 66} H{x + 112} L{x + 104},{y + 104} H{x + 60} Z", "#FDEBD7", HOT, 1.5)
    b += rect(x + 48, y + 58, 68, 8, "#C9D6E4", STEEL, 1.2, 1)
    b += line(x + 92, y + 36, x + 92, y + 62, STEEL, 1.4) + circ(x + 92, y + 34, 4, "#fff", STEEL, 1.2)
    b += line(x + 66, y + 44, x + 66, y + 80, GAS, 1.4) + t(x + 70, y + 42, "thermometer", 6.5, GAS, False, "start")
    b += path(f"M{x + 76},{y + 118} l5,-9 l5,9 Z", "#F4A259", HOT, 0.8) + t(x + 82, y + 128, "heater", 7, HOT)
    # Redwood: bath + cup + jet + flask
    x = 186
    b += rect(x + 42, y + 44, 80, 52, "#E3F2FD", WAT, 1.5, 2)
    b += rect(x + 62, y + 52, 40, 26, "#FDEBD7", HOT, 1.3, 1)
    b += path(f"M{x + 78},{y + 78} h8 l-4,10 Z", "#FDEBD7", HOT, 1.2)
    b += path(f"M{x + 72},{y + 122} h20 l-4,-16 h-12 Z", "#EFF6EE", CAT, 1.3)
    b += t(x + 82, y + 108, "timed flow", 7, CAT) + t(x + 82, y + 62 + 66, "", 7)
    b += line(x + 116, y + 38, x + 116, y + 66, GAS, 1.3)
    # cloud/pour jar in bath
    x, y = 10, 208
    b += rect(x + 44, y + 52, 76, 56, "#E3F2FD", WAT, 1.5, 2)
    b += rect(x + 70, y + 40, 24, 62, "#FFF8E7", HOT, 1.4, 1)
    b += path(f"M{x + 70},{y + 78} h24 v24 h-24 Z", "#D8C690", HOT, 0.9)
    b += line(x + 82, y + 30, x + 82, y + 58, GAS, 1.4)
    b += t(x + 82, y + 122, "cool &amp; tilt to check flow", 7, WAT)
    # penetrometer: cone over cup
    x = 186
    b += rect(x + 30, y + 48, 8, 54, "#C9D6E4", STEEL, 1.1, 1) + rect(x + 100, y + 48, 8, 54, "#C9D6E4", STEEL, 1.1, 1)
    b += rect(x + 28, y + 44, 84, 8, "#C9D6E4", STEEL, 1.1, 1)
    b += circ(x + 70, y + 42, 10, "#fff", STEEL, 1.3) + line(x + 70, y + 42, x + 76, y + 36, GAS, 1.2)
    b += path(f"M{x + 58},{y + 62} h24 l-12,22 Z", "#F3E5F5", PUR, 1.5)
    b += line(x + 70, y + 52, x + 70, y + 62, PUR, 1.4)
    b += rect(x + 52, y + 104, 36, 15, "#FDEBD7", HOT, 1.4, 1)
    b += t(x + 70, y + 132, "cone sinks in 5 s", 7, PUR)
    return svg_doc("Product tests at a glance", "Card 2.4: each product is guarded by its apparatus test", 402, b)

D = {
 "ref1_trap": ref1_trap(), "ref1_families": ref1_families(), "ref1_refinery_block": ref1_refinery_block(),
 "ref1_product_slate": ref1_product_slate(),
 "ref2_desalter": ref2_desalter(), "ref2_heater": ref2_heater(), "ref2_adu": ref2_adu(),
 "ref2_vdu": ref2_vdu(), "ref2_tests": ref2_tests(),
}
