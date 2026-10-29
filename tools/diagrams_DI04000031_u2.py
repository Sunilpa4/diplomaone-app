"""Thirteen mobile-first MongoDB diagrams; plain SVG for Flutter and HTML.
Runtime examples are real; replica-set and shard diagrams are conceptual.
"""
import os
from flowchart_lib import svg, text, arr, rbox, line, P, INK
from subject_DI04000031 import DIAG_DIR
from diagrams_DI04000031_u1 import (heading, lines, frame, foot, BLUE, BF,
    GREEN, GF, ORANGE, OF, TEAL, TF, RED, RF, GREY, PF)

TITLES = {
    'ns2_arch': 'Client, mongosh, mongod and Storage',
    'ns2_hierarchy': 'Database, Collection, Document and Field',
    'ns2_bson': 'BSON Types and Identifier Type Matching',
    'ns2_setup': 'Installation and Connection Evidence',
    'ns2_crud': 'The Four CRUD Operations',
    'ns2_filters': 'Filtering the Six-Student Fixture',
    'ns2_query': 'Sort, Limit and Projection',
    'ns2_update': 'Matched versus Modified Updates',
    'ns2_model': 'Embedded Data versus References',
    'ns2_index': 'Explain Counters with Forced Plans',
    'ns2_pipeline': 'Aggregation from Six Orders to Two Groups',
    'ns2_replica': 'Replication: Copies of the Same Dataset',
    'ns2_shard': 'Sharding: Different Subsets and Routing',
}


def stack():
    b = heading('MongoDB in the stack', 'A client is not the database server')
    cards = [(89, 'Application code / user', BF, BLUE),
             (174, 'Driver or mongosh client', PF, P),
             (259, 'mongod: query + update + indexes', GF, GREEN),
             (344, 'BSON collections + storage', OF, ORANGE)]
    for i, (y, label, fill, stroke) in enumerate(cards):
        if i: b += arr([(180, y - 61), (180, y - 26)], P)
        b += rbox(180, y, 324, 52, label, fill, stroke, 12, 'bold', stroke)
    b += foot(398, ['mongosh sends commands; mongod manages data.', 'The lesson is not a publicly hosted application.'])
    return svg(360, 438, b)


def hierarchy():
    b = heading('MongoDB data hierarchy', 'A document contains named field/value pairs')
    cards = [(90, 'Database: unit2 scratch', BF, BLUE),
             (176, 'Collection: students', PF, P),
             (262, 'Document: student _id = 1', GF, GREEN)]
    for i, (y, label, fill, stroke) in enumerate(cards):
        if i: b += arr([(180, y - 61), (180, y - 25)], P)
        b += rbox(180, y, 324, 50, label, fill, stroke, 12, 'bold', stroke)
    b += arr([(180, 287), (180, 317)], GREEN)
    b += frame(18, 317, 324, 86, OF, ORANGE)
    b += lines(34, 341, ['name: Asha', 'skills: [MongoDB, Python]', 'address: {city: Surat}'], 12, 20, anchor='start')
    b += foot(429, ['Selection alone does not persist an empty DB.'])
    return svg(360, 453, b)


def bson():
    b = heading('BSON is typed binary data', 'Not just JSON text or JavaScript typeof')
    data = [('_id', 'ObjectId'), ('name', 'String'), ('age', 'Int32'),
            ('skills', 'Array'), ('address', 'Embedded document'),
            ('active', 'Boolean'), ('joined', 'Date'), ('score', 'Double')]
    b += frame(18, 66, 324, 277, BF, BLUE)
    b += text(34, 88, 'FIELD', 11, 'start', BLUE, 'bold')
    b += text(160, 88, 'BSON TYPE', 11, 'start', BLUE, 'bold')
    b += line('M34 102 H326', BLUE, 1)
    for i, (field, kind) in enumerate(data):
        b += text(34, 122 + i * 27, field, 12, 'start')
        b += text(160, 122 + i * 27, kind, 12, 'start')
    b += frame(18, 365, 324, 65, OF, ORANGE)
    b += lines(180, 387, ['ObjectId(hex) is not the same as a string.', 'Use the stored identifier type in a filter.'], 11.5, 20)
    return svg(360, 450, b)


