'''
게임개발자인 "죠르디"는 크레인 인형뽑기 기계를 모바일 게임으로 만들려고 합니다.
"죠르디"는 게임의 재미를 높이기 위해 화면 구성과 규칙을 다음과 같이 게임 로직에 반영하려고 합니다.

게임 화면은 "1 x 1" 크기의 칸들로 이루어진 "N x N" 크기의 정사각 격자이며 위쪽에는 크레인이 있고 오른쪽에는 바구니가 있습니다. (위 그림은 "5 x 5" 크기의 예시입니다). 각 격자 칸에는 다양한 인형이 들어 있으며 인형이 없는 칸은 빈칸입니다. 모든 인형은 "1 x 1" 크기의 격자 한 칸을 차지하며 격자의 가장 아래 칸부터 차곡차곡 쌓여 있습니다. 게임 사용자는 크레인을 좌우로 움직여서 멈춘 위치에서 가장 위에 있는 인형을 집어 올릴 수 있습니다. 집어 올린 인형은 바구니에 쌓이게 되는 데, 이때 바구니의 가장 아래 칸부터 인형이 순서대로 쌓이게 됩니다. 다음 그림은 [1번, 5번, 3번] 위치에서 순서대로 인형을 집어 올려 바구니에 담은 모습입니다.

만약 같은 모양의 인형 두 개가 바구니에 연속해서 쌓이게 되면 두 인형은 터뜨려지면서 바구니에서 사라지게 됩니다. 위 상태에서 이어서 [5번] 위치에서 인형을 집어 바구니에 쌓으면 같은 모양 인형 두 개가 없어집니다.

크레인 작동 시 인형이 집어지지 않는 경우는 없으나 만약 인형이 없는 곳에서 크레인을 작동시키는 경우에는 아무런 일도 일어나지 않습니다. 또한 바구니는 모든 인형이 들어갈 수 있을 만큼 충분히 크다고 가정합니다. (그림에서는 화면표시 제약으로 5칸만으로 표현하였음)

게임 화면의 격자의 상태가 담긴 2차원 배열 board와 인형을 집기 위해 크레인을 작동시킨 위치가 담긴 배열 moves가 매개변수로 주어질 때, 크레인을 모두 작동시킨 후 터트려져 사라진 인형의 개수를 return 하도록 solution 함수를 완성해주세요.

* 제한사항
    - board 배열은 2차원 배열로 크기는 "5 x 5" 이상 "30 x 30" 이하입니다.
    - board의 각 칸에는 0 이상 100 이하인 정수가 담겨있습니다.
        - 0은 빈 칸을 나타냅니다.
        - 1 ~ 100의 각 숫자는 각기 다른 인형의 모양을 의미하며 같은 숫자는 같은 모양의 인형을 나타냅니다.
    - moves 배열의 크기는 1 이상 1,000 이하입니다.
    - moves 배열 각 원소들의 값은 1 이상이며 board 배열의 가로 크기 이하인 자연수입니다.
'''
def solution(board, moves):
    stack = []
    cnt = 0

    for m in moves:
        for i in range(len(board)):
            if board[i][m-1] != 0:
                doll = board[i][m-1]  # 뽑은 인형
                board[i][m-1] = 0     # 보드에서 제거

                if stack and stack[-1] == doll:  # 연속 인형 제거
                    stack.pop()
                    cnt += 2
                else:
                    stack.append(doll)
                break  # 한 번만 뽑기
    return cnt

