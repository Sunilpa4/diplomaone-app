"""DI04000011 Unit 1 notes: Software Process Models. English only."""
from java_content import make_TJ

SN = {}

T = make_TJ(SN)

SEC_1_1 = {
    "title": {"en": "1.1 Software and Application Domains"},
    "items": [
        T("Defining Software", """
<ul><li>Software is far more than code: <b>software = programs + documentation + configuration data + operating procedures</b> - everything needed to install, run and maintain the system.</li>
<li>Unlike hardware, software is <b>developed or engineered, not manufactured</b> - there is no physical wearing out; it instead degrades through careless changes ('maintenance scars').</li>
<li>Professionally, software counts as the instructions (programs) that make hardware useful, the <b>data</b> those instructions process, and the <b>documents</b> that describe both operation and use.</li>
<li>The exam trap: "software = set of programs" alone earns half the marks - always add documentation and data.</li></ul>
"""),
        T("Software Application Domains", """
<ul><li><b>System software</b>: serves other programs - operating systems, compilers, drivers, network stacks; close to the hardware and performance-critical.</li>
<li><b>Application software</b>: solves specific business/personal needs - accounting, word processors, attendance registers.</li>
<li><b>Embedded software</b>: firmware inside devices (ABS brakes, microwave, washing machine) - tiny, real-time and safety-sensitive.</li>
<li><b>Web applications</b>: browser-facing sites plus cloud backends - continuous deployment, zero install.</li>
<li><b>Artificial-Intelligence software</b>: systems that predict, recognise or recommend - built around data and models as much as code.</li>
<li>Domain choice shapes process choice: a firmware bug can crash an anti-lock brake, so embedded work insists on V-model rigour; a web shop can ship daily with agile cadence.</li></ul>
""", diagram="se1_domains"),
        T("Green Hydrogen Ecosystem Software", """
<ul><li>Green hydrogen is produced by <b>electrolysis powered with renewable electricity</b> - its ecosystem of plants, pipelines, storage and fuel stations cannot run without software.</li>
<li><b>Role in production:</b> software supervises electrolysers (temperature, pressure, current density), schedules runs against the solar/wind generation forecast, and logs the energy mix for 'green' certification.</li>
<li><b>Role in distribution:</b> it optimises logistics of compressed/liquefied hydrogen - tracking tankers and pipelines, monitoring leak sensors, managing storage pressure and station inventory.</li>
<li>Matching supply to demand (hydrogen made only when the sun shines, delivered when buses roll) is a scheduling-and-control problem - squarely a software-engineering one, and a natural fit for AI-assisted forecasting.</li>
<li>Syllabus point to remember: hydrogen software blends <b>embedded</b> (plant controllers), <b>system</b>-level SCADA and <b>web/AI</b> dashboards - one project wielding several domains.</li></ul>
"""),
    ],
}

