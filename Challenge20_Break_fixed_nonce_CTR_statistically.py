from base64 import b64decode

def main():
    strings = []
    with open('Challenge20.txt', 'r') as f:
        for i in f:
            if i[-1] == '\n':
                strings.append(i[:-1])
            else :
                strings.append(i)
    
    for i in strings:
        print(b64decode(i))

if __name__ == '__main__':
    main()