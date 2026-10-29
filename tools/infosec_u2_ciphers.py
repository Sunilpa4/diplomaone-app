"""Classroom ciphers, exported as ciphers.py. NOT production cryptography.

Classical text uses ASCII letters, uppercases and removes whitespace. Other
characters are rejected, not silently discarded. Playfair additionally merges
J into I and returns its prepared text; Hill returns explicit padded text.
No function guesses away fillers/padding. DES is a withdrawn historical cipher.
Only fixed educational data and in-memory byte carriers are used by examples.
"""
import math
import string
ALPHABET=string.ascii_uppercase

def letters(text):
    if not isinstance(text,str):
        raise TypeError('Text must be a string')
    if any(c not in string.ascii_letters and c not in ' \t\r\n' for c in text):
        raise ValueError('Use ASCII letters and whitespace only')
    return ''.join(c for c in text.upper() if c in ALPHABET)

def integer(value,label):
    if type(value) is not int:
        raise TypeError(label+' must be an integer')
    return value

def caesar(text,shift):
    shift=integer(shift,'Shift')%26
    return ''.join(ALPHABET[(ord(c)-65+shift)%26] for c in letters(text))

def substitution(text,alphabet,decrypt=False):
    alphabet=letters(alphabet)
    if len(alphabet)!=26 or set(alphabet)!=set(ALPHABET):
        raise ValueError('Alphabet must be a permutation of A-Z')
    source,target=(alphabet,ALPHABET) if decrypt else (ALPHABET,alphabet)
    return letters(text).translate(str.maketrans(source,target))

def vigenere(text,key,decrypt=False):
    text=letters(text);key=letters(key)
    if not key:
        raise ValueError('Key must not be empty')
    direction=-1 if decrypt else 1
    return ''.join(ALPHABET[(ord(c)-65+direction*(ord(key[i%len(key)])-65))%26]
                   for i,c in enumerate(text))

def playfair_square(key):
    key=letters(key).replace('J','I')
    if not key:
        raise ValueError('Key must not be empty')
    return ''.join(dict.fromkeys(key+ALPHABET.replace('J','')))

def playfair_prepare(text):
    text=letters(text).replace('J','I');result=[];i=0
    while i<len(text):
        first=text[i];filler='Q' if first=='X' else 'X'
        if i+1==len(text) or first==text[i+1]:
            result.extend([first,filler]);i+=1
        else:
            result.extend([first,text[i+1]]);i+=2
    return ''.join(result)

def _playfair_transform(text,square,direction):
    if len(text)%2:
        raise ValueError('Playfair needs complete letter pairs')
    position={c:divmod(i,5) for i,c in enumerate(square)};result=[]
    for i in range(0,len(text),2):
        a,b=text[i:i+2];ra,ca=position[a];rb,cb=position[b]
        if ra==rb:
            ca=(ca+direction)%5;cb=(cb+direction)%5
        elif ca==cb:
            ra=(ra+direction)%5;rb=(rb+direction)%5
        else:
            ca,cb=cb,ca
        result.extend([square[ra*5+ca],square[rb*5+cb]])
    return ''.join(result)

def playfair_encrypt(text,key):
    square=playfair_square(key);prepared=playfair_prepare(text)
    return _playfair_transform(prepared,square,1),prepared

def playfair_decrypt(cipher,key):
    cipher=letters(cipher).replace('J','I')
    return _playfair_transform(cipher,playfair_square(key),-1)

def determinant(matrix):
    if len(matrix)==1:
        return matrix[0][0]
    return sum((-1)**c*matrix[0][c]*determinant(
        [row[:c]+row[c+1:] for row in matrix[1:]])
        for c in range(len(matrix)))

def _hill_key(matrix):
    if not isinstance(matrix,(list,tuple)) or len(matrix) not in (2,3):
        raise ValueError('Teaching Hill key must be 2x2 or 3x3')
    n=len(matrix)
    if any(not isinstance(row,(list,tuple)) or len(row)!=n for row in matrix):
        raise ValueError('Key must be square')
    if any(type(x) is not int for row in matrix for x in row):
        raise TypeError('Matrix entries must be integers')
    matrix=[[x%26 for x in row] for row in matrix]
    if math.gcd(determinant(matrix),26)!=1:
        raise ValueError('Key determinant must be coprime to 26')
    return matrix

def hill_inverse(matrix):
    matrix=_hill_key(matrix);n=len(matrix)
    inverse_det=pow(determinant(matrix),-1,26);result=[]
    for r in range(n):
        row=[]
        for c in range(n):
            # Transpose the cofactor matrix to obtain the adjugate.
            minor=[line[:r]+line[r+1:]
                   for i,line in enumerate(matrix) if i!=c]
            row.append(inverse_det*(-1)**(r+c)*determinant(minor)%26)
        result.append(row)
    return result

def _hill_apply(text,matrix):
    n=len(matrix)
    if len(text)%n:
        raise ValueError('Ciphertext must contain complete Hill blocks')
    out=[]
    for start in range(0,len(text),n):
        vector=[ord(c)-65 for c in text[start:start+n]]
        out.extend(ALPHABET[sum(row[i]*vector[i] for i in range(n))%26]
                   for row in matrix)
    return ''.join(out)

