"""DI04000021 Unit 2 extras: syntax sheet, viva, exam questions."""
from java_content import SXE, VE, XE, G

SYNTAX = [
    G("Class, Object, Constructors", [
        SXE("Class and object", """class Student {
  int roll;
  String name;
  void display() { }
}
Student s = new Student();   // object
s.roll = 1;                  // dot access
s.display();                 // method call""",
            "class = blueprint; new = creates object"),
        SXE("Constructors", """Book() { }                  // default
Book(String t) {         // parameterized
  this.title = t;        // this = field
}
Book(String t, double p) {
  this(t);               // chaining (first line)
  this.price = p;
}""",
            "same name as class; no return type"),
        SXE("Method form", """static int add(int x, int y) {
  return x + y;
}
int s = add(7, 5);       // call""",
            "returnType name(params); void = nothing back"),
    ]),
    G("static, Access, Overloading", [
        SXE("static members", """static int total = 0;      // one copy
static { }                 // runs at class load
static void report() { }   // no this inside
Counter.report();          // call by class name""",
            "belongs to class; static touches static only"),
        SXE("Access modifiers", """class X {
  public String a;      // everywhere
  protected String b;   // package + subclasses
  String c;             // default: package
  private double d;     // this class only
}""",
            "public > protected > default > private"),
        SXE("Overloading", """int add(int a, int b) { }
int add(int a, int b, int c) { }
double add(double a, double b) { }

new Account();          // constructor
new Account("Riya");    // overloading too
new Account("Amit", 5000);""",
            "same name, different parameter list"),
    ]),
    G("Strings and Wrappers", [
        SXE("String methods", """s.length()       s.charAt(4)
s.substring(4)     s.substring(0,3)
s.toUpperCase()    s.toLowerCase()
s.indexOf("Dip")   s.contains("oma")
s.trim()           s.replace('D','d')
s.equals(t)        s.split(",")
String.join("-", arr)""",
            "immutable; new string returned; 0-based"),
        SXE("Wrappers and boxing", """Integer o = 42;          // autoboxing
int m = o;               // unboxing
int n = Integer.parseInt("153");
Integer.MAX_VALUE""",
            "wrapper = object twin of a primitive"),
    ]),
    G("Input and Garbage Collection", [
        SXE("Scanner input", """import java.util.Scanner;
Scanner sc = new Scanner(System.in);
String n = sc.nextLine();   // whole line
int m = sc.nextInt();       // number
sc.nextLine();              // eat leftover Enter""",
            "after a number read, eat the Enter"),
        SXE("Command line args + GC", """public static void main(String[] args)
// java Main 15 27
args.length; args[0]; args[1];

it = null;                  // object free
System.gc();                // request GC
protected void finalize() { }
""",
            "args are strings; finalize runs before destroy"),
    ]),
]

