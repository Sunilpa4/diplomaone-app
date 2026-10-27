"""DI03000021 Unit 2 notes part A: 2.1 stack, 2.2 expressions (infix/prefix/postfix), 2.3 recursion."""
from c_content import make_TE
from ds_expr import postfix_table, prefix_table, eval_postfix_table

SN = {
    "alg_push": r'''
Algorithm PUSH(STACK, TOP, MAX, ITEM)
Step 1: [Check overflow]
        If TOP = MAX - 1 then
            Write "Stack Overflow" and Exit
Step 2: Set TOP = TOP + 1
Step 3: Set STACK[TOP] = ITEM
Step 4: Exit
''',
    "alg_pop": r'''
Algorithm POP(STACK, TOP)
Step 1: [Check underflow]
        If TOP = -1 then
            Write "Stack Underflow" and Exit
Step 2: Set ITEM = STACK[TOP]
Step 3: Set TOP = TOP - 1
Step 4: Return ITEM
''',
    "alg_peek": r'''
Algorithm PEEK(STACK, TOP)
Step 1: If TOP = -1 then
            Write "Stack Empty" and Exit
Step 2: Return STACK[TOP]
''',
    "c_stack": r'''
#define MAX 5
int stack[MAX], top = -1;

void push(int x)
{
    if (top == MAX - 1)
        printf("Overflow");
    else
        stack[++top] = x;
}

int pop(void)
{
    if (top == -1) {
        printf("Underflow");
        return -1;
    }
    return stack[top--];
}
''',
    "alg_in2post": r'''
Algorithm INFIX_TO_POSTFIX(E)
Step 1: Scan E from left to right,
        one symbol at a time
Step 2: If symbol is an operand,
            add it to POSTFIX
Step 3: If symbol is '(' , PUSH it
Step 4: If symbol is ')' :
            POP and add to POSTFIX
            until '(' is found;
            discard the '('
Step 5: If symbol is an operator X:
            While top of stack has an
            operator of higher (or equal,
            except ^) precedence than X:
                POP it to POSTFIX
            PUSH X
Step 6: At the end, POP all remaining
        operators to POSTFIX
Step 7: Exit
''',
    "alg_evalpost": r'''
Algorithm EVAL_POSTFIX(P)
Step 1: Scan P from left to right
Step 2: If symbol is an operand,
            PUSH it
Step 3: If symbol is an operator op:
            B = POP   (2nd operand)
            A = POP   (1st operand)
            PUSH (A op B)
Step 4: Repeat Steps 2-3 till the end
Step 5: Result = POP
Step 6: Exit
''',
    "rec_form": r'''
type function(parameters)
{
    if (base condition)
        return value;         /* stop  */
    else
        return ... function(smaller);
}
''',
    "rec_fact": r'''
long fact(int n)
{
    if (n <= 1)               /* base case */
        return 1;
    return n * fact(n - 1);   /* recursive */
}
''',
    "rec_gcd": r'''
int gcd(int a, int b)
{
    if (b == 0)
        return a;
    return gcd(b, a % b);
}
''',
    "rec_fib": r'''
int fib(int n)
{
    if (n == 0) return 0;
    if (n == 1) return 1;
    return fib(n - 1) + fib(n - 2);
}
''',
}
T0 = make_TE(SN)


def T(h, b, examples=None, **kw):
    d = T0(h, b, **kw)
    if examples:
        d["examples"] = examples
    return d


P1, TAB1 = postfix_table("A+B*C-D/E")
PRE1, REV1, TABP = prefix_table("A+B*C-D/E")
V1, TABE = eval_postfix_table("5 3 + 8 2 - *".split())

