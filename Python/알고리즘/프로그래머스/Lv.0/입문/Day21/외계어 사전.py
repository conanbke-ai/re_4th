'''
PROGRAMMERS-962 행성에 불시착한 우주비행사 머쓱이는 외계행성의 언어를 공부하려고 합니다. 
알파벳이 담긴 배열 spell과 외계어 사전 dic이 매개변수로 주어집니다. 
spell에 담긴 알파벳을 한번씩만 모두 사용한 단어가 dic에 존재한다면 1, 존재하지 않는다면 2를 return하도록 solution 함수를 완성해주세요.

* 제한 사항
    - spell과 dic의 원소는 알파벳 소문자로만 이루어져있습니다.
    - 2 ≤ spell의 크기 ≤ 10
    - spell의 원소의 길이는 1입니다.
    - 1 ≤ dic의 크기 ≤ 10
    - 1 ≤ dic의 원소의 길이 ≤ 10
    - spell의 원소를 모두 사용해 단어를 만들어야 합니다.
    - spell의 원소를 모두 사용해 만들 수 있는 단어는 dic에 두 개 이상 존재하지 않습니다.
    - dic과 spell 모두 중복된 원소를 갖지 않습니다.
'''

def solution(spell, dic):
    # spell 글자를 정렬 후 문자열로
    target = "".join(sorted(spell))
    
    for word in dic:
        if target == "".join(sorted(word)):
            return 1
    return 2

'''
예시1)
def solution(spell, dic):
    spell = set(spell)
    for s in dic:
        if (len(spell) == len(s)) and (not spell-set(s)):
            return 1
    return 2

예시2)
def solution(spell, dic):
    for d in dic:
        if sorted(d) == sorted(spell):
            return 1
    return 2

예시3)
def solution(spell, dic):
    spell = set(spell)
    return int(any(d for d in dic if not spell - set(d))) or 2
'''