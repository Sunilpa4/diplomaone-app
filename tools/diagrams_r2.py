# -*- coding: utf-8 -*-
"""Real-type diagrams: Unit 3 (4) + Unit 4 (5)."""
from equip_lib import *

def _cyclone(cx, cy):
    return circ(cx, cy, 9, "#FFFFFF", STEEL, 1.2) + path(f"M{cx - 6},{cy + 7} L{cx},{cy + 18} L{cx + 6},{cy + 7}", "none", STEEL, 1.1)

def ref3_fcc():
    b = ""
    # Reactor (left)
    b += v_reactor(88, 84, 74, 128, (), STEEL_F, STEEL)
    b += _cyclone(112, 108) + _cyclone(140, 108)
    b += rect(94, 168, 62, 34, "#EAF1F9", STEEL, 1.0, 2) + t(125, 182, "stripper", 7.5, STEEL, True) + t(125, 193, "(steam)", 6.8, GRAY)
    b += t(125, 76, "REACTOR", 9, STEEL, True)
    # Regenerator (right)
    b += v_reactor(216, 72, 84, 150, (), "#FDECEF", GAS)
    b += rect(220, 168, 76, 46, "#F6C9D2", GAS, 0.8, 2) + t(258, 195, "coke burns", 7.5, GAS, True)
    b += _cyclone(240, 98) + _cyclone(272, 98)
    b += t(258, 62, "REGENERATOR", 9, GAS, True)
    # Riser
    b += pipe([(54, 318), (54, 226), (88, 226)], marker="ahO")
    b += t(46, 250, "riser", 8, HOT, True)
    b += pipe([(8, 318), (54, 318)], marker="ahB")
    b += lbl(6, 306, "feed oil +", "start", 8.5, WAT, True) + lbl(6, 332, "hot catalyst", "start", 8, HOT, True)
    # product vapour out
    b += pipe([(125, 84), (125, 58), (196, 58)], marker="ahG")
    b += lbl(8, 52, "cracked vapour → fractionator", "start", 8, CAT, True)
    # spent catalyst reactor -> regenerator
    b += pipe([(150, 212), (176, 244), (230, 214)], color="#444444", dash="5,3")
    b += lbl(168, 268, "spent catalyst (coked)", "middle", 7.8, GRAY)
    # regenerated catalyst regenerator -> riser base
    b += pipe([(250, 222), (250, 292), (62, 292)], color=GAS, dash="5,3", marker="ahR")
    b += lbl(120, 284, "regenerated catalyst returns hot", "start", 7.8, GAS, True)
    # air + flue
    b += pipe([(258, 262), (258, 226)], marker="ahB") + lbl(264, 256, "air in", "start", 8, WAT, True)
    b += pipe([(258, 72), (258, 48)], marker="ahR") + lbl(266, 44, "flue gas", "start", 8, GAS, True)
    b += note(180, 348, "Catalyst circulates: it carries heat from regenerator to riser")
    return svg_doc("FCC: reactor–regenerator loop", "Card 3.1(c): a few seconds in the riser, coke burned off in the regenerator", 356, b)

def _lane(y, icon, title, l1, l2, color):
    b = rect(12, y, 336, 76, "#FBFAFF", "#C9BCE0", 1.1, 6)
    b += icon
    b += t(96, y + 22, title, 10, color, True, "start")
    b += t(96, y + 40, l1, 8.3, INK, False, "start")
    b += t(96, y + 56, l2, 8.3, "#555555", False, "start")
    return b

def ref3_compare():
    b = ""
    ic1 = furnace(26, 66, 44, 34) + h_vessel(30, 108, 40, 16)
    b += _lane(52, ic1, "Thermal cracking (visbreaking, coking)", "Heat alone breaks the molecules; carbon rejected as coke.", "Simple and robust — but petrol is olefinic, lower octane.", HOT)
    ic2 = v_reactor(30, 146, 26, 40, (), STEEL_F, STEEL) + v_reactor(60, 146, 26, 40, (), "#FDECEF", GAS)
    b += _lane(136, ic2, "FCC (catalytic, no hydrogen)", "Zeolite catalyst, seconds of contact in a riser.", "Branched high-octane petrol + propylene feedstock.", STEEL)
    ic3 = v_reactor(34, 230, 34, 40, (("cat", 0.5),), "#FDF6EC", HOT) + t(78, 240, "H₂", 10, GAS, True)
    b += _lane(220, ic3, "Hydrocracking (catalytic + hydrogen)", "High-pressure H₂ saturates while cracking; S, N removed.", "Clean diesel / kerosene; costly hydrogen, heavy vessels.", CAT)
    b += note(180, 322, "Same aim — smaller molecules — three different selectivities")
    return svg_doc("Three ways to crack", "Card 3.1: thermal vs catalytic compared", 330, b)

