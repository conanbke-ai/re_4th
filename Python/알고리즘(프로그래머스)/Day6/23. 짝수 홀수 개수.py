'''
정수가 담긴 리스트 num_list가 주어질 때, num_list의 원소 중 짝수와 홀수의 개수를 담은 배열을 return 하도록 solution 함수를 완성해보세요.

* 제한 사항
    1 ≤ num_list의 길이 ≤ 100
    0 ≤ num_list의 원소 ≤ 1,000
'''


def solution(num_list):
    cnt1 = 0
    cnt2 = 0
    for x in num_list:
        if x % 2 == 0:
            cnt1 += 1
        else:
            cnt2 += 1
    return cnt1, cnt2


'''
예시1)
def solution(num_list):
    odd = sum(1 for n in num_list if n % 2)
    return [len(num_list) - odd, odd]

예시2)
def solution(num_list):
    answer = [0,0]
    for n in num_list:
        answer[n%2]+=1
    return answer

예시3)
def solution(num_list):
    div_num_list = list(map(lambda v: v % 2, num_list))
    return [div_num_list.count(0), div_num_list.count(1)]
'''
