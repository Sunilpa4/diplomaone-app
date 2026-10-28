"""DI04000021 Unit 1 - solved Java programs (introduction, data types, control flow, arrays).
All programs are compiled and run with the JDK; outputs are genuine. Practical 1-3."""
from java_content import JP

PROGRAMS = [

JP("jv1_1", "Hello World - first Java program", '''
// File: Main.java - one class per program.
class Main {
  // main(): execution always starts here
  public static void main(String[] args) {
    System.out.println("Hello, World!");
    System.out.println("Welcome to GTU");
    System.out.print("Java is ");   // no new line
    System.out.println("simple.");
  }
}
''', expl="""
<p><b>Practical 1(a).</b> Steps: save the file as <code>Main.java</code>, compile with <code>javac Main.java</code> (creates <code>Main.class</code> - byte code), run with <code>java Main</code> (JVM reads the class file).</p>
<ul><li>The output window shows the two commands and the printed lines.</li>
<li><code>println</code> moves to a new line after printing; <code>print</code> stays on the same line.</li>
<li><code>//</code> starts a comment, which the compiler ignores.</li></ul>
"""),

JP("jv1_2", "Declaring and initializing variables of all primitive types", '''
class Main {
  public static void main(String[] args) {
    byte roll = 7;                 // -128 to 127
    short sem = 4;                 // 2 bytes
    int marks = 452;               // 4 bytes
    long mob = 9876543210L;        // suffix L
    float per = 78.5f;             // suffix f
    double cgpa = 8.25;            // 8 bytes
    char sec = 'A';                // single quotes
    boolean ok = true;             // true or false only

    System.out.println("roll = " + roll);
    System.out.println("sem = " + sem);
    System.out.println("marks = " + marks);
    System.out.println("mobile = " + mob);
    System.out.println("per = " + per);
    System.out.println("cgpa = " + cgpa);
    System.out.println("section = " + sec);
    System.out.println("passed = " + ok);
  }
}
''', expl="""
<p>Java has <b>8 primitive data types</b>. Four store whole numbers (byte, short, int, long), two store decimals (float, double), one stores a single character (char) and one a truth value (boolean).</p>
<ul><li><code>long</code> values end with <code>L</code> and <code>float</code> values with <code>f</code>, otherwise the compiler treats them as int and double.</li>
<li><code>+</code> with a string <b>joins</b> (concatenates) the value to the text.</li></ul>
"""),

JP("jv1_3", "Arithmetic operations and type casting", '''
class Main {
  public static void main(String[] args) {
    int a = 17, b = 5;
    int add = a + b, sub = a - b;
    int mul = a * b;
    int div = a / b;               // int division: 3
    int rem = a % b;               // remainder: 2
    System.out.println("add = " + add);
    System.out.println("sub = " + sub);
    System.out.println("mul = " + mul);
    System.out.println("div = " + div);
    System.out.println("rem = " + rem);

    // type casting
    double exact = (double) a / b;
    System.out.println("exact = " + exact);

    int r = (int) 9.7;             // double -> int
    System.out.println("cast = " + r);

    char ch = 'A';
    int code = ch;                 // char -> int (auto)
    char nx = (char)(ch + 1);
    System.out.println("code = " + code);
    System.out.println("next = " + nx);
  }
}
''', expl="""
<p><b>Practical 1(b).</b> Integer division throws the decimal part away: 17/5 gives 3. To get the exact answer, <b>cast</b> one operand to double before dividing.</p>
<ul><li><b>Widening</b> (automatic, no data loss): byte -&gt; short -&gt; int -&gt; long -&gt; float -&gt; double; char -&gt; int.</li>
<li><b>Narrowing</b> (manual cast, possible data loss): <code>(int) 9.7</code> cuts the fraction and keeps 9.</li>
<li>The remainder operator <code>%</code> returns what is left after division (17 % 5 = 2).</li></ul>
"""),

JP("jv1_4", "Scope and lifetime of variables", '''
class Main {
  public static void main(String[] args) {
    int x = 10;                    // born here
    System.out.println("x = " + x);
    {
      int y = 20;                  // born in inner block
      System.out.println("y = " + y);
      int z = x + y;               // outer var visible
      System.out.println("x + y = " + z);
    }
    // y = 30;  // ERROR: y died at the }
    // up to here x lives, y and z are gone
    System.out.println("x again = " + x);
  }
}
''', expl="""
<p><b>Scope</b> = where a variable can be used; <b>lifetime</b> = how long it exists.</p>
<ul><li>A variable is usable only inside the block <code>{ }</code> where it is declared. When the block ends, the variable dies.</li>
<li>Inner blocks can see outer variables (<code>z = x + y</code> works), but outer code cannot see variables declared inside (<code>y = 30;</code> after the block would be a compile error - it is commented out here, try removing the // to see the error yourself in a lab).</li>
<li>Because dead variables disappear quickly, Java programs stay memory-efficient.</li></ul>
"""),

JP("jv1_5", "Operators: arithmetic, relational, logical, bitwise, ternary, ++/--", '''
class Main {
  public static void main(String[] args) {
    int a = 10, b = 3;
    System.out.println("a/b = " + (a / b));
    System.out.println("a%b = " + (a % b));

    System.out.println("a>b = " + (a > b));      // relational
    boolean ok = (a > 5) && (b < 5);             // logical
    System.out.println("both = " + ok);

    System.out.println("a&b = " + (a & b));      // bitwise AND
    System.out.println("a|b = " + (a | b));      // bitwise OR
    System.out.println("a^b = " + (a ^ b));      // XOR
    int sh = a << 1;
    System.out.println("a<<1 = " + sh);          // shift

    int max = (a > b) ? a : b;    // ternary
    System.out.println("max = " + max);

    int c = a++;                  // use, then add 1
    int d = ++a;                  // add 1, then use
    System.out.println("c = " + c);
    System.out.println("d = " + d);
  }
}
''', expl="""
<ul><li><b>Arithmetic:</b> + - * / %. Wrap arithmetic in brackets inside println - <code>"a/b = " + a / b</code> would not even compile, because <code>+</code> joins the string to <code>a</code> first and then tries to divide a string.</li>
<li><b>Relational:</b> &gt; &lt; &gt;= &lt;= == != give true/false. <b>Logical:</b> &amp;&amp; || !</li>
<li><b>Bitwise:</b> 10 = 1010 and 3 = 0011 in binary, so a&amp;b=2 (0010), a|b=11 (1011), a^b=9 (1001); <code>a &lt;&lt; 1</code> shifts bits left = 20.</li>
<li><b>Ternary:</b> <code>condition ? valueIfTrue : valueIfFalse</code>.</li>
<li><code>a++</code> uses the old value then increments (c = 10, afterwards a = 11); <code>++a</code> increments first (d = 12).</li></ul>
"""),

JP("jv1_6", "if, if-else and if-else-if ladder (result grades)", '''
class Main {
  public static void main(String[] args) {
    int marks = 72;

    if (marks >= 35)                 // 1. simple if
      System.out.println("Result: Pass");

    if (marks >= 60) {               // 2. if-else
      System.out.println("Type: First");
    } else {
      System.out.println("Type: below 60");
    }

    // 3. if-else-if ladder
    if (marks >= 70)
      System.out.println("Grade: A");
    else if (marks >= 60)
      System.out.println("Grade: B");
    else if (marks >= 50)
      System.out.println("Grade: C");
    else if (marks >= 35)
      System.out.println("Grade: D");
    else
      System.out.println("Grade: Fail");
  }
}
''', expl="""
<ul><li><b>Simple if</b> runs its statement only when the condition is true.</li>
<li><b>if-else</b> chooses between two paths.</li>
<li><b>Ladder</b> checks conditions from top and runs the FIRST true branch - so put the highest limit first (70 before 35); otherwise 72 would wrongly fall into a lower grade.</li>
<li>For a single statement the braces <code>{ }</code> are optional.</li></ul>
"""),

JP("jv1_7", "Nested if-else: maximum of three numbers", '''
class Main {
  public static void main(String[] args) {
    int a = 25, b = 40, c = 15;
    int g;
    if (a > b) {                    // outer if
      if (a > c)                    // inner if
        g = a;
      else
        g = c;
    } else {
      if (b > c)                    // nested in else
        g = b;
      else
        g = c;
    }
    System.out.println("greatest = " + g);
  }
}
''', expl="""
<p><b>Practical 2(a).</b> An if inside another if is a <b>nested if</b>. The program first compares a with b, then compares the winner with c and stores the greatest number in <code>g</code>.</p>
<ul><li>Indentation (inner code shifted right) makes nested logic readable.</li>
<li>Short alternative: <code>Math.max(a, Math.max(b, c))</code>, or one ternary expression.</li></ul>
"""),

JP("jv1_8", "switch-case: day of the week and a simple menu", '''
class Main {
  public static void main(String[] args) {
    int day = 3;
    switch (day) {
      case 1:
        System.out.println("Monday");
        break;
      case 2:
        System.out.println("Tuesday");
        break;
      case 3:
        System.out.println("Wednesday");
        break;
      case 4:
        System.out.println("Thursday");
        break;
      case 5:
        System.out.println("Friday");
        break;
      default:
        System.out.println("Weekend");
    }

    // switch on a String (Java 7+)
    String op = "+";
    int x = 8, y = 4;
    int res = 0;
    switch (op) {
      case "+":
        res = x + y;
        break;
      case "*":
        res = x * y;
        break;
      default:
        res = -1;
    }
    System.out.println("result = " + res);
  }
}
''', expl="""
<ul><li><code>switch</code> compares one value against many <code>case</code> labels; the matching block runs.</li>
<li><b>break is compulsory</b>: without it, execution falls through into the next case (a famous interview question).</li>
<li><code>default</code> runs when no case matches.</li>
<li>Since Java 7, switch works on <b>String</b> too, as the small calculator menu shows.</li></ul>
"""),

JP("jv1_9", "Loops: for, while and do-while", '''
class Main {
  public static void main(String[] args) {
    // 1. for: fixed count
    System.out.println("Table of 7:");
    for (int i = 1; i <= 5; i++) {
      int p = 7 * i;
      System.out.println(i + " x 7 = " + p);
    }

    // 2. while: check before entering
    int n = 160, count = 0;
    while (n > 0) {        // count the digits
      n = n / 10;
      count++;
    }
    System.out.println("digits = " + count);

    // 3. do-while: body runs at least once
    int k = 5;
    do {
      System.out.println("k = " + k);
      k--;
    } while (k > 0);
  }
}
''', expl="""
<ul><li><b>for(init; condition; step)</b> - best when the number of repetitions is known.</li>
<li><b>while</b> tests the condition first; if it is false at the start, the body never runs.</li>
<li><b>do-while</b> tests after the body, so the body always runs <b>at least once</b> (useful for menus).</li>
<li>The digit-counting trick divides by 10 repeatedly - a very common exam question.</li></ul>
"""),

JP("jv1_10", "Sum of digits of a number (while loop)", '''
class Main {
  public static void main(String[] args) {
    int num = 4782;
    int n = num;
    int sum = 0;
    while (n != 0) {
      int d = n % 10;     // last digit
      sum = sum + d;
      n = n / 10;         // drop last digit
    }
    System.out.println("number = " + num);
    System.out.println("sum = " + sum);
  }
}
''', expl="""
<p><b>Practical 2(b).</b> The classic digit-splitting pattern:</p>
<ul><li><code>n % 10</code> peels off the last digit, <code>n / 10</code> removes it.</li>
<li>Repeat until the number becomes 0; add each digit into <code>sum</code>.</li>
<li>Dry run for 4782: 2 + 8 + 7 + 4 = 21.</li></ul>
"""),

JP("jv1_11", "break and continue statements", '''
class Main {
  public static void main(String[] args) {
    // continue: skip to the next round
    System.out.print("odd numbers 1..9: ");
    for (int i = 1; i <= 9; i++) {
      if (i % 2 == 0)
        continue;          // skip evens
      System.out.print(i + " ");
    }
    System.out.println();

    // break: leave the loop immediately
    int[] stops = {3, 5, 12, 7, 9};
    for (int s : stops) {
      if (s > 10) {
        System.out.println("big = " + s);
        break;             // stop searching
      }
    }
  }
}
''', expl="""
<ul><li><code>continue</code> skips only the current iteration; the loop keeps going.</li>
<li><code>break</code> ends the loop at once - e.g. after finding what we were searching for.</li>
<li>The <b>for-each</b> loop <code>for (int s : stops)</code> walks through every element of an array without an index.</li></ul>
"""),

JP("jv1_12", "1D array: declaration, traversal, sum and average", '''
class Main {
  public static void main(String[] args) {
    // declare + initialize in one step
    int[] marks = {78, 85, 66, 90, 71};

    // traversal with index
    System.out.println("All marks:");
    for (int i = 0; i < marks.length; i++) {
      int m = marks[i];
      System.out.println(i + " : " + m);
    }

    // sum and average with for-each
    int sum = 0;
    for (int m : marks)
      sum += m;
    double avg = 1.0 * sum / marks.length;

    System.out.println("sum = " + sum);
    System.out.println("average = " + avg);
  }
}
''', expl="""
<p><b>Practical 3(a).</b></p>
<ul><li>An <b>array</b> stores many values of one type under one name; indexes run from 0 to length-1.</li>
<li><code>marks.length</code> gives the number of elements (no brackets - it is a field, not a method).</li>
<li><code>1.0 * sum</code> makes the division decimal, so the average keeps its fraction.</li></ul>
"""),

JP("jv1_13", "2D array: addition of two matrices", '''
class Main {
  public static void main(String[] args) {
    int[][] a = {{1, 2, 3},
                 {4, 5, 6}};
    int[][] b = {{7, 8, 9},
                 {1, 2, 3}};
    int rows = a.length;
    int cols = a[0].length;
    int[][] sum = new int[rows][cols];

    for (int i = 0; i < rows; i++) {
      for (int j = 0; j < cols; j++) {
        sum[i][j] = a[i][j] + b[i][j];
        System.out.print(sum[i][j] + " ");
      }
      System.out.println();      // next row
    }
  }
}
''', expl="""
<p><b>Practical 3(b).</b></p>
<ul><li>A 2D array is an array of arrays - here a 2x3 matrix.</li>
<li><code>a.length</code> is the number of rows and <code>a[0].length</code> the number of columns.</li>
<li>Nested loops visit every cell; corresponding cells are added into <code>sum[i][j]</code>.</li>
<li>The inner <code>print</code> stays on the same line; after each row <code>println()</code> jumps to the next line, forming the matrix layout. Genuine output: 8 10 12 / 5 7 9.</li></ul>
"""),

JP("jv1_14", "Finding smallest and largest in an array", '''
class Main {
  public static void main(String[] args) {
    int[] t = {42, 17, 55, 9, 31};
    int min = t[0];
    int max = t[0];
    for (int v : t) {
      if (v < min)
        min = v;                 // new minimum found
      if (v > max)
        max = v;                 // new maximum found
    }
    System.out.println("smallest = " + min);
    System.out.println("largest = " + max);
  }
}
''', expl="""
<p>The scan-and-remember pattern:</p>
<ul><li>Assume the first element is the answer, then compare it with every element; whenever a smaller/larger value appears, remember it.</li>
<li>Runs in one pass - a favourite GTU 4-marker.</li></ul>
"""),

JP("jv1_15", "Star patterns with nested loops", '''
class Main {
  public static void main(String[] args) {
    // pattern 1: right triangle
    for (int i = 1; i <= 4; i++) {
      for (int j = 1; j <= i; j++)
        System.out.print("* ");
      System.out.println();
    }

    // pattern 2: number triangle
    System.out.println("---");
    for (int i = 4; i >= 1; i--) {
      for (int j = i; j >= 1; j--)
        System.out.print(j + " ");
      System.out.println();
    }
  }
}
''', expl="""
<ul><li>The <b>outer loop</b> fixes the row number; the <b>inner loop</b> prints that row's characters.</li>
<li>Row i of pattern 1 prints i stars; the inner loop's limit depends on i - this dependency is the key idea of every pattern program.</li>
<li>Pattern 2 counts down (4 to 1) and prints the numbers descending in each row.</li></ul>
"""),
]
