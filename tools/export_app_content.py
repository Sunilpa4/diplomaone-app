"""Export finished content into the Flutter app's assets (and the same files are what
the admin panel uploads to Firestore).

Full data (published to GitHub Pages by tools/publish.py):
  catalog.json                      branches, semesters, subjects, "files": {path: version-hash}
  subjects/<CODE>.json              subject.json (+ unit list)
  units/<CODE>_u<N>.json            unit JSON + "svgs": {diagram_id: svg_text}
The app bundles only catalog.json + subjects/ (offline fallback); units are downloaded on demand.

Run:  python3 tools/export_app_content.py [--out DIR] [--app-assets]   (default DIR = build/data)
"""
import json, os, re, glob, shutil, hashlib, sys, time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONTENT = os.path.join(ROOT, "content")
OUT = os.path.join(ROOT, "build", "data")
APP_ASSETS = os.path.join(ROOT, "app", "assets", "content")

# ---------------------------------------------------------------- branches
# (code, key, english, gujarati, icon, colour)
BRANCHES = [
    ("07", "computer", "Computer Engineering", "કમ્પ્યુટર એન્જિનિયરિંગ", "computer", "#7B2CD9"),
    ("16", "it", "Information Technology", "ઇન્ફોર્મેશન ટેકનોલોજી", "lan", "#1565C0"),
    ("31", "cse", "Computer Science & Engineering", "કમ્પ્યુટર સાયન્સ એન્ડ એન્જિનિયરિંગ", "terminal", "#5E35B1"),
    ("32", "ict", "Information & Communication Technology", "ઇન્ફોર્મેશન એન્ડ કમ્યુનિકેશન ટેકનોલોજી", "wifi", "#00838F"),
    ("19", "mechanical", "Mechanical Engineering", "મિકેનિકલ એન્જિનિયરિંગ", "settings", "#E65100"),
    ("06", "civil", "Civil Engineering", "સિવિલ એન્જિનિયરિંગ", "apartment", "#6D4C41"),
    ("09", "electrical", "Electrical Engineering", "ઇલેક્ટ્રિકલ એન્જિનિયરિંગ", "bolt", "#F9A825"),
    ("11", "ec", "Electronics & Communication Engineering", "ઇલેક્ટ્રોનિક્સ એન્ડ કમ્યુનિકેશન એન્જિનિયરિંગ", "antenna", "#2E7D32"),
    ("02", "automobile", "Automobile Engineering", "ઓટોમોબાઇલ એન્જિનિયરિંગ", "car", "#C62828"),
    ("05", "chemical", "Chemical Engineering", "કેમિકલ એન્જિનિયરિંગ", "science", "#00897B"),
    ("01", "aeronautical", "Aeronautical Engineering", "એરોનોટિકલ એન્જિનિયરિંગ", "flight", "#0277BD"),
    ("03", "biomedical", "Biomedical Engineering", "બાયોમેડિકલ એન્જિનિયરિંગ", "heart", "#AD1457"),
    ("13", "environmental", "Environmental Engineering", "એન્વાયર્નમેન્ટલ એન્જિનિયરિંગ", "eco", "#558B2F"),
    ("17", "ic", "Instrumentation & Control Engineering", "ઇન્સ્ટ્રુમેન્ટેશન એન્ડ કંટ્રોલ એન્જિનિયરિંગ", "speed", "#4527A0"),
    ("18", "marine", "Marine Engineering", "મરીન એન્જિનિયરિંગ", "boat", "#01579B"),
    ("20", "mechatronics", "Mechatronics Engineering", "મેકાટ્રોનિક્સ એન્જિનિયરિંગ", "robot", "#6A1B9A"),
    ("21", "metallurgy", "Metallurgy Engineering", "મેટલર્જી એન્જિનિયરિંગ", "hardware", "#455A64"),
    ("22", "mining", "Mining Engineering", "માઇનિંગ એન્જિનિયરિંગ", "landscape", "#795548"),
    ("23", "plastic", "Plastic Engineering", "પ્લાસ્ટિક એન્જિનિયરિંગ", "category", "#0097A7"),
    ("24", "power", "Power Electronics", "પાવર ઇલેક્ટ્રોનિક્સ", "power", "#EF6C00"),
    ("28", "textile_mfg", "Textile Manufacturing Technology", "ટેક્સટાઇલ મેન્યુફેક્ચરિંગ ટેકનોલોજી", "textile", "#8E24AA"),
    ("29", "textile_proc", "Textile Processing Technology", "ટેક્સટાઇલ પ્રોસેસિંગ ટેકનોલોજી", "textile", "#D81B60"),
    ("34", "mech_mfg", "Mechanical Engineering (Manufacturing)", "મિકેનિકલ એન્જિનિયરિંગ (મેન્યુફેક્ચરિંગ)", "factory", "#BF360C"),
    ("41", "robotics", "Automation & Robotics", "ઓટોમેશન એન્ડ રોબોટિક્સ", "robot", "#283593"),
    ("58", "printing", "Printing Technology", "પ્રિન્ટિંગ ટેકનોલોજી", "print", "#37474F"),
    ("60", "transportation", "Transportation Engineering", "ટ્રાન્સપોર્ટેશન એન્જિનિયરિંગ", "bus", "#00695C"),
    ("61", "fire", "Fire Technology & Safety", "ફાયર ટેકનોલોજી એન્ડ સેફ્ટી", "fire", "#D84315"),
]

