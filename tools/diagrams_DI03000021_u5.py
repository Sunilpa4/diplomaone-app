"""DI03000021 Data Structures - Unit 5 diagrams: sorting, searching, hashing (all states computed by ds_sort)."""
import os
from flowchart_lib import *
from diagrams_DI03000021_u1 import box, BLUE, BLUEF, GREEN, GREENF, ORANGE, ORANGEF, RED, REDF, YEL
import ds_sort as S

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "content", "computer", "sem3", "DI03000021", "diagrams")

A6 = [45, 12, 78, 34, 23, 56]
Q8 = [25, 57, 48, 37, 12, 92, 86, 33]
M7 = [38, 27, 43, 3, 9, 82, 10]
R8 = [170, 45, 75, 90, 802, 24, 2, 66]
B10 = [5, 12, 18, 23, 34, 45, 56, 67, 78, 89]
HK = [1234, 5678, 4321, 9087, 2468]


def row(x, y, vals, fills=None, w=36, h=26, size=11.5, idx=False):
    fills = fills or {}
    b = ""
    for i, v in enumerate(vals):
        b += box(x + i * w, y, w, h, fills.get(i, "#fff"), P, 0, 1.3)
        b += text(x + i * w + w / 2, y + h / 2, str(v), size, mono=True, weight="bold")
        if idx:
            b += text(x + i * w + w / 2, y - 7, str(i), 8.6, mono=True, color="#888")
    return b


def note(x, y, w, lines, fill=BLUEF, stroke=BLUE, size=9.6, lh=15):
    b = box(x, y, w, 10 + lh * len(lines), fill, stroke, 7, 1.1)
    for i, s in enumerate(lines):
        c = INK
        if isinstance(s, tuple):
            s, c = s
        b += text(x + 8, y + 15 + i * lh, s, size, anchor="start", color=c)
    return b


# ------------------------------------------------------------------ 1. bubble
def bubble():
    b = title("Bubble Sort (pass by pass)")
    a, n = list(A6), len(A6)
    x0 = 74
    b += text(64, 50, "Input", 10, anchor="end", weight="bold") + row(x0, 37, a)
    y = 37
    p = 0
    while True:
        sw = 0
        for j in range(n - 1 - p):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]; sw += 1
        y += 36
        fills = {k: GREENF for k in range(n - 1 - p, n)}
        b += text(64, y + 13, f"Pass {p + 1}", 10, anchor="end", weight="bold", color=P) + row(x0, y, a, fills)
        b += text(x0 + 6 * 36 + 8, y + 13, f"{sw} swaps", 9, anchor="start", color="#555")
        p += 1
        if sw == 0 or p == n - 1:
            break
    y += 40
    b += note(12, y, 336, ["Compare neighbours a[j] and a[j+1]; swap if out of order.", "After each pass the largest remaining value",
                           ("bubbles up to the end (green = fixed).", GREEN), "No swap in a pass → array sorted, stop early."], size=9.6)
    return svg(360, y + 78, b)


# ------------------------------------------------------------------ 2. selection
def selection():
    b = title("Selection Sort")
    a, n = list(A6), len(A6)
    x0 = 74
    b += text(64, 50, "Input", 10, anchor="end", weight="bold") + row(x0, 37, a)
    y = 37
    for i in range(n - 1):
        m = min(range(i, n), key=lambda k: a[k])
        pre = {k: GREENF for k in range(i)}
        pre[m] = YEL
        y += 36
        a[i], a[m] = a[m], a[i]
        fills = {k: GREENF for k in range(i + 1)}
        b += text(64, y + 13, f"Pass {i + 1}", 10, anchor="end", weight="bold", color=P) + row(x0, y, a, fills)
        b += text(x0 + 6 * 36 + 8, y + 13, f"min {a[i]}", 9, anchor="start", color="#555")
    y += 40
    b += note(12, y, 336, ["Pass i: find the minimum of the unsorted part", "a[i..n-1] and swap it with a[i].",
                           ("Green = sorted part grows from the left.", GREEN), "n-1 passes, at most one swap per pass."], size=9.6)
    return svg(360, y + 78, b)


