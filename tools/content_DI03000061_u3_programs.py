"""DI03000061 RWPD Unit 3 – Bootstrap components (practicals 9-17)."""
from web_content import WE, page

P = []

# ------------------------------------------------------------------ 3.1
P.append(WE("w3_1", "Bootstrap Icons (replacement of Glyphicons)", page("Icons", """
<div class="container py-3">
  <h1 class="h4"><i class="bi bi-bootstrap-fill text-primary"></i>
    Bootstrap Icons</h1>

  <p class="fs-3">
    <i class="bi bi-house"></i>
    <i class="bi bi-person-circle"></i>
    <i class="bi bi-envelope"></i>
    <i class="bi bi-telephone"></i>
    <i class="bi bi-search"></i>
    <i class="bi bi-cart3"></i>
  </p>

  <h2 class="h6">Size and colour</h2>
  <p>
    <i class="bi bi-heart-fill text-danger fs-6"></i>
    <i class="bi bi-heart-fill text-danger fs-4"></i>
    <i class="bi bi-heart-fill text-danger fs-1"></i>
    <i class="bi bi-star-fill text-warning"
      style="font-size: 3rem;"></i>
  </p>

  <h2 class="h6">Icons in buttons</h2>
  <button class="btn btn-primary">
    <i class="bi bi-download"></i> Download</button>
  <button class="btn btn-success">
    <i class="bi bi-check-lg"></i> Save</button>
  <button class="btn btn-danger">
    <i class="bi bi-trash"></i> Delete</button>
  <button class="btn btn-outline-dark" aria-label="Settings">
    <i class="bi bi-gear"></i></button>

  <h2 class="h6 mt-3">Icons in a list</h2>
  <ul class="list-unstyled">
    <li><i class="bi bi-geo-alt-fill text-danger"></i>
      Surat, Gujarat</li>
    <li><i class="bi bi-clock text-primary"></i>
      10:30 am to 5:00 pm</li>
    <li><i class="bi bi-wifi text-success"></i> Free Wi-Fi</li>
  </ul>
</div>
""", icons=True),
"""A heading with a blue Bootstrap logo icon, then a large row of icons: house, person, envelope, telephone, search and cart.
Four red/yellow icons in increasing sizes, buttons with icons (Download, Save, Delete and a gear-only button), and a list with a red location pin, a blue clock and a green Wi-Fi icon.""",
"""
<ul><li><b>Glyphicons</b> (the icon font of Bootstrap 3) were removed in Bootstrap 4. Bootstrap 5 uses the separate, free <b>Bootstrap Icons</b> library (2000+ icons).</li>
<li>Install: link <code>bootstrap-icons.min.css</code> (local file or CDN <code>cdn.jsdelivr.net/npm/bootstrap-icons</code>).</li>
<li>Use: <code>&lt;i class="bi bi-house"&gt;&lt;/i&gt;</code>. Bootstrap 3 syntax was <code>&lt;span class="glyphicon glyphicon-home"&gt;&lt;/span&gt;</code>.</li>
<li>Icons are font characters, so <b>size</b> follows font-size (<code>fs-1</code> ... <code>fs-6</code> or CSS) and <b>colour</b> follows text colour (<code>text-danger</code>).</li>
<li>Many icons have a <code>-fill</code> version (bi-heart / bi-heart-fill).</li>
<li>For an icon-only button add <code>aria-label</code> so screen readers can describe it.</li></ul>
"""))

P.append(WE("w3_2", "Dropdown menus: right aligned, drop up, headers, dividers (Practical 9)", page("Dropdown Menus", """
<div class="container py-3">
  <h1 class="h5">Dropdown menus</h1>
  <div class="d-flex flex-wrap gap-2 mb-3">
    <div class="dropdown">
      <button class="btn btn-primary dropdown-toggle" type="button"
        data-bs-toggle="dropdown">Courses</button>
      <ul class="dropdown-menu">
        <li><h6 class="dropdown-header">Diploma</h6></li>
        <li><a class="dropdown-item" href="#">
          <i class="bi bi-pc-display"></i> Computer</a></li>
        <li><a class="dropdown-item active" href="#">
          <i class="bi bi-cpu"></i> IT</a></li>
        <li><hr class="dropdown-divider"></li>
        <li><h6 class="dropdown-header">Degree</h6></li>
        <li><a class="dropdown-item" href="#">B.E.</a></li>
        <li><a class="dropdown-item disabled">M.E. (soon)</a></li>
      </ul>
    </div>

    <div class="btn-group">
      <button class="btn btn-success">Split</button>
      <button class="btn btn-success dropdown-toggle
        dropdown-toggle-split" data-bs-toggle="dropdown"></button>
      <ul class="dropdown-menu">
        <li><a class="dropdown-item" href="#">Action</a></li>
        <li><a class="dropdown-item" href="#">Another</a></li>
      </ul>
    </div>

    <div class="dropup">
      <button class="btn btn-warning dropdown-toggle"
        data-bs-toggle="dropdown">Drop up</button>
      <ul class="dropdown-menu">
        <li><a class="dropdown-item" href="#">Item 1</a></li>
        <li><a class="dropdown-item" href="#">Item 2</a></li>
      </ul>
    </div>
  </div>

  <div class="d-flex justify-content-end">
    <div class="dropdown">
      <button class="btn btn-dark dropdown-toggle"
        data-bs-toggle="dropdown">
        <i class="bi bi-person-circle"></i> Account</button>
      <ul class="dropdown-menu dropdown-menu-end
        dropdown-menu-dark">
        <li><a class="dropdown-item" href="#">
          <i class="bi bi-person"></i> Profile</a></li>
        <li><a class="dropdown-item" href="#">
          <i class="bi bi-gear"></i> Settings</a></li>
        <li><hr class="dropdown-divider"></li>
        <li><a class="dropdown-item" href="#">
          <i class="bi bi-box-arrow-right"></i> Logout</a></li>
      </ul>
    </div>
  </div>
</div>
""", icons=True, bs_js=True),
"""Three buttons: "Courses", a split button "Split" with a separate arrow part, and a yellow "Drop up". A black "Account" button sits at the right edge below them.
Tapping Courses opens a menu with grey headers "Diploma" and "Degree", items with icons, IT highlighted in blue (active), a divider line and a greyed-out disabled item. Drop up opens its menu above the button. The Account menu is dark and right-aligned with the button (it does not go off the screen), with Profile, Settings and Logout.""",
"""
<ul><li>A dropdown needs a wrapper (<code>.dropdown</code> or <code>.btn-group</code>), a toggle button with <code>.dropdown-toggle</code> and <code>data-bs-toggle="dropdown"</code>, and a <code>ul.dropdown-menu</code> with <code>.dropdown-item</code> links. bootstrap.bundle.min.js (with Popper) makes it work.</li>
<li><b>Headers:</b> <code>h6.dropdown-header</code>. <b>Dividers:</b> <code>hr.dropdown-divider</code>. <b>States:</b> <code>.active</code> and <code>.disabled</code> on items.</li>
<li><b>Right-aligned menu:</b> <code>.dropdown-menu-end</code> (Bootstrap 3: .dropdown-menu-right / pull-right).</li>
<li><b>Direction:</b> <code>.dropup</code>, <code>.dropend</code>, <code>.dropstart</code>. <b>Dark menu:</b> <code>.dropdown-menu-dark</code>.</li>
<li><b>Split button:</b> a normal button plus a <code>.dropdown-toggle-split</code> toggle inside a <code>.btn-group</code>.</li>
<li>Icons (<code>bi bi-*</code>) can be added to items, as glyphicons were used in Bootstrap 3.</li></ul>
""", actions="bootstrap.Dropdown.getOrCreateInstance(document.querySelector('.dropdown .dropdown-toggle')).show()"))

