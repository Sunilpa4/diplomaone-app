#!/usr/bin/env python3
"""Build the solved-papers shelf for the workshop preview.

Output (all generated, do not hand-edit):

  preview/workshop/papers/index.html                 hub: one card per paper
  preview/workshop/papers/<CODE>/<session>.en.html    paper with only English blocks
  preview/workshop/papers/<CODE>/<session>.gu.html    paper with only Gujarati blocks
  preview/workshop/papers.html                        legacy entry point -> papers/index.html

Every card is a real link to a standalone page, so the preview needs no iframe, no
fetch and no cross-frame scripting. Each paper copy also gets a small navigation bar
(back to the hub / ગુ-EN switch / original PDF) so browsing stays inside the workshop.

Run:  python3 tools/solved_papers_preview.py [--check]
"""
import argparse
import html
import json
import os
import re
import sys
from html.parser import HTMLParser
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
META = HERE / "papers" / "data"
PAPERS = ROOT / "papers-upload" / "papers"
SHELF = ROOT / "preview" / "workshop"
OUT = SHELF / "papers"
HUB = OUT / "index.html"
LEGACY = SHELF / "papers.html"

ORDER = [
    ("DI01005011", "winter-2025"),
    ("DI01005011", "summer-2026"),
    ("DI01005021", "summer-2026"),
    ("DI01005021", "winter-2025"),
]

VOID = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta",
        "param", "source", "track", "wbr", "path", "line", "rect", "circle", "ellipse",
        "polygon", "polyline", "stop", "use"}


# ------------------------------------------------------------------ language filter
class LangFilter(HTMLParser):
    """Re-emit a solved paper keeping only one language's blocks.

    Same intent as website/app.js `sanitizePaper`, done at build time so the result is a
    plain standalone page a browser can open directly.
    """

    def __init__(self, drop):
        super().__init__(convert_charrefs=False)
        self.drop = drop
        self.skip = 0
        self.out = []

    def _open(self, tag, attrs, self_closing):
        if self.skip:
            if tag not in VOID:
                self.skip += 1
            return
        marks = (dict(attrs).get("class") or "").split()
        if self.drop in marks:
            if tag not in VOID and not self_closing:
                self.skip = 1
            return
        bits = [tag] + [f' {k}="{v}"' if v is not None else f" {k}" for k, v in attrs]
        self.out.append("<" + "".join(bits) + (" />" if self_closing else ">"))

    def handle_starttag(self, tag, attrs):
        self._open(tag, attrs, False)

    def handle_startendtag(self, tag, attrs):
        self._open(tag, attrs, True)

    def handle_endtag(self, tag):
        if self.skip:
            if tag not in VOID:
                self.skip -= 1
            return
        if tag not in VOID:
            self.out.append(f"</{tag}>")

    def handle_data(self, data):
        if not self.skip:
            self.out.append(data)

    def handle_entityref(self, name):
        if not self.skip:
            self.out.append(f"&{name};")

    def handle_charref(self, name):
        if not self.skip:
            self.out.append(f"&#{name};")

    def handle_decl(self, decl):
        if not self.skip:
            self.out.append(f"<!{decl}>")

    def handle_comment(self, data):
        if not self.skip:
            self.out.append(f"<!--{data}-->")


def language_copy(raw, keep, language):
    parser = LangFilter("gu" if keep == "en" else "en")
    parser.feed(raw)
    parser.close()
    return re.sub(r'(<html[^>]*\blang=")[^"]*"', r"\g<1>" + language + '"', "".join(parser.out), count=1)


# ------------------------------------------------------------------ source data
def meta_for(code, session):
    path = META / f"{code}_{session.replace('-', '')}_meta.json"
    if not path.is_file():
        return {}
    return json.loads(path.read_text(encoding="utf-8")).get("meta", {})


def counts(path):
    raw = path.read_text(encoding="utf-8")
    half = lambda pattern: len(re.findall(pattern, raw))
    return {
        "cards": half(r'<details class="card"'),
        "figures": half(r"<figure") // 2 or half(r"<figure"),
        "tables": half(r"<table") // 2 or half(r"<table"),
        "worked": half(r'class="work"') // 2 or half(r'class="work"'),
        "kb": round(path.stat().st_size / 1024),
    }


def label(session):
    a, b = session.split("-")
    return f"{a.capitalize()} {b}"


def rel(target, start=None):
    """Root-absolute URL path for a workspace file.

    The hub is served at `/` (the server maps it there), so a relative href would resolve
    against the wrong base and 404. Absolute paths point at the real files instead.
    """
    return "/" + Path(target).resolve().relative_to(ROOT).as_posix()


