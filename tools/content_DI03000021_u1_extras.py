"""DI03000021 Unit 1 extras: algorithms sheet, solved numericals, viva, exam questions (English only)."""
from c_content import SXE, VE, XE, G
from content_DI03000021_u1_notes_a import SN as SNA
from content_DI03000021_u1_notes_b import SN as SNB


def A(name, key, terms=""):
    src = {**SNA, **SNB}[key]
    return SXE(name, src.strip("\n"), terms)


def N(id_, q, a):
    return {"id": id_, "q": {"en": q}, "a": {"en": a}}


ALGORITHMS = [
    G("Array Algorithms", [
        A("Find the largest element", "alg_max", "Comparisons = n − 1 → O(n)."),
        A("Traverse an array", "alg_traverse", "Visits each element once → O(n)."),
        A("Insert at a position", "alg_insert", "Shift right from the end. Worst O(n)."),
        A("Delete from a position", "alg_delete", "Shift left from POS + 1. Worst O(n)."),
        A("Update an element", "alg_update", "By index O(1)."),
        A("Linear search", "alg_search", "Best O(1), worst O(n)."),
    ]),
    G("Address Formulas", [
        SXE("1-D array", "LOC(A[i]) = Base + w*(i - LB)\nLength  = UB - LB + 1", "w = element size, LB = lower bound."),
        SXE("2-D row major", "LOC(A[i][j]) = Base + w*\n  [(i - Lr)*N + (j - Lc)]", "N = number of columns. Used by C."),
        SXE("2-D column major", "LOC(A[i][j]) = Base + w*\n  [(j - Lc)*M + (i - Lr)]", "M = number of rows. Used by FORTRAN."),
        SXE("Rows and columns from bounds", "M = Ur - Lr + 1\nN = Uc - Lc + 1", "For A[Lr..Ur][Lc..Uc]."),
    ]),
    G("Asymptotic Notations", [
        SXE("Big O (upper bound)", "f(n) <= c*g(n)  for all n >= n0", "Worst case: at most."),
        SXE("Big Omega (lower bound)", "f(n) >= c*g(n)  for all n >= n0", "Best case: at least."),
        SXE("Big Theta (tight bound)", "c1*g(n) <= f(n) <= c2*g(n)\nfor all n >= n0", "Average / exact."),
        SXE("Order of growth", "1 < log n < n < n log n\n  < n^2 < n^3 < 2^n < n!", "Left = faster."),
    ]),
]

