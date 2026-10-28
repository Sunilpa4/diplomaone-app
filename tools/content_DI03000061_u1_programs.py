"""DI03000061 RWPD Unit 1 – jQuery basics and Bootstrap introduction (practicals 1-2). Live preview in the app."""
from web_content import WE, page

P = []
JQ_STYLE = """
body { font-family: Arial, sans-serif;
       margin: 16px; }
button { padding: 6px 14px; margin: 4px 2px; }
"""

# ------------------------------------------------------------------ 1.1 jQuery
P.append(WE("w1_1", "First jQuery program: document ready, hide and show", page("First jQuery", """
<h2>Welcome to jQuery</h2>
<p id="msg">This paragraph can be hidden
  and shown again using jQuery.</p>
<button id="btnHide">Hide</button>
<button id="btnShow">Show</button>
<button id="btnToggle">Toggle</button>
<p id="status"></p>
""", style=JQ_STYLE + """
#msg { background: #EADDF7; padding: 10px; }
#status { color: green; font-weight: bold; }
""", script="""
$(document).ready(function () {
  $("#status").text("jQuery is ready!");

  $("#btnHide").click(function () {
    $("#msg").hide();
  });
  $("#btnShow").click(function () {
    $("#msg").show();
  });
  $("#btnToggle").click(function () {
    $("#msg").toggle(400);
  });
});
""", jquery=True, bs=False),
"""A heading, a lavender paragraph and three buttons. Below them the green text "jQuery is ready!" appears as soon as the page loads.
Hide makes the paragraph disappear, Show brings it back, and Toggle hides or shows it with a 0.4 second animation.""",
"""
<ul><li>The jQuery library is included with <code>&lt;script src="js/jquery-3.7.1.min.js"&gt;</code> <b>before</b> our own script. (From a CDN: <code>https://code.jquery.com/jquery-3.7.1.min.js</code>.)</li>
<li><code>$(document).ready(function () { ... });</code> runs the code only after the whole HTML document (DOM) is loaded, so all elements exist. The short form is <code>$(function () { ... });</code></li>
<li>Basic syntax: <b>$(selector).action()</b>. <code>$("#msg")</code> selects the element with id="msg", and <code>.hide()</code> is the action.</li>
<li><code>.click(function)</code> attaches a click event handler. <code>.text("...")</code> sets the text of an element.</li>
<li><code>toggle(400)</code> hides a visible element or shows a hidden one; 400 is the animation time in milliseconds.</li></ul>
""", actions="$('#btnToggle').click()"))

P.append(WE("w1_2", "jQuery selectors: element, id, class, attribute and filters", page("jQuery Selectors", """
<h2>jQuery Selectors</h2>
<p>Paragraph 1 (element selector)</p>
<p class="note">Paragraph 2 has class="note"</p>
<p id="special">Paragraph 3 has id="special"</p>
<ul>
  <li>HTML</li>
  <li>CSS</li>
  <li>JavaScript</li>
  <li>jQuery</li>
  <li>Bootstrap</li>
</ul>
<input type="text" placeholder="type = text">
<input type="password" placeholder="type = password">
<p>
  <a href="https://getbootstrap.com">External</a> |
  <a href="#top">Internal</a>
</p>
""", style=JQ_STYLE + """
p { padding: 6px; }
input { padding: 6px; margin: 4px 0; }
""", script="""
$(function () {
  $("p").css("border", "1px solid #999");
  $(".note").css("background", "#FFF1DE");
  $("#special").css("color", "#C62828");
  $("li:first").css("font-weight", "bold");
  $("li:even").css("background", "#E3F0FC");
  $("ul li:last-child").append(" (last)");
  $("input[type='password']")
    .css("border", "2px solid #2E7D32");
  $("a[href^='https']").css("color", "orange");
  $("h2, #special").css("font-style", "italic");
});
""", jquery=True, bs=False),
"""All paragraphs get a grey border, the one with class "note" gets an orange background and the one with id "special" turns red.
In the list, HTML is bold; HTML, JavaScript and Bootstrap (positions 0, 2, 4) get a light blue background, and "(last)" is added after Bootstrap.
The password box gets a green border and the external link turns orange. The heading and Paragraph 3 are italic.""",
"""
<ul><li><b>Element selector</b> <code>$("p")</code> selects all &lt;p&gt; elements.</li>
<li><b>Class selector</b> <code>$(".note")</code> selects elements with class="note". <b>Id selector</b> <code>$("#special")</code> selects the one element with id="special".</li>
<li><b>Filters:</b> <code>:first</code> gives the first match; <code>:even</code> gives positions 0, 2, 4 ... (counting starts at 0). <code>:last-child</code> is a CSS selector that also works.</li>
<li><b>Attribute selector</b> <code>[type='password']</code> matches an attribute value; <code>[href^='https']</code> matches values that <i>start with</i> https.</li>
<li><b>Group selector</b> <code>$("h2, #special")</code> selects both. <code>.css(property, value)</code> changes a style, and <code>.append()</code> adds content at the end.</li></ul>
"""))

