"""Oracle SQL simulator on top of SQLite, used to produce REAL output for the RDBMS (DI03000031) query programs.

- Oracle functions are added as Python functions (ADD_MONTHS, MONTHS_BETWEEN, TO_CHAR, TO_DATE, INITCAP, INSTR, NVL, DECODE ...).
- Dates are stored as 'YYYY-MM-DD[ HH:MM:SS]' text and displayed in Oracle's default DD-MON-YY format.
- Statements print SQL*Plus-style feedback ("Table created.", "1 row created.", "ORA-00001: ...").
- Sequences, synonyms, users/roles/grants and DESCRIBE are emulated.
SYSDATE is fixed so the output is reproducible.
"""
import calendar
import datetime as dt
import math
import re
import sqlite3
from decimal import Decimal, ROUND_HALF_UP, ROUND_DOWN

SYSDATE = dt.datetime(2026, 10, 28, 10, 30, 15)
SCHEMA = "SCOTT"
MON = ["JAN", "FEB", "MAR", "APR", "MAY", "JUN", "JUL", "AUG", "SEP", "OCT", "NOV", "DEC"]
DAYS = ["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY"]
DATE_RE = re.compile(r"^\d{4}-\d\d-\d\d( \d\d:\d\d:\d\d)?$")


# ------------------------------------------------------------------ value helpers
def is_date(v):
    return isinstance(v, str) and bool(DATE_RE.match(v))


def to_dt(v):
    if isinstance(v, dt.datetime):
        return v
    return dt.datetime.strptime(v, "%Y-%m-%d %H:%M:%S") if len(v) > 10 else dt.datetime.strptime(v, "%Y-%m-%d")


def from_dt(d):
    return d.strftime("%Y-%m-%d %H:%M:%S") if (d.hour or d.minute or d.second) else d.strftime("%Y-%m-%d")


def num(v):
    """Normalise a number: integral floats become int."""
    if isinstance(v, float) and v.is_integer() and abs(v) < 1e15:
        return int(v)
    return v


def dround(x, n=0, mode=ROUND_HALF_UP):
    q = Decimal(1).scaleb(-int(n))
    return num(float(Decimal(str(x)).quantize(q, rounding=mode))) if n >= 0 else \
        num(float((Decimal(str(x)) / Decimal(10) ** -n).quantize(Decimal(1), rounding=mode) * Decimal(10) ** -n))


# ------------------------------------------------------------------ Oracle functions
def f_round(x, n=0):
    if x is None:
        return None
    if is_date(x):
        d = to_dt(x)
        fmt = str(n).upper() if n else "DD"
        if fmt in ("MONTH", "MON", "MM"):
            first = d.replace(day=1, hour=0, minute=0, second=0)
            return from_dt(first if d.day < 16 else add_months(first, 1))
        if fmt in ("YEAR", "YYYY", "YY"):
            return from_dt(dt.datetime(d.year + (1 if d.month >= 7 else 0), 1, 1))
        return from_dt((d + dt.timedelta(hours=12)).replace(hour=0, minute=0, second=0))
    return dround(x, n)


def f_trunc(x, n=0):
    if x is None:
        return None
    if is_date(x):
        d = to_dt(x)
        fmt = str(n).upper() if n else "DD"
        if fmt in ("MONTH", "MON", "MM"):
            return from_dt(dt.datetime(d.year, d.month, 1))
        if fmt in ("YEAR", "YYYY", "YY"):
            return from_dt(dt.datetime(d.year, 1, 1))
        return from_dt(dt.datetime(d.year, d.month, d.day))
    return dround(x, n, ROUND_DOWN)


def add_months(d, n):
    y, m = divmod(d.month - 1 + int(n), 12)
    y += d.year
    m += 1
    last_src = calendar.monthrange(d.year, d.month)[1]
    last = calendar.monthrange(y, m)[1]
    day = last if d.day == last_src else min(d.day, last)
    return d.replace(year=y, month=m, day=day)


def f_add_months(d, n):
    return None if d is None else from_dt(add_months(to_dt(d), n))


def f_months_between(a, b):
    if a is None or b is None:
        return None
    x, y = to_dt(a), to_dt(b)
    lx, ly = calendar.monthrange(x.year, x.month)[1], calendar.monthrange(y.year, y.month)[1]
    whole = (x.year - y.year) * 12 + (x.month - y.month)
    if x.day == y.day or (x.day == lx and y.day == ly):
        return whole
    secs = lambda d: d.day + (d.hour * 3600 + d.minute * 60 + d.second) / 86400
    return whole + (secs(x) - secs(y)) / 31


def f_last_day(d):
    d = to_dt(d)
    return from_dt(d.replace(day=calendar.monthrange(d.year, d.month)[1]))


def f_next_day(d, day):
    d = to_dt(d)
    tgt = [x for x in DAYS if x.startswith(day.upper()[:3])][0]
    k = (DAYS.index(tgt) - d.weekday()) % 7 or 7
    return from_dt(d + dt.timedelta(days=k))


TOK = re.compile(r'"[^"]*"|YYYY|YYY|YY|RRRR|RR|MONTH|Month|month|MON|Mon|mon|MM|DDD|DD|DAY|Day|day|DY|Dy|dy|D|HH24|HH12|HH|MI|SS|AM|PM|Q|WW|W|SP|TH|FM|[^A-Za-z"]+|[A-Za-z]', re.I)


def _case(word, pat):
    if pat.isupper():
        return word.upper()
    if pat[0].isupper():
        return word.capitalize()
    return word.lower()


