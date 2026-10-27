"""Disk-scheduling simulators for OS Unit 4 (FCFS, SSTF, SCAN, C-SCAN, LOOK, C-LOOK).
Each returns (path, total) where path is the list of head positions starting with the initial head."""


def _total(path):
    return sum(abs(b - a) for a, b in zip(path, path[1:]))


def fcfs(q, head):
    p = [head] + list(q)
    return p, _total(p)


def sstf(q, head):
    left, p, h = list(q), [head], head
    while left:
        n = min(left, key=lambda r: (abs(r - h), r))
        left.remove(n); p.append(n); h = n
    return p, _total(p)


def scan(q, head, direction="left", size=200):
    lo = sorted(r for r in q if r < head)
    hi = sorted(r for r in q if r >= head)
    if direction == "left":
        p = [head] + lo[::-1] + ([0] if hi else []) + hi
    else:
        p = [head] + hi + ([size - 1] if lo else []) + lo[::-1]
    return p, _total(p)


def cscan(q, head, direction="left", size=200, count_return=True):
    """C-SCAN: service in one direction, jump back to the other end. Returns (path, total, total_without_return)."""
    lo = sorted(r for r in q if r < head)
    hi = sorted(r for r in q if r >= head)
    if direction == "left":
        p = [head] + lo[::-1] + [0, size - 1] + hi[::-1]
    else:
        p = [head] + hi + [size - 1, 0] + lo
    tot = _total(p)
    return p, tot, tot - (size - 1)


def look(q, head, direction="left"):
    lo = sorted(r for r in q if r < head)
    hi = sorted(r for r in q if r >= head)
    p = [head] + (lo[::-1] + hi if direction == "left" else hi + lo[::-1])
    return p, _total(p)


def clook(q, head, direction="left"):
    lo = sorted(r for r in q if r < head)
    hi = sorted(r for r in q if r >= head)
    p = [head] + (lo[::-1] + hi[::-1] if direction == "left" else hi + lo)
    return p, _total(p)


def moves(path):
    """List of (from, to, |diff|) segments."""
    return [(a, b, abs(b - a)) for a, b in zip(path, path[1:])]


P5_Q, P5_H = [75, 90, 40, 135, 50, 170, 65, 10], 46
SIL_Q, SIL_H = [98, 183, 37, 122, 14, 124, 65, 67], 53

if __name__ == "__main__":
    print("P5 FCFS", fcfs(P5_Q, P5_H))
    print("P5 SSTF", sstf(P5_Q, P5_H))
    print("P5 SCAN L", scan(P5_Q, P5_H))
    print("P5 CSCAN L", cscan(P5_Q, P5_H))
    print("P5 SCAN R", scan(P5_Q, P5_H, "right"))
    print("P5 CSCAN R", cscan(P5_Q, P5_H, "right"))
    print("P5 LOOK L", look(P5_Q, P5_H), "CLOOK L", clook(P5_Q, P5_H))
    print("SIL FCFS", fcfs(SIL_Q, SIL_H)[1], "SSTF", sstf(SIL_Q, SIL_H)[1],
          "SCAN L", scan(SIL_Q, SIL_H)[1], "CSCAN R", cscan(SIL_Q, SIL_H, "right")[1:],
          "LOOK R", look(SIL_Q, SIL_H, "right")[1], "CLOOK R", clook(SIL_Q, SIL_H, "right")[1])
