"""DI04000021 Unit 2 notes: Object-Oriented Programming Concepts."""
from java_content import make_TJ

SN = {}

T = make_TJ(SN)

SEC_2_1 = {
    "title": {"en": "2.1 Principles of OOP"},
    "items": [
        T("The Four Principles: Abstraction, Encapsulation, Inheritance, Polymorphism", """
<p>Object-Oriented Programming models software the way humans see the world - as <b>objects with data and behaviour</b>. Four principles support everything built with it:</p>
<ul><li><b>Abstraction</b> - show only what the user needs, hide the rest. You press an ATM's "Withdraw" button and never see its inner code. In Java: abstract classes and interfaces (Unit 3).</li>
<li><b>Encapsulation</b> - keep data and the methods that guard it together in one <b>safe box</b> (the class), making fields private and offering public methods. A capsule protects its medicine the same way.</li>
<li><b>Inheritance</b> - a new class <b>reuses</b> an existing class and only adds or changes what is special: class Car extends class Vehicle.</li>
<li><b>Polymorphism</b> (many forms) - the same name doing different work: <code>add(2,3)</code>, <code>add(2,3,4)</code> and <code>add(2.5,7.5)</code> all "add" in their own way.</li></ul>
<p>These four are the favourite definition question of Unit 2 - learn one real-world example for each.</p>
""", diagram="jv2_pillars"),
    ],
}

SEC_2_2 = {
    "title": {"en": "2.2 Classes and Objects"},
    "items": [
        T("Class, Object, Fields and Methods", """
<ul><li>A <b>class</b> is a user-defined blueprint: it describes which data (fields) and which actions (methods) its objects will have.</li>
<li>An <b>object</b> is a real instance created with <code>new</code>: <code>Student s1 = new Student();</code> - the class name is the type, <code>new</code> reserves memory in the heap.</li>
<li><b>Fields</b> (<code>int roll; String name;</code>) hold the state of each object separately; the <b>dot operator</b> reaches members: <code>s1.roll</code>, <code>s1.display()</code>.</li>
<li>A method called on an object works with <i>that object's own</i> fields - display() of s1 prints s1's data.</li></ul>
<p>Run the Student program and see how two objects keep separate values even though the code is written once.</p>
""", diagram="jv2_class_object", programs=["jv2_1"]),
    ],
}

SEC_2_3 = {
    "title": {"en": "2.3 Constructors"},
    "items": [
        T("Default, Parameterized and Overloaded Constructors", """
<ul><li>A <b>constructor</b> is a special member that initializes a freshly created object. Rules: same name as the class, <b>no return type</b> (not even void), called automatically by <code>new</code>.</li>
<li><b>Default constructor</b>: no parameters - gives fixed starting values. If you write NO constructor at all, Java quietly supplies an empty default one.</li>
<li><b>Parameterized constructor</b>: receives values used to set up the object differently each time.</li>
<li><b>Constructor overloading</b>: several constructors with different parameter lists; the compiler selects by the <code>new</code> call's arguments.</li>
<li>Constructors are not methods (they cannot be called like <code>obj.Book()</code>) and are not inherited.</li></ul>
""", diagram="jv2_ctor", programs=["jv2_3", "jv2_4"]),
    ],
}

SEC_2_4 = {
    "title": {"en": "2.4 Keywords: this and static"},
    "items": [
        T("The this Keyword", """
<ul><li><code>this</code> is a reference to the <b>current object</b> - the one on which the method or constructor is running.</li>
<li><b>Use 1 - shadowing:</b> when a parameter has the same name as a field, <code>this.name = name;</code> assigns the parameter into the field.</li>
<li><b>Use 2 - constructor chaining:</b> <code>this(...)</code> as the first statement of a constructor calls another constructor of the same class, so shared setup is written once.</li>
<li><b>Use 3 - current object as a value:</b> <code>return this;</code> or passing <code>this</code> as an argument.</li></ul>
""", programs=["jv2_5"]),
        T("The static Keyword", """
<ul><li><code>static</code> members belong to the <b>class</b>, not to any object: there is exactly ONE copy, created when the class is loaded.</li>
<li><b>Static variable</b> - shared by all objects; the classic counter in the live program.</li>
<li><b>Static method</b> - called with the class name (<code>Counter.report()</code>), receives no <code>this</code>, and can directly touch only static members. <code>main()</code> is static for this reason.</li>
<li><b>Static block</b> - runs once when the class is loaded, before main(); used for one-time setup.</li>
<li>A <b>static nested class</b> is a helper class attached to an outer class without needing an outer object (Unit 5 uses it in lambdas' cousins).</li></ul>
""", diagram="jv2_this_static", programs=["jv2_6"]),
    ],
}

SEC_2_5 = {
    "title": {"en": "2.5 Access Modifiers"},
    "items": [
        T("public, private, protected, default", """
<p>Access modifiers decide <b>who may use</b> a class member:</p>
<ul><li><b>private</b> - only inside the same class. Hiding fields as private is the heart of encapsulation.</li>
<li><b>default</b> (no keyword written) - visible everywhere in the same <b>package</b>.</li>
<li><b>protected</b> - package + subclasses in any package (needed with inheritance, Unit 3).</li>
<li><b>public</b> - visible from anywhere.</li></ul>
<ul><li>Order from most open to most restricted: public &gt; protected &gt; default &gt; private.</li>
<li>Good practice: fields private, behaviour public - outsiders change data only through checked methods (<code>deposit()</code> rejects negative amounts).</li></ul>
""", diagram="jv2_access", programs=["jv2_7"]),
    ],
}

