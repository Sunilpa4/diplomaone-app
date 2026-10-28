"""DI04000021 Unit 3 extras: syntax sheet, viva, exam questions."""
from java_content import SXE, VE, XE, G

SYNTAX = [
    G("Inheritance", [
        SXE("extends basics", """class Employee extends Person { }
// child gets parent's fields + methods
Employee e = new Employee();
e.intro();      // inherited method""",
            "extends = acquire parent members"),
        SXE("super keyword", """class Circle extends Shape {
  Circle(double r) {
    super(\"circle\");    // parent ctor, first
    super.info();       // parent's method
    super.name;         // parent's field
  }
}""",
            "super = parent part; super() goes first"),
        SXE("Overriding + dispatch", """class Circle extends Shape {
  @Override
  double area() { return 3.14*r*r; }
}
Shape sh = new Circle();
sh.area();    // runs Circle.area()""",
            "same signature; object decides at run time"),
        SXE("final keyword", """final int WHEELS = 2;     // constant
final void service() { }  // no override
final class Pet { }       // no subclass""",
            "final = constant / frozen method / sealed class"),
    ]),
    G("Abstraction and Interfaces", [
        SXE("Abstract class", """abstract class Shape {
  abstract double area();   // no body
  void displayType() { }    // concrete ok
}
class Rect extends Shape {
  double area() { return l*w; }
}
// new Shape()  -- compile error""",
            "child must implement or be abstract"),
        SXE("Interface", """interface Drawable {
  void draw();            // public abstract
  int UNIT = 20;          // public static final
}
class Circle implements Drawable {
  public void draw() { }  // MUST be public
}""",
            "pure contract; implements = promise bodies"),
        SXE("Java 8 interface methods", """interface ShapeMath {
  double area();
  default String desc() { return \"d\"; }
  static String banner() { return \"b\"; }
}
ShapeMath.banner();       // static on interface""",
            "default = inheritable body; static = on interface"),
        SXE("Multiple inheritance", """class Report implements
    Printable, Showable { }
// two interfaces, one class - safe
// two CLASSES as parents - forbidden""",
            "many interfaces OK, one class parent only"),
    ]),
    G("Packages", [
        SXE("User package + import", """// file college/Student.java
package college;
public class Student { }

// file Main.java
import college.Student;
Student s = new Student(12, \"Pooja\");""",
            "first line package; import before class"),
        SXE("Built-in packages", """import java.util.Scanner;
import java.util.Date;
import java.util.*;        // wildcard
// java.lang: auto (String, Math)""",
            "java.lang is automatic; others need import"),
    ]),
]

