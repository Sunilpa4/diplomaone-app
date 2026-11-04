"""Bidirectional JSON <-> YAML for DiplomaOne unit files.

    python3 tools/d1yaml.py to-yaml   content/<branch>/sem<N>/<CODE>/unit1.json
    python3 tools/d1yaml.py from-yaml content/<branch>/sem<N>/<CODE>/unit1.yml -o /tmp/u1.json
    python3 tools/d1yaml.py check     content/<branch>/sem<N>/<CODE>/unit1.yml

The YAML form is the app schema 1:1, plus two conveniences:

  meta          project/authoring information, stripped on import
  diagrams[].svg  the drawing itself, inlined from diagrams/*.svg, so the
                  file is readable and shareable on its own; on import it is
                  moved into the "svgs" map that the Flutter app expects.

Requires PyYAML (python3 -m pip install --user pyyaml).
"""
import argparse
import json
import os
import sys

import yaml

SCHEMA = "diplomaone/unit@1"


class BlockDumper(yaml.SafeDumper):
    """Keeps long HTML strings readable as |- blocks instead of quoted soup."""


def _represent_str(dumper, data):
    if "\n" in data:
        style = "|"
    elif len(data) > 110 and "<" in data:
        style = "|"
    else:
        style = None
    return dumper.represent_scalar("tag:yaml.org,2002:str", data, style=style)


BlockDumper.add_representer(str, _represent_str)


def _load_pyyaml_or_die():
    try:
        import yaml as _y  # noqa: F401
    except ImportError:
        sys.exit("PyYAML missing: python3 -m pip install --user pyyaml")


def _subject_of(unit_path):
    here = os.path.dirname(os.path.abspath(unit_path))
    sp = os.path.join(here, "subject.json")
    if os.path.exists(sp):
        with open(sp, encoding="utf-8") as f:
            return json.load(f)
    return {}


def to_yaml(unit_path, out_path=None):
    with open(unit_path, encoding="utf-8") as f:
        data = json.load(f)
    subj = _subject_of(unit_path)
    diagrams = data.get("diagrams") or []
    base = os.path.dirname(os.path.abspath(unit_path))
    for d in diagrams:
        rel = d.get("file")
        if rel and "svg" not in d:
            full = os.path.join(base, rel)
            if os.path.exists(full):
                with open(full, encoding="utf-8") as f:
                    d["svg"] = f.read().strip()
    meta = {
        "schema": SCHEMA,
        "project": "DiplomaOne — GTU Diploma Engineering, Chemical",
        "subject_code": data.get("subject") or subj.get("code"),
        "subject_name": subj.get("name"),
        "semester": subj.get("semester"),
        "syllabus": {
            "authority": "Gujarat Technological University",
            "effective": subj.get("syllabus_year"),
            "source": (subj.get("sources") or [{}])[0].get("file"),
            "unit_hours": data.get("hours"),
            "unit_weightage_percent": data.get("weightage"),
        },
        "counts": {
            "sections": len(data.get("notes") or []),
            "cards": sum(len(s.get("items") or []) for s in data.get("notes") or []),
            "solved_problems": len(data.get("programs") or []),
            "diagrams": len(diagrams),
            "viva": len(data.get("viva") or []),
            "exam_questions": len(data.get("exam_questions") or []),
        },
        "languages": data.get("languages", ["en", "gu"]),
        "note": "meta is authoring information only; it is stripped when the file is converted back to JSON.",
    }
    merged = {"meta": meta}
    merged.update(data)
    out_path = out_path or os.path.splitext(unit_path)[0] + ".yml"
    with open(out_path, "w", encoding="utf-8") as f:
        f.write("# DiplomaOne unit file — edit freely, convert back with:\n")
        f.write(f"#   python3 tools/d1yaml.py from-yaml {os.path.relpath(out_path)}\n")
        f.write(f"# Schema: {SCHEMA}.  Bodies are HTML; equations carry LaTeX in data-tex.\n\n")
        yaml.dump(merged, f, Dumper=BlockDumper, allow_unicode=True,
                  sort_keys=False, default_flow_style=False, width=10 ** 6)
    return out_path


def from_yaml(yml_path, out_path=None):
    with open(yml_path, encoding="utf-8") as f:
        data = yaml.safe_load(f)
    data.pop("meta", None)
    svgs = {}
    for d in data.get("diagrams") or []:
        svg = d.pop("svg", None)
        if svg:
            svgs[d["id"]] = svg
    if svgs:
        data["svgs"] = svgs
    out_path = out_path or os.path.splitext(yml_path)[0] + ".json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=1)
    return out_path, data


def check(yml_path):
    """Structural checks that mirror tools/d1notes.Unit.validate()."""
    _, d = from_yaml(yml_path, os.devnull if os.path.exists(os.devnull) else "/tmp/_chk.json")
    problems = []
    allowed = {"notes", "programs", "diagrams", "syntax", "viva", "exam", "exam_questions", "practicals"}
    for t in d.get("tabs", []):
        if t not in allowed:
            problems.append(f"unknown tab {t!r}")
    if not d.get("title", {}).get("en"):
        problems.append("missing title.en")
    for s in d.get("notes") or []:
        if not s.get("items"):
            problems.append(f"empty section {s.get('title', {}).get('en')!r}")
        for it in s.get("items") or []:
            body = it.get("body") or {}
            if isinstance(body, dict) and not body.get("en"):
                problems.append(f"empty EN body in {it.get('h')!r}")
            if isinstance(body, dict) and not body.get("gu"):
                problems.append(f"missing GU body in {it.get('h')!r}")
            txt = body.get("en", "") if isinstance(body, dict) else str(body)
            if "<h4>" not in txt:
                problems.append(f"card {it.get('h')!r} has no <h4> headings")
    ids = {x["id"] for x in d.get("diagrams") or []}
    for s in d.get("notes") or []:
        for it in s.get("items") or []:
            if it.get("diagram") and it["diagram"] not in ids:
                problems.append(f"card {it.get('h')!r} points at unknown diagram {it['diagram']!r}")
    for v in d.get("viva") or []:
        for side in ("q", "a"):
            if not (v.get(side) or {}).get("en"):
                problems.append(f"viva entry missing {side}.en")
    for p in d.get("programs") or []:
        if not p.get("items"):
            problems.append(f"program {p.get('title')!r} has no items")
    return problems, d


def main():
    ap = argparse.ArgumentParser(description="Convert DiplomaOne unit JSON <-> YAML")
    ap.add_argument("mode", choices=["to-yaml", "from-yaml", "check"])
    ap.add_argument("path")
    ap.add_argument("-o", "--out")
    a = ap.parse_args()
    if a.mode == "to-yaml":
        print("wrote", to_yaml(a.path, a.out))
    elif a.mode == "from-yaml":
        print("wrote", from_yaml(a.path, a.out)[0])
    else:
        problems, d = check(a.path)
        print("problems:", problems or "none")
        if problems:
            sys.exit(1)


if __name__ == "__main__":
    main()
