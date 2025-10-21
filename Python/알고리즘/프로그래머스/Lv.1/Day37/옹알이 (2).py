'''
머쓱이는 태어난 지 11개월 된 조카를 돌보고 있습니다. 
조카는 아직 "aya", "ye", "woo", "ma" 네 가지 발음과 네 가지 발음을 조합해서 만들 수 있는 발음밖에 하지 못하고 연속해서 같은 발음을 하는 것을 어려워합니다. 
문자열 배열 babbling이 매개변수로 주어질 때, 머쓱이의 조카가 발음할 수 있는 단어의 개수를 return하도록 solution 함수를 완성해주세요.

* 제한사항
    - 1 ≤ babbling의 길이 ≤ 100
    - 1 ≤ babbling[i]의 길이 ≤ 30
    - 문자열은 알파벳 소문자로만 이루어져 있습니다.
'''
def solution(babbling):
    allowed = ["aya", "ye", "woo", "ma"]
    answer = 0

    for word in babbling:
        i = 0
        prev = ""   # 이전에 매칭한 음절 (연속 반복 금지 확인용)
        valid = True

        while i < len(word):
            matched = False
            # 각 음절이 현재 위치에서 시작하는지 확인
            for s in allowed:
                if word.startswith(s, i) and s != prev:
                    # 매칭되었고, 이전 음절과 같지 않으면 진행
                    prev = s
                    i += len(s)
                    matched = True
                    break
            if not matched:
                valid = False
                break

        if valid:
            answer += 1

    return answer

'''
예시1)
def solution(babbling):
    answer = 0
    for i in babbling:
        for j in ['aya','ye','woo','ma']:
            if j*2 not in i:
                i=i.replace(j,' ')
        if len(i.strip())==0:
            answer +=1
    return answer

예시2)
def solution(babbling):
    count = 0

    for b in babbling:
        if "ayaaya" in b or "yeye" in b or "woowoo" in b or "mama" in b:
            continue    
        if not b.replace("aya", " ").replace("ye", " ").replace("woo", " ").replace("ma", " ").replace(" ", ""):
            count += 1

    return count
'''