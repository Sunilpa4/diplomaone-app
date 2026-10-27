"""Content helpers for the RDBMS subject (English only, Oracle SQL).

QE(id, title, code, expl, setup=..., sim=None)
  - setup: SQL that is run silently first (e.g. the sample tables from sql_seed); it is not shown.
  - code : the Oracle SQL shown to students. Its output is produced by sql_runner (real SQLite execution).
  - sim  : optional alternative SQL that runs instead of `code` when the Oracle syntax can't be simulated
           (e.g. date arithmetic). It must produce the same result.
  - out  : optional fixed output (used for PL/SQL, where the output is computed by a Python mirror).
Notes use make_TE from c_content; `@@name@@` code blocks render as plain <pre>.
"""
import html
import re
from sql_runner import run_sql
from sql_seed import ALL

MAXW = 43


def _check(id_, code):
    for ln in code.split("\n"):
        assert len(ln) <= MAXW, f"{id_}: line too long ({len(ln)}): {ln}"


def QE(id_, title, code, expl="", setup=ALL, sim=None, out=None, rewrite=()):
    code = code.strip("\n")
    _check(id_, code)
    if out is None:
        out, _ = run_sql(sim if sim else code, setup, rewrite)
        for old, _new in rewrite:
            assert old in code, f"{id_}: rewrite text not found: {old}"
    assert "ORA-00900" not in out and "unsupported" not in out, f"{id_}: simulator problem\n{out}"
    return {"id": id_, "title": {"en": title}, "code": {"en": code}, "out": out.rstrip("\n"), "expl": {"en": expl}}


def sql_pre(code):
    code = code.strip("\n")
    _check("snippet", code)
    return '<pre class="c">' + html.escape(code, quote=False) + "</pre>"


def make_TS(snips):
    """T(heading, body_html, diagram=None, programs=None) – English only; @@name@@ → SQL block."""
    def T(h, b, diagram=None, programs=None):
        body = re.sub(r"@@(\w+)@@", lambda m: sql_pre(snips[m.group(1)]), b)
        d = {"h": {"en": h}, "body": {"en": body}}
        if diagram:
            d["diagram"] = diagram
        if programs:
            d["programs"] = programs
        return d
    return T


def result(sql, setup=ALL):
    """Output text of a query, for showing a result table inside notes."""
    return run_sql(sql, setup)[0]


def out_pre(sql, setup=ALL):
    """A <pre> with the SQL followed by its real output (for notes)."""
    return sql_pre(sql + "\n\n" + result(sql, setup))


def SXE(name, f, terms=""):
    return {"name": {"en": name}, "f": f.strip("\n"), "terms": {"en": terms}}


def VE(q, a):
    return {"q": {"en": q}, "a": {"en": a}}


def XE(q, marks):
    return {"q": {"en": q}, "marks": marks}


def G(title, items):
    return {"title": {"en": title}, "items": items}
