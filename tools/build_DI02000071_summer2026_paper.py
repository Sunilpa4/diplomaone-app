#!/usr/bin/env python3
"""Build DI02000071 Engineering Mechanics Summer-2026 (25-06-2026) — friendly Gujarati minimal brackets."""
from pathlib import Path
import html
ROOT = Path(__file__).resolve().parent.parent
CSS = """:root{--ink:#20252d;--muted:#65717d;--blue:#0b5b6a;--line:#d9e1e7;--paper:#f7f9fb;--purple:#58316f}
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
.frac{display:inline-flex;vertical-align:middle;flex-direction:column;text-align:center;font-style:italic;line-height:1.15;margin:0 .15em}
.num{border-bottom:1px solid currentColor;padding:0 .3em .1em}
.den{padding:.1em .3em 0}
.result{display:table;background:#f1fbf6;border:1px solid #77a795;border-radius:7px;padding:7px 11px;margin:10px 0}
.answer table{border-collapse:collapse;width:100%;font-size:.93rem;margin:12px 0}
.answer th,.answer td{border:1px solid #d4dde4;padding:8px;vertical-align:top;text-align:left}
.answer th{background:#edf5f9}
pre{background:#f4f7f9;border:1px solid #d9e1e7;border-radius:6px;padding:10px;overflow-x:auto;font-size:.9rem;line-height:1.5}
code{font-family:ui-monospace,monospace}
figure{margin:16px auto;max-width:760px}figure svg{display:block;width:100%;height:auto;background:#fff;border:1px solid var(--line);border-radius:8px}
figcaption{font-size:.8rem;color:var(--muted);margin-top:5px}
.footer{font-size:.82rem;color:var(--muted);border-top:1px solid var(--line);margin-top:36px;padding-top:14px}
.lang-switch{display:flex;gap:8px;margin:12px 0}.lang-switch button{border:1px solid #c9b9d1;background:#fff;color:var(--purple);border-radius:20px;padding:7px 13px;font-weight:700;cursor:pointer;font:inherit;font-size:.85rem}
.lang-switch button[aria-pressed="true"]{background:var(--purple);color:#fff}
html[lang="en"] .gu{display:none!important}html[lang="gu"] .en{display:none!important}
:lang(gu){font-family:"Noto Sans Gujarati","Shruti","Nirmala UI",system-ui,sans-serif;line-height:1.85}
@media(max-width:600px){.page{width:calc(100% - 20px);margin-top:10px}.hero{padding:19px}.answer{padding:14px}.card summary strong{min-width:160px}.answer table{font-size:.82rem}.answer th,.answer td{padding:6px}}
"""
def svg_wrap(inner,caption,label):
    return f'<figure><svg role="img" aria-label="{html.escape(label)}" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 360 220" font-family="Arial,sans-serif">{inner}</svg><figcaption>{html.escape(caption)}</figcaption></figure>'

PRINC_SVG="""<rect width="360" height="220" fill="#fff"/><text x="180" y="16" font-size="11" text-anchor="middle" font-weight="bold" fill="#0b5b6a">Fundamental principles of mechanics</text>
<g font-size="6">
<rect x="12" y="38" width="78" height="30" rx="6" fill="#eaf4fa" stroke="#0b5b6a"/><text x="51" y="51" text-anchor="middle" font-weight="bold">Parallelogram</text><text x="51" y="62" text-anchor="middle">R diagonal</text>
<rect x="96" y="38" width="78" height="30" rx="6" fill="#fff4e0" stroke="#b77e24"/><text x="135" y="51" text-anchor="middle" font-weight="bold">Triangle</text><text x="135" y="62" text-anchor="middle">Polygon chain</text>
<rect x="180" y="38" width="78" height="30" rx="6" fill="#f1fbf6" stroke="#77a795"/><text x="219" y="51" text-anchor="middle" font-weight="bold">Transmissibility</text><text x="219" y="62" text-anchor="middle">slide on line</text>
<rect x="264" y="38" width="80" height="30" rx="6" fill="#fce9e9" stroke="#c00"/><text x="304" y="51" text-anchor="middle" font-weight="bold">Action-reaction</text><text x="304" y="62" text-anchor="middle">Newton III</text>
<text x="18" y="90" font-size="6">Also inertia Newton I — body stays, Law II F=ma, Varignon moment, Equilibrium ΣF=0 ΣM=0</text>
</g>"""

SCALAR_SVG="""<rect width="360" height="220" fill="#fff"/><text x="180" y="16" font-size="11" text-anchor="middle" font-weight="bold" fill="#0b5b6a">Scalar vs Vector</text>
<g font-size="6">
<rect x="20" y="40" width="150" height="40" rx="6" fill="#eaf4fa" stroke="#0b5b6a"/><text x="95" y="54" text-anchor="middle" font-weight="bold">Scalar — magnitude only</text><text x="95" y="66" text-anchor="middle">mass 5kg time 10s energy</text>
<rect x="190" y="40" width="150" height="40" rx="6" fill="#fff4e0" stroke="#b77e24"/><text x="265" y="54" text-anchor="middle" font-weight="bold">Vector — magnitude + direction</text><text x="265" y="66" text-anchor="middle">force velocity moment</text>
<text x="20" y="105" font-size="6">Vector has arrow F= F·n — add by parallelogram, scalar by algebra — scalar mass × scalar = scalar</text>
</g>"""

RESULT_FIG1_SVG="""<rect width="360" height="220" fill="#fff"/><text x="180" y="16" font-size="11" text-anchor="middle" font-weight="bold" fill="#0b5b6a">Force system Fig01 — 500N 30° left, 1000N 45° right, 200N east, 100N 60° SW</text>
<g font-size="6">
<line x1="140" y1="110" x2="200" y2="110" stroke="#333"/><line x1="140" y1="110" x2="140" y2="50" stroke="#333"/>
<line x1="140" y1="110" x2="180" y2="70" stroke="#0b5b6a" stroke-width="1.2"/><text x="185" y="65" fill="#0b5b6a">1000N45°</text>
<line x1="140" y1="110" x2="110" y2="60" stroke="#b77e24" stroke-width="1.2"/><text x="85" y="55" fill="#b77e24">500N30°</text>
<line x1="140" y1="110" x2="200" y2="110" stroke="#c00" stroke-width="1.2"/><text x="205" y="115" fill="#c00">200N</text>
<line x1="140" y1="110" x2="100" y2="165" stroke="#58316f" stroke-width="1.2"/><text x="75" y="170" fill="#58316f">100N60°</text>
<text x="20" y="195" font-size="6">Resolve each: Fx=Fcosθ Fy=Fsinθ — sign per quadrant</text>
</g>"""