SEC_2_1 = {
    "title": {"en": "2.1 Stack"},
    "items": [
        T("2.1.1 Introduction to Stack",
          r"""<p>A <b>stack</b> is a <b>linear data structure</b> in which insertion and deletion are done at <b>only one end</b>, called the <b>TOP</b>.</p>
<p>The element inserted <b>last</b> is removed <b>first</b>, so a stack follows the <b>LIFO (Last In, First Out)</b> principle. It is also called FILO (First In, Last Out).</p>
<h4>Real-life examples</h4>
<ul><li>A pile of plates: a plate is placed on top and also taken from the top.</li>
<li>A stack of books, or bangles on a stand.</li>
<li>Undo (Ctrl + Z) in an editor; the back button of a browser.</li></ul>
<h4>Terms</h4>
<ul><li><b>TOP:</b> a variable that holds the position (index) of the topmost element.</li>
<li><b>MAX:</b> the maximum number of elements the stack can hold (the array size).</li>
<li><b>PUSH:</b> inserting an element on the top.</li>
<li><b>POP:</b> removing the top element.</li>
<li><b>PEEK / TOP:</b> reading the top element without removing it.</li>
<li><b>Overflow:</b> trying to PUSH into a <b>full</b> stack (TOP = MAX − 1).</li>
<li><b>Underflow:</b> trying to POP from an <b>empty</b> stack (TOP = −1).</li></ul>
<p>A stack can be implemented using an <b>array</b> (static, fixed size) or a <b>linked list</b> (dynamic).</p>""",
          diagram="ds2_stack_array", key=True),

        T("2.1.2 Array Representation of Stack: PUSH and POP",
          r"""<p>In the array representation, a one-dimensional array <code>STACK[MAX]</code> holds the elements and an integer <code>TOP</code> holds the index of the top element.</p>
<ul><li>Initially <b>TOP = −1</b> (empty stack).</li>
<li>PUSH increases TOP and then stores the item; POP reads the item and then decreases TOP.</li></ul>
<h4>PUSH algorithm</h4>
@@alg_push@@
<h4>POP algorithm</h4>
@@alg_pop@@
<h4>PEEK algorithm</h4>
@@alg_peek@@
<h4>Implementation in C</h4>
@@c_stack@@
<ul><li><code>stack[++top] = x</code>: pre-increment, so TOP moves up first and then the value is stored.</li>
<li><code>return stack[top--]</code>: post-decrement, so the value is returned first and then TOP moves down.</li>
<li>PUSH, POP and PEEK all take <b>O(1)</b> time, because they do not depend on the number of elements.</li></ul>""",
          diagram="ds2_push_pop", programs=["ds2p1", "ds2p2"], examples=["ds2n10"], key=True),

        T("2.1.3 Applications of Stack",
          r"""<ol><li><b>Expression conversion:</b> infix to postfix and infix to prefix.</li>
<li><b>Expression evaluation:</b> evaluating postfix and prefix expressions.</li>
<li><b>Recursion:</b> every function call is pushed on the system (call) stack and popped when it returns.</li>
<li><b>Parenthesis matching:</b> checking that brackets ( ), [ ], { } are balanced in an expression or program.</li>
<li><b>Reversing:</b> a string, a number or a list (push all, then pop all).</li>
<li><b>Decimal to binary conversion:</b> remainders are pushed and popped in reverse order.</li>
<li><b>Undo / redo</b> in editors, and the <b>back button</b> in browsers.</li>
<li><b>Backtracking:</b> maze solving, depth-first search (DFS) of a graph.</li>
<li><b>Memory management:</b> local variables of functions are stored on the stack.</li></ol>""",
          diagram="ds2_stack_apps", programs=["ds2p3", "ds2p4", "ds2p13"]),
    ],
}