_VIVA = [
    VE("What is OOP?", "A way of organising programs around objects that hold data (fields) and behaviour (methods), instead of procedures."),
    VE("Name the four principles of OOP.", "Abstraction, encapsulation, inheritance and polymorphism."),
    VE("What is abstraction? Give an example.", "Showing only the necessary features and hiding the details - an ATM user sees buttons, not the dispensing machinery. Done via abstract classes and interfaces."),
    VE("What is encapsulation? Give an example.", "Binding data and its guarding methods inside one class, with private fields - like a capsule protecting medicine; BankAcc keeps bal private and checks deposit()."),
    VE("What is inheritance?", "Creating a new class by reusing an existing class with keyword extends, so common code is written once."),
    VE("What is polymorphism?", "\"Many forms\": the same name doing different work, e.g. overloaded add() methods; runtime version comes via overriding (Unit 3)."),
    VE("What is a class? What is an object?", "A class is a blueprint (a type) describing fields and methods; an object is a real instance of it living in heap memory, created with new."),
    VE("Difference between fields and local variables?", "Fields belong to an object and live as long as it; local variables exist only inside their method or block."),
    VE("How do you access members of an object?", "With the dot operator: s1.roll and s1.display()."),
    VE("What is a constructor?", "A special member that runs automatically at new to initialize the object; it has the class name and no return type."),
    VE("What is a default constructor?", "A constructor with no parameters; if a class has none, Java adds an empty one silently."),
    VE("What is a parameterized constructor?", "A constructor that receives values, e.g. new Book(\"Java\", 299) initializes title and price in one step."),
    VE("What is constructor overloading?", "Several constructors with different parameter lists in one class; the compiler matches the new call."),
    VE("Can a constructor have a return type or be called on an object?", "No - a return type (even void) would turn it into an ordinary method, and obj.Book() is illegal."),
    VE("Differentiate constructor and method.", "Class name vs any name; no return type vs mandatory one; runs at new vs when called; not inherited vs inheritable."),
    VE("What is this keyword?", "A reference to the current object - used to separate fields from same-named parameters, to chain constructors with this(), and to return the current object."),
    VE("Where must this() be written?", "As the very first statement of a constructor."),
    VE("What is static variable?", "A class-level variable with a single copy shared by all objects, loaded once when the class loads."),
    VE("What is static method?", "A method callable with the class name; it has no this and can directly use only static members."),
    VE("Why is main() static?", "The JVM must start the program without creating any object first."),
    VE("What is a static block and when does it run?", "A block that runs once when the class is loaded, before main()."),
    VE("List the four access modifiers in restrictiveness order.", "private < default < protected < public (private most restricted)."),
    VE("Difference between default and protected?", "default is visible inside the same package only; protected also in subclasses outside the package."),
    VE("Why keep fields private?", "So outside code cannot put illegal values: changes pass through checked public methods (encapsulation)."),
    VE("What are getters and setters?", "Public methods that read (getBal) or update (deposit) private fields under control of the class."),
    VE("What is method overloading?", "Same method name with different parameter lists in one class; decided at compile time (compile-time polymorphism)."),
    VE("Is changing only the return type valid overloading?", "No - the parameter list must differ; the return type alone cannot overload."),
    VE("What is a String in Java?", "A class; its objects hold immutable character text built from literals like \"GTU\"."),
    VE("What does string immutability mean?", "Methods never change the original string - they create and return a new one."),
    VE("Give any four String methods with purpose.", "length() size, charAt(i) ith char, substring() part of the text, indexOf() first position."),
    VE("s == t vs s.equals(t)?", "== compares references (same object?); equals() compares the actual text - always use equals for strings."),
    VE("What does s.substring(0, 3) return for \"GTU\"?", "GTU - characters 0, 1 and 2; the end index is excluded."),
    VE("What do split() and join() do?", "split(\",\") breaks a string into a String[] around the separator; String.join(\"-\", arr) glues the pieces back."),
    VE("What is a wrapper class? Name all eight.", "The object twin of a primitive: Byte, Short, Integer, Long, Float, Double, Character, Boolean."),
    VE("What are autoboxing and unboxing?", "Automatic conversions since Java 5: primitive -> wrapper (Integer o = 42) and wrapper -> primitive (int m = o)."),
    VE("Why are wrapper classes needed?", "Collections store objects only, and wrappers supply parsing helpers like Integer.parseInt()."),
    VE("What happens on unboxing a null?", "A NullPointerException is thrown - wrapper objects may be null unlike primitives."),
    VE("How do you read a whole line and an integer with Scanner?", "new Scanner(System.in); nextLine() reads a line, nextInt() reads an int."),
    VE("What is the nextLine() pitfall after nextInt()?", "nextInt() leaves the pressed Enter; the next nextLine() reads it as an empty line. Use one extra nextLine() to consume it."),
    VE("What is next() vs nextLine()?", "next() reads one space-separated token; nextLine() reads the whole line."),
    VE("What are command line arguments?", "Strings written after the run command: java Main 15 27 -> args = {\"15\",\"27\"}; converted with parseInt."),
    VE("What is garbage collection?", "The automatic freeing of heap memory holding objects that no reference can reach; there is no delete keyword."),
    VE("What does System.gc() guarantee?", "Nothing - it only requests collection; the JVM decides the time and order."),
    VE("What is finalize()?", "A method the JVM calls on an object just before destroying it (last clean-up); deprecated now - try-with-resources is preferred."),
    VE("Why is memory management in Java called automatic?", "Because objects are created with new and destroyed by the garbage collector - the programmer never frees memory by hand."),
    VE("Combine: how do encapsulation, getter/setter and private relate in BankAcc?", "bal is private (hidden), deposit() checks amt > 0 (controlled change), getBal() is the only way to read it - that is encapsulation in practice."),
]

assert len(_VIVA) == 46
VIVA = [
    G("OOP Principles, Class, Object", _VIVA[0:9]),
    G("Constructors, this, static", _VIVA[9:22]),
    G("Access Modifiers and Methods", _VIVA[22:27]),
    G("Strings and Wrappers", _VIVA[27:37]),
    G("Input and Garbage Collection", _VIVA[37:46]),
]

EXAM_QS = [
    XE("Explain the four principles of OOP with real-world examples.", 6),
    XE("Define class and object. Explain with a Student class program. (Practical 4)", 4),
    XE("What is a constructor? Explain its types with examples.", 4),
    XE("Differentiate constructor and method.", 3),
    XE("Explain constructor overloading with a program. (Practical 5 part)", 4),
    XE("Explain the this keyword: shadowing and constructor chaining. (Practical 5a)", 4),
    XE("Explain the static keyword: static variable, method and block. (Practical 5b)", 4),
    XE("Explain the four access modifiers of Java.", 4),
    XE("Explain encapsulation using a bank account with getters and setters.", 4),
    XE("What is method overloading? Write a program for it. (Practical 6)", 4),
    XE("Explain any five String methods with examples. (Practical 7)", 4),
    XE("Why should strings be compared with equals() and not ==?", 3),
    XE("Explain wrapper classes, autoboxing and unboxing with examples.", 4),
    XE("Explain Scanner class input with a program. (Practical 8)", 4),
    XE("Explain command line arguments with an example.", 3),
    XE("Explain garbage collection and the finalize() method.", 4),
]
