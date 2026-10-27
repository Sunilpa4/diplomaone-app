"""DI01000131 Unit 4 notes part A: 4.1 Basics of user-defined functions, 4.2 Category of functions & passing arrays."""
from c_content import make_TE

SN = {
    "def_syn": r'''
return_type function_name(parameter list)   /* header */
{
    local variable declarations;            /* body   */
    executable statements;
    return expression;
}
''',
    "def_ex": r'''
float area(float l, float b)
{
    float a;
    a = l * b;
    return a;
}
''',
    "ret_forms": r'''
return;              /* no value (void function) */
return 0;            /* constant */
return x;            /* variable */
return (a + b);      /* expression */
return a * b;        /* parentheses optional */
''',
    "ret_multi": r'''
int sign(int n)
{
    if (n > 0)  return 1;
    if (n < 0)  return -1;
    return 0;            /* only one return executes */
}
''',
    "ret_void": r'''
void greet(void)
{
    printf("Hello\n");
}                        /* returns at closing brace */
''',
    "call_forms": r'''
line();                      /* no arguments */
s = add(5, 7);               /* value assigned */
printf("%d", add(a, b));     /* used in printf */
m = max(max(a, b), c);       /* nested call */
if (isPrime(n)) ...          /* used in condition */
t = add(a, b) * 2;           /* in expression */
''',
    "proto_syn": r'''
return_type function_name(type1 p1, type2 p2, ...);
''',
    "proto_ex": r'''
int   add(int a, int b);     /* with parameter names */
int   add(int, int);         /* names are optional */
void  line(void);            /* no parameters */
float area(float r);
''',
    "proto_place": r'''
#include <stdio.h>
int add(int, int);           /* global prototype */

int main(void)
{
    printf("%d", add(2, 3));
    return 0;
}

int add(int a, int b)        /* definition after main */
{
    return a + b;
}
''',
    "cat1": r'''
void message(void);          /* prototype */
...
message();                   /* call */
...
void message(void)           /* definition */
{
    printf("Welcome\n");
}
''',
    "cat2": r'''
void print_sum(int a, int b)
{
    printf("Sum = %d\n", a + b);
}
/* call: print_sum(4, 6); */
''',
    "cat3": r'''
int sum(int a, int b)
{
    return a + b;
}
/* call: s = sum(4, 6); */
''',
    "cat4": r'''
int get_number(void)
{
    int n;
    scanf("%d", &n);
    return n;
}
/* call: x = get_number(); */
''',
    "arr_1d": r'''
float average(int x[], int n);   /* prototype */
avg = average(a, n);             /* call: name only */

float average(int x[], int n)    /* definition */
{
    ...
}
''',
    "arr_elem": r'''
show(a[2]);          /* passes ONE element (by value) */
show_all(a, 5);      /* passes WHOLE array (address) */
''',
    "arr_2d": r'''
void display(int m[][3], int r); /* column size required */
display(mat, 2);                 /* call */
''',
}
T = make_TE(SN)