SEC_2_6 = {
    "title": {"en": "2.6 Methods"},
    "items": [
        T("Method Definition, Calling and Overloading", """
<ul><li><b>Definition:</b> <code>returnType name(parameters) { body }</code> - e.g. <code>int add(int x, int y) { return x + y; }</code>.</li>
<li><b>Calling:</b> run the method by its name with matching arguments: <code>int s = add(7, 5);</code>. Values flow into parameters; <code>return</code> sends exactly one value back.</li>
<li><code>void</code> methods return nothing - they just do work.</li>
<li><b>Method overloading</b>: the same name with different parameter lists (number or type). The compiler picks the match at <b>compile time</b> - this is compile-time (static) polymorphism. Return type alone cannot overload.</li></ul>
""", programs=["jv2_2", "jv2_8"]),
    ],
}

SEC_2_7 = {
    "title": {"en": "2.7 Strings"},
    "items": [
        T("The String Class and Common Methods", """
<ul><li><code>String</code> is a class; texts are objects created from literals: <code>String s = "GTU Diploma";</code>.</li>
<li>Strings are <b>immutable</b> - every change creates a new string; ten edits create ten objects (for heavy editing use StringBuilder).</li>
<li>Top methods for the exam: <code>length()</code>, <code>charAt(i)</code>, <code>substring(be)</code>, <code>toUpperCase()</code>, <code>toLowerCase()</code>, <code>indexOf()</code>, <code>contains()</code>, <code>trim()</code>, <code>replace()</code>, <code>equals()</code>, <code>concat()</code>, <code>split()</code>, <code>join()</code>.</li>
<li>Positions are <b>0-based</b>; substring's end index is <b>excluded</b>.</li>
<li>Compare text with <code>equals()</code>, NEVER with <code>==</code> (that compares references and works only accidentally when both literals share one object).</li></ul>
""", diagram="jv2_strings", programs=["jv2_9", "jv2_10"]),
    ],
}

SEC_2_8 = {
    "title": {"en": "2.8 Wrapper Classes"},
    "items": [
        T("Wrapper Classes, Autoboxing and Unboxing", """
<ul><li>Java is object oriented, but primitives are not objects. Every primitive has an <b>object twin - a wrapper class</b>: Byte, Short, Integer, Long, Float, Double, Character, Boolean.</li>
<li>Why wrap? Collections (Unit 4) store only objects; wrappers also carry helpers: <code>Integer.parseInt()</code>, <code>MAX_VALUE</code>, <code>toBinaryString()</code>.</li>
<li><b>Autoboxing</b> - automatic primitive -> wrapper: <code>Integer o = 42;</code>. <b>Unboxing</b> - automatic wrapper -> primitive: <code>int m = o;</code>. Before Java 5 this was written by hand with <code>valueOf()</code> / <code>intValue()</code>.</li>
<li>Wrapper objects can be <code>null</code>, so unboxing a null throws an exception (Unit 4).</li></ul>
""", diagram="jv2_boxing", programs=["jv2_11", "jv2_12"]),
    ],
}

SEC_2_9 = {
    "title": {"en": "2.9 User Input"},
    "items": [
        T("Scanner Class and Command Line Arguments", """
<ul><li><b>Scanner</b> (java.util) reads typed input: attach it to <code>System.in</code> once, then use <code>nextLine()</code> for whole lines, <code>next()</code> for one token, <code>nextInt()</code>, <code>nextDouble()</code> for numbers.</li>
<li><b>The ENTER trap:</b> numeric reads leave the pressed Enter in the queue, so a following <code>nextLine()</code> returns empty. Cure: one extra <code>sc.nextLine()</code> right after the number.</li>
<li><b>Command line arguments</b> - strings given after the run command (<code>java Main 15 27</code>) arrive in <code>String[] args</code>: no waiting, perfect for fixed settings; convert with <code>Integer.parseInt()</code>.</li></ul>
""", programs=["jv2_12", "jv2_13", "jv2_14"]),
    ],
}

SEC_2_10 = {
    "title": {"en": "2.10 Garbage Collection"},
    "items": [
        T("Garbage Collection and the finalize() Method", """
<ul><li>Java frees memory <b>automatically</b>: the <b>garbage collector</b> removes objects that no reference can reach anymore. There is no free() / delete keyword like in C++.</li>
<li>An object becomes garbage when its references are gone: <code>it = null;</code>, or the variable goes out of scope.</li>
<li><code>System.gc()</code> only <b>requests</b> a collection - the JVM decides when and in which order; you can never force it.</li>
<li><b>finalize()</b> is invoked by the JVM on an object just before destruction - a last chance to release external resources. It is deprecated in modern Java in favour of try-with-resources (Unit 5), but you must know it for the syllabus.</li></ul>
""", diagram="jv2_gc", programs=["jv2_15"]),
    ],
}

NOTES = [SEC_2_1, SEC_2_2, SEC_2_3, SEC_2_4, SEC_2_5, SEC_2_6, SEC_2_7, SEC_2_8, SEC_2_9, SEC_2_10]
