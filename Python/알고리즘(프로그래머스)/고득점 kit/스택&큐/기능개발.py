'''
프로그래머스 팀에서는 기능 개선 작업을 수행 중입니다. 
    각 기능은 진도가 100%일 때 서비스에 반영할 수 있습니다.
    또, 각 기능의 개발속도는 모두 다르기 때문에 뒤에 있는 기능이 앞에 있는 기능보다 먼저 개발될 수 있고, 이때 뒤에 있는 기능은 앞에 있는 기능이 배포될 때 함께 배포됩니다.
    먼저 배포되어야 하는 순서대로 작업의 진도가 적힌 정수 배열 progresses와 각 작업의 개발 속도가 적힌 정수 배열 speeds가 주어질 때 각 배포마다 몇 개의 기능이 배포되는지를 return 하도록 solution 함수를 완성하세요.

* 제한 사항
    - 작업의 개수(progresses, speeds배열의 길이)는 100개 이하입니다.
    - 작업 진도는 100 미만의 자연수입니다.
    - 작업 속도는 100 이하의 자연수입니다.
    - 배포는 하루에 한 번만 할 수 있으며, 하루의 끝에 이루어진다고 가정합니다. 예를 들어 진도율이 95%인 작업의 개발 속도가 하루에 4%라면 배포는 2일 뒤에 이루어집니다.
'''

'''
day_progress 구하기

작업진행률 + 30 / 100 * x == 100
left_progress = 30 / 100 * day_progress
day_progress = left_progress / 30 * 100

1. progresses 리스트 안의 각 작업 진행률에 필요한 작업 일수 구하기
2. 앞의 작업일수가 뒤의 작업일수보다 작을 시, 뒤의 기능과 같이 배포됨
3. 배포 개수와 기능 개수 반환하기
'''


import math
def solution(progresses, speeds):
    # 1. 각 기능 완료까지 남은 일수 계산
    days = [math.ceil((100 - p) / s) for p, s in zip(progresses, speeds)]

    answer = []
    current = days[0]  # 첫 기능 완료 일수 기준
    count = 1

    for day in days[1:]:
        if day <= current:
            # 뒤 기능이 앞 기능보다 빨리 끝나도, 같은 배포에 포함
            count += 1
        else:
            # 새로운 배포
            answer.append(count)
            current = day
            count = 1

    answer.append(count)  # 마지막 배포
    return answer
