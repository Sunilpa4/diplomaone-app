"""DI01000131 Unit 1 notes part C: 1.6 Operators and Expressions"""
from c_content import make_T

SN = {
    "shorthand": r'''
a += 5;     // a = a + 5
a -= 2;     // a = a - 2
a *= b + 1; // a = a * (b + 1)
a /= 4;     // a = a / 4
a %= 3;     // a = a % 3
''',
    "cond": r'''
max = (a > b) ? a : b;
printf("%s\n", (n % 2 == 0) ? "Even" : "Odd");
''',
    "comma": r'''
int a, b, c;
c = (a = 10, b = 20, a + b);     // c = 30
for (i = 0, j = 10; i < j; i++, j--)   // comma in for loop || for loop માં comma
    ;
''',
    "sizeof": r'''
int n;
printf("%zu", sizeof(n));       // 4 (on GCC) || 4 (GCC પર)
printf("%zu", sizeof(double));  // 8
''',
    "cast": r'''
int a = 7, b = 2;
float r1 = a / b;            // 3.000000 (integer division first) || 3.000000 (પહેલાં integer division)
float r2 = (float) a / b;    // 3.500000
int   k  = (int) 9.87;       // 9 (fraction truncated) || 9 (દશાંશ કપાય)
''',
}
T = make_T(SN)

