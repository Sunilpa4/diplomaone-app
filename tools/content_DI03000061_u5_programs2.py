"""DI03000061 RWPD Unit 5 part 2 - customization programs (practical 23-24)."""
from web_content import WE, page

P = []

P.append(WE("w5_11", "Overriding Bootstrap CSS variables in :root", page("CSS Variables", """
<div class="container py-3">
  <h1 class="h5">CSS custom properties (variables)</h1>
  <div class="btn-group btn-group-sm mb-3">
    <button class="btn btn-outline-primary" id="b0">Default
      Bootstrap</button>
    <button class="btn btn-outline-primary" id="b1">:root
      variables overridden</button>
  </div>

  <div class="card shadow-sm">
    <div class="card-body">
      <h2 class="h5">College Notice Board</h2>
      <span class="badge text-bg-primary mb-2">New</span>
      <p class="mb-2">Practical exams start next week.</p>
      <button class="btn btn-primary btn-sm">Read more</button>
      <a href="#" class="ms-2">All notices</a>
    </div>
  </div>

  <pre class="bg-body-secondary border rounded p-2 small mt-3"
    id="src">:root {
  /* no overrides yet */
}</pre>
</div>
""", style="""
.ovr .btn-primary {
  --bs-btn-bg: var(--bs-primary);
  --bs-btn-border-color: var(--bs-primary);
  --bs-btn-hover-bg: #6624b5;
  --bs-btn-hover-border-color: #6624b5;
  --bs-btn-active-bg: #6624b5;
  --bs-btn-active-border-color: #6624b5;
}
.ovr a { color: var(--bs-primary); }
""", script="""
var SRC = ":root {\\n" +
  "  --bs-primary: #0d6efd;\\n" +
  "  --bs-primary-rgb: 13, 110, 253;\\n" +
  "  --bs-body-font-family: system-ui, sans-serif;\\n" +
  "  --bs-border-radius: 0.375rem; }";
var SRC2 = SRC.replace(/#0d6efd/, "#7b1fa2")
  .replace(/13, 110, 253/, "123, 31, 162")
  .replace(/system-ui, sans-serif/, "Georgia, serif")
  .replace(/0.375rem/, "1rem");
var st = null;
function apply(on) {
  var root = document.documentElement.style;
  if (on) {
    root.setProperty("--bs-primary", "#7b1fa2");
    root.setProperty("--bs-primary-rgb", "123, 31, 162");
    root.setProperty("--bs-body-font-family", "Georgia, serif");
    root.setProperty("--bs-border-radius", "1rem");
    st = SRC2;
  } else {
    root.removeProperty("--bs-primary");
    root.removeProperty("--bs-primary-rgb");
    root.removeProperty("--bs-body-font-family");
    root.removeProperty("--bs-border-radius");
    st = SRC;
  }
  document.getElementById("src").textContent = st;
  document.body.classList.toggle("ovr", on);
}
b0.onclick = function() { apply(false); };
b1.onclick = function() { apply(true); };
apply(false);
"""),
"""A notice card with a "New" badge, a blue button and a link.
Click ":root variables overridden": the badge, the button and the link turn purple, the corners become very round, and the font changes to a serif font; the CSS block below shows the new variable values.
Click "Default Bootstrap" to go back to the blue default look.""",
"""
<ul><li>Bootstrap's colours, fonts, borders and spacing variables are stored as <b>CSS custom properties</b> on <code>:root</code>, e.g. <code>--bs-primary</code>, <code>--bs-font-sans-serif</code>, <code>--bs-border-radius</code>.</li>
<li>Every component and utility (btn-primary, text-bg-primary, rounded...) is built on these variables, so overriding them on <code>:root</code> changes the whole site at once — no new CSS per component.</li>
<li>For colour variables, also override the RGB twin (<code>--bs-primary-rgb</code>); it is used for transparency (shadows, opacity).</li>
<li>Buttons use their own variables (<code>--bs-btn-bg</code> ...); point them at <code>--bs-primary</code> or set them, so buttons follow the theme too.</li>
<li>Overrides can also be scoped to one element instead of <code>:root</code> to restyle just that section.</li>
<li>CSS variables are the <b>simplest level of customization</b>: no build tools needed, works at runtime. For deeper changes Sass is used (next programs).</li></ul>
""", actions="apply(true)"))

