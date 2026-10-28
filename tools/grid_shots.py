"""python3 grid_shots.py out.png id1 id2 id3 -> side by side 390 + 1100 screenshots per id (rows)."""
import sys
from PIL import Image
out, ids = sys.argv[1], sys.argv[2:]
rows = []
for i in ids:
    a = Image.open(f"/home/user/chk/{i}_390.png").convert("RGB"); a = a.crop((0, 0, 390, min(a.height, 760)))
    b = Image.open(f"/home/user/chk/{i}_1100.png").convert("RGB"); b = b.crop((0, 0, 1100, min(b.height, 760)))
    r = Image.new("RGB", (1500, 760), "#888"); r.paste(a, (0, 0)); r.paste(b, (400, 0)); rows.append(r)
g = Image.new("RGB", (1500, 770 * len(rows)), "#444")
for k, r in enumerate(rows):
    g.paste(r, (0, k * 770))
g.thumbnail((1400, 1400))
g.save(out)
