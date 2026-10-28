"""DI03000061 Unit 1 extras: syntax sheet, viva, exam (practical) questions."""
from web_content import SXE, VE, XE, G
from content_DI03000061_u1_notes import SN


def S(name, key, terms=""):
    return SXE(name, SN[key].strip("\n"), terms)


SYNTAX = [
    G("jQuery Basics", [
        S("Including jQuery", "s_include", "Load jQuery before any script that uses it."),
        S("Basic syntax", "s_syntax", "$ = jQuery. $(selector).action()"),
        S("Document ready", "s_ready", "Runs after the DOM is loaded."),
        S("jQuery vs JavaScript", "s_vs_js", "Same result, shorter code."),
    ]),
    G("Selectors", [
        S("Selector reference", "s_selectors", "CSS selectors plus jQuery filters. Index starts at 0."),
    ]),
    G("Events", [
        S("Event method", "s_event", "click, dblclick, mouseenter, keyup, change, submit ..."),
        S("on() and off()", "s_on", "on() can attach several events and use delegation."),
        S("hover()", "s_hover", "First function: mouse enters. Second: mouse leaves."),
        S("preventDefault()", "s_prevent", "Stops the default browser action."),
    ]),
    G("Effects and DOM", [
        S("Effects", "s_effects", "Speed: slow, fast or ms. Callback runs after the effect."),
        S("DOM methods", "s_dom", "No argument = get, with argument = set."),
    ]),
    G("Bootstrap Setup", [
        S("Bootstrap from CDN", "s_bs_cdn", "jsDelivr is the official CDN. Needs internet."),
        S("Local folder structure", "s_folder", "Link files with relative paths."),
        S("Basic template", "s_template", "HTML5 doctype, viewport, CSS in head, JS before </body>."),
        S("Viewport meta tag", "s_viewport", "Required for responsive pages on mobiles."),
        S("Dark mode (5.3)", "s_dark", "data-bs-theme = light or dark."),
    ]),
    G("Responsive Design", [
        S("Responsive grid", "s_responsive", "container > row > col-*. 12 columns per row."),
        S("CSS media query", "s_media", "min-width = mobile first."),
        S("Centring with utilities", "s_center", "d-flex + justify-content-center + align-items-center."),
        S("Removing responsiveness", "s_nonresp", "No viewport tag, fixed container, col-* without breakpoint."),
    ]),
]

