def greater(a:int, b:int, c:int):
    max = a
    if(a > max):
        max = a
    if(b > max):
        max = b
    if(c > max):
        max = c
    return max
    

if __name__ == '__main__':
    a = int(input('a: '))
    b = int(input('b: '))
    c = int(input('c: '))
    print(f'Greater({a}, {b}, {c}) = {greater(a, b, c)}')