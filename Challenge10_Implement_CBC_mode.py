from base64 import b64decode
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Util.strxor import strxor

def implementAES_CBC(plain, key, IV = b'\x00' * 16):
    plain = pad(plain, 16, style='pkcs7')
    prev = IV
    t = len(plain) // 16
    cipher = AES.new(key, AES.MODE_ECB)
    ciphertext = b''
    for i in range(t):
        block = plain[i*16:(i+1)*16]
        block = strxor(prev, block)
        s = cipher.encrypt(block)
        ciphertext += s
        prev = s
    return ciphertext

# for check
def breakAES_CBC(ct, key, IV = b'\x00' * 16):
    prev = IV
    t = len(ct) // 16
    cipher = AES.new(key, AES.MODE_ECB)
    plaintext = b''
    for i in range(t):
        block = ct[i*16:(i+1)*16]
        s = cipher.decrypt(block)
        s = strxor(prev, s)
        plaintext += s
        prev = block
    return plaintext

def main():
    with open('Challenge10.txt', 'r') as f:
        plain = b64decode(f.read())
    key = b'YELLOW SUBMARINE'
    print('cipher =', implementAES_CBC(plain, key))

if __name__ == '__main__':
    main()