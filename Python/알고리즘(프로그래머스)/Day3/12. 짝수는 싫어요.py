'''
정수 n이 매개변수로 주어질 때, 
    n 이하의 홀수가 오름차순으로 담긴 배열을 return하도록 solution 함수를 완성해주세요.

* 제한사항
- 1 <= n <= 100
'''


def solution(n):
    answer = []
    for i in range(0, n + 1):
        answer.append(i)
    answer = answer[1::2]
    answer.sort()
    return answer


'''
예시1)
def solution(n):
    return [i for i in range(1, n+1, 2)]

예시2)
def solution(n):
    return [x for x in range(n + 1) if x % 2]

예시3)
def solution(n):
    return list(range(1, n+1, 2))


예시4)
def solution(n):
    answer = []

    for i in range(1, n + 1):
        if i % 2 == 1:
            answer.append(i)

    return answer

예시5)
def solution(n):
    n = (n+1)//2
    return [2*i+1 for i in range(n)]
'''
