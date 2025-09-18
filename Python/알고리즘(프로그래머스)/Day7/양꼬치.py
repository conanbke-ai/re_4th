'''
머쓱이네 양꼬치 가게는 10인분을 먹으면 음료수 하나를 서비스로 줍니다.
 양꼬치는 1인분에 12,000원, 음료수는 2,000원입니다. 
 정수 n과 k가 매개변수로 주어졌을 때, 양꼬치 n인분과 음료수 k개를 먹었다면 총얼마를 지불해야 하는지 return 하도록 solution 함수를 완성해보세요.

 * 제한 사항
    - 0 < n < 1,000
    - n / 10 ≤ k < 1,000
    - 서비스로 받은 음료수는 모두 마십니다.
'''


def solution(n, k):

    # 양꼬치를 10인분 이상 먹었을 때
    if n >= 10:
        # 10인분당 음료수 1개 서비스 계산
        k = k - (n // 10)

    total_price = 12000 * n + 2000 * k

    return total_price


'''
예시1)
def solution(n, k):
    return 12000 * n + 2000 * (k - n // 10)

예시2)
def solution(n, k):
    service = n//10
    drink = max(0, k-service)
    return (12000*n)+(2000*drink)
'''
