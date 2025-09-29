'''
점 네 개의 좌표를 담은 이차원 배열  dots가 다음과 같이 매개변수로 주어집니다.

[[x1, y1], [x2, y2], [x3, y3], [x4, y4]]
주어진 네 개의 점을 두 개씩 이었을 때, 두 직선이 평행이 되는 경우가 있으면 1을 없으면 0을 return 하도록 solution 함수를 완성해보세요.

* 제한사항
    - dots의 길이 = 4
    - dots의 원소는 [x, y] 형태이며 x, y는 정수입니다.
    - 0 ≤ x, y ≤ 100
    - 서로 다른 두개 이상의 점이 겹치는 경우는 없습니다.
    - 두 직선이 겹치는 경우(일치하는 경우)에도 1을 return 해주세요.
    - 임의의 두 점을 이은 직선이 x축 또는 y축과 평행한 경우는 주어지지 않습니다.
'''

def solution(dots):
    x1, y1 = dots[0]
    x2, y2 = dots[1]
    x3, y3 = dots[2]
    x4, y4 = dots[3]

    # 세 가지 두 직선 조합
    slopes = [
        ((y2-y1)/(x2-x1), (y4-y3)/(x4-x3)),
        ((y3-y1)/(x3-x1), (y4-y2)/(x4-x2)),
        ((y4-y1)/(x4-x1), (y3-y2)/(x3-x2))
    ]

    # 평행 여부 확인
    for s1, s2 in slopes:
        if s1 == s2:
            return 1
    return 0

'''
예시1)
def solution(dots):
    [[x1, y1], [x2, y2], [x3, y3], [x4, y4]]=dots
    answer1 = ((y1-y2)*(x3-x4) == (y3-y4)*(x1-x2))
    answer2 = ((y1-y3)*(x2-x4) == (y2-y4)*(x1-x3))
    answer3 = ((y1-y4)*(x2-x3) == (y2-y3)*(x1-x4))
    return 1 if answer1 or answer2 or answer3 else 0

예시2)
from itertools import combinations

def solution(dots):
    a = []
    for (x1,y1),(x2,y2) in combinations(dots,2):
        a.append((y2-y1,x2-x1))

    for (x1,y1),(x2,y2) in combinations(a,2):
        if x1*y2==x2*y1:
            return 1
    return 0

'- itertools.combinations 기본 개념
    combinations(iterable, r)는 순서를 고려하지 않고 r개를 뽑는 모든 조합을 만들어주는 함수입니다.
    - 순서 중요하지 않음 → (A,B)와 (B,A)는 같은 조합
    - 반복 없음 → 같은 요소를 여러 번 선택하지 않음'

예시3)
def solution(dots):
    return int(any(
        (y2-y1)/(x2-x1) == (y4-y3)/(x4-x3)
        for (x1,y1),(x2,y2),(x3,y3),(x4,y4) in [(dots[0],dots[1],dots[2],dots[3]),
                                                 (dots[0],dots[2],dots[1],dots[3]),
                                                 (dots[0],dots[3],dots[1],dots[2])])
    )
'''