# ---------------------------------------------------------------- subjects
# code -> (english, gujarati, category, credits, type, alt_code)
SUBJECTS = {
    # Computer Sem 1 (2024-25)
    "DI01000021": ("Mathematics - I", "ગણિત - I", "Basic Science", 4, "theory", "DI01C00021"),
    "DI01000031": ("Communication Skills in English", "કમ્યુનિકેશન સ્કિલ્સ ઇન ઇંગ્લિશ", "Humanities", 3, "theory", "DI01C00031"),
    "DI01000061": ("Modern Physics", "મોડર્ન ફિઝિક્સ", "Basic Science", 4, "theory", "DI01C00061"),
    "DI01000131": ("Computer Programming Fundamentals (C)", "કમ્પ્યુટર પ્રોગ્રામિંગ ફંડામેન્ટલ્સ (C)", "Professional Core", 4, "programming", "DI01C00131"),
    "DI01000141": ("Computer Basics and Static Web Page Designing", "કમ્પ્યુટર બેઝિક્સ એન્ડ સ્ટેટિક વેબ પેજ ડિઝાઇનિંગ", "Engineering Science", 3, "practical", "DI01C00141"),
    "DI01000151": ("Basics of Electronics", "બેઝિક્સ ઓફ ઇલેક્ટ્રોનિક્સ", "Engineering Science", 3, "theory", "DI01C00151"),
    # Computer Sem 2 (2024-25)
    "DI02000101": ("Scripting Language (Python)", "સ્ક્રિપ્ટિંગ લેંગ્વેજ (Python)", "Professional Core", 4, "programming", "DI02C00101"),
    "DI02000091": ("Electronics Workshop and Practice", "ઇલેક્ટ્રોનિક્સ વર્કશોપ એન્ડ પ્રેક્ટિસ", "Engineering Science", 3, "practical", "DI02C00091"),
    "DI02000011": ("Applied Mathematics", "એપ્લાઇડ મેથેમેટિક્સ", "Basic Science", 4, "theory", "DI02C00011"),
    "DI01000071": ("Engineering Chemistry", "એન્જિનિયરિંગ કેમિસ્ટ્રી", "Basic Science", 4, "theory", "DI01C00071"),
    "DI02000051": ("Environmental Sustainability", "એન્વાયર્નમેન્ટલ સસ્ટેનેબિલિટી", "Engineering Science", 2, "theory", "DI02C00051"),
    "DI02000061": ("Indian Constitution", "ભારતીય બંધારણ", "Audit Course", 0, "theory", "DI02C00061"),
    "DI02000131": ("Contributor Personality Development", "કન્ટ્રિબ્યુટર પર્સનાલિટી ડેવલપમેન્ટ", "Humanities (Elective)", 3, "theory", "DI02C00131"),
    "DI02000141": ("Integrated Personality Development Course", "ઇન્ટિગ્રેટેડ પર્સનાલિટી ડેવલપમેન્ટ કોર્સ", "Humanities (Elective)", 3, "theory", "DI02C00141"),
    "DI02000151": ("Essence of Indian Knowledge and Tradition", "એસેન્સ ઓફ ઇન્ડિયન નોલેજ એન્ડ ટ્રેડિશન", "Humanities (Elective)", 3, "theory", "DI02C00151"),
    # Computer Sem 3 (2025-26 scheme)
    "DI03000011": ("Digital Electronics Fundamentals", "ડિજિટલ ઇલેક્ટ્રોનિક્સ ફંડામેન્ટલ્સ", "Engineering Science", 3, "theory", None),
    "DI03000021": ("Data Structures", "ડેટા સ્ટ્રક્ચર્સ", "Professional Core", 4, "programming", None),
    "DI03000031": ("Relational Database Management System", "રિલેશનલ ડેટાબેઝ મેનેજમેન્ટ સિસ્ટમ", "Professional Core", 4, "programming", None),
    "DI03000041": ("Fundamentals of Operating System", "ફંડામેન્ટલ્સ ઓફ ઓપરેટિંગ સિસ્ટમ", "Professional Core", 4, "theory", None),
    "DI03000051": ("Computer Networks", "કમ્પ્યુટર નેટવર્ક્સ", "Professional Core", 4, "theory", None),
    "DI03000061": ("Responsive Web Page Design", "રિસ્પોન્સિવ વેબ પેજ ડિઝાઇન", "Professional Core", 3, "practical", None),
    # Computer Sem 4 (2025-26 scheme)
    "DI04000011": ("Software Engineering", "સોફ્ટવેર એન્જિનિયરિંગ", "Professional Core", 4, "theory", None),
    "DI04000021": ("Object Oriented Programming - Java", "ઓબ્જેક્ટ ઓરિએન્ટેડ પ્રોગ્રામિંગ - જાવા", "Professional Core", 4, "programming", None),
    "DI04000031": ("Introduction to NoSQL", "નોએસક્યુએલનો પરિચય", "Professional Core", 3, "practical", None),
    "DI04007011": ("Introduction to Web Development", "વેબ ડેવલપમેન્ટનો પરિચય", "Professional Core", 4, "programming", None),
    # Computer Sem 5 (2026-27): only the provided/approved subject is added.
    "DI05007021": ("Information Security", None, "Professional Core", 4, "theory", None),
}
# branch key -> {semester: [subject codes in display order]}
BRANCH_SEMS = {
    "computer": {
        1: ["DI01000131", "DI01000151", "DI01000021", "DI01000061", "DI01000031", "DI01000141"],
        2: ["DI02000101", "DI02000091", "DI02000011", "DI01000071", "DI02000051", "DI02000061",
            "DI02000131", "DI02000141", "DI02000151"],
        3: ["DI03000021", "DI03000011", "DI03000031", "DI03000041", "DI03000051", "DI03000061"],
        4: ["DI04000021", "DI04000011", "DI04007011", "DI04000031"],
        5: ["DI05007021"],
    },
}

