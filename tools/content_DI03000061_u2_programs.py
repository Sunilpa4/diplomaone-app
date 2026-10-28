"""DI03000061 RWPD Unit 2 – Bootstrap grid, images, typography, tables, forms, buttons, carets, show/hide (practicals 3-8)."""
from web_content import WE, page

P = []
BOX = """
.box { background: #EADDF7; border: 1px solid #7B2CD9;
       padding: 10px; text-align: center; }
"""

# ------------------------------------------------------------------ 2.1 Grid
P.append(WE("w2_1", "Student information using container and container-fluid (Practical 3)", page("Containers", """
<div class="container-fluid bg-primary text-white py-3">
  <h1 class="h4 mb-0">.container-fluid: always 100% wide</h1>
</div>

<div class="container border border-primary my-3 p-3">
  <h2 class="h5">.container: fixed width per breakpoint</h2>
  <table class="table table-bordered mb-0">
    <tr><th>Name</th><td>Riya Patel</td></tr>
    <tr><th>Enrolment No.</th><td>246070307051</td></tr>
    <tr><th>Branch</th><td>Computer Engineering</td></tr>
    <tr><th>Semester</th><td>3</td></tr>
    <tr><th>College</th><td>GP Surat</td></tr>
  </table>
</div>

<div class="container-md bg-light border p-3 mb-3">
  .container-md: 100% wide below 768 px, then fixed
</div>

<footer class="container-fluid bg-dark text-white
  text-center py-2">
  Footer in .container-fluid
</footer>
"""),
"""A full-width blue header strip, then a box with a blue border holding the student details table (name, enrolment number, branch, semester, college), a grey .container-md box and a full-width black footer.
On a phone (390 px) every block is full width. On a desktop (1100 px) the header and footer still stretch edge to edge, while the student box and the grey box are 960 px wide and centred with white space on both sides.""",
"""
<ul><li><b>.container</b> is a responsive <b>fixed-width</b> box, centred with auto margins. Its max-width is 540, 720, 960, 1140 and 1320 px at sm, md, lg, xl and xxl; below 576 px it is 100%.</li>
<li><b>.container-fluid</b> is always <b>100% wide</b>, at every screen size; it suits headers, footers and full-width banners.</li>
<li><b>.container-{breakpoint}</b> (e.g. <code>.container-md</code>) is 100% wide until that breakpoint and then behaves like .container.</li>
<li>Every container has horizontal padding (gutter) so content does not touch the screen edge.</li>
<li>Utilities used: <code>bg-primary</code>, <code>text-white</code>, <code>py-3</code> (vertical padding), <code>my-3</code> (vertical margin), <code>border</code>.</li></ul>
"""))

P.append(WE("w2_2", "Grid basics: rows, columns, sizes and breakpoints", page("Grid Basics", """
<div class="container py-3">
  <p class="fw-bold mb-1">1. Equal-width columns: .col</p>
  <div class="row mb-3">
    <div class="col"><div class="box">col</div></div>
    <div class="col"><div class="box">col</div></div>
    <div class="col"><div class="box">col</div></div>
  </div>

  <p class="fw-bold mb-1">2. Fixed: col-3 + col-6 + col-3</p>
  <div class="row mb-3">
    <div class="col-3"><div class="box">3</div></div>
    <div class="col-6"><div class="box">6</div></div>
    <div class="col-3"><div class="box">3</div></div>
  </div>

  <p class="fw-bold mb-1">3. Responsive: col-12 col-md-4</p>
  <div class="row g-2 mb-3">
    <div class="col-12 col-md-4"><div class="box">A</div></div>
    <div class="col-12 col-md-4"><div class="box">B</div></div>
    <div class="col-12 col-md-4"><div class="box">C</div></div>
  </div>

  <p class="fw-bold mb-1">4. Auto width: col-auto + col</p>
  <div class="row mb-3">
    <div class="col-auto"><div class="box">col-auto</div></div>
    <div class="col"><div class="box">col (rest)</div></div>
  </div>

  <p class="fw-bold mb-1">5. row-cols-2 row-cols-md-4</p>
  <div class="row row-cols-2 row-cols-md-4 g-2">
    <div class="col"><div class="box">1</div></div>
    <div class="col"><div class="box">2</div></div>
    <div class="col"><div class="box">3</div></div>
    <div class="col"><div class="box">4</div></div>
  </div>
</div>
""", style=BOX),
"""Five lavender demo rows.
1. Three equal columns side by side. 2. Columns of widths 3, 6 and 3 (the middle one is twice as wide). 3. A, B and C stacked on a phone, but in one row of three from 768 px. 4. A narrow box that is only as wide as its text, with the rest of the row filled by the second box. 5. Two boxes per row on a phone, four per row from 768 px.""",
"""
<ul><li>The grid structure is always <b>.container &gt; .row &gt; .col-*</b>. Content goes inside the columns, and only columns may be direct children of a row.</li>
<li>Each row has <b>12 columns</b>. <code>col-3 + col-6 + col-3 = 12</code>. If the total is more than 12, the extra columns wrap to a new line.</li>
<li><code>.col</code> without a number makes equal-width columns that share the row automatically.</li>
<li><code>.col-md-4</code> means 4 of 12 columns <b>from md (768 px) upward</b>; below that, <code>col-12</code> gives full width (mobile first).</li>
<li><code>.col-auto</code> sizes a column to its content. <code>row-cols-*</code> sets the number of columns per row on the row itself.</li>
<li><code>g-2</code> sets the <b>gutter</b> (gap) between columns; <code>gx-*</code> horizontal and <code>gy-*</code> vertical only.</li></ul>
"""))

