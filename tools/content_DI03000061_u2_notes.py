"""DI03000061 Unit 2 notes: Bootstrap grid, images, typography, tables, forms, buttons, carets, show/hide."""
from web_content import make_TS

SN = {
    "s_grid": """
<div class="container">
  <div class="row">
    <div class="col-sm-4">Column 1</div>
    <div class="col-sm-8">Column 2</div>
  </div>
</div>
""",
    "s_grid_classes": """
<!-- equal width -->
<div class="row">
  <div class="col">1</div>
  <div class="col">2</div>
</div>
<!-- mobile: stacked, tablet: 2, desktop: 4 -->
<div class="row">
  <div class="col-12 col-md-6 col-lg-3">A</div>
  <div class="col-12 col-md-6 col-lg-3">B</div>
  <div class="col-12 col-md-6 col-lg-3">C</div>
  <div class="col-12 col-md-6 col-lg-3">D</div>
</div>
<!-- width from content, rest auto -->
<div class="row">
  <div class="col-auto">Label</div>
  <div class="col">Rest</div>
</div>
<!-- columns per row set on the row -->
<div class="row row-cols-2 row-cols-lg-4 g-3">...</div>
""",
    "s_containers": """
<div class="container">fixed width per breakpoint</div>
<div class="container-fluid">always 100% wide</div>
<div class="container-md">100% until md, then fixed</div>
""",
    "s_offset": """
<div class="row">
  <div class="col-md-4">.col-md-4</div>
  <div class="col-md-4 offset-md-4">
    .col-md-4 .offset-md-4</div>
</div>
<div class="row">
  <div class="col-md-6 offset-md-3">centred</div>
</div>
<div class="row">
  <div class="col-4">left</div>
  <div class="col-4 ms-auto">pushed right</div>
</div>
""",
    "s_order": """
<div class="row">
  <div class="col order-3">First in HTML</div>
  <div class="col order-1">Second in HTML</div>
  <div class="col order-2">Third in HTML</div>
</div>
<!-- different order on phone and desktop -->
<div class="row">
  <main class="col-md-8 order-md-2">Main</main>
  <aside class="col-md-4 order-md-1">Sidebar</aside>
</div>
""",
    "s_nesting": """
<div class="row">
  <div class="col-sm-9">
    Level 1: .col-sm-9
    <div class="row">
      <div class="col-6">Level 2: .col-6</div>
      <div class="col-6">Level 2: .col-6</div>
    </div>
  </div>
  <div class="col-sm-3">Level 1: .col-sm-3</div>
</div>
""",
    "s_gutters": """
<div class="row g-0">no gutter</div>
<div class="row g-4">large gutter</div>
<div class="row gx-5 gy-2">x and y separately</div>
""",
    "s_img": """
<img src="images/campus.jpg" class="img-fluid"
  alt="Campus">
<img src="a.jpg" class="rounded" alt="...">
<img src="b.jpg" class="rounded-circle" alt="...">
<img src="c.jpg" class="img-thumbnail" alt="...">
<img src="d.jpg" class="rounded mx-auto d-block"
  alt="centred">
<img src="e.jpg" class="float-end" alt="right">
""",
    "s_figure": """
<figure class="figure">
  <img src="lab.jpg" class="figure-img img-fluid rounded"
    alt="Lab">
  <figcaption class="figure-caption text-center">
    Computer lab</figcaption>
</figure>
""",
    "s_headings": """
<h1>h1 heading</h1>   <p class="h1">p styled as h1</p>
<h3>Main title
  <small class="text-body-secondary">sub title</small>
</h3>
<h1 class="display-1">Display 1</h1>
<p class="lead">Lead paragraph stands out.</p>
""",
    "s_inline": """
<mark>highlight</mark>  <del>deleted</del>
<s>no longer true</s>   <ins>inserted</ins>
<u>underline</u>        <small>fine print</small>
<strong>bold</strong>   <em>italic</em>
<abbr title="HyperText Markup Language">HTML</abbr>
<kbd>Ctrl</kbd> + <kbd>C</kbd>
""",
    "s_blockquote": """
<blockquote class="blockquote">
  <p>Write less, do more.</p>
</blockquote>
<figcaption class="blockquote-footer">
  jQuery <cite title="Motto">motto</cite>
</figcaption>
""",
    "s_lists": """
<ul class="list-unstyled"> ... </ul>
<ul class="list-inline">
  <li class="list-inline-item">HTML</li>
  <li class="list-inline-item">CSS</li>
</ul>
""",
    "s_text": """
<p class="text-start">left</p>
<p class="text-center">centre</p>
<p class="text-end">right</p>
<p class="text-md-center">centre from md</p>
<p class="text-uppercase">upper</p>
<p class="text-capitalize">each word capital</p>
<p class="fw-bold">bold</p> <p class="fst-italic">italic</p>
<p class="text-primary">blue</p> <p class="text-muted">grey</p>
<p class="text-truncate">very long text ...</p>
""",
    "s_table": """
<table class="table table-striped table-hover">
  <thead class="table-dark">
    <tr><th>Roll</th><th>Name</th></tr>
  </thead>
  <tbody>
    <tr><td>1</td><td>Aman</td></tr>
    <tr class="table-success"><td>2</td><td>Bhumi</td></tr>
  </tbody>
</table>
""",
    "s_table_resp": """
<div class="table-responsive">
  <table class="table table-bordered"> ... </table>
</div>
""",
    "s_form_vertical": """
<form>
  <div class="mb-3">
    <label for="email" class="form-label">Email</label>
    <input type="email" class="form-control" id="email">
    <div class="form-text">Help text</div>
  </div>
  <button type="submit" class="btn btn-primary">Submit</button>
</form>
""",
    "s_form_horizontal": """
<div class="row mb-3">
  <label for="city" class="col-sm-2 col-form-label">City</label>
  <div class="col-sm-10">
    <input type="text" class="form-control" id="city">
  </div>
</div>
""",
    "s_form_inline": """
<form class="row row-cols-lg-auto g-3 align-items-center">
  <div class="col-12">
    <input class="form-control" placeholder="Username">
  </div>
  <div class="col-12">
    <button class="btn btn-primary">Login</button>
  </div>
</form>
""",
    "s_controls": """
<input class="form-control form-control-lg">
<select class="form-select"><option>One</option></select>
<textarea class="form-control" rows="3"></textarea>

<div class="form-check">
  <input class="form-check-input" type="checkbox" id="c1">
  <label class="form-check-label" for="c1">Check</label>
</div>
<div class="form-check form-switch">
  <input class="form-check-input" type="checkbox" id="s1">
  <label class="form-check-label" for="s1">Switch</label>
</div>
<input type="range" class="form-range">

<div class="form-floating">
  <input class="form-control" id="n" placeholder="Name">
  <label for="n">Name</label>
</div>
""",
    "s_validation": """
<form class="needs-validation" novalidate>
  <input class="form-control" required>
  <div class="invalid-feedback">Required.</div>
  <button class="btn btn-primary">Submit</button>
</form>
<script>
  form.addEventListener("submit", function (e) {
    if (!form.checkValidity()) e.preventDefault();
    form.classList.add("was-validated");
  });
</script>
""",
    "s_buttons": """
<button type="button" class="btn btn-primary">Primary</button>
<button class="btn btn-outline-success">Outline</button>
<button class="btn btn-danger btn-lg">Large</button>
<button class="btn btn-secondary btn-sm">Small</button>
<button class="btn btn-primary" disabled>Disabled</button>
<a href="#" class="btn btn-link" role="button">Link</a>
<input type="reset" class="btn btn-warning" value="Reset">

<div class="d-grid gap-2">
  <button class="btn btn-primary">Block button</button>
</div>
""",
    "s_caret": """
<div class="dropdown">
  <button class="btn btn-primary dropdown-toggle"
    data-bs-toggle="dropdown">Menu</button>
  <ul class="dropdown-menu">
    <li><a class="dropdown-item" href="#">One</a></li>
  </ul>
</div>
<!-- .dropup  .dropend  .dropstart change the direction -->
""",
    "s_display": """
<div class="d-none">always hidden</div>
<div class="d-none d-md-block">hidden on phones only</div>
<div class="d-block d-md-none">visible on phones only</div>
<div class="d-none d-lg-block d-xl-none">only on lg</div>
<span class="invisible">hidden, keeps space</span>
<span class="visually-hidden">for screen readers</span>
<div class="d-print-none">not printed</div>
""",
}

