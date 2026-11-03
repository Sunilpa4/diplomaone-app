"""Build preview/workshop/maths.html - one review index for both mathematics subjects.

Reads the built unit JSON so the counts are always the ones actually shipped.
"""
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(HERE))

from subject_DI01000021 import SUBJ_DIR as SEM1_DIR  # noqa: E402
from subject_DI02000021 import SUBJ_DIR as SEM2_DIR  # noqa: E402

OUT = ROOT / "preview/workshop/maths.html"


def load(subj_dir):
    subject = json.loads((subj_dir / "subject.json").read_text(encoding="utf-8"))
    units = []
    for spec in subject["units"]:
        path = subj_dir / spec["file"]
        if not path.is_file():
            continue
        data = json.loads(path.read_text(encoding="utf-8"))
        teaching = data["notes"][:-1]  # the last section is always "practice with model answers"
        units.append({
            "no": data["unit"],
            "title": data["title"]["en"],
            "hours": data["hours"],
            "weight": data["weightage"],
            "marks": subject["theory_marks_by_unit"].get(str(data["unit"]), 0),
            "foundation": data["unit"] == 0 and data["hours"] == 0,
            "cards": sum(len(s["items"]) for s in teaching),
            "items": sum(len(s["items"]) for s in data["notes"]),
            "numericals": len(data["numericals"]),
            "diagrams": len(data["diagrams"]),
            "equations": sum(len(g["items"]) for g in data["equations"]),
            "viva": sum(len(g["items"]) for g in data["viva"]),
            "exam": len(data["exam_questions"]),
            "practice": len(data["notes"][-1]["items"]),
            "topics": len({it.get("syllabus_item") for s in teaching for it in s["items"]
                           if it.get("syllabus_item")}),
            "syllabus_topics": len(spec.get("topics", [])),
        })
    return subject, sorted(units, key=lambda u: u["no"])


def subject_block(subject, units, semester):
    code = subject["code"]
    name = subject["name"]["en"]
    rows = []
    for u in units:
        rows.append(
            "<tr>"
            f'<td class="no">{u["no"]}</td>'
            f'<td class="ttl"><a href="{code}_u{u["no"]}.html">{u["title"]}</a></td>'
            f'<td>{u["hours"] or "–"}</td>'
            f'<td>{(str(u["weight"]) + " %") if u["weight"] else "–"}</td>'
            f'<td>{u["marks"] or "–"}</td>'
            f'<td>{u["cards"]}</td>'
            f'<td>{u["numericals"]}</td>'
            f'<td>{u["diagrams"]}</td>'
            f'<td>{u["equations"]}</td>'
            f'<td>{u["viva"]}</td>'
            f'<td>{u["practice"]}</td>'
            f'<td class="cov">{(str(u["topics"]) + "/" + str(u["syllabus_topics"])) if u["topics"] else "–"}</td>'
            "</tr>"
        )
    totals = {k: sum(u[k] for u in units) for k in
              ("hours", "weight", "marks", "cards", "numericals", "diagrams", "equations", "viva",
               "practice")}
    total_row = (
        '<tr class="tot"><td></td><td class="ttl">All units</td>'
        f'<td>{totals["hours"]}</td><td>{totals["weight"]} %</td><td>{totals["marks"]}</td>'
        f'<td>{totals["cards"]}</td><td>{totals["numericals"]}</td><td>{totals["diagrams"]}</td>'
        f'<td>{totals["equations"]}</td><td>{totals["viva"]}</td><td>{totals["practice"]}</td>'
        "<td class=\"cov\"></td></tr>"
    )
    return f"""
  <section class="subj">
    <div class="head">
      <div>
        <div class="code">{code} · Semester {semester}</div>
        <h2>{name}</h2>
        <div class="meta">{len(units)} units · {totals["hours"]} teaching hours · theory ESE
          {subject["exam"]["theory_ese"]} + PA {subject["exam"]["theory_pa"]} ·
          {subject["exam"]["credits"]} credits · BSC</div>
      </div>
      <div class="badge">all 27 branches</div>
    </div>
    <div class="scroll"><table>
      <thead><tr>
        <th>#</th><th class="ttl">Unit</th><th>h</th><th>wt</th><th>marks</th><th>cards</th>
        <th>sums</th><th>diag</th><th>form</th><th>viva</th><th>prac</th><th>topics</th>
      </tr></thead>
      <tbody>{''.join(rows)}{total_row}</tbody>
    </table></div>
  </section>"""


