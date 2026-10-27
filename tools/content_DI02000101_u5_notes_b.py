"""DI02000101 Unit 5 notes part B: 5.3 Matplotlib, 5.4 NumPy."""
from py_content import make_TP

SN = {
    "mpl_import": r'''
pip install matplotlib        # once
import matplotlib.pyplot as plt
''',
    "mpl_steps": r'''
import matplotlib.pyplot as plt
x = [1, 2, 3, 4]
y = [10, 20, 15, 25]
plt.plot(x, y)       # 1. create plot
plt.title("Sales")   # 2. decorate
plt.show()           # 3. display
''',
    "plot_ex": r'''
plt.plot(x, y)                 # line
plt.plot(x, y, "ro--")   # red o dashed
plt.plot(x, y, color="green",
         marker="s", linestyle=":",
         linewidth=2, label="2024")
plt.plot(y)          # x = 0, 1, 2, ...
''',
    "labels": r'''
plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales (Rs.)")
plt.grid(True)          # grid lines
plt.grid(axis="y")      # only y grid
plt.legend()            # uses label=
plt.xlim(0, 10)         # axis limits
plt.ylim(0, 100)
plt.xticks([1, 2], ["Jan", "Feb"])
''',
    "bar_ex": r'''
subjects = ["Py", "Maths", "EW"]
marks = [85, 72, 90]
plt.bar(subjects, marks, color="orange",
        width=0.5)
plt.barh(subjects, marks)   # horizontal
''',
    "hist_ex": r'''
marks = [35, 42, 55, 61, 64, 72, 75, 88]
plt.hist(marks, bins=5)
plt.hist(marks, bins=[30, 50, 70, 90],
         edgecolor="black")
''',
    "pie_ex": r'''
items = ["Rent", "Food", "Other"]
amt = [6000, 4000, 2000]
plt.pie(amt, labels=items,
        autopct="%1.1f%%",
        explode=[0.1, 0, 0],
        startangle=90)
plt.axis("equal")    # perfect circle
''',
    "subplot_ex": r'''
plt.subplot(1, 2, 1)  # 1 row, 2 cols, 1st
plt.plot([1, 2, 3])
plt.title("Left")
plt.subplot(1, 2, 2)     # 2nd
plt.bar(["a", "b"], [3, 5])
plt.title("Right")
plt.tight_layout()
plt.show()
''',
    "savefig_ex": r'''
plt.plot(x, y)
plt.savefig("chart.png")            # PNG
plt.savefig("chart.pdf")            # PDF
plt.savefig("chart.jpg", dpi=200)
plt.show()     # savefig BEFORE show
''',
    "list_vs_np": r'''
import numpy as np
lst = [1, 2, 3]
arr = np.array([1, 2, 3])
lst * 2      # [1, 2, 3, 1, 2, 3]
arr * 2      # [2 4 6]
lst + [10]   # [1, 2, 3, 10]
arr + 10     # [11 12 13]
''',
    "np_create": r'''
import numpy as np
a = np.array([1, 2, 3])              # 1-D
b = np.array([[1, 2], [3, 4]])       # 2-D
c = np.array((5, 6, 7))      # from tuple
d = np.array([1, 2], dtype=float)
# d = [1. 2.]
e = np.array([1, 2.5])   # all float
type(a)      # <class 'numpy.ndarray'>
''',
    "np_attr": r'''
b = np.array([[1, 2, 3], [4, 5, 6]])
b.shape      # (2, 3)
b.ndim       # 2
b.size       # 6
b.dtype      # dtype('int64')
b.itemsize   # 8 (bytes per element)
b.nbytes     # 48
''',
    "np_init": r'''
np.zeros(3)            # [0. 0. 0.]
np.zeros((2, 3))       # 2 x 3 of 0.
np.ones((2, 2), dtype=int)
np.full((2, 2), 7)     # all 7
np.eye(3)              # identity 3 x 3
np.arange(0, 10, 2)    # [0 2 4 6 8]
np.linspace(0, 1, 5)   # [0. .25 .5 .75 1.]
np.empty(3)            # uninitialised
np.random.rand(3)      # 3 floats 0..1
np.random.randint(1, 10, 5)
''',
    "np_reshape": r'''
a = np.arange(1, 7)       # [1 2 3 4 5 6]
m = a.reshape(2, 3)       # [[1 2 3]
                          #  [4 5 6]]
m.T                       # transpose 3 x 2
m.flatten()               # back to 1-D
a.reshape(4, 2)           # ValueError
''',
    "np_idx1": r'''
a = np.array([10, 20, 30, 40, 50])
a[0], a[-1]      # 10, 50
a[1:4]           # [20 30 40]
a[::-1]          # [50 40 30 20 10]
''',
    "np_idx2": r'''
m = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])
m[1, 2]          # 6  (row 1, col 2)
m[1][2]          # 6  (also works)
m[0]             # [1 2 3]  row 0
m[:, 1]          # [2 5 8]  column 1
m[0:2, 1:3]      # [[2 3] [5 6]]
''',
    "np_bool": r'''
a = np.array([5, 12, 7, 20, 3])
a > 6            # [F T T T F]
a[a > 6]         # [12  7 20]
a[[0, 2]]        # [5 7] fancy indexing
a[a > 10] = 0    # [5 0 7 0 3]
''',
    "np_view": r'''
a = np.array([1, 2, 3, 4])
s = a[0:2]       # view, not copy
s[0] = 99        # a = [99 2 3 4]
c = a[0:2].copy()   # independent
''',
    "np_ops": r'''
a = np.array([10, 20, 30])
b = np.array([1, 2, 3])
a + b        # [11 22 33]
a - b        # [ 9 18 27]
a * b        # [10 40 90]
a / b        # [10. 10. 10.]
a ** 2       # [100 400 900]
a + 5        # [15 25 35] broadcasting
a > 15       # [False True True]
''',
    "np_ufunc": r'''
np.sqrt([4, 9, 16])    # [2. 3. 4.]
np.abs([-1, 2, -3])    # [1 2 3]
np.round(np.pi, 2)     # 3.14
np.exp([0, 1])         # [1. 2.718...]
np.sin(np.pi / 2)      # 1.0
''',
    "np_broadcast": r'''
m = np.array([[1, 2, 3],
              [4, 5, 6]])
m + np.array([10, 20, 30])
# [[11 22 33]
#  [14 25 36]]
''',
    "np_stats": r'''
a = np.array([4, 8, 6, 2])
np.sum(a)      # 20
np.min(a)      # 2
np.max(a)      # 8
np.mean(a)     # 5.0
np.var(a)      # 5.0
np.std(a)      # 2.23606797749979
np.median(a)   # 5.0
np.argmax(a)   # 1 (index of max)
''',
    "np_axis": r'''
m = np.array([[1, 2],
              [3, 4]])
np.sum(m)           # 10
np.sum(m, axis=0)   # [4 6] columns
np.sum(m, axis=1)   # [3 7] rows
np.mean(m, axis=0)  # [2. 3.]
''',
    "var_calc": r'''
data = 4, 8, 6, 2       mean = 5
deviations = -1, 3, 1, -3
squares    =  1, 9, 1,  9   sum = 20
variance = 20 / 4 = 5.0
std = sqrt(5) = 2.236
''',
    "np_dot": r'''
u = np.array([1, 2, 3])
v = np.array([4, 5, 6])
np.dot(u, v)     # 1*4 + 2*5 + 3*6 = 32
u @ v            # 32 (same)
''',
    "np_cross": r'''
np.cross(u, v)   # [-3  6 -3]
# [2*6-3*5, 3*4-1*6, 1*5-2*4]
np.cross([1, 0, 0], [0, 1, 0])  # [0 0 1]
''',
    "np_matmul": r'''
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
np.matmul(A, B)  # [[19 22] [43 50]]
A @ B            # same
np.dot(A, B)     # same for 2-D
A * B            # [[ 5 12] [21 32]]
''',
}
T = make_TP(SN)

