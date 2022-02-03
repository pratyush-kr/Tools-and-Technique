class HashMap:
    def __init__(self):
        self.map = dict()
    def add(self, x):
        try:
            self.map[x] += 1
        except KeyError:
            self.map[x] = 1

def count(str1):
    ctr = HashMap()
    for i in str1:
        ctr.add(i)
    return ctr
if __name__ == '__main__':
    str1 = input('string: ')
    print(count(str1).map)