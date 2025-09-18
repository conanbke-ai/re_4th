'''
각에서 0도 초과 90도 미만은 예각, 90도는 직각, 90도 초과 180도 미만은 둔각 180도는 평각으로 분류합니다. 
각 angle이 매개변수로 주어질 때 예각일 때 1, 직각일 때 2, 둔각일 때 3, 평각일 때 4를 return하도록 solution 함수를 완성해주세요.

    - 예각 : 0 < angle < 90
    - 직각 : angle = 90
    - 둔각 : 90 < angle < 180
    - 평각 : angle = 180

* 제한 사항
    - 0 < angle ≤ 180
    - angle은 정수입니다.
'''


def solution(angle):

    answer = 0
    # 예각일 시
    if 0 < angle < 90:
        answer = 1
    # 직각일 시
    elif angle == 90:
        answer = 2
    # 둔각일 시
    elif 90 < angle < 180:
        answer = 3
    # 평각일 시
    elif angle == 180:
        answer = 4
    else:
        print("angle은 0과 180 사이입니다.")

    return answer


'''
예시1)
def solution(angle):
    answer = (angle // 90) * 2 + (angle % 90 > 0) * 1
    return answer

예시2)
def solution(angle):
    if angle<=90:
        return 1 if angle<90 else 2
    else:
        return 3 if angle<180 else 4

예시3)
def solution(angle):
    angles = {180: 4, 91: 3, 90: 2, 0: 1}
    for base, result in angles.items():
        if angle >= base:
            return result

예시4)
def solution(angle):
    return 2 if angle==90 else 1 if angle<90 else 4 if angle==180 else 3

예시5)
def solution(angle):
    return [[1, 2], [3, 4]][angle > 90][angle % 90 == 0]
'''
