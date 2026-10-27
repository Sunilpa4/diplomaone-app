"""DI01000131 Unit 4 - solved C programs (user-defined functions). English only; compiled & run with gcc."""
from c_content import PE

PROGRAMS = [
    PE("c4p1", "Addition of two numbers using a function (three elements)", r'''
#include <stdio.h>

int add(int x, int y);              // 1. declaration (prototype)

int main(void)
{
    int a, b, s;

    printf("Enter two numbers: ");
    scanf("%d %d", &a, &b);

    s = add(a, b);                  // 2. call: a, b are actual args
    printf("Sum = %d\n", s);
    return 0;
}

int add(int x, int y)               // 3. definition: x, y are formal
{
    int z;
    z = x + y;
    return z;                       // value sent back to main()
}
''', ["18 24"],
       r"""<p>This program shows the <b>three elements</b> of a user-defined function:</p>
<ol><li><b>Declaration (prototype)</b> <code>int add(int x, int y);</code> tells the compiler the name, return type and parameter types before the function is used.</li>
<li><b>Call</b> <code>add(a, b)</code> transfers control to the function. The values of the <b>actual arguments</b> a, b are copied into the <b>formal parameters</b> x, y.</li>
<li><b>Definition</b>: the header <code>int add(int x, int y)</code> plus the body in braces. <code>return z;</code> sends the result back, where it is assigned to s.</li></ol>"""),

    PE("c4p2", "Category 1: no arguments, no return value", r'''
#include <stdio.h>

void line(void);                    // no args, returns nothing

int main(void)
{
    line();
    printf("  GUJARAT TECHNOLOGICAL UNIVERSITY\n");
    line();
    printf("  Computer Programming Fundamentals\n");
    line();
    return 0;
}

void line(void)
{
    int i;
    for (i = 0; i < 38; i++)
        printf("-");
    printf("\n");
}
''', (),
       r"""<ul><li><code>void line(void)</code>: the first <code>void</code> means it <b>returns no value</b>; <code>(void)</code> means it <b>takes no arguments</b>.</li>
<li>There is <b>no data transfer</b> between main() and line(); the function simply does its job (prints a line) each time it is called.</li>
<li>The same code is reused three times without being rewritten, which is the main benefit of functions.</li></ul>"""),

    PE("c4p3", "Category 2: arguments but no return value (multiplication table)", r'''
#include <stdio.h>

void table(int n);                  // takes n, returns nothing

int main(void)
{
    int num;
    printf("Enter a number: ");
    scanf("%d", &num);
    table(num);                     // value passed to function
    return 0;
}

void table(int n)
{
    int i;
    for (i = 1; i <= 10; i++)
        printf("%d x %2d = %3d\n", n, i, n * i);
}
''', ["7"],
       r"""<p>Data flows <b>one way</b>, from main() to the function. main() passes <code>num</code>; the function receives it in <code>n</code>, prints the table, and returns nothing (<code>void</code>). The result is printed <b>inside</b> the function, so main() cannot use it.</p>"""),

    PE("c4p4", "Category 3: arguments with return value (area of circle and maximum)", r'''
#include <stdio.h>
#define PI 3.14159

float area(float r);
int max(int a, int b);

int main(void)
{
    float rad;
    int x, y;

    printf("Enter radius: ");
    scanf("%f", &rad);
    printf("Area = %.2f\n", area(rad));     // call inside printf

    printf("Enter two integers: ");
    scanf("%d %d", &x, &y);
    printf("Maximum = %d\n", max(x, y));
    return 0;
}

float area(float r)
{
    return PI * r * r;
}

int max(int a, int b)
{
    if (a > b)
        return a;                   // more than one return allowed
    else
        return b;
}
''', ["7", "45 62"],
       r"""<ul><li>Data flows <b>both ways</b>: arguments go in and a value comes back. This is the most useful and most common category.</li>
<li>The returned value can be used directly in an expression or in printf: <code>printf("%.2f", area(rad));</code></li>
<li>A function may contain <b>several return statements</b>, but only one of them is executed, and only <b>one value</b> can be returned.</li></ul>"""),

    PE("c4p5", "Category 4: no arguments but returns a value", r'''
#include <stdio.h>

int read_positive(void);            // no args, returns int

int main(void)
{
    int n = read_positive();
    printf("You entered %d, square = %d\n", n, n * n);
    return 0;
}

int read_positive(void)
{
    int x;
    do
    {
        printf("Enter a positive number: ");
        scanf("%d", &x);
    } while (x <= 0);               // repeat until valid
    return x;
}
''', ["-5", "0", "12"],
       r"""<p>The function takes <b>no arguments</b> but <b>returns</b> a value to main(). It is useful when the function itself produces the data, e.g. reading and validating input, or generating a random number. <code>getchar()</code> is a library function of this category.</p>"""),

    PE("c4p6", "Factorial function and nCr (function called many times)", r'''
#include <stdio.h>

long fact(int n);

int main(void)
{
    int n, r;
    long ncr;

    printf("Enter n and r: ");
    scanf("%d %d", &n, &r);

    ncr = fact(n) / (fact(r) * fact(n - r));
    printf("%dC%d = %ld\n", n, r, ncr);
    return 0;
}

long fact(int n)
{
    long f = 1;
    int i;
    for (i = 2; i <= n; i++)
        f = f * i;
    return f;
}
''', ["6 2"],
       r"""<p>nCr = n! / (r! × (n−r)!). Without a function the factorial loop would have to be written three times. Calling <code>fact()</code> three times, with different arguments, shows how functions <b>avoid repetition</b>. 6C2 = 720 / (2 × 24) = 15.</p>"""),

    PE("c4p7", "Prime numbers in a range using a function", r'''
#include <stdio.h>

int isPrime(int n);                 // returns 1 or 0

int main(void)
{
    int lo, hi, i, count = 0;

    printf("Enter range (low high): ");
    scanf("%d %d", &lo, &hi);

    printf("Primes: ");
    for (i = lo; i <= hi; i++)
    {
        if (isPrime(i))
        {
            printf("%d ", i);
            count++;
        }
    }
    printf("\nTotal = %d\n", count);
    return 0;
}

int isPrime(int n)
{
    int i;
    if (n < 2)
        return 0;
    for (i = 2; i * i <= n; i++)
        if (n % i == 0)
            return 0;               // return also ends the loop
    return 1;
}
''', ["10 50"],
       r"""<ul><li><code>isPrime()</code> returns <b>1 (true)</b> or <b>0 (false)</b>, so it can be used directly in an <code>if</code>.</li>
<li><code>return 0;</code> inside the loop ends the function immediately; no break or flag is needed.</li>
<li>main() stays short and readable, because the prime-checking logic is in its own function.</li></ul>"""),

    PE("c4p8", "Call by value vs call by reference (swap)", r'''
#include <stdio.h>

void swap_value(int x, int y);
void swap_ref(int *x, int *y);

int main(void)
{
    int a = 10, b = 20;

    swap_value(a, b);               // copies passed
    printf("After call by value     : a = %d, b = %d\n", a, b);

    swap_ref(&a, &b);               // addresses passed
    printf("After call by reference : a = %d, b = %d\n", a, b);
    return 0;
}

void swap_value(int x, int y)
{
    int t = x;
    x = y;
    y = t;
    printf("Inside swap_value       : x = %d, y = %d\n", x, y);
}

void swap_ref(int *x, int *y)
{
    int t = *x;
    *x = *y;
    *y = t;
}
''', (),
       r"""<ul><li><b>Call by value:</b> <code>swap_value(a, b)</code> copies 10 and 20 into x and y. Only the copies are swapped, so a and b in main() are unchanged.</li>
<li><b>Call by reference:</b> <code>swap_ref(&amp;a, &amp;b)</code> passes the <b>addresses</b>. The function works on the original variables through <code>*x</code> and <code>*y</code>, so a and b really are swapped.</li>
<li>See the diagram "Call by Value vs Call by Reference".</li></ul>"""),

    PE("c4p9", "Returning more than one value using pointers", r'''
#include <stdio.h>

void stats(int a[], int n, int *max, int *min, float *avg);

int main(void)
{
    int m[] = {67, 82, 45, 91, 58};
    int hi, lo;
    float av;

    stats(m, 5, &hi, &lo, &av);     // 3 results come back
    printf("Max = %d, Min = %d, Average = %.2f\n", hi, lo, av);
    return 0;
}

void stats(int a[], int n, int *max, int *min, float *avg)
{
    int i, sum = 0;
    *max = *min = a[0];
    for (i = 0; i < n; i++)
    {
        if (a[i] > *max) *max = a[i];
        if (a[i] < *min) *min = a[i];
        sum += a[i];
    }
    *avg = (float) sum / n;
}
''', (),
       r"""<p><code>return</code> can send back only <b>one</b> value. To get several results, the caller passes the <b>addresses</b> of variables, and the function stores the results through the pointers (<code>*max = …</code>). This is an application of call by reference.</p>"""),

    PE("c4p10", "Passing an array to a function (average)", r'''
#include <stdio.h>

float average(int x[], int n);      // array parameter

int main(void)
{
    int a[50], n, i;

    printf("How many numbers? ");
    scanf("%d", &n);
    printf("Enter %d numbers: ", n);
    for (i = 0; i < n; i++)
        scanf("%d", &a[i]);

    printf("Average = %.2f\n", average(a, n));  // only name passed
    return 0;
}

float average(int x[], int n)
{
    int i, sum = 0;
    for (i = 0; i < n; i++)
        sum += x[i];
    return (float) sum / n;
}
''', ["5", "12 18 25 30 41"],
       r"""<ul><li>To pass a whole array, write <b>only its name</b> in the call: <code>average(a, n)</code>, not <code>a[]</code> or <code>a[n]</code>.</li>
<li>In the definition the parameter is written <code>int x[]</code> (the size can be left out). <code>int *x</code> means the same.</li>
<li>The array does not know its own size, so the number of elements <code>n</code> is passed as a separate argument.</li></ul>"""),

    PE("c4p11", "Sorting an array inside a function (array modified)", r'''
#include <stdio.h>

void sort(int x[], int n);
void print(int x[], int n);

int main(void)
{
    int a[] = {42, 7, 19, 88, 3, 56};
    int n = 6;

    printf("Before: ");  print(a, n);
    sort(a, n);
    printf("After : ");  print(a, n);
    return 0;
}

void sort(int x[], int n)           // bubble sort
{
    int i, j, t;
    for (i = 0; i < n - 1; i++)
        for (j = 0; j < n - 1 - i; j++)
            if (x[j] > x[j + 1])
            {
                t = x[j]; x[j] = x[j + 1]; x[j + 1] = t;
            }
}

void print(int x[], int n)
{
    int i;
    for (i = 0; i < n; i++)
        printf("%d ", x[i]);
    printf("\n");
}
''', (),
       r"""<p>An array is passed by its <b>base address</b>, so the function works on the <b>original array</b>, not a copy. The sorting done in <code>sort()</code> is therefore visible in main(): arrays are always passed <b>by reference</b>. Use <code>const int x[]</code> if the function must not change the array.</p>"""),

    PE("c4p12", "Passing a 2-D array to a function", r'''
#include <stdio.h>

void display(int m[][3], int rows);
int total(int m[][3], int rows);

int main(void)
{
    int mat[2][3] = { {1, 2, 3},
                      {4, 5, 6} };

    display(mat, 2);
    printf("Sum of all elements = %d\n", total(mat, 2));
    return 0;
}

void display(int m[][3], int rows)  // column size compulsory
{
    int i, j;
    for (i = 0; i < rows; i++)
    {
        for (j = 0; j < 3; j++)
            printf("%4d", m[i][j]);
        printf("\n");
    }
}

int total(int m[][3], int rows)
{
    int i, j, s = 0;
    for (i = 0; i < rows; i++)
        for (j = 0; j < 3; j++)
            s += m[i][j];
    return s;
}
''', (),
       r"""<p>For a 2-D array parameter the <b>first dimension may be omitted</b>, but the <b>column size must be given</b> (<code>int m[][3]</code>). The compiler needs the number of columns to find <code>m[i][j]</code> in row-major memory (address = base + (i × 3 + j) × size). The call uses only the name: <code>display(mat, 2)</code>.</p>"""),

    PE("c4p13", "Factorial using recursion", r'''
#include <stdio.h>

long fact(int n);

int main(void)
{
    int n;
    printf("Enter a number: ");
    scanf("%d", &n);
    printf("%d! = %ld\n", n, fact(n));
    return 0;
}

long fact(int n)
{
    if (n <= 1)                     // base case: stops recursion
        return 1;
    else
        return n * fact(n - 1);     // recursive call
}
''', ["5"],
       r"""<ul><li><b>Recursion:</b> <code>fact()</code> calls itself with a smaller value (n − 1).</li>
<li><b>Base case</b> <code>n &lt;= 1</code> returns 1 without another call. Without it the recursion would never end (stack overflow).</li>
<li>fact(5) = 5 × fact(4) = 5 × 4 × fact(3) = … = 5 × 4 × 3 × 2 × 1 = 120. See the diagram "Recursion: How fact(4) Works".</li></ul>"""),

    PE("c4p14", "Fibonacci series using recursion", r'''
#include <stdio.h>

int fib(int n);

int main(void)
{
    int n, i;
    printf("Enter number of terms: ");
    scanf("%d", &n);

    printf("Fibonacci series: ");
    for (i = 0; i < n; i++)
        printf("%d ", fib(i));
    printf("\n");
    return 0;
}

int fib(int n)
{
    if (n == 0) return 0;           // base cases
    if (n == 1) return 1;
    return fib(n - 1) + fib(n - 2); // two recursive calls
}
''', ["10"],
       r"""<p>Each term is the sum of the two previous terms: <code>fib(n) = fib(n−1) + fib(n−2)</code>, with <b>two base cases</b>, fib(0) = 0 and fib(1) = 1. The recursion tree shows that the same values are calculated many times, so the loop version (Unit 2) is much faster for large n.</p>"""),

    PE("c4p15", "GCD and power using recursion", r'''
#include <stdio.h>

int gcd(int a, int b);
long power(int x, int n);

int main(void)
{
    int a, b, x, n;

    printf("Enter two numbers for GCD: ");
    scanf("%d %d", &a, &b);
    printf("GCD(%d, %d) = %d\n", a, b, gcd(a, b));

    printf("Enter base and exponent: ");
    scanf("%d %d", &x, &n);
    printf("%d ^ %d = %ld\n", x, n, power(x, n));
    return 0;
}

int gcd(int a, int b)               // Euclid's method
{
    if (b == 0)
        return a;
    return gcd(b, a % b);
}

long power(int x, int n)
{
    if (n == 0)
        return 1;
    return x * power(x, n - 1);
}
''', ["48 36", "2 10"],
       r"""<ul><li><b>Euclid's GCD:</b> gcd(a, b) = gcd(b, a % b) until b becomes 0. gcd(48, 36) → gcd(36, 12) → gcd(12, 0) = 12.</li>
<li><b>Power:</b> x<sup>n</sup> = x × x<sup>n−1</sup>, base case x<sup>0</sup> = 1. 2<sup>10</sup> = 1024.</li>
<li>Every recursive function needs a <b>base case</b> and must move towards it with each call.</li></ul>"""),

    PE("c4p16", "Scope of variables: global, local and block", r'''
#include <stdio.h>

int g = 100;                        // global variable

void fun(void);

int main(void)
{
    int x = 10;                     // local to main
    printf("main : g = %d, x = %d\n", g, x);
    {
        int x = 20;                 // block variable hides outer x
        printf("block: x = %d\n", x);
    }
    printf("main : x = %d (outer x again)\n", x);
    fun();
    printf("main : g = %d (changed by fun)\n", g);
    return 0;
}

void fun(void)
{
    int x = 30;                     // different x, local to fun
    g = g + 1;                      // global is shared
    printf("fun  : g = %d, x = %d\n", g, x);
}
''', (),
       r"""<ul><li><b>Global</b> <code>g</code> is declared outside all functions, so it is visible in main() and fun(), and the change made by fun() is seen in main().</li>
<li><b>Local</b> <code>x</code> of main() and <code>x</code> of fun() are different variables; each exists only inside its function.</li>
<li>The inner block declares its own x, which <b>hides</b> the outer x until the block ends.</li></ul>"""),

    PE("c4p17", "auto vs static local variables", r'''
#include <stdio.h>

void counter(void);

int main(void)
{
    int i;
    for (i = 1; i <= 3; i++)
        counter();
    return 0;
}

void counter(void)
{
    auto int a = 0;                 // created on every call
    static int s = 0;               // initialized only once
    a++;
    s++;
    printf("auto a = %d, static s = %d\n", a, s);
}
''', (),
       r"""<ul><li>The <b>auto</b> variable <code>a</code> is created and set to 0 on <b>every call</b> and destroyed when the function returns, so it always prints 1.</li>
<li>The <b>static</b> variable <code>s</code> is initialized <b>only once</b> and <b>keeps its value between calls</b> (its lifetime is the whole program), so it counts 1, 2, 3.</li>
<li>Both are local: neither can be used outside <code>counter()</code>.</li></ul>"""),
]

if __name__ == "__main__":
    for p in PROGRAMS:
        print("=" * 20, p["id"], p["title"]["en"]); print(p["out"])
