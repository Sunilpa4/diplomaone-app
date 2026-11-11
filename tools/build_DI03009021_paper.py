#!/usr/bin/env python3
"""Build DI03009021 Power Generation Summer 2026 — friendly Gujarati, minimal brackets."""
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

THERMAL_SCHEM = """<rect width="360" height="220" fill="#fff"/><text x="180" y="16" font-size="11" text-anchor="middle" font-weight="bold" fill="#164f73">Thermal Power Station — coal to electricity</text>
<rect x="12" y="38" width="70" height="30" rx="6" fill="#fff3e0" stroke="#b77e24"/><text x="47" y="52" font-size="6.5" text-anchor="middle">Coal yard</text><text x="47" y="60" font-size="5.5" text-anchor="middle">+ Boiler</text>
<rect x="95" y="38" width="70" height="30" rx="6" fill="#fce9e9" stroke="#c00"/><text x="130" y="52" font-size="6.5" text-anchor="middle">Turbine</text><text x="130" y="60" font-size="5.5" text-anchor="middle">+ Generator</text>
<rect x="178" y="38" width="70" height="30" rx="6" fill="#eaf4fa" stroke="#145c8b"/><text x="213" y="52" font-size="6.5" text-anchor="middle">Condenser</text><text x="213" y="60" font-size="5.5" text-anchor="middle">+ Cooling tower</text>
<rect x="260" y="38" width="70" height="30" rx="6" fill="#efe3fa" stroke="#7B2CD9"/><text x="295" y="52" font-size="6.5" text-anchor="middle">Transformer</text><text x="295" y="60" font-size="5.5" text-anchor="middle">+ Grid</text>
<path d="M82 53 L95 53" stroke="#333" stroke-width="1.5" marker-end="url(#a)"/><path d="M165 53 L178 53" stroke="#333" stroke-width="1.5"/><path d="M248 53 L260 53" stroke="#333" stroke-width="1.5"/>
<text x="88" y="45" font-size="5" fill="#666">steam</text><text x="170" y="45" font-size="5" fill="#666">exhaust</text>
<rect x="45" y="85" width="270" height="70" rx="8" fill="#f7f9fb" stroke="#d9e1e7"/><text x="180" y="98" font-size="6.5" text-anchor="middle" font-weight="bold">Heat recovery — Economizer → Air preheater → ESP → Chimney</text><text x="180" y="112" font-size="6" text-anchor="middle" fill="#333">Coal in → heat → superheated steam → shaft work → AC after step up</text><text x="180" y="128" font-size="6" text-anchor="middle" fill="#666">Condensate pump returns water, FD fan supplies air, ash handled separately</text>
<text x="180" y="180" font-size="6.5" text-anchor="middle" fill="#0a7a2e">Net output less than gross due to auxiliaries and condenser loss</text>"""

AUX_SVG = """<rect width="360" height="220" fill="#fff"/><text x="180" y="16" font-size="11" text-anchor="middle" font-weight="bold" fill="#164f73">Thermal auxiliaries — what each does</text>
<g font-size="6.5">
<rect x="10" y="30" width="105" height="34" rx="6" fill="#fff3e0" stroke="#b77e24"/><text x="62" y="44" text-anchor="middle" font-weight="bold">Boiler</text><text x="62" y="54" text-anchor="middle">makes high pressure steam</text>
<rect x="125" y="30" width="105" height="34" rx="6" fill="#eaf4fa" stroke="#145c8b"/><text x="177" y="44" text-anchor="middle" font-weight="bold">Economizer</text><text x="177" y="54" text-anchor="middle">preheats feed water</text>
<rect x="240" y="30" width="105" height="34" rx="6" fill="#fce9e9" stroke="#c00"/><text x="292" y="44" text-anchor="middle" font-weight="bold">FD Fan + APH</text><text x="292" y="54" text-anchor="middle">air for burning</text>
<rect x="10" y="75" width="105" height="34" rx="6" fill="#efe3fa" stroke="#7B2CD9"/><text x="62" y="89" text-anchor="middle" font-weight="bold">Turbine</text><text x="62" y="99" text-anchor="middle">steam to shaft</text>
<rect x="125" y="75" width="105" height="34" rx="6" fill="#f1fbf6" stroke="#77a795"/><text x="177" y="89" text-anchor="middle" font-weight="bold">Condenser</text><text x="177" y="99" text-anchor="middle">condenses exhaust</text>
<rect x="240" y="75" width="105" height="34" rx="6" fill="#f7f9fb" stroke="#888"/><text x="292" y="89" text-anchor="middle" font-weight="bold">Cooling Tower</text><text x="292" y="99" text-anchor="middle">rejects waste heat</text>
</g>
<text x="180" y="130" font-size="7" text-anchor="middle" fill="#333">All auxiliaries support safe steady steam cycle and clean flue gas</text>"""

ENERGY_THERM_SVG = """<rect width="360" height="220" fill="#fff"/><text x="180" y="16" font-size="11" text-anchor="middle" font-weight="bold" fill="#164f73">Energy conversion in thermal station</text>
<rect x="20" y="50" width="70" height="30" rx="6" fill="#8a5a00" stroke="#5a3800"/><text x="55" y="62" font-size="6.5" text-anchor="middle" fill="#fff">Chemical</text><text x="55" y="70" font-size="5.5" text-anchor="middle" fill="#fff">coal</text>
<rect x="110" y="50" width="70" height="30" rx="6" fill="#c00" stroke="#8a0000"/><text x="145" y="62" font-size="6.5" text-anchor="middle" fill="#fff">Heat</text><text x="145" y="70" font-size="5.5" text-anchor="middle" fill="#fff">furnace</text>
<rect x="200" y="50" width="70" height="30" rx="6" fill="#145c8b" stroke="#0e3d5e"/><text x="235" y="62" font-size="6.5" text-anchor="middle" fill="#fff">Mechanical</text><text x="235" y="70" font-size="5.5" text-anchor="middle" fill="#fff">turbine shaft</text>
<rect x="285" y="50" width="60" height="30" rx="6" fill="#eab308" stroke="#8a6500"/><text x="315" y="62" font-size="6.5" text-anchor="middle">Electrical</text><text x="315" y="70" font-size="5.5" text-anchor="middle">generator</text>
<path d="M90 65 L110 65" stroke="#333" stroke-width="1.5"/><path d="M180 65 L200 65" stroke="#333" stroke-width="1.5"/><path d="M270 65 L285 65" stroke="#333" stroke-width="1.5"/>
<text x="180" y="110" font-size="7" text-anchor="middle" fill="#333">Fuel burns → water becomes steam → steam pushes blades → rotor makes AC</text>
<text x="180" y="135" font-size="6.5" text-anchor="middle" fill="#666">Transformer raises voltage for transmission, not energy source</text>"""

STEAM_CYCLE_SVG = """<rect width="360" height="220" fill="#fff"/><text x="180" y="16" font-size="11" text-anchor="middle" font-weight="bold" fill="#164f73">Feed water and steam cycle — closed loop</text>
<path d="M40 60 L120 60 L120 40 L240 40 L240 60 L320 60 L320 120 L40 120 Z" fill="none" stroke="#145c8b" stroke-width="1.6"/>
<circle cx="80" cy="60" r="6" fill="#c00"/><text x="80" y="78" font-size="5.5" text-anchor="middle">Boiler</text>
<circle cx="180" cy="40" r="6" fill="#7B2CD9"/><text x="180" y="25" font-size="5.5" text-anchor="middle">Turbine</text>
<circle cx="280" cy="60" r="6" fill="#145c8b"/><text x="280" y="78" font-size="5.5" text-anchor="middle">Condenser</text>
<circle cx="180" cy="120" r="6" fill="#77a795"/><text x="180" y="138" font-size="5.5" text-anchor="middle">Feed pump + heaters</text>
<text x="130" y="52" font-size="5.5" fill="#c00">superheated steam →</text><text x="230" y="52" font-size="5.5" fill="#666">exhaust ↓</text>
<text x="180" y="110" font-size="5.5" fill="#77a795">condensate back ↑</text>
<text x="180" y="165" font-size="6.5" text-anchor="middle" fill="#333">Economizer and heaters recover heat before boiler</text>"""

SURGE_SVG = """<rect width="360" height="220" fill="#fff"/><text x="180" y="16" font-size="11" text-anchor="middle" font-weight="bold" fill="#164f73">Surge tank and penstock — pressure control for hydro</text>
<path d="M40 40 L140 40 L140 90 L60 90 Z" fill="#eaf4fa" stroke="#145c8b"/><text x="90" y="58" font-size="6" text-anchor="middle">Reservoir</text><text x="90" y="68" font-size="5" text-anchor="middle">intake gate</text>
<rect x="140" y="70" width="110" height="14" fill="#b77e24" stroke="#8a5a00"/><text x="195" y="80" font-size="5.5" text-anchor="middle" fill="#fff">Headrace tunnel</text>
<rect x="170" y="35" width="22" height="60" rx="4" fill="#fff" stroke="#c00" stroke-width="1.4"/><text x="181" y="55" font-size="5" text-anchor="middle" fill="#c00">Surge</text><text x="181" y="62" font-size="5" text-anchor="middle" fill="#c00">tank</text>
<path d="M250 84 L285 140" stroke="#333" stroke-width="4"/><text x="240" y="115" font-size="5.5" fill="#333">Penstock</text><text x="290" y="155" font-size="6" text-anchor="middle">Turbine + generator</text>
<text x="180" y="180" font-size="6.5" text-anchor="middle" fill="#333">Surge tank absorbs hammer when gates close quickly</text>
<text x="180" y="193" font-size="6" text-anchor="middle" fill="#666">Catchment is whole rain area, reservoir is stored water part</text>"""

