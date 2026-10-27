"""Mini PL/SQL interpreter on top of OraSim2 (sql_objects) for RDBMS Unit 5.

Supports: anonymous blocks, DECLARE (variables, CONSTANT, NOT NULL, %TYPE, %ROWTYPE, RECORD types, cursors with
parameters, exceptions, PRAGMA EXCEPTION_INIT), :=, IF/ELSIF/ELSE, CASE (simple + searched, statement + expression),
LOOP/EXIT [WHEN]/CONTINUE, WHILE, numeric FOR [REVERSE], cursor FOR loops (named + inline query), explicit cursors
(OPEN/FETCH/CLOSE, %FOUND %NOTFOUND %ROWCOUNT %ISOPEN), implicit cursor SQL%..., SELECT INTO, DML/TCL, DBMS_OUTPUT,
exceptions (predefined, user-defined, RAISE, RAISE_APPLICATION_ERROR, OTHERS, SQLCODE, SQLERRM), stored procedures
and functions (IN / OUT / IN OUT, defaults, named notation, functions usable in SQL), EXEC, triggers
(BEFORE/AFTER, row/statement, INSERT/UPDATE [OF]/DELETE, WHEN, :NEW/:OLD, INSERTING/UPDATING/DELETING),
ALTER/DROP TRIGGER, USER_TRIGGERS / USER_PROCEDURES.
Expressions are evaluated by the SQL engine (SELECT expr) after variables are replaced by literals.
"""
import bisect
import copy
import re
import sqlite3

from sql_runner import OraSim, SCHEMA, num, ora_str
from sql_objects import OraSim2, OraErr, split_top, bal

TOK = re.compile(r"""\s*(?:(?P<str>'(?:''|[^'])*')|(?P<num>\d+(?:\.\d+)?(?:[eE][+-]?\d+)?)|(?P<id>[A-Za-z_][\w$#]*)|"""
                 r"""(?P<qid>"[^"]*")|(?P<op>:=|=>|\.\.|\|\||<=|>=|<>|!=|\*\*|<<|>>|[-+*/%(),;=<>.:@&]))""")
PREDEF = {1: "DUP_VAL_ON_INDEX", 1403: "NO_DATA_FOUND", 1422: "TOO_MANY_ROWS", 1476: "ZERO_DIVIDE", 1722: "INVALID_NUMBER",
          6502: "VALUE_ERROR", 1001: "INVALID_CURSOR", 6511: "CURSOR_ALREADY_OPEN", 6592: "CASE_NOT_FOUND", 6503: "PROGRAM_ERROR"}
MSG = {1403: "no data found", 1422: "exact fetch returns more than requested number of rows", 1476: "divisor is equal to zero",
       1001: "invalid cursor", 6511: "PL/SQL: cursor already open", 6592: "CASE not found while executing CASE statement",
       6503: "PL/SQL: Function returned without value", 1722: "invalid number"}
NAME2CODE = {v: k for k, v in PREDEF.items()}


def pl_str(v):
    if isinstance(v, float):
        v = num(float(f"{v:.12g}"))
    if isinstance(v, bool):
        v = int(v)
    return ora_str(v)


def lit(v):
    if v is None:
        return "NULL"
    if isinstance(v, bool):
        return "1" if v else "0"
    if isinstance(v, int):
        return str(v)
    if isinstance(v, float):
        v = num(float(f"{v:.12g}"))
        return repr(v) if isinstance(v, float) else str(v)
    return "'" + str(v).replace("'", "''") + "'"


class Tok:
    __slots__ = ("kind", "v", "s", "e", "line")

    def __init__(self, kind, v, s, e, line):
        self.kind, self.v, self.s, self.e, self.line = kind, v, s, e, line

    @property
    def u(self):
        return self.v.upper() if self.kind == "id" else None


def tokenize(src):
    nl = [i for i, ch in enumerate(src) if ch == "\n"]
    out, i = [], 0
    while i < len(src):
        m = TOK.match(src, i)
        if not m or m.end() == i:
            if src[i:].strip() == "":
                break
            raise SyntaxError(f"PL/SQL tokenizer stuck at: {src[i:i + 30]!r}")
        k = m.lastgroup
        s = m.start(k)
        out.append(Tok(k, m.group(k), s, m.end(), bisect.bisect_left(nl, s) + 1))
        i = m.end()
    return out


def strip_comments(src):
    out, i, q = [], 0, False
    while i < len(src):
        ch = src[i]
        if ch == "'":
            q = not q
        if not q and src.startswith("--", i):
            j = src.find("\n", i)
            i = len(src) if j < 0 else j
            continue
        if not q and src.startswith("/*", i):
            j = src.find("*/", i)
            seg = src[i:j + 2]
            out.append("\n" * seg.count("\n"))
            i = j + 2
            continue
        out.append(ch)
        i += 1
    return "".join(out)