SEC_2_2 = {
    "title": {"en": "2.2 Infix, Prefix and Postfix Expressions"},
    "items": [
        T("2.2.1 Infix, Prefix and Postfix Forms",
          r"""<p>An arithmetic expression consists of <b>operands</b> (A, B, 5…) and <b>operators</b> (+, −, *, /, ^). Depending on where the operator is written, there are three notations:</p>
<table>
<tr><th>Notation</th><th>Form</th><th>Example</th></tr>
<tr><td><b>Infix</b></td><td>operand <b>operator</b> operand</td><td>A + B</td></tr>
<tr><td><b>Prefix</b> (Polish)</td><td><b>operator</b> operand operand</td><td>+ A B</td></tr>
<tr><td><b>Postfix</b> (Reverse Polish, suffix)</td><td>operand operand <b>operator</b></td><td>A B +</td></tr>
</table>
<p>Prefix notation was introduced by the Polish mathematician <b>Jan Łukasiewicz</b>, hence the name "Polish notation".</p>
<h4>Why postfix and prefix?</h4>
<ul><li>Infix needs <b>precedence rules</b> and <b>brackets</b> to show the order of evaluation: A + B * C is A + (B * C).</li>
<li>Postfix and prefix need <b>no brackets and no precedence rules</b>. The order of the operators itself gives the order of evaluation.</li>
<li>A postfix expression can be evaluated in a <b>single left-to-right scan</b> with a stack. Compilers therefore convert infix to postfix.</li></ul>
<h4>Precedence and associativity</h4>
<table>
<tr><th>Operator</th><th>Precedence</th><th>Associativity</th></tr>
<tr><td>^ (exponent)</td><td>Highest</td><td>Right to left</td></tr>
<tr><td>* / %</td><td>Middle</td><td>Left to right</td></tr>
<tr><td>+ −</td><td>Lowest</td><td>Left to right</td></tr>
</table>
<h4>Quick examples</h4>
<table>
<tr><th>Infix</th><th>Prefix</th><th>Postfix</th></tr>
<tr><td>A + B * C</td><td>+ A * B C</td><td>A B C * +</td></tr>
<tr><td>(A + B) * C</td><td>* + A B C</td><td>A B + C *</td></tr>
<tr><td>(A + B) * (C − D)</td><td>* + A B − C D</td><td>A B + C D − *</td></tr>
<tr><td>A ^ B ^ C</td><td>^ A ^ B C</td><td>A B C ^ ^</td></tr>
</table>""",
          diagram="ds2_notations", key=True),

        T("2.2.2 Conversion of Infix to Postfix using Stack",
          r"""<p>The stack holds <b>operators and '('</b>; operands go straight to the output.</p>
@@alg_in2post@@
<h4>Example: A + B * C − D / E</h4>
""" + TAB1 + r"""
<p><b>Postfix: """ + P1 + r"""</b></p>
<ul><li>At '−', the stack has '+' and '*', both of precedence ≥ '−', so both are popped before '−' is pushed.</li>
<li>For bigger expressions with brackets, see the solved examples below.</li></ul>""",
          programs=["ds2p5"], examples=["ds2n1", "ds2n2", "ds2n3", "ds2n4"], key=True),

        T("2.2.3 Conversion of Infix to Prefix",
          r"""<p>The easiest method is the <b>reverse method</b>:</p>
<ol><li><b>Reverse</b> the infix expression. While reversing, change every '(' into ')' and every ')' into '('.</li>
<li>Convert the reversed expression to postfix with the same stack method, with one change: for operators of <b>equal</b> precedence, do <b>not</b> pop (push the new operator on top). Exponent '^' is the exception: equal '^' <b>is</b> popped.</li>
<li><b>Reverse</b> the result to get the prefix expression.</li></ol>
<h4>Example: A + B * C − D / E</h4>
<p>Step 1, reversed infix: <b>""" + " ".join(REV1) + r"""</b></p>
<p>Step 2, convert:</p>
""" + TABP + r"""
<p>Step 3, reverse the output: <b>Prefix = """ + " ".join(PRE1) + r"""</b></p>
<p><b>Manual check (bracket method):</b> fully bracket by precedence: ((A + (B * C)) − (D / E)). Move each operator to the front of its own bracket: − + A * B C / D E. ✔</p>""",
          examples=["ds2n5", "ds2n6"]),

        T("2.2.4 Evaluation of Postfix Expression",
          r"""<p>A postfix expression is evaluated using a stack of <b>operands</b>, in a single left-to-right scan.</p>
@@alg_evalpost@@
<h4>Example: 5 3 + 8 2 − *</h4>
""" + TABE + r"""
<p><b>Result = """ + str(V1) + r"""</b>, which is (5 + 3) × (8 − 2).</p>
<p><b>Order matters:</b> the first value popped is the <b>right</b> operand. For "8 2 −", B = 2 and A = 8, so A − B = 6 (not −6).</p>
<h4>Evaluation of a prefix expression</h4>
<p>Same idea, but scan from <b>right to left</b>. For an operator, the first value popped is the <b>left</b> operand (A), the second is the right operand (B). Example: − * + 4 3 2 5 = (4 + 3) × 2 − 5 = <b>9</b>.</p>""",
          diagram="ds2_postfix_eval", programs=["ds2p6"], examples=["ds2n7", "ds2n8", "ds2n9"], key=True),
    ],
}