def date_fmt(d, fmt):
    out, fm = [], False
    for t in TOK.findall(fmt):
        u = t.upper()
        if t.startswith('"'):
            out.append(t[1:-1])
        elif u == "FM":
            fm = True
        elif u == "YYYY" or u == "RRRR":
            out.append(f"{d.year:04d}")
        elif u in ("YY", "RR"):
            out.append(f"{d.year % 100:02d}")
        elif u == "YYY":
            out.append(f"{d.year % 1000:03d}")
        elif u == "MONTH":
            w = calendar.month_name[d.month]
            out.append(_case(w if fm else w.ljust(9), t))
        elif u == "MON":
            out.append(_case(MON[d.month - 1], t))
        elif u == "MM":
            out.append(str(d.month) if fm else f"{d.month:02d}")
        elif u == "DDD":
            out.append(f"{d.timetuple().tm_yday:03d}")
        elif u == "DD":
            out.append(str(d.day) if fm else f"{d.day:02d}")
        elif u == "DAY":
            w = DAYS[d.weekday()].capitalize()
            out.append(_case(w if fm else w.ljust(9), t))
        elif u == "DY":
            out.append(_case(DAYS[d.weekday()][:3], t))
        elif u == "D":
            out.append(str((d.weekday() + 1) % 7 + 1))
        elif u == "HH24":
            out.append(f"{d.hour:02d}")
        elif u in ("HH", "HH12"):
            out.append(f"{(d.hour % 12) or 12:02d}")
        elif u == "MI":
            out.append(f"{d.minute:02d}")
        elif u == "SS":
            out.append(f"{d.second:02d}")
        elif u in ("AM", "PM"):
            out.append("AM" if d.hour < 12 else "PM")
        elif u == "Q":
            out.append(str((d.month - 1) // 3 + 1))
        elif u == "WW":
            out.append(f"{(d.timetuple().tm_yday - 1) // 7 + 1:02d}")
        elif u == "W":
            out.append(str((d.day - 1) // 7 + 1))
        else:
            out.append(t)
    return "".join(out)


def num_fmt(x, fmt):
    f = fmt.upper()
    cur = ""
    if f.startswith("$"):
        cur, f = "$", f[1:]
    elif f.startswith("L"):
        cur, f = "Rs", f[1:]
    dec = len(f.split(".")[1]) if "." in f else 0
    s = f"{abs(x):,.{dec}f}" if "," in f else f"{abs(x):.{dec}f}"
    ip = f.split(".")[0]
    width = len(ip.replace(",", "")) 
    digits = len(s.split(".")[0].replace(",", ""))
    if digits > width:
        return "#" * (len(fmt) + 1)
    if "0" in ip:
        zeros = len(ip.replace(",", "")) - ip.replace(",", "").index("0")
        s = s.split(".")[0].replace(",", "").zfill(zeros) + ("." + s.split(".")[1] if dec else "")
    s = ("-" if x < 0 else "") + cur + s
    return s if fmt.upper().startswith("FM") else s.rjust(len(fmt) + 1)


def f_to_char(x, fmt=None):
    if x is None:
        return None
    if is_date(x):
        return date_fmt(to_dt(x), fmt or "DD-MON-YY")
    if fmt is None:
        x = num(x)
        return str(x)
    return num_fmt(x, fmt)


def f_to_date(s, fmt="DD-MON-YY"):
    if s is None:
        return None
    toks = TOK.findall(fmt)
    pat, keys = "", []
    for t in toks:
        u = t.upper()
        if t.startswith('"'):
            pat += re.escape(t[1:-1])
        elif u in ("YYYY", "RRRR"):
            pat += r"(\d{4})"; keys.append("Y")
        elif u in ("YY", "RR"):
            pat += r"(\d{2})"; keys.append("y")
        elif u == "MONTH":
            pat += r"([A-Za-z]+)"; keys.append("B")
        elif u == "MON":
            pat += r"([A-Za-z]{3})"; keys.append("b")
        elif u == "MM":
            pat += r"(\d{1,2})"; keys.append("m")
        elif u == "DD":
            pat += r"(\d{1,2})"; keys.append("d")
        elif u == "HH24":
            pat += r"(\d{1,2})"; keys.append("H")
        elif u == "MI":
            pat += r"(\d{1,2})"; keys.append("M")
        elif u == "SS":
            pat += r"(\d{1,2})"; keys.append("S")
        else:
            pat += re.escape(t)
    m = re.fullmatch(pat, s.strip(), re.I)
    if not m:
        raise sqlite3.OperationalError("ORA-01861: literal does not match format string")
    v = dict(Y=SYSDATE.year, m=1, d=1, H=0, M=0, S=0)
    for k, g in zip(keys, m.groups()):
        if k == "Y":
            v["Y"] = int(g)
        elif k == "y":
            yy = int(g)
            v["Y"] = 2000 + yy if yy < 50 else 1900 + yy
        elif k in "bB":
            v["m"] = [x[:3] for x in MON].index(g.upper()[:3]) + 1
        else:
            v[k] = int(g)
    if not 1 <= v["m"] <= 12:
        raise sqlite3.OperationalError("ORA-01843: not a valid month")
    if not 1 <= v["d"] <= calendar.monthrange(v["Y"], v["m"])[1]:
        raise sqlite3.OperationalError("ORA-01847: day of month must be between 1 and last day of month")
    return from_dt(dt.datetime(v["Y"], v["m"], v["d"], v["H"], v["M"], v["S"]))


def f_to_number(s, fmt=None):
    if s is None:
        return None
    t = str(s).replace(",", "").replace("$", "").replace("Rs", "").strip()
    try:
        return num(float(t)) if "." in t else int(t)
    except ValueError:
        raise sqlite3.OperationalError("ORA-01722: invalid number")


def f_initcap(s):
    return None if s is None else re.sub(r"[A-Za-z0-9]+", lambda m: m.group(0)[0].upper() + m.group(0)[1:].lower(), s)


def f_instr(s, sub, pos=1, occ=1):
    if s is None or sub is None:
        return None
    if pos > 0:
        i = pos - 2
        for _ in range(occ):
            i = s.find(sub, i + 1)
            if i < 0:
                return 0
        return i + 1
    end = len(s) + pos + 1
    i = end
    for _ in range(occ):
        i = s.rfind(sub, 0, i + len(sub) - 1 if i < len(s) else len(s))
        if i < 0:
            return 0
    return i + 1


def f_substr(s, pos, ln=None):
    if s is None:
        return None
    s = str(s)
    pos = int(pos)
    if pos == 0:
        pos = 1
    st = pos - 1 if pos > 0 else len(s) + pos
    if st < 0:
        return None
    r = s[st:] if ln is None else s[st:st + int(ln)]
    return r or None


def f_pad(left):
    def f(s, n, c=" "):
        if s is None:
            return None
        s, n = str(num(s)), int(n)
        if len(s) >= n:
            return s[:n]
        fill = (c * n)[:n - len(s)]
        return fill + s if left else s + fill
    return f


def f_trim(left):
    def f(s, chars=" "):
        if s is None:
            return None
        return s.lstrip(chars) if left else s.rstrip(chars)
    return f


def f_decode(*a):
    x = a[0]
    rest = a[1:]
    for i in range(0, len(rest) - 1, 2):
        if x == rest[i] or (x is None and rest[i] is None):
            return rest[i + 1]
    return rest[-1] if len(rest) % 2 else None


def f_mod(a, b):
    if a is None or b is None:
        return None
    if b == 0:
        return a
    return num(math.fmod(a, b))


def ora_str(v):
    """Oracle implicit conversion to text (NULL -> '', 10.0 -> '10', date -> DD-MON-YY)."""
    if v is None:
        return ""
    if is_date(v):
        d = to_dt(v)
        return f"{d.day:02d}-{MON[d.month - 1]}-{d.year % 100:02d}"
    return str(num(v))


def nn(f):
    def g(*a):
        return None if any(x is None for x in a) else num(f(*a))
    return g


FUNCS = {
    "ROUND": (-1, f_round), "TRUNC": (-1, f_trunc), "ADD_MONTHS": (2, f_add_months), "MONTHS_BETWEEN": (2, f_months_between),
    "LAST_DAY": (1, f_last_day), "NEXT_DAY": (2, f_next_day), "TO_CHAR": (-1, f_to_char), "TO_DATE": (-1, f_to_date),
    "TO_NUMBER": (-1, f_to_number), "INITCAP": (1, f_initcap), "INSTR": (-1, f_instr), "SUBSTR": (-1, f_substr),
    "LPAD": (-1, f_pad(True)), "RPAD": (-1, f_pad(False)), "LTRIM": (-1, f_trim(True)), "RTRIM": (-1, f_trim(False)),
    "DECODE": (-1, f_decode), "MOD": (2, f_mod), "NVL": (2, lambda a, b: b if a is None else a),
    "NVL2": (3, lambda a, b, c: c if a is None else b), "ABS": (1, nn(abs)), "POWER": (2, nn(lambda a, b: a ** b)),
    "SQRT": (1, nn(math.sqrt)), "CEIL": (1, nn(math.ceil)), "FLOOR": (1, nn(math.floor)),
    "SIGN": (1, nn(lambda a: (a > 0) - (a < 0))), "CONCAT": (2, lambda a, b: ora_str(a) + ora_str(b)),
    "GREATEST": (-1, lambda *a: None if None in a else max(a)), "LEAST": (-1, lambda *a: None if None in a else min(a)),
    "SYSDATE": (0, lambda: from_dt(SYSDATE)), "LENGTH": (1, lambda s: None if s is None else len(str(num(s)))),
    "ASCII": (1, lambda s: None if s is None else ord(s[0])), "CHR": (1, lambda n: chr(int(n))),
    "TRANSLATE": (3, lambda s, a, b: None if s is None else s.translate({ord(x): (b[i] if i < len(b) else None) for i, x in enumerate(a)})),
}


# ------------------------------------------------------------------ simulator
class OraSim:
    def __init__(self):
        self.c = sqlite3.connect(":memory:", isolation_level=None)
        self.c.execute("PRAGMA foreign_keys = ON")
        self.c.execute("PRAGMA case_sensitive_like = ON")
        def wrap(f):
            def g(*a):
                try:
                    return f(*a)
                except sqlite3.OperationalError as e:
                    self.last_err = str(e)
                    raise
            return g
        for name, (n, f) in FUNCS.items():
            self.c.create_function(name, n, wrap(f))
        self.c.create_function("__DSUB", 2, lambda a, b: None if a is None or b is None else
                               num(round((to_dt(a) - to_dt(b)).total_seconds() / 86400, 9)))
        self.c.create_function("__DADD", 2, lambda d, n: None if d is None or n is None else
                               from_dt(to_dt(d) + dt.timedelta(days=n)))
        self.rewrite = []
        self.c.create_function("__NEXTVAL", 1, self._nextval)
        self.c.create_function("__CURRVAL", 1, self._currval)
        self.c.execute("CREATE TABLE dual (dummy VARCHAR2(1))")
        self.c.execute("INSERT INTO dual VALUES ('X')")
        self.seqs, self.types, self.cons, self.synonyms = {}, {}, {}, {}
        self.in_tx = False

    # sequences
    def _raise(self, msg):
        self.last_err = msg
        raise sqlite3.OperationalError(msg)

    def _nextval(self, name):
        s = self.seqs[name.upper()]
        s["cur"] = s["start"] if s["cur"] is None else s["cur"] + s["inc"]
        if s.get("max") is not None and s["cur"] > s["max"]:
            if s.get("cycle"):
                s["cur"] = s.get("min") or 1
            else:
                self._raise(f"ORA-08004: sequence {name.upper()}.NEXTVAL exceeds MAXVALUE and cannot be instantiated")
        return s["cur"]

    def _currval(self, name):
        s = self.seqs[name.upper()]
        if s["cur"] is None:
            self._raise(f"ORA-08002: sequence {name.upper()}.CURRVAL is not yet defined in this session")
        return s["cur"]

    # ---------------------------------------------------------- translation Oracle -> SQLite
    @staticmethod
    def _outside_strings(sql, fn):
        parts = re.split(r"('(?:''|[^'])*')", sql)
        return "".join(p if i % 2 else fn(p) for i, p in enumerate(parts))

    def _any_all(self, sql):
        pat = re.compile(r"(>=|<=|<>|!=|=|>|<)\s*(ANY|SOME|ALL)\s*\(", re.I)
        while True:
            m = pat.search(sql)
            if not m:
                return sql
            op, kw = m.group(1), m.group(2).upper()
            kw = "ANY" if kw == "SOME" else kw
            i, depth = m.end(), 1
            while depth:
                depth += {"(": 1, ")": -1}.get(sql[i], 0)
                i += 1
            inner = sql[m.end():i - 1].strip()
            agg = {(">", "ALL"): "MAX", (">=", "ALL"): "MAX", ("<", "ALL"): "MIN", ("<=", "ALL"): "MIN",
                   (">", "ANY"): "MIN", (">=", "ANY"): "MIN", ("<", "ANY"): "MAX", ("<=", "ANY"): "MAX"}.get((op, kw))
            if re.match(r"SELECT\b", inner, re.I):
                if agg:
                    col = self.c.execute(f"SELECT * FROM ({self.translate(inner)}) LIMIT 0").description[0][0]
                    rep = f'{op} (SELECT {agg}("{col}") FROM ({inner}))'
                elif op == "=" and kw == "ANY":
                    rep = f"IN ({inner})"
                elif op in ("<>", "!=") and kw == "ALL":
                    rep = f"NOT IN ({inner})"
                else:
                    raise ValueError("unsupported ANY/ALL form")
            else:
                if agg:
                    rep = f"{op} {agg}({inner}{', ' + inner.split(',')[0] if ',' not in inner else ''})"
                elif op == "=" and kw == "ANY":
                    rep = f"IN ({inner})"
                elif op in ("<>", "!=") and kw == "ALL":
                    rep = f"NOT IN ({inner})"
                else:
                    raise ValueError("unsupported ANY/ALL form")
            sql = sql[:m.start()] + rep + sql[i:]

    @staticmethod
    def _order_nulls(sql):
        """Oracle: NULLs sort LAST in ASC and FIRST in DESC (SQLite does the opposite)."""
        # positions of ORDER BY outside quotes
        masked = re.sub(r"'(?:''|[^'])*'", lambda m: "_" * len(m.group(0)), sql)
        for m in reversed(list(re.finditer(r"\bORDER\s+BY\b", masked, re.I))):
            i, depth, start = m.end(), 0, m.end()
            items, cur_start = [], start
            while i < len(masked):
                ch = masked[i]
                if ch == "(":
                    depth += 1
                elif ch == ")":
                    if depth == 0:
                        break
                    depth -= 1
                elif ch == "," and depth == 0:
                    items.append((cur_start, i)); cur_start = i + 1
                i += 1
            items.append((cur_start, i))
            for a, b in reversed(items):
                it = sql[a:b]
                core = it.rstrip()
                if re.search(r"NULLS\s+(FIRST|LAST)$", core, re.I) or not core.strip():
                    continue
                add = " NULLS FIRST" if re.search(r"\bDESC$", core, re.I) else " NULLS LAST"
                sql = sql[:a] + core + add + it[len(core):] + sql[b:]
        return sql

    def translate(self, sql):
        for old, new in self.rewrite:
            sql = sql.replace(old, new)
        sql = self._order_nulls(self._any_all(sql))
        def fix(p):
            p = re.sub(r"\bMINUS\b", "EXCEPT", p, flags=re.I)
            p = re.sub(r"\bSYSDATE\b(?!\s*\()", "SYSDATE()", p, flags=re.I)
            p = re.sub(r"\b(\w+)\.NEXTVAL\b", lambda m: f"__NEXTVAL('{m.group(1)}')", p, flags=re.I)
            p = re.sub(r"\b(\w+)\.CURRVAL\b", lambda m: f"__CURRVAL('{m.group(1)}')", p, flags=re.I)
            p = p.replace("/", "*1.0/")
            p = re.sub(r"\bDATE\s*$", "DATE", p)
            return p
        sql = re.sub(r"\bDATE\s+'(\d{4}-\d\d-\d\d)'", r"'\1'", sql, flags=re.I)
        return self._outside_strings(sql, fix)

    # ---------------------------------------------------------- DDL helpers
    def _create_table(self, sql):
        m = re.match(r"CREATE\s+TABLE\s+(\w+)\s*\((.*)\)\s*$", sql, re.S | re.I)
        if not m:  # CREATE TABLE ... AS SELECT
            self.c.execute(self.translate(sql))
            return
        name, body = m.group(1).upper(), m.group(2)
        cols, depth, cur = [], 0, ""
        for ch in body:
            if ch == "," and depth == 0:
                cols.append(cur.strip()); cur = ""
                continue
            depth += ch == "("
            depth -= ch == ")"
            cur += ch
        cols.append(cur.strip())
        new = []
        for col in cols:
            cm = re.match(r"(\w+)\s+([A-Za-z0-9_]+(?:\s*\([^)]*\))?)(.*)$", col, re.S)
            if cm and cm.group(1).upper() not in ("CONSTRAINT", "PRIMARY", "UNIQUE", "FOREIGN", "CHECK"):
                cname, ctype, rest = cm.group(1).upper(), cm.group(2).upper().replace(" ", ""), cm.group(3)
                self.types[(name, cname)] = ctype
                for cn, kind in re.findall(r"CONSTRAINT\s+(\w+)\s+(PRIMARY\s+KEY|UNIQUE|CHECK|REFERENCES|NOT\s+NULL)", rest, re.I):
                    self.cons[(name, cname, kind.split()[0].upper())] = cn.upper()
                stype = "NUMERIC" if ctype.startswith(("NUMBER", "DECIMAL", "FLOAT")) else ctype
                rest = re.sub(r"CONSTRAINT\s+\w+\s+NOT\s+NULL", "NOT NULL", rest, flags=re.I)
                new.append(f"{cname} {stype}{rest}")
            else:
                tm = re.match(r"CONSTRAINT\s+(\w+)\s+(PRIMARY\s+KEY|UNIQUE|FOREIGN\s+KEY|CHECK)\s*\(([^)]*)\)", col, re.I)
                if tm:
                    kind = tm.group(2).split()[0].upper()
                    kind = "REFERENCES" if kind == "FOREIGN" else kind
                    first = re.findall(r"\w+", tm.group(3))
                    key = first[0].upper() if first and kind != "CHECK" else ("*" if kind != "CHECK" else self._check_col(tm.group(3), name))
                    self.cons[(name, key, kind)] = tm.group(1).upper()
                new.append(col)
        self.c.execute(self.translate(f"CREATE TABLE {name} (" + ", ".join(new) + ")"))

    def _check_col(self, expr, table):
        for w in re.findall(r"[A-Za-z_]\w*", expr):
            if (table, w.upper()) in self.types:
                return w.upper()
        return "*"

    def _alter(self, sql):
        m = re.match(r"ALTER\s+TABLE\s+(\w+)\s+(ADD|MODIFY|DROP\s+COLUMN|RENAME\s+COLUMN|RENAME\s+TO)\s*(.*)$", sql, re.S | re.I)
        t, op, rest = m.group(1).upper(), re.sub(r"\s+", " ", m.group(2).upper()), m.group(3).strip()
        if op in ("ADD", "MODIFY"):
            body = rest[1:-1] if rest.startswith("(") else rest
            parts, depth, cur = [], 0, ""
            for ch in body:
                if ch == "," and depth == 0:
                    parts.append(cur.strip()); cur = ""
                    continue
                depth += ch == "("
                depth -= ch == ")"
                cur += ch
            parts.append(cur.strip())
            for p in parts:
                cm = re.match(r"(\w+)\s+([A-Za-z0-9_]+(?:\s*\([^)]*\))?)(.*)$", p, re.S)
                cname, ctype = cm.group(1).upper(), cm.group(2).upper().replace(" ", "")
                self.types[(t, cname)] = ctype
                if op == "ADD":
                    st = "NUMERIC" if ctype.startswith("NUMBER") else ctype
                    self.c.execute(f"ALTER TABLE {t} ADD COLUMN {cname} {st}{cm.group(3)}")
        elif op == "DROP COLUMN":
            self.c.execute(f"ALTER TABLE {t} DROP COLUMN {rest}")
            self.types.pop((t, rest.upper()), None)
        elif op == "RENAME COLUMN":
            a, b = re.match(r"(\w+)\s+TO\s+(\w+)", rest, re.I).groups()
            self.c.execute(f"ALTER TABLE {t} RENAME COLUMN {a} TO {b}")
            self.types[(t, b.upper())] = self.types.pop((t, a.upper()), "")
        else:
            self._rename(t, rest.upper())

    def _rename(self, a, b):
        self.c.execute(f"ALTER TABLE {a} RENAME TO {b}")
        for k in list(self.types):
            if k[0] == a:
                self.types[(b, k[1])] = self.types.pop(k)

    def _desc(self, t):
        t = t.upper()
        t = self.synonyms.get(t, t)
        rows = self.c.execute(f"PRAGMA table_info({t})").fetchall()
        if not rows:
            return f"ERROR:\nORA-04043: object {t} does not exist"
        data = []
        for _, name, typ, notnull, _, pk in rows:
            data.append((name.upper(), "NOT NULL" if notnull or pk else "", self.types.get((t, name.upper()), typ.upper())))
        w = max(len(r[0]) for r in data + [("Name", 0, 0)]) + 1
        out = [f" {'Name'.ljust(w)} {'Null?'.ljust(8)} Type", f" {'-' * w} {'-' * 8} {'-' * max(4, max(len(r[2]) for r in data))}"]
        out += [f" {r[0].ljust(w)} {r[1].ljust(8)} {r[2]}" for r in data]
        return "\n".join(out)

    # ---------------------------------------------------------- output formatting
    @staticmethod
    def _fmt_val(v):
        if v is None:
            return ""
        if is_date(v):
            d = to_dt(v)
            return f"{d.day:02d}-{MON[d.month - 1]}-{d.year % 100:02d}"
        if isinstance(v, float):
            v = num(v)
            if isinstance(v, float):
                s = f"{v:.10g}"
                if len(s) > 10:
                    s = f"{v:.{max(1, 9 - len(str(int(abs(v)))))}f}".rstrip("0")
                return s
        return str(v)

    @staticmethod
    def _select_items(sql):
        """Top-level select-list items of the original (Oracle) query."""
        m = re.match(r"\s*SELECT\s+(DISTINCT\s+)?", sql, re.I)
        if not m:
            return None
        items, depth, cur, q, i = [], 0, "", False, m.end()
        while i < len(sql):
            ch = sql[i]
            if ch == "'":
                q = not q
            if not q:
                if depth == 0 and re.match(r"\s+FROM\b", sql[i:], re.I) or depth == 0 and re.match(r"FROM\b", sql[i:], re.I) and cur.endswith((" ", "\n")):
                    break
                if ch == "," and depth == 0:
                    items.append(cur.strip()); cur = ""; i += 1
                    continue
                depth += ch == "("
                depth -= ch == ")"
            cur += ch
            i += 1
        items.append(cur.strip())
        return items

    def _table(self, cur, sql):
        rows = cur.fetchall()
        if not rows:
            return "no rows selected"
        heads = []
        items = self._select_items(sql)
        use = items and len(items) == len(cur.description) and not any("*" == it[-1:] for it in items)
        for k, d in enumerate(cur.description):
            h = d[0]
            if f'"{h}"' in sql:
                heads.append(h)
                continue
            if use:
                it = items[k]
                al = re.search(r"(?:\)|'|\s)\s*(?:AS\s+)?([A-Za-z_]\w*)$", it, re.I)
                plain = re.fullmatch(r"(?:\w+\.)?(\w+)", it)
                if plain:
                    h = plain.group(1)
                elif al and not re.search(r"\b(?:AND|OR|END|NULL)$", it, re.I) and al.group(1).upper() == d[0].upper():
                    h = al.group(1)
                else:
                    h = re.sub(r"\s+", "", it) if "'" not in it else re.sub(r"\s+(?=(?:[^']*'[^']*')*[^']*$)", "", it)
            heads.append(h.upper())
        isnum = [all(isinstance(r[i], (int, float)) or r[i] is None for r in rows) and any(r[i] is not None for r in rows)
                 for i in range(len(heads))]
        vals = [[self._fmt_val(v) for v in r] for r in rows]
        w = [max([len(heads[i])] + [len(r[i]) for r in vals]) for i in range(len(heads))]
        line = lambda cells: " ".join((c.rjust(w[i]) if isnum[i] else c.ljust(w[i])) for i, c in enumerate(cells)).rstrip()
        out = [line(heads), " ".join("-" * x for x in w)] + [line(r) for r in vals]
        if len(rows) >= 6:
            out += ["", f"{len(rows)} rows selected."]
        return "\n".join(out)

    # ---------------------------------------------------------- errors
    def _ora(self, e, sql):
        msg = str(e)
        if "user-defined function raised exception" in msg and getattr(self, "last_err", None):
            msg, self.last_err = self.last_err, None
        if msg.startswith("ORA-"):
            return "ERROR at line 1:\n" + msg
        m = re.search(r"NOT NULL constraint failed: (\w+)\.(\w+)", msg)
        if m:
            return f'ERROR at line 1:\nORA-01400: cannot insert NULL into ("{SCHEMA}"."{m.group(1).upper()}"."{m.group(2).upper()}")'
        m = re.search(r"UNIQUE constraint failed: (\w+)\.(\w+)", msg)
        if m:
            t, c = m.group(1).upper(), m.group(2).upper()
            cn = self.cons.get((t, c, "PRIMARY")) or self.cons.get((t, c, "UNIQUE")) or "SYS_C008315"
            return f"ERROR at line 1:\nORA-00001: unique constraint ({SCHEMA}.{cn}) violated"
        m = re.search(r"CHECK constraint failed: (.*)", msg)
        if m:
            t = re.search(r"(?:INTO|UPDATE)\s+(\w+)", sql, re.I).group(1).upper()
            cands = [v for k, v in self.cons.items() if k[0] == t and k[2] == "CHECK"]
            named = [v for v in cands if v.upper() == m.group(1).strip().upper()]
            cn = (named or cands or ["SYS_C008316"])[0]
            return f"ERROR at line 1:\nORA-02290: check constraint ({SCHEMA}.{cn}) violated"
        if "FOREIGN KEY constraint failed" in msg:
            if re.match(r"\s*DELETE", sql, re.I):
                t = re.search(r"FROM\s+(\w+)", sql, re.I).group(1).upper()
                cn = next((v for k, v in self.cons.items() if k[2] == "REFERENCES" and self._refs(k[0], t)), "SYS_C008317")
                return f"ERROR at line 1:\nORA-02292: integrity constraint ({SCHEMA}.{cn}) violated - child record found"
            t = re.search(r"(?:INTO|UPDATE)\s+(\w+)", sql, re.I).group(1).upper()
            cn = next((v for k, v in self.cons.items() if k[0] == t and k[2] == "REFERENCES"), "SYS_C008317")
            return f"ERROR at line 1:\nORA-02291: integrity constraint ({SCHEMA}.{cn}) violated - parent key not found"
        m = re.search(r"no such table: (\w+)", msg)
        if m:
            return "ERROR at line 1:\nORA-00942: table or view does not exist"
        m = re.search(r"no such column: (\S+)", msg)
        if m:
            return f'ERROR at line 1:\nORA-00904: "{m.group(1).upper()}": invalid identifier'
        if "already exists" in msg:
            return "ERROR at line 1:\nORA-00955: name is already used by an existing object"
        if "sub-select returns" in msg or "more than one row" in msg:
            return "ERROR at line 1:\nORA-01427: single-row subquery returns more than one row"
        return "ERROR at line 1:\nORA-00900: " + msg

    def _refs(self, child, parent):
        r = self.c.execute(f"PRAGMA foreign_key_list({child})").fetchall()
        return any(x[2].upper() == parent for x in r)

    # ---------------------------------------------------------- statement dispatch
    def _begin(self):
        if not self.in_tx:
            self.c.execute("BEGIN")
            self.in_tx = True

    def _commit(self):
        if self.in_tx:
            self.c.execute("COMMIT")
            self.in_tx = False

    def exec1(self, sql):
        s = sql.strip().rstrip(";").strip()
        u = re.sub(r"\s+", " ", s.upper())
        try:
            if u.startswith(("SELECT", "WITH")):
                return self._table(self.c.execute(self.translate(s)), s)
            if u.startswith("INSERT"):
                self._begin()
                n = self.c.execute(self.translate(s)).rowcount
                return f"{n} row{'s' if n != 1 else ''} created."
            if u.startswith("UPDATE"):
                self._begin()
                n = self.c.execute(self.translate(s)).rowcount
                return f"{n} row{'s' if n != 1 else ''} updated."
            if u.startswith("DELETE"):
                self._begin()
                n = self.c.execute(self.translate(s)).rowcount
                return f"{n} row{'s' if n != 1 else ''} deleted."
            if u.startswith(("DESC ", "DESCRIBE ")):
                return self._desc(s.split()[1])
            if u == "COMMIT" or u == "COMMIT WORK":
                self._commit()
                return "Commit complete."
            if u.startswith("ROLLBACK"):
                m = re.match(r"ROLLBACK(?: WORK)? TO (?:SAVEPOINT )?(\w+)", u)
                if m:
                    self.c.execute(f"ROLLBACK TO {m.group(1)}")
                elif self.in_tx:
                    self.c.execute("ROLLBACK")
                    self.in_tx = False
                return "Rollback complete."
            if u.startswith("SAVEPOINT"):
                self._begin()
                self.c.execute(s)
                return "Savepoint created."
            if u.startswith(("SET ", "CONNECT", "CONN ")):
                return "Connected." if u.startswith("CONN") else ""
            # ---- everything below is DDL / DCL: implicit commit like Oracle
            self._commit()
            if u.startswith("CREATE TABLE"):
                self._create_table(s)
                return "Table created."
            if u.startswith("ALTER TABLE"):
                self._alter(s)
                return "Table altered."
            if u.startswith("RENAME "):
                a, b = re.match(r"RENAME\s+(\w+)\s+TO\s+(\w+)", s, re.I).groups()
                self._rename(a.upper(), b.upper())
                return "Table renamed."
            if u.startswith("DROP TABLE"):
                t = s.split()[2]
                self.c.execute(f"DROP TABLE {t}")
                return "Table dropped."
            if u.startswith("TRUNCATE TABLE"):
                self.c.execute(f"DELETE FROM {s.split()[2]}")
                return "Table truncated."
            m = re.match(r"CREATE (OR REPLACE )?(FORCE )?VIEW (\w+)(?:\s*\(([^)]*)\))? AS (.*)$", s, re.I | re.S)
            if m:
                body = re.sub(r"\s+WITH\s+(CHECK\s+OPTION|READ\s+ONLY)\s*$", "", m.group(5), flags=re.I)
                if m.group(1):
                    self.c.execute(f"DROP VIEW IF EXISTS {m.group(3)}")
                cols = f"({m.group(4)})" if m.group(4) else ""
                self.c.execute(self.translate(f"CREATE VIEW {m.group(3)}{cols} AS {body}"))
                return "View created."
            if u.startswith("ALTER VIEW"):
                return "View altered."
            if u.startswith("DROP VIEW"):
                self.c.execute(f"DROP VIEW {s.split()[2]}")
                return "View dropped."
            m = re.match(r"CREATE (?:OR REPLACE )?(?:PUBLIC )?SYNONYM (\w+) FOR (\w+)", s, re.I)
            if m:
                self.c.execute(f"CREATE VIEW {m.group(1)} AS SELECT * FROM {m.group(2)}")
                self.synonyms[m.group(1).upper()] = m.group(2).upper()
                return "Synonym created."
            if u.startswith(("DROP SYNONYM", "DROP PUBLIC SYNONYM")):
                n = s.split()[-1]
                self.c.execute(f"DROP VIEW {n}")
                self.synonyms.pop(n.upper(), None)
                return "Synonym dropped."
            m = re.match(r"(CREATE|ALTER) SEQUENCE (\w+)(.*)$", u, re.S)
            if m:
                name, opts = m.group(2), m.group(3)
                g = lambda k: (int(re.search(k + r" (-?\d+)", opts).group(1)) if re.search(k + r" (-?\d+)", opts) else None)
                if m.group(1) == "CREATE":
                    self.seqs[name] = {"start": g("START WITH") or 1, "inc": g("INCREMENT BY") or 1, "max": g("MAXVALUE"),
                                       "min": g("MINVALUE"), "cycle": " CYCLE" in opts and "NOCYCLE" not in opts, "cur": None}
                    return "Sequence created."
                sq = self.seqs[name]
                for k, key in (("INCREMENT BY", "inc"), ("MAXVALUE", "max"), ("MINVALUE", "min")):
                    if g(k) is not None:
                        sq[key] = g(k)
                if " CYCLE" in opts:
                    sq["cycle"] = "NOCYCLE" not in opts
                return "Sequence altered."
            if u.startswith("DROP SEQUENCE"):
                self.seqs.pop(u.split()[2])
                return "Sequence dropped."
            if re.match(r"CREATE (UNIQUE )?INDEX", u):
                self.c.execute(s)
                return "Index created."
            if u.startswith("DROP INDEX"):
                self.c.execute(s)
                return "Index dropped."
            if u.startswith("CREATE USER"):
                return "User created."
            if u.startswith("ALTER USER"):
                return "User altered."
            if u.startswith("DROP USER"):
                return "User dropped."
            if u.startswith("CREATE ROLE"):
                return "Role created."
            if u.startswith("DROP ROLE"):
                return "Role dropped."
            if u.startswith("GRANT"):
                return "Grant succeeded."
            if u.startswith("REVOKE"):
                return "Revoke succeeded."
            raise ValueError("unsupported statement: " + s[:60])
        except sqlite3.Error as e:
            return self._ora(e, s)

    @staticmethod
    def split(script):
        # SQL*Plus commands (DESC, SET, CONNECT) end at the end of the line, without ';'
        script = re.sub(r"(?im)^(\s*(?:DESC|DESCRIBE|CONNECT|CONN|SET\s+(?:SERVEROUTPUT|VERIFY|LINESIZE|PAGESIZE|FEEDBACK|ECHO|HEADING))\s+[^;\n]*?)\s*$", r"\1;", script)
        out, cur, q = [], "", False
        for ch in script:
            if ch == "'":
                q = not q
            if ch == ";" and not q:
                if cur.strip():
                    out.append(cur.strip())
                cur = ""
            else:
                cur += ch
        if cur.strip():
            out.append(cur.strip())
        # drop comment-only lines at the start of each statement
        res = []
        for s in out:
            s = "\n".join(l for l in s.split("\n") if not l.strip().startswith("--")).strip()
            if s:
                res.append(s)
        return res

    def run(self, script, show=True):
        outs = []
        for st in self.split(script):
            r = self.exec1(st)
            if r != "":
                outs.append(r)
        return "\n\n".join(outs) if show else ""


def run_sql(code, setup="", rewrite=()):
    """Run setup silently, then code; return the output text.
    rewrite: (oracle_text, simulator_text) pairs applied only to the executed SQL, e.g.
    ("SYSDATE - hiredate", "__DSUB(SYSDATE, hiredate)"); headings still come from the Oracle text."""
    sim = OraSim()
    if setup:
        for st in OraSim.split(setup):
            r = sim.exec1(st)
            assert not r.startswith("ERROR"), f"setup failed: {st[:60]}\n{r}"
    sim.rewrite = list(rewrite)
    return sim.run(code), sim


if __name__ == "__main__":
    demo = """
CREATE TABLE t (id NUMBER(3) CONSTRAINT pk_t PRIMARY KEY, name VARCHAR2(10) NOT NULL, sal NUMBER(8,2) CONSTRAINT ck_sal CHECK (sal > 0), jd DATE);
INSERT INTO t VALUES (1, 'amit shah', 45000, TO_DATE('31-01-2024','DD-MM-YYYY'));
INSERT INTO t VALUES (1, 'x', 10, NULL);
INSERT INTO t VALUES (2, NULL, 10, NULL);
INSERT INTO t VALUES (3, 'riya', -5, NULL);
SELECT id, INITCAP(name) name, sal/12 "Monthly", ADD_MONTHS(jd, 1) next_m, TO_CHAR(jd,'DD Month YYYY') j FROM t;
SELECT ROUND(15.567, 1), ROUND(1550, -2), TRUNC(15.567,1), MOD(17,5), POWER(2,10), SQRT(81), 7/2 FROM dual;
SELECT MONTHS_BETWEEN(TO_DATE('15-03-2024','DD-MM-YYYY'), TO_DATE('15-01-2024','DD-MM-YYYY')) mb, LAST_DAY(SYSDATE), NEXT_DAY(SYSDATE,'MONDAY'), TO_CHAR(SYSDATE,'DY DD-MON-YYYY HH24:MI') FROM dual;
SELECT INSTR('CORPORATE FLOOR','OR',3,2) i, SUBSTR('ABCDEFG',3,4) s, LPAD('77',5,'*') l, TO_CHAR(1234567.891,'9,999,999.99') n FROM dual;
CREATE SEQUENCE s1 START WITH 101 INCREMENT BY 1;
SELECT s1.NEXTVAL FROM dual;
DESC t
"""
    print(run_sql(demo)[0])
