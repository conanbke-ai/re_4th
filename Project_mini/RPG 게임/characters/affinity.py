'''
각 캐릭터의 상성 관리
'''
# advantage: 강한 상대, weakness: 약한 상대

affinities = {
    "Warrior": {"advantage": "Rogue", "weakness": "Mage"},
    "Mage": {"advantage": "Warrior", "weakness": "Rogue"},
    "Rogue": {"advantage": "Mage", "weakness": "Warrior"}
}

def get_effective_multiplier(self, target):
    """상성에 따른 공격력 배율 계산"""
    # 클래스 이름으로 변환
    attacker_name = self.__class__.__name__
    target_name = target.__class__.__name__
    if affinities[attacker_name]["advantage"] == target_name:
        return 1.2  # 20% 증가
    elif affinities[attacker_name]["weakness"] == target_name:
        return 0.8  # 20% 감소
    return 1.0