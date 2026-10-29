"""Ten self-contained mobile diagrams for classical/symmetric cryptography."""
from flowchart_lib import svg,text,arr,rbox,P
from diagrams_DI05007021_u1 import heading,foot,row,BLUE,BF,GREEN,GF,ORANGE,OF,PF,RED,RF
from subject_DI05007021 import DIAG_DIR
from infosec_u2_ciphers import playfair_square,rail_pattern
TITLES={'sec2_model':'Symmetric Encryption Model','sec2_substitution':'Cipher Classification',
 'sec2_vigenere':'Vigenere Worked Alignment','sec2_playfair':'Playfair Square and Rectangle',
 'sec2_hill':'Hill Column-Vector Calculation','sec2_otp':'One-Time-Pad Conditions',
 'sec2_rail':'Three-Rail Zigzag and Row Readout','sec2_stego':'Synthetic LSB Carrier Example',
 'sec2_des':'Historical DES Overall Structure','sec2_feistel':'DES Round Function and Key Sizes'}

def chain(title,items,height,subtitle=None,footer=()):
 b=heading(title,subtitle)
 for i,(name,detail) in enumerate(items):
  y=72+83*i
  if i:b+=arr([(180,y-23),(180,y)],P)
  b+=row(y,name,detail,BF if i%2==0 else PF,BLUE if i%2==0 else P,60)
 b+=foot(height-44,*footer)
 return svg(360,height,b)

def model():
 return chain('Symmetric: shared secret material',[
  ('Plaintext P','Prepare according to the declared convention'),
  ('Encrypt E_K','Sender uses secret key material'),('Ciphertext C','May be displayed as hexadecimal or letters'),
  ('Decrypt D_K','Receiver uses the corresponding secret'),('Recovered prepared P','Not automatically original text formatting')],550,
  footer=('Encryption alone does not authenticate.',))

def classification():
 b=heading('Do not mix up these classifications')
 rows=[('Monoalphabetic','Fixed symbol mapping: Caesar/permutation'),
       ('Polyalphabetic','Mapping varies by position: Vigenere'),
       ('Polygraphic','Pairs/blocks: Playfair and Hill'),
       ('Transposition','Reorders positions: rail fence')]
 for i,(n,d) in enumerate(rows):b+=row(64+88*i,n,d,BF if i%2==0 else PF,BLUE if i%2==0 else P,68)
 b+=foot(459,'These classical methods are teaching examples.',
              'They are not modern protection for real secrets.')
 return svg(360,505,b)

def vigenere():
 b=heading('Vigenere: add repeated-key shifts','A=0, B=1, ..., Z=25')
 for i,(label,value,color,fill) in enumerate([
   ('Plaintext','A T T A C K A T D A W N',BLUE,BF),
   ('Repeated key','L E M O N L E M O N L E',P,PF),
   ('Ciphertext','L X F O P V E F R N H R',GREEN,GF)]):
  y=76+100*i;b+=row(y,label,'',fill,color,76)
  b+=text(180,y+52,value,12,mono=True)
 b+=rbox(180,403,324,54,'C_i = (P_i + K_i) mod26',OF,ORANGE,12,mono=True)
 b+=foot(465,'Subtract key shifts to decrypt.',
              'Repeating LEMON is not a one-time pad.')
 return svg(360,510,b)

def playfair():
 b=heading('Playfair: HI becomes BM','Key PLAYFAIREXAMPLE; I/J merged')
 square=playfair_square('PLAYFAIREXAMPLE');x0=65;y0=87;cell=46
 for i,c in enumerate(square):
  r,col=divmod(i,5);x=x0+col*cell;y=y0+r*cell
  fill,color=(BF,BLUE) if c in 'HI' else (GF,GREEN) if c in 'BM' else ('#FAF7FD','#D8C9E8')
  b+=f'<rect x="{x}" y="{y}" width="{cell}" height="{cell}" fill="{fill}" stroke="{color}" stroke-width="1.4"/>'
  b+=text(x+cell/2,y+cell/2,c,18,color=color if c in 'HIBM' else '#333',weight='bold')
 b+=rbox(180,365,324,52,'Rectangle: keep each letter\'s row; swap columns',PF,P,10.8)
 b+=foot(420,'Same row: right; same column: down.',
              'Decrypt with left/up, or the same rectangle rule.',
              'Preserve the declared I/J and filler conventions.')
 return svg(360,486,b)

