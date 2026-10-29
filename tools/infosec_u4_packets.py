"""Construct a small SYNTHETIC Ethernet PCAP; no sockets/capture/network used.
The 16 frames use documentation-only IPv4 addresses, local fake MAC addresses,
reserved .test DNS, and harmless ARP/DNS/HTTP/VLAN data. This is NOT live traffic
or Packet Tracer output. TShark only dissects the owned file offline with -n -r.
"""
import ipaddress,os,struct,subprocess,tempfile
from pathlib import Path

HOST='portal.diploma.test'
CLIENT='192.0.2.10';DNS='192.0.2.53';WEB='198.51.100.10'
MAC_C=bytes.fromhex('020000000010');MAC_D=bytes.fromhex('020000000053');MAC_W=bytes.fromhex('020000000020')

def checksum(data):
    if len(data)%2:data+=b'\0'
    total=sum(struct.unpack('!%dH'%(len(data)//2),data))
    while total>>16:total=(total&65535)+(total>>16)
    return (~total)&65535

def ipv4_bytes(address):return ipaddress.IPv4Address(address).packed

def ethernet(payload,source,destination,kind=0x0800,vlan=None):
    if vlan is None:header=destination+source+struct.pack('!H',kind)
    else:
        if type(vlan) is not int or not 1<=vlan<=4094:raise ValueError('Use an ordinary VLAN ID')
        header=destination+source+struct.pack('!HHH',0x8100,vlan,kind)
    frame=header+payload
    return frame+b'\0'*max(0,60-len(frame))

def ipv4(payload,source,destination,protocol,ident):
    header=struct.pack('!BBHHHBBH4s4s',0x45,0,20+len(payload),ident,0x4000,64,protocol,0,ipv4_bytes(source),ipv4_bytes(destination))
    return header[:10]+struct.pack('!H',checksum(header))+header[12:]+payload

def transport(payload,source,destination,sport,dport,protocol,seq=0,ack=0,flags=0x10):
    if protocol==17:
        header=struct.pack('!HHHH',sport,dport,8+len(payload),0);offset=6
    elif protocol==6:
        header=struct.pack('!HHIIBBHHH',sport,dport,seq,ack,0x50,flags,32768,0,0);offset=16
    else:raise ValueError('Only TCP/UDP teaching frames are built')
    pseudo=ipv4_bytes(source)+ipv4_bytes(destination)+struct.pack('!BBH',0,protocol,len(header)+len(payload))
    value=checksum(pseudo+header+payload)
    if protocol==17 and value==0:value=65535
    return header[:offset]+struct.pack('!H',value)+header[offset+2:]+payload

def qname(name):return b''.join(bytes([len(p)])+p.encode('ascii') for p in name.split('.'))+b'\0'

def fixture_frames():
    frames=[]
    arp_prefix=struct.pack('!HHBB',1,0x0800,6,4)
    request=arp_prefix+struct.pack('!H',1)+MAC_C+ipv4_bytes(CLIENT)+bytes(6)+ipv4_bytes(DNS)
    reply=arp_prefix+struct.pack('!H',2)+MAC_D+ipv4_bytes(DNS)+MAC_C+ipv4_bytes(CLIENT)
    frames+=[ethernet(request,MAC_C,b'\xff'*6,0x0806),ethernet(reply,MAC_D,MAC_C,0x0806)]
    question=qname(HOST)+struct.pack('!HH',1,1)
    query=struct.pack('!HHHHHH',0x1234,0x0100,1,0,0,0)+question
    response=struct.pack('!HHHHHH',0x1234,0x8180,1,1,0,0)+question+b'\xc0\x0c'+struct.pack('!HHIH',1,1,60,4)+ipv4_bytes(WEB)
    def add(data,source,dest,sport,dport,proto,seq=0,ack=0,flags=0x10,vlan=None):
        segment=transport(data,source,dest,sport,dport,proto,seq,ack,flags)
        packet=ipv4(segment,source,dest,proto,100+len(frames))
        a,b=(MAC_C,MAC_D) if dest==DNS else (MAC_D,MAC_C) if source==DNS else (MAC_C,MAC_W) if source==CLIENT else (MAC_W,MAC_C)
        frames.append(ethernet(packet,a,b,vlan=vlan))
    add(query,CLIENT,DNS,53000,53,17);add(response,DNS,CLIENT,53,53000,17)
    req=b'GET /course HTTP/1.1\r\nHost: portal.diploma.test\r\n\r\n'
    rsp=b'HTTP/1.1 200 OK\r\nContent-Length: 2\r\n\r\nOK'
    cn=1001+len(req);sn=2001+len(rsp)
    add(b'',CLIENT,WEB,50000,80,6,1000,0,0x02)
    add(b'',WEB,CLIENT,80,50000,6,2000,1001,0x12)
    add(b'',CLIENT,WEB,50000,80,6,1001,2001)
    add(req,CLIENT,WEB,50000,80,6,1001,2001,0x18)
    add(rsp,WEB,CLIENT,80,50000,6,2001,cn,0x18)
    add(b'',CLIENT,WEB,50000,80,6,cn,sn)
    add(b'',CLIENT,WEB,50000,80,6,cn,sn,0x11)
    add(b'',WEB,CLIENT,80,50000,6,sn,cn+1)
    add(b'',WEB,CLIENT,80,50000,6,sn,cn+1,0x11)
    add(b'',CLIENT,WEB,50000,80,6,cn+1,sn+1)
    for vid,a,b in [(10,'203.0.113.10','203.0.113.11'),(20,'203.0.113.20','203.0.113.21')]:
        add(('VLAN'+str(vid)).encode(),a,b,40000,9000,17,vlan=vid)
    assert len(frames)==16
    return frames

def pcap_bytes():
    # Fixed teaching timestamps, not a claimed real capture time.
    out=bytearray(struct.pack('<IHHIIII',0xa1b2c3d4,2,4,0,0,65535,1))
    for i,frame in enumerate(fixture_frames()):
        out+=struct.pack('<IIII',1793275200,i*20000,len(frame),len(frame))+frame
    return bytes(out)

def tshark_version():
    return subprocess.run(['tshark','--version'],check=True,text=True,capture_output=True,timeout=10).stdout.splitlines()[0]

def dissect(fields,display_filter=None,raw=None):
    with tempfile.TemporaryDirectory(prefix='infosec-u4-pcap-') as td:
        folder=Path(td);path=folder/'synthetic.pcap';path.write_bytes(pcap_bytes() if raw is None else raw)
        env=dict(os.environ,LC_ALL='C',TZ='UTC',WIRESHARK_CONFIG_DIR=str(folder/'profile'))
        cmd=['tshark','-n','-r',str(path),'-o','ip.check_checksum:TRUE',
             '-o','tcp.check_checksum:TRUE','-o','udp.check_checksum:TRUE']
        if display_filter:cmd+=['-Y',display_filter]
        cmd+=['-T','fields','-E','separator=|','-E','occurrence=f']
        for name in fields:cmd+=['-e',name]
        result=subprocess.run(cmd,check=True,text=True,capture_output=True,timeout=20,env=env)
        if result.stderr:raise RuntimeError('Unexpected offline TShark diagnostic')
        return [line.split('|') for line in result.stdout.splitlines() if line]
