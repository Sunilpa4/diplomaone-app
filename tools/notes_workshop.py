"""DiplomaOne notes workshop - HTML previews for the units authored *now*.

The repo has hundreds of committed previews under preview/. This tool keeps a separate,
explicitly registered shelf so a reviewer only sees what was written in the current session:

  preview/workshop/manifest.json      <- only units added with `add`
  preview/workshop/<CODE>_u<N>.html   <- self-contained phone-shaped preview (same renderer as the app)
  preview/workshop/index.html         <- shelf page listing exactly those units

Commands
  add <CODE> <unit> [--note TEXT]   render the preview and put it on the shelf
  render [<CODE> <unit>|--all]      rebuild preview(s) after editing content (shelf unchanged)
  list                              show the shelf and whether a preview is stale
  check [<CODE> <unit>|--all]       link integrity + SVG text-bounds audit for shelved units
  clear [<CODE>]                    remove from the shelf (all units, or all of one subject)
  serve [--port 8800]               serve preview/workshop over HTTP (0.0.0.0) for live review

Only `add` changes the shelf: a unit that shipped before this session can never appear here
unless it is explicitly added.
"""
import argparse
import hashlib
import html
import json
import os
import re
import sys
import time
import xml.etree.ElementTree as ET
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
CONTENT = ROOT / "content"
SHELF = ROOT / "preview" / "workshop"
MANIFEST = SHELF / "manifest.json"
SVG_NS = "{http://www.w3.org/2000/svg}"

sys.path.insert(0, str(HERE))
from preview_builder import build_preview  # noqa: E402

# --------------------------------------------------------------------- text metrics
# Advance widths of the app's own fonts (app/assets/fonts/DejaVuSans[-Bold].ttf), in per-mille
# of the font size (4 digits each), generated once from the TTFs so this tool needs no
# third-party package.
CHARS = "".join(chr(c) for c in range(32, 127))
EXTRA = "×÷≈≤≥±→←↑↓°ΩµΔπ√·–—‘’“”…₹Φω"
_REG = (
    "031804010460083806360950078002750390039005000838031803610318033706360636"
    "063606360636063606360636063606360337033708380838083805311000068406860698"
    "077006320575077507520295029506560557086307480787060307870695063506110732"
    "068409890685061106850390033703900838050005000613063505500635061503520635"
    "063402780278057902780974063406120635063504110521039206340592081805920592"
    "052506360337063608380838083808380838083808380838083808380838050007640636"
    "06840602063703180500100003180318051805181000063607870837"
)
_BOLD = (
    "034804560521083806961002087203060457045705230838038004150380036506960696"
    "069606960696069606960696069606960400040008380838083805801000077407620734"
    "083006830683082108370372037207750637099508370850073308500770072006820812"
    "077411030771072407250457036504570838050005000675071605930716067804350716"
    "071203430343066503431042071206870716071604930595047807120652092406450652"
    "058207120365071208380838083808380838083808380838083808380838050008500736"
    "07740791066703800500100003800380065706571000069608500869"
)


def _table(packed):
    keys = CHARS + EXTRA
    assert len(packed) == 4 * len(keys), "width table size mismatch"
    return {k: int(packed[4 * i:4 * i + 4]) for i, k in enumerate(keys)}


WIDTH = {"regular": _table(_REG), "bold": _table(_BOLD)}


def text_width(s, size, bold=False):
    """Rendered width in px of `s` at `size`, using the real DejaVu advance widths."""
    tbl = WIDTH["bold" if bold else "regular"]
    return sum(tbl.get(ch, 560) for ch in s) / 1000.0 * size


# --------------------------------------------------------------------- helpers
def find_subject(code):
    hits = list(CONTENT.glob(f"*/sem*/{code}/subject.json"))
    if not hits:
        raise SystemExit(f"no content folder for {code}")
    if len(hits) > 1:
        raise SystemExit(f"{code} exists in several folders: {hits}")
    return hits[0].parent


