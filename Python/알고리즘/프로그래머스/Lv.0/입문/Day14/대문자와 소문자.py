'''
문자열 my_string이 매개변수로 주어질 때, 대문자는 소문자로 소문자는 대문자로 변환한 문자열을 return하도록 solution 함수를 완성해주세요.

* 제한 사항
    - 1 ≤ my_string의 길이 ≤ 1,000
    - my_string은 영어 대문자와 소문자로만 구성되어 있습니다.
'''

def solution(my_string):
    
    result = ""
    
    for i in my_string:
        
        if i == i.upper():
            result += i.lower()
            
        elif i == i.lower():
            result += i.upper()
    
    return result

# print(solution("cccCCC"))

'''
예시1)
def solution(my_string):
    return my_string.swapcase()

'- swapcase() : 대소문자 변환 메서드'    

예시2)
def solution(my_string):
    answer = ''

    for i in my_string:
        if i.isupper():
            answer+=i.lower()
        else:
            answer+=i.upper()
    return answer
    
'- isupper()/islower()'

예시3)
def solution(my_string):
    return ''.join([x.lower() if x.isupper() else x.upper() for x in my_string])

'''