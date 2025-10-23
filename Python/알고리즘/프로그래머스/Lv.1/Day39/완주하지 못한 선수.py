'''
수많은 마라톤 선수들이 마라톤에 참여하였습니다. 
단 한 명의 선수를 제외하고는 모든 선수가 마라톤을 완주하였습니다.

마라톤에 참여한 선수들의 이름이 담긴 배열 participant와 완주한 선수들의 이름이 담긴 배열 completion이 주어질 때, 완주하지 못한 선수의 이름을 return 하도록 solution 함수를 작성해주세요.

* 제한사항
    - 마라톤 경기에 참여한 선수의 수는 1명 이상 100,000명 이하입니다.
    - completion의 길이는 participant의 길이보다 1 작습니다.
    - 참가자의 이름은 1개 이상 20개 이하의 알파벳 소문자로 이루어져 있습니다.
    - 참가자 중에는 동명이인이 있을 수 있습니다.
'''

def solution(participant, completion):
    from collections import Counter

    return list((Counter(participant) - Counter(completion)).keys())[0]

# {'leo': 1, 'kiki': 1, 'eden': 1} - {'eden': 1, 'kiki': 1}
# 결과: {'leo': 1}

'''
예제1) 정렬
def solution(participant, completion):
    participant.sort()
    completion.sort()
    for p, c in zip(participant, completion):
        if p != c:
            return p
    return participant[-1]

예제2) 해시함수 사용
def solution(participant, completion):
    answer = ''
    temp = 0
    dic = {}
    for part in participant:
        dic[hash(part)] = part   # 이름의 해시값을 key로 저장
        temp += hash(part)       # 모든 참가자 이름의 해시값을 더함
    for com in completion:
        temp -= hash(com)        # 완주자의 해시값만큼 뺌
    answer = dic[temp]           # 남은 해시값의 이름을 찾아서 반환
    return answer

'- ⚠️ 단점 (주의할 점)

파이썬의 hash()는 실행할 때마다 달라집니다.
(보안상 랜덤 시드가 적용됨 → 해시 값이 프로세스마다 다름)

즉, 다른 실행 환경에서 dic[temp]가 맞지 않을 수도 있습니다.

그래서 이 코드는 “이론상 맞지만”,
프로그래머스 같은 단일 실행 환경에서는 정답,
그러나 “재실행 시 결과가 바뀔 수 있는 위험”이 있습니다.'

예제3) 재현 가능한 해시함수(파이썬 내장 hash() 대신 hashlib의 md5나 sha256을 쓰면 안전합니다.)
import hashlib

def solution(participant, completion):
    dic = {}
    temp = 0
    for part in participant:
        # 각 참가자의 이름을 **MD5 해시값(정수형)**으로 변환
            # → 이름마다 고유한 큰 정수값을 얻습니다.
            # → 딕셔너리에 {해시값: 이름} 저장
            # → 전체 해시값의 합을 temp에 누적
        h = int(hashlib.md5(part.encode()).hexdigest(), 16)
        dic[h] = part
        temp += h
    for com in completion:
        # 완주자들의 해시값을 temp에서 차감
        temp -= int(hashlib.md5(com.encode()).hexdigest(), 16)
    
    # 남은 temp는 완주하지 못한 사람의 해시값 → 이름 반환
    return dic[temp]

'- md5는 암호학적으로 안전하지 않지만, 여기선 문제 없음'
'''