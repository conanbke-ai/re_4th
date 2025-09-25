'''
괄호가 바르게 짝지어졌다는 것은 '(' 문자로 열렸으면 반드시 짝지어서 ')' 문자로 닫혀야 한다는 뜻입니다. 예를 들어

"()()" 또는 "(())()" 는 올바른 괄호입니다.
")()(" 또는 "(()(" 는 올바르지 않은 괄호입니다.
'(' 또는 ')' 로만 이루어진 문자열 s가 주어졌을 때, 문자열 s가 올바른 괄호이면 true를 return 하고, 올바르지 않은 괄호이면 false를 return 하는 solution 함수를 완성해 주세요.

*제한사항
    - 문자열 s의 길이 : 100,000 이하의 자연수
    - 문자열 s는 '(' 또는 ')' 로만 이루어져 있습니다.
'''


def solution(s):
    first, *middle, last = s
    if first == '(' and last == ')':
        return True
    else:
        return False


'''
예시1)
def solution(s):
    stack = []
    for ch in s:
        if ch == '(':
            stack.append(ch)  # 여는 괄호 push
        else:  # 닫는 괄호
            if not stack:  # = if stack == 0 스택이 비었는데 닫는 괄호가 나오면 잘못됨
                return False
            stack.pop()  # 짝 맞는 여는 괄호 제거
    return len(stack) == 0  # 스택이 비어 있어야 올바른 괄호

예시2)
def is_pair(s):
    st = list()
    for c in s:
        if c == '(':
            st.append(c)

        if c == ')':
            try:
                st.pop()
            except IndexError:
                return False

    return len(st) == 0

예시3)
def is_pair(s):
    pair = 0
    for x in s:
        if pair < 0: break
        pair = pair + 1 if x == "(" else pair - 1 if x == ")" else pair
    return pair == 0
    
예시4)
def solution(s):
    stack = 0
    
    for ch in s:
        if ch == "(":
            stack += 1
        else:
            if stack == 0:  # 여는 게 없는 데 닫는 괄호가 나오면
                return False
            else:
                stack -= 1
    return stack == 0
'''
