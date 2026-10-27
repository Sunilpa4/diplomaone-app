"""DI02000101 Unit 3 - solved Python programs (lists, tuples, sets, dictionaries). Outputs are genuine."""
from py_content import PP

PROGRAMS = [
    PP("py3p1", "List: define and access (index, slice, traverse)", r'''
marks = [78, 85, 62, 90, 71]
empty = []
mixed = [101, "Amit", 78.5, True]
nums = list(range(1, 6))            # list() constructor
chars = list("GTU")

print("marks       :", marks)
print("mixed       :", mixed)
print("nums, chars :", nums, chars)
print("marks[0]    :", marks[0])
print("marks[-1]   :", marks[-1])
print("marks[1:4]  :", marks[1:4])
print("marks[::-1] :", marks[::-1])

print("Traverse with for:")
for m in marks:
    print(m, end=" ")
print()

print("With index (enumerate):")
for i, m in enumerate(marks):
    print(f"  marks[{i}] = {m}")

matrix = [[1, 2], [3, 4]]           # nested list
print("matrix[1][0] =", matrix[1][0])
''', (),
       r"""<ul><li>A list is created with square brackets or <code>list()</code>. Items may be of different types, and a list can contain another list (a nested list).</li>
<li>Indexing starts at 0 (or −1 from the end); slicing <code>[start:end:step]</code> returns a <b>new list</b>.</li>
<li><code>enumerate()</code> gives both the index and the item while looping.</li></ul>"""),

    PP("py3p2", "List: update and delete values", r'''
a = [10, 20, 30, 40, 50]
print("Original      :", a)

a[1] = 25                       # update one item
print("a[1] = 25     :", a)
a[2:4] = [35, 45]               # update a slice
print("a[2:4] = ...  :", a)

a.append(60)
a.insert(0, 5)
a.extend([70, 80])
print("After adding  :", a)

a.remove(35)                    # by value (first match)
print("remove(35)    :", a)
x = a.pop()                     # last item
print("pop()         :", a, "-> removed", x)
y = a.pop(1)                    # by index
print("pop(1)        :", a, "-> removed", y)
del a[0]                        # by index
print("del a[0]      :", a)
del a[1:3]                      # delete a slice
print("del a[1:3]    :", a)
a.clear()                       # remove all
print("clear()       :", a)

try:
    a.remove(99)
except ValueError as e:
    print("Error         :", e)
''', (),
       r"""<ul><li>Lists are <b>mutable</b>: an item or a slice can be replaced by assignment.</li>
<li><b>Adding:</b> <code>append(x)</code> adds at the end, <code>insert(i, x)</code> at position i, and <code>extend(list)</code> adds many items.</li>
<li><b>Deleting:</b> <code>remove(x)</code> deletes the first matching value (ValueError if it is not present); <code>pop()</code> / <code>pop(i)</code> delete <b>and return</b> an item; <code>del</code> deletes by index or slice; <code>clear()</code> empties the list.</li>
<li><code>del a</code> (without an index) deletes the whole list variable.</li></ul>"""),

    PP("py3p3", "Basic list operations", r'''
a = [1, 2, 3]
b = [4, 5]
print("a + b        :", a + b)          # concatenation
print("a * 3        :", a * 3)          # repetition
print("3 in a       :", 3 in a)         # membership
print("9 not in a   :", 9 not in a)
print("len(a)       :", len(a))
print("a == [1,2,3] :", a == [1, 2, 3]) # comparison
print("[1,2] < [1,3]:", [1, 2] < [1, 3])

c = a                                   # alias (same list)
d = a.copy()                            # independent copy
a.append(99)
print("a after append:", a)
print("c (alias)     :", c)
print("d (copy)      :", d)
''', (),
       r"""<ul><li><code>+</code> joins lists and <code>*</code> repeats them; both create a new list.</li>
<li><code>in</code> / <code>not in</code> test membership; <code>==</code> and <code>&lt;</code> compare lists item by item.</li>
<li><code>c = a</code> does <b>not</b> copy: both names refer to the same list, so a change through a is seen through c. <code>a.copy()</code>, <code>a[:]</code> or <code>list(a)</code> make a separate copy (see diagram "Aliasing vs Copying a List").</li></ul>"""),

    PP("py3p4", "Built-in list functions and methods", r'''
marks = [78, 85, 62, 90, 71, 85]
print("List      :", marks)
print("len()     :", len(marks))
print("max()     :", max(marks))
print("min()     :", min(marks))
print("sum()     :", sum(marks))
print("average   :", round(sum(marks) / len(marks), 2))
print("sorted()  :", sorted(marks))
print("sorted(reverse=True):", sorted(marks, reverse=True))
print("original unchanged  :", marks)

print("count(85) :", marks.count(85))
print("index(90) :", marks.index(90))
marks.sort()
print("sort()    :", marks)
marks.reverse()
print("reverse() :", marks)

names = ["riya", "Amit", "om", "Kavya"]
print("sorted names        :", sorted(names))
print("ignore case (key)   :", sorted(names, key=str.lower))
print("by length           :", sorted(names, key=len))
''', (),
       r"""<ul><li><b>Built-in functions</b> work on any sequence: <code>len()</code>, <code>max()</code>, <code>min()</code>, <code>sum()</code>, <code>sorted()</code>, <code>list()</code>.</li>
<li><b>List methods</b> are called with a dot: <code>count()</code>, <code>index()</code>, <code>sort()</code>, <code>reverse()</code>, <code>append()</code>, etc.</li>
<li><code>sorted(list)</code> returns a <b>new sorted list</b>; <code>list.sort()</code> sorts the list <b>in place</b> and returns None.</li>
<li>Capital letters come before lowercase in sorting; <code>key=str.lower</code> ignores case and <code>key=len</code> sorts by length.</li></ul>"""),

    PP("py3p5", "List programs: input list, second largest, remove duplicates", r'''
data = input("Enter numbers separated by space: ")
nums = [int(x) for x in data.split()]
print("List            :", nums)

even = [n for n in nums if n % 2 == 0]
odd = [n for n in nums if n % 2 != 0]
print("Even, odd count :", len(even), len(odd))

unique = []
for n in nums:
    if n not in unique:
        unique.append(n)
print("Without repeats :", unique)

largest = second = None
for n in unique:
    if largest is None or n > largest:
        second = largest
        largest = n
    elif second is None or n > second:
        second = n
print("Largest         :", largest)
print("Second largest  :", second)

key = int(input("Number to search: "))
if key in nums:
    print(key, "found at index", nums.index(key))
else:
    print(key, "not found")
''', ["12 45 7 45 30 12 9", "30"],
       r"""<ul><li>A list of numbers is read in one line: <code>split()</code> breaks the input into strings and each one is converted with <code>int()</code>.</li>
<li>Duplicates are removed by appending only items <b>not already present</b>; this keeps the original order. (<code>list(set(nums))</code> also removes duplicates, but may change the order.)</li>
<li>The second largest is found in one pass, by keeping track of the largest and the second largest values so far.</li></ul>"""),

    PP("py3p6", "List as stack and queue", r'''
# Stack: Last In First Out (LIFO)
stack = []
stack.append(10)
stack.append(20)
stack.append(30)
print("Stack        :", stack)
print("Pop          :", stack.pop())
print("Top (peek)   :", stack[-1])
print("Stack now    :", stack)

# Queue: First In First Out (FIFO)
queue = []
queue.append("Amit")
queue.append("Riya")
queue.append("Om")
print("Queue        :", queue)
print("Served       :", queue.pop(0))
print("Queue now    :", queue)
''', (),
       r"""<ul><li>A <b>stack</b> (LIFO) uses <code>append()</code> to push and <code>pop()</code> to remove the last item.</li>
<li>A <b>queue</b> (FIFO) adds at the end with <code>append()</code> and removes from the front with <code>pop(0)</code>. (For large queues, <code>collections.deque</code> is faster.)</li></ul>"""),

    PP("py3p7", "List comprehension", r'''
squares = [x * x for x in range(1, 11)]
print("Squares 1-10   :", squares)

evens = [x for x in range(1, 21) if x % 2 == 0]
print("Even 1-20      :", evens)

words = ["python", "is", "fun"]
upper = [w.upper() for w in words]
print("Uppercase      :", upper)
lengths = [len(w) for w in words]
print("Lengths        :", lengths)

marks = [78, 32, 90, 28, 65]
result = ["Pass" if m >= 35 else "Fail" for m in marks]
print("Result         :", result)

# same as the first comprehension using a loop
sq = []
for x in range(1, 11):
    sq.append(x * x)
print("Using loop     :", sq == squares)
''', (),
       r"""<p>A <b>list comprehension</b> creates a list in one line: <code>[expression for item in sequence if condition]</code>. It is shorter and usually faster than a loop with <code>append()</code>. An if-else can be used in the expression part, as in the Pass/Fail example.</p>"""),

    PP("py3p8", "Matrix addition and transpose (nested lists)", r'''
A = [[1, 2, 3],
     [4, 5, 6]]
B = [[7, 8, 9],
     [1, 2, 3]]
rows, cols = len(A), len(A[0])

C = []
for i in range(rows):
    row = []
    for j in range(cols):
        row.append(A[i][j] + B[i][j])
    C.append(row)

print("A + B =")
for row in C:
    print(" ", row)

T = [[A[i][j] for i in range(rows)] for j in range(cols)]
print("Transpose of A =")
for row in T:
    print(" ", row)
''', (),
       r"""<p>A matrix is stored as a <b>list of lists</b>; <code>A[i][j]</code> is the item at row i, column j. Nested loops visit every element. For the transpose, rows become columns: element [i][j] goes to [j][i]. The second version uses a nested list comprehension.</p>"""),

    PP("py3p9", "Tuple: define, access, update and delete", r'''
t = (10, 20, 30, 40, 50)
t2 = 1, "GTU", 3.5            # packing without ( )
one = (7,)                    # single-item tuple
not_tuple = (7)
print("t        :", t)
print("t2       :", t2)
print("types    :", type(one), type(not_tuple))
print("t[0], t[-1], t[1:4] :", t[0], t[-1], t[1:4])

for item in t2:
    print("item:", item)

try:
    t[0] = 99
except TypeError as e:
    print("Update error :", e)

lst = list(t)                 # convert, change, convert back
lst[0] = 99
t = tuple(lst)
print("Updated via list :", t)
t = t + (60,)                 # new tuple by concatenation
print("Added 60         :", t)

roll, name, per = (101, "Riya", 82.5)   # unpacking
print("Unpacked :", roll, name, per)
del t                         # delete whole tuple
print("Tuple deleted")
''', (),
       r"""<ul><li>A tuple is created with parentheses, or just commas (<b>packing</b>). A single-item tuple needs a <b>trailing comma</b>; <code>(7)</code> is just an int.</li>
<li>Items are accessed by index and slicing, just like a list.</li>
<li>Tuples are <b>immutable</b>: individual items cannot be changed or deleted (TypeError). To "update", convert to a list, change it and convert back, or build a new tuple with <code>+</code>.</li>
<li>The whole tuple can be deleted with <code>del t</code>. <b>Unpacking</b> assigns the items to separate variables.</li></ul>"""),

    PP("py3p10", "Tuple operations and built-in functions", r'''
a = (3, 1, 4, 1, 5)
b = (9, 2)
print("a + b      :", a + b)
print("b * 2      :", b * 2)
print("4 in a     :", 4 in a)
print("len(a)     :", len(a))
print("max, min   :", max(a), min(a))
print("sum(a)     :", sum(a))
print("sorted(a)  :", sorted(a), "(returns a list)")
print("count(1)   :", a.count(1))
print("index(4)   :", a.index(4))
print("tuple('ab'):", tuple("ab"))

students = (("Amit", 78), ("Riya", 85), ("Om", 69))
for name, marks in students:
    print(f"  {name:5} {marks}")
best = max(students, key=lambda s: s[1])
print("Topper     :", best)

point = {(0, 0): "origin", (2, 3): "P"}   # tuple as dict key
print("point[(2, 3)] =", point[(2, 3)])
''', (),
       r"""<ul><li>Tuples support <code>+</code>, <code>*</code>, <code>in</code>, indexing, slicing and looping.</li>
<li>Built-in functions <code>len()</code>, <code>max()</code>, <code>min()</code>, <code>sum()</code>, <code>sorted()</code> and <code>tuple()</code> work on tuples. sorted() returns a <b>list</b>.</li>
<li>Tuples have only two methods: <code>count()</code> and <code>index()</code>.</li>
<li>A tuple of tuples stores fixed records. <code>max(…, key=…)</code> chooses by the second item (marks).</li>
<li>Because they are immutable, tuples can be used as dictionary keys; lists cannot.</li></ul>"""),

    PP("py3p11", "Set: define, access, update and delete", r'''
s = {5, 3, 8, 3, 5}
print("Set         :", s, " (duplicates removed)")
e = set()
print("Empty set   :", e, type(e))
print("type({})    :", type({}))
print("From list   :", set([1, 2, 2, 3]))

for x in s:                      # access by looping
    print("item", x)
print("8 in s      :", 8 in s)

s.add(10)
print("add(10)     :", s)
s.update([1, 2])
print("update      :", s)
s.remove(3)
print("remove(3)   :", s)
s.discard(99)                    # no error if missing
print("discard(99) :", s)
x = s.pop()                      # removes some item
print("pop()       :", x, s)
s.clear()
print("clear()     :", s)

fs = frozenset([1, 2, 3])
print("frozenset   :", fs)
try:
    print(s[0])                  # sets cannot be indexed
except TypeError as err:
    print("Indexing error:", err)
''', (),
       r"""<ul><li>A set stores <b>unique</b> items in <b>no fixed order</b>. An empty set must be made with <code>set()</code>, because <code>{}</code> is an empty dictionary.</li>
<li>Items cannot be accessed by index (TypeError); use a loop or <code>in</code>.</li>
<li><code>add()</code> adds one item and <code>update()</code> adds many. <code>remove()</code> raises an error if the item is missing; <code>discard()</code> does not. <code>pop()</code> removes an arbitrary item.</li>
<li>A <b>frozenset</b> is an immutable set.</li>
<li>The order in which a set is printed may be different on your computer.</li></ul>"""),

    PP("py3p12", "Set operations: union, intersection, difference", r'''
cricket = {"Amit", "Riya", "Om", "Dev"}
chess = {"Riya", "Kavya", "Dev", "Meet"}

print("Cricket            :", sorted(cricket))
print("Chess              :", sorted(chess))
print("Both games (&)     :", sorted(cricket & chess))
print("Any game (|)       :", sorted(cricket | chess))
print("Only cricket (-)   :", sorted(cricket - chess))
print("Only one game (^)  :", sorted(cricket ^ chess))

A, B = {1, 2, 3, 4}, {3, 4, 5, 6}
print("A.union(B)                :", A.union(B))
print("A.intersection(B)         :", A.intersection(B))
print("A.difference(B)           :", A.difference(B))
print("A.symmetric_difference(B) :", A.symmetric_difference(B))
print("{1, 2} <= A (subset)      :", {1, 2} <= A, {1, 2}.issubset(A))
print("A >= {3} (superset)       :", A >= {3}, A.issuperset({3}))
print("A.isdisjoint({7, 8})      :", A.isdisjoint({7, 8}))
''', (),
       r"""<ul><li><b>Union</b> (<code>|</code>, union()): items in either set. <b>Intersection</b> (<code>&amp;</code>): items in both. <b>Difference</b> (<code>-</code>): items in the first set but not the second. <b>Symmetric difference</b> (<code>^</code>): items in exactly one of the sets.</li>
<li><code>issubset()</code>/<code>&lt;=</code>, <code>issuperset()</code>/<code>&gt;=</code> and <code>isdisjoint()</code> compare sets.</li>
<li><code>sorted()</code> is used so that sets of names print in a fixed order (see diagram "Set Operations").</li></ul>"""),

    PP("py3p13", "Unique words and common letters using sets", r'''
text = input("Enter a sentence: ")
words = text.lower().split()
unique = set(words)
print("Total words  :", len(words))
print("Unique words :", len(unique))
print("Sorted unique:", sorted(unique))

w1 = input("First word : ")
w2 = input("Second word: ")
common = set(w1) & set(w2)
print("Common letters :", sorted(common))
print("Letters only in first:", sorted(set(w1) - set(w2)))
''', ["the cat and the dog and the bird", "python", "planet"],
       r"""<p>Converting a list to a set removes duplicates automatically, so <code>len(set(words))</code> counts the unique words. <code>set("python")</code> makes a set of letters, and the intersection gives the letters common to both words.</p>"""),

    PP("py3p14", "Dictionary: define, access, update and delete", r'''
student = {"roll": 101, "name": "Amit", "branch": "CE"}
d2 = dict(city="Surat", pin=395001)       # dict() constructor
d3 = dict([("a", 1), ("b", 2)])           # from list of pairs
print("student :", student)
print("d2, d3  :", d2, d3)

print("student['name']       :", student["name"])
print("student.get('marks')  :", student.get("marks"))
print("get with default      :", student.get("marks", 0))
try:
    print(student["marks"])
except KeyError as e:
    print("KeyError              :", e)

student["marks"] = 78                     # add
student["branch"] = "Computer"            # update
student.update({"sem": 2, "marks": 81})   # add/update many
print("After update :", student)

removed = student.pop("branch")
print("pop('branch'):", removed, "->", student)
last = student.popitem()
print("popitem()    :", last, "->", student)
del student["roll"]
print("del roll     :", student)
student.clear()
print("clear()      :", student)
''', (),
       r"""<ul><li>A dictionary is created with <code>{key: value}</code> or <code>dict()</code>.</li>
<li><code>d[key]</code> raises a <b>KeyError</b> if the key is missing; <code>d.get(key, default)</code> returns None or the default instead.</li>
<li>Assigning <code>d[key] = value</code> adds a new pair or updates an existing one; <code>update()</code> does this for many pairs at once.</li>
<li><code>pop(key)</code> removes a key and returns its value; <code>popitem()</code> removes the last inserted pair; <code>del d[key]</code> deletes a pair; <code>clear()</code> empties the dictionary.</li></ul>"""),

    PP("py3p15", "Dictionary methods, iteration and sorting", r'''
marks = {"Riya": 85, "Amit": 78, "Om": 69, "Kavya": 91}
print("keys()   :", list(marks.keys()))
print("values() :", list(marks.values()))
print("items()  :", list(marks.items()))
print("len      :", len(marks))
print("'Om' in marks :", "Om" in marks)

for name, m in marks.items():
    print(f"  {name:6} : {m}")

print("Sorted by name  :", dict(sorted(marks.items())))
print("Sorted by marks :", sorted(marks.items(), key=lambda kv: kv[1], reverse=True))
topper = max(marks, key=marks.get)
print("Topper          :", topper, marks[topper])
print("Class average   :", sum(marks.values()) / len(marks))

copy = marks.copy()
copy["Om"] = 75
print("Original Om, copy Om :", marks["Om"], copy["Om"])
print("setdefault :", marks.setdefault("Dev", 60), marks)
print("fromkeys   :", dict.fromkeys(["a", "b", "c"], 0))
squares = {n: n * n for n in range(1, 6)}
print("comprehension :", squares)
''', (),
       r"""<ul><li><code>keys()</code>, <code>values()</code> and <code>items()</code> return views of the keys, the values and the (key, value) pairs; <code>items()</code> is used for looping over both.</li>
<li><code>sorted(d.items())</code> sorts by key. Using <code>key=lambda kv: kv[1]</code> sorts by value. <code>max(d, key=d.get)</code> finds the key with the largest value.</li>
<li><code>copy()</code> makes a separate copy. <code>setdefault()</code> adds the key only if it is missing. <code>fromkeys()</code> creates keys with the same value.</li>
<li>A <b>dictionary comprehension</b> <code>{k: v for …}</code> builds a dictionary in one line.</li></ul>"""),

    PP("py3p16", "Word and character frequency using a dictionary", r'''
text = input("Enter text: ").lower()

freq = {}
for word in text.split():
    freq[word] = freq.get(word, 0) + 1
print("Word frequency:")
for w, c in sorted(freq.items()):
    print(f"  {w:8} {c}")

chars = {}
for ch in text:
    if ch.isalpha():
        chars[ch] = chars.get(ch, 0) + 1
most = max(chars, key=chars.get)
print("Most frequent letter:", most, "->", chars[most], "times")
''', ["to be or not to be that is the question"],
       r"""<p>Counting with a dictionary is a very common pattern: <code>freq[word] = freq.get(word, 0) + 1</code> starts each new word at 0 and adds 1 every time it appears. The keys are the words and the values are the counts. The same idea counts letters.</p>"""),

    PP("py3p17", "Book management system (project): add, update, delete", r'''
books = {101: {"title": "Let Us C", "author": "Kanetkar", "qty": 5}}

while True:
    print("\n1.Add 2.Update qty 3.Delete 4.Show 5.Exit")
    ch = input("Choice: ")
    if ch == "1":
        bid = int(input("Book id: "))
        if bid in books:
            print("Id already exists")
            continue
        title = input("Title : ")
        author = input("Author: ")
        qty = int(input("Qty   : "))
        books[bid] = {"title": title, "author": author, "qty": qty}
        print("Book added")
    elif ch == "2":
        bid = int(input("Book id: "))
        if bid in books:
            books[bid]["qty"] = int(input("New qty: "))
            print("Updated")
        else:
            print("Not found")
    elif ch == "3":
        bid = int(input("Book id: "))
        print("Deleted" if books.pop(bid, None) else "Not found")
    elif ch == "4":
        print(f"{'ID':<5}{'Title':<14}{'Author':<15}{'Qty':>3}")
        for bid, b in books.items():
            print(f"{bid:<5}{b['title']:<14}{b['author']:<15}{b['qty']:>3}")
    elif ch == "5":
        print("Thank you!")
        break
    else:
        print("Invalid choice")
''', ["1", "102", "Core Python", "Nageswara Rao", "3", "2", "101", "8", "4", "3", "101", "4", "5"],
       r"""<p>Suggested project 3 from the syllabus. The books are stored in a <b>nested dictionary</b>: the book id is the key and the value is another dictionary with the details. The menu uses a <code>while True</code> loop with an if-elif ladder. Adding is <code>books[id] = {...}</code>, updating is <code>books[id]["qty"] = …</code>, and deleting is <code>books.pop(id, None)</code>, which returns None instead of raising an error when the id does not exist.</p>"""),
]

if __name__ == "__main__":
    for p in PROGRAMS:
        print("=" * 20, p["id"], p["title"]["en"]); print(p["out"])