# ====================================================================== parser
class Parser:
    def __init__(self, src, start=0):
        self.src = src
        self.t = tokenize(src)
        self.i = next((k for k, x in enumerate(self.t) if x.s >= start), len(self.t))

    def peek(self, k=0):
        j = self.i + k
        return self.t[j] if j < len(self.t) else None

    def isk(self, *words, k=0):
        t = self.peek(k)
        return t is not None and t.kind == "id" and t.u in words

    def isop(self, op, k=0):
        t = self.peek(k)
        return t is not None and t.kind == "op" and t.v == op

    def next(self):
        t = self.peek()
        self.i += 1
        return t

    def expect_kw(self, *words):
        t = self.next()
        if t is None or t.u not in words:
            raise SyntaxError(f"expected {words} near line {t.line if t else '?'}: got {t.v if t else 'EOF'}")
        return t

    def expect_op(self, op):
        t = self.next()
        if t is None or t.v != op:
            raise SyntaxError(f"expected '{op}' near line {t.line if t else '?'}: got {t.v if t else 'EOF'}")
        return t

    def text(self, a, b):
        return self.src[self.t[a].s:self.t[b - 1].e] if b > a else ""

    def until(self, kws=(), ops=(";",)):
        """Scan an expression up to a top-level stop keyword / operator. Returns its source text."""
        a, depth = self.i, 0
        while True:
            t = self.peek()
            if t is None:
                break
            if depth == 0 and ((t.kind == "id" and t.u in kws) or (t.kind == "op" and t.v in ops)):
                break
            if t.kind == "op" and t.v == "(":
                depth += 1
            elif t.kind == "op" and t.v == ")":
                depth -= 1
            elif t.kind == "id" and t.u == "CASE":
                depth += 1
            elif t.kind == "id" and t.u == "END" and depth > 0:
                depth -= 1
            self.i += 1
        return self.text(a, self.i)

    def args(self):
        """'(' a, b => c ')' -> list of raw argument texts."""
        self.expect_op("(")
        out, a, depth = [], self.i, 0
        while True:
            t = self.next()
            if t.kind == "op" and t.v == "(":
                depth += 1
            elif t.kind == "op" and t.v == ")":
                if depth == 0:
                    if self.i - 1 > a:
                        out.append(self.text(a, self.i - 1))
                    return out
                depth -= 1
            elif t.kind == "op" and t.v == "," and depth == 0:
                out.append(self.text(a, self.i - 1))
                a = self.i

    # ---------------------------------------------------------------- declarations
    def decls(self):
        out = []
        while not self.isk("BEGIN"):
            t = self.peek()
            line = t.line
            if self.isk("CURSOR"):
                self.next()
                name = self.next().u
                params = []
                if self.isop("("):
                    for p in self.args():
                        w = p.split()
                        params.append((w[0].upper(), " ".join(x for x in w[1:] if x.upper() != "IN")))
                if self.isk("RETURN"):
                    self.next(); self.until(("IS",), ())
                self.expect_kw("IS")
                q = self.until()
                self.expect_op(";")
                out.append({"k": "cursor", "name": name, "params": params, "query": q, "line": line})
            elif self.isk("PRAGMA"):
                self.next(); self.expect_kw("EXCEPTION_INIT")
                a = self.args()
                self.expect_op(";")
                out.append({"k": "pragma", "name": a[0].strip().upper(), "code": int(a[1].replace(" ", "")), "line": line})
            elif self.isk("TYPE"):
                self.next()
                name = self.next().u
                self.expect_kw("IS")
                self.expect_kw("RECORD")
                fields = [(f.split(None, 1)[0].upper(), f.split(None, 1)[1].strip()) for f in self.args()]
                self.expect_op(";")
                out.append({"k": "rectype", "name": name, "fields": fields, "line": line})
            elif self.isk("PROCEDURE", "FUNCTION"):
                raise SyntaxError("nested subprograms are not supported")
            else:
                name = self.next().u
                if self.isk("EXCEPTION"):
                    self.next(); self.expect_op(";")
                    out.append({"k": "exc", "name": name, "line": line})
                    continue
                const = False
                if self.isk("CONSTANT"):
                    self.next(); const = True
                typ = self.until(("NOT", "DEFAULT"), (":=", ";"))
                notnull = False
                if self.isk("NOT"):
                    self.next(); self.expect_kw("NULL"); notnull = True
                init = None
                if self.isop(":=") or self.isk("DEFAULT"):
                    self.next()
                    init = self.until()
                self.expect_op(";")
                out.append({"k": "var", "name": name, "type": typ, "const": const, "notnull": notnull, "init": init, "line": line})
        return out

    # ---------------------------------------------------------------- blocks and statements
    def block(self, declare):
        line = self.peek().line
        decls = self.decls() if declare else []
        self.expect_kw("BEGIN")
        body = self.stmts(("EXCEPTION", "END"))
        handlers = []
        if self.isk("EXCEPTION"):
            self.next()
            while self.isk("WHEN"):
                self.next()
                names = [self.next().u]
                while self.isk("OR"):
                    self.next(); names.append(self.next().u)
                self.expect_kw("THEN")
                handlers.append((names, self.stmts(("WHEN", "END"))))
        self.expect_kw("END")
        if self.peek() is not None and self.peek().kind == "id":
            self.next()
        if self.isop(";"):
            self.next()
        return {"k": "block", "decls": decls, "body": body, "handlers": handlers, "line": line}

    def stmts(self, stop):
        out = []
        while not self.isk(*stop):
            if self.peek() is None:
                raise SyntaxError("unexpected end of block")
            out.append(self.stmt())
        return out

    def end(self, word):
        self.expect_kw("END")
        self.expect_kw(word)
        if self.peek() is not None and self.peek().kind == "id":
            self.next()
        self.expect_op(";")

    def stmt(self):
        t = self.peek()
        line = t.line
        col = t.s - (self.src.rfind("\n", 0, t.s) + 1) + 1
        st = self._stmt(t, line)
        st["col"] = col
        return st

    def _stmt(self, t, line):
        label = None
        if self.isop("<<"):
            self.next(); label = self.next().u; self.expect_op(">>")
            t = self.peek()
        u = t.u
        if u == "IF":
            self.next()
            arms = []
            cond = self.until(("THEN",), ())
            self.expect_kw("THEN")
            arms.append((cond, self.stmts(("ELSIF", "ELSE", "END"))))
            other = None
            while self.isk("ELSIF"):
                self.next()
                cond = self.until(("THEN",), ())
                self.expect_kw("THEN")
                arms.append((cond, self.stmts(("ELSIF", "ELSE", "END"))))
            if self.isk("ELSE"):
                self.next()
                other = self.stmts(("END",))
            self.end("IF")
            return {"k": "if", "arms": arms, "else": other, "line": line}
        if u == "LOOP":
            self.next()
            body = self.stmts(("END",))
            self.end("LOOP")
            return {"k": "loop", "body": body, "label": label, "line": line}
        if u == "WHILE":
            self.next()
            cond = self.until(("LOOP",), ())
            self.expect_kw("LOOP")
            body = self.stmts(("END",))
            self.end("LOOP")
            return {"k": "while", "cond": cond, "body": body, "label": label, "line": line}
        if u == "FOR":
            self.next()
            var = self.next().u
            self.expect_kw("IN")
            rev = False
            if self.isk("REVERSE"):
                self.next(); rev = True
            # numeric if '..' appears before LOOP at depth 0
            j, depth, numeric = self.i, 0, False
            while j < len(self.t):
                x = self.t[j]
                if x.kind == "op" and x.v == "(":
                    depth += 1
                elif x.kind == "op" and x.v == ")":
                    depth -= 1
                elif depth == 0 and x.kind == "op" and x.v == "..":
                    numeric = True; break
                elif depth == 0 and x.kind == "id" and x.u == "LOOP":
                    break
                j += 1
            if numeric:
                lo = self.until((), ("..",))
                self.expect_op("..")
                hi = self.until(("LOOP",), ())
                self.expect_kw("LOOP")
                body = self.stmts(("END",))
                self.end("LOOP")
                return {"k": "fornum", "var": var, "lo": lo, "hi": hi, "rev": rev, "body": body, "label": label, "line": line}
            if self.isop("("):
                a = self.i
                self.i = self._close_paren(self.i)
                q = self.text(a + 1, self.i - 1)
                cur, cargs = None, []
            else:
                cur = self.next().u
                cargs = self.args() if self.isop("(") else []
                q = None
            self.expect_kw("LOOP")
            body = self.stmts(("END",))
            self.end("LOOP")
            return {"k": "forcur", "var": var, "cursor": cur, "cargs": cargs, "query": q, "body": body, "label": label, "line": line}
        if u == "CASE":
            self.next()
            sel = None if self.isk("WHEN") else self.until(("WHEN",), ())
            arms, other = [], None
            while self.isk("WHEN"):
                self.next()
                c = self.until(("THEN",), ())
                self.expect_kw("THEN")
                arms.append((c, self.stmts(("WHEN", "ELSE", "END"))))
            if self.isk("ELSE"):
                self.next()
                other = self.stmts(("END",))
            self.end("CASE")
            return {"k": "case", "sel": sel, "arms": arms, "else": other, "line": line}
        if u in ("EXIT", "CONTINUE"):
            self.next()
            lab = None
            if self.peek().kind == "id" and self.peek().u != "WHEN":
                lab = self.next().u
            cond = None
            if self.isk("WHEN"):
                self.next(); cond = self.until()
            self.expect_op(";")
            return {"k": u.lower(), "cond": cond, "label": lab, "line": line}
        if u == "NULL" and self.isop(";", 1):
            self.next(); self.next()
            return {"k": "null", "line": line}
        if u == "RAISE":
            self.next()
            name = None if self.isop(";") else self.next().u
            self.expect_op(";")
            return {"k": "raise", "name": name, "line": line}
        if u == "RETURN":
            self.next()
            e = None if self.isop(";") else self.until()
            self.expect_op(";")
            return {"k": "return", "expr": e, "line": line}
        if u in ("DECLARE", "BEGIN"):
            if u == "DECLARE":
                self.next()
            b = self.block(u == "DECLARE")
            b["line"] = line
            return b
        if u == "OPEN":
            self.next()
            cur = self.next().u
            cargs = self.args() if self.isop("(") else []
            self.expect_op(";")
            return {"k": "open", "cursor": cur, "cargs": cargs, "line": line}
        if u == "FETCH":
            self.next()
            cur = self.next().u
            self.expect_kw("INTO")
            targets = [x.strip() for x in split_top(self.until())]
            self.expect_op(";")
            return {"k": "fetch", "cursor": cur, "into": targets, "line": line}
        if u == "CLOSE":
            self.next()
            cur = self.next().u
            self.expect_op(";")
            return {"k": "close", "cursor": cur, "line": line}
        if u == "SELECT":
            a = self.i
            j, depth, into_at, from_at = self.i, 0, None, None
            while not (self.t[j].kind == "op" and self.t[j].v == ";" and depth == 0):
                x = self.t[j]
                if x.kind == "op" and x.v == "(":
                    depth += 1
                elif x.kind == "op" and x.v == ")":
                    depth -= 1
                elif depth == 0 and x.u == "INTO" and into_at is None:
                    into_at = j
                elif depth == 0 and x.u == "FROM" and into_at is not None and from_at is None:
                    from_at = j
                j += 1
            if into_at is None:
                raise SyntaxError(f"line {line}: SELECT in PL/SQL needs INTO")
            sql = self.text(a, into_at) + " " + self.text(from_at, j)
            targets = [x.strip() for x in split_top(self.text(into_at + 1, from_at))]
            self.i = j + 1
            return {"k": "selinto", "sql": sql, "into": targets, "line": line}
        if u in ("INSERT", "UPDATE", "DELETE", "COMMIT", "ROLLBACK", "SAVEPOINT", "MERGE", "LOCK"):
            sql = self.until()
            self.expect_op(";")
            return {"k": "sql", "sql": sql, "line": line}
        # assignment or procedure call
        a = self.i
        j = self.i
        depth = 0
        while not (self.t[j].kind == "op" and self.t[j].v in (":=", ";") and depth == 0):
            if self.t[j].v == "(":
                depth += 1
            elif self.t[j].v == ")":
                depth -= 1
            j += 1
        if self.t[j].v == ":=":
            target = self.text(a, j)
            self.i = j + 1
            e = self.until()
            self.expect_op(";")
            return {"k": "assign", "target": target, "expr": e, "line": line}
        name = self.next().u
        while self.isop("."):
            self.next(); name += "." + self.next().u
        cargs = self.args() if self.isop("(") else []
        self.expect_op(";")
        return {"k": "call", "name": name, "args": cargs, "line": line}

    def _close_paren(self, j):
        depth = 0
        while True:
            x = self.t[j]
            if x.kind == "op" and x.v == "(":
                depth += 1
            elif x.kind == "op" and x.v == ")":
                depth -= 1
                if depth == 0:
                    return j + 1
            j += 1


