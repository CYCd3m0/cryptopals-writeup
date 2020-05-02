from Challenge03_Single_byte_XOR_cipher import freqs, breakSingleByteXor
from binascii import unhexlify

def main():
    lines = []
    # read file
    with open('Challenge04.txt', 'r') as f:
        for line in f:
            if line[-1] == '\n':
                lines.append(line[:-1])
            else:
                lines.append(line)
    
    maxScore = 0
    for line in lines:
        score = 0
        line = line.encode()
        key = breakSingleByteXor(unhexlify(line))
        plain = ''.join(chr(key ^ i) for i in unhexlify(line))

        for i in plain:
            if i.lower() in freqs.keys():
                score += freqs[i.lower()]
        if score > maxScore:
            maxScore = score
            result = [key, plain]

    print('key =', chr(result[0]))
    print('plain text =', result[1])

if __name__ == '__main__':
    main()