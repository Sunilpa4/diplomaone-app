# -*- coding: utf-8 -*-
"""Render one standalone bilingual preview HTML for the whole DI04005071 subject (Units 1-5)."""
import json, html
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SUBJ = ROOT / "content/chemical/sem4/DI04005071"
subject = json.loads((SUBJ / "subject.json").read_text(encoding="utf-8"))
units = [json.loads((SUBJ / f"unit{n}.json").read_text(encoding="utf-8")) for n in (1, 2, 3, 4, 5)]
svgs = {p.stem: p.read_text(encoding="utf-8") for p in (SUBJ / "diagrams").glob("*.svg")}

CSS = """*{box-sizing:border-box}body{margin:0;background:#f5f3fa;color:#272134;font:16px/1.7 system-ui,-apple-system,"Noto Sans Gujarati",Arial,sans-serif}
.controls{position:sticky;top:0;z-index:5;background:#fff;border-bottom:1px solid #e4dceb;padding:12px max(14px,calc((100vw - 1100px)/2));display:flex;gap:12px;align-items:center}
button{font:inherit;border:1px solid #d8c8e6;border-radius:9px;padding:8px 12px;background:white;color:#62309b;cursor:pointer}
.app{max-width:1100px;margin:auto;padding:16px}.bar{background:linear-gradient(110deg,#6824aa,#8d43cb);color:#fff;padding:22px;border-radius:14px 14px 0 0}
.bar strong{display:block;font-size:23px}.bar small{display:block;opacity:.9}
.units{display:flex;gap:6px;flex-wrap:wrap;margin:0 0 6px}.units button.active{background:#7932b8;color:white}
.tabs{display:flex;gap:2px;flex-wrap:wrap;background:#ece1f6;padding:6px;border-radius:0 0 12px 12px;margin-bottom:18px}
.tabs button{flex:1;border:0;background:transparent;white-space:nowrap}.tabs button.active{background:#7932b8;color:white}
.intro{border-left:4px solid #9255c3;background:#eee7f6;padding:15px 19px;margin:18px 0}
.section{background:#7a36b4;color:#fff;border-radius:9px;padding:12px 16px;margin:24px 0 12px;font-weight:700}
.card{background:#fff;border:1px solid #e6deed;border-radius:10px;margin:10px 0;box-shadow:0 2px 5px #30134406}
.card>summary{cursor:pointer;padding:17px 20px;font-weight:650}.body{padding:4px 22px 20px;overflow-wrap:anywhere}
.body h4{color:#6d2ca4;margin:20px 0 8px}.body svg{width:100%;max-width:360px;height:auto;display:block;margin:18px auto;border:1px solid #eee;border-radius:8px}
table{width:100%;border-collapse:collapse;margin-top:12px;font-size:14px}th,td{border:1px solid #dfd2e9;padding:9px;text-align:left}th{background:#f1e8f8}
.eq{display:block;font-family:ui-monospace,Menlo,Consolas,monospace;background:#f7f2fc;border:1px solid #e6dcf5;border-radius:8px;padding:10px 14px;margin:10px 0;overflow-x:auto;white-space:nowrap}
.eq.boxed{border:2px solid #7B2CD9;background:#fff;font-weight:700;color:#4a148c}
.pill{display:inline-block;font-size:13px;color:#7330ab;background:#f1e8f8;border-radius:999px;padding:2px 10px;margin-left:8px}
.footer{font-size:13px;color:#74687e;padding:25px 4px}
body[data-lang="en"] .lang-gu{display:none!important}body[data-lang="gu"] .lang-en{display:none!important}
@media(max-width:600px){.app{padding:10px}.body{padding:0 14px 16px}}"""

def L(d):
    if isinstance(d, dict):
        return f'<div class="lang-en">{d.get("en","")}</div><div class="lang-gu">{d.get("gu","")}</div>'
    return str(d or "")

def card(summary_en, summary_gu, body_en, body_gu, open_first=False):
    o = " open" if open_first else ""
    return (f'<details class="card"{o}><summary><span class="lang-en">{html.escape(summary_en)}</span>'
            f'<span class="lang-gu">{html.escape(summary_gu)}</span></summary>'
            f'<div class="body"><div class="lang-en">{body_en}</div><div class="lang-gu">{body_gu}</div></div></details>')

TABS = [("notes", "Notes"), ("diagrams", "Diagrams"), ("numericals", "Numericals"),
        ("syntax", "Formulae"), ("viva", "Viva"), ("exam", "Exam")]

