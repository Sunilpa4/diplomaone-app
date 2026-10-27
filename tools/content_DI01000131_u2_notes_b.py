"""DI01000131 Unit 2 notes part B: 2.2 Decision Making and Looping (English only)."""
from c_content import make_TE

SN = {
    "while_syn": r'''
initialization;
while (test condition)
{
    body of the loop;
    update;
}
''',
    "while_ex": r'''
int i = 1;                /* initialization */
while (i <= 5)            /* test */
{
    printf("%d ", i);     /* body */
    i++;                  /* update */
}
/* Output: 1 2 3 4 5 */
''',
    "do_syn": r'''
initialization;
do
{
    body of the loop;
    update;
} while (test condition);
''',
    "do_ex": r'''
int i = 10;
do
{
    printf("%d ", i);
    i++;
} while (i <= 5);
/* Output: 10  (body runs once) */
''',
    "while_cmp": r'''
int i = 10;
while (i <= 5)
{
    printf("%d ", i);
    i++;
}
/* Output: nothing */
''',
    "for_syn": r'''
for (initialization; test condition; update)
{
    body of the loop;
}
''',
    "for_ex": r'''
for (i = 1; i <= 10; i++)
    printf("%d x %d = %d\n", n, i, n * i);
''',
    "for_var": r'''
/* 1. Counting down */
for (i = 10; i >= 1; i--)

/* 2. Step of 2 */
for (i = 0; i <= 20; i += 2)

/* 3. Comma: two variables */
for (i = 1, j = 10; i < j; i++, j--)

/* 4. Parts omitted */
i = 1;
for ( ; i <= 5; )
{
    printf("%d", i);
    i++;
}

/* 5. Infinite loop */
for ( ; ; )

/* 6. Empty body (time delay) */
for (i = 0; i < 1000; i++);
''',
    "nested_syn": r'''
for (i = 1; i <= 3; i++)        /* outer loop */
{
    for (j = 1; j <= 4; j++)    /* inner loop */
        printf("%d%d ", i, j);
    printf("\n");
}
''',
    "nested_out": r'''
11 12 13 14
21 22 23 24
31 32 33 34
''',
    "break_syn": r'''
while (test)
{
    .....
    if (condition)
        break;
    .....
}
statement after loop;
''',
    "continue_syn": r'''
for (init; test; update)
{
    .....
    if (condition)
        continue;
    .....
}
''',
    "bc_ex": r'''
for (i = 1; i <= 10; i++)
{
    if (i == 7)
        break;
    if (i % 2 == 0)
        continue;
    printf("%d ", i);
}
/* Output: 1 3 5 */
''',
    "infinite": r'''
while (1)
{
    scanf("%d", &n);
    if (n == 0)
        break;            /* the only way out */
    sum += n;
}
''',
}
T = make_TE(SN)

