"""DI03000061 Unit 4 extras: syntax sheet, viva, exam (practical) questions."""
from web_content import SXE, VE, XE, G
from content_DI03000061_u4_notes import SN


def S(name, key, terms=""):
    return SXE(name, SN[key].strip("\n"), terms)


SYNTAX = [
    G("Using Plug-ins", [
        S("Include the bundle", "s_include", "bootstrap.bundle.min.js = all plug-ins + Popper; BS3 needed jQuery."),
        S("Data attributes and API", "s_api", "new bootstrap.X(el, options); methods; action.bs.plugin events"),
        S("Bootstrap 3 jQuery API", "s_bs3_api", "$(el).plugin(\"method\"), .on(\"event.bs.plugin\")"),
    ]),
    G("Transition, Modal, Scrollspy", [
        S("Fade transition", "s_fade", ".fade + .show; transitionend event"),
        S("Page transition", "s_page_fade", "tab panes with .fade switch pages without reload"),
        S("Modal", "s_modal", ".modal.fade > .modal-dialog > .modal-content > header/body/footer"),
        S("Modal API", "s_modal_js", "backdrop, keyboard, focus; show() hide(); show/shown/hide/hidden.bs.modal"),
        S("Scrollspy", "s_scrollspy", "data-bs-spy=\"scroll\" data-bs-target; href = section id"),
    ]),
    G("Tab and Dropdown", [
        S("Tab methods/events", "s_tab_js", "Tab.show(); hide/show/hidden/shown.bs.tab"),
        S("Dropdown options", "s_dropdown_js", "autoClose, offset; toggle(); *.bs.dropdown"),
    ]),
    G("Tooltip and Popover", [
        S("Tooltip", "s_tooltip", "opt-in: new bootstrap.Tooltip(el); title, placement"),
        S("Tooltip API", "s_tooltip_js", "placement, trigger, html, delay; show hide toggle disable"),
        S("Popover", "s_popover", "data-bs-title + data-bs-content; trigger focus = dismiss"),
    ]),
    G("Alert and Button", [
        S("Alert plug-in", "s_alert_plugin", "data-bs-dismiss=\"alert\"; close(); close/closed.bs.alert"),
        S("Button plug-in", "s_button", "data-bs-toggle=\"button\"; .btn-check; toggle()"),
    ]),
    G("Collapse, Carousel, Affix", [
        S("Collapse", "s_collapse", "data-bs-toggle=\"collapse\" + href / data-bs-target"),
        S("Collapse API", "s_collapse_js", "parent, toggle; show hide toggle; *.bs.collapse"),
        S("Accordion", "s_accordion", ".accordion-item, .accordion-button, data-bs-parent"),
        S("Carousel", "s_carousel", ".carousel.slide, -indicators, -inner, -item, -caption, -control"),
        S("Carousel API", "s_carousel_js", "to(n) pause() cycle() next() prev(); slide/slid.bs.carousel"),
        S("Affix vs sticky", "s_affix", "BS3 data-spy=\"affix\" -> BS5 .sticky-top"),
    ]),
]

