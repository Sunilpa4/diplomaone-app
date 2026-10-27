"""DI01000131 Unit 2 notes part A: 2.1 Decision Making and Branching (English only)."""
from c_content import make_TE

SN = {
    "if_syn": r'''
if (test expression)
{
    statement-block;
}
statement-x;
''',
    "if_ex": r'''
if (marks >= 40)
    printf("Pass\n");
printf("End\n");          /* always executed */
''',
    "semicolon_bug": r'''
if (a > b);               /* wrong: ; ends the if here */
    printf("a is big");   /* always printed */
''',
    "ifelse_syn": r'''
if (test expression)
{
    true-block statements;
}
else
{
    false-block statements;
}
statement-x;
''',
    "nested_syn": r'''
if (condition-1)
{
    if (condition-2)
        statement-1;
    else
        statement-2;
}
else
{
    statement-3;
}
statement-x;
''',
    "dangling": r'''
if (n > 0)
    if (a > b)
        z = a;
else                      /* pairs with if (a > b) */
    z = b;
''',
    "ladder_syn": r'''
if (condition-1)
    statement-1;
else if (condition-2)
    statement-2;
else if (condition-3)
    statement-3;
else
    default-statement;
statement-x;
''',
    "switch_syn": r'''
switch (expression)
{
    case value-1:
        block-1;
        break;
    case value-2:
        block-2;
        break;
    ......
    default:
        default-block;
}
statement-x;
''',
    "fallthrough": r'''
int n = 2;
switch (n)
{
    case 1: printf("One ");
    case 2: printf("Two ");     /* starts here */
    case 3: printf("Three ");   /* falls through */
            break;
    case 4: printf("Four ");
}
/* Output: Two Three */
''',
    "goto_syn": r'''
/* Forward jump */          /* Backward jump */
goto label;                 label:
.......                     .......
.......                     .......
label:                      goto label;
statement;
''',
    "goto_nested": r'''
for (i = 0; i < 10; i++)
    for (j = 0; j < 10; j++)
        if (a[i][j] == key)
            goto found;     /* exits both loops */
printf("Not found\n");
found:
printf("Found\n");
''',
}
T = make_TE(SN)

