"""DI03000021 Unit 5 extras: algorithms, numericals (all traced by ds_sort), viva, exam."""
from c_content import SXE, VE, XE, G
from content_DI03000021_u5_notes_a import SN as SNA
from content_DI03000021_u5_notes_b import SN as SNB
from ds_expr import table
import ds_sort as S

SNX = {**SNA, **SNB}
J = S.J


def A(name, key, terms=""):
    return SXE(name, SNX[key].strip("\n"), terms)


def N(id_, q, a):
    return {"id": id_, "q": {"en": q}, "a": {"en": a}}


ALGORITHMS = [
    G("Sorting", [
        A("Bubble sort", "alg_bubble", "Best O(n), worst O(n²). Stable."),
        A("Selection sort", "alg_selection", "Always O(n²). At most n−1 swaps."),
        A("Insertion sort", "alg_insertion", "Best O(n), worst O(n²). Stable."),
        A("Quick sort", "alg_quick", "Avg O(n log n), worst O(n²)."),
        A("Merge sort", "alg_merge", "Always O(n log n). Extra O(n)."),
        A("Radix sort", "alg_radix", "O(d·n). No comparisons."),
    ]),
    G("Searching", [
        A("Linear search", "alg_linear", "O(n). Unsorted data OK."),
        A("Binary search", "alg_binary", "O(log n). Sorted data only."),
    ]),
    G("Hash functions", [
        SXE("Division", "h(k) = k mod m\n(m = table size, prefer prime)", ""),
        SXE("Mid-square", "h(k) = middle r digits of k*k", ""),
        SXE("Folding", "split k into parts, add them,\nkeep last r digits (ignore carry)\nboundary: reverse alternate parts", ""),
        SXE("Linear probing", "slot = (h(k) + i) mod m,\ni = 0, 1, 2, ...", ""),
    ]),
]

# ---------- numericals ----------
N1 = [64, 34, 25, 12, 22, 11, 90]
s1, t1, c1, w1 = S.bubble_table(N1)
N2 = [29, 72, 98, 13, 87, 66, 52]
s2, t2 = S.selection_table(N2)
N3 = [38, 12, 70, 5, 44, 29]
s3, t3 = S.insertion_table(N3)
N4 = [35, 50, 15, 25, 80, 20, 90, 45]
s4, t4 = S.quick_table(N4)
N5 = [45, 23, 11, 89, 77, 98, 4, 28]
s5, t5 = S.merge_table(N5)
lv5 = S.merge_levels(N5)
N6 = [329, 457, 657, 839, 436, 720, 355]
s6, t6 = S.radix_table(N6)
for x, y in ((s1, N1), (s2, N2), (s3, N3), (s4, N4), (s5, N5), (s6, N6)):
    assert x == sorted(y)

N7 = [21, 8, 45, 17, 33, 9, 50, 12]
k7, r7 = S.linear(N7, 33)
k7b, r7b = S.linear(N7, 40)
N8 = [11, 22, 33, 44, 55, 66, 77, 88, 99]
k8, t8 = S.binary_table(N8, 77)
k8b, t8b = S.binary_table(N8, 25)
assert (k7, k7b, k8, k8b) == (4, -1, 6, -1)

K9, M9 = [245, 382, 117, 908, 561, 1234], 11
R9 = [(k, f"{k} mod 11", k % M9) for k in K9]
K10 = [3205, 4567, 1234, 9452]
R10 = []
for k in K10:
    hv, sq, mid = S.h_midsquare(k)
    R10.append((k, sq, len(str(sq)), mid))
