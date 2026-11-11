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
   "a_en":"<p><strong>Main scale</strong> is graduated 0°–360° with smallest division 20′ or 30′. <strong>Vernier</strong> has 60 divisions covering 59 main divisions in vernier theodolite.</p><p>Least count = smallest main division ÷ number of vernier divisions. If main is 20′ and vernier 60 → LC = 20′/60 = 20″. If main 30′ → LC = 30″. Example: 20″ theodolite can read 20″, 10″ electronic reads 10″ by digital encoder. Parts shown are main graduation, vernier arrow, magnifier and vernier scale.</p>"+fig(svg_vernier,"Main and vernier scales — main 0–360° every 20′, vernier 60 divisions, least count 20″"),
   "a_gu":"<p><strong>મેઇન સ્કેલ</strong> 0°–360° દર 20′ કે 30′, <strong>વર્નિયર</strong> 60 ભાગ 59 મેઇન પર.</p><p>લીસ્ટ કાઉન્ટ = નાનું મેઇન ÷ વર્નિયર સંખ્યા. 20′ હોય તો 20″, 30′ હોય તો 30″. દા. 20″ થિયોડોલાઇટ 20″ વાંચે. ભાગો: મેઇન ગ્રેજ્યુએશન, વર્નિયર તીર, મેગ્નિફાયર.</p>"+fig(svg_vernier,"મેઇન અને વર્નિયર સ્કેલ — LC 20″")},
  {"q_en":"Q.1 (c) OR Following are the bearing and length of a traverse ABCD. Find out closing error of the traverse. (07 marks)","marks_en":"07 marks","marks_gu":"૦૭ ગુણ",
   "a_en":"<p><strong>Method:</strong> Compute latitude = L·cos θ and departure = L·sin θ where θ is WCB, sum them, closing error e = √(ΣLat² + ΣDep²), relative error = e/perimeter.</p><p>AB 105.8 m 319°15′ → Lat +80.17 m Dep −69.12 m; BC 142.5 m 51°30′ → +88.64, +111.44; CD 188.8 m 131°45′ → −125.67, +140.90; DA 188.9 m 256°45′ → −43.29, −183.88. ΣLat = −0.15 m, ΣDep = −0.66 m, e = √(0.15²+0.66²) = 0.68 m, perimeter 626 m, relative 1:925, bearing of error about 257°. This is Bowditch check.</p>"+fig(svg_traverse,"Traverse ABCD with bearings and lengths — latitude and departure, closing error 0.68 m"),
   "a_gu":"<p><strong>પદ્ધતિ:</strong> લેટીટ્યુડ = L·cos θ, ડિપાર્ચર = L·sin θ, સરવાળો, e = √ΣLat²+ΣDep².</p><p>AB +80.17 −69.12, BC +88.64 +111.44, CD −125.67 +140.90, DA −43.29 −183.88, ΣLat −0.15 ΣDep −0.66, e = 0.68 m, પરિમિતિ 626 m, 1:925, એરર બેરિંગ 257°.</p>"+fig(svg_traverse,"ટ્રાવર્સ ABCD — લેટીટ્યુડ ડિપાર્ચર, ક્લોઝિંગ એરર 0.68 m")},
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
   "a_gu":"<p><strong>એનાલેટિક લેન્સ</strong> ઓબ્જેક્ટિવ અને ડાયાફ્રેમ વચ્ચે વધારાનો બહિર્ગોળ લેન્સ C = 0 અને K = 100 ચોક્કસ કરવા, D = K·S સરળ.</p><p><strong>ગેરફાયદા:</strong> પ્રકાશ 10% ઓછો, વધુ ખર્ચ, નાજુક, સફાઈ મુશ્કેલ, ચોક્કસ ગોઠવણ જોઈએ.</p>"},
  {"q_en":"Q.2 (c) To calculate the Reduced level of base of a tall chimney, the following observations were taken. The distance AB is 75 m, and station A, B and chimney are in same vertical plane. Height of chimney is 15 m. (07 marks)","marks_en":"07 marks","marks_gu":"૦૭ ગુણ",
   "a_en":"<p><strong>Given:</strong> Reading on BM at A 2.125 m angle +20°20′, at B 1.100 m angle +15°20′, RL BM 100 m, AB 75 m, chimney height 15 m. HI at A = 102.125 m, at B = 101.100 m. Let D be distance from A to foot, then A sees top under larger angle with longer D? Using same HI approx, D·tan20°20′ = (D+75)·tan15°20′ → D·0.3709 = (D+75)·0.2736 → 0.0973D = 20.52 → D = 211 m from A, height of top above HI = 211×0.3709 = 78.2 m, RL top = 180.3 m, base = top − 15 = 165.3 m. Exact value depends on HI assumption, method is D = 75·tan α2/(tan α1 − tan α2). Steps: write two h equations, equate, solve D, then RL.</p>",
   "a_gu":"<p><strong>આપેલ:</strong> A પર 2.125 m +20°20′, B પર 1.100 m +15°20′, RL BM 100 m, AB 75 m, ચીમની 15 m, HI A 102.125 m B 101.100 m. D·tan20°20′ = D+75·tan15°20′ → D = 211 m, ટોપ ઊંચાઈ 78.2 m, RL ટોપ 180.3 m, બેઝ 165.3 m. પદ્ધતિ: D = 75·tan α2/tan α1 − tan α2.</p>"},
  {"q_en":"Q.2 (c) OR The following observation were taken with a tacheometer having constant 100 and 0. Points A, B and P are in the same line. Find out the distance AB, Also find R.L. of A and B. (07 marks)","marks_en":"07 marks","marks_gu":"૦૭ ગુણ",
   "a_en":"<p><strong>At P HI 1.2 m:</strong> Sight A +5°30′ staff 1.8/2.4/3.0, RL P 50 m, sight B −7°30′ staff 1.3/2.0/2.7, K100 C0.</p><p>For A: intercept S = 1.2 m, D = 100×1.2×cos²5°30′ = 118.9 m, V = 100×1.2×sin11°/2 = +11.42 m, RL A = RL P + HI + V − staff middle 2.4 = 50+1.2+11.42−2.4 = 60.22 m.</p><p>For B: S = 1.4 m, D = 100×1.4×cos²7°30′ = 137.6 m, V = 100×1.4×sin(−15°)/2 = −18.1 m, RL B = 50+1.2−18.1−2.0 = 31.10 m. If A and B on opposite sides of P, AB = 118.9+137.6 = 256.5 m, if same side AB = 18.7 m. Method: D = K·S·cos²θ, V = K·S·sin2θ/2.</p>",
   "a_gu":"<p><strong>P HI 1.2 m:</strong> A +5°30′ S 1.2 m D 118.9 m V +11.42 m RL A = 60.22 m, B −7°30′ S 1.4 m D 137.6 m V −18.1 m RL B = 31.10 m, AB = 256.5 m વિરુદ્ધ બાજુ અથવા 18.7 m એક બાજુ. સૂત્ર D = K·S·cos²θ, V = K·S·sin2θ/2.</p>"},
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
   "a_en":"<p><strong>Components:</strong> PI intersection of tangents, PC/T1 start, PT/T2 end, R radius, Δ deflection angle, Tangent length T = R·tan(Δ/2), Curve length L = R·Δ·π/180, Long chord Lc = 2R·sin(Δ/2), External E = R·sec(Δ/2)−R, Mid ordinate M = R−R·cos(Δ/2), Apex distance, Versed sine. Three defined: T is distance PI to PC, Lc is straight chord PC−PT, M is distance from chord mid to curve.</p>"+fig(svg_elements,"Simple circular curve — PI, T1, T2, radius R, deflection Δ, tangent T, long chord Lc, external E, mid ordinate M"),
   "a_gu":"<p><strong>ઘટકો:</strong> PI ટેન્જન્ટ આંતરછેદ, PC T1 શરૂ, PT T2 અંત, R ત્રિજ્યા, Δ વિચલન, T = R·tan Δ/2, L = R·Δ·π/180, Lc = 2R·sin Δ/2, E = R·sec Δ/2−R, M = R−R·cos Δ/2, એપેક્સ, વર્સ્ડ સાઇન. ત્રણ: T PI−PC, Lc સીધો કોર્ડ, M મધ્ય ઓર્ડિનેટ.</p>"+fig(svg_elements,"સરળ ગોળાકાર વળાંક — PI, T1, T2, R, Δ, T, Lc, E, M")},
  {"q_en":"Q.3 (c) OR Two tangents intersect at a chainage of 1000 m, the intersection angle is 72˚ calculate the following for curve of radius 150 m. (07 marks)","marks_en":"07 marks","marks_gu":"૦૭ ગુણ",
   "a_en":"<p><strong>Data:</strong> PI chainage 1000 m, intersection angle 72° → deflection Δ = 72° if given as deflection, else 108° if intersection. Using Δ = 72°: T = R·tan(Δ/2) = 150·tan36° = 108.98 m, Lc = 2R·sin(Δ/2) = 176.34 m, L = R·Δ·π/180 = 188.5 m, PC = 1000−T = 891.02 m, PT = 891.02+188.5 = 1079.5 m, Apex E = R·sec(Δ/2)−R = 35.4 m, Versed sine = R·(1−cos(Δ/2)) = 28.65 m. If Δ = 108°, T = 206.5 m, Lc = 242.7 m, L = 282.7 m, PC 793.5 m, PT 1076.2 m, E 83.6 m, versed 61.8 m — state assumption.</p>",
   "a_gu":"<p><strong>ડેટા:</strong> PI 1000 m, આંતરછેદ 72° → વિચલન Δ 72° માનતા T = 108.98 m, Lc = 176.34 m, L = 188.5 m, PC 891.02 m, PT 1079.5 m, E 35.4 m, વર્સ્ડ 28.65 m. જો Δ 108° તો T 206.5 m Lc 242.7 m L 282.7 m PC 793.5 m PT 1076.2 m.</p>"},
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
   "a_en":"<p><strong>Given:</strong> Lc = 150 m, versed sine M = 2.50 m, find R from M = R − √(R²−(Lc/2)²) → 2.5 = R − √(R²−5625) → √(R²−5625) = R−2.5 → R²−5625 = R²−5R+6.25 → 5R = 5631.25 → R = 1126.25 m flat curve. Ordinate formula y = √(R²−(Lc/2−x)²) − (R−M) where R−M = 1123.75 m. For interval 10 m from T1: at 10 m x=10 y = √(1126.25²−65²)−1123.75 = 0.62 m, 20 m 1.16 m, 30 m 1.62 m, 40 m 1.99 m, 50 m 2.26 m, 60 m 2.43 m, 70 m 2.49 m, mid 75 m 2.50 m symmetric.</p>"+fig(svg_vertical,"Offsets from long chord — ordinate y = √(R²−offset²) − (R−M)"),
   "a_gu":"<p><strong>આપેલ:</strong> Lc 150 m M 2.50 m → R 1126.25 m, R−M 1123.75 m, y સૂત્ર, 10 m અંતરાલે 10 m 0.62 m, 20 m 1.16 m, 30 m 1.62 m, 40 m 1.99 m, 50 m 2.26 m, 60 m 2.43 m, 70 m 2.49 m, મધ્ય 75 m 2.50 m.</p>"+fig(svg_vertical,"લોંગ કોર્ડથી ઓર્ડિનેટ")},
  {"q_en":"Q.4 (c) OR Calculate radial offset (taken along tangents) at 45 m interval to locate a curve of radius 360 m and angle of deflection 60˚. (07 marks)","marks_en":"07 marks","marks_gu":"૦૭ ગુણ",
   "a_en":"<p><strong>Radial offsets along tangents:</strong> y = R − √(R²−x²) where x distance from PC along tangent. For R = 360 m, Δ = 60°, curve length = R·Δ·π/180 = 377 m, so 45 m interval valid up to 180 m before apex. x=45 y = 360−√(360²−45²) = 360−357.18 = 2.82 m, 90 m 11.42 m, 135 m 26.32 m, 180 m 48.13 m.</p>",
   "a_gu":"<p><strong>ટેન્જન્ટ પર રેડિયલ ઓફસેટ:</strong> y = R − √R²−x², R 360 m Δ 60° L 377 m, 45 m 2.82 m, 90 m 11.42 m, 135 m 26.32 m, 180 m 48.13 m.</p>"},
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
   "a_en":"<table><tr><th>Key</th><th>Function</th></tr><tr><td>ANG/HD</td><td>Angle / horizontal distance</td></tr><tr><td>SD/VD</td><td>Slope / vertical distance</td></tr><tr><td>COORD</td><td>Compute N,E,Z</td></tr><tr><td>S-O</td><td>Stake out</td></tr><tr><td>MLM/AREA</td><td>Missing line / area</td></tr><tr><td>MENU/ESC</td><td>Settings/back</td></tr><tr><td>STAR</td><td>EDM mode / ATR on/off</td></tr></table>"+fig(svg_total,"Total station display board — ANG, SD, COORD, S-O, MLM, MENU, STAR keys")+fig(svg_workflow,"Field to CAD workflow — total station polar to AutoCAD"),
   "a_gu":"<table><tr><th>સ્વિચ</th><th>કાર્ય</th></tr><tr><td>ANG/HD</td><td>એંગલ / હોરિઝોન્ટલ</td></tr><tr><td>SD/VD</td><td>સ્લોપ / વર્ટિકલ</td></tr><tr><td>COORD</td><td>N,E,Z</td></tr><tr><td>S-O</td><td>સ્ટેક આઉટ</td></tr><tr><td>MLM/AREA</td><td>અંતર / એરિયા</td></tr><tr><td>MENU</td><td>સેટિંગ</td></tr><tr><td>STAR</td><td>EDM / ATR</td></tr></table>"+fig(svg_total,"ટોટલ સ્ટેશન ડિસ્પ્લે — કી કાર્ય")+fig(svg_workflow,"ફિલ્ડ → CAD વર્કફ્લો")},
  {"q_en":"Q.5 (c) OR What are the latest advancement in the total station technology? Explain in detail. (07 marks)","marks_en":"07 marks","marks_gu":"૦૭ ગુણ",
   "a_en":"<p><strong>Latest:</strong> Robotic one-man with remote, reflectorless 1000 m without prism, integrated imaging and laser scanning, built-in GPS, Bluetooth to CAD, auto-leveling and auto-focusing, 3D modelling and augmented reality. Reduces crew and time, enables BIM integration and machine control.</p>",
   "a_gu":"<p><strong>નવીનતમ:</strong> રોબોટિક વન-મેન રિમોટ, રિફ્લેક્ટરલેસ 1000 m પ્રિઝમ વગર, ઇમેજિંગ અને સ્કેનિંગ, GPS, Bluetooth CAD, ઓટો-લેવલિંગ, 3D અને AR. ક્રૂ સમય ઘટે, BIM અને મશીન કંટ્રોલ શક્ય.</p>"},
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
    page=f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>DI03006021 · Summer 2026 solved paper</title><style>{CSS}</style></head><body><main class="page"><header class="hero"><div class="eyebrow">Solved question paper · English questions · Friendly Gujarati answers</div><div class="lang-switch" aria-label="Choose language"><button type="button" data-lang="en" aria-pressed="true">English</button><button type="button" data-lang="gu" aria-pressed="false">ગુજરાતી</button></div><h1>Advance Surveying</h1><div class="meta">GTU Diploma · Civil · Semester 3 · Summer 2026 · DI03006021 · 12-05-2026 · 70 marks · 02:30 PM TO 05:00 PM</div></header>{"".join(sections_html)}<div class="footer">Solved paper for study. Verify with standard spec before site use.</div></main><script>document.querySelectorAll('.lang-switch button').forEach(b=>b.addEventListener('click',()=>{{document.documentElement.lang=b.dataset.lang;document.querySelectorAll('.lang-switch button').forEach(x=>x.setAttribute('aria-pressed',x===b?'true':'false'));}}));</script></body></html>'''
    return page
def main():
    page=build_page()
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