SEC_2_1 = {
    "title": {"en": "2.1 Decision Making and Branching"},
    "items": [
        T("2.1.1 Introduction – Control Statements",
          r"""<p>Normally the statements of a C program are executed <b>sequentially</b>, one after another, in the order in which they are written. In practice we often need to:</p>
<ul><li>execute a group of statements only when a condition is true,</li>
<li>choose one group out of several groups, or</li>
<li>repeat a group of statements many times.</li></ul>
<p>Statements that change the normal sequential order of execution are called <b>control statements</b>. Decision making statements are also called <b>branching</b> statements, because the program flow branches into different paths depending on a condition.</p>
<h4>Classification (see diagram)</h4>
<table>
<tr><th>Type</th><th>Statements</th><th>Purpose</th></tr>
<tr><td><b>Decision making / branching</b></td><td>if, if-else, nested if-else, else-if ladder, switch</td><td>Select statements depending on a condition</td></tr>
<tr><td><b>Looping / iteration</b></td><td>while, do-while, for</td><td>Repeat statements while a condition is true</td></tr>
<tr><td><b>Jump (unconditional)</b></td><td>goto, break, continue, return</td><td>Transfer control without testing a condition</td></tr>
</table>
<p>The <b>conditional operator</b> <code>?:</code> (Unit 1) is also a decision-making tool, used for simple two-way choices inside expressions.</p>""",
          diagram="c2_control_tree"),

        T("2.1.2 Decision Making with if Statement",
          r"""<p>The <b>if statement</b> is the most powerful and most used decision-making statement in C. It is a <b>two-way decision</b> statement and is used together with an expression:</p>
<p style="text-align:center"><code>if (test expression)</code></p>
<ul><li>The test expression is evaluated first.</li>
<li>In C, <b>any non-zero value is true</b> and <b>zero is false</b>. Relational and logical expressions give 1 (true) or 0 (false).</li>
<li>Depending on the value, control is transferred to a particular statement.</li></ul>
<h4>Forms of the if statement</h4>
<ol><li>Simple if statement</li><li>if-else statement</li><li>Nested if-else statement</li><li>else-if ladder</li></ol>
<h4>Valid test expressions</h4>
<table><tr><th>Expression</th><th>True when</th></tr>
<tr><td><code>if (a &gt; b)</code></td><td>a is greater than b</td></tr>
<tr><td><code>if (n % 2 == 0)</code></td><td>n is even</td></tr>
<tr><td><code>if (x &gt;= 10 &amp;&amp; x &lt;= 20)</code></td><td>x is between 10 and 20</td></tr>
<tr><td><code>if (n)</code></td><td>n is non-zero (same as <code>n != 0</code>)</td></tr>
<tr><td><code>if (!n)</code></td><td>n is zero</td></tr></table>
<p><b>Common mistake:</b> <code>if (a = 5)</code> <i>assigns</i> 5 to a; the value 5 is non-zero, so the condition is always true. For comparison, use <code>==</code>.</p>"""),

        T("2.1.3 Simple if Statement",
          r"""<p>The <b>simple if</b> statement executes a statement-block <b>only if</b> the test expression is true. If it is false, the block is skipped and execution continues with the next statement (statement-x).</p>
<h4>Syntax</h4>
@@if_syn@@
<ul><li>The statement-block may be a single statement or a group of statements enclosed in braces <code>{ }</code>.</li>
<li>Without braces, only the <b>first</b> statement after <code>if</code> belongs to it.</li>
<li>statement-x is executed in both cases (true and false).</li></ul>
<h4>Example</h4>
@@if_ex@@
<h4>Flow of control (see flowchart)</h4>
<p>Entry → test expression → if <b>true</b>: statement-block, then statement-x; if <b>false</b>: directly statement-x.</p>
<h4>Common error</h4>
@@semicolon_bug@@
<p>A semicolon right after <code>if ( )</code> forms an <b>empty statement</b>, so the printf is not controlled by the if.</p>""",
          diagram="c2_fc_if", programs=["c2p1"]),

        T("2.1.4 The if-else Statement",
          r"""<p>The <b>if-else</b> statement is an extension of the simple if. It executes one block when the expression is <b>true</b> and another block when it is <b>false</b>. In either case, <b>exactly one</b> of the two blocks is executed, never both.</p>
<h4>Syntax</h4>
@@ifelse_syn@@
<h4>Working</h4>
<ol><li>The test expression is evaluated.</li>
<li>If true (non-zero) → the true-block is executed.</li>
<li>If false (zero) → the false-block is executed.</li>
<li>Control then goes to statement-x.</li></ol>
<h4>Example</h4>
<pre class="c">if (n % 2 == 0)
    printf("Even");
else
    printf("Odd");</pre>
<p><b>Equivalent conditional operator:</b> <code>printf(n % 2 == 0 ? "Even" : "Odd");</code></p>
<h4>Rules</h4>
<ul><li><code>else</code> has no condition of its own and cannot be used without an <code>if</code>.</li>
<li>No semicolon is placed directly after <code>else</code>.</li>
<li>Use braces when a block has more than one statement.</li></ul>""",
          diagram="c2_fc_ifelse", programs=["c2p2", "c2p3"]),

        T("2.1.5 Nesting of if-else Statements",
          r"""<p>When an if-else statement is written <b>inside</b> another if or else block, it is called a <b>nested if-else</b>. It is used when a decision depends on a <b>series of conditions</b>.</p>
<h4>Syntax</h4>
@@nested_syn@@
<h4>Working</h4>
<ul><li>If condition-1 is <b>false</b> → statement-3 is executed.</li>
<li>If condition-1 is <b>true</b> → condition-2 is tested: if true → statement-1, otherwise → statement-2.</li>
<li>After any of these, control goes to statement-x.</li></ul>
<h4>Dangling else problem</h4>
<p>When braces are not used, an <code>else</code> is always paired with the <b>nearest preceding unmatched if</b>, whatever the indentation shows:</p>
@@dangling@@
<p>Here the <code>else</code> belongs to <code>if (a &gt; b)</code>, not to <code>if (n &gt; 0)</code>. To pair it with the outer if, enclose the inner if in braces. <b>Always use braces in nested ifs.</b></p>
<h4>Example application</h4>
<p>Largest of three numbers: first compare a and b, then compare the larger one with c.</p>""",
          diagram="c2_fc_nested", programs=["c2p4"]),

        T("2.1.6 The else-if Ladder",
          r"""<p>The <b>else-if ladder</b> is used for <b>multi-way decisions</b>, where one of many alternatives has to be selected. It is a chain of ifs in which the statement associated with each <code>else</code> is another <code>if</code>.</p>
<h4>Syntax</h4>
@@ladder_syn@@
<h4>Working</h4>
<ul><li>The conditions are evaluated <b>from top to bottom</b>.</li>
<li>As soon as a <b>true</b> condition is found, its statement is executed and control jumps to statement-x; <b>the rest of the ladder is skipped</b>.</li>
<li>If no condition is true, the final <code>else</code> (default-statement) is executed. The final else is optional.</li></ul>
<h4>Example: grade from marks</h4>
<pre class="c">if (m >= 70)       printf("Distinction");
else if (m >= 60)  printf("First class");
else if (m >= 50)  printf("Second class");
else if (m >= 40)  printf("Pass class");
else               printf("Fail");</pre>
<p><b>Order matters:</b> conditions must be arranged so that the first true one gives the correct result. If <code>m &gt;= 40</code> were written first, every passing student would get "Pass class".</p>""",
          diagram="c2_fc_ladder", programs=["c2p5"]),

        T("2.1.7 The switch Statement",
          r"""<p>The <b>switch</b> statement is a built-in <b>multi-way decision</b> statement. It tests the value of an expression against a list of <b>case values</b> (integer or character constants). When a match is found, the block of statements for that case is executed.</p>
<h4>Syntax</h4>
@@switch_syn@@
<h4>Working</h4>
<ol><li>The expression is evaluated; it must give an <b>integer</b> (or <code>char</code>) value.</li>
<li>The value is compared with value-1, value-2, … one by one.</li>
<li>When a match is found, execution starts from that case and continues until a <code>break</code> or the end of the switch.</li>
<li><code>break</code> transfers control out of the switch to statement-x.</li>
<li>If no case matches, the <code>default</code> block is executed. If there is no default, nothing is executed.</li></ol>
<h4>Rules of switch</h4>
<ul><li>The switch expression must be of <b>integral type</b> (int, char, short, long, enum). <b>float, double and strings are not allowed.</b></li>
<li>Case labels must be <b>constants</b> or constant expressions (e.g. <code>case 3+2:</code> is fine, <code>case x:</code> is not), and they must be <b>unique</b>.</li>
<li>Each case label ends with a <b>colon</b> ( : ).</li>
<li><code>break</code> is optional; without it control <b>falls through</b> to the next case.</li>
<li><code>default</code> is optional and may be placed anywhere, though usually it is last.</li>
<li>Ranges such as <code>case 1..10</code> are not allowed in standard C.</li>
<li>switch statements can be nested.</li></ul>
<h4>Fall-through example</h4>
@@fallthrough@@
<p>Fall-through is useful when several values need the same action (e.g. vowels a, e, i, o, u in one group).</p>""",
          diagram="c2_fc_switch", programs=["c2p6", "c2p7"]),

        T("2.1.8 Difference between switch and else-if Ladder",
          r"""<table>
<tr><th>switch</th><th>else-if ladder</th></tr>
<tr><td>Tests only <b>equality</b> of one expression with constant values.</td><td>Can test <b>any condition</b>: relational, logical, ranges.</td></tr>
<tr><td>Expression must be an integer or character.</td><td>Can use int, float, double, char, etc.</td></tr>
<tr><td>Case values must be constants.</td><td>Conditions may contain variables.</td></tr>
<tr><td>Cannot test ranges (e.g. marks 60–69) directly.</td><td>Ranges are easy: <code>m &gt;= 60 &amp;&amp; m &lt; 70</code>.</td></tr>
<tr><td>More readable for many fixed choices (menus).</td><td>Becomes long and complex for many choices.</td></tr>
<tr><td>Usually faster (the compiler may use a jump table).</td><td>Conditions are checked one by one.</td></tr>
<tr><td>Needs <code>break</code> to avoid fall-through.</td><td>No fall-through; only one block runs.</td></tr>
<tr><td>Uses the <code>default</code> case.</td><td>Uses the final <code>else</code>.</td></tr>
</table>
<p><b>Rule of thumb:</b> for a menu or fixed values (1, 2, 3 or '+', '-'), use <b>switch</b>; for ranges or complex conditions, use an <b>else-if ladder</b>.</p>"""),

        T("2.1.9 The goto Statement",
          r"""<p>The <b>goto</b> statement transfers control <b>unconditionally</b> to another statement in the same function. The destination is marked by a <b>label</b>: a valid identifier followed by a colon.</p>
<h4>Syntax</h4>
@@goto_syn@@
<ul><li><b>Forward jump:</b> the label is after the goto, so some statements are skipped.</li>
<li><b>Backward jump:</b> the label is before the goto, so statements are repeated, forming a loop.</li>
<li>The label must be in the <b>same function</b> as the goto.</li></ul>
<h4>Situation where goto is useful</h4>
<p>Exiting from deeply <b>nested loops</b> at once (a <code>break</code> exits only one loop):</p>
@@goto_nested@@
<h4>Why goto should be avoided</h4>
<ul><li>It makes the program logic hard to follow ("spaghetti code").</li>
<li>Programs become difficult to debug, test and maintain.</li>
<li>Any program using goto can be written with if, loops, break and continue. Structured programming discourages goto.</li></ul>""",
          programs=["c2p8"]),

        T("Key Points – 2.1",
          r"""<ul>
<li>Control statements change sequential flow: <b>decision</b> (if, switch), <b>loop</b> (while, do-while, for), <b>jump</b> (goto, break, continue, return).</li>
<li>Non-zero = true, zero = false. Use <code>==</code> for comparison, not <code>=</code>.</li>
<li>Simple if → block or nothing. if-else → exactly one of two blocks.</li>
<li>Nested if: an <b>else pairs with the nearest unmatched if</b> (dangling else); use braces.</li>
<li>else-if ladder: top to bottom; the first true condition wins, the rest are skipped.</li>
<li>switch: integer/char expression, constant and unique case labels, <code>break</code> prevents fall-through, <code>default</code> is optional.</li>
<li>goto label; – forward jump skips, backward jump repeats; avoid it except to exit nested loops.</li>
</ul>""", key=True),
    ],
}

NOTES_A = [SEC_2_1]
