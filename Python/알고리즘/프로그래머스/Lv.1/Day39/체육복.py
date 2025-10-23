'''
점심시간에 도둑이 들어, 일부 학생이 체육복을 도난당했습니다. 
다행히 여벌 체육복이 있는 학생이 이들에게 체육복을 빌려주려 합니다. 
학생들의 번호는 체격 순으로 매겨져 있어, 바로 앞번호의 학생이나 바로 뒷번호의 학생에게만 체육복을 빌려줄 수 있습니다. 
예를 들어, 4번 학생은 3번 학생이나 5번 학생에게만 체육복을 빌려줄 수 있습니다. 
체육복이 없으면 수업을 들을 수 없기 때문에 체육복을 적절히 빌려 최대한 많은 학생이 체육수업을 들어야 합니다.

전체 학생의 수 n, 체육복을 도난당한 학생들의 번호가 담긴 배열 lost, 여벌의 체육복을 가져온 학생들의 번호가 담긴 배열 reserve가 매개변수로 주어질 때, 체육수업을 들을 수 있는 학생의 최댓값을 return 하도록 solution 함수를 작성해주세요.

* 제한사항
    - 전체 학생의 수는 2명 이상 30명 이하입니다.
    - 체육복을 도난당한 학생의 수는 1명 이상 n명 이하이고 중복되는 번호는 없습니다.
    - 여벌의 체육복을 가져온 학생의 수는 1명 이상 n명 이하이고 중복되는 번호는 없습니다.
    - 여벌 체육복이 있는 학생만 다른 학생에게 체육복을 빌려줄 수 있습니다.
    - 여벌 체육복을 가져온 학생이 체육복을 도난당했을 수 있습니다. 이때 이 학생은 체육복을 하나만 도난당했다고 가정하며, 남은 체육복이 하나이기에 다른 학생에게는 체육복을 빌려줄 수 없습니다.
'''
def solution(n, lost, reserve):
    # 여벌이 있으면서 잃어버린 학생 제거
    lost_ = sorted(list(set(lost) - set(reserve)))
    reserve_ = sorted(list(set(reserve) - set(lost)))
    
    for i in reserve_:
        if i - 1 in lost_:
            lost_.remove(i - 1)
        elif i + 1 in lost_:
            lost_.remove(i + 1)
    
    # 전체 학생 - 여전히 체육복이 없는 학생 수
    return n - len(lost_)

'''
예시1) collections.Counter
from collections import Counter

def solution(n, lost, reserve):
    clothes = Counter({i: 1 for i in range(1, n + 1)})
    for l in lost:
        clothes[l] -= 1
    for r in reserve:
        clothes[r] += 1

    for i in range(1, n + 1):
        if clothes[i] == 0:
            if i > 1 and clothes[i - 1] == 2:
                clothes[i - 1] -= 1
                clothes[i] += 1
            elif i < n and clothes[i + 1] == 2:
                clothes[i + 1] -= 1
                clothes[i] += 1

    return sum(1 for v in clothes.values() if v >= 1)

예시2) 정렬 기반 투 포인터(two-pointer)
def solution(n, lost, reserve):
    # 정렬 (중요: 투 포인터는 정렬된 상태에서 동작해야 함)
    lost.sort()
    reserve.sort()
    
    # 여벌 옷을 가진 학생이 도난당한 경우 먼저 처리
    lost_copy = lost.copy()
    for l in lost_copy:
        if l in reserve:
            lost.remove(l)
            reserve.remove(l)
    
    # 이제 투 포인터 방식으로 양쪽 비교
    i, j = 0, 0
    while i < len(lost) and j < len(reserve):
        if reserve[j] == lost[i] - 1 or reserve[j] == lost[i] + 1:
            # 빌려줄 수 있는 경우
            i += 1
            j += 1
        elif reserve[j] < lost[i] - 1:
            # 여벌 학생이 더 앞 번호 → 다음 여벌 확인
            j += 1
        else:
            # 잃어버린 학생이 더 앞 번호 → 다음 잃은 사람 확인
            i += 1
    
    # 빌리지 못한 학생 수 계산
    borrowable = n - len(lost) + i
    return borrowable
'''