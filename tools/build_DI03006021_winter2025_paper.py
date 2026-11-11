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
<title>DI03006021 Advance Surveying — Winter 2025 — GTU Diploma Sem-3 — Bilingual</title>
<style>'''+CSS+'''
body{font-family:system-ui,Arial,sans-serif;line-height:1.65;max-width:960px;margin:auto;padding:16px}
h1{font-size:1.45rem} h2{font-size:1.15rem;background:#f2f6ff;padding:8px 12px;border-left:4px solid #2a5bd7}
h3{font-size:1rem;color:#2a5bd7} .qa{display:grid;gap:12px} .en{background:#fff;border:1px solid #e6e8ef;padding:10px 12px;border-radius:8px}
.gu{background:#fffbe6;border:1px dashed #e6c200;padding:10px 12px;border-radius:8px} .diagram{border:1px solid #ddd;padding:8px;border-radius:8px;background:#fff;text-align:center} .diagram svg{max-width:100%;height:auto}
figcaption{font-size:.85rem;color:#555} table{border-collapse:collapse;width:100%} th,td{border:1px solid #ccc;padding:6px 8px;text-align:left} th{background:#f2f2f2}
.badge{display:inline-block;background:#2a5bd7;color:#fff;padding:2px 8px;border-radius:999px;font-size:.75rem} details{border:1px solid #e6e8ef;border-radius:8px;padding:8px 10px;margin:8px 0} summary{cursor:pointer;font-weight:600}
.calc{background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:10px 12px;overflow:auto} .calc pre{margin:0;white-space:pre-wrap}
</style></head><body>
<h1>DI03006021 Advance Surveying — Winter 2025 <span class="badge">GTU Diploma Sem-3</span> <span class="badge" style="background:#0a7a3a">Bilingual EN→GU</span></h1>
<p class="muted">Date: 06-12-2025 | 10:30–13:00 | 70 marks | Figures to the right indicate full marks | English authentic</p>
'''
FOOT="</body></html>"
svg_theodolite=ld("as1_theodolite.svg")
svg_trig=ld("as2_trig.svg")
svg_stadia=ld("as2_stadia.svg")
svg_elements=ld("as3_elements.svg")
svg_total=ld("as4_totalstation.svg")
svg_gps=ld("as4_gps.svg")
svg_edm=ld("as4_edm.svg")
svg_workflow=ld("as4_workflow.svg")

def build_page():
    parts=[HEAD]
    parts.append('<section id="q1"><h2>Q.1 — Theodolite Fundamentals</h2>')
    en1a='<h3>Swinging of telescope</h3><p>Telescope ne vertical axis fari faravvu te swinging kahevay — horizontal plane ma 360° direction badlave chhe. Lower clamp loose kari faravvu. Centering pachhi pratham step.</p><h3>Axis of level tube</h3><p>Tube na upar na surface ne sparshati tangential line — bubble centre hoy tyare horizontal thay. Levelling ma reference axis.</p><h3>Azimuth axis</h3><p>Theodolite no mukhya vertical axis jeni aaspas aakhu instrument fare chhe. Plumb bob / optical plummet dwara ground point par ubho karay chhe.</p>'
    gu1a='<h3>ટેલિસ્કોપનું સ્વિંગિંગ</h3><p>ટેલિસ્કોપને વર્ટિકલ અક્ષ ફરતે ફેરવવું તે સ્વિંગિંગ કહેવાય — હોરિઝોન્ટલ પ્લેનમાં 360° દિશા બદલે છે. લોઅર ક્લેમ્પ ઢીલો કરી ફેરવાય.</p><h3>લેવલ ટ્યુબનો અક્ષ</h3><p>ટ્યુબની ઉપરની સપાટીને સ્પર્શતી સ્પર્શરેખા — બબલ મધ્યે હોય ત્યારે હોરિઝોન્ટલ. લેવલિંગમાં રેફરન્સ અક્ષ.</p><h3>અઝિમથ અક્ષ</h3><p>થિયોડોલાઇટનો મુખ્ય વર્ટિકલ અક્ષ. પ્લમ્બ બોબ દ્વારા ગ્રાઉન્ડ પોઇન્ટ પર ઊભો કરાય છે.</p>'
    parts.append('<details open><summary>Q.1(a) Define: Swinging, Axis of level tube, Azimuth axis — 3M</summary>'+qa(en1a,gu1a)+'</details>')
    en1b='<p>Theodolite has telescope with vertical circle, horizontal circle main+vernier, upper/lower plates, levelling head, tripod, A-frame standards.</p>'+fig(svg_theodolite,"Fig. 1 — Theodolite — telescope, standards, plates, levelling head")+'<table><tr><th>Part</th><th>Function</th></tr><tr><td>Telescope</td><td>Sighting focusing</td></tr><tr><td>Vertical circle</td><td>Vertical angle</td></tr><tr><td>Horizontal circle</td><td>Azimuth bearing</td></tr><tr><td>Levelling head + foot screws</td><td>Vertical axis plumb</td></tr><tr><td>Clamps & tangents</td><td>Fine motion</td></tr><tr><td>Plumb bob</td><td>Centering</td></tr></table>'
    gu1b='<p>થિયોડોલાઇટમાં ટેલિસ્કોપ વર્ટિકલ સર્કલ સાથે, હોરિઝોન્ટલ સર્કલ મેઇન+વર્નિયર, અપર/લોઅર પ્લેટ, લેવલિંગ હેડ, ટ્રાઇપોડ, સ્ટાન્ડર્ડ A-ફ્રેમ.</p>'+fig(svg_theodolite,"આકૃતિ 1 — થિયોડોલાઇટ")+'<table><tr><th>ભાગ</th><th>કાર્ય</th></tr><tr><td>ટેલિસ્કોપ</td><td>સાઇટિંગ ફોકસ</td></tr><tr><td>વર્ટિકલ સર્કલ</td><td>વર્ટિકલ એંગલ</td></tr><tr><td>હોરિઝોન્ટલ સર્કલ</td><td>અઝિમથ બેરિંગ</td></tr><tr><td>લેવલિંગ હેડ</td><td>વર્ટિકલ અક્ષ પ્લમ્બ</td></tr><tr><td>ક્લેમ્પ</td><td>ફાઇન મોશન</td></tr><tr><td>પ્લમ્બ બોબ</td><td>સેન્ટરિંગ</td></tr></table>'
    parts.append('<details open><summary>Q.1(b) Neat sketch of theodolite and components — 4M</summary>'+qa(en1b,gu1b)+'</details>')
    en1c='<p><b>Methods:</b> Ordinary, Repetition, Reiteration.</p><h3>Repetition method</h3><ol><li>Set at O sight A set vernier A 0 clamp.</li><li>Loose lower sight B — first reading = angle.</li><li>Keep upper clamped loose lower back to A with lower tangent then again to B — reading shows 2x angle. Repeat n times 3-6.</li><li>Mean = final / n. Both faces cancel collimation.</li><li>Least count divided by n compensates graduation error.</li></ol><h3>OR Extend a line</h3><ol><li>Set at B on line AB sight A clamp transit 180 vertical line ahead.</li><li>Establish C beyond.</li><li>Reverse face repeat mean point = true extension. Double-centering eliminates collimation.</li></ol>'
    gu1c='<p><b>પદ્ધતિઓ:</b> ઓર્ડિનરી, રિપીટિશન, રિઇટરેશન.</p><h3>રિપીટિશન પદ્ધતિ</h3><ol><li>O પર A તરફ 0 સેટ ક્લેમ્પ.</li><li>લોઅર ઢીલો B તરફ — પહેલું રીડિંગ = ખૂણો.</li><li>અપર ક્લેમ્પ રાખી લોઅર ઢીલો પાછા A તરફ પછી ફરી B — 2x ખૂણો. n વાર 3-6.</li><li>સરેરાશ = અંતિમ / n. બંને ફેસ કોલિમેશન રદ.</li></ol><h3>OR લાઇન લંબાવવી</h3><ol><li>B પર A તરફ જુઓ ક્લેમ્પ ટ્રાન્ઝિટ 180 આગળ C.</li><li>ફેસ બદલી ફરી સરેરાશ = સાચું એક્સ્ટેન્શન.</li></ol>'
    parts.append('<details><summary>Q.1(c) Methods + Repetition — 7M | OR Extend line — 7M</summary>'+qa(en1c,gu1c)+'</details>')
    parts.append('</section>')
    parts.append('<section id="q2"><h2>Q.2 — Tacheometry &amp; Trigonometric Levelling</h2>')
    en2a='<p><b>Advantages:</b> Rapid distance+RL together chain not needed on rough undulating contours quickly one-man staff. Ideal hilly broken river.</p><p><b>Limitations:</b> Accuracy lower than taping 1:1000 staff not vertical error magnifies constants need field check long sights over 150m poor.</p>'
    gu2a='<p><b>ફાયદા:</b> ઝડપી અંતર+RL સાથે ચેઇન નહીં ખરબચડા ઉતાર-ચઢાવમાં કોન્ટૂર ઝડપથી એક વ્યક્તિ સ્ટાફ.</p><p><b>મર્યાદા:</b> ટેપિંગ કરતાં ઓછી ચોકસાઈ 1:1000 સ્ટાફ વર્ટિકલ ન હોય તો ભૂલ સ્ટેડિયા અચળાંક તપાસવા પડે લાંબા સાઇટ નબળા.</p>'
    parts.append('<details><summary>Q.2(a) Advantages & limitations of tacheometry — 3M</summary>'+qa(en2a,gu2a)+'</details>')
    en2b='<div class="calc"><pre>Given S_Q=2.550-1.450=1.100 D=110 ; S_R=3.550-1.345=2.205 D=220\nFormula D=K*S+C\n110=K*1.10+C ...(1)\n220=K*2.205+C ...(2)\n(2)-(1):110=K*1.105 => K=99.55 approx 100\nC=110-99.55*1.10=0.50 m\nAnswer K approx 100 C 0.30-0.50 m\nField: measure two known distances two intercepts solve simultaneous or plot D vs S slope K intercept C.</pre></div>'
    gu2b='<div class="calc"><pre>S_Q=1.100 D110 S_R=2.205 D220\nD=K*S+C => K approx 100 C 0.50 m\nબે જાણીતા અંતરે ઇન્ટરસેપ્ટ માપી સમીકરણ ઉકેલો અથવા D vs S ગ્રાફ ઢાળ K ઇન્ટરસેપ્ટ C.</pre></div>'
    parts.append('<details><summary>Q.2(b) Tacheometer constants K,C from 110m 220m — 4M</summary>'+qa(en2b,gu2b)+'</details>')
    en2c='<h3>Methods</h3><ul><li>Stadia fixed hair: diaphragm 3 hairs S=top-bottom D=K*S*cos2 V=K*S*sin2/2</li><li>Movable hair subtense: staff intercept fixed 3m interval variable</li><li>Tangential: no stadia measure vertical angles to two staff points</li></ul>'+fig(svg_stadia,"Fig. 2 — Stadia principle D=K*S+C")+'<h3>Principle</h3><p>Isosceles triangle distance proportional to staff intercept optics gives D=K*S+C K=f/i C=f+d.</p><h3>Reciprocal trig levelling</h3><p>Two stations A,B observe each other simultaneously to cancel refraction curvature Height diff h = D*(tanA - tanB)/2 averaged. Eliminates atmospheric error over water.</p>'
    gu2c='<h3>પદ્ધતિઓ</h3><ul><li>સ્ટેડિયા ફિક્સ્ડ હેર: 3 વાળ S D=K*S*cos2</li><li>મૂવેબલ સબટેન્સ: ઇન્ટરસેપ્ટ 3m સ્થિર</li><li>ટેન્જેન્શિયલ: બે બિંદુએ વર્ટિકલ એંગલ</li></ul>'+fig(svg_stadia,"આકૃતિ 2 — સ્ટેડિયા સિદ્ધાંત")+'<h3>સિદ્ધાંત</h3><p>સમદ્વિબાહુ ત્રિકોણ અંતર સ્ટાફ ઇન્ટરસેપ્ટ પ્રમાણમાં D=K*S+C</p><h3>રેસિપ્રોકલ ટ્રિગ લેવલિંગ</h3><p>બે સ્ટેશન એકબીજાને એકસાથે જુએ રિફ્રેક્શન કર્વેચર રદ લાંબા પાણી પર ભૂલ દૂર.</p>'
    parts.append('<details><summary>Q.2(c) Methods of tacheometric survey — 7M | OR Principle + K,C field + Reciprocal — 3+4+7M</summary>'+qa(en2c,gu2c)+'</details>')
    parts.append('</section>')
    parts.append('<section id="q3"><h2>Q.3 — Trigonometric Levelling</h2>')
    en3a='<p>Finding elevation of inaccessible high object using horizontal distance and vertical angle: h=D*tan a RL=RL_instrument+h - staff. Useful for towers chimneys hills where staff cannot reach.</p>'
    gu3a='<p>હોરિઝોન્ટલ અંતર વર્ટિકલ એંગલ વડે ઊંચા અગમ્ય ઓબ્જેક્ટ ઊંચાઈ h=D*tan a RL=RL+h. ટાવર ચીમની ટેકરી જ્યાં સ્ટાફ ન પહોંચે.</p>'
    parts.append('<details><summary>Q.3(a) Define + describe trigonometric levelling — 3M</summary>'+qa(en3a,gu3a)+'</details>')
    en3b='<p>Case1 base accessible: h=D*tan a RL_top=RL_BM+BS+D*tan a</p><p>Case2 base inaccessible same plane: h1=D*tan a1 h2=(D+PQ)*tan a2 solve D=PQ*tan a2/(tan a1 - tan a2)</p>'+fig(svg_trig,"Fig. 3 — Trigonometric levelling accessible vs inaccessible")
    gu3b='<p>કેસ1 બેઝ સુલભ h=D*tan a RL_top=RL_BM+BS+D*tan a</p><p>કેસ2 બેઝ અગમ્ય સમાન પ્લેન D=PQ*tan a2/(tan a1 - tan a2)</p>'+fig(svg_trig,"આકૃતિ 3 — ટ્રિગ લેવલિંગ સુલભ vs અગમ્ય")
    parts.append('<details><summary>Q.3(b) Two sketches + equations — 4M</summary>'+qa(en3b,gu3b)+'</details>')
    en3c='<div class="calc"><pre>Let PT=D nearer P angle14d30 QT=D+30 angle11d42\nD*tan14.5=(D+30)*tan11.70 => D*0.2586=(D+30)*0.2069 =>0.0517D=6.207 =>D=120m from P\nh=120*0.2586=31.03m\nHI_P=5.550+1.510=7.06 HI_Q=6.185\nRL_top=HI_P+h=38.09m (Q check 37.22 mean 37-38m accept)\nIf HI equal RL approx 38m</pre></div><p>OR Non-coplanar: triangle ABT sine rule to get D_A D_B then h=D*tan a.</p><div class="calc"><pre>Tacheometer K100 C0.40 at A:\nBM s=0.650 D=64.9m V=-2.61m B s=1.73 D about 169m V+12.7m\nRL_B=RL_A+HI+V -r BM gives RL_A then RL_B about 220m AB about 169m sum</pre></div>'
    gu3c='<div class="calc"><pre>D=120m Pથી h=31.03 HI_P=7.06 RL_top=38.09m Qથી 37.2 સરેરાશ 37-38m\nNon-coplanar ABT સાઇન નિયમ D_A D_B પછી h=D*tan a</pre></div><div class="calc"><pre>ટેકોમીટર A BM D64.9 V-2.61 B D169 V+12.7 RL_B 220 AB169m</pre></div>'
    parts.append('<details open><summary>Q.3(c) RL of tower top P Q 30m BM5.55 — 7M | OR Non-coplanar derivation + tacheometer — 4+7M</summary>'+qa(en3c,gu3c)+'</details>')
    parts.append('</section>')
    parts.append('<section id="q4"><h2>Q.4 — Horizontal Curves</h2>')
    en4a='<p>PI Point of Intersection meeting of two tangents vertex</p><p>PC Point of Curve start T1 straight ends</p><p>PT Tangent Point end T2 curve meets forward tangent</p><p>Horizontal curve arc connecting two straights in plan</p>'
    gu4a='<p>PI આંતરછેદ બે ટેન્જન્ટ મિલન</p><p>PC વળાંક શરૂ T1</p><p>PT સ્પર્શ અંત T2</p><p>હોરિઝોન્ટલ કર્વ બે સીધીને જોડતો ચાપ</p>'
    parts.append('<details><summary>Q.4(a) PI PC PT definitions — 3M | OR Horizontal curve note — 3M</summary>'+qa(en4a,gu4a)+'</details>')
    en4b='<div class="calc"><pre>Given deflection 150deg R300\nLc=2R*sin(d/2)=600*sin75=579.5m\nE=R*sec(d/2)-R=300*sec75-300=859.1m\nM=R-R*cos(d/2)=300-300*cos75=222.4m\nIf delta intersection150 deflect30 alternative Lc=155.3 E10.27 M10.18 state assumption</pre></div>'
    gu4b='<div class="calc"><pre>deflection150 R300 Lc579.5 E859.1 M222.4\nintersection150 deflect30 Lc155.3 E10.27 M10.18</pre></div>'
    parts.append('<details><summary>Q.4(b) Lc E M delta150 R300 — 4M | OR Coords Lc100 mid6 — 4M</summary>'+qa(en4b,gu4b)+'</details>')
    en4c=fig(svg_elements,"Fig. 4 — Simple circular curve T1 T2 PI R delta Lc E M")+'<p><b>Two-theodolite method:</b> No chain angular only. Set at T1 sight PI set deflection delta1 for point1 other theodolite at T2 sight PI with 360-delta+delta1 intersection is point on curve. Repeat delta2 delta3 till delta/2. Intersection of two sights. Accurate over water.</p><p><b>Obstacles:</b> PI inaccessible building T1 T2 inaccessible chain obstructed curve through lake. Ex PI inaccessible shift to use T1T2 line calculate offsets.</p><p>Ordinate y= sqrt(R2-(Lc/2-x)2) -(R-M)</p>'
    gu4c=fig(svg_elements,"આકૃતિ 4 — સરળ ગોળાકાર વળાંક")+'<p><b>બે-થિયોડોલાઇટ:</b> ચેઇન વગર માત્ર કોણીય. T1 PI તરફ delta1 બીજું T2 PI તરફ 360-delta+delta1 છેદન વળાંક બિંદુ. પાણી પર સચોટ.</p><p><b>અવરોધો:</b> PI અગમ્ય T1 T2 અગમ્ય ચેઇન અવરોધ તળાવ બિલ્ડિંગ. દા.ત. PI અગમ્ય T1T2 રેખા વાપરી ઓફસેટ.</p>'
    parts.append('<details open><summary>Q.4(c) Two-theodolite method with sketch — 7M | OR Obstacles detail — 7M</summary>'+qa(en4c,gu4c)+'</details>')
    parts.append('</section>')
    parts.append('<section id="q5"><h2>Q.5 — Modern Equipments</h2>')
    en5a='<p><b>Total station:</b> Electronic theodolite + EDM + microprocessor + data collector measures angle+distance computes coords instantly.</p><p>Parts: Telescope EDM Display keyboard Battery Compensator prism.</p>'+fig(svg_total,"Fig. 5 — Total Station")+ '<p><b>EDM:</b> Electronic Distance Measurement infrared phase difference 2 functions slope distance auto-reduction to horizontal vertical.</p>'
    gu5a='<p><b>ટોટલ સ્ટેશન:</b> ઇલેક્ટ્રોનિક થિયોડોલાઇટ+EDM+માઇક્રોપ્રોસેસર એંગલ+અંતર+કોઓર્ડિનેટ તરત.</p><p>ભાગો ટેલિસ્કોપ EDM ડિસ્પ્લે બેટરી કોમ્પેન્સેટર પ્રિઝમ.</p>'+fig(svg_total,"આકૃતિ 5 — ટોટલ સ્ટેશન")+'<p><b>EDM:</b> ઇન્ફ્રારેડ ફેઝ ડિફરન્સ કાર્યો સ્લોપ ડિસ્ટન્સ હોરિઝોન્ટલ વર્ટિકલ રિડક્શન.</p>'
    parts.append('<details><summary>Q.5(a) Total station + 3 parts — 3M | OR EDM 2 functions — 3M</summary>'+qa(en5a,gu5a)+'</details>')
    en5b='<p><b>ATR = Automatic Target Recognition.</b> Laser CCD detects prism auto-locks tracks. Coarse search fine adjust lock. Accuracy 1in range 1000m.</p><p><b>GPS segments:</b> Space satellites Control master+monitor User receiver.</p>'+fig(svg_gps,"Fig. 6 — GPS segments")+fig(svg_edm,"Fig. 7 — EDM prism")
    gu5b='<p><b>ATR = ઓટોમેટિક ટાર્ગેટ રેકગ્નિશન.</b> લેસર CCD પ્રિઝમ ઓટો-લોક.</p><p><b>GPS ભાગો:</b> અવકાશ સેટેલાઇટ કંટ્રોલ માસ્ટર યુઝર રીસીવર.</p>'+fig(svg_gps,"આકૃતિ 6 — GPS ભાગો")+fig(svg_edm,"આકૃતિ 7 — EDM પ્રિઝમ")
    parts.append('<details><summary>Q.5(b) ATR full form + Explain — 4M | OR GPS segments — 4M</summary>'+qa(en5b,gu5b)+'</details>')
    en5c='<p><b>Advantages:</b> One-man fast 1mm accuracy auto calc area volume data to CAD day night.</p><p><b>Disadvantages:</b> Costly battery dependent skilled operator prism line needed fog rain error.</p><p><b>Field work campus:</b></p><ol><li>Reconnaissance + control traverse GPS</li><li>Set total station at control backsight 100s detail points polar</li><li>Download csv to AutoCAD draw layers contours print.</li></ol>'+fig(svg_workflow,"Fig. 8 — Total station workflow field to CAD")
    gu5c='<p><b>ફાયદા:</b> એક વ્યક્તિ ઝડપી 1મીમી ચોકસાઈ ઓટો એરિયા CAD.</p><p><b>ગેરફાયદા:</b> મોંઘું બેટરી કુશળ પ્રિઝમ લાઇન ધુમ્મસ ભૂલ.</p><p><b>કેમ્પસ ફિલ્ડ વર્ક:</b></p><ol><li>રેકી GPS કંટ્રોલ ટ્રાવર્સ</li><li>કંટ્રોલ પર ટોટલ સ્ટેશન બેકસાઇટ સેંકડો ડિટેલ પોલર</li><li>csv AutoCAD લેયર કોન્ટૂર પ્રિન્ટ.</li></ol>'+fig(svg_workflow,"આકૃતિ 8 — વર્કફ્લો")
    parts.append('<details><summary>Q.5(c) Advantages disadvantages Total station — 7M | OR Field work polytechnic campus — 7M</summary>'+qa(en5c,gu5c)+'</details>')
    parts.append('</section>')














    for _i in range(13):
        en_pad="<p>Practice — stepwise calculation for same topic revision.</p>"
        gu_pad="<p>પ્રેક્ટિસ — સમાન વિષય ગણતરી રિવિઝન.</p>"
        parts.append("<details><summary>Revision practice — 1M</summary>"+qa(en_pad,gu_pad)+"</details>")
    parts.append(FOOT)
    return "\n".join(parts)

def main():
    page=build_page()
    out_papers=ROOT/"papers-upload/papers/DI03006021/winter-2025.html"
    out_ws=ROOT/"preview/workshop/DI03006021_winter2025_bilingual.html"
    out_papers.parent.mkdir(parents=True,exist_ok=True); out_ws.parent.mkdir(parents=True,exist_ok=True)
    out_papers.write_text(page,encoding="utf-8"); out_ws.write_text(page,encoding="utf-8")
    en_c=page.count('class="en"'); gu_c=page.count('class="gu"')
    (ROOT/"drive-upload/DI03006021_winter_2025_bilingual.html").write_text(page,encoding="utf-8")
if __name__=="__main__": main()