"""OraSim2: extends OraSim (sql_runner) with a real constraint registry and database objects for RDBMS Unit 4.

- Every table keeps a registry of columns + named constraints (P, U, C, R, NOT NULL as C) with SYS_C names for
  unnamed ones; the SQLite table is regenerated (rebuilt) on ALTER TABLE ADD / DROP / ENABLE / DISABLE CONSTRAINT,
  with Oracle validation errors (ORA-02437, 02299, 02293, 02296, 02298, 01449 ...).
- DML through simple views and synonyms (rewritten to the base table), WITH CHECK OPTION (ORA-01402) and
  WITH READ ONLY (ORA-42399); complex views give ORA-01732, virtual columns ORA-01733.
- Data dictionary: USER_CONSTRAINTS, USER_CONS_COLUMNS, USER_VIEWS, USER_SEQUENCES, USER_SYNONYMS, USER_INDEXES,
  USER_IND_COLUMNS, USER_TABLES, USER_OBJECTS, TAB.
- Indexes: unique / composite, ORA-01408, ORA-01452, ORA-02429; DROP TABLE ... CASCADE CONSTRAINTS (ORA-02449).
"""
import copy
import re
import sqlite3

from sql_runner import OraSim, SCHEMA

KW = {"NOT", "NULL", "CONSTRAINT", "DEFAULT", "CHECK", "UNIQUE", "PRIMARY", "REFERENCES", "ENABLE", "DISABLE"}
KIND = {"P": "PRIMARY", "U": "UNIQUE", "C": "CHECK", "R": "REFERENCES"}


class OraErr(Exception):
    pass


def bal(s, i):
    """s[i] == '(' -> index just after the matching ')'."""
    depth, q = 0, False
    while i < len(s):
        ch = s[i]
        if ch == "'":
            q = not q
        elif not q:
            if ch == "(":
                depth += 1
            elif ch == ")":
                depth -= 1
                if depth == 0:
                    return i + 1
        i += 1
    raise OraErr("ORA-00907: missing right parenthesis")


def split_top(body):
    parts, depth, cur, q = [], 0, "", False
    for ch in body:
        if ch == "'":
            q = not q
        if not q and ch == "," and depth == 0:
            parts.append(cur.strip()); cur = ""
            continue
        if not q:
            depth += ch == "("
            depth -= ch == ")"
        cur += ch
    if cur.strip():
        parts.append(cur.strip())
    return parts


def names(s):
    return [w.upper() for w in re.findall(r"\w+", s)]


def sub_words(text, fn):
    """Apply fn(word) to identifiers outside string literals."""
    return OraSim._outside_strings(text, lambda p: re.sub(r"\b[A-Za-z_]\w*\b", lambda m: fn(m.group(0)), p))