_VIVA = [
    VE("What is inheritance?", "A mechanism in which a new class (child/subclass) acquires the fields and methods of an existing class (parent/superclass) using extends."),
    VE("Give the need of inheritance.", "Reusability of tested code, easy extension by adding only specialities, and single-point maintenance in the parent."),
    VE("What is an IS-A relationship?", "Employee IS-A Person: if the sentence is true in real life, let Employee extend Person."),
    VE("Which keyword creates inheritance?", "extends for classes; implements for interfaces."),
    VE("What does a child NOT inherit?", "Private members (they exist but cannot be named) and constructors."),
    VE("List the types of inheritance in Java.", "Single, multilevel, hierarchical, hybrid; multiple (two class parents) is NOT supported."),
    VE("Why is multiple inheritance of classes banned?", "If both parents had the same field or method the child would face ambiguity; interfaces solve it without state."),
    VE("What is multilevel inheritance?", "A chain A -> B -> C; C receives members of both A and B (Person -> Employee -> Manager)."),
    VE("What is hierarchical inheritance?", "One parent, many children - Vehicle -> Car, Bike."),
    VE("What is the super keyword?", "Reference to the parent part of the object: super(args) calls the parent constructor, super.method() the parent method, super.field a hidden field."),
    VE("Where must super() be written and why?", "As the first statement of the child constructor; the parent part must be built before the child's body runs."),
    VE("What happens if the parent has only parameterized constructors?", "Java cannot silently add super() - the child must call super(args) explicitly, else compile error."),
    VE("What is method overriding?", "A child redefines an inherited method with the SAME name and signature so its own version runs instead."),
    VE("Overriding vs overloading?", "Same signature in child class, run-time, vs different parameters in one class, compile-time."),
    VE("What is @Override?", "An annotation asking the compiler to verify the method actually overrides one - catches signature typos."),
    VE("Which methods cannot be overridden?", "static (they are hidden, not overridden), private (not visible) and final methods."),
    VE("What is dynamic method dispatch?", "Calling an overridden method through a parent reference - the JVM runs the version of the actual object at run time."),
    VE("Give an example of run-time polymorphism.", "Shape sh = new Circle(); sh.area(); - Circle's area runs although the reference is typed Shape."),
    VE("What are the three uses of final?", "final variable = constant; final method = cannot be overridden; final class = cannot be extended."),
    VE("Why is String a final class?", "So no subclass can change string behaviour after an object is created - protects shared literals."),
    VE("What is an abstract method?", "A declaration without a body: abstract double area(); - the child provides the body."),
    VE("What is an abstract class? Can it be instantiated?", "A class declared abstract, possibly with abstract methods; no - new Shape() is a compile error."),
    VE("Give the rules of abstract classes.", "May mix abstract and concrete methods; may have fields/constructors; a subclass must implement every abstract method or be abstract too."),
    VE("When do you choose an abstract class?", "For a family blueprint that shares ready-made code (displayType) yet forces children to fill in specifics (area)."),
    VE("What is an interface?", "A pure contract of method declarations (implicitly public abstract) plus constants (public static final); no state, no constructors."),
    VE("What is the need of an interface?", "Unrelated classes promising the same ability - a Printer and a Phone can both be Callable without sharing a parent."),
    VE("How does a class implement an interface?", "class X implements Drawable { public void draw() { } } - every method must be given a public body."),
    VE("Why must an implemented method be public?", "Interface methods are public abstract; an implementing method cannot reduce visibility."),
    VE("Can an interface be instantiated? What about a reference?", "Never instantiated; but Drawable d = new Circle(); works - the object's draw() runs."),
    VE("What is multiple inheritance with interfaces?", "Implementing several interfaces at once - safe because interfaces have no state or clashing bodies."),
    VE("What are default methods in interfaces?", "Java 8+ interface methods with bodies, inherited free by every implementer; the class may override them."),
    VE("What happens if two interfaces give the same default method?", "The implementing class must override it and resolve the conflict - Java never picks silently."),
    VE("What are static methods in interfaces?", "Methods belonging to the interface itself, called as ShapeMath.banner(); not inherited into instances."),
    VE("Abstract class vs interface: three differences.", "Fields any vs constants only; constructor yes vs no; one parent class vs many interfaces."),
    VE("What is a package?", "A named group of related classes in a matching folder; controls name clashes and access (default/protected are package-based)."),
    VE("How do you define and import your own package?", "Write package college; in college/Student.java, then import college.Student; in the user file."),
    VE("Name three built-in packages.", "java.lang (String, Math - automatic), java.util (Scanner, ArrayList), java.io (files); also java.time."),
    VE("Which package never needs an import?", "java.lang."),
    VE("What does import java.util.* mean?", "Import every public class of java.util (the wildcard) - still per-name, not the whole library copied."),
    VE("How must cross-package members be declared?", "public (or protected for subclasses)."),
    VE("Is the fully-qualified name legal without import?", "Yes: java.util.Date d = new java.util.Date(); - import is just a shortcut."),
    VE("What is a hybrid inheritance example?", "Vehicle -> Car -> PetrolCar plus Vehicle -> Bike: multilevel and hierarchical combined."),
    VE("If a parent method is final, what about a useful child version?", "Impossible by design - the child inherits the exact behaviour; redesign with a non-final method."),
    VE("In Practical 10, why doesn't Drawable conflict with Shape?", "Shape is the single parent class (state, constructors); Drawable only adds a promise (draw) with no state - no diamond problem."),
]

assert len(_VIVA) == 44
VIVA = [
    G("Inheritance and super", _VIVA[0:13]),
    G("Overriding, Dispatch, final", _VIVA[13:20]),
    G("Abstract Classes", _VIVA[20:24]),
    G("Interfaces", _VIVA[24:33]),
    G("Packages", _VIVA[33:44]),
]

EXAM_QS = [
    XE("What is inheritance? Explain its need with an example.", 4),
    XE("Explain the types of inheritance with diagrams.", 6),
    XE("Write a Java program for multilevel inheritance (Person, Employee, Manager). (Practical 9)", 6),
    XE("Explain the super keyword with constructor chaining.", 4),
    XE("Differentiate method overloading and method overriding.", 4),
    XE("Explain dynamic method dispatch with a Shape example.", 4),
    XE("Explain the final keyword: variable, method, class. (Practical 11)", 4),
    XE("What is an abstract class? State its rules with an example.", 4),
    XE("Write a program for abstract class Shape with area() and displayType(). (Practical 10a)", 6),
    XE("What is an interface? Explain declaration and implementation.", 4),
    XE("Explain how interfaces achieve multiple inheritance in Java. (Practical 10b)", 4),
    XE("Explain default and static methods in interfaces (Java 8+).", 3),
    XE("Differentiate abstract class and interface.", 4),
    XE("Explain user-defined packages with a program. (Practical 12)", 6),
    XE("List built-in packages of Java and their purpose.", 3),
]
