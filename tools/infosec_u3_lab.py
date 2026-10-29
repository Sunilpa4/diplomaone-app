"""Private, disposable OpenSSL lab for fixed educational examples.
No network, TLS server, public enrollment, identity vetting, OS trust installation
or persistent CA. All real private keys are fresh, mode0600 inside a temporary
mode0700 directory, never printed/exported, and deleted on context exit.
Trusted prepared examples only: this helper is NOT an arbitrary-code sandbox,
production CA, general certificate validator or replacement for a TLS stack.
"""
import calendar,datetime,os,re,subprocess,tempfile
from pathlib import Path
HOST='portal.diploma.test'

def openssl_version():
    return subprocess.run(['openssl','version'],check=True,text=True,
                          capture_output=True,timeout=5).stdout.strip()

class Lab:
    def __enter__(self):
        self.temp=tempfile.TemporaryDirectory(prefix='infosec-u3-')
        self.folder=Path(self.temp.name);self.folder.chmod(0o700)
        self.environment=dict(os.environ,LC_ALL='C',TZ='UTC')
        self.write('openssl.cnf','[req]\ndistinguished_name=dn\nprompt=no\n[dn]\nCN=Course Lab\n')
        self.environment['OPENSSL_CONF']=str(self.path('openssl.cnf'))
        self.ready=False
        return self

    def __exit__(self,*exception):
        self.temp.cleanup()

    def path(self,name):
        if not isinstance(name,str) or not re.fullmatch(r'[a-z][a-z0-9_.-]*',name):
            raise ValueError('Use a simple owned lab filename')
        return self.folder/name

    def write(self,name,data):
        path=self.path(name)
        if path.is_symlink():
            raise ValueError('Refusing a symbolic-link output')
        flags=os.O_WRONLY|os.O_CREAT|os.O_TRUNC
        fd=os.open(path,flags,0o600)
        with os.fdopen(fd,'wb') as f:
            f.write(data.encode() if isinstance(data,str) else data)
        return path

    def run(self,*args,check=True,input=None):
        result=subprocess.run(['openssl',*map(str,args)],cwd=self.folder,
            env=self.environment,input=input,capture_output=True,timeout=25)
        if check and result.returncode:
            raise RuntimeError('OpenSSL lab operation failed: '+str(args[0]))
        return result

    def rsa(self,alias):
        private=self.path(alias+'.key.pem')
        if not private.exists():
            # Precreate private output with restrictive permissions.
            self.write(private.name,b'')
            with private.open('wb') as output:
                result=subprocess.run(['openssl','genpkey','-algorithm','RSA',
                    '-pkeyopt','rsa_keygen_bits:2048','-pkeyopt','rsa_keygen_pubexp:65537'],
                    cwd=self.folder,env=self.environment,stdout=output,
                    stderr=subprocess.PIPE,timeout=25)
            if result.returncode:
                raise RuntimeError('Private lab RSA generation failed')
            private.chmod(0o600)
        return private

    def public(self,alias):
        target=self.path(alias+'.pub.pem')
        if not target.exists():
            self.run('pkey','-in',self.rsa(alias),'-pubout','-out',target)
        return target

    def public_facts(self,alias):
        text=self.run('pkey','-pubin','-in',self.public(alias),'-text','-noout').stdout.decode()
        bits=int(re.search(r'\((\d+) bit\)',text).group(1))
        exponent=int(re.search(r'Exponent: (\d+)',text).group(1))
        return {'bits':bits,'public_exponent':exponent}

    def request(self,alias,common_name,hostname=None):
        if not re.fullmatch(r'[A-Za-z0-9 ._-]{1,64}',common_name):
            raise ValueError('Use a fictional simple lab common name')
        args=['req','-new','-sha256','-key',self.rsa(alias),
              '-subj','/CN='+common_name,'-out',self.path(alias+'.csr.pem')]
        if hostname:
            if not re.fullmatch(r'[a-z0-9.-]+\.test',hostname):
                raise ValueError('Only reserved .test identities are used here')
            args+=['-addext','subjectAltName=DNS:'+hostname]
        self.run(*args)
        return self.path(alias+'.csr.pem')

    def request_valid(self,path,der=False):
        args=['req','-verify','-noout','-in',path]
        if der:args+=['-inform','DER']
        result=self.run(*args,check=False)
        text=(result.stdout+result.stderr).decode(errors='replace').lower()
        return result.returncode==0 and 'verify ok' in text

    def oaep_encrypt(self,message,alias='recipient'):
        self.write('message.bin',message)
        result=self.run('pkeyutl','-encrypt','-pubin','-inkey',self.public(alias),
            '-in',self.path('message.bin'),'-pkeyopt','rsa_padding_mode:oaep',
            '-pkeyopt','rsa_oaep_md:sha256','-pkeyopt','rsa_mgf1_md:sha256',check=False)
        return result

    def oaep_decrypt(self,cipher,alias='recipient'):
        self.write('cipher.bin',cipher)
        return self.run('pkeyutl','-decrypt','-inkey',self.rsa(alias),
            '-in',self.path('cipher.bin'),'-pkeyopt','rsa_padding_mode:oaep',
            '-pkeyopt','rsa_oaep_md:sha256','-pkeyopt','rsa_mgf1_md:sha256',check=False)

    def pss_sign(self,message,alias='signer'):
        self.write('signed.bin',message)
        result=self.run('dgst','-sha256','-sign',self.rsa(alias),
            '-sigopt','rsa_padding_mode:pss','-sigopt','rsa_mgf1_md:sha256',
            '-sigopt','rsa_pss_saltlen:digest',self.path('signed.bin'))
        return result.stdout

    def pss_verify(self,message,signature,alias='signer'):
        self.write('verify.bin',message);self.write('signature.bin',signature)
        result=self.run('dgst','-sha256','-verify',self.public(alias),
            '-signature',self.path('signature.bin'),'-sigopt','rsa_padding_mode:pss',
            '-sigopt','rsa_mgf1_md:sha256','-sigopt','rsa_pss_saltlen:digest',self.path('verify.bin'),check=False)
        return result.returncode==0 and b'Verified OK' in result.stdout

    def pki(self):
        if self.ready:return self
        self.run('req','-new','-x509','-sha256','-key',self.rsa('root'),
            '-subj','/CN=Course Root CA','-days','365','-set_serial','1',
            '-addext','basicConstraints=critical,CA:TRUE,pathlen:1',
            '-addext','keyUsage=critical,keyCertSign,cRLSign',
            '-addext','subjectKeyIdentifier=hash',
            '-out',self.path('root.cert.pem'))
        self.request('intermediate','Course Intermediate CA')
        self.write('intermediate.ext','''[issuer]
basicConstraints=critical,CA:TRUE,pathlen:0
keyUsage=critical,keyCertSign,cRLSign
subjectKeyIdentifier=hash
authorityKeyIdentifier=keyid,issuer
''')
        self.run('x509','-req','-sha256','-in',self.path('intermediate.csr.pem'),
            '-CA',self.path('root.cert.pem'),'-CAkey',self.rsa('root'),
            '-set_serial','2','-days','30','-extfile',self.path('intermediate.ext'),
            '-extensions','issuer','-out',self.path('intermediate.cert.pem'))
        self.path('newcerts').mkdir();self.write('index.txt','')
        self.write('serial','1000\n');self.write('crlnumber','1000\n')
        self.write('ca.cnf',f'''[ca]
default_ca=course_ca
[course_ca]
dir={self.folder.as_posix()}
database=$dir/index.txt
new_certs_dir=$dir/newcerts
certificate=$dir/intermediate.cert.pem
private_key=$dir/intermediate.key.pem
serial=$dir/serial
crlnumber=$dir/crlnumber
default_md=sha256
default_days=7
default_crl_days=2
policy=course_policy
copy_extensions=none
x509_extensions=leaf_ext
crl_extensions=crl_ext
[course_policy]
commonName=supplied
[leaf_ext]
basicConstraints=critical,CA:FALSE
keyUsage=critical,digitalSignature,keyEncipherment
extendedKeyUsage=serverAuth
subjectAltName=DNS:{HOST}
subjectKeyIdentifier=hash
authorityKeyIdentifier=keyid,issuer
[crl_ext]
authorityKeyIdentifier=keyid:always
''')
        self.request('leaf','Course Portal',HOST)
        self.run('ca','-batch','-notext','-config',self.path('ca.cnf'),
            '-in',self.path('leaf.csr.pem'),'-out',self.path('leaf.cert.pem'))
        self.ready=True
        return self

    def verify(self,certificate=None,hostname=HOST,purpose='sslserver',
               root=None,intermediate=True,attime=None,crl=None):
        self.pki()
        args=['verify','-CAfile',root or self.path('root.cert.pem'),
              '-no-CApath','-no-CAstore','-check_ss_sig','-x509_strict',
              '-purpose',purpose,'-verify_hostname',hostname]
        if intermediate:args+=['-untrusted',self.path('intermediate.cert.pem')]
        if attime is not None:args+=['-attime',str(attime)]
        if crl:args+=['-crl_check','-CRLfile',crl]
        args+=[certificate or self.path('leaf.cert.pem')]
        return self.run(*args,check=False)

    def expiry_epoch(self):
        self.pki()
        line=self.run('x509','-in',self.path('leaf.cert.pem'),'-noout','-enddate').stdout.decode().strip()
        value=line.split('=',1)[1]
        parsed=datetime.datetime.strptime(value,'%b %d %H:%M:%S %Y %Z')
        return calendar.timegm(parsed.timetuple())

    def unrelated_root(self):
        self.run('req','-new','-x509','-sha256','-key',self.rsa('unrelated'),
            '-subj','/CN=Course Unrelated Root','-days','365','-set_serial','3',
            '-addext','basicConstraints=critical,CA:TRUE',
            '-addext','keyUsage=critical,keyCertSign,cRLSign',
            '-out',self.path('unrelated.cert.pem'))
        return self.path('unrelated.cert.pem')

    def crl(self,revoke=False):
        self.pki()
        if revoke:
            self.run('ca','-batch','-config',self.path('ca.cnf'),
                '-revoke',self.path('leaf.cert.pem'),'-crl_reason','keyCompromise')
        path=self.path('intermediate.crl.pem')
        self.run('ca','-batch','-config',self.path('ca.cnf'),'-gencrl','-out',path)
        return path
