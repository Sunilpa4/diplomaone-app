#!/usr/bin/env python3
from pathlib import Path
import html
ROOT=Path(__file__).resolve().parent.parent
def load_svg(name):
    p=ROOT/f"content/civil/sem3/DI03006051/diagrams/{name}"
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
svg_phase=load_svg("se2_phase.svg")
svg_2phase=load_svg("se2_2phase.svg")
svg_density=load_svg("se2_density.svg")
svg_pycno=load_svg("se2_pycno.svg")
svg_geocycle=load_svg("se1_geocycle.svg")
svg_psd=load_svg("se3_psd.svg")
svg_atterberg=load_svg("se3_atterberg.svg")
svg_casagrande=load_svg("se3_casagrande.svg")
svg_sieve=load_svg("se3_sieve.svg")
svg_proctor=load_svg("se5_proctor.svg")
svg_curve=load_svg("se5_curve.svg")
svg_rollers=load_svg("se5_rollers.svg")
svg_darcy=load_svg("se4_darcy.svg")
svg_tests=load_svg("se4_tests.svg")
svg_flownet=load_svg("se4_flownet.svg")
svg_quick=load_svg("se4_quick.svg")
svg_borelog=load_svg("se5_borelog.svg")
svg_plate=load_svg("se7_plate.svg")
svg_terzaghi=load_svg("se7_terzaghi.svg")
svg_failures=load_svg("se7_failures.svg")
svg_earth=load_svg("se7_earth.svg")
svg_mohr=load_svg("se6_mohr.svg")
svg_box=load_svg("se6_box.svg")
svg_law=load_svg("se6_law.svg")

