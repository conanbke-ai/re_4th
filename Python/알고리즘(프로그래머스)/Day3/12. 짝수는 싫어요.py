'''
정수 n이 매개변수로 주어질 때, 
    n 이하의 홀수가 오름차순으로 담긴 배열을 return하도록 solution 함수를 완성해주세요.

* 제한사항
- 1 <= n <= 100
'''


def solution(n):
    # 리스트 선언
    answer = []

    # 정수 n+1 만큼 반복
    for i in range(0, n + 1):
        # 리스트에 할당
        answer.append(i)

    # 1부터 끝까지 2의 간격으로 배열담기
    answer = answer[1::2]

    # 오름차순 정렬
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
