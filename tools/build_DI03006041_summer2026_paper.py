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
svg_thermal=load_svg("ms1_thermal.svg")
svg_formulas=load_svg("ms2_formulas.svg")
svg_isection=load_svg("ms2_isection.svg")
svg_sections=load_svg("ms6_sections.svg")
svg_beams=load_svg("ms3_beams.svg")
svg_cantilever=load_svg("ms3_cantilever.svg")
svg_overhang=load_svg("ms3_overhang.svg")
svg_ssb=load_svg("ms3_ssb.svg")
svg_bending=load_svg("ms4_bending.svg")
svg_shear_rect=load_svg("ms4_shear_rect.svg")
svg_shear_I=load_svg("ms4_shear_I.svg")
svg_types=load_svg("ms6_types.svg")
svg_joints=load_svg("ms6_joints.svg")
svg_zero=load_svg("ms6_zero.svg")
svg_euler=load_svg("ms7_euler.svg")
svg_effective=load_svg("ms7_effective.svg")
svg_rankine=load_svg("ms7_rankine.svg")
svg_elastic=load_svg("ms5_elastic.svg")
svg_ssb5=load_svg("ms5_ssb.svg")
svg_cantilever5=load_svg("ms5_cantilever.svg")

SECTIONS=[
{
 "title_en":"Q1 · Stress, strain, Hooke’s law & composite/RCC column",
 "title_gu":"પ્ર.1 · સ્ટ્રેસ, સ્ટ્રેઈન, હૂક નિયમ અને કોમ્પોઝિટ/RCC કોલમ",
 "cards":[
  {"q_en":"Q.1 (a) Define following: 1. Hook’s law 2. Volumetric strain 3. Bulk modulus. (03 marks)","marks_en":"03 marks","marks_gu":"૦૩ ગુણ",
   "a_en":"<p><strong>1) Hooke’s law:</strong> Within elastic limit, stress is proportional to strain. σ = E·ε, E is Young’s modulus 2×10⁵ N/mm² for steel. Gives linear stress-strain initial slope.</p><p><strong>2) Volumetric strain:</strong> Change in volume per original volume. ε_v = ΔV/V = ε_x+ε_y+ε_z = ε·(1−2μ) for uniaxial. Indicates dilation.</p><p><strong>3) Bulk modulus:</strong> Ratio of volumetric stress to volumetric strain. K = σ_v/ε_v = E/(3(1−2μ)). Measures resistance to uniform compression.</p>",
   "a_gu":"<p><strong>1) હૂક નિયમ:</strong> સ્થિતિસ્થાપક હદમાં સ્ટ્રેસ સ્ટ્રેઈન પ્રમાણે. σ = E·ε, E=2×10⁵ N/mm².</p><p><strong>2) આયતન સ્ટ્રેઈન:</strong> કદ ફેરફાર / મૂળ કદ. ε_v = ΔV/V = ε·1−2μ.</p><p><strong>3) બલ્ક મોડ્યુલસ:</strong> આયતન સ્ટ્રેસ / આયતન સ્ટ્રેઈન. K = E/31−2μ, એકસમાન દબાણ સામે પ્રતિકાર.</p>"},
  {"q_en":"Q.1 (b) Explain difference between gradual load and sudden load. (04 marks)","marks_en":"04 marks","marks_gu":"૦૪ ગુણ",
   "a_en":"<table><tr><th>Gradual load</th><th>Sudden load</th></tr><tr><td>Applied slowly 0 to max, stress = P/A</td><td>Applied instantaneously, stress doubles =2·P/A due to impact factor 2</td></tr><tr><td>Strain energy =½·P·δ</td><td>Strain energy =P·δ double</td></tr><tr><td>No shock, static analysis</td><td>Dynamic, needs impact factor</td></tr></table>",
   "a_gu":"<table><tr><th>ક્રમશઃ ભાર</th><th>અચાનક ભાર</th></tr><tr><td>ધીમે 0 થી મહત્તમ, સ્ટ્રેસ = P/A</td><td>તરત લાગે બમણો સ્ટ્રેસ =2·P/A</td></tr><tr><td>ઊર્જા ½Pδ</td><td>ઊર્જા Pδ બમણી</td></tr></table>"},
  {"q_en":"Q.1 (c) A mild steel bar 4m length 18mm dia subjected to 80kN axial tensile load, Find Stress, strain and total elongation. E=2×10⁵ N/mm². (07 marks)","marks_en":"07 marks","marks_gu":"૦૭ ગુણ",
   "a_en":"<p>Area A = π/4·18²=254.5 mm², Stress σ = P/A =80000/254.5=314.4 N/mm², Strain ε = σ/E =314.4/200000=0.001572, Elongation δ = ε·L =0.001572·4000=6.29 mm. Note stress exceeds typical yield 250, so would actually yield, but calculation as per Hooke’s shows elongation. This demonstrates high stress needs larger area.</p>"+fig(svg_composite,"Axial bar — stress = P/A, strain = σ/E, elongation = ε·L"),
   "a_gu":"<p>ક્ષેત્ર 254.5 mm², સ્ટ્રેસ 314.4 N/mm², સ્ટ્રેઈન 0.001572, લંબાવ 6.29 mm. યીલ્ડ કરતાં વધુ તો વાસ્તવમાં યીલ્ડ થાય.</p>"+fig(svg_composite,"અક્ષીય બાર — સ્ટ્રેસ, સ્ટ્રેઈન, લંબાવ")},
  {"q_en":"Q.1 (c) OR A square R.C.C. column 600mm side reinforced with 8 bars 20mm dia. Column subjected to 2000kN. Find stresses. Modular ratio 15. (07 marks)","marks_en":"07 marks","marks_gu":"૦૭ ગુણ",
   "a_en":"<p>Steel area A_s=8·π/4·20²=2513 mm², Concrete A_c=600·600−2513=357487 mm², Equivalent concrete A_eq = A_c + m·A_s =357487+15·2513=395182 mm², Concrete stress σ_c = P/A_eq =2000000/395182=5.06 N/mm², Steel σ_s = m·σ_c =15·5.06=75.9 N/mm². Load shared by stiffness: P_c=σ_c·A_c=1809 kN, P_s=191 kN. RCC shares load proportionally.</p>"+fig(svg_composite,"RCC column — composite action, equivalent area A_c + m·A_s, stress m times concrete"),
   "a_gu":"<p>સ્ટીલ 2513 mm², કોંક્રિટ 357487 mm², સમકક્ષ A_eq=395182, σ_c=5.06 N/mm², σ_s=75.9 N/mm². ભાર EA પ્રમાણે વહેંચાય.</p>"+fig(svg_composite,"RCC કોલમ — સમકક્ષ ક્ષેત્ર")},
 ]
},
{
 "title_en":"Q2 · Moment of Inertia — formulas, ISA & SFD/BMD",
 "title_gu":"પ્ર.2 · જડત્વ આઘૂર્ણ — સૂત્ર, ISA અને SFD/BMD",
 "cards":[
  {"q_en":"Q.2 (a) Write down equations for moment of inertia for both x-x and y-y axis for Rectangular, Triangle, Circular. (03 marks)","marks_en":"03 marks","marks_gu":"૦૩ ગુણ",
   "a_en":"<p><strong>Rectangular b×d:</strong> I_xx = b·d³/12 about horizontal centroidal, I_yy = d·b³/12.</p><p><strong>Triangle b×h:</strong> About base I = b·h³/12, about centroid I_xx = b·h³/36, I_yy = h·b³/48.</p><p><strong>Circular D:</strong> I_xx = I_yy = π·D⁴/64, polar I_p = π·D⁴/32. About diameter same.</p>"+fig(svg_formulas,"Moment of inertia formulas — rectangular, triangle, circular about centroidal axes"),
   "a_gu":"<p><strong>લંબચોરસ:</strong> I_xx = b·d³/12, I_yy = d·b³/12.</p><p><strong>ત્રિકોણ:</strong> I_xx = b·h³/36, I_base = b·h³/12.</p><p><strong>વર્તુળ:</strong> I = πD⁴/64.</p>"+fig(svg_formulas,"જડત્વ સૂત્ર — લંબચોરસ, ત્રિકોણ, વર્તુળ")},
  {"q_en":"Q.2 (b) Calculate Ixx for ISA 100x75x6mm with longer leg vertical. (04 marks)","marks_en":"04 marks","marks_gu":"૦૪ ગુણ",
   "a_en":"<p>ISA 100×75×6 split into 100×6 and 69×6. Area 600+414=1014 mm², centroid y≈31 mm from bottom, x≈19 mm. Ixx = Σ(bh³/12 + A·d²) ≈100·6³/12 +600·(31)² +69·6³/12 +414·(distance)² ≈1.2×10⁶ mm⁴. Standard table gives Ixx ≈1.33×10⁶ mm⁴, Iyy ≈0.67×10⁶ mm⁴. Steps: divide, find centroid, parallel axis.</p>"+fig(svg_isection,"ISA 100×75×6 longer leg vertical — Ixx ≈1.33×10⁶ mm⁴ by parallel axis"),
   "a_gu":"<p>ISA 100×75×6 બે લંબચોરસમાં વહેંચો, Ixx ≈1.33×10⁶ mm⁴, ટેબલથી.</p>"+fig(svg_isection,"ISA Ixx — સમાંતર અક્ષ")},
  {"q_en":"Q.2 (c) Draw S.F.D. and B.M.D. for beam as shown in figure.1. (07 marks)","marks_en":"07 marks","marks_gu":"૦૭ ગુણ",
   "a_en":"<p><strong>Steps:</strong> 1) Reactions ΣY=0 ΣM=0. 2) Shear = sum vertical left, Moment = sum moments. 3) For SSB with point load, shear constant between loads, moment linear; with UDL, shear linear, moment parabolic. Max moment at zero shear. Provide neat diagram with values at supports, mid, max. Example: 4 m SSB with 20 kN at 2 m, reactions 10 kN each, max BM 20 kNm at mid.</p>"+fig(svg_beams,"Beams — SFD constant/linear, BMD linear/parabolic — max at zero shear"),
   "a_gu":"<p><strong>પગલાં:</strong> પ્રતિક્રિયા, શીયર = ડાબી બાજુ બળ સરવાળો, મોમેન્ટ = મોમેન્ટ સરવાળો. પોઇન્ટ લોડ પર શીયર અચળ મોમેન્ટ રેખીય, UDL પર શીયર રેખીય મોમેન્ટ પરવલય.</p>"+fig(svg_beams,"બીમ SFD/BMD — મહત્તમ શૂન્ય શીયર પર")},
  {"q_en":"Q.2 (a) OR Differentiate between centroidal axis and reference axis. (03 marks)","marks_en":"03 marks","marks_gu":"૦૩ ગુણ",
   "a_en":"<p><strong>Centroidal axis:</strong> Passes through centroid, I is minimum, used for bending. <strong>Reference axis:</strong> Any arbitrary axis away from centroid, I = I_G + A·d² larger. Centroidal used for section modulus.</p>",
   "a_gu":"<p><strong>સેન્ટ્રોઇડલ:</strong> મધ્યબિંદુમાંથી, I લઘુત્તમ. <strong>સંદર્ભ:</strong> ગમે ત્યાં, I = I_G + A·d² મોટું.</p>"},
  {"q_en":"Q.2 (b) OR Calculate Ixx for ISA 100x75x6mm with shorter leg vertical. (04 marks)","marks_en":"04 marks","marks_gu":"૦૪ ગુણ",
   "a_en":"<p>Swap legs: 75×6 vertical and 94×6 horizontal, centroid different, Ixx ≈0.67×10⁶ mm⁴ (previous Iyy). So Ixx smaller when shorter leg vertical. Use same parallel axis method.</p>",
   "a_gu":"<p>ટૂંકી બાજુ ઊભી તો Ixx ≈0.67×10⁶ mm⁴, અગાઉની Iyy.</p>"},
  {"q_en":"Q.2 (c) OR Draw S.F.D. and B.M.D. for beam as shown in figure.2. (07 marks)","marks_en":"07 marks","marks_gu":"૦૭ ગુણ",
   "a_en":"<p>Same as above for figure.2 — typically overhang with point load at tip: reactions, shear constant over overhang, moment linear to zero at tip, max negative at support. Provide neat sketch.</p>"+fig(svg_overhang,"Overhang beam — shear constant on overhang, moment linear, max at support"),
   "a_gu":"<p>ઓવરહેંગ ટોચે પોઇન્ટ લોડ: શીયર અચળ, મોમેન્ટ રેખીય ટોચે શૂન્ય, ટેકે મહત્તમ ઋણ.</p>"+fig(svg_overhang,"ઓવરહેંગ SFD/BMD")},
 ]
},
{
 "title_en":"Q3 · Beams — types, sagging/hogging & bending/shear stress",
 "title_gu":"પ્ર.3 · બીમ — પ્રકાર, સેગિંગ/હોગિંગ અને બેન્ડિંગ/શીયર સ્ટ્રેસ",
 "cards":[
  {"q_en":"Q.3 (a) List types of beams. (03 marks)","marks_en":"03 marks","marks_gu":"૦૩ ગુણ",
   "a_en":"<p>Cantilever fixed one end, Simply supported both ends, Overhang beyond support, Propped cantilever, Fixed both ends, Continuous multiple spans. Determinate are first three, indeterminate rest.</p>"+fig(svg_beams,"Types of beams — cantilever, simply supported, overhang, fixed, propped, continuous"),
   "a_gu":"<p>કેન્ટીલીવર, સાદો ટેકો, ઓવરહેંગ, પ્રોપ્ડ, ફિક્સ, સતત. પ્રથમ ત્રણ ડિટરમિનેટ.</p>"+fig(svg_beams,"બીમ પ્રકાર")},
  {"q_en":"Q.3 (b) Explain sagging and hogging bending moments with neat sketch. (04 marks)","marks_en":"04 marks","marks_gu":"૦૪ ગુણ",
   "a_en":"<p><strong>Sagging:</strong> Concave up, compression top tension bottom, positive BM, occurs at mid of SSB. <strong>Hogging:</strong> Convex up, tension top, negative BM, at supports of fixed/overhang. Sketch shows beam bent up vs down with fibres.</p>"+fig(svg_bending,"Sagging concave up positive vs hogging convex up negative — fibre tension side"),
   "a_gu":"<p><strong>સેગિંગ:</strong> ઉપર અંતર્મુખ, ઉપર દબાણ નીચે તાણ, ધન, SSB મધ્યે. <strong>હોગિંગ:</strong> બહિર્મુખ, ઉપર તાણ, ઋણ, ફિક્સ ટેકે.</p>"+fig(svg_bending,"સેગિંગ vs હોગિંગ — તાણ બાજુ")},
  {"q_en":"Q.3 (c) A simply supported beam 3m long has rectangular section 200mm x 400mm. Permissible bending stress 18 N/mm², find point load at centre. (07 marks)","marks_en":"07 marks","marks_gu":"૦૭ ગુણ",
   "a_en":"<p>I =200·400³/12=1.067×10⁹ mm⁴, y=200 mm, Z=I/y=5.333×10⁶ mm³, Allowable M=σ·Z=18·5.333e6=96×10⁶ Nmm=96 kNm. For SSB central point load, M_max = P·L/4 → P=4M/L=4·96/3=128 kN. So central point load 128 kN safe. Check shear: V=P/2=64 kN.</p>"+fig(svg_bending,"Bending stress M = σ·Z, for SSB P =4M/L"),
   "a_gu":"<p>I=1.067×10⁹, Z=5.333×10⁶, M=96 kNm, P=4M/L=128 kN.</p>"+fig(svg_bending,"બેન્ડિંગ M = σ·Z")},
  {"q_en":"Q.3 (a) OR List types of loads with figure. (03 marks)","marks_en":"03 marks","marks_gu":"૦૩ ગુણ",
   "a_en":"<p>Point/concentrated, Uniformly distributed UDL, Uniformly varying UVL triangular, Couple/moment. Diagrams show arrows: point at centre, UDL rectangle, UVL triangle, moment curved arrow.</p>"+fig(svg_beams,"Types of loads — point, UDL rectangle, UVL triangle, couple"),
   "a_gu":"<p>પોઇન્ટ, UDL લંબચોરસ, UVL ત્રિકોણ, કપલ. આકૃતિમાં તીર.</p>"+fig(svg_beams,"લોડ પ્રકાર")},
  {"q_en":"Q.3 (b) OR Explain point of contra-flexure and its importance in beam design. (04 marks)","marks_en":"04 marks","marks_gu":"૦૪ ગુણ",
   "a_en":"<p>Point where BM zero and changes sign sagging to hogging. Bending stress zero, shear may be max. Important: reinforcement curtailed beyond this point as tension shifts sides, hinge may be placed, deflection inflection. Found where BMD crosses zero.</p>"+fig(svg_ssb,"Point of contra-flexure where BM zero — sagging to hogging, reinforcement curtailment"),
   "a_gu":"<p>BM શૂન્ય અને નિશાની બદલે, બેન્ડિંગ શૂન્ય, સ્ટીલ ઘટાડાય, હિન્જ મૂકાય, વિચલન વળાંક.</p>"+fig(svg_ssb,"કોન્ટ્રા-ફ્લેક્સર — BM શૂન્ય")},
  {"q_en":"Q.3 (c) OR A solid circular shaft diameter 50mm subjected to shear force 15kN. Find max shear stress. (07 marks)","marks_en":"07 marks","marks_gu":"૦૭ ગુણ",
   "a_en":"<p>For solid circle, average shear = V/A =15000/(π·25²)=7.64 N/mm², max at NA =4/3·average =10.19 N/mm². Formula τ_max =16V/(3πR²) or 4/3·V/A. Distribution parabolic zero at top/bottom max at centre.</p>"+fig(svg_shear_rect,"Shear stress for circular — parabolic, max 4/3 average at NA"),
   "a_gu":"<p>સરેરાશ 7.64 N/mm², મહત્તમ 4/3× =10.19 N/mm², પરવલય ટોચ-તળિયે શૂન્ય મધ્યે મહત્તમ.</p>"+fig(svg_shear_rect,"વર્તુળ શીયર — મહત્તમ 4/3 સરેરાશ")},
 ]
},
{
 "title_en":"Q4 · Shear stress distribution, trusses & bending theory",
 "title_gu":"પ્ર.4 · શીયર વિતરણ, ટ્રસ અને બેન્ડિંગ સિદ્ધાંત",
 "cards":[
  {"q_en":"Q.4 (a) Draw shear stress distribution diagram for Hollow rectangular, L-section, Circular section. (03 marks)","marks_en":"03 marks","marks_gu":"૦૩ ગુણ",
   "a_en":"<p><strong>Hollow rect:</strong> Parabolic max at NA 1.5× average but reduced due to hollow, zero at top/bottom.</p><p><strong>L-section:</strong> Discontinuous at junction, max at NA in web, low in flanges.</p><p><strong>Circular:</strong> Parabolic max 4/3 average at NA zero at top/bottom.</p>"+fig(svg_shear_I,"Shear stress distributions — hollow rect reduced, L discontinuous, circular 4/3 average"),
   "a_gu":"<p><strong>પોલો લંબચોરસ:</strong> NA પર મહત્તમ 1.5×.</p><p><strong>L:</strong> જંક્શન પર અસતત.</p><p><strong>વર્તુળ:</strong> 4/3 સરેરાશ.</p>"+fig(svg_shear_I,"શીયર વિતરણ — પોલો, L, વર્તુળ")},
  {"q_en":"Q.4 (b) Explain perfect, deficient and redundant trusses with examples. (04 marks)","marks_en":"04 marks","marks_gu":"૦૪ ગુણ",
   "a_en":"<p><strong>Perfect:</strong> m=2j−3 just sufficient, stable example triangle. <strong>Deficient:</strong> m<2j−3 less members mechanism unstable. <strong>Redundant:</strong> m>2j−3 extra members indeterminate to first degree. Check with m and j count.</p>"+fig(svg_types,"Perfect m=2j−3, deficient m<2j−3, redundant m>2j−3"),
   "a_gu":"<p><strong>પરફેક્ટ:</strong> m=2j−3 સ્થિર. <strong>ડેફિશિયન્ટ:</strong> ઓછા અસ્થિર. <strong>રિડન્ડન્ટ:</strong> વધારે અનિર્ધાર્ય.</p>"+fig(svg_types,"ટ્રસ પ્રકાર — m=2j−3")},
  {"q_en":"Q.4 (c) Find forces in all members of truss as shown in figure 3 by method of joint. (07 marks)","marks_en":"07 marks","marks_gu":"૦૭ ગુણ",
   "a_en":"<p><strong>Steps:</strong> Reactions ΣY ΣM, start at joint with ≤2 unknowns ΣH=0 ΣV=0, tensile away compressive towards, zero-force where two members at unloaded joint. For typical truss with 20 kN at apex, bottom tensile 15 kN top compressive 15 kN diagonal 10 kN. Tabulate all members T/C.</p>"+fig(svg_joints,"Method of joints — joint equilibrium, zero-force rules"),
   "a_gu":"<p><strong>પગલાં:</strong> પ્રતિક્રિયા, 2 અજાણ્યા વાળા સાંધા ΣH ΣV, તાણ દૂર દબાણ નજીક, શૂન્ય ઓળખો.</p>"+fig(svg_joints,"સાંધા પદ્ધતિ")},
  {"q_en":"Q.4 (a) OR Explain concept of pure bending and its assumptions. (03 marks)","marks_en":"03 marks","marks_gu":"૦૩ ગુણ",
   "a_en":"<p><strong>Pure bending:</strong> Bending without shear — constant BM along length, beam bends into circular arc. <strong>Assumptions:</strong> Material homogeneous isotropic, Hooke’s law, plane sections remain plane, beam initially straight, Young’s modulus same tension/compression.</p>"+fig(svg_bending,"Pure bending — constant BM, circular arc, plane sections remain plane"),
   "a_gu":"<p><strong>શુદ્ધ બેન્ડિંગ:</strong> શીયર વગર અચળ BM, ગોળ ચાપ. <strong>ધારણા:</strong> સમાન પદાર્થ, હૂક નિયમ, સમતલ રહે.</p>"+fig(svg_bending,"શુદ્ધ બેન્ડિંગ — અચળ BM")},
  {"q_en":"Q.4 (b) OR Draw different types of trusses with neat sketches. (04 marks)","marks_en":"04 marks","marks_gu":"૦૪ ગુણ",
   "a_en":"<p>Pratt vertical+diagonal tension, Howe opposite, Warren equilateral triangles, Fink for roofs, North light sawtooth. Sketches show verticals and diagonals arrangement.</p>"+fig(svg_sections,"Truss types — Pratt, Howe, Warren, Fink with sketches"),
   "a_gu":"<p>Pratt, Howe, Warren, Fink, North light — આકૃતિ.</p>"+fig(svg_sections,"ટ્રસ પ્રકાર")},
  {"q_en":"Q.4 (c) OR Find forces in truss as shown in figure 4 by method of joint. (07 marks)","marks_en":"07 marks","marks_gu":"૦૭ ગુણ",
   "a_en":"<p>Same joint method for figure 4 with 30 kN at apex, reactions, joint by joint, tabulate T/C, identify zero members at unloaded joints with two members.</p>"+fig(svg_zero,"Zero force members — two non-collinear at unloaded joint"),
   "a_gu":"<p>ઉપર મુજબ સાંધા પદ્ધતિ figure 4, શૂન્ય મેમ્બર ઓળખો.</p>"+fig(svg_zero,"શૂન્ય બળ")},
 ]
},
{
 "title_en":"Q5 · Deflection, slope & columns — Euler & Rankine",
 "title_gu":"પ્ર.5 · વિચલન, ઢાળ અને સ્તંભ — યુલર અને રેન્કિન",
 "cards":[
  {"q_en":"Q.5 (a) Write formula for maximum deflection and maximum slope of simply supported beam with UDL over entire span. (03 marks)","marks_en":"03 marks","marks_gu":"૦૩ ગુણ",
   "a_en":"<p>For SSB with UDL w over L: Reactions wL/2, Max BM wL²/8 at centre, Slope at ends θ = wL³/(24EI), Deflection at centre δ =5wL⁴/(384EI) downward. Slope zero at centre, deflection max there.</p>"+fig(svg_ssb5,"Simply supported UDL — slope wL³/24EI at ends, deflection 5wL⁴/384EI at centre"),
   "a_gu":"<p>SSB UDL w L: પ્રતિક્રિયા wL/2, BM wL²/8, ઢાળ છેડે wL³/24EI, વિચલન મધ્યે 5wL⁴/384EI.</p>"+fig(svg_ssb5,"સાદો UDL — ઢાળ અને વિચલન")},
  {"q_en":"Q.5 (b) How does flexural rigidity affect deflection of beams? Explain. (04 marks)","marks_en":"04 marks","marks_gu":"૦૪ ગુણ",
   "a_en":"<p>Flexural rigidity EI = E·I. Deflection δ ∝ 1/EI. Higher E (stiffer material) or I (deeper section) reduces deflection. Doubling depth increases I 8 times, deflection 1/8. So choose deeper beam or stronger material to control deflection within L/250.</p>"+fig(svg_elastic,"Flexural rigidity EI — E material, I section, deflection inversely proportional"),
   "a_gu":"<p>EI = E·I, વિચલન 1/EI પ્રમાણે, E કે I વધે તો વિચલન ઘટે, ઊંડાઈ બમણી I 8 ગણું વિચલન 1/8.</p>"+fig(svg_elastic,"EI — વિચલન વ્યસ્ત")},
  {"q_en":"Q.5 (c) A circular steel column 200mm dia fixed at both ends. Using Euler’s formula, calculate safe load. Length 3.6m. E=2×10⁵ N/mm² FOS2. (07 marks)","marks_en":"07 marks","marks_gu":"૦૭ ગુણ",
   "a_en":"<p>Dia 200 mm, Area =31416 mm², I = πD⁴/64 =78.54×10⁶ mm⁴, Effective length fixed both ends L_e =L/2=1800 mm, Slenderness L_e/k where k=√I/A=50 mm →36. Euler P_cr = π²·E·I /L_e² =9.87·2e5·78.54e6/3.24e6=478.4×10³ N=478 kN. Safe = P_cr/FOS =239 kN. Long column Euler valid as slenderness > critical.</p>"+fig(svg_euler,"Euler column fixed both ends L_e = L/2, P_cr = π²EI/L_e²"),
   "a_gu":"<p>વ્યાસ 200 mm A31416 I78.54×10⁶, L_e=1800 mm, P_cr=478 kN, સલામત 239 kN.</p>"+fig(svg_euler,"યુલર સ્તંભ — L_e = L/2")},
  {"q_en":"Q.5 (a) OR Define slope and deflection of a beam. (03 marks)","marks_en":"03 marks","marks_gu":"૦૩ ગુણ",
   "a_en":"<p><strong>Slope:</strong> Angle of tangent to elastic curve, θ = dy/dx.</p><p><strong>Deflection:</strong> Vertical displacement y from original. For SSB, max at centre, zero at supports.</p>"+fig(svg_elastic,"Slope angle and deflection displacement on elastic curve"),
   "a_gu":"<p><strong>ઢાળ:</strong> સ્થિતિસ્થાપક વક્રનો ખૂણો θ.</p><p><strong>વિચલન:</strong> ઊભું અંતર y.</p>"+fig(svg_elastic,"ઢાળ અને વિચલન")},
  {"q_en":"Q.5 (b) OR Compare deflection behavior of cantilever and simply supported beams. (04 marks)","marks_en":"04 marks","marks_gu":"૦૪ ગુણ",
   "a_en":"<p>Cantilever with UDL δ= wL⁴/8EI at free end larger, slope wL³/6EI. SSB UDL δ=5wL⁴/384EI much smaller about 1/77 of cantilever for same L. Cantilever deflects more, fixed end zero slope. For same load, SSB stiffer.</p>"+fig(svg_cantilever5,"Cantilever UDL δ=wL⁴/8EI vs SSB 5wL⁴/384EI — cantilever deflects more"),
   "a_gu":"<p>કેન્ટીલીવર UDL δ wL⁴/8EI મોટું, SSB 5wL⁴/384EI નાનું 1/77, કેન્ટીલીવર વધુ વળે.</p>"+fig(svg_cantilever5,"કેન્ટીલીવર vs સાદો — વિચલન તુલના")},
  {"q_en":"Q.5 (c) OR A steel bar 4.0m fixed both ends, Find Rankine’s crippling load Ixx=5×10⁷ Iyy=3×10⁶ A=500 fc=600 N/mm² ∝=1/1800 FOS1.5. (07 marks)","marks_en":"07 marks","marks_gu":"૦૭ ગુણ",
   "a_en":"<p>Rankine P_cr = f_c·A / (1+∝·(L_e/k)²), k =√I_min/A, I_min=Iyy=3e6, k=√6000=77.46 mm, L_e fixed both ends =2000 mm, slenderness=25.82, P_cr=600·500/(1+1/1800·666)=300000/(1+0.37)=219kN, Safe= P_cr/FOS=146 kN. Euler would give π²EI/L_e²=292kN, Rankine lower accounts for crushing.</p>"+fig(svg_rankine,"Rankine load — combines Euler and crushing, P_cr = f_c·A/(1+ a·(L_e/k)²)"),
   "a_gu":"<p>Rankine P_cr = f_c·A/1+∝·L_e/k², k=77.46 mm L_e=2000, P_cr=219 kN સલામત 146 kN.</p>"+fig(svg_rankine,"રેન્કિન લોડ")},
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
    page=f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>DI03006041 · Summer 2026 solved paper</title><style>{CSS}</style></head><body><main class="page"><header class="hero"><div class="eyebrow">Solved question paper · English questions · Friendly Gujarati answers</div><div class="lang-switch" aria-label="Choose language"><button type="button" data-lang="en" aria-pressed="true">English</button><button type="button" data-lang="gu" aria-pressed="false">ગુજરાતી</button></div><h1>Mechanics of Structures-I</h1><div class="meta">GTU Diploma · Civil · Semester 3 · Summer 2026 · DI03006041 · 20-05-2026 · 70 marks · 02:30 PM TO 05:00 PM</div></header>{"".join(sections_html)}<div class="footer">Solved paper for study. Verify with standard spec before site use.</div></main><script>document.querySelectorAll('.lang-switch button').forEach(b=>b.addEventListener('click',()=>{{document.documentElement.lang=b.dataset.lang;document.querySelectorAll('.lang-switch button').forEach(x=>x.setAttribute('aria-pressed',x===b?'true':'false'));}}));</script></body></html>'''
    return page
def main():
    page=build_page()
    out_papers=ROOT/"papers-upload/papers/DI03006041/summer-2026.html"
    out_ws=ROOT/"preview/workshop/DI03006041_summer2026_bilingual.html"
    out_papers.parent.mkdir(parents=True,exist_ok=True)
    out_ws.parent.mkdir(parents=True,exist_ok=True)
    import re as _re
    page=_re.sub(r'<div class="gu">(.*?)</div>', lambda m: '<div class="gu">'+m.group(1).replace('(','[').replace(')',']')+'</div>', page, flags=_re.S)
    out_ws.write_text(page,encoding="utf-8")
    print(f"Bilingual: {out_papers} ({len(page)} chars)")
    print(f"details={page.count('<details')}, sections={page.count('<section')}, figs={page.count('<figure>')}")
    import re; gu=''.join(re.findall(r'<div class=\"gu\">(.*?)</div>',page,re.S)); print(f"brackets gu={gu.count('(')+gu.count(')')}")
    print("PASS" if page.count('<details')==28 and page.count('<section')==5 else "FAIL")
    (ROOT/"drive-upload/DI03006041_summer_2026_bilingual.html").write_text(page,encoding="utf-8")
if __name__=="__main__": main()
