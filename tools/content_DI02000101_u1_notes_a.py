"""DI02000101 Unit 1 notes part A: 1.1 Introduction to Python, 1.2 Basic syntax (keywords, variables, literals, I/O, type casting)."""
from py_content import make_TP

SN = {
    "repl": r'''
>>> 5 + 3
8
>>> print("Hello")
Hello
>>> x = 10
>>> x * 2
20
>>> exit()
''',
    "script": r'''
# hello.py  (save the file, then run)
print("Hello, GTU!")

# Command prompt:
# python hello.py      (Windows)
# python3 hello.py     (Linux / macOS)
''',
    "verify": r'''
C:\> python --version
Python 3.13.0
C:\> pip --version
''',
    "structure": r'''
# Program : Area of a circle      <- documentation
# Author  : Ravi Patel

import math                        # import section

PI = 3.14159                       # global constant

def area(r):                       # function definition
    """Return area of circle."""   # docstring
    return PI * r * r

# main program
r = float(input("Enter radius: "))
print("Area =", area(r))
''',
    "comments": r'''
# This is a single-line comment
x = 5    # inline comment

"""
This is a multi-line string,
often used as a multi-line comment.
"""
''',
    "indent": r'''
if marks >= 35:
    print("Pass")          # 4 spaces = one block
    print("Congratulations")
else:
    print("Fail")
print("Done")              # outside the if block
''',
    "indent_err": r'''
if x > 0:
print("Positive")   # IndentationError: expected an indented block
''',
    "multi_stmt": r'''
a = 5; b = 10; print(a + b)     # ; separates statements

total = 10 + 20 + \
        30 + 40                 # \ continues a line
nums = [1, 2,
        3, 4]                   # inside ( ) [ ] { } no \ needed
''',
    "kw_check": r'''
>>> import keyword
>>> keyword.kwlist          # list of all keywords
>>> keyword.iskeyword("if")
True
''',
    "ident_ex": r'''
# Valid identifiers
roll_no   _count   Sum1   totalMarks   MAX_SIZE

# Invalid identifiers
2nd_sem      # starts with a digit
total marks  # contains a space
my-name      # contains a hyphen
for          # keyword
''',
    "var_ex": r'''
age = 18             # int
height = 5.6         # float
name = "Kavya"       # str
age = "eighteen"     # same name, now a str (dynamic typing)
print(type(age))     # <class 'str'>
''',
    "multi_assign": r'''
a = b = c = 0              # same value to many variables
x, y, z = 10, 20.5, "GTU"  # different values
a, b = b, a                # swap
''',
    "del_var": r'''
x = 100
del x            # deletes the variable
print(x)         # NameError: name 'x' is not defined
''',
    "id_ex": r'''
>>> a = 10
>>> b = a
>>> id(a) == id(b)     # same object
True
>>> a is b
True
''',
    "literal_ex": r'''
# Numeric literals
25    0b11001    0o31    0x19      # int (dec, bin, oct, hex)
3.14  2.5e3                        # float
4 + 3j                             # complex

# String literals
'GTU'   "GTU"   """multi-line"""   r"C:\new"

# Boolean and special literals
True   False   None

# Collection literals
[1, 2]   (1, 2)   {1, 2}   {"a": 1}
''',
    "const_ex": r'''
PI = 3.14159
MAX_STUDENTS = 60
GRAVITY = 9.8
# Python does not stop you changing them,
# so UPPERCASE warns: "do not modify".
''',
    "const_module": r'''
# constants.py
PI = 3.14159
G = 9.8

# main.py
import constants
print(constants.PI)
''',
    "input_ex": r'''
name = input("Enter name: ")          # str
age = int(input("Enter age: "))       # int
per = float(input("Enter %: "))       # float
a, b = input("Two words: ").split()   # two strings
x, y = map(int, input("Two numbers: ").split())
''',
    "print_syn": r'''
print(value1, value2, ..., sep=' ', end='\n', file=sys.stdout)
''',
    "print_ex": r'''
print("A", "B", 5)              # A B 5
print("A", "B", sep="-")        # A-B
print("Hi", end=" ")            # no newline
print("2025", "10", "26", sep="/")   # 2025/10/26
''',
    "format_ex": r'''
name, per = "Riya", 77.333
print("Name:", name, "Per:", per)             # comma
print("Name: %s Per: %.2f" % (name, per))     # % style
print("Name: {} Per: {:.2f}".format(name, per))
print(f"Name: {name} Per: {per:.2f}")         # f-string
print(f"{name:>10}|{per:<8.1f}|")             # width
''',
    "implicit": r'''
a = 10        # int
b = 3.5       # float
c = a + b     # int converted to float
print(c, type(c))     # 13.5 <class 'float'>
print(True + 2)       # 3   (True treated as 1)
''',
    "explicit": r'''
int("25")       # 25
int(9.8)        # 9 (truncates)
float("3.5")    # 3.5
float(7)        # 7.0
str(100)        # '100'
bool(0)         # False
complex(2, 3)   # (2+3j)
int("101", 2)   # 5 (binary to decimal)
''',
    "cast_err": r'''
int("12.5")    # ValueError
int("abc")     # ValueError
"Age: " + 18   # TypeError: can only concatenate str
"Age: " + str(18)   # correct
''',
}
T = make_TP(SN)

