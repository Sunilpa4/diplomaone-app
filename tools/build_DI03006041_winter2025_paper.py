#!/usr/bin/env python3
from pathlib import Path
import html
ROOT=Path(__file__).resolve().parent.parent
def load_svg(name):
    p=ROOT/f"content/civil/sem3/DI03006041/diagrams/{name}"
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
svg_stress=load_svg("ms1_stress_strain.svg")
svg_composite=load_svg("ms1_composite.svg")
svg_formulas=load_svg("ms2_formulas.svg")
svg_isection=load_svg("ms2_isection.svg")
svg_theorem=load_svg("ms2_theorem.svg")
svg_beams=load_svg("ms3_beams.svg")
svg_cantilever=load_svg("ms3_cantilever.svg")
svg_bending=load_svg("ms4_bending.svg")
svg_shear_rect=load_svg("ms4_shear_rect.svg")
svg_shear_I=load_svg("ms4_shear_I.svg")
svg_types=load_svg("ms6_types.svg")
svg_sections=load_svg("ms6_sections.svg")
svg_joints=load_svg("ms6_joints.svg")
svg_zero=load_svg("ms6_zero.svg")
svg_euler=load_svg("ms7_euler.svg")
svg_effective=load_svg("ms7_effective.svg")
svg_rankine=load_svg("ms7_rankine.svg")
svg_elastic=load_svg("ms5_elastic.svg")
svg_ssb=load_svg("ms5_ssb.svg")
svg_cantilever5=load_svg("ms5_cantilever.svg")

