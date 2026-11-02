"""Build preview/index.html: a browsable list of every unit preview in preview/.

    python3 tools/preview_index.py

Run it after adding a preview so the new file appears at the top of the list.
Each row links straight to the self-contained unit HTML; nothing is fetched
from the internet.
"""
import json
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PREVIEW = os.path.join(ROOT, "preview")
NAME = re.compile(r"^([A-Z]{2}\d{8})_unit(\d+)_preview\.html$")
SUBJECT = re.compile(r"^([A-Z]{2}\d{8})-complete\.html$")


def _subject_name(code):
    """Look the code up in the content tree so the index shows a real title."""
    base = os.path.join(ROOT, "content")
    for branch in sorted(os.listdir(base)):
        bdir = os.path.join(base, branch)
        if not os.path.isdir(bdir):
            continue
        for sem in sorted(os.listdir(bdir)):
            sp = os.path.join(bdir, sem, code, "subject.json")
            if os.path.exists(sp):
                try:
                    with open(sp, encoding="utf-8") as f:
                        d = json.load(f)
                    name = d.get("name") or {}
                    return (name.get("en") if isinstance(name, dict) else str(name)) or code, \
                           sem.replace("sem", ""), branch
                except Exception:
                    return code, sem.replace("sem", ""), branch
    return code, "", ""


def _unit_state(code):
    """How many syllabus units of this subject have authored content."""
    base = os.path.join(ROOT, "content")
    for branch in sorted(os.listdir(base)):
        bdir = os.path.join(base, branch)
        if not os.path.isdir(bdir):
            continue
        for sem in sorted(os.listdir(bdir)):
            d = os.path.join(bdir, sem, code)
            sj = os.path.join(d, "subject.json")
            if not os.path.exists(sj):
                continue
            try:
                with open(sj, encoding="utf-8") as f:
                    total = len(json.load(f).get("units") or [])
            except Exception:
                total = 0
            done = len([f for f in os.listdir(d) if re.match(r"^unit\d+\.json$", f)])
            return done, total
    return 0, 0


def collect_subjects():
    rows = []
    for fn in os.listdir(PREVIEW):
        m = SUBJECT.match(fn)
        if not m:
            continue
        code = m.group(1)
        name, sem, branch = _subject_name(code)
        done, total = _unit_state(code)
        rows.append({"file": fn, "code": code, "name": name, "sem": sem,
                     "branch": branch, "done": done, "total": total,
                     "kb": round(os.path.getsize(os.path.join(PREVIEW, fn)) / 1024),
                     "mtime": os.path.getmtime(os.path.join(PREVIEW, fn))})
    rows.sort(key=lambda r: (-r["mtime"], r["code"]))
    return rows


def collect():
    rows = []
    for fn in os.listdir(PREVIEW):
        m = NAME.match(fn)
        if not m:
            continue
        code, unit = m.group(1), int(m.group(2))
        name, sem, branch = _subject_name(code)
        rows.append({"file": fn, "code": code, "unit": unit, "name": name,
                     "sem": sem, "branch": branch,
                     "kb": round(os.path.getsize(os.path.join(PREVIEW, fn)) / 1024),
                     "mtime": os.path.getmtime(os.path.join(PREVIEW, fn))})
    rows.sort(key=lambda r: (-r["mtime"], r["code"], r["unit"]))
    return rows