HYDRO_CLASS_SVG = """<rect width="360" height="220" fill="#fff"/><text x="180" y="16" font-size="11" text-anchor="middle" font-weight="bold" fill="#164f73">Hydro classification — head, storage and duty</text>
<g font-size="6.5">
<rect x="10" y="32" width="105" height="36" rx="6" fill="#eaf4fa" stroke="#145c8b"/><text x="62" y="46" text-anchor="middle" font-weight="bold">By head</text><text x="62" y="56" text-anchor="middle">high / medium / low</text>
<rect x="125" y="32" width="105" height="36" rx="6" fill="#fff3e0" stroke="#b77e24"/><text x="177" y="46" text-anchor="middle" font-weight="bold">By storage</text><text x="177" y="56" text-anchor="middle">run-of-river / pondage / reservoir</text>
<rect x="240" y="32" width="105" height="36" rx="6" fill="#f1fbf6" stroke="#77a795"/><text x="292" y="46" text-anchor="middle" font-weight="bold">By duty</text><text x="292" y="56" text-anchor="middle">base / peak / pumped</text>
</g>
<text x="180" y="90" font-size="7" text-anchor="middle" fill="#333">Schemes — dam-toe, diversion canal, pumped storage with reversible machines</text>
<text x="180" y="110" font-size="6.5" text-anchor="middle" fill="#666">Pelton for high head, Francis for medium, Kaplan for low head</text>"""

SOLAR_DEF_SVG = """<rect width="360" height="220" fill="#fff"/><text x="180" y="16" font-size="11" text-anchor="middle" font-weight="bold" fill="#164f73">Solar cell to array — how pieces join</text>
<rect x="15" y="50" width="70" height="36" rx="6" fill="#eab308" stroke="#8a6500"/><text x="50" y="64" font-size="6" text-anchor="middle">1 Cell</text><text x="50" y="74" font-size="5" text-anchor="middle">0.5 V small</text>
<rect x="95" y="50" width="75" height="36" rx="6" fill="#fde68a" stroke="#b45309"/><text x="132" y="64" font-size="6" text-anchor="middle">Module</text><text x="132" y="74" font-size="5" text-anchor="middle">cells in series</text>
<rect x="180" y="50" width="80" height="36" rx="6" fill="#fff3e0" stroke="#b77e24"/><text x="220" y="64" font-size="6" text-anchor="middle">Panel</text><text x="220" y="74" font-size="5" text-anchor="middle">module + frame + glass</text>
<rect x="270" y="50" width="75" height="36" rx="6" fill="#eaf4fa" stroke="#145c8b"/><text x="307" y="64" font-size="6" text-anchor="middle">Array</text><text x="307" y="74" font-size="5" text-anchor="middle">many panels + wiring</text>
<path d="M85 68 L95 68" stroke="#333" stroke-width="1.2"/><path d="M170 68 L180 68" stroke="#333" stroke-width="1.2"/><path d="M260 68 L270 68" stroke="#333" stroke-width="1.2"/>
<text x="180" y="120" font-size="7" text-anchor="middle" fill="#333">Example 36 cells → 18 V module → panel same, array adds power</text>"""

NUCLEAR_SVG = """<rect width="360" height="220" fill="#fff"/><text x="180" y="16" font-size="11" text-anchor="middle" font-weight="bold" fill="#164f73">Nuclear station — heat from fission to steam to power</text>
<rect x="20" y="40" width="80" height="32" rx="6" fill="#fde68a" stroke="#b45309"/><text x="60" y="54" font-size="6.5" text-anchor="middle">Reactor</text><text x="60" y="62" font-size="5" text-anchor="middle">fission heat</text>
<rect x="120" y="40" width="70" height="32" rx="6" fill="#eaf4fa" stroke="#145c8b"/><text x="155" y="54" font-size="6.5" text-anchor="middle">Steam gen</text><text x="155" y="62" font-size="5" text-anchor="middle">heat exchanger</text>
<rect x="210" y="40" width="70" height="32" rx="6" fill="#fce9e9" stroke="#c00"/><text x="245" y="54" font-size="6.5" text-anchor="middle">Turbine</text><text x="245" y="62" font-size="5" text-anchor="middle">+ Gen</text>
<rect x="295" y="40" width="50" height="32" rx="6" fill="#eaf4fa" stroke="#333"/><text x="320" y="54" font-size="6.5" text-anchor="middle">Grid</text>
<path d="M100 56 L120 56" stroke="#333" stroke-width="1.2"/><path d="M190 56 L210 56" stroke="#333" stroke-width="1.2"/><path d="M280 56 L295 56" stroke="#333" stroke-width="1.2"/>
<rect x="40" y="95" width="280" height="50" rx="8" fill="#f7f9fb" stroke="#d9e1e7"/><text x="180" y="108" font-size="6.5" text-anchor="middle" font-weight="bold">Reactor core — fuel rods, moderator, control rods, coolant, shielding</text><text x="180" y="122" font-size="6" text-anchor="middle" fill="#333">Control rods absorb neutrons to control chain reaction</text><text x="180" y="135" font-size="5.5" text-anchor="middle" fill="#666">PWR keeps water pressurised, BWR boils directly, PHWR uses heavy water</text>"""

ROOFTOP_SVG = """<rect width="360" height="220" fill="#fff"/><text x="180" y="16" font-size="11" text-anchor="middle" font-weight="bold" fill="#164f73">Rooftop PV — standalone vs grid connected</text>
<rect x="20" y="45" width="150" height="70" rx="8" fill="#fff3e0" stroke="#b77e24"/><text x="95" y="60" font-size="6.5" text-anchor="middle" font-weight="bold">Standalone</text><text x="95" y="72" font-size="5.5" text-anchor="middle">PV → charge controller → battery</text><text x="95" y="82" font-size="5.5" text-anchor="middle">→ inverter → load</text><text x="95" y="94" font-size="5" text-anchor="middle" fill="#666">no grid, night from battery</text>
<rect x="190" y="45" width="150" height="70" rx="8" fill="#eaf4fa" stroke="#145c8b"/><text x="265" y="60" font-size="6.5" text-anchor="middle" font-weight="bold">Grid connected</text><text x="265" y="72" font-size="5.5" text-anchor="middle">PV → inverter → meter → grid</text><text x="265" y="82" font-size="5.5" text-anchor="middle">net metering sells extra</text><text x="265" y="94" font-size="5" text-anchor="middle" fill="#666">grid acts as storage</text>
<text x="180" y="135" font-size="6.5" text-anchor="middle" fill="#333">Hybrid adds battery to grid system for backup</text>"""

WIND_SVG = """<rect width="360" height="220" fill="#fff"/><text x="180" y="16" font-size="11" text-anchor="middle" font-weight="bold" fill="#164f73">Wind to electricity — air to shaft to generator</text>
<path d="M20 50 Q40 40 60 50 Q40 60 20 50" fill="#eaf4fa" stroke="#145c8b"/><text x="40" y="72" font-size="5.5" text-anchor="middle">Wind</text>
<rect x="90" y="45" width="70" height="30" rx="6" fill="#fff3e0" stroke="#b77e24"/><text x="125" y="58" font-size="6" text-anchor="middle">Rotor + blades</text><text x="125" y="68" font-size="5" text-anchor="middle">captures power</text>
<rect x="175" y="45" width="70" height="30" rx="6" fill="#f1fbf6" stroke="#77a795"/><text x="210" y="58" font-size="6" text-anchor="middle">Gearbox +</text><text x="210" y="68" font-size="5" text-anchor="middle">Generator</text>
<rect x="260" y="45" width="70" height="30" rx="6" fill="#eaf4fa" stroke="#145c8b"/><text x="295" y="58" font-size="6" text-anchor="middle">Transformer</text><text x="295" y="68" font-size="5" text-anchor="middle">to grid</text>
<path d="M60 50 L90 60" stroke="#333" stroke-width="1.2"/><path d="M160 60 L175 60" stroke="#333" stroke-width="1.2"/><path d="M245 60 L260 60" stroke="#333" stroke-width="1.2"/>
<text x="180" y="110" font-size="6.5" text-anchor="middle" fill="#333">Power = 0.5·ρ·A·v³·Cp — more wind, bigger swept area, higher Cp</text>"""

HAWT_VAWT_SVG = """<rect width="360" height="220" fill="#fff"/><text x="180" y="16" font-size="11" text-anchor="middle" font-weight="bold" fill="#164f73">HAWT vs VAWT — axis difference</text>
<g transform="translate(20,35)">
<line x1="50" y1="20" x2="50" y2="90" stroke="#8a5a00" stroke-width="3"/><path d="M50 20 L20 25 L50 20 L80 25" fill="#eaf4fa" stroke="#145c8b"/><text x="50" y="110" font-size="6" text-anchor="middle">HAWT</text><text x="50" y="120" font-size="5" text-anchor="middle">high efficiency, needs yaw</text>
</g>
<g transform="translate(180,35)">
<line x1="50" y1="20" x2="50" y2="90" stroke="#8a5a00" stroke-width="3"/><path d="M30 30 Q50 20 70 30 Q50 70 30 30" fill="none" stroke="#145c8b" stroke-width="1.5"/><text x="50" y="110" font-size="6" text-anchor="middle">VAWT Darrieus</text><text x="50" y="120" font-size="5" text-anchor="middle">omnidirectional, lower Cp</text>
</g>
<text x="180" y="150" font-size="6.5" text-anchor="middle" fill="#333">HAWT 3 blades upwind, high tip speed; VAWT Savonius self-start but less power</text>"""

