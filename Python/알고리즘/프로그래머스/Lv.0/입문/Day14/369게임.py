'''
머쓱이는 친구들과 369게임을 하고 있습니다. 
369게임은 1부터 숫자를 하나씩 대며 3, 6, 9가 들어가는 숫자는 숫자 대신 3, 6, 9의 개수만큼 박수를 치는 게임입니다. 
머쓱이가 말해야하는 숫자 order가 매개변수로 주어질 때, 머쓱이가 쳐야할 박수 횟수를 return 하도록 solution 함수를 완성해보세요.

* 제한 사항
    - 1 ≤ order ≤ 1,000,000
'''

'''
for 반복문을 사용해 3, 6, 9 가 몇 번 있는지 count
'''
def solution(order):
    
    num = ["3", "6", "9"]
    cnt = 0
    # order = str(order)
    
    for i in str(order):
        for n in num:
            if i == n:
                cnt += 1

    return cnt

print(solution(29423))

'''
예시1)
def solution(order):
    return sum(map(lambda x: str(order).count(str(x)), [3, 6, 9]))
    
예시2)
def solution(order):
    answer = 0
    order = str(order)
    return order.count('3') + order.count('6') + order.count('9')
    
예시3)
def solution(order):
    answer = len([1 for ch in str(order) if ch in "369"])
    return answer
'''