T = make_TS(SN)

SEC_2_1 = {
    "title": {"en": "2.1 Bootstrap Grid System"},
    "items": [
        T("Introduction to the Bootstrap Grid", """
<p>The <b>Bootstrap grid system</b> is a <b>mobile-first, flexbox-based</b> layout system that divides the page width into <b>12 equal columns</b>. Using rows and columns, content can be arranged in any layout, and the layout changes automatically at different screen sizes (breakpoints).</p>
<h4>Three main parts</h4>
<ol><li><b>Container</b> (<code>.container</code> or <code>.container-fluid</code>): centres and pads the content. Every grid must be inside a container.</li>
<li><b>Row</b> (<code>.row</code>): a horizontal group of columns. It is a flex container with negative margins that line up columns with the container edge.</li>
<li><b>Column</b> (<code>.col-*</code>): holds the content. The number tells how many of the 12 columns it spans.</li></ol>
@@s_grid@@
<h4>Rules of the grid</h4>
<ul><li>Rows must be placed inside a container; only columns can be direct children of rows.</li>
<li>Content goes inside columns, not directly in rows.</li>
<li>The total of the column numbers in one row should be 12. If it is more than 12, the extra columns wrap onto a new line.</li>
<li>Columns have horizontal padding called the <b>gutter</b>; it can be changed with <code>g-*</code>, <code>gx-*</code>, <code>gy-*</code>.</li>
<li>Column classes apply to their breakpoint <b>and all larger screens</b>.</li></ul>
@@s_gutters@@
""", diagram="web2_grid_anatomy", programs=["w2_2"]),
        T("Grid Classes and Breakpoints", """
<p>A column class has the form <b>.col-{breakpoint}-{number}</b>.</p>
<table><tr><th></th><th>xs<br>&lt;576</th><th>sm<br>&gt;=576</th><th>md<br>&gt;=768</th><th>lg<br>&gt;=992</th><th>xl<br>&gt;=1200</th><th>xxl<br>&gt;=1400</th></tr>
<tr><td>Class prefix</td><td>.col-</td><td>.col-sm-</td><td>.col-md-</td><td>.col-lg-</td><td>.col-xl-</td><td>.col-xxl-</td></tr>
<tr><td>Container width</td><td>100%</td><td>540px</td><td>720px</td><td>960px</td><td>1140px</td><td>1320px</td></tr></table>
<h4>Types of column classes</h4>
<ul><li><b>.col</b>: equal-width columns that share the row automatically.</li>
<li><b>.col-{n}</b>: n of 12 columns on all screen sizes (e.g. <code>.col-6</code> = half).</li>
<li><b>.col-{bp}-{n}</b>: n columns from that breakpoint upward; below it the column is full width (stacked).</li>
<li><b>.col-auto</b>: width according to the content.</li>
<li><b>Mixing classes:</b> <code>col-12 col-md-6 col-lg-3</code> gives 1, 2 or 4 columns per row.</li>
<li><b>.row-cols-{n}</b> on the row sets how many columns appear per row.</li></ul>
@@s_grid_classes@@
<p><b>Example:</b> for a page with 3 boxes in a row on desktop but stacked on mobile, use <code>col-md-4</code> on each box.</p>
""", diagram="web2_grid12"),
        T("Bootstrap Containers", """
<p>A <b>container</b> is the outermost layout element. It holds rows and columns, centres the content and adds padding at the left and right.</p>
<table><tr><th>Container</th><th>Behaviour</th></tr>
<tr><td>.container</td><td>Responsive fixed width: max-width changes at each breakpoint (540, 720, 960, 1140, 1320 px); 100% below 576 px</td></tr>
<tr><td>.container-fluid</td><td>Always 100% of the screen width</td></tr>
<tr><td>.container-{sm|md|lg|xl|xxl}</td><td>100% wide until that breakpoint, then fixed like .container</td></tr></table>
@@s_containers@@
<ul><li>Use <b>.container</b> for normal page content, so lines do not become too long on big screens.</li>
<li>Use <b>.container-fluid</b> for full-width headers, footers, banners and dashboards.</li>
<li>Containers can be nested, but usually this is not required.</li></ul>
""", diagram="web2_containers", programs=["w2_1"]),
        T("Offset Columns", """
<p><b>Offset</b> classes move a column to the right by leaving empty columns on its left. They increase the left margin of the column by a number of grid columns.</p>
<ul><li>Syntax: <code>.offset-{n}</code> or responsive <code>.offset-{bp}-{n}</code> (n = 1 to 11).</li>
<li><code>.col-md-4 .offset-md-4</code>: the column starts after 4 empty columns.</li>
<li><code>.col-md-6 .offset-md-3</code>: centres a half-width column (3 + 6 + 3 = 12).</li>
<li>Reset an offset at a larger breakpoint with <code>.offset-lg-0</code>.</li>
<li><b>Margin utilities</b> can also separate columns: <code>.ms-auto</code> pushes a column to the right, <code>.me-auto</code> to the left.</li></ul>
@@s_offset@@
<p><b>Bootstrap 3:</b> <code>.col-md-offset-4</code>. <b>Bootstrap 4/5:</b> <code>.offset-md-4</code>.</p>
""", diagram="web2_offset_order", programs=["w2_3"]),
        T("Reordering Columns", """
<p><b>Reordering</b> changes the visual order of columns without changing the order in the HTML code. It uses the flexbox <code>order</code> property.</p>
<ul><li><code>.order-0</code> to <code>.order-5</code>: set the order value; smaller values appear first. Columns without an order class have order 0.</li>
<li><code>.order-first</code> (order: -1) and <code>.order-last</code> (order: 6).</li>
<li>Responsive: <code>.order-{bp}-{value}</code>, e.g. <code>.order-md-2</code> works from 768 px.</li></ul>
@@s_order@@
<h4>Why reorder?</h4>
<ul><li>On a phone, the main content should come first, but on a desktop a sidebar on the left looks better.</li>
<li>Search engines and screen readers read the HTML order, so important content can be written first in HTML.</li></ul>
<p><b>Bootstrap 3</b> used <code>.col-md-push-*</code> and <code>.col-md-pull-*</code>; they were replaced by order classes in Bootstrap 4.</p>
""", programs=["w2_4"]),
        T("Nesting Columns", """
<p><b>Nesting</b> means placing a new <code>.row</code> with its own columns inside an existing column. It is used to make complex layouts.</p>
<ul><li>The nested row must be placed <b>inside a column</b>.</li>
<li>The nested row again has <b>12 columns</b>, which divide the width of the parent column (not the whole page).</li>
<li>Nested columns can use any column classes, offsets and order classes.</li>
<li>Nesting can be repeated at any depth.</li></ul>
@@s_nesting@@
<p><b>Example:</b> a <code>col-md-8</code> news area containing two <code>col-sm-6</code> news boxes. Each inner box is half of the news area, i.e. 4 of the 12 page columns.</p>
""", diagram="web2_nesting", programs=["w2_5", "w2_6"]),
        T("Advantages of the Bootstrap Grid", """
<ol><li><b>Responsive:</b> one layout works on all screen sizes; columns stack, resize or rearrange automatically.</li>
<li><b>Mobile first:</b> designed for small screens and enhanced for large screens.</li>
<li><b>Simple to use:</b> only classes are needed; no media queries or float calculations.</li>
<li><b>Flexible 12-column system:</b> 12 can be divided into 1, 2, 3, 4, 6 or 12 equal parts.</li>
<li><b>Six breakpoints</b> (xs to xxl) for fine control.</li>
<li><b>Flexbox based:</b> equal-height columns, vertical alignment (<code>align-items-center</code>), horizontal alignment (<code>justify-content-between</code>) and auto-width columns.</li>
<li><b>Offset, reorder and nesting</b> allow complex layouts.</li>
<li><b>Gutters</b> give consistent spacing that can be changed easily.</li>
<li><b>Consistent and cross-browser:</b> the same layout in all modern browsers; a team uses the same system.</li>
<li><b>Saves development time</b> and keeps the HTML organised.</li></ol>
<p>Practical 5 (class time table) shows how the grid turns a table-like design into a layout that rearranges itself on phones.</p>
""", programs=["w2_7"]),
    ],
}

