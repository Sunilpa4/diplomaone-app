"""DI03000021 Unit 1 notes part B: 1.4 arrays and their representation, 1.5 array operations."""
from c_content import make_TE

SN = {
    "arr_decl": r'''
int marks[5];                  /* 5 ints        */
float price[3] = {9.5, 12, 7.25};
char name[20] = "GTU";
int a[] = {4, 8, 15, 16, 23};  /* size 5 */
''',
    "arr_2d": r'''
int m[2][3] = { {1, 2, 3},
                {4, 5, 6} };   /* 2 rows, 3 cols */
printf("%d", m[1][2]);         /* 6 */
''',
    "alg_traverse": r'''
Algorithm TRAVERSE(A, LB, UB)
Step 1: Set K = LB
Step 2: Repeat while K <= UB
            Process A[K]   (e.g. print)
            Set K = K + 1
        [End of loop]
Step 3: Exit
''',
    "alg_insert": r'''
Algorithm INSERT(A, N, POS, ITEM)
Step 1: [Check overflow]
        If N = MAX then
            Write "Overflow" and Exit
Step 2: Set J = N - 1
Step 3: Repeat while J >= POS
            Set A[J + 1] = A[J]
            Set J = J - 1
        [End of loop]
Step 4: Set A[POS] = ITEM
Step 5: Set N = N + 1
Step 6: Exit
''',
    "alg_delete": r'''
Algorithm DELETE(A, N, POS)
Step 1: [Check underflow]
        If N = 0 then
            Write "Underflow" and Exit
Step 2: Set ITEM = A[POS]
Step 3: Repeat for J = POS to N - 2
            Set A[J] = A[J + 1]
        [End of loop]
Step 4: Set N = N - 1
Step 5: Write ITEM deleted
Step 6: Exit
''',
    "alg_update": r'''
Algorithm UPDATE(A, N, POS, NEW)
Step 1: If POS < 0 or POS >= N then
            Write "Invalid" and Exit
Step 2: Set A[POS] = NEW
Step 3: Exit
''',
    "alg_search": r'''
Algorithm LSEARCH(A, N, KEY)
Step 1: Set I = 0, LOC = -1
Step 2: Repeat while I < N
            If A[I] = KEY then
                Set LOC = I, go to Step 3
            Set I = I + 1
        [End of loop]
Step 3: If LOC = -1 then
            Write "Not found"
        Else
            Write "Found at", LOC + 1
Step 4: Exit
''',
}
T0 = make_TE(SN)


def T(h, b, examples=None, **kw):
    d = T0(h, b, **kw)
    if examples:
        d["examples"] = examples
    return d


