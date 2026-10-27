"""DI02000101 Unit 5 notes part A: 5.1 Modules, 5.2 Packages."""
from py_content import make_TP

SN = {
    "mod_file": r'''
# File: mymath.py
PI = 3.14159

def add(a, b):
    return a + b

def factorial(n):
    f = 1
    for i in range(2, n + 1):
        f *= i
    return f
''',
    "mod_use": r'''
# File: main.py (same folder)
import mymath

print(mymath.add(5, 7))      # 12
print(mymath.factorial(5))   # 120
print(mymath.PI)             # 3.14159
''',
    "name_main": r'''
# File: greet.py
def hello(name):
    return "Hello, " + name

if __name__ == "__main__":
    print(hello("Tester"))   # test code
''',
    "imp1": r'''
import math
math.sqrt(25)        # 5.0
import math as m
m.factorial(5)       # 120
import math, random  # several modules
''',
    "sys_path": r'''
import sys
print(sys.path)      # folders searched
''',
    "from1": r'''
from math import sqrt, pi
sqrt(16)             # 4.0 (no prefix)
pi                   # 3.141592653589793
from math import factorial as fact
fact(4)              # 24
from math import *   # all public names
floor(3.7)           # 3
''',
    "dir_help": r'''
import math
dir(math)            # list of names
help(math.sqrt)      # documentation
math.__name__        # 'math'
''',
    "math_const": r'''
import math
math.pi        # 3.141592653589793
math.e         # 2.718281828459045
math.inf       # infinity
math.tau       # 6.283185307179586 (2*pi)
''',
    "math_round": r'''
math.ceil(4.2)     # 5
math.floor(4.8)    # 4
math.ceil(-4.2)    # -4
math.floor(-4.2)   # -5
math.trunc(-4.8)   # -4
math.fabs(-7)      # 7.0
''',
    "math_pow": r'''
math.sqrt(49)      # 7.0
math.isqrt(50)     # 7
math.pow(2, 3)     # 8.0
math.exp(1)        # 2.718281828459045
math.log(100, 10)  # 2.0
math.log10(1000)   # 3.0
math.log2(8)       # 3.0
math.log(math.e)   # 1.0 (natural log)
''',
    "math_num": r'''
math.factorial(5)  # 120
math.gcd(24, 36)   # 12
math.lcm(4, 6)     # 12
math.comb(5, 2)    # 10  (nCr)
math.perm(5, 2)    # 20  (nPr)
math.hypot(3, 4)   # 5.0
''',
    "math_trig": r'''
math.radians(180)  # 3.141592653589793
math.degrees(math.pi)   # 180.0
math.sin(math.radians(30))  # ~0.5
math.cos(0)        # 1.0
math.tan(math.radians(45))  # ~1.0
''',
    "random_ex": r'''
import random
random.random()          # 0.0 <= x < 1.0
random.randint(1, 6)     # 1..6 (inclusive)
random.randrange(0, 10, 2)  # 0,2,4,6,8
random.uniform(1, 5)     # float 1..5
random.choice(["a", "b", "c"])
random.sample(range(50), 3)  # 3 unique
random.shuffle(lst)      # in place
random.seed(10)          # repeatable
''',
    "stat_ex": r'''
import statistics as st
d = [2, 4, 4, 5, 7]
st.mean(d)       # 4.4
st.median(d)     # 4
st.mode(d)       # 4
st.stdev(d)      # sample std. deviation
''',
    "frac_dec": r'''
from fractions import Fraction
Fraction(1, 3) + Fraction(1, 6)  # 1/2
from decimal import Decimal
Decimal("0.1") + Decimal("0.2")  # 0.3
0.1 + 0.2        # 0.30000000000000004
import cmath
cmath.sqrt(-16)  # 4j
''',
    "pkg_tree": r'''
project/
    main.py
    shapes/              # package
        __init__.py
        area.py          # module
        perimeter.py     # module
''',
    "pkg_area": r'''
# File: shapes/area.py
def circle(r):
    return round(3.14159 * r * r, 2)

def rectangle(l, b):
    return l * b
''',
    "pkg_init": r'''
# File: shapes/__init__.py
from .area import circle, rectangle
__all__ = ["area", "perimeter"]
''',
    "pkg_import": r'''
import shapes.area
shapes.area.circle(2)        # 12.57

from shapes import perimeter
perimeter.rectangle(4, 5)    # 18

from shapes.area import rectangle
rectangle(4, 5)              # 20

from shapes import *         # uses __all__
''',
    "subpkg": r'''
college/
    __init__.py
    student/
        __init__.py
        result.py
    staff/
        __init__.py
        salary.py

from college.student.result import grade
''',
    "pip": r'''
pip install numpy
pip install matplotlib
pip list            # installed packages
pip show numpy      # details
pip uninstall numpy
''',
}
T = make_TP(SN)

