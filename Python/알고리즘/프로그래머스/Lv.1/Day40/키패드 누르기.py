'''
스마트폰 전화 키패드의 각 칸에 다음과 같이 숫자들이 적혀 있습니다.

이 전화 키패드에서 왼손과 오른손의 엄지손가락만을 이용해서 숫자만을 입력하려고 합니다.
맨 처음 왼손 엄지손가락은 * 키패드에 오른손 엄지손가락은 # 키패드 위치에서 시작하며, 엄지손가락을 사용하는 규칙은 다음과 같습니다.

엄지손가락은 상하좌우 4가지 방향으로만 이동할 수 있으며 키패드 이동 한 칸은 거리로 1에 해당합니다.
왼쪽 열의 3개의 숫자 1, 4, 7을 입력할 때는 왼손 엄지손가락을 사용합니다.
오른쪽 열의 3개의 숫자 3, 6, 9를 입력할 때는 오른손 엄지손가락을 사용합니다.
가운데 열의 4개의 숫자 2, 5, 8, 0을 입력할 때는 두 엄지손가락의 현재 키패드의 위치에서 더 가까운 엄지손가락을 사용합니다.
4-1. 만약 두 엄지손가락의 거리가 같다면, 오른손잡이는 오른손 엄지손가락, 왼손잡이는 왼손 엄지손가락을 사용합니다.
순서대로 누를 번호가 담긴 배열 numbers, 왼손잡이인지 오른손잡이인 지를 나타내는 문자열 hand가 매개변수로 주어질 때, 각 번호를 누른 엄지손가락이 왼손인 지 오른손인 지를 나타내는 연속된 문자열 형태로 return 하도록 solution 함수를 완성해주세요.

* 제한사항
    - numbers 배열의 크기는 1 이상 1,000 이하입니다.
    - numbers 배열 원소의 값은 0 이상 9 이하인 정수입니다.
    - hand는 "left" 또는 "right" 입니다.
        - "left"는 왼손잡이, "right"는 오른손잡이를 의미합니다.
    - 왼손 엄지손가락을 사용한 경우는 L, 오른손 엄지손가락을 사용한 경우는 R을 순서대로 이어붙여 문자열 형태로 return 해주세요.
'''

def solution(numbers, hand):
    """
    numbers: 누를 키 순서 (리스트)
    hand: "right" 또는 "left" → 선호 손
    반환: 누른 손을 문자열로 표현 (예: "LRLLLRLLR")
    """

    # 각 키패드 위치 (행, 열)
    keypad = {
        1:(0,0), 2:(0,1), 3:(0,2),
        4:(1,0), 5:(1,1), 6:(1,2),
        7:(2,0), 8:(2,1), 9:(2,2),
        '*':(3,0), 0:(3,1), '#':(3,2)
    }

    # 초기 왼손, 오른손 위치
    left_pos = keypad['*']
    right_pos = keypad['#']

    result = ''

    for n in numbers:
        if n in [1,4,7]:  # 왼손 고정
            result += 'L'
            left_pos = keypad[n]
        elif n in [3,6,9]:  # 오른손 고정
            result += 'R'
            right_pos = keypad[n]
        else:
            # 거리 계산 (맨해튼 거리)
            n_pos = keypad[n]
            left_dist = abs(n_pos[0]-left_pos[0]) + abs(n_pos[1]-left_pos[1])
            right_dist = abs(n_pos[0]-right_pos[0]) + abs(n_pos[1]-right_pos[1])

            if left_dist < right_dist:
                result += 'L'
                left_pos = n_pos
            elif left_dist > right_dist:
                result += 'R'
                right_pos = n_pos
            else:  # 거리가 같으면 선호 손
                if hand == 'right':
                    result += 'R'
                    right_pos = n_pos
                else:
                    result += 'L'
                    left_pos = n_pos

    return result


'''
예시1)
def solution(numbers, hand):
    """
    키패드 누르기 문제 해결 (거리 테이블 사용)
    
    numbers: 누를 키 순서 (리스트)
    hand: "right" 또는 "left" → 선호 손
    반환: 누른 손을 문자열로 표현 (예: "LRLLLRLLR")
    """

    # 왼손, 오른손 현재 위치 초기화
    # 10 = '*' 위치, 11 = '#' 위치
    left_pos = 10
    right_pos = 11

    answer = ""

    # 거리 테이블
    # p[a][b] = a에서 b까지 누를 때 거리
    p = [
        [0, 4, 3, 4, 3, 2, 3, 2, 1, 2],
        [4, 0, 1, 2, 0, 2, 3, 0, 3, 4],
        [3, 1, 0, 1, 2, 1, 2, 3, 2, 3],
        [4, 2, 1, 0, 3, 2, 1, 4, 3, 2],
        [3, 0, 2, 3, 0, 1, 2, 0, 2, 3],
        [2, 2, 1, 2, 1, 0, 1, 2, 1, 2],
        [3, 3, 2, 1, 2, 1, 0, 3, 2, 1],
        [2, 0, 3, 4, 0, 2, 3, 0, 1, 2],
        [1, 3, 2, 3, 2, 1, 2, 1, 0, 1],
        [2, 4, 3, 2, 3, 2, 1, 2, 1, 0],
        [1, 0, 4, 5, 0, 3, 4, 0, 2, 3],  # '*' 위치 (10)
        [1, 5, 4, 0, 4, 3, 0, 3, 2, 0]   # '#' 위치 (11)
    ]

    for num in numbers:
        if num in [1, 4, 7]:  # 왼손 고정
            left_pos = num
            answer += "L"
        elif num in [3, 6, 9]:  # 오른손 고정
            right_pos = num
            answer += "R"
        else:  # 가운데 열 (2, 5, 8, 0)
            left_dist = p[left_pos][num]
            right_dist = p[right_pos][num]

            if left_dist < right_dist:
                left_pos = num
                answer += "L"
            elif left_dist > right_dist:
                right_pos = num
                answer += "R"
            else:  # 거리가 같으면 선호 손
                if hand == "left":
                    left_pos = num
                    answer += "L"
                else:
                    right_pos = num
                    answer += "R"

    return answer

'''