from cryptopalslib import *
import binascii

# read cipher
ciphers = open('4.txt').read().splitlines()
# loop through hexstring in cipher
for hextStrings in ciphers:
    # unhexlify
    ct = binascii.unhexlify(hextStrings)
    # loop through the key
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
