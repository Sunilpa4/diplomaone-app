"""DI02000101 Unit 2 notes part B: 2.2 Decision making, 2.3 Loops and jump statements."""
from py_content import make_TP

SN = {
    "indent": r'''
if marks >= 35:
    print("Pass")            # block of if
    print("Well done")       # same block
print("End")                 # outside the block
''',
    "if_syn": r'''
if condition:
    statement(s)
''',
    "if_ex": r'''
age = int(input("Age: "))
if age >= 18:
    print("Eligible to vote")
''',
    "ifelse_syn": r'''
if condition:
    statement(s)       # when True
else:
    statement(s)       # when False
''',
    "ifelse_ex": r'''
n = int(input("n: "))
if n % 2 == 0:
    print("Even")
else:
    print("Odd")
''',
    "ternary": r'''
result = "Pass" if marks >= 35 else "Fail"
''',
    "elif_syn": r'''
if condition1:
    block1
elif condition2:
    block2
elif condition3:
    block3
else:
    default block
''',
    "elif_ex": r'''
if per >= 75:
    print("Distinction")
elif per >= 60:
    print("First Class")
elif per >= 35:
    print("Pass")
else:
    print("Fail")
''',
    "nested": r'''
if a >= b:
    if a >= c:
        print("a is largest")
    else:
        print("c is largest")
else:
    if b >= c:
        print("b is largest")
    else:
        print("c is largest")
''',
    "while_syn": r'''
initialization
while condition:
    statement(s)
    update
else:                  # optional
    statement(s)       # runs when condition is False
''',
    "while_ex": r'''
i = 1
while i <= 5:
    print(i, end=" ")      # 1 2 3 4 5
    i += 1
''',
    "while_inf": r'''
while True:
    s = input("Command (q to quit): ")
    if s == "q":
        break
''',
    "for_syn": r'''
for variable in sequence:
    statement(s)
else:                  # optional
    statement(s)       # runs after the last item
''',
    "for_ex": r'''
for ch in "GTU":                 # string
    print(ch)
for m in [78, 85, 62]:           # list
    print(m)
for k, v in {"a": 1}.items():    # dictionary
    print(k, v)
''',
    "range_ex": r'''
range(5)            # 0 1 2 3 4
range(2, 8)         # 2 3 4 5 6 7
range(1, 10, 2)     # 1 3 5 7 9
range(10, 0, -3)    # 10 7 4 1
list(range(4))      # [0, 1, 2, 3]

for i in range(1, 6):
    print(i * i, end=" ")   # 1 4 9 16 25
''',
    "break_ex": r'''
for i in range(1, 10):
    if i == 4:
        break
    print(i, end=" ")      # 1 2 3
''',
    "continue_ex": r'''
for i in range(1, 8):
    if i % 2 == 0:
        continue
    print(i, end=" ")      # 1 3 5 7
''',
    "loop_else": r'''
for i in range(2, n):
    if n % i == 0:
        print("Not prime")
        break
else:
    print("Prime")      # only if no break
''',
    "pass_ex": r'''
for i in range(5):
    pass               # loop body to be written later

def future_feature():
    pass               # empty function

if x > 0:
    pass               # nothing to do yet
else:
    print("Not positive")
''',
    "return_ex": r'''
def is_even(n):
    if n % 2 == 0:
        return True     # function ends here
    return False

print(is_even(10))      # True
''',
    "nested_ex": r'''
for i in range(1, 4):           # outer loop: rows
    for j in range(1, 4):       # inner loop: columns
        print(i * j, end="\t")
    print()
# 1  2  3
# 2  4  6
# 3  6  9
''',
}
T = make_TP(SN)