SEC_4_1 = {
    "title": {"en": "4.1 User-defined Functions – Basics"},
    "items": [
        T("4.1.1 Introduction and Need for Functions",
          r"""<p>A <b>function</b> is a <b>self-contained block of statements</b> that performs a specific, well-defined task. A C program is a collection of one or more functions, and execution always starts from <code>main()</code>.</p>
<h4>Types of functions (see diagram)</h4>
<ul><li><b>Library (built-in) functions:</b> already written and stored in the C library; declared in header files. E.g. <code>printf()</code>, <code>scanf()</code> (stdio.h), <code>sqrt()</code>, <code>pow()</code> (math.h), <code>strlen()</code> (string.h).</li>
<li><b>User-defined functions:</b> written by the programmer for a particular task, e.g. <code>sum()</code>, <code>fact()</code>. <code>main()</code> itself is a user-defined function.</li></ul>
<h4>Need for user-defined functions</h4>
<p>If a large program is written entirely in <code>main()</code>, it becomes too long and complex, and the same code may have to be repeated many times. Dividing it into functions solves these problems. This approach is called <b>modular</b> or <b>top-down programming</b>.</p>
<h4>Advantages</h4>
<ul><li><b>Modularity:</b> a big problem is divided into small, manageable modules.</li>
<li><b>Reusability:</b> a function is written once and called many times, even in other programs.</li>
<li><b>Avoids repetition</b> of code, so the program is shorter.</li>
<li><b>Easy debugging and testing:</b> each function can be tested separately.</li>
<li><b>Readability:</b> the program is easier to understand and maintain.</li>
<li><b>Teamwork:</b> different programmers can write different functions.</li></ul>""",
          diagram="c4_func_types"),

        T("4.1.2 Library Functions vs User-defined Functions",
          r"""<table>
<tr><th>Library functions</th><th>User-defined functions</th></tr>
<tr><td>Predefined in the C library</td><td>Written by the programmer</td></tr>
<tr><td>Declared in header files (stdio.h, math.h, …)</td><td>Declared by the programmer (prototype)</td></tr>
<tr><td>Header file must be included</td><td>No header needed (defined in the program)</td></tr>
<tr><td>Code cannot be modified</td><td>Code can be changed as required</td></tr>
<tr><td>Perform general tasks</td><td>Perform tasks specific to the program</td></tr>
<tr><td>e.g. printf(), sqrt(), strlen()</td><td>e.g. main(), sum(), fact()</td></tr>
</table>
<h4>Modular programming (see diagram)</h4>
<p>In top-down design, <code>main()</code> is at the top and calls functions such as read_data(), calculate() and display(); those functions may call further functions. Each module does one job, so the program is easy to develop and maintain.</p>""",
          diagram="c4_modular"),

        T("4.1.3 Elements of User-defined Functions",
          r"""<p>To use a user-defined function, three elements are needed (see diagram):</p>
<table>
<tr><th>Element</th><th>Purpose</th><th>Example</th></tr>
<tr><td><b>1. Function declaration</b> (prototype)</td><td>Tells the compiler the function's name, return type and parameter types before it is used</td><td><code>int sum(int, int);</code></td></tr>
<tr><td><b>2. Function call</b></td><td>Invokes (executes) the function, passing actual arguments</td><td><code>s = sum(10, 20);</code></td></tr>
<tr><td><b>3. Function definition</b></td><td>The actual code of the function: header and body</td><td><code>int sum(int a, int b) { return a + b; }</code></td></tr>
</table>
<p>If the definition is written <b>before</b> main(), a separate declaration is not required, because the definition also serves as the declaration.</p>""",
          diagram="c4_elements", programs=["c4p1"]),

        T("4.1.4 Definition of Functions",
          r"""<p>A <b>function definition</b> (function implementation) contains the code of the function. It has two parts: the <b>function header</b> and the <b>function body</b>.</p>
<h4>Syntax</h4>
@@def_syn@@
<h4>1. Function header</h4>
<ul><li><b>return_type:</b> the data type of the value the function returns (int, float, char, …). Use <code>void</code> if it returns nothing. (In old C, a missing type meant int; modern compilers require it.)</li>
<li><b>function_name:</b> any valid identifier, preferably describing the task (e.g. <code>area</code>, <code>isPrime</code>).</li>
<li><b>parameter list:</b> variables that receive values from the caller, called <b>formal parameters</b>. Each parameter needs its own type: <code>(int a, int b)</code>, not <code>(int a, b)</code>. Use <code>(void)</code> or <code>()</code> if there are none.</li>
<li>No semicolon after the header.</li></ul>
<h4>2. Function body</h4>
<p>Enclosed in braces; contains local variable declarations, statements that do the task, and a <code>return</code> statement (optional for void functions).</p>
<h4>Example</h4>
@@def_ex@@
<p><b>Note:</b> a function cannot be defined inside another function (no nested definitions in C).</p>"""),

        T("4.1.5 Return Values and their Types",
          r"""<p>A function can send a value back to the calling function using the <b>return</b> statement. The value is returned to the place where the function was called.</p>
<h4>Forms of return</h4>
@@ret_forms@@
<h4>Rules</h4>
<ul><li>A function can return <b>only one value</b> per call. (To return more, use pointers or arrays.)</li>
<li>The type of the returned value should match the <b>return type</b> in the header; otherwise it is converted automatically, e.g. returning 7.9 from an <code>int</code> function gives 7.</li>
<li><code>return</code> also <b>ends</b> the function immediately; statements after it are not executed.</li>
<li>A function may have <b>several return statements</b>, but only one is executed:</li></ul>
@@ret_multi@@
<h4>Types of return values</h4>
<ul><li><b>int, char, float, double, long, pointers</b> – any data type except arrays and functions.</li>
<li><b>void</b> – returns nothing. Control returns to the caller at the closing brace or at <code>return;</code></li></ul>
@@ret_void@@
<p>The calling function may <b>ignore</b> a returned value, e.g. <code>printf()</code> returns the number of characters printed, but we usually ignore it.</p>"""),

        T("4.1.6 Function Calls",
          r"""<p>A function is executed by <b>calling</b> it: write its name followed by a list of <b>actual arguments</b> in parentheses.</p>
<p><b>Syntax:</b> <code>function_name(argument list);</code> or <code>variable = function_name(argument list);</code></p>
<h4>What happens on a call (see diagram)</h4>
<ol><li>Execution of the calling function is suspended, and control is transferred to the called function.</li>
<li>The values of the actual arguments are copied into the formal parameters.</li>
<li>The body of the called function is executed.</li>
<li>When <code>return</code> (or the closing brace) is reached, control comes back to the calling function, with the returned value, and execution continues from the point of the call.</li></ol>
<h4>Different ways of calling</h4>
@@call_forms@@
<h4>Rules for actual arguments</h4>
<ul><li>The number, order and types of actual arguments must match the formal parameters.</li>
<li>Actual arguments can be constants, variables or expressions; formal parameters must be variables.</li>
<li>Actual and formal parameters may have the same or different names; they are separate variables.</li></ul>""",
          diagram="c4_call_flow"),

        T("4.1.7 Function Declaration (Prototype)",
          r"""<p>Like a variable, a function must be <b>declared before it is called</b>. A function declaration, also called a <b>function prototype</b>, tells the compiler the function's <b>return type, name, and number and types of parameters</b>.</p>
<h4>Syntax</h4>
@@proto_syn@@
<h4>Examples</h4>
@@proto_ex@@
<h4>Points to remember</h4>
<ul><li>A prototype ends with a <b>semicolon</b>; the definition header does not.</li>
<li>Parameter <b>names are optional</b> in a prototype; only the types are required.</li>
<li>The prototype must <b>match</b> the definition (return type, number and types of parameters).</li>
<li>With the prototype, the compiler can check every call for the correct number and types of arguments.</li>
<li>Not needed if the function is <b>defined before</b> it is called.</li>
<li><b>Global prototype:</b> placed above main(), so all functions can call it. <b>Local prototype:</b> placed inside a function, so only that function can call it.</li></ul>
@@proto_place@@"""),

        T("4.1.8 Actual vs Formal Parameters; Call by Value and Call by Reference",
          r"""<table>
<tr><th>Actual parameters (arguments)</th><th>Formal parameters</th></tr>
<tr><td>Written in the function <b>call</b></td><td>Written in the function <b>definition</b> header</td></tr>
<tr><td>Can be constants, variables or expressions</td><td>Must be variables (with types)</td></tr>
<tr><td>Belong to the calling function</td><td>Local to the called function</td></tr>
<tr><td>e.g. <code>sum(a, 5)</code></td><td>e.g. <code>int sum(int x, int y)</code></td></tr>
</table>
<h4>Methods of passing arguments (see diagram)</h4>
<table>
<tr><th>Call by value</th><th>Call by reference</th></tr>
<tr><td>A <b>copy of the value</b> of each actual argument is passed</td><td>The <b>address</b> of each actual argument is passed</td></tr>
<tr><td>Formal parameters are ordinary variables: <code>void f(int x)</code></td><td>Formal parameters are pointers: <code>void f(int *x)</code></td></tr>
<tr><td>Call: <code>f(a);</code></td><td>Call: <code>f(&amp;a);</code></td></tr>
<tr><td>Changes inside the function do <b>not</b> affect the original</td><td>Changes through <code>*x</code> <b>do</b> change the original</td></tr>
<tr><td>Safer; originals are protected</td><td>Can return many values; no copying of big data</td></tr>
<tr><td>Default method in C</td><td>Achieved using pointers; arrays are always passed this way</td></tr>
</table>""",
          diagram="c4_value_ref", programs=["c4p8", "c4p9"]),

        T("Key Points – 4.1",
          r"""<ul>
<li>Function = self-contained block doing one task. Types: <b>library</b> and <b>user-defined</b>.</li>
<li>Benefits: modularity, reusability, less repetition, easy debugging, readability.</li>
<li>Three elements: <b>declaration</b> (prototype; ends with ;), <b>call</b>, <b>definition</b> (header + body).</li>
<li>Header: <code>return_type name(type p1, type p2)</code> – each parameter needs a type.</li>
<li><code>return</code> sends back <b>one value</b> and ends the function; <code>void</code> = returns nothing.</li>
<li>Actual arguments (in the call) are copied into formal parameters (in the definition).</li>
<li>Call by value → copy, original safe. Call by reference → address (pointer), original can change.</li>
</ul>""", key=True),
    ],
}

