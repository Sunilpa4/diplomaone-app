"""DI04000021 Unit 3 - solved Java programs (inheritance, interfaces, packages).
All outputs genuine. Practicals 9-12."""
from java_content import JP

PROGRAMS = [

JP("jv3_1", "Single inheritance: Person and Employee", '''
class Person {                 // parent (super class)
  String name = "Ravi";
  int age = 35;
  void intro() {
    String w = name + ", age " + age;
    System.out.println(w);
  }
}

class Employee extends Person {  // child (sub class)
  double salary = 42000;
  void work() {
    System.out.println("pay = " + salary);
  }
}

class Main {
  public static void main(String[] a) {
    Employee e = new Employee();
    e.intro();            // inherited from Person
    e.work();             // own method
    // both fields came along too:
    String row = e.name + " earns ";
    System.out.println(row + e.salary);
  }
}
''', expl="""
<p><b>Practical 9 (part 1).</b> With <code>extends</code>, the child class receives ALL fields and methods of the parent (except private ones and constructors).</p>
<ul><li><code>Employee e = new Employee()</code> has intro(), work(), name, age AND salary - as if the parent's code were copied in.</li>
<li>This relation is written <i>Employee IS-A Person</i> - inheritance models real "is a" facts.</li></ul>
"""),

JP("jv3_2", "Multilevel inheritance: Person, Employee, Manager", '''
class Person {                       // level 1
  String name = "Ravi";
  void intro() {
    System.out.println("I am " + name);
  }
}

class Employee extends Person {      // level 2
  double salary = 42000;
  void work() {
    String row = "I work for " + salary;
    System.out.println(row);
  }
}

class Manager extends Employee {     // level 3
  String dept = "Computer";
  void lead() {
    System.out.println("I lead " + dept);
  }
}

class Main {
  public static void main(String[] a) {
    Manager m = new Manager();
    m.intro();       // from Person
    m.work();        // from Employee
    m.lead();        // own
  }
}
''', expl="""
<p><b>Practical 9 (part 2).</b> <b>Multilevel inheritance</b>: Parent -> Child -> Grandchild. A Manager gets the members of both Person and Employee in one step.</p>
<ul><li>The chain is unlimited: every level passes everything it has (and got) further down.</li>
<li>Constructors also run in order Person -> Employee -> Manager when a Manager is created (see jv3_4 with super).</li></ul>
"""),

JP("jv3_3", "Types of inheritance: single, multilevel, hierarchical, hybrid", '''
class Vehicle {                     // one parent
  String type = "vehicle";
}

class Car extends Vehicle { }       // single: one child

class Bike extends Vehicle { }
// hierarchical: many children

class PetrolCar extends Car { }     // + multilevel

class Main {
  public static void main(String[] a) {
    Car c = new Car();
    Bike b = new Bike();
    PetrolCar p = new PetrolCar();
    System.out.println("car: " + c.type);
    System.out.println("bike: " + b.type);
    String pt = p.type;
    System.out.println("petrol = " + pt);
  }
}
''', expl="""
<ul><li><b>Single</b>: one parent, one child (Person -> Employee).</li>
<li><b>Multilevel</b>: a chain of generations (Car -> PetrolCar).</li>
<li><b>Hierarchical</b>: one parent, many children (Vehicle -> Car, Bike).</li>
<li><b>Hybrid</b>: a mix of the above (allowed).</li>
<li><b>Multiple</b> (two parents for one class) is <b>NOT allowed</b> for classes in Java - fields/methods would clash. The same effect is done with <b>interfaces</b> (see jv3_10).</li></ul>
"""),

JP("jv3_4", "The super keyword: constructor chaining and parent methods", '''
class Shape {
  String name;
  Shape(String name) {         // parent constructor
    this.name = name;
    System.out.println("Shape: " + name);
  }
  void info() {
    System.out.println("I am a 2D shape");
  }
}

class Circle extends Shape {
  double r;
  Circle(double r) {
    super("circle");           // 1. call parent ctor FIRST
    this.r = r;
  }
  void info() {
    super.info();              // 2. parent's version
    System.out.println("radius = " + r);
  }
}

class Main {
  public static void main(String[] a) {
    Circle c = new Circle(2.5);
    c.info();
  }
}
''', expl="""
<ul><li><code>super(...)</code> calls the <b>parent constructor</b> and must be the first statement of the child constructor. If the parent has only parameterized constructors, the child MUST call super(...) itself.</li>
<li><code>super.method()</code> explicitly calls the parent's version of a method - essential when the child overrides it.</li>
<li><code>super.field</code> reads the parent's field when names clash.</li>
<li>Watch the output order: the parent's constructor runs before the child's body - <b>top-down construction</b>.</li></ul>
"""),

JP("jv3_5", "Method overriding vs overloading", '''
class Printer {
  void print(String s) { }            // overloading:
  void print(String s, int n) { }     // different args

  void header() {
    System.out.println("-- basic --");
  }
}

class LaserPrinter extends Printer {
  @Override                          // annotation checks it
  void header() {
    System.out.println("** LaserJet **");
  }
}

class Main {
  public static void main(String[] a) {
    LaserPrinter hp = new LaserPrinter();
    hp.print("A", 5);       // overloaded form
    hp.header();            // OVERRIDDEN version runs
    // the parent's version is replaced
  }
}
''', expl="""
<ul><li><b>Overloading</b> = same name, different parameter list, same class (compile-time choice).</li>
<li><b>Overriding</b> = same name AND same signature in a child class; the child's version replaces the parent's at run time.</li>
<li><code>@Override</code> is an optional annotation - the compiler then refuses to compile if you mistyped the signature.</li>
<li>The child method cannot be <i>more private</i> than the parent's (e.g. public -> private is an error).</li></ul>
"""),

JP("jv3_6", "Dynamic method dispatch (run-time polymorphism)", '''
class Shape {
  double area() {
    return 0;
  }
}
class Circle extends Shape {
  double r = 5;
  double area() { return 3.14 * r * r; }
}
class Square extends Shape {
  double s = 4;
  double area() { return s * s; }
}

class Main {
  public static void main(String[] a) {
    Shape sh;                       // parent reference
    sh = new Circle();              // holds a Circle
    double ar = sh.area();
    System.out.println("area = " + ar);
    sh = new Square();              // now a Square
    ar = sh.area();
    System.out.println("area = " + ar);
    // WHICH area() runs is decided
    // at RUN TIME by the object, not
    // by the reference type.
  }
}
''', expl="""
<ul><li>A <b>parent reference may point to a child object</b>: <code>Shape sh = new Circle();</code>.</li>
<li>When an overridden method is called through that reference, Java looks at the <b>actual object</b> (Circle / Square) - not at the reference type - and runs the child's version.</li>
<li>This is <b>dynamic method dispatch</b> = run-time polymorphism; the choice happens while the program executes.</li>
<li>It is the engine behind flexible designs: one variable, many behaviours.</li></ul>
"""),

JP("jv3_7", "The final keyword: variable, method, class", '''
class Vehicle {
  final int WHEELS = 2;       // constant
  final void service() {
    System.out.println("service done");
  }
}

class Bike extends Vehicle {
  // void service() { }
  // ^ ERROR: a final method cannot override
  void horn() {
    System.out.println("peep");
  }
}

final class Pet {}            // no class may extend it

class Main {
  public static void main(String[] a) {
    Vehicle v = new Vehicle();
    int w = v.WHEELS;
    System.out.println("wheels = " + w);
    // v.WHEELS = 4;  // ERROR: cannot assign
    Bike b = new Bike();
    b.service();              // parent's, never changed
    b.horn();
  }
}
''', expl="""
<p><b>Practical 11.</b> <code>final</code> = "end of change", with three seats:</p>
<ul><li><b>final variable</b> - a constant: assigned once, then read-only.</li>
<li><b>final method</b> - subclasses inherit it but cannot override it.</li>
<li><b>final class</b> - cannot be extended at all (String itself is final!).</li>
<li>The commented-out lines would produce real compile errors - try them in lab.</li></ul>
"""),

JP("jv3_8", "Abstract class Shape with abstract method area()", '''
// abstract class = half-built blueprint
abstract class Shape {
  String type = "shape";

  abstract double area();   // no body
  // -> the child class MUST write it

  void displayType() {        // normal method
    System.out.println("Type: " + type);
  }
}

class Rectangle extends Shape {
  double l = 12, w = 5;
  Rectangle() { type = "rectangle"; }
  double area() {             // duty fulfilled
    return l * w;
  }
}

class Main {
  public static void main(String[] a) {
    // Shape s = new Shape();  // ERROR: abstract!
    Rectangle r = new Rectangle();
    r.displayType();          // inherited
    double ar = r.area();
    System.out.println("area = " + ar);
  }
}
''', expl="""
<p><b>Practical 10 (part 1).</b></p>
<ul><li>An <b>abstract method</b> has only a declaration - no body; any subclass must implement it or be abstract itself.</li>
<li>An <b>abstract class</b> mixes abstract and normal methods (displayType is ready-made); it <b>cannot be instantiated</b> - no <code>new Shape()</code>.</li>
<li>Use it to force a common contract ("every shape has an area") while sharing concrete code.</li></ul>
"""),

JP("jv3_9", "Interface Drawable implemented by Circle and Rectangle", '''
interface Drawable {          // a pure contract
  void draw();                // auto public abstract
  int UNIT = 20;              // auto public static final
}

abstract class Shape {
  String type = "shape";
  void displayType() { }
}

class Circle extends Shape
    implements Drawable {     // both together
  public void draw() {        // must be public!
    System.out.println("O  (circle)");
  }
}

class Rectangle extends Shape
    implements Drawable {
  public void draw() {
    System.out.println("[ ] (rectangle)");
  }
}

class Main {
  public static void main(String[] a) {
    Drawable d1 = new Circle();
    d1.draw();
    Drawable d2 = new Rectangle();
    d2.draw();
    int u = Drawable.UNIT;
    System.out.println("UNIT = " + u);
  }
}
''', expl="""
<p><b>Practical 10 (part 2).</b></p>
<ul><li>An <b>interface</b> declares <i>what</i> to do, never <i>how</i>: methods are implicitly <code>public abstract</code>, fields are implicitly <code>public static final</code> (constants).</li>
<li>A class <code>implements</code> an interface and must write a <b>public</b> body for every method; it may also extend another class at the same time (as Circle and Rectangle do).</li>
<li>Interface references work like parent references: <code>Drawable d1 = new Circle();</code> dispatches to the object's draw().</li></ul>
"""),

JP("jv3_10", "Multiple inheritance with two interfaces", '''
interface Printable {
  void print();
}
interface Showable {
  void show();
}

class Report implements Printable,
    Showable {
  public void print() {
    System.out.println("printing...");
  }
  public void show() {
    System.out.println("showing...");
  }
}

class Main {
  public static void main(String[] a) {
    Report r = new Report();
    r.print();
    r.show();
  }
}
''', expl="""
<ul><li>Classes get only ONE parent, but interfaces are unlimited: <code>implements Printable, Showable</code>.</li>
<li>No clash can happen, because interface methods carry no state and (normally) no body - the child provides the single implementation either way.</li>
<li>This is how Java supplies <b>multiple inheritance</b> safely.</li></ul>
"""),

JP("jv3_11", "Default and static methods in an interface (Java 8+)", '''
interface ShapeMath {
  double area();                    // abstract

  default String desc() {           // ready-made
    return "I have area " + area();
  }
  static String banner() {          // called on the interface
    return "== shape maths ==";
  }
}

class Square implements ShapeMath {
  double s = 4;
  public double area() { return s * s; }
  // desc() inherited for free
}

class Main {
  public static void main(String[] a) {
    Square q = new Square();
    System.out.println(ShapeMath.banner());
    System.out.println(q.desc());
  }
}
''', expl="""
<ul><li>Since Java 8 interfaces may hold <b>default</b> methods with bodies - inherited by every implementing class without rewriting.</li>
<li><b>static methods in interfaces</b> belong to the interface itself and are called as <code>ShapeMath.banner()</code>.</li>
<li>If two interfaces offer the same default method, the class must override it to resolve the conflict (the diamond rule).</li></ul>
"""),

JP("jv3_12", "User-defined package: create, import and use", '''
import college.Student;

class Main {
  public static void main(String[] a) {
    // Student lives in the package
    Student s = new Student(
        12, "Pooja");
    System.out.println("roll = " + s.roll);
    System.out.println("name = " + s.name);
    System.out.println(s.intro());
  }
}
''', extra={"college/Student.java": '''
// File: college/Student.java
package college;         // folder = package

public class Student {
  public int roll;
  public String name;

  public Student(int r, String n) {
    roll = r;
    name = n;
  }
  public String intro() {
    return "I am " + name;
  }
}
'''}, show_extra=True, expl="""
<p><b>Practical 12.</b> A <b>package</b> is a named folder for related classes - it avoids name clashes and makes imports possible.</p>
<ul><li>The class file writes <code>package college;</code> first and sits inside a folder named <code>college</code>.</li>
<li>Main.java takes it in with <code>import college.Student;</code>. Without import, its full name <code>college.Student</code> would be needed.</li>
<li>Members used from another package must be <b>public</b>.</li>
<li>The compile line is <code>javac college/Student.java Main.java</code> and then <code>java Main</code>.</li></ul>
"""),

JP("jv3_13", "Built-in packages: java.lang and java.util", '''
import java.util.ArrayList;     // from java.util
import java.util.Date;

class Main {
  public static void main(String[] a) {
    // java.lang is imported AUTOMATICALLY
    System.out.println(Math.sqrt(81));
    System.out.println(Math.max(4, 9));
    String s = "auto-imported";
    System.out.println(s.length());

    Date today = new Date();    // java.util, needed import
    System.out.println(today.getDate());
    ArrayList<String> list =
        new ArrayList<>();
    list.add("red");
    System.out.println(list);   // Unit 4!
  }
}
''', expl="""
<ul><li>Java ships hundreds of reusable packages: <b>java.lang</b> (String, Math, Object - auto-imported), <b>java.util</b> (Scanner, ArrayList, Date), java.io, java.net, java.time ...</li>
<li><code>java.lang</code> is special: it is always available without an import statement.</li>
<li>For every other package write <code>import java.util.Date;</code> or use the wildcard <code>import java.util.*;</code>.</li>
<li>Package names are lower case by convention.</li></ul>
"""),

JP("jv3_14", "Cross-package access: protected fields in subclasses", '''
import college.Student;

// a subclass IN ANOTHER package
class Topper extends Student {
  Topper() {
    super(1, "Meera");
  }
  void show() {
    // roll is protected in Student:
    // visible here because Topper
    // is a SUBCLASS (protected rule)
    System.out.println("roll = " + roll);
    System.out.println("name = " + name);
  }
}

class Main {
  public static void main(String[] a) {
    Topper t = new Topper();
    t.show();
  }
}
''', extra={"college/Student.java": '''
// File: college/Student.java
package college;

public class Student {
  protected int roll;
  protected String name;

  public Student(int r, String n) {
    roll = r;
    name = n;
  }
}
'''}, show_extra=True, expl="""
<ul><li><b>protected</b> members are visible inside the package AND inside any <b>subclass</b>, even in a different package.</li>
<li>Here Student (package college) has protected fields; class Topper in the default package extends it and reads roll and name directly.</li>
<li>Without extends, protected fields would be invisible from the default package - that is exactly the difference between default and protected.</li></ul>
"""),
]
