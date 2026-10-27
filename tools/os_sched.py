"""CPU scheduling simulators (FCFS, SJF, SRTF, RR, non-preemptive priority), Banker's algorithm, deadlock detection,
and renderers (Gantt HTML table, Gantt SVG, result tables) for DI03000041 Unit 2."""
from fractions import Fraction
from collections import deque


# ------------------------------------------------------------------ simulators
# procs: list of dicts {n: name, at: arrival, bt: burst, pr: priority (optional; smaller = higher)}
# returns segs [(name or None for idle, start, end)], and per-process dict {ct, tat, wt, rt}

def _merge(segs):
    out = []
    for s in segs:
        if out and out[-1][0] == s[0] and out[-1][2] == s[1]:
            out[-1] = (s[0], out[-1][1], s[2])
        else:
            out.append(s)
    return out


def _finish(procs, segs):
    res = {}
    for p in procs:
        mine = [s for s in segs if s[0] == p["n"]]
        ct = max(s[2] for s in mine)
        st = min(s[1] for s in mine)
        assert sum(s[2] - s[1] for s in mine) == p["bt"]
        res[p["n"]] = {"ct": ct, "tat": ct - p["at"], "wt": ct - p["at"] - p["bt"], "rt": st - p["at"]}
    return res


def nonpreemptive(procs, key):
    t, done, segs = 0, set(), []
    order = {p["n"]: i for i, p in enumerate(procs)}
    while len(done) < len(procs):
        ready = [p for p in procs if p["n"] not in done and p["at"] <= t]
        if not ready:
            nt = min(p["at"] for p in procs if p["n"] not in done)
            segs.append((None, t, nt)); t = nt
            continue
        p = min(ready, key=lambda q: (key(q), q["at"], order[q["n"]]))
        segs.append((p["n"], t, t + p["bt"])); t += p["bt"]; done.add(p["n"])
    return segs, _finish(procs, segs)


def fcfs(procs):
    return nonpreemptive(procs, lambda p: p["at"])


def sjf(procs):
    return nonpreemptive(procs, lambda p: p["bt"])


def priority(procs):
    return nonpreemptive(procs, lambda p: p["pr"])


def srtf(procs):
    rem = {p["n"]: p["bt"] for p in procs}
    order = {p["n"]: i for i, p in enumerate(procs)}
    t, segs = 0, []
    while any(rem.values()):
        ready = [p for p in procs if rem[p["n"]] and p["at"] <= t]
        if not ready:
            nt = min(p["at"] for p in procs if rem[p["n"]])
            segs.append((None, t, nt)); t = nt
            continue
        p = min(ready, key=lambda q: (rem[q["n"]], q["at"], order[q["n"]]))
        segs.append((p["n"], t, t + 1)); rem[p["n"]] -= 1; t += 1
    segs = _merge(segs)
    return segs, _finish(procs, segs)


def rr(procs, q, trace=None):
    """Round Robin. Convention: processes arriving during/at the end of a slice join the queue BEFORE the pre-empted process."""
    ps = sorted(procs, key=lambda p: p["at"])
    rem = {p["n"]: p["bt"] for p in ps}
    t, i, Q, segs = 0, 0, deque(), []
    while i < len(ps) or Q:
        while i < len(ps) and ps[i]["at"] <= t:
            Q.append(ps[i]["n"]); i += 1
        if not Q:
            segs.append((None, t, ps[i]["at"])); t = ps[i]["at"]
            continue
        n = Q.popleft()
        run = min(q, rem[n])
        segs.append((n, t, t + run)); t += run; rem[n] -= run
        while i < len(ps) and ps[i]["at"] <= t:
            Q.append(ps[i]["n"]); i += 1
        if rem[n]:
            Q.append(n)
        if trace is not None:
            trace.append((segs[-1][1], segs[-1][2], n, rem[n], list(Q)))
    segs = _merge(segs)
    return segs, _finish(procs, segs)


def P(names, at, bt, pr=None):
    return [dict(n=n, at=a, bt=b, **({"pr": pr[i]} if pr else {})) for i, (n, a, b) in enumerate(zip(names, at, bt))]


