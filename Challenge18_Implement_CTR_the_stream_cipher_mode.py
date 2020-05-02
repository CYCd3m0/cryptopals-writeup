from Crypto.Cipher import AES
from Crypto.Util.strxor import strxor
from base64 import b64decode
from struct import pack

def implementAES_CTR(plain, key, nonce = 0, counter = 0, counterStep = 1):
    if len(plain) == 0 :
        return plain

    cipher = AES.new(key, AES.MODE_ECB)
    keyStream = b''
    while len(keyStream) < len(plain):
        keyStream += cipher.encrypt(pack('<qq', nonce, counter))
        counter += counterStep
    keyStream = keyStream[:len(plain)]
    return strxor(keyStream, plain)

def breakAES_CTR(cipher, key, nonce = 0, counter = 0, counterStep = 1):
    return implementAES_CTR(cipher, key, nonce, counter, counterStep)

def main():
    s = b64decode(b'L77na/nrFsKvynd6HzOoG7GHTLXsTVu9qvY/2syLXzhPweyyMTJULu/6/kXX0KSvoOLSFQ==')
    key = b'YELLOW SUBMARINE'
    print(breakAES_CTR(s, key))
    print(implementAES_CTR(breakAES_CTR(s, key), key) == s)

if __name__ == '__main__':
    main()