CSS = """
 :root{--p:#7B2CD9;--pd:#5B1BB0;--lav:#EADDF7;--bg:#F3ECFA;--ink:#1d1b20;--muted:#6b6478}
 *{box-sizing:border-box}
 body{margin:0;background:var(--bg);color:var(--ink);font:15px/1.55 system-ui,-apple-system,"Segoe UI",Roboto,sans-serif}
 header{background:var(--p);color:#fff;padding:24px 18px 20px}
 header .wrap{max-width:860px;margin:0 auto}
 header h1{margin:0 0 6px;font-size:22px}
 header p{margin:0;opacity:.92;font-size:13.5px}
 main{max-width:860px;margin:0 auto;padding:18px 14px 44px}
 .subj{background:#fff;border:1px solid #eadcf9;border-radius:14px;padding:16px 16px 10px;margin:0 0 16px;
   box-shadow:0 1px 3px rgba(60,20,110,.12)}
 .head{display:flex;gap:12px;justify-content:space-between;align-items:flex-start;margin-bottom:10px}
 .code{font:700 11.5px/1 ui-monospace,monospace;color:var(--p);letter-spacing:.5px;text-transform:uppercase}
 h2{margin:6px 0 4px;font-size:18px}
 .meta{color:var(--muted);font-size:12.8px}
 .badge{flex:none;background:#F5EEFD;color:var(--pd);border:1px solid #dcc7f5;border-radius:999px;
   padding:5px 11px;font-size:11.5px;font-weight:700;white-space:nowrap}
 .scroll{overflow-x:auto;-webkit-overflow-scrolling:touch}
 table{border-collapse:collapse;width:100%;font-size:13px;min-width:640px}
 th,td{padding:7px 6px;text-align:right;border-bottom:1px solid #f0e8fb;white-space:nowrap}
 th{font-size:11px;text-transform:uppercase;letter-spacing:.4px;color:var(--muted);font-weight:700}
 th.ttl,td.ttl{text-align:left;white-space:normal;min-width:190px}
 td.no{text-align:right;color:var(--muted)}
 td.ttl a{color:var(--pd);text-decoration:none;font-weight:600}
 td.ttl a:hover{text-decoration:underline}
 tr.tot td{font-weight:700;background:#faf7fe;border-bottom:none}
 td.cov{color:var(--muted)}
 .tips{margin-top:18px;background:#fff;border:1px solid #eadcf9;border-radius:12px;padding:14px 16px;font-size:13.4px}
 .tips h3{margin:0 0 8px;font-size:13px;color:var(--pd);text-transform:uppercase;letter-spacing:.5px}
 .tips li{margin-bottom:5px}
 footer{max-width:860px;margin:0 auto;padding:0 14px 30px;color:var(--muted);font-size:12px}
 a.plain{color:var(--pd)}
"""


def main():
    s1, u1 = load(SEM1_DIR)
    s2, u2 = load(SEM2_DIR)
    html = f"""<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>DiplomaOne · Mathematics I and II</title>
<style>{CSS}</style></head>
<body>
<header><div class="wrap">
  <h1>Mathematics I and II</h1>
  <p>Both subjects built for all 27 branches · 11 units · tap a unit name to open its notes</p>
</div></header>
<main>
{subject_block(s1, u1, 1)}
{subject_block(s2, u2, 2)}
  <div class="tips">
    <h3>What the columns mean</h3>
    <ul>
      <li><b>cards</b> - teaching cards (a practice section is not counted).</li>
      <li><b>sums</b> - fully solved numericals, each linked from a card.</li>
      <li><b>diag</b> - hand-drawn SVG diagrams inside the notes.</li>
      <li><b>form</b> - formula-sheet entries; <b>viva</b> - oral questions with answers.</li>
      <li><b>prac</b> - practice questions with model answers, matching the exam list one for one.</li>
      <li><b>topics</b> - syllabus sub-items covered against the number in the syllabus.</li>
    </ul>
  </div>
  <p style="margin-top:16px"><a class="plain" href="index.html">← back to the notes workshop shelf</a></p>
</main>
<footer>Generated by tools/maths_index.py from the built unit JSON - counts always match what ships.</footer>
</body></html>"""
    OUT.write_text(html, encoding="utf-8")
    print(f"wrote {OUT.relative_to(ROOT)} ({OUT.stat().st_size // 1024} KB)")
    for subj, units in ((s1, u1), (s2, u2)):
        print(f"  {subj['code']}: {len(units)} units, "
              f"{sum(u['cards'] for u in units)} cards, {sum(u['numericals'] for u in units)} numericals, "
              f"{sum(u['diagrams'] for u in units)} diagrams, {sum(u['practice'] for u in units)} practice")


if __name__ == "__main__":
    main()
