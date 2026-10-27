"""DI01000131 Unit 1 notes part B: 1.4 Constants, Variables and Data Types; 1.5 Managing Input and Output"""
from c_content import make_T

SN = {
    "decl": r'''
int count;                 // one variable || એક variable
int a, b, total;           // many variables of same type || એક જ પ્રકારના ઘણા variables
float price, rate;
char grade;
double distance;
''',
    "init": r'''
int a = 10;                // declaration + initialization || declaration + initialization
float pi = 3.14f;
char ch = 'Y';
int x, y, z;
x = y = z = 0;             // multiple assignment || multiple assignment
scanf("%d", &a);           // value from keyboard || keyboard પરથી મૂલ્ય
''',
    "typedef_enum": r'''
typedef int marks;         // marks is another name for int || marks એ int નું બીજું નામ
marks m1, m2;

enum day {Mon, Tue, Wed};  // Mon=0, Tue=1, Wed=2
enum day today = Tue;
''',
    "define": r'''
#define PI 3.14159
#define MAX 100
#define PASS_MARK 35
''',
    "const": r'''
const int SIZE = 50;       // value cannot be changed || મૂલ્ય બદલી શકાય નહીં
const float G = 9.81f;
/* SIZE = 60;   -> compile error || SIZE = 60;   -> compile error */
''',
    "getchar": r'''
char ch;
ch = getchar();            // reads one character || એક character વાંચે
putchar(ch);               // displays one character || એક character દર્શાવે
''',
    "scanf_ex": r'''
int a; float b; char c;
scanf("%d", &a);           // integer
scanf("%f", &b);           // float
scanf(" %c", &c);          // space skips previous Enter || space અગાઉનો Enter છોડે
scanf("%d %f", &a, &b);    // mixed input || mixed input
scanf("%2d", &a);          // reads max 2 digits || વધુમાં વધુ 2 અંક વાંચે
''',
    "printf_syn": r'''
printf("control string", arg1, arg2, ...);
printf("Sum = %d\n", sum);
printf("%d + %d = %d\n", a, b, a + b);
''',
}
T = make_T(SN)

