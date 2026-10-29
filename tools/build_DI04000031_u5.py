"""Build short syllabus-focused Redis Unit 5 with real tested examples."""
import copy,json,sys
from pathlib import Path
from subject_DI04000031 import SUBJECT,ROOT,DIAG_DIR,check_and_write
from content_DI04000031_u5_notes import NOTES,SOURCES,SYNTAX,VIVA,PRACTICE_QS
from content_DI04000031_u5_programs import PROGRAMS
from diagrams_DI04000031_u5 import TITLES,main as draw
from redis_content import assert_runtime,remaining
from nosql_content import tr
from preview_builder import build_preview


def main():
    runtime=assert_runtime();assert remaining()==[];draw()
    unit={'subject':'DI04000031','unit':5,'format':'notes',
        'title':tr('Key-Value Databases: Redis'),'hours':10,'weightage':17,
        'tabs':['notes','programs','diagrams','syntax','viva'],
        'intro_text':tr('Concise syllabus coverage: Redis overview/setup; Strings, Lists, Sets and Hashes; basic commands; transactions; caching/TTL; AI use cases and simplified application integration. Includes eight real Redis examples for Practical 9, without advanced extras.'),
        'notes':copy.deepcopy(NOTES)+[{'title':tr('Five Short Practical Tasks'),'role':'practice',
             'items':[{'h':q['q'],'body':q['a']} for q in PRACTICE_QS]}],
        'programs':PROGRAMS,'diagrams':list(TITLES),'_diagram_titles':TITLES,
        'syntax':SYNTAX,'viva':VIVA,'exam_questions':[],
        'lesson_count':8,'practice_task_count':5,'practical_numbers':[9],
        'learning_outcomes':[tr('Implement Redis data structures for caching and performance optimization (CO5).')],
        'content_kind':'real_redis_practical','content_density':'concise',
        'assessment_note':tr('Course practical PA 20 + ESE 30 = 50; theory ESE/PA 0. No invented theory-paper marks.'),
        'runtime_evidence':{'server':'Redis','server_version':runtime['server_version'],
            'cli_version':runtime['cli_version'],'driver':'redis-py','driver_version':runtime['driver_version'],
            'python':sys.version.split()[0],'os':'Debian 13 x86_64','programs_executed':len(PROGRAMS),
            'authenticated':True,'private_loopback':True,'public_database_endpoint':False,
            'persistence_enabled':False,'single_instance':True,'modules_used':False,
            'ai_model_trained':False,'live_multi_database_integration':False,'performance_benchmark':False,
            'integration_source':'Local Python dictionary fixture, not a live second database',
            'output_origin':'Actual Redis replies through official redis-py; set/map display sorted; TTL range normalized',
            'cleanup':'Fresh SET NX namespace claim; declared keys only; watched ownership before cleanup'},
        'sources':[{'title':title,'url':url} for title,url in SOURCES]}
    path=check_and_write(unit);unit=json.loads(Path(path).read_text())
    preview=Path(ROOT,'preview/DI04000031_unit5_preview.html')
    build_preview(unit,SUBJECT,DIAG_DIR,str(preview))
    from export_DI04000031_u5_practicals import export
    export()
    print('Redis Unit 5: 8 short lessons / 8 tested examples / 4 diagrams / 8 reference cards / 12 viva / 5 tasks')
    print('Preview:',preview.stat().st_size,'bytes; remaining scoped keys:',remaining())


if __name__=='__main__':main()
