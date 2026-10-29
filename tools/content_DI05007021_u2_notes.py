"""English-only conventional/symmetric crypto: syllabus topics and worked steps."""
from subject_DI05007021 import tr
from content_DI05007021_u1_notes import ul,table,topic
SOURCES=[
 ('GTU DI05007021 syllabus, 2026–27','https://s3-ap-southeast-1.amazonaws.com/gtusitecirculars/Syallbus/DI05007021.pdf'),
 ('Handbook of Applied Cryptography, chapter 7: classical and block ciphers (historical text)','https://cacr.uwaterloo.ca/hac/about/chap7.pdf'),
 ('Handbook of Applied Cryptography, chapter 6: one-time pad and stream ciphers','https://cacr.uwaterloo.ca/hac/about/chap6.pdf'),
 ('NIST FIPS 46-3: DES, withdrawn 19 May 2005','https://csrc.nist.gov/pubs/fips/46-3/final'),
 ('NIST archived DES specification and tables','https://csrc.nist.gov/files/pubs/fips/46-3/final/docs/fips46-3.pdf'),
 ('NIST glossary: steganography','https://csrc.nist.gov/glossary/term/steganography'),
 ('Playfair rules and conventional worked vector (secondary reference)','https://en.wikipedia.org/wiki/Playfair_cipher'),
 ('Hill column-vector example and modular inverse (secondary reference)','https://en.wikipedia.org/wiki/Hill_cipher'),
 ('Vigenere repeating-key convention (secondary reference)','https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher'),
 ('Rail-fence worked zigzag example (secondary reference)','https://en.wikipedia.org/wiki/Rail_fence_cipher')]
