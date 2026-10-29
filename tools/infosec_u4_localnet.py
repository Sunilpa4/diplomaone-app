"""Bounded application examples on owned IPv4 loopback only.
A tiny HTTP allow-list and a TLS1.3 byte relay: NOT a deployed firewall, WAF,
SOCKS/VPN/IPsec implementation, production proxy or kernel/network policy.
No public target, capture, scan, permanent service or host configuration change.
"""
import socket,ssl,struct,threading
try:
    from pki_lab import Lab,HOST
except ModuleNotFoundError:
    from infosec_u3_lab import Lab,HOST

def exact(conn,count):
    if not 0<=count<=1024:raise ValueError('Teaching frame exceeds limit')
    data=bytearray()
    while len(data)<count:
        part=conn.recv(count-len(data))
        if not part:raise ConnectionError('Incomplete teaching frame')
        data.extend(part)
    return bytes(data)

def send_frame(conn,data):
    if len(data)>1024:raise ValueError('Teaching frame exceeds limit')
    conn.sendall(struct.pack('!H',len(data))+data)

def read_frame(conn):return exact(conn,struct.unpack('!H',exact(conn,2))[0])

def listener():
    sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    try:sock.bind(('127.0.0.1',0));sock.listen(1);sock.settimeout(3)
    except Exception:sock.close();raise
    return sock

def private_http(path):
    if path not in {'/course','/admin'}:raise ValueError('Use the fixed teaching paths')
    errors=[]
    with listener() as server:
        address=server.getsockname()
        def serve():
            try:
                conn,_=server.accept()
                with conn:
                    conn.settimeout(3);header=bytearray()
                    while b'\r\n\r\n' not in header and len(header)<1024:
                        part=conn.recv(min(128,1024-len(header)))
                        if not part:break
                        header.extend(part)
                    allowed=(bytes(header).split(b'\r\n',1)[0]==b'GET /course HTTP/1.1'
                             and b'\r\n\r\n' in header and len(header)<=1024)
                    code,reason,body=(200,b'OK',b'OK') if allowed else (403,b'Forbidden',b'DENIED')
                    conn.sendall(b'HTTP/1.1 '+str(code).encode()+b' '+reason+b'\r\nContent-Length: '
                                 +str(len(body)).encode()+b'\r\nConnection: close\r\n\r\n'+body)
            except Exception as error:errors.append(type(error).__name__)
        worker=threading.Thread(target=serve);worker.start()
        try:
            with socket.create_connection(address,timeout=3) as client:
                client.sendall(('GET '+path+' HTTP/1.1\r\nHost: lab.test\r\n\r\n').encode())
                response=bytearray()
                while True:
                    part=client.recv(256)
                    if not part:break
                    response.extend(part)
                    if len(response)>2048:raise ValueError('Unexpected response size')
        finally:
            worker.join(4)
        assert not worker.is_alive() and not errors,errors
        status=int(bytes(response).split(b' ',2)[1])
    return {'status':status,'loopback_only':address[0]=='127.0.0.1',
            'listener_closed':server.fileno()==-1,'worker_stopped':not worker.is_alive()}

def private_tls_relay():
    errors=[];observed={}
    with Lab() as lab:
        lab.pki()
        chain=lab.write('serverchain.pem',lab.path('leaf.cert.pem').read_bytes()+lab.path('intermediate.cert.pem').read_bytes())
        incoming=ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
        incoming.minimum_version=incoming.maximum_version=ssl.TLSVersion.TLSv1_3
        incoming.load_cert_chain(chain,lab.rsa('leaf'))
        outgoing=ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
        outgoing.minimum_version=outgoing.maximum_version=ssl.TLSVersion.TLSv1_3
        outgoing.load_verify_locations(cafile=lab.path('root.cert.pem'))
        assert outgoing.check_hostname and outgoing.verify_mode==ssl.CERT_REQUIRED
        with listener() as backend,listener() as relay:
            backend_address=backend.getsockname();relay_address=relay.getsockname()
            def backend_once():
                try:
                    conn,_=backend.accept()
                    with conn:
                        conn.settimeout(3);send_frame(conn,read_frame(conn))
                except Exception as error:errors.append(type(error).__name__)
            def relay_once():
                try:
                    raw,_=relay.accept();raw.settimeout(3)
                    try:
                        with incoming.wrap_socket(raw,server_side=True) as secure:
                            message=read_frame(secure)
                            with socket.create_connection(backend_address,timeout=3) as target:
                                send_frame(target,message);answer=read_frame(target)
                            send_frame(secure,answer)
                    finally:raw.close()
                except Exception as error:errors.append(type(error).__name__)
            workers=[threading.Thread(target=backend_once),threading.Thread(target=relay_once)]
            for w in workers:w.start()
            try:
                raw=socket.create_connection(relay_address,timeout=3)
                try:
                    with outgoing.wrap_socket(raw,server_hostname=HOST) as client:
                        message=b'NETWORK-SECURITY'
                        send_frame(client,message);answer=read_frame(client)
                        observed={'tls_version':client.version(),
                                  'echo_matches':answer==message,'checked_hostname':HOST,
                                  'certificate_required':outgoing.verify_mode==ssl.CERT_REQUIRED}
                finally:raw.close()
            finally:
                for w in workers:w.join(4)
            assert not any(w.is_alive() for w in workers) and not errors,errors
        observed.update({'loopback_only':backend_address[0]==relay_address[0]=='127.0.0.1',
                         'listeners_closed':backend.fileno()==relay.fileno()==-1,
                         'workers_stopped':not any(w.is_alive() for w in workers)})
        folder=lab.folder
    observed['temporary_keys_removed']=not folder.exists()
    return observed
