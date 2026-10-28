"""DI03000061 Unit 5 extras: syntax sheet, viva, exam (practical) questions."""
from web_content import SXE, VE, XE, G
from content_DI03000061_u5_notes import SN


def S(name, key, terms=""):
    return SXE(name, SN[key].strip("\n"), terms)


SYNTAX = [
    G("Spacing, Sizing, Display", [
        S("Spacing classes", "s_space", "{m|p}{t|b|s|e|x|y}-{0..5|auto}; gap-*, mx-auto"),
        S("Sizing classes", "s_size", "w-*/h-*/mw-100/vh-100; .ratio ratio-16x9"),
        S("Display and visibility", "s_display", "d-{bp}-{value}; invisible; visually-hidden; d-print-*"),
    ]),
    G("Position and Flexbox", [
        S("Position classes", "s_position", "position-*; top/start {0|50|100}; translate-middle; z-1..3"),
        S("Flexbox classes", "s_flex", "d-flex; justify-content-*; align-items-*; order-*; flex-grow-1"),
    ]),
    G("Colours, Borders and Effects", [
        S("Border classes", "s_border", "border[-side][-0]; border-{color}; border-{1..5}; rounded/pill/circle"),
        S("Background classes", "s_bg", "bg-*; bg-gradient; text-bg-*; bg-opacity-*; subtle + emphasis"),
        S("Opacity, overflow, shadow", "s_oos", "opacity-{0|25|50|75|100}; overflow{-x|-y}-{auto|hidden|scroll|visible}; shadow-{none|sm||lg}"),
    ]),
    G("Responsive and Customization", [
        S("Responsive infix", "s_resp", "{utility}-{sm|md|lg|xl|xxl}-{value}; larger breakpoint overrides"),
        S("CSS variables (:root)", "s_rootvars", "override --bs-primary/-rgb, font, radius at runtime"),
        S("Sass variables", "s_sass_vars", "set $vars before @import; dart-sass -> custom.css"),
        S("Components and maps", "s_sass_comp", "$card-*, $btn-*; map-merge adds brand colours and utilities"),
        S("Themes", "s_theme", "data-bs-theme=\"dark\"; [data-bs-theme=name] { --bs-... }"),
    ]),
]