NOTES=[
 {'title':tr('1. Cryptography Foundations'),'items':[
  topic('1.1 Plaintext, ciphertext and the study of ciphers',
   table(['Term','Meaning'],[
    ('Plaintext','The original information supplied to encryption; it may be text or bytes.'),
    ('Ciphertext','The transformed output of encryption; binary output can be displayed as hexadecimal.'),
    ('Encryption','Transforms plaintext using an algorithm and key to obtain ciphertext.'),
    ('Decryption','Applies the appropriate inverse operation and key to recover the encoded plaintext.'),
    ('Cryptography','Design and use of techniques for protecting information.'),
    ('Cryptanalysis','Study of obtaining information or defeating a cryptographic goal without the intended secret; here only fixed classroom examples are used.'),
    ('Cryptology','The field encompassing cryptography and cryptanalysis.')])+
   '<p><b>Distinguish:</b> hexadecimal/Base64 are encodings, not secret-key encryption. Hashing produces a digest; it is not reversible encryption with a decryption key. Ciphertext that looks random is not, by appearance alone, proven secure.</p>'),
  topic('1.2 Conventional / symmetric encryption model',
   '<p>In <b>symmetric-key encryption</b>, communicating parties share secret key material. Our classroom model uses <code>C = E_K(P)</code> and <code>P = D_K(C)</code>. The algorithm can be public; security should not depend on hiding its design.</p>'+ul(
    'Sender encrypts the prepared message; receiver uses the corresponding secret key to decrypt. The key needs secure generation, distribution, storage and retirement.',
    'Encryption chiefly addresses confidentiality. Appropriate authentication/integrity protection is still needed: obtaining readable decrypted text is not proof of sender identity or freshness.',
    'These classical ciphers and single DES are <b>historical teaching methods, not suitable choices for protecting real data today</b>. Use vetted current authenticated-encryption implementations and protocols for real applications; do not deploy this lab library.')+'<p>Actual demonstrations are offline and use public classroom messages and keys. No live target, account or real secret is attacked.</p>','sec2_model'),
  topic('1.3 Substitution, transposition and classroom conventions',
   table(['Technique','What changes?','Examples'],[
    ('Monoalphabetic substitution','One fixed alphabet mapping replaces each letter.','Caesar; a general 26-letter permutation.'),
    ('Polyalphabetic substitution','The mapping varies with position/key state.','Repeating-key Vigenere, used here as a representative.'),
    ('Polygraphic substitution','A block or pair of symbols is transformed together.','Playfair digraphs; Hill letter vectors. This term is not a synonym for polyalphabetic.'),
    ('Transposition','Positions change while the letters themselves are retained.','Rail fence; its letter histogram is unchanged.')])+
   '<p><b>Declared lab convention:</b> A=0 through Z=25; ASCII letters become uppercase and whitespace is removed. Other characters are rejected rather than silently discarded. Decryption returns normalized/prepared text, not the original case, spacing or punctuation. Playfair additionally merges J into I; fillers and Hill padding are explicit and are not guessed away.</p>','sec2_substitution')]},
 {'title':tr('2. Substitution Techniques'),'items':[
  topic('2.1 Monoalphabetic substitution',
   '<p>Choose a permutation of the alphabet. Each plaintext letter always uses the same mapped ciphertext letter. The inverse permutation decrypts it.</p>'+table(['Plain alphabet','Cipher alphabet'],[('ABCDEFGHIJKLMNOPQRSTUVWXYZ','QWERTYUIOPASDFGHJKLZXCVBNM')])+
   '<p><b>Worked example:</b> HELLO → ITSSG because H→I, E→T, L→S and O→G. Repeated L becomes repeated S.</p>'+ul(
    'A valid substitution alphabet has all 26 letters exactly once. A duplicate or missing letter prevents a unique inverse.',
    'There are 26! possible permutations, but a large nominal keyspace alone does not prove security. Repeated patterns and language frequency remain useful to cryptanalysis.',
    'Frequency analysis relabels statistical patterns; short messages may not provide enough evidence for a unique recovery.') ,programs=['sec2p03']),
  topic('2.2 Caesar cipher: shift, wraparound and reversal',
   '<p>Caesar is a restricted monoalphabetic substitution. With numeric letters and integer shift k:</p><p><code>C = (P + k) mod 26</code><br><code>P = (C - k) mod 26</code></p>'+table(['Plain letter','Numeric step, k=3','Cipher'],[
    ('A','(0+3) mod 26 = 3','D'),('T','(19+3) mod 26 = 22','W'),('X','(23+3) mod 26 = 0','A'),('Z','(25+3) mod 26 = 2','C')])+
   '<p><b>Worked message:</b> ATTACKATDAWN → DWWDFNDWGDZQ. Subtract 3 to recover the normalized plaintext. There are only 26 shifts, including the identity shift 0. The separate KHOOR demo checks all 26 on fixed teaching data; HELLO appears at shift 3. Recognizing meaningful text is not a universal automatic key-identification guarantee.</p>',programs=['sec2p01','sec2p02']),
  topic('2.3 Polyalphabetic substitution: Vigenere example',
   '<p>A changing substitution alphabet can map the same plaintext letter differently at different positions. Our representative is <b>repeating-key Vigenere</b>:</p><p><code>C_i = (P_i + K_i) mod 26</code><br><code>P_i = (C_i - K_i) mod 26</code></p>'+table(['Item','Sequence'],[
    ('Plaintext','ATTACKATDAWN'),('Repeated key','LEMONLEMONLE'),('Ciphertext','LXFOPVEFRNHR')])+
   '<p>For the first three positions: A(0)+L(11)=L(11); T(19)+E(4)=X(23); T(19)+M(12)=31 mod 26=F(5). Continue using the repeated key. Reverse by subtraction.</p>'+ul(
    'A repeated short key introduces periodic structure. Vigenere is not secure modern encryption.',
    'A key merely as long as one sample is not automatically a one-time pad: randomness, independence, secrecy and no reuse are essential too.') ,'sec2_vigenere',programs=['sec2p04']),
  topic('2.4 Playfair: key square and digraph preparation',
   '<p>Playfair transforms <b>pairs of letters</b>. Our declared variant uses a 5×5 square, combines I/J and fills unused alphabet letters after the deduplicated keyword. With key PLAYFAIREXAMPLE:</p>'+table(['1','2','3','4','5'],[
    ('P','L','A','Y','F'),('I','R','E','X','M'),('B','C','D','G','H'),('K','N','O','Q','S'),('T','U','V','W','Z')])+
   '<ol><li>Normalize letters and map J to I.</li><li>Scan pairs. If both letters would be equal, insert X after the first and reconsider the next original letter.</li><li>If the final letter has no partner, append X.</li><li>For a repeated or final X, this implementation uses Q as the filler instead.</li></ol>'+
   '<p><b>Examples:</b> BALLOON → BA LX LO ON, hence BALXLOON. XX → XQ XQ. Different conventions exist; always state the one used. Fillers are not automatically removed during decryption because genuine X/Q letters may otherwise be destroyed.</p>','sec2_playfair'),
  topic('2.5 Playfair encryption and decryption rules',
   table(['Pair positions','Encrypt','Decrypt'],[
    ('Same row','Move each letter one column right, wrapping.','Move each letter one column left.'),
    ('Same column','Move each letter one row down, wrapping.','Move each letter one row up.'),
    ('Different row and column','Use the other rectangle corner in each letter’s own row.','Use the same rectangle-corner operation.')])+
   '<p>In the above square, HI forms a rectangle: H(row 3,column 5) → B(row 3,column 1), I(row 2,column 1) → M(row 2,column 5), giving <b>HI → BM</b>.</p><p>The actual full example prepares HIDETHEGOLDINTHETREESTUMP as <b>HIDETHEGOLDINTHETREXESTUMP</b> and encrypts it to <b>BMODZBXDNABEKUDMUIXMMOUVIF</b>. Reversal returns the prepared text. Playfair is historical polygraphic substitution, not modern authenticated encryption.</p>',programs=['sec2p05']),
  topic('2.6 Hill cipher: column vectors and valid keys',
   '<p>Hill is a <b>polygraphic substitution</b> using matrix multiplication modulo 26. For an n×n key matrix K and a column vector P of n letter numbers:</p><p><code>C = K P mod 26</code><br><code>P = K^-1 C mod 26</code></p>'+ul(
    'Use a consistent convention: these notes and programs use <b>column vectors</b>, not row vectors. Different conventions can produce different ciphertext for the same displayed numbers.',
    'The matrix must be invertible modulo 26: <b>gcd(det(K),26)=1</b>. A determinant that is merely nonzero is not enough; it must not share factors 2 or 13 with 26.',
    'For K=[[3,3],[2,5]], det=15−6=9 and 9×3=27≡1 mod 26. K^-1 = 3×[[5,−3],[−2,3]] mod 26 = [[15,17],[20,9]].',
    'For example, [[2,0],[0,1]] has nonzero determinant 2 but no inverse modulo 26. The implementation rejects such a key before encrypting.',
    'Prepare complete blocks by appending X when required. Keep that prepared text or original-length knowledge; do not delete every trailing X blindly.')+'<p>The shared teaching helper supports 2×2 and 3×3 matrices, not arbitrary large matrices or a production cryptosystem.</p>','sec2_hill'),
  topic('2.7 Hill worked examples: HELP → HIAT and ACT → POH',
   '<p><b>2×2, K=[[3,3],[2,5]]:</b></p>'+table(['Block','Multiply column vector','Reduce mod 26','Cipher'],[
    ('HE = [7,4]','[3×7+3×4, 2×7+5×4] = [33,34]','[7,8]','HI'),
    ('LP = [11,15]','[3×11+3×15, 2×11+5×15] = [78,97]','[0,19]','AT')])+
   '<p>Combine to obtain HIAT. Applying [[15,17],[20,9]] to each ciphertext column returns HELP.</p><p><b>3×3:</b> K=[[6,24,1],[13,16,10],[20,17,15]] has determinant 441, coprime to 26. ACT=[0,2,19] gives [67,222,319] mod 26 = [15,14,7], hence <b>POH</b>. The actual program also prepares HI as HIX and reverses to HIX without guessing away its padding.</p>'+ '<p>Decryption is an additional checked learning aid; the official Hill practical asks for basic encryption.</p>',programs=['sec2p06','sec2p07'])]},
 {'title':tr('3. One-Time Pad and Transposition'),'items':[
  topic('3.1 One-time pad: arithmetic and essential conditions',
   '<p>A genuine <b>one-time pad (OTP)</b> uses independent, uniformly random secret key symbols at least as long as the message, with each pad part used only once. Under those ideal conditions it provides perfect secrecy of message content against ciphertext-only observation—not authentication, integrity or automatic traffic-length hiding.</p>'+table(['Item','Letter example, A=0'],[
    ('Plaintext','HELLO'),('Public worked pad','XMCKL'),('Ciphertext','EQNVZ')])+
   '<p>H(7)+X(23)=30 mod26=E(4); E(4)+M(12)=Q(16); L(11)+C(2)=N(13); L(11)+K(10)=V(21); O(14)+L(11)=Z(25). Subtract the pad modulo 26 to reverse.</p>'+ul(
    '<b>The displayed pad is public fixed classroom data:</b> it demonstrates arithmetic, not perfect secrecy.',
    'A memorized phrase, repeated Vigenere key or predictable sequence is not a genuine OTP.',
    'The difficult practical requirements are enough truly suitable key material, secure distribution/storage, synchronization and never reusing a pad portion.') ,'sec2_otp',programs=['sec2p09']),
  topic('3.2 Binary XOR pad, reuse and security limits',
   '<p>For byte/bit messages, <code>C = P XOR K</code> and <code>P = C XOR K</code>. Our fresh-key example actually uses Python secrets, an OS-backed CSPRNG; it does not prove ideal information-theoretic randomness or implement a complete key-distribution protocol.</p>'+ul(
    'Message and key lengths must match in the helper. The program never prints or saves its fresh key or random ciphertext bytes; it reports actual lengths and successful recovery.',
    '<b>Reuse is dangerous:</b> C1=P1 XOR K and C2=P2 XOR K imply C1 XOR C2=P1 XOR P2. The separate fixed public HELLO/WORLD demonstration checks this equality.',
    'This relation leaks structure but is not a claim that an attacker instantly learns both arbitrary messages.',
    'Even ideal OTP confidentiality does not stop active modification: changing ciphertext bits changes recovered plaintext bits. Integrity/authentication needs separate appropriate design.') ,programs=['sec2p10']),
  topic('3.3 Rail-fence transposition',
   '<p>Write letters diagonally across successive rails, bounce at top/bottom, then read each rail from left to right. For three rails the position pattern is <code>0,1,2,1,0,1,2,1,...</code>.</p>'+table(['Rail','Letters for WEAREDISCOVEREDRUNATONCE'],[
    ('0','WECRUO'),('1','ERDSOEERNTNE'),('2','AIVDAC')])+
   '<p>Read rows to get <b>WECRUOERDSOEERNTNEAIVDAC</b>. To decrypt, reconstruct the zigzag positions, count how many symbols each rail receives, fill the rails from ciphertext, then traverse the original zigzag.</p>'+ul(
    'Rail fence changes positions, not symbols: the ciphertext and normalized plaintext have the same letter multiset/frequencies.',
    'Rows can have unequal lengths. The code handles that directly and needs no padding.',
    'One rail produces the identity transformation. For these examples choose a positive rail count no greater than the message length; an empty message allows one rail.',
    'A small/simple rail pattern is not modern secure encryption.') ,'sec2_rail',programs=['sec2p08'])]},
 {'title':tr('4. Steganography'),'items':[
  topic('4.1 Hiding existence: carriers, types and a bounded LSB example',
   '<p><b>Steganography</b> embeds information in a carrier to conceal the existence of the communication. <b>Cryptography</b> tries to conceal meaning from unauthorized readers. Neither property automatically supplies the other.</p>'+table(['Carrier type','Illustrative technique / limitation'],[
    ('Text','Use a controlled textual representation or formatting; editing/reformatting may destroy the embedded pattern.'),
    ('Image','For example, change selected least significant bits of raw pixel channels; compression or processing can alter them.'),
    ('Audio','Embed within a controlled audio representation; resampling/compression may damage the payload.'),
    ('Video','Use controlled frame/audio data; transcoding and large carriers complicate recovery.'),
    ('Network/protocol','Use features of a communication representation or timing; no network covert channel is implemented in this unit.')])+
   '<p><b>Actual supporting example:</b> synthetic 8×8 RGB data gives 192 channel bytes. A two-byte length header plus GTU (three bytes) occupies 16+24=<b>40 low bits</b>. The program changes 13 channels by at most 1 and really extracts GTU. Its capacity rule is <code>16 + 8×payload_bytes ≤ carrier_bytes</code>.</p>'+ul(
    'This is only a private raw-byte fixture, not a PNG/JPEG editor or general image decoder. No personal media or external carrier is used.',
    'Small channel changes do not establish invisibility or resistance to steganalysis. The payload is not encrypted or authenticated.',
    'Never assume recompression, cropping or other changes preserve simple LSB data. Capacity, robustness and detectability are distinct concerns.') ,'sec2_stego',programs=['sec2p12'])]},
 {'title':tr('5. Data Encryption Standard — Historical Study'),'items':[
  topic('5.1 DES parameters and overall structure',
   '<p><b>Single DES</b> is a symmetric block cipher with a <b>64-bit data block</b> and <b>56 effective key bits</b>. Its common 64-bit key representation includes eight parity bits, one per byte; those parity bits are not extra encryption-key strength.</p>'+
   '<ol><li>Apply the initial permutation IP to the 64-bit block.</li><li>Split into L0 and R0, each 32 bits.</li><li>Apply 16 Feistel rounds with sixteen 48-bit round subkeys.</li><li>Swap the final halves, forming R16 || L16.</li><li>Apply IP inverse (the final permutation) to obtain the 64-bit ciphertext.</li></ol>'+
   '<p>Round equations: <code>L_i = R_(i-1)</code>; <code>R_i = L_(i-1) XOR f(R_(i-1),K_i)</code>. The same Feistel structure decrypts when the subkey order is reversed. IP and its inverse are fixed permutations, not independently secret operations.</p>'+
   '<p><b>Security status:</b> NIST withdrew FIPS 46-3 on <b>19 May 2005</b>. DES belongs here because the syllabus requires its structure and trade-offs, not because it is an acceptable choice for new protection.</p>','sec2_des'),
  topic('5.2 DES round function, S-boxes and key schedule',
   '<p><b>Round function f:</b></p><ol><li>Expand the 32-bit right half to 48 bits using E.</li><li>XOR with the current 48-bit subkey.</li><li>Divide into eight 6-bit groups. Each S-box maps 6 bits to 4 bits: the first/last input bits select the row; the middle four select the column.</li><li>Combine the eight outputs into 32 bits and apply the P permutation.</li></ol>'+
   '<p><b>Key schedule:</b> PC-1 selects 56 effective bits from the 64-bit representation. Split into C/D halves of 28 bits, rotate according to the round schedule, then PC-2 selects 48 bits. Rotations are 1 in rounds 1,2,9,16 and 2 in the other rounds.</p>'+table(['Actual public-vector trace','Observed value'],[
    ('Key / plaintext','133457799BBCDFF1 / 0123456789ABCDEF'),
    ('After IP','CC00CCFFF0AAF0AA'),('First subkey K1','1B02EFFC7072'),
    ('After round 1','L1=F0AAF0AA; R1=EF4A6544'),
    ('After round 16','L16=43423234; R16=0A4CD995'),
    ('Final ciphertext','85E813540F0AB405')])+
   '<p>These values are actually computed by the included pure-Python helper and the final encryption/decryption is independently checked against OpenSSL’s legacy DES for the test process only. This is <b>not</b> a NIST/FIPS validation or certification of the code.</p>','sec2_feistel',programs=['sec2p11']),
  topic('5.3 DES advantages in context, disadvantages and modern caution',
   table(['Historical/design advantage','Important limitation today'],[
    ('Published, widely studied design with compact bit operations.','Historical standardization is not present-day security approval.'),
    ('Feistel construction permits reversal with reversed round keys.','Correct reversal does not establish confidentiality strength or authentication.'),
    ('Hardware-oriented fixed block structure and clear key schedule.','A 56-bit effective key is too small for modern protection; no brute-force timing benchmark is claimed here.'),
    ('Useful for studying substitution, permutation and diffusion.','The 64-bit block size is small, and modes/key management still matter; a bare block cipher is not a full secure message protocol.')])+
   '<p><b>Do not deploy these examples:</b> classical ciphers and single DES are unsuitable for real secrets. Do not assume switching to 3DES is a modern default either. Real applications need appropriate current authenticated encryption and vetted implementations, not home-made classroom cryptography.</p><p>An independent DES check uses the OpenSSL legacy provider only for that individual process; it does not change system-wide provider settings or expose a network service.</p>')]},
 {'title':tr('6. Practical Journal and Exam Preparation'),'items':[
  topic('6.1 Practicals 2–5: evidence, normalization and limitations',
   table(['Official practical','Included example','Required interpretation'],[
    ('2: Caesar encryption/decryption','sec2p01.py','State alphabet, shift and normalization; show both directions.'),
    ('3: Hill basic encryption','sec2p06.py; sec2p07.py extension','State matrix/vector convention, valid determinant and block preparation.'),
    ('4: Playfair encryption','sec2p05.py','Show square, I/J rule, digraph/filler convention and pair transformations.'),
    ('5: Rail-fence encryption','sec2p08.py','Show the zigzag/rails, row concatenation and resulting ciphertext.')])+
   '<p>The ZIP includes the shared <code>ciphers.py</code> source beside all twelve scripts, so no PYTHONPATH setup or pip dependency is needed. Supporting examples cover fixed-sample Caesar analysis, general substitution, Vigenere, OTP arithmetic/XOR, DES and synthetic LSBs; these are not invented additional official practical numbers.</p>'+ul(
    'Record input, public demo key, preparation convention, calculation/algorithm, actual output, recovery target and limitation in the journal.',
    'Report recovery of normalized/prepared text honestly. Never silently delete arbitrary X/Q characters or promise to restore lost formatting.',
    'All example data is local and fictional/public. No files containing user secrets, live targets or external services are used.',
    '<b>Assessment:</b> the official course scheme stays theory 70+30 and practical 20+30=150. This unit is 12 hours / 25% syllabus weight; it does not guarantee exact question marks in an exam.',
    'The sixteen answered questions below are original revision exercises with suggested 3/4/7-mark sizes only—not official GTU past-paper questions, allocated marks or a promised paper pattern.')+
   '<p><b>References:</b> '+', '.join('<a href="'+u+'">'+n+'</a>' for n,u in SOURCES)+'. Historical texts are used for algorithm facts, not current deployment advice; no textbook chapter is redistributed.</p>')]}]

