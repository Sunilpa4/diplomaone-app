"""DiplomaOne notes template — the card vocabulary from `Mass-Transfer-I-complete.html`,
expressed as Python builders so every new unit comes out identical.

Design rules (see CONTENT-DESIGN.md):
  * every teaching card has a fixed heading skeleton (EN + GU);
  * numbers are always in the order Given -> Find -> Formula -> Substitution ->
    Final answer with units -> Validity check;
  * equipment cards always carry Definition -> Principle -> Construction -> Working ->
    Applications -> Limitations and precautions;
  * practical cards never invent readings — a blank observation sheet is emitted;
  * equations are stored as LaTeX text (`tex`), not rasterised images.

Usage:
    from d1notes import *
    unit = Unit("DI02005011", 1, bi("Units and Dimensions", "એકમો તથા પરિમાણો"),
                hours=9, weightage=20,
                tabs=["notes", "diagrams", "syntax", "viva", "exam"])
    unit.section(bi("Dimensions", "પરિમાણો"), [
        theory("1.2", bi("Dimensions", "પરિમાણો"),
               definition=bi("...", "..."), theory=bi("...", "..."), diagram="d1_tree"),
    ])
    unit.write("content/chemical/sem2/DI02005011/unit1.json")
    problems = unit.validate()
"""
from __future__ import annotations

import json
import os
import re

# ----------------------------------------------------------------- heading vocabulary
H = {
    "definition":       {"en": "Definition / principle",              "gu": "વ્યાખ્યા / સિદ્ધાંત"},
    "theory":           {"en": "Detailed theory and conditions",      "gu": "વિગતવાર Theory તથા Conditions"},
    "equations":        {"en": "Equations and notation",              "gu": "સમીકરણો તથા Notation"},
    "definition_equip": {"en": "Definition",                          "gu": "વ્યાખ્યા"},
    "principle_equip":  {"en": "Principle",                           "gu": "સિદ્ધાંત"},
    "construction":     {"en": "Construction",                        "gu": "રચના (Construction)"},
    "working":          {"en": "Working",                             "gu": "કાર્યપદ્ધતિ (Working)"},
    "applications":     {"en": "Applications",                        "gu": "ઉપયોગો"},
    "limitations":      {"en": "Limitations and precautions",         "gu": "Limitations તથા Precautions"},
    "symbols":          {"en": "Symbols, model and assumptions",      "gu": "સંકેતો, Model તથા Assumptions"},
    "given":            {"en": "Given",                               "gu": "આપેલ"},
    "find":             {"en": "Find",                                "gu": "શોધો"},
    "formula":          {"en": "Formula",                             "gu": "સૂત્ર"},
    "substitution":     {"en": "Substitution and calculation",        "gu": "Substitution તથા Calculation"},
    "answer":           {"en": "Final answer with units",             "gu": "Units સાથે અંતિમ જવાબ"},
    "check":            {"en": "Validity check",                      "gu": "Validity Check"},
    "objective":        {"en": "Objective and official scope",        "gu": "હેતુ તથા Official Scope"},
    "apparatus":        {"en": "Apparatus and preparation",           "gu": "Apparatus તથા તૈયારી"},
    "principle_prac":   {"en": "Principle and assumptions",           "gu": "Principle તથા Assumptions"},
    "procedure":        {"en": "Procedure and record",                "gu": "Procedure તથા Record"},
    "calculation":      {"en": "Calculation format",                  "gu": "Calculation Format"},
    "safety":           {"en": "Safety, quality and limitations",     "gu": "Safety, Quality તથા Limitations"},
    "observation":      {"en": "Blank observation sheet—record actual readings only",
                         "gu": "Blank Observation Sheet—ફક્ત actual readings લખો"},
    "exam_note":        {"en": "Study depth",                         "gu": "Study Depth"},
    "qualification":    {"en": "Qualification", "gu": "નોંધ"},
    "points":           {"en": "Key points and data", "gu": "મુખ્ય મુદ્દા તથા data"},
}

