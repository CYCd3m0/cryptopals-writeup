from Crypto.Util.strxor import strxor
from binascii import unhexlify

def repeatingKeyXor(s, key):
    q = len(s) // len(key)
    r = len(s) % len(key)
    key = key * q + key[:r]
    return strxor(s, key).hex()

def main():
    s = b'''Burning 'em, if you ain't quick and nimble
I go crazy when I hear a cymbal'''
    key = b'ICE'
    print(repeatingKeyXor(s, key))

if __name__ == '__main__':
    main()