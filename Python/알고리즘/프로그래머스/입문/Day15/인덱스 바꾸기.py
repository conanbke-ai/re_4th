'''
문자열 my_string과 정수 num1, num2가 매개변수로 주어질 때, my_string에서 인덱스 num1과 인덱스 num2에 해당하는 문자를 바꾼 문자열을 return 하도록 solution 함수를 완성해보세요.

제한사항
1 < my_string의 길이 < 100
0 ≤ num1, num2 < my_string의 길이
my_string은 소문자로 이루어져 있습니다.
num1 ≠ num2
'''
def solution(my_string, num1, num2):    
    
    result = ""

    for n, i in enumerate(my_string):
        
        if n == num1:
            result += my_string[num2]
        elif n == num2:
            result += my_string[num1]
        else:
            result += i
    
    return result

# print(solution("hello", 1, 2))

'''
예시1)
def solution(my_string, num1, num2):
    s = list(my_string)
    s[num1],s[num2] = s[num2],s[num1]
    return ''.join(s)
    
예시2)
def solution(my_string, num1, num2):
    lst = list(my_string); lst[num1], lst[num2] = lst[num2], lst[num1]; return "".join(lst)

'- ; 는 한 줄에 여러 문장 표형 시 사용됨'

예시3)
solution = lambda s, i, j: "".join(
    (lambda lst: (lst.__setitem__(i, lst[j]) or lst.__setitem__(j, lst[i]) or lst)(list(s)))()
)
'''