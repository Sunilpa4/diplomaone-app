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
    "DI02000051": ("Environmental Sustainability", "પર્યાવરણીય ટકાઉપણું", "Engineering Science", 2, "theory", "DI02C00051"),
    "DI01000111": ("Engineering Graphics", None, "Engineering Science", 3, "theory", "DI01C00111"),
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
    # Computer Sem 4 (2025-26): Cloud Computing - English-only release
    "DI04000041": ("Cloud Computing", None, "Professional Elective", 4, "theory", None),
    # Computer Sem 5 (2026-27): the two provided main-subject syllabi.
    "DI05007011": ("Computer Hardware Architecture and System Maintenance", None, "Professional Core", 4, "theory", None),
    "DI05007021": ("Information Security", None, "Professional Core", 4, "theory", None),
}
# branch key -> {semester: [subject codes in display order]}
BRANCH_SEMS = {
    "computer": {
        1: ["DI01000131", "DI01000151", "DI01000021", "DI01000061", "DI01000031", "DI01000141"],
        2: ["DI02000101", "DI02000091", "DI02000011", "DI01000071", "DI02000051", "DI02000061",
            "DI02000131", "DI02000141", "DI02000151"],
        3: ["DI03000021", "DI03000011", "DI03000031", "DI03000041", "DI03000051", "DI03000061"],
        4: ["DI04000021", "DI04000011", "DI04007011", "DI04000031", "DI04000041"],
        5: ["DI05007011", "DI05007021"],
    },
}

# DiplomaOne registration: DI01000191 mechanical semester 1
if 'DI01000191' not in SUBJECTS:
    SUBJECTS['DI01000191'] = ('Elements of Mechanical Engineering', 'મેકેનિકલ એન્જિનિયરિંગના મૂળતત્ત્વો', 'Professional Core', 4, 'theory', None)
_mechanical_sem1 = BRANCH_SEMS.setdefault('mechanical', {}).setdefault(1, [])
if 'DI01000191' not in _mechanical_sem1:
    _mechanical_sem1.append('DI01000191')

# DiplomaOne registration: DI03000141 mechanical semester 3
if 'DI03000141' not in SUBJECTS:
    SUBJECTS['DI03000141'] = ('Theory of Machines and Mechanisms', 'યંત્રો અને મિકેનિઝમ્સનો સિદ્ધાંત', 'Professional Core', 4, 'theory', None)
_mechanical_sem3 = BRANCH_SEMS.setdefault('mechanical', {}).setdefault(3, [])
if 'DI03000141' not in _mechanical_sem3:
    _mechanical_sem3.append('DI03000141')

# DiplomaOne registration: DI03000161 mechanical semester 3
if 'DI03000161' not in SUBJECTS:
    SUBJECTS['DI03000161'] = ('Manufacturing Engineering-I', 'ઉત્પાદન ઇજનેરી-I', 'Professional Core', 4, 'theory', None)
_mechanical_sem3 = BRANCH_SEMS.setdefault('mechanical', {}).setdefault(3, [])
if 'DI03000161' not in _mechanical_sem3:
    _mechanical_sem3.append('DI03000161')

# DiplomaOne registration: DI03000171 mechanical semester 3
if 'DI03000171' not in SUBJECTS:
    SUBJECTS['DI03000171'] = ('Fluid Mechanics and Hydraulic Machinery', 'પ્રવાહી યાંત્રિકી અને હાઇડ્રોલિક મશીનરી', 'Professional Core', 4, 'theory', None)
_mechanical_sem3 = BRANCH_SEMS.setdefault('mechanical', {}).setdefault(3, [])
if 'DI03000171' not in _mechanical_sem3:
    _mechanical_sem3.append('DI03000171')

# DiplomaOne registration: DI03019011 mechanical semester 3
if 'DI03019011' not in SUBJECTS:
    SUBJECTS['DI03019011'] = ('Engineering Thermodynamics', 'ઇજનેરી ઉષ્માગતિશાસ્ત્ર', 'Professional Core', 3, 'theory', None)
_mechanical_sem3 = BRANCH_SEMS.setdefault('mechanical', {}).setdefault(3, [])
if 'DI03019011' not in _mechanical_sem3:
    _mechanical_sem3.append('DI03019011')

# DiplomaOne registration: DI03000151 mechanical semester 3
if 'DI03000151' not in SUBJECTS:
    SUBJECTS['DI03000151'] = ('Measurements and Metrology', 'માપન અને માપવિજ્ઞાન', 'Professional Core', 4, 'theory', None)
_mechanical_sem3 = BRANCH_SEMS.setdefault('mechanical', {}).setdefault(3, [])
if 'DI03000151' not in _mechanical_sem3:
    _mechanical_sem3.append('DI03000151')

# DiplomaOne registration: DI03000201 mechanical semester 3
if 'DI03000201' not in SUBJECTS:
    SUBJECTS['DI03000201'] = ('Basics of Applied Mechanics', 'પ્રાયોગિક યાંત્રિકીના પાયાના સિદ્ધાંતો', 'Engineering Science', 3, 'theory', None)
