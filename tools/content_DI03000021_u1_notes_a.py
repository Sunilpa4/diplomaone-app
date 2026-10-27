"""DI03000021 Unit 1 notes part A: 1.1 data structures, 1.2 algorithms, 1.3 complexity and asymptotic notations."""
from c_content import make_TE

SN = {
    "alg_max": r'''
Algorithm MAX(A, N)
A = array of N elements, MAX = largest
Step 1: [Initialize]  Set MAX = A[0]
Step 2: [Loop]  Repeat for I = 1 to N-1
            If A[I] > MAX then
                Set MAX = A[I]
        [End of loop]
Step 3: [Output]  Print MAX
Step 4: Exit
''',
    "fc_sum": r'''
int sum(int a[], int n)
{
    int s = 0, i;             /* 1          */
    for (i = 0; i < n; i++)   /* n + 1 tests */
        s = s + a[i];         /* n          */
    return s;                 /* 1          */
}                             /* total 2n+3 */
''',
    "fc_nested": r'''
for (i = 0; i < n; i++)       /* outer: n   */
    for (j = 0; j < n; j++)   /* inner: n   */
        c = c + 1;            /* n x n = n2 */
''',
    "fc_log": r'''
i = 1;
while (i < n)        /* i = 1,2,4,8 ... */
    i = i * 2;       /* runs log2(n) times */
''',
    "fc_const": r'''
int square(int x)
{
    return x * x;    /* always 1 step: O(1) */
}
''',
    "space_fixed": r'''
int add(int a, int b)
{
    int c = a + b;   /* a, b, c: fixed */
    return c;        /* S(P) = c -> O(1) */
}
''',
    "space_var": r'''
int total(int a[], int n)
{
    int i, s = 0;    /* fixed: i, s, n  */
    for (i = 0; i < n; i++)
        s += a[i];   /* a[] : n words    */
    return s;        /* S(P) = n + 3 = O(n) */
}
''',
}
T0 = make_TE(SN)


def T(h, b, examples=None, **kw):
    d = T0(h, b, **kw)
    if examples:
        d["examples"] = examples
    return d