def avg(res, k):
    return Fraction(sum(r[k] for r in res.values()), len(res))


def fmt(fr):
    fr = Fraction(fr)
    if fr.denominator == 1:
        return str(fr.numerator)
    v = float(fr)
    s = f"{v:.2f}".rstrip("0").rstrip(".")
    return s if abs(float(s) - v) < 1e-12 else f"{v:.2f}"


# ------------------------------------------------------------------ HTML renderers
def gantt_html(segs, per=7):
    out = ""
    for k in range(0, len(segs), per):
        part = segs[k:k + per]
        r1 = "".join(f"<td><b>{n or 'idle'}</b></td>" for n, a, b in part)
        r2 = "".join(f"<td>{a}–{b}</td>" for n, a, b in part)
        out += f"<table><tr>{r1}</tr><tr>{r2}</tr></table>"
    return out


def result_table(procs, res, cols=("at", "bt", "ct", "tat", "wt"), gu=False, pr=False):
    head = {"n": "Process", "at": "AT", "bt": "BT", "pr": "Priority", "ct": "CT", "tat": "TAT = CT − AT", "wt": "WT = TAT − BT", "rt": "RT"}
    cs = ["n"] + (["at", "bt", "pr"] if pr else ["at", "bt"]) + [c for c in cols if c not in ("at", "bt")]
    h = "<table><tr>" + "".join(f"<th>{head[c]}</th>" for c in cs) + "</tr>"
    for p in procs:
        r = res[p["n"]]
        vals = {"n": p["n"], "at": p["at"], "bt": p["bt"], "pr": p.get("pr"), **r}
        vals["tat"] = f"{r['ct']} − {p['at']} = {r['tat']}"
        vals["wt"] = f"{r['tat']} − {p['bt']} = {r['wt']}"
        h += "<tr>" + "".join(f"<td>{vals[c]}</td>" for c in cs) + "</tr>"
    return h + "</table>"


def input_table(procs, pr=False):
    h = "<table><tr><th>Process</th><th>Arrival time</th><th>Burst time</th>" + ("<th>Priority</th>" if pr else "") + "</tr>"
    for p in procs:
        h += f"<tr><td>{p['n']}</td><td>{p['at']}</td><td>{p['bt']}</td>" + (f"<td>{p['pr']}</td>" if pr else "") + "</tr>"
    return h + "</table>"


def averages_html(res, gu=False):
    n = len(res)
    tat = " + ".join(str(r["tat"]) for r in res.values())
    wt = " + ".join(str(r["wt"]) for r in res.values())
    a, w = avg(res, "tat"), avg(res, "wt")
    lab = ("સરેરાશ TAT", "સરેરાશ WT") if gu else ("Average TAT", "Average WT")
    return (f"<p><b>{lab[0]}</b> = ({tat}) / {n} = {sum(r['tat'] for r in res.values())}/{n} = <b>{fmt(a)}</b> units</p>"
            f"<p><b>{lab[1]}</b> = ({wt}) / {n} = {sum(r['wt'] for r in res.values())}/{n} = <b>{fmt(w)}</b> units</p>")


def solve_html(procs, segs, res, steps_en, steps_gu, pr=False):
    en = (f"<p><b>Gantt chart:</b></p>{gantt_html(segs)}{steps_en}" + result_table(procs, res, pr=pr) + averages_html(res))
    gu = (f"<p><b>Gantt chart:</b></p>{gantt_html(segs)}{steps_gu}" + result_table(procs, res, pr=pr) + averages_html(res, True))
    return en, gu


