'''
머쓱이는 직육면체 모양의 상자를 하나 가지고 있는데 이 상자에 정육면체 모양의 주사위를 최대한 많이 채우고 싶습니다. 
상자의 가로, 세로, 높이가 저장되어있는 배열 box와 주사위 모서리의 길이 정수 n이 매개변수로 주어졌을 때, 상자에 들어갈 수 있는 주사위의 최대 개수를 return 하도록 solution 함수를 완성해주세요.

* 제한 사항
    - box의 길이는 3입니다.
    - box[0] = 상자의 가로 길이
    - box[1] = 상자의 세로 길이
    - box[2] = 상자의 높이 길이
    - 1 ≤ box의 원소 ≤ 100
    - 1 ≤ n ≤ 50
    - n ≤ box의 원소
    - 주사위는 상자와 평행하게 넣습니다.
'''
# def solution(box, n):
#     w, l, h = box
#     if (w * l * h % n**3) == 0:
#         return w * l * h / n**3
#     else:
#         return w * l * h / n**3
'- 부피 계산을 사용할 경우, 모서리가 맞지 않는 경우를 배제하였기 때문에 틀림'
    
def solution(box, n):
    
    w, l, h = box
    
    width = w // n
    length = l // n
    height = h // n
    
    return width * length * height

'''
예시1)
def solution(box, n):
    x, y, z = box
    return (x // n) * (y // n) * (z // n )


예시2)
def solution(box, n):
    answer = 1
    for b in box:
        answer *= b // n
    return answer

예시3)
import math

def solution(box, n):
    return math.prod(map(lambda v: v//n, box))

'- math.prod(iterable, *, start=1) : 반복 가능한 모든 요소를 start부터 곱해서 결과 반환, Python 3.8 이상에서 사용 가능'

'''