_mechanical_sem3 = BRANCH_SEMS.setdefault('mechanical', {}).setdefault(3, [])
if 'DI03000201' not in _mechanical_sem3:
    _mechanical_sem3.append('DI03000201')

# DiplomaOne registration: DI04019011 mechanical semester 4
if 'DI04019011' not in SUBJECTS:
    SUBJECTS['DI04019011'] = ('Thermal Engineering - I', 'થર્મલ ઇજનેરી - I', 'Professional Core', 4, 'theory', None)
_mechanical_sem4 = BRANCH_SEMS.setdefault('mechanical', {}).setdefault(4, [])
if 'DI04019011' not in _mechanical_sem4:
    _mechanical_sem4.append('DI04019011')

# DiplomaOne registration: DI04000241 mechanical semester 4
if 'DI04000241' not in SUBJECTS:
    SUBJECTS['DI04000241'] = ('Manufacturing Engineering - II', 'મેન્યુફેક્ચરિંગ ઇજનેરી - II', 'Professional Core', 4, 'theory', None)
_mechanical_sem4 = BRANCH_SEMS.setdefault('mechanical', {}).setdefault(4, [])
if 'DI04000241' not in _mechanical_sem4:
    _mechanical_sem4.append('DI04000241')

# DiplomaOne registration: DI04000251 mechanical semester 4
if 'DI04000251' not in SUBJECTS:
    SUBJECTS['DI04000251'] = ('Design of Machine Elements', 'મશીન એલિમેન્ટ્સની ડિઝાઇન', 'Professional Core', 4, 'theory', None)
_mechanical_sem4 = BRANCH_SEMS.setdefault('mechanical', {}).setdefault(4, [])
if 'DI04000251' not in _mechanical_sem4:
    _mechanical_sem4.append('DI04000251')

# DiplomaOne registration: DI05019021 mechanical semester 5
if 'DI05019021' not in SUBJECTS:
    SUBJECTS['DI05019021'] = ('Thermal Engineering - II', 'થર્મલ ઇજનેરી - II', 'Professional Core', 5, 'theory', None)
_mechanical_sem5 = BRANCH_SEMS.setdefault('mechanical', {}).setdefault(5, [])
if 'DI05019021' not in _mechanical_sem5:
    _mechanical_sem5.append('DI05019021')

# DiplomaOne registration: DI05019011 mechanical semester 5
if 'DI05019011' not in SUBJECTS:
    SUBJECTS['DI05019011'] = ('Manufacturing Engineering - III', 'મેન્યુફેક્ચરિંગ ઇજનેરી - III', 'Professional Core', 5, 'theory', None)
_mechanical_sem5 = BRANCH_SEMS.setdefault('mechanical', {}).setdefault(5, [])
if 'DI05019011' not in _mechanical_sem5:
    _mechanical_sem5.append('DI05019011')

# DiplomaOne registration: DI01000081 electrical semester 1
if 'DI01000081' not in SUBJECTS:
    SUBJECTS['DI01000081'] = ('DC Circuit', 'ડી.સી. સર્કિટ', 'Professional Core', 4, 'theory', None)
_electrical_sem1 = BRANCH_SEMS.setdefault('electrical', {}).setdefault(1, [])
if 'DI01000081' not in _electrical_sem1:
    _electrical_sem1.append('DI01000081')

# DiplomaOne registration: DI01009011 electrical semester 1
if 'DI01009011' not in SUBJECTS:
    SUBJECTS['DI01009011'] = ('Electronics Devices & Circuits', 'ઇલેક્ટ્રોનિક્સ Devices અને Circuits', 'Engineering Science', 3, 'theory', None)
_electrical_sem1 = BRANCH_SEMS.setdefault('electrical', {}).setdefault(1, [])
if 'DI01009011' not in _electrical_sem1:
    _electrical_sem1.append('DI01009011')

# DiplomaOne registration: DI01000091 electrical semester 1
if 'DI01000091' not in SUBJECTS:
    SUBJECTS['DI01000091'] = ('Fundamentals of Information and Communication Technology (FICT)', 'ફંડામેન્ટલ્સ ઑફ ICT', 'Engineering Science', 3, 'practical', None)
_electrical_sem1 = BRANCH_SEMS.setdefault('electrical', {}).setdefault(1, [])
if 'DI01000091' not in _electrical_sem1:
    _electrical_sem1.append('DI01000091')

# DiplomaOne registration: DI02000161 electrical semester 2
if 'DI02000161' not in SUBJECTS:
    SUBJECTS['DI02000161'] = ('Fundamental of Digital Electronics', 'ડિજિટલ ઇલેક્ટ્રોનિક્સના પાયા', 'Engineering Science', 3, 'theory', None)