P.append(WE("w2_3", "Offset columns", page("Offset Columns", """
<div class="container py-3">
  <h1 class="h5">Offset columns</h1>
  <div class="row mb-2">
    <div class="col-4"><div class="box">col-4</div></div>
    <div class="col-4 offset-4">
      <div class="box">col-4 offset-4</div></div>
  </div>
  <div class="row mb-2">
    <div class="col-6 offset-3">
      <div class="box">col-6 offset-3 (centred)</div></div>
  </div>
  <div class="row mb-2">
    <div class="col-md-5 offset-md-2">
      <div class="box">col-md-5 offset-md-2</div></div>
  </div>
  <div class="row">
    <div class="col-3"><div class="box">col-3</div></div>
    <div class="col-3 ms-auto">
      <div class="box">ms-auto</div></div>
  </div>
</div>
""", style=BOX),
"""Row 1: a box on the left and a box on the right, with an empty gap of 4 columns between them.
Row 2: one box of half width, centred (3 empty columns on each side).
Row 3: on a phone the box is full width; from 768 px it is 5 columns wide and starts after 2 empty columns.
Row 4: one box at the far left and one pushed to the far right.""",
"""
<ul><li><b>Offset</b> moves a column to the right by adding empty columns before it (it adds <code>margin-left</code>).</li>
<li><code>.offset-4</code> leaves 4 empty columns; total = offset + width must be 12 or less.</li>
<li><code>.col-6 .offset-3</code> centres a half-width column: 3 + 6 + 3 = 12.</li>
<li><b>Responsive offsets</b> such as <code>.offset-md-2</code> work only from that breakpoint upward; use <code>.offset-md-0</code> to reset at a larger size.</li>
<li><b>Margin utilities</b> <code>ms-auto</code> (margin-start: auto) and <code>me-auto</code> push columns to the opposite side.</li>
<li>Bootstrap 3 used <code>col-md-offset-2</code>; Bootstrap 4/5 use <code>offset-md-2</code>.</li></ul>
"""))

P.append(WE("w2_4", "Reordering columns with order classes", page("Reordering", """
<div class="container py-3">
  <h1 class="h5">Reordering columns</h1>
  <p class="small text-muted">HTML order: First, Second, Third</p>
  <div class="row g-2 mb-3">
    <div class="col-md-4"><div class="box">First</div></div>
    <div class="col-md-4 order-md-last">
      <div class="box">Second (order-md-last)</div></div>
    <div class="col-md-4 order-first order-md-0">
      <div class="box">Third (order-first)</div></div>
  </div>

  <p class="small text-muted">order-1, order-2, order-3</p>
  <div class="row g-2">
    <div class="col-4 order-3"><div class="box">A</div></div>
    <div class="col-4 order-1"><div class="box">B</div></div>
    <div class="col-4 order-2"><div class="box">C</div></div>
  </div>
</div>
""", style=BOX),
"""Group 1 on a phone shows the boxes stacked as Third, First, Second. On a desktop (768 px and wider) they appear in one row as First, Third, Second, even though the HTML order is First, Second, Third.
Group 2 always shows B, C, A, because of the order-1, order-2 and order-3 classes.""",
"""
<ul><li><b>Reordering</b> changes the <b>visual order</b> of columns without changing the HTML order. It uses the CSS flexbox <code>order</code> property.</li>
<li><code>.order-0</code> to <code>.order-5</code> set the order number; lower numbers come first. Columns without a class have order 0.</li>
<li><code>.order-first</code> (order -1) puts a column first and <code>.order-last</code> (order 6) puts it last.</li>
<li>Responsive versions such as <code>.order-md-last</code> apply only from that breakpoint, so the order can be different on phone and desktop.</li>
<li>Typical use: on a phone show the main content first and the sidebar after it, but on a desktop show the sidebar on the left.</li>
<li>Bootstrap 3 used <code>col-md-push-*</code> / <code>col-md-pull-*</code> instead.</li></ul>
"""))

P.append(WE("w2_5", "Nesting columns", page("Nesting", """
<div class="container py-3">
  <h1 class="h5">Nesting columns</h1>
  <div class="row g-2">
    <div class="col-md-8">
      <div class="box">
        Level 1: col-md-8
        <div class="row g-2 mt-1">
          <div class="col-6">
            <div class="box bg-white">Level 2: col-6</div>
          </div>
          <div class="col-6">
            <div class="box bg-white">Level 2: col-6</div>
          </div>
          <div class="col-4">
            <div class="box bg-white">col-4</div></div>
          <div class="col-4">
            <div class="box bg-white">col-4</div></div>
          <div class="col-4">
            <div class="box bg-white">col-4</div></div>
        </div>
      </div>
    </div>
    <div class="col-md-4">
      <div class="box">Level 1: col-md-4</div>
    </div>
  </div>
</div>
""", style=BOX),
"""A big lavender box "Level 1: col-md-8" contains its own row of two white boxes (col-6 each) and then three smaller white boxes (col-4 each). Next to it (on a desktop) or below it (on a phone) is the box "Level 1: col-md-4".
The inner boxes always split the parent's width into 12 again.""",
"""
<ul><li><b>Nesting</b> means placing a new <code>.row</code> inside an existing column, and then columns inside that row.</li>
<li>The nested row again has <b>12 columns</b>, measured relative to the width of the parent column, not the whole page. So the inner <code>col-6</code> is half of the col-md-8 column.</li>
<li>A nested row must be <b>inside a column</b>, never directly inside another row.</li>
<li>Nesting is used for complex layouts, e.g. a main area with a list of product cards inside it.</li>
<li>There is no limit on nesting depth, but too many levels make the HTML hard to read.</li></ul>
"""))

