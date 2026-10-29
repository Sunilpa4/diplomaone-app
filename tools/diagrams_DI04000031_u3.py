"""Thirteen small-screen Cassandra concept diagrams; plain self-contained SVG.
Multiple-node architecture is conceptual; the tested runtime has one node.
"""
import os
from flowchart_lib import svg, text, arr, rbox, line, P, INK
from subject_DI04000031 import DIAG_DIR
from diagrams_DI04000031_u1 import (heading, lines, frame, foot, BLUE, BF,
    GREEN, GF, ORANGE, OF, TEAL, TF, RED, RF, GREY, PF)

TITLES = {
    'ns3_arch': 'Peer Nodes and a Per-Request Coordinator',
    'ns3_setup': 'Installation, Private Access and Connection Evidence',
    'ns3_hierarchy': 'Keyspace, Table, Partition, Row and Column',
    'ns3_keys': 'Composite Partition Keys versus Clustering Columns',
    'ns3_partitions': 'Eight Readings in Four Logical Partitions',
    'ns3_query': 'A Selected Partition and Bounded Time Query',
    'ns3_upsert': 'INSERT and UPDATE Have Default Upsert Semantics',
    'ns3_delete': 'Cell, Row and Partition Deletion Scopes',
    'ns3_model': 'Two Query Tables and an Explicit Correction',
    'ns3_filter': 'Rejected Filtering versus a Deliberate Access Path',
    'ns3_csv': 'CSV Import Must Preserve Full Keys and UTC Times',
    'ns3_features': 'Small Per-Partition Analytical Features',
    'ns3_health': 'Read-Only nodetool Awareness and UN Interpretation',
}


def arch():
    b = heading('Cassandra peer architecture', 'Multi-node picture is conceptual, not this lab')
    b += rbox(180, 88, 324, 44, 'Client / cqlsh / application driver', BF, BLUE, 12)
    b += arr([(180, 110), (180, 145)], BLUE)
    b += rbox(180, 179, 190, 68, 'Node A\ncoordinates this request', PF, P, 12, 'bold', P)
    b += arr([(128, 213), (86, 263)], P)
    b += arr([(232, 213), (274, 263)], P)
    b += rbox(91, 298, 144, 70, 'Peer node B\nowned data ranges', GF, GREEN, 11.5)
    b += rbox(269, 298, 144, 70, 'Peer node C\nowned data ranges', GF, GREEN, 11.5)
    b += arr([(164, 302), (194, 302)], GREEN)
    b += frame(18, 363, 324, 81, OF, ORANGE)
    b += lines(180, 385, ['Another peer can coordinate another request.', 'Replica copies depend on keyspace policy.', 'There is no mandatory global write-primary.'], 11, 21)
    b += foot(470, ['Actual reference: one physical node, RF 1.', 'No multi-node availability test is claimed.'])
    return svg(360, 510, b)


def setup():
    b = heading('Install, connect, prove storage', 'Practical 4: use your actual platform/version')
    labels = ['Supported Java + matching Cassandra/cqlsh',
              'Verify official download, then extract/install',
              'Private interfaces + authorized lab account',
              'Connect; SHOW VERSION; stored round-trip',
              'Record versions and owned scratch cleanup']
    for i, label in enumerate(labels):
        y = 83 + i * 68
        if i: b += arr([(180, y - 46), (180, y - 22)], P)
        b += rbox(180, y, 324, 44, label, BF if i % 2 == 0 else PF,
                  BLUE if i % 2 == 0 else P, 11)
    b += foot(410, ['Tested: Cassandra 5.0.9 / cqlsh 6.2.0', 'Java 17.0.21 / Debian 13 x86_64', 'Small lab sizing is not a production template.'])
    return svg(360, 466, b)


