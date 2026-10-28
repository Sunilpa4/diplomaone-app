"""DI03000061 Unit 5 notes: Bootstrap utilities and customization."""
from web_content import make_TS

SN = {
    "s_space": """
<div class="p-3 m-2">all sides</div>
<div class="pt-0 pb-4">top / bottom</div>
<div class="ps-2 me-auto">start / end</div>
<div class="px-3 py-1">x = left+right, y = top+bottom</div>
<div class="w-50 mx-auto">centre block</div>
<div class="d-flex gap-2">space between items</div>
<div class="mt-0 mt-md-3">responsive spacing</div>
""",
    "s_size": """
<img src="photo.jpg" class="w-50">   <!-- 50% of parent -->
<div class="w-25 w-50 w-75 w-100 w-auto"></div>
<div class="h-100" style="height: 200px">parent needs height</div>
<img class="mw-100">  <!-- never wider than screen -->
<section class="vh-100">full-screen section</section>
<div class="ratio ratio-16x9">
  <video> or <iframe>           <!-- keeps 16:9 shape -->
</div>
""",
    "s_display": """
<span class="d-block">              span -> block
<div class="d-inline-block w-25">  sized inline
<div class="d-none d-md-block">    hidden below 768px
<div class="d-md-none">            only below 768px
<span class="invisible">           hidden, keeps space
<span class="visually-hidden">     screen readers only
<button class="d-print-none">      hidden when printing
""",
    "s_position": """
<div class="position-relative">
  <span class="position-absolute top-0 start-0">
  <span class="position-absolute bottom-0 end-0">
  <span class="position-absolute top-50 start-50
        translate-middle">exact centre</span>
  <span class="position-absolute top-0 start-100
        translate-middle badge bg-danger">5</span>
</div>
<!-- edges: 0, 50, 100  = % of the parent -->
<!-- stack order: z-n1 z-0 z-1 z-2 z-3 -->
""",
    "s_flex": """
<div class="d-flex flex-column flex-md-row gap-2
     justify-content-between align-items-center">
  <div class="order-md-2">A</div>
  <div class="flex-grow-1">B takes free space</div>
  <div class="ms-md-auto">C pushed right</div>
</div>
""",
    "s_border": """
<div class="border">, border-top, border-end, ...
<div class="border border-top-0">   remove one side
<div class="border border-danger border-2">
<div class="border border-success border-opacity-25">
<div class="rounded-0 rounded rounded-3 rounded-5">
<div class="rounded-top rounded-bottom">
<div class="rounded-pill px-4">       pill / capsule
<div class="rounded-circle">          circle (w == h)
""",
    "s_bg": """
<div class="bg-primary text-white">
<div class="bg-primary bg-gradient">  light gradient
<span class="badge text-bg-warning">  bg + text colour
<div class="bg-success-subtle text-success-emphasis">
<div class="bg-success bg-opacity-25"> fade only the bg
<p class="text-primary">, text-body-secondary
<a class="link-danger"> link colour
""",
    "s_oos": """
<img class="opacity-50">          element half visible
<div class="overflow-auto" style="height:100px">
  scroll bar only when needed</div>
<div class="overflow-hidden">     cut off, no scroll
<div class="overflow-x-auto">     sideways scroll
<div class="shadow-sm shadow shadow-lg shadow-none">
""",
    "s_resp": """
<div class="text-center text-md-start">
<div class="d-flex flex-column flex-md-row">
<div class="p-2 p-md-4 mt-1 mt-lg-3">
<span class="d-none d-md-inline">desktop only</span>
<span class="float-md-end">        floats right >=768px
<!-- pattern: {utility}-{sm|md|lg|xl|xxl}-{value} -->
""",
    "s_header": """
<header class="bg-primary bg-gradient text-white shadow">
  <div class="container d-flex flex-wrap align-items-center
       justify-content-between gap-2 py-2">
    <a class="d-flex align-items-center gap-2 ...">logo</a>
    <ul class="nav order-3 order-md-2 ...">links</ul>
    <a class="btn btn-warning btn-sm rounded-pill
       order-2 order-md-3">Book now</a>
  </div>
</header>
""",
    "s_rootvars": """
<style>
  :root {
    --bs-primary: #7b1fa2;
    --bs-primary-rgb: 123, 31, 162;
    --bs-body-font-family: Georgia, serif;
    --bs-border-radius: 1rem;
  }
  /* buttons use their own variables */
  .btn-primary { --bs-btn-bg: var(--bs-primary); }
</style>
""",
    "s_sass_vars": """
// scss/_custom.scss - variables BEFORE the import
$primary: #198754;
$border-radius: 0.75rem;
@import "bootstrap/scss/bootstrap";

// build it:
// dart-sass scss/_custom.scss css/custom.css
// page links css/custom.css instead of bootstrap.css
""",
    "s_sass_comp": """
// component variables (before import)
$card-border-radius: 1rem;
$btn-border-radius: 0.5rem;

// add a brand colour to the Sass map:
$theme-colors: map-merge($theme-colors,
               ("brand": #7b1fa2));
// -> creates btn-brand, alert-brand, bg-brand, ...
// shrink output: map-remove($theme-colors, "cyan", ...)
""",
    "s_theme": """
<html data-bs-theme="dark">   <!-- whole page dark -->
<section data-bs-theme="dark"> <!-- one section dark -->

<style>
/* own theme = its own set of variables */
[data-bs-theme="brand"] {
  --bs-body-bg: #f3ecfa;
  --bs-body-color: #3c2352;
  --bs-primary: #7b2cd9;
  --bs-border-radius: 0.9rem;
}
</style>
""",
}