VIVA = [
    G("jQuery", [
        VE("What is jQuery?", "A fast, small, cross-browser JavaScript library that simplifies DOM manipulation, event handling, animation and AJAX. Motto: write less, do more."),
        VE("Who developed jQuery and when?", "John Resig, released in January 2006."),
        VE("Is jQuery a language?", "No. It is a library written in JavaScript."),
        VE("What does $ mean in jQuery?", "$ is a short name (alias) for the jQuery function. $(\"p\") is the same as jQuery(\"p\")."),
        VE("What is the basic syntax of jQuery?", "$(selector).action(): select elements and perform an action on them."),
        VE("Why is $(document).ready() used?", "To run jQuery code only after the DOM is fully loaded, so all elements exist."),
        VE("Difference between $(document).ready() and window load?", "ready fires when the DOM is ready; load waits until images and all other resources are loaded."),
        VE("What are the two ways to include jQuery?", "From a CDN (e.g. code.jquery.com) or from a downloaded local file."),
        VE("What is a minified file?", "A file with spaces, comments and long names removed to reduce its size, e.g. jquery-3.7.1.min.js."),
        VE("What are jQuery selectors?", "Expressions used to find HTML elements by tag, id, class, attribute, position etc., based on CSS selectors."),
        VE("Which selector is the fastest?", "The id selector ($(\"#id\")), because an id is unique."),
        VE("What does $(\"li:even\") select?", "List items at index 0, 2, 4 ... (index counting starts at 0)."),
        VE("What is $(this)?", "The jQuery object of the element on which the current event occurred."),
        VE("What is an event?", "An action such as a click, key press, mouse movement, form submit or window resize to which the page can respond."),
        VE("Name some mouse events.", "click, dblclick, mouseenter, mouseleave, mousedown, mouseup, hover."),
        VE("Name some form events.", "submit, change, focus, blur."),
        VE("What is the difference between keydown and keyup?", "keydown fires when a key is pressed down, keyup when it is released."),
        VE("What is the use of the on() method?", "To attach one or more event handlers to elements, including delegated events for elements added later."),
        VE("What is event delegation?", "Attaching a handler to a parent element that handles events of its (current and future) children."),
        VE("What does e.preventDefault() do?", "Stops the browser's default action, e.g. a form reload or following a link."),
        VE("What is method chaining?", "Calling several jQuery methods one after another on the same selection in one statement."),
        VE("Difference between text() and html()?", "text() gets/sets plain text; html() gets/sets content including HTML tags."),
        VE("Difference between append() and prepend()?", "append() adds content at the end inside the element; prepend() at the beginning."),
        VE("Difference between remove() and empty()?", "remove() deletes the element itself; empty() deletes only its child content."),
        VE("Name some jQuery effects.", "hide, show, toggle, fadeIn, fadeOut, fadeToggle, slideUp, slideDown, slideToggle, animate."),
        VE("What is a callback function?", "A function that runs after another action (such as an effect) is complete."),
    ]),
    G("Bootstrap", [
        VE("What is Bootstrap?", "A free, open-source front-end framework of HTML, CSS and JavaScript for building responsive, mobile-first websites."),
        VE("Who developed Bootstrap?", "Mark Otto and Jacob Thornton at Twitter; released as open source on 19 August 2011."),
        VE("What was Bootstrap originally called?", "Twitter Blueprint (later Twitter Bootstrap)."),
        VE("What is the latest major version of Bootstrap?", "Bootstrap 5 (released 2021); version 5.3 added dark mode."),
        VE("Does Bootstrap 5 need jQuery?", "No. Bootstrap 5 uses plain JavaScript. Bootstrap 3 and 4 needed jQuery."),
        VE("What does mobile first mean?", "Styles are designed for small screens first, then larger screens are enhanced using min-width media queries."),
        VE("What is responsive web design?", "Designing pages whose layout adjusts automatically to different screen sizes and devices."),
        VE("What is a CDN?", "Content Delivery Network: a group of servers that deliver files (like Bootstrap) from the server nearest to the user."),
        VE("Which files are needed to use Bootstrap?", "bootstrap.min.css and, for interactive components, bootstrap.bundle.min.js."),
        VE("What is included in bootstrap.bundle.min.js?", "Bootstrap's JavaScript plug-ins plus Popper, used to position dropdowns, tooltips and popovers."),
        VE("Where are the CSS and JS files linked?", "CSS in the head; JavaScript just before the closing body tag."),
        VE("Why is the viewport meta tag used?", "So that mobile browsers use the device width and initial zoom 1, which makes the page responsive."),
        VE("What does width=device-width mean?", "The page width is set equal to the screen width of the device."),
        VE("How many columns are in the Bootstrap grid?", "12 columns per row."),
        VE("Name the Bootstrap 5 breakpoints.", "xs (below 576), sm 576, md 768, lg 992, xl 1200 and xxl 1400 pixels."),
        VE("Difference between .container and .container-fluid?", ".container has a fixed maximum width at each breakpoint; .container-fluid is always 100% wide."),
        VE("How can responsiveness be removed?", "Remove the viewport meta tag, give the container a fixed width and use col-* classes without breakpoints."),
        VE("Name some major features of Bootstrap.", "Responsive grid, mobile first, ready components, JavaScript plug-ins, utility classes, icons, Sass customisation, browser compatibility."),
        VE("What replaced Glyphicons?", "Bootstrap Icons, a separate open-source SVG icon library."),
        VE("What replaced panels, wells and thumbnails?", "The card component (from Bootstrap 4)."),
        VE("What is a disadvantage of Bootstrap?", "Websites can look similar, the file is large if everything is used, and HTML gets many classes."),
        VE("How do you enable dark mode in Bootstrap 5.3?", "Add data-bs-theme=\"dark\" to the html element (or any element)."),
    ]),
]

EXAM_QS = [
    XE("What is jQuery? Explain its importance and features.", 3),
    XE("Explain jQuery syntax and the document ready function with an example.", 3),
    XE("Explain different types of jQuery selectors with examples.", 4),
    XE("Explain any four jQuery events with examples.", 4),
    XE("Write a jQuery program to hide, show and toggle a paragraph on button clicks.", 3),
    XE("Write a jQuery program to change the background colour of a box on mouseenter and mouseleave.", 3),
    XE("Write a jQuery program to count characters typed in a textarea.", 3),
    XE("Write a jQuery program to validate that the name field is not empty on form submit.", 4),
    XE("Explain jQuery effects (fade and slide methods) with examples.", 4),
    XE("What is Bootstrap? Why should we use Bootstrap?", 3),
    XE("Write a short note on the history of Bootstrap.", 3),
    XE("List the advantages of Bootstrap.", 3),
    XE("Explain the methods of setting up a Bootstrap environment. (Practical 1)", 4),
    XE("Write the basic Bootstrap 5 template and explain each part.", 4),
    XE("Display the department and college name at the centre of the screen with and without Bootstrap. (Practical 2)", 4),
    XE("What is responsive web design? Create a responsive web page using Bootstrap.", 7),
    XE("Explain the viewport meta tag and Bootstrap breakpoints.", 4),
    XE("How can responsiveness be removed from a Bootstrap page? Explain with code.", 4),
    XE("Explain the major features of Bootstrap.", 4),
    XE("Compare Bootstrap 3, Bootstrap 4 and Bootstrap 5.", 4),
]
