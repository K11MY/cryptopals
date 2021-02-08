import base64
import binascii
from cryptopalslib import *

with open('6.txt') as input_file:
    ciphertext = base64.b64decode(input_file.read())

# hamming distance 
def hamming_distance(encoded1, encoded2):
    difference = 0
    for byte in xor(encoded1,encoded2):
        difference += bin(byte).count("1")
    return difference

distances = []
for keySize in range(2, 41):
    #seperate the cipher text into chunks of the key size
    # get amount of chunks in ciphertext by the keysize
    chunks = (len(ciphertext) // keySize) - 1
    distance = 0
    
    for i in range(chunks):

        chunk_1 = ciphertext[i*keySize:(i+1)*keySize]

        chunk_2 = ciphertext[(i+1)*keySize:(i+2)*keySize]

        distance += hamming_distance(chunk_1, chunk_2) / keySize

    average = distance / chunks 

    distances.append([average, keySize])


lowest_score = sorted(distances, key=lambda k:k[0])
keySize = lowest_score[0][1]
print(keySize)

key = b''
for i in range(keySize):
    key += break_singlebyte_xor(ciphertext[i::keySize])['key']
    print(key)
xor = xor(ciphertext, key)
print(xor)