def load_unit(code, number):
    d = find_subject(code)
    f = d / f"unit{int(number)}.json"
    if not f.is_file():
        raise SystemExit(f"{f} does not exist yet - build the unit first")
    unit = json.loads(f.read_text(encoding="utf-8"))
    subject = json.loads((d / "subject.json").read_text(encoding="utf-8"))
    return d, unit, subject, f


def sha1(path):
    return hashlib.sha1(Path(path).read_bytes()).hexdigest()


def shelf():
    if not MANIFEST.is_file():
        return {"created": time.strftime("%Y-%m-%d %H:%M"), "units": []}
    return json.loads(MANIFEST.read_text(encoding="utf-8"))


def save_shelf(data):
    SHELF.mkdir(parents=True, exist_ok=True)
    MANIFEST.write_text(json.dumps(data, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")


def stats_of(unit):
    notes = unit.get("notes", [])
    return {
        "sections": len(notes),
        "cards": sum(len(s.get("items", [])) for s in notes),
        "diagrams": len(unit.get("diagrams") or []),
        "programs": len(unit.get("programs") or []),
        "numericals": len(unit.get("numericals") or []),
        "viva": sum(len(s.get("items", [])) for s in unit.get("viva") or []),
        "exam": len(unit.get("exam_questions") or []),
        "kb": round(len(json.dumps(unit)) / 1024),
    }


DRAFT_BADGE = """
<style>
 #ws-badge{position:fixed;right:12px;bottom:12px;z-index:9999;display:flex;gap:8px;align-items:center;
   background:#2b1b45;color:#fff;border-radius:999px;padding:8px 12px;font:600 12.5px/1.2 system-ui,sans-serif;
   box-shadow:0 4px 14px rgba(0,0,0,.35);text-decoration:none;opacity:.92}
 #ws-badge:hover{opacity:1}
 #ws-badge span{background:#ffb703;color:#2b1b45;border-radius:999px;padding:2px 7px;font-weight:800}
</style>
<a id="ws-badge" href="index.html"><span>DRAFT</span> __TITLE__ · back to workshop</a>
"""


def render_one(code, number, note=None, register=True):
    d, unit, subject, src = load_unit(code, number)
    SHELF.mkdir(parents=True, exist_ok=True)
    name = f"{code}_u{int(number)}.html"
    out = SHELF / name
    build_preview(unit, subject, str(d / "diagrams"), str(out))
    title = f'{subject.get("name", {}).get("en", code)} – Unit {unit.get("unit")}'
    text = out.read_text(encoding="utf-8").replace("</body>", DRAFT_BADGE.replace("__TITLE__", html.escape(title)) + "\n</body>")
    out.write_text(text, encoding="utf-8")

    if register:
        data = shelf()
        entry = {
            "code": code,
            "unit": int(number),
            "title": unit.get("title", {}).get("en", ""),
            "subject": subject.get("name", {}).get("en", code),
            "file": name,
            "built": time.strftime("%Y-%m-%d %H:%M:%S"),
            "source_sha1": sha1(src),
            "note": note or "",
            "stats": stats_of(unit),
        }
        data["units"] = [u for u in data["units"] if not (u["code"] == code and u["unit"] == int(number))]
        data["units"].insert(0, entry)
        save_shelf(data)
        write_index()
    return out


def write_index():
    data = shelf()
    rows = []
    stale = 0
    for u in data["units"]:
        src = next((p for p in CONTENT.glob(f"*/sem*/{u['code']}/unit{u['unit']}.json")), None)
        is_stale = bool(src) and sha1(src) != u["source_sha1"]
        stale += is_stale
        s = u["stats"]
        chips = "".join(
            f'<span class="chip">{n} {label}</span>'
            for n, label in ((s["sections"], "sections"), (s["cards"], "cards"), (s["diagrams"], "diagrams"),
                             (s["numericals"], "numericals"), (s["viva"], "viva"), (s["exam"], "exam Qs"))
            if n
        )
        rows.append(f"""
      <a class="card" href="{u['file']}">
        <div class="row">
          <div>
            <div class="code">{u['code']} · Unit {u['unit']}</div>
            <h2>{html.escape(u['title'])}</h2>
            <div class="sub">{html.escape(u['subject'])} · {s['kb']} KB · built {u['built']}</div>
          </div>
          <div class="go">Open →</div>
        </div>
        <div class="chips">{chips}</div>
        {f'<div class="note">{html.escape(u["note"])}</div>' if u.get("note") else ''}
        {f'<div class="stale">content changed since this preview was built - run <code>render --all</code></div>' if is_stale else ''}
      </a>""")

    body = "\n".join(rows) if rows else """
      <div class="empty">
        <b>Nothing on the shelf yet.</b>
        <p>This page only lists units added with <code>python3 tools/notes_workshop.py add &lt;CODE&gt; &lt;unit&gt;</code>.
        Older previews in <code>preview/</code> are deliberately not shown.</p>
      </div>"""

    overview = (
        '<div class="bar"><a href="maths.html"><b>Mathematics I and II overview</b></a>'
        ' - all 11 units, hours, marks and syllabus coverage in one table.</div>'
        if (SHELF / "maths.html").is_file() else ""
    )
    if (SHELF / "papers.html").is_file():
        overview += (
            '<div class="bar"><a href="papers.html"><b>Solved question papers</b></a>'
            ' - the four authored papers, 28 printed parts each, both languages.</div>'
        )

    page = f"""<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>DiplomaOne · notes workshop</title>
<style>
 :root{{--p:#7B2CD9;--pd:#5B1BB0;--lav:#EADDF7;--bg:#F3ECFA;--ink:#1d1b20;--muted:#6b6478}}
 *{{box-sizing:border-box}}
 body{{margin:0;background:var(--bg);color:var(--ink);font:15px/1.55 system-ui,-apple-system,"Segoe UI",Roboto,sans-serif}}
 header{{background:var(--p);color:#fff;padding:22px 18px 18px}}
 header .wrap{{max-width:760px;margin:0 auto}}
 header h1{{margin:0 0 4px;font-size:21px;letter-spacing:.2px}}
 header p{{margin:0;opacity:.9;font-size:13.5px}}
 main{{max-width:760px;margin:0 auto;padding:16px 14px 40px}}
 .bar{{display:flex;gap:8px;flex-wrap:wrap;align-items:center;margin:0 2px 14px;color:var(--muted);font-size:13px}}
 .bar b{{color:var(--pd)}}
 .card{{display:block;background:#fff;border-radius:12px;padding:14px 15px;margin:0 0 12px;text-decoration:none;color:inherit;
   box-shadow:0 1px 3px rgba(60,20,110,.14);border:1px solid #eadcf9}}
 .card:hover{{border-color:var(--p);box-shadow:0 4px 14px rgba(60,20,110,.18)}}
 .row{{display:flex;gap:12px;align-items:flex-start;justify-content:space-between}}
 .code{{font:700 11.5px/1 ui-monospace,monospace;color:var(--p);letter-spacing:.4px;text-transform:uppercase}}
 h2{{margin:5px 0 4px;font-size:17px;line-height:1.3}}
 .sub{{color:var(--muted);font-size:12.5px}}
 .go{{flex:none;color:var(--p);font-weight:700;font-size:13.5px;padding-top:14px}}
 .chips{{margin-top:10px;display:flex;gap:6px;flex-wrap:wrap}}
 .chip{{background:#F5EEFD;color:var(--pd);border-radius:999px;padding:3px 9px;font-size:11.5px;font-weight:700}}
 .note{{margin-top:9px;font-size:12.5px;color:#4a4458;background:#faf7fe;border-left:3px solid var(--lav);padding:6px 9px;border-radius:4px}}
 .stale{{margin-top:9px;font-size:12.5px;color:#8a4b00;background:#fff6e5;border-left:3px solid #E07B00;padding:6px 9px;border-radius:4px}}
 .empty{{background:#fff;border:1px dashed #c9b6e6;border-radius:12px;padding:22px;text-align:center;color:var(--muted)}}
 .empty b{{color:var(--pd);display:block;margin-bottom:6px;font-size:16px}}
 .tips{{margin-top:22px;background:#fff;border-radius:12px;padding:14px 16px;border:1px solid #eadcf9}}
 .tips h3{{margin:0 0 8px;font-size:14px;color:var(--pd);text-transform:uppercase;letter-spacing:.5px}}
 .tips ul{{margin:0;padding-left:20px;color:#3d3950;font-size:13.5px}}
 .tips li{{margin-bottom:5px}}
 code{{background:#F1E9FB;color:var(--pd);border-radius:4px;padding:1px 5px;font-size:12.5px}}
 footer{{max-width:760px;margin:0 auto;padding:0 14px 30px;color:var(--muted);font-size:12px}}
</style></head>
<body>
<header><div class="wrap">
  <h1>Notes workshop</h1>
  <p>Only the units authored in this session are listed — {len(data['units'])} on the shelf{' · ' + str(stale) + ' stale' if stale else ''}.</p>
</div></header>
<main>
  <div class="bar"><b>How to review:</b> open a unit → tap any card to expand → check diagrams (tap to zoom) → spot-check numbers and tables.</div>
  {overview}
  {body}
  <div class="tips">
    <h3>What to look for</h3>
    <ul>
      <li><b>Coverage:</b> every syllabus line of the unit has its own card.</li>
      <li><b>Depth:</b> definitions are one clear sentence; explanations add the “why”, not just labels.</li>
      <li><b>Numericals:</b> Given → Formula → Steps → <i>bold answer with unit</i> → check line.</li>
      <li><b>Derivations:</b> symbols defined, assumptions stated, ≤6 ordered steps, final relation + validity.</li>
      <li><b>Diagrams:</b> no clipped label, arrows not crossing text, one idea per diagram (tap to zoom).</li>
      <li><b>Language:</b> English-only units must have no Gujarati text.</li>
      <li><b>Exam practice:</b> marks are <i>suggested</i> (3/4/7) and every question is answered in the last notes section.</li>
    </ul>
  </div>
</main>
<footer>Generated by <code>tools/notes_workshop.py</code> · this page is not part of the published app.</footer>
</body></html>
"""
    (SHELF / "index.html").write_text(page, encoding="utf-8")


# --------------------------------------------------------------------- audits
FORBIDDEN_SVG = ["<script", "<style", "<marker", "<foreignObject", "<image", "href="]


def audit_svg(path, problems):
    raw = Path(path).read_text(encoding="utf-8")
    for bad in FORBIDDEN_SVG:
        if bad in raw:
            problems.append(f"{path.name}: forbidden {bad}")
    try:
        root = ET.fromstring(raw)
    except ET.ParseError as e:
        problems.append(f"{path.name}: not valid XML ({e})")
        return
    vb = (root.get("viewBox") or "").split()
    if len(vb) != 4:
        problems.append(f"{path.name}: missing viewBox")
        return
    w, h = float(vb[2]), float(vb[3])
    if abs(w - 360) > 0.01:
        problems.append(f"{path.name}: width {w:g} != 360")
    for node in root.iter(SVG_NS + "text"):
        size = float(node.get("font-size", "12"))
        bold = (node.get("font-weight") or "normal") in ("bold", "700", "800")
        pieces = [node] if len(node) == 0 else list(node)
        for piece in pieces:
            txt = "".join(piece.itertext())
            if not txt:
                continue
            x = float(piece.get("x", node.get("x", "0")))
            y = float(piece.get("y", node.get("y", "0")))
            anchor = piece.get("text-anchor", node.get("text-anchor", "start"))
            width = text_width(txt, size, bold)
            left = x - width / 2 if anchor == "middle" else (x - width if anchor == "end" else x)
            if left < 1:
                problems.append(f"{path.name}: '{txt}' starts at {left:.1f}px (left edge)")
            if left + width > w - 1:
                problems.append(f"{path.name}: '{txt}' ends at {left + width:.1f}px (right edge)")
            if y - size < -1 or y + size / 3 > h + 1:
                problems.append(f"{path.name}: '{txt}' y={y:g} outside 0..{h:g}")


def audit_unit(code, number):
    d, unit, subject, src = load_unit(code, number)
    problems, notes = [], []
    listed = {x["id"] for x in unit.get("diagrams") or []}
    referenced, programs_used, examples_used = set(), set(), set()
    for sec in unit.get("notes") or []:
        for it in sec.get("items") or []:
            if it.get("diagram"):
                referenced.add(it["diagram"])
            programs_used.update(it.get("programs") or [])
            examples_used.update(it.get("examples") or [])
            if it.get("h") and not it.get("body"):
                problems.append(f"card '{it['h'].get('en')}' has no body")
            if it.get("q") and not it.get("a"):
                problems.append("question card without answer")
            body = (it.get("body") or {}).get("en", "")
            for tag in ("<script", "<style", "<img"):
                if tag in body:
                    problems.append(f"card '{it.get('h', {}).get('en', '')[:40]}' contains {tag}")
            for url in re.findall(r'href="([^"]+)"', body):
                if not url.startswith(("https://", "http://")):
                    problems.append(f"card links to a non-web target: {url[:60]}")
                else:
                    notes.append(f"card has an inline link ({url[:52]}…) - prefer the sources list")
    for missing in referenced - listed:
        problems.append(f"card references unknown diagram '{missing}'")
    for unused in listed - referenced:
        notes.append(f"diagram '{unused}' is listed but not used by any card")
    prog_ids = {p["id"] for p in unit.get("programs") or [] if "id" in p}
    for missing in programs_used - prog_ids:
        problems.append(f"card references unknown program '{missing}'")
    num_ids = {n["id"] for n in unit.get("numericals") or []}
    for missing in examples_used - num_ids:
        problems.append(f"card references unknown numerical '{missing}'")
    for dg in unit.get("diagrams") or []:
        p = d / "diagrams" / f"{dg['id']}.svg"
        if not p.is_file():
            problems.append(f"missing SVG file {p.name}")
        else:
            audit_svg(p, problems)
    known = {"notes", "programs", "diagrams", "flowcharts", "algorithms", "syntax",
             "equations", "numericals", "viva", "exam"}
    for tab in unit.get("tabs") or []:
        if tab not in known:
            problems.append(f"unknown tab '{tab}'")
    return problems, notes, stats_of(unit)


def cmd_check(args):
    data = shelf()
    targets = []
    if args.all or not args.code:
        targets = [(u["code"], u["unit"]) for u in data["units"]]
    else:
        targets = [(args.code, args.unit)]
    if not targets:
        print("shelf is empty - nothing to check")
        return 0
    bad = 0
    for code, number in targets:
        problems, notes, st = audit_unit(code, number)
        print(f"\n{code} unit {number}  ·  {st['sections']} sections / {st['cards']} cards / "
              f"{st['diagrams']} diagrams / {st['numericals']} numericals / {st['viva']} viva / {st['exam']} exam")
        for p in problems:
            print("  ERROR  ", p)
        for n in notes:
            print("  note   ", n)
        bad += len(problems)
    print(f"\n{'OK - no problems' if not bad else str(bad) + ' problem(s)'}")
    return 1 if bad else 0


# --------------------------------------------------------------------- commands
def cmd_add(args):
    out = render_one(args.code, args.unit, note=args.note, register=True)
    e = next(u for u in shelf()["units"] if u["code"] == args.code and u["unit"] == int(args.unit))
    st = e["stats"]
    print(f"shelf + {args.code} unit {args.unit} -> {out.relative_to(ROOT)}")
    print(f"  {st['sections']} sections / {st['cards']} cards / {st['diagrams']} diagrams / "
          f"{st['numericals']} numericals / {st['viva']} viva / {st['exam']} exam  ({st['kb']} KB)")
    print("  index: preview/workshop/index.html")
    return 0


def cmd_render(args):
    data = shelf()
    targets = [(u["code"], u["unit"]) for u in data["units"]] if (args.all or not args.code) else [(args.code, args.unit)]
    for code, number in targets:
        render_one(code, number, register=True)
        print("rendered", f"{code} unit {number}")
    write_index()
    return 0


def cmd_list(args):
    data = shelf()
    if not data["units"]:
        print("shelf is empty")
        return 0
    for u in data["units"]:
        src = next((p for p in CONTENT.glob(f"*/sem*/{u['code']}/unit{u['unit']}.json")), None)
        state = "stale" if (src and sha1(src) != u["source_sha1"]) else "fresh"
        s = u["stats"]
        print(f"{u['code']} u{u['unit']:<2} {state:<5} {s['sections']:>2} sec {s['cards']:>2} cards "
              f"{s['diagrams']:>2} dg {s['numericals']:>2} num {s['viva']:>2} viva {s['exam']:>2} exam  {u['title']}")
    return 0


def cmd_clear(args):
    data = shelf()
    if args.code:
        data["units"] = [u for u in data["units"] if u["code"] != args.code]
    else:
        for u in data["units"]:
            p = SHELF / u["file"]
            if p.exists():
                p.unlink()
        data["units"] = []
    save_shelf(data)
    write_index()
    print("shelf updated:", len(data["units"]), "unit(s) left")
    return 0


class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *a, root=False, **kw):
        self.root = root
        super().__init__(*a, directory=str(ROOT if root else SHELF), **kw)

    def end_headers(self):
        self.send_header("Cache-Control", "no-store, max-age=0")
        super().end_headers()

    def log_message(self, fmt, *args):
        sys.stderr.write("  %s\n" % (fmt % args))


class RootHandler(Handler):
    """Serves the repository root so papers.html can frame ../../papers-upload/..."""

    def __init__(self, *a, **kw):
        super().__init__(*a, root=True, **kw)

    def do_GET(self):
        shelf = SHELF.relative_to(ROOT).as_posix()
        if self.path in ("/", "/index.html") and (SHELF / "papers.html").is_file():
            target = "/%s/papers.html" % shelf          # solved papers first: that is what is reviewed
        elif self.path in ("/", "/index.html", "/workshop", "/workshop/"):
            target = "/%s/" % shelf
        else:
            target = None
        if target:
            self.send_response(302)
            self.send_header("Location", target)
            self.send_header("Content-Length", "0")
            self.end_headers()
            return
        super().do_GET()


def cmd_serve(args):
    write_index()
    port = args.port
    if args.root:
        handler = RootHandler
        where = "repository root (solved-paper gallery works)"
    else:
        handler = Handler
        where = f"serving {SHELF.relative_to(ROOT)}/"
    httpd = ThreadingHTTPServer(("0.0.0.0", port), handler)
    print(f"notes workshop on http://0.0.0.0:{port}/  ({where})")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nstopped")
    return 0


def main():
    ap = argparse.ArgumentParser(description="HTML previews for the units authored right now")
    sub = ap.add_subparsers(dest="cmd", required=True)

    a = sub.add_parser("add", help="render a unit preview and put it on the shelf")
    a.add_argument("code")
    a.add_argument("unit", type=int)
    a.add_argument("--note", default="", help="short reviewer note shown on the shelf")
    a.set_defaults(func=cmd_add)

    r = sub.add_parser("render", help="re-render shelved previews after content edits")
    r.add_argument("code", nargs="?")
    r.add_argument("unit", nargs="?", type=int)
    r.add_argument("--all", action="store_true")
    r.set_defaults(func=cmd_render)

    ls = sub.add_parser("list", help="show the shelf")
    ls.set_defaults(func=cmd_list)

    c = sub.add_parser("check", help="link + SVG text-bounds audit")
    c.add_argument("code", nargs="?")
    c.add_argument("unit", nargs="?", type=int)
    c.add_argument("--all", action="store_true")
    c.set_defaults(func=cmd_check)

    cl = sub.add_parser("clear", help="remove units from the shelf")
    cl.add_argument("code", nargs="?")
    cl.set_defaults(func=cmd_clear)

    s = sub.add_parser("serve", help="serve the workshop over HTTP")
    s.add_argument("--port", type=int, default=8800)
    s.add_argument("--root", action="store_true",
                   help="serve the repository root instead of preview/workshop/ (needed by papers.html)")
    s.set_defaults(func=cmd_serve)

    args = ap.parse_args()
    if args.cmd == "render" and args.unit is None and args.code:
        ap.error("render needs <CODE> <unit> or --all")
    sys.exit(args.func(args))


if __name__ == "__main__":
    main()
