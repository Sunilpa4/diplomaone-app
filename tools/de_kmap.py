"""K-map tool for DE Unit 3: exact minimisation (prime implicants + exhaustive minimum cover) and SVG drawing.
Cubes are strings over '0', '1', '-' (one char per variable, MSB first)."""
from itertools import product, combinations
from flowchart_lib import text, P, INK
import de_gates as G

VARS = "ABCD"
GRAY = [0, 1, 3, 2]
COLORS = ["#C62828", "#1565C0", "#2E7D32", "#E07B00", "#6A1B9A", "#00838F", "#AD1457"]


def cube_mins(c):
    opts = [("0", "1") if ch == "-" else (ch,) for ch in c]
    return sorted(int("".join(p), 2) for p in product(*opts))


def cube_term(c, names=VARS):
    t = "".join((nm if ch == "1" else "!" + nm) for nm, ch in zip(names, c) if ch != "-")
    return t or "1"


def cube_sum(c, names=VARS):
    """POS: cube of zeros -> sum term (complemented literals)"""
    lits = [("!" + nm if ch == "1" else nm) for nm, ch in zip(names, c) if ch != "-"]
    return "(" + " + ".join(lits) + ")" if len(lits) > 1 else (lits[0] if lits else "0")


def literals(c):
    return sum(ch != "-" for ch in c)


def primes(n, ones, dc=()):
    allowed = set(ones) | set(dc)
    imps = [("".join(c)) for c in product("01-", repeat=n) if set(cube_mins("".join(c))) <= allowed]
    imps = [c for c in imps if set(cube_mins(c)) & set(ones)]
    ms = {c: set(cube_mins(c)) for c in imps}
    return [c for c in imps if not any(ms[c] < ms[d] for d in imps)]


def minimise(n, ones, dc=()):
    """minimum SOP: list of cubes (fewest terms, then fewest literals); deterministic"""
    ones = sorted(set(ones))
    if not ones:
        return []
    if len(ones) + len(dc) == 2 ** n:
        return ["-" * n]
    P_ = sorted(primes(n, ones, dc), key=lambda c: (-len(cube_mins(c)), cube_mins(c)))
    for k in range(1, len(P_) + 1):
        best = None
        for combo in combinations(P_, k):
            cov = set().union(*(cube_mins(c) for c in combo))
            if set(ones) <= cov:
                key = sum(literals(c) for c in combo)
                if best is None or key < best[0]:
                    best = (key, combo)
        if best:
            return list(best[1])


def essential(n, ones, dc=()):
    P_ = primes(n, ones, dc)
    ess = []
    for m in ones:
        cov = [c for c in P_ if m in cube_mins(c)]
        if len(cov) == 1 and cov[0] not in ess:
            ess.append(cov[0])
    return ess


def sop_str(cubes, names=VARS):
    return " + ".join(cube_term(c, names) for c in cubes) if cubes else "0"


def pos_str(cubes, names=VARS):
    return "".join(cube_sum(c, names) for c in cubes) if cubes else "1"


def check(n, ones, dc, cubes):
    for m in range(2 ** n):
        v = any(m in cube_mins(c) for c in cubes)
        if m in ones:
            assert v, (m, cubes)
        elif m not in dc:
            assert not v, (m, cubes)
    return True


def size_name(c):
    return {1: ("single", "single"), 2: ("pair", "pair"), 4: ("quad", "quad"), 8: ("octet", "octet"), 16: ("all", "all")}[len(cube_mins(c))]


# ---------------------------------------------------------------- layout
def layout(n):
    """returns (row_vals, col_vals, row_bits, col_bits) ; cell (r, c) -> minterm"""
    if n == 2:
        return [0, 1], [0, 1], 1, 1
    if n == 3:
        return [0, 1], GRAY, 1, 2
    return GRAY, GRAY, 2, 2


def cell_min(n, r, c):
    rv, cv, rb, cb = layout(n)
    return (rv[r] << cb) | cv[c]


def pos_of(n, m):
    rv, cv, rb, cb = layout(n)
    return rv.index(m >> cb), cv.index(m & ((1 << cb) - 1))


