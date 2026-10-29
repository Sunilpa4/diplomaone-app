"""Ten small-screen NoSQL concept diagrams. Plain self-contained SVG.

No marker/CSS/external fonts/images: compatible with flutter_svg.
All records/paths are illustrative, not database engine screenshots.
"""
import os
from flowchart_lib import svg, text, arr, rbox, line, P, INK
from subject_DI04000031 import DIAG_DIR

BLUE = '#1565C0'; BF = '#EAF3FE'
GREEN = '#2E7D32'; GF = '#EDF7EE'
ORANGE = '#AA5C00'; OF = '#FFF4DF'
TEAL = '#00695C'; TF = '#E7F5F2'
RED = '#B3261E'; RF = '#FDECEA'
GREY = '#625B71'; PF = '#F3ECFB'

TITLES = {
    'ns1_workload': 'Choose a Model from the Workload',
    'ns1_scale': 'Scaling, Data Partitions and Replicas',
    'ns1_cap': 'CAP Basics During a Network Partition',
    'ns1_booking': 'CAP Analogy: One Seat, Two Offices',
    'ns1_document': 'Document Model: Different Product Attributes',
    'ns1_key_value': 'Key-Value Model: Known-Key Recommendation Cache',
    'ns1_wide_column': 'Wide-Column Model: Sensor/Day Partitions',
    'ns1_graph': 'Graph Model: A Shared-Interest Path',
    'ns1_ai_fit': 'AI Data Roles and Model Fit',
    'ns1_polyglot': 'Polyglot Persistence with Clear Ownership',
}


def heading(label, sub=None):
    b = text(180, 22, label, 15, weight='bold', color=P)
    if sub: b += text(180, 45, sub, 10.5, color=GREY)
    return b


def lines(cx, y, labels, size=11.5, gap=17, color=INK, anchor='middle', weight='normal'):
    return ''.join(text(cx, y + i * gap, label, size, color=color,
                        anchor=anchor, weight=weight) for i, label in enumerate(labels))


def frame(x, y, w, h, fill=PF, stroke=P, rx=9):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" stroke="{stroke}" stroke-width="1.4"/>'


def foot(y, labels):
    return lines(180, y, labels, 10.5, 16, GREY)


def workload():
    b = heading('Match the workload', 'NoSQL is an option, not a universal upgrade')
    b += rbox(180, 91, 324, 52, 'Shape + reads/writes + guarantees', BF, BLUE, 12, 'bold', BLUE)
    b += arr([(180, 117), (180, 137), (94, 137), (94, 155)], BLUE)
    b += arr([(180, 137), (266, 137), (266, 155)], P)
    b += frame(18, 155, 152, 139, GF, GREEN)
    b += frame(190, 155, 152, 139, PF, P)
    b += lines(94, 178, ['Relational', 'Tables and relations', 'SQL, constraints', 'Transactions', 'Often a strong default'], 11.5, 22)
    b += lines(266, 178, ['NoSQL models', 'Documents or keys', 'Wide-column or graph', 'Match access patterns', 'Check actual guarantees'], 11.5, 22)
    b += arr([(94, 294), (94, 316), (180, 316), (180, 334)], GREEN)
    b += arr([(266, 294), (266, 316), (180, 316)], P)
    b += rbox(180, 357, 324, 46, 'Simplest suitable design + a trade-off', OF, ORANGE, 11.5, 'bold', ORANGE)
    b += foot(399, ['Measure actual behaviour; do not promise a speedup.'])
    return svg(360, 420, b)


