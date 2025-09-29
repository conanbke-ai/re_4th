'''
정수 n과 정수 배열 numlist가 매개변수로 주어질 때, numlist에서 n의 배수가 아닌 수들을 제거한 배열을 return하도록 solution 함수를 완성해주세요.

* 제한 사항
    - 1 ≤ n ≤ 10,000
    - 1 ≤ numlist의 크기 ≤ 100
    - 1 ≤ numlist의 원소 ≤ 100,000
'''

def solution(n, numlist):
    
    return list(filter(lambda x: x % n == 0, numlist))

'''
예시1)
def solution(n, numlist):
    answer = [i for i in numlist if i%n==0]
    return answer
'''