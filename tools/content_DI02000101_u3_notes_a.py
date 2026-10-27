"""DI02000101 Unit 3 notes part A: 3.1 Lists, 3.2 Tuples."""
from py_content import make_TP

SN = {
    "ds_four": r'''
marks = [78, 85, 62]          # list
point = (10, 20)              # tuple
tags = {"py", "c", "java"}    # set
emp = {"id": 1, "name": "Om"} # dict
''',
    "list_create": r'''
empty = []                  # empty list
empty2 = list()             # empty list
marks = [78, 85, 62, 90]    # integers
mixed = [1, "Amit", 7.5, True]
nested = [[1, 2], [3, 4]]   # list in list
nums = list(range(1, 6))  # [1, 2, 3, 4, 5]
chars = list("GTU")  # ['G', 'T', 'U']
words = "a b c".split()  # ['a','b','c']
''',
    "list_input": r'''
data = input("Enter numbers: ")
nums = [int(x) for x in data.split()]
# input 10 20 30 -> [10, 20, 30]
''',
    "list_access": r'''
a = [10, 20, 30, 40, 50, 60]
a[0]       # 10   first item
a[3]       # 40
a[-1]      # 60   last item
a[-2]      # 50
a[1:4]     # [20, 30, 40]
a[:3]      # [10, 20, 30]
a[3:]      # [40, 50, 60]
a[::2]     # [10, 30, 50]
a[::-1]    # [60, 50, 40, 30, 20, 10]
a[10]      # IndexError
a[2:100]   # [30, 40, 50, 60] (no error)
''',
    "list_traverse": r'''
for item in a:              # by value
    print(item)

for i in range(len(a)):     # by index
    print(i, a[i])

for i, item in enumerate(a):  # both
    print(i, item)

i = 0
while i < len(a):           # while loop
    print(a[i])
    i += 1
''',
    "list_update": r'''
a = [10, 20, 30, 40, 50]
a[1] = 25           # [10, 25, 30, 40, 50]
a[-1] = 55          # [10, 25, 30, 40, 55]
a[2:4] = [35, 45]   # replace a slice
a[1:3] = [7]        # slice can shrink list
a.append(60)        # add one at end
a.insert(0, 5)      # add at index 0
a.extend([70, 80])  # add many at end
a += [90]           # same as extend
''',
    "list_delete": r'''
a = [10, 20, 30, 20, 40]
a.remove(20)  # 1st 20 -> [10, 30, 20, 40]
x = a.pop()     # x = 40   -> [10, 30, 20]
y = a.pop(0)    # y = 10   -> [30, 20]
del a[0]        # [20]
del a[0:1]      # slice delete -> []
a.clear()       # [] (list still exists)
del a           # list variable deleted
''',
    "append_extend": r'''
a = [1, 2]
a.append([3, 4])   # [1, 2, [3, 4]]
b = [1, 2]
b.extend([3, 4])   # [1, 2, 3, 4]
''',
    "list_ops": r'''
a, b = [1, 2, 3], [4, 5]
a + b         # [1, 2, 3, 4, 5]
b * 2         # [4, 5, 4, 5]
[0] * 5       # [0, 0, 0, 0, 0]
2 in a        # True
7 not in a    # True
a == [1, 2, 3]   # True
[1, 2] < [1, 3]  # True (item by item)
''',
    "list_alias": r'''
a = [1, 2, 3]
b = a          # alias: same list
c = a.copy()   # new list (also a[:])
b[0] = 99
print(a)       # [99, 2, 3]  changed!
print(c)       # [1, 2, 3]   safe
''',
    "list_builtins": r'''
m = [78, 85, 62, 90]
len(m)      # 4
max(m)      # 90
min(m)      # 62
sum(m)      # 315
sorted(m)   # [62, 78, 85, 90] new list
sorted(m, reverse=True)  # descending
list("hi")  # ['h', 'i']
any([0, 0, 5])   # True
all([1, 0, 5])   # False
''',
    "list_methods": r'''
m = [78, 85, 62, 85]
m.count(85)    # 2
m.index(62)    # 2
m.sort()       # [62, 78, 85, 85]
m.sort(reverse=True)
m.reverse()    # reverse order in place
n = m.copy()   # shallow copy
''',
    "sort_vs_sorted": r'''
a = [3, 1, 2]
b = sorted(a)   # b = [1, 2, 3], a same
r = a.sort()    # a = [1, 2, 3], r = None
''',
    "nested": r'''
m = [[1, 2, 3],
     [4, 5, 6]]
m[0]        # [1, 2, 3]  (row 0)
m[1][2]     # 6
len(m)      # 2 rows
len(m[0])   # 3 columns
for row in m:
    for x in row:
        print(x, end=" ")
''',
    "comp": r'''
sq = [x * x for x in range(1, 6)]
# [1, 4, 9, 16, 25]
ev = [x for x in range(10) if x % 2 == 0]
# [0, 2, 4, 6, 8]
res = ["P" if m >= 35 else "F"
       for m in [40, 20, 80]]
# ['P', 'F', 'P']
''',
    "stack": r'''
st = []
st.append(1)   # push
st.append(2)   # push
st.pop()       # 2  (last in, first out)
q = []
q.append("A")  # enqueue
q.append("B")
q.pop(0)       # 'A' (first in, first out)
''',
    "tup_create": r'''
t = (10, 20, 30)          # tuple
t2 = 1, "GTU", 3.5        # packing
empty = ()                # empty tuple
empty2 = tuple()
one = (5,)                # 1 item: comma
not_t = (5)               # int, not tuple
t3 = tuple([1, 2, 3])     # from list
t4 = tuple("abc")         # ('a', 'b', 'c')
nested = ((1, 2), (3, 4))
''',
    "tup_access": r'''
t = (10, 20, 30, 40, 50)
t[0]      # 10
t[-1]     # 50
t[1:4]    # (20, 30, 40)  slice -> tuple
t[::-1]   # (50, 40, 30, 20, 10)
for x in t:
    print(x)
''',
    "tup_unpack": r'''
t = (101, "Amit", 78.5)
roll, name, marks = t     # unpacking
a, b = 5, 9
a, b = b, a               # swap
first, *rest = (1, 2, 3, 4)
# first = 1, rest = [2, 3, 4]
x, y = (1, 2, 3)          # ValueError
''',
    "tup_update": r'''
t = (10, 20, 30)
t[0] = 99        # TypeError
lst = list(t)    # convert to list
lst[0] = 99
t = tuple(lst)   # (99, 20, 30)
t = t + (40,)    # (99, 20, 30, 40)
''',
    "tup_mutable_inside": r'''
t = (1, [2, 3])
t[1].append(4)   # allowed!
print(t)         # (1, [2, 3, 4])
''',
    "tup_delete": r'''
t = (10, 20, 30)
del t[0]     # TypeError
del t        # whole tuple deleted
print(t)     # NameError
''',
    "tup_ops": r'''
a, b = (1, 2), (3,)
a + b        # (1, 2, 3)
a * 3        # (1, 2, 1, 2, 1, 2)
2 in a       # True
(1, 2) < (1, 3)   # True
len(a)       # 2
''',
    "tup_funcs": r'''
t = (3, 1, 4, 1, 5)
len(t)       # 5
max(t)       # 5
min(t)       # 1
sum(t)       # 14
sorted(t)    # [1, 1, 3, 4, 5]  (a list)
tuple(sorted(t))  # (1, 1, 3, 4, 5)
t.count(1)   # 2
t.index(4)   # 2
''',
}
T = make_TP(SN)

