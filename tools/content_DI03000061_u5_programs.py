"""DI03000061 RWPD Unit 5 – Bootstrap utilities and customization (practicals 22-24)."""
from web_content import WE, page

P = []

BP_BADGE = """<span class="badge text-bg-dark">Screen:
    <span class="d-inline d-sm-none">xs</span>
    <span class="d-none d-sm-inline d-md-none">sm</span>
    <span class="d-none d-md-inline d-lg-none">md</span>
    <span class="d-none d-lg-inline d-xl-none">lg</span>
    <span class="d-none d-xl-inline">xl+</span>
  </span>"""

# ------------------------------------------------------------------ 5.1
P.append(WE("w5_1", "Spacing utilities: margin, padding and gap", page("Spacing", """
<div class="container py-3">
  <h1 class="h5">Spacing: {property}{sides}-{size}</h1>

  <h2 class="h6">Padding sizes p-0 to p-5</h2>
  <div class="d-flex flex-wrap gap-2 mb-3">
    <div class="bg-info p-0">p-0</div>
    <div class="bg-info p-1">p-1</div>
    <div class="bg-info p-2">p-2</div>
    <div class="bg-info p-3">p-3</div>
    <div class="bg-info p-4">p-4</div>
    <div class="bg-info p-5">p-5</div>
  </div>

  <h2 class="h6">Sides: t, b, s (start), e (end), x, y</h2>
  <div class="bg-warning-subtle border mb-3">
    <div class="bg-warning mt-3 ms-5 p-2">mt-3 ms-5</div>
    <div class="bg-warning my-3 mx-auto px-4 py-2"
      style="width: 200px">my-3 mx-auto (centred)</div>
  </div>

  <h2 class="h6">Gap between flex items</h2>
  <div class="d-flex gap-3 mb-3">
    <div class="bg-success text-white p-2">gap-3</div>
    <div class="bg-success text-white p-2">gap-3</div>
    <div class="bg-success text-white p-2">gap-3</div>
  </div>

  <h2 class="h6">Responsive spacing</h2>
  <div class="bg-primary text-white p-1 p-md-5">
    p-1 on phones, p-md-5 from 768 px</div>
</div>
"""),
"""A row of blue boxes with increasing padding labelled p-0 to p-5.
In a light yellow area: one box pushed down and right (mt-3 ms-5) and a 200 px box centred with mx-auto.
Three green boxes separated by gap-3. A blue box with small padding on a phone and large padding (p-md-5) on a wider screen.""",
"""
<ul><li>Format: <b>{property}{sides}-{size}</b>. Property: <code>m</code> (margin) or <code>p</code> (padding).</li>
<li>Sides: <code>t</code> top, <code>b</code> bottom, <code>s</code> start (left), <code>e</code> end (right), <code>x</code> left + right, <code>y</code> top + bottom, none = all sides. (Bootstrap 4 used l and r.)</li>
<li>Sizes: 0, 1 (0.25rem), 2 (0.5rem), 3 (1rem), 4 (1.5rem), 5 (3rem), and <code>auto</code> for margins.</li>
<li><code>mx-auto</code> centres a block element that has a width.</li>
<li><code>gap-*</code>, <code>row-gap-*</code>, <code>column-gap-*</code> set the space between flex or grid items.</li>
<li>Responsive: <code>{property}{sides}-{bp}-{size}</code>, e.g. <code>p-md-5</code>, <code>mt-lg-0</code>.</li></ul>
"""))

