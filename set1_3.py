import binascii
from cryptopalslib import *

ct = binascii.unhexlify(
    '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736')
for i in range(256):
    # make the key
    key = bytes([i])
    # make key length
    key *= len(ct)
    pt = xor_equal_length(key, ct)
    scorevalue = gucci_value(pt)
    # look at the pt and decide whats gucci or not
    if scorevalue > 300:
        print(scorevalue)
        print(pt, key)