# ------------------------------------------------------------------ 3. insertion
def insertion():
    b = title("Insertion Sort")
    a, n = list(A6), len(A6)
    x0 = 74
    b += text(64, 50, "Input", 10, anchor="end", weight="bold") + row(x0, 37, a, {0: GREENF})
    y = 37
    for i in range(1, n):
        key, j = a[i], i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]; j -= 1
        a[j + 1] = key
        fills = {k: GREENF for k in range(i + 1)}
        fills[j + 1] = YEL
        y += 36
        b += text(64, y + 13, f"key {key}", 10, anchor="end", weight="bold", color=P) + row(x0, y, a, fills)
    y += 40
    b += note(12, y, 336, ["Take the next element (key) and insert it into", "the sorted left part by shifting bigger values",
                           ("right (yellow = key placed, green = sorted).", ORANGE), "Like arranging playing cards in the hand."], size=9.6)
    return svg(360, y + 78, b)


# ------------------------------------------------------------------ 4. quick sort partition
def quick_partition():
    b = title("Quick Sort: Partition (pivot = first)")
    steps, final, j = S.quick_first_partition(Q8)
    x0, w = 36, 36
    y = 46
    for k, (a, i, jj, msg) in enumerate(steps):
        fills = {0: ORANGEF}
        if i < len(a):
            fills[i] = REDF
        fills[jj] = BLUEF
        b += row(x0, y, a, fills, w, idx=(k == 0))
        if i < len(a):
            b += text(x0 + i * w + w / 2, y + 38, "i", 10, weight="bold", color=RED)
        b += text(x0 + jj * w + w / 2, y + 38, "j", 10, weight="bold", color=BLUE)
        clean = msg.replace("&gt;", ">")
        b += text(180, y + 54, clean, 9.2, color="#444")
        y += 76
    fills = {j: GREENF}
    b += row(x0, y, final, fills, w)
    b += text(180, y + 42, f"pivot 25 is now at its final place [{j}]", 9.6, color=GREEN, weight="bold")
    b += text(180, y + 58, "left part ≤ 25 < right part; sort both parts again", 9.4, color="#444")
    b += note(12, y + 70, 336, ["i moves right while a[i] ≤ pivot", "j moves left while a[j] > pivot",
                                "if i < j: swap a[i], a[j]   else: swap pivot, a[j]"], size=9.6)
    return svg(360, y + 132, b)


# ------------------------------------------------------------------ 5. quick sort recursion
def quick_tree():
    b = title("Quick Sort: Whole Process")
    s, rows = S.quick(Q8)
    fixed = [r for r in rows if "fixed" in r[2]]
    y = 40
    for sub, piv, act, arr_ in fixed:
        b += text(16, y + 13, sub, 9.6, anchor="start", mono=True, color="#555")
        lo, hi = map(int, sub.strip("[]").split(".."))
        vals = arr_.replace("<b>", "").replace("</b>", "").split()
        pos = act.split("[")[-1].rstrip("]")
        fills = {k: "#F1E8FC" for k in range(lo, hi + 1)}
        fills[int(pos)] = GREENF
        b += row(76, y, vals, fills, 34, 26, 10.5)
        b += text(76 + 8 * 34 + 6, y + 13, f"p={piv}", 9, anchor="start", color=ORANGE, weight="bold")
        y += 36
    b += row(76, y + 6, s, {k: GREENF for k in range(8)}, 34, 26, 10.5)
    b += text(16, y + 19, "sorted", 9.6, anchor="start", weight="bold", color=GREEN)
    b += note(12, y + 46, 336, ["Lavender = sub-array being partitioned", ("Green = pivot placed at its final position", GREEN),
                                "Average O(n log n), worst O(n²) (sorted input)"], size=9.6)
    return svg(360, y + 106, b)


