"""Measure the labels of a diagram module: nothing may hang outside its canvas.

Diagram overflow is invisible to the build and to the JSON validator - a cut-off label only shows up
when somebody looks at the picture - so every figure goes through this checker before it is committed.

    python3 tools/check_diagrams.py diagrams_DI05005031_u1 u1
    python3 tools/check_diagrams.py diagrams_DI05005031_u1 u1 --png /tmp/figs

It prints one line per figure with the number of overflowing labels (0 is the only acceptable value)
and, with --png, writes a scaled PNG of each figure for a visual check.
"""
import argparse
import importlib
import re
import sys
from pathlib import Path
from xml.etree import ElementTree as ET

sys.path.insert(0, str(Path(__file__).resolve().parent))

from PIL import ImageFont  # noqa: E402

FONTS = {
    (False, False): "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
    (True, False): "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
    (False, True): "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf",
    (True, True): "/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf",
}
_cache = {}


def _font(size, weight, mono=False):
    key = (bool(weight == "bold"), mono)
    f = _cache.get(key)
    if f is None:
        f = ImageFont.truetype(FONTS[key], 200)
        _cache[key] = f
    return f, size / 200.0


def width(s, size, weight="normal", mono=False):
    f, k = _font(size, weight, mono)
    return f.getlength(s) * k


def check(svg_text, name):
    root = ET.fromstring(svg_text)
    vb = root.get("viewBox").split()
    w, h = float(vb[2]), float(vb[3])
    bad = []
    for el in root.iter("{http://www.w3.org/2000/svg}text"):
        s = el.text or ""
        if not s.strip():
            continue
        x = float(el.get("x", 0))
        y = float(el.get("y", 0))
        size = float(el.get("font-size", 12))
        anchor = el.get("text-anchor", "start")
        mono = bool(re.search(r"mono", el.get("font-family", "") or ""))
        tw = width(s, size, el.get("font-weight", "normal"), mono)
        x0 = x if anchor == "start" else (x - tw / 2 if anchor == "middle" else x - tw)
        x1 = x0 + tw
        top, bottom = y - size * 0.78, y + size * 0.24
        if x0 < -0.5 or x1 > w + 0.5 or top < -0.5 or bottom > h + 0.5:
            bad.append(f"    '{s[:52]}' x=[{x0:.0f},{x1:.0f}] y=[{top:.0f},{bottom:.0f}] "
                       f"canvas {w:.0f}x{h:.0f}")
    return bad, (w, h)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("module")
    ap.add_argument("prefix", nargs="?", default="")
    ap.add_argument("--png", default=None)
    args = ap.parse_args()
    mod = importlib.import_module(args.module)
    total = 0
    for key, fn in mod.DIAGRAMS.items():
        svg_text = fn()
        if not args.prefix or not key.startswith(args.prefix):
            continue
        bad, size = check(svg_text, key)
        total += len(bad)
        flag = "OK  " if not bad else "FAIL"
        print(f"{flag} {key:14s} {size[0]:.0f}x{size[1]:.0f}  labels outside: {len(bad)}")
        for line in bad:
            print(line)
        if args.png:
            import resvg_py
            # resvg in this sandbox has no Arial: render the PNG with DejaVu so the preview shows the
            # same picture a browser shows. The SVG itself keeps the browser-safe font stack.
            preview = svg_text.replace("Arial, Helvetica, sans-serif", "DejaVu Sans")
            out = Path(args.png)
            out.mkdir(parents=True, exist_ok=True)
            png = resvg_py.svg_to_bytes(svg_string=preview, zoom=2.0,
                                        font_dirs=["/usr/share/fonts"])
            (out / f"{key}.png").write_bytes(bytes(png))
    print("overflow:", total)
    return 1 if total else 0


if __name__ == "__main__":
    raise SystemExit(main())
