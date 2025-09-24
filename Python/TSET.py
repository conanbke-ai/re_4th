######################################################################################################
# 실습 6 타자 연습 게임 만들기

'''
1. 영단어 리스트 중 무작위로 단어가 제시됩니다.
2. 사용자는 해당 단어를 정확히 입력해야 다음 문제로 넘어갈 수 있습니다.
3. 10문제를 모두 맞히면, 게임이 종료되고 총 소요 시간이 출력됩니다.
4. 틀린 경우에는 "오타! 다시 도전!" 메시지를 출력하고, 같은 문제를 다시 도전하게 합니다.
5. 게임이 시작되기 전, 엔터키를 누르면 시작합니다.

* 요구 사항
    - 단어는 미리 주어진 리스트에서 random.choice()로 무작위 선택
    - input()으로 사용자 입력
    - time.time()으로 시작~종료 시간 측정, 소요 시간 계산
    - 문제마다 번호가 함께 출력
    - 통과/오타 메시지, 총 타자 시간까지 출력
'''
import time
import random

words = [
    "apple", "banana", "cherry", "grape", "orange",
    "peach", "pear", "plum", "melon", "lemon",
    "car", "bus", "train", "plane", "ship",
    "dog", "cat", "horse", "tiger", "lion"
]

ent = input("[타자 게임] 준비되면 엔터!")

# 엔터값 들어왔을 때 게임 시작
if ent == "":

    # 시작 시간 측정
    start_time = time.time()

    # 10문제 반복
    for i in range(1, 11):

        print(f'문제 {i}')
        # 문제 (리스트 랜덤 배열)
        q = random.choice(words)
        usr = input("")

        while True:
            # 정답을 맞출 때까지 반복
            if usr != q:
                usr = input("오타! 다시 도전! \n: ")
            else:
                print(q)
                print(usr)
                print("통과!!")
                break

    # 종료 시간 측정
    end_time = time.time()

    print(f'타자 시간 : {end_time - start_time}초')

print("[타자 게임] 종료")
