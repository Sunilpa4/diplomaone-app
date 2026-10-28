"""DI04000021 Unit 5 - solved Java programs (modern features, AI intro).
All outputs genuine (JDK 11: Java 7/8/10/11 features run; newer ones are prose).
Practical 15."""
from java_content import JP

PROGRAMS = [

JP("jv5_1", "try-with-resources: self-closing Scanner (Java 7)", '''
import java.util.Scanner;

class Main {
  public static void main(String[] a) {
    // wrap a String: no keyboard needed,
    // output stays genuine every run
    try (Scanner sc =
        new Scanner("Meera 95 Ravi 82")) {
      String name = sc.next();
      int marks = sc.nextInt();
      String r1 = name + ": " + marks;
      System.out.println(r1);
      name = sc.next();
      marks = sc.nextInt();
      String r2 = name + ": " + marks;
      System.out.println(r2);
    }
    // sc.close() happened AUTOMATICALLY,
    // even if an exception had occurred
    String m = "scanner closed by itself";
    System.out.println(m);
  }
}
''', expl="""
<p><b>Java 7's try-with-resources</b>: any object declared in the try's parentheses that implements <code>AutoCloseable</code> is closed automatically when the block ends - catch, crash or clean finish.</p>
<ul><li>Compare with Unit 4: no finally needed purely for closing - the JVM writes it for you.</li>
<li>Several resources can share one try, separated by semicolons.</li>
<li>Works with files, sockets, database connections - everything closable.</li></ul>
"""),

JP("jv5_2", "Java 7 tote bag: switch on String, diamond, multi-catch", '''
import java.util.ArrayList;

class Main {
  static String grade(String day) {
    switch (day) {   // String since Java 7
      case "Monday": return "fresh start";
      case "Friday": return "weekend!";
      default: return "regular day";
    }
  }

  public static void main(String[] a) {
    // diamond <>: type from the left
    ArrayList<String> seen =
        new ArrayList<>();
    seen.add(grade("Friday"));
    seen.add(grade("Wednesday"));
    try {
      String s = null;
      s.length();            // NPE test
      int r = 5 / 0;         // AE test
      System.out.println(r);
    } catch (NullPointerException
        | ArithmeticException e) {
      // Java 7: one handler, two types
      String t = e.getClass()
          .getSimpleName();
      String m = "multi-caught: " + t;
      System.out.println(m);
    }
    System.out.println(seen);
  }
}
''', expl="""
<p>Three Java 7 conveniences in one run:</p>
<ul><li><b>switch on String</b> - before Java 7, only int-like types worked; strings needed if-else ladders.</li>
<li><b>Diamond operator</b> <code>&lt;&gt;</code> - the right side borrows the element type from the left declaration.</li>
<li><b>Multi-catch</b> <code>catch (A | B e)</code> - one handler for several unrelated exception types (no inheritance between them).</li></ul>
<p>All three are compile-time conveniences the JVM never sees - but they make day-to-day Java much shorter.</p>
"""),

JP("jv5_3", "var: type inference for locals (Java 10)", '''
import java.util.ArrayList;

class Main {
  public static void main(String[] a) {
    var name = "Suresh";            // String
    var score = 88.5;               // double
    var subjects = new ArrayList<String>();
    subjects.add("Java");
    subjects.add("Python");

    // the compiler wrote the types, not us:
    String t1 = name.getClass()
        .getSimpleName();
    System.out.println("name is " + t1);
    String t2 = subjects.getClass()
        .getSimpleName();
    System.out.println("subs is " + t2);

    int n = subjects.size();
    for (var i = 0; i < n; i++) {
      String v = subjects.get(i);
      String row = i + ": " + v;
      System.out.println(row);
    }
    for (var s : subjects) {   // works here too
      System.out.println("again: " + s);
    }
  }
}
''', expl="""
<p><code>var</code> (Java 10) tells <b>javac</b>: "read the type from the right side".</p>
<ul><li>It is <b>compile-time inference</b> - the .class file contains the fully real type; Java stays statically typed (a var String can never later hold an int).</li>
<li>Works for local variables, counting loops and for-each - NOT for fields, parameters or return types.</li>
<li>Initialization is compulsory at declaration: <code>var x;</code> alone is a compile error because there is nothing to infer from.</li></ul>
"""),

JP("jv5_4", "Lambda basics: a functional interface implemented inline", '''
interface Speaker {
  void speak();                 // ONE abstract method
}

class Main {
  public static void main(String[] a) {
    // old style: anonymous inner class
    Speaker robot = new Speaker() {
      public void speak() {
        String m2 = "old: I am bulky";
        System.out.println(m2);
      }
    };
    robot.speak();

    // lambda: just the interesting part
    Speaker nano = () -> {
      String m3 = "lambda: just the body!";
      System.out.println(m3);
    };
    nano.speak();

    // stored + called later, like data
    Speaker later = () -> {
      String m4 = "lambdas are values too";
      System.out.println(m4);
    };
    later.speak();
  }
}
''', expl="""
<p>Java 8's headline feature. A <b>functional interface</b> has exactly ONE abstract method, so a lambda can stand in for a whole anonymous class:</p>
<ul><li>Old style: 5 lines of anonymous-class ceremony.</li>
<li>Lambda: <code>() -&gt; body</code> - parameters on the left, behaviour on the right.</li>
<li>Notice the declared type is still <b>Speaker</b>: the lambda IS-A Speaker; javac matches the single method by signature.</li>
<li>When the signature has no parameters, the parentheses are simply empty: <code>() -&gt;</code>.</li></ul>
"""),

JP("jv5_5", "Lambda with parameters: Calculator operations", '''
interface Calc {
  int op(int x, int y);       // shape of operation
}

class Main {
  static void show(String label, Calc c) {
    int r = c.op(7, 3);
    String row = label + " 7,3 -> " + r;
    System.out.println(row);
  }

  public static void main(String[] a) {
    Calc add = (x, y) -> x + y;
    Calc sub = (x, y) -> x - y;
    Calc mul = (x, y) -> x * y;

    show("add:", add);
    show("sub:", sub);
    show("mul:", mul);

    // javac reads the types from Calc
    Calc div = (p, q) -> p / q;
    int d = div.op(7, 3);
    String ds = "div: " + d;
    System.out.println(ds);
  }
}
''', expl="""
<p>When the interface's single method takes parameters, the lambda's left side lists them:</p>
<ul><li><code>(x, y) -&gt; x + y</code> - names only; javac infers int from <code>Calc.op</code>'s signature.</li>
<li>One-expression bodies need neither <code>return</code> nor braces.</li>
<li>Passing a lambda to a method (<code>show("add:", add)</code>) makes code behave like data - the seed of functional style.</li>
<li>Same Calc contract, four different behaviours, zero extra classes.</li></ul>
"""),

JP("jv5_6", "Lambdas with forEach: printing a list", '''
import java.util.ArrayList;

class Main {
  public static void main(String[] a) {
    ArrayList<String> team =
        new ArrayList<>();
    team.add("Meera");
    team.add("Ravi");
    team.add("Farhan");

    String h1 = "--- classic for-each ---";
    System.out.println(h1);
    for (String t : team) {
      System.out.println("* " + t);
    }

    String h2 = "--- forEach + lambda ---";
    System.out.println(h2);
    team.forEach(t ->
        System.out.println("# " + t));

    // block body with curly braces:
    team.forEach(t -> {
      String tag = t.toUpperCase();
      System.out.println("shout: " + tag);
    });
  }
}
''', expl="""
<p><b>Syllabus: print list elements with a lambda.</b> Every collection owns <code>forEach(action)</code>, whose parameter type is the functional interface <code>Consumer&lt;T&gt;</code>:</p>
<ul><li><code>t -&gt; System.out.println(...)</code> feeds each element to println, one by one.</li>
<li>Multiple statements? Wrap the body in braces, exactly like a tiny method.</li>
<li>Classic for-each vs forEach-lambda: same walk; the lambda form composes better with streams (next programs).</li></ul>
"""),

JP("jv5_7", "Practical 15 (A): filter even numbers with streams", '''
import java.util.Arrays;
import java.util.List;

class Main {
  public static void main(String[] a) {
    List<Integer> nums = Arrays.asList(
        5, 12, 7, 20, 33, 40, 2);
    System.out.println("all: " + nums);

    String h = "--- evens only ---";
    System.out.println(h);
    nums.stream()
        .filter(n -> n % 2 == 0)   // keep if true
        .forEach(n -> System.out
            .println("* " + n));
    // ..and how many evens?
    long count = nums.stream()
        .filter(n -> n % 2 == 0)
        .count();
    String ec = "even count = " + count;
    System.out.println(ec);
  }
}
''', expl="""
<p><b>Practical 15 (part A).</b> A <b>stream</b> is a conveyor-belt view of a collection:</p>
<ul><li><code>.stream()</code> opens the belt; <code>.filter(lambda)</code> keeps only elements where the lambda returns true; <code>.forEach(lambda)</code> consumes each survivor.</li>
<li>The original list is never touched - streams calculate views, they do not mutate.</li>
<li>A stream is single-use: for a second pipeline (count) we open a fresh <code>nums.stream()</code>.</li>
<li>Read it aloud: "stream, filter the evens, for each print". Almost English.</li></ul>
"""),

JP("jv5_8", "Practical 15 (B): map strings to uppercase", '''
import java.util.Arrays;
import java.util.List;

class Main {
  public static void main(String[] a) {
    List<String> langs = Arrays.asList(
        "java", "python", "kotlin");
    System.out.println("raw: " + langs);

    String h = "--- UPPERCASE ---";
    System.out.println(h);
    langs.stream()
        .map(s -> s.toUpperCase())  // transform
        .forEach(s -> System.out
            .println("# " + s));

    // original list UNCHANGED:
    String check = "raw is still " + langs;
    System.out.println(check);
  }
}
''', expl="""
<p><b>Practical 15 (part B).</b> <code>map</code> is the transformer station on the belt: each element goes in, the lambda's result comes out.</p>
<ul><li><code>map(s -&gt; s.toUpperCase())</code> turns a Stream of lowercase strings into a Stream of UPPERCASE ones.</li>
<li>filter + map compose: keep only what matches, transform what survives.</li>
<li>The source list stays untouched - see it printed unchanged at the end of the run.</li></ul>
"""),

JP("jv5_9", "Stream pipeline: filter, map, sorted, collect", '''
import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

class Main {
  public static void main(String[] a) {
    List<Integer> marks = Arrays.asList(
        88, 45, 72, 95, 61, 50);

    // pass only, sort, then grade text:
    List<String> report = marks.stream()
        .filter(m -> m >= 50)
        .sorted()                    // ascending
        .map(m -> "pass: " + m)      // int -> String
        .collect(Collectors.toList());

    System.out.println("input : " + marks);
    System.out.println("report: " + report);

    long passes = report.size();
    String pc = "passes = " + passes;
    System.out.println(pc);
    marks.stream()
        .filter(m -> m < 50)
        .forEach(m -> System.out
            .println("fail: " + m));
  }
}
''', expl="""
<p>A full pipeline reads like a query:</p>
<ul><li><b>Source</b> (stream), <b>intermediate</b> steps (filter, sorted, map - each returns a new stream), one <b>terminal</b> step (collect - pours results back into a List).</li>
<li>Intermediate steps are <b>lazy</b>: nothing moves until forEach/collect/count starts the belt.</li>
<li><code>Collectors.toList()</code> (java.util.stream) gathers everything back into a modifiable list.</li>
<li>This is where lambdas become genuinely expressive: complete behaviour passed as parameters to a data pipeline.</li></ul>
"""),

JP("jv5_10", "Runnable and Supplier with lambdas", '''
import java.util.function.Supplier;

class Main {
  public static void main(String[] a) {
    // Runnable = functional interface
    // with void run()
    Runnable banner = () -> {
      String b = "== attendance time ==";
      System.out.println(b);
    };
    Runnable line = () -> {
      String ln = "-----------------";
      System.out.println(ln);
    };
    banner.run();
    line.run();

    // Supplier<T>: values via get()
    Supplier<String> bell =
        () -> "next period: Java lab";
    System.out.println(bell.get());
  }
}
''', expl="""
<p>java.lang and java.util.function ship <b>ready-made functional interfaces</b>:</p>
<ul><li><b>Runnable</b> - <code>void run()</code>, classically used for threads, here simply invoked directly.</li>
<li><b>Supplier&lt;T&gt;</b> - <code>T get()</code>, hands out values on demand.</li>
<li>Others in the family: <b>Consumer&lt;T&gt;</b> (accept - used by forEach), <b>Predicate&lt;T&gt;</b> (test - used by filter), <b>Function&lt;T,R&gt;</b> (apply - used by map).</li>
<li>Recognising these five names unlocks most stream code you will ever meet.</li></ul>
"""),

JP("jv5_11", "java.time: modern dates and times (Java 8)", '''
import java.time.LocalDate;
import java.time.LocalTime;
import java.time.Period;
import java.time.format.DateTimeFormatter;

class Main {
  public static void main(String[] a) {
    LocalDate examDay =
        LocalDate.of(2027, 4, 20);
    LocalDate today = LocalDate.now();
    Period left = Period.between(
        today, examDay);
    String e1 = "exam on " + examDay;
    System.out.println(e1);
    int mo = left.getMonths();
    String r = "months to go: " + mo;
    System.out.println(r);
    String dd = "days: " + left.getDays();
    System.out.println(dd);

    LocalTime lab = LocalTime.of(13, 30);
    DateTimeFormatter fmt =
        DateTimeFormatter.ofPattern(
            "hh:mm a");
    String la = "lab at " + lab.format(fmt);
    System.out.println(la);
    var dw = examDay.getDayOfWeek();
    System.out.println("day: " + dw);
  }
}
''', expl="""
<p>Java 8 replaced the notoriously awkward Date/Calendar with <b>java.time</b>:</p>
<ul><li><code>LocalDate</code> / <code>LocalTime</code> - immutable, thread-safe, no time-zone drama.</li>
<li><code>Period.between()</code> does calendar subtraction properly (months and days, not raw milliseconds).</li>
<li>Formatting via <code>DateTimeFormatter.ofPattern("hh:mm a")</code> - the "a" prints AM/PM.</li>
<li>Run it any day: "months to go" is genuinely computed from the system clock, not hardcoded.</li></ul>
"""),

JP("jv5_12", "Records and pattern matching: exhibit + classic twin", '''
class Main {
  // needs JDK 16+; this sandbox has 11,
  // so the modern syntax stays as a
  // commented exhibit beside a working
  // classic equivalent

  static class Student {        // classic Java
    final int roll;
    final String name;
    Student(int r, String n) {
      roll = r; name = n;
    }
    public String toString() {
      return roll + " : " + name;
    }
  }

  public static void main(String[] a) {
    Student s = new Student(7, "Meera");
    System.out.println(s);
    // JDK 16 one-line equivalent:
    // record Student(int roll,
    //                String name) {}
    // gives ctor, accessors,
    // toString, equals - all free!

    Object o = "pattern demo";
    if (o instanceof String) {  // old style
      String t = (String) o;    // manual cast
      int n = t.length();
      System.out.println("len = " + n);
    }
    // JDK 16: if (o instanceof String t)
    //   -> test AND bind in one step
  }
}
''', expl="""
<p>The post-Java-8 wave keeps shrinking boilerplate:</p>
<ul><li><b>record</b> (16+): a compact immutable data class - one line writes constructor, equals, hashCode, toString and accessors (roll(), name()).</li>
<li><b>Pattern matching for instanceof</b> (16+): <code>if (o instanceof String t)</code> tests AND binds in one breath - the cast disappears.</li>
<li><b>Text blocks</b> (15+): triple-quoted multi-line strings - perfect for JSON and SQL.</li>
<li><b>Sealed classes</b> (17+): a class listing exactly who may extend it.</li></ul>
<p>The sandbox JDK is 11, so the commented lines show the new syntax while the classic equivalent still compiles and runs - exam answers should use the modern forms.</p>
"""),

JP("jv5_13", "Mini AI: nearest-neighbour classifier in pure Java", '''
class Main {
  // tiny dataset: [hours studied, attend %]
  static String[] names = {
      "pass", "pass", "fail",
      "fail", "pass"};
  static int[][] data = {
      {6, 90}, {5, 85}, {1, 40},
      {2, 55}, {7, 92}};

  static String predict(int h, int att) {
    int best = 0;
    double bestDist = 1e9;
    for (int i = 0; i < data.length; i++) {
      int dh = data[i][0] - h;
      int da = data[i][1] - att;
      double d2 = dh * dh + da * da;
      double d = Math.sqrt(d2);
      if (d < bestDist) {
        bestDist = d;
        best = i;
      }
    }
    return names[best];
  }

  public static void main(String[] a) {
    System.out.println("k-NN verdicts:");
    String v1 = predict(6, 88);
    System.out.println("6h/88% -> " + v1);
    String v2 = predict(1, 45);
    System.out.println("1h/45% -> " + v2);
    String v3 = predict(4, 70);
    System.out.println("4h/70% -> " + v3);
  }
}
''', expl="""
<p>A real (tiny) <b>machine-learning</b> idea running in plain Java - the spirit of "Java in AI":</p>
<ul><li>k-Nearest-Neighbour: classify a new student by the CLOSEST known student in (hours, attendance) space - the model simply remembers examples.</li>
<li>This is what enterprise Java + DL4J do at scale: the same distance/classify loop over millions of rows, accelerated on GPUs.</li>
<li>The behaviour comes from <b>data</b> - change the table and the verdicts change with it. That is the definition of ML: rules derived from examples rather than hand-written ifs.</li></ul>
<p>Syllabus link: meaning of AI/ML + Java's role - this program is the smallest honest demonstration of both.</p>
"""),
]