def setup():
    b = heading('Install, connect, verify', 'Practical 2: collect actual evidence')
    labels = ['Select a supported OS + architecture', 'Install Community Server and mongosh',
              'Start a private server; configure access', 'Connect, ping, create, write and read',
              'Record server and shell versions']
    for i, label in enumerate(labels):
        y = 82 + i * 69
        if i: b += arr([(180, y - 48), (180, y - 22)], P)
        b += rbox(180, y, 324, 44, label, BF if i % 2 == 0 else PF,
                  BLUE if i % 2 == 0 else P, 11.5)
    b += foot(412, ['Reference: Debian 13 x86_64', 'Server 9.0.4 / mongosh 2.14.0', 'These are tested versions, not a latest-version claim.'])
    return svg(360, 467, b)


def crud():
    b = heading('CRUD targets documents', 'Choose a filter before changing data')
    cards = [('C', 'Create', 'insertOne / insertMany', BF, BLUE),
             ('R', 'Read', 'find / findOne', GF, GREEN),
             ('U', 'Update', 'updateOne / updateMany', PF, P),
             ('D', 'Delete', 'deleteOne / deleteMany', OF, ORANGE)]
    for i, (letter, name, method, fill, stroke) in enumerate(cards):
        y = 65 + i * 86
        b += frame(18, y, 324, 70, fill, stroke)
        b += text(42, y + 35, letter, 25, color=stroke, weight='bold')
        b += text(74, y + 22, name, 12, 'start', stroke, 'bold')
        b += text(74, y + 47, method, 12, 'start')
    b += foot(429, ['Single-document writes are atomic.', 'A batch is not automatically one transaction.'])
    return svg(360, 467, b)


def filters():
    b = heading('A filter selects documents', 'Example: marks strictly greater than 80')
    b += frame(18, 65, 324, 235, BF, BLUE)
    xs = [34, 74, 153, 267]
    for x, label in zip(xs, ['ID', 'NAME', 'CITY', 'MARKS']):
        b += text(x, 88, label, 10.5, 'start', BLUE, 'bold')
    b += line('M34 102 H326', BLUE, 1)
    rows = [('1', 'Asha', 'Surat', '82'), ('2', 'Ravi', 'Bharuch', '70'),
            ('3', 'Neha', 'Surat', '92'), ('4', 'Imran', 'Vadodara', '65'),
            ('5', 'Meera', 'Surat', '82'), ('6', 'Dev', 'Ahmedabad', '50')]
    for i, row in enumerate(rows):
        y = 122 + i * 29
        for x, value in zip(xs, row):
            b += text(x, y, value, 11, 'start', GREEN if i in (0, 2, 4) else INK,
                      'bold' if i in (0, 2, 4) else 'normal')
    b += arr([(180, 300), (180, 331)], P)
    b += rbox(180, 354, 324, 46, '{marks: {$gt: 80}} -> IDs [1, 3, 5]', GF, GREEN, 12, 'bold', GREEN)
    b += foot(403, ['$gt excludes the boundary; $in tests membership.', '$and needs all clauses; $or needs at least one.'])
    return svg(360, 442, b)


def query():
    b = heading('Logical result shaping', 'Not a fixed physical optimizer execution order')
    labels = ['find({}) -> six matched students', 'sort: marks descending, _id ascending',
              'limit(3) -> first three in that order', 'projection -> name + marks; hide _id']
    for i, label in enumerate(labels):
        y = 83 + i * 68
        if i: b += arr([(180, y - 46), (180, y - 22)], P)
        b += rbox(180, y, 324, 44, label, BF if i % 2 == 0 else PF,
                  BLUE if i % 2 == 0 else P, 11.5)
    b += frame(18, 339, 324, 85, GF, GREEN)
    b += lines(180, 360, ['Neha 92', 'Asha 82', 'Meera 82'], 12, 23)
    b += foot(450, ['The _id tie-breaker fixes the 82-mark ordering.'])
    return svg(360, 474, b)


