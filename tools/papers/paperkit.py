"""Shared kit for hand-written solved papers.

A paper module builds META / PARTS and calls write_paper(); the stylesheet, the
English+Gujarati wrappers, the printed-question line, the notebook blocks and the
footer all come from here so every paper in a series looks identical.

Markup (all whitelisted by website/app.js sanitizePaper):
  .work  one statement per line, ruled left margin
  ol.steps + .step-label  numbered notebook steps
  .result  boxed final answer
  .frac .num .den  stacked fraction (numerator above, line, denominator below)
  table / ul / ol / h4 / figure(svg) / .eq
"""
from html import escape
from pathlib import Path

CSS = """
:root{--ink:#231f26;--muted:#6c6673;--blue:#145c8b;--pale:#eaf4fa;--line:#e2dde6;--paper:#f8f7f9;--accent:#6a2f86;--wash:#f3ecf7}
*{box-sizing:border-box}
body{margin:0;background:var(--paper);color:var(--ink);font:16px/1.66 system-ui,-apple-system,"Segoe UI",Arial,sans-serif}
.page{width:min(1000px,calc(100% - 28px));margin:24px auto 68px}
.hero{background:#fff;border:1px solid var(--line);border-radius:16px;padding:24px;margin-bottom:22px}
.eyebrow{color:var(--blue);font-size:.79rem;font-weight:800;letter-spacing:.08em;text-transform:uppercase}
.hero h1{font-size:clamp(1.45rem,4vw,2.1rem);line-height:1.24;margin:.4rem 0 .2rem}
.meta{color:var(--muted);font-size:.92rem}
.note{background:var(--pale);border-left:4px solid #4389b3;border-radius:7px;padding:12px 15px;margin:14px 0 0;font-size:.94rem}
.note p{margin:6px 0}
.group{margin:30px 0}
.group h2{font-size:1.3rem;color:var(--blue);margin:0 0 10px}
.card{background:#fff;border:1px solid var(--line);border-radius:11px;margin:10px 0;overflow:hidden}
.card summary{cursor:pointer;padding:14px 17px;color:#164f73;display:flex;gap:10px;align-items:baseline;flex-wrap:wrap;list-style:none}
.card summary::-webkit-details-marker{display:none}
.card summary strong{flex:1;min-width:210px;font-weight:700;line-height:1.5}
.card summary small{font-size:.78rem;color:var(--muted);white-space:nowrap}
.answer{border-top:1px solid var(--line);padding:16px 19px;overflow-wrap:anywhere}
.answer p{margin:9px 0}
.answer li{margin:5px 0}
.answer ul,.answer ol{padding-left:1.35rem}
.answer h4{margin:17px 0 5px;color:#3f4a56;font-size:.97rem}
.answer h4:first-child{margin-top:2px}
.answer .qline{color:var(--muted);font-size:.9rem;background:#f6f4f7;border-left:3px solid #cbb8d6;padding:7px 11px;border-radius:6px}
.answer table{border-collapse:collapse;width:100%;font-size:.92rem;margin:12px 0}
.answer th,.answer td{border:1px solid #d9d3de;padding:7px 9px;vertical-align:top;text-align:left}
.answer th{background:#f2ecf6;font-weight:700}
.answer code{font:13px ui-monospace,SFMono-Regular,Consolas,monospace;background:#f3eef7;border-radius:4px;padding:1px 5px}
.work{border-left:2px solid #e2d5ea;margin:12px 0;padding:2px 0 2px 14px}
.work p{margin:5px 0;line-height:1.9}
ol.steps{counter-reset:step;list-style:none;margin:12px 0;padding:0}
ol.steps>li{counter-increment:step;position:relative;margin:4px 0;padding:2px 0 2px 34px;line-height:1.85}
ol.steps>li:before{content:counter(step);position:absolute;left:0;top:5px;width:23px;height:23px;border-radius:50%;background:#f1e7f7;color:var(--accent);font:700 12px/23px system-ui,sans-serif;text-align:center}
.step-label{display:block;color:var(--accent);font-size:.76rem;font-weight:700;text-transform:uppercase;letter-spacing:.04em}
.result{display:table;border:1px solid #77a795;border-radius:8px;padding:8px 13px;background:#f1fbf6;margin:12px 0}
.frac{display:inline-flex;vertical-align:middle;flex-direction:column;text-align:center;font-style:italic;line-height:1.25;margin:0 .18em}
.num{border-bottom:1.4px solid;padding:0 .32em .12em}
.den{padding:.12em .32em 0}
.eq{font:italic 17px Georgia,serif;background:var(--wash);border-left:3px solid #b294c4;padding:8px 12px;border-radius:6px;margin:10px 0;overflow-x:auto}
figure{margin:16px auto;max-width:780px}
figure svg{display:block;width:100%;height:auto;background:#fff;border:1px solid var(--line);border-radius:9px}
figcaption{font-size:.84rem;color:var(--muted);margin-top:6px}
.footer{font-size:.86rem;color:var(--muted);border-top:1px solid var(--line);margin-top:34px;padding-top:14px}
.tag{display:inline-block;background:var(--wash);color:var(--accent);border-radius:20px;padding:2px 10px;font-size:.74rem;font-weight:700;margin:0 6px 4px 0}
@media(max-width:640px){.page{width:calc(100% - 16px);margin-top:8px}.hero{padding:17px}.answer{padding:13px}.card summary strong{min-width:150px}.answer table{font-size:.83rem}.answer th,.answer td{padding:5px 6px}}
"""


