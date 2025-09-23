'''
외과의사 머쓱이는 응급실에 온 환자의 응급도를 기준으로 진료 순서를 정하려고 합니다. 
정수 배열 emergency가 매개변수로 주어질 때 응급도가 높은 순서대로 진료 순서를 정한 배열을 return하도록 solution 함수를 완성해주세요.

* 제한 사항
     - 중복된 원소는 없습니다.
    - 1 ≤ emergency의 길이 ≤ 10
    - 1 ≤ emergency의 원소 ≤ 100
'''


def solution(emergency):
    # 큰 값이 더 높은 순위가 되도록 내림차순 정렬
    sorted_list = sorted(emergency, reverse=True)

    # 각 값에 순위를 매핑 (1부터 시작)
    rank = {value: idx + 1 for idx, value in enumerate(sorted_list)}

    # 원래 순서대로 순위 반환
    return [rank[e] for e in emergency]


'''
예시1)
def solution(emergency):
    return [sorted(emergency, reverse=True).index(e) + 1 for e in emergency]

예시2)
def solution(emergency):
    answer = []
    emer_ls = {e: i + 1 for i, e in enumerate(sorted(emergency)[::-1])}
    for e in emergency:
        answer.append(emer_ls[e])
    return answer

예시3)
def solution(emergency):
    e = sorted(emergency,reverse=True)
    return [e.index(i)+1 for i in emergency]
'''
