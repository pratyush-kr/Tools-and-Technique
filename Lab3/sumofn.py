def sumofn(n:int):
    return int(n*(n+1)/2)


if __name__ == '__main__':
    n = int(input("n: "))
    print(f'sum of integers upto{n} = {sumofn(n)}')