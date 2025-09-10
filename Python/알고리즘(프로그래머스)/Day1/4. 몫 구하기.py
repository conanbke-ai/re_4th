'''
정수 num1과 num2가 주어질 때, num1을 num2로 나눈 몫을 return하도록 solution 함수를 완성해주세요.

* 제한사항
- 0 <= num1 <= 100
- 0 <= num2 <= 100
'''


def solution(num1, num2):
    result = num1 // num2
    return result


num1, num2 = map(int, input("정수 값 2개를 입력해주세요. \n : ").split())

if (num1 > 100 or num1 < 0):
    print("첫번째 정수 값을 0과 100 사이의 값으로 입력해주세요.")
elif (num2 > 100 or num2 < 0):
    print("두번째 정수 값을 0과 100 사이의 값으로 입력해주세요.")

result = solution(num1, num2)
print(f'num1 = {num1}', f'num2 = {num2}', f'result = {result}', sep="\n")


'''
예시1) floordiv__메서드 활용
solution = int.__floordiv__

: 소수점이 나오지 않게 int활용

예시2) divmod() 함수 활용
def solution(num1, num2):
    return divmod(num1, num2)[0]

: 0 - 몫 / 1 - 나머지

예시3) 소수점 버림
def solution(num1, num2):
    answer = num1 / num2
    return int(answer)
'''
