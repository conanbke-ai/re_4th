'''
문자열 my_string이 매개변수로 주어집니다. 
my_string은 소문자, 대문자, 자연수로만 구성되어있습니다. 
my_string안의 자연수들의 합을 return하도록 solution 함수를 완성해주세요.

* 제한사항
    - 1 ≤ my_string의 길이 ≤ 1,000
    - 1 ≤ my_string 안의 자연수 ≤ 1000
    - 연속된 수는 하나의 숫자로 간주합니다.
    - 000123과 같이 0이 선행하는 경우는 없습니다.
    - 문자열에 자연수가 없는 경우 0을 return 해주세요.
'''

def solution(my_string):
    total = 0
    num = ""

    for ch in my_string:
        if ch.isdigit():      # 숫자면 문자열에 누적
            num += ch
        else:                 # 숫자가 끊기면 합산
            if num:
                total += int(num)
                num = ""
    # 마지막 숫자 처리
    if num:
        total += int(num)

    return total

'''
예시1)
import re

def solution(my_string):
    # \d+ : 숫자가 1개 이상 연속된 문자열 추출
    numbers = re.findall(r"\d+", my_string)
    return sum(map(int, numbers))

'- \d : 숫자 하나'
'- \d+ : 숫자 하나 이상 연속'
'- 알파벳만 찾기 : re.findall(r"[a-zA-Z]+", s)'
'- 특징 & 조건
s = "2025-09-29"
print(re.findall(r"(\d{4})-(\d{2})-(\d{2})", s))'

예시2)
def solution(my_string):
    s = ''.join(i if i.isdigit() else ' ' for i in my_string)
    return sum(int(i) for i in s.split())

예시3)
import re

def solution(my_string):
    return sum([int(i) for i in re.findall(r'[0-9]+', my_string)])
'''