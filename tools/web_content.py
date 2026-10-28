"""Content helpers for DI03000061 Responsive Web Page Design (HTML / Bootstrap 5 / jQuery programs, live preview in the app).

page(title, body, ...)  -> full HTML document (local Bootstrap files, as installed in practical 1)
WE(id, title, code, out, expl) -> program dict with "run": "html"
make_TS(snips) -> T(h, body, diagram=, programs=) with @@name@@ code snippets
"""
import html
import re

from sql_content import VE, XE, G  # noqa: F401  (re-exported)

MAXW = 56


def _check(id_, code):
    for ln in code.split("\n"):
        assert len(ln) <= MAXW or "://" in ln, f"{id_}: line too long ({len(ln)}): {ln}"
    assert "\t" not in code, id_


def _indent(s, n):
    s = s.strip("\n")
    return "\n".join((" " * n + ln) if ln.strip() else "" for ln in s.split("\n"))


def page(title, body, style="", script="", jquery=False, bs_js=False, icons=False, head="", bs=True, viewport=True):
    h = ["<!DOCTYPE html>", '<html lang="en">', "<head>", '  <meta charset="UTF-8">']
    if viewport:
        h += ['  <meta name="viewport"', '    content="width=device-width, initial-scale=1">']
    h.append(f"  <title>{title}</title>")
    if bs:
        h.append('  <link rel="stylesheet" href="css/bootstrap.min.css">')
    if icons:
        h += ['  <link rel="stylesheet"', '    href="css/bootstrap-icons.min.css">']
    if head:
        h.append(_indent(head, 2))
    if style:
        h += ["  <style>", _indent(style, 4), "  </style>"]
    h += ["</head>", "<body>", _indent(body, 2)]
    if jquery:
        h.append('  <script src="js/jquery-3.7.1.min.js"></script>')
    if bs_js:
        h.append('  <script src="js/bootstrap.bundle.min.js"></script>')
    if script:
        h += ["  <script>", _indent(script, 4), "  </script>"]
    h += ["</body>", "</html>"]
    return "\n".join(h)


def WE(id_, title, code, out, expl="", actions=None):
    code = code.strip("\n")
    _check(id_, code)
    assert "<" not in title, id_
    d = {"id": id_, "title": {"en": title}, "code": {"en": code}, "out": out.strip(), "expl": {"en": expl.strip()},
         "run": "html"}
    if actions:
        d["_actions"] = actions  # used only by the local render check, removed before writing
    return d


def code_pre(code):
    code = code.strip("\n")
    _check("snippet", code)
    return '<pre class="c">' + html.escape(code, quote=False) + "</pre>"


def make_TS(snips):
    def T(h, b, diagram=None, programs=None):
        body = re.sub(r"@@(\w+)@@", lambda m: code_pre(snips[m.group(1)]), b)
        d = {"h": {"en": h}, "body": {"en": body}}
        if diagram:
            d["diagram"] = diagram
        if programs:
            d["programs"] = programs
        return d
    return T


def SXE(name, f, terms=""):
    f = f.strip("\n")
    _check("syntax", f)
    return {"name": {"en": name}, "f": f, "terms": {"en": terms}}
