from Crypto.Util.Padding import pad

def main():
    s = b'YELLOW SUBMARINE'
    print(pad(s, 20, style='pkcs7'))

if __name__ == '__main__':
    main()