SEC_3_1 = {
    "title": {"en": "3.1 Lists"},
    "items": [
        T("3.1.1 Introduction to Data Structures in Python",
          r"""<p>A <b>data structure</b> is a way of storing and organising many values in a single variable, so they can be accessed and processed efficiently. Python has four built-in <b>collection</b> data types:</p>
@@ds_four@@
<table>
<tr><th>Feature</th><th>List</th><th>Tuple</th><th>Set</th><th>Dictionary</th></tr>
<tr><td>Brackets</td><td>[ ]</td><td>( )</td><td>{ }</td><td>{key: value}</td></tr>
<tr><td>Ordered</td><td>Yes</td><td>Yes</td><td>No</td><td>Yes (insertion order, 3.7+)</td></tr>
<tr><td>Mutable (changeable)</td><td>Yes</td><td>No</td><td>Yes</td><td>Yes</td></tr>
<tr><td>Duplicates</td><td>Allowed</td><td>Allowed</td><td>Not allowed</td><td>Keys unique</td></tr>
<tr><td>Indexing</td><td>Yes (0, 1, …)</td><td>Yes</td><td>No</td><td>By key</td></tr>
<tr><td>Class</td><td>list</td><td>tuple</td><td>set</td><td>dict</td></tr>
</table>
<ul><li><b>Sequence</b> types (list, tuple, string) keep items in order and support indexing and slicing.</li>
<li><b>Mutable</b> means the object can be changed after it is created; <b>immutable</b> means it cannot.</li></ul>"""),

        T("3.1.2 Defining (Creating) a List",
          r"""<p>A <b>list</b> is an <b>ordered, mutable</b> collection of items written inside square brackets <code>[ ]</code> and separated by commas. A list can hold items of <b>different data types</b> and allows <b>duplicate</b> values.</p>
@@list_create@@
<h4>Characteristics of a list</h4>
<ol><li>Ordered: items keep the position in which they were inserted.</li>
<li>Mutable: items can be added, changed or removed.</li>
<li>Allows duplicates: [1, 1, 2] is valid.</li>
<li>Heterogeneous: different types can be mixed.</li>
<li>Dynamic: the size grows or shrinks automatically.</li>
<li>Can be nested: a list can contain other lists.</li></ol>
<h4>Creating a list from user input</h4>
@@list_input@@""",
          programs=["py3p1", "py3p5"]),

        T("3.1.3 Accessing List Elements: Indexing, Slicing and Traversing",
          r"""<p><b>Indexing:</b> each item has a position number called an <b>index</b>. Positive indexes start at <b>0</b> from the left; negative indexes start at <b>−1</b> from the right. An index outside the range gives an <b>IndexError</b>.</p>
<p><b>Slicing</b> <code>list[start:end:step]</code> returns a <b>new list</b> from start up to (but <b>not including</b>) end. A missing start means 0, a missing end means the length, and a step of −1 reverses the list. Slicing never gives an IndexError.</p>
@@list_access@@
<h4>Traversing (looping through) a list</h4>
@@list_traverse@@""",
          diagram="py3_list_index", programs=["py3p1"]),

        T("3.1.4 Updating a List",
          r"""<p>Because lists are <b>mutable</b>, their items can be changed after creation without making a new list.</p>
<ul><li><b>Change one item:</b> <code>list[index] = value</code></li>
<li><b>Change a slice:</b> <code>list[start:end] = [values]</code>; the number of new values may differ from the number replaced.</li>
<li><b>append(x)</b> adds one item at the end.</li>
<li><b>insert(i, x)</b> adds x before position i.</li>
<li><b>extend(iterable)</b> adds every item of another list/tuple/string at the end.</li></ul>
@@list_update@@
<h4>append() vs extend()</h4>
@@append_extend@@
<p>append() adds its argument as <b>one</b> item (here, a whole list); extend() adds each element separately.</p>""",
          programs=["py3p2"]),

        T("3.1.5 Deleting List Elements",
          r"""<table>
<tr><th>Way</th><th>Deletes</th><th>Returns</th><th>If not found</th></tr>
<tr><td>remove(x)</td><td>First item with value x</td><td>None</td><td>ValueError</td></tr>
<tr><td>pop()</td><td>Last item</td><td>The removed item</td><td>IndexError if empty</td></tr>
<tr><td>pop(i)</td><td>Item at index i</td><td>The removed item</td><td>IndexError</td></tr>
<tr><td>del a[i] / del a[i:j]</td><td>Item / slice by index</td><td>– (statement)</td><td>IndexError</td></tr>
<tr><td>clear()</td><td>All items (list becomes [ ])</td><td>None</td><td>–</td></tr>
<tr><td>del a</td><td>The whole list variable</td><td>–</td><td>Using a later: NameError</td></tr>
</table>
@@list_delete@@
<ul><li>Use <b>remove()</b> when you know the value, and <b>pop()</b> or <b>del</b> when you know the position.</li>
<li><b>del</b> is a keyword (statement), while remove(), pop() and clear() are list methods.</li></ul>""",
          diagram="py3_list_methods", programs=["py3p2"]),

        T("3.1.6 Basic List Operations",
          r"""<table>
<tr><th>Operation</th><th>Operator</th><th>Example</th><th>Result</th></tr>
<tr><td>Concatenation</td><td>+</td><td>[1, 2] + [3]</td><td>[1, 2, 3]</td></tr>
<tr><td>Repetition</td><td>*</td><td>[0] * 3</td><td>[0, 0, 0]</td></tr>
<tr><td>Membership</td><td>in / not in</td><td>2 in [1, 2]</td><td>True</td></tr>
<tr><td>Comparison</td><td>== != &lt; &gt;</td><td>[1, 2] &lt; [1, 3]</td><td>True</td></tr>
<tr><td>Length</td><td>len()</td><td>len([5, 6, 7])</td><td>3</td></tr>
<tr><td>Iteration</td><td>for</td><td>for x in a:</td><td>each item</td></tr>
</table>
@@list_ops@@
<h4>Aliasing and copying</h4>
<p>Assignment <code>b = a</code> does <b>not</b> copy a list. Both names refer to the <b>same</b> list object (an <b>alias</b>), so a change through one name is seen through the other. To get an independent list, use <code>a.copy()</code>, <code>a[:]</code> or <code>list(a)</code>. For nested lists, use <code>copy.deepcopy(a)</code>.</p>
@@list_alias@@""",
          diagram="py3_list_copy", programs=["py3p3"]),

        T("3.1.7 Built-in Functions and Methods of List",
          r"""<h4>Built-in functions (work on many types)</h4>
<table>
<tr><th>Function</th><th>Description</th></tr>
<tr><td>len(list)</td><td>Number of items</td></tr>
<tr><td>max(list) / min(list)</td><td>Largest / smallest item</td></tr>
<tr><td>sum(list)</td><td>Total of numeric items</td></tr>
<tr><td>sorted(list)</td><td>Returns a new sorted list (original unchanged)</td></tr>
<tr><td>list(iterable)</td><td>Converts a string/tuple/set/range into a list</td></tr>
<tr><td>any(list) / all(list)</td><td>True if any / all items are true</td></tr>
</table>
@@list_builtins@@
<h4>List methods (called as list.method())</h4>
<table>
<tr><th>Method</th><th>Description</th></tr>
<tr><td>append(x)</td><td>Adds x at the end</td></tr>
<tr><td>insert(i, x)</td><td>Inserts x at index i</td></tr>
<tr><td>extend(iter)</td><td>Adds all items of iter at the end</td></tr>
<tr><td>remove(x)</td><td>Removes the first occurrence of x</td></tr>
<tr><td>pop([i])</td><td>Removes and returns the item at i (default: last)</td></tr>
<tr><td>clear()</td><td>Removes all items</td></tr>
<tr><td>index(x)</td><td>Index of the first occurrence of x</td></tr>
<tr><td>count(x)</td><td>Number of times x occurs</td></tr>
<tr><td>sort(reverse=False, key=None)</td><td>Sorts the list in place</td></tr>
<tr><td>reverse()</td><td>Reverses the list in place</td></tr>
<tr><td>copy()</td><td>Returns a shallow copy</td></tr>
</table>
@@list_methods@@
<h4>sort() vs sorted()</h4>
@@sort_vs_sorted@@
<p><b>Common mistake:</b> <code>a = a.sort()</code> makes a None. Methods that change the list in place return None.</p>""",
          programs=["py3p4", "py3p5"]),

        T("3.1.8 Nested Lists and List Comprehension",
          r"""<p>A <b>nested list</b> is a list whose items are lists. It is used to store tables and matrices. <code>m[i][j]</code> gives row i, column j.</p>
@@nested@@
<p>A <b>list comprehension</b> builds a new list from a sequence in a single line:</p>
<p><code>[expression for item in iterable if condition]</code></p>
@@comp@@
<ul><li>It is shorter and usually faster than a loop with append().</li>
<li>The if-part (filter) is optional. A conditional expression can be used in the expression part.</li></ul>""",
          programs=["py3p7", "py3p8"]),

        T("3.1.9 Applications: List as Stack and Queue",
          r"""<ul><li><b>Stack</b>: LIFO (Last In First Out), like a pile of plates. Push = <code>append()</code>, pop = <code>pop()</code>, top = <code>list[-1]</code>.</li>
<li><b>Queue</b>: FIFO (First In First Out), like a ticket line. Enqueue = <code>append()</code>, dequeue = <code>pop(0)</code>.</li></ul>
@@stack@@
<p>Other common uses of lists: storing marks of students, shopping carts, reading many inputs, searching and sorting.</p>""",
          programs=["py3p6"]),

        T("Key Points – 3.1",
          r"""<ul>
<li>A list is ordered, mutable, allows duplicates and mixed types: <code>[1, "a", 2.5]</code>.</li>
<li>Index from 0 (left) or −1 (right); a bad index raises IndexError. A slice <code>[s:e:step]</code> excludes e and returns a new list.</li>
<li>Update: <code>a[i] = x</code>, slice assignment, append(), insert(), extend().</li>
<li>Delete: remove(value), pop(index), del a[i], clear(); del a deletes the variable.</li>
<li>Operations: + (join), * (repeat), in, comparison, len().</li>
<li><code>b = a</code> is an alias; use copy(), a[:] or list(a) for a real copy.</li>
<li>sorted() returns a new list; sort() changes the list and returns None.</li>
<li>Comprehension: <code>[x*x for x in range(5) if x % 2 == 0]</code>.</li>
<li>Stack: append() + pop(); Queue: append() + pop(0).</li>
</ul>""", key=True),
    ],
}

