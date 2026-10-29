"""Small defensive teaching models: no scans, spoofing, malware or live targets."""
from urllib.parse import urlsplit
from ipaddress import IPv4Address
import math,re

def url_signals(value,expected_host='college.example.test'):
    """Parse hints only. NOT reputation, sender auth or a safe-URL guarantee."""
    if not isinstance(value,str) or any(ord(c)<32 or ord(c)>126 for c in value):
        raise ValueError('Use the fixed printable-ASCII URL fixtures')
    try:
        parsed=urlsplit(value);host=(parsed.hostname or '').lower();port=parsed.port
    except ValueError as error:
        raise ValueError('Malformed URL fixture') from error
    return {'https_scheme':parsed.scheme.lower()=='https',
            'exact_expected_host':host==expected_host.lower(),
            'userinfo_present':parsed.username is not None or parsed.password is not None,
            'expected_port':port in (None,443),
            'hostname':host,'authenticity_proven':False}

def arp_changes(reference,observed):
    """Compare fictional IPv4/MAC dictionaries; does not read/write ARP tables."""
    def normalize(mapping):
        out={}
        for ip,mac in mapping.items():
            address=str(IPv4Address(ip))
            if not isinstance(mac,str) or not re.fullmatch(r'(?:[0-9a-fA-F]{2}:){5}[0-9a-fA-F]{2}',mac):
                raise ValueError('Use a valid MAC representation')
            out[address]=mac.lower()
        return out
    reference=normalize(reference);observed=normalize(observed)
    return sorted(ip for ip,value in reference.items() if observed.get(ip)!=value)

class TokenBucket:
    """Synthetic-clock admission model, not a deployed rate limiter/DDoS test."""
    def __init__(self,capacity=2,refill=1):
        for v in [capacity,refill]:
            if type(v) not in (int,float) or not math.isfinite(v) or v<=0:
                raise ValueError('Use finite positive model parameters')
        self.capacity=capacity;self.refill=refill;self.tokens=float(capacity);self.last=0
    def allow(self,now):
        if type(now) not in (int,float) or not math.isfinite(now) or now<self.last:
            raise ValueError('Use finite nondecreasing model time')
        self.tokens=min(self.capacity,self.tokens+(now-self.last)*self.refill);self.last=now
        if self.tokens>=1:
            self.tokens-=1;return True
        return False
