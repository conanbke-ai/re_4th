'''
문자열 my_string이 매개변수로 주어집니다. 
my_string안의 모든 자연수들의 합을 return하도록 solution 함수를 완성해주세요.

* 제한 사항
    - 1 ≤ my_string의 길이 ≤ 1,000
    - my_string은 소문자, 대문자 그리고 한자리 자연수로만 구성되어있습니다.
'''

def solution(my_string):
    
    nums = 0
    
    for s in my_string:
        if s in "0123456789":
            nums += int(s)
            
    return nums

'''
예시1)
def solution(my_string):
    return sum(int(i) for i in my_string if i.isdigit())

예시2)
def solution(my_string):
    answer = 0
    for i in my_string:
        try:
            answer = answer + int(i)
        except:
            pass

    return answer

예시3)
import re
def solution(my_string):
    return sum(int(n) for n in re.sub('[^1-9]', '', my_string))

예시4)
def solution(my_string):
    answer = 0
    for c in my_string:
        if c.isnumeric():
            answer += int(c)
    return answer

예시5)
def solution(my_string):

    answer = 0

    for i in my_string :
        if not i.isalpha() :
            answer += int(i)

    return answer

예시6)
def solution(my_string):
    return sum(map(int, filter(lambda x: x.isdigit(), my_string)))
'''