VIVA = [
    G("Plug-in Basics", [
        VE("What is a Bootstrap plug-in?", "A ready-made JavaScript module that adds interactive behaviour (modal, dropdown, carousel, collapse ...) to components."),
        VE("Why use Bootstrap plug-ins?", "No custom JavaScript is needed, they save time, work in all browsers, are responsive, accessible and customisable."),
        VE("Which file contains all Bootstrap 5 plug-ins?", "bootstrap.bundle.min.js (includes Popper)."),
        VE("What is Popper used for?", "Positioning dropdowns, tooltips and popovers."),
        VE("Does Bootstrap 5 need jQuery?", "No. Bootstrap 3 and 4 needed jQuery; Bootstrap 5 uses plain JavaScript."),
        VE("What are the two ways to use a plug-in?", "Data attributes in HTML, or the JavaScript API (new bootstrap.X(el, options) and methods)."),
        VE("What is the difference between show.bs.modal and shown.bs.modal?", "show fires when opening starts; shown fires after the animation has finished."),
        VE("How do you stop a modal from opening in an event?", "Call e.preventDefault() in the show.bs.modal handler."),
        VE("What is getOrCreateInstance()?", "A static method that returns the existing plug-in object of an element or creates a new one."),
    ]),
    G("Transition and Modal", [
        VE("What was the transition plug-in?", "A Bootstrap 3 helper (transition.js) that detected the end of CSS transitions for other plug-ins; built into each plug-in since Bootstrap 4."),
        VE("What do .fade and .show do?", ".fade adds an opacity transition and hides the element; .show makes it visible."),
        VE("What is a modal?", "A dialog box shown on top of the page with a dark backdrop."),
        VE("Name the parts of a modal.", ".modal > .modal-dialog > .modal-content with .modal-header, .modal-body and .modal-footer."),
        VE("How do you open a modal without JavaScript?", "A button with data-bs-toggle=\"modal\" and data-bs-target=\"#id\"."),
        VE("How do you close a modal?", "An element with data-bs-dismiss=\"modal\", the Esc key, a backdrop click, or the hide() method."),
        VE("What is a static backdrop?", "data-bs-backdrop=\"static\": the modal does not close when clicking outside it."),
        VE("Name the modal sizes.", ".modal-sm, default, .modal-lg, .modal-xl and .modal-fullscreen."),
        VE("List the modal options.", "backdrop, keyboard and focus."),
        VE("List the modal methods.", "show(), hide(), toggle(), handleUpdate(), dispose()."),
        VE("List the modal events.", "show.bs.modal, shown.bs.modal, hide.bs.modal, hidden.bs.modal, hidePrevented.bs.modal."),
        VE("What is e.relatedTarget in show.bs.modal?", "The button that was clicked to open the modal."),
    ]),
    G("Scrollspy, Tab, Dropdown", [
        VE("What is scrollspy?", "A plug-in that updates the active nav link according to the section visible while scrolling."),
        VE("Which attributes start scrollspy?", "data-bs-spy=\"scroll\" and data-bs-target=\"#nav\" on the scrolling element."),
        VE("Which event does scrollspy fire?", "activate.bs.scrollspy."),
        VE("When is the scrollspy refresh() method used?", "After sections are added to or removed from the page."),
        VE("How do you show a tab from JavaScript?", "bootstrap.Tab.getOrCreateInstance(link).show()."),
        VE("List the tab events in order.", "hide.bs.tab, show.bs.tab, hidden.bs.tab, shown.bs.tab."),
        VE("What does the dropdown autoClose option do?", "Decides which clicks close the menu: true, \"inside\", \"outside\" or false."),
        VE("List the dropdown events.", "show.bs.dropdown, shown.bs.dropdown, hide.bs.dropdown, hidden.bs.dropdown."),
    ]),
    G("Tooltip, Popover, Alert, Button", [
        VE("What is a tooltip?", "A small label shown on hover or focus, taken from the title attribute."),
        VE("Why must tooltips be initialised with JavaScript?", "They are opt-in for performance reasons: new bootstrap.Tooltip(el)."),
        VE("Name the tooltip placements.", "top, right, bottom, left and auto."),
        VE("List the tooltip methods.", "show(), hide(), toggle(), enable(), disable(), toggleEnabled(), setContent(), update(), dispose()."),
        VE("List the tooltip events.", "show.bs.tooltip, shown.bs.tooltip, hide.bs.tooltip, hidden.bs.tooltip, inserted.bs.tooltip."),
        VE("How do you show a tooltip on a disabled button?", "Put the tooltip on a wrapper span with tabindex=\"0\"."),
        VE("Difference between a tooltip and a popover?", "A tooltip shows short text on hover; a popover has a title and content and opens on click."),
        VE("How do you make a popover close on the next click?", "Use data-bs-trigger=\"focus\" on an <a> with tabindex=\"0\"."),
        VE("What does the alert plug-in do?", "Closes alerts with data-bs-dismiss=\"alert\" or the close() method."),
        VE("Which event fires after an alert is closed?", "closed.bs.alert."),
        VE("What does data-bs-toggle=\"button\" do?", "Makes a toggle button that switches the .active class and aria-pressed."),
        VE("How was the loading state of a button made in Bootstrap 3?", "$(btn).button(\"loading\") with data-loading-text; in Bootstrap 5, disable it and add a spinner with JavaScript."),
    ]),
    G("Collapse, Carousel, Affix", [
        VE("What is the collapse plug-in?", "It shows and hides content with a height animation."),
        VE("Which classes does collapse use?", ".collapse (hidden), .collapsing (animating) and .collapse.show (visible)."),
        VE("List the collapse options.", "parent and toggle."),
        VE("List the collapse events.", "show.bs.collapse, shown.bs.collapse, hide.bs.collapse, hidden.bs.collapse."),
        VE("How does an accordion keep only one item open?", "Each collapse has data-bs-parent pointing to the accordion."),
        VE("What is a carousel?", "A slideshow that cycles through images or content."),
        VE("Which attribute starts a carousel automatically?", "data-bs-ride=\"carousel\" (time set with data-bs-interval)."),
        VE("What are carousel indicators?", "Small bars or dots that show the current slide and jump to a slide with data-bs-slide-to."),
        VE("List the carousel methods.", "cycle(), pause(), prev(), next(), nextWhenVisible(), to(n), dispose()."),
        VE("Which carousel event fires after a slide changes?", "slid.bs.carousel (slide.bs.carousel at the start); e.to gives the new index."),
        VE("How do you make a carousel fade?", "Add .carousel-fade to the .carousel."),
        VE("What was the affix plug-in?", "A Bootstrap 3 plug-in that fixed an element after scrolling past an offset (data-spy=\"affix\" data-offset-top)."),
        VE("What replaces affix in Bootstrap 5?", "CSS position: sticky through .sticky-top (and .sticky-bottom)."),
        VE("Difference between .fixed-top and .sticky-top?", ".fixed-top is always fixed; .sticky-top scrolls normally until it reaches the top, then sticks."),
    ]),
]

