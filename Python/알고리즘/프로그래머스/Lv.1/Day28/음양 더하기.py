'''
어떤 정수들이 있습니다. 
이 정수들의 절댓값을 차례대로 담은 정수 배열 absolutes와 이 정수들의 부호를 차례대로 담은 불리언 배열 signs가 매개변수로 주어집니다. 실제 정수들의 합을 구하여 return 하도록 solution 함수를 완성해주세요.

* 제한사항
    - absolutes의 길이는 1 이상 1,000 이하입니다.
    - absolutes의 모든 수는 각각 1 이상 1,000 이하입니다.
    - signs의 길이는 absolutes의 길이와 같습니다.
    - signs[i] 가 참이면 absolutes[i] 의 실제 정수가 양수임을, 그렇지 않으면 음수임을 의미합니다.
'''

def solution(absolutes, signs):
    
    x = []
    
    for i in range(len(absolutes)):
        if signs[i]:
            x.append(int(absolutes[i]))
        else:
            x.append(-(int(absolutes[i])))
        
    
    return sum(x)

'''
예시1)
def solution(absolutes, signs):
    return sum(absolutes if sign else -absolutes for absolutes, sign in zip(absolutes, signs))

예시2)
def solution(absolutes, signs):
    answer=0
    for absolute,sign in zip(absolutes,signs):
        if sign:
            answer+=absolute
        else:
            answer-=absolute
    return answer

예시3)
def solution(absolutes, signs):
    return sum([2*x*y - x for x, y in zip(absolutes, signs)])
'- 만약 y=True (1이라면) → 2*x*1 - x = 2x - x = x'
'- 만약 y=False (0이라면) → 2*x*0 - x = 0 - x = -x'
'''