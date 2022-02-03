def fact(num):
    if(num < 2):
        return 1
    f = 1
    for i in range(2, num+1):
        f *= i
    return f
if __name__ == '__main__':
    n, r = int(input('n: ')), int(input('r: '))
    P = lambda n, r: int(fact(n) / fact(n-r))
    print(f'{n}P{r} = {P(n, r)}')