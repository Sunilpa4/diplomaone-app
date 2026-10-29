"""Ten self-contained mobile SVGs for public-key, RSA and PKI concepts."""
from flowchart_lib import svg,text,arr,rbox,P
from diagrams_DI05007021_u1 import heading,foot,row,BLUE,BF,GREEN,GF,ORANGE,OF,PF,RED,RF
from subject_DI05007021 import DIAG_DIR
TITLES={'sec3_keys':'Public-Key Encryption Roles','sec3_hybrid':'Conceptual Hybrid Protection',
 'sec3_keygen':'Worked Textbook RSA Key','sec3_rsa':'RSA 65 to 2790 and Back',
 'sec3_signature':'Sign and Verify: Different from Encryption',
 'sec3_certificate':'Public Certificate Fields','sec3_enrollment':'Enrollment and CA/RA Roles',
 'sec3_chain':'Explicit Lab Trust Chain','sec3_validation':'Certificate Validation Checklist',
 'sec3_revocation':'Path Validity Is Not Non-Revocation'}

def chain(title,items,height,sub=None,footer=()):
 b=heading(title,sub)
 for i,(n,d) in enumerate(items):
  y=72+83*i
  if i:b+=arr([(180,y-23),(180,y)],P)
  b+=row(y,n,d,BF if i%2==0 else PF,BLUE if i%2==0 else P,60)
 b+=foot(height-45,*footer)
 return svg(360,height,b)

def keys():
 return chain('Encrypt for the intended recipient',[
  ('Authentic recipient public key','Public does not mean automatically genuine'),
  ('Appropriate encryption scheme','Sender encrypts the message'),
  ('Ciphertext','Not proof of sender identity'),
  ('Recipient private key + decryption','Keep real private material protected')],480,
  footer=('Different schemes are used for digital signatures.',))

def hybrid():
 return chain('Hybrid: roles, not a full protocol',[
  ('Public-key trust / establishment','Use an appropriate authenticated process'),
  ('Suitable symmetric key material','Protect lifecycle and protocol context'),
  ('Authenticated bulk encryption','Do not RSA-encrypt an unlimited file')],415,
  footer=('TLS 1.3 does not use RSA key transport.',
          'No live TLS or hybrid protocol is run here.'))

def keygen():
 return chain('RSA: PUBLIC small-number example',[
  ('Choose distinct toy primes','p=61, q=53'),('Compute modulus and totient','n=3233; phi=60*52=3120'),
  ('Choose e coprime to phi','e=17; gcd(17,3120)=1'),('Compute inverse exponent','d=2753; 17*2753 mod3120=1')],482,
  footer=('Real private parameters must not be published.',
          'These small values are not secure keys.'))

def rsa():
 return chain('Textbook RSA arithmetic only',[
  ('Numeric message m=65','Require 0 <= m < n'),('Encrypt with n3233, e17','65^17 mod3233 = 2790'),
  ('Decrypt with public demo d2753','2790^2753 mod3233 = 65')],414,
  footer=('Actual result, but no secure message padding.',
          'Real byte messages use a standardized scheme.'))

def signature():
 b=heading('Sign and verify, not private encryption')
 for i,(n,d) in enumerate([
  ('Message + private signing key','RSA-PSS/SHA-256 in the actual example'),
  ('Message and signature','The message is not thereby confidential'),
  ('Authentic public verification key','Check the exact message and scheme')]):
  y=68+88*i
  if i:b+=arr([(180,y-24),(180,y)],P)
  b+=row(y,n,d,BF if i%2==0 else PF,BLUE if i%2==0 else P,64)
 b+=rbox(90,373,144,56,'Original:\nvalid',GF,GREEN,12)
 b+=rbox(270,373,144,56,'Modified / wrong key:\ninvalid',RF,RED,10.5)
 b+=arr([(180,308),(180,328),(90,328),(90,345)],GREEN)
 b+=arr([(180,328),(270,328),(270,345)],RED)
 b+=foot(440,'Validity depends on trust and key control.',
              'Not an automatic human, truth or legal proof.')
 return svg(360,487,b)

