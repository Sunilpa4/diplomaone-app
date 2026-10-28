"""DI04000011 Unit 4 extras: key-term cards, viva, exam questions."""

from java_content import SXE, VE, XE, G

SYNTAX = [
    G("Coding cards", [
        SXE("standards vs guidelines", """STANDARDS = mandatory rules
naming indentation comments
no GOTOs, few globals
GUIDELINES = softer advice
code for the reader first""",
            "rules enforced, advice earned"),
        SXE("review pairing", """walkthrough : author led
  informal, share knowledge
inspection  : moderator led
  checklist, defect log,
  formal roles""",
            "chat vs audit"),
        SXE("docs split", """INTERNAL  inside the code
  headers comments doc-strings
EXTERNAL  beside the code
  manual guide SRS API ref""",
            "for developers vs users"),
    ]),
    G("Testing cards", [
        SXE("v and v", """VERIFICATION build it RIGHT
  reviews against the spec
VALIDATION  build the RIGHT
  testing against needs""",
            "process vs product"),
        SXE("levels ladder", """unit        one module
integration interfaces
system      whole vs SRS
acceptance  customer yes""",
            "alpha + beta live on top"),
        SXE("black-box box", """equivalence classes
boundary values 4 5 6 | 59 60 61
cause-effect graphs
error guessing""",
            "spec only, no code peeking"),
        SXE("white-box box", """statement every line once
branch    both if sides
condition each atom T/F
path      basis set, V(G)""",
            "structure LED, coverage %"),
        SXE("test case rows", """id module title
precondition steps data
EXPECTED  (before run)
actual status pass/fail""",
            "no expectation = demo"),
    ]),
]

_VIVA = [
    VE("What is the coding phase?", "Translating the detailed design into executable source code - while keeping it readable and maintainable for the humans who come after."),
    VE("What is a coding standard?", "A mandatory team rule for writing code: naming conventions, indentation, comment density, error-handling style, banned constructs like GOTO."),
    VE("How do guidelines differ from standards?", "Standards are enforced rules; guidelines are advisory wisdom - style you follow for readability but no tool will block you for breaking."),
    VE("Name four things coding standards typically police.", "Naming conventions, indentation/layout, comment density, limits on globals and GOTOs (plus function-size caps)."),
    VE("Why do teams invest in standards?", "Uniform style means anyone can maintain any module, reviews run faster, and whole bug classes are prevented at the keyboard."),
    VE("What is a code walkthrough?", "An informal, author-led review: the author narrates the code line by line and peers ask questions - mainly knowledge sharing."),
    VE("What is a code inspection?", "A formal review (Fagan): moderator, readers and recorder prepare with checklists, log every defect, and verify fixes afterwards."),
    VE("Walkthrough vs inspection in one line each.", "Walkthrough = informal chat led by the author; inspection = formal audit led by a moderator with checklists and a defect log."),
    VE("Why is review cheaper than testing for many defects?", "A fault caught in review costs about one unit to fix; the same fault in live use costs around a hundred - and reviews need no execution setup."),
    VE("What is internal documentation?", "Documentation inside the source: module headers, why-comments, meaningful names, doc-strings - serving the next developer."),
    VE("What is external documentation?", "Documents beside the code: user manual, installation guide, SRS, design docs, API reference - serving users, testers and reviewers."),
    VE("What is the objective of testing?", "To execute a program with the intent of FINDING errors - a successful test reveals a fault, it does not prove correctness."),
    VE("Error vs fault vs failure.", "Error = human mistake; fault = the defect written into the software; failure = the wrong behaviour actually observed at run time."),
    VE("Define verification and validation.", "Verification: building the product RIGHT (checked against specs, e.g. reviews). Validation: building the RIGHT product (checked against real needs, e.g. testing)."),
    VE("Why can testing never prove a program correct?", "It can only show the presence of bugs, never their absence - the input space is effectively infinite (Dijkstra)."),
    VE("Why should developers not test their own code alone?", "Authors carry blind spots and a defending mindset; independent testers hunt defects impartially."),
    VE("List the four levels of testing in order.", "Unit (module alone), integration (interfaces between modules), system (whole product vs SRS), acceptance (customer verdict: alpha/beta)."),
    VE("Which level is cheapest for fixing defects and why?", "Unit testing - the module is isolated, the author is present, and the change has no ripple effects yet."),
    VE("What does integration testing target?", "Interfaces between modules - parameter mismatch, protocol confusion, shared data assumptions."),
    VE("What is black-box testing?", "Designing tests from the specification alone - inputs in, outputs compared - with no knowledge of the internal code."),
    VE("Explain equivalence class partitioning.", "Partition inputs into classes expected to behave identically; one test per class stands for the whole class."),
    VE("Give the equivalence classes for age valid 5-60.", "Below 5 (invalid), 5-60 (valid), above 60 (invalid) - e.g. test 3, 25, 70."),
    VE("What is Boundary Value Analysis?", "Test values on and immediately beside every boundary - for 5-60: 4, 5, 6 and 59, 60, 61 - because errors cluster at edges."),
    VE("Why does BVA beat random testing at edges?", "Off-by-one and comparison-slip faults live exactly at boundaries; random inputs rarely land there."),
    VE("What is cause-effect graphing?", "Map logical combinations of input causes to output effects as a graph/decision table, then derive a test per rule combination."),
    VE("What is error guessing?", "Experience-based attack cases - empty input, duplicates, overflow, past dates - no formal method, often very effective."),
    VE("What is white-box testing?", "Designing tests with knowledge of the code's internal structure, aiming to execute statements, branches and paths."),
    VE("Define statement coverage.", "Every executable statement runs at least once - the weakest meaningful coverage criterion."),
    VE("Define branch coverage.", "Every decision takes both its true and false outcomes at least once."),
    VE("What tests give 100% branch coverage on if (x > 0)?", "One x above zero and one at-or-below zero, e.g. x=3 and x=-7."),
    VE("What is basis path testing?", "Derive V(G) = edges - nodes + 2P independent paths from the control-flow graph and write one test per basis path."),
    VE("Black-box vs white-box - one contrast each.", "Black-box: spec-driven, finds missing functionality, tester needs no code. White-box: structure-driven, finds faulty hidden code, needs source access."),
    VE("Can white-box replace black-box?", "Never - code can do everything it does correctly and STILL miss a required feature; only spec-based tests catch absence."),
    VE("What is alpha testing?", "Acceptance testing in-house at the developer's site by internal/friendly users, controlled environment, developers watching."),
    VE("What is beta testing?", "Acceptance testing at selected real client sites by real users with real data - uncontrolled environment, developers absent."),
    VE("Alpha vs beta ordering and goal.", "Alpha first in the lab to remove crashes; beta next in the wild for usability and environment surprises; then release candidate."),
    VE("What is a test case?", "A documented experiment: id, module, title, preconditions, steps, test data, expected result, actual result, pass/fail."),
    VE("Why must the expected result be written before execution?", "It must come from the SRS - otherwise testers just record whatever the buggy program does and call it correct."),
    VE("Positive vs negative test cases.", "Positive: system does what it should with valid input. Negative: system safely refuses invalid input or states."),
    VE("What is regression testing?", "Re-running the existing suite after any change to prove no old functionality broke - a test suite is a permanent asset."),
    VE("What goes into a good test case title?", "The exact behaviour under judgement, e.g. 'no double-booking of a seat' - searchable, specific, traceable to the SRS."),
    VE("How do you pick test data for a module?", "One representative per equivalence class, every boundary value, plus guilty-past cases from error guessing."),
]

