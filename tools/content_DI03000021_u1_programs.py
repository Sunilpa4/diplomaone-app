"""DI03000021 Unit 1 - solved C programs (complexity and arrays). English only; compiled & run with gcc."""
from c_content import PE

PROGRAMS = [
    PE("ds1p1", "Maximum of 10 numbers using an array (with time complexity) [Practical 1]", r'''
#include <stdio.h>
#define N 10

int main(void)
{
    int a[N], i, max, count = 0;

    printf("Enter %d numbers:\n", N);
    for (i = 0; i < N; i++)
        scanf("%d", &a[i]);

    max = a[0];               // assume first
    for (i = 1; i < N; i++) {
        count++;              // one comparison
        if (a[i] > max)
            max = a[i];
    }

    printf("Maximum = %d\n", max);
    printf("Comparisons = %d\n", count);
    printf("Time complexity = O(n)\n");
    return 0;
}
''', ["12 45 7 89 23 56 34 91 18 60"],
       r"""<ul><li>The first element is taken as the maximum. Each of the remaining <b>n − 1</b> elements is compared once with <code>max</code>.</li>
<li>The counter proves it: for n = 10 there are exactly <b>9 comparisons</b>.</li>
<li>The number of steps grows in direct proportion to n, so the time complexity is <b>O(n)</b> (linear). It is the same in the best, average and worst case, because every element must be checked.</li>
<li>Space complexity: array of n elements + 4 variables → <b>O(n)</b>; extra space apart from the input is O(1).</li></ul>"""),

    PE("ds1p2", "Primitive data types and their sizes", r'''
#include <stdio.h>

int main(void)
{
    int    i = 25;
    float  f = 3.5f;
    double d = 3.14159;
    char   c = 'A';
    int   *p = &i;            // pointer

    printf("Type  B Value\n");  // B = bytes
    printf("int   %zu %d\n", sizeof i, i);
    printf("float %zu %g\n", sizeof f, f);
    printf("dbl   %zu %g\n", sizeof d, d);
    printf("char  %zu %c\n", sizeof c, c);
    printf("ptr   %zu %d\n", sizeof p, *p);
    return 0;
}
''', (),
       r"""<ul><li>These are <b>primitive data structures</b>: the basic types that the machine works on directly. Each holds a <b>single value</b>.</li>
<li>Sizes depend on the compiler and machine. On a 64-bit GCC system an int is 4 bytes, a double 8 bytes and a pointer 8 bytes. On Turbo C (16-bit) an int is 2 bytes.</li>
<li>Non-primitive structures such as arrays, stacks and linked lists are built from these primitive types.</li></ul>"""),

    PE("ds1p3", "Counting steps: O(n), O(n²) and O(log n) loops", r'''
#include <stdio.h>

int main(void)
{
    int sizes[] = {8, 16, 32, 64};
    int k, n, i, j;
    long c1, c2, c3;

    printf("   n  O(n) O(n^2) O(logn)\n");
    for (k = 0; k < 4; k++) {
        n = sizes[k];
        c1 = c2 = c3 = 0;
        for (i = 0; i < n; i++)      // single
            c1++;
        for (i = 0; i < n; i++)      // nested
            for (j = 0; j < n; j++)
                c2++;
        for (i = 1; i < n; i = i * 2) // doubling
            c3++;
        printf("%4d %5ld %6ld %7ld\n",
               n, c1, c2, c3);
    }
    return 0;
}
''', (),
       r"""<ul><li><b>Single loop:</b> the body runs n times → <b>O(n)</b>. Doubling n doubles the count.</li>
<li><b>Nested loop:</b> n × n runs → <b>O(n²)</b>. Doubling n makes the count <b>four times</b> bigger (64 → 256 → 1024 → 4096).</li>
<li><b>Doubling loop</b> (<code>i = i * 2</code>): i takes the values 1, 2, 4, 8 … so it runs log₂n times → <b>O(log n)</b>. Even for n = 64 it runs only 6 times.</li>
<li>This is exactly how the <b>frequency count</b> method finds time complexity: count how many times the key statement executes as a function of n.</li></ul>"""),

    PE("ds1p4", "Traversing an array with addresses (contiguous memory)", r'''
#include <stdio.h>

int main(void)
{
    int a[6] = {15, 7, 42, 9, 23, 31};
    int i, n = 6, sum = 0;
    long off;

    printf("Index Value Offset\n");
    for (i = 0; i < n; i++) {  // traverse
        off = (char *)&a[i] - (char *)a;
        printf("a[%d] %5d %5ld\n",
               i, a[i], off);
        sum += a[i];
    }
    printf("Sum = %d\n", sum);
    printf("a[i] at base + %zu * i\n",
           sizeof a[0]);
    return 0;
}
''', (),
       r"""<ul><li><b>Traversing</b> means visiting every element exactly once. Here each element is printed and added to <code>sum</code>.</li>
<li>The offset column shows the distance of each element from the start of the array. It goes up by <b>4 bytes</b> (the size of an int), which proves the elements are stored in <b>contiguous</b> (side-by-side) memory.</li>
<li>So the address of a[i] = base address + 4 × i. This is the formula LOC(A[i]) = Base + w × (i − LB) with LB = 0.</li>
<li>(Real addresses change on every run, so only the offsets are printed.) Time complexity of traversal: <b>O(n)</b>.</li></ul>"""),

    PE("ds1p5", "Insert an element at a given position", r'''
#include <stdio.h>
#define MAX 20

int main(void)
{
    int a[MAX], n, i, pos, item;

    printf("Enter number of elements: ");
    scanf("%d", &n);
    printf("Enter %d elements: ", n);
    for (i = 0; i < n; i++)
        scanf("%d", &a[i]);
    printf("Position (1-%d): ", n + 1);
    scanf("%d", &pos);
    printf("Enter element to insert: ");
    scanf("%d", &item);

    if (n == MAX || pos < 1 || pos > n+1) {
        printf("Insertion not possible\n");
        return 0;
    }
    for (i = n - 1; i >= pos - 1; i--)
        a[i + 1] = a[i];   // shift right
    a[pos - 1] = item;
    n++;

    printf("Array after insertion: ");
    for (i = 0; i < n; i++)
        printf("%d ", a[i]);
    printf("\n");
    return 0;
}
''', ["5", "10 20 30 40 50", "3", "25"],
       r"""<ul><li>The user gives the position from 1, so the array index is <code>pos − 1</code>.</li>
<li>Elements from the <b>last one down to index pos − 1</b> are shifted one place right. The loop must run from the end; shifting from the front would overwrite values.</li>
<li>The new item is then placed in the free slot and <code>n</code> is increased by 1.</li>
<li>The check <code>n == MAX</code> prevents <b>overflow</b> (no free space).</li>
<li>Complexity: best case O(1) (insert at the end), worst case <b>O(n)</b> (insert at the beginning, all n elements shift).</li></ul>"""),

    PE("ds1p6", "Delete an element from a given position", r'''
#include <stdio.h>

int main(void)
{
    int a[20], n, i, pos, item;

    printf("Enter number of elements: ");
    scanf("%d", &n);
    printf("Enter %d elements: ", n);
    for (i = 0; i < n; i++)
        scanf("%d", &a[i]);
    printf("Delete position (1-%d): ", n);
    scanf("%d", &pos);

    if (n == 0 || pos < 1 || pos > n) {
        printf("Deletion not possible\n");
        return 0;
    }
    item = a[pos - 1];
    for (i = pos - 1; i < n - 1; i++)
        a[i] = a[i + 1];      // shift left
    n--;

    printf("Deleted element = %d\n", item);
    printf("Array after deletion: ");
    for (i = 0; i < n; i++)
        printf("%d ", a[i]);
    printf("\n");
    return 0;
}
''', ["6", "10 20 25 30 40 50", "2"],
       r"""<ul><li>The element at index <code>pos − 1</code> is saved in <code>item</code>, so it can be reported.</li>
<li>All elements <b>after</b> it move one place left, starting from the front. This closes the gap.</li>
<li><code>n</code> is reduced by 1. The old last slot still holds a value, but it is no longer part of the array.</li>
<li><code>n == 0</code> means the array is empty (<b>underflow</b>).</li>
<li>Complexity: best case O(1) (delete the last element), worst case <b>O(n)</b> (delete the first element).</li></ul>"""),

    PE("ds1p7", "Update (replace) a value in an array", r'''
#include <stdio.h>

int main(void)
{
    int a[] = {10, 20, 30, 40, 50};
    int n = 5, i, old, new, found = 0;

    printf("Array: ");
    for (i = 0; i < n; i++)
        printf("%d ", a[i]);
    printf("\nEnter value to update: ");
    scanf("%d", &old);
    printf("Enter new value: ");
    scanf("%d", &new);

    for (i = 0; i < n; i++) {
        if (a[i] == old) {
            a[i] = new;       // update
            found = 1;
            printf("Updated a[%d]\n", i);
            break;
        }
    }
    if (!found)
        printf("%d not found\n", old);

    printf("Array: ");
    for (i = 0; i < n; i++)
        printf("%d ", a[i]);
    printf("\n");
    return 0;
}
''', ["30", "35"],
       r"""<ul><li><b>Update</b> changes the value of an existing element. No shifting is needed, so the array size stays the same.</li>
<li>If the <b>index</b> is known, the update is a single statement <code>a[i] = new;</code> → <b>O(1)</b>.</li>
<li>If only the <b>value</b> is known (as here), it must first be searched → <b>O(n)</b> in the worst case.</li></ul>"""),

    PE("ds1p8", "Linear search in an array", r'''
#include <stdio.h>

int main(void)
{
    int a[] = {34, 12, 78, 45, 90, 23, 56};
    int n = 7, i, key, comp = 0;

    printf("Enter element to search: ");
    scanf("%d", &key);

    for (i = 0; i < n; i++) {
        comp++;
        if (a[i] == key)
            break;
    }
    if (i < n)
        printf("%d found at position %d\n",
               key, i + 1);
    else
        printf("%d not found\n", key);
    printf("Comparisons = %d\n", comp);
    return 0;
}
''', ["90"],
       r"""<ul><li>Linear search compares the key with each element <b>one by one</b>, from the first element onwards.</li>
<li>The search stops at the first match. If the loop ends with <code>i == n</code>, the key is not present.</li>
<li>Here 90 is the 5th element, so 5 comparisons are needed.</li>
<li><b>Best case</b> O(1): the key is the first element. <b>Worst case</b> O(n): the key is the last element or absent. <b>Average</b> ≈ n/2 comparisons → O(n).</li>
<li>It works on <b>unsorted</b> arrays too. Binary search (Unit 5) is faster but needs a sorted array.</li></ul>"""),

    PE("ds1p9", "Insert a value into a sorted array (keeps order)", r'''
#include <stdio.h>

int main(void)
{
    int a[20] = {5, 12, 18, 27, 33, 41};
    int n = 6, i, item;

    printf("Sorted array: ");
    for (i = 0; i < n; i++)
        printf("%d ", a[i]);
    printf("\nEnter value to insert: ");
    scanf("%d", &item);

    i = n - 1;
    while (i >= 0 && a[i] > item) {
        a[i + 1] = a[i];      // shift bigger
        i--;
    }
    a[i + 1] = item;
    n++;

    printf("New array: ");
    for (i = 0; i < n; i++)
        printf("%d ", a[i]);
    printf("\n");
    return 0;
}
''', ["20"],
       r"""<ul><li>The position does not need to be given. Starting from the end, every element <b>bigger</b> than the new item is shifted one place right.</li>
<li>When a smaller (or equal) element is found, or the start is reached, the item goes into the gap at <code>i + 1</code>.</li>
<li>The array stays sorted after insertion. This same idea is the heart of <b>insertion sort</b> (Unit 5).</li>
<li>Worst case O(n), when the new item is the smallest.</li></ul>"""),

    PE("ds1p10", "Row major and column major order of a matrix", r'''
#include <stdio.h>
#define M 2
#define N 3

int main(void)
{
    int a[M][N] = {{1, 2, 3}, {4, 5, 6}};
    int i, j, *p = &a[0][0];

    printf("Matrix:\n");
    for (i = 0; i < M; i++) {
        for (j = 0; j < N; j++)
            printf("%3d", a[i][j]);
        printf("\n");
    }
    printf("Memory order in C: ");
    for (i = 0; i < M * N; i++)
        printf("%d ", p[i]);
    printf("\nRow major order   : ");
    for (i = 0; i < M; i++)
        for (j = 0; j < N; j++)
            printf("%d ", a[i][j]);
    printf("\nColumn major order: ");
    for (j = 0; j < N; j++)
        for (i = 0; i < M; i++)
            printf("%d ", a[i][j]);
    printf("\n");
    return 0;
}
''', (),
       r"""<ul><li>A 2-D array is a table, but memory is a single line of bytes, so the table must be <b>linearised</b>.</li>
<li>Reading memory directly through a pointer (<code>p[0]</code> … <code>p[5]</code>) gives 1 2 3 4 5 6: <b>C stores arrays in row major order</b> (row 0 first, then row 1).</li>
<li><b>Row major</b>: outer loop on rows, inner loop on columns. <b>Column major</b>: outer loop on columns, inner loop on rows → 1 4 2 5 3 6 (used by FORTRAN and MATLAB).</li></ul>"""),

    PE("ds1p11", "Address calculation: 1-D, row major and column major", r'''
#include <stdio.h>

int main(void)
{
    long base, w, lb, lr, lc, m, n, i, j;

    printf("1-D: base w LB i: ");
    scanf("%ld %ld %ld %ld",
          &base, &w, &lb, &i);
    printf("A[%ld] = %ld\n", i,
           base + w * (i - lb));

    printf("2-D: base w LR LC M N: ");
    scanf("%ld %ld %ld %ld %ld %ld",
          &base, &w, &lr, &lc, &m, &n);
    printf("Find A[i][j], enter i j: ");
    scanf("%ld %ld", &i, &j);

    printf("Row major    = %ld\n",
           base + w*((i-lr)*n + (j-lc)));
    printf("Column major = %ld\n",
           base + w*((j-lc)*m + (i-lr)));
    return 0;
}
''', ["2000 2 0 23", "1000 4 1 1 4 5", "3 4"],
       r"""<ul><li><b>1-D:</b> LOC(A[i]) = Base + w × (i − LB). For base 2000, w = 2, LB = 0, i = 23 → 2000 + 46 = <b>2046</b>.</li>
<li><b>2-D:</b> array A[1..4][1..5] (M = 4 rows, N = 5 columns), base 1000, w = 4, find A[3][4]:
<br>Row major = 1000 + 4 × [(3−1) × 5 + (4−1)] = 1000 + 4 × 13 = <b>1052</b>
<br>Column major = 1000 + 4 × [(4−1) × 4 + (3−1)] = 1000 + 4 × 14 = <b>1056</b></li>
<li>In row major, the number of <b>columns N</b> is used (whole rows are skipped). In column major, the number of <b>rows M</b> is used (whole columns are skipped).</li></ul>"""),

    PE("ds1p12", "Reverse an array in place", r'''
#include <stdio.h>

int main(void)
{
    int a[] = {1, 2, 3, 4, 5, 6, 7};
    int n = 7, i, t;

    printf("Original: ");
    for (i = 0; i < n; i++)
        printf("%d ", a[i]);

    for (i = 0; i < n / 2; i++) {
        t = a[i];                 // swap ends
        a[i] = a[n - 1 - i];
        a[n - 1 - i] = t;
    }

    printf("\nReversed: ");
    for (i = 0; i < n; i++)
        printf("%d ", a[i]);
    printf("\n");
    return 0;
}
''', (),
       r"""<ul><li>The first and last elements are swapped, then the second and second-last, and so on, until the middle is reached.</li>
<li>Only <b>n / 2</b> swaps are needed (3 swaps for 7 elements; the middle element stays in place).</li>
<li>Time complexity <b>O(n)</b>. Only one extra variable <code>t</code> is used, so the extra space is <b>O(1)</b>. This is called an <b>in-place</b> algorithm.</li></ul>"""),

    PE("ds1p13", "Largest and second largest in one traversal", r'''
#include <stdio.h>
#include <limits.h>

int main(void)
{
    int a[] = {45, 89, 12, 89, 67, 34, 78};
    int n = 7, i, first, second;

    first = second = INT_MIN;
    for (i = 0; i < n; i++) {
        if (a[i] > first) {
            second = first;
            first = a[i];
        } else if (a[i] > second
                   && a[i] != first) {
            second = a[i];
        }
    }
    printf("Largest = %d\n", first);
    printf("Second = %d\n", second);
    return 0;
}
''', (),
       r"""<ul><li>Sorting first would cost O(n log n) or O(n²). A single traversal does the job in <b>O(n)</b>, a better algorithm for the same problem.</li>
<li>When a new largest is found, the old largest moves down to <code>second</code>.</li>
<li><code>a[i] != first</code> skips duplicates of the largest (89 appears twice), so the answer is 78 and not 89.</li>
<li><code>INT_MIN</code> (from limits.h) is the smallest int, a safe starting value.</li></ul>"""),

    PE("ds1p14", "Menu-driven program for array operations", r'''
#include <stdio.h>
#define MAX 10

int a[MAX], n = 0;

void display(void)
{
    int i;
    printf("Array: ");
    for (i = 0; i < n; i++)
        printf("%d ", a[i]);
    printf("\n");
}

void insert(int pos, int item)
{
    int i;
    if (n == MAX || pos < 1 || pos > n+1) {
        printf("Invalid insert\n");
        return;
    }
    for (i = n - 1; i >= pos - 1; i--)
        a[i + 1] = a[i];
    a[pos - 1] = item;
    n++;
}

void delete(int pos)
{
    int i;
    if (pos < 1 || pos > n) {
        printf("Invalid delete\n");
        return;
    }
    for (i = pos - 1; i < n - 1; i++)
        a[i] = a[i + 1];
    n--;
}

int search(int key)
{
    int i;
    for (i = 0; i < n; i++)
        if (a[i] == key)
            return i + 1;
    return -1;
}

int main(void)
{
    int ch, pos, item;
    do {
        puts("1.Insert 2.Delete 3.Search");
        puts("4.Display 5.Exit");
        printf("Choice: ");
        scanf("%d", &ch);
        switch (ch) {
        case 1:
            printf("Position and item: ");
            scanf("%d %d", &pos, &item);
            insert(pos, item);
            break;
        case 2:
            printf("Position: ");
            scanf("%d", &pos);
            delete(pos);
            break;
        case 3:
            printf("Key: ");
            scanf("%d", &item);
            pos = search(item);
            printf("Position = %d\n", pos);
            break;
        case 4:
            display();
            break;
        }
    } while (ch != 5);
    return 0;
}
''', ["1", "1 10", "1", "2 30", "1", "2 20", "4", "3", "30", "2", "1", "4", "5"],
       r"""<ul><li>Each operation is a separate function working on the <b>global</b> array <code>a</code> and its count <code>n</code>.</li>
<li>Sequence used: insert 10 at 1 → [10]; insert 30 at 2 → [10 30]; insert 20 at 2 → [10 20 30]; search 30 → position 3; delete position 1 → [20 30].</li>
<li><code>search()</code> returns <b>−1</b> when the key is absent.</li>
<li>This menu-driven style (do-while + switch) is used for the stack, queue and linked list programs in the next units too.</li></ul>"""),
]
