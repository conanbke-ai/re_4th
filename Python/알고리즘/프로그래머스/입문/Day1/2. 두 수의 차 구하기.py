'''
정수 num1과 num2가 주어질 때, num1과 num2의 차를 return하도록 solution 함수를 완성해주세요.

* 제한사항
- -50000 <= num1 <= 50000
- -50000 <= num2 <= 50000
'''


def solution(num1, num2):
    result = num1 - num2
    return result


num1, num2 = map(int, input("정수 값 2개를 입력해주세요. \n : ").split())

if (num1 > 50000 or num1 < -50000):
    print("첫번째 정수 값을 -50000과 50000 사이의 값으로 입력해주세요.")
elif (num2 > 50000 or num2 < -50000):
    print("두번째 정수 값을 - 50000과 50000 사이의 값으로 입력해주세요.")

result = solution(num1, num2)
print(f'num1 = {num1}', f'num2 = {num2}', f'result = {result}', sep="\n")


'''
예시) 람다표현식 사용
solution = lambda num1, num2 : num1 - num2
'''