P.append(WE("w5_2", "Sizing utilities: width, height and ratio", page("Sizing", """
<div class="container py-3">
  <h1 class="h5">Width (relative to parent)</h1>
  <div class="bg-light border p-1 mb-3">
    <div class="w-25 bg-primary text-white p-1 mb-1">w-25</div>
    <div class="w-50 bg-primary text-white p-1 mb-1">w-50</div>
    <div class="w-75 bg-primary text-white p-1 mb-1">w-75</div>
    <div class="w-100 bg-primary text-white p-1 mb-1">w-100</div>
    <div class="w-auto d-inline-block bg-dark text-white p-1">
      w-auto</div>
  </div>

  <h2 class="h5">Height</h2>
  <div class="d-flex align-items-start gap-2 bg-light border mb-3"
    style="height: 120px">
    <div class="h-25 bg-success text-white px-2">h-25</div>
    <div class="h-50 bg-success text-white px-2">h-50</div>
    <div class="h-75 bg-success text-white px-2">h-75</div>
    <div class="h-100 bg-success text-white px-2">h-100</div>
  </div>

  <h2 class="h5">Max width and ratio</h2>
  <img src="img/banner.jpg" class="mw-100 mb-2" width="900"
    height="120" alt="mw-100 banner">
  <div class="ratio ratio-16x9 w-50 bg-dark text-white">
    <div class="d-flex align-items-center justify-content-center">
      ratio-16x9 (video box)</div>
  </div>
</div>
"""),
"""Four blue bars that fill 25%, 50%, 75% and 100% of the grey box, plus a dark w-auto box only as wide as its text.
Four green bars that are 25% to 100% as tall as the 120 px box.
A wide banner image that never gets wider than the screen (mw-100), and a dark box with a 16:9 shape, half the page wide.""",
"""
<ul><li><b>Width:</b> <code>w-25</code>, <code>w-50</code>, <code>w-75</code>, <code>w-100</code>, <code>w-auto</code>, percentages of the parent's width.</li>
<li><b>Height:</b> <code>h-25</code> to <code>h-100</code>, <code>h-auto</code>; percentages of the parent's height (the parent needs a height).</li>
<li><b>Max:</b> <code>mw-100</code> (max-width: 100%), <code>mh-100</code>.</li>
<li><b>Viewport:</b> <code>vw-100</code>, <code>vh-100</code>, <code>min-vw-100</code>, <code>min-vh-100</code> (e.g. a full-screen landing section).</li>
<li><b>Ratio:</b> <code>.ratio .ratio-16x9</code> (also 1x1, 4x3, 21x9) keeps an aspect ratio for videos and iframes; the child fills the box.</li></ul>
"""))

P.append(WE("w5_3", "Display and visibility utilities with a breakpoint indicator", page("Display", f"""
<div class="container py-3">
  <h1 class="h5">Display and visibility</h1>
  <p>{BP_BADGE}</p>

  <h2 class="h6">Display values</h2>
  <span class="d-block bg-info p-1 mb-1">span with d-block</span>
  <div class="d-inline bg-warning p-1">div d-inline</div>
  <div class="d-inline-block bg-warning p-1 w-25">
    inline-block</div>

  <h2 class="h6 mt-3">Responsive show / hide</h2>
  <div class="alert alert-primary d-md-none py-2">
    Phone view: only on screens below 768 px</div>
  <div class="alert alert-success d-none d-md-block py-2">
    Desktop view: only from 768 px</div>

  <h2 class="h6">Visibility</h2>
  <div class="d-flex gap-2">
    <div class="bg-danger text-white p-2">A</div>
    <div class="bg-danger text-white p-2 invisible">B</div>
    <div class="bg-danger text-white p-2">C</div>
  </div>
  <p class="small">B is invisible but keeps its space.
    <span class="visually-hidden">Read by screen readers
      only.</span></p>
  <button class="btn btn-sm btn-dark d-print-none"
    onclick="window.print()">Print (button hidden when printing)
  </button>
</div>
"""),
"""A dark badge shows the current screen size, e.g. "Screen: xs" on a phone or "Screen: xl+" on a large monitor.
A blue full-width span, two yellow inline boxes, a blue "Phone view" alert on small screens or a green "Desktop view" alert on wide screens.
Boxes A and C are red with an empty gap where the invisible box B is.""",
"""
<ul><li><b>Display:</b> <code>.d-{value}</code> or <code>.d-{bp}-{value}</code>; values none, inline, inline-block, block, grid, inline-grid, table, flex, inline-flex.</li>
<li><b>Responsive hiding:</b> <code>d-none d-md-block</code> = hidden below md; <code>d-md-none</code> = visible only below md. The badge uses this to show the current breakpoint.</li>
<li><b>Visibility:</b> <code>.invisible</code> hides but keeps the space (visibility: hidden); <code>.visible</code> shows it.</li>
<li><code>.visually-hidden</code> hides content from the screen but not from screen readers.</li>
<li><b>Print:</b> <code>.d-print-none</code>, <code>.d-print-block</code> control what is printed.</li></ul>
"""))

