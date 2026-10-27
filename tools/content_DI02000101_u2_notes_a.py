"""DI02000101 Unit 2 notes part A: 2.1 Operators and precedence."""
from py_content import make_TP

SN = {
    "expr": r'''
c = a + b          # a, b: operands   + : operator
total = (m1 + m2 + m3) / 3     # expression
''',
    "arith": r'''
a, b = 17, 5
a + b     # 22
a - b     # 12
a * b     # 85
a / b     # 3.4     (always float)
a // b    # 3       (floor division)
a % b     # 2       (remainder)
a ** b    # 1419857 (power)
-17 // 5  # -4      (rounds down)
''',
    "str_arith": r'''
"Py" + "thon"    # 'Python'   (concatenation)
"ab" * 3         # 'ababab'   (repetition)
[0] * 4          # [0, 0, 0, 0]
''',
    "cmp": r'''
10 == 10      # True
10 != 5       # True
"apple" < "banana"   # True (dictionary order)
5 < x < 15    # chained: 5 < x and x < 15
''',
    "logic": r'''
age, has_id = 19, True
age >= 18 and has_id     # True
age < 12 or age > 60     # False
not has_id               # False
0 or "default"           # 'default' (short-circuit)
''',
    "assign": r'''
x = 10
x += 5     # x = x + 5   -> 15
x -= 3     # x = x - 3   -> 12
x *= 2     # x = x * 2   -> 24
x /= 4     # x = x / 4   -> 6.0
x //= 2    # x = x // 2  -> 3.0
x **= 2    # x = x ** 2  -> 9.0
x %= 4     # x = x % 4   -> 1.0
''',
    "walrus": r'''
if (n := len(name)) > 10:
    print("Long name:", n)
''',
    "bit": r'''
a, b = 12, 10        # 1100, 1010
a & b     # 8   (1000)
a | b     # 14  (1110)
a ^ b     # 6   (0110)
~a        # -13 (-(a+1))
a << 2    # 48  (a * 4)
a >> 2    # 3   (a // 4)
''',
    "member": r'''
"Py" in "Python"          # True
3 in [1, 2, 3]            # True
"Java" not in ["C", "Py"] # True
"roll" in {"roll": 1}     # True (keys)
''',
    "ident": r'''
a = [1, 2, 3]
b = a
c = [1, 2, 3]
a == c        # True  (equal values)
a is b        # True  (same object)
a is c        # False (different objects)
x is None     # recommended None test
''',
    "prec_ex": r'''
2 + 3 * 4        # 14   (* first)
(2 + 3) * 4      # 20   (parentheses first)
2 ** 3 ** 2      # 512  (** right to left)
10 - 4 - 3       # 3    (left to right)
-3 ** 2          # -9   (** before unary -)
not 5 > 3 or 2 > 1   # True
''',
}
T = make_TP(SN)