SEC_1_1 = {
    "title": {"en": "1.1 Introduction to Python"},
    "items": [
        T("1.1.1 Introduction and History of Python",
          r"""<p><b>Python</b> is a <b>high-level, interpreted, general-purpose</b> programming language known for its simple, readable syntax. It supports procedural, object-oriented and functional programming. It is <b>free and open source</b> and is maintained by the <b>Python Software Foundation (PSF)</b>.</p>
<h4>What is a scripting language?</h4>
<p>A <b>scripting language</b> is a language whose programs (scripts) are executed by an <b>interpreter</b> without a separate compile-and-link step. Scripts are used to automate tasks, glue software components together and build programs quickly. Python, JavaScript, Perl, PHP and shell script are examples. Python is used both as a scripting language and for full-scale applications.</p>
<h4>History</h4>
<ul><li>Python was created by <b>Guido van Rossum</b> at <b>CWI (Centrum Wiskunde &amp; Informatica)</b> in the Netherlands. He started it in December 1989 as a hobby project.</li>
<li>The name comes from the BBC comedy show <b>"Monty Python's Flying Circus"</b>, not from the snake.</li>
<li>It was influenced by the <b>ABC</b> language (and by Modula-3, C and Unix shell).</li>
<li><b>1991</b>: Python 0.9.0 released, with functions, exception handling, modules and core data types.</li>
<li><b>1994</b>: Python 1.0, with lambda, map, filter and reduce.</li>
<li><b>2000</b>: Python 2.0, with list comprehensions, garbage collection and Unicode support.</li>
<li><b>2008</b>: Python 3.0, a cleaned-up version that is <b>not backward compatible</b> with 2.x (e.g. <code>print</code> became a function).</li>
<li><b>2020</b>: Python 2 reached end of life (1 January 2020). Today, all new development uses <b>Python 3</b>.</li>
<li>Guido van Rossum led the language as its "Benevolent Dictator For Life" until 2018. It is now guided by an elected Steering Council.</li></ul>""",
          diagram="py1_history"),

        T("1.1.2 Features of Python",
          r"""<ol>
<li><b>Simple and easy to learn:</b> English-like syntax with few keywords; programs are short and readable.</li>
<li><b>Interpreted:</b> code is executed line by line by the interpreter. There is no separate compilation step, and errors are reported as soon as they are reached.</li>
<li><b>Free and open source:</b> Python can be downloaded, used and distributed freely, and its source code is available.</li>
<li><b>High-level language:</b> the programmer does not manage memory or hardware details; memory is handled automatically (garbage collection).</li>
<li><b>Dynamically typed:</b> variables do not need type declarations; the type is decided at run time from the value.</li>
<li><b>Platform independent (portable):</b> the same program runs on Windows, Linux and macOS without changes.</li>
<li><b>Object-oriented:</b> supports classes, objects, inheritance and polymorphism. Procedural programming is also supported.</li>
<li><b>Large standard library ("batteries included"):</b> ready modules for maths, files, dates, networking, databases and more. Thousands of further packages (NumPy, Matplotlib, Django) are available through <b>pip</b>.</li>
<li><b>Extensible and embeddable:</b> code written in C/C++ can be used in Python, and Python can be embedded in other applications.</li>
<li><b>Interactive mode:</b> statements can be tested immediately at the <code>&gt;&gt;&gt;</code> prompt.</li>
<li><b>GUI and database support:</b> Tkinter for GUIs; connectors for MySQL, SQLite and others.</li>
</ol>
<h4>Limitations</h4>
<ul><li>Slower than compiled languages like C/C++ because it is interpreted.</li>
<li>Uses more memory, and is less common for mobile app development.</li>
<li>Type errors appear only at run time because of dynamic typing.</li></ul>""",
          diagram="py1_features"),

        T("1.1.3 Applications of Python",
          r"""<table>
<tr><th>Area</th><th>Examples / libraries</th></tr>
<tr><td>Web development (server side)</td><td>Django, Flask; Instagram and Pinterest use Django</td></tr>
<tr><td>Data science and analysis</td><td>NumPy, Pandas, Matplotlib</td></tr>
<tr><td>Artificial intelligence and machine learning</td><td>TensorFlow, PyTorch, scikit-learn</td></tr>
<tr><td>Automation and scripting</td><td>renaming files, sending e-mails, web scraping</td></tr>
<tr><td>Desktop GUI applications</td><td>Tkinter, PyQt</td></tr>
<tr><td>Game development</td><td>Pygame</td></tr>
<tr><td>Scientific and numeric computing</td><td>SciPy, SymPy</td></tr>
<tr><td>Networking and cyber security</td><td>socket programming, penetration-testing tools</td></tr>
<tr><td>Embedded systems and IoT</td><td>Raspberry Pi, MicroPython</td></tr>
<tr><td>Software development tools</td><td>build and testing tools (SCons, pytest)</td></tr>
<tr><td>Education</td><td>first programming language in many schools and colleges</td></tr>
<tr><td>Blockchain and big data</td><td>smart-contract tools, PySpark</td></tr>
</table>
<p>Companies using Python include Google, YouTube, NASA, Netflix, Spotify and Dropbox.</p>"""),

        T("1.1.4 Installing and Running Python",
          r"""<h4>Installation steps (Windows)</h4>
<ol><li>Open <b>www.python.org</b> → Downloads → download the latest Python 3 installer.</li>
<li>Run the installer and <b>tick "Add python.exe to PATH"</b> (important).</li>
<li>Click <b>Install Now</b>. This installs the interpreter, <b>IDLE</b> (Python's built-in editor) and <b>pip</b> (the package installer).</li>
<li>Verify in the Command Prompt:</li></ol>
@@verify@@
<p>On Linux, Python 3 is usually pre-installed (<code>python3</code>), or it can be installed with <code>sudo apt install python3</code>.</p>
<h4>Ways to run Python code</h4>
<p><b>1. Interactive mode (REPL: Read–Evaluate–Print Loop):</b> type <code>python</code> in the command prompt or open IDLE. Each statement is executed immediately after Enter. It is useful for testing small pieces of code, but the code is not saved.</p>
@@repl@@
<p><b>2. Script mode:</b> write the program in a file with the <b>.py</b> extension and run the whole file. The code is saved and can be reused.</p>
@@script@@
<table><tr><th>Interactive mode</th><th>Script mode</th></tr>
<tr><td>Statement executed immediately</td><td>Whole file executed</td></tr>
<tr><td>Code is not saved</td><td>Code saved in a .py file</td></tr>
<tr><td>Good for testing and as a calculator</td><td>Good for complete programs</td></tr>
<tr><td>Prompt: &gt;&gt;&gt;</td><td>No prompt</td></tr></table>
<p><b>IDEs and editors:</b> IDLE, VS Code, PyCharm, Spyder, Jupyter Notebook. Online: programiz.com, onlinegdb.com.</p>
<h4>How a Python program is executed (see diagram)</h4>
<ol><li>The <b>source code</b> (.py) is first compiled by the Python compiler into <b>byte code</b> (.pyc files, stored in the __pycache__ folder).</li>
<li>The byte code is executed by the <b>Python Virtual Machine (PVM)</b>, the interpreter.</li>
<li>This happens automatically. Because the byte code is platform independent, Python programs are portable.</li></ol>
<p>The standard implementation, written in C, is called <b>CPython</b>. Other implementations include Jython (Java) and PyPy.</p>""",
          diagram="py1_exec"),

        T("1.1.5 Basic Structure of a Python Program",
          r"""<p>A Python program may contain the following sections (see diagram). Only the executable statements are compulsory.</p>
<ol><li><b>Documentation section:</b> comments giving the program name, author and purpose.</li>
<li><b>Import section:</b> <code>import</code> statements to use modules (math, random, …).</li>
<li><b>Global declarations:</b> global variables and constants.</li>
<li><b>Function / class definitions:</b> user-defined functions with <code>def</code> and classes.</li>
<li><b>Main program:</b> statements that are executed: input, processing, output.</li></ol>
@@structure@@
<h4>Comments</h4>
@@comments@@
<p><code>#</code> starts a single-line comment. Python has no special multi-line comment, but a triple-quoted string that is not assigned to anything is often used as one. A triple-quoted string written just after a function header is a <b>docstring</b> (documentation string).</p>
<h4>Indentation</h4>
<p>Python uses <b>indentation</b> (spaces at the start of a line), not braces <code>{ }</code>, to mark a <b>block</b> of code. All statements in a block must have the <b>same indentation</b>; 4 spaces is the standard. A colon <code>:</code> starts a new block.</p>
@@indent@@
@@indent_err@@
<h4>Statements and lines</h4>
@@multi_stmt@@
<ul><li>No semicolon is needed at the end of a statement; a newline ends it.</li>
<li>Python is <b>case-sensitive</b>: <code>Print</code> and <code>print</code> are different.</li></ul>""",
          diagram="py1_structure", programs=["py1p1"]),

        T("Key Points – 1.1",
          r"""<ul>
<li>Python: high-level, interpreted, dynamically typed, object-oriented, free and open source.</li>
<li>Created by <b>Guido van Rossum</b> (CWI, Netherlands), started in 1989 and released in 1991; named after Monty Python.</li>
<li>Python 3.0 (2008) is not backward compatible; Python 2 ended in 2020.</li>
<li>Applications: web (Django), data science (NumPy, Pandas), AI/ML, automation, GUI, games, IoT.</li>
<li>Interactive mode (&gt;&gt;&gt;, not saved) vs script mode (.py file).</li>
<li>Execution: source → byte code (.pyc) → PVM.</li>
<li>Indentation marks blocks; <code>#</code> starts a comment; no semicolons needed; case-sensitive.</li>
</ul>""", key=True),
    ],
}