DIESEL_SVG = """<rect width="360" height="220" fill="#fff"/><text x="180" y="16" font-size="11" text-anchor="middle" font-weight="bold" fill="#164f73">Diesel power station — block diagram</text>
<rect x="15" y="55" width="60" height="30" rx="6" fill="#fff3e0" stroke="#b77e24"/><text x="45" y="68" font-size="5.5" text-anchor="middle">Fuel tank</text>
<rect x="85" y="55" width="65" height="30" rx="6" fill="#fce9e9" stroke="#c00"/><text x="117" y="68" font-size="5.5" text-anchor="middle">Diesel engine</text>
<rect x="160" y="55" width="65" height="30" rx="6" fill="#eaf4fa" stroke="#145c8b"/><text x="192" y="68" font-size="5.5" text-anchor="middle">Alternator</text>
<rect x="235" y="55" width="55" height="30" rx="6" fill="#f1fbf6" stroke="#77a795"/><text x="262" y="68" font-size="5.5" text-anchor="middle">Cooling</text>
<rect x="295" y="55" width="50" height="30" rx="6" fill="#efe3fa" stroke="#7B2CD9"/><text x="320" y="68" font-size="5.5" text-anchor="middle">Exhaust</text>
<path d="M75 70 L85 70" stroke="#333" stroke-width="1.2"/><path d="M150 70 L160 70" stroke="#333" stroke-width="1.2"/><text x="180" y="110" font-size="6.5" text-anchor="middle" fill="#333">Engine drives generator directly, governor controls fuel for load</text>"""

LOAD_CURVE_SVG = """<rect width="360" height="220" fill="#fff"/><text x="180" y="16" font-size="11" text-anchor="middle" font-weight="bold" fill="#164f73">Load curve and load duration curve</text>
<path d="M40 150 L300 150" stroke="#333" stroke-width="1.2"/><path d="M40 150 L40 40" stroke="#333" stroke-width="1.2"/>
<path d="M40 130 L80 100 L120 80 L160 60 L200 70 L240 100 L280 120 L300 120" fill="none" stroke="#c00" stroke-width="2"/>
<text x="170" y="135" font-size="6" fill="#c00">Daily load curve — peak 20 MW, average lower</text>
<path d="M40 150 L40 30 L50 30 L50 140 L70 140 L70 50 L90 50 L90 130 L300 130 L300 150" fill="#eaf4fa" stroke="#145c8b" stroke-width="0.8" opacity="0.6"/>
<text x="180" y="170" font-size="6.5" text-anchor="middle" fill="#333">Area under curve is energy kWh. From it we get max demand, average, load factor, plant factor</text>"""

BIO_SVG = """<rect width="360" height="220" fill="#fff"/><text x="180" y="16" font-size="11" text-anchor="middle" font-weight="bold" fill="#164f73">Bio-chemical plant — waste to biogas to power</text>
<rect x="15" y="50" width="80" height="30" rx="6" fill="#fde68a" stroke="#b45309"/><text x="55" y="64" font-size="6" text-anchor="middle">Biomass / waste</text>
<rect x="105" y="50" width="80" height="30" rx="6" fill="#f1fbf6" stroke="#77a795"/><text x="145" y="64" font-size="6" text-anchor="middle">Digester</text><text x="145" y="72" font-size="5" text-anchor="middle">anaerobic</text>
<rect x="195" y="50" width="80" height="30" rx="6" fill="#fce9e9" stroke="#c00"/><text x="235" y="64" font-size="6" text-anchor="middle">Biogas holder</text>
<rect x="285" y="50" width="60" height="30" rx="6" fill="#eaf4fa" stroke="#145c8b"/><text x="315" y="64" font-size="6" text-anchor="middle">Engine + Gen</text>
<path d="M95 65 L105 65" stroke="#333" stroke-width="1.2"/><path d="M185 65 L195 65" stroke="#333" stroke-width="1.2"/><path d="M275 65 L285 65" stroke="#333" stroke-width="1.2"/>
<text x="180" y="110" font-size="6.5" text-anchor="middle" fill="#333">Microbes break waste without oxygen and make methane rich biogas</text>"""

FUELCELL_SVG = """<rect width="360" height="220" fill="#fff"/><text x="180" y="16" font-size="11" text-anchor="middle" font-weight="bold" fill="#164f73">Fuel cell — hydrogen and oxygen make water and power</text>
<rect x="30" y="60" width="100" height="40" rx="8" fill="#eaf4fa" stroke="#145c8b"/><text x="80" y="74" font-size="6" text-anchor="middle">Anode H2 → 2H+ +2e-</text><text x="80" y="84" font-size="5" text-anchor="middle">electrolyte passes H+</text>
<rect x="230" y="60" width="100" height="40" rx="8" fill="#fce9e9" stroke="#c00"/><text x="280" y="74" font-size="6" text-anchor="middle">Cathode O2 +2H+ +2e- → H2O</text>
<path d="M130 80 L230 80" stroke="#333" stroke-width="1.2" stroke-dasharray="3 3"/><text x="180" y="75" font-size="5" fill="#666">electrons via external load do work</text>
<text x="180" y="125" font-size="6.5" text-anchor="middle" fill="#333">Types — PEMFC, PAFC, MCFC, SOFC, AFC by electrolyte and temp</text>"""