P.append(WE("w5_4", "Position utilities: relative, absolute, translate-middle, z-index", page("Position", """
<div class="container py-3">
  <h1 class="h5">Position utilities</h1>
  <div class="position-relative bg-light border mb-4"
    style="height: 170px">
    <div class="position-absolute top-0 start-0 bg-primary
      text-white p-1">top-0 start-0</div>
    <div class="position-absolute top-0 end-0 bg-primary
      text-white p-1">top-0 end-0</div>
    <div class="position-absolute top-50 start-50
      translate-middle bg-danger text-white p-2">centre</div>
    <div class="position-absolute bottom-0 start-0 bg-success
      text-white p-1">bottom-0 start-0</div>
    <div class="position-absolute bottom-0 end-0 bg-success
      text-white p-1">bottom-0 end-0</div>
  </div>

  <h2 class="h6">Badge on a button</h2>
  <button class="btn btn-dark position-relative mb-4">
    Messages
    <span class="position-absolute top-0 start-100
      translate-middle badge rounded-pill bg-danger">5</span>
  </button>

  <h2 class="h6">z-index</h2>
  <div class="position-relative" style="height: 80px">
    <div class="position-absolute bg-warning p-3 z-1"
      style="left: 0; top: 0">z-1</div>
    <div class="position-absolute bg-info p-3 z-3"
      style="left: 30px; top: 20px">z-3 (on top)</div>
    <div class="position-absolute bg-success text-white p-3 z-2"
      style="left: 60px; top: 40px">z-2</div>
  </div>
</div>
"""),
"""A grey box with labels in all four corners (blue at the top, green at the bottom) and a red "centre" label exactly in the middle.
A dark "Messages" button with a red round badge "5" on its top-right corner.
Three overlapping coloured boxes; the blue z-3 box is on top of both others.""",
"""
<ul><li><b>Position:</b> <code>position-static</code>, <code>-relative</code>, <code>-absolute</code>, <code>-fixed</code>, <code>-sticky</code>.</li>
<li><b>Edges:</b> <code>top-</code>, <code>bottom-</code>, <code>start-</code>, <code>end-</code> with values 0, 50, 100 (%).</li>
<li><b>translate-middle</b> moves the element back by 50% of its own size, so <code>top-50 start-50 translate-middle</code> centres it exactly. Also <code>translate-middle-x</code> and <code>-y</code>.</li>
<li>An absolute element is placed relative to the nearest <b>position-relative</b> parent.</li>
<li><b>z-index:</b> <code>z-n1</code>, <code>z-0</code>, <code>z-1</code>, <code>z-2</code>, <code>z-3</code> (Bootstrap 5.3); higher numbers are drawn on top.</li>
<li>Shortcuts: <code>.fixed-top</code>, <code>.fixed-bottom</code>, <code>.sticky-top</code>, <code>.sticky-bottom</code>.</li></ul>
"""))

