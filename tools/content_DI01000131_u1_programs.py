"""DI01000131 Unit 1 - solved C programs (compiled & run with gcc; output captured automatically)."""
from c_content import P

PROGRAMS = [
    P("c1p1", "Hello World – first C program", "Hello World – પહેલો C program",
      r'''
/* Program to print a message || સંદેશ છાપવાનો program */
#include <stdio.h>          // link section: header file || link section: header file

int main(void)              // execution starts here || અહીંથી execution શરૂ થાય
{
    printf("Hello, World!\n");
    printf("Welcome to C Programming.\n");
    return 0;               // program ended successfully || program સફળતાપૂર્વક પૂરો
}
''', (),
      r"""<ul><li><code>#include &lt;stdio.h&gt;</code> adds the standard input-output header which declares <code>printf()</code>.</li>
<li><code>main()</code> is the function where every C program starts executing.</li>
<li><code>\n</code> is the newline escape sequence; it moves the cursor to the next line.</li>
<li><code>return 0;</code> tells the operating system that the program ended normally.</li></ul>""",
      r"""<ul><li><code>#include &lt;stdio.h&gt;</code> standard input-output header ઉમેરે છે જેમાં <code>printf()</code> declare થયેલું છે.</li>
<li><code>main()</code> એ function છે જ્યાંથી દરેક C program નું execution શરૂ થાય છે.</li>
<li><code>\n</code> newline escape sequence છે; તે cursor ને આગલી line પર લઈ જાય છે.</li>
<li><code>return 0;</code> operating system ને જણાવે છે કે program સામાન્ય રીતે પૂરો થયો.</li></ul>"""),

    P("c1p2", "Sum of two numbers (input from user)", "બે સંખ્યાઓનો સરવાળો (user પાસેથી input)",
      r'''
#include <stdio.h>

int main(void)
{
    int a, b, sum;                       // declaration || declaration (જાહેરાત)

    printf("Enter two numbers: ");
    scanf("%d %d", &a, &b);              // read two integers || બે integers વાંચો

    sum = a + b;                         // process || process (ગણતરી)
    printf("Sum = %d\n", sum);
    return 0;
}
''', ["25 17"],
      r"""<p>This program follows the flowchart <b>Read → Process → Print</b>. <code>scanf()</code> needs the <b>address</b> of each variable, so <code>&amp;a</code> and <code>&amp;b</code> are used. <code>%d</code> is the format specifier for <code>int</code>.</p>""",
      r"""<p>આ program flowchart <b>Read → Process → Print</b> ને અનુસરે છે. <code>scanf()</code> ને દરેક variable નું <b>address</b> જોઈએ, તેથી <code>&amp;a</code> અને <code>&amp;b</code> વપરાય છે. <code>%d</code> એ <code>int</code> માટેનો format specifier છે.</p>"""),

    P("c1p3", "Area and circumference of a circle using symbolic constant", "Symbolic constant વાપરી વર્તુળનું ક્ષેત્રફળ અને પરિઘ",
      r'''
#include <stdio.h>
#define PI 3.14159                     // symbolic constant || symbolic constant

int main(void)
{
    float r, area, circum;

    printf("Enter radius: ");
    scanf("%f", &r);

    area   = PI * r * r;
    circum = 2 * PI * r;

    printf("Area = %.2f\n", area);       // 2 digits after decimal || દશાંશ પછી 2 અંક
    printf("Circumference = %.2f\n", circum);
    return 0;
}
''', ["5"],
      r"""<p><code>#define PI 3.14159</code> creates a <b>symbolic constant</b>. Before compilation the preprocessor replaces every <code>PI</code> with <code>3.14159</code>. <code>%.2f</code> prints a float with 2 digits after the decimal point.</p>""",
      r"""<p><code>#define PI 3.14159</code> <b>symbolic constant</b> બનાવે છે. Compilation પહેલાં preprocessor દરેક <code>PI</code> ની જગ્યાએ <code>3.14159</code> મૂકે છે. <code>%.2f</code> float ને દશાંશ પછી 2 અંક સાથે છાપે છે.</p>"""),

    P("c1p4", "Simple interest", "સાદું વ્યાજ (Simple Interest)",
      r'''
#include <stdio.h>

int main(void)
{
    float p, r, n, si;

    printf("Enter principal amount: ");
    scanf("%f", &p);
    printf("Enter rate of interest (%%): ");   // %% prints % sign || %% થી % ચિહ્ન છપાય
    scanf("%f", &r);
    printf("Enter number of years: ");
    scanf("%f", &n);

    si = (p * r * n) / 100;
    printf("Simple Interest = %.2f\n", si);
    printf("Total Amount    = %.2f\n", p + si);
    return 0;
}
''', ["10000", "8.5", "3"],
      r"""<p>Formula: <b>SI = P × R × N / 100</b>. To print a <code>%</code> sign inside <code>printf()</code>, write <code>%%</code>.</p>""",
      r"""<p>સૂત્ર: <b>SI = P × R × N / 100</b>. <code>printf()</code> માં <code>%</code> ચિહ્ન છાપવા <code>%%</code> લખો.</p>"""),

    P("c1p5", "Convert temperature from Celsius to Fahrenheit", "તાપમાન Celsius થી Fahrenheit માં ફેરવો",
      r'''
#include <stdio.h>

int main(void)
{
    float c, f;

    printf("Enter temperature in Celsius: ");
    scanf("%f", &c);

    f = (9.0 / 5.0) * c + 32;     // use 9.0/5.0, not 9/5 || 9/5 નહીં, 9.0/5.0 વાપરો

    printf("%.2f Celsius = %.2f Fahrenheit\n", c, f);
    return 0;
}
''', ["37"],
      r"""<p>Formula: <b>F = (9/5) × C + 32</b>. In C, <code>9/5</code> is <b>integer division</b> and gives <code>1</code>, which would give a wrong answer. Writing <code>9.0/5.0</code> makes it real division (1.8).</p>""",
      r"""<p>સૂત્ર: <b>F = (9/5) × C + 32</b>. C માં <code>9/5</code> એ <b>integer division</b> છે અને <code>1</code> આપે છે, જેથી ખોટો જવાબ આવે. <code>9.0/5.0</code> લખવાથી real division (1.8) થાય છે.</p>"""),

    P("c1p6", "Swap two numbers (with and without third variable)", "બે સંખ્યાઓની અદલાબદલી (ત્રીજા variable સાથે અને વગર)",
      r'''
#include <stdio.h>

int main(void)
{
    int a, b, temp;

    printf("Enter a and b: ");
    scanf("%d %d", &a, &b);

    /* Method 1: using third variable || રીત 1: ત્રીજો variable વાપરીને */
    temp = a;
    a = b;
    b = temp;
    printf("After swap (temp)   : a = %d, b = %d\n", a, b);

    /* Method 2: without third variable || રીત 2: ત્રીજા variable વગર */
    a = a + b;
    b = a - b;
    a = a - b;
    printf("After swap again    : a = %d, b = %d\n", a, b);
    return 0;
}
''', ["10 20"],
      r"""<p><b>Method 1:</b> the value of <code>a</code> is saved in <code>temp</code>, then <code>a = b</code> and <code>b = temp</code>.</p>
<p><b>Method 2:</b> a = 10 + 20 = 30; b = 30 − 20 = 10; a = 30 − 10 = 20. The second swap brings the numbers back to the original order.</p>""",
      r"""<p><b>રીત 1:</b> <code>a</code> નું મૂલ્ય <code>temp</code> માં સાચવાય, પછી <code>a = b</code> અને <code>b = temp</code>.</p>
<p><b>રીત 2:</b> a = 10 + 20 = 30; b = 30 − 20 = 10; a = 30 − 10 = 20. બીજી અદલાબદલી સંખ્યાઓને મૂળ ક્રમમાં પાછી લાવે છે.</p>"""),

    P("c1p7", "Read a character, print it, its ASCII value and uppercase", "Character વાંચી, તેને, તેની ASCII value અને uppercase છાપો",
      r'''
#include <stdio.h>
#include <ctype.h>                 // for toupper() || toupper() માટે

int main(void)
{
    char ch;

    printf("Enter a character: ");
    ch = getchar();                // read one character || એક character વાંચો

    printf("You entered: ");
    putchar(ch);                   // write one character || એક character લખો
    putchar('\n');

    printf("ASCII value = %d\n", ch);
    printf("Uppercase   = %c\n", toupper(ch));
    return 0;
}
''', ["g"],
      r"""<p><code>getchar()</code> reads <b>one character</b> from the keyboard and <code>putchar()</code> displays one character. A <code>char</code> is stored as its <b>ASCII code</b>, so printing it with <code>%d</code> shows the number (g = 103). <code>toupper()</code> from <code>&lt;ctype.h&gt;</code> converts to uppercase.</p>""",
      r"""<p><code>getchar()</code> keyboard પરથી <b>એક character</b> વાંચે છે અને <code>putchar()</code> એક character દર્શાવે છે. <code>char</code> તેના <b>ASCII code</b> તરીકે સંગ્રહાય છે, તેથી <code>%d</code> થી છાપતાં સંખ્યા દેખાય (g = 103). <code>&lt;ctype.h&gt;</code> નું <code>toupper()</code> uppercase માં ફેરવે છે.</p>"""),

    P("c1p8", "Formatted output with printf() – width, precision and flags", "printf() વડે Formatted output – width, precision અને flags",
      r'''
#include <stdio.h>

int main(void)
{
    int n = 9876;
    float x = 98.7654;

    printf("[%d]\n", n);        // normal || સામાન્ય
    printf("[%6d]\n", n);       // width 6, right aligned || width 6, જમણે
    printf("[%-6d]\n", n);      // left aligned || ડાબે
    printf("[%06d]\n", n);      // padded with zeros || શૂન્યથી ભરેલું
    printf("[%2d]\n", n);       // width less than digits || અંકો કરતાં ઓછી width

    printf("[%f]\n", x);        // 6 decimals by default || default 6 દશાંશ
    printf("[%.2f]\n", x);      // 2 decimals || 2 દશાંશ
    printf("[%8.2f]\n", x);     // width 8, 2 decimals || width 8, 2 દશાંશ
    printf("[%e]\n", x);        // exponent form || exponent સ્વરૂપ

    printf("[%c] [%s]\n", 'A', "GTU");
    printf("[%10s] [%-10s]\n", "GTU", "GTU");
    return 0;
}
''', (),
      r"""<p>The square brackets show the exact space used by each field.</p>
<ul><li><code>%6d</code>: minimum width 6, right justified; <code>%-6d</code>: left justified; <code>%06d</code>: leading zeros.</li>
<li>If the width is smaller than the number (<code>%2d</code>), the full number is still printed.</li>
<li><code>%.2f</code>: 2 digits after the decimal point (rounded); <code>%8.2f</code>: total width 8.</li>
<li><code>%e</code>: exponential (scientific) notation.</li>
<li><code>%f</code> printed 98.765404, not 98.765400, because a <code>float</code> stores only about 6–7 significant digits accurately.</li></ul>""",
      r"""<p>Square brackets દરેક field એ વાપરેલી ચોક્કસ જગ્યા દર્શાવે છે.</p>
<ul><li><code>%6d</code>: ઓછામાં ઓછી width 6, જમણે ગોઠવાય; <code>%-6d</code>: ડાબે ગોઠવાય; <code>%06d</code>: આગળ શૂન્ય.</li>
<li>Width સંખ્યા કરતાં ઓછી હોય (<code>%2d</code>) તો પણ આખી સંખ્યા છપાય.</li>
<li><code>%.2f</code>: દશાંશ પછી 2 અંક (rounded); <code>%8.2f</code>: કુલ width 8.</li>
<li><code>%e</code>: exponential (scientific) સ્વરૂપ.</li>
<li><code>%f</code> એ 98.765400 નહીં પણ 98.765404 છાપ્યું, કારણ કે <code>float</code> ફક્ત લગભગ 6–7 significant અંકો જ ચોક્કસ સંગ્રહે છે.</li></ul>"""),

    P("c1p9", "Arithmetic operators", "Arithmetic operators",
      r'''
#include <stdio.h>

int main(void)
{
    int a, b;

    printf("Enter two integers: ");
    scanf("%d %d", &a, &b);

    printf("a + b = %d\n", a + b);
    printf("a - b = %d\n", a - b);
    printf("a * b = %d\n", a * b);
    printf("a / b = %d\n", a / b);      // integer division || integer division
    printf("a %% b = %d\n", a % b);     // remainder || શેષ
    printf("Real division = %.2f\n", (float)a / b);
    return 0;
}
''', ["17 5"],
      r"""<p>17 / 5 gives <b>3</b> because both operands are integers (fractional part is truncated). <code>17 % 5</code> gives the remainder <b>2</b>. Casting one operand to <code>float</code> gives real division 3.40.</p>""",
      r"""<p>17 / 5 નો જવાબ <b>3</b> આવે કારણ કે બંને operands integers છે (દશાંશ ભાગ કપાઈ જાય). <code>17 % 5</code> શેષ <b>2</b> આપે. એક operand ને <code>float</code> માં cast કરતાં real division 3.40 મળે.</p>"""),

    P("c1p10", "Sum of digits of a three-digit number", "ત્રણ અંકની સંખ્યાના અંકોનો સરવાળો",
      r'''
#include <stdio.h>

int main(void)
{
    int n, d1, d2, d3;

    printf("Enter a 3-digit number: ");
    scanf("%d", &n);

    d3 = n % 10;            // last digit || છેલ્લો અંક
    d2 = (n / 10) % 10;     // middle digit || વચ્ચેનો અંક
    d1 = n / 100;           // first digit || પહેલો અંક

    printf("Digits: %d %d %d\n", d1, d2, d3);
    printf("Sum of digits = %d\n", d1 + d2 + d3);
    printf("Reverse = %d%d%d\n", d3, d2, d1);
    return 0;
}
''', ["472"],
      r"""<p><code>n % 10</code> gives the last digit, <code>n / 10</code> removes the last digit (integer division), and <code>n / 100</code> gives the first digit of a 3-digit number.</p>""",
      r"""<p><code>n % 10</code> છેલ્લો અંક આપે, <code>n / 10</code> છેલ્લો અંક દૂર કરે (integer division), અને <code>n / 100</code> ત્રણ અંકની સંખ્યાનો પહેલો અંક આપે.</p>"""),

    P("c1p11", "Relational and logical operators", "Relational અને logical operators",
      r'''
#include <stdio.h>

int main(void)
{
    int a = 10, b = 20;

    printf("a <  b : %d\n", a < b);
    printf("a >  b : %d\n", a > b);
    printf("a == b : %d\n", a == b);
    printf("a != b : %d\n", a != b);

    printf("(a > 5) && (b > 5) : %d\n", (a > 5) && (b > 5));
    printf("(a > 15) || (b > 15): %d\n", (a > 15) || (b > 15));
    printf("!(a == 10)         : %d\n", !(a == 10));
    return 0;
}
''', (),
      r"""<p>Relational and logical expressions give <b>1 for true</b> and <b>0 for false</b>. <code>&amp;&amp;</code> is true only if both conditions are true; <code>||</code> is true if any one is true; <code>!</code> reverses the result.</p>""",
      r"""<p>Relational અને logical expressions <b>સાચું હોય તો 1</b> અને <b>ખોટું હોય તો 0</b> આપે છે. <code>&amp;&amp;</code> બંને શરતો સાચી હોય ત્યારે જ સાચું; <code>||</code> કોઈ એક સાચી હોય તો સાચું; <code>!</code> પરિણામ ઉલટાવે.</p>"""),

    P("c1p12", "Increment and decrement operators (prefix and postfix)", "Increment અને decrement operators (prefix અને postfix)",
      r'''
#include <stdio.h>

int main(void)
{
    int a = 5, b;

    b = ++a;     // prefix: first increment, then use || prefix: પહેલાં વધારો, પછી ઉપયોગ
    printf("Prefix : a = %d, b = %d\n", a, b);

    a = 5;
    b = a++;     // postfix: first use, then increment || postfix: પહેલાં ઉપયોગ, પછી વધારો
    printf("Postfix: a = %d, b = %d\n", a, b);

    a = 5;
    b = --a;
    printf("--a    : a = %d, b = %d\n", a, b);

    a = 5;
    b = a--;
    printf("a--    : a = %d, b = %d\n", a, b);
    return 0;
}
''', (),
      r"""<ul><li><b>Prefix</b> (<code>++a</code>): the value is incremented first and then the new value is used → a = 6, b = 6.</li>
<li><b>Postfix</b> (<code>a++</code>): the old value is used first and then incremented → b = 5, a = 6.</li></ul>""",
      r"""<ul><li><b>Prefix</b> (<code>++a</code>): પહેલાં મૂલ્ય વધે અને પછી નવું મૂલ્ય વપરાય → a = 6, b = 6.</li>
<li><b>Postfix</b> (<code>a++</code>): પહેલાં જૂનું મૂલ્ય વપરાય અને પછી વધે → b = 5, a = 6.</li></ul>"""),

    P("c1p13", "Largest of three numbers using conditional operator", "Conditional operator વાપરી ત્રણ સંખ્યાઓમાં સૌથી મોટી",
      r'''
#include <stdio.h>

int main(void)
{
    int a, b, c, max;

    printf("Enter three numbers: ");
    scanf("%d %d %d", &a, &b, &c);

    max = (a > b) ? ((a > c) ? a : c) : ((b > c) ? b : c);   // nested ?: || nested ?:

    printf("Largest = %d\n", max);
    return 0;
}
''', ["25 67 43"],
      r"""<p>Syntax: <code>condition ? expr1 : expr2</code>. If <code>a &gt; b</code> is true, we compare a with c, otherwise b with c. This is the same logic as the flowchart <i>Largest of Three Numbers</i>.</p>""",
      r"""<p>Syntax: <code>condition ? expr1 : expr2</code>. <code>a &gt; b</code> સાચું હોય તો a ની c સાથે, નહીં તો b ની c સાથે સરખામણી થાય. આ <i>Largest of Three Numbers</i> flowchart જેવું જ logic છે.</p>"""),

    P("c1p14", "Bitwise operators", "Bitwise operators",
      r'''
#include <stdio.h>

int main(void)
{
    int a = 12, b = 10;     // 12 = 1100, 10 = 1010 || 12 = 1100, 10 = 1010

    printf("a & b  = %d\n", a & b);     // 1000 = 8
    printf("a | b  = %d\n", a | b);     // 1110 = 14
    printf("a ^ b  = %d\n", a ^ b);     // 0110 = 6
    printf("~a     = %d\n", ~a);        // -(a+1) = -13
    printf("a << 2 = %d\n", a << 2);    // 12 x 4 = 48
    printf("a >> 2 = %d\n", a >> 2);    // 12 / 4 = 3
    return 0;
}
''', (),
      r"""<table><tr><th>Operation</th><th>Binary</th><th>Result</th></tr>
<tr><td>12 &amp; 10</td><td>1100 &amp; 1010 = 1000</td><td>8</td></tr>
<tr><td>12 | 10</td><td>1100 | 1010 = 1110</td><td>14</td></tr>
<tr><td>12 ^ 10</td><td>1100 ^ 1010 = 0110</td><td>6</td></tr>
<tr><td>~12</td><td>one's complement</td><td>−13</td></tr>
<tr><td>12 &lt;&lt; 2</td><td>110000</td><td>48 (× 2²)</td></tr>
<tr><td>12 &gt;&gt; 2</td><td>0011</td><td>3 (÷ 2²)</td></tr></table>""",
      r"""<table><tr><th>Operation</th><th>Binary</th><th>પરિણામ</th></tr>
<tr><td>12 &amp; 10</td><td>1100 &amp; 1010 = 1000</td><td>8</td></tr>
<tr><td>12 | 10</td><td>1100 | 1010 = 1110</td><td>14</td></tr>
<tr><td>12 ^ 10</td><td>1100 ^ 1010 = 0110</td><td>6</td></tr>
<tr><td>~12</td><td>one's complement</td><td>−13</td></tr>
<tr><td>12 &lt;&lt; 2</td><td>110000</td><td>48 (× 2²)</td></tr>
<tr><td>12 &gt;&gt; 2</td><td>0011</td><td>3 (÷ 2²)</td></tr></table>"""),

    P("c1p15", "Size of data types using sizeof operator", "sizeof operator વાપરી data types ની size",
      r'''
#include <stdio.h>

int main(void)
{
    printf("char        : %zu byte\n",  sizeof(char));
    printf("short int   : %zu bytes\n", sizeof(short));
    printf("int         : %zu bytes\n", sizeof(int));
    printf("long int    : %zu bytes\n", sizeof(long));
    printf("float       : %zu bytes\n", sizeof(float));
    printf("double      : %zu bytes\n", sizeof(double));
    printf("long double : %zu bytes\n", sizeof(long double));
    return 0;
}
''', (),
      r"""<p>This output is from <b>GCC on a 64-bit Linux system</b>. Sizes depend on the compiler: in the old 16-bit <b>Turbo C</b>, <code>int</code> is 2 bytes, <code>long</code> is 4 bytes and <code>long double</code> is 10 bytes. <code>%zu</code> is the format specifier for the result of <code>sizeof</code> (in Turbo C use <code>%d</code>).</p>""",
      r"""<p>આ output <b>64-bit Linux પર GCC</b> નું છે. Sizes compiler પર આધાર રાખે છે: જૂના 16-bit <b>Turbo C</b> માં <code>int</code> 2 bytes, <code>long</code> 4 bytes અને <code>long double</code> 10 bytes હોય છે. <code>%zu</code> એ <code>sizeof</code> ના પરિણામ માટેનો format specifier છે (Turbo C માં <code>%d</code> વાપરો).</p>"""),

    P("c1p16", "Average of marks – implicit and explicit type conversion", "ગુણની સરેરાશ – implicit અને explicit type conversion",
      r'''
#include <stdio.h>

int main(void)
{
    int m1 = 75, m2 = 82, m3 = 90, total;
    float avg1, avg2;

    total = m1 + m2 + m3;              // 247

    avg1 = total / 3;                  // int / int = 82 (fraction lost) || int / int = 82 (દશાંશ ગુમાવ્યો)
    avg2 = (float) total / 3;          // explicit cast || explicit cast

    printf("Total = %d\n", total);
    printf("Average without cast = %.2f\n", avg1);
    printf("Average with cast    = %.2f\n", avg2);
    return 0;
}
''', (),
      r"""<p><code>total / 3</code> is integer division, so 247 / 3 = 82; only then is it converted to float (82.00) – the fraction is lost. With <code>(float) total</code> the division is done in float: 247.0 / 3 = 82.33.</p>""",
      r"""<p><code>total / 3</code> integer division છે, તેથી 247 / 3 = 82; પછી જ float (82.00) માં ફેરવાય – દશાંશ ગુમાઈ જાય. <code>(float) total</code> સાથે division float માં થાય: 247.0 / 3 = 82.33.</p>"""),
]

if __name__ == "__main__":
    for p in PROGRAMS:
        print("=====", p["id"], p["title"]["en"]); print(p["out"])
