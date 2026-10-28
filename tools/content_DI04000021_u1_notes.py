"""DI04000021 Unit 1 notes: Introduction to Java Programming."""
from java_content import make_TJ

SN = {}

T = make_TJ(SN)

SEC_1_1 = {
    "title": {"en": "1.1 Introduction to Java"},
    "items": [
        T("Introduction, Features and Applications of Java", """
<p><b>Java</b> is an object-oriented, platform-independent programming language. It was created by <b>James Gosling</b> and his team (called the "Green Team") at <b>Sun Microsystems in 1995</b>; the language was first named <b>Oak</b> and later renamed Java. Oracle Corporation now owns it.</p>
<h4>Features of Java (bases of the language)</h4>
<ul><li><b>Simple</b> - syntax is like C/C++, so it is easy to learn; there are no pointers, goto or operator overloading.</li>
<li><b>Object oriented</b> - everything is organised inside classes and objects.</li>
<li><b>Platform independent</b> - <i>Write Once, Run Anywhere</i>: compile once into byte code and run the same <code>.class</code> file on Windows, Linux or Mac.</li>
<li><b>Compiled and interpreted</b> - javac compiles to byte code, the JVM interprets it line by line.</li>
<li><b>Robust</b> - strong type checking, exception handling and automatic garbage collection catch errors early.</li>
<li><b>Secure</b> - programs run inside the JVM sandbox; byte code is verified before execution.</li>
<li><b>Multithreaded</b> - several parts of a program can run at the same time.</li>
<li><b>Portable and high performance</b> - the same primitive sizes on every machine; the JIT compiler speeds up hot code.</li></ul>
<h4>Applications of Java</h4>
<ul><li><b>Android apps</b> - Java was the original language of Android development.</li>
<li><b>Web and enterprise applications</b> - banking systems, e-commerce servers (Spring, JSP).</li>
<li><b>Desktop applications</b> - IDEs like Eclipse and NetBeans are themselves written in Java.</li>
<li><b>Big data and AI</b> - Hadoop, Elasticsearch and libraries like Deeplearning4j run on the JVM.</li></ul>
"""),
    ],
}

SEC_1_2 = {
    "title": {"en": "1.2 Writing and Running the First Program"},
    "items": [
        T("JDK, JRE, JVM and Byte Code", """
<p>Three names you must distinguish for every exam:</p>
<ul><li><b>JDK (Java Development Kit)</b> - the complete kit for <b>writing</b> programs: the compiler <code>javac</code>, the launcher <code>java</code>, a debugger and other tools. It contains the JRE.</li>
<li><b>JRE (Java Runtime Environment)</b> - everything needed to <b>run</b> a program: class libraries (String, Scanner...) plus the JVM. Ordinary users install only the JRE.</li>
<li><b>JVM (Java Virtual Machine)</b> - the "virtual computer" that executes byte code instruction by instruction (interpreter), with a JIT compiler for speed. It is different for every operating system.</li></ul>
<p><b>Byte code</b> is the intermediate code stored in <code>.class</code> files after compilation. It is not machine code of any real processor - that is exactly why it is <b>portable</b>.</p>
""", diagram="jv1_jdk_jre_jvm"),
        T("Compile Once, Run Anywhere", """
<p>The life of a Java program has two steps:</p>
<ol><li><b>Compile:</b> <code>javac Main.java</code> reads the source code and writes <code>Main.class</code>, which contains <b>byte code</b>.</li>
<li><b>Run:</b> <code>java Main</code> starts the JVM, which loads and verifies the byte code and executes it.</li></ol>
<ul><li>C/C++ compile straight to the machine code of one OS, so the result works only on that OS.</li>
<li>Java compiles to byte code instead; each OS has its own JVM to execute the same <code>.class</code> file. This is the meaning of <i>Write Once, Run Anywhere</i>.</li>
<li>Debug and execute steps are identical on any machine once the JDK is installed.</li></ul>
""", diagram="jv1_wora"),
        T("Structure of a Java Program and Hello World", """
<p>Every Java program lives inside a <b>class</b>:</p>
<ul><li>The file name must match the class name (<code>Main.java</code> for <code>class Main</code>).</li>
<li>Execution starts at <code>public static void main(String[] args)</code> - <b>public</b> so that the JVM can call it, <b>static</b> so no object is needed first, <b>void</b> because it returns nothing.</li>
<li>Statements end with <code>;</code>, blocks are wrapped in <code>{ }</code>.</li>
<li><code>System.out.println(...)</code> prints a line; <code>System.out</code> is the console, <code>println</code> the method.</li>
<li>Java is <b>case sensitive</b>: <code>Main</code>, <code>main</code> and <code>MAIN</code> are three different names.</li></ul>
<p>Run the Hello World program below and study how the output matches each println/print statement.</p>
""", diagram="jv1_structure", programs=["jv1_1"]),
    ],
}