def runs(idx, L):
    s = sorted(set(idx))
    if len(s) == L:
        return [(0, L - 1, False, False)]
    if s == list(range(s[0], s[-1] + 1)):
        return [(s[0], s[-1], False, False)]
    # wrap-around: split at the edge
    lo = [i for i in s if i < L // 2]
    hi = [i for i in s if i >= L // 2]
    return [(min(hi), max(hi), False, True), (min(lo), max(lo), True, False)]


def html_map(n, ones, dc=(), names=VARS):
    rv, cv, rb, cb = layout(n)
    rn, cn = names[:rb], names[rb:n]
    fmt = lambda v, b: format(v, f"0{b}b")
    h = f"<table><tr><th>{rn}\\{cn}</th>" + "".join(f"<th>{fmt(v, cb)}</th>" for v in cv) + "</tr>"
    for r, rvv in enumerate(rv):
        h += f"<tr><th>{fmt(rvv, rb)}</th>"
        for c in range(len(cv)):
            m = cell_min(n, r, c)
            v = "<b>1</b>" if m in ones else ("X" if m in dc else "0")
            h += f"<td>{v} <sub>m{m}</sub></td>"
        h += "</tr>"
    return h + "</table>"


def kmap_svg(x, y, n, ones, dc=(), groups=(), cell=38, names=VARS, show_zero=True, numbers=True, zeros_mode=False):
    rv, cv, rb, cb = layout(n)
    R, C = len(rv), len(cv)
    rn, cn = names[:rb], names[rb:n]
    if not isinstance(names, str):
        sep = " " if any(len(v) > 1 for v in names[:n]) else ""
        rn, cn = sep.join(rn), sep.join(cn)
    b = ""
    fmt = lambda v, w: format(v, f"0{w}b")
    # header
    b += f'<path d="M{x - 38} {y - 34} L{x - 2} {y - 2}" stroke="#888" stroke-width="1"/>'
    b += text(x - 32, y - 8, rn, 10.5, weight="bold", color="#6A1B9A") + text(x - 10, y - 30, cn, 10.5, weight="bold", color="#6A1B9A")
    for c, v in enumerate(cv):
        b += text(x + c * cell + cell / 2, y - 14, fmt(v, cb), 10, mono=True, weight="bold", color=P)
    for r, v in enumerate(rv):
        b += text(x - 18, y + r * cell + cell / 2, fmt(v, rb), 10, mono=True, weight="bold", color=P)
    for r in range(R):
        for c in range(C):
            m = cell_min(n, r, c)
            on = (m not in ones) if zeros_mode else (m in ones)
            on = on and m not in dc
            fill = "#FFF8E1" if on else "#fff"
            b += f'<rect x="{x + c * cell}" y="{y + r * cell}" width="{cell}" height="{cell}" fill="{fill}" stroke="{P}" stroke-width="1.2"/>'
            if m in ones:
                s, col = "1", INK
            elif m in dc:
                s, col = "X", "#E07B00"
            else:
                s, col = ("0", INK if zeros_mode else "#BBB")
            if s != "0" or show_zero:
                b += text(x + c * cell + cell / 2, y + r * cell + cell / 2 + 2, s, 13, mono=True, weight="bold", color=col)
            if numbers:
                b += text(x + c * cell + 4, y + r * cell + 8, str(m), 7.4, anchor="start", color="#999")
    for gi, g in enumerate(groups):
        col = COLORS[gi % len(COLORS)]
        cells = [pos_of(n, m) for m in cube_mins(g)]
        ins = 3 + (gi % 3) * 3
        for r0, r1, ro_lo, ro_hi in runs([p[0] for p in cells], R):
            for c0, c1, co_lo, co_hi in runs([p[1] for p in cells], C):
                x0 = x + c0 * cell + ins - (8 if co_lo else 0)
                x1 = x + (c1 + 1) * cell - ins + (8 if co_hi else 0)
                y0 = y + r0 * cell + ins - (8 if ro_lo else 0)
                y1 = y + (r1 + 1) * cell - ins + (8 if ro_hi else 0)
                b += (f'<rect x="{x0:.1f}" y="{y0:.1f}" width="{x1 - x0:.1f}" height="{y1 - y0:.1f}" rx="10" '
                      f'fill="none" stroke="{col}" stroke-width="2.2"/>')
    return b, (x + C * cell, y + R * cell)


def legend(x, y, groups, names=VARS, pos=False, size=10.5, step=20):
    b = ""
    for gi, g in enumerate(groups):
        col = COLORS[gi % len(COLORS)]
        b += f'<rect x="{x}" y="{y + gi * step - 6}" width="14" height="10" rx="3" fill="none" stroke="{col}" stroke-width="2"/>'
        t = cube_sum(g, names) if pos else cube_term(g, names)
        b += G.bexpr(x + 22, y + gi * step + 3, t, size, anchor="start", color=col)
    return b


if __name__ == "__main__":
    r = minimise(3, [1, 3, 5, 6, 7]); check(3, [1, 3, 5, 6, 7], (), r); print(sop_str(r))
    r = minimise(4, [0, 2, 8, 10]); print(sop_str(r))           # corners -> !B!D
    r = minimise(4, [1, 3, 7, 11, 15], [0, 2, 5]); print(sop_str(r))
    r = minimise(4, [0, 1, 2, 4, 5, 6, 8, 9, 12, 13, 14]); check(4, [0, 1, 2, 4, 5, 6, 8, 9, 12, 13, 14], (), r); print(sop_str(r))
    print(runs([0, 3], 4), essential(3, [1, 3, 5, 6, 7]))


# ---------------------------------------------------------------- SOP circuit (bus style)
def sop_circuit(cubes, n, x0=26, y0=40, names=VARS, out="Y", term_gap=50, width=360):
    """AND-OR implementation of an SOP. Returns (svg, height)."""
    from de_gates import gate, wire, dot, lab, bexpr
    terms = [c for c in cubes]
    need_not = [i for i in range(n) if any(c[i] == "0" for c in terms)]
    bx = {i: x0 + i * 14 for i in range(n)}                      # true buses
    nx0 = x0 + n * 14 + 8                                       # NOT gates start
    cbx = {i: nx0 + 38 + k * 14 for k, i in enumerate(need_not)}  # complement buses
    last_bus = max(list(bx.values()) + list(cbx.values()))
    and_x = last_bus + 22
    b = ""
    for i in range(n):
        b += lab(bx[i], y0 - 4, names[i], "middle", size=10.5)
    ynot = {}
    for k, i in enumerate(need_not):
        yy = y0 + 12 + k * 24
        ynot[i] = yy
        g, (ox, _), _ = gate("NOT", nx0, yy, s=0.62)
        b += g + dot(bx[i], yy) + wire([(bx[i], yy), (nx0, yy)]) + wire([(ox, yy), (cbx[i], yy)])
        b += bexpr(cbx[i], yy - 8 if False else y0 - 4, "!" + names[i], 10, color="#555")
    top_terms = y0 + 14 + len(need_not) * 24 + 16
    ys = [top_terms + 22 + t * term_gap for t in range(len(terms))]
    bottom = ys[-1] + 28
    for i in range(n):
        b += wire([(bx[i], y0 + 2), (bx[i], bottom)])
    for i in need_not:
        b += wire([(cbx[i], ynot[i]), (cbx[i], bottom)])
    mid = (ys[0] + ys[-1]) / 2
    or_x = and_x + 45 + 10 + 7 * ((len(terms) - 1) // 2) + 12
    if len(terms) == 1:
        or_x = and_x + 45 + 20
    og, (ox, oy), oins = gate("OR", or_x, mid, n=max(2, len(terms))) if len(terms) > 1 else ("", (and_x + 45, ys[0]), [(and_x + 45, ys[0])])
    b += og
    k_mid = (len(terms) - 1) / 2
    for t, c in enumerate(terms):
        lits = [i for i in range(n) if c[i] != "-"]
        y = ys[t]
        if len(lits) == 1:
            i = lits[0]
            src = bx[i] if c[i] == "1" else cbx[i]
            b += dot(src, y) + wire([(src, y), (and_x + 45, y)])
            ex = and_x + 45
        else:
            g, (ex, _), ins = gate("AND", and_x, y, n=len(lits))
            b += g
            for (ix, iy), i in zip(ins, lits):
                src = bx[i] if c[i] == "1" else cbx[i]
                b += dot(src, iy) + wire([(src, iy), (ix, iy)])
        b += bexpr(ex + 2, y - 8, cube_term(c, names), 9, anchor="start", color=COLORS[t % len(COLORS)])
        if len(terms) > 1:
            xr = ex + 8 + 7 * abs(t - k_mid)
            ix, iy = oins[t]
            b += wire([(ex, y), (xr, y), (xr, iy), (ix, iy)])
    b += wire([(ox, oy), (ox + 14, oy)]) + lab(ox + 18, oy + 4, out, "start")
    return b, bottom + 8


def all_minimal(n, ones, dc=()):
    """every minimum-cost SOP (same term count and literal count as minimise)"""
    best = minimise(n, ones, dc)
    if not best or best == ["-" * n]:
        return [best]
    k, lit = len(best), sum(literals(c) for c in best)
    P_ = primes(n, ones, dc)
    out = []
    for combo in combinations(P_, k):
        if set(ones) <= set().union(*(cube_mins(c) for c in combo)) and sum(literals(c) for c in combo) == lit:
            out.append(list(combo))
    return out