SEC_2_2 = {
    "title": {"en": "2.2 Responsive Images, Image Shapes, Typography and Tables"},
    "items": [
        T("Responsive Images and Image Shapes", """
<h4>Responsive images</h4>
<p>The class <b>.img-fluid</b> makes an image responsive. It applies <code>max-width: 100%;</code> and <code>height: auto;</code> so the image scales down with its parent element but never becomes larger than its real size. (Bootstrap 3: <code>.img-responsive</code>.)</p>
@@s_img@@
<h4>Image shapes / styles</h4>
<table><tr><th>Class</th><th>Effect</th></tr>
<tr><td>.rounded</td><td>Rounded corners (sizes .rounded-0 to .rounded-5)</td></tr>
<tr><td>.rounded-circle</td><td>Circle (ellipse if the image is not square)</td></tr>
<tr><td>.rounded-pill</td><td>Capsule shape</td></tr>
<tr><td>.img-thumbnail</td><td>1 px border, padding and rounded corners</td></tr>
<tr><td>.rounded-top / -end / -bottom / -start</td><td>Round only one side</td></tr></table>
<h4>Aligning images</h4>
<ul><li><code>.float-start</code> / <code>.float-end</code>: float left or right (text wraps around).</li>
<li><code>.mx-auto .d-block</code>: centre a block image; or <code>.text-center</code> on the parent for an inline image.</li></ul>
<h4>Figures</h4>
@@s_figure@@
<p>Always use the <code>alt</code> attribute to describe the image. The <code>&lt;picture&gt;</code> element with <code>srcset</code> can load different image files for different screen sizes.</p>
""", diagram="web2_img_shapes", programs=["w2_8", "w2_11"]),
        T("Bootstrap Typography", """
<p><b>Typography</b> means the style and appearance of text. Bootstrap sets a default font size of <b>1rem (16 px)</b>, line height 1.5 and a native system font stack, and provides classes for headings, paragraphs, inline text, lists and alignment.</p>
<h4>Headings and display headings</h4>
@@s_headings@@
<ul><li>&lt;h1&gt; to &lt;h6&gt; and the classes <code>.h1</code> to <code>.h6</code> (heading look on any element).</li>
<li><code>.display-1</code> to <code>.display-6</code>: larger, lighter headings for hero sections.</li>
<li><code>&lt;small&gt;</code> inside a heading, with <code>.text-body-secondary</code>, gives a secondary title.</li>
<li><code>.lead</code>: larger paragraph for an introduction.</li></ul>
<h4>Inline text elements</h4>
@@s_inline@@
<h4>Blockquotes</h4>
@@s_blockquote@@
<h4>Lists</h4>
@@s_lists@@
<h4>Text utility classes</h4>
@@s_text@@
<ul><li><b>Alignment:</b> text-start, text-center, text-end (responsive: text-md-start).</li>
<li><b>Transform:</b> text-lowercase, text-uppercase, text-capitalize.</li>
<li><b>Weight and style:</b> fw-bold, fw-semibold, fw-normal, fw-light, fst-italic.</li>
<li><b>Size:</b> fs-1 to fs-6. <b>Wrapping:</b> text-wrap, text-nowrap, text-truncate.</li>
<li><b>Decoration:</b> text-decoration-underline, text-decoration-line-through, text-decoration-none.</li></ul>
""", diagram="web2_typography", programs=["w2_9"]),
        T("Bootstrap Tables", """
<p>Add the base class <b>.table</b> to any &lt;table&gt; to get Bootstrap styling (padding, horizontal dividers, full width). Other classes add more styles.</p>
<table><tr><th>Class</th><th>Effect</th></tr>
<tr><td>.table</td><td>Basic styling (required)</td></tr>
<tr><td>.table-striped</td><td>Zebra stripes on rows</td></tr>
<tr><td>.table-striped-columns</td><td>Stripes on columns</td></tr>
<tr><td>.table-bordered</td><td>Borders on all sides of every cell</td></tr>
<tr><td>.table-borderless</td><td>No borders</td></tr>
<tr><td>.table-hover</td><td>Highlight row on mouse over</td></tr>
<tr><td>.table-sm</td><td>Compact: cell padding halved</td></tr>
<tr><td>.table-dark / .table-light</td><td>Dark or light table or header</td></tr>
<tr><td>.table-active</td><td>Highlight a row or cell</td></tr>
<tr><td>.table-primary, -success, -danger, -warning, -info, -secondary</td><td>Contextual colours on a table, row or cell</td></tr>
<tr><td>.table-responsive</td><td>On a wrapper div: horizontal scroll on small screens</td></tr>
<tr><td>.caption-top</td><td>Show the &lt;caption&gt; above the table</td></tr></table>
@@s_table@@
<h4>Responsive tables</h4>
<p>Wide tables cannot shrink below their content width. Wrapping them in <code>.table-responsive</code> (or <code>.table-responsive-sm/md/lg/xl/xxl</code>) adds horizontal scrolling inside the box instead of breaking the page layout.</p>
@@s_table_resp@@
<p><b>Bootstrap 3:</b> row classes <code>.success</code>, <code>.danger</code>, <code>.active</code>, <code>.table-condensed</code>. <b>Bootstrap 5:</b> <code>.table-success</code>, <code>.table-danger</code>, <code>.table-active</code>, <code>.table-sm</code>.</p>
""", diagram="web2_tables", programs=["w2_10"]),
    ],
}

