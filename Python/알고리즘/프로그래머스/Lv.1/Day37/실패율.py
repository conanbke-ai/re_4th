'''
슈퍼 게임 개발자 오렐리는 큰 고민에 빠졌다. 
그녀가 만든 프랜즈 오천성이 대성공을 거뒀지만, 요즘 신규 사용자의 수가 급감한 것이다. 
원인은 신규 사용자와 기존 사용자 사이에 스테이지 차이가 너무 큰 것이 문제였다.

이 문제를 어떻게 할까 고민 한 그녀는 동적으로 게임 시간을 늘려서 난이도를 조절하기로 했다. 
역시 슈퍼 개발자라 대부분의 로직은 쉽게 구현했지만, 실패율을 구하는 부분에서 위기에 빠지고 말았다. 
오렐리를 위해 실패율을 구하는 코드를 완성하라.

실패율은 다음과 같이 정의한다.
스테이지에 도달했으나 아직 클리어하지 못한 플레이어의 수 / 스테이지에 도달한 플레이어 수
전체 스테이지의 개수 N, 게임을 이용하는 사용자가 현재 멈춰있는 스테이지의 번호가 담긴 배열 stages가 매개변수로 주어질 때, 실패율이 높은 스테이지부터 내림차순으로 스테이지의 번호가 담겨있는 배열을 return 하도록 solution 함수를 완성하라.

* 제한사항
    - 스테이지의 개수 N은 1 이상 500 이하의 자연수이다.
    - stages의 길이는 1 이상 200,000 이하이다.
    - stages에는 1 이상 N + 1 이하의 자연수가 담겨있다.
    - 각 자연수는 사용자가 현재 도전 중인 스테이지의 번호를 나타낸다.
    - 단, N + 1 은 마지막 스테이지(N 번째 스테이지) 까지 클리어 한 사용자를 나타낸다.
    - 만약 실패율이 같은 스테이지가 있다면 작은 번호의 스테이지가 먼저 오도록 하면 된다.
    - 스테이지에 도달한 유저가 없는 경우 해당 스테이지의 실패율은 0 으로 정의한다.
'''
def solution(N, stages):
    result = []
    total_players = len(stages)

    for i in range(1, N + 1):
        # 현재 스테이지에 머물러 있는(클리어 못한) 사람 수
        not_cleared = stages.count(i)

        # 실패율 계산
        if total_players == 0:
            fail_rate = 0
        else:
            fail_rate = not_cleared / total_players

        result.append((i, fail_rate))
        total_players -= not_cleared  # 다음 스테이지로 넘어간 사람 수 줄이기

    # 실패율 기준으로 내림차순 정렬
    result.sort(key=lambda x: x[1], reverse=True)

    # 스테이지 번호만 추출
    answer = [stage for stage, _ in result]
    return answer

'''
예시1) 실행 시간이 가장 빠름
def solution(N, stages):
    answer = []
    fail = []
    info = [0] * (N + 2)
    for stage in stages:
        info[stage] += 1
    for i in range(N):
        be = sum(info[(i + 1):])
        yet = info[i + 1]
        if be == 0:
            fail.append((str(i + 1), 0))
        else:
            fail.append((str(i + 1), yet / be))
    for item in sorted(fail, key=lambda x: x[1], reverse=True):
        answer.append(int(item[0]))
    return answer

'- value 값 기준으로 내림차순 정렬'
'- 파이썬 3.7부터 dictionary는 순서를 보장'

예시2)
def solution(N, stages):
    fail = {}
    for i in range(1,N+1):
        try:
            fail_ = len([a for a in stages if a==i])/len([a for a in stages if a>=i])
        except:
            fail_ = 0
        fail[i]=fail_
    answer = sorted(fail, key=fail.get, reverse=True)
    return answer
'''