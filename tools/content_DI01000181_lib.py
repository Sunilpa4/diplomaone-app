"""Bilingual writing helpers for DI01000181 Engineering Materials Science.

Every helper takes an (English, Gujarati) pair and returns the pair of HTML strings, so the body of a
card is written once and comes out in both languages. Mathematics is identical in both languages and
is written once with `math()` / `eq()`.

The house style of this subject:

  h4 heading  ->  what the thing is  ->  DERIVATION, one line per step  ->  result box  ->  numbers
  ->  check, and for a structure or a process: MADE (how it is built) then BEHAVES (what it does).

`math()` is the workhorse for a derivation: it prints the lines inside a monospace block, so the
integrals, the limits and the algebra stay aligned instead of being lost in running prose.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from subject_DI01000181 import tr  # noqa: E402

EN = 0
GU = 1


# ---------------------------------------------------------------- text blocks
def p(en, gu):
    return (f"<p>{en}</p>", f"<p>{gu}</p>")


def h4(en, gu):
    return (f"<h4>{en}</h4>", f"<h4>{gu}</h4>")


def b(en, gu):
    """Bold inline fragment (used inside other text)."""
    return (f"<b>{en}</b>", f"<b>{gu}</b>")


def ul(*pairs):
    en = "<ul>" + "".join(f"<li>{a}</li>" for a, _ in pairs) + "</ul>"
    gu = "<ul>" + "".join(f"<li>{c}</li>" for _, c in pairs) + "</ul>"
    return (en, gu)


def ol(*pairs):
    en = "<ol>" + "".join(f"<li>{a}</li>" for a, _ in pairs) + "</ol>"
    gu = "<ol>" + "".join(f"<li>{c}</li>" for _, c in pairs) + "</ol>"
    return (en, gu)


def _pick(cell, lang):
    """A cell may be a bilingual dict, a plain (en, gu) pair, or a string that needs no translation."""
    if isinstance(cell, dict):
        return cell[lang]
    if isinstance(cell, (tuple, list)):
        return cell[EN if lang == "en" else GU]
    return cell


def table(head, rows):
    """head: list of bilingual labels; rows: list of rows, each a list of bilingual cells."""
    def build(lang):
        h = "".join(f"<th>{_pick(c, lang)}</th>" for c in head)
        body = "".join("<tr>" + "".join(f"<td>{_pick(c, lang)}</td>" for c in row) + "</tr>"
                       for row in rows)
        return f"<table><tr>{h}</tr>{body}</table>"
    return (build("en"), build("gu"))


def math(*lines):
    """A block of mathematics - the same text in both languages, aligned in a monospace box."""
    txt = "\n".join(lines)
    html = f'<div class="math">{txt}</div>'
    return (html, html)


def eq(*lines):
    """One headline result, shown in the purple formula box."""
    txt = "   ".join(lines)
    html = f'<div class="eq">{txt}</div>'
    return (html, html)


def derive(*lines):
    """A derivation: a labelled, numbered list of algebraic steps."""
    txt = "\n".join(f"{i:>2}. {s}" for i, s in enumerate(lines, 1))
    html = f'<div class="math">{txt}</div>'
    return (html, html)


# ---------------------------------------------------------------- teaching devices
def why(en, gu):
    return p(f"<b>Why it is true.</b> {en}", f"<b>કેમ સાચું છે.</b> {gu}")


def check(en, gu):
    return p(f"<b>Check your answer.</b> {en}", f"<b>જવાબ ચકાસો.</b> {gu}")


def pit(en, gu):
    return p(f"<b>Common mistake.</b> {en}", f"<b>સામાન્ય ભૂલ.</b> {gu}")


def made(*pairs):
    """How a piece of equipment is built - one bullet per part, part name in bold."""
    head, items = h4("How it is made", "કેવી રીતે બનાવાય છે"), ul(*pairs)
    return (head[0] + items[0], head[1] + items[1])


def behaves(*pairs):
    """How the same equipment works - numbered, in the order the material moves."""
    head, steps = h4("How it behaves", "કેવું વર્તન કરે છે"), ol(*pairs)
    return (head[0] + steps[0], head[1] + steps[1])


def body(*parts_):
    """Join (en, gu) parts into the bilingual body of one card."""
    return tr("".join(x[EN] for x in parts_), "".join(x[GU] for x in parts_))


def card(heading_en, heading_gu, *parts_, diagram=None, syllabus_item=None):
    item = {"h": tr(heading_en, heading_gu), "body": body(*parts_)}
    if diagram:
        item["diagram"] = diagram
    if syllabus_item:
        item["syllabus_item"] = syllabus_item
    return item


def problem(heading_en, heading_gu, q_en, q_gu, a_parts):
    """A solved numerical: the question, then the worked answer in both languages."""
    item = {"h": tr(heading_en, heading_gu), "body": body(*a_parts),
            "question": tr(q_en, q_gu)}
    return item
