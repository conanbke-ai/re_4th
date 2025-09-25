'''
어떤 자연수를 제곱했을 때 나오는 정수를 제곱수라고 합니다. 
정수 n이 매개변수로 주어질 때, n이 제곱수라면 1을 아니라면 2를 return하도록 solution 함수를 완성해주세요.

* 제한 사항
    - 1 ≤ n ≤ 1,000,000
'''

import math

def solution(n):
    
    i = int(math.sqrt(n))
    
    if i ** 2 == n:
        return 1
    
    return 2

'- math.sqrt(n) 만 진행 시, float 형태 제곱할 경우 부정확한 계산으로 인해 실행 에러 발생 가능'

'''
예시1)
def solution(n):
    return 1 if (n ** 0.5).is_integer() else 2

'- is_integer() : 정수 판별'
'''