"""DI04000021 Unit 3 notes: Inheritance, Interfaces and Abstraction."""
from java_content import make_TJ

SN = {}

T = make_TJ(SN)

SEC_3_1 = {
    "title": {"en": "3.1 Inheritance"},
    "items": [
        T("Concept and Need of Inheritance", """
<ul><li><b>Inheritance</b> lets one class (child/subclass) acquire the members of another (parent/superclass) with <code>extends</code>: the child is born with the parent's fields and methods.</li>
<li>Write it as an IS-A sentence: Employee IS-A Person. If the sentence is true in real life, inheritance is the right tool.</li>
<li><b>Need:</b> reusability (write common code once), extensibility (a child only adds its specialities) and maintainability (fix once in the parent - 200 children heal instantly).</li>
<li>Access rules: public/protected members flow freely; private members exist in the object but cannot be named directly by the child; constructors are never inherited.</li></ul>
<p>Run jv3_1: Employee uses intro() although it never wrote it - that is the whole miracle in one line.</p>
""", programs=["jv3_1"]),
        T("Types of Inheritance", """
<ul><li><b>Single:</b> one parent, one child - Person -> Employee.</li>
<li><b>Multilevel:</b> a chain of generations - Person -> Employee -> Manager; the grandchild receives everything from both.</li>
<li><b>Hierarchical:</b> one parent, many children - Vehicle -> Car, Bike (the most common real-world shape).</li>
<li><b>Hybrid:</b> a mixture of the above.</li>
<li><b>Multiple</b> (two class parents) is <b>NOT supported</b> in Java: if both parents defined the same field or method, the child could not choose. The same effect is obtained with <b>interfaces</b> (3.3).</li></ul>
""", diagram="jv3_inherit_types", programs=["jv3_2", "jv3_3"]),
        T("The super Keyword and Constructor Chaining", """
<ul><li><code>super</code> inside a child refers to the <b>parent part</b> of the object.</li>
<li><code>super(args)</code> calls the parent's constructor and must be the <b>first statement</b> of the child constructor; constructors always run top-down (parent first).</li>
<li>If the parent has ONLY parameterized constructors, the child must call <code>super(...)</code> explicitly - otherwise a compile error.</li>
<li><code>super.method()</code> calls the parent's version of an overridden method; <code>super.field</code> reads a hidden parent field.</li>
<li>Rule of thumb: <b>this</b> = current object, <b>super</b> = its parent.</li></ul>
""", diagram="jv3_super_this", programs=["jv3_4"]),
        T("Method Overriding", """
<ul><li><b>Overriding</b>: a child gives its own body to a method it inherited - same name, same parameters. Objective: specialisation (a LaserPrinter prints its own header).</li>
<li>Contrast with <b>overloading</b> (Unit 2): same name, different parameters, same class.</li>
<li>Rules: the signature must match; the return type must match (or be a subclass); the new method must not be MORE private than the inherited one; <b>static methods cannot be overridden</b> (they are hidden, not overridden); private and final methods cannot be overridden either.</li>
<li>Add <code>@Override</code> for free signature checking by the compiler.</li></ul>
""", diagram="jv3_override_vs", programs=["jv3_5"]),
        T("Dynamic Method Dispatch (Run-Time Polymorphism)", """
<ul><li>A parent reference may hold any child object: <code>Shape sh = new Circle();</code>.</li>
<li>For an <b>overridden</b> method, the JVM decides at run time which version to run by looking at the real object behind the reference - not the reference type.</li>
<li>This is the meaning of <b>run-time (dynamic) polymorphism</b>; overloading was the compile-time version.</li>
<li>Why it matters: you can loop over <code>Shape[]</code> and every shape still answers with its own area.</li></ul>
""", diagram="jv3_dispatch", programs=["jv3_6"]),
        T("The final Keyword", """
<ul><li><b>final variable</b> - a constant: assigned once, then read-only (naming convention: WHEELS, PI in capitals).</li>
<li><b>final method</b> - a subclass inherits it but CANNOT override it - the behaviour stays identical for all children.</li>
<li><b>final class</b> - cannot be extended at all; <code>String</code> and <code>Math</code> are famous final classes (protects them from being changed at runtime).</li></ul>
<p><b>Practical 11</b> runs in jv3_7 - uncomment the error lines in the lab to see the compiler refuse.</p>
""", programs=["jv3_7"]),
    ],
}

