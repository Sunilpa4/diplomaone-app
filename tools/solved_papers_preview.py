#!/usr/bin/env python3
"""Build the solved-papers shelf page for the workshop preview.

Reads the four solved-paper metas + their built HTML and writes
preview/workshop/papers.html: one card per paper, opening the paper in a
reader pane that hides the language the reader did not pick (same behaviour as
website/app.js `sanitizePaper`).

Run:  python3 tools/solved_papers_preview.py [--check]
"""
import argparse
import html
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
META = HERE / "papers" / "data"
PAPERS = ROOT / "papers-upload" / "papers"
ORIGINALS = ROOT / "papers-upload" / "originals"
OUT = ROOT / "preview" / "workshop" / "papers.html"

ORDER = [
    ("DI01005011", "winter-2025"),
    ("DI01005011", "summer-2026"),
    ("DI01005021", "summer-2026"),
    ("DI01005021", "winter-2025"),
]


def meta_for(code, session):
    slug = session.replace("-", "")
    path = META / f"{code}_{slug}_meta.json"
    if not path.is_file():
        return {}
    return json.loads(path.read_text(encoding="utf-8")).get("meta", {})


def counts(path):
    raw = path.read_text(encoding="utf-8")
    cards = len(re.findall(r'<details class="card"', raw))
    figures = len(re.findall(r"<figure", raw)) // 2 or len(re.findall(r"<figure", raw))
    tables = len(re.findall(r"<table", raw)) // 2 or len(re.findall(r"<table", raw))
    worked = len(re.findall(r'class="work"', raw)) // 2 or len(re.findall(r'class="work"', raw))
    return {
        "cards": cards,
        "figures": figures,
        "tables": tables,
        "worked": worked,
        "kb": round(path.stat().st_size / 1024),
    }


def collect():
    rows = []
    for code, session in ORDER:
        html_path = PAPERS / code / f"{session}.html"
        if not html_path.is_file():
            print(f"skip {code}/{session}: no html", file=sys.stderr)
            continue
        pdf = PAPERS / code / f"{session}.pdf"
        meta = meta_for(code, session)
        rows.append(
            {
                "code": code,
                "session": session,
                "title": meta.get("title_en", code),
                "exam": meta.get("exam_date", ""),
                "marks": meta.get("marks", ""),
                "file": f"../../papers-upload/papers/{code}/{session}.html",
                "pdf": f"../../papers-upload/papers/{code}/{session}.pdf" if pdf.is_file() else "",
                "stats": counts(html_path),
            }
        )
    return rows


def label(session):
    a, b = session.split("-")
    return f"{a.capitalize()} {b}"


def chips(st):
    parts = [
        (st["cards"], "answer parts"),
        (st["worked"], "worked examples"),
        (st["tables"], "tables"),
        (st["figures"], "diagrams"),
    ]
    return "".join(f'<span class="chip">{n} {name}</span>' for n, name in parts if n)


def card(p, i):
    st = p["stats"]
    pdf = (
        f'<a class="pdf" href="{p["pdf"]}" target="_blank" rel="noopener">Question paper PDF ↗</a>'
        if p["pdf"]
        else ""
    )
    return f"""
      <button class="card pick" type="button" data-i="{i}" aria-pressed="{'true' if i == 0 else 'false'}">
        <div class="row">
          <div>
            <div class="code">{p['code']} · {label(p['session'])}</div>
            <h2>{html.escape(p['title'])}</h2>
            <div class="sub">Semester 1 · {p['marks']} marks · exam {p['exam']} · {st['kb']} KB</div>
          </div>
          <div class="go">Read →</div>
        </div>
        <div class="chips">{chips(st)}</div>
        {pdf}
      </button>"""


