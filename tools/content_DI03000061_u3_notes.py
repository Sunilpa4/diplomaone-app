"""DI03000061 Unit 3 notes: Bootstrap components."""
from web_content import make_TS

SN = {
    "s_icons": """
<!-- in <head> -->
<link rel="stylesheet" href="bootstrap-icons.css">

<i class="bi bi-house"></i> Home
<i class="bi bi-search text-primary fs-4"></i>
<button class="btn btn-success">
  <i class="bi bi-download"></i> Download
</button>
<i class="bi bi-star-fill" style="color: orange"></i>
""",
    "s_glyph": """
<!-- Bootstrap 3 -->
<span class="glyphicon glyphicon-user"></span>
<!-- Bootstrap 5 -->
<i class="bi bi-person"></i>
""",
    "s_dropdown": """
<div class="dropdown">
  <button class="btn btn-primary dropdown-toggle"
      type="button" data-bs-toggle="dropdown">
    Courses
  </button>
  <ul class="dropdown-menu">
    <li><h6 class="dropdown-header">Diploma</h6></li>
    <li><a class="dropdown-item" href="#">Computer</a></li>
    <li><a class="dropdown-item active" href="#">IT</a></li>
    <li><hr class="dropdown-divider"></li>
    <li><a class="dropdown-item disabled">M.E.</a></li>
  </ul>
</div>
""",
    "s_split": """
<div class="btn-group">
  <button class="btn btn-danger">Action</button>
  <button class="btn btn-danger dropdown-toggle
      dropdown-toggle-split" data-bs-toggle="dropdown">
  </button>
  <ul class="dropdown-menu dropdown-menu-end">...</ul>
</div>
<div class="btn-group dropup">...</div>
""",
    "s_card": """
<div class="card" style="width: 18rem">
  <img src="course.jpg" class="card-img-top" alt="Course">
  <div class="card-body">
    <h5 class="card-title">Python Course</h5>
    <p class="card-text">Learn Python in 30 days.</p>
    <a href="#" class="btn btn-primary">Enroll</a>
  </div>
  <div class="card-footer text-muted">Starts 1 Dec</div>
</div>
""",
    "s_card_grid": """
<div class="row row-cols-1 row-cols-md-3 g-3">
  <div class="col">
    <div class="card h-100">...</div>
  </div>
  <div class="col">
    <div class="card h-100 text-bg-success">...</div>
  </div>
</div>
""",
    "s_btn_group": """
<div class="btn-group" role="group">
  <button class="btn btn-primary">Left</button>
  <button class="btn btn-primary">Middle</button>
  <button class="btn btn-primary">Right</button>
</div>
<div class="btn-group-vertical">...</div>
""",
    "s_toolbar": """
<div class="btn-toolbar" role="toolbar">
  <div class="btn-group me-2">
    <button class="btn btn-secondary">1</button>
    <button class="btn btn-secondary">2</button>
  </div>
  <div class="btn-group">
    <button class="btn btn-info">8</button>
  </div>
</div>
""",
    "s_nested": """
<div class="btn-group">
  <button class="btn btn-primary">Sem 1</button>
  <div class="btn-group">
    <button class="btn btn-primary dropdown-toggle"
        data-bs-toggle="dropdown">Sem 3</button>
    <ul class="dropdown-menu">
      <li><a class="dropdown-item" href="#">RWPD</a></li>
    </ul>
  </div>
</div>
""",
    "s_input_group": """
<div class="input-group mb-3">
  <span class="input-group-text">@</span>
  <input type="text" class="form-control"
      placeholder="Username">
</div>
<div class="input-group mb-3">
  <span class="input-group-text">Rs.</span>
  <input type="number" class="form-control">
  <span class="input-group-text">.00</span>
</div>
<div class="input-group">
  <input type="text" class="form-control"
      placeholder="Search">
  <button class="btn btn-primary">Go</button>
</div>
""",
    "s_navs": """
<ul class="nav nav-tabs">
  <li class="nav-item">
    <a class="nav-link active" href="#">Unit 1</a>
  </li>
  <li class="nav-item">
    <a class="nav-link" href="#">Unit 2</a>
  </li>
  <li class="nav-item">
    <a class="nav-link disabled">Unit 3</a>
  </li>
</ul>
<!-- pills: nav nav-pills, vertical: add flex-column -->
""",
    "s_tab_plugin": """
<ul class="nav nav-tabs" role="tablist">
  <li class="nav-item">
    <button class="nav-link active" data-bs-toggle="tab"
        data-bs-target="#u1" type="button">Unit 1</button>
  </li>
  <li class="nav-item">
    <button class="nav-link" data-bs-toggle="tab"
        data-bs-target="#u2" type="button">Unit 2</button>
  </li>
</ul>
<div class="tab-content p-3 border border-top-0">
  <div class="tab-pane fade show active" id="u1">
    Introduction...</div>
  <div class="tab-pane fade" id="u2">Grid...</div>
</div>
""",
    "s_navbar": """
<nav class="navbar navbar-expand-lg bg-dark"
    data-bs-theme="dark">
  <div class="container-fluid">
    <a class="navbar-brand" href="#">DiplomaOne</a>
    <button class="navbar-toggler" type="button"
        data-bs-toggle="collapse" data-bs-target="#menu">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="menu">
      <ul class="navbar-nav me-auto">
        <li class="nav-item">
          <a class="nav-link active" href="#">Home</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="#">About</a>
        </li>
      </ul>
      <form class="d-flex">
        <input class="form-control me-2" type="search">
        <button class="btn btn-warning">Search</button>
      </form>
    </div>
  </div>
</nav>
""",
    "s_fixed": """
<nav class="navbar fixed-top bg-primary">...</nav>
<footer class="fixed-bottom bg-dark text-white">
  ...</footer>
<style>
  body { padding-top: 60px; padding-bottom: 50px; }
</style>
""",
    "s_breadcrumb": """
<nav aria-label="breadcrumb">
  <ol class="breadcrumb">
    <li class="breadcrumb-item"><a href="#">Home</a></li>
    <li class="breadcrumb-item"><a href="#">Sem 3</a></li>
    <li class="breadcrumb-item active">RWPD</li>
  </ol>
</nav>
""",
    "s_pagination": """
<ul class="pagination justify-content-center">
  <li class="page-item disabled">
    <a class="page-link">Previous</a>
  </li>
  <li class="page-item"><a class="page-link" href="#">1</a></li>
  <li class="page-item active">
    <a class="page-link" href="#">2</a>
  </li>
  <li class="page-item"><a class="page-link" href="#">3</a></li>
  <li class="page-item"><a class="page-link" href="#">Next</a></li>
</ul>
""",
    "s_badge": """
<h4>Notices <span class="badge bg-danger">New</span></h4>
<span class="badge rounded-pill text-bg-warning">Pill</span>
<button class="btn btn-primary">
  Inbox <span class="badge text-bg-light">7</span>
</button>
<button class="btn btn-dark position-relative">
  <i class="bi bi-bell"></i>
  <span class="position-absolute top-0 start-100
      translate-middle badge rounded-pill bg-danger">3</span>
</button>
""",
    "s_jumbotron": """
<div class="p-5 mb-4 bg-body-tertiary rounded-3">
  <h1 class="display-5 fw-bold">Learn Web Design</h1>
  <p class="lead">Free notes for GTU diploma students.</p>
  <a class="btn btn-primary btn-lg" href="#">Get started</a>
</div>
""",
    "s_page_header": """
<div class="border-bottom pb-2 mb-3">
  <h1>Exam Results
    <small class="text-body-secondary">Summer 2026</small>
  </h1>
</div>
""",
    "s_thumbnail": """
<!-- simple bordered image -->
<img src="lab.jpg" class="img-thumbnail" alt="Lab">
<!-- BS3 .thumbnail with caption = BS5 card -->
<div class="col-md-4">
  <div class="card">
    <img src="lab.jpg" class="card-img-top" alt="Lab">
    <div class="card-body">
      <h5>Computer Lab</h5>
      <a href="#" class="btn btn-primary">View</a>
    </div>
  </div>
</div>
""",
    "s_alert": """
<div class="alert alert-success" role="alert">
  <strong>Saved!</strong> Your form was submitted.
</div>
<div class="alert alert-warning alert-dismissible fade show">
  Last date for fees is 30 Nov.
  <button type="button" class="btn-close"
      data-bs-dismiss="alert"></button>
</div>
""",
    "s_alert_js": """
var box = document.getElementById("fee");
box.addEventListener("closed.bs.alert", function () {
  msg.textContent = "Alert closed";
});
// close from code
bootstrap.Alert.getOrCreateInstance(box).close();
""",
    "s_progress": """
<div class="progress" style="height: 20px">
  <div class="progress-bar bg-success" style="width: 75%">
    75%</div>
</div>
<div class="progress">
  <div class="progress-bar progress-bar-striped
      progress-bar-animated bg-danger" style="width: 85%">
  </div>
</div>
""",
    "s_progress_js": """
var v = 0;
var t = setInterval(function () {
  v = v + 10;
  bar.style.width = v + "%";
  bar.textContent = v + "%";
  if (v >= 100) clearInterval(t);
}, 500);
""",
    "s_media": """
<div class="d-flex">
  <div class="flex-shrink-0">
    <img src="grandpa.jpg" width="64" alt="">
  </div>
  <div class="flex-grow-1 ms-3">
    <h5>Grandfather</h5>
    Retired teacher.
    <div class="d-flex mt-3">  <!-- nested -->
      <img src="father.jpg" width="48" alt="">
      <div class="ms-3"><h6>Father</h6>Engineer.</div>
    </div>
  </div>
</div>
""",
    "s_list_group": """
<ul class="list-group">
  <li class="list-group-item active">JioFiber</li>
  <li class="list-group-item d-flex
      justify-content-between">Airtel
    <span class="badge bg-primary rounded-pill">4.3</span>
  </li>
  <li class="list-group-item disabled">BSNL</li>
  <li class="list-group-item list-group-item-success">
    DGVCL</li>
</ul>
<div class="list-group">
  <a href="#" class="list-group-item
      list-group-item-action">Clickable item</a>
</div>
""",
    "s_panel": """
<!-- BS3 panel -->
<div class="panel panel-primary">
  <div class="panel-heading">Internet</div>
  <div class="panel-body">...</div>
</div>
<!-- BS5 equivalent -->
<div class="card border-primary">
  <div class="card-header text-bg-primary">Internet</div>
  <div class="card-body">...</div>
</div>
""",
}

