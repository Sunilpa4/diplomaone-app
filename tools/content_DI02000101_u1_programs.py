"""DI02000101 Unit 1 - solved Python programs (basics, I/O, data types). Run with python3; outputs are genuine."""
from py_content import PP

PROGRAMS = [
    PP("py1p1", "First Python program and print() options", r'''
# My first Python program
print("Hello, World!")
print("Welcome to", "GTU", "Diploma")      # values separated by space
print("A", "B", "C", sep="-")              # custom separator
print("Python", end=" ")                   # no newline at end
print("is easy")
print("Line1\nLine2\tTabbed")              # escape sequences
print()                                    # blank line
print('Single quotes', "double quotes", """triple quotes""")
''', (),
       r"""<ul><li>A Python program needs no <code>main()</code>, header files or semicolons. Statements run from top to bottom.</li>
<li><code>print()</code> separates values with a space by default. <code>sep</code> changes the separator and <code>end</code> changes what is printed at the end (default <code>'\n'</code>).</li>
<li><code>\n</code> = newline, <code>\t</code> = tab. Strings may use single, double or triple quotes.</li>
<li>Text after <code>#</code> is a comment and is ignored by the interpreter.</li></ul>"""),

    PP("py1p2", "Read and display personal details (Practical 2)", r'''
name = input("Enter your name      : ")
contact = input("Enter contact number : ")
email = input("Enter email          : ")
dob = input("Enter birth date     : ")

print("\n------ Student Details ------")
print("Name      :", name)
print("Contact   :", contact)
print("Email     :", email)
print("Birth date:", dob)
print("-----------------------------")
''', ["Ravi Patel", "9876543210", "ravi.patel@gmail.com", "15-08-2008"],
       r"""<p><code>input(prompt)</code> shows the prompt, waits for the user to type and press Enter, and returns the text as a <b>string</b>. Here all four values are kept as strings because no calculation is needed. A contact number is stored as a string so that leading zeros and the + sign are not lost.</p>"""),

    PP("py1p3", "Sum and average of three numbers", r'''
a = int(input("Enter first number : "))
b = int(input("Enter second number: "))
c = int(input("Enter third number : "))

total = a + b + c
avg = total / 3

print("Sum     =", total)
print("Average =", avg)
print("Average (2 decimals) = %.2f" % avg)
print(f"Average using f-string = {avg:.2f}")
''', ["45", "62", "38"],
       r"""<ul><li><code>input()</code> returns a string, so <code>int()</code> converts it to an integer before adding. Without it, "45" + "62" would join the strings to give "4562".</li>
<li><code>/</code> always gives a float in Python 3 (145 / 3 = 48.333…).</li>
<li>Formatting to 2 decimal places: the old style <code>"%.2f" % value</code>, or an f-string <code>f"{value:.2f}"</code>.</li></ul>"""),

    PP("py1p4", "Area and circumference of a circle", r'''
PI = 3.14159                      # constant (by convention)

r = float(input("Enter radius: "))
area = PI * r * r
circum = 2 * PI * r

print("Area          =", round(area, 2))
print("Circumference =", round(circum, 2))
''', ["7"],
       r"""<p><code>float()</code> allows decimal input such as 7.5. Python has no <code>const</code> keyword, so constants are written in <b>UPPERCASE</b> by convention (PI), and the programmer must not change them. <code>round(x, 2)</code> rounds to 2 decimal places.</p>"""),

    PP("py1p5", "Simple interest calculation", r'''
p = float(input("Principal amount (Rs): "))
r = float(input("Rate of interest (%) : "))
n = float(input("Time (years)         : "))

si = (p * r * n) / 100
amount = p + si

print("Simple Interest = Rs", si)
print("Total Amount    = Rs", amount)
''', ["25000", "8.5", "3"],
       r"""<p>Formula: <b>SI = P × R × N / 100</b>. Each input is converted with <code>float()</code> because rates and amounts may contain decimals. Arithmetic follows normal mathematical precedence; the parentheses make the order clear.</p>"""),

    PP("py1p6", "Swap two numbers (three methods)", r'''
a = int(input("Enter a: "))
b = int(input("Enter b: "))
print("Before swap: a =", a, " b =", b)

# Method 1: using a third variable
temp = a
a = b
b = temp
print("After method 1: a =", a, " b =", b)

# Method 2: without a third variable
a = a + b
b = a - b
a = a - b
print("After method 2: a =", a, " b =", b)

# Method 3: Pythonic way (tuple unpacking)
a, b = b, a
print("After method 3: a =", a, " b =", b)
''', ["10", "25"],
       r"""<p>Method 3 is unique to Python: <code>a, b = b, a</code> first builds the tuple <code>(b, a)</code> on the right side, then assigns its items to a and b. This is called <b>multiple assignment</b> or <b>tuple unpacking</b>. Each method swaps the values once, so the output alternates.</p>"""),

    PP("py1p7", "Data types with type() and isinstance()", r'''
a = 25
b = 3.75
c = 2 + 5j
d = "Python"
e = True
f = [10, 20, 30]
g = (1, 2, 3)
h = {1, 2, 3}
i = {"roll": 101, "name": "Amit"}
j = None

for value in (a, b, c, d, e, f, g, h, i, j):
    print(repr(value).ljust(30), type(value))

print("isinstance(a, int)   :", isinstance(a, int))
print("isinstance(b, float) :", isinstance(b, float))
print("Real/imag part of c  :", c.real, c.imag)
''', (),
       r"""<ul><li>Python is <b>dynamically typed</b>: the type is decided from the value at run time, so no declaration is needed.</li>
<li><code>type(x)</code> returns the class of the value. <code>isinstance(x, T)</code> checks whether x is of type T.</li>
<li><code>repr()</code> shows the value as Python code (strings in quotes) and <code>ljust(30)</code> pads it to 30 characters so that the output lines up.</li>
<li>A complex number has <code>.real</code> and <code>.imag</code> parts; Python uses <code>j</code> for the imaginary unit.</li></ul>"""),

    PP("py1p8", "Type casting: implicit and explicit conversion", r'''
# Implicit conversion (done automatically)
x = 10          # int
y = 2.5         # float
z = x + y       # int is promoted to float
print("10 + 2.5 =", z, type(z))
print("True + 5 =", True + 5)

# Explicit conversion (done by programmer)
print('int("25")     =', int("25"))
print("int(9.99)     =", int(9.99))        # decimal part removed
print('float("3.5")  =', float("3.5"))
print("float(7)      =", float(7))
print("str(100)      =", repr(str(100)))
print("bool(0), bool(5)    =", bool(0), bool(5))
print('bool(""), bool("a") =', bool(""), bool("a"))
print("complex(2, 3) =", complex(2, 3))
print('list("GTU")   =', list("GTU"))
print("tuple([1, 2]) =", tuple([1, 2]))
print("set([1,1,2])  =", set([1, 1, 2]))
print('int("1010", 2)=', int("1010", 2))   # binary string to int

try:
    int("12.5")
except ValueError as err:
    print("Error:", err)
''', (),
       r"""<ul><li><b>Implicit conversion:</b> in mixed expressions Python converts the lower type to the higher type (bool → int → float → complex) so that no data is lost.</li>
<li><b>Explicit conversion (type casting):</b> done using functions like <code>int()</code>, <code>float()</code>, <code>str()</code>, <code>bool()</code>, <code>list()</code>, <code>tuple()</code>, <code>set()</code> and <code>complex()</code>.</li>
<li><code>int(9.99)</code> truncates to 9 (it does not round). <code>bool()</code> is False for 0, empty strings and empty collections, and True otherwise.</li>
<li>A string that is not a valid integer, such as "12.5", raises a <b>ValueError</b>. Here it is caught with try/except so the program can continue.</li></ul>"""),

    PP("py1p9", "Temperature conversion (Celsius ↔ Fahrenheit)", r'''
c = float(input("Enter temperature in Celsius: "))
f = c * 9 / 5 + 32
print(f"{c} °C = {f:.1f} °F")

f = float(input("Enter temperature in Fahrenheit: "))
c = (f - 32) * 5 / 9
print(f"{f} °F = {c:.1f} °C")
''', ["37", "98.6"],
       r"""<p>Formulas: <b>F = C × 9/5 + 32</b> and <b>C = (F − 32) × 5/9</b>. Inside an f-string, <code>{f:.1f}</code> prints the value with 1 decimal place. The same variable can be reused for a new value, because a variable is just a name for an object.</p>"""),

    PP("py1p10", "String operations: index, slice, join, repeat", r'''
s = "PYTHON"
print("String      :", s)
print("Length      :", len(s))
print("s[0], s[-1] :", s[0], s[-1])
print("s[2:5]      :", s[2:5])
print("s[:3]       :", s[:3])
print("s[3:]       :", s[3:])
print("s[::-1]     :", s[::-1])

first = "Diploma"
second = "Engineering"
print("Concatenate :", first + " " + second)
print("Repeat      :", "Hi! " * 3)
print("Membership  :", "PY" in s, "Java" in s)
print("Upper/lower :", first.upper(), first.lower())

name = input("Enter your name: ")
print("Hello " + name + ", your name has", len(name), "characters.")
''', ["Kavya"],
       r"""<ul><li>Characters are accessed by <b>index</b>: positive from 0 (left) and negative from −1 (right). See the diagram "String Indexing and Slicing".</li>
<li><b>Slicing</b> <code>s[start:end:step]</code> gives the characters from start up to <b>end − 1</b>. <code>s[::-1]</code> reverses the string.</li>
<li><code>+</code> joins (concatenates) strings, <code>*</code> repeats them, and <code>in</code> checks whether a substring is present.</li>
<li>Strings are <b>immutable</b>: methods like <code>upper()</code> return a new string and leave the original unchanged.</li></ul>"""),

    PP("py1p11", "List: create, access, update, delete (Practical 3)", r'''
marks = [78, 85, 62, 90]
print("List          :", marks)
print("First, last   :", marks[0], marks[-1])
print("Slice [1:3]   :", marks[1:3])

marks[2] = 70                     # update an element
print("After update  :", marks)

marks.append(88)                  # add at end
marks.insert(1, 55)               # add at index 1
print("After add     :", marks)

marks.remove(55)                  # delete by value
del marks[0]                      # delete by index
print("After delete  :", marks)

print("Length, sum   :", len(marks), sum(marks))
print("Max, min      :", max(marks), min(marks))
mixed = [1, "two", 3.0, True]     # different types allowed
print("Mixed list    :", mixed)
''', (),
       r"""<p>A <b>list</b> is an ordered, <b>mutable</b> collection written in square brackets. It can hold values of different types and allows duplicates. Elements can be changed with an index, added with <code>append()</code>/<code>insert()</code>, and removed with <code>remove()</code> (by value) or <code>del</code> (by index). Lists are covered in detail in Unit 3.</p>"""),

    PP("py1p12", "Tuple and set: create, access, update, delete", r'''
# Tuple: ordered, immutable
t = (10, 20, 30, 20)
print("Tuple         :", t)
print("t[1], t[-1]   :", t[1], t[-1])
print("count(20)     :", t.count(20))
print("index(30)     :", t.index(30))
single = (5,)                     # comma needed for one item
print("Single tuple  :", single, type(single))
try:
    t[0] = 99                     # not allowed
except TypeError as e:
    print("Update error  :", e)
t = t + (40,)                     # create a new tuple instead
print("New tuple     :", t)

# Set: unordered, unique items, mutable
s = {3, 1, 2, 3, 1}
print("Set           :", s)       # duplicates removed
s.add(5)
s.discard(1)
print("After add/del :", s)
print("2 in s        :", 2 in s)
a, b = {1, 2, 3}, {2, 3, 4}
print("Union a | b   :", a | b)
print("Intersection  :", a & b)
''', (),
       r"""<ul><li>A <b>tuple</b> ( ) is like a list but <b>immutable</b>: its items cannot be changed, added or removed. A new tuple must be created instead. A single-item tuple needs a trailing comma: <code>(5,)</code>.</li>
<li>A <b>set</b> { } stores <b>unique</b> items in no fixed order, so duplicates are removed automatically and indexing is not possible. It supports mathematical operations such as union <code>|</code> and intersection <code>&amp;</code>.</li>
<li>Small integers are printed in sorted order here, but the order of a set is not guaranteed.</li></ul>"""),

    PP("py1p13", "Dictionary: student record", r'''
student = {"roll": 101, "name": "Amit", "branch": "Computer"}
print("Dictionary   :", student)
print("Name         :", student["name"])
print("get('city')  :", student.get("city", "Not found"))

student["sem"] = 2                # add a new key
student["name"] = "Amit Shah"     # update a value
print("After update :", student)

del student["branch"]             # delete a key
print("After delete :", student)

print("Keys   :", list(student.keys()))
print("Values :", list(student.values()))
for key, value in student.items():
    print(f"  {key:5} -> {value}")
''', (),
       r"""<ul><li>A <b>dictionary</b> stores <b>key: value</b> pairs in braces. Values are accessed by <b>key</b>, not by position.</li>
<li>Keys must be unique and immutable (e.g. str, int, tuple); values can be of any type.</li>
<li>Assigning to a new key adds it, and assigning to an existing key updates it. <code>del</code> removes a key. <code>get()</code> returns a default value instead of raising an error if the key is missing.</li>
<li><code>keys()</code>, <code>values()</code> and <code>items()</code> give the keys, the values and the pairs.</li></ul>"""),

    PP("py1p14", "Keywords and valid identifiers", r'''
import keyword

print("Total keywords:", len(keyword.kwlist))
print(keyword.kwlist)

names = ["roll_no", "_count", "2nd_sem", "total marks", "for", "Sum1", "my-name"]
for n in names:
    if keyword.iskeyword(n):
        result = "invalid (keyword)"
    elif n.isidentifier():
        result = "valid"
    else:
        result = "invalid"
    print(f"{n:12} : {result}")
''', (),
       r"""<ul><li><b>Keywords</b> are reserved words with a special meaning, so they cannot be used as names. Python 3.13 has 35 keywords. <code>True</code>, <code>False</code> and <code>None</code> start with a capital letter.</li>
<li><b>Identifier rules:</b> use letters, digits and underscore only; do not start with a digit; no spaces or special symbols; not a keyword. Identifiers are <b>case-sensitive</b> (Sum1 and sum1 are different).</li>
<li><code>str.isidentifier()</code> checks the naming rules and <code>keyword.iskeyword()</code> checks for keywords.</li></ul>"""),

    PP("py1p15", "Literals: number systems, strings, boolean, None", r'''
# Integer literals in different number systems
dec = 25
binary = 0b11001
octal = 0o31
hexa = 0x19
print("Decimal, binary, octal, hex:", dec, binary, octal, hexa)
print("bin(25), oct(25), hex(25)  :", bin(25), oct(25), hex(25))

# Float and complex literals
print("Float literals   :", 3.14, 2.5e3, 1.5E-2)
print("Complex literal  :", 4 + 3j)
print("Readable number  :", 1_00_000)     # underscores allowed

# String literals
single = 'GTU'
multi = """Line one
Line two"""
raw = r"C:\new\test"                      # raw: \ not special
print(single, "|", raw)
print(multi)

# Boolean and special literals
print("Boolean :", True, False, True + True)
print("None    :", None, type(None))
''', (),
       r"""<ul><li>A <b>literal</b> is a fixed value written directly in the code.</li>
<li><b>Integer literals</b> can be decimal, binary (<code>0b</code>), octal (<code>0o</code>) or hexadecimal (<code>0x</code>). All four above are the same number, 25. <code>bin()</code>, <code>oct()</code> and <code>hex()</code> convert the other way.</li>
<li><b>Float literals</b> can use exponent form: 2.5e3 = 2500.0. Underscores make big numbers readable.</li>
<li><b>String literals</b>: single, double, triple (multi-line) and raw (<code>r""</code>, where backslashes are not escape characters).</li>
<li><b>Boolean literals</b>: True (1) and False (0). <b>Special literal</b>: <code>None</code>, meaning "no value".</li></ul>"""),

    PP("py1p16", "Formatted output: marksheet with f-strings and format()", r'''
name = input("Student name: ")
m1, m2, m3 = map(int, input("Marks of 3 subjects: ").split())

total = m1 + m2 + m3
per = total / 3

print("\n{:^30}".format("MARKSHEET"))
print("-" * 30)
print(f"{'Name':<12}: {name}")
print(f"{'Subject 1':<12}: {m1:>5}")
print(f"{'Subject 2':<12}: {m2:>5}")
print(f"{'Subject 3':<12}: {m3:>5}")
print("-" * 30)
print(f"{'Total':<12}: {total:>5}")
print(f"{'Percentage':<12}: {per:>8.2f} %")
print("Result: %s with %.1f%%" % (name, per))
''', ["Riya Shah", "78 85 69"],
       r"""<ul><li><code>input().split()</code> splits the line "78 85 69" into three strings. <code>map(int, …)</code> converts each one to int, and they are assigned to m1, m2, m3 in one line.</li>
<li>Alignment in format specifiers: <code>&lt;</code> left, <code>&gt;</code> right, <code>^</code> centre; <code>:&gt;8.2f</code> means right-aligned, width 8, 2 decimals.</li>
<li>Three ways to format output: f-strings <code>f"{x}"</code> (Python 3.6+), <code>str.format()</code>, and the old <code>%</code> operator (<code>%%</code> prints a % sign).</li></ul>"""),
]

if __name__ == "__main__":
    for p in PROGRAMS:
        print("=" * 20, p["id"], p["title"]["en"]); print(p["out"])