SEC_2_2 = {
    "title": {"en": "2.2 Control Flow: Decision Making"},
    "items": [
        T("2.2.1 Control Flow and the Concept of Indentation",
          r"""<p><b>Control flow</b> is the order in which the statements of a program are executed. There are three kinds of control structures:</p>
<ol><li><b>Sequential:</b> statements run one after another, top to bottom (the default).</li>
<li><b>Selection (decision making):</b> a block runs only when a condition is true: <code>if</code>, <code>if-else</code>, <code>if-elif-else</code>, nested if.</li>
<li><b>Iteration (looping):</b> a block is repeated: <code>while</code>, <code>for</code>.</li></ol>
<p><b>Jump statements</b> (<code>break</code>, <code>continue</code>, <code>pass</code>, <code>return</code>) change the normal flow.</p>
<h4>Indentation</h4>
<p>Python uses <b>indentation</b> instead of braces <code>{ }</code> to group statements into a <b>block (suite)</b>.</p>
<ul><li>A header line (<code>if</code>, <code>elif</code>, <code>else</code>, <code>while</code>, <code>for</code>, <code>def</code>) ends with a <b>colon :</b>.</li>
<li>All statements of the block are indented by the <b>same amount</b>; 4 spaces is standard (PEP 8).</li>
<li>The block ends when the indentation returns to the previous level.</li>
<li>Wrong or inconsistent indentation causes an <b>IndentationError</b>. Do not mix tabs and spaces.</li></ul>
@@indent@@"""),

        T("2.2.2 if Statement",
          r"""<p>The simple <b>if</b> statement executes a block <b>only when the condition is True</b>; otherwise the block is skipped (see the left flowchart).</p>
@@if_syn@@
@@if_ex@@
<ul><li>The condition can be any expression; non-zero numbers and non-empty values count as True.</li>
<li>A one-line form is allowed: <code>if x &gt; 0: print("Positive")</code>.</li></ul>""",
          diagram="py2_fc_ifelse"),

        T("2.2.3 if…else Statement",
          r"""<p>The <b>if…else</b> statement chooses between <b>two blocks</b>: the if block runs when the condition is True, and the else block runs when it is False. Exactly one of them always runs (see the right flowchart in 2.2.2).</p>
@@ifelse_syn@@
@@ifelse_ex@@
<h4>Conditional expression (ternary operator)</h4>
@@ternary@@
<p>Syntax: <code>value_if_true if condition else value_if_false</code>.</p>""",
          programs=["py2p7"]),

        T("2.2.4 if…elif…else Statement (Ladder)",
          r"""<p>Used when there are <b>more than two choices</b>. Conditions are tested <b>from top to bottom</b>; the block of the <b>first true condition</b> runs and the rest are skipped. If no condition is true, the <code>else</code> block (optional) runs (see diagram).</p>
@@elif_syn@@
@@elif_ex@@
<ul><li><code>elif</code> is short for "else if". Any number of elif parts may be used.</li>
<li>Python had no switch statement before 3.10, so the if-elif ladder is used for menus. (<code>match-case</code> exists from Python 3.10 but is not in the syllabus.)</li></ul>""",
          diagram="py2_fc_elif", programs=["py2p9", "py2p11"]),

        T("2.2.5 Nested if Statement",
          r"""<p>An <b>if statement placed inside another if or else block</b> is called a <b>nested if</b>. The inner condition is checked only when the outer condition allows it. Each level is indented further.</p>
@@nested@@
<p>Nested ifs can often be simplified using logical operators: <code>if a &gt;= b and a &gt;= c:</code>.</p>""",
          programs=["py2p8", "py2p10"]),

        T("Key Points – 2.2",
          r"""<ul>
<li>Control structures: sequential, selection (if) and iteration (loops).</li>
<li>Blocks are defined by a colon and consistent indentation (4 spaces).</li>
<li>if: runs a block only when the condition is True. if…else: one of two blocks.</li>
<li>if…elif…else: many choices; only the first true block runs.</li>
<li>Nested if: if inside if; can often be replaced by and/or.</li>
<li>Ternary: <code>x if cond else y</code>.</li>
</ul>""", key=True),
    ],
}