P.append(WE("w1_3", "Mouse events: click, dblclick, mouseenter, mouseleave", page("Mouse Events", """
<h2>Mouse Events</h2>
<div id="box">Point at me, click me
  or double-click me</div>
<p><b>Event log</b> (newest first):</p>
<ol id="log"></ol>
""", style=JQ_STYLE + """
#box { background: #EADDF7; padding: 30px;
       text-align: center; border-radius: 8px;
       cursor: pointer; user-select: none; }
#box.big { font-size: 26px; }
""", script="""
$(function () {
  function log(t) {
    $("#log").prepend("<li>" + t + "</li>");
  }
  $("#box").mouseenter(function () {
    $(this).css("background", "#FFF1DE");
    log("mouseenter");
  });
  $("#box").mouseleave(function () {
    $(this).css("background", "#EADDF7");
    log("mouseleave");
  });
  $("#box").click(function () {
    log("click");
  });
  $("#box").dblclick(function () {
    $(this).toggleClass("big");
    log("dblclick - text size changed");
  });
});
""", jquery=True, bs=False),
"""A lavender box. When the mouse enters it, the box turns light orange; when the mouse leaves, it turns lavender again.
Every event is added at the top of the numbered "Event log", e.g. 1. dblclick - text size changed, 2. click, 3. click, 4. mouseenter.
A double-click makes the text bigger (and smaller again on the next double-click). On a phone a tap gives a click event.""",
"""
<ul><li>An <b>event</b> is an action of the user (or browser) that the page can respond to. In jQuery: <code>$(selector).event(function () { ... });</code></li>
<li><b>mouseenter / mouseleave</b> fire when the pointer moves into / out of the element. <code>hover(fnIn, fnOut)</code> is a shortcut for both.</li>
<li><b>click</b> and <b>dblclick</b> fire on single and double clicks. A double-click also fires two click events first, as the log shows.</li>
<li>Inside a handler, <code>this</code> is the element that received the event; <code>$(this)</code> wraps it as a jQuery object.</li>
<li><code>prepend()</code> inserts content at the beginning; <code>toggleClass("big")</code> adds the class if missing and removes it if present.</li></ul>
""", actions="$('#box').trigger('mouseenter').click().click().dblclick()"))