P.append(WE("w2_6", "Responsive page with offset, reorder and nesting (Practical 4)", page("Department Page", """
<header class="bg-primary text-white text-center py-3">
  <h1 class="h4 mb-0">Computer Engineering Department</h1>
</header>
<div class="container my-3">
  <div class="row g-3">
    <main class="col-md-8 order-md-2">
      <div class="p-3 border rounded">
        <h2 class="h5">Latest News</h2>
        <div class="row g-2">
          <div class="col-sm-6">
            <div class="p-2 bg-light">Hackathon on 12 Dec</div>
          </div>
          <div class="col-sm-6">
            <div class="p-2 bg-light">Seminar on AI</div>
          </div>
        </div>
      </div>
    </main>
    <aside class="col-md-4 order-md-1">
      <div class="p-3 bg-warning-subtle rounded">
        <h2 class="h5">Quick Links</h2>
        <ul class="mb-0">
          <li>Syllabus</li><li>Time table</li>
          <li>Results</li>
        </ul>
      </div>
    </aside>
  </div>
  <div class="row mt-3">
    <div class="col-md-6 offset-md-3">
      <div class="p-3 bg-success text-white text-center
        rounded">Contact: hod.ce@gpsurat.ac.in</div>
    </div>
  </div>
</div>
"""),
"""A blue header, then "Latest News" (with two grey news boxes) and a yellow "Quick Links" list, and finally a green contact box.
On a phone: News first, then Quick Links, then the full-width contact box. On a desktop: Quick Links on the left (4 columns), News on the right (8 columns) with its two news boxes side by side, and the contact box centred below at half width.""",
"""
<ul><li><b>Reordering:</b> in the HTML, &lt;main&gt; comes first so phones show the important news first. <code>order-md-1</code> / <code>order-md-2</code> move the sidebar to the left on larger screens.</li>
<li><b>Nesting:</b> the news section contains its own <code>.row</code> with two <code>col-sm-6</code> columns.</li>
<li><b>Offset:</b> <code>col-md-6 offset-md-3</code> centres the contact box on medium and larger screens.</li>
<li>Semantic tags &lt;header&gt;, &lt;main&gt; and &lt;aside&gt; can be used as columns by giving them col classes.</li>
<li><code>bg-warning-subtle</code> is a light background colour added in Bootstrap 5.3.</li></ul>
"""))

P.append(WE("w2_7", "Class time table using the grid system (Practical 5)", page("Time Table", """
<div class="container py-3">
  <h1 class="h4 text-center">CE Semester 3 - Time Table</h1>
  <div class="row g-0 text-center fw-bold bg-primary
    text-white d-none d-md-flex">
    <div class="col-md-2 p-2">Day</div>
    <div class="col-md-2 p-2">10:30</div>
    <div class="col-md-2 p-2">11:30</div>
    <div class="col-md-2 p-2">12:30</div>
    <div class="col-md-2 p-2">2:00</div>
    <div class="col-md-2 p-2">3:00</div>
  </div>
  <div class="row g-0 text-center tt">
    <div class="col-12 col-md-2 day">Monday</div>
    <div class="col-6 col-md-2">DS</div>
    <div class="col-6 col-md-2">RDBMS</div>
    <div class="col-6 col-md-2">OS</div>
    <div class="col-6 col-md-4 lab">RWPD Lab</div>
  </div>
  <div class="row g-0 text-center tt">
    <div class="col-12 col-md-2 day">Tuesday</div>
    <div class="col-6 col-md-2">CN</div>
    <div class="col-6 col-md-2">DE</div>
    <div class="col-6 col-md-2">DS</div>
    <div class="col-6 col-md-4 lab">DS Lab</div>
  </div>
  <div class="row g-0 text-center tt">
    <div class="col-12 col-md-2 day">Wednesday</div>
    <div class="col-6 col-md-2">OS</div>
    <div class="col-6 col-md-2">RDBMS</div>
    <div class="col-6 col-md-2">CN</div>
    <div class="col-6 col-md-4 lab">RDBMS Lab</div>
  </div>
</div>
""", style="""
.tt > div { border: 1px solid #ccc; padding: 8px; }
.tt .day { background: #EADDF7; font-weight: bold; }
.tt .lab { background: #E3F5E6; }
"""),
"""A time table titled "CE Semester 3 - Time Table".
On a desktop it looks like a normal table: a blue header row (Day, 10:30 ... 3:00), then one row per day with three lectures and a green 2-hour lab spanning two periods.
On a phone the header is hidden; each day name appears as a full-width lavender bar with its subjects below it, two per line.""",
"""
<ul><li>Each day is a <code>.row</code>; the day name and periods are columns: 2 + 2 + 2 + 2 + 4 = 12 on desktop. The lab uses <code>col-md-4</code> because it lasts two periods.</li>
<li>On a phone, <code>col-12</code> makes the day name full width and <code>col-6</code> places two subjects per line.</li>
<li>The header row uses <code>d-none d-md-flex</code>: hidden on phones and shown (as a flex row) from 768 px.</li>
<li><code>g-0</code> removes gutters so the cells touch like table cells; borders are added with a small CSS rule.</li>
<li>A real &lt;table&gt; inside <code>.table-responsive</code> is another way (see the tables program); the grid version rearranges itself instead of scrolling.</li></ul>
"""))

# ------------------------------------------------------------------ 2.2 Images, typography, tables
P.append(WE("w2_8", "Responsive images and image shapes", page("Images", """
<div class="container py-3">
  <h1 class="h5">1. Responsive image: .img-fluid</h1>
  <img src="images/campus.jpg" alt="College campus"
    width="1200" height="400" class="img-fluid mb-3">

  <h2 class="h5">2. Image shapes</h2>
  <div class="row g-3 text-center">
    <div class="col-6 col-md-3">
      <img src="images/a.jpg" alt="rounded" width="300"
        height="300" class="img-fluid rounded">
      <p class="small">.rounded</p>
    </div>
    <div class="col-6 col-md-3">
      <img src="images/b.jpg" alt="circle" width="300"
        height="300" class="img-fluid rounded-circle">
      <p class="small">.rounded-circle</p>
    </div>
    <div class="col-6 col-md-3">
      <img src="images/c.jpg" alt="thumbnail" width="300"
        height="300" class="img-fluid img-thumbnail">
      <p class="small">.img-thumbnail</p>
    </div>
    <div class="col-6 col-md-3">
      <img src="images/d.jpg" alt="pill" width="300"
        height="200" class="img-fluid rounded-pill">
      <p class="small">.rounded-pill</p>
    </div>
  </div>

  <h2 class="h5">3. Figure with caption, centred image</h2>
  <figure class="figure text-center d-block">
    <img src="images/lab.jpg" alt="Computer lab" width="400"
      height="250" class="figure-img img-fluid rounded">
    <figcaption class="figure-caption">
      Fig. 1: Computer lab</figcaption>
  </figure>
</div>
"""),
"""1. A wide campus image that always fits the screen width (it shrinks on a phone and never overflows).
2. Four coloured placeholder images (they stand for real photos): one with rounded corners, one cut into a circle, one with a white border and padding like a thumbnail, and one with pill-shaped (capsule) ends. Two per row on a phone, four per row on a desktop.
3. A centred lab image with the grey caption "Fig. 1: Computer lab".""",
"""
<ul><li><b>.img-fluid</b> sets <code>max-width: 100%; height: auto;</code> so the image scales down with its parent but never grows bigger than its real size. Bootstrap 3 called this <code>.img-responsive</code>.</li>
<li><b>Image shapes:</b> <code>.rounded</code> (rounded corners), <code>.rounded-circle</code> (circle; a square image gives a perfect circle), <code>.img-thumbnail</code> (1 px border, padding, rounded), <code>.rounded-pill</code>. Sizes: <code>rounded-0</code> to <code>rounded-5</code>.</li>
<li><b>Aligning images:</b> <code>.float-start</code>, <code>.float-end</code>, or <code>.d-block mx-auto</code> to centre a block image; <code>text-center</code> on the parent centres inline images.</li>
<li><b>Figures:</b> <code>.figure</code>, <code>.figure-img</code> and <code>.figure-caption</code> show an image with a caption.</li>
<li>Always give <code>alt</code> text (for screen readers and when an image fails). In the app preview, missing photos are shown as labelled colour placeholders.</li></ul>
"""))

