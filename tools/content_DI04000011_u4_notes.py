"""DI04000011 Unit 4 notes: Coding and Testing. English only."""

from java_content import make_TJ

SN = {}

T = make_TJ(SN)

SEC_4_1 = {
    "title": {"en": "4.1 Coding: Standards, Reviews and Documentation"},
    "items": [
        T("Coding Standards and Guidelines", """
<ul><li>The coding phase translates the detailed design into source code a machine can run - and humans can still <b>read, debug and modify</b> for years.</li>
<li><b>Coding standards</b> are mandatory rules a team imposes: naming conventions (camelCase for methods, ALL_CAPS for constants), a fixed indentation/layout style, rules for comment density, allowed error-handling style, limits on global variables and <b>no GOTOs</b>.</li>
<li><b>Coding guidelines</b> are softer advice: write code for the reader first; keep functions small; avoid obscure tricks; check return values; keep side-effects out of expressions.</li>
<li><b>Why they matter</b>: code is read 10x more often than it is written. Uniform style means any team member can maintain any module, reviews go faster, and common bug classes (dangling pointers, unchecked inputs) are designed out.</li>
<li>Tool support: linters and IDE formatters enforce standards automatically - the rule is debated once, then never again.</li></ul>
""", diagram="se4_standards"),
        T("Code Review: Walkthrough and Inspection", """
<ul><li><b>Static verification</b>: humans examine a work product (code, design, SRS) <b>before it runs</b>. Eyeballs find defects testing can only reach much later - and for about 1/100th of the repair cost.</li>
<li><b>Code walkthrough</b>: informal. The author walks the team through the code line by line, narrating intent; members raise questions and spot issues. Author leads, preparation is light, output is discussion and comments.</li>
<li><b>Code inspection</b>: formal (Fagan). Defined roles - moderator, author, readers, recorder - each member prepares with <b>checklists</b> (uninitialised variables? array bounds? null handling?), the meeting logs every defect, and fixes are verified later. Goal: <b>find defects now</b>, not share knowledge.</li>
<li>Difference table (exam favourite): walkthrough = author-led, informal, little preparation, knowledge sharing; inspection = moderator-led, highly formal, checklist preparation, defect log.</li>
<li>Reviews apply to every phase product - SRS review and design review catch errors where they are cheapest.</li></ul>
""", diagram="se4_review"),
        T("Internal and External Documentation", """
<ul><li><b>Internal documentation</b> lives inside the code: header comments per class and module (purpose, author, date, change log), comments explaining <i>why</i> (the <i>what</i> is the code's job), meaningful identifiers, and doc-strings that tools turn into API docs.</li>
<li><b>External documentation</b> lives beside the code: user manual, installation guide, SRS and design documents, API reference, maintenance manual.</li>
<li>Audience split: internal serves the <b>next developer</b> (future you), external serves <b>users, testers and reviewers</b>.</li>
<li>Documentation is a <b>deliverable, not an afterthought</b>: an undocumented program is unmaintainable no matter how clever, and untestable by anyone but its author.</li>
<li>Rule of thumb: comment the intent ("retry once because the bus API drops connections"), not the mechanics ("increment i by 1").</li></ul>
""", diagram="se4_docs"),
    ],
}

SEC_4_2 = {
    "title": {"en": "4.2 Testing Fundamentals"},
    "items": [
        T("Why Test, V&V, and the Psychology of Testing", """
<ul><li><b>Objective of testing</b> (Myers): testing is the process of executing a program <b>with the intent of finding errors</b>. A successful test is one that <b>finds a fault</b> - not one that passes.</li>
<li>Testing shows the <b>presence</b> of bugs, never their absence (Dijkstra) - so we test as thoroughly as budget allows, prioritising risky areas.</li>
<li>Vocabulary: <b>error</b> = human mistake; <b>fault/defect/bug</b> = the flaw written into the software; <b>failure</b> = observed wrong behaviour at run time.</li>
<li><b>Verification</b>: are we building the product right? (reviews, walkthroughs - checks against the previous phase's spec). <b>Validation</b>: are we building the right product? (testing against requirements - does it satisfy the customer?).</li>
<li>Psychology: developers should not be the sole judges of their own code - independent testers adopt a defect-hunting mindset the author cannot.</li></ul>
"""),
        T("Levels of Testing: Unit, Integration, System, Acceptance", """
<ul><li><b>Unit testing</b>: each module/function in isolation. Done by the developer, white-box flavoured, cheapest place to catch faults. Frameworks: JUnit for Java.</li>
<li><b>Integration testing</b>: modules wired together - tests the <b>interfaces</b>. Incremental strategies (top-down with stubs, bottom-up with drivers) beat big-bang because a failure points at a small set of suspects.</li>
<li><b>System testing</b>: the whole built product against the SRS - functionality plus performance, security, recovery, load. Black-box; the test team owns it.</li>
<li><b>Acceptance testing</b>: the customer's verdict - is this the right product? Alpha and beta are its two classic forms (next section).</li>
<li>Read the pyramid bottom-up: cheap and narrow below, realistic and costly above; faults found late cost orders of magnitude more to repair.</li></ul>
""", diagram="se4_levels"),
    ],
}

