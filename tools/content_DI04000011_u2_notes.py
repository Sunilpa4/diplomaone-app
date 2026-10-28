"""DI04000011 Unit 2 notes: Software Requirement Analysis and Design. English only."""
from java_content import make_TJ

SN = {}

T = make_TJ(SN)

SEC_2_1 = {
    "title": {"en": "2.1 Requirement Gathering and Analysis"},
    "items": [
        T("Types of Requirements: Functional and Non-Functional", """
<ul><li><b>Functional requirements</b>: the verbs of the system - what it must DO. 'Student books a seat', 'system prints a receipt', 'admin cancels a route'. Every one can be tested.</li>
<li><b>Non-functional requirements</b> (quality attributes/constraints): how WELL and under WHAT limits - response under 2 seconds, 1000 concurrent users, encrypted passwords, Hindi+Gujarati UI, budget cap.</li>
<li>Common exam framing: functional = service statement; non-functional = quality/constraint statement (performance, security, reliability, usability, portability).</li>
<li>Both belong in the SRS; a system with perfect features but 30-second replies is still a failed project.</li></ul>
""", diagram="se2_req_types"),
        T("Techniques for Requirement Gathering", """
<ul><li><b>Interviews</b>: structured 1-to-1 talks with key users - deep but slow.</li>
<li><b>Questionnaires/surveys</b>: collect from MANY users fast and cheap; quality limited by question quality.</li>
<li><b>Brainstorming/workshops (JAD)</b>: stakeholders solve requirements together - conflicts settle in the room.</li>
<li><b>Observation</b>: watch users work; uncovers steps nobody REMEMBERS to mention.</li>
<li><b>Document analysis</b>: study existing forms, registers and reports for data definitions.</li>
<li><b>Prototyping</b>: a quick mock makes vague wishes concrete (Unit 1).</li>
<li>Practice (Practical 4): blend techniques - interview the registrar, questionnaire the students, watch the counter clerks.</li></ul>
""", diagram="se2_gather"),
    ],
}

SEC_2_2 = {
    "title": {"en": "2.2 Software Requirement Specification (SRS)"},
    "items": [
        T("SRS: What It Is and Its Structure", """
<ul><li>The <b>SRS</b> is the negotiated contract between customer and developers recording exactly what the software must do - prepared after requirement gathering (Practical 5 is a broad SRS for your project).</li>
<li>Typical IEEE-style structure: <b>1. Introduction</b> (purpose, scope, definitions), <b>2. Overall description</b> (product perspective, users, constraints, assumptions), <b>3. Specific requirements</b> (functional + non-functional + interfaces), appendices.</li>
<li>Distinguish voices: <b>customer requirements</b> are the client's plain-language wishes ('a fast bus booking'); <b>functional requirements</b> are testable system actions ('the system shall confirm a seat within 2 seconds').</li>
<li>The SRS is a legal-ish document: ambiguity is a defect.</li></ul>
""", diagram="se2_srs"),
        T("Characteristics of a Good SRS", """
<ul><li><b>Correct</b> - every requirement stated is one the client truly needs.</li>
<li><b>Unambiguous</b> - every sentence has exactly ONE interpretation (the flagship exam answer: two developers must not be able to build two systems).</li>
<li><b>Complete</b> - nothing significant left blank (including what happens on bad input).</li>
<li><b>Consistent</b> - requirements never contradict each other.</li>
<li><b>Ranked for importance/stability</b> - MUST vs nice-to-have flagged.</li>
<li><b>Verifiable</b> - each item testable ('fast' fails this test; 'under 2 s at 500 users' passes).</li>
<li><b>Modifiable, traceable</b> - changes are absorbed cleanly; each requirement can be traced from SRS to design to test case.</li></ul>
"""),
    ],
}

SEC_2_3 = {
    "title": {"en": "2.3 Software Design Fundamentals"},
    "items": [
        T("Good Design and Analysis vs Design", """
<ul><li><b>Analysis answers WHAT</b> (needs, use cases); <b>design answers HOW</b> (modules, classes, data structures, interfaces, algorithms). Analysis talks to the customer; design instructs the builders.</li>
<li>Characteristics of a GOOD design: <b>correct</b> (does the job per SRS), <b>complete</b>, <b>efficient</b>, <b>understandable</b>, and above all <b>changeable</b> - because requirements WILL change.</li>
<li>Changeability is achieved through modular design, where two measures rule every choice: cohesion and coupling.</li></ul>
""", diagram="se2_analysis_vs_design"),
        T("Cohesion: Strength INSIDE a Module", """
<ul><li><b>Cohesion</b> = how strongly the items inside one module belong together. HIGHER is better.</li>
<li>Worst&#8594;best ladder: <b>coincidental</b> (random grab-bag) &lt; <b>logical</b> (similar kind: 'all print utilities') &lt; <b>temporal</b> (done at the same time: 'init stuff') &lt; <b>procedural</b> (fixed sequence) &lt; <b>communicational</b> (work on the same data) &lt; <b>sequential</b> (one step's output feeds the next) &lt; <b>functional</b> (every line serves ONE clear task - the goal).</li>
<li>Memory anchor: C-L-T-P-C-S-F climbing to functional.</li>
<li>Rule in practice: if a module's name needs 'and' ("validates and saves and prints"), split it.</li></ul>
""", diagram="se2_cohesion"),
        T("Coupling: Dependence BETWEEN Modules", """
<ul><li><b>Coupling</b> = how much one module depends on another. LOWER is better.</li>
<li>Worst&#8594;best: <b>content</b> (one module rewrites another's insides) &gt; <b>common</b> (shared global data) &gt; <b>external</b> (shared file format/protocol) &gt; <b>control</b> (flags steering another's logic) &gt; <b>stamp</b> (whole records handed over when a field or two would do) &gt; <b>data</b> (just needed parameters) &gt; <b>message</b> (talk only through messages/events - loosest).</li>
<li>Why you care: high coupling makes edits ripple through the system - one change in a global structure rewrites five modules' logic.</li>
<li>The design mantra for the exam and for life: <b>high cohesion + low coupling</b>.</li></ul>
""", diagram="se2_coupling"),
    ],
}