# ====================================================================== runtime
class PLRaise(Exception):
    def __init__(self, code, name=None, msg=None):
        super().__init__(msg)
        self.code, self.name = code, name
        self.msg = msg or (f"ORA-{code:05d}: {MSG.get(code, '')}" if code != 1 or name in (None, "DUP_VAL_ON_INDEX") else "User-Defined Exception")
        self.line, self.stack, self.user = None, [], False


class ExitSig(Exception):
    def __init__(self, label):
        self.label = label


class ContinueSig(ExitSig):
    pass


class ReturnSig(Exception):
    def __init__(self, value):
        self.value = value


class Var:
    __slots__ = ("value", "typ", "const")

    def __init__(self, value, typ, const=False):
        self.value, self.typ, self.const = value, typ, const


class Frame:
    def __init__(self, unit=None, trig=None):
        self.scopes = [{}]
        self.unit = unit          # "SCOTT.NAME" for stored code, None for anonymous
        self.trig = trig          # dict(new, old, event) inside a trigger
        self.err = None           # current exception inside a handler

    def find(self, name):
        for sc in reversed(self.scopes):
            if name in sc:
                return sc[name]
        return None


class Interp:
    def __init__(self, sim):
        self.sim = sim
        self.frames = []
        self.pending = None
        self.sqlattr = {"FOUND": None, "NOTFOUND": None, "ROWCOUNT": None, "ISOPEN": 0}
        sim.c.create_function("__S", 1, pl_str)

    @property
    def f(self):
        return self.frames[-1]

    # ---------------------------------------------------------------- types and values
    def basic_type(self, t):
        t = re.sub(r"\s+", "", t.upper())
        m = re.fullmatch(r"(NUMBER|NUMERIC|DECIMAL)(?:\((\d+)(?:,(-?\d+))?\))?", t)
        if m:
            return {"base": "NUMBER", "p": int(m.group(2)) if m.group(2) else None, "s": int(m.group(3)) if m.group(3) else None}
        if t in ("INTEGER", "INT", "PLS_INTEGER", "BINARY_INTEGER", "NATURAL", "POSITIVE", "SMALLINT"):
            return {"base": "NUMBER", "p": None, "s": 0}
        if t in ("FLOAT", "REAL", "BINARY_FLOAT", "BINARY_DOUBLE"):
            return {"base": "NUMBER", "p": None, "s": None}
        m = re.fullmatch(r"(VARCHAR2|VARCHAR|CHAR|NVARCHAR2|NCHAR)(?:\((\d+)(?:BYTE|CHAR)?\))?", t)
        if m:
            return {"base": "CHAR" if m.group(1) in ("CHAR", "NCHAR") else "VARCHAR2", "n": int(m.group(2)) if m.group(2) else (1 if m.group(1) == "CHAR" else 32767)}
        if t in ("DATE", "TIMESTAMP"):
            return {"base": "DATE"}
        if t == "BOOLEAN":
            return {"base": "BOOLEAN"}
        if t in ("LONG", "CLOB", "STRING"):
            return {"base": "VARCHAR2", "n": 32767}
        return None

    def resolve_type(self, t):
        tt = re.sub(r"\s+", "", t.upper())
        m = re.fullmatch(r"(\w+)\.(\w+)%TYPE", tt)
        if m:
            ot = self.sim.types.get((m.group(1), m.group(2)))
            if ot is None:
                raise PLRaise(6550, msg=f"PLS-00302: component '{m.group(2)}' must be declared")
            return self.basic_type(ot) or {"base": "ANY"}
        m = re.fullmatch(r"(\w+)%TYPE", tt)
        if m:
            v = self.f.find(m.group(1))
            return copy.deepcopy(v.typ)
        m = re.fullmatch(r"(\w+)%ROWTYPE", tt)
        if m:
            n = m.group(1)
            if n in self.sim.tdefs:
                return {"base": "REC", "fields": [(c[0], self.basic_type(c[1]) or {"base": "ANY"}) for c in self.sim.tdefs[n]["cols"]]}
            cur = self.f.find("CURSOR:" + n)
            if cur is not None:
                names = self.cursor_columns(cur.value)
                return {"base": "REC", "fields": [(c, {"base": "ANY"}) for c in names]}
            raise PLRaise(6550, msg=f"PLS-00201: identifier '{n}' must be declared")
        rt = self.f.find("TYPE:" + tt)
        if rt is not None:
            return copy.deepcopy(rt.value)
        b = self.basic_type(t)
        if b is None:
            raise SyntaxError(f"unknown type {t}")
        return b

    def coerce(self, v, typ):
        b = typ["base"]
        if v is None:
            return None
        if b == "REC":
            names = [f for f, _ in typ["fields"]]
            if isinstance(v, dict):
                return {f: self.coerce(v.get(f), ft) for f, ft in typ["fields"]}
            return {f: self.coerce(x, ft) for (f, ft), x in zip(typ["fields"], v)}
        if b == "NUMBER":
            if isinstance(v, str):
                try:
                    v = float(v.strip())
                except ValueError:
                    raise PLRaise(6502, "VALUE_ERROR", "ORA-06502: PL/SQL: numeric or value error: character to number conversion error")
            if isinstance(v, bool):
                v = int(v)
            if typ.get("s") is not None:
                from sql_runner import dround
                v = dround(v, typ["s"])
            v = num(float(f"{v:.15g}")) if isinstance(v, float) else v
            p, s = typ.get("p"), typ.get("s") or 0
            if p is not None and abs(v) >= 10 ** (p - s):
                raise PLRaise(6502, "VALUE_ERROR", "ORA-06502: PL/SQL: numeric or value error: number precision too large")
            return v
        if b in ("VARCHAR2", "CHAR"):
            s = pl_str(v)
            if s == "":
                return None
            if len(s) > typ["n"]:
                raise PLRaise(6502, "VALUE_ERROR", "ORA-06502: PL/SQL: numeric or value error: character string buffer too small")
            return s.ljust(typ["n"]) if b == "CHAR" else s
        if b == "BOOLEAN":
            return None if v is None else bool(v)
        return v

    # ---------------------------------------------------------------- substitution and evaluation
    def subst(self, text, sql=False, when=False):
        toks = tokenize(text)
        cols = {c[0] for d in self.sim.tdefs.values() for c in d["cols"]} if sql else set()
        out, last, k = [], 0, 0
        f = self.f

        def emit(a, b, rep):
            nonlocal last
            out.append(text[last:toks[a].s]); out.append(rep); last = toks[b].e

        while k < len(toks):
            t = toks[k]
            nxt = lambda j: toks[k + j] if k + j < len(toks) else None
            if t.kind == "op" and t.v == ":" and nxt(1) and nxt(1).u in ("NEW", "OLD") and nxt(2) and nxt(2).v == "." and f.trig:
                rec = f.trig["new" if nxt(1).u == "NEW" else "old"]
                emit(k, k + 3, lit(rec.get(nxt(3).u) if rec else None)); k += 4; continue
            if t.kind == "id":
                if nxt(1) and nxt(1).v == "%" and nxt(2) and nxt(2).u in ("FOUND", "NOTFOUND", "ROWCOUNT", "ISOPEN"):
                    emit(k, k + 2, lit(self.cursor_attr(t.u, nxt(2).u))); k += 3; continue
                prev = toks[k - 1] if k else None
                if prev is not None and prev.kind == "op" and prev.v == ".":
                    k += 1; continue
                if nxt(1) and nxt(1).v == "." and nxt(2) and nxt(2).kind == "id":
                    v = f.find(t.u)
                    if v is not None and isinstance(v.value, dict) and v.typ["base"] == "REC":
                        if nxt(2).u not in v.value:
                            raise PLRaise(6550, msg=f"PLS-00302: component '{nxt(2).u}' must be declared")
                        emit(k, k + 2, lit(v.value[nxt(2).u])); k += 3; continue
                    if when and t.u in ("NEW", "OLD") and f.trig:
                        rec = f.trig["new" if t.u == "NEW" else "old"]
                        emit(k, k + 2, lit(rec.get(nxt(2).u) if rec else None)); k += 3; continue
                    k += 1; continue
                EV = {"INSERTING": "INSERT", "UPDATING": "UPDATE", "DELETING": "DELETE"}
                if f.trig and t.u == "UPDATING" and nxt(1) and nxt(1).v == "(" and nxt(2) and nxt(3) and nxt(3).v == ")":
                    col = nxt(2).v.strip("'").upper()
                    ok = f.trig["event"] == "UPDATE" and col in (f.trig.get("setcols") or [])
                    emit(k, k + 3, "1" if ok else "0"); k += 4; continue
                if nxt(1) and nxt(1).v == "(":
                    k += 1; continue
                u = t.u
                if u in ("TRUE", "FALSE"):
                    emit(k, k, "1" if u == "TRUE" else "0"); k += 1; continue
                if f.trig and u in ("INSERTING", "UPDATING", "DELETING"):
                    emit(k, k, "1" if f.trig["event"] == EV[u] else "0"); k += 1; continue
                if u in ("SQLCODE", "SQLERRM") and f.err is not None:
                    e = f.err
                    val = (100 if e.code == 1403 else (1 if e.user else -e.code)) if u == "SQLCODE" else e.msg
                    emit(k, k, lit(val)); k += 1; continue
                if u == "SQLERRM":
                    emit(k, k, lit("ORA-0000: normal, successful completion")); k += 1; continue
                if u == "SQLCODE":
                    emit(k, k, "0"); k += 1; continue
                v = f.find(u)
                if v is not None and not (sql and u in cols) and not isinstance(v.value, dict):
                    emit(k, k, lit(v.value)); k += 1; continue
            k += 1
        out.append(text[last:])
        return "".join(out)

    @staticmethod
    def wrap_concat(s):
        def inner(x):
            out, i, q = [], 0, False
            while i < len(x):
                ch = x[i]
                if ch == "'":
                    q = not q
                if not q and ch == "(":
                    j = bal(x, i)
                    out.append("(" + wrap(x[i + 1:j - 1]) + ")")
                    i = j
                    continue
                out.append(ch)
                i += 1
            return "".join(out)

        def wrap(x):
            parts, depth, q, cur, i = [], 0, False, "", 0
            while i < len(x):
                ch = x[i]
                if ch == "'":
                    q = not q
                if not q:
                    if ch == "(":
                        depth += 1
                    elif ch == ")":
                        depth -= 1
                    elif depth == 0 and x.startswith("||", i):
                        parts.append(cur); cur = ""; i += 2
                        continue
                cur += ch
                i += 1
            parts.append(cur)
            if len(parts) == 1:
                return inner(x)
            return " || ".join(f"__S({inner(p)})" for p in parts)
        return wrap(s)

    def _zero_check(self, e):
        q = False
        for i, ch in enumerate(e):
            if ch == "'":
                q = not q
            if q or ch != "/":
                continue
            rest = e[i + 1:].lstrip()
            if not rest:
                continue
            if rest[0] == "(":
                opnd = rest[:bal(rest, 0)]
            else:
                m = re.match(r"-?[\w.]+(\s*\((?:[^()]|\([^()]*\))*\))?|'(?:''|[^'])*'", rest)
                if not m:
                    continue
                opnd = m.group(0)
            if self._raw(opnd) == 0:
                raise PLRaise(1476, "ZERO_DIVIDE")

    def _raw(self, e):
        try:
            v = self.sim.c.execute(self.sim.translate("SELECT " + e)).fetchone()[0]
        except sqlite3.Error as ex:
            if self.pending is not None:
                p, self.pending = self.pending, None
                raise p
            m = re.search(r"ORA-(\d{5}): ?(.*)", str(ex)) or re.search(r"ORA-(\d{5}): ?(.*)", getattr(self.sim, "last_err", "") or "")
            if m:
                code = int(m.group(1))
                if code == 1722:
                    raise PLRaise(6502, "VALUE_ERROR", "ORA-06502: PL/SQL: numeric or value error: character to number conversion error")
                raise PLRaise(code, PREDEF.get(code), f"ORA-{m.group(1)}: {m.group(2)}")
            raise RuntimeError(f"PL/SQL expression failed: {e!r}: {ex}")
        if isinstance(v, float):
            v = num(float(f"{v:.12g}"))
        return v

    def eval(self, text):
        e = self.subst(text)
        if "||" in e:
            e = self.wrap_concat(e)
        if "/" in e:
            self._zero_check(e)
        return self._raw(e)

    def cond(self, text):
        e = self.subst(text)
        if "||" in e:
            e = self.wrap_concat(e)
        return self._raw(f"CASE WHEN ({e}) THEN 1 WHEN NOT ({e}) THEN 0 END") == 1

    # ---------------------------------------------------------------- variables
    def declare(self, d):
        sc = self.f.scopes[-1]
        k = d["k"]
        if k == "var":
            typ = self.resolve_type(d["type"])
            if typ["base"] == "REC":
                val = {f: None for f, _ in typ["fields"]}
            else:
                val = None
            if d["init"] is not None:
                val = self.coerce(self.eval(d["init"]), typ)
            elif d["notnull"]:
                raise SyntaxError("NOT NULL variable needs an initial value")
            sc[d["name"]] = Var(val, typ, d["const"])
        elif k == "cursor":
            sc["CURSOR:" + d["name"]] = Var({"name": d["name"], "query": d["query"], "params": d["params"], "open": False,
                                            "rows": [], "pos": 0, "found": None, "cols": []}, {"base": "CURSOR"})
        elif k == "exc":
            sc["EXC:" + d["name"]] = Var(None, {"base": "EXC"})
        elif k == "pragma":
            v = self.f.find("EXC:" + d["name"])
            v.value = d["code"]
        elif k == "rectype":
            sc["TYPE:" + d["name"]] = Var({"base": "REC", "fields": [(f, self.resolve_type(t)) for f, t in d["fields"]]}, {"base": "TYPE"})

    def assign(self, target, value):
        t = target.strip()
        m = re.fullmatch(r":\s*(NEW|OLD)\s*\.\s*(\w+)", t, re.I)
        if m:
            tr = self.f.trig
            if m.group(1).upper() == "OLD" or tr is None or tr.get("ro"):
                raise PLRaise(4085, msg="ORA-04085: cannot change the value of an OLD reference variable")
            col = m.group(2).upper()
            typ = self.sim.types.get((tr["table"], col))
            tr["new"][col] = self.coerce(value, self.basic_type(typ) if typ else {"base": "ANY"})
            return
        m = re.fullmatch(r"(\w+)\s*\.\s*(\w+)", t)
        if m:
            v = self.f.find(m.group(1).upper())
            if v is None:
                raise PLRaise(6550, msg=f"PLS-00201: identifier '{m.group(1).upper()}' must be declared")
            fld = m.group(2).upper()
            ft = dict(v.typ["fields"]).get(fld, {"base": "ANY"})
            v.value[fld] = self.coerce(value, ft)
            return
        v = self.f.find(t.upper())
        if v is None:
            raise PLRaise(6550, msg=f"PLS-00201: identifier '{t.upper()}' must be declared")
        if v.const:
            raise PLRaise(6550, msg=f"PLS-00363: expression '{t.upper()}' cannot be used as an assignment target")
        v.value = self.coerce(value, v.typ)

    def assign_row(self, targets, row, cols):
        if len(targets) == 1:
            v = self.f.find(targets[0].upper())
            if v is not None and v.typ["base"] == "REC":
                if isinstance(row, dict):
                    v.value = self.coerce(row, v.typ)
                else:
                    v.value = self.coerce(list(row), v.typ)
                return
        if len(targets) != len(row):
            raise PLRaise(6550, msg="PLS-00394: wrong number of values in the INTO list of a FETCH statement")
        for t, x in zip(targets, row):
            self.assign(t, x)

    # ---------------------------------------------------------------- cursors
    def cursor_attr(self, name, attr):
        if name == "SQL":
            return self.sqlattr[attr]
        v = self.f.find("CURSOR:" + name)
        if v is None:
            raise PLRaise(6550, msg=f"PLS-00201: identifier '{name}' must be declared")
        c = v.value
        if attr == "ISOPEN":
            return 1 if c["open"] else 0
        if not c["open"]:
            raise PLRaise(1001, "INVALID_CURSOR")
        if attr == "ROWCOUNT":
            return c["pos"]
        if c["found"] is None:
            return None
        return (1 if c["found"] else 0) if attr == "FOUND" else (0 if c["found"] else 1)

    def run_query(self, q):
        sub = self.subst(q, sql=True)
        sub = re.sub(r"\s+FOR\s+UPDATE(\s+OF\s+[\w\s,.]+)?(\s+NOWAIT)?\s*$", "", sub, flags=re.I)
        self.sim._refresh_dict(sub)
        try:
            cur = self.sim.c.execute(self.sim.translate(sub))
        except sqlite3.Error as ex:
            if self.pending is not None:
                p, self.pending = self.pending, None
                raise p
            raise self.err_from(self.sim._ora(ex, sub))
        rows = cur.fetchall()
        cols = [d[0].upper().split(".")[-1] for d in cur.description]
        return rows, cols

    def cursor_columns(self, c):
        self.f.scopes.append({p: Var(None, {"base": "ANY"}) for p, _ in c["params"]})
        try:
            sub = self.subst(c["query"], sql=True)
            cur = self.sim.c.execute(self.sim.translate(f"SELECT * FROM ({sub}) LIMIT 0"))
            return [d[0].upper().split(".")[-1] for d in cur.description]
        finally:
            self.f.scopes.pop()

    def open_cursor(self, name, cargs):
        v = self.f.find("CURSOR:" + name)
        if v is None:
            raise PLRaise(6550, msg=f"PLS-00201: identifier '{name}' must be declared")
        c = v.value
        if c["open"]:
            raise PLRaise(6511, "CURSOR_ALREADY_OPEN")
        vals = [self.eval(a) for a in cargs]
        sc = {}
        for (p, t), x in zip(c["params"], vals + [None] * (len(c["params"]) - len(vals))):
            sc[p] = Var(self.coerce(x, self.resolve_type(t)), self.resolve_type(t))
        self.f.scopes.append(sc)
        try:
            rows, cols = self.run_query(c["query"])
        finally:
            self.f.scopes.pop()
        c.update(open=True, rows=rows, cols=cols, pos=0, found=None)
        return c

    # ---------------------------------------------------------------- errors
    def err_from(self, text):
        m = re.search(r"ORA-(\d{5}): ?([^\n]*)", text)
        if not m:
            return PLRaise(6550, msg=text.split("\n")[-1])
        code = int(m.group(1))
        e = PLRaise(code, PREDEF.get(code), f"ORA-{m.group(1)}: {m.group(2)}")
        e.full = text.split("\n", 1)[1] if text.startswith("ERROR") else text
        return e

    def matches(self, names, e):
        for n in names:
            if n == "OTHERS" or n == e.name:
                return True
            v = self.f.find("EXC:" + n)
            if v is not None and v.value is not None and -v.value == e.code and not e.user:
                return True
            if v is not None and v.value is not None and e.user and e.name == n:
                return True
            if n in NAME2CODE and NAME2CODE[n] == e.code and not e.user:
                return True
        return False

    # ---------------------------------------------------------------- execution
    def run_block(self, b):
        self.f.scopes.append({})
        try:
            try:
                for d in b["decls"]:
                    try:
                        self.declare(d)
                    except PLRaise as e:
                        if e.line is None:
                            e.line = d["line"]
                        raise
                self.exec_list(b["body"])
            except PLRaise as e:
                for names, stmts in b["handlers"]:
                    if self.matches(names, e):
                        saved = self.f.err
                        self.f.err = e
                        try:
                            self.exec_list(stmts)
                        finally:
                            self.f.err = saved
                        return
                raise
        finally:
            self.f.scopes.pop()

    def exec_list(self, stmts):
        for s in stmts:
            try:
                self.exec(s)
            except PLRaise as e:
                if e.line is None:
                    e.line = s["line"]
                    e.col = s.get("col", 1)
                raise

    def loop_body(self, body, label):
        try:
            self.exec_list(body)
        except ContinueSig as c:
            if c.label not in (None, label):
                raise
        return True

    def exec(self, s):
        k = s["k"]
        if k == "assign":
            self.assign(s["target"], self.eval(s["expr"]))
        elif k == "call":
            self.call(s["name"], s["args"])
        elif k == "if":
            for c, body in s["arms"]:
                if self.cond(c):
                    self.exec_list(body)
                    return
            if s["else"] is not None:
                self.exec_list(s["else"])
        elif k == "case":
            sel = self.eval(s["sel"]) if s["sel"] is not None else None
            for c, body in s["arms"]:
                ok = self.cond(c) if s["sel"] is None else self._raw(f"CASE WHEN {lit(sel)} = ({self.subst(c)}) THEN 1 ELSE 0 END") == 1
                if ok:
                    self.exec_list(body)
                    return
            if s["else"] is None:
                raise PLRaise(6592, "CASE_NOT_FOUND")
            self.exec_list(s["else"])
        elif k == "loop":
            n = 0
            try:
                while True:
                    n += 1
                    if n > 100000:
                        raise RuntimeError("infinite loop")
                    self.loop_body(s["body"], s["label"])
            except ExitSig as x:
                if isinstance(x, ContinueSig) or x.label not in (None, s["label"]):
                    raise
        elif k == "while":
            try:
                n = 0
                while self.cond(s["cond"]):
                    n += 1
                    if n > 100000:
                        raise RuntimeError("infinite loop")
                    self.loop_body(s["body"], s["label"])
            except ExitSig as x:
                if isinstance(x, ContinueSig) or x.label not in (None, s["label"]):
                    raise
        elif k == "fornum":
            lo, hi = self.eval(s["lo"]), self.eval(s["hi"])
            lo, hi = int(round(lo)), int(round(hi))
            rng = range(hi, lo - 1, -1) if s["rev"] else range(lo, hi + 1)
            self.f.scopes.append({})
            try:
                for i in rng:
                    self.f.scopes[-1][s["var"]] = Var(i, {"base": "NUMBER", "p": None, "s": 0}, True)
                    self.loop_body(s["body"], s["label"])
            except ExitSig as x:
                if isinstance(x, ContinueSig) or x.label not in (None, s["label"]):
                    raise
            finally:
                self.f.scopes.pop()
        elif k == "forcur":
            if s["cursor"]:
                c = self.open_cursor(s["cursor"], s["cargs"])
                rows, cols = c["rows"], c["cols"]
            else:
                rows, cols = self.run_query(s["query"])
                c = None
            self.f.scopes.append({})
            try:
                for idx, r in enumerate(rows):
                    if c is not None:
                        c["pos"], c["found"] = idx + 1, True
                    self.f.scopes[-1][s["var"]] = Var(dict(zip(cols, r)), {"base": "REC", "fields": [(x, {"base": "ANY"}) for x in cols]})
                    self.loop_body(s["body"], s["label"])
            except ExitSig as x:
                if isinstance(x, ContinueSig) or x.label not in (None, s["label"]):
                    raise
            finally:
                self.f.scopes.pop()
                if c is not None:
                    c["open"] = False
        elif k in ("exit", "continue"):
            if s["cond"] is None or self.cond(s["cond"]):
                raise (ExitSig if k == "exit" else ContinueSig)(s["label"])
        elif k == "null":
            pass
        elif k == "raise":
            if s["name"] is None:
                if self.f.err is None:
                    raise PLRaise(6550, msg="PLS-00367: a RAISE statement with no exception name must be inside an exception handler")
                e = self.f.err
                e.line = None
                raise e
            n = s["name"]
            v = self.f.find("EXC:" + n)
            if v is not None:
                if v.value is not None:
                    e = PLRaise(-v.value, n, f"ORA-{-v.value:05d}: ")
                else:
                    e = PLRaise(1, n, "User-Defined Exception")
                    e.user = True
                raise e
            if n in NAME2CODE:
                raise PLRaise(NAME2CODE[n], n)
            raise PLRaise(6550, msg=f"PLS-00201: identifier '{n}' must be declared")
        elif k == "return":
            raise ReturnSig(self.eval(s["expr"]) if s["expr"] is not None else None)
        elif k == "block":
            self.run_block(s)
        elif k == "open":
            self.open_cursor(s["cursor"], s["cargs"])
        elif k == "fetch":
            v = self.f.find("CURSOR:" + s["cursor"])
            c = v.value
            if not c["open"]:
                raise PLRaise(1001, "INVALID_CURSOR")
            if c["pos"] < len(c["rows"]):
                self.assign_row(s["into"], c["rows"][c["pos"]], c["cols"])
                c["pos"] += 1
                c["found"] = True
            else:
                c["found"] = False
        elif k == "close":
            v = self.f.find("CURSOR:" + s["cursor"])
            if not v.value["open"]:
                raise PLRaise(1001, "INVALID_CURSOR")
            v.value["open"] = False
        elif k == "selinto":
            rows, cols = self.run_query(s["sql"])
            if not rows:
                self.sqlattr.update(FOUND=0, NOTFOUND=1, ROWCOUNT=0)
                raise PLRaise(1403, "NO_DATA_FOUND")
            if len(rows) > 1:
                self.sqlattr.update(FOUND=1, NOTFOUND=0, ROWCOUNT=len(rows))
                raise PLRaise(1422, "TOO_MANY_ROWS")
            self.sqlattr.update(FOUND=1, NOTFOUND=0, ROWCOUNT=1)
            self.assign_row(s["into"], rows[0], cols)
        elif k == "sql":
            sub = self.subst(s["sql"], sql=True)
            r = self.sim.exec1(sub)
            if r.startswith("ERROR") or "\nORA-" in r[:12]:
                raise self.err_from(r)
            m = re.match(r"(\d+) rows? (created|updated|deleted|merged)", r)
            if m:
                n = int(m.group(1))
                self.sqlattr.update(ROWCOUNT=n, FOUND=1 if n else 0, NOTFOUND=0 if n else 1)
        else:
            raise RuntimeError("unknown statement " + k)

    # ---------------------------------------------------------------- calls
    def call(self, name, args):
        if name in ("DBMS_OUTPUT.PUT_LINE", "DBMS_OUTPUT.PUT"):
            v = self.eval(args[0]) if args else None
            if self.sim.serveroutput:
                s = pl_str(True if v is True else v) if not isinstance(v, bool) else str(v).upper()
                if name.endswith("PUT"):
                    self.sim.partial += s
                else:
                    self.sim.dbms.append(self.sim.partial + s)
                    self.sim.partial = ""
            return
        if name == "DBMS_OUTPUT.NEW_LINE":
            if self.sim.serveroutput:
                self.sim.dbms.append(self.sim.partial)
                self.sim.partial = ""
            return
        if name in ("DBMS_OUTPUT.ENABLE", "DBMS_OUTPUT.DISABLE"):
            return
        if name == "RAISE_APPLICATION_ERROR":
            n = int(self.eval(args[0]))
            msg = pl_str(self.eval(args[1]))
            if not -20999 <= n <= -20000:
                raise PLRaise(21000, msg=f"ORA-21000: error number argument to raise_application_error of {n} is out of range")
            e = PLRaise(-n, None, f"ORA-{-n}: {msg}")
            for sc in self.f.scopes:
                for key, v in sc.items():
                    if key.startswith("EXC:") and v.value == n:
                        e.name = key[4:]
            raise e
        unit = self.sim.procs.get(name)
        if unit is None:
            raise PLRaise(6550, msg=f"PLS-00201: identifier '{name}' must be declared")
        if unit["kind"] == "FUNCTION":
            raise PLRaise(6550, msg=f"PLS-00221: '{name}' is not a procedure or is undefined")
        self.invoke(unit, args)

    def bind(self, unit, args, values=None):
        params = unit["params"]
        pos, named = [], {}
        for a in args:
            m = re.match(r"\s*(\w+)\s*=>\s*(.*)$", a, re.S)
            if m:
                named[m.group(1).upper()] = m.group(2)
            else:
                pos.append(a)
        sc, outs = {}, []
        for i, (pn, mode, pt, default) in enumerate(params):
            typ = self.resolve_type(pt)
            typ_free = dict(typ)
            if typ_free["base"] == "VARCHAR2":
                typ_free["n"] = 32767
            if values is not None:
                val = values[i] if i < len(values) else (self.eval(default) if default else None)
                sc[pn] = Var(self.coerce(val, typ_free), typ_free, mode == "IN")
                continue
            a = pos[i] if i < len(pos) else named.get(pn)
            if a is None:
                if default is None:
                    raise PLRaise(6550, msg=f"PLS-00306: wrong number or types of arguments in call to '{unit['name']}'")
                val = self.eval(default)
            else:
                val = self.eval(a) if mode != "OUT" else None
            sc[pn] = Var(self.coerce(val, typ_free), typ_free, mode == "IN")
            if mode != "IN":
                outs.append((pn, a))
        return sc, outs

    def invoke(self, unit, args, values=None):
        sc, outs = self.bind(unit, args, values)
        fr = Frame(unit=f"{SCHEMA}.{unit['name']}")
        fr.scopes = [sc]
        self.frames.append(fr)
        ret = None
        try:
            try:
                self.run_block(unit["block"])
                if unit["kind"] == "FUNCTION":
                    raise PLRaise(6503, "PROGRAM_ERROR")
            except ReturnSig as r:
                ret = r.value
        except PLRaise as e:
            e.stack.append(f'ORA-06512: at "{fr.unit}", line {e.line}')
            e.line = None
            raise
        finally:
            self.frames.pop()
        for pn, target in outs:
            self.assign(target, sc[pn].value)
        if unit["kind"] == "FUNCTION":
            return self.coerce(ret, self.resolve_type(unit["ret"]))
        return None

    def sql_function(self, name):
        def fn(*vals):
            try:
                if not self.frames:
                    self.frames.append(Frame())
                    try:
                        return self._norm(self.invoke(self.sim.procs[name], [], list(vals)))
                    finally:
                        self.frames.pop()
                return self._norm(self.invoke(self.sim.procs[name], [], list(vals)))
            except PLRaise as e:
                self.pending = e
                self.sim.last_err = e.msg
                raise
        return fn

    @staticmethod
    def _norm(v):
        if isinstance(v, bool):
            return int(v)
        return v

    # ---------------------------------------------------------------- top level
    def run_anonymous(self, src, echo):
        p = Parser(src)
        declare = p.isk("DECLARE")
        if declare:
            p.next()
        b = p.block(declare)
        self.frames.append(Frame())
        try:
            self.run_block(b)
        except PLRaise as e:
            return self.unhandled(e, echo)
        finally:
            self.frames.pop()
        return "PL/SQL procedure successfully completed."

    def unhandled(self, e, echo):
        first = "ORA-06510: PL/SQL: unhandled user-defined exception" if e.user else e.msg
        if getattr(e, "full", None):
            first = e.full
        if e.code == 6550 and not e.stack:
            pos = f"ORA-06550: line {e.line}, column {getattr(e, 'col', 1)}:"
            return "\n".join([echo, "*", "ERROR at line 1:", pos, e.msg, pos, "PL/SQL: Statement ignored"])
        lines = [echo, "*", "ERROR at line 1:", first] + e.stack + [f"ORA-06512: at line {e.line}"]
        return "\n".join(lines)

    def run_trigger(self, trg, event, new, old, setcols=None):
        fr = Frame(unit=f"{SCHEMA}.{trg['name']}", trig={"new": new, "old": old, "event": event, "table": trg["table"], "setcols": setcols,
                                                         "ro": trg["timing"] == "AFTER" or not trg["row"]})
        self.frames.append(fr)
        try:
            if trg["when"] and not self.cond_when(trg["when"]):
                return new
            self.run_block(trg["block"])
            return fr.trig["new"]
        except PLRaise as e:
            e.stack.append(f'ORA-06512: at "{fr.unit}", line {e.line}')
            e.stack.append(f"ORA-04088: error during execution of trigger '{fr.unit}'")
            raise
        finally:
            self.frames.pop()

    def cond_when(self, text):
        e = self.subst(text, when=True)
        return self._raw(f"CASE WHEN ({e}) THEN 1 ELSE 0 END") == 1