P.append(WE("w3_3", "Card component", page("Cards", """
<div class="container py-3">
  <div class="row row-cols-1 row-cols-md-3 g-3">
    <div class="col">
      <div class="card h-100">
        <img src="images/python.jpg" class="card-img-top"
          alt="Python">
        <div class="card-body">
          <h5 class="card-title">Python Course</h5>
          <p class="card-text">Learn Python from basics to
            projects in 8 weeks.</p>
          <a href="#" class="btn btn-primary">Enroll</a>
        </div>
      </div>
    </div>
    <div class="col">
      <div class="card h-100 text-center">
        <div class="card-header">Featured</div>
        <div class="card-body">
          <h5 class="card-title">Web Design</h5>
          <h6 class="card-subtitle mb-2 text-muted">
            HTML, CSS, Bootstrap</h6>
          <p class="card-text">Build responsive sites.</p>
          <a href="#" class="card-link">Details</a>
          <a href="#" class="card-link">Syllabus</a>
        </div>
        <div class="card-footer text-muted">Starts 1 Dec</div>
      </div>
    </div>
    <div class="col">
      <div class="card h-100 text-bg-success">
        <div class="card-body">
          <h5 class="card-title">
            <i class="bi bi-trophy"></i> Results</h5>
          <p class="card-text">98% students passed in
            summer 2026.</p>
        </div>
      </div>
    </div>
  </div>

  <div class="card mt-3">
    <div class="row g-0">
      <div class="col-4">
        <img src="images/teacher.jpg" alt="Teacher"
          width="300" height="300"
          class="img-fluid rounded-start h-100 object-fit-cover">
      </div>
      <div class="col-8">
        <div class="card-body">
          <h5 class="card-title">Horizontal card</h5>
          <p class="card-text">Image on the left using the
            grid inside a card.</p>
        </div>
      </div>
    </div>
  </div>

  <div class="card border-danger mt-3">
    <ul class="list-group list-group-flush">
      <li class="list-group-item">Card with a list group</li>
      <li class="list-group-item">border-danger</li>
    </ul>
  </div>
</div>
""", icons=True),
"""Three cards (stacked on a phone, side by side from 768 px, all the same height): a course card with an image on top, title, text and an Enroll button; a centred card with a "Featured" header, subtitle, two links and a footer "Starts 1 Dec"; and a green card with a trophy icon.
Below are a horizontal card with an image on the left and text on the right, and a red-bordered card containing a list.""",
"""
<ul><li>A <b>card</b> is a flexible content box with optional header, body, footer, images and lists. In Bootstrap 4/5 it replaced <b>panels, wells and thumbnails</b> of Bootstrap 3.</li>
<li>Parts: <code>.card</code> &gt; <code>.card-header</code>, <code>.card-body</code> (<code>.card-title</code>, <code>.card-subtitle</code>, <code>.card-text</code>, <code>.card-link</code>), <code>.card-footer</code>.</li>
<li><b>Images:</b> <code>.card-img-top</code>, <code>.card-img-bottom</code>, or <code>.card-img-overlay</code> for text over an image.</li>
<li><b>Colours:</b> <code>.text-bg-success</code> (background + matching text), <code>.border-danger</code>.</li>
<li><b>Layouts:</b> cards in a grid (<code>row-cols-md-3</code>) with <code>h-100</code> for equal heights; <code>.card-group</code> joins cards; a horizontal card uses <code>.row.g-0</code> inside the card.</li>
<li><code>.list-group-flush</code> removes outer borders of a list inside a card.</li></ul>
"""))

P.append(WE("w3_4", "Button groups and button toolbar", page("Button Groups", """
<div class="container py-3">
  <h1 class="h6">1. Basic button group</h1>
  <div class="btn-group mb-3" role="group">
    <button class="btn btn-primary">Left</button>
    <button class="btn btn-primary">Middle</button>
    <button class="btn btn-primary">Right</button>
  </div>

  <h2 class="h6">2. Sizes</h2>
  <div class="btn-group btn-group-lg mb-1">
    <button class="btn btn-outline-dark">Large</button>
    <button class="btn btn-outline-dark">Group</button>
  </div><br>
  <div class="btn-group btn-group-sm mb-3">
    <button class="btn btn-outline-dark">Small</button>
    <button class="btn btn-outline-dark">Group</button>
  </div>

  <h2 class="h6">3. Toolbar (groups in a row)</h2>
  <div class="btn-toolbar mb-3" role="toolbar">
    <div class="btn-group me-2">
      <button class="btn btn-secondary">1</button>
      <button class="btn btn-secondary">2</button>
      <button class="btn btn-secondary">3</button>
    </div>
    <div class="btn-group me-2">
      <button class="btn btn-info"><i class="bi bi-type-bold"></i>
      </button>
      <button class="btn btn-info"><i class="bi bi-type-italic"></i>
      </button>
    </div>
    <div class="btn-group">
      <button class="btn btn-success">Save</button>
    </div>
  </div>

  <h2 class="h6">4. Vertical group and nested dropdown</h2>
  <div class="d-flex gap-3 align-items-start">
    <div class="btn-group-vertical">
      <button class="btn btn-warning">Top</button>
      <button class="btn btn-warning">Middle</button>
      <button class="btn btn-warning">Bottom</button>
    </div>
    <div class="btn-group">
      <button class="btn btn-danger">Home</button>
      <div class="btn-group">
        <button class="btn btn-danger dropdown-toggle"
          data-bs-toggle="dropdown">More</button>
        <ul class="dropdown-menu">
          <li><a class="dropdown-item" href="#">About</a></li>
          <li><a class="dropdown-item" href="#">Contact</a></li>
        </ul>
      </div>
    </div>
  </div>

  <h2 class="h6 mt-3">5. Radio toggle group</h2>
  <div class="btn-group">
    <input type="radio" class="btn-check" name="v" id="v1"
      checked>
    <label class="btn btn-outline-primary" for="v1">Day</label>
    <input type="radio" class="btn-check" name="v" id="v2">
    <label class="btn btn-outline-primary" for="v2">Week</label>
    <input type="radio" class="btn-check" name="v" id="v3">
    <label class="btn btn-outline-primary" for="v3">Month</label>
  </div>
</div>
""", icons=True, bs_js=True),
"""1. Three blue buttons joined together (only the outer corners rounded).
2. A large and a small joined pair.
3. A toolbar: a group 1-2-3, a group with bold and italic icons, and a Save button, with gaps between the groups.
4. Three yellow buttons stacked vertically, and a red Home button joined with a "More" dropdown.
5. A Day / Week / Month selector where only one can be selected (Day is highlighted).""",
"""
<ul><li><b>.btn-group</b> joins buttons in one line. Add <code>role="group"</code> for accessibility.</li>
<li>Sizes for the whole group: <code>.btn-group-lg</code>, <code>.btn-group-sm</code>.</li>
<li><b>.btn-toolbar</b> combines several button groups in one row; spacing between groups with margin utilities (<code>me-2</code>).</li>
<li><b>.btn-group-vertical</b> stacks buttons vertically.</li>
<li><b>Nesting:</b> a <code>.btn-group</code> containing a dropdown can be placed inside another button group.</li>
<li><b>Checkbox / radio buttons:</b> hidden <code>input.btn-check</code> followed by a <code>label.btn</code>; radios with the same name allow one choice.</li></ul>
"""))

