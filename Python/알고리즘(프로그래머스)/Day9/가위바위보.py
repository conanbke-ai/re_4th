'''
가위는 2 바위는 0 보는 5로 표현합니다. 
가위 바위 보를 내는 순서대로 나타낸 문자열 rsp가 매개변수로 주어질 때, rsp에 저장된 가위 바위 보를 모두 이기는 경우를 순서대로 나타낸 문자열을 return하도록 solution 함수를 완성해보세요.

* 제한 사항
    - 0 < rsp의 길이 ≤ 100
    - rsp와 길이가 같은 문자열을 return 합니다.
    - rsp는 숫자 0, 2, 5로 이루어져 있습니다.

'''


def solution(rsp):
    # 이기는 값 매핑
    map_rsp = {"2": "0", "0": "5", "5": "2"}
    # 문자열 선언
    answer = ""

    # 인자를 리스트화하여 반복
    for ans_rsp in list(rsp):
        # 매핑값 할당
        answer += map_rsp[ans_rsp]

    return answer


'''
예시1)
def solution(rsp):
    d = {'0':'5','2':'0','5':'2'}
    return ''.join(d[i] for i in rsp)

예시2)
def solution(rsp):
    rsp =rsp.replace('2','s')
    rsp =rsp.replace('5','p')
    rsp =rsp.replace('0','r')
    rsp =rsp.replace('r','5')
    rsp =rsp.replace('s','0')
    rsp =rsp.replace('p','2')
    return rsp

예시3)
def solution(rsp):
    return rsp.translate(str.maketrans('025', '502'))
'''
