'''
소수점 아래 숫자가 계속되지 않고 유한개인 소수를 유한소수라고 합니다. 
분수를 소수로 고칠 때 유한소수로 나타낼 수 있는 분수인지 판별하려고 합니다. 
유한소수가 되기 위한 분수의 조건은 다음과 같습니다.

기약분수로 나타내었을 때, 분모의 소인수가 2와 5만 존재해야 합니다.
두 정수 a와 b가 매개변수로 주어질 때, a/b가 유한소수이면 1을, 무한소수라면 2를 return하도록 solution 함수를 완성해주세요.

* 제한 사항
    - a, b는 정수
    - 0 < a ≤ 1,000
    - 0 < b ≤ 1,000
'''

# import math

# def solution(a, b):
#     if math.gcd(a, b):
#         if b % a % 2 == 0:
#             if b % a % 5 == 0:
#                 return 1
#     else:
#         if b % 2 == 0:
#             if b % a % 5 == 0:
#                 return 1
                
#     return 2

import math

def solution(a, b):
    g = math.gcd(a, b)
    b //= g  # 기약분수로 만들기

    while b % 2 == 0:
        b //= 2
    while b % 5 == 0:
        b //= 5

    return 1 if b == 1 else 2

'''
예시1)
def solution(a, b):
    answer = 0
    for i in range(2, min([a, b]) + 1):
        while a % i == 0 and b % i == 0:
            a = a // i
            b = b // i
    while b % 2 == 0:
        b = b // 2
    while b % 5 == 0:
        b = b // 5
    if b == 1:
        answer = 1
    else:
        answer = 2
    return answer

예시2)
from math import gcd

def solution(a, b):
    b = b / gcd(a, b)
    for i in [2, 5]:
        while not b % i:
            b //= i

    return 1 if b == 1 else 2
'''