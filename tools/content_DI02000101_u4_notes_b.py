"""DI02000101 Unit 4 notes part B: 4.2 File handling, 4.3 User-defined functions."""
from py_content import make_TP

SN = {
    "open_syntax": r'''
f = open("data.txt", "r")    # read
f = open("data.txt", "w")    # write
f = open("data.txt", "a")    # append
f = open("pic.jpg", "rb")    # binary
f = open("C:/py/data.txt")   # full path
''',
    "file_attr": r'''
f = open("data.txt", "w")
f.name      # 'data.txt'
f.mode      # 'w'
f.closed    # False
f.close()
f.closed    # True
''',
    "close_ex": r'''
f = open("data.txt", "w")
f.write("Hello")
f.close()          # must close
''',
    "with_ex": r'''
with open("data.txt", "r") as f:
    data = f.read()
# file closed automatically here
print(data)
''',
    "read_all": r'''
with open("notes.txt") as f:
    s = f.read()       # whole file
with open("notes.txt") as f:
    s = f.read(10)     # first 10 chars
''',
    "readline_ex": r'''
with open("notes.txt") as f:
    l1 = f.readline()  # 'Python\n'
    l2 = f.readline()  # 'is easy\n'
''',
    "readlines_ex": r'''
with open("notes.txt") as f:
    lines = f.readlines()
# ['Python\n', 'is easy\n', 'Bye']
print(len(lines))      # 3 lines
''',
    "loop_ex": r'''
with open("notes.txt") as f:
    for line in f:
        print(line.rstrip())
''',
    "while_readline": r'''
f = open("notes.txt")
line = f.readline()
while line != "":
    print(line, end="")
    line = f.readline()
f.close()
''',
    "write_ex": r'''
with open("out.txt", "w") as f:
    n = f.write("Line 1\n")  # n = 7
    f.write("Line 2\n")
    f.write(str(100) + "\n")  # str only
''',
    "writelines_ex": r'''
names = ["Amit\n", "Riya\n", "Om\n"]
with open("names.txt", "w") as f:
    f.writelines(names)
# newlines must be in the strings
''',
    "append_ex": r'''
with open("log.txt", "a") as f:
    f.write("New entry\n")   # at end
''',
    "tell_seek": r'''
with open("notes.txt") as f:
    f.read(3)
    print(f.tell())   # 3 (position)
    f.seek(0)         # back to start
    print(f.read(6))  # 'Python'
''',
    "file_exc": r'''
try:
    f = open("marks.txt")
except FileNotFoundError:
    print("File does not exist")
''',
    "count_ex": r'''
lines = words = chars = 0
with open("story.txt") as f:
    for line in f:
        lines += 1
        words += len(line.split())
        chars += len(line)
''',
    "why_func": r'''
# without function: repeated code
print("=" * 20)
print("=" * 20)
# with function: write once, call often
def line():
    print("=" * 20)
line()
line()
''',
    "def_syntax": r'''
def function_name(parameters):
    """docstring (optional)"""
    statements
    return value     # optional
''',
    "def_ex": r'''
def greet(name):
    """Greets a person."""
    print("Hello,", name)

greet("Riya")        # Hello, Riya
greet("Om")          # Hello, Om
''',
    "pass_ex": r'''
def todo():
    pass             # empty function
''',
    "pos_kw": r'''
def info(name, age):
    print(name, age)

info("Om", 18)          # positional
info(age=18, name="Om") # keyword
''',
    "default_ex": r'''
def power(b, e=2):
    return b ** e

power(5)       # 25 (e = 2)
power(2, 3)    # 8
# def f(a=1, b):  -> SyntaxError
''',
    "args_ex": r'''
def total(*nums):     # nums is a tuple
    return sum(nums)

total(1, 2)           # 3
total(1, 2, 3, 4)     # 10
''',
    "kwargs_ex": r'''
def show(**d):        # d is a dict
    for k, v in d.items():
        print(k, "=", v)

show(name="Om", sem=2)
''',
    "order_ex": r'''
def f(a, b=2, *args, **kwargs):
    print(a, b, args, kwargs)

f(1, 3, 4, 5, x=9)
# 1 3 (4, 5) {'x': 9}
''',
    "ret_single": r'''
def square(n):
    return n * n

y = square(4) + 1     # 17
''',
    "ret_multi": r'''
def calc(a, b):
    return a + b, a - b, a * b

s, d, p = calc(7, 3)  # 10 4 21
r = calc(7, 3)        # (10, 4, 21)
''',
    "ret_none": r'''
def hello():
    print("Hi")

x = hello()   # prints Hi
print(x)      # None
''',
    "ret_early": r'''
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
''',
    "mut_arg": r'''
def add_item(lst):
    lst.append(99)   # changes caller's

a = [1, 2]
add_item(a)
print(a)              # [1, 2, 99]
''',
    "rec_fact": r'''
def fact(n):
    if n == 0:             # base case
        return 1
    return n * fact(n - 1) # recursive case

fact(5)   # 120
''',
    "rec_fib": r'''
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)

[fib(i) for i in range(8)]
# [0, 1, 1, 2, 3, 5, 8, 13]
''',
    "rec_sum": r'''
def sum_n(n):            # 1 + 2 + ... + n
    if n == 0:
        return 0
    return n + sum_n(n - 1)

def rev(s):              # reverse string
    if s == "":
        return ""
    return rev(s[1:]) + s[0]
''',
    "local_ex": r'''
def f():
    x = 10       # local
    print(x)

f()              # 10
print(x)         # NameError
''',
    "global_ex": r'''
rate = 5         # global

def interest(p):
    return p * rate / 100   # read global

interest(1000)   # 50.0
''',
    "global_kw": r'''
count = 0

def inc():
    global count
    count += 1

inc(); inc()
print(count)     # 2
''',
    "shadow": r'''
x = "global"

def f():
    x = "local"  # new local variable
    print(x)     # local

f()
print(x)         # global
''',
    "lambda_ex": r'''
square = lambda x: x * x
square(5)                  # 25
add = lambda a, b: a + b
add(2, 3)                  # 5
w = ["bb", "a", "ccc"]
sorted(w, key=lambda s: len(s))
# ['a', 'bb', 'ccc']
''',
}
T = make_TP(SN)