SEC_1_2 = {
    "title": {"en": "1.2 Keywords, Variables, Literals, I/O and Type Casting"},
    "items": [
        T("1.2.1 Keywords and Identifiers",
          r"""<h4>Keywords</h4>
<p><b>Keywords</b> are <b>reserved words</b> with a predefined meaning. They cannot be used as variable, function or class names. Python 3.13 has <b>35 keywords</b>; all are lowercase except <b>True, False and None</b>.</p>
<table>
<tr><th>Category</th><th>Keywords</th></tr>
<tr><td>Values</td><td>True, False, None</td></tr>
<tr><td>Operators</td><td>and, or, not, in, is</td></tr>
<tr><td>Control flow</td><td>if, elif, else, for, while, break, continue, pass</td></tr>
<tr><td>Functions and classes</td><td>def, return, lambda, class, yield, global, nonlocal</td></tr>
<tr><td>Modules</td><td>import, from, as</td></tr>
<tr><td>Exception handling</td><td>try, except, finally, raise, assert</td></tr>
<tr><td>Others</td><td>del, with, async, await</td></tr>
</table>
@@kw_check@@
<h4>Identifiers</h4>
<p>An <b>identifier</b> is the name given to a variable, function, class or module.</p>
<p><b>Rules for identifiers:</b></p>
<ol><li>May contain letters (a–z, A–Z), digits (0–9) and underscore (_).</li>
<li>Must <b>not start with a digit</b>.</li>
<li>No spaces or special symbols (@, $, %, -, etc.).</li>
<li>Must not be a keyword.</li>
<li>They are <b>case-sensitive</b>: <code>Total</code>, <code>total</code> and <code>TOTAL</code> are different.</li>
<li>Any length is allowed.</li></ol>
@@ident_ex@@
<p><b>Conventions:</b> variables and functions in lowercase_with_underscores (<code>total_marks</code>); constants in UPPERCASE (<code>PI</code>); classes in CapitalWords (<code>Student</code>). A name starting with an underscore indicates internal use.</p>""",
          programs=["py1p14"]),

        T("1.2.2 Variables",
          r"""<p>A <b>variable</b> is a name that <b>refers to a value (object) stored in memory</b>. In Python a variable is created when a value is first assigned to it; there is <b>no declaration statement</b>.</p>
@@var_ex@@
<h4>Characteristics</h4>
<ul><li><b>Dynamic typing:</b> the type is taken from the value, and the same variable can later refer to a value of another type.</li>
<li>A variable is actually a <b>reference</b> to an object. <code>b = a</code> makes both names refer to the <b>same object</b> (see diagram).</li>
<li>Every object has an identity (<code>id()</code>), a type (<code>type()</code>) and a value.</li>
<li>Using a variable before assigning it gives a <b>NameError</b>.</li></ul>
@@id_ex@@
<h4>Multiple assignment</h4>
@@multi_assign@@
<h4>Deleting a variable</h4>
@@del_var@@""",
          diagram="py1_variables", programs=["py1p6"]),

        T("1.2.3 Literals",
          r"""<p>A <b>literal</b> is a <b>raw value written directly</b> in a program, e.g. <code>25</code>, <code>3.14</code>, <code>"GTU"</code>.</p>
<table>
<tr><th>Type of literal</th><th>Examples</th></tr>
<tr><td><b>Integer</b></td><td>Decimal 25, binary 0b11001, octal 0o31, hexadecimal 0x19</td></tr>
<tr><td><b>Float</b></td><td>3.14, -0.5, 2.5e3 (= 2500.0), 1.5E-2</td></tr>
<tr><td><b>Complex</b></td><td>4+3j, 2j (real + imaginary part with j)</td></tr>
<tr><td><b>String</b></td><td>'single', "double", &#39;&#39;&#39;triple&#39;&#39;&#39;, &quot;&quot;&quot;multi-line&quot;&quot;&quot;, raw r"C:\new"</td></tr>
<tr><td><b>Boolean</b></td><td>True (1), False (0)</td></tr>
<tr><td><b>Special</b></td><td>None (absence of value)</td></tr>
<tr><td><b>Collection</b></td><td>list [1, 2], tuple (1, 2), set {1, 2}, dict {"a": 1}</td></tr>
</table>
@@literal_ex@@
<ul><li>Escape sequences in strings: <code>\n</code> newline, <code>\t</code> tab, <code>\\</code> backslash, <code>\'</code> and <code>\"</code> quotes.</li>
<li>Underscores can be used in numeric literals for readability: <code>1_00_000</code>.</li></ul>""",
          programs=["py1p15"]),

        T("1.2.4 Constants",
          r"""<p>A <b>constant</b> is a value that should not change while the program runs. Python has <b>no const keyword</b>. By convention, constants are written in <b>UPPERCASE</b> letters, and programmers agree not to modify them.</p>
@@const_ex@@
<p>Constants are often placed in a separate module and imported:</p>
@@const_module@@
<p>Built-in constants include <code>True</code>, <code>False</code> and <code>None</code>. The math module provides <code>math.pi</code> (3.14159…) and <code>math.e</code> (2.71828…).</p>
<table><tr><th>Literal</th><th>Constant</th></tr>
<tr><td>A raw value written in the code</td><td>A named value that should not change</td></tr>
<tr><td>3.14159</td><td>PI = 3.14159</td></tr></table>""",
          programs=["py1p4"]),

        T("1.2.5 Input and Output Functions: input() and print()",
          r"""<h4>input()</h4>
<p><code>variable = input("prompt")</code> displays the prompt, waits for the user to type a line and press Enter, and <b>returns the text as a string (str)</b>. To use the input as a number, convert it with <code>int()</code> or <code>float()</code>.</p>
@@input_ex@@
<ul><li><code>split()</code> breaks the input line at spaces into a list of strings.</li>
<li><code>map(int, …)</code> applies <code>int()</code> to every item.</li></ul>
<h4>print()</h4>
@@print_syn@@
<ul><li>Prints one or more values separated by <b>sep</b> (default a space) and finishes with <b>end</b> (default newline <code>'\n'</code>).</li>
<li><b>file</b> sends the output to a file instead of the screen.</li></ul>
@@print_ex@@
<h4>Formatting output</h4>
@@format_ex@@
<table><tr><th>Specifier</th><th>Meaning</th></tr>
<tr><td>%d / %f / %s</td><td>integer / float / string (old % style)</td></tr>
<tr><td>{:.2f}</td><td>2 decimal places</td></tr>
<tr><td>{:10} {:&lt;10} {:&gt;10} {:^10}</td><td>width 10: default / left / right / centre</td></tr>
<tr><td>{:,}</td><td>thousands separator: 1,00,000 → 100,000</td></tr></table>""",
          diagram="py1_io", programs=["py1p2", "py1p3", "py1p16"]),

        T("1.2.6 Type Casting (Type Conversion)",
          r"""<p><b>Type conversion</b> means changing a value from one data type to another. There are two types (see diagram).</p>
<h4>1. Implicit type conversion</h4>
<p>Done <b>automatically</b> by Python when different numeric types are mixed in an expression. The smaller type is converted to the larger type so that no data is lost: <b>bool → int → float → complex</b>.</p>
@@implicit@@
<h4>2. Explicit type conversion (type casting)</h4>
<p>Done <b>by the programmer</b> using built-in functions: <code>target_type(value)</code>.</p>
<table>
<tr><th>Function</th><th>Converts to</th><th>Example</th></tr>
<tr><td>int(x)</td><td>integer (truncates decimals)</td><td>int("25") → 25, int(9.8) → 9</td></tr>
<tr><td>float(x)</td><td>floating point</td><td>float("3.5") → 3.5</td></tr>
<tr><td>str(x)</td><td>string</td><td>str(100) → '100'</td></tr>
<tr><td>bool(x)</td><td>True / False</td><td>bool(0) → False</td></tr>
<tr><td>complex(a, b)</td><td>complex number</td><td>complex(2, 3) → (2+3j)</td></tr>
<tr><td>list(x), tuple(x), set(x)</td><td>collections</td><td>list("ab") → ['a', 'b']</td></tr>
<tr><td>dict(x)</td><td>dictionary</td><td>dict([("a", 1)]) → {'a': 1}</td></tr>
<tr><td>int(s, base)</td><td>int from a base-2/8/16 string</td><td>int("101", 2) → 5</td></tr>
</table>
@@explicit@@
<h4>Errors in conversion</h4>
@@cast_err@@
<table><tr><th>Implicit</th><th>Explicit</th></tr>
<tr><td>Done automatically by Python</td><td>Done by the programmer</td></tr>
<tr><td>No data loss</td><td>Data may be lost (int(9.8) → 9)</td></tr>
<tr><td>Only between compatible numeric types</td><td>Between any convertible types</td></tr></table>""",
          diagram="py1_typecasting", programs=["py1p8", "py1p5", "py1p9"]),

        T("Key Points – 1.2",
          r"""<ul>
<li>35 keywords (Python 3.13); True, False and None are capitalised. Keywords cannot be identifiers.</li>
<li>Identifier: letters, digits and _; not starting with a digit; no spaces or symbols; case-sensitive.</li>
<li>Variables are created by assignment; they are references to objects; dynamically typed.</li>
<li>Literals: integer (dec/bin/oct/hex), float, complex, string, boolean, None, collections.</li>
<li>Constants use UPPERCASE by convention (no const keyword).</li>
<li><code>input()</code> always returns str; convert it with int()/float(). <code>print(sep=, end=)</code>.</li>
<li>Implicit conversion is automatic (int → float); explicit conversion uses int(), float(), str(), bool(), etc.</li>
</ul>""", key=True),
    ],
}

NOTES_A = [SEC_1_1, SEC_1_2]
