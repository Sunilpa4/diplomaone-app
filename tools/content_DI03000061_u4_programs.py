"""DI03000061 RWPD Unit 4 – Bootstrap plug-ins (practicals 18-21)."""
from web_content import WE, page

P = []

# ------------------------------------------------------------------ 4.1
P.append(WE("w4_1", "Using a plug-in two ways: data attributes and JavaScript", page("Using Plug-ins", """
<div class="container py-3">
  <h1 class="h5">Bootstrap plug-ins</h1>
  <p class="small text-muted" id="ver"></p>

  <!-- 1. data attributes: no JavaScript code needed -->
  <button class="btn btn-primary mb-2" data-bs-toggle="collapse"
    data-bs-target="#box1">Toggle with data attribute</button>
  <div class="collapse" id="box1">
    <div class="card card-body mb-3">
      Opened by data-bs-toggle="collapse".</div>
  </div>

  <!-- 2. JavaScript API -->
  <div class="mb-2">
    <button class="btn btn-success" id="show">show()</button>
    <button class="btn btn-warning" id="hide">hide()</button>
    <button class="btn btn-dark" id="tog">toggle()</button>
  </div>
  <div class="collapse" id="box2">
    <div class="card card-body mb-3">
      Opened by JavaScript methods.</div>
  </div>

  <h2 class="h6">Event log</h2>
  <ul class="small" id="log"></ul>
</div>
""", script="""
document.getElementById("ver").textContent =
  "Bootstrap version: " + bootstrap.Collapse.VERSION;

// create (or get) the plug-in object for the element
var box2 = document.getElementById("box2");
var c = new bootstrap.Collapse(box2, { toggle: false });
function $(id) { return document.getElementById(id); }
$("show").onclick = function () { c.show(); };
$("hide").onclick = function () { c.hide(); };
$("tog").onclick = function () { c.toggle(); };

// events: show.bs.collapse, shown, hide, hidden
["shown", "hidden"].forEach(function (ev) {
  document.addEventListener(ev + ".bs.collapse", function (e) {
    var li = document.createElement("li");
    li.textContent = ev + ".bs.collapse on #" + e.target.id;
    document.getElementById("log").appendChild(li);
  });
});
""", bs_js=True),
"""The page shows "Bootstrap version: 5.3.3".
"Toggle with data attribute" opens and closes the first box without any JavaScript code.
The show(), hide() and toggle() buttons control the second box through JavaScript.
Each time a box finishes opening or closing, a line such as "shown.bs.collapse on #box2" is added to the event log.""",
"""
<ul><li>Every Bootstrap plug-in can be used in <b>two ways</b>:
<ol><li><b>Data attributes</b> (no code): <code>data-bs-toggle</code>, <code>data-bs-target</code>, and options as <code>data-bs-*</code>.</li>
<li><b>JavaScript API</b>: <code>new bootstrap.Collapse(el, options)</code> or <code>bootstrap.Collapse.getOrCreateInstance(el)</code>, then call methods.</li></ol></li>
<li><b>Options</b> are passed as an object, here <code>{ toggle: false }</code> so the box does not open on creation.</li>
<li><b>Methods</b> such as show(), hide(), toggle(), dispose() control the plug-in.</li>
<li><b>Events</b> are named <code>action.bs.plugin</code>: the present form (show) fires at the start and the past form (shown) after the animation ends.</li>
<li>All plug-ins are in <code>bootstrap.bundle.min.js</code>, which includes Popper (needed for dropdowns, tooltips and popovers). Bootstrap 5 does not need jQuery.</li></ul>
""", actions="document.getElementById('show').click()"))

P.append(WE("w4_2", "Transition: fade classes and the transitionend event", page("Transition", """
<div class="container py-3">
  <h1 class="h5">Bootstrap transitions</h1>

  <h2 class="h6">1. .fade and .show</h2>
  <button class="btn btn-primary mb-2" id="fadeBtn">Fade out</button>
  <div class="alert alert-info fade show" id="msg">
    I fade in and out with Bootstrap's .fade class.</div>

  <h2 class="h6">2. Custom CSS transition</h2>
  <button class="btn btn-success mb-2" id="moveBtn">Move box</button>
  <div class="box bg-success text-white p-3 rounded" id="box">
    Box</div>
  <p class="small mt-2" id="log">Waiting...</p>
</div>
""", style="""
.box {
  width: 90px;
  transition: margin-left 0.8s ease, background-color 0.8s;
}
.box.moved {
  margin-left: 60%;
  background-color: #6f42c1 !important;
}
""", script="""
var msg = document.getElementById("msg");
document.getElementById("fadeBtn").onclick = function () {
  msg.classList.toggle("show");          // opacity 1 <-> 0
  this.textContent = msg.classList.contains("show") ?
    "Fade out" : "Fade in";
};

var box = document.getElementById("box");
document.getElementById("moveBtn").onclick = function () {
  box.classList.toggle("moved");
};
// fired when a CSS transition finishes
box.addEventListener("transitionend", function (e) {
  document.getElementById("log").textContent =
    "Transition finished: " + e.propertyName;
});
"""),
"""A blue info alert with a "Fade out" button. Clicking it fades the alert smoothly to invisible, and the button changes to "Fade in".
"Move box" slides the green box to the right, changing its colour to purple. After the movement the text reads "Transition finished: margin-left" (or background-color).""",
"""
<ul><li><b>Transition plug-in (Bootstrap 3: transition.js)</b> was a helper used by other plug-ins (modal, carousel, collapse, alert) to detect the end of CSS transitions. In Bootstrap 5 it is built into every plug-in and is not used separately.</li>
<li><b>.fade</b> sets <code>transition: opacity .15s linear</code> and opacity 0; adding <b>.show</b> makes opacity 1. Toggling .show gives a fade effect.</li>
<li>Animated components: modal (fade + slide), alert (fade on close), collapse (<code>.collapsing</code> height animation), carousel (slide or <code>.carousel-fade</code>), tab panes (fade).</li>
<li>Custom effects use the CSS <code>transition</code> property; the <code>transitionend</code> event tells JavaScript when it finished.</li>
<li>Bootstrap respects the user's <b>prefers-reduced-motion</b> setting and turns animations off.</li></ul>
""", actions="document.getElementById('fadeBtn').click();document.getElementById('moveBtn').click()"))

P.append(WE("w4_3", "Smooth page transition: Home, About and Contact (Practical 18)", page("Smooth Pages", """
<nav class="navbar navbar-expand bg-primary" data-bs-theme="dark">
  <div class="container">
    <span class="navbar-brand">GreenTech</span>
    <ul class="navbar-nav" role="tablist">
      <li class="nav-item">
        <a class="nav-link active" data-bs-toggle="tab"
          href="#home">Home</a></li>
      <li class="nav-item">
        <a class="nav-link" data-bs-toggle="tab"
          href="#about">About</a></li>
      <li class="nav-item">
        <a class="nav-link" data-bs-toggle="tab"
          href="#contact">Contact</a></li>
    </ul>
  </div>
</nav>

<div class="tab-content container py-4">
  <section class="tab-pane fade show active" id="home">
    <div class="p-4 bg-body-tertiary rounded-3">
      <h1 class="display-6">Welcome to GreenTech</h1>
      <p class="lead">Solar solutions for homes in Gujarat.</p>
      <button class="btn btn-primary" id="goContact">
        Contact us</button>
    </div>
  </section>

  <section class="tab-pane fade" id="about">
    <h2>About us</h2>
    <p>Started in 2015 in Surat, we have installed solar
      panels on more than 2,000 roofs.</p>
    <div class="row g-3">
      <div class="col-sm-6"><div class="card card-body">
        <b>Mission</b> Clean energy for every home.</div></div>
      <div class="col-sm-6"><div class="card card-body">
        <b>Team</b> 40 trained engineers.</div></div>
    </div>
  </section>

  <section class="tab-pane fade" id="contact">
    <h2>Contact us</h2>
    <form class="row g-2">
      <div class="col-sm-6">
        <input class="form-control" placeholder="Name"></div>
      <div class="col-sm-6">
        <input class="form-control" placeholder="Mobile"></div>
      <div class="col-12">
        <textarea class="form-control" rows="2"
          placeholder="Message"></textarea></div>
      <div class="col-12">
        <button type="button" class="btn btn-success">
          Send</button></div>
    </form>
  </section>
</div>
""", style="""
/* extend Bootstrap's fade with a slide-up */
.tab-pane.fade {
  transform: translateY(25px);
  transition: opacity 0.5s ease, transform 0.5s ease;
}
.tab-pane.fade.show { transform: none; }
""", script="""
// open a "page" from JavaScript
document.getElementById("goContact").onclick = function () {
  var link = document.querySelector('a[href="#contact"]');
  bootstrap.Tab.getOrCreateInstance(link).show();
};
""", bs_js=True),
"""A blue navbar with the brand "GreenTech" and the links Home, About and Contact.
The Home page shows a grey welcome box with a "Contact us" button.
Clicking About or Contact (or the "Contact us" button) makes the current page fade out, and the new page fades in while sliding up slightly, without reloading. About shows two cards (Mission, Team); Contact shows a form with Name, Mobile, Message and Send.""",
"""
<ul><li>The three "pages" are <code>.tab-pane</code> sections in one <code>.tab-content</code>, so changing page needs no reload.</li>
<li>The navbar links use the <b>tab plug-in</b>: <code>data-bs-toggle="tab"</code> with <code>href="#id"</code>.</li>
<li>The <b>transition</b> comes from <code>.fade</code> on each pane: Bootstrap waits for the old pane to fade out before showing the new one (transition end detection).</li>
<li>Custom CSS adds <code>transform: translateY(25px)</code> to make the page slide up while fading in.</li>
<li><code>bootstrap.Tab.getOrCreateInstance(link).show()</code> opens a page from a button.</li>
<li><code>navbar-expand</code> keeps the menu always expanded because it has only three short links.</li></ul>
""", actions="document.querySelector('a[href=\"#about\"]').click()"))