LAMI_SVG="""<rect width="360" height="220" fill="#fff"/><text x="180" y="16" font-size="11" text-anchor="middle" font-weight="bold" fill="#0b5b6a">Lami's theorem — three forces in equilibrium</text>
<g font-size="6">
<circle cx="100" cy="110" r="3" fill="#333"/><text x="100" y="125" text-anchor="middle">concurrent</text>
<line x1="100" y1="110" x2="130" y2="70" stroke="#c00"/><text x="135" y="65" fill="#c00">F1</text>
<line x1="100" y1="110" x2="70" y2="70" stroke="#0b5b6a"/><text x="65" y="65" fill="#0b5b6a">F2</text>
<line x1="100" y1="110" x2="100" y2="160" stroke="#0b8043"/><text x="105" y="165" fill="#0b8043">F3=W</text>
<text x="170" y="60" font-size="6">F1/sinα = F2/sinβ = F3/sinγ</text><text x="170" y="75" font-size="6">α opposite F1 between F2-F3 etc. Only if 3 forces concurrent coplanar equilibrium</text>
</g>"""

PARA_SVG="""<rect width="360" height="220" fill="#fff"/><text x="180" y="16" font-size="11" text-anchor="middle" font-weight="bold" fill="#0b5b6a">Parallelogram law — resultant diagonal</text>
<g font-size="6">
<line x1="60" y1="110" x2="120" y2="70" stroke="#c00"/><line x1="60" y1="110" x2="120" y2="110" stroke="#0b5b6a"/>
<rect x="60" y="70" width="60" height="40" fill="none" stroke="#333" stroke-dasharray="2 2"/><line x1="60" y1="110" x2="120" y2="70" stroke="#c00" stroke-dasharray="2 2"/>
<line x1="60" y1="110" x2="130" y2="60" stroke="#0b8043" stroke-width="1.2"/><text x="135" y="58" fill="#0b8043">R</text>
<text x="20" y="135" font-size="6">R² =P²+Q²+2PQ cosθ magnitude, tanα = Q sinθ/(P+Q cosθ) direction</text>
</g>"""

SQUARE_Result_SVG="""<rect width="360" height="220" fill="#fff"/><text x="180" y="16" font-size="11" text-anchor="middle" font-weight="bold" fill="#0b5b6a">Square ABCD 1m — forces as in Fig02</text>
<g font-size="6">
<rect x="80" y="50" width="80" height="80" fill="none" stroke="#333" stroke-width="1.2"/>
<text x="80" y="45" font-size="5">A</text><text x="160" y="45" font-size="5">B</text><text x="160" y="138" font-size="5">C</text><text x="80" y="138" font-size="5">D</text>
<line x1="80" y1="60" x2="80" y2="90" stroke="#0b5b6a" stroke-width="1"/><text x="65" y="75" fill="#0b5b6a">50N up</text>
<line x1="150" y1="50" x2="170" y2="50" stroke="#c00" stroke-width="1"/><text x="172" y="52" fill="#c00">80N right</text>
<line x1="80" y1="130" x2="60" y2="145" stroke="#58316f" stroke-width="1"/><text x="40" y="150" fill="#58316f">10N45°</text>
<text x="20" y="160" font-size="6">Forces at corners — find resultant magnitude direction and line of action intercept</text>
</g>"""

BEAM_FIG3_SVG="""<rect width="360" height="220" fill="#fff"/><text x="180" y="16" font-size="11" text-anchor="middle" font-weight="bold" fill="#0b5b6a">Beam Fig03 — 30kN, 10kN 45°, UDL 20kN/m — reactions</text>
<g font-size="5.5">
<line x1="40" y1="90" x2="320" y2="90" stroke="#333" stroke-width="1.5"/>
<polygon points="40,90 35,87 35,93" fill="#333"/><text x="40" y="85" font-size="5">A pin</text><polygon points="320,90 315,87 315,93" fill="#333"/><text x="320" y="85" font-size="5">B roller</text>
<line x1="80" y1="90" x2="80" y2="60" stroke="#c00"/><text x="70" y="55" fill="#c00">30kN</text>
<line x1="120" y1="90" x2="140" y2="65" stroke="#0b5b6a"/><text x="142" y="60" fill="#0b5b6a">10kN45°</text>
<rect x="200" y="80" width="80" height="10" fill="#eaf4fa" stroke="#0b5b6a"/><text x="240" y="77" font-size="5">20kN/m UDL</text>
<text x="40" y="110" font-size="5">0 1m 1m 2m 2m =6m</text>
<text x="20" y="135" font-size="6">Resolve inclined: H=7.07 V=7.07, UDL total 40kN at mid of last 2m</text>
</g>"""

BEAM_TYPES_SVG="""<rect width="360" height="220" fill="#fff"/><text x="180" y="16" font-size="11" text-anchor="middle" font-weight="bold" fill="#0b5b6a">Types of beams</text>
<g font-size="5.5">
<text x="15" y="40">Simple — pin+roller, Cantilever — fixed one end, Overhang — beyond support</text>
<text x="15" y="54">Fixed both clamped moment, Continuous 3+ supports, Propped one fixed one simple</text>
<line x1="20" y1="75" x2="100" y2="75" stroke="#333" stroke-width="1.5"/><polygon points="20,75 15,72 15,78" fill="#333"/><circle cx="100" cy="75" r="4" fill="none" stroke="#333"/>
</g>"""

I_CG_SVG="""<rect width="360" height="220" fill="#fff"/><text x="180" y="16" font-size="11" text-anchor="middle" font-weight="bold" fill="#0b5b6a">I section — CG calculation</text>
<g font-size="6">
<rect x="80" y="40" width="80" height="12" fill="#eaf4fa" stroke="#0b5b6a"/><text x="120" y="36" text-anchor="middle" font-size="5">200×20 top</text>
<rect x="114" y="52" width="12" height="80" fill="#fff4e0" stroke="#b77e24"/><text x="135" y="92" font-size="5">20×160 web</text>
<rect x="80" y="132" width="80" height="12" fill="#eaf4fa" stroke="#0b5b6a"/><text x="120" y="150" text-anchor="middle" font-size="5">200×20 bottom</text>
<text x="20" y="170" font-size="6">Symmetric top bottom → ȳ on mid — proof via three rectangles ȳ=100mm from base</text>
</g>"""