# =====================================================================================
SEC_1_4 = {
    "title": {"en": "1.4 Constants, Variables and Data Types", "gu": "1.4 Constants, Variables અને Data Types"},
    "items": [
        T("1.4.1 Introduction and Character Set", "1.4.1 પરિચય અને Character Set",
          r"""<p>Just as English has alphabets → words → sentences → paragraphs, C has <b>characters → tokens → instructions (statements) → programs</b>.</p>
<p>The <b>character set</b> is the set of characters that can be used to write a C program. C uses the following four groups:</p>
<table>
<tr><th>Group</th><th>Characters</th></tr>
<tr><td><b>Letters</b></td><td>Uppercase A … Z and lowercase a … z</td></tr>
<tr><td><b>Digits</b></td><td>0 … 9</td></tr>
<tr><td><b>Special characters</b></td><td>, . ; : ? ' " ! | / \ ~ _ $ % # &amp; ^ * - + &lt; &gt; ( ) [ ] { }</td></tr>
<tr><td><b>White spaces</b></td><td>Blank space, horizontal tab, carriage return, newline, form feed</td></tr>
</table>
<p>The compiler ignores white spaces except inside strings and between keywords/identifiers. <b>Trigraph sequences</b> (e.g. <code>??=</code> for <code>#</code>) were provided for keyboards without some special characters.</p>""",
          r"""<p>જેમ English માં મૂળાક્ષરો → શબ્દો → વાક્યો → ફકરા હોય છે, તેમ C માં <b>characters → tokens → instructions (statements) → programs</b> હોય છે.</p>
<p><b>Character set</b> એ C program લખવામાં વાપરી શકાય તેવા characters નો સમૂહ છે. C નીચેના ચાર જૂથો વાપરે છે:</p>
<table>
<tr><th>જૂથ</th><th>Characters</th></tr>
<tr><td><b>Letters (અક્ષરો)</b></td><td>Uppercase A … Z અને lowercase a … z</td></tr>
<tr><td><b>Digits (અંકો)</b></td><td>0 … 9</td></tr>
<tr><td><b>Special characters</b></td><td>, . ; : ? ' " ! | / \ ~ _ $ % # &amp; ^ * - + &lt; &gt; ( ) [ ] { }</td></tr>
<tr><td><b>White spaces</b></td><td>Blank space, horizontal tab, carriage return, newline, form feed</td></tr>
</table>
<p>Strings ની અંદર અને keywords/identifiers વચ્ચે સિવાય compiler white spaces ને અવગણે છે. અમુક special characters વગરના keyboards માટે <b>Trigraph sequences</b> (દા.ત. <code>#</code> માટે <code>??=</code>) આપેલા હતા.</p>"""),

        T("1.4.2 C Tokens", "1.4.2 C Tokens",
          r"""<p><b>Definition:</b> The <b>smallest individual unit</b> of a C program is called a <b>token</b>. A C program is written using these tokens and the syntax of the language.</p>
<p>C has <b>six types of tokens</b> (see diagram):</p>
<table>
<tr><th>Token</th><th>Meaning</th><th>Examples</th></tr>
<tr><td><b>Keywords</b></td><td>Reserved words with fixed meaning</td><td><code>int, float, if, while, return</code></td></tr>
<tr><td><b>Identifiers</b></td><td>Names given to variables, functions, arrays</td><td><code>sum, main, total_marks</code></td></tr>
<tr><td><b>Constants</b></td><td>Fixed values that do not change</td><td><code>10, -5, 3.14, 'A'</code></td></tr>
<tr><td><b>Strings</b></td><td>Sequence of characters in double quotes</td><td><code>"GTU", "Hello"</code></td></tr>
<tr><td><b>Special symbols</b></td><td>Punctuators / separators</td><td><code>{ } [ ] ( ) ; , #</code></td></tr>
<tr><td><b>Operators</b></td><td>Symbols that perform operations</td><td><code>+ - * / = == &amp;&amp;</code></td></tr>
</table>
<p><b>Example:</b> <code>int sum = a + 10;</code> has 7 tokens: <code>int</code> (keyword), <code>sum</code> (identifier), <code>=</code> (operator), <code>a</code> (identifier), <code>+</code> (operator), <code>10</code> (constant), <code>;</code> (special symbol).</p>""",
          r"""<p><b>વ્યાખ્યા:</b> C program ના <b>સૌથી નાના સ્વતંત્ર એકમ</b> ને <b>token</b> કહે છે. C program આ tokens અને language ની syntax વડે લખાય છે.</p>
<p>C માં <b>છ પ્રકારના tokens</b> છે (આકૃતિ જુઓ):</p>
<table>
<tr><th>Token</th><th>અર્થ</th><th>ઉદાહરણ</th></tr>
<tr><td><b>Keywords</b></td><td>નિશ્ચિત અર્થવાળા અનામત શબ્દો</td><td><code>int, float, if, while, return</code></td></tr>
<tr><td><b>Identifiers</b></td><td>Variables, functions, arrays ને આપેલા નામ</td><td><code>sum, main, total_marks</code></td></tr>
<tr><td><b>Constants</b></td><td>ન બદલાતા નિશ્ચિત મૂલ્યો</td><td><code>10, -5, 3.14, 'A'</code></td></tr>
<tr><td><b>Strings</b></td><td>Double quotes માં characters નો ક્રમ</td><td><code>"GTU", "Hello"</code></td></tr>
<tr><td><b>Special symbols</b></td><td>Punctuators / separators</td><td><code>{ } [ ] ( ) ; , #</code></td></tr>
<tr><td><b>Operators</b></td><td>Operations કરતા symbols</td><td><code>+ - * / = == &amp;&amp;</code></td></tr>
</table>
<p><b>ઉદાહરણ:</b> <code>int sum = a + 10;</code> માં 7 tokens છે: <code>int</code> (keyword), <code>sum</code> (identifier), <code>=</code> (operator), <code>a</code> (identifier), <code>+</code> (operator), <code>10</code> (constant), <code>;</code> (special symbol).</p>""",
          diagram="c1_tokens"),

        T("1.4.3 Keywords and Identifiers", "1.4.3 Keywords અને Identifiers",
          r"""<h4>Keywords</h4>
<p><b>Keywords</b> are <b>reserved words</b> whose meaning is already defined by the compiler. They cannot be used as variable or function names. All keywords are written in <b>lowercase</b>. ANSI C has <b>32 keywords</b>:</p>
<table>
<tr><td>auto</td><td>double</td><td>int</td><td>struct</td></tr>
<tr><td>break</td><td>else</td><td>long</td><td>switch</td></tr>
<tr><td>case</td><td>enum</td><td>register</td><td>typedef</td></tr>
<tr><td>char</td><td>extern</td><td>return</td><td>union</td></tr>
<tr><td>const</td><td>float</td><td>short</td><td>unsigned</td></tr>
<tr><td>continue</td><td>for</td><td>signed</td><td>void</td></tr>
<tr><td>default</td><td>goto</td><td>sizeof</td><td>volatile</td></tr>
<tr><td>do</td><td>if</td><td>static</td><td>while</td></tr>
</table>
<h4>Identifiers</h4>
<p><b>Identifiers</b> are <b>user-defined names</b> given to variables, functions, arrays, structures etc.</p>
<p><b>Rules for identifiers:</b></p>
<ol>
<li>Can contain only <b>letters, digits and underscore ( _ )</b>.</li>
<li>The <b>first character must be a letter or underscore</b>, not a digit.</li>
<li><b>No spaces</b> or other special characters are allowed.</li>
<li>Cannot be a <b>keyword</b>.</li>
<li>They are <b>case sensitive</b>: <code>Total</code> and <code>total</code> are different.</li>
<li>ANSI C guarantees at least the first <b>31 characters</b> are significant.</li>
</ol>
<table>
<tr><th>Valid</th><th>Invalid (reason)</th></tr>
<tr><td><code>sum</code></td><td><code>2sum</code> (starts with digit)</td></tr>
<tr><td><code>total_marks</code></td><td><code>total marks</code> (space)</td></tr>
<tr><td><code>_count</code></td><td><code>int</code> (keyword)</td></tr>
<tr><td><code>num1</code></td><td><code>num-1</code> (special char –)</td></tr>
<tr><td><code>Area</code></td><td><code>$amount</code> ($ not allowed in standard C)</td></tr>
</table>""",
          r"""<h4>Keywords</h4>
<p><b>Keywords</b> એ <b>અનામત શબ્દો (reserved words)</b> છે જેનો અર્થ compiler માં પહેલેથી નક્કી છે. તેમને variable કે function ના નામ તરીકે વાપરી શકાય નહીં. બધા keywords <b>lowercase</b> માં લખાય છે. ANSI C માં <b>32 keywords</b> છે:</p>
<table>
<tr><td>auto</td><td>double</td><td>int</td><td>struct</td></tr>
<tr><td>break</td><td>else</td><td>long</td><td>switch</td></tr>
<tr><td>case</td><td>enum</td><td>register</td><td>typedef</td></tr>
<tr><td>char</td><td>extern</td><td>return</td><td>union</td></tr>
<tr><td>const</td><td>float</td><td>short</td><td>unsigned</td></tr>
<tr><td>continue</td><td>for</td><td>signed</td><td>void</td></tr>
<tr><td>default</td><td>goto</td><td>sizeof</td><td>volatile</td></tr>
<tr><td>do</td><td>if</td><td>static</td><td>while</td></tr>
</table>
<h4>Identifiers</h4>
<p><b>Identifiers</b> એ variables, functions, arrays, structures વગેરેને આપેલા <b>user-defined નામ</b> છે.</p>
<p><b>Identifiers ના નિયમો:</b></p>
<ol>
<li>ફક્ત <b>letters, digits અને underscore ( _ )</b> હોઈ શકે.</li>
<li><b>પહેલો character letter અથવા underscore</b> જ હોવો જોઈએ, digit નહીં.</li>
<li><b>Space</b> કે બીજા special characters ચાલે નહીં.</li>
<li><b>Keyword</b> ન હોઈ શકે.</li>
<li><b>Case sensitive</b> છે: <code>Total</code> અને <code>total</code> અલગ છે.</li>
<li>ANSI C પ્રથમ ઓછામાં ઓછા <b>31 characters</b> ને significant ગણે છે.</li>
</ol>
<table>
<tr><th>Valid</th><th>Invalid (કારણ)</th></tr>
<tr><td><code>sum</code></td><td><code>2sum</code> (digit થી શરૂ)</td></tr>
<tr><td><code>total_marks</code></td><td><code>total marks</code> (space)</td></tr>
<tr><td><code>_count</code></td><td><code>int</code> (keyword)</td></tr>
<tr><td><code>num1</code></td><td><code>num-1</code> (special char –)</td></tr>
<tr><td><code>Area</code></td><td><code>$amount</code> (standard C માં $ ચાલે નહીં)</td></tr>
</table>"""),

        T("1.4.4 Constants", "1.4.4 Constants (અચળાંકો)",
          r"""<p><b>Constants</b> are <b>fixed values</b> that do not change during the execution of a program.</p>
<h4>Types of constants</h4>
<ul>
<li><b>Numeric constants</b> – integer constants and real constants</li>
<li><b>Character constants</b> – single character constants and string constants</li>
</ul>
<h4>1. Integer constants</h4>
<p>Whole numbers without a decimal point. Three types:</p>
<table>
<tr><th>Type</th><th>Digits</th><th>Prefix</th><th>Examples</th></tr>
<tr><td>Decimal</td><td>0 – 9</td><td>none</td><td><code>123, -45, 0</code></td></tr>
<tr><td>Octal</td><td>0 – 7</td><td><code>0</code></td><td><code>037, 0435</code></td></tr>
<tr><td>Hexadecimal</td><td>0 – 9, A – F</td><td><code>0x</code> or <code>0X</code></td><td><code>0x2A, 0X9F</code></td></tr>
</table>
<p>Suffix <code>L</code> = long (<code>50000L</code>), <code>U</code> = unsigned (<code>100U</code>). Commas and spaces are not allowed (<code>10,000</code> is invalid).</p>
<h4>2. Real (floating-point) constants</h4>
<p>Numbers with a fractional part. Two forms:</p>
<ul><li><b>Fractional form:</b> <code>0.0083, -0.75, 435.36, 215.</code></li>
<li><b>Exponential form:</b> <code>mantissa e exponent</code> – e.g. <code>2.15e2</code> = 215, <code>1.5e-3</code> = 0.0015. Useful for very large or small numbers.</li></ul>
<h4>3. Single character constants</h4>
<p>One character in <b>single quotes</b>: <code>'A'</code>, <code>'5'</code>, <code>';'</code>, <code>' '</code>. Each has an integer ASCII value: <code>'A'</code> = 65, <code>'a'</code> = 97, <code>'0'</code> = 48.</p>
<h4>4. String constants</h4>
<p>A sequence of characters in <b>double quotes</b>: <code>"Hello"</code>, <code>"2024"</code>, <code>"A"</code>. A string is automatically terminated by the null character <code>'\0'</code>, so <code>'A'</code> (1 byte) ≠ <code>"A"</code> (2 bytes).</p>
<h4>5. Backslash character constants (escape sequences)</h4>
<table>
<tr><th>Escape</th><th>Meaning</th><th>Escape</th><th>Meaning</th></tr>
<tr><td><code>\n</code></td><td>New line</td><td><code>\\</code></td><td>Backslash</td></tr>
<tr><td><code>\t</code></td><td>Horizontal tab</td><td><code>\'</code></td><td>Single quote</td></tr>
<tr><td><code>\a</code></td><td>Alert (beep)</td><td><code>\"</code></td><td>Double quote</td></tr>
<tr><td><code>\b</code></td><td>Backspace</td><td><code>\?</code></td><td>Question mark</td></tr>
<tr><td><code>\r</code></td><td>Carriage return</td><td><code>\0</code></td><td>Null character</td></tr>
<tr><td><code>\f</code></td><td>Form feed</td><td><code>\v</code></td><td>Vertical tab</td></tr>
</table>""",
          r"""<p><b>Constants</b> એ program ના execution દરમિયાન <b>ન બદલાતા નિશ્ચિત મૂલ્યો</b> છે.</p>
<h4>Constants ના પ્રકાર</h4>
<ul>
<li><b>Numeric constants</b> – integer constants અને real constants</li>
<li><b>Character constants</b> – single character constants અને string constants</li>
</ul>
<h4>1. Integer constants</h4>
<p>દશાંશ ચિહ્ન વગરની પૂર્ણ સંખ્યાઓ. ત્રણ પ્રકાર:</p>
<table>
<tr><th>પ્રકાર</th><th>અંકો</th><th>Prefix</th><th>ઉદાહરણ</th></tr>
<tr><td>Decimal</td><td>0 – 9</td><td>નથી</td><td><code>123, -45, 0</code></td></tr>
<tr><td>Octal</td><td>0 – 7</td><td><code>0</code></td><td><code>037, 0435</code></td></tr>
<tr><td>Hexadecimal</td><td>0 – 9, A – F</td><td><code>0x</code> અથવા <code>0X</code></td><td><code>0x2A, 0X9F</code></td></tr>
</table>
<p>Suffix <code>L</code> = long (<code>50000L</code>), <code>U</code> = unsigned (<code>100U</code>). Comma અને space ચાલે નહીં (<code>10,000</code> invalid છે).</p>
<h4>2. Real (floating-point) constants</h4>
<p>દશાંશ ભાગવાળી સંખ્યાઓ. બે સ્વરૂપ:</p>
<ul><li><b>Fractional form:</b> <code>0.0083, -0.75, 435.36, 215.</code></li>
<li><b>Exponential form:</b> <code>mantissa e exponent</code> – દા.ત. <code>2.15e2</code> = 215, <code>1.5e-3</code> = 0.0015. ખૂબ મોટી કે નાની સંખ્યાઓ માટે ઉપયોગી.</li></ul>
<h4>3. Single character constants</h4>
<p><b>Single quotes</b> માં એક character: <code>'A'</code>, <code>'5'</code>, <code>';'</code>, <code>' '</code>. દરેકની integer ASCII value હોય છે: <code>'A'</code> = 65, <code>'a'</code> = 97, <code>'0'</code> = 48.</p>
<h4>4. String constants</h4>
<p><b>Double quotes</b> માં characters નો ક્રમ: <code>"Hello"</code>, <code>"2024"</code>, <code>"A"</code>. String આપોઆપ null character <code>'\0'</code> થી પૂરી થાય છે, તેથી <code>'A'</code> (1 byte) ≠ <code>"A"</code> (2 bytes).</p>
<h4>5. Backslash character constants (escape sequences)</h4>
<table>
<tr><th>Escape</th><th>અર્થ</th><th>Escape</th><th>અર્થ</th></tr>
<tr><td><code>\n</code></td><td>નવી line</td><td><code>\\</code></td><td>Backslash</td></tr>
<tr><td><code>\t</code></td><td>Horizontal tab</td><td><code>\'</code></td><td>Single quote</td></tr>
<tr><td><code>\a</code></td><td>Alert (beep)</td><td><code>\"</code></td><td>Double quote</td></tr>
<tr><td><code>\b</code></td><td>Backspace</td><td><code>\?</code></td><td>Question mark</td></tr>
<tr><td><code>\r</code></td><td>Carriage return</td><td><code>\0</code></td><td>Null character</td></tr>
<tr><td><code>\f</code></td><td>Form feed</td><td><code>\v</code></td><td>Vertical tab</td></tr>
</table>"""),

        T("1.4.5 Variables", "1.4.5 Variables (ચલ)",
          r"""<p><b>Definition:</b> A <b>variable</b> is a <b>named memory location</b> used to store a data value. Unlike a constant, the value of a variable <b>can change</b> during program execution.</p>
<p>Example: in <code>int age = 18;</code> – <code>age</code> is the variable name, <code>int</code> its type and 18 its value. The compiler reserves memory (e.g. 4 bytes) for it.</p>
<h4>Rules for variable names</h4>
<p>Variable names are identifiers, so all identifier rules apply: letters, digits and underscore only; must begin with a letter or underscore; no keywords; no spaces; case sensitive. Choose <b>meaningful names</b> such as <code>total_marks</code> instead of <code>tm</code>.</p>
<h4>Constant vs variable</h4>
<table>
<tr><th>Constant</th><th>Variable</th></tr>
<tr><td>Fixed value, cannot change</td><td>Value can change during execution</td></tr>
<tr><td>e.g. 10, 3.14, 'A'</td><td>e.g. <code>sum</code>, <code>rate</code></td></tr>
<tr><td>No name needed (literal)</td><td>Has a name and data type</td></tr>
</table>""",
          r"""<p><b>વ્યાખ્યા:</b> <b>Variable</b> એ data value સંગ્રહવા માટેનું <b>નામવાળું memory location</b> છે. Constant થી વિપરીત, variable નું મૂલ્ય program execution દરમિયાન <b>બદલાઈ શકે</b> છે.</p>
<p>ઉદાહરણ: <code>int age = 18;</code> માં – <code>age</code> variable નું નામ, <code>int</code> તેનો type અને 18 તેનું મૂલ્ય છે. Compiler તેના માટે memory (દા.ત. 4 bytes) અનામત રાખે છે.</p>
<h4>Variable નામના નિયમો</h4>
<p>Variable નામ identifiers છે, તેથી identifier ના બધા નિયમો લાગુ પડે: ફક્ત letters, digits અને underscore; letter અથવા underscore થી શરૂ; keywords નહીં; spaces નહીં; case sensitive. <code>tm</code> ની જગ્યાએ <code>total_marks</code> જેવા <b>અર્થપૂર્ણ નામ</b> પસંદ કરો.</p>
<h4>Constant vs variable</h4>
<table>
<tr><th>Constant</th><th>Variable</th></tr>
<tr><td>નિશ્ચિત મૂલ્ય, બદલાય નહીં</td><td>Execution દરમિયાન મૂલ્ય બદલાઈ શકે</td></tr>
<tr><td>દા.ત. 10, 3.14, 'A'</td><td>દા.ત. <code>sum</code>, <code>rate</code></td></tr>
<tr><td>નામની જરૂર નથી (literal)</td><td>નામ અને data type હોય</td></tr>
</table>"""),

        T("1.4.6 Data Types", "1.4.6 Data Types",
          r"""<p>A <b>data type</b> specifies the <b>type of data</b> a variable can store, the <b>memory size</b> and the <b>range</b> of values. C data types are classified as (see diagram):</p>
<ul>
<li><b>Primary (fundamental / built-in):</b> <code>int, char, float, double, void</code></li>
<li><b>Derived:</b> array, pointer, function</li>
<li><b>User-defined:</b> <code>struct, union, enum, typedef</code></li>
</ul>
<h4>Primary data types</h4>
<table>
<tr><th>Type</th><th>Size*</th><th>Range</th><th>Format</th><th>Use</th></tr>
<tr><td><code>char</code></td><td>1 byte</td><td>−128 to 127</td><td>%c</td><td>Single character</td></tr>
<tr><td><code>int</code></td><td>2 / 4 bytes</td><td>−32768 to 32767 (2 bytes)<br>−2,147,483,648 to 2,147,483,647 (4 bytes)</td><td>%d</td><td>Whole numbers</td></tr>
<tr><td><code>float</code></td><td>4 bytes</td><td>3.4E−38 to 3.4E+38 (6–7 digit precision)</td><td>%f</td><td>Real numbers</td></tr>
<tr><td><code>double</code></td><td>8 bytes</td><td>1.7E−308 to 1.7E+308 (15–16 digit precision)</td><td>%lf</td><td>Large / precise real numbers</td></tr>
<tr><td><code>void</code></td><td>–</td><td>No value</td><td>–</td><td>Functions returning nothing</td></tr>
</table>
<p>*<code>int</code> is 2 bytes in 16-bit compilers (Turbo C) and 4 bytes in 32/64-bit compilers (GCC, Visual C).</p>
<h4>Type modifiers (qualifiers)</h4>
<p><code>signed, unsigned, short, long</code> change the size/range of the basic types:</p>
<table>
<tr><th>Type</th><th>Size (GCC)</th><th>Range</th><th>Format</th></tr>
<tr><td><code>unsigned char</code></td><td>1</td><td>0 to 255</td><td>%c</td></tr>
<tr><td><code>short int</code></td><td>2</td><td>−32768 to 32767</td><td>%hd</td></tr>
<tr><td><code>unsigned int</code></td><td>4</td><td>0 to 4,294,967,295</td><td>%u</td></tr>
<tr><td><code>long int</code></td><td>4 / 8</td><td>at least −2,147,483,648 to 2,147,483,647</td><td>%ld</td></tr>
<tr><td><code>long double</code></td><td>10 / 12 / 16</td><td>3.4E−4932 to 1.1E+4932</td><td>%Lf</td></tr>
</table>
<p>Use <code>sizeof</code> to find the size on your compiler (see program).</p>""",
          r"""<p><b>Data type</b> એ variable કયા <b>પ્રકારનો data</b> સંગ્રહી શકે, તેની <b>memory size</b> અને મૂલ્યોની <b>range</b> નક્કી કરે છે. C data types નું વર્ગીકરણ (આકૃતિ જુઓ):</p>
<ul>
<li><b>Primary (fundamental / built-in):</b> <code>int, char, float, double, void</code></li>
<li><b>Derived:</b> array, pointer, function</li>
<li><b>User-defined:</b> <code>struct, union, enum, typedef</code></li>
</ul>
<h4>Primary data types</h4>
<table>
<tr><th>Type</th><th>Size*</th><th>Range</th><th>Format</th><th>ઉપયોગ</th></tr>
<tr><td><code>char</code></td><td>1 byte</td><td>−128 થી 127</td><td>%c</td><td>એક character</td></tr>
<tr><td><code>int</code></td><td>2 / 4 bytes</td><td>−32768 થી 32767 (2 bytes)<br>−2,147,483,648 થી 2,147,483,647 (4 bytes)</td><td>%d</td><td>પૂર્ણ સંખ્યાઓ</td></tr>
<tr><td><code>float</code></td><td>4 bytes</td><td>3.4E−38 થી 3.4E+38 (6–7 અંકની ચોકસાઈ)</td><td>%f</td><td>Real સંખ્યાઓ</td></tr>
<tr><td><code>double</code></td><td>8 bytes</td><td>1.7E−308 થી 1.7E+308 (15–16 અંકની ચોકસાઈ)</td><td>%lf</td><td>મોટી / ચોક્કસ real સંખ્યાઓ</td></tr>
<tr><td><code>void</code></td><td>–</td><td>કોઈ મૂલ્ય નહીં</td><td>–</td><td>કંઈ return ન કરતા functions</td></tr>
</table>
<p>*16-bit compilers (Turbo C) માં <code>int</code> 2 bytes અને 32/64-bit compilers (GCC, Visual C) માં 4 bytes હોય છે.</p>
<h4>Type modifiers (qualifiers)</h4>
<p><code>signed, unsigned, short, long</code> મૂળ types ની size/range બદલે છે:</p>
<table>
<tr><th>Type</th><th>Size (GCC)</th><th>Range</th><th>Format</th></tr>
<tr><td><code>unsigned char</code></td><td>1</td><td>0 થી 255</td><td>%c</td></tr>
<tr><td><code>short int</code></td><td>2</td><td>−32768 થી 32767</td><td>%hd</td></tr>
<tr><td><code>unsigned int</code></td><td>4</td><td>0 થી 4,294,967,295</td><td>%u</td></tr>
<tr><td><code>long int</code></td><td>4 / 8</td><td>ઓછામાં ઓછું −2,147,483,648 થી 2,147,483,647</td><td>%ld</td></tr>
<tr><td><code>long double</code></td><td>10 / 12 / 16</td><td>3.4E−4932 થી 1.1E+4932</td><td>%Lf</td></tr>
</table>
<p>તમારા compiler પર size જાણવા <code>sizeof</code> વાપરો (program જુઓ).</p>""",
          diagram="c1_datatypes", programs=["c1p15"]),

        T("1.4.7 Declaration of Variables and Assigning Values", "1.4.7 Variables નું Declaration અને મૂલ્ય આપવું (Assignment)",
          r"""<h4>Declaration</h4>
<p>Every variable must be <b>declared before use</b>. Declaration tells the compiler (1) the <b>name</b> of the variable and (2) the <b>type of data</b> it will hold, so that memory can be reserved.</p>
<p><b>Syntax:</b> <code>data_type var1, var2, …, varN;</code></p>
@@decl@@
<h4>Assigning values</h4>
<p>Values can be given to variables in three ways:</p>
<ol>
<li><b>Assignment statement:</b> <code>variable = expression;</code> e.g. <code>sum = a + b;</code></li>
<li><b>Initialization at declaration:</b> <code>int a = 10;</code></li>
<li><b>Reading from keyboard</b> with <code>scanf()</code>.</li>
</ol>
@@init@@
<p>An uninitialized local variable contains a <b>garbage value</b> (unknown value), so always initialize variables like <code>sum = 0</code> before using them.</p>
<h4>User-defined type declarations</h4>
<p><code>typedef</code> gives a new name to an existing type; <code>enum</code> defines a set of named integer constants.</p>
@@typedef_enum@@""",
          r"""<h4>Declaration</h4>
<p>દરેક variable ને <b>ઉપયોગ પહેલાં declare</b> કરવો જ પડે. Declaration compiler ને (1) variable નું <b>નામ</b> અને (2) તે કયા <b>પ્રકારનો data</b> રાખશે તે જણાવે છે, જેથી memory અનામત રાખી શકાય.</p>
<p><b>Syntax:</b> <code>data_type var1, var2, …, varN;</code></p>
@@decl@@
<h4>મૂલ્ય આપવું (Assigning values)</h4>
<p>Variables ને ત્રણ રીતે મૂલ્ય આપી શકાય:</p>
<ol>
<li><b>Assignment statement:</b> <code>variable = expression;</code> દા.ત. <code>sum = a + b;</code></li>
<li><b>Declaration વખતે initialization:</b> <code>int a = 10;</code></li>
<li><code>scanf()</code> વડે <b>keyboard પરથી વાંચીને</b>.</li>
</ol>
@@init@@
<p>Initialize ન કરેલા local variable માં <b>garbage value</b> (અજાણ્યું મૂલ્ય) હોય છે, તેથી ઉપયોગ પહેલાં <code>sum = 0</code> જેવું initialization હંમેશા કરો.</p>
<h4>User-defined type declarations</h4>
<p><code>typedef</code> હાલના type ને નવું નામ આપે છે; <code>enum</code> નામવાળા integer constants નો સમૂહ વ્યાખ્યાયિત કરે છે.</p>
@@typedef_enum@@""",
          programs=["c1p6"]),

        T("1.4.8 Defining Symbolic Constants", "1.4.8 Symbolic Constants વ્યાખ્યાયિત કરવા",
          r"""<p>A <b>symbolic constant</b> is a <b>name that represents a constant value</b>. It is defined with the <b>#define</b> preprocessor directive.</p>
<p><b>Syntax:</b> <code>#define SYMBOLIC_NAME value</code></p>
@@define@@
<p>Before compilation, the preprocessor replaces every occurrence of the name with its value.</p>
<h4>Why use symbolic constants?</h4>
<ul>
<li><b>Modifiability:</b> the value is changed at one place only (e.g. change <code>MAX</code> from 100 to 200).</li>
<li><b>Understandability:</b> <code>PASS_MARK</code> is more meaningful than the number 35.</li>
</ul>
<h4>Rules</h4>
<ol>
<li>Written in <b>CAPITAL letters</b> (by convention) to distinguish them from variables.</li>
<li><b>No semicolon</b> at the end and <b>no = sign</b>: <code>#define PI 3.14</code>.</li>
<li><code>#</code> must be the first character in the line; usually placed at the beginning of the program.</li>
<li>No blank space between <code>#</code> and <code>define</code>.</li>
<li>A symbolic name cannot be assigned a new value inside the program (<code>PI = 3.5;</code> is invalid).</li>
<li>They are not declared with a data type.</li>
</ol>
<h4>const qualifier</h4>
<p>A variable can also be made constant using the <code>const</code> keyword. Unlike <code>#define</code>, it has a data type and occupies memory.</p>
@@const@@""",
          r"""<p><b>Symbolic constant</b> એ <b>અચળ મૂલ્ય દર્શાવતું નામ</b> છે. તે <b>#define</b> preprocessor directive વડે વ્યાખ્યાયિત થાય છે.</p>
<p><b>Syntax:</b> <code>#define SYMBOLIC_NAME value</code></p>
@@define@@
<p>Compilation પહેલાં preprocessor નામની દરેક ઘટના ની જગ્યાએ તેનું મૂલ્ય મૂકે છે.</p>
<h4>Symbolic constants શા માટે?</h4>
<ul>
<li><b>ફેરફાર સરળ (Modifiability):</b> મૂલ્ય ફક્ત એક જ જગ્યાએ બદલવું પડે (દા.ત. <code>MAX</code> 100 થી 200).</li>
<li><b>સમજ સરળ (Understandability):</b> સંખ્યા 35 કરતાં <code>PASS_MARK</code> વધુ અર્થપૂર્ણ છે.</li>
</ul>
<h4>નિયમો</h4>
<ol>
<li>Variables થી અલગ પાડવા (પરંપરા મુજબ) <b>CAPITAL letters</b> માં લખાય.</li>
<li>અંતે <b>semicolon નહીં</b> અને <b>= ચિહ્ન નહીં</b>: <code>#define PI 3.14</code>.</li>
<li><code>#</code> line નો પહેલો character હોવો જોઈએ; સામાન્ય રીતે program ની શરૂઆતમાં મૂકાય.</li>
<li><code>#</code> અને <code>define</code> વચ્ચે space નહીં.</li>
<li>Program ની અંદર symbolic name ને નવું મૂલ્ય આપી શકાય નહીં (<code>PI = 3.5;</code> invalid).</li>
<li>તેમને data type સાથે declare કરાતા નથી.</li>
</ol>
<h4>const qualifier</h4>
<p><code>const</code> keyword વડે variable ને પણ અચળ બનાવી શકાય. <code>#define</code> થી વિપરીત, તેનો data type હોય છે અને તે memory રોકે છે.</p>
@@const@@""",
          programs=["c1p3"]),

        T("Key Points – 1.4", "મુખ્ય મુદ્દા – 1.4",
          r"""<ul>
<li>Character set: letters, digits, special characters, white spaces.</li>
<li><b>6 tokens:</b> keywords, identifiers, constants, strings, special symbols, operators.</li>
<li><b>32 keywords</b>, all lowercase. Identifier: letters/digits/_ , not starting with digit, not a keyword.</li>
<li>Constants: integer (decimal, octal 0…, hex 0x…), real (fractional, exponent), character 'A', string "A" (ends with \0).</li>
<li>Variable = named memory location; declare before use: <code>int a;</code></li>
<li>char 1 byte (%c), int 2/4 (%d), float 4 (%f), double 8 (%lf).</li>
<li><code>#define PI 3.14</code> – no semicolon, no =, capital letters.</li>
</ul>""",
          r"""<ul>
<li>Character set: letters, digits, special characters, white spaces.</li>
<li><b>6 tokens:</b> keywords, identifiers, constants, strings, special symbols, operators.</li>
<li><b>32 keywords</b>, બધા lowercase. Identifier: letters/digits/_ , digit થી શરૂ નહીં, keyword નહીં.</li>
<li>Constants: integer (decimal, octal 0…, hex 0x…), real (fractional, exponent), character 'A', string "A" (\0 થી પૂરી).</li>
<li>Variable = નામવાળું memory location; ઉપયોગ પહેલાં declare: <code>int a;</code></li>
<li>char 1 byte (%c), int 2/4 (%d), float 4 (%f), double 8 (%lf).</li>
<li><code>#define PI 3.14</code> – semicolon નહીં, = નહીં, capital letters.</li>
</ul>""", key=True),
    ],
}

