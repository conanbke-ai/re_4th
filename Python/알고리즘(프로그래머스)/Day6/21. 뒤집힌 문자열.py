'''
문자열 my_string이 매개변수로 주어집니다. 
my_string을 거꾸로 뒤집은 문자열을 return하도록 solution 함수를 완성해주세요.

* 제한 사항
    1 ≤ my_string의 길이 ≤ 1,000
'''


def solution(my_string):
    return my_string[::-1]


'''
예시1)
def solution(my_string):
    answer = ''
    for c in my_string:
        answer= c+answer
    return answer

예시2)
def solution(my_string):
    return ''.join(list(reversed(my_string)))

- list 빼도 가능
'''
