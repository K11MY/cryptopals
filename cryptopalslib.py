import binascii


def hex_to_64(hexString):
    encodedString = hexString
    result = binascii.b2a_base64(binascii.unhexlify(encodedString))
    return result


def xor_equal_length(b1, b2):
    output = b''
    for character in range(len(b1)):
        # we use modulo for repeating value
        xor = bytes([b1[character] ^ b2[character % len(b2)]])
        output += xor
    return output


def gucci_value(b):
    letters = b'ETAOINSHRDLU KMCPHGB,!'[::-1]
    score = 0
    for byte in b.upper():
        score += letters.find(byte)
    return score
