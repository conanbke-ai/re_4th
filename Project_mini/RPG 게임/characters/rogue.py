'''
* 클래스 별 기본값(예시)

캐릭터          체력    공격력(ATK)     특수능력
전사(Warrior)   100     15          특수 공격 시 2배 공격력(단, 본인 체력 5 감소)
마법사(Mage)    80      18          마나 100, 특수 공격 시 1.5배 공격력(마나 20 소모)
도적(Rogue)     90      12          특수 공격(급습) 확률 70%(성공 시 3배 공격력)

- 실제 기본값은 생성자를 통해 초기화
- 위 기본값은 예시이며, 임의로 기호에 맞게 설정할 것


도적(Rogue) 클래스
    - Character 클래스 상속
    - 일정 확률(30%)로 공격을 회피
    - 특수 공격 : "급습" (ambush)
                랜덤 모듈을 이용해서 70% 확률로 3배 데미지를 입힘(랜덤 확률 시스템 활용)
                실패 시 공격하지 않음
'''
from .character import Character
from .affinity import get_effective_multiplier
import random

class Rogue(Character):
    """도적 클래스"""
    dodge_chance = 0.3  # 회피 확률
    attack_chance = 0.7 # 급습 확률

    def __init__(self, name="[적] 도적"):
        super().__init__(name=name, health=90, attack_power=12)
        
    def special_attack(self, target):
        """
        급습(ambush) 특수 공격
        - 70% 확률로 3배 데미지
        - 실패 시 공격하지 않음
        """
        
        if random.random() < self.attack_chance:
            damage = round(self.attack_power * 3 * get_effective_multiplier(self, target))
            target.take_damage(damage)
            self.logger.info(f"{self.name} 급습 성공! {damage} 데미지")
        else:
            self.logger.info(f"{self.name} 급습 실패! 공격하지 못함")

    
    def take_turn(self, target, is_player=True):
        """
        한 턴 동안 수행
        - 플레이어일 경우: 공격 선택지
        - 적(AI)일 경우: 랜덤 결정
        - 상대가 회피할 확률 적용
        """
        if is_player:
            choice = input("1) 기본 공격 2) 특수 공격: ").strip()
            if choice == "2":
                self.special_attack(target)
            else:
                if random.random() < self.dodge_chance:
                    self.logger.info(f"{target.name}이(가) 공격을 회피하였습니다!")
                else:
                    self.basic_attack(target)
        else:
            if random.random() < self.dodge_chance:
                self.special_attack(target)
            else:
                if random.random() < self.dodge_chance:
                    self.logger.info(f"{target.name}이(가) 공격을 회피하였습니다!")
                else:
                    self.basic_attack(target)