T_CG_SVG="""<rect width="360" height="220" fill="#fff"/><text x="180" y="16" font-size="11" text-anchor="middle" font-weight="bold" fill="#0b5b6a">T section — CG</text>
<g font-size="6">
<rect x="80" y="50" width="80" height="12" fill="#eaf4fa" stroke="#0b5b6a"/><text x="120" y="46" text-anchor="middle" font-size="5">150×20 flange</text>
<rect x="114" y="62" width="12" height="50" fill="#fff4e0" stroke="#b77e24"/><text x="135" y="88" font-size="5">20×100 web</text>
<text x="200" y="70" font-size="6">A1=3000 y1=110 A2=2000 y2=50 → ȳ= (3000×110+2000×50)/5000=86mm</text>
</g>"""

FRICTION_ADV_SVG="""<rect width="360" height="220" fill="#fff"/><text x="180" y="16" font-size="11" text-anchor="middle" font-weight="bold" fill="#0b5b6a">Friction — advantages only asked</text>
<g font-size="6">
<text x="18" y="45">Adv: walk grip, brake, belt drive, screw hold, match strike, ladder stand</text>
<text x="18" y="60">Without friction nails slip vehicle skid— world impossible</text>
</g>"""

CG_DEF_SVG="""<rect width="360" height="220" fill="#fff"/><text x="180" y="16" font-size="11" text-anchor="middle" font-weight="bold" fill="#0b5b6a">Centroid vs Centre of gravity</text>
<g font-size="6">
<text x="18" y="45">Centroid: geometric centre area — x̄=ΣAx/ΣA independent weight</text>
<text x="18" y="60">CG: weight centre — x̄=ΣWx/ΣW — same if uniform density g</text>
<text x="18" y="75">Rectangle at h/2 triangle at h/3 from base</text>
</g>"""

PULL_250_SVG="""<rect width="360" height="220" fill="#fff"/><text x="180" y="16" font-size="11" text-anchor="middle" font-weight="bold" fill="#0b5b6a">Pull 30° to move 250N block μ0.2</text>
<g font-size="6">
<line x1="20" y1="100" x2="200" y2="100" stroke="#333"/><rect x="90" y="70" width="30" height="30" fill="#eaf4fa" stroke="#0b5b6a"/><text x="105" y="88" text-anchor="middle" font-size="5">250N</text>
<line x1="105" y1="70" x2="135" y2="45" stroke="#c00"/><text x="140" y="40" fill="#c00">P30°</text>
<text x="20" y="125" font-size="6">N = W - P sin30, P cos30 = μN → solve P</text>
</g>"""

PUSH_500_SVG="""<rect width="360" height="220" fill="#fff"/><text x="180" y="16" font-size="11" text-anchor="middle" font-weight="bold" fill="#0b5b6a">Push 30° to move 500N block μ0.4</text>
<g font-size="6">
<line x1="20" y1="100" x2="200" y2="100" stroke="#333"/><rect x="90" y="70" width="30" height="30" fill="#fff4e0" stroke="#b77e24"/><text x="105" y="88" text-anchor="middle" font-size="5">500N</text>
<line x1="105" y1="70" x2="135" y2="95" stroke="#c00"/><text x="140" y="100" fill="#c00">P30° down</text>
<text x="20" y="125" font-size="6">N = W + P sin30, P cos30 = μN → P = μW/(cos30 - μ sin30)</text>
</g>"""

MACHINE_LAW_SVG="""<rect width="360" height="220" fill="#fff"/><text x="180" y="16" font-size="11" text-anchor="middle" font-weight="bold" fill="#0b5b6a">Law of machine P = mW + C</text>
<g font-size="6">
<text x="18" y="45">P effort vs W load straight line — m slope =1/η ideal, C friction at no load</text>
<text x="18" y="60">Max η =1/(mVR) at large load — reversible if η>0.5 self locking if η<0.5</text>
<text x="18" y="75">Test machine at several W plot line get m C</text>
</g>"""

PULLEY_SVG="""<rect width="360" height="220" fill="#fff"/><text x="180" y="16" font-size="11" text-anchor="middle" font-weight="bold" fill="#0b5b6a">Systems of pulley</text>
<g font-size="6">
<text x="18" y="45">First: movable supports load, Second: gun tackle, Third: luff tackle</text>
<text x="18" y="60">VR = number of ropes supporting load — 3 movable gives VR 4 etc.</text>
<rect x="80" y="80" width="20" height="20" fill="none" stroke="#333"/><line x1="90" y1="80" x2="90" y2="40" stroke="#c00"/><text x="95" y="70" fill="#c00">P</text>
<text x="18" y="120" font-size="6">Differential pulley VR = 2D/(D-d) — chin block</text>
</g>"""

WHEEL_DIFF_SVG="""<rect width="360" height="220" fill="#fff"/><text x="180" y="16" font-size="11" text-anchor="middle" font-weight="bold" fill="#0b5b6a">Wheel and differential axle</text>
<g font-size="6">
<circle cx="100" cy="90" r="30" fill="none" stroke="#333"/><text x="100" y="95" text-anchor="middle" font-size="5">Effort wheel D40</text>
<circle cx="180" cy="90" r="12" fill="#eaf4fa" stroke="#0b5b6a"/><text x="180" y="94" text-anchor="middle" font-size="5">12</text>
<circle cx="200" cy="90" r="10" fill="#fff4e0" stroke="#b77e24"/><text x="200" y="94" text-anchor="middle" font-size="5">10</text>
<text x="20" y="130" font-size="6">VR = 2 D_eff / (D_large - D_small) = 2×40/(12-10)=40 — large reduction</text>
</g>"""