SEC_5_3 = {
    "title": {"en": "5.3 Matplotlib Package"},
    "items": [
        T("5.3.1 Introduction to Matplotlib",
          r"""<p><b>Matplotlib</b> is a third-party Python package for creating 2-D graphs and charts (data visualisation): line graphs, bar charts, histograms, pie charts, scatter plots, etc. Its <b>pyplot</b> module provides simple functions for plotting.</p>
@@mpl_import@@
<h4>Basic steps to draw a graph</h4>
<ol><li>Import pyplot: <code>import matplotlib.pyplot as plt</code></li>
<li>Prepare the data (lists or NumPy arrays).</li>
<li>Create the plot: plot(), bar(), hist(), pie().</li>
<li>Add the title, labels, grid and legend.</li>
<li>Display it with show() or save it with savefig().</li></ol>
@@mpl_steps@@
<table>
<tr><th>Function</th><th>Use</th></tr>
<tr><td>plot()</td><td>Line graph</td></tr>
<tr><td>bar()</td><td>Bar chart</td></tr>
<tr><td>hist()</td><td>Histogram</td></tr>
<tr><td>pie()</td><td>Pie chart</td></tr>
<tr><td>subplot()</td><td>Several plots in one figure</td></tr>
<tr><td>xlabel(), ylabel(), title(), grid(), legend()</td><td>Decoration</td></tr>
<tr><td>show(), savefig()</td><td>Display / save</td></tr>
</table>""",
          diagram="py5_mpl_anatomy", programs=["py5p9"]),

        T("5.3.2 plot() and show()",
          r"""<p><code>plt.plot(x, y, fmt, **options)</code> draws a <b>line graph</b> by joining the points (x, y). If only one list is given, it is used as y and x becomes 0, 1, 2, …</p>
@@plot_ex@@
<h4>Format string "[color][marker][line]"</h4>
<table>
<tr><th>Colours</th><th>Markers</th><th>Line styles</th></tr>
<tr><td>"r" red, "g" green, "b" blue, "k" black, "y" yellow, "m" magenta, "c" cyan</td><td>"o" circle, "s" square, "^" triangle, "*" star, "+" plus, "x" cross, "." point</td><td>"-" solid, "--" dashed, ":" dotted, "-." dash-dot</td></tr>
</table>
<p><code>plt.show()</code> opens a window that displays the figure. The program waits until the window is closed. Several plot() calls before show() draw several lines on the same graph.</p>""",
          programs=["py5p9", "py5p14"]),

        T("5.3.3 xlabel(), ylabel(), title(), grid() and legend()",
          r"""<table>
<tr><th>Function</th><th>Purpose</th></tr>
<tr><td>plt.title(text)</td><td>Title above the plot</td></tr>
<tr><td>plt.xlabel(text)</td><td>Label of the x-axis</td></tr>
<tr><td>plt.ylabel(text)</td><td>Label of the y-axis</td></tr>
<tr><td>plt.grid(True)</td><td>Shows grid lines (axis="x"/"y", linestyle, alpha)</td></tr>
<tr><td>plt.legend()</td><td>Box that explains each line, using label="…"</td></tr>
<tr><td>plt.xlim() / plt.ylim()</td><td>Range of the axes</td></tr>
<tr><td>plt.xticks() / plt.yticks()</td><td>Positions and labels of the tick marks</td></tr>
</table>
@@labels@@""",
          programs=["py5p9"]),

        T("5.3.4 Bar Chart: bar()",
          r"""<p>A <b>bar chart</b> compares values of different <b>categories</b> using rectangular bars whose heights are proportional to the values.</p>
<p>Syntax: <code>plt.bar(x, height, width=0.8, color=None, label=None)</code></p>
@@bar_ex@@
<ul><li>x: category names or positions; height: values.</li>
<li><code>plt.barh()</code> draws horizontal bars.</li>
<li>Uses: subject-wise marks, month-wise sales, population of cities.</li></ul>""",
          programs=["py5p10"]),

        T("5.3.5 Histogram: hist()",
          r"""<p>A <b>histogram</b> shows the <b>frequency distribution</b> of numeric data: the range of values is divided into intervals called <b>bins</b>, and the height of each bar is the number of values that fall in that bin.</p>
<p>Syntax: <code>plt.hist(data, bins=10, color=None, edgecolor=None)</code></p>
@@hist_ex@@
<table>
<tr><th>Bar chart</th><th>Histogram</th></tr>
<tr><td>Compares categories</td><td>Shows the distribution of numeric data</td></tr>
<tr><td>You give the heights</td><td>Matplotlib counts the frequencies</td></tr>
<tr><td>Gaps between the bars</td><td>Bars touch each other</td></tr>
<tr><td>plt.bar(x, height)</td><td>plt.hist(data, bins)</td></tr>
</table>""",
          programs=["py5p11"]),

        T("5.3.6 Pie Chart: pie()",
          r"""<p>A <b>pie chart</b> shows the parts of a whole as slices of a circle. The size of each slice is proportional to its share of the total.</p>
<p>Syntax: <code>plt.pie(values, labels=None, autopct=None, explode=None, colors=None, startangle=0, shadow=False)</code></p>
@@pie_ex@@
<ul><li><b>labels</b>: the name of each slice; <b>autopct</b>: shows percentages ("%1.1f%%" means 1 decimal place).</li>
<li><b>explode</b>: pulls a slice out (0.1 = 10% of the radius); <b>startangle</b>: rotates the start position.</li>
<li>Uses: monthly budget, market share, vote share.</li></ul>""",
          programs=["py5p12"]),

        T("5.3.7 Multiple Plots: subplot()",
          r"""<p><code>plt.subplot(nrows, ncols, index)</code> divides the figure into a grid of nrows × ncols cells and makes cell number <i>index</i> the current one. The index starts at <b>1</b> and counts left to right, top to bottom. It can also be written as a 3-digit number: <code>subplot(221)</code>.</p>
@@subplot_ex@@
<ul><li><code>plt.figure(figsize=(w, h))</code> sets the figure size in inches.</li>
<li><code>plt.suptitle()</code> gives a title to the whole figure; <code>plt.tight_layout()</code> adjusts the spacing.</li></ul>""",
          programs=["py5p13"]),

        T("5.3.8 Saving a Plot: savefig()",
          r"""<p><code>plt.savefig(filename, dpi=…)</code> saves the current figure as an image file. The format is chosen from the extension: .png, .jpg, .pdf or .svg.</p>
@@savefig_ex@@
<ul><li>Call savefig() <b>before</b> show(), because show() clears the figure after the window is closed, so a later savefig() would save a blank image.</li>
<li><b>dpi</b> (dots per inch) controls the resolution; <code>bbox_inches="tight"</code> removes extra white space.</li></ul>""",
          programs=["py5p10", "py5p14"]),

        T("Key Points – 5.3",
          r"""<ul>
<li>Matplotlib is a plotting package: <code>import matplotlib.pyplot as plt</code>.</li>
<li>plot(x, y, "ro--") draws a line graph; show() displays the figure.</li>
<li>title(), xlabel(), ylabel(), grid(), legend(), xlim()/ylim() decorate the plot.</li>
<li>bar() compares categories; hist(data, bins) shows a distribution; pie(values, labels, autopct) shows parts of a whole.</li>
<li>subplot(rows, cols, index) puts several plots in one figure; the index starts at 1.</li>
<li>savefig("a.png") saves the plot; call it before show().</li>
</ul>""", key=True),
    ],
}

