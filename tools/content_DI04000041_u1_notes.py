"""DI04000041 Cloud Computing - Unit 1 (Introduction to Cloud Computing).

English-only. Syllabus unit 1: cloud/computing/definition, central ideas, characteristics,
challenges, novel applications, security risks, advantages and disadvantages, 6 h / 17 %.
Every number in the numericals is recomputed in tools/test_DI04000041_u1.py.
"""
from subject_DI04000041 import tr


def p(x):
    return f"<p>{x}</p>"


def h4(x):
    return f"<h4>{x}</h4>"


def ul(*items):
    return "<ul>" + "".join(f"<li>{i}</li>" for i in items) + "</ul>"


def ol(*items):
    return "<ol>" + "".join(f"<li>{i}</li>" for i in items) + "</ol>"


def table(head, rows):
    return ("<table><tr>" + "".join(f"<th>{h}</th>" for h in head) + "</tr>"
            + "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in rows)
            + "</table>")


def self_check(q, a):
    return f'<details class="self-check"><summary>{q}</summary><p>{a}</p></details>'


def card(heading, body, diagram=None, examples=None, syllabus_item=None):
    item = {"h": tr(heading), "body": tr(body)}
    if diagram:
        item["diagram"] = diagram
    if examples:
        item["examples"] = examples
    if syllabus_item:
        item["syllabus_item"] = syllabus_item
    return item


SOURCES = [
    ("GTU DI04000041, Cloud Computing, Semester 4, w.e.f. 2025-26 (uploaded syllabus)",
     "https://s3-ap-southeast-1.amazonaws.com/gtusitecirculars/Syallbus/DI04000041.pdf"),
    ("NIST SP 800-145, The NIST Definition of Cloud Computing",
     "https://csrc.nist.gov/pubs/sp/800/145/final"),
    ("NIST CSRC glossary: cloud computing",
     "https://csrc.nist.gov/glossary/term/cloud_computing"),
    ("Amazon Web Services - Overview of Amazon Web Services (service categories)",
     "https://docs.aws.amazon.com/whitepapers/latest/aws-overview/"),
    ("Microsoft Azure - Azure Architecture Center (cloud design patterns)",
     "https://learn.microsoft.com/en-us/azure/architecture/"),
    ("Google Cloud - Google Cloud overview (regions, zones, shared responsibility)",
     "https://cloud.google.com/docs/overview"),
]

