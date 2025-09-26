'''
* 전투 관리 시스템(BattleManager)
    - 인스턴스 메서드 : start_battle 구현
    - 전투 흐름
        - 랜덤 모듈을 이용하여 전투의 선공(첫 번째 공격자)를 랜덤으로 결정한다.
        - 첫 번째 캐릭터가 공격
        - 두 번째 캐릭터가 살아있으면 반격
        - 한 캐릭터의 체력이 0이 되면 전투 종료
        - 타임 모듈을 이용해서, 전투 진행 시 딜레이를 추가하여 더 자연스러운 전투를 연출한다.
    - 기본 공격 vs 특수 공격 선택
        - 랜덤 모듈을 통해 70% 확률로 기본 공격, 30% 확률로 특수 공격(예외 발생 가능)
    - 예외 처리
        - 마나 부족 시 공격 불가
'''
from logs.logging_config import info_logger, error_logger
from characters import Warrior, Mage, Rogue
from utils.helpers import *
import random
import time
import os

class BattleManager:
    """턴제 전투를 관리하는 클래스"""

    def __init__(self, player: Warrior | Mage | Rogue, enemy: Warrior | Mage | Rogue):
        self.player = player
        self.enemy = enemy

    def start_battle(self):
        """전투 시작"""
        
        # 체력, 마나, 상태 이상 초기화
        self.player.reset_all()
        self.enemy.reset_all()
        
        info_logger.info(f"=== 전투 시작: 플레이어 - {self.player.name} VS 적 - {self.enemy.name} ===")
        # 선공 결정: True면 플레이어 먼저, False면 적 먼저
        player_first = random.choice([True, False])
        info_logger.info(f"{'※ 플레이어' if player_first else '※ 적'}이(가) 먼저 공격합니다!")
        time.sleep(1)

        while self.player.is_alive() and self.enemy.is_alive():
            if player_first:
                self.player_turn()
                if self.enemy.is_alive():
                    self.enemy_turn()
            else:
                self.enemy_turn()
                if self.player.is_alive():
                    self.player_turn()
            time.sleep(1)  # 턴 사이 딜레이

        # 전투 결과
        if self.player.is_alive():
            info_logger.info(f"🎉 플레이어 - {self.player.name} 승리! 🎉")
            # 레벨업 반영
            self.player.level_up()
            # 랜덤 이벤트 발생
            self.random_event()
            # 다음 라운드 준비
            self.prepare_next_round()
            return True
        else:
            info_logger.info(f"💀 플레이어 {self.player.name} 패배...💀")
            return False

    # ----------------------
    # 플레이어/적 턴 수행
    # ----------------------
    def player_turn(self):
        info_logger.info(f"--- 플레이어 - {self.player.name}의 턴 ---")
        # 마법사는 입력 선택 가능
        if isinstance(self.player, Mage):
            self.player.take_turn(self.enemy, is_player=True)
        else:
            self.player.take_turn(self.enemy)
        self.enemy.show_status()
        time.sleep(0.5)

    def enemy_turn(self):
        info_logger.info(f"--- 적 - {self.enemy.name}의 턴 ---")
        # 적은 AI 수행
        self.enemy.take_turn(self.player, is_player=False)
        self.player.show_status()
        time.sleep(0.5)
        
    # ----------------------
    # 랜덤 이벤트
    # ----------------------
    def random_event(self):
        """승리 후 랜덤 이벤트 발생"""
        event_roll = random.random()
        if event_roll < 0.3:
            # 체력 증가 포션 획득
            potion = 15
            self.player.max_health += potion
            info_logger.info(f"🎁 랜덤 이벤트: 체력 회복 포션 획득! 최대 HP +{potion}")
        elif event_roll < 0.5:
            # 공격력 버프
            buff = 5
            self.player.attack_power += buff
            info_logger.info(f"🎁 랜덤 이벤트: 공격력 버프! ATK +{buff}")
        elif event_roll < 0.7:
            # 상태 이상 회복
            if self.player.status_effects:
                self.player.status_effects.clear()
                info_logger.info(f"🎁 랜덤 이벤트: 상태 이상 회복!")
        
        elif event_roll < 0.9:
            # 직업별 랜덤 아이템
            item = get_random_item(self.player.__class__.__name__)
            item.apply_to(self.player)
        
        else:
            info_logger.info("🎁 랜덤 이벤트 없음...")
            
    # ----------------------
    # 다음 라운드 초기화
    # ----------------------
    def prepare_next_round(self):
        """라운드 시작 전 캐릭터 초기화"""
        self.player.reset_all()
        self.enemy.reset_all()
        info_logger.info("--- 다음 라운드를 위해 체력/마나/상태 초기화 완료 ---")
            
    