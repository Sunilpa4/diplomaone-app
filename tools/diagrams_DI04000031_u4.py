"""Fourteen self-contained mobile Neo4j SVG teaching diagrams.
Illustrative diagrams of tested fixtures, NOT fabricated Browser screenshots.
No external fonts/images, CSS, markers, GDS implementation or mathematical proof.
"""
import math
import os
from flowchart_lib import svg,text,arr,rbox,line,P,INK
from subject_DI04000031 import DIAG_DIR
from diagrams_DI04000031_u1 import (heading,lines,frame,foot,BLUE,BF,GREEN,GF,
    ORANGE,OF,TEAL,TF,RED,RF,GREY,PF)

TITLES={
 'ns4_property':'Property Graph: Nodes, Labels, Relationships and Properties',
 'ns4_direction':'Stored Direction versus the Direction of a Read Pattern',
 'ns4_setup':'Desktop or Aura Setup versus the Executed Server Reference',
 'ns4_browser':'Browser Graph Entities versus Scalar Table Results',
 'ns4_query':'MATCH, WHERE, RETURN, ORDER BY and LIMIT',
 'ns4_merge':'CREATE, MATCH and Complete-Pattern MERGE',
 'ns4_delete':'Relationship DELETE, Connected Rejection and DETACH',
 'ns4_optional':'OPTIONAL MATCH Preserves Rows with Nulls',
 'ns4_identity':'Business Uniqueness, Atomic Lab Claim and Statement Rollback',
 'ns4_import':'Actual JSON Parameters and UNWIND Import Verification',
 'ns4_social':'Two-Hop Friend Candidates in the Six-Person Fixture',
 'ns4_movies':'Unseen Movies Liked by Known People',
 'ns4_fraud':'Shared Devices Yield Review Candidates, Not Fraud Verdicts',
 'ns4_ai':'Basic Query Examples versus Unimplemented AI/Algorithms',
}


def node(x,y,id_,name='',fill=BF,stroke=BLUE,r=29):
    b=f'<circle cx="{x}" cy="{y}" r="{r}" fill="{fill}" stroke="{stroke}" stroke-width="1.6"/>'
    if name:b+=text(x,y-8,id_,10.5,color=stroke,weight='bold')+text(x,y+9,name,11.5)
    else:b+=text(x,y,id_,12,color=stroke,weight='bold')
    return b


def edge(a,b,color=P,ra=29,rb=29):
    dx=b[0]-a[0];dy=b[1]-a[1];length=math.hypot(dx,dy);ux=dx/length;uy=dy/length
    return arr([(round(a[0]+ux*ra,2),round(a[1]+uy*ra,2)),
                (round(b[0]-ux*rb,2),round(b[1]-uy*rb,2))],color)


def property_graph():
    b=heading('A property graph is connected data','Illustration of program 3, not a GUI screenshot')
    b+=edge((80,119),(280,119),P,37,37)
    b+=node(80,119,'P01','Asha',BF,BLUE,37)+node(280,119,'P02','Ravi',GF,GREEN,37)
    b+=text(180,90,'KNOWS',12,color=P,weight='bold')
    b+=text(180,143,'since: 2024',10.5,color=GREY)
    b+=frame(18,188,324,92,BF,BLUE)
    b+=lines(180,212,['NODE labels: Person (also Student in program 2)',
                        'NODE properties: person_id, name, age',
                        'A label does not automatically make an ID unique.'],10.7,24)
    b+=frame(18,306,324,95,PF,P)
    b+=lines(180,330,['RELATIONSHIP type: exactly one, KNOWS',
                        'Stored direction: Asha -> Ravi',
                        'RELATIONSHIP property: since = 2024'],11.5,24)
    b+=foot(439,['Each relationship has source and target endpoints.',
                 'The endpoints may even be the same node.',
                 'Use business identity rules, not internal IDs.'])
    return svg(360,497,b)


def direction():
    b=heading('Stored arrows, chosen read pattern','All three read patterns leave the data unchanged')
    for y,title,syntax,result,fill,stroke in [
        (68,'Outgoing from Asha','(a)-[:KNOWS]->(b)','Asha -> Ravi and Neha',BF,BLUE),
        (195,'Incoming to Ravi','(a)<-[:KNOWS]-(b)','Ravi <- Asha',PF,P),
        (322,'Either direction at Ravi','(a)-[:KNOWS]-(b)','Asha, Meera and Imran',GF,GREEN)]:
        b+=frame(18,y,324,103,fill,stroke)
        b+=text(180,y+22,title,12,color=stroke,weight='bold')
        b+=text(180,y+52,syntax,12)
        b+=text(180,y+80,result,11.5)
    b+=foot(458,['An undirected read does not create reverse edges.',
                 'Business direction is a modeling decision.'])
    return svg(360,498,b)


