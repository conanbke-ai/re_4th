'''
머쓱이는 행운의 숫자 7을 가장 좋아합니다. 
정수 배열 array가 매개변수로 주어질 때, 7이 총 몇 개 있는지 return 하도록 solution 함수를 완성해보세요.

* 제한 사항
    - 1 ≤ array의 길이 ≤ 100
    - 0 ≤ array의 원소 ≤ 100,000
'''

def solution(array):
    
    cnt = 0
    
    for i in array:
        i = str(i)
        if i.count("7"):
            cnt += i.count("7")
        
    return cnt

'''
예시1)
def solution(array):
    return str(array).count('7')

예시2)
def solution(array):
    return ''.join(map(str, array)).count('7')

예시3)
def solution(array):
    answer = sum([str(i).count("7") for i in array])
    return answer
'''