def hill_encrypt(text,matrix):
    matrix=_hill_key(matrix);text=letters(text);n=len(matrix)
    prepared=text+'X'*((-len(text))%n)
    return _hill_apply(prepared,matrix),prepared

def hill_decrypt(cipher,matrix):
    return _hill_apply(letters(cipher),hill_inverse(matrix))

def rail_pattern(length,rails):
    integer(length,'Length');integer(rails,'Rails')
    if length<0 or not 1<=rails<=max(1,length):
        raise ValueError('Use 1 through the number of letters as rails')
    if rails==1:
        return [0]*length
    cycle=2*(rails-1)
    return [min(i%cycle,cycle-i%cycle) for i in range(length)]

def rail_encrypt(text,rails):
    text=letters(text);pattern=rail_pattern(len(text),rails)
    return ''.join(c for r in range(rails)
                   for c,p in zip(text,pattern) if p==r)

def rail_decrypt(cipher,rails):
    cipher=letters(cipher);pattern=rail_pattern(len(cipher),rails)
    rows=[];start=0
    for r in range(rails):
        count=pattern.count(r);rows.append(iter(cipher[start:start+count]))
        start+=count
    return ''.join(next(rows[r]) for r in pattern)

def pad_letters(text,key,decrypt=False):
    text=letters(text);key=letters(key)
    if len(text)!=len(key):
        raise ValueError('Pad length must equal message length')
    direction=-1 if decrypt else 1
    return ''.join(ALPHABET[(ord(a)-65+direction*(ord(b)-65))%26]
                   for a,b in zip(text,key))

def xor_bytes(left,right):
    if not isinstance(left,(bytes,bytearray)) or not isinstance(right,(bytes,bytearray)):
        raise TypeError('Use bytes for binary XOR')
    if len(left)!=len(right):
        raise ValueError('Pad length must equal byte-message length')
    return bytes(a^b for a,b in zip(left,right))

def lsb_embed(carrier,payload):
    if not isinstance(carrier,bytes) or not isinstance(payload,bytes):
        raise TypeError('Use bytes for the teaching carrier and payload')
    if len(payload)>65535:
        raise ValueError('Two-byte length header cannot hold this payload')
    packed=len(payload).to_bytes(2,'big')+payload
    bits=''.join(f'{b:08b}' for b in packed)
    if len(bits)>len(carrier):
        raise ValueError('Carrier capacity is insufficient')
    out=bytearray(carrier)
    for i,bit in enumerate(bits):
        out[i]=(out[i]&254)|int(bit)
    return bytes(out)

def lsb_extract(carrier):
    if not isinstance(carrier,bytes) or len(carrier)<16:
        raise ValueError('Need at least the 16-bit teaching header')
    def read(start,count):
        bits=''.join(str(b&1) for b in carrier[start:start+count*8])
        return bytes(int(bits[i:i+8],2) for i in range(0,len(bits),8))
    length=int.from_bytes(read(0,2),'big')
    if 16+length*8>len(carrier):
        raise ValueError('Declared payload exceeds carrier capacity')
    return read(16,length)

# DES tables: FIPS 46-3 (withdrawn), 1-indexed from the input's MSB.
IP=(58,50,42,34,26,18,10,2,60,52,44,36,28,20,12,4,
    62,54,46,38,30,22,14,6,64,56,48,40,32,24,16,8,
    57,49,41,33,25,17,9,1,59,51,43,35,27,19,11,3,
    61,53,45,37,29,21,13,5,63,55,47,39,31,23,15,7)
FP=(40,8,48,16,56,24,64,32,39,7,47,15,55,23,63,31,
    38,6,46,14,54,22,62,30,37,5,45,13,53,21,61,29,
    36,4,44,12,52,20,60,28,35,3,43,11,51,19,59,27,
    34,2,42,10,50,18,58,26,33,1,41,9,49,17,57,25)
E=(32,1,2,3,4,5,4,5,6,7,8,9,8,9,10,11,12,13,
   12,13,14,15,16,17,16,17,18,19,20,21,20,21,22,23,24,25,
   24,25,26,27,28,29,28,29,30,31,32,1)
P=(16,7,20,21,29,12,28,17,1,15,23,26,5,18,31,10,
   2,8,24,14,32,27,3,9,19,13,30,6,22,11,4,25)
PC1=(57,49,41,33,25,17,9,1,58,50,42,34,26,18,
     10,2,59,51,43,35,27,19,11,3,60,52,44,36,
     63,55,47,39,31,23,15,7,62,54,46,38,30,22,
     14,6,61,53,45,37,29,21,13,5,28,20,12,4)
PC2=(14,17,11,24,1,5,3,28,15,6,21,10,
     23,19,12,4,26,8,16,7,27,20,13,2,
     41,52,31,37,47,55,30,40,51,45,33,48,
     44,49,39,56,34,53,46,42,50,36,29,32)
