"""Sorting / searching / hashing tracer for DS Unit 5. Every trace table, diagram and numerical comes from here.
Conventions (same as the C programs):
  bubble    : pass i compares a[j], a[j+1] for j < n-1-i, swaps if a[j] > a[j+1]; stops early if no swap
  selection : pass i finds min in a[i..n-1] and swaps it with a[i]
  insertion : pass i inserts a[i] into sorted a[0..i-1] by shifting
  quick     : pivot = first element; i moves right while a[i] <= pivot, j moves left while a[j] > pivot;
              swap a[i], a[j] if i < j; finally swap pivot with a[j]
  merge     : top-down, mid = (l + r) / 2
  radix     : LSD, base 10, buckets 0-9
"""


def table(head, rows):
    """raw HTML table (cells may contain <b> and entities like &gt;)"""
    h = "<table><tr>" + "".join(f"<th>{x}</th>" for x in head) + "</tr>"
    for r in rows:
        h += "<tr>" + "".join(f"<td>{x if x != '' else '–'}</td>" for x in r) + "</tr>"
    return h + "</table>"


def J(a):
    return " ".join(map(str, a))


def hl(a, idx, cls="b"):
    """array as string with chosen indices in bold"""
    return " ".join(f"<b>{v}</b>" if i in idx else str(v) for i, v in enumerate(a))


# ---------------------------------------------------------------- bubble
def bubble(a):
    a, rows, n = list(a), [], len(a)
    total_c = total_s = 0
    for i in range(n - 1):
        sw = c = 0
        for j in range(n - 1 - i):
            c += 1
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                sw += 1
        total_c += c; total_s += sw
        rows.append((i + 1, hl(a, {n - 1 - i}), c, sw))
        if sw == 0:
            break
    return a, rows, total_c, total_s


def bubble_table(a):
    s, rows, c, w = bubble(a)
    return s, table(["Pass", "Array after pass (bold = fixed)", "Comparisons", "Swaps"], rows), c, w


def bubble_pass1(a):
    """detailed comparisons of pass 1"""
    a, rows = list(a), []
    for j in range(len(a) - 1):
        x, y = a[j], a[j + 1]
        if x > y:
            a[j], a[j + 1] = y, x
        rows.append((f"a[{j}], a[{j + 1}]", f"{x} &gt; {y} ? {'yes, swap' if x > y else 'no'}", hl(a, {j, j + 1})))
    return table(["Compare", "Check", "Array"], rows)


# ---------------------------------------------------------------- selection
def selection(a):
    a, rows, n = list(a), [], len(a)
    for i in range(n - 1):
        m = i
        for j in range(i + 1, n):
            if a[j] < a[m]:
                m = j
        note = f"min {a[m]} at [{m}]; swap with a[{i}] = {a[i]}" if m != i else f"min {a[m]} already at [{i}]"
        a[i], a[m] = a[m], a[i]
        rows.append((i + 1, note, hl(a, set(range(i + 1)))))
    return a, rows


def selection_table(a):
    s, rows = selection(a)
    return s, table(["Pass", "Action", "Array (bold = sorted part)"], rows)


# ---------------------------------------------------------------- insertion
def insertion(a):
    a, rows = list(a), []
    for i in range(1, len(a)):
        key, j, shifts = a[i], i - 1, 0
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]; j -= 1; shifts += 1
        a[j + 1] = key
        rows.append((i, key, shifts, f"at [{j + 1}]", hl(a, set(range(i + 1)))))
    return a, rows


def insertion_table(a):
    s, rows = insertion(a)
    return s, table(["Pass", "Key", "Shifts", "Placed", "Array (bold = sorted part)"], rows)


# ---------------------------------------------------------------- quick
def quick(a):
    a, rows = list(a), []

    def part(lo, hi):
        p, i, j = a[lo], lo + 1, hi
        while True:
            while i <= hi and a[i] <= p:
                i += 1
            while a[j] > p:
                j -= 1
            if i < j:
                a[i], a[j] = a[j], a[i]
                rows.append((f"[{lo}..{hi}]", p, f"swap {a[j]} and {a[i]}", hl(a, {i, j})))
            else:
                break
        a[lo], a[j] = a[j], a[lo]
        rows.append((f"[{lo}..{hi}]", p, f"i&gt;j: swap pivot with a[{j}] → {p} fixed at [{j}]", hl(a, {j})))
        return j

    def qs(lo, hi):
        if lo < hi:
            k = part(lo, hi)
            qs(lo, k - 1); qs(k + 1, hi)
    qs(0, len(a) - 1)
    return a, rows


def quick_table(a):
    s, rows = quick(a)
    return s, table(["Sub-array", "Pivot", "Action", "Array"], rows)


