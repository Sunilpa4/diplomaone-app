"""DI03000061 Unit 3 extras: syntax sheet, viva, exam (practical) questions."""
from web_content import SXE, VE, XE, G
from content_DI03000061_u3_notes import SN


def S(name, key, terms=""):
    return SXE(name, SN[key].strip("\n"), terms)


SYNTAX = [
    G("Icons and Dropdowns", [
        S("Bootstrap Icons", "s_icons", "Link bootstrap-icons.css; i.bi.bi-name; size fs-*, colour text-*."),
        S("Glyphicon vs Bootstrap Icon", "s_glyph", "BS3 span.glyphicon -> BS5 i.bi"),
        S("Dropdown", "s_dropdown", ".dropdown, .dropdown-toggle, .dropdown-menu, .dropdown-item, -header, -divider"),
        S("Split / dropup", "s_split", ".dropdown-toggle-split, .dropup, .dropdown-menu-end"),
    ]),
    G("Cards", [
        S("Card", "s_card", ".card > .card-img-top, .card-body (title, text), .card-footer"),
        S("Grid of cards", "s_card_grid", "row-cols-* + .card.h-100 for equal height."),
    ]),
    G("Button and Input Groups", [
        S("Button group", "s_btn_group", ".btn-group, .btn-group-vertical, -lg / -sm"),
        S("Button toolbar", "s_toolbar", ".btn-toolbar holding several .btn-group"),
        S("Nested dropdown", "s_nested", ".btn-group inside .btn-group"),
        S("Input group", "s_input_group", ".input-group + .input-group-text / button"),
    ]),
    G("Navigation", [
        S("Navs", "s_navs", ".nav + .nav-tabs / .nav-pills / .nav-underline; .flex-column"),
        S("Tab plug-in", "s_tab_plugin", "data-bs-toggle=\"tab\", .tab-content, .tab-pane.fade"),
        S("Navbar", "s_navbar", ".navbar-expand-lg, -brand, -toggler, .collapse.navbar-collapse, .navbar-nav"),
        S("Fixed navbar / footer", "s_fixed", ".fixed-top, .fixed-bottom, .sticky-top + body padding"),
        S("Breadcrumb", "s_breadcrumb", "ol.breadcrumb > li.breadcrumb-item (.active)"),
        S("Pagination", "s_pagination", "ul.pagination > li.page-item > a.page-link"),
    ]),
    G("Badges, Jumbotron, Thumbnails", [
        S("Badges", "s_badge", ".badge + bg-* / text-bg-*, .rounded-pill, positioned badge"),
        S("Jumbotron (BS5)", "s_jumbotron", "p-5 bg-body-tertiary rounded-3 + display-5, lead"),
        S("Page header (BS5)", "s_page_header", "border-bottom pb-2 mb-3 + small subtitle"),
        S("Thumbnails", "s_thumbnail", ".img-thumbnail, or cards in grid columns"),
    ]),
    G("Alerts and Progress", [
        S("Alerts", "s_alert", ".alert-*, .alert-dismissible, .btn-close data-bs-dismiss"),
        S("Alert events", "s_alert_js", "close.bs.alert, closed.bs.alert, Alert.close()"),
        S("Progress bar", "s_progress", ".progress > .progress-bar; -striped, -animated"),
        S("Progress with JS", "s_progress_js", "bar.style.width = v + \"%\"; setInterval"),
    ]),
    G("Media, List Group, Panels", [
        S("Media object (BS5)", "s_media", "d-flex > flex-shrink-0 (img) + flex-grow-1 ms-3"),
        S("List group", "s_list_group", ".list-group-item, .active, -action, -success, -flush"),
        S("Panel vs card", "s_panel", "BS3 .panel-heading/.panel-body -> BS5 .card-header/.card-body"),
    ]),
]

