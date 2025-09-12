'''
정수 배열 numbers가 매개변수로 주어집니다. 
numbers의 각 원소에 두배한 원소를 가진 배열을 return하도록 solution 함수를 완성해주세요.

* 제한사항
- -10000 <= numbers <= 10000
- 1 <= len(numbers) <= 1000
'''


def solution(numbers):
    answer = []

    for i in numbers:
        answer.append(int(i) * 2)

    return answer


'''
예시1)
def solution(numbers):
    return [num*2 for num in numbers]

- 리스트 컴프리헨션 : 표현식 for 항목 in 반복가능객체 if 조건문 형태

예시2)
def solution(numbers):
    return list(map(lambda x: x * 2, numbers))

- map > list comprehension > map + lambda > for loop 순으로 빠름

예시3)
import numpy as np

def solution(numbers):
    answer = []
    answer = np.array(numbers)*2
    answer = answer.tolist()


    return answer

- numpy 함수 활용

예시4)
def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        answer.append(numbers[i]*2)
    return answer
'''
