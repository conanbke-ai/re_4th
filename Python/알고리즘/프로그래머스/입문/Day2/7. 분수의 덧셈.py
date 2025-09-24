'''
첫번째 분수의 분자와 분모를 뜻하는 number1, denom1, 두번째 분수의 분자와 분모를 뜻하는 number2, denom2가 매개변수로 주어진다.
두 분수를 더한 값을 기약 분수로 나타냈을 때, 분자와 분모를 순서대로 담은 배열을 return하도록 완성하세요.

* 제한사항
- 0 < nunumber1,number2
- 0 < denom1, denom2
'''

import math


def solution(numer1, denom1, numer2, denom2):
    # list 초기화
    answer = []

    # 분자
    num = numer1*denom2 + numer2*denom1
    # 분모
    denom = denom1 * denom2

    # 최대공약수 구하기
    gcd = math.gcd(num, denom)

    # list에 할당
    answer.append(num // gcd)
    answer.append(denom // gcd)

    return answer


'''
예시1)
def solution(denum1, num1, denum2, num2):
    answer = []
    s = 0

    denum0 = (denum1*num2) +(denum2*num1)
    num0 = num1*num2

    for i in range(min(denum0,num0),0,-1):
        if denum0%i == 0 and num0%i == 0:
            s = i
            break

    denum0 /= s
    num0 /= s
    answer.append(denum0)
    answer.append(num0)

    return answer

- break 없을 시, s가 최대공약수가 아닌 최소공약수가 계산됨

예시2)
from fractions import Fraction

def solution(denum1, num1, denum2, num2):
    answer = Fraction(denum1, num1) + Fraction(denum2, num2)
    return [answer.numerator, answer.denominator]

- fractions 메소드 사용

예시3)
def solution(numer1, denom1, numer2, denom2):
    num = numer1 * denom2 + numer2 * denom1
    den = denom1 * denom2
    #약수구하기
    a_num = [i for i in range(1,num+1) if num%i == 0]
    a_den = [i for i in range(1,den+1) if den%i == 0]
    #최대공약수 구하기
    big_yaksu = [i for i in a_num if i in a_den][-1]
    answer = [num/big_yaksu, den/big_yaksu]


    return answer
'''
