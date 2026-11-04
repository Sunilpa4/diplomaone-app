# -*- coding: utf-8 -*-
"""DI04000081 Unit 2 diagrams."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from equip_lib import *

def _flow(steps):
    b = ""; y = 48
    for i, (h, s) in enumerate(steps):
        b += rect(60, y, 240, 34, "#FFFFFF", STEEL, 1.3, 7) + t(180, y + 14, h, 9, STEEL, True) + t(180, y + 27, s, 7.4, "#555555")
        if i < len(steps) - 1: b += pipe([(180, y + 34), (180, y + 44)])
        y += 46
    return b, y

def ent2_pipeline():
    b, y = _flow([("1 · DISCOVER", "notice problems, gaps and changes"), ("2 · GENERATE &amp; SCREEN", "many ideas, filtered practically"),
                  ("3 · IDENTIFY PRODUCT", "one offer for one clear customer"), ("4 · EVALUATE", "market research tests willingness to pay"),
                  ("5 · BUSINESS PLAN", "marketing + financial plan written"), ("6 · SET UP &amp; LAUNCH", "register, arrange 7-M, open")])
    return svg_doc("From idea to start-up", "Cards 2.1–2.3: the Activity Map drawn as a journey", y + 2, b)

def ent2_plan():
    b = rect(105, 46, 150, 30, PUR_F, PUR, 1.4, 7) + t(180, 65, "BUSINESS PLAN", 10, PUR, True)
    b += pipe([(150, 76), (95, 96)]) + pipe([(210, 76), (265, 96)])
    b += rect(14, 96, 162, 96, "#FFFFFF", STEEL, 1.3, 7) + t(95, 112, "MARKETING PLAN", 8.8, STEEL, True)
    for i, s in enumerate(["market size &amp; target customers", "competition and pricing", "promotion &amp; sales channels", "sales forecast"]):
        b += t(95, 130 + i * 14, "• " + s, 7.4, "#444444")
    b += rect(184, 96, 162, 96, "#FFFFFF", CAT, 1.3, 7) + t(265, 112, "FINANCIAL PLAN", 8.8, CAT, True)
    for i, s in enumerate(["project cost &amp; sources of funds", "projected income and cash flow", "repayment schedule", "break-even expectation"]):
        b += t(265, 130 + i * 14, "• " + s, 7.4, "#444444")
    b += rect(34, 208, 292, 30, "#FFF7E8", HOT, 1.2, 7) + t(180, 220, "SOURCES OF CAPITAL", 8.2, HOT, True)
    b += t(180, 233, "own savings · family · bank / MUDRA · angel / VC · schemes", 7.6, "#555555")
    return svg_doc("Anatomy of a business plan", "Card 2.3: the two plans inside the plan", 246, b)

def ent2_research():
    b, y = _flow([("1 · DEFINE THE QUESTION", "who might buy, what, at what price?"), ("2 · DESIGN QUESTIONNAIRE", "short, clear, pilot-tested"),
                  ("3 · CHOOSE THE SAMPLE", "representative, not just reachable"), ("4 · CONDUCT THE SURVEY", "interview, online or observation"),
                  ("5 · ANALYSE THE DATA", "tables, percentages, charts"), ("6 · DECIDE", "go · modify · drop — with evidence")])
    b += note(180, y + 8, "Each step removes a guess before money is committed")
    return svg_doc("Market research process", "Card 2.4: evaluation is a sequence, not a hunch", y + 12, b)

def ent2_4ps():
    b = ""
    items = [(180, 56, "PRODUCT", "features, quality, brand", HOT), (288, 138, "PRICE", "price, discounts, credit", CAT),
             (180, 220, "PLACE", "shop, dealers, online", STEEL), (72, 138, "PROMOTION", "ads, offers, selling", PUR)]
    for cx, cy, h, s, c in items:
        b += line(180, 140, cx, cy, "#CBAADE", 1.1)
    for cx, cy, h, s, c in items:
        b += rect(cx - 56, cy - 19, 112, 38, "#FFFFFF", c, 1.3, 6) + t(cx, cy - 2, h, 8.8, c, True) + t(cx, cy + 11, s, 7.2, "#555555")
    b += circ(180, 140, 36, "#FFFFFF", PUR, 1.8) + t(180, 136, "TARGET", 8.5, PUR, True) + t(180, 149, "CUSTOMER", 8.5, PUR, True)
    b += note(180, 262, "Segment first, target second — then build the four Ps to fit")
    return svg_doc("The marketing mix (4Ps)", "Card 2.5: one customer at the centre of four decisions", 270, b)

def ent2_plc():
    b = line(42, 232, 42, 52, "#666666", 1.3) + line(42, 232, 342, 232, "#666666", 1.3)
    b += t(342, 244, "time →", 8, "#666666") + t(30, 60, "sales", 8, "#666666")
    pts = [(48, 222), (100, 208), (150, 168), (200, 118), (246, 100), (282, 104), (316, 138), (338, 190)]
    for (x1, y1), (x2, y2) in zip(pts, pts[1:]):
        b += line(x1, y1, x2, y2, HOT, 2.2)
    prof = [(48, 228), (120, 224), (190, 196), (240, 176), (290, 184), (338, 214)]
    for (x1, y1), (x2, y2) in zip(prof, prof[1:]):
        b += line(x1, y1, x2, y2, STEEL, 1.4)
    b += t(250, 84, "sales", 8.5, HOT, True) + t(258, 168, "profit", 8.5, STEEL, True)
    for x, s in [(78, "Introduction"), (168, "Growth"), (262, "Maturity"), (322, "Decline")]:
        b += line(x, 232, x, 224, "#999999", 1.1) + t(x, 258, s, 7.6, "#555555")
    b += note(180, 282, "Mortality warning: most new products die in Introduction or early Growth")
    return svg_doc("Product Life Cycle and mortality", "Card 2.6: sales rise, level, and fall — survival is earned early", 290, b)

def ent2_swat():
    b = t(180, 54, "INTERNAL (about us)", 7.6, "#777777") + t(180, 132, "EXTERNAL (about the world)", 7.6, "#777777")
    cells = [(14, 62, "STRENGTHS", "skills, location, low cost", CAT), (184, 62, "WEAKNESSES", "little capital, no brand yet", HOT),
             (14, 140, "OPPORTUNITIES", "schemes, growing demand", STEEL), (184, 140, "THREATS", "new entrant, price war", PUR)]
    for x, y, h, s, c in cells:
        b += rect(x, y, 162, 56, "#FFFFFF", c, 1.4, 7) + t(x + 81, y + 21, h, 9.5, c, True) + t(x + 81, y + 40, s, 7.6, "#555555")
    b += note(180, 214, "Turn every box into an action: use, fix, capture, watch")
    return svg_doc("SWOT analysis", "Card 2.8: the risk map of the venture", 222, b)

DIAGRAMS = [
 ("ent2_pipeline", "From idea to start-up (Activity Map)", ent2_pipeline()),
 ("ent2_plan", "Anatomy of a business plan", ent2_plan()),
 ("ent2_research", "Market research process", ent2_research()),
 ("ent2_4ps", "The marketing mix (4Ps)", ent2_4ps()),
 ("ent2_plc", "Product Life Cycle and mortality curve", ent2_plc()),
 ("ent2_swat", "SWOT analysis", ent2_swat()),
]
