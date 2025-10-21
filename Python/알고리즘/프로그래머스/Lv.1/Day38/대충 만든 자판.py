'''
휴대폰의 자판은 컴퓨터 키보드 자판과는 다르게 하나의 키에 여러 개의 문자가 할당될 수 있습니다. 
키 하나에 여러 문자가 할당된 경우, 동일한 키를 연속해서 빠르게 누르면 할당된 순서대로 문자가 바뀝니다.

예를 들어, 1번 키에 "A", "B", "C" 순서대로 문자가 할당되어 있다면 1번 키를 한 번 누르면 "A", 두 번 누르면 "B", 세 번 누르면 "C"가 되는 식입니다.

같은 규칙을 적용해 아무렇게나 만든 휴대폰 자판이 있습니다. 
이 휴대폰 자판은 키의 개수가 1개부터 최대 100개까지 있을 수 있으며, 특정 키를 눌렀을 때 입력되는 문자들도 무작위로 배열되어 있습니다. 
또, 같은 문자가 자판 전체에 여러 번 할당된 경우도 있고, 키 하나에 같은 문자가 여러 번 할당된 경우도 있습니다. 
심지어 아예 할당되지 않은 경우도 있습니다. 
따라서 몇몇 문자열은 작성할 수 없을 수도 있습니다.

이 휴대폰 자판을 이용해 특정 문자열을 작성할 때, 키를 최소 몇 번 눌러야 그 문자열을 작성할 수 있는지 알아보고자 합니다.

1번 키부터 차례대로 할당된 문자들이 순서대로 담긴 문자열배열 keymap과 입력하려는 문자열들이 담긴 문자열 배열 targets가 주어질 때, 각 문자열을 작성하기 위해 키를 최소 몇 번씩 눌러야 하는지 순서대로 배열에 담아 return 하는 solution 함수를 완성해 주세요.

단, 목표 문자열을 작성할 수 없을 때는 -1을 저장합니다.

* 제한사항
    - 1 ≤ keymap의 길이 ≤ 100
        - 1 ≤ keymap의 원소의 길이 ≤ 100
        - keymap[i]는 i + 1번 키를 눌렀을 때 순서대로 바뀌는 문자를 의미합니다.
            - 예를 들어 keymap[0] = "ABACD" 인 경우 1번 키를 한 번 누르면 A, 두 번 누르면 B, 세 번 누르면 A 가 됩니다.
        - keymap의 원소의 길이는 서로 다를 수 있습니다.
        - keymap의 원소는 알파벳 대문자로만 이루어져 있습니다.
    - 1 ≤ targets의 길이 ≤ 100
        - 1 ≤ targets의 원소의 길이 ≤ 100
        - targets의 원소는 알파벳 대문자로만 이루어져 있습니다.
'''
def solution(keymap, targets):
    # 1️⃣ 각 문자의 최소 입력 횟수를 저장할 딕셔너리
    key_dict = {}
    for keys in keymap:
        for i, ch in enumerate(keys, start=1):
            if ch not in key_dict:
                key_dict[ch] = i
            else:
                key_dict[ch] = min(key_dict[ch], i)

    # 2️⃣ 각 target 문자열별 총 누름 횟수 계산
    result = []
    for target in targets:
        total = 0
        for ch in target:
            if ch in key_dict:
                total += key_dict[ch]
            else:
                total = -1
                break
        result.append(total)

    return result

'''
예시1)
def solution(keymap, targets):
    answer = []
    hs = {}
    for k in keymap:
        for i, ch in enumerate(k):
            hs[ch] = min(i + 1, hs[ch]) if ch in hs else i + 1

    for i, t in enumerate(targets):
        ret = 0
        for ch in t:
            if ch not in hs:
                ret = - 1
                break
            ret += hs[ch]
        answer.append(ret)

    return answer

예시2)
def solution(keymap, targets):
    answer = []

    # A~Z까지 26개의 알파벳에 대해 “누르지 못하는 문자”를 나타내는 큰 수(101)로 초기화.
    alpha = [101 for i in range(26)]

    #keymap의 각 문자를 스캔하며 최솟값 저장
    for i in keymap:
        for idx, j in enumerate(i):
            # ord('A')를 빼서 알파벳 인덱스로 변환 (A→0, B→1, …)
            k = ord(j)-ord('A')
            alpha[k] = min(alpha[k],idx+1)

    # target 문자열별 총 누름 횟수 계산
    for i in targets:
        total = 0
        for j in i:
            cnt = alpha[ord(j) - ord('A')]
            if cnt ==101:
                answer.append(-1)
                break
            else:
                total+= cnt
        else:
            answer.append(total)

    return answer

예시3)
def solution(keymap, targets):
    alpha = [min((i.index(ch)+1 for i in keymap if ch in i), default=101) 
             for ch in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ']
    
    result = []
    for target in targets:
        total = 0
        for ch in target:
            cnt = alpha[ord(ch) - ord('A')]
            if cnt == 101:
                total = -1
                break
            total += cnt
        result.append(total)
    return result
'''