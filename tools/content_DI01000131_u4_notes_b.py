"""DI01000131 Unit 4 notes part B: 4.3 Recursion; Scope, Visibility and Lifetime of variables."""
from c_content import make_TE

SN = {
    "rec_syn": r'''
return_type fun(parameters)
{
    if (base condition)
        return value;            /* base case: no call */
    else
        return ... fun(smaller problem) ...;  /* recursive case */
}
''',
    "rec_fact": r'''
long fact(int n)
{
    if (n <= 1)
        return 1;
    return n * fact(n - 1);
}
''',
    "rec_inf": r'''
int f(int n)
{
    return n + f(n - 1);   /* no base case: never stops */
}
''',
    "rec_sum": r'''
int sum_digits(int n)
{
    if (n == 0)
        return 0;
    return (n % 10) + sum_digits(n / 10);
}
/* sum_digits(472) = 2 + 7 + 4 = 13 */
''',
    "auto": r'''
void f(void)
{
    int a;          /* same as: auto int a; */
    auto int b = 5;
}
''',
    "register": r'''
register int i;
for (i = 0; i < 1000; i++)
    ...
/* &i is not allowed for register variables */
''',
    "static": r'''
void count(void)
{
    static int c = 0;   /* initialized once */
    c++;
    printf("%d ", c);
}
/* 3 calls print: 1 2 3 */
''',
    "extern": r'''
#include <stdio.h>
int main(void)
{
    extern int total;   /* declaration: defined later */
    total = 50;
    printf("%d", total);
    return 0;
}
int total;              /* definition (global) */
''',
}
T = make_TE(SN)

