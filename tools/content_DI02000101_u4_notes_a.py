"""DI02000101 Unit 4 notes part A: 4.1 Built-in functions (conversion, math, string)."""
from py_content import make_TP

SN = {
    "builtin_ex": r'''
print("Hi")        # output
len("Python")      # 6
type(10)           # <class 'int'>
max(4, 9, 2)       # 9
''',
    "int_f": r'''
int("25")          # 25
int(9.99)          # 9   (truncates)
int(-7.8)          # -7
int("1010", 2)     # 10  (base 2)
int("ff", 16)      # 255 (base 16)
int(True)          # 1
int("12.5")        # ValueError
int(float("12.5")) # 12
''',
    "float_f": r'''
float(7)           # 7.0
float("3.75")      # 3.75
float("1e3")       # 1000.0
float("abc")       # ValueError
''',
    "str_f": r'''
str(25)            # '25'
str(3.5)           # '3.5'
"Age: " + str(18)  # 'Age: 18'
"Age: " + 18       # TypeError
''',
    "bool_f": r'''
bool(0)      # False
bool(0.0)    # False
bool("")     # False
bool([])     # False
bool(None)   # False
bool(-5)     # True
bool("0")    # True  (non-empty)
bool(" ")    # True
''',
    "complex_f": r'''
complex(2, 3)      # (2+3j)
complex(4)         # (4+0j)
complex("1-2j")    # (1-2j)
z = complex(3, 4)
z.real, z.imag     # (3.0, 4.0)
''',
    "coll_conv": r'''
list("abc")          # ['a', 'b', 'c']
list((1, 2))         # [1, 2]
list(range(3))       # [0, 1, 2]
tuple([1, 2])        # (1, 2)
set([1, 1, 2])       # {1, 2}
frozenset("aab")     # {'a', 'b'} frozen
dict([("a", 1)])     # {'a': 1}
dict(x=1, y=2)       # {'x': 1, 'y': 2}
dict(zip("ab", [1, 2]))  # {'a': 1, 'b': 2}
list({"a": 1})       # ['a'] (keys)
''',
    "bytes_f": r'''
b = bytes("Hi", "utf-8")  # b'Hi'
b[0]                      # 72
bytes([65, 66])           # b'AB'
bytes(3)                  # b'\x00\x00\x00'
b[0] = 74                 # TypeError
ba = bytearray(b"Hi")
ba[0] = 74         # bytearray(b'Ji')
ba.decode()               # 'Ji'
''',
    "abs_round": r'''
abs(-7)            # 7
abs(-2.5)          # 2.5
abs(3 + 4j)        # 5.0
round(3.14159, 2)  # 3.14
round(7.6)         # 8
round(2.5)         # 2  (to even)
round(3.5)         # 4
round(1234, -2)    # 1200
''',
    "pow_divmod": r'''
pow(2, 5)          # 32   (2 ** 5)
pow(2, -1)         # 0.5
pow(2, 5, 3)       # 2    (32 % 3)
divmod(17, 5)      # (3, 2)
divmod(-17, 5)     # (-4, 3)
q, r = divmod(125, 60)  # 2, 5
''',
    "sum_min_max": r'''
sum([1, 2, 3])          # 6
sum([1, 2, 3], 10)      # 16
min(4, 9, 2)            # 2
max([4, 9, 2])          # 9
max("python")           # 'y'
max(["ox", "tiger"], key=len)  # 'tiger'
min([])                 # ValueError
''',
    "str_len": r'''
s = "Hello World"
len(s)        # 11 (space counted)
max(s)        # 'r'
min(s)        # ' ' (space)
min("Python") # 'P' (uppercase first)
''',
    "str_is": r'''
"Py3".isalnum()      # True
"Py 3".isalnum()     # False (space)
"Python".isalpha()   # True
"2024".isdigit()     # True
"12.5".isdigit()     # False
"abc".islower()      # True
"ABC1".isupper()     # True
"  \t\n".isspace()   # True
"my_var".isidentifier()  # True
"2var".isidentifier()    # False
"".isalpha()         # False (empty)
''',
    "str_find": r'''
s = "banana"
s.find("an")        # 1
s.rfind("an")       # 3
s.find("x")         # -1
s.find("a", 2)      # 3  (search from 2)
s.index("x")        # ValueError
s.count("a")        # 3
s.count("ana")      # 1 (no overlap)
s.startswith("ba")  # True
s.endswith("na")    # True
"a.py".endswith((".py", ".c"))  # True
''',
    "str_case": r'''
s = "pYTHON is FUN"
s.capitalize()  # 'Python is fun'
s.lower()       # 'python is fun'
s.upper()       # 'PYTHON IS FUN'
s.title()       # 'Python Is Fun'
s.swapcase()    # 'Python IS fun'
''',
    "str_replace": r'''
s = "I like C. C is fast."
s.replace("C", "Python")
# 'I like Python. Python is fast.'
s.replace("C", "Java", 1)
# 'I like Java. C is fast.'
''',
    "str_strip": r'''
s = "   hello   "
s.strip()           # 'hello'
s.lstrip()          # 'hello   '
s.rstrip()          # '   hello'
"##hi##".strip("#") # 'hi'
"www.gtu.ac.in".lstrip("w.")  # 'gtu.ac.in'
''',
    "str_format": r'''
"{} is {} years".format("Om", 18)
# 'Om is 18 years'
"{1} {0}".format("A", "B") # 'B A'
"{n}-{m}".format(n="Py", m=9)  # 'Py-9'
"{:.2f}".format(3.14159) # '3.14'
"{:5d}|".format(42)     # '   42|'
"{:<6}|".format("ab")   # 'ab    |'
"{:^6}|".format("ab")   # '  ab  |'
"{:,}".format(1234567)  # '1,234,567'
''',
    "fstring": r'''
name, m = "Riya", 85.456
f"{name} scored {m:.1f}"
# 'Riya scored 85.5'
''',
    "str_align": r'''
"Py".center(8)        # '   Py   '
"Py".center(8, "*")   # '***Py***'
"Py".ljust(6, ".")    # 'Py....'
"Py".rjust(6, ".")    # '....Py'
"7".rjust(3, "0")     # '007'
''',
}
T = make_TP(SN)

