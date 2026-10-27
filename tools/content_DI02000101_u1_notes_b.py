"""DI02000101 Unit 1 notes part B: 1.3 Data types – number, string, list, tuple, set, dictionary."""
from py_content import make_TP

SN = {
    "num_ex": r'''
a = 100              # int (no size limit)
big = 2 ** 100       # 1267650600228229401496703205376
b = 3.75             # float
c = 3 + 4j           # complex
print(c.real, c.imag, abs(c))    # 3.0 4.0 5.0
d = True             # bool (subtype of int)
print(True + True)   # 2
''',
    "str_create": r'''
s1 = 'Python'
s2 = "GTU's Diploma"          # ' inside " "
s3 = """Multi
line string"""
s4 = str(123)                 # '123'
empty = ""
''',
    "str_ops": r'''
s = "PYTHON"
s[0]        # 'P'      first
s[-1]       # 'N'      last
s[1:4]      # 'YTH'    slicing
"Py" + "thon"   # 'Python'  concatenation
"Hi " * 3       # 'Hi Hi Hi '  repetition
"TH" in s       # True     membership
len(s)          # 6
''',
    "str_immut": r'''
s = "Python"
s[0] = "J"         # TypeError: immutable
s = "J" + s[1:]    # 'Jython' – a new string
''',
    "list_ex": r'''
marks = [78, 85, 62]          # create
mixed = [1, "two", 3.5, True]
empty = []
marks[0]          # 78     access
marks[1] = 90     # update -> [78, 90, 62]
marks.append(70)  # add    -> [78, 90, 62, 70]
del marks[2]      # delete -> [78, 90, 70]
len(marks)        # 3
''',
    "tuple_ex": r'''
t = (10, 20, 30)          # create
t2 = 1, 2, 3              # parentheses optional
one = (5,)                # single item: comma needed
t[0]          # 10       access
t[1:]         # (20, 30)
t[0] = 99     # TypeError: immutable
del t         # whole tuple can be deleted
''',
    "set_ex": r'''
s = {3, 1, 2, 3}         # {1, 2, 3} duplicates removed
e = set()                # empty set ({} is a dict!)
s.add(5)                 # add
s.remove(1)              # delete (error if missing)
s.discard(9)             # delete (no error)
2 in s                   # True
s[0]                     # TypeError: not subscriptable
''',
    "dict_ex": r'''
d = {"roll": 101, "name": "Amit"}   # create
d["name"]            # 'Amit'   access by key
d.get("city", "-")   # '-'      safe access
d["sem"] = 2         # add new pair
d["name"] = "Riya"   # update
del d["roll"]        # delete a pair
d.keys()   d.values()   d.items()
''',
    "mutable": r'''
lst = [1, 2, 3]
lst[0] = 10          # allowed: list is mutable
tup = (1, 2, 3)
tup[0] = 10          # TypeError: tuple is immutable
''',
}
T = make_TP(SN)

