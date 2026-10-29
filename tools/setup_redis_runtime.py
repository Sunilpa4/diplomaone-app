"""Private checksum-pinned Redis 8.10.3 core/CLI reference; no public service.
Build only core/CLI from official source; optional modules/TLS are not enabled.
Cache, ACLs and secrets stay outside the project; use the process tool to start.
"""
import hashlib,json,os
from pathlib import Path
import secrets,subprocess,tarfile,urllib.request

CACHE=Path.home()/'.cache/diplomaone-redis-u5'
VERSION='8.10.3'
SOURCE=CACHE/('redis-'+VERSION)
SERVER=SOURCE/'src/redis-server';CLI=SOURCE/'src/redis-cli'
CREDS=CACHE/'credentials.json'
SHA256='edde778f6bdee7581e42fc139ca9e07e2822212092f7501f99989656e3629d02'
URL='https://download.redis.io/releases/redis-'+VERSION+'.tar.gz'


def main():
    CACHE.mkdir(parents=True,exist_ok=True);CACHE.chmod(0o700)
    archive=CACHE/('redis-'+VERSION+'.tar.gz')
    if not archive.exists():
        request=urllib.request.Request(URL,headers={'User-Agent':'Mozilla/5.0','Accept':'application/octet-stream'})
        with urllib.request.urlopen(request,timeout=60) as response:archive.write_bytes(response.read())
    assert hashlib.sha256(archive.read_bytes()).hexdigest()==SHA256,'Official source checksum mismatch'
    if not SOURCE.exists():
        with tarfile.open(archive) as source:source.extractall(CACHE,filter='data')
    if not SERVER.exists() or not CLI.exists():
        subprocess.run(['make','-C',str(SOURCE/'src'),'-j2','redis-server','redis-cli',
                        'MALLOC=libc','OPTIMIZATION=-O2','BUILD_TLS=no'],check=True)
    if not CREDS.exists():
        fd=os.open(CREDS,os.O_CREAT|os.O_EXCL|os.O_WRONLY,0o600)
        with os.fdopen(fd,'w') as file:json.dump({'admin':secrets.token_urlsafe(36),'lab':secrets.token_urlsafe(36)},file)
    assert CREDS.stat().st_mode & 0o777==0o600
    private=json.loads(CREDS.read_text());hashed=lambda value:hashlib.sha256(value.encode()).hexdigest()
    commands='ping get set del exists type incr incrby expire ttl rpush lpush lrange llen lpop rpop sadd smembers scard sismember srem hset hget hgetall hdel hexists multi exec discard watch unwatch'.split()
    acl=['user default off','user u5_admin on #'+hashed(private['admin'])+' ~* &* +@all',
         'user u5_lab on #'+hashed(private['lab'])+' ~di04000031_u5:* '+ ' '.join('+'+c for c in commands)+' +client|setinfo']
    aclfile=CACHE/'users.acl';aclfile.write_text('\n'.join(acl)+'\n');aclfile.chmod(0o600)
    conf='\n'.join(['bind 127.0.0.1','protected-mode yes','port 6385','daemonize no','logfile ""',
        'save ""','appendonly no','dir '+str(CACHE),'aclfile '+str(aclfile),
        'maxmemory 32mb','maxmemory-policy noeviction','databases 1'])+'\n'
    (CACHE/'redis.conf').write_text(conf)
    print(subprocess.check_output([str(SERVER),'--version'],text=True).strip())
    print(subprocess.check_output([str(CLI),'--version'],text=True).strip())
    print('Verified source SHA256:',SHA256)
    print('Private ACL credentials created/retained; not displayed or exported.')
    print('Foreground command:',SERVER,CACHE/'redis.conf')


if __name__=='__main__':main()