def certificate():
 b=heading('Certificate: signed PUBLIC-key binding')
 data=[('Subject / relevant identity','Example SAN: portal.diploma.test'),
  ('Subject public-key information','Algorithm and public key, NOT private key'),
  ('Issuer / serial','Who issued it; issuer-scoped identifier'),
  ('Validity interval','notBefore and notAfter'),
  ('Constraints / usage / EKU','CA status and intended operations'),
  ('Issuer signature','Verify under the appropriate issuer key')]
 for i,(n,d) in enumerate(data):b+=row(66+75*i,n,d,BF if i%2==0 else PF,BLUE if i%2==0 else P,61)
 b+=foot(547,'Reading fields alone is not full validation.')
 return svg(360,581,b)

def enrollment():
 return chain('Obtaining a certificate: roles',[
  ('Generate/protect the key locally','Keep private material; create a signed CSR'),
  ('RA / CA identity and policy checks','CSR signature alone is not identity vetting'),
  ('CA certificate issuance','Approve attributes and sign under policy'),
  ('Application installation / lifecycle','Check chain, protect key, renew/revoke')],490,
  footer=('Real identity vetting is NOT performed here.',
          'Only disposable local issuing steps are run.'))

def trustchain():
 b=heading('Trust is configured, not self-proclaimed')
 b+=row(71,'Owned lab root: CA=TRUE','Explicitly supplied trust anchor only',BF,BLUE,70)
 b+=arr([(180,141),(180,183)],P)
 b+=row(183,'Intermediate: CA=TRUE, pathlen0','Signed by the root; constrained issuer',PF,P,70)
 b+=arr([(180,253),(180,295)],P)
 b+=row(295,'Leaf: CA=FALSE, serverAuth','SAN portal.diploma.test; signed by issuer',GF,GREEN,70)
 b+=foot(414,'Verify signatures, constraints and the full profile.',
              'No browser/OS root installation or public CA.')
 return svg(360,462,b)

def validation():
 return chain('Validation is more than one signature',[
  ('1. Trusted anchor and issuer path','Do not trust an arbitrary downloaded root'),
  ('2. Signatures and CA constraints','Include applicable critical extensions'),
  ('3. Validity interval','Use the proper evaluation time'),
  ('4. Intended identity and purpose','SAN hostname, key usage and EKU'),
  ('5. Required status policy','Use appropriate trusted/fresh status data'),
  ('6. Application/protocol checks','Offline validation is not a TLS handshake')],651,
  footer=('Do not bypass an error to force acceptance.',))

def revocation():
 b=heading('A valid path is not revocation status')
 b+=row(73,'Before local revocation','Supplied leaf CRL check succeeds',BF,BLUE,70)
 b+=row(174,'Revoke leaf and issue a new CRL','Actual CA database/status update',PF,P,70)
 b+=arr([(180,143),(180,174)],P)
 b+=arr([(180,244),(180,270),(90,270),(90,309)],GREEN)
 b+=arr([(180,270),(270,270),(270,309)],RED)
 b+=rbox(90,352,144,86,'Path only:\nstill valid\n(no CRL check)',GF,GREEN,11)
 b+=rbox(270,352,144,86,'Supplied CRL:\nrevoked rejected\n(error23)',RF,RED,10.8)
 b+=foot(438,'This demo checks only the leaf’s local CRL.',
              'No all-chain revocation, OCSP or live download.')
 return svg(360,488,b)

def main():
 DIAG_DIR.mkdir(parents=True,exist_ok=True)
 for n,draw in zip(TITLES,[keys,hybrid,keygen,rsa,signature,certificate,enrollment,trustchain,validation,revocation]):
  (DIAG_DIR/(n+'.svg')).write_text(draw())
 print('Unit 3 diagrams:',len(TITLES))

if __name__=='__main__':main()
