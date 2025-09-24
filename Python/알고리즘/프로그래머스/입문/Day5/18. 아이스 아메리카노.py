'''
머쓱이는 추운 날에도 아이스 아메리카노만 마십니다. 
    아이스 아메리카노는 한잔에 5,500원입니다. 
    머쓱이가 가지고 있는 돈 money가 매개변수로 주어질 때, 
    머쓱이가 최대로 마실 수 있는 아메리카노의 잔 수와 남는 돈을 순서대로 담은 배열을 return 하도록 solution 함수를 완성해보세요.

* 제한사항
    0 <= money <= 1000000

'''


def solution(money):

    answer = [money // 5500, money % 5500]
    return answer


'''
예시1)
def solution(money):
    return divmod(money, 5500)

예시2)
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

def solution(money):
    return [wari(money, 5500), money + ~(kake(5500, wari(money, 5500))) + 0x1]
'''