P.append(WE("w2_9", "Bootstrap typography: blog page (Practical 7)", page("Blog", """
<div class="container py-3">
  <h1 class="display-5">Tech Blog</h1>
  <p class="lead">Notes and ideas for diploma students.</p>
  <hr>
  <h2>Why learn Bootstrap?
    <small class="text-body-secondary">a quick guide</small>
  </h2>
  <p class="text-muted small">Posted on 28 Oct 2026 by
    <abbr title="Head of Department">HOD</abbr></p>
  <p>Bootstrap helps you build <mark>responsive</mark>
    pages quickly. You write <strong>less CSS</strong>
    and get a <em>consistent</em> design.
    Old way: <del>fixed-width tables</del>,
    new way: <ins>flexbox grid</ins>.</p>
  <blockquote class="blockquote border-start border-4
    ps-3">
    <p>Write less, do more.</p>
    <footer class="blockquote-footer">jQuery motto,
      <cite>jquery.com</cite></footer>
  </blockquote>
  <h3 class="h5">Topics covered</h3>
  <ul class="list-inline">
    <li class="list-inline-item badge bg-primary">Grid</li>
    <li class="list-inline-item badge bg-success">Forms</li>
    <li class="list-inline-item badge bg-danger">Tables</li>
  </ul>
  <p class="text-center text-uppercase fw-bold">centre
    uppercase bold</p>
  <p class="text-end fst-italic">right aligned italic</p>
  <p class="text-justify">Press <kbd>Ctrl</kbd> +
    <kbd>S</kbd> to save. Use <code>&lt;h1&gt;</code>
    for the main heading.</p>
</div>
"""),
"""A blog page with a very large heading "Tech Blog", a bigger grey lead line and a horizontal rule.
The post heading has a smaller grey subtitle "a quick guide", then a small grey "Posted on" line where HOD has a dotted underline (hover shows "Head of Department").
The paragraph shows "responsive" highlighted in yellow, bold, italic, struck-through and underlined words. A quotation has a left border and a grey "- jQuery motto, jquery.com" footer. Three coloured topic badges sit in one line, followed by a centred uppercase bold line, a right-aligned italic line and keyboard keys Ctrl and S.""",
"""
<ul><li><b>Headings:</b> &lt;h1&gt;-&lt;h6&gt; or classes <code>.h1</code>-<code>.h6</code>; <code>&lt;small&gt;</code> inside a heading gives a secondary sub-title.</li>
<li><b>Display headings</b> <code>.display-1</code> to <code>.display-6</code> are larger, lighter headings; <b>.lead</b> makes a paragraph stand out.</li>
<li><b>Inline text elements:</b> &lt;mark&gt; highlight, &lt;del&gt;/&lt;s&gt; deleted, &lt;ins&gt;/&lt;u&gt; inserted, &lt;strong&gt; bold, &lt;em&gt; italic, &lt;small&gt;, &lt;abbr&gt; abbreviation, &lt;kbd&gt; keyboard input, &lt;code&gt; inline code.</li>
<li><b>Blockquote:</b> <code>.blockquote</code> with <code>.blockquote-footer</code> for the source.</li>
<li><b>Lists:</b> <code>.list-unstyled</code> (no bullets) and <code>.list-inline</code> with <code>.list-inline-item</code> (items in one line).</li>
<li><b>Text utilities:</b> alignment <code>text-start / text-center / text-end</code> (also responsive, e.g. text-md-center), transform <code>text-uppercase / lowercase / capitalize</code>, weight <code>fw-bold / fw-light</code>, style <code>fst-italic</code>, colours <code>text-primary / text-muted</code>.</li></ul>
"""))