def scale():
    b = heading('Scaling and data placement', 'Different purposes; a system may combine them')
    b += frame(18, 65, 324, 99, BF, BLUE)
    b += text(34, 85, 'SCALE UP: more resources on one server', 11.5, 'start', BLUE, 'bold')
    b += rbox(96, 119, 109, 34, 'One server', '#FFFFFF', BLUE, 11)
    b += arr([(152, 119), (193, 119)], BLUE)
    b += rbox(263, 119, 136, 45, 'Bigger server', '#FFFFFF', BLUE, 11)
    b += frame(18, 181, 324, 99, PF, P)
    b += text(34, 201, 'SCALE OUT: add nodes / distribute work', 11.5, 'start', P, 'bold')
    for x, label in [(76, 'Subset A'), (180, 'Subset B'), (284, 'Subset C')]:
        b += rbox(x, 239, 91, 41, label, '#FFFFFF', P, 11)
    b += frame(18, 297, 324, 99, GF, GREEN)
    b += text(34, 317, 'REPLICATE: copies of the same data', 11.5, 'start', GREEN, 'bold')
    b += rbox(99, 356, 126, 40, 'A + B + C', '#FFFFFF', GREEN, 12)
    b += arr([(163, 356), (195, 356)], GREEN)
    b += rbox(263, 356, 126, 40, 'A + B + C', '#FFFFFF', GREEN, 12)
    b += foot(421, ['Data partitioning is not a network partition.'])
    return svg(360, 445, b)


def cap():
    b = heading('CAP: basic guarantees', 'Consider affected operations during a partition')
    cards = [
        (66, 'C', 'Consistency', ['One current logical copy', 'Read after completed write:', 'not the older value'], BF, BLUE),
        (170, 'A', 'Availability', ['Valid operations eventually complete', 'at non-failed nodes', 'A refusal/error alone is not enough'], GF, GREEN),
        (274, 'P', 'Partition tolerance', ['Account for communication failure', 'between node groups', 'Nodes can still be running'], OF, ORANGE),
    ]
    for y, letter, label, ls, fill, stroke in cards:
        b += frame(18, y, 324, 91, fill, stroke)
        b += text(37, y + 24, letter, 23, color=stroke, weight='bold')
        b += text(63, y + 22, label, 12, 'start', stroke, 'bold')
        b += lines(63, y + 43, ls, 10.5, 16, anchor='start')
    b += rbox(180, 403, 324, 48, 'Partition: cannot guarantee both C and A', PF, P, 11.5, 'bold', P)
    b += foot(445, ['Healthy communication can support both C and A.'])
    return svg(360, 468, b)


def booking():
    b = heading('One last seat, two offices', 'Analogy only — not a theorem proof')
    b += rbox(91, 94, 144, 59, 'Surat\nlocal view: 1 seat', BF, BLUE, 11.5)
    b += rbox(269, 94, 144, 59, 'Bharuch\nlocal view: 1 seat', BF, BLUE, 11.5)
    b += line('M164 94 H178 M186 94 H196', RED, 2)
    b += line('M176 84 L186 104 M186 84 L176 104', RED, 2)
    b += text(180, 141, 'Communication link fails', 11, color=RED, weight='bold')
    b += frame(18, 166, 324, 126, GF, GREEN)
    b += text(34, 188, 'CONSISTENCY FIRST (CP-style)', 12, 'start', GREEN, 'bold')
    b += lines(34, 212, ['Confirm only if the authoritative history', 'can be maintained. An isolated office', 'defers a booking it cannot safely verify.', 'Some operations lose availability.'], 11.5, 18, anchor='start')
    b += frame(18, 309, 324, 126, OF, ORANGE)
    b += text(34, 331, 'AVAILABILITY FIRST (AP-style)', 12, 'start', ORANGE, 'bold')
    b += lines(34, 355, ['Both sides may act on a local seat count.', 'Two confirmations can claim one seat.', 'Reconcile later; earlier answers were', 'not one consistent booking history.'], 11.5, 18, anchor='start')
    b += foot(463, ['A stale recommendation is less harmful than', 'conflicting confirmations of a scarce seat.'])
    return svg(360, 501, b)


