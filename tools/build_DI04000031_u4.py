"""Build Neo4j Unit 4 from actual executed Cypher and complete fixture checks."""
import copy
import hashlib
import json
from pathlib import Path
import sys

from subject_DI04000031 import SUBJECT,ROOT,DIAG_DIR,check_and_write
from content_DI04000031_u4_notes import NOTES,SOURCES
from content_DI04000031_u4_extras import SYNTAX,VIVA,PRACTICE_QS
from content_DI04000031_u4_programs import PROGRAMS
from content_DI04000031_u4_shared import PEOPLE,FRIENDSHIPS,FIXTURE_JSON
from diagrams_DI04000031_u4 import TITLES,main as draw_diagrams
from neo4j_content import assert_runtime,authentication_rejections,scratch_artifacts,shell
from nosql_content import tr
from preview_builder import build_preview


def result(n,label):
    out=next(p['out'] for p in PROGRAMS if p['id']==f'ns4p{n:02d}')
    return json.loads(next(line[len(label)+2:] for line in out.splitlines() if line.startswith(label+': ')))


def main():
    runtime=assert_runtime();denials=authentication_rejections()
    assert scratch_artifacts()=={'scope_labels':[],'constraints':[]}
    assert shell('RETURN 1 AS connected;')=='connected\n1'
    people=result(15,'verify_every_person');edges=result(15,'verify_every_relationship')
    wanted_people=[{'id':p['person_id'],'name':p['name'],'city':p['city'],'age':p['age']} for p in PEOPLE]
    wanted_edges=sorted([{'source':r['from'],'target':r['to'],'since':r['since']} for r in FRIENDSHIPS],key=lambda r:(r['source'],r['target']))
    assert people==wanted_people,'Imported person ID/property mismatch'
    assert edges==wanted_edges,'Imported relationship endpoint/year mismatch'
    index=result(11,'backing_index');assert len(index)==1 and index[0]['state']=='ONLINE'
    draw_diagrams()
    unit={
        'subject':'DI04000031','unit':4,'format':'notes',
        'title':tr('Graph Databases: Neo4j'),'hours':12,'weightage':20,
        'tabs':['notes','programs','diagrams','syntax','viva'],
        'intro_text':tr('Application-oriented property graphs, Desktop/Aura and Browser setup guidance, basic Cypher and graph CRUD. Includes 16 real Neo4j programs, verified synthetic graph import and transparent recommendation/shared-device pattern examples for Practicals 7–8. Graph algorithms are examples only, not implementations; the reference is a private Community server, not a performed Desktop/Aura GUI setup.'),
        'notes':copy.deepcopy(NOTES)+[{'title':tr('Answered Practical Revision Tasks — Not a Theory Question Paper'),
            'role':'practice','items':[{'h':q['q'],'body':q['a']} for q in PRACTICE_QS]}],
        'programs':PROGRAMS,'diagrams':list(TITLES),'_diagram_titles':TITLES,
        'syntax':SYNTAX,'viva':VIVA,'exam_questions':[],
        'lesson_count':20,'practice_task_count':18,'practical_numbers':[7,8],
        'learning_outcomes':[tr('Utilize Neo4j to solve relationship-based problems with graph queries (CO4).')],
        'content_kind':'real_neo4j_practical',
        'assessment_note':tr('Practical PA 20 + ESE 30 = 50 for the course; theory ESE/PA 0. Twenty percent is content weightage, not an invented theory-paper or per-question allocation.'),
        'runtime_evidence':{
            'server':'Neo4j','server_version':runtime['server'],'edition':runtime['edition'],
            'shell':'Cypher Shell','shell_version':runtime['shell'],'driver':'official Python neo4j',
            'driver_version':runtime['driver'],'bolt_protocol':runtime['bolt_protocol'],
            'java':runtime['java'],'python':sys.version.split()[0],'os':'Debian 13 x86_64',
            'authenticated':runtime['authenticated'],'password_change_required':runtime['password_change_required'],
            'anonymous_rejection':denials['anonymous'],'factory_password_rejection':denials['factory_password'],
            'physical_instances':runtime['physical_instances'],'public_database_endpoint':False,
            'desktop_installed':False,'aura_provisioned':False,'browser_ui_automated':False,
            'cypher_shell_connection_verified':True,'server_usage_reporting':runtime['server_usage_reporting'],
            'driver_telemetry':runtime['driver_telemetry'],'graph_algorithm_library_installed':False,
            'graph_algorithms_implemented':False,'model_trained':False,'company_deployments_verified':False,
            'cluster_failover_tested':False,'performance_benchmarked':False,'programs_executed':len(PROGRAMS),
            'execution_client':'Official Python driver over real Bolt; separate matching Cypher Shell connectivity proof',
            'output_origin':'Actual returned rows and summary counters; JSON preserves row order; temporal display ISO UTC; internal IDs/timings/non-error notifications not published as stable output',
            'transaction_scope':'Each statement is an implicit auto-commit transaction; not whole-file atomicity',
            'cleanup_scope':'Atomic fresh named constraint claim; only captured owned nodes and successfully created constraints removed',
            'business_index_observation':index[0]['state'],
            'fixture':{'file':'graph_fixture.json','synthetic':True,
                'sha256':hashlib.sha256(FIXTURE_JSON.encode()).hexdigest(),
                'imported_social_people':len(people),'imported_social_relationships':len(edges),
                'actual_json_parameter_import':True,'all_person_ids_values_match':True,
                'all_relationship_endpoints_years_match':True,'live_ingestion':False,
                'movie_banking_sections_imported_by_program15':False},
        },
        'sources':[{'title':title,'url':url} for title,url in SOURCES],
    }
    path=check_and_write(unit);unit=json.loads(Path(path).read_text())
    preview=Path(ROOT,'preview/DI04000031_unit4_preview.html')
    build_preview(unit,SUBJECT,DIAG_DIR,str(preview))
    from export_DI04000031_u4_practicals import export
    export()
    print('Neo4j Unit 4: 20 lessons / 16 real Cypher programs / 14 diagrams / 16 reference cards / 56 viva / 18 answered tasks')
    print('Real reference:',json.dumps(unit['runtime_evidence']))
    print('Remaining owned-prefix artifacts:',json.dumps(scratch_artifacts()))
    print('Preview:',preview,preview.stat().st_size,'bytes')


if __name__=='__main__':main()
