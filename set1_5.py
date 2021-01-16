import binascii
from cryptopalslib import *
output = b''
i = 0
message = b"Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"
key = b'ICE'
output = xor_equal_length(message, key)
print(binascii.hexlify(output))