SEC_4_3 = {
    "title": {"en": "4.3 Recursion; Scope, Visibility and Lifetime"},
    "items": [
        T("4.3.1 Recursion",
          r"""<p><b>Recursion</b> is a process in which a <b>function calls itself</b>, directly or indirectly. Such a function is called a <b>recursive function</b>. A problem is solved by reducing it to a smaller instance of the same problem.</p>
<h4>Two essential parts</h4>
<ul><li><b>Base case (terminating condition):</b> the simplest case, which is solved directly without a recursive call. It stops the recursion.</li>
<li><b>Recursive case:</b> the function calls itself with a <b>smaller</b> or simpler argument that moves towards the base case.</li></ul>
<h4>General form</h4>
@@rec_syn@@
<h4>Example: factorial</h4>
<p>n! = n × (n−1)! with 1! = 1 (and 0! = 1).</p>
@@rec_fact@@
<h4>How it works (see diagram)</h4>
<p>fact(4) calls fact(3), which calls fact(2), which calls fact(1). fact(1) returns 1 (base case). Then the pending calls finish in reverse order: fact(2) = 2 × 1 = 2, fact(3) = 3 × 2 = 6, fact(4) = 4 × 6 = 24. Each pending call is kept on the <b>stack</b> with its own copy of n.</p>
<h4>Without a base case</h4>
@@rec_inf@@
<p>The function calls itself forever, until the stack memory is exhausted (<b>stack overflow</b>) and the program crashes.</p>
<h4>Another example: sum of digits</h4>
@@rec_sum@@""",
          diagram="c4_recursion_fact", programs=["c4p13", "c4p15"]),

        T("4.3.2 Recursion vs Iteration",
          r"""<table>
<tr><th>Recursion</th><th>Iteration (loops)</th></tr>
<tr><td>Function calls itself</td><td>Statements are repeated using a loop</td></tr>
<tr><td>Ends at the <b>base case</b></td><td>Ends when the <b>loop condition</b> becomes false</td></tr>
<tr><td>Uses the stack for every call → more memory</td><td>Uses less memory</td></tr>
<tr><td>Slower (function-call overhead)</td><td>Faster</td></tr>
<tr><td>Code is short and elegant for naturally recursive problems</td><td>Code may be longer for such problems</td></tr>
<tr><td>Infinite recursion → stack overflow (crash)</td><td>Infinite loop → program hangs</td></tr>
<tr><td>e.g. factorial, Fibonacci, GCD, Tower of Hanoi, tree traversal</td><td>e.g. tables, sums, searching</td></tr>
</table>
<h4>Advantages of recursion</h4>
<ul><li>Short, clear code for problems defined recursively (factorial, Fibonacci, GCD, Tower of Hanoi).</li>
<li>Natural for data structures such as trees.</li></ul>
<h4>Disadvantages</h4>
<ul><li>More memory and time because of repeated calls.</li>
<li>May repeat the same calculations: fib(4) makes 9 calls and computes fib(2) twice (see diagram).</li>
<li>Harder to trace and debug; a missing base case causes a crash.</li></ul>""",
          diagram="c4_fib_tree", programs=["c4p14"]),

        T("4.3.3 Scope, Visibility and Lifetime of Variables",
          r"""<p>Every variable in C has three properties besides its data type:</p>
<ul><li><b>Scope:</b> the region of the program in which the variable can be used (is "known").</li>
<li><b>Visibility:</b> whether the variable can actually be accessed at a given point. A variable may be in scope but <b>hidden</b> by another variable with the same name in an inner block.</li>
<li><b>Lifetime (longevity):</b> how long the variable exists in memory and keeps its value during execution.</li></ul>
<h4>Types of scope (see diagram)</h4>
<table>
<tr><th>Scope</th><th>Declared</th><th>Accessible</th></tr>
<tr><td><b>Block (local) scope</b></td><td>Inside a function or a block <code>{ }</code></td><td>Only within that block, after its declaration</td></tr>
<tr><td><b>Function scope</b></td><td>Labels (for goto)</td><td>Anywhere in that function</td></tr>
<tr><td><b>File (global) scope</b></td><td>Outside all functions</td><td>From the declaration to the end of the file, in all functions</td></tr>
<tr><td><b>Function-prototype scope</b></td><td>Parameter names in a prototype</td><td>Only within the prototype</td></tr>
</table>
<h4>Local vs global variables</h4>
<table>
<tr><th>Local variable</th><th>Global variable</th></tr>
<tr><td>Declared inside a function/block</td><td>Declared outside all functions</td></tr>
<tr><td>Accessible only in that function/block</td><td>Accessible in all functions of the file</td></tr>
<tr><td>Created on entry, destroyed on exit</td><td>Exists for the whole program</td></tr>
<tr><td>Default value: garbage</td><td>Default value: 0</td></tr>
<tr><td>Safer: cannot be changed by other functions</td><td>Any function can change it (harder to debug)</td></tr>
</table>
<p>If a local and a global variable have the same name, the <b>local one hides</b> the global one inside its block.</p>""",
          diagram="c4_scope", programs=["c4p16"]),

        T("4.3.4 Storage Classes: auto, register, static, extern",
          r"""<p>A <b>storage class</b> decides where a variable is stored, its default initial value, its scope and its lifetime. C provides four storage classes:</p>
<table>
<tr><th>Storage class</th><th>Storage</th><th>Default value</th><th>Scope</th><th>Lifetime</th></tr>
<tr><td><b>auto</b></td><td>Memory (stack)</td><td>Garbage</td><td>Local to block</td><td>Till the block ends</td></tr>
<tr><td><b>register</b></td><td>CPU register (if available)</td><td>Garbage</td><td>Local to block</td><td>Till the block ends</td></tr>
<tr><td><b>static</b></td><td>Memory (data area)</td><td>Zero</td><td>Local to block (or file, if global)</td><td>Whole program; value persists between calls</td></tr>
<tr><td><b>extern</b></td><td>Memory (data area)</td><td>Zero</td><td>Global (whole program, all files)</td><td>Whole program</td></tr>
</table>
<h4>1. auto (automatic)</h4>
<p>The default storage class for local variables. Created when the block is entered and destroyed when it is left.</p>
@@auto@@
<h4>2. register</h4>
<p>Requests the compiler to keep the variable in a CPU register for <b>faster access</b>, e.g. loop counters. The compiler may ignore the request. The address operator <code>&amp;</code> cannot be used.</p>
@@register@@
<h4>3. static</h4>
<p>A static local variable is initialized <b>only once</b> and <b>retains its value</b> between function calls. A static global variable is visible only in its own file.</p>
@@static@@
<h4>4. extern (external)</h4>
<p>Global variables are external. The <code>extern</code> keyword <b>declares</b> a global variable that is <b>defined</b> elsewhere (later in the file or in another file); no new memory is allocated by the declaration.</p>
@@extern@@""",
          programs=["c4p17"]),

        T("Key Points – 4.3",
          r"""<ul>
<li>Recursion = function calling itself; needs a <b>base case</b> and a <b>recursive case</b> moving towards it.</li>
<li>Missing base case → infinite recursion → <b>stack overflow</b>.</li>
<li>Recursion: short code but more memory and time; iteration: faster, less memory.</li>
<li>Scope = where a variable is accessible; visibility = whether it is hidden; lifetime = how long it exists.</li>
<li>Local: inside a block, garbage default, dies at block end. Global: outside functions, default 0, lives for the whole program.</li>
<li>Storage classes: <b>auto</b> (default local), <b>register</b> (fast, no &amp;), <b>static</b> (keeps value between calls, default 0), <b>extern</b> (declares a global defined elsewhere).</li>
</ul>""", key=True),
    ],
}

NOTES_B = [SEC_4_3]
