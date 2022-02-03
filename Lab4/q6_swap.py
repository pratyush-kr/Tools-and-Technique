def swap(a, b):
    return b, a
if __name__ == '__main__':
    a, b = int(input('a: ')), int(input('b: '))
    print(f"swap({a}, {b}) = ", end="")
    a, b = swap(a, b)
    print(f"{a}, {b}")