'''
프로그래머스 치킨은 치킨을 시켜먹으면 한 마리당 쿠폰을 한 장 발급합니다. 
쿠폰을 열 장 모으면 치킨을 한 마리 서비스로 받을 수 있고, 서비스 치킨에도 쿠폰이 발급됩니다. 
시켜먹은 치킨의 수 chicken이 매개변수로 주어질 때 받을 수 있는 최대 서비스 치킨의 수를 return하도록 solution 함수를 완성해주세요.

* 제한 사항
    - chicken은 정수입니다.
    - 0 ≤ chicken ≤ 1,000,000
'''

def solution(chicken):
    total_chicken = chicken
    free_chicken = 0
    coupon = chicken // 10  # 초기 쿠폰

    while coupon > 0:
        free_chicken += coupon
        coupon = coupon // 10 + coupon % 10  # 새 쿠폰 + 남은 쿠폰

    return free_chicken

'''
예시1)
def solution(chicken):
    if chicken < 10:  # 쿠폰이 10장 미만이면 서비스 치킨 없음
        return 0
    free = chicken // 10
    return free + solution(free + chicken % 10)

'- 재귀함수 식'

예시2)
def solution(chicken):
    return int(chicken*0.11111111111)

'- 10% 의 10% 의... 이므로'

예시3)
def solution(chicken):
    answer = (max(chicken,1)-1)//9
    return answer

'- 서비스 치킨을 제외하고 실제 9마리의 치킨. 9마리인 경우 서비스를 받지 못하므로 -1 해줌'

예시4)
def solution(chicken):
    answer = 0
    while chicken >= 10:
        chicken, mod = divmod(chicken, 10)
        answer += chicken
        chicken += mod
    return answer
'''