# index 파일

class TextGame:

    def __init__(self):
        
        player(input("플레이어의 이름을 입력해주세요. \n : "))
        
    def player(self, name):
        self.name = name    # 플레이어 이름
        self.health = 100   # 플레이어 체력
        self.inventory = [] # 플레이어 소지품
        
        print(f'{self.name}님, 일주일간 던전 생존기에 오신 걸 환영합니다!')
        print(f'초기 체력 : {self.health}')
        print("")