SEC_4_2 = {
    "title": {"en": "4.2 File Handling Functions"},
    "items": [
        T("4.2.1 Introduction to Files and open() Function",
          r"""<p>A <b>file</b> is a named location on the disk that stores data <b>permanently</b>. Variables are lost when a program ends, but data written to a file can be used again later.</p>
<h4>Types of files</h4>
<ul><li><b>Text files</b> store readable characters, organised in lines that end with "\n" (.txt, .csv, .py).</li>
<li><b>Binary files</b> store data as bytes that only programs can interpret (.jpg, .mp3, .exe, .dat).</li></ul>
<h4>open() function</h4>
<p><code>file_object = open(file_name, mode)</code> opens a file and returns a <b>file object</b> (file handle) that is used for reading or writing. The mode is optional and defaults to "r".</p>
@@open_syntax@@
<table>
<tr><th>Mode</th><th>Meaning</th></tr>
<tr><td>"r"</td><td>Read only (default). Error if the file does not exist.</td></tr>
<tr><td>"w"</td><td>Write. Creates the file, or erases the old content if it exists.</td></tr>
<tr><td>"a"</td><td>Append. Writes at the end, keeps the old content, creates the file if needed.</td></tr>
<tr><td>"x"</td><td>Create a new file. Error if it already exists.</td></tr>
<tr><td>"r+"</td><td>Read and write (the file must exist).</td></tr>
<tr><td>"w+" / "a+"</td><td>Write/append and also read.</td></tr>
<tr><td>"b" / "t"</td><td>Binary / text (default), added to the above: "rb", "wb".</td></tr>
</table>
<h4>File object attributes</h4>
@@file_attr@@""",
          diagram="py4_file_modes", programs=["py4p9"]),

        T("4.2.2 Closing a File and the with Statement",
          r"""<p>File handling always follows three steps: <b>open → read/write → close</b>.</p>
<p><code>close()</code> saves (flushes) any data still in memory to the disk and frees the file for other programs. If a file is not closed, written data may be lost.</p>
@@close_ex@@
<h4>with statement (recommended)</h4>
<p><code>with open(...) as f:</code> opens the file and <b>closes it automatically</b> when the indented block ends, even if an error occurs. No close() call is needed.</p>
@@with_ex@@""",
          diagram="py4_file_flow", programs=["py4p9", "py4p10"]),

        T("4.2.3 Reading Functions: read(), readline(), readlines()",
          r"""<table>
<tr><th>Function</th><th>Returns</th><th>Use</th></tr>
<tr><td>read()</td><td>The whole file as one string</td><td>Small files</td></tr>
<tr><td>read(n)</td><td>The next n characters</td><td>Reading in parts</td></tr>
<tr><td>readline()</td><td>The next line (with "\n"); "" at end of file</td><td>Line by line</td></tr>
<tr><td>readlines()</td><td>A list of all lines</td><td>Counting / indexing lines</td></tr>
</table>
<h4>read()</h4>
@@read_all@@
<h4>readline()</h4>
@@readline_ex@@
<h4>readlines()</h4>
@@readlines_ex@@
<h4>Looping over a file object (most efficient)</h4>
@@loop_ex@@
<h4>Reading until the end with readline()</h4>
@@while_readline@@
<p>Each read moves the <b>file pointer</b> forward. <code>tell()</code> gives the current position and <code>seek(pos)</code> moves the pointer:</p>
@@tell_seek@@""",
          diagram="py4_read_methods", programs=["py4p10"]),

        T("4.2.4 Writing Functions: write() and writelines()",
          r"""<table>
<tr><th>write(string)</th><th>writelines(list_of_strings)</th></tr>
<tr><td>Writes one string</td><td>Writes every string of a list/iterable</td></tr>
<tr><td>Returns the number of characters written</td><td>Returns None</td></tr>
<tr><td>Does not add "\n"</td><td>Does not add "\n"</td></tr>
</table>
@@write_ex@@
@@writelines_ex@@
<ul><li>Only <b>strings</b> can be written to a text file; numbers must be converted with str().</li>
<li>The file must be opened in "w", "a", "x" or a "+" mode; writing to a file opened with "r" raises an error.</li></ul>""",
          programs=["py4p9"]),

        T("4.2.5 Appending Data to a File",
          r"""<p>To add new data <b>without deleting</b> the existing content, open the file in <b>append mode "a"</b>. All writing then happens at the <b>end</b> of the file. (The syllabus calls this "append()"; in Python it is done with mode "a" and then write()/writelines().)</p>
@@append_ex@@
<table>
<tr><th>Mode "w"</th><th>Mode "a"</th></tr>
<tr><td>Erases the old content</td><td>Keeps the old content</td></tr>
<tr><td>Writing starts at the beginning</td><td>Writing starts at the end</td></tr>
<tr><td>Creates the file if missing</td><td>Creates the file if missing</td></tr>
</table>""",
          programs=["py4p11"]),

        T("4.2.6 File Programs and Error Handling",
          r"""<h4>Count lines, words and characters</h4>
@@count_ex@@
<h4>Handling a missing file</h4>
<p>Opening a missing file in "r" mode raises <b>FileNotFoundError</b>. It can be handled with try-except:</p>
@@file_exc@@
<p>Other common file programs: copying a file, converting a file to uppercase, counting vowels, searching for a word, and storing student records as comma-separated lines.</p>""",
          programs=["py4p12", "py4p18"]),

        T("Key Points – 4.2",
          r"""<ul>
<li>Files store data permanently; there are text files and binary files.</li>
<li><code>open(name, mode)</code>: "r" read (default), "w" write (erases), "a" append, "x" create, "+" read and write, "b" binary.</li>
<li>Steps: open → read/write → close; <code>with open(...) as f:</code> closes the file automatically.</li>
<li>read() → whole string; read(n) → n characters; readline() → one line; readlines() → list of lines.</li>
<li>write(str) returns the number of characters; writelines(list) writes many strings; neither adds "\n".</li>
<li>Append = open in "a" mode; the old data is kept.</li>
<li>tell() gives the position and seek() moves it; a missing file in "r" mode → FileNotFoundError.</li>
</ul>""", key=True),
    ],
}

