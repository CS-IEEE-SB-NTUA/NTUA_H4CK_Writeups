from base64 import b64encode, b64decode
from secret import FLAG

def encrypt1(msg):
    while len(msg) < 1000:
        msg = b64decode(b64encode(msg).hex())
    return msg

def encrypt2(msg):
    return [n*7 - 37 ^ 337 + 1337 for n in msg]

enc1 = encrypt1(FLAG)
enc2 = encrypt2(enc1)
print(enc2)
