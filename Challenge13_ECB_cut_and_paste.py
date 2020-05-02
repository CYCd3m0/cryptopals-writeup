from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

def profile_for(email):
    email = email.decode('ascii').replace('&', '').replace('=', '').encode()
    encode = b''
    s = {
        b'email': email,
        b'uid': b'10',
        b'role': b'user'
    }
    for i in s.keys():
        if encode != b'' :
            encode += b'&'
        encode += i + b'=' + s[i]
    return encode

def encryptProfile(s, k):
    cipher = AES.new(k, AES.MODE_ECB)
    return cipher.encrypt(pad(s, 16, style='pkcs7'))

def decryptProfile(s, k):
    cipher = AES.new(k, AES.MODE_ECB)
    return cipher.decrypt(s)

def main():
    key = get_random_bytes(16)

    # email_1 -> get E(admin+padding) at second block
    email_1 = b'A' * 10 + b'admin' + b'\x0b' * 11
    encrypt_email_1 = encryptProfile(profile_for(email_1), key)

    # email_2 -> get E(email=...role=) at first 2 blocks
    email_2 = b'A' * 13
    encrypt_email_2 = encryptProfile(profile_for(email_2), key)

    # concatenate!!!
    s = encrypt_email_2[:32] + encrypt_email_1[16:32]
    print(unpad(decryptProfile(s, key), 16, style='pkcs7'))

if __name__ == '__main__':
    main()