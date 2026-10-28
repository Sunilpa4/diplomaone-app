"""DI03000061 Unit 2 extras: syntax sheet, viva, exam (practical) questions."""
from web_content import SXE, VE, XE, G
from content_DI03000061_u2_notes import SN


def S(name, key, terms=""):
    return SXE(name, SN[key].strip("\n"), terms)


SYNTAX = [
    G("Grid System", [
        S("Basic grid", "s_grid", "container > row > col. 12 columns per row."),
        S("Column classes", "s_grid_classes", ".col, .col-n, .col-bp-n, .col-auto, .row-cols-n"),
        S("Containers", "s_containers", ".container fixed, .container-fluid 100%, .container-bp mixed."),
        S("Gutters", "s_gutters", "g-0 to g-5; gx horizontal, gy vertical."),
        S("Offset", "s_offset", "offset-bp-n adds n empty columns on the left."),
        S("Reordering", "s_order", "order-0..5, order-first, order-last; responsive order-md-*."),
        S("Nesting", "s_nesting", "New .row inside a column; 12 columns of the parent width."),
    ]),
    G("Images", [
        S("Image classes", "s_img", "img-fluid, rounded, rounded-circle, img-thumbnail."),
        S("Figure", "s_figure", "figure, figure-img, figure-caption."),
    ]),
    G("Typography", [
        S("Headings", "s_headings", ".h1-.h6, .display-1 to 6, .lead"),
        S("Inline text", "s_inline", "mark, del, s, ins, u, small, strong, em, abbr, kbd"),
        S("Blockquote", "s_blockquote", ".blockquote + .blockquote-footer"),
        S("Lists", "s_lists", ".list-unstyled, .list-inline + .list-inline-item"),
        S("Text utilities", "s_text", "Alignment, transform, weight, colour, truncate."),
    ]),
    G("Tables", [
        S("Table classes", "s_table", "table, striped, hover, bordered, sm, dark, table-success ..."),
        S("Responsive table", "s_table_resp", "Wrapper div scrolls horizontally on small screens."),
    ]),
    G("Forms", [
        S("Vertical form", "s_form_vertical", "mb-3 groups, form-label, form-control, form-text."),
        S("Horizontal form", "s_form_horizontal", "row + col-sm-2 col-form-label + col-sm-10."),
        S("Inline form", "s_form_inline", "row-cols-lg-auto + align-items-center."),
        S("Form controls", "s_controls", "form-select, form-check, form-switch, form-range, form-floating."),
        S("Validation", "s_validation", "novalidate, checkValidity(), .was-validated, .invalid-feedback."),
    ]),
    G("Buttons, Carets and Display", [
        S("Buttons", "s_buttons", ".btn + variant; outline, lg/sm, disabled, d-grid block."),
        S("Caret", "s_caret", ".dropdown-toggle draws the caret."),
        S("Show / hide", "s_display", "d-none, d-bp-block, invisible, visually-hidden, d-print-none."),
    ]),
]

