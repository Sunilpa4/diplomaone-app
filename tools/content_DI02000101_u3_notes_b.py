"""DI02000101 Unit 3 notes part B: 3.3 Sets, 3.4 Dictionaries."""
from py_content import make_TP

SN = {
    "set_create": r'''
s = {10, 20, 30}           # set
s2 = {1, 2, 2, 3, 3}       # {1, 2, 3}
mixed = {1, "a", 2.5, (1, 2)}
empty = set()              # empty set
not_set = {}               # empty DICT!
s3 = set([1, 2, 2, 3])     # from list
s4 = set("hello")   # {'h','e','l','o'}
bad = {1, [2, 3]}          # TypeError
''',
    "set_access": r'''
s = {10, 20, 30}
s[0]            # TypeError
for x in s:     # loop (any order)
    print(x)
20 in s         # True
50 not in s     # True
''',
    "set_add": r'''
s = {1, 2}
s.add(3)            # {1, 2, 3}
s.add(2)            # no change
s.update([4, 5])    # {1, 2, 3, 4, 5}
s.update("ab")      # adds 'a', 'b'
s |= {9}            # same as update
''',
    "set_delete": r'''
s = {1, 2, 3, 4, 5}
s.remove(3)     # {1, 2, 4, 5}
s.remove(9)     # KeyError
s.discard(9)    # no error
x = s.pop()     # removes ANY item
s.clear()       # set()
del s           # set deleted
''',
    "set_ops": r'''
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
A | B     # {1, 2, 3, 4, 5, 6} union
A & B     # {3, 4}             intersection
A - B     # {1, 2}             difference
B - A     # {5, 6}
A ^ B     # {1, 2, 5, 6}  symmetric diff
''',
    "set_meth_ops": r'''
A.union(B)
A.intersection(B)
A.difference(B)
A.symmetric_difference(B)
A.intersection_update(B)  # A = A & B
A.difference_update(B)    # A = A - B
''',
    "set_rel": r'''
X = {1, 2}
Y = {1, 2, 3}
X <= Y             # True  subset
X.issubset(Y)      # True
Y >= X             # True  superset
Y.issuperset(X)    # True
X < Y              # True  proper subset
X.isdisjoint({7})  # True  nothing common
''',
    "set_funcs": r'''
s = {4, 1, 9}
len(s)      # 3
max(s)      # 9
min(s)      # 1
sum(s)      # 14
sorted(s)   # [1, 4, 9] (a list)
t = s.copy()
''',
    "frozen": r'''
fs = frozenset([1, 2, 3])
fs.add(4)      # AttributeError
fs | {4}       # frozenset({1, 2, 3, 4})
d = {fs: "ok"} # can be a dict key
''',
    "dedupe": r'''
nums = [3, 1, 3, 2, 1]
list(set(nums))   # duplicates removed
len(set(nums))    # 3 unique values
''',
    "dict_create": r'''
d = {"roll": 101, "name": "Amit"}
empty = {}                   # empty dict
empty2 = dict()
d2 = dict(city="Surat", pin=395001)
d3 = dict([("a", 1), ("b", 2)])
d4 = dict(zip(["x", "y"], [10, 20]))
d5 = {1: "one", (2, 3): "tuple key"}
bad = {[1, 2]: "no"}         # TypeError
dup = {"a": 1, "a": 2}       # {'a': 2}
''',
    "dict_access": r'''
d = {"roll": 101, "name": "Amit"}
d["name"]           # 'Amit'
d["age"]            # KeyError: 'age'
d.get("age")        # None
d.get("age", 18)    # 18 (default)
"roll" in d         # True (keys only)
101 in d            # False
101 in d.values()   # True
''',
    "dict_update": r'''
d = {"roll": 101, "name": "Amit"}
d["name"] = "Amit Shah"   # update
d["sem"] = 2              # add new pair
d.update({"sem": 3, "cpi": 8.1})
d.update(city="Surat")
d.setdefault("sem", 1)    # exists: 3
d.setdefault("div", "A")  # adds 'A'
''',
    "dict_delete": r'''
d = {"a": 1, "b": 2, "c": 3, "d": 4}
d.pop("a")          # 1, removes 'a'
d.pop("z", None)    # None, no error
d.pop("z")          # KeyError
d.popitem()         # ('d', 4) last pair
del d["b"]          # removes 'b'
d.clear()           # {}
del d               # dict deleted
''',
    "dict_ops": r'''
d = {"a": 1, "b": 2}
len(d)          # 2
"a" in d        # True
d == {"b": 2, "a": 1}   # True
d | {"c": 3}    # merge (Python 3.9+)
sorted(d)       # ['a', 'b'] keys
max(d)          # 'b' (largest key)
list(d)         # ['a', 'b']
''',
    "dict_methods": r'''
d = {"a": 1, "b": 2}
d.keys()      # dict_keys(['a', 'b'])
d.values()    # dict_values([1, 2])
d.items()     # dict_items([('a', 1),
              #             ('b', 2)])
c = d.copy()  # shallow copy
dict.fromkeys(["x", "y"], 0)
# {'x': 0, 'y': 0}
''',
    "dict_loop": r'''
m = {"Riya": 85, "Amit": 78}
for k in m:                 # keys
    print(k, m[k])
for v in m.values():        # values
    print(v)
for k, v in m.items():      # both
    print(k, "->", v)
''',
    "dict_sort": r'''
m = {"Riya": 85, "Amit": 78, "Om": 91}
dict(sorted(m.items()))     # by key
sorted(m.items(),
       key=lambda kv: kv[1])  # by value
max(m, key=m.get)           # 'Om'
''',
    "dict_comp": r'''
sq = {n: n * n for n in range(1, 4)}
# {1: 1, 2: 4, 3: 9}
''',
    "freq": r'''
freq = {}
for w in "a b a c a".split():
    freq[w] = freq.get(w, 0) + 1
# {'a': 3, 'b': 1, 'c': 1}
''',
    "nested_dict": r'''
emp = {
  101: {"name": "Om", "sal": 30000},
  102: {"name": "Riya", "sal": 42000},
}
emp[102]["name"]       # 'Riya'
emp[101]["sal"] += 5000
for eid, e in emp.items():
    print(eid, e["name"], e["sal"])
''',
    "list_of_dict": r'''
st = [{"name": "Amit", "m": 78},
      {"name": "Riya", "m": 85}]
st[1]["name"]                # 'Riya'
top = max(st, key=lambda s: s["m"])
''',
}
T = make_TP(SN)

