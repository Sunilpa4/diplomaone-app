"""DI04000021 Unit 4 notes: Exception Handling and Collections Framework."""
from java_content import make_TJ

SN = {}

T = make_TJ(SN)

SEC_4_1 = {
    "title": {"en": "4.1 Errors and Exceptions"},
    "items": [
        T("Types of Errors", """
<ul><li><b>Compile-time errors</b>: caught by <code>javac</code> - syntax slips, type mismatches, missing semicolons. No .class file is produced until they are fixed.</li>
<li><b>Runtime errors (exceptions)</b>: the program compiles cleanly but blows up while running - divide by zero, null reference, array index out of range. The JVM throws an <b>exception object</b> describing what went wrong and where.</li>
<li><b>Logical errors</b>: the program compiles and runs, yet the answer is wrong - a formula slip, an inverted condition. No compiler or JVM ever warns you; only testing does.</li></ul>
<p>Run jv4_1 to see all three side by side, then jv4_2 to watch an unhandled runtime error kill a program mid-way.</p>
""", diagram="jv4_error_types", programs=["jv4_1", "jv4_2"]),
        T("Exception Hierarchy and Built-in Exceptions", """
<ul><li>Every throwable object descends from <b>Throwable</b>, which splits into <b>Error</b> (serious JVM problems - not meant to be caught) and <b>Exception</b> (application problems - designed to be caught).</li>
<li>Under Exception sits <b>RuntimeException</b> - the <b>unchecked</b> family. javac never forces you to handle these: ArithmeticException, NullPointerException, ArrayIndexOutOfBoundsException, NumberFormatException, IllegalArgumentException, IllegalStateException.</li>
<li>Other Exception children are <b>checked</b>: javac requires either try-catch or a <code>throws</code> clause - e.g. InterruptedException, IOException.</li>
<li>Why it matters: knowing an exception's family tells you whether the compiler will help you remember to handle it.</li></ul>
""", diagram="jv4_hierarchy", programs=["jv4_5"]),
    ],
}

SEC_4_2 = {
    "title": {"en": "4.2 Exception Handling"},
    "items": [
        T("try and catch", """
<ul><li><code>try { ... }</code> wraps the risky statements; <code>catch (SomeException e) { ... }</code> holds the recovery plan.</li>
<li>The moment a statement inside try throws, control jumps to the matching catch - the rest of the try block is skipped for that run.</li>
<li><code>e</code> is the exception object: <code>e.getMessage()</code> gives the detail string, <code>e.getClass().getSimpleName()</code> gives the exact type.</li>
<li>After the catch completes, execution resumes AFTER the whole try-catch - the program survives.</li></ul>
<p><b>Practical 13 walkthrough:</b> jv4_3 and jv4_4 catch the two required built-ins - divide by zero and null pointer.</p>
""", programs=["jv4_3", "jv4_4"]),
        T("finally: Guaranteed Cleanup", """
<ul><li><code>finally { ... }</code> attaches to a try (with or without catch) and runs on <b>every</b> path: normal completion, caught exception, even uncaught exception (right before the crash).</li>
<li>That one guarantee makes finally the home of cleanup: closing files and connections, releasing locks, printing audit logs.</li>
<li>Order of blocks is fixed: try, then catch(es), then finally. Only one catch ever runs, but finally ALWAYS runs.</li></ul>
<p>jv4_7 calls bank() twice - success and failure - and "close vault" prints both times. That is finally keeping its promise.</p>
""", diagram="jv4_try_flow", programs=["jv4_7"]),
        T("Multiple catch Blocks", """
<ul><li>One try may own several catch clauses; the JVM tests them <b>top to bottom</b> and runs the first whose type matches the thrown object (matching is by IS-A - a parent type matches child objects).</li>
<li>Because of IS-A matching, order must run <b>specific first, general last</b>. A parent catch placed higher swallows everything below.</li>
<li>javac enforces this: a catch unreachable because of an earlier parent catch is a compile error.</li></ul>
<p>jv4_6 parses a too-big number and the NumberFormatException catch wins; jv4_11 shows the NPE catch beating its RuntimeException parent written below it.</p>
""", diagram="jv4_catch_order", programs=["jv4_6", "jv4_11"]),
        T("throw: Raising Exceptions Yourself", """
<ul><li><code>throw new ExceptionType("message")</code> creates and raises an exception object on the spot - a single object, so the word is singular.</li>
<li>The remainder of the method is skipped; the JVM hunts for a matching catch up the call chain.</li>
<li>Main use: <b>validation</b> - reject impossible data (negative age, overdrawn balance) the moment it appears, with a message the catch can show to a human.</li>
<li>Any class from the hierarchy may be thrown; RuntimeException children keep it unchecked.</li></ul>
<p>jv4_8 refuses under-18 voters with IllegalArgumentException - a built-in type used by our own logic.</p>
""", programs=["jv4_8"]),
        T("throws: Declaring Risk in the Header", """
<ul><li>A method that might raise a <b>checked</b> exception must say so: <code>void f() throws InterruptedException { ... }</code>.</li>
<li>This is a <b>warning, not an action</b> - it pushes the duty onto the caller, who must catch the exception or declare throws again.</li>
<li>Several types can be listed with commas: <code>throws IOException, InterruptedException</code>.</li>
<li><b>throw vs throws:</b> throw is a statement that raises one object inside the body; throws is a clause in the signature that advertises what may come out. jv4_9 and jv4_10 contrast the two.</li></ul>
""", diagram="jv4_throw_throws", programs=["jv4_9", "jv4_10"]),
    ],
}

