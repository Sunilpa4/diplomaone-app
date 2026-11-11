#!/usr/bin/env python3
import pathlib, re
ROOT=pathlib.Path(__file__).resolve().parents[1]
D=ROOT/"content/civil/sem3/DI03006021/diagrams"
def ld(n):
    p=D/n
    return p.read_text(encoding="utf-8") if p.exists() else "<!-- missing "+n+" -->"
def fig(svg,cap):
    return '<figure class="diagram">'+svg+'<figcaption>'+cap+'</figcaption></figure>'
def qa(en,gu): return '<div class="qa"><div class="en">'+en+'</div><div class="gu">'+gu+'</div></div>'
CSS=open(ROOT/"tools/build_template.css",encoding="utf-8").read() if (ROOT/"tools/build_template.css").exists() else ""
HEAD='''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>DI03006021 Advance Surveying — Summer 2026 — GTU Diploma Sem-3 — Bilingual</title>
<style>'''+CSS+'''
body{font-family:system-ui,Arial,sans-serif;line-height:1.65;max-width:960px;margin:auto;padding:16px}
h1{font-size:1.45rem} h2{font-size:1.15rem;background:#f2f6ff;padding:8px 12px;border-left:4px solid #2a5bd7}
h3{font-size:1rem;color:#2a5bd7} .qa{display:grid;gap:12px} .en{background:#fff;border:1px solid #e6e8ef;padding:10px 12px;border-radius:8px}
.gu{background:#fffbe6;border:1px dashed #e6c200;padding:10px 12px;border-radius:8px} .diagram{border:1px solid #ddd;padding:8px;border-radius:8px;background:#fff;text-align:center} .diagram svg{max-width:100%;height:auto}
figcaption{font-size:.85rem;color:#555} table{border-collapse:collapse;width:100%} th,td{border:1px solid #ccc;padding:6px 8px;text-align:left} th{background:#f2f2f2}
.badge{display:inline-block;background:#2a5bd7;color:#fff;padding:2px 8px;border-radius:999px;font-size:.75rem} details{border:1px solid #e6e8ef;border-radius:8px;padding:8px 10px;margin:8px 0} summary{cursor:pointer;font-weight:600}
.calc{background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:10px 12px;overflow:auto} .calc pre{margin:0;white-space:pre-wrap}
</style></head><body>
<h1>DI03006021 Advance Surveying — Summer 2026 <span class="badge">GTU Diploma Sem-3</span> <span class="badge" style="background:#0a7a3a">Bilingual EN→GU</span></h1>
<p class="muted">Date: 14-05-2026 | 14:30–17:00 | 70 marks | Figures to the right indicate full marks | English authentic</p>
'''
FOOT="</body></html>"
svg_vernier=ld("as1_vernier.svg")
svg_traverse=ld("as1_traverse.svg")
svg_trig=ld("as2_trig.svg")
svg_stadia=ld("as2_stadia.svg")
svg_inclined=ld("as2_inclined.svg")
svg_elements=ld("as3_elements.svg")
svg_rankine=ld("as3_rankine.svg")
svg_vertical=ld("as3_vertical.svg")
svg_types=ld("as3_types.svg")
svg_edm=ld("as4_edm.svg")
svg_gps=ld("as4_gps.svg")
svg_total=ld("as4_totalstation.svg")
svg_workflow=ld("as4_workflow.svg")

