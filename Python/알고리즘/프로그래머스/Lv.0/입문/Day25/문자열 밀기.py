'''
문자열 "hello"에서 각 문자를 오른쪽으로 한 칸씩 밀고 마지막 문자는 맨 앞으로 이동시키면 "ohell"이 됩니다. 
이것을 문자열을 민다고 정의한다면 문자열 A와 B가 매개변수로 주어질 때, A를 밀어서 B가 될 수 있다면 밀어야 하는 최소 횟수를 return하고 밀어서 B가 될 수 없으면 -1을 return 하도록 solution 함수를 완성해보세요.

* 제한 사항
    - 0 < A의 길이 = B의 길이 < 100
    - A, B는 알파벳 소문자로 이루어져 있습니다.
'''

# from collections import deque

# def solution(A, B):
    
#     if sorted(A) == sorted(B):
#         dq = deque()
#         dq.append(A)
#         for i in range(len(A)):
#             if dq.rotate(i) == B:
#                 return i
#     else :
#         return -1

from collections import deque

def solution(A, B):
    if len(A) != len(B) or sorted(A) != sorted(B):
        return -1

    dq = deque(A)
    for i in range(len(A)):
        if list(dq) == list(B):  # deque를 리스트로 변환해 비교
            return i
        dq.rotate(1)  # 오른쪽으로 한 칸씩 회전
    return -1

'''
예시1)
solution=lambda a,b:(b*2).find(a)

'- def solution(A, B): return (B * 2).find(A)'
'''