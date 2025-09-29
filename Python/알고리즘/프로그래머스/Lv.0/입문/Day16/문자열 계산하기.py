'''
my_string은 "3 + 5"처럼 문자열로 된 수식입니다. 
문자열 my_string이 매개변수로 주어질 때, 수식을 계산한 값을 return 하는 solution 함수를 완성해주세요.

* 제한 사항
    - 연산자는 +, -만 존재합니다.
    - 문자열의 시작과 끝에는 공백이 없습니다.
    - 0으로 시작하는 숫자는 주어지지 않습니다.
    - 잘못된 수식은 주어지지 않습니다.
    - 5 ≤ my_string의 길이 ≤ 100
    - my_string을 계산한 결과값은 1 이상 100,000 이하입니다.
    - my_string의 중간 계산 값은 -100,000 이상 100,000 이하입니다.
    - 계산에 사용하는 숫자는 1 이상 20,000 이하인 자연수입니다.
    - my_string에는 연산자가 적어도 하나 포함되어 있습니다.
    - return type 은 정수형입니다.
    - my_string의 숫자와 연산자는 공백 하나로 구분되어 있습니다.
'''

def solution(my_string):

    s = my_string.split()
    
    # 첫 숫자로 초기화
    result = int(s[0])

    for n, i in enumerate(s):
        
        if i == "+":
            result += int(s[n+1])
        elif i == "-":
            result -= int(s[n+1])
        else:
            continue

    return result
    
print(solution("3 + 4 + 6 - 7"))


'''
예시1)
def solution(my_string):
    return sum(int(i) for i in my_string.replace(' - ', ' + -').split(' + '))

예시2)
solution=eval

"solution = eval" → 문자열 수식을 즉시 계산
장점: 코드 간단, 연산자 우선순위 자동 처리
단점: 보안 위험, 입력 검증 필요

예시3)

'''