# ====================================================================== simulator with PL/SQL
BLOCK_START = re.compile(r"^\s*(DECLARE|BEGIN|CREATE\s+(OR\s+REPLACE\s+)?(PROCEDURE|FUNCTION|TRIGGER|PACKAGE))\b", re.I)


class OraSim3(OraSim2):
    DICT = dict(OraSim2.DICT, USER_TRIGGERS="TRIGGER_NAME, TRIGGER_TYPE, TRIGGERING_EVENT, TABLE_NAME, STATUS",
                USER_PROCEDURES="OBJECT_NAME, OBJECT_TYPE")

    def __init__(self):
        super().__init__()
        self.procs, self.triggers = {}, {}
        self.serveroutput, self.dbms, self.partial = False, [], ""
        self.pl = Interp(self)

    # ---------------------------------------------------------------- splitting
    @staticmethod
    def split(script):
        out, normal, block = [], [], None
        lines = script.split("\n")

        def flush_normal():
            if normal:
                out.extend(OraSim.split("\n".join(normal)))
                normal.clear()

        def complete(txt):
            t = OraSim._outside_strings(txt, lambda p: p)
            st = OraSim.split(txt + "\n;__END__")
            return st and st[-1] == ";__END__" or st == [] or (st and st[-1].endswith("__END__") and st[-1].strip() == "__END__")

        for ln in lines:
            if block is not None:
                if ln.strip() == "/":
                    out.append(strip_comments("\n".join(block)).strip("\n"))
                    block = None
                else:
                    block.append(ln)
                continue
            if BLOCK_START.match(ln) and OraSim3._normal_done(normal):
                flush_normal()
                block = [ln]
                continue
            m = re.match(r"\s*(EXEC|EXECUTE)\s+(.*?);?\s*$", ln, re.I)
            if m and OraSim3._normal_done(normal):
                flush_normal()
                out.append("EXEC " + m.group(2))
                continue
            if re.match(r"\s*(SHOW\s+ERR(ORS)?)\s*;?\s*$", ln, re.I) and OraSim3._normal_done(normal):
                flush_normal()
                out.append("SHOW ERRORS")
                continue
            normal.append(ln)
        flush_normal()
        if block is not None:
            out.append(strip_comments("\n".join(block)).strip("\n"))
        return out

    @staticmethod
    def _normal_done(normal):
        txt = "\n".join(l for l in normal if not l.strip().startswith("--"))
        txt = re.sub(r"(?im)^(\s*(?:DESC|DESCRIBE|CONNECT|CONN|SET\s+\w+)\s+[^;\n]*?)\s*$", r"\1;", txt)
        masked = re.sub(r"'(?:''|[^'])*'", "''", txt)
        return masked.strip() == "" or masked.rstrip().endswith(";")

    def run(self, script, show=True):
        outs = []
        self.dbms, self.partial = [], ""
        for st in self.split(script):
            r = self.exec1(st)
            if self.dbms:
                r = "\n".join(self.dbms) + ("\n\n" + r if r else "")
                self.dbms = []
            if r != "":
                outs.append(r)
        return "\n\n".join(outs) if show else ""

    # ---------------------------------------------------------------- dispatch
    def exec1(self, sql):
        s = sql.strip()
        if BLOCK_START.match(s) or re.match(r"(EXEC|SHOW ERRORS)\b", s, re.I):
            self._commit_if_ddl(s)
            return self._plsql(s)
        s2 = s.rstrip(";").strip()
        u = re.sub(r"\s+", " ", s2.upper())
        if u.startswith("SET SERVEROUTPUT"):
            self.serveroutput = " ON" in u
            return ""
        m = re.match(r"(DROP) (PROCEDURE|FUNCTION|TRIGGER) (\w+)$", u)
        if m:
            return self._drop_unit(m.group(2), m.group(3))
        m = re.match(r"ALTER TRIGGER (\w+) (ENABLE|DISABLE)$", u)
        if m:
            t = self.triggers.get(m.group(1))
            if t is None:
                return "ERROR at line 1:\nORA-04080: trigger '" + m.group(1) + "' does not exist"
            t["enabled"] = m.group(2) == "ENABLE"
            return "Trigger altered."
        m = re.match(r"ALTER TABLE (\w+) (ENABLE|DISABLE) ALL TRIGGERS$", u)
        if m:
            for t in self.triggers.values():
                if t["table"] == m.group(1):
                    t["enabled"] = m.group(2) == "ENABLE"
            return "Table altered."
        for kind, pat in (("INSERT", r"INSERT\s+INTO\s+(\w+)"), ("UPDATE", r"UPDATE\s+(\w+)"), ("DELETE", r"DELETE\s+(?:FROM\s+)?(\w+)")):
            m = re.match(pat, s2, re.I)
            if m and u.startswith(kind) and m.group(1).upper() not in self.vdefs:
                T = m.group(1).upper()
                if any(t["enabled"] and t["table"] == T and kind in t["events"] for t in self.triggers.values()):
                    try:
                        self._seq_check(s2)
                    except OraErr as e:
                        return "ERROR at line 1:\n" + str(e)
                    return self._trig_dml(kind, s2, T)
        if re.match(r"DROP TABLE (\w+)", u):
            T = u.split()[2]
            r = super().exec1(sql)
            if r == "Table dropped.":
                for n in [n for n, t in self.triggers.items() if t["table"] == T]:
                    del self.triggers[n]
            return r
        return super().exec1(sql)

    def _commit_if_ddl(self, s):
        if re.match(r"CREATE", s, re.I):
            self._commit()

    def _drop_unit(self, kind, name):
        if kind == "TRIGGER":
            if name not in self.triggers:
                return f"ERROR at line 1:\nORA-04080: trigger '{name}' does not exist"
            del self.triggers[name]
            return "Trigger dropped."
        if name not in self.procs or self.procs[name]["kind"] != kind:
            return f"ERROR at line 1:\nORA-04043: object {name} does not exist"
        if kind == "FUNCTION":
            self.c.create_function(name, -1, None)
        del self.procs[name]
        return f"{kind.capitalize()} dropped."

    def _plsql(self, s):
        u = s.upper()
        if u.startswith("SHOW ERRORS"):
            return "No errors."
        if u.startswith("EXEC"):
            call = s[4:].strip()
            if call.upper().startswith("UTE "):
                call = call[4:].strip()
            call = call.rstrip(";")
            src = f"BEGIN {call}; END;"
            return self.pl.run_anonymous(src, src)
        m = re.match(r"CREATE\s+(?:OR\s+REPLACE\s+)?(PROCEDURE|FUNCTION|TRIGGER)\s+(\w+)", s, re.I)
        if m:
            kind, name = m.group(1).upper(), m.group(2).upper()
            if not re.match(r"CREATE\s+OR\s+REPLACE", s, re.I) and (name in self.procs or name in self.triggers):
                return "ERROR at line 1:\nORA-00955: name is already used by an existing object"
            if kind == "TRIGGER":
                self._create_trigger(s, name)
                return "Trigger created."
            self._create_unit(s, kind, name, m.end())
            return f"{kind.capitalize()} created."
        echo = s.split("\n", 1)[0].strip()
        return self.pl.run_anonymous(s, echo)

    def _create_unit(self, s, kind, name, pos):
        rest = s[pos:]
        i = len(rest) - len(rest.lstrip())
        params = []
        if rest[i:i + 1] == "(":
            j = bal(rest, i)
            for p in split_top(rest[i + 1:j - 1]):
                mm = re.match(r"(\w+)\s+(?:(IN\s+OUT|IN|OUT)\s+)?(?:NOCOPY\s+)?(.*?)(?:\s*(?::=|\bDEFAULT\b)\s*(.*))?$", p.strip(), re.I | re.S)
                params.append((mm.group(1).upper(), re.sub(r"\s+", " ", (mm.group(2) or "IN").upper()), mm.group(3).strip(), mm.group(4)))
            i = j
        ret = None
        mr = re.match(r"\s*RETURN\s+([\w.%]+)", rest[i:], re.I)
        if mr:
            ret = mr.group(1)
            i += mr.end()
        ma = re.match(r"\s*(IS|AS)\b", rest[i:], re.I)
        start = pos + i + ma.end()
        p = Parser(s, start)
        b = p.block(True)
        unit = {"kind": kind, "name": name, "params": params, "ret": ret, "block": b, "src": s}
        self.procs[name] = unit
        if kind == "FUNCTION":
            self.c.create_function(name, -1, self.pl.sql_function(name))

    def _create_trigger(self, s, name):
        m = re.match(r"CREATE\s+(?:OR\s+REPLACE\s+)?TRIGGER\s+\w+\s+(BEFORE|AFTER)\s+(.*?)\s+ON\s+(\w+)(.*?)(?=\bDECLARE\b|\bBEGIN\b)", s, re.I | re.S)
        timing, ev, table, rest = m.group(1).upper(), m.group(2), m.group(3).upper(), m.group(4)
        events, cols = [], []
        for part in re.split(r"\s+OR\s+", ev.strip(), flags=re.I):
            pm = re.match(r"(INSERT|UPDATE|DELETE)(?:\s+OF\s+(.*))?$", part.strip(), re.I | re.S)
            events.append(pm.group(1).upper())
            if pm.group(2):
                cols += [c.strip().upper() for c in pm.group(2).split(",")]
        row = bool(re.search(r"FOR\s+EACH\s+ROW", rest, re.I))
        when = None
        wm = re.search(r"\bWHEN\s*\(", rest, re.I)
        if wm:
            j = bal(rest, wm.end() - 1)
            when = rest[wm.end():j - 1]
        start = m.end()
        # Oracle numbers trigger body lines from the DECLARE/BEGIN line
        body = s[start:]
        p = Parser(body)
        declare = p.isk("DECLARE")
        if declare:
            p.next()
        b = p.block(declare)
        self.triggers[name] = {"name": name, "timing": timing, "events": events, "cols": cols, "table": table, "row": row,
                               "when": when, "block": b, "enabled": True}

    # ---------------------------------------------------------------- DML with triggers
    def _fire(self, T, timing, event, row, new=None, old=None, setcols=None):
        for t in list(self.triggers.values()):
            if not (t["enabled"] and t["table"] == T and t["timing"] == timing and event in t["events"] and t["row"] == row):
                continue
            if event == "UPDATE" and t["cols"] and setcols is not None and not set(t["cols"]) & set(setcols):
                continue
            new = self.pl.run_trigger(t, event, new, old, setcols)
        return new

    def _trig_dml(self, kind, s, T):
        cols = [c[0] for c in self.tdefs[T]["cols"]]
        self._begin()
        self.c.execute("SAVEPOINT trg")
        n = 0
        try:
            if kind == "INSERT":
                m = re.match(r"INSERT\s+INTO\s+\w+\s*(?:\(([^)]*)\))?\s*(VALUES\s*\((.*)\)|(SELECT\b.*))$", s, re.S | re.I)
                given = [x.strip().upper() for x in m.group(1).split(",")] if m.group(1) else cols
                self._fire(T, "BEFORE", "INSERT", False)
                if m.group(3) is not None:
                    rows = [self.c.execute(self.translate("SELECT " + m.group(3))).fetchone()]
                else:
                    rows = self.c.execute(self.translate(m.group(4))).fetchall()
                for r in rows:
                    new = {c: None for c in cols}
                    for c in cols:
                        d = self.tdefs[T]["cols"][cols.index(c)][3]
                        if c not in given and d is not None:
                            new[c] = self.c.execute(self.translate("SELECT " + d)).fetchone()[0]
                    new.update(zip(given, r))
                    new = self._fire(T, "BEFORE", "INSERT", True, new, None)
                    self.c.execute(f"INSERT INTO {T} ({', '.join(cols)}) VALUES ({', '.join('?' * len(cols))})", [new[c] for c in cols])
                    self._fire(T, "AFTER", "INSERT", True, dict(new), None)
                    n += 1
                self._fire(T, "AFTER", "INSERT", False)
                msg = f"{n} row{'s' if n != 1 else ''} created."
            elif kind == "UPDATE":
                m = re.match(r"UPDATE\s+\w+(?:\s+(?!SET\b)(\w+))?\s+SET\s+(.*?)(?:\s+WHERE\s+(.*))?$", s, re.S | re.I)
                sets = []
                for a in split_top(m.group(2)):
                    c, e = a.split("=", 1)
                    sets.append((c.strip().upper().split(".")[-1], e.strip()))
                setcols = [c for c, _ in sets]
                where = m.group(3) or "1 = 1"
                alias = m.group(1) or T
                self._fire(T, "BEFORE", "UPDATE", False, setcols=setcols)
                rids = [r[0] for r in self.c.execute(self.translate(f"SELECT rowid FROM {T} {alias} WHERE {where}")).fetchall()]
                for rid in rids:
                    old = dict(zip(cols, self.c.execute(f"SELECT {', '.join(cols)} FROM {T} WHERE rowid = ?", (rid,)).fetchone()))
                    vals = self.c.execute(self.translate(f"SELECT {', '.join(e for _, e in sets)} FROM {T} {alias} WHERE rowid = {rid}")).fetchone()
                    new = dict(old)
                    new.update(zip(setcols, vals))
                    new = self._fire(T, "BEFORE", "UPDATE", True, new, dict(old), setcols)
                    changed = [c for c in cols if c in setcols or new[c] != old[c]]
                    self.c.execute(f"UPDATE {T} SET {', '.join(c + ' = ?' for c in changed)} WHERE rowid = ?", [new[c] for c in changed] + [rid])
                    self._fire(T, "AFTER", "UPDATE", True, dict(new), dict(old), setcols)
                    n += 1
                self._fire(T, "AFTER", "UPDATE", False, setcols=setcols)
                msg = f"{n} row{'s' if n != 1 else ''} updated."
            else:
                m = re.match(r"DELETE\s+(?:FROM\s+)?\w+(?:\s+(?!WHERE\b)(\w+))?(?:\s+WHERE\s+(.*))?$", s, re.S | re.I)
                alias = m.group(1) or T
                where = m.group(2) or "1 = 1"
                self._fire(T, "BEFORE", "DELETE", False)
                rids = [r[0] for r in self.c.execute(self.translate(f"SELECT rowid FROM {T} {alias} WHERE {where}")).fetchall()]
                for rid in rids:
                    old = dict(zip(cols, self.c.execute(f"SELECT {', '.join(cols)} FROM {T} WHERE rowid = ?", (rid,)).fetchone()))
                    self._fire(T, "BEFORE", "DELETE", True, None, dict(old))
                    self.c.execute(f"DELETE FROM {T} WHERE rowid = ?", (rid,))
                    self._fire(T, "AFTER", "DELETE", True, None, dict(old))
                    n += 1
                self._fire(T, "AFTER", "DELETE", False)
                msg = f"{n} row{'s' if n != 1 else ''} deleted."
            self.c.execute("RELEASE trg")
            return msg
        except PLRaise as e:
            self.c.execute("ROLLBACK TO trg")
            self.c.execute("RELEASE trg")
            first = getattr(e, "full", None) or e.msg
            return "\n".join(["ERROR at line 1:", first] + e.stack)
        except sqlite3.Error as e:
            self.c.execute("ROLLBACK TO trg")
            self.c.execute("RELEASE trg")
            return self._ora(e, f"{kind} {'INTO ' if kind == 'INSERT' else ('FROM ' if kind == 'DELETE' else '')}{T} x")

    # ---------------------------------------------------------------- dictionary
    def _refresh_dict(self, sql):
        super()._refresh_dict(sql)
        if re.search(r"\bUSER_TRIGGERS\b", sql, re.I):
            self.c.execute("DROP TABLE IF EXISTS USER_TRIGGERS")
            self.c.execute(f"CREATE TABLE USER_TRIGGERS ({self.DICT['USER_TRIGGERS']})")
            for t in self.triggers.values():
                typ = f"{t['timing']} {'EACH ROW' if t['row'] else 'STATEMENT'}"
                self.c.execute("INSERT INTO USER_TRIGGERS VALUES (?, ?, ?, ?, ?)",
                               (t["name"], typ, " OR ".join(t["events"]), t["table"], "ENABLED" if t["enabled"] else "DISABLED"))
        if re.search(r"\bUSER_PROCEDURES\b", sql, re.I):
            self.c.execute("DROP TABLE IF EXISTS USER_PROCEDURES")
            self.c.execute(f"CREATE TABLE USER_PROCEDURES ({self.DICT['USER_PROCEDURES']})")
            for p in self.procs.values():
                self.c.execute("INSERT INTO USER_PROCEDURES VALUES (?, ?)", (p["name"], p["kind"]))
        if re.search(r"\bUSER_OBJECTS\b", sql, re.I):
            for p in self.procs.values():
                self.c.execute("INSERT INTO USER_OBJECTS VALUES (?, ?, 'VALID')", (p["name"], p["kind"]))
            for t in self.triggers.values():
                self.c.execute("INSERT INTO USER_OBJECTS VALUES (?, 'TRIGGER', 'VALID')", (t["name"],))
