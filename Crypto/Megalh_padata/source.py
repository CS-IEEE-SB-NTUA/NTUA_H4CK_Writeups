from Crypto.Util.number import long_to_bytes, bytes_to_long, getPrime
import os
from secret import FLAG

assert len(FLAG) == 41

def xor(a, b):
    return bytes([a[i % len(a)] ^ b[i % len(b)] for i in range(max(len(a), len(b)))])
    
def encrypt(message, n, e, pad):
    rsa_ctxt = pow(bytes_to_long(message), e, n)
    ctxt = xor(long_to_bytes(rsa_ctxt), pad)
    return ctxt.hex()

p = getPrime(512)
q = getPrime(512)
n = p * q
e = 3

# They told me I should use "pad" with RSA so I did.
PAD = os.urandom(128)

print("n = ", n)
print("enc_flag =", encrypt(FLAG, n, e, PAD))
message = b"1337"
print("c = ", encrypt(message, n, e, PAD))
