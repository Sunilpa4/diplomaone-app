"""DI04000011 Unit 3 notes: Software Project Estimation and Scheduling. English only."""
from java_content import make_TJ

SN = {}

T = make_TJ(SN)

SEC_3_1 = {
    "title": {"en": "3.1 The Software Project Manager"},
    "items": [
        T("Responsibilities of a Software Project Manager", """
<ul><li><b>Estimation and planning</b>: project size, effort, cost and duration - then the task schedule that grows from it.</li>
<li><b>People choreography</b>: pick team members, assign tasks to skills, review progress honestly.</li>
<li><b>Risk and change management</b>: keep the risk register current; absorb requirement changes through a controlled process.</li>
<li><b>Communication hub</b>: report status to management and customer; shield the team from daily interruptions.</li>
<li><b>Quality guard</b>: insist reviews and tests actually happen - the schedule may flex, quality may not.</li>
<li>Mental model: the PM is the umbrella activities from Unit 1 embodied as one accountable person.</li></ul>
""", diagram="se3_pm_duties"),
    ],
}

SEC_3_2 = {
    "title": {"en": "3.2 Metrics for Size Estimation"},
    "items": [
        T("Lines of Code (LOC)", """
<ul><li>The oldest metric: estimate how many lines the finished program will have (KLOC = thousands of lines), then effort follows from historical productivity data.</li>
<li><b>Strengths</b>: intuitive, directly measurable against a delivered product.</li>
<li><b>Weaknesses</b>: only computable AFTER coding; strongly language- and style-dependent (the same task is 40 LOC in Python, 200 in assembly); rewards verbosity and punishes reusable libraries.</li>
<li>Variant <b>KLOC</b> feeds COCOMO; variant function-independent FP (below) feeds early estimates.</li></ul>
""", diagram="se3_loc_fp"),
        T("Function Points (FP)", """
<ul><li>FP measures the <b>functionality delivered</b>, from the user's view, BEFORE code exists - directly from requirements/SRS.</li>
<li>Count five component types: <b>external inputs, external outputs, external inquiries, internal logical files, external interface files</b> - each at a simple/average/complex weight.</li>
<li><b>UFP</b> = sum over components of (count &times; weight).</li>
<li>Adjust for product complexity: <b>FP = UFP &times; [0.65 + 0.01 &times; &Sigma;F<sub>i</sub>]</b> over 14 influence factors (data communication, distribution, performance, reusability...), each rated 0-5.</li>
<li>Language-independent and estimable early - its scheduling superpower. Weakness: component weights carry some subjectivity and practice.</li></ul>
""", diagram="se3_fp_calc"),
        T("Worked FP Example (Practical 12)", """
<ul><li>Mini Bus-Booking app requirement: 2 input screens (route entry, booking entry), 1 output (receipt/PNR), 1 inquiry (seat availability), 1 internal file (bookings). All 'average'.</li>
<li>UFP = 2&times;4 + 1&times;5 + 1&times;4 + 1&times;10 = 8 + 5 + 4 + 10 = <b>27</b>.</li>
<li>Suppose the 14 complexity factors sum to 30 (a typical medium project): FP = 27 &times; (0.65 + 0.01&times;30) = 27 &times; 0.95 &#8776; <b>25.7 FP</b>.</li>
<li>Using a calibration of ~5 FP per person-month in our environment &rarr; about <b>5.2 person-months</b> of effort.</li>
<li>For your own project, count every screen, report, table and interface the same way - that count is your Practical 12 deliverable.</li></ul>
"""),
    ],
}

SEC_3_3 = {
    "title": {"en": "3.3 Project Estimation: COCOMO"},
    "items": [
        T("The COCOMO Model", """
<ul><li><b>COnstructive COst MOdel</b> (Boehm, 1981): empirical equations turning estimated KLOC into effort, duration and team size.</li>
<li>Thre product classes: <b>organic</b> (small, familiar, relaxed constraints - a college app), <b>semi-detached</b> (mixed experience/limits), <b>embedded</b> (hard real-time, tight hardware, safety).</li>
<li>Basic COCOMO equations with class constants: E = a&times;(KLOC)<sup>b</sup> person-months; D = c&times;E<sup>d</sup> months; N = E/D people.</li>
<li>Accuracy ladder: <b>Basic</b> (early, KLOC only) &rarr; <b>Intermediate</b> (multiplies by 15 cost drivers: personnel capability, product complexity...) &rarr; <b>Detailed</b> (drivers per phase, per subsystem).</li>
<li>COCOMO II modernises the same idea for reuse, prototyping and object points - syllabus says 'COCOMO / COCOMO II approach', so know both names.</li></ul>
""", diagram="se3_cocomo"),
        T("Worked Basic-COCOMO Example (Practical 13)", """
<ul><li>Estimate for our bus-booking app: judged <b>organic</b>, size about 10 KLOC.</li>
<li>Effort E = 2.4 &times; (10)<sup>1.05</sup> &#8776; 2.4 &times; 11.2 &#8776; <b>27 person-months</b>.</li>
<li>Duration D = 2.5 &times; (27)<sup>0.38</sup> &#8776; 2.5 &times; 3.5 &#8776; <b>8.7 months</b>.</li>
<li>Team size N = E / D &#8776; 27 / 8.7 &#8776; <b>3 people</b> - matches a small class team with a lead.</li>
<li>Method rigour: always state (1) chosen class and WHY, (2) how KLOC was estimated, (3) the arithmetic, (4) the sanity check against FP results.</li></ul>
"""),
    ],
}