SEC_2_1 = {
    "title": {"en": "2.1 Basic Operators"},
    "items": [
        T("2.1.1 Introduction to Operators",
          r"""<p>An <b>operator</b> is a symbol (or keyword) that performs an operation on values. The values it works on are called <b>operands</b>. A combination of operators and operands that produces a value is an <b>expression</b>.</p>
@@expr@@
<ul><li><b>Unary</b> operators work on one operand (<code>-x</code>, <code>not x</code>, <code>~x</code>); <b>binary</b> operators work on two (<code>a + b</code>).</li></ul>
<h4>Types of operators in Python (see diagram)</h4>
<ol><li>Arithmetic operators</li><li>Comparison (relational) operators</li><li>Logical operators</li><li>Assignment operators</li>
<li>Bitwise operators</li><li>Membership operators</li><li>Identity operators</li></ol>""",
          diagram="py2_operators"),

        T("2.1.2 Arithmetic Operators",
          r"""<table>
<tr><th>Operator</th><th>Meaning</th><th>Example (a = 17, b = 5)</th><th>Result</th></tr>
<tr><td>+</td><td>Addition</td><td>a + b</td><td>22</td></tr>
<tr><td>-</td><td>Subtraction</td><td>a - b</td><td>12</td></tr>
<tr><td>*</td><td>Multiplication</td><td>a * b</td><td>85</td></tr>
<tr><td>/</td><td>Division (true division)</td><td>a / b</td><td>3.4</td></tr>
<tr><td>//</td><td>Floor division</td><td>a // b</td><td>3</td></tr>
<tr><td>%</td><td>Modulus (remainder)</td><td>a % b</td><td>2</td></tr>
<tr><td>**</td><td>Exponent (power)</td><td>a ** b</td><td>1419857</td></tr>
</table>
@@arith@@
<ul><li><code>/</code> always returns a <b>float</b>, even for 10 / 2 = 5.0.</li>
<li><code>//</code> returns the largest integer ≤ the quotient, so it rounds <b>down</b> for negative numbers (−17 // 5 = −4).</li>
<li>If either operand is a float, the result is a float: 7 // 2.0 = 3.0.</li>
<li><code>+</code> and <code>*</code> also work on strings and lists:</li></ul>
@@str_arith@@""",
          programs=["py2p1"]),

        T("2.1.3 Comparison (Relational) Operators",
          r"""<p>Comparison operators compare two values and return a <b>Boolean</b> result (True or False).</p>
<table>
<tr><th>Operator</th><th>Meaning</th><th>Example (x = 10, y = 20)</th><th>Result</th></tr>
<tr><td>==</td><td>Equal to</td><td>x == y</td><td>False</td></tr>
<tr><td>!=</td><td>Not equal to</td><td>x != y</td><td>True</td></tr>
<tr><td>&gt;</td><td>Greater than</td><td>x &gt; y</td><td>False</td></tr>
<tr><td>&lt;</td><td>Less than</td><td>x &lt; y</td><td>True</td></tr>
<tr><td>&gt;=</td><td>Greater than or equal to</td><td>x &gt;= 10</td><td>True</td></tr>
<tr><td>&lt;=</td><td>Less than or equal to</td><td>y &lt;= 15</td><td>False</td></tr>
</table>
@@cmp@@
<ul><li>Strings are compared character by character using Unicode values ("A" &lt; "a").</li>
<li>Python supports <b>chained comparisons</b>, e.g. <code>0 &lt;= marks &lt;= 100</code>.</li>
<li>Do not confuse <code>=</code> (assignment) with <code>==</code> (comparison).</li></ul>""",
          programs=["py2p2"]),

        T("2.1.4 Logical Operators",
          r"""<p>Logical operators combine conditions. Python uses the <b>keywords</b> <code>and</code>, <code>or</code> and <code>not</code> (not &amp;&amp;, || and ! as in C).</p>
<table>
<tr><th>A</th><th>B</th><th>A and B</th><th>A or B</th><th>not A</th></tr>
<tr><td>True</td><td>True</td><td>True</td><td>True</td><td>False</td></tr>
<tr><td>True</td><td>False</td><td>False</td><td>True</td><td>False</td></tr>
<tr><td>False</td><td>True</td><td>False</td><td>True</td><td>True</td></tr>
<tr><td>False</td><td>False</td><td>False</td><td>False</td><td>True</td></tr>
</table>
@@logic@@
<h4>Short-circuit evaluation</h4>
<ul><li><code>A and B</code>: if A is false, B is not evaluated and the result is A; otherwise the result is B.</li>
<li><code>A or B</code>: if A is true, B is not evaluated and the result is A; otherwise the result is B.</li>
<li>Values like 0, "", [], {} and None are treated as <b>False</b> (falsy); all other values are True (truthy).</li></ul>""",
          programs=["py2p2"]),

        T("2.1.5 Assignment Operators",
          r"""<p>The assignment operator <code>=</code> stores the value of the right side in the variable on the left. <b>Compound assignment</b> operators combine an arithmetic or bitwise operation with assignment.</p>
<table>
<tr><th>Operator</th><th>Example</th><th>Same as</th></tr>
<tr><td>=</td><td>x = 5</td><td>x = 5</td></tr>
<tr><td>+=</td><td>x += 3</td><td>x = x + 3</td></tr>
<tr><td>-=</td><td>x -= 3</td><td>x = x - 3</td></tr>
<tr><td>*=</td><td>x *= 3</td><td>x = x * 3</td></tr>
<tr><td>/=</td><td>x /= 3</td><td>x = x / 3</td></tr>
<tr><td>//=</td><td>x //= 3</td><td>x = x // 3</td></tr>
<tr><td>%=</td><td>x %= 3</td><td>x = x % 3</td></tr>
<tr><td>**=</td><td>x **= 3</td><td>x = x ** 3</td></tr>
<tr><td>&amp;= |= ^= &lt;&lt;= &gt;&gt;=</td><td>x &amp;= 3</td><td>x = x &amp; 3</td></tr>
</table>
@@assign@@
<ul><li>Python has <b>no increment (++) or decrement (−−)</b> operators; use <code>x += 1</code> and <code>x -= 1</code>.</li>
<li>Multiple assignment: <code>a = b = 0</code>, <code>x, y = 1, 2</code>.</li>
<li><b>Walrus operator</b> <code>:=</code> (Python 3.8+) assigns a value inside an expression:</li></ul>
@@walrus@@""",
          programs=["py2p3"]),

        T("2.1.6 Bitwise Operators",
          r"""<p>Bitwise operators work on the <b>binary representation</b> of integers, bit by bit (see diagram).</p>
<table>
<tr><th>Operator</th><th>Name</th><th>Rule</th><th>12 op 10</th></tr>
<tr><td>&amp;</td><td>AND</td><td>1 if both bits are 1</td><td>8</td></tr>
<tr><td>|</td><td>OR</td><td>1 if any bit is 1</td><td>14</td></tr>
<tr><td>^</td><td>XOR</td><td>1 if the bits are different</td><td>6</td></tr>
<tr><td>~</td><td>NOT (complement)</td><td>inverts all bits: ~x = −(x+1)</td><td>~12 = −13</td></tr>
<tr><td>&lt;&lt;</td><td>Left shift</td><td>shifts bits left: × 2ⁿ</td><td>12 &lt;&lt; 2 = 48</td></tr>
<tr><td>&gt;&gt;</td><td>Right shift</td><td>shifts bits right: ÷ 2ⁿ</td><td>12 &gt;&gt; 2 = 3</td></tr>
</table>
@@bit@@
<p><b>Working (12 &amp; 10):</b> 1100 &amp; 1010 = 1000 = 8. <b>Uses:</b> checking even/odd (<code>n &amp; 1</code>), fast multiplication/division by powers of 2, setting/clearing flags, encryption. Use <code>bin()</code> to see the bits.</p>""",
          diagram="py2_bitwise", programs=["py2p4"]),

        T("2.1.7 Membership and Identity Operators",
          r"""<h4>Membership operators</h4>
<p>Test whether a value is present in a <b>sequence or collection</b> (string, list, tuple, set, dictionary).</p>
<table><tr><th>Operator</th><th>Returns True if</th><th>Example</th></tr>
<tr><td>in</td><td>value is found</td><td>"a" in "data" → True</td></tr>
<tr><td>not in</td><td>value is not found</td><td>5 not in [1, 2] → True</td></tr></table>
@@member@@
<h4>Identity operators</h4>
<p>Test whether two variables refer to the <b>same object</b> in memory (the same <code>id()</code>), see diagram.</p>
<table><tr><th>Operator</th><th>Returns True if</th><th>Example</th></tr>
<tr><td>is</td><td>both refer to the same object</td><td>a is b</td></tr>
<tr><td>is not</td><td>they refer to different objects</td><td>a is not c</td></tr></table>
@@ident@@
<table><tr><th>==</th><th>is</th></tr>
<tr><td>Compares <b>values</b></td><td>Compares <b>identity</b> (memory location)</td></tr>
<tr><td>[1,2] == [1,2] → True</td><td>[1,2] is [1,2] → False</td></tr></table>""",
          diagram="py2_identity", programs=["py2p5"]),

        T("2.1.8 Python Operator Precedence and Associativity",
          r"""<p>When an expression has several operators, <b>precedence</b> decides which is evaluated first. <b>Associativity</b> decides the order when operators have the same precedence.</p>
<table>
<tr><th>Precedence</th><th>Operators</th><th>Associativity</th></tr>
<tr><td>1 (highest)</td><td>( ) parentheses</td><td>–</td></tr>
<tr><td>2</td><td>** exponent</td><td><b>Right to left</b></td></tr>
<tr><td>3</td><td>+x, -x, ~x (unary)</td><td>Right to left</td></tr>
<tr><td>4</td><td>*, /, //, %</td><td>Left to right</td></tr>
<tr><td>5</td><td>+, -</td><td>Left to right</td></tr>
<tr><td>6</td><td>&lt;&lt;, &gt;&gt;</td><td>Left to right</td></tr>
<tr><td>7</td><td>&amp;</td><td>Left to right</td></tr>
<tr><td>8</td><td>^</td><td>Left to right</td></tr>
<tr><td>9</td><td>|</td><td>Left to right</td></tr>
<tr><td>10</td><td>==, !=, &gt;, &lt;, &gt;=, &lt;=, is, is not, in, not in</td><td>Left to right (chaining)</td></tr>
<tr><td>11</td><td>not</td><td>Right to left</td></tr>
<tr><td>12</td><td>and</td><td>Left to right</td></tr>
<tr><td>13</td><td>or</td><td>Left to right</td></tr>
<tr><td>14 (lowest)</td><td>=, +=, -=, … (assignment)</td><td>Right to left</td></tr>
</table>
@@prec_ex@@
<p><b>Solved example:</b> evaluate <code>a + b / c * 3 - 1</code> with a = 4, b = 8, c = 2.<br>
Step 1: b / c = 4.0 → Step 2: 4.0 * 3 = 12.0 → Step 3: 4 + 12.0 = 16.0 → Step 4: 16.0 − 1 = <b>15.0</b>.</p>
<p><b>Tip:</b> use parentheses to make complex expressions clear.</p>""",
          diagram="py2_precedence", programs=["py2p6"]),

        T("Key Points – 2.1",
          r"""<ul>
<li>7 types of operators: arithmetic, comparison, logical, assignment, bitwise, membership, identity.</li>
<li><code>/</code> gives a float; <code>//</code> is floor division; <code>%</code> remainder; <code>**</code> power.</li>
<li>Comparisons return True/False and can be chained: <code>a &lt; b &lt; c</code>.</li>
<li>Logical operators are the keywords and, or, not; they short-circuit.</li>
<li>Compound assignment: += -= *= /= //= %= **=; no ++/−− in Python.</li>
<li>Bitwise: &amp; | ^ ~ &lt;&lt; &gt;&gt;; ~x = −(x+1); &lt;&lt; n = × 2ⁿ.</li>
<li>in / not in check membership; is / is not check identity; == checks value.</li>
<li>Precedence: () → ** → unary → * / // % → + − → shifts → &amp; → ^ → | → comparisons → not → and → or. ** is right-associative.</li>
</ul>""", key=True),
    ],
}

NOTES_A = [SEC_2_1]
