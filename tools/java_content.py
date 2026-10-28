"""Content helpers for Java (DI04000021) - English only.

Programs are REALLY compiled and run with the sandbox JDK (javac/java), so outputs are genuine.
Every source defines a class named Main (file Main.java). Note bodies use @@name@@ for code snippets.
"""
import html, os, re, subprocess, sys, tempfile
from c_content import SXE, VE, XE, G  # language-neutral helpers

MAXW = 44
_TRAIL = re.compile(r"^(\s*)(\S.*?)\s+(//.*)$")


def reflow(code, maxw=MAXW):
    """Lines wider than maxw with a trailing // comment: move the comment onto its own line above."""
    out = []
    for ln in code.split("\n"):
        m = _TRAIL.match(ln)
        if m and len(ln) > maxw and m.group(2).count('"') % 2 == 0:
            out += [m.group(1) + m.group(3), m.group(1) + m.group(2).rstrip()]
        else:
            out.append(ln)
    return "\n".join(out)


def code_block(code):
    return '<pre class="c">' + html.escape(reflow(code.strip("\n")), quote=False) + "</pre>"


def make_TJ(snips):
    """T(heading, body_html, diagram=None, programs=None, key=False)"""
    def T(h, b, diagram=None, programs=None):
        body = re.sub(r"@@(\w+)@@", lambda m: code_block(snips[m.group(1)]), b)
        d = {"h": {"en": h}, "body": {"en": body}}
        if diagram:
            d["diagram"] = diagram
        if programs:
            d["programs"] = programs
        return d
    return T


def run_java(code, inputs=(), args=(), extra=None):
    """Compile and run a Java program. extra: {filename: source} additional classes (e.g. packages demo)."""
    with tempfile.TemporaryDirectory() as d:
        files = dict(extra or {})
        files["Main.java"] = code
        for name, src in files.items():
            path = os.path.join(d, name)
            os.makedirs(os.path.dirname(path), exist_ok=True) if os.path.dirname(name) else None
            with open(path, "w", encoding="utf-8") as f:
                f.write(src.strip("\n") + "\n")
        try:
            subprocess.run(["javac"] + list(files), cwd=d, check=True, capture_output=True, text=True, timeout=60)
        except subprocess.CalledProcessError as e:
            return "$ javac Main.java\n" + (e.stderr or "").strip() + "\n<compile error - fix the program>\n"
        cp = subprocess.run(["java", "-cp", d, "Main", *args], input="\n".join(inputs) + ("\n" if inputs else ""),
                            capture_output=True, text=True, timeout=60)
        out = cp.stdout
        if cp.returncode != 0:
            out += ("\n" if out and not out.endswith("\n") else "") + cp.stderr
        head = "$ javac Main.java\n$ java Main" + ((" " + " ".join(args)) if args else "") + "\n"
        return head + out.rstrip("\n")


def JP(id_, title, code, inputs=(), expl="", args=(), extra=None, show_extra=False, run=True):
    """A solved Java program with genuine output from the JDK.
    extra: additional .java files {path: source}; show_extra=True lists them above Main.java in the shown code."""
    code = code.strip("\n") + "\n"
    assert 'class Main' in code, id_ + ": must define class Main"
    out = run_java(code, inputs, args, extra) if run else ""
    shown = code
    if extra and show_extra:
        parts = [f"// ===== File: {n} =====\n" + c.strip("\n") + "\n" for n, c in extra.items()]
        shown = "\n".join(parts) + f"\n// ===== File: Main.java =====\n" + code
    def _too_long(s):
        return [ln for ln in reflow(s).split("\n") if len(ln) > MAXW]
    bad = _too_long(shown)
    assert not bad, f"{id_}: lines over {MAXW}\n" + "\n".join(bad)
    return {"id": id_, "title": {"en": title}, "code": {"en": reflow(shown).rstrip("\n")}, "out": out,
            "expl": {"en": expl}}


__all__ = ["make_TJ", "JP", "SXE", "VE", "XE", "G", "reflow", "code_block", "MAXW"]
