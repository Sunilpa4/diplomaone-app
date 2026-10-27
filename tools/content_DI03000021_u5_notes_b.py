"""DI03000021 Unit 5 notes part B: 5.2 searching; 5.3 hashing."""
from c_content import make_TE
import ds_sort as S

B10 = [5, 12, 18, 23, 34, 45, 56, 67, 78, 89]

SN = {
    "alg_linear": r'''
Algorithm LINEAR(A, N, KEY)
Step 1: Repeat for I = 0 to N-1
          If A[I] = KEY then
            Write "Found at", I
            and Exit
Step 2: Write "Not found"
Step 3: Exit
''',
    "alg_binary": r'''
Algorithm BINARY(A, N, KEY)
Step 1: Set LOW = 0, HIGH = N-1
Step 2: Repeat while LOW <= HIGH
          MID = (LOW + HIGH) / 2
          If A[MID] = KEY then
            Write "Found at", MID
            and Exit
          Else If KEY < A[MID] then
            HIGH = MID - 1
          Else
            LOW = MID + 1
Step 3: Write "Not found"
Step 4: Exit
''',
}
T0 = make_TE(SN)


def T(h, b, examples=None, **kw):
    d = T0(h, b, **kw)
    if examples:
        d["examples"] = examples
    return d


_, BT23 = S.binary_table(B10, 23)

SEC_5_2 = {
    "title": {"en": "5.2 Searching"},
    "items": [
        T("5.2.1 Linear Search",
          r"""<p><b>Searching</b> is the process of finding whether a given element (the <b>key</b>) is present in a collection and, if so, its position. The search is <b>successful</b> if the key is found, otherwise <b>unsuccessful</b>.</p>
<p>In <b>linear (sequential) search</b>, the key is compared with each element <b>one by one</b>, from the first to the last, until a match is found or the list ends.</p>
@@alg_linear@@
<p><b>Example:</b> search 56 in 34 12 78 23 56 45 9 → compared with 34, 12, 78, 23, 56 → found at index 4 after 5 comparisons.</p>
<h4>Analysis</h4>
<ul><li>Best case: key at the first position, <b>O(1)</b>.</li>
<li>Worst case: key at the last position or absent, n comparisons, <b>O(n)</b>.</li>
<li>Average: about n/2 comparisons, O(n).</li>
<li>Advantage: simple; works on <b>unsorted</b> data and on linked lists. Disadvantage: slow for large lists.</li></ul>""",
          diagram="ds5_linear", programs=["ds5p8"], examples=["ds5n7"], key=True),

        T("5.2.2 Binary Search",
          rf"""<p><b>Binary search</b> works only on a <b>sorted</b> array. The key is compared with the <b>middle</b> element:</p>
<ul><li>if equal, the search is successful;</li>
<li>if the key is smaller, the search continues in the <b>left half</b>;</li>
<li>if the key is larger, the search continues in the <b>right half</b>.</li></ul>
<p>Each comparison removes half of the remaining elements.</p>
@@alg_binary@@
<h4>Example: search 23 in {S.J(B10)}</h4>
{BT23}
<p>Found at index 3 in 4 comparisons. (Linear search would also need 4 here, but for 89 binary search needs 4 while linear search needs 10.)</p>
<h4>Analysis</h4>
<ul><li>Best case O(1) (key in the middle). Average and worst case <b>O(log₂ n)</b>.</li>
<li>Maximum comparisons = ⌊log₂ n⌋ + 1: 10 elements → 4, 1000 elements → 10, 10 lakh elements → 20.</li>
<li>Can be written iteratively or recursively.</li>
<li>Disadvantages: the data must be sorted, and it needs direct (index) access, so it is not suitable for linked lists.</li></ul>""",
          diagram="ds5_binary", programs=["ds5p9", "ds5p10"], examples=["ds5n8"], key=True),

        T("5.2.3 Linear Search vs Binary Search",
          r"""<table>
<tr><th>Linear search</th><th>Binary search</th></tr>
<tr><td>Data may be unsorted</td><td>Data must be sorted</td></tr>
<tr><td>Compares elements one by one</td><td>Compares with the middle and halves the range</td></tr>
<tr><td>Time O(n)</td><td>Time O(log n)</td></tr>
<tr><td>Simple to write</td><td>Slightly more complex</td></tr>
<tr><td>Works on arrays and linked lists</td><td>Needs an array (direct access)</td></tr>
<tr><td>Good for small lists</td><td>Good for large lists</td></tr>
<tr><td>1000 elements: up to 1000 comparisons</td><td>1000 elements: at most 10 comparisons</td></tr>
</table>""",
          key=True),
    ],
}