SEC_1_2 = {
    "title": {"en": "1.2 Software Engineering: Layers and the Generic Process"},
    "items": [
        T("Software Engineering - A Layered Approach", """
<ul><li>Definition (IEEE style): <b>software engineering</b> is the application of a systematic, disciplined, quantifiable approach to the development, operation and maintenance of software.</li>
<li>SE is built on four layers, like a pyramid resting on its tip's support: <b>quality focus</b> (foundation), <b>process</b>, <b>methods</b>, <b>tools</b> (top).</li>
<li>The <b>process</b> layer defines the framework - activities, milestones, when work products are checked.</li>
<li><b>Methods</b> supply the how-to of each technical task: requirement analysis techniques, design notations, coding and testing practices.</li>
<li><b>Tools</b> automate and enforce the methods (IDEs, version control, CI pipelines, case tools).</li></ul>
""", diagram="se1_layers"),
        T("Generic Process Model: Framework Activities", """
<ul><li>Whatever model a team selects, five <b>framework activities</b> always appear: <b>communication &rarr; planning &rarr; modeling &rarr; construction &rarr; deployment</b>.</li>
<li><b>Communication</b>: gather what customers actually need (requirements).</li>
<li><b>Planning</b>: turn needs into scope, estimates, schedule and risk plans.</li>
<li><b>Modeling</b>: analysis and design - model logic, data, interfaces before writing code.</li>
<li><b>Construction</b>: code generation and testing.</li>
<li><b>Deployment</b>: delivery, training and ongoing support. Then the cycle repeats via feedback.</li>
<li>Each process model (waterfall, spiral, Scrum...) is simply a different <b>serialisation</b> of these same five.</li></ul>
""", diagram="se1_framework"),
        T("Umbrella Activities", """
<ul><li>Umbrella activities run <b>parallel to and across</b> all framework steps - they 'hold the umbrella' over the project:</li>
<li><b>Project tracking and control</b> - is the schedule honest?</li>
<li><b>Risk management</b> - what could hurt us, and what is plan B?</li>
<li><b>Software quality assurance (SQA)</b> - are work products and processes up to standard?</li>
<li><b>Measurement/metrics</b> - numbers about progress and quality for decisions.</li>
<li><b>Configuration &amp; change management</b> - one controlled copy of every artifact, every change reviewed.</li>
<li>Exam phrasing: framework activities advance the SOFTWARE; umbrella activities protect the PROJECT.</li></ul>
"""),
        T("Problem Statement and Bounded Scope", """
<ul><li><b>Practical 2:</b> define your project with a tight problem statement before touching models.</li>
<li>Shape: <b>problem</b> (what hurts), <b>actors</b> (who feels it), <b>goal</b> (what the system will do), <b>scope boundary</b> (what it explicitly will NOT do).</li>
<li>Example: 'Bus Reservation Mini' - let a student book a seat against posted schedules; NOT payments, NOT GPS tracking, NOT driver payroll.</li>
<li>A bounded scope lets you pick a sensible process model (Practical 3): tiny, well-understood scope &rarr; waterfall or a single increment; fuzzy scope &rarr; prototype; high risk + big budget &rarr; spiral; customer available weekly &rarr; agile.</li></ul>
"""),
    ],
}

SEC_1_3 = {
    "title": {"en": "1.3 Traditional Process Models"},
    "items": [
        T("Waterfall Model", """
<ul><li>The grandfather model (1970): phases flow strictly downward - <b>requirements &rarr; design &rarr; implementation &rarr; testing &rarr; deployment &rarr; maintenance</b> - each starting only after the previous gate-signs-off.</li>
<li><b>Strengths</b>: disciplined documents per phase, obvious milestones, suited to fixed, well-understood scope.</li>
<li><b>Weaknesses</b>: working software appears late; real requirements rarely freeze; a design mistake discovered in testing forces a painful climb back upstream.</li>
<li><b>Practical 1 board answer</b>: waterfall drawing with its staircase - learn phase names in order plus one strength and one weakness each.</li>
<li>Pick it for: a college attendance upgrade where every rule is already on paper.</li></ul>
""", diagram="se1_waterfall"),
        T("Incremental Model", """
<ul><li>Deliver the product in <b>increments</b>: the core product ships first; each later slice runs its own mini requirements-design-code-test and adds features.</li>
<li>Customers touch working software EARLY (like agile in spirit) and priorities shift between releases.</li>
<li>Risk spreads over slices - a slip on increment 3 does not endanger the v1 already live.</li>
<li>Fits staffing limits too: a small crew can finish slices one at a time.</li>
<li>Contrast with waterfall: same phases, but repeated per slice and delivering partial products each time.</li></ul>
""", diagram="se1_incremental"),
        T("Prototyping Model", """
<ul><li>For customers who "know it when they see it": build a <b>quick, cheap mock</b> of key screens/behaviour, let the customer react, refine, repeat - then build the final system.</li>
<li>Loop: gather rough requirements &rarr; quick design &rarr; build/throwaway prototype &rarr; customer evaluation &rarr; refine requirements &rarr; (repeat until clear) &rarr; full build.</li>
<li>Flushes out hidden requirements early, when changing them is cheap.</li>
<li>Two dangers: the customer mistakes the fragile demo for the nearly-finished product, or the rush to re-use the throwaway code drags quick-and-dirty quality into production.</li></ul>
""", diagram="se1_prototype"),
        T("Spiral Model", """
<ul><li>Boehm's model (1988): the project sweeps outward in cycles, each loop split into four quadrants - <b>planning, risk analysis, engineering, evaluation</b>.</li>
<li>It is the first model to put <b>risk front and centre</b>: every round asks "what could sink us, prove it explicitly".</li>
<li>Early loops may produce only a paper spec or prototype; later loops produce increasingly complete versions.</li>
<li>Strength: ideal for large, expensive, risk-heavy projects. Weakness: heavier overhead - risk analysis needs expertise and each loop costs money; overkill for small classroom projects.</li></ul>
""", diagram="se1_spiral"),
        T("V-Model (Verification & Validation)", """
<ul><li>A waterfall bent into a V: every development stage on the left arm pairs with a testing stage on the right arm - requirements &harr; acceptance test, system design &harr; system test, architecture (module design) &harr; integration test; the bottom is coding.</li>
<li>Test <b>plans</b> are written during the opposing build stage - acceptance test cases come straight out of the requirements document, long before any code exists.</li>
<li>Verification = "are we building the product right?" (reviews, walkthroughs); Validation = "are we building the right product?" (tests against user needs).</li>
<li>Favoured in safety- and audit-heavy domains (medical, aerospace) where each stage must be proven; inherits waterfall's rigidity for changing requirements.</li></ul>
""", diagram="se1_vmodel"),
    ],
}

