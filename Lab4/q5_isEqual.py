if __name__ == '__main__':
    a, b = int(input('a: ')), int(input('b: '))
    isEqual = lambda a, b: a==b
    print(f"isEqual({a}, {b}) = {isEqual(a, b)}")