CSS = """
:root{--p:#7B2CD9;--pd:#5B1BB0;--bg:#F3ECFA;--ink:#1E1530;--muted:#6B6275}
*{box-sizing:border-box}
body{margin:0;font-family:system-ui,-apple-system,"Segoe UI",Roboto,Arial,sans-serif;
     background:var(--bg);color:var(--ink);padding:28px 18px 60px}
.wrap{max-width:960px;margin:0 auto}
header{background:linear-gradient(135deg,#8E3BE8,#5B1BB0);color:#fff;border-radius:16px;
       padding:26px 28px;margin-bottom:22px}
h1{margin:0 0 6px;font-size:24px;letter-spacing:.2px}
header p{margin:0;opacity:.9;font-size:14px}
.count{display:inline-block;margin-top:14px;background:rgba(255,255,255,.18);
       border-radius:999px;padding:5px 14px;font-size:13px;font-weight:600}
h2{font-size:15px;text-transform:uppercase;letter-spacing:1px;color:var(--pd);
   margin:26px 0 10px}
.group{background:#fff;border-radius:14px;overflow:hidden;
       box-shadow:0 1px 2px rgba(30,21,48,.06),0 8px 24px rgba(91,27,176,.07)}
.group h3{margin:0;padding:14px 18px;font-size:14px;background:#FBF7FF;
          border-bottom:1px solid #EDE4FA;color:var(--pd)}
a.row{display:flex;align-items:center;gap:12px;padding:13px 18px;text-decoration:none;
      color:inherit;border-bottom:1px solid #F3EEFB;transition:background .12s}
a.row:last-child{border-bottom:none}
a.row:hover{background:#FAF5FF}
.code{font-family:ui-monospace,Menlo,Consolas,monospace;font-size:12.5px;font-weight:700;
      color:var(--pd);background:#F5EEFD;border-radius:6px;padding:3px 8px;flex:0 0 auto}
.name{flex:1;font-size:14.5px}
.unit{font-size:12px;color:var(--muted);flex:0 0 auto}
.go{font-size:12px;font-weight:700;color:#fff;background:var(--p);border-radius:999px;
    padding:5px 13px;flex:0 0 auto}
.empty{background:#fff;border-radius:14px;padding:30px;text-align:center;color:var(--muted)}
footer{margin-top:26px;font-size:12.5px;color:var(--muted);text-align:center;line-height:1.7}
"""


def build():
    rows = collect()
    groups = {}
    for r in rows:
        key = f"{r['code']} — {r['name']}"
        groups.setdefault(key, {"sem": r["sem"], "branch": r["branch"], "units": []})
        groups[key]["units"].append(r)

    parts = [f"""<!doctype html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>DiplomaOne — unit previews</title><style>{CSS}</style></head><body><div class="wrap">
<header><h1>DiplomaOne — unit previews</h1>
<p>Self-contained unit notes. Open one and use the EN ⇄ ગુ toggle at the top right.</p>
<div class="count">{len(rows)} unit preview{'s' if len(rows) != 1 else ''} · {len(groups)} subject{'s' if len(groups) != 1 else ''}</div>
</header>"""]

    subs = collect_subjects()
    if subs:
        parts.append('<h2>Subjects — all units in one page</h2><div class="group">')
        for r in subs:
            meta = " • ".join(x for x in [r["branch"].title() if r["branch"] else "",
                                          f"Semester {r['sem']}" if r["sem"] else ""] if x)
            parts.append(
                f'<a class="row" href="{r["file"]}">'
                f'<span class="code">{r["code"]}</span>'
                f'<span class="name">{r["name"]}<br>'
                f'<small style="color:#6B6275">{meta} &nbsp;·&nbsp; '
                f'{r["done"]}/{r["total"]} units authored &nbsp;·&nbsp; EN + ગુજરાતી</small></span>'
                f'<span class="done {"full" if r["done"] == r["total"] and r["total"] else "part"}">'
                f'{r["done"]}/{r["total"]} units</span>'
                f'<span class="go">open</span></a>')
        parts.append("</div>")

    if not rows:
        parts.append('<div class="empty">No previews yet. Run '
                     '<code>python3 tools/build_DI04005041_u1.py</code>.</div>')

    for key in sorted(groups):
        g = groups[key]
        meta = " · ".join(x for x in [g["branch"].title() if g["branch"] else "",
                                     f"Semester {g['sem']}" if g["sem"] else ""] if x)
        parts.append(f'<h2>{meta}</h2><div class="group"><h3>{key}</h3>')
        for u in sorted(g["units"], key=lambda x: x["unit"]):
            parts.append(
                f'<a class="row" href="{u["file"]}">'
                f'<span class="code">{u["code"]}</span>'
                f'<span class="name">Unit {u["unit"]}</span>'
                f'<span class="unit">{u["kb"]} KB</span>'
                f'<span class="go">open</span></a>')
        parts.append("</div>")

    parts.append("""<footer>Files live in <code>preview/</code> in the repository.
To add one, build a preview and re-run <code>python3 tools/preview_index.py</code>.<br>
Every page is offline-capable: no fonts, scripts or images are loaded from the internet.</footer>
</div></body></html>""")

    out = os.path.join(PREVIEW, "index.html")
    with open(out, "w", encoding="utf-8") as f:
        f.write("\n".join(parts))
    return out, len(rows)


if __name__ == "__main__":
    path, n = build()
    print(f"wrote {path} ({n} previews indexed)")
