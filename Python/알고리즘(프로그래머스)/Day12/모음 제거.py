'''
영어에선 a, e, i, o, u 다섯 가지 알파벳을 모음으로 분류합니다. 
문자열 my_string이 매개변수로 주어질 때 모음을 제거한 문자열을 return하도록 solution 함수를 완성해주세요.

* 제한 사항
    - my_string은 소문자와 공백으로 이루어져 있습니다.
    - 1 ≤ my_string의 길이 ≤ 1,000
'''

def solution(my_string):
    
    vowel = ["a", "e", "i", "o", "u"]
    
    for v in vowel:
        for s in my_string:
            if s == v:
                my_string = my_string.replace(s, "")
            else:
                continue

    return my_string

'''
예시1)
def solution(my_string):
    return "".join([i for i in my_string if not(i in "aeiou")])


예시2)
def solution(my_string):
    vowels = ['a','e','i','o','u']
    for vowel in vowels:
        my_string = my_string.replace(vowel, '')
    return my_string

예시3)
import re
def solution(my_string):
    return re.sub('[aeiou]', '', my_string)

예시4)
import re
def solution(my_string):
    return re.sub(r"a|e|i|o|u", "", my_string)
'''