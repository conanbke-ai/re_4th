'''
머쓱이네 피자가게는 피자를 7 조각으로 잘라 줍니다.
    피자를 나눠먹을 사람의 수 n이 매개변수로 주어질 때, 
    한 사람당 1조각 이상 먹을 수 있는 피자의 판 수를 return 하도록 solution 함수를 완성해주세요.

* 제한사항
    1 <= n <= 100
'''

import math

def solution(n):
    # 6과 n의 최소공배수
    l = n * 6 // math.gcd(n, 6)
    # 판 수
    return l // 6

'''
예시1)
def solution(n):
    answer = 1
    while 6 * answer % n:
        answer += 1
    return answer
    
예시2)
def solution(n):
    def gcd(a, b):
        while b > 0:
            a, b = b, a%b
        return a

    return n // gcd(n, 6)
    
    - modulo('%') 성질 때문에 base condition에 충족하지 않으면 gcd 함수를 재귀로 호출해서 알아서 스왑해줌
'''