_electrical_sem2 = BRANCH_SEMS.setdefault('electrical', {}).setdefault(2, [])
if 'DI02000161' not in _electrical_sem2:
    _electrical_sem2.append('DI02000161')

# DiplomaOne registration: DI02000171 electrical semester 2
if 'DI02000171' not in SUBJECTS:
    SUBJECTS['DI02000171'] = ('AC Fundamental', 'એસી ફંડામેન્ટલ', 'Professional Core', 4, 'theory', None)
_electrical_sem2 = BRANCH_SEMS.setdefault('electrical', {}).setdefault(2, [])
if 'DI02000171' not in _electrical_sem2:
    _electrical_sem2.append('DI02000171')

# DiplomaOne registration: DI03000081 electrical semester 3
if 'DI03000081' not in SUBJECTS:
    SUBJECTS['DI03000081'] = ('Electrical Machines I', 'ઇલેક્ટ્રિકલ મશીન્સ – I', 'Professional Core', 4, 'theory', None)
_electrical_sem3 = BRANCH_SEMS.setdefault('electrical', {}).setdefault(3, [])
if 'DI03000081' not in _electrical_sem3:
    _electrical_sem3.append('DI03000081')

# DiplomaOne registration: DI03000091 electrical semester 3
if 'DI03000091' not in SUBJECTS:
    SUBJECTS['DI03000091'] = ('Electrical Instrumentation', 'ઇલેક્ટ્રિકલ ઇન્સ્ટ્રુમેન્ટેશન', 'Professional Core', 4, 'theory', None)
_electrical_sem3 = BRANCH_SEMS.setdefault('electrical', {}).setdefault(3, [])
if 'DI03000091' not in _electrical_sem3:
    _electrical_sem3.append('DI03000091')

# DiplomaOne registration: DI03000101 electrical semester 3
if 'DI03000101' not in SUBJECTS:
    SUBJECTS['DI03000101'] = ('Electrical Power Transmission & Distribution', 'વિદ્યુત શક્તિ પ્રસારણ અને વિતરણ', 'Professional Core', 4, 'theory', None)
_electrical_sem3 = BRANCH_SEMS.setdefault('electrical', {}).setdefault(3, [])
if 'DI03000101' not in _electrical_sem3:
    _electrical_sem3.append('DI03000101')

# DiplomaOne registration: DI03009011 electrical semester 3
if 'DI03009011' not in SUBJECTS:
    SUBJECTS['DI03009011'] = ('Electrical Wiring Estimating & Contracting', 'ઇલેક્ટ્રિકલ વાયરિંગ અંદાજ તથા કોન્ટ્રાક્ટિંગ', 'Professional Core', 4, 'theory', None)
_electrical_sem3 = BRANCH_SEMS.setdefault('electrical', {}).setdefault(3, [])
if 'DI03009011' not in _electrical_sem3:
    _electrical_sem3.append('DI03009011')

# DiplomaOne registration: DI03009021 electrical semester 3
if 'DI03009021' not in SUBJECTS:
    SUBJECTS['DI03009021'] = ('Electrical Power Generation', 'વિદ્યુત શક્તિ ઉત્પાદન', 'Professional Core', 3, 'theory', None)
_electrical_sem3 = BRANCH_SEMS.setdefault('electrical', {}).setdefault(3, [])
if 'DI03009021' not in _electrical_sem3:
    _electrical_sem3.append('DI03009021')

# DiplomaOne registration: DI04000171 electrical semester 4
if 'DI04000171' not in SUBJECTS:
    SUBJECTS['DI04000171'] = ('Microcontroller & its Applications', 'માઇક્રોકન્ટ્રોલર તથા તેની એપ્લિકેશન્સ', 'Professional Core', 4, 'theory', None)
_electrical_sem4 = BRANCH_SEMS.setdefault('electrical', {}).setdefault(4, [])
if 'DI04000171' not in _electrical_sem4:
    _electrical_sem4.append('DI04000171')

# DiplomaOne registration: DI04000321 electrical semester 4
if 'DI04000321' not in SUBJECTS:
    SUBJECTS['DI04000321'] = ('Electrical Machines – II', 'ઇલેક્ટ્રિકલ મશીન્સ – II', 'Professional Core', 4, 'theory', None)
_electrical_sem4 = BRANCH_SEMS.setdefault('electrical', {}).setdefault(4, [])
if 'DI04000321' not in _electrical_sem4:
    _electrical_sem4.append('DI04000321')

# DiplomaOne registration: DI04009011 electrical semester 4
if 'DI04009011' not in SUBJECTS:
    SUBJECTS['DI04009011'] = ('Substation Engineering', 'સબસ્ટેશન એન્જિનિયરિંગ', 'Professional Core', 4, 'theory', None)
_electrical_sem4 = BRANCH_SEMS.setdefault('electrical', {}).setdefault(4, [])
if 'DI04009011' not in _electrical_sem4:
    _electrical_sem4.append('DI04009011')

