'''
두 정수 left와 right가 매개변수로 주어집니다. 
left부터 right까지의 모든 수들 중에서, 약수의 개수가 짝수인 수는 더하고, 약수의 개수가 홀수인 수는 뺀 수를 return 하도록 solution 함수를 완성해주세요.

* 제한 사항
    - 1 ≤ left ≤ right ≤ 1,000
'''

def solution(left, right):
    nums = range(left, right+1)
    cnts = []
    cnt = 0
    result = 0

    for num in nums:
        for i in range(1, num + 1):
            if num % i == 0:
                cnt += 1
        cnts.append(cnt)
        cnt = 0

    for x, y in zip(nums, cnts):
        if y % 2 == 0:
            result += x
        else:
            result -= x
    return result

'''
예시1)
def solution(left, right):
    answer = 0
    for i in range(left,right+1):
        if int(i**0.5)==i**0.5:
            answer -= i
        else:
            answer += i
    return answer

'- 제곱근이 정수이면 약수의 개수가 홀수이다. 이를 이용한 풀이.' 

예시2)
def solution(left, right):
    return sum(n if (n ** 0.5) % 1 else -n for n in range(left, right + 1))
'''