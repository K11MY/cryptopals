import binascii


def hex_to_64(hexString):
    encodedString = hexString
    result = binascii.b2a_base64(binascii.unhexlify(encodedString))
    return result


def xor(b1, b2):
    output = b''
    for character in range(max(len(b1), len(b2))):
        # we use modulo for repeating value
        xor = bytes([b1[character % len(b1)] ^ b2[character % len(b2)]])
        output += xor
    return output


def gucci_value(b):
    letters = b'ETAOINSHRDLU KMCPHGB,!'[::-1]
    score = 0
    for byte in b.upper():
        score += letters.find(byte)
    return score

def break_singlebyte_xor(ct):
    potential_pt = []
    for i in range(256):
        key = bytes([i])
        plaintext = xor(ct, key)
        scorevalue = gucci_value(plaintext)
        score = {
            'key': key,
            'plaintext': plaintext, 
            'score': scorevalue
        }
        potential_pt.append(score)
    plaintext = sorted(potential_pt, key=lambda x:x['score'], reverse=True)[0]
    return plaintext