P.append(WE("w4_4", "Modal dialog: basic, centred, large scrollable and static", page("Modals", """
<div class="container py-3">
  <h1 class="h5">Modal dialog boxes</h1>
  <div class="d-flex flex-wrap gap-2">
    <button class="btn btn-primary" data-bs-toggle="modal"
      data-bs-target="#basic">Basic (centred)</button>
    <button class="btn btn-success" data-bs-toggle="modal"
      data-bs-target="#rules">Large + scrollable</button>
    <button class="btn btn-danger" data-bs-toggle="modal"
      data-bs-target="#static">Static backdrop</button>
  </div>
</div>

<!-- 1. basic, vertically centred -->
<div class="modal fade" id="basic" tabindex="-1">
  <div class="modal-dialog modal-dialog-centered">
    <div class="modal-content">
      <div class="modal-header">
        <h5 class="modal-title">Welcome</h5>
        <button class="btn-close" data-bs-dismiss="modal"></button>
      </div>
      <div class="modal-body">
        Results will be declared on 5 Dec.</div>
      <div class="modal-footer">
        <button class="btn btn-secondary"
          data-bs-dismiss="modal">Close</button>
      </div>
    </div>
  </div>
</div>

<!-- 2. large, body scrolls -->
<div class="modal fade" id="rules" tabindex="-1">
  <div class="modal-dialog modal-lg modal-dialog-scrollable">
    <div class="modal-content">
      <div class="modal-header">
        <h5 class="modal-title">Exam rules</h5>
        <button class="btn-close" data-bs-dismiss="modal"></button>
      </div>
      <div class="modal-body" id="ruleList"></div>
      <div class="modal-footer">
        <button class="btn btn-success"
          data-bs-dismiss="modal">I agree</button>
      </div>
    </div>
  </div>
</div>

<!-- 3. does not close on outside click or Esc -->
<div class="modal fade" id="static" tabindex="-1"
  data-bs-backdrop="static" data-bs-keyboard="false">
  <div class="modal-dialog modal-sm">
    <div class="modal-content">
      <div class="modal-body text-center">
        <p>Session expired. Please log in again.</p>
        <button class="btn btn-danger"
          data-bs-dismiss="modal">Log in</button>
      </div>
    </div>
  </div>
</div>
""", script="""
var html = "";
for (var i = 1; i <= 25; i++) {
  html += "<p>" + i + ". Rule number " + i +
    " of the examination.</p>";
}
document.getElementById("ruleList").innerHTML = html;
""", bs_js=True),
"""Three buttons. "Basic (centred)" opens a dialog in the middle of the screen with the title "Welcome", the text "Results will be declared on 5 Dec." and a Close button; the page behind becomes dark.
"Large + scrollable" opens a wide dialog "Exam rules" with 25 rules; only the body scrolls while the header and the "I agree" button stay visible.
"Static backdrop" opens a small dialog "Session expired" that does not close on an outside click or the Esc key, only with "Log in".""",
"""
<ul><li><b>Modal structure:</b> <code>.modal.fade</code> &gt; <code>.modal-dialog</code> &gt; <code>.modal-content</code> &gt; <code>.modal-header</code> / <code>.modal-body</code> / <code>.modal-footer</code>.</li>
<li><b>Open:</b> a button with <code>data-bs-toggle="modal"</code> and <code>data-bs-target="#id"</code>. <b>Close:</b> any element with <code>data-bs-dismiss="modal"</code>, a click on the backdrop, or Esc.</li>
<li><b>Sizes:</b> <code>.modal-sm</code> (300 px), default (500 px), <code>.modal-lg</code> (800 px), <code>.modal-xl</code> (1140 px), <code>.modal-fullscreen</code> or <code>.modal-fullscreen-md-down</code>.</li>
<li><b>Position:</b> <code>.modal-dialog-centered</code>; long content: <code>.modal-dialog-scrollable</code>.</li>
<li><b>Static backdrop:</b> <code>data-bs-backdrop="static"</code> and <code>data-bs-keyboard="false"</code>.</li>
<li><code>tabindex="-1"</code> lets the modal take keyboard focus.</li></ul>
""", actions="document.querySelector('[data-bs-target=\"#basic\"]').click()"))

P.append(WE("w4_5", "Modal options, methods and events", page("Modal API", """
<div class="container py-3">
  <h1 class="h5">Student list</h1>
  <ul class="list-group mb-3">
    <li class="list-group-item d-flex justify-content-between">
      Ravi Patel
      <button class="btn btn-sm btn-outline-primary"
        data-bs-toggle="modal" data-bs-target="#edit"
        data-name="Ravi Patel">Edit</button></li>
    <li class="list-group-item d-flex justify-content-between">
      Priya Shah
      <button class="btn btn-sm btn-outline-primary"
        data-bs-toggle="modal" data-bs-target="#edit"
        data-name="Priya Shah">Edit</button></li>
  </ul>
  <button class="btn btn-dark btn-sm" id="openJs">
    Open with show()</button>
  <h2 class="h6 mt-3">Event log</h2>
  <ol class="small" id="log"></ol>
</div>

<div class="modal fade" id="edit" tabindex="-1">
  <div class="modal-dialog">
    <div class="modal-content">
      <div class="modal-header">
        <h5 class="modal-title">Edit</h5>
        <button class="btn-close" data-bs-dismiss="modal"></button>
      </div>
      <div class="modal-body">
        <input class="form-control" id="nameBox">
      </div>
      <div class="modal-footer">
        <button class="btn btn-primary" id="closeJs">
          Close with hide()</button>
      </div>
    </div>
  </div>
</div>
""", script="""
var el = document.getElementById("edit");
// options: backdrop, keyboard, focus
var modal = new bootstrap.Modal(el, {
  backdrop: "static", keyboard: false
});

document.getElementById("openJs").onclick = function () {
  modal.show();
};
document.getElementById("closeJs").onclick = function () {
  modal.hide();
};

function log(t) {
  var li = document.createElement("li");
  li.textContent = t;
  document.getElementById("log").appendChild(li);
}

// relatedTarget = the button that opened the modal
el.addEventListener("show.bs.modal", function (e) {
  var b = e.relatedTarget;
  var name = b ? b.getAttribute("data-name") : "New student";
  el.querySelector(".modal-title").textContent = "Edit " + name;
  document.getElementById("nameBox").value = b ? name : "";
  log("show.bs.modal");
});
el.addEventListener("shown.bs.modal", function () {
  document.getElementById("nameBox").focus();
  log("shown.bs.modal");
});
el.addEventListener("hide.bs.modal", function () {
  log("hide.bs.modal");
});
el.addEventListener("hidden.bs.modal", function () {
  log("hidden.bs.modal");
});
el.addEventListener("hidePrevented.bs.modal", function () {
  log("hidePrevented.bs.modal (static backdrop)");
});
""", bs_js=True),
"""A list with "Ravi Patel" and "Priya Shah", each with an Edit button. Clicking Edit next to Priya opens a modal titled "Edit Priya Shah", with her name already in the text box and the cursor in it.
"Open with show()" opens the same modal titled "Edit New student" with an empty box.
Clicking outside the modal does not close it; it only bounces and logs "hidePrevented.bs.modal (static backdrop)". "Close with hide()" closes it.
The event log lists show.bs.modal, shown.bs.modal, hide.bs.modal and hidden.bs.modal in order.""",
"""
<ul><li><b>Options</b> (object or data-bs-*): <code>backdrop</code> (true / false / "static"), <code>keyboard</code> (Esc closes), <code>focus</code>.</li>
<li><b>Methods:</b> <code>show()</code>, <code>hide()</code>, <code>toggle()</code>, <code>handleUpdate()</code> (re-position), <code>dispose()</code>; static <code>bootstrap.Modal.getInstance(el)</code> and <code>getOrCreateInstance(el)</code>.</li>
<li><b>Events:</b> <code>show.bs.modal</code> (before opening), <code>shown.bs.modal</code> (fully visible), <code>hide.bs.modal</code>, <code>hidden.bs.modal</code>, <code>hidePrevented.bs.modal</code> (static backdrop clicked).</li>
<li><code>e.relatedTarget</code> in show.bs.modal is the button that opened it, so one modal can serve many rows (data-name).</li>
<li>Calling <code>e.preventDefault()</code> in show.bs.modal or hide.bs.modal stops the modal from opening or closing.</li>
<li>Bootstrap 3 used jQuery: <code>$("#edit").modal("show")</code> and <code>.on("shown.bs.modal", ...)</code>.</li></ul>
""", actions="document.querySelectorAll('[data-name]')[1].click()"))

