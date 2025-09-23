from calc import *


class main:

    def __init__(self, a, b):
        self.a = a
        self.b = b

        calc(self.a, self.b)
        print(f'더하기 : {self.a} + {self.b} = {calc.add(self)}')
        print(f'빼기 : {self.a} - {self.b} = {calc.substract(self)}')
        print(f'곱하기 : {self.a} x {self.b} = {calc.multiply(self)}')
        print(f'나누기 : {self.a} / {self.b} = {calc.divide(self)}')


m = main(10, 0)

# 더하기 : 10 + 0 = 10
# 빼기 : 10 - 0 = 10
# 곱하기 : 10 x 0 = 0
# 0으로 나눌 수 없습니다.
# 나누기 : 10 / 0 = None