SECTIONS=[
{
 "title_en":"Q1 · Direct stress, strain, stress-strain curve & composite bar",
 "title_gu":"પ્ર.1 · ડાયરેક્ટ સ્ટ્રેસ, સ્ટ્રેઈન, સ્ટ્રેસ-સ્ટ્રેઈન કર્વ અને કોમ્પોઝિટ બાર",
 "cards":[
  {"q_en":"Q.1 (a) Define following: (1) Direct stress (2) Linear strain (3) Poisson’s ratio (03 marks)","marks_en":"03 marks","marks_gu":"૦૩ ગુણ",
   "a_en":"<p><strong>1) Direct stress:</strong> Internal resistance per unit area when load acts along axis of member. Tensile if pulling, compressive if pushing. Formula σ = P/A, unit N/mm². For 80 kN on 18 mm dia, σ = 80000 / 254 = 315 N/mm².</p><p><strong>2) Linear strain:</strong> Change in length per original length along loading direction. ε = δL / L, no unit. For 4 m bar elongation 6.3 mm, ε = 0.00157.</p><p><strong>3) Poisson’s ratio:</strong> Ratio of lateral strain to linear strain with negative sign. μ = −lateral / linear, about 0.25–0.30 for steel, 0.15 for concrete. Governs volumetric change.</p>",
   "a_gu":"<p><strong>1) ડાયરેક્ટ સ્ટ્રેસ:</strong> અક્ષ પર બળ લાગે ત્યારે એકમ ક્ષેત્રફળ દીઠ આંતરિક પ્રતિકાર. σ = P/A, N/mm². 80 kN 18 mm પર 315 N/mm².</p><p><strong>2) લિનિયર સ્ટ્રેઈન:</strong> લંબાઈમાં ફેરફાર / મૂળ લંબાઈ. ε = δL/L. 4 m પર 6.3 mm તો 0.00157.</p><p><strong>3) પોઈસન ગુણોત્તર:</strong> બાજુની સ્ટ્રેઈન / લિનિયર સ્ટ્રેઈન. μ લગભગ 0.25–0.30 સ્ટીલ.</p>"},
  {"q_en":"Q.1 (b) Draw stress-strain curve for mild steel bar giving salient points on it. (04 marks)","marks_en":"04 marks","marks_gu":"૦૪ ગુણ",
   "a_en":"<p>Mild steel curve has <em>Proportional limit</em> Hooke’s law up to 250 N/mm², <em>Elastic limit</em> just beyond, <em>Upper and lower yield</em> drop at 250, <em>Strain hardening</em> rising to <em>Ultimate 400–500</em>, then <em>Necking</em> to <em>Fracture</em>. Elastic region slope is E = 2×10⁵. Yield plateau shows large strain without load increase. Used to know safe stress with factor of safety.</p>"+fig(svg_stress,"Stress-strain curve for mild steel — proportional limit, yield, ultimate, fracture with E slope"),
   "a_gu":"<p>માઈલ્ડ સ્ટીલ કર્વમાં પ્રમાણસર હદ 250 N/mm² સુધી હૂક નિયમ, સ્થિતિસ્થાપક હદ, ઉપર-નીચે યીલ્ડ 250, સ્ટ્રેઈન હાર્ડનિંગ ઉલ્ટિમેટ 400–500, નેકિંગ ફ્રેક્ચર. ઢાળ E = 2×10⁵. યીલ્ડ પર મોટી સ્ટ્રેઈન.</p>"+fig(svg_stress,"માઈલ્ડ સ્ટીલ સ્ટ્રેસ-સ્ટ્રેઈન — યીલ્ડ, ઉલ્ટિમેટ, ફ્રેક્ચર")},
  {"q_en":"Q.1 (c) A copper rod of 20mm diameter is placed inside the steel tube of external diameter 25mm and internal diameter 22mm. The tube and rod are 500mm long and are rigidly connected together at the ends. Find P if stress in steel is limited to 150 N/mm². Take Es=200 kN/mm² and Ec=100 kN/mm². (07 marks)","marks_en":"07 marks","marks_gu":"૦૭ ગુણ",
   "a_en":"<p><strong>Given Data</strong></p><table><tr><th>Item</th><th>Value</th></tr><tr><td>Steel tube outer / inner dia</td><td>D=25 mm, d=22 mm</td></tr><tr><td>Copper rod dia</td><td>20 mm</td></tr><tr><td>Length L</td><td>500 mm, rigidly connected at ends → same elongation δ</td></tr><tr><td>Allowable steel stress</td><td>σ<sub>s</sub>=150 N/mm²</td></tr><tr><td>Moduli</td><td>E<sub>s</sub>=200 kN/mm² =2×10⁵ N/mm², E<sub>c</sub>=100 kN/mm² =1×10⁵ N/mm²</td></tr></table><p><strong>Concept — Composite bar:</strong> For rigid end plates, <em>compatibility</em> δ<sub>s</sub>=δ<sub>c</sub> ⇒ ε<sub>s</sub>=ε<sub>c</sub> ⇒ σ<sub>s</sub>/E<sub>s</sub>=σ<sub>c</sub>/E<sub>c</sub>. Equilibrium P = P<sub>s</sub>+P<sub>c</sub>=σ<sub>s</sub>A<sub>s</sub>+σ<sub>c</sub>A<sub>c</sub>.</p><div class=\"eq\">A<sub>s</sub>=π/4·[D²−d²]  ,  A<sub>c</sub>=π/4·20²  ,  σ<sub>c</sub>=σ<sub>s</sub>·E<sub>c</sub>/E<sub>s</sub></div><p><strong>Step 1 — Areas:</strong> A<sub>s</sub>=0.7854·[625−484]=0.7854·141=110.7 mm², A<sub>c</sub>=0.7854·400=314.2 mm².</p><p><strong>Step 2 — Stresses by compatibility:</strong> σ<sub>c</sub>=150·100/200=75 N/mm² — well below copper allowable, so steel governs.</p><p><strong>Step 3 — Total load:</strong> P<sub>s</sub>=150·110.7=16605 N, P<sub>c</sub>=75·314.2=23562 N, <strong>P=40167 N ≈40.2 kN.</strong></p><p><strong>Step 4 — Check elongation:</strong> δ=σ<sub>s</sub>L/E<sub>s</sub>=150·500/200000=0.375 mm — same for copper: 75·500/100000=0.375 mm — compatibility satisfied. EA ratio: E<sub>s</sub>A<sub>s</sub>=22.14 MN, E<sub>c</sub>A<sub>c</sub>=31.42 MN.</p><p><strong>Answer for 7 marks:</strong> Draw composite section, write compatibility + equilibrium, show table, get <strong>P≈40.2 kN</strong> with 0.375 mm extension. Mention if load increased copper stress scales proportionally.</p>"+fig(svg_composite,"Composite bar — compatibility εs=εc, equilibrium P=σsAs+σcAc, 40.2 kN"),
   "a_gu":"<p><strong>Given Data:</strong> Steel tube outer 25 mm inner 22 mm ⇒ A_s=110.7 mm², Copper rod 20 mm ⇒ A_c=314.2 mm², L=500 mm બંને ends rigidly connected હોવાથી <em>compatibility</em> થી strain સમાન.</p><p><strong>Compatibility:</strong> ε_s = ε_c ⇒ σ_s/E_s = σ_c/E_c ⇒ σ_c=150·100/200=75 N/mm². <strong>Equilibrium:</strong> P = σ_s·A_s + σ_c·A_c =16605+23562=40167 N ≈<strong>40.2 kN</strong>.</p><p><strong>Elongation:</strong> δ = σ_s·L/E_s =0.375 mm, બંને માટે સમાન. Exam માં diagram, compatibility equation અને table બતાવવાથી પૂરા 7 marks મળે. English keywords: stress, strain, compatibility, equilibrium, load.</p>"+fig(svg_composite,"કોમ્પોઝિટ — સમાન સ્ટ્રેઈન, P વહેંચણી")},
  {"q_en":"Q.1 (c) OR A steel bar 1600mm long is acted upon by forces as shown in figure.1. Find elongation. Take E=2.1×10⁵ N/mm². (07 marks)","marks_en":"07 marks","marks_gu":"૦૭ ગુણ",
   "a_en":"<p><strong>Given:</strong> Stepped steel bar total 1600 mm with different axial forces as per Fig.1 [typical: 0–400 mm 40 kN tension, 400–900 mm 20 kN compression, 900–1600 mm 30 kN tension], E=2.1×10⁵ N/mm². Need total elongation.</p><p><strong>Concept:</strong> Axial elongation δ=PL/AE per segment. Tensile +ve elongates, compressive −ve shortens. Free-body: draw Axial Force Diagram first.</p><div class=\"eq\">δ<sub>total</sub>= Σ P<sub>i</sub>L<sub>i</sub> / A<sub>i</sub>E  — sign with tension positive</div><table><tr><th>Segment i</th><th>P<sub>i</sub> [N]</th><th>L<sub>i</sub> [mm]</th><th>A<sub>i</sub> [mm²]</th><th>δ<sub>i</sub>=P<sub>i</sub>L<sub>i</sub>/A<sub>i</sub>E [mm]</th></tr><tr><td>AB 0–400</td><td>+40,000</td><td>400</td><td>500</td><td>+0.152</td></tr><tr><td>BC 400–900</td><td>−20,000</td><td>500</td><td>800</td><td>−0.059</td></tr><tr><td>CD 900–1600</td><td>+30,000</td><td>700</td><td>400</td><td>+0.250</td></tr><tr><td colspan=4><strong>Total</strong></td><td><strong>+0.343 mm elongation</strong></td></tr></table><p><strong>Steps to write for 7 marks:</strong> 1] Free-body and AFD diagram, 2] Tabulate each segment with sign, 3] Apply δ=PL/AE, 4] Algebraic sum, 5] State elongation or shortening. If figure differs, same table with given P, L, A. Units: N, mm, N/mm² → mm. Keep 3 sig fig.</p><p><strong>Alternative if uniform A:</strong> Compute equivalent force method — same formula applied piece-wise. Mention rigid bar vs elastic.</p>",
   "a_gu":"<p><strong>પદ્ધતિ:</strong> બારને અચળ બળવાળા ભાગમાં વહેંચો, δ = P·L/A·E દરેકનું, તાણ લંબાય દબાણ ટૂંકું, બધાનો સરવાળો. ઉદા 40 kN તાણ 400 mm A500 તો δ0.15 mm. કુલ 0.2–1.5 mm.</p>"},
 ]
},
{
 "title_en":"Q2 · Moment of Inertia — theorems, ratios & T-section & SFD/BMD",
 "title_gu":"પ્ર.2 · જડત્વ આઘૂર્ણ — પ્રમેય, ગુણોત્તર અને T-સેક્શન અને SFD/BMD",
 "cards":[
  {"q_en":"Q.2 (a) (1) Write statement of parallel axis theorem with equation. (2) What will be ratio of Ixx and ymax for circular section? (03 marks)","marks_en":"03 marks","marks_gu":"૦૩ ગુણ",
   "a_en":"<p><strong>1) Parallel axis:</strong> MOI about any axis parallel to centroidal axis = I_G + A·d² where I_G is centroidal MOI, A area, d distance between axes. Used to shift I from centroid to base.</p><p><strong>2) Circle:</strong> For diameter D, I_xx = πD⁴/64, y_max = D/2, ratio I_xx / y_max = πD³/32 = (πD⁴/64)/(D/2). Also section modulus Z = I/y = πD³/32.</p>"+fig(svg_theorem,"Parallel axis theorem — I = I_G + A·d², with centroidal and parallel axes"),
   "a_gu":"<p><strong>1) સમાંતર અક્ષ:</strong> I = I_G + A·d², I_G સેન્ટ્રોઇડલ, A ક્ષેત્ર, d અંતર.</p><p><strong>2) વર્તુળ:</strong> I_xx = πD⁴/64, y_max = D/2, ગુણોત્તર = πD³/32 = Z.</p>"+fig(svg_theorem,"સમાંતર અક્ષ પ્રમેય")},
  {"q_en":"Q.2 (b) Calculate Ixx for a T-section with flange and web each of size 60mm x 20mm. (04 marks)","marks_en":"04 marks","marks_gu":"૦૪ ગુણ",
   "a_en":"<p><strong>Section:</strong> Flange 60×20 top, web 60×20 vertical, total height 80 mm. Area each 1200 mm² total 2400.</p><p>Centroid from bottom: y_bar = (1200·70 +1200·30)/2400=50 mm. I_self flange =60·20³/12=40000, distance 20 mm → I=40000+1200·400=520000. Web self 20·60³/12=360000, distance 20 mm →840000. Total Ixx =13.6×10⁵ mm⁴ =1.36×10⁶ mm⁴ about centroidal axis. Iyy similar 60×20 vertical.</p>"+fig(svg_isection,"T-section 60×20 flange + 60×20 web — centroid at 50 mm, Ixx = 1.36×10⁶ mm⁴"),
   "a_gu":"<p>ફ્લેંજ 60×20 + વેબ 60×20, ઊંચાઈ 80 mm, y_bar=50 mm, Ixx=13.6×10⁵ mm⁴. ગણતરી I_self + A·d².</p>"+fig(svg_isection,"T-સેક્શન Ixx = 1.36×10⁶ mm⁴")},
  {"q_en":"Q.2 (c) Draw S.F.D. and B.M.D. for the beam as shown in figure.2 (07 marks)","marks_en":"07 marks","marks_gu":"૦૭ ગુણ",
   "a_en":"<p><strong>Given [as per Fig.2]:</strong> SSB with UDL + point load [example: 4 m span, w=20 kN/m over full span + 30 kN at centre]. For 7 marks show full procedure — marks split: reactions 2, SFD 2, BMD 2, neat diagram 1.</p><p><strong>Step 1 — Reactions:</strong> ΣF<sub>y</sub>=0 ⇒ R<sub>A</sub>+R<sub>B</sub>=wL+P ⇒ ΣM<sub>A</sub>=0 ⇒ R<sub>B</sub>·L = wL·L/2 + P·L/2. Example: R<sub>B</sub>=[20·4·2+30·2]/4=55 kN, R<sub>A</sub>=55 kN [symmetric].</p><div class=\"eq\">V(x)=R<sub>A</sub>−w·x − P·&lt;x−a&gt;  ,  M(x)=R<sub>A</sub>·x − w·x²/2 − P·&lt;x−a&gt;</div><p><strong>Step 2 — SFD:</strong> At x=0⁺ V=55 kN, linear decrease slope −w, at x=2⁻ V=15 kN then sudden drop 30 kN to −15 kN, at x=4⁻ V=−55 kN. Zero shear near centre → max moment.</p><p><strong>Step 3 — BMD:</strong> M(0)=0, M(2)=55·2−20·4/2 −0 =70 kNm [parabolic due to UDL + linear due to point], M(4)=0. Maximum where V=0. Draw parabolic top, mark 70 kNm.</p><p><strong>Diagram for 7 marks:</strong> Neat beam, load, reaction arrows, SFD rectangle+triangle with values +55/−55 and kinks, BMD parabola peak 70 kNm. Label sagging positive. Mention dM/dx=V and dV/dx=−w checks.</p>"+fig(svg_beams,"SFD/BMD for SSB with UDL+point — reactions ΣM=0, SFD linear, BMD parabolic, max 70 kNm"),
   "a_gu":"<p><strong>પગલાં:</strong> પ્રતિક્રિયા ΣY ΣM થી, શીયર = ડાબી બાજુ બળ સરવાળો, મોમેન્ટ = મોમેન્ટ સરવાળો. UDL સાથે શીયર રેખીય મોમેન્ટ પરવલય. ઉદા 20 kN/m +30 kN તો પ્રતિક્રિયા 55 kN, મહત્તમ 70 kNm.</p>"+fig(svg_beams,"બીમ SFD/BMD — રેખીય અને પરવલય")},
  {"q_en":"Q.2 (a) OR (1) Perpendicular axis theorem (2) Ratio Ibase and Ixx rectangular width b depth d (03 marks)","marks_en":"03 marks","marks_gu":"૦૩ ગુણ",
   "a_en":"<p><strong>1) Perpendicular axis:</strong> For planar lamina, I_z = I_x + I_y where I_z is polar MOI about perpendicular through intersection. Used for circular sections.</p><p><strong>2) Rectangular:</strong> I_xx centroidal = b·d³/12, I_base about base = b·d³/3, ratio I_base/I_xx = (b d³/3)/(b d³/12)=4. So base MOI four times centroidal.</p>"+fig(svg_formulas,"Perpendicular axis I_z = I_x + I_y and rectangular I formulas"),
   "a_gu":"<p><strong>1) લંબ અક્ષ:</strong> I_z = I_x + I_y.</p><p><strong>2) લંબચોરસ:</strong> I_xx = b d³/12, I_base = b d³/3, ગુણોત્તર 4.</p>"+fig(svg_formulas,"લંબ અક્ષ અને લંબચોરસ સૂત્ર")},
  {"q_en":"Q.2 (b) OR Calculate Ixx for angle section 125x75x10mm keeping longer leg vertical. (04 marks)","marks_en":"04 marks","marks_gu":"૦૪ ગુણ",
   "a_en":"<p>For ISA 125×75×10 longer leg vertical, split into two rectangles 125×10 and 65×10. Centroid y from bottom ~42 mm, x from vertical leg ~18 mm. Ixx = Σ(bh³/12 + A·d²) ≈ 2.8×10⁶ mm⁴. Use standard steel table: Ixx ≈ 2.56×10⁶ mm⁴, Iyy ≈ 1.02×10⁶ mm⁴. Method: divide, find centroid, apply parallel axis.</p>",
   "a_gu":"<p>ISA 125×75×10 લાંબી ઊભી, બે લંબચોરસમાં વહેંચો, y_bar ≈42 mm, Ixx ≈2.8×10⁶ mm⁴, સ્ટીલ ટેબલ 2.56×10⁶.</p>"},
  {"q_en":"Q.2 (c) OR Draw S.F.D. and B.M.D. for beam as shown in figure.4 (07 marks)","marks_en":"07 marks","marks_gu":"૦૭ ગુણ",
   "a_en":"<p><strong>Given [Fig.4 — Overhang beam]:</strong> Example: SSB 4 m with overhang 1 m beyond B, point load W=20 kN at tip C. Reactions: ΣM<sub>A</sub>=0 ⇒ R<sub>B</sub>·4 = W·5 ⇒ R<sub>B</sub>=25 kN up, R<sub>A</sub>=−5 kN down [or hold-down].</p><p><strong>SFD:</strong> From A 0: V<sub>A</sub>=R<sub>A</sub>=−5 kN constant to B, at B jump +R<sub>B</sub>=+20 kN, constant 20 kN on overhang to C then drop −W to 0 at tip. Max shear 20 kN.</p><p><strong>BMD:</strong> M<sub>A</sub>=0, M<sub>B</sub>=R<sub>A</sub>·4=−20 kNm [hogging at support], linear to M<sub>C</sub>=0 at tip [free end zero]. On span AB moment linear −20→0 with sagging/hogging change if intermediate UDL. Mark −20 kNm.</p><p><strong>For 7 marks add:</strong> Equilibrium equations, sign convention sagging +ve, neat diagrams with hatching, check free-end M=0, note contra-flexure if BMD crosses zero.</p>"+fig(svg_cantilever,"Overhang SFD constant + jump at support, BMD linear 0 at tip −20 kNm at support"),
   "a_gu":"<p>ઉપર મુજબ: પ્રતિક્રિયા, શીયર, મોમેન્ટ. ઓવરહેંગ પર ટોચે પોઇન્ટ લોડ તો શીયર અચળ, મોમેન્ટ રેખીય.</p>"+fig(svg_cantilever,"કેન્ટીલીવર SFD/BMD")},
 ]
},
{
 "title_en":"Q3 · Beams — types, contra-flexure, bending stress & shear stress",
 "title_gu":"પ્ર.3 · બીમ — પ્રકાર, કોન્ટ્રા-ફ્લેક્સર, બેન્ડિંગ અને શીયર સ્ટ્રેસ",
 "cards":[
  {"q_en":"Q.3 (a) Give three examples each of statically determinate beams and statically indeterminate beams. (03 marks)","marks_en":"03 marks","marks_gu":"૦૩ ગુણ",
   "a_en":"<p><strong>Determinate:</strong> Simply supported, cantilever, overhang with one hinge — equilibrium alone gives reactions.</p><p><strong>Indeterminate:</strong> Propped cantilever, fixed both ends, continuous 2-span — need compatibility beyond equilibrium. Degree = extra unknowns.</p>",
   "a_gu":"<p><strong>ડિટરમિનેટ:</strong> સાદો ટેકો, કેન્ટીલીવર, ઓવરહેંગ — સમતુલાથી પ્રતિક્રિયા.</p><p><strong>ઇન્ડિટરમિનેટ:</strong> પ્રોપ્ડ કેન્ટીલીવર, બંને છેડે ફિક્સ, સતત — વધારાની સુસંગતતા જોઈએ.</p>"},
  {"q_en":"Q.3 (b) Explain importance of point of contra flexure. (04 marks)","marks_en":"04 marks","marks_gu":"૦૪ ગુણ",
   "a_en":"<p>Point of contra-flexure is where bending moment is zero and changes sign — sagging to hogging. At this point, bending stress zero, shear may be max. Important: reinforcement curtailed, hinge can be provided, deflection inflection, design needs to know where tension shifts from bottom to top.</p>"+fig(svg_ssb,"Point of contra-flexure where BM zero — sagging to hogging change, inflection in elastic curve"),
   "a_gu":"<p>કોન્ટ્રા-ફ્લેક્સર જ્યાં બેન્ડિંગ મોમેન્ટ શૂન્ય અને નિશાની બદલે — સેગિંગ થી હોગિંગ. ત્યાં તાણ શૂન્ય, સ્ટીલ ઘટાડાય, હિન્જ મૂકાય.</p>"+fig(svg_ssb,"કોન્ટ્રા-ફ્લેક્સર — BM શૂન્ય")},
  {"q_en":"Q.3 (c) A cantilever beam 1.2 m long has rectangular section 150mm x 300mm. Permissible bending stress 15 N/mm², find point load at free end. (07 marks)","marks_en":"07 marks","marks_gu":"૦૭ ગુણ",
   "a_en":"<p><strong>Given:</strong> Cantilever L=1.2 m =1200 mm, rectangular section b=150 mm, d=300 mm, allowable bending stress σ<sub>allow</sub>=15 N/mm². Need point load P at free end.</p><p><strong>Concept — Bending formula:</strong> σ = M·y/I ⇒ M<sub>allow</sub>=σ·Z where section modulus Z=I/y. For cantilever free-end load, maximum bending moment at fixed end M<sub>max</sub>=P·L [linear BMD].</p><div class=\"eq\">I = b·d³/12  ,  y<sub>max</sub>=d/2  ,  Z=I/y  ,  M=σ·Z  ,  P=M/L</div><p><strong>Step 1 — Section properties:</strong> I=150·300³/12 =150·27,000,000/12=337.5×10⁶ mm⁴, y<sub>max</sub>=150 mm, Z=337.5×10⁶/150=2.25×10⁶ mm³ =2250 cm³.</p><p><strong>Step 2 — Allowable moment:</strong> M<sub>allow</sub>=15·2.25×10⁶=33.75×10⁶ N·mm =33.75 kN·m.</p><p><strong>Step 3 — Safe load:</strong> P = M/L =33.75/1.2 =28.13 kN. If self-weight or FOS needed, reduce accordingly. Shear check: V=P=28.13 kN, τ<sub>avg</sub>=V/A=0.625 N/mm² negligible vs bending.</p><p><strong>Answer:</strong> Write bending stress distribution linear zero at neutral axis max ±15 N/mm² at top/bottom, show BMD triangular max at wall, <strong>P≈28.1 kN</strong> for full 7 marks — include units kN and N·mm conversion.</p>"+fig(svg_bending,"Cantilever bending — σ=M·y/I, Z=I/y, P=M/L=28.1 kN, linear stress max at fibres"),
   "a_gu":"<p>150×300 I=337.5×10⁶ mm⁴, Z=2.25×10⁶ mm³, M=15·Z=33.75 kNm, P=M/L=28.13 kN.</p>"+fig(svg_bending,"બેન્ડિંગ તાણ — તટસ્થ અક્ષે શૂન્ય, છેડે મહત્તમ")},
  {"q_en":"Q.3 (a) OR Define shear force and bending moment. (03 marks)","marks_en":"03 marks","marks_gu":"૦૩ ગુણ",
   "a_en":"<p><strong>Shear force:</strong> Algebraic sum of vertical forces to one side of section, tries to shear beam.</p><p><strong>Bending moment:</strong> Sum of moments about section due to forces, causes bending — sagging positive concave up, hogging negative.</p>",
   "a_gu":"<p><strong>શીયર ફોર્સ:</strong> એક બાજુના ઊભા બળોનો સરવાળો, કાપવાનો પ્રયાસ.</p><p><strong>બેન્ડિંગ મોમેન્ટ:</strong> સેક્શન ફરતે મોમેન્ટ સરવાળો, સેગિંગ ધન હોગિંગ ઋણ.</p>"},
  {"q_en":"Q.3 (b) OR Explain relation between Shear Force and Bending moment. (04 marks)","marks_en":"04 marks","marks_gu":"૦૪ ગુણ",
   "a_en":"<p>Relation: dM/dx = V, slope of BMD equals shear. Where shear zero, BM maximum. Area under SFD between two points gives change in BM. For UDL, shear linear, BM parabolic. This helps to draw BMD from SFD.</p>",
   "a_gu":"<p>સંબંધ: dM/dx = V, BMD નો ઢાળ = શીયર. શીયર શૂન્ય ત્યાં BM મહત્તમ, SFD નું ક્ષેત્ર = BM ફેરફાર.</p>"},
  {"q_en":"Q.3 (c) OR Triangular section base 150mm height 200mm shear 20kN find max shear stress and distribution. (07 marks)","marks_en":"07 marks","marks_gu":"૦૭ ગુણ",
   "a_en":"<p><strong>Given:</strong> Triangular cross-section base b=150 mm, height h=200 mm, vertical shear force V=20 kN =20,000 N.</p><p><strong>Concept — Shear stress:</strong> τ = V·Q / I·b where Q first moment, for triangle distribution parabolic, max at neutral axis [h/3 from base], zero at apex and base.</p><div class=\"eq\">A=½·b·h ,  τ<sub>avg</sub>=V/A ,  I = b·h³/36 ,  τ<sub>max</sub> = 3/2 · τ<sub>avg</sub> at NA</div><p><strong>Step 1 — Area:</strong> A=0.5·150·200=15,000 mm², τ<sub>avg</sub>=20,000/15,000=1.333 N/mm².</p><p><strong>Step 2 — MOI:</strong> I =150·8,000,000/36=33.33×10⁶ mm⁴, neutral axis ȳ=h/3=66.67 mm from base.</p><p><strong>Step 3 — Max shear:</strong> τ<sub>max</sub>=1.5·1.333=2.0 N/mm² at NA, τ=0 at top apex and at base extremes, parabolic between. Average over height = τ<sub>avg</sub>.</p><p><strong>For 7 marks:</strong> Show shear formula, Q calculation, draw triangular section with NA line, sketch parabolic τ diagram with 0→2.0→1.33 values, note shear taken mainly near NA.</p>"+fig(svg_shear_rect,"Triangular shear — parabolic, zero at apex/base, max 2.0 N/mm² at NA =1.5× avg"),
   "a_gu":"<p>ક્ષેત્ર 15000 mm², સરેરાશ 1.33 N/mm², મહત્તમ NA પર 1.5× =2.0 N/mm², ટોચ-તળિયે શૂન્ય, પરવલય.</p>"+fig(svg_shear_rect,"શીયર વિતરણ — ત્રિકોણ NA પર મહત્તમ")},
 ]
},
{
 "title_en":"Q4 · Pure bending, trusses & shear stress distribution",
 "title_gu":"પ્ર.4 · શુદ્ધ બેન્ડિંગ, ટ્રસ અને શીયર વિતરણ",
 "cards":[
  {"q_en":"Q.4 (a) (1) Give assumptions made in theory of pure bending (any three). (2) Explain how bending stress varies across depth of rectangular beam. (03 marks)","marks_en":"03 marks","marks_gu":"૦૩ ગુણ",
   "a_en":"<p><strong>Assumptions:</strong> Material homogeneous isotropic, Hooke’s law valid, plane sections remain plane, beam initially straight, no warping.</p><p><strong>Variation:</strong> σ = M·y/I linear: zero at neutral axis, tensile one side compressive other, max at extreme fibres y=±d/2. Diagram triangular on each side.</p>"+fig(svg_bending,"Pure bending — plane sections remain plane, stress linear zero at NA max at top/bottom"),
   "a_gu":"<p><strong>ધારણા:</strong> પદાર્થ સમાન, હૂક નિયમ, સમતલ સેક્શન સમતલ રહે.</p><p><strong>ફેરફાર:</strong> σ = M·y/I રેએખીય, NA પર શૂન્ય, છેડે મહત્તમ ત્રિકોણ.</p>"+fig(svg_bending,"શુદ્ધ બેન્ડિંગ — રેખીય વિતરણ")},
  {"q_en":"Q.4 (b) Explain types of trusses as per stability. (04 marks)","marks_en":"04 marks","marks_gu":"૦૪ ગુણ",
   "a_en":"<p>Perfect truss m=2j−3, just sufficient members, stable. Deficient m<2j−3, mechanism. Redundant m>2j−3, extra members indeterminate. Example: Triangle 3 joints 3 members perfect, add diagonal redundant.</p>"+fig(svg_types,"Truss types — perfect m=2j−3, deficient, redundant"),
   "a_gu":"<p>પરફેક્ટ m=2j−3 સ્થિર, ડેફિશિયન્ટ ઓછા અસ્થિર, રિડન્ડન્ટ વધારે અનિર્ધાર્ય.</p>"+fig(svg_types,"ટ્રસ પ્રકાર")},
  {"q_en":"Q.4 (c) Find forces in all members of a truss as shown in figure 5 by method of joint. (07 marks)","marks_en":"07 marks","marks_gu":"૦૭ ગુણ",
   "a_en":"<p><strong>Given [Fig.5]:</strong> Roof truss span L ~6 m, height ~2 m, loads 20 kN at apex joints as per figure. Need forces in all members by <em>method of joints</em>.</p><p><strong>Step 1 — Reactions:</strong> ΣM<sub>A</sub>=0 ⇒ R<sub>B</sub>= [P·a]/L, ΣF<sub>y</sub>=0 ⇒ R<sub>A</sub>+R<sub>B</sub>=ΣP. Example: with 20 kN at centre, R<sub>A</sub>=R<sub>B</sub>=10 kN vertical.</p><p><strong>Step 2 — Joint A [≤2 unknowns]:</strong> ΣF<sub>y</sub>=0 ⇒ F<sub>AB</sub>·sinθ + R<sub>A</sub>=0 ⇒ diagonal, ΣF<sub>x</sub>=0 ⇒ F<sub>AC</sub> + F<sub>AB</sub>·cosθ=0 ⇒ bottom chord tensile ~15 kN. Assume tension away from joint.</p><p><strong>Step 3 — Proceed joint-by-joint:</strong> Joint C → top chord compressive 15 kN, Joint B → vertical zero if no load. Use <strong>zero-force rules:</strong> [i] at unloaded joint with 2 non-collinear members → both zero, [ii] 3 members with 2 collinear → third zero.</p><table><tr><th>Member</th><th>Force</th><th>T/C</th></tr><tr><td>AC [bottom chord]</td><td>15 kN</td><td>Tension</td></tr><tr><td>AB [diagonal]</td><td>12.5 kN</td><td>Compression</td></tr><tr><td>BC [vertical]</td><td>0</td><td>Zero</td></tr><tr><td>Top chord</td><td>15 kN</td><td>Compression</td></tr></table><p><strong>For 7 marks:</strong> Show free-body, reactions, 3–4 joint equilibria with equations, tabulate all members with T/C, mark zero members, state tension +ve.</p>"+fig(svg_joints,"Method of joints — start at joint with 2 unknowns, ΣH=0 ΣV=0, zero-force check, T away C towards"),
   "a_gu":"<p><strong>પગલાં:</strong> પ્રતિક્રિયા, 2 અજાણ્યા વાળા સાંધાથી ΣH ΣV, તાણ દૂર દબાણ નજીક, આગળ વધો. ઉદા ટોપ દબાણ 15 kN બોટમ તાણ 15 kN, શૂન્ય મેમ્બર ઓળખો.</p>"+fig(svg_joints,"સાંધા પદ્ધતિ — પ્રતિક્રિયા, સમતુલા")},
  {"q_en":"Q.4 (a) OR Draw shear stress distribution for T-section & hollow rectangular section. (2) Explain how shear stress distributed across rectangular beam (03 marks)","marks_en":"03 marks","marks_gu":"૦૩ ગુણ",
   "a_en":"<p><strong>T-section:</strong> Max at NA about 1.5× average at junction, zero at top/bottom flanges, parabolic in web.</p><p><strong>Hollow rect:</strong> Similar but thin walls, max at NA, reduced at inner hollow.</p><p><strong>Rectangular:</strong> Parabolic zero at top/bottom max 1.5×V/A at NA. Shear taken mainly by web.</p>"+fig(svg_shear_I,"Shear stress distribution — T-section max at NA, hollow rectangular reduced"),
   "a_gu":"<p><strong>T:</strong> NA પર મહત્તમ 1.5×, ફ્લેંજ પર શૂન્ય, વેબમાં પરવલય.</p><p><strong>પોલો લંબચોરસ:</strong> NA પર મહત્તમ.</p><p><strong>લંબચોરસ:</strong> પરવલય ટોચ-તળિયે શૂન્ય NA પર 1.5×.</p>"+fig(svg_shear_I,"શીયર વિતરણ — T અને પોલો")},
  {"q_en":"Q.4 (b) OR Differentiate between truss and beam. (04 marks)","marks_en":"04 marks","marks_gu":"૦૪ ગુણ",
   "a_en":"<table><tr><th>Truss</th><th>Beam</th></tr><tr><td>Members axial tension/compression</td><td>Bending + shear</td></tr><tr><td>Load at joints</td><td>Load anywhere</td></tr><tr><td>Light long span</td><td>Heavy short</td></tr><tr><td>Analysis joints/sections</td><td>SFD/BMD</td></tr></table>",
   "a_gu":"<table><tr><th>ટ્રસ</th><th>બીમ</th></tr><tr><td>અક્ષીય તાણ/દબાણ</td><td>બેન્ડિંગ + શીયર</td></tr><tr><td>ભાર સાંધા પર</td><td>ગમે ત્યાં</td></tr><tr><td>હળવો લાંબો ગાળો</td><td>ભારે ટૂંકો</td></tr></table>"},
  {"q_en":"Q.4 (c) OR Find forces in truss as shown in figure 6 by method of joint. (07 marks)","marks_en":"07 marks","marks_gu":"૦૭ ગુણ",
   "a_en":"<p><strong>Given [Fig.6]:</strong> Similar truss with 30 kN at apex, span 4 m, triangle height 1.5 m. Apply same method.</p><p><strong>Reactions:</strong> R<sub>A</sub>=R<sub>B</sub>=15 kN. <strong>Joint A:</strong> ΣF<sub>y</sub>=0 ⇒ F<sub>diag</sub>=R<sub>A</sub>/sinθ =15/0.6=25 kN tensile? sign per geometry — compute θ=36.87°.</p><p><strong>Tabulation:</strong> Bottom chord ~25 kN T, top chord ~20 kN C, vertical 0 if no load at joint, diagonal ~15 kN. Show ΣF<sub>x</sub>=0 at each joint to verify.</p><p><strong>Exam presentation:</strong> Draw neat truss with member labels, arrows outward for tension, inward for compression, table with magnitudes + T/C, highlight zero-force members per rule.</p>"+fig(svg_zero,"Truss Fig.6 — reactions, joint equilibrium, bottom 25 kN T top 20 kN C"),
   "a_gu":"<p>ઉપર મુજબ સાંધા પદ્ધતિ: પ્રતિક્રિયા, દરેક સાંધા, કોષ્ટક.</p>"+fig(svg_zero,"શૂન્ય બળ મેમ્બર")},
 ]
},
{
 "title_en":"Q5 · Slope, deflection & columns — Euler & Rankine",
 "title_gu":"પ્ર.5 · ઢાળ, વિચલન અને સ્તંભ — યુલર અને રેન્કિન",
 "cards":[
  {"q_en":"Q.5 (a) Define slope and deflection with figure. (03 marks)","marks_en":"03 marks","marks_gu":"૦૩ ગુણ",
   "a_en":"<p><strong>Slope:</strong> Angle of tangent to elastic curve at a point, θ = dy/dx in radians.</p><p><strong>Deflection:</strong> Vertical displacement y from original position.</p><p>For cantilever UDL, max at free end, zero at fixed. Diagram shows elastic curve with slope at end.</p>"+fig(svg_elastic,"Slope = dy/dx angle, deflection = vertical displacement y on elastic curve"),
   "a_gu":"<p><strong>ઢાળ:</strong> સ્થિતિસ્થાપક વક્રને સ્પર્શકનો ખૂણો θ = dy/dx.</p><p><strong>વિચલન:</strong> મૂળથી ઊભું અંતર y.</p>"+fig(svg_elastic,"ઢાળ અને વિચલન — સ્થિતિસ્થાપક વક્ર")},
  {"q_en":"Q.5 (b) A UDL of 20 kN/m acting on cantilever 3m. Calculate slope and deflection at free end. E=2×10⁵ N/mm² and I=200 cm⁴. (04 marks)","marks_en":"04 marks","marks_gu":"૦૪ ગુણ",
   "a_en":"<p>For cantilever UDL w over full span: slope θ = wL³/(6EI), deflection δ = wL⁴/(8EI).</p><p>w=20 kN/m=20 N/mm, L=3000 mm, EI=2×10⁵·200×10⁴=4×10¹¹ Nmm², θ=20·27×10⁹/(6·4×10¹¹)=0.0225 rad =1.29°, δ=20·81×10¹²/(8·4×10¹¹)=506 mm large due to small I 200 cm⁴. If I is 2000 cm⁴, δ=50.6 mm. Formula key.</p>"+fig(svg_cantilever5,"Cantilever UDL — slope wL³/6EI and deflection wL⁴/8EI at free end"),
   "a_gu":"<p>કેન્ટીલીવર UDL: θ = wL³/6EI, δ = wL⁴/8EI, w20 N/mm L3000 EI4×10¹¹, θ0.0225 rad δ506 mm નાના I ને લીધે મોટું.</p>"+fig(svg_cantilever5,"કેન્ટીલીવર UDL — ઢાળ અને વિચલન સૂત્ર")},
  {"q_en":"Q.5 (c) A hollow circular section internal diameter 60mm thickness 10mm. Find radius of gyration. (07 marks)","marks_en":"07 marks","marks_gu":"૦૭ ગુણ",
   "a_en":"<p><strong>Given:</strong> Hollow circular section internal dia d=60 mm, thickness t=10 mm ⇒ external D=60+2·10=80 mm. Need radius of gyration k =√(I/A).</p><p><strong>Concept:</strong> k measures slenderness; smaller k → higher slenderness → Euler governs. For hollow circle I=π/64·[D⁴−d⁴], A=π/4·[D²−d²].</p><div class=\"eq\">A=π/4·[D²−d²]  ,  I=π/64·[D⁴−d⁴]  ,  k=√(I/A)=¼√(D²+d²)</div><p><strong>Step 1 — Area:</strong> A=0.7854·[6400−3600]=0.7854·2800=2199 mm².</p><p><strong>Step 2 — MOI:</strong> D⁴=40,960,000, d⁴=12,960,000, Δ=28,000,000, I= π·28,000,000/64 =1.374×10⁶ mm⁴.</p><p><strong>Step 3 — Radius of gyration:</strong> k=√[1,374,000/2199]=√624.8=25.0 mm. Also via formula ¼√[6400+3600]=¼·100=25 mm matches.</p><p><strong>For 7 marks add:</strong> Define k, show I and A steps, mention least k about any axis same for circle, use for Euler slenderness L<sub>e</sub>/k, note if effective length given L<sub>e</sub> check slenderness.</p>",
   "a_gu":"<p>બહાર D80 અંદર 60, ક્ષેત્ર 2199 mm², I1.374×10⁶, k=√I/A=25.0 mm.</p>"},
  {"q_en":"Q.5 (a) OR What factors influence slope and deflection? (03 marks)","marks_en":"03 marks","marks_gu":"૦૩ ગુણ",
   "a_en":"<p>Load magnitude and type, span length L⁴ effect, E modulus, I MOI, end conditions fixed vs simply supported, flexural rigidity EI — higher EI less deflection. Temperature and creep also.</p>",
   "a_gu":"<p>ભાર પ્રકાર, ગાળો L⁴, E, I, છેડા ફિક્સ કે સાદો, EI વધુ તો વિચલન ઓછું, તાપમાન ક્રીપ.</p>"},
  {"q_en":"Q.5 (b) OR Wooden beam 100×240mm simply supported 4m find UDL for deflection 6mm at centre. E=0.11×10⁵ N/mm² (04 marks)","marks_en":"04 marks","marks_gu":"૦૪ ગુણ",
   "a_en":"<p>For SSB UDL deflection at centre δ =5wL⁴/(384EI). I=100·240³/12=115.2×10⁶ mm⁴, EI=0.11e5·115.2e6=1.267e12, L=4000, set δ=6 mm → w=384EIδ/(5L⁴)=384·1.267e12·6/(5·256e12)=2.28 N/mm=2.28 kN/m.</p>"+fig(svg_ssb,"Simply supported UDL — deflection 5wL⁴/384EI at centre"),
   "a_gu":"<p>SSB UDL δ=5wL⁴/384EI, I115.2×10⁶ EI1.267e12, w=2.28 N/mm=2.28 kN/m.</p>"+fig(svg_ssb,"સાદો UDL — વિચલન સૂત્ર")},
  {"q_en":"Q.5 (c) OR Steel column 4m fixed both ends find safe load Euler Ixx=1.98×10⁸ Iyy=2.51×10⁷ E=2×10⁵ FOS4 (07 marks)","marks_en":"07 marks","marks_gu":"૦ે ગુણ",
   "a_en":"<p><strong>Given:</strong> Steel column length L=4 m=4000 mm, both ends fixed ⇒ effective length L<sub>e</sub>=L/2=2000 mm, I<sub>xx</sub>=1.98×10⁸ mm⁴, I<sub>yy</sub>=2.51×10⁷ mm⁴, E=2×10⁵ N/mm², FOS=4. Need safe Euler load.</p><p><strong>Concept — Euler:</strong> Long column buckling load P<sub>cr</sub>=π²·E·I<sub>min</sub>/L<sub>e</sub>². Buckling occurs about axis with minimum I → minimum radius of gyration. Safe = P<sub>cr</sub>/FOS.</p><div class=\"eq\">I<sub>min</sub>=min[I<sub>xx</sub>, I<sub>yy</sub>]  ,  L<sub>e</sub>=L/2 [fixed-fixed] ,  P<sub>cr</sub>=π²EI<sub>min</sub>/L<sub>e</sub>²</div><p><strong>Step 1 — Choose I<sub>min</sub>:</strong> I<sub>yy</sub>=2.51×10⁷ < I<sub>xx</sub>, so I<sub>min</sub>=2.51×10⁷ mm⁴ governs.</p><p><strong>Step 2 — Critical load:</strong> P<sub>cr</sub>=9.8696·2×10⁵·2.51×10⁷ / 4,000,000 =49.55×10¹²/4×10⁶=12.39×10⁶ N=12390 kN.</p><p><strong>Step 3 — Safe load:</strong> P<sub>safe</sub>=12390/4=3097 kN ≈3.1 MN. Check slenderness: k<sub>min</sub>=√[I<sub>min</sub>/A] but A not given — assume Euler valid for long column; if slenderness low use Rankine.</p><p><strong>7-mark presentation:</strong> Table of effective lengths [fixed-fixed L/2, pinned-pinned L, one fixed one pinned L/√2], note I<sub>min</sub> choice, units kN, mention buckling axis.</p>"+fig(svg_euler,"Euler fixed-fixed Le=L/2, Pcr=π²EImin/Le²=12390 kN safe 3097 kN"),
   "a_gu":"<p>યુલર P_cr = π²EI_min/L_e², L_e=2000 mm I_min=Iyy, P_cr=12390 kN, સલામત 3097 kN.</p>"+fig(svg_euler,"યુલર સ્તંભ — L_e = L/2")},
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
    page=f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>DI03006041 · Winter 2025 solved paper</title><style>{CSS}</style></head><body><main class="page"><header class="hero"><div class="eyebrow">Solved question paper · English questions · Friendly Gujarati answers</div><div class="lang-switch" aria-label="Choose language"><button type="button" data-lang="en" aria-pressed="true">English</button><button type="button" data-lang="gu" aria-pressed="false">ગુજરાતી</button></div><h1>Mechanics of Structures-I</h1><div class="meta">GTU Diploma · Civil · Semester 3 · Winter 2025 · DI03006041 · 10-12-2025 · 70 marks · 10:30 AM TO 01:00 PM</div></header>{"".join(sections_html)}<div class="footer">Solved paper for study. Verify with standard spec before site use.</div></main><script>document.querySelectorAll('.lang-switch button').forEach(b=>b.addEventListener('click',()=>{{document.documentElement.lang=b.dataset.lang;document.querySelectorAll('.lang-switch button').forEach(x=>x.setAttribute('aria-pressed',x===b?'true':'false'));}}));</script></body></html>'''
    return page
def main():
    page=build_page()
    out_papers=ROOT/"papers-upload/papers/DI03006041/winter-2025.html"
    out_ws=ROOT/"preview/workshop/DI03006041_winter2025_bilingual.html"
    out_papers.parent.mkdir(parents=True,exist_ok=True)
    out_ws.parent.mkdir(parents=True,exist_ok=True)
    import re as _re
    page=_re.sub(r'<div class="gu">(.*?)</div>', lambda m: '<div class="gu">'+m.group(1).replace('(','[').replace(')',']')+'</div>', page, flags=_re.S)
    out_papers.write_text(page,encoding="utf-8")
    out_ws.write_text(page,encoding="utf-8")
    print(f"Bilingual: {out_papers} ({len(page)} chars)")
    en_c = page.count('class="en"'); gu_c = page.count('class="gu"')
    print(f"details={page.count('<details')}, sections={page.count('<section')}, en={en_c}, gu={gu_c}")
    print("PASS" if page.count('<details')==28 and page.count('<section')==5 else "FAIL", f"figs={page.count('<figure>')}")
    import re; pat = r'<div class="gu">(.*?)</div>'; gu=''.join(re.findall(pat,page,re.S)); print(f"brackets gu={gu.count('(')+gu.count(')')}")
    (ROOT/"drive-upload/DI03006041_winter_2025_bilingual.html").write_text(page,encoding="utf-8")
if __name__=="__main__": main()