def setup():
    b=heading('Choose a Neo4j learning setup','Practical 7: record what YOU actually install/use')
    b+=frame(18,71,152,160,BF,BLUE)+frame(190,71,152,160,GF,GREEN)
    b+=lines(94,98,['Desktop','Local development app','Create/start an instance','Private password','Open Browser / Query'],10.8,27)
    b+=lines(266,98,['AuraDB','Managed cloud service','Check tier/cost/limits','Save private credentials','Use provided TLS URI'],10.8,27)
    b+=arr([(94,231),(94,257),(180,257),(180,279)],BLUE)
    b+=arr([(266,231),(266,257),(180,257)],GREEN)
    b+=rbox(180,308,324,58,'Verify server/edition -> write/read\nObserve nodes, arrows and properties',PF,P,11.5)
    b+=frame(18,365,324,86,OF,ORANGE)
    b+=lines(180,389,['Executed reference: private Community 5.26.32',
                        'Matching shell; Java 21; official Python driver',
                        'NOT Desktop/Aura installation or GUI proof'],10.7,23)
    b+=foot(479,['Keep credentials/interfaces private; do not bypass TLS.'])
    return svg(360,504,b)


def browser():
    b=heading('Browser is a database client','Illustrative workflow, not an executed GUI capture')
    b+=rbox(180,86,324,45,'Your authorized connection to YOUR instance',BF,BLUE,11.1)
    b+=arr([(180,109),(180,139)],P)
    b+=rbox(180,164,324,50,'MATCH pattern -> choose what to RETURN',PF,P,11.7)
    b+=arr([(180,189),(180,214),(94,214),(94,240)],BLUE)
    b+=arr([(180,214),(266,214),(266,240)],GREEN)
    b+=frame(18,240,152,174,BF,BLUE)+frame(190,240,152,174,GF,GREEN)
    b+=lines(94,263,['RETURN a,r,b','Graph entities'],11.5,24,BLUE,weight='bold')
    b+=node(63,348,'A',fill='#FFFFFF',stroke=BLUE,r=18)
    b+=node(127,348,'B',fill='#FFFFFF',stroke=BLUE,r=18)
    b+=edge((63,348),(127,348),P,18,18)
    b+=text(94,388,'Inspect labels/type/props',9.5,color=GREY)
    b+=lines(266,264,['RETURN a.name','Scalar columns'],11.5,24,GREEN,weight='bold')
    b+=line('M210 324 H322 M210 351 H322 M210 378 H322',GREEN,1)
    b+=text(266,337,'name | Asha',10.5)+text(266,364,'name | Ravi',10.5)
    b+=foot(446,['Local defaults: Browser 7474 / Bolt 7687.',
                 'localhost means your computer, not this notes app.',
                 'A table result is not a missing-graph error.'])
    return svg(360,506,b)


def query():
    b=heading('Read a graph with Cypher','Logical query explanation, not an optimizer plan')
    cards=[(84,'MATCH (p:Person) -> candidate nodes',BF,BLUE),
           (158,"WHERE city='Surat' AND age>=20",PF,P),
           (232,'RETURN business ID, name and age',GF,GREEN),
           (306,'ORDER BY ID; LIMIT only when needed',OF,ORANGE)]
    for i,(y,label,fill,stroke) in enumerate(cards):
        if i:b+=arr([(180,y-51),(180,y-23)],P)
        b+=rbox(180,y,324,46,label,fill,stroke,11.5)
    b+=arr([(180,329),(180,363)],GREEN)
    b+=rbox(180,395,324,64,'P01 | Asha | 20\nP05 | Imran | 20',GF,GREEN,12)
    b+=foot(455,['A missing match returns no rows.',
                 'Without ORDER BY, do not promise row order.'])
    return svg(360,496,b)


def merge():
    b=heading('CREATE, MATCH and MERGE','Identity comes from a deliberate pattern/constraint')
    cards=[(69,'CREATE','New element; can duplicate without a rule',BF,BLUE),
           (171,'MATCH','Bind existing; missing match creates nothing',PF,P),
           (273,'MERGE P09: first execution','Not found -> create Jai, visits 1',GF,GREEN),
           (375,'MERGE P09: second execution','Found -> ON MATCH sets visits 2',OF,ORANGE)]
    for y,title,detail,fill,stroke in cards:
        b+=frame(18,y,324,79,fill,stroke)
        b+=text(180,y+23,title,12,color=stroke,weight='bold')
        b+=text(180,y+54,detail,10.8)
    b+=foot(484,['MERGE matches the whole specified pattern.',
                 'A changing name is a poor identity component.'])
    return svg(360,526,b)


