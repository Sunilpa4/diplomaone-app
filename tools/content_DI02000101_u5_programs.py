"""DI02000101 Unit 5 - solved Python programs (modules, packages, Matplotlib, NumPy). Outputs and plots are genuine."""
import os
import py_content
from py_content import PP

py_content.PLOT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "content", "computer", "sem2", "DI02000101", "diagrams")

MYMATH = r'''
"""mymath.py - a user-defined module."""
PI = 3.14159


def add(a, b):
    return a + b


def factorial(n):
    f = 1
    for i in range(2, n + 1):
        f *= i
    return f


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def circle_area(r):
    return PI * r * r
'''

GREET = r'''
"""greet.py - module with test code."""
def hello(name):
    return "Hello, " + name + "!"


print("greet.py: __name__ =", __name__)

if __name__ == "__main__":
    # runs only when greet.py is run directly
    print(hello("Tester"))
'''

SHAPES = {
    "shapes/__init__.py": r'''
"""shapes package."""
print("shapes package imported")
from .area import circle, rectangle
__all__ = ["area", "perimeter"]
''',
    "shapes/area.py": r'''
def circle(r):
    return round(3.14159 * r * r, 2)


def rectangle(l, b):
    return l * b
''',
    "shapes/perimeter.py": r'''
def circle(r):
    return round(2 * 3.14159 * r, 2)


def rectangle(l, b):
    return 2 * (l + b)
''',
}

COLLEGE = {
    "college/__init__.py": r'''
"""college package with sub-packages."""
NAME = "GTU Diploma"
''',
    "college/student/__init__.py": "",
    "college/student/result.py": r'''
def percentage(marks):
    return round(sum(marks) / len(marks), 2)


def grade(p):
    return "Distinction" if p >= 70 else "First" if p >= 60 else "Pass"
''',
    "college/staff/__init__.py": "",
    "college/staff/salary.py": r'''
def net_salary(basic, da_percent=50):
    return basic + basic * da_percent / 100
''',
}

