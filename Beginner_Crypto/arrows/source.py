from Crypto.Util.number import bytes_to_long
from secret import FLAG

n = bytes_to_long(FLAG.lstrip(b"NH4CK{").rstrip(b"}"))
print((n << 2) ^ (n >> 2))
# 28159761705955253718454662360068272342440885298700051112417729041843661663258713442591709941031131886387