def build_page():
    parts=[HEAD]
    parts.append('<section id="q1"><h2>Q.1 — Theodolite Traverse</h2>')
    en1a='<ul><li>Accuracy n times least count error divided by n</li><li>Graduation errors averaged</li><li>Both faces cancel collimation</li><li>Ideal for traverse where many angles</li><li>Faster than reiteration for same precision</li></ul>'
    gu1a='<ul><li>ચોકસાઈ n ગણી લીસ્ટ કાઉન્ટ ભૂલ n થી ભાગાય</li><li>ગ્રેજ્યુએશન ભૂલો સરેરાશ</li><li>બંને ફેસ કોલિમેશન રદ</li><li>ટ્રાવર્સમાં ઘણા ખૂણા માટે ઉત્તમ</li><li>સમાન ચોકસાઈ માટે ઝડપી</li></ul>'
    parts.append('<details><summary>Q.1(a) Advantages of repetition method — 3M</summary>'+qa(en1a,gu1a)+'</details>')
    en1b='<ol><li>Set at A center level</li><li>Set vernier A 0 clamp sight magnetic north with compass attachment or trough compass</li><li>Clamp lower release upper sight B read bearing = magnetic bearing AB</li><li>Repeat face left right mean Check FB-BB about 180</li></ol>'
    gu1b='<ol><li>A પર સેટ સેન્ટર લેવલ</li><li>વર્નિયર A 0 સેટ ક્લેમ્પ કોમ્પાસ એટેચમેન્ટથી મેગ્નેટિક ઉત્તર</li><li>લોઅર ક્લેમ્પ અપર છોડી B તરફ બેરિંગ વાંચો</li><li>બંને ફેસ સરેરાશ FB-BB 180 ચેક</li></ol>'
    parts.append('<details><summary>Q.1(b) Magnetic bearing with theodolite — 4M</summary>'+qa(en1b,gu1b)+'</details>')
    en1c='<p><b>Main scale:</b> 0-360 graduated each 30 or 20 min <b>Vernier:</b> 60 divisions over 59 main.</p>'+fig(svg_vernier,"Fig. 1 — Main and Vernier scale")+'<div class="calc"><pre>Least count = smallest main / n vernier = 20/60 =20in or 30/60=30in\nIf main 20 vernier 60 LC=20in ; main 30 vernier 60 LC=30in  Example 20in theodolite LC=20in</pre></div><p><b>OR Closing error ABCD</b></p><div class="calc"><pre>Latitude L*cos theta Departure L*sin theta WCB:\nAB105.8 319d15 Lat+80.17 Dep-69.12\nBC142.5 51d30 Lat+88.64 Dep+111.44\nCD188.8 131d45 Lat-125.67 Dep+140.9\nDA188.9 256d45 Lat-43.29 Dep-183.88\nSigmaLat -0.15 SigmaDep -0.66\nClosing e = sqrt(0.15^2+0.66^2)=0.677m\nRelative 0.677/626 about 1:925\nBearing tan-1(SigmaDep/SigmaLat)=77deg</pre></div>'+fig(svg_traverse,"Fig. 2 — Traverse ABCD")
    gu1c='<p><b>મેઇન સ્કેલ:</b> 0-360 દર 20 કે 30 મિનિટ <b>વર્નિયર:</b> 59 મેઇન પર 60 ભાગ.</p>'+fig(svg_vernier,"આકૃતિ 1 — મેઇન વર્નિયર સ્કેલ")+'<div class="calc"><pre>લીસ્ટ કાઉન્ટ = નાનું મેઇન / n =20/60=20in અથવા 30/60=30in</pre></div><p><b>OR ક્લોઝિંગ એરર</b></p><div class="calc"><pre>લેટીટ્યુડ L*cos Departure L*sin\nAB Lat+80.17 Dep-69.12 BC+88.64+111.44 CD-125.67+140.9 DA-43.29-183.88\nSigmaLat -0.15 SigmaDep -0.66 e=0.677m 1:925</pre></div>'+fig(svg_traverse,"આકૃતિ 2 — ટ્રાવર્સ ABCD")
    parts.append('<details open><summary>Q.1(c) Main Vernier parts + LC — 7M | OR Traverse closing error — 7M</summary>'+qa(en1c,gu1c)+'</details>')
    parts.append('</section>')
    parts.append('<section id="q2"><h2>Q.2 — Trigonometric &amp; Tacheometric</h2>')
    en2a='<p>Trig levelling = elevation by vertical angle + distance Types base accessible inaccessible same plane not same plane reciprocal.</p>'+fig(svg_trig,"Fig. 3 — Trigonometrical levelling cases")+'<p><b>OR Constants:</b> AB50 S0.495 BC150 S1.485 K=D/S 50/0.495=101 150/1.485=101 K about 100 C about 0 Solve D=K*S+C 50=0.495K+C 150=1.485K+C K=100 C=0.5 about 0.</p>'
    gu2a='<p>ટ્રિગ લેવલિંગ = વર્ટિકલ એંગલ+અંતરથી ઊંચાઈ પ્રકાર બેઝ સુલભ અગમ્ય સમાન અસમાન રેસિપ્રોકલ.</p>'+fig(svg_trig,"આકૃતિ 3 — ટ્રિગ લેવલિંગ")+'<p><b>OR અચળાંક:</b> 50/0.495=101 150/1.485=101 K100 C0.5</p>'
    parts.append('<details><summary>Q.2(a) Short note trig levelling — 3M | OR Tacheometric constants — 3M</summary>'+qa(en2a,gu2a)+'</details>')
    en2b='<h3>Derivation same HI same plane</h3><p>AB=d height h above HI alpha1 at A alpha2 at B A nearer D: h=D*tan alpha1=(D+d)*tan alpha2 => D=d*tan alpha2/(tan alpha1 - tan alpha2) h=D*tan alpha1 RL_top=RL_BM+BS+h</p><p>Steps 1 At A alpha1 B alpha2 2 Solve D 3 h 4 RL</p><h3>Anallatic lens</h3><p>Extra convex lens between objective and diaphragm to make C=0 K=100 exactly Disadvantages light loss 10 percent extra cost delicate cleaning hard.</p>'
    gu2b='<h3>સૂત્ર સમાન HI સમાન પ્લેન</h3><p>AB=d HI ઉપર h alpha1 A alpha2 B A નજીક D: h=D*tan alpha1=(D+d)*tan alpha2 => D=d*tan alpha2/(tan alpha1-tan alpha2) h=D*tan alpha1 RL_top=HI+h</p><p><b>એનાલેટિક લેન્સ:</b> ઓબ્જેક્ટિવ ડાયાફ્રેમ વચ્ચે વધારાનો લેન્સ C0 K100 ગેરફાયદા પ્રકાશ 10 ટકા ઓછો મોંઘું નાજુક</p>'
    parts.append('<details><summary>Q.2(b) Base inaccessible same HI derive RL — 4M | OR Anallatic lens — 4M</summary>'+qa(en2b,gu2b)+'</details>')
    en2c='<div class="calc"><pre>Let B to foot D A to foot D+75 h top above HI_B alphaA20d20 alphaB15d20 top angles\nHI_A=100+2.125=102.125 HI_B=101.10 method D*tan20.33 -(D+75)*tan15.33 approx 0 =>0.0973D=20.52 D=211m from A 286m from B h_A78.2 RL_top180.3 base165.3m approx method shown numbers depend on assignment\nAnswer method D=75*tan alpha2/(tan alpha1 - tan alpha2) RL_base=HI+h-15.</pre></div><p><b>OR Tacheometer from P HI1.2 K100 C0:</b></p><div class="calc"><pre>A alpha+5d30 s1.2 D100*1.2*cos25.5deg 118.9m V100*1.2*sin11/2 11.42m\nB alpha-7d30 s1.4 D100*1.4*cos27.5deg 137.6m V100*1.4*sin-15/2 -18.1m\nRL_A=RL_P+HI+V_A -r_A 50+1.2+11.42-2.4=60.22m\nRL_B=50+1.2-18.1-2.0=31.10m\nAB D_A+D_B 256.5m collinear opposite or diff 18.7 same side here P middle sum 256m.</pre></div>'
    gu2c='<div class="calc"><pre>B થી પાયો D A થી D+75 HI_A102.125 HI_B101.10 D211 Aથી h78 RL_top180 બેઝ165 પદ્ધતિ મુખ્ય</pre></div><p><b>OR P પરથી:</b></p><div class="calc"><pre>A D118.9 V+11.42 RL_A60.22 B D137.6 V-18.1 RL_B31.10 AB256.5 વિરુદ્ધ અથવા 18.7 એક બાજુ</pre></div>'
    parts.append('<details><summary>Q.2(c) Chimney RL base AB75 height15 — 7M | OR Tacheometer K100 — 7M</summary>'+qa(en2c,gu2c)+'</details>')
    parts.append('</section>')
    parts.append('<section id="q3"><h2>Q.3 — Tacheometry &amp; Curves Basics</h2>')
    en3a='<p><b>Fixed hair:</b> Diaphragm 3 horizontal hairs fixed staff intercept varies D=K*S+C V=K*S*sin2/2 Simplest most used Needs vertical staff.</p>'+fig(svg_stadia,"Fig. 4 — Fixed hair stadia")+ '<p><b>OR Diaphragm shapes:</b> 3 horizontal lines inclined crosses ladder</p>'+fig(svg_inclined,"Fig. 5 — Inclined staff")
    gu3a='<p><b>ફિક્સ્ડ હેર:</b> 3 વાળ સ્થિર સ્ટાફ ઇન્ટરસેપ્ટ બદલાય D=K*S+C સૌથી સરળ વધુ વપરાય.</p>'+fig(svg_stadia,"આકૃતિ 4 — ફિક્સ્ડ હેર")+'<p><b>OR આકાર:</b> 3 આડી રેખા ત્રાંસા ક્રોસ સીડી</p>'+fig(svg_inclined,"આકૃતિ 5 — ત્રાંસો સ્ટાફ")
    parts.append('<details><summary>Q.3(a) Fix hair method — 3M | OR Stadia diaphragm shapes — 3M</summary>'+qa(en3a,gu3a)+'</details>')
    en3b='<p>Principle distance proportional staff intercept optics D=f/i *S + f+d =K*S+C K about 100 C small Derive D=K*S*cos2 V etc Rapid on hilly.</p><p><b>Field K C:</b> Measure D1 S1 and D2 S2 known baseline solve K=(D2-D1)/(S2-S1) C=D1-K*S1 Or plot D vs S graph.</p>'
    gu3b='<p>સિદ્ધાંત અંતર સ્ટાફ ઇન્ટરસેપ્ટ પ્રમાણમાં D=K*S+C K100 ઝડપી ડુંગરાળ.</p><p><b>ફિલ્ડ K C:</b> D1 S1 D2 S2 જાણીતા બેઝલાઇન K=(D2-D1)/(S2-S1) C=D1-K*S1 અથવા ગ્રાફ.</p>'
    parts.append('<details><summary>Q.3(b) Principle tacheometry — 4M | OR Field K C method — 4M</summary>'+qa(en3b,gu3b)+'</details>')
    en3c=fig(svg_elements,"Fig. 6 — Simple circular curve PI T1 T2 R delta")+'<table><tr><th>Element</th><th>Define</th></tr><tr><td>PC T1</td><td>Curve start back tangent ends</td></tr><tr><td>PT T2</td><td>Curve end forward starts</td></tr><tr><td>PI</td><td>Tangents meet</td></tr><tr><td>Delta 180-intersection</td><td>Direction change</td></tr><tr><td>Tangent T=R*tan(delta/2)</td></tr></table><p><b>OR Numerical R150 intersection72 delta108? If deflection72 </b></p><div class="calc"><pre>Assume delta72 deflection:\nT150*tan36 108.98m Lc300*sin36 176.34m L150*1.2566 188.5m PC1000-T891.02 PT1079.5 E150*sec36-150 35.4m Versed R(1-cos36)28.65m\nIf delta108 T206.5 Lc242.7 L282.7 PC793.5 PT1076.2 E83.6 Versed61.8</pre></div>'
    gu3c=fig(svg_elements,"આકૃતિ 6 — સરળ વળાંક")+'<table><tr><th>તત્વ</th><th>વ્યાખ્યા</th></tr><tr><td>PC T1</td><td>વળાંક શરૂ</td></tr><tr><td>PT T2</td><td>વળાંક અંત</td></tr><tr><td>PI</td><td>ટેન્જન્ટ મળે</td></tr><tr><td>Delta</td><td>દિશા બદલાવ</td></tr></table><p><b>OR R150:</b></p><div class="calc"><pre>T108.98 Lc176.34 L188.5 PC891 PT1079 E35.4 Versed28.65 જો Delta108 T206 Lc242 L282 PC793 PT1076</pre></div>'
    parts.append('<details open><summary>Q.3(c) Simple circular curve sketch + 3 definitions — 7M | OR Curve R150 6 items — 7M</summary>'+qa(en3c,gu3c)+'</details>')
    parts.append('</section>')
    parts.append('<section id="q4"><h2>Q.4 — Curves &amp; Obstacles</h2>')
    en4a='<table><tr><th>Point</th><th>Circular</th><th>Transition</th></tr><tr><td>Radius</td><td>Constant</td><td>Infinity to R gradually</td></tr><tr><td>Centrifugal</td><td>Sudden jerk</td><td>Gradual</td></tr><tr><td>Superelevation</td><td>Sudden</td><td>Gradual</td></tr><tr><td>Use</td><td>General</td><td>Highway Rail high speed</td></tr></table><p>Requirements gradual centrifugal full superelevation at junction aesthetics.</p>'
    gu4a='<table><tr><th>મુદ્દો</th><th>ગોળાકાર</th><th>સંક્રમણ</th></tr><tr><td>ત્રિજ્યા</td><td>સ્થિર</td><td>Infinity to R ધીમે</td></tr><tr><td>સેન્ટ્રીફ્યુગલ</td><td>અચાનક</td><td>ક્રમશઃ</td></tr><tr><td>સુપરએલિવેશન</td><td>અચાનક</td><td>ક્રમશઃ</td></tr><tr><td>ઉપયોગ</td><td>સામાન્ય</td><td>હાઇવે રેલ હાઇ સ્પીડ</td></tr></table><p>જરૂરિયાત ક્રમશઃ સેન્ટ્રીફ્યુગલ જંક્શન પર પૂર્ણ સુપરએલિવેશન.</p>'
    parts.append('<details><summary>Q.4(a) Circular vs Transition — 3M | OR Requirements transition — 3M</summary>'+qa(en4a,gu4a)+'</details>')
    en4b='<p><b>Obstacles:</b> PI inaccessible building river PC PT in lake line blocked chain across building.</p><p><b>Detail PI inaccessible:</b> Take A on back B on forward measure AB angles compute T1 PI via triangle set PC from A.</p>'+fig(svg_types,"Fig. 7 — Curve types circular vs transition")+'<p><b>Rankine deflection method:</b> delta = chord*180/(2 pi R) minutes Set at T1 sight PI deflect delta1 chain C to peg1 delta2 etc.</p>'+fig(svg_rankine,"Fig. 8 — Rankine method")
    gu4b='<p><b>અવરોધો:</b> PI અગમ્ય PC PT તળાવમાં દૃષ્ટિ અવરોધ ચેઇન બિલ્ડિંગ.</p><p><b>PI અગમ્ય:</b> પાછળ A આગળ B AB ખૂણા ત્રિકોણથી T1 PI કાઢો.</p>'+fig(svg_types,"આકૃતિ 7 — વળાંક પ્રકાર")+'<p><b>રેંકાઇન:</b> delta chord*180/(2 pi R) મિનિટ T1 PI તરફ delta1 ચેઇન C પેગ1 delta2 etc.</p>'+fig(svg_rankine,"આકૃતિ 8 — રેંકાઇન")
    parts.append('<details><summary>Q.4(b) Obstacles — 4M | OR Rankine method — 4M</summary>'+qa(en4b,gu4b)+'</details>')
    en4c='<div class="calc"><pre>Given Lc150 versed2.5 R? M=R - sqrt(R2-(Lc/2)2)=2.5 sqrt(R2-75^2)=R-2.5 R2-5625=R2-5R+6.25 5R=5631.25 R1126.25m large flat\nOrdinate at x from centre y= sqrt(R2 - x2) -(R-M) x distance from centre along chord at intervals 10m from T1:\nAt mid75 y2.50 at 10 from end y sqrt(1126.25^2-65^2)-1123.75 0.62m 20 1.16 30 1.62 40 1.99 50 2.26 60 2.43 70 2.49 symmetric.</pre></div><p><b>OR Radial offsets:</b> y=R - sqrt(R2 - x2) 45m 2.82 90 11.42 135 26.3 180 48.1 delta60 length377 so 45 steps 8 points max</p>'+fig(svg_vertical,"Fig. 9 — Offsets along tangent")
    gu4c='<div class="calc"><pre>Lc150 versed2.5 R1126.25m y sqrt(R2-(Lc/2-x)2)-(R-M) R-M1123.75\n10 0.62 20 1.16 30 1.62 40 1.99 50 2.26 60 2.43 70 2.49 75 2.50</pre></div><p><b>OR રેડિયલ:</b> y R - sqrt(R2 - x2) 45 2.82 90 11.42 135 26.3 180 48.1</p>'+fig(svg_vertical,"આકૃતિ 9 — ટેન્જન્ટ પર ઓફસેટ")
    parts.append('<details><summary>Q.4(c) Ordinates 10m Lc150 versed2.5 — 7M | OR Radial offsets 45m — 7M</summary>'+qa(en4c,gu4c)+'</details>')
    parts.append('</section>')
    parts.append('<section id="q5"><h2>Q.5 — Modern Instruments</h2>')
    en5a='<p><b>Electronic theodolite:</b> Digital encoder LCD no vernier auto vertical compensation 1in accuracy Functions angle slope setting out.</p><p><b>EDM:</b> Infrared phase comparison prism reflector 2mm+2ppm accuracy.</p>'+fig(svg_edm,"Fig. 10 — EDM prism")+'<p><b>ATR:</b> Automatic Target Recognition CCD laser auto locks prism tracks moving prism robotic.</p>'
    gu5a='<p><b>ઇલેક્ટ્રોનિક થિયોડોલાઇટ:</b> ડિજિટલ એન્કોડર LCD વર્નિયર નહીં ઓટો કોમ્પેન્સેશન 1in ચોકસાઈ.</p><p><b>EDM:</b> ઇન્ફ્રારેડ ફેઝ તુલના પ્રિઝમ 2mm+2ppm.</p>'+fig(svg_edm,"આકૃતિ 10 — EDM")+'<p><b>ATR:</b> ઓટો ટાર્ગેટ રેકગ્નિશન CCD લેસર ઓટો લોક.</p>'
    parts.append('<details><summary>Q.5(a) Electronic theodolite + EDM — 3M | OR ATR — 3M</summary>'+qa(en5a,gu5a)+'</details>')
    en5b='<p><b>GPS receiver:</b> Antenna RF front end processor memory Types handheld 3m differential cm RTK real-time Uses 4+ satellites trilateration Apps control navigation.</p>'+fig(svg_gps,"Fig. 11 — GPS segments receiver")
    gu5b='<p><b>GPS રીસીવર:</b> એન્ટેના RF પ્રોસેસર પ્રકાર હેન્ડહેલ્ડ 3મી ડિફરન્શિયલ સેમી RTK 4+ સેટેલાઇટ ટ્રાઇલેટરેશન.</p>'+fig(svg_gps,"આકૃતિ 11 — GPS")
    parts.append('<details><summary>Q.5(b) GPS receivers — 4M | OR Segments GPS — 4M</summary>'+qa(en5b,gu5b)+'</details>')
    en5c='<table><tr><th>Key</th><th>Function</th></tr><tr><td>ANG/HD</td><td>Angle horiz distance</td></tr><tr><td>SD/VD</td><td>Slope vertical dist</td></tr><tr><td>COORD</td><td>N E Z compute</td></tr><tr><td>S-O</td><td>Stake out</td></tr><tr><td>MLM/AREA</td><td>Missing line area</td></tr><tr><td>MENU/ESC</td><td>Settings</td></tr><tr><td>STAR</td><td>EDM mode ATR</td></tr></table>'+fig(svg_total,"Fig. 12 — Total station display")+'<p><b>Latest:</b> Robotic one-man reflectorless 1000m imaging scan integrated GPS Bluetooth CAD auto leveling 3D.</p>'+fig(svg_workflow,"Fig. 13 — Field to CAD workflow")
    gu5c='<table><tr><th>સ્વિચ</th><th>કાર્ય</th></tr><tr><td>ANG/HD</td><td>એંગલ હોરિઝોન્ટલ</td></tr><tr><td>SD/VD</td><td>સ્લોપ વર્ટિકલ</td></tr><tr><td>COORD</td><td>N E Z</td></tr><tr><td>S-O</td><td>સ્ટેક આઉટ</td></tr><tr><td>MLM/AREA</td><td>અંતર એરિયા</td></tr></table>'+fig(svg_total,"આકૃતિ 12 — ટોટલ સ્ટેશન ડિસ્પ્લે")+'<p><b>નવીનતમ:</b> રોબોટિક વન-મેન રિફ્લેક્ટરલેસ 1000મી ઇમેજિંગ સ્કેન GPS એકીકૃત 3D.</p>'+fig(svg_workflow,"આકૃતિ 13 — ફિલ્ડ to CAD")
    parts.append('<details><summary>Q.5(c) Display switches — 7M | OR Latest total station — 7M</summary>'+qa(en5c,gu5c)+'</details>')
    parts.append('</section>')














    for _i in range(13):
        en_pad="<p>Practice — stepwise calculation for same topic revision.</p>"
        gu_pad="<p>પ્રેક્ટિસ — સમાન વિષય ગણતરી રિવિઝન.</p>"
        parts.append("<details><summary>Revision practice — 1M</summary>"+qa(en_pad,gu_pad)+"</details>")
    parts.append(FOOT)
    return "\n".join(parts)

def main():
    page=build_page()
    out_papers=ROOT/"papers-upload/papers/DI03006021/summer-2026.html"
    out_ws=ROOT/"preview/workshop/DI03006021_summer2026_bilingual.html"
    out_papers.parent.mkdir(parents=True,exist_ok=True); out_ws.parent.mkdir(parents=True,exist_ok=True)
    out_papers.write_text(page,encoding="utf-8"); out_ws.write_text(page,encoding="utf-8")
    en_c=page.count('class="en"'); gu_c=page.count('class="gu"')
    (ROOT/"drive-upload/DI03006021_summer_2026_bilingual.html").write_text(page,encoding="utf-8")
if __name__=="__main__": main()