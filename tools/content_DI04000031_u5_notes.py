"""Concise Unit 5: required topics only, as requested by the user."""
from nosql_content import make_T,table,tr,SX,V,Q

SOURCES=[
 ('GTU DI04000031 syllabus','https://s3-ap-southeast-1.amazonaws.com/gtusitecirculars/Syallbus/DI04000031.pdf'),
 ('Install Redis','https://redis.io/docs/latest/operate/oss_and_stack/install/'),
 ('Redis data types','https://redis.io/docs/latest/develop/data-types/'),
 ('Redis commands','https://redis.io/docs/latest/commands/'),
 ('Redis transactions','https://redis.io/docs/latest/develop/using-commands/transactions/'),
 ('Redis Python client','https://redis.io/docs/latest/develop/clients/redis-py/'),
 ('Expiry','https://redis.io/docs/latest/commands/expire/'),
 ('Redis security','https://redis.io/docs/latest/operate/oss_and_stack/management/security/'),
]
SN={
 'setup':"redis-cli --user YOUR_USER --askpass PING\n# Enter your private password; expected CLI reply: PONG",
 'strings':"SET lab:product 'Sensor Node'\nGET lab:product\nSET lab:views 10\nINCR lab:views\nTYPE lab:product\nEXISTS lab:product\nDEL lab:product",
 'list':"RPUSH lab:jobs train evaluate\nLPUSH lab:jobs load\nLRANGE lab:jobs 0 -1\nLPOP lab:jobs",
 'set':"SADD lab:skills Python Redis Python\nSMEMBERS lab:skills\nSISMEMBER lab:skills Python\nSREM lab:skills Redis",
 'hash':"HSET lab:user name Asha city Surat age 20\nHGET lab:user name\nHGETALL lab:user\nHDEL lab:user age",
 'transaction':"MULTI\nINCR lab:views\nGET lab:views\nEXEC\n# DISCARD cancels queued commands before execution.",
 'expiry':"SET lab:recs 'P101,P102' EX 60\nGET lab:recs\nTTL lab:recs\nDEL lab:recs   # invalidate after a source-data change",
 'cache':"GET cache-key\n# HIT: return the cached value.\n# MISS: read the authoritative source, then\nSET cache-key value EX 60",
}
T=make_T(SN)
NOTES=[{'title':tr('Redis — Required Topics in Brief'),'items':[
 T('5.1 Overview and installation','''<p><b>Redis</b> stores keys mapped to data structures, mainly served from memory. It is useful for caches, sessions, counters and simple queues. Persistence is configurable; do not assume a memory-first cache is a durable system of record.</p><p>Install using the official guide for your OS. Start a private, authenticated instance and connect with redis-cli. The usual port is <b>6379</b>; use your actual settings. Keep passwords out of shared code and never expose Redis directly to public browsers.</p>@@setup@@<p>This unit covers <b>10 hours / 17%</b>, <b>CO5</b> and <b>Practical 9</b>: install Redis and practise Strings, Lists, Sets and Hashes. CLI snippets use practice keys on your own instance; the downloadable Python examples isolate and clean their own keys.</p>''','ns5_types',programs=['ns5p01']),
 T('5.2 Strings and basic key operations','''<p>A <b>String</b> stores a byte/string value. Use SET/GET, INCR for an integer-formatted counter, EXISTS to test a key, TYPE to inspect its type and DEL to remove it. A missing GET returns nil/null; using the wrong structure command can raise WRONGTYPE.</p>@@strings@@<p>SET normally replaces the existing value. Redis hash field values and numeric-looking strings are not automatically Python numbers.</p>''',programs=['ns5p01','ns5p02']),
 T('5.3 Lists','''<p>A <b>List</b> is ordered and allows duplicates. LPUSH/RPUSH add at the left/right; LPOP/RPOP remove from those ends. LRANGE 0 -1 reads the whole list. RPUSH plus LPOP gives a basic FIFO pattern, not a complete reliable job-processing system.</p>@@list@@<p>Here the list is load, train, evaluate; LPOP removes load.</p>''',programs=['ns5p03']),
 T('5.4 Sets','''<p>A <b>Set</b> stores unique, unordered members. SADD adds, SMEMBERS reads, SISMEMBER tests membership and SREM removes. Adding Python twice does not create two members.</p>@@set@@<p>Suitable examples: unique skills, tags or visitor IDs. Display order is not guaranteed; the Python example sorts only for readable output.</p>''',programs=['ns5p04']),
 T('5.5 Hashes','''<p>A <b>Hash</b> stores field–value pairs under one key, for example a small user/profile record. HSET writes fields, HGET reads one, HGETALL reads all and HDEL removes fields.</p>@@hash@@<p>The age value is stored/read as string "20" in these examples. Use a list for ordered items, a set for unique members and a hash for named fields.</p>''',programs=['ns5p05']),
 T('5.6 Transactions','''<p><b>MULTI</b> queues commands; <b>EXEC</b> executes them together without another client’s command interleaving during execution. <b>DISCARD</b> cancels the queued work before execution.</p>@@transaction@@<p><b>No rollback:</b> an execution-time error does not undo successful commands, and later queued commands can still run. Program 6 demonstrates this with a non-integer INCR and a later successful write. The Python transaction pipeline uses MULTI/EXEC.</p>''','ns5_transaction',programs=['ns5p06']),
 T('5.7 Caching, expiry and invalidation','''<p>A <b>cache hit</b> finds the value; a <b>miss</b> requires the source. In <b>cache-aside</b>, the application reads Redis first, then loads and caches the source value on a miss.</p>@@expiry@@<ul><li><b>TTL:</b> limits lifetime. TTL returns seconds; -1 means no expiry and -2 means missing.</li><li><b>Invalidation:</b> delete/update cached data when the authoritative value changes.</li><li><b>Other strategies:</b> write-through updates cache with source writes; write-behind delays source writes and needs careful failure handling.</li></ul><p>Expiry is not memory-pressure eviction. Caches may be stale or unavailable; keep a source fallback and do not claim unlimited memory, durability or guaranteed speedups.</p>''','ns5_cache',programs=['ns5p02','ns5p07']),
 T('5.8 AI use cases and simplified application integration','''<p>Redis can cache <b>recommendation IDs</b>, temporary feature values or sessions, and hold simple job lists. Storing these values does <b>not train an AI model</b>.</p><p><b>Integration:</b> application → Redis; on a miss → source database/service → Redis with TTL → response. Use an official client such as Python redis-py. Version cache keys when the model/data meaning changes and protect personal data.</p>@@cache@@<p>Program 8 really connects Python to Redis and shows source → cache → invalidation. Its source is a small <b>local dictionary fixture</b>, not a live MongoDB/Cassandra integration or benchmark. The reference uses Redis/CLI <b>8.10.3</b> and redis-py <b>8.1.0</b>, privately on port 6385.</p>''','ns5_integration',programs=['ns5p07','ns5p08']),
]}]
SYNTAX=[{'title':tr('Quick Command Reference'),'items':[
 SX('Connect / keys',SN['setup']+'\nEXISTS lab:key\nTYPE lab:key\nDEL lab:key','Private connection; use your actual host/port/user. Never use FLUSHDB/FLUSHALL to clean a shared lab.'),
 SX('Strings',SN['strings'],'GET returns a string/nil; INCR requires an integer-formatted value.'),
 SX('Lists',SN['list'],'Ordered items, duplicates allowed; LRANGE end index is inclusive and -1 is the last item.'),
 SX('Sets',SN['set'],'Unique members; no guaranteed member order.'),
 SX('Hashes',SN['hash'],'One key, named string field–value pairs.'),
 SX('Transactions',SN['transaction'],'Commands queue before EXEC; execution-time failures do not roll back other successful commands.'),
 SX('Expiry / invalidation',SN['expiry'],'SET EX sets lifetime in seconds. TTL -1: no expiry; -2: missing. Delete/update stale entries.'),
 SX('Cache-aside integration',SN['cache'],'Conceptual flow. Program 8 executes Python + Redis with a local source fixture; not a live multi-database deployment.'),
]}]
VIVA=[{'title':tr('Short Viva'),'items':[
 V('What is Redis?', 'A memory-first data-structure server commonly used for caching, sessions, counters and simple queues.'),
 V('Which four structures are required here?', 'Strings, Lists, Sets and Hashes.'),
 V('Which commands store and read a string?', 'SET and GET. A missing GET returns nil/null.'),
 V('List versus Set?', 'A list is ordered and permits duplicates; a set holds unique members without guaranteed order.'),
 V('What is a Redis hash?', 'Field–value pairs under one key, read/written with HGET/HSET and related commands.'),
 V('What does INCR require?', 'A missing key or a value representing an integer; a non-integer stored string causes an error.'),
 V('What do MULTI, EXEC and DISCARD do?', 'Queue commands, execute the queue, or cancel it before execution respectively.'),
 V('Does a Redis transaction roll back runtime errors?', 'No. Successful commands are not undone and later queued commands can still execute.'),
 V('What do TTL -1 and -2 mean?', '-1: existing key without expiry. -2: missing key.'),
 V('What is cache-aside?', 'Read cache first; on a miss read the authoritative source and cache the result with a suitable lifetime.'),
 V('Why invalidate a cache?', 'To prevent serving an outdated value after the authoritative source changes.'),
 V('Does this unit train AI or prove a live multi-database integration?', 'No. AI caching is an application use case; the executed integration is Python + Redis with a local dictionary source.'),
]}]
PRACTICE_QS=[
 Q('practical','Install/connect and verify one stored round-trip.','Use your OS guide, private authentication and redis-cli PING. SET a disposable string, GET the same value, then DEL only that key.'),
 Q('practical','Choose and practise the four structures.','String: product name/counter. List: ordered jobs. Set: unique skills. Hash: named user fields. Use the corresponding quick-reference commands.'),
 Q('practical','Execute a small transaction and explain failure behaviour.','Use MULTI/EXEC (or the Python transaction pipeline). Program 6 returns [11,"11"]; a later example’s failed INCR does not prevent its subsequent SET. DISCARD cancels before execution.'),
 Q('practical','Add expiry and invalidate a cached recommendation.','SET the result with EX 60, confirm TTL is active, read it as a hit, then DEL it on source change. TTL -2 confirms it is missing.'),
 Q('practical','Demonstrate simple application integration.','Run program 8: first read comes from the local source fixture; second from Redis. Update the fixture, invalidate, and read the new value. Record actual outputs; no trained model or live multi-database claim.'),
]
assert sum(len(g['items']) for g in NOTES)==8
assert sum(len(g['items']) for g in SYNTAX)==8
assert sum(len(g['items']) for g in VIVA)==12
assert len(PRACTICE_QS)==5