def document():
    b = heading('Document model', 'Illustrative products in one collection')
    b += frame(18, 67, 324, 147, BF, BLUE)
    b += text(34, 89, 'Document P101: Sensor Node', 12, 'start', BLUE, 'bold')
    b += lines(34, 115, ['_id: P101', 'category: electronics', 'attributes:', '    sample_rate_hz: 10', '    battery_powered: true'], 11.5, 18, anchor='start')
    b += frame(18, 231, 324, 147, GF, GREEN)
    b += text(34, 253, 'Document P102: NoSQL Guide', 12, 'start', GREEN, 'bold')
    b += lines(34, 279, ['_id: P102', 'category: book', 'attributes:', '    pages: 320', '    language: en'], 11.5, 18, anchor='start')
    b += foot(403, ['Varying fields still need deliberate validation.', 'JSON-like illustration; MongoDB stores BSON.'])
    return svg(360, 441, b)


def key_value():
    b = heading('Key-value model', 'A known user + model-version key')
    b += text(34, 80, 'KEY', 11, 'start', BLUE, 'bold')
    b += rbox(180, 113, 324, 46, 'recs:U42:v1', BF, BLUE, 14, 'bold', BLUE)
    b += arr([(180, 136), (180, 174)], P)
    b += text(34, 165, 'VALUE', 11, 'start', P, 'bold')
    b += rbox(180, 202, 324, 55, '[ P101, P102 ]', PF, P, 14, 'bold', P)
    b += frame(18, 252, 324, 77, GF, GREEN)
    b += lines(180, 275, ['Expiry policy: 300 seconds', 'Cache miss: fetch source or recompute', 'TTL is not a correctness guarantee'], 11.5, 19)
    b += foot(355, ['Illustrative layout, not a Redis CLI transcript.'])
    return svg(360, 378, b)


def sensor_table(y, sensor, rows, fill, stroke):
    b = frame(18, y, 324, 58 + 27 * len(rows), fill, stroke)
    b += text(34, y + 21, 'Partition: (' + sensor + ', 2026-10-29)', 11.5, 'start', stroke, 'bold')
    b += text(50, y + 46, 'ts', 11, 'start', stroke, 'bold')
    b += text(178, y + 46, 'reading_c', 11, 'start', stroke, 'bold')
    b += line(f'M34 {y + 56} H326', stroke, 1)
    for i, (ts, value) in enumerate(rows):
        b += text(50, y + 73 + i * 27, ts, 12, 'start')
        b += text(178, y + 73 + i * 27, value, 12, 'start')
    return b


def wide_column():
    b = heading('Wide-column model', 'Query: one sensor/day + bounded time interval')
    b += sensor_table(67, 'S01', [('09:00', '30.5'), ('09:01', '31.0')], BF, BLUE)
    b += sensor_table(218, 'S02', [('09:00', '29.0')], GF, GREEN)
    b += frame(18, 332, 324, 75, PF, P)
    b += lines(180, 353, ['Partition key groups the rows.', 'Timestamp orders rows inside a partition.', 'Cassandra CQL uses typed columns.'], 11.5, 19)
    b += foot(433, ['Illustrative table, not Cassandra query output.'])
    return svg(360, 456, b)


def node(x, y, labels, fill, stroke, radius=40):
    return f'<circle cx="{x}" cy="{y}" r="{radius}" fill="{fill}" stroke="{stroke}" stroke-width="1.7"/>' + lines(x, y - 7, labels, 10.5, 16)