P.append(WE("w2_10", "Bootstrap tables in different styles", page("Tables", """
<div class="container py-3">
  <h1 class="h5">1. .table .table-striped .table-hover</h1>
  <table class="table table-striped table-hover">
    <thead><tr><th>Roll</th><th>Name</th><th>Marks</th>
    </tr></thead>
    <tbody>
      <tr><td>1</td><td>Aman</td><td>78</td></tr>
      <tr><td>2</td><td>Bhumi</td><td>91</td></tr>
      <tr><td>3</td><td>Chirag</td><td>65</td></tr>
    </tbody>
  </table>

  <h2 class="h5">2. Bordered, small, dark header</h2>
  <table class="table table-bordered table-sm">
    <thead class="table-dark">
      <tr><th>Subject</th><th>Code</th></tr></thead>
    <tr><td>DS</td><td>DI03000021</td></tr>
    <tr><td>RWPD</td><td>DI03000061</td></tr>
  </table>

  <h2 class="h5">3. Contextual (coloured) rows</h2>
  <table class="table">
    <tr class="table-success"><td>Pass</td><td>52</td></tr>
    <tr class="table-warning"><td>ATKT</td><td>6</td></tr>
    <tr class="table-danger"><td>Fail</td><td>2</td></tr>
    <tr class="table-info"><td>Absent</td><td>1</td></tr>
  </table>

  <h2 class="h5">4. .table-responsive (scrolls sideways)</h2>
  <div class="table-responsive">
    <table class="table table-bordered text-nowrap">
      <tr><th>Mon</th><th>Tue</th><th>Wed</th><th>Thu</th>
        <th>Fri</th><th>Sat</th></tr>
      <tr><td>DS Lab</td><td>RDBMS Lab</td><td>OS</td>
        <td>CN Lab</td><td>RWPD Lab</td><td>Library</td></tr>
    </table>
  </div>
</div>
"""),
"""1. A marks table with grey stripes on alternate rows; the row under the mouse is highlighted.
2. A small table with borders around every cell and a black header row.
3. Rows coloured green (Pass), yellow (ATKT), red (Fail) and light blue (Absent).
4. A wide timetable that does not squeeze on a phone: it scrolls horizontally inside its own box.""",
"""
<ul><li><b>.table</b> adds basic Bootstrap styling (padding, horizontal lines). It must be added to every table.</li>
<li><b>.table-striped</b> zebra-stripes the rows; <b>.table-striped-columns</b> stripes columns.</li>
<li><b>.table-hover</b> highlights a row when the mouse is over it.</li>
<li><b>.table-bordered</b> adds borders on all sides; <b>.table-borderless</b> removes them; <b>.table-sm</b> halves the cell padding.</li>
<li><b>Colours:</b> <code>.table-dark</code>, <code>.table-primary</code>, <code>.table-success</code>, <code>.table-danger</code>, <code>.table-warning</code>, <code>.table-info</code>, <code>.table-light</code> on a table, row (&lt;tr&gt;) or cell.</li>
<li><b>.table-responsive</b> on a wrapping &lt;div&gt; makes a wide table scroll horizontally on small screens; <code>.table-responsive-md</code> does this only below 768 px.</li>
<li>Bootstrap 3 used <code>.active</code>/<code>.success</code> on rows; Bootstrap 5 uses <code>.table-active</code>/<code>.table-success</code>.</li></ul>
"""))

P.append(WE("w2_11", "Co-curricular activities: images and tables (Practical 6)", page("Activities", """
<div class="container py-3">
  <h1 class="h3 text-center mb-3">Student Activities</h1>
  <div class="row g-3">
    <div class="col-sm-6 col-lg-4">
      <img src="images/sports.jpg" alt="Sports Day"
        width="600" height="400" class="img-fluid rounded">
      <h2 class="h6 mt-2">Sports Day</h2>
      <p class="small">Cricket, kabaddi and athletics.</p>
    </div>
    <div class="col-sm-6 col-lg-4">
      <img src="images/tech.jpg" alt="Tech Fest"
        width="600" height="400" class="img-fluid img-thumbnail">
      <h2 class="h6 mt-2">Tech Fest</h2>
      <p class="small">Project expo and coding contest.</p>
    </div>
    <div class="col-sm-6 col-lg-4">
      <img src="images/nss.jpg" alt="NSS Camp"
        width="600" height="400" class="img-fluid rounded-4">
      <h2 class="h6 mt-2">NSS Camp</h2>
      <p class="small">Village cleanliness drive.</p>
    </div>
    <div class="col-sm-6 col-lg-4 text-center">
      <img src="images/garba.jpg" alt="Garba" width="300"
        height="300" class="img-fluid rounded-circle w-50">
      <h2 class="h6 mt-2">Navratri Garba</h2>
      <p class="small">Cultural night on campus.</p>
    </div>
    <div class="col-sm-6 col-lg-4 text-center">
      <img src="images/blood.jpg" alt="Blood Camp"
        width="300" height="300"
        class="img-fluid rounded-circle w-50">
      <h2 class="h6 mt-2">Blood Donation</h2>
      <p class="small">120 units collected.</p>
    </div>
    <div class="col-sm-6 col-lg-4 text-center">
      <img src="images/trip.jpg" alt="Industrial Visit"
        width="300" height="300"
        class="img-fluid rounded-circle w-50">
      <h2 class="h6 mt-2">Industrial Visit</h2>
      <p class="small">Visit to a software company.</p>
    </div>
  </div>

  <h2 class="h5 mt-4">Participation</h2>
  <div class="table-responsive">
    <table class="table table-striped table-hover
      table-bordered">
      <thead class="table-primary">
        <tr><th>Activity</th><th>Students</th>
          <th>Month</th></tr>
      </thead>
      <tbody>
        <tr><td>Sports Day</td><td>180</td><td>Jan</td></tr>
        <tr class="table-success"><td>Tech Fest</td>
          <td>95</td><td>Feb</td></tr>
        <tr><td>NSS Camp</td><td>60</td><td>Mar</td></tr>
        <tr class="table-warning"><td>Garba</td>
          <td>300</td><td>Oct</td></tr>
      </tbody>
    </table>
  </div>
</div>
"""),
"""A "Student Activities" page with six activities, each with an image (placeholder), a title and a short description.
The first three images are rectangles: rounded, a thumbnail with a border, and extra-rounded. The last three are circles.
One activity per row on a phone, two from 576 px and three from 992 px. Below is a striped, bordered "Participation" table with a light blue header and a highlighted row on hover; the Tech Fest row is green and the Garba row yellow.""",
"""
<ul><li>Responsive layout: <code>col-sm-6 col-lg-4</code> gives 1, 2 or 3 activities per row.</li>
<li>Different image styles: <code>rounded</code>, <code>img-thumbnail</code>, <code>rounded-4</code> and <code>rounded-circle</code>; every image also has <code>img-fluid</code> so it fits its column. <code>w-50</code> makes the circle images half the column width.</li>
<li>The table combines several styles: striped, hover, bordered, a coloured header (<code>table-primary</code>) and coloured rows (<code>table-success</code>, <code>table-warning</code>). It is wrapped in <code>table-responsive</code>.</li>
<li>Replace <code>images/sports.jpg</code> etc. with the real photo files in the project's images folder.</li></ul>
"""))