def update():
    b = heading('Matched is not modified', 'The server reports both counts')
    b += rbox(180, 90, 324, 49, 'Before: Ravi / Bharuch / 70', BF, BLUE, 12, 'bold', BLUE)
    b += arr([(180, 115), (180, 149)], P)
    b += frame(18, 149, 324, 71, PF, P)
    b += lines(180, 172, ['filter _id:2; $set city:Surat; $inc marks:5', 'After: Ravi / Surat / 75'], 11.5, 23)
    b += frame(18, 244, 324, 140, GF, GREEN)
    b += text(34, 267, 'CASE', 11, 'start', GREEN, 'bold')
    b += text(209, 267, 'MATCH / MODIFY', 11, 'start', GREEN, 'bold')
    b += line('M34 280 H326', GREEN, 1)
    for y, label, counts in [(300, 'Real change', '1 / 1'), (332, 'Set 75 again', '1 / 0'), (364, 'Missing _id:999', '0 / 0')]:
        b += text(34, y, label, 12, 'start'); b += text(259, y, counts, 12)
    b += foot(413, ['updateMany is not one transaction across all matches.'])
    return svg(360, 438, b)


def model():
    b = heading('Embed or reference?', 'Decide from access, size and ownership')
    b += frame(18, 65, 324, 132, BF, BLUE)
    b += text(34, 88, 'EMBED: bounded address with the learner', 11.5, 'start', BLUE, 'bold')
    b += lines(34, 116, ['Learner L1', '  name: Asha', '  address: {city: Surat, pin: 395001}', 'Read the bounded record together.'], 11.5, 20, anchor='start')
    b += frame(18, 220, 324, 143, GF, GREEN)
    b += text(34, 244, 'REFERENCE: a separately managed course', 11.5, 'start', GREEN, 'bold')
    b += rbox(94, 294, 127, 57, 'Learner L1\ncourseId: C1', '#FFFFFF', GREEN, 11)
    b += arr([(158, 294), (202, 294)], GREEN)
    b += rbox(272, 294, 127, 57, 'Course C1\nMongoDB Basics', '#FFFFFF', GREEN, 10.5)
    b += text(180, 344, 'Explicit lookup; a missing reference is possible.', 10.5)
    b += foot(392, ['No automatic relational foreign-key enforcement.', 'Avoid unbounded embedded event/comment histories.'])
    return svg(360, 431, b)


def index():
    b = heading('Explain counters, not a timer', 'Same query / same three matching documents')
    b += rbox(180, 87, 324, 46, 'city = Surat and marks > 80', BF, BLUE, 12, 'bold', BLUE)
    b += arr([(180, 110), (180, 130), (94, 130), (94, 152)], P)
    b += arr([(180, 130), (266, 130), (266, 152)], P)
    b += frame(18, 152, 152, 129, OF, ORANGE)
    b += frame(190, 152, 152, 129, GF, GREEN)
    b += lines(94, 176, ['Forced scan', 'hint: $natural', 'Returned: 3', 'Docs examined: 6'], 11, 25)
    b += lines(266, 176, ['Forced index', 'hint: city_marks', 'Returned: 3', 'Docs examined: 3'], 11, 25)
    b += frame(18, 306, 324, 97, PF, P)
    b += lines(180, 328, ['Index: {city: 1, marks: -1}', 'Index keys examined in this run: 3', 'Unique email index -> duplicate error 11000', 'Indexes also cost storage and write work.'], 11, 22)
    b += foot(430, ['Hints make the tiny comparison controlled.', 'No guaranteed wall-clock speedup is claimed.'])
    return svg(360, 470, b)