T = make_TS(SN)

SEC_3_1 = {
    "title": {"en": "3.1 Components, Icons, Dropdowns, Cards, Button and Input Groups"},
    "items": [
        T("Introduction to Bootstrap Components", """
<p>A <b>Bootstrap component</b> is a ready-made, reusable user interface (UI) part, such as a navbar, card, dropdown, alert or progress bar. It is made of HTML with predefined Bootstrap classes. Interactive components also use Bootstrap's JavaScript (<code>bootstrap.bundle.min.js</code>).</p>
<h4>Advantages of components</h4>
<ul><li><b>Saves time:</b> no need to write CSS or JavaScript from scratch; just add classes.</li>
<li><b>Consistent look:</b> all pages and buttons look the same across the website.</li>
<li><b>Responsive:</b> components adjust automatically to phone, tablet and desktop.</li>
<li><b>Cross-browser:</b> tested on all modern browsers.</li>
<li><b>Accessible:</b> they use ARIA attributes and keyboard support for screen readers.</li>
<li><b>Easy to customise:</b> colours, sizes and spacing are changed with utility classes or Sass variables.</li>
<li><b>Well documented</b> with many examples, and a large community.</li></ul>
<h4>Types of components</h4>
<table><tr><th>Type</th><th>Components</th></tr>
<tr><td>Navigation</td><td>Navs (tabs, pills), navbar, breadcrumb, pagination, dropdown</td></tr>
<tr><td>Content containers</td><td>Card (panel, thumbnail, well), list group, media object, jumbotron, accordion</td></tr>
<tr><td>Buttons and forms</td><td>Buttons, button group, button toolbar, input group, close button</td></tr>
<tr><td>Feedback / status</td><td>Alerts, badges (labels), progress bars, spinners, toasts</td></tr>
<tr><td>Overlays (Unit 4)</td><td>Modal, tooltip, popover, offcanvas</td></tr></table>
<p><b>CSS-only components</b> (card, badge, breadcrumb, list group) need only bootstrap.css. <b>JavaScript components</b> (dropdown, navbar toggler, tabs, dismissible alert) also need bootstrap.bundle.min.js and work through <code>data-bs-*</code> attributes.</p>
""", diagram="web3_components"),
        T("Bootstrap 3 Components and their Bootstrap 5 Replacements", """
<p>The GTU syllabus uses some <b>Bootstrap 3</b> component names. Bootstrap 4 and 5 removed or renamed many of them. In this course we use <b>Bootstrap 5</b>, but you should know both names for the viva.</p>
<table><tr><th>Bootstrap 3</th><th>Bootstrap 5</th></tr>
<tr><td>Glyphicons (icon font in bootstrap.css)</td><td>Bootstrap Icons, a separate library: <code>bi bi-*</code></td></tr>
<tr><td>.label .label-danger</td><td>.badge .bg-danger</td></tr>
<tr><td>.panel, .panel-heading, .panel-body</td><td>.card, .card-header, .card-body</td></tr>
<tr><td>.thumbnail</td><td>.card or .img-thumbnail</td></tr>
<tr><td>.well</td><td>.card or .bg-light .p-3 .border</td></tr>
<tr><td>.jumbotron</td><td>Removed; use utilities .p-5 .bg-body-tertiary .rounded-3</td></tr>
<tr><td>.page-header</td><td>Removed; use .border-bottom .pb-2 .mb-3</td></tr>
<tr><td>.media (BS3/BS4)</td><td>Flex utilities: .d-flex .flex-shrink-0 .ms-3</td></tr>
<tr><td>.navbar-default / .navbar-inverse</td><td>.bg-* with data-bs-theme="light" / "dark"</td></tr>
<tr><td>.pull-left / .pull-right</td><td>.float-start / .float-end, or .ms-auto in flex</td></tr>
<tr><td>&lt;span class="caret"&gt;</td><td>Added automatically by .dropdown-toggle</td></tr>
<tr><td>data-toggle, data-target</td><td>data-bs-toggle, data-bs-target</td></tr>
<tr><td>.input-group-addon</td><td>.input-group-text</td></tr></table>
<p><b>Reason for the changes:</b> Bootstrap 4/5 moved to flexbox, removed jQuery, and made smaller general utility classes, so many single-purpose components were no longer needed.</p>
""", diagram="web3_bs3_map"),
        T("Glyphicons and Bootstrap Icons", """
<p><b>Glyphicons</b> were the icon font included in <b>Bootstrap 3</b> (about 250 icons). Icons were added with a span: <code>&lt;span class="glyphicon glyphicon-search"&gt;&lt;/span&gt;</code>. Bootstrap 4 dropped Glyphicons.</p>
<p><b>Bootstrap Icons</b> is the official free icon library for Bootstrap 5, with more than 2000 icons. It is a separate CSS + font file.</p>
@@s_glyph@@
<h4>Using Bootstrap Icons</h4>
<ol><li>Link <b>bootstrap-icons.css</b> in the head (from a CDN or a local copy).</li>
<li>Add <code>&lt;i class="bi bi-{name}"&gt;&lt;/i&gt;</code> where the icon should appear.</li>
<li>Because an icon is a font character, change its <b>size</b> with font-size (<code>fs-1</code> to <code>fs-6</code>) and its <b>colour</b> with text colour classes (<code>text-danger</code>).</li></ol>
@@s_icons@@
<h4>Common icons</h4>
<ul><li>bi-house, bi-person, bi-envelope, bi-telephone, bi-search</li>
<li>bi-cart, bi-heart, bi-star-fill, bi-trash, bi-pencil, bi-download</li>
<li>bi-list (menu), bi-x-lg (close), bi-check-circle, bi-exclamation-triangle</li></ul>
<p>Icons are used in buttons, navbars, menus, alerts and list items. For accessibility, add <code>aria-hidden="true"</code> to decorative icons, or a visually-hidden text label for icon-only buttons.</p>
""", programs=["w3_1"]),
        T("Dropdowns", """
<p>A <b>dropdown</b> is a toggleable menu that shows a list of links when a button or link is clicked. It is a JavaScript component and needs <b>bootstrap.bundle.min.js</b> (which includes Popper.js for positioning).</p>
<h4>Structure</h4>
<ul><li>Wrapper <code>.dropdown</code> (or <code>.btn-group</code>).</li>
<li>Toggle button with <code>.dropdown-toggle</code> and <code>data-bs-toggle="dropdown"</code>; the caret is added automatically.</li>
<li>Menu <code>ul.dropdown-menu</code> with <code>a.dropdown-item</code> items.</li></ul>
@@s_dropdown@@
<h4>Menu options</h4>
<table><tr><th>Class</th><th>Use</th></tr>
<tr><td>.dropdown-header</td><td>Non-clickable heading inside the menu</td></tr>
<tr><td>.dropdown-divider</td><td>Horizontal line between groups (BS3: li.divider)</td></tr>
<tr><td>.active / .disabled</td><td>Highlighted current item / greyed-out item</td></tr>
<tr><td>.dropdown-item-text</td><td>Plain text item</td></tr>
<tr><td>.dropdown-menu-end</td><td>Menu aligned to the right edge</td></tr>
<tr><td>.dropdown-menu-dark</td><td>Dark menu</td></tr>
<tr><td>.dropup / .dropend / .dropstart</td><td>Menu opens upward / right / left</td></tr>
<tr><td>.dropdown-toggle-split</td><td>Split button: action part + caret part</td></tr></table>
@@s_split@@
<p><b>Events:</b> show.bs.dropdown, shown.bs.dropdown, hide.bs.dropdown, hidden.bs.dropdown. Forms can also be placed inside a dropdown menu.</p>
""", diagram="web3_dropdown", programs=["w3_2"]),
        T("Cards", """
<p>A <b>card</b> is a flexible content container with optional header, footer, image and body. In Bootstrap 4/5, the card replaced the BS3 <b>panel, well and thumbnail</b>.</p>
<h4>Parts of a card</h4>
<ul><li><b>.card</b>: outer box with border and rounded corners.</li>
<li><b>.card-header / .card-footer</b>: grey strips at the top and bottom.</li>
<li><b>.card-body</b>: padded content area containing <b>.card-title</b>, <b>.card-subtitle</b>, <b>.card-text</b> and <b>.card-link</b>.</li>
<li><b>.card-img-top / .card-img-bottom</b>: full-width image at the top or bottom.</li>
<li><b>.card-img-overlay</b>: places text on top of the image.</li></ul>
@@s_card@@
<h4>Card layouts and styles</h4>
<ul><li><b>Grid of cards:</b> cards inside grid columns; <code>.h-100</code> gives equal height.</li>
<li><b>.card-group:</b> joined cards of equal height.</li>
<li><b>Horizontal card:</b> a row inside the card with image in col-md-4 and body in col-md-8.</li>
<li><b>Colours:</b> <code>text-bg-primary</code>, <code>border-success</code>.</li>
<li><b>List group in card:</b> <code>ul.list-group.list-group-flush</code>.</li>
<li><b>Width:</b> 100% by default; set it with the grid, w-* utilities or a style.</li></ul>
@@s_card_grid@@
""", diagram="web3_card", programs=["w3_3"]),
        T("Button Groups and Button Toolbar", """
<p>A <b>button group</b> joins several buttons together in a single line (no gap, only the outer corners rounded). A <b>button toolbar</b> combines several button groups in one row.</p>
<h4>Button group</h4>
@@s_btn_group@@
<ul><li><b>.btn-group</b>: horizontal group. Add <code>role="group"</code> and an aria-label for accessibility.</li>
<li><b>.btn-group-vertical</b>: buttons stacked vertically.</li>
<li><b>Sizes:</b> <code>.btn-group-lg</code>, <code>.btn-group-sm</code> on the group instead of on every button.</li>
<li><b>Toggle group:</b> radio or checkbox inputs with <code>.btn-check</code> and labels with <code>.btn</code>, so one or more buttons stay selected.</li></ul>
<h4>Button toolbar</h4>
@@s_toolbar@@
<p>Use spacing utilities (<code>me-2</code>) between the groups. Input groups can also be placed in a toolbar.</p>
<h4>Nesting (dropdown inside a group)</h4>
<p>Place a <code>.btn-group</code> containing a dropdown inside another <code>.btn-group</code>. This creates a group where one button opens a submenu, e.g. odd and even semester buttons with subject menus.</p>
@@s_nested@@
<p><b>Uses:</b> pagination-like controls, text editor toolbars (bold, italic, underline), view switchers (list/grid), semester selectors.</p>
""", diagram="web3_btn_groups", programs=["w3_4", "w3_5"]),
        T("Input Groups", """
<p>An <b>input group</b> extends a form control by adding text, icons or buttons <b>before, after or on both sides</b> of the input in one joined box.</p>
@@s_input_group@@
<h4>Classes and options</h4>
<ul><li><b>.input-group</b>: wrapper; its children are joined together.</li>
<li><b>.input-group-text</b>: grey add-on with text or an icon (BS3: <code>.input-group-addon</code>).</li>
<li><b>Buttons and dropdowns</b> can be added directly as add-ons.</li>
<li><b>Checkbox or radio</b> inside <code>.input-group-text</code> with <code>.form-check-input</code>.</li>
<li><b>Multiple inputs</b> (e.g. first and last name) and multiple add-ons are allowed.</li>
<li><b>Select and file input:</b> <code>.form-select</code>, <code>input type="file"</code>.</li>
<li><b>Sizes:</b> <code>.input-group-sm</code>, <code>.input-group-lg</code>.</li>
<li><b>.flex-nowrap</b> stops the parts wrapping onto a new line on small screens.</li></ul>
<p><b>Examples:</b> @ for username, +91 for mobile, Rs. and .00 for an amount, envelope icon for email, Search + Go button, "https://" before a website field.</p>
<p>Always connect a <b>label</b> (or aria-label) with the input because the add-on text is not a label.</p>
""", diagram="web3_input_group", programs=["w3_6"]),
    ],
}