SEC_1_4 = {
    "title": {"en": "1.4 Arrays and Their Representation"},
    "items": [
        T("1.4.1 Array: Definition and Representation in Memory",
          r"""<p>An <b>array</b> is a <b>finite, ordered collection of homogeneous (same type) elements</b> stored in <b>contiguous memory locations</b> and referred to by a <b>common name</b>. Each element is accessed with an <b>index</b> (subscript).</p>
@@arr_decl@@
<h4>Features of arrays</h4>
<ul><li><b>Homogeneous:</b> all elements have the same data type.</li>
<li><b>Contiguous:</b> elements are stored side by side in memory.</li>
<li><b>Fixed size:</b> the size is decided at declaration and cannot change (static).</li>
<li><b>Indexed:</b> in C the index starts from 0 (lower bound LB = 0) and ends at size − 1 (upper bound UB).</li>
<li><b>Random access:</b> any element can be reached directly in O(1) time using its index.</li></ul>
<h4>Number of elements (length)</h4>
<p><b>Length = UB − LB + 1</b>. For A[5..50], length = 50 − 5 + 1 = 46.</p>
<h4>Address of an element in a 1-D array</h4>
<p>Because the elements are contiguous, the address of any element can be calculated from the address of the first element (the <b>base address</b>):</p>
<p style="text-align:center"><b>LOC(A[i]) = Base + w × (i − LB)</b></p>
<ul><li><b>Base</b> = address of the first element</li>
<li><b>w</b> = size of one element in bytes (word size)</li>
<li><b>LB</b> = lower bound of the index (0 in C)</li></ul>
<p>Example: int A[6], base = 1000, w = 4. LOC(A[2]) = 1000 + 4 × (2 − 0) = <b>1008</b>.</p>""",
          diagram="ds1_array_memory", programs=["ds1p4"], examples=["ds1n1", "ds1n2", "ds1n3"], key=True),

        T("1.4.2 Two-Dimensional Arrays: Row Major and Column Major",
          r"""<p>A <b>2-D array</b> stores elements in the form of a table (matrix) of <b>M rows and N columns</b>. It has M × N elements.</p>
@@arr_2d@@
<p>Memory, however, is one-dimensional (a single line of bytes). The table is therefore stored in one of two orders:</p>
<h4>1. Row major order</h4>
<ul><li>Elements are stored <b>row by row</b>: all elements of row 0, then all of row 1, and so on.</li>
<li>Used by <b>C, C++, Java and Python</b>.</li>
<li>For a matrix [[a b c],[d e f]] the memory order is: a b c d e f.</li></ul>
<p style="text-align:center"><b>LOC(A[i][j]) = Base + w × [ (i − L<sub>r</sub>) × N + (j − L<sub>c</sub>) ]</b></p>
<h4>2. Column major order</h4>
<ul><li>Elements are stored <b>column by column</b>: all elements of column 0, then column 1, and so on.</li>
<li>Used by <b>FORTRAN, MATLAB and R</b>.</li>
<li>For the same matrix the memory order is: a d b e c f.</li></ul>
<p style="text-align:center"><b>LOC(A[i][j]) = Base + w × [ (j − L<sub>c</sub>) × M + (i − L<sub>r</sub>) ]</b></p>
<p>where M = number of rows, N = number of columns, L<sub>r</sub> = lower bound of rows, L<sub>c</sub> = lower bound of columns, w = element size.</p>
<p>If the bounds are given as A[L<sub>r</sub>..U<sub>r</sub>][L<sub>c</sub>..U<sub>c</sub>], then M = U<sub>r</sub> − L<sub>r</sub> + 1 and N = U<sub>c</sub> − L<sub>c</sub> + 1.</p>
<table>
<tr><th>Row major</th><th>Column major</th></tr>
<tr><td>Row by row</td><td>Column by column</td></tr>
<tr><td>Uses N (columns) in the formula</td><td>Uses M (rows) in the formula</td></tr>
<tr><td>C, C++, Java</td><td>FORTRAN, MATLAB</td></tr>
<tr><td>a b c d e f</td><td>a d b e c f</td></tr>
</table>
<p><i>Tip:</i> in row major, to reach row i you skip i complete rows of N elements each. In column major, to reach column j you skip j complete columns of M elements each.</p>""",
          diagram="ds1_row_col_major", programs=["ds1p10", "ds1p11"], examples=["ds1n4", "ds1n5"], key=True),

        T("1.4.3 Advantages, Disadvantages and Applications of Arrays",
          r"""<h4>Advantages</h4>
<ul><li><b>Random access:</b> any element is accessed in O(1) time with its index.</li>
<li>Simple to declare and use; many items with <b>one name</b>.</li>
<li>Easy traversal with a loop; good for sorting and searching (binary search needs an array).</li>
<li>No extra memory for links (unlike a linked list).</li>
<li>Used to implement other structures: stack, queue, heap, hash table, matrix.</li></ul>
<h4>Disadvantages</h4>
<ul><li><b>Fixed size:</b> must be known in advance; cannot grow or shrink at run time.</li>
<li><b>Memory wastage</b> if fewer elements are stored than declared; <b>overflow</b> if more are needed.</li>
<li><b>Insertion and deletion are slow (O(n))</b>, because elements must be shifted.</li>
<li>Only <b>homogeneous</b> elements can be stored.</li>
<li>Needs a <b>contiguous</b> block of memory, which may not be available for very large arrays.</li></ul>
<h4>Applications</h4>
<ul><li>Storing lists of data: marks, salaries, temperatures.</li>
<li>Matrices and tables (2-D arrays), images (pixels).</li>
<li>Implementing stack, queue, heap and hash tables.</li>
<li>Lookup tables, sorting and searching algorithms.</li>
<li>CPU scheduling tables and database records.</li></ul>"""),
    ],
}

