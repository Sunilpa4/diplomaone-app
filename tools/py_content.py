"""Content helpers for Python (Scripting Language) subjects – English only.

Note bodies use @@name@@ for code snippets from the dict passed to make_TP().
"""
import html, os, re, sys
from py_runner import run
from c_content import SXE, VE, XE, G  # language-neutral helpers

MAXW = 44
_TRAIL = re.compile(r"^(\s*)(\S.*?)\s+(#.*)$")


def reflow(code, maxw=MAXW):
    """Lines wider than maxw with a trailing # comment: move the comment onto its own line above."""
    out = []
    for ln in code.split("\n"):
        m = _TRAIL.match(ln)
        if m and len(ln) > maxw and m.group(2).count('"') % 2 == 0 and m.group(2).count("'") % 2 == 0:
            out += [m.group(1) + m.group(3), m.group(1) + m.group(2).rstrip()]
        else:
            out.append(ln)
    return "\n".join(out)


def code_block(code):
    return '<pre class="c">' + html.escape(reflow(code.strip("\n")), quote=False) + "</pre>"


def make_TP(snips):
    """T(heading, body_html, diagram=None, programs=None, key=False)"""
    def T(h, b, diagram=None, programs=None, key=False):
        body = re.sub(r"@@(\w+)@@", lambda m: code_block(snips[m.group(1)]), b)
        d = {"h": {"en": h}, "body": {"en": body}}
        if diagram:
            d["diagram"] = diagram
        if programs:
            d["programs"] = programs
        if key:
            d["key"] = True
        return d
    return T


def PP(id_, title, code, inputs=(), expl="", args=(), files=None, expect_error=False, show_files=(), cmd=None, extra=None,
       plot=None, show_extra=True, main_name="main.py"):
    """A solved Python program with genuine output.
    show_files: names of files written by the program whose contents are appended to the output.
    cmd: command line shown at the top of the output (for sys.argv programs)."""
    code = code.strip("\n") + "\n"
    r = run(code, inputs, args, files, expect_error, extra=extra)
    out = r["out"]
    for n in show_files:
        out += f"\n\n--- {n} (created by the program) ---\n" + r["files"][n].rstrip("\n")
    if cmd:
        out = "$ " + cmd + "\n" + out
    shown = code
    if extra and show_extra:  # show module / package files above the main program
        parts = [f"# ===== File: {n} =====\n" + c.strip("\n") + "\n" for n, c in extra.items()]
        shown = "\n".join(parts) + f"\n# ===== File: {main_name} =====\n" + code
    d = {"id": id_, "title": {"en": title}, "code": {"en": reflow(shown).rstrip("\n")}, "out": out, "expl": {"en": expl}}
    if plot:
        render_plot(code, os.path.join(PLOT_DIR, plot + ".svg"))
        d["plot"] = plot
    return d


PLOT_DIR = None   # set by the unit's programs module


_PLOT_WRAP = r'''
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"svg.fonttype": "none", "svg.hashsalt": "gtu", "font.family": "DejaVu Sans", "figure.dpi": 72})
_OUT = __OUT__
def _show(*a, **k):
    plt.gcf().savefig(_OUT, format="svg", metadata={"Date": None, "Creator": None}, bbox_inches="tight")
    plt.close("all")
plt.show = _show
'''


def render_plot(code, out_svg):
    """Run a Matplotlib program with plt.show() replaced by saving the current figure as SVG (the real plot window)."""
    import subprocess, tempfile, re as _re
    with tempfile.TemporaryDirectory() as d:
        src = os.path.join(d, "plotprog.py")
        with open(src, "w", encoding="utf-8") as f:
            f.write(_PLOT_WRAP.replace("__OUT__", repr(out_svg)) + "\n" + code)
        subprocess.run([sys.executable, src], cwd=d, check=True, capture_output=True, timeout=120,
                       env=dict(os.environ, MPLBACKEND="Agg", PYTHONHASHSEED="0"))
    t = open(out_svg, encoding="utf-8").read()
    t = _re.sub(r"<\?xml[^>]*>\s*", "", t)
    t = _re.sub(r"<!DOCTYPE[^>]*>\s*", "", t)
    t = _re.sub(r"<metadata>.*?</metadata>\s*", "", t, flags=_re.S)
    t = _re.sub(r"<!--.*?-->", "", t, flags=_re.S)
    t = _re.sub(r'(width|height)="([\d.]+)pt"', lambda m: f'{m.group(1)}="{float(m.group(2)):.1f}"', t, count=2)
    pre = os.path.splitext(os.path.basename(out_svg))[0] + "_"   # unique ids when several SVGs share one page
    t = _re.sub(r'id="([^"]+)"', lambda m: f'id="{pre}{m.group(1)}"', t)
    t = _re.sub(r'url\(#([^)]+)\)', lambda m: f'url(#{pre}{m.group(1)})', t)
    t = _re.sub(r'href="#([^"]+)"', lambda m: f'href="#{pre}{m.group(1)}"', t)
    with open(out_svg, "w", encoding="utf-8") as f:
        f.write(t)


__all__ = ["make_TP", "PP", "SXE", "VE", "XE", "G", "reflow", "code_block"]
