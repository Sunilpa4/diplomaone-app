# -*- coding: utf-8 -*-
"""Build DI04000081 Unit 1: subject.json + unit1.json + diagrams.
Format for this subject (owner instruction): Notes, Diagrams, Exam questions only."""
import json, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))
from equip_lib import *
from content_DI04000081_u1 import NOTES, INTRO_EN, INTRO_GU, CO_INDEX

def tr(en, gu): return {"en": en, "gu": gu}
CODE = "DI04000081"
SUBJ_DIR = ROOT / "content/common/sem4/DI04000081"

# ------------------------------------------------------------------ diagrams
def _box(cx, cy, w, h, head, sub, color, fill):
    b = rect(cx - w/2, cy - h/2, w, h, fill, color, 1.3, 6)
    b += t(cx, cy - 1, head, 8.6, color, True)
    if sub: b += t(cx, cy + 11, sub, 7.2, "#555555")
    return b

def ent1_traits():
    b = ""
    items = [(180, 56, "Need for achievement", ""), (62, 98, "Innovation", "new ways to create value"),
             (298, 98, "Calculated risk", "assessed, not blind"), (62, 216, "Leadership", "decides and carries people"),
             (298, 216, "Opportunity focus", "sees gaps others miss"), (180, 258, "Perseverance", "and self-confidence")]
    for cx, cy, h, s in items:
        b += line(180, 158, cx, cy, "#B9A8D9", 1.1)
    for cx, cy, h, s in items:
        b += _box(cx, cy, 116, 34, h, s, PUR, PUR_F)
    b += circ(180, 158, 37, "#FFFFFF", PUR, 1.8)
    b += t(180, 162, "ENTREPRENEUR", 8, PUR, True)
    b += note(180, 292, "Traits are tendencies that can be developed — that is why this course exists")
    return svg_doc("Traits of an entrepreneur", "Card 1.1: the person at the centre of the venture", 300, b)

def ent1_functions():
    b = rect(16, 128, 116, 58, STEEL_F, STEEL, 1.5, 6) + t(74, 152, "Entrepreneur", 9.5, STEEL, True) + t(74, 165, "starts a venture", 7.5, "#555555")
    rows = [("Job creation", "self-employment, then hiring others", CAT),
            ("Innovation", "new products, processes, markets", HOT),
            ("Inspiration", "visible success creates more founders", PUR),
            ("Economic development", "capital, tax revenue, regional growth", GAS)]
    y = 52
    for h, s, c in rows:
        b += pipe([(132, 157), (158, y + 17), (176, y + 17)], marker="ahG" if c == CAT else "ah")
        b += _box(262, y + 17, 172, 34, h, s, c, "#FFFFFF")
        y += 46
    b += pipe([(262, 240), (262, 260), (74, 260), (74, 190)], color=CAT, dash="5,3", marker="ahG")
    b += t(180, 276, "jobs, taxes and role models feed the next generation of founders", 8, CAT, style := False) if False else t(180, 276, "jobs, taxes and role models feed the next founders", 8, CAT)
    return svg_doc("Functions of entrepreneurship", "Card 1.2: what a venture gives society beyond profit", 286, b)

def ent1_structures():
    b = ""
    rows = [("Sole proprietorship", "1 owner · unlimited liability · simplest start", HOT),
            ("Partnership firm", "2+ partners · unlimited, joint liability · deed-based", HOT),
            ("LLP", "2+ partners · liability limited to contribution", STEEL),
            ("One-Person Company", "1 founder · limited liability · separate identity", STEEL),
            ("Private limited company", "2+ members · limited liability · can raise investment", CAT),
            ("Co-operative society", "member collective · democratic ownership", PUR)]
    pos = [(93, 76), (267, 76), (93, 140), (267, 140), (93, 204), (267, 204)]
    for (h, s, c), (cx, cy) in zip(rows, pos):
        name, _, rest = s.partition(" · ")
        b += rect(cx - 81, cy - 26, 162, 52, "#FFFFFF", c, 1.3, 6)
        b += t(cx, cy - 8, h, 8.8, c, True)
        b += t(cx, cy + 6, s.split("·")[0].strip() + " ·", 7.2, "#555555")
        b += t(cx, cy + 18, "· ".join(s.split("·")[1:]).strip(), 7.2, "#555555")
    b += note(180, 246, "More protection and fundability usually mean more compliance")
    return svg_doc("Types of business structures", "Card 1.5: who owns it, and who bears the risk", 254, b)

