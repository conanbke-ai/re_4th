'''
* Character(추상 클래스)
1. 인스턴스 변수:
    • name : 캐릭터 이름
    • level : 캐릭터 레벨
    • health : 체력
    • attack_power : 공격력

2. 인스턴스 메서드:
    • attack(self, target) : 기본 공격(추상 메서드)
    • special_attack(self, target) : 특수 공격(추상 메서드)
    • take_damage(self, damage) : 피해를 입으면 체력이 감소
    • is_alive(self) : 체력이 0 이하이면 false 반환
    • show_status(self) : 캐릭터 정보를 출력
    • reset_health(self) : 캐릭터의 체력을 초기화
    • get_name(self) : 캐릭터의 이름을 가져옴
'''

import random
from abc import ABC, abstractmethod
from .affinity import get_effective_multiplier
from logs.logging_config import info_logger, error_logger

class Character(ABC):
    """모든 캐릭터의 공통 부모 클래스"""
    
    def __init__(self, name: str, health: int, attack_power: int, mana: int = 0):
        # 기본 속성 초기화
        self.name = name
        self.health = round(health)
        self.max_health = round(health)  # 최대 체력 기록
        self.attack_power = round(attack_power)
        self.mana = round(mana)
        self.max_mana = round(mana)  # 마법사 초기 마나 저장
        self.level = 1  # 초기 레벨
        self.status_effects = {}  # 상태 이상: {"독": 턴수, "기절": 턴수 등}
        self.items = []  # 장착 아이템 목록
        self.skills = ["basic_attack", "special_attack", "heal"] # 기본 스킬

    # ----------------------
    # 전투 관련 메서드
    # ----------------------
    
    def is_alive(self) -> bool:
        """캐릭터 생존 여부 확인"""
        return self.health > 0

    def basic_attack(self, target):
        """기본 공격: 대상에게 공격력만큼 피해를 입힘"""        
        # 각 캐릭터 상성에 따른 공격력 계산
        damage = round(self.attack_power * get_effective_multiplier(self, target))
        target.take_damage(damage)
        info_logger.info(f"{self.name} 기본 공격! {damage} 데미지")

    @abstractmethod
    def special_attack(self, target):
        """자식 클래스에서 구현할 특수 공격 메서드"""
        pass
    
    @abstractmethod
    def take_turn(self, target, is_player=True):
        """캐릭터 턴 수행"""
        pass

    def take_damage(self, damage: int):
        """피해를 입어 체력 감소, 0 이하로 떨어지지 않음"""
        self.health = max(0, self.health - damage)
        info_logger.info(f"{self.name} 체력 감소! 남은 체력: {self.health}")

    def show_status(self):
        """현재 체력과 마나 상태 출력"""
        status = f"{self.name} | LV: {self.level} | HP: {self.health}/{self.max_health}"
        if self.mana > 0:
            status += f" | Mana: {self.mana}"
        if self.status_effects:
            status += f" | Status: {self.status_effects}"
        info_logger.info(status)
        print("#" * 50)

    def reset_all(self):
        """체력, 마나, 상태 이상 모두 초기화 (레벨업 반영)"""
        self.health = self.max_health
        if hasattr(self, "max_mana"):
            self.mana = self.max_mana
        elif hasattr(self, "mana"):
            # 기존 마나 속성이 있을 경우
            self.mana = getattr(self, "mana")
        # 상태 이상 초기화
        self.status_effects.clear()
        info_logger.info(f"🔄 {self.name} 초기화 완료 → HP {self.health}, MANA {self.mana}")

    def get_name(self):
        """캐릭터 이름 반환"""
        return self.name

    def get_status_dict(self):
        """캐릭터 상태를 딕셔너리로 반환"""
        return {"name": self.name, "health": self.health, "attack": self.attack_power, "mana": getattr(self, "mana", 0)}

    def heal(self, amount):
        """체력 회복"""
        if self.health == self.max_health:
            info_logger.info(f"{self.name} 체력 회복! 이미 최대 체력입니다. 현재 HP: {self.health}")
        else:
            self.health = min(self.max_health, self.health + amount)
            info_logger.info(f"{self.name} 체력 회복! +{amount} HP → 현재 HP: {self.health}")

    
    # ----------------------
    # 아이템 관련 메서드
    # ----------------------
    
    def equip_item(self, item):
        """아이템 장착"""
        self.items.append(item)
        self.attack_power += item.atk_bonus
        self.max_health += item.hp_bonus
        self.health += item.hp_bonus
        info_logger.info(f"{self.name}이 {item.name} 장착! ATK+{item.atk_bonus}, HP+{item.hp_bonus}")
        
    # ----------------------
    # 성장 관련 메서드
    # ----------------------
    def level_up(self):
        """승리 시 레벨업"""
        self.level += 1
        self.max_health = round(self.max_health + (self.level - 1) * 10)  # 레벨마다 HP +10
        self.attack_power = round(self.attack_power + (self.level - 1) * 2) # 레벨마다 공격력 +2
        if self.mana > 0:
            self.mana = round(self.mana + (self.level - 1) * 5)       # 레벨마다 마나 +5
        # 레벨업 직후 체력 회복
        self.health = self.max_health
        if hasattr(self, "max_mana"):
            self.mana = self.max_mana
        info_logger.info(f"✨ {self.name} 레벨업! LV:{self.level}, HP:{self.health}, ATK:{self.attack_power}")

    # ----------------------
    # 턴 처리
    # ----------------------
        
    def take_turn(self, target):
        """
        캐릭터가 한 턴 동안 수행할 행동 결정 및 수행
        - 70% 확률로 기본 공격
        - 30% 확률로 특수 공격
        - 특수 공격 실패(예: 마나 부족) 시 자동으로 기본 공격으로 대체
        """
        # 상태 이상 처리
        self.apply_status()
        
        if "기절" in self.status_effects:
            return  # 기절 상태면 행동 불가
        
        # 확률 설정
        basic_attack_prob = 0.7  # 기본 공격 확률 70%
        roll = random.random()  # 0~1 사이 난수 생성
        print(f"[확률 확인] 난수: {roll:.2f}")

        # 공격 결정
        if roll < basic_attack_prob:
            # 70% 확률: 기본 공격
            info_logger.info(f"{self.name}이(가) 기본 공격을 선택했습니다.")
            self.basic_attack(target)
        else:
            # 30% 확률: 특수 공격
            info_logger.info(f"{self.name}이(가) 특수 공격을 선택했습니다.")
            try:
                self.special_attack(target)
            except ValueError as e:
                # 예외 발생 시 기본 공격으로 대체
                info_logger.info(f"[예외 발생] {e} → 기본 공격으로 대체")
                self.basic_attack(target)
    
    # ----------------------
    # 상태 이상 처리
    # ----------------------
    def apply_status(self):
        """턴 시작 시 상태 이상 처리"""
        remove_keys = []
        for effect, turns in self.status_effects.items():
            if effect == "독":
                self.take_damage(5)
                info_logger.info(f"{self.name}이 독 피해 5 받음!")
            elif effect == "기절":
                info_logger.info(f"{self.name}은 기절 상태로 행동 불가!")
            self.status_effects[effect] -= 1
            if self.status_effects[effect] <= 0:
                remove_keys.append(effect)
        for key in remove_keys:
            del self.status_effects[key]
    