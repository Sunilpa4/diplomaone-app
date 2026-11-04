# -*- coding: utf-8 -*-
"""Real-type diagrams: Unit 5 (5)."""
from equip_lib import *

def _lane5(y, src, block, prod, color):
    b = rect(10, y, 340, 62, "#FBFAFF", "#C9BCE0", 1.1, 6)
    b += t(58, y + 36, src, 8.8, WAT, True)
    b += pipe([(104, y + 31), (128, y + 31)], marker="ahB")
    b += t(172, y + 36, block, 8.8, color, True)
    b += pipe([(218, y + 31), (242, y + 31)], marker="ahG")
    b += t(302, y + 30, prod, 8.2, CAT, True)
    return b

def ref5_feedstocks():
    b = _lane5(48, "natural gas", "syngas → methanol", "formaldehyde, resins", PUR)
    b += _lane5(120, "naphtha / LPG", "ethylene, propylene", "VCM·PVC, EO, PO, plastics", STEEL)
    b += _lane5(192, "reformate / FCC", "BTX aromatics, H₂", "LAB detergents, styrene", HOT)
    b += t(58, 40, "FEEDSTOCK", 7.5, GRAY, True) + t(172, 40, "BUILDING BLOCK", 7.5, GRAY, True) + t(296, 40, "PRODUCTS", 7.5, GRAY, True)
    b += note(180, 282, "Every feedstock also has a fuel value — diversion is an economic choice")
    return svg_doc("Where petrochemicals come from", "Card 5.1(b): refinery and gas streams to building blocks", 290, b)

def ref5_methanol():
    b = ""
    b += furnace(14, 96, 48, 58) + t(38, 88, "reformer", 7.8, HOT, True)
    b += lbl(6, 176, "natural gas + steam → syngas", "start", 7.5, GRAY)
    b += pipe([(62, 125), (92, 125)], marker="ahB") + pump(104, 125, 8, "") + t(104, 148, "compressor", 7, STEEL)
    b += pipe([(112, 125), (134, 125)], marker="ahB")
    b += v_reactor(134, 84, 56, 92, (("Cu catalyst", 0.5),), "#FDF6EC", HOT)
    b += t(162, 76, "converter", 8.5, HOT, True)
    b += pipe([(190, 118), (214, 118)], marker="ahG")
    b += exch(214, 106, 40, 24) + t(234, 98, "condenser", 7.5, CAT, True)
    b += h_vessel(262, 100, 56, 32, CAT_F, CAT) + t(290, 92, "separator", 8, CAT, True)
    b += pipe([(290, 132), (290, 158)], marker="ahG")
    b += column(272, 158, 36, 56, 3) + t(290, 224, "distillation", 7.5, STEEL, True)
    b += pipe([(290, 221), (290, 238)], marker="ahG") + lbl(296, 234, "methanol", "start", 8.5, CAT, True)
    # recycle
    b += pipe([(278, 100), (278, 66), (120, 66), (120, 112)], color=GAS, dash="5,3", marker="ahR")
    b += lbl(118, 58, "unconverted gas recycled", "start", 8, GAS, True)
    b += pipe([(310, 100), (330, 78)], color=GRAY, dash="3,3", marker="ah")
    b += lbl(332, 66, "purge", "start", 7.5, GRAY)
    b += note(180, 276, "CO + 2H₂ ⇌ CH₃OH — heat released, so cooling and recycle drive conversion")
    return svg_doc("Methanol synthesis loop", "Card 5.2(a): make syngas, convert, condense, recycle", 284, b)

def ref5_vcm():
    b = ""
    b += v_reactor(20, 66, 62, 54, (), STEEL_F, STEEL) + t(51, 58, "direct", 8, STEEL, True) + t(51, 132, "chlorination", 7.5, GRAY)
    b += t(51, 98, "+ Cl₂", 8.5, STEEL, True)
    b += t(188, 134, "", 7)
    b += v_reactor(150, 66, 62, 54, (), "#FFF6EC", HOT) + t(181, 58, "oxy-", 8, HOT, True) + t(190, 134, "chlorination", 7.5, GRAY, False, "start")
    b += t(181, 98, "+ HCl, O₂", 8, HOT, True)
    b += pipe([(8, 84), (20, 84)], marker="ahB") + lbl(6, 74, "C₂H₄", "start", 8, WAT, True)
    b += pipe([(118, 84), (150, 84)], marker="ahB") + lbl(124, 74, "C₂H₄", "start", 8, WAT, True)
    b += pipe([(82, 100), (120, 150)], marker="ahO") + pipe([(150, 108), (128, 142)], marker="ahO")
    b += column(104, 150, 44, 62, 4) + t(126, 142, "EDC purification", 7.5, STEEL, True)
    b += pipe([(126, 212), (126, 232)], marker="ahO")
    b += furnace(92, 232, 68, 44) + t(126, 224, "EDC cracking furnace", 8, HOT, True)
    b += pipe([(160, 250), (208, 250), (208, 176)], marker="ahG")
    b += column(190, 118, 40, 58, 3) + t(210, 110, "VCM separation", 7.5, STEEL, True)
    b += pipe([(210, 118), (210, 96)], marker="ahG") + lbl(216, 90, "VCM → PVC", "start", 9, CAT, True)
    # HCl recycle dashed red from separator to oxychlorination
    b += pipe([(196, 176), (250, 200), (250, 66), (214, 80)], color=GAS, dash="5,3", marker="ahR")
    b += lbl(354, 146, "HCl recycled —", "end", 8, GAS, True)
    b += lbl(354, 160, "none wasted (the 'balance')", "end", 7.5, GRAY)
    b += note(180, 306, "Half the ethylene is chlorinated with Cl₂, half with recycled HCl")
    return svg_doc("Balanced vinyl chloride (VCM) process", "Card 5.3(a): three steps, one loop", 314, b)