# DiplomaOne registration: DI05000171 electrical semester 5
if 'DI05000171' not in SUBJECTS:
    SUBJECTS['DI05000171'] = ('Power Electronics Converters', 'પાવર ઇલેક્ટ્રોનિક્સ કન્વર્ટર્સ', 'Professional Core', 5, 'theory', None)
_electrical_sem5 = BRANCH_SEMS.setdefault('electrical', {}).setdefault(5, [])
if 'DI05000171' not in _electrical_sem5:
    _electrical_sem5.append('DI05000171')

# DiplomaOne registration: DI05009011 electrical semester 5
if 'DI05009011' not in SUBJECTS:
    SUBJECTS['DI05009011'] = ('Switchgear and Protection', 'સ્વિચગિયર અને પ્રોટેક્શન', 'Professional Core', 5, 'theory', None)
_electrical_sem5 = BRANCH_SEMS.setdefault('electrical', {}).setdefault(5, [])
if 'DI05009011' not in _electrical_sem5:
    _electrical_sem5.append('DI05009011')

# DiplomaOne registration: DI01005011 chemical semester 1
if 'DI01005011' not in SUBJECTS:
    SUBJECTS['DI01005011'] = ('Plant Utilities', 'પ્લાન્ટ યુટિલિટીઝ', 'Professional Core', 1, 'theory', None)
_chemical_sem1 = BRANCH_SEMS.setdefault('chemical', {}).setdefault(1, [])
if 'DI01005011' not in _chemical_sem1:
    _chemical_sem1.append('DI01005011')

# DiplomaOne registration: DI01005021 chemical semester 1
if 'DI01005021' not in SUBJECTS:
    SUBJECTS['DI01005021'] = ('Material Science and Technology', 'મટીરિયલ સાયન્સ અને ટેક્નોલોજી', 'Engineering Science', 1, 'theory', None)
_chemical_sem1 = BRANCH_SEMS.setdefault('chemical', {}).setdefault(1, [])
if 'DI01005021' not in _chemical_sem1:
    _chemical_sem1.append('DI01005021')

# DiplomaOne registration: DI02005021 chemical semester 2
if 'DI02005021' not in SUBJECTS:
    SUBJECTS['DI02005021'] = ('Mechanical Operation','મેકેનિકલ ઓપરેશન','Chemical Engineering',2,'theory',None)
_chemical_sem2 = BRANCH_SEMS.setdefault('chemical',{}).setdefault(2,[])
if 'DI02005021' not in _chemical_sem2:
    _chemical_sem2.append('DI02005021')

# DiplomaOne registration: DI02005011 chemical semester 2
if 'DI02005011' not in SUBJECTS:
    SUBJECTS['DI02005011'] = ('Basic Chemical Engineering Calculations','બેઝિક કેમિકલ એન્જિનિયરિંગ કેલ્ક્યુલેશન્સ','Engineering Science',2,'theory',None)
_chemical_sem2 = BRANCH_SEMS.setdefault('chemical',{}).setdefault(2,[])
if 'DI02005011' not in _chemical_sem2:
    _chemical_sem2.append('DI02005011')

# DiplomaOne registration: DI03005041 chemical semester 3
if 'DI03005041' not in SUBJECTS:
    SUBJECTS['DI03005041'] = ('Chemical Process Technology – I','કેમિકલ પ્રોસેસ ટેક્નોલોજી – I','Professional Core',3,'theory',None)
_chemical_sem3 = BRANCH_SEMS.setdefault('chemical',{}).setdefault(3,[])
if 'DI03005041' not in _chemical_sem3:
    _chemical_sem3.append('DI03005041')

# DiplomaOne registration: DI04005011 chemical semester 4
if 'DI04005011' not in SUBJECTS:
    SUBJECTS['DI04005011'] = ('Chemical Process Technology – II','કેમિકલ પ્રોસેસ ટેક્નોલોજી – II','Professional Core',4,'theory',None)
_chemical_sem4 = BRANCH_SEMS.setdefault('chemical',{}).setdefault(4,[])
if 'DI04005011' not in _chemical_sem4:
    _chemical_sem4.append('DI04005011')

# DiplomaOne registration: DI05005051 chemical semester 5
if 'DI05005051' not in SUBJECTS:
    SUBJECTS['DI05005051'] = ('Fertilizer Technology','ફર્ટિલાઇઝર ટેક્નોલોજી','Professional Elective',5,'theory',None)
_chemical_sem5 = BRANCH_SEMS.setdefault('chemical',{}).setdefault(5,[])
if 'DI05005051' not in _chemical_sem5:
    _chemical_sem5.append('DI05005051')

# DiplomaOne registration: DI05005031 chemical semester 5
if 'DI05005031' not in SUBJECTS:
    SUBJECTS['DI05005031'] = ('Chemical Reaction Engineering','રાસાયણિક પ્રક્રિયા ઇજનેરી','Professional Elective',4,'theory',None)