# ------------------------------------------------------------------ 2.3 Forms and buttons
P.append(WE("w2_12", "Form layouts: vertical, grid, horizontal and inline", page("Form Layouts", """
<div class="container py-3">
  <h1 class="h5">1. Vertical (default)</h1>
  <form class="mb-4">
    <div class="mb-2">
      <label for="em" class="form-label">Email</label>
      <input type="email" class="form-control" id="em"
        placeholder="name@example.com">
      <div class="form-text">We never share your email.</div>
    </div>
    <button class="btn btn-primary">Send</button>
  </form>

  <h2 class="h5">2. Grid layout</h2>
  <form class="row g-2 mb-4">
    <div class="col-md-6">
      <input class="form-control" placeholder="First name">
    </div>
    <div class="col-md-6">
      <input class="form-control" placeholder="Last name">
    </div>
  </form>

  <h2 class="h5">3. Horizontal</h2>
  <form class="mb-4">
    <div class="row mb-2">
      <label class="col-sm-3 col-form-label">City</label>
      <div class="col-sm-9">
        <input class="form-control" value="Surat"></div>
    </div>
    <div class="row">
      <label class="col-sm-3 col-form-label">Pin</label>
      <div class="col-sm-9">
        <input class="form-control" value="395001"></div>
    </div>
  </form>

  <h2 class="h5">4. Inline</h2>
  <form class="row row-cols-sm-auto g-2 align-items-center">
    <div class="col-12">
      <input class="form-control" placeholder="Username">
    </div>
    <div class="col-12">
      <div class="form-check">
        <input class="form-check-input" type="checkbox"
          id="rm">
        <label class="form-check-label" for="rm">
          Remember</label>
      </div>
    </div>
    <div class="col-12">
      <button class="btn btn-success">Login</button></div>
  </form>
</div>
"""),
"""1. A vertical form: the label "Email" above a full-width input with grey help text and a blue Send button.
2. First and last name boxes side by side on a desktop, stacked on a phone.
3. Labels City and Pin on the left of their inputs (from 576 px); on a phone the label is above.
4. Username, a Remember checkbox and a green Login button in one line from 576 px, stacked on a phone.""",
"""
<ul><li><b>Vertical form</b> (default): each field in a <code>.mb-3</code> block with <code>.form-label</code> and <code>.form-control</code>; <code>.form-text</code> gives help text.</li>
<li><b>Grid form:</b> add <code>.row</code> to the form (or a div) and put fields in <code>.col-*</code> columns.</li>
<li><b>Horizontal form:</b> each field group is a <code>.row</code>; the label gets <code>.col-sm-3 .col-form-label</code> (vertically centred) and the input is inside <code>.col-sm-9</code>.</li>
<li><b>Inline form:</b> <code>.row-cols-sm-auto</code> makes each column only as wide as its content, so all fields fit in one line; <code>.align-items-center</code> aligns them vertically.</li>
<li>Bootstrap 3 used <code>.form-group</code>, <code>.form-horizontal</code> and <code>.form-inline</code>; Bootstrap 5 uses grid and spacing classes instead.</li></ul>
"""))

P.append(WE("w2_13", "Form controls: select, check, radio, switch, range, floating labels", page("Form Controls", """
<div class="container py-3">
  <form>
    <div class="form-floating mb-2">
      <input type="text" class="form-control" id="nm"
        placeholder="Name">
      <label for="nm">Floating label: Name</label>
    </div>
    <select class="form-select mb-2">
      <option selected>Choose semester</option>
      <option>Semester 1</option>
      <option>Semester 3</option>
    </select>
    <textarea class="form-control mb-2" rows="2"
      placeholder="Address"></textarea>
    <input class="form-control form-control-lg mb-2"
      placeholder=".form-control-lg">
    <input class="form-control form-control-sm mb-2"
      placeholder=".form-control-sm">
    <input class="form-control mb-2" value="Read only"
      readonly>
    <input class="form-control mb-3" placeholder="Disabled"
      disabled>

    <div class="form-check form-check-inline">
      <input class="form-check-input" type="radio" name="g"
        id="m" checked>
      <label class="form-check-label" for="m">Male</label>
    </div>
    <div class="form-check form-check-inline">
      <input class="form-check-input" type="radio" name="g"
        id="f">
      <label class="form-check-label" for="f">Female</label>
    </div>
    <div class="form-check">
      <input class="form-check-input" type="checkbox"
        id="t" checked>
      <label class="form-check-label" for="t">
        I accept the terms</label>
    </div>
    <div class="form-check form-switch mb-2">
      <input class="form-check-input" type="checkbox"
        id="sw">
      <label class="form-check-label" for="sw">
        Email notifications</label>
    </div>
    <label for="rg" class="form-label">Attendance %</label>
    <input type="range" class="form-range" id="rg"
      min="0" max="100" value="80">
    <div class="input-group mt-2">
      <span class="input-group-text">+91</span>
      <input class="form-control" placeholder="Mobile">
    </div>
  </form>
</div>
"""),
"""A form showing every control type: a Name box whose label sits inside it and floats up when you type, a Bootstrap-styled drop-down list, a two-line Address box, a large and a small input, a read-only box and a greyed-out disabled box.
Below are two inline radio buttons (Male selected), a ticked checkbox, an on/off switch, a slider set to 80 and a mobile number box with a "+91" prefix.""",
"""
<ul><li><b>.form-control</b> styles text inputs and textareas; size with <code>.form-control-lg</code> / <code>.form-control-sm</code>; use the <code>readonly</code> and <code>disabled</code> attributes.</li>
<li><b>.form-select</b> styles &lt;select&gt; drop-downs (Bootstrap 3/4 used .form-control).</li>
<li><b>Checks and radios:</b> wrapper <code>.form-check</code>, input <code>.form-check-input</code>, label <code>.form-check-label</code>; add <code>.form-check-inline</code> for one line. Radios with the same <code>name</code> allow one choice.</li>
<li><b>Switch:</b> <code>.form-check.form-switch</code> on a checkbox.</li>
<li><b>Range:</b> <code>.form-range</code> on <code>type="range"</code>.</li>
<li><b>Floating labels:</b> <code>.form-floating</code> wrapper; the input must come <b>before</b> the label and needs a placeholder.</li>
<li><b>Input group:</b> <code>.input-group</code> with <code>.input-group-text</code> adds text or buttons before/after an input (more in Unit 3).</li></ul>
"""))

