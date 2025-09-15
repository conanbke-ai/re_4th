'''
최빈값은 주어진 값 중에서 가장 자주 나오는 값을 의미합니다. 
    정수 배열 array가 매개변수로 주어질 때, 최빈값을 return 하도록 solution 함수를 완성해보세요. 
    최빈값이 여러 개면 -1을 return 합니다.

* 제한사항
- 0 < array의 길이 < 100
- -1000 < array의 원소 <= 1000
'''

from collections import Counter


def solution(array):
    # 1. 빈도수 계산
    counter = Counter(array)

    # 2. 가장 큰 빈도수 찾기
    max_freq = max(counter.values())

    # 3. 최빈값 후보 찾기
    modes = [key for key, val in counter.items() if val == max_freq]

    # 4. 최빈값이 여러 개면 -1 반환
    if len(modes) > 1:
        return -1
    else:
        return modes[0]


'''
예시 1)
def solution(array):
    while len(array) != 0:
        for i, a in enumerate(set(array)):
            array.remove(a)
        if i == 0: return a
    return -1

예시2)
def solution(array):
    answer = 0
    idx = [0] * 1001
    for i in array:
        idx[i] +=1
    if idx.count(max(idx)) >1:
        return -1
    return idx.index(max(idx))

예시3)
def solution(array):
    answer = 0
    ss = set(array)
    temp = []
    dic = {}
    for s in ss:
        dic[s] = array.count(s)
    data = list(sorted(dic.items(), key=lambda x: -x[1]))
    if len(data) == 1:
        return data[0][0]
    if data[0][1] == data[1][1]:
        return -1
    return data[0][0]


'''
