"""Seven compact mobile SVGs for Cloud Computing Unit 1.

360 px wide, white background, no <marker>/<style>/<image>/href, text kept inside the canvas.
Fonts are declared as Arial (export rewrites the family to DejaVu Sans, the app's bundled font).
"""
from flowchart_lib import svg, text, arr, rbox, P

BLUE, BF = "#1565C0", "#EAF3FD"
GREEN, GF = "#2E7D32", "#EAF6EC"
ORANGE, OF = "#B66A00", "#FFF4DF"
RED, RF = "#BD2543", "#FDECF0"
PF = "#F2EBFA"

TITLES = {
    "cc1_terms": "Cloud, computing and cloud computing",
    "cc1_central": "Six central ideas behind cloud computing",
    "cc1_characteristics": "Five essential characteristics",
    "cc1_challenges": "Challenges by category",
    "cc1_hydrogen": "Green-hydrogen analytics in the cloud",
    "cc1_shared": "Shared responsibility split",
    "cc1_advdis": "Advantages and disadvantages",
}


def heading(title, sub=None):
    body = text(180, 24, title, 14, weight="bold", color=P)
    if sub:
        body += text(180, 46, sub, 10.5, color="#666")
    return body


def foot(y, *lines):
    return "".join(text(180, y + 16 * i, s, 10.2, color="#666") for i, s in enumerate(lines))


def row(y, name, detail, fill=PF, color=P, h=58, size=12):
    return (f'<rect x="18" y="{y}" width="324" height="{h}" rx="8" fill="{fill}" '
            f'stroke="{color}" stroke-width="1.6"/>'
            + text(180, y + h / 2 - 7, name, size, weight="bold", color=color)
            + text(180, y + h / 2 + 10, detail, 10.7))


def terms():
    b = heading("Three words, one service", "The cloud is a delivery model, not the Internet")
    b += rbox(180, 96, 324, 60, "CLOUD\nRemote resources in a provider data centre", BF, BLUE, 11.6)
    b += arr([(180, 126), (180, 160)], P)
    b += rbox(180, 190, 324, 60, "COMPUTING\nProcessing, storage and network", PF, P, 11.6)
    b += arr([(180, 220), (180, 254)], P)
    b += rbox(180, 284, 324, 60, "CLOUD COMPUTING\nOn demand, pooled, elastic, metered", GF, GREEN, 11.4)
    b += foot(360, "Shared pool + network access + rapid provisioning.")
    return svg(360, 392, b)


def central():
    b = heading("Six ideas that carry the model", "Remove one and the economics collapses")
    data = [
        ("1. Resource pooling", "One hardware pool serves many customers", BF, BLUE),
        ("2. Virtualization", "A hypervisor slices host into isolated VMs", PF, P),
        ("3. Elasticity", "Capacity follows load, up and down", GF, GREEN),
        ("4. Self-service", "Portal or API provisions, not a ticket", OF, ORANGE),
        ("5. Measured service", "Usage metered, reported and billed", BF, BLUE),
        ("6. Automation", "Templates and infrastructure as code", PF, P),
    ]
    for i, (n, d, f, c) in enumerate(data):
        b += row(66 + 68 * i, n, d, f, c, 58)
    b += foot(482, "These are mechanisms; the characteristics are their outcome.")
    return svg(360, 508, b)


def characteristics():
    b = heading("A service needs all five", "Four out of five is hosting, not cloud")
    data = [
        ("On-demand self-service", "Provisioned without talking to a human", BF, BLUE),
        ("Broad network access", "Standard clients: phone, laptop, lab PC", PF, P),
        ("Resource pooling", "Shared pool, physical location hidden", GF, GREEN),
        ("Rapid elasticity", "Scales out for a spike, then releases", OF, ORANGE),
        ("Measured service", "Metered in vCPU-hours, GB-months, egress", BF, BLUE),
    ]
    for i, (n, d, f, c) in enumerate(data):
        b += row(66 + 84 * i, n, d, f, c, 72)
    b += foot(496, "Elastic is not unlimited: quota and budget bound it.")
    return svg(360, 524, b)


