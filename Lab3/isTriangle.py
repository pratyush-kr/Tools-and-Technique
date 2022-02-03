def isTriangle(a, b, c):
    s = (a+b+c)/2
    a2 = s*(s-a)*(s-b)*(s-c)
    if(a2 > 0):
        return True
    elif(a2 <= 0):
        return False

if __name__ == '__main__':
    a = float(input("a: "))
    b = float(input("b: "))
    c = float(input("c: "))
    print(isTriangle(a, b, c))
