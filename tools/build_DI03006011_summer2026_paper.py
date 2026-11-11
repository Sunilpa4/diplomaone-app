#!/usr/bin/env python3
from pathlib import Path
import html
ROOT=Path(__file__).resolve().parent.parent
def load_svg(name):
    p=ROOT/f"content/civil/sem3/DI03006011/diagrams/{name}"
    return p.read_text(encoding="utf-8") if p.exists() else ""
CSS=""":root{--ink:#20252d;--muted:#65717d;--blue:#0b5b6a;--line:#d9e1e7;--paper:#f7f9fb;--purple:#58316f}
*{box-sizing:border-box}body{margin:0;background:var(--paper);color:var(--ink);font:16px/1.65 system-ui,-apple-system,"Segoe UI",Arial,sans-serif}
.page{width:min(1000px,calc(100% - 32px));margin:26px auto 70px}
.hero{background:#fff;border:1px solid var(--line);border-radius:16px;padding:26px;margin-bottom:24px}
.eyebrow{color:var(--blue);font-size:.78rem;font-weight:800;letter-spacing:.08em;text-transform:uppercase}
.hero h1{font-size:clamp(1.5rem,4vw,2.25rem);line-height:1.2;margin:.45rem 0}
.meta{color:var(--muted);font-size:.9rem}
.group{margin:30px 0}.group h2{font-size:1.35rem;color:var(--blue);margin:0 0 10px}
.card{background:#fff;border:1px solid var(--line);border-radius:10px;margin:10px 0;overflow:hidden}
.card summary{cursor:pointer;padding:15px 17px;color:#164f73;display:flex;gap:10px;align-items:baseline;flex-wrap:wrap}
.card summary strong{flex:1;min-width:220px}.card summary small{font-size:.78rem;color:var(--muted);white-space:nowrap}
.answer{border-top:1px solid var(--line);padding:18px 20px;overflow-wrap:anywhere}
.answer p{margin:9px 0}.answer li{margin:5px 0}.answer ul,.answer ol{padding-left:1.35rem}
.eq{font-family:Georgia,serif;font-size:1.04rem;background:#f4f7f9;border-left:3px solid #7caac5;padding:9px 12px;margin:11px 0;overflow-x:auto}
.answer table{border-collapse:collapse;width:100%;font-size:.93rem;margin:12px 0}
.answer th,.answer td{border:1px solid #d4dde4;padding:8px;vertical-align:top;text-align:left}
.answer th{background:#edf5f9}
figure{margin:16px auto;max-width:780px}figure svg{display:block;width:100%;height:auto;background:#fff;border:1px solid var(--line);border-radius:8px}
figcaption{font-size:.8rem;color:var(--muted);margin-top:5px}
.footer{font-size:.82rem;color:var(--muted);border-top:1px solid var(--line);margin-top:36px;padding-top:14px}
.lang-switch{display:flex;gap:8px;margin:12px 0}.lang-switch button{border:1px solid #c9b9d1;background:#fff;color:var(--purple);border-radius:20px;padding:7px 13px;font-weight:700;cursor:pointer;font:inherit;font-size:.85rem}
.lang-switch button[aria-pressed="true"]{background:var(--purple);color:#fff}
html[lang="en"] .gu{display:none!important}html[lang="gu"] .en{display:none!important}
:lang(gu){font-family:"Noto Sans Gujarati","Shruti","Nirmala UI",system-ui,sans-serif;line-height:1.85}
@media(max-width:600px){.page{width:calc(100% - 20px);margin-top:10px}.hero{padding:19px}.answer{padding:14px}}
"""
def fig(svg,caption): return f'<figure>{svg}<figcaption>{html.escape(caption)}</figcaption></figure>'
svg_scaffold=load_svg("ct3_scaffold.svg")
svg_found=load_svg("ct2_found.svg")
svg_setout=load_svg("ct2_setout.svg")
svg_ureamed=load_svg("ct2_ureamed.svg")
svg_types=load_svg("ct1_types.svg")
svg_frame=load_svg("ct1_frame.svg")
svg_bonds=load_svg("ct3_bonds.svg")
svg_dpc=load_svg("ct3_dpc.svg")
svg_batch=load_svg("ct4_batch.svg")
svg_backhoe=load_svg("ct4_backhoe.svg")
svg_class=load_svg("ct4_class.svg")
svg_rollers=load_svg("ct4_rollers.svg")
svg_excav=load_svg("ct5_excav.svg")
svg_ppe=load_svg("ct5_ppe.svg")
svg_fail=load_svg("ct5_fail.svg")
svg_modular=load_svg("ct6_modular.svg")
svg_map=load_svg("ct6_map.svg")
svg_print=load_svg("ct6_print.svg")
svg_wall=load_svg("ct1_wall.svg")

