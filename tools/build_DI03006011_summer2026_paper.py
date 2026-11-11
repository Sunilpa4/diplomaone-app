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
svg_found=load_svg("ct2_found.svg")
svg_setout=load_svg("ct2_setout.svg")
svg_ureamed=load_svg("ct2_ureamed.svg")
svg_frame=load_svg("ct1_frame.svg")
svg_bonds=load_svg("ct3_bonds.svg")
svg_batch=load_svg("ct4_batch.svg")
svg_fail=load_svg("ct5_fail.svg")
svg_modular=load_svg("ct6_modular.svg")
svg_map=load_svg("ct6_map.svg")
svg_ppe=load_svg("ct5_ppe.svg")

SECTIONS=[
{
 "title_en":"Q1 · Structures, load bearing vs framed, black cotton & settlement",
 "title_gu":"પ્ર.1 · સ્ટ્રક્ચર, ભારવાહી vs ફ્રેમ, કાળી માટી અને સેટલમેન્ટ",
 "cards":[
  {"q_en":"Q.1 (a) Enlist different types of civil engineering structures. (03 marks)","marks_en":"03 marks","marks_gu":"૦૩ ગુણ",
   "a_en":"<p>Civil structures serve living, transport, water, industry: <em>Residential</em> bungalows apartments, <em>Commercial</em> malls offices, <em>Industrial</em> factories warehouses, <em>Water</em> dams canals tanks, <em>Transport</em> roads bridges flyovers tunnels airports ports, <em>Environmental</em> treatment plants. Each has distinct loading and durability needs.</p>",
   "a_gu":"<p>સિવિલ બાંધકામ: રહેણાંક બંગલા, કોમર્શિયલ મોલ, ઔદ્યોગિક ફેક્ટરી, પાણી ડેમ કેનાલ, વાહનવ્યવહાર રસ્તા બ્રિજ ટનલ એરપોર્ટ, પર્યાવરણ પ્લાન્ટ. દરેકને અલગ ભાર ટકાઉપણું.</p>"},
  {"q_en":"Q.1 (b) Differentiate : Load Bearing structure and Framed structure. (04 marks)","marks_en":"04 marks","marks_gu":"૦૪ ગુણ",
   "a_en":"<table><tr><th>Point</th><th>Load bearing</th><th>Framed</th></tr><tr><td>Load path</td><td>Walls transfer slab load directly to foundation — no frame</td><td>RCC columns-beams form rigid frame, walls are non-load infill</td></tr><tr><td>Wall thickness</td><td>200–350 mm, increases downwards</td><td>100–150 mm partition uniform</td></tr><tr><td>Height</td><td>Economical up to 3–4 floors</td><td>High rise 10+ floors possible</td></tr><tr><td>Plan flexibility</td><td>Walls cannot be removed</td><td>Open plan, partitions shiftable</td></tr><tr><td>Earthquake</td><td>Brittle if unreinforced</td><td>Ductile detailing improves safety</td></tr></table>"+fig(svg_frame,"Load bearing walls carry load vs framed columns-beams carry load"),
   "a_gu":"<table><tr><th>મુદ્દો</th><th>ભારવાહી</th><th>ફ્રેમ</th></tr><tr><td>ભાર માર્ગ</td><td>દિવાલ જ સીધી પાયા સુધી</td><td>કોલમ બીમ ફ્રેમ, દિવાલ પૂરક</td></tr><tr><td>જાડાઈ</td><td>200–350 mm</td><td>100–150 mm</td></tr><tr><td>ઊંચાઈ</td><td>3–4 માળ સસ્તી</td><td>ઊંચી, પ્લાન લવચીક</td></tr><tr><td>ભૂકંપ</td><td>બરડ</td><td>ડક્ટાઇલ સલામત</td></tr></table>"+fig(svg_frame,"ભારવાહી vs ફ્રેમ")},
  {"q_en":"Q.1 (c) A site has black cotton soil with high swelling and shrinkage properties. As a site engineer, which type of foundation would you recommend for a single-storey residential building? Justify your selection with reasons. (07 marks)","marks_en":"07 marks","marks_gu":"૦૭ ગુણ",
   "a_en":"<p><strong>Problem:</strong> Black cotton swells on wetting heaves floor, shrinks on drying cracks walls. Active zone 2–3.5 m seasonal movement.</p><p><strong>Recommended:</strong> <em>Under-reamed pile foundation</em> with plinth beam + granular cushion.</p><p>1. Bulbs 2–3 nos at 3–3.5 m depth anchor below active zone, uplift resisted. 2. Pile cap + plinth beam ties building acts as one. 3. 100 mm sand/murrum blanket breaks capillary and swelling pressure. 4. Economical for single storey vs raft — less concrete. Alternative low-cost: Strip raft with CNS cohesive non-swelling soil replacement 1 m + sand.</p><p><strong>Not allowed:</strong> Shallow strip directly on black cotton — severe cracks.</p>"+fig(svg_ureamed,"Under-reamed pile with bulbs below active zone for black cotton soil, plinth beam, granular cushion"),
   "a_gu":"<p><strong>સમસ્યા:</strong> કાળી માટી ભીની ફૂલે સૂકી તિરાડે active zone 2–3.5 m.</p><p><strong>ભલામણ:</strong> Under-reamed pile + plinth beam + granular blanket.</p><p>1. 3–3.5 m ઊંડે bulbs active zone નીચે anchor. 2. Plinth beam બાંધે. 3. 100 mm રેતી પથારી swelling કાપે. 4. એક માળ માટે કરકસર. વિકલ્પ: CNS માટી બદલી + raft. છીછરો strip સીધો નહીં — તિરાડ.</p>"+fig(svg_ureamed,"કાળી માટી — under-reamed bulbs active zone નીચે")},
  {"q_en":"Q.1 (c) OR During the construction of a commercial building, differential settlement is observed in the foundation. Suggest possible remedial measures and explain how proper setting out of foundation layout could have prevented this failure. (07 marks)","marks_en":"07 marks","marks_gu":"૦૭ ગુણ",
   "a_en":"<p><strong>Differential settlement</strong> is unequal settlement causing cracks, tilt.</p><p><strong>Remedial:</strong> 1. <em>Grouting</em> cement grout under footing, 2. <em>Underpinning</em> extend to hard strata with piles, 3. <em>Jacketing</em> enlarge footing, 4. Drainage correction, 5. Load reduction. Re-level and monitor.</p><p><strong>Prevention by setting out:</strong> Establish base line, 3-4-5 right angle, peg every corner, string lines, 1 m offset for trench, diagonal check equal, levels to avoid eccentric loading, check against drawing before concrete.</p>"+fig(svg_setout,"Foundation setting out — base line, 3-4-5 right angle, pegs, offsets, diagonal check")+fig(svg_fail,"Differential settlement — grouting, underpinning, drainage correction"),
   "a_gu":"<p><strong>અસમાન બેસવું</strong> તિરાડ નમવું.</p><p><strong>ઉપાય:</strong> Grouting, Underpinning ઊંડા hard પર, Jacketing મોટું, Drainage સુધારો, ભાર ઘટાડો.</p><p><strong>રોકવા setting out:</strong> Base line, 3-4-5 કાટખૂણો, દરેક ખૂણે peg, 1 m offset, diagonal સરખું, level થી eccentric નહીં.</p>"+fig(svg_setout,"સેટિંગ આઉટ — base line, 3-4-5, pegs, diagonal")+fig(svg_fail,"સેટલમેન્ટ ઉપાય")},
 ]
},
{
 "title_en":"Q2 · Piles, shallow/deep, scaffolding, failure, setting out, joints",
 "title_gu":"પ્ર.2 · પાઇલ, shallow deep, પાલખ, નિષ્ફળતા, સેટિંગ, સાંધા",
 "cards":[
  {"q_en":"Q.2 (a) State purpose of an under-reamed pile (Any three). (03 marks)","marks_en":"03 marks","marks_gu":"૦૩ ગુણ",
   "a_en":"<p>1. Anchor expansive black cotton soil below active zone. 2. Increase bearing by 2–3 bulbs — each bulb adds area. 3. Resist uplift from swelling. 4. Economical manual boring no heavy rig. 5. Suitable for light loads single storey to 3 floors.</p>",
   "a_gu":"<p>1. કાળી માટી active zone નીચે anchor. 2. 2–3 bulbs થી bearing વધે. 3. uplift રોકે. 4. હાથે ખોદાય કરકસર. 5. હળવા ભાર 1–3 માળ.</p>"},
  {"q_en":"Q.2 (b) Explain the difference between shallow and deep foundations with suitable examples. (04 marks)","marks_en":"04 marks","marks_gu":"૦૪ ગુણ",
   "a_en":"<table><tr><th>Shallow Df ≤ B</th><th>Deep Df &gt; B</th></tr><tr><td>Bearing on near good strata — spread, strip, raft</td><td>Transfer to deep hard — pile, well/caisson, pier</td></tr><tr><td>Load light to medium, good soil top</td><td>Heavy load or top weak black cotton/fill</td></tr><tr><td>Open excavation economical</td><td>Bored/driven under water possible</td></tr><tr><td>Example: 2-storey house on murrum — isolated footing</td><td>Bridge pier in river — well foundation; high rise on clay — piles</td></tr></table>"+fig(svg_found,"Shallow spread/raft bear near surface vs deep pile/caisson transfer deep"),
   "a_gu":"<table><tr><th>છીછરું Df ≤ B</th><th>ઊંડું Df &gt; B</th></tr><tr><td>નજીક સારી માટી પર — spread/raft</td><td>ઊંડા hard પર — pile/well</td></tr><tr><td>હળવો ભાર સારી ઉપર માટી</td><td>ભારે ભાર નબળી ઉપર માટી</td></tr><tr><td>ઉદા: 2 માળ ઘર murrum પર isolated</td><td>નદી પુલ well, clay પર high rise piles</td></tr></table>"+fig(svg_found,"છીછરા vs ઊંડા — ઉદાહરણ")},
  {"q_en":"Q.2 (c) A multi-storey building in congested area. Which type of scaffolding would you recommend and why. (07 marks)","marks_en":"07 marks","marks_gu":"૦૭ ગુણ",
   "a_en":"<p><strong>Recommended: Double / Independent Steel Tubular Scaffolding.</strong></p><p><strong>Why for congested high building:</strong> Needs no wall support — stands free narrow 1.2 m gap. Strong steel reusable many times, height adjustable lifts 1.5 m, braced both sides stable for 10+ floors, safe platform with guard rail, toe board, nets. Putlogs not needed so wall not damaged, traffic below uninterrupted. Bamboo/single would block road and risk overheight.</p>",
   "a_gu":"<p><strong>ભલામણ: Double Steel Tubular independent.</strong></p><p><strong>શા માટે ગીચ ઊંચી:</strong> દિવાલ ટેકા વગર 1.2 m સાંકડી ઊભી, સ્ટીલ મજબૂત ફરી વપરાય, 1.5 m lift 10+ માળ, guard rail toe board net સલામત, putlog નહીં દિવાલ બગડે નહીં, નીચે ટ્રાફિક ચાલુ.</p>"},
  {"q_en":"Q.2 (a) OR List causes of foundation failure. (03 marks)","marks_en":"03 marks","marks_gu":"૦૩ ગુણ",
   "a_en":"<p>Inadequate investigation, overestimation of bearing, swelling/shrinkage, scour by water, overloading added floors, water table rise, poor drainage, nearby excavation vibrations, chemical attack on concrete, poor compaction.</p>"+fig(svg_fail,"Causes of foundation failure — investigation, swelling, scour, overloading, water table, excavation"),
   "a_gu":"<p>તપાસ અધૂરી, bearing વધારે ગણ્યું, ફૂલવું ધોવાણ, વધુ માળ ભાર, પાણી સ્તર ઊંચું, drainage નબળું, પાસે ખોદાણ, કેમિકલ.</p>"+fig(svg_fail,"પાયા નિષ્ફળતા કારણ")},
  {"q_en":"Q.2 (b) OR Explain how center lines are marked on site during foundation setting out. (04 marks)","marks_en":"04 marks","marks_gu":"૦૪ ગુણ",
   "a_en":f"<p>1. Establish base line from boundary. 2. Mark main centre line with theodolite/tape. 3. Square with 3-4-5 triangle. 4. Drive wooden pegs at corners with nails for centre. 5. Stretch strings, 1 m offset pegs to preserve after trench. 6. Check diagonals equal, right angles, compare with drawing before excavation.</p>"+fig(svg_setout,"Centre line marking — base line, 3-4-5 square, pegs with nails, strings, 1 m offsets, diagonal check"),
   "a_gu":f"<p>1. સીમા થી base line. 2. મુખ્ય મધ્ય રેખા theodolite/tape. 3. 3-4-5 થી કાટખૂણો. 4. ખૂણે peg ખીલી. 5. દોરી, 1 m offset peg trench પછી રહે. 6. diagonal સરખા, drawing સાથે મેળ.</p>"+fig(svg_setout,"મધ્ય રેખા નિશાન — pegs, offsets, diagonal")},
  {"q_en":"Q.2 (c) OR A long concrete pavement is being constructed. Which type of construction joint should be provided, and why? (07 marks)","marks_en":"07 marks","marks_gu":"૦૭ ગુણ",
   "a_en":"<p>Long concrete expands/contracts with temperature. Provide <strong>Transverse expansion joints</strong> 20 mm wide every 30–45 m with filler and dowels for load transfer; <strong>Contraction joints</strong> every 4–5 m shallow groove to control random cracks; <strong>Longitudinal joint</strong> at lane centre with tie bars. Without them slab cracks uncontrolled, faulting, blow-up.</p>",
   "a_gu":"<p>લાંબો pavement તાપમાને વધે ઘટે. <strong>Expansion 30–45 m</strong> 20 mm filler + dowels, <strong>Contraction 4–5 m</strong> છીછરી ખાંચ તિરાડ કાબુ, <strong>Longitudinal</strong> lane મધ્યે tie bars. નહીં તો random તિરાડ faulting.</p>"},
 ]
},
{
 "title_en":"Q3 · Machinery: excavating vs hoisting, dam, plumbing-electrical, batch plant, highway, grouting",
 "title_gu":"પ્ર.3 · મશીનરી: ખોદકામ vs ઉંચક, ડેમ, પ્લમ્બિંગ-વિદ્યુત, બેચ પ્લાન્ટ, હાઇવે, ગ્રાઉટિંગ",
 "cards":[
  {"q_en":"Q.3 (a) Explain the difference between excavating machinery and hoisting machinery. (03 marks)","marks_en":"03 marks","marks_gu":"૦૩ ગુણ",
   "a_en":"<p><strong>Excavating:</strong> Dig, cut, move earth — excavator, backhoe, dozer, dragline, clam shell, scraper. Works horizontally/vertically on ground.</p><p><strong>Hoisting:</strong> Lift and place vertically — tower/mobile crane, derrick, hoist, winch. Moves material height, no digging. Some machines like excavator with hook do both but primary classes differ by function and site need.</p>",
   "a_gu":"<p><strong>Excavating:</strong> ખોદે કાપે માટી ખસેડે — excavator, backhoe, dozer, dragline, clam shell. જમીન પર.</p><p><strong>Hoisting:</strong> ઊંચકે મૂકે — tower crane, derrick, hoist. ઊભું હલન, ખોદે નહીં.</p>"},
  {"q_en":"Q.3 (b) A dam project requires large-scale earthwork. Which class of construction machinery will you recommend? (04 marks)","marks_en":"04 marks","marks_gu":"૦૪ ગુણ",
   "a_en":"<p>Dam needs <em>Heavy earthmoving</em> class: Hydraulic excavators for cut, Scrapers for haul, Bulldozers for push, Dumpers for transport, Sheep foot + vibratory rollers for compaction, Dragline for deep borrow, Batch plant + transit mixers for mass concrete, Dewatering pumps.</p>",
   "a_gu":"<p>ડેમ માટે <em>ભારે earthmoving</em>: Excavator કાપ, Scraper ખેંચ, Dozer ધકેલ, Dumper લઈ જાય, Roller દબાવે, Dragline ઊંડું, Batch plant mass concrete.</p>"},
  {"q_en":"Q.3 (c) A two-storey house requires a reliable water supply and safe wiring. Suggest suitable plumbing layout and type of electrical connection. (07 marks)","marks_en":"07 marks","marks_gu":"૦૭ ગુણ",
   "a_en":"<p><strong>Plumbing:</strong> Underground sump + terrace overhead tank 1000 L, pump up, gravity down with separate hot/cold lines, gate valves per floor, vent pipe, no cross-connection to drain.</p><p><strong>Electrical:</strong> 3-phase if load &gt;5 kW else single phase, parallel wiring each room independent, separate light/power circuits, MCB per circuit + ELCB/RCCB 30 mA, proper earthing &lt;5 ohm, conduit concealed, switch boards at 1.2 m height.</p>",
   "a_gu":"<p><strong>પ્લમ્બિંગ:</strong> ભૂગર્ભ sump + ટેરેસ overhead 1000 L pump થી ઉપર gravity નીચે ગરમ ઠંડુ અલગ, દરેક માળ valve, vent, drain સાથે જોડાણ નહીં.</p><p><strong>વિદ્યુત:</strong> 5 kW થી વધુ 3-phase નહીંતર single, parallel દરેક રૂમ independent, light/power અલગ circuit, MCB + ELCB 30 mA, earthing &lt;5 ohm, conduit અંદર.</p>"},
  {"q_en":"Q.3 (a) OR Explain the working of a batch mix plant for concrete production. (03 marks)","marks_en":"03 marks","marks_gu":"૦૩ ગુણ",
   "a_en":f"<p>Batch plant weighs aggregates in hoppers by weigh-batchers, cement by weigh hopper, water by meter. Mixer drum mixes 45–60 sec, discharged to transit mixer or pump. Controlled grading, w/c, admixture for uniform quality in large quantity. Capacity 30–120 m3/h.</p>"+fig(svg_batch,"Batch mix plant — aggregate hoppers, weigh batchers, cement weigh, water meter, mixer drum to transit"),
   "a_gu":f"<p>Batch plant માં aggregate hopper માં weigh, cement weigh, પાણી મીટર, mixer ડ્રમ 45–60 sec મિક્સ, transit માં. Uniform quality 30–120 m3/h.</p>"+fig(svg_batch,"બેચ મિક્સ પ્લાન્ટ — hoppers, weigh, mixer")},
  {"q_en":"Q.3 (b) OR A highway project requires excavation, transportation, compaction, and laying of bituminous concrete. Suggest suitable machineries for each stage. (04 marks)","marks_en":"04 marks","marks_gu":"૦૪ ગુણ",
   "a_en":"<p><strong>Excavation:</strong> Hydraulic excavator/backhoe, dozer.</p><p><strong>Transportation:</strong> Tipper dumpers, trucks.</p><p><strong>Compaction:</strong> Sheep foot for clay, smooth vibratory roller for granular, pneumatic for bitumen.</p><p><strong>Laying:</strong> Hot mix plant, paver finisher for uniform thickness, tack coat sprayer.</p>",
   "a_gu":"<p><strong>ખોદાણ:</strong> Excavator, dozer. <strong>વહન:</strong> Dumper. <strong>દબાણ:</strong> Sheep foot, vibratory, pneumatic. <strong>પાથરવું:</strong> Hot mix, paver finisher, tack coat.</p>"},
  {"q_en":"Q.3 (c) OR A water retaining structure has developed leakage cracks. Which method (grouting or guniting) would you suggest and why? (07 marks)","marks_en":"07 marks","marks_gu":"૦૭ ગુણ",
   "a_en":"<p><strong>For deep leakage cracks: Grouting first.</strong> Cement/epoxy grout injected under pressure fills internal voids, restores water tightness. Need packers, pressure 2–5 kg/cm2. <em>Guniting</em> is sprayed mortar 25–50 mm for surface repair, protective layer after grouting. For surface honeycomb only — guniting alone. Water retaining must be pressure sealed internally — grouting primary, guniting secondary.</p>",
   "a_gu":"<p><strong>ઊંડી લીક તિરાડ: Grouting પહેલાં.</strong> સિમેન્ટ/epoxy grout દબાણથી અંદર ખાલી પૂરે પાણી રોકે 2–5 kg/cm2. <em>Guniting</em> 25–50 mm spray સપાટી રિપેર, grouting પછી રક્ષણ. માત્ર સપાટી honeycomb હોય તો guniting એકલું. પાણી રોકવા અંદરથી સીલ — grouting મુખ્ય.</p>"},
 ]
},
{
 "title_en":"Q4 · Wiring, dampness, bonds, joints, concrete, w/c ratio",
 "title_gu":"પ્ર.4 · વાયરિંગ, ભીનાશ, બોન્ડ, સાંધા, કોંક્રિટ",
 "cards":[
  {"q_en":"Q.4 (a) Explain the difference between series wiring and parallel wiring in electrification. (03 marks)","marks_en":"03 marks","marks_gu":"૦૩ ગુણ",
   "a_en":"<p><strong>Series:</strong> Single path — current same, voltage divides, one bulb fails all off, dimmer, not used for buildings.</p><p><strong>Parallel:</strong> Each load gets full voltage independently, failure of one does not affect others, brighter, used for houses. Wiring more but reliable.</p>",
   "a_gu":"<p><strong>Series:</strong> એક માર્ગ — એક બગડે બધા બંધ, voltage વહેંચાય, ઝાંખું. <strong>Parallel:</strong> દરેકને પૂરું voltage independent, એક બગડે બીજું ચાલુ, ઘરમાં વપરાય.</p>"},
  {"q_en":"Q.4 (b) List sources of dampness in buildings (Any four). (04 marks)","marks_en":"04 marks","marks_gu":"૦૪ ગુણ",
   "a_en":"<p>1. Rain penetration through wall/roof cracks. 2. Rising capillary moisture from ground. 3. Condensation from temperature difference. 4. Leaking pipes and drains. 5. Poor drainage around plinth. 6. Groundwater table high.</p>",
   "a_gu":"<p>1. વરસાદ દિવાલ તિરાડથી. 2. જમીનથી capillary ઊંચે. 3. ઠંડી ગરમી condensation. 4. પાઇપ લીક. 5. plinth પાસે drainage નબળું. 6. ભૂગર્ભ પાણી ઊંચું.</p>"},
  {"q_en":"Q.4 (c) Explain the difference between English bond and Flemish bond. (07 marks)","marks_en":"07 marks","marks_gu":"૦૭ ગુણ",
   "a_en":f"<p><strong>English bond:</strong> Alternate courses all headers then all stretchers, vertical joints broken with queen closer next to quoin header. Strongest, 1/4 brick lap, best for load bearing.</p><p><strong>Flemish bond:</strong> Each course alternates header and stretcher within same course. Better appearance, uses more bats, slightly weaker, requires skilled mason. Variant Double/Single Flemish.</p>"+fig(svg_bonds,"English — alternate header/stretcher courses strongest vs Flemish — header+stretcher in same course decorative"),
   "a_gu":f"<p><strong>અંગ્રેજી:</strong> એક કોર્સ બધા હેડર, બીજો બધા સ્ટ્રેચર, queen closer થી સાંધા તૂટે. સૌથી મજબૂત ભારવાહી માટે.</p><p><strong>ફ્લેમિશ:</strong> દરેક કોર્સમાં હેડર સ્ટ્રેચર બદલે. દેખાવ સુંદર, થોડી નબળી, કુશળ કારીગર જોઈએ.</p>"+fig(svg_bonds,"અંગ્રેજી vs ફ્લેમિશ — કોર્સ vs કોર્સમાં બદલાવ")},
  {"q_en":"Q.4 (a) OR Explain the difference between expansion joints and contraction joints. (03 marks)","marks_en":"03 marks","marks_gu":"૦૩ ગુણ",
   "a_en":"<p><strong>Expansion joint:</strong> Full gap 12–25 mm with filler and dowels to allow expansion in heat, prevents blow-up. Every 30 m.</p><p><strong>Contraction joint:</strong> Weakened plane 1/3 depth groove to control shrinkage cracking, no gap, every 4–5 m. Load transfer by aggregate interlock.</p>",
   "a_gu":"<p><strong>Expansion:</strong> 12–25 mm ખાલી filler + dowels ગરમીમાં વધવા દે, blow-up રોકે 30 m.</p><p><strong>Contraction:</strong> 1/3 ઊંડાઈ ખાંચ shrinkage તિરાડ કાબુ 4–5 m, gap નહીં.</p>"},
  {"q_en":"Q.4 (b) OR List the main ingredients of concrete. (04 marks)","marks_en":"04 marks","marks_gu":"૦૪ ગુણ",
   "a_en":"<p>Cement OPC/PPC, Fine aggregate river sand Zone II, Coarse aggregate 10–20 mm, Clean potable water, Admixtures plasticizer/retarder/air entraining as needed. Ratio forms M20, M30 etc.</p>",
   "a_gu":"<p>સિમેન્ટ, રેતી Zone II, કપચી 10–20 mm, સ્વચ્છ પાણી, admixture જરૂર મુજબ. પ્રમાણ M20 M30.</p>"},
  {"q_en":"Q.4 (c) OR Explain why water-cement ratio is important in concrete mix design. (07 marks)","marks_en":"07 marks","marks_gu":"૦૭ ગુણ",
   "a_en":"<p>Water-cement ratio controls strength, workability, durability, permeability. <em>Abrams law:</em> strength inversely proportional to w/c. High w/c &gt;0.6 gives weak porous permeable, low &lt;0.35 incomplete hydration harsh mix. Optimum 0.40–0.50 for RCC balances workability and strength. Lower w/c with plasticizer gives high strength durable concrete.</p>",
   "a_gu":"<p>પાણી-સિમેન્ટ ગુણોત્તર strength, workability, durability, permeability નક્કી. Abrams નિયમ: w/c વધુ strength ઓછી. &gt;0.6 નબળું છિદ્રાળું, &lt;0.35 અધૂરું hydration. RCC માટે 0.40–0.50 ઉત્તમ, plasticizer થી વધુ strength.</p>"},
 ]
},
{
 "title_en":"Q5 · Accidents, safety, advanced tech, PPE, scaffolding, drones",
 "title_gu":"પ્ર.5 · અકસ્માત, સલામતી, નવી ટેક, PPE, પાલખ, ડ્રોન",
 "cards":[
  {"q_en":"Q.5 (a) List any common causes of construction accidents. (03 marks)","marks_en":"03 marks","marks_gu":"૦૩ ગુણ",
   "a_en":"<p>1. Falls from height/scaffold. 2. Collapse of trench/formwork/stack. 3. Struck by falling objects/tools. 4. Electrical shock. 5. Faulty equipment and PPE not used. 6. Poor training and housekeeping, slippery access.</p>"+fig(svg_fail,"Common causes — falls, collapse, struck by objects, electrical, faulty equipment, poor training"),
   "a_gu":"<p>1. ઊંચાઈથી પડવું. 2. ખાઈ ફોર્મવર્ક ધસવું. 3. પડતી વસ્તુ વાગવી. 4. વીજળી. 5. ખરાબ સાધન PPE નહીં. 6. તાલીમ સફાઈ નબળી.</p>"+fig(svg_fail,"અકસ્માત સામાન્ય કારણ — પડવું, ધસવું, વીજળી")},
  {"q_en":"Q.5 (b) You are a site supervisor; how would you ensure safety compliance during concreting work? (04 marks)","marks_en":"04 marks","marks_gu":"૦૪ ગુણ",
   "a_en":"<p>Checklist: PPE helmet gloves boots, inspect formwork bracing before pour, safe vibrator with ELCB, barricades around edge, no overloading platform, toolbox talk, first aid nearby, no concreting in rain without cover, ensure curing without climbing wet slab.</p>",
   "a_gu":"<p>તપાસ: PPE, formwork ટેકો check, vibrator ELCB, ધાર barricade, વધુ ભાર નહીં, toolbox વાત, first aid, વરસાદમાં ઢાંકણ, ભીના સ્લેબ પર ચડવું નહીં.</p>"},
  {"q_en":"Q.5 (c) Explain how the use of advanced technologies reduces cost and time in construction projects. (07 marks)","marks_en":"07 marks","marks_gu":"૦૭ ગુણ",
   "a_en":"<p><strong>BIM</strong> 3D/4D clash detection avoids rework, quantity auto, <strong>Prefab/modular</strong> factory parallel work erection days not months, <strong>3D printing</strong> walls without formwork, <strong>Drones</strong> survey progress daily, <strong>IoT sensors</strong> monitor curing/equipment, time 20–30% saved, cost via less labour waste.</p>"+fig(svg_modular,"Advanced tech — BIM, prefab, 3D printing, drones, IoT reduce cost and time"),
   "a_gu":"<p><strong>BIM</strong> અથડામણ શોધ rework ટળે, <strong>Prefab</strong> ફેક્ટરી સમાંતર દિવસમાં ઊભું, <strong>3D પ્રિન્ટ</strong> ફોર્મવર્ક વગર, <strong>ડ્રોન</strong> રોજ સર્વે, <strong>IoT</strong> curing દેખરેખ — સમય 20–30% ખર્ચ ઓછો.</p>"+fig(svg_modular,"નવી ટેક — BIM, prefab, 3D printing સમય ખર્ચ ઘટાડે")},
  {"q_en":"Q.5 (a) OR Name any three personal protective equipment (PPE). (03 marks)","marks_en":"03 marks","marks_gu":"૦૩ ગુણ",
   "a_en":"<p>Helmet protects head from fall, Safety shoes steel toe, Full body harness for height, Goggles against dust, Gloves, Ear plugs. Choose per work: height → harness + helmet, concreting → boots + gloves.</p>"+fig(svg_ppe,"PPE — helmet, harness, safety shoes, goggles, gloves"),
   "a_gu":"<p>Helmet માથું, Safety shoes ટોચ સ્ટીલ, Harness ઊંચાઈ, Goggles ધૂળ, Gloves, Ear plug. કામ મુજબ: ઊંચાઈ → harness + helmet.</p>"+fig(svg_ppe,"PPE — helmet, harness, shoes")},
  {"q_en":"Q.5 (b) OR A worker is assigned to work on scaffolding at 10 m height. Which safety equipment will you provide, and why? (04 marks)","marks_en":"04 marks","marks_gu":"૦૪ ગુણ",
   "a_en":"<p>At 10 m fall fatal: Full body harness with shock absorber anchored to independent lifeline, Helmet, Non-slip safety shoes, Guard rails 1 m + mid rail + toe board on platform, Safety net below, Safe ladder. Reason: arrest fall, protect head/feet, prevent object fall.</p>",
   "a_gu":"<p>10 m પડવું જીવલેણ: Full body harness lifeline સાથે, Helmet, Safety shoes, Guard rail 1 m + toe board, નીચે net, Ladder. પડવું અટકાવે, માથું પગ બચે.</p>"},
  {"q_en":"Q.5 (c) OR Explain how drones are useful for surveying large construction sites. (07 marks)","marks_en":"07 marks","marks_gu":"૦૭ ગુણ",
   "a_en":f"<p>Drones capture aerial photos/videos, generate orthomosaic, contour, stockpile volume in hours vs days. Progress monitoring, site logistics, safety inspection of heights without scaffold, thermal leaks. Fast for large 100 acre sites, accuracy 2–5 cm with GCP.</p>"+fig(svg_map,"Drone surveying large site — aerial mapping, stockpile volume, progress and safety inspection"),
   "a_gu":f"<p>ડ્રોન હવાઈ ફોટો, orthomosaic, contour, stockpile જથ્થો કલાકોમાં દિવસોને બદલે. પ્રગતિ, logistics, ઊંચાઈ સલામતી તપાસ પાલખ વગર. 100 acre ઝડપી 2–5 cm ચોકસાઈ.</p>"+fig(svg_map,"ડ્રોન સર્વે — હવાઈ મેપિંગ, જથ્થો, સલામતી")},
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
    page=f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>DI03006011 · Summer 2026 solved paper</title><style>{CSS}</style></head><body><main class="page"><header class="hero"><div class="eyebrow">Solved question paper · English questions · Friendly Gujarati answers</div><div class="lang-switch" aria-label="Choose language"><button type="button" data-lang="en" aria-pressed="true">English</button><button type="button" data-lang="gu" aria-pressed="false">ગુજરાતી</button></div><h1>Construction Technology</h1><div class="meta">GTU Diploma · Civil · Semester 3 · Summer 2026 · DI03006011 · 12-05-2026 · 70 marks · 02:30 PM TO 05:00 PM</div></header>{"".join(sections_html)}<div class="footer">Solved paper for study. Verify with site spec before application.</div></main><script>document.querySelectorAll('.lang-switch button').forEach(b=>b.addEventListener('click',()=>{{document.documentElement.lang=b.dataset.lang;document.querySelectorAll('.lang-switch button').forEach(x=>x.setAttribute('aria-pressed',x===b?'true':'false'));}}));</script></body></html>'''
    return page
def main():
    page=build_page()
    out_papers=ROOT/"papers-upload/papers/DI03006011/summer-2026.html"
    out_ws=ROOT/"preview/workshop/DI03006011_summer2026_bilingual.html"
    out_papers.parent.mkdir(parents=True,exist_ok=True)
    out_ws.parent.mkdir(parents=True,exist_ok=True)
    out_papers.write_text(page,encoding="utf-8")
    out_ws.write_text(page,encoding="utf-8")
    print(f"Bilingual: {out_papers} ({len(page)} chars)")
    print(f"details={page.count('<details')}, sections={page.count('<section')}, figs={page.count('<figure>')}")
    import re; gu=''.join(re.findall(r'<div class="gu">(.*?)</div>',page,re.S)); print(f"brackets gu={gu.count('(')+gu.count(')')}")
    print("PASS" if page.count('<details')==28 and page.count('<section')==5 else "FAIL")
    (ROOT/"drive-upload/DI03006011_summer_2026_bilingual.html").write_text(page,encoding="utf-8")
if __name__=="__main__": main()
