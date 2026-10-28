"""DI04000021 Unit 5 notes: Modern Java Features."""
from java_content import make_TJ

SN = {}

T = make_TJ(SN)

SEC_5_1 = {
    "title": {"en": "5.1 Java Language Version Updates"},
    "items": [
        T("The Evolution of Java: 7 to 21", """
<ul><li>Java releases roughly every 6 months now; <b>LTS</b> versions (8, 11, 17, 21) are what industry standardises on.</li>
<li><b>Java 7</b>: try-with-resources, strings in switch, diamond operator, multi-catch.</li>
<li><b>Java 8</b> (the revolution): lambda expressions, Stream API, java.time, default methods in interfaces.</li>
<li><b>Java 9-11</b>: modules (JPMS), jshell, var for locals, HttpClient.</li>
<li><b>Java 14-17</b>: switch expressions, text blocks, records, pattern-matching instanceof, sealed classes.</li>
<li>The diploma lab JDK is 11, so lambda/streams/var <b>run</b> here; the 14+ syntax appears as study-exhibits (jv5_12) and in exam theory.</li></ul>
""", diagram="jv5_timeline"),
        T("Java 7 Features: try-with-resources and Friends", """
<ul><li><b>try-with-resources</b>: declare an AutoCloseable object in the try header and the JVM closes it on EVERY exit path - the finally block of Unit 4 becomes unnecessary for pure cleanup.</li>
<li><b>Strings in switch</b>: direct case labels like "Friday" - far clearer than an if-else ladder over equals().</li>
<li><b>Diamond operator</b>: <code>new ArrayList&lt;&gt;()</code> reads the element type from the declaration on the left.</li>
<li><b>Multi-catch</b>: <code>catch (A | B e)</code> - one recovery block for unrelated exception types.</li></ul>
<p>jv5_1 closes a Scanner without finally; jv5_2 packs switch-on-String, diamond and multi-catch into one genuine run.</p>
""", diagram="jv5_twr", programs=["jv5_1", "jv5_2"]),
        T("var, java.time and the Post-8 Wave", """
<ul><li><code>var</code> (Java 10): local-variable <b>type inference</b> - javac copies the type from the right side; still fully static, not JavaScript-style dynamic typing.</li>
<li>Rules of var: locals and loops only; must be initialised where declared; not for fields, parameters or return types.</li>
<li><b>record</b> (16+): one line declares an immutable data carrier with constructor, accessors, equals, hashCode and toString.</li>
<li><b>Pattern-matching instanceof</b> (16+): <code>if (o instanceof String t)</code> tests and binds in one step - no manual cast.</li>
<li>Also in the wave: text blocks (15+), sealed classes (17+), switch expressions (14+).</li>
<li><b>java.time</b> (Java 8): LocalDate/LocalTime/Period - immutable, thread-safe, with clean formatting; it retired Date/Calendar for everyday work.</li></ul>
<p>jv5_3 runs var on JDK 11; jv5_11 counts down to an exam date with java.time; jv5_12 shows records/patterns as commented exhibits beside their classic equivalents.</p>
""", programs=["jv5_3", "jv5_11", "jv5_12"]),
    ],
}