# ------------------------------------------------------------------ 6. merge sort
def merge():
    b = title("Merge Sort: Divide and Merge")
    lv = S.merge_levels(M7)
    y = 38
    W = 34

    def draw_level(parts, y, fill):
        nonlocal b
        total = sum(len(p) for p in parts) * 30 + (len(parts) - 1) * 12
        x = 180 - total / 2
        for p in parts:
            b += row(x, y, p, {k: fill for k in range(len(p))}, 30, 24, 10.5)
            x += len(p) * 30 + 12
    for k, parts in enumerate(lv):
        draw_level(parts, y, BLUEF if k else "#fff")
        y += 36
    b += text(352, 50, "divide", 9.4, anchor="end", color=BLUE, weight="bold")
    # merge levels: rebuild bottom-up
    s, rows = S.merge_sort(M7)
    y += 4
    b += line(f"M20 {y - 10} L340 {y - 10}", "#ccc", 1, "4 3")
    for d in range(len(lv) - 2, -1, -1):
        draw_level([sorted(p) for p in lv[d]], y, GREENF)
        y += 36
    assert sorted(M7) == s
    b += text(352, y - 22, "merge", 9.4, anchor="end", color=GREEN, weight="bold")
    b += note(12, y, 336, ["Divide the array into two halves until single", "elements remain, then merge sorted halves.",
                           "Always O(n log n); needs an extra array O(n)."], size=9.6)
    return svg(360, y + 62, b)


# ------------------------------------------------------------------ 7. radix
def radix():
    b = title("Radix Sort (LSD, base 10)")
    s, rows = S.radix(R8)
    b += text(14, 46, "Input:", 10, anchor="start", weight="bold") + text(70, 46, S.J(R8), 10.4, anchor="start", mono=True)
    y = 62
    for p, name, bk, res in rows:
        b += box(12, y, 336, 66, "#FCFAFF", "#D9C8F0", 8, 1)
        b += text(22, y + 15, f"Pass {p}: {name} digit", 10, anchor="start", weight="bold", color=P)
        txt = "   ".join(f"{i}:{','.join(map(str, v))}" for i, v in enumerate(bk) if v)
        b += text(22, y + 34, txt, 9, anchor="start", mono=True, color=BLUE)
        b += text(22, y + 54, "→ " + S.J(res), 10, anchor="start", mono=True, weight="bold")
        y += 74
    b += note(12, y, 336, ["Distribute numbers into buckets 0-9 by one digit,", "collect in order, repeat for the next digit.",
                           "Passes = digits in the largest number (802 → 3).", "No comparisons: O(d × n)."], size=9.6)
    return svg(360, y + 78, b)


# ------------------------------------------------------------------ 8. linear search
def linear():
    b = title("Linear (Sequential) Search")
    a = [34, 12, 78, 23, 56, 45, 9]
    k, rows = S.linear(a, 56)
    fills = {i: REDF for i in range(k)}
    fills[k] = GREENF
    b += text(180, 44, "Search key = 56", 10.6, weight="bold", color=BLUE)
    b += row(54, 70, a, fills, 36, 28, idx=True)
    for i in range(k + 1):
        b += text(54 + i * 36 + 18, 114, "✓" if i == k else "✗", 12, color=GREEN if i == k else RED, weight="bold")
    b += text(180, 140, f"Found at index {k} after {k + 1} comparisons", 10, color=GREEN, weight="bold")
    b += note(12, 156, 336, ["Compare the key with each element from the", "first to the last until it matches.",
                             "Works on unsorted data too.", "Best O(1), worst O(n), average about n/2."], size=9.6)
    return svg(360, 228, b)


# ------------------------------------------------------------------ 9. binary search
def binary():
    b = title("Binary Search (sorted array)")
    k, rows = S.binary(B10, 23)
    b += text(180, 40, "Search key = 23", 10.6, weight="bold", color=BLUE)
    y = 64
    for lo, hi, mid, v, dec in rows:
        fills = {i: "#F1E8FC" for i in range(lo, hi + 1)}
        fills[mid] = GREENF if v == 23 else YEL
        b += row(0 + 0, y, B10, fills, 34, 24, 10.2, idx=(y == 64)) if False else row(10, y, B10, fills, 34, 24, 10.2, idx=(y == 64))
        labs = {}
        for name, k in (("L", lo), ("M", mid), ("H", hi)):
            labs.setdefault(k, []).append(name)
        for k, names in labs.items():
            col = GREEN if "M" in names else (BLUE if names == ["L"] else RED)
            b += text(10 + k * 34 + 17, y + 36, "=".join(names) if len(names) > 1 else names[0], 9, color=col, weight="bold")
        b += text(180, y + 56, dec.replace("&lt;", "<").replace("&gt;", ">") + f"   (mid = {mid})", 9.4, color="#444")
        y += 72
    b += note(12, y, 336, ["mid = (low + high) / 2; compare key with a[mid].", "key smaller → search left half (high = mid-1)",
                           "key larger → search right half (low = mid+1)", "Data must be sorted. O(log n): 10 items ≤ 4 steps."], size=9.6)
    return svg(360, y + 78, b)


