from Crypto.Util.strxor import strxor
from Crypto.Random import get_random_bytes
from Challenge10_Implement_CBC_mode import implementAES_CBC, breakAES_CBC

def encryptUserData(s, key, IV):
    s = s.decode('ascii').replace(';', '').replace('=', '').encode()
    s = b'comment1=cooking%20MCs;userdata=' + s + b';comment2=%20like%20a%20pound%20of%20bacon'
    return implementAES_CBC(s, key, IV)

def checkAdmin(s, key, IV):
    plain = breakAES_CBC(s, key, IV)
    if b';admin=true;' in plain:
        return True
    else:
        return False

def main():
    key = get_random_bytes(16)
    IV = get_random_bytes(16)

    # I can manipulate it by bitflipping
    s = b'I_can_control_it'
    ct = encryptUserData(s, key, IV)

    # prevCipher = prevCipher xor currPlain xor whatIwant
    prevBlock = ct[16:32]
    t = strxor(strxor(prevBlock, s), b'AA;admin=true;AA')
    print(checkAdmin(ct[:16] + t + ct[32:], key, IV))

if __name__ == '__main__':
    main()