P.append(WE("w2_14", "Bootstrap buttons", page("Buttons", """
<div class="container py-3">
  <h1 class="h6">Colour variants</h1>
  <button class="btn btn-primary">Primary</button>
  <button class="btn btn-secondary">Secondary</button>
  <button class="btn btn-success">Success</button>
  <button class="btn btn-danger">Danger</button>
  <button class="btn btn-warning">Warning</button>
  <button class="btn btn-info">Info</button>
  <button class="btn btn-light">Light</button>
  <button class="btn btn-dark">Dark</button>
  <button class="btn btn-link">Link</button>

  <h2 class="h6 mt-3">Outline buttons</h2>
  <button class="btn btn-outline-primary">Primary</button>
  <button class="btn btn-outline-danger">Danger</button>

  <h2 class="h6 mt-3">Sizes</h2>
  <button class="btn btn-primary btn-lg">Large</button>
  <button class="btn btn-primary">Default</button>
  <button class="btn btn-primary btn-sm">Small</button>

  <h2 class="h6 mt-3">States and tags</h2>
  <button class="btn btn-success active">Active</button>
  <button class="btn btn-success" disabled>Disabled</button>
  <a href="#" class="btn btn-dark" role="button">Link</a>
  <input type="submit" class="btn btn-info" value="Input">

  <h2 class="h6 mt-3">Full-width (block) buttons</h2>
  <div class="d-grid gap-2">
    <button class="btn btn-primary">Block button 1</button>
    <button class="btn btn-outline-secondary">
      Block button 2</button>
  </div>
  <div class="d-grid gap-2 col-6 mx-auto mt-2">
    <button class="btn btn-warning">Centred, half width</button>
  </div>
</div>
"""),
"""Coloured buttons: blue, grey, green, red, yellow, light blue, white, black and a plain blue link-style button.
Then outline buttons (coloured border, filling when hovered), a large, normal and small button, a darker "Active" button, a faded "Disabled" button, a link and an input styled as buttons.
At the bottom are two full-width buttons and one yellow half-width button in the centre.""",
"""
<ul><li>Every button needs the base class <b>.btn</b> plus a variant: <code>btn-primary, secondary, success, danger, warning, info, light, dark, link</code>.</li>
<li><b>Outline:</b> <code>.btn-outline-*</code> gives a coloured border and text with no background.</li>
<li><b>Sizes:</b> <code>.btn-lg</code> and <code>.btn-sm</code> (Bootstrap 3 also had btn-xs).</li>
<li><b>States:</b> <code>.active</code> looks pressed; the <code>disabled</code> attribute (for &lt;a&gt;, class <code>.disabled</code>) makes it unclickable.</li>
<li><b>.btn</b> works on &lt;button&gt;, &lt;a&gt; (add <code>role="button"</code>) and &lt;input type="submit/button/reset"&gt;.</li>
<li><b>Block buttons:</b> Bootstrap 4 had <code>.btn-block</code>; Bootstrap 5 uses a wrapper <code>.d-grid gap-2</code>. Add <code>col-6 mx-auto</code> to centre a narrower block button.</li></ul>
"""))

P.append(WE("w2_15", "Student registration form with validation (Practical 8)", page("Registration", """
<div class="container py-3">
  <div class="row">
    <div class="col-lg-8 offset-lg-2">
      <h1 class="h4 text-center mb-3">
        Student Registration</h1>
      <form id="reg" class="row g-3 needs-validation"
        novalidate>
        <div class="col-md-6">
          <label for="fn" class="form-label">Full name</label>
          <input class="form-control" id="fn" required>
          <div class="invalid-feedback">Enter your name.</div>
        </div>
        <div class="col-md-6">
          <label for="en" class="form-label">
            Enrolment no.</label>
          <input class="form-control" id="en" required
            pattern="[0-9]{12}">
          <div class="invalid-feedback">12 digits.</div>
        </div>
        <div class="col-md-6">
          <label for="ml" class="form-label">Email</label>
          <input type="email" class="form-control" id="ml"
            required>
          <div class="invalid-feedback">Valid email.</div>
        </div>
        <div class="col-md-6">
          <label for="br" class="form-label">Branch</label>
          <select class="form-select" id="br" required>
            <option value="">Choose...</option>
            <option>Computer</option><option>IT</option>
            <option>Electrical</option>
          </select>
          <div class="invalid-feedback">Select branch.</div>
        </div>
        <div class="col-12">
          <span class="me-3">Gender:</span>
          <div class="form-check form-check-inline">
            <input class="form-check-input" type="radio"
              name="gd" id="g1" required>
            <label class="form-check-label" for="g1">
              Male</label>
          </div>
          <div class="form-check form-check-inline">
            <input class="form-check-input" type="radio"
              name="gd" id="g2">
            <label class="form-check-label" for="g2">
              Female</label>
          </div>
        </div>
        <div class="col-12">
          <label for="ad" class="form-label">Address</label>
          <textarea class="form-control" id="ad"
            rows="2"></textarea>
        </div>
        <div class="col-12 form-check ms-2">
          <input class="form-check-input" type="checkbox"
            id="ok" required>
          <label class="form-check-label" for="ok">
            Details are correct</label>
          <div class="invalid-feedback">Please confirm.</div>
        </div>
        <div class="col-12 d-flex gap-2">
          <button type="submit" class="btn btn-primary">
            Register</button>
          <button type="reset" class="btn btn-outline-secondary">
            Reset</button>
        </div>
      </form>
      <div id="msg" class="alert alert-success mt-3 d-none">
        Registration successful!</div>
    </div>
  </div>
</div>
""", script="""
var form = document.getElementById("reg");
form.addEventListener("submit", function (e) {
  e.preventDefault();
  var ok = form.checkValidity();
  form.classList.add("was-validated");
  document.getElementById("msg")
    .classList.toggle("d-none", !ok);
});
"""),
"""A centred "Student Registration" form: Full name and Enrolment no. side by side (stacked on a phone), Email and a Branch drop-down, Male/Female radio buttons, an Address box, a confirmation checkbox, and blue Register and grey Reset buttons.
Pressing Register with empty fields turns the required fields red with messages like "Enter your name." and "12 digits."; correct fields turn green. When everything is valid, a green "Registration successful!" box appears.""",
"""
<ul><li><b>Layout:</b> <code>col-lg-8 offset-lg-2</code> centres the form on large screens; inside, <code>form.row.g-3</code> with <code>col-md-6</code> puts two fields per row from 768 px.</li>
<li><b>Controls:</b> form-control, form-select, form-check (inline radios and a checkbox) and buttons of type submit and reset.</li>
<li><b>HTML5 validation:</b> <code>required</code>, <code>type="email"</code> and <code>pattern="[0-9]{12}"</code>. The <code>novalidate</code> attribute stops the browser's own pop-ups so Bootstrap can show its styled messages.</li>
<li>On submit, <code>checkValidity()</code> checks every field and the class <b>.was-validated</b> on the form shows red/green borders and the <b>.invalid-feedback</b> messages (<code>.valid-feedback</code> for success text).</li>
<li><code>classList.toggle("d-none", !ok)</code> shows the success alert only when the form is valid.</li></ul>
""", actions="document.getElementById('fn').value='Riya'; document.querySelector('#reg button[type=submit]').click()"))