_chemical_sem5 = BRANCH_SEMS.setdefault('chemical',{}).setdefault(5,[])
if 'DI05005031' not in _chemical_sem5:
    _chemical_sem5.append('DI05005031')

# DiplomaOne registration: DI03005031 chemical semester 3
if 'DI03005031' not in SUBJECTS:
    SUBJECTS['DI03005031'] = ('Process Heat Transfer','પ્રોસેસ હીટ ટ્રાન્સફર','Core',3,'theory',None)
_chemical_sem3 = BRANCH_SEMS.setdefault('chemical',{}).setdefault(3,[])
if 'DI03005031' not in _chemical_sem3:
    _chemical_sem3.append('DI03005031')

# DiplomaOne registration: DI03005021 chemical semester 3
if 'DI03005021' not in SUBJECTS:
    SUBJECTS['DI03005021'] = ('Fluid Flow Operation','ફ્લુઇડ ફ્લો ઓપરેશન','Core',3,'theory',None)
_chemical_sem3 = BRANCH_SEMS.setdefault('chemical',{}).setdefault(3,[])
if 'DI03005021' not in _chemical_sem3:
    _chemical_sem3.append('DI03005021')

# DiplomaOne registration: DI03005061 chemical semester 3
if 'DI03005061' not in SUBJECTS:
    SUBJECTS['DI03005061'] = ('Process Calculation','પ્રોસેસ કેલ્ક્યુલેશન','Core',3,'theory',None)
_chemical_sem3 = BRANCH_SEMS.setdefault('chemical',{}).setdefault(3,[])
if 'DI03005061' not in _chemical_sem3:
    _chemical_sem3.append('DI03005061')

# DiplomaOne registration: DI03005011 chemical semester 3
if 'DI03005011' not in SUBJECTS:
    SUBJECTS['DI03005011'] = ('Basics of Process Instrumentations','બેઝિક્સ ઑફ પ્રોસેસ ઇન્સ્ટ્રુમેન્ટેશન્સ','Core',3,'theory',None)
_chemical_sem3 = BRANCH_SEMS.setdefault('chemical',{}).setdefault(3,[])
if 'DI03005011' not in _chemical_sem3:
    _chemical_sem3.append('DI03005011')

# DiplomaOne registration: DI04005021 chemical semester 4
if 'DI04005021' not in SUBJECTS:
    SUBJECTS['DI04005021'] = ('Mass Transfer-I','માસ ટ્રાન્સફર–I','Core',4,'theory',None)
_chemical_sem4 = BRANCH_SEMS.setdefault('chemical',{}).setdefault(4,[])
if 'DI04005021' not in _chemical_sem4:
    _chemical_sem4.append('DI04005021')

# DiplomaOne registration: DI04005041 chemical semester 4
if 'DI04005041' not in SUBJECTS:
    SUBJECTS['DI04005041'] = ('Chemical Engineering Thermodynamics','કેમિકલ એન્જિનિયરિંગ થર્મોડાયનેમિક્સ','Core',4,'theory',None)
_chemical_sem4 = BRANCH_SEMS.setdefault('chemical',{}).setdefault(4,[])
if 'DI04005041' not in _chemical_sem4:
    _chemical_sem4.append('DI04005041')

# DiplomaOne registration: DI04005071 chemical semester 4
if 'DI04005071' not in SUBJECTS:
    SUBJECTS['DI04005071'] = ('Petroleum Refining and Petroleum Technology','પેટ્રોલિયમ રિફાઇનિંગ તથા પેટ્રોલિયમ ટેકનોલોજી','Professional Elective',4,'theory',None)
_chemical_sem4 = BRANCH_SEMS.setdefault('chemical',{}).setdefault(4,[])
if 'DI04005071' not in _chemical_sem4:
    _chemical_sem4.append('DI04005071')

# DiplomaOne registration: DI05005011 chemical semester 5
if 'DI05005011' not in SUBJECTS:
    SUBJECTS['DI05005011'] = ('Mass Transfer - II','માસ ટ્રાન્સફર-II','Professional Core',4,'theory',None)
_chemical_sem5 = BRANCH_SEMS.setdefault('chemical',{}).setdefault(5,[])
if 'DI05005011' not in _chemical_sem5:
    _chemical_sem5.append('DI05005011')

# DiplomaOne registration: DI05005021 chemical semester 5
if 'DI05005021' not in SUBJECTS:
    SUBJECTS['DI05005021'] = ('Chemical Engineering Plant Economics','કેમિકલ એન્જિનિયરિંગ પ્લાન્ટ ઇકોનોમિક્સ','Professional Core',4,'theory',None)
_chemical_sem5 = BRANCH_SEMS.setdefault('chemical',{}).setdefault(5,[])
if 'DI05005021' not in _chemical_sem5:
    _chemical_sem5.append('DI05005021')

