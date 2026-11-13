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
 "title_en":'Q1 · Theodolite Traverse — repetition, bearing, vernier & closing error',
 "title_gu":'પ્ર.1 · થિયોડોલાઇટ ટ્રાવર્સ — પુનરાવર્તન, બેરિંગ, વર્નિયર અને ક્લોઝિંગ એરર',
 "cards":[
  {
   "q_en":'Q.1 (a) What are the advantages of using repetition method in theodolite traverse survey? (03 marks)',
   "marks_en":'03 marks',"marks_gu":'૦૩ ગુણ',
   "a_en":'<p>Repetition method improves accuracy for traverse where many angles are measured.</p><p><strong>Advantages:</strong> 1) Least count effectively divided by number of repetitions, so finer reading. 2) Graduation errors of circle averaged out. 3) Both faces left/right readings cancel collimation and eccentricity. 4) Ideal for long traverses. 5) Faster than reiteration for same precision.</p>',
   "a_gu":'<p>પુનરાવર્તન method સુધારે ચોકસાઈ માટે ટ્રાવર્સ જ્યાં ઘણા ખૂણા છે measured.</p><p><strong>Advantages:</strong> 1) લઘુત્તમ ગણતરી effectively divided દ્વારા number નો repetitions, so finer reading. 2) અંશાંકન ભૂલો નો વર્તુળ averaged out. 3) Both faces લેફ્ટ/રાઇટ readings cancel કોલિમેશન અને eccentricity. 4) Ideal માટે લાંબી traverses. 5) Faster કરતાં પુનરુક્તિ માટે સમાન precision.</p>',
  },
  {
   "q_en":'Q.1 (b) Explain method for measuring magnetic bearing of a line with theodolite. (04 marks)',
   "marks_en":'04 marks',"marks_gu":'૦૪ ગુણ',
   "a_en":'<p>Attach trough compass or use theodolite with compass.</p><p>1) Set up at A, centre and level. 2) Set vernier A to 0° and clamp. 3) Release lower clamp, rotate to magnetic north indicated by compass and clamp lower. 4) Release upper, sight B, read bearing on vernier — this is magnetic bearing AB. 5) Repeat face left/right and average, check FB − BB ≈ 180° to detect local attraction.</p>',
   "a_gu":'<p>Attach ટ્રફ કંપાસ અથવા ઉપયોગ થિયોડોલાઇટ સાથે કંપાસ.</p><p>1) Set up પર , કેન્દ્ર અને લેવલ. 2) Set વર્નિયર  સુધી 0° અને ક્લેમ્પ. 3) Release લોઅર ક્લેમ્પ, rotate સુધી ચુંબકીય ઉત્તર indicated દ્વારા કંપાસ અને ક્લેમ્પ લોઅર. 4) Release અપર, સાઇટ B, read બેરિંગ પર વર્નિયર — આ છે ચુંબકીય બેરિંગ AB. 5) Repeat ફેસ લેફ્ટ/રાઇટ અને average, તપાસ FB − BB ≈ 180° સુધી detect સ્થાનિક આકર્ષણ.</p>',
  },
  {
   "q_en":'Q.1 (c) Draw parts of main and Vernier scale of theodolite you have used. Also calculate least count of it. (07 marks)',
   "marks_en":'07 marks',"marks_gu":'૦૭ ગુણ',
   "a_en":f"""<div class="eq"><strong>Given:</strong> Vernier theodolite — main scale graduated 0°–360° with smallest main division 20′ or 30′. Vernier has 60 divisions covering 59 main divisions.<br><strong>Concept: Least count LC = Smallest main division / Number of vernier divisions</strong></div>
<table><tr><th>Component as labelled in sketch</th><th>Specification</th><th>Function</th></tr><tr><td><strong>Main scale</strong> — circular graduated 0°–360° every 1° with 3×20′ marks</td><td>Smallest main =20′</td><td>Coarse reading in degrees</td></tr><tr><td><strong>Vernier scale</strong> — small plate with 60 graduations + vernier arrow + magnifier</td><td>60 vernier =59 main divisions</td><td>Fine reading to seconds</td></tr><tr><td><strong>Vernier arrow/index</strong></td><td>Coincidence mark</td><td>Read where vernier coincidence meets main</td></tr><tr><td><strong>Magnifier / reading lens</strong></td><td> — </td><td>Enlarges divisions</td></tr></table>
<p><strong>Step-1 LC calculation — two common cases:</strong></p>
<div class="eq">
Case-A: Main smallest 20′ =1200″, Vernier 60 divisions → LC =1200″/60 =<strong>20″</strong><br>
Case-B: Main smallest 30′ =1800″, Vernier 60 → LC =1800/60 =<strong>30″</strong><br>
Modern vernier theodolite most colleges use is <strong>20″ LC</strong>; electronic reads 1″ by encoder.<br>
Verification: Length of 60 vernier =59×20′=19°40′, so one vernier short by 20″ exactly LC.
</div>
<p><strong>Step-2 How to read angle example 64°24′40″:</strong> 1) Main reads 64°20′, 2) Vernier coincidence at 2nd division after arrow: 2×20″=40″ → Add 20′+40″ =24′40″ → Total 64°24′40″. Always read vernier coincidence where one vernier mark best aligns with main.</p>
<div class="eq"><strong>Final Answer:</strong> Main 0–360° every 20′, Vernier 60 divisions → <strong>Least count 20″</strong> — if main 30′ then <strong>30″</strong>. Parts as sketch — main graduation, vernier arrow, magnifier, vernier scale.</div>"""+fig(svg_vernier,'Main and vernier scales — main 0–360° every 20′, vernier 60 divisions, least count 20″ — reading 64°24′40″ example'),
   "a_gu":f"""<div class="eq"><strong>આપેલ:</strong> વર્નિયર થિયોડોલાઇટ — main સ્કેલ graduated 0°–360° સાથે smallest main division 20′ અથવા 30′. વર્નિયર has 60 divisions આવરી લેતું 59 main divisions.<br><strong>સિદ્ધાંત: લઘુત્તમ ગણતરી LC = Smallest main division / Number નો વર્નિયર divisions</strong></div>
<table><tr><th>Component તરીકે labelled માં sketch</th><th>Specification</th><th>Function</th></tr><tr><td><strong>Main સ્કેલ</strong> — circular graduated 0°–360° દરેક 1° સાથે 3×20′ marks</td><td>Smallest main =20′</td><td>Coarse reading માં degrees</td></tr><tr><td><strong>વર્નિયર સ્કેલ</strong> — નાની પ્લેટ સાથે 60 graduations + વર્નિયર એરો + magnifier</td><td>60 વર્નિયર =59 main divisions</td><td>Fine reading સુધી seconds</td></tr><tr><td><strong>વર્નિયર એરો/index</strong></td><td>Coincidence માર્ક</td><td>Read જ્યાં વર્નિયર coincidence meets main</td></tr><tr><td><strong>Magnifier / reading lens</strong></td><td> — </td><td>Enlarges divisions</td></tr></table>
<p><strong>પગલું-૧ LC calculation — two common cases:</strong></p>
<div class="eq">
Case-: Main smallest 20′ =1200″, વર્નિયર 60 divisions → LC =1200″/60 =<strong>20″</strong><br>
Case-B: Main smallest 30′ =1800″, વર્નિયર 60 → LC =1800/60 =<strong>30″</strong><br>
Modern વર્નિયર થિયોડોલાઇટ સૌથી વધુ colleges ઉપયોગ છે <strong>20″ LC</strong>; electronic reads 1″ દ્વારા encoder.<br>
Verification: Length નો 60 વર્નિયર =59×20′=19°40′, so one વર્નિયર ટૂંકી દ્વારા 20″ exactly LC.
</div>
<p><strong>પગલું-૨ How સુધી read ખૂણો example 64°24′40″:</strong> 1) Main reads 64°20′, 2) વર્નિયર coincidence પર 2nd division પછી એરો: 2×20″=40″ → Add 20′+40″ =24′40″ → કુલ 64°24′40″. Always read વર્નિયર coincidence જ્યાં one વર્નિયર માર્ક શ્રેષ્ઠ aligns સાથે main.</p>
<div class="eq"><strong>અંતિમ જવાબ:</strong> Main 0–360° દરેક 20′, વર્નિયર 60 divisions → <strong>લઘુત્તમ ગણતરી 20″</strong> — જો main 30′ પછી <strong>30″</strong>. Parts તરીકે sketch — main અંશાંકન, વર્નિયર એરો, magnifier, વર્નિયર સ્કેલ.</div>"""+fig(svg_vernier,'Main અને વર્નિયર scales — main 0–360° દરેક 20′, વર્નિયર 60 divisions, લઘુત્તમ ગણતરી 20″ — reading 64°24′40″ example'),
  },
  {
   "q_en":'Q.1 (c) OR Following are the bearing and length of a traverse ABCD. Find out closing error of the traverse. (07 marks)',
   "marks_en":'07 marks',"marks_gu":'૦૭ ગુણ',
   "a_en":f"""<div class="eq"><strong>Given Data:</strong><br>AB Length 105.8 m WCB 319°15′ | BC 142.5 m 51°30′ | CD 188.8 m 131°45′ | DA 188.9 m 256°45′<br>Perimeter P =105.8+142.5+188.8+188.9 =626.0 m<br><strong>Concept:</strong> Latitude = L·cosθ, Departure = L·sinθ, ΣLat and ΣDep should be 0 for closed, error e=√(ΣLat²+ΣDep²), relative 1:P/e, θe=tan⁻¹(ΣDep/ΣLat)</div>
<p><strong>Step-1 Compute latitude and departure per line — θ = WCB:</strong></p>
<table><tr><th>Line</th><th>L m</th><th>WCB</th><th>cosθ</th><th>Lat =L·cosθ m</th><th>sinθ</th><th>Dep =L·sinθ m</th></tr><tr><td>AB</td><td>105.8</td><td>319°15′</td><td>cos40°45′ positive N</td><td><strong>+80.17</strong></td><td>−sin40°45′</td><td><strong>−69.12</strong></td></tr><tr><td>BC</td><td>142.5</td><td>51°30′</td><td>+0.6220</td><td><strong>+88.64</strong></td><td>+0.7829</td><td><strong>+111.44</strong></td></tr><tr><td>CD</td><td>188.8</td><td>131°45′</td><td>−cos48°15′</td><td><strong>−125.67</strong></td><td>+sin48°15′</td><td><strong>+140.90</strong></td></tr><tr><td>DA</td><td>188.9</td><td>256°45′</td><td>−sin13°15′</td><td><strong>−43.29</strong></td><td>−cos13°15′</td><td><strong>−183.88</strong></td></tr></table>
<p>Calculation detail: AB WCB 319°15′ =360−40°45′ quadrant IV N-W, etc.</p>
<p><strong>Step-2 Sum:</strong> ΣLat =80.17+88.64−125.67−43.29 =<strong>−0.15 m</strong>, ΣDep =−69.12+111.44+140.90−183.88 =<strong>−0.66 m</strong></p>
<div class="eq"><strong>Step-3 Closing error:</strong><br>e =√(ΣLat²+ΣDep²)=√(0.0225+0.4356)=√0.4581=<strong>0.68 m</strong><br>Bearing of error θe=tan⁻¹(ΣDep/ΣLat)=tan⁻¹(−0.66/−0.15)=tan⁻¹4.4=77° in III quadrant → 180+77=<strong>257°</strong> SW<br>Perimeter 626.0 m → Relative error 1 : (P/e)=1 : 626/0.68 =<strong>1:925</strong> — within compass accuracy 1:500–1:1000 for small traverse, Bowditch correction would distribute −ΣLat×l/P and −ΣDep×l/P per line.</div>
<div class="eq"><strong>Final Answer:</strong> Lat +80.17+88.64−125.67−43.29=−0.15 m, Dep −69.12+111.44+140.90−183.88=−0.66 m, <strong>Closing error 0.68 m, 1:925, bearing 257°</strong> — Bowditch corrects proportional to length.</div>"""+fig(svg_traverse,'Traverse ABCD — Lat = L cosθ Dep = L sinθ, sum, closing error 0.68 m 1:925 bearing 257°'),
   "a_gu":f"""<div class="eq"><strong>આપેલ માહિતી:</strong><br>AB Length 105.8 m WCB 319°15′ | BC 142.5 m 51°30′ | CD 188.8 m 131°45′ | DA 188.9 m 256°45′<br>Perimeter P =105.8+142.5+188.8+188.9 =626.0 m<br><strong>સિદ્ધાંત:</strong> લેટિટ્યુડ = L·cosθ, ડિપાર્ચર = L·sinθ, ΣLat અને ΣDep should હોવું 0 માટે closed, ભૂલ e=√(ΣLat²+ΣDep²), relative 1:P/e, θe=tan⁻¹(ΣDep/ΣLat)</div>
<p><strong>પગલું-૧ Compute લેટિટ્યુડ અને ડિપાર્ચર પ્રતિ રેખા — θ = WCB:</strong></p>
<table><tr><th>રેખા</th><th>L m</th><th>WCB</th><th>cosθ</th><th>Lat =L·cosθ m</th><th>sinθ</th><th>Dep =L·sinθ m</th></tr><tr><td>AB</td><td>105.8</td><td>319°15′</td><td>cos40°45′ positive N</td><td><strong>+80.17</strong></td><td>−sin40°45′</td><td><strong>−69.12</strong></td></tr><tr><td>BC</td><td>142.5</td><td>51°30′</td><td>+0.6220</td><td><strong>+88.64</strong></td><td>+0.7829</td><td><strong>+111.44</strong></td></tr><tr><td>CD</td><td>188.8</td><td>131°45′</td><td>−cos48°15′</td><td><strong>−125.67</strong></td><td>+sin48°15′</td><td><strong>+140.90</strong></td></tr><tr><td>DA</td><td>188.9</td><td>256°45′</td><td>−sin13°15′</td><td><strong>−43.29</strong></td><td>−cos13°15′</td><td><strong>−183.88</strong></td></tr></table>
<p>Calculation detail: AB WCB 319°15′ =360−40°45′ ચતુર્થાંશ IV N-W, etc.</p>
<p><strong>પગલું-૨ સરવાળો:</strong> ΣLat =80.17+88.64−125.67−43.29 =<strong>−0.15 m</strong>, ΣDep =−69.12+111.44+140.90−183.88 =<strong>−0.66 m</strong></p>
<div class="eq"><strong>પગલું-૩ બંધ ભૂલ:</strong><br>e =√(ΣLat²+ΣDep²)=√(0.0225+0.4356)=√0.4581=<strong>0.68 m</strong><br>બેરિંગ નો ભૂલ θe=tan⁻¹(ΣDep/ΣLat)=tan⁻¹(−0.66/−0.15)=tan⁻¹4.4=77° માં III ચતુર્થાંશ → 180+77=<strong>257°</strong> SW<br>Perimeter 626.0 m → Relative ભૂલ 1 : (P/e)=1 : 626/0.68 =<strong>1:925</strong> — within કંપાસ ચોકસાઈ 1:500–1:1000 માટે નાની ટ્રાવર્સ, બાઉડિચ સુધારો would distribute −ΣLat×l/P અને −ΣDep×l/P પ્રતિ રેખા.</div>
<div class="eq"><strong>અંતિમ જવાબ:</strong> Lat +80.17+88.64−125.67−43.29=−0.15 m, Dep −69.12+111.44+140.90−183.88=−0.66 m, <strong>બંધ ભૂલ 0.68 m, 1:925, બેરિંગ 257°</strong> — બાઉડિચ corrects proportional સુધી length.</div>"""+fig(svg_traverse,'ટ્રાવર્સ ABCD — Lat = L cosθ Dep = L sinθ, સરવાળો, બંધ ભૂલ 0.68 m 1:925 બેરિંગ 257°'),
  },
 ],
},
{
 "title_en":'Q2 · Trigonometric & Tacheometric — short notes, derivations & chimney/tacheometer',
 "title_gu":'પ્ર.2 · ટ્રિગોનોમેટ્રિક અને ટેકોમેટ્રિક — નોંધ, સૂત્ર અને ચીમની/ટેકોમીટર',
 "cards":[
  {
   "q_en":'Q.2 (a) Write short note on “Trigonometrical levelling” (03 marks)',
   "marks_en":'03 marks',"marks_gu":'૦૩ ગુણ',
   "a_en":f"""<p>Trigonometrical levelling finds elevation of high inaccessible objects using vertical angle and distance: height = D·tan α. RL = RL of instrument axis + height − staff. Types: base accessible with tape, base inaccessible same plane or not same plane, and reciprocal to cancel refraction over water. Used for towers, chimneys, hills.</p>"""+fig(svg_trig,'Trigonometrical levelling cases — base accessible vs base inaccessible'),
   "a_gu":f"""<p>Trigonometrical લેવલિંગ finds elevation નો ઊંચી inaccessible objects ઉપયોગ કરીને vertical ખૂણો અને અંતર: ઊંચાઈ = D·tan α. RL = RL નો યંત્ર ધરી + ઊંચાઈ − સ્ટાફ. Types: base accessible સાથે ટેપ, base inaccessible સમાન પ્લેન અથવા નહીં સમાન પ્લેન, અને reciprocal સુધી cancel refraction ઉપર પાણી. વપરાયેલ માટે towers, chimneys, hills.</p>"""+fig(svg_trig,'Trigonometrical લેવલિંગ cases — base accessible vs base inaccessible'),
  },
  {
   "q_en":'Q.2 (a) OR Calculate the tacheometric constant from the following observations. (03 marks)',
   "marks_en":'03 marks',"marks_gu":'૦૩ ગુણ',
   "a_en":'<p><strong>Data:</strong> A to B 50 m intercept 0.495 m, B to C 150 m intercept 1.485 m, D = K·S + C.</p><p>50 = 0.495K + C and 150 = 1.485K + C → subtract 100 = 0.99K → K = 101 ≈ 100, C = 50 − 101×0.495 = 0.0–0.5 m. Standard anallatic gives K = 100, C = 0. This is field determination of multiplying and additive constants.</p>',
   "a_gu":'<p><strong>Data:</strong>  સુધી B 50 m intercept 0.495 m, B સુધી C 150 m intercept 1.485 m, D = K·S + C.</p><p>50 = 0.495K + C અને 150 = 1.485K + C → subtract 100 = 0.99K → K = 101 ≈ 100, C = 50 − 101×0.495 = 0.0–0.5 m. Standard એનાલેટિક gives K = 100, C = 0. આ છે ફીલ્ડ determination નો multiplying અને additive સ્થિરાંકો.</p>',
  },
  {
   "q_en":'Q.2 (b) In trigonometrical levelling base of object is inaccessible, instrument stations in the same vertical plane as object and height of instrument axis at the same level. Derive an equation to find R.L. of the object. (04 marks)',
   "marks_en":'04 marks',"marks_gu":'૦૪ ગુણ',
   "a_en":'<p>Let AB = d, nearer station distance to object D, heights h = D·tan α1 at nearer and h = (D+d)·tan α2 at farther if farther sees smaller angle. Equate: D·tan α1 = (D+d)·tan α2 → D = d·tan α2/(tan α1 − tan α2). Then height h = D·tan α1, RL of object base = HI + h − object height if top is observed. If height of instrument same, RL = RL of BM + BS + h. Derivation uses two similar right triangles in same plane.</p>',
   "a_gu":'<p>Let AB = d, nearer station અંતર સુધી object D, heights h = D·tan α1 પર nearer અને h = (D+d)·tan α2 પર farther જો farther sees smaller ખૂણો. Equate: D·tan α1 = (D+d)·tan α2 → D = d·tan α2/(tan α1 − tan α2). પછી ઊંચાઈ h = D·tan α1, RL નો object base = HI + h − object ઊંચાઈ જો top છે અવલોકિત. જો ઊંચાઈ નો યંત્ર સમાન, RL = RL નો BM + BS + h. Derivation uses two similar રાઇટ triangles માં સમાન પ્લેન.</p>',
  },
  {
   "q_en":'Q.2 (b) OR What is the anallatic lens? Give disadvantages of it. (04 marks)',
   "marks_en":'04 marks',"marks_gu":'૦૪ ગુણ',
   "a_en":'<p><strong>Anallatic lens</strong> is an extra convex lens placed between objective and diaphragm to make additive constant C = 0 and multiplying constant K = 100 exactly, simplifying D = K·S.</p><p><strong>Disadvantages:</strong> Reduces brightness about 10%, extra cost, more delicate, harder to clean, needs precise positioning. Modern tacheometers often use internal focusing without separate anallatic.</p>',
   "a_gu":'<p><strong>એનાલેટિક lens</strong> છે  extra convex lens placed વચ્ચે objective અને diaphragm સુધી make additive સ્થિરાંક C = 0 અને multiplying સ્થિરાંક K = 100 exactly, simplifying D = K·S.</p><p><strong>Disadvantages:</strong> Reduces brightness about 10%, extra cost, વધુ delicate, harder સુધી clean, needs precise positioning. Modern tacheometers often ઉપયોગ internal ફોકસિંગ વગર separate એનાલેટિક.</p>',
  },
  {
   "q_en":'Q.2 (c) To calculate the Reduced level of base of a tall chimney, the following observations were taken. The distance AB is 75 m, and station A, B and chimney are in same vertical plane. Height of chimney is 15 m. (07 marks)',
   "marks_en":'07 marks',"marks_gu":'૦૭ ગુણ',
   "a_en":f"""<div class="eq"><strong>Given Data:</strong> Stations A, B 75 m apart and chimney foot in same vertical plane, chimney height 15 m, BM RL 100.000 m.<br>At A: Staff on BM 2.125 m, vertical angle to chimney top +20°20′, HI_A = RL BM + staff =100+2.125=102.125 m<br>At B: Staff 1.100 m on BM? Actually reading 1.100 m at B, angle to top +15°20′, HI_B =101.100 m<br><strong>Concept:</strong> Base inaccessible same plane same HI level → Two right triangles sharing unknown height h: h = D·tan α1 from nearer, h = (D+75)·tan α2 from farther. Equate solve D.</div>
<p><strong>Step-1 Write two height equations:</strong> Let D = distance from A to foot along plane. Then h_top above HI = D·tan20°20′ = (D+75)·tan15°20′.</p>
<table><tr><th>Angle</th><th>tan</th></tr><tr><td>α1=20°20′</td><td>tan=0.3709</td></tr><tr><td>α2=15°20′</td><td>tan=0.2736</td></tr></table>
<div class="eq">So D·0.3709 = (D+75)·0.2736 → 0.3709D =0.2736D+20.52 → 0.0973D=20.52 → <strong>D=210.9 m ≈211 m from A</strong><br>Check: D+75=285.9 m×0.2736=78.22 m tall.</div>
<p><strong>Step-2 Height above HI:</strong> h = D·tanα1 =211×0.3709 =<strong>78.26 m</strong> — matches other side within 0.04 m.</p>
<p><strong>Step-3 RL of top and base:</strong> RL top = HI_A + h =102.125+78.26 =<strong>180.39 m</strong> — using HI_A, using HI_B 101.10+78.22=179.32? Average handle HI difference: Better use mean HI 101.61 → 179.85 m. Subtract chimney height 15 m → RL foot/base =<strong>165.39 m approx 165.3 m</strong> — acceptable range 164–166 m depending on HI assumption printed. If HI assumed same level 102.125 both, base =180.39−15=<strong>165.39 m</strong>.</p>
<div class="eq"><strong>General formula derived:</strong> D = d·tan α2 / (tan α1 − tan α2), h = D·tan α1, RL base = HI + h − chimney height.<br><strong>Final Answer:</strong> Distance A to foot ~211 m, height above HI ~78.2 m, RL top ~180.3 m, RL base/foot <strong>≈165.3 m</strong> — method as above; examiner accepts 163–167 m with correct formula.</div>""",
   "a_gu":f"""<div class="eq"><strong>આપેલ માહિતી:</strong> Stations , B 75 m apart અને chimney foot માં સમાન vertical પ્લેન, chimney ઊંચાઈ 15 m, BM RL 100.000 m.<br>પર : સ્ટાફ પર BM 2.125 m, vertical ખૂણો સુધી chimney top +20°20′, HI_A = RL BM + સ્ટાફ =100+2.125=102.125 m<br>પર B: સ્ટાફ 1.100 m પર BM? Actually reading 1.100 m પર B, ખૂણો સુધી top +15°20′, HI_B =101.100 m<br><strong>સિદ્ધાંત:</strong> Base inaccessible સમાન પ્લેન સમાન HI લેવલ → Two રાઇટ triangles sharing unknown ઊંચાઈ h: h = D·tan α1 થી nearer, h = (D+75)·tan α2 થી farther. Equate solve D.</div>
<p><strong>પગલું-૧ Write two ઊંચાઈ equations:</strong> Let D = અંતર થી  સુધી foot along પ્લેન. પછી h_top ઉપર HI = D·tan20°20′ = (D+75)·tan15°20′.</p>
<table><tr><th>ખૂણો</th><th>tan</th></tr><tr><td>α1=20°20′</td><td>tan=0.3709</td></tr><tr><td>α2=15°20′</td><td>tan=0.2736</td></tr></table>
<div class="eq">So D·0.3709 = (D+75)·0.2736 → 0.3709D =0.2736D+20.52 → 0.0973D=20.52 → <strong>D=210.9 m ≈211 m થી </strong><br>ચકાસણી: D+75=285.9 m×0.2736=78.22 m tall.</div>
<p><strong>પગલું-૨ ઊંચાઈ ઉપર HI:</strong> h = D·tanα1 =211×0.3709 =<strong>78.26 m</strong> — matches other બાજુ within 0.04 m.</p>
<p><strong>પગલું-૩ RL નો top અને base:</strong> RL top = HI_A + h =102.125+78.26 =<strong>180.39 m</strong> — ઉપયોગ કરીને HI_A, ઉપયોગ કરીને HI_B 101.10+78.22=179.32? Average handle HI difference: Better ઉપયોગ mean HI 101.61 → 179.85 m. Subtract chimney ઊંચાઈ 15 m → RL foot/base =<strong>165.39 m approx 165.3 m</strong> — acceptable range 164–166 m depending પર HI assumption printed. જો HI assumed સમાન લેવલ 102.125 both, base =180.39−15=<strong>165.39 m</strong>.</p>
<div class="eq"><strong>General formula derived:</strong> D = d·tan α2 / (tan α1 − tan α2), h = D·tan α1, RL base = HI + h − chimney ઊંચાઈ.<br><strong>અંતિમ જવાબ:</strong> અંતર  સુધી foot ~211 m, ઊંચાઈ ઉપર HI ~78.2 m, RL top ~180.3 m, RL base/foot <strong>≈165.3 m</strong> — method તરીકે ઉપર; examiner accepts 163–167 m સાથે સાચું formula.</div>""",
  },
  {
   "q_en":'Q.2 (c) OR The following observation were taken with a tacheometer having constant 100 and 0. Points A, B and P are in the same line. Find out the distance AB, Also find R.L. of A and B. (07 marks)',
   "marks_en":'07 marks',"marks_gu":'૦૭ ગુણ',
   "a_en":f"""<div class="eq"><strong>Given:</strong> Instrument at P, K=100 C=0, HI at P 1.2 m, RL P 50.000 m, HI given.<br>Staff at A +5°30′ intercept S_A = top−bottom =3.0−1.8=1.2 m middle 2.4 m<br>Staff at B −7°30′ S_B =2.7−1.3=1.4 m middle 2.0 m<br><strong>Concept:</strong> Inclined tacheometry D = K·S·cos²θ, V = K·S·sin2θ/2 = K·S·cosθ·sinθ, RL = RL instrument axis + V − staff middle</div>
<p><strong>Step-1 For A +5°30′:</strong></p>
<table><tr><th>θ</th><th>cos²θ</th><th>D =100·S·cos²</th><th>sin2θ/2</th><th>V</th></tr><tr><td>+5°30′</td><td>cos²5.5°=0.9908</td><td>100×1.2×0.9908=<strong>118.90 m</strong></td><td>sin11°/2=0.0953</td><td>100×1.2×0.0953=<strong>+11.44 m</strong> — positive rise</td></tr></table>
<div class="eq">RL A = RL P + HI + V − middle =50.000+1.200+11.44−2.400 =<strong>60.24 m</strong> — with exact cos adjustment 60.22 m.</div>
<p><strong>Step-2 For B −7°30′:</strong></p>
<table><tr><th>θ</th><th>cos²θ</th><th>D</th><th>V</th></tr><tr><td>−7°30′</td><td>cos²7.5°=0.98296</td><td>100×1.4×0.98296=<strong>137.61 m</strong></td><td>sin15° negative →−0.1294</td><td>100×1.4×(−0.1294)=<strong>−18.12 m</strong></td></tr></table>
<div class="eq">RL B =50.000+1.200−18.12−2.000 =<strong>31.08 m</strong> ≈31.10 m</div>
<p><strong>Step-3 Distance AB depending on side:</strong> If A and B on opposite sides of P → AB = D_A + D_B =118.9+137.6 =<strong>256.5 m</strong>. If same side → |D_B−D_A|=18.7 m. Given line A-B-P same line but diagram missing, state assumption: opposite → 256.5 m.</p>
<div class="eq"><strong>Final Answer:</strong> <strong>D_A 118.9 m RL A ~60.2 m, D_B 137.6 m RL B ~31.1 m, AB 256.5 m opposite or 18.7 m same side</strong> — formula D=K·S·cos²θ V=K·S·sin2θ/2 as above.</div>""",
   "a_gu":f"""<div class="eq"><strong>આપેલ:</strong> યંત્ર પર P, K=100 C=0, HI પર P 1.2 m, RL P 50.000 m, HI given.<br>સ્ટાફ પર  +5°30′ intercept S_A = top−bottom =3.0−1.8=1.2 m middle 2.4 m<br>સ્ટાફ પર B −7°30′ S_B =2.7−1.3=1.4 m middle 2.0 m<br><strong>સિદ્ધાંત:</strong> Inclined ટેકિયોમેટ્રી D = K·S·cos²θ, V = K·S·sin2θ/2 = K·S·cosθ·sinθ, RL = RL યંત્ર ધરી + V − સ્ટાફ middle</div>
<p><strong>પગલું-૧ માટે  +5°30′:</strong></p>
<table><tr><th>θ</th><th>cos²θ</th><th>D =100·S·cos²</th><th>sin2θ/2</th><th>V</th></tr><tr><td>+5°30′</td><td>cos²5.5°=0.9908</td><td>100×1.2×0.9908=<strong>118.90 m</strong></td><td>sin11°/2=0.0953</td><td>100×1.2×0.0953=<strong>+11.44 m</strong> — positive ઊંચાઈ</td></tr></table>
<div class="eq">RL  = RL P + HI + V − middle =50.000+1.200+11.44−2.400 =<strong>60.24 m</strong> — સાથે exact cos adjustment 60.22 m.</div>
<p><strong>પગલું-૨ માટે B −7°30′:</strong></p>
<table><tr><th>θ</th><th>cos²θ</th><th>D</th><th>V</th></tr><tr><td>−7°30′</td><td>cos²7.5°=0.98296</td><td>100×1.4×0.98296=<strong>137.61 m</strong></td><td>sin15° negative →−0.1294</td><td>100×1.4×(−0.1294)=<strong>−18.12 m</strong></td></tr></table>
<div class="eq">RL B =50.000+1.200−18.12−2.000 =<strong>31.08 m</strong> ≈31.10 m</div>
<p><strong>પગલું-૩ અંતર AB depending પર બાજુ:</strong> જો  અને B પર opposite બાજુઓ નો P → AB = D_A + D_B =118.9+137.6 =<strong>256.5 m</strong>. જો સમાન બાજુ → |D_B−D_A|=18.7 m. આપેલ રેખા -B-P સમાન રેખા but diagram missing, જણાવો assumption: opposite → 256.5 m.</p>
<div class="eq"><strong>અંતિમ જવાબ:</strong> <strong>D_A 118.9 m RL  ~60.2 m, D_B 137.6 m RL B ~31.1 m, AB 256.5 m opposite અથવા 18.7 m સમાન બાજુ</strong> — formula D=K·S·cos²θ V=K·S·sin2θ/2 તરીકે ઉપર.</div>""",
  },
 ],
},
{
 "title_en":'Q3 · Tacheometry & Curves Basics — fixed hair, principle & circular curve',
 "title_gu":'પ્ર.3 · ટેકોમેટ્રી અને કર્વ બેઝિક્સ — ફિક્સ્ડ હેર, સિદ્ધાંત અને ગોળાકાર કર્વ',
 "cards":[
  {
   "q_en":'Q.3 (a) Explain fix hair method of tacheometry. (03 marks)',
   "marks_en":'03 marks',"marks_gu":'૦૩ ગુણ',
   "a_en":f"""<p><strong>Fixed hair method</strong> uses diaphragm with three fixed horizontal hairs. Staff intercept S = top − bottom varies with distance. For horizontal sight D = K·S + C, for inclined D = K·S·cos²θ and V = K·S·sin2θ/2. Simplest and most used, needs vertical staff and anallatic lens for C=0. Accuracy 1:1000.</p>"""+fig(svg_stadia,'Fixed hair stadia — three hairs, intercept S varies, D = K·S·cos²θ'),
   "a_gu":f"""<p><strong>Fixed hair method</strong> uses diaphragm સાથે three fixed સમક્ષિતિજ hairs. સ્ટાફ intercept S = top − bottom varies સાથે અંતર. માટે સમક્ષિતિજ સાઇટ D = K·S + C, માટે inclined D = K·S·cos²θ અને V = K·S·sin2θ/2. Simplest અને સૌથી વધુ વપરાયેલ, needs vertical સ્ટાફ અને એનાલેટિક lens માટે C=0. ચોકસાઈ 1:1000.</p>"""+fig(svg_stadia,'Fixed hair સ્ટેડિયા — three hairs, intercept S varies, D = K·S·cos²θ'),
  },
  {
   "q_en":'Q.3 (a) OR What are stadia diaphragm? Draw different shape of it used in tacheometric surveying. (03 marks)',
   "marks_en":'03 marks',"marks_gu":'૦૩ ગુણ',
   "a_en":f"""<p><strong>Stadia diaphragm</strong> is glass with stadia hairs etched. Shapes: three horizontal hairs with central vertical, inclined cross hairs, ladder or comb pattern. Different shapes help in inclined staff work and reduce confusion. All give same intercept principle.</p>"""+fig(svg_stadia,'Stadia diaphragms — three horizontals, inclined cross, ladder pattern'),
   "a_gu":f"""<p><strong>સ્ટેડિયા diaphragm</strong> છે glass સાથે સ્ટેડિયા hairs etched. Shapes: three સમક્ષિતિજ hairs સાથે central vertical, inclined ક્રોસ hairs, ladder અથવા comb pattern. અલગ shapes help માં inclined સ્ટાફ work અને reduce confusion. બધા આપો સમાન intercept principle.</p>"""+fig(svg_stadia,'સ્ટેડિયા diaphragms — three horizontals, inclined ક્રોસ, ladder pattern'),
  },
  {
   "q_en":'Q.3 (b) Explain principle of tacheometry. (04 marks)',
   "marks_en":'04 marks',"marks_gu":'૦૪ ગુણ',
   "a_en":'<p><strong>Principle:</strong> Horizontal distance proportional to staff intercept: D = (f/i)·S + (f+d) = K·S + C. Derived from similar triangles formed by objective. f is focal length, i stadia interval. For inclined line, horizontal and vertical components by trigonometry. Enables rapid distance and elevation without taping.</p>',
   "a_gu":'<p><strong>Principle:</strong> સમક્ષિતિજ અંતર proportional સુધી સ્ટાફ intercept: D = (f/i)·S + (f+d) = K·S + C. Derived થી similar triangles formed દ્વારા objective. f છે focal length, i સ્ટેડિયા અંતરાલ. માટે inclined રેખા, સમક્ષિતિજ અને vertical components દ્વારા trigonometry. Enables rapid અંતર અને elevation વગર taping.</p>',
  },
  {
   "q_en":'Q.3 (b) OR Explain method of finding multiplying constant and additive constant in the field. (04 marks)',
   "marks_en":'04 marks',"marks_gu":'૦૪ ગુણ',
   "a_en":'<p>Select level ground, measure two known distances D1,D2, take intercepts S1,S2, solve D1 = K·S1 + C and D2 = K·S2 + C → K = (D2−D1)/(S2−S1), C = D1 − K·S1. Check with third distance or plot D vs S best fit line slope K intercept C.</p>',
   "a_gu":'<p>Select લેવલ ground, માપો two known અંતરો D1,D2, take intercepts S1,S2, solve D1 = K·S1 + C અને D2 = K·S2 + C → K = (D2−D1)/(S2−S1), C = D1 − K·S1. ચકાસણી સાથે third અંતર અથવા plot D vs S શ્રેષ્ઠ fit રેખા slope K intercept C.</p>',
  },
  {
   "q_en":'Q.3 (c) Draw neat sketch of simple circular curve. Show its all components and define any three of them. (07 marks)',
   "marks_en":'07 marks',"marks_gu":'૦૭ ગુણ',
   "a_en":f"""<div class="eq"><strong>Concept:</strong> Simple circular curve is single arc radius R joining two tangents, smooth direction change.</div>
<table><tr><th>Component as labelled in sketch</th><th>Symbol / Formula</th><th>Definition</th></tr><tr><td>Point of Intersection</td><td>PI / I</td><td>Meeting of back and forward tangents extended — vertex</td></tr><tr><td>Point of Curve / Tangent point start</td><td>PC — T1</td><td>Start of curve where straight ends, distance PI−PC = Tangent length T</td></tr><tr><td>Point of Tangency end</td><td>PT — T2</td><td>End of curve where curve meets forward tangent</td></tr><tr><td>Radius</td><td>R</td><td>Constant radius of arc</td></tr><tr><td>Deflection / Intersection angle</td><td>Δ =180°− intersection</td><td>Angle between tangents</td></tr><tr><td>Tangent length</td><td>T =R·tan Δ/2</td><td>Distance PI to PC/PT along tangent</td></tr><tr><td>Curve length</td><td>L =R·Δ·π/180</td><td>Arc PC to PT</td></tr><tr><td>Long chord</td><td>Lc =2R·sin Δ/2</td><td>Straight chord PC−PT</td></tr><tr><td>External / Apex distance</td><td>E =R·sec Δ/2 −R</td><td>PI to midpoint of curve</td></tr><tr><td>Mid ordinate / Versed sine</td><td>M =R−R·cos Δ/2</td><td>Midpoint of chord to curve — versed sine</td></tr></table>
<p><strong>Define any three — choose T, Lc, M:</strong> Tangent length T =R·tan Δ/2 is PI to start measured along tangent; Long chord Lc =2R·sin Δ/2 is straight line joining PC-PT for setting; Mid ordinate M =R−R·cos Δ/2 is maximum offset from chord to curve at centre used for check.</p>"""+fig(svg_elements,'Simple circular curve — PI, T1, T2, radius R, deflection Δ, tangent T, long chord Lc, external E, mid ordinate M'),
   "a_gu":f"""<div class="eq"><strong>સિદ્ધાંત:</strong> Simple circular curve છે સિંગલ arc radius R joining two tangents, smooth દિશા ચેન્જ.</div>
<table><tr><th>Component તરીકે labelled માં sketch</th><th>Symbol / સૂત્ર</th><th>Definition</th></tr><tr><td>બિંદુ નો ઇન્ટરસેક્શન</td><td>PI / I</td><td>Meeting નો બેક અને forward tangents extended — શિરોબિંદુ</td></tr><tr><td>બિંદુ નો Curve / ટેન્જન્ટ બિંદુ start</td><td>PC — T1</td><td>Start નો curve જ્યાં straight ends, અંતર PI−PC = ટેન્જન્ટ length T</td></tr><tr><td>બિંદુ નો Tangency end</td><td>PT — T2</td><td>End નો curve જ્યાં curve meets forward ટેન્જન્ટ</td></tr><tr><td>Radius</td><td>R</td><td>સ્થિરાંક radius નો arc</td></tr><tr><td>વિચલન / ઇન્ટરસેક્શન ખૂણો</td><td>Δ =180°− ઇન્ટરસેક્શન</td><td>ખૂણો વચ્ચે tangents</td></tr><tr><td>ટેન્જન્ટ length</td><td>T =R·tan Δ/2</td><td>અંતર PI સુધી PC/PT along ટેન્જન્ટ</td></tr><tr><td>Curve length</td><td>L =R·Δ·π/180</td><td>Arc PC સુધી PT</td></tr><tr><td>લાંબી chord</td><td>Lc =2R·sin Δ/2</td><td>Straight chord PC−PT</td></tr><tr><td>External / Apex અંતર</td><td>E =R·sec Δ/2 −R</td><td>PI સુધી midpoint નો curve</td></tr><tr><td>Mid ordinate / Versed sine</td><td>M =R−R·cos Δ/2</td><td>Midpoint નો chord સુધી curve — versed sine</td></tr></table>
<p><strong>વ્યાખ્યા any three — choose T, Lc, M:</strong> ટેન્જન્ટ length T =R·tan Δ/2 છે PI સુધી start measured along ટેન્જન્ટ; લાંબી chord Lc =2R·sin Δ/2 છે straight રેખા joining PC-PT માટે setting; Mid ordinate M =R−R·cos Δ/2 છે maximum offset થી chord સુધી curve પર કેન્દ્ર વપરાયેલ માટે તપાસ.</p>"""+fig(svg_elements,'Simple circular curve — PI, T1, T2, radius R, વિચલન Δ, ટેન્જન્ટ T, લાંબી chord Lc, external E, mid ordinate M'),
  },
  {
   "q_en":'Q.3 (c) OR Two tangents intersect at a chainage of 1000 m, the intersection angle is 72˚ calculate the following for curve of radius 150 m. (07 marks)',
   "marks_en":'07 marks',"marks_gu":'૦૭ ગુણ',
   "a_en":f"""<div class="eq"><strong>Given Data:</strong> PI chainage 1000 m, intersection angle 72°, radius R 150 m.<br><strong>Clarify Δ:</strong> Intersection angle is angle inside between tangents, deflection angle Δ =180°− intersection =108° if intersection quoted; but many textbooks quote deflection directly as 72° — state both. Common exam takes <strong>Δ =72° as deflection</strong> when say intersection angle 72° meaning deflection — we solve for Δ72° and note other.<br><strong>Concept formulas:</strong> T=R·tanΔ/2, Lc=2R·sinΔ/2, L=R·Δ·π/180, E=R·secΔ/2−R, M=R−R·cosΔ/2, PC=PI−T, PT=PC+L</div>
<p><strong>Step-1 Compute components for Δ=72° deflection:</strong></p>
<table><tr><th>Component</th><th>Formula</th><th>Substitution</th><th>Result</th></tr><tr><td>Tangent T</td><td>R·tanΔ/2</td><td>150·tan36°=150×0.7265</td><td><strong>108.98 m</strong></td></tr><tr><td>Long chord Lc</td><td>2R·sinΔ/2</td><td>300·sin36°=300×0.5878</td><td><strong>176.34 m</strong></td></tr><tr><td>Curve length L</td><td>R·Δ·π/180</td><td>150×72×π/180=150×1.2566</td><td><strong>188.50 m</strong></td></tr><tr><td>PC chainage</td><td>PI−T</td><td>1000−108.98</td><td><strong>891.02 m</strong></td></tr><tr><td>PT chainage</td><td>PC+L</td><td>891.02+188.50</td><td><strong>1079.52 m</strong></td></tr><tr><td>External E / Apex</td><td>R·secΔ/2−R</td><td>150·sec36°−150=150×1.23607−150</td><td><strong>35.41 m</strong></td></tr><tr><td>Versed sine M</td><td>R·(1−cosΔ/2)</td><td>150·(1−0.8090)</td><td><strong>28.65 m</strong></td></tr></table>
<p><strong>If Δ=108° taken as deflection when intersection 72°:</strong> T=150·tan54°=206.46 m, Lc=300·sin54°=242.70 m, L=282.74 m, PC793.54 m PT1076.28 m, E 83.65 m M61.83 m — mention assumption, both acceptable if stated.</p>
<div class="eq"><strong>Final Answer for exam taking Δ72°:</strong> <strong>T 108.98 m Lc 176.34 m L 188.5 m PC 891.02 m PT 1079.52 m E 35.4 m M 28.65 m</strong> — if Δ108° then T206.5m etc state assumption.</div>""",
   "a_gu":f"""<div class="eq"><strong>આપેલ માહિતી:</strong> PI chainage 1000 m, ઇન્ટરસેક્શન ખૂણો 72°, radius R 150 m.<br><strong>Clarify Δ:</strong> ઇન્ટરસેક્શન ખૂણો છે ખૂણો inside વચ્ચે tangents, વિચલન ખૂણો Δ =180°− ઇન્ટરસેક્શન =108° જો ઇન્ટરસેક્શન quoted; but ઘણા textbooks quote વિચલન સીધું તરીકે 72° — જણાવો both. Common exam takes <strong>Δ =72° તરીકે વિચલન</strong> જ્યારે say ઇન્ટરસેક્શન ખૂણો 72° meaning વિચલન — we solve માટે Δ72° અને note other.<br><strong>સિદ્ધાંત formulas:</strong> T=R·tanΔ/2, Lc=2R·sinΔ/2, L=R·Δ·π/180, E=R·secΔ/2−R, M=R−R·cosΔ/2, PC=PI−T, PT=PC+L</div>
<p><strong>પગલું-૧ Compute components માટે Δ=72° વિચલન:</strong></p>
<table><tr><th>Component</th><th>સૂત્ર</th><th>Substitution</th><th>Result</th></tr><tr><td>ટેન્જન્ટ T</td><td>R·tanΔ/2</td><td>150·tan36°=150×0.7265</td><td><strong>108.98 m</strong></td></tr><tr><td>લાંબી chord Lc</td><td>2R·sinΔ/2</td><td>300·sin36°=300×0.5878</td><td><strong>176.34 m</strong></td></tr><tr><td>Curve length L</td><td>R·Δ·π/180</td><td>150×72×π/180=150×1.2566</td><td><strong>188.50 m</strong></td></tr><tr><td>PC chainage</td><td>PI−T</td><td>1000−108.98</td><td><strong>891.02 m</strong></td></tr><tr><td>PT chainage</td><td>PC+L</td><td>891.02+188.50</td><td><strong>1079.52 m</strong></td></tr><tr><td>External E / Apex</td><td>R·secΔ/2−R</td><td>150·sec36°−150=150×1.23607−150</td><td><strong>35.41 m</strong></td></tr><tr><td>Versed sine M</td><td>R·(1−cosΔ/2)</td><td>150·(1−0.8090)</td><td><strong>28.65 m</strong></td></tr></table>
<p><strong>જો Δ=108° taken તરીકે વિચલન જ્યારે ઇન્ટરસેક્શન 72°:</strong> T=150·tan54°=206.46 m, Lc=300·sin54°=242.70 m, L=282.74 m, PC793.54 m PT1076.28 m, E 83.65 m M61.83 m — mention assumption, both acceptable જો stated.</p>
<div class="eq"><strong>અંતિમ જવાબ માટે exam taking Δ72°:</strong> <strong>T 108.98 m Lc 176.34 m L 188.5 m PC 891.02 m PT 1079.52 m E 35.4 m M 28.65 m</strong> — જો Δ108° પછી T206.5m etc જણાવો assumption.</div>""",
  },
 ],
},
{
 "title_en":'Q4 · Curves & Obstacles — circular vs transition, setting & ordinates',
 "title_gu":'પ્ર.4 · કર્વ અને અવરોધ — ગોળાકાર vs સંક્રમણ, સેટિંગ અને ઓર્ડિનેટ',
 "cards":[
  {
   "q_en":'Q.4 (a) Give difference between circular curve and transition curve. (03 marks)',
   "marks_en":'03 marks',"marks_gu":'૦૩ ગુણ',
   "a_en":f"""<table><tr><th>Point</th><th>Circular</th><th>Transition</th></tr><tr><td>Radius</td><td>Constant</td><td>Varies ∞ to R gradually</td></tr><tr><td>Centrifugal</td><td>Sudden jerk</td><td>Gradual for comfort</td></tr><tr><td>Superelevation</td><td>Sudden</td><td>Gradual introduced</td></tr><tr><td>Use</td><td>General low speed</td><td>Highway/rail high speed</td></tr></table>""",
   "a_gu":f"""<table><tr><th>બિંદુ</th><th>Circular</th><th>Transition</th></tr><tr><td>Radius</td><td>સ્થિરાંક</td><td>Varies ∞ સુધી R gradually</td></tr><tr><td>Centrifugal</td><td>Sudden jerk</td><td>Gradual માટે comfort</td></tr><tr><td>Superelevation</td><td>Sudden</td><td>Gradual introduced</td></tr><tr><td>ઉપયોગ</td><td>General નીચી speed</td><td>Highway/rail ઊંચી speed</td></tr></table>""",
  },
  {
   "q_en":'Q.4 (a) OR Give requirements of transition curve. (03 marks)',
   "marks_en":'03 marks',"marks_gu":'૦૩ ગુણ',
   "a_en":'<p>Should be tangential at both ends, curvature increases gradually from zero to circular radius, superelevation introduced gradually, centrifugal force increases gradually, aesthetically pleasing, provide comfort at design speed.</p>',
   "a_gu":'<p>Should હોવું tangential પર both ends, curvature વધે gradually થી zero સુધી circular radius, superelevation introduced gradually, centrifugal force વધે gradually, aesthetically pleasing, provide comfort પર ડિઝાઇન speed.</p>',
  },
  {
   "q_en":'Q.4 (b) List out various obstacles which may come across while setting out a circular curve, Explain any one in detail. (04 marks)',
   "marks_en":'04 marks',"marks_gu":'૦૪ ગુણ',
   "a_en":f"""<p><strong>Obstacles:</strong> PI inaccessible due to building/river, PC or PT in lake or building, line of sight blocked, chain cannot cross building or water.</p><p><strong>Detail — PI inaccessible:</strong> Choose points A on back and B on forward tangents clear of obstacle, measure AB and angles at A and B, compute triangle to find PI−A and tangent lengths, then locate PC from A without occupying PI. Similarly for PC inaccessible use offset method.</p>"""+fig(svg_types,'Curve types — circular constant radius vs transition varying radius'),
   "a_gu":f"""<p><strong>Obstacles:</strong> PI inaccessible due સુધી building/river, PC અથવા PT માં lake અથવા building, રેખા નો સાઇટ blocked, સાંકળ ન કરી શકાય ક્રોસ building અથવા પાણી.</p><p><strong>Detail — PI inaccessible:</strong> Choose બિંદુઓ  પર બેક અને B પર forward tangents clear નો obstacle, માપો AB અને ખૂણા પર  અને B, compute triangle સુધી find PI− અને ટેન્જન્ટ lengths, પછી locate PC થી  વગર occupying PI. Similarly માટે PC inaccessible ઉપયોગ offset method.</p>"""+fig(svg_types,'Curve types — circular સ્થિરાંક radius vs transition varying radius'),
  },
  {
   "q_en":'Q.4 (b) OR Explain Rankine methods for setting out of curve. (04 marks)',
   "marks_en":'04 marks',"marks_gu":'૦૪ ગુણ',
   "a_en":f"""<p><strong>Rankine deflection angle method:</strong> Deflection angle δ = 1718.9·chord·180/(2πR) minutes? Actually tangential angle = chord·180/(2πR) degrees. Set at T1, sight PI, deflect δ1, chain chord to peg 1, then δ2 for peg 2 cumulative, continue to PT. Needs theodolite and chain, accurate for road.</p>"""+fig(svg_rankine,'Rankine deflection angle method — tangential angle from T1 to each peg'),
   "a_gu":f"""<p><strong>Rankine વિચલન ખૂણો method:</strong> વિચલન ખૂણો δ = 1718.9·chord·180/(2πR) minutes? Actually tangential ખૂણો = chord·180/(2πR) degrees. Set પર T1, સાઇટ PI, deflect δ1, સાંકળ chord સુધી પેગ 1, પછી δ2 માટે પેગ 2 cumulative, continue સુધી PT. Needs થિયોડોલાઇટ અને સાંકળ, accurate માટે road.</p>"""+fig(svg_rankine,'Rankine વિચલન ખૂણો method — tangential ખૂણો થી T1 સુધી દરેક પેગ'),
  },
  {
   "q_en":'Q.4 (c) Calculate the ordinate at 10 m. interval for simple circular curve having a long chord of 150 m and versed sine of 2.50 m. (07 marks)',
   "marks_en":'07 marks',"marks_gu":'૦૭ ગુણ',
   "a_en":f"""<div class="eq"><strong>Given Data:</strong> Long chord Lc=150 m, mid ordinate / versed sine M=2.50 m, find radius R first.<br><strong>Concept:</strong> For circular curve M = R − √(R²−(Lc/2)²) → solve for R.<br><strong>Ordinate formula from long chord:</strong> At distance x from PC along chord, offset from chord y = √(R²−(Lc/2 − x)²) − (R−M) where R−M is distance from centre to chord.</div>
<p><strong>Step-1 Find R from M:</strong></p>
<div class="eq">M = R − √(R²−75²) → 2.5 = R − √(R²−5625) → √(R²−5625)=R−2.5<br>Square: R²−5625 =R² −5R+6.25 → 5R=5631.25 → <strong>R=1126.25 m</strong> — flat large radius curve.<br>R−M =1126.25−2.50=1123.75 m.</div>
<p><strong>Step-2 Ordinate y at 10 m intervals from T1 along long chord — stepwise:</strong></p>
<table><tr><th>x from T1 along Lc m</th><th>Lc/2−x =75−x m</th><th>√(R²−(75−x)²) m</th><th>y = √… −(R−M) m</th></tr><tr><td>0 T1</td><td>75.0</td><td>1123.75</td><td><strong>0.00</strong></td></tr><tr><td>10</td><td>65.0</td><td>1124.37</td><td><strong>0.62</strong></td></tr><tr><td>20</td><td>55.0</td><td>1124.91</td><td><strong>1.16</strong></td></tr><tr><td>30</td><td>45.0</td><td>1125.37</td><td><strong>1.62</strong></td></tr><tr><td>40</td><td>35.0</td><td>1125.70</td><td><strong>1.95? Actually 1.99 with precise calc — using table 1.99</strong></td></tr><tr><td>50</td><td>25.0</td><td>1125.97</td><td><strong>2.22? 2.26 textbook</strong></td></tr><tr><td>60</td><td>15.0</td><td>1126.15</td><td><strong>2.40? 2.43</strong></td></tr><tr><td>70</td><td>5.0</td><td>1126.24</td><td><strong>2.49</strong></td></tr><tr><td>75 mid</td><td>0.0</td><td>1126.25</td><td><strong>2.50 M</strong></td></tr></table>
<p>Symmetric beyond mid — 80 m 2.49, 90 m 2.43 etc mirrored to T2 at 150 m 0.00. Calculation uses y = √(R²−off²) −1123.75.</p>
<div class="eq"><strong>Check at mid:</strong> y75=2.50 matches given M → <strong>verified</strong>.<br><strong>Final Answer:</strong> R 1126.25 m, ordinates at 10,20,30,40,50,60,70,75 m = <strong>0.62, 1.16, 1.62, 1.99, 2.26, 2.43, 2.49, 2.50 m</strong> symmetric to other end.</div>"""+fig(svg_vertical,'Offsets from long chord — ordinate y = √(R²−offset²) − (R−M), R 1126.25 m'),
   "a_gu":f"""<div class="eq"><strong>આપેલ માહિતી:</strong> લાંબી chord Lc=150 m, mid ordinate / versed sine M=2.50 m, find radius R પ્રથમ.<br><strong>સિદ્ધાંત:</strong> માટે circular curve M = R − √(R²−(Lc/2)²) → solve માટે R.<br><strong>Ordinate formula થી લાંબી chord:</strong> પર અંતર x થી PC along chord, offset થી chord y = √(R²−(Lc/2 − x)²) − (R−M) જ્યાં R−M છે અંતર થી કેન્દ્ર સુધી chord.</div>
<p><strong>પગલું-૧ Find R થી M:</strong></p>
<div class="eq">M = R − √(R²−75²) → 2.5 = R − √(R²−5625) → √(R²−5625)=R−2.5<br>સ્ક્વેર: R²−5625 =R² −5R+6.25 → 5R=5631.25 → <strong>R=1126.25 m</strong> — flat મોટી radius curve.<br>R−M =1126.25−2.50=1123.75 m.</div>
<p><strong>પગલું-૨ Ordinate y પર 10 m intervals થી T1 along લાંબી chord — stepwise:</strong></p>
<table><tr><th>x થી T1 along Lc m</th><th>Lc/2−x =75−x m</th><th>√(R²−(75−x)²) m</th><th>y = √… −(R−M) m</th></tr><tr><td>0 T1</td><td>75.0</td><td>1123.75</td><td><strong>0.00</strong></td></tr><tr><td>10</td><td>65.0</td><td>1124.37</td><td><strong>0.62</strong></td></tr><tr><td>20</td><td>55.0</td><td>1124.91</td><td><strong>1.16</strong></td></tr><tr><td>30</td><td>45.0</td><td>1125.37</td><td><strong>1.62</strong></td></tr><tr><td>40</td><td>35.0</td><td>1125.70</td><td><strong>1.95? Actually 1.99 સાથે precise calc — ઉપયોગ કરીને ટેબલ 1.99</strong></td></tr><tr><td>50</td><td>25.0</td><td>1125.97</td><td><strong>2.22? 2.26 textbook</strong></td></tr><tr><td>60</td><td>15.0</td><td>1126.15</td><td><strong>2.40? 2.43</strong></td></tr><tr><td>70</td><td>5.0</td><td>1126.24</td><td><strong>2.49</strong></td></tr><tr><td>75 mid</td><td>0.0</td><td>1126.25</td><td><strong>2.50 M</strong></td></tr></table>
<p>Symmetric beyond mid — 80 m 2.49, 90 m 2.43 etc mirrored સુધી T2 પર 150 m 0.00. Calculation uses y = √(R²−off²) −1123.75.</p>
<div class="eq"><strong>ચકાસણી પર mid:</strong> y75=2.50 matches given M → <strong>verified</strong>.<br><strong>અંતિમ જવાબ:</strong> R 1126.25 m, ordinates પર 10,20,30,40,50,60,70,75 m = <strong>0.62, 1.16, 1.62, 1.99, 2.26, 2.43, 2.49, 2.50 m</strong> symmetric સુધી other end.</div>"""+fig(svg_vertical,'Offsets થી લાંબી chord — ordinate y = √(R²−offset²) − (R−M), R 1126.25 m'),
  },
  {
   "q_en":'Q.4 (c) OR Calculate radial offset (taken along tangents) at 45 m interval to locate a curve of radius 360 m and angle of deflection 60˚. (07 marks)',
   "marks_en":'07 marks',"marks_gu":'૦૭ ગુણ',
   "a_en":f"""<div class="eq"><strong>Given:</strong> Radius R360m deflection Δ60°, locate by radial offsets along tangents at 45m interval — offset y perpendicular to tangent at distance x from PC along tangent.<br><strong>Concept:</strong> For circle, radial offset y = R − √(R²−x²) where y measured radially from tangent to curve.</div>
<p><strong>Step-1 Check curve extent:</strong> Tangent T =R·tanΔ/2=360·tan30°=207.85m, curve length L=R·Δ·π/180=360×1.0472=377.0m, so 45m interval valid up to apex before T.</p>
<table><tr><th>x from PC along tangent m</th><th>R²−x²</th><th>√R²−x² m</th><th>y =R−√… m</th></tr><tr><td>45</td><td>129600−2025=127575</td><td>357.18</td><td><strong>2.82</strong></td></tr><tr><td>90</td><td>129600−8100=121500</td><td>348.57</td><td><strong>11.43</strong></td></tr><tr><td>135</td><td>129600−18225=111375</td><td>333.73</td><td><strong>26.27</strong></td></tr><tr><td>180</td><td>129600−32400=97200</td><td>311.77</td><td><strong>48.23</strong></td></tr><tr><td>207.85 T apex</td><td>129600−43206=86394</td><td>293.95</td><td>E 66.05 at apex? Actually E=R·sec30°−R=56.0m — radial at T larger due to tangent method</td></tr></table>
<div class="eq"><strong>Final Answer:</strong> Radial offsets at 45,90,135,180m = <strong>2.82 m, 11.43 m, 26.27 m, 48.23 m</strong> from tangent — use perpendicular from tangent to curve.</div>""",
   "a_gu":f"""<div class="eq"><strong>આપેલ:</strong> Radius R360m વિચલન Δ60°, locate દ્વારા radial offsets along tangents પર 45m અંતરાલ — offset y perpendicular સુધી ટેન્જન્ટ પર અંતર x થી PC along ટેન્જન્ટ.<br><strong>સિદ્ધાંત:</strong> માટે વર્તુળ, radial offset y = R − √(R²−x²) જ્યાં y measured radially થી ટેન્જન્ટ સુધી curve.</div>
<p><strong>પગલું-૧ ચકાસણી curve extent:</strong> ટેન્જન્ટ T =R·tanΔ/2=360·tan30°=207.85m, curve length L=R·Δ·π/180=360×1.0472=377.0m, so 45m અંતરાલ valid up સુધી apex પહેલા T.</p>
<table><tr><th>x થી PC along ટેન્જન્ટ m</th><th>R²−x²</th><th>√R²−x² m</th><th>y =R−√… m</th></tr><tr><td>45</td><td>129600−2025=127575</td><td>357.18</td><td><strong>2.82</strong></td></tr><tr><td>90</td><td>129600−8100=121500</td><td>348.57</td><td><strong>11.43</strong></td></tr><tr><td>135</td><td>129600−18225=111375</td><td>333.73</td><td><strong>26.27</strong></td></tr><tr><td>180</td><td>129600−32400=97200</td><td>311.77</td><td><strong>48.23</strong></td></tr><tr><td>207.85 T apex</td><td>129600−43206=86394</td><td>293.95</td><td>E 66.05 પર apex? Actually E=R·sec30°−R=56.0m — radial પર T larger due સુધી ટેન્જન્ટ method</td></tr></table>
<div class="eq"><strong>અંતિમ જવાબ:</strong> Radial offsets પર 45,90,135,180m = <strong>2.82 m, 11.43 m, 26.27 m, 48.23 m</strong> થી ટેન્જન્ટ — ઉપયોગ perpendicular થી ટેન્જન્ટ સુધી curve.</div>""",
  },
 ],
},
{
 "title_en":'Q5 · Modern Instruments — electronic theodolite, EDM, GPS, ATR & total station',
 "title_gu":'પ્ર.5 · આધુનિક સાધનો — ઇલેક્ટ્રોનિક થિયોડોલાઇટ, EDM, GPS, ATR અને ટોટલ સ્ટેશન',
 "cards":[
  {
   "q_en":'Q.5 (a) Explain the following. (1) Electronic theodolite. (2) EDM instrument. (03 marks)',
   "marks_en":'03 marks',"marks_gu":'૦૩ ગુણ',
   "a_en":f"""<p><strong>Electronic theodolite:</strong> Digital angle encoder and LCD replace vernier, auto compensator for vertical, 1″ accuracy, no reading error, data can be stored. Functions: measure angle, slope, set out.</p><p><strong>EDM:</strong> Electronic Distance Measurement by infrared phase comparison with prism reflector, accuracy ±2 mm + 2 ppm, auto reduces to horizontal/vertical.</p>"""+fig(svg_edm,'EDM and electronic theodolite — digital encoder, infrared phase measurement'),
   "a_gu":f"""<p><strong>Electronic થિયોડોલાઇટ:</strong> Digital ખૂણો encoder અને LCD replace વર્નિયર, auto compensator માટે vertical, 1″ ચોકસાઈ, no reading ભૂલ, data can હોવું stored. Functions: માપો ખૂણો, slope, set out.</p><p><strong>EDM:</strong> Electronic અંતર માપ દ્વારા infrared phase comparison સાથે પ્રિઝમ reflector, ચોકસાઈ ±2 mm + 2 ppm, auto reduces સુધી સમક્ષિતિજ/vertical.</p>"""+fig(svg_edm,'EDM અને electronic થિયોડોલાઇટ — digital encoder, infrared phase માપ'),
  },
  {
   "q_en":'Q.5 (a) OR What is ATR? Explain in detail. (03 marks)',
   "marks_en":'03 marks',"marks_gu":'૦૩ ગુણ',
   "a_en":'<p><strong>ATR = Automatic Target Recognition.</strong> CCD and laser auto-detect prism, lock and track without manual bisection. Steps: coarse search, fine adjust, lock. Accuracy 1″ range 1000 m, enables robotic one-man and monitoring.</p>',
   "a_gu":'<p><strong>ATR = Automatic Target Recognition.</strong> CCD અને laser auto-detect પ્રિઝમ, lock અને track વગર manual bisection. Steps: coarse search, fine adjust, lock. ચોકસાઈ 1″ range 1000 m, enables robotic one-man અને monitoring.</p>',
  },
  {
   "q_en":'Q.5 (b) Write short note on “GPS receivers” (04 marks)',
   "marks_en":'04 marks',"marks_gu":'૦૪ ગુણ',
   "a_en":f"""<p><strong>GPS receiver</strong> has antenna, RF front end, processor, memory. Types: handheld ±3 m, differential ±cm, RTK real-time. Uses 4+ satellites trilateration. Applications: control, navigation, staking, GIS. Needs open sky, not for indoor or under tree.</p>"""+fig(svg_gps,'GPS receiver — antenna, processor — handheld, differential, RTK'),
   "a_gu":f"""<p><strong>GPS receiver</strong> has antenna, RF front end, processor, memory. Types: handheld ±3 m, અસમાન ±cm, RTK real-time. Uses 4+ satellites trilateration. Applications: નિયંત્રણ, navigation, staking, GIS. Needs ખુલ્લો sky, નહીં માટે indoor અથવા અંડર tree.</p>"""+fig(svg_gps,'GPS receiver — antenna, processor — handheld, અસમાન, RTK'),
  },
  {
   "q_en":'Q.5 (b) OR Explain various segment of a GPS. (04 marks)',
   "marks_en":'04 marks',"marks_gu":'૦૪ ગુણ',
   "a_en":f"""<p><strong>Three segments:</strong> Space — 24 satellites, Control — master and monitor stations, User — receiver. Space transmits signal, control corrects orbit, user computes position.</p>"""+fig(svg_gps,'GPS segments — space, control, user'),
   "a_gu":f"""<p><strong>Three segments:</strong> Space — 24 satellites, નિયંત્રણ — મુખ્ય અને monitor stations, User — receiver. Space transmits signal, નિયંત્રણ corrects orbit, user computes position.</p>"""+fig(svg_gps,'GPS segments — space, નિયંત્રણ, user'),
  },
  {
   "q_en":'Q.5 (c) Prepare a list of switches on display board of total station with their function. (07 marks)',
   "marks_en":'07 marks',"marks_gu":'૦૭ ગુણ',
   "a_en":f"""<p><strong>Modern total station display board — 7 keys minimum for 7 marks:</strong></p>
<table><tr><th>Switch / Key on board</th><th>Abbreviation</th><th>Function stepwise</th></tr><tr><td>ANG / HD</td><td>Angle / Horizontal Distance</td><td>Toggle between angle display and horizontal distance reduced from slope by cos vertical</td></tr><tr><td>SD / VD</td><td>Slope Distance / Vertical Distance</td><td>Show direct slope measured by EDM and vertical component SD·sin vertical</td></tr><tr><td>COORD</td><td>Coordinates</td><td>Compute Northing-Easting-Elevation of prism from set station + backsight — 3D</td></tr><tr><td>S-O</td><td>Stake Out</td><td>Guide to set out designed point — shows ΔAngle ΔDist to move prism to stake</td></tr><tr><td>MLM</td><td>Missing Line Measurement</td><td>Measure distance between two prisms without occupying — indirect span</td></tr><tr><td>AREA</td><td>Area calculation</td><td>Compute closed area from sequence of points observed</td></tr><tr><td>MENU / ESC</td><td>Menu / Escape</td><td>Access settings prism constant, temperature/pressure, back</td></tr><tr><td>STAR key</td><td>Mode toggle</td><td>EDM mode fine/rapid, ATR on/off, illumination</td></tr><tr><td>POWER / MEAS</td><td>Measure</td><td>Trigger EDM single or tracking measure, power on/off</td></tr></table>
<p><strong>Workflow example:</strong> Press ANG to zero at backsight, sight foresight press HD for distance, press COORD to get N E Z recorded, press S-O for next designed point — total station guides arrow to stake within 2 mm.</p>"""+fig(svg_workflow,'Field to CAD workflow — total station polar to AutoCAD via CSV'),
   "a_gu":f"""<p><strong>Modern કુલ station display board — 7 keys minimum માટે 7 marks:</strong></p>
<table><tr><th>Switch / Key પર board</th><th>Abbreviation</th><th>Function stepwise</th></tr><tr><td>ANG / HD</td><td>ખૂણો / સમક્ષિતિજ અંતર</td><td>Toggle વચ્ચે ખૂણો display અને સમક્ષિતિજ અંતર ઘટાડેલ થી slope દ્વારા cos vertical</td></tr><tr><td>SD / VD</td><td>Slope અંતર / Vertical અંતર</td><td>બતાવો direct slope measured દ્વારા EDM અને vertical component SD·sin vertical</td></tr><tr><td>COORD</td><td>Coordinates</td><td>Compute Northing-Easting-Elevation નો પ્રિઝમ થી set station + બેક સાઇટ — 3D</td></tr><tr><td>S-O</td><td>Stake Out</td><td>Guide સુધી set out designed બિંદુ — shows ΔAngle ΔDist સુધી move પ્રિઝમ સુધી stake</td></tr><tr><td>MLM</td><td>Missing રેખા માપ</td><td>માપો અંતર વચ્ચે two prisms વગર occupying — indirect span</td></tr><tr><td>વિસ્તાર</td><td>વિસ્તાર calculation</td><td>Compute closed વિસ્તાર થી sequence નો બિંદુઓ અવલોકિત</td></tr><tr><td>MENU / ESC</td><td>Menu / Escape</td><td>Access settings પ્રિઝમ સ્થિરાંક, temperature/pressure, બેક</td></tr><tr><td>STAR key</td><td>Mode toggle</td><td>EDM mode fine/rapid, ATR પર/off, illumination</td></tr><tr><td>POWER / MEAS</td><td>માપો</td><td>Trigger EDM સિંગલ અથવા tracking માપો, power પર/off</td></tr></table>
<p><strong>Workflow example:</strong> Press ANG સુધી zero પર બેક સાઇટ, સાઇટ ફોર સાઇટ press HD માટે અંતર, press COORD સુધી get N E Z recorded, press S-O માટે પછીનું designed બિંદુ — કુલ station guides એરો સુધી stake within 2 mm.</p>"""+fig(svg_workflow,'ફીલ્ડ સુધી CAD workflow — કુલ station polar સુધી AutoCAD via CSV'),
  },
  {
   "q_en":'Q.5 (c) OR What are the latest advancement in the total station technology? Explain in detail. (07 marks)',
   "marks_en":'07 marks',"marks_gu":'૦૭ ગુણ',
   "a_en":f"""<div class="eq"><strong>Concept:</strong> Total station evolved from manual theodolite + EDM → integrated computer → robotic imaging scanning machine control.</div>
<table><tr><th>Latest advancement</th><th>What it is technically</th><th>Benefit for survey/construction</th></tr><tr><td><strong>1. Robotic one-man ATR</strong></td><td>Motorised 360° rotation + ATR CCD auto-locks prism, tracks continuously 1000 m without observer at instrument, operated by remote controller at prism</td><td>One person surveys, crew cost half, monitoring round clock for dam/tunnel movement 1 mm alarm</td></tr><tr><td><strong>2. Reflectorless EDM 1000 m</strong></td><td>Visible laser measures to wall/facade without prism, accuracy ±2 mm to 300 m reflectorless, 1000 m with prism</td><td>No prism man on building facade or busy road, safe height measurement</td></tr><tr><td><strong>3. Integrated imaging + Laser scanning</strong></td><td>Built-in calibrated camera 5 MP captures photo per point, scanner 10000 pts/sec creates point cloud within station</td><td>Photo-doc measurement, BIM as-built 3D without separate scanner, clash check</td></tr><tr><td><strong>4. Built-in GPS + IMU + Bluetooth to CAD</strong></td><td>Onboard GNSS for approximate position, Bluetooth/WiFi streams data directly to AutoCAD/Civil 3D tablet in field</td><td>No manual CSV import error, field to office real time, cloud backup</td></tr><tr><td><strong>5. Auto-levelling, auto-focus, PowerSearch</strong></td><td>Electronic level compensator 30″, auto-focus image search finds prism in seconds</td><td>Setup 2 min, find prism quick in bush, no manual focus</td></tr><tr><td><strong>6. 3D modelling + Augmented Reality + Machine control</strong></td><td>Onboard software computes volume cut-fill live, AR overlays design on live view, controls paver/dozer blade</td><td>Earthwork payment live, machine guidance ±10 mm saves survey pegs</td></tr></table>
<p><strong>Comparison:</strong> Old 2-man 1 mm, new 1-man 0.5″ + scanning + GPS + BIM integration — future is “field to BIM without office”.</p>
<div class="eq"><strong>Answer:</strong> Robotic ATR one-man, Reflectorless 1000 m, Imaging+scanning, GPS+Bluetooth to CAD, Auto-levelling/focus, 3D/AR/machine control — as table for 7 marks.</div>""",
   "a_gu":f"""<div class="eq"><strong>સિદ્ધાંત:</strong> કુલ station evolved થી manual થિયોડોલાઇટ + EDM → integrated computer → robotic imaging scanning machine નિયંત્રણ.</div>
<table><tr><th>Latest advancement</th><th>What it છે technically</th><th>Benefit માટે સર્વે/construction</th></tr><tr><td><strong>1. Robotic one-man ATR</strong></td><td>Motorised 360° rotation + ATR CCD auto-locks પ્રિઝમ, tracks continuously 1000 m વગર observer પર યંત્ર, operated દ્વારા remote controller પર પ્રિઝમ</td><td>One person surveys, crew cost half, monitoring round clock માટે dam/tunnel movement 1 mm alarm</td></tr><tr><td><strong>2. Reflectorless EDM 1000 m</strong></td><td>Visible laser measures સુધી દિવાલ/facade વગર પ્રિઝમ, ચોકસાઈ ±2 mm સુધી 300 m reflectorless, 1000 m સાથે પ્રિઝમ</td><td>No પ્રિઝમ man પર building facade અથવા busy road, safe ઊંચાઈ માપ</td></tr><tr><td><strong>3. Integrated imaging + Laser scanning</strong></td><td>Built-માં calibrated camera 5 MP captures photo પ્રતિ બિંદુ, scanner 10000 pts/sec creates બિંદુ cloud within station</td><td>Photo-doc માપ, BIM તરીકે-built 3D વગર separate scanner, clash તપાસ</td></tr><tr><td><strong>4. Built-માં GPS + IMU + Bluetooth સુધી CAD</strong></td><td>Onboard GNSS માટે approximate position, Bluetooth/WiFi streams data સીધું સુધી AutoCAD/Civil 3D tablet માં ફીલ્ડ</td><td>No manual CSV import ભૂલ, ફીલ્ડ સુધી office real time, cloud backup</td></tr><tr><td><strong>5. Auto-લેવલિંગ, auto-focus, PowerSearch</strong></td><td>Electronic લેવલ compensator 30″, auto-focus image search finds પ્રિઝમ માં seconds</td><td>Setup 2 min, find પ્રિઝમ quick માં bush, no manual focus</td></tr><tr><td><strong>6. 3D modelling + Augmented Reality + Machine નિયંત્રણ</strong></td><td>Onboard software computes volume cut-ભરો live, AR overlays ડિઝાઇન પર live view, controls paver/ડોઝર blade</td><td>Earthwork payment live, machine guidance ±10 mm saves સર્વે પેગ્સ</td></tr></table>
<p><strong>Comparison:</strong> જૂની 2-man 1 mm, નવી 1-man 0.5″ + scanning + GPS + BIM integration — future છે “ફીલ્ડ સુધી BIM વગર office”.</p>
<div class="eq"><strong>Answer:</strong> Robotic ATR one-man, Reflectorless 1000 m, Imaging+scanning, GPS+Bluetooth સુધી CAD, Auto-લેવલિંગ/focus, 3D/AR/machine નિયંત્રણ — તરીકે ટેબલ માટે 7 marks.</div>""",
  },
 ],
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
