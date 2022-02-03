if __name__ == '__main__':
    a, b = int(input('a: ')), int(input('b: '))
    sum = lambda a, b: a+b
    print(f"{a} + {b} = {sum(a, b)}")