SHIFTS=(1,1,2,2,2,2,2,2,1,2,2,2,2,2,2,1)
SBOXES=(
 ((14,4,13,1,2,15,11,8,3,10,6,12,5,9,0,7),
  (0,15,7,4,14,2,13,1,10,6,12,11,9,5,3,8),
  (4,1,14,8,13,6,2,11,15,12,9,7,3,10,5,0),
  (15,12,8,2,4,9,1,7,5,11,3,14,10,0,6,13)),
 ((15,1,8,14,6,11,3,4,9,7,2,13,12,0,5,10),
  (3,13,4,7,15,2,8,14,12,0,1,10,6,9,11,5),
  (0,14,7,11,10,4,13,1,5,8,12,6,9,3,2,15),
  (13,8,10,1,3,15,4,2,11,6,7,12,0,5,14,9)),
 ((10,0,9,14,6,3,15,5,1,13,12,7,11,4,2,8),
  (13,7,0,9,3,4,6,10,2,8,5,14,12,11,15,1),
  (13,6,4,9,8,15,3,0,11,1,2,12,5,10,14,7),
  (1,10,13,0,6,9,8,7,4,15,14,3,11,5,2,12)),
 ((7,13,14,3,0,6,9,10,1,2,8,5,11,12,4,15),
  (13,8,11,5,6,15,0,3,4,7,2,12,1,10,14,9),
  (10,6,9,0,12,11,7,13,15,1,3,14,5,2,8,4),
  (3,15,0,6,10,1,13,8,9,4,5,11,12,7,2,14)),
 ((2,12,4,1,7,10,11,6,8,5,3,15,13,0,14,9),
  (14,11,2,12,4,7,13,1,5,0,15,10,3,9,8,6),
  (4,2,1,11,10,13,7,8,15,9,12,5,6,3,0,14),
  (11,8,12,7,1,14,2,13,6,15,0,9,10,4,5,3)),
 ((12,1,10,15,9,2,6,8,0,13,3,4,14,7,5,11),
  (10,15,4,2,7,12,9,5,6,1,13,14,0,11,3,8),
  (9,14,15,5,2,8,12,3,7,0,4,10,1,13,11,6),
  (4,3,2,12,9,5,15,10,11,14,1,7,6,0,8,13)),
 ((4,11,2,14,15,0,8,13,3,12,9,7,5,10,6,1),
  (13,0,11,7,4,9,1,10,14,3,5,12,2,15,8,6),
  (1,4,11,13,12,3,7,14,10,15,6,8,0,5,9,2),
  (6,11,13,8,1,4,10,7,9,5,0,15,14,2,3,12)),
 ((13,2,8,4,6,15,11,1,10,9,3,14,5,0,12,7),
  (1,15,13,8,10,3,7,4,12,5,6,11,0,14,9,2),
  (7,11,4,1,9,12,14,2,0,6,10,13,15,3,5,8),
  (2,1,14,7,4,10,8,13,15,12,9,0,3,5,6,11)))

def permute(value,table,width):
    out=0
    for position in table:
        out=(out<<1)|((value>>(width-position))&1)
    return out

def _des_bytes(data,label):
    if not isinstance(data,bytes) or len(data)!=8:
        raise ValueError(label+' must be exactly 8 bytes')
    return data

def des_round_keys(key):
    key=_des_bytes(key,'DES key')
    selected=permute(int.from_bytes(key,'big'),PC1,64)
    c,d=selected>>28,selected&((1<<28)-1);keys=[]
    for shift in SHIFTS:
        c=((c<<shift)|(c>>(28-shift)))&((1<<28)-1)
        d=((d<<shift)|(d>>(28-shift)))&((1<<28)-1)
        keys.append(permute((c<<28)|d,PC2,56))
    return keys

def des_f(right,subkey):
    mixed=permute(right,E,32)^subkey;out=0
    for i,box in enumerate(SBOXES):
        six=(mixed>>(42-6*i))&63
        row=((six>>5)<<1)|(six&1);column=(six>>1)&15
        out=(out<<4)|box[row][column]
    return permute(out,P,32)

def des_trace(block,key,decrypt=False):
    block=_des_bytes(block,'DES block');keys=des_round_keys(key)
    if decrypt:
        keys=keys[::-1]
    initial=permute(int.from_bytes(block,'big'),IP,64)
    left,right=initial>>32,initial&0xffffffff
    rows=[{'round':0,'left':f'{left:08X}','right':f'{right:08X}','subkey':''}]
    for i,subkey in enumerate(keys,1):
        left,right=right,left^des_f(right,subkey)
        rows.append({'round':i,'left':f'{left:08X}',
                     'right':f'{right:08X}','subkey':f'{subkey:012X}'})
    result=permute((right<<32)|left,FP,64).to_bytes(8,'big')
    return {'result':result,'rounds':rows,'initial':f'{initial:016X}'}

def des_block(block,key,decrypt=False):
    """Exactly one old DES block. No mode, padding, authentication or key service."""
    return des_trace(block,key,decrypt)['result']