SEC_1_3 = {
    "title": {"en": "1.3 Data Types, Variables and Operators"},
    "items": [
        T("Data Types and Variables", """
<ul><li>A <b>variable</b> is a named memory location that stores a changeable value; a <b>data type</b> fixes what kind of value it can hold and how much memory it uses.</li>
<li>Java's 8 <b>primitive types</b>: whole numbers - <code>byte</code>, <code>short</code>, <code>int</code>, <code>long</code>; decimals - <code>float</code>, <code>double</code>; character - <code>char</code>; truth - <code>boolean</code>.</li>
<li><b>Declaring and initializing</b>: <code>int marks = 452;</code> - type, name, initial value, all in one statement. A variable must be initialized (or assigned) before use; Java refuses to read uninitialized local variables.</li>
<li>Note the suffixes: <code>L</code> for long values, <code>f</code> for float values.</li>
<li><code>String</code> is a <b>class</b>, not a primitive type - but it is so common that it is written without <code>new</code>: <code>String city = "Surat";</code>.</li></ul>
""", diagram="jv1_datatypes", programs=["jv1_2"]),
        T("Scope and Lifetime of Variables", """
<ul><li><b>Scope</b> tells in which region of code a variable may be used; <b>lifetime</b> tells how long it keeps its memory.</li>
<li>A variable declared inside a block <code>{ }</code> is a <b>local variable</b>: it is born when the block is entered and dies when the block ends.</li>
<li>Inner blocks may use outer variables; outer code may never use a variable declared inside a block.</li>
<li>Fields (member variables) of a class live as long as the object lives - scope and lifetime become important again in Unit 2.</li></ul>
""", programs=["jv1_4"]),
        T("Type Conversion and Type Casting", """
<ul><li><b>Automatic (widening) conversion</b>: Java itself converts a smaller type into a larger one when no data can be lost: byte -&gt; short -&gt; int -&gt; long -&gt; float -&gt; double. Example: <code>long l = 452;</code>.</li>
<li><b>Manual (narrowing) casting</b>: converting a larger type into a smaller one needs an explicit cast and may lose data: <code>int r = (int) 9.7;</code> gives 9.</li>
<li><code>char</code> and <code>int</code> convert freely using the character's code value ('A' is 65): <code>int code = 'A';</code> and <code>char nx = (char)('A' + 1);</code> gives 'B'.</li>
<li>In mixed expressions Java widens the smaller operand first, so <code>(double) a / b</code> divides exactly while <code>a / b</code> (two ints) drops the fraction.</li></ul>
""", diagram="jv1_casting", programs=["jv1_3"]),
        T("Operators in Java", """
<ul><li><b>Arithmetic:</b> <code>+ - * / %</code>; <code>%</code> gives the remainder, integer division discards the fraction.</li>
<li><b>Relational:</b> <code>&lt; &gt; &lt;= &gt;= == !=</code> - answers are boolean.</li>
<li><b>Logical:</b> <code>&amp;&amp; || !</code> combine conditions.</li>
<li><b>Assignment:</b> <code>=</code> and shortcuts <code>+= -= *= /= %=</code>.</li>
<li><b>Conditional (ternary):</b> <code>condition ? a : b</code> - a one-line if-else that returns a value.</li>
<li><b>Increment/decrement:</b> <code>++</code> and <code>--</code>; prefix (<code>++i</code>) changes first, postfix (<code>i++</code>) uses the old value first.</li>
<li><b>Bitwise:</b> <code>&amp; | ^ &lt;&lt; &gt;&gt;</code> operate on bits; shifts multiply/divide by powers of 2.</li></ul>
<p>Careful with <code>==</code>: it compares values for primitives, but objects (like String) are compared with <code>equals()</code>.</p>
""", diagram="jv1_operators", programs=["jv1_5"]),
    ],
}