_TAG = re.compile(r"<[^>]+>")
BAD_SPACING = [
    (re.compile(r"\b([a-z]{2,})(\d)"), "missing space before a number"),
    (re.compile(r"([a-z0-9])[,;:](?=[A-Za-z0-9])"), "missing space after , ; :"),
    (re.compile(r"(\d)(mg|kg|ml|mL|kW|kJ|km|cm|mm|MPa|kPa|mol|°C|Pa|W|J|m/s)(?![/\w])"), "missing space before a unit"),
]


def bi(en: str, gu: str | None = None) -> dict:
    """Bilingual string. Un-translated text falls back to English only."""
    return {"en": en} if gu is None else {"en": en, "gu": gu}


def _h(key: str) -> str:
    v = H[key]
    return f"<h4>{v['en']}</h4>" if v.get("gu") is None else f"<h4>{v['en']}</h4>"


def h4(key_en: str) -> str:
    return f"<h4>{key_en}</h4>"


def p(text: str) -> str:
    return f"<p>{text}</p>"


def ul(items) -> str:
    return "<ul>" + "".join(f"<li>{i}</li>" for i in items) + "</ul>"


def ol(items) -> str:
    return "<ol>" + "".join(f"<li>{i}</li>" for i in items) + "</ol>"


def table(head, rows) -> str:
    """Plain table (the app renders th, td and scrolls wide tables)."""
    th = "".join(f"<th>{c}</th>" for c in head)
    tr = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in rows)
    return f"<table><thead><tr>{th}</tr></thead><tbody>{tr}</tbody></table>"


def eq(display: str, tex: str | None = None, note: str = "") -> str:
    """A displayed equation.

    `display` is readable Unicode maths that every current renderer can show today
    (the app, the preview HTML). `tex` keeps the exact LaTeX source in `data-tex`
    so a future KaTeX / flutter_math renderer can upgrade it without touching content.
    """
    src = tex or display
    return (f'<div class="math" data-tex="{src}" aria-label="{src}">{display}</div>'
            + (f"<p>{note}</p>" if note else ""))


def card(ref: str, title: dict, body_en: str, body_gu: str | None = None,
         diagram: str | None = None, examples=None, programs=None) -> dict:
    """One tap-to-open card. `body_en` is HTML using the h4 vocabulary."""
    item = {"h": title, "body": bi(body_en, body_gu)}
    if diagram:
        item["diagram"] = diagram
    if examples:
        item["examples"] = list(examples)
    if programs:
        item["programs"] = list(programs)
    return {"ref": ref, "title": title, "format": "rich_cards", "items": [item]}


# ----------------------------------------------------------------- card builders
def _pick(v, lang: str) -> str:
    """Read a str or a {en, gu} mapping in the requested language (falls back to en)."""
    if v is None:
        return ""
    if isinstance(v, dict):
        return v.get(lang) or v.get("en") or ""
    return str(v)


def _has_gu(*values) -> bool:
    for v in values:
        if isinstance(v, dict) and v.get("gu"):
            return True
        if isinstance(v, (list, tuple)):
            if any(isinstance(x, dict) and x.get("gu") for x in v):
                return True
    return False


EQUATION_LATEX = {}


def _eq(value, lang: str) -> str:
    """One equation given either as a string or as (display, latex)."""
    if isinstance(value, (list, tuple)):
        display = _pick(value[0], lang)
        tex = _pick(value[1] if len(value) > 1 else value[0], "en")
        if len(value) > 2 and value[2]:
            return eq(display, tex, _pick(value[2], lang))
    else:
        display = _pick(value, lang)
        tex = display
    return eq(display, tex)


def _blocks(lang: str, spec) -> str:
    """spec = [(heading_key, value, kind)] where kind is 'p', 'ul' or 'eq'."""
    out = ""
    for key, value, kind in spec:
        if value in (None, "", []):
            continue
        head = f"<h4>{H[key][lang]}</h4>"
        if kind == "p":
            out += head + p(_pick(value, lang))
        elif kind == "ul":
            items = [_pick(v, lang) for v in (value if isinstance(value, (list, tuple)) else [value])]
            out += head + ul(items)
        elif kind == "eq":
            items = value if isinstance(value, (list, tuple)) else [value]
            out += head + "".join(_eq(e, lang) for e in items)
    return out


