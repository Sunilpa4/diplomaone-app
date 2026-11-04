# -*- coding: utf-8 -*-
"""DI04000081 Unit 4 diagrams."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from equip_lib import *

def ent4_support():
    b = t(95, 56, "STATE LEVEL — nearest door", 9, STEEL, True) + t(265, 56, "NATIONAL LEVEL", 9, CAT, True)
    L = [("DIC", "district first stop: guidance, schemes"), ("Industries Commissionerate / GIDC", "policy, estates, state incentives"),
         ("CED Gujarat · EDII · i-Hub/SSIP", "training, student start-up support"), ("State finance / lead banks", "state-level finance arm")]
    R = [("Ministry of MSME · MSME-DI", "policy, facilitation, tool rooms"), ("NSIC · SIDBI · KVIC", "marketing, MSME finance, PMEGP"),
         ("DPIIT / Startup India", "recognition and start-up policy"), ("Flagship schemes", "PMEGP · MUDRA · CGTMSE · Stand-up India")]
    y = 66
    for h, s in L:
        b += rect(10, y, 170, 38, STEEL_F, STEEL, 1.2, 6) + t(95, y + 15, h, 7.9, STEEL, True) + t(95, y + 29, s, 7.0, "#555555"); y += 46
    y = 66
    for h, s in R:
        b += rect(180, y, 170, 38, CAT_F, CAT, 1.2, 6) + t(265, y + 15, h, 7.9, CAT, True) + t(265, y + 29, s, 7.0, "#555555"); y += 46
    b += note(180, y + 8, "Agencies inform, train, guarantee and co-fund — only customers sell the product")
    return svg_doc("The support ecosystem", "Card 4.1: state and national agencies around the founder", y + 14, b)

def ent4_incubation():
    b = ""; y = 48
    steps = [("PRE-INCUBATION", "idea &amp; prototype — students welcome (SSIP)", PUR), ("INCUBATION", "product, first customers, company set-up", CAT),
             ("ACCELERATION", "short intense growth push for selling ventures", HOT), ("GRADUATION", "own premises, follow-on funding, alumni network", STEEL)]
    for i, (h, s, c) in enumerate(steps):
        b += rect(45, y, 270, 34, "#FFFFFF", c, 1.3, 7) + t(180, y + 14, h, 8.8, c, True) + t(180, y + 27, s, 7.3, "#555555")
        if i < len(steps) - 1: b += pipe([(180, y + 34), (180, y + 44)])
        y += 46
    b += rect(25, y + 2, 310, 34, "#F3EAF9", PUR, 1.2, 7) + t(180, y + 15, "THE SHELTER THROUGHOUT", 8.2, PUR, True)
    b += t(180, y + 29, "space · mentors · legal/IPR help · investor access · scheme guidance", 7.3, "#555555")
    return svg_doc("The incubation journey", "Card 4.2: from fragile idea to independent venture", y + 44, b)

def ent4_pitch():
    b = ""
    items = [("1 PROBLEM", "pain worth paying for"), ("2 SOLUTION", "your answer, simply"), ("3 PRODUCT", "show it working"), ("4 MARKET", "big enough, reachable"),
             ("5 MODEL", "how money is made"), ("6 TRACTION", "sales, users, pilots"), ("7 EDGE", "vs competition"), ("8 TEAM", "why you can do it"),
             ("9 FINANCIALS", "numbers + assumptions"), ("10 THE ASK", "how much, for what")]
    pos = [(66, 84), (180, 84), (294, 84), (66, 140), (180, 140), (294, 140), (66, 196), (180, 196), (294, 196), (180, 252)]
    for (h, s), (cx, cy) in zip(items, pos):
        b += rect(cx - 54, cy - 21, 108, 42, "#FFFFFF", STEEL, 1.2, 6) + t(cx, cy - 3, h, 8.0, STEEL, True) + t(cx, cy + 11, s, 7.0, "#555555")
    b += note(180, 288, "Investors buy a share of a growing business — not a product demo")
    return svg_doc("The 10-slide investor pitch", "Card 4.3: the standard story, in order", 296, b)

def ent4_ipr():
    b = ""
    cells = [(10, 50, "PATENT", "new invention", "20 yrs from filing", HOT), (182, 50, "TRADEMARK", "brand name, logo", "10 yrs, renewable", CAT),
             (10, 148, "COPYRIGHT", "code, designs, content", "life + 60 years", STEEL), (182, 148, "TRADE SECRET", "recipes, know-how", "while kept secret", PUR)]
    for x, y, h, s, term, c in cells:
        b += rect(x, y, 168, 84, "#FFFFFF", c, 1.3, 7) + t(x + 84, y + 24, h, 9.2, c, True) + t(x + 84, y + 44, s, 7.6, "#555555") + t(x + 84, y + 62, term, 7.6, c, True)
    b += rect(40, 244, 280, 30, "#FFF7E8", HOT, 1.2, 7) + t(180, 256, "LICENSING", 8.4, HOT, True) + t(180, 269, "rent out your IP for royalty — protection that also earns", 7.3, "#555555")
    b += note(180, 288, "Terms are indicative — verify current law before filing")
    return svg_doc("Intellectual property at a glance", "Card 4.4: four protections, four different jobs", 296, b)

DIAGRAMS = [
 ("ent4_support", "State and national support ecosystem", ent4_support()),
 ("ent4_incubation", "The incubation journey", ent4_incubation()),
 ("ent4_pitch", "The 10-slide investor pitch", ent4_pitch()),
 ("ent4_ipr", "Intellectual property rights at a glance", ent4_ipr()),
]
