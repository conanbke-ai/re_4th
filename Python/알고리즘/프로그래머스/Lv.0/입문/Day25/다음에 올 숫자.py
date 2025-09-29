'''
등차수열 혹은 등비수열 common이 매개변수로 주어질 때, 마지막 원소 다음으로 올 숫자를 return 하도록 solution 함수를 완성해보세요.

* 제한 사항
    - 2 < common의 길이 < 1,000
    - -1,000 < common의 원소 < 2,000
    - common의 원소는 모두 정수입니다.
    - 등차수열 혹은 등비수열이 아닌 경우는 없습니다.
    - 등비수열인 경우 공비는 0이 아닌 정수입니다.
'''

def solution(common):
    # 길이 3 이상이면 첫 두 항으로 판단 가능
    if common[1] - common[0] == common[2] - common[1]:
        # 등차수열
        d = common[1] - common[0]
        return common[-1] + d
    else:
        # 등비수열
        r = common[1] / common[0]
        return common[-1] * r
    
'''
예시1)
def solution(common):
    answer = 0
    a,b,c = common[:3]
    if (b-a) == (c-b):
        return common[-1]+(b-a)
    else:
        return common[-1] * (b//a)
    return answer

예시2)
def solution(common):
    isSequence = common[2] - common[1] == common[1] - common[0]
    if isSequence:
        return common[-1] + common[1] - common[0]
    return common[-1] * (common[1] / common[0])
'''