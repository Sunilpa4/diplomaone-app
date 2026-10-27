"""DI01000131 Unit 1 notes part A: 1.1 Flowchart, 1.2 Algorithm, 1.3 Overview of C"""
from c_content import make_T

SN = {
    "structure_ex": r'''
/* Program: Area of circle        (Documentation) || Program: વર્તુળનું ક્ષેત્રફળ   (Documentation) */
#include <stdio.h>               /* Link section || Link section */
#define PI 3.14                  /* Definition section || Definition section */

float area;                      /* Global declaration || Global declaration */

int main(void)                   /* main() function || main() function */
{
    float r = 5;                 /* Declaration part || Declaration part */
    area = PI * r * r;           /* Executable part || Executable part */
    printf("Area = %.2f\n", area);
    return 0;
}
''',
    "gcc_cmd": r'''
$ gcc prog.c -o prog      (compile + link)
$ ./prog                  (run)
''',
}
T = make_T(SN)

# =====================================================================================
SEC_1_1 = {
    "title": {"en": "1.1 Flowchart", "gu": "1.1 Flowchart"},
    "items": [
        T("1.1.1 Definition and Symbols of Flowchart", "1.1.1 Flowchart ની વ્યાખ્યા અને Symbols",
          r"""<p><b>Definition:</b> A <b>flowchart</b> is a <b>pictorial (graphical) representation</b> of the steps of an algorithm or program, drawn using <b>standard symbols</b> connected by <b>arrows</b> that show the flow of control.</p>
<p>It shows <i>what</i> is done at each step and <i>in which order</i>. Flowcharts are drawn before writing a program to plan the logic.</p>
<h4>Standard flowchart symbols (see diagram)</h4>
<table>
<tr><th>Symbol</th><th>Name</th><th>Purpose</th></tr>
<tr><td>Oval / rounded rectangle</td><td><b>Terminal</b></td><td>Start and Stop of the flowchart</td></tr>
<tr><td>Parallelogram</td><td><b>Input / Output</b></td><td>Read input data or print output (READ, PRINT)</td></tr>
<tr><td>Rectangle</td><td><b>Process</b></td><td>Calculations, assignments (e.g. SUM = A + B)</td></tr>
<tr><td>Diamond (rhombus)</td><td><b>Decision</b></td><td>Checking a condition; has two exits: Yes / No (True / False)</td></tr>
<tr><td>Arrow</td><td><b>Flow line</b></td><td>Shows the direction of flow of steps</td></tr>
<tr><td>Small circle</td><td><b>Connector</b></td><td>Joins two parts of a flowchart (on the same page) when lines would cross or the chart is long</td></tr>
<tr><td>Rectangle with double side lines</td><td><b>Predefined process</b></td><td>A function / sub-program defined elsewhere</td></tr>
</table>""",
          r"""<p><b>વ્યાખ્યા:</b> <b>Flowchart</b> એ algorithm અથવા program ના steps નું <b>ચિત્રાત્મક (graphical) રજૂઆત</b> છે, જે <b>standard symbols</b> અને flow of control દર્શાવતા <b>arrows</b> વડે દોરાય છે.</p>
<p>તે દરેક step માં <i>શું</i> થાય છે અને <i>કયા ક્રમમાં</i> થાય છે તે બતાવે છે. Logic નું આયોજન કરવા program લખતા પહેલાં flowchart દોરાય છે.</p>
<h4>Standard flowchart symbols (આકૃતિ જુઓ)</h4>
<table>
<tr><th>Symbol</th><th>નામ</th><th>હેતુ</th></tr>
<tr><td>Oval / ગોળ ખૂણાવાળો લંબચોરસ</td><td><b>Terminal</b></td><td>Flowchart ની શરૂઆત (Start) અને અંત (Stop)</td></tr>
<tr><td>Parallelogram (સમાંતરબાજુ ચતુષ્કોણ)</td><td><b>Input / Output</b></td><td>Input data વાંચવા અથવા output છાપવા (READ, PRINT)</td></tr>
<tr><td>Rectangle (લંબચોરસ)</td><td><b>Process</b></td><td>ગણતરી, assignment (દા.ત. SUM = A + B)</td></tr>
<tr><td>Diamond (સમચતુષ્કોણ)</td><td><b>Decision</b></td><td>શરત ચકાસવા; બે માર્ગ: Yes / No (True / False)</td></tr>
<tr><td>Arrow (તીર)</td><td><b>Flow line</b></td><td>Steps ના પ્રવાહની દિશા દર્શાવે</td></tr>
<tr><td>નાનું વર્તુળ</td><td><b>Connector</b></td><td>Lines ઓળંગાતી હોય કે chart લાંબો હોય ત્યારે flowchart ના બે ભાગ જોડે</td></tr>
<tr><td>બંને બાજુ બેવડી line વાળો લંબચોરસ</td><td><b>Predefined process</b></td><td>બીજે વ્યાખ્યાયિત function / sub-program</td></tr>
</table>""",
          diagram="c1_fc_symbols"),

        T("1.1.2 Rules, Advantages and Disadvantages of Flowchart", "1.1.2 Flowchart ના નિયમો, ફાયદા અને ગેરફાયદા",
          r"""<h4>Rules (guidelines) for drawing a flowchart</h4>
<ol>
<li>Every flowchart must have exactly one <b>Start</b> and at least one <b>Stop</b> terminal.</li>
<li>Use only <b>standard symbols</b>.</li>
<li>The flow should be from <b>top to bottom</b> and <b>left to right</b>.</li>
<li>Flow lines should not cross each other; use <b>connectors</b> if needed.</li>
<li>A process symbol has one entry and one exit; a <b>decision</b> symbol has one entry and <b>two exits</b> (Yes / No).</li>
<li>Write statements inside symbols <b>briefly and clearly</b>.</li>
<li>The flowchart should be neat, simple and easy to follow.</li>
</ol>
<h4>Advantages</h4>
<ul>
<li><b>Easy to understand:</b> a picture is easier to understand than text.</li>
<li><b>Better communication</b> of logic to other programmers.</li>
<li><b>Effective analysis:</b> problems can be analysed and logic errors found easily.</li>
<li>Acts as a <b>guide (blueprint)</b> while writing the program – <b>efficient coding</b>.</li>
<li><b>Proper documentation</b> of the program.</li>
<li>Helps in <b>debugging</b> and <b>program maintenance</b>.</li>
</ul>
<h4>Disadvantages</h4>
<ul>
<li>Drawing flowcharts for <b>large, complex programs</b> is time-consuming and difficult.</li>
<li>If the logic changes, the flowchart must be <b>redrawn</b> (difficult to modify).</li>
<li>No standard for the <b>level of detail</b> to be shown.</li>
<li>Takes more space; reproduction is difficult.</li>
<li>It is not a program – it must still be converted into a programming language.</li>
</ul>""",
          r"""<h4>Flowchart દોરવાના નિયમો (guidelines)</h4>
<ol>
<li>દરેક flowchart માં બરાબર એક <b>Start</b> અને ઓછામાં ઓછું એક <b>Stop</b> terminal હોવું જોઈએ.</li>
<li>ફક્ત <b>standard symbols</b> વાપરો.</li>
<li>પ્રવાહ <b>ઉપરથી નીચે</b> અને <b>ડાબેથી જમણે</b> હોવો જોઈએ.</li>
<li>Flow lines એકબીજાને ઓળંગવી ન જોઈએ; જરૂર હોય તો <b>connectors</b> વાપરો.</li>
<li>Process symbol માં એક entry અને એક exit હોય; <b>decision</b> symbol માં એક entry અને <b>બે exits</b> (Yes / No) હોય.</li>
<li>Symbols ની અંદર statements <b>ટૂંકા અને સ્પષ્ટ</b> લખો.</li>
<li>Flowchart સ્વચ્છ, સરળ અને સમજવામાં સહેલો હોવો જોઈએ.</li>
</ol>
<h4>ફાયદા</h4>
<ul>
<li><b>સમજવામાં સરળ:</b> લખાણ કરતાં ચિત્ર સહેલાઈથી સમજાય.</li>
<li>બીજા programmers ને logic ની <b>વધુ સારી રજૂઆત (communication)</b>.</li>
<li><b>અસરકારક analysis:</b> problem નું analysis અને logic errors સહેલાઈથી શોધી શકાય.</li>
<li>Program લખતી વખતે <b>માર્ગદર્શક (blueprint)</b> તરીકે કામ કરે – <b>efficient coding</b>.</li>
<li>Program નું <b>યોગ્ય documentation</b>.</li>
<li><b>Debugging</b> અને <b>program maintenance</b> માં મદદરૂપ.</li>
</ul>
<h4>ગેરફાયદા</h4>
<ul>
<li><b>મોટા, જટિલ programs</b> માટે flowchart દોરવો સમય માંગી લે અને મુશ્કેલ છે.</li>
<li>Logic બદલાય તો flowchart <b>ફરીથી દોરવો</b> પડે (ફેરફાર મુશ્કેલ).</li>
<li>કેટલી <b>વિગત</b> બતાવવી તેનું કોઈ standard નથી.</li>
<li>વધુ જગ્યા લે; નકલ કરવી મુશ્કેલ.</li>
<li>તે program નથી – તેને programming language માં ફેરવવો જ પડે.</li>
</ul>"""),

        T("1.1.3 Flowchart Example – Sum of Two Numbers", "1.1.3 Flowchart ઉદાહરણ – બે સંખ્યાઓનો સરવાળો",
          r"""<p>This is a <b>sequential</b> flowchart – the steps are executed one after another without any decision.</p>
<ol>
<li><b>Start</b></li>
<li><b>Input:</b> Read two numbers A and B (parallelogram).</li>
<li><b>Process:</b> SUM = A + B (rectangle).</li>
<li><b>Output:</b> Print SUM (parallelogram).</li>
<li><b>Stop</b></li>
</ol>
<p>Most simple programs follow this pattern: <b>Input → Process → Output</b>. The C program for this flowchart is given in topic 1.5.3.</p>""",
          r"""<p>આ <b>sequential</b> flowchart છે – કોઈ decision વગર steps એક પછી એક execute થાય છે.</p>
<ol>
<li><b>Start</b></li>
<li><b>Input:</b> બે સંખ્યાઓ A અને B વાંચો (parallelogram).</li>
<li><b>Process:</b> SUM = A + B (rectangle).</li>
<li><b>Output:</b> SUM છાપો (parallelogram).</li>
<li><b>Stop</b></li>
</ol>
<p>મોટા ભાગના સરળ programs આ pattern અનુસરે છે: <b>Input → Process → Output</b>. આ flowchart નો C program topic 1.5.3 માં આપેલ છે.</p>""",
          diagram="c1_fc_sum"),

        T("1.1.4 Flowchart Example – Largest of Three Numbers", "1.1.4 Flowchart ઉદાહરણ – ત્રણ સંખ્યાઓમાં સૌથી મોટી",
          r"""<p>This flowchart uses <b>decision</b> (diamond) symbols – an example of <b>branching</b>.</p>
<ol>
<li>Start; read A, B, C.</li>
<li>Is A &gt; B?
<ul><li><b>Yes</b> → Is A &gt; C? Yes → print A; No → print C.</li>
<li><b>No</b> → Is B &gt; C? Yes → print B; No → print C.</li></ul></li>
<li>Stop.</li>
</ol>
<p><b>Dry run:</b> A = 25, B = 67, C = 43 → A &gt; B? No → B &gt; C? Yes → print <b>67</b>.</p>""",
          r"""<p>આ flowchart <b>decision</b> (diamond) symbols વાપરે છે – <b>branching</b> નું ઉદાહરણ.</p>
<ol>
<li>Start; A, B, C વાંચો.</li>
<li>A &gt; B છે?
<ul><li><b>Yes</b> → A &gt; C છે? Yes → A છાપો; No → C છાપો.</li>
<li><b>No</b> → B &gt; C છે? Yes → B છાપો; No → C છાપો.</li></ul></li>
<li>Stop.</li>
</ol>
<p><b>Dry run:</b> A = 25, B = 67, C = 43 → A &gt; B? No → B &gt; C? Yes → <b>67</b> છાપો.</p>""",
          diagram="c1_fc_largest", programs=["c1p13"]),

        T("1.1.5 Flowchart Example – Factorial of a Number (Loop)", "1.1.5 Flowchart ઉદાહરણ – સંખ્યાનો Factorial (Loop)",
          r"""<p>Factorial: N! = 1 × 2 × 3 × … × N. This flowchart shows a <b>loop (iteration)</b> – a set of steps repeated while a condition is true.</p>
<ol>
<li>Start; read N.</li>
<li>Initialise F = 1, i = 1.</li>
<li>Is i ≤ N? If <b>Yes</b>: F = F × i, i = i + 1 and go back to the condition.</li>
<li>If <b>No</b>: print F; Stop.</li>
</ol>
<p><b>Dry run (N = 4):</b></p>
<table><tr><th>i</th><th>i ≤ 4?</th><th>F = F × i</th></tr>
<tr><td>1</td><td>Yes</td><td>1</td></tr><tr><td>2</td><td>Yes</td><td>2</td></tr>
<tr><td>3</td><td>Yes</td><td>6</td></tr><tr><td>4</td><td>Yes</td><td>24</td></tr>
<tr><td>5</td><td>No</td><td>print 24</td></tr></table>
<p>The three basic structures of any logic are: <b>sequence</b> (1.1.3), <b>selection / decision</b> (1.1.4) and <b>iteration / loop</b> (1.1.5).</p>""",
          r"""<p>Factorial: N! = 1 × 2 × 3 × … × N. આ flowchart <b>loop (iteration)</b> બતાવે છે – શરત સાચી હોય ત્યાં સુધી steps નું પુનરાવર્તન.</p>
<ol>
<li>Start; N વાંચો.</li>
<li>F = 1, i = 1 initialise કરો.</li>
<li>i ≤ N છે? <b>Yes</b> હોય તો: F = F × i, i = i + 1 અને ફરી શરત પર જાઓ.</li>
<li><b>No</b> હોય તો: F છાપો; Stop.</li>
</ol>
<p><b>Dry run (N = 4):</b></p>
<table><tr><th>i</th><th>i ≤ 4?</th><th>F = F × i</th></tr>
<tr><td>1</td><td>Yes</td><td>1</td></tr><tr><td>2</td><td>Yes</td><td>2</td></tr>
<tr><td>3</td><td>Yes</td><td>6</td></tr><tr><td>4</td><td>Yes</td><td>24</td></tr>
<tr><td>5</td><td>No</td><td>24 છાપો</td></tr></table>
<p>કોઈપણ logic ના ત્રણ મૂળભૂત structures: <b>sequence</b> (1.1.3), <b>selection / decision</b> (1.1.4) અને <b>iteration / loop</b> (1.1.5).</p>""",
          diagram="c1_fc_factorial"),

        T("Key Points – 1.1", "મુખ્ય મુદ્દા – 1.1",
          r"""<ul>
<li>Flowchart = <b>pictorial representation</b> of an algorithm using standard symbols.</li>
<li>Oval → Start/Stop; parallelogram → Input/Output; rectangle → Process; diamond → Decision; circle → Connector.</li>
<li>Decision symbol has <b>two exits</b> (Yes/No); flow is top-to-bottom.</li>
<li>Advantages: easy understanding, communication, analysis, documentation, debugging.</li>
<li>Disadvantages: hard for complex logic, difficult to modify, time-consuming.</li>
<li>Three structures: <b>sequence, selection, iteration</b>.</li>
</ul>""",
          r"""<ul>
<li>Flowchart = standard symbols વડે algorithm ની <b>ચિત્રાત્મક રજૂઆત</b>.</li>
<li>Oval → Start/Stop; parallelogram → Input/Output; rectangle → Process; diamond → Decision; circle → Connector.</li>
<li>Decision symbol માં <b>બે exits</b> (Yes/No); પ્રવાહ ઉપરથી નીચે.</li>
<li>ફાયદા: સરળ સમજ, communication, analysis, documentation, debugging.</li>
<li>ગેરફાયદા: જટિલ logic માટે મુશ્કેલ, ફેરફાર મુશ્કેલ, સમય માંગી લે.</li>
<li>ત્રણ structures: <b>sequence, selection, iteration</b>.</li>
</ul>""", key=True),
    ],
}