P.append(WE("w1_4", "Keyboard and form events: focus, blur, keyup, change, submit", page("Form Events", """
<h2>Feedback Form</h2>
<form id="f">
  <label>Name</label>
  <input type="text" id="name">
  <label>Feedback (max 50 characters)</label>
  <textarea id="fb" maxlength="50"></textarea>
  <small id="count">0 / 50</small>
  <label>Branch</label>
  <select id="branch">
    <option value="">-- select --</option>
    <option>Computer</option>
    <option>IT</option>
    <option>Mechanical</option>
  </select>
  <p id="choice"></p>
  <button type="submit">Submit</button>
  <p id="result"></p>
</form>
""", style=JQ_STYLE + """
label { display: block; margin-top: 10px; }
input, textarea, select { width: 100%;
  max-width: 320px; padding: 6px; }
#count { display: block; color: #666; }
#result { font-weight: bold; }
""", script="""
$(function () {
  $("input, textarea").focus(function () {
    $(this).css("background", "#FFFDE7");
  }).blur(function () {
    $(this).css("background", "#fff");
  });

  $("#fb").keyup(function () {
    var n = $(this).val().length;
    $("#count").text(n + " / 50");
  });

  $("#branch").change(function () {
    $("#choice").text("You selected: " +
      $(this).val());
  });

  $("#f").submit(function (e) {
    e.preventDefault();
    var name = $("#name").val().trim();
    if (name === "") {
      $("#result").text("Please enter your name")
        .css("color", "red");
    } else {
      $("#result").text("Thank you, " + name)
        .css("color", "green");
    }
  });
});
""", jquery=True, bs=False),
"""A feedback form with Name, Feedback, Branch and a Submit button.
The box you are typing in turns light yellow, and white again when you leave it. While you type feedback, the counter shows e.g. "12 / 50".
Choosing a branch shows "You selected: Computer". Submit with an empty name shows a red "Please enter your name"; with a name it shows a green "Thank you, Riya" and the page is not reloaded.""",
"""
<ul><li><b>focus</b> fires when an input gets the cursor and <b>blur</b> when it loses it. jQuery methods can be <b>chained</b>: <code>.focus(...).blur(...)</code>.</li>
<li><b>keyup</b> fires when a key is released; <code>.val()</code> reads the current value, so the length is counted on every key press. (Other keyboard events: keydown, keypress.)</li>
<li><b>change</b> fires when the selected option of a &lt;select&gt; (or a checkbox, radio or input value) changes.</li>
<li><b>submit</b> fires when the form is submitted. <code>e.preventDefault()</code> stops the browser from sending the form and reloading the page, so we can validate it first.</li>
<li><code>.trim()</code> removes spaces from both ends, so a name of only spaces is also treated as empty.</li></ul>
""", actions="$('#fb').val('Very good lab').keyup(); $('#branch').val('Computer').change(); $('#name').val('Riya'); $('#f').submit()"))

P.append(WE("w1_5", "on() method, event object and window resize", page("Screen Size", """
<h2>Screen width: <span id="w"></span> px</h2>
<p>Device type: <b id="type"></b></p>
<p>Resize the browser window (or switch to
  desktop view) to see the values change.</p>
<button class="b" data-color="#C62828">Red</button>
<button class="b" data-color="#2E7D32">Green</button>
<button class="b" data-color="#1565C0">Blue</button>
<p id="info"></p>
""", style=JQ_STYLE + """
h2 { color: #7B2CD9; }
""", script="""
function showSize() {
  var w = $(window).width();
  var t;
  if (w < 576) t = "Mobile (xs)";
  else if (w < 768) t = "Large mobile (sm)";
  else if (w < 992) t = "Tablet (md)";
  else if (w < 1200) t = "Laptop (lg)";
  else t = "Desktop (xl)";
  $("#w").text(w);
  $("#type").text(t);
}

$(function () {
  showSize();
  $(window).on("resize", showSize);

  $(".b").on("click", function (event) {
    var c = $(this).data("color");
    $("h2").css("color", c);
    $("#info").text("Event type: " + event.type +
      ", button: " + $(this).text());
  });
});
""", jquery=True, bs=False),
"""The heading shows the current width of the browser window, e.g. "Screen width: 390 px", and the device type "Mobile (xs)" (on a desktop browser of 1100 px: "Laptop (lg)").
The numbers update immediately when the window is resized. The Red, Green and Blue buttons change the colour of the heading and show "Event type: click, button: Green".""",
"""
<ul><li><code>.on(event, handler)</code> is the general way to attach any event; <code>.click(fn)</code> is a shortcut for <code>.on("click", fn)</code>. <code>.off()</code> removes handlers.</li>
<li>The <b>resize</b> event of <code>$(window)</code> fires whenever the browser size changes. <code>$(window).width()</code> gives the width in pixels.</li>
<li>The width limits 576, 768, 992 and 1200 px are the same <b>breakpoints</b> that Bootstrap uses for responsive layouts.</li>
<li>The handler receives an <b>event object</b> with details: <code>event.type</code>, <code>event.target</code>, <code>event.pageX / pageY</code>, <code>event.which</code> (key code).</li>
<li><code>.data("color")</code> reads the custom attribute <code>data-color</code>; one handler serves all three buttons.</li></ul>
""", actions="$('.b').eq(1).click()"))

