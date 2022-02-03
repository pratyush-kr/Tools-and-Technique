def sumofn(n):
    return int(n*(n+1)/2)
if __name__ == '__main__':
    n = int(input('n: '))
    print(f"sumof({n}) = {sumofn(n)}")