import binascii
from cryptopalslib import *
a = '1c0111001f010100061a024b53535009181c'
b = '686974207468652062756c6c277320657965'


if __name__ == "__main__":
    b1 = binascii.unhexlify(a)
    b2 = binascii.unhexlify(b)

    print(xor_equal_length(b1, b2))