SEC_1_3 = {
    "title": {"en": "1.3 Data Types in Python"},
    "items": [
        T("1.3.1 Introduction to Data Types",
          r"""<p>A <b>data type</b> tells what kind of value a variable holds and which operations can be done on it. In Python, <b>everything is an object</b>, and every value has a type (a class). The type is found with <code>type()</code>.</p>
<table>
<tr><th>Category</th><th>Types</th><th>Example</th></tr>
<tr><td>Numeric</td><td>int, float, complex</td><td>10, 3.14, 2+3j</td></tr>
<tr><td>Boolean</td><td>bool</td><td>True, False</td></tr>
<tr><td>Sequence</td><td>str, list, tuple (and range)</td><td>"GTU", [1, 2], (1, 2)</td></tr>
<tr><td>Set</td><td>set, frozenset</td><td>{1, 2, 3}</td></tr>
<tr><td>Mapping</td><td>dict</td><td>{"a": 1}</td></tr>
<tr><td>None type</td><td>NoneType</td><td>None</td></tr>
</table>
<h4>Mutable and immutable types</h4>
<ul><li><b>Mutable</b> (can be changed after creation): <b>list, set, dict</b>.</li>
<li><b>Immutable</b> (cannot be changed): <b>int, float, complex, bool, str, tuple, frozenset</b>.</li></ul>
@@mutable@@
<p><b>Declaration and use:</b> Python has no separate declaration. A variable gets its type when a value is assigned, e.g. <code>x = 5</code> (int) or <code>x = [5]</code> (list).</p>""",
          diagram="py1_datatypes", programs=["py1p7"]),

        T("1.3.2 Numbers: int, float, complex (and bool)",
          r"""<ul>
<li><b>int:</b> whole numbers, positive or negative, with <b>no size limit</b> (limited only by memory). They can be written in decimal, binary (0b), octal (0o) or hexadecimal (0x).</li>
<li><b>float:</b> real numbers with a decimal point or in exponent form, e.g. 3.14 or 1.5e3. Accurate to about 15–17 significant digits, which is why 145/3 prints as 48.333333333333336.</li>
<li><b>complex:</b> numbers of the form <b>a + bj</b>, where j = √−1. Use <code>.real</code> and <code>.imag</code> to get the parts.</li>
<li><b>bool:</b> True or False. bool is a subtype of int: True = 1 and False = 0.</li></ul>
@@num_ex@@""",
          programs=["py1p3"]),

        T("1.3.3 String (str)",
          r"""<p>A <b>string</b> is an <b>ordered, immutable sequence of characters</b> enclosed in single, double or triple quotes. Python has no separate char type; a single character is a string of length 1.</p>
<h4>Declaration</h4>
@@str_create@@
<h4>Accessing and basic operations</h4>
<p>Each character has an <b>index</b>: positive from 0 (left to right) and negative from −1 (right to left). <b>Slicing</b> <code>s[start:end:step]</code> extracts part of a string; the end index is excluded (see diagram).</p>
@@str_ops@@
<h4>Immutability</h4>
@@str_immut@@
<p>String methods such as <code>upper()</code>, <code>lower()</code>, <code>replace()</code>, <code>find()</code> and <code>split()</code> are covered in Unit 4.</p>""",
          diagram="py1_string_index", programs=["py1p10"]),

        T("1.3.4 List",
          r"""<p>A <b>list</b> is an <b>ordered, mutable</b> collection of items written in <b>square brackets [ ]</b> and separated by commas.</p>
<ul><li>It can contain items of <b>different types</b>, and <b>duplicates</b> are allowed.</li>
<li>Items are accessed by index (0, 1, … or −1, −2, …) and slicing.</li>
<li>Items can be added, changed and removed after creation.</li></ul>
@@list_ex@@
<p>Uses: a collection of marks, names or any items that may change. Lists are covered in detail in Unit 3.</p>""",
          programs=["py1p11"]),

        T("1.3.5 Tuple",
          r"""<p>A <b>tuple</b> is an <b>ordered, immutable</b> collection of items written in <b>parentheses ( )</b>.</p>
<ul><li>Like a list it is indexed and allows duplicates and mixed types, but its items <b>cannot be changed, added or removed</b>.</li>
<li>A single-item tuple needs a trailing comma: <code>(5,)</code>. Without the comma, <code>(5)</code> is just the int 5.</li>
<li>It is faster and uses less memory than a list, and it can be used as a dictionary key.</li></ul>
@@tuple_ex@@
<p>Uses: fixed data such as days of the week, (x, y) coordinates or RGB colours.</p>""",
          programs=["py1p12"]),

        T("1.3.6 Set",
          r"""<p>A <b>set</b> is an <b>unordered</b> collection of <b>unique</b> items written in <b>curly braces { }</b>.</p>
<ul><li><b>No duplicates:</b> repeated values are stored only once.</li>
<li><b>No indexing or slicing</b>, because there is no fixed order.</li>
<li>The set itself is mutable (items can be added or removed), but its items must be immutable (numbers, strings, tuples).</li>
<li>An empty set is created with <code>set()</code>; <code>{}</code> creates an empty dictionary.</li>
<li>It supports mathematical set operations: union <code>|</code>, intersection <code>&amp;</code>, difference <code>-</code>, symmetric difference <code>^</code>.</li>
<li><b>frozenset</b> is an immutable version of a set.</li></ul>
@@set_ex@@
<p>Uses: removing duplicates, membership testing, finding common items.</p>""",
          programs=["py1p12"]),

        T("1.3.7 Dictionary (dict)",
          r"""<p>A <b>dictionary</b> is a <b>mutable</b> collection of <b>key: value pairs</b> written in <b>curly braces { }</b>. Values are accessed by <b>key</b>, not by index.</p>
<ul><li>Keys must be <b>unique</b> and <b>immutable</b> (str, int, tuple); values can be of any type and may repeat.</li>
<li>It keeps insertion order (from Python 3.7).</li>
<li>Assigning to a new key adds a pair; assigning to an existing key updates its value.</li></ul>
@@dict_ex@@
<p>Uses: records (student details), word counts, phone books, configuration settings.</p>""",
          programs=["py1p13"]),

        T("1.3.8 Comparison: List, Tuple, Set and Dictionary",
          r"""<table>
<tr><th>Property</th><th>List</th><th>Tuple</th><th>Set</th><th>Dictionary</th></tr>
<tr><td>Brackets</td><td>[ ]</td><td>( )</td><td>{ }</td><td>{key: value}</td></tr>
<tr><td>Ordered</td><td>Yes</td><td>Yes</td><td>No</td><td>Yes (3.7+)</td></tr>
<tr><td>Mutable</td><td>Yes</td><td>No</td><td>Yes</td><td>Yes</td></tr>
<tr><td>Duplicates</td><td>Allowed</td><td>Allowed</td><td>Not allowed</td><td>Keys unique</td></tr>
<tr><td>Indexing</td><td>By position</td><td>By position</td><td>Not possible</td><td>By key</td></tr>
<tr><td>Empty</td><td>[] or list()</td><td>() or tuple()</td><td>set()</td><td>{} or dict()</td></tr>
<tr><td>Example</td><td>[1, 2, 2]</td><td>(1, 2, 2)</td><td>{1, 2}</td><td>{"a": 1}</td></tr>
<tr><td>Use</td><td>Changing collection</td><td>Fixed data</td><td>Unique items</td><td>Key-based lookup</td></tr>
</table>""",
          diagram="py1_collections"),

        T("Key Points – 1.3",
          r"""<ul>
<li>Everything in Python is an object; <code>type()</code> gives its class.</li>
<li>Numeric: int (unlimited size), float, complex (a+bj); bool is a subtype of int (True = 1).</li>
<li>str: immutable, ordered sequence of characters; indexing from 0 and −1; slicing [start:end:step] with end excluded.</li>
<li>list [ ]: ordered, mutable, allows duplicates.</li>
<li>tuple ( ): ordered, immutable; single item needs a comma: (5,).</li>
<li>set { }: unordered, unique items, no indexing; empty set = set().</li>
<li>dict {k: v}: key-value pairs; keys unique and immutable; empty dict = {}.</li>
<li>Mutable: list, set, dict. Immutable: int, float, complex, bool, str, tuple, frozenset.</li>
</ul>""", key=True),
    ],
}

NOTES_B = [SEC_1_3]