SEC_2_2 = {
    "title": {"en": "2.2 Decision Making and Looping"},
    "items": [
        T("2.2.1 Introduction to Looping",
          r"""<p><b>Looping</b> (iteration) means executing a group of statements <b>repeatedly</b> until a condition is satisfied. A program loop has two parts: the <b>body of the loop</b> and the <b>control statement</b>, which tests a condition and decides whether the body is executed again.</p>
<h4>Steps of a loop</h4>
<ol><li><b>Initialization</b> of the loop control variable (counter), e.g. <code>i = 1</code>.</li>
<li><b>Test</b> of a condition, e.g. <code>i &lt;= 10</code>.</li>
<li><b>Execution</b> of the body of the loop.</li>
<li><b>Update</b> (increment/decrement) of the counter, e.g. <code>i++</code>.</li></ol>
<h4>Types of loops by position of the test (see diagram)</h4>
<table>
<tr><th>Entry-controlled loop</th><th>Exit-controlled loop</th></tr>
<tr><td>Condition tested <b>before</b> the body</td><td>Condition tested <b>after</b> the body</td></tr>
<tr><td>Body may not run at all (0 times)</td><td>Body runs <b>at least once</b></td></tr>
<tr><td>Also called a pre-test loop</td><td>Also called a post-test loop</td></tr>
<tr><td><code>while</code>, <code>for</code></td><td><code>do-while</code></td></tr>
</table>
<h4>Types of loops by termination</h4>
<ul><li><b>Counter-controlled (definite) loop:</b> the number of repetitions is known in advance, e.g. print 1 to 10. A for loop is usually used.</li>
<li><b>Sentinel-controlled (indefinite) loop:</b> the number of repetitions is not known; the loop stops when a special value (<b>sentinel</b>), such as 0 or -1, is read. A while or do-while loop is usually used.</li></ul>
<p><b>Infinite loop:</b> if the condition never becomes false (e.g. the update is forgotten), the loop runs forever. Always make sure the condition eventually becomes false.</p>""",
          diagram="c2_loop_types"),

        T("2.2.2 The while Statement",
          r"""<p>The <b>while</b> loop is the simplest looping structure in C. It is an <b>entry-controlled</b> loop: the condition is tested first, and the body is executed only while the condition is true.</p>
<h4>Syntax</h4>
@@while_syn@@
<h4>Working</h4>
<ol><li>The test condition is evaluated.</li>
<li>If it is <b>true</b>, the body is executed, and control goes back to the condition.</li>
<li>This repeats until the condition becomes <b>false</b>; then control passes to the statement after the loop.</li></ol>
<h4>Example</h4>
@@while_ex@@
<ul><li>The body can be a single statement or a block in braces.</li>
<li>The update statement must be inside the body; otherwise the loop becomes infinite.</li>
<li>Do not put a semicolon after <code>while (condition)</code>: <code>while (i &lt;= 5);</code> creates an empty, possibly infinite, loop.</li>
<li>while is preferred when the number of iterations is <b>not known</b> in advance, e.g. processing the digits of a number (see the flowchart "Reverse of a Number").</li></ul>""",
          diagram="c2_fc_reverse", programs=["c2p9"]),

        T("2.2.3 The do Statement (do-while)",
          r"""<p>The <b>do-while</b> loop is an <b>exit-controlled</b> loop. The body is executed first and the condition is tested <b>at the end</b>. Therefore the body is always executed <b>at least once</b>, even if the condition is false at the start.</p>
<h4>Syntax</h4>
@@do_syn@@
<h4>Working</h4>
<ol><li>The body of the loop is executed.</li>
<li>The test condition is evaluated.</li>
<li>If it is true, control goes back to <code>do</code> and the body runs again; if false, the loop ends.</li></ol>
<h4>Example – body runs once even though the condition is false</h4>
@@do_ex@@
<p><b>Important:</b> a <b>semicolon is compulsory</b> after <code>while (condition)</code> in a do-while loop.</p>
<h4>Applications</h4>
<ul><li><b>Menu-driven programs:</b> the menu must be shown at least once.</li>
<li>Input validation, e.g. read a value again until it is valid.</li>
<li>Reading data until a sentinel value is entered.</li></ul>""",
          programs=["c2p10", "c2p17"]),

        T("2.2.4 Difference between while and do-while",
          r"""<table>
<tr><th>while</th><th>do-while</th></tr>
<tr><td><b>Entry-controlled</b> loop</td><td><b>Exit-controlled</b> loop</td></tr>
<tr><td>Condition is tested <b>before</b> executing the body</td><td>Condition is tested <b>after</b> executing the body</td></tr>
<tr><td>Body may execute <b>zero</b> times</td><td>Body executes <b>at least once</b></td></tr>
<tr><td>No semicolon after <code>while( )</code></td><td>Semicolon required: <code>} while (cond);</code></td></tr>
<tr><td>Syntax: <code>while (cond) { body }</code></td><td>Syntax: <code>do { body } while (cond);</code></td></tr>
<tr><td>Used when the body may not need to run at all</td><td>Used for menus and input validation</td></tr>
</table>
<h4>Same code, different output (i = 10)</h4>
@@while_cmp@@
@@do_ex@@"""),

        T("2.2.5 The for Statement",
          r"""<p>The <b>for</b> loop is an <b>entry-controlled</b> loop that gives a more <b>concise</b> loop structure: initialization, test and update are written together in one line. It is best for <b>counter-controlled</b> loops, where the number of iterations is known.</p>
<h4>Syntax</h4>
@@for_syn@@
<h4>Working (see flowchart)</h4>
<ol><li><b>Initialization</b> is executed only <b>once</b>, at the beginning.</li>
<li>The <b>test condition</b> is checked. If false, the loop ends.</li>
<li>If true, the <b>body</b> is executed.</li>
<li>The <b>update</b> expression is executed, and control goes back to step 2.</li></ol>
<h4>Example – multiplication table of n</h4>
@@for_ex@@
<h4>Additional features / variations of for loop</h4>
@@for_var@@
<ul><li>More than one variable can be initialized and updated using the <b>comma operator</b>.</li>
<li>Any of the three parts may be omitted, but the two <b>semicolons are compulsory</b>.</li>
<li>If the test is omitted, it is taken as <b>true</b> → infinite loop <code>for( ; ; )</code>, which is ended with <code>break</code>.</li>
<li>A semicolon right after <code>for( )</code> makes the body empty (a time-delay loop).</li></ul>""",
          diagram="c2_fc_for", programs=["c2p11", "c2p12"]),

        T("2.2.6 Nesting of Loops",
          r"""<p>A loop written <b>inside the body of another loop</b> is called a <b>nested loop</b>. For each iteration of the <b>outer loop</b>, the <b>inner loop</b> runs completely.</p>
@@nested_syn@@
<p><b>Output:</b></p>
@@nested_out@@
<ul><li>Total executions of the inner body = outer iterations × inner iterations = 3 × 4 = 12.</li>
<li>Any loop can be nested inside any other (for in while, while in for, etc.).</li>
<li>The inner and outer loops must use <b>different</b> control variables.</li>
<li><b>Applications:</b> patterns (outer = rows, inner = columns), 2D arrays/matrices (Unit 3), tables, sorting.</li></ul>""",
          programs=["c2p15", "c2p14"]),

        T("2.2.7 Comparison of while, do-while and for",
          r"""<table>
<tr><th>Feature</th><th>while</th><th>do-while</th><th>for</th></tr>
<tr><td>Type</td><td>Entry-controlled</td><td>Exit-controlled</td><td>Entry-controlled</td></tr>
<tr><td>Minimum executions</td><td>0</td><td>1</td><td>0</td></tr>
<tr><td>Initialization</td><td>Before the loop</td><td>Before the loop</td><td>Inside for( )</td></tr>
<tr><td>Update</td><td>Inside the body</td><td>Inside the body</td><td>Inside for( )</td></tr>
<tr><td>Semicolon after condition</td><td>No</td><td>Yes</td><td>Separates the 3 parts</td></tr>
<tr><td>Best used when</td><td>Iterations not known</td><td>Body must run at least once</td><td>Iterations known (counter)</td></tr>
<tr><td>Example</td><td>Reverse digits</td><td>Menu program</td><td>Factorial, tables</td></tr>
</table>
<h4>Same loop in three forms – print 1 to 5</h4>
<p><b>while</b></p>
<pre class="c">i = 1;
while (i &lt;= 5)
{
    printf("%d ", i);
    i++;
}</pre>
<p><b>do-while</b></p>
<pre class="c">i = 1;
do
{
    printf("%d ", i);
    i++;
} while (i &lt;= 5);</pre>
<p><b>for</b></p>
<pre class="c">for (i = 1; i &lt;= 5; i++)
    printf("%d ", i);</pre>"""),

        T("2.2.8 Jumps in Loops – break Statement",
          r"""<p>Sometimes a loop must be ended <b>before</b> its condition becomes false, e.g. when the searched item has been found. The <b>break</b> statement does this.</p>
<p><b>break:</b> when executed inside a loop (or switch), it <b>immediately terminates</b> the loop, and control passes to the <b>first statement after the loop</b>.</p>
<h4>Syntax and flow</h4>
@@break_syn@@
<ul><li>break is normally used with an <code>if</code> condition inside the loop.</li>
<li>In <b>nested loops</b>, break exits only the <b>innermost</b> loop that contains it.</li>
<li>In a <b>switch</b>, break exits the switch (prevents fall-through).</li>
<li>break is commonly used to end an <b>infinite loop</b>:</li></ul>
@@infinite@@
<p><b>exit() function:</b> <code>exit(0);</code> (header <code>&lt;stdlib.h&gt;</code>) terminates the <b>whole program</b>, not just the loop.</p>""",
          diagram="c2_break_continue", programs=["c2p13"]),

        T("2.2.9 Skipping a Part of Loop – continue Statement",
          r"""<p>The <b>continue</b> statement skips the <b>remaining statements</b> of the current iteration and starts the <b>next iteration</b> of the loop. It does not end the loop.</p>
<h4>Syntax</h4>
@@continue_syn@@
<ul><li>In <b>while / do-while</b>: control goes directly to the <b>test condition</b>.</li>
<li>In <b>for</b>: control goes to the <b>update</b> expression, then to the test.</li>
<li>continue can be used only inside loops, not in a switch alone.</li></ul>
<h4>Example using both</h4>
@@bc_ex@@
<p>Even numbers are skipped by <code>continue</code>; when i becomes 7, <code>break</code> ends the loop.</p>
<h4>Difference between break and continue</h4>
<table>
<tr><th>break</th><th>continue</th></tr>
<tr><td>Terminates the loop completely</td><td>Skips only the current iteration</td></tr>
<tr><td>Control goes to the statement after the loop</td><td>Control goes to the next iteration (test / update)</td></tr>
<tr><td>Used in loops <b>and switch</b></td><td>Used <b>only in loops</b></td></tr>
<tr><td>Keyword: <code>break;</code></td><td>Keyword: <code>continue;</code></td></tr>
<tr><td>e.g. stop when 0 is entered</td><td>e.g. skip negative numbers</td></tr>
</table>""",
          programs=["c2p16"]),

        T("Key Points – 2.2",
          r"""<ul>
<li>A loop has 4 steps: <b>initialization, test, body, update</b>.</li>
<li><b>Entry-controlled:</b> while, for (0 or more runs). <b>Exit-controlled:</b> do-while (at least 1 run).</li>
<li>Counter-controlled loop → iterations known (for). Sentinel-controlled → stops at a special value (while / do-while).</li>
<li><code>do { } while (cond);</code> – the semicolon is compulsory.</li>
<li><code>for (init; test; update)</code> – init runs once; any part can be omitted but both <code>;</code> must stay; <code>for(;;)</code> is infinite.</li>
<li>Nested loop: inner loop runs fully for every outer iteration (outer = rows, inner = columns).</li>
<li><b>break</b> exits the loop/switch; <b>continue</b> skips to the next iteration; <b>exit()</b> ends the program.</li>
</ul>""", key=True),
    ],
}

NOTES_B = [SEC_2_2]
