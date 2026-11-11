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
pre{background:#f4f7f9;border:1px solid #d9e1e7;border-radius:6px;padding:10px;overflow-x:auto;font-size:.88rem;line-height:1.5}
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
svg_theo=load_svg("as1_theodolite.svg")
svg_axes=load_svg("as1_axes.svg")
svg_vernier=load_svg("as1_vernier.svg")
svg_traverse=load_svg("as1_traverse.svg")
svg_stadia=load_svg("as2_stadia.svg")
svg_inclined=load_svg("as2_inclined.svg")
svg_trig=load_svg("as2_trig.svg")
svg_elements=load_svg("as3_elements.svg")
svg_rankine=load_svg("as3_rankine.svg")
svg_types=load_svg("as3_types.svg")
svg_total=load_svg("as4_totalstation.svg")
svg_edm=load_svg("as4_edm.svg")
svg_gps=load_svg("as4_gps.svg")

SECTIONS=[
{
 "title_en":"Q1 · Theodolite basics, repetition and line extension",
 "title_gu":"પ્ર.1 · થિયોડોલાઇટ બેઝિક, પુનરાવર્તન અને રેખા લંબાવવી",
 "cards":[
  {"q_en":"Q.1 (a) Define following term related to theodolite. (1) Swinging of telescope. (2) Axis of level tube. (3) Azimuth axis. (03 marks)","marks_en":"03 marks","marks_gu":"૦૩ ગુણ","a_en":"<p><strong>Swinging:</strong> Rotating telescope about vertical axis in horizontal plane.</p><p><strong>Axis of level tube:</strong> Line tangent to bubble tube at centre.</p><p><strong>Azimuth axis:</strong> Vertical axis about which instrument rotates for horizontal angle.</p>"+fig(svg_axes,"Theodolite axes — vertical azimuth, level tube, collimation"),
   "a_gu":"<p>Swinging આડું ફેરવવું, level tube અક્ષ bubble સ્પર્શક, azimuth ઊભો અક્ષ.</p>"+fig(svg_axes,"અક્ષો")},
  {"q_en":"Q.1 (b) Draw a neat sketch of theodolite and show its components. (04 marks)","marks_en":"04 marks","marks_gu":"૦૪ ગુણ","a_en":f"<p>Telescope, eyepiece, objective, vertical circle, vernier/main scale, upper/lower plates, levelling head, foot screws, plumb bob.</p>"+fig(svg_theo,"Transit theodolite components"),
   "a_gu":f"<p>Telescope, vertical circle, plates, foot screws — આકૃતિ.</p>"+fig(svg_theo,"થિયોડોલાઇટ")},
  {"q_en":"Q.1 (c) List out the methods of measurement of horizontal angle by theodolite and discuss repetition method. (07 marks)","marks_en":"07 marks","marks_gu":"૦૭ ગુણ","a_en":"<p><strong>Methods:</strong> Direct, repetition, reiteration.</p><p><strong>Repetition:</strong> Measure angle multiple times cumulatively on vernier, divide total by n. Errors of graduation divided by n, least count improved. Procedure: sight A 0°, transit clamp sight B read, transit back to A without unclamping repeat n times, final = total/n both faces.</p>"+fig(svg_vernier,"Repetition method accumulates angle n times"),
   "a_gu":"<p>Direct, repetition, reiteration — repetition માં n વાર ઉમેરી ભાગાકાર error 1/n.</p>"+fig(svg_vernier,"પુનરાવર્તન")},
  {"q_en":"Q.1 (c) OR Explain step by step procedure to extend a line with theodolite. (07 marks)","marks_en":"07 marks","marks_gu":"૦૭ ગુણ","a_en":"<p>Set at B, backsight A face left, transit telescope, mark C1 face right repeat mark C2, mean is extension. Double face eliminates collimation error. Check by measuring 180°.</p>"+fig(svg_traverse,"Extend line AB to C by transiting — double face mean"),
   "a_gu":"<p>A backsight transit C1 face left right mean — double face.</p>"+fig(svg_traverse,"રેખા લંબાવવી")},
 ]
},
{
 "title_en":"Q2 · Tacheometry constants, principle and trigonometric levelling",
 "title_gu":"પ્ર.2 · ટેકિયોમેટ્રી અચળાંક, સિદ્ધાંત અને ત્રિકોણમિતીય લેવલિંગ",
 "cards":[
  {"q_en":"Q.2 (a) Enlist the advantages and limitations of tacheometry. (03 marks)","marks_en":"03 marks","marks_gu":"૦૩ ગુણ","a_en":"<p><strong>Adv:</strong> No chain, rapid contour hilly, traverses. <strong>Limitation:</strong> Less accurate than direct, staff verticality crucial, limited distance.</p>",
   "a_gu":"<p>ફાયદા chain વગર ઝડપી, મર્યાદા ચોકસાઈ ઓછી.</p>"},
  {"q_en":"Q.2 (b) Determine the constant of a tacheometer from the following data. Distance Q 110 m and R 220 m from P. Staff readings Top/Bottom Q 2.550/1.450 R 3.550/1.345 (04 marks)","marks_en":"04 marks","marks_gu":"૦૪ ગુણ","a_en":"""<div class="eq">Intercept s = Top−Bottom: sQ =1.10m, sR =2.205m</div><div class="eq">D = K·s + C → 110 = K·1.10 + C, 220 = K·2.205 + C</div><div class="eq">Subtract: 110 = K·1.105 → <strong>K =99.55 ≈100</strong></div><div class="eq">C =110 −99.55·1.10 = <strong>0.50m</strong></div>"""+fig(svg_stadia,"Tacheometer D=K·s+C"),
   "a_gu":"""<p>110=K·1.10+C 220=K·2.205+C → K=99.55 C=0.50</p>"""+fig(svg_stadia,"અચળાંક")},
  {"q_en":"Q.2 (c) Discuss on methods of tacheometry survey. (07 marks)","marks_en":"07 marks","marks_gu":"૦૭ ગુણ","a_en":"<p><strong>Fixed hair:</strong> Diaphragm hairs fixed K=100. <strong>Movable hair:</strong> Adjust hair interval. <strong>Tangential:</strong> Measure vertical angle tangents.</p>"+fig(svg_stadia,"Fixed hair movable hair tangential"),
   "a_gu":"<p>Fixed hair K100, movable hair, tangential.</p>"+fig(svg_stadia,"પદ્ધતિ")},
  {"q_en":"Q.2 (a) OR State and Explain the principle of tacheometry. (03 marks)","marks_en":"03 marks","marks_gu":"૦૩ ગુણ","a_en":"<p>Similar triangles optical — distance proportional to intercept. Isosceles triangle with apex at instrument.</p>"+fig(svg_inclined,"Principle D ∝ s"),
   "a_gu":"<p>Similar triangle D ∝ s.</p>"+fig(svg_inclined,"સિદ્ધાંત")},
  {"q_en":"Q.2 (b) OR Define Tacheometry.How to determine the co-efficient for stadia constants K and C in the field. (04 marks)","marks_en":"04 marks","marks_gu":"૦૪ ગુણ","a_en":"<p><strong>Tacheometry:</strong> Angular measurement to get distance and elevation.</p><p>Field: Measure known distances D1 D2 with intercepts s1 s2, solve two equations as above for K C.</p>",
   "a_gu":"<p>Known D s થી બે સમીકરણ K C કાઢો.</p>"},
  {"q_en":"Q.2 (c) OR Explain reciprocal method of Trigonometrical levelling. (07 marks)","marks_en":"07 marks","marks_gu":"૦૭ ગુણ","a_en":"<p>Simultaneous vertical angles from both ends, mean eliminates refraction. RL diff = D·tanα mean.</p>"+fig(svg_trig,"Reciprocal eliminates refraction"),
   "a_gu":"<p>બન્ને છેડે સામટા ખૂણા mean થી refraction cancel.</p>"+fig(svg_trig,"રેસિપ્રોકલ")},
 ]
},
{
 "title_en":"Q3 · Trigonometrical levelling and tacheometer RL",
 "title_gu":"પ્ર.3 · ત્રિકોણમિતીય લેવલિંગ અને ટેકિયોમીટર RL",
 "cards":[
  {"q_en":"Q.3 (a) Define Trigonometrical Levelling and describe it. (03 marks)","marks_en":"03 marks","marks_gu":"૦૩ ગુણ","a_en":"<p>Indirect levelling by vertical angle + distance. Measure angle to target, compute height D·tanθ, add to instrument RL.</p>"+fig(svg_trig,"Trigonometrical levelling D·tanθ"),
   "a_gu":"<p>ખૂણા થી height D·tanθ.</p>"+fig(svg_trig,"વ્યાખ્યા")},
  {"q_en":"Q.3 (b) Draw any two sketches for different methods of trigonometric levelling and write equations. (04 marks)","marks_en":"04 marks","marks_gu":"૦૪ ગુણ","a_en":"<p><strong>Case A accessible base:</strong> h = D·tanθ RL_top = RL_BM + h + eye?</p><p><strong>Case B inaccessible same plane:</strong> Let D unknown two stations l apart: h = l·tanθ1·tanθ2 /(tanθ1−tanθ2).</p>"+fig(svg_trig,"Two cases accessible and inaccessible base same plane"),
   "a_gu":"<p>Accessible h=Dtanθ, inaccessible h=l·tan1·tan2/(tan1−tan2).</p>"+fig(svg_trig,"સમીકરણ")},
  {"q_en":"Q.3 (c) Following observation to find RL of tower top Instrument P Q staff BM 1.510/0.635 vertical +14°30' +11°42' RL BM 5.55 PQ30 same plane (07 marks)","marks_en":"07 marks","marks_gu":"૦૭ ગુણ","a_en":"""<div class="eq">HI_P =5.55+1.510=7.06, HI_Q=5.55+0.635=6.185</div><div class="eq">Let P nearer tower D, Q farther D+30: RL_T =HI_P + D·tan14°30' =HI_Q +(D+30)·tan11°42'</div><div class="eq">7.06+0.2586D =6.185+0.2069(D+30) →0.0517D=5.335 → <strong>D=103.2m from P, 133.2m from Q</strong></div><div class="eq">RL_T =7.06+0.2586×103.2= <strong>33.76m</strong></div>""",
   "a_gu":"""<p>HI_P7.06 HI_Q6.185 D103.2m RL 33.76m</p>"""},
  {"q_en":"Q.3 (a) OR In which situations tacheometric survey is useful. (03 marks)","marks_en":"03 marks","marks_gu":"૦૩ ગુણ","a_en":"<p>Hilly rough, fill surveys, reconnaissance, contouring.</p>",
   "a_gu":"<p>ડુંગરાળ fill contour હિલી.</p>"},
  {"q_en":"Q.3 (b) OR Derive expressions for trigonometric leveling while base inaccessible, instrument stations not in same vertical plane as elevated object. (04 marks)","marks_en":"04 marks","marks_gu":"૦૪ ગુણ","a_en":"<p>Two stations A B not collinear: solve triangle ABP sine law to get D_A, then h = D_A·tanθ.</p>"+fig(svg_trig,"Not same plane sine law"),
   "a_gu":"<p>Sine law થી D_A કાઢી h=D·tanθ.</p>"+fig(svg_trig,"સમીકરણ")},
  {"q_en":"Q.3 (c) OR Tacheometer constant 100/0.40 from A BM -2°18' 3.225/3.55/3.875 BM 207.655 B +8°36' 1.65/2.515/3.38 Find RL B and distance AB (07 marks)","marks_en":"07 marks","marks_gu":"૦૭ ગુણ","a_en":"""<div class="eq">s_BM=0.65 D_BM =100·0.65·cos²2.3°+0.40·cos2.3°=65.27m V_BM =50·0.65·sin4.6°+0.40·sin2.3°=−2.62m</div><div class="eq">RL_Axis =RL_BM −V+ r? Actually axis =RL_BM + r −V? With depression: Axis =207.655+3.55+2.62=213.83m (HI)</div><div class="eq">For B s=1.73 D=100·1.73·cos²8.6°+0.40·cos8.6°=169.52m V=86.5·sin17.2°+0.40·sin8.6°=25.64m</div><div class="eq">RL_B =213.83+25.64−2.515= <strong>236.96m</strong> AB =169.5m horizontal</div>""",
   "a_gu":"""<p>Axis 213.83 D 169.5m V25.64 → RL_B 236.96m</p>"""},
 ]
},
{
 "title_en":"Q4 · Curves: elements, long chord, offsets",
 "title_gu":"પ્ર.4 · વળાંક: તત્વ, કોર્ડ, ઓફસેટ",
 "cards":[
  {"q_en":"Q.4 (a) Define (1) Point of intersection (2) Point of curve (3) Tangent point . (03 marks)","marks_en":"03 marks","marks_gu":"૦૩ ગુણ","a_en":"<p><strong>PI:</strong> Tangents meet. <strong>PC:</strong> Tangency start. <strong>PT:</strong> Tangency end.</p>"+fig(svg_elements,"PI PC PT curve elements"),
   "a_gu":"<p>PI છેદ, PC શરૂ, PT અંત.</p>"+fig(svg_elements,"વ્યાખ્યા")},
  {"q_en":"Q.4 (b) Determine Length of long chord, External distance and Mid Ordinate. Take deflection angle 150º and radius 300 M. (04 marks)","marks_en":"04 marks","marks_gu":"૦૪ ગુણ","a_en":"""<div class="eq">Δ=150° Δ/2=75°: Long chord L=2R·sinΔ/2=600·sin75°= <strong>579.56m</strong></div><div class="eq">External E=R(secΔ/2−1)=300(sec75°−1)=300·(3.8637−1)= <strong>859.11m</strong></div><div class="eq">Mid ordinate M=R(1−cosΔ/2)=300(1−cos75°)= <strong>222.36m</strong></div>"""+fig(svg_elements,"Long chord external mid-ordinate"),
   "a_gu":"""<p>L579.56m E859.11m M222.36m</p>"""+fig(svg_elements,"ગણતરી")},
  {"q_en":"Q.4 (c) Explain with sketch two theodolite method of setting out a simple curve. (07 marks)","marks_en":"07 marks","marks_gu":"૦૭ ગુણ","a_en":"<p><strong>Method1:</strong> Deflection angle from PC. <strong>Method2:</strong> Two theodolites on PC PT intersection.</p>"+fig(svg_rankine,"Two theodolite method"),
   "a_gu":"<p>PC થી deflection, બે theodolite intersection.</p>"+fig(svg_rankine,"પદ્ધતિ")},
  {"q_en":"Q.4 (a) OR Write short note on Horizontal curve. (03 marks)","marks_en":"03 marks","marks_gu":"૦૩ ગુણ","a_en":"<p>Change direction horizontal plane, circular simple compound reverse transition.</p>"+fig(svg_types,"Horizontal curve types"),
   "a_gu":"<p>Horizontal direction બદલે circular.</p>"+fig(svg_types,"આડો વળાંક")},
  {"q_en":"Q.4 (b) OR Calculate coordinates of a curve having long chord 100M and mid-ordinate 6.0M, For interval 10.0M (04 marks)","marks_en":"04 marks","marks_gu":"૦૪ ગુણ","a_en":"""<div class="eq">R = L²/(8M)+M/2 =10000/48+3=211.33m. Central ordinate max 6m, offsets y = R −√(R²−x²) where x from centre. For x=0→6m, x=10→211.33−√(44660−100)=211.33−211.09=0.24? Actually compute offsets perpendicular to long chord: y = √(R²−x²) −(R−M). Provide table: x=0 y6.00, x10 y5.76, x20 y5.04, x30 y3.83, x40 y2.10, x50 y0.</div>""",
   "a_gu":"""<p>R211.33m y x=0 6.00 x10 5.76 x20 5.04 x30 3.83</p>"""},
  {"q_en":"Q.4 (c) OR List obstacles while setting out circular curve, Explain any one. (07 marks)","marks_en":"07 marks","marks_gu":"૦૭ ગુણ","a_en":"<p>PI inaccessible, PC/PT inaccessible, chain obstruction, visibility, high ground — <strong>PI inaccessible:</strong> Use shift etc.</p>",
   "a_gu":"<p>PI PC inaccessible chain visibility — PI shift.</p>"},
 ]
},
{
 "title_en":"Q5 · Total station, EDM, GPS",
 "title_gu":"પ્ર.5 · ટોટલ સ્ટેશન, EDM, GPS",
 "cards":[
  {"q_en":"Q.5 (a) Define Total station and give function of any three parts. (03 marks)","marks_en":"03 marks","marks_gu":"૦૩ ગુણ","a_en":"<p>Electronic theodolite + EDM + processor. Parts: telescope, EDM reflector, keyboard/display.</p>"+fig(svg_total,"Total station"),
   "a_gu":"<p>Electronic theodolite+EDM — telescope EDM display.</p>"+fig(svg_total,"ટોટલ સ્ટેશન")},
  {"q_en":"Q.5 (b) Write full form ATR and Explain ATR. (04 marks)","marks_en":"04 marks","marks_gu":"૦૪ ગુણ","a_en":"<p><strong>ATR Automatic Target Recognition.</strong> Locks prism auto tracks.</p>",
   "a_gu":"<p>Automatic Target Recognition prism auto.</p>"},
  {"q_en":"Q.5 (c) Write advantages and disadvantages of Total station. (07 marks)","marks_en":"07 marks","marks_gu":"૦૭ ગુણ","a_en":"<p><strong>Adv:</strong> Fast accurate digital no manual errors. <strong>Disadv:</strong> Cost, battery, skill, not for rainy.</p>",
   "a_gu":"<p>ફાયદા fast accurate, ગેરફાયદા cost battery.</p>"},
  {"q_en":"Q.5 (a) OR Define EDM and give its 2 functions. (03 marks)","marks_en":"03 marks","marks_gu":"૦૩ ગુણ","a_en":"<p><strong>EDM:</strong> Electronic Distance Measurement via infrared/microwave. Functions: distance, coordinate.</p>"+fig(svg_edm,"EDM infrared"),
   "a_gu":"<p>Infrared distance coordinate.</p>"+fig(svg_edm,"EDM")},
  {"q_en":"Q.5 (b) OR Write segments of GPS. (04 marks)","marks_en":"04 marks","marks_gu":"૦૪ ગુણ","a_en":"<p>Space segment satellites, Control segment tracking, User segment receivers.</p>"+fig(svg_gps,"GPS segments space control user"),
   "a_gu":"<p>Space Control User.</p>"+fig(svg_gps,"GPS ભાગ")},
  {"q_en":"Q.5 (c) OR how will you prepare field work for drawing polytechnic campus in total station? (07 marks)","marks_en":"07 marks","marks_gu":"૦૭ ગુણ","a_en":"<p>Reconnaissance, control traverse, setup, backsight, collect detail points with codes, download process CAD.</p>"+fig(svg_total,"Field work workflow"),
   "a_gu":"<p>Control traverse backsight detail code CAD.</p>"+fig(svg_total,"ફીલ્ડ વર્ક")},
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
    page=f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>DI03006021 · Winter 2025 solved paper</title><style>{CSS}</style></head><body><main class="page"><header class="hero"><div class="eyebrow">Solved question paper · English questions · Friendly Gujarati answers</div><div class="lang-switch" aria-label="Choose language"><button type="button" data-lang="en" aria-pressed="true">English</button><button type="button" data-lang="gu" aria-pressed="false">ગુજરાતી</button></div><h1>Advance Surveying</h1><div class="meta">GTU Diploma · Civil · Semester 3 · Winter 2025 · DI03006021 · 06-12-2025 · 70 marks · 10:30 AM TO 01:00 PM</div></header>{"".join(sections_html)}<div class="footer">Solved paper for study. Verify with standard spec before site use.</div></main><script>document.querySelectorAll('.lang-switch button').forEach(b=>b.addEventListener('click',()=>{{document.documentElement.lang=b.dataset.lang;document.querySelectorAll('.lang-switch button').forEach(x=>x.setAttribute('aria-pressed',x===b?'true':'false'));}}));</script></body></html>'''
    return page
def main():
    page=build_page()
    out_papers=ROOT/"papers-upload/papers/DI03006021/winter-2025.html"
    out_ws=ROOT/"preview/workshop/DI03006021_winter2025_bilingual.html"
    out_papers.parent.mkdir(parents=True,exist_ok=True); out_ws.parent.mkdir(parents=True,exist_ok=True)
    out_papers.write_text(page,encoding="utf-8"); out_ws.write_text(page,encoding="utf-8")
    en_c=page.count('class="en"'); gu_c=page.count('class="gu"')
    print(f"Bilingual: {out_papers} ({len(page)} chars)")
    print(f"details={page.count('<details')}, sections={page.count('<section')}, en={en_c}, gu={gu_c}")
    print("PASS" if page.count('<details')==28 and page.count('<section')==5 else "FAIL", f"figs={page.count('<figure>')}")
    import re; pat=r'<div class="gu">(.*?)</div>'; gu=''.join(re.findall(pat,page,re.S)); print(f"brackets gu={gu.count('(')+gu.count(')')}")
    (ROOT/"drive-upload/DI03006021_winter_2025_bilingual.html").write_text(page,encoding="utf-8")
if __name__=="__main__": main()