P.append(WE("w5_5", "Flexbox utilities: direction, justify, align, wrap, order, grow", page("Flexbox", """
<div class="container py-3">
  <h1 class="h5">Flexbox utilities</h1>
  <label class="form-label small mb-1">justify-content-*</label>
  <select class="form-select form-select-sm mb-2" id="jc">
    <option>start</option><option>center</option>
    <option>end</option>
    <option selected>between</option><option>around</option>
    <option>evenly</option>
  </select>
  <label class="form-label small mb-1">align-items-*</label>
  <select class="form-select form-select-sm mb-2" id="ai">
    <option>start</option><option selected>center</option>
    <option>end</option><option>stretch</option>
  </select>
  <div class="d-flex justify-content-between align-items-center
    bg-light border mb-1" id="box" style="height: 110px">
    <div class="bg-primary text-white p-2">One</div>
    <div class="bg-primary text-white p-3">Two</div>
    <div class="bg-primary text-white p-2">Three</div>
  </div>
  <code class="small" id="cls"></code>

  <h2 class="h6 mt-3">Column on phone, row from md</h2>
  <div class="d-flex flex-column flex-md-row gap-2 mb-3">
    <div class="bg-success text-white p-2 order-md-2">A
      (order-md-2)</div>
    <div class="bg-success text-white p-2 flex-grow-1">B
      (flex-grow-1)</div>
    <div class="bg-success text-white p-2 ms-md-auto">C
      (ms-md-auto)</div>
  </div>

  <h2 class="h6">flex-wrap</h2>
  <div class="d-flex flex-wrap gap-1" id="wrap"></div>
</div>
""", script="""
var box = document.getElementById("box");
function update() {
  box.className = "d-flex bg-light border mb-1" +
    " justify-content-" + jc.value + " align-items-" + ai.value;
  document.getElementById("cls").textContent =
    'class="d-flex justify-content-' + jc.value +
    " align-items-" + ai.value + '"';
}
jc.onchange = update;
ai.onchange = update;
update();

for (var i = 1; i <= 12; i++) {
  document.getElementById("wrap").innerHTML +=
    '<span class="badge text-bg-secondary p-2">Item ' + i +
    "</span>";
}
"""),
"""Two drop-down lists choose justify-content (start, center, end, between, around, evenly) and align-items (start, center, end, stretch). The three blue boxes move immediately and the class used is shown below, e.g. class="d-flex justify-content-between align-items-center".
Three green boxes are stacked on a phone and form a row from 768 px, where A moves to the middle, B stretches and C is pushed to the right.
Twelve grey badges wrap onto new lines.""",
"""
<ul><li><code>d-flex</code> / <code>d-inline-flex</code> make a flex container (responsive: <code>d-md-flex</code>).</li>
<li><b>Direction:</b> <code>flex-row</code>, <code>flex-column</code>, <code>-reverse</code>; e.g. <code>flex-column flex-md-row</code>.</li>
<li><b>justify-content-</b>start / center / end / between / around / evenly: main-axis spacing.</li>
<li><b>align-items-</b>start / center / end / baseline / stretch: cross-axis alignment; <code>align-self-*</code> for one item; <code>align-content-*</code> for wrapped lines.</li>
<li><b>Wrap:</b> <code>flex-wrap</code>, <code>flex-nowrap</code>. <b>Order:</b> <code>order-0</code> to <code>order-5</code>, <code>order-first</code>, <code>order-last</code>.</li>
<li><b>Grow/shrink:</b> <code>flex-fill</code>, <code>flex-grow-1</code>, <code>flex-shrink-0</code>. <b>Auto margins</b> (<code>ms-auto</code>) push items apart.</li></ul>
""", actions="jc.value='evenly';ai.value='end';update()"))