T = make_TS(SN)

SEC_5_1 = {
    "title": {"en": "5.1 Bootstrap Utilities"},
    "items": [
        T("Why Use Utility Classes and How They Are Named", """
<p>So far every page had to mix Bootstrap components with hand-written CSS for every small change: a little more space here, a border there. <b>Bootstrap utilities</b> are tiny, single-purpose CSS classes that add one style (margin, colour, border...) directly in the HTML.</p>
<h4>Benefits of using utilities</h4>
<ul><li><b>No custom CSS files</b> for small fixes - the same class works in every project.</li>
<li><b>Faster development:</b> spacing, sizes and colours are set while writing the markup.</li>
<li><b>Consistent look:</b> all values come from Bootstrap's scale (0-5), so the design stays uniform.</li>
<li><b>Responsive by default:</b> many utilities exist in breakpoint versions like <code>p-md-4</code>.</li>
<li><b>Small and safe:</b> using them does not add extra size to the downloaded CSS beyond bootstrap.css itself.</li></ul>
<h4>Naming rules</h4>
<ul><li>Spacing follows <b>{property}{sides}-{size}</b>: <code>mt-3</code> = margin-top of size 3.</li>
<li>Other families follow <b>{utility}-{value}</b>, e.g. <code>bg-primary</code>, <code>rounded-pill</code>, <code>shadow-lg</code>.</li>
<li>Responsive versions insert the breakpoint: <code>{utility}-{bp}-{value}</code>, e.g. <code>d-md-flex</code>.</li></ul>
@@s_space@@
""", diagram="web5_utility_class", programs=["w5_1"]),

        T("The Utility Families at a Glance", """
<p>The syllabus lists the utility families together; this topic maps each family to a typical class and use:</p>
<ul><li><b>Spacing</b> - margin, padding, gap (w5_1).</li>
<li><b>Sizing</b> - width, height, viewport, ratio (w5_2).</li>
<li><b>Display and visibility</b> - show, hide, flow (w5_3).</li>
<li><b>Positioning</b> - corners, centre, badges, z-index (w5_4).</li>
<li><b>Flexbox</b> - rows, columns, alignment (w5_5).</li>
<li><b>Border</b> - sides, colour, width, rounding (w5_6).</li>
<li><b>Background</b> - fills, gradient, subtle, opacity (w5_7).</li>
<li><b>Opacity, overflow, shadow</b> - transparency, clipping, depth (w5_8).</li>
<li>All families become <b>responsive</b> with a breakpoint infix (w5_9).</li></ul>
<p>The diagram is the complete cheat-sheet table; learn the family names for theory questions.</p>
""", diagram="web5_group_map"),

        T("Sizing Utilities", """
<p>Sizing utilities set <b>width and height as a percentage of the parent</b> (or fit content):</p>
<ul><li><b>Width:</b> <code>w-25</code> <code>w-50</code> <code>w-75</code> <code>w-100</code> <code>w-auto</code>; maximum <code>mw-100</code>.</li>
<li><b>Height:</b> <code>h-25</code> ... <code>h-100</code>, <code>h-auto</code>, <code>mh-100</code>. A percentage height works only if the parent has a height.</li>
<li><b>Viewport:</b> <code>vw-100</code>, <code>vh-100</code>, <code>min-vh-100</code> for full-screen sections.</li>
<li><b>Ratio:</b> <code>.ratio</code> with <code>ratio-1x1</code>, <code>ratio-4x3</code>, <code>ratio-16x9</code>, <code>ratio-21x9</code> keeps videos and iframes in proportion on any screen.</li></ul>
@@s_size@@
<p>Try the live example: blue bars at 25-100% width, green bars at 25-100% height, a banner limited by <code>mw-100</code> and a 16:9 video box.</p>
""", programs=["w5_2"]),

        T("Display and Visibility Utilities", """
<p><b>Display utilities</b> control how an element takes part in the layout. Format: <code>d-{value}</code> or <code>d-{breakpoint}-{value}</code>.</p>
<ul><li>Values: <code>none</code>, <code>inline</code>, <code>inline-block</code>, <code>block</code>, <code>table</code>, <code>flex</code>, <code>inline-flex</code>, <code>grid</code>.</li>
<li><b>Responsive hiding:</b> <code>d-md-none</code> hides from 768 px up; <code>d-none d-md-block</code> shows only from 768 px. Combine them for different phone and desktop layouts.</li>
<li><b>Visibility</b> is different: <code>.invisible</code> hides but keeps the space in the layout; <code>d-none</code> removes the space completely.</li>
<li><code>.visually-hidden</code> keeps content for screen readers only.</li>
<li><code>.d-print-*</code> controls printing, e.g. hide a Print button on paper.</li></ul>
@@s_display@@
<p>The live example shows a <b>breakpoint badge</b> that always displays the current screen size - the trick used in many real websites.</p>
""", programs=["w5_3"]),

        T("Position Utilities", """
<p>Position utilities place elements without writing CSS:</p>
<ul><li><b>position-*:</b> static, relative, absolute, fixed, sticky.</li>
<li><b>Edge placement:</b> <code>top-0</code>, <code>bottom-0</code>, <code>start-0</code>, <code>end-0</code>, also 50 and 100 (percentages).</li>
<li><b>translate-middle</b> shifts the element back by half of its own size, so <code>top-50 start-50 translate-middle</code> centres it exactly inside a <code>position-relative</code> parent. The classic badge on a button uses <code>top-0 start-100 translate-middle</code>.</li>
<li><b>z-index:</b> <code>z-n1</code>, <code>z-0</code> ... <code>z-3</code> control which overlapping element is in front.</li>
<li>Shortcuts: <code>.fixed-top</code>, <code>.fixed-bottom</code>, <code>.sticky-top</code>.</li></ul>
@@s_position@@
""", programs=["w5_4"]),

        T("Flexbox Utilities", """
<p><b>Flexbox</b> lays items out in one direction with automatic spacing and alignment. Add <code>d-flex</code> to any container and tune it with utilities:</p>
<ul><li><b>Direction:</b> <code>flex-row</code> (default), <code>flex-column</code>, and <code>*-reverse</code> versions; responsive with <code>flex-md-row</code>.</li>
<li><b>Main axis</b> (along the direction) is controlled by <code>justify-content-</code>start / center / end / between / around / evenly.</li>
<li><b>Cross axis</b> by <code>align-items-</code>start / center / end / baseline / stretch; <code>align-self-*</code> overrides one item, <code>align-content-*</code> spaces wrapped lines.</li>
<li><b>Wrapping:</b> <code>flex-wrap</code> sends extra items to a new line.</li>
<li><b>Per item:</b> <code>order-0..5</code>, <code>flex-grow-1</code> (fill free space), <code>ms-auto</code> (push apart).</li></ul>
@@s_flex@@
<p>The live example has drop-downs for both axes and a stacked-on-phone / row-on-desktop layout - the standard pattern for headers and cards.</p>
""", diagram="web5_flex_axes", programs=["w5_5"]),

        T("Border and Rounded-Corner Utilities", """
<ul><li><b>Add:</b> <code>border</code>, <code>border-top</code>, <code>border-end</code>, <code>border-bottom</code>, <code>border-start</code>.</li>
<li><b>Remove:</b> <code>border-0</code>, <code>border-top-0</code> ...</li>
<li><b>Colour:</b> <code>border-primary</code>, <code>border-danger</code>, <code>border-success-subtle</code> ...; set <code>border</code> first (it creates the edge), then colour it.</li>
<li><b>Width:</b> <code>border-1</code> to <code>border-5</code>; <b>opacity:</b> <code>border-opacity-10/25/50/75</code>.</li>
<li><b>Rounding:</b> <code>rounded</code>, <code>rounded-0</code> ... <code>rounded-5</code> (corner size), <code>rounded-top/-end/-bottom/-start</code> (one side), <code>rounded-pill</code> (capsule), <code>rounded-circle</code> (needs equal width and height).</li></ul>
@@s_border@@
""", programs=["w5_6"]),

        T("Background and Text Colour Utilities", """
<ul><li><b>Fills:</b> <code>bg-primary</code>, <code>-secondary</code>, <code>-success</code>, <code>-danger</code>, <code>-warning</code>, <code>-info</code>, <code>-light</code>, <code>-dark</code>, <code>-white</code>, <code>-transparent</code>, <code>bg-body</code>, <code>bg-body-secondary</code>/<code>-tertiary</code>.</li>
<li><b>text-bg-*</b> sets the fill AND a readable text colour together - ideal for badges and dark headers.</li>
<li><b>bg-gradient</b> adds a subtle light-to-dark gradient over any fill.</li>
<li><b>Subtle colours:</b> <code>bg-*-subtle</code> with <code>text-*-emphasis</code> for soft highlight panels (Bootstrap 5.3).</li>
<li><b>bg-opacity-*</b> fades only the background, leaving text solid.</li>
<li><b>Text:</b> <code>text-primary</code> ... <code>text-body-secondary</code> (muted), <code>text-white-50</code>; <b>links:</b> <code>link-*</code> and <code>link-underline-opacity-0</code>.</li></ul>
@@s_bg@@
<p>Background and text colour utilities are <b>not responsive</b> - a colour stays the same on all screen sizes.</p>
""", programs=["w5_7"]),

        T("Opacity, Overflow and Shadow Utilities", """
<ul><li><b>Opacity</b> <code>opacity-0/25/50/75/100</code> makes the whole element - including its text and children - transparent. Use <code>bg-opacity-*</code> when only the background should fade.</li>
<li><b>Overflow</b> decides what happens when content is bigger than its box: <code>overflow-auto</code> (scroll bar when needed), <code>overflow-hidden</code> (clip it, e.g. to keep round corners on an image), <code>overflow-visible</code> (default), <code>overflow-scroll</code> (always scroll bars); single direction with <code>overflow-x-*</code> / <code>overflow-y-*</code>. Requires a fixed height/width on the box.</li>
<li><b>Shadow</b> gives depth: <code>shadow-none</code> <code>shadow-sm</code> <code>shadow</code> <code>shadow-lg</code>; very common on cards, fixed navbars and FAB buttons.</li></ul>
@@s_oos@@
""", programs=["w5_8"]),

        T("Responsive Utilities: the Breakpoint Infix", """
<p>Bootstrap is <b>mobile first</b>: a class without a breakpoint applies to <b>all</b> screens, and a class with a breakpoint overrides it from that width <b>up</b>:</p>
<ul><li><code>{utility}-{bp}-{value}</code> where bp = <code>sm</code> (576), <code>md</code> (768), <code>lg</code> (992), <code>xl</code> (1200), <code>xxl</code> (1400 px).</li>
<li><code>d-none d-md-block</code>: hidden on phones, visible from tablets. <code>flex-column flex-md-row</code>: stack on phones, row from tablets.</li>
<li>Responsive families: display, flex (direction, justify, align, order), spacing, text alignment (<code>text-md-start</code>), float (<code>float-md-end</code>), sticky (<code>sticky-md-top</code>) and grid columns.</li>
<li><b>Not responsive:</b> width/height (<code>w-50</code>), colours, borders, shadows - add your own small media-query class like <code>.w-md-auto</code> in the live page, or generate them with the Sass utility API.</li></ul>
@@s_resp@@
""", diagram="web5_responsive", programs=["w5_9"]),

        T("Practical 22: Header and Footer with Only Utility Classes", """
<p>The practical asks for a tourism website header and footer built <b>only with utility classes</b> (no custom CSS beyond one helper). The live program shows the keys:</p>
<ul><li><b>Header layout</b> is pure flexbox: <code>d-flex flex-wrap align-items-center justify-content-between gap-2</code>.</li>
<li><b>Responsive order:</b> <code>order-3 order-md-2</code> puts the menu on a second line on phones and between logo and button on desktops.</li>
<li><b>Colours and depth:</b> <code>bg-primary bg-gradient</code>, <code>shadow</code>, <code>text-white-50</code>, <code>link-light</code>.</li>
<li><b>Footer grid:</b> <code>col-12 col-md-5</code> etc. give 1 column on a phone and 3 on a desktop; <code>border-top border-secondary</code> separates the copyright line.</li>
<li>Typography classes do the text design: <code>fs-5</code>, <code>fw-bold</code>, <code>small</code>, <code>text-body-secondary</code>.</li></ul>
@@s_header@@
""", programs=["w5_10"]),
    ],
}

