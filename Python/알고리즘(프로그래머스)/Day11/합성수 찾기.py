'''
약수의 개수가 세 개 이상인 수를 합성수라고 합니다. 
자연수 n이 매개변수로 주어질 때 n이하의 합성수의 개수를 return하도록 solution 함수를 완성해주세요.

* 제한 사항
     - 1 ≤ n ≤ 100
'''

def solution(n):
    count = 0
    for num in range(4, n+1):  # 4부터 n까지 (1,2,3은 합성수가 아님)
        divisors = 0
        for i in range(1, num+1):
            if num % i == 0:
                divisors += 1
        if divisors >= 3:
            count += 1
    return count

'''
🔹 최적화 (약수 세는 반복 줄이기)

약수는 num의 제곱근까지만 확인하고, 나누어떨어지면 2개 추가

이미 약수가 3개 이상이면 합성수로 판단 → 더 이상 계산 안 함
'''
import math

def solution(n):
    count = 0
    for num in range(4, n+1):
        divisors = 0
        for i in range(1, int(math.sqrt(num)) + 1):
            if num % i == 0:
                divisors += 2 if i != num // i else 1
            if divisors >= 3:
                count += 1
                break
    return count


import math

def solution(n):
    if n < 4:
        return 0  # 1~3까지는 합성수가 없음
    
    # 에라토스테네스의 체로 소수 판별
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    
    for i in range(2, int(math.sqrt(n)) + 1):
        if is_prime[i]:
            for j in range(i*i, n+1, i):
                is_prime[j] = False
    
    # 합성수 개수 = n - 1 - 소수 개수
    return n - 1 - sum(is_prime[2:])

'''
예시1)
def get_divisors(n):
    return list(filter(lambda v: n % v ==0, range(1, n+1)))

def solution(n):
    return len(list(filter(lambda v: len(get_divisors(v)) >= 3, range(1, n+1))))

예시2)
def solution(n):
    return len([i for i in range(2, n + 1) if not all(i % j for j in range(2, i))])

'''