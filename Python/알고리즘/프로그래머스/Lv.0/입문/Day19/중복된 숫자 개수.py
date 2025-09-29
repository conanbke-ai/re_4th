'''
정수가 담긴 배열 array와 정수 n이 매개변수로 주어질 때, array에 n이 몇 개 있는 지를 return 하도록 solution 함수를 완성해보세요.

* 제한 사항
    - 1 ≤ array의 길이 ≤ 100
    - 0 ≤ array의 원소 ≤ 1,000
    - 0 ≤ n ≤ 1,000
'''

def solution(array, n):
    return sum(1 for num in array if num == n)

'''
예시1)
def solution(array, n):
    return array.count(n)

'- count() : 리스트, 튜플 등 배열 안에 있는 요소값과 비교하기 때문에 타입이 동일하면 순회하며 비교 가능'
'''