# --------------------------------------------------------------------------- notes
NOTES = [
    {"title": tr("1. Cloud, Computing and the Cloud-Computing Definition"),
     "items": [
         card("1.1 Cloud, computing and what the two words mean together",
              h4("Definition")
              + p("<b>Cloud</b> means the computing resources are not in front of you: they sit in a provider's "
                  "data centre and are reached over a network. <b>Computing</b> means the work itself - "
                  "processing, storing and moving data. <b>Cloud computing</b> combines the two: computing "
                  "delivered as a service from a shared pool, obtained on demand and paid for as it is used.")
              + h4("Explanation and application")
              + ul("The word cloud is a <b>delivery model</b>, not another name for the Internet. The Internet is "
                   "the road; the cloud is the managed factory at the end of it.",
                   "The customer no longer buys the server room. The provider owns the building, power, cooling, "
                   "hardware and the virtualization layer; the customer owns the data, the accounts and the "
                   "configuration.",
                   "Resources are requested through a console or an API in minutes, not through a purchase order "
                   "that takes weeks.",
                   "Capacity is shared: your virtual machine runs beside other tenants on the same physical host, "
                   "isolated by the hypervisor and the provider's controls.")
              + table(["Question", "On-premises server", "Cloud service"],
                      [("Who owns the hardware?", "The college", "The provider"),
                       ("Time to add capacity", "Weeks (budget, delivery, install)", "Minutes (API or console)"),
                       ("Cost pattern", "Capital purchase + maintenance", "Recurring usage-based bill"),
                       ("Who patches the host?", "College IT staff", "Provider patches the platform; the customer "
                                                                      "patches the guest OS and application")])
              + h4("Common mistake / conditions")
              + p("A web application running on a single rented server with a fixed yearly bill is <b>hosting</b>, "
                  "not necessarily cloud computing. Elastic self-service from a shared pool is the test, not the "
                  "presence of a network cable."),
              "cc1_terms", syllabus_item="1.1"),
         card("1.2 The standard definition (NIST SP 800-145)",
              h4("Definition")
              + p("Cloud computing is <b>a model for enabling ubiquitous, convenient, on-demand network access to "
                  "a shared pool of configurable computing resources</b> - networks, servers, storage, "
                  "applications and services - that can be rapidly provisioned and released with minimal "
                  "management effort or provider interaction.")
              + h4("The definition unpacks into three lists")
              + table(["Part of the definition", "What it names", "Where it is used"],
                      [("Five essential characteristics", "On-demand self-service, broad network access, resource "
                                                          "pooling, rapid elasticity, measured service",
                        "Unit 1: the properties every cloud must show"),
                       ("Three service models", "SaaS, PaaS, IaaS", "Unit 3: who manages which layer"),
                       ("Four deployment models", "Public, private, hybrid, community", "Unit 2: who shares the "
                                                                                     "infrastructure")])
              + h4("Why the wording matters in an exam")
              + ul("Every phrase carries a mark: <b>ubiquitous</b> (anywhere), <b>on-demand</b> (no waiting for "
                   "procurement), <b>shared pool</b> (multi-tenancy), <b>rapidly provisioned and released</b> "
                   "(elasticity) and <b>minimal management effort</b> (self-service automation).",
                   "The same definition is the reason a private cloud still counts: ownership does not change the "
                   "model, sharing and automation do.")
              + self_check("Is a college data centre with virtualization but no self-service a cloud?",
                           "It is a virtualized data centre. Without on-demand self-service, pooling and measured "
                           "service it does not meet the NIST definition, even though the same hypervisor is used."),
              "cc1_central", syllabus_item="1.1"),
         card("1.3 The central ideas behind cloud computing",
              h4("Definition")
              + p("Six ideas carry the whole model. Remove any one and the economics or the elasticity collapses.")
              + h4("Explanation and application")
              + table(["Central idea", "What it does", "What disappears"],
                      [("Resource pooling", "Many customers share one large pool of hardware",
                        "One server per application"),
                       ("Virtualization", "A hypervisor slices hardware into isolated virtual machines",
                        "Hardware bound to one operating system"),
                       ("Elasticity", "Capacity grows and shrinks with load",
                        "Buying for the yearly peak"),
                       ("Self-service", "The user provisions through a portal or API", "Ticket queues for a VM"),
                       ("Measured service", "Usage is metered and billed", "One flat annual bill"),
                       ("Automation and orchestration", "Templates, autoscaling, infrastructure as code",
                        "Manual rebuilds that nobody can reproduce")])
              + h4("Relation to the syllabus")
              + p("These ideas are the mechanism; the <b>characteristics</b> in the next section are the observable "
                  "result; the <b>challenges</b> later in this unit are the price paid for them. Answering "
                  "\"explain central ideas\" by listing the five characteristics loses marks, because the "
                  "characteristics are outcomes, not mechanisms."),
              "cc1_central", syllabus_item="1.2")]},

    {"title": tr("2. Characteristics of Cloud Computing"),
     "items": [
         card("2.1 The five essential characteristics",
              h4("Definition")
              + p("A service is cloud computing only if it shows all five essential characteristics. Four out of "
                  "five is hosting.")
              + h4("Explanation and application")
              + table(["Characteristic", "Meaning", "Observable symptom"],
                      [("On-demand self-service", "The consumer provisions compute, storage or software without "
                                                  "human interaction with the provider",
                        "A student creates a VM at 2 a.m. from a portal"),
                       ("Broad network access", "Services are reachable over the network from phones, laptops and "
                                                "other standard clients",
                        "The same catalogue opens on a phone and a lab PC"),
                       ("Resource pooling", "Provider resources serve many consumers from a shared pool, with "
                                            "location abstracted",
                        "A new VM lands in any available host of the region"),
                       ("Rapid elasticity", "Capacity can scale out and back quickly, appearing unlimited to the "
                                            "consumer",
                        "Result-day traffic is absorbed, then the extra capacity is released"),
                       ("Measured service", "Usage is automatically metered, controlled and reported",
                        "The bill lists vCPU-hours, GB-months and egress GB")])
              + h4("Common mistake / conditions")
              + p("\"Elastic\" is not the same as \"unlimited\". Elasticity is bounded by the provider's quota, the "
                  "account's limit and the budget. A quota reached during a result-day spike is a real outage in "
                  "exactly the same way as a full on-premises server."),
              "cc1_characteristics", syllabus_item="1.3"),
         card("2.2 Supporting traits that are not on the five-item list",
              h4("Definition")
              + p("Multi-tenancy, resilience, automation and a metered catalogue are not in the NIST list of five, "
                  "yet they are the properties students actually notice. Treat them as supporting traits.")
              + h4("Explanation and application")
              + ul("<b>Multi-tenancy:</b> several customers share the physical layer. It is the source of the "
                   "price advantage and the source of the isolation question in Unit 5.",
                   "<b>Resilience:</b> a provider replicates across zones, but only if the customer uses more than "
                   "one zone. A single-zone deployment inherits the zone's failures.",
                   "<b>Automation:</b> templates and infrastructure-as-code make environments reproducible, which "
                   "is what makes elastic scaling safe.",
                   "<b>Metered billing:</b> cost becomes a design variable. A poorly designed query can cost more "
                   "than a server, which is why cost control is listed as a challenge in Section 3.")
              + h4("Examination use")
              + p("If a question asks for the characteristics, give the five and name the supporting traits "
                  "separately. Mixing them into one list is the most common way to lose the structure marks."),
              syllabus_item="1.3"),
         card("2.3 What is not cloud computing",
              h4("Definition")
              + p("Three services are often mislabelled as cloud. Each fails at least one essential characteristic.")
              + h4("Explanation and application")
              + table(["Service", "Why it is not cloud", "What it really is"],
                      [("Colocation", "The customer owns the hardware; no pooling, no self-service, no elasticity",
                        "Rented space, power and cooling"),
                       ("Plain shared web hosting", "Fixed plans, no measured compute, no API-driven provisioning",
                        "Managed hosting"),
                       ("A virtual machine on a laptop", "Virtualization without pooling, network access or "
                                                         "measured service",
                        "Local virtualization (useful, but not cloud)"),
                       ("Traditional IT outsourcing", "A contract to run the customer's own servers",
                        "Managed services on dedicated hardware")])
              + h4("Test to apply in the viva")
              + ol("Can the consumer provision it without talking to a human?",
                   "Is the capacity drawn from a pool shared with other tenants?",
                   "Can it grow and shrink within minutes?",
                   "Is usage metered and billed?")
              + p("Any \"no\" means the service is hosted or virtualized, not cloud computing."),
              syllabus_item="1.3")]},

    {"title": tr("3. Challenges of Cloud Computing"),
     "items": [
         card("3.1 Technical challenges",
              h4("Definition")
              + p("Technical challenges come from putting a boundary between the application and the hardware it "
                  "runs on. Each one has a measurable symptom and a standard mitigation.")
              + h4("Explanation and application")
              + ul("<b>Connectivity dependence:</b> if the campus link is down, a cloud-hosted exam portal is down "
                   "even though the provider is healthy. Mitigate with a redundant link, not with hope.",
                   "<b>Latency and bandwidth:</b> a round trip to a distant region adds delay to every request; "
                   "data-heavy workflows pay for egress. Keep chatty protocols off long-haul links.",
                   "<b>Migration complexity:</b> moving a database is easy until the stored procedures, scheduled "
                   "jobs and licence dependencies arrive with it.",
                   "<b>Integration with legacy systems:</b> an on-premises ERP on a private address space needs a "
                   "secure tunnel or an API before anything can talk to it.",
                   "<b>Performance variability:</b> a noisy neighbour on a shared host, or a burst credit "
                   "exhausted, changes throughput without changing configuration.",
                   "<b>Skills:</b> cloud work is configuration, identity and cost engineering, not only servers.")
              + h4("Common mistake / conditions")
              + p("\"The cloud is down\" is usually a statement about one service, one region or one configuration. "
                  "Diagnose in layers: link, DNS, identity, quota, application, then provider status."),
              "cc1_challenges", syllabus_item="1.4"),
         card("3.2 Business, legal and cost challenges",
              h4("Definition")
              + p("The commercial and legal obligations do not disappear when the server does; they move into a "
                  "contract and a bill.")
              + h4("Explanation and application")
              + table(["Challenge", "Why it matters", "Practical control"],
                      [("Vendor lock-in", "Proprietary services and APIs make exit expensive",
                        "Prefer open formats; keep an export path documented"),
                       ("Compliance and data residency", "Some records must stay in a stated jurisdiction",
                        "Choose the region first, then the service"),
                       ("Unpredictable cost", "Elastic capacity can multiply spend in a weekend",
                        "Budgets, alerts, tagging and a monthly review"),
                       ("Shadow IT", "A department buys its own cloud account outside IT policy",
                        "Central account structure with delegated, audited access"),
                       ("SLA gaps", "A 99.9 % promise still allows hours of downtime, and credits are not "
                                    "refunds of business loss",
                        "Read the remedy clause; design for failure; keep a fallback"),
                       ("Exit and skills", "The team that built the system may not be able to rebuild it elsewhere",
                        "Document architecture; avoid unmanaged one-off configuration")])
              + h4("Reading an SLA honestly")
              + p("An SLA is a service credit agreement, not an insurance policy. Before quoting a percentage in an "
                  "answer, convert it into downtime with the arithmetic in Section 7 - 99.9 % of a month is "
                  "still about 43 minutes."),
              syllabus_item="1.4")]},

    {"title": tr("4. Novel Applications of Cloud Computing"),
     "items": [
         card("4.1 Education and campus services",
              h4("Definition")
              + p("Colleges were early adopters because their load is spiky and their budgets are capital-poor: "
                  "a result portal is idle for weeks and then serves the whole institute in one morning.")
              + h4("Explanation and application")
              + ul("<b>Learning management:</b> course material, assignments and video lectures in object storage, "
                   "with the application tier scaled on demand.",
                   "<b>Examination and result portals:</b> the classic burst pattern - minutes of extreme load "
                   "followed by months of quiet.",
                   "<b>Virtual laboratories:</b> browser-accessible machines for programming, networking or "
                   "simulation practicals, reset from a template between batches.",
                   "<b>Backup and archival:</b> staff records and project reports replicated to a second region at "
                   "low cost.",
                   "<b>Collaboration:</b> shared documents and mail with identity managed centrally.")
              + h4("Why cloud fits")
              + p("The demand curve, not the technology, is the argument: paying for peak capacity all year would "
                  "waste most of it."),
              syllabus_item="1.5"),
         card("4.2 Health, agriculture, transport and media",
              h4("Definition")
              + p("The novel applications share one pattern: many small sites producing data that is analysed "
                  "centrally and answered back to a phone.")
              + h4("Explanation and application")
              + table(["Domain", "Cloud application", "Why cloud"],
                      [("Health", "Telemedicine records, imaging archives, appointment systems",
                        "Spiky demand, large images, strict access control"),
                       ("Agriculture", "Soil and weather advisories, mandi price feeds, drone imagery",
                        "Seasonal peaks, many remote users"),
                       ("Transport", "Ticketing, fleet tracking, route planning",
                        "Burst load at festival peaks; location data from vehicles"),
                       ("Media", "Video transcoding, content delivery, recommendation engines",
                        "Storage-heavy and compute-heavy for short periods")])
              + h4("Condition to state in an answer")
              + p("Each of these handles personal data, so the application is only acceptable with the privacy "
                  "controls of Unit 5: least-privilege access, encryption, audit logging and a deletion policy."),
              syllabus_item="1.5"),
         card("4.3 Engineering analytics: the green-hydrogen data hub",
              h4("Definition")
              + p("A hydrogen plant produces a continuous stream of measurements - electrolyser current, stack "
                  "temperature, pressure, purity, renewable input and output flow. Cloud analytics turns that "
                  "stream into maintenance decisions and efficiency gains.")
              + h4("Explanation and application")
              + ol("<b>Ingest:</b> sensors and gateways push readings to a cloud endpoint at a fixed interval.",
                   "<b>Store:</b> raw telemetry in object storage; downsampled series in a time-series database "
                   "for fast charts.",
                   "<b>Analyse:</b> detect drift, estimate efficiency (energy per kilogram of hydrogen) and flag "
                   "anomalies before a stack fails.",
                   "<b>Predict:</b> a model trained on history schedules maintenance instead of waiting for a "
                   "breakdown.",
                   "<b>Present:</b> a dashboard shows the plant, the fleet of sites and the savings to operators "
                   "and management.")
              + h4("Why cloud, and where its limits are")
              + ul("Fits: multi-site data collection, variable computing for model training, and remote dashboards "
                   "that must work from a phone.",
                   "Limits: a control loop that trips a valve cannot wait for a network round trip - safety "
                   "control stays local, analytics stays in the cloud.",
                   "Limits: plant data may be commercially sensitive or legally local, so region choice and access "
                   "control are part of the design, not an afterthought."),
              "cc1_hydrogen", syllabus_item="1.5"),
     ]},

    {"title": tr("5. Security Risks of Cloud Computing"),
     "items": [
         card("5.1 Shared responsibility: who secures what",
              h4("Definition")
              + p("Security in the cloud is split. The provider secures the cloud <b>of</b> the cloud - facilities, "
                  "hardware, network fabric and the virtualization layer. The customer secures what runs <b>in</b> "
                  "the cloud - data, identities, configuration and application code.")
              + h4("Explanation and application")
              + table(["Layer", "Responsible party (IaaS)", "Typical failure"],
                      [("Facility, power, physical access", "Provider", "Rare; covered by provider audits"),
                       ("Host hardware, network fabric", "Provider", "Hardware fault, network partition"),
                       ("Hypervisor and isolation", "Provider", "A tenant escape would be a provider fault"),
                       ("Guest operating system and patches", "Customer", "Unpatched server exploited"),
                       ("Identity, keys and permissions", "Customer", "Over-privileged account, leaked key"),
                       ("Data classification and encryption", "Customer", "Public bucket holding student records"),
                       ("Application code and configuration", "Customer", "Debug endpoint left enabled")])
              + h4("Common mistake / conditions")
              + p("The provider's compliance certificate covers the provider's half. It does not make an "
                  "openly-readable storage bucket compliant. Most real cloud incidents land on the customer's "
                  "side of the line."),
              "cc1_shared", syllabus_item="1.6"),
         card("5.2 Seven common cloud security risks and their controls",
              h4("Definition")
              + p("The risks below are the ones a diploma project or a campus deployment actually meets. Each "
                  "control is something a student can configure.")
              + h4("Explanation and application")
              + table(["Risk", "What it looks like", "Control"],
                      [("Misconfiguration", "Storage bucket set to public; security group open to 0.0.0.0/0",
                        "Templates with secure defaults; configuration scanning; review before release"),
                       ("Account compromise", "No multi-factor authentication; long-lived access keys in code",
                        "MFA on all privileged accounts; short-lived roles; secrets in a managed store"),
                       ("Insecure API", "Unencrypted endpoints; no rate limit; verbose errors",
                        "TLS everywhere; authentication on every route; throttle and log"),
                       ("Data breach", "Sensitive data copied out through a stolen credential",
                        "Least privilege, encryption at rest and in transit, anomaly alerts"),
                       ("Denial of service", "Traffic or cost exhaustion against a public endpoint",
                        "Edge filtering, autoscaling limits, budget alerts, provider DDoS protection"),
                       ("Malicious insider", "An administrator reads data without a need to know",
                        "Separation of duties, audit trails, access reviews"),
                       ("Data loss", "Deleted object, failed migration, no tested backup",
                        "Versioning, cross-region backup, restore drills")])
              + h4("Shared-tenancy caution")
              + p("Isolation between tenants is the provider's job, but a shared service still shares fate: a "
                  "regional control-plane failure affects every tenant in that region, which is why multi-zone "
                  "design is the customer's decision."),
              syllabus_item="1.6"),
         card("5.3 Privacy: location, retention and third-party access",
              h4("Definition")
              + p("Privacy asks a different question from security: not only \"who can reach the data\" but \"who "
                  "may lawfully hold it, for how long, and where\".")
              + h4("Explanation and application")
              + ul("<b>Location:</b> a region choice decides which country's law applies to the stored copy.",
                   "<b>Retention and deletion:</b> a deletion request must also reach backups and replicas, or the "
                   "data never really leaves.",
                   "<b>Third-party access:</b> providers use sub-processors; the customer must know who can touch "
                   "the data and under what terms.",
                   "<b>Access by provider staff:</b> support access should be logged, time-limited and approved.",
                   "<b>Exit copy:</b> the customer must be able to take a usable export away, not only a screenshot.")
              + h4("Indian context")
              + p("For personal data of students or patients, the Digital Personal Data Protection Act, 2023 "
                  "introduces consent, purpose limitation and breach-reporting duties on the data fiduciary. Cloud "
                  "does not transfer those duties to the provider; the institute remains responsible."),
              syllabus_item="1.6")]},

    {"title": tr("6. Advantages and Disadvantages"),
     "items": [
         card("6.1 Advantages, with the reason behind each",
              h4("Definition")
              + p("The advantages are all consequences of pooling, elasticity and measured service - which is why "
                  "they should be stated with their mechanism, not as a list of adjectives.")
              + h4("Explanation and application")
              + table(["Advantage", "Mechanism", "Example"],
                      [("No capital expenditure", "Provider owns the hardware; the customer pays monthly",
                        "A department starts a project without buying servers"),
                       ("Elastic capacity", "Pooled resources are added and released in minutes",
                        "Result-day portal absorbs a spike"),
                       ("Global reach", "Regions place the application near its users",
                        "An app served from Mumbai and Singapore"),
                       ("Managed services", "Databases, queues and monitoring are run by the provider",
                        "The team writes features instead of patching database hosts"),
                       ("Resilience options", "Multi-zone replication is a configuration choice",
                        "A zone failure does not stop the service"),
                       ("Faster experiments", "Environments are created and destroyed on demand",
                        "A lab batch of 60 machines for two hours")])
              + h4("Condition")
              + p("Every advantage is conditional on design. Elastic capacity without a budget alert becomes "
                  "elastic cost; managed services without an exit plan become lock-in."),
              "cc1_advdis", syllabus_item="1.7"),
         card("6.2 Disadvantages and their honest limits",
              h4("Definition")
              + p("The disadvantages are the mirror image of the same properties. An exam answer that lists only "
                  "benefits is incomplete.")
              + h4("Explanation and application")
              + ul("<b>Recurring cost:</b> a stable workload run for years can cost more than owned hardware. "
                   "Model it - Section 7 does exactly that.",
                   "<b>Network dependency:</b> the campus link becomes a single point of failure for teaching "
                   "systems.",
                   "<b>Egress and storage charges:</b> data leaving the provider is billed, and archives grow "
                   "quietly.",
                   "<b>Limited control:</b> no access to the physical host, the hypervisor or the maintenance "
                   "window.",
                   "<b>Vendor lock-in:</b> proprietary APIs, identity models and managed services raise exit cost.",
                   "<b>Latency:</b> every call crosses a network boundary; hard real-time control is unsuitable.",
                   "<b>Compliance and trust:</b> data location, sub-processors and lawful access are contract "
                   "questions, not technical ones.")
              + h4("Balance")
              + p("The correct conclusion is not \"cloud is good\" or \"cloud is bad\", but \"cloud for spiky, "
                  "new or distributed workloads; owned hardware for stable, predictable, latency-critical or "
                  "strictly local workloads\"."),
              syllabus_item="1.7"),
         card("6.3 When cloud is the wrong choice",
              h4("Definition")
              + p("A decision checklist is more useful than a slogan. If any of these is true, a cloud-first "
                  "answer needs a strong justification.")
              + h4("Explanation and application")
              + ol("<b>Hard real-time control</b> - a loop that must react in milliseconds stays local.",
                   "<b>Strict data localisation</b> - if no available region satisfies the rule, the data cannot "
                   "leave.",
                   "<b>Stable, fully used hardware</b> - a server already running at high utilisation for years is "
                   "cheap to keep.",
                   "<b>No reliable connectivity</b> - a site with intermittent power and link cannot depend on a "
                   "remote console.",
                   "<b>Unbudgeted metered spend</b> - an organisation that cannot monitor a variable bill will "
                   "either overspend or be surprised.")
              + h4("Decision pattern for a report")
              + p("State the workload, the demand shape, the data sensitivity, the connectivity and the cost model. "
                  "Then choose public, private, hybrid or community - the deployment models are the next unit."),
              syllabus_item="1.7")]},

    {"title": tr("7. Worked Numericals: Availability, Cost and Sizing"),
     "items": [
         card("7.1 Availability percentages converted into downtime",
              h4("Definition")
              + p("An availability figure is only meaningful as downtime. The conversion is one line: allowed "
                  "downtime = (100 % - availability) x total minutes.")
              + h4("Explanation and application")
              + p("Three worked examples use a year (525,600 minutes) and a 30-day month (43,200 minutes). They are "
                  "linked below as EX boxes; the arithmetic and the check line are in each box.")
              + ol("<b>99.9 % for one year:</b> 0.1 % of 525,600 = <b>525.6 minutes = 8.76 hours</b>.",
                   "<b>99.95 % for a month:</b> 0.05 % of 43,200 = <b>21.6 minutes</b>.",
                   "<b>99.99 % for a month:</b> 0.01 % of 43,200 = <b>4.32 minutes</b>.")
              + h4("Interpretation")
              + p("The jump from 99.9 % to 99.99 % is a factor of ten in downtime, and usually a much larger factor "
                  "in engineering effort: redundancy, health checks, tested failover and rehearsed recovery. Quote "
                  "the minutes, not the marketing percentage."),
              examples=["cc1n1", "cc1n2", "cc1n3"], syllabus_item="1.7"),
         card("7.2 Comparing owned hardware with a cloud bill",
              h4("Definition")
              + p("The fair comparison is total cost over the same period: capital cost plus operations on one "
                  "side, usage-based cost plus egress on the other.")
              + h4("Explanation and application")
              + ul("One-time purchase is divided by the monthly difference to get a break-even point.",
                   "If the cloud bill is higher every month, break-even is the number of months after which the "
                   "purchase wins - provided the server really lives that long.",
                   "If the server would be idle for most of the year, there is no break-even to compute: the "
                   "cloud wins on avoided idle capacity.")
              + h4("Worked example")
              + p("A server costs 90,000 once, plus 3,000 per month to run. The equivalent cloud service is 8,000 "
                  "per month with no purchase. Break-even = 90,000 / (8,000 - 3,000) = <b>18 months</b>. Below 18 "
                  "months the cloud is cheaper; above it, ownership is - in this simple model that ignores refresh, "
                  "staff time and failure risk."),
              examples=["cc1n4", "cc1n5"], syllabus_item="1.7"),
         card("7.3 Sizing storage, egress and sensor data",
              h4("Definition")
              + p("Three bills dominate most student projects: stored GB-months, egress GB and the compute needed "
                  "after consolidation.")
              + h4("Explanation and application")
              + ol("<b>Growth:</b> stored volume after n years = initial volume x (1 + growth)^n. Multiply by the "
                   "per-GB rate for the monthly bill.",
                   "<b>Egress:</b> monthly transfer x per-GB rate; multiply by 12 for the yearly figure, because it "
                   "is usually the surprise line.",
                   "<b>Consolidation:</b> used capacity = servers x vCPU x utilisation; add headroom before choosing "
                   "the instance size.",
                   "<b>Telemetry:</b> samples per month x bytes per sample. Raw sensor data is small; indexes, "
                   "replication and dashboards are what cost money.")
              + h4("Interpretation")
              + p("Storage grows exponentially but slowly at first; egress grows with popularity; telemetry grows "
                  "with the number of sensors. Model all three before quoting a monthly cost to a client."),
              examples=["cc1n6", "cc1n7", "cc1n8"], syllabus_item="1.7")]},
]

