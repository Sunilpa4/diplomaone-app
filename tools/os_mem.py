"""Memory-management simulators for DI03000041 Unit 3: first/best/worst fit (fixed and dynamic partitions), paging and
segmentation address translation, FIFO / LRU / optimal page replacement, and HTML renderers."""


# ------------------------------------------------------------------ fit
def _choose(sizes, need, method, free):
    cand = [i for i in range(len(sizes)) if free[i] and sizes[i] >= need]
    if not cand:
        return None
    if method == "first":
        return cand[0]
    if method == "best":
        return min(cand, key=lambda i: (sizes[i], i))
    return max(cand, key=lambda i: (sizes[i], -i))


def fit_fixed(jobs, parts, method):
    """Fixed partitions: one job per partition; leftover space is internal fragmentation.
    Returns list of (job_index, part_index or None)."""
    free = [True] * len(parts)
    out = []
    for j, need in enumerate(jobs):
        i = _choose(parts, need, method, free)
        if i is not None:
            free[i] = False
        out.append((j, i))
    return out


def fit_dynamic(jobs, holes, method):
    """Dynamic (variable) partitions: a job takes part of a hole; the rest stays a smaller hole.
    Returns list of (job_index, hole_index or None, hole_size_before, hole_size_after) and final holes."""
    h = list(holes)
    out = []
    for j, need in enumerate(jobs):
        i = _choose(h, need, method, [True] * len(h))
        if i is None:
            out.append((j, None, None, None))
        else:
            before = h[i]
            h[i] -= need
            out.append((j, i, before, h[i]))
    return out, h


# ------------------------------------------------------------------ page replacement
def replace(refs, nframes, algo):
    """Returns steps [(ref, frames_after (list, slot order), fault(bool), victim or None)], faults."""
    frames = []
    last_used, loaded = {}, {}
    steps, faults = [], 0
    for t, r in enumerate(refs):
        victim = None
        if r in frames:
            fault = False
        else:
            fault = True
            faults += 1
            if len(frames) < nframes:
                frames.append(r)
            else:
                if algo == "fifo":
                    victim = min(frames, key=lambda p: loaded[p])
                elif algo == "lru":
                    victim = min(frames, key=lambda p: last_used[p])
                else:   # optimal
                    def nxt(p):
                        for k in range(t + 1, len(refs)):
                            if refs[k] == p:
                                return k
                        return 10 ** 9
                    victim = max(frames, key=lambda p: (nxt(p), -frames.index(p)))
                frames[frames.index(victim)] = r
            loaded[r] = t
        last_used[r] = t
        steps.append((r, list(frames), fault, victim))
    return steps, faults


def replace_html(steps, nframes, gu=False):
    hd = ["Ref"] + [f"F{i + 1}" for i in range(nframes)] + (["Fault / Hit", "Victim"] if not gu else ["Fault / Hit", "Victim"])
    h = "<table><tr>" + "".join(f"<th>{x}</th>" for x in hd) + "</tr>"
    for r, fr, fault, victim in steps:
        cells = [f"<b>{r}</b>"] + [(f"<b>{p}</b>" if (p == r and fault) else str(p)) if k < len(fr) else "–" for k, p in
                                   enumerate(fr + [None] * (nframes - len(fr)))]
        h += "<tr>" + "".join(f"<td>{c}</td>" for c in cells) + f"<td>{'F' if fault else 'H'}</td><td>{victim if victim is not None else ''}</td></tr>"
    return h + "</table>"


# ------------------------------------------------------------------ paging / segmentation
def page_translate(la, psize, table):
    p, d = divmod(la, psize)
    f = table[p]
    return p, d, f, f * psize + d


def seg_translate(s, d, segtab):
    base, limit = segtab[s]
    return (base + d) if d < limit else None


if __name__ == "__main__":
    J, Pp = [20, 200, 500, 50, 150], [50, 300, 75, 700, 100]
    for m in ("first", "best", "worst"):
        print(m, fit_fixed(J, Pp, m), fit_dynamic(J, Pp, m))
    R = [1, 2, 3, 4, 5, 1, 3, 1, 6, 3, 2, 3]
    for a in ("fifo", "lru", "opt"):
        print(a, replace(R, 4, a)[1])
    C = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2, 1, 2, 0, 1, 7, 0, 1]
    print([replace(C, 3, a)[1] for a in ("fifo", "lru", "opt")])
    B = [1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5]
    print(replace(B, 3, "fifo")[1], replace(B, 4, "fifo")[1])
    print(fit_dynamic([212, 417, 112, 426], [100, 500, 200, 300, 600], "first"))
