'''
문자열 my_string과 문자 letter이 매개변수로 주어집니다. 
my_string에서 letter를 제거한 문자열을 return하도록 solution 함수를 완성해주세요.

* 제한 사항
    - 1 ≤ my_string의 길이 ≤ 100
    - letter은 길이가 1인 영문자입니다.
    - my_string과 letter은 알파벳 대소문자로 이루어져 있습니다.
    - 대문자와 소문자를 구분합니다.
'''


def solution(my_string, letter):
    answer = ""
    for i in my_string:
        for j in letter:
            if i != j:
                answer += i
    return answer


'''
예시1)
def solution(my_string, letter):
    return my_string.replace(letter, '')

예시2)
def solution(my_string, letter):
    return ''.join([c for c in my_string if c != letter])

예시3)
from re import sub
solution = lambda s,l : sub(l,"",s)
'''