NUMERICALS = [
    N("ds1n1", "An integer array A[50] has base address 2000 and each element takes 2 bytes. Find the address of A[23] and of the last element (index starts from 0).",
      r"""<p>Given: Base = 2000, w = 2, LB = 0, UB = 49.</p>
<p>LOC(A[i]) = Base + w × (i − LB)</p>
<p>LOC(A[23]) = 2000 + 2 × (23 − 0) = 2000 + 46 = <b>2046</b></p>
<p>Last element is A[49]: LOC(A[49]) = 2000 + 2 × 49 = <b>2098</b></p>"""),
    N("ds1n2", "An array is declared as A[5:50]. Each element needs 4 bytes and the base address is 1000. Find (i) the number of elements, (ii) the address of A[20], (iii) the address of the last element.",
      r"""<p>Given: LB = 5, UB = 50, w = 4, Base = 1000.</p>
<p>(i) Length = UB − LB + 1 = 50 − 5 + 1 = <b>46 elements</b></p>
<p>(ii) LOC(A[20]) = 1000 + 4 × (20 − 5) = 1000 + 60 = <b>1060</b></p>
<p>(iii) LOC(A[50]) = 1000 + 4 × (50 − 5) = 1000 + 180 = <b>1180</b></p>"""),
    N("ds1n3", "An array A[−10 .. 20] is stored from address 500, with 2 bytes per element. Find the number of elements and the addresses of A[0] and A[15].",
      r"""<p>Given: LB = −10, UB = 20, w = 2, Base = 500.</p>
<p>Length = 20 − (−10) + 1 = <b>31 elements</b></p>
<p>LOC(A[0]) = 500 + 2 × (0 − (−10)) = 500 + 20 = <b>520</b></p>
<p>LOC(A[15]) = 500 + 2 × (15 + 10) = 500 + 50 = <b>550</b></p>"""),
    N("ds1n4", "A 2-D array A[10][20] (indexes start from 0) has base address 100 and each element needs 2 bytes. Find the address of A[5][8] using (i) row major and (ii) column major order.",
      r"""<p>Given: M = 10 rows, N = 20 columns, Lr = Lc = 0, w = 2, Base = 100, i = 5, j = 8.</p>
<p><b>(i) Row major</b><br>LOC = Base + w × [(i − Lr) × N + (j − Lc)]<br>= 100 + 2 × [5 × 20 + 8] = 100 + 2 × 108 = <b>316</b></p>
<p><b>(ii) Column major</b><br>LOC = Base + w × [(j − Lc) × M + (i − Lr)]<br>= 100 + 2 × [8 × 10 + 5] = 100 + 2 × 85 = <b>270</b></p>"""),
    N("ds1n5", "An array A[1..4][1..5] has base address 1000 and element size 4 bytes. Find the address of A[3][4] in row major and column major order.",
      r"""<p>Given: Lr = 1, Ur = 4 → M = 4; Lc = 1, Uc = 5 → N = 5; w = 4; Base = 1000; i = 3, j = 4.</p>
<p><b>Row major:</b> 1000 + 4 × [(3 − 1) × 5 + (4 − 1)] = 1000 + 4 × [10 + 3] = 1000 + 52 = <b>1052</b></p>
<p><b>Column major:</b> 1000 + 4 × [(4 − 1) × 4 + (3 − 1)] = 1000 + 4 × [12 + 2] = 1000 + 56 = <b>1056</b></p>
<p><i>Checked with Program ds1p11.</i></p>"""),
    N("ds1n12", "An array A[−2..2][2..6] is stored from base address 1500 and each element takes 4 bytes. Find the address of A[1][4] in row major and column major order.",
      r"""<p>Rows: Lr = −2, Ur = 2 → M = 2 − (−2) + 1 = 5. Columns: Lc = 2, Uc = 6 → N = 6 − 2 + 1 = 5. w = 4, Base = 1500.</p>
<p><b>Row major:</b> 1500 + 4 × [(1 − (−2)) × 5 + (4 − 2)] = 1500 + 4 × [15 + 2] = 1500 + 68 = <b>1568</b></p>
<p><b>Column major:</b> 1500 + 4 × [(4 − 2) × 5 + (1 − (−2))] = 1500 + 4 × [10 + 3] = 1500 + 52 = <b>1552</b></p>"""),
    N("ds1n6", "Find the frequency count and time complexity of the function that adds the n elements of an array (s = 0; for i = 0 to n−1: s = s + a[i]; return s). How many steps for n = 10?",
      r"""<table><tr><th>Statement</th><th>Count</th></tr>
<tr><td>s = 0</td><td>1</td></tr>
<tr><td>for (i = 0; i &lt; n; i++) (condition tests)</td><td>n + 1</td></tr>
<tr><td>s = s + a[i]</td><td>n</td></tr>
<tr><td>return s</td><td>1</td></tr>
<tr><td><b>Total</b></td><td><b>2n + 3</b></td></tr></table>
<p>Highest-order term is n → <b>O(n)</b>.</p>
<p>For n = 10: 2 × 10 + 3 = <b>23 steps</b>.</p>"""),
    N("ds1n7", "Find the time complexity of: for (i = 0; i < n; i++) for (j = 0; j < i; j++) count++; How many times does count++ run for n = 10?",
      r"""<p>For each value of i, the inner loop runs i times:</p>
<p>i = 0 → 0, i = 1 → 1, i = 2 → 2, …, i = n − 1 → n − 1</p>
<p>Total = 0 + 1 + 2 + … + (n − 1) = <b>n(n − 1) / 2</b> = (n² − n)/2</p>
<p>Highest-order term n²/2 → <b>O(n²)</b>.</p>
<p>For n = 10: 10 × 9 / 2 = <b>45 times</b>.</p>"""),
    N("ds1n8", "Find the time complexity of: i = 1; while (i < n) i = i * 2; How many iterations for n = 64 and n = 1000?",
      r"""<p>i takes the values 1, 2, 4, 8, …, 2ᵏ. The loop stops when 2ᵏ ≥ n, i.e. after k = ⌈log₂ n⌉ iterations.</p>
<p>Time complexity = <b>O(log n)</b>.</p>
<p>n = 64: i = 1, 2, 4, 8, 16, 32 → <b>6 iterations</b> (log₂ 64 = 6).</p>
<p>n = 1000: 2⁹ = 512 &lt; 1000 ≤ 2¹⁰ = 1024 → <b>10 iterations</b>.</p>"""),
    N("ds1n9", "Show that f(n) = 3n + 2 is O(n), Ω(n) and Θ(n).",
      r"""<p><b>Big O:</b> 3n + 2 ≤ 3n + n = 4n when n ≥ 2. So f(n) ≤ 4·n for all n ≥ 2 → c = 4, n₀ = 2 → <b>f(n) = O(n)</b>.</p>
<p><b>Big Ω:</b> 3n + 2 ≥ 3n for all n ≥ 1 → c = 3, n₀ = 1 → <b>f(n) = Ω(n)</b>.</p>
<p><b>Big Θ:</b> combining both, 3n ≤ 3n + 2 ≤ 4n for all n ≥ 2 → c₁ = 3, c₂ = 4, n₀ = 2 → <b>f(n) = Θ(n)</b>.</p>"""),
    N("ds1n10", "Show that f(n) = 10n² + 4n + 2 is O(n²). Find suitable c and n₀.",
      r"""<p>Try c = 11: we need 10n² + 4n + 2 ≤ 11n², i.e. 4n + 2 ≤ n².</p>
<table><tr><th>n</th><th>4n + 2</th><th>n²</th><th>holds?</th></tr>
<tr><td>4</td><td>18</td><td>16</td><td>No</td></tr>
<tr><td>5</td><td>22</td><td>25</td><td>Yes</td></tr>
<tr><td>6</td><td>26</td><td>36</td><td>Yes</td></tr></table>
<p>For all n ≥ 5 the condition holds (n² grows faster than 4n + 2).</p>
<p>So 10n² + 4n + 2 ≤ 11n² for n ≥ 5 → c = 11, n₀ = 5 → <b>f(n) = O(n²)</b>.</p>
<p>(Also 10n² + 4n + 2 ≥ 10n² for n ≥ 1, so f(n) = Ω(n²) and hence Θ(n²).)</p>"""),
    N("ds1n11", "Find the memory needed for int A[10][20] if an int takes 4 bytes. What is the space complexity of adding two n × n matrices into a third matrix?",
      r"""<p>Number of elements = 10 × 20 = <b>200</b>. Memory = 200 × 4 = <b>800 bytes</b>.</p>
<p>Matrix addition C = A + B for n × n matrices needs 3 matrices of n² elements each, plus the loop variables i, j and n (fixed part).</p>
<p>S(P) = 3n² + 3 → <b>O(n²)</b>.</p>"""),
]