SEC_2_3 = {
    "title": {"en": "2.3 Recursion"},
    "items": [
        T("2.3.1 Recursive Functions and the Stack",
          r"""<p><b>Recursion</b> is a technique in which a <b>function calls itself</b>, directly or indirectly, to solve a smaller version of the same problem. Such a function is called a <b>recursive function</b>.</p>
<h4>Two essential parts</h4>
<ol><li><b>Base case</b> (terminating condition): a condition for which the answer is known directly, and the function does <b>not</b> call itself. Without it, recursion never ends and the program crashes with <b>stack overflow</b>.</li>
<li><b>Recursive case:</b> the function calls itself with a <b>smaller</b> input that moves towards the base case.</li></ol>
@@rec_form@@
<h4>How recursion uses the stack</h4>
<ul><li>Every call creates a new <b>activation record</b> (stack frame) holding its parameters, local variables and return address. The frame is <b>pushed</b> on the system stack.</li>
<li><b>Winding phase:</b> calls are made one after another until the base case is reached.</li>
<li><b>Unwinding phase:</b> each call returns its result to the caller, and its frame is <b>popped</b>.</li>
<li>Because the last call returns first, recursion is a natural application of <b>LIFO</b>.</li></ul>
<h4>Types</h4>
<ul><li><b>Direct recursion:</b> function A calls A.</li>
<li><b>Indirect recursion:</b> A calls B and B calls A.</li>
<li><b>Tail recursion:</b> the recursive call is the last statement (e.g. gcd).</li></ul>
<h4>Recursion vs iteration</h4>
<table>
<tr><th>Recursion</th><th>Iteration (loop)</th></tr>
<tr><td>Function calls itself</td><td>Loop repeats statements</td></tr>
<tr><td>Stops at the base case</td><td>Stops when the loop condition fails</td></tr>
<tr><td>Uses the system stack (more memory)</td><td>No extra stack memory</td></tr>
<tr><td>Slower (function-call overhead)</td><td>Faster</td></tr>
<tr><td>Short, elegant code for trees, Tower of Hanoi</td><td>Code may be longer</td></tr>
<tr><td>Missing base case → stack overflow</td><td>Wrong condition → infinite loop</td></tr>
</table>""",
          diagram="ds2_recursion_fact", key=True),

        T("2.3.2 Factorial using Recursion",
          r"""<p>Mathematical definition:</p>
<p style="text-align:center"><b>n! = 1</b> if n = 0 or 1 &nbsp;&nbsp;(base case)<br><b>n! = n × (n − 1)!</b> if n &gt; 1 &nbsp;&nbsp;(recursive case)</p>
@@rec_fact@@
<p><b>Trace for fact(4):</b></p>
<p>fact(4) = 4 × fact(3)<br>&nbsp;&nbsp;fact(3) = 3 × fact(2)<br>&nbsp;&nbsp;&nbsp;&nbsp;fact(2) = 2 × fact(1)<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;fact(1) = 1 (base case)<br>&nbsp;&nbsp;&nbsp;&nbsp;fact(2) = 2 × 1 = 2<br>&nbsp;&nbsp;fact(3) = 3 × 2 = 6<br>fact(4) = 4 × 6 = <b>24</b></p>
<p>Number of calls = n; time <b>O(n)</b>; stack space <b>O(n)</b>.</p>""",
          programs=["ds2p7"]),

        T("2.3.3 Greatest Common Divisor (GCD) using Recursion",
          r"""<p>Using <b>Euclid's algorithm</b>:</p>
<p style="text-align:center"><b>gcd(a, b) = a</b> if b = 0 &nbsp;&nbsp;(base case)<br><b>gcd(a, b) = gcd(b, a mod b)</b> otherwise</p>
@@rec_gcd@@
<p><b>Trace for gcd(48, 18):</b></p>
<table><tr><th>Call</th><th>a mod b</th></tr>
<tr><td>gcd(48, 18)</td><td>48 mod 18 = 12</td></tr>
<tr><td>gcd(18, 12)</td><td>18 mod 12 = 6</td></tr>
<tr><td>gcd(12, 6)</td><td>12 mod 6 = 0</td></tr>
<tr><td>gcd(6, 0)</td><td>b = 0 → return <b>6</b></td></tr></table>
<p>LCM can then be found as (a × b) / GCD = (48 × 18) / 6 = 144.</p>""",
          programs=["ds2p8"], examples=["ds2n13"]),

        T("2.3.4 Fibonacci Series using Recursion",
          r"""<p>The Fibonacci series is 0, 1, 1, 2, 3, 5, 8, 13, 21, 34 … Each term is the sum of the previous two.</p>
<p style="text-align:center"><b>fib(0) = 0, fib(1) = 1</b> &nbsp;&nbsp;(two base cases)<br><b>fib(n) = fib(n − 1) + fib(n − 2)</b> for n ≥ 2</p>
@@rec_fib@@
<p><b>Trace for fib(4):</b> fib(4) = fib(3) + fib(2) = (fib(2) + fib(1)) + (fib(1) + fib(0)) = ((1 + 0) + 1) + (1 + 0) = <b>3</b>.</p>
<ul><li>The recursion tree (diagram) shows that fib(2) is computed <b>twice</b>. For larger n the repetition explodes: fib(10) needs 177 calls.</li>
<li>Time complexity ≈ <b>O(2ⁿ)</b>; stack depth O(n).</li>
<li>An iterative loop (keeping the last two terms) needs only O(n) time.</li></ul>""",
          diagram="ds2_fib_tree", programs=["ds2p9"]),
    ],
}

NOTES_A = [SEC_2_1, SEC_2_2, SEC_2_3]
