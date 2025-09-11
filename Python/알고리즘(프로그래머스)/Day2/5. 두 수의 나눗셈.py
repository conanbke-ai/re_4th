'''
정수 num1과 num2가 주어질 때, num1을 num2로 나눈 뒤, 1000을 곱한 값에 대한 정수 값을 return하도록 solution 함수를 완성해주세요.

* 제한사항
- 0 <= num1 <= 100
- 0 <= num2 <= 100
'''


def solution(num1, num2):
    answer = int((num1 / num2) * 1000)
    return answer


'''
예시1)
def solution(num1, num2):
    return int(num1 / num2 * 1000)

- 변수 저장 시, 비용이 들고 시스템 성능 저하가 올 수 있으므로 재사용없는 함수의 경우, 지역변수 추천 X

예시2)
def solution(num1, num2):
    answer = (num1/num2)*1000
    return answer//1

- int 형 변환 시보다 처리 시간 빠름

예시3)
solution = lambda x, y: 1000 * x // y

- num1과 num2의 범위 제한이 존재하기 때문에 int 형변환 불필요

예시4)
import math

def solution(num1, num2):
    return math.trunc(num1 / num2 * 1000) 

- math 함수 활용
'''
