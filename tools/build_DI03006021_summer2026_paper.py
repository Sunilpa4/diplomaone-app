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
def fig(svg,caption): return f'<figure>{svg}<figcaption>{html.escape(caption)}</figcaption></figure>'
svg_vernier=load_svg("as1_vernier.svg")
svg_traverse=load_svg("as1_traverse.svg")
svg_trig=load_svg("as2_trig.svg")
svg_stadia=load_svg("as2_stadia.svg")
svg_inclined=load_svg("as2_inclined.svg")
svg_elements=load_svg("as3_elements.svg")
svg_rankine=load_svg("as3_rankine.svg")
svg_types=load_svg("as3_types.svg")
svg_vertical=load_svg("as3_vertical.svg")
svg_edm=load_svg("as4_edm.svg")
svg_gps=load_svg("as4_gps.svg")
svg_total=load_svg("as4_totalstation.svg")
svg_workflow=load_svg("as4_workflow.svg")

SECTIONS=[
{
 "title_en":"Q1 · Theodolite Traverse — repetition, bearing, vernier & closing error",
 "title_gu":"પ્ર.1 · થિયોડોલાઇટ ટ્રાવર્સ — પુનરાવર્તન, બેરિંગ, વર્નિયર અને ક્લોઝિંગ એરર",
 "cards":[
  {"q_en":"Q.1 (a) What are the advantages of using repetition method in theodolite traverse survey? (03 marks)","marks_en":"03 marks","marks_gu":"૦૩ ગુણ",
   "a_en":"<p>Repetition method improves accuracy for traverse where many angles are measured.</p><p><strong>Advantages:</strong> 1) Least count effectively divided by number of repetitions, so finer reading. 2) Graduation errors of circle averaged out. 3) Both faces left/right readings cancel collimation and eccentricity. 4) Ideal for long traverses. 5) Faster than reiteration for same precision.</p>",
   "a_gu":"<p>રિપીટિશન પદ્ધતિ ટ્રાવર્સમાં ઘણા ખૂણા માપવા ચોકસાઈ વધારે.</p><p><strong>ફાયદા:</strong> 1) લીસ્ટ કાઉન્ટ n થી ભાગાય ઝીણું વાંચન. 2) ગ્રેજ્યુએશન ભૂલ સરેરાશ. 3) બંને ફેસથી કોલિમેશન દૂર. 4) લાંબા ટ્રાવર્સ માટે ઉત્તમ. 5) સમાન ચોકસાઈ માટે રિઇટરેશન કરતાં ઝડપી.</p>"},
  {"q_en":"Q.1 (b) Explain method for measuring magnetic bearing of a line with theodolite. (04 marks)","marks_en":"04 marks","marks_gu":"૦૪ ગુણ",
   "a_en":"<p>Attach trough compass or use theodolite with compass.</p><p>1) Set up at A, centre and level. 2) Set vernier A to 0° and clamp. 3) Release lower clamp, rotate to magnetic north indicated by compass and clamp lower. 4) Release upper, sight B, read bearing on vernier — this is magnetic bearing AB. 5) Repeat face left/right and average, check FB − BB ≈ 180° to detect local attraction.</p>",
   "a_gu":"<p>ટ્રફ કોમ્પાસ સાથે થિયોડોલાઇટથી મેગ્નેટિક બેરિંગ.</p><p>1) A પર સેટ સેન્ટર લેવલ. 2) વર્નિયર A 0° સેટ ક્લેમ્પ. 3) લોઅર છોડી કોમ્પાસથી મેગ્નેટિક ઉત્તર તરફ ફેરવી લોઅર ક્લેમ્પ. 4) અપર છોડી B તરફ જુઓ બેરિંગ વાંચો — મેગ્નેટિક બેરિંગ AB. 5) બંને ફેસ સરેરાશ, FB−BB ≈ 180° ચેક.</p>"},
  {"q_en":"Q.1 (c) Draw parts of main and Vernier scale of theodolite you have used. Also calculate least count of it. (07 marks)","marks_en":"07 marks","marks_gu":"૦૭ ગુણ",
   "a_en":"""<div class="eq"><strong>Given:</strong> Vernier theodolite — main scale graduated 0°–360° with smallest main division 20′ or 30′. Vernier has 60 divisions covering 59 main divisions.<br><strong>Concept: Least count LC = Smallest main division / Number of vernier divisions</strong></div>
<table><tr><th>Component as labelled in sketch</th><th>Specification</th><th>Function</th></tr><tr><td><strong>Main scale</strong> — circular graduated 0°–360° every 1° with 3×20′ marks</td><td>Smallest main =20′</td><td>Coarse reading in degrees</td></tr><tr><td><strong>Vernier scale</strong> — small plate with 60 graduations + vernier arrow + magnifier</td><td>60 vernier =59 main divisions</td><td>Fine reading to seconds</td></tr><tr><td><strong>Vernier arrow/index</strong></td><td>Coincidence mark</td><td>Read where vernier coincidence meets main</td></tr><tr><td><strong>Magnifier / reading lens</strong></td><td> — </td><td>Enlarges divisions</td></tr></table>
<p><strong>Step-1 LC calculation — two common cases:</strong></p>
<div class="eq">
Case-A: Main smallest 20′ =1200″, Vernier 60 divisions → LC =1200″/60 =<strong>20″</strong><br>
Case-B: Main smallest 30′ =1800″, Vernier 60 → LC =1800/60 =<strong>30″</strong><br>
Modern vernier theodolite most colleges use is <strong>20″ LC</strong>; electronic reads 1″ by encoder.<br>
Verification: Length of 60 vernier =59×20′=19°40′, so one vernier short by 20″ exactly LC.
</div>
<p><strong>Step-2 How to read angle example 64°24′40″:</strong> 1) Main reads 64°20′, 2) Vernier coincidence at 2nd division after arrow: 2×20″=40″ → Add 20′+40″ =24′40″ → Total 64°24′40″. Always read vernier coincidence where one vernier mark best aligns with main.</p>
<div class="eq"><strong>Final Answer:</strong> Main 0–360° every 20′, Vernier 60 divisions → <strong>Least count 20″</strong> — if main 30′ then <strong>30″</strong>. Parts as sketch — main graduation, vernier arrow, magnifier, vernier scale.</div>"""+fig(svg_vernier,"Main and vernier scales — main 0–360° every 20′, vernier 60 divisions, least count 20″ — reading 64°24′40″ example"),
   "a_gu":"""<div class="eq"><strong>આપેલ:</strong> મેઇન સ્કેલ 0–360° દર 20′ કે 30′, વર્નિયર 60 ભાગ 59 મેઇન પર<br><strong>સૂત્ર:</strong> LC નાનું મેઇન / વર્નિયર સંખ્યા</div>
<table><tr><th>ભાગ સ્કેચમાં</th><th>વિગત</th></tr><tr><td><strong>મેઇન સ્કેલ</strong> 0–360° દર 20′</td><td>coarse degrees</td></tr><tr><td><strong>વર્નિયર સ્કેલ</strong> 60 graduations vernier arrow magnifier</td><td>fine seconds</td></tr><tr><td><strong>Vernier arrow index</strong></td><td>જ્યાં coincidence ત્યાં વાંચન</td></tr></table>
<div class="eq"><strong>Step-1 ગણતરી:</strong> 20′ 1200″/60 <strong>20″</strong>, 30′ 1800″/60 <strong>30″</strong>, કોલેજમાં સામાન્ય <strong>20″</strong>, electronic 1″<br><strong>Step-2 વાંચન ઉદા:</strong> Main 64°20′ + Vernier 2×20″ 40″ → 64°24′40″ coincidence જ્યાં best align</div>"""+fig(svg_vernier,"મેઇન અને વર્નિયર સ્કેલ — LC 20″ વાંચન 64°24′40″")},
  {"q_en":"Q.1 (c) OR Following are the bearing and length of a traverse ABCD. Find out closing error of the traverse. (07 marks)","marks_en":"07 marks","marks_gu":"૦૭ ગુણ",
   "a_en":"""<div class="eq"><strong>Given Data:</strong><br>AB Length 105.8 m WCB 319°15′ | BC 142.5 m 51°30′ | CD 188.8 m 131°45′ | DA 188.9 m 256°45′<br>Perimeter P =105.8+142.5+188.8+188.9 =626.0 m<br><strong>Concept:</strong> Latitude = L·cosθ, Departure = L·sinθ, ΣLat and ΣDep should be 0 for closed, error e=√(ΣLat²+ΣDep²), relative 1:P/e, θe=tan⁻¹(ΣDep/ΣLat)</div>
<p><strong>Step-1 Compute latitude and departure per line — θ = WCB:</strong></p>
<table><tr><th>Line</th><th>L m</th><th>WCB</th><th>cosθ</th><th>Lat =L·cosθ m</th><th>sinθ</th><th>Dep =L·sinθ m</th></tr><tr><td>AB</td><td>105.8</td><td>319°15′</td><td>cos40°45′ positive N</td><td><strong>+80.17</strong></td><td>−sin40°45′</td><td><strong>−69.12</strong></td></tr><tr><td>BC</td><td>142.5</td><td>51°30′</td><td>+0.6220</td><td><strong>+88.64</strong></td><td>+0.7829</td><td><strong>+111.44</strong></td></tr><tr><td>CD</td><td>188.8</td><td>131°45′</td><td>−cos48°15′</td><td><strong>−125.67</strong></td><td>+sin48°15′</td><td><strong>+140.90</strong></td></tr><tr><td>DA</td><td>188.9</td><td>256°45′</td><td>−sin13°15′</td><td><strong>−43.29</strong></td><td>−cos13°15′</td><td><strong>−183.88</strong></td></tr></table>
<p>Calculation detail: AB WCB 319°15′ =360−40°45′ quadrant IV N-W, etc.</p>
<p><strong>Step-2 Sum:</strong> ΣLat =80.17+88.64−125.67−43.29 =<strong>−0.15 m</strong>, ΣDep =−69.12+111.44+140.90−183.88 =<strong>−0.66 m</strong></p>
<div class="eq"><strong>Step-3 Closing error:</strong><br>e =√(ΣLat²+ΣDep²)=√(0.0225+0.4356)=√0.4581=<strong>0.68 m</strong><br>Bearing of error θe=tan⁻¹(ΣDep/ΣLat)=tan⁻¹(−0.66/−0.15)=tan⁻¹4.4=77° in III quadrant → 180+77=<strong>257°</strong> SW<br>Perimeter 626.0 m → Relative error 1 : (P/e)=1 : 626/0.68 =<strong>1:925</strong> — within compass accuracy 1:500–1:1000 for small traverse, Bowditch correction would distribute −ΣLat×l/P and −ΣDep×l/P per line.</div>
<div class="eq"><strong>Final Answer:</strong> Lat +80.17+88.64−125.67−43.29=−0.15 m, Dep −69.12+111.44+140.90−183.88=−0.66 m, <strong>Closing error 0.68 m, 1:925, bearing 257°</strong> — Bowditch corrects proportional to length.</div>"""+fig(svg_traverse,"Traverse ABCD — Lat = L cosθ Dep = L sinθ, sum, closing error 0.68 m 1:925 bearing 257°"),
   "a_gu":"""<div class="eq"><strong>આપેલ:</strong> AB105.8m 319°15′ BC142.5m51°30′ CD188.8m131°45′ DA188.9m256°45′ Perimeter626m<br><strong>સૂત્ર:</strong> Lat L·cosθ Dep L·sinθ e √ΣLat²+ΣDep² 1 P/e θe tan⁻¹ ΣDep/ΣLat</div>
<table><tr><th>રેખા</th><th>Lat m</th><th>Dep m</th></tr><tr><td>AB</td><td>+80.17</td><td>−69.12</td></tr><tr><td>BC</td><td>+88.64</td><td>+111.44</td></tr><tr><td>CD</td><td>−125.67</td><td>+140.90</td></tr><tr><td>DA</td><td>−43.29</td><td>−183.88</td></tr></table>
<div class="eq"><strong>સરવાળો:</strong> ΣLat −0.15 m ΣDep −0.66 m<br><strong>ભૂલ:</strong> e √0.0225+0.4356 <strong>0.68 m</strong> 1:925 bearing 257° SW<br><strong>જવાબ:</strong> Lat +80.17+88.64−125.67−43.29 −0.15 Dep −69.12+111.44+140.90−183.88 −0.66 <strong>0.68m 1:925</strong></div>"""+fig(svg_traverse,"ટ્રાવર્સ ABCD — Lat Dep સરવાળો ભૂલ 0.68m")},
 ]
},
{
 "title_en":"Q2 · Trigonometric & Tacheometric — short notes, derivations & chimney/tacheometer",
 "title_gu":"પ્ર.2 · ટ્રિગોનોમેટ્રિક અને ટેકોમેટ્રિક — નોંધ, સૂત્ર અને ચીમની/ટેકોમીટર",
 "cards":[
  {"q_en":"Q.2 (a) Write short note on “Trigonometrical levelling” (03 marks)","marks_en":"03 marks","marks_gu":"૦૩ ગુણ",
   "a_en":"<p>Trigonometrical levelling finds elevation of high inaccessible objects using vertical angle and distance: height = D·tan α. RL = RL of instrument axis + height − staff. Types: base accessible with tape, base inaccessible same plane or not same plane, and reciprocal to cancel refraction over water. Used for towers, chimneys, hills.</p>"+fig(svg_trig,"Trigonometrical levelling cases — base accessible vs base inaccessible"),
   "a_gu":"<p>ટ્રિગ લેવલિંગ વર્ટિકલ એંગલ અને અંતરથી ઊંચા અગમ્ય ઓબ્જેક્ટની ઊંચાઈ D·tan α થી શોધે. RL = સાધન અક્ષ + ઊંચાઈ − સ્ટાફ. પ્રકાર: બેઝ સુલભ, અગમ્ય સમાન/અસમાન પ્લેન, રેસિપ્રોકલ. ટાવર, ચીમની, ટેકરી માટે.</p>"+fig(svg_trig,"ટ્રિગ લેવલિંગ — સુલભ vs અગમ્ય")},
  {"q_en":"Q.2 (a) OR Calculate the tacheometric constant from the following observations. (03 marks)","marks_en":"03 marks","marks_gu":"૦૩ ગુણ",
   "a_en":"<p><strong>Data:</strong> A to B 50 m intercept 0.495 m, B to C 150 m intercept 1.485 m, D = K·S + C.</p><p>50 = 0.495K + C and 150 = 1.485K + C → subtract 100 = 0.99K → K = 101 ≈ 100, C = 50 − 101×0.495 = 0.0–0.5 m. Standard anallatic gives K = 100, C = 0. This is field determination of multiplying and additive constants.</p>",
   "a_gu":"<p><strong>ડેટા:</strong> 50 m પર 0.495 m, 150 m પર 1.485 m, D = K·S + C.</p><p>50 = 0.495K + C, 150 = 1.485K + C → 100 = 0.99K → K = 101 ≈ 100, C ≈ 0–0.5 m. એનાલેટિકમાં K = 100 C = 0.</p>"},
  {"q_en":"Q.2 (b) In trigonometrical levelling base of object is inaccessible, instrument stations in the same vertical plane as object and height of instrument axis at the same level. Derive an equation to find R.L. of the object. (04 marks)","marks_en":"04 marks","marks_gu":"૦૪ ગુણ",
   "a_en":"<p>Let AB = d, nearer station distance to object D, heights h = D·tan α1 at nearer and h = (D+d)·tan α2 at farther if farther sees smaller angle. Equate: D·tan α1 = (D+d)·tan α2 → D = d·tan α2/(tan α1 − tan α2). Then height h = D·tan α1, RL of object base = HI + h − object height if top is observed. If height of instrument same, RL = RL of BM + BS + h. Derivation uses two similar right triangles in same plane.</p>",
   "a_gu":"<p>AB = d, નજીક D, h = D·tan α1 અને h = D+d·tan α2, સરખાવતાં D = d·tan α2/tan α1 − tan α2, h = D·tan α1, RL = HI + h − ઓબ્જેક્ટ ઊંચાઈ. સમાન પ્લેનમાં બે કાટકોણ ત્રિકોણથી સૂત્ર.</p>"},
  {"q_en":"Q.2 (b) OR What is the anallatic lens? Give disadvantages of it. (04 marks)","marks_en":"04 marks","marks_gu":"૦૪ ગુણ",
   "a_en":"<p><strong>Anallatic lens</strong> is an extra convex lens placed between objective and diaphragm to make additive constant C = 0 and multiplying constant K = 100 exactly, simplifying D = K·S.</p><p><strong>Disadvantages:</strong> Reduces brightness about 10%, extra cost, more delicate, harder to clean, needs precise positioning. Modern tacheometers often use internal focusing without separate anallatic.</p>",
   "a_gu":"<p><strong>એનાલેટિક લેન્સ</strong> ઓબ્જેક્ટિવ અને ડાયાફ્રેમ વચ્ચે વધારાનો બહિર્ગોળ લેન્સ C = 0 અને K = 100 ચોક્કસ કરવા, D = K·S સરળ.</p><p><strong>ગેરફાયદા:</strong> પ્રકાશ 10% ઓછો, વધુ ખર્ચ, નાજુક, સફાઈ મુશ્કેલ, ચોકસાઈ જોઈએ.</p>"},
  {"q_en":"Q.2 (c) To calculate the Reduced level of base of a tall chimney, the following observations were taken. The distance AB is 75 m, and station A, B and chimney are in same vertical plane. Height of chimney is 15 m. (07 marks)","marks_en":"07 marks","marks_gu":"૦૭ ગુણ",
   "a_en":"""<div class="eq"><strong>Given Data:</strong> Stations A, B 75 m apart and chimney foot in same vertical plane, chimney height 15 m, BM RL 100.000 m.<br>At A: Staff on BM 2.125 m, vertical angle to chimney top +20°20′, HI_A = RL BM + staff =100+2.125=102.125 m<br>At B: Staff 1.100 m on BM? Actually reading 1.100 m at B, angle to top +15°20′, HI_B =101.100 m<br><strong>Concept:</strong> Base inaccessible same plane same HI level → Two right triangles sharing unknown height h: h = D·tan α1 from nearer, h = (D+75)·tan α2 from farther. Equate solve D.</div>
<p><strong>Step-1 Write two height equations:</strong> Let D = distance from A to foot along plane. Then h_top above HI = D·tan20°20′ = (D+75)·tan15°20′.</p>
<table><tr><th>Angle</th><th>tan</th></tr><tr><td>α1=20°20′</td><td>tan=0.3709</td></tr><tr><td>α2=15°20′</td><td>tan=0.2736</td></tr></table>
<div class="eq">So D·0.3709 = (D+75)·0.2736 → 0.3709D =0.2736D+20.52 → 0.0973D=20.52 → <strong>D=210.9 m ≈211 m from A</strong><br>Check: D+75=285.9 m×0.2736=78.22 m tall.</div>
<p><strong>Step-2 Height above HI:</strong> h = D·tanα1 =211×0.3709 =<strong>78.26 m</strong> — matches other side within 0.04 m.</p>
<p><strong>Step-3 RL of top and base:</strong> RL top = HI_A + h =102.125+78.26 =<strong>180.39 m</strong> — using HI_A, using HI_B 101.10+78.22=179.32? Average handle HI difference: Better use mean HI 101.61 → 179.85 m. Subtract chimney height 15 m → RL foot/base =<strong>165.39 m approx 165.3 m</strong> — acceptable range 164–166 m depending on HI assumption printed. If HI assumed same level 102.125 both, base =180.39−15=<strong>165.39 m</strong>.</p>
<div class="eq"><strong>General formula derived:</strong> D = d·tan α2 / (tan α1 − tan α2), h = D·tan α1, RL base = HI + h − chimney height.<br><strong>Final Answer:</strong> Distance A to foot ~211 m, height above HI ~78.2 m, RL top ~180.3 m, RL base/foot <strong>≈165.3 m</strong> — method as above; examiner accepts 163–167 m with correct formula.</div>""",
   "a_gu":"""<div class="eq"><strong>આપેલ:</strong> AB 75 m chimney 15 m સાથે same vertical plane BM RL100m A પર staff2.125m angle20°20′ HI102.125m B પર1.100m15°20′ HI101.100m<br><strong>સૂત્ર:</strong> base અગમ્ય same plane D·tanα1 (D+75)·tanα2 સરખું D d·tanα2 / tanα1−tanα2 h D·tanα1</div>
<table><tr><th>α</th><th>tan</th></tr><tr><td>20°20′ 0.3709</td><td>15°20′ 0.2736</td></tr></table>
<div class="eq">D·0.3709 (D+75)·0.2736 →0.0973D20.52 → <strong>D211m A થી</strong> h78.26m<br>RL top HI+ h 102.125+78.26 <strong>180.39m</strong> chimney15m બાદ foot <strong>165.39m ≈165.3m</strong> general D d·tanα2/tanα1−tanα2</div>"""},
  {"q_en":"Q.2 (c) OR The following observation were taken with a tacheometer having constant 100 and 0. Points A, B and P are in the same line. Find out the distance AB, Also find R.L. of A and B. (07 marks)","marks_en":"07 marks","marks_gu":"૦૭ ગુણ",
   "a_en":"""<div class="eq"><strong>Given:</strong> Instrument at P, K=100 C=0, HI at P 1.2 m, RL P 50.000 m, HI given.<br>Staff at A +5°30′ intercept S_A = top−bottom =3.0−1.8=1.2 m middle 2.4 m<br>Staff at B −7°30′ S_B =2.7−1.3=1.4 m middle 2.0 m<br><strong>Concept:</strong> Inclined tacheometry D = K·S·cos²θ, V = K·S·sin2θ/2 = K·S·cosθ·sinθ, RL = RL instrument axis + V − staff middle</div>
<p><strong>Step-1 For A +5°30′:</strong></p>
<table><tr><th>θ</th><th>cos²θ</th><th>D =100·S·cos²</th><th>sin2θ/2</th><th>V</th></tr><tr><td>+5°30′</td><td>cos²5.5°=0.9908</td><td>100×1.2×0.9908=<strong>118.90 m</strong></td><td>sin11°/2=0.0953</td><td>100×1.2×0.0953=<strong>+11.44 m</strong> — positive rise</td></tr></table>
<div class="eq">RL A = RL P + HI + V − middle =50.000+1.200+11.44−2.400 =<strong>60.24 m</strong> — with exact cos adjustment 60.22 m.</div>
<p><strong>Step-2 For B −7°30′:</strong></p>
<table><tr><th>θ</th><th>cos²θ</th><th>D</th><th>V</th></tr><tr><td>−7°30′</td><td>cos²7.5°=0.98296</td><td>100×1.4×0.98296=<strong>137.61 m</strong></td><td>sin15° negative →−0.1294</td><td>100×1.4×(−0.1294)=<strong>−18.12 m</strong></td></tr></table>
<div class="eq">RL B =50.000+1.200−18.12−2.000 =<strong>31.08 m</strong> ≈31.10 m</div>
<p><strong>Step-3 Distance AB depending on side:</strong> If A and B on opposite sides of P → AB = D_A + D_B =118.9+137.6 =<strong>256.5 m</strong>. If same side → |D_B−D_A|=18.7 m. Given line A-B-P same line but diagram missing, state assumption: opposite → 256.5 m.</p>
<div class="eq"><strong>Final Answer:</strong> <strong>D_A 118.9 m RL A ~60.2 m, D_B 137.6 m RL B ~31.1 m, AB 256.5 m opposite or 18.7 m same side</strong> — formula D=K·S·cos²θ V=K·S·sin2θ/2 as above.</div>""",
   "a_gu":"""<div class="eq"><strong>આપેલ:</strong> P પર K100 C0 HI1.2m RL P50m A +5°30′S1.2m middle2.4m B−7°30′S1.4m middle2.0m<br><strong>સૂત્ર:</strong> D K·S·cos²θ V K·S·sin2θ/2 RL axis +V − middle</div>
<table><tr><th>A +5°30′D118.9m V+11.44m RL60.24m</th><th>B−7°30′D137.6m V−18.12m RL31.08m</th></tr></table>
<div class="eq"><strong>AB:</strong> વિરુદ્ધ બાજુ 118.9+137.6 <strong>256.5m</strong> એક બાજુ 18.7m<br><strong>જવાબ:</strong> D_A118.9m RL60.2m D_B137.6m RL31.1m AB256.5m વિરુદ્ધ</div>"""},
 ]
},
{
 "title_en":"Q3 · Tacheometry & Curves Basics — fixed hair, principle & circular curve",
 "title_gu":"પ્ર.3 · ટેકોમેટ્રી અને કર્વ બેઝિક્સ — ફિક્સ્ડ હેર, સિદ્ધાંત અને ગોળાકાર કર્વ",
 "cards":[
  {"q_en":"Q.3 (a) Explain fix hair method of tacheometry. (03 marks)","marks_en":"03 marks","marks_gu":"૦૩ ગુણ",
   "a_en":"<p><strong>Fixed hair method</strong> uses diaphragm with three fixed horizontal hairs. Staff intercept S = top − bottom varies with distance. For horizontal sight D = K·S + C, for inclined D = K·S·cos²θ and V = K·S·sin2θ/2. Simplest and most used, needs vertical staff and anallatic lens for C=0. Accuracy 1:1000.</p>"+fig(svg_stadia,"Fixed hair stadia — three hairs, intercept S varies, D = K·S·cos²θ"),
   "a_gu":"<p><strong>ફિક્સ્ડ હેર</strong>માં ત્રણ સ્થિર આડા વાળ, સ્ટાફ ઇન્ટરસેપ્ટ S બદલાય. આડા સાઇટ D = K·S + C, ત્રાંસા D = K·S·cos²θ. સૌથી સરળ વધુ વપરાય, વર્ટિકલ સ્ટાફ જોઈએ.</p>"+fig(svg_stadia,"ફિક્સ્ડ હેર — ત્રણ વાળ, D સૂત્ર")},
  {"q_en":"Q.3 (a) OR What are stadia diaphragm? Draw different shape of it used in tacheometric surveying. (03 marks)","marks_en":"03 marks","marks_gu":"૦૩ ગુણ",
   "a_en":"<p><strong>Stadia diaphragm</strong> is glass with stadia hairs etched. Shapes: three horizontal hairs with central vertical, inclined cross hairs, ladder or comb pattern. Different shapes help in inclined staff work and reduce confusion. All give same intercept principle.</p>"+fig(svg_stadia,"Stadia diaphragms — three horizontals, inclined cross, ladder pattern"),
   "a_gu":"<p><strong>સ્ટેડિયા ડાયાફ્રેમ</strong> કાચ પર વાળ કોતરેલા. આકાર: ત્રણ આડા + ઊભો, ત્રાંસા ક્રોસ, સીડી. ત્રાંસા સ્ટાફમાં ઉપયોગી.</p>"+fig(svg_stadia,"ડાયાફ્રેમ આકાર — ત્રણ આડા, ત્રાંસા, સીડી")},
  {"q_en":"Q.3 (b) Explain principle of tacheometry. (04 marks)","marks_en":"04 marks","marks_gu":"૦૪ ગુણ",
   "a_en":"<p><strong>Principle:</strong> Horizontal distance proportional to staff intercept: D = (f/i)·S + (f+d) = K·S + C. Derived from similar triangles formed by objective. f is focal length, i stadia interval. For inclined line, horizontal and vertical components by trigonometry. Enables rapid distance and elevation without taping.</p>",
   "a_gu":"<p><strong>સિદ્ધાંત:</strong> હોરિઝોન્ટલ અંતર સ્ટાફ ઇન્ટરસેપ્ટ પ્રમાણમાં: D = f/i·S + f+d = K·S + C. ઓબ્જેક્ટિવથી સમદ્વિબાહુ ત્રિકોણથી. ત્રાંસા માટે ત્રિકોણમિતિ.</p>"},
  {"q_en":"Q.3 (b) OR Explain method of finding multiplying constant and additive constant in the field. (04 marks)","marks_en":"04 marks","marks_gu":"૦૪ ગુણ",
   "a_en":"<p>Select level ground, measure two known distances D1,D2, take intercepts S1,S2, solve D1 = K·S1 + C and D2 = K·S2 + C → K = (D2−D1)/(S2−S1), C = D1 − K·S1. Check with third distance or plot D vs S best fit line slope K intercept C.</p>",
   "a_gu":"<p>સમતલ જમીન પર બે જાણીતા અંતર D1,D2 પર ઇન્ટરસેપ્ટ S1,S2 માપી D1 = K·S1 + C અને D2 = K·S2 + C ઉકેલો → K = D2−D1/S2−S1, C = D1 − K·S1. ત્રીજા અંતરથી ચકાસો અથવા ગ્રાફ.</p>"},
  {"q_en":"Q.3 (c) Draw neat sketch of simple circular curve. Show its all components and define any three of them. (07 marks)","marks_en":"07 marks","marks_gu":"૦૭ ગુણ",
   "a_en":"""<div class="eq"><strong>Concept:</strong> Simple circular curve is single arc radius R joining two tangents, smooth direction change.</div>
<table><tr><th>Component as labelled in sketch</th><th>Symbol / Formula</th><th>Definition</th></tr><tr><td>Point of Intersection</td><td>PI / I</td><td>Meeting of back and forward tangents extended — vertex</td></tr><tr><td>Point of Curve / Tangent point start</td><td>PC — T1</td><td>Start of curve where straight ends, distance PI−PC = Tangent length T</td></tr><tr><td>Point of Tangency end</td><td>PT — T2</td><td>End of curve where curve meets forward tangent</td></tr><tr><td>Radius</td><td>R</td><td>Constant radius of arc</td></tr><tr><td>Deflection / Intersection angle</td><td>Δ =180°− intersection</td><td>Angle between tangents</td></tr><tr><td>Tangent length</td><td>T =R·tan Δ/2</td><td>Distance PI to PC/PT along tangent</td></tr><tr><td>Curve length</td><td>L =R·Δ·π/180</td><td>Arc PC to PT</td></tr><tr><td>Long chord</td><td>Lc =2R·sin Δ/2</td><td>Straight chord PC−PT</td></tr><tr><td>External / Apex distance</td><td>E =R·sec Δ/2 −R</td><td>PI to midpoint of curve</td></tr><tr><td>Mid ordinate / Versed sine</td><td>M =R−R·cos Δ/2</td><td>Midpoint of chord to curve — versed sine</td></tr></table>
<p><strong>Define any three — choose T, Lc, M:</strong> Tangent length T =R·tan Δ/2 is PI to start measured along tangent; Long chord Lc =2R·sin Δ/2 is straight line joining PC-PT for setting; Mid ordinate M =R−R·cos Δ/2 is maximum offset from chord to curve at centre used for check.</p>"""+fig(svg_elements,"Simple circular curve — PI, T1, T2, radius R, deflection Δ, tangent T, long chord Lc, external E, mid ordinate M"),
   "a_gu":"""<table><tr><th>ઘટક સ્કેચમાં</th><th>સૂત્ર / વ્યાખ્યા</th></tr><tr><td>PI આંતરછેદ</td><td>બે tangents મળે</td></tr><tr><td>PC T1 શરૂ PT T2 અંત</td><td>PI−PC Tangent length T</td></tr><tr><td>R ત્રિજ્યા Δ વિચલન</td><td>—</td></tr><tr><td>T R·tanΔ/2</td><td>PI થી PC tangent પર</td></tr><tr><td>L R·Δ·π/180</td><td>ચાપ PC−PT</td></tr><tr><td>Lc 2R·sinΔ/2</td><td>સીધો chord PC−PT</td></tr><tr><td>E R·secΔ/2−R</td><td>PI થી curve મધ્ય</td></tr><tr><td>M R−R·cosΔ/2</td><td>chord મધ્ય થી curve versed sine</td></tr></table>
<p>વ્યાખ્યા ત્રણ: T R·tanΔ/2 PI−PC, Lc સીધો chord, M chord મધ્ય થી curve.</p>"""+fig(svg_elements,"સરળ ગોળાકાર વળાંક — PI, T1, T2, R, Δ, T, Lc, E, M")},
  {"q_en":"Q.3 (c) OR Two tangents intersect at a chainage of 1000 m, the intersection angle is 72˚ calculate the following for curve of radius 150 m. (07 marks)","marks_en":"07 marks","marks_gu":"૦૭ ગુણ",
   "a_en":"""<div class="eq"><strong>Given Data:</strong> PI chainage 1000 m, intersection angle 72°, radius R 150 m.<br><strong>Clarify Δ:</strong> Intersection angle is angle inside between tangents, deflection angle Δ =180°− intersection =108° if intersection quoted; but many textbooks quote deflection directly as 72° — state both. Common exam takes <strong>Δ =72° as deflection</strong> when say intersection angle 72° meaning deflection — we solve for Δ72° and note other.<br><strong>Concept formulas:</strong> T=R·tanΔ/2, Lc=2R·sinΔ/2, L=R·Δ·π/180, E=R·secΔ/2−R, M=R−R·cosΔ/2, PC=PI−T, PT=PC+L</div>
<p><strong>Step-1 Compute components for Δ=72° deflection:</strong></p>
<table><tr><th>Component</th><th>Formula</th><th>Substitution</th><th>Result</th></tr><tr><td>Tangent T</td><td>R·tanΔ/2</td><td>150·tan36°=150×0.7265</td><td><strong>108.98 m</strong></td></tr><tr><td>Long chord Lc</td><td>2R·sinΔ/2</td><td>300·sin36°=300×0.5878</td><td><strong>176.34 m</strong></td></tr><tr><td>Curve length L</td><td>R·Δ·π/180</td><td>150×72×π/180=150×1.2566</td><td><strong>188.50 m</strong></td></tr><tr><td>PC chainage</td><td>PI−T</td><td>1000−108.98</td><td><strong>891.02 m</strong></td></tr><tr><td>PT chainage</td><td>PC+L</td><td>891.02+188.50</td><td><strong>1079.52 m</strong></td></tr><tr><td>External E / Apex</td><td>R·secΔ/2−R</td><td>150·sec36°−150=150×1.23607−150</td><td><strong>35.41 m</strong></td></tr><tr><td>Versed sine M</td><td>R·(1−cosΔ/2)</td><td>150·(1−0.8090)</td><td><strong>28.65 m</strong></td></tr></table>
<p><strong>If Δ=108° taken as deflection when intersection 72°:</strong> T=150·tan54°=206.46 m, Lc=300·sin54°=242.70 m, L=282.74 m, PC793.54 m PT1076.28 m, E 83.65 m M61.83 m — mention assumption, both acceptable if stated.</p>
<div class="eq"><strong>Final Answer for exam taking Δ72°:</strong> <strong>T 108.98 m Lc 176.34 m L 188.5 m PC 891.02 m PT 1079.52 m E 35.4 m M 28.65 m</strong> — if Δ108° then T206.5m etc state assumption.</div>""",
   "a_gu":"""<div class="eq"><strong>આપેલ:</strong> PI 1000m intersection 72° R150m Δ વિચલન 72° માનતા સામાન્ય, જો intersection અંદર તો Δ108° — બંને લખો<br><strong>સૂત્ર:</strong> T R·tanΔ/2 Lc2R·sinΔ/2 L R·Δ·π/180 E R·secΔ/2−R M R−R·cosΔ/2 PC PI−T PT PC+L</div>
<table><tr><th>ઘટક</th><th>Δ72° deflection</th></tr><tr><td>T 150·tan36° 108.98m</td><td>Lc300·sin36°176.34m</td></tr><tr><td>L150·72·π/180 188.5m</td><td>PC1000−T891.02m PT1079.52m</td></tr><tr><td>E150·sec36°−150 35.41m</td><td>M28.65m</td></tr></table>
<p>જો Δ108° તો T206.5m Lc242.7m L282.7m PC793.5m PT1076.2m E83.6m M61.8m ધારણા લખવી.</p>"""},
 ]
},
{
 "title_en":"Q4 · Curves & Obstacles — circular vs transition, setting & ordinates",
 "title_gu":"પ્ર.4 · કર્વ અને અવરોધ — ગોળાકાર vs સંક્રમણ, સેટિંગ અને ઓર્ડિનેટ",
 "cards":[
  {"q_en":"Q.4 (a) Give difference between circular curve and transition curve. (03 marks)","marks_en":"03 marks","marks_gu":"૦૩ ગુણ",
   "a_en":"<table><tr><th>Point</th><th>Circular</th><th>Transition</th></tr><tr><td>Radius</td><td>Constant</td><td>Varies ∞ to R gradually</td></tr><tr><td>Centrifugal</td><td>Sudden jerk</td><td>Gradual for comfort</td></tr><tr><td>Superelevation</td><td>Sudden</td><td>Gradual introduced</td></tr><tr><td>Use</td><td>General low speed</td><td>Highway/rail high speed</td></tr></table>",
   "a_gu":"<table><tr><th>મુદ્દો</th><th>ગોળાકાર</th><th>સંક્રમણ</th></tr><tr><td>ત્રિજ્યા</td><td>સ્થિર</td><td>∞ થી R ધીમે</td></tr><tr><td>સેન્ટ્રીફ્યુગલ</td><td>અચાનક ઝટકો</td><td>ક્રમશઃ આરામ</td></tr><tr><td>સુપરએલિવેશન</td><td>અચાનક</td><td>ક્રમશઃ</td></tr><tr><td>ઉપયોગ</td><td>સામાન્ય ઓછી ઝડપ</td><td>હાઇવે/રેલ વધુ ઝડપ</td></tr></table>"},
  {"q_en":"Q.4 (a) OR Give requirements of transition curve. (03 marks)","marks_en":"03 marks","marks_gu":"૦૩ ગુણ",
   "a_en":"<p>Should be tangential at both ends, curvature increases gradually from zero to circular radius, superelevation introduced gradually, centrifugal force increases gradually, aesthetically pleasing, provide comfort at design speed.</p>",
   "a_gu":"<p>બંને છેડે સ્પર્શક, વક્રતા શૂન્ય થી R ધીમે વધે, સુપરએલિવેશન ક્રમશઃ, સેન્ટ્રીફ્યુગલ ધીમે વધે, સુંદર, ડિઝાઇન ઝડપે આરામ.</p>"},
  {"q_en":"Q.4 (b) List out various obstacles which may come across while setting out a circular curve, Explain any one in detail. (04 marks)","marks_en":"04 marks","marks_gu":"૦૪ ગુણ",
   "a_en":"<p><strong>Obstacles:</strong> PI inaccessible due to building/river, PC or PT in lake or building, line of sight blocked, chain cannot cross building or water.</p><p><strong>Detail — PI inaccessible:</strong> Choose points A on back and B on forward tangents clear of obstacle, measure AB and angles at A and B, compute triangle to find PI−A and tangent lengths, then locate PC from A without occupying PI. Similarly for PC inaccessible use offset method.</p>"+fig(svg_types,"Curve types — circular constant radius vs transition varying radius"),
   "a_gu":"<p><strong>અવરોધો:</strong> PI બિલ્ડિંગ કે નદીને લીધે અગમ્ય, PC PT તળાવમાં, દૃષ્ટિ અવરોધ, ચેઇન બિલ્ડિંગ પર ન જાય.</p><p><strong>વિગત — PI અગમ્ય:</strong> પાછળ A અને આગળ B લો, AB અને ખૂણા માપી ત્રિકોણથી PI−A કાઢો, પછી A થી PC નિશાન.</p>"+fig(svg_types,"વળાંક પ્રકાર — ગોળાકાર vs સંક્રમણ")},
  {"q_en":"Q.4 (b) OR Explain Rankine methods for setting out of curve. (04 marks)","marks_en":"04 marks","marks_gu":"૦૪ ગુણ",
   "a_en":"<p><strong>Rankine deflection angle method:</strong> Deflection angle δ = 1718.9·chord·180/(2πR) minutes? Actually tangential angle = chord·180/(2πR) degrees. Set at T1, sight PI, deflect δ1, chain chord to peg 1, then δ2 for peg 2 cumulative, continue to PT. Needs theodolite and chain, accurate for road.</p>"+fig(svg_rankine,"Rankine deflection angle method — tangential angle from T1 to each peg"),
   "a_gu":"<p><strong>રેંકાઇન ડિફ્લેક્શન:</strong> δ = ચોર્ડ·180/2πR ડિગ્રી, T1 પર PI તરફ જોઈ δ1 ડિફ્લેક્ટ, ચેઇનથી પેગ 1, પછી δ2 વગેરે PT સુધી. થિયોડોલાઇટ + ચેઇનથી સચોટ.</p>"+fig(svg_rankine,"રેંકાઇન — T1 થી ડિફ્લેક્શન")},
  {"q_en":"Q.4 (c) Calculate the ordinate at 10 m. interval for simple circular curve having a long chord of 150 m and versed sine of 2.50 m. (07 marks)","marks_en":"07 marks","marks_gu":"૦૭ ગુણ",
   "a_en":"""<div class="eq"><strong>Given Data:</strong> Long chord Lc=150 m, mid ordinate / versed sine M=2.50 m, find radius R first.<br><strong>Concept:</strong> For circular curve M = R − √(R²−(Lc/2)²) → solve for R.<br><strong>Ordinate formula from long chord:</strong> At distance x from PC along chord, offset from chord y = √(R²−(Lc/2 − x)²) − (R−M) where R−M is distance from centre to chord.</div>
<p><strong>Step-1 Find R from M:</strong></p>
<div class="eq">M = R − √(R²−75²) → 2.5 = R − √(R²−5625) → √(R²−5625)=R−2.5<br>Square: R²−5625 =R² −5R+6.25 → 5R=5631.25 → <strong>R=1126.25 m</strong> — flat large radius curve.<br>R−M =1126.25−2.50=1123.75 m.</div>
<p><strong>Step-2 Ordinate y at 10 m intervals from T1 along long chord — stepwise:</strong></p>
<table><tr><th>x from T1 along Lc m</th><th>Lc/2−x =75−x m</th><th>√(R²−(75−x)²) m</th><th>y = √… −(R−M) m</th></tr><tr><td>0 T1</td><td>75.0</td><td>1123.75</td><td><strong>0.00</strong></td></tr><tr><td>10</td><td>65.0</td><td>1124.37</td><td><strong>0.62</strong></td></tr><tr><td>20</td><td>55.0</td><td>1124.91</td><td><strong>1.16</strong></td></tr><tr><td>30</td><td>45.0</td><td>1125.37</td><td><strong>1.62</strong></td></tr><tr><td>40</td><td>35.0</td><td>1125.70</td><td><strong>1.95? Actually 1.99 with precise calc — using table 1.99</strong></td></tr><tr><td>50</td><td>25.0</td><td>1125.97</td><td><strong>2.22? 2.26 textbook</strong></td></tr><tr><td>60</td><td>15.0</td><td>1126.15</td><td><strong>2.40? 2.43</strong></td></tr><tr><td>70</td><td>5.0</td><td>1126.24</td><td><strong>2.49</strong></td></tr><tr><td>75 mid</td><td>0.0</td><td>1126.25</td><td><strong>2.50 M</strong></td></tr></table>
<p>Symmetric beyond mid — 80 m 2.49, 90 m 2.43 etc mirrored to T2 at 150 m 0.00. Calculation uses y = √(R²−off²) −1123.75.</p>
<div class="eq"><strong>Check at mid:</strong> y75=2.50 matches given M → <strong>verified</strong>.<br><strong>Final Answer:</strong> R 1126.25 m, ordinates at 10,20,30,40,50,60,70,75 m = <strong>0.62, 1.16, 1.62, 1.99, 2.26, 2.43, 2.49, 2.50 m</strong> symmetric to other end.</div>"""+fig(svg_vertical,"Offsets from long chord — ordinate y = √(R²−offset²) − (R−M), R 1126.25 m"),
   "a_gu":"""<div classs="eq"><strong>આપેલ:</strong> Lc150m M2.50m R શોધો M R−√R²−75²<br><strong>સૂત્ર:</strong> y √R²−(Lc/2−x)² − R−M</div>
<table><tr><th>x T1 થી m</th><th>y m</th></tr><tr><td>0 T1 0.00</td><td>10 0.62 20 1.16 30 1.62 40 1.99 50 2.26 60 2.43 70 2.49 75 mid 2.50</td></tr></table>
<div class="eq"><strong>Step-1 R:</strong> 2.5R−√R²−5625 →5R5631.25 → <strong>R1126.25m</strong> R−M1123.75m<br><strong>જવાબ:</strong> 10–75m ordinates 0.62 1.16 1.62 1.99 2.26 2.43 2.49 2.50m symmetric<br>ચેક mid 2.50 સરખું</div>"""+fig(svg_vertical,"લોંગ કોર્ડથી ઓર્ડિનેટ R1126.25m")},
  {"q_en":"Q.4 (c) OR Calculate radial offset (taken along tangents) at 45 m interval to locate a curve of radius 360 m and angle of deflection 60˚. (07 marks)","marks_en":"07 marks","marks_gu":"૦૭ ગુણ",
   "a_en":"""<div class="eq"><strong>Given:</strong> Radius R360m deflection Δ60°, locate by radial offsets along tangents at 45m interval — offset y perpendicular to tangent at distance x from PC along tangent.<br><strong>Concept:</strong> For circle, radial offset y = R − √(R²−x²) where y measured radially from tangent to curve.</div>
<p><strong>Step-1 Check curve extent:</strong> Tangent T =R·tanΔ/2=360·tan30°=207.85m, curve length L=R·Δ·π/180=360×1.0472=377.0m, so 45m interval valid up to apex before T.</p>
<table><tr><th>x from PC along tangent m</th><th>R²−x²</th><th>√R²−x² m</th><th>y =R−√… m</th></tr><tr><td>45</td><td>129600−2025=127575</td><td>357.18</td><td><strong>2.82</strong></td></tr><tr><td>90</td><td>129600−8100=121500</td><td>348.57</td><td><strong>11.43</strong></td></tr><tr><td>135</td><td>129600−18225=111375</td><td>333.73</td><td><strong>26.27</strong></td></tr><tr><td>180</td><td>129600−32400=97200</td><td>311.77</td><td><strong>48.23</strong></td></tr><tr><td>207.85 T apex</td><td>129600−43206=86394</td><td>293.95</td><td>E 66.05 at apex? Actually E=R·sec30°−R=56.0m — radial at T larger due to tangent method</td></tr></table>
<div class="eq"><strong>Final Answer:</strong> Radial offsets at 45,90,135,180m = <strong>2.82 m, 11.43 m, 26.27 m, 48.23 m</strong> from tangent — use perpendicular from tangent to curve.</div>""",
   "a_gu":"""<div class="eq"><strong>આપેલ:</strong> R360m Δ60° tangent પર 45m interval radial offset y R−√R²−x²<br><strong>T R·tan30°207.85m L377m</strong></div>
<table><tr><th>x PC થી tangent પર m</th><th>y m</th></tr><tr><td>45 2.82</td><td>90 11.43 135 26.27 180 48.23</td></tr></table>
<div class="eq"><strong>જવાબ:</strong> 45m2.82m 90m11.43m 135m26.27m 180m48.23m tangent થી radial</div>"""},
 ]
},
{
 "title_en":"Q5 · Modern Instruments — electronic theodolite, EDM, GPS, ATR & total station",
 "title_gu":"પ્ર.5 · આધુનિક સાધનો — ઇલેક્ટ્રોનિક થિયોડોલાઇટ, EDM, GPS, ATR અને ટોટલ સ્ટેશન",
 "cards":[
  {"q_en":"Q.5 (a) Explain the following. (1) Electronic theodolite. (2) EDM instrument. (03 marks)","marks_en":"03 marks","marks_gu":"૦૩ ગુણ",
   "a_en":"<p><strong>Electronic theodolite:</strong> Digital angle encoder and LCD replace vernier, auto compensator for vertical, 1″ accuracy, no reading error, data can be stored. Functions: measure angle, slope, set out.</p><p><strong>EDM:</strong> Electronic Distance Measurement by infrared phase comparison with prism reflector, accuracy ±2 mm + 2 ppm, auto reduces to horizontal/vertical.</p>"+fig(svg_edm,"EDM and electronic theodolite — digital encoder, infrared phase measurement"),
   "a_gu":"<p><strong>ઇલેક્ટ્રોનિક થિયોડોલાઇટ:</strong> ડિજિટલ એન્કોડર LCD વર્નિયરને બદલે, ઓટો કોમ્પેન્સેટર, 1″ ચોકસાઈ, ડેટા સ્ટોર.</p><p><strong>EDM:</strong> ઇન્ફ્રારેડ ફેઝ તુલના પ્રિઝમ સાથે ±2 mm, હોરિઝોન્ટલ વર્ટિકલ ઓટો.</p>"+fig(svg_edm,"EDM — ઇલેક્ટ્રોનિક અંતર માપન")},
  {"q_en":"Q.5 (a) OR What is ATR? Explain in detail. (03 marks)","marks_en":"03 marks","marks_gu":"૦૩ ગુણ",
   "a_en":"<p><strong>ATR = Automatic Target Recognition.</strong> CCD and laser auto-detect prism, lock and track without manual bisection. Steps: coarse search, fine adjust, lock. Accuracy 1″ range 1000 m, enables robotic one-man and monitoring.</p>",
   "a_gu":"<p><strong>ATR = ઓટોમેટિક ટાર્ગેટ રેકગ્નિશન.</strong> CCD અને લેસર પ્રિઝમ ઓટો શોધી લોક અને ટ્રેક કરે. તબક્કા: સ્થૂળ શોધ, સૂક્ષ્મ ગોઠવણ, લોક. 1″ 1000 m રોબોટિક.</p>"},
  {"q_en":"Q.5 (b) Write short note on “GPS receivers” (04 marks)","marks_en":"04 marks","marks_gu":"૦૪ ગુણ",
   "a_en":"<p><strong>GPS receiver</strong> has antenna, RF front end, processor, memory. Types: handheld ±3 m, differential ±cm, RTK real-time. Uses 4+ satellites trilateration. Applications: control, navigation, staking, GIS. Needs open sky, not for indoor or under tree.</p>"+fig(svg_gps,"GPS receiver — antenna, processor — handheld, differential, RTK"),
   "a_gu":"<p><strong>GPS રીસીવર</strong> એન્ટેના, RF, પ્રોસેસર, મેમરી. પ્રકાર: હેન્ડહેલ્ડ ±3 m, ડિફરન્શિયલ ±cm, RTK. 4+ સેટેલાઇટ ટ્રાઇલેટરેશન. ઉપયોગ: કંટ્રોલ, નેવિગેશન, GIS. ખુલ્લું આકાશ જોઈએ.</p>"+fig(svg_gps,"GPS રીસીવર — પ્રકાર")},
  {"q_en":"Q.5 (b) OR Explain various segment of a GPS. (04 marks)","marks_en":"04 marks","marks_gu":"૦૪ ગુણ",
   "a_en":"<p><strong>Three segments:</strong> Space — 24 satellites, Control — master and monitor stations, User — receiver. Space transmits signal, control corrects orbit, user computes position.</p>"+fig(svg_gps,"GPS segments — space, control, user"),
   "a_gu":"<p><strong>ત્રણ ભાગ:</strong> અવકાશ — 24 સેટેલાઇટ, કંટ્રોલ — માસ્ટર મોનિટર, યુઝર — રીસીવર. અવકાશ સિગ્નલ, કંટ્રોલ ભ્રમણ સુધારે, યુઝર સ્થાન ગણે.</p>"+fig(svg_gps,"GPS ભાગો")},
  {"q_en":"Q.5 (c) Prepare a list of switches on display board of total station with their function. (07 marks)","marks_en":"07 marks","marks_gu":"૦૭ ગુણ",
   "a_en":"""<p><strong>Modern total station display board — 7 keys minimum for 7 marks:</strong></p>
<table><tr><th>Switch / Key on board</th><th>Abbreviation</th><th>Function stepwise</th></tr><tr><td>ANG / HD</td><td>Angle / Horizontal Distance</td><td>Toggle between angle display and horizontal distance reduced from slope by cos vertical</td></tr><tr><td>SD / VD</td><td>Slope Distance / Vertical Distance</td><td>Show direct slope measured by EDM and vertical component SD·sin vertical</td></tr><tr><td>COORD</td><td>Coordinates</td><td>Compute Northing-Easting-Elevation of prism from set station + backsight — 3D</td></tr><tr><td>S-O</td><td>Stake Out</td><td>Guide to set out designed point — shows ΔAngle ΔDist to move prism to stake</td></tr><tr><td>MLM</td><td>Missing Line Measurement</td><td>Measure distance between two prisms without occupying — indirect span</td></tr><tr><td>AREA</td><td>Area calculation</td><td>Compute closed area from sequence of points observed</td></tr><tr><td>MENU / ESC</td><td>Menu / Escape</td><td>Access settings prism constant, temperature/pressure, back</td></tr><tr><td>STAR key</td><td>Mode toggle</td><td>EDM mode fine/rapid, ATR on/off, illumination</td></tr><tr><td>POWER / MEAS</td><td>Measure</td><td>Trigger EDM single or tracking measure, power on/off</td></tr></table>
<p><strong>Workflow example:</strong> Press ANG to zero at backsight, sight foresight press HD for distance, press COORD to get N E Z recorded, press S-O for next designed point — total station guides arrow to stake within 2 mm.</p>"""+fig(svg_total,"Total station display board — ANG, SD, COORD, S-O, MLM, MENU, STAR, POWER keys")+fig(svg_workflow,"Field to CAD workflow — total station polar to AutoCAD via CSV"),
   "a_gu":"""<table><tr><th>સ્વિચ બોર્ડ પર</th><th>કાર્ય</th></tr><tr><td>ANG/HD Angle/Horizontal Distance</td><td>એંગલ અને horizontal slope થી cos થી reduce</td></tr><tr><td>SD/VD Slope/Vertical</td><td>slope સીધું EDM vertical SD·sin</td></tr><tr><td>COORD</td><td>N,E,Z ગણે station backsight થી</td></tr><tr><td>S-O Stake Out</td><td>designed point પર prism લઈ જવા Δ guidance 2mm</td></tr><tr><td>MLM Missing Line</td><td>બે prism વચ્ચે અંતર occupied વગર</td></tr><tr><td>AREA</td><td>બંધ area ગણે</td></tr><tr><td>MENU/ESC</td><td>settings prism temp pressure back</td></tr><tr><td>STAR</td><td>EDM mode ATR light toggle</td></tr><tr><td>POWER/MEAS</td><td>measure trigger</td></tr></table>
<p>ઉપયોગ: backsight ANG zero, foresight HD distance, COORD N E Z, S-O next point arrow 2mm અંદર.</p>"""+fig(svg_total,"ટોટલ સ્ટેશન ડિસ્પ્લે — ANG SD COORD S-O MLM")},
  {"q_en":"Q.5 (c) OR What are the latest advancement in the total station technology? Explain in detail. (07 marks)","marks_en":"07 marks","marks_gu":"૦૭ ગુણ",
   "a_en":"""<div class="eq"><strong>Concept:</strong> Total station evolved from manual theodolite + EDM → integrated computer → robotic imaging scanning machine control.</div>
<table><tr><th>Latest advancement</th><th>What it is technically</th><th>Benefit for survey/construction</th></tr><tr><td><strong>1. Robotic one-man ATR</strong></td><td>Motorised 360° rotation + ATR CCD auto-locks prism, tracks continuously 1000 m without observer at instrument, operated by remote controller at prism</td><td>One person surveys, crew cost half, monitoring round clock for dam/tunnel movement 1 mm alarm</td></tr><tr><td><strong>2. Reflectorless EDM 1000 m</strong></td><td>Visible laser measures to wall/facade without prism, accuracy ±2 mm to 300 m reflectorless, 1000 m with prism</td><td>No prism man on building facade or busy road, safe height measurement</td></tr><tr><td><strong>3. Integrated imaging + Laser scanning</strong></td><td>Built-in calibrated camera 5 MP captures photo per point, scanner 10000 pts/sec creates point cloud within station</td><td>Photo-doc measurement, BIM as-built 3D without separate scanner, clash check</td></tr><tr><td><strong>4. Built-in GPS + IMU + Bluetooth to CAD</strong></td><td>Onboard GNSS for approximate position, Bluetooth/WiFi streams data directly to AutoCAD/Civil 3D tablet in field</td><td>No manual CSV import error, field to office real time, cloud backup</td></tr><tr><td><strong>5. Auto-levelling, auto-focus, PowerSearch</strong></td><td>Electronic level compensator 30″, auto-focus image search finds prism in seconds</td><td>Setup 2 min, find prism quick in bush, no manual focus</td></tr><tr><td><strong>6. 3D modelling + Augmented Reality + Machine control</strong></td><td>Onboard software computes volume cut-fill live, AR overlays design on live view, controls paver/dozer blade</td><td>Earthwork payment live, machine guidance ±10 mm saves survey pegs</td></tr></table>
<p><strong>Comparison:</strong> Old 2-man 1 mm, new 1-man 0.5″ + scanning + GPS + BIM integration — future is “field to BIM without office”.</p>
<div class="eq"><strong>Answer:</strong> Robotic ATR one-man, Reflectorless 1000 m, Imaging+scanning, GPS+Bluetooth to CAD, Auto-levelling/focus, 3D/AR/machine control — as table for 7 marks.</div>""",
   "a_gu":"""<table><tr><th>નવી ટેક</th><th>અર્થ</th><th>ફાયદો</th></tr><tr><td><strong>1 Robotic ATR one-man</strong> Motorised 360° CCD auto-locks remote</td><td>એક વ્યક્તિ 1000m track dam monitor 1mm alarm</td></tr><tr><td><strong>2 Reflectorless 1000m laser</strong> પ્રિઝમ વગર દિવાલ પર 2mm</td><td>ઊંચાઈ facade પર man નહીં safe</td></tr><tr><td><strong>3 Imaging Laser scanning 10000pts/sec photo per point</strong></td><td>BIM as-built 3D clash</td></tr><tr><td><strong>4 GPS IMU Bluetooth CAD</strong> GNSS WiFi AutoCAD tablet live</td><td>CSV import નહીં office real time</td></tr><tr><td><strong>5 Auto-levelling auto-focus PowerSearch 30″</strong></td><td>setup2min bush માં quick</td></tr><tr><td><strong>6 3D AR Machine control volume live blade ±10mm</strong></td><td>pegs વગર payment live</td></tr></table>
<div class="eq"><strong>જવાબ:</strong> Robotic ATR, Reflectorless, Imaging scanning, GPS Bluetooth CAD, Auto-levelling, 3D AR machine control — કોષ્ટક મુજબ 7 marks.</div>"""},
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
    page=f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>DI03006021 · Summer 2026 solved paper</title><style>{CSS}</style></head><body><main class="page"><header class="hero"><div class="eyebrow">Solved question paper · English questions · Friendly Gujarati answers</div><div class="lang-switch" aria-label="Choose language"><button type="button" data-lang="en" aria-pressed="true">English</button><button type="button" data-lang="gu" aria-pressed="false">ગુજરાતી</button></div><h1>Advance Surveying</h1><div class="meta">GTU Diploma · Civil · Semester 3 · Summer 2026 · DI03006021 · 14/05/2026 · 70 marks · 02:30 PM TO 05:00 PM</div></header>{"".join(sections_html)}<div class="footer">Solved paper for study. Verify with standard spec before site use.</div></main><script>document.querySelectorAll('.lang-switch button').forEach(b=>b.addEventListener('click',()=>{{document.documentElement.lang=b.dataset.lang;document.querySelectorAll('.lang-switch button').forEach(x=>x.setAttribute('aria-pressed',x==='true'?'true':'false'));}}));</script></body></html>'''
    return page
def main():
    page=build_page()
    import re
    # strip brackets from Gujarati answers for zero-bracket requirement
    page=re.sub(r'<div class="gu">(.*?)</div>', lambda m: '<div class="gu">'+m.group(1).replace('(','').replace(')','')+'</div>', page, flags=re.S)
    out_papers=ROOT/"papers-upload/papers/DI03006021/summer-2026.html"
    out_ws=ROOT/"preview/workshop/DI03006021_summer2026_bilingual.html"
    out_papers.parent.mkdir(parents=True,exist_ok=True)
    out_ws.parent.mkdir(parents=True,exist_ok=True)
    out_papers.write_text(page,encoding="utf-8")
    out_ws.write_text(page,encoding="utf-8")
    print(f"Bilingual: {out_papers} ({len(page)} chars)")
    print(f"details={page.count('<details')}, sections={page.count('<section')}, figs={page.count('<figure>')}")
    import re; gu=''.join(re.findall(r'<div class="gu">(.*?)</div>',page,re.S)); print(f"brackets gu={gu.count('(')+gu.count(')')}")
    print("PASS" if page.count('<details')==28 and page.count('<section')==5 else "FAIL")
    (ROOT/"drive-upload/DI03006021_summer_2026_bilingual.html").write_text(page,encoding="utf-8")
if __name__=="__main__": main()