P.append(WE("w4_6", "Save and delete record confirmation modals (Practical 19)", page("Record Confirmation", """
<div class="container py-3">
  <h1 class="h5">Student records</h1>
  <form class="row g-2 mb-3" id="frm">
    <div class="col-7">
      <input class="form-control" id="name"
        placeholder="Student name" required></div>
    <div class="col-3">
      <input class="form-control" id="sem" type="number"
        min="1" max="6" placeholder="Sem" required></div>
    <div class="col-2 d-grid">
      <button class="btn btn-primary" type="submit">Save</button>
    </div>
  </form>
  <div id="msg"></div>
  <table class="table table-bordered table-sm">
    <thead class="table-light">
      <tr><th>Name</th><th>Sem</th><th></th></tr></thead>
    <tbody id="rows">
      <tr><td>Ravi Patel</td><td>3</td><td></td></tr>
      <tr><td>Priya Shah</td><td>5</td><td></td></tr>
    </tbody>
  </table>
</div>

<div class="modal fade" id="saveModal" tabindex="-1">
  <div class="modal-dialog modal-dialog-centered">
    <div class="modal-content">
      <div class="modal-header bg-primary text-white">
        <h5 class="modal-title">
          <i class="bi bi-save"></i> Save record?</h5>
        <button class="btn-close btn-close-white"
          data-bs-dismiss="modal"></button>
      </div>
      <div class="modal-body" id="saveText"></div>
      <div class="modal-footer">
        <button class="btn btn-secondary"
          data-bs-dismiss="modal">Cancel</button>
        <button class="btn btn-primary" id="yesSave">Yes, save</button>
      </div>
    </div>
  </div>
</div>

<div class="modal fade" id="delModal" tabindex="-1">
  <div class="modal-dialog modal-dialog-centered modal-sm">
    <div class="modal-content">
      <div class="modal-body text-center">
        <i class="bi bi-exclamation-triangle
          text-danger fs-1"></i>
        <h5>Delete record?</h5>
        <p id="delText"></p>
        <button class="btn btn-secondary"
          data-bs-dismiss="modal">No</button>
        <button class="btn btn-danger" id="yesDel">Delete</button>
      </div>
    </div>
  </div>
</div>
""", script="""
var saveM = new bootstrap.Modal("#saveModal");
var delM = new bootstrap.Modal("#delModal");
var rows = document.getElementById("rows");
var delRow = null;

function addDeleteButton(tr) {
  tr.cells[2].innerHTML = '<button class="btn btn-sm ' +
    'btn-outline-danger"><i class="bi bi-trash"></i></button>';
  tr.cells[2].firstChild.onclick = function () {
    delRow = tr;
    document.getElementById("delText").textContent =
      tr.cells[0].textContent + " will be removed.";
    delM.show();
  };
}
Array.from(rows.rows).forEach(addDeleteButton);

function show(text, type) {
  document.getElementById("msg").innerHTML =
    '<div class="alert alert-' + type + ' py-2">' +
    text + "</div>";
}

document.getElementById("frm").onsubmit = function (e) {
  e.preventDefault();
  document.getElementById("saveText").textContent =
    "Save " + name.value + " (Sem " + sem.value + ")?";
  saveM.show();
};
document.getElementById("yesSave").onclick = function () {
  var tr = rows.insertRow();
  tr.insertCell().textContent = name.value;
  tr.insertCell().textContent = sem.value;
  tr.insertCell();
  addDeleteButton(tr);
  show("Record of " + name.value + " saved.", "success");
  document.getElementById("frm").reset();
  saveM.hide();
};
document.getElementById("yesDel").onclick = function () {
  show(delRow.cells[0].textContent + " deleted.", "danger");
  delRow.remove();
  delM.hide();
};
""", icons=True, bs_js=True),
"""A form (Student name, Sem, Save) above a table with Ravi Patel (3) and Priya Shah (5); each row has a red trash button.
After filling in "Amit Desai" and 4 and clicking Save, a centred blue modal "Save record?" asks "Save Amit Desai (Sem 4)?". "Yes, save" adds the row, closes the modal and shows a green message "Record of Amit Desai saved."
Clicking a trash button opens a small modal with a warning icon: "Delete record? Priya Shah will be removed." Delete removes the row and shows a red message "Priya Shah deleted."; No just closes it.""",
"""
<ul><li>Two modals: a <b>save confirmation</b> (blue header, Cancel / Yes) and a <b>delete confirmation</b> (small, warning icon, No / Delete).</li>
<li>The form's <code>submit</code> event is stopped with <code>e.preventDefault()</code>; the browser first checks the <code>required</code> fields, then the save modal opens.</li>
<li><code>new bootstrap.Modal("#saveModal")</code> creates the modal object; <code>show()</code> and <code>hide()</code> are called after the user's choice.</li>
<li><code>delRow</code> remembers which row's trash button was clicked, so the same delete modal works for every row.</li>
<li><code>insertRow()</code>, <code>insertCell()</code> and <code>remove()</code> change the table; the result is shown in a Bootstrap alert.</li>
<li><code>name</code> and <code>sem</code> are used directly because elements with an id are available as global variables (writing <code>document.getElementById</code> is safer in big projects).</li></ul>
""", actions="document.querySelector('#rows .btn').click()"))

P.append(WE("w4_7", "Scrollspy: highlight the menu while scrolling", page("Scrollspy", """
<div class="container py-3">
  <h1 class="h5">RWPD units</h1>
  <nav id="unitNav" class="navbar bg-body-tertiary px-2 mb-2">
    <ul class="nav nav-pills small">
      <li class="nav-item">
        <a class="nav-link" href="#u1">jQuery</a></li>
      <li class="nav-item">
        <a class="nav-link" href="#u2">Grid</a></li>
      <li class="nav-item">
        <a class="nav-link" href="#u3">Components</a></li>
      <li class="nav-item">
        <a class="nav-link" href="#u4">Plug-ins</a></li>
    </ul>
  </nav>

  <div class="spy border rounded p-3" data-bs-spy="scroll"
    data-bs-target="#unitNav" data-bs-smooth-scroll="true"
    tabindex="0">
    <h4 id="u1">Unit 1: jQuery</h4>
    <p>Selectors, events, effects and DOM changes...</p>
    <h4 id="u2">Unit 2: Bootstrap grid</h4>
    <p>Containers, rows, columns, offset and nesting...</p>
    <h4 id="u3">Unit 3: Components</h4>
    <p>Navbar, cards, alerts, badges, list groups...</p>
    <h4 id="u4">Unit 4: Plug-ins</h4>
    <p>Modal, scrollspy, tooltip, collapse, carousel...</p>
  </div>
  <p class="small mt-2">Now reading: <b id="now">-</b></p>
</div>
""", style="""
.spy { height: 220px; overflow-y: auto; position: relative; }
.spy p { min-height: 180px; }
""", script="""
var spy = document.querySelector(".spy");
spy.addEventListener("activate.bs.scrollspy", function (e) {
  document.getElementById("now").textContent =
    e.relatedTarget.textContent;
});
""", bs_js=True),
"""A grey bar with the pills jQuery, Grid, Components and Plug-ins above a scrollable box containing the four unit sections.
At first "jQuery" is highlighted. As the box is scrolled, the highlighted pill changes automatically to Grid, then Components, then Plug-ins, and "Now reading:" shows the same name.
Clicking a pill scrolls smoothly to that section.""",
"""
<ul><li><b>Scrollspy</b> automatically updates the active link of a nav or list group according to the section that is visible while scrolling.</li>
<li>Add <code>data-bs-spy="scroll"</code> and <code>data-bs-target="#navId"</code> to the <b>scrolling element</b> (here the box; it can also be the body).</li>
<li>Each link's <code>href</code> must match a section <code>id</code> (#u1 ... #u4), and the target must be a visible .nav, .navbar or .list-group.</li>
<li>The scroll container needs a fixed <b>height</b> with <code>overflow-y: auto</code>, plus <code>tabindex="0"</code> for keyboard access.</li>
<li><b>Options:</b> <code>smoothScroll</code>, <code>rootMargin</code>, <code>threshold</code> (Bootstrap 3 used <code>offset</code>). <b>Method:</b> <code>refresh()</code> after adding sections. <b>Event:</b> <code>activate.bs.scrollspy</code> with <code>e.relatedTarget</code> = the newly active link.</li></ul>
""", actions="var s=document.querySelector('.spy');s.scrollTop=document.getElementById('u3').offsetTop-10"))

