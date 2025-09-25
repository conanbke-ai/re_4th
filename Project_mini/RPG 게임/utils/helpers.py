from characters import Warrior, Mage, Rogue
from items.item import Item
import random
from wcwidth import wcswidth

    # ----------------------
    # 직업 선택
    # ----------------------

def choose_character(prompt: str, is_player: bool = True):
    """
    플레이어 또는 적 캐릭터를 선택
    - prompt: 출력 메시지
    - is_player: True면 이름 입력 가능, False면 기본 이름 사용
    """
    char_map = {"1": Warrior, "2": Mage, "3": Rogue}
    default_names = {"1": "전사", "2": "마법사", "3": "도적"}

    while True:
        
        sels = [
            f"1) 전사 (Warrior)",
            f"2) 마법사 (Mage)",
            f"3) 도적 (Rogue)"
        ]
        
        box_width = max(len(sel) for sel in sels) + 6
        
        print(f"\n[ {prompt} ]")
        print("#" * box_width)
        for sel in sels:
            # 좌우 정렬
            padding = box_width - wcswidth(sel) - 3  # 오른쪽 공백 계산
            print(f"# {sel}{' ' * padding}#")
        print("#" * box_width)
        print("")
        choice = input("선택 (1/2/3): ").strip()
        if choice in char_map:
            cls = char_map[choice]
            if is_player:
                name = input(f"플레이어 닉네임 입력 (엔터 시 기본값 '{default_names[choice]}'): ").strip()
                name = name or default_names[choice]
                return cls(name=(f'[플레이어] {default_names[choice]} {name}'))
            else:
                # 적은 이름 입력 없이 기본값 사용
                return cls()
        else:
            print("잘못된 선택입니다. 1, 2, 3 중에서 입력해주세요.")

    # ----------------------
    # 아이템 관련 메서드
    # ----------------------
         
ITEM_POOL = [
    # 전사용
    Item("강철검", attack_bonus=5, valid_classes=["Warrior"]),
    Item("방패", health_bonus=15, valid_classes=["Warrior"]),
    
    # 마법사용
    Item("마법 지팡이", attack_bonus=4, valid_classes=["Mage"]),
    Item("마나 반지", health_bonus=10, valid_classes=["Mage"]),
    
    # 도적용
    Item("단검", attack_bonus=3, valid_classes=["Rogue"]),
    Item("민첩 부츠", health_bonus=5, valid_classes=["Rogue"]),
    
    # 모든 직업 공용
    Item("힘의 목걸이", attack_bonus=2, health_bonus=5, valid_classes=["Warrior", "Mage", "Rogue"]),
]

def get_random_item(character_class=None):
    """
    캐릭터 클래스에 맞는 랜덤 아이템 반환
    character_class: 캐릭터 클래스 이름(str)
    """
    if character_class:
        valid_items = [item for item in ITEM_POOL if character_class in item.valid_classes]
    else:
        valid_items = ITEM_POOL
    return random.choice(valid_items)