def ref3_platforming():
    b = ""
    b += pipe([(8, 150), (40, 150)], marker="ahB")
    b += lbl(8, 200, "feed: hydrotreated naphtha + H₂", "start", 8, WAT, True)
    xs = [78, 148, 218]
    for i, cx in enumerate(xs):
        if i: b += furnace(cx - 58, 132, 26, 36)
        b += sphere(cx, 150, 19)
        b += t(cx, 154, "Pt", 8.5, HOT, True)
        b += t(cx, 182, f"reactor {i+1}", 7.5, HOT, True)
        if i < 2: b += pipe([(cx + 19, 150), (xs[i+1] - 45, 150)], marker="ahO")
    b += furnace(40, 132, 26, 36)
    b += pipe([(288, 150), (306, 150)], marker="ahG")
    b += h_vessel(306, 134, 48, 32, CAT_F, CAT) + t(330, 176, "separator", 7.5, CAT, True)
    b += pipe([(330, 134), (330, 96), (34, 96), (34, 140)], color=GAS, dash="5,3", marker="ahR")
    b += lbl(104, 88, "hydrogen recycled; net H₂ exported", "start", 8, GAS, True)
    b += pipe([(330, 166), (330, 196)], marker="ahG") + lbl(352, 194, "reformate out", "end", 8, CAT, True) + lbl(352, 208, "(high-octane petrol)", "end", 7.3, GRAY)
    b += t(53, 128, "heater", 7, HOT) + t(113, 128, "heater", 7, HOT) + t(183, 128, "heater", 7, HOT)
    b += note(180, 244, "Reheat between reactors: the main reactions absorb heat")
    b += note(180, 260, "More, smaller reactors in series = closer to ideal reforming")
    return svg_doc("Platforming: catalytic reformer train", "Card 3.2(b): heater–reactor–heater–reactor …", 268, b)

def ref3_hydrotreater():
    b = ""
    b += pump(30, 268) + pipe([(8, 288), (30, 278)], marker="ahB")
    b += lbl(6, 254, "feed oil", "start", 8.5, WAT, True)
    b += pipe([(38, 262), (66, 238)], marker="ahB")
    b += exch(66, 224, 38, 22) + t(85, 218, "heat recovery", 7, CAT)
    b += pipe([(104, 232), (126, 232), (126, 150)], marker="ahO")
    b += lbl(108, 200, "+ hydrogen", "start", 8, GAS, True)
    b += pipe([(70, 286), (70, 300), (200, 300), (200, 252)], color=GAS, dash="5,3", marker="ahR")
    b += lbl(76, 292, "recycle H₂ returns", "start", 7.5, GAS)
    b += furnace(104, 118, 46, 30) + t(127, 110, "heater", 7.5, HOT, True)
    b += pipe([(127, 118), (127, 92), (160, 92)], marker="ahO")
    b += v_reactor(160, 84, 58, 150, (("catalyst bed", 0.30), ("catalyst bed", 0.68)), "#FDF6EC", HOT)
    b += t(189, 76, "reactor", 8.5, HOT, True)
    b += pipe([(218, 130), (238, 130)], marker="ahG")
    b += h_vessel(238, 112, 66, 36, CAT_F, CAT) + t(271, 104, "separator", 8, CAT, True)
    b += pipe([(271, 112), (271, 84), (310, 84)], color=GAS, marker="ahR")
    b += lbl(354, 76, "H₂ recycled", "end", 7.8, GAS, True) + lbl(354, 90, "H₂S → sulfur plant", "end", 7.8, GAS)
    b += pipe([(271, 148), (271, 176)], marker="ahG")
    b += column(252, 176, 38, 62, 4) + t(246, 214, "stripper", 7.5, STEEL, True, "end")
    b += pipe([(271, 245), (271, 262)], marker="ahG") + lbl(276, 256, "treated product", "start", 8.5, CAT, True) + lbl(276, 270, "(low sulfur)", "start", 7.3, GRAY)
    b += note(180, 330, "Hydrogen cleans the molecules; the carbon skeleton stays")
    return svg_doc("Hydrotreater (HDS) unit", "Card 3.3: S, N and O leave as H₂S, NH₃ and water", 338, b)