P.append(WE("w4_8", "Tab plug-in: list group tabs with methods and events", page("Tab Plug-in", """
<div class="container py-3">
  <h1 class="h5">Course details</h1>
  <div class="row g-3">
    <div class="col-sm-4">
      <div class="list-group" id="tabs" role="tablist">
        <a class="list-group-item list-group-item-action active"
          data-bs-toggle="list" href="#t1">Overview</a>
        <a class="list-group-item list-group-item-action"
          data-bs-toggle="list" href="#t2">Syllabus</a>
        <a class="list-group-item list-group-item-action"
          data-bs-toggle="list" href="#t3">Fees</a>
      </div>
    </div>
    <div class="col-sm-8">
      <div class="tab-content border rounded p-3">
        <div class="tab-pane fade show active" id="t1">
          3-year diploma in Computer Engineering.</div>
        <div class="tab-pane fade" id="t2">
          6 semesters, about 40 subjects.</div>
        <div class="tab-pane fade" id="t3">
          Rs. 15,000 per year.</div>
      </div>
      <button class="btn btn-sm btn-outline-dark mt-2"
        id="prev">&laquo; Previous</button>
      <button class="btn btn-sm btn-dark mt-2"
        id="next">Next &raquo;</button>
      <p class="small mt-2" id="log"></p>
    </div>
  </div>
</div>
""", script="""
var links = Array.from(document.querySelectorAll("#tabs a"));

function current() {
  return links.findIndex(function (a) {
    return a.classList.contains("active");
  });
}
function go(step) {
  var i = (current() + step + links.length) % links.length;
  bootstrap.Tab.getOrCreateInstance(links[i]).show();
}
var nextBtn = document.getElementById("next");
var prevBtn = document.getElementById("prev");
nextBtn.onclick = function () { go(1); };
prevBtn.onclick = function () { go(-1); };

links.forEach(function (a) {
  a.addEventListener("shown.bs.tab", function (e) {
    document.getElementById("log").textContent =
      "shown.bs.tab: " + e.target.textContent +
      " (previous: " + e.relatedTarget.textContent + ")";
  });
});
""", bs_js=True),
"""A vertical list (Overview, Syllabus, Fees) beside a content box; on a phone the list is above the box. Overview is active, showing "3-year diploma in Computer Engineering."
Clicking Syllabus or Fees fades in that content. "Next »" and "« Previous" move through the tabs in a loop.
After each change the text shows, e.g., "shown.bs.tab: Syllabus (previous: Overview)".""",
"""
<ul><li>The <b>tab plug-in</b> works with .nav-tabs, .nav-pills and also <b>list groups</b>: <code>data-bs-toggle="list"</code> (or "tab" / "pill").</li>
<li>Each link points to a <code>.tab-pane</code> by href or <code>data-bs-target</code>; panes are inside <code>.tab-content</code>.</li>
<li><b>Method:</b> <code>bootstrap.Tab.getOrCreateInstance(link).show()</code> activates a tab from code (also <code>dispose()</code>).</li>
<li><b>Events</b> (in order): <code>hide.bs.tab</code> on the old tab, <code>show.bs.tab</code> on the new tab, <code>hidden.bs.tab</code>, <code>shown.bs.tab</code>. <code>e.relatedTarget</code> is the previous (or next) tab.</li>
<li>The modulo <code>%</code> makes Next go from the last tab back to the first.</li></ul>
""", actions="document.getElementById('next').click()"))

P.append(WE("w4_9", "Dropdown plug-in: auto-close options, methods and events", page("Dropdown Plug-in", """
<div class="container py-3">
  <h1 class="h5">Dropdown plug-in</h1>
  <div class="d-flex flex-wrap gap-2 mb-3">
    <div class="dropdown">
      <button class="btn btn-primary dropdown-toggle" id="dd1"
        data-bs-toggle="dropdown">Default</button>
      <ul class="dropdown-menu">
        <li><a class="dropdown-item" href="#">Computer</a></li>
        <li><a class="dropdown-item" href="#">IT</a></li>
      </ul>
    </div>
    <div class="dropdown">
      <button class="btn btn-success dropdown-toggle"
        data-bs-toggle="dropdown"
        data-bs-auto-close="outside">Outside only</button>
      <div class="dropdown-menu p-3">
        <div class="form-check">
          <input class="form-check-input" type="checkbox" id="c1">
          <label class="form-check-label" for="c1">Hostel</label>
        </div>
        <div class="form-check">
          <input class="form-check-input" type="checkbox" id="c2">
          <label class="form-check-label" for="c2">Bus</label>
        </div>
      </div>
    </div>
    <div class="dropdown">
      <button class="btn btn-warning dropdown-toggle"
        data-bs-toggle="dropdown" data-bs-offset="0,12"
        data-bs-auto-close="false">Manual close</button>
      <ul class="dropdown-menu">
        <li><span class="dropdown-item-text">Closes only
          on button click</span></li>
      </ul>
    </div>
  </div>
  <button class="btn btn-dark btn-sm" id="tog">
    toggle() first dropdown</button>
  <ol class="small mt-3" id="log"></ol>
</div>
""", script="""
var dd1 = bootstrap.Dropdown.getOrCreateInstance("#dd1");
document.getElementById("tog").onclick = function (e) {
  e.stopPropagation();  // this click must not close it again
  dd1.toggle();
};

["show", "shown", "hide", "hidden"].forEach(function (ev) {
  document.addEventListener(ev + ".bs.dropdown", function (e) {
    var li = document.createElement("li");
    li.textContent = ev + ".bs.dropdown: " +
      e.target.textContent.trim();
    document.getElementById("log").appendChild(li);
  });
});
""", bs_js=True),
"""Three dropdown buttons. "Default" opens a menu (Computer, IT) that closes on any click.
"Outside only" opens a small form with Hostel and Bus checkboxes; ticking them keeps the menu open, and it closes only when clicking outside.
"Manual close" opens a menu 12 px lower that closes only when its own button is clicked again.
"toggle() first dropdown" opens and closes the Default menu from code. The log lists events such as "show.bs.dropdown: Default" and "hidden.bs.dropdown: Default".""",
"""
<ul><li>The <b>dropdown plug-in</b> opens a .dropdown-menu when the toggle with <code>data-bs-toggle="dropdown"</code> is clicked. It uses <b>Popper</b> for positioning, so the bundle file is needed.</li>
<li><b>Options:</b> <code>autoClose</code> = true (any click), "inside", "outside" or false; <code>offset</code> = "x,y" distance; <code>display</code> = "static" (no Popper); <code>boundary</code>, <code>reference</code>.</li>
<li><b>Methods:</b> <code>toggle()</code>, <code>show()</code>, <code>hide()</code>, <code>update()</code>, <code>dispose()</code>.</li>
<li><b>Events:</b> <code>show.bs.dropdown</code>, <code>shown.bs.dropdown</code>, <code>hide.bs.dropdown</code>, <code>hidden.bs.dropdown</code>; they fire on the toggle button.</li>
<li><code>e.stopPropagation()</code> stops the outside-click handler from closing the menu immediately after toggle().</li>
<li>Keyboard: arrow keys move through items, Esc closes the menu.</li></ul>
""", actions="document.getElementById('tog').click()"))

