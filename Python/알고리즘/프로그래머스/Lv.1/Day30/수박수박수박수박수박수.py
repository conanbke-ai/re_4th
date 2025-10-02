'''
길이가 n이고, "수박수박수박수...."와 같은 패턴을 유지하는 문자열을 리턴하는 함수, solution을 완성하세요. 
예를들어 n이 4이면 "수박수박"을 리턴하고 3이라면 "수박수"를 리턴하면 됩니다.

* 제한 조건
    - n은 길이 10,000이하인 자연수입니다.
'''

def solution(n):
    
    s = []
    
    for i in range(n):
        if i == 0:
            s.append("수")
        elif i % 2 == 0 :
            s.append("수")
        else :
            s.append("박")
    
    x = "".join(str(i) for i in s)
    
    return x

'''
예시1)
def solution(n):
    result = []

    for i in range(n):
        if i % 2 == 0:
            result.append("수")
        else:
            result.append("박")
    
    return "".join(result)

예시2)
def solution(n):
    return "".join(["수박"[i%2] for i in range(n)])    
'''