SEC_2_3 = {
    "title": {"en": "2.3 Form Layout and Buttons"},
    "items": [
        T("Bootstrap Form Layouts", """
<p>Bootstrap styles forms consistently in all browsers and offers several layouts.</p>
<h4>1. Vertical form (default)</h4>
<p>Labels appear above full-width controls. Each group gets a margin class (<code>.mb-3</code>).</p>
@@s_form_vertical@@
<h4>2. Grid form</h4>
<p>Use <code>.row</code> and <code>.col-*</code> to place several fields in one row (e.g. first and last name side by side).</p>
<h4>3. Horizontal form</h4>
<p>Labels and controls are side by side. Each field is a <code>.row</code>; the label gets a column class plus <code>.col-form-label</code> (vertically centred with the input).</p>
@@s_form_horizontal@@
<h4>4. Inline form</h4>
<p>All fields in one line on larger screens, using <code>.row-cols-lg-auto</code> and <code>.align-items-center</code>; they stack on phones.</p>
@@s_form_inline@@
<h4>Important form classes</h4>
<ul><li><b>.form-label</b> for labels; <b>.form-text</b> for help text.</li>
<li><b>.form-control</b> for text inputs and textareas; <b>.form-select</b> for select boxes.</li>
<li><b>.col-form-label</b> in horizontal forms.</li>
<li>Bootstrap 3's <code>.form-group</code>, <code>.form-horizontal</code> and <code>.form-inline</code> were replaced by grid and spacing utilities.</li></ul>
""", diagram="web2_form_layouts", programs=["w2_12"]),
        T("Form Controls and Validation", """
<h4>Form controls</h4>
@@s_controls@@
<ul><li><b>Text inputs</b> (.form-control): sizes <code>.form-control-lg</code>, <code>.form-control-sm</code>; attributes readonly, disabled; <code>.form-control-plaintext</code> for read-only plain text.</li>
<li><b>Select</b> (.form-select): also sizes and <code>multiple</code>.</li>
<li><b>Checkboxes and radios:</b> <code>.form-check</code> wrapper, <code>.form-check-input</code>, <code>.form-check-label</code>; <code>.form-check-inline</code> places them in a row.</li>
<li><b>Switches:</b> add <code>.form-switch</code> to a checkbox's .form-check.</li>
<li><b>Range:</b> <code>.form-range</code>. <b>File input:</b> .form-control with type="file". <b>Colour:</b> .form-control-color.</li>
<li><b>Floating labels:</b> <code>.form-floating</code>; the input comes before the label and needs a placeholder.</li>
<li><b>Input groups:</b> <code>.input-group</code> + <code>.input-group-text</code> for prefixes such as +91 or @.</li></ul>
<h4>Form validation</h4>
<p>Bootstrap uses the browser's HTML5 validation (<code>required</code>, <code>type="email"</code>, <code>pattern</code>, <code>min</code>, <code>maxlength</code>) and shows coloured feedback:</p>
@@s_validation@@
<ul><li><code>novalidate</code> on the form turns off the browser's default pop-up messages.</li>
<li>Adding <b>.was-validated</b> to the form shows red borders and <b>.invalid-feedback</b> text for invalid fields, green borders and <b>.valid-feedback</b> for valid ones.</li>
<li>For server-side validation, add <code>.is-invalid</code> or <code>.is-valid</code> to individual fields.</li></ul>
""", programs=["w2_13", "w2_15"]),
        T("Bootstrap Buttons", """
<p>Buttons are created with the base class <b>.btn</b> plus a <b>variant</b> class. They can be used on &lt;button&gt;, &lt;a&gt; and &lt;input&gt; elements.</p>
@@s_buttons@@
<table><tr><th>Type</th><th>Classes</th></tr>
<tr><td>Colours</td><td>btn-primary, btn-secondary, btn-success, btn-danger, btn-warning, btn-info, btn-light, btn-dark, btn-link</td></tr>
<tr><td>Outline</td><td>btn-outline-primary, btn-outline-danger, ...</td></tr>
<tr><td>Sizes</td><td>btn-lg, btn-sm (Bootstrap 3 also had btn-xs)</td></tr>
<tr><td>Block (full width)</td><td>wrapper .d-grid (BS4: btn-block)</td></tr>
<tr><td>States</td><td>.active, disabled attribute (or .disabled on &lt;a&gt;)</td></tr>
<tr><td>Toggle</td><td>data-bs-toggle="button"</td></tr>
<tr><td>Close button</td><td>.btn-close</td></tr></table>
<ul><li>For an &lt;a&gt; used as a button, add <code>role="button"</code>.</li>
<li>Always set <code>type</code> on &lt;button&gt; (submit, reset or button).</li>
<li>Button groups and toolbars are covered in Unit 3.</li></ul>
""", diagram="web2_buttons", programs=["w2_14"]),
    ],
}

