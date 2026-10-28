"""DI04000021 Unit 4 extras: syntax sheet, viva, exam questions."""
from java_content import SXE, VE, XE, G

SYNTAX = [
    G("try, catch, finally", [
        SXE("try-catch", """try {
  double avg = marks / subjects;
} catch (ArithmeticException e) {
  System.out.println(e.getMessage());
}""",
            "risky code in try, recovery in catch"),
        SXE("multiple catch", """try { ... }
catch (NullPointerException e) { }
catch (RuntimeException e)  { }
catch (Exception e)         { }
// specific first, parent last!""",
            "first matching catch runs; only one"),
        SXE("finally block", """try { ... }
catch (Exception e) { ... }
finally {
  file.close();   // ALWAYS runs
}""",
            "guaranteed cleanup on every path"),
    ]),
    G("throw / throws", [
        SXE("throw", """if (age < 18) {
  throw new IllegalArgumentException(
    "age " + age + " is below 18");
}""",
            "raise one exception object yourself"),
        SXE("throws", """void nap(int ms)
    throws InterruptedException {
  Thread.sleep(ms);
}""",
            "header warning for checked exceptions"),
        SXE("both together", """void withdraw(int bal, int amt)
    throws IllegalStateException {
  if (amt > bal) throw new
    IllegalStateException("no funds");
}""",
            "throws warns callers, throw does it"),
    ]),
    G("Collections", [
        SXE("ArrayList", """ArrayList<String> team =
    new ArrayList<>();
team.add("Meera");
team.add(1, "Zoya");
team.remove("Farhan");
team.contains("Zoya");   // true
team.get(0);  team.size();""",
            "growable list - add, remove, search"),
        SXE("HashSet", """HashSet<String> tags =
    new HashSet<>();
tags.add("java");
tags.add("java");  // ignored
tags.contains("exam");  // fast
tags.remove("coding");""",
            "unique members, no order, no index"),
        SXE("for-each loop", """for (int m : marks) {
  total += m;
}
for (String t : tags) {
  System.out.println(t);
}""",
            "visit every element, no index needed"),
    ]),
]

