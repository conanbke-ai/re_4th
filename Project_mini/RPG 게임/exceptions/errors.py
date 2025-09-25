class RPGException(Exception):
    """RPG 게임 전용 기본 예외"""
    pass

class NotEnoughManaError(RPGException):
    """마법 사용 시 마나 부족 예외"""
    def __init__(self, character_name, required_mana):
        self.character_name = character_name
        self.required_mana = required_mana
        super().__init__(f"{self.character_name}의 마나가 부족합니다! 필요한 마나: {self.required_mana}")
        
class NotEnoughHealthError(RPGException):
    """전사 스킬 사용 시 체력 부족 예외"""
    def __init__(self, character_name, required_health):
        self.character_name = character_name
        self.required_health = required_health
        super().__init__(f"{self.character_name}의 체력이 부족합니다! 필요한 체력: {self.required_health}")