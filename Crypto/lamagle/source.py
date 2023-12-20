from Crypto.Util.number import *
import random
from string import ascii_letters, digits
from secret import FLAG

ALPHABET = ascii_letters + digits

def gen_params():
    while True:
        q = getPrime(1024)
        p = 2*q + 1
        if isPrime(p):
            if pow(2, q, p) == 1:
                g = 2
                break
    x = getRandomRange(1, q - 1)
    h = pow(g, x, p)
    pubkey = (p, q, g, h)
    return pubkey, x

pub, priv = gen_params()
p, q, g, h = pub

# Entropy is scarce these days. Better use the same for all my messages
randomness = getRandomRange(1, q)

def getrand():
    global randomness
    randomness = randomness >> 8
    return randomness

def elgamal_encrypt(pubkey, msg):
    m = bytes_to_long(msg)
    p, q, g, h = pubkey
    y = getrand()
    if y == 0:
        return 0, 0
    s = pow(h, y, p)
    c1 = pow(g, y, p)
    c2 = m*s % p
    return (c1, c2)

flag_enc = elgamal_encrypt(pub, FLAG)

c2s = []
while True:
    msg = "".join([random.choice(ALPHABET) for _ in range(30)])
    _, c2 = elgamal_encrypt(pub, msg.encode())
    if c2 == 0:
        break
    c2s.append(c2)

with open("output.txt", "w") as f:
    f.write(f"{flag_enc}\n")
    f.write(f"{pub}\n")
    f.write(f"{c2s}\n")
    
