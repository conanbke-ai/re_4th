'''

'''

def solution(n):
    
    result = 0
    l = len(str(n)) - 1
    
    while True:
        result += n // (10 ** l)
        n %= (10 ** l)
        l -= 1
        
        if l == -1:
            return result
        
'''
예시1)
def solution(n):
    return sum(int(d) for d in str(n))

예시2)
def solution(n):
    result = 0
    while n > 0:
        result += n % 10  # 가장 오른쪽 자리 숫자 추출
        n //= 10          # 오른쪽 자리 제거
    return result

예시3)
def solution(n):
    return sum(list(map(int,list(str(n)))))

예시4)
def solution(n):
    answer = 0
    while n:
        n, r = divmod(n, 10)
        answer += r
    return answer
'''