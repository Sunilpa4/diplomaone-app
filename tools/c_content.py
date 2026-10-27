"""Content helpers for C-programming subjects.

Code is written ONCE. Bilingual comments use ' || ' inside a comment:
    printf("Hi");   // print message || સંદેશ છાપો
    /* English part || ગુજરાતી ભાગ */
EN mode keeps the left part, GU mode the right part. Code outside comments is never touched.

In note bodies, a code block is written as  @@name@@  where name is a key in the snippet dict given to make_T().
"""
import html, re
from c_runner import run

_LINE = re.compile(r"//(\s*)(.*?)\s\|\|\s(.*)$", re.M)
_BLOCK = re.compile(r"/\*(\s*)(.*?)\s\|\|\s(.*?)(\s*)\*/", re.S)


MAXW = 44   # characters that fit a phone screen in the code view
_TRAIL = re.compile(r"^(\s*)(\S.*?)\s+(//.*|/\*.*?\*/)\s*$")


def reflow(code, maxw=MAXW):
    """Lines wider than maxw with a trailing comment: move the comment onto its own line above (same indent)."""
    out = []
    for ln in code.split("\n"):
        m = _TRAIL.match(ln)
        if m and len(ln) > maxw and m.group(2).count('"') % 2 == 0:
            out += [m.group(1) + m.group(3), m.group(1) + m.group(2).rstrip()]
        else:
            out.append(ln)
    return "\n".join(out)


def split(code, lang):
    k = 2 if lang == "en" else 3
    code = _LINE.sub(lambda m: "//" + m.group(1) + m.group(k).rstrip(), code)
    code = _BLOCK.sub(lambda m: "/*" + m.group(1) + m.group(k) + m.group(4) + "*/", code)
    return reflow(code)


def code_block(code, lang):
    return '<pre class="c">' + html.escape(split(code.strip("\n"), lang), quote=False) + "</pre>"


def make_T(snips):
    def expand(body, lang):
        return re.sub(r"@@(\w+)@@", lambda m: code_block(snips[m.group(1)], lang), body)

    def T(h_en, h_gu, b_en, b_gu, diagram=None, programs=None, key=False):
        d = {"h": {"en": h_en, "gu": h_gu}, "body": {"en": expand(b_en, "en"), "gu": expand(b_gu, "gu")}}
        if diagram:
            d["diagram"] = diagram
        if programs:
            d["programs"] = programs
        if key:
            d["key"] = True
        return d
    return T


def P(id_, title_en, title_gu, code, inputs=(), expl_en="", expl_gu="", args=(), files=None):
    code = code.strip("\n") + "\n"
    r = run(split(code, "en"), inputs, args, files)
    if r["warn"]:
        print(f"[warn] {id_}:\n{r['warn']}\n")
    return {"id": id_, "title": {"en": title_en, "gu": title_gu},
            "code": {"en": split(code, "en").rstrip("\n"), "gu": split(code, "gu").rstrip("\n")},
            "out": r["out"], "expl": {"en": expl_en, "gu": expl_gu}}


def SX(name_en, name_gu, f, terms_en="", terms_gu=""):
    return {"name": {"en": name_en, "gu": name_gu}, "f": f.strip("\n"), "terms": {"en": terms_en, "gu": terms_gu}}



# ---------------- English-only helpers (subjects with languages = ["en"]) ----------------
def make_TE(snips):
    """T(heading, body_html, diagram=None, programs=None, key=False) – English only."""
    def T(h, b, diagram=None, programs=None, key=False):
        body = re.sub(r"@@(\w+)@@", lambda m: code_block(snips[m.group(1)], "en"), b)
        d = {"h": {"en": h}, "body": {"en": body}}
        if diagram:
            d["diagram"] = diagram
        if programs:
            d["programs"] = programs
        if key:
            d["key"] = True
        return d
    return T


def PE(id_, title, code, inputs=(), expl="", args=(), files=None):
    code = code.strip("\n") + "\n"
    r = run(code, inputs, args, files)
    if r["warn"]:
        print(f"[warn] {id_}:\n{r['warn']}\n")
    return {"id": id_, "title": {"en": title}, "code": {"en": reflow(code).rstrip("\n")}, "out": r["out"], "expl": {"en": expl}}


def SXE(name, f, terms=""):
    return {"name": {"en": name}, "f": f.strip("\n"), "terms": {"en": terms}}


def VE(q, a):
    return {"q": {"en": q}, "a": {"en": a}}


def XE(q, marks):
    return {"q": {"en": q}, "marks": marks}


def G(title, items):
    return {"title": {"en": title}, "items": items}


if __name__ == "__main__":
    c = 'int a = 5;   // value || મૂલ્ય\nif (a || b) x = 1; /* check || ચકાસો */'
    print(split(c, "en")); print(split(c, "gu"))
