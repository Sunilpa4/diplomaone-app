#!/usr/bin/env python3
"""Build DI01006021 Construction Material Summer-2026 (07-07-2026) — friendly Gujarati minimal brackets."""
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

# SVGs
ECO_SVG="""<rect width="360" height="220" fill="#fff"/><text x="180" y="16" font-size="11" text-anchor="middle" font-weight="bold" fill="#0b5b6a">Eco-friendly construction materials</text>
<g font-size="6">
<rect x="12" y="38" width="105" height="32" rx="6" fill="#e6f4ef" stroke="#0b8043"/><text x="64" y="51" text-anchor="middle" font-weight="bold">Bamboo, Timber FSC</text><text x="64" y="62" text-anchor="middle">renewable low carbon</text>
<rect x="127" y="38" width="105" height="32" rx="6" fill="#eaf4fa" stroke="#0b5b6a"/><text x="179" y="51" text-anchor="middle" font-weight="bold">Fly ash, GGBS</text><text x="179" y="62" text-anchor="middle">waste reuse in concrete</text>
<rect x="242" y="38" width="106" height="32" rx="6" fill="#fff4e0" stroke="#b77e24"/><text x="295" y="51" text-anchor="middle" font-weight="bold">AAC, CSEB</text><text x="295" y="62" text-anchor="middle">light earth blocks</text>
<rect x="12" y="80" width="105" height="32" rx="6" fill="#efe3fa" stroke="#58316f"/><text x="64" y="93" text-anchor="middle" font-weight="bold">Recycled aggregate</text><text x="64" y="104" text-anchor="middle">C&D waste reuse</text>
<rect x="127" y="80" width="105" height="32" rx="6" fill="#fce9e9" stroke="#c00"/><text x="179" y="93" text-anchor="middle" font-weight="bold">Low VOC paint</text><text x="179" y="104" text-anchor="middle">natural lime, linseed</text>
<rect x="242" y="80" width="106" height="32" rx="6" fill="#f1fbf6" stroke="#77a795"/><text x="295" y="93" text-anchor="middle" font-weight="bold">Solar glass, green roof</text><text x="295" y="104" text-anchor="middle">energy saving</text>
</g>
<text x="180" y="135" font-size="7" text-anchor="middle">Choice criterion: low embodied energy, local, recyclable, non-toxic, durable</text>"""

RECYCLE_SVG="""<rect width="360" height="220" fill="#fff"/><text x="180" y="16" font-size="11" text-anchor="middle" font-weight="bold" fill="#0b5b6a">Recycled construction materials cycle</text>
<g font-size="6">
<text x="40" y="45">Demolition → segregation →</text><rect x="150" y="38" width="60" height="22" rx="5" fill="#eaf4fa" stroke="#0b5b6a"/><text x="180" y="52" text-anchor="middle">Crusher</text>
<text x="220" y="45">→ recycled aggregate</text>
<text x="40" y="70">Scrap steel → melt →</text><rect x="150" y="63" width="60" height="22" rx="5" fill="#fff3e0" stroke="#b77e24"/><text x="180" y="77" text-anchor="middle">Rebar</text>
<text x="40" y="95">Glass cullet →</text><rect x="150" y="88" width="60" height="22" rx="5" fill="#f1fbf6" stroke="#77a795"/><text x="180" y="102" text-anchor="middle">Tiles</text>
<text x="40" y="120">Plastic waste →</text><rect x="150" y="113" width="60" height="22" rx="5" fill="#fce9e9" stroke="#c00"/><text x="180" y="127" text-anchor="middle">Paver blocks</text>
<text x="40" y="145">Fly ash →</text><rect x="150" y="138" width="60" height="22" rx="5" fill="#efe3fa" stroke="#58316f"/><text x="180" y="152" text-anchor="middle">Bricks</text>
</g>
<text x="180" y="180" font-size="6.5" text-anchor="middle">Benefit: save natural stone sand, reduce landfill — quality check as per IS 383 required</text>"""

LIME_SVG="""<rect width="360" height="220" fill="#fff"/><text x="180" y="16" font-size="11" text-anchor="middle" font-weight="bold" fill="#0b5b6a">Lime — slaking and setting</text>
<g font-size="6.5">
<rect x="18" y="38" width="95" height="38" rx="6" fill="#fff4e0" stroke="#b77e24"/><text x="65" y="52" text-anchor="middle" font-weight="bold">Quick lime CaO</text><text x="65" y="64" text-anchor="middle">from calcination 900°C</text>
<text x="120" y="58" font-size="10">+ H2O →</text>
<rect x="145" y="38" width="95" height="38" rx="6" fill="#e6f4ef" stroke="#0b8043"/><text x="192" y="52" text-anchor="middle" font-weight="bold">Slaked Ca(OH)2</text><text x="192" y="64" text-anchor="middle">hiss, heat, cracks</text>
<text x="247" y="58" font-size="10">+ CO2 →</text>
<rect x="275" y="38" width="65" height="38" rx="6" fill="#eaf4fa" stroke="#0b5b6a"/><text x="307" y="52" text-anchor="middle" font-weight="bold">Set CaCO3</text><text x="307" y="64" text-anchor="middle">hardens</text>
<text x="18" y="95" font-size="6">Slaking: CaO + H2O = Ca(OH)2 + heat 65kJ, volume 2.5×, must do slowly with excess water 3 days</text>
<text x="18" y="110" font-size="6">Setting: Ca(OH)2 + CO2 = CaCO3 + H2O — carbonation, needs air, months — hydraulic lime also C2S hydrate under water</text>
</g>"""

SEASON_SVG="""<rect width="360" height="220" fill="#fff"/><text x="180" y="16" font-size="11" text-anchor="middle" font-weight="bold" fill="#0b5b6a">Seasoning of timber — why and how</text>
<g font-size="6">
<rect x="15" y="38" width="75" height="30" rx="6" fill="#eaf4fa" stroke="#0b5b6a"/><text x="52" y="50" text-anchor="middle">Natural</text><text x="52" y="60" text-anchor="middle">air stack 6 months</text>
<rect x="100" y="38" width="75" height="30" rx="6" fill="#fff4e0" stroke="#b77e24"/><text x="137" y="50" text-anchor="middle">Kiln</text><text x="137" y="60" text-anchor="middle">chamber 40-90°C</text>
<rect x="185" y="38" width="75" height="30" rx="6" fill="#f1fbf6" stroke="#77a795"/><text x="222" y="50" text-anchor="middle">Chemical</text><text x="222" y="60" text-anchor="middle">salt soak</text>
<rect x="270" y="38" width="75" height="30" rx="6" fill="#fce9e9" stroke="#c00"/><text x="307" y="50" text-anchor="middle">Water/Boiling</text>
<text x="18" y="90" font-size="6">Purpose: reduce moisture 50% → 12%, avoid warp, increase strength, protect from fungi, take polish better</text>
<text x="18" y="104" font-size="6">Steps: stack with spacers under shade, airflow, weigh till constant, kiln controlled temp humidity 10-20 days</text>
</g>"""

TREE_SVG="""<rect width="360" height="220" fill="#fff"/><text x="180" y="16" font-size="11" text-anchor="middle" font-weight="bold" fill="#0b5b6a">Cross section of exogenous tree — 7 parts</text>
<circle cx="95" cy="110" r="55" fill="none" stroke="#5a3e1b" stroke-width="1.2"/>
<circle cx="95" cy="110" r="45" fill="#fff8e1" stroke="#b77e24" stroke-dasharray="2 2"/>
<circle cx="95" cy="110" r="35" fill="#ffe9a0" stroke="#b77e24"/>
<circle cx="95" cy="110" r="20" fill="#ffcc80" stroke="#8d5a00"/>
<circle cx="95" cy="110" r="6" fill="#5a3e1b"/>
<g font-size="5.5">
<text x="170" y="50">1 Bark outer — protection</text>
<text x="170" y="62">2 Inner bark — transports food</text>
<text x="170" y="74">3 Cambium — growth layer thin</text>
<text x="170" y="86">4 Sapwood light — carries water</text>
<text x="170" y="98">5 Heartwood dark — strong durable</text>
<text x="170" y="110">6 Medullary rays — radial strength</text>
<text x="170" y="122">7 Pith centre — soft, weak</text>
</g>
<text x="95" y="180" font-size="6" text-anchor="middle">Exogenous grows outward ring each year — age by counting rings</text>"""