VIVA = [
    G("Data and Data Structures", [
        VE("What is a data structure?", "A way of organising and storing data in memory so that it can be accessed and modified efficiently."),
        VE("Differentiate data and information.", "Data are raw facts with no meaning (e.g. marks). Information is processed, meaningful data (e.g. result, average)."),
        VE("What are primitive data structures? Give examples.", "Basic types operated directly by machine instructions and holding a single value: int, float, char, double, pointer."),
        VE("What are non-primitive data structures?", "Structures derived from primitive types that store a collection of values: array, stack, queue, linked list, tree, graph."),
        VE("Differentiate linear and non-linear data structures.", "Linear: elements in a sequence, traversed in one run (array, stack, queue, list). Non-linear: hierarchy or network (tree, graph)."),
        VE("Is a stack linear or non-linear?", "Linear. Its elements are kept in a sequence, though insertion and deletion happen only at the top."),
        VE("What is the difference between static and dynamic data structures?", "Static: size fixed at compile time (array). Dynamic: size changes at run time (linked list)."),
        VE("List the common operations on data structures.", "Traversing, searching, insertion, deletion, sorting and merging."),
    ]),
    G("Algorithms and Complexity", [
        VE("What is an algorithm?", "A finite sequence of well-defined steps that solves a problem, taking input and producing output in finite time."),
        VE("State the characteristics of an algorithm.", "Input, output, definiteness, finiteness and effectiveness."),
        VE("What is time complexity?", "The amount of time an algorithm needs as a function of input size n, measured by counting basic operations."),
        VE("What is space complexity?", "The amount of memory an algorithm needs as a function of n: fixed part + variable part."),
        VE("What is the frequency count method?", "Counting how many times each statement executes and adding them to get the total steps as a function of n."),
        VE("What is Big O notation?", "An upper bound on growth: f(n) ≤ c·g(n) for all n ≥ n₀. It gives the worst case."),
        VE("What is Big Omega notation?", "A lower bound: f(n) ≥ c·g(n) for all n ≥ n₀. It gives the best case."),
        VE("What is Big Theta notation?", "A tight bound: c₁·g(n) ≤ f(n) ≤ c₂·g(n). Both upper and lower bound."),
        VE("What is the time complexity of a nested loop of n inside n?", "O(n²)."),
        VE("Which is faster: O(n log n) or O(n²)?", "O(n log n). For large n it grows much more slowly."),
        VE("What are the best and worst cases of linear search?", "Best O(1) (key at the first position), worst O(n) (key at the end or absent)."),
    ]),
    G("Arrays", [
        VE("What is an array?", "A finite collection of same-type elements stored in contiguous memory under one name and accessed by index."),
        VE("Why does the array index start at 0 in C?", "The index is the offset from the base address: a[i] is at base + i × w, so the first element has offset 0."),
        VE("Give the address formula for a 1-D array.", "LOC(A[i]) = Base + w × (i − LB)."),
        VE("What is row major order?", "Storing a 2-D array row by row. C uses it."),
        VE("What is column major order?", "Storing a 2-D array column by column. FORTRAN uses it."),
        VE("Why are insertion and deletion slow in arrays?", "Elements must be shifted to make or close a gap, which takes O(n) time."),
        VE("What is overflow and underflow in an array?", "Overflow: inserting into a full array. Underflow: deleting from an empty array."),
        VE("Give two disadvantages of arrays.", "Fixed size (wastage or overflow) and slow insertion and deletion."),
    ]),
]