P.append(WE("w3_5", "Odd and even semester menu using button groups and toolbar (Practical 10)", page("Semester Menu", """
<div class="container py-3">
  <h1 class="h4 text-center mb-3">Computer Engineering</h1>

  <div class="btn-toolbar justify-content-center gap-2"
    role="toolbar">
    <div class="btn-group flex-wrap" role="group">
      <span class="btn btn-dark disabled">Odd</span>
      <div class="btn-group">
        <button class="btn btn-primary dropdown-toggle"
          data-bs-toggle="dropdown">Sem 1</button>
        <ul class="dropdown-menu">
          <li><a class="dropdown-item" href="#">Maths 1</a></li>
          <li><a class="dropdown-item" href="#">C Programming</a></li>
          <li><a class="dropdown-item" href="#">Physics</a></li>
        </ul>
      </div>
      <div class="btn-group">
        <button class="btn btn-primary dropdown-toggle"
          data-bs-toggle="dropdown">Sem 3</button>
        <ul class="dropdown-menu">
          <li><a class="dropdown-item" href="#">Data Structures</a></li>
          <li><a class="dropdown-item" href="#">RDBMS</a></li>
          <li><a class="dropdown-item" href="#">RWPD</a></li>
        </ul>
      </div>
      <div class="btn-group">
        <button class="btn btn-primary dropdown-toggle"
          data-bs-toggle="dropdown">Sem 5</button>
        <ul class="dropdown-menu">
          <li><a class="dropdown-item" href="#">Java</a></li>
          <li><a class="dropdown-item" href="#">Cloud</a></li>
        </ul>
      </div>
    </div>

    <div class="btn-group flex-wrap" role="group">
      <span class="btn btn-dark disabled">Even</span>
      <div class="btn-group">
        <button class="btn btn-success dropdown-toggle"
          data-bs-toggle="dropdown">Sem 2</button>
        <ul class="dropdown-menu">
          <li><a class="dropdown-item" href="#">Python</a></li>
          <li><a class="dropdown-item" href="#">Electronics</a></li>
        </ul>
      </div>
      <div class="btn-group">
        <button class="btn btn-success dropdown-toggle"
          data-bs-toggle="dropdown">Sem 4</button>
        <ul class="dropdown-menu">
          <li><a class="dropdown-item" href="#">OOP with Java</a></li>
          <li><a class="dropdown-item" href="#">Web Dev</a></li>
        </ul>
      </div>
      <div class="btn-group">
        <button class="btn btn-success dropdown-toggle"
          data-bs-toggle="dropdown">Sem 6</button>
        <ul class="dropdown-menu dropdown-menu-end">
          <li><a class="dropdown-item" href="#">Project</a></li>
          <li><a class="dropdown-item" href="#">Mobile Apps</a></li>
        </ul>
      </div>
    </div>
  </div>
  <p class="text-center mt-3" id="pick">Select a course</p>
</div>
""", script="""
var items = document.querySelectorAll(".dropdown-item");
items.forEach(function (a) {
  a.addEventListener("click", function (e) {
    e.preventDefault();
    var sem = a.closest(".btn-group")
               .querySelector(".dropdown-toggle").textContent;
    document.getElementById("pick").textContent =
      sem.trim() + " : " + a.textContent;
  });
});
""", bs_js=True),
"""Two joined button groups in a toolbar: "Odd | Sem 1 | Sem 3 | Sem 5" in blue and "Even | Sem 2 | Sem 4 | Sem 6" in green (on a phone the second group moves to the next line).
Each semester button opens a submenu with its courses. Choosing a course, e.g. RDBMS under Sem 3, shows "Sem 3 : RDBMS" below the menu.""",
"""
<ul><li>The <b>button toolbar</b> (<code>.btn-toolbar</code>) holds two <b>button groups</b>: odd and even semesters. <code>justify-content-center gap-2</code> centres them with a gap.</li>
<li>Each semester is a <b>nested button group</b> containing a dropdown toggle and a <code>.dropdown-menu</code> (the submenu of courses).</li>
<li>The "Odd" / "Even" labels are disabled buttons used as titles.</li>
<li><code>flex-wrap</code> lets buttons wrap on narrow screens, keeping the page responsive.</li>
<li>The small script uses <code>closest()</code> to find the semester of the clicked course and shows the choice.</li></ul>
""", actions="document.querySelectorAll('.dropdown-item')[4].click()"))

P.append(WE("w3_6", "Input groups: job application form (Practical 11)", page("Job Application", """
<div class="container py-3" style="max-width: 640px;">
  <h1 class="h4 mb-3">Job Application</h1>
  <form>
    <div class="input-group mb-2">
      <span class="input-group-text"><i class="bi bi-person"></i></span>
      <input class="form-control" placeholder="First name">
      <input class="form-control" placeholder="Last name">
    </div>
    <div class="input-group mb-2">
      <span class="input-group-text">@</span>
      <input type="email" class="form-control"
        placeholder="email">
      <span class="input-group-text">.com</span>
    </div>
    <div class="input-group mb-2">
      <span class="input-group-text">+91</span>
      <input type="tel" class="form-control"
        placeholder="Mobile number">
    </div>
    <div class="input-group mb-2">
      <span class="input-group-text">Expected salary Rs.</span>
      <input type="number" class="form-control">
      <span class="input-group-text">.00</span>
    </div>
    <div class="input-group mb-2">
      <label class="input-group-text" for="post">Post</label>
      <select class="form-select" id="post">
        <option>Web Developer</option>
        <option>Tester</option>
      </select>
    </div>
    <div class="input-group mb-2">
      <div class="input-group-text">
        <input class="form-check-input mt-0" type="checkbox"
          checked>
      </div>
      <input class="form-control" value="Ready to relocate">
    </div>
    <div class="input-group mb-2">
      <input type="file" class="form-control" id="cv">
      <label class="input-group-text" for="cv">Upload CV</label>
    </div>
    <div class="input-group input-group-sm mb-2">
      <span class="input-group-text">Portfolio</span>
      <input class="form-control" placeholder="https://">
      <button class="btn btn-outline-secondary" type="button">
        Check</button>
    </div>
    <div class="input-group mb-3">
      <span class="input-group-text">Cover letter</span>
      <textarea class="form-control" rows="2"></textarea>
    </div>
    <button class="btn btn-primary w-100">
      <i class="bi bi-send"></i> Apply</button>
  </form>
</div>
""", icons=True),
"""A "Job Application" form in which every field has a grey attached part: a person icon before first and last name, "@" and ".com" around the email, "+91" before the mobile number, "Expected salary Rs." and ".00" around the salary, "Post" before a drop-down, a checkbox before "Ready to relocate", an "Upload CV" label after the file input, a small "Portfolio" field with a Check button, and a "Cover letter" box. A full-width blue Apply button is at the bottom.""",
"""
<ul><li>An <b>input group</b> attaches text, icons, buttons, checkboxes or selects to the sides of a form control: wrapper <code>.input-group</code>, addon <code>.input-group-text</code>.</li>
<li>Addons can be placed <b>before</b>, <b>after</b> or on <b>both sides</b>; several inputs can share one group (first + last name).</li>
<li>Sizes: <code>.input-group-sm</code>, <code>.input-group-lg</code>.</li>
<li>A <b>checkbox or radio</b> goes inside <code>.input-group-text</code> with <code>.mt-0</code>.</li>
<li><b>Buttons</b> and <b>dropdowns</b> can be put directly in the group; <code>.form-select</code> and file inputs also work.</li>
<li>Bootstrap 3/4 used <code>.input-group-addon</code> / <code>.input-group-prepend</code>; Bootstrap 5 uses only <code>.input-group-text</code>.</li></ul>
"""))

