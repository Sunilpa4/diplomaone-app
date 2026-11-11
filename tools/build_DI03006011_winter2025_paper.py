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
svg_formwork=load_svg("ct3_formwork.svg")
svg_found=load_svg("ct2_found.svg")
svg_setout=load_svg("ct2_setout.svg")
svg_timber=load_svg("ct2_timber.svg")
svg_ureamed=load_svg("ct2_ureamed.svg")
svg_bonds=load_svg("ct3_bonds.svg")
svg_dpc=load_svg("ct3_dpc.svg")
svg_frame=load_svg("ct1_frame.svg")
svg_types=load_svg("ct1_types.svg")
svg_wall=load_svg("ct1_wall.svg")
svg_fail=load_svg("ct5_fail.svg")
svg_excav=load_svg("ct5_excav.svg")
svg_ppe=load_svg("ct5_ppe.svg")
svg_types5=load_svg("ct5_types.svg")
svg_print=load_svg("ct6_print.svg")

SECTIONS=[
{
 "title_en":"Q1 · Building items, structure types, scaffolding/formwork",
 "title_gu":"પ્ર.1 · બિલ્ડિંગ વસ્તુ, સ્ટ્રક્ચર પ્રકાર, પાલખ/ફોર્મવર્ક",
 "cards":[
  {"q_en":"Q.1 (a) Write functions of following items in Building: Lintel, Sill, Weather sheds. (03 marks)","marks_en":"03 marks","marks_gu":"૦૩ ગુણ","a_en":f"<p><strong>Lintel:</strong> Beam over opening to transfer wall load to sides.</p><p><strong>Sill:</strong> Bottom of window, sheds water, supports frame.</p><p><strong>Weather shed / chhajja:</strong> Protects opening from rain sun.</p>"+fig(svg_wall,"Lintel over opening, sill below window, chhajja projection"),
   "a_gu":f"<p><strong>Lintel:</strong> બારી ઉપર ભાર બાજુએ લઈ જાય. <strong>Sill:</strong> બારી નીચે પાણી કાઢે. <strong>છજું:</strong> વરસાદ તડકો રોકે.</p>"+fig(svg_wall,"લિંટલ સિલ છજું")},
  {"q_en":"Q.1 (b) Differentiate between Load Bearing and Framed Structures. (04 marks)","marks_en":"04 marks","marks_gu":"૦૪ ગુણ","a_en":"<table><tr><th>Load bearing</th><th>Framed</th></tr><tr><td>Walls carry load to foundation</td><td>Columns beams carry load walls partition</td></tr><tr><td>Thick walls, limited height, cheaper low rise</td><td>Slender, high rise, flexible plan</td></tr><tr><td>Brick/stone masonry</td><td>RCC/steel frame</td></tr></table>"+fig(svg_frame,"Load bearing walls vs framed columns-beams"),
   "a_gu":"<p>ભારવાહી માં દિવાલ ભાર લે, ફ્રેમ માં કોલમ બીમ લે.</p>"+fig(svg_frame,"ભારવાહી vs ફ્રેમ")},
  {"q_en":"Q.1 (c) With neat sketch explain components of Scaffolding. (07 marks)","marks_en":"07 marks","marks_gu":"૦૭ ગુણ","a_en":f"<p><strong>Components:</strong> Standards vertical, ledgers horizontal, transoms, bracing, putlogs, platform, guard rail, toe board, base plate. Types: single, double, steel tubular, needle.</p>"+fig(svg_scaffold,"Scaffolding standards ledgers bracing platform"),
   "a_gu":f"<p>Standards ઊભા, ledgers આડા, bracing, platform, guard rail.</p>"+fig(svg_scaffold,"પાલખ ભાગો")},
  {"q_en":"Q.1 (c) OR Discuss in detail: Characteristics of good formwork. (07 marks)","marks_en":"07 marks","marks_gu":"૦૭ ગુણ","a_en":f"<ul><li>Strong to bear concrete + vibration load without deflection.</li><li>Leak proof joints, smooth face, easy stripping, reusable, economical.</li><li>Light, rigid, correct alignment.</li></ul>"+fig(svg_formwork,"Good formwork strong leak-proof smooth reusable"),
   "a_gu":f"<ul><li>મજબૂત deflection નહીં.</li><li>Leak proof સ્મૂથ સરળ છોડાય.</li></ul>"+fig(svg_formwork,"ફોર્મવર્ક લક્ષણ")},
 ]
},
{
 "title_en":"Q2 · Foundations, cofferdam, piles, caisson, timbering",
 "title_gu":"પ્ર.2 · પાયા, કોફરડેમ, પાઇલ, કેશન, ટિમ્બરિંગ",
 "cards":[
  {"q_en":"Q.2 (a) List out the Types of Shallow Foundation and Deep Foundations. (03 marks)","marks_en":"03 marks","marks_gu":"૦૩ ગુણ","a_en":"<p><strong>Shallow:</strong> Strip/wall footing, spread, combined, raft/mat, mat.</p><p><strong>Deep:</strong> Pile driven/bored/under-reamed, pier, caisson/well.</p>"+fig(svg_found,"Shallow strip spread raft vs deep pile caisson"),
   "a_gu":"<p>Shallow strip raft, Deep pile pier caisson.</p>"+fig(svg_found,"પાયા પ્રકાર")},
  {"q_en":"Q.2 (b) Draw Neat Sketch of RCC Footing for Brick Masonary Wall. (04 marks)","marks_en":"04 marks","marks_gu":"૦૪ ગુણ","a_en":f"<p>Wall 200mm on RCC footing width ~900mm, base concrete, PCC lean, offset 150mm each side, reinforcement main bars.</p>"+fig(svg_found,"RCC footing for brick wall section"),
   "a_gu":f"<p>દિવાલ 200mm RCC ફૂટિંગ 900mm offset 150mm.</p>"+fig(svg_found,"RCC ફૂટિંગ")},
  {"q_en":"Q.2 (c) Enlist Types of coffer Dams, Draw neat Sketch of Rock Fill Crib Cofferdam. (07 marks)","marks_en":"07 marks","marks_gu":"૦૭ ગુણ","a_en":"<p>Earthen, rock fill, single/double wall, crib, cellular. <strong>Rock fill crib:</strong> Timber cribs filled with rock, impervious fill upstream, stable for deep water.</p>"+fig(svg_wall,"Rock fill crib cofferdam"),
   "a_gu":"<p>Earthen, rock fill, crib, cellular — rock fill crib લાકડા પેટી માં પથ્થર.</p>"+fig(svg_wall,"કોફરડેમ")},
  {"q_en":"Q.2 (a) OR Explain End bearing Pile with Sketch. (03 marks)","marks_en":"03 marks","marks_gu":"૦૩ ગુણ","a_en":"<p>End bearing pile transfers load through tip to hard stratum, acts as column.</p>"+fig(svg_ureamed,"End bearing pile on hard strata"),
   "a_gu":"<p>છેડા પર હાર્ડ સ્તર પર ભાર.</p>"+fig(svg_ureamed,"એન્ડ બેરિંગ પાઇલ")},
  {"q_en":"Q.2 (b) OR Draw neat Sketch of Box Caisson. (04 marks)","marks_en":"04 marks","marks_gu":"૦૪ ગુણ","a_en":"<p>Box caisson open top closed bottom, floated and sunk, placed on rock bed.</p>"+fig(svg_found,"Box caisson"),
   "a_gu":"<p>Box ઉપર ખુલ્લું નીચે બંધ તરતું મૂકાય.</p>"+fig(svg_found,"બોક્સ કેશન")},
  {"q_en":"Q.2 (c) OR Write Short note on Timbering of Trenches. (07 marks)","marks_en":"07 marks","marks_gu":"૦૭ ગુણ","a_en":f"<p>Stay bracing, box sheeting, vertical/horizontal sheeting with struts to prevent collapse in loose soil. Sequencing excavation and support.</p>"+fig(svg_timber,"Timbering trenches sheeting struts"),
   "a_gu":f"<p>Trench માં sheeting struts થી collapse રોકો.</p>"+fig(svg_timber,"ટિમ્બરિંગ")},
 ]
},
{
 "title_en":"Q3 · Masonry, bonds, concrete, plaster",
 "title_gu":"પ્ર.3 · ચણતર, બોન્ડ, કોંક્રિટ, પ્લાસ્ટર",
 "cards":[
  {"q_en":"Q.3 (a) Define with sketch: Frog, Header, Stretcher. (03 marks)","marks_en":"03 marks","marks_gu":"૦૩ ગુણ","a_en":"<p><strong>Frog:</strong> Depression on top face for key. <strong>Header:</strong> Short face 90mm seen. <strong>Stretcher:</strong> Long face 190mm seen.</p>"+fig(svg_bonds,"Frog header stretcher"),
   "a_gu":"<p>Frog ખાડો, Header ટૂંકી બાજુ, Stretcher લાંબી.</p>"+fig(svg_bonds,"ફ્રોગ હેડર સ્ટ્રેચર")},
  {"q_en":"Q.3 (b) Draw neat sketch of English Bond for Brick thick wall. (04 marks)","marks_en":"04 marks","marks_gu":"૦૪ ગુણ","a_en":f"<p>Alternate courses headers and stretchers, queen closer at ends to break joint, strongest bond.</p>"+fig(svg_bonds,"English bond 1 brick wall alternate courses"),
   "a_gu":f"<p>એક કોર્સ header બીજો stretcher queen closer સાથે.</p>"+fig(svg_bonds,"અંગ્રેજી બોન્ડ")},
  {"q_en":"Q.3 (c) List out Ingredients of Concrete. Explain Compaction of Concrete. (07 marks)","marks_en":"07 marks","marks_gu":"૦૭ ગુણ","a_en":"<p><strong>Ingredients:</strong> Cement, fine aggregate sand, coarse aggregate, water, admixture.</p><p><strong>Compaction:</strong> Remove air by hand tamping, needle vibrator, table vibrator to achieve density strength avoid honeycomb.</p>",
   "a_gu":"<p>સિમેન્ટ રેતી કપચી પાણી — કોમ્પેક્શન needle vibrator થી હવા કાઢો.</p>"},
  {"q_en":"Q.3 (a) OR Define with sketch: King Closer, Queen Closer, Half Bat (03 marks)","marks_en":"03 marks","marks_gu":"૦૩ ગુણ","a_en":"<p><strong>King closer:</strong> Brick cut diagonally half header half stretcher. <strong>Queen closer:</strong> Half width longitudinal. <strong>Half bat:</strong> Half length.</p>"+fig(svg_bonds,"King queen closer half bat"),
   "a_gu":"<p>King ત્રાંસુ કાપેલું, Queen અડધી પહોળાઈ, Half bat અડધી લંબાઈ.</p>"+fig(svg_bonds,"ક્લોઝર")},
  {"q_en":"Q.3 (b) OR Write Advantages of Hollow Concrete Block Masonary. (04 marks)","marks_en":"04 marks","marks_gu":"૦૪ ગુણ","a_en":"<p>Light, thermal insulation, faster, less mortar, earthquake resistant, economical, cavity reduces damp.</p>",
   "a_gu":"<p>હળવું insulation ઝડપી mortar ઓછું.</p>"},
  {"q_en":"Q.3 (c) OR Explain Method of Applying Sand faced Plaster on Outer Wall. (07 marks)","marks_en":"07 marks","marks_gu":"૦૭ ગુણ","a_en":"<p>Two coats: 12mm base 1:4 cement-sand, then 8mm finishing coat 1:3 with sponge finishing dashed texture water cured.</p>",
   "a_gu":"<p>12mm base 1:4 પછી 8mm sand faced sponge texture.</p>"},
 ]
},
{
 "title_en":"Q4 · Damp, DPC, machinery, joints, equipment",
 "title_gu":"પ્ર.4 · ભીનાશ, DPC, મશીનરી, સાંધા",
 "cards":[
  {"q_en":"Q.4 (a) Explain Anti Termite treatment. (03 marks)","marks_en":"03 marks","marks_gu":"૦૩ ગુણ","a_en":"<p>Chemical barrier chlorpyrifos under foundation pit, sides, plinth to block termite path.</p>",
   "a_gu":"<p>પાયા નીચે chemical barrier termite રોકે.</p>"},
  {"q_en":"Q.4 (b) Draw neat Sketch for DPC of Basement. (04 marks)","marks_en":"04 marks","marks_gu":"૦૪ ગુણ","a_en":f"<p>Horizontal DPC on raft, vertical on retaining wall connected, no break.</p>"+fig(svg_dpc,"Basement DPC horizontal + vertical"),
   "a_gu":f"<p>રાફ્ટ પર horizontal દિવાલ પર vertical જોડેલું.</p>"+fig(svg_dpc,"બેઝમેન્ટ DPC")},
  {"q_en":"Q.4 (c) Explain factor affecting selection of Construction Machineries. (07 marks)","marks_en":"07 marks","marks_gu":"૦૭ ગુણ","a_en":"<p>Scope quantity, site terrain access, soil type, time, cost, availability, skill, safety, environment.</p>",
   "a_gu":"<p>કામ જથ્થો, જમીન સમય ખર્ચ skill સલામતી.</p>"},
  {"q_en":"Q.4 (a) OR Explain Construction Joints. (03 marks)","marks_en":"03 marks","marks_gu":"૦૩ ગુણ","a_en":"<p>Joints where fresh concrete placed on hardened — toothed, dowels for continuity, water bar for tanks.</p>",
   "a_gu":"<p>જૂના નવા concrete જોડાણ toothed dowel.</p>"},
  {"q_en":"Q.4 (b) OR Enlist Safety Points for plumbing Work. (04 marks)","marks_en":"04 marks","marks_gu":"૦૪ ગુણ","a_en":"<p>PPE, trench shoring, no overhead live wires, pressure test cautiously, ventilation for solvents.</p>",
   "a_gu":"<p>PPE, trench support, pressure test સાવધાન.</p>"},
  {"q_en":"Q.4 (c) OR Write short note on Clam shell. (07 marks)","marks_en":"07 marks","marks_gu":"૦૭ ગુણ","a_en":"<p>Grab bucket two halves for deep excavation under water, pile pits, well sinking.</p>",
   "a_gu":"<p>Clam shell બે પાંખ deep excavation પાણી માં.</p>"},
 ]
},
{
 "title_en":"Q5 · Maintenance, green/prefab, safety",
 "title_gu":"પ્ર.5 · જાળવણી, ગ્રીન/પ્રિફેબ, સલામતી",
 "cards":[
  {"q_en":"Q.5 (a) What are the purpose of Maintenance of Buildings ? (03 marks)","marks_en":"03 marks","marks_gu":"૦૩ ગુણ","a_en":"<p>Retain serviceability, prevent decay, safety, aesthetics, value, hygiene.</p>"+fig(svg_types5,"Maintenance purpose"),
   "a_gu":"<p>સેવા ટકાવો decay રોકો સલામતી value.</p>"+fig(svg_types5,"જાળવણી હેતુ")},
  {"q_en":"Q.5 (b) Write advantages and disadvantages of Green Building Technology. (04 marks)","marks_en":"04 marks","marks_gu":"૦૪ ગુણ","a_en":"<p><strong>Adv:</strong> Energy water saving, healthy, less CO2. <strong>Disadv:</strong> Higher initial cost, skill, certification.</p>",
   "a_gu":"<p>ફાયદા energy બચત, ગેરફાયદા initial ખર્ચ વધારે.</p>"},
  {"q_en":"Q.5 (c) Explain Physical Causes of Accidents in Construction. (07 marks)","marks_en":"07 marks","marks_gu":"૦૭ ગુણ","a_en":"<p>Unsafe scaffolds, unguarded edges, faulty equipment, falling objects, collapse, electrical, poor housekeeping.</p>"+fig(svg_fail,"Physical causes of accidents"),
   "a_gu":"<p>પાલખ unsafe, edge ખુલ્લું, સાધન ખામી, collapse.</p>"+fig(svg_fail,"અકસ્માત ભૌતિક કારણ")},
  {"q_en":"Q.5 (a) OR Explain Repairing of Plaster. (03 marks)","marks_en":"03 marks","marks_gu":"૦૩ ગુણ","a_en":"<p>Cut defective area rectangular, clean, wet, apply bonding coat, new plaster flush, cure.</p>",
   "a_gu":"<p>ખરાબ ભાગ કાપી clean ભીનું કરી નવું plaster.</p>"},
  {"q_en":"Q.5 (b) OR Write advantages and disadvantages of Pre-Fabricated Construction. (04 marks)","marks_en":"04 marks","marks_gu":"૦૪ ગુણ","a_en":"<p><strong>Adv:</strong> Fast, quality, less labour, weather independent. <strong>Disadv:</strong> Transport, joints, heavy crane, design rigid.</p>",
   "a_gu":"<p>ફાયદા ઝડપી quality, ગેરફાયદા transport crane.</p>"},
  {"q_en":"Q.5 (c) OR Explain Safety in Excavation. (07 marks)","marks_en":"07 marks","marks_gu":"૦૭ ગુણ","a_en":f"<p>Survey utilities, slope/bracing, ladders, dewatering, barricades, PPE inspections.</p>"+fig(svg_excav,"Excavation safety barricades bracing"),
   "a_gu":f"<p>Utility check, slope bracing, ladder barricade PPE.</p>"+fig(svg_excav,"ખોદાણ સલામતી")},
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
    page=f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>DI03006011 · Winter 2025 solved paper</title><style>{CSS}</style></head><body><main class="page"><header class="hero"><div class="eyebrow">Solved question paper · English questions · Friendly Gujarati answers</div><div class="lang-switch" aria-label="Choose language"><button type="button" data-lang="en" aria-pressed="true">English</button><button type="button" data-lang="gu" aria-pressed="false">ગુજરાતી</button></div><h1>Construction Technology</h1><div class="meta">GTU Diploma · Civil · Semester 3 · Winter 2025 · DI03006011 · 04-12-2025 · 70 marks · 10:30 AM TO 01:00 PM</div></header>{"".join(sections_html)}<div class="footer">Solved paper for study. Verify with standard spec before site use.</div></main><script>document.querySelectorAll('.lang-switch button').forEach(b=>b.addEventListener('click',()=>{{document.documentElement.lang=b.dataset.lang;document.querySelectorAll('.lang-switch button').forEach(x=>x.setAttribute('aria-pressed',x===b?'true':'false'));}}));</script></body></html>'''
    return page
def main():
    page=build_page()
    out_papers=ROOT/"papers-upload/papers/DI03006011/winter-2025.html"
    out_ws=ROOT/"preview/workshop/DI03006011_winter2025_bilingual.html"
    out_papers.parent.mkdir(parents=True,exist_ok=True)
    out_ws.parent.mkdir(parents=True,exist_ok=True)
    out_papers.write_text(page,encoding="utf-8")
    out_ws.write_text(page,encoding="utf-8")
    print(f"Bilingual: {out_papers} ({len(page)} chars)")
    en_c = page.count('class="en"'); gu_c = page.count('class="gu"')
    print(f"details={page.count('<details')}, sections={page.count('<section')}, en={en_c}, gu={gu_c}")
    print("PASS" if page.count('<details')==28 and page.count('<section')==5 else "FAIL", f"figs={page.count('<figure>')}")
    import re; pat = r'<div class="gu">(.*?)</div>'; gu=''.join(re.findall(pat,page,re.S)); print(f"brackets gu={gu.count('(')+gu.count(')')}")
    (ROOT/"drive-upload/DI03006011_winter_2025_bilingual.html").write_text(page,encoding="utf-8")
if __name__=="__main__": main()