SEC_3_2 = {
    "title": {"en": "3.2 Navs, Navbar, Breadcrumb, Pagination and Badges"},
    "items": [
        T("Navs: Tabs and Pills", """
<p><b>Navs</b> are navigation components built from a list of links. The base class <code>.nav</code> with <code>.nav-item</code> and <code>.nav-link</code> gives a simple horizontal menu.</p>
@@s_navs@@
<h4>Nav styles</h4>
<table><tr><th>Class</th><th>Result</th></tr>
<tr><td>.nav-tabs</td><td>Tabs: the active link looks like a folder tab joined to the content below</td></tr>
<tr><td>.nav-pills</td><td>Pills: the active link has a coloured rounded background</td></tr>
<tr><td>.nav-underline</td><td>Active link underlined</td></tr>
<tr><td>.nav-fill / .nav-justified</td><td>Items fill the full width (justified = equal widths)</td></tr>
<tr><td>.flex-column</td><td>Vertical (stacked) nav</td></tr>
<tr><td>.justify-content-center / -end</td><td>Centre or right-align the items</td></tr>
<tr><td>.active / .disabled</td><td>Current item / disabled item</td></tr></table>
<h4>Tab and pill plug-in (dynamic tabs)</h4>
<p>With JavaScript, tabs and pills switch between content panes without loading a new page.</p>
<ul><li>Each link gets <code>data-bs-toggle="tab"</code> (or "pill") and <code>data-bs-target="#id"</code>.</li>
<li>Panes are <code>.tab-pane</code> inside <code>.tab-content</code>; the first pane has <code>show active</code>.</li>
<li><code>.fade</code> gives a fade animation.</li></ul>
@@s_tab_plugin@@
<p>Events: show.bs.tab, shown.bs.tab, hide.bs.tab. From code: <code>bootstrap.Tab.getOrCreateInstance(el).show()</code>.</p>
""", diagram="web3_navs", programs=["w3_7", "w3_8"]),
        T("Navbar", """
<p>A <b>navbar</b> is the responsive navigation header of a website. It contains the brand (logo/name), navigation links, dropdowns, forms and buttons. On small screens it collapses behind a <b>hamburger</b> (toggler) button.</p>
@@s_navbar@@
<h4>Parts of a navbar</h4>
<ul><li><b>.navbar</b> with <b>.navbar-expand-{bp}</b>: the menu is expanded from that breakpoint upward and collapsed below it (e.g. lg = collapsed below 992 px).</li>
<li><b>.navbar-brand</b>: website name or logo image.</li>
<li><b>.navbar-toggler</b> with <b>.navbar-toggler-icon</b>: the hamburger button; <code>data-bs-toggle="collapse"</code> opens the menu.</li>
<li><b>.collapse.navbar-collapse</b>: the part that is hidden on small screens; its id matches data-bs-target.</li>
<li><b>.navbar-nav</b> with .nav-item / .nav-link: the links; .dropdown items are allowed.</li>
<li><b>.navbar-text</b>: plain text.</li>
<li><b>Forms:</b> <code>form.d-flex</code> for a search box; <code>me-auto</code> on navbar-nav pushes the form to the right.</li></ul>
<h4>Colour schemes</h4>
<p>Use a background class (<code>bg-dark</code>, <code>bg-primary</code>, <code>bg-body-tertiary</code>) and <code>data-bs-theme="dark"</code> for light text. (BS3: .navbar-default and .navbar-inverse.)</p>
<h4>Fixed navbar</h4>
<table><tr><th>Class</th><th>Behaviour</th></tr>
<tr><td>.fixed-top</td><td>Stays at the top of the screen while scrolling</td></tr>
<tr><td>.fixed-bottom</td><td>Stays at the bottom (used for footers)</td></tr>
<tr><td>.sticky-top</td><td>Scrolls with the page, then sticks at the top</td></tr></table>
<p>Fixed elements are removed from the normal flow, so add <b>padding-top</b> (and padding-bottom) to the body so that content is not hidden behind them.</p>
@@s_fixed@@
""", diagram="web3_navbar", programs=["w3_9", "w3_10"]),
        T("Breadcrumb and Pagination", """
<h4>Breadcrumb</h4>
<p>A <b>breadcrumb</b> shows the current page's location in the website hierarchy, e.g. Home / Computer / Sem 3 / RWPD. Each level is a link except the current page.</p>
@@s_breadcrumb@@
<ul><li><code>ol.breadcrumb</code> with <code>li.breadcrumb-item</code>; the last item has <code>.active</code> and <code>aria-current="page"</code>.</li>
<li>The separator "/" is added by CSS. Change it with the CSS variable <code>--bs-breadcrumb-divider</code>, e.g. '&gt;'.</li>
<li>Wrap it in <code>nav aria-label="breadcrumb"</code> for accessibility.</li></ul>
<h4>Pagination</h4>
<p><b>Pagination</b> splits long content (search results, products, articles) into pages and shows numbered page links.</p>
@@s_pagination@@
<ul><li>Structure: <code>ul.pagination &gt; li.page-item &gt; a.page-link</code>.</li>
<li><code>.active</code> marks the current page; <code>.disabled</code> greys out Previous on the first page or Next on the last page.</li>
<li>Sizes: <code>.pagination-lg</code>, <code>.pagination-sm</code>.</li>
<li>Alignment: <code>justify-content-center</code> or <code>-end</code> on the ul.</li>
<li>Arrows: use <code>&amp;laquo;</code> and <code>&amp;raquo;</code> (shown as double arrows) for Previous / Next.</li></ul>
<p><b>With JavaScript:</b> keep a list of items and show only the items of the current page: <code>items.slice((page - 1) * perPage, page * perPage)</code>. Rebuild the page links on every click.</p>
""", diagram="web3_breadcrumb", programs=["w3_11"]),
        T("Badges (Labels)", """
<p>A <b>badge</b> is a small count or label that is attached to text, buttons or links, e.g. "New", the number of unread messages, or a status. In <b>Bootstrap 3</b> these were called <b>labels</b> (<code>.label .label-success</code>) and <b>badges</b> (rounded counters); Bootstrap 5 joins both in <b>.badge</b>.</p>
@@s_badge@@
<ul><li><b>Colour:</b> <code>bg-*</code> or <code>text-bg-*</code> (text-bg also sets a readable text colour).</li>
<li><b>.rounded-pill</b>: pill-shaped badge.</li>
<li><b>Size:</b> a badge scales with its parent, so a badge in an h1 is larger than one in a paragraph.</li>
<li><b>In buttons:</b> shows counts like Inbox 7.</li>
<li><b>Positioned:</b> <code>position-absolute top-0 start-100 translate-middle</code> puts a notification count on the corner of an icon button.</li>
<li>Add visually-hidden text (e.g. "unread messages") so screen readers understand the number.</li></ul>
<p><b>Uses:</b> new items, notification counts, status (Paid / Pending), tags and categories, ratings in list groups.</p>
""", programs=["w3_12"]),
    ],
}