SEC_4_3 = {
    "title": {"en": "4.3 User-defined Functions"},
    "items": [
        T("4.3.1 Introduction to User-defined Functions",
          r"""<p>A <b>user-defined function</b> is a function written by the programmer to perform a specific task. It is defined once with the <code>def</code> keyword and can be called many times.</p>
@@why_func@@
<h4>Advantages of functions</h4>
<ol><li><b>Code reusability:</b> write once, use many times.</li>
<li><b>Modularity:</b> a big program is divided into small, manageable parts.</li>
<li><b>Easy debugging and testing:</b> each function can be checked separately.</li>
<li><b>Readability:</b> meaningful function names make the code self-explanatory.</li>
<li><b>Less code:</b> no repetition, so programs are shorter and easier to maintain.</li></ol>""",
          diagram="py4_func_types", programs=["py4p13"]),

        T("4.3.2 Function Definition and Function Calling",
          r"""<h4>Function definition</h4>
@@def_syntax@@
<ol><li>It starts with the keyword <b>def</b>, followed by the function name and brackets ( ).</li>
<li><b>Parameters</b> (if any) are written inside the brackets, separated by commas.</li>
<li>The header ends with a colon <b>:</b>.</li>
<li>The body is <b>indented</b>. The first statement may be a <b>docstring</b> describing the function.</li>
<li><b>return</b> (optional) sends a value back to the caller.</li></ol>
<h4>Function calling</h4>
<p>A function runs only when it is <b>called</b>: its name followed by brackets containing the <b>arguments</b>. Control jumps to the function, the body runs, and control comes back to the statement after the call.</p>
@@def_ex@@
<ul><li><b>Parameter</b>: the variable in the function definition (name). <b>Argument</b>: the actual value passed in the call ("Riya").</li>
<li>A function must be defined before it is called, or a NameError occurs.</li>
<li>An empty function body uses <code>pass</code>:</li></ul>
@@pass_ex@@""",
          diagram="py4_func_anatomy", programs=["py4p13"]),

        T("4.3.3 Passing Parameters to a Function",
          r"""<p>Python supports four kinds of arguments:</p>
<h4>1. Positional arguments</h4>
<p>Values are matched to parameters by their <b>order</b>. The number of arguments must match the number of parameters.</p>
<h4>2. Keyword arguments</h4>
<p>Values are passed as <code>name=value</code>, so the order does not matter.</p>
@@pos_kw@@
<h4>3. Default arguments</h4>
<p>A parameter can have a default value, which is used when no argument is given. Default parameters must come <b>after</b> non-default parameters.</p>
@@default_ex@@
<h4>4. Variable-length arguments</h4>
<ul><li><code>*args</code> accepts any number of positional arguments and stores them in a <b>tuple</b>.</li>
<li><code>**kwargs</code> accepts any number of keyword arguments and stores them in a <b>dictionary</b>.</li></ul>
@@args_ex@@
@@kwargs_ex@@
<p>Order when they are combined: normal → default → *args → **kwargs.</p>
@@order_ex@@""",
          programs=["py4p14"]),

        T("4.3.4 Returning Values from a Function",
          r"""<p>The <b>return</b> statement ends the function and sends a value back to the caller. The returned value can be stored in a variable, printed or used in an expression.</p>
<h4>Returning a single value</h4>
@@ret_single@@
<h4>Returning multiple values</h4>
<p>Values separated by commas are returned as a <b>tuple</b>, which can be unpacked into separate variables.</p>
@@ret_multi@@
<h4>Function without return</h4>
<p>If there is no return statement (or just <code>return</code>), the function returns <b>None</b>.</p>
@@ret_none@@
<h4>Several return statements</h4>
<p>The first return that executes ends the function immediately.</p>
@@ret_early@@
<h4>Passing mutable objects</h4>
<p>Python passes a reference to the object. A list or dictionary changed inside the function is changed for the caller too; assigning a new value to a parameter does not affect the caller.</p>
@@mut_arg@@""",
          programs=["py4p15"]),

        T("4.3.5 Recursion",
          r"""<p><b>Recursion</b> is a technique in which a function <b>calls itself</b>. Such a function is called a <b>recursive function</b>. Every recursive function has two parts:</p>
<ol><li><b>Base case</b>: the condition at which the function stops calling itself and returns a value directly.</li>
<li><b>Recursive case</b>: the function calls itself with a smaller or simpler input, moving towards the base case.</li></ol>
<h4>Factorial using recursion</h4>
<p>n! = n × (n−1)!, with 0! = 1! = 1</p>
@@rec_fact@@
<p><b>Working of fact(4):</b> fact(4) = 4 × fact(3) = 4 × 3 × fact(2) = 4 × 3 × 2 × fact(1) = 4 × 3 × 2 × 1 = 24. The calls go down to the base case, and the results then return back up (see diagram).</p>
<h4>Fibonacci using recursion</h4>
@@rec_fib@@
<h4>More examples</h4>
@@rec_sum@@
<table>
<tr><th>Advantages</th><th>Disadvantages</th></tr>
<tr><td>Short, clean code</td><td>Uses more memory (each call is kept on the stack)</td></tr>
<tr><td>Natural for problems such as factorial, Fibonacci, Tower of Hanoi and tree traversal</td><td>Slower than loops; hard to debug</td></tr>
<tr><td>Breaks a big problem into smaller ones</td><td>No base case → RecursionError (limit ≈ 1000 calls)</td></tr>
</table>""",
          diagram="py4_recursion", programs=["py4p16"]),

        T("4.3.6 Scope of Variables: Local and Global",
          r"""<p>The <b>scope</b> of a variable is the part of the program where the variable can be accessed.</p>
<h4>Local variable</h4>
<p>A variable created <b>inside a function</b> is local to it. It exists only while the function runs and cannot be used outside it (NameError).</p>
@@local_ex@@
<h4>Global variable</h4>
<p>A variable created <b>outside all functions</b> is global. It can be <b>read</b> inside any function.</p>
@@global_ex@@
<h4>global keyword</h4>
<p>To <b>change</b> a global variable inside a function, declare it with <code>global</code>. Without it, an assignment creates a local variable, and <code>count += 1</code> raises <b>UnboundLocalError</b>.</p>
@@global_kw@@
<h4>Same name: local hides global</h4>
@@shadow@@
<table>
<tr><th>Local variable</th><th>Global variable</th></tr>
<tr><td>Declared inside a function</td><td>Declared outside all functions</td></tr>
<tr><td>Accessible only in that function</td><td>Accessible throughout the program</td></tr>
<tr><td>Created when the function is called; destroyed when it returns</td><td>Exists until the program ends</td></tr>
<tr><td>Different functions can use the same local name</td><td>Must be declared with <code>global</code> to be changed in a function</td></tr>
</table>
<p>Python searches for a name in the order <b>L</b>ocal → <b>E</b>nclosing → <b>G</b>lobal → <b>B</b>uilt-in (the LEGB rule).</p>""",
          diagram="py4_scope", programs=["py4p17"]),

        T("4.3.7 Lambda Functions and a Complete Example",
          r"""<p>A <b>lambda function</b> is a small <b>anonymous</b> (unnamed) function written in one line: <code>lambda arguments: expression</code>. It can have any number of arguments but only one expression, whose value is returned automatically. Lambdas are often used as the <code>key</code> in sorted(), max() and min().</p>
@@lambda_ex@@
<p>The solved project <b>"Employee details management"</b> brings this unit together: several user-defined functions (add, show, give a raise, search, save), a dictionary of dictionaries for the data, string formatting for the table, and file writing to save the records.</p>""",
          programs=["py4p18"]),

        T("Key Points – 4.3",
          r"""<ul>
<li>Define with <code>def name(params):</code> and an indented body; call with <code>name(args)</code>.</li>
<li>Advantages: reusability, modularity, readability, easier debugging.</li>
<li>Parameter = name in the definition; argument = value in the call.</li>
<li>Argument types: positional, keyword, default (b=2), *args (tuple), **kwargs (dict).</li>
<li>return sends a value back; return a, b returns a tuple; no return → None.</li>
<li>Recursion = a function calling itself; it needs a base case, otherwise RecursionError.</li>
<li>Local variables exist inside the function only; globals can be read anywhere; changing one needs <code>global</code>.</li>
<li>Lambda: <code>lambda x: x * x</code>, a one-expression anonymous function.</li>
</ul>""", key=True),
    ],
}

NOTES_B = [SEC_4_2, SEC_4_3]
