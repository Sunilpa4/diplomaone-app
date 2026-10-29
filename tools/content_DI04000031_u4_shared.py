"""Pure, SYNTHETIC Neo4j fixtures; no database connection on import."""
import json

PEOPLE=[
 {'person_id':'P01','name':'Asha','city':'Surat','age':20},
 {'person_id':'P02','name':'Ravi','city':'Bharuch','age':21},
 {'person_id':'P03','name':'Neha','city':'Surat','age':19},
 {'person_id':'P04','name':'Meera','city':'Vadodara','age':22},
 {'person_id':'P05','name':'Imran','city':'Surat','age':20},
 {'person_id':'P06','name':'Dev','city':'Rajkot','age':23},
]
FRIENDSHIPS=[
 {'from':'P01','to':'P02','since':2024},
 {'from':'P01','to':'P03','since':2025},
 {'from':'P02','to':'P04','since':2023},
 {'from':'P03','to':'P04','since':2024},
 {'from':'P02','to':'P05','since':2025},
 {'from':'P04','to':'P06','since':2022},
]
MOVIES=[{'movie_id':'M01','title':'Graph Journeys'},
        {'movie_id':'M02','title':'Database Stories'},
        {'movie_id':'M03','title':'Space Signals'}]
LIKES=[{'person':'P01','movie':'M01'}, {'person':'P02','movie':'M01'},
       {'person':'P02','movie':'M02'}, {'person':'P03','movie':'M03'}]
ACCOUNTS=[{'account_id':'A01','holder':'User One'},
          {'account_id':'A02','holder':'User Two'},
          {'account_id':'A03','holder':'User Three'},
          {'account_id':'A04','holder':'User Four'}]
DEVICES=[{'device_id':'D01'},{'device_id':'D02'}]
USES=[{'account':'A01','device':'D01'}, {'account':'A02','device':'D01'},
      {'account':'A03','device':'D02'}, {'account':'A04','device':'D01'}]
FIXTURE={'people':PEOPLE,'friendships':FRIENDSHIPS,'movies':MOVIES,'likes':LIKES,
         'accounts':ACCOUNTS,'devices':DEVICES,'uses':USES}
FIXTURE_JSON=json.dumps(FIXTURE,ensure_ascii=False,indent=2)+'\n'


def cypher(value):
    if isinstance(value,str):return "'"+value.replace('\\','\\\\').replace("'","\\'")+"'"
    if isinstance(value,bool):return 'true' if value else 'false'
    if isinstance(value,(int,float)):return str(value)
    raise TypeError(type(value))

PERSON_SEED=''
for row in PEOPLE:
    PERSON_SEED += ('CREATE (:@@L@@:Person {person_id:'+cypher(row['person_id'])+',\n'
                    '  name:'+cypher(row['name'])+', city:'+cypher(row['city'])+', age:'+str(row['age'])+'});\n')
SOCIAL_SEED=PERSON_SEED
for edge in FRIENDSHIPS:
    SOCIAL_SEED += ("MATCH (a:@@L@@:Person {person_id:"+cypher(edge['from'])+"}),\n"
                    "      (b:@@L@@:Person {person_id:"+cypher(edge['to'])+"})\n"
                    'CREATE (a)-[:KNOWS {since:'+str(edge['since'])+'}]->(b);\n')
MOVIE_SEED=SOCIAL_SEED
for row in MOVIES:
    MOVIE_SEED += ('CREATE (:@@L@@:Movie {movie_id:'+cypher(row['movie_id'])+',\n'
                   '  title:'+cypher(row['title'])+'});\n')
for edge in LIKES:
    MOVIE_SEED += ('MATCH (p:@@L@@:Person {person_id:'+cypher(edge['person'])+'}),\n'
                   '      (m:@@L@@:Movie {movie_id:'+cypher(edge['movie'])+'})\n'
                   'CREATE (p)-[:LIKES]->(m);\n')
BANK_SEED=''
for row in ACCOUNTS:
    BANK_SEED += ('CREATE (:@@L@@:Account {account_id:'+cypher(row['account_id'])+',\n'
                  '  holder:'+cypher(row['holder'])+'});\n')
for row in DEVICES:
    BANK_SEED += ('CREATE (:@@L@@:Device {device_id:'+cypher(row['device_id'])+'});\n')
for edge in USES:
    BANK_SEED += ('MATCH (a:@@L@@:Account {account_id:'+cypher(edge['account'])+'}),\n'
                  '      (d:@@L@@:Device {device_id:'+cypher(edge['device'])+'})\n'
                  'CREATE (a)-[:USES_DEVICE]->(d);\n')
