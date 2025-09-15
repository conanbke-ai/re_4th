'''
정수 num1, num2가 매개변수로 주어집니다. 
num1을 num2로 나눈 나머지를 return 하도록 완성해주세요.

* 제한사항
- 0 < num1 <= 100
- 0 < num2 <= 100
'''


def solution(num1, num2):

    # 나머지 구하기
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

예시3)
solution = lambda num1, num2 : num1 % num2    

예시4)
def solution(num1, num2):
    answer = num1 % num2

    if (num1 > 0 and num1 <= 100) and (num2 > 0 and num2 <= 100):
        return answer

    else :
        answer = false

예시5)
import math
def kake(a, b):
    res = 0
    while (b > 0):
        if (b & 1):res = res + a
        a = a << 1
        b = b >> 1
    return res

def wari(w1, w2):
    ans = math.exp(math.log(abs(w1)) - math.log(abs(w2))) + 0.0000000001
    return math.trunc(ans)

def solution(num1, num2):
    return  num1 + ~(kake(num2, wari(num1, num2))) + 0x01

    - kake - 러시아 농부 곱셈 공부

'''
