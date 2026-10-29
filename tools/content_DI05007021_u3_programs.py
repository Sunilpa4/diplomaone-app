"""Ten actual RSA/signature/PKI examples; no execution at import time."""
import subprocess,sys,tempfile,textwrap
from pathlib import Path
from subject_DI05007021 import ROOT,tr
HELPERS={'rsa_math.py':ROOT/'tools/infosec_u3_math.py',
         'pki_lab.py':ROOT/'tools/infosec_u3_lab.py'}

def example(n,title,code,expl):
 return {'id':f'sec3p{n:02d}','title':tr(title),
         'code':tr(textwrap.dedent(code).strip()+'\n'),'expl':tr(expl)}

EXAMPLES=[
 example(1,'Practical 6: textbook RSA with public small-number data',r'''
 from rsa_math import toy_keypair, rsa_encrypt, rsa_decrypt

 pair = toy_keypair(61, 53, 17)
 cipher = rsa_encrypt(65, pair)
 print("n:", pair["n"])
 print("phi:", pair["phi"])
 print("public_exponent:", pair["e"])
 print("public_demo_private_exponent:", pair["d"])
 print("ciphertext:", cipher)
 print("recovered:", rsa_decrypt(cipher, pair))
 print("ed_mod_phi:", pair["e"] * pair["d"] % pair["phi"])
 ''','Actually computes n=3233, phi=3120, d=2753 and 65 -> 2790 -> 65. Every number, including the toy private exponent, is PUBLIC classroom data. This fulfils the arithmetic part of Practical 6, not secure message encryption. Real keys need secure generation, much larger parameters, appropriate standardized padding and vetted implementations.'),
 example(2,'RSA computational aspect: modular exponentiation trace',r'''
 from rsa_math import power_trace

 result, rows = power_trace(65, 17, 3233)
 print("successive_powers:", [row["power"] for row in rows])
 print("processed_exponent_bits:", len(rows))
 print("ciphertext:", result)
 print("matches_builtin_pow:", result == pow(65, 17, 3233))
 ''','The helper performs actual square-and-multiply, reducing after each multiplication instead of first constructing the enormous integer 65**17. For exponent 17 the powers are 65,992,1232,1547,789 modulo3233. This is a transparent, bounded teaching implementation, not constant-time production RSA.'),
 example(3,'Why raw textbook RSA is not a secure encryption scheme',r'''
 from rsa_math import toy_keypair, rsa_encrypt

 pair = toy_keypair(61, 53, 17)
 a, b = 2, 3
 c1, c2 = rsa_encrypt(a, pair), rsa_encrypt(b, pair)
 print("same_message_same_raw_cipher:",
       rsa_encrypt(65, pair) == rsa_encrypt(65, pair))
 print("multiplicative_relation:",
       c1 * c2 % pair["n"] == rsa_encrypt(a * b, pair))
 print("fixed_sample_product:", a * b)
 ''','Uses only fixed tiny public classroom values. Raw RSA is deterministic and has an algebraic multiplicative relation: those are warnings against deploying textbook pow-based encryption, not an attack on a live service. Anyone with a public encryption key can encrypt, so ciphertext is not sender authentication.'),
 example(4,'Real RSA-OAEP/SHA-256: recovery, size bound and rejection',r'''
 from pki_lab import Lab

 with Lab() as lab:
     facts = lab.public_facts("recipient")
     message = b"Course S01: public key demo"
     first = lab.oaep_encrypt(message)
     second = lab.oaep_encrypt(message)
     assert first.returncode == second.returncode == 0
     recovered = lab.oaep_decrypt(first.stdout)
     too_long = lab.oaep_encrypt(b"A" * 191)
     changed = bytearray(first.stdout)
     changed[-1] ^= 1
     tampered = lab.oaep_decrypt(bytes(changed))
     assert b"data too large" in too_long.stderr.lower()
     print("rsa_bits:", facts["bits"])
     print("public_exponent:", facts["public_exponent"])
     print("ciphertext_bytes:", len(first.stdout))
     print("oaep_sha256_max_bytes:", facts["bits"] // 8 - 66)
     print("randomized_ciphertexts:", first.stdout != second.stdout)
     print("recovered_matches:", recovered.stdout == message)
     print("oversize_rejected:", too_long.returncode != 0)
     print("tampered_rejected:", tampered.returncode != 0)
 ''','Actual OpenSSL generates a fresh 2048-bit RSA key and performs OAEP with SHA-256 and MGF1-SHA-256. The 256-byte modulus allows at most256−2×32−2=190 message bytes under this profile; a191-byte input is really rejected. Random ciphertext/key bytes are not published. This is not a complete authenticated messaging protocol, TLS implementation or promise that a2048-bit key is suitable forever.'),
 example(5,'Real RSA-PSS/SHA-256: signature and tamper/wrong-key checks',r'''
 from pki_lab import Lab

 with Lab() as lab:
     message = b"Course document: approved version 1"
     signature = lab.pss_sign(message)
     print("signature_bytes:", len(signature))
     print("original_valid:", lab.pss_verify(message, signature))
     print("modified_valid:",
           lab.pss_verify(b"Modified course document", signature))
     print("wrong_key_valid:",
           lab.pss_verify(message, signature, "other"))
 ''','Really signs using RSA-PSS, SHA-256 and digest-length salt and verifies the original, modified data and a separately generated wrong public key. A signature is not described as encrypting a message with the private key. Public-key authenticity, private-key control, identity binding and evidence procedures remain necessary; mathematical validity alone does not prove a human action, truth or a legal outcome.'),
 example(6,'CSR signature: key possession is not identity vetting',r'''
 from pki_lab import Lab, HOST

 with Lab() as lab:
     request = lab.request("learner", "Course Learner S01", HOST)
     der = lab.run("req", "-in", request, "-outform", "DER").stdout
     modified = bytearray(der)
     modified[-1] ^= 1
     bad = lab.write("bad.csr.der", bytes(modified))
     print("original_csr_signature_valid:", lab.request_valid(request))
     print("modified_csr_signature_valid:", lab.request_valid(bad, True))
     print("ra_identity_vetting_performed:", False)
 ''','Creates and really verifies a PKCS#10 request, then flips a signature byte in its DER copy and observes rejection. The request contains a public key and a signature made with its corresponding private key, not that private key. Possession of a key does NOT establish that the requested name belongs to the requester; RA/CA identity checks are conceptual here, not performed.'),
 example(7,'Local CA -> intermediate -> server certificate chain',r'''
 from pki_lab import Lab, HOST

 with Lab() as lab:
     lab.pki()
     names = lab.run("x509", "-in", lab.path("leaf.cert.pem"),
                     "-noout", "-subject", "-issuer",
                     "-nameopt", "RFC2253").stdout.decode().splitlines()
     san = lab.run("x509", "-in", lab.path("leaf.cert.pem"),
                   "-noout", "-ext", "subjectAltName").stdout.decode()
     result = lab.verify()
     print(names[0])
     print(names[1])
     print("reserved_SAN_present:", "DNS:" + HOST in san)
     print("explicit_lab_trust_path_valid:", result.returncode == 0)
     print("public_CA_enrollment:", False)
 ''','Actual fresh RSA keys, signed root/intermediate/leaf certificates and OpenSSL path verification are used. The root is trusted ONLY because this isolated verifier explicitly receives the owned lab root. No browser/system trust store is changed; no public CA, real domain, external enrollment, RA vetting or live TLS handshake is involved.'),
 example(8,'Real certificate validation matrix: reject five bad profiles',r'''
 from pki_lab import Lab

 def rejected(result, code):
     text = (result.stdout + result.stderr).decode(errors="replace")
     return result.returncode != 0 and f"error {code} at " in text

 with Lab() as lab:
     print("valid_profile:", lab.verify().returncode == 0)
     print("wrong_hostname_rejected:",
           rejected(lab.verify(hostname="wrong.diploma.test"), 62))
     print("wrong_purpose_rejected:",
           rejected(lab.verify(purpose="sslclient"), 26))
     print("missing_intermediate_rejected:",
           rejected(lab.verify(intermediate=False), 20))
     print("expired_at_evaluation_time_rejected:",
           rejected(lab.verify(attime=lab.expiry_epoch() + 1), 10))
     print("unrelated_root_rejected:",
           rejected(lab.verify(root=lab.unrelated_root()), 20))
 ''','Actual OpenSSL failures are checked for the expected verification error codes, not merely any failed command. The matrix checks five bad cases (hostname, usage, missing issuer, expiry and unrelated root) plus a positive control. Expiry uses an explicit evaluation timestamp, not a changed OS clock. No bypass flags, network fetching or system-root installation are used.'),
 example(9,'Actual local leaf CRL check before and after revocation',r'''
 from pki_lab import Lab

 with Lab() as lab:
     before = lab.verify(crl=lab.crl())
     after = lab.verify(crl=lab.crl(revoke=True))
     unchecked = lab.verify()
     text = (after.stdout + after.stderr).decode(errors="replace")
     print("before_revocation_valid:", before.returncode == 0)
     print("revoked_with_supplied_CRL_rejected:",
           after.returncode != 0 and "error 23 at " in text)
     print("path_without_CRL_still_valid:", unchecked.returncode == 0)
     print("full_chain_revocation_or_OCSP_checked:", False)
 ''','A real local CA database issues the leaf, generates a CRL, marks that leaf revoked and generates a replacement CRL. Explicit leaf CRL checking then rejects it. Ordinary path verification alone still succeeds, demonstrating that path validity is not a revocation-status assertion. Only the leaf is checked against a locally supplied CRL; full-chain revocation, live CRL download and OCSP are NOT performed.'),
 example(10,'Certificate integrity: modified signature and private-key cleanup',r'''
 import stat
 from pki_lab import Lab

 with Lab() as lab:
     lab.pki()
     der = lab.run("x509", "-in", lab.path("leaf.cert.pem"),
                   "-outform", "DER").stdout
     modified = bytearray(der)
     modified[-1] ^= 1
     bad = lab.write("bad.cert.der", bytes(modified))
     result = lab.verify(certificate=bad)
     text = (result.stdout + result.stderr).decode(errors="replace")
     modes = {stat.S_IMODE(p.stat().st_mode)
              for p in lab.folder.glob("*.key.pem")}
     print("original_profile_valid:", lab.verify().returncode == 0)
     print("modified_signature_rejected:",
           result.returncode != 0 and "error 7 at " in text)
     print("private_key_modes_0600:", modes == {0o600})
     folder = lab.folder
 print("temporary_lab_removed:", not folder.exists())
 ''','Actually modifies the certificate signature bytes and gets a signature-validation failure under the correct lab trust profile. All fresh private-key files are restricted to0600 within a0700 temporary directory and removed at context exit, including failure cleanup paths tested separately. No private PEM material is exported in notes, expected outputs or the ZIP. This disposable lab is not a production CA or arbitrary-code security sandbox.')]

def run_program(example):
 with tempfile.TemporaryDirectory(prefix='infosec-u3-example-') as td:
  folder=Path(td)
  for name,source in HELPERS.items():(folder/name).write_text(source.read_text())
  script=folder/(example['id']+'.py');script.write_text(example['code']['en'])
  result=subprocess.run([sys.executable,'-E',str(script)],cwd=folder,text=True,capture_output=True,timeout=60)
  assert result.returncode==0,(example['id'],result.stderr)
  assert not result.stderr,(example['id'],result.stderr)
 return dict(example,out=result.stdout)

def execute_all():return [run_program(p) for p in EXAMPLES]
