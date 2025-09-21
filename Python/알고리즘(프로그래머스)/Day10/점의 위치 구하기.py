'''
사분면은 한 평면을 x축과 y축을 기준으로 나눈 네 부분입니다. 사분면은 아래와 같이 1부터 4까지 번호를매깁니다.
스크린샷 2022-07-07 오후 3.27.04 복사본.png

x 좌표와 y 좌표가 모두 양수이면 제1사분면에 속합니다.
x 좌표가 음수, y 좌표가 양수이면 제2사분면에 속합니다.
x 좌표와 y 좌표가 모두 음수이면 제3사분면에 속합니다.
x 좌표가 양수, y 좌표가 음수이면 제4사분면에 속합니다.
x 좌표 (x, y)를 차례대로 담은 정수 배열 dot이 매개변수로 주어집니다. 좌표 dot이 사분면 중 어디에 속하는지 1, 2, 3, 4 중 하나를 return 하도록 solution 함수를 완성해주세요.

* 제한 사항
    - dot의 길이 = 2
    - dot[0]은 x좌표를, dot[1]은 y좌표를 나타냅니다
    - -500 ≤ dot의 원소 ≤ 500
    - dot의 원소는 0이 아닙니다.
'''

def solution(dot):

    x, y = dot
    
    if x != 0 and y != 0:
        if x > 0:
            if y > 0 :
                return 1
            else:
                return 4
        elif x < 0:
            if y > 0 :
                return 2
            else:
                return 3
    else:
        pass

'''
예시1)
def solution(dot):
    quad = [(3,2),(4,1)]
    return quad[dot[0] > 0][dot[1] > 0]

예시2)
def solution(dot):
    a, b = 1, 0
    if dot[0]*dot[1] > 0:
        b = 1
    if dot[1] < 0:
        a = 2
    return 2*a-b

예시3)
def solution(dot):
    return [[1, 4], [2, 3]][dot[0] < 0][dot[1] < 0]
'''