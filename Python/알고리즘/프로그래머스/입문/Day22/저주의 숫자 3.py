'''
3x 마을 사람들은 3을 저주의 숫자라고 생각하기 때문에 3의 배수와 숫자 3을 사용하지 않습니다. 
3x 마을 사람들의 숫자는 다음과 같습니다.

10진법	3x 마을에서 쓰는 숫자	10진법	3x 마을에서 쓰는 숫자
1	1	6	8
2	2	7	10
3	4	8	11
4	5	9	14
5	7	10	16
정수 n이 매개변수로 주어질 때, n을 3x 마을에서 사용하는 숫자로 바꿔 return하도록 solution 함수를 완성해주세요.

제한사항
1 ≤ n ≤ 100
'''

def solution(n):
    num = 0    # 실제 3x 마을 숫자
    count = 0  # 3x 마을 숫자 개수
    
    while count < n:
        num += 1
        if num % 3 == 0 or '3' in str(num):
            continue
        count += 1
    
    return num

'''
예시1)
def solution(n):
    return n + (n+2)//3
'''