def hierarchy():
    b = heading('Cassandra data hierarchy', 'A partition is a logical data unit, not a node')
    cards = [(88, 'Keyspace: disposable lab namespace', BF, BLUE),
             (160, 'Table: readings_by_device_day', PF, P),
             (232, 'Partition: (S01, 2026-10-29)', GF, GREEN),
             (304, 'Row: reading_at 09:01 UTC', OF, ORANGE)]
    for i, (y, label, fill, stroke) in enumerate(cards):
        if i: b += arr([(180, y - 48), (180, y - 24)], P)
        b += rbox(180, y, 324, 48, label, fill, stroke, 11.5, 'bold', stroke)
    b += arr([(180, 328), (180, 357)], ORANGE)
    b += frame(18, 357, 324, 67, BF, BLUE)
    b += lines(180, 381, ['Typed regular columns:', 'temperature_c = 31.0; status = ok'], 12, 22)
    b += foot(450, ['Keyspace options include replication policy.', 'Many partitions can reside on one physical node.'])
    return svg(360, 490, b)


def keys():
    b = heading('Keys decide the layout', 'Short names device/day/ts used in this figure')
    for y, clause, detail, sample, fill, stroke in [
        (68, 'PRIMARY KEY (device, day, ts)', ['Partition key: device', 'Clustering: day, then ts'],
         'S01 across days: same partition', BF, BLUE),
        (248, 'PRIMARY KEY ((device, day), ts)', ['Partition key: device + day', 'Clustering: ts'],
         'S01 on a new day: another partition', GF, GREEN)]:
        b += frame(18, y, 324, 155, fill, stroke)
        b += text(180, y + 25, clause, 11.5, color=stroke, weight='bold')
        b += line(f'M34 {y + 39} H326', stroke, 1)
        b += lines(180, y + 64, detail, 12, 24)
        b += text(180, y + 132, sample, 11)
    b += foot(433, ['Full schema uses device_id, day, reading_at.', 'The complete primary key identifies a row.', 'Bucketing must fit the actual rate and size.'])
    return svg(360, 489, b)


def partitions():
    b = heading('Four logical partitions', 'Eight synthetic rows; default time order is DESC')
    groups = [(18, 68, 'S01 / 29 Oct', ['09:02 -> 32.0', '09:01 -> 31.0', '09:00 -> 30.0'], BF, BLUE),
              (190, 68, 'S02 / 29 Oct', ['09:01 -> 29.0', '09:00 -> 28.0'], GF, GREEN),
              (18, 252, 'S01 / 30 Oct', ['09:01 -> 34.0', '09:00 -> 33.0'], PF, P),
              (190, 252, 'S03 / 29 Oct', ['09:00 -> 27.0'], OF, ORANGE)]
    for x, y, title, data, fill, stroke in groups:
        b += frame(x, y, 152, 157, fill, stroke)
        b += text(x + 76, y + 24, title, 12, color=stroke, weight='bold')
        b += line(f'M{x + 12} {y + 39} H{x + 140}', stroke, 1)
        b += lines(x + 76, y + 62, data, 11.5, 23)
        b += text(x + 76, y + 138, str(len(data)) + ' row(s)', 11, color=stroke)
    b += foot(438, ['3 + 2 + 2 + 1 = 8; times are UTC.', 'All four logical partitions are on one node here.', 'Partition count is not server or replica count.'])
    return svg(360, 493, b)


def query():
    b = heading('A bounded partition query', 'Logical intent, not a physical optimizer plan')
    cards = [(86, 'WHERE device S01 + day 29 Oct', BF, BLUE),
             (162, 'Time interval: [09:00, 09:02) UTC', PF, P),
             (238, 'Clustering order: reading_at DESC', GF, GREEN),
             (314, 'LIMIT 2: at most two returned rows', OF, ORANGE)]
    for i, (y, label, fill, stroke) in enumerate(cards):
        if i: b += arr([(180, y - 53), (180, y - 23)], P)
        b += rbox(180, y, 324, 46, label, fill, stroke, 11.5)
    b += arr([(180, 337), (180, 369)], ORANGE)
    b += rbox(180, 401, 324, 64, '09:01 -> 31.0\n09:00 -> 30.0', GF, GREEN, 12)
    b += foot(459, ['09:02 is excluded by the upper boundary.', 'ORDER BY is not a free sort on any column.'])
    return svg(360, 500, b)