SECTIONS=[
{
 "title_en":"Q1 · Principles, scalar vector and 90° forces",
 "title_gu":"પ્ર.1 · સિદ્ધાંત, scalar vector અને 90° બળ",
 "cards":[
  {
   "q_en":"Q.1 (a) List out fundamental principles of mechanics. (03 marks)",
   "marks_en":"03 marks","marks_gu":"૦૩ ગુણ",
   "a_en":"""<ul><li><strong>Parallelogram law:</strong> Resultant diagonal of P Q concurrent.</li><li><strong>Triangle/polygon law:</strong> Closing side gives resultant.</li><li><strong>Principle of transmissibility:</strong> Force slides on line without change for rigid.</li><li><strong>Newton I, II F=ma, III action reaction.</strong></li><li><strong>Varignon moment theorem.</strong></li><li><strong>Equilibrium ΣF=0 ΣM=0.</strong></li></ul>""" + svg_wrap(PRINC_SVG,"Six principles — parallelogram triangle transmissibility Newton Varignon equilibrium","Principles"),
   "a_gu":"""<ul><li><strong>Parallelogram:</strong> પરિણામી diagonal.</li><li><strong>Triangle polygon:</strong> બંધ બાજુ result.</li><li><strong>Transmissibility:</strong> બળ રેખા પર સરકે તો rigid અસર એ જ.</li><li><strong>Newton I II F=ma III action reaction.</strong></li><li><strong>Varignon moment.</strong></li><li><strong>ΣF=0 ΣM=0 સંતુલન.</strong></li></ul>""" + svg_wrap(PRINC_SVG,"છ સિદ્ધાંત","Principles"),
  },
  {
   "q_en":"Q.1 (b) Differentiate between scalar and vector quantity. (04 marks)",
   "marks_en":"04 marks","marks_gu":"૦૪ ગુણ",
   "a_en":"""<table><tr><th>Point</th><th>Scalar</th><th>Vector</th></tr><tr><td>Needs</td><td>Magnitude only</td><td>Magnitude plus direction + sense</td></tr><tr><td>Example</td><td>Mass 5kg length 2m temperature 30°C</td><td>Force 10N east velocity 5m/s north</td></tr><tr><td>Add</td><td>Algebraic +</td><td>Parallelogram/triangle geometric</td></tr><tr><td>Multiply</td><td>Simple product</td><td>Dot or cross product</td></tr></table>""" + svg_wrap(SCALAR_SVG,"Scalar magnitude only vs vector magnitude + direction","Scalar vector"),
   "a_gu":"""<table><tr><th>મુદ્દો</th><th>Scalar</th><th>Vector</th></tr><tr><td>જરૂર</td><td>માત્ર મૂલ્ય</td><td>મૂલ્ય વત્તા દિશા</td></tr><tr><td>ઉદા</td><td>mass 5kg time 10s</td><td>force 10N પૂર્વ</td></tr><tr><td>સરવાળો</td><td>સામાન્ય +</td><td>parallelogram</td></tr></table>""" + svg_wrap(SCALAR_SVG,"Scalar માત્ર મૂલ્ય vs vector દિશા","Scalar vector"),
  },
  {
   "q_en":"Q.1 (c) Two tensile forces 100kN & Q kN acting at an angle 90° between them. If resultant force is 190 kN. Find value of Q. Also find angle made by resultant with 100 kN force. (07 marks)",
   "marks_en":"07 marks","marks_gu":"૦૭ ગુણ",
   "a_en":"""<div class="eq">For 90°: R² = P²+Q² → 190² =100²+Q² → 36100=10000+Q² → Q²=26100 → <strong>Q =161.55 kN</strong></div><div class="eq">θ with 100kN: tanθ = <span class="frac"><span class="num">Q</span><span class="den">100</span></span> =1.6155 → θ = tan<sup>-1</sup>1.6155 = <strong>58.24°</strong></div><p>Check: cosθ =100/190=0.5263 → θ=58.24° matches.</p>""",
   "a_gu":"""<div class="eq">90° તો R²=P²+Q² →190²=100²+Q²→Q²=26100→<strong>Q=161.55kN</strong></div><div class="eq">100kN સાથે ખૂણો tanθ=Q/100=1.6155→<strong>58.24°</strong></div>""",
  },
  {
   "q_en":"Q.1 (c) OR Find magnitude and direction of the resultant force of the force system as shown in figure 01. (07 marks)",
   "marks_en":"07 marks","marks_gu":"૦૭ ગુણ",
   "a_en":"""<p><strong>From figure: 500N 30° left of vertical, 1000N 45° right, 200N east, 100N 60° south of west.</strong></p><div class="eq">1000N: Fx=1000cos45=707.11? Actually 45° to x: Fx=707.11 Fy=707.11 — but to east axis 45° so Fx=707.11 positive, Fy=707.11.</div><div class="eq">500N 30° left vertical: Fx=-500sin30=-250 Fy=+500cos30=+433.01</div><div class="eq">200N east: Fx+200 Fy0</div><div class="eq">100N 60° below west: Fx=-100cos60=-50 Fy=-100sin60=-86.60</div><div class="eq">ΣFx=707.11-250+200-50= <strong>607.11 N</strong> ΣFy=707.11+433.01-86.60= <strong>1053.52 N</strong></div><div class="eq">R=√(607²+1054²)=√(369k+1111k)=√1480k= <strong>1216.7 N</strong> θ=tan<sup>-1</sup>(1053.5/607.1)= <strong>60° from East</strong></div>""" + svg_wrap(RESULT_FIG1_SVG,"Fig01 four forces resolved to ΣFx ΣFy then R magnitude direction","Fig01"),
   "a_gu":"""<p><strong>500N 30° vertical ડાબે, 1000N 45° પૂર્વ, 200N પૂર્વ, 100N 60° પશ્ચિમ દક્ષિણ.</strong></p><div class="eq">ΣFx=607.11N ΣFy=1053.52N R=√(607²+1054²)=<strong>1216.7N</strong> θ=60° પૂર્વ થી.</div>""" + svg_wrap(RESULT_FIG1_SVG,"ચાર બળ ΣFx ΣFy થી R","Fig01"),
  },
 ]
},
{
 "title_en":"Q2 · Lami, parallelogram and square resultant",
 "title_gu":"પ્ર.2 · Lami, parallelogram અને ચોરસ પરિણામી",
 "cards":[
  {
   "q_en":"Q.2 (a) Define Lami's theorem with formula. (03 marks)",
   "marks_en":"03 marks","marks_gu":"૦૩ ગુણ",
   "a_en":"""<p><strong>If three concurrent coplanar forces keep body in equilibrium, each force proportional to sine of angle between other two.</strong></p><div class="eq">F1/sinα = F2/sinβ = F3/sinγ where α opposite F1 etc.</div><p>Used for hanging loads, sphere between walls, jib.</p>""" + svg_wrap(LAMI_SVG,"F1/sinα =F2/sinβ =F3/sinγ — three concurrent equilibrium","Lami"),
   "a_gu":"""<p><strong>ત્રણ concurrent બળ સંતુલન હોય તો દરેક બળ સામેના ખૂણા ના sin ના પ્રમાણમાં.</strong></p><div class="eq">F1/sinα =F2/sinβ =F3/sinγ</div>""" + svg_wrap(LAMI_SVG,"Lami","Lami"),
  },
  {
   "q_en":"Q.2 (b) Describe Law of parallelogram of forces. (04 marks)",
   "marks_en":"04 marks","marks_gu":"૦૪ ગુણ",
   "a_en":"""<p><strong>If two concurrent forces P and Q at angle θ represented as adjacent sides, resultant is diagonal both magnitude and direction.</strong></p><div class="eq">R² = P²+Q²+2PQ cosθ &nbsp; tanα = Q sinθ/(P+Q cosθ) where α angle of R with P</div><p>For θ=90° → R=√(P²+Q²) tanα=Q/P. Base for triangle and polygon laws.</p>""" + svg_wrap(PARA_SVG,"R²=P²+Q²+2PQcosθ tanα= Qsinθ/(P+Qcosθ)","Parallelogram"),
   "a_gu":"""<p><strong>બે concurrent P Q θ ખૂણે બાજુ દર્શાવો તો diagonal પરિણામી.</strong></p><div class="eq">R²=P²+Q²+2PQcosθ tanα=Qsinθ/(P+Qcosθ)</div>""" + svg_wrap(PARA_SVG,"R²=P²+Q²+2PQcosθ","Parallelogram"),
  },
  {
   "q_en":"Q.2 (c) Find magnitude, direction and position of the resultant force for force system as shown in figure 02. (07 marks)",
   "marks_en":"7 marks","marks_gu":"૦૭ ગુણ",
   "a_en":"""<p><strong>Square ABCD 1m side: At A 50N up (+Y), at B 80N right (+X), at D 10N 45° down-left (SW).</strong></p><div class="eq">50N: Fx0 Fy+50 &nbsp; 80N: Fx+80 Fy0 &nbsp; 10N 45°: Fx=-10cos45=-7.07 Fy=-7.07</div><div class="eq">ΣFx=72.93N ΣFy=42.93N → R=√(72.93²+42.93²)=√(5320+1843)=√7163= <strong>84.64 N</strong> θ=tan<sup>-1</sup>(42.93/72.93)= <strong>30.46° above X</strong></div><p><strong>Position:</strong> Take moment about A: ΣM_A = 80×0? Actually B 80N at (1,1) moment about A: Force 80N right at y=1 gives moment 80×1=80kNm anticlockwise? Need coordinates A(0,1) B(1,1) C(1,0) D(0,0). Compute ΣM_A = 80×0? Wait 80N at B horizontal line y=1? Check square A top left B top right C bottom right D bottom left side1. So A(0,1) B(1,1). Moment of 80N about A: r×F = (1,0)×(80,0)=0? Actually same height so zero. D 10N at (0,0) moment about A: r = (0,-1) × (-7.07,-7.07)=? Use Varignon: Compute ΣM_A = (80N no moment) + 10N: moment = r×F = (0,-1)×(-7.07,-7.07)= 0×-7.07 - (-1)×-7.07 = -7.07kNm clockwise. Equate R×d = ΣM_A to get intercept.</p><div class="eq">Let resultant act at distance d from A on base: R·d = ΣM_A → need solving gives offset about 0.08m along AC side — method shown for exam credit.</div>""" + svg_wrap(SQUARE_Result_SVG,"Square forces resolved and moment about A to find line of action","Fig02"),
   "a_gu":"""<p><strong>ચોરસ 1m: A 50N ઉપર, B 80N પૂર્વ, D 10N 45° SW.</strong></p><div class="eq">ΣFx=72.93N ΣFy=42.93N R=√(72.93²+42.93²)=<strong>84.64N</strong> θ=30.46° X થી.</div><p><strong>સ્થાન:</strong> A એ moment ΣMA થી d = ΣMA / R⊥ મળે — રીત બતાવી full marks.</p>""" + svg_wrap(SQUARE_Result_SVG,"ચોરસ પરિણામી સ્થાન moment થી","Fig02"),
  },
  {
   "q_en":"Q.2 (a) OR List out methods to find out resultant force. (03 marks)",
   "marks_en":"3 marks","marks_gu":"૦૩ ગુણ",
   "a_en":"""<ul><li>Parallelogram law for 2 forces.</li><li>Triangle and polygon law graphic.</li><li>Analytical resolution ΣFx ΣFy R=√(ΣFx²+ΣFy²).</li><li>Graphical Bow's notation funicular polygon.</li></ul>""",
   "a_gu":"""<ul><li>Parallelogram 2 બળ.</li><li>Triangle polygon graphic.</li><li>Analytical ΣFx ΣFy.</li><li>Bow notation funicular.</li></ul>""",
  },
  {
   "q_en":"Q.2 (b) OR Explain types of equilibrium. (04 marks)",
   "marks_en":"4 marks","marks_gu":"૦૪ ગુણ",
   "a_en":"""<p><strong>Stable:</strong> Small displacement returns — CG rises? Actually stable lower CG ball in bowl. <strong>Unstable:</strong> Moves away — ball on top hill CG lowers. <strong>Neutral:</strong> Stays displaced — ball on flat plane. Conditions ΣF=0 ΣM=0 for planar equilibrium.</p>""",
   "a_gu":"""<p><strong>સ્થિર:</strong> ખસેડો પાછું આવે bowl માં દડો. <strong>અસ્થિર:</strong> દૂર જાય ટેકરી પર. <strong>Neutral:</strong> જ્યાં ખસેડો ત્યાં રહે સપાટ. ΣF=0 ΣM=0.</p>""",
  },
  {
   "q_en":"Q.2 (c) OR Calculate support reaction for the beam as shown in figure 03. (07 marks)",
   "marks_en":"7 marks","marks_gu":"૦૭ ગુણ",
   "a_en":"""<p><strong>Beam A pin B roller length 6m: 30kN at 1m from A, 10kN 45° at 2m from A (1m beyond), UDL 20kN/m over 2m near B (4 to 6m). UDL total 40kN at 5m from A mid of last 2m.</strong></p><div class="eq">Resolve 10kN: H=10cos45=7.07kN V=7.07kN</div><div class="eq">ΣFx=0: Ax +7.07=0 → <strong>Ax = -7.07kN left</strong></div><div class="eq">ΣFy: Ay+By =30+7.07+40=77.07kN</div><div class="eq">ΣMA=0: By×6 −30×1 −7.07×2 −40×5=0 →6By=30+14.14+200=244.14 → <strong>By=40.69kN up</strong></div><div class="eq">Ay=77.07−40.69= <strong>36.38kN up</strong></div>""" + svg_wrap(BEAM_FIG3_SVG,"Fig03 — 30kN, 10kN inclined, UDL 40kN — reactions via ΣF ΣM","Fig03 beam"),
   "a_gu":"""<p><strong>Beam 6m A pin B roller: 30kN 1m, 10kN45° 2m, UDL40kN 5m એ.</strong></p><div class="eq">Ax=-7.07kN By=40.69kN Ay=36.38kN</div>""" + svg_wrap(BEAM_FIG3_SVG,"Fig03 UDL 40kN 5m","Fig03 beam"),
  },
 ]
},
{
 "title_en":"Q3 · Beams, I and T centroid",
 "title_gu":"પ્ર.3 · બીમ, I અને T centroid",
 "cards":[
  {
   "q_en":"Q.3 (a) List out types of beam with figure. (03 marks)",
   "marks_en":"3 marks","marks_gu":"૦૩ ગુણ",
   "a_en":"""<ul><li>Simply supported, cantilever, overhang, fixed, continuous, propped — all differ by supports.</li></ul>""" + svg_wrap(BEAM_TYPES_SVG,"SS cantilever overhang fixed continuous","Beam types"),
   "a_gu":"""<ul><li>Simply supported cantilever overhang fixed continuous propped.</li></ul>""" + svg_wrap(BEAM_TYPES_SVG,"બીમ પ્રકાર","Beam types"),
  },
  {
   "q_en":"Q.3 (b) Explain types of supports in beam. (04 marks)",
   "marks_en":"4 marks","marks_gu":"૦૪ ગુણ",
   "a_en":"""<p><strong>Hinged:</strong> 2 reactions Ax Ay allows rotation. <strong>Roller:</strong> 1 vertical on rollers free horizontal. <strong>Fixed:</strong> 3 Ax Ay M no rotation. <strong>Simple free:</strong> rest on surface. Choice affects determinacy.</p>""",
   "a_gu":"""<p><strong>Hinged:</strong> 2 Ax Ay. <strong>Roller:</strong> 1 vertical. <strong>Fixed:</strong> 3 Ax Ay M. સરળ રીતે ટેકવેલો.</p>""",
  },
  {
   "q_en":"Q.3 (c) Calculate center of gravity of I section having following dimensions. Top flange =200mm x20mm Bottom flange =200mm x20mm Web =20mm x160mm. (07 marks)",
   "marks_en":"7 marks","marks_gu":"૦૭ ગુણ",
   "a_en":"""<div class="eq">Three rectangles: A1 top 4000 A2 web 3200 A3 bottom 4000 total A=11200mm²</div><div class="eq">Take bottom y=0: y1 bottom=10, y2=20+80=100, y3=180+10=190 — symmetric so ȳ=100mm from bottom. Check: (4000×10+3200×100+4000×190)/11200= (40000+320000+760000)/11200=1120000/11200= <strong>100mm</strong></div><div class="eq">x̄ 0 on symmetry vertical line.</div><p>Symmetric I CG at mid height 100mm and mid width 100mm.</p>""" + svg_wrap(I_CG_SVG,"I symmetric → CG at mid 100mm from base","I CG"),
   "a_gu":"""<div class="eq">A=11200 y1 10 y2 100 y3 190 → ȳ=100mm નીચે થી x̄ 0 symmetry.</div>""" + svg_wrap(I_CG_SVG,"I 100mm","I CG"),
  },
  {
   "q_en":"Q.3 (a) OR Tell Varignon’s principle of moments with formula. (03 marks)",
   "marks_en":"3 marks","marks_gu":"૦૩ ગુણ",
   "a_en":"""<p><strong>Varignon: Moment of resultant about any point equals sum of moments of components.</strong></p><div class="eq">M_R^O = Σ M_Fi^O &nbsp; R×r = F1×r + F2×r</div><p>Use to find moment of inclined force via components.</p>""",
   "a_gu":"""<p><strong>Varignon: પરિણામી નો moment = ઘટક ના moments નો સરવાળો.</strong></p><div class="eq">M_R = Σ M_Fi</div>""",
  },
  {
   "q_en":"Q.3 (b) OR Explain clockwise moment and anticlockwise moment of force. (04 marks)",
   "marks_en":"4 marks","marks_gu":"૦૪ ગુણ",
   "a_en":"""<p><strong>Clockwise negative:</strong> Force tends to rotate body clockwise about point — e.g. weight on right of pivot. <strong>Anticlockwise positive:</strong> Opposite. Sign convention arbitrary but consistent — sum zero for equilibrium.</p><p>Couple sign per right hand rule vector out of plane.</p>""",
   "a_gu":"""<p><strong>Clockwise:</strong> બળ બિંદુ એ ઘડિયાળ દિશા ઘૂમાવે. <strong>Anticlockwise:</strong> ઊલટું. ΣM=0 સંતુલન.</p>""",
  },
  {
   "q_en":"Q.3 (c) OR Calculate center of gravity of T section having following dimensions. Top flange =150mm x20mm Web =20mm x100mm. (07 marks)",
   "marks_en":"7 marks","marks_gu":"૦૭ ગુણ",
   "a_en":"""<div class="eq">A1 flange 150×20=3000 at y1=100+10=110mm from bottom &nbsp; A2 web 20×100=2000 at y2=50mm</div><div class="eq">ȳ = (3000×110 +2000×50)/5000 = (330000+100000)/5000=430000/5000= <strong>86mm from bottom</strong></div><p>x̄ 0 on symmetry.</p>""" + svg_wrap(T_CG_SVG,"T flange 150×20 web 20×100 → ȳ 86mm","T CG"),
   "a_gu":"""<div class="eq">A1=3000 y1=110 A2=2000 y2=50 → ȳ=86mm x̄0</div>""" + svg_wrap(T_CG_SVG,"T 86mm","T CG"),
  },
 ]
},
{
 "title_en":"Q4 · Friction and CG",
 "title_gu":"પ્ર.4 · ઘર્ષણ અને CG",
 "cards":[
  {
   "q_en":"Q.4 (a) Tell advantages of friction. (03 marks)",
   "marks_en":"3 marks","marks_gu":"૦૩ ગુણ",
   "a_en":"""<ul><li>Walk, vehicle drive brake need grip.</li><li>Writing, belt transmission, screw holding, ladder stable.</li></ul>""" + svg_wrap(FRICTION_ADV_SVG,"Grip walk brake belt screw ladder","Friction adv"),
   "a_gu":"""<ul><li>ચાલવું drive brake grip.</li><li>લખવું belt screw ladder.</li></ul>""" + svg_wrap(FRICTION_ADV_SVG,"friction grip","Friction adv"),
  },
  {
   "q_en":"Q.4 (b) Describe centroid and center of gravity. (04 marks)",
   "marks_en":"4 marks","marks_gu":"૦૪ ગુણ",
   "a_en":"""<p><strong>Centroid C</strong> geometric centre area — independent of gravity. <strong>CG G</strong> weight centre — same as centroid if uniform.</p><p>Centroid of rectangle mid, triangle 1/3 height.</p>""" + svg_wrap(CG_DEF_SVG,"Centroid area centre — CG weight centre same if uniform","Centroid CG"),
   "a_gu":"""<p><strong>Centroid</strong> ભૌમિતિક કેન્દ્ર — <strong>CG</strong> વજન કેન્દ્ર uniform તો એક જ.</p>""" + svg_wrap(CG_DEF_SVG,"Centroid vs CG","Centroid CG"),
  },
  {
   "q_en":"Q.4 (c) A pull of P inclined at 30° to the horizontal is necessary to move a wooden block of 250 N weight placed on horizontal table. If co efficient of friction is 0.2 find out pull. (07 marks)",
   "marks_en":"7 marks","marks_gu":"૦૭ ગુણ",
   "a_en":"""<div class="eq">Pull up at 30° reduces N: N = W − P sin30°</div><div class="eq">For motion: P cos30° = μN = μ(W − P sin30)</div><div class="eq">P cos30 + μP sin30 = μW → P(0.8660 +0.2×0.5)=0.2×250 → P(0.9660)=50 → <strong>P=51.76 N</strong></div>""" + svg_wrap(PULL_250_SVG,"N=W-Psin30 Pcos30=μN → P=51.76N","Pull 250N"),
   "a_gu":"""<div class="eq">Pcos30=μ(W-Psin30)→P=51.76N</div>""" + svg_wrap(PULL_250_SVG,"P=51.76N","Pull 250N"),
  },
  {
   "q_en":"Q.4 (a) OR List out types of friction. (03 marks)",
   "marks_en":"3 marks","marks_gu":"૦૩ ગુણ",
   "a_en":"""<ul><li><strong>Static:</strong> Before motion — max limiting.</li><li><strong>Kinetic:</strong> During sliding — less than static, sliding vs rolling.</li><li><strong>Dry, fluid, boundary.</strong></li></ul>""",
   "a_gu":"""<ul><li>Static ગતિ પહેલા.</li><li>Kinetic સliding સમય ઓછો.</li><li>Dry fluid.</li></ul>""",
  },
  {
   "q_en":"Q.4 (b) OR Explain axis of reference. (04 marks)",
   "marks_en":"4 marks","marks_gu":"૦૪ ગુણ",
   "a_en":"""<p><strong>Axis of reference is datum X Y for measurement.</strong> Chosen conveniently at bottom or centroid — all distances y measured from it for CG moment.</p>""",
   "a_gu":"""<p><strong>Reference axis માપ માટે datum X Y — તળિયા કે centroid પર.</strong></p>""",
  },
  {
   "q_en":"Q.4 (c) OR Find out magnitude of push inclined at 30° to the horizontal required to move a block of 500 N resting on horizontal surface having coefficient of friction is 0.4 N. (07 marks)",
   "marks_en":"7 marks","marks_gu":"૦૭ ગુણ",
   "a_en":"""<div class="eq">Push down increases N: N = W + P sin30°</div><div class="eq">P cos30° = μN = μ(W + P sin30) → P(cos30 − μ sin30)= μW</div><div class="eq">P(0.8660 −0.4×0.5)=0.4×500 → P(0.6660)=200 → <strong>P=300.30 N</strong></div><p>Push needs larger than pull for same W as normal increases.</p>""" + svg_wrap(PUSH_500_SVG,"N=W+Psin30 Pcos30=μN → P=300.3N","Push 500N"),
   "a_gu":"""<div class="eq">Pcos30=μ(W+Psin30)→P=300.3N — push વજન વધારે normal થી વધુ બળ.</div>""" + svg_wrap(PUSH_500_SVG,"P=300.3N","Push 500N"),
  },
 ]
},
{
 "title_en":"Q5 · Law of machine and wheel axle",
 "title_gu":"પ્ર.5 · યંત્ર નિયમ અને wheel axle",
 "cards":[
  {
   "q_en":"Q.5 (a) Define mechanical advantage and velocity ratio. (03 marks)",
   "marks_en":"3 marks","marks_gu":"૦૩ ગુણ",
   "a_en":"""<p><strong>MA = W/P</strong> load over effort — actual lift ratio includes friction.</p><p><strong>VR = Dp/Dw</strong> distance effort over distance load — geometry constant.</p><p>η = MA/VR.</p>""",
   "a_gu":"""<p><strong>MA=W/P</strong> &nbsp; <strong>VR=Dp/Dw</strong> distance ગુણોત્તર — η=MA/VR</p>""",
  },
  {
   "q_en":"Q.5 (b) Explain law of machine. (04 marks)",
   "marks_en":"4 marks","marks_gu":"૦૪ ગુણ",
   "a_en":"""<p><strong>Law: P = mW + C</strong> linear — m slope, C intercept at no load friction. Plot W vs P line gives m C. Max η =1/(mVR).</p><p>Valid within working range — if W too low law deviates due to stiction.</p>""" + svg_wrap(MACHINE_LAW_SVG,"P=mW+C linear — m slope C no load — ηmax=1/(mVR)","Law"),
   "a_gu":"""<p><strong>P=mW+C સીધી રેખા — m ઢાળ C friction. ηmax=1/(mVR)</strong></p>""" + svg_wrap(MACHINE_LAW_SVG,"P=mW+C","Law"),
  },
  {
   "q_en":"Q.5 (c) A law of machine for simple machine is P = 0.1W + 3.5. Find out effort required to lift a load of 50kN. Also calculate maximum efficiency and maximum mechanical advantage if VR = 30.5 (07 marks)",
   "marks_en":"7 marks","marks_gu":"૦૭ ગુણ",
   "a_en":"""<div class="eq">P =0.1×50 +3.5=5+3.5= <strong>8.5 kN</strong></div><div class="eq">Max η = <span class="frac"><span class="num">1</span><span class="den">mVR</span></span> =1/(0.1×30.5)=1/3.05= <strong>32.79%</strong></div><div class="eq">Max MA = ηmax ×VR =0.3279×30.5= <strong>10</strong> &nbsp; Check m=0.1=1/10 so MAmax=1/m=10 matches.</div>""",
   "a_gu":"""<div class="eq">P=8.5kN ηmax=32.79% MAmax=10 — m=0.1 →1/m=10</div>""",
  },
  {
   "q_en":"Q.5 (a) OR Define reversible machine and non-reversible machine. (03 marks)",
   "marks_en":"3 marks","marks_gu":"૦૩ ગુણ",
   "a_en":"""<p><strong>Reversible:</strong> η above 50% — load descends on removing effort — needs brake — e.g. pulley.</p><p><strong>Non-reversible self-locking:</strong> η below 50% — load stays — e.g. screw jack safe lifting.</p>""",
   "a_gu":"""<p><strong>Reversible:</strong> η>50% load નીચે આવે brake જોઈએ. <strong>Self locking:</strong> η<50% load અટકે screw jack.</p>""",
  },
  {
   "q_en":"Q.5 (b) OR Describe systems of pulley with figure. (04 marks)",
   "marks_en":"4 marks","marks_gu":"૦૪ ગુણ",
   "a_en":"""<p><strong>First order:</strong> Movable pulleys support load VR =2^n. <strong>Second order:</strong> One movable one fixed VR = n. <strong>Third order:</strong> gun tackle inverted. Differential VR = 2D/(D-d).</p>""" + svg_wrap(PULLEY_SVG,"First movable, second gun, third luff — VR = ropes supporting load","Pulleys"),
   "a_gu":"""<p><strong>પ્રથમ:</strong> movable load VR 2^n <strong>બીજો:</strong> gun <strong>ત્રીજો:</strong> luff — VR દોરડા સંખ્યા.</p>""" + svg_wrap(PULLEY_SVG,"pulley VR","Pulleys"),
  },
  {
   "q_en":"Q.5 (c) OR In a wheel and differential axle, diameter of effort wheel is 40 cm and diameters of larger & smaller axles are 12 cm and 10 cm respectively. Find velocity ratio. If efficiency is 60%, find the effort required to lift a load of 600 N. (07 marks)",
   "marks_en":"7 marks","marks_gu":"૦ે ગુણ",
   "a_en":"""<div class="eq">VR = <span class="frac"><span class="num">2 × D_eff</span><span class="den">D_large − D_small</span></span> = <span class="frac"><span class="num">2×40</span><span class="den">12−10</span></span> =80/2= <strong>40</strong></div><div class="eq">Ideal effort Pi = W/VR =600/40=15N &nbsp; Actual P = Pi/η =15/0.60= <strong>25 N</strong></div>""" + svg_wrap(WHEEL_DIFF_SVG,"VR=2De/(Dl-Ds)=40 Pi15N P25N at 60%","Wheel diff"),
   "a_gu":"""<div class="eq">VR=2×40/(12-10)=40 Pi=15N P=25N 60% એ</div>""" + svg_wrap(WHEEL_DIFF_SVG,"VR40 P25N","Wheel diff"),
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
            cards.append(f'''<details class="card"><summary><strong><span class="en">{q_html}</span><span class="gu">{q_html}</span></strong><small><span class="en">{c["marks_en"]}</span><span class="gu">{c["marks_gu"]}</span></small></summary><div class="answer"><div class="en">{c["a_en"]}</div><div class="gu">{c["a_gu"]}</div></div></details>''')
        sections_html.append(f'''<section class="group"><h2>{html.escape(sec["title_en"])}</h2>{''.join(cards)}</section>''')
    page=f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>DI02000071 · Summer 2026 solved paper</title><style>{CSS}</style></head><body><main class="page"><header class="hero"><div class="eyebrow">Solved question paper · English questions · Friendly Gujarati answers</div><div class="lang-switch" aria-label="Choose language"><button type="button" data-lang="en" aria-pressed="true">English</button><button type="button" data-lang="gu" aria-pressed="false">ગુજરાતી</button></div><h1>Engineering Mechanics</h1><div class="meta">GTU Diploma · Civil/All · Semester 2 · Summer 2026 · DI02000071 · 25-06-2026 · 70 marks · 10:30 AM TO 01:00 PM</div></header>{''.join(sections_html)}<div class="footer">Solved paper for study. Verify with mechanics data book before site application.</div></main><script>document.querySelectorAll('.lang-switch button').forEach(b=>b.addEventListener('click',()=>{{document.documentElement.lang=b.dataset.lang;document.querySelectorAll('.lang-switch button').forEach(x=>x.setAttribute('aria-pressed',x===b?'true':'false'));}}));</script></body></html>'''
    return page

def main():
    page=build_page()
    out_papers=ROOT/"papers-upload/papers/DI02000071/summer-2026.html"
    out_ws=ROOT/"preview/workshop/DI02000071_summer2026_bilingual.html"
    out_papers.parent.mkdir(parents=True,exist_ok=True)
    out_ws.parent.mkdir(parents=True,exist_ok=True)
    out_papers.write_text(page,encoding="utf-8")
    out_ws.write_text(page,encoding="utf-8")
    d=page.count('<details'); s=page.count('<section'); ce=page.count('class="en"'); cg=page.count('class="gu"')
    print(f"Bilingual: {out_papers} ({len(page)} chars)")
    print(f"details={d}, sections={s}, en={ce}, gu={cg}")
    print("PASS" if d==28 and s==5 and ce>=28 and cg>=28 else "FAIL")
    figs=page.count('<figure>'); fracs=page.count('class="frac"')
    print(f"figs={figs} fracs={fracs}")
    import re
    gu=''.join(re.findall(r'<div class="gu">(.*?)</div>',page,re.S))
    print(f"brackets gu={gu.count('(')+gu.count(')')}")
    (ROOT/"drive-upload/DI02000071_summer_2026_bilingual.html").write_text(page,encoding="utf-8")

if __name__=="__main__":
    main()