DEFECT_SVG="""<rect width="360" height="220" fill="#fff"/><text x="180" y="16" font-size="11" text-anchor="middle" font-weight="bold" fill="#0b5b6a">Defects in timber with sketches</text>
<g font-size="5.5">
<rect x="12" y="38" width="80" height="32" rx="6" fill="#eaf4fa" stroke="#0b5b6a"/><text x="52" y="50" text-anchor="middle" font-weight="bold">Knot</text><text x="52" y="60" text-anchor="middle">branch base hard spot</text>
<rect x="98" y="38" width="80" height="32" rx="6" fill="#fff4e0" stroke="#b77e24"/><text x="138" y="50" text-anchor="middle" font-weight="bold">Shake</text><text x="138" y="60" text-anchor="middle">split along grain</text>
<rect x="184" y="38" width="80" height="32" rx="6" fill="#fce9e9" stroke="#c00"/><text x="224" y="50" text-anchor="middle" font-weight="bold">Warp / Bow</text><text x="224" y="60" text-anchor="middle">bend due to drying</text>
<rect x="270" y="38" width="78" height="32" rx="6" fill="#f1fbf6" stroke="#77a795"/><text x="309" y="50" text-anchor="middle" font-weight="bold">Fungal decay</text><text x="309" y="60" text-anchor="middle">soft rot, white</text>
<text x="12" y="88" font-size="6">Also: honeycombing inside cracks, wane missing edge, case hardening, sap stain, insect holes</text>
<text x="12" y="102" font-size="6">Natural: knots, twisted fibre. Defects from conversion: warp. Fungi/insect: rot.</text>
<line x1="40" y1="108" x2="80" y2="118" stroke="#333"/><text x="85" y="120" font-size="5">knot</text>
<line x1="120" y1="108" x2="160" y2="118" stroke="#333"/><text x="165" y="120" font-size="5">shake line</text>
</g>"""

AGG_SVG="""<rect width="360" height="220" fill="#fff"/><text x="180" y="16" font-size="11" text-anchor="middle" font-weight="bold" fill="#0b5b6a">Aggregate classification by size — IS 383</text>
<g font-size="6">
<rect x="18" y="40" width="100" height="30" rx="6" fill="#eaf4fa" stroke="#0b5b6a"/><text x="68" y="52" text-anchor="middle" font-weight="bold">Fine &lt;4.75mm</text><text x="68" y="62" text-anchor="middle">sand zone I to IV</text>
<rect x="130" y="40" width="100" height="30" rx="6" fill="#fff4e0" stroke="#b77e24"/><text x="180" y="52" text-anchor="middle" font-weight="bold">Coarse &gt;4.75mm</text><text x="180" y="62" text-anchor="middle">10,20,40mm single</text>
<rect x="242" y="40" width="100" height="30" rx="6" fill="#f1fbf6" stroke="#77a795"/><text x="292" y="52" text-anchor="middle" font-weight="bold">All-in / graded</text><text x="292" y="62" text-anchor="middle">40mm down well mixed</text>
<text x="18" y="90" font-size="6">Fine fills voids between coarse, good grading reduces cement paste — Fuller curve ideal</text>
<text x="18" y="104" font-size="6">Based on source: natural river, crushed, recycled. Based on shape: rounded, angular.</text>
</g>"""

BRICKMFG_SVG="""<rect width="360" height="220" fill="#fff"/><text x="180" y="16" font-size="11" text-anchor="middle" font-weight="bold" fill="#0b5b6a">Brick manufacturing — flow diagram</text>
<g font-size="6">
<rect x="12" y="38" width="62" height="24" rx="5" fill="#fff4e0" stroke="#b77e24"/><text x="43" y="52" text-anchor="middle">Clay prep</text>
<text x="78" y="52">→</text><rect x="85" y="38" width="52" height="24" rx="5" fill="#eaf4fa" stroke="#0b5b6a"/><text x="111" y="52" text-anchor="middle">Mould</text>
<text x="141" y="52">→</text><rect x="148" y="38" width="52" height="24" rx="5" fill="#f1fbf6" stroke="#77a795"/><text x="174" y="52" text-anchor="middle">Dry</text>
<text x="204" y="52">→</text><rect x="211" y="38" width="50" height="24" rx="5" fill="#fce9e9" stroke="#c00"/><text x="236" y="52" text-anchor="middle">Burn</text>
<text x="265" y="52">→</text><rect x="275" y="38" width="60" height="24" rx="5" fill="#e6f4ef" stroke="#0b8043"/><text x="305" y="52" text-anchor="middle">Sort/test</text>
<text x="18" y="80" font-size="6">Prep: dig, weather, grind, temper with water. Mould: hand or machine 19×9×9cm with frog</text>
<text x="18" y="94" font-size="6">Dry: shade 7 days to 8% moisture, avoid cracking. Burn: clamp or kiln to 1100°C</text>
</g>"""

HOFFMAN_SVG="""<rect width="360" height="220" fill="#fff"/><text x="180" y="16" font-size="11" text-anchor="middle" font-weight="bold" fill="#0b5b6a">Hoffmann kiln — continuous circular</text>
<g font-size="5.5">
<ellipse cx="180" cy="95" rx="85" ry="45" fill="none" stroke="#0b5b6a" stroke-width="1.2"/>
<text x="180" y="98" text-anchor="middle" font-size="6">12 chambers circular — fire moves, not bricks</text>
<text x="95" y="70">Load</text><text x="220" y="70">Burning 1100°C</text><text x="140" y="120">Cooling</text><text x="210" y="120">Drying by waste heat</text>
<line x1="130" y1="85" x2="120" y2="70" stroke="#333"/><line x1="200" y1="80" x2="210" y2="68" stroke="#333"/>
<text x="18" y="150" font-size="6">Fuel from top, draught via chimney in centre. Green bricks enter drying zone, then burning, then cooling air preheats fuel</text>
<text x="18" y="162" font-size="6">Capacity 20,000/day, fuel efficient, better quality control than clamp —needs permanent structure</text>
</g>"""

CLAMP_KILN_SVG="""<rect width="360" height="220" fill="#fff"/><text x="180" y="16" font-size="11" text-anchor="middle" font-weight="bold" fill="#0b5b6a">Clamp vs Kiln burning — comparison</text>
<g font-size="5.5">
<text x="18" y="38" font-weight="bold">Clamp — temporary stack ground</text><text x="18" y="50">Fuel layers with bricks, burn 15 days, cool 10 days</text><text x="18" y="62">Cheap no building, but 25% over/burnt, high fuel, weather dependent</text>
<text x="18" y="80" font-weight="bold">Hoffman kiln — permanent circular 12 chambers</text><text x="18" y="92">Fire moves daily, waste heat dries next load, continuous</text><text x="18" y="104">Cost high to build but fuel less, uniform quality, large scale</text>
<text x="18" y="122" font-size="6" fill="#0b5b6a">Choice: village 10,000 need clamp, city 1 lakh need kiln</text>
</g>"""

BRICKCUT_SVG="""<rect width="360" height="220" fill="#fff"/><text x="180" y="16" font-size="11" text-anchor="middle" font-weight="bold" fill="#0b5b6a">Queen closer, King closer, Bat — brick cuts</text>
<g font-size="6">
<rect x="25" y="40" width="70" height="35" rx="3" fill="#fff4e0" stroke="#b77e24"/><text x="60" y="55" text-anchor="middle">Full 19×9×9</text>
<line x1="60" y1="60" x2="60" y2="72" stroke="#c00" stroke-dasharray="2 2"/><text x="60" y="70" text-anchor="middle" font-size="5" fill="#c00">cut</text>
<rect x="110" y="40" width="35" height="35" rx="3" fill="#eaf4fa" stroke="#0b5b6a"/><text x="127" y="52" text-anchor="middle" font-size="5">Queen</text><text x="127" y="62" text-anchor="middle" font-size="5">4.5cm wide</text><text x="127" y="72" font-size="4.5">lengthwise</text>
<rect x="160" y="40" width="70" height="35" rx="3" fill="#eaf4fa" stroke="#0b5b6a"/><text x="195" y="52" text-anchor="middle" font-size="5">King 19×(4.5+9) L</text><text x="195" y="64" text-anchor="middle" font-size="5">notch</text>
<rect x="245" y="40" width="70" height="35" rx="3" fill="#f1fbf6" stroke="#77a795"/><text x="280" y="55" text-anchor="middle">Bat 3/4, 1/2</text><text x="280" y="65" text-anchor="middle" font-size="5">across width</text>
<text x="18" y="95" font-size="6">Use: queen closer closing bond next to quoin header, king for splayed jamb, bat for broken bond</text>
</g>"""

