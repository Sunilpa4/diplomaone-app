"""DI03000061 Unit 1 notes: introduction to jQuery and Bootstrap."""
from web_content import make_TS

SN = {
    "s_include": """
<!-- 1. from a CDN -->
<script src="https://code.jquery.com/jquery-3.7.1.min.js">
</script>

<!-- 2. from a local file -->
<script src="js/jquery-3.7.1.min.js"></script>

<!-- your own code AFTER jQuery -->
<script src="js/script.js"></script>
""",
    "s_syntax": """
$(selector).action();

$(this).hide();      // current element
$("p").hide();       // all <p> elements
$(".test").hide();   // all with class="test"
$("#test").hide();   // element with id="test"
""",
    "s_ready": """
$(document).ready(function () {
  // jQuery code here
});

// short form
$(function () {
  // jQuery code here
});
""",
    "s_vs_js": """
// Plain JavaScript
document.getElementById("msg")
        .style.display = "none";

// jQuery
$("#msg").hide();
""",
    "s_selectors": """
$("*")                 // all elements
$("p")                 // element
$("#roll")             // id
$(".note")             // class
$("h1, h2, p")         // group
$("ul li")             // descendant
$("ul > li")           // direct child
$("[href]")            // has attribute
$("[type='text']")     // attribute value
$("a[href^='https']")  // value starts with
$("li:first")          // first match
$("tr:even")           // index 0, 2, 4 ...
$("li:eq(2)")          // index 2
$(":button")           // all buttons
""",
    "s_event": """
$(selector).event(function (e) {
  // code runs when the event occurs
});

$("#btn").click(function () {
  $("p").hide();
});
""",
    "s_on": """
// one event
$("#btn").on("click", function () { ... });

// several events, one handler
$("#box").on("mouseenter mouseleave",
  function () { $(this).toggleClass("hi"); });

// delegation (works for new elements)
$("#list").on("click", "li", function () {
  $(this).remove();
});

$("#btn").off("click");  // remove handler
""",
    "s_hover": """
$("#box").hover(
  function () { $(this).css("color", "red"); },
  function () { $(this).css("color", "black"); }
);
""",
    "s_prevent": """
$("#form1").submit(function (e) {
  e.preventDefault();   // do not reload
  var n = $("#name").val();
  if (n === "") alert("Enter name");
});
""",
    "s_effects": """
$("#p1").hide(400);
$("#p1").show("slow");
$("#p1").toggle();
$("#p1").fadeIn(); $("#p1").fadeOut();
$("#p1").fadeToggle(); $("#p1").fadeTo(500, 0.4);
$("#p1").slideDown(); $("#p1").slideUp();
$("#p1").slideToggle(300, function () {
  alert("done");   // callback
});
$("#b").animate({ left: "200px",
                  opacity: 0.5 }, 1000);
""",
    "s_dom": """
$("#p1").text();              // get text
$("#p1").text("Hello");       // set text
$("#p1").html("<b>Hi</b>");   // set HTML
$("#name").val();             // get input value
$("a").attr("href", "#top");  // set attribute
$("ul").append("<li>end</li>");
$("ul").prepend("<li>start</li>");
$("#p1").after("<hr>");
$("#p1").remove();   $("ul").empty();
$("p").addClass("big");
$("p").removeClass("big");
$("p").toggleClass("big");
$("p").css("color", "blue");
""",
    "s_bs_cdn": """
<link rel="stylesheet"
  href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css">

<script
  src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js">
</script>
""",
    "s_template": """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport"
    content="width=device-width, initial-scale=1">
  <title>My first Bootstrap page</title>
  <link rel="stylesheet" href="css/bootstrap.min.css">
</head>
<body>
  <div class="container">
    <h1>Hello, world!</h1>
  </div>
  <script src="js/bootstrap.bundle.min.js"></script>
</body>
</html>
""",
    "s_folder": """
my_site/
  index.html
  css/
    bootstrap.min.css
  js/
    bootstrap.bundle.min.js
  images/
""",
    "s_viewport": """
<meta name="viewport"
  content="width=device-width, initial-scale=1">
""",
    "s_responsive": """
<div class="container">
  <div class="row">
    <div class="col-12 col-sm-6 col-lg-3">A</div>
    <div class="col-12 col-sm-6 col-lg-3">B</div>
    <div class="col-12 col-sm-6 col-lg-3">C</div>
    <div class="col-12 col-sm-6 col-lg-3">D</div>
  </div>
</div>
""",
    "s_media": """
/* plain CSS media query */
.box { width: 100%; }
@media (min-width: 768px) {
  .box { width: 50%; }
}
""",
    "s_nonresp": """
<!-- 1. no viewport meta tag -->
<style>
  /* 2. fixed width container */
  .container {
    width: 970px !important;
    max-width: none !important;
  }
</style>
<!-- 3. grid classes without breakpoints -->
<div class="row">
  <div class="col-4">...</div>
  <div class="col-4">...</div>
  <div class="col-4">...</div>
</div>
""",
    "s_center": """
<div class="d-flex min-vh-100
  justify-content-center align-items-center
  text-center">
  <h1>Government Polytechnic</h1>
</div>
""",
    "s_dark": """
<html lang="en" data-bs-theme="dark">
""",
}

