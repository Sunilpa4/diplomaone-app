"""Mirror of app/lib/widgets/web_preview.dart: builds the offline preview page and renders it with headless
Chromium (playwright) to check HTML/Bootstrap programs: screenshots at phone/desktop width + JS errors.

  shots(code, "/home/user/chk/q1", widths=(390, 1100)) -> {"errors": [...], "files": [...], "height": {...}}
"""
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
ASSETS = os.path.join(HERE, "..", "app", "assets", "web")

RE_ICONS = re.compile(r'''<link\b[^>]*href\s*=\s*["'][^"']*bootstrap-icons[^"']*\.css[^"']*["'][^>]*>''', re.I)
RE_BS_CSS = re.compile(r'''<link\b[^>]*href\s*=\s*["'][^"']*/bootstrap(?:\.min)?\.css[^"']*["'][^>]*>''', re.I)
RE_BS_JS = re.compile(r'''<script\b[^>]*src\s*=\s*["'][^"']*/bootstrap(?:\.bundle)?(?:\.min)?\.js[^"']*["'][^>]*>\s*</script>''', re.I)
RE_JQ = re.compile(r'''<script\b[^>]*src\s*=\s*["'][^"']*/jquery[^"'/]*\.js[^"']*["'][^>]*>\s*</script>''', re.I)
RE_HEAD = re.compile(r"<head\b[^>]*>", re.I)
RE_VP = re.compile(r"width\s*=\s*device-width", re.I)

_A = {}


def assets():
    if not _A:
        for n in ("bootstrap.min.css", "bootstrap.bundle.min.js", "jquery.min.js", "bootstrap-icons.min.css", "shell.js"):
            _A[n] = open(os.path.join(ASSETS, n), encoding="utf-8").read()
    return _A


def build_preview(code, desktop=False):
    a = assets()
    h = code
    h = RE_ICONS.sub(lambda m: "<style>" + a["bootstrap-icons.min.css"] + "</style>", h)
    h = RE_BS_CSS.sub(lambda m: "<style>" + a["bootstrap.min.css"] + "</style>", h)
    h = RE_JQ.sub(lambda m: "<script>" + a["jquery.min.js"] + "</script>", h)
    h = RE_BS_JS.sub(lambda m: "<script>" + a["bootstrap.bundle.min.js"] + "</script>", h)
    if desktop:
        h = RE_VP.sub("width=1100", h, count=1)
    shell = "<script>" + a["shell.js"] + "</script>"
    m = RE_HEAD.search(h)
    return h[:m.end()] + shell + h[m.end():] if m else shell + h


def shots(code, prefix, widths=(390, 1100), actions=None, full=True, max_h=2400):
    """Render code at each width. actions: optional JS run after load (e.g. open a modal), then 700 ms wait."""
    from playwright.sync_api import sync_playwright
    res = {"errors": [], "files": [], "height": {}}
    html = build_preview(code)
    with sync_playwright() as p:
        b = p.chromium.launch()
        for w in widths:
            pg = b.new_page(viewport={"width": w, "height": 760}, device_scale_factor=1)
            pg.on("pageerror", lambda e: res["errors"].append(str(e)))
            pg.on("console", lambda m: res["errors"].append("console: " + m.text) if m.type == "error" else None)
            pg.set_content(html, wait_until="load")
            pg.wait_for_timeout(400)
            if actions:
                pg.evaluate(actions)
                pg.wait_for_timeout(700)
            h = pg.evaluate("document.documentElement.scrollHeight")
            res["height"][w] = h
            f = f"{prefix}_{w}.png"
            pg.screenshot(path=f, full_page=False, clip={"x": 0, "y": 0, "width": w, "height": min(h, max_h)} if full else None)
            res["files"].append(f)
            pg.close()
        b.close()
    return res