SEC_3_2 = {
    "title": {"en": "3.2 Abstract Classes"},
    "items": [
        T("Abstract Class and Abstract Methods", """
<ul><li>An <b>abstract method</b> declares WHAT without HOW: <code>abstract double area();</code> - no braces, no body.</li>
<li>A class with <b>at least one</b> abstract method must itself be declared <b>abstract</b>; an abstract class <b>cannot be instantiated</b> (no <code>new Shape()</code>).</li>
<li><b>Rules of an abstract class:</b> it may mix abstract and ready-made concrete methods, may hold any fields and constructors; a subclass extending it MUST implement every abstract method or declare itself abstract.</li>
<li>Use it for "half-built blueprints": share the common parts (displayType), force the special parts (area) on children.</li></ul>
<p><b>Practical 10(a)</b> builds exactly the syllabus's Shape with abstract area() and concrete displayType() - run jv3_8.</p>
""", programs=["jv3_8"]),
    ],
}

SEC_3_3 = {
    "title": {"en": "3.3 Interfaces"},
    "items": [
        T("Interface: Need, Declaration and Implementation", """
<ul><li>An <b>interface</b> is a pure contract: method declarations with no state. Need: when different classes must promise the same ability without being related by a family tree (a Printer and a Phone can both be <i>Callable</i>).</li>
<li><b>Declaration:</b> <code>interface Drawable { void draw(); }</code> - methods are implicitly <code>public abstract</code>; fields are implicitly <code>public static final</code> (constants).</li>
<li><b>Implementation:</b> <code>implements</code> keyword; the class must give <b>public</b> bodies for every method, or declare itself abstract.</li>
<li>Interfaces cannot be instantiated, but references are allowed: <code>Drawable d = new Circle();</code> - the object's own draw() runs (dynamic dispatch).</li>
<li>Abstract class vs interface table - the diagram.</li></ul>
""", diagram="jv3_abstract_vs", programs=["jv3_9"]),
        T("Multiple Inheritance and Default/Static Methods in Interfaces", """
<ul><li>Class-level multiple inheritance is banned, but a class may implement <b>any number of interfaces</b>: <code>class Report implements Printable, Showable</code> - safe because interface methods carry no state and no default body clashes.</li>
<li>Java 8 added <b>default methods</b> with bodies inside interfaces: ready-made behaviour that every implementer inherits for free; and <b>static methods</b> invoked on the interface name.</li>
<li>If two interfaces offer the same default method, the class must override it - diamond conflicts are solved explicitly, never silently.</li></ul>
""", diagram="jv3_interface_multi", programs=["jv3_10", "jv3_11"]),
    ],
}

SEC_3_4 = {
    "title": {"en": "3.4 Packages"},
    "items": [
        T("Defining, Importing and Built-in Packages", """
<ul><li>A <b>package</b> is a named family of classes stored in a matching folder: it prevents name clashes, shapes access control (default and protected are package-scoped) and keeps projects navigable.</li>
<li><b>Defining:</b> first line of the file: <code>package college;</code> - the file lives in a folder named college.</li>
<li><b>Importing:</b> <code>import college.Student;</code> for one class, <code>import java.util.*;</code> for many, or the fully qualified name with no import at all: <code>java.util.Date</code>.</li>
<li><b>Built-in packages:</b> java.lang (String, Math, Object - imported automatically), java.util (Scanner, ArrayList, Date), java.io (files), java.time (dates).</li></ul>
<p>Practical 12 (jv3_12) creates the <code>college</code> package with a real Student class and imports it from Main - watch both files in the program window.</p>
""", diagram="jv3_packages", programs=["jv3_12", "jv3_13", "jv3_14"]),
    ],
}

NOTES = [SEC_3_1, SEC_3_2, SEC_3_3, SEC_3_4]
