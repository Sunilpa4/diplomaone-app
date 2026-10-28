"""DI04000021 Unit 2 - solved Java programs (OOP concepts). All outputs genuine. Practicals 4-8."""
from java_content import JP

PROGRAMS = [

JP("jv2_1", "A Student class: fields, methods, object creation", '''
class Student {              // class = blueprint
  int roll;                  // fields (member variables)
  String name;
  void setData(int r, String n) {   // method
    roll = r;
    name = n;
  }
  void display() {
    System.out.println(roll + " : " + name);
  }
}

class Main {
  public static void main(String[] a) {
    Student s1 = new Student();     // 1st object
    s1.setData(1, "Asha");
    Student s2 = new Student();     // 2nd object
    s2.setData(2, "Bhavesh");
    s1.display();                   // each object keeps
    s2.display();                   // its own values
  }
}
''', expl="""
<p><b>Practical 4.</b> A <b>class</b> is a blueprint; an <b>object</b> is a real copy made from it with <code>new</code>.</p>
<ul><li><b>Fields</b> (roll, name) store data; <b>methods</b> (setData, display) define behaviour.</li>
<li>Two objects hold independent values: setting s2 does not change s1.</li>
<li>Methods are called on an object with a dot: <code>s1.display();</code>.</li></ul>
"""),

JP("jv2_2", "Methods: parameters, return values and calling", '''
class Main {
  // method with two parameters, returns int
  static int add(int x, int y) {
    return x + y;            // sends result back
  }

  static void greet(String n) {     // returns nothing
    System.out.println("Hi " + n);
  }

  static double average(int a, int b) {
    return (a + b) / 2.0;
  }

  public static void main(String[] args) {
    int s = add(7, 5);              // call + store
    System.out.println("sum = " + s);
    greet("Sunil");
    double av = average(70, 90);
    System.out.println("avg = " + av);
  }
}
''', expl="""
<ul><li>A <b>method definition</b> has: return type, name, parameter list, body.</li>
<li><b>Method calling</b> copies values into the parameters; <code>return</code> sends one value back to the caller.</li>
<li><code>void</code> methods (greet) perform an action but return nothing.</li>
<li>Methods inside the same class as main() are called plain (<code>add(7, 5)</code>) because both are <code>static</code>.</li></ul>
"""),

JP("jv2_3", "Default and parameterized constructors with 'this'", '''
class Book {
  String title;
  double price;

  Book() {                       // default constructor
    title = "Java";
    price = 0;
  }

  Book(String title, double price) {
    this.title = title;          // this.field = parameter
    this.price = price;
  }

  void show() {
    String row = title + " Rs. " + price;
    System.out.println(row);
  }
}

class Main {
  public static void main(String[] a) {
    Book b1 = new Book();                    // default
    Book b2 = new Book("OOP in Java", 299);  // parameterized
    b1.show();
    b2.show();
  }
}
''', expl="""
<p><b>Practical 5(a).</b> A <b>constructor</b> initializes the new object. It has the same name as the class and no return type (not even void).</p>
<ul><li>The <b>default constructor</b> takes no arguments; the <b>parameterized constructor</b> receives values.</li>
<li><b>this</b> distinguishes the field (<code>this.title</code>) from the parameter (<code>title</code>) when both have the same name.</li>
<li>Which constructor runs is decided by the argument list of <code>new</code>.</li></ul>
"""),

JP("jv2_4", "Constructor overloading", '''
class Account {
  String name;
  double bal;

  Account() {                         // 1: no args
    name = "Guest";
    bal = 0;
  }
  Account(String name) {              // 2: one arg
    this.name = name;
    bal = 500;
  }
  Account(String name, double bal) {  // 3: two args
    this.name = name;
    this.bal = bal;
  }
  void show() {
    System.out.println(name + " -> " + bal);
  }
}

class Main {
  public static void main(String[] a) {
    Account a1 = new Account();
    Account a2 = new Account("Riya");
    Account a3 = new Account("Amit", 5000);
    a1.show();
    a2.show();
    a3.show();
  }
}
''', expl="""
<ul><li><b>Constructor overloading</b> = several constructors with different parameter lists in one class.</li>
<li>The compiler picks the one whose signature matches the <code>new</code> call.</li>
<li>Gives users flexible ways to create objects with more or less initial data.</li></ul>
"""),

JP("jv2_5", "The 'this' keyword: shadowing and constructor chaining", '''
class Mobile {
  String model;
  double price;

  Mobile(String model) {
    this.model = model;      // field = parameter
    this.price = 9999;
  }
  // this() calls another constructor first
  Mobile(String model, double price) {
    this(model);             // constructor chaining
    this.price = price;
  }
  void update(double price) {
    this.price = price;      // field = parameter
  }
  Mobile bigger(Mobile o) {
    // return the costlier mobile
    return this.price > o.price ? this : o;
  }
  void show() {
    String row = model + " Rs. " + price;
    System.out.println(row);
  }
}

class Main {
  public static void main(String[] a) {
    Mobile m1 = new Mobile("Note 12");
    Mobile m2 = new Mobile("Galaxy", 21249);
    m1.update(14999);
    m1.show();
    m2.show();
    m1.bigger(m2).show();
  }
}
''', expl="""
<ul><li><b>this.field</b> solves <b>shadowing</b>: parameter names normally hide the fields.</li>
<li><b>this(args)</b> calls another constructor of the same class - chaining avoids duplicate code (must be the first statement).</li>
<li><b>this as a value</b> refers to the current object: <code>m1.bigger(m2)</code> returns this (m1) or o (m2), and show() runs on the result.</li></ul>
"""),

JP("jv2_6", "The 'static' keyword: variable, method and block", '''
class Counter {
  static int total = 0;      // ONE copy for all objects
  int id;                    // one copy per object

  static {                   // static block:
    System.out.println("class loading...");  // runs first
  }

  Counter() {
    total++;                 // count every object
    id = total;
  }

  static void report() {     // static method:
    System.out.println("total = " + total);  // no object
  }
}

class Main {
  public static void main(String[] a) {
    new Counter();
    new Counter();
    Counter c = new Counter();
    System.out.println("c.id = " + c.id);
    Counter.report();        // called via class name
    System.out.println(Counter.total);
  }
}
''', expl="""
<p><b>Practical 5(b).</b></p>
<ul><li>A <b>static variable</b> belongs to the class, not to objects: all objects share one <code>total</code>, while each has its own <code>id</code>.</li>
<li>A <b>static block</b> runs once when the class is loaded - before main() starts.</li>
<li>A <b>static method</b> can be called with the class name (<code>Counter.report()</code>) and can touch only static members directly.</li>
<li>Static classes (nested) group related helper classes - seen again in Unit 5.</li></ul>
"""),

JP("jv2_7", "Access modifiers with getters and setters", '''
class BankAcc {
  private double bal;        // hidden from outside
  String owner;              // default: same package
  public String bank = "SBI";

  public void deposit(double amt) {
    if (amt > 0)
      bal = bal + amt;       // insiders may change it
  }
  public double getBal() {   // controlled reading
    return bal;
  }
}

class Main {
  public static void main(String[] a) {
    BankAcc ac = new BankAcc();
    ac.owner = "Sunil";
    ac.deposit(1200);
    ac.deposit(-500);        // rejected by the check
    // ac.bal = 99999;
    // ^ compile error: bal is private
    String ow = ac.owner;
    double bl = ac.getBal();
    System.out.println("owner = " + ow);
    System.out.println("bank = " + ac.bank);
    System.out.println("balance = " + bl);
  }
}
''', expl="""
<ul><li><b>private</b> - only inside the same class; <b>default</b> (no keyword) - anywhere in the same package; <b>protected</b> - package + subclasses (Unit 3); <b>public</b> - everywhere.</li>
<li>Hiding <code>bal</code> and giving public <b>getters/setters</b> is <b>encapsulation</b>: the check <code>if (amt > 0)</code> prevents nonsense changes.</li>
<li>Try uncommenting <code>ac.bal = 99999;</code> - the compiler itself stops you.</li></ul>
"""),

JP("jv2_8", "Method overloading", '''
class Calc {
  // same name, different parameter lists
  int add(int a, int b) {
    return a + b;
  }
  int add(int a, int b, int c) {
    return a + b + c;
  }
  double add(double a, double b) {
    return a + b;
  }
}

class Main {
  public static void main(String[] x) {
    Calc c = new Calc();
    System.out.println(c.add(2, 3));
    System.out.println(c.add(2, 3, 4));
    System.out.println(c.add(2.5, 3.5));
  }
}
''', expl="""
<p><b>Practical 6.</b></p>
<ul><li><b>Method overloading</b>: several methods share one name but differ in the <b>number or type of parameters</b> - the compiler chooses by matching the call.</li>
<li>Changing only the return type is NOT enough; the parameter list must differ.</li>
<li>This is <b>compile-time (static) polymorphism</b> - the decision is made at compile time.</li></ul>
"""),

JP("jv2_9", "Common String methods", '''
class Main {
  public static void main(String[] a) {
    String s = "GTU Diploma";

    System.out.println(s.length());        // 11
    System.out.println(s.charAt(4));       // 'D'
    System.out.println(s.substring(4));    // Diploma
    System.out.println(s.substring(0, 3)); // GTU
    System.out.println(s.toUpperCase());
    System.out.println(s.toLowerCase());

    System.out.println(s.indexOf("Dip"));  // 4
    System.out.println(s.contains("oma")); // true
    System.out.println(s.startsWith("GT"));
    System.out.println("  hi  ".trim());   // hi
    System.out.println(s.concat(" 2026"));
    System.out.println(s.replace('D','d'));

    String t = "GTU Diploma";
    System.out.println(s.equals(t));       // true
    System.out.println(s == t);            // ?
  }
}
''', expl="""
<p><b>Practical 7.</b> String is immutable: every method returns a NEW string, <code>s</code> itself never changes.</p>
<ul><li><code>substring(4)</code> = from index 4 to the end; <code>substring(0,3)</code> = 0,1,2 (end excluded).</li>
<li><code>indexOf</code> gives the first position, or -1 if absent.</li>
<li><code>equals()</code> compares text; <code>==</code> compares references - two strings with the same text may or may not share memory (here both literals do - see output).</li></ul>
"""),

JP("jv2_10", "String joining, splitting and an array of strings", '''
class Main {
  public static void main(String[] a) {
    String line = "red,green,blue";
    String[] parts = line.split(",");
    for (int i = 0; i < parts.length; i++) {
      String p = parts[i];
      System.out.println(i + " : " + p);
    }

    String j = String.join(" - ", parts);
    System.out.println(j);

    // char array <-> string
    char[] ch = "JAVA".toCharArray();
    for (char c : ch)
      System.out.print(c + " ");
    System.out.println();
    String back = new String(ch);
    System.out.println(back);
  }
}
''', expl="""
<ul><li><code>split(",")</code> breaks a string around the separator and returns a <b>String[]</b> array.</li>
<li><code>String.join(" - ", parts)</code> glues array pieces with a separator.</li>
<li><code>toCharArray()</code> gives the characters as a char[]; <code>new String(ch)</code> builds a string back.</li>
<li>These three appear constantly in data-entry and CSV-style programs.</li></ul>
"""),

JP("jv2_11", "Wrapper classes: Integer, Double, parsing", '''
class Main {
  public static void main(String[] a) {
    // each primitive type has a wrapper
    Integer iObj = Integer.valueOf(42);
    Double dObj = Double.valueOf(7.5);
    Character cObj = Character.valueOf('A');
    Boolean bObj = Boolean.valueOf(true);

    System.out.println(iObj);
    String line = dObj + " " + cObj;
    System.out.println(line + " " + bObj);

    // string -> number with parse methods
    int n = Integer.parseInt("153");
    double d = Double.parseDouble("4.5");
    System.out.println(n + 1);       // 154, real math
    System.out.println(d * 2);

    // useful constants and helpers
    System.out.println(Integer.MAX_VALUE);
    System.out.println(Integer.MIN_VALUE);
    String bin = Integer.toBinaryString(10);
    System.out.println(bin);
  }
}
''', expl="""
<ul><li><b>Wrapper classes</b> box each primitive into an object: Byte, Short, Integer, Long, Float, Double, Character, Boolean.</li>
<li>Objects are needed because collections (Unit 4) store only objects, and wrapper classes carry helpers like <code>parseInt</code> and <code>MAX_VALUE</code>.</li>
<li><code>Integer.parseInt("153")</code> converts text entered by a user into a real number - without it "153" + 1 would be "1531".</li></ul>
"""),

JP("jv2_12", "Scanner input + autoboxing and unboxing", '''
import java.util.Scanner;

class Main {
  public static void main(String[] arg) {
    Scanner sc = new Scanner(System.in);
    System.out.print("Enter name: ");
    String name = sc.nextLine();
    System.out.print("Enter marks (int): ");
    int marks = sc.nextInt();
    System.out.print("Enter CGPA: ");
    double cg = sc.nextDouble();

    // autoboxing: primitive -> wrapper
    Integer mObj = marks;
    Double cgObj = cg;

    // unboxing: wrapper -> primitive (auto)
    int m2 = mObj;
    double d2 = cgObj;

    System.out.println("name: " + name);
    int m3 = m2 + 1;
    System.out.println("box marks=" + mObj);
    System.out.println("marks int = " + m3);
    System.out.println("box CGPA=" + cgObj);
    System.out.println("CGPA unbox=" + d2);
  }
}
''', inputs=("Sunil Patel", "452", "8.25"), expl="""
<p><b>Practical 8.</b></p>
<ul><li><b>Scanner</b> (java.util) reads user input: <code>nextLine()</code> text, <code>nextInt()</code> whole numbers, <code>nextDouble()</code> decimals - the program waits for you to type.</li>
<li><b>Autoboxing</b>: Java automatically wraps a primitive into its wrapper object (<code>Integer mObj = marks;</code>).</li>
<li><b>Unboxing</b>: the opposite (<code>int m2 = mObj;</code>), done automatically too. Before Java 5 you had to write <code>Integer.valueOf()</code> / <code>intValue()</code> by hand.</li></ul>
<p>Try it live: the output shows what the program printed after reading name = Sunil Patel, marks = 452, CGPA = 8.25.</p>
"""),

JP("jv2_13", "Scanner: mixed input and nextLine pitfalls", '''
import java.util.Scanner;

class Main {
  public static void main(String[] ar) {
    Scanner sc = new Scanner(System.in);
    System.out.print("Age: ");
    int age = sc.nextInt();
    sc.nextLine();   // eat the leftover new line
    System.out.print("Full name: ");
    String nm = sc.nextLine();
    System.out.print("Single token: ");
    String tk = sc.next();
    System.out.println("age = " + age);
    System.out.println("name = " + nm);
    System.out.println("token = " + tk);
  }
}
''', inputs=("19", "Priya Sharma", "hello extra"), expl="""
<ul><li><code>nextInt()</code> reads only the number; the ENTER you pressed stays in the queue.</li>
<li>The extra <code>sc.nextLine()</code> consumes that leftover ENTER - without it, the following <code>nextLine()</code> would read an empty line and the program would seem to "skip" the name input.</li>
<li><code>next()</code> reads one token (stops at space): "hello extra" gives back only "hello".</li></ul>
"""),

JP("jv2_14", "Command line arguments (String[] args)", '''
class Main {
  public static void main(String[] args) {
    int n = args.length;
    System.out.println("count = " + n);
    for (int i = 0; i < args.length; i++) {
      String ar = args[i];
      System.out.println(i + " : " + ar);
    }

    if (args.length >= 2) {
      int x = Integer.parseInt(args[0]);
      int y = Integer.parseInt(args[1]);
      int sm = x + y;
      System.out.println("sum = " + sm);
    }
  }
}
''', args=("15", "27"), expl="""
<ul><li>Everything typed after <code>java Main ...</code> lands inside <code>args</code> as <b>strings</b>.</li>
<li>This run used <code>java Main 15 27</code> - see both values and their sum in the output window.</li>
<li>Arguments reach the program without any <code>Scanner</code>; parse with <code>Integer.parseInt</code> for numbers.</li>
<li>Great for small tools where input stays fixed per run.</li></ul>
"""),

JP("jv2_15", "Garbage collection and the finalize() method", '''
class Main {
  static void drop(String n) {
    Item it = new Item(n);
    it = null;
    System.gc();              // ask the collector
    System.runFinalization();
    try {
      Thread.sleep(300);
    } catch (Exception e) { }
  }
  public static void main(String[] a) {
    drop("pen");
    drop("book");
    drop("bag");
    System.out.println("main ends");
  }
}
class Item {
  String n;
  Item(String n) { this.n = n; }
  // finalize() runs before the
  // object is destroyed
  protected void finalize() {
    System.out.println("collecting " + n);
  }
}
''', expl="""
<ul><li>Java's <b>garbage collector (GC)</b> frees memory of objects that have no reference left - exactly like <code>it</code> after <code>it = null;</code>.</li>
<li><b>finalize()</b> is called by the JVM on an object <b>just before</b> it is destroyed - a last chance to clean up (e.g. close a file). Note it is deprecated in modern Java; modern code uses try-with-resources instead (Unit 5).</li>
<li><code>System.gc()</code> only <b>requests</b> collection; the order and timing belong to the JVM, never to you.</li>
<li>The output shows each item being collected right after it becomes unreachable.</li></ul>
"""),
]