# ------------------------------------------------------------------ 4.2
P.append(WE("w4_10", "Tooltip plug-in: placements, HTML, methods and events", page("Tooltips", """
<div class="container py-3">
  <h1 class="h5">Tooltips</h1>
  <div class="d-flex flex-wrap gap-2 mb-3">
    <button class="btn btn-secondary" data-bs-toggle="tooltip"
      data-bs-placement="top" title="Tooltip on top">Top</button>
    <button class="btn btn-secondary" data-bs-toggle="tooltip"
      data-bs-placement="right" title="Right side">Right</button>
    <button class="btn btn-secondary" data-bs-toggle="tooltip"
      data-bs-placement="bottom" title="Below">Bottom</button>
    <button class="btn btn-secondary" data-bs-toggle="tooltip"
      data-bs-placement="left" title="On the left">Left</button>
  </div>
  <p>Read about
    <a href="#" data-bs-toggle="tooltip" data-bs-html="true"
      title="<b>HTML</b>: <i>HyperText</i> Markup">HTML</a>
    and
    <i class="bi bi-info-circle text-primary"
      data-bs-toggle="tooltip" title="Icon tooltip"></i>
    icons.</p>
  <span class="d-inline-block" tabindex="0"
    data-bs-toggle="tooltip" title="Form is closed">
    <button class="btn btn-primary" disabled>Apply</button>
  </span>

  <h2 class="h6 mt-3">Methods on the "Target" button</h2>
  <button class="btn btn-success" id="target" title="I am the target"
    data-bs-trigger="manual">Target</button>
  <div class="btn-group btn-group-sm ms-2">
    <button class="btn btn-outline-dark" id="s">show</button>
    <button class="btn btn-outline-dark" id="h">hide</button>
    <button class="btn btn-outline-dark" id="t">toggle</button>
  </div>
  <p class="small mt-2" id="log"></p>
</div>
""", script="""
// tooltips are opt-in: create them yourself
var sel = '[data-bs-toggle="tooltip"]';
document.querySelectorAll(sel).forEach(function (el) {
  new bootstrap.Tooltip(el);
});

var target = document.getElementById("target");
var tip = new bootstrap.Tooltip(target, {
  placement: "bottom"
});
function $(id) { return document.getElementById(id); }
$("s").onclick = function () { tip.show(); };
$("h").onclick = function () { tip.hide(); };
$("t").onclick = function () {
  tip.toggle();
};

["shown", "hidden"].forEach(function (ev) {
  target.addEventListener(ev + ".bs.tooltip", function () {
    document.getElementById("log").textContent =
      "Event: " + ev + ".bs.tooltip";
  });
});
""", icons=True, bs_js=True),
"""Four grey buttons (Top, Right, Bottom, Left). Hovering (or tapping on a phone) shows a small black tooltip on that side.
The link "HTML" shows a tooltip with bold and italic text; the info icon also has a tooltip; the disabled "Apply" button shows "Form is closed" through its wrapper.
The show, hide and toggle buttons control the tooltip below the green "Target" button, and the text shows "Event: shown.bs.tooltip" or "Event: hidden.bs.tooltip".""",
"""
<ul><li>A <b>tooltip</b> is a small pop-up label shown on hover or focus. Text comes from the <code>title</code> attribute (or <code>data-bs-title</code>).</li>
<li>For performance, tooltips are <b>opt-in</b>: they must be initialised with JavaScript, <code>new bootstrap.Tooltip(el)</code>. They use Popper (bundle file).</li>
<li><b>Options:</b> <code>placement</code> (top, right, bottom, left, auto), <code>trigger</code> ("hover focus", "click", "manual"), <code>html</code>, <code>delay</code>, <code>animation</code>, <code>offset</code>, <code>container</code>.</li>
<li><b>Methods:</b> show(), hide(), toggle(), enable(), disable(), toggleEnabled(), setContent(), update(), dispose().</li>
<li><b>Events:</b> show.bs.tooltip, shown.bs.tooltip, hide.bs.tooltip, hidden.bs.tooltip, inserted.bs.tooltip.</li>
<li>Disabled elements do not fire mouse events, so the tooltip is put on a wrapper span with <code>tabindex="0"</code>.</li></ul>
""", actions="document.getElementById('s').click()"))

P.append(WE("w4_11", "Popover plug-in: title, content, dismiss on next click", page("Popovers", """
<div class="container py-3">
  <h1 class="h5">Popovers</h1>
  <div class="d-flex flex-wrap gap-2 mb-3">
    <button class="btn btn-danger" data-bs-toggle="popover"
      data-bs-title="Last date" data-bs-placement="bottom"
      data-bs-content="Fees must be paid by 30 Nov.">
      Click me</button>
    <button class="btn btn-info" data-bs-toggle="popover"
      data-bs-placement="right" data-bs-trigger="hover focus"
      data-bs-content="Opens on hover and closes on leave.">
      Hover me</button>
    <a tabindex="0" class="btn btn-warning" role="button"
      data-bs-toggle="popover" data-bs-trigger="focus"
      data-bs-title="Dismissible"
      data-bs-content="Click anywhere else to close.">
      Dismiss on next click</a>
  </div>
  <button class="btn btn-outline-primary" id="prof">
    Profile card (HTML)</button>
  <p class="small mt-3" id="log"></p>
</div>
""", script="""
document.querySelectorAll('[data-bs-toggle="popover"]')
  .forEach(function (el) { new bootstrap.Popover(el); });

// options given in JavaScript, with HTML content
var prof = document.getElementById("prof");
var pop = new bootstrap.Popover(prof, {
  html: true,
  placement: "bottom",
  title: "Ravi Patel",
  content: "<b>Sem 3</b>, Computer<br>Enrolment: 2401001"
});
prof.addEventListener("shown.bs.popover", function () {
  document.getElementById("log").textContent =
    "shown.bs.popover fired";
});
""", bs_js=True),
"""A red "Click me" button opens a box below it with the heading "Last date" and the text "Fees must be paid by 30 Nov."; clicking again closes it.
"Hover me" shows its popover only while the mouse is over it. The yellow "Dismiss on next click" popover closes when the user clicks anywhere else.
"Profile card (HTML)" opens a popover titled "Ravi Patel" with bold "Sem 3", "Computer" and the enrolment number on a new line, and the text "shown.bs.popover fired" appears.""",
"""
<ul><li>A <b>popover</b> is like a larger tooltip with a <b>title</b> and <b>content</b>, shown on click by default.</li>
<li>Attributes: <code>data-bs-toggle="popover"</code>, <code>data-bs-title</code>, <code>data-bs-content</code>, <code>data-bs-placement</code>, <code>data-bs-trigger</code>.</li>
<li>Popovers are also <b>opt-in</b>: initialise each with <code>new bootstrap.Popover(el, options)</code>. Popover depends on the tooltip plug-in and Popper.</li>
<li><b>Dismiss on next click:</b> <code>trigger: "focus"</code> on an &lt;a&gt; with <code>tabindex="0"</code>.</li>
<li><b>Options:</b> html, placement, trigger, title, content, delay, offset, container. <b>Methods:</b> show(), hide(), toggle(), enable(), disable(), setContent(), dispose().</li>
<li><b>Events:</b> show.bs.popover, shown.bs.popover, hide.bs.popover, hidden.bs.popover, inserted.bs.popover.</li></ul>
""", actions="document.querySelector('.btn-danger').click();document.getElementById('prof').click()"))

