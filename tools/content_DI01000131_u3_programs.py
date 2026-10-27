"""DI01000131 Unit 3 - solved C programs (arrays, pointers). English only; compiled & run with gcc."""
from c_content import PE

PROGRAMS = [
    PE("c3p1", "Read N elements, print them with sum and average", r'''
#include <stdio.h>

int main(void)
{
    int a[50], n, i, sum = 0;
    float avg;

    printf("How many elements? ");
    scanf("%d", &n);

    printf("Enter %d elements: ", n);
    for (i = 0; i < n; i++)         // run-time initialization
        scanf("%d", &a[i]);

    for (i = 0; i < n; i++)
        sum = sum + a[i];
    avg = (float) sum / n;

    printf("Elements: ");
    for (i = 0; i < n; i++)
        printf("%d ", a[i]);
    printf("\nSum = %d\nAverage = %.2f\n", sum, avg);
    return 0;
}
''', ["5", "12 45 7 23 56"],
       r"""<ul><li><code>int a[50]</code> reserves space for up to 50 integers; only the first <code>n</code> are used.</li>
<li>The elements are read at <b>run time</b> with a for loop. <code>&amp;a[i]</code> is the address of the i-th element.</li>
<li>Index runs from <code>0</code> to <code>n-1</code>, so the loop condition is <code>i &lt; n</code>.</li>
<li><code>(float) sum / n</code> avoids integer division: 143 / 5 = 28.60.</li></ul>"""),

    PE("c3p2", "Largest and smallest element of an array", r'''
#include <stdio.h>

int main(void)
{
    int a[50], n, i, max, min;

    printf("How many elements? ");
    scanf("%d", &n);
    printf("Enter %d elements: ", n);
    for (i = 0; i < n; i++)
        scanf("%d", &a[i]);

    max = min = a[0];               // assume first is max and min
    for (i = 1; i < n; i++)
    {
        if (a[i] > max)
            max = a[i];
        if (a[i] < min)
            min = a[i];
    }
    printf("Largest = %d\nSmallest = %d\n", max, min);
    return 0;
}
''', ["6", "34 -8 91 17 0 56"],
       r"""<p>The first element is taken as both the largest and the smallest. Every other element is then compared with them and replaces them if it is bigger or smaller. Starting with <code>a[0]</code> instead of 0 makes the program work for negative numbers as well.</p>"""),

    PE("c3p3", "Linear search", r'''
#include <stdio.h>

int main(void)
{
    int a[50], n, i, key, pos = -1;

    printf("How many elements? ");
    scanf("%d", &n);
    printf("Enter %d elements: ", n);
    for (i = 0; i < n; i++)
        scanf("%d", &a[i]);

    printf("Enter element to search: ");
    scanf("%d", &key);

    for (i = 0; i < n; i++)
    {
        if (a[i] == key)
        {
            pos = i;
            break;                  // stop at first match
        }
    }

    if (pos != -1)
        printf("%d found at index %d (position %d)\n", key, pos, pos + 1);
    else
        printf("%d not found\n", key);
    return 0;
}
''', ["6", "15 42 8 23 4 16", "23"],
       r"""<p><b>Linear (sequential) search</b> compares the key with each element, starting at index 0, until a match is found or the array ends (see flowchart).</p>
<ul><li><code>pos = -1</code> means "not found yet"; -1 can never be a valid index.</li>
<li>Index 3 is the <b>4th position</b>, because indexing starts at 0.</li>
<li>Worst case: n comparisons. It works on unsorted arrays.</li></ul>"""),

    PE("c3p4", "Bubble sort (ascending order)", r'''
#include <stdio.h>

int main(void)
{
    int a[50], n, i, j, temp;

    printf("How many elements? ");
    scanf("%d", &n);
    printf("Enter %d elements: ", n);
    for (i = 0; i < n; i++)
        scanf("%d", &a[i]);

    for (i = 0; i < n - 1; i++)             // passes
    {
        for (j = 0; j < n - 1 - i; j++)     // comparisons
        {
            if (a[j] > a[j + 1])            // swap if out of order
            {
                temp = a[j];
                a[j] = a[j + 1];
                a[j + 1] = temp;
            }
        }
    }

    printf("Sorted array: ");
    for (i = 0; i < n; i++)
        printf("%d ", a[i]);
    printf("\n");
    return 0;
}
''', ["5", "50 20 40 10 30"],
       r"""<ul><li>The outer loop makes <code>n-1</code> <b>passes</b>. In each pass the inner loop compares <b>adjacent</b> elements and swaps them if they are in the wrong order.</li>
<li>After pass 1 the largest element is at the end, so each later pass checks one element fewer (<code>n - 1 - i</code>).</li>
<li>The diagram "Bubble Sort – Pass by Pass" traces this exact input.</li>
<li>For <b>descending</b> order, change <code>&gt;</code> to <code>&lt;</code>.</li></ul>"""),

    PE("c3p5", "Reverse the elements of an array (in place)", r'''
#include <stdio.h>

int main(void)
{
    int a[] = {11, 22, 33, 44, 55, 66};
    int n = sizeof(a) / sizeof(a[0]);       // number of elements
    int i, temp;

    for (i = 0; i < n / 2; i++)
    {
        temp = a[i];                        // swap first and last
        a[i] = a[n - 1 - i];
        a[n - 1 - i] = temp;
    }

    printf("Reversed: ");
    for (i = 0; i < n; i++)
        printf("%d ", a[i]);
    printf("\n");
    return 0;
}
''', (),
       r"""<ul><li><b>Compile-time initialization</b> with the size omitted: the compiler counts 6 values and makes <code>a[6]</code>.</li>
<li><code>sizeof(a) / sizeof(a[0])</code> = 24 / 4 = 6 gives the number of elements.</li>
<li>Element <code>i</code> is swapped with element <code>n-1-i</code>. Only <code>n/2</code> swaps are needed; going further would reverse the array back.</li></ul>"""),

    PE("c3p6", "Insert an element at a given position", r'''
#include <stdio.h>

int main(void)
{
    int a[50] = {10, 20, 30, 40, 50};
    int n = 5, i, pos, item;

    printf("Enter element and position (1 to %d): ", n + 1);
    scanf("%d %d", &item, &pos);

    if (pos < 1 || pos > n + 1)
    {
        printf("Invalid position\n");
        return 1;
    }

    for (i = n - 1; i >= pos - 1; i--)      // shift right
        a[i + 1] = a[i];
    a[pos - 1] = item;
    n++;

    printf("Array after insertion: ");
    for (i = 0; i < n; i++)
        printf("%d ", a[i]);
    printf("\n");
    return 0;
}
''', ["25 3"],
       r"""<p>An array has a fixed size and its elements are contiguous, so to insert in the middle, the elements from the end down to the position are <b>shifted one place to the right</b>. The shift starts from the <b>last</b> element so that no value is overwritten. Position 3 means index 2.</p>"""),

    PE("c3p7", "Read and display a matrix (2-D array)", r'''
#include <stdio.h>

int main(void)
{
    int m[10][10], r, c, i, j;
    int t[2][3] = { {1, 2, 3},
                    {4, 5, 6} };            // compile-time

    printf("Initialized matrix t:\n");
    for (i = 0; i < 2; i++)
    {
        for (j = 0; j < 3; j++)
            printf("%4d", t[i][j]);
        printf("\n");
    }

    printf("Enter rows and columns: ");
    scanf("%d %d", &r, &c);
    printf("Enter %d elements row-wise:\n", r * c);
    for (i = 0; i < r; i++)                 // run-time
        for (j = 0; j < c; j++)
            scanf("%d", &m[i][j]);

    printf("Matrix m:\n");
    for (i = 0; i < r; i++)
    {
        for (j = 0; j < c; j++)
            printf("%4d", m[i][j]);
        printf("\n");
    }
    return 0;
}
''', ["3 3", "1 0 2", "4 5 6", "7 8 9"],
       r"""<ul><li>A 2-D array is processed with <b>nested loops</b>: the outer loop selects the row <code>i</code>, the inner loop the column <code>j</code>.</li>
<li><code>%4d</code> gives each number a width of 4, so the columns line up.</li>
<li><code>printf("\n")</code> after the inner loop starts a new row.</li></ul>"""),

    PE("c3p8", "Addition of two matrices", r'''
#include <stdio.h>

int main(void)
{
    int a[10][10], b[10][10], s[10][10], r, c, i, j;

    printf("Enter rows and columns: ");
    scanf("%d %d", &r, &c);

    printf("Enter matrix A:\n");
    for (i = 0; i < r; i++)
        for (j = 0; j < c; j++)
            scanf("%d", &a[i][j]);

    printf("Enter matrix B:\n");
    for (i = 0; i < r; i++)
        for (j = 0; j < c; j++)
            scanf("%d", &b[i][j]);

    for (i = 0; i < r; i++)
        for (j = 0; j < c; j++)
            s[i][j] = a[i][j] + b[i][j];

    printf("Sum matrix:\n");
    for (i = 0; i < r; i++)
    {
        for (j = 0; j < c; j++)
            printf("%4d", s[i][j]);
        printf("\n");
    }
    return 0;
}
''', ["2 3", "1 2 3", "4 5 6", "6 5 4", "3 2 1"],
       r"""<p>Matrices can be added only if they have the <b>same order</b> (rows × columns). Each element of the result is <code>s[i][j] = a[i][j] + b[i][j]</code>. For subtraction, change + to −.</p>"""),

    PE("c3p9", "Multiplication of two matrices", r'''
#include <stdio.h>

int main(void)
{
    int a[10][10], b[10][10], c[10][10];
    int m, n, p, q, i, j, k;

    printf("Enter rows and columns of A: ");
    scanf("%d %d", &m, &n);
    printf("Enter rows and columns of B: ");
    scanf("%d %d", &p, &q);

    if (n != p)
    {
        printf("Multiplication not possible\n");
        return 1;
    }

    printf("Enter matrix A:\n");
    for (i = 0; i < m; i++)
        for (j = 0; j < n; j++)
            scanf("%d", &a[i][j]);
    printf("Enter matrix B:\n");
    for (i = 0; i < p; i++)
        for (j = 0; j < q; j++)
            scanf("%d", &b[i][j]);

    for (i = 0; i < m; i++)
        for (j = 0; j < q; j++)
        {
            c[i][j] = 0;
            for (k = 0; k < n; k++)         // row of A x column of B
                c[i][j] += a[i][k] * b[k][j];
        }

    printf("Product matrix:\n");
    for (i = 0; i < m; i++)
    {
        for (j = 0; j < q; j++)
            printf("%5d", c[i][j]);
        printf("\n");
    }
    return 0;
}
''', ["2 2", "2 2", "1 2", "3 4", "5 6", "7 8"],
       r"""<ul><li>Condition: <b>columns of A = rows of B</b> (n = p). The result has order m × q.</li>
<li>Each element <code>c[i][j]</code> is the sum of the products of row i of A and column j of B, so a <b>third loop</b> (k) is needed.</li>
<li><code>c[i][j]</code> must be set to 0 before adding the products.</li>
<li>See the diagram "Matrix Multiplication": C[0][0] = 1×5 + 2×7 = 19.</li></ul>"""),

    PE("c3p10", "Transpose of a matrix", r'''
#include <stdio.h>

int main(void)
{
    int a[3][4] = { {1, 2, 3, 4},
                    {5, 6, 7, 8},
                    {9, 10, 11, 12} };
    int t[4][3], i, j;

    for (i = 0; i < 3; i++)
        for (j = 0; j < 4; j++)
            t[j][i] = a[i][j];              // rows become columns

    printf("Transpose (4 x 3):\n");
    for (i = 0; i < 4; i++)
    {
        for (j = 0; j < 3; j++)
            printf("%4d", t[i][j]);
        printf("\n");
    }
    return 0;
}
''', (),
       r"""<p>In the <b>transpose</b> the rows become columns: <code>t[j][i] = a[i][j]</code>. A 3 × 4 matrix gives a 4 × 3 transpose, so a separate array <code>t</code> of the opposite order is used.</p>"""),

    PE("c3p11", "Sum of diagonal elements and row sums of a square matrix", r'''
#include <stdio.h>

int main(void)
{
    int a[3][3] = { {4, 1, 2},
                    {3, 5, 7},
                    {6, 8, 9} };
    int i, j, diag = 0, rsum;

    for (i = 0; i < 3; i++)
    {
        rsum = 0;
        for (j = 0; j < 3; j++)
        {
            rsum += a[i][j];
            if (i == j)                     // main diagonal
                diag += a[i][j];
        }
        printf("Sum of row %d = %d\n", i, rsum);
    }
    printf("Sum of main diagonal = %d\n", diag);
    return 0;
}
''', (),
       r"""<p>The elements of the <b>main diagonal</b> have equal row and column index (<code>i == j</code>): 4 + 5 + 9 = 18. The row sum is reset to 0 at the start of each row. (Secondary diagonal: <code>i + j == n - 1</code>.)</p>"""),

    PE("c3p12", "Pointer basics: & and * operators", r'''
#include <stdio.h>

int main(void)
{
    int x = 25;
    int *p;                 // pointer declaration
    p = &x;                 // p stores address of x

    printf("Value of x      = %d\n", x);
    printf("Address of x    = %p\n", (void *) &x);
    printf("Value of p      = %p\n", (void *) p);
    printf("Value at *p     = %d\n", *p);
    printf("Address of p    = %p\n", (void *) &p);

    *p = 40;                // change x through the pointer
    printf("After *p = 40, x = %d\n", x);

    printf("sizeof(p) = %zu bytes\n", sizeof(p));
    return 0;
}
''', (),
       r"""<ul><li><code>&amp;x</code> (address-of operator) gives the memory address of x. It is stored in pointer <code>p</code>.</li>
<li><code>*p</code> (indirection / dereference operator) gives the <b>value at</b> that address, i.e. 25.</li>
<li><code>*p = 40;</code> changes x itself, because p points to x.</li>
<li><code>%p</code> prints an address in hexadecimal. <b>The addresses differ on every computer and run.</b></li>
<li>On a 64-bit system every pointer is 8 bytes, whatever type it points to.</li></ul>"""),

    PE("c3p13", "Swap two numbers using pointers", r'''
#include <stdio.h>

int main(void)
{
    int a, b, temp;
    int *pa = &a, *pb = &b;         // declare and initialize

    printf("Enter two numbers: ");
    scanf("%d %d", pa, pb);         // pa already holds &a

    temp = *pa;
    *pa = *pb;
    *pb = temp;

    printf("After swap: a = %d, b = %d\n", a, b);
    return 0;
}
''', ["15 40"],
       r"""<ul><li><code>int *pa = &amp;a;</code> declares and initializes a pointer in one statement.</li>
<li><code>scanf("%d", pa)</code> needs no &amp;, because <code>pa</code> already contains the address of a.</li>
<li>The swap is done through <code>*pa</code> and <code>*pb</code>, so the original variables a and b change. This idea is used in Unit 4 for <b>call by reference</b>.</li></ul>"""),

    PE("c3p14", "Access array elements using a pointer", r'''
#include <stdio.h>

int main(void)
{
    int a[5] = {10, 20, 30, 40, 50};
    int *p = a;                     // same as p = &a[0]
    int i, sum = 0;

    for (i = 0; i < 5; i++)
    {
        printf("*(p + %d) = %d\n", i, *(p + i));
        sum += *(p + i);
    }
    printf("Sum = %d\n", sum);

    p = &a[2];
    printf("*p = %d, *(p + 1) = %d, *(p - 1) = %d\n", *p, *(p + 1), *(p - 1));
    printf("p + 1 - p = %d element(s)\n", (int) ((p + 1) - p));
    return 0;
}
''', (),
       r"""<ul><li>The array name <code>a</code> is the address of its first element, so <code>p = a</code> is valid.</li>
<li><b>Pointer arithmetic:</b> <code>p + i</code> points to the i-th element after p. The address increases by <code>i × sizeof(int)</code>, not by i bytes.</li>
<li><code>*(p + i)</code> is the same as <code>a[i]</code> and <code>p[i]</code>.</li>
<li>Subtracting two pointers gives the number of elements between them.</li></ul>"""),

    PE("c3p15", "void (generic) pointer", r'''
#include <stdio.h>

int main(void)
{
    int i = 10;
    float f = 2.5f;
    char c = 'A';
    void *vp;                       // generic pointer

    vp = &i;
    printf("int   value = %d\n", *(int *) vp);      // cast, then *
    vp = &f;
    printf("float value = %.1f\n", *(float *) vp);
    vp = &c;
    printf("char  value = %c\n", *(char *) vp);
    return 0;
}
''', (),
       r"""<ul><li>A <b>void pointer</b> can store the address of a variable of <b>any</b> data type.</li>
<li>It cannot be dereferenced directly (the compiler does not know the size of the data), so it must first be <b>type-cast</b>: <code>*(int *) vp</code>.</li>
<li>Pointer arithmetic is not allowed on void pointers in standard C.</li>
<li>Library functions such as <code>malloc()</code> return <code>void *</code>.</li></ul>"""),

    PE("c3p16", "NULL pointer – safe use", r'''
#include <stdio.h>

int main(void)
{
    int x = 7;
    int *p = NULL;                  // points nowhere yet

    if (p == NULL)
        printf("p is NULL - not dereferenced\n");

    p = &x;
    if (p != NULL)
        printf("p points to x, *p = %d\n", *p);

    p = NULL;                       // reset after use
    printf("p reset to NULL: %s\n", p ? "not null" : "null");
    return 0;
}
''', (),
       r"""<ul><li>A <b>NULL pointer</b> holds the value <code>NULL</code> (0), meaning it points to no valid memory.</li>
<li>Initializing a pointer to NULL avoids a <b>wild pointer</b> (an uninitialized pointer holding a garbage address).</li>
<li>Always check <code>if (p != NULL)</code> before using <code>*p</code>. Dereferencing NULL crashes the program (segmentation fault).</li>
<li>In a condition, a NULL pointer is <b>false</b>, so <code>p ? … : …</code> works.</li></ul>"""),
]

if __name__ == "__main__":
    for p in PROGRAMS:
        print("=" * 20, p["id"], p["title"]["en"]); print(p["out"])
