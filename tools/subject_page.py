"""Build one self-contained, subject-complete HTML in the reference layout.

    python3 tools/subject_page.py DI04005021
    python3 tools/subject_page.py DI04005021 -o preview/Mass-Transfer-I-complete.html

Layout matched to the GTU-style reference the user asked for:
  - sticky bar: unit <select> + language button (EN / ગુજરાતી)
  - purple .bar with title, then "subject • code • branch Semester N • hours/% • year"
  - .tabs row, one tab set per unit and language
  - .intro coverage sentence
  - .section headers with a "બધું ખોલો / બંધ કરો" (open/close all) button
  - cards as <details><summary>, body h4/p/ul/svg
  - exam questions carry (4marks), viva collapses to Q + A

Everything is inlined: SVGs, styles, script. No external requests, so the file
opens offline and can be mailed or printed.
"""
import argparse
import html
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

TAB_LABELS = {
    "notes": ("Notes", "નોટ્સ"),
    "programs": ("Practical / Numericals", "પ્રેક્ટિકલ"),
    "diagrams": ("Diagrams", "ડાયાગ્રામ"),
    "syntax": ("Equations & Summary", "સમીકરણો તથા Summary"),
    "viva": ("Viva", "વાઇવા"),
    "exam": ("Exam", "પરીક્ષા"),
    "coverage": ("Syllabus coverage", "Syllabus કવરેજ"),
}


def _bi(v, lang):
    if isinstance(v, dict):
        return v.get(lang) or v.get("en") or ""
    return str(v or "")


def _find_subject(code):
    base = os.path.join(ROOT, "content")
    for branch in sorted(os.listdir(base)):
        bdir = os.path.join(base, branch)
        if not os.path.isdir(bdir):
            continue
        for sem in sorted(os.listdir(bdir)):
            d = os.path.join(bdir, sem, code)
            if os.path.isdir(d):
                return d, branch, int(sem.replace("sem", ""))
    raise SystemExit(f"subject {code} not found under content/")


def _svg(svg_path):
    if not os.path.exists(svg_path):
        return ""
    with open(svg_path, encoding="utf-8") as f:
        s = f.read().strip()
    # make it behave inside the card
    s = s.replace("<svg ", '<svg class="diagram" preserveAspectRatio="xMidYMid meet" ', 1)
    return s


STOP = set("""a an and are as at be by for from has have in into is it its of on or
that the their then there these this to was were with within without which while
also such only more most other than when where how why does do not no can may such""".split())


def _plain(t):
    return re.sub(r"<[^>]+>", " ", t or "")


def _terms(text):
    words = re.findall(r"[A-Za-z][A-Za-z\-]{3,}", _plain(text).lower())
    return {w for w in words if w not in STOP}


def _counts(u, lang="en"):
    cards = [i for s in (u.get("notes") or []) for i in s["items"]]
    body = " ".join(_bi(c.get("body"), lang) for c in cards)
    words = len(_plain(body).split())
    heads = " ".join(_plain(_bi(c.get("h"), lang)) for c in cards).lower()
    prog = u.get("programs") or []
    prog_text = " ".join(_bi(i.get("body"), lang) for p in prog for i in (p.get("items") or []))
    return {
        "cards": len(cards),
        "words": words,
        "derivations": heads.count("derivation"),
        "equipment": sum(1 for c in cards if "construct" in _plain(_bi(c.get("body"), "en")).lower()),
        "numericals": len(prog),
        "diagrams": len(u.get("diagrams") or []),
        "viva": len(u.get("viva") or []),
        "exam": len(u.get("exam_questions") or []),
        "formulae": sum(len(g.get("items") or []) for g in (u.get("syntax") or [])),
        "_text": _terms(body + " " + prog_text + " " + heads),
    }