SEC_2_4 = {
    "title": {"en": "2.4 Carets and Show/Hide Text"},
    "items": [
        T("Carets", """
<p>A <b>caret</b> is the small triangle (arrow) shown on a button or link to indicate that it opens a dropdown menu.</p>
<ul><li>In <b>Bootstrap 5</b>, the class <b>.dropdown-toggle</b> adds the caret automatically using a CSS ::after pseudo-element.</li>
<li>In <b>Bootstrap 3</b>, the caret was a separate element: <code>&lt;span class="caret"&gt;&lt;/span&gt;</code>.</li>
<li>The caret direction follows the wrapper class: <code>.dropdown</code> (down), <code>.dropup</code> (up), <code>.dropend</code> (right), <code>.dropstart</code> (left).</li>
<li><code>.dropdown-toggle-split</code> makes a split button with the caret on a separate part.</li></ul>
@@s_caret@@
<p>Dropdowns need <code>bootstrap.bundle.min.js</code> (includes Popper) and the attribute <code>data-bs-toggle="dropdown"</code>. They are studied in detail in Units 3 and 4.</p>
"""),
        T("Hide or Show Text in Bootstrap", """
<p>Bootstrap <b>display utility classes</b> show or hide elements, and they can depend on the screen size.</p>
<p>Format: <b>.d-{value}</b> for all sizes or <b>.d-{breakpoint}-{value}</b> from a breakpoint upward. Values: none, inline, inline-block, block, grid, table, flex, inline-flex.</p>
@@s_display@@
<table><tr><th>Requirement</th><th>Classes</th></tr>
<tr><td>Hidden on all screens</td><td>.d-none</td></tr>
<tr><td>Hidden only on xs (phones)</td><td>.d-none .d-sm-block</td></tr>
<tr><td>Hidden only on md</td><td>.d-md-none .d-lg-block</td></tr>
<tr><td>Visible only on xs</td><td>.d-block .d-sm-none</td></tr>
<tr><td>Visible only on lg</td><td>.d-none .d-lg-block .d-xl-none</td></tr>
<tr><td>Hidden when printing</td><td>.d-print-none</td></tr></table>
<h4>Other ways to hide</h4>
<ul><li><b>.invisible:</b> hides the element but it still takes up space (visibility: hidden). <b>.visible</b> shows it again.</li>
<li><b>.visually-hidden:</b> hides it from the screen but screen readers still read it (Bootstrap 3/4: .sr-only).</li>
<li><b>JavaScript:</b> toggle the d-none class, e.g. <code>element.classList.toggle("d-none")</code>, or use the collapse plug-in (Unit 4).</li></ul>
<p><b>Bootstrap 3</b> used <code>.hidden-xs</code>, <code>.hidden-sm</code>, <code>.visible-md-block</code> etc. Bootstrap 4/5 replaced them with d-* classes.</p>
""", diagram="web2_display", programs=["w2_16"]),
    ],
}

NOTES = [SEC_2_1, SEC_2_2, SEC_2_3, SEC_2_4]