T = make_TS(SN)

SEC_1_1 = {
    "title": {"en": "1.1 Introduction to jQuery"},
    "items": [
        T("What is jQuery?", """
<p><b>jQuery</b> is a fast, small and feature-rich <b>JavaScript library</b>. Its motto is <i>"Write less, do more"</i>. It makes common JavaScript tasks such as selecting HTML elements, handling events, creating animations and making AJAX calls much easier, with short code that works the same in all browsers.</p>
<ul><li>Created by <b>John Resig</b> and released in <b>January 2006</b>.</li>
<li>Free and open source (MIT licence), maintained by the OpenJS Foundation.</li>
<li>A <b>library</b> is a collection of ready-made functions. jQuery is a single JavaScript file (about 30 KB minified and compressed).</li>
<li>Current version used in these notes: <b>jQuery 3.7.1</b>.</li></ul>
<h4>What jQuery can do</h4>
<ul><li><b>HTML/DOM manipulation:</b> read and change content, attributes and elements.</li>
<li><b>CSS manipulation:</b> change styles and classes.</li>
<li><b>Event handling:</b> click, keyup, submit, resize and more.</li>
<li><b>Effects and animations:</b> hide, show, fade, slide, animate.</li>
<li><b>AJAX:</b> load data from the server without reloading the page.</li>
<li><b>Utilities</b> and a large number of <b>plug-ins</b> (sliders, date pickers, validation).</li></ul>
<h4>Including jQuery in a page</h4>
<p>jQuery must be added with a &lt;script&gt; tag <b>before</b> any script that uses it. It can be loaded from a <b>CDN</b> (Content Delivery Network) or from a downloaded local file (<code>jquery-3.7.1.min.js</code> from jquery.com).</p>
@@s_include@@
<p>The <b>.min.js</b> (minified) version has spaces and comments removed, so it downloads faster; the uncompressed version is used for reading and debugging.</p>
"""),
        T("Importance of jQuery", """
<h4>Why jQuery became important</h4>
<ul><li><b>Write less, do more:</b> one line of jQuery often replaces many lines of JavaScript.</li>
<li><b>Cross-browser compatibility:</b> jQuery hides the differences between browsers, so the same code works everywhere.</li>
<li><b>Easy DOM selection:</b> uses CSS selectors that web designers already know.</li>
<li><b>Simple event handling</b> and <b>built-in animations</b> without writing timers.</li>
<li><b>Easy AJAX</b> with <code>$.ajax()</code>, <code>$.get()</code>, <code>load()</code>.</li>
<li><b>Method chaining:</b> many actions on the same element in one statement.</li>
<li><b>Huge plug-in ecosystem</b>, good documentation and a large community.</li>
<li>Used by many websites and older frameworks: Bootstrap 3 and 4 needed jQuery for their JavaScript components; WordPress still includes it.</li></ul>
<h4>jQuery vs plain JavaScript</h4>
@@s_vs_js@@
<table><tr><th>JavaScript</th><th>jQuery</th></tr>
<tr><td>A programming language</td><td>A library written in JavaScript</td></tr>
<tr><td>Longer code for DOM tasks</td><td>Short, readable code</td></tr>
<tr><td>Browser differences must be handled</td><td>Cross-browser handled by jQuery</td></tr>
<tr><td>No extra file; fastest</td><td>Needs the jQuery file; slightly slower</td></tr></table>
<h4>Limitations</h4>
<ul><li>An extra file must be downloaded.</li>
<li>Modern JavaScript (<code>querySelector</code>, <code>fetch</code>, <code>classList</code>) now does many jQuery tasks, so new frameworks (and Bootstrap 5) do not depend on it.</li></ul>
"""),
        T("jQuery Syntax and Document Ready", """
<p>The basic jQuery syntax <b>selects</b> HTML elements and performs an <b>action</b> on them:</p>
<p><code>$(selector).action()</code></p>
<ul><li><b>$</b> is a short name for the <code>jQuery</code> function (<code>jQuery("p")</code> = <code>$("p")</code>).</li>
<li><b>(selector)</b> finds HTML elements, using CSS selector syntax.</li>
<li><b>action()</b> is a jQuery method performed on the selected elements.</li></ul>
@@s_syntax@@
<h4>The document ready event</h4>
<p>jQuery code is normally written inside the <b>document ready</b> function. It runs only after the whole HTML document (the DOM) has been loaded, so that all elements exist before we try to use them. Without it, code in the &lt;head&gt; would try to select elements that are not created yet.</p>
@@s_ready@@
<ul><li><code>$(document).ready()</code> runs when the DOM is ready (before images finish loading).</li>
<li><code>$(window).on("load", fn)</code> waits until images and all other files are loaded too.</li></ul>
<h4>Method chaining</h4>
<p>Most jQuery methods return the same jQuery object, so several methods can be joined: <code>$("#p1").css("color", "red").slideUp(500).slideDown(500);</code></p>
<h4>Getters and setters</h4>
<p>The same method reads or writes depending on the arguments: <code>$("#a").val()</code> gets the value, <code>$("#a").val("5")</code> sets it. The same is true for <code>text()</code>, <code>html()</code>, <code>attr()</code> and <code>css()</code>.</p>
""", diagram="web1_jq_syntax", programs=["w1_1", "w1_6"]),
        T("jQuery Selectors", """
<p><b>Selectors</b> are used to find (select) HTML elements by their name, id, class, attributes, type, position and more. jQuery selectors are based on <b>CSS selectors</b>, plus some extra filters of its own. All selectors start with the dollar sign and parentheses: <code>$()</code>.</p>
<h4>1. Element selector</h4>
<p>Selects elements by tag name: <code>$("p")</code> selects all paragraphs.</p>
<h4>2. #id selector</h4>
<p>Selects the single element with a given id: <code>$("#roll")</code>. An id must be unique in a page, so this is the fastest selector.</p>
<h4>3. .class selector</h4>
<p>Selects all elements with a given class: <code>$(".note")</code>.</p>
<h4>4. Other selectors</h4>
@@s_selectors@@
<table><tr><th>Type</th><th>Meaning</th></tr>
<tr><td>Universal *</td><td>Every element</td></tr>
<tr><td>Group (comma)</td><td>Elements matching any of the selectors</td></tr>
<tr><td>Descendant (space) / child (&gt;)</td><td>Elements inside another element</td></tr>
<tr><td>Attribute [ ]</td><td>Elements with an attribute or attribute value (=, ^= starts with, $= ends with, *= contains)</td></tr>
<tr><td>Filters :first, :last, :even, :odd, :eq(n)</td><td>Select by position (index starts at 0)</td></tr>
<tr><td>Form filters :button, :input, :checked</td><td>Select form elements by type or state</td></tr>
<tr><td>$(this)</td><td>The element that fired the current event</td></tr></table>
<p><b>Note:</b> <code>:first</code>, <code>:even</code> and <code>:eq()</code> are deprecated from jQuery 3.4 but still work; the recommended methods are <code>.first()</code>, <code>.even()</code> and <code>.eq(n)</code>.</p>
""", diagram="web1_selectors", programs=["w1_2"]),
        T("jQuery Events", """
<p>An <b>event</b> is an action the page can respond to, such as clicking a button, moving the mouse over an element, pressing a key, submitting a form or resizing the window. The moment an event happens is called <b>firing</b>; the function that responds is the <b>event handler</b>.</p>
@@s_event@@
<h4>Common DOM events</h4>
<table><tr><th>Mouse</th><th>Keyboard</th><th>Form</th><th>Document / window</th></tr>
<tr><td>click</td><td>keydown</td><td>submit</td><td>ready</td></tr>
<tr><td>dblclick</td><td>keyup</td><td>change</td><td>load</td></tr>
<tr><td>mouseenter</td><td>keypress</td><td>focus</td><td>resize</td></tr>
<tr><td>mouseleave</td><td></td><td>blur</td><td>scroll</td></tr></table>
<h4>Important event methods</h4>
<ul><li><b>click() / dblclick():</b> single or double click.</li>
<li><b>mouseenter() / mouseleave():</b> pointer enters / leaves the element. <b>hover(in, out)</b> combines both.</li>
<li><b>keydown() / keyup():</b> key pressed / released.</li>
<li><b>focus() / blur():</b> a field gets / loses the cursor.</li>
<li><b>change():</b> the value of a select, checkbox or input changes.</li>
<li><b>submit():</b> a form is submitted.</li>
<li><b>on():</b> attaches one or more events; <b>off()</b> removes them.</li></ul>
@@s_hover@@
@@s_on@@
<h4>The event object</h4>
<p>jQuery passes an <b>event object</b> to the handler. Useful members: <code>e.type</code> (event name), <code>e.target</code> (element), <code>e.pageX / e.pageY</code> (mouse position), <code>e.which</code> or <code>e.key</code> (key pressed), <code>e.preventDefault()</code> (stop default action, e.g. form submit or link) and <code>e.stopPropagation()</code> (stop the event from reaching parent elements).</p>
@@s_prevent@@
""", diagram="web1_events", programs=["w1_3", "w1_4", "w1_5"]),
        T("jQuery Effects and DOM Manipulation", """
<h4>Effects</h4>
<table><tr><th>Method</th><th>Effect</th></tr>
<tr><td>hide(), show(), toggle()</td><td>Hide / show elements</td></tr>
<tr><td>fadeIn(), fadeOut(), fadeToggle(), fadeTo()</td><td>Change opacity gradually</td></tr>
<tr><td>slideDown(), slideUp(), slideToggle()</td><td>Change height gradually</td></tr>
<tr><td>animate({css}, speed)</td><td>Custom animation of numeric CSS properties</td></tr>
<tr><td>stop()</td><td>Stop a running animation</td></tr></table>
<p>The <b>speed</b> can be "slow", "fast" or milliseconds. A <b>callback</b> function runs after the effect is complete.</p>
@@s_effects@@
<h4>DOM manipulation</h4>
<ul><li><b>Get/set content:</b> text(), html(), val().</li>
<li><b>Attributes:</b> attr(), removeAttr(), data().</li>
<li><b>Add elements:</b> append() (end, inside), prepend() (start, inside), after(), before() (outside).</li>
<li><b>Remove elements:</b> remove() (the element itself), empty() (only its children).</li>
<li><b>CSS classes:</b> addClass(), removeClass(), toggleClass(), hasClass(); <b>css()</b> for inline style.</li>
<li><b>Traversing:</b> parent(), children(), find(), next(), prev(), siblings().</li></ul>
@@s_dom@@
""", programs=["w1_7"]),
    ],
}