CEMENT_DRY_SVG="""<rect width="360" height="220" fill="#fff"/><text x="180" y="16" font-size="11" text-anchor="middle" font-weight="bold" fill="#0b5b6a">Cement — dry process flow</text>
<g font-size="5.5">
<rect x="12" y="38" width="65" height="24" rx="5" fill="#eaf4fa" stroke="#0b5b6a"/><text x="44" y="52" text-anchor="middle">Crush limestone</text>
<text x="80" y="52">→</text><rect x="86" y="38" width="55" height="24" rx="5" fill="#fff4e0" stroke="#b77e24"/><text x="113" y="52" text-anchor="middle">Grind raw</text>
<text x="145" y="52">→</text><rect x="151" y="38" width="55" height="24" rx="5" fill="#f1fbf6" stroke="#77a795"/><text x="178" y="52" text-anchor="middle">Preheat 800°C</text>
<text x="210" y="52">→</text><rect x="218" y="38" width="55" height="24" rx="5" fill="#fce9e9" stroke="#c00"/><text x="245" y="52" text-anchor="middle">Kiln 1450°C</text>
<text x="278" y="52">→</text><rect x="288" y="38" width="60" height="24" rx="5" fill="#e6f4ef" stroke="#0b8043"/><text x="318" y="52" text-anchor="middle">Grind + gypsum</text>
<text x="18" y="80" font-size="6">Dry ground raw meal to cyclone preheater, rotary kiln makes clinker nodules, cooled, ground with 3% gypsum to cement</text>
<text x="18" y="94" font-size="6">Fuel less vs wet, dust control needed, modern all dry process in India</text>
</g>"""

GLASS_SVG="""<rect width="360" height="220" fill="#fff"/><text x="180" y="16" font-size="11" text-anchor="middle" font-weight="bold" fill="#0b5b6a">Glass fibres — types</text>
<g font-size="6">
<rect x="20" y="40" width="100" height="40" rx="6" fill="#eaf4fa" stroke="#0b5b6a"/><text x="70" y="53" text-anchor="middle">Glass fibre</text><text x="70" y="65" text-anchor="middle">thin filaments 10 micron</text>
<rect x="130" y="40" width="100" height="40" rx="6" fill="#fff4e0" stroke="#b77e24"/><text x="180" y="53" text-anchor="middle">GRP / FRP</text><text x="180" y="65" text-anchor="middle">resin + fibre sheet</text>
<rect x="240" y="40" width="100" height="40" rx="6" fill="#f1fbf6" stroke="#77a795"/><text x="290" y="53" text-anchor="middle">Plastic fibre</text><text x="290" y="65" text-anchor="middle">PP, nylon in concrete</text>
<text x="20" y="105" font-size="6">Use: crack control in concrete, waterproof boards, pipes — not for main rebar, alkaline sensitive need AR glass</text>
</g>"""

ANTITERM_SVG="""<rect width="360" height="220" fill="#fff"/><text x="180" y="16" font-size="11" text-anchor="middle" font-weight="bold" fill="#0b5b6a">Anti-termite measures — IS 6313</text>
<g font-size="5.5">
<text x="18" y="40">Pre-construction: clear roots, soil poison chlorpyrifos 1% under foundation and plinth 5L/m2, 7.5L/m2 wall-floor joint</text>
<text x="18" y="54">Physical: metal shield on plinth, no wood-soil contact, ventilate, keep dry</text>
<text x="18" y="68">Post-construction: drill holes 300mm deep at wall floor, inject chemical, 300mm apart</text>
<text x="18" y="82">Maintain: no leak, inspect yearly, retreat 5 years</text>
<text x="18" y="100" font-size="6" fill="#c00">Safety: wear mask, keep children food away — many chemicals banned, use approved low toxicity</text>
</g>"""

THERMAL_SVG="""<rect width="360" height="220" fill="#fff"/><text x="180" y="16" font-size="11" text-anchor="middle" font-weight="bold" fill="#0b5b6a">Thermal insulating materials — requirements of good</text>
<g font-size="6">
<rect x="15" y="38" width="80" height="30" rx="6" fill="#eaf4fa" stroke="#0b5b6a"/><text x="55" y="50" text-anchor="middle">Low k &lt;0.07</text><text x="55" y="60" text-anchor="middle">trapped air</text>
<rect x="105" y="38" width="80" height="30" rx="6" fill="#fff4e0" stroke="#b77e24"/><text x="145" y="50" text-anchor="middle">Light, porous</text><text x="145" y="60" text-anchor="middle">cork, fibre board</text>
<rect x="195" y="38" width="80" height="30" rx="6" fill="#f1fbf6" stroke="#77a795"/><text x="235" y="50" text-anchor="middle">Moisture proof</text><text x="235" y="60" text-anchor="middle">not lose k</text>
<rect x="285" y="38" width="65" height="30" rx="6" fill="#fce9e9" stroke="#c00"/><text x="317" y="50" text-anchor="middle">Fire proof</text>
<text x="18" y="88" font-size="6">Materials: cork, mineral wool, glass wool, polyurethane foam, AAC, gypsum board — roof walls cold store</text>
</g>"""

PAINT_SVG="""<rect width="360" height="220" fill="#fff"/><text x="180" y="16" font-size="11" text-anchor="middle" font-weight="bold" fill="#0b5b6a">Good paint characteristics</text>
<g font-size="6">
<text x="18" y="40">• Bright colour, high opacity, easy brush, quick dry 24h</text>
<text x="18" y="52">• Adhesive to surface, tough elastic no crack, washable</text>
<text x="18" y="64">• No fading, resists moisture fungi, cheap maintainable</text>
<rect x="18" y="78" width="80" height="26" rx="5" fill="#eaf4fa" stroke="#0b5b6a"/><text x="58" y="94" text-anchor="middle">Base lead/titanium</text>
<rect x="105" y="78" width="80" height="26" rx="5" fill="#fff4e0" stroke="#b77e24"/><text x="145" y="94" text-anchor="middle">Binder oil/alkyd</text>
<rect x="192" y="78" width="80" height="26" rx="5" fill="#f1fbf6" stroke="#77a795"/><text x="232" y="94" text-anchor="middle">Solvent turpentine</text>
<rect x="279" y="78" width="65" height="26" rx="5" fill="#fce9e9" stroke="#c00"/><text x="311" y="94" text-anchor="middle">Pigment/drier</text>
</g>"""

GEO_SVG="""<rect width="360" height="220" fill="#fff"/><text x="180" y="16" font-size="11" text-anchor="middle" font-weight="bold" fill="#0b5b6a">Geosynthetics — uses</text>
<g font-size="6">
<rect x="15" y="38" width="80" height="30" rx="6" fill="#eaf4fa" stroke="#0b5b6a"/><text x="55" y="50" text-anchor="middle">Geotextile</text><text x="55" y="60" text-anchor="middle">filter, separation</text>
<rect x="105" y="38" width="80" height="30" rx="6" fill="#fff4e0" stroke="#b77e24"/><text x="145" y="50" text-anchor="middle">Geomembrane</text><text x="145" y="60" text-anchor="middle">impermeable liner</text>
<rect x="195" y="38" width="80" height="30" rx="6" fill="#f1fbf6" stroke="#77a795"/><text x="235" y="50" text-anchor="middle">Geogrid</text><text x="235" y="60" text-anchor="middle">strength slope</text>
<rect x="285" y="38" width="60" height="30" rx="6" fill="#fce9e9" stroke="#c00"/><text x="315" y="50" text-anchor="middle">Geocell</text>
<text x="18" y="90" font-size="6">Polymer mats: road subgrade, retaining wall, canal lining, pond, drainage — cheap vs stone filter, long life if UV protected</text>
</g>"""

WASTE_SVG="""<rect width="360" height="220" fill="#fff"/><text x="180" y="16" font-size="11" text-anchor="middle" font-weight="bold" fill="#0b5b6a">Industrial waste materials in construction</text>
<g font-size="5.5">
<text x="12" y="40">Fly ash — from thermal power, replaces 20-35% cement in concrete, makes workable low heat</text>
<text x="12" y="52">GGBS — blast furnace slag, in slag cement, high durability sulphate resistant</text>
<text x="12" y="64">Red mud — from aluminium, for bricks tiles low strength</text>
<text x="12" y="76">Marble slurry — fine filler in tiles</text>
<text x="12" y="88">Rice husk ash — pozzolana, silica fume ultra fine for high strength</text>
<text x="12" y="100">Use saves landfill, but test for leaching, radioactivity — as per IS 3812, 12089</text>
</g>"""


