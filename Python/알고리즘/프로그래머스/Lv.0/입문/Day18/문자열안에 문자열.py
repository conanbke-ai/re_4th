'''
문자열 str1, str2가 매개변수로 주어집니다. \
str1 안에 str2가 있다면 1을 없다면 2를 return하도록 solution 함수를 완성해주세요.

* 제한 사항
    - 1 ≤ str1의 길이 ≤ 100
    - 1 ≤ str2의 길이 ≤ 100
    - 문자열은 알파벳 대문자, 소문자, 숫자로 구성되어 있습니다.
'''

def solution(str1, str2):
    if str2 in str1:
        return 1
    else:
        return 2
    
'''
예시1)
def solution(str1, str2):
    return 1 if str2 in str1 else 2

예시2)
def solution(str1, str2):
    return 1 + int(str2 not in str1)

예시3)
def solution(str1, str2):
    if str1.count(str2):
        return 1
    else:
        return 2
'''