P.append(WE("w5_12", "Customizing Bootstrap variables with Sass (Practical 23)", page("Sass Variables", """
<div class="container py-3">
  <h1 class="h5">Set Sass variables, then compile</h1>
  <label class="form-label small mb-1">$brand colour</label>
  <input type="color" class="form-control form-control-color mb-2"
    id="col" value="#198754">
  <label class="form-label small mb-1">$border-radius</label>
  <select class="form-select form-select-sm mb-3 w-50" id="rad">
    <option value="0.125rem">0.125rem</option>
    <option value="0.375rem">0.375rem</option>
    <option value="0.75rem" selected>0.75rem</option>
  </select>

  <div class="row g-2">
    <div class="col-12 col-md-6">
      <p class="small mb-1 fw-bold">_variables.scss (input)</p>
      <pre class="text-bg-dark text-light border rounded p-2 small"
        id="scss"></pre>
    </div>
    <div class="col-12 col-md-6">
      <p class="small mb-1 fw-bold">Compiled result (preview)</p>
      <div class="border rounded p-2" id="prev">
        <div class="alert alert-c py-1 small mb-2">
          Semester 3 results are out!</div>
        <button class="btn btn-c btn-sm rounded-c">Download</button>
        <span class="badge badge-c ms-1">Result</span>
      </div>
    </div>
  </div>
  <p class="small mt-2 mb-0">Real step: run
    <code>dart-sass main.scss custom.css</code> (or the Bootstrap
    build) and use <code>custom.css</code> instead of
    bootstrap.css.</p>
</div>
""", style="""
.alert-c { color: #fff; background-color: var(--c); border: 0; }
.btn-c { color: #fff; background-color: var(--c);
  border-radius: var(--r); }
.badge-c { color: #fff; background-color: var(--c); }
.rounded-c { border-radius: var(--r); }
.btn-c:hover { color: #fff; filter: brightness(0.9); }
""", script="""
function hexToRgb(h) {
  var n = parseInt(h.slice(1), 16);
  var rgb = (n >> 16 & 255) + ", " + (n >> 8 & 255);
  return rgb + ", " + (n & 255);
}
function build() {
  var c = document.getElementById("col").value;
  var r = document.getElementById("rad").value;
  document.getElementById("prev").style
    .setProperty("--c", c);
  document.getElementById("prev").style
    .setProperty("--r", r);
  document.getElementById("scss").textContent =
    "// before importing Bootstrap\\n" +
    "$primary: " + c + ";\\n" +
    "$border-radius: " + r + ";\\n\\n" +
    '@import "bootstrap/scss/bootstrap";';
}
col.onchange = build;
rad.onchange = build;
build();
"""),
"""Left: the Sass input file shows $brand colour value #198754; $border-radius: 0.75rem; and the @import of Bootstrap.
Right: a live preview — a green "results are out" alert, a green Download button with large rounded corners and a green badge.
Choose another colour with the colour picker (for example red): the Sass source text and the preview both change to that colour immediately.""",
"""
<ul><li>Bootstrap is written in <b>Sass</b>. Its defaults live in <code>_variables.scss</code> (<code>$primary</code>, <code>$secondary</code>, <code>$border-radius</code>, <code>$font-family-sans-serif</code>, grid breakpoints...).</li>
<li>To customize, create your own file, set the variables <b>before</b> the import line, then import Bootstrap's Sass. Sass variables with <code>!default</code> in Bootstrap yield to your values.</li>
<li>Change the brand colour or corner radius here and see the compiled result instantly; the left panel shows the exact Sass source that produces it.</li>
<li>Compile with <code>dart-sass main.scss custom.css</code> (or npm + sass) and link custom.css instead of the default bootstrap.css. Every component uses the new defaults without touching the HTML.</li>
<li>Needs Node/Sass toolchain — the only method that changes default values for ALL components at compile time.</li></ul>
"""))