def unit_block(unit):
    n = unit["unit"]
    out = [f'<div class="unitblock" data-unit="{n}"' + (' hidden' if n != 1 else '') + '>']
    out.append(f'<div class="bar"><strong><span class="lang-en">Unit {n}: {html.escape(unit["title"]["en"])}</span>'
               f'<span class="lang-gu">Unit {n}: {html.escape(unit["title"]["gu"])}</span></strong>'
               f'<small>Petroleum Refining and Petroleum Technology • DI04005071 • Chemical Semester 4 • '
               f'{unit["hours"]}h / {unit["weightage"]}% • GTU 2025–26</small></div>')
    out.append('<nav class="tabs">' + "".join(
        f'<button data-tab="{k}" class="{"active" if i == 0 else ""}">{v}</button>' for i, (k, v) in enumerate(TABS)) + '</nav>')
    out.append(f'<div class="intro">{L(unit["intro_text"])}</div>')

    out.append('<section class="panel" data-panel="notes">')
    first = True
    for sec in unit["notes"]:
        out.append(f'<div class="section"><span class="lang-en">{html.escape(sec["title"]["en"])}</span><span class="lang-gu">{html.escape(sec["title"]["gu"])}</span></div>')
        for it in sec["items"]:
            h = it.get("h") or {}
            body_en, body_gu = it["body"]["en"], it["body"]["gu"]
            dg = it.get("diagram")
            if dg and dg in svgs:
                cap = next((d["title"]["en"] for d in unit["diagrams"] if d["id"] == dg), dg)
                ins = f'<div class="diagram-wrap">{svgs[dg]}<p class="pill">📐 {html.escape(cap)}</p></div>'
                body_en += ins; body_gu += ins
            if it.get("examples"):
                ex = f'<p class="pill">EX: Solved numerical {", ".join(it["examples"])}</p>'
                body_en += ex; body_gu += ex
            out.append(card(h.get("en", ""), h.get("gu", ""), body_en, body_gu, first)); first = False
    out.append('</section>')

    out.append('<section class="panel" data-panel="diagrams" hidden>')
    for d in unit["diagrams"]:
        out.append(card(d["title"]["en"], d["title"]["gu"], svgs.get(d["id"], ""), svgs.get(d["id"], "")))
    out.append('</section>')

    out.append('<section class="panel" data-panel="numericals" hidden>')
    for nm in unit["numericals"]:
        out.append(card(nm["q"]["en"], nm["q"]["gu"], nm["a"]["en"], nm["a"]["gu"]))
    out.append('</section>')

    out.append('<section class="panel" data-panel="syntax" hidden>')
    for g in unit["syntax"]:
        out.append(f'<div class="section"><span class="lang-en">{html.escape(g["title"]["en"])}</span><span class="lang-gu">{html.escape(g["title"]["gu"])}</span></div>')
        for it in g["items"]:
            out.append(card(it["name"]["en"], it["name"]["gu"],
                            f'<div class="eq">{html.escape(it["f"])}</div><p>{it["terms"]["en"]}</p>',
                            f'<div class="eq">{html.escape(it["f"])}</div><p>{it["terms"]["gu"]}</p>'))
    out.append('</section>')

    out.append('<section class="panel" data-panel="viva" hidden>')
    for g in unit["viva"]:
        out.append(f'<div class="section"><span class="lang-en">{html.escape(g["title"]["en"])}</span><span class="lang-gu">{html.escape(g["title"]["gu"])}</span></div>')
        for it in g["items"]:
            out.append(card(it["q"]["en"], it["q"]["gu"], f'<p>{it["a"]["en"]}</p>', f'<p>{it["a"]["gu"]}</p>'))
    out.append('</section>')

    out.append('<section class="panel" data-panel="exam" hidden>')
    out.append(f'<div class="intro">{html.escape(unit["question_provenance"])} — marks are suggested.</div>')
    for i, q in enumerate(unit["exam_questions"], 1):
        out.append(card(f'Q{i}. ({q["marks"]} marks)', f'Q{i}. ({q["marks"]} marks)',
                        f'<p>{html.escape(q["q"]["en"])}</p>', f'<p>{html.escape(q["q"]["gu"])}</p>'))
    out.append('<p class="pill">Model answers: see “Answered practice” at the end of the Notes tab — matched 1:1.</p></section>')
    out.append('</div>')
    return "".join(out)

def build():
    out = ['<!doctype html><html lang="gu"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">'
           f'<title>DI04005071 Petroleum Refining and Petroleum Technology — Complete Notes (Units 1–5)</title><style>{CSS}</style>']
    out.append('<body data-lang="gu"><div class="controls"><strong style="flex:1">DI04005071 • Petroleum Refining and Petroleum Technology (Units 1–5)</strong>'
               '<button id="langBtn" type="button">English</button></div><main class="app">')
    out.append('<nav class="units">' + "".join(
        f'<button data-unitbtn="{u["unit"]}" class="{"active" if u["unit"] == 1 else ""}">Unit {u["unit"]}</button>' for u in units) + '</nav>')
    for u in units:
        out.append(unit_block(u))
    out.append('<div class="footer">DRAFT preview — DiplomaOne DI04005071, complete subject (5 units, 45 teaching hours, 100% weightage). '
               'Not yet published. Sources: official GTU syllabus DI04005071 (w.e.f. 2025–26) and the syllabus books listed in subject.json. '
               'Exam questions are original practice items in the official syllabus coverage; suggested marks only.</div>')
    out.append('</main><script>'
               'const b=document.getElementById("langBtn");b.onclick=()=>{const bd=document.body;const en=bd.dataset.lang==="en";bd.dataset.lang=en?"gu":"en";b.textContent=en?"English":"ગુજરાતી"};'
               'document.querySelectorAll("[data-unitbtn]").forEach(x=>x.onclick=()=>{document.querySelectorAll("[data-unitbtn]").forEach(y=>y.classList.remove("active"));x.classList.add("active");document.querySelectorAll(".unitblock").forEach(p=>p.hidden=p.dataset.unit!==x.dataset.unitbtn)});'
               'document.querySelectorAll(".unitblock").forEach(ub=>{ub.querySelectorAll(".tabs button").forEach(x=>x.onclick=()=>{ub.querySelectorAll(".tabs button").forEach(y=>y.classList.remove("active"));x.classList.add("active");ub.querySelectorAll(".panel").forEach(p=>p.hidden=p.dataset.panel!==x.dataset.tab)})});'
               '</script></body></html>')
    dest = ROOT / "DI04005071_complete_preview.html"
    dest.write_text("".join(out), encoding="utf-8")
    print(f"wrote {dest} ({dest.stat().st_size/1024:.1f} KB)")

if __name__ == "__main__":
    build()