SEC_1_4 = {
    "title": {"en": "1.4 The Agile Approach"},
    "items": [
        T("Agile: Values and Principles", """
<ul><li>Agile (2001) answered heavyweight plans with four values: <b>working software over comprehensive documentation; responding to change over following a plan; individuals and interactions over processes and tools; customer collaboration over contract negotiation</b>.</li>
<li>The right-hand items still matter - the left are simply valued MORE.</li>
<li>Of the twelve principles, the heart three: satisfy the customer through early, <b>continuous delivery</b>; <b>welcome change</b>, even late; deliver working software every few <b>weeks</b>.</li>
<li>Others to quote: working software is the primary measure of progress; close daily business-developer contact; self-organising teams; regular reflection and tuning.</li>
<li><b>Practical 3 link:</b> agile is the right model when requirements will evolve and the customer can review a build every sprint.</li></ul>
""", diagram="se1_agile"),
        T("Scrum Framework", """
<ul><li>Scrum organises agile work into <b>sprints</b> - fixed 2-4 week timeboxes, each ending with a ship-able product increment.</li>
<li>Artifacts: <b>product backlog</b> (every feature, prioritised by the Product Owner) &rarr; <b>sprint backlog</b> (committed slice for this sprint) &rarr; <b>increment</b> (potentially deployable outcome).</li>
<li>Ceremonies: sprint planning, the <b>daily 15-minute stand-up</b> (what done, what next, what blocks), sprint review (demo), retrospective (process tune-up).</li>
<li>Roles: <b>Product Owner</b> decides WHAT; <b>Developers</b> decide HOW; the <b>Scrum Master</b> clears obstacles and guards the process.</li>
<li>The iron rule of timeboxing: scope may slip, the deadline does not.</li></ul>
""", diagram="se1_scrum"),
        T("Extreme Programming (XP)", """
<ul><li>XP pushes each good engineering practice to its extreme: if reviews help, review continuously - that is <b>pair programming</b> (two at one keyboard, one driving, one navigating).</li>
<li><b>Test-driven development (TDD)</b>: write the failing test first, then just enough code to pass.</li>
<li><b>Continuous integration</b>: merge and run the whole test suite several times a day.</li>
<li><b>Refactoring</b>: improve design continuously in tiny safe steps; <b>small releases</b>: ship thin slices frequently.</li>
<li><b>Simple design</b>: solve today's need only; plus supporting habits - collective ownership, coding standards, 40-hour sustainable pace, on-site customer.</li>
<li>XP supplies the engineering <i>discipline</i>; Scrum the project <i>rhythm</i> - real agile teams usually blend both.</li></ul>
""", diagram="se1_xp"),
    ],
}

NOTES = [SEC_1_1, SEC_1_2, SEC_1_3, SEC_1_4]
