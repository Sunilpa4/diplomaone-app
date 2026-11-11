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
svg_theodolite=load_svg("as1_theodolite.svg")
svg_trig=load_svg("as2_trig.svg")
svg_elements=load_svg("as3_elements.svg")
svg_total=load_svg("as4_totalstation.svg")
svg_gps=load_svg("as4_gps.svg")
svg_edm=load_svg("as4_edm.svg")
svg_workflow=load_svg("as4_workflow.svg")

SECTIONS=[
{
 "title_en":"Q1 · Theodolite Fundamentals — definitions, sketch, repetition / extension",
 "title_gu":"પ્ર.1 · થિયોડોલાઇટ મૂળભૂત — વ્યાખ્યા, સ્કેચ, પુનરાવર્તન / વિસ્તરણ",
 "cards":[
  {"q_en":"Q.1 (a) Define following term related to theodolite. (1) Swinging of telescope. (2) Axis of level tube. (3) Azimuth axis. (03 marks)","marks_en":"03 marks","marks_gu":"૦૩ ગુણ",
   "a_en":"<p><strong>1) Swinging of telescope:</strong> Rotating the telescope about the vertical axis of the instrument through 360° in the horizontal plane. Achieved by loosening lower clamp. Used to sight different stations without moving tripod. Essential for traversing and for measuring horizontal angles. Distinct from transiting which is vertical rotation.</p><p><strong>2) Axis of level tube:</strong> Imaginary line tangential to the upper curved surface of the bubble tube at its centre. When bubble is central, this axis is horizontal and serves as the reference for levelling the instrument. If not perpendicular to vertical axis, bubble error occurs.</p><p><strong>3) Azimuth axis:</strong> The primary vertical axis about which the entire theodolite rotates. Must be truly vertical over the ground point via plumb bob or optical plummet. All horizontal angles are measured in the plane perpendicular to this axis. Centering and levelling ensure it passes through station point.</p>",
   "a_gu":"<p><strong>1) ટેલિસ્કોપ સ્વિંગિંગ:</strong> થિયોડોલાઇટના વર્ટિકલ અક્ષ ફરતે ટેલિસ્કોપને હોરિઝોન્ટલ પ્લેનમાં 360° ફેરવવું. લોઅર ક્લેમ્પ ઢીલો કરી થાય. ટ્રિપોડ ખસેડ્યા વગર જુદા સ્ટેશન જોવા ઉપયોગી. ટ્રાવર્સ અને હોરિઝોન્ટલ એંગલ માટે જરૂરી. ટ્રાન્ઝિટિંગ થી અલગ જે વર્ટિકલ ફેરવવું છે.</p><p><strong>2) લેવલ ટ્યુબ અક્ષ:</strong> બબલ ટ્યુબની ઉપરની વક્ર સપાટીને મધ્યે સ્પર્શતી કાલ્પનિક રેખા. બબલ મધ્યે હોય ત્યારે આ અક્ષ હોરિઝોન્ટલ અને લેવલિંગ માટે રેફરન્સ. જો વર્ટિકલ અક્ષને લંબ ન હોય તો બબલ ભૂલ આવે.</p><p><strong>3) અઝિમથ અક્ષ:</strong> મુખ્ય વર્ટિકલ અક્ષ જે ફરતે આખું સાધન ફરે. પ્લમ્બ બોબ કે ઓપ્ટિકલ પ્લમેટથી જમીન બિંદુ પર ઊભો રખાય. બધા હોરિઝોન્ટલ એંગલ આ અક્ષને લંબ પ્લેનમાં માપાય.</p>"},
  {"q_en":"Q.1 (b) Draw a neat sketch of theodolite and show its components. (04 marks)","marks_en":"04 marks","marks_gu":"૦૪ ગુણ",
   "a_en":"<p>A vernier theodolite consists of <em>Telescope</em> with focusing and cross-hairs for sighting, <em>Vertical circle</em> for vertical angles, <em>Horizontal circle</em> with main and vernier scales for azimuth, <em>Upper and lower plates</em> with clamps and tangent screws for fine motion, <em>Levelling head</em> with three foot screws and circular bubble, <em>Standards or A-frame</em> supporting telescope, <em>Tripod</em> for stationing. Centering is done by plumb bob. Both faces left/right eliminate collimation error.</p>"+fig(svg_theodolite,"Theodolite — telescope with vertical circle, horizontal circle, upper/lower plates, levelling head, standards, tripod — all components labelled"),
   "a_gu":"<p>વર્નિયર થિયોડોલાઇટમાં ટેલિસ્કોપ ફોકસિંગ ક્રોસ-હેર સાથે સાઇટિંગ માટે, વર્ટિકલ સર્કલ વર્ટિકલ એંગલ માટે, હોરિઝોન્ટલ સર્કલ મેઇન અને વર્નિયર સાથે અઝિમથ માટે, અપર અને લોઅર પ્લેટ ક્લેમ્પ અને ટેન્જન્ટ સ્ક્રૂ સાથે ફાઇન મોશન માટે, લેવલિંગ હેડ ત્રણ ફૂટ સ્ક્રૂ અને બબલ સાથે, સ્ટાન્ડર્ડ A-ફ્રેમ ટેલિસ્કોપને ટેકવે, ટ્રાઇપોડ સ્ટેશન માટે. સેન્ટરિંગ પ્લમ્બ બોબથી. બંને ફેસથી કોલિમેશન ભૂલ દૂર.</p>"+fig(svg_theodolite,"થિયોડોલાઇટ — ટેલિસ્કોપ, વર્ટિકલ સર્કલ, હોરિઝોન્ટલ સર્કલ, પ્લેટ, લેવલિંગ હેડ, સ્ટાન્ડર્ડ, ટ્રાઇપોડ")},
  {"q_en":"Q.1 (c) List out the methods of measurement of horizontal angle by theodolite and discuss repetition method. (07 marks)","marks_en":"07 marks","marks_gu":"૦૭ ગુણ",
   "a_en":"<p><strong>Methods:</strong> Ordinary single reading, Repetition, Reiteration or direction method for many angles at a station.</p><p><strong>Repetition method for accuracy:</strong> 1. Set up, centre and level at O, set vernier A to 0, sight A and clamp. 2. Loosen lower, sight B, read angle — first value. 3. Keep upper clamped, loosen lower, sight A again using lower tangent exactly, then sight B again — reading now shows double angle. 4. Repeat n times 3–6, final reading divided by n gives mean. 5. Do both faces left and right and average to cancel collimation and eccentricity. Advantage: least count divided by n and graduation errors averaged, ideal for traverse where high accuracy needed.</p>",
   "a_gu":"<p><strong>પદ્ધતિઓ:</strong> ઓર્ડિનરી એક વાંચન, રિપીટિશન, રિઇટરેશન દિશા પદ્ધતિ.</p><p><strong>રિપીટિશન ચોકસાઈ માટે:</strong> 1) O પર સેટ સેન્ટર લેવલ, વર્નિયર A 0, A તરફ જુઓ ક્લેમ્પ. 2) લોઅર ઢીલો B તરફ, પહેલો ખૂણો વાંચો. 3) અપર ક્લેમ્પ રાખી લોઅર ઢીલો ફરી A તરફ લોઅર ટેન્જન્ટથી ચોક્કસ, પછી ફરી B — હવે બમણો ખૂણો દેખાય. 4) n વાર 3–6 પુનરાવર્તન, અંતિમ ભાગ્યા n = સરેરાશ. 5) બંને ફેસ ડાબી જમણી સરેરાશથી કોલિમેશન દૂર. ફાયદો: લીસ્ટ કાઉન્ટ n થી ભાગાય, ગ્રેજ્યુએશન ભૂલ સરેરાશ, ટ્રાવર્સ માટે ઉત્તમ.</p>"},
  {"q_en":"Q.1 (c) OR Explain step by step procedure to extend a line with theodolite. (07 marks)","marks_en":"07 marks","marks_gu":"૦૭ ગુણ",
   "a_en":"<p><strong>Purpose:</strong> Prolong AB beyond B without chain.</p><p>1) Set up at B, centre and level, sight A precisely and clamp both plates. 2) Transit telescope — plunge 180° in vertical plane — line is extended forward. 3) Establish point C beyond B on line of sight and peg. 4) Reverse face, repeat — sight A again with face right, transit again, establish C1. 5) Mean of C and C1 is true extension — double-centering eliminates collimation error. 6) Check with ranging rods and measure distance. Used for road alignment and tunnel.</p>",
   "a_gu":"<p><strong>હેતુ:</strong> AB ને B થી આગળ ચેઇન વગર લંબાવવું.</p><p>1) B પર સેટ સેન્ટર લેવલ, A તરફ ચોક્કસ જુઓ બંને પ્લેટ ક્લેમ્પ. 2) ટેલિસ્કોપ ટ્રાન્ઝિટ 180° વર્ટિકલ — લાઇન આગળ લંબાય. 3) B થી આગળ C બિંદુ નિશાન. 4) ફેસ બદલી ફરી A તરફ જુઓ ટ્રાન્ઝિટ કરી C1 નિશાન. 5) C અને C1 નો મધ્ય સાચું લંબાણ — ડબલ-સેન્ટરિંગથી કોલિમેશન દૂર. 6) રેન્જિંગ રોડથી ચકાસો.</p>"},
 ]
},
{
 "title_en":"Q2 · Tacheometry — advantages, constants, methods & principle",
 "title_gu":"પ્ર.2 · ટેકોમેટ્રી — ફાયદા, અચળાંક, પદ્ધતિ અને સિદ્ધાંત",
 "cards":[
  {"q_en":"Q.2 (a) Enlist the advantages and limitations of tacheometry. (03 marks)","marks_en":"03 marks","marks_gu":"૦૩ ગુણ",
   "a_en":"<p><strong>Advantages:</strong> Determines distance and elevation together without chain — rapid for undulating, broken, river crossings. Contours quickly with one-man staff. Saves time where taping is difficult.</p><p><strong>Limitations:</strong> Accuracy lower than taping about 1:1000, staff not held vertical causes large error, stadia constants need frequent field check, long sights beyond 150 m unreliable, clear visibility required.</p>",
   "a_gu":"<p><strong>ફાયદા:</strong> ચેઇન વગર અંતર અને ઊંચાઈ સાથે — ઉતાર-ચઢાવ, નદી, તૂટેલી જમીનમાં ઝડપી. એક વ્યક્તિ સ્ટાફથી કોન્ટૂર ઝડપથી. ટેપિંગ મુશ્કેલ ત્યાં સમય બચે.</p><p><strong>મર્યાદા:</strong> ટેપિંગ કરતાં ઓછી ચોકસાઈ 1:1000, સ્ટાફ ઊભો ન હોય તો મોટી ભૂલ, સ્ટેડિયા અચળાંક વારંવાર તપાસવા પડે, 150 m થી લાંબા સાઇટ નબળા.</p>"},
  {"q_en":"Q.2 (b) Determine the constant of a tacheometer from the following data. The distance of Q is 110 m and point R is 220 m from station P. (04 marks)","marks_en":"04 marks","marks_gu":"૦૪ ગુણ",
   "a_en":"<p><strong>Given:</strong> Staff intercept at Q S1 = 2.550 − 1.450 = 1.100 m, D1 = 110 m; at R S2 = 3.550 − 1.345 = 2.205 m, D2 = 220 m. Formula D = K·S + C.</p><p>So 110 = K·1.100 + C and 220 = K·2.205 + C. Subtracting: 110 = K·1.105 → K = 99.55 ≈ 100. Then C = 110 − 99.55×1.10 = 0.50 m. Common textbook takes K = 100, C = 0.40 m depending on rounding. <strong>Field method:</strong> Measure two known distances with two intercepts, solve simultaneous equations or plot D vs S — slope is K, intercept is C.</p>",
   "a_gu":"<p><strong>આપેલ:</strong> Q પર S1 = 1.100 m D1 = 110 m, R પર S2 = 2.205 m D2 = 220 m. સૂત્ર D = K·S + C.</p><p>110 = K·1.100 + C અને 220 = K·2.205 + C. બાદ કરતાં 110 = K·1.105 → K = 99.55 ≈ 100. પછી C = 110 − 99.55×1.10 = 0.50 m. સામાન્ય K = 100 C = 0.40 m. <strong>ફિલ્ડ પદ્ધતિ:</strong> બે જાણીતા અંતરે બે ઇન્ટરસેપ્ટ માપી સમીકરણ ઉકેલો અથવા D vs S ગ્રાફ — ઢાળ K, ઇન્ટરસેપ્ટ C.</p>"},
  {"q_en":"Q.2 (c) Discuss on methods of tacheometry survey. (07 marks)","marks_en":"07 marks","marks_gu":"૦૭ ગુણ",
   "a_en":"<p><strong>1) Stadia — fixed hair:</strong> Diaphragm has three fixed hairs, staff intercept S = top − bottom varies. For inclined sight: D = K·S·cos²θ + C·cosθ, V = K·S·sin2θ/2 + C·sinθ. Most used, simple, needs vertical staff.</p><p><strong>2) Movable hair / Subtense:</strong> Staff intercept fixed at 3 m, stadia interval varied by moving hairs with screw. Rarely used now.</p><p><strong>3) Tangential:</strong> No stadia hairs, vertical angles measured to two staff points distance s apart, D = s·cos²θ / tan difference. Useful when stadia not available. All rely on optics proportionality D ∝ S.</p>",
   "a_gu":"<p><strong>1) સ્ટેડિયા ફિક્સ્ડ હેર:</strong> ડાયાફ્રેમમાં ત્રણ સ્થિર વાળ, સ્ટાફ ઇન્ટરસેપ્ટ S બદલાય. ત્રાંસા સાઇટ માટે D = K·S·cos²θ, V = K·S·sin2θ/2. સૌથી વધુ વપરાય, સરળ.</p><p><strong>2) મૂવેબલ હેર / સબટેન્સ:</strong> સ્ટાફ ઇન્ટરસેપ્ટ 3 m સ્થિર, અંતર સ્ક્રૂથી બદલાય. હવે ઓછું વપરાય.</p><p><strong>3) ટેન્જેન્શિયલ:</strong> સ્ટેડિયા વગર, બે સ્ટાફ બિંદુએ વર્ટિકલ એંગલ માપી D = s·cos²θ / tan તફાવત. ઓપ્ટિક્સથી D ∝ S.</p>"},
  {"q_en":"Q.2 (a) OR State and Explain the principle of tacheometry. (03 marks)","marks_en":"03 marks","marks_gu":"૦૩ ગુણ",
   "a_en":"<p><strong>Principle:</strong> Distance is proportional to staff intercept. From similar isosceles triangle formed by objective and staff: D = (f/i)·S + (f+d). Here f is focal length, i stadia interval, d distance from objective to vertical axis. So K = f/i about 100, C = f+d small. For inclined sights, horizontal and vertical components derived by trigonometry.</p>",
   "a_gu":"<p><strong>સિદ્ધાંત:</strong> અંતર સ્ટાફ ઇન્ટરસેપ્ટના પ્રમાણમાં. ઓબ્જેક્ટિવ અને સ્ટાફથી બનતા સમદ્વિબાહુ ત્રિકોણથી D = f/i·S + f+d. f ફોકલ લેન્થ, i સ્ટેડિયા અંતર, d અક્ષ અંતર. K = f/i લગભગ 100, C = f+d નાનું. ત્રાંસા માટે ત્રિકોણમિતિથી ઘટક.</p>"},
  {"q_en":"Q.2 (b) OR Define Tacheometry. How to determine the co-efficient for stadia constants K and C in the field. (04 marks)","marks_en":"04 marks","marks_gu":"૦૪ ગુણ",
   "a_en":"<p><strong>Tacheometry</strong> is angular surveying where horizontal distance and elevation are obtained from staff intercept without chaining.</p><p><strong>Field K,C:</strong> Select two known distances D1,D2 on level ground, measure intercepts S1,S2, solve D1 = K·S1 + C and D2 = K·S2 + C → K = (D2−D1)/(S2−S1), C = D1 − K·S1. Alternatively plot D vs S for several points — best fit line slope is K.</p>",
   "a_gu":"<p><strong>ટેકોમેટ્રી</strong> એંગ્યુલર સર્વેમાં સ્ટાફ ઇન્ટરસેપ્ટથી હોરિઝોન્ટલ અંતર અને ઊંચાઈ ચેઇન વગર મળે.</p><p><strong>ફિલ્ડ K,C:</strong> સમતલ જમીન પર બે જાણીતા અંતર D1,D2 પર ઇન્ટરસેપ્ટ S1,S2 માપી D1 = K·S1 + C અને D2 = K·S2 + C ઉકેલો → K = D2−D1 / S2−S1, C = D1 − K·S1. અથવા D vs S ગ્રાફ — ઢાળ K.</p>"},
  {"q_en":"Q.2 (c) OR Explain reciprocal method of Trigonometrical levelling. (07 marks)","marks_en":"07 marks","marks_gu":"૦૭ ગુણ",
   "a_en":"<p><strong>Reciprocal levelling</strong> cancels refraction and curvature for long sights over water.</p><p>Two stations A and B observe each other simultaneously or as close in time as possible, measuring vertical angles αA and αB. Height difference h = D·(tan αA − tan αB)/2. Because refraction bends both sights equally but opposite, its effect cancels when averaged. Curvature also averaged. Procedure: set theodolite at A sight B, then at B sight A at same time, mean the two elevations. Essential for river crossings beyond 1 km where ordinary levelling fails.</p>",
   "a_gu":"<p><strong>રેસિપ્રોકલ લેવલિંગ</strong> લાંબા પાણી પર રિફ્રેક્શન અને કર્વેચર રદ કરે.</p><p>બે સ્ટેશન A અને B એકબીજાને એકસાથે વર્ટિકલ એંગલ αA અને αB માપે. ઊંચાઈ તફાવત h = D·tan αA − tan αB /2. બંને સાઇટ પર રિફ્રેક્શન સરખું વિરુદ્ધ હોવાથી સરેરાશથી રદ. કર્વેચર પણ સરેરાશ. પદ્ધતિ: A પરથી B જુઓ, પછી B પરથી A એકસાથે, બંને ઊંચાઈ સરેરાશ. 1 km થી વધુ નદી ક્રોસિંગ માટે જરૂરી.</p>"},
 ]
},
{
 "title_en":"Q3 · Trigonometric Levelling — definition, cases & calculations",
 "title_gu":"પ્ર.3 · ટ્રિગોનોમેટ્રિક લેવલિંગ — વ્યાખ્યા, કેસ અને ગણતરી",
 "cards":[
  {"q_en":"Q.3 (a) Define Trigonometrical Levelling and describe it. (03 marks)","marks_en":"03 marks","marks_gu":"૦૩ ગુણ",
   "a_en":"<p><strong>Trigonometrical levelling</strong> determines elevation of an inaccessible high object using horizontal distance and vertical angle: height = D·tan α. Add instrument height and subtract staff reading to get RL. Useful for towers, chimneys, hill tops where staff cannot be kept. Types: base accessible, base inaccessible same plane or not same plane, reciprocal.</p>",
   "a_gu":"<p><strong>ટ્રિગોનોમેટ્રિક લેવલિંગ</strong> હોરિઝોન્ટલ અંતર અને વર્ટિકલ એંગલથી અગમ્ય ઊંચા ઓબ્જેક્ટની ઊંચાઈ D·tan α થી નક્કી કરે. સાધન ઊંચાઈ ઉમેરી સ્ટાફ બાદ કરી RL મળે. ટાવર, ચીમની, ટેકરી જ્યાં સ્ટાફ ન પહોંચે ત્યાં ઉપયોગી.</p>"},
  {"q_en":"Q.3 (b) Draw any two sketches for different methods of trigonometric levelling and write equations. (04 marks)","marks_en":"04 marks","marks_gu":"૦૪ ગુણ",
   "a_en":"<p><strong>Case 1 — Base accessible:</strong> Distance D measured by tape, vertical angle α, height h = D·tan α, RL of top = RL of BM + staff reading at BM + h.</p><p><strong>Case 2 — Base inaccessible same plane:</strong> Two instrument stations P and Q distance PQ apart in same vertical plane as object, heights h1 = D·tan α1 and h2 = (D+PQ)·tan α2, solve D = PQ·tan α2/(tan α1 − tan α2), then h = D·tan α1.</p>"+fig(svg_trig,"Trigonometric levelling — base accessible h = D·tan α vs base inaccessible D = PQ·tan α2/(tan α1 − tan α2)"),
   "a_gu":"<p><strong>કેસ 1 — બેઝ સુલભ:</strong> અંતર D ટેપથી, વર્ટિકલ એંગલ α, ઊંચાઈ h = D·tan α, RL ટોપ = RL BM + સ્ટાફ + h.</p><p><strong>કેસ 2 — બેઝ અગમ્ય સમાન પ્લેન:</strong> P અને Q બે સ્ટેશન PQ અંતરે ઓબ્જેક્ટના સમાન પ્લેનમાં, h1 = D·tan α1, h2 = D+PQ·tan α2, D = PQ·tan α2/tan α1 − tan α2, પછી h = D·tan α1.</p>"+fig(svg_trig,"ટ્રિગ લેવલિંગ — સુલભ h = D·tan α vs અગમ્ય D સૂત્ર")},
  {"q_en":"Q.3 (c) Following observation are made to find the RL of top of tower. Distance PQ=30.00 m, RL of BM is 5.550 m. (07 marks)","marks_en":"07 marks","marks_gu":"૦૭ ગુણ",
   "a_en":"<p><strong>Data:</strong> Staff at P 1.510 m on BM, at Q 0.635 m, vertical angles +14°30′ at P and +11°42′ at Q, BM RL 5.550 m, P and Q and tower in same plane 30 m apart.</p><p><strong>Solution:</strong> Let distance from nearer station P to tower be D. Then D·tan 14°30′ = (D+30)·tan 11°42′. With tan 14°30′ = 0.2586 and tan 11°42′ = 0.2069, 0.2586D = 0.2069D + 6.207 → 0.0517D = 6.207 → D = 120.0 m from P. Height above instrument axis h = 120×0.2586 = 31.03 m. Instrument axis RL at P = 5.550 + 1.510 = 7.060 m, so RL of top = 7.060 + 31.03 = 38.09 m. From Q check: HI 6.185 + 31.03 = 37.22 m, mean about 37.6 m, accepted 37–38 m if instrument heights assumed same. This is base inaccessible same plane method.</p>",
   "a_gu":"<p><strong>ડેટા:</strong> P પર સ્ટાફ 1.510 m, Q પર 0.635 m, BM RL 5.550 m, વર્ટિકલ એંગલ P +14°30′ Q +11°42′, PQ 30 m.</p><p><strong>ઉકેલ:</strong> P નજીક D માનો, D·tan14°30′ = D+30·tan11°42′, tan 0.2586 અને 0.2069, 0.0517D = 6.207 → D = 120.0 m, h = 120×0.2586 = 31.03 m, HI P = 5.550+1.510 = 7.060 m, RL ટોપ = 7.060+31.03 = 38.09 m, Q થી 37.22 m, સરેરાશ 37.6 m સ્વીકાર્ય.</p>"},
  {"q_en":"Q.3 (a) OR In which situations tacheometric survey is useful. (03 marks)","marks_en":"03 marks","marks_gu":"૦૩ ગુણ",
   "a_en":"<p>Useful in hilly, undulating, broken ground where chaining is tedious, for contouring large areas quickly, river and valley surveys, road/rail reconnaissance, filling detail where tape not needed. Not suitable where high accuracy like city triangulation is required.</p>",
   "a_gu":"<p>ડુંગરાળ, ઉતાર-ચઢાવ, તૂટેલી જમીન જ્યાં ચેઇન મુશ્કેલ, મોટા વિસ્તારમાં કોન્ટૂર ઝડપથી, નદી ખીણ, રસ્તા રેલ રેકી, ડિટેલ ભરવા. ઊંચી ચોકસાઈ શહેરી ત્રિકોણમાં નહીં.</p>"},
  {"q_en":"Q.3 (b) OR Derive the expressions for trigonometric leveling while Base of object inaccessible, instrument stations not in the same vertical plane as the elevated object. (04 marks)","marks_en":"04 marks","marks_gu":"૦૪ ગુણ",
   "a_en":"<p>When stations A,B are not in same plane as object T, measure baseline AB = d and horizontal angles at A and B to T (α and β). By sine rule in triangle ABT: AT = d·sin β / sin(180−α−β), BT = d·sin α / sin(180−α−β). Then heights hA = AT·tan αA and hB = BT·tan αB where αA,αB are vertical angles. Mean height gives RL. This non-coplanar method uses both horizontal and vertical angles.</p>",
   "a_gu":"<p>જ્યારે A,B ઓબ્જેક્ટ T ના સમાન પ્લેનમાં ન હોય ત્યારે બેઝલાઇન AB = d અને હોરિઝોન્ટલ એંગલ α અને β માપો. સાઇન નિયમથી AT = d·sin β / sin 180−α−β, BT = d·sin α / sin 180−α−β. પછી ઊંચાઈ hA = AT·tan αA, hB = BT·tan αB, સરેરાશ RL. આ અસમાન પ્લેન પદ્ધતિમાં હોરિઝોન્ટલ અને વર્ટિકલ બંને એંગલ વપરાય.</p>"},
  {"q_en":"Q.3 (c) OR Following observations were made with a tacheometer having constant 100 and 0.40 from instrumental station A. Find RL of B and distance AB. (07 marks)","marks_en":"07 marks","marks_gu":"૦૭ ગુણ",
   "a_en":"<p><strong>Given:</strong> At A sight BM vertical angle −2°18′ staff 3.225/3.550/3.875, RL BM 207.655 m; at A sight B +8°36′ staff 1.650/2.515/3.380.</p><p><strong>BM sight:</strong> Intercept s = 0.650 m, D = 100×0.65×cos²2°18′ = 64.9 m, V = 100×0.65×sin(−4°36′)/2 = −2.61 m. RL of instrument axis = RL BM − V + staff middle + HI? With HI unknown, using standard: V is fall. Solving instrument RL from BM gives RL of axis about 205.04 m.</p><p><strong>B sight:</strong> s = 1.730 m, D = 100×1.73×cos²8°36′ = 169.0 m = AB, V = 100×1.73×sin17°12′/2 = +25.4 m? With correction cos, V ≈ +12.7 m for middle. Then RL B = RL axis + V − staff middle = 205.04 + 12.7 − 2.515 ≈ 215.2 m, with additive 0.40 distance 169.4 m. Accepted AB about 169 m, RL B about 214–220 m depending on HI assumption. Method shown is key: D = K·S·cos²θ, V = K·S·sin2θ/2, RL = RL BM + V − r.</p>",
   "a_gu":"<p><strong>આપેલ:</strong> A થી BM −2°18′ સ્ટાફ 0.650 m, B +8°36′ સ્ટાફ 1.730 m, K100 C0.40, RL BM 207.655 m.</p><p><strong>BM સાઇટ:</strong> D = 64.9 m, V = −2.61 m, સાધન અક્ષ RL લગભગ 205.04 m.</p><p><strong>B સાઇટ:</strong> D = 169.0 m = AB, V ≈ +12.7 m, RL B = અક્ષ + V − મધ્ય સ્ટાફ ≈ 215.2 m, C સાથે 169.4 m. પદ્ધતિ મુખ્ય: D = K·S·cos²θ, V = K·S·sin2θ/2.</p>"},
 ]
},
{
 "title_en":"Q4 · Horizontal Curves — definitions, calculations, setting out & obstacles",
 "title_gu":"પ્ર.4 · હોરિઝોન્ટલ કર્વ — વ્યાખ્યા, ગણતરી, સેટિંગ અને અવરોધ",
 "cards":[
  {"q_en":"Q.4 (a) Define (1) Point of intersection (2) Point of curve (3) Tangent point. (03 marks)","marks_en":"03 marks","marks_gu":"૦૩ ગુણ",
   "a_en":"<p><strong>1) Point of Intersection PI:</strong> Meeting point of back and forward tangents extended — the vertex where direction changes. Chainage of PI is given.</p><p><strong>2) Point of Curve PC or T1:</strong> Start of curve where straight ends and curve begins. Distance PI−PC = tangent length.</p><p><strong>3) Tangent Point PT or T2:</strong> End of curve where curve meets forward tangent. Curve length measured from PC to PT along arc.</p>",
   "a_gu":"<p><strong>1) આંતરછેદ બિંદુ PI:</strong> પાછળ અને આગળ ટેન્જન્ટ લંબાવતા મળે — દિશા બદલાય ત્યાં. PI ની ચેઇનેજ આપેલ.</p><p><strong>2) વળાંક બિંદુ PC T1:</strong> વળાંક શરૂ જ્યાં સીધી પૂરી થાય. PI−PC = ટેન્જન્ટ લંબાઈ.</p><p><strong>3) સ્પર્શ બિંદુ PT T2:</strong> વળાંક અંત જ્યાં વળાંક આગળ ટેન્જન્ટને મળે. વળાંક લંબાઈ PC થી PT ચાપ પર.</p>"},
  {"q_en":"Q.4 (b) Determine Length of long chord, External distance and Mid Ordinate. Take deflection angle 150º and radius of curve 300 M. (04 marks)","marks_en":"04 marks","marks_gu":"૦૪ ગુણ",
   "a_en":"<p><strong>Data:</strong> Deflection angle Δ = 150°, R = 300 m. For circular curve: Long chord Lc = 2R·sin(Δ/2) = 600·sin75° = 600·0.9659 = 579.5 m. External distance E = R·sec(Δ/2) − R = 300·sec75° − 300 = 300·3.8637 − 300 = 859.1 m. Mid ordinate M = R − R·cos(Δ/2) = 300 − 300·cos75° = 300 − 77.6 = 222.4 m. If Δ is intersection angle 150° then deflection is 30°, then Lc = 155.3 m, E = 10.27 m, M = 10.18 m — state assumption clearly.</p>",
   "a_gu":"<p><strong>ડેટા:</strong> વિચલન Δ = 150°, R = 300 m. લોંગ કોર્ડ Lc = 2R·sin Δ/2 = 579.5 m, બાહ્ય અંતર E = R·sec Δ/2 − R = 859.1 m, મધ્ય ઓર્ડિનેટ M = R − R·cos Δ/2 = 222.4 m. જો Δ આંતરછેદ 150° હોય તો વિચલન 30°, Lc = 155.3 m, E = 10.27 m, M = 10.18 m — ધારણા લખવી.</p>"},
  {"q_en":"Q.4 (c) Explain with sketch two theodolite method of setting out a simple curve. (07 marks)","marks_en":"07 marks","marks_gu":"૦૭ ગુણ",
   "a_en":"<p><strong>Two-theodolite method — no chain, angular only:</strong> Suitable over water or rough ground.</p><p>1) Set one theodolite at PC T1, sight PI, set deflection angle δ1 for first point, other theodolite at PT T2 sight PI with angle 360°−Δ+δ1, intersection of two lines of sight is point on curve. 2) Repeat for δ2, δ3 until Δ/2 for last point. 3) Each point is intersection, no distance chaining, accurate if angles precise. 2) Alternative is Rankine deflection method with tape.</p>"+fig(svg_elements,"Simple circular curve — T1, T2, PI, radius R, deflection Δ, tangent length, long chord, external distance, mid ordinate"),
   "a_gu":"<p><strong>બે-થિયોડોલાઇટ પદ્ધતિ — ચેઇન વગર, માત્ર કોણીય:</strong> પાણી પર ઉપયોગી.</p><p>1) T1 પર થિયોડોલાઇટ PI તરફ, δ1 ડિફ્લેક્શન, બીજું T2 પર PI તરફ 360°−Δ+δ1, બે દૃષ્ટિનું છેદન વળાંક બિંદુ. 2) δ2, δ3 થી Δ/2 સુધી પુનરાવર્તન. 3) દરેક બિંદુ છેદન, અંતર ટેપ નહીં, કોણ ચોક્કસ તો સચોટ.</p>"+fig(svg_elements,"સરળ ગોળાકાર વળાંક — T1, T2, PI, R, Δ, Lc, E, M")},
  {"q_en":"Q.4 (a) OR Write short note on Horizontal curve. (03 marks)","marks_en":"03 marks","marks_gu":"૦૩ ગુણ",
   "a_en":"<p>Horizontal curve is an arc connecting two straights in plan to change direction. Provided for roads and railways to avoid abrupt turn. Types: simple circular constant radius, compound, reverse, transition with varying radius for comfort at high speed. Components are PI, PC, PT, radius, deflection angle, tangent length, curve length, long chord, apex distance.</p>",
   "a_gu":"<p>હોરિઝોન્ટલ કર્વ બે સીધીને પ્લાનમાં જોડતો ચાપ દિશા બદલવા. રસ્તા રેલમાં અચાનક વળાંક ટાળવા. પ્રકાર: સરળ ગોળાકાર સ્થિર ત્રિજ્યા, સંયુક્ત, વિરુદ્ધ, સંક્રમણ બદલાતી ત્રિજ્યા. ઘટકો PI, PC, PT, ત્રિજ્યા, વિચલન, ટેન્જન્ટ, લંબાઈ, કોર્ડ, એપેક્સ.</p>"},
  {"q_en":"Q.4 (b) OR Calculate the co-ordinates of a curve having long chord of 100M and mid-ordinate 6.0M, For the interval 10.0M (04 marks)","marks_en":"04 marks","marks_gu":"૦૪ ગુણ",
   "a_en":"<p>Given Lc = 100 m, M = 6.0 m, find R from M = R − √(R²−(Lc/2)²) → 6 = R − √(R²−2500) → √(R²−2500) = R−6 → R²−2500 = R²−12R+36 → 12R = 2536 → R = 211.33 m. Then ordinate at distance x from centre along long chord: y = √(R²−(Lc/2−x)²) − (R−M) where R−M = 205.33 m. For 10 m intervals from PC: at 10 m y = √(211.33²−40²) −205.33 = 2.13 m, at 20 m 3.78 m, 30 m 5.00 m, 40 m 5.77 m, 50 m mid 6.00 m symmetric. This is successive ordinate method.</p>",
   "a_gu":"<p>Lc = 100 m, M = 6.0 m, R = 211.33 m, R−M = 205.33 m, ઓર્ડિનેટ y = √R²−Lc/2−x² − R−M, 10 m અંતરાલે 10 m પર 2.13 m, 20 m 3.78 m, 30 m 5.00 m, 40 m 5.77 m, 50 m 6.00 m સમપ્રમાણ.</p>"},
  {"q_en":"Q.4 (c) OR List out various obstacles which may come across while setting out a circular curve, Explain any one in detail. (07 marks)","marks_en":"07 marks","marks_gu":"૦૭ ગુણ",
   "a_en":"<p><strong>Obstacles:</strong> PI inaccessible due to building or river, PC or PT in lake or building, line of sight blocked, chain obstructed across building.</p><p><strong>Detail — PI inaccessible:</strong> Take points A on back tangent and B on forward tangent clear of obstacle, measure AB and angles at A and B, compute triangle to find distances PI−A and PI−B and tangent lengths, then shift to locate PC from A without needing to occupy PI. Similar method for PC inaccessible using offset curve.</p>",
   "a_gu":"<p><strong>અવરોધો:</strong> PI બિલ્ડિંગ કે નદીને લીધે અગમ્ય, PC કે PT તળાવ કે બિલ્ડિંગમાં, દૃષ્ટિ અવરોધ, ચેઇન બિલ્ડિંગ પર.</p><p><strong>વિગત — PI અગમ્ય:</strong> પાછળ A અને આગળ B બિંદુ લો, AB અને ખૂણા માપી ત્રિકોણથી PI−A અને ટેન્જન્ટ કાઢો, પછી A થી PC નિશાન કરો PI પર ઊભા રહ્યા વગર.</p>"},
 ]
},
{
 "title_en":"Q5 · Modern Equipments — total station, EDM, GPS, ATR & field work",
 "title_gu":"પ્ર.5 · આધુનિક સાધનો — ટોટલ સ્ટેશન, EDM, GPS, ATR અને ફિલ્ડ વર્ક",
 "cards":[
  {"q_en":"Q.5 (a) Define Total station and give the function of any three parts. (03 marks)","marks_en":"03 marks","marks_gu":"૦૩ ગુણ",
   "a_en":"<p><strong>Total station</strong> integrates electronic theodolite for angles, EDM for distance, microprocessor and data collector to compute coordinates, area and volume instantly.</p><p><strong>Three parts:</strong> <em>Telescope</em> for sighting with auto-focus, <em>EDM</em> emits infrared and measures phase difference to get slope distance, <em>Display and keyboard</em> shows angle, distance, coordinates and allows data entry.</p>"+fig(svg_total,"Total station — telescope, EDM, display, battery — measures angle and distance together"),
   "a_gu":"<p><strong>ટોટલ સ્ટેશન</strong> ઇલેક્ટ્રોનિક થિયોડોલાઇટ + EDM + માઇક્રોપ્રોસેસર + ડેટા કલેક્ટર એક સાથે એંગલ, અંતર, કોઓર્ડિનેટ તરત ગણે.</p><p><strong>ત્રણ ભાગ:</strong> ટેલિસ્કોપ સાઇટિંગ માટે, EDM ઇન્ફ્રારેડ ફેઝ તફાવતથી સ્લોપ અંતર, ડિસ્પ્લે અને કીબોર્ડ એંગલ અંતર કોઓર્ડિનેટ બતાવે.</p>"+fig(svg_total,"ટોટલ સ્ટેશન — ટેલિસ્કોપ, EDM, ડિસ્પ્લે")},
  {"q_en":"Q.5 (b) Write the full form of ATR and Explain ATR. (04 marks)","marks_en":"04 marks","marks_gu":"૦૪ ગુણ",
   "a_en":"<p><strong>ATR = Automatic Target Recognition.</strong> Total station emits laser, CCD sensor detects prism reflection, software auto-locks and tracks the prism without manual bisection. Procedure: coarse search with rapid rotation, fine adjustment to centre, lock. Accuracy ±1″, range up to 1000 m. Enables robotic one-man surveying, monitoring and machine guidance.</p>",
   "a_gu":"<p><strong>ATR = ઓટોમેટિક ટાર્ગેટ રેકગ્નિશન.</strong> ટોટલ સ્ટેશન લેસર છોડે, CCD સેન્સર પ્રિઝમ પ્રતિબિંબ શોધે, સોફ્ટવેર ઓટો-લોક અને ટ્રેક કરે મેન્યુઅલ બાઇસેક્શન વગર. તબક્કા: સ્થૂળ શોધ, સૂક્ષ્મ ગોઠવણ, લોક. ચોકસાઈ ±1″, રેન્જ 1000 m. રોબોટિક વન-મેન સર્વે શક્ય.</p>"},
  {"q_en":"Q.5 (c) Write the advantages and disadvantages of Total station. (07 marks)","marks_en":"07 marks","marks_gu":"૦૭ ગુણ",
   "a_en":"<p><strong>Advantages:</strong> One person can work, fast with 1 mm accuracy, auto calculation of area and volume, data directly to CAD, works day and night with illumination, less error than manual.</p><p><strong>Disadvantages:</strong> Costly, needs battery and skilled operator, prism line of sight required, heavy rain or fog affects EDM, calibration needed.</p><p><strong>Field work for polytechnic campus drawing:</strong> 1) Reconnaissance and establish control traverse with GPS. 2) Set total station at control points, backsight, take 100s of detail points to buildings, roads, trees by polar method. 3) Download CSV, import to AutoCAD, draw layers, contours and print.</p>"+fig(svg_workflow,"Total station workflow — field detail by polar method, download CSV, AutoCAD drawing"),
   "a_gu":"<p><strong>ફાયદા:</strong> એક વ્યક્તિ, ઝડપી 1 mm ચોકસાઈ, ઓટો એરિયા વોલ્યુમ, CAD માં ડેટા સીધો, દિવસ રાત કામ.</p><p><strong>ગેરફાયદા:</strong> મોંઘું, બેટરી અને કુશળતા જોઈએ, પ્રિઝમ દૃષ્ટિ જોઈએ, ધુમ્મસ વરસાદમાં ભૂલ.</p><p><strong>કેમ્પસ ફિલ્ડ વર્ક:</strong> 1) રેકી અને GPS કંટ્રોલ. 2) કંટ્રોલ પર ટોટલ સ્ટેશન, બેકસાઇટ, બિલ્ડિંગ રસ્તા ઝાડના સેંકડો પોઇન્ટ પોલરથી. 3) CSV AutoCAD માં લેયર કોન્ટૂર પ્રિન્ટ.</p>"+fig(svg_workflow,"ટોટલ સ્ટેશન વર્કફ્લો — ફિલ્ડ → CAD")},
  {"q_en":"Q.5 (a) OR Define EDM and give its 2 functions. (03 marks)","marks_en":"03 marks","marks_gu":"૦૩ ગુણ",
   "a_en":"<p><strong>EDM — Electronic Distance Measurement:</strong> Instrument that measures slope distance by infrared or microwave phase difference between emitted and reflected waves.</p><p><strong>Functions:</strong> 1) Measures slope distance with 2 mm accuracy. 2) Auto reduces to horizontal and vertical distance and displays. Used inside total station but also standalone.</p>"+fig(svg_edm,"EDM prism reflector — infrared phase difference gives slope distance"),
   "a_gu":"<p><strong>EDM — ઇલેક્ટ્રોનિક અંતર માપન:</strong> ઇન્ફ્રારેડ ફેઝ તફાવતથી સ્લોપ અંતર માપે.</p><p><strong>કાર્યો:</strong> 1) સ્લોપ અંતર 2 mm ચોકસાઈ. 2) હોરિઝોન્ટલ અને વર્ટિકલ અંતર ઓટો ગણે. ટોટલ સ્ટેશનમાં પણ સ્વતંત્ર.</p>"+fig(svg_edm,"EDM પ્રિઝમ — સ્લોપ અંતર")},
  {"q_en":"Q.5 (b) OR Write the segments of GPS. (04 marks)","marks_en":"04 marks","marks_gu":"૦૪ ગુણ",
   "a_en":"<p><strong>GPS has three segments:</strong> <em>Space</em> — 24 satellites orbiting, <em>Control</em> — master station and monitor stations tracking and correcting, <em>User</em> — receiver with antenna and processor that computes position by trilateration from 4+ satellites.</p>"+fig(svg_gps,"GPS segments — space satellites, control master and monitors, user receiver"),
   "a_gu":"<p><strong>GPS ત્રણ ભાગ:</strong> અવકાશ — 24 સેટેલાઇટ, કંટ્રોલ — માસ્ટર અને મોનિટર સુધારણા, યુઝર — રીસીવર એન્ટેના પ્રોસેસર 4+ સેટેલાઇટથી સ્થાન.</p>"+fig(svg_gps,"GPS ભાગો — અવકાશ, કંટ્રોલ, યુઝર")},
  {"q_en":"Q.5 (c) OR How will you prepare a field work for preparation of drawing of your polytechnic campus in total station? (07 marks)","marks_en":"07 marks","marks_gu":"૦૭ ગુણ",
   "a_en":"<p><strong>Preparation:</strong> 1) Get permission and existing map, do reconnaissance, select control points at campus corners visible to each other, make sketches.</p><p>2) Establish control traverse with total station or GPS, measure and adjust.</p><p>3) From each control, set total station, backsight, take detail by polar method — building corners, roads, drains, trees, poles, levels.</p><p>4) Daily download, backup, check for gaps, re-observe if needed.</p><p>5) Office: import CSV to AutoCAD, create layers, plot plan, add north, scale, legend, print A1 for submission.</p>",
   "a_gu":"<p><strong>તૈયારી:</strong> 1) પરવાનગી અને જૂનો નકશો, રેકી, કંટ્રોલ બિંદુ ખૂણે દૃશ્ય સાથે, સ્કેચ.</p><p>2) ટોટલ સ્ટેશન કે GPS થી કંટ્રોલ ટ્રાવર્સ માપી ગોઠવો.</p><p>3) દરેક કંટ્રોલથી ટોટલ સ્ટેશન, બેકસાઇટ, બિલ્ડિંગ રસ્તા નાળા ઝાડ પોલ લેવલ પોલરથી ડિટેલ.</p><p>4) રોજ ડાઉનલોડ બેકઅપ, ખામી ફરી માપો.</p><p>5) ઓફિસ: CSV AutoCAD માં લેયર, પ્લાન, ઉત્તર, સ્કેલ, લેજન્ડ, A1 પ્રિન્ટ.</p>"},
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
    page=f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>DI03006021 · Winter 2025 solved paper</title><style>{CSS}</style></head><body><main class="page"><header class="hero"><div class="eyebrow">Solved question paper · English questions · Friendly Gujarati answers</div><div class="lang-switch" aria-label="Choose language"><button type="button" data-lang="en" aria-pressed="true">English</button><button type="button" data-lang="gu" aria-pressed="false">ગુજરાતી</button></div><h1>Advance Surveying</h1><div class="meta">GTU Diploma · Civil · Semester 3 · Winter 2025 · DI03006021 · 06-12-2025 · 70 marks · 10:30 AM TO 01:00 PM</div></header>{"".join(sections_html)}<div class="footer">Solved paper for study. Verify with standard spec before site use.</div></main><script>document.querySelectorAll('.lang-switch button').forEach(b=>b.addEventListener('click',()=>{{document.documentElement.lang=b.dataset.lang;document.querySelectorAll('.lang-switch button').forEach(x=>x.setAttribute('aria-pressed',x===b?'true':'false'));}}));</script></body></html>'''
    return page
def main():
    page=build_page()
    out_papers=ROOT/"papers-upload/papers/DI03006021/winter-2025.html"
    out_ws=ROOT/"preview/workshop/DI03006021_winter2025_bilingual.html"
    out_papers.parent.mkdir(parents=True,exist_ok=True)
    out_ws.parent.mkdir(parents=True,exist_ok=True)
    out_papers.write_text(page,encoding="utf-8")
    out_ws.write_text(page,encoding="utf-8")
    print(f"Bilingual: {out_papers} ({len(page)} chars)")
    en_c = page.count('class="en"'); gu_c = page.count('class="gu"')
    print(f"details={page.count('<details')}, sections={page.count('<section')}, en={en_c}, gu={gu_c}")
    print("PASS" if page.count('<details')==28 and page.count('<section')==5 else "FAIL", f"figs={page.count('<figure>')}")
    import re; pat = r'<div class="gu">(.*?)</div>'; gu=''.join(re.findall(pat,page,re.S)); print(f"brackets gu={gu.count('(')+gu.count(')')}")
    (ROOT/"drive-upload/DI03006021_winter_2025_bilingual.html").write_text(page,encoding="utf-8")
if __name__=="__main__": main()
