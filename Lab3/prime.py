from math import sqrt
def isPrime(num:int):
    x = 1
    for i in range(2, int(sqrt(num)+1)):
        if(num%i == 0):
            x += 1
        if(x == 2):
            return False
    return True

if __name__ == '__main__':
    num = int(input('num: '))
    print(isPrime(num))