# --------------------------------------------------------------------------- numericals
NUMERICALS = [
    {"id": "cc1n1",
     "q": tr("A provider promises 99.9 % availability for one year. How much downtime does that allow, in minutes "
             "and in hours?"),
     "a": tr(h4("Given and assumptions")
             + p("Availability = 99.9 %; one year = 365 days; a year has 365 x 24 x 60 = 525,600 minutes. Treat "
                 "the promise as the whole allowed budget for the year.")
             + h4("Formula")
             + p("Allowed downtime = (100 % - availability) x total minutes")
             + h4("Step-by-step solution")
             + ol("Unavailability = 100 % - 99.9 % = 0.1 % = 0.001",
                  "Downtime = 0.001 x 525,600 = 525.6 minutes",
                  "525.6 / 60 = 8.76 hours")
             + h4("Interpretation and check")
             + p("<b>About 526 minutes, that is 8.76 hours, per year.</b> Check: 8.76 h is a little over one "
                 "working day, which matches the rule of thumb that each additional 9 in the SLA removes roughly "
                 "90 % of the allowed downtime."))},
    {"id": "cc1n2",
     "q": tr("An exam portal is contracted at 99.95 % for a 30-day month. What downtime is permitted?"),
     "a": tr(h4("Given and assumptions")
             + p("Availability = 99.95 %; month = 30 days = 30 x 24 x 60 = 43,200 minutes.")
             + h4("Formula")
             + p("Allowed downtime = (1 - 0.9995) x 43,200")
             + h4("Step-by-step solution")
             + ol("Unavailability = 0.0005",
                  "Downtime = 0.0005 x 43,200 = 21.6 minutes")
             + h4("Interpretation and check")
             + p("<b>21.6 minutes per month.</b> One unplanned 25-minute outage already exceeds the monthly budget, "
                 "so a result-day deployment needs tested failover rather than a better promise."))},
    {"id": "cc1n3",
     "q": tr("Complete the table for a 30-day month: 99 %, 99.5 %, 99.9 %, 99.95 % and 99.99 % availability, in "
             "minutes of allowed downtime."),
     "a": tr(h4("Given and assumptions")
             + p("30-day month = 43,200 minutes. Downtime = (1 - availability) x 43,200.")
             + h4("Step-by-step solution")
             + table(["Availability", "Unavailability", "Allowed downtime"],
                     [("99 %", "0.01", "432 min (7.2 h)"),
                      ("99.5 %", "0.005", "216 min (3.6 h)"),
                      ("99.9 %", "0.001", "43.2 min"),
                      ("99.95 %", "0.0005", "21.6 min"),
                      ("99.99 %", "0.0001", "4.32 min")])
             + h4("Interpretation and check")
             + p("Each nine divides the allowance by about ten. Check: 43,200 x 0.001 = 43.2, and 43,200 x 0.0001 = "
                 "4.32, so the trend is consistent."))},
    {"id": "cc1n4",
     "q": tr("A college can buy a server for 90,000 and run it for 3,000 per month, or rent an equivalent cloud "
             "service for 8,000 per month with no purchase. Find the break-even period."),
     "a": tr(h4("Given and assumptions")
             + p("Purchase = 90,000 (one time); on-premises running cost = 3,000 per month; cloud = 8,000 per "
                 "month. Ignore hardware refresh, staff time and failure risk; both options deliver the same "
                 "capacity.")
             + h4("Formula")
             + p("Break-even months = purchase price / (cloud monthly cost - on-premises monthly cost)")
             + h4("Step-by-step solution")
             + ol("Monthly difference = 8,000 - 3,000 = 5,000",
                  "Break-even = 90,000 / 5,000 = 18 months")
             + h4("Interpretation and check")
             + p("<b>18 months.</b> If the server is genuinely used for three years, ownership saves "
                 "5,000 x 18 = 90,000 after the break-even. If the workload is idle for two thirds of the year, "
                 "the comparison should be made against a smaller cloud instance instead - the assumption, not "
                 "the arithmetic, decides the answer."))},
    {"id": "cc1n5",
     "q": tr("A project stores 4 TB today, growing 25 % per year. Cloud storage costs 1.50 per GB-month (1 TB = "
             "1,000 GB). Find the monthly storage cost after two years."),
     "a": tr(h4("Given and assumptions")
             + p("Initial volume = 4 TB; growth = 25 % per year for 2 years; rate = 1.50 per GB-month; decimal "
                 "multiples (1 TB = 1,000 GB).")
             + h4("Formula")
             + p("Volume after n years = 4 x (1.25)^n TB; cost = volume in GB x rate")
             + h4("Step-by-step solution")
             + ol("Year 1: 4 x 1.25 = 5 TB = 5,000 GB",
                  "Year 2: 5 x 1.25 = 6.25 TB = 6,250 GB",
                  "Cost = 6,250 x 1.50 = 9,375 per month")
             + h4("Interpretation and check")
             + p("<b>9,375 per month</b> after two years, against 6,000 for the first year's 4 TB. Check: 6.25/4 = "
                 "1.5625 = 1.25 squared, so the volume grew 56.25 % in two years and the bill grew by the same "
                 "factor. Archive tiers and lifecycle rules control this line."))},
    {"id": "cc1n6",
     "q": tr("A media project serves 1.5 TB of egress per month at 4.20 per GB. Find the monthly and yearly "
             "egress cost."),
     "a": tr(h4("Given and assumptions")
             + p("Egress = 1.5 TB per month = 1,500 GB; rate = 4.20 per GB; 12 months.")
             + h4("Formula")
             + p("Monthly cost = GB x rate; yearly cost = monthly x 12")
             + h4("Step-by-step solution")
             + ol("Monthly = 1,500 x 4.20 = 6,300",
                  "Yearly = 6,300 x 12 = 75,600")
             + h4("Interpretation and check")
             + p("<b>6,300 per month, 75,600 per year.</b> Check the order of magnitude: 4.2 per GB means roughly "
                 "4,200 per TB, and 1.5 TB x 4,200 = 6,300. Serving media through a CDN with a committed plan, or "
                 "compressing it, usually moves this line more than any compute decision."))},
    {"id": "cc1n7",
     "q": tr("Eight servers each have 8 vCPU and average 12 % utilisation. How much capacity is actually used, "
             "and what instance size replaces the estate with 40 % headroom?"),
     "a": tr(h4("Given and assumptions")
             + p("8 servers x 8 vCPU = 64 vCPU installed; average utilisation 12 %; headroom factor 1.4 before "
                 "choosing the instance; assume the workload can be consolidated onto one host.")
             + h4("Formula")
             + p("Used capacity = servers x vCPU x utilisation; required = used x headroom")
             + h4("Step-by-step solution")
             + ol("Installed = 8 x 8 = 64 vCPU",
                  "Used = 64 x 0.12 = 7.68 vCPU",
                  "Required with headroom = 7.68 x 1.4 = 10.75, so choose a 12 vCPU instance",
                  "Capacity retired = 64 - 12 = 52 vCPU (81 %)")
             + h4("Interpretation and check")
             + p("<b>7.68 vCPU are doing the work; a 12 vCPU instance replaces 64.</b> The saving is real, but the "
                 "consolidated host is now a single point of failure: keep a second instance or a tested restore "
                 "path before switching off the old servers."))},
    {"id": "cc1n8",
     "q": tr("A hydrogen plant has 2,000 sensors, each sending one 8-byte sample per minute. Find the raw "
             "telemetry volume per day and per 30-day month, and its storage cost at 1.50 per GB-month."),
     "a": tr(h4("Given and assumptions")
             + p("Sensors = 2,000; rate = 1 sample per minute; payload = 8 bytes; 1 day = 1,440 minutes; month = 30 "
                 "days; 1 GB = 1,000,000,000 bytes (decimal); ignore protocol and index overhead.")
             + h4("Formula")
             + p("Samples per day = sensors x samples per minute x 1,440; bytes = samples x 8")
             + h4("Step-by-step solution")
             + ol("Samples per day = 2,000 x 1,440 = 2,880,000",
                  "Bytes per day = 2,880,000 x 8 = 23,040,000 B = 23.04 MB",
                  "Bytes per month = 23.04 x 30 = 691.2 MB = 0.6912 GB",
                  "Monthly storage cost = 0.6912 x 1.50 = about 1.04")
             + h4("Interpretation and check")
             + p("<b>23.04 MB per day, 691.2 MB per month, about 1.04 per month to store raw.</b> The lesson is "
                 "that raw telemetry is not the cost driver: the time-series index, replication, long retention and "
                 "the dashboards that query it usually cost far more than the bytes themselves."))},
]