SEC_2_3 = {
    "title": {"en": "2.3 Loops and Jump Statements"},
    "items": [
        T("2.3.1 while Loop",
          r"""<p>The <b>while</b> loop repeats a block <b>as long as the condition is True</b>. The condition is checked <b>before</b> each iteration, so it is an <b>entry-controlled</b> loop; the body may not run even once (see diagram).</p>
@@while_syn@@
@@while_ex@@
<ul><li>The loop variable must be <b>initialized</b> before the loop and <b>updated</b> inside it. Otherwise the loop never ends (an infinite loop).</li>
<li>It is used when the number of iterations is <b>not known</b> in advance, e.g. processing digits or repeating until the user quits.</li>
<li>Python has <b>no do-while</b> loop; <code>while True</code> with <code>break</code> is used instead:</li></ul>
@@while_inf@@""",
          diagram="py2_fc_while", programs=["py2p12", "py2p15", "py2p18"]),

        T("2.3.2 for Loop",
          r"""<p>The <b>for</b> loop <b>iterates over the items of a sequence</b> (string, list, tuple, set, dictionary, range), taking one item at a time (see diagram).</p>
@@for_syn@@
@@for_ex@@
<ul><li>The number of iterations equals the number of items, so a for loop is used when the count is <b>known</b>.</li>
<li>There is no explicit condition or update; Python moves to the next item automatically.</li>
<li>Combined with <code>range()</code>, it works like the counting for loop of C.</li></ul>""",
          diagram="py2_fc_for"),

        T("2.3.3 range() Function",
          r"""<p><code>range()</code> generates a sequence of <b>integers</b>, mostly used with for loops (see diagram).</p>
<table>
<tr><th>Form</th><th>Generates</th><th>Example</th></tr>
<tr><td>range(stop)</td><td>0 to stop − 1</td><td>range(5) → 0 1 2 3 4</td></tr>
<tr><td>range(start, stop)</td><td>start to stop − 1</td><td>range(2, 6) → 2 3 4 5</td></tr>
<tr><td>range(start, stop, step)</td><td>start, start+step, … (before stop)</td><td>range(1, 10, 3) → 1 4 7</td></tr>
</table>
@@range_ex@@
<ul><li>The <b>stop value is never included</b>.</li>
<li>A negative step counts down: <code>range(10, 0, -1)</code> gives 10 to 1.</li>
<li>Arguments must be integers, and the step cannot be 0 (ValueError).</li>
<li>range() does not store all the numbers; it produces them as needed, so it uses little memory. Use <code>list(range(…))</code> to see them.</li></ul>""",
          diagram="py2_range", programs=["py2p13"]),

        T("2.3.4 Difference between while and for Loop",
          r"""<table>
<tr><th>while loop</th><th>for loop</th></tr>
<tr><td>Repeats while a condition is True</td><td>Repeats for each item of a sequence</td></tr>
<tr><td>Used when the number of iterations is unknown</td><td>Used when the number of iterations is known</td></tr>
<tr><td>Initialization and update written by the programmer</td><td>The next item is taken automatically</td></tr>
<tr><td>Risk of an infinite loop if the update is missed</td><td>Ends after the last item</td></tr>
<tr><td>while i &lt;= 10:</td><td>for i in range(1, 11):</td></tr>
<tr><td>e.g. reverse digits, menu until quit</td><td>e.g. tables, traversing a list</td></tr>
</table>
<p>Both loops can have an optional <code>else</code> block, and both support <code>break</code> and <code>continue</code>.</p>"""),

        T("2.3.5 break and continue Statements",
          r"""<h4>break</h4>
<p><code>break</code> <b>terminates the loop immediately</b>, and control goes to the first statement after the loop. In nested loops it exits only the innermost loop.</p>
@@break_ex@@
<h4>continue</h4>
<p><code>continue</code> <b>skips the remaining statements of the current iteration</b> and moves to the next iteration. In a while loop, make sure the update happens before <code>continue</code>.</p>
@@continue_ex@@
<h4>else with loops</h4>
<p>The <code>else</code> block of a loop runs only when the loop ends <b>normally</b> (not by break). It is useful for searching:</p>
@@loop_else@@
<table><tr><th>break</th><th>continue</th></tr>
<tr><td>Ends the whole loop</td><td>Skips only the current iteration</td></tr>
<tr><td>Control goes after the loop</td><td>Control goes to the next iteration</td></tr>
<tr><td>The loop's else is skipped</td><td>The loop's else still runs</td></tr></table>""",
          diagram="py2_break_continue", programs=["py2p14"]),

        T("2.3.6 pass and return Statements",
          r"""<h4>pass</h4>
<p><code>pass</code> is a <b>null statement</b>: it does nothing. Python does not allow an empty block, so <code>pass</code> is used as a <b>placeholder</b> where a statement is required but no action is needed yet.</p>
@@pass_ex@@
<h4>return</h4>
<p><code>return</code> is used <b>inside a function</b>. It ends the function immediately and sends a value back to the caller. Without a value, or without a return statement, a function returns <code>None</code>. A return inside a loop also ends the loop. Functions are covered in Unit 4.</p>
@@return_ex@@
<table><tr><th>pass</th><th>continue</th><th>break</th><th>return</th></tr>
<tr><td>Does nothing</td><td>Next iteration</td><td>Exits loop</td><td>Exits function with a value</td></tr></table>""",
          programs=["py2p16"]),

        T("2.3.7 Nesting of Loops",
          r"""<p>A loop placed inside another loop is a <b>nested loop</b>. For each iteration of the <b>outer loop</b>, the <b>inner loop runs completely</b>. If the outer loop runs m times and the inner loop n times, the inner body executes m × n times.</p>
@@nested_ex@@
<ul><li>Any combination is possible: for in for, while in for, etc.</li>
<li>Typical uses: patterns (rows × columns), multiplication tables, matrices, prime numbers in a range.</li>
<li><code>break</code> inside the inner loop exits only the inner loop.</li></ul>""",
          programs=["py2p17"]),

        T("Key Points – 2.3",
          r"""<ul>
<li>while: entry-controlled; repeats while the condition is True; needs initialization and update; no do-while in Python.</li>
<li>for: iterates over the items of a sequence; used with range() for counting.</li>
<li>range(start, stop, step): stop is excluded; default start 0, step 1; a negative step counts down.</li>
<li>break exits the loop; continue skips to the next iteration; pass does nothing; return exits a function.</li>
<li>A loop's else runs only if the loop was not ended by break.</li>
<li>Nested loops: the inner loop runs fully for each outer iteration (patterns, tables).</li>
</ul>""", key=True),
    ],
}

NOTES_B = [SEC_2_2, SEC_2_3]