def theory(ref, title, definition, theory_text, equations=None, list_items=None,
           diagram=None, qualification=None, **_) -> dict:
    """Teaching card: definition -> theory -> (equations) -> (list) -> (qualification)."""
    spec = [("definition", definition, "p"), ("theory", theory_text, "p")]
    if equations:
        spec.append(("equations", equations, "eq"))
    if list_items:
        spec.append(("points", list_items, "ul"))
    if qualification:
        spec.append(("qualification", qualification, "p"))
    en = _blocks("en", spec)
    gu = _blocks("gu", spec) if _has_gu(definition, theory_text, equations, list_items, qualification) else None
    return card(ref, title, en, gu, diagram=diagram)


def equipment(ref, title, definition, principle, construction, working,
              applications, limitations, diagram=None) -> dict:
    """Equipment card: the Construction / Working skeleton GTU papers ask for."""
    spec = [("definition_equip", definition, "p"), ("principle_equip", principle, "p"),
            ("construction", construction, "ul"), ("working", working, "ul"),
            ("applications", applications, "p"), ("limitations", limitations, "p")]
    en = _blocks("en", spec)
    gu = _blocks("gu", spec) if _has_gu(definition, principle, construction, working,
                                         applications, limitations) else None
    return card(ref, title, en, gu, diagram=diagram)


def _step_list(lang, symbols, steps, final) -> str:
    out = f"<h4>{H['symbols'][lang]}</h4>" + p(_pick(symbols, lang)) + "<ol>"
    for text, formula in steps:
        out += f"<li>{p(_pick(text, lang))}"
        if formula:
            out += _eq(formula, lang)
        out += "</li>"
    out += "</ol>" + f"<h4>{'Result' if lang == 'en' else 'પરિણામ'}</h4>"
    out += _eq(final, lang)
    return out


def derivation(ref, title, symbols, steps, final, diagram=None, **_) -> dict:
    """Derivation: assumptions -> numbered steps (sentence + formula) -> boxed result."""
    en = _step_list("en", symbols, steps, final)
    gu = _step_list("gu", symbols, steps, final) if _has_gu(symbols, [s[0] for s in steps]) else None
    return card(ref, title, en, gu, diagram=diagram)


def numerical(ref, title, given, find, formula, substitution, answer, check,
              diagram=None, **_) -> dict:
    """Worked numerical: Given -> Find -> Formula -> Substitution -> Answer -> Validity check."""
    spec = [("given", given, "p"), ("find", find, "p"),
            ("formula", formula, "eq"), ("substitution", substitution, "p"),
            ("answer", answer, "p"), ("check", check, "p")]
    en = _blocks("en", spec)
    gu = _blocks("gu", spec) if _has_gu(given, find, substitution, answer, check) else None
    return card(ref, title, en, gu, diagram=diagram)


def practical(ref, title, objective, apparatus, principle, procedure,
              calculation, safety, columns, rows=3) -> dict:
    """Official practical: no fabricated result, a blank observation sheet only."""
    blank = [["\u2014"] * len(columns) for _ in range(rows)]
    en = (_blocks("en", [("objective", objective, "p"), ("apparatus", apparatus, "p"),
                         ("principle_prac", principle, "p"), ("procedure", procedure, "ul"),
                         ("calculation", calculation, "eq"), ("safety", safety, "p")])
          + f"<h4>{H['observation']['en']}</h4>" + table(columns, blank)
          + p("Result: to be calculated from signed laboratory observations; "
              "no performance or experiment completion is claimed."))
    gu = None
    if _has_gu(objective, apparatus, principle, procedure, safety):
        gu = (_blocks("gu", [("objective", objective, "p"), ("apparatus", apparatus, "p"),
                             ("principle_prac", principle, "p"), ("procedure", procedure, "ul"),
                             ("calculation", calculation, "eq"), ("safety", safety, "p")])
              + f"<h4>{H['observation']['gu']}</h4>" + table(columns, blank))
    return {"ref": ref, "title": title, "format": "rich_cards",
            "items": [{"h": title, "body": bi(en, gu)}]}