PRACTICE=[
 ('Define plaintext, ciphertext, encryption, decryption, cryptanalysis and cryptology.',3,
  '<p>Plaintext is input information; ciphertext is encryption output. Encryption transforms plaintext under a key; decryption applies the appropriate inverse and key. Cryptanalysis studies how cryptographic goals may be defeated without the intended secret. Cryptology includes cryptography and cryptanalysis. Encoding and hashing are different operations: hexadecimal is a representation, while a digest has no decryption key.</p>'),
 ('Explain the symmetric encryption model and its key-management issue.',4,
  '<p>Draw sender P → E_K → C → D_K → recovered P at the receiver. Both parties need the corresponding shared secret key material. Protect key generation, distribution, storage and retirement; knowing the algorithm need not reveal the secret key. Encryption alone does not establish sender identity, integrity or freshness. The lab models this flow on normalized/prepared messages; it is not a production secure protocol.</p>'),
 ('Differentiate substitution and transposition, including monoalphabetic, polyalphabetic and polygraphic methods.',7,
  '<p>Substitution replaces symbols or blocks; transposition reorders their positions. Caesar and a fixed alphabet permutation are monoalphabetic. Repeating-key Vigenere is polyalphabetic because mapping varies with key position. Playfair is polygraphic on pairs; Hill is polygraphic on vectors, not simply a synonym for polyalphabetic. Rail fence is transposition: letters and their histogram are retained. All these classical methods are historical, not suitable modern protection.</p>'),
 ('Encrypt ATTACKATDAWN with Caesar shift 3 and explain wraparound and reversal.',4,
  '<p>Use A=0 and C=(P+3) mod26. A→D, T→W, C→F, K→N, D→G, W→Z and N→Q. Thus ATTACKATDAWN → DWWDFNDWGDZQ. Decrypt with P=(C−3) mod26. Wraparound gives X→A, Y→B, Z→C. Only 26 shifts, including identity 0, exist, so trying them on a fixed classroom sample is straightforward; this is not real-data security.</p>'),
 ('Explain why a monoalphabetic cipher can be weak despite 26! possible mappings.',3,
  '<p>The mapping is a permutation, so repeated plaintext letters always map to the same repeated ciphertext letters and frequencies are relabelled rather than eliminated. For the shown alphabet, HELLO becomes ITSSG and LL becomes SS. Language patterns can aid analysis even with a large nominal keyspace. Short samples may be ambiguous; frequency evidence is not an automatic unique recovery guarantee.</p>'),
 ('Work the Vigenere example ATTACKATDAWN with key LEMON.',4,
  '<p>Repeat the key to LEMONLEMONLE and add letter numbers modulo 26. The first positions give A+L=L, T+E=X, T+M=F. Continuing produces LXFOPVEFRNHR. Subtract the same key sequence to recover ATTACKATDAWN. The short key repeats, introducing structure; this is a historical polyalphabetic example, not a one-time pad.</p>'),
 ('Prepare BALLOON and XX for the declared Playfair variant and state why fillers are preserved.',4,
  '<p>Map J to I, split digraphs, insert X between repeated letters and after an unpaired ending; use Q instead when the repeated/final letter is X. BALLOON becomes BA LX LO ON = BALXLOON. XX becomes XQ XQ = XQXQ. Decryption returns prepared text. Automatically removing every X/Q or guessing I/J would damage valid original letters, so any later interpretation needs external knowledge.</p>'),
 ('Explain the Playfair square and three transformation rules with a worked pair.',7,
  '<p>Deduplicate PLAYFAIREXAMPLE then append remaining letters, merging I/J: PLAYF / IREXM / BCDGH / KNOQS / TUVWZ. Same-row pairs shift right, same-column pairs shift down, and other pairs use rectangle corners in their own rows; wrap edges. Decryption shifts left/up or applies the same rectangle rule. HI uses H(row3,col5), I(row2,col1), giving BM. Apply the declared preparation rules before pairing; this remains historical, unauthenticated encryption.</p>'),
 ('Encrypt HELP with Hill key [[3,3],[2,5]] using column vectors.',7,
  '<p>A=0. det(K)=3×5−3×2=9, coprime to26, so the key is valid. HE=[7,4] gives K×P=[33,34] mod26=[7,8]=HI. LP=[11,15] gives [78,97] mod26=[0,19]=AT. Combine to obtain HIAT. State the column-vector convention and block size; changing conventions changes the computation. With an odd number of letters this helper appends X explicitly rather than claiming original formatting is recovered.</p>'),
 ('Find the inverse Hill matrix for [[3,3],[2,5]] and explain the validity condition.',7,
  '<p>det=9 and 9^-1 mod26=3 since 9×3=27≡1. The adjugate is [[5,−3],[−2,3]]. Multiply by3 and reduce modulo 26: K^-1=[[15,17],[20,9]]. K×K^-1 reduces to the identity matrix modulo 26, allowing recovery of prepared letter columns. A key is valid only when gcd(det,26)=1; a nonzero determinant such as2 is still invalid modulo 26.</p>'),
 ('Explain the 3x3 ACT → POH Hill calculation and the padding limitation.',4,
  '<p>With K=[[6,24,1],[13,16,10],[20,17,15]], ACT=[0,2,19]. Multiplication gives [67,222,319] mod26=[15,14,7]=POH. det=441 is coprime to26. A short block HI is prepared as HIX. Decryption returns that prepared text; without original-length information, a final X cannot safely be labelled padding and removed automatically.</p>'),
 ('State genuine one-time-pad conditions and work HELLO with pad XMCKL.',7,
  '<p>The pad must be independent, uniformly random, secret, at least as long as the message and never reused. Under the ideal conditions OTP gives perfect message-content secrecy against ciphertext-only observation, not authentication. With A=0, HELLO+XMCKL modulo 26 gives EQNVZ; subtract the pad to reverse. The published fixed sample demonstrates arithmetic only. A repeated phrase or a CSPRNG demonstration is not itself proof of ideal information-theoretic randomness. Key distribution, storage and single use remain hard practical requirements.</p>'),
 ('Show why reusing an XOR pad leaks a relation between plaintexts.',4,
  '<p>If C1=P1 XOR K and C2=P2 XOR K, then C1 XOR C2=P1 XOR P2 because K XOR K=0. The fixed HELLO/WORLD lab checks this equality. It reveals a relation and may aid recovery with additional knowledge, but does not assert that both arbitrary messages are instantly known. Use pad material once; even a correctly used ideal OTP still needs separate integrity/authentication protection against active modification.</p>'),
 ('Explain three-rail encryption of WEAREDISCOVEREDRUNATONCE.',4,
  '<p>The zigzag visits rails 0,1,2,1 repeatedly. Filling positions yields rail0 WECRUO, rail1 ERDSOEERNTNE, rail2 AIVDAC. Read rows to produce WECRUOERDSOEERNTNEAIVDAC. Reverse by reconstructing the position pattern and correct per-rail counts, not by assuming equal row lengths. No padding is used here. Only positions change, so the letter histogram is preserved.</p>'),
 ('Differentiate steganography from cryptography and explain the LSB capacity example.',4,
  '<p>Cryptography seeks to hide meaning; steganography seeks to hide communication’s existence using a carrier, such as text, image, audio, video or protocol data. For the synthetic 8×8 RGB example, 192 channel bytes hold one low bit each. A two-byte length header plus three-byte GTU payload needs16+24=40 bits. Actual extraction recovers GTU. This is not a real image editor, undetectability proof, encryption or authentication; compression and processing can destroy a simple LSB pattern.</p>'),
 ('Describe DES structure, round/key parameters and why it is not modern protection.',7,
  '<p>DES processes 64-bit blocks with 56 effective key bits plus 8 representation/parity bits. IP is followed by 32-bit halves and 16 Feistel rounds: L_i=R_(i−1), R_i=L_(i−1) XOR f(R_(i−1),K_i). f expands 32→48, XORs a 48-bit subkey, maps eight 6-bit groups through S-boxes to 32 bits, then permutes P. PC-1, 28-bit rotations and PC-2 derive 16 subkeys. After the final half-swap apply IP inverse; reverse subkeys for decryption. NIST withdrew FIPS 46-3 on 19 May 2005. The short effective key, small block and lack of built-in authentication make single DES unsuitable for new protection. The lab trace is not FIPS certification.</p>')]