EXAM_QS = [
    XE("What are Bootstrap plug-ins? Why are they used?", 3),
    XE("Explain the two ways of using Bootstrap plug-ins with an example.", 4),
    XE("Explain the transition plug-in.", 3),
    XE("Design a smooth page transition between home, about and contact us pages using the Bootstrap transition plug-in. (Practical 18)", 7),
    XE("Explain the modal plug-in with its structure.", 4),
    XE("Explain the properties, methods and events of the modal dialog box.", 4),
    XE("Design a web page with modal dialogs for save record confirmation and delete record confirmation. (Practical 19)", 7),
    XE("Explain the scrollspy plug-in with an example.", 4),
    XE("Explain the tab plug-in with its methods and events.", 3),
    XE("Explain the dropdown plug-in.", 3),
    XE("Explain the tooltip plug-in with its methods and events.", 4),
    XE("Explain the popover plug-in. Differentiate between tooltip and popover.", 4),
    XE("Design a news story page using scrollspy for multiple sections, tooltips for photos, and collapsible and popover plug-ins. (Practical 20)", 7),
    XE("Explain the alert and button plug-ins.", 3),
    XE("Explain the collapse plug-in with its properties, methods and events.", 4),
    XE("Create an accordion using the collapse plug-in.", 3),
    XE("Explain the carousel plug-in with its options, methods and events.", 4),
    XE("Design an animated photo gallery page using the carousel plug-in with at least seven photos. (Practical 21)", 7),
    XE("What was the affix plug-in? How is the same effect achieved in Bootstrap 5?", 3),
]
