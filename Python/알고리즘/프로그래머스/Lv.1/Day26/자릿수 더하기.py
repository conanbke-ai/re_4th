'''
자연수 N이 주어지면, N의 각 자릿수의 합을 구해서 return 하는 solution 함수를 만들어 주세요.
예를들어 N = 123이면 1 + 2 + 3 = 6을 return 하면 됩니다.

* 제한 사항
    - N의 범위 : 100,000,000 이하의 자연수
'''

def solution(n):

    result = 0
    
    while n > 0:
        result += n % 10  # 일의 자리 더하기
        n //= 10         # 10으로 나눠서 다음 자리로
        
    return result

'''
예시1)
def solution(n):
    temp = list(map(int, list(str(n))))
    answer = sum(temp)
    return answer
'''