def ent1_7m():
    b = ""
    items = [(180, 50, "Man", "people and skills"), (286, 88, "Money", "capital and credit"),
             (302, 168, "Materials", "inputs and supply"), (254, 240, "Machines", "plant and tools"),
             (106, 240, "Methods", "process and know-how"), (58, 168, "Markets", "customers and demand"),
             (74, 88, "Management", "organises the other six")]
    for cx, cy, h, s in items:
        b += line(180, 160, cx, cy, "#B9A8D9", 1.1)
    for cx, cy, h, s in items:
        b += _box(cx, cy, 104, 36, h, s, STEEL, STEEL_F)
    b += circ(180, 160, 38, "#FFFFFF", PUR, 1.8)
    b += t(180, 156, "NEW", 9, PUR, True) + t(180, 168, "ENTERPRISE", 8.5, PUR, True)
    b += note(180, 292, "A plan silent about any one M has found its likely failure point")
    return svg_doc("The 7-M resources", "Card 1.7: everything a venture must assemble", 300, b)

def ent1_udyam():
    b = ""
    b += t(95, 56, "UDYAM — for every MSME", 9.5, STEEL, True) + t(265, 56, "DPIIT — for start-ups", 9.5, CAT, True)
    L = [("1 · Open the official portal", "udyamregistration.gov.in — free"), ("2 · Enter enterprise details", "Aadhaar-linked; PAN/GST as applicable"),
         ("3 · Online verification", "no documents to upload, no fee"), ("4 · Udyam certificate issued", "permanent registration number")]
    R = [("1 · Incorporate the entity", "Pvt Ltd company / LLP / partnership"), ("2 · Apply on Startup India portal", "with a brief on the innovation"),
         ("3 · Eligibility examined", "age, turnover and innovation tests"), ("4 · DPIIT recognition issued", "certificate and recognition number")]
    y = 74
    for (h, s) in L:
        b += _box(95, y + 18, 168, 38, h, s, STEEL, STEEL_F); y += 48
    y = 74
    for (h, s) in R:
        b += _box(265, y + 18, 168, 38, h, s, CAT, CAT_F); y += 48
    b += note(180, 282, "SSIP and i-Hub Gujarat support student innovators before either registration")
    return svg_doc("Registering the enterprise", "Cards 1.8–1.9: two gateways, one pipeline", 290, b)

DIAGRAMS = [
 ("ent1_traits", "Traits of an entrepreneur", ent1_traits()),
 ("ent1_functions", "Functions of entrepreneurship", ent1_functions()),
 ("ent1_structures", "Types of business structures", ent1_structures()),
 ("ent1_7m", "The 7-M resources of an enterprise", ent1_7m()),
 ("ent1_udyam", "Udyam and DPIIT registration", ent1_udyam()),
]

