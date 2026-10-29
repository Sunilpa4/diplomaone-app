"""Twelve offline classroom examples; actual outputs captured explicitly at build."""
import subprocess,sys,tempfile,textwrap
from pathlib import Path
from subject_DI05007021 import ROOT,tr
HELPER=ROOT/'tools/infosec_u2_ciphers.py'

def example(n,title,code,explanation):
 return {'id':f'sec2p{n:02d}','title':tr(title),
         'code':tr(textwrap.dedent(code).strip()+'\n'),'expl':tr(explanation)}

EXAMPLES=[
 example(1,'Practical 2: Caesar encryption and decryption',r'''
 from ciphers import caesar

 plain = "ATTACKATDAWN"
 cipher = caesar(plain, 3)
 print("plaintext:", plain)
 print("shift: 3")
 print("ciphertext:", cipher)
 print("decrypted:", caesar(cipher, -3))
 print("wrap_XYZ:", caesar("XYZ", 3))
 ''','Actual modulo-26 substitution, A=0 through Z=25. The helper uppercases ASCII letters and removes whitespace, rejecting other characters. Decryption recovers normalized letters, not original formatting. Shift 3 is public teaching data; Caesar is not suitable for real secrets.'),
 example(2,'Cryptanalysis of only a fixed Caesar classroom sample',r'''
 from ciphers import caesar

 sample = "KHOOR"
 candidates = [caesar(sample, -k) for k in range(26)]
 print("fixed_sample:", sample)
 print("candidate_count:", len(candidates))
 print("candidate_at_shift_3:", candidates[3])
 print("HELLO_occurrences:", candidates.count("HELLO"))
 ''','All 26 shifts are actually tested on the fixed sample KHOOR. HELLO is recognizable in this example; the program does not automatically understand arbitrary languages or identify a unique correct key for every short text. No live system, password or external data is attacked.'),
 example(3,'Monoalphabetic substitution and inverse mapping',r'''
 from ciphers import substitution

 alphabet = "QWERTYUIOPASDFGHJKLZXCVBNM"
 plain = "HELLO"
 cipher = substitution(plain, alphabet)
 print("plaintext:", plain)
 print("ciphertext:", cipher)
 print("decrypted:", substitution(cipher, alphabet, True))
 print("repeated_L_maps_to_SS:", cipher[2:4] == "SS")
 ''','The 26-letter key is checked for a complete permutation. H maps to I, E to T, L to S and O to G. A fixed substitution preserves repeated-letter patterns and relabels frequency counts; its large nominal keyspace does not make it modern secure encryption.'),
 example(4,'Polyalphabetic substitution: repeating-key Vigenere',r'''
 from ciphers import vigenere

 plain = "ATTACKATDAWN"
 key = "LEMON"
 cipher = vigenere(plain, key)
 print("plaintext:", plain)
 print("repeated_key: LEMONLEMONLE")
 print("ciphertext:", cipher)
 print("decrypted:", vigenere(cipher, key, True))
 ''','The familiar LXFOPVEFRNHR vector is genuinely computed. Repeating-key Vigenere uses different Caesar shifts according to key position. Its short repeated key is not a one-time pad and should not be used as modern protection.'),
 example(5,'Practical 4: Playfair preparation, encryption and reversal',r'''
 from ciphers import (playfair_square, playfair_prepare,
                      playfair_encrypt, playfair_decrypt)

 key = "PLAYFAIREXAMPLE"
 plain = "HIDETHEGOLDINTHETREESTUMP"
 cipher, prepared = playfair_encrypt(plain, key)
 print("square:", playfair_square(key))
 print("prepared:", prepared)
 print("ciphertext:", cipher)
 print("decrypted_prepared:", playfair_decrypt(cipher, key))
 print("BALLOON_prepared:", playfair_prepare("BALLOON"))
 print("XX_prepared:", playfair_prepare("XX"))
 ''','Uses a 5x5 I/J-merged square, row/column/rectangle rules, and X between repeated letters or at an odd ending. For a repeated/final X the declared fallback is Q, avoiding an XX pair. The real known vector is BMODZBXDNABEKUDMUIXMMOUVIF. Decryption preserves fillers: deleting every X or guessing J would destroy legitimate information.'),
 example(6,'Practical 3: Hill 2x2 encryption and modular inverse',r'''
 from ciphers import hill_encrypt, hill_decrypt, hill_inverse

 key = [[3, 3], [2, 5]]
 cipher, prepared = hill_encrypt("HELP", key)
 print("prepared:", prepared)
 print("determinant: 9; inverse_det_mod26: 3")
 print("inverse_matrix:", hill_inverse(key))
 print("ciphertext:", cipher)
 print("decrypted:", hill_decrypt(cipher, key))
 ''','Uses A=0 and COLUMN vectors: C=K*P modulo 26. HE=[7,4] becomes [7,8]=HI; LP becomes AT. det(K)=9 is invertible modulo 26, yielding inverse [[15,17],[20,9]]. A nonzero determinant is insufficient unless it is coprime to 26. This extends the official basic encryption practical with a checked reversal.'),
 example(7,'Hill 3x3 known vector and explicit padding',r'''
 from ciphers import hill_encrypt, hill_decrypt

 key = [[6, 24, 1], [13, 16, 10], [20, 17, 15]]
 cipher, prepared = hill_encrypt("ACT", key)
 print("prepared:", prepared)
 print("ciphertext:", cipher)
 print("decrypted:", hill_decrypt(cipher, key))
 padded_cipher, padded = hill_encrypt("HI", key)
 print("HI_prepared:", padded)
 print("padding_preserved:", hill_decrypt(padded_cipher, key))
 ''','Actually computes ACT -> POH with the declared column-vector convention. HI is prepared as HIX so its length is a multiple of three. The helper does not guess whether an ending X was original or padding. Both 2x2 and 3x3 matrices are supported; this is not a general large-matrix or secure cipher library.'),
 example(8,'Practical 5: rail-fence encryption and decryption',r'''
 from ciphers import rail_encrypt, rail_decrypt

 plain = "WEAREDISCOVEREDRUNATONCE"
 cipher = rail_encrypt(plain, 3)
 print("rails: 3")
 print("ciphertext:", cipher)
 print("decrypted:", rail_decrypt(cipher, 3))
 print("same_letter_multiset:", sorted(plain) == sorted(cipher))
 ''','Letters are genuinely written along the 0,1,2,1 zigzag and read row by row. Decoding reconstructs the exact rail positions, including uneven row lengths. Rail fence changes positions, not the letters; a histogram is therefore preserved. No padding is necessary in this implementation.'),
 example(9,'One-time-pad letter arithmetic — fixed worked example only',r'''
 from ciphers import pad_letters

 plain = "HELLO"
 public_demo_pad = "XMCKL"
 cipher = pad_letters(plain, public_demo_pad)
 print("plaintext:", plain)
 print("ciphertext:", cipher)
 print("decrypted:", pad_letters(cipher, public_demo_pad, True))
 print("pad_length_matches:", len(public_demo_pad) == len(plain))
 ''','Computes HELLO + XMCKL modulo 26 = EQNVZ. This public, fixed demonstration key is NOT a secret random pad and does not demonstrate perfect secrecy. A genuine OTP requires an independent uniformly random secret pad at least as long as the message, used only once.'),
 example(10,'Binary XOR pad, fresh-key round trip and key-reuse relation',r'''
 import secrets
 from ciphers import xor_bytes

 plain = b"HELLO"
 ephemeral_pad = secrets.token_bytes(len(plain))
 cipher = xor_bytes(plain, ephemeral_pad)
 print("fresh_pad_bytes:", len(ephemeral_pad))
 print("cipher_bytes:", len(cipher))
 print("recovered:", xor_bytes(cipher, ephemeral_pad).decode())

 # Separate PUBLIC fixed data: intentionally show why reuse is wrong.
 first, second = b"HELLO", b"WORLD"
 public_demo_pad = bytes.fromhex("1020304050")
 c1 = xor_bytes(first, public_demo_pad)
 c2 = xor_bytes(second, public_demo_pad)
 print("reuse_leaks_relation:",
       xor_bytes(c1, c2) == xor_bytes(first, second))
 ''','Fresh-key XOR really runs and the ephemeral key/cipher bytes are never printed or stored. secrets uses an OS-backed CSPRNG, not a proof of ideal information-theoretic randomness. The separate fixed public example verifies C1 XOR C2 = P1 XOR P2 on reuse. This algebra does not imply an attacker always learns both messages outright; key management and authentication are not implemented.'),
 example(11,'Historical DES: actual 16-round known-answer trace',r'''
 from ciphers import des_trace, des_block

 # PUBLIC classroom vector; DES is withdrawn and obsolete.
 key = bytes.fromhex("133457799BBCDFF1")
 plain = bytes.fromhex("0123456789ABCDEF")
 trace = des_trace(plain, key)
 cipher = trace["result"]
 print("initial_permutation:", trace["initial"])
 for number in (1, 16):
     row = trace["rounds"][number]
     print(f"round_{number}: L={row['left']} R={row['right']} "
           f"K={row['subkey']}")
 print("ciphertext:", cipher.hex().upper())
 print("decrypted:", des_block(cipher, key, True).hex().upper())
 print("round_count:", len(trace["rounds"]) - 1)
 ''','The included pure-Python helper performs the actual DES permutations, key schedule, eight S-boxes, 16 Feistel rounds and final swap/permutation. The 85E813540F0AB405 result is independently checked against OpenSSL with its legacy provider for this single test process only. DES is historical teaching, not production protection or a FIPS-validated implementation. This is an optional structure illustration, not an extra official cipher practical.'),
 example(12,'Steganography illustration: LSBs of synthetic RGB bytes',r'''
 from ciphers import lsb_embed, lsb_extract

 cover = bytes([120, 96, 180]) * 64  # 8x8 synthetic RGB pixels
 payload = b"GTU"
 stego = lsb_embed(cover, payload)
 print("carrier_channels:", len(cover))
 print("header_and_payload_bits:", 16 + 8 * len(payload))
 print("modified_channels:", sum(a != b for a, b in zip(cover, stego)))
 print("largest_channel_change:",
       max(abs(a - b) for a, b in zip(cover, stego)))
 print("recovered:", lsb_extract(stego).decode())
 print("cover_unchanged:", cover == bytes([120, 96, 180]) * 64)
 ''','Actually embeds a two-byte length header and the harmless GTU payload into low bits of a private synthetic RGB byte array. This is not a JPEG/PNG editor, network covert channel, general image decoder or claim of undetectability. Steganography hides existence; it does not by itself encrypt or authenticate content. Capacity checks and declared-length checks reject unsuitable carriers.')]

def run_program(example):
 with tempfile.TemporaryDirectory(prefix='infosec-u2-example-') as td:
  folder=Path(td);(folder/'ciphers.py').write_text(HELPER.read_text())
  script=folder/(example['id']+'.py');script.write_text(example['code']['en'])
  result=subprocess.run([sys.executable,'-E',str(script)],cwd=folder,text=True,capture_output=True,timeout=12)
  assert result.returncode==0,(example['id'],result.stderr)
  assert not result.stderr,(example['id'],result.stderr)
 return dict(example,out=result.stdout)

def execute_all():return [run_program(p) for p in EXAMPLES]