P.append(WE("w5_6", "Border and rounded corner utilities", page("Borders", """
<div class="container py-3">
  <h1 class="h5">Borders</h1>
  <div class="d-flex flex-wrap gap-2 mb-3 text-center small">
    <div class="border p-2">border</div>
    <div class="border-top p-2">border-top</div>
    <div class="border-end p-2">border-end</div>
    <div class="border-bottom p-2">border-bottom</div>
    <div class="border-start p-2">border-start</div>
    <div class="border border-top-0 p-2">border-top-0</div>
  </div>
  <div class="d-flex flex-wrap gap-2 mb-3 text-center small">
    <div class="border border-primary p-2">primary</div>
    <div class="border border-danger border-2 p-2">danger 2</div>
    <div class="border border-success border-5 p-2">success 5</div>
    <div class="border border-dark border-3 border-opacity-25 p-2">
      opacity-25</div>
  </div>

  <h2 class="h5">Rounded corners</h2>
  <div class="d-flex flex-wrap gap-2 align-items-center small">
    <div class="bg-info p-3 rounded-0">rounded-0</div>
    <div class="bg-info p-3 rounded">rounded</div>
    <div class="bg-info p-3 rounded-3">rounded-3</div>
    <div class="bg-info p-3 rounded-5">rounded-5</div>
    <div class="bg-info p-3 rounded-top">top</div>
    <div class="bg-warning p-3 rounded-pill px-4">pill</div>
    <div class="bg-warning rounded-circle d-flex align-items-center
      justify-content-center" style="width: 70px; height: 70px">
      circle</div>
  </div>
</div>
"""),
"""Boxes with a border on all sides, only one side, or all sides except the top.
Coloured borders: blue, red 2 px, thick green 5 px and a faint dark border (opacity 25%).
Light-blue boxes with no rounding, normal, larger and very large rounded corners, and rounding only at the top; a yellow pill-shaped box (pill) and a yellow circle.""",
"""
<ul><li><b>Add borders:</b> <code>border</code>, <code>border-top</code>, <code>border-end</code>, <code>border-bottom</code>, <code>border-start</code>.</li>
<li><b>Remove:</b> <code>border-0</code>, <code>border-top-0</code>, etc.</li>
<li><b>Colour:</b> <code>border-primary</code>, <code>border-danger</code>, <code>border-success-subtle</code>...; <b>width:</b> <code>border-1</code> to <code>border-5</code>; <b>opacity:</b> <code>border-opacity-10/25/50/75</code>.</li>
<li><b>Rounded:</b> <code>rounded</code>, <code>rounded-0</code> to <code>rounded-5</code>, <code>rounded-top/-end/-bottom/-start</code>, <code>rounded-circle</code>, <code>rounded-pill</code>.</li>
<li>A circle needs equal width and height.</li></ul>
"""))