SEC_3_3 = {
    "title": {"en": "3.3 Sets"},
    "items": [
        T("3.3.1 Defining (Creating) a Set",
          r"""<p>A <b>set</b> is an <b>unordered</b> collection of <b>unique</b> items written inside curly braces <code>{ }</code>. Sets are based on the mathematical idea of a set and support union, intersection, etc.</p>
@@set_create@@
<h4>Characteristics of a set</h4>
<ol><li><b>Unordered:</b> items have no fixed position, so there is no indexing or slicing.</li>
<li><b>Unique:</b> duplicate values are removed automatically.</li>
<li><b>Mutable:</b> items can be added and removed.</li>
<li>Items must be <b>immutable (hashable)</b>: numbers, strings and tuples are allowed; lists, sets and dicts are not.</li>
<li>Membership testing (<code>in</code>) is very fast.</li></ol>
<p><b>Important:</b> <code>{}</code> creates an empty <b>dictionary</b>; use <code>set()</code> for an empty set. The printed order of a set may differ from computer to computer.</p>""",
          programs=["py3p11"]),

        T("3.3.2 Accessing Set Elements",
          r"""<p>Since a set is unordered, its items <b>cannot be accessed by index</b>: <code>s[0]</code> raises <b>TypeError: 'set' object is not subscriptable</b>. Items are accessed by:</p>
<ol><li>looping with <code>for</code>;</li>
<li>checking membership with <code>in</code> / <code>not in</code>;</li>
<li>converting to a list or sorted list: <code>sorted(s)</code>.</li></ol>
@@set_access@@""",
          programs=["py3p11"]),

        T("3.3.3 Updating a Set (Adding Items)",
          r"""<p>Existing items of a set cannot be changed (there is no index), but new items can be added:</p>
<ul><li><b>add(x)</b> adds one item. If x is already present, nothing happens.</li>
<li><b>update(iterable)</b> adds all items of a list, tuple, string or another set.</li></ul>
@@set_add@@
<p>To "change" an item, remove the old value and add the new one.</p>""",
          programs=["py3p11"]),

        T("3.3.4 Deleting Set Elements",
          r"""<table>
<tr><th>Method</th><th>Action</th><th>If item missing</th></tr>
<tr><td>remove(x)</td><td>Removes x</td><td>KeyError</td></tr>
<tr><td>discard(x)</td><td>Removes x</td><td>No error</td></tr>
<tr><td>pop()</td><td>Removes and returns an arbitrary item</td><td>KeyError if the set is empty</td></tr>
<tr><td>clear()</td><td>Removes all items → set()</td><td>–</td></tr>
<tr><td>del s</td><td>Deletes the whole set</td><td>–</td></tr>
</table>
@@set_delete@@
<p><b>remove() vs discard():</b> both delete an item; only remove() raises an error when the item is not present.</p>""",
          programs=["py3p11"]),

        T("3.3.5 Set Operations",
          r"""<table>
<tr><th>Operation</th><th>Operator</th><th>Method</th><th>Result contains</th></tr>
<tr><td>Union</td><td>A | B</td><td>A.union(B)</td><td>All items of A and B</td></tr>
<tr><td>Intersection</td><td>A &amp; B</td><td>A.intersection(B)</td><td>Items common to A and B</td></tr>
<tr><td>Difference</td><td>A - B</td><td>A.difference(B)</td><td>Items in A but not in B</td></tr>
<tr><td>Symmetric difference</td><td>A ^ B</td><td>A.symmetric_difference(B)</td><td>Items in A or B but not both</td></tr>
</table>
@@set_ops@@
<p>The methods also accept lists and tuples, while the operators need sets on both sides. The <code>_update</code> versions change A itself:</p>
@@set_meth_ops@@
<h4>Subset, superset and disjoint</h4>
@@set_rel@@""",
          diagram="py3_set_ops", programs=["py3p12"]),

        T("3.3.6 Built-in Functions, Methods and frozenset",
          r"""<table>
<tr><th>Function / Method</th><th>Description</th></tr>
<tr><td>len(s), max(s), min(s), sum(s)</td><td>Count, largest, smallest, total</td></tr>
<tr><td>sorted(s)</td><td>Sorted list of the items</td></tr>
<tr><td>set(iterable)</td><td>Creates a set (removes duplicates)</td></tr>
<tr><td>add(), update()</td><td>Add items</td></tr>
<tr><td>remove(), discard(), pop(), clear()</td><td>Delete items</td></tr>
<tr><td>union(), intersection(), difference(), symmetric_difference()</td><td>Set operations</td></tr>
<tr><td>issubset(), issuperset(), isdisjoint()</td><td>Relationship tests (True/False)</td></tr>
<tr><td>copy()</td><td>Shallow copy</td></tr>
</table>
@@set_funcs@@
<h4>frozenset</h4>
<p>A <b>frozenset</b> is an <b>immutable set</b>: it supports the set operations but not add/remove. It can be used as a dictionary key or as an item of another set.</p>
@@frozen@@
<h4>Common use: removing duplicates</h4>
@@dedupe@@""",
          programs=["py3p13"]),

        T("Key Points – 3.3",
          r"""<ul>
<li>A set is unordered, mutable, holds unique items only: <code>{1, 2, 3}</code>; the empty set is <code>set()</code>, not {}.</li>
<li>Items must be immutable; there is no indexing (TypeError). Access with for and in.</li>
<li>Add: add(x), update(iterable). Delete: remove (KeyError), discard (no error), pop (arbitrary), clear.</li>
<li>| union, &amp; intersection, − difference, ^ symmetric difference.</li>
<li>issubset (&lt;=), issuperset (&gt;=), isdisjoint().</li>
<li>frozenset = immutable set; can be a dict key.</li>
<li><code>set(list)</code> removes duplicates quickly.</li>
</ul>""", key=True),
    ],
}

