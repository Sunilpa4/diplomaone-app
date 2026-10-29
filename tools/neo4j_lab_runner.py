"""Guarded runner for trusted Unit 4 Cypher files on REAL Neo4j.

Requires the official Python neo4j driver. Every statement is sent unchanged
(apart from ignored comments) in its own implicit auto-commit transaction.
A uniquely named, freshly created constraint is the atomic namespace claim:
refuse existing scope nodes/schema; ownership starts only after CREATE succeeds.
Finally remove ONLY the captured owned scope and successfully created constraints.
No whole-database deletion, fake engine or graph-algorithm implementation.
This prepared-file guard is NOT a security parser for arbitrary untrusted Cypher.
"""
import argparse
from datetime import datetime, date, timezone
import getpass
import json
import os
from pathlib import Path
import re


def load_driver():
    try:
        import neo4j
        from neo4j import GraphDatabase
        from neo4j.exceptions import Neo4jError
        from neo4j.time import Date, DateTime
    except ImportError as e:
        raise RuntimeError('Install the official neo4j Python driver: python3 -m pip install -r requirements.txt') from e
    return neo4j, GraphDatabase, Neo4jError, Date, DateTime


def connect(uri, username, password):
    _, GraphDatabase, _, _, _ = load_driver()
    driver = GraphDatabase.driver(uri, auth=(username,password), telemetry_disabled=True,
                                  connection_timeout=10, max_connection_pool_size=2)
    try:
        driver.verify_connectivity(); return driver
    except BaseException:
        driver.close(); raise


def normalize(value):
    _, _, _, Date, DateTime = load_driver()
    if isinstance(value, DateTime): value = value.to_native()
    if isinstance(value, datetime):
        if value.tzinfo is None: value = value.replace(tzinfo=timezone.utc)
        return value.astimezone(timezone.utc).isoformat(timespec='milliseconds').replace('+00:00','Z')
    if isinstance(value, (Date, date)): return str(value)
    if isinstance(value, dict): return {str(k):normalize(v) for k,v in value.items()}
    if isinstance(value, (list,tuple)): return [normalize(v) for v in value]
    if value is None or isinstance(value,(str,bool,int,float)): return value
    raise TypeError('Return business properties/primitive values rather than unstable internal graph objects.')


def statements(source):
    """Lexer for the supplied Cypher: quotes/backticks, escapes and // comments.

    Human-readable @result/@expect/@params/@params_file/@stats comments apply
    to the next statement. They are runner annotations, NOT Cypher extensions.
    Block comments, shell commands and arbitrary custom scripts are unsupported.
    """
    result=[];chars=[];quote=None;i=0;meta={}
    while i<len(source):
        c=source[i]
        if quote:
            chars.append(c)
            if c=='\\' and quote!='`' and i+1<len(source):
                chars.append(source[i+1]);i+=1
            elif c==quote:
                if i+1<len(source) and source[i+1]==quote:
                    chars.append(source[i+1]);i+=1
                else:quote=None
        elif c in ('\"',"'",'`'): quote=c;chars.append(c)
        elif source[i:i+2]=='//':
            end=source.find('\n',i)
            if end<0:end=len(source)
            comment=source[i:end]
            for kind in ('result','expect','params_file'):
                m=re.match(r'//\s*@'+kind+r'\s+(\S+)\s*$',comment)
                if m:meta[kind]=m.group(1)
            m=re.match(r'//\s*@params\s+(.+)\s*$',comment)
            if m:
                params=json.loads(m.group(1))
                if not isinstance(params,dict):raise ValueError('@params must be a JSON object')
                meta['params']=params
            if re.fullmatch(r'//\s*@stats\s*',comment):meta['stats']=True
            chars.append('\n');i=end-1
        elif c==';':
            sql=''.join(chars).strip()
            if sql:result.append({'sql':sql,**meta})
            chars=[];meta={}
        else:chars.append(c)
        i+=1
    if quote or ''.join(chars).strip():raise ValueError('Unterminated Cypher string/statement; supply the final semicolon.')
    return result


def constraint_prefix(scope): return 'di04000031_u4_'+scope.removeprefix('NS4_')+'_'


