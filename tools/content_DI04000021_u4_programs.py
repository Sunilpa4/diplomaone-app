"""DI04000021 Unit 4 - solved Java programs (exceptions, collections).
All outputs genuine. Practicals 13-14."""
from java_content import JP

PROGRAMS = [

JP("jv4_1", "Types of errors: compile-time, runtime, logical", '''
class Main {
  public static void main(String[] a) {
    // 1) COMPILE-TIME: javac stops it:
    //    int n = "ten";  // won't compile
    //    (String cannot hold an int value)

    // 2) LOGICAL error: code runs but the
    //    answer is wrong
    int sum = 10 + 20;
    double avg = sum / 2 + 1;  // wanted +10
    String w = "avg (wrong) = " + avg;
    System.out.println(w);
    // bug: / applied before +; meant +10

    // 3) RUNTIME error: compiles fine but
    //    crashes while running (see next)
    String r = "logic bugs compile + run";
    System.out.println(r);
  }
}
''', expl="""
<p>The three species of program error:</p>
<ul><li><b>Compile-time</b>: grammar or type mistakes; <code>javac</code> refuses to build the .class file.</li>
<li><b>Runtime</b> (an <b>exception</b>): compiles fine, crashes while running - divide by zero, null reference.</li>
<li><b>Logical</b>: runs perfectly and prints the WRONG answer - the hardest kind, no one flags it for you.</li></ul>
<p>The logical bug above: <code>sum / 2</code> happens before <code>+ 1</code>, so 16.0 prints where +10 was intended. Only careful testing catches such bugs.</p>
"""),

JP("jv4_2", "Division by zero without try-catch (program crashes)", '''
class Main {
  public static void main(String[] a) {
    int marks = 90;
    int subjects = 0;   // division by zero!

    System.out.println("before the crash");
    double avg = marks / subjects;
    // JVM throws ArithmeticException here
    System.out.println("avg = " + avg);

    // this line never runs:
    System.out.println("after the crash");
  }
}
''', expl="""
<p>This is what an <b>unhandled exception</b> does: the program stops dead at the line <code>marks / subjects</code>.</p>
<ul><li>The JVM creates an <b>ArithmeticException</b> object and looks for a handler - finds none.</li>
<li>So it prints the <b>stack trace</b> (<i>Exception in thread "main"</i>, the exception name, and the exact line number) and terminates.</li>
<li>The last println never executes - proof that the crash killed the rest of main().</li></ul>
<p>The next program catches exactly this politely, with try-catch.</p>
"""),

JP("jv4_3", "try-catch: handling ArithmeticException politely", '''
class Main {
  public static void main(String[] a) {
    int marks = 90;
    int subjects = 0;

    try {
      String note = "try: computing...";
      System.out.println(note);
      double avg = marks / subjects;  // boom
      System.out.println("avg = " + avg);
    } catch (ArithmeticException e) {
      String m = "caught: "+e.getMessage();
      System.out.println(m);
      subjects = 1;  // recover politely
    }

    String go = "program continues...";
    System.out.println(go);
    double avg = marks / subjects;
    System.out.println("avg = " + avg);
  }
}
''', expl="""
<p><b>Practical 13 (part 1).</b> Put risky code in <code>try</code>, put recovery in <code>catch</code>:</p>
<ul><li>As soon as the division throws, control <b>jumps</b> to the matching catch - <code>e</code> is the exception object.</li>
<li><code>e.getMessage()</code> gives the detail: <code>/ by zero</code>.</li>
<li>After catch finishes, normal flow resumes - the program ends gracefully instead of crashing.</li></ul>
"""),

JP("jv4_4", "try-catch: NullPointerException", '''
class Main {
  public static void main(String[] a) {
    String name = null;  // no object at all!

    try {
      String t = "try to read length...";
      System.out.println(t);
      int n = name.length();   // NPE!
      System.out.println("length = " + n);
    } catch (NullPointerException e) {
      String m = "caught a null pointer!";
      System.out.println(m);
      String w = "name was never set";
      System.out.println(w);
    }

    String end = "still running fine";
    System.out.println(end);
  }
}
''', expl="""
<p><b>Practical 13 (part 2).</b> A reference holding <code>null</code> points to <i>nothing</i> - calling a method on it throws <b>NullPointerException</b>.</p>
<ul><li>Fix it by catching, or better: check <code>if (name != null)</code> before touching it.</li>
<li>NPE is the most common exception in real Java code; careful design avoids returning null at all.</li></ul>
"""),

JP("jv4_5", "try-catch: stepping past the end of an array", '''
class Main {
  public static void main(String[] a) {
    int[] marks = {80, 75, 90};  // indexes 0..2

    try {
      for (int i = 0; i <= 3; i++) {  // 3 is bad
        String row = "marks[" + i + "]";
        row += " = " + marks[i];
        System.out.println(row);
      }
    } catch (RuntimeException e) {
      String t = e.getClass()
          .getSimpleName();
      System.out.println("caught: " + t);
      System.out.println(e.getMessage());
    }
    System.out.println("loop recovered");
  }
}
''', expl="""
<p>Arrays know their own size; stepping outside <code>0 .. length-1</code> throws <b>ArrayIndexOutOfBoundsException</b>.</p>
<ul><li>Here <code>i &lt;= 3</code> is the classic off-by-one slip - the report names it exactly (see the printed class name and message).</li>
<li>We caught the parent <code>RuntimeException</code> and asked the object its own type with <code>getSimpleName()</code> - proof that this exception is part of the runtime family.</li>
<li>Simply writing <code>i &lt; marks.length</code> makes this exception impossible.</li></ul>
"""),

JP("jv4_6", "Multiple catch blocks: first match wins", '''
class Main {
  public static void main(String[] a) {
    String small = "5";         // parseable
    String big = "99999999999";  // boom

    try {
      int n = Integer.parseInt(small);
      System.out.println("small = " + n);
      n = Integer.parseInt(big);
      System.out.println("big = " + n);
    } catch (NumberFormatException e) {
      String m = "not a valid int value";
      System.out.println(m);
    } catch (ArithmeticException e) {
      String m = "math trouble";
      System.out.println(m);
    } catch (Exception e) {  // parent last
      String m = "other: " + e.getMessage();
      System.out.println(m);
    }
    String done = "done either way";
    System.out.println(done);
  }
}
''', expl="""
<p>One try may have <b>several catch blocks</b>; the JVM walks them top-down and runs the <b>first</b> whose type fits.</p>
<ul><li><code>parseInt("99999999999")</code> overflows int and throws NumberFormatException, so the first catch runs.</li>
<li>Only ONE catch block runs per exception.</li>
<li>Order matters: specific children first, general <code>Exception</code> last - a parent catch written first would swallow everything (and javac rejects unreachable catches).</li></ul>
"""),

JP("jv4_7", "finally: runs whether or not an exception occurs", '''
class Main {
  static void bank(int amount) {
    try {
      System.out.println("open vault");
      if (amount < 0) {
        int r = amount / 0;  // fault!
        System.out.println(r);
      }
      String p = "pay out " + amount;
      System.out.println(p);
    } catch (ArithmeticException e) {
      String t = "transaction failed";
      System.out.println(t);
    } finally {
      String c = "close vault (always!)";
      System.out.println(c);
    }
  }
  public static void main(String[] a) {
    bank(500);
    System.out.println("---------");
    bank(-1);
  }
}
''', expl="""
<p><b>finally</b> is the "whatever happens" block - it runs:</p>
<ul><li>when the try completes normally (first call),</li>
<li>when an exception is caught (second call),</li>
<li>even when an exception is NOT caught (right before the crash).</li></ul>
<p>That is why it is the correct place for cleanup: closing files, releasing locks, logging out. Notice how "close vault" prints in <i>both</i> runs of bank().</p>
"""),

JP("jv4_8", "throw: raising an exception yourself", '''
class Main {
  static void checkAge(int age) {
    if (age < 18) {
      throw new IllegalArgumentException(
        "age " + age + " is below 18");
      // a line after throw never runs
    }
    String ok = "voter card approved";
    System.out.println(ok);
  }

  public static void main(String[] a) {
    try {
      checkAge(21);
      checkAge(15);  // this one explodes
      checkAge(40);  // never reached
    } catch (IllegalArgumentException e) {
      System.out.println("rejected:");
      System.out.println(e.getMessage());
    }
    String end = "registration desk closed";
    System.out.println(end);
  }
}
''', expl="""
<p><code>throw</code> lets <b>your own code</b> raise an exception object:</p>
<ul><li>Syntax: <code>throw new ExceptionType(message)</code> - one single object, created on the spot.</li>
<li>The rest of the method is skipped; the nearest matching catch (here, in main) takes over.</li>
<li>Use it to reject impossible input - classic for validation rules like a minimum voting age.</li></ul>
<p>Practical 13 shape: a built-in exception type raised deliberately, with our own message, handled by try-catch.</p>
"""),

JP("jv4_9", "throws: declaring that a method may fail", '''
class Main {
  // promises it may pause (checked)
  static void nap(int ms)
      throws InterruptedException {
    String s = "sleeping " + ms + "ms...";
    System.out.println(s);
    Thread.sleep(ms);  // may throw
    System.out.println("awake!");
  }

  public static void main(String[] a)
      throws InterruptedException {
    nap(300);
    nap(100);
    String end = "end of a quiet day";
    System.out.println(end);
  }
}
''', expl="""
<p><code>throws</code> belongs to a method's <b>signature</b>: it advertises "calling me might raise this checked exception - handle it or pass it on".</p>
<ul><li><code>Thread.sleep()</code> is declared <code>throws InterruptedException</code>, so every caller must catch it or re-declare throws.</li>
<li>Here we choose to declare it again on main() - the JVM tolerates that.</li>
<li><b>throw</b> = actually raise; <b>throws</b> = merely warn in the header. They are NOT interchangeable.</li></ul>
"""),

JP("jv4_10", "throw + throws together in a real method", '''
class Main {
  static void withdraw(int bal, int amt)
      throws IllegalStateException {
    if (amt > bal) {
      throw new IllegalStateException(
        "not enough balance: " + bal);
    }
    String p = "paid out " + amt;
    System.out.println(p);
  }

  public static void main(String[] a) {
    int balance = 2000;
    try {
      withdraw(balance, 1500);  // fine
      withdraw(balance, 3000);  // too much!
    } catch (IllegalStateException e) {
      System.out.println("ATM error:");
      System.out.println(e.getMessage());
    }
    String end = "thank you, visit again";
    System.out.println(end);
  }
}
''', expl="""
<p>The typical business-method pairing:</p>
<ul><li><code>throws IllegalStateException</code> in the header warns callers "this may fail";</li>
<li><code>throw new ...</code> inside enforces the rule (amount must fit the balance);</li>
<li>The caller decides politely: catch the fault and show a human message instead of crashing the ATM screen.</li></ul>
<p>IllegalStateException is unchecked; a checked exception would have FORCED the caller to handle it at compile time.</p>
"""),

JP("jv4_11", "Catch order: subclass before the superclass", '''
class Main {
  public static void main(String[] a) {
    Object o = null;
    try {
      String s = (String) o;  // null cast ok
      s.length();   // NPE is thrown
    } catch (NullPointerException e) {
      String m1 = "1st: specific - NPE";
      System.out.println(m1);
    } catch (RuntimeException e) {
      String m2 = "2nd: parent runtime";
      System.out.println(m2);
    } catch (Exception e) {
      String m3 = "3rd: grandparent";
      System.out.println(m3);
    }
    String tail = "narrow ones first!";
    System.out.println(tail);
  }
}
''', expl="""
<p>Catch blocks are matched <b>top to bottom by type</b>:</p>
<ul><li>The thrown object is a NullPointerException, so the <b>first</b> catch prints - not the parent RuntimeException one below it.</li>
<li>Had we written <code>catch (Exception e)</code> first, the child catches would be unreachable and javac would complain.</li>
<li>Rule of thumb: go <b>up the hierarchy as you go down the catch list</b> - most specific first, most general last.</li></ul>
"""),

JP("jv4_12", "ArrayList: add, remove, search", '''
import java.util.ArrayList;

class Main {
  public static void main(String[] a) {
    ArrayList<String> team =
        new ArrayList<>();

    team.add("Meera");      // append
    team.add("Ravi");
    team.add("Farhan");
    team.add(1, "Zoya");  // insert at index
    System.out.println("team = " + team);
    int sz = team.size();
    System.out.println("size = " + sz);

    team.remove("Farhan");  // by value
    team.remove(0);         // by index
    String now = "after remove: " + team;
    System.out.println(now);

    boolean has = team.contains("Zoya");
    System.out.println("has Zoya? " + has);
    int pos = team.indexOf("Ravi");
    String ri = "Ravi at index " + pos;
    System.out.println(ri);
    String f = "first = " + team.get(0);
    System.out.println(f);
  }
}
''', expl="""
<p><b>Practical 14 (part A).</b> <code>ArrayList&lt;String&gt;</code> is the growable array of the Collections framework - the diamond names the element type.</p>
<ul><li><code>add()</code> grows the list; the two-argument add inserts in the middle.</li>
<li><code>remove()</code> works by value or by index; <code>size()</code> replaces array <code>length</code>.</li>
<li>Search trio: <code>contains()</code> answers yes/no, <code>indexOf()</code> answers where, <code>get(i)</code> fetches.</li>
<li>Printing the list shows <code>[a, b, c]</code> - ArrayList brings its own friendly toString.</li></ul>
"""),

JP("jv4_13", "ArrayList traversal: for-each loop in action", '''
import java.util.ArrayList;

class Main {
  public static void main(String[] a) {
    ArrayList<Integer> marks =
        new ArrayList<>();
    marks.add(82);  // boxed to Integer
    marks.add(95);
    marks.add(67);
    marks.add(88);

    String h1 = "--- index loop ---";
    System.out.println(h1);
    for (int k = 0; k < marks.size(); k++) {
      String row = k + ": " + marks.get(k);
      System.out.println(row);
    }

    String h2 = "--- for-each loop ---";
    System.out.println(h2);
    int total = 0;
    for (int m : marks) {   // clean + safe
      total += m;           // auto-unboxing
    }
    double avg = total * 1.0 / marks.size();
    System.out.println("total = " + total);
    System.out.println("average = " + avg);
  }
}
''', expl="""
<p><b>Practical 14 (part B).</b> Two traversal styles:</p>
<ul><li>The classic counting loop gives the <b>index</b> k - useful when position matters.</li>
<li>The <b>for-each</b> loop <code>for (int m : marks)</code> reads naturally ("for each mark m in marks") and can never walk past the end.</li>
<li>Autoboxing quietly wraps <code>int</code> into <code>Integer</code> on add and unwraps on use - you saw it in Unit 2; here the glove work pays off.</li></ul>
"""),

JP("jv4_14", "HashSet: uniqueness and fast membership", '''
import java.util.HashSet;
import java.util.ArrayList;

class Main {
  public static void main(String[] a) {
    HashSet<String> tags =
        new HashSet<>();
    tags.add("java");
    tags.add("exam");
    tags.add("java");  // dup ignored
    tags.add("coding");
    System.out.println("tags = " + tags);
    int sz = tags.size();
    System.out.println("size = " + sz);

    boolean hasExam = tags.contains("exam");
    String h = "has exam? " + hasExam;
    System.out.println(h);
    tags.remove("coding");
    String now = "after remove: " + tags;
    System.out.println(now);

    String h2 = "--- each unique tag ---";
    System.out.println(h2);
    for (String t : tags) {
      System.out.println("* " + t);
    }

    ArrayList<String> likes =
        new ArrayList<>();
    likes.add("tea"); likes.add("tea");
    String d = "list dup ok: " + likes;
    System.out.println(d);
  }
}
''', expl="""
<p><b>Practical 14 (part C).</b> HashSet = a bag that refuses duplicates:</p>
<ul><li>Four adds, one repeated "java" - <code>size()</code> stays honest at 3.</li>
<li><code>contains()</code> on a HashSet is a hash-table lookup: very fast even with thousands of members.</li>
<li>Traversal uses the same for-each loop as a list, but the <b>order is not insertion order</b> - it follows the hash table, so never rely on it.</li>
<li>Compare the ArrayList at the end: lists happily keep duplicates; sets do not. Use a set for unique tags/friends/roll numbers and a list when order and duplicates matter.</li></ul>
"""),
]
