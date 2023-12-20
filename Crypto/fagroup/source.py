from Crypto.Util.number import getPrime, isPrime, bytes_to_long
import random
from secret import FLAG

primes_between_32_and_64 = [i for i in range(32, 64) if isPrime(i)]

def getStrongPrime(nbits):
    assert nbits >= 512
    while True:
        q = getPrime(nbits - 28) * 2
        small_primes = [random.choice(primes_between_32_and_64) for i in range(5)]
        for sp in small_primes:
            q *= sp
        q += 1
        if isPrime(q):
            return q
        
def magic_function(p, q, n): 
    # REDACTED ...
    return ord, r
    
  
p = getStrongPrime(512)
q = getStrongPrime(512)
e = 65537
n = p*q
print(f"{n = }")
ord, r = magic_function(p, q, n)
assert pow(r, ord, n) == 1
print(f"{ord = }")
# print(f"{r = }") # oops, naughty kids don't get presents for christmas

m = bytes_to_long(FLAG)
c = pow(m, e, n)
print(f"{c = }")
