def main():
    lines = []
    # read file
    with open('Challenge08.txt', 'r') as f:
        for line in f:
            if line[-1] == '\n':
                lines.append(line[:-1])
            else:
                lines.append(line)
    
    lineNum = 0
    # detect AES ECB
    for line in lines:
        lineNum += 1
        blocks = [line[i*32:(i+1)*32] for i in range(10)]
        blockSet = set(blocks)
        if len(blockSet) < 10:
            print('line :', lineNum)
            print('cipher :', line)

if __name__ == '__main__':
    main()