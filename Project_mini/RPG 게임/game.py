from battle.battle_manager import BattleManager
from utils.helpers import choose_character

def main():
    print("=" * 25)
    print("=== 턴제 RPG 게임 시작 ===")
    print("=" * 25)
    player = choose_character("플레이어 캐릭터 선택", is_player=True)
    while True:
        enemy = choose_character("적 캐릭터 선택", is_player=False)
        battle = BattleManager(player, enemy)
        win = battle.start_battle()
        if not win:
            print("\n💀 당신은 패배했습니다. 게임 오버...")
            break

        # 승리 시 계속 진행 여부
        cont = input("\n🎉 승리했습니다! \n계속해서 다음 적과 전투하시겠습니까? (y/n): ").strip().lower()
        if cont != "y":
            print("게임을 종료합니다. 👋")
            break

if __name__ == "__main__":
    main()
        
        


