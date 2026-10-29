"""Explicit logical teaching models, NOT real switches, firewalls or IDS products.
No kernel networking or routes are changed. No packet is sent to model addresses.
Real TCP/TLS examples live in a separate helper and bind only owned loopback.
"""
from dataclasses import dataclass
from ipaddress import IPv4Address,IPv4Network
import hashlib,math

@dataclass(frozen=True)
class Flow:
    src:str
    dst:str
    sport:int
    dport:int
    proto:str='TCP'
    def __post_init__(self):
        object.__setattr__(self,'src',str(IPv4Address(self.src)))
        object.__setattr__(self,'dst',str(IPv4Address(self.dst)))
        if self.proto not in {'TCP','UDP'}:raise ValueError('Model supports TCP or UDP')
        if any(type(p) is not int or not 1<=p<=65535 for p in [self.sport,self.dport]):
            raise ValueError('Use valid nonzero transport ports')
    def reverse(self):return Flow(self.dst,self.src,self.dport,self.sport,self.proto)

@dataclass(frozen=True)
class Rule:
    name:str
    source:str
    destination:str
    proto:str
    dport:object
    action:str
    def __post_init__(self):
        IPv4Network(self.source);IPv4Network(self.destination)
        if self.proto not in {'ANY','TCP','UDP'} or self.action not in {'allow','deny'}:
            raise ValueError('Invalid teaching rule')
        if self.dport is not None and (type(self.dport) is not int or not 1<=self.dport<=65535):
            raise ValueError('Invalid destination port')
    def matches(self,flow):
        return (IPv4Address(flow.src) in IPv4Network(self.source)
            and IPv4Address(flow.dst) in IPv4Network(self.destination)
            and (self.proto=='ANY' or self.proto==flow.proto)
            and (self.dport is None or self.dport==flow.dport))

RULES=[
 Rule('outside-web','192.0.2.0/24','198.51.100.10/32','TCP',80,'allow'),
 Rule('inside-web','203.0.113.0/24','198.51.100.10/32','TCP',80,'allow'),
 Rule('app-db','198.51.100.10/32','203.0.113.20/32','TCP',5432,'allow')]

def decide(flow,rules=RULES):
    for rule in rules:
        if rule.matches(flow):return rule.action=='allow',rule.name
    return False,'default-deny'

class StatefulModel:
    """Tiny TCP direction/phase/TTL model, not RFC-complete TCP or netfilter.
    No sequence validation, retransmissions, fragments, NAT or kernel enforcement.
    A caller's claimed ESTABLISHED flag is not an accepted shortcut.
    """
    def __init__(self,rules=RULES,ttl=30):
        if not isinstance(ttl,(int,float)) or isinstance(ttl,bool) or not math.isfinite(ttl) or ttl<=0:raise ValueError('TTL must be finite and positive')
        self.rules=rules;self.ttl=ttl;self.sessions={};self.last_time=None
    def observe(self,flow,event,now):
        if flow.proto!='TCP' or event not in {'SYN','SYNACK','ACK','DATA','RST'}:
            raise ValueError('Unsupported model event')
        if not isinstance(now,(int,float)) or isinstance(now,bool) or not math.isfinite(now) or now<0 or (self.last_time is not None and now<self.last_time):raise ValueError('Use finite nondecreasing model time')
        self.last_time=now
        self.sessions={f:r for f,r in self.sessions.items() if r[1]>now}
        reverse=flow.reverse();origin=flow if flow in self.sessions else reverse if reverse in self.sessions else None
        if origin is None:
            if event=='SYN' and decide(flow,self.rules)[0]:
                self.sessions[flow]=('SYN_SENT',now+self.ttl);return True
            return False
        phase,expiry=self.sessions[origin]
        if event=='RST':self.sessions.pop(origin);return True
        if phase=='SYN_SENT' and flow==origin.reverse() and event=='SYNACK':
            self.sessions[origin]=('SYN_ACK',now+self.ttl);return True
        if phase=='SYN_ACK' and flow==origin and event=='ACK':
            self.sessions[origin]=('ESTABLISHED',now+self.ttl);return True
        if phase=='ESTABLISHED' and event in {'ACK','DATA'}:
            self.sessions[origin]=(phase,now+self.ttl);return True
        return False

def vlan_l2_allowed(left,right):
    for vid in [left,right]:
        if type(vid) is not int or not 1<=vid<=4094:raise ValueError('Use an ordinary VLAN ID')
    return left==right

def hids_check(path,trusted_digest):
    return hashlib.sha256(path.read_bytes()).hexdigest()!=trusted_digest

def nids_fixture_alert(record):
    """Alert on one fixed example policy pattern; not an intrusion verdict."""
    return record['zone']=='outside' and record['destination_port']==22

def confusion_counts(truth,predicted):
    if len(truth)!=len(predicted) or any(type(x) is not bool for x in truth+predicted):
        raise ValueError('Use equally sized boolean fixture labels')
    result={'TP':0,'FP':0,'FN':0,'TN':0}
    for expected,actual in zip(truth,predicted):
        result['TP' if expected and actual else 'FN' if expected else 'FP' if actual else 'TN']+=1
    return result