# ---------------------------------------------------------------------- exam
_PRACTICE = [
 ("Practice: Define the term 'entrepreneur' and explain any six traits of a successful entrepreneur.", "Practice: 'Entrepreneur' શબ્દની વ્યાખ્યા આપો અને સફળ entrepreneur ના કોઈ છ traits સમજાવો.", 7),
 ("Practice: Explain the four functions of entrepreneurship: job creation, innovation, inspiration and economic development.", "Practice: Entrepreneurship ના ચાર functions સમજાવો: job creation, innovation, inspiration તથા economic development.", 7),
 ("Practice: Classify entrepreneurship by venture type and by the entrepreneur's behaviour, writing one line on each type.", "Practice: Entrepreneurship નું venture type તથા entrepreneur ના વર્તન મુજબ classification કરો, દરેક પ્રકાર પર એક line લખીને.", 4),
 ("Practice: What is intrapreneurship? State what motivates (a) organisations and (b) employees to practise it.", "Practice: Intrapreneurship શું છે? (a) organisations તથા (b) employees ને તે practice કરવા શું પ્રેરે છે તે જણાવો.", 4),
 ("Practice: Compare sole proprietorship, partnership firm and private limited company on owners, liability and suitability.", "Practice: Sole proprietorship, partnership firm તથા private limited company ની માલિકો, જવાબદારી તથા યોગ્યતા પર સરખામણી કરો.", 7),
 ("Practice: State four differences and two similarities between an entrepreneur and a manager.", "Practice: Entrepreneur તથા manager વચ્ચે ચાર તફાવત તથા બે સામ્યતાઓ જણાવો.", 4),
 ("Practice: Explain the 7-M resources that a new enterprise must assemble.", "Practice: નવા enterprise એ ભેગા કરવા પડતા 7-M resources સમજાવો.", 4),
 ("Practice: Give the MSME classification by investment and turnover, describe the Udyam registration process, and state what Startup India, Stand-up India and SSIP each provide.", "Practice: Investment તથા turnover મુજબ MSME classification આપો, Udyam registration process વર્ણવો, અને Startup India, Stand-up India તથા SSIP દરેક શું પૂરું પાડે છે તે જણાવો.", 7),
]
EXAM = [{"q": tr(en, gu), "marks": m} for (en, gu, m) in _PRACTICE]

SOURCES = [
 {"title": "Coulter, M. — Entrepreneurship in Action, PHI (GTU syllabus book 1)", "url": ""},
 {"title": "Gordon, E. & Natarajan, K. — Entrepreneurship Development, Himalaya Publishing (GTU syllabus book 2)", "url": ""},
 {"title": "Hisrich, R. D. & Manimala, M. J. — Entrepreneurship, McGraw Hill (GTU syllabus book 3)", "url": ""},
 {"title": "Khanka, S. S. — Entrepreneurial Development, S. Chand (GTU syllabus book 4)", "url": ""},
 {"title": "Charantimath, P. M. — Entrepreneurship Development & Small Business Enterprise, Pearson (GTU syllabus book 12)", "url": ""},
 {"title": "Desai, V. — Small Scale Industries and Entrepreneurship, Himalaya Publishing (GTU syllabus book 7)", "url": ""},
 {"title": "Startup India (DPIIT) — official portal (GTU syllabus open-source link)", "url": "https://www.startupindia.gov.in/"},
 {"title": "Udyam Registration, Ministry of MSME — official free portal", "url": "https://udyamregistration.gov.in/"},
 {"title": "SSIP Gujarat (Student Startup and Innovation Policy)", "url": "https://www.ssipgujarat.in/"},
]