SEC_5_2 = {
    "title": {"en": "5.2 Bootstrap Customization"},
    "items": [
        T("Why Customize Bootstrap and the Five Levels", """
<p>Default Bootstrap is safe but generic - every site looks the same blue. <b>Customization</b> makes the framework match your own brand and your own components.</p>
<h4>Benefits of customizing Bootstrap</h4>
<ul><li><b>Brand identity</b> - your colours, fonts and corner styles instead of defaults.</li>
<li><b>Smaller CSS</b> - keep only the colours and utilities you use.</li>
<li><b>Design that updates itself:</b> change one variable and every component follows, no class-by-class patching.</li>
<li><b>Consistency:</b> custom values become part of the same utility system (<code>btn-brand</code>, <code>bg-brand</code>).</li></ul>
<h4>The five levels (simple -> powerful)</h4>
<ol><li><b>CSS variables</b> on <code>:root</code> - change at runtime, no tools needed.</li>
<li><b>Sass variables</b> before the import - change the defaults for the whole library (<code>$primary</code>, <code>$border-radius</code>...).</li>
<li><b>Sass maps and the utility API</b> - add your own colours and utilities.</li>
<li><b>Component variables</b> - tune one component (<code>$card-border-radius</code>) without touching global defaults.</li>
<li><b>Themes</b> - a packaged set of levels 1-4 that gives the site a complete identity.</li></ol>
<p>The live program demonstrates level 1: overriding <code>--bs-primary</code> and friends on <code>:root</code>.</p>
@@s_rootvars@@
""", diagram="web5_customize_levels", programs=["w5_11"]),

        T("Customizing Bootstrap Variables with Sass", """
<p>Bootstrap is written in <b>Sass</b>, and its defaults are variables with <code>!default</code> - meaning <i>use this value only if nothing else was set</i>. That single feature powers the whole customization system:</p>
<ol><li>Create your own file, e.g. <code>scss/_custom.scss</code>.</li>
<li><b>Set variables BEFORE the import line</b>: <code>$primary: #198754;</code>, <code>$border-radius: 0.75rem;</code> - your values replace the <code>!default</code> values.</li>
<li>Import Bootstrap: <code>@import "bootstrap/scss/bootstrap";</code>.</li>
<li>Compile: <code>dart-sass scss/_custom.scss css/custom.css</code> (or an npm script).</li>
<li>Link <code>custom.css</code> <b>instead of</b> bootstrap.css on every page.</li></ol>
<ul><li>Files starting with an underscore (<code>_variables.scss</code>) are <b>partials</b> - they are merged into the build, not compiled alone.</li>
<li>Recompile whenever a variable changes; editors like VS Code can rebuild on save.</li>
<li>The live program (Practical 23) shows the Sass source and the compiled result side by side as you change the brand colour and corner radius.</li></ul>
@@s_sass_vars@@
""", diagram="web5_sass_flow", programs=["w5_12"]),

        T("Customizing Bootstrap Components with Sass", """
<p>Every component also has its own Sass variables, so one component can be restyled <b>without</b> changing the global defaults:</p>
<ul><li>Examples: <code>$card-border-radius</code>, <code>$card-box-shadow</code>, <code>$btn-border-radius</code>, <code>$navbar-padding-y</code>, <code>$modal-content-border-width</code>. They are documented at the bottom of each component's page.</li>
<li>Set them before the import, compile, and that component alone keeps the new shape everywhere.</li></ul>
<h4>Sass maps: your own theme colours</h4>
<ul><li>Bootstrap's colours live in the <code>$theme-colors</code> map. <code>map-merge</code> adds colours; Bootstrap then automatically creates <code>btn-brand</code>, <code>alert-brand</code>, <code>bg-brand</code>, <code>text-brand</code> ... with correct hover and contrast.</li>
<li><code>map-remove</code> drops colours you never use, shrinking the compiled CSS.</li>
<li>The <b>utility API</b> works the same way: its <code>$utilities</code> map can be extended to generate e.g. responsive width classes (<code>w-md-25</code>).</li></ul>
@@s_sass_comp@@
<p>The live program (Practical 24a) lets you drag the card corner radius and shows the exact Sass source that produces the result.</p>
""", programs=["w5_13"]),

        T("Customizing Bootstrap Themes", """
<p>A <b>theme</b> is a complete, documented set of variable and component overrides that gives the site its identity.</p>
<ul><li>Bootstrap 5.3 ships two built-in <b>colour modes</b>: <code>light</code> and <code>dark</code>. Set <code>data-bs-theme="dark"</code> on <code>&lt;html&gt;</code> (whole page) or on any section - every component adapts automatically.</li>
<li><b>Custom themes</b> are built by overriding CSS variables under your own <code>[data-bs-theme="name"]</code> selector (as in the demo), or by compiling a separate Sass build per theme.</li>
<li><b>Packaged themes</b> (Bootswatch, Start Bootstrap) are exactly such override sets - install one and its classes are still plain Bootstrap.</li></ul>
<h4>Rules for themable markup</h4>
<ul><li>Style with <b>semantic classes</b>: <code>text-bg-primary</code>, <code>btn-primary</code>, <code>bg-body</code> - never hard-coded hex colours.</li>
<li>Then a theme switch only changes variables, and the whole site flips cleanly - as the dropdown in the live program (Practical 24b) shows.</li></ul>
@@s_theme@@
""", diagram="web5_themes", programs=["w5_14"]),
    ],
}

NOTES = [SEC_5_1, SEC_5_2]