PROGRAMS = [
    # ------------------------------------------------------------------ 5.1 Modules
    PP("py5p1", "math module: constants and functions", r'''
import math

print("pi            :", math.pi)
print("e             :", math.e)
print("sqrt(49)      :", math.sqrt(49))
print("isqrt(50)     :", math.isqrt(50))
print("pow(2, 10)    :", math.pow(2, 10))
print("ceil(4.2)     :", math.ceil(4.2))
print("floor(4.8)    :", math.floor(4.8))
print("ceil(-4.2)    :", math.ceil(-4.2))
print("floor(-4.2)   :", math.floor(-4.2))
print("trunc(-4.8)   :", math.trunc(-4.8))
print("fabs(-7)      :", math.fabs(-7))
print("factorial(5)  :", math.factorial(5))
print("gcd(24, 36)   :", math.gcd(24, 36))
print("lcm(4, 6)     :", math.lcm(4, 6))
print("log(100, 10)  :", math.log(100, 10))
print("log10(1000)   :", math.log10(1000))
print("log2(8)       :", math.log2(8))
print("exp(1)        :", math.exp(1))
print("radians(180)  :", math.radians(180))
print("degrees(pi)   :", math.degrees(math.pi))
print("sin(30 deg)   :", round(math.sin(math.radians(30)), 2))
print("cos(60 deg)   :", round(math.cos(math.radians(60)), 2))
print("hypot(3, 4)   :", math.hypot(3, 4))
print("comb(5, 2), perm(5, 2):", math.comb(5, 2), math.perm(5, 2))

r = float(input("Radius: "))
print("Area of circle:", round(math.pi * r ** 2, 2))
''', ["7"],
       r"""<ul><li>The <b>math</b> module is a built-in module that gives mathematical constants (pi, e) and functions. Write <code>import math</code>, then call each function as <code>math.function()</code>.</li>
<li><code>ceil()</code> rounds <b>up</b> and <code>floor()</code> rounds <b>down</b> (towards −∞); <code>trunc()</code> just removes the decimal part.</li>
<li>Trigonometric functions use <b>radians</b>, so convert degrees with <code>math.radians()</code>.</li>
<li>math.pow() and math.sqrt() always return a float; <code>isqrt()</code> returns the integer square root.</li></ul>"""),

    PP("py5p2", "Different ways of importing a module", r'''
import math                      # 1. whole module
print("1.", math.sqrt(16))

import math as m                 # 2. with alias
print("2.", m.factorial(4))

from math import pi, ceil        # 3. selected names
print("3.", pi, ceil(2.1))

from math import *               # 4. all names
print("4.", floor(7.9), gcd(12, 18))

from math import sqrt as root    # 5. name with alias
print("5.", root(81))

print("Module name :", math.__name__)
names = [n for n in dir(math) if not n.startswith("_")]
print("math has", len(names), "public names")
print("First 6     :", names[:6])
''', (),
       r"""<ul><li><code>import module</code>: names are used with the module prefix (math.sqrt).</li>
<li><code>import module as alias</code>: gives a short name (math → m).</li>
<li><code>from module import name1, name2</code>: imports only the names you need, which are then used <b>without</b> the prefix.</li>
<li><code>from module import *</code>: imports all public names. This is not recommended in big programs because names may clash.</li>
<li><code>dir(module)</code> lists everything defined in a module.</li></ul>"""),

    PP("py5p3", "Writing and importing a user-defined module", r'''
import mymath

print("PI          :", mymath.PI)
print("add(5, 7)   :", mymath.add(5, 7))
print("factorial(6):", mymath.factorial(6))
print("Area (r=3)  :", round(mymath.circle_area(3), 2))

from mymath import is_prime
primes = [n for n in range(1, 30) if is_prime(n)]
print("Primes < 30 :", primes)
print("Functions   :", [n for n in dir(mymath) if not n.startswith("_")])
print("Docstring   :", mymath.__doc__)
''', (),
       r"""<ul><li>Any <b>.py file</b> is a module. Here <i>mymath.py</i> holds a constant and four functions.</li>
<li>The main program, saved in the <b>same folder</b>, imports it with <code>import mymath</code> (the file name without .py).</li>
<li>The module's variables and functions are then used as <code>mymath.name</code>, or imported directly with <code>from mymath import is_prime</code>.</li>
<li>When a module is imported for the first time, Python compiles it into the <i>__pycache__</i> folder, which makes later imports faster.</li></ul>""",
       extra={"mymath.py": MYMATH}),

    PP("py5p4", "__name__ == \"__main__\": test code in a module", r'''
import greet

print("main.py : __name__ =", __name__)
print(greet.hello("Riya"))
''', (),
       r"""<ul><li>Every module has a built-in variable <code>__name__</code>. When the file is <b>run directly</b> it is <code>"__main__"</code>; when it is <b>imported</b> it is the module's name ("greet").</li>
<li>Code inside <code>if __name__ == "__main__":</code> therefore runs only when greet.py is run directly. That is why "Hello, Tester!" is <b>not</b> printed here.</li>
<li>Running <code>python greet.py</code> directly would print <code>greet.py: __name__ = __main__</code> and <code>Hello, Tester!</code>.</li></ul>""",
       extra={"greet.py": GREET}),

    PP("py5p5", "random module: random numbers (OTP, dice, shuffle)", r'''
import random

random.seed(10)          # same numbers every run (for testing)
print("random()        :", round(random.random(), 4))
print("randint(1, 6)   :", random.randint(1, 6))
print("randrange(0,50,5):", random.randrange(0, 50, 5))
print("uniform(1, 10)  :", round(random.uniform(1, 10), 2))
colors = ["red", "green", "blue", "yellow"]
print("choice()        :", random.choice(colors))
print("sample(3)       :", random.sample(range(1, 50), 3))
cards = [1, 2, 3, 4, 5]
random.shuffle(cards)
print("shuffle()       :", cards)

otp = "".join(str(random.randint(0, 9)) for _ in range(6))
print("6-digit OTP     :", otp)
rolls = [random.randint(1, 6) for _ in range(10)]
print("10 dice rolls   :", rolls)
''', (),
       r"""<ul><li><code>random()</code>: a float from 0.0 up to (but not including) 1.0. <code>randint(a, b)</code>: an integer from a to b, <b>both included</b>. <code>randrange(start, stop, step)</code>: stop is excluded.</li>
<li><code>uniform(a, b)</code>: a random float between a and b. <code>choice(seq)</code>: one random item. <code>sample(seq, k)</code>: k unique items. <code>shuffle(list)</code>: mixes the list in place.</li>
<li><code>seed()</code> fixes the starting point, so the same "random" numbers appear on every run. Without it, you get different numbers each time.</li></ul>"""),

    PP("py5p6", "statistics, fractions, decimal and cmath modules", r'''
import statistics as st
from fractions import Fraction
from decimal import Decimal, getcontext
import cmath

marks = [78, 85, 62, 90, 85, 71]
print("mean    :", round(st.mean(marks), 2))
print("median  :", st.median(marks))
print("mode    :", st.mode(marks))
print("stdev   :", round(st.stdev(marks), 2))
print("variance:", round(st.variance(marks), 2))

f = Fraction(1, 3) + Fraction(1, 6)
print("1/3 + 1/6       =", f)
print("Fraction(0.75)  =", Fraction(0.75))

print("0.1 + 0.2 (float)   =", 0.1 + 0.2)
print("0.1 + 0.2 (Decimal) =", Decimal("0.1") + Decimal("0.2"))
getcontext().prec = 5
print("1/7 with 5 digits   =", Decimal(1) / Decimal(7))

z = cmath.sqrt(-16)
print("cmath.sqrt(-16) =", z)
print("abs(3+4j)       =", abs(3 + 4j))
print("phase(1j)       =", round(cmath.phase(1j), 4))
''', (),
       r"""<p>Python's <b>numeric and mathematical modules</b> include:</p>
<ul><li><b>statistics</b>: mean, median, mode, standard deviation and variance.</li>
<li><b>fractions</b>: exact rational numbers (1/3 + 1/6 = 1/2).</li>
<li><b>decimal</b>: exact decimal arithmetic with a chosen precision. It avoids float errors like 0.1 + 0.2 = 0.30000000000000004, which matters for money calculations.</li>
<li><b>cmath</b>: math functions for complex numbers; for example, the square root of a negative number.</li>
<li>Also <b>math</b> and <b>random</b> (previous programs) and <b>numbers</b> (abstract number types).</li></ul>"""),

    # ------------------------------------------------------------------ 5.2 Packages
    PP("py5p7", "Writing and importing a user-defined package (shapes)", r'''
import shapes.area
print("Area of circle (r=2)  :", shapes.area.circle(2))

from shapes import perimeter
print("Perimeter of circle   :", perimeter.circle(2))

from shapes.area import rectangle
print("Area of rectangle 4x5 :", rectangle(4, 5))

from shapes.perimeter import rectangle as rect_p
print("Perimeter rectangle   :", rect_p(4, 5))

import shapes
print("Via __init__ import   :", shapes.circle(1))
print("__all__               :", shapes.__all__)
''', (),
       r"""<ul><li>A <b>package</b> is a folder of modules containing an <code>__init__.py</code> file. Here the package <i>shapes</i> has two modules: <i>area.py</i> and <i>perimeter.py</i>.</li>
<li>Modules are imported with dot notation: <code>import shapes.area</code>, <code>from shapes import perimeter</code> or <code>from shapes.area import rectangle</code>.</li>
<li><code>__init__.py</code> runs <b>once</b>, on the first import of the package (the message is printed only once). It can import functions so they are available directly, as in <code>shapes.circle</code>.</li>
<li><code>__all__</code> lists the modules imported by <code>from shapes import *</code>.</li></ul>""",
       extra=SHAPES),

    PP("py5p8", "Package with sub-packages (college)", r'''
import college
from college.student.result import percentage, grade
from college.staff import salary

print("Package :", college.NAME)
marks = [78, 85, 69, 91, 74]
p = percentage(marks)
print("Percentage:", p, "->", grade(p))
print("Net salary:", salary.net_salary(30000))
print("With DA 40%:", salary.net_salary(30000, 40))
''', (),
       r"""<ul><li>A package can contain <b>sub-packages</b> (folders inside folders), each with its own <code>__init__.py</code>, e.g. <code>college/student/result.py</code>.</li>
<li>Python follows the dotted path: <code>college.student.result</code> means the folder college → folder student → file result.py.</li>
<li>Large libraries such as NumPy and Matplotlib are organised in exactly this way (for example, <code>matplotlib.pyplot</code>).</li></ul>""",
       extra=COLLEGE),

    # ------------------------------------------------------------------ 5.3 Matplotlib
    PP("py5p9", "Matplotlib line plot: plot(), xlabel(), ylabel(), title(), grid(), show()", r'''
import matplotlib.pyplot as plt

days = [1, 2, 3, 4, 5, 6, 7]
surat = [31, 33, 32, 35, 36, 34, 33]
ahmedabad = [33, 35, 36, 38, 37, 36, 35]

plt.plot(days, surat, "o-", color="purple", label="Surat")
plt.plot(days, ahmedabad, "s--", color="orange", label="Ahmedabad")
plt.title("Maximum Temperature in a Week")
plt.xlabel("Day")
plt.ylabel("Temperature (°C)")
plt.grid(True)
plt.legend()
print("Highest in Surat:", max(surat), "°C on day", days[surat.index(max(surat))])
plt.show()
''', (),
       r"""<ul><li><code>import matplotlib.pyplot as plt</code> is the standard way to import the plotting module.</li>
<li><code>plt.plot(x, y, fmt)</code> draws a line graph; the format string "o-" means circle markers with a solid line, and "s--" means squares with a dashed line.</li>
<li><code>title()</code>, <code>xlabel()</code> and <code>ylabel()</code> add text; <code>grid(True)</code> draws grid lines; <code>legend()</code> shows the labels.</li>
<li><code>plt.show()</code> opens the plot window, shown below the output.</li></ul>""",
       plot="py5_out_line"),

    PP("py5p10", "Bar chart with bar() and saving it with savefig()", r'''
import matplotlib.pyplot as plt

subjects = ["Python", "Maths", "Physics", "English", "EW"]
marks = [85, 72, 64, 78, 90]
colors = ["#7B2CD9", "#1565C0", "#2E7D32", "#E07B00", "#C62828"]

plt.bar(subjects, marks, color=colors, width=0.6)
plt.title("Semester 2 Marks")
plt.xlabel("Subject")
plt.ylabel("Marks")
plt.ylim(0, 100)
for i, m in enumerate(marks):
    plt.text(i, m + 2, str(m), ha="center")
plt.grid(axis="y", linestyle=":")
plt.savefig("marks_bar.png")
print("Chart saved as marks_bar.png")
plt.show()
''', (),
       r"""<ul><li><code>plt.bar(categories, values)</code> draws vertical bars (<code>plt.barh()</code> draws horizontal ones). The options <code>color</code> and <code>width</code> change the look.</li>
<li><code>plt.text(x, y, s)</code> writes the value above each bar; <code>ylim()</code> sets the y-axis range.</li>
<li><code>plt.savefig("file.png")</code> saves the chart as an image file (png, jpg, pdf or svg). It must be called <b>before</b> show(), because show() clears the figure.</li></ul>""",
       plot="py5_out_bar"),

    PP("py5p11", "Histogram with hist()", r'''
import matplotlib.pyplot as plt

marks = [35, 42, 48, 51, 55, 58, 60, 62, 63, 65,
         66, 68, 70, 71, 72, 74, 75, 76, 78, 80,
         81, 83, 85, 86, 88, 90, 92, 95, 97, 45]

plt.hist(marks, bins=[30, 40, 50, 60, 70, 80, 90, 100],
         color="skyblue", edgecolor="black")
plt.title("Marks Distribution of 30 Students")
plt.xlabel("Marks range")
plt.ylabel("Number of students")
plt.grid(axis="y", alpha=0.5)

for low in range(30, 100, 10):
    n = len([m for m in marks if low <= m < low + 10])
    print(f"{low}-{low + 9}: {n}")
plt.show()
''', (),
       r"""<ul><li>A <b>histogram</b> shows how many values fall into each range (<b>bin</b>). <code>plt.hist(data, bins)</code> counts the values automatically.</li>
<li>bins can be a number (e.g. 7 equal bins) or a list of bin edges, as here. <code>edgecolor</code> draws borders between the bars.</li>
<li>Difference from a bar chart: a bar chart compares <b>categories</b>; a histogram shows the <b>distribution</b> of numeric data, with touching bars.</li></ul>""",
       plot="py5_out_hist"),

    PP("py5p12", "Pie chart with pie()", r'''
import matplotlib.pyplot as plt

items = ["Rent", "Food", "Travel", "Books", "Savings"]
amount = [6000, 4000, 1500, 1000, 2500]
explode = [0, 0, 0, 0, 0.1]

plt.pie(amount, labels=items, autopct="%1.1f%%",
        explode=explode, startangle=90, shadow=True)
plt.title("Monthly Expenses of a Student")
plt.axis("equal")
total = sum(amount)
for i, a in zip(items, amount):
    print(f"{i:8}: {a:5}  ({a / total * 100:.1f}%)")
plt.show()
''', (),
       r"""<ul><li><code>plt.pie(values, labels=…)</code> draws a circle divided into slices that are proportional to the values.</li>
<li><code>autopct="%1.1f%%"</code> prints the percentage on each slice; <code>explode</code> pulls a slice out; <code>startangle=90</code> rotates the chart to start at the top; <code>shadow</code> adds depth.</li>
<li><code>plt.axis("equal")</code> keeps the pie a perfect circle.</li></ul>""",
       plot="py5_out_pie"),

    PP("py5p13", "Multiple plots in one figure with subplot()", r'''
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 4, 1, 5, 3]

plt.figure(figsize=(8, 6))

plt.subplot(2, 2, 1)
plt.plot(x, y, "o-")
plt.title("Line")

plt.subplot(2, 2, 2)
plt.bar(x, y, color="orange")
plt.title("Bar")

plt.subplot(2, 2, 3)
plt.hist([1, 2, 2, 3, 3, 3, 4, 4, 5], bins=5, color="green")
plt.title("Histogram")

plt.subplot(2, 2, 4)
plt.pie(y, labels=["A", "B", "C", "D", "E"])
plt.title("Pie")

plt.suptitle("subplot(rows, cols, index)")
plt.tight_layout()
print("4 plots drawn in a 2 x 2 grid")
plt.show()
''', (),
       r"""<ul><li><code>plt.subplot(rows, cols, index)</code> divides the figure into a grid and selects one cell; the index starts at <b>1</b> and goes left to right, top to bottom.</li>
<li>Every plotting command after a subplot() call draws in that cell.</li>
<li><code>figure(figsize=(w, h))</code> sets the size in inches; <code>suptitle()</code> gives a title to the whole figure; <code>tight_layout()</code> prevents overlapping.</li></ul>""",
       plot="py5_out_subplot"),

    PP("py5p14", "Plotting sin and cos with NumPy and Matplotlib", r'''
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2 * np.pi, 100)   # 100 points
plt.plot(x, np.sin(x), label="sin(x)", color="purple")
plt.plot(x, np.cos(x), label="cos(x)", color="green", linestyle="--")
plt.axhline(0, color="black", linewidth=0.8)
plt.title("Sine and Cosine Waves")
plt.xlabel("x (radians)")
plt.ylabel("value")
plt.grid(True)
plt.legend()
plt.savefig("waves.png", dpi=150)
print("x has", x.size, "points from", x[0], "to", round(x[-1], 4))
plt.show()
''', (),
       r"""<ul><li><code>np.linspace(start, stop, n)</code> creates n evenly spaced points, and <code>np.sin()</code>/<code>np.cos()</code> work on the whole array at once, so no loop is needed.</li>
<li>NumPy and Matplotlib are almost always used together: NumPy computes the data and Matplotlib draws it.</li>
<li><code>savefig(…, dpi=150)</code> saves a high-resolution image.</li></ul>""",
       plot="py5_out_waves"),

    # ------------------------------------------------------------------ 5.4 NumPy
    PP("py5p15", "Creating NumPy arrays and array attributes", r'''
import numpy as np

a = np.array([10, 20, 30, 40])
b = np.array([[1, 2, 3], [4, 5, 6]])
c = np.array([1.5, 2.5, 3.5])
d = np.array([1, 2, 3], dtype=float)
e = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

for name, arr in [("a", a), ("b", b), ("c", c), ("d", d), ("e", e)]:
    print(f"{name}: shape={arr.shape} ndim={arr.ndim} size={arr.size} "
          f"dtype={arr.dtype} itemsize={arr.itemsize}")
print("b =")
print(b)
print("type(b)  :", type(b))
print("b.nbytes :", b.nbytes, "bytes")
print("mixed    :", np.array([1, 2.5, 3]))
print("as list  :", a.tolist())
''', (),
       r"""<ul><li><code>np.array(list)</code> creates an <b>ndarray</b> (n-dimensional array). All items have the <b>same type</b>; mixing int and float converts everything to float.</li>
<li><b>Attributes:</b> <code>shape</code> (size of each dimension, as a tuple), <code>ndim</code> (number of dimensions), <code>size</code> (total number of elements), <code>dtype</code> (data type), <code>itemsize</code> (bytes per element) and <code>nbytes</code> (total bytes = size × itemsize).</li>
<li>int64 and float64 use 8 bytes per element.</li></ul>"""),

    PP("py5p16", "Array initialization: zeros, ones, full, eye, arange, linspace, reshape", r'''
import numpy as np

print("zeros(4)        :", np.zeros(4))
print("ones((2, 3)) =", np.ones((2, 3), dtype=int), sep="\n")
print("full((2, 2), 7) =", np.full((2, 2), 7), sep="\n")
print("eye(3) =", np.eye(3, dtype=int), sep="\n")
print("arange(0, 10, 2):", np.arange(0, 10, 2))
print("arange(5)       :", np.arange(5))
print("linspace(0,1,5) :", np.linspace(0, 1, 5))
r = np.arange(1, 13).reshape(3, 4)
print("arange(1,13).reshape(3,4) =", r, sep="\n")
print("flatten()       :", r.flatten())
print("transpose shape :", r.T.shape)
np.random.seed(1)
print("random.randint  :", np.random.randint(1, 100, 5))
print("random.rand(3)  :", np.round(np.random.rand(3), 3))
''', (),
       r"""<ul><li><code>zeros()</code>, <code>ones()</code> and <code>full(shape, value)</code> create arrays filled with 0, 1 or any value. The shape is given as a tuple for 2-D arrays.</li>
<li><code>eye(n)</code> creates an identity matrix.</li>
<li><code>arange(start, stop, step)</code> works like range() (stop excluded); <code>linspace(start, stop, n)</code> gives n equally spaced values, <b>including</b> stop.</li>
<li><code>reshape(r, c)</code> changes the shape without changing the data (r × c must equal size); <code>flatten()</code> makes it 1-D; <code>.T</code> transposes.</li>
<li><code>np.random</code> creates arrays of random numbers.</li></ul>"""),

    PP("py5p17", "Indexing and slicing of NumPy arrays", r'''
import numpy as np

a = np.array([10, 20, 30, 40, 50, 60])
print("a[0], a[-1]   :", a[0], a[-1])
print("a[1:4]        :", a[1:4])
print("a[::2]        :", a[::2])
print("a[::-1]       :", a[::-1])

m = np.array([[1, 2, 3, 4],
              [5, 6, 7, 8],
              [9, 10, 11, 12]])
print("m[1, 2]       :", m[1, 2])
print("m[1]          :", m[1])
print("m[:, 2]       :", m[:, 2])
print("m[0:2, 1:3] =", m[0:2, 1:3], sep="\n")
print("m[-1, -1]     :", m[-1, -1])

print("a[a > 25]     :", a[a > 25])          # boolean indexing
print("m[m % 2 == 0] :", m[m % 2 == 0])
print("a[[0, 2, 5]]  :", a[[0, 2, 5]])       # fancy indexing
a[a > 40] = 0
print("a after a[a>40]=0:", a)
s = a[1:3]
s[0] = 99
print("slice is a view -> a:", a)
''', (),
       r"""<ul><li>1-D arrays are indexed and sliced like lists.</li>
<li>2-D arrays use <code>m[row, col]</code>; slices work on each axis: <code>m[:, 2]</code> is column 2 and <code>m[0:2, 1:3]</code> is a sub-matrix.</li>
<li><b>Boolean indexing</b> <code>a[a &gt; 25]</code> selects the elements that satisfy a condition; <b>fancy indexing</b> <code>a[[0, 2, 5]]</code> selects the given positions.</li>
<li>Unlike a list slice, a NumPy slice is a <b>view</b>: changing it changes the original array (use <code>.copy()</code> to avoid this).</li></ul>"""),

    PP("py5p18", "Array operations: element-wise arithmetic, broadcasting, comparison", r'''
import numpy as np

a = np.array([10, 20, 30, 40])
b = np.array([1, 2, 3, 4])
print("a + b  :", a + b)
print("a - b  :", a - b)
print("a * b  :", a * b)
print("a / b  :", a / b)
print("a ** 2 :", a ** 2)
print("a % 3  :", a % 3)
print("a + 5  :", a + 5)          # broadcasting a scalar
print("a > 15 :", a > 15)
print("sqrt(b):", np.round(np.sqrt(b), 3))

m = np.array([[1, 2, 3], [4, 5, 6]])
row = np.array([10, 20, 30])
print("m + row =", m + row, sep="\n")      # broadcasting a row
print("m * 2 =", m * 2, sep="\n")

lst = [1, 2, 3]
print("list * 2  :", lst * 2)
print("array * 2 :", np.array(lst) * 2)
''', (),
       r"""<ul><li>Arithmetic operators work <b>element by element</b> on arrays of the same shape, with no loop needed (this is called <b>vectorisation</b>).</li>
<li><b>Broadcasting:</b> a scalar or a smaller array is automatically stretched to match the shape (a + 5, m + row).</li>
<li>Comparisons give Boolean arrays. Universal functions (ufuncs) such as <code>np.sqrt()</code>, <code>np.sin()</code> and <code>np.exp()</code> also work element-wise.</li>
<li>Note the difference: <code>list * 2</code> repeats the list, while <code>array * 2</code> doubles each element.</li></ul>"""),

    PP("py5p19", "NumPy math and statistics: sum, min, max, mean, std, var", r'''
import numpy as np

marks = np.array([[78, 85, 62],
                  [90, 71, 88],
                  [65, 80, 75]])   # rows: students, cols: subjects
print("Marks =", marks, sep="\n")
print("np.sum(marks)       :", np.sum(marks))
print("np.min, np.max      :", np.min(marks), np.max(marks))
print("np.mean(marks)      :", round(np.mean(marks), 2))
print("np.std(marks)       :", round(np.std(marks), 2))
print("np.var(marks)       :", round(np.var(marks), 2))
print("Total per student   :", np.sum(marks, axis=1))
print("Average per subject :", np.round(np.mean(marks, axis=0), 2))
print("Max per subject     :", np.max(marks, axis=0))
print("Topper (row index)  :", np.argmax(np.sum(marks, axis=1)))
print("np.median           :", np.median(marks))
print("cumsum of row 0     :", np.cumsum(marks[0]))
''', (),
       r"""<ul><li><code>np.sum()</code>, <code>np.min()</code>, <code>np.max()</code>, <code>np.mean()</code>, <code>np.std()</code> (standard deviation) and <code>np.var()</code> (variance) work on the whole array by default.</li>
<li><b>axis=0</b> works <b>down the columns</b> (one result per column); <b>axis=1</b> works <b>across the rows</b> (one result per row).</li>
<li>Variance = mean of the squared deviations from the mean; standard deviation = √variance. NumPy uses the population formula (divide by n).</li>
<li><code>argmax()</code> gives the index of the largest value.</li></ul>"""),

    PP("py5p20", "np.dot(), np.cross() and np.matmul()", r'''
import numpy as np

u = np.array([1, 2, 3])
v = np.array([4, 5, 6])
print("u * v (element-wise):", u * v)
print("np.dot(u, v)        :", np.dot(u, v))
print("np.cross(u, v)      :", np.cross(u, v))

A = np.array([[1, 2],
              [3, 4]])
B = np.array([[5, 6],
              [7, 8]])
print("A * B (element-wise) =", A * B, sep="\n")
print("np.dot(A, B) =", np.dot(A, B), sep="\n")
print("np.matmul(A, B) =", np.matmul(A, B), sep="\n")
print("A @ B =", A @ B, sep="\n")

C = np.array([[1, 2, 3],
              [4, 5, 6]])          # 2 x 3
D = np.array([[1, 0],
              [0, 1],
              [2, 2]])             # 3 x 2
print("C (2x3) @ D (3x2) =", np.matmul(C, D), sep="\n")
try:
    np.matmul(C, C)
except ValueError as e:
    print("Error:", str(e).split(",")[0])
''', (),
       r"""<ul><li><code>np.dot(u, v)</code> of two vectors gives a <b>scalar</b>: 1×4 + 2×5 + 3×6 = 32.</li>
<li><code>np.cross(u, v)</code> gives a vector perpendicular to both: (2×6−3×5, 3×4−1×6, 1×5−2×4) = (−3, 6, −3).</li>
<li><code>np.matmul(A, B)</code> (or the <code>@</code> operator) is <b>matrix multiplication</b>: row × column. For 2-D arrays, np.dot gives the same result.</li>
<li>The <code>*</code> operator is element-wise, <b>not</b> matrix multiplication.</li>
<li>For matmul, the number of columns of the first matrix must equal the number of rows of the second, otherwise a ValueError is raised.</li></ul>"""),
]

if __name__ == "__main__":
    for p in PROGRAMS:
        print("=" * 20, p["id"], p["title"]["en"]); print(p["out"])
