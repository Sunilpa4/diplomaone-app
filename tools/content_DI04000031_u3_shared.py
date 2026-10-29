"""Pure synthetic Cassandra fixtures; no network/database imports.

Eight sensor readings in four logical device/day partitions, not live hardware
or evidence of placement across multiple physical nodes. Explicit UTC samples.
"""
import csv
import io

CSV = '''device_id,day,reading_at,temperature_c,status
S01,2026-10-29,2026-10-29T09:00:00Z,30.0,ok
S01,2026-10-29,2026-10-29T09:01:00Z,31.0,ok
S01,2026-10-29,2026-10-29T09:02:00Z,32.0,high
S02,2026-10-29,2026-10-29T09:00:00Z,28.0,ok
S02,2026-10-29,2026-10-29T09:01:00Z,29.0,ok
S01,2026-10-30,2026-10-30T09:00:00Z,33.0,high
S01,2026-10-30,2026-10-30T09:01:00Z,34.0,high
S03,2026-10-29,2026-10-29T09:00:00Z,27.0,ok
'''
READINGS = list(csv.DictReader(io.StringIO(CSV)))
for row in READINGS: row['temperature_c'] = float(row['temperature_c'])
SENSOR_DDL = '''CREATE TABLE readings_by_device_day (
  device_id text, day date, reading_at timestamp,
  temperature_c double, status text,
  PRIMARY KEY ((device_id, day), reading_at)
) WITH CLUSTERING ORDER BY (reading_at DESC);
'''


def quoted(value): return "'" + str(value).replace("'", "''") + "'"


SENSOR_SEED = SENSOR_DDL
for row in READINGS:
    SENSOR_SEED += ('INSERT INTO readings_by_device_day\n'
        '  (device_id, day, reading_at, temperature_c, status)\n'
        'VALUES (' + ', '.join(quoted(row[k]) for k in ('device_id', 'day', 'reading_at'))
        + ',\n        ' + str(row['temperature_c']) + ', ' + quoted(row['status']) + ');\n')

STUDENT_DDL = '''CREATE TABLE learners_by_id (
  learner_id int PRIMARY KEY, name text, city text, marks int
);
'''
STUDENT_SEED = STUDENT_DDL + '''INSERT INTO learners_by_id (learner_id, name, city, marks)
VALUES (1, 'Asha', 'Surat', 82);
INSERT INTO learners_by_id (learner_id, name, city, marks)
VALUES (2, 'Ravi', 'Bharuch', 70);
INSERT INTO learners_by_id (learner_id, name, city, marks)
VALUES (3, 'Neha', 'Surat', 92);
'''


def expected_readings():
    """CSV rows normalized exactly like genuine CQL result display values."""
    from datetime import datetime
    result = []
    for original in READINGS:
        row = dict(original)
        row['reading_at'] = datetime.fromisoformat(row['reading_at']).isoformat(timespec='milliseconds').replace('+00:00', 'Z')
        result.append(row)
    return result