# =====================================================================================
SEC_1_5 = {
    "title": {"en": "1.5 Managing Input and Output Operations", "gu": "1.5 Input અને Output Operations"},
    "items": [
        T("1.5.1 Reading a Character", "1.5.1 Character વાંચવો (Reading a Character)",
          r"""<p>C has no built-in input/output statements. All I/O is done through <b>library functions</b> declared in the header file <code>&lt;stdio.h&gt;</code> (standard input-output).</p>
<p>I/O functions are of two types: <b>unformatted</b> (<code>getchar(), putchar(), gets(), puts()</code>) and <b>formatted</b> (<code>scanf(), printf()</code>).</p>
<h4>getchar()</h4>
<p>Reads <b>a single character</b> from the standard input (keyboard).</p>
<p><b>Syntax:</b> <code>variable_name = getchar();</code></p>
@@getchar@@
<ul>
<li>It waits until a key is pressed <b>and Enter</b> is pressed (buffered input).</li>
<li>It returns the character read (as an int); returns <code>EOF</code> at end of file.</li>
</ul>
<p>Related (non-standard, <code>&lt;conio.h&gt;</code> in Turbo C): <code>getch()</code> – reads a character without echo and without Enter; <code>getche()</code> – reads with echo.</p>
<h4>Character test functions – &lt;ctype.h&gt;</h4>
<table>
<tr><th>Function</th><th>Test / action</th></tr>
<tr><td><code>isalpha(c)</code></td><td>Is c a letter?</td></tr>
<tr><td><code>isdigit(c)</code></td><td>Is c a digit?</td></tr>
<tr><td><code>isalnum(c)</code></td><td>Letter or digit?</td></tr>
<tr><td><code>islower(c)</code> / <code>isupper(c)</code></td><td>Lowercase / uppercase letter?</td></tr>
<tr><td><code>isspace(c)</code></td><td>White-space character?</td></tr>
<tr><td><code>ispunct(c)</code></td><td>Punctuation character?</td></tr>
<tr><td><code>tolower(c)</code> / <code>toupper(c)</code></td><td>Convert to lowercase / uppercase</td></tr>
</table>""",
          r"""<p>C માં built-in input/output statements નથી. બધા I/O header file <code>&lt;stdio.h&gt;</code> (standard input-output) માં declare થયેલા <b>library functions</b> વડે થાય છે.</p>
<p>I/O functions બે પ્રકારના છે: <b>unformatted</b> (<code>getchar(), putchar(), gets(), puts()</code>) અને <b>formatted</b> (<code>scanf(), printf()</code>).</p>
<h4>getchar()</h4>
<p>Standard input (keyboard) પરથી <b>એક character</b> વાંચે છે.</p>
<p><b>Syntax:</b> <code>variable_name = getchar();</code></p>
@@getchar@@
<ul>
<li>Key દબાવી <b>Enter</b> દબાવાય ત્યાં સુધી રાહ જુએ (buffered input).</li>
<li>વાંચેલો character (int તરીકે) return કરે; file ના અંતે <code>EOF</code> return કરે.</li>
</ul>
<p>સંબંધિત (non-standard, Turbo C માં <code>&lt;conio.h&gt;</code>): <code>getch()</code> – echo અને Enter વગર character વાંચે; <code>getche()</code> – echo સાથે વાંચે.</p>
<h4>Character test functions – &lt;ctype.h&gt;</h4>
<table>
<tr><th>Function</th><th>Test / કાર્ય</th></tr>
<tr><td><code>isalpha(c)</code></td><td>c letter છે?</td></tr>
<tr><td><code>isdigit(c)</code></td><td>c digit છે?</td></tr>
<tr><td><code>isalnum(c)</code></td><td>Letter અથવા digit?</td></tr>
<tr><td><code>islower(c)</code> / <code>isupper(c)</code></td><td>Lowercase / uppercase letter?</td></tr>
<tr><td><code>isspace(c)</code></td><td>White-space character?</td></tr>
<tr><td><code>ispunct(c)</code></td><td>Punctuation character?</td></tr>
<tr><td><code>tolower(c)</code> / <code>toupper(c)</code></td><td>Lowercase / uppercase માં ફેરવે</td></tr>
</table>""",
          programs=["c1p7"]),

        T("1.5.2 Writing a Character", "1.5.2 Character લખવો (Writing a Character)",
          r"""<h4>putchar()</h4>
<p>Displays (writes) <b>a single character</b> on the standard output (screen).</p>
<p><b>Syntax:</b> <code>putchar(variable_name);</code> or <code>putchar('A');</code></p>
<ul>
<li><code>putchar(ch);</code> – prints the character stored in <code>ch</code>.</li>
<li><code>putchar('\n');</code> – moves the cursor to the next line.</li>
<li>It returns the character written, or <code>EOF</code> on error.</li>
</ul>
<p>Related: <code>putch()</code> (<code>&lt;conio.h&gt;</code>, Turbo C). For strings, <code>gets()</code>/<code>puts()</code> are used (Unit 5).</p>
<h4>getchar() vs putchar()</h4>
<table>
<tr><th>getchar()</th><th>putchar()</th></tr>
<tr><td>Input function</td><td>Output function</td></tr>
<tr><td>Reads one character from keyboard</td><td>Writes one character to screen</td></tr>
<tr><td><code>ch = getchar();</code> – no argument</td><td><code>putchar(ch);</code> – one argument</td></tr>
</table>""",
          r"""<h4>putchar()</h4>
<p>Standard output (screen) પર <b>એક character</b> દર્શાવે (લખે) છે.</p>
<p><b>Syntax:</b> <code>putchar(variable_name);</code> અથવા <code>putchar('A');</code></p>
<ul>
<li><code>putchar(ch);</code> – <code>ch</code> માં સંગ્રહેલો character છાપે.</li>
<li><code>putchar('\n');</code> – cursor ને આગલી line પર લઈ જાય.</li>
<li>લખેલો character return કરે, error હોય તો <code>EOF</code>.</li>
</ul>
<p>સંબંધિત: <code>putch()</code> (<code>&lt;conio.h&gt;</code>, Turbo C). Strings માટે <code>gets()</code>/<code>puts()</code> વપરાય (Unit 5).</p>
<h4>getchar() vs putchar()</h4>
<table>
<tr><th>getchar()</th><th>putchar()</th></tr>
<tr><td>Input function</td><td>Output function</td></tr>
<tr><td>Keyboard પરથી એક character વાંચે</td><td>Screen પર એક character લખે</td></tr>
<tr><td><code>ch = getchar();</code> – argument નહીં</td><td><code>putchar(ch);</code> – એક argument</td></tr>
</table>"""),

        T("1.5.3 Formatted Input – scanf()", "1.5.3 Formatted Input – scanf()",
          r"""<p><code>scanf()</code> reads <b>formatted data</b> (int, float, char, string, …) from the keyboard.</p>
<p><b>Syntax:</b> <code>scanf("control string", &amp;var1, &amp;var2, …);</code></p>
<ul>
<li><b>Control string</b> contains <b>format specifiers</b> (beginning with <code>%</code>) that tell the type of data to read.</li>
<li>The <b>address-of operator &amp;</b> must be written before each variable name, because scanf stores the value at that address (not needed for strings / arrays).</li>
<li>Inputs are separated by spaces, tabs or Enter.</li>
<li>scanf returns the number of values successfully read.</li>
</ul>
<h4>Format specifiers</h4>
<table>
<tr><th>Specifier</th><th>Data type</th><th>Specifier</th><th>Data type</th></tr>
<tr><td><code>%d</code> / <code>%i</code></td><td>int</td><td><code>%c</code></td><td>char</td></tr>
<tr><td><code>%f</code></td><td>float</td><td><code>%s</code></td><td>string</td></tr>
<tr><td><code>%lf</code></td><td>double</td><td><code>%u</code></td><td>unsigned int</td></tr>
<tr><td><code>%ld</code></td><td>long int</td><td><code>%o</code> / <code>%x</code></td><td>octal / hexadecimal</td></tr>
<tr><td><code>%hd</code></td><td>short int</td><td><code>%e</code></td><td>float (exponent)</td></tr>
</table>
@@scanf_ex@@
<p><b>Field width:</b> <code>%2d</code> reads at most 2 digits; e.g. input <code>12345</code> with <code>scanf("%2d%3d", &amp;a, &amp;b)</code> gives a = 12, b = 345.</p>""",
          r"""<p><code>scanf()</code> keyboard પરથી <b>formatted data</b> (int, float, char, string, …) વાંચે છે.</p>
<p><b>Syntax:</b> <code>scanf("control string", &amp;var1, &amp;var2, …);</code></p>
<ul>
<li><b>Control string</b> માં <b>format specifiers</b> (<code>%</code> થી શરૂ) હોય છે જે વાંચવાના data નો પ્રકાર જણાવે છે.</li>
<li>દરેક variable નામ પહેલાં <b>address-of operator &amp;</b> લખવો જ પડે, કારણ કે scanf મૂલ્ય તે address પર સંગ્રહે છે (strings / arrays માટે જરૂરી નથી).</li>
<li>Inputs space, tab અથવા Enter થી અલગ કરાય છે.</li>
<li>scanf સફળતાપૂર્વક વાંચેલા મૂલ્યોની સંખ્યા return કરે છે.</li>
</ul>
<h4>Format specifiers</h4>
<table>
<tr><th>Specifier</th><th>Data type</th><th>Specifier</th><th>Data type</th></tr>
<tr><td><code>%d</code> / <code>%i</code></td><td>int</td><td><code>%c</code></td><td>char</td></tr>
<tr><td><code>%f</code></td><td>float</td><td><code>%s</code></td><td>string</td></tr>
<tr><td><code>%lf</code></td><td>double</td><td><code>%u</code></td><td>unsigned int</td></tr>
<tr><td><code>%ld</code></td><td>long int</td><td><code>%o</code> / <code>%x</code></td><td>octal / hexadecimal</td></tr>
<tr><td><code>%hd</code></td><td>short int</td><td><code>%e</code></td><td>float (exponent)</td></tr>
</table>
@@scanf_ex@@
<p><b>Field width:</b> <code>%2d</code> વધુમાં વધુ 2 અંક વાંચે; દા.ત. <code>scanf("%2d%3d", &amp;a, &amp;b)</code> માં input <code>12345</code> આપતાં a = 12, b = 345.</p>""",
          programs=["c1p2"]),

        T("1.5.4 Formatted Output – printf()", "1.5.4 Formatted Output – printf()",
          r"""<p><code>printf()</code> displays <b>formatted output</b> on the screen.</p>
<p><b>Syntax:</b></p>
@@printf_syn@@
<p>The control string may contain: (1) <b>characters</b> printed as they are, (2) <b>format specifiers</b> (<code>%d, %f, …</code>) replaced by the values of the arguments, (3) <b>escape sequences</b> (<code>\n, \t</code>).</p>
<h4>Format specification: %[flag][width][.precision]type</h4>
<ul>
<li><b>width</b> – minimum number of columns.</li>
<li><b>.precision</b> – digits after decimal point (for float) or maximum characters (for strings).</li>
<li><b>flags</b> – <code>-</code> left justify, <code>0</code> pad with zeros, <code>+</code> show sign.</li>
</ul>
<table>
<tr><th>Statement</th><th>Output (□ = space)</th></tr>
<tr><td><code>printf("%d", 9876)</code></td><td>9876</td></tr>
<tr><td><code>printf("%6d", 9876)</code></td><td>□□9876</td></tr>
<tr><td><code>printf("%-6d", 9876)</code></td><td>9876□□</td></tr>
<tr><td><code>printf("%06d", 9876)</code></td><td>009876</td></tr>
<tr><td><code>printf("%2d", 9876)</code></td><td>9876 (width ignored)</td></tr>
<tr><td><code>printf("%.2f", 98.7654)</code></td><td>98.77</td></tr>
<tr><td><code>printf("%8.2f", 98.7654)</code></td><td>□□□98.77</td></tr>
<tr><td><code>printf("%e", 98.7654)</code></td><td>9.876540e+01</td></tr>
<tr><td><code>printf("%10s", "GTU")</code></td><td>□□□□□□□GTU</td></tr>
<tr><td><code>printf("%.2s", "GTU")</code></td><td>GT</td></tr>
</table>""",
          r"""<p><code>printf()</code> screen પર <b>formatted output</b> દર્શાવે છે.</p>
<p><b>Syntax:</b></p>
@@printf_syn@@
<p>Control string માં હોઈ શકે: (1) જેમ છે તેમ છપાતા <b>characters</b>, (2) arguments ના મૂલ્યોથી બદલાતા <b>format specifiers</b> (<code>%d, %f, …</code>), (3) <b>escape sequences</b> (<code>\n, \t</code>).</p>
<h4>Format specification: %[flag][width][.precision]type</h4>
<ul>
<li><b>width</b> – ઓછામાં ઓછા columns.</li>
<li><b>.precision</b> – દશાંશ પછીના અંકો (float માટે) અથવા વધુમાં વધુ characters (strings માટે).</li>
<li><b>flags</b> – <code>-</code> ડાબે ગોઠવે, <code>0</code> શૂન્યથી ભરે, <code>+</code> ચિહ્ન બતાવે.</li>
</ul>
<table>
<tr><th>Statement</th><th>Output (□ = space)</th></tr>
<tr><td><code>printf("%d", 9876)</code></td><td>9876</td></tr>
<tr><td><code>printf("%6d", 9876)</code></td><td>□□9876</td></tr>
<tr><td><code>printf("%-6d", 9876)</code></td><td>9876□□</td></tr>
<tr><td><code>printf("%06d", 9876)</code></td><td>009876</td></tr>
<tr><td><code>printf("%2d", 9876)</code></td><td>9876 (width અવગણાય)</td></tr>
<tr><td><code>printf("%.2f", 98.7654)</code></td><td>98.77</td></tr>
<tr><td><code>printf("%8.2f", 98.7654)</code></td><td>□□□98.77</td></tr>
<tr><td><code>printf("%e", 98.7654)</code></td><td>9.876540e+01</td></tr>
<tr><td><code>printf("%10s", "GTU")</code></td><td>□□□□□□□GTU</td></tr>
<tr><td><code>printf("%.2s", "GTU")</code></td><td>GT</td></tr>
</table>""",
          programs=["c1p8"]),

        T("1.5.5 Formatted vs Unformatted I/O", "1.5.5 Formatted vs Unformatted I/O",
          r"""<table>
<tr><th>Formatted I/O</th><th>Unformatted I/O</th></tr>
<tr><td><code>scanf()</code>, <code>printf()</code></td><td><code>getchar(), putchar(), gets(), puts(), getch()</code></td></tr>
<tr><td>Use format specifiers (%d, %f …)</td><td>No format specifiers</td></tr>
<tr><td>Can read/write any data type</td><td>Only characters / strings</td></tr>
<tr><td>Output can be arranged (width, precision)</td><td>No formatting control</td></tr>
<tr><td>Slower, more flexible</td><td>Simple and faster</td></tr>
</table>
<h4>scanf() vs printf()</h4>
<table>
<tr><th>scanf()</th><th>printf()</th></tr>
<tr><td>Input function</td><td>Output function</td></tr>
<tr><td>Needs <code>&amp;</code> (address) before variables</td><td>Variables written without <code>&amp;</code></td></tr>
<tr><td>Returns number of items read</td><td>Returns number of characters printed</td></tr>
</table>""",
          r"""<table>
<tr><th>Formatted I/O</th><th>Unformatted I/O</th></tr>
<tr><td><code>scanf()</code>, <code>printf()</code></td><td><code>getchar(), putchar(), gets(), puts(), getch()</code></td></tr>
<tr><td>Format specifiers (%d, %f …) વાપરે</td><td>Format specifiers નહીં</td></tr>
<tr><td>કોઈપણ data type વાંચી/લખી શકે</td><td>ફક્ત characters / strings</td></tr>
<tr><td>Output ગોઠવી શકાય (width, precision)</td><td>Formatting નિયંત્રણ નહીં</td></tr>
<tr><td>ધીમું, વધુ લવચીક</td><td>સરળ અને ઝડપી</td></tr>
</table>
<h4>scanf() vs printf()</h4>
<table>
<tr><th>scanf()</th><th>printf()</th></tr>
<tr><td>Input function</td><td>Output function</td></tr>
<tr><td>Variables પહેલાં <code>&amp;</code> (address) જોઈએ</td><td>Variables <code>&amp;</code> વગર લખાય</td></tr>
<tr><td>વાંચેલી items ની સંખ્યા return કરે</td><td>છાપેલા characters ની સંખ્યા return કરે</td></tr>
</table>"""),

        T("Key Points – 1.5", "મુખ્ય મુદ્દા – 1.5",
          r"""<ul>
<li>I/O functions are in <code>&lt;stdio.h&gt;</code>.</li>
<li><code>getchar()</code> reads one character; <code>putchar()</code> writes one character.</li>
<li><code>scanf("%d", &amp;a);</code> – <b>&amp;</b> is compulsory for variables.</li>
<li><code>printf("%6.2f", x);</code> – width 6, 2 decimals; <code>-</code> flag left-justifies.</li>
<li>%d int, %f float, %lf double, %c char, %s string, %u unsigned, %ld long.</li>
</ul>""",
          r"""<ul>
<li>I/O functions <code>&lt;stdio.h&gt;</code> માં છે.</li>
<li><code>getchar()</code> એક character વાંચે; <code>putchar()</code> એક character લખે.</li>
<li><code>scanf("%d", &amp;a);</code> – variables માટે <b>&amp;</b> ફરજિયાત.</li>
<li><code>printf("%6.2f", x);</code> – width 6, 2 દશાંશ; <code>-</code> flag ડાબે ગોઠવે.</li>
<li>%d int, %f float, %lf double, %c char, %s string, %u unsigned, %ld long.</li>
</ul>""", key=True),
    ],
}

NOTES_B = [SEC_1_4, SEC_1_5]