# -------------------------------------------------------------------- subject
SUBJECT = {
 "code": CODE, "name": tr("Entrepreneurship & Start-up", "એન્ટ્રપ્રિન્યોરશિપ અને સ્ટાર્ટ-અપ"),
 "branch": "common", "common_to_all_branches": True, "semester": 4, "syllabus_year": "2025-26",
 "category": "MOPEC", "type": "theory", "languages": ["en", "gu"], "code_lang": None,
 "teaching": {"lecture": 3, "tutorial": 0, "practical": 0},
 "exam": {"theory_ese": 70, "theory_pa": 30, "practical_pa": 0, "practical_ese": 0, "total": 100, "credits": 3},
 "prerequisites": [],
 "units": [
  {"no": 1, "title": tr("Introduction to Entrepreneurship and Start-Ups", "Entrepreneurship તથા Start-Ups નો પરિચય"), "hours": 9, "weightage": 20,
   "topics": ["1.1 Definition, Traits of an entrepreneur", "1.2 Functions of Entrepreneurship - Job Creation, Innovation, Inspiration, Economic Development", "1.3 Types of Entrepreneurship", "1.4 Motivation for Intrapreneurship", "1.5 Types of Business Structures", "1.6 Similarities and differences between entrepreneurs and managers", "1.7 7-M Resources", "1.8 Micro, Small, Medium Enterprise/MSME - Industry Registration Process", "1.9 Startup India, Standup India and SSIP Gujarat & Startup registration process"], "file": "unit1.json"},
  {"no": 2, "title": tr("Business Ideas & their Implementation (Idea to Start-up)", "Business Ideas અને તેમનો અમલ (Idea to Start-up)"), "hours": 9, "weightage": 20,
   "topics": ["2.1-2.2 Discovering ideas, visualizing the business, Activity map, Idea Generation, Product Identification", "2.3 Business Plan - Marketing Plan & Financial Plan / Sources of Capital", "2.4 Business opportunity identification & evaluation - Market research, Questionnaire design, Sampling, Market survey, Data analysis & interpretation", "2.5 Marketing Mix (4Ps) - target market, Competition evaluation & Strategy, Segmentation, Advertising & Branding, Digital Marketing, B2B, E-commerce and GeM", "2.6 Product terms - PLC, Mortality Curve, New product Development steps, Inventory, Supply Chain Management", "2.7 Innovation - importance, concept, sources & process", "2.8 Risk analysis & mitigation by SWOT Analysis"], "file": None},
  {"no": 3, "title": tr("Management Practices", "વ્યવસ્થાપન પદ્ધતિઓ (Management Practices)"), "hours": 12, "weightage": 27,
   "topics": ["3.1 Industry, Commerce and Business", "3.2 Types of ownership in the organization - Characteristics, Merits & Demerits", "3.3 Different Leadership Models", "3.4 Functions of Management - Planning, Company's Organization Structure, Directing, Controlling, Staffing (Recruitment & management of talent)", "3.5 Financial organization and management", "3.6 Differences between Management and Administration"], "file": None},
  {"no": 4, "title": tr("Support Agencies and Incubators", "Support Agencies તથા Incubators"), "hours": 8, "weightage": 18,
   "topics": ["4.1 State & National Level Support agencies and Current Promotional Schemes for new Enterprise", "4.2 Start-up Incubation and modalities", "4.3 Communication of Ideas to potential investors - Investor Pitch", "4.4 Legal Issues - Contracts, Copyrights, Insurance, IPR, Licensing, Patents, Trade Secrets, Trademarks"], "file": None},
  {"no": 5, "title": tr("Project Proposal & Exit Strategies", "Project Proposal તથા Exit Strategies"), "hours": 7, "weightage": 15,
   "topics": ["5.1 Project Planning - project report, Feasibility study, Project cost estimation, Breakeven point, Return on investment & Return on sales", "5.2 Corporate Social Responsibilities & Economic Performance", "5.3 Business Ethics", "5.4 Ex-Im policies", "5.5 Succession and harvesting strategy", "5.6 Bankruptcy and avoidance"], "file": None},
 ],
 "course_outcomes": [
  tr("CO1: Understanding the dynamic role of entrepreneurship and Startups by acquiring entrepreneurial spirit, resourcefulness, quality, competency, and motivation (RBT: R, U, A)", "CO1: Entrepreneurial spirit, resourcefulness, quality, competency તથા motivation કેળવી entrepreneurship તથા Startups ની dynamic ભૂમિકા સમજવી (RBT: R, U, A)"),
  tr("CO2: Identify a Business Idea and implement it (RBT: R, U, A)", "CO2: Business Idea ઓળખવો અને તેનો અમલ કરવો (RBT: R, U, A)"),
  tr("CO3: Select suitable Management practices like leadership and Ownership, resource institutes (RBT: R, U, A)", "CO3: Leadership તથા Ownership જેવી યોગ્ય Management practices પસંદ કરવી (RBT: R, U, A)"),
  tr("CO4: Overview of Support Agencies and Incubators (RBT: R, U)", "CO4: Support Agencies તથા Incubators ની ઝાંખી (RBT: R, U)"),
  tr("CO5: Building Project Proposal & knowing CSR, Ethics, Ex-Im, & Exit strategies (RBT: R, U, A)", "CO5: Project Proposal બનાવવો તથા CSR, Ethics, Ex-Im, અને Exit strategies જાણવી (RBT: R, U, A)")],
 "theory_rbt_percent": {"R": 35, "U": 32, "A": 33},
 "practicals": [],
 "suggested_projects": ["Entrepreneur Traits and Behavior Modelling", "State and Central Entrepreneurship Promotional Schemes and Start-up Policies", "Business Model for a Startup and study of Unicorns", "Make your own Product/Service portfolio/Proposal with USP, logo, advertisement, jingle, packaging, labelling and branding", "Work as a leader/a team member (micro-project)", "Practice ethics and waste-reduction/environment-conserving methods in designing a new business till commercialization"],
 "books": [
  {"title": "Entrepreneurship in Action — Coulter, PHI"}, {"title": "Entrepreneurship Development — Gordon & Natarajan, Himalaya"},
  {"title": "Entrepreneurship — Hisrich & Manimala, McGraw Hill"}, {"title": "Entrepreneurial Development — Khanka, S. Chand"},
  {"title": "Small Scale Industries and Entrepreneurship — Desai, Himalaya"}, {"title": "Entrepreneurship — Rajeev Roy, Oxford"},
  {"title": "Entrepreneurship Development & Small Business Enterprise — Charantimath, Pearson"}, {"title": "Industrial Engineering & Management — O.P. Khanna, Dhanpat Rai"}],
 "source_note": "Official GTU syllabus DI04000081 (w.e.f. 2025-26), 8 pages, uploaded by the owner; text copy in tools/syllabus_DI04000081.txt.",
 "source_discrepancies": ["Theory RBT table in the official PDF gives R=35, U=32, A=33 and dashes for N, E, C; recorded exactly as printed.", "The official PDF shows no practical component (PR=0, PA(I)=0, ESE(V)=0); the syllabus instead lists suggested projects and student activities, which the notes use as guided activities."],
 "available_units": [1],
}