SEC_4_3 = {
    "title": {"en": "4.3 Collections Framework"},
    "items": [
        T("Need of Collections and the Hierarchy", """
<ul><li>Arrays are fixed-size and type-naked; real programs need containers that <b>grow</b>, <b>search</b>, and <b>remove</b> - that is the Collections framework (package <code>java.util</code>).</li>
<li>Top of the family: interface <b>Collection</b>; below it interfaces <b>List</b> and <b>Set</b>; concrete classes such as <b>ArrayList</b> and <b>HashSet</b> implement them.</li>
<li>Collections store <b>objects</b>, not primitives - autoboxing (Unit 2) wraps <code>int</code> into <code>Integer</code> automatically when you add.</li>
<li>Design habit: declare with the interface type (<code>List&lt;String&gt; l = new ArrayList&lt;&gt;();</code>) and construct with the class - swapping implementations later costs one word.</li></ul>
""", diagram="jv4_collections"),
        T("List: ArrayList Essentials", """
<ul><li><code>ArrayList&lt;E&gt;</code> - the growable array: <code>add(e)</code> appends, <code>add(i, e)</code> inserts, <code>get(i)</code>/<code>set(i, e)</code> access by index, <code>size()</code> replaces array <code>length</code>.</li>
<li><b>Remove</b> by value <code>remove("Farhan")</code> or by index <code>remove(0)</code>; the list shrinks and re-indexes itself.</li>
<li><b>Search</b>: <code>contains(e)</code> answers yes/no, <code>indexOf(e)</code> answers where (-1 when absent).</li>
<li>Printing the list object itself shows <code>[a, b, c]</code> - friendly toString included.</li></ul>
<p><b>Practical 14 walkthrough:</b> jv4_12 performs add, remove and search exactly as the practical demands.</p>
""", programs=["jv4_12"]),
        T("Iterating Collections: the for-each Loop", """
<ul><li>The enhanced for loop - <code>for (String t : team) { ... }</code> - visits every element left to right with no index bookkeeping.</li>
<li>Works on any List or Set (any Collection), so one syntax covers the whole framework.</li>
<li>Limits: no index inside the body, and you cannot add/remove elements of the collection while iterating (that throws ConcurrentModificationException in real programs).</li>
<li>Keep the classic counting loop for tasks that genuinely need positions.</li></ul>
<p>jv4_13 runs both loops on the same ArrayList of marks and totals them with for-each.</p>
""", programs=["jv4_13"]),
        T("Set: HashSet and Uniqueness", """
<ul><li><code>HashSet&lt;E&gt;</code> stores each element <b>once</b>: re-adding an equal value is silently ignored - perfect for unique tags, roll numbers, friend lists.</li>
<li><code>contains()</code> is a hash-table lookup - near-instant even for huge sets, unlike a linear scan in a list.</li>
<li>No <code>get(i)</code> and no insertion order: traversal follows the hash table's own arrangement.</li>
<li><b>List vs Set</b>: choose List when order and duplicates matter (marks, steps, history), Set when membership must be unique (IDs, hashtags).</li></ul>
<p>jv4_14 adds a duplicate "java" and HashSet quietly refuses - then compares with an ArrayList that keeps both "tea" entries.</p>
""", diagram="jv4_list_vs_set", programs=["jv4_14"]),
    ],
}

NOTES = [SEC_4_1, SEC_4_2, SEC_4_3]
