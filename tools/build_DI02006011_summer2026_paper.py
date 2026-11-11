#!/usr/bin/env python3
from pathlib import Path
import html
ROOT=Path(__file__).resolve().parent.parent
def load_svg(name):
    p=ROOT/f"content/civil/sem2/DI02006011/diagrams/{name}"
    if p.exists():
        txt=p.read_text(encoding="utf-8")
        # strip xml declaration if any
        return txt
    return ""
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
.result{display:table;background:#f1fbf6;border:1px solid #77a795;border-radius:7px;padding:7px 11px;margin:10px 0}
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
@media(max-width:600px){.page{width:calc(100% - 20px);margin-top:10px}.hero{padding:19px}.answer{padding:14px}.card summary strong{min-width:160px}}
"""
def fig(svg_text,caption):
    return f'<figure>{svg_text}<figcaption>{html.escape(caption)}</figcaption></figure>'

# Load SVGs
svg_principles=load_svg("sv1_principles.svg")
svg_bearings=load_svg("sv3_bearings.svg")
svg_compass=load_svg("sv3_compass.svg")
svg_ptable=load_svg("sv3_ptable.svg")
svg_dumpy=load_svg("sv4_dumpy.svg")
svg_contour=load_svg("sv4_contour.svg")
svg_terms=load_svg("sv4_terms.svg")
svg_theodolite=load_svg("sv5_theodolite.svg")
svg_adjust=load_svg("sv5_adjust.svg")
svg_closing=load_svg("sv3_closing.svg")
svg_chain=load_svg("sv2_chain.svg")
svg_interp=load_svg("sv4_interp.svg")

SECTIONS=[
{
 "title_en":"Q1 · Principles, ranging and WCB angles",
 "title_gu":"પ્ર.1 · સિદ્ધાંત, રેન્જિંગ અને WCB ખૂણા",
 "cards":[
  {
   "q_en":"Q.1 (a) Explain Principles of surveying. (03 marks)",
   "marks_en":"03 marks","marks_gu":"૦૩ ગુણ",
   "a_en":f"<p><strong>Whole to part:</strong> Establish major control triangle / traverse first, minor detail inside. Errors stay local, never accumulate.</p><p><strong>Fix by two independent references:</strong> Every new point located from two known points — intersection of distance or direction — so check possible.</p><p>Other corollaries: work from firm datum, provide independent checks, economy of accuracy.</p>"+fig(svg_principles,"Whole to part control first, then detail — two references fix a point"),
   "a_gu":f"<p><strong>આખા થી ભાગ:</strong> મોટું control પહેલા, નાની વિગત અંદર.</p><p><strong>બે સંદર્ભ થી નવો બિંદુ:</strong> દરેક નવો point બે જાણીતા થી નક્કી.</p>"+fig(svg_principles,"આખા થી ભાગ — control પહેલા"),
  },
  {
   "q_en":"Q.1 (b) Explain Types of ranging in detail. (04 marks)",
   "marks_en":"04 marks","marks_gu":"૦૪ ગુણ",
   "a_en":"<p><strong>Direct ranging:</strong> End stations intervisible — ranging rod by eye or line ranger, intermediate rods in line.</p><p><strong>Indirect / reciprocal:</strong> Obstacle / rising ground — two intermediates, reciprocal sight until both align.</p><p>Random line ranging for forest.</p>",
   "a_gu":"<p><strong>Direct:</strong> બન્ને છેડા દેખાય ત્યાં eye થી line માં rod.</p><p><strong>Indirect:</strong> ટેકરી વચ્ચે બે rod વારાફરતી align.</p>",
  },
  {
   "q_en":"Q.1 (c) Explain whole circle bearing. And then calculate internal angles for following closed traverse. Apply usual check. AB 65°/245° BC 145°/325° CD 255°/75° DA 345°/165° (07 marks)",
   "marks_en":"07 marks","marks_gu":"૦૭ ગુણ",
   "a_en":f"""<p><strong>WCB</strong> 0° to 360° clockwise from north.</p><div class="eq">FB to BB diff 180° confirms no local attraction.</div><p><strong>Interior at station = BB of previous − FB of next, take &lt;180° (360−diff if &gt;180°)</strong></p><table><tr><th>Station</th><th>BB prev</th><th>FB next</th><th>Diff</th><th>Interior</th></tr><tr><td>B</td><td>245°</td><td>145°</td><td>100°</td><td>100°</td></tr><tr><td>C</td><td>325°</td><td>255°</td><td>70°</td><td>70°</td></tr><tr><td>D</td><td>75°</td><td>345°</td><td>90° (360−270)</td><td>90°</td></tr><tr><td>A</td><td>165°</td><td>65°</td><td>100°</td><td>100°</td></tr></table><div class="eq">Sum =100+70+90+100=360° = (n−2)180 for n=4 → <strong>check ok.</strong></div>"""+fig(svg_bearings,"WCB 0-360 from north, QB from N/S toward E/W"),
   "a_gu":f"""<p><strong>WCB</strong> ઉત્તર થી clockwise 0-360.</p><p>BB − FB 180 હોય તો local attraction નહીં.</p><div class="eq">B 100° C 70° D 90° A 100° સરવાળો 360° = (4−2)180 pass.</div>"""+fig(svg_bearings,"WCB 0-360"),
  },
  {
   "q_en":"Q.1 (c) OR Enlist any seven survey instruments used in chain, Tape & compass Survey with its functions. (07 marks)",
   "marks_en":"07 marks","marks_gu":"૦૭ ગુણ",
   "a_en":"<table><tr><th>Instrument</th><th>Function</th></tr><tr><td>Metric chain 20/30m</td><td>Horizontal distance</td></tr><tr><td>Arrows</td><td>Mark chain end</td></tr><tr><td>Ranging rods 2-3m</td><td>Mark stations line</td></tr><tr><td>Tape steel/invar</td><td>Offsets accurate</td></tr><tr><td>Cross staff / optical square</td><td>Right angle offset</td></tr><tr><td>Plumb bob</td><td>Vertical transfer on slope</td></tr><tr><td>Prismatic compass</td><td>Bearing</td></tr><tr><td>Pegs, hammer</td><td>Fix stations</td></tr></table>"+fig(svg_chain,"Chain tape compass accessories"),
   "a_gu":"<p>Chain, arrows, ranging rod, tape, cross staff, plumb bob, compass, pegs — કોષ્ટક ઉપર.</p>"+fig(svg_chain,"સાંકળ સાધનો"),
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
   "a_en":"<table><tr><th>Point</th><th>Prismatic</th><th>Surveyor</th></tr><tr><td>Graduation</td><td>0-360 WCB on ring attached to needle</td><td>0-90 QB on fixed box</td></tr><tr><td>Reading</td><td>Prism magnified while sighting</td><td>Direct on top after sighting</td></tr><tr><td>Needle</td><td>Magnetic needle carries card</td><td>Card fixed needle moves</td></tr><tr><td>Tripod</td><td>Usually on tripod small</td><td>Larger on stand</td></tr></table>"+fig(svg_compass,"Prismatic 0-360 vs Surveyor QB"),
   "a_gu":"<p>Prismatic 0-360 prism થી વંચાય, Surveyor 0-90 QB direct.</p>"+fig(svg_compass,"કંપાસ તફાવત"),
  },
  {
   "q_en":"Q.2 (b) State methods of Plane Tabling and explain any one in detail. (04 marks)",
   "marks_en":"04 marks","marks_gu":"૦૪ ગુણ",
   "a_en":"<p><strong>Methods:</strong> Radiation, intersection, traversing, resection. <strong>Radiation detail:</strong> Set over one station, orient, draw rays to all detail points, measure distance scale off — suitable for small area.</p>"+fig(svg_ptable,"Plane table radiation intersection traversing resection"),
   "a_gu":"<p>Radiation, intersection, traversing, resection — radiation માં એક station થી કિરણ દોરી અંતર માપી point મૂકો.</p>"+fig(svg_ptable,"પ્લેન ટેબલ પદ્ધતિ"),
  },
  {
   "q_en":"Q.2 (c) Explain Temporary adjustment of Prismatic compass. (07 marks)",
   "marks_en":"07 marks","marks_gu":"૦૭ ગુણ",
   "a_en":"<ol><li><strong>Centering:</strong> Tripod over station plumb.</li><li><strong>Levelling:</strong> Ball and socket bring bubble centre.</li><li><strong>Focussing prism:</strong> Clear graduation.</li><li><strong>Orientation check:</strong> Free needle swing.</li></ol>",
   "a_gu":"<ol><li>Centering tripod.</li><li>Level bubble.</li><li>Prism focus.</li></ol>",
  },
  {
   "q_en":"Q.2 (a) OR Define (i) Contour (ii) Fore sight (iii) Axis of telescope (03 marks)",
   "marks_en":"03 marks","marks_gu":"૦૩ ગુણ",
   "a_en":"<p><strong>Contour:</strong> Line joining equal RL — horizontal slice. <strong>Fore sight:</strong> Last staff reading before shifting level. <strong>Axis of telescope:</strong> Line through objective centre and cross hair.</p>"+fig(svg_terms,"Contour equal RL, FS last reading, telescope axis"),
   "a_gu":"<p>Contour સરખા RL ની રેખા, Fore sight shift પહેલા છેલ્લું વાંચન, telescope axis objective થી cross hair.</p>"+fig(svg_terms,"પરિભાષા"),
  },
  {
   "q_en":"Q.2 (b) OR Explain characteristics of contours. (04 marks)",
   "marks_en":"04 marks","marks_gu":"૦૪ ગુણ",
   "a_en":"<ul><li>Never intersect except overhang / vertical cliff merged.</li><li>Close steep, wide flat.</li><li>Perpendicular to steepest slope, loop around hill.</li></ul>"+fig(svg_contour,"Contours close=steep wide=flat"),
   "a_gu":"<ul><li>ભેગી ન થાય cliff સિવાય.</li><li>નજીક steep દૂર flat.</li></ul>"+fig(svg_contour,"સમોચ્ચ લક્ષણ"),
  },
  {
   "q_en":"Q.2 (c) OR The following readings were taken with dumpy level: 1.155, 1.565, 2.695, 3.580, 2.085, 2.895, 4.125. Level shifted after 4th reading. Calculate RL by Rise and Fall. Assume BM 100.00 (07 marks)",
   "marks_en":"07 marks","marks_gu":"૦૭ ગુણ",
   "a_en":"""<p><strong>Two setups:</strong> Setup1 BS 1.155 FS 3.580, Setup2 BS 2.085 FS 4.125. CP at 3.580/2.085 same point.</p><table><tr><th>Pt</th><th>BS</th><th>IS</th><th>FS</th><th>HI</th><th>RL</th></tr><tr><td>BM</td><td>1.155</td><td></td><td></td><td>101.155</td><td>100.000</td></tr><tr><td>1</td><td></td><td>1.565</td><td></td><td></td><td>99.590</td></tr><tr><td>2</td><td></td><td>2.695</td><td></td><td></td><td>98.460</td></tr><tr><td>CP</td><td>2.085</td><td></td><td>3.580</td><td>99.660</td><td>97.575</td></tr><tr><td>3</td><td></td><td>2.895</td><td></td><td></td><td>96.765</td></tr><tr><td>4</td><td></td><td></td><td>4.125</td><td></td><td>95.535</td></tr></table><div class="eq">Rise/Fall check: ΣBS 3.240 ΣFS 7.705 diff −4.465 = last RL 95.535 −100.000 ✓</div><p><em>Alternatively via rise/fall between successive points omitting CP duplicate: fall 0.410,1.130,0.885,0.810,1.23 sum 4.465.</em></p>"""+fig(svg_terms,"Levelling HI = RL+BS, RL=HI−IS/FS"),
   "a_gu":"""<p><strong>બે setup:</strong> HI1 101.155 RL 99.59 98.46 97.575 HI2 99.66 RL 96.765 95.535.</p><div class="eq">ΣBS−ΣFS −4.465 = છેલ્લા−પ્રથમ ✓</div>"""+fig(svg_terms,"HI રીત"),
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
   "a_en":"<table><tr><th>Plan</th><th>Map</th></tr><tr><td>Large scale 1:500-1:5000</td><td>Small scale 1:50000+</td></tr><tr><td>Small area curvature ignored</td><td>Large area curvature considered</td></tr><tr><td>Detail engineering layout</td><td>Topography geography</td></tr></table>",
   "a_gu":"<p>Plan મોટો scale નાનો વિસ્તાર curvature નહીં, Map નાનો scale મોટો વિસ્તાર curvature માન્ય.</p>",
  },
  {
   "q_en":"Q.3 (b) Convert following WCB into RB and RB into WCB (i)288° (ii)165°30' (iii)N58°30'E (iv)S72°W (04 marks)",
   "marks_en":"04 marks","marks_gu":"૦૪ ગુણ",
   "a_en":"""<table><tr><th>Given</th><th>Convert</th><th>Answer</th></tr><tr><td>288° WCB</td><td>RB</td><td>360−288=72° → <strong>N72°W</strong></td></tr><tr><td>165°30' WCB</td><td>RB</td><td>180−165°30=14°30 → <strong>S14°30'E</strong></td></tr><tr><td>N58°30'E RB</td><td>WCB</td><td><strong>58°30'</strong></td></tr><tr><td>S72°W RB</td><td>WCB</td><td>180+72=<strong>252°00'</strong></td></tr></table><div class="eq">Rule: Quadrant 1 WCB=RB, 2: 180−RB, 3:180+RB, 4:360−θ</div>"""+fig(svg_bearings,"Conversion WCB ↔ RB"),
   "a_gu":"""<p>288° → N72°W, 165°30' → S14°30'E, N58°30'E→58°30', S72°W→252°.</p>"""+fig(svg_bearings,"WCB RB ફેર"),
  },
  {
   "q_en":"Q.3 (c) Explain errors in the compass survey and describe the closing error. (07 marks)",
   "marks_en":"07 marks","marks_gu":"૦૭ ગુણ",
   "a_en":"<p><strong>Instrumental:</strong> Pivot, needle, graduation. <strong>Personal:</strong> Centering levelling reading. <strong>Natural:</strong> Magnetic storm, local attraction iron, declination.</p><p><strong>Closing error:</strong> Traverse fails to close on itself due to angular/linear errors. Vector e = √ (ΣLat²+ΣDep²). Adjusted by Bowditch or transit rule.</p>"+fig(svg_closing,"Errors instrumental personal natural, closing error vector"),
   "a_gu":"<p>યંત્ર, વ્યક્તિ, natural local attraction — closing error traverse બંધ ન થાય, Bowditch થી સુધારો.</p>"+fig(svg_closing,"ભૂલ અને closing"),
  },
  {
   "q_en":"Q.3 (a) OR Explain the classifications of the Theodolite (03 marks)",
   "marks_en":"03 marks","marks_gu":"૦૩ ગુણ",
   "a_en":"<p>Transit vs non-transit, vernier vs micrometer, primary vs secondary, digital electronic total station.</p>"+fig(svg_theodolite,"Theodolite types overview"),
   "a_gu":"<p>Transit, vernier, digital — પ્રકાર.</p>"+fig(svg_theodolite,"થિયોડોલાઇટ પ્રકાર"),
  },
  {
   "q_en":"Q.3 (b) OR Enlist instruments used for setting out right angles. explain each in details. (04 marks)",
   "marks_en":"04 marks","marks_gu":"૦૪ ગુણ",
   "a_en":"<p><strong>Cross staff open/french, optical square, prism square, site square, theodolite.</strong> Open cross four slots 90°, optical uses 45° mirrors to turn 90° without moving.</p>",
   "a_gu":"<p>Cross staff, optical square, prism square, theodolite — કાટખૂણો.</p>",
  },
  {
   "q_en":"Q.3 (c) OR Draw a neat sketch of dumpy level and label its all parts. (07 marks)",
   "marks_en":"07 marks","marks_gu":"૦૭ ગુણ",
   "a_en":"<p>Telescope, eyepiece, objective, levelling screws 3, bubble tubes, compass, tripod. Levelling by foot screws, focussing, reading staff.</p>"+fig(svg_dumpy,"Dumpy level — telescope eyepiece objective bubble foot screws"),
   "a_gu":"<p>Telescope, bubble, foot screws — આકૃતિ.</p>"+fig(svg_dumpy,"ડમ્પી લેવલ"),
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
   "a_en":"<ul><li>Horizontal vertical angles, bearing, prolong line, offsets, contour tachometry.</li></ul>",
   "a_gu":"<ul><li>આડા ઊભા ખૂણા, line લંબાવો, contour.</li></ul>",
  },
  {
   "q_en":"Q.4 (b) List the fundamental axis of theodolite & give relation between them. (04 marks)",
   "marks_en":"04 marks","marks_gu":"૦૪ ગુણ",
   "a_en":"<p><strong>Axes:</strong> Vertical, horizontal/trunnion, collimation, altitude bubble, plate level.</p><p><strong>Relation:</strong> All perpendicular where needed — collimation ⊥ horizontal, horizontal ⊥ vertical, bubble ⊥ vertical when levelled.</p>"+fig(svg_adjust,"Axes: vertical, horizontal, collimation, bubble"),
   "a_gu":"<p>Vertical, horizontal, collimation, bubble — બધા પરસ્પર લંબ.</p>"+fig(svg_adjust,"અક્ષ"),
  },
  {
   "q_en":"Q.4 (c) Draw a neat sketch of Theodolite and label its all parts. (07 marks)",
   "marks_en":"07 marks","marks_gu":"૦૭ ગુણ",
   "a_en":"<p>Telescope, vertical circle, vernier, upper lower plates, levelling head, tripod, plumb bob.</p>"+fig(svg_theodolite,"Transit theodolite parts"),
   "a_gu":"<p>Telescope, vertical circle, plates — આકૃતિ.</p>"+fig(svg_theodolite,"થિયોડોલાઇટ"),
  },
  {
   "q_en":"Q.4 (a) OR Define (i) Face right (ii) Vertical axis (iii) Swinging (03 marks)",
   "marks_en":"03 marks","marks_gu":"૦૩ ગુણ",
   "a_en":"<p><strong>Face right:</strong> Vertical circle right of observer. <strong>Vertical axis:</strong> Axis about which instrument rotates horizontally. <strong>Swinging:</strong> Turn telescope in horizontal plane.</p>",
   "a_gu":"<p>Face right circle જમણે, vertical axis ઊભો, swinging આડું ફેરવવું.</p>",
  },
  {
   "q_en":"Q.4 (b) OR Differentiate between Rise & Fall method and H.I. Method (04 marks)",
   "marks_en":"04 marks","marks_gu":"૦૪ ગુણ",
   "a_en":"<table><tr><th>Rise & Fall</th><th>H.I.</th></tr><tr><td>Compare successive staff readings</td><td>HI=RL+BS for each setup</td></tr><tr><td>Check ΣRise−ΣFall = last−first</td><td>Check ΣBS−ΣFS same</td></tr><tr><td>Slower more accurate visual</td><td>Faster but error hidden</td></tr></table>",
   "a_gu":"<p>Rise Fall ક્રમિક તુલના, HI દરેક setup HI કાઢી minus — બન્ને check સરખા.</p>",
  },
  {
   "q_en":"Q.4 (c) OR Write Advantages and Disadvantages of Plain Table Survey. (07 marks)",
   "marks_en":"07 marks","marks_gu":"૦૭ ગુણ",
   "a_en":"<p><strong>Adv:</strong> No office plotting error, field check, cheap, good for small fill-in. <strong>Disadv:</strong> Not for rainy/windy, precise work, replot difficult, needs skilled alidade.</p>"+fig(svg_ptable,"Plain table pros cons"),
   "a_gu":"<p>ફાયદા field જ check, ગેરફાયદા પવન વરસાદ માં નહીં.</p>"+fig(svg_ptable,"પ્લેન ટેબલ"),
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
   "a_en":"<p><strong>Orientation:</strong> Table parallel to ground so plotted lines parallel to field. By magnetic compass, back sighting, or resection. Always orient before shifting.</p>",
   "a_gu":"<p>Orientation એટલે ટેબલ નો નકશો જમીન ને સમાંતર — compass કે back sight થી.</p>",
  },
  {
   "q_en":"Q.5 (b) Explain temporary adjustment of Theodolite. (04 marks)",
   "marks_en":"04 marks","marks_gu":"૦૪ ગુણ",
   "a_en":"<p>Setting over station, centering, levelling with plate bubble, focussing eyepiece/objective, parallax removal.</p>"+fig(svg_adjust,"Temporary adjustment centering levelling focussing"),
   "a_gu":"<p>Centering, levelling, focusing.</p>"+fig(svg_adjust,"સમાયોજન"),
  },
  {
   "q_en":"Q.5 (c) Explain the methods of locating contour lines in surveying. (07 marks)",
   "marks_en":"07 marks","marks_gu":"૦૭ ગુણ",
   "a_en":"<p><strong>Direct:</strong> Trace contour by level searching points of same RL. <strong>Indirect:</strong> Grid/spot levels then interpolate. <strong>Tachometry</strong> for hills. Interpolation by arithmetic or graphical.</p>"+fig(svg_interp,"Direct trace vs indirect grid interpolation"),
   "a_gu":"<p>Direct contour પર ફરી point, indirect grid લઈ interpolate.</p>"+fig(svg_interp,"contour પદ્ધતિ"),
  },
  {
   "q_en":"Q.5 (a) OR What are the objectives and uses of surveying? (03 marks)",
   "marks_en":"03 marks","marks_gu":"૦૩ ગુણ",
   "a_en":"<p><strong>Objective:</strong> Prepare plan/map relative positions. Uses: design alignment, earthwork, boundaries, GIS valuation.</p>",
   "a_gu":"<p>નકશો બનાવો — design, earthwork, હદ.</p>",
  },
  {
   "q_en":"Q.5 (b) OR Explain: Bowditch rule and Transit rule. (04 marks)",
   "marks_en":"04 marks","marks_gu":"૦૪ ગુણ",
   "a_en":"<p><strong>Bowditch:</strong> Correction ∝ length — C_lat = −e_lat × l / Σl. <strong>Transit:</strong> Correction ∝ |lat| or |dep| — better for angular errors.</p>"+fig(svg_closing,"Bowditch vs Transit adjustment"),
   "a_gu":"<p>Bowditch length પ્રમાણે, Transit latitude પ્રમાણે.</p>"+fig(svg_closing,"નિયમ"),
  },
  {
   "q_en":"Q.5 (c) OR Enlist any Seven equipment and accessories used in Plain Table Survey with its uses. (07 marks)",
   "marks_en":"07 marks","marks_gu":"૦૭ ગુણ",
   "a_en":"<table><tr><th>Item</th><th>Use</th></tr><tr><td>Plane table board</td><td>Drawing sheet</td></tr><tr><td>Tripod</td><td>Support level</td></tr><tr><td>Alidade plain/telescopic</td><td>Sight rays</td></tr><tr><td>Spirit level</td><td>Level board</td></tr><tr><td>Trough compass</td><td>Orient north</td></tr><tr><td>U-fork plumb</td><td>Center over peg</td></tr><tr><td>Chain/tape</td><td>Distance</td></tr></table>",
   "a_gu":"<p>Board, tripod, alidade, spirit level, compass, U-fork, tape — કોષ્ટક.</p>",
  },
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
    page=f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>DI02006011 · Summer 2026 solved paper</title><style>{CSS}</style></head><body><main class="page"><header class="hero"><div class="eyebrow">Solved question paper · English questions · Friendly Gujarati answers</div><div class="lang-switch" aria-label="Choose language"><button type="button" data-lang="en" aria-pressed="true">English</button><button type="button" data-lang="gu" aria-pressed="false">ગુજરાતી</button></div><h1>Basic Surveying</h1><div class="meta">GTU Diploma · Civil · Semester 2 · Summer 2026 · DI02006011 · 02-07-2026 · 70 marks · 10:30 AM TO 01:00 PM</div></header>{"".join(sections_html)}<div class="footer">Solved paper for study. Verify with field book before site use.</div></main><script>document.querySelectorAll('.lang-switch button').forEach(b=>b.addEventListener('click',()=>{{document.documentElement.lang=b.dataset.lang;document.querySelectorAll('.lang-switch button').forEach(x=>x.setAttribute('aria-pressed',x===b?'true':'false'));}}));</script></body></html>'''
    return page
def main():
    page=build_page()
    out_papers=ROOT/"papers-upload/papers/DI02006011/summer-2026.html"
    out_ws=ROOT/"preview/workshop/DI02006011_summer2026_bilingual.html"
    out_papers.parent.mkdir(parents=True,exist_ok=True)
    out_ws.parent.mkdir(parents=True,exist_ok=True)
    out_papers.write_text(page,encoding="utf-8")
    out_ws.write_text(page,encoding="utf-8")
    d=page.count('<details'); s=page.count('<section')
    ce=page.count('class="en"'); cg=page.count('class="gu"')
    print(f"Bilingual: {out_papers} ({len(page)} chars)")
    print(f"details={d}, sections={s}, en={ce}, gu={cg}")
    print("PASS" if d==28 and s==5 and ce>=28 and cg>=28 else "FAIL")
    print(f"figs={page.count('<figure>')}")
    import re
    gu=''.join(re.findall(r'<div class=\"gu\">(.*?)</div>',page,re.S))
    print(f"brackets gu={gu.count('(')+gu.count(')')}")
    (ROOT/"drive-upload/DI02006011_summer_2026_bilingual.html").write_text(page,encoding="utf-8")
if __name__=="__main__":
    main()