# ------------------------------------------------------------------ 3.2 Navs and navbar
P.append(WE("w3_7", "Navigation tabs and pills", page("Navs", """
<div class="container py-3">
  <h1 class="h6">1. Base nav</h1>
  <ul class="nav mb-3">
    <li class="nav-item"><a class="nav-link active" href="#">Home</a></li>
    <li class="nav-item"><a class="nav-link" href="#">Notes</a></li>
    <li class="nav-item"><a class="nav-link disabled">Soon</a></li>
  </ul>

  <h2 class="h6">2. Tabs</h2>
  <ul class="nav nav-tabs mb-3">
    <li class="nav-item"><a class="nav-link active" href="#">Unit 1</a></li>
    <li class="nav-item"><a class="nav-link" href="#">Unit 2</a></li>
    <li class="nav-item"><a class="nav-link" href="#">Unit 3</a></li>
  </ul>

  <h2 class="h6">3. Pills, justified (equal width)</h2>
  <ul class="nav nav-pills nav-justified mb-3">
    <li class="nav-item"><a class="nav-link active" href="#">Day</a></li>
    <li class="nav-item"><a class="nav-link" href="#">Week</a></li>
    <li class="nav-item"><a class="nav-link" href="#">Month</a></li>
  </ul>

  <h2 class="h6">4. Centred pills and underline</h2>
  <ul class="nav nav-pills justify-content-center mb-2">
    <li class="nav-item"><a class="nav-link" href="#">A</a></li>
    <li class="nav-item"><a class="nav-link active" href="#">B</a></li>
    <li class="nav-item"><a class="nav-link" href="#">C</a></li>
  </ul>
  <ul class="nav nav-underline justify-content-end mb-3">
    <li class="nav-item"><a class="nav-link active" href="#">New</a></li>
    <li class="nav-item"><a class="nav-link" href="#">Popular</a></li>
  </ul>

  <h2 class="h6">5. Vertical pills</h2>
  <ul class="nav nav-pills flex-column" style="max-width: 200px;">
    <li class="nav-item"><a class="nav-link active" href="#">
      <i class="bi bi-speedometer2"></i> Dashboard</a></li>
    <li class="nav-item"><a class="nav-link" href="#">
      <i class="bi bi-people"></i> Students</a></li>
    <li class="nav-item"><a class="nav-link" href="#">
      <i class="bi bi-gear"></i> Settings</a></li>
  </ul>
</div>
""", icons=True),
"""1. Plain links Home (active), Notes and a greyed-out Soon.
2. Folder-style tabs Unit 1, Unit 2, Unit 3 with Unit 1 selected.
3. Three pill buttons filling the full width with Day in blue.
4. Centred pills with B selected, then right-aligned underline links with New underlined.
5. A vertical menu of pills: Dashboard (blue), Students and Settings, with icons.""",
"""
<ul><li>A base nav is <code>ul.nav</code> &gt; <code>li.nav-item</code> &gt; <code>a.nav-link</code>; <code>.active</code> marks the current item and <code>.disabled</code> greys it out.</li>
<li><b>Tabs:</b> <code>.nav-tabs</code>. <b>Pills:</b> <code>.nav-pills</code>. <b>Underline:</b> <code>.nav-underline</code> (Bootstrap 5.3).</li>
<li><b>Fill and justify:</b> <code>.nav-fill</code> stretches items to fill the width; <code>.nav-justified</code> makes them equal width.</li>
<li><b>Alignment:</b> flex utilities <code>justify-content-center</code> / <code>justify-content-end</code>.</li>
<li><b>Vertical:</b> <code>.flex-column</code> (or <code>flex-sm-row</code> to be vertical only on phones).</li>
<li>These navs only look like tabs. To switch content when clicked, the tab plug-in is used (next program).</li></ul>
"""))

P.append(WE("w3_8", "Course unit summary using tabs and pills (Practical 12)", page("Unit Summary", """
<div class="container py-3">
  <h1 class="h4">Responsive Web Page Design</h1>
  <ul class="nav nav-tabs" role="tablist">
    <li class="nav-item">
      <button class="nav-link active" data-bs-toggle="tab"
        data-bs-target="#u1" type="button">Unit 1</button></li>
    <li class="nav-item">
      <button class="nav-link" data-bs-toggle="tab"
        data-bs-target="#u2" type="button">Unit 2</button></li>
    <li class="nav-item">
      <button class="nav-link" data-bs-toggle="tab"
        data-bs-target="#u3" type="button">Unit 3</button></li>
  </ul>
  <div class="tab-content border border-top-0 p-3 mb-4">
    <div class="tab-pane fade show active" id="u1">
      <h2 class="h5">jQuery and Bootstrap Intro</h2>
      <p>Selectors, events, Bootstrap setup, responsive page.</p>
    </div>
    <div class="tab-pane fade" id="u2">
      <h2 class="h5">Bootstrap Grid</h2>
      <p>Containers, offset, ordering, nesting, forms.</p>
    </div>
    <div class="tab-pane fade" id="u3">
      <h2 class="h5">Components</h2>
      <p>Cards, navbar, alerts, progress bars, list group.</p>
    </div>
  </div>

  <div class="row">
    <div class="col-md-3 mb-2">
      <div class="nav flex-md-column nav-pills" role="tablist">
        <button class="nav-link active" data-bs-toggle="pill"
          data-bs-target="#p4" type="button">Unit 4</button>
        <button class="nav-link" data-bs-toggle="pill"
          data-bs-target="#p5" type="button">Unit 5</button>
      </div>
    </div>
    <div class="col-md-9">
      <div class="tab-content bg-light p-3 rounded">
        <div class="tab-pane fade show active" id="p4">
          <h2 class="h5">Plug-ins</h2>
          <p>Modal, tooltip, popover, collapse, carousel.</p>
        </div>
        <div class="tab-pane fade" id="p5">
          <h2 class="h5">Utilities and Customisation</h2>
          <p>Spacing, flex, colours, Sass variables, themes.</p>
        </div>
      </div>
    </div>
  </div>
</div>
""", bs_js=True),
"""Tabs Unit 1, Unit 2, Unit 3 above a bordered box. Unit 1's summary is shown first; tapping Unit 2 or Unit 3 fades in that unit's summary instead.
Below are pills Unit 4 and Unit 5 (side by side on a phone, a vertical list on the left on a desktop) with a grey content box that changes when a pill is tapped.""",
"""
<ul><li>The <b>tab plug-in</b> switches content: each nav button has <code>data-bs-toggle="tab"</code> (or <code>"pill"</code>) and <code>data-bs-target="#id"</code> pointing to a <code>.tab-pane</code>.</li>
<li>Panes are inside <code>.tab-content</code>. The first pane has <code>.show .active</code>; <code>.fade</code> adds a fade animation.</li>
<li>Vertical pills: <code>.flex-md-column</code> makes the pill list vertical from 768 px, inside a grid column next to the content.</li>
<li>Using &lt;button&gt; for the nav links is recommended for accessibility; <code>role="tablist"</code> describes the purpose.</li>
<li>Tabs can also be switched from JavaScript: <code>bootstrap.Tab.getOrCreateInstance(el).show()</code>.</li></ul>
""", actions="document.querySelector('[data-bs-target=\"#u2\"]').click()"))

