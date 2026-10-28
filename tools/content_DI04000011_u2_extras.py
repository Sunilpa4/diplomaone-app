"""DI04000011 Unit 2 extras: key-term cards, viva, exam questions."""
from java_content import SXE, VE, XE, G

SYNTAX = [
    G("Requirements & SRS", [
        SXE("requirement types", """functional  = what system DOES
  (book seat, print receipt)
non-functional = constraints
  (2s reply, encrypted pwd)""",
            "verbs vs qualities"),
        SXE("gathering toolkit", """interviews | questionnaires |
workshops | observation |
document study | prototyping""",
            "blend several, never just one"),
        SXE("good SRS checklist", """correct, unambiguous, complete,
consistent, ranked, verifiable,
modifiable, traceable""",
            "the eight golden adjectives"),
    ]),
    G("Design Quality", [
        SXE("cohesion ladder (best last)", """coincidental < logical <
temporal < procedural <
communicational < sequential <
FUNCTIONAL  (one clear job)""",
            "inside modules: aim high"),
        SXE("coupling ladder (worst first)", """content > common > external >
control > stamp > data >
MESSAGE  (loosest)""",
            "between modules: aim low"),
    ]),
    G("Diagram Symbols", [
        SXE("DFD symbols", """circle      = process
rect        = external entity
|| double   = data store
-> labeled  = data flow""",
            "data moves THROUGH processes"),
        SXE("class diagram marks", """box       = class (name/attr/op)
line      = association + 1..* count
diamond   = aggregation (> weak)
triangle  = generalisation (IS-A)""",
            "static structure"),
        SXE("sequence diagram marks", """stick/box up top + dashed lifeline
solid ->  = call   dashed -> = reply
time flows DOWNWARD""",
            "one scenario, in order"),
        SXE("activity diagram marks", """dot = start   ring-dot = end
rounded box = action
diamond = decision
bold bars = fork/join (parallel)""",
            "flowchart, upgraded"),
    ]),
]