SEC_5_1 = {
    "title": {"en": "5.1 Python Modules"},
    "items": [
        T("5.1.1 Introduction to Python Modules",
          r"""<p>A <b>module</b> is a file containing Python code (variables, functions and classes) saved with the <b>.py</b> extension. A module lets us organise related code in one file and <b>reuse</b> it in other programs by importing it.</p>
<h4>Advantages of modules</h4>
<ol><li><b>Reusability:</b> write the code once and use it in many programs.</li>
<li><b>Modularity:</b> a large program is divided into small, logical files.</li>
<li><b>Namespace separation:</b> each module has its own names, which avoids name clashes (math.sqrt vs mymath.sqrt).</li>
<li><b>Easy maintenance:</b> changes are made in one place only.</li></ol>
<h4>Types of modules</h4>
<table>
<tr><th>Type</th><th>Description</th><th>Examples</th></tr>
<tr><td>Built-in (standard library)</td><td>Installed with Python</td><td>math, random, os, sys, statistics, datetime</td></tr>
<tr><td>User-defined</td><td>Written by the programmer</td><td>mymath.py, greet.py</td></tr>
<tr><td>Third-party</td><td>Installed with pip</td><td>numpy, matplotlib, pandas</td></tr>
</table>""",
          diagram="py5_module", programs=["py5p3"]),

        T("5.1.2 Writing a Module",
          r"""<p>Writing a module is simple: create a .py file and define variables and functions in it. The file name (without .py) becomes the <b>module name</b>, so it must be a valid identifier (no spaces, and it must not start with a digit).</p>
@@mod_file@@
@@mod_use@@
<h4>The __name__ variable</h4>
<p>Each module has a built-in variable <code>__name__</code>. It equals <code>"__main__"</code> when the file is run directly, and the module name when the file is imported. Test code is therefore written inside <code>if __name__ == "__main__":</code>, so that it does not run when the module is imported.</p>
@@name_main@@
<p>When a module is imported for the first time, Python runs it once and stores the compiled bytecode in the <b>__pycache__</b> folder (.pyc files).</p>""",
          programs=["py5p3", "py5p4"]),

        T("5.1.3 Importing a Module",
          r"""<p>The <code>import</code> statement loads a module so that its contents can be used. After <code>import module</code>, the names are accessed with the <b>dot operator</b>: <code>module.name</code>.</p>
@@imp1@@
<ul><li><code>import module as alias</code> gives the module a short name, e.g. <code>import numpy as np</code>.</li>
<li>Several modules can be imported in one statement, separated by commas.</li>
<li>A module is loaded only once, even if it is imported many times.</li></ul>
<h4>Where does Python look for modules?</h4>
<ol><li>The folder of the running program (current directory)</li>
<li>The folders listed in the PYTHONPATH environment variable</li>
<li>The standard library folders</li>
<li>site-packages (third-party packages installed with pip)</li></ol>
@@sys_path@@
<p>If the module is not found, Python raises <b>ModuleNotFoundError</b>.</p>""",
          diagram="py5_import_forms", programs=["py5p2"]),

        T("5.1.4 Importing Objects from a Module",
          r"""<p>The <code>from … import …</code> statement imports specific names (functions, variables, classes) from a module. They can then be used <b>without</b> the module prefix.</p>
@@from1@@
<table>
<tr><th>import math</th><th>from math import sqrt</th></tr>
<tr><td>Imports the whole module</td><td>Imports only the given names</td></tr>
<tr><td>Use: math.sqrt(4)</td><td>Use: sqrt(4)</td></tr>
<tr><td>No name conflicts</td><td>May clash with your own names</td></tr>
</table>
<p><code>from module import *</code> imports all public names (those not starting with _). It is avoided in large programs because it can overwrite existing names silently.</p>
<h4>Exploring a module</h4>
@@dir_help@@""",
          programs=["py5p2"]),

        T("5.1.5 Built-in Mathematic Module: math",
          r"""<p>The <b>math</b> module provides mathematical constants and functions for real numbers. Import it with <code>import math</code>.</p>
<h4>Constants</h4>
@@math_const@@
<h4>Rounding functions</h4>
@@math_round@@
<h4>Power and logarithm functions</h4>
@@math_pow@@
<h4>Number-theory functions</h4>
@@math_num@@
<h4>Trigonometric functions (angles in radians)</h4>
@@math_trig@@
<table>
<tr><th>Function</th><th>Description</th></tr>
<tr><td>ceil(x) / floor(x)</td><td>Smallest integer ≥ x / largest integer ≤ x</td></tr>
<tr><td>trunc(x)</td><td>Removes the decimal part</td></tr>
<tr><td>fabs(x)</td><td>Absolute value as a float</td></tr>
<tr><td>sqrt(x), isqrt(x)</td><td>Square root (float) / integer square root</td></tr>
<tr><td>pow(x, y), exp(x)</td><td>x<sup>y</sup> (float), e<sup>x</sup></td></tr>
<tr><td>log(x[, base]), log10, log2</td><td>Logarithms</td></tr>
<tr><td>factorial(n), gcd(a, b), lcm(a, b)</td><td>n!, HCF, LCM</td></tr>
<tr><td>sin, cos, tan, radians, degrees</td><td>Trigonometry and angle conversion</td></tr>
</table>""",
          diagram="py5_math_round", programs=["py5p1"]),

        T("5.1.6 Other Numeric Modules: random, statistics, fractions, decimal, cmath",
          r"""<p>Python's standard library has a group of <b>"Numeric and Mathematical Modules"</b>: numbers, math, cmath, decimal, fractions, random and statistics.</p>
<h4>random: generating random numbers</h4>
@@random_ex@@
<p>Uses: games (dice), OTP generation, lucky draws, shuffling quiz questions and simulations.</p>
<h4>statistics</h4>
@@stat_ex@@
<h4>fractions, decimal and cmath</h4>
@@frac_dec@@
<table>
<tr><th>Module</th><th>Purpose</th></tr>
<tr><td>math</td><td>Functions for real numbers</td></tr>
<tr><td>cmath</td><td>Functions for complex numbers</td></tr>
<tr><td>random</td><td>Random numbers and choices</td></tr>
<tr><td>statistics</td><td>Mean, median, mode, standard deviation, variance</td></tr>
<tr><td>fractions</td><td>Exact rational numbers</td></tr>
<tr><td>decimal</td><td>Exact decimal arithmetic (money)</td></tr>
<tr><td>numbers</td><td>Abstract base classes for number types</td></tr>
</table>""",
          programs=["py5p5", "py5p6"]),

        T("Key Points – 5.1",
          r"""<ul>
<li>A module is a .py file of reusable code; there are built-in, user-defined and third-party modules.</li>
<li>Writing a module = saving functions in name.py; use it with <code>import name</code> from the same folder.</li>
<li>Import forms: import m; import m as x; from m import a, b; from m import *; from m import a as b.</li>
<li><code>if __name__ == "__main__":</code> runs test code only when the file is run directly.</li>
<li>dir(module) lists the names in a module; a missing module → ModuleNotFoundError.</li>
<li>math: pi, e, sqrt, pow, ceil, floor, trunc, factorial, gcd, log, sin (radians).</li>
<li>random: random, randint (both ends included), choice, shuffle, sample, seed.</li>
<li>statistics, fractions, decimal and cmath are the other numeric modules.</li>
</ul>""", key=True),
    ],
}

