import math

class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def add(self):
        return self.a + self.b
    def sub(self):
        return self.a - self.b
    def multiply(self):
        return self.a * self.b
    def divide(self):
        return self.a / self.b
    def pow(self):
        return self.a ** self.b
    def log10(self):
        return math.log10(self.a), math.log10(self.b)
    def log_base_b_a(self):
        return math.log10(self.a)/math.log10(self.b)
    def log2(self):
        return math.log2(self.a), math.log2(self.b)

if __name__ == '__main__':
    a = float(input('a: '))
    b = float(input('b: '))
    calculator = Calculator(a, b)
    print(f'{a} + {b} = {calculator.add()}')
    print(f'{a} - {b} = {calculator.sub()}')
    print(f'{a} * {b} = {calculator.multiply()}')
    print(f'{a} / {b} = {calculator.divide()}')
    print(f'{a}^{b} = {calculator.pow()}')
    print(f'log10({a}), log10({b}) = {calculator.log10()}')
    print(f'log{b}({a}) =  {calculator.log_base_b_a()}')
    print(f'log2({a}), log2({b}) = {calculator.log2()}')