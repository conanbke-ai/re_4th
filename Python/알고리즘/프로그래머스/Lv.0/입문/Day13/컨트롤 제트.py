'''
숫자와 "Z"가 공백으로 구분되어 담긴 문자열이 주어집니다.
 문자열에 있는 숫자를 차례대로 더하려고 합니다. 
 이 때 "Z"가 나오면 바로 전에 더했던 숫자를 뺀다는 뜻입니다. 
 숫자와 "Z"로 이루어진 문자열 s가 주어질 때, 머쓱이가 구한 값을 return 하도록 solution 함수를 완성해보세요.

* 제한 사항
    - 1 ≤ s의 길이 ≤ 200
    - -1,000 < s의 원소 중 숫자 < 1,000
    - s는 숫자, "Z", 공백으로 이루어져 있습니다.
    - s에 있는 숫자와 "Z"는 서로 공백으로 구분됩니다.
    - 연속된 공백은 주어지지 않습니다.
    - 0을 제외하고는 0으로 시작하는 숫자는 없습니다.
    - s는 "Z"로 시작하지 않습니다.
    - s의 시작과 끝에는 공백이 없습니다.
    - "Z"가 연속해서 나오는 경우는 없습니다.
'''

def solution(s):
    stack = []
    
    for n in s.split():
        # 숫자인 경우 스택에 추가 (양수/음수 모두)
        if n.isdigit() or (n.startswith('-') and n[1:].isdigit()):
            stack.append(int(n))
        # "Z"인 경우 직전 숫자 제거
        elif n == "Z" and stack:
            stack.pop()
    
    return sum(stack)

'- isdigit()은 양수만 처리'

'''
예시1)
def solution(s):
    answer = 0
    for i in range(len(s := s.split(" "))):
        answer += int(s[i]) if s[i] != "Z" else -int(s[i-1])
    return answer

예시2)
def solution(s):
    stack = []
    for a in s.split():
        if a != 'Z':
            stack.append(int(a))
        else:
            if stack:
                stack.pop()

    return sum(stack)
'''