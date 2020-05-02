from base64 import b64decode
from itertools import combinations
from Challenge03_Single_byte_XOR_cipher import freqs, breakSingleByteXor
from Challenge05_Implement_repeating_key_XOR import repeatingKeyXor

def getEditDistance(s, t):
    return sum(bin(s[i] ^ t[i]).count('1') for i in range(len(s)))

def normalized(cipher, keySize):
    blocks = [cipher[i*keySize:(i+1)*keySize] for i in range(4)]
    # combinations -> generate 6 pairs
    pairs = list(combinations(blocks, 2))
    return sum(getEditDistance(i[0], i[1]) / keySize for i in pairs) / 6

def findXorKey(cipher, keySize):
    blocks = [cipher[i*keySize:(i+1)*keySize] for i in range(len(cipher) // keySize )]
    # unzip -> transpose[0] = first byte of each block , transpose[1] = second byte of each block , and so on
    transpose = list(zip(*blocks))
    # x = tuple of int
    key = [breakSingleByteXor(bytes(x)) for x in transpose]
    return bytes(key)

def main():
    with open('Challenge06.txt', 'r') as f:
        cipher = b64decode(f.read())
    # important!!! -> use lambda to iterate first parameter
    keySize = min(range(2,41), key = lambda k: normalized(cipher, k))
    key = findXorKey(cipher, keySize)
    plain = repeatingKeyXor(cipher, key)
    print('key =', key.decode('ascii'))
    print('plain =', plain)

if __name__ == '__main__':
    main()