SEC_3_4 = {
    "title": {"en": "3.4 Dictionaries"},
    "items": [
        T("3.4.1 Defining (Creating) a Dictionary",
          r"""<p>A <b>dictionary</b> is a collection of <b>key : value pairs</b> written inside curly braces. Each <b>key</b> is mapped to a <b>value</b>, and values are looked up by key instead of by position (like a word and its meaning in a real dictionary).</p>
@@dict_create@@
<h4>Rules and characteristics</h4>
<ol><li><b>Keys must be unique.</b> If a key is repeated, the last value is kept.</li>
<li><b>Keys must be immutable</b> (str, int, float, tuple). A list cannot be a key.</li>
<li><b>Values</b> can be of any type and may repeat.</li>
<li>Dictionaries are <b>mutable</b>: pairs can be added, changed and removed.</li>
<li>From Python 3.7 they keep the <b>insertion order</b>.</li></ol>""",
          diagram="py3_dict_struct", programs=["py3p14"]),

        T("3.4.2 Accessing Dictionary Elements",
          r"""<ul><li><b>Square brackets</b> <code>d[key]</code> return the value, or raise a <b>KeyError</b> if the key does not exist.</li>
<li><b>get()</b>: <code>d.get(key)</code> returns None for a missing key, and <code>d.get(key, default)</code> returns the default. It never raises an error.</li>
<li><code>in</code> checks only the <b>keys</b>; use <code>d.values()</code> to search values.</li></ul>
@@dict_access@@
<table>
<tr><th>d[key]</th><th>d.get(key)</th></tr>
<tr><td>KeyError if the key is missing</td><td>Returns None or a default value</td></tr>
<tr><td>Can also be used to assign</td><td>Read-only</td></tr>
</table>""",
          programs=["py3p14"]),

        T("3.4.3 Updating a Dictionary (Adding and Changing)",
          r"""<ul><li><code>d[key] = value</code>: if the key exists, its value is <b>changed</b>; otherwise a new pair is <b>added</b>.</li>
<li><code>d.update(other)</code> adds or changes several pairs from another dictionary or keyword arguments.</li>
<li><code>d.setdefault(key, value)</code> returns the value if the key exists; if not, it adds key: value.</li></ul>
@@dict_update@@
<p>Keys cannot be renamed directly. To rename a key: <code>d["new"] = d.pop("old")</code>.</p>""",
          programs=["py3p14", "py3p17"]),

        T("3.4.4 Deleting Dictionary Elements",
          r"""<table>
<tr><th>Way</th><th>Action</th><th>Returns</th><th>Missing key</th></tr>
<tr><td>pop(key)</td><td>Removes the pair with that key</td><td>Its value</td><td>KeyError</td></tr>
<tr><td>pop(key, default)</td><td>Same</td><td>Value or default</td><td>No error</td></tr>
<tr><td>popitem()</td><td>Removes the last inserted pair</td><td>(key, value) tuple</td><td>KeyError if empty</td></tr>
<tr><td>del d[key]</td><td>Removes the pair</td><td>–</td><td>KeyError</td></tr>
<tr><td>clear()</td><td>Removes all pairs → {}</td><td>None</td><td>–</td></tr>
<tr><td>del d</td><td>Deletes the dictionary</td><td>–</td><td>–</td></tr>
</table>
@@dict_delete@@""",
          programs=["py3p14", "py3p17"]),

        T("3.4.5 Basic Dictionary Operations and Built-in Functions",
          r"""<table>
<tr><th>Operation / Function</th><th>Result</th></tr>
<tr><td>len(d)</td><td>Number of key-value pairs</td></tr>
<tr><td>key in d / key not in d</td><td>Membership test on keys</td></tr>
<tr><td>d1 == d2</td><td>True if the same pairs (order does not matter)</td></tr>
<tr><td>d1 | d2</td><td>New merged dictionary (Python 3.9+)</td></tr>
<tr><td>sorted(d), max(d), min(d)</td><td>Work on the <b>keys</b></td></tr>
<tr><td>list(d)</td><td>List of the keys</td></tr>
<tr><td>dict(), str(d), type(d)</td><td>Create, convert to string, type</td></tr>
</table>
@@dict_ops@@
<p>Dictionaries do <b>not</b> support <code>+</code>, <code>*</code>, indexing by position, or slicing.</p>""",
          programs=["py3p15"]),

        T("3.4.6 Dictionary Methods",
          r"""<table>
<tr><th>Method</th><th>Description</th></tr>
<tr><td>keys()</td><td>View of all keys</td></tr>
<tr><td>values()</td><td>View of all values</td></tr>
<tr><td>items()</td><td>View of (key, value) tuples</td></tr>
<tr><td>get(key[, default])</td><td>Value for key, or None/default</td></tr>
<tr><td>update(other)</td><td>Adds/changes pairs</td></tr>
<tr><td>pop(key[, default])</td><td>Removes key and returns its value</td></tr>
<tr><td>popitem()</td><td>Removes and returns the last pair</td></tr>
<tr><td>setdefault(key[, value])</td><td>Returns the value; inserts the key if missing</td></tr>
<tr><td>fromkeys(keys[, value])</td><td>New dict with the given keys, all with the same value</td></tr>
<tr><td>copy()</td><td>Shallow copy</td></tr>
<tr><td>clear()</td><td>Removes all pairs</td></tr>
</table>
@@dict_methods@@
<p>keys(), values() and items() return <b>view objects</b> that update automatically when the dictionary changes. Wrap them in <code>list()</code> to get a list.</p>""",
          diagram="py3_dict_methods", programs=["py3p15"]),

        T("3.4.7 Traversing, Sorting and Dictionary Comprehension",
          r"""<h4>Looping over a dictionary</h4>
@@dict_loop@@
<h4>Sorting</h4>
@@dict_sort@@
<h4>Dictionary comprehension</h4>
@@dict_comp@@
<h4>Counting frequency (very common exam program)</h4>
@@freq@@""",
          programs=["py3p15", "py3p16"]),

        T("3.4.8 Nested Data Structures",
          r"""<p>Collections can contain other collections. This is how real records are stored in Python programs:</p>
<ul><li><b>List of lists:</b> a matrix or table.</li>
<li><b>List of dictionaries:</b> a list of records (students, products).</li>
<li><b>Dictionary of dictionaries:</b> records looked up by an id (employees, books).</li>
<li><b>Dictionary of lists:</b> several values per key (the marks of each student).</li></ul>
@@nested_dict@@
@@list_of_dict@@
<p>Access works step by step from left to right: <code>emp[102]["name"]</code> first gets the inner dictionary, then the name.</p>""",
          diagram="py3_nested", programs=["py3p17"]),

        T("3.4.9 Comparison of List, Tuple, Set and Dictionary",
          r"""<table>
<tr><th>Point</th><th>List</th><th>Tuple</th><th>Set</th><th>Dictionary</th></tr>
<tr><td>Syntax</td><td>[1, 2]</td><td>(1, 2)</td><td>{1, 2}</td><td>{"a": 1}</td></tr>
<tr><td>Empty</td><td>[ ] / list()</td><td>( ) / tuple()</td><td>set()</td><td>{ } / dict()</td></tr>
<tr><td>Ordered</td><td>Yes</td><td>Yes</td><td>No</td><td>Yes (3.7+)</td></tr>
<tr><td>Mutable</td><td>Yes</td><td>No</td><td>Yes</td><td>Yes</td></tr>
<tr><td>Duplicates</td><td>Yes</td><td>Yes</td><td>No</td><td>Keys: No, values: Yes</td></tr>
<tr><td>Access</td><td>Index</td><td>Index</td><td>Loop / in</td><td>Key</td></tr>
<tr><td>Add</td><td>append, insert, extend</td><td>Not possible</td><td>add, update</td><td>d[k] = v, update</td></tr>
<tr><td>Remove</td><td>remove, pop, del</td><td>Not possible</td><td>remove, discard, pop</td><td>pop, popitem, del</td></tr>
<tr><td>Use</td><td>Ordered changing data</td><td>Fixed data</td><td>Unique items, math sets</td><td>Lookup by key</td></tr>
</table>""",
          diagram="py3_choose", programs=["py3p17"]),

        T("Key Points – 3.4",
          r"""<ul>
<li>A dictionary stores key: value pairs: <code>{"roll": 1}</code>; keys are unique and immutable, values can be anything.</li>
<li>Access: d[key] (KeyError if missing) or d.get(key, default) (no error).</li>
<li>Add/update: d[key] = value, update(), setdefault().</li>
<li>Delete: pop(key), popitem() (last pair), del d[key], clear().</li>
<li>keys(), values(), items() for looping; <code>in</code> checks keys only.</li>
<li>sorted(), max(), min() and len() work on the keys.</li>
<li>Frequency count: <code>freq[w] = freq.get(w, 0) + 1</code>.</li>
<li>Nested: list of dicts, dict of dicts; access like <code>emp[101]["name"]</code>.</li>
</ul>""", key=True),
    ],
}

NOTES_B = [SEC_3_3, SEC_3_4]