SECTIONS=[
{
 "title_en":"Q1 · Eco materials and lime",
 "title_gu":"પ્ર.1 · ઇકો મટીરિયલ અને ચૂનો",
 "cards":[
  {
   "q_en":"Q.1 (a) Prepare a list of eco-friendly construction materials. (3 marks)",
   "marks_en":"3 marks","marks_gu":"૦૩ ગુણ",
   "a_en":"""<p><strong>Eco-friendly means low embodied energy, renewable and recyclable.</strong></p><table><tr><th>Material</th><th>Eco reason</th></tr><tr><td>Bamboo, FSC timber</td><td>Fast growing, CO2 stored</td></tr><tr><td>Fly ash bricks, GGBS concrete, AAC blocks</td><td>Uses waste, less cement, light</td></tr><tr><td>CSEB, rammed earth, mud plaster</td><td>Local soil, no burn</td></tr><tr><td>Recycled aggregate, reclaimed wood, steel</td><td>Saves quarry, reuse</td></tr><tr><td>Low VOC paint, lime wash, natural oil varnish</td><td>No toxic fumes</td></tr></table>""" + svg_wrap(ECO_SVG,"Eco list — bamboo, fly ash, earth, recycled, low VOC","Eco-friendly"),
   "a_gu":"""<p><strong>Eco-friendly એટલે ઓછી ઉર્જા, ફરી ઉગે અને ફરી વપરાય.</strong></p><table><tr><th>સામગ્રી</th><th>Eco કારણ</th></tr><tr><td>Bamboo, FSC timber</td><td>ઝડપી ઉગે, CO2 સંગ્રહ</td></tr><tr><td>Fly ash brick, GGBS concrete, AAC block</td><td>કચરો વપરાય, સિમેન્ટ ઓછો</td></tr><tr><td>CSEB, rammed earth, માટી પ્લાસ્ટર</td><td>સ્થાનિક માટી, દહન નહિ</td></tr><tr><td>Recycled aggregate, જૂનું લાકડું સ્ટીલ</td><td>ખાણ બચે</td></tr><tr><td>Low VOC paint, lime wash</td><td>ઝેરી ધુમાડો નહિ</td></tr></table>""" + svg_wrap(ECO_SVG,"Eco યાદી — bamboo fly ash માટી recycled low VOC","Eco-friendly"),
  },
  {
   "q_en":"Q.1 (b) Enlist and explain recycled construction materials. (4 marks)",
   "marks_en":"4 marks","marks_gu":"૦૪ ગુણ",
   "a_en":"""<p><strong>Recycled from C&D waste and industry:</strong></p><ul><li><strong>Recycled aggregate:</strong> Crusher breaks old concrete, sieved to 20mm, used in sub base and non structural concrete.</li><li><strong>Fly ash, GGBS:</strong> Power/steel waste as partial cement, improves workability.</li><li><strong>Reclaimed timber, steel, bricks:</strong> Direct reuse after cleaning.</li><li><strong>Glass cullet for tiles, plastic for paver blocks, rubber for asphalt.</strong></li></ul><p>Need testing per IS 383 — limit 20% replacement in structural concrete, save nature and landfill.</p>""" + svg_wrap(RECYCLE_SVG,"Recycle flow — demolition → crusher → reuse as aggregate, steel, tiles","Recycled"),
   "a_gu":"""<p><strong>C&D અને ઉદ્યોગ કચરા માંથી:</strong></p><ul><li><strong>Recycled aggregate:</strong> જૂનો કોંક્રિટ crusher માં ભાંગી 20mm કરી sub base અને સામાન્ય કોંક્રિટ માં.</li><li><strong>Fly ash GGBS:</strong> પાવર સ્ટીલ કચરો સિમેન્ટ માં 20-35% વાપરો, કામ સરળ.</li><li><strong>જૂનું લાકડું સ્ટીલ ઈંટ:</strong> સાફ કરી સીધું વાપરો.</li><li><strong>કાચ tiles માં, પ્લાસ્ટિક paver માં.</strong></li></ul><p>IS 383 પ્રમાણે તપાસ — structure માં 20% થી વધુ નહિ, પ્રકૃતિ અને landfill બચે.</p>""" + svg_wrap(RECYCLE_SVG,"Recycle પ્રવાહ — તોડકામ → crusher → aggregate steel tiles","Recycled"),
  },
  {
   "q_en":"Q.1 (c) Explain slaking and setting of lime. (7 marks)",
   "marks_en":"7 marks","marks_gu":"૦૭ ગુણ",
   "a_en":"""<p><strong>Calcination:</strong> CaCO3 heated 900°C → CaO quick lime + CO2.</p><p><strong>Slaking:</strong> CaO + H2O → Ca(OH)2 slaked lime + heat ~65 kJ per mol. Quick lime hisses, cracks, swells 2.5 times, needs gentle water sprinkling and maturing 3 days in pit. Fat lime slakes vigorously, hydraulic slowly.</p><p><strong>Setting/hardening:</strong> Ca(OH)2 paste exposed to air reacts Ca(OH)2 + CO2 → CaCO3 + H2O — carbonation forms hard limestone again, months, needs air and little moisture. Hydraulic lime also forms calcium silicate hydrates under water, so sets even without air — used for foundations.</p>""" + svg_wrap(LIME_SVG,"CaO + water → Ca(OH)2 slaking with heat, then + CO2 → CaCO3 setting","Lime slaking"),
   "a_gu":"""<p><strong>Calcination:</strong> CaCO3 900°C એ CaO + CO2.</p><p><strong>Slaking:</strong> CaO + H2O → Ca(OH)2 + ગરમી. CaO પાણી મળતા ફૂંફાડા તિરાડ અને 2.5 ગણું ફૂલે, ધીમે પાણી છાંટી 3 દિવસ પાકવા દો. fat lime ઝડપી hydraulic ધીમું.</p><p><strong>Setting:</strong> Ca(OH)2 હવા માં CO2 સાથે Ca(OH)2 + CO2 → CaCO3 + H2O — પાછું સખત ચૂનો બને મહિના લાગે, હવા જોઈએ. hydraulic lime પાણી માં પણ silicate થી સખત થાય — પાયા માટે.</p>""" + svg_wrap(LIME_SVG,"CaO + પાણી → Ca(OH)2 ગરમી, પછી CO2 → CaCO3 સખત","Lime slaking"),
  },
  {
   "q_en":"Q.1 (c) OR Explain seasoning of Timber. (7 marks)",
   "marks_en":"7 marks","marks_gu":"૦૭ ગુણ",
   "a_en":"""<p><strong>Seasoning is drying timber from 50% moisture to 12-14% for use.</strong> Fresh wood shrinks, warps and rots.</p><p><strong>Purpose:</strong> Prevent shrinkage cracks, increase strength and hardness, make light, allow paint polish, protect from fungi insects, improve workability.</p><p><strong>Methods:</strong> Natural — stack planks with spacers in shade with airflow 6 months to 2 years, cheap but slow. Artificial — kiln chamber controls temp 40-90°C and humidity, 10-20 days fast and uniform. Chemical salt, boiling or water soaking leach sap.</p><p>Kiln seasoning best for furniture, natural for beams. Test by weighing till constant and moisture meter.</p>""" + svg_wrap(SEASON_SVG,"Seasoning purpose and methods — natural 6 months vs kiln 10 days","Seasoning"),
   "a_gu":"""<p><strong>Seasoning એટલે લાકડા માં ભેજ 50% થી 12-14% સુધી સુકવવું.</strong> તાજું લાકડું સંકોચાય, વળે, સડે.</p><p><strong>હેતુ:</strong> સંકોચ તિરાડ રોકે, મજબૂત સખત બનાવે, હલકું કરે, paint polish લાગે, ફૂગ જીવડાં રોકે.</p><p><strong>રીત:</strong> Natural — પાટિયા વચ્ચે ટેકા છાંયા હવા માં 6 મહિના થી 2 વર્ષ, સસ્તી ધીમી. Kiln — ચેમ્બર 40-90°C અને ભેજ કંટ્રોલ 10-20 દિવસ ઝડપી. chemical, પાણી ઉકાળવું.</p><p>ફર્નિચર માટે kiln, beam માટે natural, વજન સ્થિર થાય ત્યાં સુધી તપાસો.</p>""" + svg_wrap(SEASON_SVG,"Seasoning હેતુ રીત — natural 6 મહિના kiln 10 દિવસ","Seasoning"),
  },
 ]
},
{
 "title_en":"Q2 · Timber and aggregate",
 "title_gu":"પ્ર.2 · ટિમ્બર અને એગ્રીગેટ",
 "cards":[
  {
   "q_en":"Q.2 (a) Explain Construction material in Transportation Engineering. (3 marks)",
   "marks_en":"3 marks","marks_gu":"૦૩ ગુણ",
   "a_en":"""<ul><li><strong>Roads:</strong> Aggregate base, bitumen binder, cement concrete slab, geosynthetics for subgrade.</li><li><strong>Bridges:</strong> High strength concrete, steel girders, prestressing strands, elastomeric bearings.</li><li><strong>Rail:</strong> Ballast stone 50mm, sleepers RCC or steel, rails high carbon steel.</li></ul><p>Need hard abrasion resistant aggregate, ductile bitumen, durable concrete against water and load repetitions.</p>""",
   "a_gu":"""<ul><li><strong>રસ્તા:</strong> aggregate base, bitumen binder, સિમેન્ટ slab, geosynthetics.</li><li><strong>પુલ:</strong> મજબૂત કોંક્રિટ સ્ટીલ girder prestress.</li><li><strong>રેલ:</strong> ballast 50mm, sleeper RCC, rail high carbon સ્ટીલ.</li></ul><p>સખત abrasion સહન aggregate, લચીલું bitumen, પાણી અને વારંવાર લોડ સહન કોંક્રિટ જોઈએ.</p>""",
  },
  {
   "q_en":"Q.2 (b) Draw a cross section of exogenous tree and explain its various parts. (4 marks)",
   "marks_en":"4 marks","marks_gu":"૦૪ ગુણ",
   "a_en":"""<ul><li><strong>Bark outer + inner:</strong> Protection and food transport.</li><li><strong>Cambium layer:</strong> Thin growth zone makes new wood each year.</li><li><strong>Sapwood:</strong> Light outer rings carry water, less durable.</li><li><strong>Heartwood:</strong> Dark central strong durable gives structure.</li><li><strong>Medullary rays:</strong> Radial lines carry nutrients, add shear strength.</li><li><strong>Pith:</strong> Soft centre, weak, often removed.</li></ul>""" + svg_wrap(TREE_SVG,"Bark cambium sapwood heartwood rays pith — exogenous grows outward","Tree section"),
   "a_gu":"""<ul><li><strong>Bark બહાર અંદર:</strong> રક્ષણ અને ખોરાક વહન.</li><li><strong>Cambium:</strong> પાતળો વૃદ્ધિ સ્તર દર વર્ષે નવું લાકડું.</li><li><strong>Sapwood:</strong> આછું પાણી વહન, ઓછું ટકાઉ.</li><li><strong>Heartwood:</strong> ઘાટું મજબૂત ટકાઉ મુખ્ય ભાગ.</li><li><strong>Medullary rays:</strong> ત્રિજ્યા રેખા પોષણ વહન.</li><li><strong>Pith:</strong> નરમ મધ્ય નબળો.</li></ul>""" + svg_wrap(TREE_SVG,"Bark cambium sapwood heartwood rays pith — બહાર વૃદ્ધિ","Tree section"),
  },
  {
   "q_en":"Q.2 (c) Explain defects in timber with neat sketches. (7 marks)",
   "marks_en":"7 marks","marks_gu":"૦૭ ગુણ",
   "a_en":"""<p><strong>Conversion defects:</strong> Knot — branch base hard circle weakens, warp bow twist from uneven drying, wane missing edge.</p><p><strong>Natural:</strong> Shake — split along grain ring shake cup shake, twisted grain.</p><p><strong>Biodeterioration:</strong> Fungal rot — brown white decay soft, sap stain, insect beetle holes reduce strength.</p><p>Select clear straight grain, season well, treat with creosote to avoid.</p>""" + svg_wrap(DEFECT_SVG,"Knot shake warp fungal — natural, conversion and biological defects","Timber defects"),
   "a_gu":"""<p><strong>Conversion:</strong> Knot — ડાળી ગાંઠ સખત નબળું પાડે, warp ધનુષ વળાંક અસમાન સુકવણી થી.</p><p><strong>Natural:</strong> Shake — અનાજ સાથે ચિરો, vank twisted fibre.</p><p><strong>જીવ:</strong> ફૂગ સડો ભુરો સફેદ નરમ, beetle કાણાં.</p><p>સીધું ગાંઠ વગર લાકડું પસંદ કરો, સારી seasoning, creosote થી બચાવો.</p>""" + svg_wrap(DEFECT_SVG,"Knot shake warp fungal — કુદરતી conversion જૈવ ખામી","Timber defects"),
  },
  {
   "q_en":"Q.2 (a) OR Explain Construction material us in Irrigation Engineering. (3 marks)",
   "marks_en":"3 marks","marks_gu":"૦૩ ગુણ",
   "a_en":"""<ul><li><strong>Dams/canals:</strong> Impervious clay core, stone riprap pitching, concrete lining M15, geomembrane to stop seepage.</li><li><strong>Gates:</strong> Mild steel, stainless for corrosion, rubber seals.</li><li>Need water tightness, erosion resistance, durability under wet dry cycles.</li></ul>""",
   "a_gu":"""<ul><li><strong>ડેમ કેનાલ:</strong> impermeable માટી core, પથ્થર pitching, કોંક્રિટ lining M15, geomembrane seepage રોકે.</li><li><strong>દરવાજા:</strong> mild steel stainless કાટ રોકે rubber seal.</li><li>પાણી રોકવાની ક્ષમતા, ઘસારો પ્રતિકાર, ભીનું સૂકું ટકાઉપણું જોઈએ.</li></ul>""",
  },
  {
   "q_en":"Q.2 (b) OR Enlist requirements of good building stones. (4 marks)",
   "marks_en":"4 marks","marks_gu":"૦૪ ગુણ",
   "a_en":"""<ul><li>High crushing strength 60 MPa above, hardness to resist wear, toughness against impact.</li><li>Low water absorption below 5%, low porosity, high durability against frost and acid.</li><li>Workable, seasons well, cheap locally, good appearance, free from soft patches.</li><li>Specific gravity about 2.7, does not weather or flake, fire resistant for important works.</li></ul>""",
   "a_gu":"""<ul><li>crushing તાકાત 60 MPa થી વધુ, hardness ઘસારો સહે, toughness ઝટકો સહે.</li><li>પાણી શોષણ 5% થી ઓછું, છિદ્રાળુતા ઓછી, frost acid સામે ટકાઉ.</li><li>કામ સરળ, સસ્તું નજીક, દેખાવ સારો, નરમ ડાઘ નહિ.</li><li>ગુણ 2.7, weathering નહિ, fire પ્રતિરોધક.</li></ul>""",
  },
  {
   "q_en":"Q.2 (c) OR Explain classification of aggregate based on size. (7 marks)",
   "marks_en":"7 marks","marks_gu":"૦૭ ગુણ",
   "a_en":"""<p><strong>As per IS 383 by sieve:</strong></p><table><tr><th>Type</th><th>Size</th><th>Use</th></tr><tr><td>Fine aggregate</td><td>Pass 4.75mm, sand zone I coarse to IV fine</td><td>Fills voids, mortar</td></tr><tr><td>Coarse aggregate</td><td>Retain 4.75mm: 10mm, 20mm, 40mm nominal</td><td>Concrete bulk volume</td></tr><tr><td>All-in aggregate</td><td>0.075 to 40mm graded continuous</td><td>Mass filling</td></tr><tr><td>Single sized vs graded</td><td>Gap graded no intermediate, well graded all fractions</td><td>Well graded gives dense strong concrete</td></tr></table><p>Grading influences workability and strength — Fuller max density curve guides ideal mix.</p>""" + svg_wrap(AGG_SVG,"Fine under 4.75mm sand vs coarse over 4.75mm — grading makes dense concrete","Aggregate size"),
   "a_gu":"""<p><strong>IS 383 sieve પ્રમાણે:</strong></p><table><tr><th>પ્રકાર</th><th>કદ</th><th>ઉપયોગ</th></tr><tr><td>Fine aggregate</td><td>4.75mm નીચે રેતી zone I થી IV</td><td>ખાલી પૂરે mortar</td></tr><tr><td>Coarse aggregate</td><td>4.75mm ઉપર 10 20 40mm</td><td>કોંક્રિટ જથ્થો</td></tr><tr><td>All-in</td><td>0.075 થી 40mm સતત</td><td>mass filling</td></tr></table><p>Grading થી workability તાકાત — Fuller curve આદર્શ મિશ્રણ બતાવે.</p>""" + svg_wrap(AGG_SVG,"Fine 4.75mm નીચે vs coarse ઉપર — grading થી ઘન કોંક્રિટ","Aggregate size"),
  },
 ]
},
{
 "title_en":"Q3 · Bricks and kilns",
 "title_gu":"પ્ર.3 · ઈંટ અને ભઠ્ઠી",
 "cards":[
  {
   "q_en":"Q.3 (a) Explain cutback and emulsion. (3 marks)",
   "marks_en":"3 marks","marks_gu":"૦૩ ગુણ",
   "a_en":"""<p><strong>Cutback bitumen:</strong> Hot bitumen thinned with volatile solvent kerosene or diesel, cold applied, solvent evaporates leaves bond. Types RC rapid cure with petrol, MC medium with kerosene, SC slow with diesel. Used tack coat prime coat in cold weather.</p><p><strong>Emulsion:</strong> Bitumen droplets 55% suspended in water with emulsifier soap, brown liquid cold applied, water breaks leaving black film. No heating fire safe. Types RS rapid set for surface dressing, MS for mix, SS slow for crack filler. Cold safe but strength slower.</p>""",
   "a_gu":"""<p><strong>Cutback:</strong> ગરમ bitumen માં kerosene diesel ભેળવી પાતળું ઠંડું લગાડો, solvent ઉડી જાય bond રહે. RC ઝડપી petrol MC kerosene SC ધીમું diesel. tack coat prime coat ઠંડા હવામાન માં.</p><p><strong>Emulsion:</strong> bitumen ટીપાં 55% પાણી માં સાબુ emulsifier થી, ભૂરું પ્રવાહી ઠંડું લગાડો પાણી છૂટું પડી કાળી ફિલ્મ. ગરમી આગ નહિ. RS ઝડપી surface MS mix SS તિરાડ. ઠંડું સલામત પણ તાકાત ધીમી.</p>""",
  },
  {
   "q_en":"Q.3 (b) Draw flow diagram for manufacturing process of bricks. (4 marks)",
   "marks_en":"4 marks","marks_gu":"૦૪ ગુણ",
   "a_en":"""<p><strong>Steps:</strong> 1 Unsoiling remove top soil, 2 Digging, 3 Weathering 1 month, 4 Blending with ash, 5 Tempering knead with water to plastic, 6 Moulding hand/machine, 7 Drying shade 7 days, 8 Burning, 9 Sorting. Ideal clay 30% alumina 50% silica, free from lime nodules and organics.</p>""" + svg_wrap(BRICKMFG_SVG,"Clay prep → mould → dry → burn → sort — 19×9×9cm standard","Brick flow"),
   "a_gu":"""<p><strong>પગલાં:</strong> 1 ઉપર માટી કાઢો 2 ખોદો 3 એક મહિનો weather 4 ash ભેળવો 5 પાણી થી temper 6 mould 7 છાંયા 7 દિવસ суકવો 8 દહન 9 વર્ગીકરણ. સારી માટી 30% alumina 50% silica ચૂના ગાંઠ નહિ.</p>""" + svg_wrap(BRICKMFG_SVG,"માટી તૈયાર → mould → સૂકવો → દહન → વર્ગીકરણ","Brick flow"),
  },
  {
   "q_en":"Q.3 (c) Explain Hoffman’s Kiln with neat sketch. (7 marks)",
   "marks_en":"7 marks","marks_gu":"૦૭ ગુણ",
   "a_en":"""<p><strong>Hoffman kiln is continuous circular of 12 chambers around central chimney.</strong> Green bricks stacked in drying chamber use waste heat from burning chamber to dry. Next chamber burning at 1100°C via top fuel holes and draught. Next cooling — incoming air cools fired bricks and preheats combustion air. Fire moves one chamber per day, bricks stay, cycle repeats year round.</p><p><strong>Advantages:</strong> Fuel 40% less than clamp, quality uniform, capacity high 20,000 per day, weather independent, continuous supply. Disadvantage high initial cost needs permanent building and skilled operation.</p>""" + svg_wrap(HOFFMAN_SVG,"12 chambers ring — drying with waste heat → burning 1100°C → cooling preheats air","Hoffman kiln"),
   "a_gu":"""<p><strong>Hoffman ભઠ્ઠી 12 ચેમ્બર વાળી ગોળાકાર વચ્ચે ચીમની.</strong> લીલી ઈંટ суકવણી ચેમ્બર માં સળગતી ગરમી થી суકાય. પછી burning 1100°C ઉપર થી fuel છિદ્ર અને ખેંચાણ. પછી cooling હવા પાકી ઈંટ ઠંડી કરી combustion હવા ગરમ કરે. આગ દરરોજ એક ચેમ્બર ખસે ઈંટ સ્થિર, આખું વર્ષ સતત.</p><p><strong>ફાયદા:</strong> clamp કરતાં 40% fuel ઓછો, ગુણવત્તા એકસરખી, 20,000 પ્રતિ દિવસ, હવામાન અસર નહિ. ગેરલાભ બાંધકામ ખર્ચ વધુ.</p>""" + svg_wrap(HOFFMAN_SVG,"12 ચેમ્બર ring — waste heat суકવણી → 1100°C દહન → ઠંડક હવા ગરમ","Hoffman kiln"),
  },
  {
   "q_en":"Q.3 (a) OR Enlist properties of good sand. (3 marks)",
   "marks_en":"3 marks","marks_gu":"૦૩ ગુણ",
   "a_en":"""<ul><li>Clean coarse well graded, free from clay, silt below 3%, organic colour test light.</li><li>Hard sharp angular grains, not rounded sea sand, low absorption.</li><li>Sound strong, grading zone II ideal, fineness modulus 2.6 to 2.9.</li></ul>""",
   "a_gu":"""<ul><li>સ્વચ્છ coarse સારી grading, clay silt 3% થી ઓછું organic હલકો રંગ.</li><li>સખત તીક્ષ્ણ angular, ગોળ દરિયા રેતી નહિ, શોષણ ઓછું.</li><li>મજબૂત, zone II શ્રેષ્ઠ, fineness 2.6 થી 2.9.</li></ul>""",
  },
  {
   "q_en":"Q.3 (b) OR Write merits and demerits of aerated concrete blocks. (4 marks)",
   "marks_en":"4 marks","marks_gu":"૦૪ ગુણ",
   "a_en":"""<p><strong>AAC blocks are light cellular with air 60%:</strong> Merits — light 1/3 brick weight, thermal insulating, fire 4 hrs, easy cut, earthquake light, fast masonry. Demerits — compressive 3 MPa low vs brick 7, cost higher per piece, needs thin bed mortar and plaster care, water absorption higher if not coated, not for foundation water contact.</p>""",
   "a_gu":"""<p><strong>AAC હવા 60% હલકો:</strong> ફાયદા — ઈંટ થી 1/3 વજન, thermal રોકે, fire 4 કલાક, કાપવો સરળ, ભૂકંપ હલકો, ઝડપી. ગેરલાભ — તાકાત 3 MPa ઈંટ 7 કરતાં ઓછી, કિંમત વધુ, thin bed mortar જોઈએ, પાણી શોષણ વધુ પાયા માં નહિ.</p>""",
  },
  {
   "q_en":"Q.3 (c) OR Compare between 'Clamp Burning and Kiln Burning'. (7 marks)",
   "marks_en":"7 marks","marks_gu":"૦૭ ગુણ",
   "a_en":"""<table><tr><th>Point</th><th>Clamp</th><th>Kiln Hoffman</th></tr><tr><td>Structure</td><td>Temporary stack on ground with fuel layers</td><td>Permanent brick building 12 chambers circular</td></tr><tr><td>Operation</td><td>Intermittent 15+10 days one batch</td><td>Continuous fire moves daily, year round supply</td></tr><tr><td>Fuel</td><td>More, heat waste</td><td>40% less, waste heat reuse</td></tr><tr><td>Quality</td><td>Uneven 25% over/under burnt, mix</td><td>Uniform controlled 1100°C</td></tr><tr><td>Cost</td><td>Low start, labour high</td><td>High build but cheap per 1000 for large</td></tr></table>""" + svg_wrap(CLAMP_KILN_SVG,"Clamp temporary intermittent vs kiln permanent continuous","Clamp kiln"),
   "a_gu":"""<table><tr><th>મુદ્દો</th><th>Clamp</th><th>Kiln Hoffman</th></tr><tr><td>બાંધકામ</td><td>જમીન પર કામચલાઉ ઢગ fuel સાથે</td><td>કાયમી 12 ચેમ્બર ગોળ ઇમારત</td></tr><tr><td>ચલાવપ</td><td>રુકી રુકી 15+10 દિવસ એક batch</td><td>સતત આગ દરરોજ ખસે</td></tr><tr><td>fuel</td><td>વધુ ગરમી બગડે</td><td>40% ઓછો reuse</td></tr><tr><td>ગુણવત્તા</td><td>અસમાન 25% કાચી પાકી ભેળ</td><td>એકસરખી 1100°C</td></tr></table>""" + svg_wrap(CLAMP_KILN_SVG,"Clamp કામચલાઉ રુકી vs kiln કાયમી સતત","Clamp kiln"),
  },
 ]
},
{
 "title_en":"Q4 · Bricks, cement and glass",
 "title_gu":"પ્ર.4 · ઈંટ સિમેન્ટ અને કાચ",
 "cards":[
  {
   "q_en":"Q.4 (a) Define the terms: (1) Queen closer (2) King closer (3) Bat. (3 marks)",
   "marks_en":"3 marks","marks_gu":"૦૩ ગુણ",
   "a_en":"""<p><strong>Queen closer:</strong> Brick cut lengthwise into two halves 19×4.5×9cm, placed next to quoin header to maintain bond and avoid continuous vertical joints. Width half.</p><p><strong>King closer:</strong> Corner cut off one side forming splayed jamb, piece size 19×9 with triangle notch 4.5cm, used for chamfered corners.</p><p><strong>Bat:</strong> Brick cut across width — 3/4 bat 14.25cm long, 1/2 bat 9.5cm, used to adjust bond lengths.</p>""" + svg_wrap(BRICKCUT_SVG,"Queen lengthwise half, King splayed L, Bat across width","Brick cuts"),
   "a_gu":"""<p><strong>Queen closer:</strong> ઈંટ લંબાઈ એ બે ભાગ 19×4.5×9cm, quoin header પાસે bond જાળવવા. પહોળાઈ અડધી.</p><p><strong>King closer:</strong> ખૂણો કપાય બાજુ chamfer, 19×9 ત્રિકોણ notch 4.5cm.</p><p><strong>Bat:</strong> પહોળાઈ એ કાપ — 3/4 bat 14.25cm, 1/2 bat 9.5cm, bond લંબાઈ ગોઠવવા.</p>""" + svg_wrap(BRICKCUT_SVG,"Queen લંબાઈ અડધી King ત્રાંસો Bat પહોળાઈ કાપ","Brick cuts"),
  },
  {
   "q_en":"Q.4 (b) Explain in detail: Anti termite measures. (4 marks)",
   "marks_en":"4 marks","marks_gu":"૦૪ ગુણ",
   "a_en":"""<p><strong>As per IS 6313:</strong> Pre-construction soil treatment — clear roots, spray chlorpyrifos or imidacloprid approved 1% at 5 L per sqm under foundation, 7.5 L per sqm at wall floor joint, plus around plinth. Physical barrier metal shield, no wood soil contact, ventilate crawl space dry. Post-construction drill 300mm holes at wall floor every 300mm inject chemical. Regular inspection, leaky pipes fix, retreat 5 years.</p>""" + svg_wrap(ANTITERM_SVG,"Soil poison under foundation and wall floor joint plus physical barrier","Anti termite"),
   "a_gu":"""<p><strong>IS 6313 પ્રમાણે:</strong> બાંધકામ પહેલા માટી poison — મૂળ સાફ, foundation નીચે 5 L/m2, દીવાલ ફ્લોર સાંધા 7.5 L/m2, plinth ફરતે. ધાતુ shield, લાકડું જમીન અડે નહિ, હવાદાર સૂકું રાખો. પછી દીવાલ ફ્લોર પર 300mm કાણાં 300mm અંતરે chemical. નિયમિત તપાસ લીક રિપેર 5 વર્ષે ફરી.</p>""" + svg_wrap(ANTITERM_SVG,"Foundation નીચે અને દીવાલ ફ્લોર સાંધા poison barrier","Anti termite"),
  },
  {
   "q_en":"Q.4 (c) Draw the flow diagram for manufacturing of cement by dry process. (7 marks)",
   "marks_en":"7 marks","marks_gu":"૦૭ ગુણ",
   "a_en":"""<p><strong>Dry process modern:</strong> Limestone crushed → raw mill grind dry powder → cyclone preheater 800°C → rotary kiln 1450°C where calcination and clinker formation C3S, C2S, C3A → cooler → grind clinker with 3% gypsum to retard set → cement packed.</p><p>Fuel consumption about 100 kg coal per ton vs wet 250, dust bag filter needed, quality uniform.</p>""" + svg_wrap(CEMENT_DRY_SVG,"Crush → grind raw → preheat 800°C → kiln 1450°C → grind + gypsum cement","Cement dry"),
   "a_gu":"""<p><strong>Dry process આધુનિક:</strong> ચૂના પથ્થર ભાંગો → raw mill સૂકો પાઉડર → cyclone 800°C → rotary kiln 1450°C calcination clinker C3S C2S → cooler → 3% gypsum સાથે દળો cement.</p><p>fuel 100 kg/ટન wet માં 250, bag filter જોઈએ, ગુણવત્તા એકસરખી.</p>""" + svg_wrap(CEMENT_DRY_SVG,"ભાંગો → raw grind → 800°C preheat → 1450°C kiln → gypsum દળો","Cement dry"),
  },
  {
   "q_en":"Q.4 (a) OR Enlist properties of glass. (3 marks)",
   "marks_en":"3 marks","marks_gu":"૦૩ ગુણ",
   "a_en":"""<ul><li>Transparent to translucent, hard brittle, takes high polish.</li><li>High compressive strength, low tensile, good electrical insulator.</li><li>Chemical resistant except HF, not affected by air water, recyclable but weather not.</li><li>Can be drawn to fibres, available as toughened, laminated.</li></ul>""",
   "a_gu":"""<ul><li>પારદર્શક, સખત બરડ, polish થાય.</li><li>crush તાકાત વધુ tensile ઓછી, insulator.</li><li>HF સિવાય chemical ટકાઉ, હવા પાણી અસર નહિ, recyclable.</li><li>fibre થાય, toughened laminated મળે.</li></ul>""",
  },
  {
   "q_en":"Q.4 (b) OR Explain glass fibres and plastic fibres. (4 marks)",
   "marks_en":"4 marks","marks_gu":"૦૪ ગુણ",
   "a_en":"""<p><strong>Glass fibres:</strong> Molten glass drawn to 10 micron filaments, woven mat, high tensile 1000 MPa, alkali sensitive so use AR glass in concrete for crack control, in GRP tanks pipes.</p><p><strong>Plastic fibres:</strong> Polypropylene PP 12mm chopped strands dosed 0.6 kg/m3 in concrete reduce plastic shrinkage cracks, improve impact, not for structural strength. Nylon etc for flooring.</p>""" + svg_wrap(GLASS_SVG,"Glass AR fibres for crack control vs PP fibres shrinkage control","Fibres"),
   "a_gu":"""<p><strong>Glass fibre:</strong> પીગળેલ કાચ થી 10 micron તાર, tensile 1000 MPa, AR glass કોંક્રિટ તિરાડ રોકે, GRP tank pipe.</p><p><strong>Plastic fibre:</strong> PP 12mm 0.6 kg/m3 તિરાડ ઘટાડે impact વધારે, structure તાકાત નહિ.</p>""" + svg_wrap(GLASS_SVG,"Glass તિરાડ રોકે vs PP shrinkage રોકે","Fibres"),
  },
  {
   "q_en":"Q.4 (c) OR Explain Properties and use of Ferrous Metals. (7 marks)",
   "marks_en":"7 marks","marks_gu":"૦૭ ગુણ",
   "a_en":"""<p><strong>Properties:</strong> Contain iron, high strength ductile magnetic, rusts, weldable, high melting ~1500°C, fatigue endurance.</p><table><tr><th>Metal</th><th>Property</th><th>Use</th></tr><tr><td>Mild steel 0.15% C</td><td>Ductile weldable</td><td>Rebar, beams, sheets, gates</td></tr><tr><td>Cast iron 3% C</td><td>Brittle castable compressive</td><td>Pipes, manhole covers, bases</td></tr><tr><td>Wrought iron</td><td>Fibrous rust resistant</td><td>Historic grill</td></tr><tr><td>Stainless 18% Cr</td><td>No rust</td><td>Kitchen, facade, railing</td></tr></table>""",
   "a_gu":"""<p><strong>ગુણ:</strong> લોખંડ વાળા, મજબૂત લચીલા ચુંબકીય, કાટ લાગે, weld થાય, 1500°C.</p><table><tr><th>ધાતુ</th><th>ગુણ</th><th>ઉપયોગ</th></tr><tr><td>Mild steel</td><td>લચીલું weld</td><td>saria beam sheet</td></tr><tr><td>Cast iron</td><td>બરડ cast, crush વધુ</td><td>pipe cover</td></tr><tr><td>Stainless</td><td>કાટ નહિ</td><td>kitchen railing</td></tr></table>""",
  },
 ]
},
{
 "title_en":"Q5 · Paints and special materials",
 "title_gu":"પ્ર.5 · રંગ અને ખાસ મટીરિયલ",
 "cards":[
  {
   "q_en":"Q.5 (a) Write short note on :Varnish (3 marks)",
   "marks_en":"3 marks","marks_gu":"૦૩ ગુણ",
   "a_en":"""<p><strong>Varnish is clear transparent coating without pigment:</strong> Resin copal or polyurethane dissolved in linseed oil plus turpentine solvent plus drier. Applied thin on wood to show grain, gives gloss water proof. Types oil, spirit, turpentine, water based. Apply 2 coats on clean dry sanded wood.</p>""",
   "a_gu":"""<p><strong>Varnish રંગ વગર પારદર્શક coating:</strong> resin linseed oil turpentine drier. લાકડા પર પાતળું grain દેખાય gloss પાણી રોકે. oil spirit water based 2 coat સાફ સૂકા ઘસેલા લાકડા પર.</p>""",
  },
  {
   "q_en":"Q.5 (b) Explain of good thermal insulating materials. (4 marks)",
   "marks_en":"4 marks","marks_gu":"૦૪ ગુણ",
   "a_en":"""<p><strong>Good thermal insulator has:</strong> Low thermal conductivity below 0.07 W per mK via trapped air, low density porous, moisture and fire resistant, durable light, cheap.</p><p><strong>Materials:</strong> Cork board, mineral wool, glass wool blanket, polyurethane foam spray, AAC wall, gypsum plaster, asbestos free boards. Use roof walls cold stores, pipe lagging, acoustic also.</p>""" + svg_wrap(THERMAL_SVG,"Low k under 0.07 with trapped air — cork wool foam AAC criteria","Thermal"),
   "a_gu":"""<p><strong>સારો thermal insulator:</strong> k 0.07 થી ઓછો trapped air થી, હલકો છિદ્રાળુ, ભેજ fire ટકાઉ, સસ્તું.</p><p><strong>સામગ્રી:</strong> cork mineral wool glass wool PU foam AAC wall gypsum. roof દીવાલ cold store pipe માં.</p>""" + svg_wrap(THERMAL_SVG,"k 0.07 થી ઓછો trapped air — cork wool foam AAC","Thermal"),
  },
  {
   "q_en":"Q.5 (c) Explain industrial waste materials. (7 marks)",
   "marks_en":"7 marks","marks_gu":"૦૭ ગુણ",
   "a_en":"""<p><strong>Reuse in cement concrete and bricks:</strong></p><ul><li><strong>Fly ash:</strong> From coal power, pozzolana, replaces 30% cement, improves workability reduces heat.</li><li><strong>GGBS:</strong> Steel slag granulated, in slag cement sulphate resistant for marine.</li><li><strong>Silica fume:</strong> Very fine from silicon industry, high strength concrete.</li><li><strong>Rice husk ash marble slurry red mud:</strong> For low cost bricks tiles filler.</li></ul><p>Must test for soundness and leaching per IS 3812 12089 — save resource and landfill.</p>""" + svg_wrap(WASTE_SVG,"Fly ash GGBS silica fume marble slurry rice husk — waste to resource","Waste"),
   "a_gu":"""<p><strong>સિમેન્ટ કોંક્રિટ ઈંટ માં reuse:</strong></p><ul><li><strong>Fly ash:</strong> કોલસા power થી 30% cement બદલે workability ગરમી ઓછી.</li><li><strong>GGBS:</strong> slag granulated marine sulphate ટકાઉ.</li><li><strong>Silica fume:</strong> અતિ ઝીણું high strength.</li><li><strong>Rice husk marble slurry red mud:</strong> સસ્તી ઈંટ filler.</li></ul><p>IS 3812 12089 તપાસ — સંસાધન landfill બચે.</p>""" + svg_wrap(WASTE_SVG,"Fly ash GGBS silica fume rice husk — કચરો સંસાધન","Waste"),
  },
  {
   "q_en":"Q.5 (a) OR Enlist characteristics of good paint. (3 marks)",
   "marks_en":"3 marks","marks_gu":"૦૩ ગુણ",
   "a_en":"""<ul><li>Good opacity covers, bright stable colour, easy to apply by brush, dries 24h no tack.</li><li>Tough elastic no crack, adhesive well, washable, resists moisture and fungi.</li><li>Durable no fading chalking 3 years, economical, can be recoated.</li></ul>""" + svg_wrap(PAINT_SVG,"Opacity bright easy adhesive washable durable — paint traits","Paint"),
   "a_gu":"""<ul><li>opacity ઢાંકે, રંગ તેજ સ્થિર, brush સરળ, 24h сукું.</li><li>ટકાઉ લચીલું તિરાડ નહિ, ચોંટે ધોવાય, ભેજ ફૂગ રોકે.</li><li>3 વર્ષ ટકે fading નહિ, સસ્તું ફરી લગાડી શકાય.</li></ul>""" + svg_wrap(PAINT_SVG,"opacity તેજ સરળ ચોંટે ધોવાય ટકાઉ — paint લક્ષણ","Paint"),
  },
  {
   "q_en":"Q.5 (b) OR Explain good sound insulating materials. (4 marks)",
   "marks_en":"4 marks","marks_gu":"૦૪ ગુણ",
   "a_en":"""<p><strong>Good sound insulator absorbs or reflects:</strong> Porous fibrous — mineral wool, glass wool, acoustic foam open cells; heavy dense — lead sheet, gypsum double layer; resilient — rubber mat decouples floor.</p><p>Criteria: high absorption NRC above 0.7 at 500Hz, non combustible, light, moisture resistant. Use theatre partition floor floating, ceiling false with air gap 100mm improves 40 dB loss.</p>""",
   "a_gu":"""<p><strong>સારું sound insulator શોષે કે પ્રતિબિંબે:</strong> છિદ્રાળુ mineral wool glass wool foam, ભારે lead sheet gypsum double, resilient rubber floor અલગ કરે.</p><p>NRC 0.7 થી વધુ 500Hz, non combustible, ભેજ ટકાઉ. theatre partition floating floor false ceiling 100mm gap 40 dB.</p>""",
  },
  {
   "q_en":"Q.5 (c) OR Explain Geosynthetics. (7 marks)",
   "marks_en":"7 marks","marks_gu":"૦૭ ગુણ",
   "a_en":"""<p><strong>Geosynthetics are polymer sheets used with soil:</strong></p><ul><li><strong>Geotextile:</strong> Woven nonwoven filter separates soil, in road subgrade and drain.</li><li><strong>Geomembrane:</strong> Impermeable LDPE HDPE 1mm liner for pond canal landfill top.</li><li><strong>Geogrid:</strong> Stiff grid reinforces embankment retaining wall.</li><li><strong>Geocell Geocomposite:</strong> Honeycomb confines soil on slope.</li></ol><p>Adv cheap vs graded filter, easy lay, functions — separation filtration drainage reinforcement protection. Need UV cover, proper overlap joints.</p>""" + svg_wrap(GEO_SVG,"Geotextile filter, geomembrane liner, geogrid strength, geocell slope","Geosynthetics"),
   "a_gu":"""<p><strong>Geosynthetics polymer sheet માટી સાથે:</strong></p><ul><li><strong>Geotextile:</strong> filter separation રસ્તા drain માં.</li><li><strong>Geomembrane:</strong> impermeable LDPE તળાવ કેનાલ landfill liner.</li><li><strong>Geogrid:</strong> સખત grid ઢોળાવ દીવાલ મજબૂત.</li><li><strong>Geocell:</strong> મધપૂડો માટી પકડે.</li></ul><p>ફાયદો sasta graded filter કરતાં, કાર્ય — separation filter drainage reinforcement. UV ઢાંકણ જોઈએ.</p>""" + svg_wrap(GEO_SVG,"Geotextile filter geomembrane liner geogrid","Geosynthetics"),
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
    page=f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>DI01006021 · Summer 2026 solved paper</title><style>{CSS}</style></head><body><main class="page"><header class="hero"><div class="eyebrow">Solved question paper · English questions · Friendly Gujarati answers</div><div class="lang-switch" aria-label="Choose language"><button type="button" data-lang="en" aria-pressed="true">English</button><button type="button" data-lang="gu" aria-pressed="false">ગુજરાતી</button></div><h1>Construction Material</h1><div class="meta">GTU Diploma · Civil · Semester 1 · Summer 2026 · DI01006021 · 07-07-2026 · 70 marks · 10:30 AM TO 01:00 PM</div></header>{''.join(sections_html)}<div class="footer">Solved paper for study. Confirm current IS codes and site safety before use.</div></main><script>document.querySelectorAll('.lang-switch button').forEach(b=>b.addEventListener('click',()=>{{document.documentElement.lang=b.dataset.lang;document.querySelectorAll('.lang-switch button').forEach(x=>x.setAttribute('aria-pressed',x===b?'true':'false'));}}));</script></body></html>'''
    return page

def main():
    page=build_page()
    out_papers=ROOT/"papers-upload/papers/DI01006021/summer-2026.html"
    out_ws=ROOT/"preview/workshop/DI01006021_summer2026_bilingual.html"
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
    (ROOT/"drive-upload/DI01006021_summer_2026_bilingual.html").write_text(page,encoding="utf-8")

if __name__=="__main__":
    main()