def ref5_eo():
    b = ""
    b += pipe([(8, 120), (64, 120)], marker="ahB")
    b += lbl(2, 104, "ethylene + O₂", "start", 7.5, WAT, True) + lbl(6, 136, "+ ballast gas", "start", 7.5, GRAY)
    # tubular reactor
    b += rect(64, 78, 74, 92, "#FDF6EC", HOT, 1.7, 2)
    for i in range(5):
        tx = 76 + i * 13
        b += line(tx, 86, tx, 162, HOT, 1.6)
    b += circ(60, 96, 2.5, "#fff", HOT, 0.8)
    b += t(101, 70, "tubular reactor", 8.5, HOT, True) + t(101, 182, "Ag catalyst tubes, cooled", 7.5, GRAY)
    b += pipe([(138, 118), (148, 118)], marker="ahO")
    b += column(148, 66, 50, 130, 6)
    b += t(173, 84, "absorber", 8.5, STEEL, True) + t(173, 96, "(water)", 7, GRAY)
    b += pipe([(173, 196), (173, 222)], marker="ahG")
    b += h_vessel(140, 222, 66, 28, CAT_F, CAT)
    b += lbl(210, 232, "EO solution → purification", "start", 8.5, CAT, True) + lbl(210, 246, "(part → ethylene glycol)", "start", 7.5, GRAY)
    b += pipe([(160, 66), (160, 44), (90, 44), (90, 74)], color=GAS, dash="5,3", marker="ahR")
    b += lbl(64, 60, "unconverted ethylene recycled", "start", 7.5, GAS, True)
    b += rect(246, 92, 100, 56, "#FDF1F2", GAS, 1.1, 5)
    b += t(296, 106, "the enemy reaction:", 8, GAS, True) + t(296, 121, "C₂H₄ + 3O₂ → 2CO₂ + 2H₂O", 7.0, GAS, True) + t(296, 136, "wastes feed, adds heat", 7.3, GRAY)
    b += pipe([(198, 110), (248, 110)], color=GAS, dash="3,3", marker="ahR")
    b += note(180, 282, "Selectivity is everything: stop at the epoxide, never burn to CO₂")
    return svg_doc("Ethylene oxide from ethylene", "Card 5.3(b): direct oxidation over silver", 290, b)

def ref5_lab():
    b = ""
    b += v_reactor(16, 92, 54, 66, (), STEEL_F, STEEL)
    b += t(43, 84, "molecular-sieve", 7.5, STEEL, True) + t(43, 170, "separation", 7.5, GRAY)
    b += t(43, 130, "n-C₁₀–₁₄", 8.5, STEEL, True)
    b += pipe([(8, 108), (16, 108)], marker="ahB") + lbl(6, 98, "kerosene cut", "start", 7.8, WAT, True)
    b += pipe([(70, 118), (96, 118)], marker="ahB")
    b += v_reactor(96, 92, 54, 66, (("cat", 0.5),), "#FDF6EC", HOT)
    b += t(123, 84, "dehydrogenation", 7.5, HOT, True) + t(123, 170, "to linear olefins", 7.5, GRAY)
    b += pipe([(150, 118), (176, 118)], marker="ahO")
    b += v_reactor(176, 92, 58, 66, (), "#FFF6EC", HOT)
    b += t(205, 84, "alkylation reactor", 8, HOT, True) + t(205, 170, "acid catalyst", 7.5, GRAY)
    b += t(205, 128, "benzene", 8, HOT, True) + t(205, 140, "(excess)", 7, GRAY)
    b += pipe([(234, 118), (258, 118)], marker="ahG")
    b += column(258, 74, 42, 110, 5)
    b += t(279, 64, "fractionation", 8, STEEL, True)
    b += pipe([(279, 74), (279, 52), (205, 52), (205, 88)], color=GAS, dash="5,3", marker="ahR")
    b += lbl(238, 44, "benzene recycled", "start", 8, GAS, True)
    b += pipe([(279, 184), (279, 208)], marker="ahG")
    b += lbl(352, 202, "LAB → sulfonation", "end", 8.5, CAT, True) + lbl(352, 216, "= detergent (LAS)", "end", 7.5, GRAY)
    b += note(180, 252, "Straight C₁₀–C₁₄ chain on the ring: detergents that biodegrade")
    return svg_doc("Linear alkyl benzene (LAB)", "Card 5.4: from kerosene paraffins to detergent feedstock", 260, b)

D = {
 "ref5_feedstocks": ref5_feedstocks(), "ref5_methanol": ref5_methanol(), "ref5_vcm": ref5_vcm(),
 "ref5_eo": ref5_eo(), "ref5_lab": ref5_lab(),
}