P.append(WE("w1_6", "Simple calculator using jQuery", page("Calculator", """
<h2>Simple Calculator</h2>
<input type="number" id="a" placeholder="First no.">
<input type="number" id="b" placeholder="Second no.">
<div>
  <button data-op="+">+</button>
  <button data-op="-">-</button>
  <button data-op="*">x</button>
  <button data-op="/">/</button>
  <button id="clear">Clear</button>
</div>
<h3 id="ans">Result:</h3>
""", style=JQ_STYLE + """
input { display: block; width: 220px;
        padding: 8px; margin: 6px 0; }
button { min-width: 48px; font-size: 18px; }
#ans { color: #2E7D32; }
""", script="""
$(function () {
  $("button[data-op]").click(function () {
    var a = parseFloat($("#a").val());
    var b = parseFloat($("#b").val());
    var op = $(this).data("op");
    var r;
    if (isNaN(a) || isNaN(b)) {
      r = "Enter both numbers";
    } else if (op === "+") {
      r = a + b;
    } else if (op === "-") {
      r = a - b;
    } else if (op === "*") {
      r = a * b;
    } else {
      r = (b === 0) ? "Cannot divide by 0" : a / b;
    }
    $("#ans").text("Result: " + r);
  });

  $("#clear").click(function () {
    $("#a, #b").val("");
    $("#ans").text("Result:");
  });
});
""", jquery=True, bs=False),
"""Two number boxes and the buttons + - x / Clear.
Enter 25 and 4 and press x: the green line shows "Result: 100". Press / to get "Result: 6.25". With an empty box it shows "Result: Enter both numbers", and dividing by 0 shows "Result: Cannot divide by 0". Clear empties both boxes.""",
"""
<ul><li><code>.val()</code> without an argument <b>reads</b> the value of an input; <code>.val("")</code> <b>sets</b> it. The same getter/setter rule applies to <code>.text()</code>, <code>.html()</code> and <code>.css()</code>.</li>
<li>Input values are strings, so <code>parseFloat()</code> converts them to numbers; <code>isNaN()</code> checks for an empty or invalid entry.</li>
<li><code>$("button[data-op]")</code> selects only buttons that have a data-op attribute, so the Clear button is handled separately.</li>
<li>One handler serves four buttons: <code>$(this).data("op")</code> tells which operator was pressed.</li></ul>
""", actions="$('#a').val('25'); $('#b').val('4'); $('button[data-op=\"*\"]').click()"))

P.append(WE("w1_7", "jQuery effects and DOM: slideToggle, append, fadeOut", page("FAQ and To-do", """
<h2>FAQ</h2>
<div class="q">What is jQuery?</div>
<div class="a">A fast, small JavaScript library
  that makes DOM handling, events and
  animation easy.</div>
<div class="q">Who created jQuery?</div>
<div class="a">John Resig, in 2006.</div>

<h2>To-do list</h2>
<input id="item" placeholder="New task">
<button id="add">Add</button>
<ul id="list"></ul>
<small>Click a task to mark it done,
  double-click to delete it.</small>
""", style=JQ_STYLE + """
.q { background: #7B2CD9; color: #fff;
     padding: 8px; margin-top: 6px;
     cursor: pointer; }
.a { display: none; padding: 8px;
     background: #F3ECFA; }
.done { text-decoration: line-through;
        color: #999; }
#item { padding: 6px; }
""", script="""
$(function () {
  $(".q").click(function () {
    $(this).next(".a").slideToggle(300);
  });

  $("#add").click(function () {
    var t = $("#item").val().trim();
    if (t !== "") {
      $("#list").append("<li>" + t + "</li>");
      $("#item").val("").focus();
    }
  });

  $("#list").on("click", "li", function () {
    $(this).toggleClass("done");
  });
  $("#list").on("dblclick", "li", function () {
    $(this).fadeOut(400, function () {
      $(this).remove();
    });
  });
});
""", jquery=True, bs=False),
"""Two purple FAQ questions; tapping a question slides its answer open (and closed again).
Below is a to-do list: type "Complete practical 1" and press Add to add it to the list. Tapping a task strikes it through in grey; double-tapping fades it out and removes it.""",
"""
<ul><li><b>Effects:</b> <code>slideToggle()</code>, <code>slideUp()</code>, <code>slideDown()</code>, <code>fadeIn()</code>, <code>fadeOut()</code>, <code>fadeToggle()</code>, <code>animate()</code>. The number is the speed in ms; a <b>callback</b> function runs after the effect ends.</li>
<li><code>$(this).next(".a")</code> moves to the next sibling element with class "a" (DOM traversal).</li>
<li><code>append()</code> creates new elements from an HTML string; <code>remove()</code> deletes elements.</li>
<li><b>Event delegation:</b> <code>$("#list").on("click", "li", fn)</code> attaches one handler to the &lt;ul&gt; that also works for &lt;li&gt; items added later. A plain <code>$("li").click()</code> would not work for new items.</li></ul>
""", actions="$('.q').first().click(); $('#item').val('Complete practical 1'); $('#add').click(); $('#item').val('Prepare viva'); $('#add').click(); $('#list li').first().click()"))