def collect():
    rows = []
    for code, session in ORDER:
        src = PAPERS / code / f"{session}.html"
        if not src.is_file():
            print(f"skip {code}/{session}: no html", file=sys.stderr)
            continue
        meta = meta_for(code, session)
        pdf = PAPERS / code / f"{session}.pdf"
        rows.append({
            "code": code,
            "session": session,
            "title": meta.get("title_en", code),
            "exam": meta.get("exam_date", ""),
            "marks": meta.get("marks", ""),
            "pdf": pdf if pdf.is_file() else None,
            "stats": counts(src),
            "source": src,
        })
    return rows


# ------------------------------------------------------------------ paper pages
BAR_CSS = """
.pv-bar{position:sticky;top:0;z-index:9;display:flex;gap:10px;align-items:center;justify-content:space-between;
 flex-wrap:wrap;background:#4c1d80;color:#fff;padding:9px 14px;font:600 13px/1.35 system-ui,-apple-system,"Segoe UI",Roboto,sans-serif}
.pv-bar a{color:#fff;text-decoration:none;border-bottom:1px solid rgba(255,255,255,.45)}
.pv-bar a:hover{border-bottom-color:#fff}
.pv-bar .pv-right{display:flex;gap:10px;align-items:center;flex-wrap:wrap}
.pv-bar .pv-on{background:#fff;color:#4c1d80;border-radius:999px;padding:4px 11px;font-weight:800;border:0}
.pv-bar .pv-off{background:rgba(255,255,255,.14);border:1px solid rgba(255,255,255,.5);border-radius:999px;padding:4px 11px;font-weight:700}
"""


def bar(row, keep, out_dir):
    pdf = ""
    if row["pdf"]:
        pdf = f'<a href="{rel(row["pdf"])}" target="_blank" rel="noopener">PDF ↗</a>'
    other = "gu" if keep == "en" else "en"
    other_href = f"/preview/workshop/papers/{row['code']}/{row['session']}.{other}.html"
    en = '<span class="pv-on">EN</span>' if keep == "en" else f'<a class="pv-off" href="{other_href}">EN</a>'
    gu = '<span class="pv-on">ગુ</span>' if keep == "gu" else f'<a class="pv-off" href="{other_href}">ગુ</a>'
    return (
        '<div class="pv-bar">'
        f'<a href="{rel(HUB)}">← All solved papers</a>'
        f'<span>{html.escape(row["code"])} · {label(row["session"])} · {html.escape(row["title"])}</span>'
        f'<span class="pv-right">{pdf}<span>{en}{gu}</span></span>'
        "</div>"
    )


def paper_page(row, keep):
    out_dir = OUT / row["code"]
    out_dir.mkdir(parents=True, exist_ok=True)
    page = language_copy(row["source"].read_text(encoding="utf-8"), keep, keep)
    nav = bar(row, keep, out_dir)
    page = page.replace("</head>", f"<style>{BAR_CSS}</style></head>", 1)
    page = re.sub(r"(<body[^>]*>)", lambda m: m.group(1) + nav, page, count=1)
    target = out_dir / f'{row["session"]}.{keep}.html'
    target.write_text(page, encoding="utf-8")
    return target


# ------------------------------------------------------------------ hub
def chips(st):
    parts = [(st["cards"], "answer parts"), (st["worked"], "worked examples"),
             (st["tables"], "tables"), (st["figures"], "diagrams")]
    return "".join(f'<span class="chip">{n} {name}</span>' for n, name in parts if n)


def card(row):
    st = row["stats"]
    pdf = f'<a class="link" href="{rel(row["pdf"])}" target="_blank" rel="noopener">PDF ↗</a>' if row["pdf"] else ""
    return f"""
      <div class="card">
        <div class="row">
          <div>
            <div class="code">{row['code']} · {label(row['session'])}</div>
            <h2>{html.escape(row['title'])}</h2>
            <div class="sub">Semester 1 · {row['marks']} marks · exam {row['exam']} · {st['kb']} KB</div>
          </div>
        </div>
        <div class="chips">{chips(st)}</div>
        <div class="links">
          <a class="open" href="/preview/workshop/papers/{row['code']}/{row['session']}.en.html">Read in English →</a>
          <a class="open gu" href="/preview/workshop/papers/{row['code']}/{row['session']}.gu.html">ગુજરાતીમાં વાંચો →</a>
          {pdf}
        </div>
      </div>"""