def challenges():
    b = heading("Every benefit has a bill", "Group the challenges before answering")
    data = [
        ("Technical", "Link, latency, migration, legacy integration", BF, BLUE),
        ("Performance", "Noisy neighbour, burst credits, variance", PF, P),
        ("Money", "Egress, idle resources, unbudgeted elasticity", OF, ORANGE),
        ("Legal and people", "Residency, compliance, skills, lock-in", RF, RED),
    ]
    for i, (n, d, f, c) in enumerate(data):
        b += row(64 + 96 * i, n, d, f, c, 84, 12.5)
    b += foot(462, "Diagnose in layers: link, DNS, identity, quota, app.")
    return svg(360, 492, b)


def hydrogen():
    b = heading("From stack sensor to dashboard", "Safety control stays local; analytics moves up")
    data = [
        ("1. Sensors and gateway", "Current, temperature, pressure, purity", BF, BLUE),
        ("2. Cloud ingest endpoint", "Fixed interval, authenticated upload", PF, P),
        ("3. Store", "Raw object storage + time-series index", GF, GREEN),
        ("4. Analyse and predict", "Drift, efficiency, maintenance model", OF, ORANGE),
        ("5. Dashboards", "Plant, fleet and savings on a phone", BF, BLUE),
    ]
    tops = []
    for i, (n, d, f, c) in enumerate(data):
        top = 66 + 80 * i
        tops.append(top)
        b += rbox(180, top + 28, 324, 56, n + "\n" + d, f, c, 11.2)
    for i in range(1, len(tops)):            # arrows after the boxes, so no arrowhead is covered
        b += arr([(180, tops[i - 1] + 58), (180, tops[i] - 5)], P)
    b += foot(74 + 80 * 5, "A trip loop cannot wait for a round trip.",
              "Region choice is a legal decision, not only latency.")
    return svg(360, 110 + 80 * 5, b)


def shared():
    b = heading("Two halves of one contract", "The certificate covers only the left half")
    b += rbox(95, 96, 150, 56, "PROVIDER\nsecures the cloud OF", BF, BLUE, 10.6)
    b += rbox(265, 96, 150, 56, "CUSTOMER\nsecures what is IN", PF, P, 10.6)
    left = ["Facility and power", "Servers and disks", "Network fabric", "Hypervisor isolation"]
    right = ["Guest OS patches", "Identities and keys", "Data and backups", "App configuration"]
    for i, (l, r) in enumerate(zip(left, right)):
        y = 166 + 56 * i
        b += rbox(95, y, 150, 46, l, BF, BLUE, 10.2)
        b += rbox(265, y, 150, 46, r, PF, P, 10.2)
    b += f'<rect x="18" y="{166 + 56 * 4 - 8}" width="324" height="42" rx="8" fill="{OF}" stroke="{ORANGE}" stroke-width="1.6"/>'
    b += text(180, 166 + 56 * 4 + 13, "Most incidents land on the right-hand side", 10.8, weight="bold", color=ORANGE)
    b += foot(166 + 56 * 4 + 48, "A public bucket is the customer's failure, not the provider's.")
    return svg(360, 166 + 56 * 4 + 76, b)


def advdis():
    b = heading("The same properties, both ways", "Elasticity is a benefit and a cost risk")
    b += rbox(95, 88, 150, 48, "ADVANTAGES", GF, GREEN, 11, weight="bold")
    b += rbox(265, 88, 150, 48, "DISADVANTAGES", RF, RED, 11, weight="bold")
    left = ["No capital spend", "Elastic capacity", "Global regions", "Managed services", "Fast experiments"]
    right = ["Recurring bill", "Link dependency", "Egress charges", "Vendor lock-in", "Limited control"]
    for i, (l, r) in enumerate(zip(left, right)):
        y = 154 + 52 * i
        b += rbox(95, y, 150, 42, l, GF, GREEN, 10.4)
        b += rbox(265, y, 150, 42, r, RF, RED, 10.4)
    b += foot(154 + 52 * 5 + 6, "Choose by workload: spiky and new → cloud;", "stable, local, real-time → owned hardware.")
    return svg(360, 154 + 52 * 5 + 54, b)


def main():
    from subject_DI04000041 import DIAG_DIR
    DIAG_DIR.mkdir(parents=True, exist_ok=True)
    for name, draw in zip(TITLES, [terms, central, characteristics, challenges, hydrogen, shared, advdis]):
        (DIAG_DIR / f"{name}.svg").write_text(draw(), encoding="utf-8")
    print(f"Cloud Computing Unit 1 diagrams: {len(TITLES)}")


if __name__ == "__main__":
    main()
