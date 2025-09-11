'''
정수 num1과 num2가 주어질 때, 두 수가 같으면 1, 다르면 -1을 return 하도록 완성해주세요.

* 제한사항
- 0 <= num1 <= 10000
- 0 <= num2 <= 10000
'''


def solution(num1, num2):
    if num1 == num2:
        answer = 1
    else:
        answer = -1
    return answer


'''
예시1)
def solution(num1, num2):
    return 1 if num1==num2 else -1

- 파이토닉
- 리스트 컴프리헨션
- 삼항연산자

예시2)
def solution(num1, num2):
    return sum([num1==num2])*2-1

- int 형 변환 시보다 처리 시간 빠름

예시3)
def solution(num1, num2):
    answer = -1
    if num1 == num2 :
        answer = 1
    return answe

예시4)
def solution(num1, num2):
    return ((num1 == num2)-0.5)*2 

'''