# ------------------------------------------------------------------ 1.2 Bootstrap
P.append(WE("w1_8", "Bootstrap starter template (Practical 1)", page("Bootstrap Starter", """
<div class="container py-4">
  <h1 class="text-primary">Hello, Bootstrap!</h1>
  <p class="lead">Bootstrap 5 is installed and
    working.</p>
  <div class="alert alert-success">
    bootstrap.min.css is linked correctly.
  </div>
  <button class="btn btn-primary">Primary</button>
  <button class="btn btn-outline-secondary">
    Secondary</button>
  <button class="btn btn-danger" id="tip"
    data-bs-toggle="tooltip"
    title="bootstrap.bundle.min.js works">
    Tooltip</button>
</div>
""", script="""
var el = document.getElementById("tip");
new bootstrap.Tooltip(el);
""", bs_js=True),
"""A page with a blue heading "Hello, Bootstrap!", a larger grey lead paragraph and a green success alert box.
Below are three styled buttons: blue Primary, grey outlined Secondary and red Tooltip. Pointing at (or tapping) the red button shows a black tooltip "bootstrap.bundle.min.js works".
If the CSS file was not linked, the page would show plain black text and grey browser buttons.""",
"""
<ul><li><b>&lt;!DOCTYPE html&gt;</b> and <b>lang</b> are required for HTML5. <code>&lt;meta charset="UTF-8"&gt;</code> sets the character encoding.</li>
<li>The <b>viewport meta tag</b> <code>width=device-width, initial-scale=1</code> makes the page use the real width of the device; without it a phone shows a zoomed-out desktop page.</li>
<li><code>css/bootstrap.min.css</code> (in &lt;head&gt;) contains all Bootstrap styles. <code>js/bootstrap.bundle.min.js</code> (just before &lt;/body&gt;) contains the JavaScript plug-ins plus Popper (needed for tooltips and dropdowns).</li>
<li>Using a CDN instead of local files: <code>href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css"</code> and the matching js/bootstrap.bundle.min.js URL.</li>
<li>Tooltips are opt-in, so they are initialised with <code>new bootstrap.Tooltip(element)</code>.</li></ul>
""", actions="bootstrap.Tooltip.getInstance(document.getElementById('tip')).show()"))

