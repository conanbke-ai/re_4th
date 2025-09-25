from logs.logging_config import info_logger, error_logger

class RPGException(Exception):
    """RPG 게임 전용 기본 예외"""
    def __init__(self, message: str):
        self.message = message
        super().__init__(message)
        # 예외 발생 시 자동으로 에러 로그에 기록
        error_logger.error(message, exc_info=True)  # 트레이스백까지 기록

class NotEnoughManaError(RPGException):
    """마법 사용 시 마나 부족 예외"""
    def __init__(self, character_name, required_mana):
        self.character_name = character_name
        self.required_mana = required_mana
        message = f"⚠️ {self.character_name}의 마나가 부족합니다! 필요한 마나: {self.required_mana}"
        super().__init__(message)
        # INFO 레벨로 기록
        info_logger.info(message)
        
class NotEnoughHealthError(RPGException):
    """전사 스킬 사용 시 체력 부족 예외"""
    def __init__(self, character_name, required_health):
        self.character_name = character_name
        self.required_health = required_health
        message = f"⚠️ {self.character_name}의 체력이 부족합니다! 필요한 체력: {self.required_health}"
        super().__init__(message)
        # INFO 레벨로 기록
        info_logger.info(message)
