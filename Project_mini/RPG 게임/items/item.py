'''
랜덤으로 item을 drop하여 캐릭터 버프받을 수 있다.

각 직업 별 유효한 item이 있다.
'''
from logs.logging_config import info_logger, error_logger

class Item:
    """아이템 클래스"""
    
    def __init__(self, name, attack_bonus=0, health_bonus=0, valid_classes=None):
        """
        valid_classes: ['Warrior', 'Mage', 'Rogue'] 처럼 장착 가능한 직업 리스트
        """
        self.name = name
        self.attack_bonus = attack_bonus
        self.health_bonus = health_bonus
        self.valid_classes = valid_classes or ["Warrior", "Mage", "Rogue"]

    def apply_to(self, character):
        """캐릭터가 장착 가능한 아이템인지 확인 후 적용"""
        if character.__class__.__name__ in self.valid_classes:
            character.attack_power += self.attack_bonus
            character.max_health += self.health_bonus
            character.health += self.health_bonus
            info_logger.info(f"{character.name}이(가) {self.name} 장착! ATK+{self.attack_bonus}, HP+{self.health_bonus}")
        else:
            info_logger.info(f"{self.name}은(는) {character.__class__.__name__}이(가) 사용할 수 없습니다.")