P.append(WE("w1_9", "College name at the centre WITHOUT Bootstrap (Practical 2a)", page("Without Bootstrap", """
<div class="center">
  <h1>Government Polytechnic, Surat</h1>
  <h2>Department of Computer Engineering</h2>
  <p>Gujarat Technological University</p>
</div>
""", style="""
* { margin: 0; padding: 0;
    box-sizing: border-box; }
body { font-family: Arial, sans-serif; }
.center {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  text-align: center;
  background: #F3ECFA;
  padding: 16px;
}
h1 { color: #7B2CD9; font-size: 28px; }
h2 { color: #333; font-size: 20px;
     margin: 10px 0; }
p { color: #666; }
@media (min-width: 768px) {
  h1 { font-size: 40px; }
  h2 { font-size: 26px; }
}
""", bs=False),
"""The college name (purple), department name and university name appear in the exact centre of the screen, both horizontally and vertically, on a light lavender background. On screens 768 px and wider the text is larger.""",
"""
<ul><li>Without Bootstrap, every style must be written by hand in CSS.</li>
<li><code>display: flex</code> with <code>justify-content: center</code> (vertical, because flex-direction is column) and <code>align-items: center</code> (horizontal) centres the content.</li>
<li><code>min-height: 100vh</code> makes the box as tall as the screen (vh = 1% of viewport height).</li>
<li>The <b>media query</b> <code>@media (min-width: 768px)</code> changes the font size on bigger screens; this is how responsiveness is done in plain CSS.</li>
<li>Compare the amount of CSS with the next program, which does the same with Bootstrap classes.</li></ul>
"""))

P.append(WE("w1_10", "College name at the centre WITH Bootstrap (Practical 2b)", page("With Bootstrap", """
<div class="d-flex flex-column min-vh-100
  justify-content-center align-items-center
  text-center bg-light p-3">
  <h1 class="display-5 fw-bold text-primary">
    Government Polytechnic, Surat</h1>
  <h2 class="h4 my-2">
    Department of Computer Engineering</h2>
  <p class="text-muted">
    Gujarat Technological University</p>
  <a href="#" class="btn btn-primary mt-2">
    Visit Department</a>
</div>
"""),
"""The same college, department and university names in the centre of the screen on a light grey background, with a large bold blue college name and a blue "Visit Department" button. The heading size adjusts automatically to the screen width.""",
"""
<ul><li>No custom CSS is written: only Bootstrap <b>utility classes</b> are used.</li>
<li><code>d-flex flex-column justify-content-center align-items-center</code> = the flexbox centring of the previous program. <code>min-vh-100</code> = min-height: 100vh.</li>
<li><code>text-center</code>, <code>bg-light</code>, <code>p-3</code> (padding), <code>my-2</code> (vertical margin) and <code>mt-2</code> (top margin) handle alignment and spacing.</li>
<li><code>display-5</code> is a large display heading whose size is responsive; <code>fw-bold</code> = bold; <code>text-primary</code> and <code>text-muted</code> are theme colours; <code>h4</code> makes an h2 look like an h4.</li>
<li><b>Advantage:</b> faster development, consistent look, and the page is responsive by default.</li></ul>
"""))

P.append(WE("w1_11", "Responsive web page: one layout for mobile, tablet and desktop", page("Responsive Page", """
<header class="bg-primary text-white text-center p-3">
  <h1 class="h3 mb-0">Computer Engineering</h1>
</header>
<div class="container my-3">
  <div class="row g-3">
    <div class="col-12 col-sm-6 col-lg-3">
      <div class="card h-100 p-3 bg-light">
        <h5>Semester 1</h5>
        <p class="mb-0">C Programming</p>
      </div>
    </div>
    <div class="col-12 col-sm-6 col-lg-3">
      <div class="card h-100 p-3 bg-light">
        <h5>Semester 2</h5>
        <p class="mb-0">Python Programming</p>
      </div>
    </div>
    <div class="col-12 col-sm-6 col-lg-3">
      <div class="card h-100 p-3 bg-light">
        <h5>Semester 3</h5>
        <p class="mb-0">Web Page Design</p>
      </div>
    </div>
    <div class="col-12 col-sm-6 col-lg-3">
      <div class="card h-100 p-3 bg-light">
        <h5>Semester 4</h5>
        <p class="mb-0">Java Programming</p>
      </div>
    </div>
  </div>
</div>
<footer class="text-center text-muted small p-2">
  Resize the window to see 1, 2 or 4 columns
</footer>
"""),
"""A blue header "Computer Engineering", then four grey cards (Semester 1 to 4) and a footer.
On a phone (under 576 px) the cards are stacked one below the other; from 576 px they appear 2 per row; on a large screen (992 px and above, desktop view) all 4 cards sit in one row.""",
"""
<ul><li>A <b>responsive web page</b> adjusts its layout to the screen size, so it is easy to read on mobiles, tablets and desktops without zooming or horizontal scrolling.</li>
<li>Each card is in a column with three classes: <code>col-12</code> (full width on extra-small screens), <code>col-sm-6</code> (half width from 576 px) and <code>col-lg-3</code> (quarter width from 992 px).</li>
<li>The grid has 12 columns per row: 12 = 1 card per row, 6 = 2 cards, 3 = 4 cards.</li>
<li><code>g-3</code> adds a gap (gutter) between columns; <code>h-100</code> makes all cards in a row the same height.</li>
<li>Bootstrap is <b>mobile first</b>: the smallest-screen class is written first, and larger breakpoints override it.</li></ul>
"""))

