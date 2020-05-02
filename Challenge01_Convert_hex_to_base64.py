from base64 import b64encode
from binascii import unhexlify

def hexToBase64(s):
    s = unhexlify(s)
    return b64encode(s).decode('ascii')

def main():
    x = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
    print(hexToBase64(x))
    
if __name__ == '__main__':
    main()