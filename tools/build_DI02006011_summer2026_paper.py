#!/usr/bin/env python3
from pathlib import Path
import html
ROOT=Path(__file__).resolve().parent.parent
def load_svg(name):
    p=ROOT/f"content/civil/sem2/DI02006011/diagrams/{name}"
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
svg_bearings=load_svg("sv3_bearings.svg")
svg_dumpy=load_svg("sv4_dumpy.svg")
svg_theodolite=load_svg("sv5_theodolite.svg")

SECTIONS=[
{
 "title_en":"Q1 · Principles, ranging and WCB angles",
 "title_gu":"પ્ર.1 · સિદ્ધાંત, રેન્જિંગ અને WCB ખૂણા",
 "cards":[
  {
   "q_en":"Q.1 (a) Explain Principles of surveying. (03 marks)",
   "marks_en":"03 marks","marks_gu":"૦૩ ગુણ",
   "a_en":"""<p><strong>1) Work from whole to part:</strong> First establish a master control framework with high accuracy — primary traverse or triangulation covering the whole area. Then fill interior details with lower accuracy. If error occurs in a detail, it stays local and does not distort the master. Opposite (part to whole) accumulates errors and can shift the entire survey.</p><p><strong>2) Fix every point by at least two independent measurements:</strong> A new station is located by two distances, or a distance + direction, or two angles from two known points. This gives a check — the two arcs/rays must intersect at one point. A single linear measurement leaves ambiguity.</p><p>Corollary: Provide independent checks (closing traverse, tie lines), work systematically, and choose scale/accuracy suitable for purpose.</p>""",
   "a_gu":"""<p><strong>1) આખા થી ભાગ તરફ:</strong> પહેલા આખા વિસ્તાર માટે મોટું કંટ્રોલ નેટવર્ક ચોકસાઈથી બનાવો, પછી અંદરના નાના પોઇન્ટ ઓછી ચોકસાઈથી ભરો. ભૂલ સ્થાનિક રહે, આખો નકશો બગડે નહીં.</p><p><strong>2) દરેક નવો પોઇન્ટ બે સ્વતંત્ર માપથી નક્કી:</strong> બે અંતર અથવા અંતર+દિશા અથવા બે ખૂણા — બે કમાન એક બિંદુએ મળે તો જ પોઇન્ટ સાચો. એક માપથી ચેક ન થાય.</p><p>વધુમાં ચેક લાઇન, સિસ્ટમેટિક કામ અને યોગ્ય સ્કેલ જરૂરી.</p>""",
  },
  {
   "q_en":"Q.1 (b) Explain Types of ranging in detail. (04 marks)",
   "marks_en":"04 marks","marks_gu":"૦૪ ગુણ",
   "a_en":"""<p><strong>Direct ranging — when ends intervisible:</strong> Observer behind one end rod aligns intermediate rods by eye or with a line ranger. One rod at a time is moved until its flag covers the far rod. Fastest, used on flat open ground, accuracy ~1:1000.</p><p><strong>Indirect / reciprocal ranging — when rising ground or hill blocks view:</strong> Two surveyors stand at intermediate points M and N. Each sees the other and the far end. They alternately direct each other into line until both are simultaneously on AB. Needs 4-6 iterations.</p><p><strong>Random line ranging:</strong> When a forest or building completely blocks view, run a random traverse close to the true line, offset to the blocked point and back-calculate. Slowest.</p><p>Choice depends on visibility and urgency.</p>""",
   "a_gu":"""<p><strong>Direct રેન્જિંગ:</strong> બંને છેડા દેખાય ત્યારે eye અથવા line ranger થી વચ્ચેના rod લાઇનમાં ગોઠવો. સપાટ ખુલ્લી જમીનમાં ઝડપી.</p><p><strong>Indirect / reciprocal:</strong> વચ્ચે ટેકરી હોય ત્યારે બે વ્યક્તિ M અને N પર ઊભા રહી વારાફરતી એકબીજાને direction આપી લાઇનમાં લાવે — 4-6 પ્રયાસે બંને AB પર આવે.</p><p><strong>Random line:</strong> જંગલ/મકાન આડે હોય ત્યારે નજીકની random line ચલાવી offset થી સાચી line કાઢો.</p>""",
  },
  {
   "q_en":"Q.1 (c) Explain whole circle bearing. And then calculate internal angles for following closed traverse. Apply usual check. AB 65°/245° BC 145°/325° CD 255°/75° DA 345°/165° (07 marks)",
   "marks_en":"07 marks","marks_gu":"૦૭ ગુણ",
   "a_en":f"""<p><strong>Whole Circle Bearing (WCB):</strong> Angle measured clockwise from magnetic or true north, 0° to 360°. North 0°/360°, East 90°, South 180°, West 270°. Advantage: Single value, no quadrant confusion, ideal for traverse calculation. Back bearing = FB ±180°.</p><div class="eq">Given FB and BB differ by exactly 180° for every line → no local attraction, survey is consistent.</div><p><strong>Rule for interior:</strong> At each vertex, interior = Back bearing of previous line − Fore bearing of next line. If result &gt;180°, interior = 360° − result (exterior to interior). For closed polygon sum must be (n−2)×180°.</p><table><tr><th>Station</th><th>BB of previous</th><th>FB of next</th><th>Diff</th><th>Interior</th></tr><tr><td>B (AB→BC)</td><td>245°</td><td>145°</td><td>100°</td><td><strong>100°</strong></td></tr><tr><td>C (BC→CD)</td><td>325°</td><td>255°</td><td>70°</td><td><strong>70°</strong></td></tr><tr><td>D (CD→DA)</td><td>75°</td><td>345°</td><td>−270° →360−270=90°</td><td><strong>90°</strong></td></tr><tr><td>A (DA→AB)</td><td>165°</td><td>65°</td><td>100°</td><td><strong>100°</strong></td></tr></table><div class="eq">Sum =100+70+90+100 =360° = (4−2)×180° → <strong>check satisfied, closing error 0°</strong></div><p>If sum differed, error is distributed equally to all angles.</p>"""+fig(svg_bearings,"WCB 0°–360° clockwise from north; interior = BB_prev − FB_next"),
   "a_gu":f"""<p><strong>WCB:</strong> ઉત્તરથી clockwise 0-360. ઉત્તર 0°, પૂર્વ 90°, દક્ષિણ 180°, પશ્ચિમ 270°. Back bearing = FB ±180°. સરળ, એક જ મૂલ્ય.</p><p>FB અને BB માં 180° તફાવત → local attraction નથી.</p><p><strong>આંતરિક કોણ = પાછળની રેખાનો BB − આગળની રેખાનો FB</strong>, &gt;180 હોય તો 360−diff.</p><div class="eq">B 100° C 70° D 90° A 100° સરવાળો 360° = (4−2)×180° → <strong>ચેક પાસ</strong></div>"""+fig(svg_bearings,"WCB અને આંતરિક કોણ ગણતરી"),
  },
  {
   "q_en":"Q.1 (c) OR Enlist any seven survey instruments used in chain, Tape & compass Survey with its functions. (07 marks)",
   "marks_en":"07 marks","marks_gu":"૦૭ ગુણ",
   "a_en":"""<table><tr><th>No</th><th>Instrument</th><th>Primary function</th><th>When used</th></tr><tr><td>1</td><td>Metric chain 20m/30m (150 links)</td><td>Measure horizontal distance</td><td>Main line & offsets</td></tr><tr><td>2</td><td>Steel & invar tape</td><td>Accurate distances, check chain</td><td>Precise work, uneven ground</td></tr><tr><td>3</td><td>Arrows (10 nos, 400mm)</td><td>Mark end of each chain length</td><td>Counting chains</td></tr><tr><td>4</td><td>Ranging rods 2–3m with flag</td><td>Mark stations, keep alignment</td><td>Ranging, offsets</td></tr><tr><td>5</td><td>Cross-staff / optical square</td><td>Set 90° offsets</td><td>Locate details from chain line</td></tr><tr><td>6</td><td>Prismatic compass</td><td>Measure magnetic bearing</td><td>Traverse orientation</td></tr><tr><td>7</td><td>Plumb bob + pegs + hammer</td><td>Vertical transfer & permanent mark</td><td>Slope, station fixing</td></tr><tr><td>8</td><td>Line ranger / field book</td><td>Rapid ranging & recording</td><td>Chaining party</td></tr></table><p>Chain + tape give distance, rods + cross-staff give position, compass gives direction — complete linear + angular control.</p>""",
   "a_gu":"""<p>સાંકળ/ટેપ અંતર, ranging rod alignment, cross-staff કાટખૂણો, compass દિશા, plumb bob ઢાળ પર vertical, peg station — આ સાધનોથી chain-tape-compass સર્વે પૂર્ણ.</p><table><tr><th>સાધન</th><th>કાર્ય</th></tr><tr><td>સાંકળ ટેપ</td><td>અંતર</td></tr><tr><td>Ranging rod</td><td>alignment</td></tr><tr><td>Cross-staff</td><td>90° offset</td></tr><tr><td>Compass</td><td>bearing</td></tr><tr><td>Plumb bob peg</td><td>vertical & mark</td></tr></table>""",
  },
 ]
},
{
 "title_en":"Q2 · Compass, plane table and levelling",
 "title_gu":"પ્ર.2 · કંપાસ, પ્લેન ટેબલ અને લેવલિંગ",
 "cards":[
  {
   "q_en":"Q.2 (a) Differentiate between prismatic compass and surveyor compass. (03 marks)",
   "marks_en":"03 marks","marks_gu":"૦૩ ગુણ",
   "a_en":"""<table><tr><th>Point</th><th>Prismatic compass</th><th>Surveyor compass</th></tr><tr><td>Graduation type</td><td>0°–360° WCB printed on aluminium ring that moves with magnetic needle</td><td>0°–90° quadrantal (QB) printed fixed on box</td></tr><tr><td>Reading position</td><td>Prism magnifies and reads while sighting — one observer, no parallax</td><td>Lift eye to read on top after sighting — two steps</td></tr><tr><td>Needle</td><td>Broad needle carries the ring, pivoted on agate</td><td>Edge-bar needle moves over fixed scale</td></tr><tr><td>Sighting</td><td>Object vane + eye vane with prism, fine wire</td><td>Slit + hair, open sight</td></tr><tr><td>Tripod</td><td>Small, usually on tripod with ball-socket levelling</td><td>Larger, on stand with levelling screws</td></tr><tr><td>Accuracy & use</td><td>~30' least count, routine traverse</td><td>~15' with vernier, old cadastral</td></tr></table><p>Today prismatic is standard for compass traverse; surveyor is largely obsolete.</p>""",
   "a_gu":"""<p><strong>Prismatic:</strong> 0-360° ring સોય સાથે ફરે, prism થી જોતાં જ વંચાય, નાની tripod.</p><p><strong>Surveyor:</strong> 0-90° QB fixed scale, sight પછી ઉપરથી વાંચો, મોટી, જૂની. Prismatic હવે standard.</p><table><tr><th>મુદ્દો</th><th>Prismatic</th><th>Surveyor</th></tr><tr><td>Graduation</td><td>0-360 WCB</td><td>0-90 QB</td></tr><tr><td>વાંચન</td><td>prism સાથે</td><td>પછી ઉપરથી</td></tr></table>""",
  },
  {
   "q_en":"Q.2 (b) State methods of Plane Tabling and explain any one in detail. (04 marks)",
   "marks_en":"04 marks","marks_gu":"૦૪ ગુણ",
   "a_en":"""<p><strong>Four methods:</strong> (i) Radiation (ii) Intersection (iii) Traversing (iv) Resection.</p><p><strong>Radiation — detailed steps for 4 marks:</strong> 1) Choose a central station O that sees all details. 2) Set plane table over O, centre with plumb fork, level with spirit level, orient with trough compass to north. 3) Pin paper, mark O, sight each detail point A,B,C with alidade touching O, draw rays OA, OB... 4) Measure ground distance OA with chain/tape, scale it on the ray (e.g., 1cm=2m), prick point a. Repeat for all. 5) Join detail points for outline. Ideal for small open plot, one setup covers all, quick but error radiates from one point so orientation must be precise.</p><p>Intersection needs two stations, traversing links many stations, resection locates the table itself.</p>""",
   "a_gu":"""<p><strong>ચાર પદ્ધતિ:</strong> Radiation, Intersection, Traversing, Resection.</p><p><strong>Radiation વિગત:</strong> મધ્યમાં O પસંદ કરો, table centre-level-orient, alidade થી દરેક detail તરફ કિરણ દોરો, chain થી અંતર માપી scale થી point મૂકો — નાના પ્લોટ માટે એક setup માં ઝડપી, પણ orientation ચોક્કસ.</p>""",
  },
  {
   "q_en":"Q.2 (c) Explain Temporary adjustment of Prismatic compass. (07 marks)",
   "marks_en":"07 marks","marks_gu":"૦૭ ગુણ",
   "a_en":"""<ol><li><strong>Fixing to tripod:</strong> Screw compass box to tripod head firmly. Tripod legs spread ~60°, shoes firmly pressed. Height chest level.</li><li><strong>Centering over station:</strong> Drop plumb bob from box centre to peg. Shift tripod bodily until bob is exact. For precise work use plumb fork.</li><li><strong>Levelling — bring bubble central:</strong> Ball-and-socket joint is loosened, box tilted until circular bubble is centre. This lets graduated ring swing freely without touching glass — otherwise friction causes 1°–2° error.</li><li><strong>Focussing the prism:</strong> Slide prism up/down until graduations appear sharp and vertical. Clean lens, adjust for eye.</li><li><strong>Checking freedom of needle:</strong> Lift brake pin, needle should swing freely and settle. If sluggish, magnetize or clean pivot.</li><li><strong>Taking bearing:</strong> Release brake, sight through eye slit to object vane wire, read graduation under prism at the same instant. Record FB from A→B, shift to B read BB (should be FB±180°). If not, local attraction present.</li></ol><p>All four adjustments must be repeated at every station; levelling is most critical.</p>""",
   "a_gu":"""<p><strong>Temporary adjustment:</strong> 1) Tripod પર fix. 2) Plumb bob થી centering. 3) Bubble centre કરી levelling — ring free ફરે. 4) Prism focus સાફ દેખાય. 5) Brake છોડી સોય free ફરે છે કે check. પછી eye slit થી sight કરી prism નીચે bearing વાંચો — FB અને BB 180° તફાવત check.</p>""",
  },
  {
   "q_en":"Q.2 (a) OR Define (i) Contour (ii) Fore sight (iii) Axis of telescope (03 marks)",
   "marks_en":"03 marks","marks_gu":"૦૩ ગુણ",
   "a_en":"""<p><strong>(i) Contour:</strong> An imaginary line on ground joining points of equal elevation above datum (mean sea level). In plan it is horizontal section of terrain at a fixed RL — e.g., 102.0m contour. Spacing indicates steepness.</p><p><strong>(ii) Fore Sight (FS):</strong> The staff reading taken on the last point observed from a level setup, just before the instrument is shifted. It indicates the point being left. In calculations FS is subtracted from Height of Instrument.</p><p><strong>(iii) Axis of telescope (Line of collimation):</strong> The optical axis — line joining the optical centre of objective lens and the intersection of horizontal + vertical cross-hairs. It must be horizontal when bubble is centre; its collimation error is checked by two-peg test.</p>""",
   "a_gu":"""<p><strong>Contour:</strong> સરખા RL ને જોડતી કાલ્પનિક રેખા — datum થી સમાન ઊંચાઈ. </p><p><strong>Fore Sight:</strong> setup બદલતા પહેલા છેલ્લું staff વાંચન — શિફ્ટ પહેલા point.</p><p><strong>Telescope axis:</strong> objective કેન્દ્ર અને cross-hair intersection ને જોડતી રેખા — collimation line.</p>""",
  },
  {
   "q_en":"Q.2 (b) OR Explain characteristics of contours. (04 marks)",
   "marks_en":"04 marks","marks_gu":"૦૪ ગુણ",
   "a_en":"""<ul><li><strong>Never cross, except</strong> overhanging cliff / cave where two elevations occupy same plan position. Otherwise contours are nested.</li><li><strong>Closeness = steepness:</strong> Closely spaced → steep slope (e.g., 1m interval at 2mm plan = 1:50 slope). Widely spaced → flat/gentle.</li><li><strong>Perpendicular to steepest slope:</strong> Water flows at right angle to contour. Ridge lines are convex outward, valley lines concave.</li><li><strong>Closed loops:</strong> Hill — values increase inwards; pond — values decrease inwards. A loop never ends inside the sheet.</li><li><strong>Equal interval in vertical, not horizontal:</strong> Contour interval (e.g., 1m) is constant; horizontal equivalent varies with slope.</li></ul>""",
   "a_gu":"""<p>1) cliff સિવાય ક્યારેય cross નહીં. 2) નજીક = steep, દૂર = flat. 3) steepest slope ને લંબ, પાણી contour ને કાટખૂણે વહે. 4) બંધ loop — ટેકરી અંદર વધે, તળાવમાં ઘટે. 5) vertical interval fixed, horizontal બદલે.</p>""",
  },
  {
   "q_en":"Q.2 (c) OR The following readings were taken with dumpy level: 1.155, 1.565, 2.695, 3.580, 2.085, 2.895, 4.125. Level shifted after 4th reading. Calculate RL by Rise and Fall. Assume BM 100.00 (07 marks)",
   "marks_en":"07 marks","marks_gu":"૦૭ ગુણ",
   "a_en":"""<p><strong>Identify setup:</strong> Setup-1: BS 1.155 (on BM), IS 1.565, IS 2.695, FS 3.580 on Change Point CP. Setup-2: BS 2.085 on same CP, IS 2.895, FS 4.125. CP has two readings (FS of old, BS of new) but one RL.</p><table><tr><th>Station</th><th>BS</th><th>IS</th><th>FS</th><th>HI</th><th>RL</th><th>Remarks / Rise-Fall</th></tr><tr><td>BM</td><td>1.155</td><td></td><td></td><td>101.155</td><td><strong>100.000</strong></td><td>BM known</td></tr><tr><td>1</td><td></td><td>1.565</td><td></td><td></td><td>99.590</td><td>Fall 0.410 (1.565&gt;1.155)</td></tr><tr><td>2</td><td></td><td>2.695</td><td></td><td></td><td>98.460</td><td>Fall 1.130</td></tr><tr><td>CP</td><td>2.085</td><td></td><td>3.580</td><td>99.660</td><td>97.575</td><td>Fall 0.885</td></tr><tr><td>3</td><td></td><td>2.895</td><td></td><td></td><td>96.765</td><td>Fall 0.810 (2.895&gt;2.085)</td></tr><tr><td>4</td><td></td><td></td><td>4.125</td><td></td><td>95.535</td><td>Fall 1.230</td></tr></table><p><strong>Calculation:</strong> RL = HI − staff, HI = RL_prev + BS. Rise = previous staff − current if negative = fall.</p><div class="eq">Arithmetic check: ΣBS =1.155+2.085=3.240, ΣFS =3.580+4.125=7.705, ΣBS−ΣFS =−4.465 = Last RL − First RL (95.535−100.00) ✓</div><p>Also ΣFall =0.410+1.130+0.885+0.810+1.230=4.465 = ΣBS−ΣFS magnitude.</p>""",
   "a_gu":"""<p><strong>Setup-1 BS 1.155 FS 3.580, Setup-2 BS 2.085 FS 4.125, CP same point.</strong> BM 100 થી HI 101.155, 1.565→99.59 fall 0.41, 2.695→98.46 fall1.13, 3.580→97.575 fall0.885, 2.895→96.765 fall0.81, 4.125→95.535 fall1.23.</p><div class="eq">ΣBS 3.24 ΣFS 7.705 તફાવત −4.465 = છેલ્લા−પ્રથમ RL ✓</div>""",
  },
 ]
},
{
 "title_en":"Q3 · Plan map, bearings and compass errors",
 "title_gu":"પ્ર.3 · પ્લાન નકશો, બેરિંગ અને ભૂલ",
 "cards":[
  {
   "q_en":"Q.3 (a) Differentiate between Plan and Map. (03 marks)",
   "marks_en":"03 marks","marks_gu":"૦૩ ગુણ",
   "a_en":"""<table><tr><th>Aspect</th><th>Plan</th><th>Map</th></tr><tr><td>Scale</td><td>Large 1:100 to 1:5000 (e.g., building plan 1:100)</td><td>Small 1:50,000 to 1:10,00,000</td></tr><tr><td>Area covered</td><td>Small (plot, colony) — curvature of earth ignored</td><td>Large (taluka/district) — curvature considered, projection used</td></tr><tr><td>Detail</td><td>Shows engineering details — walls, invert levels, offsets</td><td>Shows topography — contours, rivers, boundaries</td></tr><tr><td>Use</td><td>Execution, estimation, layout</td><td>Planning, navigation, GIS</td></tr></table><p>Every plan is a map, but not vice versa.</p>""",
   "a_gu":"""<table><tr><th>Plan</th><th>Map</th></tr><tr><td>મોટો scale 1:100-5000, નાનો વિસ્તાર, curvature ignore, execution માટે</td><td>નાનો scale 1:50000+, મોટો વિસ્તાર, curvature consider, planning માટે</td></tr></table>""",
  },
  {
   "q_en":"Q.3 (b) Convert following WCB into RB and RB into WCB (i)288° (ii)165°30' (iii)N58°30'E (iv)S72°W (04 marks)",
   "marks_en":"04 marks","marks_gu":"૦૪ ગુણ",
   "a_en":f"""<p><strong>Rule:</strong> I quadrant (0–90°) WCB = RB NθE, II (90–180°) RB =180°−WCB S(θ)E, III (180–270°) S(θ)W, IV (270–360°) N(θ)W.</p><table><tr><th>Given</th><th>Type</th><th>Step</th><th>Answer</th></tr><tr><td>288° WCB</td><td>WCB→RB (IV)</td><td>360−288=72°</td><td><strong>N72°00'W</strong></td></tr><tr><td>165°30' WCB</td><td>WCB→RB (II)</td><td>180−165°30=14°30'</td><td><strong>S14°30'E</strong></td></tr><tr><td>N58°30'E</td><td>RB→WCB (I)</td><td>Same as RB</td><td><strong>58°30'</strong></td></tr><tr><td>S72°W</td><td>RB→WCB (III)</td><td>180+72</td><td><strong>252°00'</strong></td></tr></table><p>For FB→BB simply ±180°.</p>"""+fig(svg_bearings,"WCB ↔ RB conversion quadrants"),
   "a_gu":f"""<p>Rule: I NθE =WCB, II 180−WCB, III 180+θ, IV 360−θ.</p><p>288°→N72°W, 165°30'→S14°30'E, N58°30'E→58°30', S72°W→252°.</p>"""+fig(svg_bearings,"રૂપાંતર"),
  },
  {
   "q_en":"Q.3 (c) Explain errors in the compass survey and describe the closing error. (07 marks)",
   "marks_en":"07 marks","marks_gu":"૦૭ ગુણ",
   "a_en":"""<p><strong>A) Instrumental errors:</strong> Pivot friction, bent needle, worn agate, eccentricity of graduations, prism misalignment. Remedy: Service, test on known bearing.</p><p><strong>B) Personal errors:</strong> Inaccurate centering (1cm shift =0.5° in 10m), poor levelling (graduation touches glass), parallax in prism, reading without steady needle. Use plumb, level carefully.</p><p><strong>C) Natural errors:</strong> Local attraction from iron pipes, fences, DC lines; diurnal magnetic variation (~10' per day), magnetic storms, declination not corrected. Avoid by stepping away from steel, apply declination.</p><p><strong>Closing error:</strong> For closed traverse, sum of latitudes ΣL·cosθ and departures ΣL·sinθ should be zero. Practical sum is e = √(ΣLat²+ΣDep²) — the gap between start and end. Expressed as 1 in (Perimeter/e). Bowditch rule distributes correction ∝ length: CorrLat = −e_lat·(l/Σl); Transit rule ∝ |Lat| for angular dominance. If e within 1:500–1:1000 acceptable.</p>""",
   "a_gu":"""<p><strong>યંત્ર ભૂલ:</strong> pivot ઘર્ષણ, scale eccentricity. <strong>વ્યક્તિ:</strong> centering/levelling ખોટું. <strong>Natural:</strong> local attraction લોખંડ, diurnal variation. <strong>Closing error:</strong> બંધ traverse માં ΣLat ΣDep શૂન્ય હોવા જોઈએ, અંતર e=√(ΣLat²+ΣDep²), Bowditch થી length પ્રમાણે સુધારો.</p>""",
  },
  {
   "q_en":"Q.3 (a) OR Explain the classifications of the Theodolite (03 marks)",
   "marks_en":"03 marks","marks_gu":"૦૩ ગુણ",
   "a_en":"""<p><strong>By transit:</strong> Transit (telescope can be transited 180° vertical) vs non-transit (Y theodolite).</p><p><strong>By reading:</strong> Vernier (20'' LC) vs micrometer optical (1'') vs electronic digital (1'').</p><p><strong>By use:</strong> Primary/precise (0.1'') for triangulation, secondary (10–20'') for traverse.</p><p>Modern total stations are electronic transit theodolites with EDM.</p>""",
   "a_gu":"""<p>Transit vs non-transit, vernier vs electronic, primary precise vs secondary traverse — total station એ electronic transit.</p>""",
  },
  {
   "q_en":"Q.3 (b) OR Enlist instruments used for setting out right angles. explain each in details. (04 marks)",
   "marks_en":"04 marks","marks_gu":"૦૪ ગુણ",
   "a_en":"""<p><strong>1) Open cross-staff:</strong> Octagonal box with 4 slits at 90°, sight through one, second line perpendicular. Simple, ~0.5° accuracy.</p><p><strong>2) French cross-staff:</strong> Adds 45° slits for 45° offset.</p><p><strong>3) Optical square:</strong> Two mirrors at 45° reflect ray by 90° — observer sees direct and reflected images coincide when perpendicular.</p><p><strong>4) Prism square:</strong> Uses pentaprism, more accurate, no parallax.</p><p><strong>5) Site square / theodolite:</strong> Most accurate for long offsets, set 90° on horizontal circle.</p>""",
   "a_gu":"""<p>Open cross-staff 4 slit 90°, optical square 45° mirror થી 90°, prism square, theodolite સૌથી ચોક્કસ.</p>""",
  },
  {
   "q_en":"Q.3 (c) OR Draw a neat sketch of dumpy level and label its all parts. (07 marks)",
   "marks_en":"07 marks","marks_gu":"૦૭ ગુણ",
   "a_en":f"""<p><strong>Parts (label in sketch):</strong> (1) Telescope (objective, eyepiece, focussing screw, diaphragm with cross-hairs) (2) Levelling head with 3 foot screws + tribrach (3) Longitudinal bubble + cross bubble (4) Compass trough (5) Ray shade (6) Tripod.</p><p><strong>Function:</strong> Foot screws bring bubble centre → line of collimation horizontal → staff reading gives RL via HI = RL_known + BS.</p><p><strong>Precautions:</strong> Protect from sun, handle gently, check two-peg test weekly.</p>"""+fig(svg_dumpy,"Dumpy level — telescope, foot screws, bubble, tripod"),
   "a_gu":f"""<p>Telescope, 3 foot screws, bubble, compass, tripod — bubble centre કરો તો line horizontal, RL = HI − staff.</p>"""+fig(svg_dumpy,"ડમ્પી લેવલ"),
  },
 ]
},
{
 "title_en":"Q4 · Theodolite, axis and sketches",
 "title_gu":"પ્ર.4 · થિયોડોલાઇટ, અક્ષ અને આકૃતિ",
 "cards":[
  {
   "q_en":"Q.4 (a) Write uses of Theodolite. (03 marks)",
   "marks_en":"03 marks","marks_gu":"૦૩ ગુણ",
   "a_en":"""<ul><li>Measure horizontal angles for traverse, bearing, prolong line.</li><li>Measure vertical angles for height, gradient, trigonometric levelling.</li><li>Set right angles, offsets, curves, columns verticality, tunnel alignment.</li><li>Tacheometry: distance + RL without chain.</li></ul><p>One instrument replaces chain, compass and level for detailed work.</p>""",
   "a_gu":"""<p>આડા ખૂણા traverse, ઊભા ખૂણા height, કાટખૂણો, વળાંક, tacheometry — એક યંત્ર ઘણાં કામ.</p>""",
  },
  {
   "q_en":"Q.4 (b) List the fundamental axis of theodolite & give relation between them. (04 marks)",
   "marks_en":"04 marks","marks_gu":"૦૪ ગુણ",
   "a_en":"""<p><strong>Five axes:</strong> 1) Vertical (azimuth) axis 2) Horizontal (trunnion) axis 3) Line of collimation (sight) axis 4) Plate level axis 5) Altitude bubble/stadia axis.</p><p><strong>Relations for a perfect instrument (permanent adjustment):</strong> (i) Plate level axis ⊥ vertical axis (so when bubble centre, vertical is true vertical). (ii) Line of collimation ⊥ horizontal axis. (iii) Horizontal axis ⊥ vertical axis. (iv) When all satisfied, line of collimation sweeps a vertical plane when telescope is transited. Two-peg and spire tests verify.</p>""",
   "a_gu":"""<p>પાંચ અક્ષ: vertical, horizontal, collimation, plate level, altitude bubble. Relation: plate ⊥ vertical, collimation ⊥ horizontal, horizontal ⊥ vertical — તો collimation vertical plane માં ફરે.</p>""",
  },
  {
   "q_en":"Q.4 (c) Draw a neat sketch of Theodolite and label its all parts. (07 marks)",
   "marks_en":"07 marks","marks_gu":"૦૭ ગુણ",
   "a_en":f"""<p><strong>Parts to label:</strong> Telescope (objective, eyepiece, focusing screw), Vertical circle with vernier/micrometer, Horizontal circle (main + vernier), Upper & lower plates with clamps & tangents, Levelling head + foot screws, Standards (A-frame), Plumb bob, Tripod.</p><p><strong>Operation:</strong> Upper plate for fine angle, lower for orientation, transiting for face left/right.</p>"""+fig(svg_theodolite,"Transit theodolite — telescope, vertical/horizontal circles, plates, foot screws"),
   "a_gu":f"""<p>Telescope, vertical/horizontal circle, upper-lower plates, foot screws, plumb — face left/right.</p>"""+fig(svg_theodolite,"થિયોડોલાઇટ"),
  },
  {
   "q_en":"Q.4 (a) OR Define (i) Face right (ii) Vertical axis (iii) Swinging (03 marks)",
   "marks_en":"03 marks","marks_gu":"૦૩ ગુણ",
   "a_en":"""<p><strong>(i) Face right:</strong> When vertical circle is on observer's right while sighting. Face right and face left readings differ by 180°; mean eliminates collimation error.</p><p><strong>(ii) Vertical (azimuth) axis:</strong> The axis about which the whole instrument rotates in horizontal plane. Must be truly vertical after levelling.</p><p><strong>(iii) Swinging (or swivelling):</strong> Rotating telescope about vertical axis in horizontal plane — e.g., swinging from backsight to foresight to measure angle.</p>""",
   "a_gu":"""<p><strong>Face right:</strong> circle જમણે. <strong>Vertical axis:</strong> આડા plane માં ફરવાનો ઊભો અક્ષ. <strong>Swinging:</strong> horizontal plane માં telescope ફેરવવું.</p>""",
  },
  {
   "q_en":"Q.4 (b) OR Differentiate between Rise & Fall method and H.I. Method (04 marks)",
   "marks_en":"04 marks","marks_gu":"૦૪ ગુણ",
   "a_en":"""<table><tr><th>Aspect</th><th>Rise & Fall</th><th>Height of Instrument (HI)</th></tr><tr><td>Principle</td><td>Successive staff difference: rise if second reading smaller (ground higher)</td><td>HI = RL + BS for each setup; next RL = HI − IS/FS</td></tr><tr><td>Check</td><td>ΣRise − ΣFall = Last RL − First RL = ΣBS − ΣFS</td><td>ΣBS − ΣFS = Last − First (same)</td></tr><tr><td>Error visibility</td><td>Every point error visible immediately</td><td>Mid-setup error hidden until check</td></tr><tr><td>Speed</td><td>Slower, more calculations</td><td>Faster, fewer columns</td></tr><tr><td>Use</td><td>Precise levelling, teaching</td><td>Routine fly levelling</td></tr></table><p>Both give same RLs; Rise/Fall is preferred for check.</p>""",
   "a_gu":"""<p><strong>Rise-Fall:</strong> ક્રમિક તફાવત rise/fall, દરેક point ભૂલ દેખાય. <strong>HI:</strong> દરેક setup HI કાઢી minus — ઝડપી. બંને check સરખા.</p>""",
  },
  {
   "q_en":"Q.4 (c) OR Write Advantages and Disadvantages of Plain Table Survey. (07 marks)",
   "marks_en":"07 marks","marks_gu":"૦૭ ગુણ",
   "a_en":"""<p><strong>Advantages (4–5 points for 3.5 marks):</strong> 1) Field is also office — no transcription error. 2) Omitted details seen on ground immediately. 3) No need for skilled chain/compass party — one table operator. 4) Cheapest for small fill-in, contour interpolation directly. 5) Suitable for magnetically disturbed areas (no compass needed if oriented by backsight).</p><p><strong>Disadvantages:</strong> 1) Not usable in rain/wind — paper spoils. 2) Not for precise large surveys — alidade accuracy ~1:1000. 3) Replotting difficult if sheet damaged. 4) Heavy board + tripod to carry. 5) Requires calm, skilled orienting each setup.</p>""",
   "a_gu":"""<p><strong>ફાયદા:</strong> field જ office — ભૂલ ઓછી, છૂટી વિગત દેખાય, સસ્તું, magnetic disturbance માં ચાલે.</p><p><strong>ગેરફાયદા:</strong> વરસાદ/પવનમાં નહીં, precise નહીં, sheet બગડે તો replotting અઘરું, ભારે.</p>""",
  },
 ]
},
{
 "title_en":"Q5 · Orientation, adjustment and contouring",
 "title_gu":"પ્ર.5 · દિકસ્થાપન, સમાયોજન અને contour",
 "cards":[
  {
   "q_en":"Q.5 (a) Explain the Orientation in Plain Table Survey (03 marks)",
   "marks_en":"03 marks","marks_gu":"૦૩ ગુણ",
   "a_en":"""<p><strong>Orientation = keeping table at every station parallel to its position at first station.</strong> Then plotted rays remain parallel to ground lines. Without it, traversing will not close.</p><p><strong>Three ways:</strong> (i) Magnetic compass — align trough compass north to sheet north. Quick but affected by local attraction. (ii) Backsighting — alidade on previous line drawn on sheet, sight back to previous station and rotate table till exact. Most accurate. (iii) Resection — after two known points plotted, table oriented by intersecting. Always orient before taking new rays.</p>""",
   "a_gu":"""<p><strong>Orientation:</strong> દરેક station પર ટેબલ પહેલાની જેમ સમાંતર રાખવું — નહિ તો traverse બંધ ન થાય. Compass થી અથવા back-sight થી (પાછળની રેખા પર alidade મૂકી પાછળ sight કરી table ફેરવો) — back-sight સૌથી ચોક્કસ.</p>""",
  },
  {
   "q_en":"Q.5 (b) Explain temporary adjustment of Theodolite. (04 marks)",
   "marks_en":"04 marks","marks_gu":"૦૪ ગુણ",
   "a_en":"""<p><strong>1) Setting up & centering:</strong> Tripod over peg, plumb bob exact, legs firm.</p><p><strong>2) Levelling:</strong> Turn plate until plate bubble parallel to two foot screws — turn them opposite equally until bubble centre; turn 90° and use third screw. Repeat until bubble centre in all positions → vertical axis vertical.</p><p><strong>3) Focussing eyepiece:</strong> Turn eyepiece until cross-hairs sharp (no parallax).</p><p><strong>4) Focussing objective:</strong> Direct to staff, turn focusing screw until image sharp and cross-hairs do not move when eye moves. Ready for angle measurement.</p>""",
   "a_gu":"""<p>1) Plumb થી centering. 2) Plate bubble બે screw વિરુદ્ધ ફેરવી centre, 90° ફેરવી ત્રીજો screw. 3) Eyepiece focus cross-hair sharp. 4) Objective focus — parallax નહીં.</p>""",
  },
  {
   "q_en":"Q.5 (c) Explain the methods of locating contour lines in surveying. (07 marks)",
   "marks_en":"07 marks","marks_gu":"૦૭ ગુણ",
   "a_en":"""<p><strong>Direct method:</strong> Find and peg points of a required RL with level — radiate from a setup, staff-man moves until reading = HI − required RL. Trace closed loop. Accurate but slow, used for small areas, highways.</p><p><strong>Indirect methods:</strong></p><ul><li><strong>Grid (squares) method:</strong> Divide area into 10×10m squares, take RL of each grid corner with level, interpolate contour between corners. Best for flat civil sites.</li><li><strong>Cross-section method:</strong> Run centre line, take levels at regular intervals and perpendicular offsets — ideal for roads/canals.</li><li><strong>Tacheometric method:</strong> Use tacheometer to get distance + RL rapidly for hilly large areas.</li></ul><p><strong>Interpolation:</strong> Arithmetic (proportional calculation), graphical (trace paper), or estimation between spot heights to draw contour.</p>""",
   "a_gu":"""<p><strong>Direct:</strong> જરૂરી RL ના points level થી શોધી trace — slow. </p><p><strong>Indirect:</strong> Grid 10×10m દરેક corner RL લઈ interpolate; Cross-section રસ્તા માટે; Tacheometric ડુંગરમાં ઝડપી. Arithmetic/graphical થી contour દોરો.</p>""",
  },
  {
   "q_en":"Q.5 (a) OR What are the objectives and uses of surveying? (03 marks)",
   "marks_en":"03 marks","marks_gu":"૦૩ ગુણ",
   "a_en":"""<p><strong>Objectives:</strong> (i) Determine relative positions of points on/above/below earth surface (distance, direction, elevation). (ii) Prepare plans/maps to scale. (iii) Compute areas, volumes, set out works.</p><p><strong>Uses:</strong> Design roads, railways, dams, tunnels; fix property boundaries; estimate earthwork; prepare GIS, town planning, navigation charts.</p>""",
   "a_gu":"""<p><strong>ઉદ્દેશ:</strong> બિંદુઓની સાપેક્ષ સ્થિતિ નક્કી, નકશો બનાવવો, area/volume કાઢવા.</p><p><strong>ઉપયોગ:</strong> રસ્તા ડેમ ટનલ design, હદ નક્કી, earthwork estimate, town planning.</p>""",
  },
  {
   "q_en":"Q.5 (b) OR Explain: Bowditch rule and Transit rule. (04 marks)",
   "marks_en":"04 marks","marks_gu":"૦૪ ગુણ",
   "a_en":"""<p><strong>Bowditch (compass) rule — assumes errors proportional to length:</strong> Correction in latitude = −(ΣLat error) × (length of line / perimeter). Same for departure. Used when linear and angular errors both present (most compass traverses). Also called compass rule.</p><p><strong>Transit rule — assumes angular error dominates:</strong> Correction in latitude = −(ΣLat error) × (|Latitude| / Σ|Latitude|). Gives more correction to lines with larger latitude. Used for theodolite traverses where angles are precise. Bowditch is more popular.</p><p>After correction, ΣLat =0 and ΣDep =0, traverse closes.</p>""",
   "a_gu":"""<p><strong>Bowditch:</strong> સુધારો length પ્રમાણે — Corr = −error × l/Σl. Compass traverse માટે.</p><p><strong>Transit:</strong> સુધારો |Lat| પ્રમાણે — angular error વધારે હોય ત્યારે theodolite માટે.</p>""",
  },
  {
   "q_en":"Q.5 (c) OR Enlist any Seven equipment and accessories used in Plain Table Survey with its uses. (07 marks)",
   "marks_en":"07 marks","marks_gu":"૦૭ ગુણ",
   "a_en":"""<table><tr><th>Item</th><th>Use in plain table</th></tr><tr><td>1. Plane table board (600×750mm) with tripod</td><td>Drawing surface, can be levelled and oriented</td></tr><tr><td>2. Alidade (plain or telescopic)</td><td>Sight details and draw rays</td></tr><tr><td>3. Spirit level</td><td>Check table is horizontal</td></tr><tr><td>4. Trough compass</td><td>Mark magnetic north, orient table</td></tr><tr><td>5. U-fork with plumb bob</td><td>Centre table exactly over ground peg</td></tr><tr><td>6. Chain / tape / tape + arrows</td><td>Measure distances to plot to scale</td></tr><tr><td>7. Drawing paper, pins, clips, pencil, eraser</td><td>Plot, fix paper, draw</td></tr><tr><td>8. Spirit level for alidade</td><td>Check sights are horizontal when needed</td></tr></table><p>All must be carried together; forgetting plumb fork or compass makes orientation impossible.</p>""",
   "a_gu":"""<p>Board+tripod, Alidade ray દોરે, Spirit level આડું, Trough compass north, U-fork plumb centre, Chain અંતર, paper/pin — આ વગર orientation અશક્ય.</p>""",
  },
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
    page=f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>DI02006011 · Summer 2026 solved paper</title><style>{CSS}</style></head><body><main class="page"><header class="hero"><div class="eyebrow">Solved question paper · English questions · Friendly Gujarati answers</div><div class="lang-switch" aria-label="Choose language"><button type="button" data-lang="en" aria-pressed="true">English</button><button type="button" data-lang="gu" aria-pressed="false">ગુજરાતી</button></div><h1>Basic Surveying</h1><div class="meta">GTU Diploma · Civil · Semester 2 · Summer 2026 · DI02006011 · 02-07-2026 · 70 marks · 10:30 AM TO 01:00 PM</div></header>{"".join(sections_html)}<div class="footer">Solved paper for study. Verify with field book before site use.</div></main><script>document.querySelectorAll('.lang-switch button').forEach(b=>b.addEventListener('click',()=>{{document.documentElement.lang=b.dataset.lang;document.querySelectorAll('.lang-switch button').forEach(x=>x.setAttribute('aria-pressed',x===b?'true':'false'));}}));</script></body></html>'''
    return page
def main():
    page=build_page()
    out_papers=ROOT/"papers-upload/papers/DI02006011/summer-2026.html"
    out_ws=ROOT/"preview/workshop/DI02006011_summer2026_bilingual.html"
    out_papers.parent.mkdir(parents=True,exist_ok=True); out_ws.parent.mkdir(parents=True,exist_ok=True)
    out_papers.write_text(page,encoding="utf-8"); out_ws.write_text(page,encoding="utf-8")
    print(f"Bilingual: {out_papers} ({len(page)} chars)")
    en_c=page.count('class="en"'); gu_c=page.count('class="gu"')
    print(f"details={page.count('<details')}, sections={page.count('<section')}, en={en_c}, gu={gu_c}")
    print("PASS" if page.count('<details')==28 and page.count('<section')==5 else "FAIL", f"figs={page.count('<figure>')}")
    import re; pat=r'<div class="gu">(.*?)</div>'; gu_text=''.join(re.findall(pat,page,re.S)); print(f"brackets gu={gu_text.count('(')+gu_text.count(')')}")
    (ROOT/"drive-upload/DI02006011_summer_2026_bilingual.html").write_text(page,encoding="utf-8")
if __name__=="__main__": main()