P.append(WE("w3_9", "Responsive navbar with collapse", page("Navbar", """
<nav class="navbar navbar-expand-lg bg-primary" data-bs-theme="dark">
  <div class="container-fluid">
    <a class="navbar-brand" href="#">
      <i class="bi bi-mortarboard-fill"></i> GP Surat</a>
    <button class="navbar-toggler" type="button"
      data-bs-toggle="collapse" data-bs-target="#menu"
      aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="menu">
      <ul class="navbar-nav me-auto">
        <li class="nav-item">
          <a class="nav-link active" href="#">Home</a></li>
        <li class="nav-item">
          <a class="nav-link" href="#">Departments</a></li>
        <li class="nav-item">
          <a class="nav-link" href="#">Admission</a></li>
      </ul>
      <span class="navbar-text">Helpline: 0261-2240000</span>
    </div>
  </div>
</nav>
<div class="container py-3">
  <p>On small screens the menu collapses into the
    <b>hamburger</b> button. Tap it to open the menu.</p>
  <p>From 992 px (lg) the full menu is shown.</p>
</div>
""", icons=True, bs_js=True),
"""A blue navigation bar with the brand "GP Surat" and a graduation cap icon.
On a phone only the brand and a three-line (hamburger) button are visible; tapping the button slides down the menu Home, Departments, Admission and the helpline text. On a desktop (992 px and wider) all links appear in one line, with the helpline text at the right.""",
"""
<ul><li><code>nav.navbar</code> + <b>.navbar-expand-lg</b>: the menu is expanded from lg upward and collapsed below it (other options: -sm, -md, -xl, or <code>.navbar-expand</code> to never collapse).</li>
<li><b>.navbar-brand</b>: the logo/name. <b>.navbar-nav</b> with <b>.nav-link</b>: the menu links. <b>.navbar-text</b>: plain text.</li>
<li><b>.navbar-toggler</b> with <code>data-bs-toggle="collapse"</code> and <code>data-bs-target="#menu"</code> opens and closes the <code>.collapse.navbar-collapse</code> part.</li>
<li><code>.me-auto</code> on the links pushes the following content to the right.</li>
<li><b>Colours:</b> a background class (<code>bg-primary</code>, <code>bg-dark</code>, <code>bg-body-tertiary</code>) plus <code>data-bs-theme="dark"</code> for light text (Bootstrap 3/4: navbar-inverse / navbar-dark).</li></ul>
""", actions="document.querySelector('.navbar-toggler').click()"))

P.append(WE("w3_10", "Fixed-top navbar with dropdown, search and sign-up, fixed-bottom footer (Practical 13)", page("Fixed Navbar", """
<nav class="navbar navbar-expand-md fixed-top bg-dark" data-bs-theme="dark">
  <div class="container">
    <a class="navbar-brand d-flex align-items-center gap-2" href="#">
      <img src="images/logo.png" alt="Logo" width="32" height="32"
        class="rounded-circle"> EduWorld</a>
    <button class="navbar-toggler" data-bs-toggle="collapse"
      data-bs-target="#nav1" aria-label="Menu">
      <span class="navbar-toggler-icon"></span></button>
    <div class="collapse navbar-collapse" id="nav1">
      <ul class="navbar-nav me-auto">
        <li class="nav-item">
          <a class="nav-link active" href="#">Home</a></li>
        <li class="nav-item dropdown">
          <a class="nav-link dropdown-toggle" href="#"
            data-bs-toggle="dropdown">Courses</a>
          <ul class="dropdown-menu">
            <li><a class="dropdown-item" href="#">Diploma</a></li>
            <li><a class="dropdown-item" href="#">Degree</a></li>
          </ul>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="#">Contact</a></li>
      </ul>
      <form class="d-flex gap-2" role="search">
        <input class="form-control" type="search"
          placeholder="Search">
        <button class="btn btn-outline-light" type="submit">
          <i class="bi bi-search"></i></button>
        <button class="btn btn-warning text-nowrap" type="button">
          Sign up</button>
      </form>
    </div>
  </div>
</nav>

<main class="container">
  <h1 class="h3">Welcome to EduWorld</h1>
  <p>Scroll the page: the top menu and the bottom footer stay
    fixed while this content moves.</p>
  <p class="lorem">Lorem ipsum ...</p>
</main>

<footer class="fixed-bottom bg-dark text-white text-center
  small py-2">
  &copy; 2026 EduWorld | Surat, Gujarat |
  <i class="bi bi-telephone"></i> 98765 43210
</footer>
""", style="""
body { padding-top: 70px; padding-bottom: 50px; }
.lorem { height: 900px;
  background: linear-gradient(#F3ECFA, #fff); }
""", icons=True, bs_js=True),
"""A black menu bar fixed at the top with a round logo placeholder and "EduWorld". On a desktop it shows Home, a Courses dropdown (Diploma, Degree), Contact, a search box with a search button and a yellow "Sign up" button. On a phone these are hidden behind the hamburger button.
A black footer "© 2026 EduWorld | Surat, Gujarat | 98765 43210" is fixed at the bottom. When the page is scrolled, the long lavender area moves but the top bar and footer stay in place.""",
"""
<ul><li><b>.fixed-top</b> fixes the navbar to the top of the screen; <b>.fixed-bottom</b> fixes the footer to the bottom. They use <code>position: fixed</code>.</li>
<li>Fixed elements are removed from the normal flow, so <b>padding-top</b> and <b>padding-bottom</b> are added to the body to stop content hiding behind them.</li>
<li><code>.sticky-top</code> is an alternative: the navbar scrolls with the page until it reaches the top, then sticks.</li>
<li>A <b>logo</b> is an &lt;img&gt; inside <code>.navbar-brand</code>.</li>
<li>A <b>dropdown in a navbar</b> uses <code>li.nav-item.dropdown</code> with a <code>.dropdown-toggle</code> link.</li>
<li><b>Forms in a navbar:</b> a <code>form.d-flex</code> with an input and buttons; it moves into the collapsed menu on small screens.</li></ul>
"""))

P.append(WE("w3_11", "Breadcrumb and pagination (applied to a list)", page("Breadcrumb and Pagination", """
<div class="container py-3">
  <nav aria-label="breadcrumb">
    <ol class="breadcrumb">
      <li class="breadcrumb-item"><a href="#">Home</a></li>
      <li class="breadcrumb-item"><a href="#">Computer</a></li>
      <li class="breadcrumb-item"><a href="#">Semester 3</a></li>
      <li class="breadcrumb-item active">RWPD</li>
    </ol>
  </nav>

  <h1 class="h5">Student list</h1>
  <ul class="list-group mb-3" id="list"></ul>

  <nav aria-label="Student pages">
    <ul class="pagination justify-content-center" id="pager"></ul>
  </nav>

  <h2 class="h6">Pagination sizes</h2>
  <ul class="pagination pagination-sm">
    <li class="page-item disabled"><span class="page-link">
      &laquo;</span></li>
    <li class="page-item active"><span class="page-link">1</span></li>
    <li class="page-item"><a class="page-link" href="#">2</a></li>
    <li class="page-item"><a class="page-link" href="#">&raquo;</a></li>
  </ul>
  <ul class="pagination pagination-lg">
    <li class="page-item"><a class="page-link" href="#">1</a></li>
    <li class="page-item"><a class="page-link" href="#">2</a></li>
  </ul>
</div>
""", script="""
var names = ["Aarav", "Bhavya", "Chirag", "Diya", "Esha",
  "Farhan", "Gauri", "Harsh", "Isha", "Jay", "Kavya"];
var per = 4, page = 1;
var pages = Math.ceil(names.length / per);

function item(n, label, cls) {
  return '<li class="page-item' + cls + '">' +
    '<a class="page-link" href="#" data-p="' + n + '">' +
    label + "</a></li>";
}

function show() {
  var start = (page - 1) * per;
  var html = "";
  names.slice(start, start + per).forEach(function (n, i) {
    html += '<li class="list-group-item">' + (start + i + 1) +
      ". " + n + "</li>";
  });
  document.getElementById("list").innerHTML = html;

  var first = page == 1 ? " disabled" : "";
  var p = item(page - 1, "Previous", first);
  for (var i = 1; i <= pages; i++) {
    p += item(i, i, i == page ? " active" : "");
  }
  var last = page == pages ? " disabled" : "";
  p += item(page + 1, "Next", last);
  document.getElementById("pager").innerHTML = p;
}

document.getElementById("pager").onclick = function (e) {
  e.preventDefault();
  var n = parseInt(e.target.dataset.p);
  if (n >= 1 && n <= pages) { page = n; show(); }
};
show();
"""),
"""A breadcrumb trail "Home / Computer / Semester 3 / RWPD" where the first three are links and RWPD is the current page.
A student list shows 4 names at a time (1. Aarav to 4. Diya) with a centred pagination bar "Previous 1 2 3 Next". Tapping 2 shows students 5-8, tapping 3 shows 9-11; Previous is disabled on page 1 and Next on the last page.
Below are a small and a large pagination example.""",
"""
<ul><li><b>Breadcrumb</b> shows the user's location in the site hierarchy: <code>ol.breadcrumb</code> with <code>li.breadcrumb-item</code>; the last item has <code>.active</code>. The separator "/" is added by CSS (change it with the <code>--bs-breadcrumb-divider</code> variable).</li>
<li><b>Pagination</b> divides long content into pages: <code>ul.pagination</code> &gt; <code>li.page-item</code> &gt; <code>a.page-link</code>; states <code>.active</code> and <code>.disabled</code>; sizes <code>.pagination-lg</code> / <code>.pagination-sm</code>; alignment with <code>justify-content-center</code>.</li>
<li><b>Applying pagination:</b> the script shows only <code>per</code> items using <code>slice(start, start + per)</code> and rebuilds the page buttons. One click handler on the &lt;ul&gt; reads <code>data-p</code> from the clicked link (event delegation).</li>
<li>&amp;laquo; and &amp;raquo; are the &laquo; and &raquo; symbols.</li></ul>
""", actions="document.querySelector('#pager [data-p=\"2\"]').click()"))