# --------------------------------------------------------------------------- reference tab
EQUATIONS = [
    {"title": tr("Rules worth quoting exactly"),
     "items": [
         {"name": tr("Cloud is not the Internet"),
          "f": "cloud = delivered service; Internet = transport",
          "terms": tr("The Internet carries the traffic; the cloud is the managed, metered service at the end "
                      "of it.")},
         {"name": tr("The cloud test"),
          "f": "self-service + pooling + elasticity + metering",
          "terms": tr("Fail one of these and the service is hosting or virtualization, not cloud computing.")},
         {"name": tr("Elasticity vs scalability"),
          "f": "elastic = up and down; scalable = can grow",
          "terms": tr("Only elasticity releases capacity again, which is what makes the bill follow the load.")},
         {"name": tr("Multi-tenancy"),
          "f": "many tenants → one shared physical pool",
          "terms": tr("Source of the price advantage and of the isolation question in Unit 5.")},
         {"name": tr("Shared responsibility"),
          "f": "provider secures the cloud; customer secures in it",
          "terms": tr("The provider's certificate covers its half only; configuration and data remain the "
                      "customer's duty.")},
     ]},
    {"title": tr("Availability arithmetic"),
     "items": [
         {"name": tr("Allowed downtime"),
          "f": "downtime = (1 - availability) x total minutes",
          "terms": tr("Year = 525,600 min; 30-day month = 43,200 min; 31-day month = 44,640 min.")},
         {"name": tr("Availability from measurements"),
          "f": "A = uptime / (uptime + downtime) x 100 %",
          "terms": tr("Use the same observation window for both terms, otherwise the figure is meaningless.")},
         {"name": tr("Composite availability"),
          "f": "A(total) = A1 x A2 x ... (independent parts in series)",
          "terms": tr("Two 99.9 % components in series give about 99.8 %: chaining services lowers availability.")},
         {"name": tr("Redundancy"),
          "f": "A(pair) = 1 - (1 - A)^2",
          "terms": tr("Two independent 99 % paths give 99.99 %: redundancy raises availability only if the "
                      "failure modes are independent.")},
     ]},
    {"title": tr("Cost and sizing formulas"),
     "items": [
         {"name": tr("Break-even"),
          "f": "months = purchase / (cloud monthly - on-prem monthly)",
          "terms": tr("Only valid when both options deliver the same capacity and service level.")},
         {"name": tr("Growth"),
          "f": "V(n) = V0 x (1 + g)^n",
          "terms": tr("Storage and telemetry planning; multiply by the per-GB-month rate for the bill.")},
         {"name": tr("Egress"),
          "f": "cost = GB out x rate per GB",
          "terms": tr("Inbound traffic is usually free; outbound is billed. Check the current rate in the "
                      "provider's price list before quoting.")},
         {"name": tr("Consolidation"),
          "f": "used vCPU = servers x vCPU x utilisation",
          "terms": tr("Add 30-50 % headroom before choosing the instance size; a consolidated host is a single "
                      "point of failure.")},
     ]},
    {"title": tr("Unit 1 in one line each"),
     "items": [
         {"name": tr("Five characteristics"),
          "f": "self-service, broad access, pooling, elasticity, measured",
          "terms": tr("All five are required; four out of five is hosting.")},
         {"name": tr("Three service models"),
          "f": "SaaS, PaaS, IaaS",
          "terms": tr("Unit 3. The split decides who patches the operating system.")},
         {"name": tr("Four deployment models"),
          "f": "public, private, hybrid, community",
          "terms": tr("Unit 2. The split decides who shares the infrastructure.")},
         {"name": tr("Unit 1 sequence"),
          "f": "definition → ideas → traits → limits → uses",
          "terms": tr("Answer structure: definition first, then characteristics, then challenges, then "
                      "applications, then risks.")},
     ]},
]

