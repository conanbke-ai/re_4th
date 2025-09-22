'''
정수가 담긴 배열 numbers와 문자열 direction가 매개변수로 주어집니다. 
배열 numbers의 원소를 direction방향으로 한 칸씩 회전시킨 배열을 return하도록 solution 함수를 완성해주세요.

* 제한 사항
    - 3 ≤ numbers의 길이 ≤ 20
    - direction은 "left" 와 "right" 둘 중 하나입니다.
'''

from collections import deque


def solution(numbers, direction):

    array = deque(numbers)

    # 방향이 right 인 경우
    if direction == "right":
        # 오른쪽 방향으로 1칸
        array.rotate(1)
    # 방향이 left 인 경우
    elif direction == "left":
        # 왼쪽 방향으로 1칸
        array.rotate(-1)
    else:
        pass

    return list(array)


'''
예시1)
def solution(numbers, direction):
    return [numbers[-1]] + numbers[:-1] if direction == 'right' else numbers[1:] + [numbers[0]]


예시2)
def solution(numbers, direction):
    if direction == "right":
        answer = [numbers[-1]] + numbers[:len(numbers)-1]
    else:
        answer = numbers[1:] + [numbers[0]]
    return answer

예시3)
def solution_slice(numbers, direction):
    if direction == "right":
        # 마지막 요소 + 나머지
        return [numbers[-1]] + numbers[:-1]
    elif direction == "left":
        # 맨 앞 빼고 + 맨 앞
        return numbers[1:] + [numbers[0]]

예시4)
def solution(numbers, direction):
    if direction == 'right':
        numbers.insert(0,numbers.pop())
    else:
        numbers.append(numbers.pop(0))
    return numbers
'''