# ------------------------------------------------------------------ 3.3
P.append(WE("w3_12", "Badges (labels) and page header", page("Badges", """
<div class="container py-3">
  <div class="pb-2 mb-3 border-bottom">
    <h1>Exam Results <small class="text-body-secondary">
      Summer 2026</small></h1>
  </div>

  <h2>Notices <span class="badge bg-danger">New</span></h2>
  <h4>Messages <span class="badge bg-secondary">4</span></h4>

  <p>
    <span class="badge bg-primary">Primary</span>
    <span class="badge bg-success">Passed</span>
    <span class="badge bg-warning text-dark">Pending</span>
    <span class="badge bg-info text-dark">Info</span>
    <span class="badge bg-dark">Dark</span>
  </p>
  <p>
    <span class="badge rounded-pill bg-primary">Pill</span>
    <span class="badge rounded-pill text-bg-success">99+</span>
    <span class="badge text-bg-light border">Light</span>
  </p>

  <button class="btn btn-primary">
    Inbox <span class="badge text-bg-light">7</span>
  </button>
  <button class="btn btn-dark position-relative ms-3">
    <i class="bi bi-bell"></i>
    <span class="position-absolute top-0 start-100
      translate-middle badge rounded-pill bg-danger">3</span>
  </button>
</div>
""", icons=True),
"""A page header "Exam Results" with a grey "Summer 2026" subtitle and a line below it.
"Notices" has a red "New" badge and "Messages" a grey "4" badge (badges scale with the heading size). A row of coloured badges (Primary, Passed, Pending, Info, Dark), then pill-shaped badges.
A blue "Inbox 7" button with a white count, and a black bell button with a small red "3" bubble on its top-right corner.""",
"""
<ul><li>A <b>badge</b> is a small count or label: <code>&lt;span class="badge bg-primary"&gt;</code>. It scales to the size of its parent (inside h2 it is larger).</li>
<li><b>Bootstrap 3</b> had <b>labels</b> (<code>.label .label-success</code>) and <b>badges</b> (<code>.badge</code> for counts); Bootstrap 4/5 use badges for both.</li>
<li>Colours: <code>bg-*</code> (add <code>text-dark</code> for light colours) or <code>text-bg-*</code>, which sets a readable text colour automatically.</li>
<li><code>.rounded-pill</code> gives a capsule shape.</li>
<li><b>Positioned badge</b> (notification bubble): <code>.position-relative</code> on the button and <code>position-absolute top-0 start-100 translate-middle</code> on the badge.</li>
<li><b>Page header</b> (Bootstrap 3 <code>.page-header</code>) is made in Bootstrap 5 with utilities: <code>pb-2 mb-3 border-bottom</code>.</li></ul>
"""))

P.append(WE("w3_13", "Education website: breadcrumb, pagination, badge, jumbotron, thumbnails (Practical 14)", page("Education Website", """
<div class="container py-3">
  <nav aria-label="breadcrumb">
    <ol class="breadcrumb">
      <li class="breadcrumb-item"><a href="#">Home</a></li>
      <li class="breadcrumb-item active">Courses</li>
    </ol>
  </nav>

  <div class="p-4 p-md-5 mb-4 bg-body-tertiary rounded-3">
    <h1 class="display-6 fw-bold">Learn Web Design
      <span class="badge bg-success fs-6 align-middle">Free</span>
    </h1>
    <p class="lead">Online courses for GTU diploma students:
      notes, videos and practicals.</p>
    <a class="btn btn-primary btn-lg" href="#">Get started</a>
  </div>

  <div class="pb-1 mb-3 border-bottom">
    <h2 class="h4">Popular courses
      <small class="text-body-secondary">(page 1 of 3)</small></h2>
  </div>

  <div class="row g-3">
    <div class="col-6 col-md-3">
      <div class="card h-100">
        <img src="images/html.jpg" class="card-img-top" alt="HTML">
        <div class="card-body p-2">
          <h3 class="h6">HTML5 <span class="badge
            bg-danger">Hot</span></h3>
          <small class="text-muted">12 lessons</small>
        </div>
      </div>
    </div>
    <div class="col-6 col-md-3">
      <div class="card h-100">
        <img src="images/css.jpg" class="card-img-top" alt="CSS">
        <div class="card-body p-2">
          <h3 class="h6">CSS3</h3>
          <small class="text-muted">15 lessons</small>
        </div>
      </div>
    </div>
    <div class="col-6 col-md-3">
      <a href="#" class="d-block">
        <img src="images/js.jpg" class="img-thumbnail" alt="JavaScript"
          width="400" height="260"></a>
      <p class="small mb-0">JavaScript (thumbnail link)</p>
    </div>
    <div class="col-6 col-md-3">
      <a href="#" class="d-block">
        <img src="images/bootstrap.jpg" class="img-thumbnail"
          alt="Bootstrap" width="400" height="260"></a>
      <p class="small mb-0">Bootstrap <span class="badge
        bg-primary">New</span></p>
    </div>
  </div>

  <nav class="mt-4" aria-label="Course pages">
    <ul class="pagination justify-content-center">
      <li class="page-item disabled">
        <span class="page-link">Previous</span></li>
      <li class="page-item active"><span class="page-link">1</span></li>
      <li class="page-item"><a class="page-link" href="#">2</a></li>
      <li class="page-item"><a class="page-link" href="#">3</a></li>
      <li class="page-item"><a class="page-link" href="#">Next</a></li>
    </ul>
  </nav>
</div>
"""),
"""An education site page: the breadcrumb "Home / Courses", then a large grey jumbotron box with the heading "Learn Web Design", a green "Free" badge, a lead line and a big "Get started" button.
A "Popular courses (page 1 of 3)" header with a line below, then four course thumbnails (2 per row on a phone, 4 on a desktop): two cards (HTML5 with a red "Hot" badge, CSS3) and two bordered thumbnail images (JavaScript, Bootstrap with a "New" badge). A centred pagination bar "Previous 1 2 3 Next" is at the bottom.""",
"""
<ul><li><b>Jumbotron:</b> a big box to highlight the main message. The <code>.jumbotron</code> class was removed in Bootstrap 5; it is built with utilities: <code>p-5 mb-4 bg-body-tertiary rounded-3</code> plus <code>.display-*</code> and <code>.lead</code> text.</li>
<li><b>Page header:</b> heading with <code>small</code> subtitle and <code>border-bottom</code>.</li>
<li><b>Thumbnails:</b> Bootstrap 3 had <code>.thumbnail</code>; in Bootstrap 5 use <code>.img-thumbnail</code> images or cards in a grid.</li>
<li><b>Badges</b> mark new or popular items; <b>breadcrumb</b> shows the location; <b>pagination</b> moves between pages of courses.</li>
<li>The grid <code>col-6 col-md-3</code> gives 2 or 4 thumbnails per row.</li></ul>
"""))

