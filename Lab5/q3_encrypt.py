if __name__ == '__main__':
    str1 = input('string: ')
    encrypt = ''
    key = int(input('Key: '))
    for e in str1:
        encrypt += chr(ord(e)+key)
    str1 = encrypt
    encrypt = ''
    print(f'encrypted = {str1}')
    for e in str1:
        encrypt += chr(ord(e)-key)
    print(f'Decrypted = {encrypt}')