def ref4_sulfur_routes():
    b = ""
    ic1 = h_vessel(26, 70, 46, 20) + pump(50, 108, 7)
    b += _lane(52, ic1, "Sweetening — Doctor / MEROX", "Mercaptans → disulfides: odour and corrosion cured.", "Sulfur stays in the fuel — cheapest, shallowest.", HOT)
    ic2 = column(38, 142, 26, 46, 4)
    b += _lane(136, ic2, "Extractive treatment — caustic / SO₂", "Solvent dissolves part of the S compounds + aromatics.", "Deeper; solvent must be recovered and recycled.", STEEL)
    ic3 = v_reactor(34, 226, 34, 40, (("cat", 0.5),), "#FDF6EC", HOT) + t(80, 240, "H₂", 10, GAS, True)
    b += _lane(220, ic3, "Catalytic desulfurisation (HDS)", "All sulfur forms → H₂S, then sulfur recovery.", "Deepest — the only route to ultra-low-sulfur fuels.", CAT)
    b += pipe([(353, 290), (353, 70)], color=GAS, marker="ahR")
    b += t(338, 300, "cost &amp; depth rise", 7.5, GAS, True, "end")
    return svg_doc("Removing sulfur: three depths", "Card 4.1–4.2: choose by how much sulfur must go", 330, b)

def ref4_merox():
    b = ""
    b += column(56, 92, 46, 130, 6)
    b += t(79, 82, "EXTRACTOR", 8.5, STEEL, True)
    b += pipe([(8, 196), (56, 196)], marker="ahB") + lbl(6, 186, "sour LPG /", "start", 8.5, WAT, True) + lbl(6, 210, "petrol in", "start", 8, WAT)
    b += pipe([(79, 92), (79, 66), (150, 66)], marker="ahG")
    b += lbl(120, 58, "sweet product out", "start", 8.5, CAT, True)
    b += t(79, 106, "caustic in", 7.5, PUR, True)
    b += pipe([(102, 200), (140, 200), (140, 168)], color=PUR, marker="ahR")
    b += lbl(146, 208, "caustic + mercaptans out", "start", 7.5, PUR)
    b += v_reactor(140, 108, 56, 60, (("Co catalyst", 0.5),), "#FDF6EC", PUR)
    b += t(168, 100, "OXIDISER", 8.5, PUR, True)
    b += pipe([(168, 190), (168, 172)], marker="ahB") + lbl(174, 186, "air in", "start", 8.5, WAT, True)
    b += pipe([(196, 128), (232, 128)], color=PUR, marker="ahR")
    b += h_vessel(232, 110, 66, 36, PUR_F, PUR) + t(265, 102, "separator", 8, PUR, True)
    b += pipe([(298, 118), (322, 118)], color=HOT, marker="ahO")
    b += lbl(354, 104, "disulfide oil out", "end", 8, HOT, True)
    b += pipe([(248, 146), (248, 226), (86, 226), (86, 200)], color=PUR, dash="5,3", marker="ahR")
    b += pump(150, 226, 7)
    b += lbl(96, 246, "caustic regenerated &amp; recycled — only air is consumed", "start", 8, PUR, True)
    b += note(180, 282, "Mercaptans are oxidised to disulfides inside the caustic loop")
    return svg_doc("MEROX sweetening unit", "Card 4.2(c): extract, oxidise, regenerate the caustic", 290, b)

def ref4_so2():
    b = ""
    b += column(140, 66, 54, 168, 7)
    b += t(167, 56, "extraction column (cold)", 8.5, STEEL, True)
    # refrigeration coil
    for i in range(5):
        yy = 84 + i * 26
        b += path(f"M132,{yy} q35,-10 70,0", "none", WAT, 1.1)
    b += lbl(88, 92, "chilled: liquid SO₂", "end", 7.8, WAT, True) + lbl(88, 104, "selective solvent", "end", 7.3, GRAY)
    b += pipe([(60, 208), (140, 208)], marker="ahB") + lbl(8, 198, "kerosene in", "start", 8.5, WAT, True)
    b += pipe([(167, 66), (167, 48), (240, 48)], marker="ahG")
    b += column(228, 48, 34, 58, 3) + t(245, 122, "stripper", 7.5, STEEL, True)
    b += pipe([(262, 66), (300, 66)], marker="ahG") + lbl(352, 60, "treated kerosene", "end", 8.5, CAT, True) + lbl(352, 74, "(high smoke point)", "end", 7.3, GRAY)
    b += pipe([(167, 234), (167, 262), (96, 262)], marker="ahO")
    b += exch(60, 250, 38, 22) + t(79, 244, "evaporator", 7.5, HOT, True)
    b += pipe([(60, 261), (30, 261)], marker="ahO") + lbl(4, 250, "aromatic", "start", 8, HOT, True) + lbl(4, 280, "extract out", "start", 7.5, HOT)
    b += pipe([(257, 106), (257, 226), (120, 226), (120, 120)], color=WAT, dash="5,3", marker="ahB")
    b += pump(160, 226, 7)
    b += lbl(120, 240, "SO₂ recovered &amp; recycled (closed loop)", "start", 8, WAT, True)
    b += note(180, 296, "Physical selectivity: SO₂ dissolves aromatics and sulfur compounds")
    return svg_doc("Liquid SO₂ extraction of kerosene (Edeleanu)", "Card 4.3: aromatics leave with the extract phase", 304, b)