'''
예시1) deque 버전
from collections import deque

def solution(board, moves):
    """
    크레인 인형뽑기 게임을 시뮬레이션하여, 
    연속으로 같은 인형이 쌓이면 제거된 인형의 총 개수를 반환합니다.

    Parameters:
    - board (list of list of int): 게임판 (2차원 리스트), 0은 빈 칸
    - moves (list of int): 크레인이 뽑을 열 순서 (1-indexed)

    Returns:
    - int: 제거된 인형의 총 개수
    """

    # 1️⃣ 각 열을 deque로 변환하고 0 제거
    # zip(*board) → board를 전치하여 열 단위로 변환
    # filter(lambda y: y > 0, col) → 0 제거
    # deque(...) → 앞에서 O(1)로 뽑기 가능
    cols = [deque(filter(lambda y: y > 0, col)) for col in zip(*board)]

    removed_count = 0  # 제거된 인형 수
    stack = [0]        # 뽑은 인형을 쌓을 스택, 초기값 0으로 오류 방지

    # 2️⃣ moves 순서대로 인형 뽑기
    for move in moves:
        col_index = move - 1  # 1-indexed → 0-indexed 변환

        # 해당 열에 인형이 남아 있는 경우
        if cols[col_index]:
            doll = cols[col_index].popleft()  # 열에서 맨 위 인형 뽑기
            last = stack.pop()                 # 스택에서 마지막 인형 꺼내기

            # 3️⃣ 연속 인형 제거
            if doll == last:
                removed_count += 2  # 같은 인형이 쌓이면 2개 제거
            else:
                # 스택에 다시 쌓기
                stack.extend([last, doll])

    return removed_count

예시2) stack 버전
def solution(board, moves):
    """
    크레인 인형뽑기 게임 시뮬레이션

    Parameters:
    - board (list of list of int): 게임판 (2차원 리스트), 0은 빈 칸
    - moves (list of int): 크레인이 뽑을 열 순서 (1-indexed)

    Returns:
    - int: 제거된 인형의 총 개수
    """

    stack = []        # 뽑은 인형을 쌓는 스택
    removed_count = 0 # 제거된 인형 수

    # moves 순서대로 인형 뽑기
    for move in moves:
        col_index = move - 1  # 1-indexed → 0-indexed
        doll = 0              # 뽑은 인형 초기화

        # 해당 열에서 위에서부터 인형 찾기
        for row in range(len(board)):
            if board[row][col_index] != 0:
                doll = board[row][col_index]  # 인형 뽑기
                board[row][col_index] = 0     # 보드에서 제거
                break  # 한 열에서 한 번만 뽑기

        # 인형을 뽑았는지 확인
        if doll == 0:
            continue  # 인형이 없으면 다음 move로

        # 스택이 비어있으면 그냥 쌓기
        if not stack:
            stack.append(doll)
        # 스택 맨 위와 같은 인형이면 제거
        elif stack[-1] == doll:
            stack.pop()
            removed_count += 2
        # 아니면 스택에 쌓기
        else:
            stack.append(doll)

    return removed_count

예시3) walrus 버전(:= 은 값을 변수에 저장하면서 동시에 표현식에서 사용할 수 있는 연산자)
from collections import deque

def solution(board, moves):
    """
    크레인 인형뽑기 게임 시뮬레이션 (Walrus 연산자 버전)

    Parameters:
    - board (list of list of int): 게임판 (2차원 리스트), 0은 빈 칸
    - moves (list of int): 크레인이 뽑을 열 순서 (1-indexed)

    Returns:
    - int: 제거된 인형의 총 개수
    """

    # 1️⃣ 각 열을 deque로 변환하고 0 제거
    cols = [deque(filter(lambda y: y > 0, col)) for col in zip(*board)]

    removed_count = 0  # 제거된 인형 수
    stack = [0]        # 스택 초기화, 맨 처음 0으로 오류 방지

    # 2️⃣ moves 순서대로 인형 뽑기
    for move in moves:
        col_index = move - 1  # 1-indexed → 0-indexed

        # 열에 인형이 남아 있는 경우
        if cols[col_index]:
            # walrus 연산자로 뽑은 인형을 변수에 저장하면서 비교
            if (doll := cols[col_index].popleft()) == (last := stack.pop()):
                removed_count += 2  # 같은 인형이면 제거
            else:
                stack.extend([last, doll])  # 스택에 다시 쌓기

    return removed_count

'''