SEC_1_1 = {
    "title": {"en": "1.1 Basic Concepts of Data Structures"},
    "items": [
        T("1.1.1 Data and Information",
          r"""<p><b>Data</b> are raw facts and figures, such as numbers, characters, names or marks, that have no meaning on their own. Example: <i>67, 82, 45, 91</i>.</p>
<p><b>Information</b> is data that has been <b>processed</b> (organised, calculated, compared) so that it has a meaning and is useful for decisions. Example: <i>"Sara is the topper with 91 marks; class average is 71.25"</i>.</p>
<table>
<tr><th>Data</th><th>Information</th></tr>
<tr><td>Raw, unorganised facts</td><td>Processed, organised data</td></tr>
<tr><td>No meaning by itself</td><td>Meaningful and useful</td></tr>
<tr><td>Input to processing</td><td>Output of processing</td></tr>
<tr><td>Example: list of marks</td><td>Example: result, rank, average</td></tr>
</table>
<h4>Related terms</h4>
<ul><li><b>Data item / field:</b> a single unit of value, e.g. roll number.</li>
<li><b>Group item:</b> a data item made of sub-items, e.g. name = first name + last name.</li>
<li><b>Record:</b> a collection of related fields about one entity, e.g. one student's roll no, name and marks.</li>
<li><b>File:</b> a collection of records of the same type, e.g. all students of a class.</li>
<li><b>Entity:</b> something that has attributes, e.g. student. <b>Attribute:</b> a property of the entity, e.g. age.</li></ul>""",
          diagram="ds1_data_info"),

        T("1.1.2 Data Structure: Definition and Need",
          r"""<p>A <b>data structure</b> is a particular way of <b>organising, storing and managing data in memory</b> so that it can be used (accessed and modified) <b>efficiently</b>.</p>
<p>In short: <b>Data Structure = organised data + allowed operations</b>.</p>
<p>Niklaus Wirth summed it up as: <b>Algorithms + Data Structures = Programs</b>.</p>
<h4>Need for data structures</h4>
<ul><li><b>Efficient processing:</b> a good structure makes searching, inserting and deleting faster. Example: searching a sorted array with binary search takes about 20 comparisons for 10 lakh items, while linear search may take 10 lakh.</li>
<li><b>Large amounts of data:</b> real applications (banking, railway reservation, social media) handle millions of records that must be organised.</li>
<li><b>Proper use of memory:</b> structures like linked lists use memory only when needed.</li>
<li><b>Reusability:</b> a stack or queue, once written, can be used in many programs.</li>
<li><b>Abstraction:</b> the user works with operations (push, pop) without worrying about how they are stored.</li></ul>
<h4>Real-life examples</h4>
<ul><li><b>Stack:</b> pile of plates, undo in an editor, browser back button.</li>
<li><b>Queue:</b> ticket counter line, printer jobs, CPU scheduling.</li>
<li><b>Tree:</b> folders on a computer, family tree, organisation chart.</li>
<li><b>Graph:</b> road map (Google Maps), friends on social media, computer networks.</li></ul>""",
          key=True),

        T("1.1.3 Types of Data Structures: Primitive and Non-Primitive",
          r"""<p>Data structures are classified as shown in the diagram.</p>
<h4>1. Primitive data structures</h4>
<ul><li>Basic data types that are <b>directly operated upon by machine instructions</b>.</li>
<li>Each holds a <b>single value</b>.</li>
<li>Examples: <code>int</code>, <code>float</code>, <code>double</code>, <code>char</code>, pointer.</li>
<li>Their size depends on the machine and compiler (e.g. int = 2 bytes in Turbo C, 4 bytes in GCC).</li></ul>
<h4>2. Non-primitive data structures</h4>
<ul><li><b>Derived</b> from primitive data structures.</li>
<li>Store a <b>group of values</b> (homogeneous or heterogeneous) and the relationship between them.</li>
<li>Examples: arrays, stacks, queues, linked lists, trees, graphs, files.</li>
<li>They are further divided into <b>linear</b> and <b>non-linear</b> data structures.</li></ul>
<table>
<tr><th>Primitive</th><th>Non-primitive</th></tr>
<tr><td>Basic, built-in types</td><td>Derived from primitive types</td></tr>
<tr><td>Hold a single value</td><td>Hold a collection of values</td></tr>
<tr><td>Operated directly by the CPU</td><td>Operated through algorithms</td></tr>
<tr><td>Fixed size</td><td>Size may be fixed or dynamic</td></tr>
<tr><td>int, float, char, double, pointer</td><td>Array, stack, queue, list, tree, graph</td></tr>
</table>""",
          diagram="ds1_classification", programs=["ds1p2"], key=True),

        T("1.1.4 Linear and Non-Linear Data Structures",
          r"""<h4>Linear data structure</h4>
<p>Elements are arranged in a <b>sequence</b>, one after another. Every element (except the first and the last) has exactly one <b>predecessor</b> and one <b>successor</b>. Elements can be traversed in a single run.</p>
<p>Examples: <b>array, stack, queue, linked list</b>.</p>
<h4>Non-linear data structure</h4>
<p>Elements are arranged in a <b>hierarchical</b> or <b>network</b> manner. One element can be connected to several other elements, so they cannot be traversed in a single run.</p>
<p>Examples: <b>tree, graph</b>.</p>
<table>
<tr><th>Linear</th><th>Non-linear</th></tr>
<tr><td>Elements in a sequence</td><td>Elements in a hierarchy or network</td></tr>
<tr><td>Each element has at most one predecessor and one successor</td><td>An element may be linked to many elements</td></tr>
<tr><td>Single level</td><td>Multiple levels</td></tr>
<tr><td>Traversed in a single run</td><td>Needs special traversals (inorder, BFS, DFS…)</td></tr>
<tr><td>Easy to implement</td><td>More complex to implement</td></tr>
<tr><td>Memory may be wasted (array)</td><td>Memory used efficiently</td></tr>
<tr><td>Array, stack, queue, linked list</td><td>Tree, graph</td></tr>
</table>
<h4>Static and dynamic data structures</h4>
<ul><li><b>Static:</b> size fixed at compile time, e.g. array.</li>
<li><b>Dynamic:</b> size can grow or shrink at run time, e.g. linked list.</li></ul>""",
          diagram="ds1_linear_nonlinear", key=True),

        T("1.1.5 Operations on Data Structures",
          r"""<p>The following operations are performed on almost every data structure:</p>
<ol><li><b>Traversing:</b> accessing each element exactly once to process it (print, count, sum).</li>
<li><b>Searching:</b> finding the location of an element with a given value (key).</li>
<li><b>Insertion:</b> adding a new element.</li>
<li><b>Deletion:</b> removing an existing element.</li>
<li><b>Sorting:</b> arranging elements in ascending or descending order.</li>
<li><b>Merging:</b> combining the elements of two structures into one.</li></ol>
<p>Some structures allow these operations only in a restricted way. In a <b>stack</b>, insertion (push) and deletion (pop) happen only at the top. In a <b>queue</b>, insertion is at the rear and deletion at the front.</p>
<p>The choice of data structure depends on which operations are needed most often. For example, arrays give fast access by index, while linked lists give fast insertion and deletion.</p>""",
          diagram="ds1_operations"),
    ],
}

