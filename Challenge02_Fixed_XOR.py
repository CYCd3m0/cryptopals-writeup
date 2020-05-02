from Crypto.Util.strxor import strxor
from binascii import unhexlify

# .hex()  ->  bytes to hex(str)
def bytesXor(s, t):
    return strxor(s, t).hex()

def main():
    s = '1c0111001f010100061a024b53535009181c'
    t = '686974207468652062756c6c277320657965'
    print(bytesXor(unhexlify(s), unhexlify(t)))

if __name__ == '__main__':
    main()