# --------------------------------------------------------------------------- viva
VIVA = [
    {"title": tr("Basics and definitions"), "items": [
        {"q": tr("Define cloud computing."),
         "a": tr("A model that provides on-demand network access to a shared pool of configurable computing "
                 "resources which can be provisioned and released rapidly with minimal management effort.")},
        {"q": tr("Is cloud computing the same as the Internet?"),
         "a": tr("No. The Internet is the transport; cloud computing is computing delivered as a metered service "
                 "over that transport.")},
        {"q": tr("Name the five essential characteristics."),
         "a": tr("On-demand self-service, broad network access, resource pooling, rapid elasticity and measured "
                 "service.")},
        {"q": tr("What is resource pooling?"),
         "a": tr("Provider hardware is shared by many consumers, with the exact physical location hidden from "
                 "them and isolation enforced by the platform.")},
        {"q": tr("What is measured service?"),
         "a": tr("Usage of compute, storage and network is metered automatically and billed, so cost depends on "
                 "what is consumed.")},
        {"q": tr("Give four central ideas behind cloud computing."),
         "a": tr("Virtualization, resource pooling, elasticity and self-service, with automation and metered "
                 "billing supporting them.")},
    ]},
    {"title": tr("Characteristics and limits"), "items": [
        {"q": tr("Is elasticity the same as unlimited capacity?"),
         "a": tr("No. Quotas, account limits and budget bound elasticity; a reached quota behaves like a full "
                 "server.")},
        {"q": tr("Why is colocation not cloud computing?"),
         "a": tr("The customer owns and manages the hardware, so there is no pooling, self-service or measured "
                 "compute.")},
        {"q": tr("What is multi-tenancy?"),
         "a": tr("Several customers share the same physical resources while the platform keeps their workloads "
                 "isolated.")},
        {"q": tr("Can a private cloud be cloud computing?"),
         "a": tr("Yes, if it provides the same self-service, pooling, elasticity and measured service inside one "
                 "organisation.")},
        {"q": tr("Name two supporting traits that are not among the five."),
         "a": tr("Multi-tenancy and resilience, together with automation and metered billing detail.")},
    ]},
    {"title": tr("Challenges and risks"), "items": [
        {"q": tr("Give three technical challenges of cloud computing."),
         "a": tr("Dependence on connectivity, latency and bandwidth limits, and migration or integration "
                 "complexity with legacy systems.")},
        {"q": tr("What is vendor lock-in?"),
         "a": tr("Dependence on a provider's proprietary services and APIs that makes moving the workload "
                 "expensive or impractical.")},
        {"q": tr("What does shared responsibility mean?"),
         "a": tr("The provider secures the infrastructure and platform; the customer secures data, identities, "
                 "configuration and application code.")},
        {"q": tr("Name four common cloud security risks."),
         "a": tr("Misconfiguration, compromised accounts, insecure APIs and data loss by deletion or failed "
                 "migration.")},
        {"q": tr("Why is a public storage bucket a customer problem, not a provider problem?"),
         "a": tr("Configuration and access policy belong to the customer; the provider's certification does not "
                 "make a public bucket compliant.")},
        {"q": tr("What is a data-residency requirement?"),
         "a": tr("A legal or policy rule that data must be stored or processed in a stated jurisdiction, which "
                 "fixes the region choice.")},
    ]},
    {"title": tr("Applications and cost"), "items": [
        {"q": tr("Why do colleges suit cloud hosting?"),
         "a": tr("Their load is spiky - result-day and admission peaks - so paying for peak capacity all year "
                 "would be wasteful.")},
        {"q": tr("Give one cloud application in agriculture and one in health."),
         "a": tr("Agriculture: weather and mandi advisories; health: telemedicine records and imaging archives.")},
        {"q": tr("How is cloud used in a green-hydrogen plant?"),
         "a": tr("Sensor telemetry is ingested and stored centrally, analysed for efficiency and predictive "
                 "maintenance, and shown on remote dashboards; safety control stays local.")},
        {"q": tr("What is a break-even calculation used for?"),
         "a": tr("It finds the number of months after which an owned server becomes cheaper than a recurring "
                 "cloud bill.")},
        {"q": tr("Why is egress often the surprising line on a cloud bill?"),
         "a": tr("Inbound traffic is usually free but outbound transfer is billed per GB, so popularity increases "
                 "cost directly.")},
        {"q": tr("When is cloud a poor choice?"),
         "a": tr("Hard real-time control, strict localisation, stable fully-used hardware, unreliable "
                 "connectivity, or an organisation unable to monitor a metered bill.")},
    ]},
]