K11 = 123456789
parts = [K11 // 10 ** 6, K11 // 10 ** 3 % 1000, K11 % 1000]
shift = sum(parts)
bnd = int(str(parts[0])[::-1]) + parts[1] + int(str(parts[2])[::-1])
assert (shift, bnd) == (1368, 1764)


def probe(keys, m):
    tab, rows = [None] * m, []
    for k in keys:
        h = k % m
        i, tries = h, []
        while tab[i] is not None:
            tries.append(str(i)); i = (i + 1) % m
        tab[i] = k
        rows.append((k, h, ", ".join(tries) + " full" if tries else "-", i))
    return tab, rows


K12 = [72, 27, 36, 24, 63, 81, 92, 101]
tab12, r12 = probe(K12, 10)

NUMERICALS = [
    N("ds5n1", f"Sort {', '.join(map(str, N1))} using bubble sort. Show every pass.",
      "<p><b>Pass 1 in detail:</b></p>" + S.bubble_pass1(N1) + "<p><b>All passes:</b></p>" + t1
      + f"<p>Sorted: <b>{J(s1)}</b>. Comparisons = {c1}, swaps = {w1}.</p>"),
    N("ds5n2", f"Sort {', '.join(map(str, N2))} using selection sort.", t2 + f"<p>Sorted: <b>{J(s2)}</b> (n − 1 = 6 passes).</p>"),
    N("ds5n3", f"Sort {', '.join(map(str, N3))} using insertion sort.", t3 + f"<p>Sorted: <b>{J(s3)}</b>.</p>"),
    N("ds5n4", f"Sort {', '.join(map(str, N4))} using quick sort (first element as pivot).",
      "<p>i moves right while a[i] ≤ pivot; j moves left while a[j] &gt; pivot; swap if i &lt; j, else swap the pivot with a[j].</p>"
      + t4 + f"<p>Sorted: <b>{J(s4)}</b>.</p>"),
    N("ds5n5", f"Sort {', '.join(map(str, N5))} using merge sort.",
      "<p><b>Divide:</b></p>" + table(["Level", "Parts"], [(i, "  ".join(f"[{J(p)}]" for p in lv)) for i, lv in enumerate(lv5)])
      + "<p><b>Merge:</b></p>" + t5 + f"<p>Sorted: <b>{J(s5)}</b>.</p>"),
    N("ds5n6", f"Sort {', '.join(map(str, N6))} using radix sort.", t6 + f"<p>Sorted: <b>{J(s6)}</b> (3 passes because the largest number has 3 digits).</p>"),
    N("ds5n7", f"Search 33 and 40 in {', '.join(map(str, N7))} using linear search.",
      "<p><b>Search 33:</b></p>" + table(["Index", "a[i]", "= 33 ?"], r7) + f"<p>Found at index {k7} after {k7 + 1} comparisons.</p>"
      + "<p><b>Search 40:</b></p>" + table(["Index", "a[i]", "= 40 ?"], r7b) + f"<p>Not found after {len(N7)} comparisons (worst case).</p>"),
    N("ds5n8", f"Search 77 and 25 in the sorted list {', '.join(map(str, N8))} using binary search.",
      "<p><b>Search 77:</b></p>" + t8 + f"<p>Found at index {k8}.</p><p><b>Search 25:</b></p>" + t8b
      + "<p>Not found. At most ⌊log₂ 9⌋ + 1 = 4 comparisons are needed for 9 elements.</p>"),
    N("ds5n9", f"Using the division method with m = 11, find the hash addresses of {', '.join(map(str, K9))}.",
      table(["Key", "k mod 11", "Address"], R9)
      + "<p>All addresses are different, so there is no collision. (11 is prime, which helps spread the keys.)</p>"),
    N("ds5n10", f"Using the mid-square method (2-digit address), find the hash addresses of {', '.join(map(str, K10))}.",
      table(["Key", "k²", "Digits", "Middle 2 digits"], R10)
      + "<p>For an even number of digits the exact middle is used; for an odd number (1234² = 1522756, 7 digits) digits 3 and 4 from the left are taken. Use the same positions for every key of the table.</p>"),
    N("ds5n11", f"Find the 3-digit hash address of the key {K11} using (a) fold shifting and (b) fold boundary.",
      table(["Method", "Parts", "Sum", "Address"], [("Fold shifting", f"{parts[0]} + {parts[1]} + {parts[2]}", shift, f"{shift % 1000:03d}"),
                                                    ("Fold boundary", f"{str(parts[0])[::-1]} + {parts[1]} + {str(parts[2])[::-1]}", bnd, f"{bnd % 1000:03d}")])
      + "<p>In fold boundary the outer parts are reversed. The carry digit (1) is ignored to get a 3-digit address.</p>"),
    N("ds5n12", f"Insert the keys {', '.join(map(str, K12))} into a hash table of size 10 using h(k) = k mod 10 and linear probing.",
      table(["Key", "h(k)", "Slots tried (full)", "Stored at"], r12)
      + "<p><b>Final hash table:</b></p>" + table(["Slot", "Key"], [(i, v if v is not None else "empty") for i, v in enumerate(tab12)])
      + "<p>92 collides at 2 and moves on to 5; 101 collides at 1 and must probe 2 to 7 before slot 8. This shows <b>clustering</b>.</p>"),
]

VIVA = [
    G("Sorting", [
        VE("What is sorting?", "Arranging data in ascending or descending order."),
        VE("Internal vs external sorting?", "Internal sorting works on data in main memory; external sorting is used when the data is on disk because it is too large for memory."),
        VE("What is a stable sort?", "A sort that keeps equal elements in their original relative order, e.g. bubble, insertion, merge."),
        VE("How does bubble sort work?", "It repeatedly compares adjacent elements and swaps them if they are out of order; the largest element moves to the end in each pass."),
        VE("What is the best case of bubble sort?", "O(n), when the array is already sorted and a swap flag is used."),
        VE("How does selection sort work?", "In each pass it selects the smallest element of the unsorted part and swaps it with the first unsorted position."),
        VE("Which simple sort makes the fewest swaps?", "Selection sort: at most n − 1 swaps."),
        VE("How does insertion sort work?", "Each element is inserted into its correct place in the sorted left part by shifting larger elements right."),
        VE("When is insertion sort best?", "For small or nearly sorted data: O(n) in the best case."),
        VE("What is a pivot in quick sort?", "The element around which the array is partitioned; after partitioning it is at its final position."),
        VE("Worst case of quick sort and when?", "O(n²), when the array is already sorted and the first element is the pivot."),
        VE("What is the principle of quick sort and merge sort?", "Divide and conquer."),
        VE("Time complexity of merge sort?", "O(n log n) in all cases; it needs O(n) extra space."),
        VE("How many passes does radix sort need?", "Equal to the number of digits in the largest number."),
        VE("Which sort does not compare elements?", "Radix sort."),
    ]),
    G("Searching", [
        VE("What is linear search?", "Comparing the key with every element one by one until it is found or the list ends."),
        VE("Time complexity of linear search?", "O(n); best case O(1)."),
        VE("What is the condition for binary search?", "The data must be sorted and directly accessible (array)."),
        VE("How is mid calculated in binary search?", "mid = (low + high) / 2."),
        VE("Time complexity of binary search?", "O(log n)."),
        VE("Maximum comparisons in binary search of 1000 elements?", "10."),
    ]),
    G("Hashing", [
        VE("What is hashing?", "A technique that computes the storage address of a record directly from its key using a hash function."),
        VE("What is a hash table?", "An array of slots in which records are stored at addresses given by the hash function."),
        VE("What is a hash function?", "A function that converts a key into a table index."),
        VE("Explain the division method.", "h(k) = k mod m, where m is the table size (preferably prime)."),
        VE("Explain the mid-square method.", "Square the key and take the middle digits as the address."),
        VE("Explain the folding method.", "Split the key into parts, add them, and take the last digits of the sum as the address."),
        VE("What is a collision?", "When two different keys produce the same hash address."),
        VE("Name two collision resolution methods.", "Linear probing (open addressing) and chaining."),
        VE("Average search time with hashing?", "O(1)."),
    ]),
]

EXAM_QS = [
    XE("What is sorting? Differentiate internal and external sorting.", 3),
    XE("Write an algorithm for bubble sort and sort 64, 34, 25, 12, 22, 11, 90.", 4),
    XE("Explain selection sort with an example.", 4),
    XE("Write an algorithm for insertion sort and trace it on given data.", 4),
    XE("Explain quick sort with an algorithm and an example.", 7),
    XE("Explain merge sort with an example. Give its time complexity.", 7),
    XE("Explain radix sort with an example.", 4),
    XE("Compare the time complexity of the sorting algorithms.", 3),
    XE("Write a C program to sort an array using bubble sort.", 4),
    XE("Write a C program to implement selection sort / insertion sort.", 4),
    XE("Explain linear search with an algorithm.", 3),
    XE("Write an algorithm for binary search and search a given key in a sorted list.", 4),
    XE("Write a C program to implement binary search.", 4),
    XE("Differentiate linear search and binary search.", 3),
    XE("Define hashing, key, hash table and hash function.", 3),
    XE("Explain the division, mid-square and folding hash methods with examples.", 7),
    XE("What is a collision? Explain linear probing with an example.", 4),
]
