"""DI03000061 Unit 4 notes: Bootstrap plug-ins."""
from web_content import make_TS

SN = {
    "s_include": """
<!-- end of body: one file for all plug-ins -->
<script src="js/bootstrap.bundle.min.js"></script>
<!-- Bootstrap 3 needed jQuery first -->
<script src="js/jquery.min.js"></script>
<script src="js/bootstrap.min.js"></script>
""",
    "s_api": """
<!-- 1. data attributes -->
<button data-bs-toggle="collapse" data-bs-target="#box">
  Toggle</button>
<div class="collapse" id="box">...</div>
<script>
  // 2. JavaScript API
  var el = document.getElementById("box");
  var c = new bootstrap.Collapse(el, { toggle: false });
  c.show();                                 // method
  bootstrap.Collapse.getInstance(el);       // existing
  bootstrap.Collapse.getOrCreateInstance(el);
  el.addEventListener("shown.bs.collapse", function () {
    console.log("opened");                  // event
  });
</script>
""",
    "s_bs3_api": """
// Bootstrap 3 (jQuery)
$("#box").collapse("show");
$("#myModal").on("shown.bs.modal", function () { });
""",
    "s_fade": """
<div class="alert alert-info fade show" id="msg">Hello</div>
<script>
  msg.classList.toggle("show");   // fade out / in
  msg.addEventListener("transitionend", function () {
    console.log("finished");
  });
</script>
""",
    "s_page_fade": """
<a class="nav-link active" data-bs-toggle="tab"
  href="#home">Home</a>
<a class="nav-link" data-bs-toggle="tab"
  href="#about">About</a>
<div class="tab-content">
  <section class="tab-pane fade show active" id="home">
    ...</section>
  <section class="tab-pane fade" id="about">...</section>
</div>
""",
    "s_modal": """
<button class="btn btn-primary" data-bs-toggle="modal"
  data-bs-target="#info">Open</button>

<div class="modal fade" id="info" tabindex="-1">
  <div class="modal-dialog modal-dialog-centered">
    <div class="modal-content">
      <div class="modal-header">
        <h5 class="modal-title">Welcome</h5>
        <button class="btn-close" data-bs-dismiss="modal">
        </button>
      </div>
      <div class="modal-body">Results on 5 Dec.</div>
      <div class="modal-footer">
        <button class="btn btn-secondary"
          data-bs-dismiss="modal">Close</button>
      </div>
    </div>
  </div>
</div>
""",
    "s_modal_js": """
var el = document.getElementById("info");
var m = new bootstrap.Modal(el, {
  backdrop: "static",     // no close on outside click
  keyboard: false         // no close on Esc
});
m.show();
el.addEventListener("show.bs.modal", function (e) {
  var opener = e.relatedTarget;    // button clicked
});
el.addEventListener("hidden.bs.modal", function () {
  console.log("closed");
});
""",
    "s_scrollspy": """
<nav id="menu">
  <ul class="nav nav-pills">
    <li class="nav-item"><a class="nav-link" href="#s1">One</a></li>
    <li class="nav-item"><a class="nav-link" href="#s2">Two</a></li>
  </ul>
</nav>
<div data-bs-spy="scroll" data-bs-target="#menu"
  data-bs-smooth-scroll="true" tabindex="0"
  style="height: 300px; overflow-y: auto">
  <h4 id="s1">One</h4><p>...</p>
  <h4 id="s2">Two</h4><p>...</p>
</div>
""",
    "s_tab_js": """
var link = document.querySelector('a[href="#about"]');
bootstrap.Tab.getOrCreateInstance(link).show();

link.addEventListener("shown.bs.tab", function (e) {
  // e.target = new tab, e.relatedTarget = previous tab
});
""",
    "s_dropdown_js": """
<button class="btn btn-success dropdown-toggle"
  data-bs-toggle="dropdown" data-bs-auto-close="outside"
  data-bs-offset="0,10">Filters</button>
<script>
  var dd = bootstrap.Dropdown.getOrCreateInstance(btn);
  dd.toggle();
  btn.addEventListener("hidden.bs.dropdown", function () {
    console.log("menu closed");
  });
</script>
""",
    "s_tooltip": """
<button class="btn btn-secondary" data-bs-toggle="tooltip"
  data-bs-placement="top" title="Save the form">Save</button>
<script>
  var sel = '[data-bs-toggle="tooltip"]';
  document.querySelectorAll(sel).forEach(function (el) {
    new bootstrap.Tooltip(el);
  });
</script>
""",
    "s_tooltip_js": """
var t = new bootstrap.Tooltip(btn, {
  placement: "bottom", trigger: "click", html: true,
  title: "<b>Bold</b> tip", delay: { show: 200, hide: 100 }
});
t.show();  t.hide();  t.toggle();  t.disable();
btn.addEventListener("shown.bs.tooltip", function () { });
""",
    "s_popover": """
<button class="btn btn-danger" data-bs-toggle="popover"
  data-bs-title="Last date"
  data-bs-content="Fees by 30 Nov.">Click me</button>
<a tabindex="0" class="btn btn-warning" role="button"
  data-bs-toggle="popover" data-bs-trigger="focus"
  data-bs-content="Closes on next click">Dismissible</a>
<script>
  document.querySelectorAll('[data-bs-toggle="popover"]')
    .forEach(function (el) { new bootstrap.Popover(el); });
</script>
""",
    "s_button": """
<button class="btn btn-outline-primary"
  data-bs-toggle="button">Like</button>
<input type="checkbox" class="btn-check" id="c1">
<label class="btn btn-outline-success" for="c1">Hostel</label>
<script>
  bootstrap.Button.getOrCreateInstance(likeBtn).toggle();
</script>
""",
    "s_alert_plugin": """
<div class="alert alert-warning alert-dismissible fade show"
  id="note">Holiday on Monday.
  <button class="btn-close" data-bs-dismiss="alert"></button>
</div>
<script>
  bootstrap.Alert.getOrCreateInstance(note).close();
  note.addEventListener("closed.bs.alert", function () {
    console.log("alert removed");
  });
</script>
""",
    "s_collapse": """
<a class="btn btn-primary" data-bs-toggle="collapse"
  href="#more">Read more</a>
<button class="btn btn-success" data-bs-toggle="collapse"
  data-bs-target=".multi">Toggle both</button>
<div class="collapse" id="more">Extra text...</div>
<div class="collapse multi">A</div>
<div class="collapse multi">B</div>
""",
    "s_collapse_js": """
var c = new bootstrap.Collapse("#more", {
  toggle: false,          // do not open on creation
  parent: "#faq"          // accordion behaviour
});
c.show();  c.hide();  c.toggle();
more.addEventListener("hidden.bs.collapse", function () {
  console.log("closed");
});
""",
    "s_accordion": """
<div class="accordion" id="faq">
  <div class="accordion-item">
    <h2 class="accordion-header">
      <button class="accordion-button" data-bs-toggle="collapse"
        data-bs-target="#q1">Who can apply?</button>
    </h2>
    <div id="q1" class="accordion-collapse collapse show"
      data-bs-parent="#faq">
      <div class="accordion-body">SSC passed.</div>
    </div>
  </div>
  <!-- more .accordion-item ... -->
</div>
""",
    "s_carousel": """
<div id="g" class="carousel slide" data-bs-ride="carousel"
  data-bs-interval="3000">
  <div class="carousel-indicators">
    <button data-bs-target="#g" data-bs-slide-to="0"
      class="active"></button>
    <button data-bs-target="#g" data-bs-slide-to="1"></button>
  </div>
  <div class="carousel-inner">
    <div class="carousel-item active">
      <img src="img/1.jpg" class="d-block w-100" alt="One">
      <div class="carousel-caption">
        <h5>Rani ki Vav</h5><p>Patan</p></div>
    </div>
    <div class="carousel-item">
      <img src="img/2.jpg" class="d-block w-100" alt="Two">
    </div>
  </div>
  <button class="carousel-control-prev" data-bs-target="#g"
    data-bs-slide="prev">
    <span class="carousel-control-prev-icon"></span></button>
  <button class="carousel-control-next" data-bs-target="#g"
    data-bs-slide="next">
    <span class="carousel-control-next-icon"></span></button>
</div>
""",
    "s_carousel_js": """
var car = bootstrap.Carousel.getOrCreateInstance("#g");
car.to(3);   car.pause();   car.cycle();
car.next();  car.prev();
g.addEventListener("slid.bs.carousel", function (e) {
  count.textContent = "Photo " + (e.to + 1);
});
""",
    "s_affix": """
<!-- Bootstrap 3 -->
<nav class="navbar" data-spy="affix" data-offset-top="200">
<!-- Bootstrap 5 -->
<nav class="navbar sticky-top bg-dark">...</nav>
<style>
  .side { position: sticky; top: 70px; }
</style>
""",
}