# ----------------------------------------------------------------------- unit
unit = {
 "subject": CODE, "unit": 1, "format": "notes",
 "title": SUBJECT["units"][0]["title"], "hours": 9, "weightage": 20, "languages": ["en", "gu"],
 "tabs": ["notes", "diagrams", "exam"],
 "tab_labels": {},
 "intro_text": {"en": INTRO_EN, "gu": INTRO_GU},
 "notes": NOTES,
 "diagrams": [{"id": i, "title": tr(t, t), "file": f"diagrams/{i}.svg"} for (i, t, _s) in DIAGRAMS],
 "numericals": [], "syntax": [], "viva": [],
 "exam_questions": EXAM,
 "practicals": [], "practical_numbers": [],
 "learning_outcomes": [SUBJECT["course_outcomes"][i] for i in CO_INDEX],
 "content_kind": "theory_with_guided_activities",
 "assessment_note": tr("Official scheme (GTU DI04000081): Theory ESE 70 + PA 30, total 100 marks, 3 credits, no practical examination. Unit 1 carries 9 hours and 20 % weightage in the official syllabus. All exam questions in this unit are original practice questions; their marks are suggested, not from an official paper.",
                       "સત્તાવાર scheme (GTU DI04000081): Theory ESE 70 + PA 30, કુલ 100 marks, 3 credits, કોઈ practical examination નથી. Unit 1 ને સત્તાવાર syllabus માં 9 hours તથા 20 % weightage છે. આ unit ના બધા exam questions original practice questions છે; તેમના marks suggested છે, સત્તાવાર paper માંથી નથી."),
 "question_provenance": "Original revision questions; not official past papers",
 "question_marks_are_suggested": True,
 "lesson_count": sum(len(s["items"]) for s in NOTES),
 "answered_practice_count": 0,
 "sources": SOURCES,
}

def main():
    (SUBJ_DIR / "diagrams").mkdir(parents=True, exist_ok=True)
    for (did, _t, svg) in DIAGRAMS:
        (SUBJ_DIR / "diagrams" / f"{did}.svg").write_text(svg, encoding="utf-8")
    (SUBJ_DIR / "subject.json").write_text(json.dumps(SUBJECT, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    (SUBJ_DIR / "unit1.json").write_text(json.dumps(unit, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(f"wrote subject.json + unit1.json ({(SUBJ_DIR/'unit1.json').stat().st_size/1024:.1f} KB) | cards={unit['lesson_count']} diagrams={len(DIAGRAMS)} exam={len(EXAM)}")

if __name__ == "__main__":
    main()
