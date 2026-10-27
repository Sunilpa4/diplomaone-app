"""DI03000021 Unit 5 notes part A: 5.1 sorting (bubble, selection, insertion, quick, merge, radix, comparison)."""
from c_content import make_TE
import ds_sort as S

A6 = [45, 12, 78, 34, 23, 56]
Q8 = [25, 57, 48, 37, 12, 92, 86, 33]
M7 = [38, 27, 43, 3, 9, 82, 10]
R8 = [170, 45, 75, 90, 802, 24, 2, 66]

SN = {
    "alg_bubble": r'''
Algorithm BUBBLE(A, N)
Step 1: Repeat Step 2 for I = 0 to N-2
Step 2:   Set FLAG = 0
          Repeat for J = 0 to N-2-I
            If A[J] > A[J+1] then
              Swap A[J] and A[J+1]
              Set FLAG = 1
          If FLAG = 0 then go to Step 3
Step 3: Exit
''',
    "alg_selection": r'''
Algorithm SELECTION(A, N)
Step 1: Repeat Steps 2-4 for
        I = 0 to N-2
Step 2:   Set MIN = I
Step 3:   Repeat for J = I+1 to N-1
            If A[J] < A[MIN] then
              Set MIN = J
Step 4:   If MIN != I then
            Swap A[I] and A[MIN]
Step 5: Exit
''',
    "alg_insertion": r'''
Algorithm INSERTION(A, N)
Step 1: Repeat Steps 2-5 for
        I = 1 to N-1
Step 2:   Set KEY = A[I], J = I - 1
Step 3:   Repeat while J >= 0 and
          A[J] > KEY
            Set A[J+1] = A[J]
            Set J = J - 1
Step 4:   Set A[J+1] = KEY
Step 5: [End of loop]
Step 6: Exit
''',
    "alg_quick": r'''
Algorithm QUICK(A, LOW, HIGH)
Step 1: If LOW < HIGH then
          K = PARTITION(A, LOW, HIGH)
          QUICK(A, LOW, K-1)
          QUICK(A, K+1, HIGH)
Step 2: Exit

Algorithm PARTITION(A, LOW, HIGH)
Step 1: PIVOT = A[LOW]
        I = LOW + 1, J = HIGH
Step 2: Repeat
          While I <= HIGH and
                A[I] <= PIVOT: I = I+1
          While A[J] > PIVOT: J = J-1
          If I < J then
            Swap A[I] and A[J]
        Until I >= J
Step 3: Swap A[LOW] and A[J]
Step 4: Return J
''',
    "alg_merge": r'''
Algorithm MERGESORT(A, L, R)
Step 1: If L < R then
          M = (L + R) / 2
          MERGESORT(A, L, M)
          MERGESORT(A, M+1, R)
          MERGE(A, L, M, R)
Step 2: Exit

Algorithm MERGE(A, L, M, R)
Step 1: I = L, J = M+1, K = 0
Step 2: While I <= M and J <= R
          If A[I] <= A[J] then
            T[K++] = A[I++]
          Else T[K++] = A[J++]
Step 3: Copy the rest of A[I..M]
        and A[J..R] into T
Step 4: Copy T back into A[L..R]
''',
    "alg_radix": r'''
Algorithm RADIX(A, N)
Step 1: Find MAX; D = number of
        digits in MAX
Step 2: Repeat for P = 1 to D
          a) Empty buckets 0 to 9
          b) For each A[I]: digit =
             P-th digit from right;
             put A[I] in bucket[digit]
          c) Collect buckets 0..9 in
             order back into A
Step 3: Exit
''',
}
T0 = make_TE(SN)


def T(h, b, examples=None, **kw):
    d = T0(h, b, **kw)
    if examples:
        d["examples"] = examples
    return d


_, BT, BC, BS = S.bubble_table(A6)
_, ST = S.selection_table(A6)
_, IT = S.insertion_table(A6)
_, QT = S.quick_table(Q8)
_, MT = S.merge_table(M7)
_, RT = S.radix_table(R8)
J = S.J

