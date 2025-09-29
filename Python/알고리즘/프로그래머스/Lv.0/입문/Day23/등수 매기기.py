'''
영어 점수와 수학 점수의 평균 점수를 기준으로 학생들의 등수를 매기려고 합니다. 
영어 점수와 수학 점수를 담은 2차원 정수 배열 score가 주어질 때, 영어 점수와 수학 점수의 평균을 기준으로 매긴 등수를 담은 배열을 return하도록 solution 함수를 완성해주세요.

* 제한 사항
    - 0 ≤ score[0], score[1] ≤ 100
    - 1 ≤ score의 길이 ≤ 10
    - score의 원소 길이는 2입니다.
    - score는 중복된 원소를 갖지 않습니다.
'''

def solution(score):
    # 각 학생의 평균 구하기
    avg = [sum(s)/2 for s in score]
    
    # 내림차순 정렬 후 등수 매기기
    result = []
    for a in avg:
        rank = 1 + sum(1 for x in avg if x > a)  # 자신보다 평균 높은 학생 수 + 1
        result.append(rank)
    return result

'''
예시1)
def solution(score):
    a = sorted([sum(i) for i in score], reverse = True)
    return [a.index(sum(i))+1 for i in score]

'- index 처리 시, 동점자 처리가 안되는 문제가 발생됨'

예시2)
from functools import reduce

def solution(score):
    totals = reduce(lambda x, y: x + [sum(y)], score, [])
    return [1 + sum(t > s for t in totals) for s in totals]
'''