def gcd(a, b):
    if(a == 0 or b == 0):
        return 0
    elif(a == b):
        return a
    elif(a > b):
        return gcd(a-b, b)
    return gcd(a, b-a)

if __name__ == '__main__':
    a, b = int(input('a: ')), int(input('b: '))
    print(f'gcd({a}, {b}) = {gcd(a, b)}')