'''
두 정수 X, Y의 임의의 자리에서 공통으로 나타나는 정수 k(0 ≤ k ≤ 9)들을 이용하여 만들 수 있는 가장 큰 정수를 두 수의 짝꿍이라 합니다(단, 공통으로 나타나는 정수 중 서로 짝지을 수 있는 숫자만 사용합니다). 
X, Y의 짝꿍이 존재하지 않으면, 짝꿍은 -1입니다. 
X, Y의 짝꿍이 0으로만 구성되어 있다면, 짝꿍은 0입니다.

예를 들어, X = 3403이고 Y = 13203이라면, X와 Y의 짝꿍은 X와 Y에서 공통으로 나타나는 3, 0, 3으로 만들 수 있는 가장 큰 정수인 330입니다. 
다른 예시로 X = 5525이고 Y = 1255이면 X와 Y의 짝꿍은 X와 Y에서 공통으로 나타나는 2, 5, 5로 만들 수 있는 가장 큰 정수인 552입니다(X에는 5가 3개, Y에는 5가 2개 나타나므로 남는 5 한 개는 짝 지을 수 없습니다.)
두 정수 X, Y가 주어졌을 때, X, Y의 짝꿍을 return하는 solution 함수를 완성해주세요.

* 제한사항
    - 3 ≤ X, Y의 길이(자릿수) ≤ 3,000,000입니다.
    - X, Y는 0으로 시작하지 않습니다.
    - X, Y의 짝꿍은 상당히 큰 정수일 수 있으므로, 문자열로 반환합니다.
'''
from collections import Counter

def solution(X, Y):
    # 숫자 개수 세기
    counter_X = Counter(X)
    counter_Y = Counter(Y)

    # 공통 숫자 계산
    mate = []
    for num in '9876543210':  # 내림차순
        common = min(counter_X.get(num, 0), counter_Y.get(num, 0))
        mate.extend([num] * common)

    if not mate:
        return "-1"
    if mate[0] == '0':  # 모든 숫자가 0이면
        return "0"

    return ''.join(mate)

'''
예시1)
def solution(X, Y):
    answer = ''

    for i in range(9,-1,-1) :
        answer += (str(i) * min(X.count(str(i)), Y.count(str(i))))

    if answer == '' :
        return '-1'
    elif len(answer) == answer.count('0'):
        return '0'
    else :
        return answer

예시2)
from collections import Counter, defaultdict
def solution(X, Y):
    x, y = list(X), list(Y)
    arr = []
    answer = ""

    c_x, c_y = Counter(x) , Counter(y)
    for key in c_x.keys():
        if key in c_y.keys():
            arr.append((int(key), min(c_x[key], c_y[key])))

    if not arr:
        return "-1"
    elif len(arr) == 1 and arr[0][0] == 0:
        return "0"

    arr = sorted(arr, key = lambda x : x[0], reverse= True)

    for ar in arr:
        answer += str(ar[0]) * int(ar[1])
    return answer

예시3)
from functools import reduce
import re
def solution(X, Y):
    result = "".join(sorted(reduce(lambda result, i: result + i*min(X.count(i), Y.count(i)), map(str, range(10)), ""), reverse=True)) or "-1"
    return "0" if re.match(r"0+", result) else result
'''