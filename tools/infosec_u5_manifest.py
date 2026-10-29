"""Verify frozen OFFICIAL SIGNED METADATA in an isolated GPG home.
No downloads, keyservers, ISO verification, Kali installation or OS boot occur.
The primary fingerprint pin was compared with Kali's official documentation on
2026-10-29. A valid metadata signature does NOT verify missing ISO bytes.
"""
from pathlib import Path
import re,subprocess,tempfile,os
PRIMARY='827C8569F2518CC677FECA1AED65462EC8D5E4C5'
INSTALLER='kali-linux-2026.3-installer-amd64.iso'

def verify_manifest(folder,expected_primary=PRIMARY):
    if not re.fullmatch(r'[0-9A-F]{40}',expected_primary):
        raise ValueError('Use an explicit 40-hex primary fingerprint pin')
    folder=Path(folder)
    with tempfile.TemporaryDirectory(prefix='infosec-u5-gpg-') as td:
        home=Path(td);home.chmod(0o700)
        env=dict(os.environ,LC_ALL='C',TZ='UTC')
        base=['gpg','--no-options','--batch','--no-tty','--no-autostart',
              '--no-auto-key-retrieve','--auto-key-locate','clear','--homedir',td]
        shown=subprocess.run(base+['--with-colons','--show-keys',str(folder/'kali-archive-key.asc')],
            text=True,capture_output=True,env=env,timeout=15,check=True)
        primaries=[];next_primary=False
        for line in shown.stdout.splitlines():
            parts=line.split(':')
            if parts[0]=='pub':next_primary=True
            elif parts[0]=='sub':next_primary=False
            elif parts[0]=='fpr' and next_primary:
                primaries.append(parts[9]);next_primary=False
        if expected_primary not in primaries:
            raise ValueError('Public key does not match the documented primary pin')
        subprocess.run(base+['--import',str(folder/'kali-archive-key.asc')],
            text=True,capture_output=True,env=env,timeout=15,check=True)
        verified=subprocess.run(base+['--status-fd','1','--verify',str(folder/'SHA256SUMS.gpg'),str(folder/'SHA256SUMS')],
            text=True,capture_output=True,env=env,timeout=15)
        statuses=[line.split() for line in verified.stdout.splitlines() if line.startswith('[GNUPG:] ')]
        bad={'BADSIG','ERRSIG','EXPSIG','EXPKEYSIG','REVKEYSIG','KEYEXPIRED','SIGEXPIRED'}
        valid=[s for s in statuses if len(s)>2 and s[1]=='VALIDSIG' and expected_primary in (s[2],s[-1])]
        if verified.returncode!=0 or not valid or any(s[1] in bad for s in statuses):
            raise ValueError('Pinned manifest signature verification failed')
        lines=[]
        for line in (folder/'SHA256SUMS').read_text().splitlines():
            pieces=line.split()
            if len(pieces)==2 and pieces[1].lstrip('*')==INSTALLER:
                if not re.fullmatch(r'[0-9a-fA-F]{64}',pieces[0]):
                    raise ValueError('Malformed manifest digest')
                lines.append(pieces[0].lower())
        if len(lines)!=1:raise ValueError('Expected one explicit installer manifest entry')
        result={'signature_valid':True,'primary_fingerprint':expected_primary,
                'release':'2026.3','installer_filename':INSTALLER,
                'published_installer_sha256':lines[0],
                'ISO_downloaded_or_verified':False,'Kali_booted':False}
    result['isolated_keyring_removed']=not home.exists()
    return result
