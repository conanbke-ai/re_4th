'''
순서쌍이란 두 개의 숫자를 순서를 정하여 짝지어 나타낸 쌍으로 (a, b)로 표기합니다. 
자연수 n이 매개변수로 주어질 때 두 숫자의 곱이 n인 자연수 순서쌍의 개수를 return하도록 solution 함수를 완성해주세요.

* 제한사항
    - 1 ≤ n ≤ 1,000,000
'''


def solution(n):
    count = 0
    for a in range(1, n+1):
        if n % a == 0:       # a가 n을 나누면
            b = n // a
            if 1 <= b <= n:  # b도 자연수 범위 안에 있으면
                count += 1
    return count


'''
예시1)
def solution(n):
    answer = 0
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            answer += 2

            if i * i == n:
                answer -= 1

    return answer

예시2)
def solution(n):
    return len(list(filter(lambda v: n % (v+1) == 0, range(n))))    

예시3)
def solution(n):
    return len([number for number in range(1, n+1) if n%number == 0])    

예시4)
def solution(n):
    answer =0 
    for i in range(n):
        if n % (i+1) ==0:
            answer +=1
    return answer
'''