SEC_1_2 = {
    "title": {"en": "1.2 Introduction to Algorithms"},
    "items": [
        T("1.2.1 Algorithm: Definition and Writing Conventions",
          r"""<p>An <b>algorithm</b> is a <b>finite sequence of well-defined steps</b> for solving a particular problem. It takes some input, processes it, and produces the required output in a finite amount of time.</p>
<p>The word comes from the name of the Persian mathematician <b>al-Khwarizmi</b>.</p>
<h4>Conventions used in GTU-style algorithms</h4>
<ul><li>Name of the algorithm with its parameters: <code>Algorithm MAX(A, N)</code>.</li>
<li>Numbered steps: Step 1, Step 2, …, each with a comment in [ ] brackets.</li>
<li>Assignment with <b>Set</b> or <code>←</code>: <code>Set MAX = A[0]</code>.</li>
<li>Decision: <code>If condition then … [End of If]</code>.</li>
<li>Loop: <code>Repeat for I = 1 to N</code> or <code>Repeat while condition</code>.</li>
<li>Input/Output: <code>Read</code>, <code>Write</code> / <code>Print</code>; and <code>Exit</code> at the end.</li></ul>
<h4>Example: largest of N numbers</h4>
@@alg_max@@
<h4>Algorithm vs program</h4>
<table>
<tr><th>Algorithm</th><th>Program</th></tr>
<tr><td>Step-by-step solution in simple language</td><td>Implementation of the algorithm in a programming language</td></tr>
<tr><td>Independent of language and machine</td><td>Depends on the language (C, Python…)</td></tr>
<tr><td>Written at the design stage</td><td>Written at the implementation stage</td></tr>
<tr><td>Must terminate (finite)</td><td>May run forever (e.g. an OS)</td></tr>
<tr><td>Analysed for time and space</td><td>Tested and executed</td></tr>
</table>""",
          programs=["ds1p1"]),

        T("1.2.2 Characteristics of an Algorithm",
          r"""<p>Every algorithm must have the following five properties (see diagram):</p>
<ol><li><b>Input:</b> it takes <b>zero or more</b> inputs from outside.</li>
<li><b>Output:</b> it produces <b>at least one</b> output (result).</li>
<li><b>Definiteness:</b> each step is <b>clear and unambiguous</b>; it has only one meaning. "Add a few numbers" is not definite; "add A and B" is.</li>
<li><b>Finiteness:</b> the algorithm must <b>terminate after a finite number of steps</b> for every input. A loop with no end condition breaks this rule.</li>
<li><b>Effectiveness:</b> every step must be <b>basic enough</b> to be carried out exactly, in a finite time, using pencil and paper.</li></ol>
<p>Other desirable properties:</p>
<ul><li><b>Correctness:</b> gives the right output for every valid input.</li>
<li><b>Generality:</b> works for all inputs of the problem, not just one case.</li>
<li><b>Efficiency:</b> uses as little time and memory as possible.</li>
<li><b>Language independence:</b> can be coded in any language.</li></ul>""",
          diagram="ds1_characteristics", key=True),

        T("1.2.3 Analysis of an Algorithm: Best, Worst and Average Case",
          r"""<p><b>Analysis of an algorithm</b> means estimating the <b>resources</b> (time and memory) it needs, as a function of the input size <b>n</b>. It helps us choose the best of several algorithms for the same problem.</p>
<h4>Two approaches</h4>
<ul><li><b>A priori analysis</b> (theoretical): done before running, by counting steps. Independent of machine and language. This is what we use.</li>
<li><b>A posteriori analysis</b> (empirical): run the program and measure the actual time. Depends on the machine, compiler and load.</li></ul>
<h4>Three cases</h4>
<p>The running time often depends not only on n but also on the arrangement of the input. Example: linear search for a key in n elements.</p>
<ul><li><b>Best case:</b> the minimum time, for the most favourable input. Key found at the first position → 1 comparison → <b>O(1)</b>.</li>
<li><b>Worst case:</b> the maximum time, for the most unfavourable input. Key at the last position or absent → n comparisons → <b>O(n)</b>.</li>
<li><b>Average case:</b> the expected time over all inputs. Key equally likely anywhere → about (n + 1)/2 comparisons → <b>O(n)</b>.</li></ul>
<p>The <b>worst case</b> is usually the most important, because it gives a guarantee: the algorithm will never take longer than this.</p>""",
          programs=["ds1p8"]),
    ],
}

