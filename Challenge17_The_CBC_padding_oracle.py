from Crypto.Random import get_random_bytes
from Crypto.Random.random import choice
from Crypto.Util.Padding import unpad
from base64 import b64decode
from Challenge10_Implement_CBC_mode import implementAES_CBC, breakAES_CBC

def encryption(key, IV):
    strings = [
        b'MDAwMDAwTm93IHRoYXQgdGhlIHBhcnR5IGlzIGp1bXBpbmc=',
        b'MDAwMDAxV2l0aCB0aGUgYmFzcyBraWNrZWQgaW4gYW5kIHRoZSBWZWdhJ3MgYXJlIHB1bXBpbic=',
        b'MDAwMDAyUXVpY2sgdG8gdGhlIHBvaW50LCB0byB0aGUgcG9pbnQsIG5vIGZha2luZw==',
        b'MDAwMDAzQ29va2luZyBNQydzIGxpa2UgYSBwb3VuZCBvZiBiYWNvbg==',
        b'MDAwMDA0QnVybmluZyAnZW0sIGlmIHlvdSBhaW4ndCBxdWljayBhbmQgbmltYmxl',
        b'MDAwMDA1SSBnbyBjcmF6eSB3aGVuIEkgaGVhciBhIGN5bWJhbA==',
        b'MDAwMDA2QW5kIGEgaGlnaCBoYXQgd2l0aCBhIHNvdXBlZCB1cCB0ZW1wbw==',
        b'MDAwMDA3SSdtIG9uIGEgcm9sbCwgaXQncyB0aW1lIHRvIGdvIHNvbG8=',
        b'MDAwMDA4b2xsaW4nIGluIG15IGZpdmUgcG9pbnQgb2g=',
        b'MDAwMDA5aXRoIG15IHJhZy10b3AgZG93biBzbyBteSBoYWlyIGNhbiBibG93'
    ]
    s = b64decode(choice(strings))
    return implementAES_CBC(s, key, IV)

def checkPadding(ct, key, IV):
    s = breakAES_CBC(ct, key, IV)
    try:
        unpad(s, 16, style='pkcs7')
        return True
    except:
        return False

def findLastByte(partCipher, key, IV, currDecryptBlock, currPlainBlock):
    # padding -> pad bytes(paddingByte) * int(paddingByte)
    paddingByte = len(currDecryptBlock) + 1
    prefix = get_random_bytes(16 - paddingByte)

    # change a byte of prevCipherBlock to bytes(i) -> to get valid padding
    for i in range(256):
        if len(partCipher) > 16 :
            prevCipherBlock = partCipher[-32:-16]
        else :
            prevCipherBlock = IV

        manipulateBlock = prefix + bytes([i]) + bytes([paddingByte ^ x for x in currDecryptBlock])
        manipulateCipher = partCipher[:-32] + manipulateBlock + partCipher[-16:]

        if checkPadding(manipulateCipher, key, IV):
            decryptByte = i ^ paddingByte
            plainByte = decryptByte ^ prevCipherBlock[-paddingByte]
            return bytes([decryptByte] + list(currDecryptBlock)), bytes([plainByte] + list(currPlainBlock))
    raise Exception('padding error!!!')

def findLastBlock(partCipher, key, IV):
    # currDecryptBlock -> D(cipher) , currPlainBlock -> plain
    currDecryptBlock = b''
    currPlainBlock = b''
    for i in range(16):
        currDecryptBlock, currPlainBlock = findLastByte(partCipher, key, IV, currDecryptBlock, currPlainBlock)
    return currPlainBlock

def paddingOracleAttack(ct, key, IV):
    result = b''
    t = len(ct) // 16
    for i in range(t):
        # partCipher -> abort last block which is accomplish (padding works at last block)
        partCipher = ct[:(t-i)*16]
        result = findLastBlock(partCipher, key, IV) + result
    return result

def main():
    key = get_random_bytes(16)
    IV = get_random_bytes(16)
    ct = encryption(key, IV)

    result = paddingOracleAttack(ct, key, IV)
    print(unpad(result, 16, style='pkcs7'))

if __name__ == '__main__':
    main()