def _coverage(u, syllabus):
    """Does each official syllabus clause have matching vocabulary in the unit?"""
    have = _counts(u)["_text"]
    rows = []
    for clause in syllabus or []:
        want = _terms(clause.get("topic", ""))
        if not want:
            continue
        hit = want & have
        ratio = len(hit) / len(want)
        rows.append({"no": clause["no"], "topic": clause["topic"],
                     "ratio": ratio, "hits": sorted(hit), "miss": sorted(want - hit),
                     "ok": ratio >= 0.5})
    return rows


def _cards_html(items, lang, unit_no, diagrams, start=1):
    out = []
    n = start
    for it in items:
        head = _bi(it.get("h") or it.get("title"), lang)
        body = _bi(it.get("body"), lang)
        svg = ""
        did = it.get("diagram")
        if did and did in diagrams:
            svg = _svg(diagrams[did])
        if not body and not svg:
            continue
        num = it.get("ref") or f"{unit_no}.{n}"
        n += 1
        label = f"{num} • {head}" if head else num
        open_attr = " open" if len(out) == 0 else ""
        out.append(
            f'<details class="card"{open_attr}><summary>{html.escape(label)}</summary>'
            f'<div class="body">{body}{svg}</div></details>')
    return "".join(out)


def _qa_html(items, lang, numbered=True):
    out = []
    for i, v in enumerate(items, 1):
        q = _bi(v.get("q"), lang)
        a = _bi(v.get("a"), lang)
        if not q:
            continue
        n = f"{i}. " if numbered else ""
        out.append(
            f'<details class="card"><summary>{n}{html.escape(q)}</summary>'
            f'<div class="body"><p>{a}</p></div></details>')
    return "".join(out)


def _exam_html(items, lang):
    out = ["<ol>"]
    for x in items:
        q = _bi(x.get("q"), lang)
        mk = x.get("marks") or 4
        out.append(f'<li>{q} <span class="pill">({mk}marks)</span></li>')
    out.append("</ol>")
    return "".join(out)


def _syntax_html(groups, lang):
    out = []
    for g in groups:
        title = _bi(g.get("title"), lang)
        body = g.get("body")
        out.append(f"<h4>{html.escape(title)}</h4>")
        if body:
            out.append(_bi(body, lang))
            continue
        rows = []
        for it in g.get("items") or []:
            t = _bi(it.get("title"), lang)
            f = it.get("f") or ""
            terms = it.get("terms") or ""
            rows.append(f"<tr><td><b>{html.escape(t)}</b></td><td><code>{html.escape(f)}</code>"
                        f"<br><small>{html.escape(terms)}</small></td></tr>")
        out.append('<table class="fx"><tr><th>Relation</th><th>Formula and notes</th></tr>'
                   + "".join(rows) + "</table>")
    return "".join(out)


def _diagram_html(diagrams, lang):
    out = []
    for did, path in diagrams.items():
        title = diagrams.meta.get(did, "")
        out.append(f'<h4>{html.escape(title)}</h4>{_svg(path)}')
    return "".join(out)


def _stats_line(c, lang):
    if lang == "en":
        return (f'{c["cards"]} notes cards · {c["words"]:,} words · {c["numericals"]} solved numericals · '
                f'{c["diagrams"]} diagrams · {c["viva"]} viva · {c["exam"]} exam questions · '
                f'{c["formulae"]} formulae')
    return (f'{c["cards"]} નોટ્સ કાર્ડ · {c["words"]:,} શબ્દો · {c["numericals"]} ઉકેલેલા દાખલા · '
            f'{c["diagrams"]} ડાયાગ્રામ · {c["viva"]} વાઇવા · {c["exam"]} પરીક્ષા પ્રશ્નો · '
            f'{c["formulae"]} સૂત્રો')


