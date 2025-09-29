'''
선분 세 개로 삼각형을 만들기 위해서는 다음과 같은 조건을 만족해야 합니다.

가장 긴 변의 길이는 다른 두 변의 길이의 합보다 작아야 합니다.
삼각형의 두 변의 길이가 담긴 배열 sides이 매개변수로 주어집니다. 
나머지 한 변이 될 수 있는 정수의 개수를 return하도록 solution 함수를 완성해주세요.

* 제한 사항
    - sides의 원소는 자연수입니다.
    - sides의 길이는 2입니다.
    - 1 ≤ sides의 원소 ≤ 1,000
'''

def solution(sides):
    a, b = sides
    small, big = min(a, b), max(a, b)

    # 1) x가 가장 긴 변일 때: 1 <= x < a+b
    case1 = (a + b - 1) - big

    # 2) a 또는 b가 가장 긴 변일 때: big < small + x → x > big-small
    case2 = small

    return case1 + case2

'''
예시1)
def solution(sides):
    return sum(sides) - max(sides) + min(sides) - 1

'주어지지 않은 변의 길이를 n이라고 할 때, 
n이 삼각형의 가장 긴 변이라면 주어진 두 변의 합보다 작아야 하고(sum(sides) > n) 
가장 긴 변이 아니라면 주어진 두 변 중 큰 변(max(sides))이 n과 작은 변(min(sides))의 합보다 커야 함(n > max(sides) - min(sides)) 
따라서 n의 범위는 (sum(sides)> n > max(sides) - min(sides))가 되고 
열린 범위(경계값이 포함되지 않음)기 때문에 두 값의 차에서 -1을 하는 것. 
위 식은 (sum(sides) - (max(sides) - min(sides)) - 1) 에서 괄호를 풀어준 것.'

예시2)
def solution(sides):
    return 2 * min(sides) - 1
'''