# DiplomaOne registration: DI02000121 mechanical semester 2 (English-only subject)
if 'DI02000121' not in SUBJECTS:
    SUBJECTS['DI02000121'] = ('Mechanical Drafting',None,'Professional Core',4,'theory',None)
_mechanical_sem2 = BRANCH_SEMS.setdefault('mechanical',{}).setdefault(2,[])
if 'DI02000121' not in _mechanical_sem2:
    _mechanical_sem2.append('DI02000121')

# DiplomaOne registration: DI01006021 civil semester 1
if 'DI01006021' not in SUBJECTS:
    SUBJECTS['DI01006021'] = ('Construction Material','કન્સ્ટ્રક્શન મટીરિયલ','Engineering Science',3,'theory',None)
_civil_sem1 = BRANCH_SEMS.setdefault('civil',{}).setdefault(1,[])
if 'DI01006021' not in _civil_sem1:
    _civil_sem1.append('DI01006021')

# DiplomaOne registration: DI01006011 civil semester 1 (English-only subject)
if 'DI01006011' not in SUBJECTS:
    SUBJECTS['DI01006011'] = ('Civil Engineering Drawing',None,'Professional Core',4,'theory',None)
_civil_sem1 = BRANCH_SEMS.setdefault('civil',{}).setdefault(1,[])
if 'DI01006011' not in _civil_sem1:
    _civil_sem1.append('DI01006011')

# DiplomaOne registration: DI02000071 civil + environmental semester 2
if 'DI02000071' not in SUBJECTS:
    SUBJECTS['DI02000071'] = ('Engineering Mechanics','એન્જિનિયરિંગ મિકેનિક્સ','Professional Core',4,'theory',None)
for _br in ('civil','environmental'):
    _bs = BRANCH_SEMS.setdefault(_br,{}).setdefault(2,[])
    if 'DI02000071' not in _bs:
        _bs.append('DI02000071')

# DiplomaOne registration: DI02006011 civil semester 2
if 'DI02006011' not in SUBJECTS:
    SUBJECTS['DI02006011'] = ('Basic Surveying','મૂળભૂત સર્વેક્ષણ','Engineering Science',3,'theory',None)
_civil_sem2 = BRANCH_SEMS.setdefault('civil',{}).setdefault(2,[])
if 'DI02006011' not in _civil_sem2:
    _civil_sem2.append('DI02006011')


# Chemistry courses: the GTU syllabus assigns shared subject codes to several branches.
# The first seven units follow each course's syllabus; units 8 and 9 are supplementary.
if 'DI01000161' not in SUBJECTS:
    SUBJECTS['DI01000161'] = ('Basic Chemistry', 'બેઝિક કેમિસ્ટ્રી', 'Basic Science', 4, 'theory', None)
for _key, _sem in [('chemical', 1), ('textile_proc', 1), ('ic', 2), ('textile_mfg', 2), ('robotics', 2), ('printing', 2)]:
    _courses = BRANCH_SEMS.setdefault(_key, {}).setdefault(_sem, [])
    if 'DI01000161' not in _courses:
        _courses.append('DI01000161')
for _key, _sem in [('electrical', 1), ('it', 1), ('power', 1), ('biomedical', 2), ('computer', 2), ('ec', 2), ('cse', 2), ('ict', 2)]:
    _courses = BRANCH_SEMS.setdefault(_key, {}).setdefault(_sem, [])
    if 'DI01000071' not in _courses:
        _courses.append('DI01000071')

FONT_MAP = [
    (re.compile(r'font-family="Arial, Helvetica, sans-serif"'), 'font-family="DejaVu Sans"'),
    (re.compile(r'font-family="DejaVu Sans Mono, Consolas, monospace"'), 'font-family="DejaVu Sans Mono"'),
]


def clean_svg(svg):
    for rx, rep in FONT_MAP:
        svg = rx.sub(rep, svg)
    return svg


