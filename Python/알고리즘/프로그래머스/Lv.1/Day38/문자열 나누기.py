'''
문자열 s가 입력되었을 때 다음 규칙을 따라서 이 문자열을 여러 문자열로 분해하려고 합니다.

먼저 첫 글자를 읽습니다. 이 글자를 x라고 합시다.
이제 이 문자열을 왼쪽에서 오른쪽으로 읽어나가면서, x와 x가 아닌 다른 글자들이 나온 횟수를 각각 셉니다. 
처음으로 두 횟수가 같아지는 순간 멈추고, 지금까지 읽은 문자열을 분리합니다.
s에서 분리한 문자열을 빼고 남은 부분에 대해서 이 과정을 반복합니다. 
남은 부분이 없다면 종료합니다.
만약 두 횟수가 다른 상태에서 더 이상 읽을 글자가 없다면, 역시 지금까지 읽은 문자열을 분리하고, 종료합니다.
문자열 s가 매개변수로 주어질 때, 위 과정과 같이 문자열들로 분해하고, 분해한 문자열의 개수를 return 하는 함수 solution을 완성하세요.

* 제한사항
    - 1 ≤ s의 길이 ≤ 10,000
    - s는 영어 소문자로만 이루어져 있습니다.
'''
def solution(s):
    result = []  # 분리된 문자열 저장
    while s:
        x = s[0]
        same, diff = 0, 0

        for i, ch in enumerate(s):
            if ch == x:
                same += 1
            else:
                diff += 1

            # 같아지면 분리 지점
            if same == diff:
                result.append(s[:i+1])
                s = s[i+1:]
                break
        else:
            # 끝까지 같아지지 않으면 남은 전부 추가
            result.append(s)
            break

    return len(result)

'''
예시1)
def solution(s):
    result = 0
    same = 0
    diff = 0
    x = s[0]

    for i in range(len(s)):
        if s[i] == x:
            same += 1
        else:
            diff += 1
        
        # 같으면 분리
        if same == diff:
            result += 1
            same, diff = 0, 0
            if i + 1 < len(s):
                x = s[i + 1]

    # 남은 문자열이 있으면 1개 추가
    if same != diff:
        result += 1

    return result

예시2)
from collections import deque

def solution(s):

    ans = 0

    q = deque(s)    
    while q:
        a, b = 1, 0
        x = q.popleft()    

        while q:
            n = q.popleft()
            if n == x:
                a += 1
            else:
                b += 1

            if a == b:
                ans += 1
                break
    if a != b:
        ans += 1

    return ans

예시3)
def solution(s):
    answer = 0
    same = 0
    diff = 0

    for ch in s:
        if same == diff:
            answer += 1
            target = ch

        if ch == target:
            same += 1
        else:
            diff += 1

    return answer

예시4)
def solution(s):
    j = 0 
    cnt = 0 
    ans =0
    for idx,i in enumerate(s): 
        cnt += 1 if s[j] == i else -1 
        if cnt == 0 : 
            ans +=1 
            j = idx+1 
    return ans + 1 if cnt else ans
'''