VIVA = [
    G("Components and Icons", [
        VE("What is a Bootstrap component?", "A ready-made, reusable UI part (navbar, card, alert, dropdown ...) built with HTML and Bootstrap classes, plus JavaScript for interactive ones."),
        VE("Give four advantages of Bootstrap components.", "They save time, give a consistent look, are responsive, work in all browsers, are accessible and easy to customise."),
        VE("Name the types of Bootstrap components.", "Navigation (navs, navbar, breadcrumb, pagination), content (card, list group, media), buttons and forms (button group, input group), feedback (alert, badge, progress)."),
        VE("Which file is needed for JavaScript components?", "bootstrap.bundle.min.js, which includes Popper.js."),
        VE("What are Glyphicons?", "The icon font included in Bootstrap 3 (about 250 icons), used as span.glyphicon.glyphicon-name."),
        VE("What replaced Glyphicons in Bootstrap 5?", "Bootstrap Icons, a separate free library used as i.bi.bi-name."),
        VE("How do you change the size and colour of a Bootstrap icon?", "It is a font, so use font-size (fs-1 to fs-6) and text colour classes such as text-danger."),
    ]),
    G("Dropdowns and Cards", [
        VE("Which attribute opens a dropdown?", "data-bs-toggle=\"dropdown\" on the toggle button."),
        VE("What does .dropdown-toggle do?", "Marks the toggle button and adds the caret automatically."),
        VE("What is .dropdown-header?", "A non-clickable heading inside a dropdown menu."),
        VE("What is .dropdown-divider?", "A horizontal line that separates groups of items."),
        VE("How do you make a dropdown open upward?", "Use .dropup instead of .dropdown (.dropend and .dropstart for right and left)."),
        VE("What is a split button dropdown?", "A button group with an action button and a separate caret button with .dropdown-toggle-split."),
        VE("What is a card?", "A flexible content container with optional header, image, body and footer."),
        VE("Which Bootstrap 3 components were replaced by the card?", "Panel, well and thumbnail."),
        VE("Name the parts of a card body.", ".card-title, .card-subtitle, .card-text and .card-link."),
        VE("How do you make cards in a row the same height?", "Put them in grid columns and add .h-100 to each card (or use .card-group)."),
    ]),
    G("Button and Input Groups", [
        VE("What is a button group?", "A set of buttons joined in one line using .btn-group."),
        VE("What is a button toolbar?", "A .btn-toolbar that contains several button groups in a row."),
        VE("How do you make a vertical button group?", "Use .btn-group-vertical."),
        VE("How do you add a dropdown inside a button group?", "Nest a .btn-group containing the dropdown toggle and menu inside the main .btn-group."),
        VE("What is an input group?", "A form control with text, icons or buttons added before or after it in one joined box."),
        VE("Which class holds the add-on text in an input group?", ".input-group-text (Bootstrap 3: .input-group-addon)."),
        VE("How do you change the size of an input group?", "Add .input-group-sm or .input-group-lg to the wrapper."),
    ]),
    G("Navs, Navbar, Breadcrumb, Pagination, Badges", [
        VE("Difference between nav tabs and nav pills?", "Tabs look like folder tabs joined to the content; pills show the active link with a coloured rounded background."),
        VE("How do you make a vertical nav?", "Add .flex-column to the .nav."),
        VE("What is the difference between .nav-fill and .nav-justified?", ".nav-fill fills the width with items of different widths; .nav-justified gives all items equal width."),
        VE("How do tabs switch content without reloading the page?", "data-bs-toggle=\"tab\" and data-bs-target link each tab to a .tab-pane inside .tab-content."),
        VE("What is a navbar?", "A responsive navigation header with brand, links, dropdowns and forms that collapses on small screens."),
        VE("What does .navbar-expand-lg mean?", "The menu is expanded from the lg breakpoint (992 px) and collapsed behind the toggler below it."),
        VE("What is .navbar-toggler?", "The hamburger button that opens and closes the collapsed menu."),
        VE("How do you make a fixed navbar?", "Add .fixed-top (or .fixed-bottom) and add body padding so content is not hidden."),
        VE("Difference between .fixed-top and .sticky-top?", ".fixed-top is always fixed; .sticky-top scrolls with the page until it reaches the top, then sticks."),
        VE("How is a dark navbar made in Bootstrap 5?", "bg-dark with data-bs-theme=\"dark\" (Bootstrap 3: .navbar-inverse)."),
        VE("What is a breadcrumb?", "A navigation aid showing the current page's location in the site hierarchy, e.g. Home / Sem 3 / RWPD."),
        VE("What is pagination?", "Numbered page links that split long content into pages: ul.pagination > li.page-item > a.page-link."),
        VE("What is a badge?", "A small label or count attached to text or buttons, e.g. New or 7 unread."),
        VE("What were labels in Bootstrap 3 called in Bootstrap 5?", "Badges (.label became .badge)."),
    ]),
    G("Jumbotron to Panels", [
        VE("What is a jumbotron?", "A large padded box with a light background used to highlight the main message of a page."),
        VE("Is .jumbotron available in Bootstrap 5?", "No. It is built with utilities like p-5, bg-body-tertiary, rounded-3 and display-5."),
        VE("What is .img-thumbnail?", "An image class that adds padding, a 1 px border and rounded corners."),
        VE("What is an alert?", "A contextual feedback message, e.g. success, danger, warning or info."),
        VE("How do you make a dismissible alert?", "Add .alert-dismissible and a button.btn-close with data-bs-dismiss=\"alert\"; .fade .show animate it."),
        VE("Which event fires after an alert is closed?", "closed.bs.alert (close.bs.alert fires when closing starts)."),
        VE("What is a progress bar?", "A bar showing how much of a task is complete: .progress with a .progress-bar whose width is set in %."),
        VE("How do you make an animated progress bar?", "Add .progress-bar-striped and .progress-bar-animated."),
        VE("How do you change a progress bar with JavaScript?", "Set bar.style.width = value + \"%\" and update its text."),
        VE("What is a media object?", "An image on one side with text beside it; in Bootstrap 5 it is made with d-flex, flex-shrink-0 and ms-3."),
        VE("What is a list group?", "A bordered list of items: .list-group with .list-group-item."),
        VE("What does .list-group-item-action do?", "Adds hover and active effects to clickable list items (links or buttons)."),
        VE("What is a panel?", "A Bootstrap 3 bordered box with a coloured heading and body, replaced by cards in Bootstrap 4/5."),
    ]),
]

