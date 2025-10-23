'''
수포자는 수학을 포기한 사람의 준말입니다. 
수포자 삼인방은 모의고사에 수학 문제를 전부 찍으려 합니다. 
수포자는 1번 문제부터 마지막 문제까지 다음과 같이 찍습니다.

1번 수포자가 찍는 방식: 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, ...
2번 수포자가 찍는 방식: 2, 1, 2, 3, 2, 4, 2, 5, 2, 1, 2, 3, 2, 4, 2, 5, ...
3번 수포자가 찍는 방식: 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, ...

1번 문제부터 마지막 문제까지의 정답이 순서대로 들은 배열 answers가 주어졌을 때, 가장 많은 문제를 맞힌 사람이 누구인지 배열에 담아 return 하도록 solution 함수를 작성해주세요.

* 제한 조건
    - 시험은 최대 10,000 문제로 구성되어있습니다.
    - 문제의 정답은 1, 2, 3, 4, 5중 하나입니다.
    - 가장 높은 점수를 받은 사람이 여럿일 경우, return하는 값을 오름차순 정렬해주세요.
'''

def solution(answers):
    # 각 수포자의 찍기 패턴
    p1 = [1, 2, 3, 4, 5]
    p2 = [2, 1, 2, 3, 2, 4, 2, 5]
    p3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    # 맞춘 개수 계산
    scores = [0, 0, 0]  # 1번, 2번, 3번
    for i, ans in enumerate(answers):
        if ans == p1[i % len(p1)]:
            scores[0] += 1
        if ans == p2[i % len(p2)]:
            scores[1] += 1
        if ans == p3[i % len(p3)]:
            scores[2] += 1

    # 가장 많이 맞춘 사람 구하기
    max_score = max(scores)
    result = [i+1 for i, s in enumerate(scores) if s == max_score]

    return result

'''
예시1)
def solution(answers):
    # 각 수포자의 찍기 패턴
    patterns = [
        [1, 2, 3, 4, 5],                   # 1번 수포자
        [2, 1, 2, 3, 2, 4, 2, 5],           # 2번 수포자
        [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]      # 3번 수포자
    ]

    scores = [0] * len(patterns)  # 수포자별 맞힌 개수 저장

    # 각 문제에 대해 정답 비교
    for q_idx, answer in enumerate(answers):
        for person_idx, pattern in enumerate(patterns):
            # (문제 번호 mod 패턴 길이)로 패턴 반복
            if answer == pattern[q_idx % len(pattern)]:
                scores[person_idx] += 1

    # 최고 점수를 받은 사람(1번부터 시작)
    top_score = max(scores)
    return [i + 1 for i, score in enumerate(scores) if score == top_score]

예시2)
def solution(answers):
    p = [[1,2,3,4,5],[2,1,2,3,2,4,2,5],[3,3,1,1,2,2,4,4,5,5]]
    s = [sum(a == v[i % len(v)] for i, a in enumerate(answers)) for v in p]
    return [i + 1 for i, v in enumerate(s) if v == max(s)]

예시3)
def answer_type(pattern, length):
    return (pattern * (length // len(pattern))) + pattern[:length % len(pattern)]

def check_answer(p, a):
    return sum(x == y for x, y in zip(p, a))

def solution(answers):
    patterns = [
        [1, 2, 3, 4, 5],
        [2, 1, 2, 3, 2, 4, 2, 5],
        [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    ]
    scores = [check_answer(answer_type(p, len(answers)), answers) for p in patterns]
    max_score = max(scores)
    return [i + 1 for i, score in enumerate(scores) if score == max_score]

'''