SEC_3_4 = {
    "title": {"en": "3.4 Project Scheduling"},
    "items": [
        T("From Estimates to a Schedule", """
<ul><li>Scheduling decomposes the project into tasks (a <b>Work Breakdown Structure</b>), estimates each task's effort, finds <b>dependencies</b> (testing waits on coding) and lays the tasks over a calendar with owners.</li>
<li>The work itself is a LOOP: list tasks &rarr; estimate &rarr; dependencies &rarr; draw chart &rarr; track weekly &rarr; re-plan - the schedule is rebuilt as fast as reality shifts (see flow chart).</li>
<li>Two charting styles follow from the chosen process model: Gantt for planned projects; sprint burndown for agile ones.</li></ul>
""", diagram="se3_flow"),
        T("Gantt Chart", """
<ul><li>One horizontal bar per task over weeks/months; bar length = duration; overlap = parallelism; a bar's end feeding the next bar's start shows dependencies.</li>
<li>Update bars with % done during reviews; slipping bars are impossible to hide - that visibility is the Gantt's power.</li>
<li>Strength: instantly readable by anyone, ideal for communicating plans; weakness: deep 'which delay kills the deadline?' (the critical path) needs annotations or a PERT-style companion.</li>
<li>Practical 14 (traditional track): host your project's tasks on an 8-week Gantt like the example.</li></ul>
""", diagram="se3_gantt"),
        T("Sprint Burndown Chart (Agile)", """
<ul><li>Track <b>remaining effort</b> daily through a sprint: the dashed ideal line drops evenly toward zero; the team's actual line above it = behind schedule, below it = ahead.</li>
<li>Set plotted points honestly each stand-up - the burndown answers "are we on time RIGHT NOW?" in one glance.</li>
<li>Compare: Gantt = when will everything happen; burndown = are we on time today. Sprint-based agile replaces per-task Gantts with per-sprint burndowns.</li>
<li>Practical 14 (agile track): plot remaining task-hours for your sprint every day and read the gap.</li></ul>
""", diagram="se3_burndown"),
    ],
}

SEC_3_5 = {
    "title": {"en": "3.5 Risk Management"},
    "items": [
        T("Risk Identification and Assessment", """
<ul><li>A <b>risk</b> is an uncertain event that, if it happens, hurts the project (deadline, budget, quality, people).</li>
<li><b>Identification</b> sources: checklists of classic software risks (team inexperience, changing requirements, unproven tech), brainstorming with the team, vendor/dependency review.</li>
<li><b>Assessment</b> scores each risk by <b>probability</b> (P) and <b>impact</b> (I); risk exposure R = P &times; I ranks them - high/high demands action today, low/low just gets accepted.</li>
<li>Output: the <b>risk register</b> - risk description, P, I, R, owner, mitigation plan, trigger to watch.</li></ul>
""", diagram="se3_risk_matrix"),
        T("Risk Mitigation, Monitoring and Control", """
<ul><li><b>Mitigation strategies</b>: avoid (drop the risky feature/tech), transfer (buy a proven library, outsource), reduce probability (prototype the scary part first - remember Spiral!), reduce impact (backups, extra buffer).</li>
<li>Only two roots work long-term: <b>risk avoidance</b> (design the risk out) and <b>contingency</b> (prepare a concrete plan B with a trigger).</li>
<li><b>Monitoring &amp; control</b>: re-scan risks weekly, watch trigger signs (API keeps changing, key developer's notice period), execute plan B when triggered, re-score the register.</li>
<li>Exam phrasing: the cycle identify &rarr; assess &rarr; mitigate &rarr; monitor repeats for the project's whole life - never a one-time activity.</li></ul>
""", diagram="se3_risk_cycle"),
    ],
}

NOTES = [SEC_3_1, SEC_3_2, SEC_3_3, SEC_3_4, SEC_3_5]