# ---------------------------------------------------------------------------
# building blocks
# ---------------------------------------------------------------------------

def frac(num, den):
    return f'<span class="frac"><span class="num">{num}</span><span class="den">{den}</span></span>'


def work(*lines):
    return '<div class="work">' + ''.join(f'<p>{l}</p>' for l in lines) + '</div>'


def steps(*items):
    """Each item is a string, or (label, line)."""
    out = []
    for item in items:
        if isinstance(item, tuple):
            label, line = item
            out.append(f'<li><span class="step-label">{label}</span>{line}</li>')
        else:
            out.append(f'<li>{item}</li>')
    return '<ol class="steps">' + ''.join(out) + '</ol>'


def result(html):
    return f'<p class="result"><b>{html}</b></p>'


def table(headers, rows):
    head = ''.join(f'<th>{h}</th>' for h in headers)
    body = ''.join('<tr>' + ''.join(f'<td>{c}</td>' for c in row) + '</tr>' for row in rows)
    return f'<table><thead><tr>{head}</tr></thead><tbody>{body}</tbody></table>'


def bullets(*items):
    return '<ul>' + ''.join(f'<li>{i}</li>' for i in items) + '</ul>'


def numbered(*items):
    return '<ol>' + ''.join(f'<li>{i}</li>' for i in items) + '</ol>'


def h4(title):
    return f'<h4>{title}</h4>'


def p(*chunks):
    return ''.join(f'<p>{c}</p>' for c in chunks)


def eq(html):
    return f'<div class="eq">{html}</div>'


def figure(svg, caption):
    return f'<figure>{svg}<figcaption>{caption}</figcaption></figure>'


# ---------------------------------------------------------------------------
# paper assembly
# ---------------------------------------------------------------------------

def _both(en, gu):
    return f'<div class="en">{en}</div><div class="gu">{gu}</div>'


def card(part):
    """part = dict(number, marks, q, en, gu, tag=None).

    `q` is the question exactly as printed in English; it is repeated unchanged in
    both language modes so the paper's own wording never drifts.
    """
    tag = f'<span class="tag">{part["tag"]}</span>' if part.get('tag') else ''
    q = part['q']
    summary = (
        '<summary>'
        f'<span class="en"><strong>{escape(part["number"])} · {q}</strong>{tag}'
        f'<small>{part["marks"]} marks</small></span>'
        f'<span class="gu"><strong>{escape(part["number"])} · {q}</strong>{tag}'
        f'<small>{part["marks"]} ગુણ</small></span>'
        '</summary>'
    )
    en_body = f'<div class="answer"><p class="qline"><b>Question as printed:</b> {q}</p>{part["en"]}</div>'
    gu_body = f'<div class="answer"><p class="qline"><b>Question as printed:</b> {q}</p>{part["gu"]}</div>'
    return f'<details class="card">{summary}{_both(en_body, gu_body)}</details>'


def write_paper(path, meta, groups):
    """meta: dict with code, session, exam_date, marks, title_en, title_gu, meta_en,
    meta_gu, notes_en, notes_gu, assumptions_en, assumptions_gu, footer_en, footer_gu,
    part_count. groups: [{title_en, title_gu, cards:[part, ...]}]"""
    hero = f"""<header class="hero">
{_both(
    f'<div class="eyebrow">GTU Diploma · solved question paper · English edition</div>'
    f'<h1>{meta["title_en"]}</h1><div class="meta">{meta["meta_en"]}</div>',
    f'<div class="eyebrow">GTU ડિપ્લોમા · ઉકેલેલું પ્રશ્નપત્ર · ગુજરાતી આવૃત્તિ</div>'
    f'<h1>{meta["title_gu"]}</h1><div class="meta">{meta["meta_gu"]}</div>')}
<div class="note">
{_both(
    meta['notes_en'],
    meta['notes_gu'])}
</div>
</header>"""

    body = []
    for g in groups:
        cards = ''.join(card(c) for c in g['cards'])
        heading = _both(f'<h2>{g["title_en"]}</h2>', f'<h2>{g["title_gu"]}</h2>')
        body.append(f'<section class="group">{heading}{cards}</section>')

    footer = f"""<footer class="footer">
{_both(f'<p><b>Source:</b> {meta["footer_en"]}</p>',
        f'<p><b>સ્રોત:</b> {meta["footer_gu"]}</p>')}
<p>DiplomaOne · a solved paper is study support, not official GTU material. Always check the printed
question paper and your institute's answer key.</p>
</footer>"""

    html = f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{meta['code']} · {meta['session']} solved paper</title>
<style>{CSS}</style></head>
<body><main class="page">
{hero}
{''.join(body)}
{footer}
</main></body></html>
"""
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(html, encoding='utf-8')
    return path