# =====================================================================================
SEC_1_2 = {
    "title": {"en": "1.2 Algorithm", "gu": "1.2 Algorithm"},
    "items": [
        T("1.2.1 Definition and Characteristics of Algorithm", "1.2.1 Algorithm ની વ્યાખ્યા અને લાક્ષણિકતાઓ",
          r"""<p><b>Definition:</b> An <b>algorithm</b> is a <b>finite set of well-defined, step-by-step instructions</b> for solving a particular problem. The word comes from the name of the Persian mathematician <b>Al-Khwarizmi</b>.</p>
<p>An algorithm is written in simple English-like language, independent of any programming language. A program is an algorithm written in a programming language.</p>
<h4>Characteristics (properties) of a good algorithm</h4>
<ol>
<li><b>Input:</b> It takes zero or more inputs.</li>
<li><b>Output:</b> It produces at least one output (result).</li>
<li><b>Definiteness:</b> Each step must be clear and unambiguous (only one meaning).</li>
<li><b>Finiteness:</b> It must terminate after a finite number of steps.</li>
<li><b>Effectiveness:</b> Each step must be basic enough to be carried out (by hand, with pen and paper) in finite time.</li>
<li><b>Generality / language independence:</b> It should solve all problems of a given type and can be coded in any language.</li>
</ol>""",
          r"""<p><b>વ્યાખ્યા:</b> <b>Algorithm</b> એ કોઈ ચોક્કસ problem ઉકેલવા માટેની <b>સ્પષ્ટ રીતે વ્યાખ્યાયિત, step-by-step સૂચનાઓનો મર્યાદિત (finite) સમૂહ</b> છે. આ શબ્દ ફારસી ગણિતશાસ્ત્રી <b>Al-Khwarizmi</b> ના નામ પરથી આવ્યો છે.</p>
<p>Algorithm કોઈપણ programming language થી સ્વતંત્ર, સાદી English જેવી ભાષામાં લખાય છે. Programming language માં લખેલો algorithm એટલે program.</p>
<h4>સારા algorithm ની લાક્ષણિકતાઓ (properties)</h4>
<ol>
<li><b>Input:</b> શૂન્ય અથવા વધુ inputs લે.</li>
<li><b>Output:</b> ઓછામાં ઓછું એક output (પરિણામ) આપે.</li>
<li><b>Definiteness (સ્પષ્ટતા):</b> દરેક step સ્પષ્ટ અને એક જ અર્થવાળું હોવું જોઈએ.</li>
<li><b>Finiteness (મર્યાદિતતા):</b> મર્યાદિત steps પછી પૂરું થવું જોઈએ.</li>
<li><b>Effectiveness (અસરકારકતા):</b> દરેક step એટલું સરળ હોવું જોઈએ કે મર્યાદિત સમયમાં (કાગળ-પેનથી) કરી શકાય.</li>
<li><b>Generality / language independence:</b> તે પ્રકારના બધા problems ઉકેલે અને કોઈપણ language માં code થઈ શકે.</li>
</ol>"""),

        T("1.2.2 Writing Algorithms using Pseudo Code", "1.2.2 Pseudo Code વાપરી Algorithm લખવું",
          r"""<p><b>Pseudo code</b> ("false code") is an informal, English-like way of writing an algorithm that looks similar to a program but does not follow the exact syntax of any language. It is meant for humans, not for the computer.</p>
<h4>Common pseudo-code keywords</h4>
<table>
<tr><th>Purpose</th><th>Keywords</th></tr>
<tr><td>Start / end</td><td>START (BEGIN), STOP (END)</td></tr>
<tr><td>Input</td><td>READ, INPUT, GET</td></tr>
<tr><td>Output</td><td>PRINT, DISPLAY, WRITE</td></tr>
<tr><td>Process</td><td>COMPUTE, CALCULATE, SET, ← (assignment)</td></tr>
<tr><td>Decision</td><td>IF … THEN … ELSE … ENDIF</td></tr>
<tr><td>Loop</td><td>WHILE … DO … ENDWHILE, FOR … TO … ENDFOR, REPEAT … UNTIL</td></tr>
</table>
<h4>Steps to develop an algorithm</h4>
<ol>
<li>Understand the problem: identify the <b>input</b>, required <b>output</b> and the <b>formula / logic</b>.</li>
<li>Write the steps in order, numbered Step 1, Step 2, …</li>
<li>Use proper keywords and indentation for decisions and loops.</li>
<li>Check (dry run) with sample data.</li>
</ol>
<h4>Example: area of a rectangle</h4>
<p>Step 1: START<br>Step 2: READ length L, breadth B<br>Step 3: AREA ← L × B<br>Step 4: PRINT AREA<br>Step 5: STOP</p>""",
          r"""<p><b>Pseudo code</b> ("ખોટો code") એ algorithm લખવાની અનૌપચારિક, English જેવી રીત છે જે program જેવી દેખાય છે પણ કોઈ language ની ચોક્કસ syntax ને અનુસરતી નથી. તે computer માટે નહીં પણ માણસો માટે છે.</p>
<h4>સામાન્ય pseudo-code keywords</h4>
<table>
<tr><th>હેતુ</th><th>Keywords</th></tr>
<tr><td>શરૂ / અંત</td><td>START (BEGIN), STOP (END)</td></tr>
<tr><td>Input</td><td>READ, INPUT, GET</td></tr>
<tr><td>Output</td><td>PRINT, DISPLAY, WRITE</td></tr>
<tr><td>Process</td><td>COMPUTE, CALCULATE, SET, ← (assignment)</td></tr>
<tr><td>Decision</td><td>IF … THEN … ELSE … ENDIF</td></tr>
<tr><td>Loop</td><td>WHILE … DO … ENDWHILE, FOR … TO … ENDFOR, REPEAT … UNTIL</td></tr>
</table>
<h4>Algorithm વિકસાવવાના steps</h4>
<ol>
<li>Problem સમજો: <b>input</b>, જરૂરી <b>output</b> અને <b>સૂત્ર / logic</b> ઓળખો.</li>
<li>Steps ક્રમમાં લખો, Step 1, Step 2, … નંબર આપીને.</li>
<li>Decisions અને loops માટે યોગ્ય keywords અને indentation વાપરો.</li>
<li>નમૂનાના data સાથે ચકાસો (dry run).</li>
</ol>
<h4>ઉદાહરણ: લંબચોરસનું ક્ષેત્રફળ</h4>
<p>Step 1: START<br>Step 2: લંબાઈ L, પહોળાઈ B READ કરો<br>Step 3: AREA ← L × B<br>Step 4: AREA PRINT કરો<br>Step 5: STOP</p>"""),

        T("1.2.3 Algorithm Examples", "1.2.3 Algorithm ના ઉદાહરણો",
          r"""<h4>1. Simple interest</h4>
<p>Step 1: START<br>Step 2: READ P, R, N<br>Step 3: SI ← (P × R × N) / 100<br>Step 4: PRINT SI<br>Step 5: STOP</p>
<h4>2. Check whether a number is even or odd</h4>
<p>Step 1: START<br>Step 2: READ N<br>Step 3: IF N MOD 2 = 0 THEN PRINT "Even" ELSE PRINT "Odd"<br>Step 4: STOP</p>
<h4>3. Largest of three numbers</h4>
<p>Step 1: START<br>Step 2: READ A, B, C<br>Step 3: IF A &gt; B AND A &gt; C THEN PRINT A<br>Step 4: ELSE IF B &gt; C THEN PRINT B<br>Step 5: ELSE PRINT C<br>Step 6: STOP</p>
<h4>4. Factorial of N</h4>
<p>Step 1: START<br>Step 2: READ N<br>Step 3: F ← 1, I ← 1<br>Step 4: WHILE I ≤ N DO<br>&nbsp;&nbsp;&nbsp;&nbsp;F ← F × I<br>&nbsp;&nbsp;&nbsp;&nbsp;I ← I + 1<br>&nbsp;&nbsp;&nbsp;ENDWHILE<br>Step 5: PRINT F<br>Step 6: STOP</p>
<h4>5. Sum of first N natural numbers</h4>
<p>Step 1: START<br>Step 2: READ N<br>Step 3: SUM ← 0, I ← 1<br>Step 4: REPEAT SUM ← SUM + I, I ← I + 1 UNTIL I &gt; N<br>Step 5: PRINT SUM<br>Step 6: STOP</p>""",
          r"""<h4>1. સાદું વ્યાજ</h4>
<p>Step 1: START<br>Step 2: P, R, N READ કરો<br>Step 3: SI ← (P × R × N) / 100<br>Step 4: SI PRINT કરો<br>Step 5: STOP</p>
<h4>2. સંખ્યા even છે કે odd તે ચકાસો</h4>
<p>Step 1: START<br>Step 2: N READ કરો<br>Step 3: IF N MOD 2 = 0 THEN "Even" PRINT કરો ELSE "Odd" PRINT કરો<br>Step 4: STOP</p>
<h4>3. ત્રણ સંખ્યાઓમાં સૌથી મોટી</h4>
<p>Step 1: START<br>Step 2: A, B, C READ કરો<br>Step 3: IF A &gt; B AND A &gt; C THEN A PRINT કરો<br>Step 4: ELSE IF B &gt; C THEN B PRINT કરો<br>Step 5: ELSE C PRINT કરો<br>Step 6: STOP</p>
<h4>4. N નો Factorial</h4>
<p>Step 1: START<br>Step 2: N READ કરો<br>Step 3: F ← 1, I ← 1<br>Step 4: WHILE I ≤ N DO<br>&nbsp;&nbsp;&nbsp;&nbsp;F ← F × I<br>&nbsp;&nbsp;&nbsp;&nbsp;I ← I + 1<br>&nbsp;&nbsp;&nbsp;ENDWHILE<br>Step 5: F PRINT કરો<br>Step 6: STOP</p>
<h4>5. પ્રથમ N પ્રાકૃતિક સંખ્યાઓનો સરવાળો</h4>
<p>Step 1: START<br>Step 2: N READ કરો<br>Step 3: SUM ← 0, I ← 1<br>Step 4: REPEAT SUM ← SUM + I, I ← I + 1 UNTIL I &gt; N<br>Step 5: SUM PRINT કરો<br>Step 6: STOP</p>""",
          programs=["c1p4"]),

        T("1.2.4 Advantages and Disadvantages of Algorithm; Algorithm vs Flowchart", "1.2.4 Algorithm ના ફાયદા-ગેરફાયદા; Algorithm vs Flowchart",
          r"""<h4>Advantages of algorithm</h4>
<ul>
<li>Step-by-step representation – <b>easy to understand</b>.</li>
<li><b>Language independent</b> – can be converted into any programming language.</li>
<li>Breaks a problem into small steps; makes it <b>easy to write the program</b>.</li>
<li>Easy to <b>find errors</b> (debug) in logic before coding.</li>
<li>Easy to modify compared with a flowchart; no special symbols needed.</li>
</ul>
<h4>Disadvantages of algorithm</h4>
<ul>
<li><b>Time-consuming</b> to write for large problems.</li>
<li>Branching and looping are <b>difficult to show</b> clearly in text.</li>
<li>Not as easy to understand at a glance as a flowchart (no picture).</li>
<li>No standard rules for writing pseudo code.</li>
</ul>
<h4>Difference between algorithm and flowchart</h4>
<table>
<tr><th>Algorithm</th><th>Flowchart</th></tr>
<tr><td>Step-by-step written (text) procedure</td><td>Pictorial (graphical) representation</td></tr>
<tr><td>Uses English-like statements / pseudo code</td><td>Uses standard symbols and arrows</td></tr>
<tr><td>Comparatively difficult to understand</td><td>Easy to understand</td></tr>
<tr><td>Easy to write and modify</td><td>Difficult to draw and modify</td></tr>
<tr><td>Branching and looping hard to show</td><td>Branching and looping easy to show</td></tr>
<tr><td>Suitable for large / complex problems</td><td>Becomes complex for large problems</td></tr>
<tr><td>Usually written first</td><td>Usually drawn from the algorithm</td></tr>
</table>""",
          r"""<h4>Algorithm ના ફાયદા</h4>
<ul>
<li>Step-by-step રજૂઆત – <b>સમજવામાં સરળ</b>.</li>
<li><b>Language independent</b> – કોઈપણ programming language માં ફેરવી શકાય.</li>
<li>Problem ને નાના steps માં વહેંચે; <b>program લખવાનું સરળ</b> બનાવે.</li>
<li>Coding પહેલાં logic માં <b>errors શોધવી</b> (debug) સરળ.</li>
<li>Flowchart ની સરખામણીમાં ફેરફાર સરળ; ખાસ symbols ની જરૂર નથી.</li>
</ul>
<h4>Algorithm ના ગેરફાયદા</h4>
<ul>
<li>મોટા problems માટે લખવામાં <b>સમય લાગે</b>.</li>
<li>Branching અને looping લખાણમાં સ્પષ્ટ <b>બતાવવા મુશ્કેલ</b>.</li>
<li>Flowchart જેટલું એક નજરે સમજાતું નથી (ચિત્ર નથી).</li>
<li>Pseudo code લખવાના કોઈ standard નિયમો નથી.</li>
</ul>
<h4>Algorithm અને flowchart વચ્ચેનો તફાવત</h4>
<table>
<tr><th>Algorithm</th><th>Flowchart</th></tr>
<tr><td>Step-by-step લખેલી (text) પદ્ધતિ</td><td>ચિત્રાત્મક (graphical) રજૂઆત</td></tr>
<tr><td>English જેવા statements / pseudo code વાપરે</td><td>Standard symbols અને arrows વાપરે</td></tr>
<tr><td>સમજવામાં પ્રમાણમાં અઘરું</td><td>સમજવામાં સરળ</td></tr>
<tr><td>લખવું અને બદલવું સરળ</td><td>દોરવું અને બદલવું મુશ્કેલ</td></tr>
<tr><td>Branching અને looping બતાવવા અઘરા</td><td>Branching અને looping બતાવવા સરળ</td></tr>
<tr><td>મોટા / જટિલ problems માટે યોગ્ય</td><td>મોટા problems માટે જટિલ બને</td></tr>
<tr><td>સામાન્ય રીતે પહેલાં લખાય</td><td>સામાન્ય રીતે algorithm પરથી દોરાય</td></tr>
</table>"""),

        T("Key Points – 1.2", "મુખ્ય મુદ્દા – 1.2",
          r"""<ul>
<li>Algorithm = <b>finite, step-by-step</b> procedure to solve a problem.</li>
<li>Properties: <b>input, output, definiteness, finiteness, effectiveness</b>.</li>
<li>Pseudo code = English-like algorithm using keywords READ, PRINT, IF-THEN-ELSE, WHILE, FOR.</li>
<li>Algorithm is text and easy to modify; flowchart is a picture and easy to understand.</li>
</ul>""",
          r"""<ul>
<li>Algorithm = problem ઉકેલવાની <b>મર્યાદિત, step-by-step</b> પદ્ધતિ.</li>
<li>Properties: <b>input, output, definiteness, finiteness, effectiveness</b>.</li>
<li>Pseudo code = READ, PRINT, IF-THEN-ELSE, WHILE, FOR keywords વાપરતો English જેવો algorithm.</li>
<li>Algorithm લખાણ છે અને બદલવો સરળ; flowchart ચિત્ર છે અને સમજવો સરળ.</li>
</ul>""", key=True),
    ],
}

