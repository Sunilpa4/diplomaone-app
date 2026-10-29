# DI04000031 — Source and scope record

Checked: **29 October 2026**. The current release covers **Unit 1 only**.

## Authoritative curriculum

- [GTU official DI04000031 PDF](https://s3-ap-southeast-1.amazonaws.com/gtusitecirculars/Syallbus/DI04000031.pdf), effective 2025–26; local transcription `tools/syllabus_DI04000031.txt`.
- Computer/CSE, semester 4; practical subject; 3 credits; L0/T1/PR4.
- Theory ESE 0, theory PA 0, practical PA 20, practical ESE 30: total 50.
- Units: Introduction 8h/13%; MongoDB 18h/30%; Cassandra 12h/20%; Neo4j 12h/20%; Redis 10h/17%. Total 60h/100%.
- Unit 1: why NoSQL and RDBMS trade-offs; CAP basics with analogy only; four models; AI uses. CO1 selects and justifies a model.
- Practical 1 is **comparative study**, not installation of all four engines. MongoDB setup starts in Practical 2.
- Later scope limits: MongoDB replication/sharding conceptual; Cassandra health awareness; graph recommendation/fraud algorithm examples, not implementations.

## Technical references used for Unit 1

1. [Gilbert and Lynch — Brewer's Conjecture and the Feasibility of Consistent, Available, Partition-Tolerant Web Services](https://users.ece.cmu.edu/~adrian/731-sp04/readings/GL-cap.pdf). CAP C is linearizability, distinct from ACID C. Availability is eventual operation completion, not a fixed latency promise. The theorem concerns partition executions; no proof is taught here.
2. [MongoDB — Data Modeling](https://www.mongodb.com/docs/manual/data-modeling/). Flexible documents, nested fields, validation and access-pattern design. BSON is not simply JSON text.
3. [Apache Cassandra — Introduction to Data Modeling](https://cassandra.apache.org/doc/latest/cassandra/developing/data-modeling/intro.html). Query-driven typed tables, partition/clustering keys, denormalization and no relational joins. This does not imply a columnar analytical warehouse.
4. [Neo4j — Graph Database Concepts](https://neo4j.com/docs/getting-started/appendix/graphdb-concepts/). Nodes, labels, directed typed relationships, properties and paths.
5. [Redis — Data Types](https://redis.io/docs/latest/develop/data-types/). Redis supports multiple data structures rather than only plain string values. Unit 5 retains the syllabus's basic strings/lists/sets/hashes scope.

## Evidence boundaries

- Document records, key/value entries, sensor partitions and graph paths are **illustrative teaching fixtures**.
- Tests check valid JSON, field/key consistency, the illustrated shared-interest candidate, source/diagram integrity, safe HTML, preview JavaScript and the workbook. These are **not database engine runs** or performance measurements.
- No named-company deployment claims, latest-version claims or fabricated benchmark numbers.
- The course is practical-only. The unit has no official-theory-paper tab, no allocated per-question marks, and 16 answered revision tasks in Notes.
- The workbook contains worked comparison/selection/CAP sheets and a blank editable journal. A defensible alternative model is allowed when the workload reasoning supports it.

## Deliverables

- `content/computer/sem4/DI04000031/subject.json` and `unit1.json`
- Ten self-contained SVG diagrams in the subject's `diagrams/` directory
- `preview/DI04000031_unit1_preview.html`
- `preview/DI04000031_unit1_practical1_worksheet.xlsx`

Rebuild: `python3 tools/build_DI04000031_u1.py`.
Validate: `python3 tools/test_DI04000031_u1.py`.
Release only after the established exact-commit app-render CI succeeds.
