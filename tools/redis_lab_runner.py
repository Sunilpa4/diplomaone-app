"""Shared helper for trusted short Redis examples; never a Python sandbox.
Connect to YOUR private Redis; allocate a fresh key namespace, refuse collisions,
claim it with SET NX, and clean only its declared keys while watching ownership.
"""
import getpass,json,os,re,uuid
import redis


def client():
    password=os.environ.get('REDIS_PASSWORD')
    if password is None:password=getpass.getpass('Your Redis password (hidden): ') or None
    return redis.Redis(host=os.environ.get('REDIS_HOST','127.0.0.1'),
        port=int(os.environ.get('REDIS_PORT','6379')),
        username=os.environ.get('REDIS_USERNAME') or None,password=password,
        ssl=os.environ.get('REDIS_TLS','0')=='1',decode_responses=True,
        protocol=2,socket_connect_timeout=5,socket_timeout=5)


def normalize(value):
    if isinstance(value,redis.exceptions.ResponseError):return {'server_error':str(value)}
    if isinstance(value,dict):return {k:normalize(value[k]) for k in sorted(value)}
    if isinstance(value,(list,tuple)):return [normalize(v) for v in value]
    if isinstance(value,set):return sorted(normalize(v) for v in value)
    return value


def show(label,value):print(label+': '+json.dumps(normalize(value),ensure_ascii=False,separators=(',',':')))


class Lab:
    def __init__(self,name,keys,*,connection=None,suffix=None):
        if not re.fullmatch(r'[a-z0-9_]{1,32}',name):raise ValueError('Invalid prepared lab name')
        if len(set(keys))!=len(keys) or not keys:raise ValueError('Declare unique data-key names')
        if any(not re.fullmatch(r'[a-zA-Z0-9:_-]{1,48}',k) or k=='__owner' for k in keys):
            raise ValueError('Invalid/reserved data-key name')
        suffix=suffix or uuid.uuid4().hex
        if not re.fullmatch(r'[a-z0-9_]{1,48}',suffix):raise ValueError('Invalid scope suffix')
        self.prefix='di04000031_u5:'+name+':'+suffix+':'
        self.keys={k:self.prefix+k for k in keys};self.owner=self.prefix+'__owner'
        self.token=uuid.uuid4().hex;self.r=connection;self.external=connection is not None;self.owned=False

    def key(self,name):return self.keys[name]

    def __enter__(self):
        if self.r is None:self.r=client()
        try:
            self.r.ping()
            if self.r.exists(self.owner,*self.keys.values()):raise RuntimeError('Existing scope refused; nothing deleted')
            if not self.r.set(self.owner,self.token,nx=True):raise RuntimeError('Scope claim failed; nothing deleted')
            self.owned=True;return self
        except BaseException:
            if not self.external:self.r.close()
            raise

    def __exit__(self,kind,error,traceback):
        try:
            if self.owned:
                with self.r.pipeline() as pipe:
                    pipe.watch(self.owner)
                    if pipe.get(self.owner)!=self.token:raise RuntimeError('Scope ownership changed; inspect, do not delete')
                    pipe.multi();pipe.delete(*self.keys.values());pipe.delete(self.owner)
                    result=pipe.execute()
                    if result[-1]!=1:raise RuntimeError('Scope claim cleanup not confirmed')
                self.owned=False
        finally:
            if not self.external:self.r.close()
        return False
