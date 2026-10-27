"""DI03000021 Unit 5 - solved C programs (sorting, searching, hashing). gcc-verified; arrays same as ds_sort traces."""
from c_content import PE

PROGRAMS = [
    PE("ds5p1", "Bubble sort with pass-by-pass output [Practical 11]", r'''
#include <stdio.h>

void show(int a[], int n)
{
    int i;
    for (i = 0; i < n; i++)
        printf("%d ", a[i]);
    printf("\n");
}

int main(void)
{
    int a[20], n, i, j, t, swapped;

    scanf("%d", &n);
    for (i = 0; i < n; i++)
        scanf("%d", &a[i]);

    for (i = 0; i < n - 1; i++) {
        swapped = 0;
        for (j = 0; j < n - 1 - i; j++) {
            if (a[j] > a[j + 1]) {
                t = a[j];
                a[j] = a[j + 1];
                a[j + 1] = t;
                swapped = 1;
            }
        }
        printf("Pass %d: ", i + 1);
        show(a, n);
        if (swapped == 0)
            break;          /* already sorted */
    }
    printf("Sorted: ");
    show(a, n);
    return 0;
}
''', ("6", "45 12 78 34 23 56"),
       r"""<ul><li>Adjacent elements are compared, and swapped if the left one is bigger. After pass 1 the largest value (78) is at the end.</li>
<li>The inner loop runs <code>n − 1 − i</code> times, because the last i elements are already in place.</li>
<li>The <code>swapped</code> flag stops the sort early: pass 4 makes no swap, so the array is already sorted and pass 5 is skipped.</li></ul>"""),

    PE("ds5p2", "Bubble sort: count comparisons and swaps", r'''
#include <stdio.h>

void bubble(int a[], int n)
{
    int i, j, t, comp = 0, swp = 0, flag;
    for (i = 0; i < n - 1; i++) {
        flag = 0;
        for (j = 0; j < n - 1 - i; j++) {
            comp++;
            if (a[j] > a[j + 1]) {
                t = a[j];
                a[j] = a[j + 1];
                a[j + 1] = t;
                swp++;
                flag = 1;
            }
        }
        if (!flag) break;
    }
    printf("comp = %2d, swaps = %2d\n",
           comp, swp);
}

int main(void)
{
    int s[6] = {12, 23, 34, 45, 56, 78};
    int r[6] = {78, 56, 45, 34, 23, 12};
    int m[6] = {45, 12, 78, 34, 23, 56};
    printf("Sorted : ");
    bubble(s, 6);
    printf("Reverse: ");
    bubble(r, 6);
    printf("Random : ");
    bubble(m, 6);
    return 0;
}
''', (),
       r"""<ul><li><b>Best case</b> (already sorted): one pass, n − 1 = 5 comparisons, 0 swaps → O(n).</li>
<li><b>Worst case</b> (reverse order): n(n − 1)/2 = 15 comparisons and 15 swaps → O(n²).</li>
<li>The random input needs 14 comparisons and 7 swaps.</li></ul>"""),

    PE("ds5p3", "Selection sort with pass-by-pass output [Practical 12]", r'''
#include <stdio.h>

void show(int a[], int n)
{
    int i;
    for (i = 0; i < n; i++)
        printf("%d ", a[i]);
    printf("\n");
}

int main(void)
{
    int a[20], n, i, j, min, t;

    scanf("%d", &n);
    for (i = 0; i < n; i++)
        scanf("%d", &a[i]);

    for (i = 0; i < n - 1; i++) {
        min = i;
        for (j = i + 1; j < n; j++)
            if (a[j] < a[min])
                min = j;
        if (min != i) {
            t = a[i];
            a[i] = a[min];
            a[min] = t;
        }
        printf("Pass %d (min %d): ",
               i + 1, a[i]);
        show(a, n);
    }
    return 0;
}
''', ("6", "45 12 78 34 23 56"),
       r"""<ul><li>In pass i, the index of the <b>smallest</b> element of <code>a[i..n−1]</code> is found and that element is swapped into position i.</li>
<li>The sorted part grows from the left by one element every pass.</li>
<li>There is at most <b>one swap per pass</b> (n − 1 swaps in total), but the comparisons are always n(n − 1)/2 = 15, even for sorted data → O(n²) in every case.</li></ul>"""),

    PE("ds5p4", "Insertion sort with pass-by-pass output [Practical 13]", r'''
#include <stdio.h>

void show(int a[], int n)
{
    int i;
    for (i = 0; i < n; i++)
        printf("%d ", a[i]);
    printf("\n");
}

int main(void)
{
    int a[20], n, i, j, key;

    scanf("%d", &n);
    for (i = 0; i < n; i++)
        scanf("%d", &a[i]);

    for (i = 1; i < n; i++) {
        key = a[i];
        j = i - 1;
        while (j >= 0 && a[j] > key) {
            a[j + 1] = a[j];    /* shift right */
            j--;
        }
        a[j + 1] = key;
        printf("key %d: ", key);
        show(a, n);
    }
    return 0;
}
''', ("6", "45 12 78 34 23 56"),
       r"""<ul><li>The left part <code>a[0..i−1]</code> is always sorted. The next element (<b>key</b>) is inserted into it.</li>
<li>Bigger elements are <b>shifted</b> one place right until the correct position of the key is found.</li>
<li>Best case (sorted data): no shifting, O(n). Worst case (reverse order): O(n²). It is very good for small or nearly sorted data.</li></ul>"""),

    PE("ds5p5", "Quick sort (pivot = first element) with partition trace", r'''
#include <stdio.h>

int a[8] = {25, 57, 48, 37,
             12, 92, 86, 33};
int n = 8;

void show(void)
{
    int i;
    for (i = 0; i < n; i++)
        printf("%d ", a[i]);
    printf("\n");
}

int partition(int lo, int hi)
{
    int p = a[lo], i = lo + 1, j = hi, t;
    while (1) {
        while (i <= hi && a[i] <= p)
            i++;
        while (a[j] > p)
            j--;
        if (i < j) {
            t = a[i];
            a[i] = a[j];
            a[j] = t;
        } else
            break;
    }
    a[lo] = a[j];        /* pivot to place */
    a[j] = p;
    return j;
}

void quick(int lo, int hi)
{
    int k;
    if (lo < hi) {
        k = partition(lo, hi);
        printf("pivot %d -> [%d]: ",
               a[k], k);
        show();
        quick(lo, k - 1);
        quick(k + 1, hi);
    }
}

int main(void)
{
    printf("Input          : ");
    show();
    quick(0, n - 1);
    printf("Sorted         : ");
    show();
    return 0;
}
''', (),
       r"""<ul><li><b>Divide and conquer:</b> <code>partition()</code> places the pivot at its <b>final position</b> k, with smaller values on its left and larger values on its right.</li>
<li>i moves right while <code>a[i] ≤ pivot</code>, j moves left while <code>a[j] &gt; pivot</code>; out-of-place pairs are swapped. When i and j cross, the pivot is swapped with a[j].</li>
<li>The two parts are sorted <b>recursively</b>. Each output line shows one pivot reaching its final place.</li>
<li>Average O(n log n); worst case O(n²) when the data is already sorted.</li></ul>"""),

    PE("ds5p6", "Merge sort (recursive)", r'''
#include <stdio.h>

void merge(int a[], int l, int m, int r)
{
    int t[20], i = l, j = m + 1, k = 0;
    while (i <= m && j <= r) {
        if (a[i] <= a[j])
            t[k++] = a[i++];
        else
            t[k++] = a[j++];
    }
    while (i <= m) t[k++] = a[i++];
    while (j <= r) t[k++] = a[j++];
    for (i = l, k = 0; i <= r; i++, k++)
        a[i] = t[k];
}

void msort(int a[], int l, int r)
{
    int m, i;
    if (l < r) {
        m = (l + r) / 2;
        msort(a, l, m);
        msort(a, m + 1, r);
        merge(a, l, m, r);
        printf("merged [%d..%d]: ", l, r);
        for (i = l; i <= r; i++)
            printf("%d ", a[i]);
        printf("\n");
    }
}

int main(void)
{
    int a[7] = {38, 27, 43, 3, 9, 82, 10};
    int i;
    msort(a, 0, 6);
    printf("Sorted: ");
    for (i = 0; i < 7; i++)
        printf("%d ", a[i]);
    printf("\n");
    return 0;
}
''', (),
       r"""<ul><li><b>Divide:</b> split the array at <code>m = (l + r) / 2</code> until each part has one element.</li>
<li><b>Conquer and combine:</b> <code>merge()</code> joins two sorted halves into one sorted part using a temporary array.</li>
<li>The output shows each merge: [0..1] = 27 38, then [2..3] = 3 43, then [0..3] = 3 27 38 43, and so on.</li>
<li>Always O(n log n) (best, average and worst), but it needs O(n) extra memory.</li></ul>"""),

    PE("ds5p7", "Radix sort (LSD, base 10) with pass output", r'''
#include <stdio.h>

int main(void)
{
    int a[8] = {170, 45, 75, 90,
                802, 24, 2, 66};
    int n = 8, b[10][8], cnt[10];
    int i, j, k, d, max = a[0];
    int exp = 1, pass = 0;

    for (i = 1; i < n; i++)
        if (a[i] > max) max = a[i];

    while (max / exp > 0) {
        for (d = 0; d < 10; d++)
            cnt[d] = 0;
        for (i = 0; i < n; i++) {
            d = (a[i] / exp) % 10;
            b[d][cnt[d]++] = a[i];
        }
        k = 0;
        for (d = 0; d < 10; d++)
            for (j = 0; j < cnt[d]; j++)
                a[k++] = b[d][j];
        printf("Pass %d: ", ++pass);
        for (i = 0; i < n; i++)
            printf("%d ", a[i]);
        printf("\n");
        exp *= 10;
    }
    return 0;
}
''', (),
       r"""<ul><li>Numbers are put into <b>buckets 0–9</b> by the units digit, collected in bucket order, then distributed again by the tens digit, then the hundreds digit.</li>
<li>The number of passes = the number of digits in the largest number (802 → 3 passes).</li>
<li>No element is compared with another. Time O(d × n), where d = number of digits.</li>
<li>Collecting in order keeps the earlier passes' order (<b>stable</b>), which is why it works.</li></ul>"""),

    PE("ds5p8", "Linear search", r'''
#include <stdio.h>

int linear(int a[], int n, int key)
{
    int i;
    for (i = 0; i < n; i++)
        if (a[i] == key)
            return i;
    return -1;
}

int main(void)
{
    int a[7] = {34, 12, 78, 23, 56, 45, 9};
    int keys[3] = {56, 34, 99}, i, k;

    for (i = 0; i < 3; i++) {
        k = linear(a, 7, keys[i]);
        if (k != -1)
            printf("%d at [%d], comp=%d\n",
                   keys[i], k, k + 1);
        else
            printf("%d not found\n",
                   keys[i]);
    }
    return 0;
}
''', (),
       r"""<ul><li>Each element is compared with the key from the first to the last.</li>
<li><b>Best case:</b> key at the first position (34): 1 comparison. <b>Worst case:</b> key at the end or not present (99): n comparisons.</li>
<li>Works on <b>unsorted</b> data. Time O(n).</li></ul>"""),

    PE("ds5p9", "Binary search (iterative) with steps [Practical 14]", r'''
#include <stdio.h>

int main(void)
{
    int a[10] = {5, 12, 18, 23, 34,
                 45, 56, 67, 78, 89};
    int low = 0, high = 9, mid, key;

    scanf("%d", &key);
    while (low <= high) {
        mid = (low + high) / 2;
        printf("low=%d high=%d mid=%d ",
               low, high, mid);
        printf("a[mid]=%d\n", a[mid]);
        if (a[mid] == key) {
            printf("%d found at [%d]\n",
                   key, mid);
            return 0;
        } else if (key < a[mid])
            high = mid - 1;
        else
            low = mid + 1;
    }
    printf("%d not found\n", key);
    return 0;
}
''', ("23",),
       r"""<ul><li>The array must be <b>sorted</b>.</li>
<li>Compare the key with the middle element: if equal, it is found; if smaller, search the left half (<code>high = mid − 1</code>); if larger, the right half (<code>low = mid + 1</code>).</li>
<li>Half of the remaining elements are discarded each step: 23 is found in 4 steps instead of up to 10 → O(log n).</li></ul>"""),

    PE("ds5p10", "Binary search (recursive)", r'''
#include <stdio.h>

int bsearch_r(int a[], int low, int high,
              int key)
{
    int mid;
    if (low > high)
        return -1;            /* base case */
    mid = (low + high) / 2;
    if (a[mid] == key)
        return mid;
    if (key < a[mid])
        return bsearch_r(a, low, mid - 1,
                         key);
    return bsearch_r(a, mid + 1, high,
                     key);
}

int main(void)
{
    int a[10] = {5, 12, 18, 23, 34,
                 45, 56, 67, 78, 89};
    int keys[4] = {5, 89, 45, 60}, i, k;
    for (i = 0; i < 4; i++) {
        k = bsearch_r(a, 0, 9, keys[i]);
        printf("search %2d -> %d\n",
               keys[i], k);
    }
    return 0;
}
''', (),
       r"""<ul><li>The same logic written recursively: each call searches one half.</li>
<li>The base case <code>low &gt; high</code> means the range is empty, so the function returns −1 (not found).</li>
<li>The output gives the index of each key, or −1 for 60.</li></ul>"""),

    PE("ds5p11", "Sort names alphabetically (strings)", r'''
#include <stdio.h>
#include <string.h>

int main(void)
{
    char s[5][20] = {"Ravi", "Amit",
                     "Neha", "Meena",
                     "Bhavin"};
    char t[20];
    int i, j, n = 5;

    for (i = 0; i < n - 1; i++)
        for (j = 0; j < n - 1 - i; j++)
            if (strcmp(s[j], s[j+1]) > 0) {
                strcpy(t, s[j]);
                strcpy(s[j], s[j + 1]);
                strcpy(s[j + 1], t);
            }
    for (i = 0; i < n; i++)
        printf("%s\n", s[i]);
    return 0;
}
''', (),
       r"""<ul><li>Bubble sort works for strings too: <code>strcmp(a, b) &gt; 0</code> means a comes after b in dictionary order.</li>
<li>Strings cannot be assigned with <code>=</code>, so <code>strcpy</code> is used to swap them through a temporary array.</li></ul>"""),

    PE("ds5p12", "Hash table: division method with linear probing", r'''
#include <stdio.h>
#define M 10

int table[M];

void insert(int key)
{
    int h = key % M, i = h;
    while (table[i] != -1)
        i = (i + 1) % M;   /* next slot */
    table[i] = key;
    printf("%d: h=%d slot=%d", key, h, i);
    if (i != h)
        printf(" (collision)");
    printf("\n");
}

int search(int key)
{
    int i = key % M, c = 0;
    while (table[i] != -1 && c < M) {
        if (table[i] == key) return i;
        i = (i + 1) % M;
        c++;
    }
    return -1;
}

int main(void)
{
    int k[6] = {1234, 5678, 4321, 9087,
                2466, 3456};
    int i;
    for (i = 0; i < M; i++) table[i] = -1;
    for (i = 0; i < 6; i++) insert(k[i]);
    for (i = 0; i < M; i++)
        printf("[%d] %d\n", i, table[i]);
    printf("search 3456 -> slot %d\n",
           search(3456));
    printf("search 1111 -> slot %d\n",
           search(1111));
    return 0;
}
''', (),
       r"""<ul><li><b>Hash function (division method):</b> <code>h(k) = k % 10</code> gives the slot directly, so most searches need only one comparison.</li>
<li>3456 also hashes to 6 (already used by 2466): a <b>collision</b>. With <b>linear probing</b> the next free slot is used: 7 and 8 are full, so it goes to slot 9.</li>
<li>Searching follows the same probe sequence; −1 means not found. (−1 in the table marks an empty slot.)</li></ul>"""),

    PE("ds5p13", "Mid-square and folding hash functions", r'''
#include <stdio.h>
#include <string.h>

int digits(long x)
{
    int d = 0;
    do { d++; x /= 10; } while (x > 0);
    return d;
}

int midsquare(long k)       /* 2 digits */
{
    long sq = k * k, p = 1;
    int n = digits(sq), drop, i;
    drop = n - (n - 2) / 2 - 2;
    for (i = 0; i < drop; i++)
        p *= 10;
    printf("k=%ld k^2=%ld ", k, sq);
    return (int)((sq / p) % 100);
}

int folding(long k)    /* parts of 2 */
{
    char s[20];
    int i, sum = 0, n;
    sprintf(s, "%ld", k);
    n = strlen(s);
    for (i = 0; i < n; i += 2) {
        int part = s[i] - '0';
        if (i + 1 < n)
            part = part * 10
                   + s[i + 1] - '0';
        sum += part;
    }
    printf("k=%ld sum=%d ", k, sum);
    return sum % 100;
}

int main(void)
{
    printf("-> %d\n", midsquare(3205));
    printf("-> %d\n", midsquare(4567));
    printf("-> %d\n", folding(12345678));
    printf("-> %d\n", folding(9876543));
    return 0;
}
''', (),
       r"""<ul><li><b>Mid-square:</b> square the key and take the <b>middle 2 digits</b>: 3205² = 10272025 → 72. The middle digits depend on all digits of the key, so the spread is good.</li>
<li><b>Folding (shift folding):</b> split the key into 2-digit parts from the left and add them: 12 + 34 + 56 + 78 = 180 → keep the last 2 digits → 80.</li>
<li>For 9876543 the last part has one digit: 98 + 76 + 54 + 3 = 231 → 31.</li></ul>"""),

    PE("ds5p14", "Compare bubble, selection and insertion sort (comparisons)", r'''
#include <stdio.h>

int bubble(int a[], int n)
{
    int i, j, t, c = 0, f;
    for (i = 0; i < n - 1; i++) {
        f = 0;
        for (j = 0; j < n - 1 - i; j++) {
            c++;
            if (a[j] > a[j + 1]) {
                t = a[j]; a[j] = a[j + 1];
                a[j + 1] = t; f = 1;
            }
        }
        if (!f) break;
    }
    return c;
}

int selection(int a[], int n)
{
    int i, j, m, t, c = 0;
    for (i = 0; i < n - 1; i++) {
        m = i;
        for (j = i + 1; j < n; j++) {
            c++;
            if (a[j] < a[m]) m = j;
        }
        t = a[i]; a[i] = a[m]; a[m] = t;
    }
    return c;
}

int insertion(int a[], int n)
{
    int i, j, k, c = 0;
    for (i = 1; i < n; i++) {
        k = a[i];
        for (j = i - 1; j >= 0; j--) {
            c++;
            if (a[j] <= k) break;
            a[j + 1] = a[j];
        }
        a[j + 1] = k;
    }
    return c;
}

void copy(int d[], int s[])
{
    int i;
    for (i = 0; i < 8; i++) d[i] = s[i];
}

int main(void)
{
    int in[3][8] = {
        {1, 2, 3, 4, 5, 6, 7, 8},
        {8, 7, 6, 5, 4, 3, 2, 1},
        {25, 57, 48, 37, 12, 92, 86, 33}};
    char *nm[3] = {"sorted ", "reverse",
                   "random "};
    int w[8], i;
    puts("input  bubble select insert");
    for (i = 0; i < 3; i++) {
        printf("%s", nm[i]);
        copy(w, in[i]);
        printf("%6d", bubble(w, 8));
        copy(w, in[i]);
        printf("%7d", selection(w, 8));
        copy(w, in[i]);
        printf("%7d\n", insertion(w, 8));
    }
    return 0;
}
''', (),
       r"""<ul><li>The same three inputs of 8 elements are given to each algorithm, and the comparisons are counted.</li>
<li><b>Sorted input:</b> bubble (with flag) and insertion need only n − 1 = 7 comparisons (best case O(n)); selection still needs 28.</li>
<li><b>Reverse input:</b> all need n(n − 1)/2 = 28 comparisons (worst case O(n²)).</li>
<li>Insertion sort usually makes the fewest comparisons on random data.</li></ul>"""),
]
