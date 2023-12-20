from Crypto.Util.number import long_to_bytes, bytes_to_long, getPrime
from secret import FLAG

p = getPrime(512)
q = getPrime(512)
r = getPrime(512)

n = p * q
t = q * r

e = 65537
m = bytes_to_long(FLAG)
c = pow(m, e, n)

print(f"{n = }")
print(f"{t = }")
print(f"{c = }")
