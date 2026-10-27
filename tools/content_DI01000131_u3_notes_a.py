"""DI01000131 Unit 3 notes part A: 3.1 Arrays (English only)."""
from c_content import make_TE

SN = {
    "need": r'''
/* Without array: 5 variables */
int m1, m2, m3, m4, m5;

/* With array: one name */
int m[5];
''',
    "decl_1d": r'''
data_type array_name[size];
''',
    "decl_ex": r'''
int   marks[60];      /* 60 integers  = 240 bytes */
float price[10];      /* 10 floats    = 40 bytes  */
char  name[20];       /* 20 characters = 20 bytes */

#define N 100
int roll[N];          /* symbolic constant as size */
''',
    "decl_bad": r'''
int a[];              /* error: size missing */
int n = 5; int b[n];  /* VLA: C99 only, avoid in Turbo C */
int c[-5];            /* error: negative size */
int d[2.5];           /* error: size must be integer */
''',
    "init_ct": r'''
int a[5] = {10, 20, 30, 40, 50};   /* full */
int b[5] = {1, 2};                 /* partial: 1 2 0 0 0 */
int c[5] = {0};                    /* all elements 0 */
int d[]  = {4, 8, 15, 16};         /* size taken as 4 */
char s[] = {'G', 'T', 'U', '\0'};  /* character array */
char t[] = "GTU";                  /* same, size 4 */
''',
    "init_err": r'''
int e[3] = {1, 2, 3, 4};           /* error: too many */
''',
    "init_rt": r'''
for (i = 0; i < n; i++)
    scanf("%d", &a[i]);

for (i = 0; i < 100; i++)          /* assign by formula */
    sq[i] = i * i;
''',
    "access": r'''
a[0] = 5;             /* first element */
a[n - 1] = 9;         /* last element */
x = a[2] + a[3];
a[i]++;
''',
    "bounds": r'''
int a[5];
a[5] = 100;           /* no compiler error, but outside the array! */
''',
    "decl_2d": r'''
data_type array_name[row_size][column_size];
''',
    "decl_2d_ex": r'''
int   m[3][4];        /* 3 rows, 4 columns = 12 ints = 48 bytes */
float marks[60][5];   /* 60 students x 5 subjects */
''',
    "init_2d": r'''
/* 1. Row-wise with inner braces (recommended) */
int a[2][3] = { {1, 2, 3},
                {4, 5, 6} };

/* 2. Without inner braces – filled row by row */
int b[2][3] = {1, 2, 3, 4, 5, 6};

/* 3. Partial – missing elements become 0 */
int c[2][3] = { {1}, {4, 5} };    /* 1 0 0 / 4 5 0 */

/* 4. First dimension may be omitted */
int d[][3] = { {1, 2, 3}, {4, 5, 6} };

/* 5. All zero */
int z[3][3] = {0};
''',
    "init_2d_rt": r'''
for (i = 0; i < r; i++)
    for (j = 0; j < c; j++)
        scanf("%d", &a[i][j]);
''',
}
T = make_TE(SN)