T = make_TS(SN)

SEC_4_1 = {
    "title": {"en": "4.1 Plug-ins: Transition, Modal, Scrollspy, Tab and Dropdown"},
    "items": [
        T("Introduction to Bootstrap Plug-ins", """
<p>A <b>Bootstrap plug-in</b> is a ready-made JavaScript module that adds interactive behaviour to components: opening a modal, showing a dropdown menu, sliding a carousel, collapsing content, and so on.</p>
<h4>Why plug-ins?</h4>
<ul><li><b>No custom JavaScript needed:</b> most plug-ins work just by adding data attributes in HTML.</li>
<li><b>Saves development time</b> and gives the same tested behaviour in all browsers.</li>
<li><b>Responsive and touch friendly</b> (e.g. swipe in carousel).</li>
<li><b>Accessible:</b> keyboard support, focus handling and ARIA attributes are built in.</li>
<li><b>Customisable</b> through options, methods and events when needed.</li></ul>
<h4>Including plug-ins</h4>
<p>All plug-ins are in one file, <b>bootstrap.bundle.min.js</b>, which also contains <b>Popper</b> (needed for dropdowns, tooltips and popovers). Place it at the end of the body. Bootstrap 5 does <b>not</b> need jQuery; Bootstrap 3 needed jQuery loaded first.</p>
@@s_include@@
<h4>List of plug-ins</h4>
<table><tr><th>Plug-in</th><th>Use</th></tr>
<tr><td>Transition</td><td>Helper for CSS animations (built in since BS4)</td></tr>
<tr><td>Modal</td><td>Dialog box / pop-up window</td></tr>
<tr><td>Dropdown</td><td>Toggleable menus</td></tr>
<tr><td>Scrollspy</td><td>Highlights nav links while scrolling</td></tr>
<tr><td>Tab</td><td>Switches tab panes</td></tr>
<tr><td>Tooltip / Popover</td><td>Small hover labels / click boxes</td></tr>
<tr><td>Alert</td><td>Dismisses alert messages</td></tr>
<tr><td>Button</td><td>Toggle state of buttons</td></tr>
<tr><td>Collapse</td><td>Shows / hides content, accordion</td></tr>
<tr><td>Carousel</td><td>Image slideshow</td></tr>
<tr><td>Affix</td><td>Fixes an element on scroll (BS3; now .sticky-top)</td></tr></table>
<p>Bootstrap 5 also adds <b>Offcanvas</b> (side panel) and <b>Toast</b> (small notification).</p>
""", diagram="web4_plugins"),
        T("Using Plug-ins: Data Attributes and JavaScript API", """
<p>Every Bootstrap plug-in can be used in two ways.</p>
<h4>1. Data attributes (no code)</h4>
<p>Add <code>data-bs-toggle</code>, <code>data-bs-target</code>, <code>data-bs-dismiss</code>, <code>data-bs-ride</code> etc. to HTML elements. Options can also be given as attributes, e.g. <code>data-bs-interval="3000"</code>. In Bootstrap 3 the prefix was <code>data-</code> (data-toggle).</p>
<h4>2. JavaScript API</h4>
<ul><li><b>Create:</b> <code>new bootstrap.Modal(element, options)</code> or <code>bootstrap.Modal.getOrCreateInstance(element)</code>.</li>
<li><b>Options:</b> an object such as <code>{ backdrop: "static" }</code>.</li>
<li><b>Methods:</b> show(), hide(), toggle(), dispose() and plug-in-specific ones. Methods are asynchronous: they start the animation and return immediately.</li>
<li><b>Events:</b> each plug-in fires custom events named <code>action.bs.plugin</code>. The infinitive form (<b>show</b>.bs.modal) fires at the start; the past participle (<b>shown</b>.bs.modal) fires after the animation. Calling <code>e.preventDefault()</code> in a start event cancels the action.</li></ul>
@@s_api@@
<p>Bootstrap 3 used jQuery syntax:</p>
@@s_bs3_api@@
""", diagram="web4_api", programs=["w4_1"]),
        T("Transition Plug-in", """
<p>The <b>transition plug-in</b> (transition.js in Bootstrap 3) was a small helper that detected the end of CSS transitions (the <code>transitionend</code> event) so that other plug-ins could wait for animations. It was required by modal, carousel, collapse, alert and tab for their animations.</p>
<ul><li>In <b>Bootstrap 4/5</b> it is no longer a separate plug-in; the transition logic is built into each plug-in.</li>
<li><b>.fade</b> gives an opacity transition; <b>.show</b> makes the element visible. Toggling .show fades an element in or out.</li>
<li>Animations: modal (fade and slide down), alert (fade out), collapse (<code>.collapsing</code> height change), carousel (<code>.slide</code> or <code>.carousel-fade</code>), tab panes (fade).</li>
<li>Custom transitions use the CSS <code>transition</code> property; JavaScript can react to <code>transitionend</code>.</li>
<li>Animations are switched off when the user's system has <b>reduced motion</b> enabled.</li></ul>
@@s_fade@@
<h4>Smooth page transition (Practical 18)</h4>
<p>Home, About and Contact can be placed as <code>.tab-pane.fade</code> sections in one page. Navbar links with <code>data-bs-toggle="tab"</code> switch them; the old page fades out and the new page fades in without reloading. Extra CSS (<code>transform: translateY()</code>) can add a slide effect.</p>
@@s_page_fade@@
""", programs=["w4_2", "w4_3"]),
        T("Modal Dialog Box", """
<p>A <b>modal</b> is a dialog box (pop-up window) displayed on top of the current page. The page behind is covered by a dark <b>backdrop</b> and cannot be used until the modal is closed. Uses: confirmations (save, delete), login forms, messages, image previews.</p>
@@s_modal@@
<h4>Structure</h4>
<ul><li><b>.modal</b> (with <code>.fade</code> for animation, <code>tabindex="-1"</code>) &gt; <b>.modal-dialog</b> &gt; <b>.modal-content</b>.</li>
<li><b>.modal-header</b> (title + close button), <b>.modal-body</b> (content), <b>.modal-footer</b> (action buttons).</li></ul>
<h4>Opening and closing</h4>
<ul><li>Open: <code>data-bs-toggle="modal"</code> and <code>data-bs-target="#id"</code> on a button (or href on a link).</li>
<li>Close: any element with <code>data-bs-dismiss="modal"</code>, a click on the backdrop, or the Esc key.</li></ul>
<h4>Variations</h4>
<table><tr><th>Class / attribute</th><th>Effect</th></tr>
<tr><td>.modal-sm / .modal-lg / .modal-xl</td><td>Small (300 px) / large (800 px) / extra large (1140 px)</td></tr>
<tr><td>.modal-fullscreen, .modal-fullscreen-md-down</td><td>Full screen (always / below md)</td></tr>
<tr><td>.modal-dialog-centered</td><td>Vertically centred</td></tr>
<tr><td>.modal-dialog-scrollable</td><td>Only the body scrolls for long content</td></tr>
<tr><td>data-bs-backdrop="static"</td><td>Does not close on an outside click</td></tr>
<tr><td>data-bs-keyboard="false"</td><td>Does not close with Esc</td></tr></table>
<p>Only one modal should be open at a time. Place the modal HTML at the top level of the body.</p>
""", diagram="web4_modal", programs=["w4_4"]),
        T("Modal: Properties, Methods and Events", """
<h4>Properties (options)</h4>
<table><tr><th>Option</th><th>Default</th><th>Meaning</th></tr>
<tr><td>backdrop</td><td>true</td><td>true = dark backdrop that closes the modal on click; false = no backdrop; "static" = backdrop that does not close it</td></tr>
<tr><td>keyboard</td><td>true</td><td>Close the modal with the Esc key</td></tr>
<tr><td>focus</td><td>true</td><td>Put the focus on the modal when opened</td></tr></table>
<p>(Bootstrap 3 also had <code>show</code> and <code>remote</code> options.)</p>
<h4>Methods</h4>
<ul><li><b>show()</b>, <b>hide()</b>, <b>toggle()</b>: open, close, switch.</li>
<li><b>handleUpdate()</b>: re-adjust the position if the height changes while open.</li>
<li><b>dispose()</b>: destroys the modal object.</li>
<li><b>getInstance(el)</b>, <b>getOrCreateInstance(el)</b>: static methods to get the object.</li></ul>
<h4>Events</h4>
<table><tr><th>Event</th><th>Fires</th></tr>
<tr><td>show.bs.modal</td><td>When show is called (before opening); <code>e.relatedTarget</code> = the clicked button</td></tr>
<tr><td>shown.bs.modal</td><td>After the modal is fully visible</td></tr>
<tr><td>hide.bs.modal</td><td>When hide is called</td></tr>
<tr><td>hidden.bs.modal</td><td>After the modal is fully hidden</td></tr>
<tr><td>hidePrevented.bs.modal</td><td>When a static backdrop is clicked or Esc is pressed with keyboard false</td></tr></table>
@@s_modal_js@@
<p><b>Practical 19:</b> a "Save record confirmation" modal opens when the form is submitted and adds the row only after "Yes"; a "Delete record confirmation" modal shows the name of the row and removes it after "Delete".</p>
""", diagram="web4_modal_api", programs=["w4_5", "w4_6"]),
        T("Scrollspy Plug-in", """
<p><b>Scrollspy</b> automatically updates the active link in a navigation (nav, navbar or list group) according to the section of the page that is currently visible while scrolling. It shows the user where they are in a long page.</p>
@@s_scrollspy@@
<h4>Requirements</h4>
<ul><li>Add <code>data-bs-spy="scroll"</code> to the <b>scrolling element</b> (body or a div) and <code>data-bs-target</code> pointing to the nav.</li>
<li>Each nav link <code>href="#id"</code> must match the id of a section; the target nav must be visible.</li>
<li>A scrolling div needs a fixed <b>height</b>, <code>overflow-y: auto</code> and <code>tabindex="0"</code>.</li></ul>
<h4>Options, method and event</h4>
<ul><li><b>Options:</b> <code>smoothScroll</code> (smooth scrolling on link click), <code>rootMargin</code> and <code>threshold</code> (when a section counts as visible), <code>target</code>. Bootstrap 3/4 used <code>offset</code> (pixels from the top).</li>
<li><b>Method:</b> <code>refresh()</code> after adding or removing sections; <code>dispose()</code>.</li>
<li><b>Event:</b> <code>activate.bs.scrollspy</code> fires when a new link becomes active (<code>e.relatedTarget</code> = that link).</li></ul>
<p>Uses: long articles, documentation, single-page websites, news stories (Practical 20).</p>
""", diagram="web4_scrollspy", programs=["w4_7"]),
        T("Tab Plug-in", """
<p>The <b>tab plug-in</b> makes tabs, pills or list groups switch between content panes without loading a new page (see Unit 3 for the nav styles).</p>
<ul><li>Links get <code>data-bs-toggle="tab"</code>, <code>"pill"</code> or <code>"list"</code>, and point to a pane with href or <code>data-bs-target</code>.</li>
<li>Panes are <code>.tab-pane</code> inside <code>.tab-content</code>; the first has <code>.active</code> (and <code>.show</code> with <code>.fade</code>).</li></ul>
<h4>Methods</h4>
<ul><li><code>bootstrap.Tab.getOrCreateInstance(link).show()</code>: activates the tab and shows its pane.</li>
<li><code>dispose()</code>, <code>getInstance()</code>.</li></ul>
@@s_tab_js@@
<h4>Events (order)</h4>
<ol><li><b>hide.bs.tab</b> on the current tab</li>
<li><b>show.bs.tab</b> on the new tab</li>
<li><b>hidden.bs.tab</b> on the previous tab</li>
<li><b>shown.bs.tab</b> on the new tab</li></ol>
<p><code>e.target</code> is the active tab and <code>e.relatedTarget</code> the previous one. Uses: product details, unit summaries, settings pages, and the page switch of Practical 18.</p>
""", programs=["w4_8"]),
        T("Dropdown Plug-in", """
<p>The <b>dropdown plug-in</b> toggles a <code>.dropdown-menu</code> when the button with <code>data-bs-toggle="dropdown"</code> is clicked. It uses <b>Popper</b> to place the menu so that it stays inside the screen.</p>
<h4>Options</h4>
<table><tr><th>Option</th><th>Meaning</th></tr>
<tr><td>autoClose</td><td>true (any click closes), "inside", "outside", false (only the toggle closes it)</td></tr>
<tr><td>offset</td><td>Distance of the menu, e.g. "0,10"</td></tr>
<tr><td>boundary / reference</td><td>Area for overflow checking / element used for positioning</td></tr>
<tr><td>display</td><td>"dynamic" (Popper) or "static"</td></tr></table>
<h4>Methods and events</h4>
<ul><li><b>Methods:</b> toggle(), show(), hide(), update() (re-position), dispose().</li>
<li><b>Events:</b> show.bs.dropdown, shown.bs.dropdown, hide.bs.dropdown, hidden.bs.dropdown (fired on the toggle element).</li>
<li><b>Keyboard:</b> up/down arrows move through the items; Esc closes.</li></ul>
@@s_dropdown_js@@
""", programs=["w4_9"]),
    ],
}

