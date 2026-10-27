"""Generates step-by-step tables (HTML) for infix->postfix, infix->prefix, postfix/prefix evaluation.
Used by Data Structures Unit 2 so every worked example is produced by the real algorithm (no hand errors)."""
import html

PREC = {"^": 3, "*": 2, "/": 2, "%": 2, "+": 1, "-": 1}
RIGHT = {"^"}


def _tok(expr):
    return [c for c in expr if not c.isspace()]


def to_postfix(expr):
    """Returns (postfix, rows) where rows = [(symbol, stack, output)]."""
    st, out, rows = [], [], []
    for c in _tok(expr):
        if c.isalnum():
            out.append(c)
        elif c == "(":
            st.append(c)
        elif c == ")":
            while st and st[-1] != "(":
                out.append(st.pop())
            st.pop()
        else:
            while st and st[-1] != "(" and (PREC[st[-1]] > PREC[c] or (PREC[st[-1]] == PREC[c] and c not in RIGHT)):
                out.append(st.pop())
            st.append(c)
        rows.append((c, "".join(st), "".join(out)))
    while st:
        out.append(st.pop())
    rows.append(("end", "", "".join(out)))
    return "".join(out), rows


def to_prefix(expr):
    """Reverse method: reverse infix (swap brackets), convert (right-assoc for equal precedence except ^), reverse.
    Returns (prefix, reversed_infix, rows)."""
    rev = []
    for c in reversed(_tok(expr)):
        rev.append({"(": ")", ")": "("}.get(c, c))
    st, out, rows = [], [], []
    for c in rev:
        if c.isalnum():
            out.append(c)
        elif c == "(":
            st.append(c)
        elif c == ")":
            while st and st[-1] != "(":
                out.append(st.pop())
            st.pop()
        else:   # pop only strictly higher precedence (or equal for right-assoc ^)
            while st and st[-1] != "(" and (PREC[st[-1]] > PREC[c] or (PREC[st[-1]] == PREC[c] and c in RIGHT)):
                out.append(st.pop())
            st.append(c)
        rows.append((c, "".join(st), "".join(out)))
    while st:
        out.append(st.pop())
    rows.append(("end", "", "".join(out)))
    return "".join(reversed(out)), "".join(rev), rows


def _apply(a, b, op):
    if op == "+": return a + b
    if op == "-": return a - b
    if op == "*": return a * b
    if op == "/": return a // b
    if op == "%": return a % b
    if op == "^": return a ** b
    raise ValueError(op)


def eval_postfix(tokens):
    """tokens: list of numbers (as str) and operators. Returns (value, rows[(symbol, action, stack)])."""
    st, rows = [], []
    for t in tokens:
        if t in PREC:
            b, a = st.pop(), st.pop()
            r = _apply(a, b, t)
            st.append(r)
            rows.append((t, f"pop {b}, pop {a}; {a} {t} {b} = {r}; push", " ".join(map(str, st))))
        else:
            st.append(int(t))
            rows.append((t, "push", " ".join(map(str, st))))
    return st[-1], rows


def eval_prefix(tokens):
    """Scan right to left. Returns (value, rows)."""
    st, rows = [], []
    for t in reversed(tokens):
        if t in PREC:
            a, b = st.pop(), st.pop()
            r = _apply(a, b, t)
            st.append(r)
            rows.append((t, f"pop {a}, pop {b}; {a} {t} {b} = {r}; push", " ".join(map(str, st))))
        else:
            st.append(int(t))
            rows.append((t, "push", " ".join(map(str, st))))
    return st[-1], rows


def e(s):
    return html.escape(str(s), quote=False)


def table(head, rows):
    h = "<table><tr>" + "".join(f"<th>{e(x)}</th>" for x in head) + "</tr>"
    for r in rows:
        h += "<tr>" + "".join(f"<td>{e(x) if x != '' else '–'}</td>" for x in r) + "</tr>"
    return h + "</table>"


def postfix_table(expr):
    p, rows = to_postfix(expr)
    rows = [(i + 1, s, st, o) for i, (s, st, o) in enumerate(rows)]
    return p, table(["Step", "Symbol", "Stack", "Postfix"], rows)


def prefix_table(expr):
    p, rev, rows = to_prefix(expr)
    rows = [(i + 1, s, st, o) for i, (s, st, o) in enumerate(rows)]
    return p, rev, table(["Step", "Symbol", "Stack", "Output"], rows)


def eval_postfix_table(tokens):
    v, rows = eval_postfix(tokens)
    return v, table(["Symbol", "Action", "Stack"], rows)


def eval_prefix_table(tokens):
    v, rows = eval_prefix(tokens)
    return v, table(["Symbol", "Action", "Stack"], rows)


if __name__ == "__main__":
    for x in ["A+B*C", "(A+B)*C", "A+B*C-D/E", "A*(B+C)/D-E", "A+(B*C-(D/E^F)*G)*H", "A^B^C", "(A+B)*(C-D)"]:
        print(x, "->", to_postfix(x)[0], "| prefix", to_prefix(x)[0])
    print(eval_postfix("5 3 + 8 2 - *".split())[0], eval_postfix("6 2 3 + - 3 8 2 / + * 2 ^ 3 +".split())[0])
    print(eval_prefix("- * + 4 3 2 5".split())[0])