P.append(WE("w4_12", "Button plug-in and alert plug-in", page("Button and Alert", """
<div class="container py-3">
  <h1 class="h5">Button plug-in</h1>
  <button class="btn btn-outline-primary" id="like"
    data-bs-toggle="button">
    <i class="bi bi-hand-thumbs-up"></i> Like</button>
  <button class="btn btn-dark btn-sm" id="jsTog">toggle() Like</button>
  <span class="small ms-2" id="state">Not pressed</span>

  <h2 class="h6 mt-3">Checkbox and radio buttons</h2>
  <div class="btn-group mb-2">
    <input type="checkbox" class="btn-check" id="b1" checked>
    <label class="btn btn-outline-success" for="b1">Hostel</label>
    <input type="checkbox" class="btn-check" id="b2">
    <label class="btn btn-outline-success" for="b2">Bus</label>
  </div>
  <div class="btn-group mb-2">
    <input type="radio" class="btn-check" name="sh" id="r1" checked>
    <label class="btn btn-outline-danger" for="r1">Morning</label>
    <input type="radio" class="btn-check" name="sh" id="r2">
    <label class="btn btn-outline-danger" for="r2">Noon</label>
  </div>

  <h2 class="h6 mt-2">Loading state</h2>
  <button class="btn btn-primary" id="load">Submit</button>

  <h1 class="h5 mt-4">Alert plug-in</h1>
  <div class="alert alert-warning fade show" id="note">
    Holiday on Monday for Diwali.</div>
  <button class="btn btn-warning btn-sm" id="closeNote">
    Close alert with close()</button>
  <p class="small mt-2" id="log"></p>
</div>
""", script="""
var like = document.getElementById("like");
var b = bootstrap.Button.getOrCreateInstance(like);
function showState() {
  document.getElementById("state").textContent =
    like.classList.contains("active") ?
    "Pressed" : "Not pressed";
}
like.addEventListener("click", showState);
document.getElementById("jsTog").onclick = function () {
  b.toggle();
  showState();
};

// loading state (Bootstrap 3: data-loading-text)
document.getElementById("load").onclick = function () {
  var btn = this;
  btn.disabled = true;
  btn.innerHTML = '<span class="spinner-border ' +
    'spinner-border-sm"></span> Saving...';
  setTimeout(function () {
    btn.disabled = false;
    btn.textContent = "Submit";
  }, 2000);
};

var note = document.getElementById("note");
document.getElementById("closeNote").onclick = function () {
  bootstrap.Alert.getOrCreateInstance(note).close();
};
note.addEventListener("close.bs.alert", function () {
  document.getElementById("log").textContent = "close.bs.alert";
});
note.addEventListener("closed.bs.alert", function () {
  document.getElementById("log").textContent +=
    " -> closed.bs.alert (removed from page)";
});
""", icons=True, bs_js=True),
"""An outlined "Like" button turns solid blue when clicked and the text changes to "Pressed"; "toggle() Like" does the same from code.
"Hostel" and "Bus" can both be selected (checkboxes), while only one of "Morning" or "Noon" stays selected (radio).
"Submit" shows a spinner with "Saving..." and is disabled for 2 seconds.
"Close alert with close()" fades out the yellow Diwali alert and the log shows "close.bs.alert -> closed.bs.alert (removed from page)".""",
"""
<ul><li><b>Button plug-in:</b> <code>data-bs-toggle="button"</code> makes a toggle button; clicking adds/removes <code>.active</code> and sets <code>aria-pressed</code>. Method: <code>bootstrap.Button.getOrCreateInstance(el).toggle()</code>.</li>
<li><b>Checkbox / radio buttons:</b> Bootstrap 5 uses <code>input.btn-check</code> + <code>label.btn</code> (Bootstrap 3 used data-toggle="buttons").</li>
<li><b>Loading state:</b> Bootstrap 3 had <code>$(btn).button("loading")</code> with data-loading-text. In Bootstrap 5, disable the button and show a <code>.spinner-border-sm</code> with JavaScript.</li>
<li><b>Alert plug-in:</b> makes alerts dismissible. Method <code>close()</code>; events <code>close.bs.alert</code> (closing starts) and <code>closed.bs.alert</code> (alert removed).</li></ul>
""", actions="document.getElementById('jsTog').click();document.getElementById('closeNote').click()"))

P.append(WE("w4_13", "Collapse plug-in: properties, methods and events", page("Collapse", """
<div class="container py-3">
  <h1 class="h5">Collapse</h1>
  <a class="btn btn-primary" data-bs-toggle="collapse"
    href="#info">Link with href</a>
  <button class="btn btn-primary" data-bs-toggle="collapse"
    data-bs-target="#info">Button with data-bs-target</button>
  <div class="collapse mt-2" id="info">
    <div class="card card-body">Admission opens on 1 June.</div>
  </div>

  <h2 class="h6 mt-3">One button, multiple targets</h2>
  <button class="btn btn-success" data-bs-toggle="collapse"
    data-bs-target=".multi">Toggle both</button>
  <div class="row g-2 mt-1">
    <div class="col-6"><div class="collapse multi show">
      <div class="card card-body">Box A</div></div></div>
    <div class="col-6"><div class="collapse multi show">
      <div class="card card-body">Box B</div></div></div>
  </div>

  <h2 class="h6 mt-3">Horizontal</h2>
  <button class="btn btn-warning" data-bs-toggle="collapse"
    data-bs-target="#side">Width animation</button>
  <div class="collapse collapse-horizontal mt-2" id="side">
    <div class="card card-body" style="width: 220px">
      Slides open sideways.</div>
  </div>

  <h2 class="h6 mt-3">Methods</h2>
  <div class="btn-group btn-group-sm">
    <button class="btn btn-outline-dark" id="m1">show()</button>
    <button class="btn btn-outline-dark" id="m2">hide()</button>
    <button class="btn btn-outline-dark" id="m3">toggle()</button>
  </div>
  <ol class="small mt-2" id="log"></ol>
</div>
""", script="""
var info = document.getElementById("info");
var c = bootstrap.Collapse.getOrCreateInstance(info, {
  toggle: false
});
function $(id) { return document.getElementById(id); }
$("m1").onclick = function () { c.show(); };
$("m2").onclick = function () { c.hide(); };
$("m3").onclick = function () {
  c.toggle();
};

["show", "shown", "hide", "hidden"].forEach(function (ev) {
  info.addEventListener(ev + ".bs.collapse", function () {
    var li = document.createElement("li");
    li.textContent = ev + ".bs.collapse";
    document.getElementById("log").appendChild(li);
  });
});
""", bs_js=True),
""""Link with href" and "Button with data-bs-target" both open and close the same box "Admission opens on 1 June." with a smooth height animation.
"Toggle both" hides or shows Box A and Box B together. "Width animation" slides a box open sideways.
show(), hide() and toggle() control the first box from code, and the log lists show.bs.collapse, shown.bs.collapse, hide.bs.collapse and hidden.bs.collapse.""",
"""
<ul><li><b>Collapse</b> shows and hides content with a height animation. The content gets <code>.collapse</code> (hidden), <code>.collapsing</code> (during animation) and <code>.collapse.show</code> (visible).</li>
<li><b>Trigger:</b> an &lt;a&gt; with <code>href="#id"</code> or a button with <code>data-bs-target="#id"</code>, plus <code>data-bs-toggle="collapse"</code>. A class selector (<code>.multi</code>) controls <b>multiple targets</b>.</li>
<li><code>.collapse-horizontal</code> animates the width instead of the height (the child needs a width).</li>
<li><b>Properties (options):</b> <code>parent</code> (selector; only one child of the parent stays open, used for accordions) and <code>toggle</code> (toggle on creation, default true).</li>
<li><b>Methods:</b> show(), hide(), toggle(), dispose(), getInstance(), getOrCreateInstance().</li>
<li><b>Events:</b> show.bs.collapse, shown.bs.collapse, hide.bs.collapse, hidden.bs.collapse.</li></ul>
""", actions="document.getElementById('m1').click()"))

P.append(WE("w4_14", "Accordion (collapse with data-bs-parent): FAQ", page("Accordion", """
<div class="container py-3">
  <h1 class="h5">Admission FAQ</h1>
  <div class="accordion" id="faq">
    <div class="accordion-item">
      <h2 class="accordion-header">
        <button class="accordion-button" data-bs-toggle="collapse"
          data-bs-target="#q1">Who can apply?</button></h2>
      <div id="q1" class="accordion-collapse collapse show"
        data-bs-parent="#faq">
        <div class="accordion-body">
          Students who passed SSC (Class 10).</div>
      </div>
    </div>
    <div class="accordion-item">
      <h2 class="accordion-header">
        <button class="accordion-button collapsed"
          data-bs-toggle="collapse" data-bs-target="#q2">
          How is merit decided?</button></h2>
      <div id="q2" class="accordion-collapse collapse"
        data-bs-parent="#faq">
        <div class="accordion-body">
          By SSC marks through ACPDC online admission.</div>
      </div>
    </div>
    <div class="accordion-item">
      <h2 class="accordion-header">
        <button class="accordion-button collapsed"
          data-bs-toggle="collapse" data-bs-target="#q3">
          What is the course duration?</button></h2>
      <div id="q3" class="accordion-collapse collapse"
        data-bs-parent="#faq">
        <div class="accordion-body">
          3 years (6 semesters).</div>
      </div>
    </div>
  </div>
</div>
""", bs_js=True),
"""Three questions in bordered rows. The first answer, "Students who passed SSC (Class 10).", is open with a blue header.
Clicking another question opens its answer with an animation and automatically closes the open one, so only one answer is visible at a time. The arrow on the right rotates when a row opens.""",
"""
<ul><li>An <b>accordion</b> is a group of collapse panels where only one is open at a time.</li>
<li>Structure: <code>.accordion</code> &gt; <code>.accordion-item</code> &gt; <code>.accordion-header</code> (with <code>button.accordion-button</code>) + <code>.accordion-collapse.collapse</code> &gt; <code>.accordion-body</code>.</li>
<li><code>data-bs-parent="#faq"</code> is the collapse <b>parent option</b>: opening one panel closes the others. Remove it to allow several open panels.</li>
<li><code>.collapsed</code> on a button shows the closed arrow; <code>.show</code> on the first panel opens it at the start.</li>
<li><code>.accordion-flush</code> removes borders and rounded corners. (Bootstrap 3 built accordions from panels: .panel-group.)</li></ul>
""", actions="document.querySelector('[data-bs-target=\"#q2\"]').click()"))