def quick_first_partition(a):
    """detailed i/j movement of the first partition, for the diagram + notes"""
    a = list(a)
    lo, hi = 0, len(a) - 1
    p, i, j = a[lo], lo + 1, hi
    steps = []
    while True:
        while i <= hi and a[i] <= p:
            i += 1
        while a[j] > p:
            j -= 1
        if i < j:
            steps.append((list(a), i, j, f"a[{i}]={a[i]} &gt; {p}, a[{j}]={a[j]} ≤ {p}: swap"))
            a[i], a[j] = a[j], a[i]
        else:
            steps.append((list(a), i, j, f"i={i} &gt; j={j}: stop, swap pivot {p} with a[{j}]={a[j]}"))
            break
    a[lo], a[j] = a[j], a[lo]
    return steps, a, j


# ---------------------------------------------------------------- merge
def merge_sort(a):
    rows = []

    def ms(x, depth):
        if len(x) <= 1:
            return x
        m = (len(x) + 1) // 2           # (l+r)/2 with l=0 -> left part gets the middle element
        L, R = ms(x[:m], depth + 1), ms(x[m:], depth + 1)
        out, i, j = [], 0, 0
        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                out.append(L[i]); i += 1
            else:
                out.append(R[j]); j += 1
        out += L[i:] + R[j:]
        rows.append((depth, f"[{J(L)}] + [{J(R)}]", f"[{J(out)}]"))
        return out
    s = ms(list(a), 0)
    return s, rows


def merge_table(a):
    s, rows = merge_sort(a)
    return s, table(["Level", "Merge", "Result"], rows)


def merge_levels(a):
    """divide levels (for the diagram): list of lists of parts"""
    levels = [[list(a)]]
    while any(len(p) > 1 for p in levels[-1]):
        nxt = []
        for p in levels[-1]:
            if len(p) > 1:
                m = (len(p) + 1) // 2
                nxt += [p[:m], p[m:]]
            else:
                nxt.append(p)
        levels.append(nxt)
    return levels


# ---------------------------------------------------------------- radix
def radix(a):
    a, rows = list(a), []
    d = len(str(max(a)))
    for k in range(d):
        b = [[] for _ in range(10)]
        for v in a:
            b[(v // 10 ** k) % 10].append(v)
        a = [v for bk in b for v in bk]
        rows.append((k + 1, ["units", "tens", "hundreds", "thousands"][k], b, list(a)))
    return a, rows


def radix_table(a):
    s, rows = radix(a)
    out = ""
    for p, name, b, res in rows:
        out += f"<p><b>Pass {p} ({name} digit)</b></p>"
        out += table(["Bucket", "Numbers"], [(i, ", ".join(map(str, bk)) or "-") for i, bk in enumerate(b) if bk])
        out += f"<p>Collect: {J(res)}</p>"
    return s, out


# ---------------------------------------------------------------- searching
def linear(a, x):
    rows = []
    for i, v in enumerate(a):
        rows.append((i, v, "found" if v == x else "no"))
        if v == x:
            return i, rows
    return -1, rows


def binary(a, x):
    lo, hi, rows = 0, len(a) - 1, []
    while lo <= hi:
        mid = (lo + hi) // 2
        if a[mid] == x:
            rows.append((lo, hi, mid, a[mid], f"{a[mid]} = {x}: found")); return mid, rows
        if x < a[mid]:
            rows.append((lo, hi, mid, a[mid], f"{x} &lt; {a[mid]}: high = {mid - 1}")); hi = mid - 1
        else:
            rows.append((lo, hi, mid, a[mid], f"{x} &gt; {a[mid]}: low = {mid + 1}")); lo = mid + 1
    rows.append((lo, hi, "-", "-", "low &gt; high: not found"))
    return -1, rows


def binary_table(a, x):
    k, rows = binary(a, x)
    return k, table(["low", "high", "mid", "a[mid]", "Decision"], rows)


# ---------------------------------------------------------------- hashing
def h_division(k, m):
    return k % m


def h_midsquare(k, digits=2):
    """square, take the middle `digits` digits (for odd extra length the extra digit goes to the right side)"""
    s = str(k * k)
    start = (len(s) - digits) // 2
    return int(s[start:start + digits]), k * k, s[start:start + digits]


def h_folding(k, part=2, size=None):
    """fold shifting: split into parts of `part` digits from the left, add, keep last `part` digits"""
    s = str(k)
    parts = [int(s[i:i + part]) for i in range(0, len(s), part)]
    tot = sum(parts)
    keep = size or part
    return tot % (10 ** keep), parts, tot


if __name__ == "__main__":
    A = [45, 12, 78, 34, 23, 56]
    print(bubble(A)[0], bubble(A)[2:], selection(A)[0], insertion(A)[0])
    Q = [25, 57, 48, 37, 12, 92, 86, 33]
    s, r = quick(Q); print(s); [print(x) for x in r]
    print(merge_sort([38, 27, 43, 3, 9, 82, 10]))
    print(radix([170, 45, 75, 90, 802, 24, 2, 66])[0])
    B = [5, 12, 18, 23, 34, 45, 56, 67, 78, 89]
    print(binary(B, 23), binary(B, 60))
    print(h_division(1234, 10), h_midsquare(3205), h_folding(12345678))