SECTIONS=[
{
 "title_en":"Q1 · Thermal and nuclear basics",
 "title_gu":"પ્ર.1 · થર્મલ અને ન્યુક્લિયર બેઝિક",
 "cards":[
  {
   "q_en":"Q.1 (a) Explain site selection of Thermal Power Station. (3 marks)",
   "marks_en":"3 marks","marks_gu":"૦૩ ગુણ",
   "a_en":"""<p><strong>Site selection factors for thermal station:</strong></p><ol><li><strong>Fuel & water:</strong> Near coal mine or port/rail for coal transport; abundant cooling water from river/sea.</li><li><strong>Load & grid:</strong> Not too far from demand centre to reduce transmission loss; good road/rail access.</li><li><strong>Land & environment:</strong> Large flat land for plant, ash pond, future expansion; away from dense habitation but consider ash disposal and pollution control; soil must bear heavy foundations.</li></ol>""",
   "a_gu":"""<p><strong>થર્મલ પાવર સ્ટેશન માટે જગ્યા પસંદ કરતી વખતે ધ્યાને લેવાની બાબતો:</strong></p><ol><li><strong>બળતણ અને પાણી:</strong> કોલસાની ખાણ કે બંદર કે રેલવે નજીક હોય તો કોલસો લાવવો સસ્તો પડે અને ઠંડુ કરવા માટે નદી કે દરિયા નું પાણી મળવું જોઈએ.</li><li><strong>લોડ અને ગ્રીડ:</strong> વીજળી વાપરવાનું સ્થળ બહુ દૂર ન હોય તો લાઇન લોસ ઓછો થાય અને રસ્તા રેલવે ની સારી સુવિધા હોય.</li><li><strong>જમીન અને પર્યાવરણ:</strong> પ્લાન્ટ, રાખ ના તળાવ અને ભવિષ્ય ના વિસ્તરણ માટે મોટી સપાટ જમીન જોઈએ, ગીચ વસ્તી થી દૂર હોય અને જમીન ભારે મશીન નું વજન સહન કરી શકે.</li></ol>""",
  },
  {
   "q_en":"Q.1 (b) Explain Nuclear Fusion, Nuclear Fission and Chain reaction. (4 marks)",
   "marks_en":"4 marks","marks_gu":"૦૪ ગુણ",
   "a_en":"""<p><strong>Fission:</strong> Heavy nucleus like U-235 splits into smaller nuclei when hit by neutron and releases huge energy plus 2-3 new neutrons.</p><p><strong>Fusion:</strong> Two very light nuclei like hydrogen join to form heavier nucleus and release even more energy per mass. Needs millions of degrees, happens in sun.</p><p><strong>Chain reaction:</strong> Neutrons from one fission hit other U atoms and cause more fissions continuously. Controlled by control rods in reactor, uncontrolled causes explosion.</p>""",
   "a_gu":"""<p><strong>ફિશન એટલે ભારે ન્યુક્લિયસ તૂટવું:</strong> યુરેનિયમ 235 જેવો ભારે કણ ન્યુટ્રોન અથડાતા નાના ટુકડા માં તૂટે છે અને ઘણી ગરમી સાથે બે ત્રણ નવા ન્યુટ્રોન બહાર આવે છે.</p><p><strong>ફ્યુઝન એટલે હલકા કણો જોડાવા:</strong> હાઇડ્રોજન જેવા હલકા કણો જોડાઈ ને ભારે કણ બને છે અને વજન દીઠ ફિશન કરતા વધુ ઊર્જા આપે છે. સૂર્ય માં આ પ્રક્રિયા થાય છે અને લાખો ડિગ્રી ગરમી જોઈએ.</p><p><strong>ચેઇન રિએક્શન એટલે સાંકળ:</strong> એક ફિશન માંથી નીકળેલ ન્યુટ્રોન બીજા યુરેનિયમ ને તોડે અને આમ સતત પ્રક્રિયા ચાલે. રિએક્ટર માં કંટ્રોલ રોડ આને કાબૂ માં રાખે છે.</p>""",
  },
  {
   "q_en":"Q.1 (c) Draw Schematic Diagram of Thermal Power Station. (7 marks)",
   "marks_en":"7 marks","marks_gu":"૦૭ ગુણ",
   "a_en":"""<p><strong>Main parts from coal to grid:</strong> Coal handling → Pulveriser → Boiler with economizer, superheater, air preheater and FD fan → Turbine coupled to generator → Condenser with cooling tower → Feed pump and heaters back to boiler → ESP, chimney for flue gas → Ash handling. Transformer steps up to grid.</p><p><strong>Working in brief:</strong> Coal burns, water becomes high pressure steam, steam turns turbine, turbine turns generator, exhaust steam condenses and returns as feed water. Heat recovery improves efficiency.</p>""" + svg_wrap(THERMAL_SCHEM,"Thermal schematic — coal → boiler → turbine → condenser → feed pump loop","Thermal schematic"),
   "a_gu":"""<p><strong>કોલસા થી ગ્રીડ સુધી ના મુખ્ય ભાગો:</strong> કોલસો લાવવો → દળવો → બોઇલર જેમાં ઇકોનોમાઇઝર, સુપરહીટર, એર પ્રીહીટર અને FD ફેન હોય → ટર્બાઇન જે જનરેટર સાથે જોડેલ હોય → કન્ડેન્સર અને કુલિંગ ટાવર → ફીડ પંપ અને હીટર પાછા બોઇલર તરફ → ધુમાડા માટે ESP અને ચીમની → રાખ નિકાલ. ટ્રાન્સફોર્મર વોલ્ટેજ વધારી ગ્રીડ માં મોકલે.</p><p><strong>ટૂંક માં કામ:</strong> કોલસો બળે, પાણી હાઇ પ્રેશર વરાળ બને, વરાળ ટર્બાઇન ફેરવે, ટર્બાઇન જનરેટર ફેરવે, વરાળ પાછી પાણી બને અને ફરી બોઇલર માં જાય. ગરમી નો ફેર ઉપયોગ કાર્યક્ષમતા વધારે.</p>""" + svg_wrap(THERMAL_SCHEM,"થર્મલ સ્કીમેટિક — કોલસો → બોઇલર → ટર્બાઇન → કન્ડેન્સર → ફીડ પંપ લૂપ","Thermal schematic"),
  },
  {
   "q_en":"Q.1 (c) OR Explain the function of following auxiliaries of Thermal Power Station : (1) Boiler (2) Economizer (3) F. D. Fan (4) Air Preheater (5) Condenser (6) Turbine (7) Cooling Tower (7 marks)",
   "marks_en":"7 marks","marks_gu":"૦૭ ગુણ",
   "a_en":"""<ol><li><strong>Boiler:</strong> Burns fuel and transfers heat to water to make high pressure steam.</li><li><strong>Economizer:</strong> Uses leftover flue gas heat to warm feed water before boiler, saves fuel.</li><li><strong>FD Fan:</strong> Forces fresh air into furnace for proper burning.</li><li><strong>Air Preheater:</strong> Heats incoming air using hot flue gas, improves burning.</li><li><strong>Condenser:</strong> Condenses exhaust steam to water and keeps low pressure at turbine exit.</li><li><strong>Turbine:</strong> Converts steam energy to rotating shaft work to drive generator.</li><li><strong>Cooling Tower:</strong> Cools condenser water by air so heat can be rejected.</li></ol>""" + svg_wrap(AUX_SVG,"Thermal auxiliaries — boiler, economizer, FD fan, air preheater, condenser, turbine, cooling tower","Thermal auxiliaries"),
   "a_gu":"""<ol><li><strong>બોઇલર:</strong> બળતણ બાળી પાણી ને ગરમ કરી હાઇ પ્રેશર વરાળ બનાવે.</li><li><strong>ઇકોનોમાઇઝર:</strong> ચીમની માં જતા ગરમ ધુમાડા ની ગરમી થી ફીડ વોટર ને પહેલા ગરમ કરી બળતણ બચાવે.</li><li><strong>FD ફેન:</strong> ભઠ્ઠી માં તાજી હવા ધકેલે જેથી કોલસો સારી રીતે બળે.</li><li><strong>એર પ્રીહીટર:</strong> આવતી હવા ને ગરમ ધુમાડા થી ગરમ કરી બર્નિંગ સુધારે.</li><li><strong>કન્ડેન્સર:</strong> ટર્બાઇન માંથી નીકળેલ વરાળ ને પાણી બનાવે અને ટર્બાઇન ના છેડે ઓછું પ્રેશર રાખે.</li><li><strong>ટર્બાઇન:</strong> વરાળ ની શક્તિ ને ફરતા શાફ્ટ માં ફેરવી જનરેટર ચલાવે.</li><li><strong>કુલિંગ ટાવર:</strong> કન્ડેન્સર ના પાણી ને હવા થી ઠંડુ કરી વધારાની ગરમી બહાર કાઢે.</li></ol>""" + svg_wrap(AUX_SVG,"થર્મલ સહાયક — બોઇલર, ઇકોનોમાઇઝર, FD ફેન, એર પ્રીહીટર, કન્ડેન્સર, ટર્બાઇન, કુલિંગ ટાવર","Thermal auxiliaries"),
  },
 ]
},
{
 "title_en":"Q2 · Thermal cycles and hydro",
 "title_gu":"પ્ર.2 · થર્મલ સાઇકલ અને હાઇડ્રો",
 "cards":[
  {
   "q_en":"Q.2 (a) Draw & Explain Energy conversion Process in thermal power station. (3 marks)",
   "marks_en":"3 marks","marks_gu":"૦૩ ગુણ",
   "a_en":"""<p>Chemical energy in coal → heat in furnace → heat in steam → mechanical rotation of turbine → electrical output from generator. After turbine steam is condensed and pumped back, so cycle repeats. Losses occur in flue gas, condenser and auxiliaries.</p>""" + svg_wrap(ENERGY_THERM_SVG,"Energy chain — chemical → heat → mechanical → electrical","Energy conversion thermal"),
   "a_gu":"""<p>કોલસા માં રહેલ રાસાયણિક ઊર્જા → ભઠ્ઠી માં ગરમી → વરાળ માં ગરમી → ટર્બાઇન નું ફરવું → જનરેટર માંથી વીજળી. ટર્બાઇન પછી વરાળ પાણી બને અને પાછી બોઇલર માં જાય તેથી સાયકલ ફરે છે. ધુમાડો, કન્ડેન્સર અને સહાયક સાધનો માં થોડી ઊર્જા બગડે છે.</p>""" + svg_wrap(ENERGY_THERM_SVG,"ઊર્જા સાંકળ — રાસાયણિક → ગરમી → યાંત્રિક → વિદ્યુત","Energy conversion thermal"),
  },
  {
   "q_en":"Q.2 (b) Draw and explain feed water and steam cycle of thermal power station. (4 marks)",
   "marks_en":"4 marks","marks_gu":"૦૪ ગુણ",
   "a_en":"""<p><strong>Steam path:</strong> Boiler → superheater → turbine stages → condenser. <strong>Feed water path:</strong> Condenser → condensate pump → low pressure heater → deaerator → boiler feed pump → economizer → boiler. Heaters take bled steam from turbine to warm feed water.</p><p>This closed loop saves treated water and heat.</p>""" + svg_wrap(STEAM_CYCLE_SVG,"Feed water and steam cycle — boiler to turbine to condenser and back","Steam cycle"),
   "a_gu":"""<p><strong>વરાળ નો રસ્તો:</strong> બોઇલર → સુપરહીટર → ટર્બાઇન સ્ટેજ → કન્ડેન્સર. <strong>ફીડ વોટર નો રસ્તો:</strong> કન્ડેન્સર → કન્ડેન્સેટ પંપ → લો પ્રેશર હીટર → ડીએરેટર → બોઇલર ફીડ પંપ → ઇકોનોમાઇઝર → બોઇલર. હીટર ટર્બાઇન માંથી થોડી વરાળ લઈ ફીડ વોટર ગરમ કરે છે.</p><p>આ બંધ લૂપ થી શુદ્ધ પાણી અને ગરમી બંને બચે છે.</p>""" + svg_wrap(STEAM_CYCLE_SVG,"ફીડ વોટર અને વરાળ સાયકલ — બોઇલર થી ટર્બાઇન થી કન્ડેન્સર અને પાછું","Steam cycle"),
  },
  {
   "q_en":"Q.2 (c) Explain the function of surge-tank and pen-stock. Give the difference between catchment area and reservoir. (7 marks)",
   "marks_en":"7 marks","marks_gu":"૦૭ ગુણ",
   "a_en":"""<p><strong>Surge tank:</strong> Vertical shaft open to air connected to headrace. When turbine gates close suddenly, water hammer pressure rises and surge tank absorbs it by allowing water level to oscillate. Also supplies water when gates open quickly.</p><p><strong>Penstock:</strong> High pressure steel/concrete pipe from surge tank to turbine inlet. It carries water under full head with minimal loss.</p><table><tr><th>Catchment area</th><th>Reservoir</th></tr><tr><td>Total land where rain collects into river feeding site</td><td>Man-made or natural stored water behind dam within catchment</td></tr><tr><td>Bigger area decides inflow potential</td><td>Storage decides usable energy and regulation</td></tr></table>""" + svg_wrap(SURGE_SVG,"Surge tank absorbs hammer, penstock carries high pressure water to turbine","Surge tank penstock"),
   "a_gu":"""<p><strong>સર્જ ટેન્ક:</strong> હેડરેસ સાથે જોડેલ હવા ખુલ્લી ઊભી ટાંકી. ટર્બાઇન ના ગેટ ઝડપથી બંધ થાય ત્યારે પાણી નો ધક્કો વધે અને સર્જ ટેન્ક પાણી ની સપાટી ઊંચી કરી તે ધક્કો શોષી લે છે. ગેટ ઝડપથી ખુલે ત્યારે પાણી પણ આપે છે.</p><p><strong>પેનસ્ટોક:</strong> સર્જ ટેન્ક થી ટર્બાઇન સુધી નો હાઇ પ્રેશર સ્ટીલ કે કોંક્રિટ નો પાઇપ. આખા હેડ સાથે પાણી ઓછા લોસ સાથે પહોંચાડે છે.</p><table><tr><th>કેચમેન્ટ એરિયા</th><th>જળાશય</th></tr><tr><td>જ્યાં વરસાદ નું પાણી ભેગું થઈ નદી માં આવી સાઇટ પર પહોંચે તે આખો વિસ્તાર</td><td>ડેમ પાછળ સંગ્રહિત પાણી જે કેચમેન્ટ નો ભાગ છે</td></tr><tr><td>મોટો કેચમેન્ટ વધુ આવક ની શક્યતા આપે</td><td>સંગ્રહ ઊર્જા અને નિયંત્રણ નક્કી કરે</td></tr></table>""" + svg_wrap(SURGE_SVG,"સર્જ ટેન્ક ધક્કો શોષે, પેનસ્ટોક હાઇ પ્રેશર પાણી ટર્બાઇન સુધી લઈ જાય","Surge tank penstock"),
  },
  {
   "q_en":"Q.2 (a) OR Draw and explain energy conversion process in Hydro Power Plant. (3 marks)",
   "marks_en":"3 marks","marks_gu":"૦૩ ગુણ",
   "a_en":"""<p>Potential energy of stored water → kinetic energy in penstock → mechanical rotation of turbine → electrical from generator. Water returns to tailrace, not consumed. Head and flow decide power P = ρ·g·Q·H·η.</p>""",
   "a_gu":"""<p>સંગ્રહિત પાણી ની સ્થિતિ ઊર્જા → પેનસ્ટોક માં ગતિ ઊર્જા → ટર્બાઇન નું ફરવું → જનરેટર માંથી વીજળી. પાણી ટેઇલરેસ માં પાછું જાય છે, વપરાઈ જતું નથી. હેડ અને ફ્લો પાવર નક્કી કરે છે.</p>""",
  },
  {
   "q_en":"Q.2 (b) OR Explain fuel and ash cycle with diagram for thermal power station. (4 marks)",
   "marks_en":"4 marks","marks_gu":"૦૪ ગુણ",
   "a_en":"""<p><strong>Fuel cycle:</strong> Coal yard → conveyor → crusher → pulveriser → feeder → furnace. Air from FD fan via air preheater supports burning.</p><p><strong>Ash cycle:</strong> Bottom ash falls to water filled hopper, fly ash collected by ESP, both sent by slurry pumps to ash pond. Clean flue gas goes via chimney.</p>""",
   "a_gu":"""<p><strong>બળતણ ચક્ર:</strong> કોલસા યાર્ડ → કન્વેયર → ક્રશર → દળવાનું મશીન → ફીડર → ભઠ્ઠી. FD ફેન ની હવા એર પ્રીહીટર થઈ બર્નિંગ માં મદદ કરે છે.</p><p><strong>રાખ ચક્ર:</strong> તળિયા ની રાખ પાણી ભરેલ હોપર માં પડે, ઉડતી રાખ ESP માં પકડાય, બંને સ્લરી પંપ થી રાખ તળાવ માં જાય. સ્વચ્છ ધુમાડો ચીમની થી બહાર જાય છે.</p>""",
  },
  {
   "q_en":"Q.2 (c) OR Give the classification of Hydro Power Station. State the different schemes used in Hydro Power Station. (7 marks)",
   "marks_en":"7 marks","marks_gu":"૦૭ ગુણ",
   "a_en":"""<p><strong>Classification:</strong></p><ol><li><strong>By head:</strong> High above 100m, medium 30 to 100m, low below 30m. Pelton for high, Francis for medium, Kaplan for low.</li><li><strong>By storage:</strong> Run-of-river without pondage, run-of-river with pondage, reservoir storage, pumped storage.</li><li><strong>By duty:</strong> Base load, peak load.</li></ol><p><strong>Schemes:</strong> Dam toe powerhouse, headrace tunnel with penstock, diversion canal, pumped storage with reversible pump turbine.</p>""" + svg_wrap(HYDRO_CLASS_SVG,"Hydro types by head, storage and duty; schemes as dam toe, diversion, pumped","Hydro classification"),
   "a_gu":"""<p><strong>વર્ગીકરણ:</strong></p><ol><li><strong>હેડ પ્રમાણે:</strong> ઊંચું 100m થી વધુ, મધ્યમ 30 થી 100m, નીચું 30m થી ઓછું. ઊંચા માટે પેલ્ટન, મધ્યમ માટે ફ્રાન્સિસ, નીચા માટે કાપલાન.</li><li><strong>સંગ્રહ પ્રમાણે:</strong> તળાવ વગર નું નદી પર, તળાવ સાથે નું નદી પર, જળાશય વાળું, પંપ સ્ટોરેજ વાળું.</li><li><strong>કામ પ્રમાણે:</strong> બેઝ લોડ, પીક લોડ.</li></ol><p><strong>યોજનાઓ:</strong> ડેમ ને અડી ને પાવરહાઉસ, ટનલ અને પેનસ્ટોક વાળું, ડાઇવર્ઝન કેનાલ વાળું, રિવર્સિબલ પંપ ટર્બાઇન વાળું પંપ સ્ટોરેજ.</p>""" + svg_wrap(HYDRO_CLASS_SVG,"હાઇડ્રો પ્રકાર હેડ, સંગ્રહ અને કામ પ્રમાણે","Hydro classification"),
  },
 ]
},
{
 "title_en":"Q3 · Hydro, solar and nuclear",
 "title_gu":"પ્ર.3 · હાઇડ્રો, સોલર અને ન્યુક્લિયર",
 "cards":[
  {
   "q_en":"Q.3 (a) What are the points to be considered while selecting site for hydro power station? (3 marks)",
   "marks_en":"3 marks","marks_gu":"૦૩ ગુણ",
   "a_en":"""<ol><li><strong>Water & head:</strong> Good catchment rainfall, perennial flow, high head possible with dam site.</li><li><strong>Geology & access:</strong> Strong rock for dam and tunnels, not too far from load, road access for machines.</li><li><strong>Storage & environment:</strong> Space for reservoir without displacing many people, low silt, forest and wildlife clearance possible.</li></ol>""",
   "a_gu":"""<ol><li><strong>પાણી અને હેડ:</strong> સારો વરસાદ વાળો કેચમેન્ટ, આખું વર્ષ પાણી, ડેમ થી ઊંચો હેડ મળે.</li><li><strong>જમીન અને પહોંચ:</strong> ડેમ અને ટનલ માટે મજબૂત ખડક, લોડ થી બહુ દૂર નહીં, મશીન લાવવા રસ્તો.</li><li><strong>સંગ્રહ અને પર્યાવરણ:</strong> જળાશય માટે જગ્યા જ્યાં ઓછા લોકો ને ખસેડવા પડે, કાંપ ઓછો, જંગલ અને વન્યજીવ ની મંજૂરી મળી શકે.</li></ol>""",
  },
  {
   "q_en":"Q.3 (b) Define the following terms: (1) Solar Cell (2) Solar Module (3) Solar Panel (4) Solar Array. (4 marks)",
   "marks_en":"4 marks","marks_gu":"૦૪ ગુણ",
   "a_en":"""<ol><li><strong>Solar Cell:</strong> Basic semiconductor device that converts light directly to DC, about 0.5V.</li><li><strong>Solar Module:</strong> Many cells joined in series/parallel to get required voltage and current, with lamination.</li><li><strong>Solar Panel:</strong> Module fitted with glass, frame, junction box for installation.</li><li><strong>Solar Array:</strong> Group of panels connected to get desired power for plant.</li></ol>""" + svg_wrap(SOLAR_DEF_SVG,"Cell is single, module is cells joined, panel is framed module, array is many panels","Solar cell to array"),
   "a_gu":"""<ol><li><strong>સોલર સેલ:</strong> પ્રકાશ ને સીધો DC માં ફેરવતો નાનો સેમિકન્ડક્ટર ટુકડો, લગભગ 0.5V.</li><li><strong>સોલર મોડ્યુલ:</strong> ઘણા સેલ ને સીરીઝ પેરેલલ માં જોડી જરૂરી વોલ્ટેજ કરંટ મેળવવા, લેમિનેશન સાથે.</li><li><strong>સોલર પેનલ:</strong> મોડ્યુલ ને કાચ, ફ્રેમ, જંક્શન બોક્સ સાથે લગાવવા યોગ્ય બનાવેલું.</li><li><strong>સોલર એરે:</strong> ઘણી પેનલ ને જોડી પ્લાન્ટ માટે જોઈતો પાવર બનાવવો.</li></ol>""" + svg_wrap(SOLAR_DEF_SVG,"સેલ એકલો, મોડ્યુલ સેલ નું જોડાણ, પેનલ ફ્રેમ વાળું, એરે ઘણી પેનલ","Solar cell to array"),
  },
  {
   "q_en":"Q.3 (c) Draw and explain schematic diagram of Nuclear Power Station. Draw nuclear reactor diagram showing its major elements. (7 marks)",
   "marks_en":"7 marks","marks_gu":"૦૭ ગુણ",
   "a_en":"""<p><strong>Nuclear station flow:</strong> Reactor generates heat → steam generator makes steam → turbine → generator → condenser → feed pump back. Pressuriser keeps pressure in PWR, BWR boils directly.</p><p><strong>Reactor elements:</strong> Fuel rods with U pellets inside zirconium tubes, moderator to slow neutrons, control rods to absorb neutrons, coolant to carry heat, reflector and thick concrete shielding for safety. Pressure vessel encloses core.</p>""" + svg_wrap(NUCLEAR_SVG,"Nuclear plant — reactor heat → steam → turbine → generator; reactor shows fuel, moderator, control rods, coolant, shielding","Nuclear station and reactor"),
   "a_gu":"""<p><strong>ન્યુક્લિયર સ્ટેશન નો પ્રવાહ:</strong> રિએક્ટર ગરમી બનાવે → સ્ટીમ જનરેટર વરાળ બનાવે → ટર્બાઇન → જનરેટર → કન્ડેન્સર → ફીડ પંપ પાછું. PWR માં પ્રેશરાઇઝર પ્રેશર રાખે, BWR સીધું ઉકાળે છે.</p><p><strong>રિએક્ટર ના મુખ્ય ભાગો:</strong> યુરેનિયમ પેલેટ વાળા ફ્યુઅલ રોડ ઝિર્કોનિયમ ટ્યુબ માં, ન્યુટ્રોન ધીમા કરવા મોડરેટર, કંટ્રોલ કરવા કંટ્રોલ રોડ, ગરમી લઈ જવા કુલન્ટ, અને સલામતી માટે જાડી કોંક્રિટ શિલ્ડિંગ. પ્રેશર વેસલ કોર ને ઢાંકે છે.</p>""" + svg_wrap(NUCLEAR_SVG,"ન્યુક્લિયર પ્લાન્ટ — રિએક્ટર ગરમી → વરાળ → ટર્બાઇન → જનરેટર","Nuclear station and reactor"),
  },
  {
   "q_en":"Q.3 (a) OR Explain site selection of Nuclear Power Station. (3 marks)",
   "marks_en":"3 marks","marks_gu":"૦૩ ગુણ",
   "a_en":"""<ol><li>Near sea/river for huge cooling water, stable rock for heavy reactor building, away from dense city and earthquake zone.</li><li>Good road/rail for heavy equipment and waste transport, not too far from grid.</li><li>Environment clearance, low population evacuation zone, no flood risk.</li></ol>""",
   "a_gu":"""<ol><li>દરિયા કે નદી નજીક ઠંડા પાણી માટે, ભારે રિએક્ટર બિલ્ડિંગ માટે મજબૂત ખડક, ગીચ શહેર અને ધરતીકંપ ઝોન થી દૂર.</li><li>ભારે સાધન અને કચરો લઈ જવા સારો રસ્તો રેલવે, ગ્રીડ થી બહુ દૂર નહીં.</li><li>પર્યાવરણ મંજૂરી, ઓછી વસ્તી વાળો ખાલી વિસ્તાર, પૂર નો ભય નહીં.</li></ol>""",
  },
  {
   "q_en":"Q.3 (b) OR Draw and explain the characteristics of solar cell. (4 marks)",
   "marks_en":"4 marks","marks_gu":"૦૪ ગુણ",
   "a_en":"""<p><strong>I-V curve:</strong> At zero voltage current is short circuit current Isc, at zero current voltage is open circuit Voc. Max power point Vmpp, Impp gives Pmax. Fill factor = Pmax / Voc·Isc. Efficiency = Pmax / incident light power.</p><p>More light raises current, higher temperature slightly drops voltage.</p>""",
   "a_gu":"""<p><strong>I-V કર્વ:</strong> ઝીરો વોલ્ટેજ પર કરંટ શોર્ટ સર્કિટ કરંટ કહેવાય, ઝીરો કરંટ પર વોલ્ટેજ ઓપન સર્કિટ વોલ્ટેજ કહેવાય. વચ્ચે મહત્તમ પાવર પોઇન્ટ હોય જ્યાં Vmpp અને Impp થી Pmax મળે. ફિલ ફેક્ટર = Pmax ભાગ્યા Voc ગુણ્યા Isc. કાર્યક્ષમતા = Pmax ભાગ્યા આવતો પ્રકાશ પાવર.</p><p>વધુ પ્રકાશ થી કરંટ વધે, વધુ ગરમી થી વોલ્ટેજ થોડો ઘટે.</p>""",
  },
  {
   "q_en":"Q.3 (c) OR Explain Rooftop Solar PV Power System: Grid connected and standalone with diagram. (7 marks)",
   "marks_en":"7 marks","marks_gu":"૦૭ ગુણ",
   "a_en":"""<p><strong>Standalone:</strong> PV → charge controller → battery → inverter → load. Works off grid, battery supplies night. Controller prevents overcharge.</p><p><strong>Grid connected:</strong> PV → inverter → net meter → grid. No battery needed, excess power goes to grid and meter runs backward. Needs grid present to operate.</p><p>Hybrid combines both for backup.</p>""" + svg_wrap(ROOFTOP_SVG,"Rooftop PV — standalone with battery vs grid connected with net meter","Rooftop PV"),
   "a_gu":"""<p><strong>સ્ટેન્ડઅલોન:</strong> PV → ચાર્જ કંટ્રોલર → બેટરી → ઇન્વર્ટર → લોડ. ગ્રીડ વગર ચાલે, રાત્રે બેટરી આપે. કંટ્રોલર ઓવરચાર્જ અટકાવે.</p><p><strong>ગ્રીડ કનેક્ટેડ:</strong> PV → ઇન્વર્ટર → નેટ મીટર → ગ્રીડ. બેટરી જરૂર નથી, વધારાની વીજળી ગ્રીડ માં જાય અને મીટર પાછું ફરે. ગ્રીડ હાજર હોય ત્યારે જ ચાલે.</p><p>હાઇબ્રિડ બંને નું મિશ્રણ છે જેથી બેકઅપ મળે.</p>""" + svg_wrap(ROOFTOP_SVG,"રૂફટોપ PV — બેટરી વાળું સ્ટેન્ડઅલોન વિરુદ્ધ નેટ મીટર વાળું ગ્રીડ કનેક્ટેડ","Rooftop PV"),
  },
 ]
},
{
 "title_en":"Q4 · Wind, captive and diesel",
 "title_gu":"પ્ર.4 · વિન્ડ, કેપ્ટિવ અને ડીઝલ",
 "cards":[
  {
   "q_en":"Q.4 (a) Draw and explain energy conversion process in wind power plant. (3 marks)",
   "marks_en":"3 marks","marks_gu":"૦૩ ગુણ",
   "a_en":"""<p>Wind kinetic energy → rotor blades capture → gearbox increases speed → generator makes AC → transformer to grid. Power depends on air density, swept area and wind cube, limited by Betz to 59%.</p>""" + svg_wrap(WIND_SVG,"Wind energy — wind → rotor → generator → grid, power 0.5·ρ·A·v³·Cp","Wind conversion"),
   "a_gu":"""<p>હવા ની ગતિ ઊર્જા → બ્લેડ પકડે → ગિયરબોક્સ ઝડપ વધારે → જનરેટર AC બનાવે → ટ્રાન્સફોર્મર ગ્રીડ માં મોકલે. પાવર હવા ની ઘનતા, સ્વેપ્ટ એરિયા અને હવા ની ઝડપ ના ઘન પર આધાર રાખે, બેટ્ઝ મર્યાદા 59%.</p>""" + svg_wrap(WIND_SVG,"વિન્ડ ઊર્જા — હવા → રોટર → જનરેટર → ગ્રીડ","Wind conversion"),
  },
  {
   "q_en":"Q.4 (b) Compare between HAWT and VAWT. (4 marks)",
   "marks_en":"4 marks","marks_gu":"૦૪ ગુણ",
   "a_en":"""<table><tr><th>Point</th><th>HAWT</th><th>VAWT</th></tr><tr><td>Axis</td><td>Horizontal, faces wind</td><td>Vertical, works from any direction</td></tr><tr><td>Efficiency</td><td>High, 40 to 45%</td><td>Lower, 20 to 30%</td></tr><tr><td>Yaw/starter</td><td>Needs yaw, needs motor start</td><td>No yaw, self start Savonius type</td></tr><tr><td>Use</td><td>Large farms</td><td>Small urban rooftop</td></tr></table>""" + svg_wrap(HAWT_VAWT_SVG,"HAWT horizontal high efficiency needs yaw, VAWT vertical omnidirectional lower Cp","HAWT vs VAWT"),
   "a_gu":"""<table><tr><th>મુદ્દો</th><th>HAWT</th><th>VAWT</th></tr><tr><td>ધરી</td><td>આડી, હવા સામે મોઢું</td><td>ઊભી, કોઈપણ દિશા થી ચાલે</td></tr><tr><td>કાર્યક્ષમતા</td><td>ઊંચી, 40 થી 45%</td><td>ઓછી, 20 થી 30%</td></tr><tr><td>ફરવું અને સ્ટાર્ટ</td><td>ફરવું પડે, મોટર થી સ્ટાર્ટ</td><td>ફરવું ન પડે, સાવોનિયસ જાતે ચાલુ થાય</td></tr><tr><td>ઉપયોગ</td><td>મોટા ફાર્મ</td><td>નાના શહેરી છત પર</td></tr></table>""" + svg_wrap(HAWT_VAWT_SVG,"HAWT આડો વધુ કાર્યક્ષમ, VAWT ઊભો ઓછો","HAWT vs VAWT"),
  },
  {
   "q_en":"Q.4 (c) State advantages, disadvantages and limitations of solar power plant and wind power plant. (7 marks)",
   "marks_en":"7 marks","marks_gu":"૦૭ ગુણ",
   "a_en":"""<p><strong>Solar advantages:</strong> Free sun, no fuel, no pollution during operation, modular, low tilt and rooftop possible.</p><p><strong>Solar disadvantages:</strong> Only day, needs sun, low efficiency 15 to 20%, high first cost, cleaning needed, needs storage for night.</p><p><strong>Wind advantages:</strong> Free wind, good for farms, quick install.</p><p><strong>Wind disadvantages:</strong> Needs windy site, noisy, bird risk, variable output, needs forecasting.</p><p><strong>Common limitation:</strong> Intermittent, needs grid support or storage.</p>""",
   "a_gu":"""<p><strong>સોલર ના ફાયદા:</strong> સૂરજ મફત, બળતણ નહીં, ચાલતી વખતે પ્રદૂષણ નહીં, નાના મોટા કરી શકાય, છત પર લગાવી શકાય.</p><p><strong>સોલર ના ગેરફાયદા:</strong> દિવસે જ ચાલે, તડકો જોઈએ, કાર્યક્ષમતા 15 થી 20% ઓછી, શરૂઆત નો ખર્ચ વધુ, સફાઈ કરવી પડે, રાત માટે સ્ટોરેજ જોઈએ.</p><p><strong>વિન્ડ ના ફાયદા:</strong> હવા મફત, ફાર્મ માટે સારું, ઝડપથી લાગે.</p><p><strong>વિન્ડ ના ગેરફાયદા:</strong> પવન વાળી જગ્યા જોઈએ, અવાજ, પક્ષી ને નુકસાન, ઉત્પાદન બદલાતું રહે, આગાહી કરવી પડે.</p><p><strong>સામાન્ય મર્યાદા:</strong> બંને હવામાન પર આધાર રાખે તેથી ગ્રીડ ની મદદ કે સ્ટોરેજ જોઈએ.</p>""",
  },
  {
   "q_en":"Q.4 (a) OR Explain Captive Power Plant. (3 marks)",
   "marks_en":"3 marks","marks_gu":"૦૩ ગુણ",
   "a_en":"""<p>Captive plant is owned by factory to meet its own demand, like sugar mill using bagasse, steel plant using waste heat. It may export surplus to grid. Gives reliability and cost control, but needs fuel and maintenance by owner.</p>""",
   "a_gu":"""<p>કેપ્ટિવ પ્લાન્ટ એટલે ફેક્ટરી પોતાની વીજળી માટે પોતાનો પ્લાન્ટ, જેમ ખાંડ મિલ બગાસ થી, સ્ટીલ પ્લાન્ટ ગરમી ના બગાડ થી બનાવે. વધારાની વીજળી ગ્રીડ ને આપી શકે. પોતાનો ભરોસો અને ખર્ચ કાબૂ રહે, પણ બળતણ અને જાળવણી માલિકે કરવાની.</p>""",
  },
  {
   "q_en":"Q.4 (b) OR Define the following terms: (1) Wind Turbine Efficiency (2) Swept Area (3) Cut in Wind Speed (4) Cut out Wind Speed (4 marks)",
   "marks_en":"4 marks","marks_gu":"૦૪ ગુણ",
   "a_en":"""<ol><li><strong>Turbine Efficiency Cp:</strong> Ratio of power captured to wind power available.</li><li><strong>Swept Area A:</strong> Circle traced by blade tips, π·D²/4.</li><li><strong>Cut in speed:</strong> Minimum wind to start generating.</li><li><strong>Cut out speed:</strong> High wind where turbine stops to stay safe.</li></ol>""",
   "a_gu":"""<ol><li><strong>ટર્બાઇન કાર્યક્ષમતા:</strong> હવા ના પાવર માંથી કેટલો પકડાયો તે ગુણોત્તર.</li><li><strong>સ્વેપ્ટ એરિયા:</strong> બ્લેડ ની ટોચ ફરે ત્યારે બનતું વર્તુળ, π·D²/4.</li><li><strong>કટ ઇન સ્પીડ:</strong> જેટલી ઓછામાં ઓછી હવા થી વીજળી બનવા માંડે.</li><li><strong>કટ આઉટ સ્પીડ:</strong> જેટલી વધુ હવા થી મશીન બંધ કરી દેવાય સલામતી માટે.</li></ol>""",
  },
  {
   "q_en":"Q.4 (c) OR Draw line diagram of diesel power station, explain each block. Write advantages and disadvantages of diesel power station. (7 marks)",
   "marks_en":"7 marks","marks_gu":"૦૭ ગુણ",
   "a_en":"""<p><strong>Blocks:</strong> Fuel storage tank → fuel injection → diesel engine → alternator → cooling via radiator → exhaust silencer → air filter. Engine governor controls fuel as load changes.</p><p><strong>Advantages:</strong> Quick start, good for standby and remote, small area, less water.</p><p><strong>Disadvantages:</strong> Diesel costly, noisy, pollution, small size only, fuel transport needed.</p>""" + svg_wrap(DIESEL_SVG,"Diesel station — fuel → engine → alternator → cooling → exhaust","Diesel station"),
   "a_gu":"""<p><strong>બ્લોક:</strong> બળતણ ટાંકી → ઇંજેક્શન → ડીઝલ એન્જિન → અલ્ટરનેટર → રેડિયેટર થી ઠંડુ → સાઇલેન્સર થી ધુમાડો → એર ફિલ્ટર. લોડ બદલાય ત્યારે ગવર્નર બળતણ કાબૂ કરે.</p><p><strong>ફાયદા:</strong> ઝડપથી ચાલુ થાય, સ્ટેન્ડબાય અને દૂર ના વિસ્તાર માટે સારું, નાની જગ્યા, ઓછું પાણી.</p><p><strong>ગેરફાયદા:</strong> ડીઝલ મોંઘું, અવાજ, પ્રદૂષણ, નાના કદ જ, બળતણ લાવવું પડે.</p>""" + svg_wrap(DIESEL_SVG,"ડીઝલ સ્ટેશન — બળતણ → એન્જિન → અલ્ટરનેટર → કુલિંગ → એક્ઝોસ્ટ","Diesel station"),
  },
 ]
},
{
 "title_en":"Q5 · Load, bio power and calculations",
 "title_gu":"પ્ર.5 · લોડ, બાયો પાવર અને ગણતરી",
 "cards":[
  {
   "q_en":"Q.5 (a) State the importance of Load Curve and which are the information available from the load curve ? (3 marks)",
   "marks_en":"3 marks","marks_gu":"૦૩ ગુણ",
   "a_en":"""<p><strong>Importance:</strong> Shows how demand changes over 24h. Helps plan generation, decide peak and base plants, schedule maintenance when load low.</p><p><strong>Information:</strong> Max demand, average load, energy per day as area, load factor, when peak occurs.</p>""" + svg_wrap(LOAD_CURVE_SVG,"Load curve gives peak, average, energy and timing","Load curve"),
   "a_gu":"""<p><strong>મહત્વ:</strong> 24 કલાક માં માંગ કેવી બદલાય તે બતાવે. ઉત્પાદન પ્લાન, પીક અને બેઝ પ્લાન્ટ પસંદ, રિપેર માટે ઓછા લોડ નો સમય નક્કી કરવામાં મદદ કરે.</p><p><strong>મળતી માહિતી:</strong> મહત્તમ માંગ, સરેરાશ લોડ, દિવસ ની ઊર્જા જે એરિયા માંથી, લોડ ફેક્ટર, પીક ક્યારે આવે.</p>""" + svg_wrap(LOAD_CURVE_SVG,"લોડ કર્વ થી પીક, સરેરાશ, ઊર્જા અને સમય ખબર પડે","Load curve"),
  },
  {
   "q_en":"Q.5 (b) What is Bio-Chemical conversion process? Explain Layout of Bio-Chemical based power plant with neat diagram. (4 marks)",
   "marks_en":"4 marks","marks_gu":"૦૪ ગુણ",
   "a_en":"""<p>Bio-chemical uses microbes to break bio waste without oxygen and make biogas rich in methane.</p><p><strong>Layout:</strong> Waste collection → shredder → digester kept warm → biogas holder → gas cleaning → engine generator. Digested slurry is good manure.</p>""" + svg_wrap(BIO_SVG,"Bio-chemical — waste → digester → biogas → engine generator, slurry as manure","Bio chemical plant"),
   "a_gu":"""<p>બાયો કેમિકલ માં જીવાણુ કચરા ને હવા વગર તોડી મિથેન વાળો બાયોગેસ બનાવે છે.</p><p><strong>લેઆઉટ:</strong> કચરો ભેગો → કટર → ગરમ ડાયજેસ્ટર → બાયોગેસ ટાંકી → ગેસ સાફ → એન્જિન જનરેટર. બચેલ સ્લરી સારું ખાતર બને.</p>""" + svg_wrap(BIO_SVG,"બાયો કેમિકલ — કચરો → ડાયજેસ્ટર → બાયોગેસ → એન્જિન જનરેટર","Bio chemical plant"),
  },
  {
   "q_en":"Q.5 (c) Define the following terms: (1) Average Demand (2) Maximum Demand (3) Load Factor (4) Connected Load (5) Demand Factor (6) Diversity Factor (7) Plant use Factor. (7 marks)",
   "marks_en":"7 marks","marks_gu":"૦૭ ગુણ",
   "a_en":"""<table><tr><th>Term</th><th>Meaning</th></tr><tr><td>Average Demand</td><td>Energy per period divided by time</td></tr><tr><td>Maximum Demand</td><td>Highest load during period</td></tr><tr><td>Load Factor</td><td>Average / Maximum, shows utilization</td></tr><tr><td>Connected Load</td><td>Sum of all equipment ratings connected</td></tr><tr><td>Demand Factor</td><td>Maximum Demand / Connected Load, always less than 1</td></tr><tr><td>Diversity Factor</td><td>Sum of individual max demands / Group max, always more than 1</td></tr><tr><td>Plant Use Factor</td><td>Energy generated / Plant capacity × time, shows plant use</td></tr></table>""",
   "a_gu":"""<table><tr><th>શબ્દ</th><th>અર્થ</th></tr><tr><td>સરેરાશ માંગ</td><td>સમય ના ગાળા માં ઊર્જા ભાગ્યા સમય</td></tr><tr><td>મહત્તમ માંગ</td><td>ગાળા માં સૌથી વધુ લોડ</td></tr><tr><td>લોડ ફેક્ટર</td><td>સરેરાશ ભાગ્યા મહત્તમ, ઉપયોગ કેટલો તે બતાવે</td></tr><tr><td>કનેક્ટેડ લોડ</td><td>જોડેલ બધા સાધન ના રેટિંગ નો સરવાળો</td></tr><tr><td>ડિમાન્ડ ફેક્ટર</td><td>મહત્તમ માંગ ભાગ્યા કનેક્ટેડ લોડ, હંમેશા એક થી ઓછો</td></tr><tr><td>ડાઇવર્સિટી ફેક્ટર</td><td>દરેક ની મહત્તમ નો સરવાળો ભાગ્યા જૂથ ની મહત્તમ, હંમેશા એક થી વધુ</td></tr><tr><td>પ્લાન્ટ યુઝ ફેક્ટર</td><td>બનેલી ઊર્જા ભાગ્યા પ્લાન્ટ ક્ષમતા ગુણ્યા સમય, પ્લાન્ટ કેટલો વપરાયો તે</td></tr></table>""",
  },
  {
   "q_en":"Q.5 (a) OR Compare base load and peak load power station. (3 marks)",
   "marks_en":"3 marks","marks_gu":"૦૩ ગુણ",
   "a_en":"""<table><tr><th>Base load station</th><th>Peak load station</th></tr><tr><td>Runs most of day at steady output, e.g., large thermal, nuclear, run-of-river hydro</td><td>Runs only at peak hours, e.g., gas turbine, pumped hydro, diesel</td></tr><tr><td>Low running cost, slow start</td><td>Higher running cost but quick start</td></tr></table>""",
   "a_gu":"""<table><tr><th>બેઝ લોડ સ્ટેશન</th><th>પીક લોડ સ્ટેશન</th></tr><tr><td>દિવસ નો મોટો ભાગ સ્થિર ચાલે, જેમ મોટું થર્મલ, ન્યુક્લિયર, નદી નું હાઇડ્રો</td><td>માત્ર પીક કલાકો માં ચાલે, જેમ ગેસ ટર્બાઇન, પંપ હાઇડ્રો, ડીઝલ</td></tr><tr><td>ચાલવાનો ખર્ચ ઓછો, ચાલુ થતા વાર લાગે</td><td>ચાલવાનો ખર્ચ વધુ પણ ઝડપથી ચાલુ થાય</td></tr></table>""",
  },
  {
   "q_en":"Q.5 (b) OR Explain working principle of fuel cell for electricity generation. State types of fuel cells. (4 marks)",
   "marks_en":"4 marks","marks_gu":"૦૪ ગુણ",
   "a_en":"""<p>Fuel cell makes DC directly by chemical reaction, not burning. At anode hydrogen splits to H+ and electrons. H+ passes through electrolyte, electrons go via load. At cathode oxygen plus H+ plus electrons make water. No moving parts, low pollution.</p><p><strong>Types:</strong> PEMFC, PAFC, MCFC, SOFC, AFC.</p>""" + svg_wrap(FUELCELL_SVG,"Fuel cell — anode H2 splits, cathode makes water, electrons work via load","Fuel cell"),
   "a_gu":"""<p>ફ્યુઅલ સેલ બાળ્યા વગર રાસાયણિક પ્રક્રિયા થી સીધો DC બનાવે. એનોડ પર હાઇડ્રોજન તૂટી H+ અને ઇલેક્ટ્રોન બને. H+ ઇલેક્ટ્રોલાઇટ માંથી જાય, ઇલેક્ટ્રોન લોડ માંથી જાય. કેથોડ પર ઓક્સિજન, H+ અને ઇલેક્ટ્રોન થી પાણી બને. ફરતા ભાગ નહીં, પ્રદૂષણ ઓછું.</p><p><strong>પ્રકાર:</strong> PEMFC, PAFC, MCFC, SOFC, AFC.</p>""" + svg_wrap(FUELCELL_SVG,"ફ્યુઅલ સેલ — એનોડ H2 તૂટે, કેથોડ પાણી બનાવે, ઇલેક્ટ્રોન કામ કરે","Fuel cell"),
  },
  {
   "q_en":"Q.5 (c) OR A generating station has a connected load of 43 MW and a maximum demand of 20 MW; the units generated being 61.5 x 10^6 per annum. Calculate (i) the demand factor and (ii) load factor. (7 marks)",
   "marks_en":"7 marks","marks_gu":"૦૭ ગુણ",
   "a_en":"""<p><strong>Given:</strong> Connected load 43 MW, Max demand 20 MW, Units per year 61.5 ×10^6 kWh.</p><div class="eq">Demand factor = <span class="frac"><span class="num">Max demand</span><span class="den">Connected load</span></span> = <span class="frac"><span class="num">20</span><span class="den">43</span></span> = <strong>0.465</strong></div><div class="eq">Average demand = <span class="frac"><span class="num">Units per year</span><span class="den">8760 h</span></span> = <span class="frac"><span class="num">61.5×10<sup>6</sup></span><span class="den">8760</span></span> = <strong>7020.5 kW ≈7.02 MW</strong></div><div class="eq">Load factor = <span class="frac"><span class="num">Average</span><span class="den">Max</span></span> ×100 = <span class="frac"><span class="num">7.02</span><span class="den">20</span></span> ×100 = <strong>35.1%</strong></div><p>Low load factor means peak high compared to average, capacity underused part of year.</p>""",
   "a_gu":"""<p><strong>આપેલ:</strong> કનેક્ટેડ લોડ 43 MW, મહત્તમ માંગ 20 MW, વર્ષ ની ઊર્જા 61.5 ×10^6 kWh.</p><div class="eq">ડિમાન્ડ ફેક્ટર = <span class="frac"><span class="num">મહત્તમ માંગ</span><span class="den">કનેક્ટેડ લોડ</span></span> = <span class="frac"><span class="num">20</span><span class="den">43</span></span> = <strong>0.465</strong></div><div class="eq">સરેરાશ માંગ = <span class="frac"><span class="num">વર્ષ ની ઊર્જા</span><span class="den">8760 કલાક</span></span> = <span class="frac"><span class="num">61.5×10<sup>6</sup></span><span class="den">8760</span></span> = <strong>7020.5 kW ≈7.02 MW</strong></div><div class="eq">લોડ ફેક્ટર = <span class="frac"><span class="num">સરેરાશ</span><span class="den">મહત્તમ</span></span> ×100 = <span class="frac"><span class="num">7.02</span><span class="den">20</span></span> ×100 = <strong>35.1%</strong></div><p>ઓછો લોડ ફેક્ટર એટલે પીક સરેરાશ કરતા ઘણો વધુ, વર્ષ ના ભાગ માં ક્ષમતા ઓછી વપરાય.</p>""",
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
    page=f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>DI03009021 · Summer 2026 solved paper</title><style>{CSS}</style></head><body><main class="page"><header class="hero"><div class="eyebrow">Solved question paper · English questions · Friendly Gujarati answers</div><div class="lang-switch" aria-label="Choose language"><button type="button" data-lang="en" aria-pressed="true">English</button><button type="button" data-lang="gu" aria-pressed="false">ગુજરાતી</button></div><h1>Electrical Power Generation</h1><div class="meta">GTU Diploma · Electrical Engineering · Semester 3 · Summer 2026 · DI03009021 · 22 May 2026 · 70 marks · 02:30 PM TO 05:00 PM</div></header>{''.join(sections_html)}<div class="footer">Solved paper for study. Verify site data from official standards before field use.</div></main><script>document.querySelectorAll('.lang-switch button').forEach(b=>b.addEventListener('click',()=>{{document.documentElement.lang=b.dataset.lang;document.querySelectorAll('.lang-switch button').forEach(x=>x.setAttribute('aria-pressed',x===b?'true':'false'));}}));</script></body></html>'''
    return page
def main():
    page=build_page()
    out_papers=ROOT/"papers-upload/papers/DI03009021/summer-2026.html"
    out_ws=ROOT/"preview/workshop/DI03009021_summer2026_bilingual.html"
    out_papers.parent.mkdir(parents=True,exist_ok=True)
    out_ws.parent.mkdir(parents=True,exist_ok=True)
    out_papers.write_text(page,encoding="utf-8")
    out_ws.write_text(page,encoding="utf-8")
    d=page.count('<details'); s=page.count('<section'); ce=page.count('class="en"'); cg=page.count('class="gu"')
    print(f"Bilingual: {out_papers} ({len(page)} chars)")
    print(f"details={d}, sections={s}, en={ce}, gu={cg}")
    print("PASS" if d==28 and s==5 and ce>=28 and cg>=28 else "FAIL")
    figs=page.count('<figure>')
    fracs=page.count('class="frac"')
    print(f"figs={figs} fracs={fracs}")

if __name__=="__main__":
    main()
