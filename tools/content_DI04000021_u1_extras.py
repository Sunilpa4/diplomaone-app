"""DI04000021 Unit 1 extras: syntax sheet, viva, exam questions."""
from java_content import SXE, VE, XE, G

SYNTAX = [
    G("First Program", [
        SXE("Program skeleton", """class Main {
  public static void main(String[] args) {
    // statements
  }
}
// javac Main.java  then  java Main""",
            "class name = file name; main() = entry point"),
        SXE("Printing", """System.out.println("text");  // + new line
System.out.print("text");    // same line
System.out.println("x = " + x);   // join""",
            "println vs print; + joins text and value"),
    ]),
    G("Data Types and Operators", [
        SXE("Primitive types", """byte b = 7;      short s = 400;
int i = 452;      long l = 9876543210L;
float f = 78.5f;  double d = 8.25;
char c = 'A';     boolean ok = true;""",
            "8 primitives; L and f suffixes"),
        SXE("Casting", """double d = i;            // auto (widen)
int r = (int) 9.7;       // manual cast
int code = 'A';          // 65
char nx = (char)('A'+1); // 'B'""",
            "widening automatic, narrowing needs (type)"),
        SXE("Operators", """+ - * / %          arithmetic
< > <= >= == !=    relational
&& || !            logical
+= -= *= /= %=     compound assignment
cond ? x : y       ternary
++ --              increment / decrement
& | ^ << >>        bitwise""",
            "postfix i++ uses old value, prefix ++i new value"),
    ]),
    G("Control Flow", [
        SXE("if / if-else / ladder", """if (x > 0) { }
if (x > 0) { } else { }
if (m>=70) A;
else if (m>=60) B;
else if (m>=35) D;
else Fail;""",
            "ladder: first true branch runs"),
        SXE("switch-case", """switch (day) {
  case 1:
    System.out.println("Mon");
    break;
  default:
    System.out.println("Other");
}""",
            "break required; String allowed (Java 7+)"),
        SXE("Loops", """for (int i = 1; i <= 5; i++) { }
while (n != 0) { }
do { } while (k > 0);
for (int m : marks) { }   // for-each""",
            "while tests first; do-while runs at least once"),
        SXE("break and continue", """if (s > 10) break;     // exit loop
if (i % 2 == 0) continue; // next round""",
            "break exits innermost loop/switch"),
    ]),
    G("Arrays", [
        SXE("1D arrays", """int[] a = {78, 85, 66};
int[] b = new int[5];
a.length                   // size (field)
a[0] .. a[a.length - 1]    // 0-based""",
            "declaration, creation, length, indexing"),
        SXE("2D arrays", """int[][] m = {{1,2,3},{4,5,6}};
m.length      // rows
m[0].length   // columns
m[i][j]       // row i, column j""",
            "array of arrays; nested loops to visit cells"),
    ]),
]

