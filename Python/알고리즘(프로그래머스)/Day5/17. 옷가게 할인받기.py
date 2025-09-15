'''
머쓱이네 옷가게는 10만 원 이상 사면 5%, 30만 원 이상 사면 10%, 50만 원 이상 사면 20%를 할인해줍니다.
    구매한 옷의 가격 price가 주어질 때, 지불해야 할 금액을 return 하도록 solution 함수를 완성해보세요.


* 제한사항
    10 <= price <= 1000000
        price는 10원 단위(1의 자리 0)으로 주어집니다.
    소수점 이하를 버린 정수를 return 합니다.
'''

import math


def solution(price):

    # 10원 단위로 맞추기 (1의 자리 버리기)
    price = math.trunc(price/10) * 10

    # 할인율 조건
    if price >= 500000:
        price *= 0.80
    elif price >= 300000:
        price *= 0.90
    elif price >= 100000:
        price *= 0.95

    # 정수값으로 리턴
    return int(price)


'''
예시1)
def solution(price):
    discount_rates = {500000: 0.8, 300000: 0.9, 100000: 0.95, 0: 1}
    for discount_price, discount_rate in discount_rates.items():
        if price >= discount_price:
            return int(price * discount_rate)

예시2)
def solution(price):
    return (100 - len([1 for k in [100000, 300000, 500000, 500000] if k<=price])*5) * price // 100

'''