SECTIONS=[
{
 "title_en":"Q1 · Soil basics, phases & density",
 "title_gu":"પ્ર.1 · માટીના મૂળભૂત, ફેઝ અને ઘનતા",
 "cards":[
  {"q_en":"Q.1 (a) Define soil, sand and water content. (03 marks)","marks_en":"03 marks","marks_gu":"૦૩ ગુણ",
   "a_en":"<p><strong>Soil:</strong> Natural aggregate of mineral particles with voids filled by water/air, formed by weathering of rocks.</p><p><strong>Sand:</strong> Coarse-grained fraction 0.075–4.75 mm, cohesionless, visible grains, IS classification.</p><p><strong>Water content w:</strong> Ratio of water mass to solids mass, w = M<sub>w</sub>/M<sub>s</sub>·100%, measured by oven drying at 105°C.</p>",
   "a_gu":"<p><strong>Soil માટી:</strong> ખડકના weathering થી બનેલ ખનિજ કણો + voids માં water/air.</p><p><strong>Sand રેતી:</strong> 0.075–4.75 mm coarse-grained, cohesionless.</p><p><strong>Water content w:</strong> પાણીનું વજન / ઘન કણોનું વજન ·100%, oven drying થી મળે. English keywords: soil, sand, water content, void.</p>"},
  {"q_en":"Q.1 (b) Draw three phase diagram of soil; give full name of all parts. (04 marks)","marks_en":"04 marks","marks_gu":"૦૪ ગુણ",
   "a_en":"<p><strong>Three-phase system:</strong> Soil has solids + water + air. Diagram shows volumes V<sub>a</sub> air, V<sub>w</sub> water, V<sub>s</sub> solids and weights W<sub>a</sub>≈0, W<sub>w</sub>, W<sub>s</sub>.</p><p>Full names: V<sub>a</sub>=Volume of air, V<sub>w</sub>=Volume of water, V<sub>s</sub>=Volume of solids, V<sub>v</sub>=V<sub>a</sub>+V<sub>w</sub> voids, W<sub>s</sub>=Weight of solids. Relations: n=V<sub>v</sub>/V, e=V<sub>v</sub>/V<sub>s</sub>, S<sub>r</sub>=V<sub>w</sub>/V<sub>v</sub>·100%.</p>"+fig(svg_phase,"Three-phase diagram — volumes Va, Vw, Vs and weights Wa, Ww, Ws"),
   "a_gu":"<p><strong>Three-phase diagram:</strong> માટીમાં solids + water + air. Volumes V_a, V_w, V_s અને weights W_s, W_w.</p><p>V_v = V_a+V_w voids, n= V_v/V, e=V_v/V_s, Sr=V_w/V_v. English keywords: three phase, void ratio e, porosity n, degree of saturation Sr.</p>"+fig(svg_phase,"Soil three-phase — Va, Vw, Vs, Ws")},
  {"q_en":"Q.1 (c) Explain core cutter method for determination of density of soil. (07 marks)","marks_en":"07 marks","marks_gu":"૦૭ ગુણ",
   "a_en":"<p><strong>Objective:</strong> Find field bulk density γ = W/V and dry density γ<sub>d</sub>=γ/[1+w] for cohesive soils using core cutter.</p><p><strong>Apparatus [IS 2720 Part 29]:</strong> Cylindrical cutter 10 cm dia 12.7 cm height V≈1000 cc, dolly 2.5 cm, rammer, balance, palette, oven.</p><p><strong>Step 1 — Calibration:</strong> Measure cutter inner dia D and height H, volume V=πD²H/4. Weigh empty cutter W<sub>1</sub>.</p><p><strong>Step 2 — Field driving:</strong> Clean ground, place cutter with dolly, drive with rammer till dolly sinks, excavate, trim top/bottom flush with straight edge.</p><p><strong>Step 3 — Weighing:</strong> Weigh cutter+soil W<sub>2</sub>, soil weight W=W<sub>2</sub>−W<sub>1</sub>, bulk density γ=W/V g/cm³.</p><p><strong>Step 4 — Water content:</strong> Take representative sample, oven dry to get w.</p><p><strong>Step 5 — Calculations:</strong> γ<sub>d</sub>=γ/[1+w], void ratio e=Gγ<sub>w</sub>/γ<sub>d</sub>−1.</p><p><strong>Precautions:</strong> Suitable only for soft cohesive soils, not gravel, drive vertical, avoid shattering, trim without voids.</p><p><strong>Limitation & Use:</strong> Quick field γ for compaction control vs sand replacement for granular. Report γ, γ<sub>d</sub>, w.</p>"+fig(svg_density,"Core cutter — cutter, dolly, bulk density γ=W/V, dry density γd=γ/[1+w]"),
   "a_gu":"<p><strong>Core cutter method:</strong> Field માં bulk density γ=W/V કાઢવા, cohesive soil માટે.</p><p><strong>Apparatus:</strong> Cutter 10 cm dia, dolly, rammer, balance, oven.</p><p><strong>Steps:</strong> 1] V=πD²H/4 અને ખાલી વજન W1, 2] જમીન પર dolly સાથે rammer થી drive કરો, trim કરો, 3] W2 વજન કરી W=W2−W1 ⇒ γ=W/V, 4] નમૂનામાંથી w, 5] γd=γ/[1+w].</p><p><strong>Care:</strong> Gravel માં નહીં, vertical drive. English keywords: bulk density, dry density, core cutter, water content.</p>"+fig(svg_density,"Core cutter steps — drive, weigh, γ, γd")},
  {"q_en":"Q.1 (c) OR A soil sample has bulk density 1.714 gm/cm³, water content 20% & specific gravity 2.7. Calculate dry density, void ratio & degree of saturation. (07 marks)","marks_en":"07 marks","marks_gu":"૦૭ ગુણ",
   "a_en":"<p><strong>Given Data:</strong> Bulk density γ =1.714 g/cm³, w=20%=0.20, G=2.7, γ<sub>w</sub>=1 g/cm³.</p><p><strong>Concept:</strong> From phase relations γ = [G·γ<sub>w</sub>·[1+w]]/[1+e], γ<sub>d</sub>=γ/[1+w], e=G·γ<sub>w</sub>/γ<sub>d</sub>−1, S<sub>r</sub>=w·G/e.</p><div class=\"eq\">γ<sub>d</sub>=γ/[1+w] ,  e=G·γ<sub>w</sub>/γ<sub>d</sub>−1 ,  S<sub>r</sub>=w·G/e·100%</div><p><strong>Step 1 — Dry density:</strong> γ<sub>d</sub>=1.714/1.20=1.428 g/cm³ =14.01 kN/m³.</p><p><strong>Step 2 — Void ratio:</strong> e=2.7·1/1.428−1=1.891−1=0.891.</p><p><strong>Step 3 — Degree of saturation:</strong> S<sub>r</sub>=0.20·2.7/0.891=0.606=60.6%.</p><p><strong>Step 4 — Checks:</strong> Also γ= [G+w·G]/[1+e]·γ<sub>w</sub>=[2.7+0.54]/1.891=1.713 matches. Porosity n=e/[1+e]=0.471=47.1%.</p><p><strong>Answer for 7 marks:</strong> Draw phase diagram, write formulas, substitute with units g/cm³, show division, <strong>γ<sub>d</sub>=1.43 g/cm³, e=0.89, S<sub>r</sub>=60.6%</strong>. Mention if saturated γ<sub>sat</sub> would be higher.</p>",
   "a_gu":"<p><strong>Given:</strong> Bulk γ1.714 g/cm³ w20% G2.7.</p><p><strong>Formulas:</strong> γd=γ/[1+w], e=G·γw/γd−1, Sr=w·G/e.</p><p><strong>Step 1:</strong> γd=1.714/1.2=1.428 g/cm³.</p><p><strong>Step 2:</strong> e=2.7/1.428−1=0.891.</p><p><strong>Step 3:</strong> Sr=0.2·2.7/0.891=60.6%.</p><p><strong>Answer:</strong> γd1.43, e0.89, Sr60.6% — phase diagram દોરી formulas લખો. English keywords: bulk density, dry density, void ratio, degree of saturation, specific gravity.</p>"},
 ]
},
{
 "title_en":"Q2 · Index properties, Cu, Cc & Atterberg",
 "title_gu":"પ્ર.2 · ઇન્ડેક્સ ગુણધર્મ, Cu, Cc અને એટરબર્ગ",
 "cards":[
  {"q_en":"Q.2 (a) Give fundamental uses of soil. (03 marks)","marks_en":"03 marks","marks_gu":"૦૩ ગુણ",
   "a_en":"<p>1] Foundation support for buildings, 2] Construction material for embankments, dams, 3] Subgrade for roads/railways, 4] Burial medium for pipelines, 5] Source of minerals. Soil mechanics ensures stability and settlement control.</p>",
   "a_gu":"<p>1] Foundation support, 2] Embankment/dam material, 3] Road subgrade, 4] Pipeline bed, 5] Minerals source. English keywords: foundation, embankment, subgrade.</p>"},
  {"q_en":"Q.2 (b) After test of soil sample following properties collected: (I) LL=25% (II) PL=15% (III) D10=0.17mm (IV) D30=0.38mm (V) D60=0.75mm. Calculate uniformity coefficient & coefficient of curvature. (04 marks)","marks_en":"04 marks","marks_gu":"૦૪ ગુણ",
   "a_en":"<p><strong>Given:</strong> D<sub>10</sub>=0.17 mm [effective size], D<sub>30</sub>=0.38 mm, D<sub>60</sub>=0.75 mm.</p><div class=\"eq\">C<sub>u</sub>=D<sub>60</sub>/D<sub>10</sub> ,  C<sub>c</sub>=D<sub>30</sub>²/[D<sub>60</sub>·D<sub>10</sub>]</div><p><strong>Step 1 — Cu:</strong> 0.75/0.17=4.41.</p><p><strong>Step 2 — Cc:</strong> 0.38²/[0.75·0.17]=0.1444/0.1275=1.13.</p><p><strong>Interpretation:</strong> Cu>4 and 1<Cc<3 indicates well-graded sand [IS]. LL/PL not needed for Cu/Cc — for classification PI=10% later.</p>",
   "a_gu":"<p><strong>Given:</strong> D10 0.17 mm D30 0.38 mm D60 0.75 mm.</p><p><strong>Cu:</strong> D60/D10=4.41, <strong>Cc:</strong> D30²/D60·D10=1.13 — well-graded sand. English keywords: uniformity coefficient Cu, curvature Cc, effective size D10.</p>"+fig(svg_psd,"PSD curve — D10, D30, D60, Cu=D60/D10, Cc=D30²/D60·D10")},
  {"q_en":"Q.2 (c) Explain the method to find liquid limit of soil. (07 marks)","marks_en":"07 marks","marks_gu":"૦૭ ગુણ",
   "a_en":"<p><strong>Objective [IS 2720 Part 5]:</strong> Water content at which soil flows to close 12 mm groove after 25 blows in Casagrande apparatus.</p><p><strong>Apparatus:</strong> Casagrande cup, grooving tools Type A/B, sieved soil <425 µm, spatula, 6–8 containers, oven.</p><p><strong>Step 1 — Preparation:</strong> Take 120 g air-dried 425 µ soil, add distilled water, mix to paste, cure 24 h.</p><p><strong>Step 2 — First trial:</strong> Place paste in cup max 10 mm thick, cut 12 mm groove along centre, rotate crank 2 rps, count blows N to close 12 mm at bottom. Take water content w.</p><p><strong>Step 3 — Repeat:</strong> Change water to get N≈10–40, 4–5 readings. For each N measure w by oven drying.</p><p><strong>Step 4 — Flow curve:</strong> Plot w [Y linear] vs log N [X]. Best-fit straight line. Liquid limit LL is w at N=25 from curve.</p><p><strong>Step 5 — Alternative cone:</strong> 80 g cone 30°, penetration 20 mm in 5 s gives LL [IS].</p><p><strong>Uses:</strong> Classification, PI=LL−PL, toughness index. Reproducible within 2%.</p>"+fig(svg_casagrande,"Casagrande apparatus — cup, groove, blows vs water content, LL at 25 blows"),
   "a_gu":"<p><strong>Liquid limit:</strong> 25 blows પર groove 12 mm બંધ થાય તે w.</p><p><strong>Apparatus:</strong> Casagrande cup, grooving tool, 425 µ soil.</p><p><strong>Steps:</strong> 1] Paste બનાવો, 2] Cup માં મૂકી groove કાપો, 2 rps પર blows ગણો અને w કાઢો, 3] 4–5 વખત N10–40, 4] Flow curve w vs logN દોરો, N25 પર LL વાંચો. English keywords: liquid limit, Casagrande, flow curve, blows.</p>"+fig(svg_casagrande,"Liquid limit — flow curve LL at 25 blows")},
  {"q_en":"Q.2 (a) OR Draw chart of Indian Standard classification for soil. (03 marks)","marks_en":"03 marks","marks_gu":"૦૩ ગુણ",
   "a_en":"<p>IS 1498 chart: Coarse >50% retained 4.75 mm → GW, GP, GM, GC and SW, SP, SM, SC based on Cu, Cc, fines PI. Fine >50% passing 75 µ → ML, CL, OL vs MH, CH, OH via A-line PI=0.73[LL−20] and LL 35/50 thresholds. Organic OL/OH below A-line. Show flow diagram coarse→fine→A-line.</p>"+fig(svg_sieve,"IS classification flow chart — coarse vs fine, GW, GP, SW, SP, ML, CL, CH etc."),
   "a_gu":"<p>IS 1498 માં coarse >50% 4.75 mm → GW, GP, SW etc based on Cu, Cc; fine માટે A-line PI=0.73[LL−20] અને LL 35/50. English keywords: IS classification, A-line, GW, CL, CH.</p>"+fig(svg_sieve,"IS soil classification chart")},
  {"q_en":"Q.2 (b) OR A soil sample has w=50%, LL=55% PL=26% Calculate PI and LI. (04 marks)","marks_en":"04 marks","marks_gu":"૦૪ ગુણ",
   "a_en":"<div class=\"eq\">PI=LL−PL ,  LI=[w−PL]/PI ,  CI=[LL−w]/PI</div><p>PI=55−26=29%, LI=[50−26]/29=0.827, also CI=0.173. LI 0.8 indicates near liquid state, soft. Consistent: LI+CI=1.</p>",
   "a_gu":"<p>PI=LL−PL=29%, LI=[w−PL]/PI=0.827, CI=0.17. LI near 1 = liquid state. English keywords: plasticity index PI, liquidity index LI.</p>"},
  {"q_en":"Q.2 (c) OR Explain and draw particle size distribution curve for soil. (07 marks)","marks_en":"07 marks","marks_gu":"૦૭ ગુણ",
   "a_en":"<p><strong>Objective:</strong> Show % finer vs particle size [0.001–100 mm log scale] via sieve + hydrometer.</p><p><strong>Step 1 — Sieve analysis [>75 µ]:</strong> Oven dry sample, stack IS sieves 4.75 mm–75 µ, shake, weigh retained, % retained, % finer.</p><p><strong>Step 2 — Sedimentation [<75 µ]:</strong> Stokes law v=[G−1]γ<sub>w</sub>D²/18µ, hydrometer at intervals, % finer.</p><p><strong>Step 3 — Plot:</strong> X log size, Y % finer linear. Read D<sub>10</sub>, D<sub>30</sub>, D<sub>60</sub>, compute Cu, Cc. Shape indicates well-graded [S-shaped], gap-graded [step], uniform [flat].</p><p><strong>Uses:</strong> Classification, permeability estimate k∝D<sub>10</sub>², filter design.</p>"+fig(svg_psd,"Particle size distribution — log size vs % finer, sieve + hydrometer, Cu, Cc"),
   "a_gu":"<p><strong>PSD curve:</strong> % finer vs log size. Sieve >75 µ અને hydrometer <75 µ.</p><p>Stokes law થી D, D10 D30 D60 વાંચી Cu, Cc. Shape well-graded/gap/uniform. English keywords: PSD curve, sieve, hydrometer, Cu, Cc, D10.</p>"+fig(svg_psd,"PSD — % finer vs log size")},
 ]
},
{
 "title_en":"Q3 · Compaction, consolidation & Proctor",
 "title_gu":"પ્ર.3 · કોમ્પેક્શન, કોન્સોલિડેશન અને પ્રોક્ટર",
 "cards":[
  {"q_en":"Q.3 (a) List out name of factors affecting compaction. (03 marks)","marks_en":"03 marks","marks_gu":"૦૩ ગુણ",
   "a_en":"<p>1] Water content, 2] Compactive effort [rammer weight, drops, layers], 3] Soil type [gradation, clay mineral], 4] Admixtures [salts], 5] Layer thickness, 6] Method [static, vibratory].</p>",
   "a_gu":"<p>1] Water content, 2] Compactive effort, 3] Soil type, 4] Admixtures, 5] Layer thickness, 6] Method. English keywords: compaction, water content, effort.</p>"},
  {"q_en":"Q.3 (b) Give difference of compaction and consolidation. (04 marks)","marks_en":"04 marks","marks_gu":"૦૪ ગુણ",
   "a_en":"<table><tr><th>Compaction</th><th>Consolidation</th></tr><tr><td>Mechanical expulsion of air — short term</td><td>Expulsion of pore water under sustained load — long term</td></tr><tr><td>Dynamic/impact load</td><td>Static sustained load</td></tr><tr><td>Unsaturated zone</td><td>Saturated clay</td></tr><tr><td>Increases density quickly</td><td>Settlement over years</td></tr></table>",
   "a_gu":"<table><tr><th>Compaction</th><th>Consolidation</th></tr><tr><td>હવા કાઢવી — ટૂંકા ગાળા</td><td>પાણી કાઢવું — લાંબા ગાળા</td></tr><tr><td>Dynamic impact</td><td>Static sustained</td></tr></table>"},
  {"q_en":"Q.3 (c) Explain standard proctor test. (07 marks)","marks_en":"07 marks","marks_gu":"૦૭ ગુણ",
   "a_en":"<p><strong>Aim [IS 2720 Part 7]:</strong> Find Optimum Moisture Content OMC and Maximum Dry Density MDD for a given compactive effort.</p><p><strong>Apparatus:</strong> Mould 1000 cc 10 cm dia, rammer 2.6 kg drop 310 mm, IS sieve 20 mm, oven, balance.</p><p><strong>Step 1 — Preparation:</strong> Take 3 kg air-dry soil 20 mm passing, add water 6% trial, mix temper 16 h.</p><p><strong>Step 2 — Compaction:</strong> Fill mould in 3 layers, each 25 blows evenly, trim top, weigh W<sub>2</sub>.</p><p><strong>Step 3 — w & γ<sub>d</sub>:</strong> Take sample for w, bulk γ=W/V, dry γ<sub>d</sub>=γ/[1+w].</p><p><strong>Step 4 — Repeat:</strong> Increase water by 2–3% each trial 5–6 times until γ<sub>d</sub> falls after peak.</p><p><strong>Step 5 — Curve:</strong> Plot γ<sub>d</sub> vs w, peak gives MDD and OMC. Also plot 0% air voids γ<sub>d</sub>=G·γ<sub>w</sub>/[1+w·G/S<sub>r</sub>].</p><p><strong>Energy:</strong> 592 kJ/m³ [Standard vs Modified 2700 kJ/m³]. Use for field control ≥95% MDD.</p>"+fig(svg_proctor,"Standard Proctor — mould, 2.6 kg rammer, 3 layers 25 blows, γd vs w curve OMC, MDD"),
   "a_gu":"<p><strong>Standard Proctor [IS 2720-7]:</strong> OMC અને MDD શોધવા.</p><p><strong>Apparatus:</strong> 1000 cc mould, 2.6 kg rammer 310 mm drop.</p><p><strong>Steps:</strong> 1] 3 kg soil માં પાણી ઉમેરો, 2] 3 layers દરેક 25 blows, trim weigh, 3] w લઈ γd=γ/[1+w], 4] 5–6 trials, 5] γd vs w curve peak = MDD/OMC. English keywords: OMC, MDD, compactive effort, dry density.</p>"+fig(svg_proctor,"Standard Proctor curve — OMC, MDD")},
  {"q_en":"Q.3 (a) OR Give name of methods of compaction in the field. (03 marks)","marks_en":"03 marks","marks_gu":"૦૩ ગુણ",
   "a_en":"<p>Smooth wheel roller, pneumatic tyre roller, sheepfoot roller, vibratory roller, impact/rammer tamper, grid roller. Choice depends on soil type and layer thickness.</p>"+fig(svg_rollers,"Field rollers — smooth, pneumatic, sheepfoot, vibratory, tamper"),
   "a_gu":"<p>Smooth, pneumatic, sheepfoot, vibratory, tamper, grid roller. English keywords: roller, compaction.</p>"+fig(svg_rollers,"Field compaction methods")},
  {"q_en":"Q.3 (b) OR Classify effects of compaction on the properties of soil. (04 marks)","marks_en":"04 marks","marks_gu":"૦૪ ગુણ",
   "a_en":"<p>1] Increases shear strength, bearing capacity, 2] Reduces permeability, compressibility, settlement, 3] Reduces frost susceptibility, swelling, 4] Improves stability on wetting. Dry of optimum brittle, wet of optimum ductile with higher pore pressure.</p>",
   "a_gu":"<p>1] Shear strength વધે, 2] Permeability settlement ઘટે, 3] Swelling frost ઘટે, 4] Stability વધે. English keywords: shear strength, permeability, compressibility.</p>"},
  {"q_en":"Q.3 (c) OR The following observation were made in a proctor compaction test, w 8% 10% 12% 15% Bulk Density 2.20 2.40 2.50 2.30 Mg/m³ Calculate OMC & MDD from graph. (07 marks)","marks_en":"07 marks","marks_gu":"૦૭ ગુણ",
   "a_en":"<p><strong>Given:</strong> w[8,10,12,15]%, γ[2.20,2.40,2.50,2.30] Mg/m³ = g/cm³.</p><div class=\"eq\">γ<sub>d</sub>=γ/[1+w]</div><p><strong>Step 1 — Compute dry densities:</strong></p><table><tr><th>w [%]</th><th>γ [Mg/m³]</th><th>1+w</th><th>γ<sub>d</sub>=γ/[1+w]</th></tr><tr><td>8</td><td>2.20</td><td>1.08</td><td>2.037</td></tr><tr><td>10</td><td>2.40</td><td>1.10</td><td>2.182</td></tr><tr><td>12</td><td>2.50</td><td>1.12</td><td>2.232</td></tr><tr><td>15</td><td>2.30</td><td>1.15</td><td>2.000</td></tr></table><p><strong>Step 2 — Plot:</strong> γ<sub>d</sub> vs w, points rise to 12% then fall. Peak at w≈12%, γ<sub>d</sub>≈2.23 Mg/m³.</p><p><strong>Step 3 — Answer:</strong> <strong>OMC≈12%, MDD≈2.23 Mg/m³ =2.23 g/cm³ =21.9 kN/m³.</strong> Verify zero-air line not crossed. Mention modified Proctor gives higher MDD lower OMC due to more energy.</p>"+fig(svg_curve,"Proctor curve γd vs w — peak MDD 2.23 at OMC 12%"),
   "a_gu":"<p><strong>Given:</strong> w8,10,12,15% γ2.20,2.40,2.50,2.30 Mg/m³.</p><p><strong>γd=γ/[1+w]:</strong> 2.037, 2.182, 2.232, 2.00. Plot કરો peak 12% પર MDD2.23. <strong>OMC12% MDD2.23 Mg/m³.</strong> English keywords: OMC, MDD, dry density, compaction curve.</p>"+fig(svg_curve,"MDD/OMC from graph")},
 ]
},
{
 "title_en":"Q4 · Permeability, shear strength & seepage",
 "title_gu":"પ્ર.4 · પારગમ્યતા, શીયર સ્ટ્રેન્થ અને સીપેજ",
 "cards":[
  {"q_en":"Q.4 (a) Describe importance of permeability in civil engineering. (03 marks)","marks_en":"03 marks","marks_gu":"૦૩ ગુણ",
   "a_en":"<p>Controls seepage under dams, excavation dewatering, drainage design, consolidation rate, well yield, stability of slopes/retaining walls affected by pore pressure. Low k needed for core, high k for filters/drains.</p>",
   "a_gu":"<p>Seepage, dewatering, drainage, consolidation, well yield, slope stability — permeability નું મહત્વ. English keywords: permeability, seepage, drainage.</p>"},
  {"q_en":"Q.4 (b) Define cohesion, internal friction, shear strength and angle of repose. (04 marks)","marks_en":"04 marks","marks_gu":"૦૪ ગુણ",
   "a_en":"<p><strong>Cohesion c:</strong> Intermolecular bond shear resistance at zero normal stress, due to electrostatic forces in clay.</p><p><strong>Angle internal friction φ:</strong> Resistance due to interlocking, τ=σ·tanφ at zero cohesion.</p><p><strong>Shear strength τ<sub>f</sub>:</strong> Max shear before failure, τ<sub>f</sub>=c+σ·tanφ [Coulomb].</p><p><strong>Angle of repose θ:</strong> Max heap slope without sliding, for granular θ≈φ.</p>"+fig(svg_law,"Coulomb τ=c+σ·tanφ — cohesion, φ, shear strength, repose"),
   "a_gu":"<p><strong>Cohesion c:</strong> zero normal પર shear resistance clay માં.</p><p><strong>φ:</strong> interlocking resistance.</p><p><strong>τf=c+σ·tanφ:</strong> shear strength.</p><p><strong>Angle of repose:</strong> heap નો max slope ≈φ. English keywords: cohesion, friction, shear strength.</p>"+fig(svg_law,"Shear strength law")},
  {"q_en":"Q.4 (c) Explain factors affecting Permeability in soil. (07 marks)","marks_en":"07 marks","marks_gu":"૦૭ ગુણ",
   "a_en":"<p><strong>Darcy's law:</strong> v=k·i, k coefficient of permeability.</p><p>1] <strong>Grain size:</strong> Coarse → high k ∝ D<sub>10</sub>² [Hazen k= C·D<sub>10</sub>²].</p><p>2] <strong>Void ratio e:</strong> k ∝ e³/[1+e] [Kozeny-Carman], compaction reduces k.</p><p>3] <strong>Composition:</strong> Clay mineral montmorillonite low k due to adsorbed water.</p><p>4] <strong>Structure:</strong> Flocculated higher k than dispersed.</p><p>5] <strong>Fabric/stratification:</strong> Horizontal k >> vertical k [k<sub>h</sub>≈k<sub>v</sub>·5].</p><p>6] <strong>Degree saturation:</strong> Partial saturation blocks voids with air, k falls.</p><p>7] <strong>Fluid viscosity/temperature:</strong> k ∝ γ<sub>w</sub>/µ, warm water higher k.</p><p><strong>Uses:</strong> Filter design needs controlled k, dam core low k.</p>"+fig(svg_tests,"Factors — grain size, void ratio, clay mineral, structure, stratification, saturation, viscosity"),
   "a_gu":"<p><strong>k પર અસર:</strong> 1] Grain size D10², 2] Void ratio e³/[1+e], 3] Clay mineral, 4] Structure flocculated/dispersed, 5] k_h>k_v, 6] Saturation, 7] Viscosity/temperature.</p><p>English keywords: permeability, Darcy, void ratio, grain size.</p>"+fig(svg_tests,"Permeability factors")},
  {"q_en":"Q.4 (a) OR Define permeability, seepage and piping failure. (03 marks)","marks_en":"03 marks","marks_gu":"૦૩ ગુણ",
   "a_en":"<p><strong>Permeability k:</strong> Ability to transmit water under head, q=k·i·A.</p><p><strong>Seepage:</strong> Flow through soil due to head difference, causes pore pressure.</p><p><strong>Piping:</strong> Progressive erosion by seepage forming pipe channel, failure when exit gradient i<sub>e</sub>≥i<sub>cr</sub>= [G−1]/[1+e].</p>",
   "a_gu":"<p><strong>Permeability:</strong> પાણી પસાર કરવાની ક્ષમતા k.</p><p><strong>Seepage:</strong> head difference થી flow.</p><p><strong>Piping:</strong> seepage થી erosion pipe બની failure, i_cr=[G−1]/[1+e]. English keywords: permeability, seepage, piping, gradient.</p>"},
  {"q_en":"Q.4 (b) OR List out name of tests used to determine shear strength of soil in laboratory. (04 marks)","marks_en":"04 marks","marks_gu":"૦૪ ગુણ",
   "a_en":"<p>1] Direct shear/box shear test, 2] Triaxial UU/CU/CD, 3] Unconfined compression UCS, 4] Vane shear, 5] Laboratory shear vane. Field: SPT, CPT, vane.</p>"+fig(svg_box,"Lab shear tests — box shear, triaxial, UCS, vane"),
   "a_gu":"<p>1] Box shear, 2] Triaxial UU/CU/CD, 3] UCS, 4] Vane shear. English keywords: shear strength, triaxial, box shear.</p>"+fig(svg_box,"Shear tests lab")},
  {"q_en":"Q.4 (c) OR During permeability test following observations: permeameter dia 100mm L128mm, stand pipe dia 10mm, head 150→110mm in 30 min. Calculate permeability. (07 marks)","marks_en":"07 marks","marks_gu":"૦૭ ગુણ",
   "a_en":"<p><strong>Given:</strong> Permeameter D=100 mm ⇒ A=π·50²=7854 mm², L=128 mm, stand pipe d=10 mm ⇒ a=π·5²=78.54 mm², h<sub>1</sub>=150 mm, h<sub>2</sub>=110 mm, t=30 min=1800 s.</p><p><strong>Concept — Falling head [variable head]:</strong> For low permeability clay, water level falls in stand pipe, Darcy q=k·i·A, integration gives log decay.</p><div class=\"eq\">k=2.3·a·L/[A·t]·log<sub>10</sub>[h<sub>1</sub>/h<sub>2</sub>]</div><p><strong>Step 1 — Areas:</strong> a=78.54 mm², A=7854 mm², ratio a/A=0.01.</p><p><strong>Step 2 — Log term:</strong> log[150/110]=log[1.3636]=0.1347.</p><p><strong>Step 3 — k:</strong> k=2.3·78.54·128/[7854·1800]·0.1347=23120/14,137,200·0.1347=0.001635·0.1347=2.20×10⁻⁴ mm/s.</p><p><strong>Step 4 — Units:</strong> =2.20×10⁻⁵ cm/s =2.20×10⁻⁷ m/s. For 7 marks note assumptions laminar flow, saturated, no side leakage.</p><p><strong>Answer:</strong> <strong>k≈2.2×10⁻⁴ mm/s =2.2×10⁻⁵ cm/s</strong>, low permeability clay-silt range.</p>"+fig(svg_darcy,"Falling head k=2.3aL/At·log[h1/h2]=2.2×10⁻⁴ mm/s"),
   "a_gu":"<p><strong>Given:</strong> D100 L128 mm, stand pipe 10 mm, h150→110 mm t30 min.</p><p><strong>Falling head:</strong> k=2.3·a·L/[A·t]·log[h1/h2]. a78.54 A7854 log0.1347 ⇒ k2.2×10⁻⁴ mm/s =2.2×10⁻⁵ cm/s. English keywords: falling head, permeability, stand pipe, Darcy.</p>"+fig(svg_darcy,"Falling head permeability")},
 ]
},
{
 "title_en":"Q5 · Shear failure, exploration & foundations",
 "title_gu":"પ્ર.5 · શીયર ભંગાણ, એક્સપ્લોરેશન અને પાયા",
 "cards":[
  {"q_en":"Q.5 (a) Calculate shear strength of frictionless cohesive soil having C=8.5 N/mm². (03 marks)","marks_en":"03 marks","marks_gu":"૦૩ ગુણ",
   "a_en":"<p>For φ=0 cohesive soil Coulomb τ<sub>f</sub>=C+σ·tanφ = C =8.5 N/mm². If units intended kN/m² [typical], τ=8.5 kPa. For any σ, strength = cohesion only, independent of normal stress. Note 8.5 N/mm²=8500 kPa unrealistically high — likely 8.5 kN/m²; exam still τ=8.5 [same units].</p>",
   "a_gu":"<p>φ=0 માટે τf=C+σ·tan0=C=8.5 N/mm² [જો kN/m² તો 8.5 kPa]. Normal stress ની અસર નહીં. English keywords: shear strength, cohesion, friction.</p>"},
  {"q_en":"Q.5 (b) Summarize objectives of site exploration. (04 marks)","marks_en":"04 marks","marks_gu":"૦૪ ગુણ",
   "a_en":"<p>1] Know soil profile & strata, 2] Depth of bedrock/water table, 3] Engineering properties & bearing capacity, 4] Suitable foundation type/depth, 5] Construction problems, 6] Material source for fill. Methods: borings, trial pits, geophysics, sampling.</p>"+fig(svg_borelog,"Site exploration — borehole log, strata, water table, bearing capacity"),
   "a_gu":"<p>1] Soil profile, 2] Bedrock/water table, 3] Properties & bearing, 4] Foundation type, 5] Construction issues. English keywords: site exploration, bore log, bearing capacity.</p>"+fig(svg_borelog,"Site exploration objectives")},
  {"q_en":"Q.5 (c) Differentiate between general & local shear failure in soil. (07 marks)","marks_en":"07 marks","marks_gu":"૦ે ગુણ",
   "a_en":"<table><tr><th>General shear</th><th>Local shear</th></tr><tr><td>Sudden, well-defined slip surface to ground surface, load-settlement curve peak</td><td>Gradual, partial slip surface, no clear peak, large settlement</td></tr><tr><td>In dense sand/ stiff clay with high relative density</td><td>In loose sand/ soft clay low density</td></tr><tr><td>Bearing capacity high, Terzaghi q<sub>u</sub>=cN<sub>c</sub>+γD<sub>f</sub>N<sub>q</sub>+0.5γBN<sub>γ</sub></td><td>Reduced due to compressibility — c′=2/3c, φ′≈reduced</td></tr><tr><td>Heave on sides visible</td><td>Heave minimal, punching type</td></tr><tr><td>Failure at small strain</td><td>Large strain before failure</td></tr></table><p><strong>Diagram:</strong> General shows full rupture lines to surface, local shows limited wedge. Use Terzaghi local shear reduces N factors.</p>"+fig(svg_failures,"General vs local shear — rupture surface, load-settlement, dense vs loose"),
   "a_gu":"<table><tr><th>General shear</th><th>Local shear</th></tr><tr><td>અચાનક slip surface ground સુધી, peak load</td><td>ક્રમશઃ partial surface, peak નહીં large settlement</td></tr><tr><td>Dense sand/stiff clay</td><td>Loose/soft</td></tr><tr><td>Bearing high q_u formula</td><td>Compressibility થી ઓછું c′=2/3c</td></tr></table><p>English keywords: general shear, local shear, bearing capacity, slip surface.</p>"+fig(svg_failures,"General vs local failure")},
  {"q_en":"Q.5 (a) OR Describe soil samples in field. (03 marks)","marks_en":"03 marks","marks_gu":"૦૩ ગુણ",
   "a_en":"<p><strong>Disturbed:</strong> Structure altered, used for classification, w, G.</p><p><strong>Undisturbed:</strong> Intact structure via thin-wall sampler, for strength/compressibility.</p><p><strong>Non-representative:</strong> Mixed with drilling fluid, only for strata ID.</p>",
   "a_gu":"<p><strong>Disturbed:</strong> structure બગડી classification માટે.</p><p><strong>Undisturbed:</strong> intact strength માટે thin-wall sampler.</p><p><strong>Non-representative:</strong> drilling fluid mix. English keywords: disturbed, undisturbed, sampler.</p>"},
  {"q_en":"Q.5 (b) OR Define lateral earth pressure and give name of its types. (04 marks)","marks_en":"04 marks","marks_gu":"૦૪ ગુણ",
   "a_en":"<p><strong>Lateral earth pressure:</strong> Horizontal stress exerted by soil on retaining structure per unit area.</p><p>Types: 1] At-rest p<sub>0</sub>=K<sub>0</sub>·γ·z, no movement, 2] Active p<sub>a</sub>=K<sub>a</sub>·γ·z when wall moves away, K<sub>a</sub>=tan²[45−φ/2], 3] Passive p<sub>p</sub>=K<sub>p</sub>·γ·z when wall pushes, K<sub>p</sub>=tan²[45+φ/2].</p>"+fig(svg_earth,"Earth pressure — at-rest K0, active Ka, passive Kp, Kactive/Kpassive"),
   "a_gu":"<p><strong>Lateral earth pressure:</strong> retaining wall પર horizontal stress.</p><p>1] At-rest K0, 2] Active Ka=tan²[45−φ/2] wall away, 3] Passive Kp=tan²[45+φ/2] wall push. English keywords: active, passive, at-rest, Ka, Kp.</p>"+fig(svg_earth,"Lateral earth pressure types")},
  {"q_en":"Q.5 (c) OR Enlist types of shallow and deep foundations and draw sketch of strap footing. (07 marks)","marks_en":"07 marks","marks_gu":"૦૭ ગુણ",
   "a_en":"<p><strong>Shallow [D<sub>f</sub>/B≤1]:</strong> Isolated footing, combined, strap/cantilever, mat/raft, stepped.</p><p><strong>Deep [D<sub>f</sub>/B>1]:</strong> Pile [driven, bored], well/caisson, pier.</p><p><strong>Strap footing:</strong> Two isolated footings connected by rigid beam strap to balance eccentric load, strap takes moment, footings take vertical. Draw plan: two rectangular bases with strap beam spanning, no contact pressure under strap. Use when property line footing eccentric.</p><p><strong>Choice:</strong> Based on bearing capacity, settlement, water table, structure load. Shallow if good soil near surface else deep piles to hard stratum.</p>"+fig(svg_terzaghi,"Strap footing — two footings + strap beam, eccentric balancing, shallow vs deep types"),
   "a_gu":"<p><strong>Shallow:</strong> Isolated, combined, strap, mat/raft.</p><p><strong>Deep:</strong> Pile, well/caisson, pier.</p><p><strong>Strap footing:</strong> બે footings ને rigid strap beam થી જોડવાથી eccentric load balance થાય, strap moment લે. Property line પાસે ઉપયોગ. English keywords: shallow foundation, deep foundation, strap footing, pile, raft.</p>"+fig(svg_terzaghi,"Strap footing sketch")},
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
    page=f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>DI03006051 · Winter 2025 solved paper</title><style>{CSS}</style></head><body><main class="page"><header class="hero"><div class="eyebrow">Solved question paper · English questions · Friendly Gujarati answers</div><div class="lang-switch" aria-label="Choose language"><button type="button" data-lang="en" aria-pressed="true">English</button><button type="button" data-lang="gu" aria-pressed="false">ગુજરાતી</button></div><h1>Soil Engineering</h1><div class="meta">GTU Diploma · Civil · Semester 3 · Winter 2025 · DI03006051 · 12-12-2025 · 70 marks · 10:30 AM TO 01:00 PM</div></header>{"".join(sections_html)}<div class="footer">Solved paper for study. Verify with standard spec before site use.</div></main><script>document.querySelectorAll('.lang-switch button').forEach(b=>b.addEventListener('click',()=>{{document.documentElement.lang=b.dataset.lang;document.querySelectorAll('.lang-switch button').forEach(x=>x.setAttribute('aria-pressed',x===b?'true':'false'));}}));</script></body></html>'''
    return page
def main():
    page=build_page()
    out_papers=ROOT/"papers-upload/papers/DI03006051/winter-2025.html"
    out_ws=ROOT/"preview/workshop/DI03006051_winter2025_bilingual.html"
    out_papers.parent.mkdir(parents=True,exist_ok=True)
    out_ws.parent.mkdir(parents=True,exist_ok=True)
    import re as _re
    page=_re.sub(r'<div class="gu">(.*?)</div>', lambda m: '<div class="gu">'+m.group(1).replace('(','[').replace(')',']')+'</div>', page, flags=_re.S)
    out_papers.write_text(page,encoding="utf-8")
    out_ws.write_text(page,encoding="utf-8")
    print(f"Bilingual: {out_papers} ({len(page)} chars)")
    print(f"details={page.count('<details')}, sections={page.count('<section')}, figs={page.count('<figure>')}")
    import re; gu=''.join(re.findall(r'<div class="gu">(.*?)</div>',page,re.S)); print(f"brackets gu={gu.count('(')+gu.count(')')}")
    print("PASS" if page.count('<details')==28 and page.count('<section')==5 else "FAIL")
    (ROOT/"drive-upload/DI03006051_winter_2025_bilingual.html").write_text(page,encoding="utf-8")
if __name__=="__main__": main()