SEC_4_3 = {
    "title": {"en": "4.3 Black-Box Testing"},
    "items": [
        T("Black-Box Techniques (Specification-Based)", """
<ul><li>Test from the <b>specification only</b> - the code is an opaque box. We feed inputs, observe outputs, and compare against what the SRS promises.</li>
<li><b>Equivalence class partitioning</b>: divide the input domain into classes assumed to behave alike; one representative per class stands for a thousand inputs. Example age validation 5-60: classes = {below 5}, {5..60}, {above 60} - test 3, 25, 70.</li>
<li><b>Boundary Value Analysis (BVA)</b>: bugs breed at edges, so test <b>on and just beside</b> every boundary: for 5-60 test 4, 5, 6 and 59, 60, 61. BVA extends (not replaces) equivalence classes.</li>
<li><b>Cause-effect graphing</b>: map logical combinations of input causes to output effects (a decision table) - generates tests for complex ruled logic like booking eligibility.</li>
<li><b>Error guessing</b>: experience-led attacks - empty fields, duplicate booking, past dates, overflow inputs. No method, often gold.</li>
<li>Detection and repair strategy: isolate the failing class, reproduce with the smallest input, then widen coverage around the fix.</li></ul>
""", diagram="se4_blackbox"),
    ],
}

SEC_4_4 = {
    "title": {"en": "4.4 White-Box Testing"},
    "items": [
        T("White-Box Test Case Design (Structure-Based)", """
<ul><li>The box is transparent: testers see the code and design inputs that <b>exercise its structures</b> - statements, branches, loops.</li>
<li><b>Statement coverage</b>: every statement executes at least once. Weakest useful criterion - a never-taken branch can hide a crash.</li>
<li><b>Branch (decision) coverage</b>: every if takes both the TRUE and FALSE side at least once. For <code>if (x &gt; 0)</code>, tests x=3 and x=-7 give 100% branch coverage.</li>
<li><b>Condition coverage</b> refines further for compound decisions (a &amp;&amp; b): each atomic condition true and false.</li>
<li><b>Path coverage</b>: every route from entry to exit executes; bounded with <b>basis path testing</b> - count independent paths via cyclomatic complexity V(G) = edges - nodes + 2P, then design one test per basis path. Loops are exercised zero, once, and many times.</li>
<li>Relation to black-box: <b>complements, never replaces</b>. Black-box finds missing functionality; white-box finds hidden faulty code. Real test plans mix both.</li></ul>
""", diagram="se4_whitebox"),
    ],
}

SEC_4_5 = {
    "title": {"en": "4.5 Alpha, Beta and Designing Test Cases"},
    "items": [
        T("Alpha and Beta Testing", """
<ul><li>Both are <b>acceptance testing</b>: real usage decides whether the product is releasable.</li>
<li><b>Alpha</b>: performed <b>in-house</b> at the developer's site, by internal staff or friendly users, with developers watching. Controlled environment, late development/fix stage; goal is to catch crashes and glaring defects before outsiders see them.</li>
<li><b>Beta</b>: performed <b>in the wild</b> at selected client sites, by real users with real data on real hardware - developers are absent. Uncontrolled environment; goal is feedback on usability, configuration surprises and defects only the wild can produce.</li>
<li>Order: alpha first (lab), then beta (limited clients), then release candidate, then release.</li>
<li>Exam contrast: alpha = developer's site, controlled, internal users; beta = customer's site, uncontrolled, real users.</li></ul>
""", diagram="se4_ab"),
        T("Designing Test Cases (Practical 15)", """
<ul><li>A <b>test case</b> is a documented experiment: unique <b>id</b>, module, title, preconditions, numbered steps, <b>test data</b>, <b>expected result</b>, actual result, and pass/fail status.</li>
<li>The expected result is written <b>before</b> execution - from the SRS, not from what the program happens to do. A test without expectations is a demo, not a test.</li>
<li>Design habit: for every module write <b>positive</b> cases (does it do what it should) and <b>negative</b> cases (does it refuse what it must), then add boundary cases from BVA.</li>
<li>Example for a bus-booking seat module: TC-07 'no double-booking' - precondition seat 12A already booked; steps: login as user2, book 12A; expected: error message, seat allocation unchanged.</li>
<li>Test design techniques feed in from both worlds: black-box classes and boundaries derive cases from the spec; white-box coverage adds cases from the code structure. Record everything - a test suite is a project asset for every future regression.</li></ul>
""", diagram="se4_testcase"),
    ],
}

NOTES = [SEC_4_1, SEC_4_2, SEC_4_3, SEC_4_4, SEC_4_5]