def delete():
    b=heading('Deletion has a graph scope','Preview the match; use only owned disposable data')
    cards=[(70,'DELETE connected node','Rejected while incident relationships remain',RF,RED),
           (184,'DELETE the selected relationship','Both endpoint nodes remain',BF,BLUE),
           (298,'DETACH DELETE selected node','Node + ALL incident relationships removed',OF,ORANGE)]
    for y,title,detail,fill,stroke in cards:
        b+=frame(18,y,324,88,fill,stroke)
        b+=text(180,y+24,title,12,color=stroke,weight='bold')
        b+=text(180,y+57,detail,10.7)
    b+=foot(424,['Other endpoints are not automatically deleted.',
                 'SET/REMOVE can change properties/labels instead.',
                 'No whole-database wipe or physical-erasure claim.'])
    return svg(360,485,b)


def optional():
    b=heading('OPTIONAL MATCH keeps a row','Six people; only Asha has an outgoing MENTORS link')
    b+=node(76,115,'P01','Asha',BF,BLUE,35)+node(284,115,'P02','Ravi',GF,GREEN,35)
    b+=edge((76,115),(284,115),P,35,35)+text(180,86,'MENTORS',11.5,color=P,weight='bold')
    b+=frame(18,183,324,137,PF,P)
    b+=lines(180,209,['Person row | optional mentee',
                        'P01 | Ravi', 'P02–P06 | null',
                        'Unmatched people are still returned.'],11.5,27)
    b+=frame(18,349,152,69,BF,BLUE)+frame(190,349,152,69,GF,GREEN)
    b+=lines(94,369,['count(*)','6 rows'],12,26,BLUE)
    b+=lines(266,369,['count(mentee)','1 non-null value'],11.5,26,GREEN)
    b+=foot(450,['A later non-null WHERE deliberately removes null rows.',
                 'An absent relationship is not a proven real-world fact.'])
    return svg(360,493,b)


def identity():
    b=heading('Identity and lab ownership differ','Only successfully created scope/schema is owned')
    b+=frame(18,68,324,98,BF,BLUE)
    b+=lines(180,93,['BUSINESS uniqueness: person_id',
                       'Duplicate P01 is rejected; ONLINE backing index.',
                       'No ID can still be absent: uniqueness != existence.'],10.8,26)
    b+=frame(18,193,324,106,PF,P)
    b+=lines(180,217,['LAB claim: fresh named ownership constraint',
                        'CREATE succeeds -> this runner owns the scope.',
                        'Existing/failed claim -> do not remove it.',
                        'A prefix alone is not a security sandbox.'],10.7,23)
    b+=frame(18,328,324,102,GF,GREEN)
    b+=lines(180,351,['One statement: create P98, then duplicate P01',
                        'Server rejects -> whole statement rolled back.',
                        'Observed P98 count is 0.',
                        'Earlier separate statements are not undone.'],10.8,23)
    b+=foot(462,['No index-speed or multi-statement-atomicity claim.'])
    return svg(360,490,b)


def fixture_import():
    b=heading('Import, then verify every element','Program 15: actual JSON parameters + UNWIND')
    cards=[(86,'graph_fixture.json: people + friendships',BF,BLUE),
           (165,'Official driver sends arrays as parameters',PF,P),
           (244,'UNWIND creates 6 people and 6 KNOWS edges',GF,GREEN)]
    for i,(y,label,fill,stroke) in enumerate(cards):
        if i:b+=arr([(180,y-55),(180,y-24)],P)
        b+=rbox(180,y,324,48,label,fill,stroke,11)
    b+=arr([(180,268),(180,304)],GREEN)
    b+=frame(18,304,324,119,OF,ORANGE)
    b+=lines(180,328,['Read-back verification, not just input length:',
                        'Every person ID / name / city / age',
                        'Every relationship source / target / since',
                        'Counters are actual server summary values.'],11,24)
    b+=foot(456,['Only the social arrays are imported in this program.',
                 'Synthetic snapshot: no live ingestion or training.'])
    return svg(360,497,b)