# ------------------------------------------------------------------ 2.4 Carets, show / hide
P.append(WE("w2_16", "Carets and show/hide text on different screens", page("Carets and Display", """
<div class="container py-3">
  <h1 class="h5">1. Carets (dropdown arrows)</h1>
  <div class="d-flex flex-wrap gap-2 mb-4">
    <div class="dropdown">
      <button class="btn btn-primary dropdown-toggle"
        data-bs-toggle="dropdown">Down</button>
      <ul class="dropdown-menu">
        <li><a class="dropdown-item" href="#">Item 1</a></li>
        <li><a class="dropdown-item" href="#">Item 2</a></li>
      </ul>
    </div>
    <div class="dropup">
      <button class="btn btn-success dropdown-toggle"
        data-bs-toggle="dropdown">Up</button>
      <ul class="dropdown-menu">
        <li><a class="dropdown-item" href="#">Item</a></li>
      </ul>
    </div>
    <div class="dropend">
      <button class="btn btn-warning dropdown-toggle"
        data-bs-toggle="dropdown">End</button>
      <ul class="dropdown-menu">
        <li><a class="dropdown-item" href="#">Item</a></li>
      </ul>
    </div>
    <div class="dropstart">
      <button class="btn btn-info dropdown-toggle"
        data-bs-toggle="dropdown">Start</button>
      <ul class="dropdown-menu">
        <li><a class="dropdown-item" href="#">Item</a></li>
      </ul>
    </div>
  </div>

  <h2 class="h5">2. Show or hide by screen size</h2>
  <p class="d-block d-md-none alert alert-warning">
    Visible ONLY on mobile (below 768 px)</p>
  <p class="d-none d-md-block alert alert-success">
    Visible ONLY on tablet and desktop</p>
  <p class="d-none d-lg-block alert alert-info">
    Visible only on large screens (992 px +)</p>
  <p>Text <span class="invisible">hidden but takes
    space</span> end.</p>
  <p>Screen reader text:
    <span class="visually-hidden">secret</span> (hidden)</p>
  <button class="btn btn-dark" id="tg">Show / hide note</button>
  <p id="note" class="d-none mt-2">Toggled with d-none.</p>
</div>
""", script="""
document.getElementById("tg").onclick = function () {
  document.getElementById("note")
    .classList.toggle("d-none");
};
""", bs_js=True),
"""1. Four buttons, each with a small triangle (caret): Down (arrow points down, its menu opens below), Up (opens above), End (arrow points right, opens on the right) and Start (arrow points left, opens on the left).
2. On a phone only the yellow "Visible ONLY on mobile" box is shown; on a desktop it is replaced by the green box and, from 992 px, the blue box too. "Text ... end." shows an empty gap where the invisible words are. The black button shows and hides the line "Toggled with d-none." """,
"""
<ul><li><b>Caret:</b> the small triangle that shows a menu can open. In Bootstrap 5 the class <b>.dropdown-toggle</b> draws it automatically; Bootstrap 3 used <code>&lt;span class="caret"&gt;</code>.</li>
<li>Its direction follows the wrapper: <code>.dropdown</code> (down), <code>.dropup</code> (up), <code>.dropend</code> (right), <code>.dropstart</code> (left). <code>data-bs-toggle="dropdown"</code> and bootstrap.bundle.min.js make the menu work.</li>
<li><b>Display utilities</b> <code>.d-{breakpoint}-{value}</code> show or hide elements: <code>d-none</code> hides, <code>d-block / d-inline / d-flex</code> show.</li>
<li>Hide on mobile only: <code>d-none d-md-block</code>. Show on mobile only: <code>d-block d-md-none</code>.</li>
<li><code>.invisible</code> hides the content but keeps its space (visibility: hidden); <code>.visible</code> shows it.</li>
<li><code>.visually-hidden</code> hides content from the screen but keeps it for screen readers (Bootstrap 3: .sr-only).</li>
<li>Bootstrap 3 used <code>.hidden-xs</code>, <code>.visible-md</code> etc.; these were replaced by d-* classes.</li></ul>
""", actions="document.getElementById('tg').click(); bootstrap.Dropdown.getOrCreateInstance(document.querySelector('.dropdown .dropdown-toggle')).show()"))

PROGRAMS = P