def upsert():
    b = heading('Normal writes are upserts', 'Same complete key means the same logical row')
    b += frame(18, 67, 324, 157, BF, BLUE)
    b += text(180, 93, 'INSERT using existing learner_id = 1', 12, color=BLUE, weight='bold')
    b += lines(180, 123, ['name: Asha -> Asha Patel', 'Existing city Surat and marks 82 remain.', 'Only supplied regular values are written.'], 11.5, 25)
    b += frame(18, 248, 324, 157, GF, GREEN)
    b += text(180, 274, 'UPDATE missing learner_id = 99', 12, color=GREEN, weight='bold')
    b += lines(180, 304, ['Creates a row: name Jai, marks 68', 'city is null in this new row.', 'Normal UPDATE does not require prior existence.'], 11, 25)
    b += foot(437, ['No normal duplicate-key error for this INSERT.', 'No MongoDB-style matched/modified count.', 'Conditional writes have separate semantics/costs.'])
    return svg(360, 494, b)


def delete():
    b = heading('Deletion scope follows the key', 'Use the disposable lab, never system data')
    cards = [(67, 'CELL: DELETE city', ['Asha still has name and marks 82.', 'Only the selected city value is removed.'], BF, BLUE),
             (183, 'ROW: full row identity', ['learner_id 2 -> no returned row', 'device + day + time -> one sensor reading'], PF, P),
             (299, 'PARTITION: device + day', ['S02 / 29 Oct -> all its readings removed', 'Missing time is deliberate partition scope.'], OF, ORANGE)]
    for y, label, detail, fill, stroke in cards:
        b += frame(18, y, 324, 95, fill, stroke)
        b += text(180, y + 24, label, 12, color=stroke, weight='bold')
        b += lines(180, y + 51, detail, 11, 21)
    b += foot(426, ['Logical deletion uses tombstones.', 'No immediate physical-erasure proof or undo.', 'Cleanup targets only the newly owned keyspace.'])
    return svg(360, 482, b)


def model():
    b = heading('Query-first tables have a cost', 'Two read paths, deliberately duplicated records')
    b += frame(18, 68, 152, 128, BF, BLUE)
    b += frame(190, 68, 152, 128, GF, GREEN)
    b += lines(94, 92, ['Device/day table', '(S01, 29 Oct)', '09:02 -> 32.0', 'Read device history'], 11.5, 25)
    b += lines(266, 92, ['Status/day table', '(high, 29 Oct)', 'S01 09:02 -> 32.0', 'Read high-status data'], 11, 25)
    b += arr([(94, 196), (94, 237)], BLUE)
    b += arr([(266, 196), (266, 237)], GREEN)
    b += rbox(94, 267, 152, 60, 'Base corrected\n35.0', BF, BLUE, 12, 'bold', BLUE)
    b += rbox(266, 267, 152, 60, 'Copy still old\n32.0', RF, RED, 12, 'bold', RED)
    b += arr([(266, 297), (266, 329), (180, 329), (180, 354)], P)
    b += rbox(180, 385, 324, 62, 'Explicit second write -> copy 35.0\nNo automatic cross-table correction', PF, P, 11.5)
    b += foot(447, ['No join/foreign-key/cascade is being enforced.', 'The two writes are not one automatic transaction.'])
    return svg(360, 489, b)


def filtering():
    b = heading('A filter is an access decision', 'Tiny output does not prove tiny query work')
    b += frame(18, 67, 324, 112, RF, RED)
    b += lines(180, 92, ['Unindexed temperature_c > 30', 'No designed partition-key access', 'Adding LIMIT 1 does not legalize it.', 'Observed server response: InvalidRequest'], 11.5, 22)
    b += frame(18, 207, 324, 112, OF, ORANGE)
    b += lines(180, 233, ['Teaching-only bounded filter', 'Select S01 + 29 Oct: three known rows.', 'ALLOW FILTERING permits residual scanning.', 'Returns 32.0 and 31.0 in this fixture.'], 11.5, 22)
    b += frame(18, 347, 324, 85, GF, GREEN)
    b += lines(180, 372, ['For a real repeated access requirement:', 'design a query-shaped table or choose', 'a suitable index deliberately.'], 11.5, 22)
    b += foot(461, ['ALLOW FILTERING is not an index or speed promise.'])
    return svg(360, 486, b)