HUB_PAGE = """<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>DiplomaOne · solved papers</title>
<style>
 :root{{--p:#7B2CD9;--pd:#5B1BB0;--lav:#EADDF7;--bg:#F3ECFA;--ink:#1d1b20;--muted:#6b6478}}
 *{{box-sizing:border-box}}
 body{{margin:0;background:var(--bg);color:var(--ink);font:15px/1.55 system-ui,-apple-system,"Segoe UI",Roboto,sans-serif}}
 header{{background:var(--p);color:#fff;padding:20px 18px 18px}}
 header .wrap{{max-width:820px;margin:0 auto}}
 header h1{{margin:0 0 4px;font-size:21px;letter-spacing:.2px}}
 header p{{margin:0;opacity:.9;font-size:13.5px}}
 main{{max-width:820px;margin:0 auto;padding:16px 14px 40px}}
 .bar{{margin:0 2px 6px;color:var(--muted);font-size:13px}}
 .bar b{{color:var(--pd)}}
 .bar a{{color:var(--pd)}}
 .card{{background:#fff;border-radius:12px;padding:14px 15px;margin:12px 0;border:1px solid #eadcf9;
   box-shadow:0 1px 3px rgba(60,20,110,.14)}}
 .card:hover{{border-color:var(--p);box-shadow:0 4px 14px rgba(60,20,110,.18)}}
 .row{{display:flex;gap:12px;justify-content:space-between;align-items:flex-start}}
 .code{{font:700 11.5px/1 ui-monospace,monospace;color:var(--p);letter-spacing:.4px;text-transform:uppercase}}
 h2{{margin:5px 0 4px;font-size:17px;line-height:1.3}}
 .sub{{color:var(--muted);font-size:12.5px}}
 .chips{{margin-top:10px;display:flex;gap:6px;flex-wrap:wrap}}
 .chip{{background:#F5EEFD;color:var(--pd);border-radius:999px;padding:3px 9px;font-size:11.5px;font-weight:700}}
 .links{{margin-top:12px;display:flex;gap:10px;flex-wrap:wrap}}
 .links a{{display:inline-block;border-radius:9px;padding:8px 13px;font:700 13px/1 system-ui,sans-serif;text-decoration:none;
   background:var(--p);color:#fff}}
 .links a:hover{{background:var(--pd)}}
 .links a.gu{{background:#fff;color:var(--pd);border:1px solid #cbb0ea}}
 .links a.link{{background:#fff;color:var(--pd);border:1px solid #e2d5f2}}
 footer{{max-width:820px;margin:0 auto;padding:0 14px 30px;color:var(--muted);font-size:12px}}
 code{{background:#F1E9FB;color:var(--pd);border-radius:4px;padding:1px 5px;font-size:12.5px}}
</style></head>
<body>
<header><div class="wrap">
  <h1>Solved papers</h1>
  <p>Chemical Engineering Semester 1 · {count} papers · all 28 printed parts answered in both languages</p>
</div></header>
<main>
  <div class="bar"><b>Tap a language button</b> — each paper opens as its own page, so it always loads.</div>
  <div class="bar"><a href="/preview/workshop/index.html">← Unit notes shelf</a> · {units} authored unit previews</div>
{cards}
</main>
<footer>Generated by <code>tools/solved_papers_preview.py</code> from <code>papers-upload/papers/</code> · same markup the app reader shows.</footer>
</body></html>
"""

LEGACY_PAGE = """<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8">
<meta http-equiv="refresh" content="0; url=papers/index.html">
<title>DiplomaOne · solved papers</title>
<style>body{{margin:0;background:#F3ECFA;color:#1d1b20;font:15px/1.6 system-ui,sans-serif;padding:40px;text-align:center}}
a{{color:#5B1BB0}}</style></head>
<body><p>Solved papers moved to <a href="papers/index.html">papers/index.html</a>.</p></body></html>
"""


def unit_count():
    path = SHELF / "manifest.json"
    try:
        return len(json.loads(path.read_text(encoding="utf-8")).get("units", []))
    except (OSError, ValueError):
        return 0


def build():
    rows = collect()
    OUT.mkdir(parents=True, exist_ok=True)
    pages = [(row, paper_page(row, keep)) for row in rows for keep in ("en", "gu")]
    hub = HUB_PAGE.format(count=len(rows), units=unit_count(), cards="".join(card(r) for r in rows))
    return rows, pages, hub


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true", help="fail if the generated files are out of date")
    args = ap.parse_args()
    rows, pages, hub = build()
    stale = []
    if HUB.read_text(encoding="utf-8") != hub if HUB.is_file() else True:
        stale.append(HUB)
    stale += [p for _, p in pages if not p.is_file()]
    if args.check:
        if stale:
            print("solved-papers preview is stale - run python3 tools/solved_papers_preview.py")
            for p in stale[:5]:
                print("  ", p.relative_to(ROOT))
            return 1
        print(f"solved-papers preview is current ({len(rows)} papers, {len(pages)} pages)")
        return 0
    HUB.write_text(hub, encoding="utf-8")
    LEGACY.write_text(LEGACY_PAGE, encoding="utf-8")
    print(f"wrote {HUB.relative_to(ROOT)} with {len(rows)} papers")
    for row, page in pages:
        print(f"  {page.relative_to(ROOT)}  {page.stat().st_size // 1024} KB")
    return 0


if __name__ == "__main__":
    sys.exit(main())