EXAM=[{'q':tr('Practice: '+q),'marks':m} for q,m,a in PRACTICE]
ANSWERED={'title':tr('7. Answered Exam-Style Practice — Suggested Marks Only'),'role':'practice',
 'items':[topic(f'Practice {i}. {q}',a) for i,(q,m,a) in enumerate(PRACTICE,1)]}

CARDS=[
 ('Basic model','C = E_K(P)\nP = D_K(C)','Shared secret material is needed; encryption alone does not authenticate.'),
 ('Alphabet convention','A=0, B=1, ..., Z=25\nUppercase ASCII; whitespace removed','Other characters are rejected. Recovery targets normalized/prepared text, not formatting.'),
 ('Caesar','C=(P+k) mod26\nP=(C-k) mod26','26 shifts including identity 0; historical classroom use only.'),
 ('Monoalphabetic versus polyalphabetic','Fixed alphabet: HELLO -> ITSSG\nChanging shifts: Vigenere','Polygraphic instead means pairs/blocks: Playfair and Hill.'),
 ('Vigenere','C_i=(P_i+K_i) mod26\nP_i=(C_i-K_i) mod26','Here the key repeats. That is not a genuine one-time pad.'),
 ('Playfair','5x5; I/J merged\nSame row: right/left\nSame column: down/up\nRectangle: swap columns','Insert X for repeats/endings; use Q for repeated/final X in this declared variant. Preserve fillers.'),
 ('Hill','C=K*P mod26; column vectors\nP=K^-1*C mod26\ngcd(det(K),26)=1','Only 2x2 and 3x3 in the teaching helper. Nonzero determinant alone is insufficient.'),
 ('Hill 2x2 inverse','K=[[3,3],[2,5]]\nK^-1=[[15,17],[20,9]]\nHELP -> HIAT','det=9; inverse determinant=3 modulo 26. Preserve explicit X padding.'),
 ('OTP conditions','Independent + uniformly random + secret\nPad >= message; never reuse a pad part','Public fixed pads show arithmetic, not perfect secrecy. Ideal OTP does not authenticate.'),
 ('XOR and reuse','C=P XOR K; P=C XOR K\nC1 XOR C2 = P1 XOR P2 if key reused','A fresh CSPRNG key in a lab is not proof of ideal information-theoretic randomness.'),
 ('Rail fence','Write zigzag; read rows\n3-rail pattern: 0,1,2,1,...','Transposition preserves letters; unequal rail lengths are handled without padding.'),
 ('LSB teaching capacity','16 + 8*payload_bytes <= carrier_bytes','Two-byte length header; only synthetic raw channel bytes, not a PNG/JPEG decoder.'),
 ('DES dimensions','64-bit block; 56 effective key bits\n8 parity bits; 16 rounds\n48-bit round subkeys','DES is withdrawn; these are structure facts, not production advice.'),
 ('DES Feistel round','L_i=R_(i-1)\nR_i=L_(i-1) XOR f(R_(i-1),K_i)\nf: expand -> XOR -> S-boxes -> P','Eight 6-to-4-bit S-boxes return 32 bits; final swap precedes IP inverse.')]
