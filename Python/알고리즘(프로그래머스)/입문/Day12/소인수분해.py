'''
소인수분해란 어떤 수를 소수들의 곱으로 표현하는 것입니다. 
예를 들어 12를 소인수 분해하면 2 * 2 * 3 으로 나타낼 수 있습니다. 
따라서 12의 소인수는 2와 3입니다. 
자연수 n이 매개변수로 주어질 때 n의 소인수를 오름차순으로 담은 배열을 return하도록 solution 함수를 완성해주세요.

* 제한 사항
    - 2 ≤ n ≤ 10,000
'''

def solution(n):
    prime_factors = set()   # 소인수를 담을 집합 (중복 제거)
    i = 2
    while i * i <= n:       # n의 제곱근까지만 확인
        if n % i == 0:      # 나누어 떨어지면 i는 소인수
            prime_factors.add(i)
            n //= i         # n을 i로 나눈 몫으로 갱신
        else:
            i += 1          # 안 나누어지면 다음 수 확인
    if n > 1:               # 마지막에 남은 n이 소수라면 추가
        prime_factors.add(n)
    return sorted(prime_factors)

'''
예시1)
def solution(n):
    answer = []
    d = 2
    while d <= n:
        if n % d == 0:
            n /= d
            if d not in answer:
                answer.append(d)
        else:
            d += 1
    return answer

예시2)
def solution(n):
    k = 2
    answer = []
    while n>1:
        if n%k==0:
            answer.append(k)
            while n%k==0:
                n//=k
        k+=1

    return answer
'''