SEC_1_5 = {
    "title": {"en": "1.5 Array Operations: Traverse, Insert, Delete, Update, Search"},
    "items": [
        T("1.5.1 Traversing an Array",
          r"""<p><b>Traversing</b> means accessing (visiting) <b>each element exactly once</b> in order to process it: print it, add it to a sum, count it, find the maximum, etc.</p>
@@alg_traverse@@
<ul><li>Number of steps = number of elements = n.</li>
<li>Time complexity: <b>O(n)</b>. Space: O(1) extra.</li></ul>
<p>Applications: displaying elements, sum and average, maximum and minimum, counting even/odd numbers, reversing an array.</p>""",
          programs=["ds1p12", "ds1p13"]),

        T("1.5.2 Insertion in an Array",
          r"""<p><b>Insertion</b> adds a new element at a given position. Since array elements are contiguous, all elements from that position to the end must first be <b>shifted one place to the right</b> to create space.</p>
<ul><li>Shifting must start from the <b>last element</b> and move backwards. Starting from the front would overwrite values.</li>
<li>Before inserting, check for <b>overflow</b> (array already full, N = MAX).</li></ul>
@@alg_insert@@
<p>(POS here is the array index, starting from 0.)</p>
<h4>Complexity</h4>
<ul><li><b>Best case</b> O(1): insert at the end, no shifting.</li>
<li><b>Worst case</b> O(n): insert at the beginning, all n elements shift.</li>
<li><b>Average case</b> O(n): about n/2 shifts.</li></ul>
<p><b>Inserting into a sorted array:</b> start from the end, shift every element larger than the new item one place right, then place the item in the gap.</p>""",
          diagram="ds1_insert_delete", programs=["ds1p5", "ds1p9"], key=True),

        T("1.5.3 Deletion from an Array",
          r"""<p><b>Deletion</b> removes the element at a given position. All the elements after it are <b>shifted one place to the left</b> to fill the gap, and the number of elements N is reduced by 1.</p>
<ul><li>Shifting starts from the element <b>just after</b> the deleted position and moves forward.</li>
<li>Before deleting, check for <b>underflow</b> (array empty, N = 0).</li></ul>
@@alg_delete@@
<h4>Complexity</h4>
<ul><li><b>Best case</b> O(1): delete the last element.</li>
<li><b>Worst case</b> O(n): delete the first element, n − 1 elements shift.</li>
<li><b>Average case</b> O(n).</li></ul>
<p>Deleting <b>by value</b> means first searching for the value (O(n)) and then deleting at that position.</p>""",
          programs=["ds1p6"], key=True),

        T("1.5.4 Updating an Element",
          r"""<p><b>Update</b> (modify) changes the value of an existing element. No shifting is needed and the number of elements does not change.</p>
@@alg_update@@
<ul><li><b>Update by index:</b> a single assignment <code>A[POS] = NEW</code> → <b>O(1)</b>.</li>
<li><b>Update by value:</b> first search for the old value (O(n)), then replace it → <b>O(n)</b>.</li></ul>""",
          programs=["ds1p7"]),

        T("1.5.5 Searching in an Array",
          r"""<p><b>Searching</b> finds the location (index or position) of an element with a given value, called the <b>key</b>. The search is <b>successful</b> if the key is found, and <b>unsuccessful</b> otherwise.</p>
<h4>Linear (sequential) search</h4>
<p>The key is compared with every element, one by one from the first, until it is found or the array ends.</p>
@@alg_search@@
<ul><li>Works on <b>unsorted and sorted</b> arrays.</li>
<li>Best case O(1), worst case O(n), average about n/2 comparisons → O(n).</li></ul>
<p><b>Binary search</b> (Unit 5) works only on <b>sorted</b> arrays. It repeatedly halves the search range, giving O(log n).</p>
<h4>Summary of array operations</h4>
<table>
<tr><th>Operation</th><th>Best</th><th>Worst</th></tr>
<tr><td>Access by index</td><td>O(1)</td><td>O(1)</td></tr>
<tr><td>Traverse</td><td>O(n)</td><td>O(n)</td></tr>
<tr><td>Insert</td><td>O(1) at end</td><td>O(n) at start</td></tr>
<tr><td>Delete</td><td>O(1) at end</td><td>O(n) at start</td></tr>
<tr><td>Update by index</td><td>O(1)</td><td>O(1)</td></tr>
<tr><td>Linear search</td><td>O(1)</td><td>O(n)</td></tr>
</table>""",
          programs=["ds1p14"]),
    ],
}

NOTES_B = [SEC_1_4, SEC_1_5]