SYNTAX=[{'title':tr('Cipher and Formula Quick Reference'),'items':[{'name':tr(n),'f':f,'terms':tr(t)} for n,f,t in CARDS]}]
QA=[
 ('What is plaintext?','The original information supplied to encryption; not necessarily printable text.'),
 ('What is ciphertext?','The transformed encryption output, often represented as bytes or hexadecimal.'),
 ('How does cryptanalysis differ from cryptography?','Cryptography designs/uses protections; cryptanalysis studies defeating goals without the intended secret.'),
 ('What is cryptology?','The field including cryptography and cryptanalysis.'),
 ('Is Base64 encryption?','No. It is an encoding without a secret decryption key.'),
 ('Does hashing have a decryption key?','No. A digest is not ciphertext that can be reversed with a key.'),
 ('What does symmetric-key mean?','Parties share corresponding secret key material for encryption and decryption.'),
 ('Does encryption alone prove sender identity?','No. Suitable authentication, integrity and freshness protection require appropriate additional design.'),
 ('What does substitution change?','Symbols or symbol blocks are replaced according to the cipher/key.'),
 ('What does transposition change?','Positions; the symbols themselves and their counts are retained.'),
 ('Is Hill simply a polyalphabetic cipher?','It is polygraphic substitution on letter vectors; polygraphic and polyalphabetic are different classifications.'),
 ('What is the Caesar formula?','C=(P+k) mod26 and P=(C−k) mod26, using the declared A=0 convention.'),
 ('How many Caesar shifts exist?','26 including identity shift 0; 25 are non-identity.'),
 ('Why can a monoalphabetic permutation leak patterns?','A fixed replacement preserves repeated-letter patterns and relabels letter frequencies.'),
 ('Why is repeating-key Vigenere not an OTP?','Its short key repeats and is not independent uniform secret pad material used once for every message position.'),
 ('What does Playfair encrypt at a time?','Pairs of letters, using a declared 5×5 square and preparation convention.'),
 ('How is I/J handled here?','J maps to I to fit 25 alphabet positions; decryption cannot automatically restore which letter was original.'),
 ('How is BALLOON prepared?','BA LX LO ON, giving BALXLOON.'),
 ('Why does this variant use Q for a repeated/final X?','To avoid creating an XX pair while applying the declared filler rule.'),
 ('Can every X be removed after Playfair decryption?','No. X may be legitimate; the result is prepared text, not a guaranteed recovery of original formatting/fillers.'),
 ('What are the three Playfair cases?','Same row, same column, and rectangle; encryption shifts right/down or swaps columns.'),
 ('What is the Hill key condition modulo 26?','gcd(det(K),26)=1; a nonzero determinant alone is insufficient.'),
 ('Why specify column vectors?','Matrix multiplication direction matters; a different convention may yield a different ciphertext.'),
 ('What is HELP encrypted with [[3,3],[2,5]]?','HIAT under A=0 and column vectors.'),
 ('What is the inverse of that Hill matrix?','[[15,17],[20,9]] modulo 26.'),
 ('Why preserve Hill X padding?','Without trustworthy original-length information, an ending X may be genuine plaintext.'),
 ('What are ideal OTP requirements?','Independent uniform random secret pad material at least as long as the message, with no pad-part reuse.'),
 ('Does an ideal OTP authenticate a message?','No. Perfect confidentiality is not integrity, authentication or replay protection.'),
 ('What happens algebraically if an XOR pad is reused?','C1 XOR C2=P1 XOR P2, exposing a plaintext relation.'),
 ('Why is a secrets.token_bytes demonstration not a proof of perfect secrecy?','It uses an OS-backed CSPRNG; ideal information-theoretic randomness and complete key handling are not proven.'),
 ('What is the three-rail position cycle?','0,1,2,1 repeatedly, with period 4.'),
 ('Does rail fence change letter frequencies?','No. It changes only positions in normalized text.'),
 ('What does steganography hide?','The existence of communication in a carrier; it does not automatically encrypt or authenticate content.'),
 ('What is DES block size versus effective key size?','A 64-bit data block and 56 effective key bits, commonly represented with 8 additional parity bits.'),
 ('How many DES rounds and subkey bits?','16 Feistel rounds, each using a 48-bit round subkey; eight 6-to-4-bit S-boxes return 32 bits.'),
 ('Why must DES remain historical teaching?','FIPS 46-3 was withdrawn 19 May 2005; single DES is unsuitable for modern protection, and this classroom implementation is not FIPS-validated.')]
VIVA=[{'title':tr('Unit 2 Viva and Short Revision'),'items':[{'q':tr(q),'a':tr(a)} for q,a in QA]}]
