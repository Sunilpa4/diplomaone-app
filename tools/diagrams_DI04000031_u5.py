"""Four compact Redis topic diagrams, self-contained and mobile-sized."""
import os
from flowchart_lib import svg,text,arr,rbox,P
from subject_DI04000031 import DIAG_DIR
from diagrams_DI04000031_u1 import heading,lines,frame,foot,BLUE,BF,GREEN,GF,ORANGE,OF,PF

TITLES={'ns5_types':'Four Required Redis Structures','ns5_transaction':'MULTI, EXEC and DISCARD',
        'ns5_cache':'Cache Hit, Miss, TTL and Invalidation','ns5_integration':'Simplified Application and Redis Integration'}


def types():
    b=heading('Redis: choose the value structure')
    for y,title,example,fill,stroke in [(66,'STRING','product -> Sensor Node',BF,BLUE),
       (158,'LIST','jobs -> load, train, evaluate',PF,P),
       (250,'SET','skills -> unique Python, Redis',GF,GREEN),
       (342,'HASH','user -> name / city / age fields',OF,ORANGE)]:
        b+=frame(18,y,324,72,fill,stroke)
        b+=text(180,y+20,title,12,color=stroke,weight='bold')
        b+=text(180,y+49,example,11.5)
    b+=foot(446,['Lists are ordered; sets are unique and unordered.'])
    return svg(360,472,b)


def transaction():
    b=heading('A small Redis transaction','No other client interleaves during EXEC execution')
    for i,(y,title,fill,stroke) in enumerate([(88,'MULTI -> begin queue',BF,BLUE),
        (166,'Commands -> QUEUED',PF,P),(244,'EXEC -> ordered command replies',GF,GREEN)]):
        if i:b+=arr([(180,y-54),(180,y-24)],P)
        b+=rbox(180,y,324,48,title,fill,stroke,12)
    b+=frame(18,303,324,101,OF,ORANGE)
    b+=lines(180,328,['DISCARD cancels before execution.',
                       'Runtime errors do NOT cause rollback.',
                       'Later queued commands can still succeed.'],11.3,24)
    return svg(360,432,b)


def cache():
    b=heading('Cache-aside in brief')
    b+=rbox(180,86,324,48,'Application asks Redis for a key',BF,BLUE,12)
    b+=arr([(180,110),(180,139),(94,139),(94,166)],GREEN)
    b+=arr([(180,139),(266,139),(266,166)],ORANGE)
    b+=frame(18,166,152,96,GF,GREEN)+frame(190,166,152,96,OF,ORANGE)
    b+=lines(94,191,['HIT','Return cached value'],11.2,31)
    b+=lines(266,191,['MISS','Read source data'],11.2,31)
    b+=arr([(266,262),(266,301),(180,301),(180,329)],ORANGE)
    b+=rbox(180,358,324,58,'Cache source value with TTL\nReturn value to the application',PF,P,11.5)
    b+=foot(421,['Invalidate when the authoritative value changes.',
                 'Expiry is not memory-pressure eviction.'])
    return svg(360,462,b)


def integration():
    b=heading('Application integration','Reference: real Python + Redis, fixture source')
    for i,(y,label,fill,stroke) in enumerate([(88,'Python / web application',BF,BLUE),
          (168,'Redis -> cached values / sessions / IDs',PF,P),
          (248,'Source database/service on a cache miss',GF,GREEN)]):
        if i:b+=arr([(180,y-56),(180,y-24)],P)
        b+=rbox(180,y,324,48,label,fill,stroke,11.5)
    b+=frame(18,313,324,95,OF,ORANGE)
    b+=lines(180,337,['The executed source is a local dictionary.',
                       'No live multi-database integration or benchmark.',
                       'Caching recommendation IDs is not AI training.'],10.7,24)
    b+=foot(443,['Keep Redis private; applications mediate browser access.'])
    return svg(360,470,b)


def main():
    for id_,build in zip(TITLES,[types,transaction,cache,integration]):
        with open(os.path.join(DIAG_DIR,id_+'.svg'),'w',encoding='utf-8') as f:f.write(build())
    print('Redis diagrams:',len(TITLES))


if __name__=='__main__':main()
