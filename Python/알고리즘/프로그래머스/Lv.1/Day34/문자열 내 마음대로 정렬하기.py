'''
문자열로 구성된 리스트 strings와, 정수 n이 주어졌을 때, 각 문자열의 인덱스 n번째 글자를 기준으로 오름차순 정렬하려 합니다. 예를 들어 strings가 ["sun", "bed", "car"]이고 n이 1이면 각 단어의 인덱스 1의 문자 "u", "e", "a"로 strings를 정렬합니다.

* 제한 조건
    - strings는 길이 1 이상, 50이하인 배열입니다.
    - strings의 원소는 소문자 알파벳으로 이루어져 있습니다.
    - strings의 원소는 길이 1 이상, 100이하인 문자열입니다.
    - 모든 strings의 원소의 길이는 n보다 큽니다.
    - 인덱스 1의 문자가 같은 문자열이 여럿 일 경우, 사전순으로 앞선 문자열이 앞쪽에 위치합니다.
'''

def solution(strings, n):
    # key: (n번째 문자, 전체 문자열) → 튜플로 정렬
    return sorted(strings, key=lambda x: (x[n], x))

'''
예시1)
from operator import itemgetter, attrgetter, methodcaller

def solution(strings, n):
    return sorted(sorted(strings), key=itemgetter(n))

예시2)
def solution(strings, n):
    # 1. n번째 문자를 기준으로 묶기
    temp = []
    for s in strings:
        temp.append((s[n], s))  # (n번째 문자, 전체 문자열) 튜플 생성

    # 2. n번째 문자 기준으로 정렬 (버블 정렬 사용 예시)
    for i in range(len(temp)):
        for j in range(i + 1, len(temp)):
            # 먼저 n번째 문자 비교
            if temp[i][0] > temp[j][0]:
                temp[i], temp[j] = temp[j], temp[i]
            # n번째 문자가 같으면 전체 문자열 사전순 비교
            elif temp[i][0] == temp[j][0] and temp[i][1] > temp[j][1]:
                temp[i], temp[j] = temp[j], temp[i]

    # 3. 정렬된 문자열만 추출
    result = [s[1] for s in temp]
    return result
'''