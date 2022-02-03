def fact(num):
    if(num < 2):
        return 1
    f = 1
    for i in range(2, num+1):
        f *= i
    return f
if __name__ == '__main__':
    num = int(input('num: '))
    print(f'{num}! = {fact(num)}')