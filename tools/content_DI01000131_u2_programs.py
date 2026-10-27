"""DI01000131 Unit 2 - solved C programs (English only; compiled & run with gcc, output captured automatically)."""
from c_content import PE

PROGRAMS = [
    PE("c2p1", "Absolute value of a number (simple if)", r'''
#include <stdio.h>

int main(void)
{
    int n;

    printf("Enter a number: ");
    scanf("%d", &n);

    if (n < 0)          // simple if: block runs only when true
        n = -n;

    printf("Absolute value = %d\n", n);
    return 0;
}
''', ["-27"],
       r"""<p>A <b>simple if</b> has no else part. If <code>n &lt; 0</code> is true, the sign is changed; otherwise the statement is skipped and control goes directly to <code>printf()</code>. For input 27 the output would also be 27.</p>"""),

    PE("c2p2", "Even or odd number (if-else)", r'''
#include <stdio.h>

int main(void)
{
    int n;

    printf("Enter an integer: ");
    scanf("%d", &n);

    if (n % 2 == 0)
        printf("%d is EVEN\n", n);
    else
        printf("%d is ODD\n", n);

    return 0;
}
''', ["17"],
       r"""<p><code>n % 2</code> gives the remainder after dividing by 2. A remainder of 0 means the number is even. In an <b>if-else</b> statement exactly one of the two blocks is executed.</p>"""),

    PE("c2p3", "Leap year check", r'''
#include <stdio.h>

int main(void)
{
    int year;

    printf("Enter year: ");
    scanf("%d", &year);

    /* leap: divisible by 4 but not by 100, OR divisible by 400 */
    if ((year % 4 == 0 && year % 100 != 0) || (year % 400 == 0))
        printf("%d is a LEAP year\n", year);
    else
        printf("%d is NOT a leap year\n", year);

    return 0;
}
''', ["2024"],
       r"""<p><b>Rule:</b> a year is a leap year if it is divisible by 4 and not by 100, <b>or</b> if it is divisible by 400.</p>
<ul><li>2024 → divisible by 4, not by 100 → leap.</li><li>1900 → divisible by 100 but not 400 → not leap.</li><li>2000 → divisible by 400 → leap.</li></ul>
<p>The logical operators <code>&amp;&amp;</code> and <code>||</code> combine the conditions in a single if-else.</p>"""),

    PE("c2p4", "Largest of three numbers (nested if-else)", r'''
#include <stdio.h>

int main(void)
{
    int a, b, c;

    printf("Enter three numbers: ");
    scanf("%d %d %d", &a, &b, &c);

    if (a > b)
    {
        if (a > c)              // inner if inside outer if
            printf("Largest = %d\n", a);
        else
            printf("Largest = %d\n", c);
    }
    else
    {
        if (b > c)
            printf("Largest = %d\n", b);
        else
            printf("Largest = %d\n", c);
    }
    return 0;
}
''', ["25 67 43"],
       r"""<p>This follows the flowchart of Unit 1 (largest of three). The outer if compares <code>a</code> and <code>b</code>; the winner is then compared with <code>c</code> by an <b>inner (nested) if-else</b>. Braces <code>{ }</code> make the pairing of each <code>else</code> clear.</p>"""),

    PE("c2p5", "Result class from percentage (else-if ladder)", r'''
#include <stdio.h>

int main(void)
{
    float per;

    printf("Enter percentage: ");
    scanf("%f", &per);

    if (per < 0 || per > 100)
        printf("Invalid percentage\n");
    else if (per >= 70)
        printf("Distinction\n");
    else if (per >= 60)
        printf("First Class\n");
    else if (per >= 50)
        printf("Second Class\n");
    else if (per >= 40)
        printf("Pass Class\n");
    else
        printf("Fail\n");           // default

    return 0;
}
''', ["64.5"],
       r"""<p>In an <b>else-if ladder</b> the conditions are tested from top to bottom. As soon as one is true its statement runs and the rest of the ladder is skipped. For 64.5: <code>per &gt;= 70</code> is false, <code>per &gt;= 60</code> is true → "First Class". The final <code>else</code> is the default when no condition is true.</p>"""),

    PE("c2p6", "Simple calculator (switch)", r'''
#include <stdio.h>

int main(void)
{
    float a, b;
    char op;

    printf("Enter expression (e.g. 12 * 5): ");
    scanf("%f %c %f", &a, &op, &b);

    switch (op)
    {
        case '+': printf("Result = %.2f\n", a + b); break;
        case '-': printf("Result = %.2f\n", a - b); break;
        case '*': printf("Result = %.2f\n", a * b); break;
        case '/':
            if (b != 0)
                printf("Result = %.2f\n", a / b);
            else
                printf("Error: division by zero\n");
            break;
        default:  printf("Invalid operator\n");
    }
    return 0;
}
''', ["12 * 5"],
       r"""<ul><li>The <code>switch</code> expression <code>op</code> is a <code>char</code> (an integer type), so it can be used in switch. Case labels are character constants.</li>
<li>Each case ends with <code>break</code>, which sends control out of the switch. Without it, execution would <b>fall through</b> to the next case.</li>
<li><code>default</code> handles any operator that matches no case.</li>
<li>An if-else inside <code>case '/'</code> prevents division by zero.</li></ul>"""),

    PE("c2p7", "Vowel or consonant (switch with grouped cases)", r'''
#include <stdio.h>
#include <ctype.h>

int main(void)
{
    char ch;

    printf("Enter an alphabet: ");
    scanf(" %c", &ch);

    if (!isalpha(ch)) {
        printf("Not an alphabet\n");
        return 0;
    }

    switch (tolower(ch))
    {
        case 'a':
        case 'e':
        case 'i':
        case 'o':
        case 'u':               // fall-through groups the vowels
            printf("%c is a VOWEL\n", ch);
            break;
        default:
            printf("%c is a CONSONANT\n", ch);
    }
    return 0;
}
''', ["E"],
       r"""<p>The cases <code>'a'</code> to <code>'u'</code> have no statements and no <code>break</code>, so control <b>falls through</b> to the common printf. This is the useful side of fall-through: several case values share one block. <code>tolower()</code> converts uppercase input to lowercase, so both 'E' and 'e' work.</p>"""),

    PE("c2p8", "Sum of 1 to N using goto", r'''
#include <stdio.h>

int main(void)
{
    int n, i = 1, sum = 0;

    printf("Enter N: ");
    scanf("%d", &n);

    if (n <= 0)
        goto error;             // forward jump

loop:                           // label
    sum = sum + i;
    i++;
    if (i <= n)
        goto loop;              // backward jump -> loop

    printf("Sum of 1 to %d = %d\n", n, sum);
    return 0;

error:
    printf("N must be positive\n");
    return 1;
}
''', ["10"],
       r"""<ul><li><code>loop:</code> and <code>error:</code> are <b>labels</b> (an identifier followed by a colon).</li>
<li><code>goto loop;</code> is a <b>backward jump</b>: it repeats statements, forming a loop.</li>
<li><code>goto error;</code> is a <b>forward jump</b>: it skips statements.</li>
<li>Sum = 1 + 2 + … + 10 = 55. The same work is done more clearly with a <code>for</code> loop; goto is shown here because it is in the syllabus.</li></ul>"""),

    PE("c2p9", "Reverse a number and check palindrome (while)", r'''
#include <stdio.h>

int main(void)
{
    int n, temp, d, rev = 0;

    printf("Enter a number: ");
    scanf("%d", &n);

    temp = n;                   // keep original value
    while (temp > 0)
    {
        d = temp % 10;          // last digit
        rev = rev * 10 + d;     // append digit to rev
        temp = temp / 10;       // remove last digit
    }

    printf("Reverse = %d\n", rev);
    if (rev == n)
        printf("%d is a PALINDROME\n", n);
    else
        printf("%d is NOT a palindrome\n", n);
    return 0;
}
''', ["12321"],
       r"""<p>This is the flowchart "Reverse of a Number" in code. Dry run for 123:</p>
<table><tr><th>temp</th><th>d</th><th>rev</th></tr><tr><td>123</td><td>3</td><td>3</td></tr><tr><td>12</td><td>2</td><td>32</td></tr><tr><td>1</td><td>1</td><td>321</td></tr><tr><td>0</td><td colspan="2">loop ends</td></tr></table>
<p>The number of digits is not known in advance, so a <b>while</b> loop is used. A copy (<code>temp</code>) is reversed so the original <code>n</code> is still available for the comparison.</p>"""),

    PE("c2p10", "Sum of numbers until 0 is entered (do-while)", r'''
#include <stdio.h>

int main(void)
{
    int n, sum = 0, count = 0;

    printf("Enter numbers (0 to stop):\n");
    do
    {
        scanf("%d", &n);
        sum = sum + n;
        if (n != 0)
            count++;
    } while (n != 0);           // note the semicolon

    printf("Total of %d numbers = %d\n", count, sum);
    return 0;
}
''', ["15", "8", "22", "5", "0"],
       r"""<p>The body must run <b>at least once</b> (a number has to be read before it can be tested), so an exit-controlled <b>do-while</b> loop is ideal. The value 0 is a <b>sentinel</b> that marks the end of input. Note the semicolon after <code>while (n != 0);</code>. 15 + 8 + 22 + 5 = 50.</p>"""),

    PE("c2p11", "Factorial of a number (for)", r'''
#include <stdio.h>

int main(void)
{
    int n, i;
    unsigned long long fact = 1;

    printf("Enter a number: ");
    scanf("%d", &n);

    if (n < 0)
        printf("Factorial of a negative number does not exist\n");
    else
    {
        for (i = 1; i <= n; i++)
            fact = fact * i;
        printf("%d! = %llu\n", n, fact);
    }
    return 0;
}
''', ["10"],
       r"""<p>n! = 1 × 2 × 3 × … × n, and 0! = 1 (the loop does not run, so <code>fact</code> stays 1). Factorials grow very fast (13! exceeds a 32-bit int), so <code>unsigned long long</code> with <code>%llu</code> is used. It is correct up to 20!. 10! = 3628800.</p>"""),

    PE("c2p12", "Fibonacci series of N terms", r'''
#include <stdio.h>

int main(void)
{
    int n, i, a = 0, b = 1, c;

    printf("Enter number of terms: ");
    scanf("%d", &n);

    printf("Fibonacci series: ");
    for (i = 1; i <= n; i++)
    {
        printf("%d ", a);
        c = a + b;              // next term
        a = b;
        b = c;
    }
    printf("\n");
    return 0;
}
''', ["10"],
       r"""<p>In the Fibonacci series each term is the sum of the previous two: 0, 1, 1, 2, 3, 5, 8, … Variables <code>a</code> and <code>b</code> hold the last two terms. After printing <code>a</code>, the pair shifts forward: <code>a ← b</code>, <code>b ← a + b</code>.</p>"""),

    PE("c2p13", "Prime number check (for + break)", r'''
#include <stdio.h>

int main(void)
{
    int n, i, isPrime = 1;

    printf("Enter a number: ");
    scanf("%d", &n);

    if (n < 2)
        isPrime = 0;

    for (i = 2; i * i <= n; i++)
    {
        if (n % i == 0)
        {
            isPrime = 0;        // divisor found
            break;              // no need to check further
        }
    }

    if (isPrime)
        printf("%d is a PRIME number\n", n);
    else
        printf("%d is NOT a prime number\n", n);
    return 0;
}
''', ["97"],
       r"""<ul><li>A prime number has exactly two factors: 1 and itself. 0 and 1 are not prime.</li>
<li>It is enough to test divisors up to √n (<code>i * i &lt;= n</code>), because any larger factor pairs with a smaller one.</li>
<li><code>isPrime</code> is a <b>flag</b> variable. When a divisor is found, <code>break</code> exits the loop early.</li>
<li>Simpler version accepted in exams: <code>for (i = 2; i &lt;= n / 2; i++)</code>.</li></ul>"""),

    PE("c2p14", "Armstrong number check", r'''
#include <stdio.h>

int main(void)
{
    int n, temp, d, digits = 0, i, p;
    long sum = 0;

    printf("Enter a number: ");
    scanf("%d", &n);

    for (temp = n; temp > 0; temp /= 10)    // count digits
        digits++;

    temp = n;
    while (temp > 0)
    {
        d = temp % 10;
        p = 1;
        for (i = 1; i <= digits; i++)       // p = d ^ digits
            p = p * d;
        sum = sum + p;
        temp = temp / 10;
    }

    if (sum == n)
        printf("%d is an ARMSTRONG number\n", n);
    else
        printf("%d is NOT an Armstrong number\n", n);
    return 0;
}
''', ["153"],
       r"""<p>An <b>Armstrong number</b> equals the sum of its digits, each raised to the power of the number of digits.</p>
<p>153 → 3 digits → 1³ + 5³ + 3³ = 1 + 125 + 27 = 153 ✔. Other examples: 370, 371, 407, 1634.</p>
<p>The program uses a for loop to count digits, a while loop to extract digits, and a <b>nested</b> for loop to compute the power without <code>pow()</code>.</p>"""),

    PE("c2p15", "Star and number patterns (nested for)", r'''
#include <stdio.h>

int main(void)
{
    int n = 4, i, j;

    /* Pattern 1: right triangle of stars */
    for (i = 1; i <= n; i++)
    {
        for (j = 1; j <= i; j++)
            printf("* ");
        printf("\n");
    }
    printf("\n");

    /* Pattern 2: number pyramid */
    for (i = 1; i <= n; i++)
    {
        for (j = 1; j <= n - i; j++)    // leading spaces
            printf(" ");
        for (j = 1; j <= i; j++)
            printf("%d ", j);
        printf("\n");
    }
    return 0;
}
''', (),
       r"""<p>In a <b>nested loop</b> the outer loop controls the <b>rows</b> and the inner loop controls the <b>columns</b> (items in each row).</p>
<ul><li>Pattern 1: row <code>i</code> prints <code>i</code> stars.</li>
<li>Pattern 2: row <code>i</code> first prints <code>n - i</code> spaces, then the numbers 1 to <code>i</code>. Each number is followed by a space, which centres the pyramid.</li>
<li>Total inner iterations = 1 + 2 + … + n.</li></ul>"""),

    PE("c2p16", "Sum of positive numbers (break and continue)", r'''
#include <stdio.h>

int main(void)
{
    int i, n, sum = 0;

    printf("Enter up to 10 numbers (0 to stop):\n");
    for (i = 1; i <= 10; i++)
    {
        scanf("%d", &n);
        if (n == 0)
            break;              // leave the loop
        if (n < 0)
            continue;           // skip negative, go to i++
        sum = sum + n;
    }
    printf("Sum of positive numbers = %d\n", sum);
    return 0;
}
''', ["12", "-4", "7", "-9", "11", "0"],
       r"""<ul><li><code>break</code>: when 0 is entered the loop ends at once, even though <code>i</code> has not reached 10.</li>
<li><code>continue</code>: a negative number skips the rest of the body (<code>sum = sum + n</code>), and control jumps to the update <code>i++</code> of the for loop.</li>
<li>Sum = 12 + 7 + 11 = 30.</li></ul>"""),

    PE("c2p17", "Menu-driven program (do-while + switch)", r'''
#include <stdio.h>

int main(void)
{
    int choice, n, i;
    long f;

    do
    {
        printf("\n1. Square  2. Cube  3. Factorial  4. Exit\n");
        printf("Enter choice: ");
        scanf("%d", &choice);

        switch (choice)
        {
            case 1:
                printf("Enter n: ");  scanf("%d", &n);
                printf("Square = %d\n", n * n);
                break;
            case 2:
                printf("Enter n: ");  scanf("%d", &n);
                printf("Cube = %d\n", n * n * n);
                break;
            case 3:
                printf("Enter n: ");  scanf("%d", &n);
                for (f = 1, i = 1; i <= n; i++)
                    f = f * i;
                printf("Factorial = %ld\n", f);
                break;
            case 4:
                printf("Thank you!\n");
                break;
            default:
                printf("Invalid choice\n");
        }
    } while (choice != 4);
    return 0;
}
''', ["1", "6", "3", "5", "7", "4"],
       r"""<p>A <b>menu-driven</b> program shows the menu again and again until the user selects Exit. The menu has to appear at least once, so <b>do-while</b> is used. <b>switch</b> selects the action for each choice. The same structure is used for the GTU micro-projects (bank menu, calculator).</p>
<p>The for loop in case 3 uses the <b>comma operator</b> to initialize two variables: <code>f = 1, i = 1</code>.</p>"""),
]

if __name__ == "__main__":
    for p in PROGRAMS:
        print("=" * 20, p["id"], p["title"]["en"]); print(p["out"])