P.append(WE("w4_15", "News story page: scrollspy, tooltip, collapse and popover (Practical 20)", page("News Story", """
<div class="container py-2">
  <h1 class="h4 mb-1">Surat Gets New Metro Line</h1>
  <p class="small text-muted mb-2">By
    <a href="#" id="reporter" data-bs-toggle="popover"
      data-bs-trigger="focus" data-bs-title="Neha Joshi"
      data-bs-content="City reporter, 8 years at the desk.">
      Neha Joshi</a> | 28 Oct 2026</p>

  <nav id="newsNav" class="mb-2">
    <ul class="nav nav-pills nav-fill small">
      <li class="nav-item">
        <a class="nav-link" href="#s1">Story</a></li>
      <li class="nav-item">
        <a class="nav-link" href="#s2">Photos</a></li>
      <li class="nav-item">
        <a class="nav-link" href="#s3">Route</a></li>
      <li class="nav-item">
        <a class="nav-link" href="#s4">Opinion</a></li>
    </ul>
  </nav>

  <div class="news border rounded p-3" data-bs-spy="scroll"
    data-bs-target="#newsNav" tabindex="0">
    <section id="s1">
      <h2 class="h5">The story</h2>
      <p>The first phase of the metro was opened today. Trains
        will run every 10 minutes from 6 am to 10 pm.</p>
      <button class="btn btn-sm btn-outline-primary"
        data-bs-toggle="collapse" data-bs-target="#more">
        Read more</button>
      <div class="collapse" id="more">
        <p class="mt-2">The line has 14 stations and connects
          the railway station with the diamond market.</p>
      </div>
    </section>
    <section id="s2">
      <h2 class="h5">Photos</h2>
      <div class="row g-2">
        <div class="col-6">
          <img src="img/train.jpg" alt="Train" class="img-fluid
            rounded" data-bs-toggle="tooltip"
            title="New metro train at the depot"></div>
        <div class="col-6">
          <img src="img/station.jpg" alt="Station" class="img-fluid
            rounded" data-bs-toggle="tooltip"
            title="Platform of Chowk Bazar station"></div>
      </div>
    </section>
    <section id="s3">
      <h2 class="h5">Route</h2>
      <p>Sarthana to Dream City, 21.6 km, with a
        <abbr data-bs-toggle="tooltip" title="Inter-change">
          interchange</abbr> at Majura Gate.</p>
    </section>
    <section id="s4">
      <h2 class="h5">Opinion</h2>
      <p>Daily travellers say the metro will save
        30 minutes a day.</p>
      <button class="btn btn-sm btn-warning" data-bs-toggle="popover"
        data-bs-placement="top"
        data-bs-content="Fare: Rs. 10 to 40.">
        Ticket fare</button>
    </section>
  </div>
</div>
""", style="""
.news { height: 330px; overflow-y: auto; position: relative; }
.news section { min-height: 300px; }
""", script="""
document.querySelectorAll('[data-bs-toggle="tooltip"]')
  .forEach(function (el) { new bootstrap.Tooltip(el); });
document.querySelectorAll('[data-bs-toggle="popover"]')
  .forEach(function (el) { new bootstrap.Popover(el); });
""", bs_js=True),
"""A news page with the heading "Surat Gets New Metro Line", the reporter's name and date, and the pills Story, Photos, Route and Opinion.
The story box scrolls, and the active pill changes automatically (scrollspy). "Read more" expands extra text (collapse).
Pointing at either photo shows a tooltip such as "New metro train at the depot". Clicking the reporter's name shows a popover about her, which closes on the next click. "Ticket fare" opens a popover "Fare: Rs. 10 to 40.".""",
"""
<ul><li><b>Scrollspy:</b> the scroll box has <code>data-bs-spy="scroll"</code> and <code>data-bs-target="#newsNav"</code>; each pill's href matches a section id.</li>
<li><b>Tooltip:</b> photos and the abbreviation have <code>data-bs-toggle="tooltip"</code> and a <code>title</code>; all are initialised with <code>new bootstrap.Tooltip(el)</code>.</li>
<li><b>Collapse:</b> "Read more" toggles the hidden paragraph <code>#more</code>.</li>
<li><b>Popover:</b> the reporter link uses <code>data-bs-trigger="focus"</code> (closes on the next click); "Ticket fare" uses the default click trigger.</li>
<li>Tooltips and popovers must be initialised by JavaScript; scrollspy and collapse work with data attributes alone.</li>
<li>The images are placeholders; use your own photos in an <code>img</code> folder.</li></ul>
""", actions="var t=document.querySelector('#s2 img');bootstrap.Tooltip.getInstance(t).show();var n=document.querySelector('.news');n.scrollTop=document.getElementById('s2').offsetTop-10"))

P.append(WE("w4_16", "Carousel plug-in: indicators, controls, captions, options", page("Carousel", """
<div class="container py-3">
  <h1 class="h5">College events</h1>
  <div id="events" class="carousel slide" data-bs-ride="carousel"
    data-bs-interval="3000">
    <div class="carousel-indicators">
      <button data-bs-target="#events" data-bs-slide-to="0"
        class="active"></button>
      <button data-bs-target="#events" data-bs-slide-to="1"></button>
      <button data-bs-target="#events" data-bs-slide-to="2"></button>
    </div>
    <div class="carousel-inner rounded">
      <div class="carousel-item active">
        <img src="img/annual-day.jpg" class="d-block w-100"
          alt="Annual Day" width="1200" height="400">
        <div class="carousel-caption d-none d-md-block">
          <h5>Annual Day</h5><p>Dance and drama night.</p></div>
      </div>
      <div class="carousel-item">
        <img src="img/sports.jpg" class="d-block w-100"
          alt="Sports" width="1200" height="400">
        <div class="carousel-caption d-none d-md-block">
          <h5>Sports Week</h5><p>Cricket and kabaddi.</p></div>
      </div>
      <div class="carousel-item">
        <img src="img/tech-fest.jpg" class="d-block w-100"
          alt="Tech Fest" width="1200" height="400">
        <div class="carousel-caption d-none d-md-block">
          <h5>Tech Fest</h5><p>Project exhibition.</p></div>
      </div>
    </div>
    <button class="carousel-control-prev" data-bs-target="#events"
      data-bs-slide="prev">
      <span class="carousel-control-prev-icon"></span>
    </button>
    <button class="carousel-control-next" data-bs-target="#events"
      data-bs-slide="next">
      <span class="carousel-control-next-icon"></span>
    </button>
  </div>
</div>
""", style="""
.carousel-item img { height: 260px; object-fit: cover; }
.carousel-caption {
  background: rgba(0, 0, 0, 0.45);
  border-radius: 8px;
  padding: 8px;
}
""", bs_js=True),
"""A slideshow of three event photos (Annual Day, Sports Week, Tech Fest) that changes automatically every 3 seconds with a sliding animation.
Small bars at the bottom (indicators) show the current slide and jump to any slide; arrows at the left and right go to the previous or next photo. On tablet and desktop each photo has a white caption.""",
"""
<ul><li>A <b>carousel</b> is a slideshow that cycles through images or content.</li>
<li>Structure: <code>.carousel.slide</code> &gt; <code>.carousel-indicators</code>, <code>.carousel-inner</code> &gt; <code>.carousel-item</code> (one with <code>.active</code>), <code>.carousel-caption</code>, <code>.carousel-control-prev / -next</code>.</li>
<li><code>data-bs-ride="carousel"</code> starts it automatically on page load; <code>data-bs-interval="3000"</code> sets 3 seconds per slide.</li>
<li>Indicators use <code>data-bs-slide-to="n"</code>; controls use <code>data-bs-slide="prev"</code> / <code>"next"</code>.</li>
<li><b>Options:</b> interval, keyboard, pause ("hover"), ride, wrap (loop), touch (swipe). <code>.carousel-fade</code> fades instead of sliding; <code>data-bs-interval</code> on an item sets its own time.</li>
<li><code>object-fit: cover</code> with a fixed height keeps all slides the same height; a semi-transparent caption background keeps the text readable on bright photos.</li></ul>
"""))

