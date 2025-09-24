'''
두 배열이 얼마나 유사한지 확인해보려고 합니다. 
문자열 배열 s1과 s2가 주어질 때 같은 원소의 개수를 return하도록 solution 함수를 완성해주세요.

* 제한 사항
    - 1 ≤ s1, s2의 길이 ≤ 100
    - 1 ≤ s1, s2의 원소의 길이 ≤ 10
    - s1과 s2의 원소는 알파벳 소문자로만 이루어져 있습니다
    - s1과 s2는 각각 중복된 원소를 갖지 않습니다.
'''

def solution(s1, s2):
    
    cnt = 0
    
    for i in s1:
        cnt += s2.count(i)
    
    return cnt

'''
예시1)
def solution(s1, s2):
    return len(set(s1)&set(s2))
    
'- 집합 set() 을 활용하여 교집합의 길이 계산'    

예시2)
def solution(s1, s2):
    answer = 0

    for word in s1:
        if word in s2:
            answer += 1
        else:
            continue

    return answer
    
예시3)
def solution(s1, s2):
    dic = {i:1 for i in s1}
    answer = sum(dic.get(j,0)for j in s2)
    return answer
'''