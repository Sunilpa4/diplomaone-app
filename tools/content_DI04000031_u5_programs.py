"""Eight short examples; importing executes each against the REAL Redis server."""
from redis_content import P

PROGRAMS=[
 P('ns5p01','Connect and Use Basic Keys','''
with Lab('ns5p01',['product']) as lab:
    r=lab.r; k=lab.key('product')
    show('ping',r.ping())
    show('set',r.set(k,'Sensor Node'))
    show('get',r.get(k))
    show('exists',r.exists(k))
    show('type',r.type(k))
    show('deleted',r.delete(k))
    show('missing',r.get(k))
''','<p>Real stored round-trip. redis-py reports PING/SET success as true; redis-cli shows PONG/OK. Lab isolates and cleans declared keys.</p>'),
 P('ns5p02','String Counter and Expiry','''
with Lab('ns5p02',['views','temporary']) as lab:
    r=lab.r; k=lab.key('views'); temp=lab.key('temporary')
    r.set(k,'10')
    show('incremented',r.incr(k))
    show('stored_string',r.get(k))
    r.set(temp,'cached',ex=60)
    show('ttl_active',0<r.ttl(temp)<=60)
    r.expire(temp,0)
    show('after_immediate_expiry',r.get(temp))
    show('missing_ttl',r.ttl(temp))
''','<p>INCR returns integer 11; GET reads string "11". SET EX adds a lifetime; EXPIRE 0 immediately expires the key. TTL -2 means missing.</p>'),
 P('ns5p03','Ordered List Operations','''
with Lab('ns5p03',['jobs']) as lab:
    r=lab.r; k=lab.key('jobs')
    r.rpush(k,'train','evaluate'); r.lpush(k,'load')
    show('jobs',r.lrange(k,0,-1))
    show('removed_left',r.lpop(k))
    show('remaining',r.lrange(k,0,-1))
    show('length',r.llen(k))
''','<p>Lists preserve order. These are job-name strings, not executed AI training or a reliable-worker implementation.</p>'),
 P('ns5p04','Unique Set Members','''
with Lab('ns5p04',['skills']) as lab:
    r=lab.r; k=lab.key('skills')
    show('added',r.sadd(k,'Python','Redis','Python'))
    show('members',sorted(r.smembers(k)))
    show('has_python',r.sismember(k,'Python'))
    show('removed',r.srem(k,'Redis'))
    show('remaining',sorted(r.smembers(k)))
''','<p>Duplicate Python is stored once. Sorting is only for readable output; Redis set order is not guaranteed.</p>'),
 P('ns5p05','Hash Fields','''
with Lab('ns5p05',['user']) as lab:
    r=lab.r; k=lab.key('user')
    show('new_fields',r.hset(k,mapping={
        'name':'Asha','city':'Surat','age':'20'}))
    show('name',r.hget(k,'name'))
    show('profile',r.hgetall(k))
    show('removed_age',r.hdel(k,'age'))
    show('remaining',r.hgetall(k))
''','<p>A hash keeps named string fields under one key. The helper sorts map fields for stable display; it does not change stored values.</p>'),
 P('ns5p06','Transactions and the No-Rollback Rule','''
with Lab('ns5p06',['count','after']) as lab:
    r=lab.r; k=lab.key('count'); after=lab.key('after')
    r.set(k,'10')
    with r.pipeline(transaction=True) as p:
        p.incr(k); p.get(k)
        show('exec',p.execute())
    r.set(k,'text')
    with r.pipeline(transaction=True) as p:
        p.incr(k); p.set(after,'done')
        show('exec_with_error',p.execute(raise_on_error=False))
    show('later_write',r.get(after))
''','<p>The transaction pipeline uses MULTI/EXEC. A real non-integer INCR error does not stop the later SET; Redis does not roll back successful commands.</p>'),
 P('ns5p07','Recommendation Cache and Invalidation','''
with Lab('ns5p07',['recs:U42:v1']) as lab:
    r=lab.r; k=lab.key('recs:U42:v1')
    show('initial_miss',r.get(k))
    r.set(k,'P101,P102',ex=60)
    show('cache_hit',r.get(k))
    show('ttl_active',0<r.ttl(k)<=60)
    r.delete(k)
    show('after_invalidation',r.get(k))
''','<p>Cache recommendation IDs under a versioned key with TTL. These fixed IDs are not output from a trained model; invalidation removes the cached copy.</p>'),
 P('ns5p08','Python Cache-Aside Integration','''
with Lab('ns5p08',['product:P101']) as lab:
    r=lab.r; k=lab.key('product:P101')
    source={'P101':'Sensor Node'}
    def read_product():
        value=r.get(k)
        if value is not None:
            return {'from':'cache','value':value}
        value=source['P101']
        r.set(k,value,ex=60)
        return {'from':'source','value':value}
    show('first',read_product())
    show('second',read_product())
    source['P101']='Sensor Node v2'; r.delete(k)
    show('after_update',read_product())
''','<p>Actual Python + Redis: miss → source fixture, hit → Redis, update/invalidate → new source value. The dictionary is not a live MongoDB/Cassandra service or a performance benchmark.</p>'),
]
assert len(PROGRAMS)==8