def graph():
    b = heading('Graph model', 'Entities + directed, typed relationships')
    b += arr([(75, 134), (75, 204)], BLUE)
    b += arr([(255, 124), (107, 217)], P)
    b += arr([(285, 134), (285, 204)], TEAL)
    b += text(50, 170, 'LIKES', 10.5, color=BLUE, weight='bold')
    b += text(195, 172, 'LIKES', 10.5, color=P, weight='bold')
    b += text(310, 170, 'LIKES', 10.5, color=TEAL, weight='bold')
    b += node(75, 93, ['Person: U42', 'Ravi'], BF, BLUE)
    b += node(285, 93, ['Person: U77', 'Asha'], BF, BLUE)
    b += node(75, 246, ['P101', 'Sensor Node'], GF, GREEN, 42)
    b += node(285, 246, ['P102', 'NoSQL Guide'], GF, GREEN, 42)
    b += frame(18, 320, 324, 77, PF, P)
    b += lines(180, 342, ['Ravi and Asha share an interest in P101.', 'Asha also likes P102: a candidate for Ravi.', 'A heuristic, not a trained AI model.'], 11, 19)
    b += foot(424, ['Illustrative path, not an executed Neo4j result.'])
    return svg(360, 447, b)


def ai_fit():
    b = heading('AI data role -> model fit', 'Choose from the data and access pattern')
    cards = [
        ('Document', 'Evolving user / learner profiles', 'Bounded nested fields + validation', BF, BLUE),
        ('Key-Value', 'Known-key prediction / result cache', 'Versioned keys + expiry + miss fallback', GF, GREEN),
        ('Wide-Column', 'Large sensor / interaction history', 'Query-first time-bucketed partitions', OF, ORANGE),
        ('Graph', 'Connected fraud / recommendation patterns', 'Bounded paths; review false positives', TF, TEAL),
    ]
    for i, (name, a, c, fill, stroke) in enumerate(cards):
        y = 65 + 91 * i
        b += frame(18, y, 324, 77, fill, stroke)
        b += text(34, y + 20, name, 12.5, 'start', stroke, 'bold')
        b += lines(34, y + 42, [a, c], 11, 17, anchor='start')
    b += foot(447, ['Storage supports AI; training and inference are separate.'])
    return svg(360, 470, b)


def polyglot():
    b = heading('Polyglot persistence', 'An optional design — one database may be enough')
    b += rbox(180, 91, 324, 49, 'Shop application', BF, BLUE, 14, 'bold', BLUE)
    b += line('M180 116 V142 M66 142 H294', P, 1.8)
    for x in (66, 180, 294): b += arr([(x, 142), (x, 177)], P)
    panels = [(66, 'Relational', 'Orders /', 'payments', GF, GREEN),
              (180, 'Document', 'Product', 'catalog', PF, P),
              (294, 'Key-Value', 'Cached', 'recs', OF, ORANGE)]
    for x, label, a, c, fill, stroke in panels:
        b += frame(x - 51, 177, 102, 111, fill, stroke)
        b += text(x, 198, label, 11, color=stroke, weight='bold')
        b += lines(x, 224, [a, c], 11, 18)
        b += text(x, 270, 'authority' if x == 66 else 'own boundary', 9.5, color=stroke)
    b += frame(18, 316, 324, 102, TF, TEAL)
    b += text(180, 338, 'Declare ownership and synchronization', 11.5, color=TEAL, weight='bold')
    b += lines(180, 363, ['Payment source of truth: relational ledger', 'A cache must not confirm a payment.', 'More stores mean more operational work.'], 11, 19)
    b += foot(446, ['Add a store only for a justified workload benefit.'])
    return svg(360, 469, b)


BUILDERS = {
    'ns1_workload': workload, 'ns1_scale': scale, 'ns1_cap': cap,
    'ns1_booking': booking, 'ns1_document': document,
    'ns1_key_value': key_value, 'ns1_wide_column': wide_column,
    'ns1_graph': graph, 'ns1_ai_fit': ai_fit, 'ns1_polyglot': polyglot,
}


def main():
    os.makedirs(DIAG_DIR, exist_ok=True)
    for id_, draw in BUILDERS.items():
        path = os.path.join(DIAG_DIR, id_ + '.svg')
        with open(path, 'w', encoding='utf-8') as f: f.write(draw())
    print('NoSQL Unit 1 diagrams:', len(BUILDERS))


if __name__ == '__main__': main()
