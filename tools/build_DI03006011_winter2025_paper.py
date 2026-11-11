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
# Load only minimal essential SVGs (12 max - unique)
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
 "title_en":"Q1 · Building items, structure types, scaffolding / formwork",
 "title_gu":"પ્ર.1 · બિલ્ડિંગ વસ્તુ, સ્ટ્રક્ચર પ્રકાર, પાલખ / ફોર્મવર્ક",
 "cards":[
  {"q_en":"Q.1 (a) Write functions of following items in Building: Lintel, Sill, Weather sheds. (03 marks)","marks_en":"03 marks","marks_gu":"૦૩ ગુણ",
   "a_en":f"<p><strong>Lintel:</strong> Horizontal RCC/steel beam over door-window opening that carries wall load above and transfers it to jambs. Prevents cracking, keeps opening square. Provided 150 mm bearing each side, depth 1/10 of span.</p><p><strong>Sill:</strong> Bottom horizontal member of window frame. Supports window, sheds rain water outward with 1:20 slope, protects wall top from damp, provides level base for shutter.</p><p><strong>Weather shed / Chhajja:</strong> 450–600 mm projection above opening. Shades from sun and rain, protects lintel and window from direct weathering, reduces heat gain. RCC cantilever 75–100 mm thick with drip groove.</p>"+fig(svg_wall,"Lintel over opening carries wall load, sill drains water outward, chhajja shades — all seen in wall cross-section"),
   "a_gu":f"<p><strong>લિન્ટલ:</strong> બારણા બારી ઉપરનો આડો RCC બીમ ઉપરની દિવાલનો ભાર બાજુની જામ્બ પર લઈ જાય. તિરાડ અટકાવે, ઓપનિંગ ચોરસ રાખે. દરેક બાજુ 150 mm બેરિંગ, ઊંડાઈ ગાળાના 1/10.</p><p><strong>સિલ:</strong> બારી ફ્રેમનો નીચેનો આડો ભાગ. બારીને ટેકો, વરસાદી પાણી બહાર કાઢવા 1:20 ઢાળ, દિવાલને ભીનાશથી બચાવે.</p><p><strong>છજું:</strong> ઓપનિંગ ઉપર 450–600 mm બહાર નીકળેલો RCC કૅન્ટિલિવર. તડકો વરસાદથી રક્ષણ, ગરમી ઘટાડે, નીચે ડ્રિપ ખાંચાથી પાણી ટપકે.</p>"+fig(svg_wall,"લિન્ટલ ભાર વહન, સિલ પાણી નિકાલ, છજું છાંયો — દિવાલ કટમાં")},
  {"q_en":"Q.1 (b) Differentiate between Load Bearing and Framed Structures. (04 marks)","marks_en":"04 marks","marks_gu":"૦૪ ગુણ",
   "a_en":"<table><tr><th>Point</th><th>Load Bearing</th><th>Framed</th></tr><tr><td>Load path</td><td>Walls themselves carry slab load to foundation</td><td>RCC columns + beams form frame, walls are infill</td></tr><tr><td>Wall thickness</td><td>200–350 mm, thicker at lower floors</td><td>100–150 mm partition, uniform</td></tr><tr><td>Height limit</td><td>3–4 floors economical beyond uneconomical</td><td>High rise 10+ floors, flexible plan</td></tr><tr><td>Material</td><td>Brick/stone masonry + RCC slab</td><td>RCC/steel frame, brick/AAC infill</td></tr><tr><td>Earthquake</td><td>Stiff but brittle if not reinforced</td><td>Ductile detailing possible, better performance</td></tr></table>"+fig(svg_frame,"Load bearing walls carry load vs framed columns-beams carry load"),
   "a_gu":"<table><tr><th>મુદ્દો</th><th>ભારવાહી</th><th>ફ્રેમ</th></tr><tr><td>ભાર માર્ગ</td><td>દિવાલ જ ભાર પાયા સુધી લઈ જાય</td><td>RCC કોલમ બીમ ફ્રેમ બનાવે દિવાલ પૂરક</td></tr><tr><td>જાડાઈ</td><td>200–350 mm નીચે વધુ જાડી</td><td>100–150 mm પાતળી</td></tr><tr><td>ઊંચાઈ</td><td>3–4 માળ સુધી સસ્તી</td><td>ઊંચી ઇમારત, પ્લાન લવચીક</td></tr><tr><td>સામગ્રી</td><td>ઈંટ પથ્થર + સ્લેબ</td><td>RCC/સ્ટીલ ફ્રેમ, AAC પૂરક</td></tr></table>"+fig(svg_frame,"ભારવાહી vs ફ્રેમ — ભાર વહન માર્ગ")},
  {"q_en":"Q.1 (c) With neat sketch explain components of Scaffolding. (07 marks)","marks_en":"07 marks","marks_gu":"૦૭ ગુણ",
   "a_en":f"<p><strong>Purpose:</strong> Temporary platform for masons, material, safety at height.</p><p><strong>Components:</strong> <em>Standards</em> vertical posts 2 m c/c; <em>Ledgers</em> horizontal runners; <em>Transoms/Putlogs</em> bear platform, one end in wall hole; <em>Bracing</em> diagonal stability; <em>Base plate + sole board</em> spread load; <em>Platform/boards</em> 225 mm thick; <em>Guard rail</em> 1 m + <em>toe board</em> 150 mm; <em>Ladder</em> access. <strong>Types:</strong> Single/bricklayer, Double/independent, Steel tubular, Needle/cantilever.</p><p><strong>Erection:</strong> Base level, standards plumb, ledgers at 1.5 m lift, check 3-4-5, tie to wall every 4 m.</p>"+fig(svg_scaffold,"Scaffolding — standards vertical, ledgers horizontal, putlogs, bracing, platform, guard rail, toe board"),
   "a_gu":f"<p><strong>હેતુ:</strong> ઊંચાઈએ કામ માટે કામચલાઉ મંચ.</p><p><strong>ભાગો:</strong> Standards ઊભા થાંભલા, Ledgers આડા, Putlogs મંચને ટેકવે, Bracing ત્રાંસી સ્થિરતા, Base plate ભાર ફેલાવે, Platform પાટિયા, Guard rail 1 m + Toe board, Ladder. <strong>પ્રકાર:</strong> Single, Double, Steel tubular, Needle.</p><p><strong>ઊભું કરવું:</strong> Base સમતલ, standards ઊભા, ledgers 1.5 m lift, દિવાલ સાથે tie.</p>"+fig(svg_scaffold,"પાલખ — standards, ledgers, putlogs, bracing, platform")},
  {"q_en":"Q.1 (c) OR Discuss in detail: Characteristics of good formwork. (07 marks)","marks_en":"07 marks","marks_gu":"૦૭ ગુણ",
   "a_en":"<p>Good formwork must be <strong>strong</strong> to carry fresh concrete + vibration without deflection &gt;3 mm; <strong>rigid</strong> to keep line and level; <strong>leak-proof</strong> tight joints to prevent grout loss and honeycomb; <strong>smooth</strong> face for good finish; <strong>light</strong> for handling; <strong>easy to strip</strong> without damage — oiled, correct striking time 24 h sides, 14–21 d slabs; <strong>reusable</strong> many times economical; <strong>accurate</strong> size, alignment, plumb. Materials: timber, plywood, steel, aluminium, plastic.</p>",
   "a_gu":"<p>સારું ફોર્મવર્ક <strong>મજબૂત</strong> તાજા કોંક્રિટ વાઇબ્રેશન ખમી શકે deflection 3 mm થી ઓછું, <strong>કડક</strong> લાઇન લેવલ જાળવે, <strong>લીક પ્રૂફ</strong> સાંધા બંધ honeycomb ન થાય, <strong>સુંવાળું</strong> ફિનિશ સારું, <strong>હલકું</strong> ઉંચકાય, <strong>સરળતાથી છૂટે</strong> તેલ લગાવેલું 24 કલાક સાઇડ 14–21 દિવસ સ્લેબ, <strong>ફરી વપરાય</strong> કરકસર, <strong>ચોક્કસ માપ</strong>.</p>"},
 ]
},
{
 "title_en":"Q2 · Foundations, cofferdam, piles, caisson, timbering",
 "title_gu":"પ્ર.2 · પાયા, કોફરડેમ, પાઇલ, કેશન, ટિમ્બરિંગ",
 "cards":[
  {"q_en":"Q.2 (a) List out the Types of Shallow Foundation and Deep Foundations. (03 marks)","marks_en":"03 marks","marks_gu":"૦૩ ગુણ",
   "a_en":"<p><strong>Shallow Df ≤ B:</strong> Strip/wall footing, Isolated spread, Combined, Cantilever/strap, Raft/mat, Inverted arch.</p><p><strong>Deep Df &gt; B:</strong> Driven/bored pile, Under-reamed pile, Well/caisson, Pier, Pile cap groups. Chosen when top soil weak, heavy load, black cotton active zone deep.</p>"+fig(svg_found,"Shallow wall/isolated/raft bear near surface vs deep pile/caisson go deep"),
   "a_gu":"<p><strong>છીછરા Df ≤ B:</strong> Strip, Isolated, Combined, Raft.</p><p><strong>ઊંડા Df &gt; B:</strong> Driven/bored, Under-reamed, Well/Caisson. ઉપરની માટી નબળી કે ભારે ભાર ત્યારે.</p>"+fig(svg_found,"છીછરા vs ઊંડા પાયા")},
  {"q_en":"Q.2 (b) Draw Neat Sketch of RCC Footing for Brick Masonary Wall. (04 marks)","marks_en":"04 marks","marks_gu":"૦૪ ગુણ",
   "a_en":"<p>Wall 200 mm on RCC footing: PCC lean 100 mm, RCC base 900 mm wide × 300 mm thick, wall offset 150 mm each side, 8 mm @150 c/c distribution + 10 mm @150 main steel, 50 mm cover, plinth beam above. Bearing pressure ≤ SBC 150 kN/m2.</p>",
   "a_gu":"<p>200 mm દિવાલ પર RCC ફૂટિંગ: PCC 100 mm, RCC બેઝ 900×300 mm, દરેક બાજુ 150 mm ઓફસેટ, 10 mm મુખ્ય + 8 mm વિતરણ સ્ટીલ, કવર 50 mm.</p>"},
  {"q_en":"Q.2 (c) Enlist Types of coffer Dams, Draw neat Sketch of Rock Fill Crib Cofferdam. (07 marks)","marks_en":"07 marks","marks_gu":"૦૭ ગુણ",
   "a_en":"<p><strong>Types:</strong> Earthen, Rock fill, Single wall, Double wall, Crib, Cellular, Pneumatic.</p><p><strong>Rock fill crib:</strong> Timber cribs 2×2 m filled with boulders, placed in water, impervious puddle clay on water side, stable for 6–10 m deep flow. Water pumped out inside to work dry. Advantages: uses local rock, resists current, reusable timber.</p>",
   "a_gu":"<p><strong>પ્રકાર:</strong> Earthen, Rock fill, Single/Double wall, Crib, Cellular.</p><p><strong>રોક ફિલ ક્રિબ:</strong> લાકડાની પેટી 2×2 m માં પથ્થર ભરી પાણીમાં મૂકવી, પાણી બાજુ ચીકણી માટી પડદો, અંદર પાણી ખેંચી સૂકું કામ. 6–10 m ઊંડા વહેણમાં સ્થિર.</p>"},
  {"q_en":"Q.2 (a) OR Explain End bearing Pile with Sketch. (03 marks)","marks_en":"03 marks","marks_gu":"૦૩ ગુણ",
   "a_en":"<p>End bearing pile acts as column — tip rests on hard rock/dense sand, load transferred mainly by point bearing. Friction negligible. Length up to rock, diameter 300–600 mm, safe load 500–1500 kN. Uses: high load to rock within 20 m.</p>"+fig(svg_ureamed,"End bearing pile tip on hard strata acts as column"),
   "a_gu":"<p>એન્ડ બેરિંગ પાઇલ થાંભલાની જેમ — ટોચ હાર્ડ ખડક પર, ભાર સીધો નીચે. ઘર્ષણ નહિવત્. ખડક 20 m અંદર હોય ત્યારે.</p>"+fig(svg_ureamed,"એન્ડ બેરિંગ પાઇલ — ટોચ હાર્ડ પર")},
  {"q_en":"Q.2 (b) OR Draw neat Sketch of Box Caisson. (04 marks)","marks_en":"04 marks","marks_gu":"૦૪ ગુણ",
   "a_en":"<p>Box caisson is open at top closed at bottom — RCC box floated to site, sunk onto prepared rock bed, filled with sand/concrete. No dewatering of bottom. For bridge piers, wharves where rock at bed level.</p>",
   "a_gu":"<p>બોક્સ કેશન ઉપર ખુલ્લું નીચે બંધ — તરતું લઈ જઈ ખડક પર બેસાડાય, અંદર રેતી કોંક્રિટ ભરાય. તળિયા સુકવવાની જરૂર નહીં.</p>"},
  {"q_en":"Q.2 (c) OR Write Short note on Timbering of Trenches. (07 marks)","marks_en":"07 marks","marks_gu":"૦૭ ગુણ",
   "a_en":f"<p>To prevent collapse in loose/water-charged soil, sides supported as excavation proceeds. <strong>Systems:</strong> Stay bracing poling boards + wallings + struts 1.5 m c/c; <em>Box sheeting</em> for deep; <em>Vertical sheeting</em> with horizontal wallings; <em>Runners</em> for running sand. Sequence: 1.2 m dig → place boards → struts wedged → next lift. Remove bottom-up after backfill.</p>"+fig(svg_timber,"Timbering trenches — poling boards, wallings, struts prevent collapse"),
   "a_gu":f"<p>ઢીલી પાણીવાળી માટીમાં ધસી ન પડે માટે બાજુ ટેકવાય. Stay bracing, Box sheeting, Vertical sheeting + struts 1.5 m. ક્રમ: 1.2 m ખોદો → પાટિયા → struts → આગળ. ભર્યા પછી નીચેથી કાઢો.</p>"+fig(svg_timber,"ટિમ્બરિંગ — પાટિયા, wallings, struts")},
 ]
},
{
 "title_en":"Q3 · Masonry, bonds, concrete, plaster",
 "title_gu":"પ્ર.3 · ચણતર, બોન્ડ, કોંક્રિટ, પ્લાસ્ટર",
 "cards":[
  {"q_en":"Q.3 (a) Define with sketch: Frog, Header, Stretcher. (03 marks)","marks_en":"03 marks","marks_gu":"૦૩ ગુણ",
   "a_en":"<p><strong>Frog:</strong> 10 mm deep depression 100×40 mm on top face of brick for key with mortar, also marks top. <strong>Header:</strong> Short end face 90×90 mm visible when brick laid width-wise. <strong>Stretcher:</strong> Long face 190×90 mm visible when laid length-wise.</p>"+fig(svg_bonds,"Frog depression, header short face, stretcher long face — helps break vertical joints"),
   "a_gu":"<p><strong>ફ્રોગ:</strong> ઈંટની ઉપર 10 mm ખાડો 100×40 મોર્ટાર પકડ માટે. <strong>હેડર:</strong> ટૂંકી બાજુ 90×90 mm. <strong>સ્ટ્રેચર:</strong> લાંબી બાજુ 190×90 mm.</p>"+fig(svg_bonds,"ફ્રોગ, હેડર, સ્ટ્રેચર — ઊભા સાંધા તોડવા")},
  {"q_en":"Q.3 (b) Draw neat sketch of English Bond for Brick thick wall. (04 marks)","marks_en":"04 marks","marks_gu":"૦૪ ગુણ",
   "a_en":"<p>Strongest bond: alternate courses all headers then all stretchers. Vertical joints broken by queen closer next to quoin header. Lap 1/4 brick. For 200 mm wall: course 1 headers, course 2 stretchers. Minimum crushing strength.</p>",
   "a_gu":"<p>સૌથી મજબૂત: એક કોર્સ બધા હેડર, બીજો બધા સ્ટ્રેચર. Quoin હેડર પાસે queen closer થી સાંધા તૂટે. 200 mm દિવાલ.</p>"},
  {"q_en":"Q.3 (c) List out Ingredients of Concrete. Explain Compaction of Concrete. (07 marks)","marks_en":"07 marks","marks_gu":"૦૭ ગુણ",
   "a_en":"<p><strong>Ingredients:</strong> Cement, Fine aggregate sand, Coarse aggregate 10–20 mm, Water potable, Admixture plasticizer/retarder as needed.</p><p><strong>Compaction:</strong> Expel entrapped air to achieve density. Methods: hand tamping for plain, needle vibrator 25–40 mm for RCC beams columns 30–60 sec until cement slurry appears, surface vibrator for slabs, table vibrator for precast. Over-vibration causes segregation, under-vibration honeycomb. Done in layers 300–450 mm.</p>",
   "a_gu":"<p><strong>ઘટકો:</strong> સિમેન્ટ, રેતી, કપચી 10–20 mm, પાણી, admixture.</p><p><strong>કોમ્પેક્શન:</strong> હવા કાઢી ઘન બનાવવું. હાથ ઠોક, needle vibrator 30–60 sec સિમેન્ટ પાણી દેખાય ત્યાં સુધી, સ્લેબ માટે surface vibrator. વધુ વાઇબ્રેશનથી segregation, ઓછું honeycomb. 300–450 mm થર.</p>"},
  {"q_en":"Q.3 (a) OR Define with sketch: King Closer, Queen Closer, Half Bat (03 marks)","marks_en":"03 marks","marks_gu":"૦૩ ગુણ",
   "a_en":"<p><strong>King closer:</strong> Brick cut diagonally from header centre to stretcher centre — half header half stretcher. <strong>Queen closer:</strong> Cut longitudinally into two halves 95 mm wide — placed next to quoin. <strong>Half bat:</strong> Cut across length — half length 95 mm.</p>",
   "a_gu":"<p><strong>કિંગ ક્લોઝર:</strong> ત્રાંસુ કાપેલું અડધું હેડર અડધું સ્ટ્રેચર. <strong>ક્વીન ક્લોઝર:</strong> લંબાઈમાં બે ભાગ 95 mm. <strong>હાફ બેટ:</strong> લંબાઈમાં અડધું 95 mm.</p>"},
  {"q_en":"Q.3 (b) OR Write Advantages of Hollow Concrete Block Masonary. (04 marks)","marks_en":"04 marks","marks_gu":"૦૪ ગુણ",
   "a_en":"<p>Lighter 1/3 weight saves foundation, hollow gives thermal and sound insulation, faster laying large size 400×200, less mortar, cavity reduces damp, earthquake lighter mass, precise size less plaster.</p>",
   "a_gu":"<p>1/3 હળવું પાયા ખર્ચ ઓછો, પોલાણથી ગરમી અવાજ અવરોધ, મોટી સાઇઝથી ઝડપી, મોર્ટાર ઓછું, ભીનાશ ઓછી, ભૂકંપમાં હળવું.</p>"},
  {"q_en":"Q.3 (c) OR Explain Method of Applying Sand faced Plaster on Outer Wall. (07 marks)","marks_en":"07 marks","marks_gu":"૦૭ ગુણ",
   "a_en":"<p><strong>Two coats:</strong> Clean wall, wet, 12 mm base coat 1:4 cement:sand levelled. After 24 h, 8 mm finishing coat 1:3 with coarse sand, dashed with sponge/trowel to get granular texture. Cure 7 days 2× daily. Thickness ensures no cracks, water shedding.</p>",
   "a_gu":"<p>દિવાલ clean ભીની, 12 mm base 1:4 level, 24 કલાક પછી 8 mm finishing 1:3 જાડી રેતી spongeથી ટેક્સચર, 7 દિવસ પાણી. તિરાડ નહીં પાણી સરકે.</p>"},
 ]
},
{
 "title_en":"Q4 · Damp, DPC, machinery, joints, equipment",
 "title_gu":"પ્ર.4 · ભીનાશ, DPC, મશીનરી, સાંધા",
 "cards":[
  {"q_en":"Q.4 (a) Explain Anti Termite treatment. (03 marks)","marks_en":"03 marks","marks_gu":"૦૩ ગુણ",
   "a_en":"<p>Chemical barrier of chlorpyrifos 1% or imidacloprid under and around building. Process: trench 30 cm deep around foundation, soil treatment 7.5 L/m2, pit bottom 5 L/m2 before PCC, plinth junction, pipe entry sealed. Blocks termite path from ground to wood.</p>",
   "a_gu":"<p>Chlorpyrifos 1% નો રાસાયણિક પડદો પાયા નીચે આસપાસ. 30 cm ખાઈ 7.5 L/m2, ખાડા તળિયા 5 L/m2 PCC પહેલાં, plinth સાંધા પાઇપ સીલ.</p>"},
  {"q_en":"Q.4 (b) Draw neat Sketch for DPC of Basement. (04 marks)","marks_en":"04 marks","marks_gu":"૦૪ ગુણ",
   "a_en":f"<p>Basement needs continuous waterproof envelope: 40 mm cement concrete 1:2:4 + waterproof compound on base slab, 20 mm bitumen mastic vertical on retaining wall tied to horizontal DPC at plinth with 150 mm lap, weep holes. No break at junctions.</p>"+fig(svg_dpc,"Basement DPC — horizontal on base slab + vertical on retaining wall continuous, no break"),
   "a_gu":f"<p>બેઝમેન્ટમાં સતત પડદો: તળિયા પર 40 mm 1:2:4 + waterproof, દિવાલ પર 20 mm bitumen vertical, plinth પર horizontal સાથે 150 mm lap, weep holes.</p>"+fig(svg_dpc,"બેઝમેન્ટ DPC — આડું + ઊભું સતત")},
  {"q_en":"Q.4 (c) Explain factor affecting selection of Construction Machineries. (07 marks)","marks_en":"07 marks","marks_gu":"૦૭ ગુણ",
   "a_en":"<p><strong>Selection depends on:</strong> Nature and quantity of work, site topography and access, soil type rock/hard strata, time schedule, cost hire vs buy, availability and spares, skilled operator, safety and noise, environmental restrictions. Example: high lift → tower crane not mobile crane; congested → compact excavator.</p>",
   "a_gu":"<p><strong>પસંદગી આધાર:</strong> કામ પ્રકાર જથ્થો, સાઇટ ભૂપ્રદેશ રસ્તો, માટી પ્રકાર, સમય, ખર્ચ ભાડે vs ખરીદ, ઉપલબ્ધતા, કુશળતા, સલામતી અવાજ, પર્યાવરણ. ઊંચું → ટાવર ક્રેન, સાંકડી → નાની excavator.</p>"},
  {"q_en":"Q.4 (a) OR Explain Construction Joints. (03 marks)","marks_en":"03 marks","marks_gu":"૦૩ ગુણ",
   "a_en":"<p>Joints where fresh concrete placed against hardened after pause &gt;30 min. Toothed or dowelled for continuity, placed at low shear zone, cleaned and bonding slurry applied. Water bar in water tanks.</p>",
   "a_gu":"<p>30 min થી વધુ રોકાણ પછી જૂના નવા કોંક્રિટ જોડાણ — દાંતાદાર/dowel, ઓછા shear સ્થળે, સાફ કરી bonding slurry.</p>"},
  {"q_en":"Q.4 (b) OR Enlist Safety Points for plumbing Work. (04 marks)","marks_en":"04 marks","marks_gu":"૦૪ ગુણ",
   "a_en":"<p>Wear PPE gloves goggles, shoring of trenches &gt;1.5 m, no open flame for solvent, pressure test at 1.5× working slowly, keep valves accessible, ventilate, lock pumps during repair.</p>",
   "a_gu":"<p>PPE, 1.5 m થી ઊંડી ખાઈને ટેકો, સોલવન્ટ પાસે જ્યોત નહીં, pressure test 1.5× ધીમે, valve ખુલ્લા, હવા, પંપ બંધ કરી કામ.</p>"},
  {"q_en":"Q.4 (c) OR Write short note on Clam shell. (07 marks)","marks_en":"07 marks","marks_gu":"૦૭ ગુણ",
   "a_en":"<p>Clam shell is grab bucket with two hinged halves suspended by crane. Opens, drops, closes grabbing loose earth, lifts for deep narrow pits, under water, well sinking, pile bores. Capacity 0.5–2 m3, depth up to 30 m. Needs crane and skilled operator.</p>",
   "a_gu":"<p>Clam shell બે પાંખવાળો ગ્રેબ બકેટ ક્રેનથી લટકે. ખોલી નાખી બંધ કરી માટી પકડી ઉપર લાવે. ઊંડા સાંકડા ખાડા, પાણીમાં, well sinking 30 m.</p>"},
 ]
},
{
 "title_en":"Q5 · Maintenance, green/prefab, safety",
 "title_gu":"પ્ર.5 · જાળવણી, ગ્રીન/પ્રિફેબ, સલામતી",
 "cards":[
  {"q_en":"Q.5 (a) What are the purpose of Maintenance of Buildings ? (03 marks)","marks_en":"03 marks","marks_gu":"૦૩ ગુણ",
   "a_en":"<p>Retain structural safety and serviceability, prevent decay and damp, keep hygiene and comfort, preserve appearance and value, extend life, reduce major repair cost, meet statutory requirements.</p>",
   "a_gu":"<p>સલામતી સેવા ટકાવો, સડો ભીનાશ રોકો, સ્વચ્છતા આરામ, દેખાવ કિંમત જાળવો, આયુષ્ય વધારો, મોટા સમારકામ ખર્ચ ઘટાડો.</p>"},
  {"q_en":"Q.5 (b) Write advantages and disadvantages of Green Building Technology. (04 marks)","marks_en":"04 marks","marks_gu":"૦૪ ગુણ",
   "a_en":"<p><strong>Advantages:</strong> 30–40% energy saving, water harvesting, less CO2, healthy daylight ventilation, waste reduction, long-term low bills, LEED/GRIHA rating value.</p><p><strong>Disadvantages:</strong> 5–15% higher initial cost, needs skilled design, certified materials limited, maintenance training.</p>",
   "a_gu":"<p><strong>ફાયદા:</strong> 30–40% વીજ બચત, વરસાદી પાણી, CO2 ઓછું, તંદુરસ્ત પ્રકાશ હવા, કચરો ઓછો.</p><p><strong>ગેરફાયદા:</strong> શરૂઆત ખર્ચ 5–15% વધુ, કુશળ ડિઝાઇન, સામગ્રી મર્યાદિત.</p>"},
  {"q_en":"Q.5 (c) Explain Physical Causes of Accidents in Construction. (07 marks)","marks_en":"07 marks","marks_gu":"૦૭ ગુણ",
   "a_en":f"<p><strong>Physical unsafe conditions:</strong> Weak/unbraced scaffolds, unguarded edges and openings, faulty ladders, defective tools and machines, falling objects, collapse of trench/formwork, electrical naked wires, poor housekeeping, inadequate lighting/ventilation. Each causes fall, crush, electrocution.</p>"+fig(svg_fail,"Physical causes — weak scaffold, unguarded edge, faulty tools, collapse, electrical, poor housekeeping"),
   "a_gu":f"<p><strong>ભૌતિક અસુરક્ષિત સ્થિતિ:</strong> નબળું પાલખ, ખુલ્લી ધાર, ખામી સીડી, ખરાબ સાધન, પડતી વસ્તુ, ધસી પડવું, ખુલ્લા વાયર, અવ્યવસ્થા, પ્રકાશ/હવા ઓછા — પડવું, દબાવું, વીજળી.</p>"+fig(svg_fail,"અકસ્માત ભૌતિક કારણ — નબળું પાલખ, ખુલ્લી ધાર, ધસારો")},
  {"q_en":"Q.5 (a) OR Explain Repairing of Plaster. (03 marks)","marks_en":"03 marks","marks_gu":"૦૩ ગુણ",
   "a_en":"<p>Mark defective area, cut rectangular edges 10 mm deep, remove loose, clean, wet, apply bonding agent, first 6 mm scratch coat, second flush finishing, cure 7 days. Match existing thickness.</p>",
   "a_gu":"<p>ખરાબ ભાગ નિશાન, લંબચોરસ 10 mm કાપો, ખરાબ કાઢો, સાફ ભીનું, bonding, 6 mm scratch + finishing flush, 7 દિવસ પાણી.</p>"},
  {"q_en":"Q.5 (b) OR Write advantages and disadvantages of Pre-Fabricated Construction. (04 marks)","marks_en":"04 marks","marks_gu":"૦૪ ગુણ",
   "a_en":"<p><strong>Advantages:</strong> Factory quality, fast erection, less site labour and shuttering, weather independent, less waste.</p><p><strong>Disadvantages:</strong> Heavy transport needs crane, joint leakage risk, design rigid, initial mould cost high.</p>",
   "a_gu":"<p><strong>ફાયદા:</strong> ફેક્ટરી quality, ઝડપી, મજૂર ફોર્મવર્ક ઓછું, હવામાન અસર નહીં.</p><p><strong>ગેરફાયદા:</strong> ભારે transport ક્રેન, સાંધા લીક, ડિઝાઇન કઠણ, શરૂ ખર્ચ વધુ.</p>"},
  {"q_en":"Q.5 (c) OR Explain Safety in Excavation. (07 marks)","marks_en":"07 marks","marks_gu":"૦૭ ગુણ",
   "a_en":f"<p><strong>Safety measures:</strong> 1. Survey underground utilities. 2. Slope 1:1 or timber/steel shoring beyond 1.5 m. 3. Ladders every 7.5 m for exit. 4. Dewatering pumps, no workers near edge. 5. Barricades 1 m away, red lights night. 6. PPE helmet boots. 7. Daily inspection by engineer, stop during rain. 8. Spoil 1 m away from edge.</p>"+fig(svg_excav,"Excavation safety — slope/shoring, ladders, barricades 1 m away, PPE"),
   "a_gu":f"<p><strong>સલામતી:</strong> 1. ભૂગર્ભ લાઇન તપાસ. 2. 1:1 ઢાળ કે 1.5 m થી શોરિંગ. 3. દર 7.5 m નિસરણી. 4. પાણી ખેંચો ધાર પાસે ન ઊભા રહો. 5. 1 m દૂર barricade રાત્રે લાઇટ. 6. PPE. 7. રોજ તપાસ વરસાદમાં બંધ. 8. માટી ધારથી 1 m દૂર.</p>"+fig(svg_excav,"ખોદાણ સલામતી — ઢાળ/શોરિંગ, નિસરણી, barricade")},
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
    page=f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>DI03006011 · Winter 2025 solved paper</title><style>{CSS}</style></head><body><main class="page"><header class="hero"><div class="eyebrow">Solved question paper · English questions · Friendly Gujarati answers</div><div class="lang-switch" aria-label="Choose language"><button type="button" data-lang="en" aria-pressed="true">English</button><button type="button" data-lang="gu" aria-pressed="false">ગુજરાતી</button></div><h1>Construction Technology</h1><div class="meta">GTU Diploma · Civil · Semester 3 · Winter 2025 · DI03006011 · 04-12-2025 · 70 marks · 10:30 AM TO 01:00 PM</div></header>{"".join(sections_html)}<div class="footer">Solved paper for study. Verify with standard spec before site use.</div></main><script>document.querySelectorAll('.lang-switch button').forEach(b=>b.addEventListener('click',()=>{{document.documentElement.lang=b.dataset.lang;document.querySelectorAll('.lang-switch button').forEach(x=>x.setAttribute('aria-pressed',x===b?'true':'false'));}}));</script></body></html>'''
    return page
def main():
    page=build_page()
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
