import math
def solution(n):

    for i in range(10):
        if math.factorial(i) <= n:
            return i
        continue

