from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Random.random import randint
from Crypto.Util.Padding import pad

targetBytes = b"Rollin' in my 5.0\nWith my rag-top down so my hair can blow\nThe girlies on standby waving just to say hi\nDid you stop? No, I just drove by\n"
prefix = get_random_bytes(randint(1, 64))
key = get_random_bytes(16)

def AES_128_ECB(s):
    cipher = AES.new(key, AES.MODE_ECB)
    return cipher.encrypt(pad(prefix + s + targetBytes, 16, style='pkcs7'))

def findNextByte(s):
    prefixLen = len(prefix)
    byteNum = prefixLen + len(s) + 1
    blockNum = (prefixLen + len(s)) // 16

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
    global targetBytes
    global prefix
    global key

    result = b''
    while len(result) < len(targetBytes) :
        c = findNextByte(result)
        result += c
    print(result)

if __name__ == '__main__':
    main()