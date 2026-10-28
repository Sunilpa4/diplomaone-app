"""DI04000011 Unit 1 extras: key-term cards, viva, exam questions."""
from java_content import SXE, VE, XE, G

SYNTAX = [
    G("Process Model Cheat Cards", [
        SXE("waterfall in one line", """phases flow strictly downward:
req -> design -> impl -> test -> maintain
frozen scope only; late working software
fixing upstream = painful""",
            "the 1970 doc-first, one-way staircase"),
        SXE("incremental in one line", """core product ships first (mini-
waterfall per slice);
later increments add features on top""",
            "early feedback without agile ceremonies"),
        SXE("prototype in one line", """rough req -> quick design -> demo
-> customer reacts -> refine -> repeat
then real build""",
            "learn requirements by SHOWING"),
        SXE("spiral in one line", """repeat quadrants: plan -->
analyse RISK --> engineer --> customer
evaluates --> wider loop""",
            "risk-driven cycles for big projects"),
        SXE("V-model in one line", """left arm builds (req -> design ->
code), right arm tests back upward -
each stage plans its own test early""",
            "build-test pairs; audit-friendly"),
    ]),
    G("Agile Cheat Cards", [
        SXE("agile in one line", """values: working software > docs;
change response > plans; people >
processes; collaboration > contract""",
            "the 2001 manifesto - deliver often"),
        SXE("scrum in one line", """product backlog -> sprint backlog ->
2-4 week sprint -> ship-able increment
(+ daily stand-up, review, retro)""",
            "timeboxed agile by Scrum Master"),
        SXE("XP in one line", """pair programming, TDD, continuous
integration, refactoring, small
releases, simple design""",
            "engineering discipline to the max"),
    ]),
]