SEC_1_3 = {
    "title": {"en": "1.3 Time Complexity, Space Complexity and Asymptotic Notations"},
    "items": [
        T("1.3.1 Time Complexity",
          r"""<p>The <b>time complexity</b> of an algorithm is the <b>amount of time it needs to run to completion, expressed as a function of the input size n</b>. We do not measure seconds (they depend on the machine). Instead we count the number of <b>basic operations</b> (comparisons, assignments, additions) executed.</p>
<h4>Frequency count (step count) method</h4>
<p>Count how many times each statement executes, then add them up. Keep only the <b>highest-order term</b> and drop constants to get the Big O.</p>
<p><b>Example 1: sum of an array → O(n)</b></p>
@@fc_sum@@
<p>Total = 1 + (n + 1) + n + 1 = <b>2n + 3</b> → <b>O(n)</b>.</p>
<p><b>Example 2: nested loops → O(n²)</b></p>
@@fc_nested@@
<p><b>Example 3: loop variable doubles → O(log n)</b></p>
@@fc_log@@
<p><b>Example 4: no loop → O(1)</b></p>
@@fc_const@@
<h4>Common complexities (fastest to slowest)</h4>
<table>
<tr><th>Big O</th><th>Name</th><th>Example</th></tr>
<tr><td>O(1)</td><td>Constant</td><td>Access a[i], push/pop</td></tr>
<tr><td>O(log n)</td><td>Logarithmic</td><td>Binary search</td></tr>
<tr><td>O(n)</td><td>Linear</td><td>Linear search, traversal</td></tr>
<tr><td>O(n log n)</td><td>Linearithmic</td><td>Merge sort, quick sort (avg)</td></tr>
<tr><td>O(n²)</td><td>Quadratic</td><td>Bubble, selection, insertion sort</td></tr>
<tr><td>O(2ⁿ)</td><td>Exponential</td><td>Recursive Fibonacci</td></tr>
</table>""",
          diagram="ds1_growth", programs=["ds1p3"], examples=["ds1n6", "ds1n7", "ds1n8"], key=True),

        T("1.3.2 Space Complexity",
          r"""<p>The <b>space complexity</b> of an algorithm is the <b>amount of memory it needs to run to completion</b>, as a function of the input size n.</p>
<p>Space needed S(P) = <b>Fixed part (c)</b> + <b>Variable part (S<sub>p</sub>)</b></p>
<ul><li><b>Fixed part:</b> independent of the input size. Space for the code (instructions), simple variables, constants and fixed-size structures.</li>
<li><b>Variable part:</b> depends on the input size. Space for arrays of size n, dynamically allocated memory, and the <b>recursion stack</b> (each recursive call needs space for its parameters, local variables and return address).</li></ul>
<p><b>Example 1: constant space → O(1)</b></p>
@@space_fixed@@
<p><b>Example 2: space grows with n → O(n)</b></p>
@@space_var@@
<p>The array needs n words; i, s and n need 3 words. S(P) = n + 3 → <b>O(n)</b>.</p>
<h4>Time–space trade-off</h4>
<p>Often we can make an algorithm faster by using more memory, or save memory at the cost of time. Example: a lookup table of pre-computed squares answers in O(1) time but needs O(n) extra space.</p>""",
          examples=["ds1n11"]),

        T("1.3.3 Asymptotic Notations: Big O, Big Omega, Big Theta",
          r"""<p><b>Asymptotic notations</b> are mathematical tools that describe the <b>growth rate</b> of an algorithm's running time when the input size n becomes very large. Constants and lower-order terms are ignored, because for large n only the highest-order term matters.</p>
<h4>1. Big O notation (upper bound)</h4>
<p>f(n) = O(g(n)) if there exist positive constants <b>c</b> and <b>n₀</b> such that</p>
<p style="text-align:center"><b>f(n) ≤ c · g(n)</b> for all n ≥ n₀</p>
<ul><li>g(n) is an <b>upper bound</b>: the algorithm takes <b>at most</b> this much time.</li>
<li>Used to express the <b>worst case</b>. It is the most widely used notation.</li>
<li>Example: 3n + 2 = O(n), because 3n + 2 ≤ 4n for all n ≥ 2 (c = 4, n₀ = 2).</li></ul>
<h4>2. Big Omega (Ω) notation (lower bound)</h4>
<p>f(n) = Ω(g(n)) if there exist positive constants c and n₀ such that</p>
<p style="text-align:center"><b>f(n) ≥ c · g(n)</b> for all n ≥ n₀</p>
<ul><li>g(n) is a <b>lower bound</b>: the algorithm takes <b>at least</b> this much time.</li>
<li>Used to express the <b>best case</b>.</li>
<li>Example: 3n + 2 = Ω(n), because 3n + 2 ≥ 3n for all n ≥ 1 (c = 3, n₀ = 1).</li></ul>
<h4>3. Big Theta (Θ) notation (tight bound)</h4>
<p>f(n) = Θ(g(n)) if there exist positive constants c₁, c₂ and n₀ such that</p>
<p style="text-align:center"><b>c₁ · g(n) ≤ f(n) ≤ c₂ · g(n)</b> for all n ≥ n₀</p>
<ul><li>g(n) is both an upper and a lower bound: an <b>exact</b> (tight) growth rate.</li>
<li>Often used for the <b>average case</b>.</li>
<li>Example: 3n + 2 = Θ(n), because 3n ≤ 3n + 2 ≤ 4n for all n ≥ 2.</li></ul>
<table>
<tr><th>Notation</th><th>Bound</th><th>Meaning</th><th>Case</th></tr>
<tr><td>O</td><td>Upper</td><td>at most</td><td>Worst</td></tr>
<tr><td>Ω</td><td>Lower</td><td>at least</td><td>Best</td></tr>
<tr><td>Θ</td><td>Tight</td><td>exactly</td><td>Average</td></tr>
</table>
<h4>Rules for finding Big O quickly</h4>
<ul><li>Drop constants: O(5n) = O(n).</li>
<li>Keep only the largest term: O(n² + 3n + 7) = O(n²).</li>
<li>Consecutive blocks add: O(n) + O(n²) = O(n²).</li>
<li>Nested blocks multiply: a loop of n inside a loop of n = O(n × n) = O(n²).</li></ul>""",
          diagram="ds1_asymptotic", examples=["ds1n9", "ds1n10"], key=True),
    ],
}

NOTES_A = [SEC_1_1, SEC_1_2, SEC_1_3]
