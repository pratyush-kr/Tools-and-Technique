if __name__ == '__main__':
    str1 = input('string: ')
    str2 = ''
    idx = 0
    for i in range(0, len(str1)):
        if i == 0:
            str2 += chr(ord(str1[i])-32)
            continue
        str2 += str1[i]
    print(f'{str2}')