class OraSim2(OraSim):
    def __init__(self):
        super().__init__()
        self.tdefs, self.vdefs, self.indexes = {}, {}, {}
        self._sysn = 8400

    # ------------------------------------------------------------------ helpers
    def _sys(self):
        self._sysn += 1
        return f"SYS_C{self._sysn:06d}"

    def _con(self, name, typ, cols, **kw):
        d = {"name": name or self._sys(), "type": typ, "cols": cols, "cond": None, "rt": None, "rcols": None,
             "rule": "NO ACTION", "status": "ENABLED", "gen": "USER NAME" if name else "GENERATED NAME", "nn": False}
        d.update(kw)
        return d

    def _parse_inline(self, rest, col):
        cons, default, rest = [], None, rest.strip()
        while rest:
            name = None
            m = re.match(r"CONSTRAINT\s+(\w+)\s+", rest, re.I)
            if m:
                name, rest = m.group(1).upper(), rest[m.end():]
            if m := re.match(r"NOT\s+NULL\b", rest, re.I):
                cons.append(self._con(name, "C", [col], cond=f'"{col}" IS NOT NULL', nn=True))
            elif m := re.match(r"NULL\b", rest, re.I):
                pass
            elif m := re.match(r"PRIMARY\s+KEY\b", rest, re.I):
                cons.append(self._con(name, "P", [col]))
            elif m := re.match(r"UNIQUE\b", rest, re.I):
                cons.append(self._con(name, "U", [col]))
            elif m := re.match(r"CHECK\s*(?=\()", rest, re.I):
                e = bal(rest, m.end())
                cons.append(self._con(name, "C", [col], cond=rest[m.end() + 1:e - 1].strip()))
                rest = rest[e:].strip()
                continue
            elif m := re.match(r"REFERENCES\s+(\w+)\s*(\(([^)]*)\))?(\s*ON\s+DELETE\s+(CASCADE|SET\s+NULL))?", rest, re.I):
                cons.append(self._con(name, "R", [col], rt=m.group(1).upper(), rcols=names(m.group(3)) if m.group(3) else None,
                                      rule=re.sub(r"\s+", " ", m.group(5).upper()) if m.group(5) else "NO ACTION"))
            elif m := re.match(r"DEFAULT\s+('(?:''|[^'])*'|\([^)]*\)|[^\s,]+)", rest, re.I):
                default = m.group(1)
            elif m := re.match(r"(ENABLE|DISABLE)\b", rest, re.I):
                if m.group(1).upper() == "DISABLE" and cons:
                    cons[-1]["status"] = "DISABLED"
            else:
                raise OraErr("ORA-00907: missing right parenthesis")
            rest = rest[m.end():].strip()
        return cons, default

    def _parse_tcon(self, text):
        text = text.strip()
        name = None
        m = re.match(r"CONSTRAINT\s+(\w+)\s+", text, re.I)
        if m:
            name, text = m.group(1).upper(), text[m.end():]
        if m := re.match(r"(PRIMARY\s+KEY|UNIQUE)\s*\(([^)]*)\)", text, re.I):
            return self._con(name, "P" if m.group(1).upper().startswith("P") else "U", names(m.group(2)))
        if m := re.match(r"CHECK\s*(?=\()", text, re.I):
            e = bal(text, m.end())
            return self._con(name, "C", [], cond=text[m.end() + 1:e - 1].strip())
        if m := re.match(r"FOREIGN\s+KEY\s*\(([^)]*)\)\s*REFERENCES\s+(\w+)\s*(\(([^)]*)\))?(\s*ON\s+DELETE\s+(CASCADE|SET\s+NULL))?", text, re.I):
            return self._con(name, "R", names(m.group(1)), rt=m.group(2).upper(), rcols=names(m.group(4)) if m.group(4) else None,
                             rule=re.sub(r"\s+", " ", m.group(6).upper()) if m.group(6) else "NO ACTION")
        return None

    def _check_cols(self, cond, T):
        cols = [c[0] for c in self.tdefs[T]["cols"]]
        out = []
        sub_words(cond, lambda w: (out.append(w.upper()) if w.upper() in cols and w.upper() not in out else None) or w)
        return out

    def _pk(self, T):
        return next((c for c in self.tdefs[T]["cons"] if c["type"] == "P"), None)

    def _resolve_fk(self, T, con, tdef=None):
        """Fill rcols and check that the parent key exists (ORA-00942 / ORA-02270)."""
        parent = tdef if con["rt"] == T and tdef is not None else self.tdefs.get(con["rt"])
        if parent is None:
            raise OraErr("ORA-00942: table or view does not exist")
        keys = [c for c in parent["cons"] if c["type"] in ("P", "U")]
        if con["rcols"] is None:
            pk = next((c for c in keys if c["type"] == "P"), None)
            if pk is None:
                raise OraErr("ORA-02268: referenced table does not have a primary key")
            con["rcols"] = list(pk["cols"])
        if not any(c["cols"] == con["rcols"] for c in keys):
            raise OraErr("ORA-02270: no matching unique or primary key for this column-list")

    def _sync_cons(self):
        self.cons = {}
        for T, d in self.tdefs.items():
            for c in d["cons"]:
                if not c["nn"]:
                    self.cons[(T, (c["cols"] or ["*"])[0], KIND[c["type"]])] = c["name"]

    def _ddl(self, T, as_name=None):
        d = self.tdefs[T]
        en = [c for c in d["cons"] if c["status"] == "ENABLED"]
        nn = {c["cols"][0] for c in en if c["nn"]} | {x for c in en if c["type"] == "P" for x in c["cols"]}
        parts = []
        for name, otype, stype, default in d["cols"]:
            p = f"{name} {stype}"
            if default is not None:
                p += f" DEFAULT ({self.translate(default)})" if not re.fullmatch(r"'(?:''|[^'])*'|-?[\d.]+", default) else f" DEFAULT {default}"
            if name in nn:
                p += " NOT NULL"
            parts.append(p)
        for c in en:
            if c["nn"]:
                continue
            cols = ", ".join(c["cols"])
            if c["type"] == "P":
                parts.append(f"CONSTRAINT {c['name']} PRIMARY KEY ({cols})")
            elif c["type"] == "U":
                parts.append(f"CONSTRAINT {c['name']} UNIQUE ({cols})")
            elif c["type"] == "C":
                parts.append(f"CONSTRAINT {c['name']} CHECK ({self.translate(c['cond'])})")
            else:
                rule = "" if c["rule"] == "NO ACTION" else f" ON DELETE {c['rule']}"
                parts.append(f"CONSTRAINT {c['name']} FOREIGN KEY ({cols}) REFERENCES {c['rt']}({', '.join(c['rcols'])}){rule}")
        return f"CREATE TABLE {as_name or T} (" + ", ".join(parts) + ")"

    def _fk_precheck(self, T, con):
        cols, rcols = con["cols"], con["rcols"]
        notnull = " AND ".join(f"c.{x} IS NOT NULL" for x in cols)
        match = " AND ".join(f"p.{b} = c.{a}" for a, b in zip(cols, rcols))
        n = self.c.execute(f"SELECT COUNT(*) FROM {T} c WHERE {notnull} AND NOT EXISTS "
                           f"(SELECT 1 FROM {con['rt']} p WHERE {match})").fetchone()[0]
        if n:
            raise OraErr(f"ORA-02298: cannot validate ({SCHEMA}.{con['name']}) - parent keys not found")

    def _rebuild(self, T, target=None, colmap=None):
        """Regenerate table T from its registry, copying the data; target = constraint being validated."""
        d = self.tdefs[T]
        if target and target["type"] == "R" and target["status"] == "ENABLED":
            self._fk_precheck(T, target)
        new = f"NEW__{T}"
        old_cols = {r[1].upper() for r in self.c.execute(f"PRAGMA table_info({T})").fetchall()}
        colmap = colmap or {}
        pairs = [(c[0], colmap.get(c[0], c[0])) for c in d["cols"]]
        pairs = [(a, b) for a, b in pairs if b in old_cols]
        self.c.execute("PRAGMA foreign_keys = OFF")
        self.c.execute("PRAGMA legacy_alter_table = ON")
        try:
            self.c.execute("BEGIN")
            self.c.execute(self._ddl(T, new))
            if pairs:
                self.c.execute(f"INSERT INTO {new} ({', '.join(a for a, _ in pairs)}) SELECT {', '.join(b for _, b in pairs)} FROM {T}")
            self.c.execute(f"DROP TABLE {T}")
            self.c.execute(f"ALTER TABLE {new} RENAME TO {T}")
            for n, ix in list(self.indexes.items()):
                if ix["table"] == T:
                    if all(x in [c[0] for c in d["cols"]] for x in ix["cols"]):
                        self.c.execute(ix["sql"])
                    else:
                        del self.indexes[n]
            self.c.execute("COMMIT")
        except sqlite3.Error as e:
            self.c.execute("ROLLBACK")
            raise OraErr(self._validate_msg(str(e), target))
        finally:
            self.c.execute("PRAGMA legacy_alter_table = OFF")
            self.c.execute("PRAGMA foreign_keys = ON")
        self._sync_cons()

    @staticmethod
    def _validate_msg(msg, t):
        nm = t["name"] if t else ""
        if "NOT NULL" in msg:
            if t and t["type"] == "P":
                return "ORA-01449: column contains NULL values; cannot alter to NOT NULL"
            return f"ORA-02296: cannot enable ({SCHEMA}.{nm if t and t['gen'] == 'USER NAME' else ''}) - null values found"
        if "UNIQUE" in msg:
            if t and t["type"] == "P":
                return f"ORA-02437: cannot validate ({SCHEMA}.{nm}) - primary key violated"
            return f"ORA-02299: cannot validate ({SCHEMA}.{nm}) - duplicate keys found"
        if "CHECK" in msg:
            return f"ORA-02293: cannot validate ({SCHEMA}.{nm}) - check constraint violated"
        return "ORA-00900: " + msg

    def _children(self, T, con=None):
        """Foreign keys in other tables that reference T (optionally only those using key con)."""
        out = []
        for CT, d in self.tdefs.items():
            for c in d["cons"]:
                if c["type"] == "R" and c["rt"] == T and (con is None or c["rcols"] == con["cols"]) and not (CT == T and c is con):
                    out.append((CT, c))
        return out

    # ------------------------------------------------------------------ CREATE TABLE
    def _create_table(self, sql):
        m = re.match(r"CREATE\s+TABLE\s+(\w+)\s*\((.*)\)\s*$", sql, re.S | re.I)
        if not m:
            super()._create_table(sql)
            T = re.match(r"CREATE\s+TABLE\s+(\w+)", sql, re.I).group(1).upper()
            src = [w.upper() for w in re.findall(r"\bFROM\s+(\w+)|\bJOIN\s+(\w+)", sql, re.I) for w in w if w]
            cols = []
            for r in self.c.execute(f"PRAGMA table_info({T})").fetchall():
                cn = r[1].upper()
                ot = next((self.types[(s, cn)] for s in src if (s, cn) in self.types), r[2].upper() or "NUMBER")
                self.types[(T, cn)] = ot
                cols.append([cn, ot, r[2], None])
            self.tdefs[T] = {"cols": cols, "cons": []}
            return
        T = m.group(1).upper()
        if T in self.tdefs or self.c.execute("SELECT 1 FROM sqlite_master WHERE UPPER(name) = ?", (T,)).fetchone():
            raise OraErr("ORA-00955: name is already used by an existing object")
        d = {"cols": [], "cons": []}
        for part in split_top(m.group(2)):
            con = self._parse_tcon(part)
            if con:
                d["cons"].append(con)
                continue
            cm = re.match(r"(\w+)\s+([A-Za-z0-9_]+(?:\s*\([^)]*\))?)(.*)$", part, re.S)
            cname, otype = cm.group(1).upper(), cm.group(2).upper().replace(" ", "")
            cons, default = self._parse_inline(cm.group(3), cname)
            stype = "NUMERIC" if otype.startswith(("NUMBER", "DECIMAL", "FLOAT", "INTEGER")) else otype
            d["cols"].append([cname, otype, stype, default])
            d["cons"].extend(cons)
        for c in d["cons"]:
            if c["type"] == "C" and not c["cols"]:
                c["cols"] = [x for x in self._check_cols_d(c["cond"], d)]
            if c["type"] == "R":
                self._resolve_fk(T, c, d)
        self.tdefs[T] = d
        for (n, ot, _, _) in d["cols"]:
            self.types[(T, n)] = ot
        try:
            self.c.execute(self._ddl(T))
        except sqlite3.Error:
            del self.tdefs[T]
            raise
        self._sync_cons()

    @staticmethod
    def _check_cols_d(cond, d):
        cols = [c[0] for c in d["cols"]]
        out = []
        sub_words(cond, lambda w: (out.append(w.upper()) if w.upper() in cols and w.upper() not in out else None) or w)
        return out

    # ------------------------------------------------------------------ ALTER TABLE
    def _alter(self, sql):
        m = re.match(r"ALTER\s+TABLE\s+(\w+)\s+(.*)$", sql, re.S | re.I)
        T, rest = m.group(1).upper(), m.group(2).strip()
        if T not in self.tdefs:
            raise OraErr("ORA-00942: table or view does not exist")
        snap = copy.deepcopy(self.tdefs)
        try:
            self._alter_do(T, rest)
        except Exception:
            self.tdefs = snap
            self._sync_cons()
            raise

    def _find(self, T, name):
        c = next((c for c in self.tdefs[T]["cons"] if c["name"] == name.upper()), None)
        if c is None:
            raise OraErr("ORA-02443: Cannot drop constraint  - nonexistent constraint")
        return c

    def _alter_do(self, T, rest):
        d = self.tdefs[T]
        colnames = lambda: [c[0] for c in d["cols"]]
        u = re.sub(r"\s+", " ", rest.upper())
        # ---- ADD constraint(s)
        m = re.match(r"ADD\s*(\(.*\)|.*)$", rest, re.S | re.I)
        if m and re.match(r"ADD\s*\(?\s*(CONSTRAINT|PRIMARY|UNIQUE|CHECK|FOREIGN)\b", rest, re.I):
            body = m.group(1).strip()
            body = body[1:-1] if body.startswith("(") and bal(body, 0) == len(body) else body
            for part in split_top(body):
                con = self._parse_tcon(part)
                if con is None:
                    raise OraErr("ORA-00904: : invalid identifier")
                if any(c["name"] == con["name"] for t in self.tdefs.values() for c in t["cons"]):
                    raise OraErr("ORA-02264: name already used by an existing constraint")
                if con["type"] == "C":
                    con["cols"] = self._check_cols(con["cond"], T)
                for x in con["cols"]:
                    if x not in colnames():
                        raise OraErr(f'ORA-00904: "{x}": invalid identifier')
                if con["type"] == "P" and self._pk(T):
                    raise OraErr("ORA-02260: table can have only one primary key")
                if con["type"] == "R":
                    self._resolve_fk(T, con)
                d["cons"].append(con)
                self._rebuild(T, con)
            return
        # ---- ADD column(s)
        if m:
            body = m.group(1).strip()
            body = body[1:-1] if body.startswith("(") else body
            target = None
            for part in split_top(body):
                cm = re.match(r"(\w+)\s+([A-Za-z0-9_]+(?:\s*\([^)]*\))?)(.*)$", part, re.S)
                cname, otype = cm.group(1).upper(), cm.group(2).upper().replace(" ", "")
                if cname in colnames():
                    raise OraErr("ORA-01430: column being added already exists in table")
                cons, default = self._parse_inline(cm.group(3), cname)
                stype = "NUMERIC" if otype.startswith(("NUMBER", "DECIMAL", "FLOAT", "INTEGER")) else otype
                d["cols"].append([cname, otype, stype, default])
                self.types[(T, cname)] = otype
                for c in cons:
                    if c["type"] == "R":
                        self._resolve_fk(T, c)
                d["cons"].extend(cons)
                target = cons[-1] if cons else target
            self._rebuild(T, target)
            return
        # ---- MODIFY column(s)
        m = re.match(r"MODIFY\s*(.*)$", rest, re.S | re.I)
        if m and not re.match(r"MODIFY\s+CONSTRAINT", rest, re.I):
            body = m.group(1).strip()
            body = body[1:-1] if body.startswith("(") else body
            target = None
            for part in split_top(body):
                cm = re.match(r"(\w+)\s*(.*)$", part, re.S)
                cname, r2 = cm.group(1).upper(), cm.group(2).strip()
                col = next((c for c in d["cols"] if c[0] == cname), None)
                if col is None:
                    raise OraErr(f'ORA-00904: "{cname}": invalid identifier')
                tm = re.match(r"([A-Za-z0-9_]+(?:\s*\([^)]*\))?)", r2)
                if tm and tm.group(1).split("(")[0].upper() not in KW:
                    col[1] = tm.group(1).upper().replace(" ", "")
                    col[2] = "NUMERIC" if col[1].startswith(("NUMBER", "DECIMAL", "FLOAT")) else col[1]
                    self.types[(T, cname)] = col[1]
                    r2 = r2[tm.end():].strip()
                if re.fullmatch(r"NULL", r2, re.I):
                    if not any(c["nn"] and c["cols"] == [cname] for c in d["cons"]):
                        raise OraErr("ORA-01451: column to be modified to NULL cannot be modified to NULL")
                    d["cons"] = [c for c in d["cons"] if not (c["nn"] and c["cols"] == [cname])]
                    continue
                cons, default = self._parse_inline(r2, cname)
                if default is not None:
                    col[3] = default
                for c in cons:
                    if c["nn"] and any(x["nn"] and x["cols"] == [cname] for x in d["cons"]):
                        raise OraErr("ORA-01442: column to be modified to NOT NULL is already NOT NULL")
                    if c["type"] == "R":
                        self._resolve_fk(T, c)
                d["cons"].extend(cons)
                target = cons[-1] if cons else target
            self._rebuild(T, target)
            return
        # ---- DROP / DISABLE / ENABLE constraint
        m = re.match(r"(DROP|DISABLE|ENABLE) (?:CONSTRAINT (\w+)|(PRIMARY KEY)|UNIQUE ?\(([^)]*)\))( CASCADE)?$", u)
        if m:
            act, cascade = m.group(1), bool(m.group(5))
            if m.group(2):
                con = self._find(T, m.group(2))
            elif m.group(3):
                con = self._pk(T)
                if con is None:
                    raise OraErr("ORA-02441: Cannot drop nonexistent primary key")
            else:
                con = next((c for c in d["cons"] if c["type"] == "U" and c["cols"] == names(m.group(4))), None)
                if con is None:
                    raise OraErr("ORA-02442: Cannot drop nonexistent unique key")
            kids = self._children(T, con) if con["type"] in ("P", "U") else []
            if act == "DROP":
                if kids and not cascade:
                    raise OraErr("ORA-02273: this unique/primary key is referenced by some foreign keys")
                for CT, k in kids:
                    self.tdefs[CT]["cons"].remove(k)
                    if CT != T:
                        self._rebuild(CT)
                d["cons"].remove(con)
                self._rebuild(T)
            elif act == "DISABLE":
                live = [(CT, k) for CT, k in kids if k["status"] == "ENABLED"]
                if live and not cascade:
                    raise OraErr(f"ORA-02297: cannot disable constraint ({SCHEMA}.{con['name']}) - dependencies exist")
                for CT, k in live:
                    k["status"] = "DISABLED"
                    if CT != T:
                        self._rebuild(CT)
                con["status"] = "DISABLED"
                self._rebuild(T)
            else:
                if con["type"] == "R":
                    parent_key = next((c for c in self.tdefs[con["rt"]]["cons"] if c["cols"] == con["rcols"] and c["type"] in "PU"), None)
                    if parent_key and parent_key["status"] != "ENABLED":
                        raise OraErr("ORA-02270: no matching unique or primary key for this column-list")
                con["status"] = "ENABLED"
                self._rebuild(T, con)
            return
        # ---- DROP COLUMN
        m = re.match(r"DROP\s+(?:COLUMN\s+(\w+)|\(([^)]*)\))", rest, re.I)
        if m:
            drop = [m.group(1).upper()] if m.group(1) else names(m.group(2))
            for x in drop:
                if x not in colnames():
                    raise OraErr(f'ORA-00904: "{x}": invalid identifier')
                for c in d["cons"]:
                    if c["type"] in ("P", "U") and x in c["cols"] and self._children(T, c):
                        raise OraErr("ORA-12992: cannot drop parent key column")
            d["cols"] = [c for c in d["cols"] if c[0] not in drop]
            d["cons"] = [c for c in d["cons"] if not set(c["cols"]) & set(drop)]
            for x in drop:
                self.types.pop((T, x), None)
            self._rebuild(T)
            return
        # ---- RENAME COLUMN
        m = re.match(r"RENAME\s+COLUMN\s+(\w+)\s+TO\s+(\w+)", rest, re.I)
        if m:
            a, b = m.group(1).upper(), m.group(2).upper()
            col = next((c for c in d["cols"] if c[0] == a), None)
            if col is None:
                raise OraErr(f'ORA-00904: "{a}": invalid identifier')
            col[0] = b
            ren = lambda w: b if w.upper() == a else w
            for c in d["cons"]:
                c["cols"] = [b if x == a else x for x in c["cols"]]
                if c["cond"]:
                    c["cond"] = sub_words(c["cond"], ren).replace(f'"{a}"', f'"{b}"')
            for CT, k in self._children(T):
                k["rcols"] = [b if x == a else x for x in k["rcols"]]
            for ix in self.indexes.values():
                if ix["table"] == T:
                    ix["cols"] = [b if x == a else x for x in ix["cols"]]
                    ix["sql"] = sub_words(ix["sql"], ren)
            self.types[(T, b)] = self.types.pop((T, a), col[1])
            self._rebuild(T, colmap={b: a})
            for CT, k in self._children(T):
                if CT != T:
                    self._rebuild(CT)
            return
        # ---- RENAME TO
        m = re.match(r"RENAME\s+TO\s+(\w+)", rest, re.I)
        if m:
            self._rename(T, m.group(1).upper())
            return
        raise OraErr("ORA-01735: invalid ALTER TABLE option")

    def _rename(self, a, b):
        super()._rename(a, b)
        if a in self.tdefs:
            self.tdefs[b] = self.tdefs.pop(a)
            for d in self.tdefs.values():
                for c in d["cons"]:
                    if c["rt"] == a:
                        c["rt"] = b
            for ix in self.indexes.values():
                if ix["table"] == a:
                    ix["table"] = b
                    ix["sql"] = re.sub(rf"\bON\s+{a}\b", f"ON {b}", ix["sql"], flags=re.I)
            self._sync_cons()

    # ------------------------------------------------------------------ DROP TABLE
    def _drop_table(self, s):
        m = re.match(r"DROP\s+TABLE\s+(\w+)(\s+CASCADE\s+CONSTRAINTS)?(\s+PURGE)?\s*$", s, re.I)
        T = m.group(1).upper()
        if T not in self.tdefs:
            raise OraErr("ORA-00942: table or view does not exist")
        kids = [(CT, k) for CT, k in self._children(T) if CT != T]
        if kids and not m.group(2):
            raise OraErr("ORA-02449: unique/primary keys in table referenced by foreign keys")
        for CT, k in kids:
            self.tdefs[CT]["cons"].remove(k)
            self._rebuild(CT)
        self.c.execute(f"DROP TABLE {T}")
        del self.tdefs[T]
        for n in [n for n, ix in self.indexes.items() if ix["table"] == T]:
            del self.indexes[n]
        self._sync_cons()
        return "Table dropped."

    # ------------------------------------------------------------------ views and synonyms
    def _register_view(self, s):
        m = re.match(r"CREATE\s+(?:OR\s+REPLACE\s+)?(?:FORCE\s+)?VIEW\s+(\w+)(?:\s*\(([^)]*)\))?\s+AS\s+(.*)$", s, re.I | re.S)
        V, collist, body = m.group(1).upper(), m.group(2), m.group(3).strip()
        opt = re.search(r"\s+WITH\s+(CHECK\s+OPTION|READ\s+ONLY)(?:\s+CONSTRAINT\s+\w+)?\s*$", body, re.I)
        kind = opt.group(1).upper().split()[0] if opt else None
        text = body[:opt.start()].strip() if opt else body
        vd = {"text": text, "check": kind == "CHECK", "ro": kind == "READ", "base": None, "map": {}, "where": None, "cols": []}
        core = re.sub(r"\s+ORDER\s+BY\s+[^()]*$", "", text, flags=re.I)
        vcols = [r[1].upper() for r in self.c.execute(f"PRAGMA table_info({V})").fetchall()]
        vd["cols"] = vcols
        simple = not re.search(r"\b(DISTINCT|GROUP\s+BY|UNION|INTERSECT|MINUS|EXCEPT|JOIN|CONNECT|ROWNUM)\b|\b(COUNT|SUM|AVG|MIN|MAX)\s*\(", core, re.I)
        fm = re.match(r"SELECT\s+.*?\s+FROM\s+(\w+)(?:\s+(?!WHERE\b)(\w+))?\s*(?:WHERE\s+(.*))?$", core, re.S | re.I)
        if simple and fm and fm.group(1).upper() in self.tdefs:
            base, alias = fm.group(1).upper(), fm.group(2)
            strip = (lambda x: re.sub(rf"\b{alias}\.", "", x, flags=re.I)) if alias else (lambda x: x)
            bcols = [c[0] for c in self.tdefs[base]["cols"]]
            items = self._select_items(core)
            mp = []
            for it in items:
                it = strip(it)
                if it == "*":
                    mp += [(c, c, True) for c in bcols]
                    continue
                pm = re.fullmatch(r"(\w+)(?:\s+(?:AS\s+)?(\w+))?", it, re.I)
                if pm and pm.group(1).upper() in bcols:
                    mp.append(((pm.group(2) or pm.group(1)).upper(), pm.group(1).upper(), True))
                else:
                    am = re.search(r"\s+(?:AS\s+)?(\w+)$", it, re.I)
                    expr = it[:am.start()] if am else it
                    mp.append(((am.group(1) if am else it).upper(), expr, False))
            if collist:
                mp = [(n, e, p) for n, (_, e, p) in zip(names(collist), mp)]
            vd["base"] = base
            vd["map"] = {n: (e, p) for n, e, p in mp}
            vd["where"] = strip(fm.group(3)).strip() if fm.group(3) else None
        self.vdefs[V] = vd

    def _view_dml(self, kind, s, V):
        vd = self.vdefs[V]
        if vd["ro"]:
            raise OraErr("ORA-42399: cannot perform a DML operation on a read-only view")
        if not vd["base"]:
            raise OraErr("ORA-01732: data manipulation operation not legal on this view")
        base, mp, vw = vd["base"], vd["map"], vd["where"]

        def remap(text):
            def f(w):
                e = mp.get(w.upper())
                if e is None:
                    return w
                return e[0] if e[1] else f"({e[0]})"
            return sub_words(text, f)

        def plain(c):
            e = mp.get(c.upper())
            if e is None:
                raise OraErr(f'ORA-00904: "{c.upper()}": invalid identifier')
            if not e[1]:
                raise OraErr("ORA-01733: virtual column not allowed here")
            return e[0]

        self._begin()
        self.c.execute("SAVEPOINT vdml")
        try:
            if kind == "INSERT":
                m = re.match(r"INSERT\s+INTO\s+\w+\s*(?:\(([^)]*)\))?\s*(VALUES\s*\(.*\)|SELECT\b.*)$", s, re.S | re.I)
                cols = names(m.group(1)) if m.group(1) else vd["cols"]
                bcols = [plain(c) for c in cols]
                before = self.c.execute(f"SELECT COALESCE(MAX(rowid), 0) FROM {base}").fetchone()[0]
                new = f"INSERT INTO {base} ({', '.join(bcols)}) {m.group(2)}"
                n = self._exec_mapped(new)
                rids = f"rowid > {before}"
                msg = f"{n} row{'s' if n != 1 else ''} created."
            elif kind == "UPDATE":
                m = re.match(r"UPDATE\s+\w+\s+SET\s+(.*?)(?:\s+WHERE\s+(.*))?$", s, re.S | re.I)
                sets = []
                for a in split_top(m.group(1)):
                    c, e = a.split("=", 1)
                    sets.append(f"{plain(c.strip())} = {remap(e.strip())}")
                cond = " AND ".join(f"({x})" for x in (vw, remap(m.group(2)) if m.group(2) else None) if x) or "1 = 1"
                ids = [r[0] for r in self.c.execute(self.translate(f"SELECT rowid FROM {base} WHERE {cond}")).fetchall()]
                rids = f"rowid IN ({', '.join(map(str, ids)) or 'NULL'})"
                self._exec_mapped(f"UPDATE {base} SET {', '.join(sets)} WHERE {rids}")
                n = len(ids)
                msg = f"{n} row{'s' if n != 1 else ''} updated."
            else:
                m = re.match(r"DELETE\s+(?:FROM\s+)?\w+(?:\s+WHERE\s+(.*))?$", s, re.S | re.I)
                cond = " AND ".join(f"({x})" for x in (vw, remap(m.group(1)) if m.group(1) else None) if x) or "1 = 1"
                n = self._exec_mapped(f"DELETE FROM {base} WHERE rowid IN (SELECT rowid FROM {base} WHERE {cond})")
                rids = None
                msg = f"{n} row{'s' if n != 1 else ''} deleted."
            if vd["check"] and vw and rids:
                bad = self.c.execute(self.translate(f"SELECT COUNT(*) FROM {base} WHERE {rids} AND COALESCE(({vw}), 0) = 0")).fetchone()[0]
                if bad:
                    raise OraErr("ORA-01402: view WITH CHECK OPTION where-clause violation")
            self.c.execute("RELEASE vdml")
            return msg
        except Exception:
            self.c.execute("ROLLBACK TO vdml")
            self.c.execute("RELEASE vdml")
            raise

    def _exec_mapped(self, sql):
        try:
            return self.c.execute(self.translate(sql)).rowcount
        except sqlite3.Error as e:
            raise OraErr(self._ora(e, sql).split("\n", 1)[1])

    # ------------------------------------------------------------------ indexes
    def _create_index(self, s):
        m = re.match(r"CREATE\s+(UNIQUE\s+)?INDEX\s+(\w+)\s+ON\s+(\w+)\s*\((.*)\)\s*$", s, re.I | re.S)
        uq, n, T, body = bool(m.group(1)), m.group(2).upper(), m.group(3).upper(), m.group(4)
        if T not in self.tdefs:
            raise OraErr("ORA-00942: table or view does not exist")
        if n in self.indexes or self.c.execute("SELECT 1 FROM sqlite_master WHERE UPPER(name) = ?", (n,)).fetchone():
            raise OraErr("ORA-00955: name is already used by an existing object")
        cols = [re.sub(r"\s+(ASC|DESC)$", "", p, flags=re.I).strip().upper() for p in split_top(body)]
        same = [c["cols"] for c in self.tdefs[T]["cons"] if c["type"] in "PU" and c["status"] == "ENABLED"]
        same += [ix["cols"] for ix in self.indexes.values() if ix["table"] == T]
        if cols in same:
            raise OraErr("ORA-01408: such column list already indexed")
        sql = f"CREATE {'UNIQUE ' if uq else ''}INDEX {n} ON {T} ({body})"
        try:
            self.c.execute(sql)
        except sqlite3.IntegrityError:
            raise OraErr("ORA-01452: cannot CREATE UNIQUE INDEX; duplicate keys found")
        self.indexes[n] = {"table": T, "cols": cols, "unique": uq, "sql": sql}
        return "Index created."

    def _drop_index(self, s):
        n = s.split()[2].upper()
        if any(c["name"] == n and c["type"] in "PU" for d in self.tdefs.values() for c in d["cons"]):
            raise OraErr("ORA-02429: cannot drop index used for enforcement of unique/primary key")
        if n not in self.indexes:
            raise OraErr("ORA-01418: specified index does not exist")
        self.c.execute(f"DROP INDEX {n}")
        del self.indexes[n]
        return "Index dropped."

    def _alter_index(self, s):
        m = re.match(r"ALTER\s+INDEX\s+(\w+)\s+(RENAME\s+TO\s+(\w+)|REBUILD.*|UNUSABLE|VISIBLE|INVISIBLE)$", s, re.I | re.S)
        n = m.group(1).upper()
        if n not in self.indexes:
            raise OraErr("ORA-01418: specified index does not exist")
        if m.group(3):
            new = m.group(3).upper()
            ix = self.indexes.pop(n)
            self.c.execute(f"DROP INDEX {n}")
            ix["sql"] = re.sub(rf"\bINDEX\s+{n}\b", f"INDEX {new}", ix["sql"], flags=re.I)
            self.c.execute(ix["sql"])
            self.indexes[new] = ix
        return "Index altered."

    # ------------------------------------------------------------------ data dictionary
    DICT = {
        "USER_CONSTRAINTS": "OWNER, CONSTRAINT_NAME, CONSTRAINT_TYPE, TABLE_NAME, SEARCH_CONDITION, R_OWNER, R_CONSTRAINT_NAME, DELETE_RULE, STATUS, GENERATED",
        "USER_CONS_COLUMNS": "OWNER, CONSTRAINT_NAME, TABLE_NAME, COLUMN_NAME, POSITION",
        "USER_VIEWS": "VIEW_NAME, TEXT_LENGTH, TEXT, READ_ONLY",
        "USER_SEQUENCES": "SEQUENCE_NAME, MIN_VALUE, MAX_VALUE, INCREMENT_BY, CYCLE_FLAG, ORDER_FLAG, CACHE_SIZE, LAST_NUMBER",
        "USER_SYNONYMS": "SYNONYM_NAME, TABLE_OWNER, TABLE_NAME, DB_LINK",
        "USER_INDEXES": "INDEX_NAME, INDEX_TYPE, TABLE_OWNER, TABLE_NAME, UNIQUENESS, STATUS",
        "USER_IND_COLUMNS": "INDEX_NAME, TABLE_NAME, COLUMN_NAME, COLUMN_POSITION, DESCEND",
        "USER_TABLES": "TABLE_NAME, TABLESPACE_NAME, STATUS",
        "USER_OBJECTS": "OBJECT_NAME, OBJECT_TYPE, STATUS",
        "TAB": "TNAME, TABTYPE, CLUSTERID",
    }

    def _refresh_dict(self, sql):
        used = [k for k in self.DICT if re.search(rf"\b{k}\b", sql, re.I)]
        if not used:
            return
        rows = {k: [] for k in self.DICT}
        for T, d in self.tdefs.items():
            for c in d["cons"]:
                rname = None
                if c["type"] == "R":
                    rname = next((k["name"] for k in self.tdefs.get(c["rt"], {"cons": []})["cons"]
                                  if k["type"] in "PU" and k["cols"] == c["rcols"]), None)
                rows["USER_CONSTRAINTS"].append((SCHEMA, c["name"], c["type"], T, c["cond"], SCHEMA if rname else None, rname,
                                                 c["rule"] if c["type"] == "R" else None, c["status"], c["gen"]))
                for i, x in enumerate(c["cols"], 1):
                    rows["USER_CONS_COLUMNS"].append((SCHEMA, c["name"], T, x, i if c["type"] in "PUR" else None))
                if c["type"] in "PU":
                    rows["USER_INDEXES"].append((c["name"], "NORMAL", SCHEMA, T, "UNIQUE", "VALID"))
                    for i, x in enumerate(c["cols"], 1):
                        rows["USER_IND_COLUMNS"].append((c["name"], T, x, i, "ASC"))
            rows["USER_TABLES"].append((T, "USERS", "VALID"))
            rows["USER_OBJECTS"].append((T, "TABLE", "VALID"))
            rows["TAB"].append((T, "TABLE", None))
        for n, ix in self.indexes.items():
            rows["USER_INDEXES"].append((n, "NORMAL", SCHEMA, ix["table"], "UNIQUE" if ix["unique"] else "NONUNIQUE", "VALID"))
            rows["USER_OBJECTS"].append((n, "INDEX", "VALID"))
            for i, x in enumerate(ix["cols"], 1):
                rows["USER_IND_COLUMNS"].append((n, ix["table"], x, i, "ASC"))
        for V, vd in self.vdefs.items():
            if V in self.synonyms:
                rows["USER_SYNONYMS"].append((V, SCHEMA, self.synonyms[V], None))
                rows["USER_OBJECTS"].append((V, "SYNONYM", "VALID"))
                rows["TAB"].append((V, "SYNONYM", None))
            else:
                txt = re.sub(r"\s+", " ", vd["text"])
                rows["USER_VIEWS"].append((V, len(vd["text"]), txt, "Y" if vd["ro"] else "N"))
                rows["USER_OBJECTS"].append((V, "VIEW", "VALID"))
                rows["TAB"].append((V, "VIEW", None))
        for n, sq in self.seqs.items():
            cache = sq.get("cache", 20)
            if sq["cur"] is None:
                last = sq["start"]
            elif cache == 0:
                last = sq["cur"] + sq["inc"]
            else:
                used_n = (sq["cur"] - sq["start"]) // sq["inc"] + 1
                last = sq["start"] + sq["inc"] * cache * (-(-used_n // cache))
            rows["USER_SEQUENCES"].append((n, sq.get("min") or 1, sq.get("max") or "1.0000E+28", sq["inc"],
                                           "Y" if sq.get("cycle") else "N", "N", cache, last))
            rows["USER_OBJECTS"].append((n, "SEQUENCE", "VALID"))
        for k in used:
            self.c.execute(f"DROP TABLE IF EXISTS {k}")
            self.c.execute(f"CREATE TABLE {k} ({self.DICT[k]})")
            cols = self.DICT[k].count(",") + 1
            self.c.executemany(f"INSERT INTO {k} VALUES ({', '.join('?' * cols)})", rows[k])

    def _desc(self, t):
        T = t.upper()
        vd = self.vdefs.get(T)
        if vd is None or T in self.synonyms:
            return super()._desc(t)
        data = []
        base = vd["base"]
        nn = set()
        if base:
            d = self.tdefs[base]
            nn = {c["cols"][0] for c in d["cons"] if c["nn"] and c["status"] == "ENABLED"}
            nn |= {x for c in d["cons"] if c["type"] == "P" and c["status"] == "ENABLED" for x in c["cols"]}
        for col in vd["cols"]:
            e = vd["map"].get(col)
            if base and e and e[1]:
                data.append((col, "NOT NULL" if e[0] in nn else "", self.types.get((base, e[0]), "NUMBER")))
            else:
                typ = next((v for (tb, cn), v in self.types.items() if cn == col), "NUMBER")
                data.append((col, "", typ))
        w = max(len(r[0]) for r in data + [("Name", 0, 0)]) + 1
        out = [f" {'Name'.ljust(w)} {'Null?'.ljust(8)} Type", f" {'-' * w} {'-' * 8} {'-' * max(4, max(len(r[2]) for r in data))}"]
        out += [f" {r[0].ljust(w)} {r[1].ljust(8)} {r[2]}" for r in data]
        return "\n".join(out)

    # ------------------------------------------------------------------ errors
    def _ora(self, e, sql):
        msg = str(e)
        m = re.search(r"NOT NULL constraint failed: (\w+)\.(\w+)", msg)
        if m and re.match(r"\s*UPDATE", sql, re.I):
            return f'ERROR at line 1:\nORA-01407: cannot update ("{SCHEMA}"."{m.group(1).upper()}"."{m.group(2).upper()}") to NULL'
        m = re.search(r"UNIQUE constraint failed: (.*)", msg)
        if m:
            parts = [p.strip().split(".") for p in m.group(1).split(",")]
            T, cols = parts[0][0].upper(), sorted(p[-1].upper() for p in parts)
            cn = next((c["name"] for c in self.tdefs.get(T, {"cons": []})["cons"] if c["type"] in "PU" and sorted(c["cols"]) == cols), None)
            cn = cn or next((n for n, ix in self.indexes.items() if ix["table"] == T and sorted(ix["cols"]) == cols), None)
            if cn:
                return f"ERROR at line 1:\nORA-00001: unique constraint ({SCHEMA}.{cn}) violated"
        if "FOREIGN KEY constraint failed" in msg:
            t = re.search(r"(?:INTO|UPDATE|FROM)\s+(\w+)", sql, re.I)
            T = t.group(1).upper() if t else ""
            own = [c for c in self.tdefs.get(T, {"cons": []})["cons"] if c["type"] == "R" and c["status"] == "ENABLED"]
            kids = [k for _, k in self._children(T) if k["status"] == "ENABLED"]
            parent_side = re.match(r"\s*DELETE", sql, re.I) or (re.match(r"\s*UPDATE", sql, re.I) and not own)
            if parent_side and kids:
                return f"ERROR at line 1:\nORA-02292: integrity constraint ({SCHEMA}.{kids[0]['name']}) violated - child record found"
            if own:
                return f"ERROR at line 1:\nORA-02291: integrity constraint ({SCHEMA}.{own[0]['name']}) violated - parent key not found"
        return super()._ora(e, sql)

    # ------------------------------------------------------------------ dispatch
    def exec1(self, sql):
        s = sql.strip().rstrip(";").strip()
        u = re.sub(r"\s+", " ", s.upper())
        try:
            if u.startswith(("SELECT", "WITH", "INSERT", "UPDATE", "DELETE")):
                self._seq_check(s)
            if u.startswith(("SELECT", "WITH")):
                self._refresh_dict(s)
            for kind, pat in (("INSERT", r"INSERT\s+INTO\s+(\w+)"), ("UPDATE", r"UPDATE\s+(\w+)"), ("DELETE", r"DELETE\s+(?:FROM\s+)?(\w+)")):
                m = re.match(pat, s, re.I)
                if m and u.startswith(kind) and m.group(1).upper() in self.vdefs:
                    return self._view_dml(kind, s, m.group(1).upper())
            if u.startswith("DROP TABLE"):
                self._commit()
                return self._drop_table(s)
            if re.match(r"CREATE (UNIQUE )?INDEX", u):
                self._commit()
                return self._create_index(s)
            if u.startswith("DROP INDEX"):
                self._commit()
                return self._drop_index(s)
            if u.startswith("ALTER INDEX"):
                self._commit()
                return self._alter_index(s)
            if re.match(r"CREATE (OR REPLACE )?(FORCE )?VIEW", u):
                V = re.match(r"CREATE\s+(?:OR\s+REPLACE\s+)?(?:FORCE\s+)?VIEW\s+(\w+)", s, re.I).group(1).upper()
                if V in self.tdefs or (V in self.vdefs and not u.startswith("CREATE OR REPLACE")):
                    raise OraErr("ORA-00955: name is already used by an existing object")
                r = super().exec1(sql)
                if r == "View created.":
                    self._register_view(s)
                return r
            if u.startswith("DROP VIEW"):
                V = s.split()[2].upper()
                if V not in self.vdefs or V in self.synonyms:
                    raise OraErr("ORA-00942: table or view does not exist")
                r = super().exec1(sql)
                self.vdefs.pop(V, None)
                return r
            m = re.match(r"CREATE (?:OR REPLACE )?(?:PUBLIC )?SYNONYM (\w+) FOR (\w+)", u)
            if m:
                if m.group(2) not in self.tdefs and m.group(2) not in self.vdefs:
                    pass  # Oracle allows a synonym for a missing object; it fails when used
                r = super().exec1(sql)
                if r == "Synonym created.":
                    tgt = m.group(2)
                    base = copy.deepcopy(self.vdefs[tgt]) if tgt in self.vdefs else None
                    if base is None and tgt in self.tdefs:
                        cols = [c[0] for c in self.tdefs[tgt]["cols"]]
                        base = {"text": f"SELECT * FROM {tgt}", "check": False, "ro": False, "base": tgt,
                                "map": {c: (c, True) for c in cols}, "where": None, "cols": cols}
                    if base:
                        self.vdefs[m.group(1)] = base
                return r
            if u.startswith(("DROP SYNONYM", "DROP PUBLIC SYNONYM")):
                n = s.split()[-1].upper()
                if n not in self.synonyms:
                    raise OraErr("ORA-01434: private synonym to be dropped does not exist")
                r = super().exec1(sql)
                self.vdefs.pop(n, None)
                return r
            m = re.match(r"(CREATE|ALTER) SEQUENCE (\w+)", u)
            if m:
                if m.group(1) == "CREATE" and m.group(2) in self.seqs:
                    raise OraErr("ORA-00955: name is already used by an existing object")
                if m.group(1) == "ALTER" and m.group(2) not in self.seqs:
                    raise OraErr("ORA-02289: sequence does not exist")
                if m.group(1) == "ALTER" and "START WITH" in u:
                    raise OraErr("ORA-02283: cannot alter starting sequence number")
                r = super().exec1(sql)
                sq = self.seqs[m.group(2)]
                c = re.search(r"\bCACHE (\d+)", u)
                if "NOCACHE" in u:
                    sq["cache"] = 0
                elif c:
                    sq["cache"] = int(c.group(1))
                else:
                    sq.setdefault("cache", 20)
                return r
            if u.startswith("DROP SEQUENCE") and u.split()[2] not in self.seqs:
                raise OraErr("ORA-02289: sequence does not exist")
            return super().exec1(sql)
        except OraErr as e:
            return "ERROR at line 1:\n" + str(e)
        except sqlite3.Error as e:
            return self._ora(e, s)

    def _seq_check(self, sql):
        for n in re.findall(r"\b(\w+)\.(?:NEXTVAL|CURRVAL)\b", sql, re.I):
            if n.upper() not in self.seqs:
                raise OraErr("ORA-02289: sequence does not exist")