SEC_5_1 = {
    "title": {"en": "5.1 Sorting"},
    "items": [
        T("5.1.1 Introduction to Sorting",
          r"""<p><b>Sorting</b> means arranging data elements in a particular order: <b>ascending</b> (increasing) or <b>descending</b> (decreasing). Example: 45 12 78 34 → 12 34 45 78.</p>
<h4>Why sort?</h4>
<ul><li>Searching becomes much faster (binary search needs sorted data).</li>
<li>Reports, merit lists, telephone directories and dictionaries are easier to read.</li></ul>
<h4>Types and terms</h4>
<ul><li><b>Internal sorting:</b> all data fits in main memory (RAM). E.g. bubble, selection, insertion, quick sort.</li>
<li><b>External sorting:</b> the data is too large for main memory and is kept on disk. E.g. merge sort is used.</li>
<li><b>Stable sort:</b> equal elements keep their original relative order (bubble, insertion, merge, radix). Unstable: selection, quick.</li>
<li><b>In-place sort:</b> needs no (or constant) extra memory (bubble, selection, insertion, quick). Merge and radix need extra memory.</li>
<li><b>Pass:</b> one complete scan over the (unsorted part of the) array.</li></ul>
<p>The efficiency of a sort is measured by the number of <b>comparisons</b> and <b>swaps/moves</b>, written in Big-O notation.</p>"""),

        T("5.1.2 Bubble Sort",
          rf"""<p>In bubble sort, <b>adjacent elements are compared</b> and swapped if they are in the wrong order. In each pass, the largest remaining element "bubbles up" to its correct position at the end.</p>
@@alg_bubble@@
<h4>Example: {J(A6)}</h4>
{BT}
<p>Total comparisons = {BC}, swaps = {BS}. Pass 4 has no swap, so the algorithm stops early (FLAG = 0).</p>
<h4>Analysis</h4>
<ul><li>Passes: at most n − 1. Comparisons: (n − 1) + (n − 2) + … + 1 = <b>n(n − 1)/2</b>.</li>
<li>Best case (already sorted, with flag): <b>O(n)</b>. Average and worst case: <b>O(n²)</b>.</li>
<li>Space: O(1), in-place and stable.</li>
<li>Advantage: very simple. Disadvantage: slow for large data.</li></ul>""",
          diagram="ds5_bubble", programs=["ds5p1", "ds5p2"], examples=["ds5n1"], key=True),

        T("5.1.3 Selection Sort",
          rf"""<p>In selection sort, the <b>smallest element</b> of the unsorted part is <b>selected</b> and swapped with the first element of the unsorted part. The sorted part grows from the left by one element in every pass.</p>
@@alg_selection@@
<h4>Example: {J(A6)}</h4>
{ST}
<h4>Analysis</h4>
<ul><li>Comparisons are always n(n − 1)/2 (even for sorted data): best, average and worst case <b>O(n²)</b>.</li>
<li>Swaps: at most n − 1 (one per pass): useful when writing to memory is costly.</li>
<li>Space: O(1), in-place; not stable.</li></ul>""",
          diagram="ds5_selection", programs=["ds5p3"], examples=["ds5n2"], key=True),

        T("5.1.4 Insertion Sort",
          rf"""<p>Insertion sort builds the sorted array one element at a time. Each new element (the <b>key</b>) is <b>inserted</b> into its correct position in the already sorted left part, by shifting the larger elements one place to the right. It works the way we arrange playing cards in the hand.</p>
@@alg_insertion@@
<h4>Example: {J(A6)}</h4>
{IT}
<h4>Analysis</h4>
<ul><li>Best case (sorted data): only one comparison per element, <b>O(n)</b>.</li>
<li>Average and worst case (reverse order): <b>O(n²)</b>.</li>
<li>Space O(1), in-place and stable. Very efficient for <b>small</b> or <b>nearly sorted</b> data.</li></ul>""",
          diagram="ds5_insertion", programs=["ds5p4"], examples=["ds5n3"], key=True),

        T("5.1.5 Quick Sort: Partition",
          rf"""<p>Quick sort is a <b>divide and conquer</b> algorithm (developed by C. A. R. Hoare). One element is chosen as the <b>pivot</b> (here, the first element), and the array is <b>partitioned</b> so that:</p>
<ul><li>all elements smaller than (or equal to) the pivot are on its left,</li>
<li>all elements greater than the pivot are on its right, and</li>
<li>the pivot is at its <b>final sorted position</b>.</li></ul>
@@alg_quick@@
<h4>First partition of {J(Q8)} (pivot 25)</h4>
<ol><li>i moves right from 57: 57 &gt; 25, so i stops at index 1. j moves left from 33: 33, 86 and 92 are &gt; 25, so j stops at 12 (index 4). Since i &lt; j, swap 57 and 12 → 25 12 48 37 57 92 86 33.</li>
<li>i continues: 12 ≤ 25, so it moves on and stops at 48 (index 2). j continues: 57, 37 and 48 are &gt; 25, so it stops at 12 (index 1).</li>
<li>Now i &gt; j, so swap the pivot with a[j] → <b>12 25 48 37 57 92 86 33</b>. 25 is at its final place; everything on its left is ≤ 25 and everything on its right is &gt; 25.</li></ol>""",
          diagram="ds5_quick_partition", programs=["ds5p5"], key=True),

        T("5.1.6 Quick Sort: Complete Process and Analysis",
          rf"""<p>After partitioning, the left part and the right part are sorted <b>recursively</b> in the same way, until every part has 0 or 1 element.</p>
<h4>Example: {J(Q8)}</h4>
{QT}
<h4>Analysis</h4>
<ul><li>Best and average case: <b>O(n log n)</b> (the pivot splits the array into nearly equal halves).</li>
<li>Worst case: <b>O(n²)</b>, when the array is already sorted or reverse sorted (the pivot is always the smallest or largest).</li>
<li>In-place (only the recursion stack, O(log n)); not stable. One of the fastest sorts in practice.</li>
<li>Choosing the middle or a random element as the pivot avoids the worst case for sorted data.</li></ul>""",
          diagram="ds5_quick_tree", programs=["ds5p5"], examples=["ds5n4"], key=True),

        T("5.1.7 Merge Sort",
          rf"""<p>Merge sort is also a <b>divide and conquer</b> algorithm:</p>
<ol><li><b>Divide:</b> split the array into two halves at the middle, M = (L + R) / 2.</li>
<li><b>Conquer:</b> sort each half recursively, until a part has only one element (which is already sorted).</li>
<li><b>Combine:</b> <b>merge</b> the two sorted halves into one sorted array.</li></ol>
@@alg_merge@@
<h4>Example: {J(M7)}</h4>
<p>Divide: [38 27 43 3] and [9 82 10] → [38 27] [43 3] [9 82] [10] → single elements.</p>
{MT}
<h4>Analysis</h4>
<ul><li>Best, average and worst case: always <b>O(n log n)</b> (log n levels, O(n) merging work per level).</li>
<li>Needs an extra array: space <b>O(n)</b>. Stable.</li>
<li>Used for <b>external sorting</b> (large files) and for sorting linked lists.</li></ul>""",
          diagram="ds5_merge", programs=["ds5p6"], examples=["ds5n5"], key=True),

        T("5.1.8 Radix Sort",
          rf"""<p>Radix sort (bucket sort) sorts numbers <b>digit by digit</b>, without comparing elements with each other. It starts from the <b>least significant digit</b> (units) and moves to the most significant digit, using <b>10 buckets</b> (0 to 9) for decimal numbers.</p>
@@alg_radix@@
<h4>Example: {J(R8)}</h4>
<p>The largest number, 802, has 3 digits, so there are 3 passes.</p>
{RT}
<h4>Analysis</h4>
<ul><li>Time: <b>O(d × n)</b>, where d = number of digits. For small d it is effectively linear.</li>
<li>Extra space for buckets: O(n + 10). Stable.</li>
<li>Works for integers and strings of fixed length; not suitable for real numbers directly.</li></ul>""",
          diagram="ds5_radix", programs=["ds5p7"], examples=["ds5n6"], key=True),

        T("5.1.9 Comparison of Sorting Algorithms",
          r"""<table>
<tr><th>Sort</th><th>Best</th><th>Average</th><th>Worst</th><th>Extra space</th><th>Stable</th><th>Method</th></tr>
<tr><td>Bubble</td><td>O(n)</td><td>O(n²)</td><td>O(n²)</td><td>O(1)</td><td>Yes</td><td>exchange</td></tr>
<tr><td>Selection</td><td>O(n²)</td><td>O(n²)</td><td>O(n²)</td><td>O(1)</td><td>No</td><td>selection</td></tr>
<tr><td>Insertion</td><td>O(n)</td><td>O(n²)</td><td>O(n²)</td><td>O(1)</td><td>Yes</td><td>insertion</td></tr>
<tr><td>Quick</td><td>O(n log n)</td><td>O(n log n)</td><td>O(n²)</td><td>O(log n)</td><td>No</td><td>divide and conquer</td></tr>
<tr><td>Merge</td><td>O(n log n)</td><td>O(n log n)</td><td>O(n log n)</td><td>O(n)</td><td>Yes</td><td>divide and conquer</td></tr>
<tr><td>Radix</td><td>O(d·n)</td><td>O(d·n)</td><td>O(d·n)</td><td>O(n + k)</td><td>Yes</td><td>distribution</td></tr>
</table>
<h4>Which one to use?</h4>
<ul><li>Small or nearly sorted data → <b>insertion sort</b>.</li>
<li>Large data in memory, fastest on average → <b>quick sort</b>.</li>
<li>Guaranteed O(n log n), linked lists, external files → <b>merge sort</b>.</li>
<li>Integers with few digits → <b>radix sort</b>.</li>
<li>Fewest swaps → <b>selection sort</b>.</li></ul>""",
          programs=["ds5p14", "ds5p11"], key=True),
    ],
}

NOTES_A = [SEC_5_1]
