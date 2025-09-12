'''
정수 num1, num2가 매개변수로 주어집니다. 
num1을 num2로 나눈 나머지를 return 하도록 완성해주세요.

* 제한사항
- 0 < num1 <= 100
- 0 < num2 <= 100
'''


def solution(num1, num2):
    answer = num1 % num2
    return answer


'''
예시1)
def solution(num1, num2):
    #return num1%num2
    while num1 >= num2:
        num1 -= num2
    return num1

예시2)
def solution(num1, num2):
    return divmod(num1, num2)[1]    
'''