def ref4_lube_extraction():
    b = ""
    b += column(120, 58, 56, 190, 8)
    b += t(148, 78, "extraction tower", 8.5, STEEL, True)
    b += pipe([(148, 40), (148, 58)], marker="ahB") if False else ""
    b += pipe([(90, 44), (138, 44), (148, 58)], marker="ahB")
    b += lbl(8, 38, "solvent in (top):", "start", 8.5, WAT, True) + lbl(8, 52, "furfural / phenol", "start", 8, WAT)
    b += pipe([(30, 130), (120, 130)], marker="ahB")
    b += lbl(8, 120, "lube distillate in", "start", 8.5, WAT, True)
    b += pipe([(148, 58), (148, 40), (230, 40)], marker="ahG")
    b += column(230, 40, 34, 56, 3) + t(247, 108, "solvent recovery", 7.5, STEEL, True)
    b += pipe([(264, 52), (296, 52)], marker="ahG")
    b += lbl(354, 44, "raffinate:", "end", 8.5, CAT, True)
    b += lbl(354, 58, "high-VI base oil", "end", 8, CAT)
    b += lbl(354, 72, "→ dewaxing next", "end", 7.5, GRAY)
    b += pipe([(148, 248), (148, 272), (230, 272)], marker="ahO")
    b += column(230, 226, 34, 52, 3)
    b += pipe([(264, 252), (300, 252)], marker="ahO")
    b += lbl(352, 246, "extract: aromatic oil", "end", 8.5, HOT, True)
    b += pipe([(247, 226), (247, 110), (108, 62)], color=WAT, dash="5,3", marker="ahB")
    b += lbl(196, 150, "solvent recovered", "start", 7.5, WAT) + lbl(196, 162, "&amp; recycled", "start", 7.5, WAT)
    b += note(180, 306, "Countercurrent contact: solvent takes the low-VI aromatics down")
    return svg_doc("Solvent refining of lube oil", "Card 4.4: furfural or phenol extraction", 314, b)

def ref4_ketone_dewaxing():
    b = ""
    b += pipe([(8, 118), (34, 118)], marker="ahB")
    b += lbl(8, 88, "waxy oil + MEK–toluene in", "start", 8, WAT, True)
    # scraped-surface chiller
    b += h_vessel(34, 100, 96, 38, WAT_F, WAT)
    b += pipe([(44, 119), (58, 110), (72, 128), (86, 110), (100, 128), (114, 112)], WAT, 1.2, None, "ahB", arrow=False)
    b += lbl(36, 154, "scraped-surface chiller (refrigerated)", "start", 7.5, GRAY)
    b += pipe([(130, 119), (168, 119), (168, 138)], marker="ahO")
    b += drum_filter(216, 150, 34)
    b += t(216, 116, "rotary vacuum filter", 8.5, HOT, True)
    b += path("M238,128 L252,116", "none", HOT, 1.6) + lbl(258, 138, "scraper:", "start", 8, HOT, True) + lbl(258, 152, "wax cake off", "start", 7.5, HOT)
    b += pipe([(252, 168), (282, 168), (282, 190)], marker="ahO")
    b += lbl(284, 184, "slack wax →", "start", 8.5, HOT, True) + lbl(284, 198, "de-oiling", "start", 7.5, GRAY)
    b += pipe([(196, 190), (196, 220), (90, 220)], marker="ahG")
    b += lbl(60, 234, "dewaxed oil (low pour point)", "start", 8.5, CAT, True)
    b += column(286, 208, 30, 52, 3)
    b += lbl(301, 278, "solvent recovery", "middle", 7.3, STEEL, True)
    b += pipe([(196, 220), (286, 226)], color=WAT, dash="4,3", marker="ahB")
    b += note(180, 300, "Ketone throws the wax out; toluene keeps the oil dissolved")
    return svg_doc("Ketone (solvent) dewaxing", "Card 4.6(b): chill → crystallise → filter → recover solvent", 308, b)

D = {
 "ref3_fcc": ref3_fcc(), "ref3_compare": ref3_compare(), "ref3_platforming": ref3_platforming(),
 "ref3_hydrotreater": ref3_hydrotreater(),
 "ref4_sulfur_routes": ref4_sulfur_routes(), "ref4_merox": ref4_merox(), "ref4_so2": ref4_so2(),
 "ref4_lube_extraction": ref4_lube_extraction(), "ref4_ketone_dewaxing": ref4_ketone_dewaxing(),
}
