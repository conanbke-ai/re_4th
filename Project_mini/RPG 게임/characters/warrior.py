'''
* 클래스 별 기본값(예시)

캐릭터          체력    공격력(ATK)     특수능력
전사(Warrior)   100     15          특수 공격 시 2배 공격력(단, 본인 체력 5 감소)
마법사(Mage)    80      18          마나 100, 특수 공격 시 1.5배 공격력(마나 20 소모)
도적(Rogue)     90      12          특수 공격(급습) 확률 70%(성공 시 3배 공격력)

- 실제 기본값은 생성자를 통해 초기화
- 위 기본값은 예시이며, 임의로 기호에 맞게 설정할 것

전사(Warrior) 클래스
    - Character 클래스 상속
    - 턴 종료 시, 2 체력 회복
    - 특수 공격 : "강력한 일격" (power_strike)
                2배의 공격력을 가하지만, 본인도 5의 체력을 잃음
'''
from .character import Character
from .affinity import get_effective_multiplier
from exceptions.errors import NotEnoughHealthError
from logs.logging_config import info_logger, error_logger
import random

class Warrior(Character):
    """전사 클래스"""
    min_health = 5

    def __init__(self, name="[적] 전사"):
        super().__init__(name=name, health=100, attack_power=15)

    def special_attack(self, target):
        """강력한 일격: 50% 확률 성공, 체력 5 소모"""
        if self.health <= self.min_health:
            raise NotEnoughHealthError(self.name, self.min_health)

        if random.random() < 0.5:
            damage = round(self.attack_power * 2 * get_effective_multiplier(self, target))
            target.take_damage(damage)
            self.health -= 5
            info_logger.info(f"{self.name} 강력한 일격!! {damage} 데미지, 체력 5 감소 → 남은 HP: {self.health}")
        else:
            info_logger.info(f"{self.name} 특수 공격 실패!")

    def take_turn(self, target, is_player=True):
        """전사 한 턴 수행"""
        if is_player:
            choice = input("1) 기본 공격 2) 특수 공격(체력 5 소모): ").strip()
            if choice == "1":
                self.basic_attack(target)
            elif choice == "2":
                try:
                    self.special_attack(target)
                except NotEnoughHealthError as e:
                        info_logger.info(f"[예외 발생] {e} → 기본 공격으로 대체")
                        self.basic_attack(target)
            else:
                info_logger.info("잘못된 입력, 기본 공격으로 처리")
                self.basic_attack(target)
        else:
            # 적(AI) 랜덤: 70% 기본, 30% 특수 공격
            if random.random() < 0.3:
                self.special_attack(target)
            else:
                self.basic_attack(target)

        # 턴 종료 후 체력 회복 2
        if self.health == self.max_health:
            info_logger.info(f"{self.name} 턴 종료 후 현재 HP: {self.health}")
        else:
            self.health = round(min(self.max_health, self.health + 2))
            info_logger.info(f"{self.name} 턴 종료 후 체력 2 회복 → 현재 HP: {self.health}")