PAGE = """<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>DiplomaOne · solved papers</title>
<style>
 :root{{--p:#7B2CD9;--pd:#5B1BB0;--lav:#EADDF7;--bg:#F3ECFA;--ink:#1d1b20;--muted:#6b6478}}
 *{{box-sizing:border-box}}
 body{{margin:0;background:var(--bg);color:var(--ink);font:15px/1.55 system-ui,-apple-system,"Segoe UI",Roboto,sans-serif}}
 header{{background:var(--p);color:#fff;padding:20px 18px 18px}}
 header .wrap{{max-width:1180px;margin:0 auto;display:flex;gap:14px;align-items:center;justify-content:space-between;flex-wrap:wrap}}
 header h1{{margin:0 0 4px;font-size:21px;letter-spacing:.2px}}
 header p{{margin:0;opacity:.9;font-size:13.5px}}
 .lang{{flex:none;border:1px solid rgba(255,255,255,.55);background:rgba(255,255,255,.12);color:#fff;border-radius:999px;
   padding:8px 15px;font:700 13px/1 system-ui,sans-serif;cursor:pointer}}
 .lang:hover{{background:rgba(255,255,255,.22)}}
 main{{max-width:1180px;margin:0 auto;padding:16px 14px 40px}}
 .bar{{display:flex;gap:8px;flex-wrap:wrap;align-items:center;margin:0 2px 14px;color:var(--muted);font-size:13px}}
 .bar b{{color:var(--pd)}}
 .card{{display:block;width:100%;text-align:left;font:inherit;color:inherit;background:#fff;border-radius:12px;padding:14px 15px;
   margin:0 0 12px;cursor:pointer;box-shadow:0 1px 3px rgba(60,20,110,.14);border:1px solid #eadcf9}}
 .card:hover{{border-color:var(--p);box-shadow:0 4px 14px rgba(60,20,110,.18)}}
 .card[aria-pressed="true"]{{border-color:var(--p);box-shadow:0 0 0 2px var(--lav) inset}}
 .row{{display:flex;gap:12px;align-items:flex-start;justify-content:space-between}}
 .code{{font:700 11.5px/1 ui-monospace,monospace;color:var(--p);letter-spacing:.4px;text-transform:uppercase}}
 h2{{margin:5px 0 4px;font-size:17px;line-height:1.3}}
 .sub{{color:var(--muted);font-size:12.5px}}
 .go{{flex:none;color:var(--p);font-weight:700;font-size:13.5px;padding-top:14px}}
 .chips{{margin-top:10px;display:flex;gap:6px;flex-wrap:wrap}}
 .chip{{background:#F5EEFD;color:var(--pd);border-radius:999px;padding:3px 9px;font-size:11.5px;font-weight:700}}
 .pdf{{display:inline-block;margin-top:9px;font-size:12.5px;color:var(--pd);text-decoration:none;border-bottom:1px solid var(--lav)}}
 .reader{{margin-top:6px;background:#fff;border-radius:12px;border:1px solid #eadcf9;overflow:hidden;box-shadow:0 1px 3px rgba(60,20,110,.14)}}
 .reader-top{{display:flex;gap:10px;justify-content:space-between;align-items:center;padding:9px 13px;border-bottom:1px solid #eadcf9;
   font-size:12.5px;color:var(--muted);flex-wrap:wrap}}
 .reader-top b{{color:var(--pd)}}
 iframe{{display:block;width:100%;height:78vh;min-height:520px;border:0;background:#f8f7f9}}
 .status{{padding:30px;text-align:center;color:var(--muted);font-size:13.5px}}
 footer{{max-width:1180px;margin:0 auto;padding:0 14px 30px;color:var(--muted);font-size:12px}}
 code{{background:#F1E9FB;color:var(--pd);border-radius:4px;padding:1px 5px;font-size:12.5px}}
</style></head>
<body>
<header><div class="wrap">
  <div>
    <h1>Solved papers</h1>
    <p>Chemical Engineering Semester 1 · {count} papers · all 28 printed parts answered in both languages</p>
  </div>
  <button class="lang" id="lang" type="button">ગુ / <strong>EN</strong></button>
</div></header>
<main>
  <div class="bar"><b>How to review:</b> pick a paper → it opens in the reader below → the language button swaps every answer block.</div>
{cards}
  <div class="reader">
    <div class="reader-top" id="reader-top"></div>
    <div class="status" id="status">Loading…</div>
    <iframe id="view" title="Solved paper reader" hidden></iframe>
  </div>
</main>
<footer>Generated by <code>tools/solved_papers_preview.py</code> from <code>papers-upload/papers/</code> · same markup the app reader shows.</footer>
<script>
const PAPERS = {data};
let i = 0;
let lang = 'en';
const cache = new Map();
const view = document.getElementById('view');
const status = document.getElementById('status');
const top = document.getElementById('reader-top');
const btn = document.getElementById('lang');

function paintLang(){{
  document.documentElement.lang = lang;
  btn.innerHTML = lang === 'en' ? 'ગુ / <strong>EN</strong>' : '<strong>ગુ</strong> / EN';
  btn.setAttribute('aria-label', lang === 'en' ? 'Switch to Gujarati' : 'Switch to English');
}}
function notice(){{
  const p = PAPERS[i];
  top.innerHTML = `<span><b>${{p.code}} · ${{p.session}}</b> — ${{p.title}}</span>` +
    (p.pdf ? `<a class="pdf" href="${{p.pdf}}" target="_blank" rel="noopener">Original question paper (PDF) ↗</a>` : '');
}}
// Same idea as website/app.js: keep only the chosen language's blocks.
function filter(html, language){{
  const doc = new DOMParser().parseFromString(html, 'text/html');
  doc.querySelectorAll('.en, .gu').forEach(node => {{
    const isEn = node.classList.contains('en');
    if ((isEn && language !== 'en') || (!isEn && language !== 'gu')) node.remove();
  }});
  doc.documentElement.lang = language;
  return '<!doctype html>' + doc.documentElement.outerHTML;
}}
async function load(){{
  const p = PAPERS[i];
  paintLang(); notice();
  document.querySelectorAll('.pick').forEach(el => el.setAttribute('aria-pressed', String(+el.dataset.i === i)));
  status.hidden = false; view.hidden = true; status.textContent = 'Loading ' + p.code + ' · ' + p.session + ' …';
  try {{
    if (!cache.has(p.file)) {{
      const res = await fetch(p.file, {{ cache: 'no-store' }});
      if (!res.ok) throw new Error('HTTP ' + res.status);
      cache.set(p.file, await res.text());
    }}
    view.srcdoc = filter(cache.get(p.file), lang);
    view.hidden = false; status.hidden = true;
  }} catch (err) {{
    view.hidden = true; status.hidden = false;
    status.textContent = 'Could not load the paper (' + err.message + '). Serve the repository root: python3 tools/notes_workshop.py serve --root';
  }}
}}
document.querySelectorAll('.pick').forEach(el => el.addEventListener('click', () => {{ i = +el.dataset.i; load(); }}));
btn.addEventListener('click', () => {{ lang = lang === 'en' ? 'gu' : 'en'; if (view.hidden === false) {{ load(); }} else {{ paintLang(); }} }});
paintLang(); load();
</script>
</body></html>
"""


def build():
    rows = collect()
    data = json.dumps(rows, ensure_ascii=False, separators=(",", ":"))
    page = PAGE.format(count=len(rows), cards="".join(card(p, i) for i, p in enumerate(rows)), data=data)
    return page, rows


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true", help="fail if the page on disk is out of date")
    args = ap.parse_args()
    page, rows = build()
    if args.check:
        current = OUT.read_text(encoding="utf-8") if OUT.is_file() else ""
        if current != page:
            print("preview/workshop/papers.html is stale - run python3 tools/solved_papers_preview.py")
            return 1
        print(f"papers.html is current ({len(rows)} papers)")
        return 0
    OUT.write_text(page, encoding="utf-8")
    print(f"wrote {OUT.relative_to(ROOT)} with {len(rows)} papers")
    for r in rows:
        print(f"  {r['code']} {r['session']:<11} {r['stats']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