def social():
    b=heading("Asha's two-hop candidates",'Stored KNOWS arrows; read either direction here')
    pos={'P01':(180,100),'P02':(76,203),'P03':(284,203),
         'P04':(199,309),'P05':(61,353),'P06':(270,414)}
    for a,c in [('P01','P02'),('P01','P03'),('P02','P04'),('P03','P04'),('P02','P05'),('P04','P06')]:
        b+=edge(pos[a],pos[c],GREY)
    for id_,name in [('P01','Asha'),('P02','Ravi'),('P03','Neha'),('P04','Meera'),('P05','Imran'),('P06','Dev')]:
        fill,stroke=(GF,GREEN) if id_ in ('P04','P05') else (BF,BLUE) if id_=='P01' else (PF,P)
        b+=node(*pos[id_],id_,name,fill,stroke)
    b+=foot(465,['Green candidates: P04 Meera and P05 Imran.',
                 'Exclude self/direct links; DISTINCT removes repeat paths.',
                 'Dev is three hops away, not a two-hop candidate.'])
    return svg(360,524,b)


def movies():
    b=heading('Unseen movie candidates','Asha knows Ravi/Neha; the arrows below are LIKES')
    for x,id_,name in [(66,'P01','Asha'),(180,'P02','Ravi'),(294,'P03','Neha')]:
        b+=node(x,105,id_,name,BF,BLUE,28)
    b+=arr([(66,133),(66,221)],BLUE)
    b+=arr([(164,129),(93,221)],P)
    b+=arr([(180,133),(180,221)],P)
    b+=arr([(294,133),(294,221)],P)
    for x,id_,title,fill,stroke in [(66,'M01','Graph\nJourneys',RF,RED),
                                  (180,'M02','Database\nStories',GF,GREEN),
                                  (294,'M03','Space\nSignals',GF,GREEN)]:
        b+=rbox(x,265,96,87,title,fill,stroke,11)
        b+=text(x,321,id_,11,color=stroke,weight='bold')
    b+=frame(18,359,324,87,PF,P)
    b+=lines(180,382,['M01 already liked -> excluded',
                        'M02 and M03 -> distinct unseen candidates',
                        'No score, model training or relevance proof'],11,24)
    b+=foot(476,['Netflix-like workload analogy, not deployment evidence.'])
    return svg(360,503,b)


def fraud():
    b=heading('Shared device: investigate, not accuse','All account/device records are synthetic')
    for x,label in [(62,'A01'),(180,'A02'),(298,'A04')]:
        b+=node(x,110,label,fill=BF,stroke=BLUE,r=28)
        b+=edge((x,110),(180,231),P,28,36)
    b+=node(180,231,'D01','device',GF,GREEN,36)
    b+=text(180,65,'All three arrows: USES_DEVICE',10.5,color=P,weight='bold')
    b+=frame(18,290,324,83,OF,ORANGE)
    b+=lines(180,313,['Three distinct unordered review pairs:',
                        'A01–A02 | A01–A04 | A02–A04',
                        'Exclude self and symmetric duplicates.'],11,23)
    b+=rbox(180,411,324,45,'A03 -> D02 alone: contributes no shared pair',BF,BLUE,10.8)
    b+=foot(462,['Families/public computers can legitimately share devices.',
                 'A shared device is NOT a fraud verdict.',
                 'Context, consent, false positives and review matter.'])
    return svg(360,522,b)


def ai_boundary():
    b=heading('A graph query is not trained AI','Algorithm families are examples, not implementations')
    cards=[(83,'Synthetic entities + meaningful relationships',BF,BLUE),
           (155,'Basic MATCH / WHERE / RETURN patterns',PF,P),
           (227,'Traceable candidates or simple input features',GF,GREEN)]
    for i,(y,label,fill,stroke) in enumerate(cards):
        if i:b+=arr([(180,y-49),(180,y-23)],P)
        b+=rbox(180,y,324,46,label,fill,stroke,11.2)
    b+=arr([(180,250),(180,285)],ORANGE)
    b+=frame(18,285,324,107,OF,ORANGE)
    b+=lines(180,310,['Separate optional work — NOT executed here:',
                        'GDS algorithms / model training / ranking',
                        'Evaluation, eligibility, monitoring and governance',
                        'No accuracy or throughput numbers are claimed.'],10.6,23)
    b+=foot(430,['Connection examples do not prove a company deployment.',
                 'A community is not automatically a fraud ring.',
                 'Keep provenance, privacy and human oversight.'])
    return svg(360,492,b)

BUILDERS=[property_graph,direction,setup,browser,query,merge,delete,optional,
          identity,fixture_import,social,movies,fraud,ai_boundary]


def main():
    assert len(TITLES)==len(BUILDERS)==14
    for id_,build in zip(TITLES,BUILDERS):
        with open(os.path.join(DIAG_DIR,id_+'.svg'),'w',encoding='utf-8') as file:file.write(build())
    print('Neo4j Unit 4 diagrams:',len(TITLES))


if __name__=='__main__':main()