SEC_1_2 = {
    "title": {"en": "1.2 Introduction to Bootstrap"},
    "items": [
        T("What is Bootstrap and Why Use It?", """
<p><b>Bootstrap</b> is a free and open-source <b>front-end framework</b> for designing <b>responsive, mobile-first</b> websites and web applications. It contains ready-made <b>HTML and CSS</b> design templates for typography, forms, buttons, tables, navigation, cards, modals, image carousels and more, plus optional <b>JavaScript plug-ins</b>.</p>
<ul><li>A <b>framework</b> gives a ready structure and rules; we build our page by adding Bootstrap <b>classes</b> to normal HTML elements, e.g. <code>class="btn btn-primary"</code>.</li>
<li>Website: getbootstrap.com. Latest major version: <b>Bootstrap 5</b> (5.3.3 used here).</li></ul>
<h4>Why use Bootstrap?</h4>
<ul><li><b>Saves time:</b> no need to write CSS for common components; they are ready.</li>
<li><b>Responsive by default:</b> the same page fits mobiles, tablets and desktops.</li>
<li><b>Mobile first:</b> styles are designed for small screens first.</li>
<li><b>Consistent design</b> across all pages and team members.</li>
<li><b>Browser compatibility:</b> works in all modern browsers (Chrome, Firefox, Edge, Safari, Opera).</li>
<li><b>Easy to learn:</b> only basic HTML and CSS knowledge is needed.</li></ul>
<h4>Example: centring text with and without Bootstrap</h4>
<p>Without Bootstrap we write our own flexbox CSS and media queries (Practical 2a). With Bootstrap the same result needs only classes (Practical 2b):</p>
@@s_center@@
""", programs=["w1_9", "w1_10"]),
        T("History of Bootstrap", """
<ul><li><b>2010:</b> developed at <b>Twitter</b> by <b>Mark Otto</b> and <b>Jacob Thornton</b> as an internal tool called <i>Twitter Blueprint</i>, to keep the design of Twitter's internal tools consistent.</li>
<li><b>19 August 2011:</b> released as an open-source project on GitHub with the name <b>Bootstrap</b> (originally "Twitter Bootstrap").</li>
<li><b>Bootstrap 2 (January 2012):</b> added responsive design with a 12-column fluid grid and Glyphicons.</li>
<li><b>Bootstrap 3 (August 2013):</b> rewritten to be <b>mobile first</b>, flat design, grid classes xs/sm/md/lg; panels, thumbnails, wells and jumbotron. It needed jQuery.</li>
<li><b>Bootstrap 4 (January 2018):</b> moved from Less to <b>Sass</b>, <b>Flexbox</b> grid, rem units, new xl breakpoint; <b>cards</b> replaced panels, wells and thumbnails; Glyphicons dropped.</li>
<li><b>Bootstrap 5 (May 2021):</b> <b>jQuery removed</b> (pure JavaScript), Internet Explorer support dropped, new xxl breakpoint, RTL support, Utility API, improved forms, <b>Bootstrap Icons</b> library, <code>data-bs-*</code> attributes.</li>
<li><b>Bootstrap 5.3 (2023):</b> <b>colour modes</b> (dark mode) with the <code>data-bs-theme</code> attribute.</li></ul>
<p>Bootstrap is one of the most popular projects on GitHub and is used by millions of websites.</p>
""", diagram="web1_bs_history"),
        T("Bootstrap 3 vs Bootstrap 4 vs Bootstrap 5", """
<p>The GTU syllabus mentions some Bootstrap 3 components (panel, jumbotron, thumbnail, affix, glyphicons). These notes use <b>Bootstrap 5</b> and show the modern replacement for each old item.</p>
<table><tr><th>Feature</th><th>Bootstrap 3</th><th>Bootstrap 4</th><th>Bootstrap 5</th></tr>
<tr><td>CSS source</td><td>Less</td><td>Sass</td><td>Sass</td></tr>
<tr><td>Grid</td><td>float</td><td>flexbox</td><td>flexbox (+ CSS grid option)</td></tr>
<tr><td>Breakpoints</td><td>xs, sm, md, lg</td><td>+ xl</td><td>+ xxl</td></tr>
<tr><td>jQuery</td><td>required</td><td>required</td><td>not needed</td></tr>
<tr><td>Icons</td><td>Glyphicons</td><td>none built-in</td><td>Bootstrap Icons (separate)</td></tr>
<tr><td>Panels, wells, thumbnails</td><td>yes</td><td>replaced by card</td><td>card</td></tr>
<tr><td>Jumbotron</td><td>yes</td><td>yes</td><td>removed (use utilities)</td></tr>
<tr><td>Affix plug-in</td><td>yes</td><td>removed (use sticky-top)</td><td>sticky-top</td></tr>
<tr><td>Data attributes</td><td>data-toggle</td><td>data-toggle</td><td>data-bs-toggle</td></tr>
<tr><td>Internet Explorer</td><td>IE 8+</td><td>IE 10+</td><td>not supported</td></tr></table>
<h4>Using jQuery with Bootstrap 5</h4>
<p>Bootstrap 5 does not need jQuery, but jQuery can still be added for our own scripts. jQuery handles events and creates elements, Bootstrap gives the styling. Bootstrap 5.3 also supports dark mode:</p>
@@s_dark@@
""", programs=["w1_14"]),
        T("Advantages of Bootstrap", """
<ol><li><b>Responsive grid system:</b> a 12-column flexbox grid with six breakpoints makes layouts adapt automatically.</li>
<li><b>Mobile-first approach:</b> pages are designed for phones first and enhanced for larger screens.</li>
<li><b>Pre-styled components:</b> buttons, navbars, cards, forms, alerts, badges, modals, carousels and many more.</li>
<li><b>Fast development:</b> classes are added instead of writing CSS, saving time.</li>
<li><b>Consistency:</b> the same look on every page, by every developer.</li>
<li><b>Cross-browser compatibility:</b> tested on all modern browsers.</li>
<li><b>JavaScript plug-ins</b> ready to use with data attributes, no coding needed.</li>
<li><b>Customisable:</b> Sass variables, maps and the Utility API allow own colours, fonts and themes; unused parts can be removed.</li>
<li><b>Utility classes</b> for spacing, colours, display, flex, borders, shadows.</li>
<li><b>Free and open source</b>, excellent documentation, huge community, many free themes and templates.</li></ol>
<h4>Disadvantages</h4>
<ul><li>Many websites look similar if the default style is not customised.</li>
<li>The CSS file is large if the whole library is used.</li>
<li>HTML can contain many classes (class-heavy markup).</li>
<li>Learning the class names takes some time, and overriding default styles can be difficult.</li></ul>
"""),
        T("Setting up the Bootstrap Environment", """
<p>Bootstrap can be added to a web page in two common ways (a third way is installing it with a package manager such as <b>npm install bootstrap</b>).</p>
<h4>Method 1: Using a CDN</h4>
<p>A <b>CDN</b> (Content Delivery Network) is a network of servers that delivers files from the server nearest to the user. Bootstrap's official CDN is <b>jsDelivr</b>. No download is required, and the file may already be cached in the browser, but an internet connection is needed.</p>
@@s_bs_cdn@@
<h4>Method 2: Downloading Bootstrap (local files)</h4>
<ol><li>Go to <b>getbootstrap.com</b> and click <b>Download</b> (compiled CSS and JS).</li>
<li>Extract the zip file. It contains the <b>css</b> and <b>js</b> folders.</li>
<li>Copy <code>bootstrap.min.css</code> and <code>bootstrap.bundle.min.js</code> into the project folders.</li>
<li>Link them from the HTML page with relative paths.</li></ol>
@@s_folder@@
<h4>Basic Bootstrap template (Practical 1)</h4>
@@s_template@@
<ul><li><b>&lt;!DOCTYPE html&gt;</b>: Bootstrap requires the HTML5 doctype.</li>
<li><b>Viewport meta tag</b>: needed for responsive behaviour on mobiles.</li>
<li><b>CSS</b> is linked in &lt;head&gt;; the <b>JavaScript bundle</b> is placed just before &lt;/body&gt; so the page appears first.</li>
<li><b>bootstrap.bundle.min.js</b> includes <b>Popper</b> (used to position dropdowns, tooltips and popovers). If <code>bootstrap.min.js</code> is used instead, Popper must be added separately.</li>
<li>Content is placed inside a <b>.container</b> (fixed width per breakpoint) or <b>.container-fluid</b> (full width).</li>
<li>To install Bootstrap Icons, link <code>bootstrap-icons.min.css</code> the same way.</li></ul>
""", diagram="web1_setup", programs=["w1_8"]),
        T("Creating a Responsive Web Page", """
<p><b>Responsive web design (RWD)</b> is an approach in which a web page automatically adjusts its layout, images and text to the size of the screen (mobile, tablet, laptop, desktop), so it is easy to read and use without zooming or horizontal scrolling. The term was introduced by Ethan Marcotte in 2010.</p>
<h4>Main ingredients</h4>
<ol><li><b>Viewport meta tag</b>, so the browser uses the device width.</li>
<li><b>Fluid grid:</b> widths in percentages instead of fixed pixels.</li>
<li><b>Flexible images:</b> <code>max-width: 100%</code> (Bootstrap class <code>img-fluid</code>).</li>
<li><b>Media queries:</b> different CSS rules for different screen widths.</li></ol>
@@s_media@@
<h4>Responsive page with Bootstrap</h4>
<p>Bootstrap gives all four ingredients. Its grid has <b>12 columns</b> in each row; a column class tells how many of the 12 columns an element uses at each breakpoint:</p>
@@s_responsive@@
<ul><li><b>col-12</b>: full width (1 per row) on extra-small screens.</li>
<li><b>col-sm-6</b>: half width (2 per row) from 576 px.</li>
<li><b>col-lg-3</b>: one quarter (4 per row) from 992 px.</li></ul>
<h4>Steps to create a responsive page</h4>
<ol><li>Start from the basic template with the viewport tag and Bootstrap linked.</li>
<li>Wrap content in <code>.container</code>, then <code>.row</code>, then <code>.col-*</code>.</li>
<li>Choose column classes for each breakpoint (mobile first).</li>
<li>Use <code>img-fluid</code> for images and responsive utilities (d-none, d-md-block) to hide or show parts.</li>
<li>Test by resizing the browser or with the browser's device toolbar (F12).</li></ol>
""", diagram="web1_responsive", programs=["w1_11"]),
        T("Viewport and Breakpoints", """
<h4>The viewport meta tag</h4>
<p>The <b>viewport</b> is the visible area of a web page on the screen. Mobile browsers, by default, render a page at a virtual width of about 980 px and then shrink it to fit the phone, so text becomes tiny. The viewport meta tag tells the browser to use the actual width of the device.</p>
@@s_viewport@@
<ul><li><b>width=device-width:</b> set the page width equal to the screen width of the device.</li>
<li><b>initial-scale=1:</b> set the zoom level to 100% when the page is first loaded.</li>
<li>Other options: <code>maximum-scale</code>, <code>minimum-scale</code>, <code>user-scalable=no</code> (not recommended, it stops users from zooming).</li></ul>
<h4>Bootstrap 5 breakpoints</h4>
<p><b>Breakpoints</b> are the screen widths at which the layout changes. They are used in class names as <b>infixes</b>, e.g. <code>col-md-6</code>, <code>d-lg-none</code>.</p>
<table><tr><th>Breakpoint</th><th>Class infix</th><th>Width</th></tr>
<tr><td>Extra small</td><td>(none)</td><td>&lt; 576 px</td></tr>
<tr><td>Small</td><td>sm</td><td>&gt;= 576 px</td></tr>
<tr><td>Medium</td><td>md</td><td>&gt;= 768 px</td></tr>
<tr><td>Large</td><td>lg</td><td>&gt;= 992 px</td></tr>
<tr><td>Extra large</td><td>xl</td><td>&gt;= 1200 px</td></tr>
<tr><td>Extra extra large</td><td>xxl</td><td>&gt;= 1400 px</td></tr></table>
<p>Bootstrap uses <b>min-width</b> media queries, so a class applies <b>at its breakpoint and above</b>. This is why Bootstrap is called <b>mobile first</b>.</p>
""", diagram="web1_viewport"),
        T("Bootstrap Breakpoints and Containers", """
<p>Every Bootstrap layout starts with a <b>container</b>. The container width changes at each breakpoint:</p>
<table><tr><th>Class</th><th>xs</th><th>sm</th><th>md</th><th>lg</th><th>xl</th><th>xxl</th></tr>
<tr><td>.container</td><td>100%</td><td>540px</td><td>720px</td><td>960px</td><td>1140px</td><td>1320px</td></tr>
<tr><td>.container-sm</td><td>100%</td><td>540px</td><td>720px</td><td>960px</td><td>1140px</td><td>1320px</td></tr>
<tr><td>.container-md</td><td>100%</td><td>100%</td><td>720px</td><td>960px</td><td>1140px</td><td>1320px</td></tr>
<tr><td>.container-lg</td><td>100%</td><td>100%</td><td>100%</td><td>960px</td><td>1140px</td><td>1320px</td></tr>
<tr><td>.container-fluid</td><td>100%</td><td>100%</td><td>100%</td><td>100%</td><td>100%</td><td>100%</td></tr></table>
<ul><li><b>.container:</b> responsive fixed-width box, centred on the page.</li>
<li><b>.container-fluid:</b> always 100% wide.</li>
<li><b>.container-{breakpoint}:</b> 100% wide until the breakpoint, then fixed width.</li></ul>
<p>Grid and container details are studied in Unit 2.</p>
""", diagram="web1_breakpoints"),
        T("How to Remove Responsiveness", """
<p>Sometimes a page must keep a fixed desktop layout on all devices, for example an internal admin page or a report. Bootstrap is responsive by default, so the following steps are used to <b>disable responsiveness</b>:</p>
<ol><li><b>Remove the viewport meta tag.</b> Mobile browsers then show the page at desktop width and zoom it out.</li>
<li><b>Override the container width</b> with a fixed value and set <code>max-width: none !important</code>, so it does not shrink at breakpoints.</li>
<li><b>Use grid classes without breakpoints</b> (<code>.col-4</code> instead of <code>.col-md-4</code>), so columns never stack.</li>
<li>For a <b>navbar</b>, remove the collapse and toggler (or use <code>navbar-expand</code>, which never collapses).</li>
<li>Avoid responsive utility classes such as <code>d-md-none</code>.</li></ol>
@@s_nonresp@@
<p><b>Result:</b> on a phone the user sees a small, zoomed-out page and must zoom or scroll sideways. This is why responsiveness should be removed only when it is really needed.</p>
""", programs=["w1_12"]),
        T("Major Features of Bootstrap", """
<ol><li><b>Responsive grid system:</b> 12 columns, 6 breakpoints, flexbox based; offsets, ordering and nesting.</li>
<li><b>Mobile-first styles</b> throughout the framework.</li>
<li><b>Reboot and typography:</b> consistent default styles for headings, lists, tables, display headings, lead text.</li>
<li><b>Components:</b> buttons, button groups, navs, navbar, breadcrumb, pagination, badges, alerts, cards, list groups, progress bars, spinners, toasts, forms and input groups.</li>
<li><b>JavaScript plug-ins:</b> modal, dropdown, collapse, carousel, tooltip, popover, scrollspy, tab, offcanvas, toast; used with <code>data-bs-*</code> attributes or JavaScript.</li>
<li><b>Utility classes:</b> spacing (m-3, p-2), colours, display, flex, borders, shadows, sizing, position, text.</li>
<li><b>Forms:</b> styled controls, floating labels, validation styles.</li>
<li><b>Icons:</b> Bootstrap Icons, an open-source library of 2000+ SVG icons.</li>
<li><b>Customisation:</b> Sass variables, maps, mixins, CSS variables, the Utility API and colour modes (dark mode).</li>
<li><b>Browser compatibility</b> and accessibility (ARIA attributes, keyboard support).</li>
<li><b>Documentation and community:</b> clear official docs with examples; free and open source (MIT licence).</li></ol>
""", diagram="web1_features", programs=["w1_13"]),
    ],
}

NOTES = [SEC_1_1, SEC_1_2]