# ------------------------------------------------------------------ 10. hash table
def hash_table():
    b = title("Hashing: Key, Hash Function, Hash Table")
    keys = [1234, 5678, 4321, 9087, 2466]
    m = 10
    y0 = 52
    for i, k in enumerate(keys):
        y = y0 + i * 40
        b += box(14, y, 62, 26, BLUEF, BLUE, 6) + text(45, y + 13, str(k), 11, mono=True, weight="bold")
        b += arr([(78, y + 13), (112, y + 13)], "#888")
        b += box(114, y, 92, 26, ORANGEF, ORANGE, 6) + text(160, y + 13, f"{k} % 10 = {k % m}", 9.6, mono=True)
        b += arr([(208, y + 13), (262, 46 + (k % m) * 26 + 13 - 0)], "#888")
    b += text(45, 42, "key", 9.6, weight="bold", color=BLUE) + text(160, 42, "h(k) = k mod 10", 9.6, weight="bold", color=ORANGE)
    used = {k % m: k for k in keys}
    for i in range(10):
        y = 46 + i * 26
        b += box(264, y, 30, 26, "#F1E8FC", P, 0, 1.2) + text(279, y + 13, str(i), 10, mono=True, color="#666")
        b += box(294, y, 56, 26, GREENF if i in used else "#fff", P, 0, 1.2)
        if i in used:
            b += text(322, y + 13, str(used[i]), 10.5, mono=True, weight="bold")
    b += text(306, 40, "hash table", 9.6, weight="bold", color=P)
    b += note(12, 312, 336, ["Key: the value used to store and find a record.", "Hash function: converts the key into a table index.",
                             "Search time is O(1) on average: no scanning.", ("Two keys with the same index = collision.", RED)], size=9.6)
    return svg(360, 384, b)


# ------------------------------------------------------------------ 11. hash methods
def hash_methods():
    b = title("Hash Functions")
    hv, sq, mid = S.h_midsquare(3205)
    fv, parts, tot = S.h_folding(12345678)
    blocks = [("1. Division method", "h(k) = k mod m   (m: table size, prime)", [f"k = 1234, m = 97", f"1234 mod 97 = {1234 % 97}"], BLUE, BLUEF),
              ("2. Mid-square method", "square the key, take the middle digits", [f"k = 3205, k² = {sq}", f"middle 2 digits = {mid}  → index {hv}"], GREEN, GREENF),
              ("3. Folding method", "split key into parts, add, keep last digits", [f"k = 12345678 → {' + '.join(map(str, parts))}", f"= {tot} → last 2 digits = {fv:02d}"], ORANGE, ORANGEF)]
    y = 36
    for t, f, ex, c, fc in blocks:
        b += box(12, y, 336, 92, fc, c, 8, 1.2)
        b += text(22, y + 18, t, 11, anchor="start", weight="bold", color=c)
        b += text(22, y + 38, f, 9.6, anchor="start", color="#333")
        for i, e in enumerate(ex):
            b += text(30, y + 58 + i * 17, e, 10, anchor="start", mono=True, weight="bold")
        y += 100
    return svg(360, y + 4, b)


DIAGRAMS = {"ds5_bubble": bubble, "ds5_selection": selection, "ds5_insertion": insertion, "ds5_quick_partition": quick_partition,
            "ds5_quick_tree": quick_tree, "ds5_merge": merge, "ds5_radix": radix, "ds5_linear": linear, "ds5_binary": binary,
            "ds5_hash_table": hash_table, "ds5_hash_methods": hash_methods}

if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    for k, f in DIAGRAMS.items():
        with open(os.path.join(OUT, k + ".svg"), "w", encoding="utf-8") as fh:
            fh.write(f())
    print("written", len(DIAGRAMS))
