'''
정수 배열 numbers가 주어집니다. 
numbers에서 서로 다른 인덱스에 있는 두 개의 수를 뽑아 더해서 만들 수 있는 모든 수를 배열에 오름차순으로 담아 return 하도록 solution 함수를 완성해주세요.

* 제한사항
    - numbers의 길이는 2 이상 100 이하입니다.
    - numbers의 모든 수는 0 이상 100 이하입니다.
'''

def solution(numbers):
    
    result = []
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if i != j:
                if numbers[i] + numbers[j] not in result:
                    result.append(numbers[i] + numbers[j])
    
    return sorted(result)

'''
예시1)
def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            answer.append(numbers[i] + numbers[j])
    return sorted(list(set(answer)))

예시2)
from itertools import combinations

def solution(numbers):
    answer = []
    l = list(combinations(numbers, 2))

    for i in l:
        answer.append(i[0]+i[1])
    answer = list(set(answer))
    answer.sort()

    return answer
'''