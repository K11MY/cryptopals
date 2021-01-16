import base64
import binascii
from cryptopalslib import *

with open('6.txt') as input_file:
    ciphertext = base64.b64decode(input_file.read())

for keySize in range(2, 41):
    # hamming distance