SEC_3_3 = {
    "title": {"en": "3.3 Jumbotron, Thumbnails, Alerts, Progress, Media, List Group and Panels"},
    "items": [
        T("Jumbotron and Page Header", """
<h4>Jumbotron</h4>
<p>A <b>jumbotron</b> is a large, padded box with a light background used to highlight important content, such as the main message on a home page, with a big heading, a lead paragraph and a call-to-action button.</p>
<ul><li>Bootstrap 3 and 4 had the class <code>.jumbotron</code> (and <code>.jumbotron-fluid</code> for full width).</li>
<li><b>Bootstrap 5 removed it</b>; the same result is built with utilities: padding <code>p-5</code>, background <code>bg-body-tertiary</code>, <code>rounded-3</code>, big heading <code>display-5</code>, and <code>lead</code> text.</li>
<li>For a full-width jumbotron, put it outside the container and use a <code>container</code> inside.</li></ul>
@@s_jumbotron@@
<h4>Page header</h4>
<p>A <b>page header</b> is a heading at the top of a page or section with extra space and a line below it. BS3 used <code>.page-header</code>; in BS5 use <code>border-bottom pb-2 mb-3</code>, with a <code>small</code> grey subtitle.</p>
@@s_page_header@@
""", programs=["w3_13"]),
        T("Thumbnails", """
<p>A <b>thumbnail</b> is a small preview image (often with a caption) shown in a grid, used for photo galleries, products, courses or videos.</p>
<ul><li><b>Bootstrap 3:</b> <code>.thumbnail</code> on a box around an image, with <code>.caption</code> for the text.</li>
<li><b>Bootstrap 5:</b> <code>.img-thumbnail</code> gives an image a 1 px border, padding and rounded corners. For thumbnails with captions and buttons, use <b>cards</b> in grid columns.</li></ul>
@@s_thumbnail@@
<h4>Thumbnail gallery steps</h4>
<ol><li>Create a <code>.row</code> with <code>g-3</code> gutters.</li>
<li>Use responsive columns such as <code>col-6 col-md-3</code> (2 per row on phones, 4 on desktop).</li>
<li>In each column put an image with <code>img-fluid img-thumbnail</code>, or a card with <code>card-img-top</code>.</li>
<li>Add a caption, and wrap the image in a link for a larger view.</li></ol>
<p>The education site example (Practical 14) combines a breadcrumb, a jumbotron, badges, thumbnails and pagination on one page.</p>
"""),
        T("Alerts", """
<p><b>Alerts</b> provide contextual feedback messages for user actions, e.g. success after saving, an error, a warning or information.</p>
@@s_alert@@
<h4>Alert classes</h4>
<ul><li><b>.alert</b> with a colour: <code>alert-primary, -secondary, -success, -danger, -warning, -info, -light, -dark</code>.</li>
<li><b>.alert-link</b>: link in the matching colour; <b>.alert-heading</b>: title in the alert.</li>
<li><b>Dismissible alert:</b> add <code>.alert-dismissible</code> and a close button <code>button.btn-close data-bs-dismiss="alert"</code>. <code>.fade .show</code> adds a fade-out animation.</li>
<li>Add <code>role="alert"</code> so screen readers announce the message.</li></ul>
<h4>Alert JavaScript</h4>
<p>The alert plug-in fires <b>close.bs.alert</b> (when closing starts) and <b>closed.bs.alert</b> (after it is removed). A message can be shown after an alert is closed, as in Practical 17.</p>
@@s_alert_js@@
<p>New alerts can be created by inserting alert HTML into a container with JavaScript.</p>
""", diagram="web3_alerts_badges", programs=["w3_14"]),
        T("Progress Bars", """
<p>A <b>progress bar</b> shows how much of a task is complete, e.g. a file upload, the steps of a form, course completion or skill levels.</p>
@@s_progress@@
<h4>Types of progress bars</h4>
<table><tr><th>Type</th><th>How</th></tr>
<tr><td>Basic</td><td>.progress outer track + .progress-bar with style="width: 40%"</td></tr>
<tr><td>With label</td><td>Text inside .progress-bar (e.g. 75%)</td></tr>
<tr><td>Height</td><td>style="height: 20px" on .progress</td></tr>
<tr><td>Coloured</td><td>bg-success, bg-info, bg-warning, bg-danger</td></tr>
<tr><td>Striped</td><td>.progress-bar-striped</td></tr>
<tr><td>Animated</td><td>.progress-bar-striped .progress-bar-animated (stripes move)</td></tr>
<tr><td>Multiple (stacked)</td><td>Several bars in .progress-stacked, each in its own .progress</td></tr></table>
<p>For accessibility add <code>role="progressbar"</code> and <code>aria-valuenow</code>, <code>aria-valuemin</code>, <code>aria-valuemax</code>.</p>
<h4>Changing progress with JavaScript</h4>
<p>Change the width style and the text of the bar. <code>setInterval()</code> increases the value step by step.</p>
@@s_progress_js@@
""", diagram="web3_progress", programs=["w3_15"]),
        T("Media Objects", """
<p>A <b>media object</b> is a layout with an image (or video, icon) on one side and text content beside it. It is used for comments, tweets, blog posts, testimonials and profile lists.</p>
<ul><li><b>Bootstrap 3/4:</b> <code>.media</code>, <code>.media-left</code>, <code>.media-body</code>, <code>.media-heading</code>.</li>
<li><b>Bootstrap 5:</b> the media component was removed because the same layout is made with <b>flex utilities</b>: <code>.d-flex</code> on the wrapper, <code>.flex-shrink-0</code> on the image part, <code>.flex-grow-1 .ms-3</code> on the text part.</li></ul>
@@s_media@@
<h4>Variations</h4>
<ul><li><b>Nesting:</b> place another d-flex block inside the text part, e.g. replies to a comment or a family tree (Practical 16).</li>
<li><b>Alignment:</b> <code>align-items-center</code> or <code>align-self-end</code> moves the image to the middle or bottom.</li>
<li><b>Order:</b> put the image after the text (with <code>ms-3</code>) for a right-aligned image.</li>
<li><b>Media list:</b> use a ul with <code>list-unstyled</code> and each li as a d-flex media item.</li></ul>
""", diagram="web3_media_list", programs=["w3_16"]),
        T("List Group and Panels", """
<h4>List group</h4>
<p>A <b>list group</b> displays a series of content items as a bordered list. It is used for menus, settings, notifications and lists of providers.</p>
@@s_list_group@@
<ul><li><code>ul.list-group</code> with <code>li.list-group-item</code>.</li>
<li><b>.active / .disabled</b>: current or disabled item.</li>
<li><b>Links and buttons:</b> <code>div.list-group</code> with <code>a.list-group-item-action</code> for hover and click effects.</li>
<li><b>Colours:</b> <code>list-group-item-success</code>, <code>-danger</code>, <code>-warning</code>, etc.</li>
<li><b>.list-group-flush</b>: removes outer borders (used inside cards); <b>.list-group-numbered</b>: numbers the items; <b>.list-group-horizontal</b>: items in a row.</li>
<li><b>Badges</b> with <code>d-flex justify-content-between</code> show counts on the right.</li>
<li>With <code>data-bs-toggle="list"</code>, list items work like tabs.</li></ul>
<h4>Panels</h4>
<p>A <b>panel</b> (Bootstrap 3) is a bordered box with a coloured heading and a body, used to group related content, e.g. "Internet providers". Classes: <code>.panel .panel-primary</code>, <code>.panel-heading</code>, <code>.panel-title</code>, <code>.panel-body</code>, <code>.panel-footer</code>. Panels were <b>replaced by cards</b> in Bootstrap 4/5.</p>
@@s_panel@@
<p>Practical 17 combines card panels, list groups and dismissible alerts, and shows a message after an alert is closed.</p>
""", programs=["w3_17"]),
    ],
}

NOTES = [SEC_3_1, SEC_3_2, SEC_3_3]
