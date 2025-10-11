'''
숫자로 이루어진 문자열 t와 p가 주어질 때, t에서 p와 길이가 같은 부분문자열 중에서, 이 부분문자열이 나타내는 수가 p가 나타내는 수보다 작거나 같은 것이 나오는 횟수를 return하는 함수 solution을 완성하세요.

예를 들어, t="3141592"이고 p="271" 인 경우, t의 길이가 3인 부분 문자열은 314, 141, 415, 159, 592입니다. 이 문자열이 나타내는 수 중 271보다 작거나 같은 수는 141, 159 2개 입니다.

* 제한사항
    - 1 ≤ p의 길이 ≤ 18
    - p의 길이 ≤ t의 길이 ≤ 10,000
    - t와 p는 숫자로만 이루어진 문자열이며, 0으로 시작하지 않습니다.
'''
# import random

# def solution(t, p):
    
#     stack = []
#     cnt = 0
#     x = []
#     y = ""

#     for i in range(len(t)**len(p)):
#         x = random.choices(list(t), k=3)
#         for z in x:
#             y += z
#         if int(y) not in stack:
#             stack.append(int(y))

#     for j in stack:
#         if stack.pop() <= int(p):
#             cnt += 1

#     return cnt

def solution(t, p):
    count = 0
    p_len = len(p)
    p_num = int(p)

    # t에서 길이 p_len 만큼의 부분 문자열을 순차적으로 확인
    for i in range(len(t) - p_len + 1):
        sub = int(t[i:i+p_len])
        if sub <= p_num:
            count += 1

    return count

'''
예시1)
def solution(t, p):
    return len([t[i: i+len(p)] for i in range(len(t)-len(p)+1) if int(t[i: i+len(p)]) <= int(p)])
'''