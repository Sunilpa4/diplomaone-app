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

svg_principles=load_svg("sv1_principles.svg")
svg_scale=load_svg("sv1_scale.svg")
svg_bearings=load_svg("sv3_bearings.svg")
svg_compass=load_svg("sv3_compass.svg")
svg_closing=load_svg("sv3_closing.svg")
svg_ptable=load_svg("sv3_ptable.svg")
svg_dumpy=load_svg("sv4_dumpy.svg")
svg_contour=load_svg("sv4_contour.svg")
svg_terms=load_svg("sv4_terms.svg")
svg_theodolite=load_svg("sv5_theodolite.svg")
svg_adjust=load_svg("sv5_adjust.svg")
svg_chain=load_svg("sv2_chain.svg")
svg_ordinates=load_svg("sv2_ordinates.svg")
svg_interp=load_svg("sv4_interp.svg")

SECTIONS=[
{
 "title_en":"Q1 · RF, offsets and principles",
 "title_gu":"પ્ર.1 · RF, offsets અને સિદ્ધાંત",
 "cards":[
  {
   "q_en":"Q.1 (a) Define: (1) Representative fraction (2) Plan (3) Map (03 marks)",
   "marks_en":"03 marks","marks_gu":"૦૩ ગુણ",
   "a_en":"<p><strong>RF:</strong> Ratio map distance to ground distance same unit — e.g. 1:50000 means 1cm =500m.</p><p><strong>Plan:</strong> Large scale 1:500-5000, small area, curvature ignored, engineering detail.</p><p><strong>Map:</strong> Small scale 1:50000+, large area, curvature considered, topography.</p>",
   "a_gu":"<p><strong>RF:</strong> નકશા અને જમીન અંતર નો ગુણોત્તર — 1:50000 એટલે 1cm =500m.</p><p><strong>Plan:</strong> મોટો scale નાનો વિસ્તાર, <strong>Map:</strong> નાનો scale મોટો વિસ્તાર.</p>",
  },
  {
   "q_en":"Q.1 (b) Define: (1) Offset (2) Tie line (3) Base line (4) Check line (04 marks)",
   "marks_en":"04 marks","marks_gu":"૦૪ ગુણ",
   "a_en":"<p><strong>Offset:</strong> Perpendicular distance from chain line to detail. <strong>Tie line:</strong> Joins two tie stations to locate interior detail. <strong>Base line:</strong> Longest main line on which framework rests. <strong>Check line:</strong> Joins apex to side to verify accuracy.</p>",
   "a_gu":"<p>Offset લંબ અંતર, Tie line interior બિંદુ જોડે, Base line સૌથી લાંબી, Check line ચકાસણી.</p>",
  },
  {
   "q_en":"Q.1 (c) State the principles of Surveying and explain with help of sketch (07 marks)",
   "marks_en":"07 marks","marks_gu":"૦૭ ગુણ",
   "a_en":f"<p><strong>Whole to part and fix by two references</strong> as before.</p>"+fig(svg_principles,"Whole to part — control triangle ABC then detail"),
   "a_gu":f"<p><strong>આખા થી ભાગ અને બે સંદર્ભ થી નવો બિંદુ</strong></p>"+fig(svg_principles,"સિદ્ધાંત"),
  },
  {
   "q_en":"Q.1 (c) OR Construct a diagonal scale of 1cm = 3 km and represent 48.7 km distance on scale. (07 marks)",
   "marks_en":"07 marks","marks_gu":"૦૭ ગુણ",
   "a_en":f"""<div class="eq">RF =1cm /3km =1/300000. Length for 54km max =18cm. Take 18cm, 6 primary divisions 9km each, subdivide 1st into 3km, diagonal into 10 ×0.3km and 10 ×0.03km for 0.7km.</div><p>Mark 48km +0.7km =48.7km with divider between 48km main and 0.7 diagonal.</p>"""+fig(svg_scale,"Diagonal scale 1cm=3km RF 1:300000 length 18cm for 54km show 48.7km"),
   "a_gu":f"""<p>RF 1:300000 18cm માં 54km, 48.7km mark — main 48km + diagonal 0.7km.</p>"""+fig(svg_scale,"વિકર્ણ સ્કેલ 1cm=3km"),
  },
 ]
},
{
 "title_en":"Q2 · Tapes, area and prismatic compass",
 "title_gu":"પ્ર.2 · ટેપ, ક્ષેત્રફળ અને કંપાસ",
 "cards":[
  {
   "q_en":"Q.2 (a) Enlist different types of tapes used and explain any one in detail. (03 marks)",
   "marks_en":"03 marks","marks_gu":"૦૩ ગુણ",
   "a_en":"<p>Cloth, metallic, steel, invar. <strong>Steel tape:</strong> 20-30m, accurate, applies sag temperature corrections.</p>",
   "a_gu":"<p>Cloth, metallic, steel, invar — steel સચોટ sag correction.</p>",
  },
  {
   "q_en":"Q.2 (b) List out different methods used for computation of area by taking offsets and explain any one in detail. (04 marks)",
   "marks_en":"04 marks","marks_gu":"૦૪ ગુણ",
   "a_en":"<p>Mid ordinate, average ordinate, trapezoidal, Simpson. <strong>Simpson:</strong> Area = d/3 [first+last +4 odd +2 even] needs even intervals parabolic accuracy.</p>",
   "a_gu":"<p>Mid, average, trapezoidal, Simpson — Simpson d/3 [first+last+4odd+2even] parabolic.</p>",
  },
  {
   "q_en":"Q.2 (c) Draw neat sketch of Prismatic compass and label all its parts. (07 marks)",
   "marks_en":"07 marks","marks_gu":"૦૭ ગુણ",
   "a_en":f"<p>Magnetic needle with graduated ring 0-360, prism, object vane, eye vane, brake pin, lifting lever, tripod socket.</p>"+fig(svg_compass,"Prismatic compass parts — prism, vane, ring 0-360"),
   "a_gu":f"<p>Needle ring 0-360, prism, vane, brake — આકૃતિ.</p>"+fig(svg_compass,"કંપાસ આકૃતિ"),
  },
  {
   "q_en":"Q.2 (a) OR Enlist various instruments used in chaining with their uses. (03 marks)",
   "marks_en":"03 marks","marks_gu":"૦૩ ગુણ",
   "a_en":"<p>Chain, arrows, ranging rods, offset rods, plumb bob, cross staff, pegs, hammers.</p>",
   "a_gu":"<p>Chain, arrows, rods, plumb bob, cross staff — યાદી.</p>",
  },
  {
   "q_en":"Q.2 (b) OR Differentiate between prismatic and surveyor compass (04 marks)",
   "marks_en":"04 marks","marks_gu":"૦૪ ગુણ",
   "a_en":"<table><tr><th>Prismatic</th><th>Surveyor</th></tr><tr><td>WCB 0-360 rotating ring</td><td>QB 0-90 fixed</td></tr><tr><td>Prism read while sighting</td><td>Read after sighting on top</td></tr></table>",
   "a_gu":"<p>Prismatic WCB 0-360 prism, Surveyor QB 0-90 direct.</p>",
  },
  {
   "q_en":"Q.2 (c) OR Write Advantages and Disadvantages of Plain Table Survey. (07 marks)",
   "marks_en":"07 marks","marks_gu":"૦૭ ગુણ",
   "a_en":"<p>Adv no plotting office, field check, simple. Disadv not for wet/windy, less accurate than theodolite, replot hard.</p>",
   "a_gu":"<p>ફાયદા office નહીં, ગેરફાયદા વરસાદ માં નહીં.</p>",
  },
 ]
},
{
 "title_en":"Q3 · Bearings, adjustment and conversions",
 "title_gu":"પ્ર.3 · બેરિંગ, સમાયોજન અને રૂપાંતર",
 "cards":[
  {
   "q_en":"Q.3 (a) Define: i) Magnetic bearing ii) Fore bearing iii) Isogonic lines. (03 marks)",
   "marks_en":"03 marks","marks_gu":"૦૩ ગુણ",
   "a_en":"<p><strong>Magnetic bearing:</strong> Angle from magnetic north. <strong>Fore bearing:</strong> Bearing in forward direction of progress. <strong>Isogonic:</strong> Lines joining equal declination.</p>",
   "a_gu":"<p>Magnetic ઉત્તર થી ખૂણો, Fore આગળ દિશા, Isogonic સરખા declination ની રેખા.</p>",
  },
  {
   "q_en":"Q.3 (b) Explain Temporary adjustment of Prismatic compass. (04 marks)",
   "marks_en":"04 marks","marks_gu":"૦૪ ગુણ",
   "a_en":"<p>Centering, levelling bubble, focussing prism, checking free swing.</p>",
   "a_gu":"<p>Centering, levelling, prism focus.</p>",
  },
  {
   "q_en":"Q.3 (c) During compass survey traverse ABCDE bearings FB 106°19' 27°06' 279°42' 193°17' 126°32' BB 286°19' 207°06' 99°42' 13°17' 306°32'. Compute interior angles and closing error. (07 marks)",
   "marks_en":"07 marks","marks_gu":"૦૭ ગુણ",
   "a_en":f"""<p><strong>FB to BB diff 180° → no local attraction.</strong></p><table><tr><th>At</th><th>BB prev</th><th>FB next</th><th>Diff</th><th>Interior (&lt;180)</th></tr><tr><td>B</td><td>286°19'</td><td>27°06'</td><td>259°13'</td><td>100°47'</td></tr><tr><td>C</td><td>207°06'</td><td>279°42'</td><td>72°36'</td><td>72°36'</td></tr><tr><td>D</td><td>99°42'</td><td>193°17'</td><td>93°35'</td><td>93°35'</td></tr><tr><td>E</td><td>13°17'</td><td>126°32'</td><td>113°15'</td><td>113°15'</td></tr><tr><td>A</td><td>306°32'</td><td>106°19'</td><td>200°13'</td><td>159°47'</td></tr></table><div class="eq">Sum =540°00' = (5−2)180 → <strong>closing error 0°00'</strong></div>""",
   "a_gu":f"""<p>FB to BB 180 તફાવત — local attraction નહીં.</p><div class="eq">B100°47' C72°36' D93°35' E113°15' A159°47' સરવાળો 540° closing 0.</div>""",
  },
  {
   "q_en":"Q.3 (a) OR Differentiate between Whole Circle Bearing and Quadrantal Bearing (03 marks)",
   "marks_en":"03 marks","marks_gu":"૦૩ ગુણ",
   "a_en":"<table><tr><th>WCB</th><th>QB</th></tr><tr><td>0-360 from north clockwise</td><td>0-90 from N or S toward E/W</td></tr><tr><td>Prismatic</td><td>Surveyor</td></tr></table>",
   "a_gu":"<p>WCB 0-360, QB N/S થી 0-90.</p>",
  },
  {
   "q_en":"Q.3 (b) OR Enlist different methods of Plane table surveying and explain any one in detail. (04 marks)",
   "marks_en":"04 marks","marks_gu":"૦૪ ગુણ",
   "a_en":"<p>Radiation, intersection, traversing, resection — radiation one station rays scale distance.</p>",
   "a_gu":"<p>Radiation, intersection, traversing, resection.</p>",
  },
  {
   "q_en":"Q.3 (c) OR (i) Convert WCB into Reduced bearing (1)65° (2)195° (3)295° (ii) Convert Fore bearing into Back bearing AB 12°24' BC 119°48' CD 266°30' DE 354°18' (07 marks)",
   "marks_en":"07 marks","marks_gu":"૦૭ ગુણ",
   "a_en":f"""<p><strong>WCB to RB:</strong> 65° → N65°E, 195° → S15°W (180−195 negative →195−180=15 SW), 295° → N65°W (360−295=65).</p><p><strong>FB to BB ±180:</strong> 12°24'→192°24', 119°48'→299°48', 266°30'→86°30', 354°18'→174°18' (&lt;180 +180 else −180).</p>"""+fig(svg_bearings,"WCB to RB and FB to BB ±180"),
   "a_gu":f"""<p>WCB→RB: 65° N65°E, 195° S15°W, 295° N65°W. FB→BB +180 mod360.</p>"""+fig(svg_bearings,"રૂપાંતર"),
  },
 ]
},
{
 "title_en":"Q4 · Levelling, HI and contour terms",
 "title_gu":"પ્ર.4 · લેવલિંગ, HI અને સમોચ્ચ",
 "cards":[
  {
   "q_en":"Q.4 (a) Define: (1) Levelling (2) Reduced level (3) Bench Mark (03 marks)",
   "marks_en":"03 marks","marks_gu":"૦૩ ગુણ",
   "a_en":"<p><strong>Levelling:</strong> Find elevation relative to datum. <strong>RL:</strong> Height above datum. <strong>BM:</strong> Known RL point.</p>",
   "a_gu":"<p>Levelling ઊંચાઈ, RL datum થી, BM જાણીતો RL.</p>",
  },
  {
   "q_en":"Q.4 (b) Explain Contour Interval and Horizontal equivalent. (04 marks)",
   "marks_en":"04 marks","marks_gu":"૦૪ ગુણ",
   "a_en":"<p><strong>CI:</strong> Vertical distance between successive contours — constant. <strong>HE:</strong> Horizontal distance between them — varies with slope steep small HE.</p>",
   "a_gu":"<p>CI ઊભું અંતર fixed, HE આડું અંતર slope પર.</p>",
  },
  {
   "q_en":"Q.4 (c) Readings on 4m staff continuous sloping ground 30m interval: 0.76,1.515,1.935,2.400,2.985,3.650,1.015,1.855,2.495,3.57,0.875,1.085,1.790,2.450. RL first 200.500 HI method. (07 marks)",
   "marks_en":"07 marks","marks_gu":"૦૭ ગુણ",
   "a_en":"""<p><strong>Three setups:</strong> CP1 after 3.650 CP2 after 3.57</p><table><tr><th>Pt</th><th>BS</th><th>IS</th><th>FS</th><th>HI</th><th>RL</th><th>Dist</th></tr><tr><td>1</td><td>0.76</td><td></td><td></td><td>201.260</td><td>200.500</td><td>0</td></tr><tr><td>2</td><td></td><td>1.515</td><td></td><td></td><td>199.745</td><td>30</td></tr><tr><td>3</td><td></td><td>1.935</td><td></td><td></td><td>199.325</td><td>60</td></tr><tr><td>4</td><td></td><td>2.400</td><td></td><td></td><td>198.860</td><td>90</td></tr><tr><td>5</td><td></td><td>2.985</td><td></td><td></td><td>198.275</td><td>120</td></tr><tr><td>6 CP1</td><td>1.015</td><td></td><td>3.650</td><td>198.625</td><td>197.610</td><td>150</td></tr><tr><td>7</td><td></td><td>1.855</td><td></td><td></td><td>196.770</td><td>180</td></tr><tr><td>8</td><td></td><td>2.495</td><td></td><td></td><td>196.130</td><td>210</td></tr><tr><td>9 CP2</td><td>0.875</td><td></td><td>3.57</td><td>195.930</td><td>195.055</td><td>240</td></tr><tr><td>10</td><td></td><td>1.085</td><td></td><td></td><td>194.845</td><td>270</td></tr><tr><td>11</td><td></td><td>1.790</td><td></td><td></td><td>194.140</td><td>300</td></tr><tr><td>12</td><td></td><td></td><td>2.450</td><td></td><td>193.480</td><td>330</td></tr></table><div class="eq">ΣBS2.65 ΣFS9.67 diff −7.02 =193.48−200.50 ✓</div>""",
   "a_gu":"""<p><strong>ત્રણ setup:</strong> HI1 201.26 CP1 197.61 HI2 198.625 CP2 195.055 છેલ્લા 193.48 check ΣBS−ΣFS −7.02.</p>""",
  },
  {
   "q_en":"Q.4 (a) OR Define: (1) Line of collimation (2) Back Sight (3) Fore Sight (03 marks)",
   "marks_en":"03 marks","marks_gu":"૦૩ ગુણ",
   "a_en":"<p><strong>Line of collimation:</strong> Sight line objective to cross hair. <strong>BS:</strong> First reading after setup. <strong>FS:</strong> Last before shifting.</p>",
   "a_gu":"<p>Collimation sight line, BS setup પછી પ્રથમ, FS shift પહેલા છેલ્લું.</p>",
  },
  {
   "q_en":"Q.4 (b) OR Explain difference between Rise and fall method and H.I. method. (04 marks)",
   "marks_en":"04 marks","marks_gu":"૦૪ ગુણ",
   "a_en":"<table><tr><th>Rise Fall</th><th>H.I.</th></tr><tr><td>Successive diff</td><td>HI per setup</td></tr><tr><td>Visual check each point</td><td>Faster</td></tr></table>",
   "a_gu":"<p>Rise Fall ક્રમિક તફાવત, HI setup HI.</p>",
  },
  {
   "q_en":"Q.4 (c) OR Readings 0.950,1.615,1.925,2.515,2.895,3.495,1.125,1.980,2.450,3.750,0.925,1.455,1.750,2.850 interval 25m RL100 rise/fall and gradient first-last. (07 marks)",
   "marks_en":"07 marks","marks_gu":"૦૭ ગુણ",
   "a_en":"""<p><strong>Three setups CP after 3.495 and 3.75:</strong></p><table><tr><th>Pt</th><th>BS</th><th>IS</th><th>FS</th><th>Rise/Fall</th><th>RL</th></tr><tr><td>1</td><td>0.95</td><td></td><td></td><td></td><td>100.000</td></tr><tr><td>2</td><td></td><td>1.615</td><td></td><td>F0.665</td><td>99.335</td></tr><tr><td>3</td><td></td><td>1.925</td><td></td><td>F0.310</td><td>99.025</td></tr><tr><td>4</td><td></td><td>2.515</td><td></td><td>F0.590</td><td>98.435</td></tr><tr><td>5</td><td></td><td>2.895</td><td></td><td>F0.380</td><td>98.055</td></tr><tr><td>6 CP1</td><td>1.125</td><td></td><td>3.495</td><td>F0.600</td><td>97.455</td></tr><tr><td>7</td><td></td><td>1.98</td><td></td><td>F0.855</td><td>96.600</td></tr><tr><td>8</td><td></td><td>2.45</td><td></td><td>F0.470</td><td>96.130</td></tr><tr><td>9 CP2</td><td>0.925</td><td></td><td>3.75</td><td>F1.300</td><td>94.830</td></tr><tr><td>10</td><td></td><td>1.455</td><td></td><td>F0.530</td><td>94.300</td></tr><tr><td>11</td><td></td><td>1.75</td><td></td><td>F0.295</td><td>94.005</td></tr><tr><td>12</td><td></td><td></td><td>2.85</td><td>F1.100</td><td>92.905</td></tr></table><div class="eq">ΣFall 7.095 ΣRise0 diff −7.095 =92.905−100 ✓ Gradient = (92.905−100)/325 = −7.095/325 = −1 in 45.8 or −2.18% falling.</div>""",
   "a_gu":"""<p>CP1 97.455 CP2 94.83 છેલ્લા 92.905 gradient −7.095/325 = 1 in 45.8 downwards.</p>""",
  },
 ]
},
{
 "title_en":"Q5 · Levelling errors, theodolite and contour",
 "title_gu":"પ્ર.5 · ભૂલ, થિયોડોલાઇટ અને સમોચ્ચ",
 "cards":[
  {
   "q_en":"Q.5 (a) Enlist Errors in levelling and explain anyone. (03 marks)",
   "marks_en":"03 marks","marks_gu":"૦૩ ગુણ",
   "a_en":"<p>Instrumental collimation bubble, staff not vertical, personal reading, natural curvature refraction, settlement.</p><p><strong>Collimation:</strong> Line not horizontal — balance BS=FS distances to cancel.</p>",
   "a_gu":"<p>Collimation, staff vertical, curvature — collimation દૂર BS FS સરખા.</p>",
  },
  {
   "q_en":"Q.5 (b) Explain Temporary adjustment of theodolite. (04 marks)",
   "marks_en":"04 marks","marks_gu":"૦૪ ગુણ",
   "a_en":"<p>Setting, centering, levelling with plate bubbles, focussing.</p>",
   "a_gu":"<p>Centering, levelling, focusing.</p>",
  },
  {
   "q_en":"Q.5 (c) Explain Characteristics of contour with help of sketch. (07 marks)",
   "marks_en":"07 marks","marks_gu":"૦૭ ગુણ",
   "a_en":"<p>See Q2b OR summertime — never cross except cliff, close steep etc.</p>"+fig(svg_contour,"Contour characteristics"),
   "a_gu":"<p>Steep નજીક flat દૂર, cliff પર મળે.</p>"+fig(svg_contour,"લક્ષણ"),
  },
  {
   "q_en":"Q.5 (a) OR Enlist Methods of levelling and explain any one in detail. (03 marks)",
   "marks_en":"03 marks","marks_gu":"૦૩ ગુણ",
   "a_en":"<p>Simple, differential, fly, check, profile, cross, reciprocal. <strong>Fly:</strong> Rapid to connect BM.</p>",
   "a_gu":"<p>Simple, differential, fly, profile — fly BM જોડવા ઝડપી.</p>",
  },
  {
   "q_en":"Q.5 (b) OR Explain Following terms with respect to Theodolite (1) Transiting (2) Face left observation (3) Line of Collimation (4) Trunnion axis (04 marks)",
   "marks_en":"04 marks","marks_gu":"૦૪ ગુણ",
   "a_en":"<p><strong>Transiting:</strong> Telescope 180 vertical to invert. <strong>Face left:</strong> Vertical circle left. <strong>Collimation:</strong> Sight line. <strong>Trunnion:</strong> Horizontal tilting axis.</p>",
   "a_gu":"<p>Transiting 180 flip, Face left circle ડાબે, collimation sight, trunnion આડો axis.</p>",
  },
  {
   "q_en":"Q.5 (c) OR Draw neat sketch of Dumpy level and label its all parts. (07 marks)",
   "marks_en":"07 marks","marks_gu":"૦૭ ગુણ",
   "a_en":f"<p>As Q3c summer — telescope etc.</p>"+fig(svg_dumpy,"Dumpy level parts"),
   "a_gu":f"<p>Telescope, bubble — આકૃતિ.</p>"+fig(svg_dumpy,"ડમ્પી લેવલ"),
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
    page=f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>DI02006011 · Winter 2025 solved paper</title><style>{CSS}</style></head><body><main class="page"><header class="hero"><div class="eyebrow">Solved question paper · English questions · Friendly Gujarati answers</div><div class="lang-switch" aria-label="Choose language"><button type="button" data-lang="en" aria-pressed="true">English</button><button type="button" data-lang="gu" aria-pressed="false">ગુજરાતી</button></div><h1>Basic Surveying</h1><div class="meta">GTU Diploma · Civil · Semester 2 · Winter 2025 · DI02006011 · 27-01-2026 · 70 marks · 10:30 AM TO 01:00PM</div></header>{"".join(sections_html)}<div class="footer">Solved paper for study. Verify with field book before site use.</div></main><script>document.querySelectorAll('.lang-switch button').forEach(b=>b.addEventListener('click',()=>{{document.documentElement.lang=b.dataset.lang;document.querySelectorAll('.lang-switch button').forEach(x=>x.setAttribute('aria-pressed',x===b?'true':'false'));}}));</script></body></html>'''
    return page
def main():
    page=build_page()
    out_papers=ROOT/"papers-upload/papers/DI02006011/winter-2025.html"
    out_ws=ROOT/"preview/workshop/DI02006011_winter2025_bilingual.html"
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
    (ROOT/"drive-upload/DI02006011_winter_2025_bilingual.html").write_text(page,encoding="utf-8")
if __name__=="__main__":
    main()