P.append(WE("w3_14", "Alerts, dismissible alerts and message after closing", page("Alerts", """
<div class="container py-3">
  <div class="alert alert-primary">A simple primary alert.</div>
  <div class="alert alert-success d-flex align-items-center gap-2">
    <i class="bi bi-check-circle-fill"></i>
    <div>Form submitted successfully.</div>
  </div>
  <div class="alert alert-warning">
    <h4 class="alert-heading">Exam form</h4>
    <p class="mb-0">Last date is 30 November. See the
      <a href="#" class="alert-link">notice</a>.</p>
  </div>

  <div class="alert alert-danger alert-dismissible fade show"
    id="err" role="alert">
    <strong>Error!</strong> Fee not paid.
    <button type="button" class="btn-close"
      data-bs-dismiss="alert" aria-label="Close"></button>
  </div>
  <div class="alert alert-info alert-dismissible fade show"
    id="inf" role="alert">
    Library closed on Sunday.
    <button type="button" class="btn-close"
      data-bs-dismiss="alert" aria-label="Close"></button>
  </div>

  <p id="log" class="text-success fw-bold"></p>
  <button class="btn btn-outline-dark" id="add">
    Show new alert</button>
</div>
""", script="""
document.addEventListener("closed.bs.alert", function (e) {
  document.getElementById("log").textContent =
    "Alert '" + e.target.id + "' was closed.";
});

document.getElementById("add").onclick = function () {
  var d = document.createElement("div");
  d.id = "new" + Date.now() % 1000;
  d.className =
    "alert alert-secondary alert-dismissible fade show";
  d.innerHTML = "New alert added at " +
    new Date().toLocaleTimeString() +
    '<button type="button" class="btn-close"' +
    ' data-bs-dismiss="alert"></button>';
  this.before(d);
};
""", icons=True, bs_js=True),
"""Coloured alert boxes: blue (simple), green with a tick icon, and yellow with a heading "Exam form" and a bold link.
A red "Error! Fee not paid." alert and a blue "Library closed on Sunday." alert each have a close (x) button. Closing one fades it out, and a green message appears, e.g. "Alert 'err' was closed." The "Show new alert" button adds a grey dismissible alert with the current time.""",
"""
<ul><li><b>Alert:</b> <code>div.alert</code> + colour <code>alert-primary / success / danger / warning / info / secondary / light / dark</code>.</li>
<li>Extra content: <code>.alert-heading</code> for a title and <code>.alert-link</code> for links in matching colour; icons can be added with flex utilities.</li>
<li><b>Dismissible alert:</b> add <code>.alert-dismissible</code> and a <code>button.btn-close</code> with <code>data-bs-dismiss="alert"</code>. <code>.fade .show</code> animate the closing. (Bootstrap 3 used <code>class="close"</code> and &amp;times;.)</li>
<li><b>Alert events:</b> <code>close.bs.alert</code> fires when closing starts, <code>closed.bs.alert</code> after the alert is removed. Here the second one shows a message after closing.</li>
<li>JavaScript: <code>bootstrap.Alert.getOrCreateInstance("#err").close()</code> closes an alert from code.</li></ul>
""", actions="document.querySelector('#err .btn-close').click()"))

P.append(WE("w3_15", "Progress bars: labels, colours, striped, animated, dynamic (Practical 15)", page("Progress Bars", """
<div class="container py-3">
  <h1 class="h6">a. Basic progress bar</h1>
  <div class="progress mb-3" role="progressbar" aria-valuenow="40"
    aria-valuemin="0" aria-valuemax="100">
    <div class="progress-bar" style="width: 40%"></div>
  </div>

  <h2 class="h6">b. With label and height</h2>
  <div class="progress mb-3" style="height: 22px;">
    <div class="progress-bar bg-success" style="width: 75%">
      75% complete</div>
  </div>

  <h2 class="h6">c. Colours, striped, animated, multiple</h2>
  <div class="progress mb-2">
    <div class="progress-bar bg-warning progress-bar-striped"
      style="width: 60%">60%</div>
  </div>
  <div class="progress mb-2">
    <div class="progress-bar bg-danger progress-bar-striped
      progress-bar-animated" style="width: 85%">85%</div>
  </div>
  <div class="progress-stacked mb-3">
    <div class="progress" style="width: 30%">
      <div class="progress-bar bg-success">Pass 30%</div></div>
    <div class="progress" style="width: 20%">
      <div class="progress-bar bg-warning">ATKT 20%</div></div>
    <div class="progress" style="width: 10%">
      <div class="progress-bar bg-danger">Fail</div></div>
  </div>

  <h2 class="h6">d. Change value with JavaScript</h2>
  <div class="progress mb-2" style="height: 24px;">
    <div class="progress-bar progress-bar-striped" id="bar"
      style="width: 0%">0%</div>
  </div>
  <button class="btn btn-primary btn-sm" id="start">Start upload</button>
  <button class="btn btn-outline-secondary btn-sm" id="minus">-10</button>
  <button class="btn btn-outline-secondary btn-sm" id="plus">+10</button>
</div>
""", script="""
var bar = document.getElementById("bar");
var value = 0, timer = null;

function setValue(v) {
  value = Math.max(0, Math.min(100, v));
  bar.style.width = value + "%";
  bar.textContent = value + "%";
  bar.classList.toggle("bg-success", value == 100);
  if (value == 100) bar.textContent = "Done!";
}

document.getElementById("start").onclick = function () {
  clearInterval(timer);
  setValue(0);
  timer = setInterval(function () {
    setValue(value + 5);
    if (value >= 100) clearInterval(timer);
  }, 200);
};
document.getElementById("plus").onclick = function () {
  setValue(value + 10);
};
document.getElementById("minus").onclick = function () {
  setValue(value - 10);
};
"""),
"""a. A thin grey bar, 40% filled in blue.
b. A taller green bar, 75% filled, with the text "75% complete".
c. A yellow striped bar at 60%, a red striped bar at 85% whose stripes move, and one bar split into green "Pass 30%", yellow "ATKT 20%" and red "Fail".
d. An empty bar with buttons. "Start upload" fills it 5% at a time (0% to 100% in 4 seconds) and it turns green with "Done!". The +10 and -10 buttons change the value by 10.""",
"""
<ul><li>A progress bar has two parts: the track <code>.progress</code> and the filled part <code>.progress-bar</code>. The <b>width</b> style sets the value.</li>
<li><b>Label:</b> text inside .progress-bar. <b>Height:</b> set on .progress. <b>Accessibility:</b> <code>role="progressbar"</code> with aria-valuenow, -valuemin, -valuemax.</li>
<li><b>Colours:</b> <code>bg-success, bg-info, bg-warning, bg-danger</code>.</li>
<li><b>Striped:</b> <code>.progress-bar-striped</code>; <b>animated:</b> add <code>.progress-bar-animated</code>.</li>
<li><b>Multiple bars:</b> <code>.progress-stacked</code> containing several <code>.progress</code> elements, each with its own width (Bootstrap 5.3).</li>
<li><b>Dynamic value:</b> JavaScript changes <code>style.width</code> and the text; <code>setInterval()</code> repeats the change every 200 ms and <code>clearInterval()</code> stops it.</li></ul>
""", actions="document.getElementById('plus').click(); document.getElementById('plus').click(); document.getElementById('plus').click()"))

