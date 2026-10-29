"""Independent historical DES cross-check, using public/seeded test fixtures only."""
import random,subprocess
from infosec_u2_ciphers import des_block

def check_des():
 version=subprocess.run(['openssl','version'],check=True,text=True,capture_output=True,timeout=5).stdout.strip()
 rng=random.Random(202627)  # Reproducible TEST data, never production keys.
 fixtures=[(bytes.fromhex('133457799BBCDFF1'),bytes.fromhex('0123456789ABCDEF')),
           (bytes(8),bytes(8))]
 fixtures += [(rng.randbytes(8),rng.randbytes(64)) for _ in range(8)]
 blocks=0
 for key,plain in fixtures:
  cmd=['openssl','enc','-des-ecb','-provider','default','-provider','legacy',
       '-K',key.hex(),'-nosalt','-nopad']
  actual=subprocess.run(cmd,input=plain,capture_output=True,check=True,timeout=5)
  assert not actual.stderr
  expected=b''.join(des_block(plain[i:i+8],key) for i in range(0,len(plain),8))
  assert actual.stdout==expected,'Independent DES encryption mismatch'
  recovered=subprocess.run(cmd+['-d'],input=expected,capture_output=True,check=True,timeout=5)
  assert not recovered.stderr and recovered.stdout==plain
  assert b''.join(des_block(expected[i:i+8],key,True) for i in range(0,len(expected),8))==plain
  blocks+=len(plain)//8
 assert des_block(fixtures[0][1],fixtures[0][0]).hex().upper()=='85E813540F0AB405'
 assert des_block(bytes(8),bytes(8)).hex().upper()=='8CA64DE9C1B123A7'
 return {'engine':'OpenSSL','version':version,'historical_cipher':'DES-ECB for block comparison only',
         'compared_blocks':blocks,'directions':['encrypt','decrypt'],
         'fixtures':'Two known/public vectors and eight seeded 8-block test cases',
         'legacy_provider_scope':'Explicit per-process flags only; no system-wide configuration changed',
         'certification_claim':False}