def csv_import():
    b = heading('Import full keys, not just rows', 'Practical 6: actual cqlsh COPY FROM')
    cards = [(86, 'sensors.csv: eight synthetic records', BF, BLUE),
             (164, 'Map columns + HEADER + explicit time format', PF, P),
             (242, 'cqlsh COPY FROM: eight rows processed', GF, GREEN)]
    for i, (y, label, fill, stroke) in enumerate(cards):
        if i: b += arr([(180, y - 55), (180, y - 23)], P)
        b += rbox(180, y, 324, 46, label, fill, stroke, 11)
    b += arr([(180, 265), (180, 301)], GREEN)
    b += frame(18, 301, 324, 115, OF, ORANGE)
    b += lines(180, 325, ['Verify with real server reads:', '8 stored rows / 4 logical device-day keys', 'Correct UTC times, including 09:02 -> 32.0', 'Repeated full keys can collapse into upserts.'], 11, 23)
    b += foot(445, ['DATETIMEFORMAT uses %z for the UTC Z suffix.', 'A processed-row message alone is not enough.', 'Fixed snapshot, not live ingestion or a benchmark.'])
    return svg(360, 502, b)


def features():
    b = heading('Small partition-level features', 'S01 / 29 October — synthetic readings')
    b += rbox(180, 90, 324, 53, '30.0 + 31.0 + 32.0', BF, BLUE, 16, 'bold', BLUE)
    b += arr([(180, 117), (180, 157)], P)
    b += frame(18, 157, 324, 193, GF, GREEN)
    values = [('count(*)', '3'), ('sum', '93.0'), ('avg', '31.0'), ('min / max', '30.0 / 32.0')]
    for i, (label, value) in enumerate(values):
        b += text(42, 192 + i * 42, label, 13, 'start', GREEN, 'bold')
        b += text(232, 192 + i * 42, value, 13, 'start')
    b += arr([(180, 350), (180, 386)], GREEN)
    b += rbox(180, 418, 324, 64, 'Inputs for a report or a later model\nNot a trained anomaly detector', PF, P, 12)
    b += foot(478, ['Bound the partition; plan large analytics separately.'])
    return svg(360, 502, b)


def health():
    b = heading('Read-only health awareness', 'nodetool status uses management/JMX, not CQL')
    b += rbox(180, 88, 324, 46, 'Observed reference: one local UN node', GF, GREEN, 12, 'bold', GREEN)
    b += frame(18, 160, 152, 147, BF, BLUE)
    b += frame(190, 160, 152, 147, PF, P)
    b += lines(94, 186, ['STATUS', 'U = Up', 'D = Down'], 12, 31, BLUE)
    b += lines(266, 182, ['STATE', 'N = Normal', 'J = Joining', 'L = Leaving', 'M = Moving'], 11.5, 24, P)
    b += frame(18, 337, 324, 102, OF, ORANGE)
    b += lines(180, 361, ['UN is a useful observation, not a full guarantee.', 'Check authorized application reads/writes too.', 'Keep CQL, internode and JMX access private.', 'No repair/decommission/failure-injection lab.'], 11, 22)
    b += foot(470, ['Load, node UUID and ownership vary.', 'No replicated-cluster availability proof is claimed.'])
    return svg(360, 512, b)

BUILDERS = [arch, setup, hierarchy, keys, partitions, query, upsert, delete,
            model, filtering, csv_import, features, health]


def main():
    for id_, build in zip(TITLES, BUILDERS):
        with open(os.path.join(DIAG_DIR, id_ + '.svg'), 'w', encoding='utf-8') as file:
            file.write(build())
    assert len(BUILDERS) == len(TITLES) == 13
    print('Cassandra Unit 3 diagrams:', len(TITLES))


if __name__ == '__main__': main()