EXAM_QS = [
    XE("Define data structure. Explain the classification of data structures with a diagram.", 4),
    XE("Differentiate primitive and non-primitive data structures.", 3),
    XE("Differentiate linear and non-linear data structures with examples.", 3),
    XE("Differentiate data and information.", 3),
    XE("List and explain the operations performed on data structures.", 4),
    XE("Define algorithm. Explain the characteristics of an algorithm.", 4),
    XE("Explain time complexity and space complexity with examples.", 4),
    XE("Explain Big O, Big Omega and Big Theta notations with graphs.", 7),
    XE("Explain best case, worst case and average case analysis with an example.", 3),
    XE("Find the time complexity of a given code segment using the frequency count method.", 3),
    XE("What is an array? Explain the representation of a 1-D array in memory with the address formula.", 4),
    XE("Explain row major and column major representation of a 2-D array with formulas.", 4),
    XE("An array A[1..4][1..5] has base address 1000 and w = 4. Find the address of A[3][4] in row major and column major order.", 3),
    XE("Write an algorithm to insert an element at a given position in an array.", 4),
    XE("Write an algorithm to delete an element from a given position in an array.", 4),
    XE("Write a C program to find the maximum of 10 numbers using an array and state its time complexity.", 4),
    XE("Write a menu-driven C program to perform insert, delete, search and display operations on an array.", 7),
    XE("Give the advantages, disadvantages and applications of arrays.", 3),
]
