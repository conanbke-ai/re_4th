'''
한국중학교에 다니는 학생들은 각자 정수 번호를 갖고 있습니다. 
이 학교 학생 3명의 정수 번호를 더했을 때 0이 되면 3명의 학생은 삼총사라고 합니다. 
예를 들어, 5명의 학생이 있고, 각각의 정수 번호가 순서대로 -2, 3, 0, 2, -5일 때, 첫 번째, 세 번째, 네 번째 학생의 정수 번호를 더하면 0이므로 세 학생은 삼총사입니다. 또한, 두 번째, 네 번째, 다섯 번째 학생의 정수 번호를 더해도 0이므로 세 학생도 삼총사입니다. 따라서 이 경우 한국중학교에서는 두 가지 방법으로 삼총사를 만들 수 있습니다.

한국중학교 학생들의 번호를 나타내는 정수 배열 number가 매개변수로 주어질 때, 학생들 중 삼총사를 만들 수 있는 방법의 수를 return 하도록 solution 함수를 완성하세요.

* 제한사항
    - 3 ≤ number의 길이 ≤ 13
    - -1,000 ≤ number의 각 원소 ≤ 1,000
    - 서로 다른 학생의 정수 번호가 같을 수 있습니다.
'''
'- for문 이용'
def solution(number):
    count = 0  # 삼총사 개수를 세기 위한 변수
    
    # 세 명을 뽑는 모든 조합 확인 (중복 없이)
    for i in range(len(number)):
        for j in range(i + 1, len(number)):
            for k in range(j + 1, len(number)):
                # 세 학생 번호의 합이 0이면 삼총사
                if number[i] + number[j] + number[k] == 0:
                    count += 1
                    
    return count

'''
예시1) combination() 이용
from itertools import combinations

def solution(number):
    return sum(1 for a, b, c in combinations(number, 3) if a + b + c == 0)

예시2)
def solution (number) :
    from itertools import combinations
    cnt = 0
    for i in combinations(number,3) :
        if sum(i) == 0 :
            cnt += 1
    return cnt

예시3) 투 포인터 이용
def solution(number):
    number.sort()  # 오름차순 정렬
    count = 0
    n = len(number)
    
    # 첫 번째 원소를 고정하고, 나머지 두 개는 투포인터로 찾기
    for i in range(n - 2):
        left, right = i + 1, n - 1
        
        while left < right:
            total = number[i] + number[left] + number[right]
            
            if total == 0:
                count += 1
                left += 1
                right -= 1
            elif total < 0:
                left += 1  # 합이 작으면 더 큰 수를 선택
            else:
                right -= 1  # 합이 크면 더 작은 수를 선택
                
    return count

예시4) DFS(깊이 우선 탐색) 이용
def solution(number):
    tot = 0  # 삼총사 개수 누적용

    def dfs(i, cnt, sum_num):
        nonlocal tot  # 내부 함수에서 바깥 변수 tot 변경 가능하게 함

        # 🎯 종료 조건 1: 세 명 뽑았고 합이 0이면 삼총사
        if cnt == 3 and not sum_num:
            tot += 1
            return

        # 🎯 종료 조건 2: 인덱스가 끝까지 갔으면 종료
        if i == len(number):
            return

        # 👇 두 가지 선택지로 분기
        if cnt < 3:
            # 현재 number[i]를 포함하는 경우
            dfs(i + 1, cnt + 1, sum_num + number[i])
            # 현재 number[i]를 포함하지 않는 경우
            dfs(i + 1, cnt, sum_num)

    dfs(0, 0, 0)  # 탐색 시작
    return tot
'''