EXAM_QS = [
    XE("What are Bootstrap components? List their advantages and types.", 4),
    XE("Explain Glyphicons and Bootstrap Icons with examples.", 3),
    XE("Design a web page with different types of menus using dropdowns, dropdown headers, dividers and icons. (Practical 9)", 7),
    XE("Explain the dropdown component with its classes.", 4),
    XE("Explain the card component with an example.", 4),
    XE("Explain button groups and button toolbar with examples.", 4),
    XE("Create a web page showing odd and even semester subjects using button groups and a button toolbar with dropdowns. (Practical 10)", 7),
    XE("Explain input groups. Design a job application form using input groups. (Practical 11)", 7),
    XE("Differentiate between nav tabs and nav pills.", 3),
    XE("Create a web page that shows a unit summary using the tab and pill plug-in. (Practical 12)", 7),
    XE("Explain the parts of a responsive navbar.", 4),
    XE("Design a page with a fixed navbar (logo, links, dropdown, search, sign up) and a fixed footer. (Practical 13)", 7),
    XE("Explain breadcrumb and pagination with examples.", 4),
    XE("What are badges? How are they used?", 3),
    XE("Design an education website using breadcrumb, jumbotron, badges, thumbnails and pagination. (Practical 14)", 7),
    XE("Explain alerts and dismissible alerts.", 3),
    XE("Create basic, labelled, striped and animated progress bars and change them with JavaScript. (Practical 15)", 7),
    XE("Explain the media object. Display a family tree using nested media objects. (Practical 16)", 4),
    XE("Explain list groups and panels.", 4),
    XE("Display service providers using panels, list groups and alerts, and show a message after an alert is closed. (Practical 17)", 7),
]