_VIVA = [
    VE("What are Bootstrap utilities?", "Tiny single-purpose CSS classes (margin, colour, border...) applied in HTML instead of writing custom CSS."),
    VE("Give four benefits of using utilities.", "No custom CSS files, faster development, consistent values from Bootstrap's scale, and responsive versions for many utilities."),
    VE("What does mt-3 mean?", "Margin-Top of size 3 = 1rem. m = margin, t = top, 3 = third step of the spacing scale."),
    VE("What are the spacing sizes 0 to 5?", "0, 0.25rem, 0.5rem, 1rem, 1.5rem and 3rem; \"auto\" also exists for margins."),
    VE("What do s and e mean in ms-2, pe-3?", "Start and end: s = left, e = right (Bootstrap 4 used l and r)."),
    VE("What does mx-auto do?", "Sets left and right margins to auto, centring a block element that has a width."),
    VE("What is gap-3 used for?", "Equal 1rem space between items of a flex or grid container; row-gap and column-gap set one direction only."),
    VE("Differentiate w-50 and mw-100.", "w-50 fixes the width to 50% of the parent; mw-100 only limits the width to never exceed the parent (max-width: 100%)."),
    VE("When does h-50 work?", "Only when the parent element has a height set; percentages are relative to the parent's height."),
    VE("What are vh-100 and vw-100?", "100% of the viewport height and width, used for full-screen sections."),
    VE("What is .ratio-16x9?", "A box that keeps a 16:9 aspect ratio on any screen, used for videos and iframes."),
    VE("List some display values available as utilities.", "none, inline, inline-block, block, table, flex, inline-flex, grid."),
    VE("How do you hide an element only on phones?", "d-none d-sm-block (or d-md-block) - hidden below the breakpoint, shown above."),
    VE("d-none vs invisible?", "d-none removes the element from the layout; invisible hides it but keeps its space (visibility: hidden)."),
    VE("What is .visually-hidden for?", "Content hidden from sighted users but still read by screen readers (accessibility)."),
    VE("What are d-print-none and d-print-block?", "Print utilities: they show or hide content specifically in the printed output."),
    VE("Why does position-absolute need a relative parent?", "An absolutely positioned element is placed relative to the nearest ancestor with position: relative (or any non-static position)."),
    VE("Write classes to place a badge on a button's top-right corner.", "Button: position-relative; badge: position-absolute top-0 start-100 translate-middle."),
    VE("What does translate-middle do?", "Translates the element by -50% of its own width and height, so top-50 start-50 centres it exactly."),
    VE("What is z-3 used for?", "z-index stacking: elements with higher z-index values are drawn on top of overlapping elements."),
    VE("List five flexbox direction and alignment classes.", "flex-row, flex-column, justify-content-center (main axis), align-items-end (cross axis), flex-wrap."),
    VE("justify-content vs align-items?", "justify-content spaces items along the main axis; align-items aligns them on the cross axis."),
    VE("What are space-between, space-around and space-evenly?", "justify-content values: largest gaps only between items / equal space inside and half outside / equal space everywhere."),
    VE("How do you stack items on a phone but show a row from tablets?", "d-flex flex-column flex-md-row."),
    VE("What do order-md-2 and flex-grow-1 do?", "order-md-2 moves the item later from md up; flex-grow-1 makes the item take the container's free space."),
    VE("How does ms-auto help in a flex row?", "Auto margin pushes that item and everything after it to the far side (e.g. logout button at the right)."),
    VE("Why set border before border-danger?", "The border utility creates the 1px edge; colour utilities only recolour an existing border."),
    VE("Difference between rounded-pill and rounded-circle?", "Pill rounds any rectangle into a capsule; circle needs equal width and height to make a perfect circle."),
    VE("What does text-bg-* do?", "Bootstrap 5.3 class that sets the background colour AND a contrasting text colour in one class."),
    VE("bg-opacity-25 vs opacity-25?", "bg-opacity-25 fades only the background; opacity-25 fades the whole element including its text."),
    VE("What are bg-*-subtle and text-*-emphasis?", "Soft background tints with matching readable text colours, for gentle highlight panels (Bootstrap 5.3)."),
    VE("overflow-auto vs overflow-hidden?", "Auto shows scroll bars only when content overflows; hidden clips the overflowing content with no scrolling."),
    VE("What must an overflow box have to work?", "A fixed height or width, otherwise the box just grows with its content."),
    VE("Which shadow utilities exist?", "shadow-none, shadow-sm, shadow and shadow-lg."),
    VE("What is the breakpoint infix rule?", "{utility}-{sm|md|lg|xl|xxl}-{value}; the base class applies everywhere and the breakpoint class overrides from that width up."),
    VE("Which utilities are NOT responsive by default?", "Widths and heights (w-*, h-*), colours, borders and shadows; design has not been compiled with them; use a custom class or the Sass utility API."),
    VE("Why is Bootstrap called mobile first?", "Styles apply to the smallest screens by default and md/lg media queries only ADD changes for larger screens."),
    VE("Why customize Bootstrap at all?", "For brand identity, smaller CSS, automatic site-wide updates from one variable and design consistency."),
    VE("What are Bootstrap CSS variables? Examples.", "Custom properties on :root: --bs-primary, --bs-primary-rgb, --bs-body-font-family, --bs-border-radius; overriding them restyles the site at runtime."),
    VE("Why override --bs-primary-rgb too?", "Many effects (shadows, semi-transparent fills) build the colour from the RGB triplet, so both must stay in sync."),
    VE("Where is Sass used in Bootstrap customization?", "Bootstrap's source is Sass; its defaults are variables with !default that our custom file overrides, then a compiler (Dart Sass) builds a custom bootstrap.css."),
    VE("What does !default mean in Sass?", "\"Use this value only if it is not already set\" - so our variables written before the import always win."),
    VE("Where should custom Sass variables be placed?", "Before the @import of Bootstrap in the custom .scss file."),
    VE("What is a Sass partial?", "A .scss file whose name starts with an underscore; it is imported into other files and not compiled on its own."),
    VE("How do you compile Sass to CSS?", "With Dart Sass: dart-sass input.scss output.css, usually through an npm build script."),
    VE("What are component variables? Give two.", "Variables that tune one component: e.g. $card-border-radius, $btn-border-radius, $navbar-padding-y."),
    VE("What is a Sass map in Bootstrap?", "A key-value list like $theme-colors; adding a key with map-merge creates every utility and component variant for that colour."),
    VE("What does map-merge($theme-colors, (\"brand\": #7b1fa2)) create?", "btn-brand, alert-brand, bg-brand, text-brand, border-brand and friends, with proper hover and contrast states."),
    VE("How do you make the compiled CSS smaller?", "Remove unused colours with map-remove and import only the needed Bootstrap modules."),
    VE("What is a Bootstrap theme?", "A packaged set of variable and component overrides (colours, radius, shadows, fonts) giving the site a consistent identity."),
    VE("How do you enable dark mode in Bootstrap 5.3?", "Set data-bs-theme=\"dark\" on the html element or on any section; all components adapt automatically."),
    VE("How do you build a custom colour mode?", "Define a [data-bs-theme=\"name\"] selector that overrides the CSS variables, then apply the attribute where wanted."),
    VE("What rule keeps markup themable?", "Use semantic classes (btn-primary, text-bg-primary, bg-body) and never hard-coded hex colours, so themes can restyle everything."),
]

