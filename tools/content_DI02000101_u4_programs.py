"""DI02000101 Unit 4 - solved Python programs (built-in functions, strings, files, UDF). Outputs are genuine."""
from py_content import PP

STORY = """Python is a popular language.
It is easy to learn.
Python is used in AI and web development.
"""

PROGRAMS = [
    PP("py4p1", "Type conversion: int(), float(), str(), bool(), complex()", r'''
print("int('25')      :", int("25"))
print("int(9.99)      :", int(9.99))
print("int(-7.8)      :", int(-7.8))
print("int('1010', 2) :", int("1010", 2))
print("int('ff', 16)  :", int("ff", 16))
print("float('3.5')   :", float("3.5"))
print("float(7)       :", float(7))
print("str(12.5) + 'kg':", str(12.5) + "kg")
print("bool(0), bool(7)     :", bool(0), bool(7))
print("bool(''), bool('0')  :", bool(""), bool("0"))
print("bool([]), bool([0])  :", bool([]), bool([0]))
print("complex(2, 3)  :", complex(2, 3))
print("complex('4-5j'):", complex("4-5j"))

a = input("Enter first number : ")
b = input("Enter second number: ")
print("Without conversion :", a + b)
print("With int()         :", int(a) + int(b))

try:
    int("12.5")
except ValueError as e:
    print("Error:", e)
''', ["12", "30"],
       r"""<ul><li><code>int()</code> converts a string of digits or a float to an integer. A float is <b>truncated</b> towards zero (9.99 → 9, −7.8 → −7). A second argument gives the base (2, 8, 16).</li>
<li><code>float()</code> gives a decimal number, <code>str()</code> gives text, and <code>complex(real, imag)</code> gives a complex number.</li>
<li><code>bool()</code> is False only for 0, 0.0, "", [], (), {}, set() and None; everything else (even "0") is True.</li>
<li><code>input()</code> always returns a string, so "12" + "30" = "1230". Convert first to add the numbers.</li>
<li><code>int("12.5")</code> raises ValueError; use <code>int(float("12.5"))</code>.</li></ul>"""),

    PP("py4p2", "Collection conversion: list(), tuple(), set(), frozenset(), dict()", r'''
s = "hello"
print("list(s)       :", list(s))
print("tuple(s)      :", tuple(s))
print("sorted(set(s)):", sorted(set(s)))

nums = [3, 1, 3, 2, 1]
print("tuple(nums)   :", tuple(nums))
print("set(nums)     :", set(nums))
print("frozenset     :", frozenset(nums))
print("list(range(5)):", list(range(5)))

pairs = [("a", 1), ("b", 2)]
print("dict(pairs)   :", dict(pairs))
print("dict(kw)      :", dict(x=10, y=20))
print("dict(zip)     :", dict(zip(["roll", "name"], [7, "Om"])))
d = {"p": 1, "q": 2}
print("list(d)       :", list(d))
print("list(items)   :", list(d.items()))
print("tuple(d.values()):", tuple(d.values()))
''', (),
       r"""<ul><li><code>list()</code>, <code>tuple()</code>, <code>set()</code> and <code>frozenset()</code> accept any <b>iterable</b> (string, list, tuple, range, dict…) and build that type from its items.</li>
<li>set() and frozenset() remove duplicates; frozenset is immutable.</li>
<li><code>dict()</code> needs key-value pairs: a list of 2-item tuples, keyword arguments, or <code>zip(keys, values)</code>.</li>
<li>Converting a dictionary with list() gives its <b>keys</b>.</li></ul>"""),

    PP("py4p3", "bytes() and bytearray()", r'''
b = bytes("Hi", "utf-8")
print("bytes('Hi')     :", b)
print("type            :", type(b))
print("b[0]            :", b[0], "(ASCII of 'H')")
print("bytes([65, 66]) :", bytes([65, 66]))
print("bytes(3)        :", bytes(3))
print("decode()        :", b.decode("utf-8"))

ba = bytearray("Hi", "utf-8")
ba[0] = 74                # 'J'
ba.append(33)             # '!'
print("bytearray       :", ba)
print("as text         :", ba.decode())

try:
    b[0] = 74
except TypeError as e:
    print("bytes error     :", e)
''', (),
       r"""<ul><li><code>bytes()</code> creates an <b>immutable</b> sequence of bytes (integers 0–255). A string needs an encoding such as "utf-8"; a list of integers is used directly; <code>bytes(n)</code> gives n zero bytes.</li>
<li><code>bytearray()</code> is the <b>mutable</b> version: bytes can be changed and appended.</li>
<li><code>decode()</code> converts bytes back into a string. Bytes are used in binary files, images and network data.</li></ul>"""),

    PP("py4p4", "Math built-in functions: abs, round, pow, divmod, sum, min, max", r'''
print("abs(-7.5)        :", abs(-7.5))
print("abs(3 - 4j)      :", abs(3 - 4j))
print("round(3.14159, 2):", round(3.14159, 2))
print("round(7.6)       :", round(7.6))
print("round(2.5), round(3.5):", round(2.5), round(3.5))
print("round(1234, -2)  :", round(1234, -2))
print("pow(2, 5)        :", pow(2, 5))
print("pow(2, 5, 3)     :", pow(2, 5, 3))
print("divmod(17, 5)    :", divmod(17, 5))
q, r = divmod(125, 60)
print("125 minutes      :", q, "hour", r, "minutes")

marks = [78, 85, 62, 90]
print("sum(marks)       :", sum(marks))
print("sum(marks, 10)   :", sum(marks, 10))
print("min, max         :", min(marks), max(marks))
print("max of values    :", max(4, 9, 2))
print("longest word     :", max(["cat", "tiger", "ox"], key=len))
''', (),
       r"""<ul><li><code>abs(x)</code> gives the absolute value (magnitude for complex numbers: |3−4j| = 5).</li>
<li><code>round(x, n)</code> rounds to n decimal places. With no n it returns an int. Exact halves go to the <b>nearest even</b> number (2.5 → 2, 3.5 → 4).</li>
<li><code>pow(x, y)</code> = x<sup>y</sup>; <code>pow(x, y, m)</code> = x<sup>y</sup> % m.</li>
<li><code>divmod(a, b)</code> returns the tuple (a // b, a % b).</li>
<li><code>sum(iterable, start)</code>, <code>min()</code> and <code>max()</code> work on sequences or on separate arguments; <code>key=</code> changes how items are compared.</li></ul>"""),

    PP("py4p5", "String testing methods: isalnum, isalpha, isdigit … (password checker)", r'''
for s in ["Python3", "Python", "2024", "hello", "HELLO", "   ", "my_var", "2var"]:
    print(f"{s!r:10} alnum={s.isalnum()!s:5} alpha={s.isalpha()!s:5} "
          f"digit={s.isdigit()!s:5} id={s.isidentifier()}")

print("'abc'.islower(), 'ABC'.isupper():", "abc".islower(), "ABC".isupper())
print("'  '.isspace():", "  ".isspace())

pwd = input("Enter password: ")
upper = lower = digit = special = 0
for ch in pwd:
    if ch.isupper():
        upper += 1
    elif ch.islower():
        lower += 1
    elif ch.isdigit():
        digit += 1
    elif not ch.isspace():
        special += 1
print("Upper:", upper, "Lower:", lower, "Digit:", digit, "Special:", special)
if len(pwd) >= 8 and upper and lower and digit and special:
    print("Strong password")
else:
    print("Weak password")
''', ["Gtu@2025"],
       r"""<ul><li>The <b>is…()</b> methods test a string and return True or False:
isalnum() (letters/digits only), isalpha() (letters only), isdigit() (digits only), islower(), isupper(), isspace() (whitespace only), isidentifier() (valid variable name).</li>
<li>The password checker loops through each character and counts categories. Note that <code>0</code> counts as False, so <code>if upper</code> means "at least one uppercase letter".</li></ul>"""),

    PP("py4p6", "String functions: len, max, min, find, rfind, count, startswith, endswith", r'''
s = "banana bread"
print("String          :", s)
print("len(s)          :", len(s))
print("max(s), min(s)  :", repr(max(s)), repr(min(s)))
print("find('an')      :", s.find("an"))
print("rfind('an')     :", s.rfind("an"))
print("find('xyz')     :", s.find("xyz"))
print("find('a', 4)    :", s.find("a", 4))
print("count('a')      :", s.count("a"))
print("count('an')     :", s.count("an"))
print("startswith('ban'):", s.startswith("ban"))
print("endswith('read') :", s.endswith("read"))

files = ["notes.pdf", "photo.jpg", "prog.py", "data.csv", "test.py"]
py_files = [f for f in files if f.endswith(".py")]
print("Python files    :", py_files)

email = input("Enter email: ")
at = email.find("@")
if at > 0 and email.rfind(".") > at:
    print("Username:", email[:at], " Domain:", email[at + 1:])
else:
    print("Invalid email")
''', ["riya.shah@gtu.ac.in"],
       r"""<ul><li><code>len()</code> counts characters (including spaces). <code>max()</code>/<code>min()</code> give the character with the largest/smallest Unicode value (a space is smallest).</li>
<li><code>find(sub)</code> returns the index of the <b>first</b> occurrence and <code>rfind(sub)</code> the <b>last</b>; both return <b>−1</b> if not found. An optional start index can be given.</li>
<li><code>count(sub)</code> counts non-overlapping occurrences.</li>
<li><code>startswith()</code>/<code>endswith()</code> check the beginning/end of a string, e.g. a file extension.</li></ul>"""),

    PP("py4p7", "Case conversion and replace(): capitalize, lower, upper, title, swapcase", r'''
s = "python PROGRAMMING is fun"
print("Original     :", s)
print("capitalize() :", s.capitalize())
print("lower()      :", s.lower())
print("upper()      :", s.upper())
print("title()      :", s.title())
print("swapcase()   :", s.swapcase())
print("replace()    :", s.replace("fun", "easy"))
print("replace once :", "a-b-c-d".replace("-", "+", 1))
print("original unchanged:", s)

name = input("Enter your full name: ")
print("Proper case  :", name.title())
initials = "".join(w[0].upper() + "." for w in name.split())
print("Initials     :", initials)
ans = input("Continue? (yes/no): ")
print("Accepted" if ans.strip().lower() == "yes" else "Stopped")
''', ["amit kumar shah", "  YES "],
       r"""<ul><li><code>capitalize()</code>: first character uppercase, all others lowercase. <code>title()</code>: first letter of <b>every word</b> uppercase.</li>
<li><code>lower()</code>/<code>upper()</code> change all letters; <code>swapcase()</code> swaps lower and upper.</li>
<li><code>replace(old, new[, count])</code> replaces occurrences, optionally only the first <i>count</i>.</li>
<li>Strings are immutable: every method returns a <b>new string</b> and the original is unchanged.</li>
<li><code>.strip().lower()</code> makes input checks work for "YES", " yes " and so on.</li></ul>"""),

    PP("py4p8", "strip, lstrip, rstrip, format(), center, ljust, rjust (marksheet)", r'''
raw = "   Surat   "
print("[" + raw + "]")
print("[" + raw.strip() + "]  strip")
print("[" + raw.lstrip() + "]  lstrip")
print("[" + raw.rstrip() + "]  rstrip")
print("[" + "**GTU**".strip("*") + "]  strip('*')")

print("{} scored {} marks".format("Riya", 85))
print("{1} before {0}".format("A", "B"))
print("{name} is in sem {sem}".format(name="Om", sem=2))
print("Pi = {:.3f}".format(3.14159))
print("[" + "Hi".center(10, "-") + "]")
print("[" + "Hi".ljust(10) + "]")
print("[" + "Hi".rjust(10) + "]")

data = [("Python", 85), ("Maths", 72), ("Physics", 91)]
print("=" * 26)
print("MARKSHEET".center(26))
print("=" * 26)
for sub, m in data:
    print(sub.ljust(15) + str(m).rjust(11))
print("-" * 26)
total = sum(m for _, m in data)
print("Total".ljust(15) + str(total).rjust(11))
print("Percentage".ljust(15) + "{:.2f}%".format(total / 3).rjust(11))
''', (),
       r"""<ul><li><code>strip()</code> removes spaces (or the given characters) from both ends; <code>lstrip()</code> from the left; <code>rstrip()</code> from the right.</li>
<li><code>format()</code> fills <code>{}</code> placeholders by position, index or name; <code>{:.3f}</code> formats a float to 3 decimal places.</li>
<li><code>center(w, ch)</code>, <code>ljust(w)</code> and <code>rjust(w)</code> pad a string to width w, which is useful for printing neat tables such as this marksheet.</li></ul>"""),

    PP("py4p9", "Writing a file: write() and writelines()", r'''
f = open("students.txt", "w")
n = f.write("Roll,Name,Marks\n")
print("Characters written:", n)
f.write("1,Amit,78\n")
f.write("2,Riya,85\n")
f.close()

lines = ["3,Om,69\n", "4,Kavya,91\n"]
with open("students.txt", "a") as f:
    f.writelines(lines)

with open("cities.txt", "w") as f:
    for city in ["Surat", "Ahmedabad", "Rajkot"]:
        f.write(city + "\n")
print("Files written successfully")
''', (),
       r"""<ul><li>Mode <b>"w"</b> creates the file, or <b>erases</b> it if it already exists.</li>
<li><code>write(str)</code> writes one string and returns the number of characters written. It does <b>not</b> add a newline; you must write <code>"\n"</code> yourself.</li>
<li><code>writelines(list)</code> writes every string of a list; again, no newlines are added automatically.</li>
<li>Calling <code>close()</code>, or using <code>with</code>, saves the data to disk.</li></ul>""",
       show_files=["students.txt", "cities.txt"]),

    PP("py4p10", "Reading a file: read(), read(n), readline(), readlines(), loop", r'''
with open("notes.txt", "w") as f:
    f.write("Python\nis easy\nBye")

f = open("notes.txt", "r")
print("read():", repr(f.read()))
f.close()

with open("notes.txt") as f:
    print("read(4):", repr(f.read(4)))
    print("rest   :", repr(f.read()))

with open("notes.txt") as f:
    print("readline():", repr(f.readline()))
    print("readline():", repr(f.readline()))
    print("readline():", repr(f.readline()))
    print("at end    :", repr(f.readline()))

with open("notes.txt") as f:
    print("readlines():", f.readlines())

print("Loop over file:")
with open("notes.txt") as f:
    for no, line in enumerate(f, start=1):
        print(f"  {no}: {line.rstrip()}")
''', (),
       r"""<ul><li><code>read()</code> returns the whole file as one string; <code>read(n)</code> returns the next n characters.</li>
<li><code>readline()</code> returns one line <b>including</b> its "\n"; at the end of the file it returns an empty string "".</li>
<li><code>readlines()</code> returns a <b>list</b> of all lines.</li>
<li>Looping <code>for line in f</code> reads one line at a time, which is best for big files. <code>rstrip()</code> removes the trailing newline.</li>
<li>Each read moves the file pointer forward, so after <code>read(4)</code> the next read continues from the 5th character.</li></ul>"""),

    PP("py4p11", "Appending to a file (mode 'a')", r'''
with open("diary.txt", "w") as f:
    f.write("Day 1: Learned lists\n")

with open("diary.txt", "a") as f:
    f.write("Day 2: Learned tuples\n")

entry = input("Enter today's entry: ")
with open("diary.txt", "a") as f:
    f.write("Day 3: " + entry + "\n")

with open("diary.txt") as f:
    print("File now contains:")
    print(f.read(), end="")

with open("diary.txt", "w") as f:
    f.write("Overwritten!\n")
with open("diary.txt") as f:
    print("After 'w' again:", f.read(), end="")
''', ["Learned file handling"],
       r"""<ul><li>Python has no <code>append()</code> method for files: appending means opening the file in mode <b>"a"</b>. New data is added at the <b>end</b> and the old data is kept. The file is created if it does not exist.</li>
<li>Opening an existing file in mode <b>"w"</b> erases all of its old content, as the last part of the output shows.</li></ul>"""),

    PP("py4p12", "File programs: count lines, words, characters; copy a file", r'''
lines = words = chars = 0
with open("story.txt") as f:
    for line in f:
        lines += 1
        words += len(line.split())
        chars += len(line)
print("Lines     :", lines)
print("Words     :", words)
print("Characters:", chars)

with open("story.txt") as f:
    text = f.read()
print("'Python' occurs", text.count("Python"), "times")

with open("story.txt") as src, open("copy.txt", "w") as dst:
    for line in src:
        dst.write(line.upper())
print("Copied in uppercase to copy.txt")

try:
    open("missing.txt")
except FileNotFoundError as e:
    print("Error:", e)
''', (),
       r"""<p>The program reads <i>story.txt</i> line by line: each line adds 1 to the line count, <code>len(line.split())</code> to the word count and <code>len(line)</code> (including "\n") to the character count. It then copies the file into <i>copy.txt</i> in uppercase. Two files can be opened in one <code>with</code> statement. Opening a missing file for reading raises <b>FileNotFoundError</b>.</p>""",
       files={"story.txt": STORY}, show_files=["copy.txt"]),

    PP("py4p13", "User-defined function: definition and calling", r'''
def welcome():
    """Prints a welcome message."""
    print("Welcome to Python functions!")


def area_circle(r):
    return 3.14159 * r * r


def is_even(n):
    return n % 2 == 0


welcome()                         # call without arguments
a = area_circle(5)                # call with an argument
print("Area of circle (r=5):", round(a, 2))
print("Area (r=2.5):", round(area_circle(2.5), 2))
for x in [4, 7]:
    print(x, "is even?", is_even(x))
print("Docstring:", welcome.__doc__)
print("Type:", type(welcome).__name__)
''', (),
       r"""<ul><li>A function is <b>defined</b> with <code>def name(parameters):</code> followed by an indented body. It runs only when it is <b>called</b> by name with brackets.</li>
<li><code>return</code> sends a value back to the caller, and that value can be stored, printed or used in expressions.</li>
<li>The string in triple quotes just after the def line is the <b>docstring</b>, available as <code>name.__doc__</code>.</li>
<li>A function must be defined <b>before</b> it is called.</li></ul>"""),

    PP("py4p14", "Passing parameters: positional, keyword, default, *args, **kwargs", r'''
def student(name, branch, sem):
    print(f"  {name} | {branch} | Sem {sem}")

print("Positional:")
student("Amit", "CE", 2)
print("Keyword (any order):")
student(sem=2, name="Riya", branch="IT")


def power(base, exp=2):           # default parameter
    return base ** exp

print("Default: power(5) =", power(5), " power(2, 10) =", power(2, 10))


def total(*nums):                 # variable-length
    print("  nums =", nums)
    return sum(nums)

print("*args:", total(1, 2), total(5, 10, 15, 20))


def profile(**info):              # keyword variable-length
    for k, v in info.items():
        print(f"  {k}: {v}")

print("**kwargs:")
profile(name="Om", city="Surat", cpi=8.4)

try:
    student("Kavya", "CE")
except TypeError as e:
    print("Error:", e)
''', (),
       r"""<ul><li><b>Positional</b> arguments are matched by order; <b>keyword</b> arguments by name (order does not matter).</li>
<li>A <b>default</b> parameter (<code>exp=2</code>) is used when no argument is given. Default parameters must come after non-default ones.</li>
<li><code>*args</code> collects any number of positional arguments into a <b>tuple</b>; <code>**kwargs</code> collects keyword arguments into a <b>dictionary</b>.</li>
<li>Missing a required argument raises TypeError.</li></ul>"""),

    PP("py4p15", "Returning values: single, multiple, None; passing a list", r'''
def stats(nums):
    return min(nums), max(nums), sum(nums) / len(nums)


def grade(p):
    if p >= 70:
        return "Distinction"
    if p >= 60:
        return "First class"
    return "Pass"


def show(msg):
    print(msg)                # no return statement


def add_bonus(marks):
    for i in range(len(marks)):
        marks[i] += 5         # changes caller's list


m = [62, 75, 88]
lo, hi, avg = stats(m)        # multiple values (a tuple)
print("Min:", lo, "Max:", hi, "Avg:", round(avg, 2))
print("stats() returns:", stats(m))
print("Grade:", grade(avg))
r = show("Hello")
print("show() returned:", r)
add_bonus(m)
print("After add_bonus:", m)


def change(x):
    x = 100                   # new local value only

n = 5
change(n)
print("n after change():", n)
''', (),
       r"""<ul><li><code>return</code> ends the function and sends a value back. Several values separated by commas are returned as a <b>tuple</b>, which can be unpacked.</li>
<li>A function can have several return statements; the first one that runs ends the function.</li>
<li>A function with no return statement returns <b>None</b>.</li>
<li>Arguments are passed by object reference: a <b>mutable</b> object (a list) can be changed inside the function, but giving a parameter a new value (x = 100) does not affect the caller's variable.</li></ul>"""),

    PP("py4p16", "Recursion: factorial, Fibonacci, sum of digits, power", r'''
def fact(n):
    if n == 0 or n == 1:      # base case
        return 1
    return n * fact(n - 1)    # recursive case


def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)


def digit_sum(n):
    if n == 0:
        return 0
    return n % 10 + digit_sum(n // 10)


def power(x, y):
    if y == 0:
        return 1
    return x * power(x, y - 1)


num = int(input("Enter a number: "))
print(f"{num}! =", fact(num))
print("Fibonacci:", [fib(i) for i in range(num + 3)])
print("Digit sum of 98765 =", digit_sum(98765))
print("power(2, 10) =", power(2, 10))


def no_base(n):
    return no_base(n - 1)

try:
    no_base(5)
except RecursionError as e:
    print("Error:", e)
''', ["5"],
       r"""<ul><li>A <b>recursive function</b> calls itself. Each call works on a smaller problem until the <b>base case</b> is reached, which returns a value without another call.</li>
<li>fact(5) = 5 × fact(4) = 5 × 4 × fact(3) … = 120 (see diagram "Recursion: fact(4)").</li>
<li>Without a base case, the calls never stop and Python raises a <b>RecursionError</b> (the default limit is about 1000 calls).</li>
<li>Recursion gives short, clear code for problems like factorial, Fibonacci and Tower of Hanoi, but uses more memory than a loop.</li></ul>"""),

    PP("py4p17", "Scope of variables: local, global and the global keyword", r'''
college = "GTU"                  # global variable
count = 0                        # global variable


def show():
    city = "Surat"               # local variable
    print("Inside show():", college, city)


def increment():
    global count                 # use the global count
    count += 1


def shadow():
    college = "Local college"    # new local, same name
    print("Inside shadow():", college)


show()
increment()
increment()
print("count after 2 calls:", count)
shadow()
print("Global college:", college)

try:
    print(city)
except NameError as e:
    print("NameError:", e)


def wrong():
    count += 1                   # no global statement

try:
    wrong()
except UnboundLocalError as e:
    print("UnboundLocalError:", e)
''', (),
       r"""<ul><li>A <b>local variable</b> is created inside a function and exists only while the function runs; using it outside gives a NameError.</li>
<li>A <b>global variable</b> is created outside all functions and can be <b>read</b> anywhere.</li>
<li>To <b>change</b> a global variable inside a function, declare it with the <code>global</code> keyword. Without it, assigning (<code>count += 1</code>) makes Python treat count as local, giving <b>UnboundLocalError</b>.</li>
<li>A local variable with the same name as a global one hides (shadows) the global inside that function.</li></ul>"""),

    PP("py4p18", "Employee details management using functions and a dictionary (project)", r'''
employees = {}


def add_employee(eid, name, dept, salary):
    employees[eid] = {"name": name, "dept": dept, "salary": salary}


def show_all():
    print(f"{'ID':<5}{'Name':<10}{'Dept':<8}{'Salary':>8}")
    for eid, e in employees.items():
        print(f"{eid:<5}{e['name']:<10}{e['dept']:<8}{e['salary']:>8}")


def give_raise(dept, percent):
    for e in employees.values():
        if e["dept"] == dept:
            e["salary"] = round(e["salary"] * (1 + percent / 100))


def search(name):
    for eid, e in employees.items():
        if e["name"].lower() == name.lower():
            return eid, e
    return None


def save(filename):
    with open(filename, "w") as f:
        for eid, e in employees.items():
            f.write(f"{eid},{e['name']},{e['dept']},{e['salary']}\n")


add_employee(1, "Amit", "IT", 30000)
add_employee(2, "Riya", "HR", 28000)
add_employee(3, "Om", "IT", 35000)
n = int(input("How many more employees? "))
for i in range(n):
    data = input("id name dept salary: ").split()
    add_employee(int(data[0]), data[1], data[2], int(data[3]))

show_all()
give_raise("IT", 10)
print("After 10% raise for IT:")
show_all()
print("Search 'riya':", search("riya"))
print("Search 'Dev' :", search("Dev"))
save("employees.txt")
print("Saved to employees.txt")
''', ["1", "4 Kavya Sales 32000"],
       r"""<p>Suggested project 4 from the syllabus. Each task is a separate <b>user-defined function</b>: add, show, raise salary, search and save. The data is a <b>dictionary of dictionaries</b> (employee id → details). <code>search()</code> returns a tuple when it finds the name and None when it does not. <code>save()</code> uses file handling to write the records as comma-separated lines.</p>""",
       show_files=["employees.txt"]),
]

if __name__ == "__main__":
    for p in PROGRAMS:
        print("=" * 20, p["id"], p["title"]["en"]); print(p["out"])