def build(code, out_path=None):
    sdir, branch, sem = _find_subject(code)
    with open(os.path.join(sdir, "subject.json"), encoding="utf-8") as f:
        subject = json.load(f)
    units = []
    for u in subject.get("units", []):
        fn = u.get("file") or f"unit{u['no']}.json"
        p = os.path.join(sdir, fn)
        if not os.path.exists(p):
            continue
        with open(p, encoding="utf-8") as f:
            data = json.load(f)
        units.append(data)
    if not units:
        raise SystemExit("no unit files found")

    name_en = _bi(subject.get("name"), "en")
    year = subject.get("syllabus_year") or "2025-26"
    apps, options_gu, options_en, titles = [], [], [], {}

    for u in units:
        no = u["unit"]
        hours = u.get("hours", "")
        wt = u.get("weightage", "")
        titles[str(no)] = {"en": _bi(u["title"], "en"), "gu": _bi(u["title"], "gu")}
        options_gu.append(f'<option value="{no}">{no}. {titles[str(no)]["gu"]}</option>')
        options_en.append(f'<option value="{no}">{no}. {titles[str(no)]["en"]}</option>')

        dmap = {}
        for d in u.get("diagrams") or []:
            dmap[d["id"]] = os.path.join(sdir, d["file"])
        diagram_titles = {d["id"]: _bi(d["title"], "gu") for d in u.get("diagrams") or []}

        syl = u.get("syllabus") or (subject.get("units") or [{}])[no - 1].get("syllabus") or []
        cov = _coverage(u, syl)
        c = _counts(u)

        for lang in ("gu", "en"):
            uid = f"u{no}-{lang}"
            tabs = u.get("tabs") or ["notes", "programs", "diagrams", "syntax", "viva", "exam"]
            tabs = [t for t in tabs if t in TAB_LABELS]
            if (u.get("exam_questions")) and "exam" not in tabs:
                tabs.append("exam")
            if (u.get("syllabus") or syl) and "coverage" not in tabs:
                tabs.insert(0, "coverage")

            tabbar, panels = [], []
            first = True
            for t in tabs:
                lab = TAB_LABELS[t][0 if lang == "en" else 1]
                tabbar.append(
                    f'<button class="{"active" if first else ""}" data-tab="{uid}-{t}">{lab}</button>')
                if t == "notes":
                    all_items = [i for sec in (u.get("notes") or []) for i in sec["items"]]
                    body = (f'<div class="section"><span>{no}. {lab}</span>'
                            f'<button class="toggle-group">'
                            f'{"Open all / close all" if lang == "en" else "બધું ખોલો / બંધ કરો"}</button></div>'
                            f'<div class="group">{_cards_html(all_items, lang, no, dmap)}</div>')
                elif t == "programs":
                    progs = []
                    for p in u.get("programs") or []:
                        items = p.get("items") or []
                        body_p = "".join(_bi(i.get("body"), lang) for i in items)
                        progs.append(
                            f'<details class="card"><summary>{html.escape(_bi(p.get("title"), lang))}</summary>'
                            f'<div class="body">{body_p}</div></details>')
                    body = (f'<div class="section"><span>'
                            f'{"Solved numericals and practicals" if lang == "en" else "ઉકેલેલા દાખલા તથા પ્રેક્ટિકલ"}'
                            f'</span><button class="toggle-group">'
                            f'{"Open all / close all" if lang == "en" else "બધું ખોલો / બંધ કરો"}</button></div>'
                            f'<div class="group">{"".join(progs)}</div>')
                elif t == "diagrams":
                    body = "".join(
                        f'<h4>{html.escape(_bi(d["title"], lang))}</h4>'
                        f'{_svg(os.path.join(sdir, d["file"]))}'
                        for d in u.get("diagrams") or [])
                elif t == "syntax":
                    body = _syntax_html(u.get("syntax") or [], lang)
                elif t == "viva":
                    body = (f'<div class="section"><span>{"Viva questions" if lang == "en" else "વાઇવા પ્રશ્નો"}</span>'
                            f'<button class="toggle-group">'
                            f'{"Open all / close all" if lang == "en" else "બધું ખોલો / બંધ કરો"}</button></div>'
                            f'<div class="group">{_qa_html(u.get("viva") or [], lang)}</div>')
                elif t == "exam":
                    body = _exam_html(u.get("exam_questions") or [], lang)
                elif t == "coverage":
                    if not cov:
                        body = ('<p>No syllabus mapping recorded for this unit.</p>'
                                if lang == "en" else '<p>આ યુનિટ માટે syllabus mapping નથી.</p>')
                    else:
                        done = sum(1 for r in cov if r["ok"])
                        body = (f'<div class="section"><span>'
                                f'{"Syllabus clauses" if lang == "en" else "Syllabus કલમો"} · '
                                f'{done}/{len(cov)} '
                                f'{"covered" if lang == "en" else "આવરી લીધી"}</span></div>'
                                f'<table><tr><th>{"Clause" if lang == "en" else "કલમ"}</th>'
                                f'<th>{"Official topic" if lang == "en" else "Syllabus topic"}</th>'
                                f'<th>{"Status" if lang == "en" else "સ્થિતિ"}</th></tr>'
                                + "".join(
                                    f'<tr><td><code>{r["no"]}</code></td><td>{html.escape(r["topic"])}</td>'
                                    f'<td>{"✔ covered" if r["ok"] else "— thin"}</td></tr>'
                                    for r in cov)
                                + '</table>')
                else:
                    body = ""
                panels.append(
                    f'<section class="panel" id="{uid}-{t}"{"" if first else " hidden"}>{body}</section>')
                first = False

            intro = (f'Syllabus according to detailed theory, derivations, equipment construction and working '
                     f'and worked numericals. Practicals carry official suggested exercises and blank '
                     f'observation sheets — no fabricated results.'
                     if lang == "en" else
                     f'Syllabus મુજબ વિગતવાર Theory, derivations, equipment ના Construction/Working તથા '
                     f'worked Numericals. Practical માં official suggested exercises તથા blank observation '
                     f'sheets છે—fabricated results નથી.')
            apps.append(
                f'<main class="app" data-unit="{no}" data-language="{lang}" hidden>'
                f'<div class="bar"><strong>{no}. {html.escape(_bi(u["title"], lang))}</strong>'
                f'<small>{html.escape(name_en)} • {code} • {branch.title()} Semester{sem} • '
                f'{hours}h / {wt}% • GTU{year}</small>'
                f'<small class="stats">{_stats_line(c, lang)}</small></div>'
                f'<nav class="tabs">{"".join(tabbar)}</nav>'
                f'<div class="intro">{intro}</div>'
                f'{"".join(panels)}</main>')

    doc = f"""<!doctype html><html lang="gu"><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(name_en)} • {code}</title>
<style>{CSS}</style>
<div class="controls">
  <select id="unit" aria-label="Select unit">{''.join(options_gu)}</select>
  <button id="language">English</button>
</div>
{''.join(apps)}
<div class="footer">DiplomaOne • {html.escape(name_en)} ({code}) • original teaching material,
drawn and written for this subject. GTU syllabus {year}.</div>
<script>const TITLES={json.dumps(titles, ensure_ascii=False)};
let lang='gu';const unit=document.querySelector('#unit'),lb=document.querySelector('#language');
function show(){{
  document.querySelectorAll('.app').forEach(a=>a.hidden=a.dataset.unit!==unit.value||a.dataset.language!==lang);
  lb.textContent=lang==='gu'?'English':'ગુજરાતી';
  unit.querySelectorAll('option').forEach(o=>o.textContent=o.value+'. '+TITLES[o.value][lang]);
  document.documentElement.lang=lang;window.scrollTo(0,0);
}}
unit.onchange=show;lb.onclick=()=>{{lang=lang==='gu'?'en':'gu';show()}};
document.querySelectorAll('.tabs button').forEach(b=>b.onclick=()=>{{
  let a=b.closest('.app');
  a.querySelectorAll('.panel').forEach(p=>p.hidden=p.id!==b.dataset.tab);
  a.querySelectorAll('.tabs button').forEach(t=>t.classList.toggle('active',t===b));
}});
document.querySelectorAll('.toggle-group').forEach(b=>b.onclick=()=>{{
  let g=b.closest('.section').nextElementSibling;
  let ds=[...g.querySelectorAll('details')],open=ds.some(d=>!d.open);
  ds.forEach(d=>d.open=open);
}});
show();</script>"""

    out_path = out_path or os.path.join(ROOT, "preview", f"{code}-complete.html")
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(doc)
    return out_path, len(units)