def syntax_item(name: dict, formula: str, terms: str = "") -> dict:
    return {"title": name, "f": formula, "terms": terms}


def viva(q: dict, a: dict) -> dict:
    return {"q": q, "a": a}


def exam(q: dict, marks: int) -> dict:
    return {"q": q, "marks": marks}


# ----------------------------------------------------------------- unit
KNOWN_TABS = {"notes", "programs", "diagrams", "flowcharts", "algorithms",
              "syntax", "equations", "numericals", "viva", "exam"}


class Unit:
    def __init__(self, subject, number, title, hours, weightage, tabs,
                 languages=("en", "gu"), tab_labels=None):
        self.data = {
            "subject": subject, "unit": number, "format": "notes", "title": title,
            "languages": list(languages), "tabs": list(tabs),
            "hours": hours, "weightage": weightage,
            "notes": [], "diagrams": [], "viva": [], "exam_questions": [],
        }
        if tab_labels:
            self.data["tab_labels"] = tab_labels

    def section(self, title: dict, cards, gu_title: str | None = None) -> "Unit":
        items = []
        for c in cards:
            # a card builder returns {"items":[...]}; a section holds the items
            items.extend(c["items"] if "items" in c and "format" in c else [c])
        self.data["notes"].append({"title": title, "items": items})
        return self

    def diagram(self, did: str, title: dict, path: str) -> "Unit":
        self.data["diagrams"].append({"id": did, "title": title, "file": path})
        return self

    def syntax(self, title: dict, items) -> "Unit":
        self.data.setdefault("syntax", []).append({"title": title, "items": list(items)})
        return self

    def practicals(self, items) -> "Unit":
        self.data.setdefault("programs", []).extend(items)
        return self

    def viva_questions(self, items) -> "Unit":
        self.data["viva"].extend(items)
        return self

    def exam_questions(self, items) -> "Unit":
        self.data["exam_questions"].extend(items)
        return self

    # -------------------------------------------------------------- output
    def dumps(self) -> str:
        return json.dumps(self.data, ensure_ascii=False, indent=1)

    def write(self, path: str) -> str:
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w", encoding="utf-8") as f:
            f.write(self.dumps())
        return path

    # -------------------------------------------------------------- checks
    def validate(self) -> list[str]:
        """Return a list of problems; empty means the unit matches the template."""
        d = self.data
        out: list[str] = []
        for t in d.get("tabs", []):
            if t not in KNOWN_TABS:
                out.append(f"tab '{t}' is not in the app's knownTabs")
        if not d["notes"]:
            out.append("unit has no notes sections")
        if not d["diagrams"] and any(t == "diagrams" for t in d.get("tabs", [])):
            out.append("diagrams tab declared but no diagrams listed")
        if not d["exam_questions"] and "exam" in d.get("tabs", []):
            out.append("exam tab declared but no exam questions")
        if not d["viva"] and "viva" in d.get("tabs", []):
            out.append("viva tab declared but no viva questions")
        for si, sec in enumerate(d["notes"]):
            for ii, it in enumerate(sec["items"]):
                where = f"notes[{si}].items[{ii}]"
                body = it.get("body")
                if not isinstance(body, dict) or not body.get("en"):
                    out.append(f"{where}: empty English body")
                    continue
                en = body["en"]
                heads = re.findall(r"<h4>(.*?)</h4>", en)
                if not heads:
                    out.append(f"{where}: no <h4> headings — not following the template")
                if it.get("diagram") and it["diagram"] not in {x["id"] for x in d["diagrams"]}:
                    out.append(f"{where}: diagram '{it['diagram']}' not in the diagrams list")
                for rx, why in BAD_SPACING:
                    m = rx.search(_TAG.sub(" ", en))
                    if m:
                        out.append(f"{where}: {why} near '{en[max(0, m.start() - 25):m.start() + 15]}'")
                        break
        ids = [x["id"] for x in d["diagrams"]]
        if len(ids) != len(set(ids)):
            out.append("duplicate diagram ids")
        return out