SEC_5_2 = {
    "title": {"en": "5.2 Python Packages"},
    "items": [
        T("5.2.1 Introduction to Packages",
          r"""<p>A <b>package</b> is a <b>folder (directory)</b> that contains related modules and a special file named <code>__init__.py</code>. Packages organise modules in a hierarchy, just as folders organise files on a computer.</p>
@@pkg_tree@@
<table>
<tr><th>Module</th><th>Package</th></tr>
<tr><td>A single .py file</td><td>A folder of modules</td></tr>
<tr><td>Contains functions, classes, variables</td><td>Contains modules and sub-packages</td></tr>
<tr><td>e.g. math, random, area.py</td><td>e.g. numpy, matplotlib, shapes</td></tr>
<tr><td>import area</td><td>import shapes.area</td></tr>
</table>
<h4>Role of __init__.py</h4>
<ul><li>It marks the folder as a Python package.</li>
<li>It runs automatically, once, when the package is first imported.</li>
<li>It can import selected functions so that they are available directly from the package, and it can define <code>__all__</code>.</li>
<li>It may be empty. (Since Python 3.3, a folder without it still works as a "namespace package", but the syllabus/exam answer is that __init__.py is required.)</li></ul>""",
          diagram="py5_package_tree", programs=["py5p7"]),

        T("5.2.2 Writing a Package",
          r"""<h4>Steps to create a user-defined package</h4>
<ol><li>Create a folder with the package name, e.g. <b>shapes</b>.</li>
<li>Create an <code>__init__.py</code> file inside it (it may be empty).</li>
<li>Add module files (area.py, perimeter.py) containing functions.</li>
<li>Write the main program <b>outside</b> the package folder (in its parent folder) and import the package.</li></ol>
@@pkg_area@@
@@pkg_init@@
<h4>Sub-packages</h4>
<p>A package can contain other packages (sub-packages), each with its own __init__.py:</p>
@@subpkg@@""",
          programs=["py5p7", "py5p8"]),

        T("5.2.3 Importing from Packages and Third-party Packages",
          r"""<p>Modules inside a package are imported with <b>dot notation</b>: <code>package.module</code> or <code>package.subpackage.module</code>.</p>
@@pkg_import@@
<ul><li><code>__all__</code> in __init__.py controls what <code>from package import *</code> imports.</li>
<li>A dot inside a package (<code>from .area import circle</code>) is a <b>relative import</b>, meaning "from this package".</li></ul>
<h4>Installing third-party packages with pip</h4>
<p><b>pip</b> (Python's package installer) downloads packages from PyPI (the Python Package Index). Commands are typed in the terminal / command prompt:</p>
@@pip@@
<p>Popular packages: <b>NumPy</b> (numerical arrays), <b>Matplotlib</b> (graphs), Pandas (data analysis), Django/Flask (web development), Requests (HTTP).</p>""",
          programs=["py5p8"]),

        T("Key Points – 5.2",
          r"""<ul>
<li>A package is a folder of modules with an __init__.py file; it can have sub-packages.</li>
<li>__init__.py marks the package, runs once on the first import, and may define __all__.</li>
<li>To write a package: create a folder → add __init__.py → add modules → import from outside.</li>
<li>Import: <code>import pkg.mod</code>, <code>from pkg import mod</code>, <code>from pkg.mod import func</code>.</li>
<li>Third-party packages are installed with <code>pip install name</code> (numpy, matplotlib).</li>
</ul>""", key=True),
    ],
}

NOTES_A = [SEC_5_1, SEC_5_2]
