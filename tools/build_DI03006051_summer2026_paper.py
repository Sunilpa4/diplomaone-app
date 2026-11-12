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
 "title_en":"Q1 · Phase relations & index properties",
 "title_gu":"પ્ર.1 · ફેઝ સંબંધો અને ઇન્ડેક્સ ગુણધર્મ",
 "cards":[
  {"q_en":"Q.1 (a) Establish relation among Sr, w, G and e. (03 marks)","marks_en":"03 marks","marks_gu":"૦૩ ગુણ",
   "a_en":"<p><strong>Derivation from phase diagram:</strong> Consider volume of solids V<sub>s</sub>=1. Then void volume V<sub>v</sub>=e·V<sub>s</sub>=e, water volume V<sub>w</sub>=S<sub>r</sub>·V<sub>v</sub>=S<sub>r</sub>·e.</p><p>Weights: W<sub>s</sub>=G·γ<sub>w</sub>·V<sub>s</sub>=G·γ<sub>w</sub>, W<sub>w</sub>=γ<sub>w</sub>·V<sub>w</sub>=γ<sub>w</sub>·S<sub>r</sub>·e.</p><p>Water content w=W<sub>w</sub>/W<sub>s</sub>=S<sub>r</sub>·e/G ⇒ <strong>S<sub>r</sub>·e = w·G</strong>. For saturation S<sub>r</sub>=1 ⇒ e=w·G.</p>",
   "a_gu":"<p><strong>Relation:</strong> Phase diagram માં V_s=1 લો તો V_v=e, V_w=S_r·e, W_s=G·γw, W_w=γw·S_r·e ⇒ w=W_w/W_s=S_r·e/G ⇒ <strong>S_r·e=w·G</strong>. Saturated માટે e=w·G. English keywords: degree of saturation Sr, water content w, specific gravity G, void ratio e.</p>"},
  {"q_en":"Q.1 (b) Explain soil formation in geological cycle. (04 marks)","marks_en":"04 marks","marks_gu":"૦૪ ગુણ",
   "a_en":"<p>Rock → <strong>Weathering</strong> [physical disintegration, chemical decomposition, biological] → transported by <strong>water, wind, glacier, gravity</strong> → <strong>deposition</strong> [alluvial, aeolian, glacial, marine, residual if in-situ]. Factors: climate, parent rock, topography, time, organisms. Example residual laterite in-situ vs transported alluvial silt.</p>"+fig(svg_geocycle,"Geological cycle — weathering, transport, deposition, residual vs transported"),
   "a_gu":"<p>Rock → Weathering [physical, chemical, biological] → water/wind/glacier/gravity થી transport → deposition [alluvial, aeolian etc] અથવા residual. English keywords: weathering, transport, deposition, geological cycle.</p>"+fig(svg_geocycle,"Soil formation cycle")},
  {"q_en":"Q.1 (c) A soil sample has porosity 30% and G=2.6 Find void ratio, dry density saturated density and submerged density. (07 marks)","marks_en":"07 marks","marks_gu":"૦૭ ગુણ",
   "a_en":"<p><strong>Given:</strong> Porosity n=30%=0.30, G=2.6, γ<sub>w</sub>=1 g/cm³ =9.81 kN/m³.</p><p><strong>Concept:</strong> e=n/[1−n], γ<sub>d</sub>=G·γ<sub>w</sub>/[1+e], γ<sub>sat</sub>=[G+e]·γ<sub>w</sub>/[1+e], γ′=γ<sub>sat</sub>−γ<sub>w</sub>.</p><div class=\"eq\">e=n/[1−n] ,  γ<sub>d</sub>=G·γ<sub>w</sub>/[1+e] ,  γ<sub>sat</sub>=[G+e]·γ<sub>w</sub>/[1+e]</div><p><strong>Step 1 — Void ratio:</strong> e=0.30/0.70=0.4286.</p><p><strong>Step 2 — Dry density:</strong> γ<sub>d</sub>=2.6·1/1.4286=1.820 g/cm³ =17.85 kN/m³.</p><p><strong>Step 3 — Saturated density:</strong> γ<sub>sat</sub>=[2.6+0.4286]/1.4286=3.0286/1.4286=2.120 g/cm³ =20.80 kN/m³.</p><p><strong>Step 4 — Submerged:</strong> γ′=2.120−1=1.120 g/cm³ =10.99 kN/m³. Also γ′=[G−1]·γ<sub>w</sub>/[1+e]=1.6/1.4286=1.12 matches.</p><p><strong>Answer:</strong> <strong>e=0.43, γ<sub>d</sub>=1.82 g/cm³, γ<sub>sat</sub>=2.12 g/cm³, γ′=1.12 g/cm³</strong>. Draw two-phase solid-water diagram at saturation.</p>",
   "a_gu":"<p><strong>Given:</strong> n30% G2.6.</p><p><strong>Formulas:</strong> e=n/[1−n], γd=G·γw/[1+e], γsat=[G+e]γw/[1+e], γ′=γsat−γw.</p><p><strong>Steps:</strong> e0.4286, γd1.82, γsat2.12, γ′1.12 g/cm³. <strong>e0.43 γd1.82 γsat2.12 γ′1.12.</strong> English keywords: porosity n, void ratio e, dry density, saturated density, submerged density.</p>"},
  {"q_en":"Q.1 (c) OR A moist sample has volume 464 cc in natural state and weight 795 gm, dry weight 735 gm, G=2.65. Determine void ratio, porosity etc. (07 marks)","marks_en":"07 marks","marks_gu":"૦૭ ગુણ",
   "a_en":"<p><strong>Given:</strong> V=464 cm³, W=795 g, W<sub>d</sub>=735 g, G=2.65.</p><div class=\"eq\">γ=W/V , γ<sub>d</sub>=W<sub>d</sub>/V , w=[W−W<sub>d</sub>]/W<sub>d</sub> , e=G·γ<sub>w</sub>/γ<sub>d</sub>−1 , n=e/[1+e]</div><p><strong>Step 1 — Densities:</strong> γ=795/464=1.713 g/cm³, γ<sub>d</sub>=735/464=1.584 g/cm³, w=60/735=8.16%.</p><p><strong>Step 2 — Void ratio:</strong> e=2.65·1/1.584−1=0.673.</p><p><strong>Step 3 — Porosity:</strong> n=0.673/1.673=0.402=40.2%.</p><p><strong>Step 4 — Saturation:</strong> S<sub>r</sub>=w·G/e=0.0816·2.65/0.673=32.1%.</p><p><strong>Answer:</strong> <strong>γ=1.71, γ<sub>d</sub>=1.58 g/cm³, w=8.2%, e=0.673, n=40.2%, S<sub>r</sub>=32%</strong>. Step-wise substitution required for 7 marks.</p>",
   "a_gu":"<p><strong>Given:</strong> V464 cc W795 g Wd735 g G2.65.</p><p>γ=1.713 γd=1.584 w8.16% e=0.673 n40.2% Sr32.1% — steps બતાવો. English keywords: bulk density, dry density, water content, void ratio, porosity, degree of saturation.</p>"},
 ]
},
{
 "title_en":"Q2 · Plasticity, PSD & classification",
 "title_gu":"પ્ર.2 · પ્લાસ્ટિસિટી, PSD અને વ વર્ગીકરણ",
 "cards":[
  {"q_en":"Q.2 (a) Write assumptions for drawing phase diagram of soil. (03 marks)","marks_en":"03 marks","marks_gu":"૦૩ ગુણ",
   "a_en":"<p>1] Solids mass occupies single phase volume V<sub>s</sub>, 2] Air weight negligible, 3] Continuous voids, 4] Phases distinct, 5] In saturated case V<sub>a</sub>=0 two-phase, unsaturated three-phase. Allows V<sub>s</sub>=1 reference.</p>",
   "a_gu":"<p>1] Solids volume distinct, 2] Air weight zero, 3] Continuous voids, 4] Phases separate, 5] Saturated માં Va0 two-phase. English keywords: phase diagram, void, saturated.</p>"},
  {"q_en":"Q.2 (b) Draw I.S. Plasticity chart with all parameters. (04 marks)","marks_en":"04 marks","marks_gu":"૦૪ ગુણ",
   "a_en":"<p>X LL [0–100], Y PI [0–60], A-line PI=0.73[LL−20] divides clay above / silt below. U-line PI=0.9[LL−8] upper bound. Quadrants: CL, ML, CI, MI, CH, MH, OL, OH. LL 35/50 divides low/intermediate/high plasticity. Mark A-line, U-line, zones.</p>"+fig(svg_atterberg,"I.S. plasticity chart — A-line PI=0.73[LL−20], LL thresholds 35/50, zones CL/CH/ML/MH"),
   "a_gu":"<p>LL-X PI-Y, A-line PI=0.73[LL−20] clay ઉપર silt નીચે, LL35/50 low/intermediate/high. English keywords: plasticity chart, A-line, LL, PI, CL, CH.</p>"+fig(svg_atterberg,"Plasticity chart")},
  {"q_en":"Q.2 (c) Draw two phase and three phase diagram of soil. (07 marks)","marks_en":"07 marks","marks_gu":"૦૭ ગુણ",
   "a_en":"<p><strong>Two-phase:</strong> Saturated soil: solids V<sub>s</sub>, water V<sub>w</sub> with V<sub>v</sub>=V<sub>w</sub>, e=V<sub>w</sub>/V<sub>s</sub>, solids+water only. Dry soil: solids + air V<sub>a</sub>.</p><p><strong>Three-phase:</strong> Unsaturated: V<sub>a</sub>+V<sub>w</sub>=V<sub>v</sub>, W<sub>a</sub>≈0, W<sub>w</sub>, W<sub>s</sub>. Relations n=V<sub>v</sub>/V, e=V<sub>v</sub>/V<sub>s</sub>, S<sub>r</sub>=V<sub>w</sub>/V<sub>v</sub>.</p><p>Draw volumes left, weights right, label V<sub>a</sub>, V<sub>w</sub>, V<sub>s</sub>, W<sub>w</sub>, W<sub>s</sub>. Mark two-phase as special case S<sub>r</sub>=1 or 0.</p>"+fig(svg_2phase,"Two-phase [saturated] Vs+Vw vs three-phase Va+Vw+Vs with Wa~0"),
   "a_gu":"<p><strong>Two-phase:</strong> Saturated Vs+Vw, dry Vs+Va.</p><p><strong>Three-phase:</strong> Vs+Vw+Va. Volumes ડાબે weights જમણે. English keywords: two-phase, three-phase, void ratio, saturation.</p>"+fig(svg_2phase,"2-phase vs 3-phase")},
  {"q_en":"Q.2 (a) OR Explain Plastic limit test of soil in detail. (03 marks)","marks_en":"03 marks","marks_gu":"૦૩ ગુણ",
   "a_en":"<p>IS 2720: Roll 425 µ wetted soil into 3 mm thread on glass until crumbling. Water content at crumbling is PL. Repeat 3 times average. Apparatus glass plate, thread, oven. Gives brittle transition.</p>",
   "a_gu":"<p>ભીની માટીને 3 mm thread બનાવી crumbling થાય ત્યારે w = PL. English keywords: plastic limit, thread, crumbling.</p>"},
  {"q_en":"Q.2 (b) OR Draw the scale of soil classification as per Indian standard. (04 marks)","marks_en":"04 marks","marks_gu":"૦૪ ગુણ",
   "a_en":"<p>Size ranges: Boulder >300 mm, Cobble 80–300, Gravel 4.75–80, Sand 0.075–4.75 [coarse 2–4.75, medium 0.425–2, fine 0.075–0.425], Silt 0.002–0.075, Clay <0.002 mm. Show logarithmic scale 0.001–1000 mm with IS sieve sizes.</p>"+fig(svg_sieve,"IS particle size scale — boulder, gravel, sand, silt, clay 0.002–4.75 mm"),
   "a_gu":"<p>Boulder >300, Gravel 4.75–80, Sand 0.075–4.75, Silt 0.002–0.075, Clay <0.002 mm. English keywords: IS scale, sieve size, clay, silt.</p>"+fig(svg_sieve,"Particle size scale")},
  {"q_en":"Q.2 (c) OR Test on soil w=24% LL=49% PL=28% D60=0.06 D30=0.04 D10=0.008mm Calculate PI, Cu, Cc, Consistency Index & Liquidity Index. (07 marks)","marks_en":"07 marks","marks_gu":"૦૭ ગુણ",
   "a_en":"<div class=\"eq\">PI=LL−PL , C<sub>u</sub>=D<sub>60</sub>/D<sub>10</sub> , C<sub>c</sub>=D<sub>30</sub>²/[D<sub>60</sub>·D<sub>10</sub>] , LI=[w−PL]/PI , CI=[LL−w]/PI</div><p><strong>Step 1 — PI:</strong> 49−28=21%.</p><p><strong>Step 2 — Cu:</strong> 0.06/0.008=7.5.</p><p><strong>Step 3 — Cc:</strong> 0.04²/[0.06·0.008]=0.0016/0.00048=3.33.</p><p><strong>Step 4 — LI:</strong> [24−28]/21=−0.19 indicates semi-solid, overconsolidated.</p><p><strong>Step 5 — CI [Consistency Index]:</strong> [49−24]/21=1.19. Note LI+CI=1. Remark: Cc>3 suggests gap-graded despite high Cu — check well-graded needs 1<Cc<3.</p><p><strong>Answer:</strong> <strong>PI=21%, Cu=7.5, Cc=3.33, LI=−0.19, CI=1.19</strong>. Mention A-line check PI 21 vs 0.73[29]=21.2 borderline clay-silt.</p>",
   "a_gu":"<p>PI21% Cu7.5 Cc3.33 LI−0.19 CI1.19. Steps: PI LL−PL, Cu D60/D10, Cc D30²/D60·D10, LI w−PL/PI, CI LL−w/PI. English keywords: plasticity index, uniformity, curvature, liquidity, consistency.</p>"},
 ]
},
{
 "title_en":"Q3 · Shear strength & compaction",
 "title_gu":"પ્ર.3 · શીયર સ્ટ્રેન્થ અને કોમ્પેક્શન",
 "cards":[
  {"q_en":"Q.3 (a) Define cohesion and angle of internal friction with notations. (03 marks)","marks_en":"03 marks","marks_gu":"૦૩ ગુણ",
   "a_en":"<p><strong>Cohesion c [kPa]:</strong> Shear intercept at σ=0 due to bonding, symbol c.</p><p><strong>Angle internal friction φ [°]:</strong> Slope angle of Mohr-Coulomb line, tanφ gradient, φ from triaxial/box test. Notation φ, sometimes ϕ.</p>",
   "a_gu":"<p><strong>Cohesion c:</strong> σ0 પર shear intercept kPa.</p><p><strong>Angle φ:</strong> Mohr-Coulomb નો ઢાળ tanφ. Symbols c, φ. English keywords: cohesion, friction angle.</p>"},
  {"q_en":"Q.3 (b) Enlist objectives of Site Exploration. (04 marks)","marks_en":"04 marks","marks_gu":"૦૪ ગુણ",
   "a_en":"<p>1] Strata profile, 2] Water table, 3] Properties bearing capacity, 4] Foundation choice, 5] Ground improvement need, 6] Material availability. Methods borings, pits, geophysics.</p>"+fig(svg_borelog,"Site exploration — bore log, water table, strata, sampling"),
   "a_gu":"<p>1] Strata, 2] Water table, 3] Bearing, 4] Foundation, 5] Improvement. English keywords: site exploration, bore log.</p>"+fig(svg_borelog,"Site exploration")},
  {"q_en":"Q.3 (c) A clayed soil w=45% LL=52% PL=27% Calculate PI, LI, CI. (07 marks)","marks_en":"07 marks","marks_gu":"૦૭ ગુણ",
   "a_en":"<div class=\"eq\">PI=LL−PL , LI=[w−PL]/PI , CI=[LL−w]/PI</div><p><strong>Step 1 — PI:</strong> 52−27=25%.</p><p><strong>Step 2 — LI:</strong> [45−27]/25=18/25=0.72 — plastic state, near liquid.</p><p><strong>Step 3 — CI:</strong> [52−45]/25=7/25=0.28 — soft consistency. Check LI+CI=1.</p><p><strong>Step 4 — Classification:</strong> LL52 high plasticity, PI25 above A-line 0.73[32]=23.4 → CH clay. Consistency soft.</p><p><strong>Answer:</strong> <strong>PI=25%, LI=0.72, CI=0.28</strong>, high plasticity clay, plastic state.</p>",
   "a_gu":"<p>PI25% LI0.72 CI0.28. Steps PI LL−PL, LI w−PL/PI, CI LL−w/PI. A-line 23.4 હોવાથી CH clay. English keywords: PI, LI, CI, plasticity, A-line, CH.</p>"},
  {"q_en":"Q.3 (a) OR Explain: C-soil, ϕ-soil and C-ϕ soil. (03 marks)","marks_en":"03 marks","marks_gu":"૦૩ ગુણ",
   "a_en":"<p><strong>C-soil:</strong> Pure cohesive clay φ≈0 τ<sub>f</sub>=c.</p><p><strong>ϕ-soil:</strong> Cohesionless sand c≈0 τ<sub>f</sub>=σ·tanφ.</p><p><strong>C-ϕ soil:</strong> Mixed silt/clayey sand τ<sub>f</sub>=c+σ·tanφ.</p>"+fig(svg_law,"C, phi, C-phi soils — τ=c, τ=σ·tanφ, τ=c+σ·tanφ"),
   "a_gu":"<p>C-soil clay φ0 τc, ϕ-soil sand c0 τσ·tanφ, C-ϕ mixed τc+σ·tanφ. English keywords: cohesion, friction, C-phi.</p>"+fig(svg_law,"Soil types")},
  {"q_en":"Q.3 (b) OR Explain Coulomb’s law for shear strength. (04 marks)","marks_en":"04 marks","marks_gu":"૦૪ ગુણ",
   "a_en":"<p>Coulomb [1776]: Shear strength τ<sub>f</sub>=c+σ·tanφ. Graphical Mohr-Coulomb line intercept c, slope φ. For total stress use c<sub>u</sub>, φ<sub>u</sub> / effective c′, φ′. Test via triaxial.</p>"+fig(svg_mohr,"Mohr-Coulomb — τ=c+σ·tanφ, Mohr circles, c intercept, φ slope"),
   "a_gu":"<p>Coulomb τf=c+σ·tanφ, intercept c slope φ, total/effective c′, φ′. English keywords: shear strength, Mohr-Coulomb.</p>"+fig(svg_mohr,"Coulomb law")},
  {"q_en":"Q.3 (c) OR Explain Standard Proctor test in detail. (07 marks)","marks_en":"07 marks","marks_gu":"૦૭ ગુણ",
   "a_en":"<p><strong>Aim IS 2720 Part 7:</strong> OMC/MDD for given energy 592 kJ/m³.</p><p><strong>Apparatus:</strong> 1000 cc mould, 2.6 kg rammer 310 mm drop, 20 mm sieve.</p><p><strong>Step 1 — Mix:</strong> 3 kg soil 6% water temper 16 h.</p><p><strong>Step 2 — Compact:</strong> 3 layers ×25 blows, trim, weigh W₂.</p><p><strong>Step 3 — γ<sub>d</sub>:</strong> γ=W/V, w from oven, γ<sub>d</sub>=γ/[1+w].</p><p><strong>Step 4 — Repeat:</strong> +2% water 5–6 times till γ<sub>d</sub> falls.</p><p><strong>Step 5 — Curve:</strong> γ<sub>d</sub> vs w peak = MDD/OMC, zero-air line G·γ<sub>w</sub>/[1+wG]. Modified uses 2700 kJ/m³ gives higher MDD.</p>"+fig(svg_proctor,"Standard Proctor — 3 layers 25 blows, γd vs w OMC/MDD"),
   "a_gu":"<p><strong>Standard Proctor:</strong> OMC/MDD. 1000 cc mould 2.6 kg rammer 3×25 blows, γd=γ/[1+w], curve peak MDD/OMC. English keywords: OMC, MDD, Proctor, compactive effort.</p>"+fig(svg_proctor,"Proctor")},
 ]
},
{
 "title_en":"Q4 · Permeability, compaction & stabilization",
 "title_gu":"પ્ર.4 · પારગમ્યતા, કોમ્પેક્શન અને સ્ટેબિલાઇઝેશન",
 "cards":[
  {"q_en":"Q.4 (a) Enlist importance of Permeability in Civil Engineering. (03 marks)","marks_en":"03 marks","marks_gu":"૦૩ ગુણ",
   "a_en":"<p>Seepage under dams, dewatering excavations, drainage filter design, consolidation settlement rate, well yield, slope stability pore pressure, grout design. Low k core, high k drain.</p>",
   "a_gu":"<p>Seepage, dewatering, drainage, consolidation, well, slope — permeability મહત્વ. English keywords: permeability, seepage, drainage.</p>"},
  {"q_en":"Q.4 (b) Explain Compaction Curve. Also Explain O.M.C. & M.D.D. (04 marks)","marks_en":"04 marks","marks_gu":"૦૪ ગુણ",
   "a_en":"<p>Plot γ<sub>d</sub> vs w is parabolic, rises to peak then falls. <strong>OMC:</strong> w at peak max density. <strong>MDD:</strong> peak γ<sub>d</sub> value. Left dry of optimum: flocculated, high voids, higher k. Right wet: dispersed, high pore pressure. Zero-air voids line theoretical max never crossed.</p>"+fig(svg_curve,"Compaction curve — γd vs w, OMC at peak, MDD, zero-air voids line"),
   "a_gu":"<p>γd vs w curve peak પર OMC [water] અને MDD [dry density]. Dry બાજુ flocculated wet બાજુ dispersed. English keywords: compaction curve, OMC, MDD, dry density.</p>"+fig(svg_curve,"Compaction curve OMC/MDD")},
  {"q_en":"Q.4 (c) Explain Light Compaction Test carried out in laboratory. (07 marks)","marks_en":"07 marks","marks_gu":"૦૭ ગુણ",
   "a_en":"<p><strong>Light Compaction [Standard Proctor, IS 2720 Part 7 low energy]:</strong> Energy 592 kJ/m³ simulating light rollers.</p><p><strong>Apparatus:</strong> 1000 cc mould, 2.6 kg rammer 310 mm, collar, base.</p><p><strong>Step 1 — Prep:</strong> Air-dry 20 mm passing 3 kg, add water 8% initial, temper.</p><p><strong>Step 2 — Fill:</strong> 3 equal layers, each 25 blows distributed, scarify between layers.</p><p><strong>Step 3 — Measure:</strong> Remove collar trim, weigh, extract sample for w, compute γ= W/V, γ<sub>d</sub>=γ/[1+w].</p><p><strong>Step 4 — Series:</strong> Repeat at w+2% until γ<sub>d</sub> drops past optimum [5–6 points].</p><p><strong>Step 5 — Plot:</strong> γ<sub>d</sub> vs w, peak is MDD/OMC, draw zero-air voids G=2.65 for check.</p><p><strong>Result:</strong> Report OMC to 0.5%, MDD to 0.01 g/cm³. Light vs Heavy [4.5 kg 450 mm 5 layers] energy contrast.</p>"+fig(svg_proctor,"Light compaction — mould, rammer, 3 layers, γd vs w OMC/MDD, energy 592 kJ/m³"),
   "a_gu":"<p><strong>Light compaction:</strong> Standard Proctor 592 kJ/m³ light rollers માટે.</p><p>1000 cc mould 2.6 kg rammer 3×25 blows, γ= W/V γd=γ/[1+w], 5–6 points plot peak MDD/OMC. English keywords: light compaction, OMC, MDD, mould, rammer, dry density.</p>"+fig(svg_proctor,"Light compaction lab")},
  {"q_en":"Q.4 (a) OR Enlist factors affecting permeability and explain any one in detail. (03 marks)","marks_en":"03 marks","marks_gu":"૦૩ ગુણ",
   "a_en":"<p>Factors: grain size, void ratio, composition, fabric, stratification, saturation, viscosity/temperature.</p><p><strong>Detail — Void ratio:</strong> k ∝ e³/[1+e] [Kozeny-Carman], compaction reduces e→k drops 10× per 0.1 e. Flocculated has larger pores higher k than dispersed at same e.</p>",
   "a_gu":"<p>Factors: grain size, void ratio, composition etc. Void ratio માં k ∝ e³/[1+e] flocculated vs dispersed. English keywords: permeability, void ratio, Kozeny-Carman.</p>"},
  {"q_en":"Q.4 (b) OR Explain Mechanical soil stabilization and Chemical soil stabilization. (04 marks)","marks_en":"04 marks","marks_gu":"૦૪ ગુણ",
   "a_en":"<p><strong>Mechanical:</strong> Blending soils/gravel, compaction control, geotextile reinforcement — no chemical, improves gradation/density.</p><p><strong>Chemical:</strong> Add lime [CaO reduces plasticity], cement [C-S-H bonds], bitumen [waterproof], fly ash/polymers — pozzolanic reactions increase strength and reduce swell.</p>",
   "a_gu":"<p><strong>Mechanical:</strong> blending, compaction, geotextile.</p><p><strong>Chemical:</strong> lime, cement, bitumen — pozzolanic reaction strength વધે. English keywords: stabilization, lime, cement, geotextile.</p>"},
  {"q_en":"Q.4 (c) OR Explain Constant Head Permeability Test with diagram in detail. (07 marks)","marks_en":"07 marks","marks_gu":"૦૭ ગુણ",
   "a_en":"<p><strong>Aim:</strong> For coarse soils k>10⁻⁵ m/s, head constant via overflow.</p><p><strong>Apparatus:</strong> Permeameter D10 cm L10 cm, constant head tank, manometers, measuring cylinder, water supply.</p><p><strong>Step 1 — Sample:</strong> Compact saturated sample in permeameter, saturate under vacuum, connect to head tank.</p><p><strong>Step 2 — Flow:</strong> Maintain h constant, collect discharge Q in time t, measure head difference h over length L.</p><p><strong>Step 3 — Formula Darcy:</strong> q=k·i·A, i=h/L, Q=q·t ⇒ k= Q·L/[A·h·t].</p><p><strong>Step 4 — Corrections:</strong> Temperature to 27°C k<sub>27</sub>=k<sub>T</sub>·µ<sub>T</sub>/µ<sub>27</sub>, multiple trials average.</p><p><strong>Example:</strong> If Q=100 cm³ t=60 s L=10 cm A=78.5 cm² h=20 cm ⇒ k=100·10/[78.5·20·60]=0.0106 cm/s.</p>"+fig(svg_darcy,"Constant head — tank, permeameter, Q·L/A·h·t, coarse soil"),
   "a_gu":"<p><strong>Constant head:</strong> coarse soil માટે head constant રાખી Q મેળવો.</p><p>k= Q·L/[A·h·t], i=h/L, Q collection, temperature correction. English keywords: constant head, Darcy, permeability, hydraulic gradient.</p>"+fig(svg_darcy,"Constant head test")},
 ]
},
{
 "title_en":"Q5 · Shear tests, bearing & foundations",
 "title_gu":"પ્ર.5 · શીયર ટેસ્ટ, બેરિંગ અને પાયા",
 "cards":[
  {"q_en":"Q.5 (a) Explain Merits and Limitations of Box shear Test. (03 marks)","marks_en":"03 marks","marks_gu":"૦૩ ગુણ",
   "a_en":"<p><strong>Merits:</strong> Simple, cheap, direct c/φ, drained/undrained, suitable coarse soils.</p><p><strong>Limitations:</strong> Forced failure plane not weakest, non-uniform stress, no pore pressure control, limited drainage, area correction needed.</p>"+fig(svg_box,"Box shear — split box, forced plane, c/φ, limitations"),
   "a_gu":"<p><strong>Merits:</strong> simple cheap direct c/φ coarse માટે.</p><p><strong>Limitations:</strong> forced plane, non-uniform, no pore pressure. English keywords: box shear, direct shear, c, φ.</p>"+fig(svg_box,"Box shear merits/limits")},
  {"q_en":"Q.5 (b) State the parameters that are used for determining the bearing capacity of soil. (04 marks)","marks_en":"04 marks","marks_gu":"૦૪ ગુણ",
   "a_en":"<p>1] Shear strength c, φ, 2] Unit weight γ, 3] Foundation depth D<sub>f</sub> width B, 4] Water table, 5] Compressibility, 6] SPT N-value. Terzaghi q<sub>u</sub>=cN<sub>c</sub>+γD<sub>f</sub>N<sub>q</sub>+0.5γBN<sub>γ</sub>.</p>",
   "a_gu":"<p>1] c, φ, 2] γ, 3] Df, B, 4] Water table, 5] N-value. Terzaghi formula. English keywords: bearing capacity, c, φ, N-values.</p>"},
  {"q_en":"Q.5 (c) Explain Liquefaction, its causes, effect and state remedies for Liquefaction. (07 marks)","marks_en":"07 marks","marks_gu":"૦૭ ગુણ",
   "a_en":"<p><strong>Definition:</strong> Saturated loose sand loses strength due to earthquake/cyclic loading, excess pore pressure u→σ′→0 behaves like liquid.</p><p><strong>Causes:</strong> Loose saturated sand D<sub>r</sub><50%, M≥6 earthquake, high water table, uniform sand low fines.</p><p><strong>Effects:</strong> Bearing failure, settlement, lateral spreading, sand boils, tilting structures.</p><p><strong>Remedies:</strong> 1] Densification vibro-compaction/stone columns, 2] Lower water table dewatering, 3] Grouting, 4] Deep piles to hard stratum, 5] Avoid liquefiable layer, 6] Soil replacement, 7] Drainage wells to dissipate u.</p><p><strong>Assessment:</strong> SPT N<sub>1</sub>60>22 safe, factor safety against liquefaction =CRR/CSR.</p>"+fig(svg_quick,"Liquefaction — pore pressure rise, sand boils, densification, stone columns, dewatering"),
   "a_gu":"<p><strong>Liquefaction:</strong> saturated loose sand cyclic load થી strength ઘટે pore pressure વધે.</p><p><strong>Causes:</strong> loose sand, earthquake, high water table.</p><p><strong>Effects:</strong> bearing failure, settlement, lateral spread.</p><p><strong>Remedies:</strong> densification, stone columns, dewatering, grouting, piles. English keywords: liquefaction, pore pressure, densification, stone columns, SPT.</p>"+fig(svg_quick,"Liquefaction remedies")},
  {"q_en":"Q.5 (a) OR State only names of different types of Bearing Capacities. (03 marks)","marks_en":"03 marks","marks_gu":"૦૩ ગુણ",
   "a_en":"<p>Ultimate q<sub>u</sub>, Net ultimate q<sub>nu</sub>, Net safe q<sub>ns</sub>=q<sub>nu</sub>/FOS, Safe gross, Allowable q<sub>a</sub> [safe + settlement].</p>",
   "a_gu":"<p>Ultimate, Net ultimate, Net safe, Safe gross, Allowable. English keywords: bearing capacity, allowable, safe.</p>"},
  {"q_en":"Q.5 (b) OR Differentiate between general shear failure and local shear failure. (04 marks)","marks_en":"04 marks","marks_gu":"૦૪ ગુણ",
   "a_en":"<table><tr><th>General</th><th>Local</th></tr><tr><td>Well-defined slip to surface, peak load</td><td>Partial slip, no peak, large settlement</td></tr><tr><td>Dense sand/stiff clay</td><td>Loose/soft</td></tr><tr><td>c′=c φ′=φ Terzaghi</td><td>c′=2/3c φ reduced N factors lower</td></tr><tr><td>Heave visible</td><td>Heave minimal punching</td></tr></table>"+fig(svg_failures,"General vs local shear — slip surface, dense vs loose, Terzaghi factors"),
   "a_gu":"<table><tr><th>General</th><th>Local</th></tr><tr><td>clear slip surface peak</td><td>partial no peak large settlement</td></tr><tr><td>dense</td><td>loose</td></tr></table><p>English keywords: general shear, local shear, bearing, Terzaghi.</p>"+fig(svg_failures,"Shear failure types")},
  {"q_en":"Q.5 (c) OR Explain the types of foundation and describe in detail. (07 marks)","marks_en":"07 marks","marks_gu":"૦૭ ગુણ",
   "a_en":"<p><strong>Shallow D<sub>f</sub>/B≤1:</strong> Isolated pad, combined rectangular/trapezoidal, strap [two pads + beam], mat/raft for low bearing or large load.</p><p><strong>Deep:</strong> Pile [driven/bored, end bearing/friction], well/caisson sunk to rock, pier.</p><p><strong>Selection:</strong> Load, soil bearing, water table, settlement, site constraints. Detail strap footing: two isolated footings connected by beam to balance eccentric outer column, beam rigid no soil pressure, transfers moment allowing economical design.</p><p><strong>Uses:</strong> Shallow on good surface soil, deep when weak up to depth. IS 1904/2911 guidelines.</p>"+fig(svg_terzaghi,"Foundations — shallow isolated/combined/strap/mat vs deep pile/well, strap beam"),
   "a_gu":"<p><strong>Shallow:</strong> isolated, combined, strap, mat/raft.</p><p><strong>Deep:</strong> pile, well/caisson.</p><p>Strap footing બે footings beam થી જોડી eccentric balance કરે. English keywords: shallow, deep, isolated, strap, mat, pile, well.</p>"+fig(svg_terzaghi,"Foundation types")},
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
    page=f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>DI03006051 · Summer 2026 solved paper</title><style>{CSS}</style></head><body><main class="page"><header class="hero"><div class="eyebrow">Solved question paper · English questions · Friendly Gujarati answers</div><div class="lang-switch" aria-label="Choose language"><button type="button" data-lang="en" aria-pressed="true">English</button><button type="button" data-lang="gu" aria-pressed="false">ગુજરાતી</button></div><h1>Soil Engineering</h1><div class="meta">GTU Diploma · Civil · Semester 3 · Summer 2026 · DI03006051 · 22-05-2026 · 70 marks · 02:30 PM TO 05:00 PM</div></header>{"".join(sections_html)}<div class="footer">Solved paper for study. Verify with standard spec before site use.</div></main><script>document.querySelectorAll('.lang-switch button').forEach(b=>b.addEventListener('click',()=>{{document.documentElement.lang=b.dataset.lang;document.querySelectorAll('.lang-switch button').forEach(x=>x.setAttribute('aria-pressed',x===b?'true':'false'));}}));</script></body></html>'''
    return page
def main():
    page=build_page()
    out_papers=ROOT/"papers-upload/papers/DI03006051/summer-2026.html"
    out_ws=ROOT/"preview/workshop/DI03006051_summer2026_bilingual.html"
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
    (ROOT/"drive-upload/DI03006051_summer_2026_bilingual.html").write_text(page,encoding="utf-8")
if __name__=="__main__": main()