_VIVA = [
    VE("Name the three types of errors in Java.", "Compile-time (javac stops it), runtime (exception while running) and logical (runs but wrong answer)."),
    VE("Which error type is hardest to find and why?", "Logical - nothing flags it; the program simply produces the wrong output, so only testing reveals it."),
    VE("What is an exception?", "An object the JVM creates at run time describing a failure - it carries the type (e.g. ArithmeticException), a message and the stack trace."),
    VE("What happens to an uncaught exception?", "The JVM prints the stack trace and terminates the program; statements after the throwing line never run."),
    VE("What is the root class of all throwables?", "Throwable - with two children: Error (serious, not caught) and Exception (application-level, catchable)."),
    VE("Checked vs unchecked exceptions?", "Checked: javac forces try-catch or throws (InterruptedException, IOException). Unchecked: RuntimeException children - the compiler stays silent (ArithmeticException, NPE)."),
    VE("List five built-in unchecked exceptions.", "ArithmeticException, NullPointerException, ArrayIndexOutOfBoundsException, NumberFormatException, IllegalArgumentException."),
    VE("What causes a NullPointerException?", "Calling a method or touching a field through a reference that holds null (no object behind it)."),
    VE("What is the message of integer divide by zero?", "The ArithmeticException carries \"/ by zero\"."),
    VE("What do try and catch do?", "try wraps risky statements; catch (Type e) receives the thrown object and runs recovery - one catch handles one exception family."),
    VE("Which statements are skipped when an exception is thrown?", "The rest of the try block; control jumps straight to the matching catch."),
    VE("What does e.getMessage() give?", "The detail string of the exception - for division by zero, \"/ by zero\"."),
    VE("When does finally run?", "Always: after normal try completion, after a caught exception, and even when nothing catches (right before the program dies)."),
    VE("Give two good uses of finally.", "Closing files/connections and releasing locks - cleanup that must happen on every path."),
    VE("Can finally exist without catch?", "Yes - try-finally is legal; the exception still propagates after finally runs. Catching is simpler for beginners."),
    VE("How many catch blocks can follow one try? How many run?", "Any number may follow, but exactly one runs - the first whose type matches."),
    VE("Which catch must come first: Exception or NullPointerException?", "NullPointerException - specific children before parent types, otherwise the parent shadows them (javac error)."),
    VE("How does the JVM pick a catch block?", "Top to bottom, first block whose declared type IS-A supertype of the thrown object."),
    VE("What does throw do, and what follows it?", "It raises an exception object immediately: throw new ArithmeticException(\"msg\"); - a NEW object, so the keyword is followed by a constructor call."),
    VE("Give a real use of throw.", "Input validation - rejecting age below 18 or an overdrawn amount before corrupt data spreads."),
    VE("What does throws declare?", "That a method may raise the listed checked exceptions - a warning in the signature, not an action."),
    VE("Difference between throw and throws?", "throw is a statement in the body that raises one object; throws is a clause in the header listing possible checked exceptions."),
    VE("If a method says throws InterruptedException, what must callers do?", "Either wrap the call in try-catch or declare throws again in their own header."),
    VE("Why is Thread.sleep() special for beginners?", "It declares throws InterruptedException, so callers are FORCED to handle or declare - a convenient checked-exception example."),
    VE("Is IllegalArgumentException checked or unchecked?", "Unchecked (a RuntimeException child) - the compiler does not force handling; good design still catches it."),
    VE("Practical 13: which two exceptions are demonstrated?", "ArithmeticException (divide by zero) and NullPointerException - each caught with try-catch-finally."),
    VE("Why do we need the Collections framework?", "Arrays are fixed-size and low-level; programs need growable containers with add, remove and search built in - ArrayList, HashSet etc. of java.util."),
    VE("Name the root interface and two child interfaces.", "Collection; children List and Set (Queue too)."),
    VE("Which classes implement List and Set for this course?", "ArrayList implements List; HashSet implements Set."),
    VE("Can collections store primitive int directly?", "No - only objects; autoboxing wraps int into Integer automatically when you add it."),
    VE("What does the diamond <> do in ArrayList<String>?", "Names the element type (generics); the compiler then rejects anything that is not a String."),
    VE("How is add(i, e) different from add(e)?", "add(e) appends at the end; add(i, e) inserts at index i, shifting the rest right."),
    VE("Two ways to remove from an ArrayList?", "By value - remove(\"Farhan\"); or by index - remove(0)."),
    VE("Search trio of ArrayList?", "contains(e) -> boolean, indexOf(e) -> position or -1, get(i) -> element."),
    VE("How do you get the length-equivalent of an ArrayList?", "size() - a method, unlike array's length field."),
    VE("What prints when you println an ArrayList?", "A friendly [a, b, c] form - ArrayList implements toString()."),
    VE("What is the for-each loop form?", "for (Type x : collection) { ... } - visits every element in order, no counter needed."),
    VE("Two limitations of for-each?", "No index available inside, and you cannot add/remove elements of the same collection during the loop."),
    VE("What does HashSet do with a duplicate add?", "Silently ignores it - the set keeps one copy; size() does not grow."),
    VE("How does a HashSet find members so fast?", "Hashing: the element's hashCode points to its bucket, so contains() is near-instant instead of a full scan."),
    VE("Does HashSet keep insertion order?", "No - traversal follows the hash table's arrangement; never rely on the order."),
    VE("ArrayList vs HashSet: duplicates and order?", "ArrayList keeps duplicates in insertion order; HashSet forbids duplicates and promises no order."),
    VE("When do you pick a Set over a List?", "When membership must be unique - tags, roll numbers- and order does not matter."),
    VE("Practical 14: which operations are shown on ArrayList and HashSet?", "add, remove, search (contains/indexOf) and traversal with a for-each loop on both collections."),
    VE("Which exception fires if a list is modified during for-each?", "ConcurrentModificationException - the iterator notices the structure changed."),
]

assert len(_VIVA) == 45
VIVA = [
    G("Errors, Hierarchy, try-catch", _VIVA[0:13]),
    G("finally and Multiple catch", _VIVA[13:18]),
    G("throw and throws", _VIVA[18:26]),
    G("Collections Framework", _VIVA[26:45]),
]

EXAM_QS = [
    XE("Explain the three types of errors in Java with examples.", 4),
    XE("Draw and explain the Exception hierarchy (Throwable, Error, Exception, RuntimeException).", 6),
    XE("Distinguish between checked and unchecked exceptions with examples.", 4),
    XE("Write a Java program demonstrating try-catch for divide by zero and null pointer. (Practical 13)", 6),
    XE("Explain try, catch and finally blocks with a suitable program.", 6),
    XE("Write a program showing multiple catch blocks. State the order rule.", 4),
    XE("Differentiate throw and throws with an example method.", 4),
    XE("Write a program using throw to validate age and throws to declare a risky method.", 6),
    XE("List five built-in exceptions and the situation that raises each.", 4),
    XE("Explain the need of the Collections framework over arrays.", 3),
    XE("Draw the Collection hierarchy and explain List vs Set briefly.", 4),
    XE("Write a program using ArrayList: add, remove, search and traverse. (Practical 14)", 6),
    XE("Write a program using HashSet showing uniqueness; display with for-each. (Practical 14)", 4),
    XE("Differentiate ArrayList and HashSet (any six points).", 4),
    XE("Explain the for-each loop. How is it different from the classic for loop for collections?", 3),
]
