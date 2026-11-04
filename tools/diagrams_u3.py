# -*- coding: utf-8 -*-
"""DI04000081 Unit 3 diagrams."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from equip_lib import *

def ent3_commerce():
    b = rect(115, 44, 130, 32, PUR_F, PUR, 1.5, 7) + t(180, 64, "BUSINESS", 10, PUR, True)
    b += pipe([(145, 76), (95, 98)]) + pipe([(215, 76), (265, 98)])
    b += rect(14, 98, 162, 40, STEEL_F, STEEL, 1.3, 7) + t(95, 115, "INDUSTRY — makes", 9, STEEL, True) + t(95, 129, "primary · extractive · manufacturing", 7.2, "#555555")
    b += rect(184, 98, 162, 40, "#FFFFFF", CAT, 1.3, 7) + t(265, 115, "COMMERCE — moves", 9, CAT, True) + t(265, 129, "trade + aids to trade", 7.2, "#555555")
    b += pipe([(230, 138), (120, 158)]) + pipe([(300, 138), (262, 158)])
    b += rect(34, 158, 152, 46, "#FFFFFF", CAT, 1.2, 7) + t(110, 176, "TRADE", 8.6, CAT, True) + t(110, 191, "wholesale · retail · foreign", 7.3, "#555555")
    b += rect(194, 158, 152, 46, CAT_F, CAT, 1.2, 7) + t(270, 176, "AIDS TO TRADE", 8.6, CAT, True) + t(270, 191, "transport · banking · insurance · storage", 7.3, "#555555")
    b += note(180, 224, "Industry makes, commerce moves, business organises both for a market")
    return svg_doc("Industry, commerce and business", "Card 3.1: the three interlocking activities", 232, b)

def ent3_ownership():
    b = ""
    rows = [("Sole proprietorship", "one owner · unlimited liability · fastest start", HOT), ("Partnership / LLP", "shared capital &amp; skills · LLP limits liability", HOT),
            ("Company (OPC–private–public)", "separate identity · limited liability · raises capital", STEEL), ("Co-operative society", "member-owned · one member, one vote", CAT),
            ("Public-sector forms", "departmental · statutory corporation · govt company", PUR)]
    y = 50
    for h, s, c in rows:
        b += rect(30, y, 300, 34, "#FFFFFF", c, 1.3, 7) + t(180, y + 14, h, 8.8, c, True) + t(180, y + 27, s, 7.4, "#555555"); y += 42
    b += note(180, y + 6, "Choose by capital need, risk tolerance, compliance capacity and ambition")
    return svg_doc("Forms of ownership at a glance", "Card 3.2: control and simplicity versus capital and protection", y + 12, b)

def ent3_leadership():
    b = ""
    segs = [(14, "AUTOCRATIC", "leader decides alone", HOT), (124, "DEMOCRATIC", "team is consulted", CAT), (234, "FREE-REIN", "team decides", STEEL)]
    for x, h, s, c in segs:
        b += rect(x, 62, 112, 44, "#FFFFFF", c, 1.4, 7) + t(x + 56, 82, h, 8.6, c, True) + t(x + 56, 97, s, 7.2, "#555555")
    b += pipe([(20, 122), (340, 122)], color="#888888") + t(14, 136, "leader control", 7.6, "#777777", anchor="start") + t(346, 136, "team freedom", 7.6, "#777777", anchor="end")
    b += rect(54, 152, 252, 52, PUR_F, PUR, 1.3, 7) + t(180, 172, "MANAGERIAL GRID (9,9) team style", 8.8, PUR, True) + t(180, 189, "high concern for production AND for people", 7.6, "#555555")
    b += note(180, 224, "Situational rule: match the style to the person's readiness")
    return svg_doc("Leadership styles and models", "Card 3.3: who decides, and how much each side is cared for", 232, b)

def ent3_functions():
    b = ""
    items = [(180, 54, "PLANNING", "decide in advance", HOT), (292, 118, "ORGANISING", "arrange work &amp; authority", CAT),
             (248, 220, "STAFFING", "right people in boxes", STEEL), (112, 220, "DIRECTING", "guide &amp; motivate daily", PUR),
             (68, 118, "CONTROLLING", "compare &amp; correct", GAS)]
    for cx, cy, h, s, c in items:
        b += line(180, 150, cx, cy, "#CBAADE", 1.1)
    for cx, cy, h, s, c in items:
        b += rect(cx - 54, cy - 19, 108, 38, "#FFFFFF", c, 1.3, 6) + t(cx, cy - 2, h, 8.4, c, True) + t(cx, cy + 11, s, 7.0, "#555555")
    b += circ(180, 150, 34, "#FFFFFF", PUR, 1.8) + t(180, 146, "MANAGE-", 8, PUR, True) + t(180, 158, "MENT", 8, PUR, True)
    b += note(180, 268, "A cycle, not a queue: controlling feeds the next plan — skip one, get its failure")
    return svg_doc("The five functions of management", "Card 3.4: what a manager actually does all day", 276, b)

def ent3_orgchart():
    b = rect(120, 46, 120, 30, PUR_F, PUR, 1.4, 7) + t(180, 59, "FOUNDER / MD", 8.8, PUR, True) + t(180, 70, "top level", 7.0, "#555555")
    b += pipe([(150, 76), (95, 96)]) + pipe([(210, 76), (265, 96)])
    for cx, h, s in [(95, "PRODUCTION MANAGER", "middle level"), (265, "SALES MANAGER", "middle level")]:
        b += rect(cx - 72, 96, 144, 32, "#FFFFFF", STEEL, 1.3, 6) + t(cx, 110, h, 7.8, STEEL, True) + t(cx, 122, s, 7.0, "#555555")
    b += pipe([(95, 128), (95, 148)]) + pipe([(265, 128), (265, 148)])
    for cx in (95, 265):
        b += rect(cx - 72, 148, 144, 32, "#FFFFFF", CAT, 1.3, 6) + t(cx, 162, "SUPERVISORS", 8.2, CAT, True) + t(cx, 174, "operating level", 7.0, "#555555")
    b += pipe([(95, 180), (95, 200)]) + pipe([(265, 180), (265, 200)])
    b += rect(23, 200, 144, 30, CAT_F, CAT, 1.2, 6) + t(95, 218, "WORKERS / OPERATORS", 7.8, CAT, True)
    b += rect(193, 200, 144, 30, CAT_F, CAT, 1.2, 6) + t(265, 218, "SALES &amp; SERVICE STAFF", 7.8, CAT, True)
    b += note(180, 250, "Line structure: every task has an owner, every person one boss")
    return svg_doc("Organisation structure (line type)", "Card 3.4: three levels of a growing unit", 258, b)

def ent3_control():
    b = ""
    steps = [(95, 74, "1 · SET STANDARDS", "from plan &amp; budget", HOT), (265, 74, "2 · MEASURE ACTUAL", "counts, reports, observation", CAT),
             (265, 168, "3 · COMPARE", "find deviations that matter", STEEL), (95, 168, "4 · CORRECT", "fix work — or revise the standard", PUR)]
    for cx, cy, h, s, c in steps:
        b += rect(cx - 78, cy - 22, 156, 44, "#FFFFFF", c, 1.3, 7) + t(cx, cy - 3, h, 8.4, c, True) + t(cx, cy + 11, s, 7.2, "#555555")
    b += pipe([(173, 74), (187, 74)]) + pipe([(265, 96), (265, 146)]) + pipe([(187, 168), (173, 168)]) + pipe([(95, 146), (95, 96)])
    b += note(180, 214, "Backward-looking measurement, forward-looking purpose: early warning")
    return svg_doc("The controlling process", "Card 3.4: a four-step correction loop", 222, b)

DIAGRAMS = [
 ("ent3_commerce", "Industry, commerce and business", ent3_commerce()),
 ("ent3_ownership", "Forms of ownership at a glance", ent3_ownership()),
 ("ent3_leadership", "Leadership styles and models", ent3_leadership()),
 ("ent3_functions", "The five functions of management", ent3_functions()),
 ("ent3_orgchart", "Organisation structure (line type)", ent3_orgchart()),
 ("ent3_control", "The controlling process", ent3_control()),
]