_VIVA = [
    VE("Define software.", "Programs + configuration data + documentation + operating procedures - not just code."),
    VE("How is software different from hardware?", "It is engineered/developed, not manufactured; it does not wear out physically, though constant careless changes corrupt it."),
    VE("Name five application domains of software.", "System, application, embedded, web application, and AI-based software (green-hydrogen control software is a sixth in your syllabus)."),
    VE("Give an embedded software example.", "The ABS firmware in a car - tiny, real-time and safety-critical."),
    VE("What role does software play in green hydrogen production?", "It supervises electrolysers, schedules production against renewable generation forecasts and logs the energy mix for 'green' certification."),
    VE("And in hydrogen distribution?", "Tracking tankers/pipelines, watching leak sensors, managing storage pressure and station inventory - matching supply with demand."),
    VE("Define software engineering.", "The systematic, disciplined, quantifiable approach to developing, operating and maintaining software."),
    VE("Name the four SE layers in order.", "Quality focus (bedrock), process, methods, tools."),
    VE("Which layer is the foundation and why?", "Quality focus - every other layer exists to protect the quality of the final product."),
    VE("List the five generic framework activities.", "Communication, planning, modeling, construction, deployment."),
    VE("What umbrella activities span a project?", "Tracking and control, risk management, SQA, metrics, and configuration/change management."),
    VE("Framework vs umbrella activities?", "Framework steps advance the software forward; umbrella activities protect the whole project while it advances."),
    VE("What is a process model?", "A chosen arrangement/serialisation of the framework activities - how work, reviews and releases flow."),
    VE("Name five traditional process models.", "Waterfall, incremental, prototype, spiral and the V-model."),
    VE("Describe the waterfall model in one line.", "Phases proceed linearly downward - requirements to design to code to testing to maintenance - with no return path assumed."),
    VE("When does waterfall work best?", "When requirements are stable, complete and well understood from day one."),
    VE("Waterfall's biggest weakness?", "Working software arrives very late; fixing upstream errors mid-way is costly and awkward."),
    VE("What is the incremental model?", "The product is built in slices: the core ships first, and each increment runs its own mini requirement-design-code-test to add features."),
    VE("Why do customers like incremental delivery?", "They use real software early and can re-prioritise later increments based on hands-on feedback."),
    VE("When do you choose the prototyping model?", "When requirements are vague - the customer will 'know it when they see it'; the disposable mock exposes true needs cheaply."),
    VE("What are the risks of prototyping?", "The customer may take the demo for the finished product, or throwaway quality may leak into the final build."),
    VE("Explain the four quadrants of the spiral model.", "Planning, risk analysis, engineering, customer evaluation - repeated outward until delivery."),
    VE("Who should use the spiral model?", "Large, expensive, risk-heavy projects; risk expertise is a prerequisite, so it is overkill for small projects."),
    VE("Explain the V-model pairing.", "Each build stage on the left (requirements, system design, module design, coding) pairs with a test stage on the right (acceptance, system, integration)."),
    VE("Verification vs validation?", "Verification - building the product RIGHT (reviews against spec); validation - building the RIGHT product (tests against user needs)."),
    VE("Which model writes acceptance tests from requirements, early?", "The V-model - test planning starts opposite the corresponding build phase."),
    VE("State the four Agile Manifesto values.", "Working software over comprehensive documentation; responding to change over following a plan; individuals and interactions over processes and tools; customer collaboration over contract negotiation."),
    VE("Name three core agile principles.", "Early and continuous delivery of working software; welcome changing requirements; deliver working software every few weeks."),
    VE("What is the primary measure of progress in agile?", "Working software."),
    VE("What is a sprint?", "A fixed 2-4 week timebox in Scrum that ends with a potentially ship-able product increment."),
    VE("Name Scrum's three roles.", "Product Owner (decides WHAT), Developers (decide HOW), Scrum Master (removes blockers, guards the process)."),
    VE("What happens in a daily stand-up?", "Each member answers: what I did, what I will do, what blocks me - in under 15 minutes, standing."),
    VE("Product backlog vs sprint backlog?", "Product backlog: every desired feature, prioritised; sprint backlog: the committed slice for the current sprint."),
    VE("What if a sprint's scope proves too big?", "Scope drops out of the sprint; the deadline never moves - that is timeboxing."),
    VE("Name four XP practices.", "Pair programming, test-driven development, continuous integration, refactoring (also small releases and simple design)."),
    VE("What is pair programming?", "Two programmers at one keyboard - one drives (types), one navigates (reviews, plans), swapping frequently."),
    VE("What is test-driven development?", "Write the failing test first, then write just enough code to pass it; the suite grows with every feature."),
    VE("Why does XP insist on small releases?", "Thin, frequent releases keep the customer steering the product and keep regression risk tiny."),
    VE("Scrum vs XP - one line each.", "Scrum supplies project RHYTHM (sprints, roles, ceremonies); XP supplies engineering DISCIPLINE (TDD, pairing, refactoring)."),
    VE("Say a college bus-booking app must evolve weekly with user feedback - which model?", "An agile model - Scrum with short sprints; scope is fluid and stakeholders are available."),
    VE("A missile-control firmware with frozen specs?", "Waterfall or V-model: everything specified upfront, verification-heavy, audits at each phase."),
    VE("Requirements unclear and budget limited?", "Prototyping - a cheap visible mock flushes out true requirements before real investment."),
    VE("(Practical 2) What makes a good problem statement?", "Problem, actors, goal and an explicit boundary of what the system will NOT do - the bounded scope."),
    VE("(Practical 3) Task set for the incremental model?", "Core slice first: minimal req-design-code-test, then repeat per slice; each slice is a deployable increment."),
]

assert len(_VIVA) == 44
VIVA = [
    G("Software and SE Foundations", _VIVA[0:11]),
    G("Traditional Models", _VIVA[11:26]),
    G("Agile, Scrum and XP", _VIVA[26:44]),
]

EXAM_QS = [
    XE("Define software and explain its components. List the application domains of software.", 6),
    XE("Explain the role of software in green hydrogen production and distribution.", 4),
    XE("Explain the layered approach of software engineering with a diagram.", 4),
    XE("What is the generic process model? Explain the five framework activities.", 6),
    XE("Explain umbrella activities and why they run alongside the framework activities.", 4),
    XE("Explain the waterfall model with a diagram. State two strengths and two weaknesses.", 6),
    XE("Explain the incremental process model and how it differs from waterfall.", 4),
    XE("Explain the prototyping model with its refinement cycle.", 4),
    XE("Explain the spiral model with its four quadrants. Which projects suit it?", 6),
    XE("Draw the V-model and explain how testing pairs with each development stage.", 6),
    XE("List the four values of the Agile Manifesto and explain any two.", 4),
    XE("Explain three principles of agile development and their effect on delivery pace.", 3),
    XE("Explain the Scrum framework: roles, artifacts and ceremonies.", 6),
    XE("Explain any four Extreme Programming (XP) practices.", 4),
    XE("For the project in Practical 2/3, justify your choice of process model over two alternatives.", 4),
]