VIVA = [
    G("Coding, Standards and Review", _VIVA[0:11]),
    G("Testing Fundamentals and Levels", _VIVA[11:18]),
    G("Black-Box and White-Box", _VIVA[18:33]),
    G("Alpha-Beta and Test Cases", _VIVA[33:42]),
]

assert len(_VIVA) == 42, len(_VIVA)

EXAM_QS = [
    XE("Explain the need for coding standards and list four rules a standard typically enforces.", 4),
    XE("Distinguish coding standards from coding guidelines with two examples of each.", 3),
    XE("Compare code walkthrough and code inspection in a four-point table.", 4,),
    XE("Explain the roles and checklist-based process of a formal code inspection.", 4),
    XE("Distinguish internal from external documentation with examples of each.", 4),
    XE("'Testing can show the presence of bugs, never their absence.' Discuss testing objectives and psychology.", 6),
    XE("Distinguish error, fault and failure; and verification from validation.", 4),
    XE("Explain the four levels of testing with one activity and owner for each.", 6),
    XE("Explain equivalence class partitioning and Boundary Value Analysis with the age(5-60) example.", 6),
    XE("Explain cause-effect graphing and error guessing as black-box techniques.", 4),
    XE("Explain statement, branch and path coverage. Show the tests achieving 100% branch coverage for if (x > 0).", 6),
    XE("What is basis path testing? Explain cyclomatic complexity V(G) = E - N + 2P.", 4),
    XE("Compare black-box and white-box testing; explain why both are needed in a real plan.", 4),
    XE("Compare alpha and beta testing (site, users, environment, goal, order).", 4),
    XE("Design a complete test case (all fields) for 'a seat cannot be booked twice' in a bus-booking app. (Practical 15)", 6),
]
