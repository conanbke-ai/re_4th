'''
다음 그림과 같이 지뢰가 있는 지역과 지뢰에 인접한 위, 아래, 좌, 우 대각선 칸을 모두 위험지역으로 분류합니다.
image.png
지뢰는 2차원 배열 board에 1로 표시되어 있고 board에는 지뢰가 매설 된 지역 1과, 지뢰가 없는 지역 0만 존재합니다.
지뢰가 매설된 지역의 지도 board가 매개변수로 주어질 때, 안전한 지역의 칸 수를 return하도록 solution 함수를 완성해주세요.

* 제한사항
    - board는 n * n 배열입니다.
    - 1 ≤ n ≤ 100
    - 지뢰는 1로 표시되어 있습니다.
    - board에는 지뢰가 있는 지역 1과 지뢰가 없는 지역 0만 존재합니다.
'''

def solution(board):
    n = len(board)
    
    # 위험지역을 표시할 배열
    danger = [[0] * n for _ in range(n)]
    
    # 8방향 + 자기 자신 좌표
    directions = [(-1, -1), (-1, 0), (-1, 1),
                  (0, -1),  (0, 0),  (0, 1),
                  (1, -1),  (1, 0),  (1, 1)]
    
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:  # 지뢰 발견
                for dx, dy in directions:
                    nx, ny = i + dx, j + dy
                    if 0 <= nx < n and 0 <= ny < n:
                        danger[nx][ny] = 1  # 위험지역 표시
    
    # 안전한 지역 개수 세기
    safe_count = 0
    for i in range(n):
        for j in range(n):
            if board[i][j] == 0 and danger[i][j] == 0:
                safe_count += 1
    
    return safe_count

'''
예시1)
def solution(board):
    n = len(board)
    danger = set()  # 위험지역 좌표 저장
    
    # 8방향 + 자기 자신
    directions = [(-1, -1), (-1, 0), (-1, 1),
                  (0, -1),  (0, 0),  (0, 1),
                  (1, -1),  (1, 0),  (1, 1)]
    
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:  # 지뢰 발견
                for dx, dy in directions:
                    nx, ny = i + dx, j + dy
                    if 0 <= nx < n and 0 <= ny < n:
                        danger.add((nx, ny))  # 위험지역 좌표 추가
    
    # 안전한 지역 개수 세기
    safe_count = 0
    for i in range(n):
        for j in range(n):
            if board[i][j] == 0 and (i, j) not in danger:
                safe_count += 1
    
    return safe_count

예시2)
def solution(board):
    n = len(board)
    danger = set()
    for i, row in enumerate(board):
        for j, x in enumerate(row):
            if not x:
                continue
            danger.update((i+di, j+dj) for di in [-1,0,1] for dj in [-1, 0, 1])
    return n*n - sum(0 <= i < n and 0 <= j < n for i, j in danger)

예시3)
def solution(board):
    answer = 0

    for col in range(len(board)):
        for row in range(len(board[col])):
            if board[row][col] == 1:
                for j in range(max(col-1,0),min(col+2,len(board))):
                    for i in range(max(row-1,0),min(row+2,len(board))):
                        if board[i][j] == 1:
                            continue
                        board[i][j] = -1
    for i in board:
        answer += i.count(0)

    return answer

예시4)
def get_arounds(x, y, max_length):
    arounds = []

    for m in (-1, 0, 1):
        for n in (-1, 0, 1):
            loc = x+m, y+n
            if 0 <= loc[0] < max_length and 0 <= loc[1] < max_length:
                arounds.append(loc)
    return arounds


def solution(board):
    mines = []
    n = len(board)
    for i in range(n):
        for j in range(n):
            if board[i][j]:
                mines.append((i,j))
    for x, y in mines:
        arounds = get_arounds(x, y, n)
        for a, b in arounds:
            board[a][b] = 1

    return sum(row.count(0) for row in board)
'''