"""Private real-Neo4j teaching harness; never export its credentials/runtime."""
import json
from pathlib import Path
import re
import subprocess
import sys
import tempfile

from setup_neo4j_runtime import CACHE, HOME, JAVA, CONF, CREDENTIALS, environment
from neo4j_lab_runner import connect, run_source, constraint_prefix
from content_DI04000031_u4_shared import FIXTURE_JSON

URI='bolt://127.0.0.1:7688'
DATABASE='neo4j'


def credentials():
    assert CREDENTIALS.stat().st_mode & 0o777 == 0o600
    return json.loads(CREDENTIALS.read_text())


def open_driver():
    c=credentials();return connect(URI,c['username'],c['password'])


def scratch_artifacts():
    with open_driver() as driver,driver.session(database=DATABASE) as session:
        labels=session.run("MATCH (n) UNWIND labels(n) AS label WITH DISTINCT label WHERE label STARTS WITH 'NS4_' RETURN label ORDER BY label").value()
        constraints=session.run("SHOW CONSTRAINTS YIELD name WHERE name STARTS WITH 'di04000031_u4_' RETURN name ORDER BY name").value()
    return {'scope_labels':labels,'constraints':constraints}


def shell(source):
    c=credentials();env=environment();env.update({'NEO4J_USERNAME':c['username'],'NEO4J_PASSWORD':c['password']})
    with tempfile.TemporaryDirectory(prefix='neo4j-shell-') as tmp:
        file=Path(tmp,'query.cypher');file.write_text(source+'\n')
        result=subprocess.run([str(HOME/'bin/cypher-shell'),'--address',URI,'--database',DATABASE,
                               '--format','plain','--non-interactive','--file',str(file)],
                              env=env,text=True,capture_output=True,timeout=45)
    if result.returncode:raise RuntimeError('Actual cypher-shell failed: '+(result.stdout+result.stderr).replace(c['password'],'<private password>'))
    return result.stdout.rstrip('\n')


def assert_runtime():
    import neo4j
    with open_driver() as driver,driver.session(database=DATABASE) as session:
        component=session.run('CALL dbms.components() YIELD name,versions,edition RETURN name,versions,edition').single().data()
        user=session.run('SHOW CURRENT USER YIELD user,passwordChangeRequired RETURN user,passwordChangeRequired').single().data()
        settings=session.run("SHOW SETTINGS YIELD name,value WHERE name IN ['dbms.security.auth_enabled','dbms.usage_report.enabled','server.bolt.listen_address','server.http.listen_address'] RETURN name,value").data()
        settings={row['name']:row['value'] for row in settings}
        optional=session.run("SHOW PROCEDURES YIELD name WHERE name STARTS WITH 'gds.' OR name STARTS WITH 'apoc.' RETURN count(*) AS n").single()['n']
        assert optional==0
        info=driver.get_server_info()
    assert neo4j.__version__=='5.28.8'
    assert component['versions']==['5.26.32'] and component['edition']=='community'
    assert user['user']==credentials()['username'] and user['passwordChangeRequired'] is False
    assert settings['dbms.security.auth_enabled']=='true'
    assert settings['dbms.usage_report.enabled']=='false'
    assert settings['server.bolt.listen_address']=='127.0.0.1:7688'
    assert settings['server.http.listen_address']=='127.0.0.1:7475'
    java=subprocess.check_output([str(JAVA/'bin/java'),'-version'],stderr=subprocess.STDOUT,text=True)
    version=re.search(r'Temurin-([0-9.+]+)',java).group(1);assert version=='21.0.13+9'
    client=subprocess.check_output([str(HOME/'bin/cypher-shell'),'--version'],env=environment(),text=True).strip()
    assert client=='Cypher-Shell 5.26.32'
    return {'server':'5.26.32','edition':component['edition'],'shell':'5.26.32',
            'driver':neo4j.__version__,'java':'Temurin '+version,'authenticated':True,
            'password_change_required':False,'server_agent':info.agent,'bolt_protocol':'.'.join(map(str,info.protocol_version)),
            'server_usage_reporting':False,'driver_telemetry':False,'physical_instances':1,
            'desktop_installed':False,'aura_provisioned':False,'browser_ui_automated':False,
            'public_database_endpoint':False,'graph_algorithm_library_installed':bool(optional)}



def authentication_rejections():
    from neo4j import GraphDatabase
    from neo4j.exceptions import AuthError
    observed={}
    for label,auth in [('anonymous',None),('factory_password',('neo4j','neo4j'))]:
        driver=GraphDatabase.driver(URI,auth=auth,telemetry_disabled=True,connection_timeout=5)
        try:
            try:driver.verify_connectivity()
            except AuthError as error:
                assert error.code=='Neo.ClientError.Security.Unauthorized'
                observed[label]=error.code
            else:raise AssertionError('Unexpected insecure connection was accepted')
        finally:driver.close()
    # Confirm denials did not just reflect a stopped server or lock out valid access.
    with open_driver() as driver:driver.verify_connectivity()
    return observed


def run_script(source):
    with tempfile.TemporaryDirectory(prefix='neo4j-fixtures-') as tmp:
        Path(tmp,'graph_fixture.json').write_text(FIXTURE_JSON)
        with open_driver() as driver,driver.session(database=DATABASE) as session:
            return run_source(source,session,tmp)


def source_for(id_,body):
    scope='NS4_'+id_;claim=constraint_prefix(scope)+'owner'
    header=('// Trusted prepared example; fresh disposable scope only.\n'
            '// @scope '+scope+'\n'
            'CREATE CONSTRAINT '+claim+'\n'
            'FOR (n:'+scope+') REQUIRE n.__owner IS UNIQUE;\n'
            'CREATE (:'+scope+" {__owner:'di04000031_u4_"+id_+"'});\n")
    footer=('\n// Remove only this newly owned graph, then release its claim.\n'
            'MATCH (n:'+scope+') DETACH DELETE n;\n'
            'DROP CONSTRAINT '+claim+';\n')
    return header+body.strip('\n').replace('@@L@@',scope).replace('@@C@@',constraint_prefix(scope)+'person_id')+'\n'+footer


def P(id_,title,body,explanation):
    source=source_for(id_,body)
    output=run_script(source)
    return {'id':id_,'title':{'en':title},'code':{'en':source.rstrip('\n')},
            'out':output,'expl':{'en':explanation}}


if __name__=='__main__':
    print(json.dumps(assert_runtime(),indent=2))
    print('Remaining owned-prefix artifacts:',json.dumps(scratch_artifacts()))
    print('Actual cypher-shell:',shell('RETURN 1 AS connected;'))
