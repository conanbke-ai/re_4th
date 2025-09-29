'''
이진수를 의미하는 두 개의 문자열 bin1과 bin2가 매개변수로 주어질 때, 두 이진수의 합을 return하도록 solution 함수를 완성해주세요.

* 제한 사항
    - return 값은 이진수를 의미하는 문자열입니다.
    - 1 ≤ bin1, bin2의 길이 ≤ 10
    - bin1과 bin2는 0과 1로만 이루어져 있습니다.
    - bin1과 bin2는 "0"을 제외하고 0으로 시작하지 않습니다.
'''

def solution(bin1, bin2):
    
    return format(int(bin1, 2) + int(bin2, 2), 'b')

'''
예시1)
def solution(bin1, bin2):
    answer = bin(int(bin1,2) + int(bin2,2))[2:]
    return answer

'- bin() : 2진수 변환
    [2:] - 앞의 접두사 '0b' 제외'

예시2)
def solution(bin1, bin2):
    answer = 0
    bin1_size = len(bin1)
    bin2_size = len(bin2)

    sum = 0

    for i in bin1:
        sum += int(i) * (2 ** (bin1_size - 1))
        bin1_size -= 1

    for i in bin2:
        sum += int(i) * (2 ** (bin2_size - 1))
        bin2_size -= 1

    answer = str(bin(sum))[2:]
    return answer

예시3)
def solution(bin1, bin2):
    bin1, bin2 = bin1[::-1], bin2[::-1]
    i, carry = 0, 0
    output = ""
    while i < len(bin1) or i < len(bin2) or carry:
        op1 = bin1[i] if i < len(bin1) else '0'
        op2 = bin2[i] if i < len(bin2) else '0'
        result = int(op1) + int(op2) + carry
        output += str(result % 2)
        carry = result // 2
        i += 1

    return output[::-1]

'- 비트마다 더하기'
'''