SEC_4_1 = {
    "title": {"en": "4.1 Built-in Functions"},
    "items": [
        T("4.1.1 Introduction to Functions and Built-in Functions",
          r"""<p>A <b>function</b> is a named block of code that performs a specific task. It can take inputs (arguments) and give back a result (return value). Functions make programs shorter, reusable and easier to understand.</p>
<h4>Types of functions in Python</h4>
<ol><li><b>Built-in functions</b> are ready-made functions that come with Python and are always available without any import: <code>print()</code>, <code>input()</code>, <code>len()</code>, <code>type()</code>, <code>int()</code>, <code>max()</code>, etc.</li>
<li><b>User-defined functions</b> are written by the programmer using the <code>def</code> keyword (topic 4.3).</li>
<li>(Functions from <b>modules</b>, such as <code>math.sqrt()</code>, are covered in Unit 5.)</li></ol>
@@builtin_ex@@
<h4>Built-in functions in this unit</h4>
<ul><li><b>Type / data conversion:</b> int(), float(), str(), bool(), complex(), list(), tuple(), dict(), set(), frozenset(), bytes(), bytearray()</li>
<li><b>Math:</b> abs(), round(), pow(), divmod(), sum(), min(), max()</li>
<li><b>String:</b> len(), max(), min() and string methods such as isalpha(), find(), upper(), strip(), format(), center()</li>
<li><b>File:</b> open(), read(), readline(), readlines(), write(), writelines()</li></ul>
<p><b>Function vs method:</b> a function is called on its own, <code>len(s)</code>; a method belongs to an object and is called with a dot, <code>s.upper()</code>.</p>""",
          diagram="py4_func_types", programs=["py4p13"]),

        T("4.1.2 Type Conversion Functions: int(), float(), str(), bool(), complex()",
          r"""<p><b>Type conversion</b> (type casting) means changing a value from one data type to another. Python does it in two ways:</p>
<ul><li><b>Implicit conversion</b>: done automatically by Python, e.g. <code>3 + 2.5 = 5.5</code> (the int becomes a float).</li>
<li><b>Explicit conversion</b>: done by the programmer using conversion functions.</li></ul>
<h4>int(x [, base])</h4>
<p>Converts a number or a string of digits to an integer. A float is truncated (the decimal part is cut off). The optional base converts from binary, octal or hexadecimal.</p>
@@int_f@@
<h4>float(x)</h4>
@@float_f@@
<h4>str(x)</h4>
<p>Converts any value into a string. It is needed for joining numbers with text.</p>
@@str_f@@
<h4>bool(x)</h4>
<p>Returns False for "empty" or zero values (0, 0.0, "", [], (), {}, set(), None) and True for everything else.</p>
@@bool_f@@
<h4>complex(real [, imag])</h4>
@@complex_f@@""",
          diagram="py4_conversion", programs=["py4p1"]),

        T("4.1.3 Collection Conversion: list(), tuple(), set(), frozenset(), dict()",
          r"""<table>
<tr><th>Function</th><th>Converts to</th><th>Notes</th></tr>
<tr><td>list(iterable)</td><td>List</td><td>Mutable, ordered</td></tr>
<tr><td>tuple(iterable)</td><td>Tuple</td><td>Immutable, ordered</td></tr>
<tr><td>set(iterable)</td><td>Set</td><td>Removes duplicates, unordered</td></tr>
<tr><td>frozenset(iterable)</td><td>Frozen set</td><td>Immutable set</td></tr>
<tr><td>dict(pairs / kwargs)</td><td>Dictionary</td><td>Needs key-value pairs</td></tr>
</table>
@@coll_conv@@
<ul><li>An <b>iterable</b> is any object that can be looped over: string, list, tuple, set, dict, range, file.</li>
<li>Called with no argument, each function returns an empty object: <code>list()</code> → [], <code>dict()</code> → {}.</li></ul>""",
          programs=["py4p2"]),

        T("4.1.4 bytes() and bytearray()",
          r"""<p>Computers store all data as <b>bytes</b> (numbers from 0 to 255). Python has two byte types:</p>
<table>
<tr><th>bytes()</th><th>bytearray()</th></tr>
<tr><td>Immutable sequence of bytes</td><td>Mutable sequence of bytes</td></tr>
<tr><td>Literal: b'Hi'</td><td>bytearray(b'Hi')</td></tr>
<tr><td>Items cannot be changed</td><td>Items can be changed, appended, removed</td></tr>
</table>
<h4>Ways to create</h4>
<ul><li><code>bytes("text", "utf-8")</code>: from a string, with an encoding.</li>
<li><code>bytes([65, 66])</code>: from a list of integers 0–255.</li>
<li><code>bytes(n)</code>: n zero bytes.</li></ul>
@@bytes_f@@
<p>Indexing a bytes object gives an <b>integer</b> (the byte value). <code>decode()</code> converts bytes back to a string, and <code>str.encode()</code> converts a string to bytes. They are used for binary files (images, audio) and network communication.</p>""",
          programs=["py4p3"]),

        T("4.1.5 Math Functions: abs(), round(), pow(), divmod(), sum(), min(), max()",
          r"""<table>
<tr><th>Function</th><th>Description</th><th>Example</th><th>Result</th></tr>
<tr><td>abs(x)</td><td>Absolute value</td><td>abs(-7)</td><td>7</td></tr>
<tr><td>round(x[, n])</td><td>Round to n decimal places</td><td>round(3.146, 2)</td><td>3.15</td></tr>
<tr><td>pow(x, y[, z])</td><td>x<sup>y</sup> (mod z)</td><td>pow(2, 3)</td><td>8</td></tr>
<tr><td>divmod(a, b)</td><td>(quotient, remainder)</td><td>divmod(17, 5)</td><td>(3, 2)</td></tr>
<tr><td>sum(iter[, start])</td><td>Total of the items</td><td>sum([1, 2, 3])</td><td>6</td></tr>
<tr><td>min(…)</td><td>Smallest item</td><td>min(4, 9, 2)</td><td>2</td></tr>
<tr><td>max(…)</td><td>Largest item</td><td>max([4, 9, 2])</td><td>9</td></tr>
</table>
<h4>abs() and round()</h4>
@@abs_round@@
<p>round() uses <b>banker's rounding</b>: an exact .5 goes to the nearest <b>even</b> number. A negative n rounds to tens, hundreds, etc.</p>
<h4>pow() and divmod()</h4>
@@pow_divmod@@
<h4>sum(), min(), max()</h4>
@@sum_min_max@@
<p>min() and max() accept either one iterable or several separate values. The optional <code>key</code> argument decides what to compare.</p>""",
          programs=["py4p4"]),

        T("4.1.6 String Functions: len(), max(), min() and Testing Methods",
          r"""<h4>len(), max(), min() on strings</h4>
@@str_len@@
<p>max() and min() compare characters by their <b>Unicode (ASCII) values</b>: space &lt; digits &lt; uppercase letters &lt; lowercase letters.</p>
<h4>String testing methods (return True / False)</h4>
<table>
<tr><th>Method</th><th>Returns True if the string…</th></tr>
<tr><td>isalnum()</td><td>contains only letters and digits</td></tr>
<tr><td>isalpha()</td><td>contains only letters</td></tr>
<tr><td>isdigit()</td><td>contains only digits</td></tr>
<tr><td>islower()</td><td>has letters and all of them are lowercase</td></tr>
<tr><td>isupper()</td><td>has letters and all of them are uppercase</td></tr>
<tr><td>isspace()</td><td>contains only whitespace (space, \t, \n)</td></tr>
<tr><td>isidentifier()</td><td>is a valid Python identifier (variable name)</td></tr>
</table>
@@str_is@@
<p>All of these return <b>False for an empty string</b>. They are commonly used to validate input: checking a mobile number, a password or a name.</p>""",
          diagram="py4_str_is", programs=["py4p5"]),

        T("4.1.7 Searching Methods: find(), rfind(), count(), startswith(), endswith()",
          r"""<table>
<tr><th>Method</th><th>Description</th></tr>
<tr><td>find(sub[, start[, end]])</td><td>Index of the first occurrence of sub; −1 if not found</td></tr>
<tr><td>rfind(sub)</td><td>Index of the last occurrence; −1 if not found</td></tr>
<tr><td>count(sub)</td><td>Number of non-overlapping occurrences</td></tr>
<tr><td>startswith(prefix)</td><td>True if the string begins with prefix</td></tr>
<tr><td>endswith(suffix)</td><td>True if the string ends with suffix</td></tr>
</table>
@@str_find@@
<ul><li><b>find() vs index():</b> both return the position, but index() raises <b>ValueError</b> when the substring is missing, while find() returns −1.</li>
<li>startswith() and endswith() also accept a tuple of options.</li></ul>""",
          programs=["py4p6"]),

        T("4.1.8 Case Conversion and replace(): capitalize(), lower(), upper(), title(), swapcase()",
          r"""<table>
<tr><th>Method</th><th>Action</th><th>"hello WORLD" →</th></tr>
<tr><td>capitalize()</td><td>First character upper, rest lower</td><td>'Hello world'</td></tr>
<tr><td>lower()</td><td>All letters lowercase</td><td>'hello world'</td></tr>
<tr><td>upper()</td><td>All letters uppercase</td><td>'HELLO WORLD'</td></tr>
<tr><td>title()</td><td>First letter of each word upper</td><td>'Hello World'</td></tr>
<tr><td>swapcase()</td><td>Lower ↔ upper</td><td>'HELLO world'</td></tr>
</table>
@@str_case@@
<h4>replace(old, new[, count])</h4>
<p>Returns a copy of the string in which <i>old</i> is replaced by <i>new</i>, either everywhere or only the first <i>count</i> times.</p>
@@str_replace@@
<p><b>Remember:</b> strings are <b>immutable</b>, so these methods never change the original string; they return a new string. Use <code>s = s.upper()</code> to keep the result.</p>""",
          programs=["py4p7"]),

        T("4.1.9 Strip and Formatting Methods: strip(), format(), center(), ljust(), rjust()",
          r"""<h4>strip(), lstrip(), rstrip()</h4>
<p>These remove whitespace (or the characters given as an argument) from both ends, the left end or the right end of a string. Characters in the middle are never removed.</p>
@@str_strip@@
<h4>format()</h4>
<p><code>"template".format(values)</code> replaces each <code>{}</code> placeholder with a value. Placeholders can use a position <code>{0}</code>, a name <code>{name}</code> and a format specification after a colon: <code>.2f</code> (2 decimals), <code>5d</code> (width 5), <code>&lt;</code> left, <code>&gt;</code> right, <code>^</code> centre, <code>,</code> thousands separator.</p>
@@str_format@@
<p>The modern <b>f-string</b> uses the same format codes:</p>
@@fstring@@
<h4>center(), ljust(), rjust()</h4>
<p><code>center(width[, fill])</code>, <code>ljust(width[, fill])</code> and <code>rjust(width[, fill])</code> pad the string to the given width with spaces (or the fill character).</p>
@@str_align@@""",
          diagram="py4_align", programs=["py4p8"]),

        T("Key Points – 4.1",
          r"""<ul>
<li>Built-in functions are always available; user-defined functions are created with def.</li>
<li>int() truncates floats and accepts a base: int("1010", 2) = 10; int("12.5") → ValueError.</li>
<li>bool() is False for 0, 0.0, "", [], (), {}, set(), None; otherwise True (even "0").</li>
<li>list(), tuple(), set(), frozenset() and dict() convert between collections; dict() needs pairs.</li>
<li>bytes is immutable and bytearray is mutable; decode() turns bytes into a string.</li>
<li>round(2.5) = 2 (rounds to even); divmod(a, b) = (a // b, a % b); pow(x, y, z) = x<sup>y</sup> % z.</li>
<li>The is…() methods test strings and return False for "".</li>
<li>find()/rfind() return −1 if not found; count() counts occurrences.</li>
<li>capitalize, lower, upper, title, swapcase and replace return new strings.</li>
<li>strip/lstrip/rstrip trim the ends; format(), center(), ljust() and rjust() format output.</li>
</ul>""", key=True),
    ],
}

NOTES_A = [SEC_4_1]
