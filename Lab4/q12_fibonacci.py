def fibonnaci(n):
    if(n == 0):
        return 0
    if(n <= 2):
        return 1
    return fibonnaci(n-1) + fibonnaci(n-2)

if __name__ == '__main__':
    n = int(input('n: '))
    print(f'[{0}', end='')
    for x in range(1, n):
        print(f', {fibonnaci(x)}', end='')
    print(']')