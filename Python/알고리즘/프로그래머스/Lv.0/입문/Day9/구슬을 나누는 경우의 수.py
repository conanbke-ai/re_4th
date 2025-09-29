'''
머쓱이는 구슬을 친구들에게 나누어주려고 합니다. 
구슬은 모두 다르게 생겼습니다. 
머쓱이가 갖고 있는 구슬의 개수 balls와 친구들에게 나누어 줄 구슬 개수 share이 매개변수로 주어질 때, balls개의 구슬 중 share개의 구슬을 고르는 가능한 모든 경우의 수를 return 하는 solution 함수를 완성해주세요.

* 제한 사항
    - 1 ≤ balls ≤ 30
    - 1 ≤ share ≤ 30
    - 구슬을 고르는 순서는 고려하지 않습니다.
    - share ≤ balls

'''

import math


def solution(balls, share):
    # Python 3.8 이상에서 사용 가능
    return math.comb(balls, share)


'''
math.comb(n, k)
    - n : 전체 원소 수
    - k : 뽑을 원소 수
    - 반환값 : n개 중 k개를 순서 상관없이 뽑는 경우의 수
'''
'''
math.factorial(n)
    - n : 0 이상 정수
    - 반환값 : n!(n 팩토리얼)
        - n! = 1 * 2 * 3 * ... * n
        - 0! = 1 (수학적 정의)
'''

'''
예시1) 재귀/팩토리얼 계산
def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

def solution(balls, share):
    return factorial(balls) // (factorial(share) * factorial(balls - share))

예시2) 효율적인 반복 계산
def solution(balls, share):
    result = 1
    k = min(share, balls - share)  # 계산 최소화
    for i in range(1, k+1):
        result = result * (balls - i + 1) // i
    return result 

예시3)
def solution(balls, share):
    a, b = 1, 1
    for i in range(1,share+1):
        a *= balls
        balls -= 1
        b *= i
    return int(a / b)

예시4)
import math
def solution(balls, share):
    return math.factorial(balls)/(math.factorial(balls-share)*math.factorial(share))
'''