SEC_3_2 = {
    "title": {"en": "3.2 Tuples"},
    "items": [
        T("3.2.1 Defining (Creating) a Tuple",
          r"""<p>A <b>tuple</b> is an <b>ordered, immutable</b> collection of items written inside parentheses <code>( )</code> and separated by commas. Once a tuple is created, its items <b>cannot be changed, added or removed</b>.</p>
@@tup_create@@
<ul><li>It is the <b>comma</b> that makes a tuple, not the brackets. A single-item tuple needs a trailing comma: <code>(5,)</code>.</li>
<li>Like lists, tuples allow duplicates and mixed data types, and can be nested.</li></ul>
<h4>Why use tuples?</h4>
<ol><li>They protect data that must not change (days of the week, coordinates, database records).</li>
<li>They are faster and use less memory than lists.</li>
<li>They can be used as <b>dictionary keys</b> and set items (lists cannot).</li>
<li>Functions return several values as a tuple: <code>return a, b</code>.</li></ol>""",
          programs=["py3p9"]),

        T("3.2.2 Accessing Tuple Elements, Packing and Unpacking",
          r"""<p>Tuple items are accessed in the same way as list items: by <b>index</b> (0 … n−1 or −1 … −n), by <b>slicing</b> (which returns a new tuple), and with a <b>for loop</b>.</p>
@@tup_access@@
<h4>Packing and unpacking</h4>
<ul><li><b>Packing:</b> putting several values into one tuple: <code>t = 101, "Amit", 78.5</code>.</li>
<li><b>Unpacking:</b> taking the values out into separate variables: <code>roll, name, marks = t</code>. The number of variables must equal the number of items, otherwise a <b>ValueError</b> is raised. A starred variable (<code>*rest</code>) collects the extra items as a list.</li></ul>
@@tup_unpack@@""",
          diagram="py3_tuple_pack", programs=["py3p9"]),

        T("3.2.3 Updating and Deleting a Tuple",
          r"""<p>Tuples are <b>immutable</b>, so <code>t[0] = 99</code> raises <b>TypeError: 'tuple' object does not support item assignment</b>. There are no append(), insert(), remove() or pop() methods.</p>
<h4>Ways to "update" a tuple</h4>
<ol><li>Convert it to a list, change the list, and convert it back with <code>tuple()</code>.</li>
<li>Create a new tuple using concatenation <code>+</code> and slicing.</li></ol>
@@tup_update@@
<p><b>Note:</b> if a tuple contains a mutable object (like a list), that object can still be changed:</p>
@@tup_mutable_inside@@
<h4>Deleting</h4>
<p>Individual items cannot be deleted, but the <b>whole tuple</b> can be deleted with <code>del</code>.</p>
@@tup_delete@@""",
          programs=["py3p9"]),

        T("3.2.4 Basic Tuple Operations",
          r"""<table>
<tr><th>Operation</th><th>Example</th><th>Result</th></tr>
<tr><td>Concatenation (+)</td><td>(1, 2) + (3,)</td><td>(1, 2, 3)</td></tr>
<tr><td>Repetition (*)</td><td>("Hi",) * 2</td><td>('Hi', 'Hi')</td></tr>
<tr><td>Membership (in)</td><td>3 in (1, 2, 3)</td><td>True</td></tr>
<tr><td>Comparison</td><td>(1, 2) &lt; (1, 3)</td><td>True</td></tr>
<tr><td>Indexing / slicing</td><td>(5, 6, 7)[1:]</td><td>(6, 7)</td></tr>
<tr><td>Iteration</td><td>for x in t:</td><td>each item</td></tr>
</table>
@@tup_ops@@
<p>+ and * do not change the original tuple; they always create a <b>new</b> tuple.</p>""",
          programs=["py3p10"]),

        T("3.2.5 Built-in Functions and Methods of Tuple",
          r"""<table>
<tr><th>Function / Method</th><th>Description</th></tr>
<tr><td>len(t)</td><td>Number of items</td></tr>
<tr><td>max(t) / min(t)</td><td>Largest / smallest item</td></tr>
<tr><td>sum(t)</td><td>Sum of numeric items</td></tr>
<tr><td>sorted(t)</td><td>Returns a sorted <b>list</b></td></tr>
<tr><td>tuple(iterable)</td><td>Converts a list/string/set into a tuple</td></tr>
<tr><td>t.count(x)</td><td>Number of times x occurs</td></tr>
<tr><td>t.index(x)</td><td>Index of the first occurrence of x (ValueError if absent)</td></tr>
</table>
@@tup_funcs@@
<p>Tuples have only <b>two methods</b>, count() and index(), because every other list method would change the data.</p>""",
          diagram="py3_builtin_matrix", programs=["py3p10"]),

        T("3.2.6 Difference between List and Tuple",
          r"""<table>
<tr><th>Point</th><th>List</th><th>Tuple</th></tr>
<tr><td>Syntax</td><td>[1, 2, 3]</td><td>(1, 2, 3)</td></tr>
<tr><td>Mutability</td><td>Mutable (can change)</td><td>Immutable (cannot change)</td></tr>
<tr><td>Methods</td><td>Many (append, insert, remove, pop, sort …)</td><td>Only count() and index()</td></tr>
<tr><td>Speed</td><td>Slower</td><td>Faster</td></tr>
<tr><td>Memory</td><td>More</td><td>Less</td></tr>
<tr><td>Dictionary key</td><td>Cannot be used</td><td>Can be used</td></tr>
<tr><td>Single item</td><td>[5]</td><td>(5,)</td></tr>
<tr><td>Use</td><td>Data that changes (marks list, cart)</td><td>Fixed data (days, coordinates, records)</td></tr>
</table>""",
          programs=["py3p9", "py3p10"]),

        T("Key Points – 3.2",
          r"""<ul>
<li>A tuple is ordered and immutable: <code>(1, 2, 3)</code>; a single item needs a comma <code>(5,)</code>.</li>
<li>Access by index, slicing and loops, exactly like lists.</li>
<li>Packing: <code>t = 1, 2</code>; unpacking: <code>a, b = t</code>; swap: <code>a, b = b, a</code>.</li>
<li><code>t[0] = x</code> → TypeError. To update, use list() → change → tuple(), or build a new tuple with +.</li>
<li>Single items cannot be deleted; <code>del t</code> deletes the whole tuple.</li>
<li>Operations: +, *, in, comparison; functions: len, max, min, sum, sorted (returns a list).</li>
<li>Only 2 methods: count() and index().</li>
<li>Tuples are faster, use less memory, and can be dictionary keys.</li>
</ul>""", key=True),
    ],
}

NOTES_A = [SEC_3_1, SEC_3_2]
