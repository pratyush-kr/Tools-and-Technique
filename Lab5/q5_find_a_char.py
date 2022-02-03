def find(ch, str):
    for i in str:
        if ch == i:
            return True
    return False
            
if __name__ == '__main__':
    str1 = input('string: ')
    ch = input('char: ')
    print(f'find({ch}, {str1}) = {find(ch, str1)}')