_VIVA = [
    VE("What are functional requirements?", "Statements of what the system DOES - services like booking a seat, issuing a receipt, searching records."),
    VE("What are non-functional requirements?", "Quality and constraint statements - performance, security, capacity, usability, portability - telling how well functions must work."),
    VE("Give one functional and one non-functional requirement for a library system.", "Functional: 'the system records each book issue'; Non-functional: 'search results appear within 2 seconds for 200 users.'"),
    VE("Name four requirement gathering techniques.", "Interviews, questionnaires, brainstorming workshops and observation (plus document study and prototyping)."),
    VE("When is observation better than interviews?", "When users do work they cannot fully describe - watching reveals steps never mentioned in a talk."),
    VE("What is requirement analysis?", "Classifying, negotiating and validating gathered requirements into a consistent, agreed set before designing."),
    VE("What is an SRS?", "Software Requirement Specification - the formal document stating exactly what the software must do, agreed between customer and developer."),
    VE("List any four characteristics of a good SRS.", "Correct, unambiguous, complete, consistent (also: ranked, verifiable, modifiable, traceable)."),
    VE("Why must an SRS be unambiguous?", "Every sentence needs exactly ONE meaning - ambiguity lets two developers build two different systems from the same line."),
    VE("Customer requirements vs functional requirements?", "Customer requirements are the client's plain-language needs; functional requirements are their testable restatement as system actions."),
    VE("What makes a requirement 'verifiable'?", "Some finite, cost-effective test exists to prove the system meets it ('responds within 2 s' - yes; 'fast' - no)."),
    VE("Analysis vs design, one line?", "Analysis defines WHAT the system must do for users; design defines HOW the build will do it for the developers."),
    VE("What makes a design 'good'?", "Correct, complete, efficient, understandable and - above all - changeable."),
    VE("Define cohesion.", "The measure of how strongly the elements INSIDE one module belong together - the higher, the better."),
    VE("Best and worst cohesion types?", "Best: functional (one clear job). Worst: coincidental (a random grab-bag)."),
    VE("Define coupling.", "The measure of interdependence BETWEEN modules - the lower, the better."),
    VE("Worst and best coupling types?", "Worst: content coupling (one rewrites another's innards). Best: message/data coupling (only needed parameters/messages cross)."),
    VE("State the design golden rule.", "High cohesion, low coupling - modules each do one clear job and lean on each other as little as possible."),
    VE("What is a DFD?", "Data Flow Diagram - shows how data moves through processes, stores and external entities, without fixing code details."),
    VE("Name the four DFD symbols.", "Process (circle), external entity (rectangle), data store (two parallel lines), data flow (labeled arrow)."),
    VE("What is a context-level DFD?", "The whole system drawn as ONE bubble with only external entities and the flows between them."),
    VE("What changes from context to level-1 DFD?", "The single bubble is exploded into 4-8 major functions; external flows must stay balanced across the change."),
    VE("What is balancing in a DFD?", "The in/out flows of a bubble on one level must exactly match the in/out flows of its expanded lower level."),
    VE("Can a data store talk directly to an entity?", "No - all data movement passes through a process bubble; that's a DFD rule commonly probed."),
    VE("What does a use case diagram show?", "Actors (roles) and the user goals (use cases) they can perform within the system boundary."),
    VE("include vs extend in use cases?", "<<include>> = always-reused shared part; <<extend>> = optional behaviour added only in some cases."),
    VE("What are the three compartments of a class box?", "Class name, attributes, operations."),
    VE("What does multiplicity mean in a class diagram?", "The count constraint at each end of an association - e.g. Member 1...* borrows Book 0...*."),
    VE("Association vs generalisation?", "Association links peer classes (borrows); generalisation is IS-A inheritance (EBook -> Book, hollow triangle)."),
    VE("What does a component diagram emphasise?", "Physical, replaceable units (components) and the provided/required interfaces they snap together through."),
    VE("Lollipop vs socket symbols?", "Lollipop = PROVIDED interface (offered service); socket = REQUIRED interface (needed service)."),
    VE("What does a sequence diagram show?", "Interaction over time: objects across the top, lifelines downward, ordered messages (calls solid, returns dashed)."),
    VE("When do you pick a sequence diagram?", "To walk one scenario step by step in time order - e.g. exactly what happens when the student taps 'order'."),
    VE("Sequence vs activity diagram?", "Sequence emphasises WHO sends WHICH message WHEN; activity emphasises flow of actions including decisions and parallel branches."),
    VE("What are the start and end symbols in an activity diagram?", "A filled circle; a bull's-eye (ring with filled dot)."),
    VE("What are swimlanes for?", "They group actions by the actor/system-role that performs them, making hand-offs visible."),
    VE("Subject verbs for UML: which diagram for 'workflow with decisions'?", "Activity diagram."),
    VE("Practical 6: give a sensible level-1 bubble list for a food app.", "browse menu, place order, pay, notify kitchen."),
    VE("Which SIX artifacts does Practical 4-11 ask you to produce?", "Gathered requirements, a broad SRS, DFD + E-R diagrams, use-case diagram, class/component/sequence/activity diagrams."),
    VE("What draws biggest exam marks from this unit?", "DFD levels, cohesion/coupling ladders and each UML diagram symbol set - draw them."),
    VE("Why does a class diagram matter before coding?", "It freezes the nouns, their data and relations, so implementation follows one agreed static structure."),
]

assert len(_VIVA) == 41
VIVA = [
    G("Requirements and SRS", _VIVA[0:11]),
    G("Design: Cohesion and Coupling", _VIVA[11:18]),
    G("DFDs (Practical 6)", _VIVA[18:24]),
    G("UML Diagrams (Practicals 7-11)", _VIVA[24:41]),
]

EXAM_QS = [
    XE("Distinguish functional and non-functional requirements with three examples each.", 4),
    XE("Explain any four requirement-gathering techniques and their best-fit situations.", 4),
    XE("What is an SRS? Describe its standard structure with section meanings.", 6),
    XE("State and explain six characteristics of a good SRS. (Practical 5)", 6),
    XE("Differentiate analysis and design with a WHAT-vs-HOW table.", 3),
    XE("Explain the characteristics of a good software design.", 3),
    XE("Explain six classes of cohesion from worst to best with mini examples.", 6),
    XE("Explain the types of coupling from worst to best with mini examples.", 6),
    XE("Why do we pursue 'high cohesion and low coupling'? Justify with maintenance impact.", 3),
    XE("Draw the four DFD symbols and state the flow rules among them.", 4),
    XE("Draw context-level and level-1 DFDs for an online food ordering system. (Practical 6a)", 6),
    XE("Explain balancing across DFD levels with an example.", 3),
    XE("Draw a use case diagram for a food ordering app showing two actors and <<include>>. (Practical 7)", 6),
    XE("Draw a class diagram with association, multiplicity and generalisation for a library system. (Practical 8)", 6),
    XE("Differentiate use case, sequence and activity diagrams by viewpoint.", 4),
    XE("Draw the sequence diagram for 'place order' including a payment gateway. (Practical 10)", 6),
    XE("Draw an activity diagram for an order flow with a payment decision branch. (Practical 11)", 4),
    XE("Explain a component diagram's symbols and their use in a backend design. (Practical 9)", 4),
]
