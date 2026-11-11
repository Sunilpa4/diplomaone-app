#!/usr/bin/env python3
from pathlib import Path
import html
ROOT=Path(__file__).resolve().parent.parent
def load_svg(name):
    p=ROOT/f"content/civil/sem3/DI03006021/diagrams/{name}"
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
def fig(svg,caption):
    return f'<figure>{svg}<figcaption>{html.escape(caption)}</figcaption></figure>'
svg_vernier=load_svg("as1_vernier.svg")
svg_traverse=load_svg("as1_traverse.svg")
svg_theo=load_svg("as1_theodolite.svg")
svg_axes=load_svg("as1_axes.svg")
svg_stadia=load_svg("as2_stadia.svg")
svg_inclined=load_svg("as2_inclined.svg")
svg_trig=load_svg("as2_trig.svg")
svg_elements=load_svg("as3_elements.svg")
svg_types=load_svg("as3_types.svg")
svg_total=load_svg("as4_totalstation.svg")
svg_edm=load_svg("as4_edm.svg")
svg_gps=load_svg("as4_gps.svg")
svg_rankine=load_svg("as3_rankine.svg")

SECTIONS=[
{
 "title_en":"Q1 · Repetition, magnetic bearing, vernier least count / closing error",
 "title_gu":"પ્ર.1 · પુનરાવર્તન, ચુંબકીય બેરિંગ, વર્નિયર LC / ક્લોઝિંગ એરર",
 "cards":[
  {"q_en":"Q.1 (a) What are the advantages of using repetition method in theodolite traverse survey? (03 marks)","marks_en":"03 marks","marks_gu":"૦૩ ગુણ","a_en":"<p>Divides graduation error by n, improves accuracy, eliminates eccentricity, checks blunders, suitable for small angles.</p>"+fig(svg_vernier,"Repetition divides error by n"),
   "a_gu":"<p>Error 1/n, ચોકસાઈ વધે, blunder check.</p>"+fig(svg_vernier,"ફાયદા")},
  {"q_en":"Q.1 (b) Explain method for measuring magnetic bearing of a line with theodolite. (04 marks)","marks_en":"04 marks","marks_gu":"૦૪ ગુણ","a_en":"<p>Fix compass to alidade, orient to magnetic north, sight line, read horizontal circle. Correct for declination to true.</p>"+fig(svg_axes,"Magnetic bearing with theodolite + trough compass"),
   "a_gu":"<p>Compass સાથે north orient line sight declination સુધારો.</p>"+fig(svg_axes,"બેરિંગ માપન")},
  {"q_en":"Q.1 (c) Draw parts of main and Vernier scale of theodolite you have used. Also calculate least count of it. (07 marks)","marks_en":"07 marks","marks_gu":"૦૭ ગુણ","a_en":"""<p><strong>Main:</strong> 360° divided 0°30' graduation. <strong>Vernier:</strong> 30 divisions cover 29 main divisions.</p><div class="eq">Least count =1 main division / n vernier =30' /30 = <strong>1' =20'' if double vernier</strong> (depends 1° main 60 vernier →20'').</div>"""+fig(svg_vernier,"Main and vernier scale LC 20''"),
   "a_gu":"""<p>Main 30' Vernier 30 → LC 1' અથવા 20''</p>"""+fig(svg_vernier,"LC ગણતરી")},
  {"q_en":"Q.1 (c) OR Following are bearing and length traverse ABCD. Find closing error. AB 105.8 319°15' BC142.5 51°30' CD188.8 131°45' DA188.9 256°45' (07 marks)","marks_en":"07 marks","marks_gu":"૦૭ ગુણ","a_en":"""<table><tr><th>Line</th><th>L</th><th>Bearing</th><th>Lat L·cosθ</th><th>Dep L·sinθ</th></tr><tr><td>AB</td><td>105.8</td><td>319°15'</td><td>+80.05</td><td>−69.15</td></tr><tr><td>BC</td><td>142.5</td><td>51°30'</td><td>+88.68</td><td>+111.49</td></tr><tr><td>CD</td><td>188.8</td><td>131°45'</td><td>−125.72</td><td>+140.82</td></tr><tr><td>DA</td><td>188.9</td><td>256°45'</td><td>−43.28</td><td>−183.87</td></tr><tr><td colspan=3>Sum</td><td>−0.27 N</td><td>−0.71 E</td></tr></table><div class="eq">Closing error e =√(0.27²+0.71²)= <strong>0.76m</strong> θ =tan⁻¹(|Dep|/|Lat|)=69° in SW quadrant bearing S69°W =249°</div><div class="eq">Relative accuracy 1:(626/0.76)= <strong>1:824</strong> perimeter 626m</div>"""+fig(svg_traverse,"Closing error vector"),
   "a_gu":"""<p>ΣLat −0.27 ΣDep −0.71 e0.76m 1:824</p>"""+fig(svg_traverse,"ક્લોઝિંગ એરર")},
 ]
},
{
 "title_en":"Q2 · Trigonometrical levelling and tacheometric constants",
 "title_gu":"પ્ર.2 · ત્રિકોણમિતીય લેવલિંગ અને ટેકિયોમેટ્રિક અચળાંક",
 "cards":[
  {"q_en":"Q.2 (a) Write short note on Trigonometrical levelling (03 marks)","marks_en":"03 marks","marks_gu":"૦૩ ગુણ","a_en":"<p>Height by vertical angle distance. Good for tall chimneys hills. Single plane two planes methods.</p>"+fig(svg_trig,"Trigonometrical levelling"),
   "a_gu":"<p>ખૂણા અંતર થી height — chimney hill.</p>"+fig(svg_trig,"ટૂંક નોંધ")},
  {"q_en":"Q.2 (b) In trigonometrical levelling base inaccessible, instrument stations same vertical plane and height at same level. Derive equation to find RL. (04 marks)","marks_en":"04 marks","marks_gu":"૦૪ ગુણ","a_en":"<p>Two stations distance l: let h =D·tanθ1=(D+l)·tanθ2 → D = l·tanθ2/(tanθ1−tanθ2) RL = RL_inst + h.</p>"+fig(svg_trig,"Same plane same level h = l·tan1·tan2/(tan1−tan2)"),
   "a_gu":"<p>D = l·tan2/(tan1−tan2) RL = HI + D·tan1</p>"+fig(svg_trig,"સમીકરણ")},
  {"q_en":"Q.2 (c) To calculate RL of chimney base observations distance AB75m stations A B chimney same plane height 15m Instrument readings BM 2.125 angle +20°20' BM100 B 1.100 +15°20' (07 marks)","marks_en":"07 marks","marks_gu":"૦૭ ગુણ","a_en":"""<div class="eq">Let base RL = X, top = X+15. HI_A =100+2.125=102.125, HI_B=101.10. Let D_A distance A to chimney base, D_B = D_A +75 (B farther if A nearer). Top RL =HI_A + D_A·tan20°20' =HI_B + D_B·tan15°20'</div><div class="eq">102.125+0.371D =101.10+0.2738(D+75)=101.10+0.2738D+20.535 →0.0972D=19.51 → <strong>D_A=200.7m from A, D_B=275.7m</strong></div><div class="eq">RL_top =102.125+74.48=176.61m → <strong>Base RL =161.61m</strong> (top−15)</div>""",
   "a_gu":"""<p>D_A200.7m top176.6 base161.6m</p>"""},
  {"q_en":"Q.2 (a) OR Calculate tacheometric constant from distance 50 s0.495 and 150 s1.485 (03 marks)","marks_en":"03 marks","marks_gu":"૦૩ ગુણ","a_en":"""<div class="eq">50=K·0.495+C, 150=K·1.485+C →100=K·0.99 → <strong>K=101.01 ≈100</strong> C=50−50=0 (additive negligible)</div>""",
   "a_gu":"""<p>K101 C≈0</p>"""},
  {"q_en":"Q.2 (b) OR What is anallatic lens? Give disadvantages. (04 marks)","marks_en":"04 marks","marks_gu":"૦૪ ગુણ","a_en":"<p>Extra lens makes additive constant zero K100. <strong>Disadv:</strong> Light loss, costly, internal fouling.</p>"+fig(svg_stadia,"Anallatic lens makes C=0"),
   "a_gu":"<p>C zero કરે — light loss costly.</p>"+fig(svg_stadia,"એનાલેટિક")},
  {"q_en":"Q.2 (c) OR Points A B and P same line tacheometer 100/0 P HI1.2m A+5°30' 1.8/2.4/3.0 P RL50 B−7°30' 1.3/2.0/2.7 Find AB RL A B (07 marks)","marks_en":"07 marks","marks_gu":"૦૭ ગુણ","a_en":"""<div class="eq">sA=1.2 D_A =100·1.2·cos²5.5°+0 =119.0m? compute: cos5.5°0.9954 cos²0.9908 →K·s·cos²=118.90. V_A=60·sin11°+0=60·0.1908=11.45m. RL_A =50+1.2+11.45−2.4=60.25m</div><div class="eq">sB=1.4 D_B=100·1.4·cos²7.5°=140·0.983=137.6m V_B=70·sin15°(−)=70·(−0.2588)=−18.12 RL_B=50+1.2−18.12−2.0=31.08m</div><div class="eq">AB = D_A + D_B? P between A B opposite sides: <strong>AB =256.6m RL_A60.25 RL_B31.08</strong></div>""",
   "a_gu":"""<p>D_A119 RL_A60.25 D_B137.6 RL_B31.08 AB256.6</p>"""},
 ]
},
{
 "title_en":"Q3 · Tacheometry principle, stadia and circular curves",
 "title_gu":"પ્ર.3 · ટેકિયોમેટ્રી સિદ્ધાંત, સ્ટેડિયા અને વળાંક",
 "cards":[
  {"q_en":"Q.3 (a) Explain fix hair method of tacheometry. (03 marks)","marks_en":"03 marks","marks_gu":"૦૩ ગુણ","a_en":"<p>Hairs fixed interval K100. Distance =K·s·cos²θ +C·cosθ.</p>"+fig(svg_stadia,"Fixed hair K100"),
   "a_gu":"<p>K100 fixed hair.</p>"+fig(svg_stadia,"ફિક્સ હેર")},
  {"q_en":"Q.3 (b) Explain principle of tacheometry. (04 marks)","marks_en":"04 marks","marks_gu":"૦૪ ગુણ","a_en":"<p>Isosceles triangle optics distance ∝ intercept.</p>"+fig(svg_inclined,"Principle D=K·s"),
   "a_gu":"<p>D ∝ s similar triangle.</p>"+fig(svg_inclined,"સિદ્ધાંત")},
  {"q_en":"Q.3 (c) Draw neat sketch simple circular curve show all components define three (07 marks)","marks_en":"07 marks","marks_gu":"૦૭ ગુણ","a_en":"<p>PC, PT, PI, radius, tangent length, long chord, external, mid ordinate.</p>"+fig(svg_elements,"Circular curve components"),
   "a_gu":"<p>PC PT PI radius chord external.</p>"+fig(svg_elements,"ઘટકો")},
  {"q_en":"Q.3 (a) OR What are stadia diaphragm? Draw different shape used. (03 marks)","marks_en":"03 marks","marks_gu":"૦૩ ગુણ","a_en":"<p>Diaphragm with stadia hairs. Shapes: vertical line with two horizontals, inclined, etc.</p>"+fig(svg_stadia,"Stadia diaphragm shapes"),
   "a_gu":"<p>Stadia hair patterns.</p>"+fig(svg_stadia,"ડાયાફ્રેમ")},
  {"q_en":"Q.3 (b) OR Explain method of finding multiplying constant and additive constant in field. (04 marks)","marks_en":"04 marks","marks_gu":"૦૪ ગુણ","a_en":"<p>Measure two known distances with intercepts solve K C as above. Take three for check.</p>",
   "a_gu":"<p>Known D s થી K C.</p>"},
  {"q_en":"Q.3 (c) OR Two tangents intersect chainage 1000m intersection 72° radius150 calculate tangent, long chord, curve length, chainage PC PT, apex distance, versed sine. (07 marks)","marks_en":"07 marks","marks_gu":"૦૭ ગુણ","a_en":"""<div class="eq">Δ=108° (180−72) T=R·tanΔ/2=150·tan54°= <strong>206.42m</strong></div><div class="eq">LC=2R·sinΔ/2=300·sin54°= <strong>242.71m</strong></div><div class="eq">Length=R·Δ_rad=150·1.88496= <strong>282.74m</strong></div><div class="eq">PC=1000−T= <strong>793.58m</strong> PT=PC+L= <strong>1076.32m</strong></div><div class="eq">Apex =R(secΔ/2−1)=150·(sec54°−1)= <strong>105.17m</strong></div><div class="eq">Versed =R(1−cosΔ/2)=150·(1−cos54°)= <strong>61.83m</strong></div>"""+fig(svg_elements,"Curve Δ108° tangent chord etc."),
   "a_gu":"""<p>T206.42 LC242.71 L282.74 PC793.58 PT1076.32 apex105.17 versed61.83</p>"""+fig(svg_elements,"ગણતરી")},
 ]
},
{
 "title_en":"Q4 · Circular vs transition, obstacles, ordinates, Rankine, radial offsets",
 "title_gu":"પ્ર.4 · ગોળાકાર vs સંક્રમણ, અવરોધ, ઓર્ડિનેટ, રેંકાઇન, રેડિયલ ઓફસેટ",
 "cards":[
  {"q_en":"Q.4 (a) Give difference between circular curve and transition curve. (03 marks)","marks_en":"03 marks","marks_gu":"૦૩ ગુણ","a_en":"<table><tr><th>Circular constant R</th><th>Transition varying R</th></tr><tr><td>Radius constant</td><td>Radius ∞→R</td></tr><tr><td>Super elevation sudden</td><td>Gradual</td></tr></table>"+fig(svg_types,"Circular vs transition"),
   "a_gu":"<p>Circular R fixed, transition R બદલે.</p>"+fig(svg_types,"તફાવત")},
  {"q_en":"Q.4 (b) List obstacles while setting out circular curve, Explain any one. (04 marks)","marks_en":"04 marks","marks_gu":"૦૪ ગુણ","a_en":"<p>PI/PC inaccessible, chain/ranging obstructed, visibility, high bank — PI inaccessible solved by shifting via triangle method.</p>",
   "a_gu":"<p>PI PC inaccessible chain visibility — shift.</p>"},
  {"q_en":"Q.4 (c) Calculate ordinate at 10m interval for simple circular curve long chord150 versed2.50 (07 marks)","marks_en":"07 marks","marks_gu":"૦૭ ગુણ","a_en":"""<div class="eq">R = L²/(8·vs)+vs/2 =22500/20+1.25=1126.25m. Ordinate y =√(R²−x²)−(R−vs) where x from centre. x=0→2.50, x10→2.45, x20→2.32, x30→2.10, x40→1.79, x50→1.39, x60→0.90, x75→0.</div>"""+fig(svg_elements,"Ordinates from long chord"),
   "a_gu":"""<p>R1126.25 y0 2.50 y10 2.45 y20 2.32</p>"""+fig(svg_elements,"ઓર્ડિનેટ")},
  {"q_en":"Q.4 (a) OR Give requirements of transition curve. (03 marks)","marks_en":"03 marks","marks_gu":"૦૩ ગુણ","a_en":"<p>Meet tangent tangentially, curvature gradual, super elevation gradual, aesthetic.</p>",
   "a_gu":"<p>Tangential meet gradual curvature.</p>"},
  {"q_en":"Q.4 (b) OR Explain Rankine methods for setting out of curve. (04 marks)","marks_en":"04 marks","marks_gu":"૦૪ ગુણ","a_en":"<p>Deflection angle δ=1718.9·C/R per chord minute. Theodolite at PC set δ to locate points chord wise.</p>"+fig(svg_rankine,"Rankine deflection angle"),
   "a_gu":"<p>δ=1718.9·C/R minute chord wise.</p>"+fig(svg_rankine,"રેંકાઇન")},
  {"q_en":"Q.4 (c) OR Calculate radial offset (taken along tangents) at 45m interval curve radius360 deflection60° (07 marks)","marks_en":"07 marks","marks_gu":"૦૭ ગુણ","a_en":"""<div class="eq">Radial offset y =R−√(R²−x²): x45→2.82m, x90→11.41m, x135→26.26m, x180→47.98m. Tangent length T=R·tan30°=207.85 so up to 180m within.</div>""",
   "a_gu":"""<p>y45 2.82 y90 11.41 y135 26.26</p>"""},
 ]
},
{
 "title_en":"Q5 · Electronic theodolite, EDM, GPS, total station advances",
 "title_gu":"પ્ર.5 · ઇલેક્ટ્રોનિક થિયોડોલાઇટ, EDM, GPS, ટોટલ સ્ટેશન",
 "cards":[
  {"q_en":"Q.5 (a) Explain following. (1) Electronic theodolite. (2) EDM instrument. (03 marks)","marks_en":"03 marks","marks_gu":"૦૩ ગુણ","a_en":"<p><strong>Electronic theodolite:</strong> Digital angle display. <strong>EDM:</strong> Infrared/microwave distance.</p>"+fig(svg_edm,"Electronic theodolite EDM"),
   "a_gu":"<p>Digital angle EDM distance.</p>"+fig(svg_edm,"વ્યાખ્યા")},
  {"q_en":"Q.5 (b) Write short note on GPS receivers (04 marks)","marks_en":"04 marks","marks_gu":"૦૪ ગુણ","a_en":"<p>Satellite signals, triangulation, accurate positioning, RTK, rover/base.</p>"+fig(svg_gps,"GPS receiver"),
   "a_gu":"<p>Satellite triangulation RTK.</p>"+fig(svg_gps,"GPS")},
  {"q_en":"Q.5 (c) Prepare list of switches on display board total station with function. (07 marks)","marks_en":"07 marks","marks_gu":"૦૭ ગુણ","a_en":"<p>ANG/DIST, HOLD, COORD, REC, EDM, PRISM, MENU, FUNC.</p>"+fig(svg_total,"Total station display switches"),
   "a_gu":"<p>ANG DIST HOLD COORD REC EDM.</p>"+fig(svg_total,"સ્વિચ")},
  {"q_en":"Q.5 (a) OR What is ATR? Explain. (03 marks)","marks_en":"03 marks","marks_gu":"૦૩ ગુણ","a_en":"<p>Automatic Target Recognition auto locks prism.</p>",
   "a_gu":"<p>Auto target lock.</p>"},
  {"q_en":"Q.5 (b) OR Explain various segment of GPS. (04 marks)","marks_en":"04 marks","marks_gu":"૦૪ ગુણ","a_en":"<p>Space, control, user.</p>"+fig(svg_gps,"GPS segments"),
   "a_gu":"<p>Space Control User.</p>"+fig(svg_gps,"સેગમેન્ટ")},
  {"q_en":"Q.5 (c) OR What are latest advancement in total station? Explain. (07 marks)","marks_en":"07 marks","marks_gu":"૦૭ ગુણ","a_en":"<p>Robotic, imaging, scanning, GNSS integrated, BIM.</p>"+fig(svg_total,"Robotic imaging scanning total station"),
   "a_gu":"<p>Robotic imaging GNSS BIM.</p>"+fig(svg_total,"નવું")},
 ]
},
]
def build_page():
    sections_html=[]
    for sec in SECTIONS:
        cards=[]
        for c in sec["cards"]:
            q=html.escape(c["q_en"])
            cards.append(f'<details class="card"><summary><strong><span class="en">{q}</span><span class="gu">{q}</span></strong><small><span class="en">{c["marks_en"]}</span><span class="gu">{c["marks_gu"]}</span></small></summary><div class="answer"><div class="en">{c["a_en"]}</div><div class="gu">{c["a_gu"]}</div></div></details>')
        sections_html.append(f'<section class="group"><h2>{html.escape(sec["title_en"])}</h2>{"".join(cards)}</section>')
    page=f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>DI03006021 · Summer 2026 solved paper</title><style>{CSS}</style></head><body><main class="page"><header class="hero"><div class="eyebrow">Solved question paper · English questions · Friendly Gujarati answers</div><div class="lang-switch" aria-label="Choose language"><button type="button" data-lang="en" aria-pressed="true">English</button><button type="button" data-lang="gu" aria-pressed="false">ગુજરાતી</button></div><h1>Advance Surveying</h1><div class="meta">GTU Diploma · Civil · Semester 3 · Summer 2026 · DI03006021 · 14/05/2026 · 70 marks · 02:30 PM TO 05:00 PM</div></header>{"".join(sections_html)}<div class="footer">Solved paper for study. Verify with standard spec before site use.</div></main><script>document.querySelectorAll('.lang-switch button').forEach(b=>b.addEventListener('click',()=>{{document.documentElement.lang=b.dataset.lang;document.querySelectorAll('.lang-switch button').forEach(x=>x.setAttribute('aria-pressed',x===b?'true':'false'));}}));</script></body></html>'''
    return page
def main():
    page=build_page()
    out_papers=ROOT/"papers-upload/papers/DI03006021/summer-2026.html"
    out_ws=ROOT/"preview/workshop/DI03006021_summer2026_bilingual.html"
    out_papers.parent.mkdir(parents=True,exist_ok=True); out_ws.parent.mkdir(parents=True,exist_ok=True)
    out_papers.write_text(page,encoding="utf-8"); out_ws.write_text(page,encoding="utf-8")
    en_c=page.count('class="en"'); gu_c=page.count('class="gu"')
    print(f"Bilingual: {out_papers} ({len(page)} chars)")
    print(f"details={page.count('<details')}, sections={page.count('<section')}, en={en_c}, gu={gu_c}")
    print("PASS" if page.count('<details')==28 and page.count('<section')==5 else "FAIL", f"figs={page.count('<figure>')}")
    import re; pat=r'<div class="gu">(.*?)</div>'; gu=''.join(re.findall(pat,page,re.S)); print(f"brackets gu={gu.count('(')+gu.count(')')}")
    (ROOT/"drive-upload/DI03006021_summer_2026_bilingual.html").write_text(page,encoding="utf-8")
if __name__=="__main__": main()