SECTIONS=[
{
 "title_en":"Q1 · Structures, load bearing vs framed, black cotton & settlement",
 "title_gu":"પ્ર.1 · સ્ટ્રક્ચર, ભારવાહી vs ફ્રેમ, કાળી માટી અને સેટલમેન્ટ",
 "cards":[
  {"q_en":"Q.1 (a) Enlist different types of civil engineering structures. (03 marks)","marks_en":"03 marks","marks_gu":"૦૩ ગુણ","a_en":"<p>Residential, commercial, industrial, dams, bridges, roads, tunnels, water supply, ports, airports.</p>"+fig(svg_types,"Types of civil structures"),
   "a_gu":"<p>રહેણાંક, કોમર્શિયલ, ડેમ, બ્રિજ, રસ્તા, ટનલ, પોર્ટ.</p>"+fig(svg_types,"બાંધકામ પ્રકાર")},
  {"q_en":"Q.1 (b) Differentiate : Load Bearing structure and Framed structure. (04 marks)","marks_en":"04 marks","marks_gu":"૦૪ ગુણ","a_en":"<table><tr><th>Load bearing</th><th>Framed</th></tr><tr><td>Walls transfer load</td><td>Frame transfers load walls infill</td></tr><tr><td>Limited stories, thick walls</td><td>High rise, open plan</td></tr></table>"+fig(svg_frame,"Load bearing vs framed"),
   "a_gu":"<p>ભારવાહી દિવાલ, ફ્રેમ કોલમ બીમ.</p>"+fig(svg_frame,"તફાવત")},
  {"q_en":"Q.1 (c) A site has black cotton soil with high swelling and shrinkage. As site engineer, which type of foundation would you recommend for single-storey residential? Justify. (07 marks)","marks_en":"07 marks","marks_gu":"૦૭ ગુણ","a_en":"<p><strong>Recommendation:</strong> Under-reamed pile or raft with granular cushion, plinth beam.</p><p>Black cotton swells on wet heaves, shrinks cracks. Deep under-reamed bulbs anchor below active zone 3-3.5m, resist uplift, granular fill breaks capillary, plinth beam ties.</p><p>Alternative: Strip raft with sand blanket + CNS layer if single storey low cost.</p>"+fig(svg_ureamed,"Under-reamed pile bulbs in black cotton soil"),
   "a_gu":"<p>Under-reamed pile 3m નીચે bulb, granular cushion, plinth beam — swelling નીચે anchor.</p>"+fig(svg_ureamed,"કાળી માટી પાયો")},
  {"q_en":"Q.1 (c) OR During construction differential settlement observed. Suggest remedial measures and how proper setting out could have prevented failure. (07 marks)","marks_en":"07 marks","marks_gu":"૦૭ ગુણ","a_en":"<p><strong>Remedial:</strong> Grouting, underpinning, jacketing, drainage, load reduction.</p><p><strong>Prevention by setting out:</strong> Correct centre line with pegs, offsets, right angle checks, diagonal verify, levels to avoid eccentric loading.</p>"+fig(svg_setout,"Foundation setting out centre lines pegs diagonal check")+fig(svg_fail,"Differential settlement remedial grouting underpinning"),
   "a_gu":"<p>Grouting underpinning drainage — center line peg diagonal check થી eccentric રોકાય.</p>"+fig(svg_setout,"સેટિંગ આઉટ")+fig(svg_fail,"સેટલમેન્ટ ઉપાય")},
 ]
},
{
 "title_en":"Q2 · Piles, shallow/deep, scaffolding, failure, setting out, joints",
 "title_gu":"પ્ર.2 · પાઇલ, shallow deep, પાલખ, નિષ્ફળતા, સેટિંગ, સાંધા",
 "cards":[
  {"q_en":"Q.2 (a) State purpose of an under-reamed pile (Any three). (03 marks)","marks_en":"03 marks","marks_gu":"૦૩ ગુણ","a_en":"<p>Anchor expansive soil, increase bearing by bulb, resist uplift, economical for black cotton, easy manual boring.</p>"+fig(svg_ureamed,"Under-reamed bulb increases bearing"),
   "a_gu":"<p>Expansive માટી anchor, bearing વધે, uplift રોકે.</p>"+fig(svg_ureamed,"હેતુ")},
  {"q_en":"Q.2 (b) Explain the difference between shallow and deep foundations with suitable examples. (04 marks)","marks_en":"04 marks","marks_gu":"૦૪ ગુણ","a_en":"<table><tr><th>Shallow Df≤B</th><th>Deep Df>B</th></tr><tr><td>Bearing on near strata, spread/raft</td><td>Transfer to deep hard, pile/caisson</td></tr><tr><td>Low rise good soil</td><td>High load weak top black cotton</td></tr></table>"+fig(svg_found,"Shallow spread vs deep pile"),
   "a_gu":"<p>Shallow નજીક strata, Deep ઊંડા hard — strip vs pile.</p>"+fig(svg_found,"તફાવત")},
  {"q_en":"Q.2 (c) A multi-storey building in congested area. Which type of scaffolding would you recommend and why. (07 marks)","marks_en":"07 marks","marks_gu":"૦૭ ગુણ","a_en":"<p><strong>Steel tubular independent double scaffolding.</strong> Narrow footprint, adjustable, strong, reusable, safe for high, needs less space than bamboo.</p>"+fig(svg_scaffold,"Double steel scaffolding for congested high building"),
   "a_gu":"<p>Steel double tubular — સાંકડી જગ્યા મજબૂત reusable.</p>"+fig(svg_scaffold,"ગીચ વિસ્તાર પાલખ")},
  {"q_en":"Q.2 (a) OR List causes of foundation failure. (03 marks)","marks_en":"03 marks","marks_gu":"૦૩ ગુણ","a_en":"<p>Poor investigation, swelling soil, scour, overloading, water table, poor drainage, nearby excavation.</p>"+fig(svg_fail,"Causes of foundation failure"),
   "a_gu":"<p>Investigation નબળું, swelling scour overloading.</p>"+fig(svg_fail,"કારણ")},
  {"q_en":"Q.2 (b) OR Explain how center lines are marked on site during foundation setting out. (04 marks)","marks_en":"04 marks","marks_gu":"૦૪ ગુણ","a_en":f"<p>Establish base line, use theodolite/tape, right angle by 3-4-5, pegs at corners, string, offset 1m for trench, check diagonals.</p>"+fig(svg_setout,"Centre line marking pegs strings offsets"),
   "a_gu":f"<p>Base line થી 3-4-5 કાટખૂણો peg string offset 1m diagonal check.</p>"+fig(svg_setout,"મધ્ય રેખા")},
  {"q_en":"Q.2 (c) OR A long concrete pavement being constructed. Which type of construction joint should be provided, and why? (07 marks)","marks_en":"07 marks","marks_gu":"૦૭ ગુણ","a_en":"<p><strong>Transverse expansion + contraction + longitudinal joints with dowels/tie bars.</strong> Concrete expands contracts temperature — prevents random cracks, load transfer via dowels.</p>",
   "a_gu":"<p>Expansion contraction longitudinal dowel tie bar — તાપમાન તિરાડ રોકે.</p>"},
 ]
},
{
 "title_en":"Q3 · Machinery: excavating vs hoisting, dam, plumbing-electrical, batch plant, highway, grouting",
 "title_gu":"પ્ર.3 · મશીનરી: ખોદકામ vs ઉંચક, ડેમ, પ્લમ્બિંગ-વિદ્યુત, બેચ પ્લાન્ટ, હાઇવે, ગ્રાઉટિંગ",
 "cards":[
  {"q_en":"Q.3 (a) Explain the difference between excavating machinery and hoisting machinery. (03 marks)","marks_en":"03 marks","marks_gu":"૦૩ ગુણ","a_en":"<p><strong>Excavating:</strong> Dig move earth — excavator, dozer, dragline, clam shell. <strong>Hoisting:</strong> Lift — crane, hoist, derrick, tower crane.</p>"+fig(svg_backhoe,"Excavator vs crane"),
   "a_gu":"<p>Excavating ખોદે dozer, Hoisting ઉંચકે crane.</p>"+fig(svg_backhoe,"તફાવત")},
  {"q_en":"Q.3 (b) A dam project requires large-scale earthwork. Which class of construction machinery will you recommend? (04 marks)","marks_en":"04 marks","marks_gu":"૦૪ ગુણ","a_en":"<p>Heavy earthmoving: excavators, scrapers, dozers, dumpers, rollers, dragline, batch plant for mass concrete.</p>"+fig(svg_class,"Earthwork machinery for dam"),
   "a_gu":"<p>Excavator scraper dozer dumper roller — mass earthwork.</p>"+fig(svg_class,"ડેમ મશીનરી")},
  {"q_en":"Q.3 (c) A two-storey house requires reliable water supply and safe wiring. Suggest suitable plumbing layout and type of electrical connection. (07 marks)","marks_en":"07 marks","marks_gu":"૦૭ ગુણ","a_en":"<p><strong>Plumbing:</strong> Overhead tank gravity, direct pump up, separate hot cold, vent. <strong>Electrical:</strong> Parallel wiring, separate circuits lights power, ELCB MCB earthing.</p>",
   "a_gu":"<p>Overhead tank gravity plumbing, parallel wiring MCB ELCB earthing.</p>"},
  {"q_en":"Q.3 (a) OR Explain the working of a batch mix plant for concrete production. (03 marks)","marks_en":"03 marks","marks_gu":"૦૩ ગુણ","a_en":f"<p>Aggregates weighed in hoppers, cement weighed, water dosed, mixed in drum, discharged to transit mixer.</p>"+fig(svg_batch,"Batch mix plant hoppers weigh mixer"),
   "a_gu":f"<p>Hopper weigh mixer transit — આકૃતિ.</p>"+fig(svg_batch,"બેચ પ્લાન્ટ")},
  {"q_en":"Q.3 (b) OR A highway project requires excavation, transportation, compaction, and laying of bituminous concrete. Suggest suitable machineries for each stage. (04 marks)","marks_en":"04 marks","marks_gu":"૦૪ ગુણ","a_en":"<p>Excavation excavator/dozer, transport dumper, compaction vibratory roller, laying paver finisher.</p>"+fig(svg_rollers,"Excavator dumper roller paver"),
   "a_gu":"<p>Excavator dumper roller paver.</p>"+fig(svg_rollers,"હાઇવે તબક્કા")},
  {"q_en":"Q.3 (c) OR A water retaining structure has developed leakage cracks. Which method (grouting or guniting) would you suggest and why? (07 marks)","marks_en":"07 marks","marks_gu":"૦૭ ગુણ","a_en":"<p><strong>Grouting</strong> for deep cracks voids under pressure — cement/epoxy. Guniting for surface coating. Water retaining needs pressure sealing grouting, then guniting protective layer.</p>",
   "a_gu":"<p>Leakage deep તો grouting pressure, surface coating guniting.</p>"},
 ]
},
{
 "title_en":"Q4 · Wiring, dampness, bonds, joints, concrete, w/c ratio",
 "title_gu":"પ્ર.4 · વાયરિંગ, ભીનાશ, બોન્ડ, સાંધા, કોંક્રિટ",
 "cards":[
  {"q_en":"Q.4 (a) Explain the difference between series wiring and parallel wiring in electrification. (03 marks)","marks_en":"03 marks","marks_gu":"૦૩ ગુણ","a_en":"<p><strong>Series:</strong> One path failure kills all, voltage divides. <strong>Parallel:</strong> Each independent full voltage, reliable for buildings.</p>",
   "a_gu":"<p>Series એક fail બધા બંધ, parallel દરેક independent.</p>"},
  {"q_en":"Q.4 (b) List sources of dampness in buildings (Any four). (04 marks)","marks_en":"04 marks","marks_gu":"૦૪ ગુણ","a_en":"<p>Rain penetration, rising moisture capillary, condensation, leaking pipes, poor drainage, groundwater.</p>"+fig(svg_dpc,"Sources of dampness"),
   "a_gu":"<p>વરસાદ capillary condensation pipe leak.</p>"+fig(svg_dpc,"ભીનાશ સ્ત્રોત")},
  {"q_en":"Q.4 (c) Explain the difference between English bond and Flemish bond. (07 marks)","marks_en":"07 marks","marks_gu":"૦૭ ગુણ","a_en":f"<p><strong>English:</strong> Alternate courses header/stretcher strong. <strong>Flemish:</strong> Each course header stretcher alternate attractive but weaker.</p>"+fig(svg_bonds,"English vs Flemish bond"),
   "a_gu":f"<p>English કોર્સ બદલે header stretcher, Flemish દરેક કોર્સ મિશ્ર સુંદર.</p>"+fig(svg_bonds,"બોન્ડ તફાવત")},
  {"q_en":"Q.4 (a) OR Explain the difference between expansion joints and contraction joints. (03 marks)","marks_en":"03 marks","marks_gu":"૦૩ ગુણ","a_en":"<p>Expansion allows expansion with filler gap, contraction weakens to control cracking, filler optional.</p>",
   "a_gu":"<p>Expansion gap filler, contraction crack control.</p>"},
  {"q_en":"Q.4 (b) OR List the main ingredients of concrete. (04 marks)","marks_en":"04 marks","marks_gu":"૦૪ ગુણ","a_en":"<p>Cement, fine aggregate, coarse aggregate, water, admixtures.</p>",
   "a_gu":"<p>સિમેન્ટ રેતી કપચી પાણી admixture.</p>"},
  {"q_en":"Q.4 (c) OR Explain why water-cement ratio is important in concrete mix design. (07 marks)","marks_en":"07 marks","marks_gu":"૦૭ ગુણ","a_en":"<p>Controls strength workability durability permeability. Abrams law strength inverse to w/c too high segregation too low incomplete hydration.</p>",
   "a_gu":"<p>w/c strength workability durability નક્કી — વધારે segregation ઓછું hydration અધૂરું.</p>"},
 ]
},
{
 "title_en":"Q5 · Accidents, safety, advanced tech, PPE, scaffolding, drones",
 "title_gu":"પ્ર.5 · અકસ્માત, સલામતી, નવી ટેક, PPE, પાલખ, ડ્રોન",
 "cards":[
  {"q_en":"Q.5 (a) List any common causes of construction accidents. (03 marks)","marks_en":"03 marks","marks_gu":"૦૩ ગુણ","a_en":"<p>Falls, collapse, electrical, struck by object, faulty PPE, poor training.</p>"+fig(svg_fail,"Common causes falls collapse electrical"),
   "a_gu":"<p>પડવું collapse electric PPE નહીં.</p>"+fig(svg_fail,"અકસ્માત કારણ")},
  {"q_en":"Q.5 (b) You are a site supervisor; how would you ensure safety compliance during concreting work? (04 marks)","marks_en":"04 marks","marks_gu":"૦૪ ગુણ","a_en":"<p>PPE, formwork check, vibrator safe, barricades, no overloading, first aid, toolbox talk.</p>",
   "a_gu":"<p>PPE formwork check barricade toolbox talk.</p>"},
  {"q_en":"Q.5 (c) Explain how the use of advanced technologies reduces cost and time in construction projects. (07 marks)","marks_en":"07 marks","marks_gu":"૦૭ ગુણ","a_en":"<p>BIM 4D planning, prefab, 3D printing, drones, IoT sensors — clash detection, faster erection, less rework.</p>"+fig(svg_modular,"BIM prefab 3D printing drones save time cost"),
   "a_gu":"<p>BIM prefab drone IoT — rework ઓછું સમય ખર્ચ ઘટે.</p>"+fig(svg_modular,"નવી ટેક")},
  {"q_en":"Q.5 (a) OR Name any three personal protective equipment (PPE). (03 marks)","marks_en":"03 marks","marks_gu":"૦૩ ગુણ","a_en":"<p>Helmet, safety shoes, harness, goggles, gloves, ear plug.</p>"+fig(svg_ppe,"PPE helmet harness shoes"),
   "a_gu":"<p>Helmet harness shoes goggles.</p>"+fig(svg_ppe,"PPE")},
  {"q_en":"Q.5 (b) OR A worker is assigned to work on scaffolding at 10 m height. Which safety equipment will you provide, and why? (04 marks)","marks_en":"04 marks","marks_gu":"૦૪ ગુણ","a_en":"<p>Full body harness anchor, helmet, guardrails toe boards, nets, safe ladder.</p>",
   "a_gu":"<p>Harness helmet guardrail net ladder.</p>"},
  {"q_en":"Q.5 (c) OR Explain how drones are useful for surveying large construction sites. (07 marks)","marks_en":"07 marks","marks_gu":"૦૭ ગુણ","a_en":f"<p>Aerial mapping, stockpile volume, progress monitoring, safety inspection without scaffold, fast large area.</p>"+fig(svg_map,"Drone surveying large site"),
   "a_gu":f"<p>Aerial mapping progress safety ઝડપી.</p>"+fig(svg_map,"ડ્રોન")},
 ]
},
]
def build_page():
    sections_html=[]
    for sec in SECTIONS:
        cards=[]
        for c in sec["cards"]:
            q_html=html.escape(c["q_en"])
            cards.append(f'<details class="card"><summary><strong><span class="en">{q_html}</span><span class="gu">{q_html}</span></strong><small><span class="en">{c["marks_en"]}</span><span class="gu">{c["marks_gu"]}</span></small></summary><div class="answer"><div class="en">{c["a_en"]}</div><div class="gu">{c["a_gu"]}</div></div></details>')
        sections_html.append(f'<section class="group"><h2>{html.escape(sec["title_en"])}</h2>{"".join(cards)}</section>')
    page=f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>DI03006011 · Summer 2026 solved paper</title><style>{CSS}</style></head><body><main class="page"><header class="hero"><div class="eyebrow">Solved question paper · English questions · Friendly Gujarati answers</div><div class="lang-switch" aria-label="Choose language"><button type="button" data-lang="en" aria-pressed="true">English</button><button type="button" data-lang="gu" aria-pressed="false">ગુજરાતી</button></div><h1>Construction Technology</h1><div class="meta">GTU Diploma · Civil · Semester 3 · Summer 2026 · DI03006011 · 12-05-2026 · 70 marks · 02:30 PM TO 05:00 PM</div></header>{"".join(sections_html)}<div class="footer">Solved paper for study. Verify with site spec before application.</div></main><script>document.querySelectorAll('.lang-switch button').forEach(b=>b.addEventListener('click',()=>{{document.documentElement.lang=b.dataset.lang;document.querySelectorAll('.lang-switch button').forEach(x=>x.setAttribute('aria-pressed',x===b?'true':'false'));}}));</script></body></html>'''
    return page
def main():
    page=build_page()
    out_papers=ROOT/"papers-upload/papers/DI03006011/summer-2026.html"
    out_ws=ROOT/"preview/workshop/DI03006011_summer2026_bilingual.html"
    out_papers.parent.mkdir(parents=True,exist_ok=True)
    out_ws.parent.mkdir(parents=True,exist_ok=True)
    out_papers.write_text(page,encoding="utf-8")
    out_ws.write_text(page,encoding="utf-8")
    print(f"Bilingual: {out_papers} ({len(page)} chars)")
    print(f"details={page.count('<details')}, sections={page.count('<section')}, figs={page.count('<figure>')}")
    import re; gu=''.join(re.findall(r'<div class=\"gu\">(.*?)</div>',page,re.S)); print(f"brackets gu={gu.count('(')+gu.count(')')}")
    print("PASS" if page.count('<details')==28 and page.count('<section')==5 else "FAIL")
    (ROOT/"drive-upload/DI03006011_summer_2026_bilingual.html").write_text(page,encoding="utf-8")
if __name__=="__main__": main()
