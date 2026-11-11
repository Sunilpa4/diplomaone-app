#!/usr/bin/env python3
"""Build DI04009011 Substation Engineering Summer 2026 — friendly Gujarati, minimal brackets."""
from pathlib import Path
import html
ROOT = Path(__file__).resolve().parent.parent
CSS = """:root{--ink:#20252d;--muted:#65717d;--blue:#145c8b;--line:#d9e1e7;--paper:#f7f9fb;--purple:#58316f}
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
SLD132_SVG="""<rect width="360" height="220" fill="#fff"/><text x="180" y="16" font-size="11" text-anchor="middle" font-weight="bold" fill="#164f73">132 kV single bus substation — single line diagram</text>
<g font-size="5.5">
<line x1="20" y1="45" x2="340" y2="45" stroke="#c00" stroke-width="2"/><text x="180" y="40" font-size="6" text-anchor="middle" fill="#c00">132 kV Single Bus</text>
<text x="40" y="65">Incomer 1</text><line x1="50" y1="68" x2="50" y2="90" stroke="#333"/><rect x="40" y="90" width="20" height="12" rx="2" fill="#fce9e9" stroke="#c00"/><text x="50" y="98" text-anchor="middle" font-size="5">CB</text>
<rect x="38" y="105" width="24" height="8" rx="2" fill="#eaf4fa" stroke="#145c8b"/><text x="50" y="111" text-anchor="middle" font-size="4.5">Isolator</text>
<rect x="40" y="118" width="20" height="10" rx="2" fill="#fff3e0" stroke="#b77e24"/><text x="50" y="125" text-anchor="middle" font-size="4.5">CT</text>
<rect x="30" y="135" width="40" height="22" rx="4" fill="#f1fbf6" stroke="#77a795"/><text x="50" y="144" text-anchor="middle" font-weight="bold">Tr 132/33</text><text x="50" y="152" text-anchor="middle">kV 50MVA</text>
<text x="120" y="65">Incomer 2</text><line x1="130" y1="68" x2="130" y2="90" stroke="#333"/><rect x="120" y="90" width="20" height="12" rx="2" fill="#fce9e9" stroke="#c00"/><text x="130" y="98" text-anchor="middle" font-size="5">CB</text>
<rect x="118" y="105" width="24" height="8" rx="2" fill="#eaf4fa" stroke="#145c8b"/><text x="130" y="111" text-anchor="middle" font-size="4.5">Isolator</text>
<text x="200" y="65">Bus coupler</text><line x1="210" y1="68" x2="210" y2="90" stroke="#333"/><rect x="200" y="90" width="20" height="12" rx="2" fill="#fce9e9" stroke="#c00"/><text x="210" y="98" text-anchor="middle" font-size="5">CB</text>
<text x="270" y="65">Feeder</text><line x1="280" y1="68" x2="280" y2="90" stroke="#333"/><rect x="270" y="90" width="20" height="12" rx="2" fill="#fce9e9" stroke="#c00"/><text x="280" y="98" text-anchor="middle" font-size="5">CB</text>
<rect x="268" y="105" width="24" height="8" rx="2" fill="#eaf4fa" stroke="#145c8b"/><text x="280" y="111" text-anchor="middle" font-size="4.5">Isolator</text>
<text x="50" y="175" font-size="6">LA PT Earth switch on each bay, battery DC for control</text>
</g>"""

BUSLAYOUT_SVG="""<rect width="360" height="220" fill="#fff"/><text x="180" y="16" font-size="11" text-anchor="middle" font-weight="bold" fill="#164f73">Bus layouts — single vs double bus with coupler</text>
<rect x="15" y="35" width="150" height="55" rx="6" fill="#eaf4fa" stroke="#145c8b"/><text x="90" y="48" text-anchor="middle" font-size="7" font-weight="bold">Single bus</text><line x1="30" y1="58" x2="150" y2="58" stroke="#c00" stroke-width="1.5"/><text x="90" y="70" font-size="5.5" text-anchor="middle">cheapest, one fault → all off</text><text x="90" y="80" font-size="5.5" text-anchor="middle">flexibility low</text>
<rect x="185" y="35" width="160" height="55" rx="6" fill="#fff3e0" stroke="#b77e24"/><text x="265" y="48" text-anchor="middle" font-size="7" font-weight="bold">Double bus with coupler</text><line x1="200" y1="58" x2="330" y2="58" stroke="#c00" stroke-width="1.5"/><line x1="200" y1="66" x2="330" y2="66" stroke="#145c8b" stroke-width="1.5"/><text x="265" y="78" font-size="5.5" text-anchor="middle">any feeder on either bus</text><text x="265" y="86" font-size="5.5" text-anchor="middle">maintain without shutdown</text>
<rect x="15" y="100" width="150" height="55" rx="6" fill="#f1fbf6" stroke="#77a795"/><text x="90" y="113" text-anchor="middle" font-size="7" font-weight="bold">Ring / Mesh</text><text x="90" y="125" font-size="5.5" text-anchor="middle">each breaker two paths</text><text x="90" y="135" font-size="5.5" text-anchor="middle">breaker fail still supply on</text>
<rect x="185" y="100" width="160" height="55" rx="6" fill="#efe3fa" stroke="#7B2CD9"/><text x="265" y="113" text-anchor="middle" font-size="7" font-weight="bold">One and half breaker</text><text x="265" y="125" font-size="5.5" text-anchor="middle">3 breakers per 2 feeders</text><text x="265" y="135" font-size="5.5" text-anchor="middle">EHV 220 kV+ high reliability</text>
<text x="180" y="175" font-size="6.5" text-anchor="middle">Choice by importance: distribution single bus, transmission double or 1.5 breaker</text>"""

GIS_SVG="""<rect width="360" height="220" fill="#fff"/><text x="180" y="16" font-size="11" text-anchor="middle" font-weight="bold" fill="#164f73">GIS advantages over AIS</text>
<g font-size="6">
<rect x="15" y="35" width="105" height="32" rx="6" fill="#eaf4fa" stroke="#145c8b"/><text x="67" y="47" text-anchor="middle" font-weight="bold">Compact 1/10 area</text><text x="67" y="58" text-anchor="middle">indoor, city centre</text>
<rect x="125" y="35" width="105" height="32" rx="6" fill="#fff3e0" stroke="#b77e24"/><text x="177" y="47" text-anchor="middle" font-weight="bold">SF6 insulated</text><text x="177" y="58" text-anchor="middle">no pollution flashover</text>
<rect x="240" y="35" width="105" height="32" rx="6" fill="#f1fbf6" stroke="#77a795"/><text x="292" y="47" text-anchor="middle" font-weight="bold">Low maintenance</text><text x="292" y="58" text-anchor="middle">sealed 25 years</text>
<rect x="15" y="75" width="105" height="32" rx="6" fill="#fce9e9" stroke="#c00"/><text x="67" y="87" text-anchor="middle" font-weight="bold">Safe — enclosed</text><text x="67" y="98" text-anchor="middle">no touch live</text>
<rect x="125" y="75" width="105" height="32" rx="6" fill="#efe3fa" stroke="#7B2CD9"/><text x="177" y="87" text-anchor="middle" font-weight="bold">Low outage</text><text x="177" y="98" text-anchor="middle">reliable for EHV</text>
<rect x="240" y="75" width="105" height="32" rx="6" fill="#f7f9fb" stroke="#333"/><text x="292" y="87" text-anchor="middle" font-weight="bold">Cost high</text><text x="292" y="98" text-anchor="middle">but land saving</text>
</g>
<text x="180" y="135" font-size="7" text-anchor="middle">GIS uses SF6 gas in sealed metal enclosure at ~0.4 MPa, all live inside</text>"""

ISOLATOR_SVG="""<rect width="360" height="220" fill="#fff"/><text x="180" y="16" font-size="11" text-anchor="middle" font-weight="bold" fill="#164f73">Isolator types — off load disconnects</text>
<g font-size="6">
<rect x="15" y="35" width="100" height="40" rx="6" fill="#eaf4fa" stroke="#145c8b"/><text x="65" y="48" text-anchor="middle" font-weight="bold">Vertical break</text><text x="65" y="58" text-anchor="middle">blade lifts up, eye to eye</text><text x="65" y="68" text-anchor="middle">single phase stack</text>
<rect x="125" y="35" width="100" height="40" rx="6" fill="#fff3e0" stroke="#b77e24"/><text x="175" y="48" text-anchor="middle" font-weight="bold">Horizontal centre</text><text x="175" y="58" text-anchor="middle">two arms open sideways</text><text x="175" y="68" text-anchor="middle">needs more width</text>
<rect x="235" y="35" width="110" height="40" rx="6" fill="#f1fbf6" stroke="#77a795"/><text x="290" y="48" text-anchor="middle" font-weight="bold">Pantograph</text><text x="290" y="58" text-anchor="middle">scissor lifts vertically</text><text x="290" y="68" text-anchor="middle">GIS, height saving</text>
<text x="65" y="95" font-size="5.5">EHV 220kV+</text><text x="175" y="95" font-size="5.5">66 to 132kV</text><text x="290" y="95" font-size="5.5">220 to 400kV height limited</text>
</g>
<text x="180" y="120" font-size="7" text-anchor="middle">All open only when current zero — no arc, interlocked with CB</text>
<text x="180" y="135" font-size="6" text-anchor="middle" fill="#666">With earth switch: line earthed after isolator open for safety</text>"""

PLCC_SVG="""<rect width="360" height="220" fill="#fff"/><text x="180" y="16" font-size="11" text-anchor="middle" font-weight="bold" fill="#164f73">PLCC — Power Line Carrier Communication</text>
<g font-size="6">
<rect x="20" y="40" width="60" height="28" rx="6" fill="#eaf4fa" stroke="#145c8b"/><text x="50" y="52" text-anchor="middle">Control room</text><text x="50" y="62" font-size="5" text-anchor="middle">voice/data relay</text>
<rect x="100" y="40" width="60" height="28" rx="6" fill="#fff3e0" stroke="#b77e24"/><text x="130" y="52" text-anchor="middle">Carrier set</text><text x="130" y="62" font-size="5" text-anchor="middle">40 to 500kHz</text>
<rect x="180" y="40" width="60" height="28" rx="6" fill="#f1fbf6" stroke="#77a795"/><text x="210" y="52" text-anchor="middle">Coupling cap</text><text x="210" y="62" font-size="5" text-anchor="middle">blocks 50Hz</text>
<rect x="260" y="40" width="60" height="28" rx="6" fill="#fce9e9" stroke="#c00"/><text x="290" y="52" text-anchor="middle">Line trap</text><text x="290" y="62" font-size="5" text-anchor="middle">blocks HF to bus</text>
<line x1="80" y1="54" x2="100" y2="54" stroke="#333"/><line x1="160" y1="54" x2="180" y2="54" stroke="#333"/><line x1="240" y1="54" x2="260" y2="54" stroke="#333"/><line x1="320" y1="54" x2="340" y2="54" stroke="#333"/>
<text x="180" y="85" font-size="6" text-anchor="middle">HF signal rides on power line itself — no extra telephone wire needed</text>
<text x="180" y="98" font-size="6" text-anchor="middle">Used for teleprotection, speech, SCADA data between substations</text>
</g>"""

BATTERY_SVG="""<rect width="360" height="220" fill="#fff"/><text x="180" y="16" font-size="11" text-anchor="middle" font-weight="bold" fill="#164f73">Battery comparison for substation DC supply</text>
<g font-size="5.5">
<text x="20" y="40" font-weight="bold">Lead Acid</text><text x="20" y="52">Cheap 2V per cell, vented needs water, 3 to 5 years, heavy, good surge</text><text x="20" y="62">Self discharge high, works -10 to 40°C, needs ventilation hydrogen</text>
<text x="20" y="80" font-weight="bold">Nickel Cadmium NiCd</text><text x="20" y="92">Costly 1.2V, sealed maintenance free, 15 to 20 years, rugged</text><text x="20" y="102">Low self discharge, -20 to 50°C wide, deep discharge tolerant, memory effect slight</text>
<text x="20" y="120" font-size="6" fill="#145c8b">Substation DC mostly 110V or 220V: breaker trip needs reliable battery — NiCd preferred for remote unmanned</text>
</g>"""

RECLOSER_SVG="""<rect width="360" height="220" fill="#fff"/><text x="180" y="16" font-size="11" text-anchor="middle" font-weight="bold" fill="#164f73">Auto recloser — self restore after transient fault</text>
<g font-size="6">
<rect x="20" y="40" width="70" height="30" rx="6" fill="#eaf4fa" stroke="#145c8b"/><text x="55" y="52" text-anchor="middle">Fault → trip</text><text x="55" y="62" text-anchor="middle">sense I</text>
<rect x="100" y="40" width="70" height="30" rx="6" fill="#fff3e0" stroke="#b77e24"/><text x="135" y="52" text-anchor="middle">Dead time</text><text x="135" y="62" text-anchor="middle">0.3 to 1 sec</text>
<rect x="180" y="40" width="80" height="30" rx="6" fill="#f1fbf6" stroke="#77a795"/><text x="220" y="52" text-anchor="middle">Reclose</text><text x="220" y="62" text-anchor="middle">if transient gone OK</text>
<rect x="270" y="40" width="70" height="30" rx="6" fill="#fce9e9" stroke="#c00"/><text x="305" y="52" text-anchor="middle">Lockout</text><text x="305" y="62" text-anchor="middle">if permanent</text>
<line x1="90" y1="55" x2="100" y2="55" stroke="#333"/><line x1="170" y1="55" x2="180" y2="55" stroke="#333"/><line x1="260" y1="55" x2="270" y2="55" stroke="#333"/>
<text x="20" y="90" font-size="6">Typical sequence: trip — reclose fast 1st, if still fault trip — reclose slow 2nd — lockout after 3rd</text>
<text x="20" y="102" font-size="6">80% overhead faults are transient lightning branch — recloser avoids long outage</text>
</g>
<text x="180" y="125" font-size="7" text-anchor="middle">Coordinated with sectionaliser: recloser opens → sectionaliser counts and isolates faulty section</text>"""

ARRESTER_SVG="""<rect width="360" height="220" fill="#fff"/><text x="180" y="16" font-size="11" text-anchor="middle" font-weight="bold" fill="#164f73">Surge arrester types — clips overvoltage</text>
<g font-size="6">
<rect x="20" y="35" width="100" height="35" rx="6" fill="#eaf4fa" stroke="#145c8b"/><text x="70" y="48" text-anchor="middle" font-weight="bold">Gap type obsolete</text><text x="70" y="58" text-anchor="middle">rod horn gap sparks over</text>
<rect x="130" y="35" width="100" height="35" rx="6" fill="#fff3e0" stroke="#b77e24"/><text x="180" y="48" text-anchor="middle" font-weight="bold">Silicon carbide</text><text x="180" y="58" text-anchor="middle">gap plus non linear resistor</text>
<rect x="240" y="35" width="100" height="35" rx="6" fill="#f1fbf6" stroke="#77a795"/><text x="290" y="48" text-anchor="middle" font-weight="bold">Metal oxide ZnO</text><text x="290" y="58" text-anchor="middle">gapless, modern, best</text>
<text x="20" y="90" font-size="6">ZnO: resistance very high at normal V, drops sharply at surge → conducts surge to earth</text>
<text x="20" y="102" font-size="6">Placed at transformer bushing, line entry, across equipment — earth lead short</text>
<text x="20" y="114" font-size="6">Rating by MCOV and discharge current 10kA, class 1 to 4</text>
</g>
<text x="180" y="140" font-size="7" text-anchor="middle">Without arrester lightning 1000kV would puncture insulation — arrester holds to ~650kV</text>"""

SWITCH_SCHEME_SVG="""<rect width="360" height="220" fill="#fff"/><text x="180" y="16" font-size="11" text-anchor="middle" font-weight="bold" fill="#164f73">220 kV Double bus with bus coupler — switching scheme</text>
<g font-size="5.5">
<line x1="30" y1="50" x2="330" y2="50" stroke="#c00" stroke-width="2"/><text x="180" y="44" text-anchor="middle" fill="#c00">Bus A 220 kV Main 1</text>
<line x1="30" y1="70" x2="330" y2="70" stroke="#145c8b" stroke-width="2"/><text x="180" y="85" text-anchor="middle" fill="#145c8b">Bus B 220 kV Main 2</text>
<text x="40" y="100">Bay 1: CB1 to A via isolator 1</text><text x="40" y="112">CB2 to B via isolator 2</text><text x="40" y="124">Normal on A, if maintain A shift to B</text>
<text x="40" y="140">Bus coupler CB joins A and B</text><text x="40" y="152">when both live synchronised</text>
<line x1="100" y1="60" x2="100" y2="90" stroke="#333"/><circle cx="100" cy="60" r="3" fill="#fff" stroke="#333"/><circle cx="100" cy="90" r="3" fill="#fff" stroke="#333"/>
<line x1="200" y1="60" x2="200" y2="90" stroke="#333"/><circle cx="200" cy="60" r="3" fill="#fff" stroke="#333"/><circle cx="200" cy="90" r="3" fill="#fff" stroke="#333"/>
</g>
<text x="180" y="175" font-size="6.5" text-anchor="middle">Any feeder can be on either bus — flexibility plus maintenance without shutdown, cost of extra isolators justified for EHV</text>"""

MONITOR_PF_SVG="""<rect width="360" height="220" fill="#fff"/><text x="180" y="16" font-size="11" text-anchor="middle" font-weight="bold" fill="#164f73">Power flow and voltage monitoring — block diagram</text>
<g font-size="6">
<rect x="20" y="40" width="70" height="28" rx="6" fill="#eaf4fa" stroke="#145c8b"/><text x="55" y="52" text-anchor="middle">CT VT</text><text x="55" y="62" text-anchor="middle">field inputs</text>
<rect x="110" y="40" width="70" height="28" rx="6" fill="#fff3e0" stroke="#b77e24"/><text x="145" y="52" text-anchor="middle">IED / Meter</text><text x="145" y="62" text-anchor="middle">P Q V I f</text>
<rect x="200" y="40" width="70" height="28" rx="6" fill="#f1fbf6" stroke="#77a795"/><text x="235" y="52" text-anchor="middle">RTU / Gateway</text>
<rect x="280" y="40" width="60" height="28" rx="6" fill="#fce9e9" stroke="#c00"/><text x="310" y="52" text-anchor="middle">SCADA</text>
<line x1="90" y1="54" x2="110" y2="54" stroke="#333"/><line x1="180" y1="54" x2="200" y2="54" stroke="#333"/><line x1="270" y1="54" x2="280" y2="54" stroke="#333"/>
<text x="20" y="90" font-size="6">Calculates active P, reactive Q, voltage profile, alerts if V low or overload</text>
<text x="20" y="102" font-size="6">Triggers tap changer, capacitor bank in or out, display trends for load dispatch</text>
</g>
<text x="180" y="125" font-size="7" text-anchor="middle">Real time monitoring avoids blackout — operator sees flow arrows and voltage heat map</text>"""

EARTH_POT_SVG="""<rect width="360" height="220" fill="#fff"/><text x="180" y="16" font-size="11" text-anchor="middle" font-weight="bold" fill="#164f73">Step and touch potential — safety</text>
<g font-size="6">
<circle cx="90" cy="90" r="40" fill="none" stroke="#145c8b"/><text x="90" y="92" text-anchor="middle">Fault grid</text><text x="90" y="105" font-size="5" text-anchor="middle">I to earth → gradients</text>
<text x="160" y="60">Step: feet 1m apart → V step between feet while walking near fault</text><text x="160" y="72">limit ~ few kV for 1 sec, mesh voltage must be below</text>
<text x="160" y="90">Touch: hand on earthed structure and feet on ground → V touch hand to feet</text><text x="160" y="102">more dangerous, heart path, limit lower ~1 to 2kV</text>
<text x="20" y="135" font-size="6">IS 3043 aims: low earth resistance below 1Ω for EHV, meshes plus rods reduce gradient, crushed rock raises foot resistance</text>
</g>
<text x="180" y="160" font-size="7" text-anchor="middle">Design checks E touch and E step per IEEE 80 — if exceed, add meshes or rods</text>"""

HGIS_SVG="""<rect width="360" height="220" fill="#fff"/><text x="180" y="16" font-size="11" text-anchor="middle" font-weight="bold" fill="#164f73">Hybrid GIS — HGIS compact</text>
<g font-size="6">
<rect x="20" y="40" width="100" height="40" rx="6" fill="#eaf4fa" stroke="#145c8b"/><text x="70" y="53" text-anchor="middle">AIS bus and lines</text><text x="70" y="64" text-anchor="middle">air insulated open</text>
<rect x="130" y="40" width="100" height="40" rx="6" fill="#fff3e0" stroke="#b77e24"/><text x="180" y="53" text-anchor="middle">HGIS bay</text><text x="180" y="64" text-anchor="middle">CB+Isolator SF6 sealed</text>
<rect x="240" y="40" width="100" height="40" rx="6" fill="#f1fbf6" stroke="#77a795"/><text x="290" y="53" text-anchor="middle">AIS again</text><text x="290" y="64" text-anchor="middle">transformer overhead</text>
<text x="20" y="100" font-size="6">Purpose: keep air bus cheap, but breaker and switches compact maintenance free in city or polluted area</text>
<text x="20" y="112" font-size="6">Size about 40% less than AIS, cost between AIS and full GIS, outage less, suits extensions</text>
</g>
<text x="180" y="135" font-size="7" text-anchor="middle">HGIS ideal for uprating old AIS without full rebuild</text>"""

GREEN_SVG="""<rect width="360" height="220" fill="#fff"/><text x="180" y="16" font-size="11" text-anchor="middle" font-weight="bold" fill="#164f73">Green substation features</text>
<g font-size="6">
<rect x="20" y="40" width="80" height="32" rx="6" fill="#eaf4fa" stroke="#145c8b"/><text x="60" y="52" text-anchor="middle">SF6 free or eco</text><text x="60" y="62" text-anchor="middle">g3 / dry air</text>
<rect x="110" y="40" width="80" height="32" rx="6" fill="#fff3e0" stroke="#b77e24"/><text x="150" y="52" text-anchor="middle">Vegetation & oil</text><text x="150" y="62" text-anchor="middle">natural ester, rain harvest</text>
<rect x="200" y="40" width="80" height="32" rx="6" fill="#f1fbf6" stroke="#77a795"/><text x="240" y="52" text-anchor="middle">Solar + LED</text><text x="240" y="62" text-anchor="middle">low energy use</text>
<rect x="290" y="40" width="50" height="32" rx="6" fill="#fce9e9" stroke="#c00"/><text x="315" y="52" text-anchor="middle">Noise low</text>
<text x="20" y="90" font-size="6">Also: recycling, low EMF design, bird friendly, digital monitoring cuts visits</text>
<text x="20" y="102" font-size="6">Certification like LEED, helps utility ESG and local acceptance</text>
</g>
<text x="180" y="125" font-size="7" text-anchor="middle">Green does not mean no equipment but low impact over life cycle</text>"""

SMARTGRID_SVG="""<rect width="360" height="220" fill="#fff"/><text x="180" y="16" font-size="11" text-anchor="middle" font-weight="bold" fill="#164f73">Smart grid substation communication</text>
<g font-size="6">
<rect x="20" y="40" width="70" height="28" rx="6" fill="#eaf4fa" stroke="#145c8b"/><text x="55" y="52" text-anchor="middle">CT/VT</text><text x="55" y="62" text-anchor="middle">merging unit</text>
<rect x="110" y="40" width="70" height="28" rx="6" fill="#fff3e0" stroke="#b77e24"/><text x="145" y="52" text-anchor="middle">IEDs</text><text x="145" y="62" text-anchor="middle">protection bay</text>
<rect x="200" y="40" width="70" height="28" rx="6" fill="#f1fbf6" stroke="#77a795"/><text x="235" y="52" text-anchor="middle">Station bus</text><text x="235" y="62" text-anchor="middle">IEC61850 GOOSE</text>
<rect x="280" y="40" width="60" height="28" rx="6" fill="#fce9e9" stroke="#c00"/><text x="310" y="52" text-anchor="middle">Gateway</text><text x="310" y="62" text-anchor="middle">to control centre</text>
<line x1="90" y1="54" x2="110" y2="54" stroke="#333"/><line x1="180" y1="54" x2="200" y2="54" stroke="#333"/><line x1="270" y1="54" x2="280" y2="54" stroke="#333"/>
<text x="20" y="90" font-size="6">Process bus samples analog at 4kHz, GOOSE trips in 4ms, station bus MMS reports, time sync PTP</text>
</g>
<text x="180" y="120" font-size="7" text-anchor="middle">Smart grid adds DER, self healing, demand response via this network</text>"""

DIGITAL_SVG="""<rect width="360" height="220" fill="#fff"/><text x="180" y="16" font-size="11" text-anchor="middle" font-weight="bold" fill="#164f73">Digital substation concept</text>
<g font-size="6">
<text x="20" y="45">Conventional: copper 100s cores from yard to relay house — heavy, EMI</text>
<text x="20" y="60">Digital: CT VT → merging unit in yard → one fiber to IEDs — copper almost gone</text>
<rect x="30" y="75" width="80" height="26" rx="6" fill="#eaf4fa" stroke="#145c8b"/><text x="70" y="91" text-anchor="middle">Non-conv CT/VT</text>
<rect x="130" y="75" width="80" height="26" rx="6" fill="#fff3e0" stroke="#b77e24"/><text x="170" y="91" text-anchor="middle">Merging unit</text>
<rect x="230" y="75" width="80" height="26" rx="6" fill="#f1fbf6" stroke="#77a795"/><text x="270" y="91" text-anchor="middle">Fiber network</text>
<text x="20" y="115" font-size="6">Adv: low wiring, accurate, flexible, self diagnostics. Disadv: cost high, cyber risk, skills needed</text>
</g>"""

THREE_POS_SVG="""<rect width="360" height="220" fill="#fff"/><text x="180" y="16" font-size="11" text-anchor="middle" font-weight="bold" fill="#164f73">Three position disconnector / earth switch in GIS</text>
<g font-size="6">
<rect x="40" y="40" width="80" height="40" rx="6" fill="#eaf4fa" stroke="#145c8b"/><text x="80" y="53" text-anchor="middle">CLOSED</text><text x="80" y="64" text-anchor="middle">connected to bus</text>
<rect x="140" y="40" width="80" height="40" rx="6" fill="#fff3e0" stroke="#b77e24"/><text x="180" y="53" text-anchor="middle">OPEN</text><text x="180" y="64" text-anchor="middle">isolated floating</text>
<rect x="240" y="40" width="80" height="40" rx="6" fill="#f1fbf6" stroke="#77a795"/><text x="280" y="53" text-anchor="middle">EARTHED</text><text x="280" y="64" text-anchor="middle">grounded safe</text>
<line x1="120" y1="60" x2="140" y2="60" stroke="#333"/><line x1="220" y1="60" x2="240" y2="60" stroke="#333"/>
<text x="20" y="100" font-size="6">One moving blade with three stable positions — saves space, motor driven, interlocked so cannot go directly closed to earth</text>
</g>
<text x="180" y="125" font-size="7" text-anchor="middle">GIS bay uses one drive instead of separate isolator and earth switch</text>"""

HVDC_SVG="""<rect width="360" height="220" fill="#fff"/><text x="180" y="16" font-size="11" text-anchor="middle" font-weight="bold" fill="#164f73">12 pulse HVDC converter station</text>
<g font-size="5.5">
<rect x="20" y="35" width="80" height="30" rx="6" fill="#eaf4fa" stroke="#145c8b"/><text x="60" y="48" text-anchor="middle">AC 400kV Y</text><text x="60" y="58" text-anchor="middle">transformer Y-Y</text>
<rect x="110" y="35" width="80" height="30" rx="6" fill="#fff3e0" stroke="#b77e24"/><text x="150" y="48" text-anchor="middle">AC 400kV Y-Δ</text><text x="150" y="58" text-anchor="middle">30° shift</text>
<rect x="210" y="35" width="60" height="30" rx="6" fill="#f1fbf6" stroke="#77a795"/><text x="240" y="48" text-anchor="middle">6 pulse bridge</text>
<rect x="280" y="35" width="60" height="30" rx="6" fill="#fce9e9" stroke="#c00"/><text x="310" y="48" text-anchor="middle">6 pulse bridge</text>
<rect x="120" y="80" width="120" height="24" rx="6" fill="#efe3fa" stroke="#7B2CD9"/><text x="180" y="94" text-anchor="middle">Series DC ±500kV</text>
<text x="20" y="115" font-size="6">Two 6 pulse in series via Y-Y and Y-Δ phase shift give 12 pulse → much less harmonics 11th 13th canceled</text>
<text x="20" y="127" font-size="6">Each station has filters, smoothing reactor, DC breaker, controls fire angle alpha rectifier inverter gamma</text>
</g>
<text x="180" y="150" font-size="7" text-anchor="middle">12 pulse is standard for high power HVDC long distance and interconnection</text>"""

CONVERTER_MON_SVG="""<rect width="360" height="220" fill="#fff"/><text x="180" y="16" font-size="11" text-anchor="middle" font-weight="bold" fill="#164f73">Digital monitoring of converter performance</text>
<g font-size="6">
<rect x="20" y="40" width="70" height="28" rx="6" fill="#eaf4fa" stroke="#145c8b"/><text x="55" y="52" text-anchor="middle">Valve U I T</text><text x="55" y="62" text-anchor="middle">thyristor stack</text>
<rect x="110" y="40" width="70" height="28" rx="6" fill="#fff3e0" stroke="#b77e24"/><text x="145" y="52" text-anchor="middle">Sensors</text><text x="145" y="62" text-anchor="middle">fibre optic</text>
<rect x="200" y="40" width="70" height="28" rx="6" fill="#f1fbf6" stroke="#77a795"/><text x="235" y="52" text-anchor="middle">IED</text><text x="235" y="62" text-anchor="middle">analytics</text>
<rect x="280" y="40" width="60" height="28" rx="6" fill="#fce9e9" stroke="#c00"/><text x="310" y="52" text-anchor="middle">HMI alert</text>
<line x1="90" y1="54" x2="110" y2="54" stroke="#333"/><line x1="180" y1="54" x2="200" y2="54" stroke="#333"/><line x1="270" y1="54" x2="280" y2="54" stroke="#333"/>
<text x="20" y="90" font-size="6">Monitors firing angle, commutation failure, temperature, harmonics, loss — predicts failure before outage</text>
</g>
<text x="180" y="120" font-size="k" font-size="7" text-anchor="middle">Digital twin compares real vs expected — early warning</text>"""

SCADA_SVG="""<rect width="360" height="220" fill="#fff"/><text x="180" y="16" font-size="11" text-anchor="middle" font-weight="bold" fill="#164f73">SCADA substation</text>
<g font-size="6">
<rect x="20" y="40" width="60" height="28" rx="6" fill="#eaf4fa" stroke="#145c8b"/><text x="50" y="52" text-anchor="middle">Field IED</text>
<rect x="100" y="40" width="70" height="28" rx="6" fill="#fff3e0" stroke="#b77e24"/><text x="135" y="52" text-anchor="middle">RTU Gateway</text>
<rect x="190" y="40" width="70" height="28" rx="6" fill="#f1fbf6" stroke="#77a795"/><text x="225" y="52" text-anchor="middle">Comm WAN</text>
<rect x="280" y="40" width="60" height="28" rx="6" fill="#fce9e9" stroke="#c00"/><text x="310" y="52" text-anchor="middle">Master</text>
<line x1="80" y1="54" x2="100" y2="54" stroke="#333"/><line x1="170" y1="54" x2="190" y2="54" stroke="#333"/><line x1="260" y1="54" x2="280" y2="54" stroke="#333"/>
<text x="20" y="80" font-size="6">Adv: remote view and control, faster fault restoration, data logging, unmanned operation, load management</text>
</g>"""

SECTIONS=[
{
 "title_en":"Q1 · Substation basics and bus",
 "title_gu":"પ્ર.1 · સબસ્ટેશન બેઝિક અને બસ",
 "cards":[
  {
   "q_en":"Q.1 (a) List basic functions of an electrical substation. (3 marks)",
   "marks_en":"3 marks","marks_gu":"૦૩ ગુણ",
   "a_en":"""<ul><li><strong>Voltage change:</strong> Step up at generation for transmission, step down for distribution to users.</li><li><strong>Switching:</strong> Connect or disconnect lines and feeders via breaker and isolator for operation and maintenance.</li><li><strong>Protection:</strong> Detect fault via CT VT and relay then trip breaker to isolate faulty part.</li><li><strong>Metering and monitoring:</strong> Measure V I P Q energy for billing and control.</li><li><strong>Reactive support:</strong> Capacitor or reactor banks for voltage control and power factor.</li><li><strong>Communication node:</strong> PLCC, fiber, SCADA interface for grid control.</li></ul>""",
   "a_gu":"""<ul><li><strong>વોલ્ટેજ બદલવું:</strong> ઉત્પાદન પર વધારવું ટ્રાન્સમિશન માટે, વિતરણ માટે ઘટાડવું.</li><li><strong>જોડવું તોડવું:</strong> બ્રેકર isolator થી લાઇન ફીડર ચાલુ બંધ.</li><li><strong>રક્ષણ:</strong> CT VT relay થી fault પારખે પછી બ્રેકર ટ્રિપ કરી અલગ કરે.</li><li><strong>માપ અને દેખરેખ:</strong> V I P Q ઉર્જા મીટર બિલિંગ અને કંટ્રોલ માટે.</li><li><strong>રિએક્ટિવ સહાય:</strong> કેપેસિટર reactor થી વોલ્ટેજ અને power factor કંટ્રોલ.</li><li><strong>કોમ્યુનિકેશન નોડ:</strong> PLCC fiber SCADA ઇન્ટરફેસ ગ્રીડ કંટ્રોલ માટે.</li></ul>""",
  },
  {
   "q_en":"Q.1 (b) Sate and explain the factors considered for substation site selection. (4 marks)",
   "marks_en":"4 marks","marks_gu":"૦૪ ગુણ",
   "a_en":"""<ul><li><strong>Load centre:</strong> Near major loads to reduce distribution length and losses.</li><li><strong>Land:</strong> Enough level area with space for future bays, easy shape, low cost, good bearing capacity.</li><li><strong>Access:</strong> Road for transformer delivery, rail if possible, water for construction and fire.</li><li><strong>Network in and out:</strong> Feasible line corridors without excessive crossings, river or forest restrictions.</li><li><strong>Environment:</strong> No heavy flooding, low pollution dust salt, avoid forest and habitation resistance, earthing soil not rocky.</li><li><strong>Utilities and safety:</strong> Grid nearby, telecom, labour, clearance from airports schools.</li></ul><p>Final site compares 2 to 3 options on cost, losses, reliability.</p>""",
   "a_gu":"""<ul><li><strong>લોડ કેન્દ્ર:</strong> મોટા લોડ નજીક જેથી વિતરણ લંબાઈ અને loss ઓછા.</li><li><strong>જમીન:</strong> સપાટ પૂરતી જગ્યા ભવિષ્ય બે માટે, આકાર સરળ, કિંમત ઓછી, વજન ઝીલે તેવી.</li><li><strong>પહોંચ:</strong> ટ્રાન્સફોર્મર લાવવા રસ્તા, શક્ય તો રેલ, પાણી બાંધકામ અને ફાયર માટે.</li><li><strong>નેટવર્ક:</strong> આવનારી નીકળતી લાઇન માટે corridor શક્ય, નદી જંગલ નડતર ઓછું.</li><li><strong>પર્યાવરણ:</strong> પૂર ન આવે, ધૂળ ખાર ઓછો, જંગલ વસાહત વિરોધ નહિ, માટી ખડકાળ નહિ જેથી અર્થિંગ થાય.</li><li><strong>સગવડ સલામતી:</strong> ગ્રીડ નજીક, ટેલિકોમ મજૂર, એરપોર્ટ શાળા થી clearance.</li></ul><p>અંતે 2 થી 3 જગ્યા ના ખર્ચ loss વિશ્વસનીયતા નો તુલના કરો.</p>""",
  },
  {
   "q_en":"Q.1 (c) Draw a single line diagram of a 132KV substation with a single bus system and explain each component in detail. (7 marks)",
   "marks_en":"7 marks","marks_gu":"૦૭ ગુણ",
   "a_en":"""<p><strong>Layout:</strong> Two incomers 132kV plus one transformer bay 132/33kV and two feeders all on one common bus. Each bay has bus isolator, circuit breaker, line isolator with earth switch, CT, PT, lightning arrester.</p><ul><li><strong>Bus bar 132kV:</strong> Aluminium tube carries all power, rated for 2000A short time 31.5kA.</li><li><strong>Isolator:</strong> Visible break for maintenance only at no load, interlocked with CB.</li><li><strong>Circuit breaker SF6:</strong> Interrupts load and fault current, main protection.</li><li><strong>CT PT:</strong> Step down I V for metering and relay.</li><li><strong>Power transformer 132/33kV:</strong> ONAN/ONAF 50MVA with tap changer.</li><li><strong>Arrester, earth:</strong> Clips surge, earthing grid safety.</li></ul><p>Adv cheap simple, disadv bus fault shuts all.</p>""" + svg_wrap(SLD132_SVG,"132kV single bus — incomers via CB to common bus to transformer and feeders","132kV SLD"),
   "a_gu":"""<p><strong>રચના:</strong> બે આવક 132kV વત્તા એક ટ્રાન્સફોર્મર 132/33kV અને બે ફીડર બધા એક બસ પર. દરેક bay માં બસ isolator, બ્રેકર, લાઇન isolator earth switch, CT PT, arrester.</p><ul><li><strong>બસ 132kV:</strong> એલ્યુમિનિયમ ટ્યુબ બધો પાવર વહન કરે.</li><li><strong>Isolator:</strong> દેખીતો કાપ માત્ર નો લોડે જાળવણી માટે, CB સાથે interlock.</li><li><strong>બ્રેકર SF6:</strong> લોડ અને fault કરંટ તોડે.</li><li><strong>CT PT:</strong> I V નાના કરી મીટર relay ને.</li><li><strong>ટ્રાન્સફોર્મર 132/33kV:</strong> 50MVA tap changer સાથે.</li><li><strong>arrester earth:</strong> surge રોકે, અર્થિંગ સલામતી.</li></ul><p>ફાયદો સસ્તું સરળ, ગેરલાભ બસ fault એ બધું બંધ.</p>""" + svg_wrap(SLD132_SVG,"132kV single bus — incomer CB થી common bus થી ટ્રાન્સફોર્મર ફીડર","132kV SLD"),
  },
  {
   "q_en":"Q.1 (c) OR List different bus layouts used in substations. Explain any two with neat diagrams. (7 marks)",
   "marks_en":"7 marks","marks_gu":"૦૭ ગુણ",
   "a_en":"""<p><strong>Layouts:</strong> Single bus, single bus sectionalised, double bus single breaker, double bus with bus coupler, ring mesh, one and half breaker, double breaker.</p><p><strong>Single bus:</strong> All feeders on one bus via one CB each. Cheapest for distribution, one bus fault loses all. Operation simple.</p><p><strong>Double bus with coupler:</strong> Two main buses A and B, each feeder can select via two isolators, coupler CB connects buses. For maintenance shift feeder to other bus without outage, flexibility high, cost more but justified for EHV. Protection needs bus selection logic.</p>""" + svg_wrap(BUSLAYOUT_SVG,"Bus choices — single cheap, double flexible, ring high reliability","Bus layouts"),
   "a_gu":"""<p><strong>લેઆઉટ:</strong> single bus, sectionalised, double bus, ring mesh, one and half breaker, double breaker.</p><p><strong>Single bus:</strong> બધા ફીડર એક bus પર એક CB થી. વિતરણ માટે સસ્તું, bus fault એ બધું બંધ. ચલાવવું સરળ.</p><p><strong>Double bus coupler સાથે:</strong> બે bus A B, દરેક ફીડર બે isolator થી કોઈ પણ પર, coupler CB બંને જોડે. જાળવણી વખતે બીજા પર ફેરવો outage વગર, લવચીકતા વધુ, EHV માટે ખર્ચ વાજબી.</p>""" + svg_wrap(BUSLAYOUT_SVG,"Bus પસંદગી — single સસ્તું double લવચીક ring વિશ્વાસુ","Bus layouts"),
  },
 ]
},
{
 "title_en":"Q2 · Equipment and safety",
 "title_gu":"પ્ર.2 · સાધન અને સલામતી",
 "cards":[
  {
   "q_en":"Q.2 (a) State advantages of GIS substations. (3 marks)",
   "marks_en":"3 marks","marks_gu":"૦૩ ગુણ",
   "a_en":"""<ul><li>Area about 10% of AIS — fits in city buildings or underground.</li><li>Not affected by pollution, salt, dust — no external flashover.</li><li>Very low maintenance sealed SF6 25 years, personnel safe all live enclosed.</li><li>High reliability availability for EHV, low outage rate.</li><li>Lower lifecycle cost when land costly, less site work.</li></ul>""" + svg_wrap(GIS_SVG,"GIS compact SF6 sealed — area 1/10, low maintenance, high reliability","GIS advantages"),
   "a_gu":"""<ul><li>જગ્યા AIS ના 10% — શહેર બિલ્ડિંગ કે અન્ડરગ્રાઉન્ડ માં બેસે.</li><li>પ્રદૂષણ ખાર ધૂળ અસર નહિ — બાહ્ય flashover નહિ.</li><li>જાળવણી ખૂબ ઓછી SF6 સીલ 25 વર્ષ, માણસ સલામત બધું ઢંકાયેલું.</li><li>વિશ્વાસ વધુ EHV માટે outage ઓછો.</li><li>જમીન મોંઘી ત્યાં કુલ ખર્ચ ઓછો.</li></ul>""" + svg_wrap(GIS_SVG,"GIS compact SF6 સીલ — જગ્યા 1/10 જાળવણી ઓછી વિશ્વાસ વધુ","GIS advantages"),
  },
  {
   "q_en":"Q.2 (b) Explain condition monitoring of a transformer. (4 marks)",
   "marks_en":"4 marks","marks_gu":"૦૪ ગુણ",
   "a_en":"""<p><strong>On line checks without shutdown:</strong></p><ul><li><strong>Oil:</strong> Temperature top and winding via sensor, oil level, moisture, dissolved gas analysis DGA for incipient fault — H2 C2H2 high means discharge.</li><li><strong>Bushing:</strong> Tan delta and capacitance, infrared thermography for hot spots.</li><li><strong>Load and tap:</strong> Current loading vs rating, tap changer operations count and wear.</li><li><strong>Acoustics vibration:</strong> Hum change indicates core looseness, partial discharge sensor UHF.</li></ul><p>Periodic tests: insulation resistance, turns ratio, moisture in paper. Alarms to SCADA, trending predicts failure.</p>""",
   "a_gu":"""<p><strong>બંધ કર્યા વગર તપાસ:</strong></p><ul><li><strong>તેલ:</strong> તાપમાન સેન્સર, તેલ સ્તર, ભેજ, DGA — H2 C2H2 વધે તો discharge.</li><li><strong>Bushing:</strong> tan delta capacitance, infrared થી ગરમ જગ્યા.</li><li><strong>લોડ tap:</strong> કરંટ rating સામે, tap કેટલી વાર બદલાયો.</li><li><strong>અવાજ કંપન:</strong> ઘોંઘાટ બદલાય તો core ઢીલું, partial discharge UHF.</li></ul><p>સમયાંતરે IR turns ratio કાગળ ભેજ તપાસ, SCADA ને alarm, trend થી ખામી આગાહી.</p>""",
  },
  {
   "q_en":"Q.2 (c) List out types of isolators. Explain any one in detail. (7 marks)",
   "marks_en":"7 marks","marks_gu":"૦૭ ગુણ",
   "a_en":"""<p><strong>Types:</strong> Vertical break, horizontal centre break, double break, pantograph, semi pantograph.</p><p><strong>Vertical break detailed:</strong> One moving blade pivots vertically, one fixed jaw. When open blade swings up leaving visible gap. Single column per phase, three columns on one base. Operation motor plus manual handle, interlocked so CB must be open. Arcing horns optional. Needs less width than centre break, suits EHV lines where phase spacing large. With earth switch blade grounds line after opening for safety.</p><p>Rating upto 420kV, short time 40kA, all at no load only.</p>""" + svg_wrap(ISOLATOR_SVG,"Vertical, horizontal, pantograph isolators — all opened only at no current","Isolator types"),
   "a_gu":"""<p><strong>પ્રકાર:</strong> vertical break, horizontal centre break, double break, pantograph.</p><p><strong>Vertical break વિગતે:</strong> એક ચલ blade ઊભું ફરે, સામે સ્થિર jaw. ખૂલે ત્યારે blade ઉપર જાય દેખીતો gap. એક column પ્રતિ ફેઝ ત્રણ એક બેઝ પર. મોટર વત્તા હાથો, CB ખૂલ્યું હોય ત્યારે જ ખૂલે interlock. ઓછી પહોળાઈ centre break થી, EHV માં અનુકૂળ. earth switch સાથે ખૂલ્યા પછી લાઇન earth થાય સલામતી.</p><p>420kV સુધી, માત્ર નો લોડે.</p>""" + svg_wrap(ISOLATOR_SVG,"Vertical horizontal pantograph isolator — બધા માત્ર નો કરંટે ખૂલે","Isolator types"),
  },
  {
   "q_en":"Q.2 (a) OR Explain sequence of operation of isolator, circuit breaker and earth switch while opening and closing a line. (3 marks)",
   "marks_en":"3 marks","marks_gu":"૦૩ ગુણ",
   "a_en":"""<p><strong>Opening line:</strong> First open CB to break current, then open line isolator, then bus isolator, then close earth switch to ground line for work. CB must be open before isolator to avoid arcing under load.</p><p><strong>Closing line:</strong> Reverse: first open earth switch, then close bus isolator, then line isolator, finally close CB to energise. Check sync check relay for voltage matching. Interlock enforces order.</p>""",
   "a_gu":"""<p><strong>લાઇન ખોલવી:</strong> પહેલા CB ખોલો કરંટ તોડવા, પછી line isolator, પછી bus isolator, પછી earth switch બંધ કરી લાઇન earth કરો કામ માટે. isolator લોડે ખોલો તો ચિંગારી થાય તેથી CB પહેલા.</p><p><strong>લાઇન બંધ કરવી:</strong> ઊલટું: earth switch ખોલો, bus isolator બંધ, line isolator બંધ, છેલ્લે CB બંધ કરી ઊર્જા આપો. sync check થી વોલ્ટેજ મળતું તપાસો. interlock ક્રમ સાચવે.</p>""",
  },
  {
   "q_en":"Q.2 (b) OR Explain the importance of pad locking arrangement. (4 marks)",
   "marks_en":"4 marks","marks_gu":"૦૪ ગુણ",
   "a_en":"""<p><strong>Padlock = lockout tagout personal safety.</strong> Each work crew puts own padlock on isolator handle, earth switch, CB trolley so no one can operate while men work on line. Keys held by crew, only after all remove locks can close.</p><p>Prevents accidental energising by remote SCADA or another operator. Complies with factory act. Colour codes: red danger do not operate, yellow caution. Log book records who locked.</p>""",
   "a_gu":"""<p><strong>Padlock = lockout tagout વ્યક્તિ સલામતી.</strong> દરેક ટોળી પોતાનું તાળું isolator હાથો earth switch CB trolley પર લગાવે જેથી કોઈ ચાલુ ન કરી શકે માણસ કામ કરતા હોય ત્યાં. ચાવી ટોળી પાસે, બધા તાળા કાઢે પછી જ બંધ થાય.</p><p>અચાનક SCADA કે બીજા operator થી ચાલુ થતું અટકે. factory act પાલન. રંગ લાલ જોખમ ન ચલાવો પીળો સાવધ. log book માં નોંધ.</p>""",
  },
  {
   "q_en":"Q.2 (c) OR Draw and explain PLCC (Power Line Carrier Communication) schematic diagram. (7 marks)",
   "marks_en":"7 marks","marks_gu":"૦૭ ગુણ",
   "a_en":"""<p><strong>PLCC sends high frequency 40 to 500kHz speech and teleprotection over power line itself.</strong> Blocks: control room voice to carrier set modulator, coupling capacitor connects HF to line while blocking power frequency, line trap inductor blocks HF entering substation bus to keep it on line, at far end reverse.</p><p>Uses: speech between stations, relay carrier blocking or permissive trip signals, SCADA RTU data, no need for separate phone line even 200km. Limitation noise and attenuation, now partly replaced by fiber OPGW but still backup.</p>""" + svg_wrap(PLCC_SVG,"Carrier set → coupling capacitor → line trap → far end — HF on same conductor","PLCC"),
   "a_gu":"""<p><strong>PLCC ઉચ્ચ frequency 40 થી 500kHz વાત અને relay સિગ્નલ પાવર લાઇન પર જ મોકલે.</strong> ભાગ: કંટ્રોલ રૂમ વાત → carrier set modulator, coupling capacitor HF ને લાઇન પર જોડે પણ 50Hz રોકે, line trap inductor HF ને bus માં જતો રોકી લાઇન પર રાખે, સામે ઊલટું.</p><p>ઉપયોગ: સ્ટેશન વચ્ચે વાત, relay carrier સિગ્નલ, SCADA ડેટા, 200km સુધી અલગ ફોન લાઇન ન જોઈએ. ખામી ઘોંઘાટ attenuation, હવે fiber OPGW આવ્યું પણ backup તરીકે ચાલુ.</p>""" + svg_wrap(PLCC_SVG,"Carrier set → coupling capacitor → line trap → સામે છેડો — HF એ જ વાહક પર","PLCC"),
  },
 ]
},
{
 "title_en":"Q3 · Batteries, reclosers and monitoring",
 "title_gu":"પ્ર.3 · બેટરી રીક્લોઝર અને મોનિટરિંગ",
 "cards":[
  {
   "q_en":"Q.3 (a) Compare lead acid battery and Nickel cadmium battery. (3 marks)",
   "marks_en":"3 marks","marks_gu":"૦૩ ગુણ",
   "a_en":"""<table><tr><th>Point</th><th>Lead acid</th><th>Nickel Cadmium NiCd</th></tr><tr><td>Voltage per cell</td><td>2.0V nominal</td><td>1.2V nominal</td></tr><tr><td>Cost</td><td>Cheaper upfront</td><td>2 to 3 times costlier but long life 15 to 20 years</td></tr><tr><td>Maintenance</td><td>Vented needs water topping, hydrogen vent</td><td>Sealed low maintenance</td></tr><tr><td>Temperature</td><td>-10 to 40°C</td><td>-20 to 50°C wide, rugged</td></tr><tr><td>Self discharge</td><td>Higher</td><td>Lower</td></tr></table><p>Substation uses 110V DC: lead acid where staff present, NiCd where unmanned remote for reliability.</p>""" + svg_wrap(BATTERY_SVG,"Lead acid cheap vented vs NiCd rugged long life for DC trip supply","Battery compare"),
   "a_gu":"""<table><tr><th>મુદ્દો</th><th>Lead acid</th><th>NiCd</th></tr><tr><td>volt per cell</td><td>2.0V</td><td>1.2V</td></tr><tr><td>કિંમત</td><td>શરૂ માં સસ્તી</td><td>2 થી 3 ગણી મોંઘી પણ 15 થી 20 વર્ષ ચાલે</td></tr><tr><td>જાળવણી</td><td>પાણી નાખવું, hydrogen બહાર</td><td>સીલ ઓછી જાળવણી</td></tr><tr><td>તાપમાન</td><td>-10 થી 40°C</td><td>-20 થી 50°C પહોળું</td></tr><tr><td>self discharge</td><td>વધુ</td><td>ઓછું</td></tr></table><p>સબસ્ટેશન 110V DC: માણસ હોય ત્યાં lead acid, દૂર અમાનવ ત્યાં NiCd વિશ્વાસુ.</p>""" + svg_wrap(BATTERY_SVG,"Lead acid સસ્તી vented અને NiCd મજબૂત લાંબુ આયુષ્ય","Battery compare"),
  },
  {
   "q_en":"Q.3 (b) Explain the function of Auto recloser in detail. (4 marks)",
   "marks_en":"4 marks","marks_gu":"૦૪ ગુણ",
   "a_en":"""<p><strong>Auto recloser automatically re energises line after transient fault without crew.</strong> Most overhead faults 80% are transient lightning or branch touch that self clear when de energised briefly.</p><p>Sequence: fault sensed → CB trip → wait dead time 0.3 to 1 sec → reclose. If fault gone stay closed, if still there trip again → second reclose slower, if still fault lockout after 3 attempts and sectionaliser isolates.</p><p>Benefits less outage minutes, coordinated with sectionaliser and fuse, settings adjustable.</p>""" + svg_wrap(RECLOSER_SVG,"Fault trip → dead time → reclose — transient clears → stay, permanent → lockout","Auto recloser"),
   "a_gu":"""<p><strong>Auto recloser ક્ષણિક fault પછી જાતે લાઇન પાછી ચાલુ કરે માણસ વગર.</strong> 80% overhead fault ક્ષણિક વીજળી કે ડાળી અડવી જે થોડી વાર બંધ રહે તો જાતે મટે.</p><p>ક્રમ: fault લાગે → CB ટ્રિપ → 0.3 થી 1 sec રાહ → reclose. fault ગયો તો ચાલુ રહે, હોય તો ફરી ટ્રિપ → બીજું ધીમું reclose, હજુ હોય તો 3 વાર પછી lockout અને sectionaliser અલગ કરે.</p><p>ફાયદો outage ઓછો, sectionaliser fuse સાથે coordination.</p>""" + svg_wrap(RECLOSER_SVG,"Fault ટ્રિપ → dead time → reclose — ક્ષણિક મટે તો ચાલુ નહિ તો lockout","Auto recloser"),
  },
  {
   "q_en":"Q.3 (c) List out types of surge arrester and explain any one in detail. (7 marks)",
   "marks_en":"7 marks","marks_gu":"૦૭ ગુણ",
   "a_en":"""<p><strong>Types:</strong> Rod gap, horn gap, expulsion, silicon carbide with gaps, metal oxide gapless ZnO modern.</p><p><strong>Metal oxide ZnO detailed gapless:</strong> Stack of ZnO varistor discs between line and earth inside porcelain or polymer housing. At normal voltage resistance in mega ohms leakage micro amps. When surge like lightning doubles voltage, resistance collapses to few ohms, conducts kilo amps surge to earth clamping voltage to protective level ~1.5 times normal, then returns to high resistance. No power follow current, no gap sparking. Energy rating 2 to 10kJ per kV, discharge current 10kA nominal.</p><p>Placed near transformer bushing, line entrance, GIS, lead length short.</p>""" + svg_wrap(ARRESTER_SVG,"Gap obsolete vs silicon carbide vs modern gapless ZnO — normal high R surge low R","Surge arrester"),
   "a_gu":"""<p><strong>પ્રકાર:</strong> rod gap, horn gap, expulsion, silicon carbide gap સાથે, metal oxide gapless ZnO આધુનિક.</p><p><strong>Metal oxide ZnO વિગતે gapless:</strong> ZnO varistor discs લાઇન અને earth વચ્ચે porcelain કે polymer ઘર માં. સામાન્ય વોલ્ટેજે અવરોધ મેગા ઓહ્મ micro amp leakage. વીજળી surge બમણું થાય ત્યારે અવરોધ થોડા ઓહ્મ થઈ kilo amp surge earth માં લઈ જાય, વોલ્ટેજ 1.5 ગણું પકડી રાખે, પછી પાછો ઊંચો અવરોધ. gap ચિંગારી નહિ, follow કરંટ નહિ. energy 2 થી 10kJ per kV, 10kA.</p><p>ટ્રાન્સફોર્મર bushing લાઇન પ્રવેશ GIS પાસે નાનો lead.</p>""" + svg_wrap(ARRESTER_SVG,"Gap જૂનું vs silicon carbide vs gapless ZnO — સામાન્ય ઊંચો R surge નીચો R","Surge arrester"),
  },
  {
   "q_en":"Q.3 (a) OR State the desired properties of a line insulator. (3 marks)",
   "marks_en":"3 marks","marks_gu":"૦૩ ગુણ",
   "a_en":"""<ul><li>High electrical resistance to avoid leakage, high dielectric strength to withstand surge.</li><li>Mechanically strong to carry tension with wind and ice, good compressive strength.</li><li>Not porous, no cracks, glaze to shed water and pollution.</li><li>Withstands temperature, UV, acid from industry, non brittle.</li><li>High ratio of puncture to flashover, visible flashover before puncture preferred.</li></ul>""",
   "a_gu":"""<ul><li>વિદ્યુત અવરોધ ઊંચો leakage નહિ, dielectric તાકાત ઊંચી surge સહે.</li><li>યાંત્રિક મજબૂત વજન પવન બરફ તાણ ઝીલે.</li><li>છિદ્ર વગર તિરાડ વગર glaze થી પાણી પ્રદૂષણ સરે.</li><li>ગરમી UV acid સહે, બરડ નહિ.</li><li>puncture કરતાં flashover મોટો, flashover પહેલા દેખાય તો સારું.</li></ul>""",
  },
  {
   "q_en":"Q.3 (b) OR Explain switching scheme for 220KV substation for double bus with bus coupler. (4 marks)",
   "marks_en":"4 marks","marks_gu":"૦૪ ગુણ",
   "a_en":"""<p>Two main buses A and B both 220kV. Each feeder bay has two bus isolators one to A one to B plus CB and line isolator. Normal feeder on A, B standby.</p><p>For maintenance of A without outage: close bus coupler CB to parallel A and B, then shift feeder isolator from A to B one by one, then isolate A. Reverse to return. Coupler CB rated same as feeders and interlocked.</p><p>Adv flexibility and security, disadv more isolators and protection CT switching.</p>""" + svg_wrap(SWITCH_SCHEME_SVG,"Double bus A and B — feeder via two isolators plus coupler CB to shift without outage","Switching scheme"),
   "a_gu":"""<p>બે bus A B બંને 220kV. દરેક bay માં A અને B માટે બે isolator વત્તા CB. સામાન્ય A પર B standby.</p><p>A જાળવણી માટે outage વગર: bus coupler CB બંધ કરી A B સમાંતર, પછી ફીડર isolator એક પછી એક A થી B પર ફેરવો, પછી A અલગ કરો. પાછા એ જ રીતે. coupler CB rating સરખો, interlock.</p><p>ફાયદો લવચીકતા સુરક્ષા, ગેરલાભ વધુ isolator અને protection switch.</p>""" + svg_wrap(SWITCH_SCHEME_SVG,"Double bus A B — બે isolator વત્તા coupler થી outage વગર ફેરવો","Switching scheme"),
  },
  {
   "q_en":"Q.3 (c) OR Draw and explain block diagram of power flow and voltage monitoring system. (7 marks)",
   "marks_en":"7 marks","marks_gu":"૦૭ ગુણ",
   "a_en":"""<p><strong>Inputs CT VT from bays give I V to IED energy meter calculates P = V I cos φ, Q = V I sin φ, f, V.</strong> Values sent via RTU gateway over fiber or PLCC to SCADA.</p><p>System displays real time power direction arrows, voltage heat map, overload alarm if line exceeds thermal, under voltage if below 0.95 pu triggers tap changer or capacitor.</p><p>Operator sees trends, load flow estimation, predictive alerts before blackout.</p>""" + svg_wrap(MONITOR_PF_SVG,"CT VT → IED P Q V → RTU gateway → SCADA — alerts for overload tap","Power flow monitor"),
   "a_gu":"""<p><strong>CT VT થી I V IED મીટર માં P = V I cos φ Q = V I sin φ f V ગણે.</strong> RTU gateway fiber કે PLCC થી SCADA ને મોકલે.</p><p>સિસ્ટમ power દિશા તીર, વોલ્ટેજ heat map બતાવે, line overload કે V 0.95 pu થી નીચું તો alarm tap changer કે capacitor ચાલુ.</p><p>operator trend load flow અંદાજ blackout પહેલા ચેતવણી જુએ.</p>""" + svg_wrap(MONITOR_PF_SVG,"CT VT → IED P Q V → RTU → SCADA — overload tap alarm","Power flow monitor"),
  },
 ]
},
{
 "title_en":"Q4 · Earthing, maintenance and smart",
 "title_gu":"પ્ર.4 · અર્થિંગ જાળવણી અને સ્માર્ટ",
 "cards":[
  {
   "q_en":"Q.4 (a) State the objectives of earthing as per IS 3043. (3 marks)",
   "marks_en":"3 marks","marks_gu":"૦૩ ગુણ",
   "a_en":"""<ul><li>Provide low impedance path for fault current to earth to operate protection quickly.</li><li>Keep step and touch potentials within safe limits for personnel.</li><li>Maintain zero potential reference for relays and communication.</li><li>Protect equipment from overvoltage by providing discharge path.</li><li>Ensure reliable lightning discharge via earth grid.</li></ul>""",
   "a_gu":"""<ul><li>fault કરંટ ને earth માં ઓછા અવરોધે લઈ જઈ protection ઝડપી ચલાવો.</li><li>step અને touch potential માણસ માટે સલામત મર્યાદા માં રાખો.</li><li>relay કોમ્યુનિકેશન માટે zero reference.</li><li>overvoltage થી સાધન બચાવવા discharge path.</li><li>વીજળી discharge વિશ્વાસુ earth grid થી.</li></ul>""",
  },
  {
   "q_en":"Q.4 (b) Explain the need for preventive maintenance in substation. (4 marks)",
   "marks_en":"4 marks","marks_gu":"૦૪ ગુણ",
   "a_en":"""<p><strong>Preventive keeps failures before they happen instead of after.</strong></p><ul><li>Detect hot spots, loose contacts, oil degradation early via thermography DGA.</li><li>Extend life of transformer breaker by timely oil filtering, contact dressing, lubrication.</li><li>Reduce unplanned outage and revenue loss, improve SAIDI SAIFI indices.</li><li>Safety: avoid blast or fire from neglected pressure relief or bushing crack.</li></ul><p>Schedule daily visual, monthly battery and relay check, yearly oil test, 5 yearly major overhaul per manufacturer.</p>""",
   "a_gu":"""<p><strong>Preventive ખામી પછી નહિ પહેલા રોકે.</strong></p><ul><li>ગરમ જગ્યા ઢીલો contact તેલ બગાડ વહેલો પારખો thermography DGA થી.</li><li>સમયસર તેલ ગાળણ contact સમાર સ્નેહન થી ટ્રાન્સફોર્મર બ્રેકર આયુષ્ય વધે.</li><li>અણધાર્યું બંધ અને આવક નુકસાન ઘટે, SAIDI SAIFI સુધરે.</li><li>સલામતી: pressure relief bushing તિરાડ અવગણો તો ધડાકો આગ ટળે.</li></ul><p>રોજ દૃશ્ય, માસિક બેટરી relay, વાર્ષિક તેલ, 5 વર્ષે મોટું overhauling.</p>""",
  },
  {
   "q_en":"Q.4 (c) Explain step potential and touch potential with safety significance. (7 marks)",
   "marks_en":"7 marks","marks_gu":"૦૭ ગુણ",
   "a_en":"""<p><strong>When fault current enters earth grid, potential rises near injection point forming gradients.</strong></p><p><strong>Step potential:</strong> Voltage between two feet 1m apart while walking near fault. If mesh voltage gradient high, current flows feet to feet through body. Limit depends on body weight and duration per IEEE 80, typically 2 to 3kV for 0.5 sec with crushed rock.</p><p><strong>Touch potential:</strong> Voltage between hand touching earthed structure and feet on ground. More dangerous because heart in path. Limit lower about 1kV for same duration. Must be below tolerable E touch from calculation.</p><p>Design uses grid with meshes 5 to 10m, plus vertical rods, high resistivity crushed rock 2000 Ωm on surface to raise foot resistance, low earth resistance below 1Ω.</p>""" + svg_wrap(EARTH_POT_SVG,"Fault inject → gradients → step feet 1m, touch hand to feet — heart path more dangerous","Step touch"),
   "a_gu":"""<p><strong>fault કરંટ earth માં જાય ત્યારે inject જગ્યા પાસે potential ઊંચું gradient બને.</strong></p><p><strong>Step potential:</strong> fault પાસે ચાલતા બે પગ 1m વચ્ચે વોલ્ટેજ. gradient વધારે તો પગ થી પગ પ્રવાહ શરીર માં. મર્યાદા વજન સમય પર IEEE 80 પ્રમાણે 0.5 sec માટે crushed rock સાથે 2 થી 3kV.</p><p><strong>Touch potential:</strong> હાથ earth structure પર અને પગ જમીન પર વચ્ચે વોલ્ટેજ. વધારે જોખમી હૃદય વચ્ચે. મર્યાદા ઓછી ~1kV. ગણતરી E touch થી નીચે રાખવી.</p><p>ડિઝાઇન માં 5 થી 10m mesh વાળો grid વત્તા rod, સપાટી પર crushed rock 2000 Ωm પગ અવરોધ વધારવા, earth resistance 1Ω થી નીચો.</p>""" + svg_wrap(EARTH_POT_SVG,"Fault inject → gradient → step 1m touch હાથ થી પગ — હૃદય વધુ જોખમ","Step touch"),
  },
  {
   "q_en":"Q.4 (a) OR Explain the purpose of Hybrid Gas Insulation Substation (HGIS). (3 marks)",
   "marks_en":"3 marks","marks_gu":"૦૩ ગુણ",
   "a_en":"""<p><strong>HGIS mixes AIS and GIS:</strong> Bus stays air insulated cheap, but breaker isolator earth switch are in compact SF6 modules. Purpose is to get GIS reliability in polluted or space limited retrofit without paying for full GIS enclosure of whole bus.</p><p>Reduces size ~40%, maintenance free live parts, suitable for extending old AIS or indoor limited height.</p>""" + svg_wrap(HGIS_SVG,"Air bus cheap + SF6 bay compact — size 40% less, suits retrofit in city","HGIS"),
   "a_gu":"""<p><strong>HGIS AIS અને GIS નું મિશ્રણ:</strong> bus હવામાં સસ્તી રહે, પણ બ્રેકર isolator SF6 મોડ્યુલ માં compact. હેતુ પ્રદૂષિત કે જગ્યા ઓછી જૂની AIS ને full GIS ખર્ચ વગર GIS વિશ્વાસ આપવો.</p><p>કદ ~40% ઓછું, live ભાગ જાળવણી મુક્ત, જૂની AIS વધારવા કે ઓછી ઊંચાઈ માં અનુકૂળ.</p>""" + svg_wrap(HGIS_SVG,"હવા bus સસ્તી + SF6 bay compact — 40% નાનું શહેર retrofit અનુકૂળ","HGIS"),
  },
  {
   "q_en":"Q.4 (b) OR Explain the features of green substation. (4 marks)",
   "marks_en":"4 marks","marks_gu":"૦૪ ગુણ",
   "a_en":"""<ul><li>Uses eco gas g3 or dry air instead of SF6 where possible, natural ester oil transformers biodegradable.</li><li>Low energy: LED lighting, solar rooftop, efficient cooling, rain water harvesting.</li><li>Low noise and EMF design with setbacks vegetation screening.</li><li>Waste management recycling, bird diverters, oil containment pits no leak to soil.</li><li>Digital monitoring reduces site visits fuel, may get LEED certification and public acceptance.</li></ul>""" + svg_wrap(GREEN_SVG,"Eco gas, solar LED, rain harvest, low noise, bird friendly — low impact life cycle","Green substation"),
   "a_gu":"""<ul><li>SF6 બદલે eco gas g3 કે dry air, natural ester તેલ biodegradable.</li><li>ઓછી ઉર્જા: LED solar છત કાર્યક્ષમ કુલિંગ rain water.</li><li>ઓછો અવાજ EMF setback વૃક્ષ પડદો.</li><li>કચરો રિસાયકલ પક્ષી બચાવ oil pit જમીન માં ન જાય.</li><li>digital દેખરેખ થી મુલાકાત ઓછી LEED સર્ટિફિકેશન લોક સ્વીકાર.</li></ul>""" + svg_wrap(GREEN_SVG,"Eco gas solar LED rain low noise — જીવન ચક્ર અસર ઓછી","Green substation"),
  },
  {
   "q_en":"Q.4 (c) OR Draw and explain block diagram of smart grid based substation communication. (7 marks)",
   "marks_en":"7 marks","marks_gu":"૦૭ ગુણ",
   "a_en":"""<p><strong>Smart grid adds intelligence to traditional SCADA:</strong> Field CT VT → merging units digitise at 4kHz → process bus fiber to bay IEDs for protection using GOOSE trip in 4ms → station bus MMS to gateway → WAN to control centre plus DER and demand response servers.</p><p>Time sync via PTP, cybersecurity firewall, supports self healing — fault auto locates and isolates healthy sections remotely, integrates solar wind and storage, demand price signals.</p>""" + svg_wrap(SMARTGRID_SVG,"CT VT merging unit → IED GOOSE → station bus → gateway to centre with DER self healing","Smart grid comm"),
   "a_gu":"""<p><strong>Smart grid પરંપરાગત SCADA માં બુદ્ધિ ઉમેરે:</strong> CT VT → merging unit 4kHz digitise → process bus fiber bay IED GOOSE 4ms trip → station bus MMS gateway → WAN control centre વત્તા DER demand server.</p><p>PTP time sync firewall, self healing — fault જાતે શોધી તંદુરસ્ત ભાગ દૂર થી ચાલુ, solar wind storage જોડે, માંગ કિંમત સંકેત.</p>""" + svg_wrap(SMARTGRID_SVG,"CT VT merging unit → IED GOOSE → station bus → gateway DER self healing","Smart grid comm"),
  },
 ]
},
{
 "title_en":"Q5 · Digital, SCADA and HVDC",
 "title_gu":"પ્ર.5 · ડિજિટલ SCADA અને HVDC",
 "cards":[
  {
   "q_en":"Q.5 (a) State advantage and disadvantage of digital substation. (3 marks)",
   "marks_en":"3 marks","marks_gu":"૦૩ ગુણ",
   "a_en":"""<p><strong>Advantages:</strong> Massive copper reduction one fiber replaces 100s cores, less EMI, accurate non conventional sensors, flexible logic without rewiring, self diagnostics fast commissioning.</p><p><strong>Disadvantages:</strong> High initial cost, needs optical CT VT and merging units, cyber vulnerability, staff needs new skills, interoperability testing per IEC61850 needed.</p>""" + svg_wrap(DIGITAL_SVG,"Copper 100 cores → one fiber, less EMI, accurate, flexible but cost and cyber","Digital substation"),
   "a_gu":"""<p><strong>ફાયદા:</strong> તાંબું ઘણું ઓછું એક fiber 100 core બદલે, EMI ઓછો, non conventional સેન્સર સચોટ, rewiring વગર લવચીક logic, self તપાસ ઝડપી.</p><p><strong>ગેરલાભ:</strong> શરૂ ખર્ચ વધુ, optical CT VT merging unit જોઈએ, cyber જોખમ, નવી આવડત જોઈએ, IEC61850 પરીક્ષણ.</p>""" + svg_wrap(DIGITAL_SVG,"તાંબું 100 core → fiber, EMI ઓછો લવચીક પણ ખર્ચ cyber","Digital substation"),
  },
  {
   "q_en":"Q.5 (b) Explain three position disconnector/earthing switch used in GIS. (4 marks)",
   "marks_en":"4 marks","marks_gu":"૦૪ ગુણ",
   "a_en":"""<p><strong>One blade has three stable positions in one GIS enclosure:</strong> CLOSED connects to bus, OPEN isolated floating, EARTHED connects conductor to enclosure earth for safety.</p><p>Motor drive moves blade sequentially, mechanical interlock forbids direct CLOSED to EARTHED without passing OPEN, position feedback to control. Saves space and cost versus separate isolator and earth switch, one drive.</p>""" + svg_wrap(THREE_POS_SVG,"One blade CLOSED → OPEN → EARTHED — saves space in GIS, interlocked","Three position"),
   "a_gu":"""<p><strong>એક blade એક GIS ઘર માં ત્રણ સ્થિર સ્થાન:</strong> CLOSED bus સાથે, OPEN તરતું અલગ, EARTHED earth સાથે સલામતી.</p><p>મોટર ક્રમે ફેરવે interlock સીધું CLOSED થી EARTHED ન જાય OPEN થઈ ને જાય, position feedback. અલગ isolator earth switch કરતા જગ્યા ખર્ચ બચે એક drive.</p>""" + svg_wrap(THREE_POS_SVG,"એક blade CLOSED → OPEN → EARTHED — GIS માં જગ્યા બચે interlock","Three position"),
  },
  {
   "q_en":"Q.5 (c) Draw and explain digital monitoring of converter performance. (7 marks)",
   "marks_en":"7 marks","marks_gu":"૦૭ ગુણ",
   "a_en":"""<p><strong>Sensors on valves measure thyristor voltage, current, temperature via fiber optic isolated.</strong> Data to local IED computes firing alpha, commutation margin gamma, harmonics, losses.</p><p>Compare to digital twin expected values, flag abnormal: rising temperature means cooling fault, miss commutation means AC voltage dip. Alerts to HMI, trends predictive maintenance, avoids catastrophic valve failure.</p>""" + svg_wrap(CONVERTER_MON_SVG,"Valve U I T via fiber → IED analytics → HMI alert — twin predicts failure","Converter monitor"),
   "a_gu":"""<p><strong>valve પર સેન્સર thyristor વોલ્ટેજ કરંટ તાપમાન fiber થી માપે.</strong> IED alpha gamma harmonic loss ગણે.</p><p>digital twin સામે સરખાવે: તાપમાન વધે તો cooling ખામી, commutation miss તો AC dip. HMI ચેતવણી predictive જાળવણી valve નિષ્ફળતા ટાળે.</p>""" + svg_wrap(CONVERTER_MON_SVG,"Valve U I T fiber → IED → HMI — twin નિષ્ફળતા આગાહી","Converter monitor"),
  },
  {
   "q_en":"Q.5 (a) OR State the advantages of SCADA substation. (3 marks)",
   "marks_en":"3 marks","marks_gu":"૦૩ ગુણ",
   "a_en":"""<ul><li>Remote monitoring of all V I P Q breaker states from control centre, fewer site visits.</li><li>Faster fault location and restoration via remote control.</li><li>Data logging for post fault analysis and load forecasting.</li><li>Unmanned operation possible with alarms, reduces manpower cost.</li><li>Coordination across grid for optimal dispatch.</li></ul>""" + svg_wrap(SCADA_SVG,"Field IED → RTU → WAN → master — remote view control logging","SCADA"),
   "a_gu":"""<ul><li>બધા V I P Q breaker સ્થિતિ દૂર થી દેખરેખ મુલાકાત ઓછી.</li><li>fault ઝડપી શોધ પુનઃસ્થાપન remote control થી.</li><li>post fault વિશ્લેષણ load forecast માટે logging.</li><li>alarm સાથે માણસ વગર ચલાવી શકાય ખર્ચ ઓછો.</li><li>ગ્રીડ ભર coordination ઇષ્ટતમ dispatch.</li></ul>""" + svg_wrap(SCADA_SVG,"Field IED → RTU → WAN → master — દૂર દેખરેખ logging","SCADA"),
  },
  {
   "q_en":"Q.5 (b) OR Explain modern technologies used in digital substations. (4 marks)",
   "marks_en":"4 marks","marks_gu":"૦૩ ગુણ",
   "a_en":"""<ul><li><strong>Non conventional instrument transformers:</strong> Optical current and voltage, accurate wide range, light.</li><li><strong>Merging units:</strong> Sample analog at 80 per cycle digitise to IEC61850-9-2.</li><li><strong>Process bus fiber:</strong> Replaces copper, GOOSE peer peer trip.</li><li><strong>Time sync PTP:</strong> Microsecond accuracy for synchrophasor.</li><li><strong>Cybersecurity:</strong> Firewall intrusion detection, role based access.</li></ul>""",
   "a_gu":"""<ul><li><strong>Optical CT VT:</strong> પ્રકાશીય સચોટ હળવું.</li><li><strong>Merging unit:</strong> 80 sample per cycle digitise IEC61850-9-2.</li><li><strong>Process bus fiber:</strong> તાંબું બદલે GOOSE trip.</li><li><strong>PTP time sync:</strong> microsecond synchrophasor.</li><li><strong>Cyber સુરક્ષા:</strong> firewall intrusion.</li></ul>""",
  },
  {
   "q_en":"Q.5 (c) OR Draw and explain 12 pulse HVDC converter station in detail. (7 marks)",
   "marks_en":"7 marks","marks_gu":"૦૭ ગુણ",
   "a_en":"""<p><strong>Two 6 pulse bridges series gives 12 pulse:</strong> AC 400kV feed via two transformers: one Y-Y and one Y-Δgiving 30° phase shift. Each feeds one 6 pulse thyristor bridge. DC sides series add to ±500kV high power.</p><p>Harmonics improve: 5th 7th cancel leaving 11th 13th smaller so filters smaller. Includes converter transformer with tap, thyristor valve hall, smoothing reactor, AC/DC filters, DC breaker, control sets firing angles alpha for rectifier 15° inverter gamma 15° for power control and reversal.</p><p>Used for long distance bulk transmission and asynchronous intertie.</p>""" + svg_wrap(HVDC_SVG,"Y-Y plus Y-Δ 30° → two 6 pulse series → 12 pulse ±500kV low harmonics","12 pulse HVDC"),
   "a_gu":"""<p><strong>બે 6 pulse શ્રેણી →12 pulse:</strong> AC 400kV બે ટ્રાન્સફોર્મર Y-Y અને Y-Δ 30° shift વાળા દરેક એક 6 pulse thyristor bridge ને. DC શ્રેણી ±500kV વધુ power.</p><p>Harmonic સુધરે: 5th 7th cancel 11th 13th નાના filter નાના. ભાગ: tap વાળો ટ્રાન્સફોર્મર valve hall reactor filter DC breaker control alpha 15° gamma 15° થી power.</p><p>લાંબા અંતર મોટા transmission અને અલગ frequency જોડાણ માટે.</p>""" + svg_wrap(HVDC_SVG,"Y-Y અને Y-Δ 30° → બે 6 pulse શ્રેણી →12 pulse ±500kV harmonic ઓછો","12 pulse HVDC"),
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
            cards.append(f'''<details class="card"><summary><strong><span class="en">{q_html}</span><span class="gu">{q_html}</span></strong><small><span class="en">{(c["marks_en"])}</span><span class="gu">{(c["marks_gu"])}</span></small></summary><div class="answer"><div class="en">{c["a_en"]}</div><div class="gu">{c["a_gu"]}</div></div></details>''')
        sections_html.append(f'''<section class="group"><h2>{html.escape(sec["title_en"])}</h2>{''.join(cards)}</section>''')
    page=f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>DI04009011 · Summer 2026 solved paper</title><style>{CSS}</style></head><body><main class="page"><header class="hero"><div class="eyebrow">Solved question paper · English questions · Friendly Gujarati answers</div><div class="lang-switch" aria-label="Choose language"><button type="button" data-lang="en" aria-pressed="true">English</button><button type="button" data-lang="gu" aria-pressed="false">ગુજરાતી</button></div><h1>Substation Engineering</h1><div class="meta">GTU Diploma · Electrical · Semester 4 · Summer 2026 · DI04009011 · 21 May 2026 · 70 marks · 10:30 AM TO 01:00 PM</div></header>{''.join(sections_html)}<div class="footer">Solved paper for study. Verify clearances and ratings from official IE and utility standards before practice.</div></main><script>document.querySelectorAll('.lang-switch button').forEach(b=>b.addEventListener('click',()=>{{document.documentElement.lang=b.dataset.lang;document.querySelectorAll('.lang-switch button').forEach(x=>x.setAttribute('aria-pressed',x===b?'true':'false'));}}));</script></body></html>'''
    return page

def main():
    page=build_page()
    out_papers=ROOT/"papers-upload/papers/DI04009011/summer-2026.html"
    out_ws=ROOT/"preview/workshop/DI04009011_summer2026_bilingual.html"
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
    (ROOT/"drive-upload/DI04009011_summer_2026_bilingual.html").write_text(page,encoding="utf-8")

if __name__=="__main__":
    main()
