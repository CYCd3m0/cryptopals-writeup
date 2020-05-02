from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Random.random import randint
from Crypto.Util.Padding import pad
from Challenge10_Implement_CBC_mode import implementAES_CBC

def encryption_oracle(s):
    s = get_random_bytes(randint(5, 10)) + s + get_random_bytes(randint(5, 10))
    key = get_random_bytes(16)
    mode = randint(0, 1)

    # 0 -> ECB , 1 -> CBC
    if mode :
        IV = get_random_bytes(16)
        return implementAES_CBC(s, key, IV)
    else :
        cipher = AES.new(key, AES.MODE_ECB)
        s = pad(s, 16, style='pkcs7')
        return cipher.encrypt(s)

def main():
    s = b'\x20' * 48
    ct = encryption_oracle(s)
    if ct[16:32] == ct[32:48]:
        print('MODE ECB')
    else :
        print('MODE CBC')

if __name__ == '__main__':
    main()