SEC_3_1 = {
    "title": {"en": "3.1 Arrays"},
    "items": [
        T("3.1.1 Introduction to Arrays",
          r"""<p><b>Definition:</b> An <b>array</b> is a <b>fixed-size</b>, <b>sequenced</b> collection of elements of the <b>same data type</b>, stored in <b>contiguous</b> (adjacent) memory locations and accessed by a <b>common name</b> with an <b>index</b> (subscript).</p>
<h4>Need for arrays</h4>
<p>To store the marks of 60 students we would need 60 separate variables, which is impractical. An array stores all of them under one name:</p>
@@need@@
<p>With an array, a loop can read, process and print all elements using the index.</p>
<h4>Characteristics of arrays</h4>
<ul><li>All elements are of the <b>same data type</b> (homogeneous).</li>
<li>Elements are stored in <b>contiguous</b> memory locations.</li>
<li>The size is <b>fixed</b> at declaration and cannot be changed at run time.</li>
<li>The index starts at <b>0</b>; the last index is <b>size − 1</b>.</li>
<li>Any element can be accessed directly by its index (<b>random access</b>).</li>
<li>The array name holds the <b>base address</b> (address of the first element).</li>
<li>C does <b>not</b> check array bounds.</li></ul>
<h4>Types of arrays (see diagram)</h4>
<ol><li><b>One-dimensional (1-D)</b> – a list, e.g. <code>int a[5];</code></li>
<li><b>Two-dimensional (2-D)</b> – a table/matrix, e.g. <code>int m[3][4];</code></li>
<li><b>Multi-dimensional</b> – three or more dimensions, e.g. <code>int x[2][3][4];</code></li></ol>
<h4>Advantages and disadvantages</h4>
<table><tr><th>Advantages</th><th>Disadvantages</th></tr>
<tr><td>Many values under one name</td><td>Fixed size: memory may be wasted or be insufficient</td></tr>
<tr><td>Easy processing with loops</td><td>Only one data type</td></tr>
<tr><td>Fast random access by index</td><td>Insertion/deletion needs shifting</td></tr>
<tr><td>Used for sorting, searching, matrices</td><td>No bounds checking</td></tr></table>""",
          diagram="c3_array_types"),

        T("3.1.2 One-dimensional Arrays",
          r"""<p>A list of items that is given <b>one variable name</b> and uses <b>only one subscript</b> is called a <b>one-dimensional array</b>. For example, <code>a[5]</code> contains five elements: <code>a[0], a[1], a[2], a[3], a[4]</code>.</p>
<h4>Memory representation (see diagram)</h4>
<p>For <code>int a[5] = {10, 20, 30, 40, 50};</code> with base address 1000 and 4-byte int, the elements are at 1000, 1004, 1008, 1012 and 1016.</p>
<p style="text-align:center"><b>Address of a[i] = Base address + i × sizeof(data type)</b></p>
<p>Example: address of a[3] = 1000 + 3 × 4 = 1012.</p>
<p><b>Total memory</b> = size × sizeof(data type) = 5 × 4 = 20 bytes.</p>
<h4>Accessing elements</h4>
@@access@@
<p>The subscript can be any integer expression: a constant, a variable or an expression such as <code>a[i+1]</code>.</p>
<h4>No bounds checking</h4>
@@bounds@@
<p>C does not check whether an index is inside the array. Writing outside the array can overwrite other data or crash the program, so the programmer must keep the index between 0 and size−1.</p>""",
          diagram="c3_1d_memory"),

        T("3.1.3 Declaration of One-dimensional Arrays",
          r"""<p>Like any other variable, an array must be <b>declared before</b> it is used, so that the compiler can allocate memory.</p>
<h4>Syntax</h4>
@@decl_1d@@
<ul><li><b>data_type</b> – type of each element (int, float, char, …).</li>
<li><b>array_name</b> – a valid identifier.</li>
<li><b>size</b> – maximum number of elements; must be a <b>positive integer constant</b> (or a symbolic constant).</li></ul>
<h4>Examples</h4>
@@decl_ex@@
<h4>Invalid declarations</h4>
@@decl_bad@@
<p><b>Note:</b> a character array (string) must have one extra place for the null character <code>'\0'</code>. To store "GTU" we need <code>char s[4]</code>.</p>"""),

        T("3.1.4 Initialization of One-dimensional Arrays",
          r"""<p>Storing initial values in an array is called <b>initialization</b>. An array can be initialized at <b>compile time</b> or at <b>run time</b>. An uninitialized local array contains <b>garbage</b> values.</p>
<h4>1. Compile-time initialization</h4>
<p><b>Syntax:</b> <code>data_type array_name[size] = {list of values};</code></p>
@@init_ct@@
<ul><li>Values are separated by commas and enclosed in braces.</li>
<li>If fewer values than the size are given, the remaining elements are set to <b>0</b> (partial initialization).</li>
<li>If the size is omitted, the compiler takes the number of values as the size.</li>
<li>Giving more values than the size is an error:</li></ul>
@@init_err@@
<h4>2. Run-time initialization</h4>
<p>Values are given while the program runs, using <code>scanf()</code> or assignment inside a loop. This is used for large arrays or values entered by the user.</p>
@@init_rt@@""",
          programs=["c3p1", "c3p5"]),

        T("3.1.5 Operations on One-dimensional Arrays",
          r"""<p>Common operations performed on 1-D arrays:</p>
<table>
<tr><th>Operation</th><th>Meaning</th><th>Logic</th></tr>
<tr><td><b>Traversal</b></td><td>Visit every element once (print, sum, count)</td><td><code>for (i = 0; i &lt; n; i++)</code></td></tr>
<tr><td><b>Largest / smallest</b></td><td>Find the max or min element</td><td>Start with <code>a[0]</code>, compare with the rest</td></tr>
<tr><td><b>Searching</b></td><td>Find whether an item is present and where</td><td>Linear search: compare one by one</td></tr>
<tr><td><b>Sorting</b></td><td>Arrange in ascending/descending order</td><td>Bubble sort: swap adjacent pairs</td></tr>
<tr><td><b>Insertion</b></td><td>Add an element at a position</td><td>Shift elements right, then insert</td></tr>
<tr><td><b>Deletion</b></td><td>Remove an element from a position</td><td>Shift elements left</td></tr>
<tr><td><b>Reversal</b></td><td>Reverse the order of elements</td><td>Swap a[i] with a[n-1-i]</td></tr>
</table>
<h4>Linear search algorithm (see flowchart)</h4>
<ol><li>Read n, the elements and the key.</li><li>Set i = 0.</li><li>If i &lt; n is false, print "Not found" and stop.</li>
<li>If a[i] == key, print "Found at i" and stop.</li><li>i = i + 1; go to step 3.</li></ol>
<h4>Bubble sort algorithm</h4>
<ol><li>Repeat for pass i = 0 to n−2:</li>
<li>&nbsp;&nbsp;Repeat for j = 0 to n−2−i: if a[j] &gt; a[j+1], swap them.</li>
<li>Print the sorted array.</li></ol>
<p>See the diagram "Bubble Sort – Pass by Pass" for a traced example.</p>""",
          diagram="c3_fc_search", programs=["c3p2", "c3p3", "c3p6"]),

        T("3.1.6 Bubble Sort – Working",
          r"""<p><b>Bubble sort</b> is the simplest sorting technique. In each pass, <b>adjacent elements are compared</b> and <b>swapped</b> if they are in the wrong order. After every pass the largest remaining element moves ("bubbles") to its correct position at the end.</p>
<h4>Example: 50 20 40 10 30 (see diagram)</h4>
<table><tr><th>Pass</th><th>Result</th><th>Comparisons</th></tr>
<tr><td>1</td><td>20 40 10 30 <b>50</b></td><td>4</td></tr>
<tr><td>2</td><td>20 10 30 <b>40 50</b></td><td>3</td></tr>
<tr><td>3</td><td>10 20 <b>30 40 50</b></td><td>2</td></tr>
<tr><td>4</td><td><b>10 20 30 40 50</b></td><td>1</td></tr></table>
<ul><li>For n elements: <b>n − 1 passes</b>; pass i needs n − 1 − i comparisons.</li>
<li>Total comparisons = n(n − 1)/2 = 10 for n = 5.</li>
<li>Swapping uses a temporary variable: <code>temp = a[j]; a[j] = a[j+1]; a[j+1] = temp;</code></li></ul>""",
          diagram="c3_bubble", programs=["c3p4"]),

        T("3.1.7 Two-dimensional Arrays",
          r"""<p>An array with <b>two subscripts</b> is called a <b>two-dimensional array</b>. It stores data in the form of a <b>table</b> (matrix) with rows and columns, e.g. the marks of 60 students in 5 subjects.</p>
<p>In <code>m[i][j]</code>, the first subscript <code>i</code> is the <b>row</b> and the second subscript <code>j</code> is the <b>column</b>. Both start at 0.</p>
<h4>Memory representation – row-major order (see diagram)</h4>
<p>Memory is linear, so C stores a 2-D array <b>row by row</b>: all elements of row 0, then row 1, and so on. This is called <b>row-major order</b>.</p>
<p style="text-align:center"><b>Address of a[i][j] = Base + (i × number_of_columns + j) × size</b></p>
<p>Example: <code>int m[2][3]</code>, base 1000 → address of m[1][2] = 1000 + (1×3 + 2)×4 = 1020.</p>
<p><b>Total memory</b> = rows × columns × size = 2 × 3 × 4 = 24 bytes.</p>
<h4>Applications</h4>
<p>Matrices (addition, multiplication, transpose), tables of marks/sales, games boards, images (pixels).</p>""",
          diagram="c3_2d_memory"),

        T("3.1.8 Declaration of Two-dimensional Arrays",
          r"""<h4>Syntax</h4>
@@decl_2d@@
<ul><li><b>row_size</b> – number of rows; <b>column_size</b> – number of columns.</li>
<li>Each size is written in a separate pair of brackets. <code>int m[3,4];</code> is <b>wrong</b>.</li>
<li>Total elements = row_size × column_size.</li></ul>
<h4>Examples</h4>
@@decl_2d_ex@@
<p>Elements of <code>int m[3][4]</code>: m[0][0] … m[0][3], m[1][0] … m[1][3], m[2][0] … m[2][3].</p>"""),

        T("3.1.9 Initialization of Two-dimensional Arrays",
          r"""<h4>1. Compile-time initialization</h4>
@@init_2d@@
<ul><li>Inner braces make each row clear; elements not given become 0.</li>
<li>The <b>first dimension (rows) may be omitted</b>; the <b>column size is compulsory</b>, because the compiler needs it to know where each row ends.</li></ul>
<h4>2. Run-time initialization</h4>
<p>Nested loops are used: the outer loop for rows, the inner loop for columns.</p>
@@init_2d_rt@@
<p>To print in matrix form, put <code>printf("\n")</code> after the inner loop.</p>""",
          programs=["c3p7"]),

        T("3.1.10 Matrix Operations using 2-D Arrays",
          r"""<table>
<tr><th>Operation</th><th>Condition</th><th>Formula</th><th>Result order</th></tr>
<tr><td><b>Addition</b></td><td>Same order</td><td><code>c[i][j] = a[i][j] + b[i][j]</code></td><td>m × n</td></tr>
<tr><td><b>Subtraction</b></td><td>Same order</td><td><code>c[i][j] = a[i][j] - b[i][j]</code></td><td>m × n</td></tr>
<tr><td><b>Multiplication</b></td><td>cols of A = rows of B</td><td><code>c[i][j] += a[i][k] * b[k][j]</code></td><td>m × p</td></tr>
<tr><td><b>Transpose</b></td><td>Any</td><td><code>t[j][i] = a[i][j]</code></td><td>n × m</td></tr>
<tr><td><b>Diagonal sum</b></td><td>Square matrix</td><td><code>if (i == j) sum += a[i][j]</code></td><td>–</td></tr>
</table>
<h4>Matrix multiplication (see diagram)</h4>
<p>Each element C[i][j] is the sum of products of <b>row i of A</b> and <b>column j of B</b>, so three nested loops are needed:</p>
<pre class="c">for (i = 0; i &lt; m; i++)
    for (j = 0; j &lt; p; j++)
    {
        c[i][j] = 0;
        for (k = 0; k &lt; n; k++)
            c[i][j] += a[i][k] * b[k][j];
    }</pre>""",
          diagram="c3_matmul", programs=["c3p8", "c3p9", "c3p10", "c3p11"]),

        T("Key Points – 3.1",
          r"""<ul>
<li>Array = fixed-size collection of <b>same-type</b> elements in <b>contiguous</b> memory, accessed by index.</li>
<li>Index: 0 to size−1. C does <b>no bounds checking</b>.</li>
<li>1-D: <code>int a[5];</code> address = base + i × size; memory = n × size.</li>
<li>Initialization: <code>{10, 20}</code> → rest 0; <code>int d[] = {…}</code> → size from list; run time with a loop + scanf.</li>
<li>2-D: <code>int m[r][c];</code> stored in <b>row-major</b> order; address = base + (i × c + j) × size.</li>
<li>2-D initialization: row size may be omitted, <b>column size is compulsory</b>.</li>
<li>Bubble sort: n−1 passes, adjacent swaps. Linear search: compare one by one.</li>
<li>Matrix multiplication needs cols(A) = rows(B) and 3 nested loops.</li>
</ul>""", key=True),
    ],
}

NOTES_A = [SEC_3_1]