SEC_5_4 = {
    "title": {"en": "5.4 NumPy Package"},
    "items": [
        T("5.4.1 Introduction to NumPy",
          r"""<p><b>NumPy</b> (Numerical Python) is a third-party package for fast numerical computing. Its main object is the <b>ndarray</b> (n-dimensional array): a grid of values that all have the <b>same data type</b>. It is the base of data science libraries such as Pandas, SciPy and scikit-learn. Install it with <code>pip install numpy</code> and import it as <code>import numpy as np</code>.</p>
@@list_vs_np@@
<table>
<tr><th>Python list</th><th>NumPy array</th></tr>
<tr><td>Can hold mixed types</td><td>All elements of one type (homogeneous)</td></tr>
<tr><td>Slower; more memory</td><td>Much faster; less memory (stored in one block)</td></tr>
<tr><td>No element-wise maths (list * 2 repeats)</td><td>Element-wise maths (array * 2 doubles)</td></tr>
<tr><td>Size can change (append)</td><td>Fixed size once created</td></tr>
<tr><td>Built-in</td><td>Needs import numpy</td></tr>
</table>
<p>Uses: matrices, scientific calculations, image processing, statistics and machine learning.</p>""",
          programs=["py5p18"]),

        T("5.4.2 Creating NumPy Arrays",
          r"""<p><code>np.array(object, dtype=None)</code> converts a list, a tuple or nested lists into an ndarray.</p>
@@np_create@@
<ul><li>A list of lists gives a <b>2-D array</b> (matrix); a third level of nesting gives a 3-D array.</li>
<li>If the types are mixed, NumPy converts all elements to the most general type (int → float → str).</li>
<li><code>dtype</code> sets the type explicitly: int, float, complex, bool, str.</li></ul>""",
          diagram="py5_np_array", programs=["py5p15"]),

        T("5.4.3 Array Attributes: shape, ndim, size, dtype, itemsize",
          r"""<table>
<tr><th>Attribute</th><th>Meaning</th><th>For [[1, 2, 3], [4, 5, 6]]</th></tr>
<tr><td>shape</td><td>Tuple giving the size of each dimension (rows, columns)</td><td>(2, 3)</td></tr>
<tr><td>ndim</td><td>Number of dimensions (axes)</td><td>2</td></tr>
<tr><td>size</td><td>Total number of elements (product of shape)</td><td>6</td></tr>
<tr><td>dtype</td><td>Data type of the elements</td><td>int64</td></tr>
<tr><td>itemsize</td><td>Memory of one element in bytes</td><td>8</td></tr>
<tr><td>nbytes</td><td>Total memory = size × itemsize</td><td>48</td></tr>
</table>
@@np_attr@@
<p>Attributes are written <b>without brackets</b> (a.shape), because they are not functions.</p>""",
          programs=["py5p15"]),

        T("5.4.4 Array Initialization",
          r"""<p>NumPy has functions that create arrays filled with initial values, without typing every element:</p>
<table>
<tr><th>Function</th><th>Creates</th></tr>
<tr><td>np.zeros(shape)</td><td>All 0 (float by default)</td></tr>
<tr><td>np.ones(shape)</td><td>All 1</td></tr>
<tr><td>np.full(shape, value)</td><td>All elements = value</td></tr>
<tr><td>np.eye(n) / np.identity(n)</td><td>Identity matrix</td></tr>
<tr><td>np.arange(start, stop, step)</td><td>Evenly spaced values; stop excluded</td></tr>
<tr><td>np.linspace(start, stop, num)</td><td>num equally spaced values; stop included</td></tr>
<tr><td>np.empty(shape)</td><td>Uninitialised (garbage values; fast)</td></tr>
<tr><td>np.random.rand(n), randint(a, b, n)</td><td>Random values</td></tr>
</table>
@@np_init@@
<h4>Changing the shape</h4>
@@np_reshape@@""",
          programs=["py5p16"]),

        T("5.4.5 Indexing and Slicing",
          r"""<h4>1-D arrays: same as lists</h4>
@@np_idx1@@
<h4>2-D arrays: arr[row, column]</h4>
@@np_idx2@@
<h4>Boolean and fancy indexing</h4>
<p>A condition gives a Boolean array, which can be used to select (filter) elements. A list of indexes selects those positions.</p>
@@np_bool@@
<h4>Slices are views</h4>
@@np_view@@""",
          diagram="py5_np_slicing", programs=["py5p17"]),

        T("5.4.6 Array Operations",
          r"""<p>Arithmetic on arrays happens <b>element by element</b>, without loops. This is called <b>vectorisation</b> and is much faster than Python loops.</p>
@@np_ops@@
<h4>Broadcasting</h4>
<p>When the shapes differ, NumPy automatically "stretches" the smaller array (or scalar) to match the bigger one, if the shapes are compatible.</p>
@@np_broadcast@@
<h4>Universal functions (ufuncs)</h4>
@@np_ufunc@@""",
          programs=["py5p18"]),

        T("5.4.7 Basic Math and Statistics Functions",
          r"""<table>
<tr><th>Function</th><th>Returns</th></tr>
<tr><td>np.sum(a)</td><td>Sum of the elements</td></tr>
<tr><td>np.min(a) / np.max(a)</td><td>Smallest / largest element</td></tr>
<tr><td>np.mean(a)</td><td>Average = sum / count</td></tr>
<tr><td>np.var(a)</td><td>Variance = mean of (x − mean)²</td></tr>
<tr><td>np.std(a)</td><td>Standard deviation = √variance</td></tr>
<tr><td>np.median(a)</td><td>Middle value</td></tr>
<tr><td>np.argmin(a) / np.argmax(a)</td><td>Index of the min / max</td></tr>
</table>
@@np_stats@@
<h4>Working of var and std for [4, 8, 6, 2]</h4>
@@var_calc@@
<h4>The axis parameter (2-D arrays)</h4>
<p><b>axis=0</b> works down the columns (result per column); <b>axis=1</b> works across the rows (result per row). Without axis, all elements are used.</p>
@@np_axis@@""",
          diagram="py5_np_axis", programs=["py5p19"]),

        T("5.4.8 np.dot(), np.cross() and np.matmul()",
          r"""<h4>np.dot(a, b): dot product</h4>
<p>For two vectors, the dot product is the sum of the products of corresponding elements, a <b>scalar</b>: a·b = a₁b₁ + a₂b₂ + a₃b₃.</p>
@@np_dot@@
<h4>np.cross(a, b): cross product</h4>
<p>For two 3-D vectors, it gives a <b>vector perpendicular</b> to both: a × b = (a₂b₃ − a₃b₂, a₃b₁ − a₁b₃, a₁b₂ − a₂b₁).</p>
@@np_cross@@
<h4>np.matmul(A, B): matrix multiplication</h4>
<p>Each element of the result = (row of A) · (column of B). The number of columns of A must equal the number of rows of B: (m × n) @ (n × p) → (m × p). The <code>@</code> operator does the same.</p>
@@np_matmul@@
<table>
<tr><th>Operation</th><th>Meaning</th><th>Result for vectors</th></tr>
<tr><td>a * b</td><td>Element-wise product</td><td>Array</td></tr>
<tr><td>np.dot(a, b)</td><td>Dot product (matrix product for 2-D)</td><td>Scalar</td></tr>
<tr><td>np.cross(a, b)</td><td>Cross product</td><td>Perpendicular vector</td></tr>
<tr><td>np.matmul(a, b) / a @ b</td><td>Matrix multiplication</td><td>Scalar for 1-D, matrix for 2-D</td></tr>
</table>""",
          diagram="py5_np_ops", programs=["py5p20"]),

        T("Key Points – 5.4",
          r"""<ul>
<li>NumPy gives the fast, homogeneous ndarray: <code>import numpy as np; a = np.array([1, 2, 3])</code>.</li>
<li>Attributes: shape (tuple), ndim, size, dtype, itemsize (bytes per element), nbytes.</li>
<li>Initialization: zeros, ones, full, eye, arange (stop excluded), linspace (stop included), random; reshape changes the shape.</li>
<li>Indexing: a[i], m[row, col], m[:, c], m[r1:r2, c1:c2], a[a &gt; 5]; slices are views.</li>
<li>Operations are element-wise; broadcasting handles scalars and rows.</li>
<li>np.sum, min, max, mean, std, var, median; axis=0 → columns, axis=1 → rows.</li>
<li>dot → scalar for vectors; cross → perpendicular vector; matmul / @ → matrix product; * is element-wise.</li>
</ul>""", key=True),
    ],
}

NOTES_B = [SEC_5_3, SEC_5_4]