P.append(WE("w5_7", "Background and colour utilities", page("Background", """
<div class="container py-3">
  <h1 class="h5">Background colours</h1>
  <div class="row row-cols-2 row-cols-md-4 g-2 mb-3 small">
    <div><div class="p-2 bg-primary text-white">bg-primary</div></div>
    <div><div class="p-2 bg-success text-white">bg-success</div></div>
    <div><div class="p-2 bg-danger text-white">bg-danger</div></div>
    <div><div class="p-2 bg-warning">bg-warning</div></div>
    <div><div class="p-2 bg-info">bg-info</div></div>
    <div><div class="p-2 bg-dark text-white">bg-dark</div></div>
    <div><div class="p-2 bg-light border">bg-light</div></div>
    <div><div class="p-2 bg-body-secondary">body-secondary</div></div>
  </div>

  <h2 class="h6">text-bg-* (background + readable text)</h2>
  <span class="badge text-bg-warning">Warning</span>
  <span class="badge text-bg-info">Info</span>
  <span class="badge text-bg-light">Light</span>

  <h2 class="h6 mt-3">Gradient, subtle and opacity</h2>
  <div class="d-flex flex-wrap gap-2 small">
    <div class="p-3 bg-primary bg-gradient text-white">
      gradient</div>
    <div class="p-3 bg-danger-subtle text-danger-emphasis">
      subtle + emphasis</div>
    <div class="p-3 bg-success bg-opacity-75 text-white">
      opacity-75</div>
    <div class="p-3 bg-success bg-opacity-25">opacity-25</div>
  </div>

  <h2 class="h6 mt-3">Text colours</h2>
  <p class="mb-0"><span class="text-primary">primary</span>
    <span class="text-success">success</span>
    <span class="text-danger">danger</span>
    <span class="text-body-secondary">muted</span>
    <span class="text-white bg-dark px-1">white</span>
    <a href="#" class="link-danger">link-danger</a></p>
</div>
"""),
"""Eight coloured boxes (2 per row on a phone, 4 on a desktop): blue, green, red, yellow, light blue, dark, light and light grey.
Three badges with automatic readable text colour. A blue box with a soft gradient, a pale red box with dark red text, and two green boxes at 75% and 25% opacity.
A line of words in different text colours and a red link.""",
"""
<ul><li><b>Background:</b> <code>bg-primary</code>, <code>-secondary</code>, <code>-success</code>, <code>-danger</code>, <code>-warning</code>, <code>-info</code>, <code>-light</code>, <code>-dark</code>, <code>-white</code>, <code>-transparent</code>, <code>bg-body</code>, <code>bg-body-secondary</code>, <code>bg-body-tertiary</code>.</li>
<li><b>text-bg-*</b> sets the background and a contrasting text colour together.</li>
<li><b>bg-gradient</b> adds a light gradient over the colour.</li>
<li><b>Subtle colours:</b> <code>bg-*-subtle</code> with <code>text-*-emphasis</code> (Bootstrap 5.3).</li>
<li><b>bg-opacity-10/25/50/75/100</b> changes only the background transparency (also <code>text-opacity-*</code>).</li>
<li><b>Text colour:</b> <code>text-primary</code> ... <code>text-body-secondary</code> (muted); <b>link colour:</b> <code>link-*</code>.</li></ul>
"""))

P.append(WE("w5_8", "Opacity, overflow and shadow utilities", page("Opacity Overflow Shadow", """
<div class="container py-3">
  <h1 class="h5">Opacity</h1>
  <div class="d-flex gap-2 mb-3 small">
    <div class="bg-primary text-white p-2 opacity-100">100</div>
    <div class="bg-primary text-white p-2 opacity-75">75</div>
    <div class="bg-primary text-white p-2 opacity-50">50</div>
    <div class="bg-primary text-white p-2 opacity-25">25</div>
  </div>

  <h2 class="h5">Overflow</h2>
  <div class="row g-2 mb-3 small">
    <div class="col-6 col-md-3"><div class="overflow-auto border p-1"
      style="height: 70px">overflow-auto: scroll bar appears only
      when the text is longer than the box.</div></div>
    <div class="col-6 col-md-3"><div class="overflow-hidden border p-1"
      style="height: 70px">overflow-hidden: the extra text is cut
      off and cannot be seen at all.</div></div>
    <div class="col-6 col-md-3"><div class="overflow-scroll border p-1"
      style="height: 70px">overflow-scroll: always shows
      scroll bars.</div></div>
    <div class="col-6 col-md-3"><div class="overflow-x-auto border p-1">
      <span class="text-nowrap">overflow-x-auto: a very long
        line scrolls sideways</span></div></div>
  </div>

  <h2 class="h5">Shadows</h2>
  <div class="d-flex flex-wrap gap-3 p-2">
    <div class="shadow-none p-3 bg-body-tertiary rounded">
      none</div>
    <div class="shadow-sm p-3 bg-body rounded">shadow-sm</div>
    <div class="shadow p-3 bg-body rounded">shadow</div>
    <div class="shadow-lg p-3 bg-body rounded">shadow-lg</div>
  </div>
</div>
"""),
"""Four blue boxes from fully solid (100) to very faint (25).
Four small bordered boxes: one with a scroll bar for long text, one that cuts the text off, one that always shows scroll bars, and one with a long line that scrolls sideways.
Four white boxes with no shadow, a small shadow, a normal shadow and a large shadow.""",
"""
<ul><li><b>Opacity:</b> <code>opacity-0</code>, <code>-25</code>, <code>-50</code>, <code>-75</code>, <code>-100</code>; makes the whole element (text too) transparent. To fade only the background use <code>bg-opacity-*</code>.</li>
<li><b>Overflow:</b> <code>overflow-auto</code> (scroll if needed), <code>-hidden</code> (cut off), <code>-visible</code> (default, spills out), <code>-scroll</code> (always scroll bars); <code>overflow-x-*</code> and <code>overflow-y-*</code> for one direction.</li>
<li>Overflow only matters when the element has a fixed height or width.</li>
<li><b>Shadow:</b> <code>shadow-none</code>, <code>shadow-sm</code>, <code>shadow</code>, <code>shadow-lg</code>; used on cards, navbars and buttons to give depth.</li></ul>
"""))