SEC_5_3 = {
    "title": {"en": "5.3 Hashing"},
    "items": [
        T("5.3.1 Hashing: Key, Hash Table and Hash Function",
          r"""<p><b>Hashing</b> is a technique that finds the storage location of a record <b>directly from its key</b>, using a formula, so that searching takes <b>O(1)</b> time on average, without comparing many elements.</p>
<h4>Terms</h4>
<ul><li><b>Key:</b> the field that uniquely identifies a record and is used to store and find it, e.g. enrolment number, employee ID.</li>
<li><b>Hash table:</b> an array of fixed size m in which the records are stored. Each position is called a <b>slot</b> or <b>bucket</b>.</li>
<li><b>Hash function h(k):</b> a function that converts a key k into a slot address (index) between 0 and m − 1.</li>
<li><b>Hash address / hash value:</b> the index produced by the hash function.</li>
<li><b>Collision:</b> when two different keys give the same hash address, e.g. 2466 % 10 = 6 and 3456 % 10 = 6.</li></ul>
<h4>Qualities of a good hash function</h4>
<ul><li>Easy and fast to compute.</li>
<li>Distributes keys <b>uniformly</b> over the table.</li>
<li>Produces as few collisions as possible.</li>
<li>Uses all parts of the key.</li></ul>
<h4>Applications</h4>
<p>Symbol tables in compilers, database indexing, password storage, caches, and dictionaries (e.g. Python dict).</p>""",
          diagram="ds5_hash_table", programs=["ds5p12"], key=True),

        T("5.3.2 Division Method",
          r"""<p>The key is divided by the table size m, and the <b>remainder</b> is the hash address:</p>
<p style="text-align:center"><b>h(k) = k mod m</b></p>
<ul><li>The address lies between 0 and m − 1.</li>
<li>m should preferably be a <b>prime number</b> (not close to a power of 2 or 10) to spread the keys better.</li>
<li>Example: m = 97, k = 1234 → 1234 mod 97 = 70. With m = 10, k = 1234 → 4.</li>
<li>Advantage: the simplest and fastest method. Disadvantage: a bad choice of m causes many collisions.</li></ul>""",
          examples=["ds5n9"], key=True),

        T("5.3.3 Mid-Square Method",
          r"""<p>The key is <b>squared</b>, and the required number of digits are taken from the <b>middle</b> of the result as the address:</p>
<p style="text-align:center"><b>h(k) = middle digits of k²</b></p>
<ul><li>The number of digits taken depends on the table size (2 digits for a table of 100 slots, 3 for 1000).</li>
<li>Example: k = 3205 → k² = 10272025 → middle 2 digits = <b>72</b>.</li>
<li>Example: k = 4567 → k² = 20857489 → middle 2 digits = <b>57</b>.</li>
<li>Advantage: the middle digits depend on <b>all</b> digits of the key, so the distribution is good.</li>
<li>Disadvantage: squaring large keys can overflow; the same positions must be used for every key.</li></ul>""",
          examples=["ds5n10"], key=True),

        T("5.3.4 Folding Method",
          r"""<p>The key is divided into <b>parts</b> of equal size (the last part may be shorter), and the parts are <b>added</b>. The last digits of the sum (as many as the address size) form the hash address; the final carry is ignored.</p>
<h4>1. Fold shifting</h4>
<p>The parts are added as they are.<br>k = 12345678, parts of 2 digits: 12 + 34 + 56 + 78 = 180 → address <b>80</b>.</p>
<h4>2. Fold boundary</h4>
<p>Alternate parts (the outer / boundary parts) are <b>reversed</b> before adding.<br>k = 123456789, parts of 3: 321 + 456 + 987 = 1764 → address <b>764</b>.<br>(Fold shifting of the same key: 123 + 456 + 789 = 1368 → 368.)</p>
<ul><li>Useful when keys are very long (phone numbers, account numbers).</li>
<li>All digits of the key take part in the address.</li></ul>""",
          diagram="ds5_hash_methods", programs=["ds5p13"], examples=["ds5n11"], key=True),

        T("5.3.5 Collision and its Resolution (brief)",
          r"""<p>A <b>collision</b> occurs when a hash function gives the same address for two different keys. Since the table is smaller than the range of keys, collisions cannot be avoided completely; they must be handled.</p>
<h4>1. Open addressing: linear probing</h4>
<p>If slot h(k) is occupied, try the next slots one by one, (h(k) + 1) mod m, (h(k) + 2) mod m, …, until a free slot is found. Searching follows the same sequence. Disadvantage: <b>clustering</b> (keys pile up in groups).</p>
<h4>2. Chaining (separate chaining)</h4>
<p>Each slot holds a <b>linked list</b> of all keys that hash to it. A colliding key is simply added to the list (an application of linked lists).</p>
<p>Other methods: quadratic probing and double hashing.</p>""",
          examples=["ds5n12"]),
    ],
}

NOTES_B = [SEC_5_2, SEC_5_3]
