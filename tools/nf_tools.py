"""Normalization helpers used to VERIFY the worked examples of RDBMS Unit 3.
FDs are given as strings like "A,B->C" or lists of (lhs_set, rhs_set)."""
from itertools import combinations


def parse(fds):
    out = []
    for f in fds:
        l, r = f.split("->")
        out.append((frozenset(x.strip() for x in l.split(",")), frozenset(x.strip() for x in r.split(","))))
    return out


def closure(attrs, fds):
    c = set(attrs)
    changed = True
    while changed:
        changed = False
        for l, r in fds:
            if l <= c and not r <= c:
                c |= r
                changed = True
    return c


def closure_steps(attrs, fds):
    """Returns the list of (fd_used, closure_after) steps, for writing the solution."""
    c, steps = set(attrs), []
    changed = True
    while changed:
        changed = False
        for l, r in fds:
            if l <= c and not r <= c:
                c |= r
                steps.append((l, r, set(c)))
                changed = True
    return steps


def candidate_keys(R, fds):
    R = set(R)
    keys = []
    for n in range(1, len(R) + 1):
        for combo in combinations(sorted(R), n):
            s = set(combo)
            if any(k <= s for k in keys):
                continue
            if closure(s, fds) == R:
                keys.append(s)
    return keys


def prime(R, fds):
    return set().union(*candidate_keys(R, fds))


def partial_deps(R, fds):
    """FDs X->A where X is a proper subset of some candidate key and A is non-prime."""
    keys, pr, out = candidate_keys(R, fds), prime(R, fds), []
    for k in keys:
        for n in range(1, len(k)):
            for sub in combinations(sorted(k), n):
                dep = closure(set(sub), fds) - set(sub) - pr
                if dep:
                    out.append((set(sub), dep))
    return out


def is_2nf(R, fds):
    return not partial_deps(R, fds)


def is_3nf(R, fds):
    keys, pr = candidate_keys(R, fds), prime(R, fds)
    for l, r in fds:
        for a in r - l:
            if closure(l, fds) >= set(R):   # l is a superkey
                continue
            if a in pr:
                continue
            return False
    return True


def is_bcnf(R, fds):
    return all(closure(l, fds) >= set(R) for l, r in fds if not r <= l)


def highest_nf(R, fds):
    if not is_2nf(R, fds):
        return "1NF"
    if not is_3nf(R, fds):
        return "2NF"
    if not is_bcnf(R, fds):
        return "3NF"
    return "BCNF"


def project(fds, attrs):
    """FDs that hold inside a sub-relation (simple projection using closures)."""
    attrs = set(attrs)
    out = []
    for n in range(1, len(attrs)):
        for combo in combinations(sorted(attrs), n):
            c = closure(set(combo), fds) & attrs
            rhs = c - set(combo)
            if rhs and not any(set(l) < set(combo) and rhs <= (closure(set(l), fds) & attrs) for l, _ in out):
                out.append((frozenset(combo), frozenset(rhs)))
    return out


def fmt(s):
    return ", ".join(sorted(s))


if __name__ == "__main__":
    F = parse(["A->B,C", "C,D->E", "B->D", "E->A"])
    print([fmt(k) for k in candidate_keys("ABCDE", F)])
    F2 = parse(["A,B->C", "C->D"])
    print(highest_nf("ABCD", F2), partial_deps("ABCD", F2))
    F3 = parse(["A->B", "A,C->D", "D->E"])
    print(highest_nf("ABCDE", F3), [fmt(k) for k in candidate_keys("ABCDE", F3)], partial_deps("ABCDE", F3))
