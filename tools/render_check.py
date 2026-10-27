"""Dev helper: render SVGs to PNG (resvg) and tile them for visual checking. usage: render_check.py out.png a.svg b.svg ..."""
import sys, os, subprocess, resvg_py
out, files = sys.argv[1], sys.argv[2:]
pngs = []
for f in files:
    b = resvg_py.svg_to_bytes(svg_path=os.path.abspath(f), zoom=1.4, font_dirs=['/usr/share/fonts/truetype/dejavu'],
                              sans_serif_family='DejaVu Sans', font_family='DejaVu Sans', skip_system_fonts=True)
    p = '/tmp/png/' + os.path.basename(f)[:-4] + '.png'
    os.makedirs('/tmp/png', exist_ok=True)
    open(p, 'wb').write(bytes(b)); pngs.append(p)
subprocess.run(['convert', *pngs, '-background', 'white', '-gravity', 'north', '+append', out], check=True)