def normalize_for_app(unit):
    """Adapt newer rich-card layouts to the existing app without altering sources.

    Rich practical cards and reference text can be shown as note sections, which
    also preserves their inline diagrams in older versions of the app. Flat viva
    questions are wrapped in the grouped format understood by the app.
    """
    # Some source files use the field name as a tab id; older apps use "exam".
    if isinstance(unit.get("tabs"), list):
        tabs = ["exam" if tab == "exam_questions" else tab for tab in unit["tabs"]]
        unit["tabs"] = list(dict.fromkeys(tabs))

    # Some recent subjects store a single group as an object, while released
    # app readers require lists. Keep their rich HTML and identifiers intact.
    viva = unit.get("viva")
    if isinstance(viva, dict):
        if not isinstance(viva.get("items"), list) or not all(
            isinstance(item, dict) and "q" in item and "a" in item for item in viva["items"]
        ):
            raise ValueError("Unsupported grouped viva format")
        unit["viva"] = [viva]

    numericals = unit.get("numericals")
    if isinstance(numericals, dict):
        if not isinstance(numericals.get("items"), list) or not all(
            isinstance(item, dict) and "title" in item and "body" in item for item in numericals["items"]
        ):
            raise ValueError("Unsupported grouped numericals format")
        # The app's numericals tab expects question/answer pairs, not rich cards.
        unit["numericals"] = [dict(item, q=item["title"], a=item["body"]) for item in numericals["items"]]

    syntax = unit.get("syntax")
    if isinstance(syntax, dict):
        if not isinstance(syntax.get("items"), list) or not all(
            isinstance(item, dict) and "name" in item and "body" in item for item in syntax["items"]
        ):
            raise ValueError("Unsupported grouped reference format")
        # Formulae here are rich HTML, not programming syntax. Existing app
        # versions can display them faithfully as expandable note cards.
        cards = [dict(item, h=item["name"]) for item in syntax["items"]]
        if cards:
            unit.setdefault("notes", []).append({"title": syntax.get("title", {"en": "Reference and formulas", "gu": "સંદર્ભ અને સૂત્રો"}), "items": cards})
        unit.pop("syntax")
        if isinstance(unit.get("tabs"), list):
            unit["tabs"] = [tab for tab in unit["tabs"] if tab != "syntax"]
            if cards and "notes" not in unit["tabs"]:
                unit["tabs"].insert(0, "notes")

    programs = unit.get("programs")
    if isinstance(programs, list):
        rich = [p for p in programs if isinstance(p, dict) and p.get("format") == "rich_cards" and isinstance(p.get("items"), list)]
        if rich:
            unit.setdefault("notes", []).extend({"title": p["title"], "items": p["items"]} for p in rich)
            remaining = [p for p in programs if p not in rich]
            if remaining:
                unit["programs"] = remaining
            else:
                unit.pop("programs", None)
                unit["tabs"] = [tab for tab in unit.get("tabs", []) if tab != "programs"]

    syntax = unit.get("syntax")
    if isinstance(syntax, list) and syntax and all(isinstance(e, dict) and "title" in e and "body" in e and "items" not in e for e in syntax):
        unit.setdefault("notes", []).append({
            "title": {"en": "Reference and formulas", "gu": "સંદર્ભ અને સૂત્રો"},
            "items": [{"h": e["title"], "body": e["body"]} for e in syntax],
        })
        unit.pop("syntax")
        unit["tabs"] = [tab for tab in unit.get("tabs", []) if tab != "syntax"]

    viva = unit.get("viva")
    if isinstance(viva, list) and viva and all(isinstance(e, dict) and "q" in e and "a" in e and "items" not in e for e in viva):
        unit["viva"] = [{"title": {"en": "Viva questions", "gu": "વાઇવા પ્રશ્નો"}, "items": viva}]


# Engineering Mathematics (DI02000021) - the Semester 2 mathematics subject. The syllabus lists it
# for Electrical, Renewable Energy, Automation & Robotics, Instrumentation & Control and Power
# Electronics, but it is the semester-2 mathematics course every branch teaches, so it is listed in
# semester 2 of every branch (user decision, like Mathematics-I in semester 1).
SUBJECTS.setdefault("DI02000021", ("Engineering Mathematics", "એન્જિનિયરિંગ ગણિત",
                                   "Basic Science", 4, "theory", "DI02C00021"))
for _branch in BRANCHES:
    _sem2 = BRANCH_SEMS.setdefault(_branch[1], {}).setdefault(2, [])
    if "DI02000021" not in _sem2:
        _sem2.insert(0, "DI02000021")

# Environmental Sustainability (DI02000051) prints "Branch: ALL" in its syllabus, so it is listed in
# semester 2 of every diploma branch, just after Engineering Mathematics.
for _branch in BRANCHES:
    _sem2 = BRANCH_SEMS.setdefault(_branch[1], {}).setdefault(2, [])
    if "DI02000051" not in _sem2:
        _pos = _sem2.index("DI02000021") + 1 if "DI02000021" in _sem2 else len(_sem2)
        _sem2.insert(_pos, "DI02000051")

# Mathematics-I (DI01000021) is a common "Branch: All" subject - list it in semester 1 of every branch.
for _branch in BRANCHES:
    _sem1 = BRANCH_SEMS.setdefault(_branch[1], {}).setdefault(1, [])
    if "DI01000021" not in _sem1:
        _sem1.insert(0, "DI01000021")

# Applied Physics (DI01000121) is one subject with two home semesters: semester 1 for Civil,
# Environmental, Mining, Textile Manufacturing, Ceramic, Printing and Renewable Energy; semester 2 for
# Automobile, Chemical, Mechanical, Mechatronics, Textile Processing, Fabrication, Textile Design and
# Mechanical (CAD/CAM). The app carries ten of those branches, so it is listed in each of them at the
# semester printed in the PDF (subject.json records the split in "semester_by_branch").
SUBJECTS.setdefault("DI01000121", ("Applied Physics", "એપ્લાઇડ ફિઝિક્સ", "Basic Science", 4,
                                   "theory", None))