SEC_4_2 = {
    "title": {"en": "4.2 Tooltip, Popover, Alert, Button, Collapse, Carousel and Affix"},
    "items": [
        T("Tooltip Plug-in", """
<p>A <b>tooltip</b> is a small label that appears when the user hovers over or focuses on an element. The text comes from the <code>title</code> (or <code>data-bs-title</code>) attribute.</p>
@@s_tooltip@@
<ul><li>Tooltips are <b>opt-in</b>: for performance they must be initialised with JavaScript (<code>new bootstrap.Tooltip(el)</code>).</li>
<li>They depend on <b>Popper</b> (use the bundle file).</li>
<li>Empty titles show no tooltip. For disabled buttons, put the tooltip on a wrapper span with <code>tabindex="0"</code>.</li></ul>
<h4>Options</h4>
<p><b>placement</b> (top, right, bottom, left, auto), <b>trigger</b> ("hover focus", "click", "focus", "manual"), <b>html</b> (allow HTML), <b>title</b>, <b>delay</b>, <b>animation</b>, <b>offset</b>, <b>container</b>, <b>customClass</b>.</p>
<h4>Methods</h4>
<p>show(), hide(), toggle(), enable(), disable(), toggleEnabled(), setContent(), update(), dispose().</p>
<h4>Events</h4>
<table><tr><th>Event</th><th>Fires</th></tr>
<tr><td>show.bs.tooltip</td><td>When show starts</td></tr>
<tr><td>shown.bs.tooltip</td><td>After the tooltip is visible</td></tr>
<tr><td>hide.bs.tooltip / hidden.bs.tooltip</td><td>When hiding starts / ends</td></tr>
<tr><td>inserted.bs.tooltip</td><td>After the tooltip element is added to the page</td></tr></table>
@@s_tooltip_js@@
""", diagram="web4_tooltip_popover", programs=["w4_10"]),
        T("Popover Plug-in", """
<p>A <b>popover</b> is a larger pop-up box with a <b>title</b> and <b>content</b>, opened by a click by default. It is built on the tooltip plug-in.</p>
@@s_popover@@
<ul><li>Attributes: <code>data-bs-toggle="popover"</code>, <code>data-bs-title</code>, <code>data-bs-content</code>, <code>data-bs-placement</code>, <code>data-bs-trigger</code>.</li>
<li>Popovers are <b>opt-in</b> and need Popper, like tooltips.</li>
<li><b>Dismiss on next click:</b> <code>data-bs-trigger="focus"</code> on an &lt;a&gt; with tabindex="0".</li>
<li><b>Options:</b> same as tooltip plus <code>content</code>. <b>Methods:</b> show(), hide(), toggle(), enable(), disable(), setContent(), dispose(). <b>Events:</b> show/shown/hide/hidden/inserted.bs.popover.</li></ul>
<table><tr><th>Tooltip</th><th>Popover</th></tr>
<tr><td>Short text only</td><td>Title and content (can be HTML)</td></tr>
<tr><td>Hover / focus</td><td>Click (default)</td></tr>
<tr><td>Small black label</td><td>White box with header</td></tr></table>
<p><b>Practical 20</b> uses scrollspy for the story sections, tooltips on photos, collapse for "Read more" and popovers for the reporter and fare details.</p>
""", programs=["w4_11", "w4_15"]),
        T("Alert and Button Plug-ins", """
<h4>Alert plug-in</h4>
<p>The <b>alert plug-in</b> makes alerts dismissible. A close button with <code>data-bs-dismiss="alert"</code> removes the alert from the page (with a fade when <code>.fade .show</code> are present).</p>
@@s_alert_plugin@@
<ul><li><b>Methods:</b> <code>close()</code> (fade out and remove), <code>dispose()</code>, getInstance(), getOrCreateInstance().</li>
<li><b>Events:</b> <code>close.bs.alert</code> (close called) and <code>closed.bs.alert</code> (alert removed); used to show a message after closing.</li></ul>
<h4>Button plug-in</h4>
<p>The <b>button plug-in</b> controls the state of buttons.</p>
@@s_button@@
<ul><li><b>Toggle button:</b> <code>data-bs-toggle="button"</code> switches the <code>.active</code> class and <code>aria-pressed</code> on every click. Method: <code>toggle()</code>.</li>
<li><b>Checkbox / radio buttons:</b> in Bootstrap 5, <code>input.btn-check</code> with <code>label.btn</code>; in Bootstrap 3, <code>data-toggle="buttons"</code> on a btn-group.</li>
<li><b>Loading state:</b> Bootstrap 3 had <code>$(btn).button("loading")</code> with <code>data-loading-text</code>, and <code>button("reset")</code>. In Bootstrap 5, disable the button and add a <code>.spinner-border-sm</code> using JavaScript.</li></ul>
""", programs=["w4_12"]),
        T("Collapse Plug-in", """
<p>The <b>collapse plug-in</b> shows and hides content with a smooth height animation. It is used for "Read more" sections, FAQs, accordions and the responsive navbar menu.</p>
@@s_collapse@@
<h4>How it works</h4>
<ul><li>Hidden content has <code>.collapse</code>; while animating it gets <code>.collapsing</code>; when visible it has <code>.collapse.show</code>.</li>
<li>Trigger: <code>data-bs-toggle="collapse"</code> on a link (href) or button (data-bs-target). A class selector controls <b>multiple targets</b>.</li>
<li><code>.collapse-horizontal</code> animates width instead of height.</li></ul>
<h4>Properties, methods and events</h4>
<table><tr><th>Type</th><th>Members</th></tr>
<tr><td>Options</td><td><b>parent</b>: selector; when one item opens, others in the parent close (accordion). <b>toggle</b>: toggle on creation (default true)</td></tr>
<tr><td>Methods</td><td>show(), hide(), toggle(), dispose(), getInstance(), getOrCreateInstance()</td></tr>
<tr><td>Events</td><td>show.bs.collapse, shown.bs.collapse, hide.bs.collapse, hidden.bs.collapse</td></tr></table>
@@s_collapse_js@@
<h4>Accordion</h4>
<p>An <b>accordion</b> is a group of collapsible items where only one is open at a time, using <code>data-bs-parent</code>.</p>
@@s_accordion@@
""", diagram="web4_collapse", programs=["w4_13", "w4_14"]),
        T("Carousel Plug-in", """
<p>A <b>carousel</b> is a slideshow that cycles through images, text or other content, with optional controls, indicators and captions.</p>
@@s_carousel@@
<h4>Parts</h4>
<ul><li><b>.carousel.slide</b>: wrapper with an id; <code>data-bs-ride="carousel"</code> starts auto-play on load.</li>
<li><b>.carousel-inner</b> &gt; <b>.carousel-item</b>: the slides; one must have <code>.active</code>.</li>
<li><b>.carousel-caption</b>: text over the image.</li>
<li><b>.carousel-indicators</b>: small bars to jump to a slide (<code>data-bs-slide-to</code>).</li>
<li><b>.carousel-control-prev / -next</b>: arrows (<code>data-bs-slide="prev"/"next"</code>).</li></ul>
<h4>Options, methods and events</h4>
<table><tr><th>Type</th><th>Members</th></tr>
<tr><td>Options</td><td>interval (ms, default 5000), ride, pause ("hover"), wrap (loop), keyboard, touch (swipe)</td></tr>
<tr><td>Methods</td><td>cycle(), pause(), prev(), next(), nextWhenVisible(), to(n), dispose()</td></tr>
<tr><td>Events</td><td>slide.bs.carousel (start), slid.bs.carousel (end); e.from, e.to, e.direction</td></tr></table>
@@s_carousel_js@@
<ul><li><code>.carousel-fade</code> fades between slides instead of sliding; <code>.carousel-dark</code> gives dark controls (BS 5.3: data-bs-theme="dark").</li>
<li><code>data-bs-interval</code> on a single item sets its own time.</li>
<li>Give all images the same size (or fixed height with <code>object-fit: cover</code>) so the carousel does not jump.</li></ul>
<p><b>Practical 21</b> builds an animated gallery of seven photos with indicators, captions, a fade switch, pause/play and thumbnails.</p>
""", diagram="web4_carousel", programs=["w4_16", "w4_17"]),
        T("Affix Plug-in", """
<p>The <b>affix plug-in</b> (Bootstrap 3) fixed an element, such as a navbar or side menu, in place after the page was scrolled past a certain point. Before that point the element scrolled normally.</p>
<ul><li>Usage: <code>data-spy="affix"</code> with <code>data-offset-top="200"</code> (and data-offset-bottom).</li>
<li>The plug-in switched classes: <code>.affix-top</code> (before the offset), <code>.affix</code> (fixed), <code>.affix-bottom</code> (near the bottom). The developer wrote CSS for these classes.</li>
<li>Events: affix.bs.affix, affixed.bs.affix, affix-top.bs.affix, etc.</li></ul>
<h4>Bootstrap 4/5 replacement</h4>
<p>The affix plug-in was <b>removed in Bootstrap 4</b> because CSS <b>position: sticky</b> gives the same result without JavaScript.</p>
@@s_affix@@
<ul><li><b>.sticky-top</b>: the element scrolls with the page until it reaches the top, then sticks there.</li>
<li><b>.sticky-{sm|md|lg|xl|xxl}-top</b>: sticky only from that breakpoint; <b>.sticky-bottom</b> sticks at the bottom.</li>
<li><b>.fixed-top</b>: always fixed (not the same as affix).</li>
<li>For extra effects (shadow, smaller logo), a <code>scroll</code> event listener can add a class when <code>scrollY</code> passes an offset.</li></ul>
""", diagram="web4_affix", programs=["w4_18"]),
    ],
}

NOTES = [SEC_4_1, SEC_4_2]