VIVA = [
    G("Grid System", [
        VE("What is the Bootstrap grid system?", "A mobile-first, flexbox-based layout system that divides the page into 12 columns using containers, rows and columns."),
        VE("How many columns does the Bootstrap grid have?", "12 columns per row."),
        VE("What are the three parts of the grid?", "Container, row and column."),
        VE("What happens if the columns in a row add up to more than 12?", "The extra column(s) wrap onto a new line."),
        VE("What is the difference between .container and .container-fluid?", ".container has a fixed max-width at each breakpoint and is centred; .container-fluid is always 100% wide."),
        VE("What is .container-md?", "A container that is 100% wide below the md breakpoint (768 px) and fixed width from md upward."),
        VE("What does col-md-6 mean?", "The column takes 6 of 12 columns (half width) on screens 768 px and wider; on smaller screens it is full width."),
        VE("What does .col (without a number) do?", "It creates equal-width columns that share the row automatically."),
        VE("What is .col-auto?", "A column whose width depends on its content."),
        VE("What is a gutter?", "The space (padding) between columns, controlled with g-*, gx-* and gy-* classes."),
        VE("What is an offset?", "Empty columns added to the left of a column to move it right, e.g. offset-md-3."),
        VE("How can a column be centred using offset?", "col-md-6 offset-md-3 (3 + 6 + 3 = 12)."),
        VE("What is column reordering?", "Changing the visual order of columns without changing the HTML, using order-* classes."),
        VE("Which CSS property is used by order classes?", "The flexbox order property."),
        VE("What replaced push and pull classes of Bootstrap 3?", "The order-* classes (order-first, order-last, order-md-2 etc.)."),
        VE("What is nesting of columns?", "Placing a new row with columns inside an existing column."),
        VE("In nesting, the 12 columns are relative to what?", "The width of the parent column."),
        VE("List two advantages of the Bootstrap grid.", "Automatic responsive layouts without media queries, and flexible column sizes with offset, ordering and nesting."),
    ]),
    G("Images, Typography and Tables", [
        VE("Which class makes an image responsive?", ".img-fluid (max-width: 100%; height: auto). Bootstrap 3 used .img-responsive."),
        VE("How do you make a circular image?", "Add .rounded-circle to a square image."),
        VE("What does .img-thumbnail do?", "Adds a 1 px border, padding and rounded corners like a thumbnail."),
        VE("How can an image be centred?", "Use .d-block .mx-auto on the image, or .text-center on its parent."),
        VE("What is the default font size in Bootstrap 5?", "1rem, normally 16 px."),
        VE("What are display headings?", "Large, lighter headings with classes .display-1 to .display-6."),
        VE("What does the .lead class do?", "Makes a paragraph larger so it stands out."),
        VE("Which tag highlights text?", "The mark element."),
        VE("What is the use of .list-unstyled?", "It removes bullets and left padding from a list."),
        VE("Which classes align text?", "text-start, text-center and text-end (also responsive like text-md-center)."),
        VE("Which class is needed on every Bootstrap table?", ".table"),
        VE("How do you create a striped table?", "Add .table-striped to the table."),
        VE("What does .table-hover do?", "Highlights a table row when the mouse is over it."),
        VE("How do you make a table responsive?", "Wrap it in a div with class .table-responsive so it scrolls horizontally on small screens."),
        VE("Name some contextual table classes.", "table-primary, table-success, table-danger, table-warning, table-info, table-active."),
    ]),
    G("Forms, Buttons, Carets and Display", [
        VE("Name the form layouts in Bootstrap.", "Vertical (default), grid, horizontal and inline."),
        VE("Which class styles text inputs?", ".form-control"),
        VE("Which class styles a select box in Bootstrap 5?", ".form-select"),
        VE("How is a horizontal form created?", "Each field is a .row; the label uses a column class with .col-form-label and the input is placed in another column."),
        VE("What are floating labels?", "Labels shown inside the input that move up when the user types; created with .form-floating."),
        VE("How do you create a switch?", "Add .form-switch to the .form-check of a checkbox."),
        VE("What is the use of novalidate?", "It disables the browser's default validation pop-ups so Bootstrap's styled messages can be shown."),
        VE("What does .was-validated do?", "Shows valid (green) or invalid (red) styles and feedback messages for all fields in the form."),
        VE("What is the base class of a Bootstrap button?", ".btn"),
        VE("How do you create an outline button?", "Use btn-outline-* classes, e.g. btn-outline-primary."),
        VE("How is a full-width (block) button made in Bootstrap 5?", "Place it in a wrapper with .d-grid (Bootstrap 4 used .btn-block)."),
        VE("What is a caret?", "A small triangle that shows a button or link opens a dropdown menu."),
        VE("How is a caret added in Bootstrap 5?", "The .dropdown-toggle class adds it automatically (Bootstrap 3 used span.caret)."),
        VE("How do you hide an element on phones only?", "Use .d-none .d-md-block (or .d-sm-block)."),
        VE("Difference between .d-none and .invisible?", ".d-none removes the element from the layout; .invisible hides it but keeps its space."),
        VE("What is .visually-hidden?", "Hides content visually but keeps it for screen readers (Bootstrap 3/4: .sr-only)."),
    ]),
]

EXAM_QS = [
    XE("Explain the Bootstrap grid system with an example.", 4),
    XE("Explain container, container-fluid and responsive containers. (Practical 3)", 4),
    XE("Display student information on a responsive web page using container and container-fluid classes. (Practical 3)", 4),
    XE("Explain offset columns with an example.", 3),
    XE("Explain reordering of columns with an example.", 3),
    XE("Explain nesting of columns with an example.", 3),
    XE("Create a responsive web page using offset, reordering and nesting columns. (Practical 4)", 7),
    XE("List the advantages of the Bootstrap grid system.", 3),
    XE("Create a responsive class time table using the Bootstrap grid system. (Practical 5)", 7),
    XE("Explain responsive images and image shape classes in Bootstrap.", 4),
    XE("Explain table classes in Bootstrap with examples.", 4),
    XE("Create a responsive page showing student activities with images in different styles and tables in different styles. (Practical 6)", 7),
    XE("Explain Bootstrap typography classes.", 4),
    XE("Create a responsive blog page using Bootstrap typography. (Practical 7)", 4),
    XE("Explain different form layouts in Bootstrap.", 4),
    XE("Explain Bootstrap button classes with examples.", 3),
    XE("Design a responsive student registration form using form layout, form controls and buttons. (Practical 8)", 7),
    XE("What is a caret? How is it created in Bootstrap 5?", 3),
    XE("How can text be shown or hidden on different screen sizes in Bootstrap?", 4),
]