def hill():
 b=heading('Hill: multiply COLUMN vectors','K = [[3,3],[2,5]], A=0')
 data=[('HE -> [7,4]^T','Use two-letter blocks'),
       ('K * P = [33,34]^T','[3*7+3*4, 2*7+5*4]'),
       ('mod26 -> [7,8]^T -> HI','LP similarly becomes AT; HELP -> HIAT')]
 for i,(n,d) in enumerate(data):
  y=78+104*i
  if i:b+=arr([(180,y-32),(180,y)],P)
  b+=row(y,n,d,BF if i%2==0 else PF,BLUE if i%2==0 else P,72)
 b+=foot(424,'det(K)=9; gcd(9,26)=1.',
              'K^-1 = [[15,17],[20,9]] mod26.',
              'A nonzero determinant alone is not enough.')
 return svg(360,493,b)

def otp():
 b=heading('OTP: conditions, not just key length')
 b+=row(65,'Independent + uniformly random','Secret pad material, not a repeated phrase',BF,BLUE,68)
 b+=row(150,'Pad at least as long as the message','Use each pad portion only once',PF,P,68)
 b+=row(235,'HELLO + XMCKL -> EQNVZ','Public fixed arithmetic example only',GF,GREEN,68)
 b+=rbox(180,365,324,70,'Reused XOR pad:\nC1 XOR C2 = P1 XOR P2',OF,ORANGE,12)
 b+=foot(433,'The public sample does not prove perfect secrecy.',
              'Ideal confidentiality still does not authenticate.')
 return svg(360,480,b)

def rail():
 plain='WEAREDISCOVEREDRUNATONCE';pattern=rail_pattern(len(plain),3)
 b=heading('Rail fence: write zigzag, read rows','Three rails; letters are not substituted')
 for r in range(3):
  b+=text(11,112+r*38,str(r),10,color='#666')
  for i,c in enumerate(plain):
   b+=text(25+i*13,112+r*38,c if pattern[i]==r else '.',11,mono=True,color=P if pattern[i]==r else '#CCC')
 y=243
 for r in range(3):
  letters=''.join(c for c,p in zip(plain,pattern) if p==r)
  b+=row(y+r*76,'Rail '+str(r),letters,BF if r%2==0 else PF,BLUE if r%2==0 else P,61)
 b+=foot(493,'WECRUO + ERDSOEERNTNE + AIVDAC',
              'Reconstruct per-rail counts to decrypt.',
              'No padding or letter changes are needed here.')
 return svg(360,560,b)

def stego():
 b=heading('LSB illustration: synthetic RGB bytes')
 b+=row(64,'Carrier byte: 120','01111000 (last bit 0)',BF,BLUE,68)
 b+=arr([(180,132),(180,167)],P)
 b+=row(167,'Embed the teaching bit 1','01111001 -> 121 (change of 1)',PF,P,68)
 b+=row(268,'8x8 RGB -> 192 channel bytes','Header 16 bits + GTU 24 bits = 40 bits',GF,GREEN,71)
 b+=foot(387,'Actual extraction recovers the public text GTU.',
              'Raw byte fixture, not a PNG/JPEG editor.',
              'Not encryption, authentication or invisibility proof.')
 return svg(360,456,b)

def des():
 return chain('DES: historical 64-bit block cipher',[
  ('Initial permutation IP','Input block: 64 bits'),('Split L0 / R0','32 bits in each half'),
  ('16 Feistel rounds','Sixteen 48-bit subkeys from 56 key bits'),
  ('Final swap: R16 || L16','Combine into 64 bits'),('Inverse IP','Output ciphertext: 64 bits')],560,
  subtitle='Withdrawn: do not deploy for real protection',
  footer=('Decrypt by reversing the round-key order.',))

def feistel():
 b=heading('DES f: 32 bits in, 32 bits out')
 for i,(n,d) in enumerate([
  ('Expansion E: 32 -> 48','Expand the previous right half'),('XOR with K_i: 48 bits','Round-key mixing'),
  ('Eight S-boxes: 8 x (6 -> 4)','Combined output: 32 bits'),('Permutation P: 32 -> 32','Feed the Feistel XOR with the left half')]):
  y=65+86*i
  if i:b+=arr([(180,y-22),(180,y)],P)
  b+=row(y,n,d,BF if i%2==0 else PF,BLUE if i%2==0 else P,64)
 b+=rbox(180,461,324,70,'Key: 64 representation bits -> PC-1: 56\n28+28 rotations -> PC-2: 48 per round',OF,ORANGE,10.8)
 b+=foot(526,'The extra eight key bits are parity, not strength.',
              'S-box row: outer bits; column: inner four bits.')
 return svg(360,573,b)

def main():
 DIAG_DIR.mkdir(parents=True,exist_ok=True)
 for name,draw in zip(TITLES,[model,classification,vigenere,playfair,hill,otp,rail,stego,des,feistel]):
  (DIAG_DIR/(name+'.svg')).write_text(draw())
 print('Unit 2 diagrams:',len(TITLES))

if __name__=='__main__':main()
