'''
머쓱이네 피자가게는 피자를 7 조각으로 잘라 줍니다.
    피자를 나눠먹을 사람의 수 n이 매개변수로 주어질 때, 
    한 사람당 최소 1조각 이상 먹을 수 있는 피자의 판 수를 return 하도록 solution 함수를 완성해주세요.

* 제한사항
    1 <= n <= 100
'''

import math


def solution(n):

    # 올림 처리
    return math.ceil(n/7)


'''
math.ceil : 올림
math.floor : 내림
math.trunc : 버림
math.round : 반올림
'''

'''
예시1)
def solution(n):
    return (n - 1) // 7 + 1
    
예시2)
def solution(n):
    answer = 0

    if n%7 != 0:
        answer = (n//7) + 1
    else:
        answer = n//7

    return answer
'''