SEC_2_4 = {
    "title": {"en": "2.4 Function-Oriented Design: Data Flow Diagrams"},
    "items": [
        T("DFD Symbols and Rules", """
<ul><li>A <b>DFD</b> shows how data MOVES through a system - the four symbols: process (circle, transforms data), external entity (rectangle: outside actor), data store (two parallel lines: file/DB at rest), data flow (labeled arrow).</li>
<li>Rules that exams check: data always flows THROUGH a process; entities never talk directly to each other or to stores; every flow is labeled; every process both consumes and produces data.</li>
<li>DFDs document the business workflow without deciding HOW it is coded - they are analysis artifacts handed to design.</li></ul>
""", diagram="se2_dfd_symbols"),
        T("Context Level and Level-1 DFD", """
<ul><li><b>Context level</b>: the ENTIRE system as a single bubble, with only external entities and the flows between them - 'the system at a glance'.</li>
<li><b>Level 1</b>: explode that bubble into its major functions (4-8 bubbles), keeping the same external flows - an act called <b>balancing</b> (in/out flows must match between levels).</li>
<li>Deeper levels keep exploding: bubble 2 becomes 2.1, 2.2, ... Stop when a bubble is one clear task.</li>
<li>Practical 6: build context + level-1 DFD for your chosen project (here: food ordering) and note the order store under the bubbles.</li></ul>
""", diagram="se2_dfd_levels"),
    ],
}

SEC_2_5 = {
    "title": {"en": "2.5 Object-Oriented Modeling with UML"},
    "items": [
        T("Use Case Diagram", """
<ul><li>A use-case diagram is the <b>who-wants-what</b> map: stick-figure <b>actors</b> (roles, not persons) linked to <b>use case</b> ovals inside a system-boundary rectangle.</li>
<li>Relations: default plain lines ('actor can do this'); <b>&lt;&lt;include&gt;&gt;</b> when one case always reuses another (place order &rarr; include pay); <b>&lt;&lt;extend&gt;&gt;</b> for optional add-ons (apply coupon).</li>
<li>Practical 7: derive actors first, then per-actor goals - each oval is a testable user goal, not a screen.</li></ul>
""", diagram="se2_usecase"),
        T("Class Diagram", """
<ul><li>The static backbone: <b>classes</b> as three-compartment boxes (name / attributes / operations), with <b>associations</b> (plain line, e.g. Member borrows Book), <b>multiplicity</b> (1, 0..*, 1..*), and <b>generalisation</b> (hollow triangle toward the parent: EBook &#8594; Book IS-A).</li>
<li>Also know: aggregation (hollow diamond - weak whole-part), composition (filled diamond - strong), dependency (dashed arrow).</li>
<li>Build order (Practical 8): nouns of the SRS &rarr; classes; their properties &rarr; attributes; verbs &rarr; operations; relationships + multiplicity last.</li></ul>
""", diagram="se2_class"),
        T("Component Diagram", """
<ul><li>Shows the physical packaging: <b>components</b> (replaceable boxes such as OrderService, PaymentGateway) with <b>interfaces</b> drawn as lollipop (provided) and socket (required).</li>
<li>Components connect only through interfaces - so a payment-gateway swap touches nothing else.</li>
<li>Practical 9: carve your app into 3-5 components and mark what each OFFERS and what it NEEDS.</li></ul>
""", diagram="se2_component"),
        T("Sequence Diagram", """
<ul><li>An <b>interaction over time</b>: objects/actors across the top with vertical dashed <b>lifelines</b> running downward; horizontal solid arrows are calls, dashed arrows returns; thin bars on lifelines show activation.</li>
<li>Time flows DOWN the page, so the diagram doubles as the call script for one scenario (e.g. place an order with a payment gateway).</li>
<li>Practical 10: pick ONE use case and lay out its message order - if the diagram reads cleanly, the workflow is understood.</li></ul>
""", diagram="se2_sequence"),
        T("Activity Diagram", """
<ul><li>Flowchart's object-aware cousin: filled dot = start, ringed dot = end, rounded boxes = actions, <b>diamonds = decisions</b>, bold fork/join bars = parallel work (e.g. notify kitchen WHILE the receipt prints).</li>
<li>Swimlanes can assign actions to roles (customer lane vs kitchen lane) - great for showing hand-offs.</li>
<li>Practical 11: draw the complete flow of one user story, marking where the flow splits on 'pay online?' and where it merges back.</li></ul>
""", diagram="se2_activity"),
    ],
}

NOTES = [SEC_2_1, SEC_2_2, SEC_2_3, SEC_2_4, SEC_2_5]