SEC_1_6 = {
    "title": {"en": "1.6 Operators and Expressions", "gu": "1.6 Operators અને Expressions"},
    "items": [
        T("1.6.1 Introduction and Classification of Operators", "1.6.1 પરિચય અને Operators નું વર્ગીકરણ",
          r"""<p>An <b>operator</b> is a <b>symbol</b> that tells the computer to perform a mathematical or logical operation. The values on which it operates are called <b>operands</b>. An <b>expression</b> is a combination of operands and operators that gives a value, e.g. <code>a + b * 5</code>.</p>
<h4>Based on number of operands</h4>
<ul>
<li><b>Unary</b> – one operand: <code>-a, ++a, !x, sizeof(a)</code></li>
<li><b>Binary</b> – two operands: <code>a + b, a &gt; b, a &amp;&amp; b</code></li>
<li><b>Ternary</b> – three operands: <code>?:</code> (conditional operator)</li>
</ul>
<h4>Based on operation – 8 categories (see diagram)</h4>
<ol>
<li>Arithmetic operators: <code>+ - * / %</code></li>
<li>Relational operators: <code>&lt; &lt;= &gt; &gt;= == !=</code></li>
<li>Logical operators: <code>&amp;&amp; || !</code></li>
<li>Assignment operators: <code>= += -= *= /= %=</code></li>
<li>Increment and decrement operators: <code>++ --</code></li>
<li>Conditional operator: <code>? :</code></li>
<li>Bitwise operators: <code>&amp; | ^ ~ &lt;&lt; &gt;&gt;</code></li>
<li>Special operators: <code>, sizeof &amp; * . -&gt;</code></li>
</ol>""",
          r"""<p><b>Operator</b> એ computer ને ગાણિતિક અથવા logical operation કરવાનું કહેતું <b>symbol</b> છે. જેના પર operation થાય તે મૂલ્યોને <b>operands</b> કહે છે. <b>Expression</b> એ operands અને operators નું સંયોજન છે જે મૂલ્ય આપે છે, દા.ત. <code>a + b * 5</code>.</p>
<h4>Operands ની સંખ્યા પ્રમાણે</h4>
<ul>
<li><b>Unary</b> – એક operand: <code>-a, ++a, !x, sizeof(a)</code></li>
<li><b>Binary</b> – બે operands: <code>a + b, a &gt; b, a &amp;&amp; b</code></li>
<li><b>Ternary</b> – ત્રણ operands: <code>?:</code> (conditional operator)</li>
</ul>
<h4>Operation પ્રમાણે – 8 વર્ગો (આકૃતિ જુઓ)</h4>
<ol>
<li>Arithmetic operators: <code>+ - * / %</code></li>
<li>Relational operators: <code>&lt; &lt;= &gt; &gt;= == !=</code></li>
<li>Logical operators: <code>&amp;&amp; || !</code></li>
<li>Assignment operators: <code>= += -= *= /= %=</code></li>
<li>Increment અને decrement operators: <code>++ --</code></li>
<li>Conditional operator: <code>? :</code></li>
<li>Bitwise operators: <code>&amp; | ^ ~ &lt;&lt; &gt;&gt;</code></li>
<li>Special operators: <code>, sizeof &amp; * . -&gt;</code></li>
</ol>""",
          diagram="c1_operators"),

        T("1.6.2 Arithmetic Operators", "1.6.2 Arithmetic Operators",
          r"""<table>
<tr><th>Operator</th><th>Meaning</th><th>Example (a = 17, b = 5)</th><th>Result</th></tr>
<tr><td><code>+</code></td><td>Addition / unary plus</td><td><code>a + b</code></td><td>22</td></tr>
<tr><td><code>-</code></td><td>Subtraction / unary minus</td><td><code>a - b</code></td><td>12</td></tr>
<tr><td><code>*</code></td><td>Multiplication</td><td><code>a * b</code></td><td>85</td></tr>
<tr><td><code>/</code></td><td>Division</td><td><code>a / b</code></td><td>3</td></tr>
<tr><td><code>%</code></td><td>Modulo (remainder)</td><td><code>a % b</code></td><td>2</td></tr>
</table>
<h4>Types of arithmetic</h4>
<ul>
<li><b>Integer arithmetic:</b> both operands integers → result integer. Division <b>truncates</b> the fractional part: <code>5 / 2 = 2</code>, <code>-7 / 2 = -3</code>.</li>
<li><b>Real arithmetic:</b> both operands real → real result: <code>5.0 / 2.0 = 2.5</code>.</li>
<li><b>Mixed-mode arithmetic:</b> one integer and one real operand → the integer is converted to real and the result is real: <code>5 / 2.0 = 2.5</code>.</li>
</ul>
<h4>Modulus operator %</h4>
<ul>
<li>Works <b>only with integers</b> (not float/double; use <code>fmod()</code> for reals).</li>
<li>The sign of the result is the <b>sign of the first operand</b>: <code>-14 % 3 = -2</code>, <code>14 % -3 = 2</code>.</li>
<li>Uses: checking even/odd (<code>n % 2</code>), extracting digits (<code>n % 10</code>), divisibility.</li>
</ul>""",
          r"""<table>
<tr><th>Operator</th><th>અર્થ</th><th>ઉદાહરણ (a = 17, b = 5)</th><th>પરિણામ</th></tr>
<tr><td><code>+</code></td><td>સરવાળો / unary plus</td><td><code>a + b</code></td><td>22</td></tr>
<tr><td><code>-</code></td><td>બાદબાકી / unary minus</td><td><code>a - b</code></td><td>12</td></tr>
<tr><td><code>*</code></td><td>ગુણાકાર</td><td><code>a * b</code></td><td>85</td></tr>
<tr><td><code>/</code></td><td>ભાગાકાર</td><td><code>a / b</code></td><td>3</td></tr>
<tr><td><code>%</code></td><td>Modulo (શેષ)</td><td><code>a % b</code></td><td>2</td></tr>
</table>
<h4>Arithmetic ના પ્રકાર</h4>
<ul>
<li><b>Integer arithmetic:</b> બંને operands integers → પરિણામ integer. ભાગાકારમાં દશાંશ ભાગ <b>કપાઈ</b> જાય: <code>5 / 2 = 2</code>, <code>-7 / 2 = -3</code>.</li>
<li><b>Real arithmetic:</b> બંને operands real → real પરિણામ: <code>5.0 / 2.0 = 2.5</code>.</li>
<li><b>Mixed-mode arithmetic:</b> એક integer અને એક real operand → integer, real માં ફેરવાય અને પરિણામ real: <code>5 / 2.0 = 2.5</code>.</li>
</ul>
<h4>Modulus operator %</h4>
<ul>
<li><b>ફક્ત integers</b> સાથે કામ કરે (float/double નહીં; reals માટે <code>fmod()</code>).</li>
<li>પરિણામનું ચિહ્ન <b>પહેલા operand નું ચિહ્ન</b> હોય: <code>-14 % 3 = -2</code>, <code>14 % -3 = 2</code>.</li>
<li>ઉપયોગ: even/odd ચકાસવું (<code>n % 2</code>), અંકો કાઢવા (<code>n % 10</code>), વિભાજ્યતા.</li>
</ul>""",
          programs=["c1p9", "c1p10"]),

        T("1.6.3 Relational Operators", "1.6.3 Relational Operators",
          r"""<p><b>Relational operators</b> compare two values. The result of a relational expression is <b>1 (true)</b> or <b>0 (false)</b>. They are used in decision making (<code>if</code>) and loops.</p>
<table>
<tr><th>Operator</th><th>Meaning</th><th>Example (a = 10, b = 20)</th><th>Result</th></tr>
<tr><td><code>&lt;</code></td><td>less than</td><td><code>a &lt; b</code></td><td>1</td></tr>
<tr><td><code>&lt;=</code></td><td>less than or equal to</td><td><code>a &lt;= 10</code></td><td>1</td></tr>
<tr><td><code>&gt;</code></td><td>greater than</td><td><code>a &gt; b</code></td><td>0</td></tr>
<tr><td><code>&gt;=</code></td><td>greater than or equal to</td><td><code>b &gt;= 25</code></td><td>0</td></tr>
<tr><td><code>==</code></td><td>equal to</td><td><code>a == b</code></td><td>0</td></tr>
<tr><td><code>!=</code></td><td>not equal to</td><td><code>a != b</code></td><td>1</td></tr>
</table>
<p><b>Note:</b> <code>=</code> is assignment and <code>==</code> is comparison. Writing <code>if (a = 5)</code> instead of <code>if (a == 5)</code> is a common logical error. Arithmetic operators have higher priority than relational operators: <code>a + b &gt; c</code> means <code>(a + b) &gt; c</code>.</p>""",
          r"""<p><b>Relational operators</b> બે મૂલ્યોની સરખામણી કરે છે. Relational expression નું પરિણામ <b>1 (true)</b> અથવા <b>0 (false)</b> હોય છે. તેઓ decision making (<code>if</code>) અને loops માં વપરાય છે.</p>
<table>
<tr><th>Operator</th><th>અર્થ</th><th>ઉદાહરણ (a = 10, b = 20)</th><th>પરિણામ</th></tr>
<tr><td><code>&lt;</code></td><td>થી નાનું</td><td><code>a &lt; b</code></td><td>1</td></tr>
<tr><td><code>&lt;=</code></td><td>થી નાનું અથવા બરાબર</td><td><code>a &lt;= 10</code></td><td>1</td></tr>
<tr><td><code>&gt;</code></td><td>થી મોટું</td><td><code>a &gt; b</code></td><td>0</td></tr>
<tr><td><code>&gt;=</code></td><td>થી મોટું અથવા બરાબર</td><td><code>b &gt;= 25</code></td><td>0</td></tr>
<tr><td><code>==</code></td><td>બરાબર</td><td><code>a == b</code></td><td>0</td></tr>
<tr><td><code>!=</code></td><td>બરાબર નથી</td><td><code>a != b</code></td><td>1</td></tr>
</table>
<p><b>નોંધ:</b> <code>=</code> assignment છે અને <code>==</code> સરખામણી છે. <code>if (a == 5)</code> ની જગ્યાએ <code>if (a = 5)</code> લખવું સામાન્ય logical error છે. Arithmetic operators ની priority relational કરતાં વધુ છે: <code>a + b &gt; c</code> એટલે <code>(a + b) &gt; c</code>.</p>"""),

        T("1.6.4 Logical Operators", "1.6.4 Logical Operators",
          r"""<p><b>Logical operators</b> combine two or more conditions (relational expressions). The result is 1 (true) or 0 (false). In C, any <b>non-zero value is true</b> and <b>zero is false</b>.</p>
<table>
<tr><th>Operator</th><th>Meaning</th><th>Result is true when</th></tr>
<tr><td><code>&amp;&amp;</code></td><td>Logical AND</td><td>both conditions are true</td></tr>
<tr><td><code>||</code></td><td>Logical OR</td><td>at least one condition is true</td></tr>
<tr><td><code>!</code></td><td>Logical NOT</td><td>condition is false (reverses it)</td></tr>
</table>
<h4>Truth table</h4>
<table>
<tr><th>A</th><th>B</th><th>A &amp;&amp; B</th><th>A || B</th><th>!A</th></tr>
<tr><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td></tr>
<tr><td>0</td><td>1</td><td>0</td><td>1</td><td>1</td></tr>
<tr><td>1</td><td>0</td><td>0</td><td>1</td><td>0</td></tr>
<tr><td>1</td><td>1</td><td>1</td><td>1</td><td>0</td></tr>
</table>
<p><b>Examples:</b> <code>(marks &gt;= 35) &amp;&amp; (marks &lt;= 100)</code>; <code>(ch == 'y') || (ch == 'Y')</code>; <code>!(n % 2)</code> is true for even n.</p>
<p><b>Short-circuit evaluation:</b> in <code>A &amp;&amp; B</code>, if A is false, B is not evaluated; in <code>A || B</code>, if A is true, B is not evaluated.</p>""",
          r"""<p><b>Logical operators</b> બે અથવા વધુ શરતો (relational expressions) ને જોડે છે. પરિણામ 1 (true) અથવા 0 (false) હોય. C માં કોઈપણ <b>શૂન્ય સિવાયનું મૂલ્ય true</b> અને <b>શૂન્ય false</b> છે.</p>
<table>
<tr><th>Operator</th><th>અર્થ</th><th>પરિણામ true ક્યારે</th></tr>
<tr><td><code>&amp;&amp;</code></td><td>Logical AND</td><td>બંને શરતો સાચી હોય</td></tr>
<tr><td><code>||</code></td><td>Logical OR</td><td>ઓછામાં ઓછી એક શરત સાચી હોય</td></tr>
<tr><td><code>!</code></td><td>Logical NOT</td><td>શરત ખોટી હોય (ઉલટાવે)</td></tr>
</table>
<h4>Truth table</h4>
<table>
<tr><th>A</th><th>B</th><th>A &amp;&amp; B</th><th>A || B</th><th>!A</th></tr>
<tr><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td></tr>
<tr><td>0</td><td>1</td><td>0</td><td>1</td><td>1</td></tr>
<tr><td>1</td><td>0</td><td>0</td><td>1</td><td>0</td></tr>
<tr><td>1</td><td>1</td><td>1</td><td>1</td><td>0</td></tr>
</table>
<p><b>ઉદાહરણ:</b> <code>(marks &gt;= 35) &amp;&amp; (marks &lt;= 100)</code>; <code>(ch == 'y') || (ch == 'Y')</code>; even n માટે <code>!(n % 2)</code> true છે.</p>
<p><b>Short-circuit evaluation:</b> <code>A &amp;&amp; B</code> માં A false હોય તો B evaluate થતું નથી; <code>A || B</code> માં A true હોય તો B evaluate થતું નથી.</p>""",
          programs=["c1p11"]),

        T("1.6.5 Assignment Operators", "1.6.5 Assignment Operators",
          r"""<p>The <b>assignment operator =</b> assigns the value of the expression on the right to the variable on the left: <code>variable = expression;</code></p>
<p>C also has <b>shorthand (compound) assignment operators</b> of the form <code>v op= exp;</code> which is the same as <code>v = v op (exp);</code></p>
@@shorthand@@
<table>
<tr><th>Simple assignment</th><th>Shorthand</th></tr>
<tr><td><code>a = a + 1</code></td><td><code>a += 1</code></td></tr>
<tr><td><code>a = a - 1</code></td><td><code>a -= 1</code></td></tr>
<tr><td><code>a = a * (n + 1)</code></td><td><code>a *= n + 1</code></td></tr>
<tr><td><code>a = a / (n + 1)</code></td><td><code>a /= n + 1</code></td></tr>
<tr><td><code>a = a % b</code></td><td><code>a %= b</code></td></tr>
</table>
<h4>Advantages of shorthand operators</h4>
<ul><li>Left-hand variable is written only once – less typing.</li>
<li>Statement is more concise and easier to read.</li>
<li>More efficient.</li></ul>
<p><b>Multiple assignment:</b> <code>a = b = c = 0;</code> (right-to-left associativity).</p>""",
          r"""<p><b>Assignment operator =</b> જમણી બાજુના expression નું મૂલ્ય ડાબી બાજુના variable ને આપે છે: <code>variable = expression;</code></p>
<p>C માં <code>v op= exp;</code> સ્વરૂપના <b>shorthand (compound) assignment operators</b> પણ છે, જે <code>v = v op (exp);</code> બરાબર છે.</p>
@@shorthand@@
<table>
<tr><th>Simple assignment</th><th>Shorthand</th></tr>
<tr><td><code>a = a + 1</code></td><td><code>a += 1</code></td></tr>
<tr><td><code>a = a - 1</code></td><td><code>a -= 1</code></td></tr>
<tr><td><code>a = a * (n + 1)</code></td><td><code>a *= n + 1</code></td></tr>
<tr><td><code>a = a / (n + 1)</code></td><td><code>a /= n + 1</code></td></tr>
<tr><td><code>a = a % b</code></td><td><code>a %= b</code></td></tr>
</table>
<h4>Shorthand operators ના ફાયદા</h4>
<ul><li>ડાબી બાજુનો variable એક જ વાર લખાય – ઓછું typing.</li>
<li>Statement ટૂંકું અને વાંચવામાં સરળ.</li>
<li>વધુ કાર્યક્ષમ.</li></ul>
<p><b>Multiple assignment:</b> <code>a = b = c = 0;</code> (right-to-left associativity).</p>"""),

        T("1.6.6 Increment and Decrement Operators", "1.6.6 Increment અને Decrement Operators",
          r"""<p><code>++</code> adds 1 to the operand and <code>--</code> subtracts 1. They are <b>unary</b> operators and work only on variables (not constants: <code>5++</code> is invalid).</p>
<table>
<tr><th>Form</th><th>Name</th><th>Meaning</th></tr>
<tr><td><code>++a</code></td><td>Pre-increment (prefix)</td><td>First increment a, then use the new value</td></tr>
<tr><td><code>a++</code></td><td>Post-increment (postfix)</td><td>First use the current value, then increment</td></tr>
<tr><td><code>--a</code></td><td>Pre-decrement</td><td>First decrement, then use</td></tr>
<tr><td><code>a--</code></td><td>Post-decrement</td><td>First use, then decrement</td></tr>
</table>
<p>When used alone (<code>a++;</code> or <code>++a;</code>) both forms give the same result. The difference appears in expressions:</p>
<ul>
<li><code>a = 5; b = ++a;</code> → a = 6, b = 6</li>
<li><code>a = 5; b = a++;</code> → a = 6, b = 5</li>
</ul>
<p><b>Caution:</b> do not use the same variable with ++/-- more than once in one expression (e.g. <code>a++ + ++a</code>) – the result is <b>undefined</b> and differs between compilers.</p>""",
          r"""<p><code>++</code> operand માં 1 ઉમેરે અને <code>--</code> 1 બાદ કરે. તેઓ <b>unary</b> operators છે અને ફક્ત variables પર કામ કરે (constants પર નહીં: <code>5++</code> invalid).</p>
<table>
<tr><th>સ્વરૂપ</th><th>નામ</th><th>અર્થ</th></tr>
<tr><td><code>++a</code></td><td>Pre-increment (prefix)</td><td>પહેલાં a વધારો, પછી નવું મૂલ્ય વાપરો</td></tr>
<tr><td><code>a++</code></td><td>Post-increment (postfix)</td><td>પહેલાં હાલનું મૂલ્ય વાપરો, પછી વધારો</td></tr>
<tr><td><code>--a</code></td><td>Pre-decrement</td><td>પહેલાં ઘટાડો, પછી વાપરો</td></tr>
<tr><td><code>a--</code></td><td>Post-decrement</td><td>પહેલાં વાપરો, પછી ઘટાડો</td></tr>
</table>
<p>એકલા વાપરતાં (<code>a++;</code> અથવા <code>++a;</code>) બંને સ્વરૂપ સરખું પરિણામ આપે. તફાવત expressions માં દેખાય:</p>
<ul>
<li><code>a = 5; b = ++a;</code> → a = 6, b = 6</li>
<li><code>a = 5; b = a++;</code> → a = 6, b = 5</li>
</ul>
<p><b>સાવધાની:</b> એક જ expression માં એક જ variable સાથે ++/-- એક કરતાં વધુ વાર ન વાપરો (દા.ત. <code>a++ + ++a</code>) – પરિણામ <b>undefined</b> છે અને compilers પ્રમાણે બદલાય.</p>""",
          programs=["c1p12"]),

        T("1.6.7 Conditional Operator", "1.6.7 Conditional Operator",
          r"""<p>The <b>conditional operator ?:</b> is the only <b>ternary operator</b> in C (three operands). It is a short form of a simple <code>if…else</code>.</p>
<p><b>Syntax:</b> <code>exp1 ? exp2 : exp3</code></p>
<p><code>exp1</code> is evaluated first. If it is <b>true (non-zero)</b>, <code>exp2</code> is evaluated and becomes the value of the whole expression; otherwise <code>exp3</code> is evaluated.</p>
@@cond@@
<p>Equivalent <code>if…else</code>: <code>if (a &gt; b) max = a; else max = b;</code></p>
<p>It can be <b>nested</b> to find the largest of three numbers (see program), but deep nesting reduces readability.</p>""",
          r"""<p><b>Conditional operator ?:</b> એ C નો એકમાત્ર <b>ternary operator</b> (ત્રણ operands) છે. તે સાદા <code>if…else</code> નું ટૂંકું સ્વરૂપ છે.</p>
<p><b>Syntax:</b> <code>exp1 ? exp2 : exp3</code></p>
<p>પહેલાં <code>exp1</code> evaluate થાય. તે <b>true (non-zero)</b> હોય તો <code>exp2</code> evaluate થઈ આખા expression નું મૂલ્ય બને; નહીં તો <code>exp3</code> evaluate થાય.</p>
@@cond@@
<p>સમકક્ષ <code>if…else</code>: <code>if (a &gt; b) max = a; else max = b;</code></p>
<p>ત્રણ સંખ્યાઓમાં સૌથી મોટી શોધવા તેને <b>nested</b> કરી શકાય (program જુઓ), પણ વધુ nesting વાંચવાનું અઘરું બનાવે.</p>""",
          programs=["c1p13"]),

        T("1.6.8 Bitwise Operators", "1.6.8 Bitwise Operators",
          r"""<p><b>Bitwise operators</b> work on the individual <b>bits</b> (0/1) of integer operands (<code>char, int, long</code>; not float/double). They are used in low-level programming, device control, encryption and compression.</p>
<table>
<tr><th>Operator</th><th>Meaning</th><th>Rule</th></tr>
<tr><td><code>&amp;</code></td><td>Bitwise AND</td><td>1 if both bits are 1</td></tr>
<tr><td><code>|</code></td><td>Bitwise OR</td><td>1 if any bit is 1</td></tr>
<tr><td><code>^</code></td><td>Bitwise XOR</td><td>1 if bits are different</td></tr>
<tr><td><code>~</code></td><td>One's complement</td><td>Inverts every bit (unary); ~a = −(a+1)</td></tr>
<tr><td><code>&lt;&lt;</code></td><td>Left shift</td><td>Shifts bits left; a &lt;&lt; n = a × 2ⁿ</td></tr>
<tr><td><code>&gt;&gt;</code></td><td>Right shift</td><td>Shifts bits right; a &gt;&gt; n = a ÷ 2ⁿ</td></tr>
</table>
<h4>Example: a = 12 (0000 1100), b = 10 (0000 1010)</h4>
<table>
<tr><th>Expression</th><th>Binary</th><th>Decimal</th></tr>
<tr><td><code>a &amp; b</code></td><td>0000 1000</td><td>8</td></tr>
<tr><td><code>a | b</code></td><td>0000 1110</td><td>14</td></tr>
<tr><td><code>a ^ b</code></td><td>0000 0110</td><td>6</td></tr>
<tr><td><code>a &lt;&lt; 2</code></td><td>0011 0000</td><td>48</td></tr>
<tr><td><code>a &gt;&gt; 2</code></td><td>0000 0011</td><td>3</td></tr>
<tr><td><code>~a</code></td><td>1111 0011</td><td>−13</td></tr>
</table>
<p><b>Logical vs bitwise:</b> <code>&amp;&amp;</code> works on whole values (true/false), <code>&amp;</code> works bit by bit: <code>12 &amp;&amp; 10 = 1</code> but <code>12 &amp; 10 = 8</code>.</p>""",
          r"""<p><b>Bitwise operators</b> integer operands (<code>char, int, long</code>; float/double નહીં) ના દરેક <b>bit</b> (0/1) પર કામ કરે છે. તેઓ low-level programming, device control, encryption અને compression માં વપરાય છે.</p>
<table>
<tr><th>Operator</th><th>અર્થ</th><th>નિયમ</th></tr>
<tr><td><code>&amp;</code></td><td>Bitwise AND</td><td>બંને bits 1 હોય તો 1</td></tr>
<tr><td><code>|</code></td><td>Bitwise OR</td><td>કોઈ એક bit 1 હોય તો 1</td></tr>
<tr><td><code>^</code></td><td>Bitwise XOR</td><td>bits અલગ હોય તો 1</td></tr>
<tr><td><code>~</code></td><td>One's complement</td><td>દરેક bit ઉલટાવે (unary); ~a = −(a+1)</td></tr>
<tr><td><code>&lt;&lt;</code></td><td>Left shift</td><td>Bits ડાબે ખસે; a &lt;&lt; n = a × 2ⁿ</td></tr>
<tr><td><code>&gt;&gt;</code></td><td>Right shift</td><td>Bits જમણે ખસે; a &gt;&gt; n = a ÷ 2ⁿ</td></tr>
</table>
<h4>ઉદાહરણ: a = 12 (0000 1100), b = 10 (0000 1010)</h4>
<table>
<tr><th>Expression</th><th>Binary</th><th>Decimal</th></tr>
<tr><td><code>a &amp; b</code></td><td>0000 1000</td><td>8</td></tr>
<tr><td><code>a | b</code></td><td>0000 1110</td><td>14</td></tr>
<tr><td><code>a ^ b</code></td><td>0000 0110</td><td>6</td></tr>
<tr><td><code>a &lt;&lt; 2</code></td><td>0011 0000</td><td>48</td></tr>
<tr><td><code>a &gt;&gt; 2</code></td><td>0000 0011</td><td>3</td></tr>
<tr><td><code>~a</code></td><td>1111 0011</td><td>−13</td></tr>
</table>
<p><b>Logical vs bitwise:</b> <code>&amp;&amp;</code> આખા મૂલ્ય (true/false) પર, <code>&amp;</code> bit-by-bit કામ કરે: <code>12 &amp;&amp; 10 = 1</code> પણ <code>12 &amp; 10 = 8</code>.</p>""",
          programs=["c1p14"]),

        T("1.6.9 Special Operators", "1.6.9 Special Operators",
          r"""<h4>1. Comma operator ( , )</h4>
<p>Links related expressions together. Expressions are evaluated <b>left to right</b> and the value of the <b>rightmost</b> expression is the value of the whole expression.</p>
@@comma@@
<h4>2. sizeof operator</h4>
<p>A compile-time unary operator that returns the <b>number of bytes</b> occupied by a variable, constant or data type. Used to find sizes of arrays/structures and for dynamic memory allocation.</p>
@@sizeof@@
<h4>3. Pointer operators – &amp; and *</h4>
<p><code>&amp;</code> (address of) gives the memory address of a variable: <code>&amp;a</code>. <code>*</code> (indirection / value at address) gives the value stored at an address: <code>*p</code>. (Details in Unit 3.)</p>
<h4>4. Member selection operators – . and -&gt;</h4>
<p>Used to access members of structures and unions: <code>s.roll</code> (with a structure variable) and <code>p-&gt;roll</code> (with a pointer to a structure).</p>""",
          r"""<h4>1. Comma operator ( , )</h4>
<p>સંબંધિત expressions ને જોડે છે. Expressions <b>ડાબેથી જમણે</b> evaluate થાય અને <b>સૌથી જમણા</b> expression નું મૂલ્ય આખા expression નું મૂલ્ય બને.</p>
@@comma@@
<h4>2. sizeof operator</h4>
<p>Compile-time unary operator જે variable, constant અથવા data type એ રોકેલા <b>bytes ની સંખ્યા</b> return કરે છે. Arrays/structures ની size શોધવા અને dynamic memory allocation માં વપરાય.</p>
@@sizeof@@
<h4>3. Pointer operators – &amp; અને *</h4>
<p><code>&amp;</code> (address of) variable નું memory address આપે: <code>&amp;a</code>. <code>*</code> (indirection / value at address) address પર સંગ્રહેલું મૂલ્ય આપે: <code>*p</code>. (વિગત Unit 3 માં.)</p>
<h4>4. Member selection operators – . અને -&gt;</h4>
<p>Structures અને unions ના members access કરવા: <code>s.roll</code> (structure variable સાથે) અને <code>p-&gt;roll</code> (structure ના pointer સાથે).</p>"""),

        T("1.6.10 Arithmetic Expressions and Their Evaluation", "1.6.10 Arithmetic Expressions અને તેનું Evaluation",
          r"""<p>An <b>arithmetic expression</b> is a combination of variables, constants and arithmetic operators. Algebraic expressions must be written in C form – multiplication must be shown with <code>*</code> and there is no operator for power (use <code>pow()</code> from <code>&lt;math.h&gt;</code>).</p>
<table>
<tr><th>Algebraic expression</th><th>C expression</th></tr>
<tr><td>a × b − c</td><td><code>a * b - c</code></td></tr>
<tr><td>(m + n)(x + y)</td><td><code>(m + n) * (x + y)</code></td></tr>
<tr><td>ab / c</td><td><code>a * b / c</code></td></tr>
<tr><td>3x² + 2x + 1</td><td><code>3 * x * x + 2 * x + 1</code></td></tr>
<tr><td>x / y + c</td><td><code>x / y + c</code></td></tr>
<tr><td>(a + b) / (c + d)</td><td><code>(a + b) / (c + d)</code></td></tr>
<tr><td>√(b² − 4ac)</td><td><code>sqrt(b * b - 4 * a * c)</code></td></tr>
<tr><td>πr²</td><td><code>3.14 * r * r</code></td></tr>
</table>
<h4>Evaluation</h4>
<p>Expressions are evaluated using an assignment statement <code>variable = expression;</code>. All variables in the expression must have values before evaluation. The expression is evaluated first and the result replaces the previous value of the variable on the left.</p>
<p>e.g. <code>x = a * b - c;</code> &nbsp; <code>y = b / c * a;</code> &nbsp; <code>z = a - b / c + d;</code></p>""",
          r"""<p><b>Arithmetic expression</b> એ variables, constants અને arithmetic operators નું સંયોજન છે. બીજગણિતીય expressions ને C સ્વરૂપમાં લખવા પડે – ગુણાકાર <code>*</code> થી બતાવવો પડે અને ઘાત (power) માટે operator નથી (<code>&lt;math.h&gt;</code> નું <code>pow()</code> વાપરો).</p>
<table>
<tr><th>બીજગણિતીય expression</th><th>C expression</th></tr>
<tr><td>a × b − c</td><td><code>a * b - c</code></td></tr>
<tr><td>(m + n)(x + y)</td><td><code>(m + n) * (x + y)</code></td></tr>
<tr><td>ab / c</td><td><code>a * b / c</code></td></tr>
<tr><td>3x² + 2x + 1</td><td><code>3 * x * x + 2 * x + 1</code></td></tr>
<tr><td>x / y + c</td><td><code>x / y + c</code></td></tr>
<tr><td>(a + b) / (c + d)</td><td><code>(a + b) / (c + d)</code></td></tr>
<tr><td>√(b² − 4ac)</td><td><code>sqrt(b * b - 4 * a * c)</code></td></tr>
<tr><td>πr²</td><td><code>3.14 * r * r</code></td></tr>
</table>
<h4>Evaluation</h4>
<p>Expressions assignment statement <code>variable = expression;</code> વડે evaluate થાય છે. Evaluation પહેલાં expression ના બધા variables ને મૂલ્ય હોવું જોઈએ. પહેલાં expression evaluate થાય અને પરિણામ ડાબી બાજુના variable ના જૂના મૂલ્યની જગ્યા લે.</p>
<p>દા.ત. <code>x = a * b - c;</code> &nbsp; <code>y = b / c * a;</code> &nbsp; <code>z = a - b / c + d;</code></p>""",
          programs=["c1p5"]),

        T("1.6.11 Precedence of Arithmetic Operators", "1.6.11 Arithmetic Operators ની Precedence",
          r"""<p>When an expression has more than one operator, the order of evaluation is decided by <b>precedence (priority)</b>. Arithmetic operators have two priority levels:</p>
<ul>
<li><b>High priority:</b> <code>*  /  %</code></li>
<li><b>Low priority:</b> <code>+  -</code></li>
</ul>
<p>Operators of the same priority are evaluated <b>left to right</b> (associativity). Expressions in <b>parentheses ( )</b> are evaluated first; innermost parentheses first.</p>
<h4>Example 1: x = a - b / 3 + c * 2 - 1, with a = 9, b = 12, c = 3</h4>
<p><b>First pass</b> (high priority, left to right):<br>Step 1: b / 3 = 12 / 3 = 4 → x = 9 − 4 + c * 2 − 1<br>Step 2: c * 2 = 3 * 2 = 6 → x = 9 − 4 + 6 − 1</p>
<p><b>Second pass</b> (low priority, left to right):<br>Step 3: 9 − 4 = 5<br>Step 4: 5 + 6 = 11<br>Step 5: 11 − 1 = <b>10</b></p>
<h4>Example 2: y = a - b / (3 + c) * (2 - 1)</h4>
<p>Parentheses first: (3 + c) = 6, (2 − 1) = 1 → y = 9 − 12 / 6 * 1<br>Then: 12 / 6 = 2 → 2 * 1 = 2 → 9 − 2 = <b>7</b></p>
<p><b>Rules:</b> use parentheses to make the order clear; the number of opening and closing parentheses must be equal.</p>""",
          r"""<p>Expression માં એક કરતાં વધુ operator હોય ત્યારે evaluation નો ક્રમ <b>precedence (priority)</b> થી નક્કી થાય. Arithmetic operators ના બે priority levels છે:</p>
<ul>
<li><b>ઊંચી priority:</b> <code>*  /  %</code></li>
<li><b>નીચી priority:</b> <code>+  -</code></li>
</ul>
<p>સરખી priority વાળા operators <b>ડાબેથી જમણે</b> evaluate થાય (associativity). <b>Parentheses ( )</b> માંના expressions પહેલાં evaluate થાય; સૌથી અંદરના parentheses પહેલાં.</p>
<h4>ઉદાહરણ 1: x = a - b / 3 + c * 2 - 1, જ્યાં a = 9, b = 12, c = 3</h4>
<p><b>પહેલો pass</b> (ઊંચી priority, ડાબેથી જમણે):<br>Step 1: b / 3 = 12 / 3 = 4 → x = 9 − 4 + c * 2 − 1<br>Step 2: c * 2 = 3 * 2 = 6 → x = 9 − 4 + 6 − 1</p>
<p><b>બીજો pass</b> (નીચી priority, ડાબેથી જમણે):<br>Step 3: 9 − 4 = 5<br>Step 4: 5 + 6 = 11<br>Step 5: 11 − 1 = <b>10</b></p>
<h4>ઉદાહરણ 2: y = a - b / (3 + c) * (2 - 1)</h4>
<p>પહેલાં parentheses: (3 + c) = 6, (2 − 1) = 1 → y = 9 − 12 / 6 * 1<br>પછી: 12 / 6 = 2 → 2 * 1 = 2 → 9 − 2 = <b>7</b></p>
<p><b>નિયમો:</b> ક્રમ સ્પષ્ટ કરવા parentheses વાપરો; ખુલતા અને બંધ થતા parentheses ની સંખ્યા સરખી હોવી જોઈએ.</p>"""),

        T("1.6.12 Type Conversions in Expressions", "1.6.12 Expressions માં Type Conversion",
          r"""<p>When an expression contains operands of different data types, they are converted to a common type. There are two kinds of type conversion:</p>
<h4>1. Implicit (automatic) type conversion</h4>
<p>Done <b>automatically by the compiler</b>. In a mixed expression, the operand of the <b>lower type is promoted to the higher type</b> before the operation, and the result is of the higher type (see hierarchy diagram). This is also called <b>type promotion</b>.</p>
<ul>
<li><code>char</code> and <code>short</code> are always converted to <code>int</code>.</li>
<li>int + float → float; int + double → double; float + double → double; int + long → long.</li>
<li>In an <b>assignment</b>, the right side is converted to the type of the left side. If a higher type is assigned to a lower type, data may be lost: float → int truncates the fraction; double → float rounds digits; long → int drops higher bits.</li>
</ul>
<p>e.g. <code>int i = 5; float f = 2.5; double d = i * f;</code> → i is promoted to float, i * f = 12.5 (float), then converted to double.</p>
<h4>2. Explicit type conversion (type casting)</h4>
<p>Done <b>by the programmer</b> using the <b>cast operator</b>.</p>
<p><b>Syntax:</b> <code>(type_name) expression</code></p>
@@cast@@
<table>
<tr><th>Implicit conversion</th><th>Explicit conversion (casting)</th></tr>
<tr><td>Automatic, by compiler</td><td>Done by programmer with (type)</td></tr>
<tr><td>Lower → higher type (promotion)</td><td>Any type to any type</td></tr>
<tr><td>No data loss in expressions</td><td>Data may be lost (e.g. (int) 9.87 = 9)</td></tr>
</table>""",
          r"""<p>Expression માં અલગ data types ના operands હોય ત્યારે તેમને એક સામાન્ય type માં ફેરવાય છે. Type conversion બે પ્રકારનું છે:</p>
<h4>1. Implicit (automatic) type conversion</h4>
<p><b>Compiler આપોઆપ</b> કરે છે. Mixed expression માં operation પહેલાં <b>નીચા type નો operand ઊંચા type માં promote</b> થાય છે, અને પરિણામ ઊંચા type નું હોય (hierarchy આકૃતિ જુઓ). તેને <b>type promotion</b> પણ કહે છે.</p>
<ul>
<li><code>char</code> અને <code>short</code> હંમેશા <code>int</code> માં ફેરવાય.</li>
<li>int + float → float; int + double → double; float + double → double; int + long → long.</li>
<li><b>Assignment</b> માં જમણી બાજુ ડાબી બાજુના type માં ફેરવાય. ઊંચો type નીચા type ને assign થાય તો data ગુમાઈ શકે: float → int દશાંશ કાપે; double → float અંકો round કરે; long → int ઉપરના bits છોડે.</li>
</ul>
<p>દા.ત. <code>int i = 5; float f = 2.5; double d = i * f;</code> → i float માં promote થાય, i * f = 12.5 (float), પછી double માં ફેરવાય.</p>
<h4>2. Explicit type conversion (type casting)</h4>
<p><b>Cast operator</b> વાપરી <b>programmer</b> કરે છે.</p>
<p><b>Syntax:</b> <code>(type_name) expression</code></p>
@@cast@@
<table>
<tr><th>Implicit conversion</th><th>Explicit conversion (casting)</th></tr>
<tr><td>આપોઆપ, compiler દ્વારા</td><td>Programmer (type) વડે કરે</td></tr>
<tr><td>નીચો → ઊંચો type (promotion)</td><td>કોઈપણ type થી કોઈપણ type</td></tr>
<tr><td>Expressions માં data ગુમાતો નથી</td><td>Data ગુમાઈ શકે (દા.ત. (int) 9.87 = 9)</td></tr>
</table>""",
          diagram="c1_type_hierarchy", programs=["c1p16"]),

        T("1.6.13 Operator Precedence and Associativity", "1.6.13 Operator Precedence અને Associativity",
          r"""<p><b>Precedence</b> decides which operator is evaluated first when an expression has different operators. <b>Associativity</b> decides the order (left-to-right or right-to-left) when operators of the <b>same precedence</b> appear together.</p>
<table>
<tr><th>Rank</th><th>Operators</th><th>Description</th><th>Associativity</th></tr>
<tr><td>1</td><td><code>() [] -&gt; .</code></td><td>Function call, array, member</td><td>Left to right</td></tr>
<tr><td>2</td><td><code>+ - ++ -- ! ~ * &amp; sizeof (type)</code></td><td>Unary operators</td><td>Right to left</td></tr>
<tr><td>3</td><td><code>* / %</code></td><td>Multiplicative</td><td>Left to right</td></tr>
<tr><td>4</td><td><code>+ -</code></td><td>Additive</td><td>Left to right</td></tr>
<tr><td>5</td><td><code>&lt;&lt; &gt;&gt;</code></td><td>Shift</td><td>Left to right</td></tr>
<tr><td>6</td><td><code>&lt; &lt;= &gt; &gt;=</code></td><td>Relational</td><td>Left to right</td></tr>
<tr><td>7</td><td><code>== !=</code></td><td>Equality</td><td>Left to right</td></tr>
<tr><td>8</td><td><code>&amp;</code></td><td>Bitwise AND</td><td>Left to right</td></tr>
<tr><td>9</td><td><code>^</code></td><td>Bitwise XOR</td><td>Left to right</td></tr>
<tr><td>10</td><td><code>|</code></td><td>Bitwise OR</td><td>Left to right</td></tr>
<tr><td>11</td><td><code>&amp;&amp;</code></td><td>Logical AND</td><td>Left to right</td></tr>
<tr><td>12</td><td><code>||</code></td><td>Logical OR</td><td>Left to right</td></tr>
<tr><td>13</td><td><code>?:</code></td><td>Conditional</td><td>Right to left</td></tr>
<tr><td>14</td><td><code>= += -= *= /= %= &amp;= ^= |= &lt;&lt;= &gt;&gt;=</code></td><td>Assignment</td><td>Right to left</td></tr>
<tr><td>15</td><td><code>,</code></td><td>Comma</td><td>Left to right</td></tr>
</table>
<h4>Example</h4>
<p><code>if (x == 10 + 15 &amp;&amp; y &lt; 10)</code> with x = 20, y = 5:<br>
1. <code>10 + 15</code> = 25 (arithmetic first)<br>
2. <code>x == 25</code> → 0 (false); <code>y &lt; 10</code> → 1 (true) (relational before equality, both before &amp;&amp;)<br>
3. <code>0 &amp;&amp; 1</code> → <b>0</b> (false)</p>
<p><b>Memory aid:</b> Unary → Arithmetic → Shift → Relational → Equality → Bitwise → Logical → Conditional → Assignment → Comma.</p>""",
          r"""<p><b>Precedence</b> નક્કી કરે છે કે expression માં અલગ operators હોય ત્યારે કયો operator પહેલાં evaluate થાય. <b>Associativity</b> નક્કી કરે છે કે <b>સરખી precedence</b> વાળા operators સાથે આવે ત્યારે ક્રમ (ડાબેથી જમણે કે જમણેથી ડાબે) કયો હોય.</p>
<table>
<tr><th>ક્રમ</th><th>Operators</th><th>વર્ણન</th><th>Associativity</th></tr>
<tr><td>1</td><td><code>() [] -&gt; .</code></td><td>Function call, array, member</td><td>ડાબેથી જમણે</td></tr>
<tr><td>2</td><td><code>+ - ++ -- ! ~ * &amp; sizeof (type)</code></td><td>Unary operators</td><td>જમણેથી ડાબે</td></tr>
<tr><td>3</td><td><code>* / %</code></td><td>Multiplicative</td><td>ડાબેથી જમણે</td></tr>
<tr><td>4</td><td><code>+ -</code></td><td>Additive</td><td>ડાબેથી જમણે</td></tr>
<tr><td>5</td><td><code>&lt;&lt; &gt;&gt;</code></td><td>Shift</td><td>ડાબેથી જમણે</td></tr>
<tr><td>6</td><td><code>&lt; &lt;= &gt; &gt;=</code></td><td>Relational</td><td>ડાબેથી જમણે</td></tr>
<tr><td>7</td><td><code>== !=</code></td><td>Equality</td><td>ડાબેથી જમણે</td></tr>
<tr><td>8</td><td><code>&amp;</code></td><td>Bitwise AND</td><td>ડાબેથી જમણે</td></tr>
<tr><td>9</td><td><code>^</code></td><td>Bitwise XOR</td><td>ડાબેથી જમણે</td></tr>
<tr><td>10</td><td><code>|</code></td><td>Bitwise OR</td><td>ડાબેથી જમણે</td></tr>
<tr><td>11</td><td><code>&amp;&amp;</code></td><td>Logical AND</td><td>ડાબેથી જમણે</td></tr>
<tr><td>12</td><td><code>||</code></td><td>Logical OR</td><td>ડાબેથી જમણે</td></tr>
<tr><td>13</td><td><code>?:</code></td><td>Conditional</td><td>જમણેથી ડાબે</td></tr>
<tr><td>14</td><td><code>= += -= *= /= %= &amp;= ^= |= &lt;&lt;= &gt;&gt;=</code></td><td>Assignment</td><td>જમણેથી ડાબે</td></tr>
<tr><td>15</td><td><code>,</code></td><td>Comma</td><td>ડાબેથી જમણે</td></tr>
</table>
<h4>ઉદાહરણ</h4>
<p>x = 20, y = 5 માટે <code>if (x == 10 + 15 &amp;&amp; y &lt; 10)</code>:<br>
1. <code>10 + 15</code> = 25 (પહેલાં arithmetic)<br>
2. <code>x == 25</code> → 0 (false); <code>y &lt; 10</code> → 1 (true) (relational, equality પહેલાં; બંને &amp;&amp; પહેલાં)<br>
3. <code>0 &amp;&amp; 1</code> → <b>0</b> (false)</p>
<p><b>યાદ રાખવાની રીત:</b> Unary → Arithmetic → Shift → Relational → Equality → Bitwise → Logical → Conditional → Assignment → Comma.</p>"""),

        T("Key Points – 1.6", "મુખ્ય મુદ્દા – 1.6",
          r"""<ul>
<li>8 operator types: arithmetic, relational, logical, assignment, ++/--, conditional, bitwise, special.</li>
<li>Integer division truncates (5/2 = 2); % only for integers; sign of % = sign of first operand.</li>
<li>Relational/logical results are 1 or 0; <code>&amp;&amp;</code> and <code>||</code> use short-circuit evaluation.</li>
<li><code>b = ++a</code> (increment then use) vs <code>b = a++</code> (use then increment).</li>
<li><code>?:</code> is the only ternary operator. <code>~a = -(a+1)</code>; <code>a&lt;&lt;n = a×2ⁿ</code>.</li>
<li>Precedence: <code>* / %</code> before <code>+ -</code>; same level left to right; parentheses first.</li>
<li>Implicit conversion: lower → higher type; explicit: <code>(float) a / b</code>.</li>
<li>Unary, conditional and assignment operators are right-to-left associative.</li>
</ul>""",
          r"""<ul>
<li>8 operator પ્રકાર: arithmetic, relational, logical, assignment, ++/--, conditional, bitwise, special.</li>
<li>Integer division દશાંશ કાપે (5/2 = 2); % ફક્ત integers માટે; % નું ચિહ્ન = પહેલા operand નું ચિહ્ન.</li>
<li>Relational/logical પરિણામ 1 અથવા 0; <code>&amp;&amp;</code> અને <code>||</code> short-circuit evaluation વાપરે.</li>
<li><code>b = ++a</code> (વધારો પછી ઉપયોગ) vs <code>b = a++</code> (ઉપયોગ પછી વધારો).</li>
<li><code>?:</code> એકમાત્ર ternary operator. <code>~a = -(a+1)</code>; <code>a&lt;&lt;n = a×2ⁿ</code>.</li>
<li>Precedence: <code>+ -</code> પહેલાં <code>* / %</code>; સરખા level પર ડાબેથી જમણે; પહેલાં parentheses.</li>
<li>Implicit conversion: નીચો → ઊંચો type; explicit: <code>(float) a / b</code>.</li>
<li>Unary, conditional અને assignment operators right-to-left associative છે.</li>
</ul>""", key=True),
    ],
}

NOTES_C = [SEC_1_6]
