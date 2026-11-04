"""Render one or more SVGs into a single contact-sheet PNG for visual checking.

    python3 tools/render_sheet.py out.png a.svg b.svg ...     (needs resvg-py + pillow)

Used during authoring only; it is not part of the content pipeline.
"""
import sys

import resvg_py
from PIL import Image

FONTS = ["/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
         "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"]


def render(svg_paths, out_png, gap=14):
    imgs = []
    for p in svg_paths:
        png = bytes(resvg_py.svg_to_bytes(svg_path=p, font_files=FONTS,
                                          font_family="DejaVu Sans",
                                          sans_serif_family="DejaVu Sans",
                                          serif_family="DejaVu Serif"))
        tmp = f"/tmp/_sheet_{len(imgs)}.png"
        with open(tmp, "wb") as f:
            f.write(png)
        imgs.append(Image.open(tmp))
    w = max(i.width for i in imgs)
    h = sum(i.height + gap for i in imgs)
    sheet = Image.new("RGB", (w, h), "#dddddd")
    y = 0
    for i in imgs:
        sheet.paste(i, (0, y))
        y += i.height + gap
    sheet.save(out_png)
    return out_png, sheet.size


if __name__ == "__main__":
    print(render(sys.argv[2:], sys.argv[1]))
