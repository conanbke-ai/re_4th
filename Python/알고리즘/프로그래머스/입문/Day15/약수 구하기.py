'''
정수 n이 매개변수로 주어질 때, n의 약수를 오름차순으로 담은 배열을 return하도록 solution 함수를 완성해주세요.

* 제한 사항
    - 1 ≤ n ≤ 10,000
'''

def solution(n):
    
    result = []
    
    for i in range(1, n+1):
        if n % i == 0:
            result.append(i)

    return sorted(result)

print(solution(24))

'''
예시1)
def solution(n):
    return [i for i in range(1,n+1) if n%i == 0]
    
예시2)
def solution(n):
    return list(filter(lambda v: n % v == 0, [i for i in range(1, n//2+1)])) + [n]

'''