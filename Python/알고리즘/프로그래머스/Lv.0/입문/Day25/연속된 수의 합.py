'''
연속된 세 개의 정수를 더해 12가 되는 경우는 3, 4, 5입니다. 
두 정수 num과 total이 주어집니다. 
연속된 수 num개를 더한 값이 total이 될 때, 정수 배열을 오름차순으로 담아 return하도록 solution함수를 완성해보세요.

* 제한 사항
    - 1 ≤ num ≤ 100
    - 0 ≤ total ≤ 1000
    - num개의 연속된 수를 더하여 total이 될 수 없는 테스트 케이스는 없습니다.
'''

def solution(num, total):
    start = (total - num*(num-1)//2) // num
    return [start + i for i in range(num)]

'''
예시1)
def solution(num, total):
    return [(total - (num * (num - 1) // 2)) // num + i for i in range(num)]

예시2)
def solution(num, total):
    answer = []
    var = sum(range(num+1))
    diff = total - var
    start_num = diff//num
    answer = [i+1+start_num for i in range(num)]
    return answer

예시3)
def solution(num, total):
    if num % 2 == 1:
        return list(range(total//num-num//2, total//num+num//2+1))
    else:
        return list(range(total//num-num//2+1, total//num+num//2+1))

예시4)
def solution(num, total):
    # base
    # offset
    # # sum of offsets = num(num-1) / 2
    base = total - num * (num-1) / 2
    base = int(base // num)
    answer = [i for i in range(base, base+num)]
    return answer
'''