# =====================================================================================
SEC_1_3 = {
    "title": {"en": "1.3 Overview of C", "gu": "1.3 C નો પરિચય (Overview)"},
    "items": [
        T("1.3.1 History of C", "1.3.1 C નો ઇતિહાસ",
          r"""<p><b>C</b> is a general-purpose, structured programming language developed by <b>Dennis M. Ritchie</b> at <b>AT&amp;T Bell Laboratories</b>, USA, in <b>1972</b>. It was developed to write the <b>UNIX operating system</b>.</p>
<table>
<tr><th>Year</th><th>Language</th><th>Developed by</th></tr>
<tr><td>1960</td><td>ALGOL 60</td><td>International committee</td></tr>
<tr><td>1963</td><td>CPL (Combined Programming Language)</td><td>Cambridge &amp; London University</td></tr>
<tr><td>1967</td><td>BCPL (Basic CPL)</td><td>Martin Richards</td></tr>
<tr><td>1970</td><td>B</td><td>Ken Thompson (Bell Labs)</td></tr>
<tr><td><b>1972</b></td><td><b>C</b></td><td><b>Dennis Ritchie (Bell Labs)</b></td></tr>
<tr><td>1978</td><td>K&amp;R C (book "The C Programming Language")</td><td>Kernighan &amp; Ritchie</td></tr>
<tr><td>1989 / 1990</td><td>ANSI C (C89) / ISO C (C90)</td><td>ANSI / ISO committee</td></tr>
<tr><td>1999</td><td>C99</td><td>ISO</td></tr>
<tr><td>2011, 2018, 2024</td><td>C11, C17, C23</td><td>ISO</td></tr>
</table>
<p>C took many ideas from <b>B</b> and <b>BCPL</b> and added data types. The name "C" comes from being the successor of "B".</p>""",
          r"""<p><b>C</b> એ general-purpose, structured programming language છે, જે <b>Dennis M. Ritchie</b> એ <b>AT&amp;T Bell Laboratories</b>, USA માં <b>1972</b> માં વિકસાવી. તે <b>UNIX operating system</b> લખવા માટે વિકસાવાઈ હતી.</p>
<table>
<tr><th>વર્ષ</th><th>Language</th><th>વિકસાવનાર</th></tr>
<tr><td>1960</td><td>ALGOL 60</td><td>આંતરરાષ્ટ્રીય સમિતિ</td></tr>
<tr><td>1963</td><td>CPL (Combined Programming Language)</td><td>Cambridge &amp; London University</td></tr>
<tr><td>1967</td><td>BCPL (Basic CPL)</td><td>Martin Richards</td></tr>
<tr><td>1970</td><td>B</td><td>Ken Thompson (Bell Labs)</td></tr>
<tr><td><b>1972</b></td><td><b>C</b></td><td><b>Dennis Ritchie (Bell Labs)</b></td></tr>
<tr><td>1978</td><td>K&amp;R C (પુસ્તક "The C Programming Language")</td><td>Kernighan &amp; Ritchie</td></tr>
<tr><td>1989 / 1990</td><td>ANSI C (C89) / ISO C (C90)</td><td>ANSI / ISO સમિતિ</td></tr>
<tr><td>1999</td><td>C99</td><td>ISO</td></tr>
<tr><td>2011, 2018, 2024</td><td>C11, C17, C23</td><td>ISO</td></tr>
</table>
<p>C એ <b>B</b> અને <b>BCPL</b> માંથી ઘણા વિચારો લીધા અને data types ઉમેર્યા. "B" ની અનુગામી હોવાથી નામ "C" પડ્યું.</p>"""),

        T("1.3.2 Importance and Features of C", "1.3.2 C નું મહત્વ અને વિશેષતાઓ",
          r"""<ol>
<li><b>Middle-level language:</b> combines features of high-level languages (easy to write) with low-level features (bit manipulation, direct memory access using pointers). Suitable for both system and application programs.</li>
<li><b>Structured language:</b> a program is divided into <b>functions (modules)</b>; easy to write, test, debug and maintain.</li>
<li><b>Fast and efficient:</b> programs written in C run very fast because of its rich set of data types and operators and its closeness to the hardware.</li>
<li><b>Portable:</b> a C program written on one computer can run on another with little or no modification.</li>
<li><b>Rich library:</b> many built-in (library) functions; we can also add our own functions to the library – <b>extensible</b>.</li>
<li><b>Small number of keywords:</b> only <b>32 keywords</b> (ANSI C) – easy to learn.</li>
<li><b>Powerful operators and data types</b>, including pointers, dynamic memory allocation and recursion.</li>
<li><b>Case sensitive:</b> <code>sum</code> and <code>Sum</code> are different.</li>
<li><b>Base for other languages:</b> C++, Java, C#, Python (CPython) etc. borrow its syntax.</li>
</ol>
<h4>Applications of C</h4>
<p>Operating systems (UNIX, Linux kernel, parts of Windows), compilers and interpreters, embedded systems and microcontrollers, device drivers, databases (MySQL), text editors, network software and games.</p>""",
          r"""<ol>
<li><b>Middle-level language:</b> high-level languages ની સુવિધાઓ (લખવામાં સરળ) અને low-level સુવિધાઓ (bit manipulation, pointers વડે સીધો memory access) ને જોડે છે. System અને application બંને programs માટે યોગ્ય.</li>
<li><b>Structured language:</b> program <b>functions (modules)</b> માં વહેંચાય છે; લખવું, test, debug અને maintain કરવું સરળ.</li>
<li><b>ઝડપી અને કાર્યક્ષમ:</b> સમૃદ્ધ data types, operators અને hardware ની નજીક હોવાથી C programs ખૂબ ઝડપથી ચાલે છે.</li>
<li><b>Portable:</b> એક computer પર લખેલો C program બીજા પર ઓછા કે કોઈ ફેરફાર વગર ચાલે.</li>
<li><b>સમૃદ્ધ library:</b> ઘણા built-in (library) functions; આપણા પોતાના functions પણ library માં ઉમેરી શકાય – <b>extensible</b>.</li>
<li><b>ઓછા keywords:</b> ફક્ત <b>32 keywords</b> (ANSI C) – શીખવામાં સરળ.</li>
<li><b>શક્તિશાળી operators અને data types</b>, જેમાં pointers, dynamic memory allocation અને recursion નો સમાવેશ.</li>
<li><b>Case sensitive:</b> <code>sum</code> અને <code>Sum</code> અલગ છે.</li>
<li><b>બીજી languages નો પાયો:</b> C++, Java, C#, Python (CPython) વગેરે તેની syntax અપનાવે છે.</li>
</ol>
<h4>C ના ઉપયોગો</h4>
<p>Operating systems (UNIX, Linux kernel, Windows ના ભાગો), compilers અને interpreters, embedded systems અને microcontrollers, device drivers, databases (MySQL), text editors, network software અને games.</p>"""),

        T("1.3.3 Basic Structure of a C Program", "1.3.3 C Program નું મૂળભૂત બંધારણ (Structure)",
          r"""<p>A C program is made of the following sections (see diagram). Only the <b>main()</b> section is compulsory.</p>
<ol>
<li><b>Documentation section:</b> comments giving the program name, author, date and purpose. Comments are written between <code>/* … */</code> or after <code>//</code> and are ignored by the compiler.</li>
<li><b>Link section:</b> tells the compiler to link functions from the system library using <code>#include</code>, e.g. <code>#include &lt;stdio.h&gt;</code>, <code>#include &lt;math.h&gt;</code>.</li>
<li><b>Definition section:</b> defines symbolic constants using <code>#define</code>, e.g. <code>#define PI 3.14</code>.</li>
<li><b>Global declaration section:</b> declares global variables (usable in all functions) and user-defined function prototypes. It is outside all functions.</li>
<li><b>main() function section:</b> every program must have one <code>main()</code>; execution starts here. It has two parts inside braces <code>{ }</code>:
<ul><li><b>Declaration part</b> – declares all variables used in the executable part.</li>
<li><b>Executable part</b> – at least one statement. Every statement ends with a semicolon <code>;</code>.</li></ul></li>
<li><b>Subprogram section:</b> contains user-defined functions called from <code>main()</code>. Usually placed after main().</li>
</ol>
<h4>Example showing all sections</h4>
@@structure_ex@@""",
          r"""<p>C program નીચેના sections નો બનેલો છે (આકૃતિ જુઓ). ફક્ત <b>main()</b> section ફરજિયાત છે.</p>
<ol>
<li><b>Documentation section:</b> program નું નામ, લેખક, તારીખ અને હેતુ દર્શાવતી comments. Comments <code>/* … */</code> વચ્ચે અથવા <code>//</code> પછી લખાય છે અને compiler તેમને અવગણે છે.</li>
<li><b>Link section:</b> <code>#include</code> વડે system library ના functions link કરવા compiler ને જણાવે, દા.ત. <code>#include &lt;stdio.h&gt;</code>, <code>#include &lt;math.h&gt;</code>.</li>
<li><b>Definition section:</b> <code>#define</code> વડે symbolic constants વ્યાખ્યાયિત કરે, દા.ત. <code>#define PI 3.14</code>.</li>
<li><b>Global declaration section:</b> global variables (બધા functions માં વાપરી શકાય) અને user-defined function prototypes declare કરે. તે બધા functions ની બહાર હોય છે.</li>
<li><b>main() function section:</b> દરેક program માં એક <code>main()</code> હોવું જ જોઈએ; execution અહીંથી શરૂ થાય. તેમાં braces <code>{ }</code> ની અંદર બે ભાગ છે:
<ul><li><b>Declaration part</b> – executable part માં વપરાતા બધા variables declare કરે.</li>
<li><b>Executable part</b> – ઓછામાં ઓછું એક statement. દરેક statement semicolon <code>;</code> થી પૂરું થાય.</li></ul></li>
<li><b>Subprogram section:</b> <code>main()</code> માંથી બોલાવાતા user-defined functions. સામાન્ય રીતે main() પછી મૂકાય.</li>
</ol>
<h4>બધા sections દર્શાવતું ઉદાહરણ</h4>
@@structure_ex@@""",
          diagram="c1_structure", programs=["c1p1"]),

        T("1.3.4 Executing a C Program", "1.3.4 C Program નું Execution (ચલાવવું)",
          r"""<p>Executing a C program involves the following steps (see diagram):</p>
<ol>
<li><b>Creating (editing) the program:</b> type the program in an editor and save it with extension <b>.c</b> (e.g. <code>prog.c</code>). This is the <b>source code</b>.</li>
<li><b>Preprocessing:</b> the preprocessor handles lines beginning with <code>#</code> – it inserts header files (<code>#include</code>) and replaces symbolic constants (<code>#define</code>).</li>
<li><b>Compiling:</b> the <b>compiler</b> checks the program for <b>syntax errors</b> and translates it into machine language – <b>object code</b> (<code>prog.obj</code> in Windows / <code>prog.o</code> in Linux). If there are errors, the program is corrected and compiled again.</li>
<li><b>Linking:</b> the <b>linker</b> joins the object code with the code of the <b>library functions</b> used (such as <code>printf()</code>) and creates an <b>executable file</b> (<code>prog.exe</code> / <code>a.out</code>).</li>
<li><b>Loading and executing:</b> the <b>loader</b> loads the executable into memory and it runs. Input data is given and output is obtained.</li>
<li><b>Testing:</b> if the output is wrong (<b>logic error</b>), the program is corrected and the steps are repeated.</li>
</ol>
<h4>Commands</h4>
<table>
<tr><th>Environment</th><th>Compile</th><th>Run</th><th>See output</th></tr>
<tr><td>Turbo C / Borland (Windows)</td><td>Alt + F9</td><td>Ctrl + F9</td><td>Alt + F5</td></tr>
<tr><td>GCC (Linux / Windows MinGW)</td><td colspan="2"><code>gcc prog.c -o prog</code> then <code>./prog</code></td><td>Terminal</td></tr>
<tr><td>Code::Blocks / Dev-C++ / VS Code</td><td colspan="2">Build and Run (F9 / F11 / Ctrl+F5)</td><td>Console window</td></tr>
</table>
@@gcc_cmd@@
<h4>Types of errors</h4>
<ul>
<li><b>Syntax (compile-time) errors:</b> violation of grammar rules, e.g. missing semicolon, undeclared variable – detected by the compiler.</li>
<li><b>Linker errors:</b> e.g. misspelled <code>main</code> or library function not found.</li>
<li><b>Run-time errors:</b> occur while running, e.g. division by zero.</li>
<li><b>Logical errors:</b> program runs but gives wrong output, e.g. using <code>+</code> instead of <code>*</code> – found by testing.</li>
</ul>""",
          r"""<p>C program ચલાવવામાં નીચેના steps છે (આકૃતિ જુઓ):</p>
<ol>
<li><b>Program બનાવવો (editing):</b> editor માં program type કરી <b>.c</b> extension સાથે save કરો (દા.ત. <code>prog.c</code>). આ <b>source code</b> છે.</li>
<li><b>Preprocessing:</b> preprocessor <code>#</code> થી શરૂ થતી lines સંભાળે છે – header files (<code>#include</code>) ઉમેરે અને symbolic constants (<code>#define</code>) બદલે.</li>
<li><b>Compiling:</b> <b>compiler</b> program માં <b>syntax errors</b> તપાસે અને તેને machine language – <b>object code</b> (Windows માં <code>prog.obj</code> / Linux માં <code>prog.o</code>) માં ફેરવે. Errors હોય તો program સુધારી ફરી compile કરાય.</li>
<li><b>Linking:</b> <b>linker</b> object code ને વપરાયેલા <b>library functions</b> (જેમ કે <code>printf()</code>) ના code સાથે જોડી <b>executable file</b> (<code>prog.exe</code> / <code>a.out</code>) બનાવે.</li>
<li><b>Loading અને executing:</b> <b>loader</b> executable ને memory માં load કરે અને તે ચાલે. Input data અપાય અને output મળે.</li>
<li><b>Testing:</b> output ખોટું હોય (<b>logic error</b>) તો program સુધારી steps ફરી કરાય.</li>
</ol>
<h4>Commands</h4>
<table>
<tr><th>Environment</th><th>Compile</th><th>Run</th><th>Output જોવા</th></tr>
<tr><td>Turbo C / Borland (Windows)</td><td>Alt + F9</td><td>Ctrl + F9</td><td>Alt + F5</td></tr>
<tr><td>GCC (Linux / Windows MinGW)</td><td colspan="2"><code>gcc prog.c -o prog</code> પછી <code>./prog</code></td><td>Terminal</td></tr>
<tr><td>Code::Blocks / Dev-C++ / VS Code</td><td colspan="2">Build and Run (F9 / F11 / Ctrl+F5)</td><td>Console window</td></tr>
</table>
@@gcc_cmd@@
<h4>Errors ના પ્રકાર</h4>
<ul>
<li><b>Syntax (compile-time) errors:</b> વ્યાકરણના નિયમોનો ભંગ, દા.ત. semicolon ખૂટે, undeclared variable – compiler શોધે.</li>
<li><b>Linker errors:</b> દા.ત. <code>main</code> ની ખોટી જોડણી અથવા library function ન મળે.</li>
<li><b>Run-time errors:</b> ચલાવતી વખતે થાય, દા.ત. શૂન્ય વડે ભાગાકાર.</li>
<li><b>Logical errors:</b> program ચાલે પણ ખોટો output આપે, દા.ત. <code>*</code> ની જગ્યાએ <code>+</code> – testing થી મળે.</li>
</ul>""",
          diagram="c1_execute"),

        T("Key Points – 1.3", "મુખ્ય મુદ્દા – 1.3",
          r"""<ul>
<li>C developed by <b>Dennis Ritchie</b>, <b>Bell Labs, 1972</b>, for UNIX; derived from BCPL and B.</li>
<li>Features: middle-level, structured, fast, portable, rich library, 32 keywords, case sensitive.</li>
<li>Structure: Documentation → Link → Definition → Global declaration → <b>main()</b> → Subprograms.</li>
<li>Steps: Edit (.c) → Preprocess → Compile (.obj/.o) → Link (.exe) → Load &amp; Run.</li>
<li>Errors: syntax, linker, run-time, logical.</li>
</ul>""",
          r"""<ul>
<li>C ને <b>Dennis Ritchie</b> એ <b>Bell Labs, 1972</b> માં UNIX માટે વિકસાવી; BCPL અને B પરથી.</li>
<li>વિશેષતાઓ: middle-level, structured, ઝડપી, portable, સમૃદ્ધ library, 32 keywords, case sensitive.</li>
<li>Structure: Documentation → Link → Definition → Global declaration → <b>main()</b> → Subprograms.</li>
<li>Steps: Edit (.c) → Preprocess → Compile (.obj/.o) → Link (.exe) → Load &amp; Run.</li>
<li>Errors: syntax, linker, run-time, logical.</li>
</ul>""", key=True),
    ],
}

NOTES_A = [SEC_1_1, SEC_1_2, SEC_1_3]
