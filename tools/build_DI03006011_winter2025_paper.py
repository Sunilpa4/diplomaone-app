#!/usr/bin/env python3
from pathlib import Path
import html
ROOT=Path(__file__).resolve().parent.parent
def load_svg(name):
    p=ROOT/f"content/civil/sem3/DI03006011/diagrams/{name}"
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
svg_wall=load_svg("ct1_wall.svg")
svg_frame=load_svg("ct1_frame.svg")
svg_scaffold=load_svg("ct3_scaffold.svg")
svg_found=load_svg("ct2_found.svg")
svg_bonds=load_svg("ct3_bonds.svg")
svg_ureamed=load_svg("ct2_ureamed.svg")
svg_dpc=load_svg("ct3_dpc.svg")
svg_timber=load_svg("ct2_timber.svg")
svg_excav=load_svg("ct5_excav.svg")
svg_fail=load_svg("ct5_fail.svg")
svg_ppe=load_svg("ct5_ppe.svg")
svg_formwork=load_svg("ct3_formwork.svg")

SECTIONS=[
{
 "title_en":'Q1 · Building items, structure types, scaffolding / formwork',
 "title_gu":'પ્ર.1 · બિલ્ડિંગ વસ્તુ, સ્ટ્રક્ચર પ્રકાર, પાલખ / ફોર્મવર્ક',
 "cards":[
  {
   "q_en":'Q.1 (a) Write functions of following items in Building: Lintel, Sill, Weather sheds. (03 marks)',
   "marks_en":'03 marks',"marks_gu":'૦૩ ગુણ',
   "a_en":f"""<p><strong>Lintel:</strong> Horizontal RCC/steel beam over door-window opening that carries wall load above and transfers it to jambs. Prevents cracking, keeps opening square. Provided 150 mm bearing each side, depth 1/10 of span.</p><p><strong>Sill:</strong> Bottom horizontal member of window frame. Supports window, sheds rain water outward with 1:20 slope, protects wall top from damp, provides level base for shutter.</p><p><strong>Weather shed / Chhajja:</strong> 450–600 mm projection above opening. Shades from sun and rain, protects lintel and window from direct weathering, reduces heat gain. RCC cantilever 75–100 mm thick with drip groove.</p>"""+fig(svg_wall,'Lintel over opening carries wall load, sill drains water outward, chhajja shades — all seen in wall cross-section'),
   "a_gu":f"""<p><strong>Lintel:</strong> સમક્ષિતિજ RCC/સ્ટીલ બીમ ઉપર door-window opening તે carries દિવાલ ભાર ઉપર અને transfers it સુધી jambs. Prevents cracking, keeps opening સ્ક્વેર. Provided 150 mm બેરિંગ દરેક બાજુ, depth 1/10 નો span.</p><p><strong>Sill:</strong> Bottom સમક્ષિતિજ member નો window ફ્રેમ. Supports window, sheds rain પાણી outward સાથે 1:20 slope, protects દિવાલ top થી ભેજવાળું, provides લેવલ base માટે shutter.</p><p><strong>Weather shed / Chhajja:</strong> 450–600 mm projection ઉપર opening. Shades થી sun અને rain, protects lintel અને window થી direct weathering, reduces heat gain. RCC કેન્ટીલીવર 75–100 mm thick સાથે drip groove.</p>"""+fig(svg_wall,'Lintel ઉપર opening carries દિવાલ ભાર, sill drains પાણી outward, chhajja shades — બધા seen માં દિવાલ ક્રોસ-section'),
  },
  {
   "q_en":'Q.1 (b) Differentiate between Load Bearing and Framed Structures. (04 marks)',
   "marks_en":'04 marks',"marks_gu":'૦૪ ગુણ',
   "a_en":f"""<table><tr><th>Point</th><th>Load Bearing</th><th>Framed</th></tr><tr><td>Load path</td><td>Walls themselves carry slab load to foundation</td><td>RCC columns + beams form frame, walls are infill</td></tr><tr><td>Wall thickness</td><td>200–350 mm, thicker at lower floors</td><td>100–150 mm partition, uniform</td></tr><tr><td>Height limit</td><td>3–4 floors economical beyond uneconomical</td><td>High rise 10+ floors, flexible plan</td></tr><tr><td>Material</td><td>Brick/stone masonry + RCC slab</td><td>RCC/steel frame, brick/AAC infill</td></tr><tr><td>Earthquake</td><td>Stiff but brittle if not reinforced</td><td>Ductile detailing possible, better performance</td></tr></table>"""+fig(svg_frame,'Load bearing walls carry load vs framed columns-beams carry load'),
   "a_gu":f"""<table><tr><th>બિંદુ</th><th>ભારવાહી</th><th>ફ્રેમ</th></tr><tr><td>ભાર માર્ગ</td><td>દિવાલો themselves લઈ જવું સ્લેબ ભાર સુધી પાયો</td><td>RCC કોલમો + બીમો form ફ્રેમ, દિવાલો છે પૂરક</td></tr><tr><td>દિવાલ જાડાઈ</td><td>200–350 mm, thicker પર લોઅર માળ</td><td>100–150 mm પાર્ટીશન, એકસરખું</td></tr><tr><td>ઊંચાઈ limit</td><td>3–4 માળ કરકસરભર્યું beyond uneconomical</td><td>ઊંચી ઊંચાઈ 10+ માળ, flexible plan</td></tr><tr><td>Material</td><td>ઈંટ/stone masonry + RCC સ્લેબ</td><td>RCC/સ્ટીલ ફ્રેમ, ઈંટ/AAC પૂરક</td></tr><tr><td>Earthquake</td><td>Stiff but બરડ જો નહીં reinforced</td><td>તન્ય detailing શક્ય, better performance</td></tr></table>"""+fig(svg_frame,'ભાર બેરિંગ દિવાલો લઈ જવું ભાર vs framed કોલમો-બીમો લઈ જવું ભાર'),
  },
  {
   "q_en":'Q.1 (c) With neat sketch explain components of Scaffolding. (07 marks)',
   "marks_en":'07 marks',"marks_gu":'૦૭ ગુણ',
   "a_en":f"""<div class="eq"><strong>Given:</strong> Need temporary working platform for masons/material at 3–10 m height — scaffolding must be safe, stable, accessible.<br><strong>Concept:</strong> Scaffold is temporary braced frame of standards+ledgers+bracings carrying planks.</div>
<table><tr><th>Component as labelled in sketch</th><th>Size / spacing</th><th>Function</th></tr><tr><td><strong>Standards — vertical posts</strong></td><td>48 mm steel tubes 2 m c/c, rest on base plate+sole board</td><td>Carry vertical load to ground</td></tr><tr><td><strong>Ledgers — horizontal runners</strong></td><td>1.5 m lift intervals, clamp to standards</td><td>Tie standards longitudinally, support transoms</td></tr><tr><td><strong>Transoms / Putlogs</strong></td><td>1.2 m gap, one end on ledger, one in wall hole 75 mm</td><td>Support platform boards</td></tr><tr><td><strong>Bracing — diagonal + longitudinal</strong></td><td>45° both planes every 4 bays</td><td>Resist sway wind, make rigid</td></tr><tr><td><strong>Base plate + sole board 225×35 mm</strong></td><td>150×150 mm steel plate on timber</td><td>Spread load, prevent sinking</td></tr><tr><td><strong>Platform / boards + guard rail + toe board</strong></td><td>Boards 225 mm thick, guard rail 1 m + mid rail 0.5 m, toe board 150 mm</td><td>Safe working, prevent fall of person/material</td></tr><tr><td><strong>Ladder access + ties to building</strong></td><td>Ties every 4 m 6 m grid, ladder inclination 75°</td><td>Anchor against overturning, access</td></tr></table>
<p><strong>Types in brief:</strong> Single / Bricklayer putlog in wall for brick work up to 3 floors, Double / Independent free standing for framed/high building, Steel tubular reusable, Needle/cantilever projecting over footpath where ground no space, Suspended gondola for facade.</p>
<p><strong>Erection stepwise 7 steps:</strong> 1) Level ground, sole boards along wall 2) Erect standards plumb checked by plumb bob 3) Fix ledgers at 1.5 m height with couplers 4) Fix transoms + boards 5) Add diagonal bracing 6) Fix guard rails/toe boards/ladder 7) Tie to wall every 4 m, check 3-4-5 for squareness, test load 2 kN/m2 before use.</p>
<div class="eq"><strong>Answer:</strong> 7+ components as table — standards, ledgers, putlogs, bracing, base plate, platform, guard/toe, ladder+ties with sizes and erection steps — full 7 marks with sketch.</div>"""+fig(svg_scaffold,'Scaffolding — standards vertical, ledgers horizontal, putlogs, bracing, platform, guard rail, toe board, base plate, ties'),
   "a_gu":f"""<div class="eq"><strong>આપેલ:</strong> જરૂર temporary working પ્લેટફોર્મ માટે masons/material પર 3–10 m ઊંચાઈ — પાલખ must હોવું safe, stable, accessible.<br><strong>સિદ્ધાંત:</strong> Scaffold છે temporary braced ફ્રેમ નો સ્ટાન્ડર્ડ્સ+ledgers+bracings carrying planks.</div>
<table><tr><th>Component તરીકે labelled માં sketch</th><th>Size / spacing</th><th>Function</th></tr><tr><td><strong>સ્ટાન્ડર્ડ્સ — vertical posts</strong></td><td>48 mm સ્ટીલ tubes 2 m c/c, rest પર base પ્લેટ+sole board</td><td>લઈ જવું vertical ભાર સુધી ground</td></tr><tr><td><strong>Ledgers — સમક્ષિતિજ runners</strong></td><td>1.5 m lift intervals, ક્લેમ્પ સુધી સ્ટાન્ડર્ડ્સ</td><td>Tie સ્ટાન્ડર્ડ્સ longitudinally, support transoms</td></tr><tr><td><strong>Transoms / Putlogs</strong></td><td>1.2 m gap, one end પર ledger, one માં દિવાલ hole 75 mm</td><td>Support પ્લેટફોર્મ boards</td></tr><tr><td><strong>Bracing — diagonal + longitudinal</strong></td><td>45° both planes દરેક 4 bays</td><td>Resist sway wind, make કઠોર</td></tr><tr><td><strong>Base પ્લેટ + sole board 225×35 mm</strong></td><td>150×150 mm સ્ટીલ પ્લેટ પર timber</td><td>Spread ભાર, prevent sinking</td></tr><tr><td><strong>પ્લેટફોર્મ / boards + guard rail + ટો board</strong></td><td>Boards 225 mm thick, guard rail 1 m + mid rail 0.5 m, ટો board 150 mm</td><td>Safe working, prevent ફોલ નો person/material</td></tr><tr><td><strong>Ladder access + ties સુધી building</strong></td><td>Ties દરેક 4 m 6 m grid, ladder inclination 75°</td><td>Anchor against overturning, access</td></tr></table>
<p><strong>Types માં brief:</strong> સિંગલ / Bricklayer putlog માં દિવાલ માટે ઈંટ work up સુધી 3 માળ, ડબલ / Independent free standing માટે framed/ઊંચી building, સ્ટીલ ટ્યુબ્યુલર reusable, નીડલ/કેન્ટીલીવર projecting ઉપર footpath જ્યાં ground no space, લટકતું gondola માટે facade.</p>
<p><strong>Erection stepwise 7 steps:</strong> 1) લેવલ ground, sole boards along દિવાલ 2) Erect સ્ટાન્ડર્ડ્સ પ્લમ્બ checked દ્વારા પ્લમ્બ બોબ 3) Fix ledgers પર 1.5 m ઊંચાઈ સાથે couplers 4) Fix transoms + boards 5) Add diagonal bracing 6) Fix guard rails/ટો boards/ladder 7) Tie સુધી દિવાલ દરેક 4 m, તપાસ 3-4-5 માટે squareness, test ભાર 2 kN/m2 પહેલા ઉપયોગ.</p>
<div class="eq"><strong>Answer:</strong> 7+ components તરીકે ટેબલ — સ્ટાન્ડર્ડ્સ, ledgers, putlogs, bracing, base પ્લેટ, પ્લેટફોર્મ, guard/ટો, ladder+ties સાથે sizes અને erection steps — full 7 marks સાથે sketch.</div>"""+fig(svg_scaffold,'પાલખ — સ્ટાન્ડર્ડ્સ vertical, ledgers સમક્ષિતિજ, putlogs, bracing, પ્લેટફોર્મ, guard rail, ટો board, base પ્લેટ, ties'),
  },
  {
   "q_en":'Q.1 (c) OR Discuss in detail: Characteristics of good formwork. (07 marks)',
   "marks_en":'07 marks',"marks_gu":'૦૭ ગુણ',
   "a_en":f"""<div class="eq"><strong>Concept:</strong> Formwork is temporary mould to hold fresh concrete till it gains strength — must give accurate shape vs economy and safety.</div>
<table><tr><th>Characteristic for good formwork</th><th>What it means technically</th><th>Why needed / limit</th></tr><tr><td><strong>1. Strong enough</strong></td><td>Withstand fresh concrete pressure + vibration + worker load without failure. Design for 25–30 kN/m2 lateral for wall</td><td>No collapse, safety factor 2</td></tr><tr><td><strong>2. Rigid — minimal deflection</strong></td><td>Deflection &lt;3 mm or span/300 to keep line and level</td><td>No bulged wall/slab, fair face</td></tr><tr><td><strong>3. Leak-proof — tight joints</strong></td><td>Joints sealed with foam/tape, grout tight</td><td>No grout loss → no honeycomb, strength maintained</td></tr><tr><td><strong>4. Smooth face</strong></td><td>Plywood 12 mm with film, steel plates</td><td>Good finish less plaster, easy de-shutter</td></tr><tr><td><strong>5. Light & handleable</strong></td><td>Aluminium or plywood panels 1.2×2.4 m man-handleable</td><td>Speed, crane not needed low rise</td></tr><tr><td><strong>6. Easy to strip without damage</strong></td><td>Oiled with shuttering oil, taper, correct striking time — sides 24 h, slabs 14 d, beams 21 d per IS 456</td><td>Concrete not damaged, panels reusable 50+ times steel</td></tr><tr><td><strong>7. Accurate to size, plumb and level</strong></td><td>Within ±5 mm vertical ±3 mm thickness, checked with plumb and level</td><td>Structural accuracy</td></tr><tr><td><strong>8. Reusable & economical</strong></td><td>Standard module sizes to repeat floor-to-floor</td><td>Cost per use low</td></tr></table>
<p><strong>Materials:</strong> Traditional timber, plywood with timber battens, steel panels for mass, aluminium for fast cycle, plastic for small repeats. Choice balancing characteristic vs cost.</p>
<div class="eq"><strong>Answer:</strong> 8 characteristics as table — strong, rigid, leak-proof, smooth, light, easy strip, accurate, reusable — with limits and striking times for full 7 marks.</div>""",
   "a_gu":f"""<div class="eq"><strong>સિદ્ધાંત:</strong> Formwork છે temporary mould સુધી hold fresh કોંક્રિટ till it gains મજબૂતાઈ — must આપો accurate shape vs economy અને સલામતી.</div>
<table><tr><th>Characteristic માટે સારી formwork</th><th>What it means technically</th><th>Why needed / limit</th></tr><tr><td><strong>1. Strong enough</strong></td><td>Withstand fresh કોંક્રિટ pressure + vibration + worker ભાર વગર નિષ્ફળતા. ડિઝાઇન માટે 25–30 kN/m2 lateral માટે દિવાલ</td><td>No collapse, સલામતી factor 2</td></tr><tr><td><strong>2. કઠોર — minimal વિચલન</strong></td><td>વિચલન &lt;3 mm અથવા span/300 સુધી keep રેખા અને લેવલ</td><td>No bulged દિવાલ/સ્લેબ, fair ફેસ</td></tr><tr><td><strong>3. Leak-proof — tight સાંધાઓ</strong></td><td>સાંધાઓ sealed સાથે foam/ટેપ, grout tight</td><td>No grout loss → no honeycomb, મજબૂતાઈ maintained</td></tr><tr><td><strong>4. Smooth ફેસ</strong></td><td>Plywood 12 mm સાથે film, સ્ટીલ plates</td><td>સારી finish less plaster, easy de-shutter</td></tr><tr><td><strong>5. Light & handleable</strong></td><td>Aluminium અથવા plywood panels 1.2×2.4 m man-handleable</td><td>Speed, ક્રેન નહીં needed નીચી ઊંચાઈ</td></tr><tr><td><strong>6. Easy સુધી સ્ટ્રીપ વગર damage</strong></td><td>Oiled સાથે shuttering oil, taper, સાચું striking time — બાજુઓ 24 h, slabs 14 d, બીમો 21 d પ્રતિ છે 456</td><td>કોંક્રિટ નહીં damaged, panels reusable 50+ times સ્ટીલ</td></tr><tr><td><strong>7. Accurate સુધી size, પ્લમ્બ અને લેવલ</strong></td><td>Within ±5 mm vertical ±3 mm જાડાઈ, checked સાથે પ્લમ્બ અને લેવલ</td><td>Structural ચોકસાઈ</td></tr><tr><td><strong>8. Reusable & કરકસરભર્યું</strong></td><td>Standard module sizes સુધી repeat માળ-સુધી-માળ</td><td>Cost પ્રતિ ઉપયોગ નીચી</td></tr></table>
<p><strong>Materials:</strong> Traditional timber, plywood સાથે timber battens, સ્ટીલ panels માટે mass, aluminium માટે fast cycle, plastic માટે નાની repeats. Choice balancing characteristic vs cost.</p>
<div class="eq"><strong>Answer:</strong> 8 characteristics તરીકે ટેબલ — strong, કઠોર, leak-proof, smooth, light, easy સ્ટ્રીપ, accurate, reusable — સાથે limits અને striking times માટે full 7 marks.</div>""",
  },
 ],
},
{
 "title_en":'Q2 · Foundations, cofferdam, piles, caisson, timbering',
 "title_gu":'પ્ર.2 · પાયા, કોફરડેમ, પાઇલ, કેશન, ટિમ્બરિંગ',
 "cards":[
  {
   "q_en":'Q.2 (a) List out the Types of Shallow Foundation and Deep Foundations. (03 marks)',
   "marks_en":'03 marks',"marks_gu":'૦૩ ગુણ',
   "a_en":f"""<p><strong>Shallow Df ≤ B:</strong> Strip/wall footing, Isolated spread, Combined, Cantilever/strap, Raft/mat, Inverted arch.</p><p><strong>Deep Df &gt; B:</strong> Driven/bored pile, Under-reamed pile, Well/caisson, Pier, Pile cap groups. Chosen when top soil weak, heavy load, black cotton active zone deep.</p>"""+fig(svg_found,'Shallow wall/isolated/raft bear near surface vs deep pile/caisson go deep'),
   "a_gu":f"""<p><strong>છીછરો Df ≤ B:</strong> સ્ટ્રીપ/દિવાલ ફૂટિંગ, આઇસોલેટેડ spread, કમ્બાઇન્ડ, કેન્ટીલીવર/strap, રાફ્ટ/મેટ, Inverted arch.</p><p><strong>ઊંડો Df &gt; B:</strong> Driven/bored પાઈલ, અંડર-રીમ્ડ પાઈલ, Well/caisson, Pier, પાઈલ cap groups. Chosen જ્યારે top માટી weak, heavy ભાર, કાળી કપાસ સક્રિય ક્ષેત્ર ઊંડો.</p>"""+fig(svg_found,'છીછરો દિવાલ/આઇસોલેટેડ/રાફ્ટ bear નજીક સપાટી vs ઊંડો પાઈલ/caisson go ઊંડો'),
  },
  {
   "q_en":'Q.2 (b) Draw Neat Sketch of RCC Footing for Brick Masonary Wall. (04 marks)',
   "marks_en":'04 marks',"marks_gu":'૦૪ ગુણ',
   "a_en":'<p>Wall 200 mm on RCC footing: PCC lean 100 mm, RCC base 900 mm wide × 300 mm thick, wall offset 150 mm each side, 8 mm @150 c/c distribution + 10 mm @150 main steel, 50 mm cover, plinth beam above. Bearing pressure ≤ SBC 150 kN/m2.</p>',
   "a_gu":'<p>દિવાલ 200 mm પર RCC ફૂટિંગ: PCC lean 100 mm, RCC base 900 mm wide × 300 mm thick, દિવાલ offset 150 mm દરેક બાજુ, 8 mm @150 c/c વિતરણ + 10 mm @150 main સ્ટીલ, 50 mm આવરી લે, plinth બીમ ઉપર. બેરિંગ pressure ≤ SBC 150 kN/m2.</p>',
  },
  {
   "q_en":'Q.2 (c) Enlist Types of coffer Dams, Draw neat Sketch of Rock Fill Crib Cofferdam. (07 marks)',
   "marks_en":'07 marks',"marks_gu":'૦૭ ગુણ',
   "a_en":f"""<div class="eq"><strong>Concept:</strong> Cofferdam is temporary watertight enclosure to work dry in water for pier, foundation — pump out inside, keep water out.</div>
<table><tr><th>Type of cofferdam</th><th>Water depth / soil suitable</th><th>Key feature</th></tr><tr><td>1. Earthen embankment</td><td>Shallow 1–3 m low flow</td><td>Cheap mud puddle</td></tr><tr><td>2. Rock fill</td><td>3–10 m fast current</td><td>Boulders resist scour</td></tr><tr><td>3. Single wall sheet pile</td><td>Moderate depth</td><td>Interlocked sheet piles driven, wales+struts</td></tr><tr><td>4. Double wall sheet pile</td><td>Deep 6–12 m</td><td>Two walls with fill between, more stable</td></tr><tr><td>5. <strong>Rock fill crib — to detail</strong></td><td>6–10 m rock bed, strong current</td><td>Timber cribs 2×2 m filled boulders, puddle clay on water side watertight</td></tr><tr><td>6. Cellular steel</td><td>Very deep 10–20 m + hard bed</td><td>Circular cells filled sand, self stable</td></tr><tr><td>7. Pneumatic caisson as coffer</td><td>Very deep pressurised</td><td>Compressed air keeps water out</td></tr></table>
<p><strong>Rock fill crib in detail — 7 steps:</strong> 1) Prefab timber cribs 2×2×1.5 m on shore, 2) Float / place in line around work area on rock bed, 3) Fill each crib with 200–300 mm boulders for weight, 4) On water side pack puddle clay 300 mm + polythene for impermeability, 5) Brace cribs together with ties, 6) Dewater inside with pumps, 7) Excavate to rock and construct pier dry. Advantages: Uses local rock, resists current and waves, timber reusable, no deep sheet driving on rock. Disadvantage: Needs rock bed to seat, bulky.</p>
<div class="eq"><strong>Answer:</strong> 7 types listed, Rock fill crib detailed as timber cribs filled boulders + puddle clay water side for 6–10 m deep flow — with sketch.</div>""",
   "a_gu":f"""<div class="eq"><strong>સિદ્ધાંત:</strong> Cofferdam છે temporary watertight enclosure સુધી work dry માં પાણી માટે pier, પાયો — પંપ out inside, keep પાણી out.</div>
<table><tr><th>Type નો cofferdam</th><th>પાણી depth / માટી suitable</th><th>Key feature</th></tr><tr><td>1. Earthen embankment</td><td>છીછરો 1–3 m નીચી flow</td><td>Cheap mud puddle</td></tr><tr><td>2. Rock ભરો</td><td>3–10 m fast current</td><td>Boulders resist scour</td></tr><tr><td>3. સિંગલ દિવાલ sheet પાઈલ</td><td>Moderate depth</td><td>Interlocked sheet પાઈલ્સ driven, wales+struts</td></tr><tr><td>4. ડબલ દિવાલ sheet પાઈલ</td><td>ઊંડો 6–12 m</td><td>Two દિવાલો સાથે ભરો વચ્ચે, વધુ stable</td></tr><tr><td>5. <strong>Rock ભરો crib — સુધી detail</strong></td><td>6–10 m rock bed, strong current</td><td>Timber cribs 2×2 m filled boulders, puddle clay પર પાણી બાજુ watertight</td></tr><tr><td>6. Cellular સ્ટીલ</td><td>ખૂબ ઊંડો 10–20 m + hard bed</td><td>Circular cells filled રેતી, self stable</td></tr><tr><td>7. Pneumatic caisson તરીકે coffer</td><td>ખૂબ ઊંડો pressurised</td><td>Compressed air keeps પાણી out</td></tr></table>
<p><strong>Rock ભરો crib માં detail — 7 steps:</strong> 1) Prefab timber cribs 2×2×1.5 m પર shore, 2) Float / place માં રેખા around work વિસ્તાર પર rock bed, 3) ભરો દરેક crib સાથે 200–300 mm boulders માટે વજન, 4) પર પાણી બાજુ pack puddle clay 300 mm + polythene માટે impermeability, 5) Brace cribs together સાથે ties, 6) Dewater inside સાથે pumps, 7) Excavate સુધી rock અને construct pier dry. Advantages: Uses સ્થાનિક rock, resists current અને waves, timber reusable, no ઊંડો sheet driving પર rock. Disadvantage: Needs rock bed સુધી seat, bulky.</p>
<div class="eq"><strong>Answer:</strong> 7 types listed, Rock ભરો crib detailed તરીકે timber cribs filled boulders + puddle clay પાણી બાજુ માટે 6–10 m ઊંડો flow — સાથે sketch.</div>""",
  },
  {
   "q_en":'Q.2 (a) OR Explain End bearing Pile with Sketch. (03 marks)',
   "marks_en":'03 marks',"marks_gu":'૦૩ ગુણ',
   "a_en":f"""<p>End bearing pile acts as column — tip rests on hard rock/dense sand, load transferred mainly by point bearing. Friction negligible. Length up to rock, diameter 300–600 mm, safe load 500–1500 kN. Uses: high load to rock within 20 m.</p>"""+fig(svg_ureamed,'End bearing pile tip on hard strata acts as column'),
   "a_gu":f"""<p>End બેરિંગ પાઈલ acts તરીકે કોલમ — tip rests પર hard rock/dense રેતી, ભાર transferred mainly દ્વારા બિંદુ બેરિંગ. Friction negligible. Length up સુધી rock, diameter 300–600 mm, safe ભાર 500–1500 kN. Uses: ઊંચી ભાર સુધી rock within 20 m.</p>"""+fig(svg_ureamed,'End બેરિંગ પાઈલ tip પર hard strata acts તરીકે કોલમ'),
  },
  {
   "q_en":'Q.2 (b) OR Draw neat Sketch of Box Caisson. (04 marks)',
   "marks_en":'04 marks',"marks_gu":'૦૪ ગુણ',
   "a_en":'<p>Box caisson is open at top closed at bottom — RCC box floated to site, sunk onto prepared rock bed, filled with sand/concrete. No dewatering of bottom. For bridge piers, wharves where rock at bed level.</p>',
   "a_gu":'<p>Box caisson છે ખુલ્લો પર top closed પર bottom — RCC box floated સુધી સાઇટ, sunk onto prepared rock bed, filled સાથે રેતી/કોંક્રિટ. No dewatering નો bottom. માટે bridge piers, wharves જ્યાં rock પર bed લેવલ.</p>',
  },
  {
   "q_en":'Q.2 (c) OR Write Short note on Timbering of Trenches. (07 marks)',
   "marks_en":'07 marks',"marks_gu":'૦૭ ગુણ',
   "a_en":f"""<div class="eq"><strong>Concept:</strong> Timbering supports trench sides to prevent collapse in loose, water-charged or deep &gt;1.5 m soil — safety for workers + adjacent structures.</div>
<table><tr><th>Method / System</th><th>Soil / depth suitable</th><th>Components as labelled in sketch</th></tr><tr><td><strong>1. Stay bracing — most common</strong></td><td>Firm to loose 1.5–3 m</td><td>Poling boards 200×35 mm vertical, wallings horizontal 100×100 mm, struts 100×100 mm wedged 1.5 m c/c</td></tr><tr><td>2. Box sheeting</td><td>Loose running 3–4 m</td><td>Horizontal sheeting full facing, vertical wallings, struts</td></tr><tr><td>3. Vertical sheeting</td><td>Deep loose with water</td><td>Vertical sheets driven before excavation, horizontal wallings</td></tr><tr><td>4. Runners for running sand</td><td>Very loose sand running</td><td>Pointed boards driven as excavation proceeds, advanced ahead</td></tr></table>
<p><strong>Procedure stepwise 6 steps:</strong> 1) Excavate 1.2 m lift, 2) Place poling boards against sides, 3) Set wallings behind boards, 4) Insert struts and wedge tight with wedges, 5) Excavate next 1.2 m repeat, 6) After pipe laying backfill in layers and remove timber bottom-up, never leave voids. Safety: Keep excavated spoil 1 m away, ladder every 7.5 m, pump water, no worker below unsecured side.</p>
<div class="eq"><strong>Answer:</strong> 4 systems — Stay bracing common — components poling boards + wallings + struts 1.5 m c/c, steps as above, bottom-up removal — with sketch.</div>"""+fig(svg_timber,'Timbering trenches — poling boards vertical, wallings horizontal, struts 100×100 wedged 1.5 m c/c, steps'),
   "a_gu":f"""<div class="eq"><strong>સિદ્ધાંત:</strong> Timbering supports ખાઈ બાજુઓ સુધી prevent collapse માં loose, પાણી-charged અથવા ઊંડો &gt;1.5 m માટી — સલામતી માટે workers + adjacent structures.</div>
<table><tr><th>Method / System</th><th>માટી / depth suitable</th><th>Components તરીકે labelled માં sketch</th></tr><tr><td><strong>1. Stay bracing — સૌથી વધુ common</strong></td><td>Firm સુધી loose 1.5–3 m</td><td>Poling boards 200×35 mm vertical, wallings સમક્ષિતિજ 100×100 mm, struts 100×100 mm wedged 1.5 m c/c</td></tr><tr><td>2. Box sheeting</td><td>Loose running 3–4 m</td><td>સમક્ષિતિજ sheeting full facing, vertical wallings, struts</td></tr><tr><td>3. Vertical sheeting</td><td>ઊંડો loose સાથે પાણી</td><td>Vertical sheets driven પહેલા ખોદકામ, સમક્ષિતિજ wallings</td></tr><tr><td>4. Runners માટે running રેતી</td><td>ખૂબ loose રેતી running</td><td>Pointed boards driven તરીકે ખોદકામ proceeds, advanced ahead</td></tr></table>
<p><strong>Procedure stepwise 6 steps:</strong> 1) Excavate 1.2 m lift, 2) Place poling boards against બાજુઓ, 3) Set wallings behind boards, 4) Insert struts અને wedge tight સાથે wedges, 5) Excavate પછીનું 1.2 m repeat, 6) પછી pipe laying backfill માં layers અને remove timber bottom-up, never leave voids. સલામતી: Keep excavated spoil 1 m away, ladder દરેક 7.5 m, પંપ પાણી, no worker નીચે unsecured બાજુ.</p>
<div class="eq"><strong>Answer:</strong> 4 systems — Stay bracing common — components poling boards + wallings + struts 1.5 m c/c, steps તરીકે ઉપર, bottom-up removal — સાથે sketch.</div>"""+fig(svg_timber,'Timbering trenches — poling boards vertical, wallings સમક્ષિતિજ, struts 100×100 wedged 1.5 m c/c, steps'),
  },
 ],
},
{
 "title_en":'Q3 · Masonry, bonds, concrete, plaster',
 "title_gu":'પ્ર.3 · ચણતર, બોન્ડ, કોંક્રિટ, પ્લાસ્ટર',
 "cards":[
  {
   "q_en":'Q.3 (a) Define with sketch: Frog, Header, Stretcher. (03 marks)',
   "marks_en":'03 marks',"marks_gu":'૦૩ ગુણ',
   "a_en":f"""<p><strong>Frog:</strong> 10 mm deep depression 100×40 mm on top face of brick for key with mortar, also marks top. <strong>Header:</strong> Short end face 90×90 mm visible when brick laid width-wise. <strong>Stretcher:</strong> Long face 190×90 mm visible when laid length-wise.</p>"""+fig(svg_bonds,'Frog depression, header short face, stretcher long face — helps break vertical joints'),
   "a_gu":f"""<p><strong>Frog:</strong> 10 mm ઊંડો depression 100×40 mm પર top ફેસ નો ઈંટ માટે key સાથે mortar, પણ marks top. <strong>હેડર:</strong> ટૂંકી end ફેસ 90×90 mm visible જ્યારે ઈંટ laid width-wise. <strong>સ્ટ્રેચર:</strong> લાંબી ફેસ 190×90 mm visible જ્યારે laid length-wise.</p>"""+fig(svg_bonds,'Frog depression, હેડર ટૂંકી ફેસ, સ્ટ્રેચર લાંબી ફેસ — helps break vertical સાંધાઓ'),
  },
  {
   "q_en":'Q.3 (b) Draw neat sketch of English Bond for Brick thick wall. (04 marks)',
   "marks_en":'04 marks',"marks_gu":'૦૪ ગુણ',
   "a_en":'<p>Strongest bond: alternate courses all headers then all stretchers. Vertical joints broken by queen closer next to quoin header. Lap 1/4 brick. For 200 mm wall: course 1 headers, course 2 stretchers. Minimum crushing strength.</p>',
   "a_gu":'<p>Strongest બોન્ડ: alternate courses બધા headers પછી બધા stretchers. Vertical સાંધાઓ broken દ્વારા queen closer પછીનું સુધી quoin હેડર. Lap 1/4 ઈંટ. માટે 200 mm દિવાલ: course 1 headers, course 2 stretchers. Minimum crushing મજબૂતાઈ.</p>',
  },
  {
   "q_en":'Q.3 (c) List out Ingredients of Concrete. Explain Compaction of Concrete. (07 marks)',
   "marks_en":'07 marks',"marks_gu":'૦૭ ગુણ',
   "a_en":f"""<div class="eq"><strong>Ingredients of concrete:</strong> Cement OPC/PPC binder, Fine aggregate river sand Zone I-III for workability, Coarse aggregate 10–20 mm for strength, Clean potable water w/c 0.4–0.5, Admixtures plasticizer/retarder/air entrainer as needed. Ratio M20 1:1.5:3 etc.</div>
<table><tr><th>Compaction aspect</th><th>Why needed</th><th>Method stepwise</th><th>Precaution</th></tr><tr><td><strong>Purpose</strong></td><td>Remove entrapped 5–8% air to achieve full density, ensure aggregate-cement contact, avoid honeycomb, get strength</td><td> — </td><td>Without compaction strength 30% low</td></tr><tr><td><strong>Hand tamping/roding</strong></td><td>Plain unreinforced small works</td><td>16 mm rod 25 blows per layer 300 mm thick</td><td>Limited depth</td></tr><tr><td><strong>Needle / Internal vibrator — main for RCC</strong></td><td>Beams, columns, footings heavily reinforced</td><td>25–40 mm needle inserted vertical 400–500 mm apart, 30–60 sec till cement slurry rises and air bubbles stop, withdraw slowly</td><td>Over-vibration segregation, under-vibration honeycomb; insert spacing 1.5× radius</td></tr><tr><td><strong>Surface vibrator</strong></td><td>Slabs, roads thickness &lt;150 mm</td><td>Screed vibrator dragged on surface, layer 150–200 mm</td><td>Uniform pass</td></tr><tr><td><strong>Table / Form vibrator</strong></td><td>Precast small elements</td><td>Mould on vibrating table 3000 rpm</td><td>Clamp mould</td></tr></table>
<p><strong>Process as per IS 456:</strong> Place in layers 300–450 mm, compact each before next, needle penetrates 100 mm into previous, do within initial setting 30 min, cure 7 days. Test by slump 75–100 mm for RCC indicates correct w/c and compaction.</p>
<div class="eq"><strong>Answer:</strong> Ingredients 5 as above + compaction purpose, 4 methods — hand, needle internal main 30–60 sec, surface, table — with stepwise procedure and precautions for 7 marks.</div>""",
   "a_gu":f"""<div class="eq"><strong>Ingredients નો કોંક્રિટ:</strong> સિમેન્ટ OPC/PPC binder, Fine એગ્રિગેટ river રેતી ક્ષેત્ર I-III માટે workability, Coarse એગ્રિગેટ 10–20 mm માટે મજબૂતાઈ, Clean potable પાણી w/c 0.4–0.5, Admixtures plasticizer/retarder/air entrainer તરીકે needed. ગુણોત્તર M20 1:1.5:3 etc.</div>
<table><tr><th>કોમ્પેક્શન aspect</th><th>Why needed</th><th>Method stepwise</th><th>Precaution</th></tr><tr><td><strong>હેતુ</strong></td><td>Remove entrapped 5–8% air સુધી achieve full density, ensure એગ્રિગેટ-સિમેન્ટ contact, avoid honeycomb, get મજબૂતાઈ</td><td> — </td><td>વગર કોમ્પેક્શન મજબૂતાઈ 30% નીચી</td></tr><tr><td><strong>Hand tamping/roding</strong></td><td>Plain અનરિઇન્ફોર્સ્ડ નાની works</td><td>16 mm રોડ 25 blows પ્રતિ layer 300 mm thick</td><td>Limited depth</td></tr><tr><td><strong>નીડલ / Internal vibrator — main માટે RCC</strong></td><td>બીમો, કોલમો, footings heavily reinforced</td><td>25–40 mm નીડલ inserted vertical 400–500 mm apart, 30–60 sec till સિમેન્ટ slurry rises અને air bubbles stop, withdraw slowly</td><td>ઉપર-vibration segregation, અંડર-vibration honeycomb; insert spacing 1.5× radius</td></tr><tr><td><strong>સપાટી vibrator</strong></td><td>Slabs, roads જાડાઈ &lt;150 mm</td><td>Screed vibrator dragged પર સપાટી, layer 150–200 mm</td><td>એકસરખું pass</td></tr><tr><td><strong>ટેબલ / Form vibrator</strong></td><td>Precast નાની elements</td><td>Mould પર vibrating ટેબલ 3000 rpm</td><td>ક્લેમ્પ mould</td></tr></table>
<p><strong>Process તરીકે પ્રતિ છે 456:</strong> Place માં layers 300–450 mm, compact દરેક પહેલા પછીનું, નીડલ penetrates 100 mm into previous, do within initial setting 30 min, cure 7 days. Test દ્વારા slump 75–100 mm માટે RCC indicates સાચું w/c અને કોમ્પેક્શન.</p>
<div class="eq"><strong>Answer:</strong> Ingredients 5 તરીકે ઉપર + કોમ્પેક્શન હેતુ, 4 methods — hand, નીડલ internal main 30–60 sec, સપાટી, ટેબલ — સાથે stepwise procedure અને precautions માટે 7 marks.</div>""",
  },
  {
   "q_en":'Q.3 (a) OR Define with sketch: King Closer, Queen Closer, Half Bat (03 marks)',
   "marks_en":'03 marks',"marks_gu":'૦૩ ગુણ',
   "a_en":'<p><strong>King closer:</strong> Brick cut diagonally from header centre to stretcher centre — half header half stretcher. <strong>Queen closer:</strong> Cut longitudinally into two halves 95 mm wide — placed next to quoin. <strong>Half bat:</strong> Cut across length — half length 95 mm.</p>',
   "a_gu":'<p><strong>King closer:</strong> ઈંટ cut diagonally થી હેડર કેન્દ્ર સુધી સ્ટ્રેચર કેન્દ્ર — half હેડર half સ્ટ્રેચર. <strong>Queen closer:</strong> Cut longitudinally into two halves 95 mm wide — placed પછીનું સુધી quoin. <strong>Half bat:</strong> Cut across length — half length 95 mm.</p>',
  },
  {
   "q_en":'Q.3 (b) OR Write Advantages of Hollow Concrete Block Masonary. (04 marks)',
   "marks_en":'04 marks',"marks_gu":'૦૪ ગુણ',
   "a_en":'<p>Lighter 1/3 weight saves foundation, hollow gives thermal and sound insulation, faster laying large size 400×200, less mortar, cavity reduces damp, earthquake lighter mass, precise size less plaster.</p>',
   "a_gu":'<p>Lighter 1/3 વજન saves પાયો, hollow gives thermal અને sound insulation, faster laying મોટી size 400×200, less mortar, cavity reduces ભેજવાળું, earthquake lighter mass, precise size less plaster.</p>',
  },
  {
   "q_en":'Q.3 (c) OR Explain Method of Applying Sand faced Plaster on Outer Wall. (07 marks)',
   "marks_en":'07 marks',"marks_gu":'૦૭ ગુણ',
   "a_en":f"""<div class="eq"><strong>Concept:</strong> Sand faced plaster is two-coat granular finish for outer wall — weather shedding + rough texture hides unevenness + attractive.</div>
<table><tr><th>Step</th><th>Action detailed</th><th>Mix / Thickness / Tool</th><th>Check</th></tr><tr><td>1. Preparation</td><td>Rake joints 10 mm, hack smooth concrete, clean dust, wet wall 24 h before</td><td>Wire brush, water spray</td><td>Surface damp not dry — suction controlled</td></tr><tr><td>2. Base coat 12 mm — levelling</td><td>Apply 1:4 cement:sand by trowel, rule with straight edge, check plumb, scratch cross lines for key</td><td>12 mm thick, wooden float level</td><td>No undulation &gt;3 mm/2 m</td></tr><tr><td>3. Cure base</td><td>Keep moist 24 h, let set but not hard fully</td><td>Water spray 2–3 times</td><td>Green base bonds better</td></tr><tr><td>4. Finishing coat 8 mm — texture</td><td>1:3 cement:coarse sand 2–3 mm sand, throw/ dash with trowel, then finish with sponge or wooden float in circular motion to expose sand grains uniformly</td><td>8 mm, sponge float, total 20 mm</td><td>Granular texture uniform, no trowel marks, thickness checked with template</td></tr><tr><td>5. Grooving if needed</td><td>Cut 10×10 mm grooves at floor levels for architectural lines</td><td>Groove tool</td><td>Straight lines</td></tr><tr><td>6. Curing</td><td>Water 7 days 2× daily + polythene in hot wind</td><td> — </td><td>No cracks, damp 7 days</td></tr></table>
<p><strong>Why two coats:</strong> Single 20 mm would sag and crack; base levels, finishing gives texture and water shedding.</p>
<div class="eq"><strong>Answer:</strong> 6 steps — prep, 12 mm base 1:4, cure, 8 mm finish 1:3 coarse sand sponge texture, groove, 7-day cure — total 20 mm granular finish for outer wall.</div>""",
   "a_gu":f"""<div class="eq"><strong>સિદ્ધાંત:</strong> રેતી faced plaster છે two-coat granular finish માટે outer દિવાલ — weather shedding + rough texture hides unevenness + attractive.</div>
<table><tr><th>Step</th><th>Action detailed</th><th>મિક્સ / જાડાઈ / Tool</th><th>ચકાસણી</th></tr><tr><td>1. Preparation</td><td>Rake સાંધાઓ 10 mm, hack smooth કોંક્રિટ, clean dust, wet દિવાલ 24 h પહેલા</td><td>Wire brush, પાણી spray</td><td>સપાટી ભેજવાળું નહીં dry — suction controlled</td></tr><tr><td>2. Base coat 12 mm — લેવલિંગ</td><td>Apply 1:4 સિમેન્ટ:રેતી દ્વારા trowel, rule સાથે straight edge, તપાસ પ્લમ્બ, scratch ક્રોસ રેખાઓ માટે key</td><td>12 mm thick, wooden float લેવલ</td><td>No undulation &gt;3 mm/2 m</td></tr><tr><td>3. Cure base</td><td>Keep moist 24 h, let set but નહીં hard fully</td><td>પાણી spray 2–3 times</td><td>Green base બોન્ડ્સ better</td></tr><tr><td>4. Finishing coat 8 mm — texture</td><td>1:3 સિમેન્ટ:coarse રેતી 2–3 mm રેતી, throw/ dash સાથે trowel, પછી finish સાથે sponge અથવા wooden float માં circular motion સુધી expose રેતી grains uniformly</td><td>8 mm, sponge float, કુલ 20 mm</td><td>Granular texture એકસરખું, no trowel marks, જાડાઈ checked સાથે template</td></tr><tr><td>5. Grooving જો needed</td><td>Cut 10×10 mm grooves પર માળ levels માટે architectural રેખાઓ</td><td>Groove tool</td><td>Straight રેખાઓ</td></tr><tr><td>6. ક્યુરિંગ</td><td>પાણી 7 days 2× daily + polythene માં hot wind</td><td> — </td><td>No તિરાડો, ભેજવાળું 7 days</td></tr></table>
<p><strong>Why two coats:</strong> સિંગલ 20 mm would sag અને તિરાડ; base levels, finishing gives texture અને પાણી shedding.</p>
<div class="eq"><strong>Answer:</strong> 6 steps — prep, 12 mm base 1:4, cure, 8 mm finish 1:3 coarse રેતી sponge texture, groove, 7-day cure — કુલ 20 mm granular finish માટે outer દિવાલ.</div>""",
  },
 ],
},
{
 "title_en":'Q4 · Damp, DPC, machinery, joints, equipment',
 "title_gu":'પ્ર.4 · ભીનાશ, DPC, મશીનરી, સાંધા',
 "cards":[
  {
   "q_en":'Q.4 (a) Explain Anti Termite treatment. (03 marks)',
   "marks_en":'03 marks',"marks_gu":'૦૩ ગુણ',
   "a_en":'<p>Chemical barrier of chlorpyrifos 1% or imidacloprid under and around building. Process: trench 30 cm deep around foundation, soil treatment 7.5 L/m2, pit bottom 5 L/m2 before PCC, plinth junction, pipe entry sealed. Blocks termite path from ground to wood.</p>',
   "a_gu":'<p>Chemical barrier નો chlorpyrifos 1% અથવા imidacloprid અંડર અને around building. Process: ખાઈ 30 cm ઊંડો around પાયો, માટી treatment 7.5 L/m2, pit bottom 5 L/m2 પહેલા PCC, plinth junction, pipe entry sealed. Blocks termite માર્ગ થી ground સુધી wood.</p>',
  },
  {
   "q_en":'Q.4 (b) Draw neat Sketch for DPC of Basement. (04 marks)',
   "marks_en":'04 marks',"marks_gu":'૦૪ ગુણ',
   "a_en":f"""<p>Basement needs continuous waterproof envelope: 40 mm cement concrete 1:2:4 + waterproof compound on base slab, 20 mm bitumen mastic vertical on retaining wall tied to horizontal DPC at plinth with 150 mm lap, weep holes. No break at junctions.</p>"""+fig(svg_dpc,'Basement DPC — horizontal on base slab + vertical on retaining wall continuous, no break'),
   "a_gu":f"""<p>Basement needs continuous waterproof envelope: 40 mm સિમેન્ટ કોંક્રિટ 1:2:4 + waterproof compound પર base સ્લેબ, 20 mm bitumen mastic vertical પર retaining દિવાલ tied સુધી સમક્ષિતિજ DPC પર plinth સાથે 150 mm lap, weep holes. No break પર junctions.</p>"""+fig(svg_dpc,'Basement DPC — સમક્ષિતિજ પર base સ્લેબ + vertical પર retaining દિવાલ continuous, no break'),
  },
  {
   "q_en":'Q.4 (c) Explain factor affecting selection of Construction Machineries. (07 marks)',
   "marks_en":'07 marks',"marks_gu":'૦૭ ગુણ',
   "a_en":f"""<div class="eq"><strong>Concept:</strong> Machinery = 25–40% of project cost — wrong choice = delay + cost overrun; selection balances work, ground, access, time, cost.</div>
<table><tr><th>Factor</th><th>What to check</th><th>Example decision</th></tr><tr><td>1. Nature & quantity of work</td><td>Earthwork vs concreting vs lifting, volume m3</td><td>Mass dam 10000 m3 → scraper + dozer not manual</td></tr><tr><td>2. Site topography & access</td><td>Hill slope, narrow lane 3 m, headroom</td><td>Congested 1.2 m gap → mini excavator not large</td></tr><tr><td>3. Soil / rock type</td><td>Hard rock blast vs soft clay</td><td>Rock → ripper + breaker, clay → sheep foot roller</td></tr><tr><td>4. Depth / height & reach</td><td>Excav depth 6 m, lift height 30 m</td><td>Deep trench → backhoe not dozer; high lift → tower crane not mobile</td></tr><tr><td>5. Time schedule</td><td>Duration months, working hours</td><td>Tight 30 days → high capacity 120 m3/h plant</td></tr><tr><td>6. Cost — hire vs buy / fuel vs electric</td><td>Ownership cost per hour = depreciation+fuel+operator</td><td>Short 2 months → hire, long 1 year → buy</td></tr><tr><td>7. Availability, spares, operator skill</td><td>Service network, spare parts lead time</td><td>Caterpillar dealer near site → reliable</td></tr><tr><td>8. Safety, noise, environment</td><td>Urban night work noise &lt;75 dB, emission Bharat IV</td><td>Electric mini not diesel in basement</td></tr><tr><td>9. Weather / working conditions</td><td>Rain, wind, water table high</td><td>High water → dewatering pumps + coffer</td></tr></table>
<div class="eq"><strong>Answer:</strong> 9 factors stepwise — work nature, site access, soil, depth/height, time, cost, availability, safety/environment, weather — with example as table for 7 marks.</div>""",
   "a_gu":f"""<div class="eq"><strong>સિદ્ધાંત:</strong> Machinery = 25–40% નો project cost — ખોટું choice = delay + cost overrun; selection balances work, ground, access, time, cost.</div>
<table><tr><th>Factor</th><th>What સુધી તપાસ</th><th>Example decision</th></tr><tr><td>1. Nature & quantity નો work</td><td>Earthwork vs concreting vs lifting, volume m3</td><td>Mass dam 10000 m3 → સ્ક્રેપર + ડોઝર નહીં manual</td></tr><tr><td>2. સાઇટ topography & access</td><td>Hill slope, narrow lane 3 m, headroom</td><td>Congested 1.2 m gap → mini એક્સ્કેવેટર નહીં મોટી</td></tr><tr><td>3. માટી / rock type</td><td>Hard rock blast vs soft clay</td><td>Rock → ripper + breaker, clay → sheep foot રોલર</td></tr><tr><td>4. Depth / ઊંચાઈ & reach</td><td>Excav depth 6 m, lift ઊંચાઈ 30 m</td><td>ઊંડો ખાઈ → બેકહો નહીં ડોઝર; ઊંચી lift → tower ક્રેન નહીં mobile</td></tr><tr><td>5. Time schedule</td><td>Duration months, working hours</td><td>Tight 30 days → ઊંચી ક્ષમતા 120 m3/h પ્લાન્ટ</td></tr><tr><td>6. Cost — hire vs buy / fuel vs electric</td><td>Ownership cost પ્રતિ hour = depreciation+fuel+operator</td><td>ટૂંકી 2 months → hire, લાંબી 1 year → buy</td></tr><tr><td>7. Availability, spares, operator skill</td><td>Service network, spare parts lead time</td><td>Caterpillar dealer નજીક સાઇટ → reliable</td></tr><tr><td>8. સલામતી, noise, environment</td><td>Urban night work noise &lt;75 dB, emission Bharat IV</td><td>Electric mini નહીં diesel માં basement</td></tr><tr><td>9. Weather / working conditions</td><td>Rain, wind, પાણી ટેબલ ઊંચી</td><td>ઊંચી પાણી → dewatering pumps + coffer</td></tr></table>
<div class="eq"><strong>Answer:</strong> 9 factors stepwise — work nature, સાઇટ access, માટી, depth/ઊંચાઈ, time, cost, availability, સલામતી/environment, weather — સાથે example તરીકે ટેબલ માટે 7 marks.</div>""",
  },
  {
   "q_en":'Q.4 (a) OR Explain Construction Joints. (03 marks)',
   "marks_en":'03 marks',"marks_gu":'૦૩ ગુણ',
   "a_en":'<p>Joints where fresh concrete placed against hardened after pause &gt;30 min. Toothed or dowelled for continuity, placed at low shear zone, cleaned and bonding slurry applied. Water bar in water tanks.</p>',
   "a_gu":'<p>સાંધાઓ જ્યાં fresh કોંક્રિટ placed against hardened પછી pause &gt;30 min. Toothed અથવા dowelled માટે continuity, placed પર નીચી shear ક્ષેત્ર, cleaned અને bonding slurry applied. પાણી bar માં પાણી tanks.</p>',
  },
  {
   "q_en":'Q.4 (b) OR Enlist Safety Points for plumbing Work. (04 marks)',
   "marks_en":'04 marks',"marks_gu":'૦૪ ગુણ',
   "a_en":'<p>Wear PPE gloves goggles, shoring of trenches &gt;1.5 m, no open flame for solvent, pressure test at 1.5× working slowly, keep valves accessible, ventilate, lock pumps during repair.</p>',
   "a_gu":'<p>Wear PPE ગ્લોવ્સ goggles, shoring નો trenches &gt;1.5 m, no ખુલ્લો flame માટે solvent, pressure test પર 1.5× working slowly, keep valves accessible, ventilate, lock pumps દરમિયાન repair.</p>',
  },
  {
   "q_en":'Q.4 (c) OR Write short note on Clam shell. (07 marks)',
   "marks_en":'07 marks',"marks_gu":'૦૭ ગુણ',
   "a_en":f"""<div class="eq"><strong>Concept:</strong> Clam shell is grab bucket with two hinged halves like clam — suspended by crane cable for vertical digging where other excavators cannot reach deep narrow.</div>
<table><tr><th>Aspect</th><th>Details</th></tr><tr><td>Construction</td><td>Two buckets hinged at top, weight 500–2000 kg, volume 0.5–2.0 m3, tagline prevents spinning, crane boom 15–30 m</td></tr><tr><td>Working cycle 5 steps</td><td>1. Open buckets 2. Drop by gravity to bottom 3. Close by pulling closing cable — grabs 0.5–2 m3 soil 4. Lift up 5. Swing and discharge into dumper</td></tr><tr><td>Depth capability</td><td>Up to 30 m vertical, can work underwater, no slope needed</td></tr><tr><td>Uses</td><td>Deep narrow foundation pits, well sinking, diaphragm wall trench, pile bore spoil removal, under water dredging, handling bulk material</td></tr><tr><td>Advantages</td><td>Reaches great depth vertical, works under water, needs no side approach ramp</td></tr><tr><td>Limitations</td><td>Needs high headroom crane 10 m, slow cycle 2–3 min, not for hard rock needs blasting, skilled operator for tagline control</td></tr></table>
<div class="eq"><strong>Answer:</strong> Clam shell = hinged grab 0.5–2 m3 on crane, cycle open-drop-close-lift-discharge, depth 30 m underwater, uses — deep pits, wells, pile bores, limitations crane headroom as table.</div>""",
   "a_gu":f"""<div class="eq"><strong>સિદ્ધાંત:</strong> Clam shell છે grab bucket સાથે two hinged halves જેવું clam — લટકતું દ્વારા ક્રેન cable માટે vertical digging જ્યાં other excavators ન કરી શકાય reach ઊંડો narrow.</div>
<table><tr><th>Aspect</th><th>વિગતો</th></tr><tr><td>Construction</td><td>Two buckets hinged પર top, વજન 500–2000 kg, volume 0.5–2.0 m3, tagline prevents spinning, ક્રેન boom 15–30 m</td></tr><tr><td>કાર્યપદ્ધતિ cycle 5 steps</td><td>1. ખુલ્લો buckets 2. Drop દ્વારા gravity સુધી bottom 3. Close દ્વારા pulling બંધ cable — grabs 0.5–2 m3 માટી 4. Lift up 5. Swing અને discharge into ડમ્પર</td></tr><tr><td>Depth capability</td><td>Up સુધી 30 m vertical, can work underwater, no slope needed</td></tr><tr><td>Uses</td><td>ઊંડો narrow પાયો pits, well sinking, diaphragm દિવાલ ખાઈ, પાઈલ bore spoil removal, અંડર પાણી dredging, handling bulk material</td></tr><tr><td>Advantages</td><td>Reaches great depth vertical, works અંડર પાણી, needs no બાજુ approach ramp</td></tr><tr><td>Limitations</td><td>Needs ઊંચી headroom ક્રેન 10 m, slow cycle 2–3 min, નહીં માટે hard rock needs blasting, skilled operator માટે tagline નિયંત્રણ</td></tr></table>
<div class="eq"><strong>Answer:</strong> Clam shell = hinged grab 0.5–2 m3 પર ક્રેન, cycle ખુલ્લો-drop-close-lift-discharge, depth 30 m underwater, uses — ઊંડો pits, wells, પાઈલ bores, limitations ક્રેન headroom તરીકે ટેબલ.</div>""",
  },
 ],
},
{
 "title_en":'Q5 · Maintenance, green/prefab, safety',
 "title_gu":'પ્ર.5 · જાળવણી, ગ્રીન/પ્રિફેબ, સલામતી',
 "cards":[
  {
   "q_en":'Q.5 (a) What are the purpose of Maintenance of Buildings ? (03 marks)',
   "marks_en":'03 marks',"marks_gu":'૦૩ ગુણ',
   "a_en":'<p>Retain structural safety and serviceability, prevent decay and damp, keep hygiene and comfort, preserve appearance and value, extend life, reduce major repair cost, meet statutory requirements.</p>',
   "a_gu":'<p>Retain structural સલામતી અને serviceability, prevent decay અને ભેજવાળું, keep hygiene અને comfort, preserve appearance અને value, extend life, reduce major repair cost, meet statutory requirements.</p>',
  },
  {
   "q_en":'Q.5 (b) Write advantages and disadvantages of Green Building Technology. (04 marks)',
   "marks_en":'04 marks',"marks_gu":'૦૪ ગુણ',
   "a_en":'<p><strong>Advantages:</strong> 30–40% energy saving, water harvesting, less CO2, healthy daylight ventilation, waste reduction, long-term low bills, LEED/GRIHA rating value.</p><p><strong>Disadvantages:</strong> 5–15% higher initial cost, needs skilled design, certified materials limited, maintenance training.</p>',
   "a_gu":'<p><strong>Advantages:</strong> 30–40% energy saving, પાણી harvesting, less CO2, healthy daylight ventilation, waste reduction, લાંબી-term નીચી bills, LEED/GRIHA rating value.</p><p><strong>Disadvantages:</strong> 5–15% higher initial cost, needs skilled ડિઝાઇન, certified materials limited, જાળવણી training.</p>',
  },
  {
   "q_en":'Q.5 (c) Explain Physical Causes of Accidents in Construction. (07 marks)',
   "marks_en":'07 marks',"marks_gu":'૦૭ ગુણ',
   "a_en":f"""<div class="eq"><strong>Concept:</strong> Accidents cause = Unsafe act + Unsafe physical condition. Physical causes are hazardous site conditions that invite fall, crush, shock — independent of worker behaviour.</div>
<table><tr><th>Physical unsafe condition</th><th>Example on site</th><th>Accident it causes</th><th>Control</th></tr><tr><td>1. Weak / unbraced scaffolds, platforms</td><td>Ledger spacing &gt;1.8 m, missing bracing, rotten planks, no toe board</td><td>Collapse drop person + material 10 m fatal</td><td>Design scaffold IS 4014, inspect daily</td></tr><tr><td>2. Unguarded edges & floor openings</td><td>Slab edge open, lift shaft uncovered, stair void</td><td>Fall from height</td><td>Guard rail 1 m + mid rail + mesh, cover openings</td></tr><tr><td>3. Faulty ladders & access</td><td>Cracked rungs, too short, not tied, oily steps, no handhold 1 m above landing</td><td>Fall while climbing</td><td>IS ladder, 4:1 slope, tie top, check before use</td></tr><tr><td>4. Defective tools & machines</td><td>Mixer guard missing, chain sling kinked, crane limit switch failed, vibrator insulation broken</td><td>Crush, amputation, electrocution</td><td>Daily check, tag defective red</td></tr><tr><td>5. Falling objects</td><td>Unstacked bricks 3 m high, no nets on scaffold, lifted load over workers</td><td>Struck by falling 2 kg from 10 m = 2000 N</td><td>Stack &lt;1.5 m, nets, hard hats, barricade below lift</td></tr><tr><td>6. Collapse of trench / formwork / stack</td><td>Deep trench &gt;1.5 m unshored, formwork underdesigned for fresh concrete 30 kN/m2</td><td>Bury alive, form burst</td><td>Shoring/strutting, form design check</td></tr><tr><td>7. Electrical naked wires & poor earthing</td><td>Joint open, cable dragged on wet ground, no ELCB 30 mA, lighting 230V bare</td><td>Shock, fire</td><td>Insulated cables, ELCB, 24V hand lamps</td></tr><tr><td>8. Poor housekeeping, lighting, ventilation</td><td>Rebars scattered, oil spill, dark basement, dust, noise &gt;90 dB</td><td>Trip slip, eye/lung disease, fatigue mistake</td><td>Daily cleanup, 50 lux minimum, masks earplugs</td></tr></table>
<p><strong>Heinrich triangle reminder:</strong> For every fatal 29 minor + 300 near-miss from these physical causes — fix condition early.</p>
<div class="eq"><strong>Answer:</strong> 8 physical causes as table — weak scaffold, unguarded edge, faulty ladder, defective tools, falling objects, trench/form collapse, electrical, housekeeping/lighting — with example, accident and control for 7 marks.</div>"""+fig(svg_fail,'Physical causes — weak scaffold, unguarded edge, faulty tools, collapse, electrical, poor housekeeping — conditions cause accidents'),
   "a_gu":f"""<div class="eq"><strong>સિદ્ધાંત:</strong> Accidents cause = Unsafe act + Unsafe physical condition. Physical causes છે hazardous સાઇટ conditions તે invite ફોલ, crush, shock — independent નો worker behaviour.</div>
<table><tr><th>Physical unsafe condition</th><th>Example પર સાઇટ</th><th>અકસ્માત it causes</th><th>નિયંત્રણ</th></tr><tr><td>1. Weak / unbraced scaffolds, platforms</td><td>Ledger spacing &gt;1.8 m, missing bracing, rotten planks, no ટો board</td><td>Collapse drop person + material 10 m fatal</td><td>ડિઝાઇન scaffold છે 4014, inspect daily</td></tr><tr><td>2. Unguarded edges & માળ openings</td><td>સ્લેબ edge ખુલ્લો, lift shaft uncovered, stair void</td><td>ફોલ થી ઊંચાઈ</td><td>Guard rail 1 m + mid rail + mesh, આવરી લે openings</td></tr><tr><td>3. Faulty ladders & access</td><td>Cracked rungs, too ટૂંકી, નહીં tied, oily steps, no handhold 1 m ઉપર landing</td><td>ફોલ while climbing</td><td>છે ladder, 4:1 slope, tie top, તપાસ પહેલા ઉપયોગ</td></tr><tr><td>4. Defective tools & machines</td><td>મિક્સર guard missing, સાંકળ sling kinked, ક્રેન limit switch failed, vibrator insulation broken</td><td>Crush, amputation, electrocution</td><td>Daily તપાસ, tag defective red</td></tr><tr><td>5. Falling objects</td><td>Unstacked ઈંટો 3 m ઊંચી, no nets પર scaffold, lifted ભાર ઉપર workers</td><td>Struck દ્વારા falling 2 kg થી 10 m = 2000 N</td><td>Stack &lt;1.5 m, nets, hard hats, barricade નીચે lift</td></tr><tr><td>6. Collapse નો ખાઈ / formwork / stack</td><td>ઊંડો ખાઈ &gt;1.5 m unshored, formwork underdesigned માટે fresh કોંક્રિટ 30 kN/m2</td><td>Bury alive, form burst</td><td>Shoring/strutting, form ડિઝાઇન તપાસ</td></tr><tr><td>7. Electrical naked wires & નબળી earthing</td><td>સાંધો ખુલ્લો, cable dragged પર wet ground, no ELCB 30 mA, lighting 230V bare</td><td>Shock, fire</td><td>Insulated cables, ELCB, 24V hand lamps</td></tr><tr><td>8. નબળી housekeeping, lighting, ventilation</td><td>Rebars scattered, oil spill, dark basement, dust, noise &gt;90 dB</td><td>Trip slip, eye/lung disease, fatigue mistake</td><td>Daily cleanup, 50 lux minimum, masks earplugs</td></tr></table>
<p><strong>Heinrich triangle reminder:</strong> માટે દરેક fatal 29 minor + 300 નજીક-miss થી આ physical causes — fix condition early.</p>
<div class="eq"><strong>Answer:</strong> 8 physical causes તરીકે ટેબલ — weak scaffold, unguarded edge, faulty ladder, defective tools, falling objects, ખાઈ/form collapse, electrical, housekeeping/lighting — સાથે example, અકસ્માત અને નિયંત્રણ માટે 7 marks.</div>"""+fig(svg_fail,'Physical causes — weak scaffold, unguarded edge, faulty tools, collapse, electrical, નબળી housekeeping — conditions cause accidents'),
  },
  {
   "q_en":'Q.5 (a) OR Explain Repairing of Plaster. (03 marks)',
   "marks_en":'03 marks',"marks_gu":'૦૩ ગુણ',
   "a_en":'<p>Mark defective area, cut rectangular edges 10 mm deep, remove loose, clean, wet, apply bonding agent, first 6 mm scratch coat, second flush finishing, cure 7 days. Match existing thickness.</p>',
   "a_gu":'<p>માર્ક defective વિસ્તાર, cut rectangular edges 10 mm ઊંડો, remove loose, clean, wet, apply bonding agent, પ્રથમ 6 mm scratch coat, બીજું flush finishing, cure 7 days. Match existing જાડાઈ.</p>',
  },
  {
   "q_en":'Q.5 (b) OR Write advantages and disadvantages of Pre-Fabricated Construction. (04 marks)',
   "marks_en":'04 marks',"marks_gu":'૦૪ ગુણ',
   "a_en":'<p><strong>Advantages:</strong> Factory quality, fast erection, less site labour and shuttering, weather independent, less waste.</p><p><strong>Disadvantages:</strong> Heavy transport needs crane, joint leakage risk, design rigid, initial mould cost high.</p>',
   "a_gu":'<p><strong>Advantages:</strong> Factory quality, fast erection, less સાઇટ labour અને shuttering, weather independent, less waste.</p><p><strong>Disadvantages:</strong> Heavy transport needs ક્રેન, સાંધો લીકેજ risk, ડિઝાઇન કઠોર, initial mould cost ઊંચી.</p>',
  },
  {
   "q_en":'Q.5 (c) OR Explain Safety in Excavation. (07 marks)',
   "marks_en":'07 marks',"marks_gu":'૦૭ ગુણ',
   "a_en":f"""<div class="eq"><strong>Concept:</strong> Excavation &gt;1.5 m deep loose/water-charged soil can collapse bury workers; falling spoil and no egress also kill — safety prevents trench failure.</div>
<table><tr><th>Safety measure</th><th>How implemented</th><th>Standard / limit</th></tr><tr><td>1. Survey underground utilities before dig</td><td>Trial pits, cable detector, get maps of water/gas/electric</td><td>No damage to live 11 kV</td></tr><tr><td>2. Slope or shoring beyond 1.5 m</td><td>Side slope 1:1 for loose, or timber/steel shoring — poling boards+wallings+struts 1.5 m c/c, runners for running sand</td><td>IS 3764: 1.5 m threshold</td></tr><tr><td>3. Safe access — ladders every 7.5 m</td><td>Mild steel ladder 1 m above edge, secured, lighting 50 lux in deep</td><td>Egress &lt;7.5 m travel, 1 m handhold</td></tr><tr><td>4. Keep spoil + machines away from edge</td><td>Excavated earth stacked 1 m away minimum, no vehicle within 1.5 m</td><td>Surcharge not adds to lateral pressure</td></tr><tr><td>5. Dewatering + prevent water softening</td><td>Sump pumps, well points, divert surface water by bund, stop during heavy rain</td><td>Water pressure zero for stability</td></tr><tr><td>6. Barricades + warning lights</td><td>Hard barricade 1 m from edge, reflective tape, red light at night, watchman</td><td>Public not fall in 2 m deep trench</td></tr><tr><td>7. PPE + daily inspection</td><td>Helmet, safety boots, harness near deep edge, competent person inspects each morning + after rain, tag safe/unsafe</td><td>Stop work if crack &gt;10 mm on top</td></tr><tr><td>8. Adjacent structures — underpin monitor</td><td>If excavation near building, underpin, fix tell-tales, monitor settlement 1 mm/day alarm</td><td>Building not tilted</td></tr></table>
<div class="eq"><strong>Answer:</strong> 8 measures as table — utilities, slope/shoring &gt;1.5 m, ladders 7.5 m, spoil 1 m away, dewatering, barricades/lights, PPE + daily check, adjacent underpin — for 7 marks.</div>"""+fig(svg_excav,'Excavation safety — slope 1:1 or shoring beyond 1.5 m, ladders every 7.5 m, barricades 1 m away, PPE, pumps'),
   "a_gu":f"""<div class="eq"><strong>સિદ્ધાંત:</strong> ખોદકામ &gt;1.5 m ઊંડો loose/પાણી-charged માટી can collapse bury workers; falling spoil અને no egress પણ kill — સલામતી prevents ખાઈ નિષ્ફળતા.</div>
<table><tr><th>સલામતી માપો</th><th>How implemented</th><th>Standard / limit</th></tr><tr><td>1. સર્વે underground utilities પહેલા dig</td><td>Trial pits, cable detector, get maps નો પાણી/gas/electric</td><td>No damage સુધી live 11 kV</td></tr><tr><td>2. Slope અથવા shoring beyond 1.5 m</td><td>બાજુ slope 1:1 માટે loose, અથવા timber/સ્ટીલ shoring — poling boards+wallings+struts 1.5 m c/c, runners માટે running રેતી</td><td>છે 3764: 1.5 m threshold</td></tr><tr><td>3. Safe access — ladders દરેક 7.5 m</td><td>Mild સ્ટીલ ladder 1 m ઉપર edge, secured, lighting 50 lux માં ઊંડો</td><td>Egress &lt;7.5 m travel, 1 m handhold</td></tr><tr><td>4. Keep spoil + machines away થી edge</td><td>Excavated earth stacked 1 m away minimum, no vehicle within 1.5 m</td><td>Surcharge નહીં adds સુધી lateral pressure</td></tr><tr><td>5. Dewatering + prevent પાણી softening</td><td>Sump pumps, well બિંદુઓ, divert સપાટી પાણી દ્વારા bund, stop દરમિયાન heavy rain</td><td>પાણી pressure zero માટે stability</td></tr><tr><td>6. Barricades + warning lights</td><td>Hard barricade 1 m થી edge, reflective ટેપ, red light પર night, watchman</td><td>Public નહીં ફોલ માં 2 m ઊંડો ખાઈ</td></tr><tr><td>7. PPE + daily inspection</td><td>હેલ્મેટ, સલામતી boots, હાર્નેસ નજીક ઊંડો edge, competent person inspects દરેક morning + પછી rain, tag safe/unsafe</td><td>Stop work જો તિરાડ &gt;10 mm પર top</td></tr><tr><td>8. Adjacent structures — underpin monitor</td><td>જો ખોદકામ નજીક building, underpin, fix tell-tales, monitor બેસવું 1 mm/day alarm</td><td>Building નહીં tilted</td></tr></table>
<div class="eq"><strong>Answer:</strong> 8 measures તરીકે ટેબલ — utilities, slope/shoring &gt;1.5 m, ladders 7.5 m, spoil 1 m away, dewatering, barricades/lights, PPE + daily તપાસ, adjacent underpin — માટે 7 marks.</div>"""+fig(svg_excav,'ખોદકામ સલામતી — slope 1:1 અથવા shoring beyond 1.5 m, ladders દરેક 7.5 m, barricades 1 m away, PPE, pumps'),
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
    page=f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>DI03006011 · Winter 2025 solved paper</title><style>{CSS}</style></head><body><main class="page"><header class="hero"><div class="eyebrow">Solved question paper · English questions · Friendly Gujarati answers</div><div class="lang-switch" aria-label="Choose language"><button type="button" data-lang="en" aria-pressed="true">English</button><button type="button" data-lang="gu" aria-pressed="false">ગુજરાતી</button></div><h1>Construction Technology</h1><div class="meta">GTU Diploma · Civil · Semester 3 · Winter 2025 · DI03006011 · 04-12-2025 · 70 marks · 10:30 AM TO 01:00 PM</div></header>{"".join(sections_html)}<div class="footer">Solved paper for study. Verify with standard spec before site use.</div></main><script>document.querySelectorAll('.lang-switch button').forEach(b=>b.addEventListener('click',()=>{{document.documentElement.lang=b.dataset.lang;document.querySelectorAll('.lang-switch button').forEach(x=>x.setAttribute('aria-pressed',x==='true'?'true':'false'));}}));</script></body></html>'''
    return page
def main():
    page=build_page()
    import re
    # strip brackets from Gujarati answers for zero-bracket requirement
    page=re.sub(r'<div class="gu">(.*?)</div>', lambda m: '<div class="gu">'+m.group(1).replace('(','').replace(')','')+'</div>', page, flags=re.S)
    out_papers=ROOT/"papers-upload/papers/DI03006011/winter-2025.html"
    out_ws=ROOT/"preview/workshop/DI03006011_winter2025_bilingual.html"
    out_papers.parent.mkdir(parents=True,exist_ok=True)
    out_ws.parent.mkdir(parents=True,exist_ok=True)
    out_papers.write_text(page,encoding="utf-8")
    out_ws.write_text(page,encoding="utf-8")
    print(f"Bilingual: {out_papers} ({len(page)} chars)")
    en_c = page.count('class="en"'); gu_c = page.count('class="gu"')
    print(f"details={page.count('<details')}, sections={page.count('<section')}, en={en_c}, gu={gu_c}")
    print("PASS" if page.count('<details')==28 and page.count('<section')==5 else "FAIL", f"figs={page.count('<figure>')}")
    import re; pat = r'<div class="gu">(.*?)</div>'; gu=''.join(re.findall(pat,page,re.S)); print(f"brackets gu={gu.count('(')+gu.count(')')}")
    (ROOT/"drive-upload/DI03006011_winter_2025_bilingual.html").write_text(page,encoding="utf-8")
if __name__=="__main__": main()