EXAM_QS = [
    XE("What are Bootstrap utilities? State their benefits.", 3),
    XE("Explain the naming rule of spacing utilities with the pattern and examples.", 4),
    XE("Write a class for each: padding 1.5rem on all sides from 768px; margin removed at the start; a block centred horizontally.", 4),
    XE("Explain w-50, mw-100 and h-100 with an example each; when does h-100 fail?", 4),
    XE("Explain sizing utilities for full-screen sections and for a 16:9 video.", 3),
    XE("Differentiate display utilities and visibility utilities with examples.", 4),
    XE("Design a breakpoint badge using only Bootstrap classes. (Ref: w5_3)", 4),
    XE("Explain position utilities with the example of a notification badge on a button. (Ref: w5_4)", 4),
    XE("Explain z-index utilities with overlapping boxes.", 3),
    XE("Explain flexbox utilities: direction, justify-content, align-items, wrap, order and flex-grow. (Ref: w5_5)", 6),
    XE("Show how mt-auto or ms-auto positions items in a flex container.", 3),
    XE("Explain border utilities: sides, colours, widths, opacity and rounded variants.", 4),
    XE("Explain background utilities including gradient, subtle colours, text-bg-* and bg-opacity-*.", 4),
    XE("Explain opacity, overflow and shadow utilities with short examples.", 4),
    XE("Explain the responsive infix and mobile-first behaviour of utilities.", 4),
    XE("Develop the header and footer of a tourism website using only Bootstrap utility classes. (Practical 22 - w5_10)", 7),
    XE("Explain how to override Bootstrap using CSS variables on :root. (Ref: w5_11)", 4),
    XE("Explain the steps to customize Bootstrap variables with Sass, and build a custom bootstrap.css. (Practical 23 - w5_12)", 6),
    XE("Explain customizing Bootstrap components with Sass variables and map-merge. (Practical 24 - w5_13)", 6),
    XE("Explain Bootstrap colour modes and how to build a custom theme. (Practical 24 - w5_14)", 4),
]


assert len(_VIVA) == 53
VIVA = [
    G("Spacing and Sizing", _VIVA[0:11]),
    G("Display, Visibility, Position", _VIVA[11:20]),
    G("Flexbox", _VIVA[20:26]),
    G("Colours, Borders, Overflow", _VIVA[26:34]),
    G("Responsive Behaviour", _VIVA[34:37]),
    G("Customization: Variables and Sass", _VIVA[37:45]),
    G("Components, Maps and Themes", _VIVA[45:53]),
]
