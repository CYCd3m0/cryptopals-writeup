from base64 import b64decode
from Crypto.Cipher import AES

def breakAES_ECB(s, k):
    cipher = AES.new(k, AES.MODE_ECB)
    return cipher.decrypt(s)

def main():
    with open('Challenge07.txt', 'r') as f:
        cipher = b64decode(f.read())
    key = b'YELLOW SUBMARINE'
    print(breakAES_ECB(cipher, key))

if __name__ == '__main__':
    main()