def pipeline():
    b = heading('Aggregation pipeline', 'The input and output counts can differ')
    for i, (label, color, fill) in enumerate([
        ('Six order documents', BLUE, BF),
        ('$match status:paid -> five documents', P, PF),
        ('$group by $category -> two summaries', GREEN, GF),
    ]):
        y = 82 + i * 71
        if i: b += arr([(180, y - 48), (180, y - 23)], P)
        b += rbox(180, y, 324, 46, label, fill, color, 11.5)
    b += frame(18, 278, 324, 101, OF, ORANGE)
    xs = [34, 137, 202, 279]
    for x, label in zip(xs, ['CATEGORY', 'COUNT', 'TOTAL', 'AVG']):
        b += text(x, 300, label, 10, 'start', ORANGE, 'bold')
    b += line('M34 311 H326', ORANGE, 1)
    for y, row in [(333, ['book', '3', '600', '200']), (361, ['tool', '2', '1000', '500'])]:
        for x, value in zip(xs, row): b += text(x, y, value, 12, 'start')
    b += foot(405, ['$sum:1 counts; $sum:$amount adds values.', '$avg computes the mean; source orders remain six.'])
    return svg(360, 447, b)


def replica():
    b = heading('Replication = same dataset', 'Conceptual only — not configured in this unit')
    b += rbox(180, 88, 324, 46, 'Client writes to the primary', BF, BLUE, 12)
    b += arr([(180, 111), (180, 145)], P)
    b += rbox(180, 179, 188, 68, 'Primary\nData A + B + C', PF, P, 12)
    b += arr([(130, 213), (88, 249)], P)
    b += arr([(230, 213), (272, 249)], P)
    b += text(180, 239, 'asynchronous updates', 10.5, color=GREY)
    b += rbox(91, 284, 146, 70, 'Secondary 1\nData A + B + C', GF, GREEN, 11.5)
    b += rbox(269, 284, 146, 70, 'Secondary 2\nData A + B + C', GF, GREEN, 11.5)
    b += frame(18, 345, 324, 74, OF, ORANGE)
    b += lines(180, 367, ['An eligible member may become the new primary.', 'Elections can interrupt service; lag can exist.', 'Replication is not an independent backup.'], 11, 19)
    b += foot(445, ['No replica-set setup or failover test is claimed.'])
    return svg(360, 469, b)


def shard():
    b = heading('Sharding = different subsets', 'Conceptual routing, not a configured cluster')
    b += rbox(180, 85, 324, 44, 'Client application', BF, BLUE, 12)
    b += arr([(180, 107), (180, 137)], P)
    b += rbox(180, 161, 214, 48, 'mongos query router', PF, P, 12, 'bold', P)
    b += arr([(130, 185), (90, 235)], P)
    b += arr([(230, 185), (270, 235)], P)
    b += rbox(91, 275, 146, 80, 'Shard A\nSubset: 1, 2, 3\nReplica set', GF, GREEN, 11.5)
    b += rbox(269, 275, 146, 80, 'Shard B\nSubset: 4, 5, 6\nReplica set', GF, GREEN, 11.5)
    b += rbox(180, 367, 324, 48, 'Config-server metadata supports routing', OF, ORANGE, 11.5)
    b += foot(416, ['A shard key influences placement and routing.', 'Hot keys and broad queries can add cost.', 'No sharding setup or benchmark is claimed.'])
    return svg(360, 471, b)


BUILDERS = {'ns2_arch': stack, 'ns2_hierarchy': hierarchy, 'ns2_bson': bson,
    'ns2_setup': setup, 'ns2_crud': crud, 'ns2_filters': filters,
    'ns2_query': query, 'ns2_update': update, 'ns2_model': model,
    'ns2_index': index, 'ns2_pipeline': pipeline,
    'ns2_replica': replica, 'ns2_shard': shard}


def main():
    os.makedirs(DIAG_DIR, exist_ok=True)
    for id_, draw in BUILDERS.items():
        with open(os.path.join(DIAG_DIR, id_ + '.svg'), 'w', encoding='utf-8') as f:
            f.write(draw())
    print('MongoDB Unit 2 diagrams:', len(BUILDERS))


if __name__ == '__main__': main()