P.append(WE("w1_12", "How to remove responsiveness (fixed-width page)", page("Non-responsive", """
<div class="container">
  <h1 class="h3 my-3">Non-responsive page</h1>
  <div class="row">
    <div class="col-4">
      <div class="p-3 bg-warning">Column 1</div>
    </div>
    <div class="col-4">
      <div class="p-3 bg-info">Column 2</div>
    </div>
    <div class="col-4">
      <div class="p-3 bg-success text-white">
        Column 3</div>
    </div>
  </div>
  <p class="mt-3">The page is always 970 px wide.
    On a phone it is zoomed out or scrolls
    sideways.</p>
</div>
""", style="""
/* 2. fixed width for the container */
.container {
  width: 970px !important;
  max-width: none !important;
}
""", head="<!-- 1. no viewport meta tag -->", viewport=False),
"""The page is always 970 px wide with three coloured columns (yellow, light blue, green) side by side in one row.
On a phone the three columns do not stack: the whole page appears zoomed out (or must be scrolled sideways), like an old desktop-only website.""",
"""
<p>Sometimes a fixed desktop layout is required (e.g. an admin panel or a printed report). Steps to <b>disable responsiveness</b> in Bootstrap:</p>
<ol><li><b>Remove</b> (or do not add) the <code>&lt;meta name="viewport"&gt;</code> tag. The phone browser then renders the page at about 980 px and zooms it out.</li>
<li>Give <code>.container</code> a <b>fixed width</b> and override <code>max-width</code> with <code>!important</code>.</li>
<li>Use grid classes <b>without breakpoints</b> (<code>col-4</code>, not <code>col-md-4</code>), so columns never stack.</li>
<li>For a navbar, do not use the collapse/toggler; keep the menu always expanded.</li></ol>
<p>Compare with the previous program, where the cards rearrange themselves on small screens.</p>
"""))

P.append(WE("w1_13", "Major features of Bootstrap on one page", page("Bootstrap Features", """
<div class="container py-3">
  <h1 class="h3">Bootstrap Features
    <span class="badge bg-danger">New</span></h1>
  <p class="text-muted">Typography, colours,
    components and icons</p>

  <div class="row g-2 mb-3">
    <div class="col-6 col-md-3">
      <div class="p-2 bg-primary text-white">
        Grid 1</div></div>
    <div class="col-6 col-md-3">
      <div class="p-2 bg-success text-white">
        Grid 2</div></div>
    <div class="col-6 col-md-3">
      <div class="p-2 bg-warning">Grid 3</div></div>
    <div class="col-6 col-md-3">
      <div class="p-2 bg-info">Grid 4</div></div>
  </div>

  <button class="btn btn-primary">
    <i class="bi bi-download"></i> Download</button>
  <button class="btn btn-outline-success">
    <i class="bi bi-check-circle"></i> Save</button>

  <div class="alert alert-warning alert-dismissible
    fade show mt-3">
    <i class="bi bi-exclamation-triangle"></i>
    Exam form last date: 30 November.
    <button type="button" class="btn-close"
      data-bs-dismiss="alert"></button>
  </div>

  <div class="card">
    <div class="card-body">
      <h5 class="card-title">Card component</h5>
      <input class="form-control mb-2"
        placeholder="Styled form control">
      <div class="progress">
        <div class="progress-bar" style="width:70%">
          70%</div>
      </div>
    </div>
  </div>
</div>
""", icons=True, bs_js=True),
"""One page showing many features: a heading with a red "New" badge, four coloured grid boxes (2 per row on a phone, 4 per row from 768 px), a blue Download button and a green outlined Save button with icons, a yellow warning alert with a close (x) button that removes it, and a card containing a styled input box and a blue progress bar at 70%.""",
"""
<ul><li><b>Responsive grid</b>: <code>row</code> + <code>col-6 col-md-3</code>.</li>
<li><b>Typography and colours</b>: headings, <code>text-muted</code>, contextual colours like primary, success, warning, info, danger.</li>
<li><b>Components</b>: badge, buttons, alert, card, form control and progress bar, ready to use with classes only.</li>
<li><b>JavaScript plug-ins</b>: the dismissible alert closes because of <code>data-bs-dismiss="alert"</code> and bootstrap.bundle.min.js.</li>
<li><b>Icons</b>: Bootstrap Icons (<code>&lt;i class="bi bi-download"&gt;</code>) replace the Glyphicons of Bootstrap 3.</li>
<li>Everything is cross-browser and mobile first.</li></ul>
"""))

