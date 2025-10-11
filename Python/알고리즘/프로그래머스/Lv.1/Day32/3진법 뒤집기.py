'''
자연수 n이 매개변수로 주어집니다. 
n을 3진법 상에서 앞뒤로 뒤집은 후, 이를 다시 10진법으로 표현한 수를 return 하도록 solution 함수를 완성해주세요.

* 제한사항
    - n은 1 이상 100,000,000 이하인 자연수입니다.
'''

def solution(n):
    x = ""

    # 3진법 변환 + 뒤집기
    while n > 0:
        x += str(n % 3)
        n //= 3

    # 뒤집힌 3진수를 10진수로 변환
    return int(x, 3)
'- int(문자열, 진법) : 진법의 문자열을 10진수로 변환'

'''
예시1)
def solution(n):
    answer = 0
    cnt = 1
    a = ''

    while n>0:
        a+=str(n%3)
        n = n//3

    for b in range(len(a),0,-1):
        answer += (int(a[b-1])*cnt)
        cnt *= 3
    return answer

예시2)
def solution(n):
    answer = []
    while True:
        if n < 3:
            answer.append(n)
            break
        answer.append(n % 3)
        n = n // 3
    answer.reverse()
    sum = 0
    for i in range(len(answer)):
        sum += (answer[i] * (3 ** i))
    return sum
'''