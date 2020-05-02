from Crypto.Util.Padding import unpad

def pkcs7_validation(s):
    try:
        t = unpad(s, 16, style='pkcs7')
        return True, t
    except:
        return False

def main():
    s = b'ICE ICE BABY\x04\x04\x04\x04'
    print('validation :', pkcs7_validation(s))

if __name__ == '__main__':
    main()