P.append(WE("w3_16", "Media objects: family tree with nested media (Practical 16)", page("Family", """
<div class="container py-3">
  <h1 class="h4 mb-3">Our Family</h1>
  <div class="d-flex mb-3">
    <img src="images/grandfather.jpg" alt="Grandfather"
      width="64" height="64" class="rounded-circle flex-shrink-0">
    <div class="ms-3">
      <h2 class="h6 mb-0">Ramesh Patel (Grandfather)</h2>
      <p class="small text-muted">Retired teacher, age 72</p>

      <div class="d-flex mt-2">
        <img src="images/father.jpg" alt="Father" width="56"
          height="56" class="rounded-circle flex-shrink-0">
        <div class="ms-3">
          <h3 class="h6 mb-0">Mahesh Patel (Father)</h3>
          <p class="small text-muted">Engineer, age 48</p>

          <div class="d-flex mt-2">
            <img src="images/me.jpg" alt="Me" width="48" height="48"
              class="rounded flex-shrink-0">
            <div class="ms-3">
              <h4 class="h6 mb-0">Riya Patel (Me)</h4>
              <p class="small text-muted mb-0">Diploma, 18</p>
            </div>
          </div>
          <div class="d-flex mt-2">
            <img src="images/brother.jpg" alt="Brother" width="48"
              height="48" class="rounded flex-shrink-0">
            <div class="ms-3">
              <h4 class="h6 mb-0">Dev Patel (Brother)</h4>
              <p class="small text-muted mb-0">Class 9, 14</p>
            </div>
          </div>
        </div>
      </div>

      <div class="d-flex mt-2">
        <img src="images/uncle.jpg" alt="Uncle" width="56"
          height="56" class="rounded-circle flex-shrink-0">
        <div class="ms-3">
          <h3 class="h6 mb-0">Suresh Patel (Uncle)</h3>
          <p class="small text-muted mb-0">Businessman, age 45</p>
        </div>
      </div>
    </div>
  </div>

  <div class="d-flex flex-row-reverse text-end border-top pt-3">
    <img src="images/grandmother.jpg" alt="Grandmother" width="64"
      height="64" class="rounded-circle flex-shrink-0">
    <div class="me-3">
      <h2 class="h6 mb-0">Savita Patel (Grandmother)</h2>
      <p class="small text-muted mb-0">Image on the right side</p>
    </div>
  </div>
</div>
"""),
"""A family tree: Grandfather (round photo) at the top with his details. Indented under him are Father and Uncle (smaller round photos); indented under Father are "Riya Patel (Me)" and "Dev Patel (Brother)" with small rounded-square photos.
Each level moves further right, showing the hierarchy. At the bottom, the Grandmother entry has its photo on the right and right-aligned text.""",
"""
<ul><li>A <b>media object</b> is an image (or icon) beside text content, like a comment or profile.</li>
<li>Bootstrap 4 had <code>.media</code> / <code>.media-body</code>; in Bootstrap 5 it is built with <b>flex utilities</b>: <code>div.d-flex</code> containing an image with <code>.flex-shrink-0</code> and a content div with <code>.ms-3</code> (space) and optionally <code>.flex-grow-1</code>.</li>
<li><b>Rounded media:</b> <code>.rounded-circle</code> or <code>.rounded</code> on the image.</li>
<li><b>Nested media:</b> put another <code>.d-flex</code> media block inside the content div; each level is indented, showing parent-child hierarchy.</li>
<li><b>Image on the right:</b> <code>.flex-row-reverse</code> with <code>.me-3</code>. Vertical alignment: <code>.align-items-center</code> or <code>.align-items-end</code>.</li></ul>
"""))

P.append(WE("w3_17", "Service providers: panels (cards), list groups and alerts (Practical 17)", page("Service Providers", """
<div class="container py-3">
  <h1 class="h4 mb-3">City Service Providers</h1>
  <div class="alert alert-info alert-dismissible fade show" id="tip">
    <i class="bi bi-info-circle"></i> Tap a provider to select it.
    <button type="button" class="btn-close"
      data-bs-dismiss="alert"></button>
  </div>
  <p id="closed" class="text-success small"></p>

  <div class="row g-3">
    <div class="col-md-6">
      <div class="card border-primary">
        <div class="card-header text-bg-primary">
          <i class="bi bi-wifi"></i> Internet providers</div>
        <div class="list-group list-group-flush" id="net">
          <a href="#" class="list-group-item list-group-item-action
            d-flex justify-content-between">JioFiber
            <span class="badge text-bg-primary">4.5</span></a>
          <a href="#" class="list-group-item list-group-item-action
            d-flex justify-content-between">Airtel Xstream
            <span class="badge text-bg-primary">4.3</span></a>
          <a href="#" class="list-group-item list-group-item-action
            disabled">BSNL (not available)</a>
        </div>
        <div class="card-footer small text-muted">3 providers</div>
      </div>
    </div>
    <div class="col-md-6">
      <div class="card border-success">
        <div class="card-header text-bg-success">
          <i class="bi bi-lightning"></i> Power and gas</div>
        <ul class="list-group list-group-flush">
          <li class="list-group-item list-group-item-success">
            DGVCL - electricity</li>
          <li class="list-group-item list-group-item-warning">
            Gujarat Gas - piped gas</li>
          <li class="list-group-item list-group-item-danger">
            Emergency: 1912</li>
        </ul>
      </div>
    </div>
  </div>
  <div id="msg" class="mt-3"></div>
</div>
""", script="""
document.getElementById("tip")
  .addEventListener("closed.bs.alert", function () {
    document.getElementById("closed").textContent =
      "Tip closed. You can still select a provider.";
  });

document.querySelectorAll("#net .list-group-item").forEach(
  function (item) {
    item.addEventListener("click", function (e) {
      e.preventDefault();
      document.querySelectorAll("#net .active").forEach(
        function (a) { a.classList.remove("active"); });
      item.classList.add("active");
      var name = item.firstChild.textContent.trim();
      document.getElementById("msg").innerHTML =
        '<div class="alert alert-success alert-dismissible">' +
        "You selected <b>" + name + "</b>." +
        '<button class="btn-close" data-bs-dismiss="alert">' +
        "</button></div>";
    });
  });
""", icons=True, bs_js=True),
"""A "City Service Providers" page with a blue dismissible tip alert. Closing it shows the green text "Tip closed. You can still select a provider."
Two panels (side by side on a desktop): a blue "Internet providers" panel listing JioFiber 4.5 and Airtel Xstream 4.3 with rating badges and a greyed-out BSNL, plus a footer "3 providers"; and a green "Power and gas" panel (electricity and gas) with green, yellow and red coloured list items.
Tapping an internet provider highlights it in blue and shows a green alert "You selected JioFiber.".""",
"""
<ul><li><b>Panel:</b> Bootstrap 3 had <code>.panel .panel-primary</code> with <code>.panel-heading</code>, <code>.panel-body</code>, <code>.panel-footer</code>. In Bootstrap 5 a <b>card</b> is used: <code>.card.border-primary</code>, <code>.card-header.text-bg-primary</code>, <code>.card-footer</code>.</li>
<li><b>List group:</b> <code>.list-group</code> with <code>.list-group-item</code>; <code>.list-group-flush</code> inside a card; clickable items with <code>a.list-group-item-action</code>; states <code>.active</code>, <code>.disabled</code>; colours <code>.list-group-item-success</code> etc.; badges aligned with <code>d-flex justify-content-between</code>.</li>
<li><b>Alerts:</b> the dismissible tip and the success message. The <code>closed.bs.alert</code> event shows a message after the alert has been closed.</li>
<li>The click handler removes <code>.active</code> from all items and adds it to the clicked one.</li></ul>
""", actions="document.querySelector('#tip .btn-close').click(); setTimeout(function(){document.querySelector('#net .list-group-item').click();}, 50)"))

PROGRAMS = P