P.append(WE("w1_14", "jQuery with Bootstrap: dynamic alerts and dark mode", page("jQuery + Bootstrap", """
<div class="container py-3">
  <div class="d-flex justify-content-between
    align-items-center mb-3">
    <h1 class="h4 mb-0">Notice Board</h1>
    <div class="form-check form-switch">
      <input class="form-check-input"
        type="checkbox" id="dark">
      <label class="form-check-label" for="dark">
        Dark mode</label>
    </div>
  </div>
  <div class="input-group mb-3">
    <input id="txt" class="form-control"
      placeholder="Type a notice">
    <select id="type" class="form-select"
      style="max-width:120px">
      <option value="info">Info</option>
      <option value="success">Success</option>
      <option value="danger">Urgent</option>
    </select>
    <button id="post" class="btn btn-primary">
      Post</button>
  </div>
  <div id="notices"></div>
</div>
""", script="""
$(function () {
  $("#post").click(function () {
    var t = $("#txt").val().trim();
    if (t === "") return;
    var c = $("#type").val();
    $("#notices").prepend(
      '<div class="alert alert-' + c +
      ' alert-dismissible fade show">' + t +
      '<button class="btn-close"' +
      ' data-bs-dismiss="alert"></button></div>');
    $("#txt").val("");
  });

  $("#dark").change(function () {
    var mode = this.checked ? "dark" : "light";
    $("html").attr("data-bs-theme", mode);
  });
});
""", jquery=True, bs_js=True),
"""A "Notice Board" heading with a Dark mode switch, and an input box with a type list (Info / Success / Urgent) and a Post button.
Typing "Practical exam on Monday", choosing Urgent and pressing Post adds a red alert with a close (x) button at the top of the list; Info gives a light blue alert and Success a green one.
Turning on the switch changes the whole page to dark colours.""",
"""
<ul><li>jQuery and Bootstrap work well together: jQuery handles events and creates elements, Bootstrap provides the styling.</li>
<li>The new alert is built as an HTML string with the class <code>alert-info</code>, <code>alert-success</code> or <code>alert-danger</code> from the select box, and inserted with <code>prepend()</code>.</li>
<li>The close button works even for alerts added later, because Bootstrap listens for <code>data-bs-dismiss</code> clicks on the whole document.</li>
<li><code>.attr("data-bs-theme", "dark")</code> on the &lt;html&gt; element switches Bootstrap 5.3 to its dark colour mode.</li>
<li>Bootstrap 5 itself does not need jQuery (Bootstrap 3 and 4 did); jQuery is added here only for our own script.</li></ul>
""", actions="$('#txt').val('Practical exam on Monday'); $('#type').val('danger'); $('#post').click(); $('#txt').val('Library open till 6 pm'); $('#type').val('info'); $('#post').click()"))

PROGRAMS = P
