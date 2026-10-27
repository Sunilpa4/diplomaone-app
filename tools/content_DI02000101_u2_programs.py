"""DI02000101 Unit 2 - solved Python programs (operators, control flow). Outputs are genuine."""
from py_content import PP

PROGRAMS = [
    PP("py2p1", "Arithmetic operators", r'''
a = int(input("Enter a: "))
b = int(input("Enter b: "))

print("a + b  =", a + b)
print("a - b  =", a - b)
print("a * b  =", a * b)
print("a / b  =", a / b)       # true division (float)
print("a // b =", a // b)      # floor division
print("a % b  =", a % b)       # remainder
print("a ** b =", a ** b)      # power
print("-17 // 5 =", -17 // 5, "  -17 % 5 =", -17 % 5)
''', ["17", "5"],
       r"""<ul><li><code>/</code> always gives a <b>float</b> (17/5 = 3.4). <code>//</code> gives the <b>floor</b> of the quotient (3).</li>
<li><code>%</code> gives the remainder, and <code>**</code> is the power operator (17⁵ = 1419857).</li>
<li>With negative numbers, <code>//</code> rounds <b>down</b> towards −∞: −17 // 5 = −4. Then −17 % 5 = 3, because −4 × 5 + 3 = −17.</li></ul>"""),

    PP("py2p2", "Comparison and logical operators", r'''
x, y = 10, 20
print("x == y :", x == y)
print("x != y :", x != y)
print("x > y  :", x > y)
print("x < y  :", x < y)
print("x >= 10:", x >= 10)
print("y <= 15:", y <= 15)
print("Chained 5 < x < 15 :", 5 < x < 15)

age, has_id = 19, True
print("and :", age >= 18 and has_id)
print("or  :", age < 12 or age > 60)
print("not :", not has_id)

# and / or return one of the operands
print("0 or 'default' ->", 0 or "default")
print("5 and 7 ->", 5 and 7)
''', (),
       r"""<ul><li>Comparison operators return <code>True</code> or <code>False</code>. Python allows <b>chained comparisons</b>: <code>5 &lt; x &lt; 15</code> means <code>5 &lt; x and x &lt; 15</code>.</li>
<li><code>and</code> is True only if both sides are True; <code>or</code> is True if either side is True; <code>not</code> reverses the value.</li>
<li><b>Short-circuit evaluation:</b> <code>and</code> stops at the first false value and <code>or</code> stops at the first true value, and the result is that operand. So <code>0 or 'default'</code> gives 'default' and <code>5 and 7</code> gives 7.</li></ul>"""),

    PP("py2p3", "Assignment operators", r'''
x = 10
print("x = 10    ->", x)
x += 5;  print("x += 5    ->", x)
x -= 3;  print("x -= 3    ->", x)
x *= 2;  print("x *= 2    ->", x)
x /= 4;  print("x /= 4    ->", x)
x //= 2; print("x //= 2   ->", x)
x **= 3; print("x **= 3   ->", x)
x %= 5;  print("x %= 5    ->", x)

n = 6
n &= 3;  print("n &= 3    ->", n)
n |= 8;  print("n |= 8    ->", n)

# Walrus operator := (Python 3.8+) assigns inside an expression
if (length := len("Diploma")) > 5:
    print("Length", length, "is more than 5")
''', (),
       r"""<ul><li>A <b>compound assignment</b> <code>x op= y</code> means <code>x = x op y</code>; e.g. <code>x += 5</code> means <code>x = x + 5</code>.</li>
<li>After <code>/=</code> the value becomes a float (6.0), and it stays a float.</li>
<li>Python has <b>no ++ or −−</b>; write <code>x += 1</code>.</li>
<li>The <b>walrus operator</b> <code>:=</code> assigns a value inside an expression.</li></ul>"""),

    PP("py2p4", "Bitwise operators with binary view", r'''
a, b = 12, 10
print(f"a      = {a:3}  -> {a:08b}")
print(f"b      = {b:3}  -> {b:08b}")
print(f"a & b  = {a & b:3}  -> {a & b:08b}")
print(f"a | b  = {a | b:3}  -> {a | b:08b}")
print(f"a ^ b  = {a ^ b:3}  -> {a ^ b:08b}")
print(f"~a     = {~a:3}")
print(f"a << 2 = {a << 2:3}  -> {a << 2:08b}")
print(f"a >> 2 = {a >> 2:3}  -> {a >> 2:08b}")

n = int(input("Enter a number: "))
print(n, "is", "even" if n & 1 == 0 else "odd", "(checked with n & 1)")
''', ["37"],
       r"""<ul><li>Bitwise operators work on the <b>binary bits</b> of integers. The format <code>:08b</code> prints a number as 8 binary digits.</li>
<li><code>&amp;</code> is 1 only where both bits are 1; <code>|</code> where either bit is 1; <code>^</code> where the bits differ.</li>
<li><code>~a</code> = −(a + 1) = −13.</li>
<li><code>&lt;&lt; n</code> multiplies by 2ⁿ and <code>&gt;&gt; n</code> divides by 2ⁿ (integer result).</li>
<li><code>n &amp; 1</code> is 0 for even numbers, because the last bit of an even number is 0.</li></ul>"""),

    PP("py2p5", "Membership and identity operators", r'''
subjects = ["Python", "Maths", "Chemistry"]
print("'Python' in subjects    :", "Python" in subjects)
print("'Java' not in subjects  :", "Java" not in subjects)
print("'th' in 'Python'        :", "th" in "Python")
student = {"roll": 1, "name": "Om"}
print("'roll' in student       :", "roll" in student)   # checks keys

a = [1, 2, 3]
b = a
c = [1, 2, 3]
print("a == c :", a == c)       # same value
print("a is b :", a is b)       # same object
print("a is c :", a is c)       # different objects
print("a is not c :", a is not c)
x = None
print("x is None :", x is None)
''', (),
       r"""<ul><li><b>Membership:</b> <code>in</code> and <code>not in</code> test whether a value is present in a sequence (string, list, tuple, set). For a dictionary they check the <b>keys</b>.</li>
<li><b>Identity:</b> <code>is</code> and <code>is not</code> test whether two names refer to the <b>same object</b> in memory, while <code>==</code> compares <b>values</b> (see diagram "Identity (is) vs Equality (==)").</li>
<li>The recommended way to test for None is <code>x is None</code>.</li></ul>"""),

    PP("py2p6", "Operator precedence and associativity", r'''
print("2 + 3 * 4        =", 2 + 3 * 4)
print("(2 + 3) * 4      =", (2 + 3) * 4)
print("2 ** 3 ** 2      =", 2 ** 3 ** 2)    # right to left
print("(2 ** 3) ** 2    =", (2 ** 3) ** 2)
print("10 - 4 - 3       =", 10 - 4 - 3)      # left to right
print("100 / 10 * 2     =", 100 / 10 * 2)
print("-3 ** 2          =", -3 ** 2)         # ** before unary -
print("5 + 2 > 6 and 3 < 1 =", 5 + 2 > 6 and 3 < 1)
print("not 5 > 3 or 2 > 1  =", not 5 > 3 or 2 > 1)
a, b, c = 4, 8, 2
print("a + b / c * 3 - 1   =", a + b / c * 3 - 1)
''', (),
       r"""<ul><li><b>Precedence</b> decides which operator is applied first: <code>**</code> → unary → <code>* / // %</code> → <code>+ -</code> → shifts → bitwise → comparisons → <code>not</code> → <code>and</code> → <code>or</code>.</li>
<li><b>Associativity</b> decides the order among operators of equal precedence. Most are left to right; <code>**</code> is <b>right to left</b>, so 2 ** 3 ** 2 = 2 ** 9 = 512.</li>
<li><code>-3 ** 2</code> = −9, because ** is applied before the unary minus.</li>
<li>Last line: b / c = 4.0; × 3 = 12.0; 4 + 12.0 − 1 = 15.0. Use parentheses to make the order clear.</li></ul>"""),

    PP("py2p7", "Even/odd and positive/negative/zero", r'''
n = int(input("Enter a number: "))

# if...else
if n % 2 == 0:
    print(n, "is EVEN")
else:
    print(n, "is ODD")

# if...elif...else
if n > 0:
    print(n, "is POSITIVE")
elif n < 0:
    print(n, "is NEGATIVE")
else:
    print("The number is ZERO")

# conditional expression (ternary)
kind = "even" if n % 2 == 0 else "odd"
print("Using ternary:", kind)
''', ["-7"],
       r"""<ul><li><code>if…else</code> chooses between two blocks. <code>if…elif…else</code> chooses one block from many.</li>
<li>The colon <code>:</code> and the indentation mark each block.</li>
<li>The one-line <b>conditional expression</b> <code>x if condition else y</code> works like the ?: operator of C.</li>
<li>−7 % 2 = 1 in Python, so −7 is odd.</li></ul>"""),

    PP("py2p8", "Largest of three numbers (nested if)", r'''
a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

if a >= b:
    if a >= c:
        largest = a
    else:
        largest = c
else:
    if b >= c:
        largest = b
    else:
        largest = c
print("Largest (nested if)     :", largest)

if a >= b and a >= c:
    largest = a
elif b >= c:
    largest = b
else:
    largest = c
print("Largest (elif + and)    :", largest)
print("Largest (max function)  :", max(a, b, c))
''', ["45", "78", "23"],
       r"""<p>A <b>nested if</b> is an if statement inside another if or else block; each level is indented further. The same problem is solved more simply with <code>elif</code> and the logical <code>and</code>, or with the built-in <code>max()</code>. In exams, write the nested-if version unless the question says otherwise.</p>"""),

    PP("py2p9", "Grade from percentage (if-elif ladder)", r'''
m1 = float(input("Marks of subject 1: "))
m2 = float(input("Marks of subject 2: "))
m3 = float(input("Marks of subject 3: "))
per = (m1 + m2 + m3) / 3
print(f"Percentage = {per:.2f}")

if per >= 75:
    grade = "Distinction"
elif per >= 60:
    grade = "First Class"
elif per >= 50:
    grade = "Second Class"
elif per >= 35:
    grade = "Pass Class"
else:
    grade = "Fail"
print("Result     =", grade)
''', ["72", "65", "58"],
       r"""<p>The conditions are checked <b>from top to bottom</b>, and only the block of the <b>first true condition</b> executes; the rest are skipped. Because ≥ 75 is checked first, the next test only needs ≥ 60 (not "60 to 74"). The <code>else</code> part runs when no condition is true. See the flowchart "if…elif…else Ladder (Grade)".</p>"""),

    PP("py2p10", "Leap year check", r'''
year = int(input("Enter year: "))

if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print(year, "is a LEAP year")
else:
    print(year, "is NOT a leap year")

for y in (1900, 2000, 2024, 2026):
    leap = (y % 4 == 0 and y % 100 != 0) or y % 400 == 0
    print(y, "->", leap)
''', ["2028"],
       r"""<p>A year is a leap year if it is divisible by 4 but <b>not by 100</b>, <b>or</b> if it is divisible by 400. So 1900 is not a leap year, but 2000 is. The parentheses make the combination of <code>and</code> and <code>or</code> clear.</p>"""),

    PP("py2p11", "Simple calculator (menu with if-elif)", r'''
print("1. Add  2. Subtract  3. Multiply  4. Divide")
choice = int(input("Enter choice: "))
a = float(input("Enter first number : "))
b = float(input("Enter second number: "))

if choice == 1:
    print("Result =", a + b)
elif choice == 2:
    print("Result =", a - b)
elif choice == 3:
    print("Result =", a * b)
elif choice == 4:
    if b != 0:
        print("Result =", round(a / b, 3))
    else:
        print("Error: division by zero")
else:
    print("Invalid choice")
''', ["4", "22", "7"],
       r"""<p>Suggested project 1 from the syllabus. The <code>if-elif</code> chain works like a <code>switch</code> statement. A nested if prevents division by zero. (Python 3.10+ also has <code>match-case</code>, which is not in the syllabus.)</p>"""),

    PP("py2p12", "Sum of digits, reverse and palindrome number (while)", r'''
n = int(input("Enter a number: "))
temp = n
total = 0
rev = 0
while temp > 0:
    digit = temp % 10          # last digit
    total += digit
    rev = rev * 10 + digit
    temp //= 10                # remove last digit

print("Sum of digits =", total)
print("Reverse       =", rev)
if rev == n:
    print(n, "is a PALINDROME number")
else:
    print(n, "is NOT a palindrome")
''', ["12321"],
       r"""<ul><li><code>while</code> repeats as long as the condition is true. It is used when the number of repetitions is not known in advance.</li>
<li><code>% 10</code> gives the last digit and <code>// 10</code> removes it. Each digit is added to the sum and appended to the reverse.</li>
<li>The original value is kept in <code>n</code> because <code>temp</code> becomes 0.</li></ul>"""),

    PP("py2p13", "Factorial and multiplication table (for, range)", r'''
n = int(input("Enter a number: "))

fact = 1
for i in range(1, n + 1):
    fact *= i
print(f"{n}! = {fact}")

print(f"Table of {n}:")
for i in range(1, 11):
    print(f"{n} x {i:2} = {n * i:3}")

print("Even numbers 2-20:", end=" ")
for i in range(2, 21, 2):
    print(i, end=" ")
print()
''', ["7"],
       r"""<ul><li><code>for i in range(1, n + 1)</code> runs with i = 1, 2, …, n. The stop value is excluded, so <b>n + 1</b> is written.</li>
<li><code>range(2, 21, 2)</code> gives 2, 4, …, 20 (step 2).</li>
<li><code>end=" "</code> keeps the output on one line, and the final <code>print()</code> ends the line.</li></ul>"""),

    PP("py2p14", "Prime number check (for-else) and primes in a range", r'''
n = int(input("Enter a number: "))
if n < 2:
    print(n, "is not prime")
else:
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            print(f"{n} is NOT prime (divisible by {i})")
            break
    else:
        print(n, "is PRIME")

print("Primes between 1 and 50:")
for num in range(2, 51):
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            break
    else:
        print(num, end=" ")
print()
''', ["91"],
       r"""<ul><li>A loop can have an <b>else</b> block, which runs only if the loop ends normally, <b>without break</b>. If a divisor is found, <code>break</code> skips the else. So the else means "no divisor found → prime".</li>
<li>Checking divisors up to √n is enough: 91 = 7 × 13 is found at 7.</li>
<li>The second part uses <b>nested loops</b>: for each number, an inner loop checks for divisors.</li></ul>"""),

    PP("py2p15", "Fibonacci series (while) and sum of N numbers", r'''
n = int(input("How many Fibonacci terms? "))
a, b = 0, 1
count = 0
while count < n:
    print(a, end=" ")
    a, b = b, a + b
    count += 1
print()

total, i = 0, 1
while i <= 100:
    total += i
    i += 1
else:
    print("Loop finished normally.")
print("Sum of 1 to 100 =", total)
''', ["10"],
       r"""<p>Each Fibonacci term is the sum of the previous two (0, 1, 1, 2, 3, 5, …). The multiple assignment <code>a, b = b, a + b</code> updates both values at once without a temporary variable. A <code>while</code> loop can also have an <code>else</code> part, which runs when the condition becomes false (not after a break).</p>"""),

    PP("py2p16", "break, continue and pass", r'''
print("break    :", end=" ")
for i in range(1, 8):
    if i == 4:
        break             # exit the loop
    print(i, end=" ")
print()

print("continue :", end=" ")
for i in range(1, 8):
    if i == 4:
        continue          # skip this iteration
    print(i, end=" ")
print()

print("pass     :", end=" ")
for i in range(1, 8):
    if i == 4:
        pass              # do nothing (placeholder)
    print(i, end=" ")
print()

def check(n):
    if n < 0:
        return "negative"   # return ends the function
    return "non-negative"
print("return   :", check(-5), check(3))

while True:               # infinite loop with exit
    s = input("Type 'q' to quit: ")
    if s == "q":
        print("Bye!")
        break
''', ["hello", "q"],
       r"""<ul><li><b>break</b> immediately ends the loop.</li>
<li><b>continue</b> skips the rest of the current iteration and goes to the next one.</li>
<li><b>pass</b> does nothing. It is used where a statement is required syntactically but no action is needed, e.g. an empty function or a block to be written later.</li>
<li><b>return</b> ends a function and sends a value back to the caller (Unit 4).</li>
<li><code>while True</code> with break is the usual way to repeat until the user chooses to stop.</li></ul>"""),

    PP("py2p17", "Pattern printing using nested loops", r'''
n = int(input("Enter rows: "))

print("Right triangle:")
for i in range(1, n + 1):
    for j in range(i):
        print("*", end=" ")
    print()

print("Number triangle:")
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

print("Pyramid:")
for i in range(1, n + 1):
    print(" " * (n - i) + "* " * i)

print("Floyd's triangle:")
k = 1
for i in range(1, n + 1):
    for j in range(i):
        print(f"{k:3}", end="")
        k += 1
    print()
''', ["4"],
       r"""<ul><li>In <b>nested loops</b>, the outer loop controls the <b>rows</b> and the inner loop prints the <b>columns</b> of each row. The inner loop runs completely for each pass of the outer loop.</li>
<li><code>print()</code> after the inner loop moves to the next line.</li>
<li>The pyramid uses string repetition: (n − i) spaces followed by i stars.</li>
<li>Floyd's triangle prints consecutive numbers, with <code>k</code> continuing across rows.</li></ul>"""),

    PP("py2p18", "Number guessing game (project)", r'''
import random

random.seed(6)               # fixed seed only for this demo
secret = random.randint(1, 50)
attempts = 0

print("Guess the number between 1 and 50")
while True:
    guess = int(input("Your guess: "))
    attempts += 1
    if guess < secret:
        print("Too low!")
    elif guess > secret:
        print("Too high!")
    else:
        print(f"Correct! You guessed it in {attempts} attempts.")
        break
''', ["25", "40", "35", "37"],
       r"""<p>Suggested project 2 from the syllabus. It combines a <code>while True</code> loop, an <code>if-elif-else</code> ladder and <code>break</code>. <code>random.randint(1, 50)</code> picks a random integer from 1 to 50. The seed is fixed here only so that the demo output is repeatable; remove <code>random.seed(6)</code> to get a new number each time.</p>"""),
]

if __name__ == "__main__":
    for p in PROGRAMS:
        print("=" * 20, p["id"], p["title"]["en"]); print(p["out"])
