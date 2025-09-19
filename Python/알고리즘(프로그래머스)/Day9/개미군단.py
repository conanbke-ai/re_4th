'''
개미 군단이 사냥을 나가려고 합니다. 
개미군단은 사냥감의 체력에 딱 맞는 병력을 데리고 나가려고 합니다. 
장군개미는 5의 공격력을, 병정개미는 3의 공격력을 일개미는 1의 공격력을 가지고 있습니다. 
예를 들어 체력 23의 여치를 사냥하려고 할 때, 일개미 23마리를 데리고 가도 되지만, 장군개미 네 마리와 병정개미 한 마리를 데리고 간다면 더 적은 병력으로 사냥할 수 있습니다. 
사냥감의 체력 hp가 매개변수로 주어질 때, 사냥감의 체력에 딱 맞게 최소한의 병력을 구성하려면 몇 마리의 개미가 필요한지를 return하도록 solution 함수를 완성해주세요.

* 제한 사항
    - hp는 자연수입니다.
    - 0 ≤ hp ≤ 1000
'''

# 장군, 병정, 일꾼 개미 공격력
general, soldier, worker = 5, 3, 1


def solution(hp):
    # 총 병력 선언
    result = 0

    if 0 <= hp <= 1000:
        # 장군개미 필요한 경우
        if hp // general > 0:
            # 장군개미 개수 추가 할당
            result += hp // 5
            # 소모된 hp 계산
            hp = hp % 5
            # 병정개미 필요한 경우
            if hp // soldier > 0:
                # 병정개미 개수 추가 할당
                result += hp // 3
                # 소모된 hp 계산
                hp = hp % 3
                # 일꾼개미 필요한 경우
                if hp // worker > 0:
                    # 일꾼개미 개수 추가 할당
                    result += hp // 1
        else:
            # 병정개미 필요한 경우
            if hp // soldier > 0:
                # 병정개미 개수 추가 할당
                result += hp // 3
                # 소모된 hp 계산
                hp = hp % 3
            # 일꾼개미 필요한 경우
                if hp // worker > 0:
                    # 일꾼개미 개수 추가 할당
                    result += hp // 1
            else:
                # 일꾼개미 필요한 경우
                if hp // worker > 0:
                    # 일꾼개미 개수 추가 할당
                    result += hp // 1
    else:
        return 0

    # 총 병력 반환
    return result


'''
예시1)
def solution(hp):    
    return hp // 5 + (hp % 5 // 3) + ((hp % 5) % 3)

예시2)
def solution(hp):
    answer = 0
    for ant in [5, 3, 1]:
        d, hp = divmod(hp, ant)
        answer += d
    return answer
'''
