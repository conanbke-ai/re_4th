'''
1부터 입력받은 숫자 n 사이에 있는 소수의 개수를 반환하는 함수, solution을 만들어 보세요.

소수는 1과 자기 자신으로만 나누어지는 수를 의미합니다.
(1은 소수가 아닙니다.)

* 제한 조건
    - n은 2이상 1000000이하의 자연수입니다.
'''
'- 에라스토스테네스의 체'
import math

def solution(n):
    if n < 2:
        return 0
    
    # 처음에는 모두 소수(True)라고 가정
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False  # 0과 1은 소수가 아님

    for i in range(2, int(math.sqrt(n)) + 1):
        if sieve[i]:  # 아직 소수로 판정된 수라면
            # i의 배수들은 모두 소수가 아님
            for j in range(i * i, n + 1, i):
                sieve[j] = False

    # True로 남은 인덱스의 개수가 소수 개수
    return sum(sieve)

'''
예시1)
def solution(n):
    num=set(range(2,n+1))

    for i in range(2,n+1):
        if i in num:
            num-=set(range(2*i,n+1,i))
    return len(num)
'- 에라스토스테네스의 체 간결한 버전'
'''