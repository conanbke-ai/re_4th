'''
정수 n을 기준으로 n과 가까운 수부터 정렬하려고 합니다. 
이때 n으로부터의 거리가 같다면 더 큰 수를 앞에 오도록 배치합니다. 
정수가 담긴 배열 numlist와 정수 n이 주어질 때 numlist의 원소를 n으로부터 가까운 순서대로 정렬한 배열을 return하도록 solution 함수를 완성해주세요.

* 제한 사항
    - 1 ≤ n ≤ 10,000
    - 1 ≤ numlist의 원소 ≤ 10,000
    - 1 ≤ numlist의 길이 ≤ 100
    - numlist는 중복된 원소를 갖지 않습니다.
'''
def solution(numlist, n):
            # (거리 순, 큰 수 우선) 기준으로 정렬
    return sorted(numlist, key=lambda x: (abs(x - n), -x))

'''
예시1)
def solution(numlist, n):
    # num -> (abs(n-num), -num)
    numlist = [(abs(n-num), -num) for num in numlist]
    # 첫 번째 요소를 기준으로 오름차순 정렬 and 두 번째 요소를 기준으로 내림차순 정렬
    numlist.sort()
    # 두 번쨰 요소만 반환
    return [-num for _, num in numlist]
'''