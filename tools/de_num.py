"""Number-system tool for DE Unit 1. Every conversion / complement step table (EN + GU) comes from here.
All arithmetic is exact (fractions.Fraction); results are cross-checked with Python's int(x, base)."""
from fractions import Fraction
from html import escape as e

DIG = "0123456789ABCDEF"
BASE_NAME = {2: ("binary", "binary"), 8: ("octal", "octal"), 10: ("decimal", "decimal"), 16: ("hexadecimal", "hexadecimal")}


def tbl(head_en, head_gu, rows):
    def one(head):
        h = "<table><tr>" + "".join(f"<th>{e(str(x))}</th>" for x in head) + "</tr>"
        for r in rows:
            h += "<tr>" + "".join(f"<td>{x}</td>" for x in r) + "</tr>"
        return h + "</table>"
    return one(head_en), one(head_gu)


def sub(n, b):
    return f"({n})<sub>{b}</sub>"


# ---------------------------------------------------------------- decimal integer -> base (repeated division)
def int_to_base(n, b):
    rows, q = [], n
    if n == 0:
        return "0", tbl(["Divide", "Quotient", "Remainder"], ["ભાગાકાર", "ભાગફળ", "શેષ"], [("0", "0", "0")])
    while q > 0:
        rows.append((f"{q} ÷ {b}", q // b, f"<b>{DIG[q % b]}</b>" + (f" ({q % b})" if q % b > 9 else "")))
        q //= b
    res = "".join(DIG[int(r[2].split("<b>")[1][0], 16)] if False else r[2][3] for r in rows)[::-1]
    assert int(res, b) == n
    return res, tbl(["Divide", "Quotient", "Remainder"], ["ભાગાકાર", "ભાગફળ", "શેષ"], rows)


# ---------------------------------------------------------------- decimal fraction -> base (repeated multiplication)
def frac_to_base(f, b, places=6):
    f = Fraction(f)
    rows, digits = [], ""
    for _ in range(places):
        if f == 0:
            break
        p = f * b
        d = int(p)
        rows.append((f"{float(f):g} × {b}", f"{float(p):g}", f"<b>{DIG[d]}</b>"))
        digits += DIG[d]
        f = p - d
    exact = f == 0
    return digits, exact, tbl(["Multiply", "Product", "Integer part"], ["ગુણાકાર", "ગુણનફળ", "પૂર્ણાંક ભાગ"], rows)


# ---------------------------------------------------------------- any base -> decimal (positional weights)
def to_decimal(s, b):
    s = s.upper()
    ip, _, fp = s.partition(".")
    terms, total = [], Fraction(0)
    for i, ch in enumerate(ip):
        p = len(ip) - 1 - i
        v = DIG.index(ch)
        terms.append((ch, f"{b}<sup>{p}</sup>", b ** p, v * b ** p))
        total += v * b ** p
    for i, ch in enumerate(fp):
        p = -(i + 1)
        v = DIG.index(ch)
        w = Fraction(1, b ** (i + 1))
        terms.append((ch, f"{b}<sup>{p}</sup>", f"{float(w):g}", f"{float(v * w):g}"))
        total += v * w
    expr = " + ".join(f"{DIG.index(t[0])}×{t[1]}" for t in terms)
    rows = [(t[0] + (f" ({DIG.index(t[0])})" if DIG.index(t[0]) > 9 else ""), t[1], t[2], t[3]) for t in terms]
    if not fp:
        assert int(total) == int(ip, b)
    return total, expr, tbl(["Digit", "Weight", "Weight value", "Digit × weight"], ["Digit", "Weight", "Weight ની કિંમત", "Digit × weight"], rows)


def fmt(fr):
    return str(int(fr)) if fr.denominator == 1 else f"{float(fr):g}"


# ---------------------------------------------------------------- binary <-> octal / hex grouping
def bin_group(bits, k):
    """bits may contain '.', groups of k from the point outward"""
    ip, _, fp = bits.partition(".")
    ip = ip.zfill((len(ip) + k - 1) // k * k)
    fp = fp.ljust((len(fp) + k - 1) // k * k, "0") if fp else ""
    gi = [ip[i:i + k] for i in range(0, len(ip), k)]
    gf = [fp[i:i + k] for i in range(0, len(fp), k)]
    di = "".join(DIG[int(g, 2)] for g in gi).lstrip("0") or "0"
    df = "".join(DIG[int(g, 2)] for g in gf)
    res = di + ("." + df if df else "")
    rows = [(g, DIG[int(g, 2)]) for g in gi] + ([(".", ".")] if gf else []) + [(g, DIG[int(g, 2)]) for g in gf]
    return res, gi, gf, tbl(["Group", "Digit"], ["Group", "Digit"], rows)


def to_bin_from(s, base):
    k = {8: 3, 16: 4}[base]
    s = s.upper()
    ip, _, fp = s.partition(".")
    gi = [format(DIG.index(c), f"0{k}b") for c in ip]
    gf = [format(DIG.index(c), f"0{k}b") for c in fp]
    res = ("".join(gi).lstrip("0") or "0") + ("." + "".join(gf).rstrip("0") if gf else "")
    rows = [(c, g) for c, g in zip(ip, gi)] + ([(".", ".")] if gf else []) + [(c, g) for c, g in zip(fp, gf)]
    return res, tbl(["Digit", f"{k}-bit binary"], ["Digit", f"{k}-bit binary"], rows)


# ---------------------------------------------------------------- binary arithmetic
def ones(s):
    return "".join("1" if c == "0" else "0" for c in s)


def twos(s):
    n = len(s)
    return format((int(ones(s), 2) + 1) % (2 ** n), f"0{n}b")


def add_bits(a, b):
    """column addition with carry row; returns (sum string, carry_out, carries list)"""
    n = max(len(a), len(b))
    a, b = a.zfill(n), b.zfill(n)
    c, out, carries = 0, [], []
    for i in range(n - 1, -1, -1):
        s = int(a[i]) + int(b[i]) + c
        carries.append(c)
        out.append(str(s % 2))
        c = s // 2
    return "".join(reversed(out)), c, list(reversed(carries))


def add_table(a, b):
    n = max(len(a), len(b))
    s, c, cr = add_bits(a, b)
    width = n + 1
    carry_row = ("1" if c else " ") + "".join(str(x) for x in cr[1:]) + " "
    rows = [("Carry", " ".join(("1" if c else "") .rjust(1) for _ in [0]) + " " + " ".join(str(x) for x in (cr[1:] + [0])) if False else ""),]
    res = ("1" if c else "") + s
    assert int(res, 2) == int(a, 2) + int(b, 2)
    return res, c


def col_html(lines):
    """right-aligned monospace block (works in the app's <pre>)"""
    w = max(len(x) for _, x in lines)
    return "<pre>" + "\n".join(f"{lab:<9}{x.rjust(w)}" for lab, x in lines) + "</pre>"


def add_work(a, b):
    n = max(len(a), len(b))
    a2, b2 = a.zfill(n), b.zfill(n)
    s, c, cr = add_bits(a2, b2)
    carry_str = (("1" if c else " ") + "".join("1" if x else " " for x in cr[:-1]))
    res = ("1" if c else "") + s
    assert int(res, 2) == int(a, 2) + int(b, 2)
    lines = [("Carry", carry_str.rstrip() and carry_str + " "), ("", " " + a2), ("+", " " + b2), ("", "-" * (n + 1)), ("Sum", res.rjust(n + 1))]
    return res, col_html([(l, x) for l, x in lines if x is not None])


def sub_direct(a, b):
    """direct binary subtraction a - b (a >= b) with borrow"""
    n = max(len(a), len(b))
    a2, b2 = a.zfill(n), b.zfill(n)
    r = int(a2, 2) - int(b2, 2)
    assert r >= 0
    res = format(r, f"0{n}b")
    return res, col_html([("", a2), ("-", b2), ("", "-" * n), ("Diff", res)])


def sub_ones(a, b):
    """a - b using 1's complement. returns steps (en, gu) and result string with sign"""
    n = max(len(a), len(b))
    a2, b2 = a.zfill(n), b.zfill(n)
    c1 = ones(b2)
    s, carry, _ = add_bits(a2, c1)
    st_en, st_gu = [], []
    st_en.append(f"Make both numbers {n} bits: A = {a2}, B = {b2}.")
    st_gu.append(f"બંને numbers ને {n} bits ના બનાવો: A = {a2}, B = {b2}.")
    st_en.append(f"1's complement of B = <b>{c1}</b>.")
    st_gu.append(f"B નો 1's complement = <b>{c1}</b>.")
    work = col_html([("", " " + a2), ("+", " " + c1), ("", "-" * (n + 1)), ("", ("1" if carry else " ") + s)])
    if carry:
        final = format(int(s, 2) + 1, f"0{n}b")[-n:]
        work2 = col_html([("", s), ("+ carry", "1".rjust(n)), ("", "-" * n), ("", final)])
        st_en.append("Add A and the 1's complement of B:" + work)
        st_gu.append("A અને B ના 1's complement નો સરવાળો કરો:" + work)
        st_en.append("A carry is generated, so the result is <b>positive</b>. Add the carry to the LSB (<b>end-around carry</b>):" + work2)
        st_gu.append("Carry ઉત્પન્ન થાય છે, તેથી જવાબ <b>positive</b> છે. Carry ને LSB માં ઉમેરો (<b>end-around carry</b>):" + work2)
        result = final
    else:
        final = ones(s)
        st_en.append("Add A and the 1's complement of B:" + work)
        st_gu.append("A અને B ના 1's complement નો સરવાળો કરો:" + work)
        st_en.append(f"No carry, so the result is <b>negative</b> and is in 1's complement form. Take the 1's complement of {s}: <b>−{final}</b>.")
        st_gu.append(f"Carry નથી, તેથી જવાબ <b>negative</b> છે અને 1's complement સ્વરૂપમાં છે. {s} નો 1's complement લો: <b>−{final}</b>.")
        result = "-" + final
    v = int(result.lstrip("-"), 2) * (-1 if result.startswith("-") else 1)
    assert v == int(a, 2) - int(b, 2), (a, b, result)
    return result, st_en, st_gu


def sub_twos(a, b):
    n = max(len(a), len(b))
    a2, b2 = a.zfill(n), b.zfill(n)
    c2 = twos(b2)
    s, carry, _ = add_bits(a2, c2)
    st_en = [f"Make both numbers {n} bits: A = {a2}, B = {b2}.",
             f"2's complement of B = 1's complement + 1 = {ones(b2)} + 1 = <b>{c2}</b>."]
    st_gu = [f"બંને numbers ને {n} bits ના બનાવો: A = {a2}, B = {b2}.",
             f"B નો 2's complement = 1's complement + 1 = {ones(b2)} + 1 = <b>{c2}</b>."]
    work = col_html([("", " " + a2), ("+", " " + c2), ("", "-" * (n + 1)), ("", ("1" if carry else " ") + s)])
    st_en.append("Add A and the 2's complement of B:" + work)
    st_gu.append("A અને B ના 2's complement નો સરવાળો કરો:" + work)
    if carry:
        st_en.append(f"A carry is generated: <b>discard it</b>. The result is positive: <b>{s}</b>.")
        st_gu.append(f"Carry ઉત્પન્ન થાય છે: તેને <b>અવગણો (discard)</b>. જવાબ positive છે: <b>{s}</b>.")
        result = s
    else:
        t = twos(s)
        st_en.append(f"No carry, so the result is <b>negative</b> and is in 2's complement form. Take the 2's complement of {s}: <b>−{t}</b>.")
        st_gu.append(f"Carry નથી, તેથી જવાબ <b>negative</b> છે અને 2's complement સ્વરૂપમાં છે. {s} નો 2's complement લો: <b>−{t}</b>.")
        result = "-" + t
    v = int(result.lstrip("-"), 2) * (-1 if result.startswith("-") else 1)
    assert v == int(a, 2) - int(b, 2), (a, b, result)
    return result, st_en, st_gu


def steps_html(st):
    return "<ol>" + "".join(f"<li>{x}</li>" for x in st) + "</ol>"


if __name__ == "__main__":
    print(int_to_base(45, 2)[0], int_to_base(2748, 16)[0], int_to_base(125, 8)[0])
    print(frac_to_base(Fraction(5, 8), 2)[:2], frac_to_base(Fraction(3, 10), 2, 5)[:2])
    print(fmt(to_decimal("1101.101", 2)[0]), fmt(to_decimal("2AF", 16)[0]), fmt(to_decimal("157", 8)[0]))
    print(bin_group("11010110.1011", 3)[0], bin_group("11010110.1011", 4)[0])
    print(to_bin_from("3A7.C", 16)[0], to_bin_from("527", 8)[0], to_bin_from("6.4", 8)[0])
    print(ones("10110"), twos("10110"), twos("01000"))
    print(add_work("1011", "1101")[0])
    print(sub_ones("11010", "10011")[0], sub_ones("10011", "11010")[0])
    print(sub_twos("11010", "10011")[0], sub_twos("10011", "11010")[0])