def safe_scope(source):
    scopes=re.findall(r'(?m)^//\s*@scope\s+(NS4_[a-z0-9_]{1,32})\s*$',source)
    if len(scopes)!=1:raise ValueError('One explicit prefix-scoped Unit 4 namespace is required.')
    scope=scopes[0];prefix=constraint_prefix(scope);claim=prefix+'owner';parsed=statements(source)
    first='CREATE CONSTRAINT '+claim+' FOR (n:'+scope+') REQUIRE n.__owner IS UNIQUE'
    if not parsed or re.sub(r'\s+',' ',parsed[0]['sql'])!=first or set(parsed[0])!={'sql'}:
        raise ValueError('The first statement must atomically CREATE the fresh ownership constraint.')
    footer=['MATCH (n:'+scope+') DETACH DELETE n','DROP CONSTRAINT '+claim]
    if len(parsed)<3 or [re.sub(r'\s+',' ',item['sql']) for item in parsed[-2:]]!=footer:
        raise ValueError('Complete prepared files must end by cleaning their scope and releasing the claim last.')
    for item in parsed:
        sql=item['sql']
        if re.match(r'^(?:CREATE|ALTER|DROP|START|STOP)\s+(?:DATABASE|USER|ROLE|ALIAS)\b|^(?:GRANT|DENY|REVOKE|USE)\b',sql,re.I):
            raise ValueError('Database/user/role management and context switching are not course data operations.')
        m=re.match(r'^(CREATE|DROP)\s+CONSTRAINT\s+(\w+)\b',sql,re.I)
        if m and (not m.group(2).startswith(prefix) or 'IF NOT EXISTS' in sql.upper() or 'IF EXISTS' in sql.upper()):
            raise ValueError('Only fresh explicitly named constraints in the captured scope are allowed.')
        if m and item.get('expect'):raise ValueError('Schema ownership statements cannot be expected failures.')
        if re.search(r'\b(?:DELETE|SET|REMOVE|CREATE|MERGE)\b',sql,re.I) and not m:
            if not re.search(r':'+re.escape(scope)+r'\b',sql):
                raise ValueError('A prepared write must include its explicit scope label.')
        if re.match(r'^CALL\s+',sql,re.I) and not re.match(r'^CALL\s+(?:dbms\.components|db\.awaitIndexes)\s*\(',sql,re.I):
            raise ValueError('Only the listed read-only built-in metadata/index-wait calls are used here.')
    return scope,claim,parsed


def scope_count(session,scope):
    # Read-only small-lab preflight; no UnknownLabel notification for a NEW label.
    return session.run('MATCH (n) WHERE $scope IN labels(n) RETURN count(n) AS n',scope=scope).single()['n']


def scope_constraints(session,scope):
    return [r['name'] for r in session.run('SHOW CONSTRAINTS YIELD name WHERE name STARTS WITH $prefix RETURN name ORDER BY name',
                                          prefix=constraint_prefix(scope))]


def run_source(source,session,fixtures='.'):
    scope,claim,parsed=safe_scope(source)
    if scope_count(session,scope) or scope_constraints(session,scope):
        raise RuntimeError('Refusing pre-existing scope nodes/schema; nothing removed: '+scope)
    owned=False;constraints=set();output=[]
    try:
        for index,item in enumerate(parsed):
            if index and not owned:raise ValueError('No statement may run after the namespace claim was released.')
            sql=item['sql'];params=item.get('params',{}).copy()
            if 'params_file' in item:
                filename=item['params_file']
                if filename!='graph_fixture.json':raise ValueError('Only the supplied graph_fixture.json is used.')
                file=Path(fixtures)/filename
                if not file.is_file():raise ValueError('Supply --fixtures with the folder holding graph_fixture.json')
                loaded=json.loads(file.read_text())
                if not isinstance(loaded,dict):raise ValueError('Fixture parameters must be a JSON object')
                params={**loaded,**params}
            expected=item.get('expect');label=item.get('result','result')
            try:
                result=session.run(sql,parameters=params)
                columns=result.keys();rows=[normalize(record.data()) for record in result]
                summary=result.consume()
            except Exception as error:
                code=getattr(error,'code',None)
                if not expected or code!=expected:raise
                output.append(label+': '+code+' (server rejection)');continue
            if expected:raise AssertionError('Expected server rejection not raised: '+expected)
            match=re.match(r'^(CREATE|DROP)\s+CONSTRAINT\s+(\w+)\b',sql,re.I)
            if match:
                action,name=match.groups()
                if action.upper()=='CREATE':
                    constraints.add(name)
                    if name==claim:owned=True
                else:
                    constraints.discard(name)
                    if name==claim:owned=False
            if columns:output.append(label+': '+json.dumps(rows,ensure_ascii=False,separators=(',',':')))
            if item.get('stats'):
                keys=('nodes_created','nodes_deleted','relationships_created','relationships_deleted',
                      'properties_set','labels_added','labels_removed','constraints_added','constraints_removed')
                counters={key:getattr(summary.counters,key) for key in keys}
                output.append(label+'_counters: '+json.dumps(counters,separators=(',',':')))
    finally:
        if owned:
            session.run('MATCH (n:'+scope+') DETACH DELETE n').consume()
            for name in sorted(constraints-{claim}):session.run('DROP CONSTRAINT '+name).consume()
            if claim in constraints:session.run('DROP CONSTRAINT '+claim).consume()
    if scope_count(session,scope) or scope_constraints(session,scope):raise RuntimeError('Owned scope cleanup incomplete')
    output.append('Scoped graph and constraints removed: true')
    return '\n'.join(output)


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('script',type=Path)
    parser.add_argument('--uri',default=os.environ.get('NEO4J_URI','bolt://127.0.0.1:7687'))
    parser.add_argument('--database',default=os.environ.get('NEO4J_DATABASE','neo4j'))
    parser.add_argument('--username',default=os.environ.get('NEO4J_USERNAME','neo4j'))
    parser.add_argument('--fixtures',type=Path,default=Path.cwd())
    args=parser.parse_args()
    password=os.environ.get('NEO4J_PASSWORD') or getpass.getpass('Private Neo4j password (hidden): ')
    with connect(args.uri,args.username,password) as driver:
        with driver.session(database=args.database) as session:
            print(run_source(args.script.read_text(),session,args.fixtures))


if __name__=='__main__':main()