P.append(WE("w4_17", "Animated photo gallery with seven photos (Practical 21)", page("Photo Gallery", """
<div class="container py-3">
  <h1 class="h4 text-center">Wonders of Gujarat</h1>
  <div class="form-check form-switch mb-2">
    <input class="form-check-input" type="checkbox" id="fade">
    <label class="form-check-label" for="fade">Fade effect</label>
  </div>

  <div id="gallery" class="carousel slide shadow"
    data-bs-ride="carousel" data-bs-interval="2500">
    <div class="carousel-indicators" id="dots"></div>
    <div class="carousel-inner rounded" id="slides"></div>
    <button class="carousel-control-prev" data-bs-target="#gallery"
      data-bs-slide="prev">
      <span class="carousel-control-prev-icon"></span></button>
    <button class="carousel-control-next" data-bs-target="#gallery"
      data-bs-slide="next">
      <span class="carousel-control-next-icon"></span></button>
  </div>

  <div class="d-flex justify-content-between
    align-items-center my-2">
    <span class="badge text-bg-dark" id="count">Photo 1 of 7</span>
    <div>
      <button class="btn btn-sm btn-outline-dark" id="pause">
        <i class="bi bi-pause-fill"></i> Pause</button>
      <button class="btn btn-sm btn-dark" id="play">
        <i class="bi bi-play-fill"></i> Play</button>
    </div>
  </div>
  <div class="row g-1" id="thumbs"></div>
</div>
""", style="""
.carousel-item img { height: 300px; object-fit: cover; }
.carousel-caption {
  background: rgba(0, 0, 0, 0.45);
  border-radius: 8px;
  padding: 8px;
}
.thumb { height: 50px; object-fit: cover; cursor: pointer;
  opacity: 0.5; transition: opacity 0.3s; }
.thumb.on { opacity: 1; outline: 3px solid #0d6efd; }
/* caption slides up on every new photo */
.carousel-item.active .carousel-caption {
  animation: up 0.8s ease;
}
@keyframes up {
  from { transform: translateY(40px); opacity: 0; }
  to { transform: none; opacity: 1; }
}
""", script="""
var photos = [
  ["rani-ki-vav", "Rani ki Vav", "Stepwell in Patan"],
  ["gir", "Gir Forest", "Home of Asiatic lions"],
  ["statue-of-unity", "Statue of Unity", "182 m tall"],
  ["rann", "Rann of Kutch", "White salt desert"],
  ["somnath", "Somnath Temple", "On the Arabian Sea"],
  ["saputara", "Saputara", "Hill station in Dang"],
  ["dwarka", "Dwarkadhish Temple", "Dwarka"]
];
var dots = "", slides = "", thumbs = "";
photos.forEach(function (p, i) {
  var on = i === 0 ? " active" : "";
  dots += '<button data-bs-target="#gallery" class="' + on +
    '" data-bs-slide-to="' + i + '"></button>';
  slides += '<div class="carousel-item' + on + '">' +
    '<img src="img/' + p[0] + '.jpg"' +
    ' class="d-block w-100" width="1200" height="400"' +
    ' alt="' + p[1] + '"><div class="carousel-caption">' +
    "<h5>" + p[1] + "</h5><p>" + p[2] + "</p></div></div>";
  thumbs += '<div class="col"><img src="img/' + p[0] +
    '.jpg" alt="' + (i + 1) + '" class="thumb w-100 rounded' +
    (i === 0 ? " on" : "") + '" data-i="' + i + '"></div>';
});
document.getElementById("dots").innerHTML = dots;
document.getElementById("slides").innerHTML = slides;
document.getElementById("thumbs").innerHTML = thumbs;

var el = document.getElementById("gallery");
var car = bootstrap.Carousel.getOrCreateInstance(el);
var th = document.querySelectorAll(".thumb");

th.forEach(function (t) {
  t.onclick = function () { car.to(Number(t.dataset.i)); };
});
document.getElementById("pause").onclick = function () {
  car.pause();
};
document.getElementById("play").onclick = function () {
  car.cycle();
};
document.getElementById("fade").onchange = function () {
  el.classList.toggle("carousel-fade", this.checked);
};

// slid.bs.carousel: e.to = index of the new slide
el.addEventListener("slid.bs.carousel", function (e) {
  document.getElementById("count").textContent =
    "Photo " + (e.to + 1) + " of " + photos.length;
  th.forEach(function (t, i) {
    t.classList.toggle("on", i === e.to);
  });
});
""", icons=True, bs_js=True),
"""A gallery titled "Wonders of Gujarat" with seven photos (Rani ki Vav, Gir Forest, Statue of Unity, Rann of Kutch, Somnath Temple, Saputara, Dwarkadhish Temple) that change every 2.5 seconds. Each caption slides up when its photo appears.
Below the slideshow, a badge shows "Photo 3 of 7", next to Pause and Play buttons. A row of seven small thumbnails highlights the current photo, and clicking a thumbnail jumps to that photo.
Turning on the "Fade effect" switch makes the photos fade instead of slide; the arrows and indicators also work.""",
"""
<ul><li>The seven slides, indicators and thumbnails are generated from the <code>photos</code> array with <code>forEach</code>, which avoids repeating HTML seven times.</li>
<li><code>data-bs-ride="carousel"</code> + <code>data-bs-interval="2500"</code> auto-play the gallery.</li>
<li><b>Methods:</b> <code>to(n)</code> goes to slide n (thumbnail click), <code>pause()</code> stops, <code>cycle()</code> starts auto-play; also <code>prev()</code>, <code>next()</code>, <code>nextWhenVisible()</code>, <code>dispose()</code>.</li>
<li><b>Events:</b> <code>slide.bs.carousel</code> (slide starts) and <code>slid.bs.carousel</code> (slide finished); <code>e.to</code> and <code>e.from</code> give the indexes and <code>e.direction</code> the direction.</li>
<li><b>Animation:</b> <code>.slide</code> slides; toggling <code>.carousel-fade</code> gives a cross-fade; a CSS <code>@keyframes</code> animation makes each caption slide up.</li>
<li>Replace the placeholders with real photos in an <code>img</code> folder using the same file names.</li></ul>
""", actions="bootstrap.Carousel.getInstance(document.getElementById('gallery')).to(2)"))

P.append(WE("w4_18", "Affix plug-in replaced by sticky positioning", page("Sticky (Affix)", """
<div class="page border rounded" id="page">
  <header class="bg-primary text-white p-3">
    <h1 class="h5 m-0">DiplomaOne Blog</h1></header>
  <nav class="navbar bg-dark sticky-top px-3" id="bar"
    data-bs-theme="dark">
    <span class="navbar-brand small">Menu</span>
    <span class="text-white-50 small" id="state">normal</span>
  </nav>
  <div class="row g-0">
    <div class="col-4 p-2">
      <div class="list-group small sticky-top side">
        <a href="#" class="list-group-item">Latest</a>
        <a href="#" class="list-group-item">Popular</a>
        <a href="#" class="list-group-item">Tips</a>
      </div>
    </div>
    <div class="col-8 p-2" id="posts"></div>
  </div>
</div>
""", style="""
.page { height: 420px; overflow-y: auto; }
.side { top: 64px; }            /* below the sticky navbar */
#bar.stuck { box-shadow: 0 4px 10px rgba(0, 0, 0, .5); }
""", script="""
var html = "";
for (var i = 1; i <= 12; i++) {
  html += '<div class="card card-body mb-2">Post ' + i +
    ": responsive web design tips...</div>";
}
document.getElementById("posts").innerHTML = html;

// affix-like class change after scrolling 60 px
var page = document.getElementById("page");
page.addEventListener("scroll", function () {
  var stuck = page.scrollTop > 60;
  var bar = document.getElementById("bar");
  bar.classList.toggle("stuck", stuck);
  document.getElementById("state").textContent =
    stuck ? "affixed (sticky)" : "normal";
});
"""),
"""A blog page with a blue header, a dark "Menu" bar, a side menu (Latest, Popular, Tips) and 12 posts.
When the page is scrolled, the blue header moves away but the dark bar stays fixed at the top with a shadow, and its text changes from "normal" to "affixed (sticky)". The side menu also stays visible just below the bar while the posts scroll.""",
"""
<ul><li><b>Affix (Bootstrap 3)</b> made an element fixed after the page scrolled past an offset: <code>data-spy="affix" data-offset-top="200"</code>, adding the classes .affix-top, .affix and .affix-bottom.</li>
<li>Bootstrap 4 <b>removed the affix plug-in</b> because CSS <code>position: sticky</code> does the same job without JavaScript.</li>
<li><b>.sticky-top</b> keeps an element in normal flow until it reaches the top of its scroll container, then it sticks. Responsive: <code>.sticky-md-top</code>; also <code>.sticky-bottom</code>.</li>
<li>The side menu uses <code>top: 64px</code> so it sticks below the navbar.</li>
<li>For extra effects, a <code>scroll</code> event listener adds a class (like .affix) when <code>scrollTop</code> passes an offset; here it adds a shadow.</li></ul>
""", actions="var p=document.getElementById('page');p.scrollTop=300;p.dispatchEvent(new Event('scroll'))"))

PROGRAMS = P