_VIVA = [
    VE("Who developed Java and in which year?", "James Gosling with the Green Team at Sun Microsystems, in 1995; the language was first called Oak."),
    VE("What is Java?", "An object-oriented, platform-independent programming language that is both compiled (to byte code) and interpreted (by the JVM)."),
    VE("Give five features of Java.", "Simple, object oriented, platform independent, robust, secure; also multithreaded, portable and high performance."),
    VE("Why is Java called platform independent?", "javac produces byte code, not machine code; the same .class file runs on any OS because every OS has its own JVM."),
    VE("Name four application areas of Java.", "Android apps, web and enterprise servers, desktop applications, and big data / AI tools."),
    VE("What are JDK, JRE and JVM?", "JDK = development kit for writing programs (javac + tools), contains JRE; JRE = runtime environment (libraries + JVM); JVM = virtual machine that executes byte code."),
    VE("What is byte code?", "The intermediate, OS-independent code that javac writes into .class files; the JVM executes it."),
    VE("Write the commands to compile and run Main.java.", "javac Main.java (compile to Main.class) and java Main (run on the JVM)."),
    VE("What does 'Write Once, Run Anywhere' mean?", "Compile the program a single time into byte code and run the same file on every operating system."),
    VE("Which method starts every Java program?", "public static void main(String[] args)."),
    VE("Why must main() be public and static?", "public so the JVM can call it from outside; static so it can run without creating an object first."),
    VE("What does void in main() mean?", "The method returns nothing."),
    VE("Why must the file be saved as Main.java?", "The file name must match the class name declared inside it."),
    VE("Is Java case sensitive?", "Yes: Main, main and MAIN are different names."),
    VE("Difference between print() and println()?", "println adds a new line after printing; print stays on the same line."),
    VE("List the 8 primitive data types of Java.", "byte, short, int, long, float, double, char, boolean."),
    VE("What are the sizes of int and double?", "int = 4 bytes, double = 8 bytes."),
    VE("Why do we write 9876543210L and 78.5f?", "Without L the number is treated as int (too large here); without f a decimal is treated as double and cannot go into a float."),
    VE("Is String a primitive type?", "No, String is a class; but Java allows the easy literal form String s = \"Hi\";."),
    VE("What is a variable?", "A named memory location whose value can change; in Java it must be declared with a type before use."),
    VE("Define scope and lifetime of a variable.", "Scope = the region of code where the variable can be used (its block); lifetime = how long it exists (block entry to block end)."),
    VE("Can outer code use a variable declared inside { }?", "No - the variable dies when the block ends; using it outside is a compile error."),
    VE("What is the difference between widening and narrowing?", "Widening converts a smaller type to a larger one automatically without data loss; narrowing needs a manual cast and may lose data."),
    VE("What does (int) 9.7 do?", "A narrowing cast: the fraction is cut, so the value is 9."),
    VE("What is the output of char ch = 'A' + 1?", "'A' + 1 is int 66; assigning back to char needs a cast: (char)('A'+1) gives 'B'."),
    VE("Why does 17/5 print 3 but (double)17/5 prints 3.4?", "int/int is integer division; casting one operand to double makes it decimal division."),
    VE("Name the groups of operators in Java.", "Arithmetic, relational, logical, assignment, conditional (ternary), increment/decrement, bitwise."),
    VE("Difference between i++ and ++i?", "i++ uses the old value then increments; ++i increments first and uses the new value."),
    VE("What does the ternary operator do?", "condition ? valueIfTrue : valueIfFalse - a one-line if-else that returns a value."),
    VE("What is the operator precedence problem in \"sum = \" + a + b?", "It joins as text (sum = 105); to add first, write \"sum = \" + (a + b)."),
    VE("Why is 17 % 5 equal to 2?", "% is the remainder operator: 17 = 5 x 3 + 2."),
    VE("When do you use an if-else-if ladder?", "When several ranges are tested, like grade calculation; the first true branch runs."),
    VE("What is a nested if?", "An if statement placed inside another if (or else) block."),
    VE("Why must each case in switch end with break?", "Without break, execution falls through and the following cases also run."),
    VE("Can switch work on strings?", "Yes, since Java 7 switch accepts String values."),
    VE("Differentiate while and do-while.", "while tests before the body (may run zero times); do-while tests after, so the body always runs at least once."),
    VE("When is the for loop preferred?", "When the number of repetitions is known in advance."),
    VE("What is the role of break and continue?", "break exits the innermost loop or switch immediately; continue skips to the next iteration."),
    VE("What is the difference between length in arrays and length() in String?", "length is a field of an array; length() is a method of the String class."),
    VE("How are array elements numbered?", "From 0 to length-1; marks[0] is the first element."),
    VE("How do you create an array of 5 integers?", "int[] a = new int[5]; or with values int[] a = {78, 85, 66, 90, 71};."),
    VE("What is a 2D array?", "An array of arrays, viewed as rows and columns; a[0].length is the number of columns."),
    VE("Why are two loops used for matrix addition?", "The outer loop selects the row i and the inner loop the column j, so every cell m[i][j] is added."),
    VE("What is the sum-of-digits algorithm?", "while n != 0: add n % 10 and set n = n / 10, until the number becomes 0."),
    VE("What is for-each loop in Java?", "for (int m : marks) - visits each element of the array without an index variable."),
]

assert len(_VIVA) == 45
VIVA = [
    G("Introduction, JDK/JRE/JVM", _VIVA[0:15]),
    G("Data Types, Scope, Casting, Operators", _VIVA[15:31]),
    G("Control Flow and Arrays", _VIVA[31:45]),
]

EXAM_QS = [
    XE("Define Java. Explain any four features of Java.", 4),
    XE("Differentiate compiling and interpreting with respect to Java.", 3),
    XE("Explain JDK, JRE and JVM with a neat diagram.", 4),
    XE("Explain byte code and 'Write Once, Run Anywhere'.", 4),
    XE("Explain the structure of a Java program with the Hello World example.", 4),
    XE("List and explain the primitive data types of Java with sizes and examples.", 6),
    XE("Explain the scope and lifetime of variables in Java.", 3),
    XE("Explain widening and narrowing conversion with examples.", 4),
    XE("Explain any four operators of Java with examples.", 4),
    XE("Explain if-else and the if-else-if ladder with a grading example.", 4),
    XE("Explain switch-case with an example. Why is break needed?", 4),
    XE("Differentiate while and do-while loops with examples.", 3),
    XE("Explain break and continue with examples.", 3),
    XE("Write a Java program to find the maximum of three numbers using nested if. (Practical 2a)", 4),
    XE("Write a Java program to find the sum of digits of a number. (Practical 2b)", 4),
    XE("Write a Java program to print the sum and average of array elements. (Practical 3a)", 4),
    XE("Write a Java program to add two matrices. (Practical 3b)", 6),
    XE("Explain arithmetic operations and type casting with a Java program. (Practical 1b)", 4),
]
