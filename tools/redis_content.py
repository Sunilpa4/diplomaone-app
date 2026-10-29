"""Private Redis execution harness; never export private ACL/password files."""
import json,os,subprocess,sys,tempfile
from pathlib import Path
import redis
from setup_redis_runtime import CACHE,CREDS,SERVER,CLI,VERSION

ROOT=Path(__file__).resolve().parent.parent


def private():
    assert CREDS.stat().st_mode & 0o777==0o600
    return json.loads(CREDS.read_text())


def env():
    e=os.environ.copy();e.update({'REDIS_HOST':'127.0.0.1','REDIS_PORT':'6385','REDIS_USERNAME':'u5_lab',
        'REDIS_PASSWORD':private()['lab'],'REDIS_TLS':'0'})
    return e


def client(admin=False):
    return redis.Redis(host='127.0.0.1',port=6385,username='u5_admin' if admin else 'u5_lab',
        password=private()['admin' if admin else 'lab'],protocol=2,decode_responses=True,
        socket_connect_timeout=5,socket_timeout=5)


def cli(source):
    e=os.environ.copy();e['REDISCLI_AUTH']=private()['lab']
    p=subprocess.run([str(CLI),'-h','127.0.0.1','-p','6385','--user','u5_lab','--raw'],
        input=source+'\n',env=e,capture_output=True,text=True,timeout=15)
    assert p.returncode==0,p.stderr
    return p.stdout.rstrip('\n')


def remaining():
    with client(admin=True) as r:return sorted(r.scan_iter('di04000031_u5:*'))


def assert_runtime():
    with client(admin=True) as r:
        info=r.info('server');assert info['redis_version']==VERSION
        assert r.config_get('bind')['bind']=='127.0.0.1'
        assert r.config_get('save')['save']=='' and r.config_get('appendonly')['appendonly']=='no'
        assert 'off' in r.acl_getuser('default')['flags']
    with client() as r:assert r.ping()
    assert redis.__version__=='8.1.0'
    assert subprocess.check_output([str(CLI),'--version'],text=True).strip()=='redis-cli '+VERSION
    assert cli('PING')=='PONG'
    return {'server_version':VERSION,'cli_version':VERSION,'driver_version':redis.__version__,
            'authenticated':True,'private_loopback':True,'persistence_enabled':False,
            'public_database_endpoint':False,'single_instance':True,'modules_used':False,
            'ai_model_trained':False,'live_multi_database_integration':False,'performance_benchmark':False}


def run_program(source):
    with tempfile.TemporaryDirectory(prefix='redis-u5-') as folder:
        Path(folder,'lab.py').write_text((ROOT/'tools/redis_lab_runner.py').read_text())
        Path(folder,'example.py').write_text(source)
        p=subprocess.run([sys.executable,'example.py'],cwd=folder,env=env(),capture_output=True,text=True,timeout=20)
        if p.returncode:raise RuntimeError('Actual Redis example failed: '+p.stderr.replace(private()['lab'],'<private password>'))
        assert not p.stderr,p.stderr
        return p.stdout.rstrip('\n')


def P(id_,title,source,explanation):
    source='from lab import Lab, show\n\n'+source.strip()+'\n'
    return {'id':id_,'title':{'en':title},'code':{'en':source.rstrip()},
            'out':run_program(source),'expl':{'en':explanation}}


if __name__=='__main__':
    print(json.dumps(assert_runtime(),indent=2));print('Remaining scoped keys:',remaining())