# --------------------------------------------------------------------------- exam + practice
# (question, suggested marks, model answer). Marks are sizes for revision, not official allocations.
PRACTICE = [
    ("Define cloud computing and explain the five essential characteristics with one example each.", 7,
     h4("Definition (1 mark)")
     + p("Cloud computing is a model for enabling ubiquitous, convenient, on-demand network access to a shared "
         "pool of configurable computing resources - networks, servers, storage, applications and services - that "
         "can be rapidly provisioned and released with minimal management effort or provider interaction.")
     + h4("Characteristics (5 marks, 1 each)")
     + ul("<b>On-demand self-service:</b> a student starts a virtual machine from a portal at midnight without "
          "raising a ticket.",
          "<b>Broad network access:</b> the same notes portal opens on a phone, a lab PC and a tablet.",
          "<b>Resource pooling:</b> the new VM is placed on any free host in the region; the student never learns "
          "which one.",
          "<b>Rapid elasticity:</b> the result portal scales out on result day and releases the extra capacity "
          "the next morning.",
          "<b>Measured service:</b> the bill lists vCPU-hours, GB-months and egress GB for that VM.")
     + h4("Conclusion (1 mark)")
     + p("All five must be present; a service with four is hosted or virtualized, not cloud computing.")),
    ("Differentiate cloud computing from traditional on-premises computing (any four points).", 4,
     h4("Four differences (1 mark each)")
     + table(["Basis", "On-premises", "Cloud"],
             [("Hardware ownership", "College buys and owns it", "Provider owns it; customer rents capacity"),
              ("Provisioning time", "Weeks for budget, delivery and installation", "Minutes through a console or API"),
              ("Cost pattern", "Capital purchase plus maintenance", "Recurring usage-based bill"),
              ("Responsibility", "College patches host, hypervisor and application",
               "Provider patches the platform; customer patches the guest and the application")])
     + p("Mention any one consequence in a closing line: cloud shifts cost from capital to operating and shifts "
         "platform patching to the provider.")),
    ("Explain the central ideas behind cloud computing.", 4,
     h4("Six ideas with the manual practice each replaces")
     + ol("<b>Resource pooling</b> - one hardware pool serves many customers instead of one server per application.",
          "<b>Virtualization</b> - a hypervisor slices that hardware into isolated virtual machines instead of one "
          "operating system per machine.",
          "<b>Elasticity</b> - capacity follows the load instead of being bought for the yearly peak.",
          "<b>Self-service</b> - a portal or API provisions resources instead of a ticket queue.",
          "<b>Measured service</b> - usage is metered and billed instead of one flat annual bill.",
          "<b>Automation and orchestration</b> - templates and infrastructure as code replace manual rebuilds that "
          "nobody can reproduce.")
     + p("Close by distinguishing mechanism from outcome: these six produce the five characteristics.")),
    ("What is multi-tenancy? Why does it create both savings and risk?", 3,
     h4("Meaning (1 mark)")
     + p("Multi-tenancy means several customers share the same physical host, storage array or network, with "
         "isolation enforced by the virtualization layer and the provider's access controls.")
     + h4("Saving (1 mark)")
     + p("Hardware, power and cooling are used by many tenants, so the cost per tenant falls and small workloads "
         "become affordable.")
     + h4("Risk (1 mark)")
     + p("Isolation is now a security dependency: a hypervisor flaw or a misconfigured shared service can expose "
         "one tenant to another, and a noisy neighbour can consume shared capacity. The provider owns isolation; "
         "the customer still owns its own permissions and configuration.")),
    ("Explain any four challenges of cloud computing and one mitigation for each.", 7,
     h4("Four challenges (4 marks) and mitigations (3 marks)")
     + table(["Challenge", "Why it happens", "Mitigation"],
             [("Connectivity dependence", "The application sits beyond the campus link",
               "Redundant links and an offline fallback for critical pages"),
              ("Latency and egress", "Every call crosses a network boundary; outbound data is billed",
               "Choose the nearest region; compress; cache at the edge"),
              ("Vendor lock-in", "Proprietary APIs and managed services make exit costly",
               "Open formats, documented export, portable containers"),
              ("Cost control", "Elastic capacity can multiply spend without warning",
               "Budgets, alerts, tagging and a monthly review")])
     + p("Any four rows earn full credit; add one sentence that each mitigation reduces probability, impact or "
         "both.")),
    ("Describe the shared responsibility model for IaaS with a layer table.", 7,
     h4("The split (2 marks)")
     + p("The provider secures the cloud itself - facilities, hardware, network fabric and hypervisor. The "
         "customer secures what runs in the cloud - guest operating system, identities, data, configuration and "
         "application code.")
     + h4("Layer table (4 marks)")
     + table(["Layer", "Owner"],
             [("Building, power, cooling", "Provider"),
              ("Servers, storage, network fabric", "Provider"),
              ("Hypervisor and tenant isolation", "Provider"),
              ("Guest OS patches", "Customer"),
              ("Identity, keys, permissions", "Customer"),
              ("Data classification and encryption", "Customer")])
     + h4("Conclusion (1 mark)")
     + p("Compliance certificates cover the provider's rows only; a public bucket is still the customer's "
         "failure.")),
    ("List five cloud security risks and the control for each.", 4,
     h4("Five risks with controls")
     + ul("<b>Misconfiguration</b> - public bucket or open security group; control: secure templates and "
          "configuration scanning.",
          "<b>Account compromise</b> - no MFA, keys in code; control: MFA, short-lived roles, managed secrets.",
          "<b>Insecure API</b> - unencrypted or unauthenticated endpoints; control: TLS, authentication on every "
          "route, throttling.",
          "<b>Data breach</b> - stolen credential copies data out; control: least privilege, encryption, anomaly "
          "alerts.",
          "<b>Denial of service or cost exhaustion</b> - control: edge filtering, scaling limits and budget "
          "alerts.")
     + p("Add data loss (versioning and tested restore) as a sixth if the question allows five plus one.")),
    ("Explain three novel applications of cloud computing.", 4,
     h4("Any three, each with the reason")
     + ol("<b>Campus services:</b> LMS, result portal and virtual labs - the load is spiky and the budget is "
          "capital-poor, so pooled capacity is cheaper than peak hardware.",
          "<b>Healthcare:</b> telemedicine records and imaging archives - large images, many remote users, strict "
          "access control and audit.",
          "<b>Green-hydrogen analytics:</b> sensors stream to a cloud store; models flag drift and schedule "
          "maintenance, while dashboards show plant efficiency remotely. Safety control stays local.")
     + p("One line on privacy: each application handles personal data, so least privilege, encryption and a "
         "deletion policy are part of the answer.")),
    ("State four advantages and three disadvantages of cloud computing.", 4,
     h4("Advantages (2 marks)")
     + ul("No capital expenditure - monthly billing replaces a purchase.",
          "Elastic capacity - the result-day peak is absorbed and released.",
          "Global reach - regions place the app near users.",
          "Managed services - the team writes features instead of patching database hosts.")
     + h4("Disadvantages (2 marks)")
     + ul("Recurring cost - a stable long-running workload can cost more than owned hardware.",
          "Network dependency - the campus link becomes a single point of failure.",
          "Egress and lock-in - outbound data is billed and proprietary APIs raise exit cost.")
     + p("Close with the balance: cloud for spiky, new or distributed loads; owned hardware for stable, "
         "latency-critical or strictly local loads.")),
    ("A provider offers 99.9 % availability. Compute the allowed downtime per year and comment.", 3,
     h4("Given and formula")
     + p("Year = 365 x 24 x 60 = 525,600 minutes; allowed downtime = (1 - 0.999) x 525,600.")
     + h4("Calculation")
     + p("0.001 x 525,600 = <b>525.6 minutes = 8.76 hours per year</b>.")
     + h4("Comment")
     + p("That is roughly one working day. Each additional nine cuts the allowance by about ten, but requires "
         "redundancy, health checks and rehearsed failover - so the percentage should be quoted as minutes.")),
    ("A server costs 90,000 plus 3,000 per month; the cloud equivalent is 8,000 per month. Find the break-even "
     "and interpret it.", 4,
     h4("Given and formula")
     + p("Purchase = 90,000; monthly difference = 8,000 - 3,000 = 5,000; break-even = purchase / difference.")
     + h4("Calculation")
     + p("90,000 / 5,000 = <b>18 months</b>.")
     + h4("Interpretation")
     + p("If the server is used for less than 18 months, or sits idle for much of the year, the cloud is cheaper. "
         "Beyond 18 months of genuine use, ownership wins in this model - which ignores hardware refresh, staff "
         "time and failure risk, so state those assumptions.")),
    ("When should an organisation avoid moving a workload to the cloud?", 3,
     h4("Five conditions (any three for full marks)")
     + ul("<b>Hard real-time control</b> - a millisecond loop cannot wait for a network round trip.",
          "<b>Strict data localisation</b> - if no available region satisfies the rule, the data cannot leave.",
          "<b>Stable, fully used hardware</b> - an already busy server is cheap to keep running.",
          "<b>Unreliable connectivity</b> - a site with intermittent power and link cannot depend on a remote "
          "console.",
          "<b>No cost governance</b> - an organisation that cannot monitor a metered bill will overspend.")
     + p("Then recommend the middle path: keep control and sensitive data local and move analytics or archives "
         "to the cloud - a hybrid decision, which is the next unit.")),
]

ANSWERED = {"title": tr("8. Answered Practice (original questions, suggested marks)"), "items": [
    {"h": tr(f"Practice {i}. {q}"), "body": tr(a)} for i, (q, _m, a) in enumerate(PRACTICE, 1)
]}

EXAM = [{"q": tr("Practice: " + q), "marks": m} for q, m, _ in PRACTICE]

LESSON_COUNT = sum(len(s["items"]) for s in NOTES)