SEC_4_2 = {
    "title": {"en": "4.2 Category of Functions and Passing Arrays"},
    "items": [
        T("4.2.1 Category of Functions – Overview",
          r"""<p>Depending on whether <b>arguments</b> are passed and whether a <b>value is returned</b>, user-defined functions are classified into four categories (see diagram):</p>
<table>
<tr><th>Category</th><th>Arguments</th><th>Return value</th><th>Prototype example</th></tr>
<tr><td>1. No arguments and no return values</td><td>No</td><td>No</td><td><code>void f(void);</code></td></tr>
<tr><td>2. Arguments but no return values</td><td>Yes</td><td>No</td><td><code>void f(int);</code></td></tr>
<tr><td>3. Arguments with return values</td><td>Yes</td><td>Yes</td><td><code>int f(int);</code></td></tr>
<tr><td>4. No arguments but returns a value</td><td>No</td><td>Yes</td><td><code>int f(void);</code></td></tr>
</table>
<p>Arguments carry data <b>into</b> the function (calling → called); the return value carries data <b>out</b> (called → calling).</p>""",
          diagram="c4_categories"),

        T("4.2.2 No Arguments and No Return Values",
          r"""<p>The function <b>does not receive</b> any data from the calling function and <b>does not return</b> any value. There is <b>no data communication</b> between the two functions; only control is transferred.</p>
@@cat1@@
<ul><li>The return type is <code>void</code> and the parameter list is <code>(void)</code>.</li>
<li>The function does its own input and output, if any.</li>
<li><b>Use:</b> printing messages, menus, lines, headings.</li></ul>""",
          programs=["c4p2"]),

        T("4.2.3 Arguments but No Return Values",
          r"""<p>The calling function <b>passes arguments</b> to the called function, but the called function <b>does not return</b> a value. This is <b>one-way</b> data communication.</p>
@@cat2@@
<ul><li>The return type is <code>void</code>; the parameter list contains formal parameters.</li>
<li>The result is usually <b>printed inside</b> the function, so the caller cannot use it in further calculations.</li>
<li><b>Use:</b> printing a table, displaying an array, printing a pattern of n rows.</li></ul>""",
          programs=["c4p3"]),

        T("4.2.4 Arguments with Return Values",
          r"""<p>The calling function <b>passes arguments</b>, and the called function <b>returns a value</b>. This is <b>two-way</b> data communication, and it is the <b>best and most used</b> category.</p>
@@cat3@@
<ul><li>The function only calculates; the caller decides what to do with the result (print it, store it, use it in an expression).</li>
<li>Such functions are the most reusable, e.g. <code>sqrt(x)</code>, <code>pow(x, y)</code>.</li>
<li><b>Use:</b> factorial, maximum, area, isPrime, GCD.</li></ul>""",
          programs=["c4p4", "c4p6", "c4p7"]),

        T("4.2.5 No Arguments but Returns a Value",
          r"""<p>The function <b>does not receive</b> any arguments, but it <b>returns a value</b> to the calling function. The function produces the data itself, typically by reading input.</p>
@@cat4@@
<ul><li>The return type is not void, and the parameter list is <code>(void)</code>.</li>
<li><b>Use:</b> reading and validating input, generating values; library examples: <code>getchar()</code>, <code>rand()</code>.</li></ul>
<h4>Comparison of the four categories</h4>
<table><tr><th>Category</th><th>Data in?</th><th>Data out?</th><th>Typical use</th></tr>
<tr><td>1</td><td>✗</td><td>✗</td><td>Messages, menus</td></tr>
<tr><td>2</td><td>✔</td><td>✗</td><td>Display/print results</td></tr>
<tr><td>3</td><td>✔</td><td>✔</td><td>Calculations</td></tr>
<tr><td>4</td><td>✗</td><td>✔</td><td>Reading input</td></tr></table>""",
          programs=["c4p5"]),

        T("4.2.6 Passing Arrays to Functions",
          r"""<h4>Passing a one-dimensional array</h4>
<p>To pass an entire array, write <b>only the array name</b> (without brackets) as the actual argument, together with its size. The formal parameter is declared with empty brackets.</p>
@@arr_1d@@
<ul><li>The array name is the <b>base address</b>, so the address is passed, not a copy of all elements (see diagram).</li>
<li>Arrays are therefore always passed by <b>reference</b>: changes made by the function affect the <b>original array</b>.</li>
<li>The size is not known inside the function, so it is passed as a separate argument.</li>
<li><code>int x[]</code> and <code>int *x</code> are equivalent as parameters.</li></ul>
<h4>Passing a single element vs the whole array</h4>
@@arr_elem@@
<h4>Passing a two-dimensional array</h4>
@@arr_2d@@
<ul><li>The <b>first dimension may be omitted</b>, but the <b>second (column) dimension must be specified</b>, so that the compiler can calculate element addresses.</li>
<li>The call uses only the array name.</li></ul>""",
          diagram="c4_pass_array", programs=["c4p10", "c4p11", "c4p12"]),

        T("Key Points – 4.2",
          r"""<ul>
<li>4 categories: (1) no args, no return; (2) args, no return; (3) args with return; (4) no args, returns value.</li>
<li><code>void</code> as return type = no return value; <code>(void)</code> as parameter list = no arguments.</li>
<li>Category 3 is the most flexible and reusable.</li>
<li>Pass an array by its <b>name only</b>: <code>f(a, n)</code>; parameter <code>int x[]</code>.</li>
<li>Arrays are passed by <b>address</b>, so the function can modify the original.</li>
<li>2-D parameter: <code>int m[][COLS]</code> – column size is compulsory.</li>
</ul>""", key=True),
    ],
}

NOTES_A = [SEC_4_1, SEC_4_2]
