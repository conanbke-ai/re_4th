'''
차원 좌표 평면에 변이 축과 평행한 직사각형이 있습니다. 
직사각형 네 꼭짓점의 좌표 [[x1, y1], [x2, y2], [x3, y3], [x4, y4]]가 담겨있는 배열 dots가 매개변수로 주어질 때, 직사각형의 넓이를 return 하도록 solution 함수를 완성해보세요.

* 제한 사항
    - dots의 길이 = 4
    - dots의 원소의 길이 = 2
    - -256 < dots[i]의 원소 < 256
    - 잘못된 입력은 주어지지 않습니다.
'''

def solution(dots):
    # dots에서 x좌표, y좌표 각각 분리
    x_coords = [x for x, _ in dots]
    y_coords = [y for _, y in dots]
    
    # 가로, 세로 길이 구하기
    width = max(x_coords) - min(x_coords)
    height = max(y_coords) - min(y_coords)
    
    return width * height

'''
예시1)
def solution(dots):
    return (max(dots)[0] - min(dots)[0])*(max(dots)[1] - min(dots)[1])

예시2)
def solution(dots):
    answer = 0
    for i in range(1, len(dots)):
        if dots[i][1] == dots[0][1]:
            width = abs(dots[i][0] - dots[0][0])
        if dots[i][0] == dots[0][0]:
            height = abs(dots[i][1] - dots[0][1])
    answer = width * height
    return answer
'''