APPLIED_PHYSICS_BRANCHES = {
    1: ["civil", "environmental", "mining", "textile_mfg", "printing"],
    2: ["automobile", "chemical", "mechanical", "mechatronics", "textile_proc"],
}
for _sem, _keys in APPLIED_PHYSICS_BRANCHES.items():
    for _key in _keys:
        _lst = BRANCH_SEMS.setdefault(_key, {}).setdefault(_sem, [])
        if "DI01000121" not in _lst:
            _pos = _lst.index("DI01000021") + 1 if "DI01000021" in _lst else len(_lst)
            _lst.insert(_pos, "DI01000121")

# Communication Skills in English (DI01000031) prints "Branch: All" in its syllabus, so it is listed
# in semester 1 of every diploma branch. It sits just after Mathematics-I in the display order.
for _branch in BRANCHES:
    _sem1 = BRANCH_SEMS.setdefault(_branch[1], {}).setdefault(1, [])
    if "DI01000031" not in _sem1:
        _sem1.insert(_sem1.index("DI01000021") + 1 if "DI01000021" in _sem1 else 0, "DI01000031")

# Engineering Graphics (DI01000111) is the English-only drawing course of twelve branch programmes
# in semester 1 (the PDF names fifteen branches; the app does not carry Ceramic, Mechanical CAD/CAM
# or Fabrication as separate branches). It sits after Mathematics-I, like the other common subjects.
SUBJECTS.setdefault("DI01000111", ("Engineering Graphics", None, "Engineering Science", 3,
                                   "theory", "DI01C00111"))
ENGINEERING_GRAPHICS_BRANCHES = ["power", "robotics", "civil", "environmental", "mining", "chemical",
                                 "metallurgy", "plastic", "mechanical", "automobile", "mechatronics",
                                 "textile_proc"]
for _key in ENGINEERING_GRAPHICS_BRANCHES:
    _sem1 = BRANCH_SEMS.setdefault(_key, {}).setdefault(1, [])
    if "DI01000111" not in _sem1:
        _pos = _sem1.index("DI01000021") + 1 if "DI01000021" in _sem1 else len(_sem1)
        _sem1.insert(_pos, "DI01000111")

# Entrepreneurship & Start-up (DI04000081) prints "Branch: All" in its syllabus (Semester 4, MOPEC),
# so it is listed in semester 4 of every diploma branch.
SUBJECTS.setdefault("DI04000081", ("Entrepreneurship & Start-up", "એન્ટ્રપ્રિન્યોરશિપ અને સ્ટાર્ટ-અપ",
                                   "MOPEC", 3, "theory", None))
for _branch in BRANCHES:
    _sem4 = BRANCH_SEMS.setdefault(_branch[1], {}).setdefault(4, [])
    if "DI04000081" not in _sem4:
        _sem4.append("DI04000081")

# DiplomaOne registration: DI01000181 mechanical semester 1 (Engineering Materials Science, the
# subject built unit by unit in this branch: six units, both languages, 45 teaching hours).
if 'DI01000181' not in SUBJECTS:
    SUBJECTS['DI01000181'] = ('Engineering Materials Science', 'ઇજનેરી સામગ્રી વિજ્ઞાન',
                              'Engineering Science', 4, 'theory', None)
_mechanical_sem1 = BRANCH_SEMS.setdefault('mechanical', {}).setdefault(1, [])
if 'DI01000181' not in _mechanical_sem1:
    _mechanical_sem1.append('DI01000181')


# Civil subjects registered in the November batch.
for _code, _en, _gu, _cat, _credits, _sem in [
    ('DI03006011', 'Construction Technology', 'બાંધકામ ટેકનોલોજી', 'ESC', 3, 3),
    ('DI03006021', 'Advance Surveying', 'અદ્યતન સર્વેક્ષણ', 'PCC', 4, 3),
    ('DI03006031', 'Basic Transportation Engineering', 'મૂળભૂત પરિવહન ઇજનેરી', 'PCC', 4, 3),
    ('DI03006041', 'Mechanics of Structures-I', 'સ્ટ્રક્ચર્સનું મિકેનિક્સ-I', 'PCC', 4, 3),
    ('DI03006051', 'Soil Engineering', 'મૃદા ઇજનેરી', 'PCC', 4, 3),
    ('DI04000151', 'Hydraulics', 'હાઇડ્રોલિક્સ', 'PCC / Professional Elective - I', 4, 4),
]:
    SUBJECTS[_code] = (_en, _gu, _cat, _credits, 'theory', None)
    _courses = BRANCH_SEMS.setdefault('civil', {}).setdefault(_sem, [])
    if _code not in _courses: _courses.append(_code)

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
            normalize_for_app(unit)
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
            # count the units that actually have a file, not every syllabus unit listed
            "units": len([u for u in done[code][1]["units"] if u.get("file")]) if avail else 0,
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