SEC_1_4 = {
    "title": {"en": "1.4 Control Flow"},
    "items": [
        T("Selection: if, if-else, Ladder and Nested if", """
<ul><li><b>if</b> runs a block only when its condition is true; <b>if-else</b> gives a second path for false.</li>
<li>The <b>if-else-if ladder</b> checks a list of conditions top-down and executes the first true one, then skips the rest - used for ranges like grades.</li>
<li>A <b>nested if</b> (an if inside another if) is used when the second question matters only after the first answer, e.g. the maximum-of-three program.</li></ul>
""", programs=["jv1_6", "jv1_7"]),
        T("switch-case", """
<ul><li><code>switch</code> chooses one of many <code>case</code> blocks by matching a single value - cleaner than a long ladder when testing equality.</li>
<li>Each case must end with <code>break</code>; otherwise execution falls through into the next case.</li>
<li><code>default</code> catches all unmatched values.</li>
<li>Allowed values: char, byte, short, int, and since Java 7 also <b>String</b>.</li></ul>
""", programs=["jv1_8"]),
        T("Loops: for, while, do-while", """
<ul><li><b>for(initialisation; condition; update)</b> - all loop control on one line; the right choice when the count is known (tables, array indexes).</li>
<li><b>while</b> - condition checked before every round; the body may never run. Perfect for "until it becomes zero" algorithms like digit counting.</li>
<li><b>do-while</b> - condition checked after the body, so the body always runs at least once; used for menu-driven programs.</li>
<li>The <b>for-each</b> form <code>for (int m : marks)</code> visits every element of an array without an index.</li></ul>
""", programs=["jv1_9", "jv1_10", "jv1_15"]),
        T("Jump Statements: break and continue", """
<ul><li><code>break</code> leaves the innermost loop or switch immediately - used when the answer is already found and more rounds would be wasted.</li>
<li><code>continue</code> skips only the rest of the current round and starts the next one - used to filter (e.g. skip even numbers).</li>
<li>Both are called <b>jump statements</b>; overusing them makes code harder to follow, so use them for clear cases only.</li></ul>
""", diagram="jv1_loops", programs=["jv1_11"]),
    ],
}

SEC_1_5 = {
    "title": {"en": "1.5 Arrays"},
    "items": [
        T("1D Arrays: Declaration, Initialization and Traversal", """
<ul><li>An <b>array</b> is a single name for a numbered group of same-type values, stored one after another in memory.</li>
<li>Declaration: <code>int[] marks;</code>; create: <code>marks = new int[5];</code>; or both with values: <code>int[] marks = {78, 85, 66, 90, 71};</code>.</li>
<li>Indexes are <b>0-based</b>: the first element is <code>marks[0]</code>, the last <code>marks[marks.length - 1]</code>.</li>
<li><code>marks.length</code> (a field, no brackets) keeps the size - loops that use it survive array resizing automatically.</li>
<li>Traverse with an indexed <code>for</code> loop or with <code>for-each</code>; classic tasks are sum/average and min/max in one pass.</li></ul>
""", programs=["jv1_12", "jv1_14"]),
        T("2D Arrays", """
<ul><li>A <b>2D array</b> is an array of arrays - picture it as a table with rows and columns (a matrix).</li>
<li>Declaration with values: <code>int[][] a = {{1,2,3},{4,5,6}};</code> (2 rows, 3 columns).</li>
<li><code>a.length</code> = number of rows; <code>a[i].length</code> = number of columns in row i.</li>
<li>Two nested loops visit every cell; <code>a[i][j]</code> is the element at row i, column j.</li>
<li>Matrix addition: add elements at matching positions and store the result in a third matrix of the same shape.</li></ul>
""", programs=["jv1_13"]),
    ],
}

NOTES = [SEC_1_1, SEC_1_2, SEC_1_3, SEC_1_4, SEC_1_5]