P.append(WE("w5_9", "Responsive utilities: classes with breakpoint infixes", page("Responsive Utilities", f"""
<div class="container py-3">
  <p>{BP_BADGE}</p>
  <div class="d-flex flex-column flex-md-row align-items-center
    gap-3 border rounded p-3 p-lg-4 mb-3
    text-center text-md-start">
    <img src="img/teacher.jpg" class="rounded-circle" width="90"
      height="90" alt="Teacher">
    <div class="flex-grow-1">
      <h2 class="h5 mb-1">Prof. A. Mehta</h2>
      <p class="mb-0 text-body-secondary">Computer Engineering
        department</p>
    </div>
    <button class="btn btn-primary w-100 w-md-auto">Contact</button>
  </div>
  <div class="bg-light border p-2 small">
    <span class="float-md-end text-success">float-md-end</span>
    Text on the left; the green text moves to the right from md.
  </div>
  <p class="mt-3 small">Classes used:
    flex-column flex-md-row, text-center text-md-start,
    p-3 p-lg-4, float-md-end, w-100 w-md-auto.</p>
</div>
""", style="""
/* Bootstrap has no w-md-auto; add your own responsive class */
@media (min-width: 768px) {
  .w-md-auto { width: auto !important; }
}
"""),
"""On a phone: the teacher's photo, name and department are stacked and centred, and the Contact button is full width.
From 768 px: photo, text and button are in one row, text is left-aligned, and the button is normal width. From 992 px the padding becomes larger.
The green "float-md-end" text moves to the right side from md. The badge shows the current breakpoint.""",
"""
<ul><li>Most utilities have <b>responsive versions</b> with a breakpoint infix: <code>{utility}-{bp}-{value}</code>, where bp = sm, md, lg, xl, xxl.</li>
<li>Bootstrap is <b>mobile first</b>: the class without a breakpoint applies to all screens; the md class overrides it from 768 px up.</li>
<li>Responsive utilities include display (<code>d-md-flex</code>), flex (<code>flex-md-row</code>, <code>justify-content-lg-between</code>), spacing (<code>p-lg-4</code>), text alignment (<code>text-md-start</code>), float (<code>float-md-end</code>), sticky (<code>sticky-md-top</code>) and grid columns.</li>
<li>Width, height, colour and border utilities are <b>not</b> responsive by default; a small media query (like <code>.w-md-auto</code> here) or the Sass utility API adds them.</li></ul>
"""))

