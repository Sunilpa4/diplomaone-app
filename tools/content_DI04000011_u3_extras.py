"""DI04000011 Unit 3 extras: key-term cards, viva, exam questions."""
from java_content import SXE, VE, XE, G

SYNTAX = [
    G("Estimation cards", [
        SXE("size metrics", """LOC = count code lines
      (late, language-bound)
FP  = count functionality
      (early, from the SRS)""",
            "bricks vs rooms"),
        SXE("FP formula", """FP = UFP x (0.65 + 0.01 x Sum(Fi))
UFP = sum(count x weight)
over inputs outputs inquiries
internal-files external-files""",
            "5 component types, 14 factors"),
        SXE("COCOMO equations", """E = a x (KLOC)^b    person-months
D = c x E^d         months
N = E / D           people
a b c d per class: organic /
semi-detached / embedded""",
            "KLOC in, effort/time/team out"),
    ]),
    G("Scheduling & Risk cards", [
        SXE("Gantt read", """bars over calendar weeks
overlap = parallel tasks
bar-end -> next start = depends
% filled = progress now""",
            "the whole plan at a glance"),
        SXE("burndown read", """plot remaining effort daily
dashed line = ideal finish
actual above = BEHIND
actual below = AHEAD""",
            "are we on time today?"),
        SXE("risk cycle", """identify -> assess (P x I)
-> mitigate / plan B -> monitor
weekly -> (repeat)""",
            "never a one-time act"),
        SXE("risk register row", """risk | prob | impact | R=P*I |
owner | mitigation | trigger""",
            "one line per watched risk"),
    ]),
]

_VIVA = [
    VE("List four responsibilities of a software project manager.", "Estimation and planning, task/team assignment and tracking, risk and change management, stakeholder communication and quality guarding."),
    VE("Why does a PM own risk management?", "Risk scanning needs authority over schedule and budget - only the PM can act on the register."),
    VE("What is project estimation?", "Predicting size, effort, cost and duration before (and while) building - the basis of every plan."),
    VE("Define LOC as a size metric.", "Estimated or counted lines of code of the finished product (KLOC in thousands) - the oldest, simplest size unit."),
    VE("Two weaknesses of LOC.", "Available only after coding; language- and style-dependent, so it inflates verbose code and depresses reusable-library projects."),
    VE("What is a Function Point?", "A measure of functionality DELIVERED, counted from requirements (inputs, outputs, inquiries, files) - before any code exists."),
    VE("List the five FP component types.", "External inputs, external outputs, external inquiries, internal logical files, external interface files."),
    VE("Write the FP adjustment formula.", "FP = UFP x (0.65 + 0.01 x S Fi), with Fi the 14 general system characteristics scored 0-5."),
    VE("Why is FP estimable earlier than LOC?", "It is calculated from the SRS, i.e. before design and coding - perfect for planning in week 1."),
    VE("Compute UFP: 2 inputs, 1 output, 1 inquiry, 1 internal file, all average.", "2x4 + 1x5 + 1x4 + 1x10 = 27."),
    VE("What is COCOMO?", "Boehm's empirical model converting estimated KLOC into effort, duration and team size via class-tuned constants."),
    VE("Name COCOMO's three project classes.", "Organic (small/familiar), semi-detached (mixed) and embedded (hard real-time/binding constraints)."),
    VE("Give the basic COCOMO effort and duration equations.", "Effort E = a x (KLOC)^b person-months; Duration D = c x E^d months; team size N = E / D."),
    VE("Organic constants for basic COCOMO?", "a=2.4, b=1.05, c=2.5, d=0.38."),
    VE("Levels of COCOMO?", "Basic (KLOC only), Intermediate (15 cost-driver multipliers), Detailed (drivers applied per phase)."),
    VE("Estimate E, D, N for an organic 10-KLOC app.", "E = 2.4 x 10^1.05 ≈ 27 pm; D = 2.5 x 27^0.38 ≈ 8.7 months; N ≈ 3 people."),
    VE("What is a Work Breakdown Structure?", "The project decomposed hierarchically into tasks/subtasks - the input list for scheduling."),
    VE("What is a task dependency?", "A 'must finish before start' relation - testing depends on coding, deployment on testing."),
    VE("What is a Gantt chart?", "A bar chart: tasks listed vertically, calendar horizontally; bar length = duration; overlaps = parallel work."),
    VE("Gantt strength and weakness?", "Strength: instantly readable progress/schedule view. Weakness: critical-path and deep dependency effects hide unless annotated."),
    VE("When is a flow chart used in scheduling?", "To document the plan-building procedure itself: tasks -> estimate -> dependencies -> chart -> track -> re-plan."),
    VE("What is a sprint burndown chart?", "Daily plot of REMAINING sprint effort against an ideal straight line - shows instantly whether the team is ahead or behind."),
    VE("Burndown above the ideal line means?", "Behind schedule - more work remains than the plan expects today."),
    VE("Which chart suits an agile team and why?", "Burndown: one sprint scope, daily accuracy, zero drawing ceremony; a Gantt is redundant within a sprint."),
    VE("Define risk in software projects.", "An uncertain event which, if it occurs, harms the project - time, cost, quality or people."),
    VE("Name three classic software risks.", "Unrealistic schedule, changing requirements, key-person loss (also: unproven third-party tech)."),
    VE("Steps of risk management?", "Identification, assessment (probability x impact), mitigation planning, monitoring and control."),
    VE("What is risk exposure R?", "R = probability x impact - the ranking number that decides which risks deserve attention."),
    VE("High-probability high-impact risk - response?", "Mitigate now: redesign it out, prototype early, add buffer - plus a concrete contingency (plan B)."),
    VE("What does risk monitoring do?", "Re-scans the register weekly, watches triggers (vendor slipping, churning requirements) and fires plan B when triggered."),
    VE("Avoid/transfer/reduce - examples?", "Avoid: drop the risky feature. Transfer: buy a proven component. Reduce: prototype the unknown API first."),
    VE("What is a risk register?", "A living table: risk, probability, impact, R=P x I, owner, mitigation, trigger - one row per watched risk."),
    VE("Why is Spiral called risk-driven? (link to U1)", "Each cycle runs an explicit risk-analysis quadrant before more engineering spends."),
    VE("Practical 12 deliverable?", "Your project's FP count - table of the five components with weights, UFP, factor sum, final FP."),
    VE("Practical 13 deliverable?", "Basic COCOMO: chosen class with reason, estimated KLOC, E/D/N arithmetic."),
    VE("Practical 14 deliverable?", "Flow-chart the schedule steps; Gantt for a planned project or sprint burndown for an agile one."),
    VE("Estimate effort if basic COCOMO says N = 4 for 8 months.", "E = N x D = 32 person-months."),
    VE("One sentence: estimation vs scheduling vs tracking.", "Estimate predicts size/effort; scheduling turns it into a dated task plan; tracking measures reality against it."),
]