SEC_5_2 = {
    "title": {"en": "5.2 Functional Features (Java 8)"},
    "items": [
        T("Functional Interfaces and Lambda Basics", """
<ul><li>A <b>functional interface</b> has EXACTLY ONE abstract method (any number of default/static ones) - that single method is what the lambda implements.</li>
<li><b>Lambda syntax</b>: <code>(parameters) -&gt; body</code>; empty parentheses when no parameters; a single expression needs no braces and no return keyword; braces for multi-statement bodies.</li>
<li>javac matches parameter types from the interface's method signature, so lambda parameter types are usually omitted.</li>
<li><code>@FunctionalInterface</code> asks the compiler to police the one-method rule.</li></ul>
<p>jv5_4 contrasts a 5-line anonymous class with its one-line lambda twin - both print, both are Speaker objects.</p>
""", diagram="jv5_lambda", programs=["jv5_4"]),
        T("Lambdas with Parameters: Passing Behaviour Around", """
<ul><li><code>Calc add = (x, y) -&gt; x + y;</code> - one contract, many behaviours, each a two-word class.</li>
<li>Lambdas are <b>values</b>: store them in variables, pass them to methods, call them later - code becomes data.</li>
<li>This is run-time flexibility without inheritance: the strategy is chosen by which lambda you pass, not by which subclass you wrote.</li></ul>
<p>jv5_5 passes add/sub/mul/div lambdas of the same Calc type into a shared show() method.</p>
""", programs=["jv5_5"]),
        T("forEach and the Ready-made Functional Interfaces", """
<ul><li>Every collection owns <code>forEach(Consumer)</code>: <code>team.forEach(t -&gt; println(...))</code> visits each element - the syllabus' "print list elements" task.</li>
<li>Meet the built-ins of <code>java.util.function</code>: <b>Supplier&lt;T&gt;</b> (get), <b>Consumer&lt;T&gt;</b> (accept), <b>Predicate&lt;T&gt;</b> (test), <b>Function&lt;T,R&gt;</b> (apply); plus old friend <b>Runnable</b> (run).</li>
<li>These five cover filter/map/forEach/factory tasks without writing your own interfaces.</li></ul>
<p>jv5_6 prints a list three ways; jv5_10 runs Runnable and Supplier lambdas directly.</p>
""", diagram="jv5_func_iface", programs=["jv5_6", "jv5_10"]),
        T("Stream API: filter, map, forEach", """
<ul><li>A <b>stream</b> is a conveyor-belt view over a collection - not a container, not a loop.</li>
<li><code>filter(Predicate)</code> keeps elements whose test is true; <code>map(Function)</code> transforms each element; <code>forEach(Consumer)</code> consumes them.</li>
<li>The source collection is <b>never mutated</b> - streams compute views; a spent stream cannot be reused.</li>
<li><b>Practical 15</b>: filter even numbers (jv5_7) and map strings to uppercase (jv5_8) - exactly the two required tasks.</li></ul>
""", diagram="jv5_stream", programs=["jv5_7", "jv5_8"]),
        T("Full Pipelines: sorted, collect, and Laziness", """
<ul><li>Pipelines chain <b>intermediate</b> steps (filter, map, sorted - each returns a new stream) and end with ONE <b>terminal</b> step (forEach, count, collect).</li>
<li>Intermediate steps are <b>lazy</b>: nothing flows until the terminal step starts the belt - this enables wholesale optimisation.</li>
<li><code>collect(Collectors.toList())</code> pours the survivors back into a real modifiable List.</li>
<li>Style gain: whole "data questions" read as one readable sentence instead of nested loops with temp lists.</li></ul>
<p>jv5_9 filters passes, sorts them, maps to grade strings and collects - one pipeline, new list, originals intact.</p>
""", programs=["jv5_9"]),
    ],
}

SEC_5_3 = {
    "title": {"en": "5.3 Introduction to AI with Java"},
    "items": [
        T("Meaning of AI and Machine Learning", """
<ul><li><b>Artificial Intelligence</b>: the goal - getting machines to perform tasks that would need human intelligence (recognise, decide, predict, translate).</li>
<li><b>Machine Learning</b>: the dominant approach inside AI - instead of hand-writing every rule, the program <b>learns behaviour from data/examples</b>. Change the data, and behaviour changes without rewriting code.</li>
<li><b>Deep Learning</b>: ML using layered neural networks - today's image/speech/language breakthroughs.</li>
<li>Exam line: AI is the destination; ML is the road paved with examples; DL is the newest, fastest vehicle on that road.</li></ul>
""", diagram="jv5_aiml"),
        T("Role of Java in AI and Its Libraries", """
<ul><li>Java dominates enterprise backends; AI columns inside such systems (fraud scores, recommendations, routing) are deployed <b>in Java</b> - data handling via collections/streams/JDBC, integration via APIs.</li>
<li><b>Deeplearning4j (DL4J)</b>: build and train neural networks natively on the JVM, with GPU acceleration.</li>
<li><b>TensorFlow Java API</b>: load and run <b>pre-trained</b> TensorFlow models from Java code - train in Python, deploy in Java is a common industry split.</li>
<li>Also worth meeting: Weka (classic ML library) and the shape of an AI service call from a Java app.</li></ul>
<p>jv5_13 demonstrates the ML idea in 30 honest lines: a nearest-neighbour predictor that classifies new students from examples alone - no hand-written pass/fail rule anywhere.</p>
""", diagram="jv5_ailibs", programs=["jv5_13"]),
    ],
}

NOTES = [SEC_5_1, SEC_5_2, SEC_5_3]
