'''
* 클래스 별 기본값(예시)

캐릭터          체력    공격력(ATK)     특수능력
전사(Warrior)   100     15          특수 공격 시 2배 공격력(단, 본인 체력 5 감소)
마법사(Mage)    80      18          마나 100, 특수 공격 시 1.5배 공격력(마나 20 소모)
도적(Rogue)     90      12          특수 공격(급습) 확률 70%(성공 시 3배 공격력)

- 실제 기본값은 생성자를 통해 초기화
- 위 기본값은 예시이며, 임의로 기호에 맞게 설정할 것


마법사(Mage) 클래스
    - Character 클래스 상속
    - 추가 인스턴스 변수 : mana(마나, 기본값 100)
    - 공격대신 힐을 선택할 수 있음
    - 특수 공격 : "파이어볼" (fireball)
                마나 20을 소모하여 1.5배의 공격력으로 공격
                마나 부족 시 예외 발생(예외 처리 필요)
'''
from .character import Character
from .affinity import get_effective_multiplier
from exceptions.errors import NotEnoughManaError
from logs.logging_config import info_logger, error_logger
import random

class Mage(Character):
    """마법사 클래스"""
    min_mana = 20

    def __init__(self, name="[적] 마법사"):
        super().__init__(name=name, health=80, attack_power=18, mana=100)

    def special_attack(self, target):
        
        # 마나가 20미만일 시
        if self.mana < self.min_mana:
            # 정의한 error 발생
            raise NotEnoughManaError(self.name, self.min_mana)
        damage = round(self.attack_power * 1.5 * get_effective_multiplier(self, target))
        info_logger.info(f"{self.name}의 파이어볼! {damage} 데미지")
        target.take_damage(damage)
        self.mana -= 20
        info_logger.info(f"{self.name} 남은 마나: {self.mana}")
        
    def choose_skill(self, target, is_player=True):
        """마법사 스킬 선택"""
        import random
        if is_player:
            choice = ""
            while choice not in ["1", "2"]:
                choice = input(f"{self.name} 턴! 1) 공격 2) 힐(마나 20 소모): ")
            return "attack" if choice == "1" else "heal"
        else:
            # 적 AI: 체력 낮으면 50% 확률로 힐
            if self.health / self.max_health < 0.3 and self.mana >= 20 and random.random() < 0.5:
                return "heal"
            return "attack"

    def take_turn(self, target, is_player=True):
        """마법사 턴 수행"""
        # 플레이어인 경우
        if is_player:
        # 체력이 최대면 힐 선택지 제거
            if self.health >= self.max_health or self.mana < 20:
                self.basic_attack(target)
            else:
                choice = input("1) 기본 공격 2) 특수 공격(마나 20 소모) 3) 힐(마나 20 소모): ").strip()
                if choice == "2":
                    try:
                        self.special_attack(target)
                    except NotEnoughManaError as e:
                        info_logger.info(f"[예외 발생] {e} → 기본 공격으로 대체")
                        self.basic_attack(target)
                elif choice == "3":
                    if self.mana >= 20:
                        self.heal(20)
                        self.mana -= 20
                        info_logger.info(f"{self.name} 마나 사용 후 남은 마나: {self.mana}")
                    else:
                        logger.info("마나 부족! 기본 공격으로 전환")
                        self.basic_attack(target)
                else:
                    self.basic_attack(target)
        else:
            # AI
            if self.health / self.max_health < 0.3 and self.mana >= 20 and random.random() < 0.5:
                self.heal(20)
                self.mana -= 20
                info_logger.info(f"{self.name} 힐 사용 → 남은 마나: {self.mana}")
            else:
                if random.random() < 0.7:
                    self.basic_attack(target)
                else:
                    self.special_attack(target)