P.append(WE("w5_13", "Customizing Bootstrap components with Sass (Practical 24a)", page("Component Customization", """
<div class="container py-3">
  <h1 class="h5">Override component variables</h1>
  <label class="form-label small mb-1">$card-border-radius:
    <b id="rv">1.5rem</b></label>
  <input type="range" class="form-range w-50 mb-1" id="rang"
    min="0" max="30" value="24">
  <div class="row g-2">
    <div class="col-12 col-md-6">
      <p class="small mb-1 fw-bold">_vars.scss (input)</p>
      <pre class="text-bg-dark text-light border rounded p-2 small"
        id="src"></pre>
    </div>
    <div class="col-12 col-md-6">
      <p class="small mb-1 fw-bold">Customized card + button</p>
      <div class="card cbig shadow">
        <div class="card-body">
          <h2 class="h6">Exam form</h2>
          <p class="small mb-2">Last date: 30 Oct</p>
          <button class="btn btn-primary btn-sm bbig">Apply</button>
        </div>
      </div>
    </div>
  </div>
  <p class="small mt-2 mb-0">Add your own component variant with
    <code>map-merge</code>:
    <code>$theme-colors: map-merge($theme-colors,
      ("brand": #7b1fa2));</code> gives you
    <code>btn-brand</code>, <code>alert-brand</code> and
    <code>bg-brand</code> for free.</p>
</div>
""", script="""
function build() {
  var px = document.getElementById("rang").value;
  var rem = (px / 16) + "rem";
  document.getElementById("rv").textContent = rem;
  document.querySelectorAll(".cbig").forEach(function(e) {
    e.style.setProperty("--bs-card-border-radius", rem);
  });
  document.querySelectorAll(".bbig").forEach(function(e) {
    e.style.borderRadius = (px / 32) + "rem";
  });
  document.getElementById("src").textContent =
    "// component variables\\n" +
    "$card-border-radius: " + rem + ";\\n" +
    "$btn-border-radius: " + (px / 32) + "rem;\\n\\n" +
    '@import "bootstrap/scss/bootstrap";';
}
rang.oninput = build;
build();
"""),
"""Left: the Sass source shows $card-border-radius: 1.5rem; and $btn-border-radius: 0.75rem; before the Bootstrap import.
Right: a shadowed card with very round corners and a round Apply button.
Drag the slider: the card and button corners and the Sass source update live — exactly what changes when you recompile with the new component variables.""",
"""
<ul><li>Every component has its own Sass variables: <code>$card-border-radius</code>, <code>$card-box-shadow</code>, <code>$btn-border-radius-lg</code>, <code>$navbar-padding-y</code>, <code>$modal-content-border-width</code>...</li>
<li>Set them before importing Bootstrap to reshape only that component (like the card above), while the global <code>$border-radius</code> stays untouched.</li>
<li>Component variables are documented at the bottom of each component's docs page.</li>
<li><b>Sass maps</b>: extend <code>$theme-colors</code> with <code>map-merge</code> to add a brand colour; it automatically creates utilities and component variants (btn-brand, alert-brand, text-brand, bg-brand).</li>
<li>Remove unused colours with <code>map-remove</code> to shrink the compiled CSS.</li></ul>
""", actions="rang.value=4;build()"))

P.append(WE("w5_14", "Customizing Bootstrap themes and dark mode (Practical 24b)", page("Themes and Dark Mode", """
<div data-bs-theme="light" id="zone" class="bg-body
  text-body rounded p-2">
  <div class="container py-2">
    <div class="d-flex align-items-center justify-content-between
      mb-3">
      <span class="fw-bold">DiplomaOne</span>
      <select class="form-select form-select-sm w-auto" id="th">
        <option value="light">Default theme</option>
        <option value="dark">Dark theme</option>
        <option value="bsnew">Custom theme (purple)</option>
      </select>
    </div>
    <div class="card shadow-sm mb-2">
      <div class="card-body">
        <h2 class="h6">Unit 5: Utilities</h2>
        <span class="badge text-bg-primary mb-2">New</span>
        <p class="small mb-2">Spacing, flexbox, colours, Sass.</p>
        <button class="btn btn-primary btn-sm">Open</button>
      </div>
    </div>
  </div>
</div>
<p class="small text-body-secondary px-2">The select sets
  <code>data-bs-theme</code> and the variables inside the box.</p>
""", style="""
[data-bs-theme="bsnew"] {
  --bs-body-bg: #f3ecfa;
  --bs-body-color: #3c2352;
  --bs-primary: #7b2cd9;
  --bs-primary-rgb: 123, 44, 217;
  --bs-border-radius: 0.9rem;
  color-scheme: light;
}
[data-bs-theme="bsnew"] .text-bg-primary {
  color: #fff !important;
  background-color: rgba(123, 44, 217, 1) !important;
}
[data-bs-theme="bsnew"] .btn-primary {
  --bs-btn-bg: #7b2cd9;
  --bs-btn-border-color: #7b2cd9;
  --bs-btn-hover-bg: #6624b5;
  --bs-btn-hover-border-color: #6624b5;
}
""", script="""
th.onchange = function() {
  document.getElementById("zone").dataset.bsTheme = th.value;
};
"""),
"""A mini page with a "DiplomaOne" header bar, a Unit 5 card with a badge and an Open button.
Choose "Dark theme": the box background and the card go dark, text becomes light — real Bootstrap dark mode via data-bs-theme="dark".
Choose "Custom theme (purple)": the box turns light lavender, headings become dark purple, the badge and button become the app's brand purple with larger rounded corners.""",
"""
<ul><li>A <b>theme</b> is a complete set of variable and component overrides that gives the site its own identity (colours, radius, shadows, fonts).</li>
<li>Bootstrap 5.3 adds <b>colour modes</b>: set <code>data-bs-theme="dark"</code> on <code>&lt;html&gt;</code> or on any section to switch it to dark; <code>data-bs-theme="light"</code> is the default. All components react automatically.</li>
<li><b>Custom themes</b> are made by overriding CSS variables under your own <code>[data-bs-theme="name"]</code> selector (as in this program), or by compiling a custom Sass build per theme.</li>
<li>Keep theming at variable level: write markup with semantic classes (text-bg-primary, btn-primary), never hard-coded hex colours, and themes switch cleanly.</li>
<li>Ready-made themes (Bootswatch, Start Bootstrap) are simply packaged sets of these same overrides.</li></ul>
"""))

PROGRAMS2 = P