# ------------------------------------------------------------------ SVG gantt
def gantt_svg_body(segs, x0, y, width, h=30, colors=None, size=10):
    from flowchart_lib import text, line
    T = segs[-1][2]
    T0 = segs[0][1]
    sc = width / (T - T0)
    pal = colors or {}
    b = ""
    for n, a, e in segs:
        x, w = x0 + (a - T0) * sc, (e - a) * sc
        f, s = pal.get(n, ("#F2F2F2", "#999")) if n else ("#FFFFFF", "#BBB")
        b += f'<rect x="{x:.1f}" y="{y}" width="{w:.1f}" height="{h}" fill="{f}" stroke="{s}" stroke-width="1.3"/>'
        b += text(x + w / 2, y + h / 2, n or "idle", size if n else 8, color=s, weight="bold")
    ticks = sorted({a for _, a, _ in segs} | {T})
    prev, low = -99, False
    for t in ticks:
        x = x0 + (t - T0) * sc
        low = (not low) if x - prev < 15 else False
        b += text(x, y + h + 10 + (9 if low else 0), str(t), 8.8, color="#444")
        prev = x
    return b


# ------------------------------------------------------------------ Banker's algorithm and detection
def bankers(alloc, maxm, avail, names=None):
    n, m = len(alloc), len(avail)
    names = names or [f"P{i}" for i in range(n)]
    need = [[maxm[i][j] - alloc[i][j] for j in range(m)] for i in range(n)]
    work, fin, seq, steps = list(avail), [False] * n, [], []
    progress = True
    while progress:
        progress = False
        for i in range(n):
            if not fin[i] and all(need[i][j] <= work[j] for j in range(m)):
                old = list(work)
                work = [work[j] + alloc[i][j] for j in range(m)]
                fin[i] = True; seq.append(names[i]); steps.append((names[i], need[i], old, list(work)))
                progress = True
    return need, seq, all(fin), steps


def detect(alloc, request, avail, names=None):
    n, m = len(alloc), len(avail)
    names = names or [f"P{i}" for i in range(n)]
    work = list(avail)
    fin = [all(a == 0 for a in alloc[i]) for i in range(n)]
    seq, steps, progress = [], [], True
    while progress:
        progress = False
        for i in range(n):
            if not fin[i] and all(request[i][j] <= work[j] for j in range(m)):
                old = list(work)
                work = [work[j] + alloc[i][j] for j in range(m)]
                fin[i] = True; seq.append(names[i]); steps.append((names[i], request[i], old, list(work)))
                progress = True
    return seq, [names[i] for i in range(n) if not fin[i]], steps


def vec(v):
    return "(" + ", ".join(map(str, v)) + ")"


if __name__ == "__main__":
    a = P(["P0", "P1", "P2", "P3"], [0, 1, 2, 3], [5, 3, 8, 6])
    for f in (fcfs, sjf, srtf):
        s, r = f(a); print(f.__name__, s, fmt(avg(r, "tat")), fmt(avg(r, "wt")))
    s, r = rr(a, 2); print("rr2", s, fmt(avg(r, "tat")), fmt(avg(r, "wt")))
    b = P(["P0", "P1", "P2", "P3"], [3, 0, 4, 5], [5, 4, 2, 4])
    for f in (fcfs, sjf):
        s, r = f(b); print(f.__name__, s, fmt(avg(r, "tat")), fmt(avg(r, "wt")))
    s, r = rr(b, 2); print("rr2", s, fmt(avg(r, "tat")), fmt(avg(r, "wt")))
    c = P(["P1", "P2", "P3", "P4"], [0, 1, 2, 3], [8, 4, 9, 5]); s, r = srtf(c); print("srtf", s, fmt(avg(r, "wt")))
    d = P(["P1", "P2", "P3"], [0, 0, 0], [24, 3, 3]); s, r = rr(d, 4); print("rr4", s, fmt(avg(r, "wt")))
    e = P(["P1", "P2", "P3", "P4", "P5"], [0] * 5, [10, 1, 2, 1, 5], [3, 1, 4, 5, 2]); s, r = priority(e); print("pri", s, fmt(avg(r, "wt")))
    print(bankers([[0, 1, 0], [2, 0, 0], [3, 0, 2], [2, 1, 1], [0, 0, 2]], [[7, 5, 3], [3, 2, 2], [9, 0, 2], [2, 2, 2], [4, 3, 3]], [3, 3, 2])[1:3])