assert len(_VIVA) == 38
VIVA = [
    G("Project Manager and Metrics", _VIVA[0:10]),
    G("COCOMO Estimation", _VIVA[10:16]),
    G("Scheduling Charts", _VIVA[16:24]),
    G("Risk Management", _VIVA[24:38]),
]

EXAM_QS = [
    XE("List and explain the responsibilities of a software project manager.", 4),
    XE("Compare LOC and Function Point metrics, including two weaknesses of each.", 4),
    XE("Explain the five components and the adjustment formula of Function Point analysis.", 6),
    XE("Calculate FP for a mini bus-booking app (2 inputs, 1 output, 1 inquiry, 1 internal file, all average; sum of complexity factors 30). (Practical 12)", 6),
    XE("Explain the COCOMO model with its three project classes.", 4),
    XE("Estimate effort, duration and team size for an organic 10-KLOC project; show equations. (Practical 13)", 6),
    XE("Distinguish Basic, Intermediate and Detailed COCOMO.", 3),
    XE("What is project scheduling? Explain the role of WBS and task dependencies.", 4),
    XE("Draw and explain an example Gantt chart for an 8-week project. (Practical 14)", 4),
    XE("Explain the sprint burndown chart and how a team reads ahead/behind status.", 4),
    XE("Compare Gantt charts and sprint burndown charts as scheduling tools.", 3),
    XE("Explain the four steps of risk management in a loop.", 4),
    XE("Explain probability-impact assessment with a 3x3 risk matrix.", 4),
    XE("Describe mitigation strategies (avoid, transfer, reduce) with software examples.", 4),
    XE("Explain the risk register and the monitoring/control step.", 3),
]
