from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes
from base64 import b64decode

key = get_random_bytes(16)

append = b'''Um9sbGluJyBpbiBteSA1LjAKV2l0aCBteSByYWctdG9wIGRvd24gc28gbXkg
aGFpciBjYW4gYmxvdwpUaGUgZ2lybGllcyBvbiBzdGFuZGJ5IHdhdmluZyBq
dXN0IHRvIHNheSBoaQpEaWQgeW91IHN0b3A/IE5vLCBJIGp1c3QgZHJvdmUg
YnkK'''

# let append to be unknown-string
append = b64decode(append)

def AES_128_ECB(s):
    cipher = AES.new(key, AES.MODE_ECB)
    return cipher.encrypt(pad(s + append, 16, style='pkcs7'))

def discoverBlockSize():
    i = 1
    l = len(AES_128_ECB(b''))
    while True:
        s = b'A' * i
        ct = AES_128_ECB(s)
        if len(ct) > l :
            return len(ct) - l
        i += 1

def detectECB(blockSize):
    s = b'A' * (blockSize * 2)
    ct = AES_128_ECB(s)
    if ct[:blockSize] == ct[blockSize:2*blockSize] :
        return True
    else :
        return False

def findNextByte(s):
    byteNum = len(s) + 1
    blockNum = len(s) // 16

    if byteNum % 16 != 0 :
        paddingCnt = 16 - (byteNum % 16)
    else :
        paddingCnt = 0

    for i in range(256):
        guess = AES_128_ECB(b'A' * paddingCnt + s + bytes([i]))[16*blockNum:16*(blockNum+1)]
        target = AES_128_ECB(b'A' * paddingCnt)[16*blockNum:16*(blockNum+1)]
        if guess == target :
            return bytes([i])

def main():
    global key
    global append
    blockSize = discoverBlockSize()
    print(detectECB(blockSize))

    result = b''
    while len(result) < len(append) :
        c = findNextByte(result)
        result += c
    print(result)

if __name__ == '__main__':
    main()