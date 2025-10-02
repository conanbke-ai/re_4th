'''
길이가 같은 두 1차원 정수 배열 a, b가 매개변수로 주어집니다. 
a와 b의 내적을 return 하도록 solution 함수를 완성해주세요.

이때, a와 b의 내적은 a[0]*b[0] + a[1]*b[1] + ... + a[n-1]*b[n-1] 입니다. (n은 a, b의 길이)

* 제한 사항
    - a, b의 길이는 1 이상 1,000 이하입니다.
    - a, b의 모든 수는 -1,000 이상 1,000 이하입니다.
'''

import numpy as np

def solution(a, b):
    
    a = np.array(a)
    b = np.array(b)
    
    return int(np.matmul(a, b))

'- return 시, int()로 감싸서 정수형으로 변환해주어야 함. np.matmul()의 반환형이 numpy.int64이기 때문.'

'''
예시1)
def solution(a, b):

    return sum([x*y for x, y in zip(a,b)])

예시2)
def solution(a, b):
    c = []
    for i in range(len(a)):
        c.append(a[i]*b[i])
    return sum(c)
'''