CSS = """*{box-sizing:border-box}
body{margin:0;background:#f5f3fa;color:#272134;font:16px/1.7 system-ui,-apple-system,"Noto Sans Gujarati",Arial,sans-serif}
.controls{position:sticky;top:0;z-index:5;background:#fff;border-bottom:1px solid #e4dceb;padding:12px max(14px,calc((100vw - 1100px)/2));display:flex;gap:12px;align-items:center}
select,button{font:inherit;border:1px solid #d8c8e6;border-radius:9px;padding:8px 12px;background:white;color:#62309b;cursor:pointer}
select{flex:1;min-width:0}
.app{max-width:1100px;margin:auto;padding:16px}
.bar{background:linear-gradient(110deg,#6824aa,#8d43cb);color:#fff;padding:22px;border-radius:14px 14px 0 0}
.bar strong{display:block;font-size:23px}.bar small{display:block;opacity:.9}
.tabs{display:flex;gap:2px;flex-wrap:wrap;background:#ece1f6;padding:6px;border-radius:0 0 12px 12px;margin-bottom:18px}
.tabs button{flex:1;border:0;background:transparent;white-space:nowrap}
.tabs button.active{background:#7932b8;color:white}
.intro{border-left:4px solid #9255c3;background:#eee7f6;padding:15px 19px;margin:18px 0}
.section{display:flex;justify-content:space-between;gap:10px;align-items:center;background:#7a36b4;color:#fff;border-radius:9px;padding:12px 16px;margin:24px 0 12px;font-weight:700}
.section button{background:#ffffff22;color:white;border:0}
.card{background:#fff;border:1px solid #e6deed;border-radius:10px;margin:10px 0;box-shadow:0 2px 5px #30134406}
.card>summary{cursor:pointer;list-style:none;padding:17px 20px;font-weight:650}
.card>summary:before{content:"＋";display:inline-block;color:#8c43c3;margin-right:12px}
.card[open]>summary:before{content:"−"}
.card[open]>summary{border-bottom:1px solid #eee6f5}
.body{padding:4px 22px 20px;overflow-wrap:anywhere}
.body h4{color:#6d2ca4;margin:20px 0 8px}
.body p{margin:10px 0}.body li{margin:9px 0}
.body svg{width:100%;height:auto;max-height:750px;display:block;border:1px solid #eee;border-radius:8px;margin:18px auto}
.math{background:#f3ecfa;border-left:4px solid #7b2cd9;border-radius:6px;padding:10px 14px;margin:8px 0 12px;
font:15px/1.6 ui-monospace,Menlo,Consolas,monospace;color:#5b1bb0;overflow-x:auto;white-space:pre-wrap}
pre{background:#211a2e;color:#f5ebff;border-radius:9px;padding:18px;overflow:auto;line-height:1.55;white-space:pre;font:14px/1.6 ui-monospace,monospace}
table{width:100%;border-collapse:collapse;margin-top:18px;font-size:14px}
th,td{border:1px solid #dfd2e9;padding:9px;text-align:left}
th{background:#f1e8f8}
.pill{font-size:13px;color:#7330ab}
.footer{font-size:13px;color:#6b6275;text-align:center;padding:26px 16px 40px}
@media print{.controls{display:none}.card{border:0}.card>summary{font-weight:700}}
"""


def main():
    ap = argparse.ArgumentParser(description="Build a subject-complete HTML page")
    ap.add_argument("code", help="subject code, e.g. DI04005021")
    ap.add_argument("-o", "--out", help="output path")
    a = ap.parse_args()
    path, n = build(a.code, a.out)
    print(f"wrote {path} ({n} units, {os.path.getsize(path)//1024} KB)")


if __name__ == "__main__":
    main()