FONT_MAP = [
    (re.compile(r'font-family="Arial, Helvetica, sans-serif"'), 'font-family="DejaVu Sans"'),
    (re.compile(r'font-family="DejaVu Sans Mono, Consolas, monospace"'), 'font-family="DejaVu Sans Mono"'),
]


def clean_svg(svg):
    for rx, rep in FONT_MAP:
        svg = rx.sub(rep, svg)
    return svg


def main():
    global OUT
    if "--out" in sys.argv:
        OUT = os.path.abspath(sys.argv[sys.argv.index("--out") + 1])
    if os.path.isdir(OUT):
        shutil.rmtree(OUT)
    os.makedirs(os.path.join(OUT, "subjects"))
    os.makedirs(os.path.join(OUT, "units"))

    # find finished subjects
    done = {}
    for sj in glob.glob(os.path.join(CONTENT, "*", "sem*", "*", "subject.json")):
        s = json.load(open(sj, encoding="utf-8"))
        done[s["code"]] = (os.path.dirname(sj), s)

    total_units = 0
    for code, (d, s) in done.items():
        units = []
        for u in s["units"]:
            fp = os.path.join(d, u.get("file") or f'unit{u["no"]}.json')
            if not os.path.exists(fp):
                continue
            unit = json.load(open(fp, encoding="utf-8"))
            svgs = {}
            for dg in unit.get("diagrams", []):
                with open(os.path.join(d, "diagrams", dg["id"] + ".svg"), encoding="utf-8") as f:
                    svgs[dg["id"]] = clean_svg(f.read())
            for sec in unit.get("notes", []):          # no star / key-point marks in the app (user request)
                for it in sec.get("items", []):
                    it.pop("key", None)
            unit["svgs"] = svgs
            with open(os.path.join(OUT, "units", f'{code}_u{u["no"]}.json'), "w", encoding="utf-8") as f:
                json.dump(unit, f, ensure_ascii=False, separators=(",", ":"))
            units.append(u["no"])
            total_units += 1
        s = dict(s)
        s["available_units"] = units
        s.setdefault("languages", ["en", "gu"])
        s.setdefault("code_lang", "c" if s.get("type") == "programming" else None)
        with open(os.path.join(OUT, "subjects", code + ".json"), "w", encoding="utf-8") as f:
            json.dump(s, f, ensure_ascii=False, separators=(",", ":"))

    subjects = {}
    for code, (en, gu, cat, cr, typ, alt) in SUBJECTS.items():
        avail = code in done
        subjects[code] = {
            "code": code, "alt_code": alt, "name": {"en": en, **({"gu": gu} if gu else {})}, "category": cat,
            "credits": cr, "type": typ, "status": "available" if avail else "soon",
            "units": len(done[code][1]["units"]) if avail else 0,
            "languages": done[code][1].get("languages", ["en", "gu"]) if avail else ["en"],
        }
    catalog = {
        "version": 1,
        "syllabus_year": "2024-25",
        "branches": [
            {"code": c, "key": k, "name": {"en": en, "gu": gu}, "icon": ic, "color": col,
             "semesters": {str(n): BRANCH_SEMS.get(k, {}).get(n, []) for n in range(1, 7)}}
            for c, k, en, gu, ic, col in BRANCHES
        ],
        "subjects": subjects,
    }
    files = {}
    for fp in sorted(glob.glob(os.path.join(OUT, "*", "*.json"))):
        rel = os.path.relpath(fp, OUT).replace(os.sep, "/")
        files[rel] = hashlib.sha1(open(fp, "rb").read()).hexdigest()[:12]
    catalog["files"] = files
    catalog["generated"] = time.strftime("%Y-%m-%d %H:%M")
    with open(os.path.join(OUT, "catalog.json"), "w", encoding="utf-8") as f:
        json.dump(catalog, f, ensure_ascii=False, separators=(",", ":"))

    # app bundle (only with --app-assets): catalog + subject files as offline fallback
    if "--app-assets" not in sys.argv:
        pass
    elif os.path.isdir(APP_ASSETS):
        shutil.rmtree(APP_ASSETS)
    if "--app-assets" in sys.argv:
        shutil.copytree(os.path.join(OUT, "subjects"), os.path.join(APP_ASSETS, "subjects"))
        shutil.copy(os.path.join(OUT, "catalog.json"), APP_ASSETS)
        print("app assets refreshed")

    size = sum(os.path.getsize(p) for p in glob.glob(os.path.join(OUT, "**", "*.json"), recursive=True))
    print(f"subjects done: {len(done)}  units: {total_units}  catalog subjects: {len(subjects)}  "
          f"size: {size // 1024} KB -> {OUT}")


if __name__ == "__main__":
    main()