P.append(WE("w5_10", "Header and footer of a tourism website using only utility classes (Practical 22)", page("Tourism Header Footer", """
<header class="bg-primary bg-gradient text-white shadow">
  <div class="container d-flex flex-wrap align-items-center
    justify-content-between gap-2 py-2">
    <a href="#" class="d-flex align-items-center gap-2 text-white
      text-decoration-none">
      <i class="bi bi-globe-asia-australia fs-2"></i>
      <span class="fs-5 fw-bold">Gujarat Tourism</span>
    </a>
    <ul class="nav order-3 order-md-2 w-100 w-md-auto
      justify-content-center small">
      <li><a href="#" class="nav-link px-2 text-white
        fw-semibold">Home</a></li>
      <li><a href="#" class="nav-link px-2 text-white-50">Places</a></li>
      <li><a href="#" class="nav-link px-2 text-white-50">Hotels</a></li>
      <li><a href="#" class="nav-link px-2 text-white-50">Contact</a></li>
    </ul>
    <a href="#" class="btn btn-warning btn-sm rounded-pill px-3
      order-2 order-md-3">Book now</a>
  </div>
</header>

<main class="container py-5 text-center">
  <h1 class="display-6 fw-bold">Welcome to Gujarat</h1>
  <p class="lead text-body-secondary">Page content goes here.</p>
</main>

<footer class="bg-dark text-white-50 pt-4 small">
  <div class="container">
    <div class="row g-3">
      <div class="col-12 col-md-5">
        <h2 class="h6 text-white">Gujarat Tourism</h2>
        <p class="mb-0">Heritage, wildlife, beaches and festivals
          of Gujarat in one place.</p>
      </div>
      <div class="col-6 col-md-3">
        <h2 class="h6 text-white">Quick links</h2>
        <ul class="list-unstyled mb-0">
          <li><a href="#" class="link-light
            link-underline-opacity-0">Places</a></li>
          <li><a href="#" class="link-light
            link-underline-opacity-0">Packages</a></li>
          <li><a href="#" class="link-light
            link-underline-opacity-0">FAQ</a></li>
        </ul>
      </div>
      <div class="col-6 col-md-4">
        <h2 class="h6 text-white">Contact</h2>
        <p class="mb-1"><i class="bi bi-telephone me-1"></i>
          1800 200 5080</p>
        <p class="d-flex gap-3 fs-5 mb-0">
          <i class="bi bi-facebook"></i>
          <i class="bi bi-instagram"></i>
          <i class="bi bi-youtube"></i></p>
      </div>
    </div>
    <div class="border-top border-secondary mt-3 py-3 text-center">
      &copy; 2026 Gujarat Tourism. All rights reserved.</div>
  </div>
</footer>
""", style="""
@media (min-width: 768px) {
  .w-md-auto { width: auto !important; }
}
""", icons=True),
"""A blue gradient header with a shadow: a globe icon with "Gujarat Tourism", the links Home, Places, Hotels and Contact, and a yellow pill button "Book now". On a phone, the links move to a second centred line.
A centred "Welcome to Gujarat" heading in the middle of the page.
A dark footer with an about text, quick links, a phone number and Facebook, Instagram and YouTube icons in three columns (stacked on a phone), and a copyright line above a thin border.""",
"""
<ul><li>The header and footer are built only with Bootstrap <b>utility classes</b>; the only custom CSS is one responsive helper (<code>.w-md-auto</code>).</li>
<li><b>Flex utilities</b>: <code>d-flex flex-wrap align-items-center justify-content-between gap-2</code> lay out the header.</li>
<li><b>Order utilities</b>: <code>order-3 order-md-2</code> moves the menu below the logo on phones and between logo and button on desktops.</li>
<li><b>Colour</b>: <code>bg-primary bg-gradient</code>, <code>text-white-50</code>, <code>link-light</code>; <b>shadow</b>: <code>shadow</code>; <b>border</b>: <code>border-top border-secondary</code>; <b>rounded</b>: <code>rounded-pill</code>.</li>
<li><b>Spacing</b>: <code>py-2</code>, <code>px-3</code>, <code>pt-4</code>, <code>mt-3</code>, <code>gap-3</code>. <b>Typography</b>: <code>fs-5 fw-bold small</code>.</li>
<li>The footer grid (<code>col-12 col-md-5</code>, <code>col-6 col-md-3</code>) gives one column on phones and three on desktops.</li></ul>
"""))

PROGRAMS = P + __import__(
    "content_DI03000061_u5_programs2").PROGRAMS2
