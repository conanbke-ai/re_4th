'''
정수 배열 numbers가 매개변수로 주어집니다. 
numbers의 원소 중 두 개를 곱해 만들 수 있는 최댓값을 return하도록 solution 함수를 완성해주세요.

* 제한 사항
    - -10,000 ≤ numbers의 원소 ≤ 10,000
    - 2 ≤ numbers 의 길이 ≤ 100
'''
def solution(numbers):

    numbers.sort()
    
    return max(numbers[-1] * numbers[-2], numbers[0] * numbers[1])

'''
예시1)
from itertools  import combinations as comb

def solution(numbers):
    an_list=[]
    for i,j in comb(numbers,2):
        an_list.append(i*j)
    return max(an_list)
    
'- math.comb(n, k)
    조합의 개수를 계산하는 함수
    Python 3.8 이상에서 사용 가능
    n : 전체 원소 개수
    k : 뽑을 원소 개수
    반환 : 경우의 수(int)
'
'- itertools.combinations(iterable, r)
    실제 조합된 원소들을 튜플 형태로 생성해 줌
    경우의 수(숫자)가 아니라, 조합의 구체적인 결과를 얻고 싶을 때 사용
    
    ex)
    from itertools import combinations

    nums = [1, 2, 3, 4]
    for c in combinations(nums, 2):
        print(c)   
        
    # (1, 2)
    # (1, 3)
    # (1, 4)
    # (2, 3)
    # (2, 4)
    # (3, 4)
'
'''