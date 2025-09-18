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

'''


import math
def solution(progresses, speeds):
    # 1. 각 기능 완료까지 걸리는 일수 계산
    days = [math.ceil((100 - p) / s) for p, s in zip(progresses, speeds)]

    answer = []
    current = days[0]
    count = 1

    # 2. 배포 단위로 묶기
    for day in days[1:]:
        if day <= current:
            count += 1   # 같은 배포에 포함
        else:
            answer.append(count)  # 배포 완료
            current = day         # 새로운 배포 시작
            count = 1
    answer.append(count)  # 마지막 배포 개수 추가

    return answer


'''
예시1)
from collections import deque
import math

def solution(progresses, speeds):
    # 1. 각 작업마다 걸리는 일수 계산
    days = [math.ceil((100 - p) / s) for p, s in zip(progresses, speeds)]
    
    q = deque(days)
    answer = []
    
    while q:
        front = q.popleft()  # 기준 배포일
        count = 1            # 이번 배포에 포함될 기능 수
        
        # 큐의 앞에서부터 확인하며 같은 배포 묶기
        while q and q[0] <= front:
            q.popleft()
            count += 1
        
        answer.append(count)
    
    return answer

- 큐 활용
    FIFO(선입선출) 구조 활용: 앞에서부터 순차적으로 꺼내며 배포 진행
    deque 사용 → popleft()가 O(1)이라 효율적
    로직이 “배포 순서대로 처리”라는 문제 설명과 직관적으로 잘 맞음

예시2)
def solution(progresses, speeds):
    Q=[]
    for p, s in zip(progresses, speeds):
        if len(Q)==0 or Q[-1][0]<-((p-100)//s):
            Q.append([-((p-100)//s),1])
        else:
            Q[-1][1]+=1
    return [q[1] for q in Q]

- `zip()`을 이용해서 기능의 작업률과 속도를 합쳐서 계산이 쉽도록 했다. 
    `-((p-100)//s)` 이 부분은 필요한 작업일수를 구하는 계산식이다. 
    음수(-)로 몫을 구한 다음 다시 양수로 바꿔주었는데 `math.ceil()`한 것과 동일하다. 
    `Q[i][0]` 부분은 작업이 끝나기까지 필요한 일수이며, `Q[i][1]` 부분은 `Q[i][0]`일째에 배포 가능한 기능 수라고 보면 된다. 
    (Q = [... , [days, functions]]) 뒷 작업은 앞 작업이 끝나기까지 필요한 날짜와 비교해서 작으면 이미 앞작업에서 구했던 Q의 원소에서 기능수 부분에 +1 해주고 크면 list Q에 [필요한 일수, 기능수 = 1]의 형태로 새로 추가한다. 
    원소 개수 만큼 반복이 끝나면 배포 가능한 기능 수 부분만 잘라서 답을 리턴하면 된다.

예시3)
def solution(progresses, speeds):
    print(progresses)
    print(speeds)
    answer = []
    time = 0
    count = 0
    while len(progresses)> 0:
        if (progresses[0] + time*speeds[0]) >= 100:
            progresses.pop(0)
            speeds.pop(0)
            count += 1
        else:
            if count > 0:
                answer.append(count)
                count = 0
            time += 1
    answer.append(count)
    return answer

- pop(0) 쓰려면 첨에 리스트 reverse 해놓고 pop(0) 대신 pop() * -1 default 쓰면 됩니다.

예시4)
from math import ceil

def solution(progresses, speeds):
    daysLeft = list(map(lambda x: (ceil((100 - progresses[x]) / speeds[x])), range(len(progresses))))
    count = 1
    retList = []

    for i in range(len(daysLeft)):
        try:
            if daysLeft[i] < daysLeft[i + 1]:
                retList.append(count)
                count = 1
            else:
                daysLeft[i + 1] = daysLeft[i]
                count += 1
        except IndexError:
            retList.append(count)

    return retList

예시5)
import math

def solution(progresses, speeds):
    answer = []
    rest = []
    temp = []

    size = len(progresses)

    for i in progresses:
        rest.append(100 - i)

    for i in range(size):
        temp.append(math.ceil(rest[i] / speeds[i]))

    cnt = 0
    p = temp[0]
    for i in range(len(temp)):
        if p < temp[i]:
            answer.append(cnt)
            p = temp[i]
            cnt = 0
        cnt += 1
    answer.append(cnt)


    return answer
'''
