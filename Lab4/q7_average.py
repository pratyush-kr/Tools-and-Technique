from posixpath import split


def average(a):
    sum = 0
    for x in a:
        sum += x
    return sum/len(a)
if __name__ == '__main__':
    a = [int(x) for x in input('nums: ').split(', ')]
    print(f"average({a}) = {average(a)}")