# -*- coding: utf-8 -*-
"""DI04000081 Unit 5 diagrams."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from equip_lib import *

def ent5_dpr():
    b = ""; y = 48
    steps = [("IDEA &amp; FEASIBILITY", "Unit 2 evaluation, done at project scale"), ("DPR PREPARATION", "costs, means of finance, projections"),
             ("APPRAISAL &amp; SANCTION", "bank/agency examine, then fund"), ("IMPLEMENTATION", "land, machinery, registration, hiring"),
             ("OPERATIONS &amp; REVIEW", "produce, sell, monitor against the DPR")]
    for i, (h, s) in enumerate(steps):
        b += rect(50, y, 260, 34, "#FFFFFF", STEEL, 1.3, 7) + t(180, y + 14, h, 8.8, STEEL, True) + t(180, y + 27, s, 7.3, "#555555")
        if i < len(steps) - 1: b += pipe([(180, y + 34), (180, y + 44)])
        y += 46
    b += note(180, y + 6, "The DPR is a promise with arithmetic attached")
    return svg_doc("Project life: idea to operations", "Card 5.1: where the project report sits", y + 12, b)

def ent5_feasibility():
    b = ""
    items = [(180, 54, "MARKET", "demand is real"), (292, 106, "TECHNICAL", "can we make it?"), (262, 208, "FINANCIAL", "returns acceptable?"),
             (98, 208, "MANAGERIAL", "team covers it?"), (68, 106, "LEGAL &amp; ECO-SOCIAL", "licences, jobs, duties")]
    for cx, cy, h, s in items:
        b += line(180, 140, cx, cy, "#CBAADE", 1.1)
    for cx, cy, h, s in items:
        b += rect(cx - 56, cy - 19, 112, 38, "#FFFFFF", STEEL, 1.3, 6) + t(cx, cy - 2, h, 7.6, STEEL, True) + t(cx, cy + 11, s, 7.0, "#555555")
    b += circ(180, 140, 36, "#FFFFFF", PUR, 1.8) + t(180, 136, "PROJECT", 8.5, PUR, True) + t(180, 149, "IDEA", 8.5, PUR, True)
    b += note(180, 258, "Weakness in any one lens can stop or reshape the project")
    return svg_doc("Feasibility: five lenses on one idea", "Card 5.1: test before you build", 266, b)

def ent5_cost():
    b = ""
    rows = [("Land / premises", "purchase, development — or rent deposits"), ("Building &amp; civil work", "or furnishing of rented space"),
            ("Plant &amp; machinery", "with installation, freight, electrification"), ("Other fixed assets", "furniture, computers, vehicles"),
            ("Pre-operative expenses", "registration, legal, trial runs, setup interest"), ("Contingency", "the honest allowance for surprises"),
            ("Working-capital margin", "your share of daily running funds")]
    y = 48
    for h, s in rows:
        b += rect(30, y, 300, 30, "#FFFFFF", STEEL, 1.2, 6) + t(180, y + 12, h, 8.4, STEEL, True) + t(180, y + 24, s, 7.1, "#555555"); y += 36
    b += rect(30, y + 2, 300, 30, STEEL_F, STEEL, 1.4, 6) + t(180, y + 20, "= TOTAL PROJECT COST  ↔  MEANS OF FINANCE", 8.4, STEEL, True)
    return svg_doc("Building up the project cost", "Card 5.1: component by component, from quotations", y + 40, b)

def ent5_bep():
    b = line(46, 226, 46, 46, "#666666", 1.3) + line(46, 226, 340, 226, "#666666", 1.3)
    b += t(30, 52, "₹", 10, "#666666", True) + t(336, 240, "output →", 8, "#666666")
    b += line(46, 150, 340, 150, GAS, 1.6) + t(330, 142, "fixed cost F", 8, GAS, True, anchor="end")
    b += line(46, 150, 340, 62, HOT, 2.0) + t(334, 58, "total cost", 8.5, HOT, True, anchor="end")
    b += line(46, 226, 340, 84, STEEL, 2.0) + t(334, 96, "total revenue", 8.5, STEEL, True, anchor="end")
    # intersection of TC: y=150-88*(x-46)/294 ; TR: y=226-142*(x-46)/294 ; equal: 150-88u=226-142u -> 54u=76 -> u=1.407?? recompute below in builder
    bx = 46 + 294 * (76 / 54) / 2  # placeholder replaced by exact calc under
    bx = 46 + (76 * 294) / (142 - 88 + 76)  # not used
    # exact: TC y = 150 - (88/294)(x-46); TR y = 226 - (142/294)(x-46). Set equal:
    # 226-150 = (142-88)/294 * (x-46) -> (x-46) = 76*294/54 = 413.8 -- off-chart; adjust slopes instead:
    return None  # replaced below

def _bep():
    b = line(46, 226, 46, 46, "#666666", 1.3) + line(46, 226, 340, 226, "#666666", 1.3)
    b += t(28, 54, "Rs", 9, "#666666", True) + t(338, 241, "output", 8, "#666666", anchor="end")
    b += line(46, 156, 340, 156, GAS, 1.6) + t(336, 148, "fixed cost F", 8, GAS, True, anchor="end")
    # total cost from (46,156) to (340,96); revenue from (46,226) to (340,66)
    b += line(46, 156, 340, 96, HOT, 2.0) + t(336, 90, "total cost", 8.5, HOT, True, anchor="end")
    b += line(46, 226, 340, 66, STEEL, 2.0) + t(336, 118, "total revenue", 8.5, STEEL, True, anchor="end")
    # intersection: TC: y=156-(60/294)(x-46); TR: y=226-(160/294)(x-46); equal -> 70=(100/294)(x-46) -> x-46=205.8 -> x=251.8; y=156-42=114
    bx, by = 252, 114
    b += circ(bx, by, 4.5, HOT_F, HOT, 1.6)
    b += pipe([(bx, by), (bx, 226)], color=HOT, dash="4,3", marker="ahR")
    b += t(bx, 240, "BEP output", 8.5, HOT, True)
    b += t(120, 120, "LOSS", 9, HOT, True) + t(310, 160, "PROFIT", 9, CAT, True)
    b += note(180, 266, "BEP = Fixed costs / (Price - Variable cost per unit); right of BEP, distance = margin of safety")
    return svg_doc("The break-even chart", "Card 5.1: where total revenue crosses total cost", 274, b)

def ent5_exit():
    b = rect(105, 44, 150, 30, PUR_F, PUR, 1.4, 7) + t(180, 63, "FOUNDER'S EXIT", 9.5, PUR, True)
    rows = [("SUCCESSION", "family or professional manager takes over", CAT), ("SALE / MERGER", "strategic buyer pays for market &amp; brand", STEEL),
            ("IPO", "public listing — only at real scale", HOT), ("INCOME HARVEST", "managers run it; owner draws income", PUR)]
    y = 88
    b += pipe([(180, 74), (180, y)])
    for h, s, c in rows:
        b += pipe([(180, y + 15), (120, y + 15)], color=c, marker=None if False else "ah")
        b += rect(110, y, 200, 30, "#FFFFFF", c, 1.3, 6) + t(210, y + 12, h, 8.4, c, True) + t(210, y + 24, s, 7.1, "#555555")
        y += 38
        if y < 240: b += pipe([(180, y - 8), (180, y)])
    b += rect(30, y + 2, 300, 28, "#FDECEC", HOT, 1.2, 6) + t(180, y + 13, "LAST RESORT: orderly liquidation", 8.2, HOT, True) + t(180, y + 25, "bankruptcy avoided by early warning + early action", 7.2, "#555555")
    return svg_doc("Exit routes of the founder", "Cards 5.5–5.6: planned endings, and the unplanned one", y + 38, b)

DIAGRAMS = [
 ("ent5_dpr", "Project life: idea to operations", ent5_dpr()),
 ("ent5_feasibility", "Feasibility study lenses", ent5_feasibility()),
 ("ent5_cost", "Components of project cost", ent5_cost()),
 ("ent5_bep", "Break-even chart", _bep()),
 ("ent5_exit", "Exit routes of the founder", ent5_exit()),
]
